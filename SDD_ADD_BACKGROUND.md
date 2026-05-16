# Spec-Driven and Agent-Driven Development: Background and Context

---

## 1. The Starting Point: Problems That Emerged When LLMs First Entered Coding

Between 2022 and 2023, as code generation via GitHub Copilot and ChatGPT became widespread, the prevailing development style was "write a prompt, paste the returned code."

In February 2025, Andrej Karpathy (co-founder of OpenAI) gave this style a name: **vibe coding**. The phrase — "fully give in to the vibes and forget that the code even exists" — described a workflow of generating and revising code through high-level natural-language instructions alone.

This approach carried structural problems.

As LLM-based coding agents went mainstream in 2024–2025, three failure modes emerged. The first was **intent drift**: underspecified instructions such as "add login" caused the model to choose defaults that did not match the team's actual intent. The second was **context decay**: once a codebase exceeded the agent's effective context window, the agent would forget earlier decisions and produce contradictory implementations. The third was **unverifiable output**: without explicit acceptance criteria, there was no basis for judging whether the agent's code was correct.

In September 2025, Fast Company reported what it called the "vibe coding hangover," documenting senior engineers experiencing "development hell" caused by AI-generated code.

---

## 2. The First Response: The Emergence of AGENTS.md and CLAUDE.md

Tool vendors responded to the cost of re-explaining the same context on every session with a structural solution.

OpenAI's Codex implemented automatic reading of an `AGENTS.md` file placed inside the repository. Like a `README.md`, this plain text file communicates codebase navigation conventions, test commands, and standard project practices to the agent without manual re-entry.

`AGENTS.md` emerged from collaborative efforts across multiple organizations — OpenAI Codex, Google Jules, and others — and in December 2025 was transferred to the **Agentic AI Foundation (AAIF)**, a directed fund under the Linux Foundation, to be maintained as an open standard.

Codex walks downward from the project root to the current working directory, concatenating each `AGENTS.md` it finds. Files discovered later override earlier instructions, enabling subdirectory-level overrides in monorepos.

At this stage, however, only the "context persistence" problem was solved; scope control remained unaddressed.

---

## 3. The Rise of Spec-Driven Development: Writing the Spec First

After `AGENTS.md` solved context persistence, the next problem was the absence of any definition of what to build before implementation began.

Spec-Driven Development (SDD) treats the specification as the source of truth and code as a derived, verified secondary artifact. Instead of "add photo sharing," the instruction becomes: "Users can upload JPEG or PNG files up to 10 MB. Photos are stored in S3 with user-ID-prefixed keys." Only then does implementation begin.

The intellectual lineage of this approach draws on TDD (Test-Driven Development) and BDD (Behavior-Driven Development).

According to Thoughtworks' analysis, SDD technically means "explicitly defining the external behavior of the target software" — input/output mappings, preconditions, postconditions, and so on. It goes beyond a Product Requirements Document (PRD) by incorporating structured prompts and explicit technical constraints.

A well-formed Spec Card is said to define six elements: outcomes, scope boundaries, constraints, prior decisions, task breakdown, and verification criteria.

---

## 4. The Rise of PROJECT_CONTRACT.md: Cross-Task Constraints

It became clear that per-task specs alone were insufficient. A cross-task definition of "what must never be done in this repository" was needed.

The "constitution" file found in GitHub Spec Kit and BMAD serves this role. Its typical content takes the form of EARS-style declarations: "The system shall use TypeScript strict mode. The system shall reject PRs that lower test coverage." With these in place, an agent can read a requirement, generate code, and write the tests to verify it — all without guessing at scope.

A key insight gained from practice: **specificity is decisive** for a constitution to be effective.

- Bad example: "Write high-quality code."
- Good example: "File output is restricted to paths under `--out-root`. Paths that escape this root must fail."

---

## 5. The Rise of Workflow Branching: Separating Work by Risk Level

Mixing work that agents could handle autonomously with work requiring mandatory human review became a recognized problem.

Acceptance criteria must be **Executable** — anything that cannot be run is an opinion, not a criterion. They must be **Binary** — "reasonably fast" or "clean code" are not criteria. They must also be **Independent** — bundling "tests pass AND coverage is 85% AND no network calls" into one criterion makes it impossible to know what failed.

The typical implementation pattern became branching by a `risk` field:

```text
low-risk:   Planner → Implementer → automated verification → done
high-risk:  Planner → [human review] → Implementer → Reviewer → [human review] → done
```

File deletion, subprocess execution, and network transmission are canonical examples of high-risk operations.

---

## 6. The Rise of Agent Separation: Role Specialization

The structural problem of a single agent both implementing and reviewing its own work became recognized.

AgentMesh (2025) proposed separating four specialized agents: Planner, Coder, Debugger, and Reviewer. The Planner decomposes user requests into subtasks; the Coder implements them; the Debugger tests and fixes them; the Reviewer validates the final output against requirements and assesses quality. Research on systems such as ChatDev suggests that this kind of role separation outperforms single-agent approaches on complex tasks.

In this structure, explicitly restricting which files each agent may read and which it may modify became the standard approach for preventing role boundary violations.

---

## 7. The Current State: Tool Proliferation and Convergence

The SDD tool landscape expanded rapidly from the GitHub Spec Kit announcement in July 2025 through the release of AWS Kiro and into early 2026.

| Tool | Scale and characteristics |
|---|---|
| GitHub Spec Kit | Open source; full constitution → spec → plan → tasks → implementation flow |
| AWS Kiro | IDE-integrated commercial environment; positions itself as "prototype to production" |
| cc-sdd | Mid-scale multi-agent harness; 17 skills × 8 agent platforms |
| OpenSpec | Lightweight; oriented toward brownfield (existing codebase) projects |
| BMAD | Multi-role, large-scale process: Analyst / PM / Architect / Developer / QA |

Effectiveness has also been challenged by empirical research. A study by ETH Zurich and LogicStar.ai (arXiv:2602.11988, February 2026), evaluating multiple coding agents and LLMs, found that context files tend to reduce task success rates compared to providing no repository context, while also increasing inference cost by over 20%.

The study's interpretation: LLM-generated context files hurt performance, whereas developer-written, minimal context files show a small positive effect.

---

## 8. Summary and the Emerging Future

**The arc in a single sentence:**

As work delegation to LLM agents expanded, the need to convert "ambiguous instructions" into "verifiable structures" became progressively clearer — a staged historical process.

| Period | Problem solved | Concept that emerged |
|---|---|---|
| 2022–2023 | Cost of re-explaining the same context each session | AGENTS.md / CLAUDE.md |
| 2023–2024 | Scope drift; absence of a definition of done | Spec Card (Must / Must not / Done) |
| 2024– | Cross-task constraint definition | PROJECT_CONTRACT.md / Constitution |
| 2024–2025 | Risk-based separation of work types | Workflow branching |
| 2025– | Quality degradation from mixed agent roles | Agent separation (Planner / Implementer / Reviewer) |

**An emerging paradigm on the horizon:**

The next shift becoming visible in 2025–2026 is called **Context Engineering**.

Where prompt engineering focuses on *how to phrase instructions*, context engineering focuses on designing the entire information environment in which a model operates — memory, retrieved documents, tool definitions, conversation history. Patrick Debois introduced the concept "Context is the new Code" at AI Engineer London 2024, framing a Context Development Lifecycle (CDLC) that mirrors the traditional Software Development Lifecycle (SDLC).

The arXiv paper "Spec-Driven Development: From Code to Contract in the Age of AI" (February 2026) draws the core distinction: traditional specifications are read by humans, while SDD specifications **execute as validation gates**.

This direction represents a shift from static documents to executable constraints — pointing toward a future in which designing context and specifications, rather than writing code, becomes the central engineering activity.

---

**Primary Sources**

| Type | Reference |
|---|---|
| Academic paper | arXiv:2602.11988 (ETH Zurich, 2026-02): Empirical evaluation of AGENTS.md effectiveness |
| Academic paper | arXiv:2602.00180 (2026-01): Comprehensive guide to SDD |
| Official documentation | https://agents.md/ — AGENTS.md specification |
| Official documentation | https://openai.com/index/introducing-codex/ — Codex announcement |
| Official documentation | https://developers.openai.com/codex/guides/agents-md — AGENTS.md implementation spec |
| Industry analysis | Thoughtworks (2025-12): SDD in practice |
| Industry analysis | InfoQ (2026-01): SDD as executable architecture |