# Spec Card: 000_scan_validate_plan

```yaml
task_id: 000_scan_validate_plan
risk: low
touch: read_only_manifest_and_dry_run_plan
validation: fast
requires_planner: false
requires_reviewer: false
```

## Goal

Create a small CLI that scans an example Blender-style asset tree, writes a manifest,
validates the manifest, and creates a dry-run export plan.

## Scope note

The example `.blend`, `.obj`, `.glb`, and `.png` files are placeholder path fixtures.
The implementation must not parse these formats or call Blender.

## Must

- Run from Windows cmd.exe using `python -m assetpack`.
- Use only Python standard library in application code.
- Generate deterministic JSON output.
- Reject absolute manifest file paths.
- Reject manifest file paths containing `..`.
- Keep export planning dry-run only.

## Must not

- Delete files.
- Copy files.
- Overwrite asset files.
- Execute external commands from application code.
- Access the network.
- Require Blender, Maya, or other DCC applications.

## Done

- `python scripts\validate.py --profile fast` passes.
- `run_demo.bat` can be used as the simple Windows demo path.
