# SAMPLE_SCOPE.md

This file explains the boundary between **working implementation**, **agent-control definitions**, and **illustrative sample material**.

## Purpose of this repository

This repository is not a full Blender add-on and does not call Blender Python APIs.
It is a minimal harness for comparing:

- prompt-only implementation
- spec-driven implementation
- agent-driven implementation with small task specs and mechanical checks

The domain is Blender-style asset packaging, but the implementation is pure Python.

## Implemented and executable

These files are part of the working sample:

| Path | Status | Meaning |
|---|---|---|
| `src/assetpack/cli.py` | implemented | command-line interface for `scan`, `validate`, and `plan-export` |
| `src/assetpack/manifest.py` | implemented | scans file trees, writes/loads JSON, validates manifests, builds dry-run export plans |
| `src/assetpack/paths.py` | implemented | path normalization and escape checks |
| `scripts/validate.py` | implemented | validation profile runner |
| `scripts/check_boundaries.py` | implemented | simple forbidden-token boundary guard |
| `tests/test_assetpack.py` | implemented | pytest tests for scan, validation, and dry-run export planning |
| `run_demo.bat` | implemented | Windows cmd.exe demo path |

## Agent-control definitions

These files are not application runtime code. They are control surfaces for Codex/Claude-style work:

| Path | Status | Meaning |
|---|---|---|
| `AGENTS.md` | definition | tool-agnostic working instructions, usable by Codex-style agents |
| `CLAUDE.md` | definition | Claude Code entry file that imports `AGENTS.md` |
| `.codex/agents/spec-reviewer.toml` | definition | optional Codex reviewer role sample |
| `.claude/agents/spec-reviewer.md` | definition | optional Claude Code reviewer role sample |
| `PROJECT_CONTRACT.md` | definition | allowed/forbidden operations and validation profiles |
| `WORKFLOW.md` | definition | default vs strict workflow |
| `STATE.yaml` | definition | current sample state |

## Task specs

| Path | Status | Meaning |
|---|---|---|
| `tasks/000_scan_validate_plan/spec.md` | implemented spec | describes the implemented low-risk task |
| `tasks/000_scan_validate_plan/result.md` | result log | records the completed sample result |
| `tasks/010_safe_copy_todo/spec.md` | future spec | intentionally not implemented; used as a high-risk comparison task |

## Example data

`examples/shot001/` is test fixture data, not production data.

The files under `examples/shot001/` are placeholders. Their extensions are Blender/interchange-oriented,
but their contents are not valid production assets.

Examples:

- `*.blend`: placeholder path fixture, not a valid Blender binary file
- `*.obj`: placeholder path fixture, not a valid OBJ mesh
- `*.glb`: placeholder path fixture, not a valid glTF binary
- `*.png`: placeholder path fixture, not a valid texture image

The application currently scans file paths and file sizes only. It does **not** parse Blender files,
load meshes, inspect materials, validate texture contents, or call `bpy`.

## What is intentionally not implemented

The following are future tasks, not current behavior:

- actual file copying/exporting
- overwrite handling
- extension-specific validation
- Blender `bpy` integration
- `.blend` content inspection
- dependency graph extraction from Blender scenes
- packaging into a Blender add-on

## How to interpret correctness

Correctness in this minimal sample means:

1. the CLI runs from Windows cmd.exe
2. file-tree scanning is deterministic
3. manifest validation rejects unsafe relative paths
4. export planning is dry-run only
5. boundary checks and pytest pass
6. the repository structure shows how Codex/Claude can be guided by task specs

It does not mean the repository is a complete Blender pipeline tool.
