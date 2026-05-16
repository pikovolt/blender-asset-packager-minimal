from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .paths import ensure_within, resolved, safe_relative_path

SCHEMA_VERSION = 1


def scan_tree(root: str | Path) -> dict[str, Any]:
    root_path = resolved(root)
    if not root_path.is_dir():
        raise ValueError(f"input root is not a directory: {root_path}")

    files: list[dict[str, Any]] = []
    for path in sorted(root_path.rglob("*")):
        if not path.is_file():
            continue
        rel = ensure_within(root_path, path).relative_to(root_path).as_posix()
        files.append({
            "path": rel,
            "ext": path.suffix.lower(),
            "size": path.stat().st_size,
        })

    return {
        "schema_version": SCHEMA_VERSION,
        "root": str(root_path),
        "files": files,
    }


def write_json(data: dict[str, Any], output_path: str | Path) -> None:
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True) + "\n"
    path.write_text(text, encoding="utf-8")


def load_json(path: str | Path) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError("manifest must be a JSON object")
    return data


def validate_manifest(manifest: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    if manifest.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"schema_version must be {SCHEMA_VERSION}")

    root_value = manifest.get("root")
    if not isinstance(root_value, str):
        errors.append("root must be a string")
        root_path = None
    else:
        root_path = resolved(root_value)
        if not root_path.is_dir():
            errors.append(f"root does not exist: {root_path}")

    files = manifest.get("files")
    if not isinstance(files, list):
        errors.append("files must be a list")
        return errors

    seen: set[str] = set()
    for index, item in enumerate(files):
        if not isinstance(item, dict):
            errors.append(f"files[{index}] must be an object")
            continue

        rel_value = item.get("path")
        if not isinstance(rel_value, str):
            errors.append(f"files[{index}].path must be a string")
            continue

        try:
            rel = safe_relative_path(rel_value)
        except ValueError as exc:
            errors.append(str(exc))
            continue

        if rel in seen:
            errors.append(f"duplicate path: {rel}")
        seen.add(rel)

        if root_path is not None:
            source = root_path / rel
            try:
                ensure_within(root_path, source)
            except ValueError as exc:
                errors.append(str(exc))
            if not source.is_file():
                errors.append(f"missing source file: {rel}")

    return errors


def build_export_plan(manifest: dict[str, Any], out_root: str | Path) -> dict[str, Any]:
    errors = validate_manifest(manifest)
    if errors:
        raise ValueError("manifest is invalid: " + "; ".join(errors))

    source_root = resolved(str(manifest["root"]))
    output_root = resolved(out_root)
    operations: list[dict[str, str]] = []

    for item in manifest["files"]:
        rel = safe_relative_path(str(item["path"]))
        src = ensure_within(source_root, source_root / rel)
        dst = ensure_within(output_root, output_root / rel)
        operations.append({
            "op": "copy",
            "path": rel,
            "src": str(src),
            "dst": str(dst),
        })

    return {
        "dry_run": True,
        "out_root": str(output_root),
        "operations": operations,
    }
