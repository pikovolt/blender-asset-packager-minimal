# RELATED_WORK.md

This document lists representative repositories and projects related to spec-driven and agent-driven development, with explicit comparison to this sample.

The goal is not to recommend the "best" one. The goal is to help readers understand **where this sample sits in the landscape** and **what to read next based on their own situation**.

---

## How to Read This Document

Each entry follows the same format:

```text
Name / link
Scale     : approximate size or maturity
Goal      : what the project is trying to deliver
Audience  : who the project is designed for
Difference from this sample : explicit contrast in 1–3 lines
```

This sample positions itself as a **minimal observation sample**.
That positioning is repeated in the comparisons below so the contrast stays consistent.

---

## 1. GitHub Spec Kit

- Repository: <https://github.com/github/spec-kit>
- Scale: Industry-standard SDD framework with extensive templates, CLI, and 30+ agent integrations
- Goal: Provide a complete spec-driven development workflow (`constitution.md` → `spec.md` → `plan.md` → `tasks.md` → implementation) usable across many coding agents
- Audience: Teams and individuals who want a ready-to-adopt SDD framework for real projects
- Difference from this sample:
  - Spec Kit **is** the framework. This sample is a small observation harness whose elements correspond to parts of Spec Kit.
  - Spec Kit has a `specify` CLI, slash commands, and `.specify/memory/` directory. This sample has none of those.
  - For real-project adoption, Spec Kit is a stronger starting point. For first understanding the **concept**, this sample is smaller and faster to read end-to-end.

## 2. cc-sdd

- Repository: <https://github.com/gotalab/cc-sdd>
- Scale: Multi-agent SDD harness with 17 skills × 8 coding agents (Claude Code, Codex, Cursor, Copilot, Windsurf, OpenCode, Gemini CLI, Antigravity); installed via `npx cc-sdd@latest`
- Goal: Turn approved specs into long-running autonomous implementation. Reproduce the Kiro IDE SDD flow across many agent platforms.
- Audience: Developers who want a ready-made multi-agent SDD harness installable into an existing project
- Difference from this sample:
  - cc-sdd is the **closest neighbor** to this sample in framing ("a minimal, adaptable SDD harness").
  - However, cc-sdd is an **installer that injects skills/commands into your repo**. This sample is a **fixed, self-contained observation repo** with example code and an intentionally unimplemented task for comparative experiments.
  - cc-sdd assumes you are starting or already in a real project. This sample assumes you are still learning the concepts.

## 3. OpenSpec

- Repository: <https://github.com/Fission-AI/OpenSpec>
- Scale: Lightweight SDD framework, MIT license, supports 20+ AI assistants via slash commands
- Goal: Provide a per-change workflow (`propose` → `apply` → `archive`) with `proposal.md` / `specs/` / `design.md` / `tasks.md` artifacts. Brownfield-first design.
- Audience: Solo developers and small teams who want a lighter alternative to Spec Kit, especially when modifying existing codebases
- Difference from this sample:
  - OpenSpec splits per-change work into separate folders. This sample treats one task as one `tasks/<id>/spec.md`.
  - OpenSpec's `propose`/`apply`/`archive` flow is closer to a real workflow tool. This sample stops at the observation stage.
  - OpenSpec is positioned as a lighter alternative to Spec Kit. This sample is even lighter — it does not provide a workflow tool at all.

## 4. agents.md (specification)

- Site: <https://agents.md/>
- Repository: <https://github.com/openai/agents.md>
- Scale: An open specification, not a framework. Stewarded by the Agentic AI Foundation (Linux Foundation) since December 2025.
- Goal: Define the conventions of `AGENTS.md` as a tool-agnostic README for coding agents
- Audience: Anyone authoring `AGENTS.md` for their own project
- Difference from this sample:
  - agents.md is the **convention**. This sample is one **concrete example** of using that convention together with `CLAUDE.md`, `PROJECT_CONTRACT.md`, and small Spec Cards.
  - For writing your own `AGENTS.md` from scratch, read the agents.md site first. For seeing how `AGENTS.md` works alongside other artifacts in a small project, read this sample.

## 5. BMAD-METHOD

- Repository: <https://github.com/bmad-code-org/BMAD-METHOD>
- Scale: Multi-role agent framework (Analyst / PM / Architect / Developer / QA, etc.) targeting medium-to-large workflows
- Goal: Provide a complete role-based agent orchestration system, including PRD, architecture documents, and sharded epics
- Audience: Teams that want a heavier process with distinct agent roles, often integrated with Spec Kit's templates
- Difference from this sample:
  - BMAD assumes a multi-role workflow from the start. This sample assumes a solo or 1–3 person setting and only escalates to Planner/Implementer/Reviewer for `risk: high` tasks.
  - BMAD's artifacts (PRD, architecture, epics) require a substantial up-front investment. This sample's artifacts are minimal task-level Spec Cards.

## 6. Kiro IDE

- Site: <https://kiro.dev/>
- Scale: A dedicated AI development environment built around spec-driven development with custom agents
- Goal: Provide an integrated experience for moving from prototypes to production work through executable specs, steering files, and IDE/CLI support
- Audience: Developers who want a paid, integrated environment rather than a self-assembled toolset
- Difference from this sample:
  - Kiro is an **IDE/environment**, not a repo template. This sample is a repo template only.
  - The cc-sdd project (entry 2) is partly an open-source reproduction of Kiro's workflow across multiple agents. This sample is even further upstream — it shows the concepts before any tool wraps them.

## 7. Anthropic Claude Code (native capabilities)

- Documentation: <https://code.claude.com/docs/>
- Scale: First-party tooling from Anthropic; `CLAUDE.md` + subagents + hooks + skills + tasks
- Goal: Provide Claude Code's built-in mechanisms for context, role separation, and workflow control
- Audience: Claude Code users who want to use only the native primitives (no external SDD framework on top)
- Difference from this sample:
  - Claude Code's native capabilities are the **primitives**. This sample uses `CLAUDE.md` and `.claude/agents/spec-reviewer.md` as a small illustration of how those primitives can be wired together.
  - For production Claude Code workflows, the Anthropic documentation is the authoritative source. This sample is only a minimal example.

## 8. OpenAI Codex (native capabilities)

- Documentation: <https://developers.openai.com/codex/>
- Scale: First-party tooling from OpenAI; `AGENTS.md` + subagents + customization
- Goal: Provide Codex's built-in mechanisms for project context, agent roles, and operational guardrails
- Audience: Codex users who want to use only the native primitives
- Difference from this sample:
  - Symmetric to entry 7. This sample uses `AGENTS.md` and `.codex/agents/spec-reviewer.toml` as a small illustration.
  - For real Codex usage, read the official documentation first.

---

## Where This Sample Sits

| Axis | Position of this sample |
|---|---|
| Scale | Smallest among the projects listed above. Roughly 30 files, pure Python standard library only. |
| Goal | Observation, not adoption. The sample exists to make the underlying ideas inspectable in one sitting. |
| Audience | Readers who have not yet committed to any specific framework and want to understand the concepts first. |
| Domain | DCC / asset-packaging flavor in the example. The majority of public SDD samples target web applications instead. |

In short:

- If the reader's question is **"what is spec-driven / agent-driven development, in the smallest concrete form?"** → this sample is appropriate as a first stop.
- If the reader's question is **"how do I introduce SDD into a real project?"** → Spec Kit, cc-sdd, or OpenSpec are stronger starting points than continuing with this sample.
- If the reader's question is **"what conventions does AGENTS.md actually require?"** → read the agents.md specification directly.

This sample is not in competition with the projects above.
It is intentionally positioned **upstream** of them: a place to look at the concepts before choosing a framework.

---

## Notes on This List

- All scale figures and feature descriptions are accurate as of the time this document was written. Frameworks in this space evolve quickly; verify current state at each project's official page before adoption.
- The list is not exhaustive. Other notable projects include `wshobson/agents` (large agent/skill collection for Claude Code), Tessl, and various community SDD presets/extensions. They are omitted here because they target scales or audiences far from this sample's scope.
- For research-level context on whether context files like `AGENTS.md` actually help, see Gloaguen et al. (2026), "Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?" (arXiv:2602.11988). The takeaway is that developer-written, minimal context files give a small positive effect, while auto-generated verbose ones can hurt — which is consistent with the design choices in this sample.
