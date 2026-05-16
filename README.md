# Blender Asset Packager Minimal

This is a **small Codex-first sample repository** for spec-driven + agent-driven implementation.

The code itself is not the point.
This repository shows how to structure specs, contracts, and validation
so that an AI agent can implement a bounded task without widening scope.
The working CLI is the minimum needed to make that structure observable.

It is intentionally small and pure Python so it can run from Windows Command Prompt without Blender,
Maya, or any other DCC application.

## What "spec-driven" means here

In this repository, spec-driven implementation means that the expected behavior is written before the AI edits code.

The task spec defines:

- what the tool should do
- what it must not do
- what files or behavior are in scope
- what validation commands must pass

The spec is not just documentation after implementation.
It is the primary input that constrains the implementation work.

## What "agent-driven" means here

In this repository, agent-driven implementation means that an AI coding agent reads the repository-local instructions and performs a bounded implementation task.

The agent is expected to read:

- project-level rules
- task-scoped specifications
- forbidden behavior
- validation commands
- expected reporting format

The important point is that the agent is not asked to freely redesign the tool.
Humans define the work boundary and review criteria.
The agent performs implementation work inside that boundary.

## Minimal working example

The sample task is a Blender-oriented asset packaging CLI:

1. scan an asset tree and create a manifest
2. validate the manifest
3. create a dry-run export plan
4. leave actual file copy as a later high-risk task

## What is real, and what is only a sample?

Read [`SAMPLE_SCOPE.md`](SAMPLE_SCOPE.md) first.

In short:

- **Implemented and executable**: `src/assetpack/`, `scripts/validate.py`, `scripts/check_boundaries.py`, `tests/`, `run_demo.bat`.
- **Definitions used to guide agents**: `AGENTS.md`, `PROJECT_CONTRACT.md`, `WORKFLOW.md`, `tasks/*/spec.md`.
- **Example data only**: `examples/shot001/`. The `.blend`, `.obj`, `.glb`, and `.png` files are placeholder files for path/manifest tests. They are not parsed as real Blender files.
- **Not implemented yet**: `tasks/010_safe_copy_todo/spec.md` describes a future high-risk export/copy task.


## Start here

This repository is meant to demonstrate **spec-driven + agent-driven implementation**, not just a small CLI.

Read in this order:

1. [`README.md`](README.md) - repository overview
2. [`SAMPLE_SCOPE.md`](SAMPLE_SCOPE.md) - what is implemented vs illustrative
3. [`TUTORIAL.md`](TUTORIAL.md) - what to run and what each step proves
4. [`tasks/000_scan_validate_plan/spec.md`](tasks/000_scan_validate_plan/spec.md) - implemented Spec Card
5. [`tasks/010_safe_copy_todo/spec.md`](tasks/010_safe_copy_todo/spec.md) - future agent-driven task
6. [`NEXT_STEPS.md`](NEXT_STEPS.md) - where to go after completing the tutorial
7. [`RELATED_WORK.md`](RELATED_WORK.md) - comparison with similar spec-driven / agent-driven projects

## After the tutorial

After you have run the demo and read `TUTORIAL.md`, read [`NEXT_STEPS.md`](NEXT_STEPS.md).
It explains how this minimal sample connects to comparison experiments, real project adoption,
and representative spec-driven / agent-driven tools.

For a side-by-side comparison with related projects (Spec Kit, cc-sdd, OpenSpec, and others),
see [`RELATED_WORK.md`](RELATED_WORK.md).

`NEXT_STEPS.md` and `RELATED_WORK.md` are for human readers. Agents do not need to read them unless explicitly asked.

## Quick start on Windows cmd.exe

```bat
cd blender-asset-packager-minimal
python -m venv .venv
.venv\Scripts\activate.bat
python -m pip install -U pip
python -m pip install -e .[dev]

python -m assetpack scan examples\shot001 --out work\shot001.manifest.json
python -m assetpack validate work\shot001.manifest.json
python -m assetpack plan-export work\shot001.manifest.json --out-root work\export --dry-run --out work\shot001.export_plan.json
python scripts\validate.py --profile fast
```

Without installation, use:

```bat
run_demo.bat
```

## Codex usage

Ask Codex to read:

1. `AGENTS.md`
2. `PROJECT_CONTRACT.md`
3. `WORKFLOW.md`
4. one task spec under `tasks/`
5. `SAMPLE_SCOPE.md` when there is ambiguity about what is real vs illustrative

Codex should implement only the current task and run the requested validation profile.

## Claude Code migration

`CLAUDE.md` imports `AGENTS.md`. Claude-specific reviewer guidance is under `.claude/agents/`.
The repository contract and task specs remain tool-agnostic.
