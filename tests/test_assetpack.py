from __future__ import annotations

from pathlib import Path

from assetpack.manifest import build_export_plan, scan_tree, validate_manifest


REPO_ROOT = Path(__file__).resolve().parents[1]
EXAMPLE_ROOT = REPO_ROOT / "examples" / "shot001"


def test_scan_tree_finds_example_assets() -> None:
    manifest = scan_tree(EXAMPLE_ROOT)
    paths = {item["path"] for item in manifest["files"]}
    assert "assets/char_hero/model/hero_model.blend" in paths
    assert "assets/prop_sword/model/sword_model.obj" in paths
    assert validate_manifest(manifest) == []


def test_validate_rejects_parent_escape(tmp_path: Path) -> None:
    manifest = {
        "schema_version": 1,
        "root": str(tmp_path),
        "files": [{"path": "../evil.txt", "ext": ".txt", "size": 1}],
    }
    errors = validate_manifest(manifest)
    assert any(".." in error for error in errors)


def test_export_plan_is_dry_run_and_inside_out_root(tmp_path: Path) -> None:
    manifest = scan_tree(EXAMPLE_ROOT)
    out_root = tmp_path / "export"
    plan = build_export_plan(manifest, out_root)
    assert plan["dry_run"] is True
    assert plan["operations"]
    for operation in plan["operations"]:
        dst = Path(operation["dst"]).resolve()
        assert dst.relative_to(out_root.resolve())
