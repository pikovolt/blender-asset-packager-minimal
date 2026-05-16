# NEXT_STEPS.md

This document is a **guide to the next phase** for readers who have finished reading `TUTORIAL.md` and have confirmed the sample's operation via `run_demo.bat` or an equivalent command.

This sample is a **minimal observation sample** for spec-driven + agent-driven development.
It is neither a finished tool nor an industry-standard framework itself.
Here, what was confirmed in this sample is connected to representative external tools and real-project operations.

---

## 1. What Was Confirmed with This Sample

At the point of completing this sample, the following scope has been confirmed.

| Perspective | What was confirmed with this sample |
|---|---|
| Location of specs | Spec Cards (`tasks/*/spec.md`) can be placed inside the repo and used as input per unit of work |
| Correspondence between spec and implementation | Must / Must not / Done can be mapped to CLI, tests, and validation commands |
| Mechanical checks | Simple forbidden-token inspection is possible with `scripts/check_boundaries.py` |
| Project contract | Allowed / Forbidden / Path policy can be consolidated in `PROJECT_CONTRACT.md` |
| Workflow branching | low-risk and high-risk can be separated using the `risk` field in task specs |
| Tool independence | `AGENTS.md` can serve as the common definition and `CLAUDE.md` as a thin adapter |
| Observability | Artifacts can be verified as `work/*.json` |

In other words, what was experienced up to this point is the **minimal flow of translating a natural-language requirement into specs, contracts, mechanical checks, and observable artifacts inside the repo**.

---

## 2. What This Sample Intentionally Omits

Because this sample is introductory, it omits a significant number of elements required in real projects.
The omissions themselves are not defects — they are a design choice to keep the observation points small.

### 2.1 Formalizing Spec Descriptions

This sample uses short Spec Cards with Must / Must not / Done.
In real projects, the following are added as needed.

- Requirements descriptions such as EARS format
- Acceptance scenarios
- Non-functional requirements
- Expected behavior on error
- Compatibility, performance, and logging policies

However, all of these do not need to be included from the start.
The purpose of this sample is to gain a feel for **first fixing one task as a small spec**.

### 2.2 Separating Spec → Plan → Tasks

This sample is self-contained with a single `tasks/<id>/spec.md`.
In larger projects, the following separation may be used.

```text
spec.md   What to build / why it is needed
plan.md   How to implement / data structures / technical constraints
tasks.md  Implementation order / checklist / dependencies
```

The `tasks/010_safe_copy_todo/spec.md` in this sample is the minimal form before introducing this separation.

### 2.3 Verifiability of Constitution / Project Contract

`PROJECT_CONTRACT.md` plays a role close to a constitution, but its content is minimal.
In real projects, principles are oriented toward being "verifiable and concrete."

```text
Bad example:  Write high-quality code
Good example: File output is restricted to under --out-root; paths that go outside must fail
```

### 2.4 Operating Agent Separation

`WORKFLOW.md` describes the division of Planner / Implementer / Reviewer, but actual context isolation and handoff formats are not implemented.
For full-scale operation, the following must be defined.

- Files the Planner reads
- The plan format the Planner outputs
- Files the Implementer is permitted to edit
- The diff and validation log the Reviewer examines
- Whether each role continues in the same conversation or starts in a fresh context

### 2.5 Automating State Management

`STATE.yaml` is a manually maintained note of the current position.
When running multiple tasks sequentially, a mechanism is needed to update the state after task completion and select the next task candidate.

### 2.6 Domain-Specific Boundary Checks

`scripts/check_boundaries.py` is a simple string inspection.
In real projects, checks are expanded to match the domain.

For Blender/DCC, examples include:

- Save-related APIs such as `bpy.ops.wm.save_as_mainfile`
- File delete and overwrite APIs
- Arbitrary external process execution
- Network transmission
- Correspondence between scene mutation and dry-run

---

## 3. How to Proceed Next

After completing this sample, there are broadly three directions to take.

### Direction A: Run Comparative Experiments with the Same Minimal Sample

**Purpose:** Observe how closely the agent you are using follows the Spec Card.

`tasks/010_safe_copy_todo/spec.md` is intentionally left unimplemented.
Have it implemented in three ways and compare the results.

#### A-1. Prompt-only

```text
Add an export copy feature to this CLI.
Make it safe, and write tests too.
```

#### A-2. Spec-driven

```text
Read PROJECT_CONTRACT.md and tasks/010_safe_copy_todo/spec.md,
and implement only within that scope.
```

#### A-3. Agent-driven / strict workflow

```text
Read AGENTS.md, PROJECT_CONTRACT.md, WORKFLOW.md, and tasks/010_safe_copy_todo/spec.md.
This task is high-risk, so proceed in order: Planner → Implementer → Reviewer.
```

The points to examine in the comparison are not the completeness of the code itself, but the following.

| Perspective | Where to look |
|---|---|
| Whether scope was expanded | `git diff` |
| Whether it diverged into Blender integration | imports / changed files |
| Whether delete / subprocess / network were introduced | `scripts/check_boundaries.py` |
| Whether output outside out-root is rejected | tests |
| Whether overwrite rejection is present | tests |
| Whether validation results are reported | agent final report |

### Direction B: Port This Structure to Your Own Project

**Purpose:** Introduce a minimal spec-driven + agent-driven skeleton into a real project.

What can be reused is primarily the **structure**.
The application implementation, forbidden tokens, and validation profiles must be replaced without exception.

Minimal checklist for porting:

- [ ] Rewrite `PROJECT_CONTRACT.md` to the Allowed / Forbidden for your own project
- [ ] Replace `FORBIDDEN` in `scripts/check_boundaries.py` with items specific to your domain
- [ ] Align the validation command in `AGENTS.md` with your project's tests
- [ ] Replace `tasks/000_*/spec.md` with your first small implementation task
- [ ] Use Strict workflow only for high-risk tasks
- [ ] Keep `STATE.yaml` updated as a note of the current position

There is no need to include EARS, `plan.md` separation, and automated state management all at once from the start.
As with this sample, it is realistic to begin with just **Spec Card + implementation + mechanical check**.

### Direction C: Migrate to Representative External Tools

**Purpose:** Operate on a more systematized framework.

After grasping the concepts with this sample, migrate to external tools as needed.
"External tools" here are not all industry standards in a strict sense — they are **standard candidates, representative examples, and reference implementations**.

| Tool / category | Characteristics | Relationship to this sample |
|---|---|---|
| GitHub Spec Kit | An SDD-type tool with a constitution → spec → plan → tasks → implementation flow | A development path from `PROJECT_CONTRACT.md` / Spec Card |
| Claude Code | Work context can be structured with `CLAUDE.md`, subagents, hooks, skills, etc. | A development path from `CLAUDE.md` / `.claude/agents/` |
| Codex + AGENTS.md | Repo-specific work conventions are provided via `AGENTS.md` | The basic form of this sample |
| Lightweight SDD such as OpenSpec | Framework-independent, spec-centric approach | A closely related approach for small-scale projects |
| BMAD / Kiro family | Agent/SDD-type systems designed for multiple roles and multiple artifacts | A comparison target at medium scale and above |

---

## 4. Correspondence Table Between This Sample and Representative External Tools

Even if file names do not exactly match, the roles are often closely related.
When migrating, understanding the correspondence by **role** rather than by name is easier.

| This sample | Role | Closest concept in external tools |
|---|---|---|
| `AGENTS.md` | Common agent instructions | AGENTS.md convention / Codex project instructions |
| `CLAUDE.md` | Entry point for Claude Code | Claude Code project memory |
| `PROJECT_CONTRACT.md` | Project principles | Constitution-type files in Spec Kit |
| `tasks/<id>/spec.md` | Small Spec Card | Simplified version of a feature spec in Spec Kit |
| `WORKFLOW.md` | Default / Strict branching | Agent workflow / subagent orchestration |
| `.claude/agents/spec-reviewer.md` | Review-dedicated agent | Claude Code custom subagent |
| `.codex/agents/spec-reviewer.toml` | Review definition for Codex | Codex custom subagent |
| `scripts/check_boundaries.py` | Boundary check | Simplified version of hooks / validation gate |
| `scripts/validate.py` | Validation profile runner | Simplified version of test runner / consistency check |
| `STATE.yaml` | Current position note | Minimal sample of memory / task state |

Notes:

- `scripts/validate.py` is not the analysis command from Spec Kit itself.
  In this sample, it is a lightweight runner that executes tests and boundary checks together.
- `PROJECT_CONTRACT.md` is a simplified constitution, but in real projects the principles need to be made more verifiable.
- `NEXT_STEPS.md` is a learning guide for humans. It is not a work instruction to be continuously fed to Codex / Claude Code.

---

## 5. Reading List

References for moving to the next phase.
Primary sources and explanatory articles are listed separately.

### Primary Sources

- AGENTS.md: https://agents.md/
- OpenAI Codex AGENTS.md guide: https://developers.openai.com/codex/guides/agents-md
- OpenAI Codex customization: https://developers.openai.com/codex/concepts/customization
- OpenAI Codex subagents: https://developers.openai.com/codex/subagents
- Claude Code documentation: https://code.claude.com/docs/
- Claude Code memory: https://code.claude.com/docs/en/memory
- Claude Code subagents: https://code.claude.com/docs/en/sub-agents
- Claude Code hooks: https://code.claude.com/docs/en/hooks
- GitHub Spec Kit repository: https://github.com/github/spec-kit

### Explanatory and Comparative Articles

- Addy Osmani, "How to write a good spec for AI agents"
- Martin Fowler / Birgitta Böckeler, articles related to SDD

Explanatory articles are useful, but for grounding tool specifications, prioritize primary sources.

For a side-by-side comparison of representative spec-driven and agent-driven projects (Spec Kit, cc-sdd, OpenSpec, BMAD, Kiro, and others) and how each one differs from this sample, see [`RELATED_WORK.md`](RELATED_WORK.md).

---

## 6. Graduation Criteria for This Sample

The purpose of this sample is for the reader to become able to do at least one of the following.

1. Place a document equivalent to `PROJECT_CONTRACT.md` in their own project
2. Write a Spec Card for one task
3. Judge the workflow branching between low-risk and high-risk
4. Think through a mechanical check equivalent to `scripts/check_boundaries.py` for their own domain
5. When looking at Spec Kit / Claude Code / AGENTS.md and similar tools, understand them by mapping to the structure of this sample

If even one of these has been achieved, the role of this sample is essentially complete.
Proceed next to whichever of Direction A / B / C applies.