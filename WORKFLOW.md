# WORKFLOW.md

## Default workflow

1. Read the project contract.
2. Read `SAMPLE_SCOPE.md` to understand which parts are implemented vs illustrative.
3. Read the current task spec.
4. Implement only that task.
5. Run the requested validation profile.
6. Report changed files, validation results, and risks.

## Strict workflow

Use only when the task is marked high risk.

1. Planner: refine the task and risks without editing code.
2. Implementer: make the smallest code change.
3. Boundary guard: run `python scripts\check_boundaries.py`.
4. Reviewer: compare the diff against the spec and contract.

## Current sample status

- `000_scan_validate_plan`: implemented
- `010_safe_copy_todo`: intentionally not implemented; used as a later high-risk comparison task

Do not treat `export-safe` as proof that filesystem export/copy behavior is safe yet.
When `010_safe_copy_todo` is implemented, `export-safe` must be strengthened to test filesystem-output safety.
