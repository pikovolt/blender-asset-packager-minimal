from __future__ import annotations

from pathlib import Path


def resolved(path: str | Path) -> Path:
    return Path(path).expanduser().resolve()


def ensure_within(root: str | Path, target: str | Path) -> Path:
    root_path = resolved(root)
    target_path = resolved(target)
    try:
        target_path.relative_to(root_path)
    except ValueError as exc:
        raise ValueError(f"path escapes root: {target_path} not under {root_path}") from exc
    return target_path


def safe_relative_path(path: str) -> str:
    candidate = Path(path)
    if candidate.is_absolute():
        raise ValueError(f"absolute manifest path is not allowed: {path}")
    if ".." in candidate.parts:
        raise ValueError(f"manifest path may not contain '..': {path}")
    return candidate.as_posix()
