# Spec Card: 010_safe_copy_todo

```yaml
task_id: 010_safe_copy_todo
risk: high
touch: filesystem_output
validation: export-safe
requires_planner: true
requires_reviewer: true
status: intentionally_unimplemented_agent_exercise
```

## Purpose of this spec

This is the **agent-driven exercise task**.
It is intentionally not implemented in the zip so that Codex or Claude Code can be asked to implement it from a bounded specification.

Current sample note: `scripts/validate.py --profile export-safe` is present as a named profile, but currently aliases `fast`. When this task is implemented, `export-safe` must be strengthened so that the Done condition below is meaningful for filesystem output.

Use it to compare:

- prompt-only implementation: "add export copy"
- spec-driven implementation: this file + `PROJECT_CONTRACT.md` + validation
- agent-driven implementation: planner / implementer / reviewer split

## Goal

Add an `export` command that copies files according to a previously generated dry-run export plan.

Example intended command:

```bat
python -m assetpack export work\shot001.export_plan.json --out-root work\export
```

## Allowed files

The implementer may edit only:

- `src/assetpack/cli.py`
- `src/assetpack/manifest.py`
- `src/assetpack/paths.py`
- `tests/test_assetpack.py`
- `scripts/validate.py` if the `export-safe` profile needs a stronger check

## Must

- Require a prior dry-run export plan.
- Copy only under the provided `--out-root`.
- Reject destination paths that escape `--out-root`.
- Reject overwrite unless `--overwrite` is explicit.
- Preserve relative paths from the export plan.
- Use temporary test directories in validation.
- Add at least one test for successful copy.
- Add at least one test for overwrite rejection or path escape rejection.

## Must not

- Delete files.
- Follow paths outside `--out-root`.
- Add network access.
- Add subprocess execution.
- Require Blender or `bpy`.
- Parse `.blend`, `.obj`, `.glb`, or `.png` file contents.

## Done

- `python scripts\validate.py --profile export-safe` passes.
- The reviewer finds no violation of `PROJECT_CONTRACT.md`.
- The final report lists changed files, validation commands, skipped checks, and remaining risks.

## What this task is meant to prove

This task should show whether an agent can:

1. read a small task spec,
2. avoid widening scope into Blender integration,
3. implement a filesystem-output feature safely,
4. add tests around dangerous boundaries, and
5. report validation results instead of just claiming completion.
