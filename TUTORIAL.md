# TUTORIAL.md

This tutorial exists to explicitly state **what this repository does and what it is a sample for observing**.

The purpose of this sample is not to provide a finished Blender tool.
The purpose is to **observe how far a small implementation can be controlled using spec-driven + agent-driven approaches**.

---

## 0. What You Can Observe with This Sample

| What to observe | Where to look / run | What you can confirm |
|---|---|---|
| Whether the minimal CLI runs | `run_demo.bat` | scan → validate → dry-run plan → test all pass |
| Whether the implementation is readable from the spec | `tasks/000_scan_validate_plan/spec.md` | Must / Must not / Done correspond to the implementation |
| Whether artifacts are observable | `work/*.json` | manifest and export plan are generated |
| Whether mechanical checks work | `scripts/check_boundaries.py` | Forbidden tokens can be inspected |
| Whether there are unimplemented tasks to hand to an agent | `tasks/010_safe_copy_todo/spec.md` | A comparative experiment implementing safe copy is possible |
| Whether there is an entry point for Codex/Claude migration | `AGENTS.md`, `CLAUDE.md` | Common specs and tool-specific adapters can be separated |

---

## 1. First, Confirm What Is Already Implemented

What is implemented in this sample is the following.

```text
src/assetpack/      A working Python CLI
scripts/            Validation commands
tests/              pytest
run_demo.bat        Demo for Windows cmd.exe
```

On the other hand, the following are **definitions for controlling agent work**.

```text
AGENTS.md
CLAUDE.md
PROJECT_CONTRACT.md
WORKFLOW.md
tasks/*/spec.md
.codex/
.claude/
```

Additionally, `examples/shot001/` is a placeholder for testing.
Files with extensions `.blend`, `.obj`, `.glb`, and `.png` are present, but they are not valid data readable by Blender.
This CLI does not analyze file contents — it handles **only paths, extensions, and sizes**.

---

## 2. Running the Baseline

Navigate to the extracted folder in Windows Command Prompt.

```bat
cd blender_asset_packager_min_v3
run_demo.bat
```

On success, the following sequence is executed.

```text
1. Scan examples\shot001
2. Generate work\shot001.manifest.json
3. Validate the manifest
4. Generate work\shot001.export_plan.json
5. Run boundary check and pytest
```

The expected final output is roughly as follows.

```text
boundary check OK
3 passed
```

### What You Can Observe Here

What this step confirms is that **the minimal CLI actually runs, prior to any spec management**.
In other words, this repo is not merely a Markdown template — it contains an observable implementation.

---

## 3. Inspecting the Generated Artifacts

After running `run_demo.bat`, the following files are generated.

```text
work/shot001.manifest.json
work/shot001.export_plan.json
```

In `shot001.manifest.json`, you can review the list of files found in the input tree.

Points to examine:

```text
files[].path
files[].ext
files[].size
```

In `shot001.export_plan.json`, no copy is performed yet — only the plan for a future copy is recorded.

Points to examine:

```text
dry_run: true
operations[].src
operations[].dst
```

### What You Can Observe Here

What this confirms is that **the results of the implementation are observable as JSON artifacts**.
Even when an agent performs the work, you can verify "what was accomplished" via files rather than conversation.

---

## 4. Examining the Correspondence Between the Spec Card and the Implementation

The implemented task is as follows.

```text
tasks/000_scan_validate_plan/spec.md
```

Examine how the `Must` / `Must not` / `Done` entries in this Spec Card correspond to the implementation.

| Spec requirement | Primary location | How to verify |
|---|---|---|
| Runs via `python -m assetpack` from Windows cmd.exe | `src/assetpack/__main__.py`, `cli.py` | `run_demo.bat` |
| Standard library only | `pyproject.toml`, `src/assetpack/*` | Inspect dependencies |
| Deterministic JSON | `sort_keys=True` in `manifest.py` | Inspect generated JSON |
| Reject manifest paths containing `..` | `paths.py`, `validate_manifest()` | `tests/test_assetpack.py` |
| Export planning is dry-run only | `build_export_plan()` | `work/*.export_plan.json` |
| No copy/delete | `manifest.py`, `check_boundaries.py` | boundary check |

### What You Can Observe Here

What this confirms is that **natural-language specs are translated down into implementation, tests, and validation commands**.
This is the minimal sample portion of "spec-driven" development.

---

## 5. Running the Mechanical Check Standalone

```bat
python scripts\check_boundaries.py
```

This is a lightweight check to detect whether dangerous processing fragments have been introduced into application code.

Examples currently checked:

```text
import socket
import subprocess
shutil.rmtree
os.remove
os.unlink
commandPort
cmds.file(save=True
```

To run a more comprehensive check, execute the following:

```bat
python scripts\validate.py --profile fast
```

### What You Can Observe Here

What this confirms is that **boundaries can be enforced mechanically, rather than relying solely on prompting "don't do this"**.

The boundary check in this sample is minimal, but in DCC tool implementations it can be extended to checks such as:

```text
- Whether output destinations go outside the permitted directory
- Whether delete / overwrite are introduced without a spec
- Whether Blender/Maya dependencies are introduced
- Whether scene mutation APIs are used without authorization
```

---

## 6. Examining the Agent-Driven Experimental Task

The unimplemented comparative task is as follows.

```text
tasks/010_safe_copy_todo/spec.md
```

This task is intentionally left unimplemented.
The reason is to use it as an experimental subject for **spec-driven + agent-driven implementation** with Codex or Claude Code.

The content to be implemented in this task is a safe copy based on the dry-run export plan.

The risk is that file output is involved.
Therefore it is marked `risk: high`.

### What You Can Observe Here

What this task is intended to confirm is whether the agent can adhere to the following:

```text
- Implement only safe copy, without expanding into Blender integration
- Do not output outside out-root
- Reject overwrite by default
- Do not add delete / network / subprocess
- Add pytest
- Pass export-safe validation
```

---

## 7. Example Prompt for Passing to Codex

A minimal example prompt for having Codex implement `010_safe_copy_todo`:

```text
Read AGENTS.md, PROJECT_CONTRACT.md, WORKFLOW.md, SAMPLE_SCOPE.md, and tasks/010_safe_copy_todo/spec.md.

Implement only tasks/010_safe_copy_todo/spec.md.
Do not add Blender, bpy, network, subprocess, delete, or scene mutation behavior.
Run:
python scripts\validate.py --profile export-safe

End with changed files, validation results, skipped checks, and remaining risks.
```

For a more agent-driven separation, use the following:

```text
Use strict workflow for tasks/010_safe_copy_todo/spec.md.

1. Planner: read the spec and identify implementation risks. Do not edit files.
2. Implementer: make the smallest code/test changes for the spec only.
3. Run python scripts\validate.py --profile export-safe.
4. Reviewer: review the diff against PROJECT_CONTRACT.md and the task spec.
5. Stop. Do not choose the next task.
```

### What You Can Observe Here

What this confirms is that **work instructions can be anchored to specs inside the repo rather than in conversation memory**.
Also, by separating Planner / Implementer / Reviewer, you can experiment with applying heavier treatment only to high-risk tasks.

---

## 8. Transitioning to Claude Code

For Claude Code, use the following as entry points:

```text
CLAUDE.md
.claude/agents/spec-reviewer.md
```

`CLAUDE.md` is a thin adapter; the substance resides in `AGENTS.md` / `PROJECT_CONTRACT.md` / `WORKFLOW.md` / `tasks/*/spec.md`.

In other words, this sample demonstrates a structure where tool-specific files are kept thin and common specs are reused.

---

## 9. Perspectives for Comparing Against Prompt-Only Implementation

To use this sample for a comparative experiment, compare the following two patterns:

### A. Prompt-only

```text
Add an export copy feature to this CLI.
Make it safe, and write tests too.
```

### B. Spec-driven + agent-driven

```text
Read AGENTS.md / PROJECT_CONTRACT.md / WORKFLOW.md / tasks/010_safe_copy_todo/spec.md,
and implement only within that scope.
```

Perspectives for comparison:

| Perspective | Where to look |
|---|---|
| Whether features outside the spec were added | git diff |
| Whether delete / subprocess / network were introduced | `scripts/check_boundaries.py` |
| Whether overwrite rejection is present | tests |
| Whether output outside out-root is rejected | tests |
| Whether it diverged into Blender integration | changed files / imports |
| Whether the completion report includes validation results | agent final report |

---

## 10. The Scope of What This Sample Can Claim as "Possible"

What this repo demonstrates is:

```text
- A small CLI implementation can be derived from a Spec Card
- Implemented and unimplemented tasks can be separated within the repo
- Dangerous boundaries can be offloaded to PROJECT_CONTRACT.md and check_boundaries.py
- AGENTS.md for Codex and CLAUDE.md for Claude can coexist
- Only high-risk tasks need to be subject to Planner / Implementer / Reviewer separation
```

Conversely, what this repo alone does not demonstrate:

```text
- Blender add-on implementation
- bpy API usage
- .blend content analysis
- Genuine asset dependency resolution
- Large-scale parallel agent execution
- Complete safety guarantees
```

---

## 11. Conclusion

This sample is not a template for a finished tool — it is a **minimal observation sample for spec-driven + agent-driven development**.

The key points to examine are not the volume of code, but the following:

```text
Spec Card → implementation → JSON artifacts → validation → next task spec → agent implementation experiment
```

If this flow can be confirmed, the purpose of this repo is fulfilled.

---

## 12. What to Read Next

After completing this tutorial, read [`NEXT_STEPS.md`](NEXT_STEPS.md).

`NEXT_STEPS.md` covers the following:

```text
- What was confirmed with this sample
- What must be intentionally added in a real project
- Comparative experiments: prompt-only / spec-driven / agent-driven
- Minimal checklist for porting to your own project
- Correspondence with representative external tools such as Spec Kit / Claude Code / AGENTS.md
```

Note: `NEXT_STEPS.md` is a guide for humans.
It is not a work instruction to be continuously fed to Codex / Claude Code.