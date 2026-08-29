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

## 2026-08-29 | AgentFactory deep-dive

Read the `master` branch README of `zzatpku/AgentFactory` and mapped it to AMOS self-evolution and subagent governance.

### Verified shape

- ACL 2026 System Demonstrations paper; 63 stars.
- Three-phase lifecycle: Install (create subagents) → Self-Evolve (refine on feedback) → Deploy (export as Python modules).
- Meta-Agent decomposes problems, allocates subsets of tools, iteratively refines subagents.
- Skill levels: Meta Skills (`create_subagent`, `run_subagent`, `modify_subagent`, ...), Tool Skills (`web_search`, `web_reading`, `browser_automation`, `shell_command`), Subagent Skills (dynamically generated Python).
- Subagents are saved as Python code + `SKILL.md` documentation, portable to LangChain, AutoGen, Claude Code.
- Workspace Manager isolates execution environments per task.
- Requires Python 3.12, Playwright, Flask, `LLM_*` keys; cannot install on current host Python 3.9.6.

### Integration points for AMOS

1. **Executable subagent library → `amos-agent-orchestrator` and `amos-integrated-agent`**
   - AgentFactory stores successful solutions as Python code. AMOS could store canonical subagents as `.devin/agents/` JSON and `SKILL.md` pairs after `amos-validation-pipeline`.

2. **Meta Skills → `amos-skill-builder` and `amos-agent-systems-master`**
   - The meta-agent primitives (`create/run/modify/list/view`) are a natural expansion of `amos-agent-orchestrator` subagent dispatch and `skill_operations_enhancer.py`.

3. **Self-evolve feedback loop → `amos-evolution-loop` and `amos-brain-model-integration`**
   - Retrieve → detect limitations → modify → validate. This maps directly to the `GMEF` evolution gate and the `AMOS_AUTONOMOUS_EVOLUTION_LAYER` already in `cosmo-brain/`.

4. **Workspace Manager → `amos-boundary-scope-master` and `amos-memory-immune-system`**
   - Isolated per-task workspaces prevent a subagent from corrupting the shared skill library. AMOS can enforce the same via project directories and `memory/short_term/` vs `memory/long_term/`.

5. **SKILL.md + Python deployment → `amos-skill-builder` bundle format**
   - AMOS skill bundles can already include `SKILL.md`; adding a `subagent.py` or `scripts/` Python artifact would make AMOS skills deployable like AgentFactory modules.

### Open questions / gaps

- 63 stars; ACL demo but not yet battle-tested.
- README claims 57% token reduction; not independently benchmarked by AMOS.
- Requires multiple API keys and Playwright; not all AMOS users will have these.
- The `SKILL.md` format in AgentFactory is not documented in the README; would need to inspect `prompt4cc.txt` or code.

### Recommended next step

Clone `zzatpku/AgentFactory` and inspect `prompt4cc.txt` and a saved `SKILL.md` to compare the AgentFactory bundle format with the AMOS `amos-skill-builder` bundle spec.

Raw source: [[AGENTFACTORY_README_2026_08_29]]

## 2026-08-29 | Agent Skill Registry deep-dive

Read the `main` branch README of `gfernandf/agent-skill-registry` and mapped it to AMOS skill registry and vocabulary governance.

### Verified shape

- Apache 2.0, open registry of capabilities and skills.
- 159 capabilities, 37 skills; validation, catalog generation, stats, governance guardrails.
- Controlled vocabulary: `domain.noun.verb` for capability identifiers.
- Declarative skills as dataflow: `inputs → steps → outputs` with capability/skill references.
- Machine-readable catalogs: `capabilities.json`, `skills.json`, `graph.json`, `stats.json`.
- Governance artifacts: `catalog/governance_guardrails.json`, `capability_governance_guardrails.json`.
- Tools: `validate_registry.py`, `generate_catalog.py`, `registry_stats.py`, `governance_guardrails.py`.

### Integration points for AMOS

1. **Vocabulary control → `amos-skill-builder` and `amos-skill-registry-gateway`**
   - The `domain.noun.verb` capability pattern can tighten AMOS skill `name` and `capabilities` naming.
   - AMOS can add a `vocabulary.json` to `.devin/skills/` and validate names with `skill-check`.

2. **Declarative skill dataflow → `amos-workflow-builder` and `amos-workflow-runner`**
   - Skill workflows as dataflow `steps` referencing capabilities/skills by ID maps to AMOS workflow `steps` and `inputs/outputs`.
   - Could extend `amos-workflow-builder` to emit `agent-skill-registry`-compatible YAML/JSON.

3. **Machine-readable catalog → `amos-skill-catalog-generator` and `agent-registry`**
   - The generated `catalog/` files mirror AMOS `.devin/agents/` index and `skill_catalog_generator.py` outputs.
   - Export AMOS `.devin/skills/` to `catalog/skills.json` for interop.

4. **Governance guardrails → `skill_guardrail_checker` and `amos-promotion-gates`**
   - `governance_guardrails.py` and `capability_governance_guardrails.py` are references for `skill_guardrail_checker` and `amos-promotion-gates`.

5. **Stats and sunset → `skill_version_manager` and `token_budget_analyzer`**
   - `registry_stats.py` and `enforce_capability_sunset.py` map to AMOS skill deprecation, version lifecycle, and usage analytics.

### Open questions / gaps

- 159 capabilities is small compared to AMOS 642 skills; mapping effort would be large.
- The README claims are not benchmarked; no runtime execution data shown.
- Apache 2.0 is compatible, but per-skill license governance still needed for AMOS ingestion.

### Recommended next step

Generate a machine-readable catalog from `gfernandf/agent-skill-registry` and compare its `capabilities.json` schema to the AMOS `SKILL.md` frontmatter to identify missing fields or naming mismatches.

Raw source: [[AGENT_SKILL_REGISTRY_README_2026_08_29]]

## 2026-08-29 | AgentSkills Registry deep-dive

Read the `main` branch README of `kai98k/agent-skills-registry` and mapped it to AMOS skill packaging and registry distribution.

### Verified shape

- Go CLI (`agentskills`) + server; npm/Docker Hub-like registry for AI agent skills.
- Skill bundle format: `SKILL.md` + optional `scripts/`, `references/`, `assets/`.
- CLI: `init`, `login`, `push`, `pull`, `search`, `vendor` (with lock file and checksum).
- Versioning: strict semver, pin, and `agentskills.lock` with SHA-256 for supply-chain safety.
- Security: checksum verification, path traversal protection, per-file 200 MB size limits, bearer token auth.
- Go + Cobra, file-based `.tar.gz` storage, JSON metadata.

### Integration points for AMOS

1. **Skill bundle format → `amos-skill-builder` and `skill-check`**
   - AgentSkills bundle (`SKILL.md`, `scripts/`, `references/`, `assets/`) mirrors AMOS skill directories.
   - AMOS `MANIFEST.yaml` can be extended to include `bundle_format: agentskills` and `checksum` fields for registry export.

2. **Vendor + lock file → `skill_integrity_lock.py` and `skill_registry_packager.py`**
   - `agentskills vendor` and `agentskills.lock` directly map to AMOS `skill_integrity_lock` and `skill_registry_packager`.
   - Add SHA-256 `checksum` and `source_server` to the existing AMOS lock artifacts.

3. **Semver and version pinning → `skill_version_manager.py`**
   - Strict `name@version` pulling is a reference for `amos-skill-builder` and `skill_version_manager` to pin skill versions per environment.

4. **Search and discovery → `amos-skill-registry-gateway` and `amos-agent-orchestrator`**
   - `agentskills search <keyword>` can be wrapped as an MCP tool or a `skill-check` subcommand.
   - AMOS agents can query a registry before falling back to local skills.

5. **Self-hosted registry → `amos-mcp-connector` and enterprise governance**
   - The standalone Go server supports private registries. AMOS could ship an `amos-skill-registry` MCP tool for on-premise skill distribution.

### Open questions / gaps

- No explicit star count in README; smaller than SkillNet / AgentFactory.
- Security claims (SHA-256, path traversal, size limits) not independently audited by AMOS.
- Quality of published skills is author responsibility; AMOS would still need `skill-check` and `skill_guardrail_checker` on `pull`.

### Recommended next step

Package one AMOS skill (e.g., `amos-llm-wiki`) into an AgentSkills-compatible `.tar.gz` bundle and validate that `SKILL.md` + `scripts/` + `references/` structure is accepted.

Raw source: [[AGENTSKILLS_REGISTRY_README_2026_08_29]]

## 2026-08-29 | XSkill deep-dive

Read the `main` branch README of `XSkill-Agent/XSkill` and mapped it to AMOS continual learning and memory systems.

### Verified shape

- ICML 2026, MIT License.
- Two-phase loop: Phase I (Accumulation) distills skill documents and experience entries from trajectories; Phase II (Inference) retrieves and adapts knowledge into the system prompt.
- Visually-grounded trajectory summarization, cross-rollout critique, hierarchical consolidation.
- `memory_bank/` created at runtime with experience library and skill documents.
- Supports text and multimodal (images) samples; OpenAI-compatible API; needs SerpAPI, Jina, ImgBB keys.
- Evaluated on VisualToolBench, TIR-Bench, MMSearch-Plus, AgentVista, MMBrowseComp.

### Integration points for AMOS

1. **Experience + skill memory bank → `amos-memory-systems-master` and `amos-llm-wiki`**
   - The `memory_bank/` of structured skills/experiences maps directly to AMOS `11_KNOWLEDGE/LLM_WIKI/raw/` and `memory/short_term/` vs `memory/long_term/` split.
   - AMOS can store trajectories as `agent_interaction.md` and consolidate them into `SKILL.md` upgrades via `skill_operations_enhancer.py`.

2. **Phase I trajectory summarization → `amos-observability-driven-harness-evolution-rscf`**
   - `trajectory_summary.py` and `experience_critique.py` mirror the AMOS `execution trace → memory → consolidated skill` pipeline.
   - Could reuse `amos-observability-driven-harness-evolution-rscf` to generate `best_skill.md` candidates.

3. **Phase II retrieval + prompt injection → `amos-agent-orchestrator` and `amos-llm-wiki`**
   - Retrieve relevant skills from the bank and inject into the system prompt, similar to AMOS `AMOS_BOOT.md` and `CLAUDE.md` context window management.
   - `amos-llm-wiki` can serve as the retrieval corpus.

4. **Skill documents from trajectories → `amos-skill-builder` and `amos-evolution-loop`**
   - `skill_builder.py` automatically creates structured skill documents from rollouts. AMOS `amos-skill-builder` can consume execution traces to propose `SKILL.md` updates.

5. **Multimodal sample format → `amos-structured-document-parsing-rscf` and `amos-multimodal-perception-layer`**
   - The JSON sample format with `problem`, `images`, `<image>` placeholders is a reference for AMOS multimodal prompts.

### Open questions / gaps

- Requires many API keys (SERPAPI, JINA, ImgBB, OpenAI endpoints); not all AMOS users will have these.
- No explicit SOTA improvement claims; only "considerable performance gains" without numbers in README.
- Python 3.11 recommended; current host is 3.9.6.

### Recommended next step

Inspect the `eval/exskill/skill_builder.py` output format and compare an XSkill-generated skill document to the AMOS `SKILL.md` frontmatter schema.

Raw source: [[XSKILL_README_2026_08_29]]

## 2026-08-29 | Agent Skills (agentskills.io) deep-dive

Read the canonical Agent Skills README and specification and verified AMOS compliance.

### Verified shape

- Anthropic-opened standard, Apache 2.0, 24,770+ stars.
- Skill bundle: `SKILL.md` + optional `scripts/`, `references/`, `assets/`.
- `SKILL.md` frontmatter: `name` (1-64 lowercase alphanumeric/hyphens), `description` (≤1024 chars), optional `license`, `compatibility`, `metadata`, `allowed-tools`.
- Progressive disclosure: metadata (~100 tokens) → full `SKILL.md` instructions → `scripts/` / `references/` / `assets/` on demand.
- Keep `SKILL.md` under 500 lines; move detailed reference material to `references/`.
- `agentskills` package has `skills-ref validate` tool.

### Integration points for AMOS

1. **Canonical bundle format → `amos-skill-builder` package spec**
   - AMOS skill bundles are already structurally equivalent (`SKILL.md`, `references/`, `scripts/`). The `assets/` directory and `allowed-tools` frontmatter can be added as optional fields.

2. **Progressive disclosure → `amos-skill-builder/references/progressive_loading.md`**
   - Agent Skills three-stage disclosure mirrors AMOS `references/progressive_loading.md` and `CAPABILITY_NAMING_CONTRACT.md`.

3. **Validation tool `skills-ref` → `skill-check` and `sota_skill_validator.py`**
   - The 642 AMOS skills already pass the `name` and `description` constraints.
   - `skill-check` can be extended to check `allowed-tools` and `compatibility` fields.

4. **Open standard adoption → `amos-skill-registry-gateway` and `amos-mcp-connector`**
   - Export AMOS `.devin/skills/` as Agent Skills bundles; import Agent Skills from public registries.

### Open questions / gaps

- AMOS uses `_` in some `tags` and `domain` values, but `name` fields are clean.
- AMOS `SKILL.md` files are already under 500 lines after the `SOTA Evaluation Contract` split.

### Recommended next step

Add `allowed-tools` and `compatibility` as optional frontmatter fields in `amos-skill-builder` and validate that existing 642 skills can still pass `sota_skill_validator.py`.

Raw sources: [[AGENTSKILLS_SPEC_README_2026_08_29]] · [[AGENTSKILLS_SPECIFICATION_2026_08_29]]

## 2026-08-29 | OpenSkills SDK deep-dive

Read the `main` branch README of `ljluestc/OpenSkills` and mapped it to AMOS progressive disclosure and script execution.

### Verified shape

- Apache 2.0, PyPI `openskills-sdk`, Python 3.10+.
- Three-layer progressive disclosure: Metadata (Layer 1) → Instructions (Layer 2) → Resources (Layer 3).
- `SKILL.md` frontmatter: `name`, `description`, `version`, `triggers`, `references`, `scripts`.
- Reference loading modes: `explicit` (condition), `implicit` (LLM decides), `always`.
- Auto-discovery of `references/` directory.
- Script execution via `[INVOKE:name]` marker and optional AIO Sandbox container.
- Multiple LLM providers: OpenAI, Azure, Ollama, Together, Groq, DeepSeek.
- Multimodal support: images via URL, base64, or file path.

### Integration points for AMOS

1. **Progressive disclosure layers → `amos-skill-builder/references/progressive_loading.md`**
   - OpenSkills L1/L2/L3 directly maps to AMOS `references/` progressive loading. AMOS `SKILL.md` frontmatter is L1, body is L2, `references/` and `scripts/` are L3.

2. **Reference loading modes → `amos-skill-builder` reference manifest**
   - Add `mode: explicit|implicit|always` and `condition` fields to `references/` entries. This can be added to `MANIFEST.yaml` or a `references/index.yaml`.

3. **Auto-discovery of `references/` → `amos-skill-builder` and `skill-check`**
   - `skill-check` can auto-index `references/` and validate that all referenced files exist, similar to the wikilink lint.

4. **Script invocation via `[INVOKE:name]` → `amos-workflow-runner` and `amos-agent-orchestrator`**
   - AMOS `scripts/` can be triggered by the LLM outputting an explicit marker. `amos-workflow-runner` can parse `[INVOKE:script_name]` in skill outputs and execute the matching script.

5. **AIO Sandbox → `amos-security-safety-master` and `amos-os-runtime-master`**
   - Containerized script execution with dependency auto-install is a reference for `amos-os-runtime-master` and `skill_guardrail_checker.py`.

### Open questions / gaps

- Requires Python 3.10+ and Docker for sandbox; current host Python 3.9.6.
- `triggers` frontmatter is more specific than AMOS `description` triggers; AMOS could add `triggers` list.

### Recommended next step

Add `triggers` and `references` loading-mode metadata to the AMOS `SKILL.md` frontmatter and `CONTRACT_TEMPLATE.yaml` to align with OpenSkills progressive disclosure.

Raw source: [[OPENSKILLS_README_2026_08_29]]
