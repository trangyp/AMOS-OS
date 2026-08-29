---
title: SOTA Agent Skill / Workflow / Orchestration Repos
type: wiki
source: 11_KNOWLEDGE/LLM_WIKI/raw/SOTA_AGENT_SKILL_WORKFLOW_REPOS_2026_08_25.md
date: '2026-08-25'
epistemic_class: DERIVED
provenance: Synthesized from web_search and README snippets
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: SOTA_AGENT_SKILL_WORKFLOW_REPOS_2026_08_25.md
  scope: AMOS_knowledge
tags:
- llm-wiki
- sota
- agent-skills
- agent-workflows
- orchestration
- github
- llm-wiki-synthesis
---

# SOTA Agent Skill / Workflow / Orchestration Repositories

**Epistemic class:** `DERIVED`  
**Raw source:** [[SOTA_AGENT_SKILL_WORKFLOW_REPOS_2026_08_25]]

## Top pick for skill security / registry hardening

`tech-leads-club/agent-skills` (5.1k★)  
- Designed for safe, validated skill distribution.
- Aligns directly with AMOS guardrail and provenance concerns: lockfiles, content hashing, Snyk scanning, path/symlink guards, audit trails.
- Best candidate for importing skill-lifecycle controls.

## Top pick for production multi-agent orchestration

`microsoft/agent-framework` (13.1k★)  
- Multi-language, production-grade agent and workflow framework.
- Supports durable, observable, graph-based multi-agent patterns: sequential, concurrent, handoff, group collaboration.
- Best candidate for hardening AMOS `amos-workflow-runner` and runtime orchestration.

## Top pick for repository-native agentic CI/CD

`github/gh-aw` — GitHub Agentic Workflows  
- Markdown-defined workflows compiled to GitHub Actions.
- Sandboxed, scoped permissions, `safe-outputs`, threat detection, cost controls.
- Best candidate for publishing AMOS workflows into a CI/CD execution layer.

## Specialized candidates

| Repo | Strength | AMOS fit |
|------|----------|----------|
| `yuzhaopeng-up/skill-framework` | 208-skill inventory, L0–L4 classification, YAML templates | Skill taxonomy and governance checklists |
| `agent-skill-harbor` | Org-wide catalog, recommended/discouraged/prohibited governance | Enterprise skill discovery and provenance |
| `gfernandf/agent-skill-registry` | Declarative capabilities/skills, machine-readable catalogs | Standardized capability vocabulary |
| `yiheng8023/agent-skills-curated` | Reviewed, provenance-tracked, release manifests | Curated third-party skill ingestion |
| `microsoft/conductor` | Deterministic YAML workflows, Jinja2 routing, parallel execution | Multi-agent workflow definition language |
| `agentenv/agentflow` | Large-scale agent graphs, optimization rounds, multi-target execution | Scale-out workflow harnesses |

## Synthesis for AMOS

The strongest near-term integration path is:

1. Adopt `tech-leads-club/agent-skills` guardrail patterns for the `skill_guardrail_checker` pipeline.
2. Study `microsoft/agent-framework` orchestration primitives to enhance `amos-workflow-runner` and `amos-agent-orchestrator`.
3. Mirror `github/gh-aw` for execution-boundary controls and cost governance.

**Confidence ceiling:** 0.85 (derived from README claims and star counts, not empirical benchmarks).

---
**MOC:** [[LLM_WIKI_MOC]]

## 2026-08-29 update

Follow-up scan expanded the candidate pool with five additional high-value repositories.

### Best skill marketplaces and runtimes

| Repo | Strength | AMOS fit |
|------|----------|----------|
| `wuyifeishu/nexus-agentos` | Universal agent runtime + 64 built-in skills + MCP + TUI | Harden AMOS runtime and `.devin/skills` discovery/install |
| `zjunlp/SkillNet` | 500K+ skills, 5-dimension scoring, orchestration, MCP | Import skill-evaluation and relationship-graph tooling |
| `songfang/AgentSkillOS` | 90K+ skills, DAG orchestration, skill tree, GUI | Cross-check skill-retrieval and DAG-composition models |

### Best markdown/native orchestration and registry formats

| Repo | Strength | AMOS fit |
|------|----------|----------|
| `nuryslyrt/ORPHEUS` | Natural-language → multi-skill pipeline; typed contracts; filesystem only | Validate AMOS workflow and contract design patterns |
| `gfernandf/agent-skill-registry` | Declarative capabilities/skills, machine-readable catalogs | Standardize AMOS capability vocabulary and registry export |
| `kai98k/agent-skills-registry` | Skill bundles with `SKILL.md`, semver, push/pull CLI | Align skill-bundle packaging with `amos-skill-builder` |
| `yepengfan/agent-registry` | Claude Code native agent/skill/orchestrator registry | Compare install/routing conventions for agents |
| `Rainnystone/skill-orchestration-system` | Local skill packs, vault isolation, workspace routing | Reduce prompt-pollution for large `.devin/skills` trees |
| `tavianm/aidd-framework` | 31 skills, 3 agents, Claude/Cursor/Copilot builds | Reference multi-format skill distribution |

### Updated near-term integration priorities

1. **SkillNet** for the largest evaluatable skill corpus and community scoring.
2. **AgentOS** if AMOS needs a runtime marketplace with MCP integration.
3. **ORPHEUS** to benchmark AMOS workflow contracts and markdown-first orchestration.
4. **agent-skill-registry** / **agent-skills-registry** for vocabulary and bundle standards.

Raw capture: [[SOTA_AGENT_SKILL_WORKFLOW_REPOS_2026_08_29]]

**Confidence ceiling:** 0.80 (derived from README claims; not independently benchmarked).

## 2026-08-29 | SkillNet deep-dive

Read the `main` branch README of `zjunlp/SkillNet` and mapped it to AMOS operations.

### Verified shape

- PyPI package: `skillnet-ai` (Python 3.10+, MIT).
- CLI + Python SDK.
- Public skill search/install are credential-free.
- Requires `API_KEY`, `BASE_URL`, `SKILLNET_MODEL` for create/evaluate/analyze/orchestrate.
- Optional extras: `skillnet-ai[graph]` and `skillnet-ai[orchestrate]`.

### Integration points for AMOS

1. **Skill discovery → `amos-skill-builder` / `07_SKILLS`**
   - Use `skillnet search <intent>` and `skillnet download <url>` to find public skills that AMOS has not yet ingested.
   - Feed downloaded `SKILL.md` files into `skill-check` and the RSCF canonicalizer before adding them to the vault.

2. **Skill evaluation → `skill-check` and guardrails**
   - SkillNet scores safety, completeness, executability, maintainability, and cost awareness.
   - AMOS can map these dimensions to H/M/L and `rscf.state` before promoting a skill.

3. **Skill graph / composition → `amos-routing-audit` and `amos-workflow-runner`**
   - `skillnet analyze` returns `compose_with` and `depend_on` relationships.
   - These can augment AMOS workflow dependencies and agent capability bindings.

4. **Orchestration → `amos-agent-orchestrator` and `amos-workflow-runner`**
   - `skillnet orchestrate` returns a selected skill set and a downstream agent prompt.
   - AMOS could use this as an external handoff generator for tasks where no local skill is optimal.

5. **MCP integration → `amos-mcp-connector` (if it exists) or new skill**
   - SkillNet has an MCP server; a new `amos-skillnet-mcp` skill could let AMOS agents query it at runtime.

### Open questions / gaps

- The 500K+ skill count is an unverified README claim.
- `orchestrate` currently supports only the `sciatlas` scene in the first release.
- Cost/evaluation scoring methodology is not detailed in the README.
- License is MIT, but each downloaded skill may have its own license — AMOS must scan per-skill licenses before ingestion.

### Recommended next step

Clone a small SkillNet skill (e.g., a `pdf` or `rag` skill) and run the AMOS `skill-check` + `skill_rscf_canonicalizer` pipeline on it as an end-to-end ingestion trial.

Raw source: [[SKILLNET_README_2026_08_29]]

## 2026-08-29 | ORPHEUS deep-dive

Read the `main` branch README of `nuryslyrt/ORPHEUS` and mapped it to AMOS operations.

### Verified shape

- Filesystem-only runtime — no pip/npm/docker; skills are markdown files.
- Install is `cp -r ORPHEUS/skill/ ~/.claude/skills/orpheus/`.
- Meta-orchestrator + 4 experts (Builder, Runner, Doctor, Auditor, Surgeon) + 7 workers.
- Generated `.orpheus/` contains `system.yaml`, `registry.yaml`, `orchestrator/SKILL.md`, `experts/{name}/SKILL.md + contract.yaml`, `workers/{name}/SKILL.md + contract.yaml`, `scripts/`, `logs/`.
- Decision-level logging: every decision records WHAT, WHY, and confidence.
- Error chain preservation with full root-cause-to-symptom YAML traces.
- Target runtime: Claude Code / coding agent.

### Integration points for AMOS

1. **Markdown-first orchestration → `amos-workflow-builder` and `amos-routing-audit`**
   - ORPHEUS proves that a single coding agent can run orchestrator/expert/worker hierarchies with only markdown files.
   - AMOS can compare its `.devin/skills` / `.devin/agents` / `.devin/workflows` against the ORPHEUS `orchestrator/SKILL.md` + `contract.yaml` pattern.

2. **Typed contracts → `amos-skill-builder` references/**
   - `contract.yaml` defines typed I/O between skills.
   - AMOS could add a `contract/` or `contract.yaml` artifact to skills that need composable boundaries.

3. **Decision logs → `amos-observability-driven-harness-evolution-rscf` and audit trail**
   - ORPHEUS logs `question / options_considered / chosen / reasoning / confidence`.
   - AMOS `AGENT_VALIDATION_REPORT` and `LLM_WIKI_LOG` already capture some of this; can be aligned to the same schema.

4. **Meta-expert roles → `amos-agent-orchestrator`**
   - Builder/Runner/Doctor/Auditor/Surgeon are natural-role templates that could become AMOS agents or workflow modes.

### Open questions / gaps

- 0 stars on the repo at time of scan; no community validation.
- README claims are not empirically benchmarked (no SWE-bench, no eval harness shown).
- Claude Code-specific; portability to Devin / other coding agents unproven.
- Security and provenance controls (content hashing, guardrails, sandboxing) are not described.

### Recommended next step

Clone `nuryslyrt/ORPHEUS`, inspect the `skill/` directory structure, and compare one generated `.orpheus/` system to an AMOS workflow to see if any contract/role patterns should be imported.

Raw source: [[ORPHEUS_README_2026_08_29]]

## 2026-08-29 | SkillOpt deep-dive

Read the `main` branch README of `microsoft/SkillOpt` and mapped it to AMOS skill training and governance.

### Verified shape

- PyPI package: `skillopt` (Python 3.10+, MIT).
- CLI `skillopt`, WebUI `skillopt_webui`, and offline `skillopt-sleep`.
- Training loop: rollout → reflect → aggregate → select → update → evaluate.
- Optimizer model turns scored rollouts into bounded `add / delete / replace` edits on a single skill document.
- Candidate edits accepted only when they strictly improve a held-out validation score.
- Built-in backends: OpenAI, Azure, Claude, Qwen, MiniMax, Codex CLI, Claude Code CLI, Cursor, Copilot; `openai_compatible` fallback.
- Six built-in benchmarks; project page, paper arXiv:2605.23904, and docs in `docs/`.

### Integration points for AMOS

1. **Skill quality evolution → `amos-skill-builder` and `skill-check`**
   - `best_skill.md` artifact produced after validation is the same object AMOS stores as `SKILL.md`.
   - AMOS can adopt the rollout-reflect-edit-evaluate loop as a governed `skill-check --evolve` mode, producing a promoted `best_skill.md` only after a held-out gate passes.

2. **Held-out validation gates → `amos-validation-pipeline` and promotion gates**
   - SkillOpt rejects edits that do not improve a held-out score. This matches `PROMOTION_GATES` and the `amos-validation-levels` contract.
   - Could add `skillopt_eval` as a `validation_status` step before a skill moves `draft → staging → production`.

3. **Multi-backend / multi-harness validation → `amos-agent-orchestrator` and `amos-cli-failure-process-diagnostics-rscf`**
   - SkillOpt tests the same skill across direct chat, Codex, Claude Code, Cursor. AMOS can run `skill-check` against multiple agent harnesses before releasing.

4. **SkillOpt-Sleep offline self-evolution → `amos-evolution-loop` and `amos-brain-model-integration`**
   - Nightly `harvest → mine → replay → consolidate` with validation. AMOS could schedule this over `.devin/skills/` using the `enforcement_trust_contract` and `AMOS_AUTONOMOUS_EVOLUTION_LAYER` already in `cosmo-brain/`.

### Open questions / gaps

- README claims 52 cells best/tied-best and +23.5 point lifts — not independently benchmarked by AMOS.
- The 2026 dates in the README are future-dated relative to current AMOS context; source freshness should be flagged.
- License is MIT, but the paper and benchmarks are Microsoft-copyrighted; ingestion of example skills should respect per-file license.

### Recommended next step

Install `skillopt` in a sandbox, run a built-in benchmark on one AMOS skill (e.g., `amos-llm-wiki`), and compare the `best_skill.md` output to the current `SKILL.md` to see if validation-gated evolution improves SOTA score.

Raw source: [[SKILLOPT_README_2026_08_29]]

## 2026-08-29 | SkillFlow deep-dive

Read the `main` branch README of `linxuhao/SkillFlow` and mapped it to AMOS workflow and runtime governance.

### Verified shape

- PyPI package: `skillflow-py` (Python 3.12+, MIT).
- CLI tools: `skillflow-lint`, `skillflow-run`, `skillflow-convert`, `skillflow-mcp`.
- YAML-defined DAG pipelines; engine handles traversal, loops, retries, recovery.
- Capability-gated I/O: each step declares inputs/outputs; the engine generates dedicated `write_*` / `create_*` / `edit_*` / `append_*` tools so the agent cannot access undeclared files.
- Human-in-the-loop by design: approve/reject-with-feedback checkpoints are first-class nodes.
- Immutable SQLite audit trace keyed by `step_instance_id`.
- Framework Mode (engine drives agent step-by-step) and Runner Mode (external agent drives pipelines via CLI/MCP).
- MCP transport `skillflow-mcp` for Claude Code / opencode with zero agent-side code.

### Integration points for AMOS

1. **Deterministic workflow runner → `amos-workflow-runner` and `amos-routing-audit`**
   - SkillFlow's YAML DAG executor with linting and replay is a reference for hardening AMOS `.devin/workflows` parsing.
   - The `amos-workflow-runner` can adopt a `workflow.yaml` lint step before execution.

2. **Capability-gated I/O → `amos-skill-builder` contracts and `amos-routing-audit`**
   - SkillFlow's `write_<slot>` / `edit_<slot>` pattern strengthens the `CONTRACT_TEMPLATE.yaml` added earlier.
   - AMOS skill contracts can declare file slots and the runtime can expose only those tools.

3. **Human-in-the-loop checkpoints → `amos-promotion-gates` and `amos-authority-canon`**
   - First-class approve/reject nodes match AMOS `PROMOTION_GATES` and `L7_AUTHORITY` for human escalation before irreversible effects.

4. **Immutable audit trace → `amos-observability-driven-harness-evolution-rscf`**
   - The `step_instance_id` keyed SQLite trace is a concrete reference for AMOS execution provenance and `AGENT_VALIDATION_REPORT`.

5. **MCP transport → `amos-mcp-connector` / `amos-llm-wiki`**
   - `skillflow-mcp` can be mounted as an MCP server, letting AMOS agents run SkillFlow pipelines without new code.

### Open questions / gaps

- 3 stars on the repo at time of scan; no broad community validation.
- README claims deterministic replay, but reproducibility across model providers is not empirically verified by AMOS.
- The `edit_*` staging logic is subtle; importing it requires careful testing against AMOS's existing `skill_operations_enhancer.py`.

### Recommended next step

Install `skillflow-py` in a sandbox, convert one AMOS workflow (e.g., `amos-skill-builder-workflow.md`) into a SkillFlow YAML, and run `skillflow-lint` to see how much of the AMOS workflow contract can be expressed in SkillFlow's DAG schema.

Raw source: [[SKILLFLOW_README_2026_08_29]]
