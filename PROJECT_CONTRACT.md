# PROJECT_CONTRACT.md

## Supported environment

- OS: Windows 10/11 cmd.exe first
- Python: 3.11+
- Runtime: pure Python
- Blender dependency: none
- Maya dependency: none

## Domain boundary

This is a Blender-oriented asset-packaging **harness sample**.
It does not parse `.blend` files and does not use `bpy`.
Example files under `examples/` are path fixtures only.

## Allowed operations

- Read files under the requested input root.
- Write generated JSON files under `work/` or an explicitly provided output path.
- Create an export plan in dry-run mode.

## Forbidden application behavior

- Do not delete files.
- Do not overwrite asset files.
- Do not execute external commands from application code.
- Do not access the network.
- Do not mutate DCC scenes.
- Do not require Blender or Maya to run the current sample.

## Path policy

- Normalize paths with `pathlib`.
- Reject manifest file paths that are absolute or escape the manifest root.
- Reject destination paths that escape `--out-root`.
- Dry-run is required before any future copy operation.

## Validation profiles

- `fast`: boundary scan + pytest
- `export-safe`: currently aliases `fast` in this intentionally incomplete sample; when `tasks/010_safe_copy_todo` is implemented, this profile must be strengthened with filesystem-output safety checks
