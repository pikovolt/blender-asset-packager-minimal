# AGENTS.md

## Read first

1. `PROJECT_CONTRACT.md`
2. `WORKFLOW.md`
3. `SAMPLE_SCOPE.md`
4. The current task spec under `tasks/<task_id>/spec.md`

## Default rule

- Implement only the current task.
- Do not widen scope.
- Do not choose successor tasks.
- Prefer small diffs.
- Run the validation profile requested by the task spec.

## Validation

Default command:

```bat
python scripts\validate.py --profile fast
```

For filesystem-output tasks, also run:

```bat
python scripts\check_boundaries.py
```

## Report format

End with:

- changed files
- validation commands and results
- skipped checks, if any
- remaining risks

## Escalate to strict workflow when touching

- filesystem output that writes or overwrites files
- destructive delete
- external process execution
- network access
- DCC scene mutation


## Human-facing guide

`NEXT_STEPS.md`, `RELATED_WORK.md` and `SDD_ADD_BACKGROUND.md` are post-tutorial guides for human readers.
Do not treat them as implementation instruction unless the user explicitly asks.
