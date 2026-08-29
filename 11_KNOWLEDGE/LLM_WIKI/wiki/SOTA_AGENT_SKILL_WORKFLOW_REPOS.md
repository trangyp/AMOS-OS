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

## 2026-08-29 | MMSkills for Visual Agents deep-dive

Read the `main` branch README of `zkangning/MMSkills_for_Visual_Agents` and mapped it to AMOS multimodal skill packaging.

### Verified shape

- Apache 2.0, Python 3.10+, 515 skills in library.
- Skill package: `SKILL.md` + runtime state cards + audit state cards + visual keyframes.
- Multimodal evidence gating: runtime decides if visual references are needed, loads only requested state views.
- Branch-loaded planning: temporary planner branch consults selected skills and returns guidance, fallback, verification cues.
- Agent adapters for Codex, OpenClaw, Claude Code.
- OSWorld, macOSWorld, VAB-Minecraft, GamingAgent integrations.

### Integration points for AMOS

1. **Visual keyframes / state cards → `amos-multimodal-perception-layer` and `amos-structured-document-parsing-rscf`**
   - AMOS skills can include `assets/` with images and `references/` with state cards, gated by runtime evidence needs.

2. **Multimodal evidence gating → `amos-boundary-scope-master` and `amos-context-budget-governor-rscf`**
   - Only load visual references when task state requires them, reducing context budget.

3. **Branch-loaded planning → `amos-agent-orchestrator` and `amos-workflow-runner`**
   - Temporary planner branch can be modeled as a subagent dispatch that consults a skill and returns concise guidance.

4. **Agent Adapter pattern → `amos-mcp-connector` and `amos-skill-registry-gateway`**
   - One-line adapter for Claude Code / Codex maps to AMOS `CLAUDE.md` and `SKILL_INDEX.md` integration.

5. **Searchable skill library → `amos-skill-registry-gateway` and `amos-llm-wiki`**
   - On-demand Hugging Face / web skill retrieval can be mirrored to `11_KNOWLEDGE/LLM_WIKI/raw/` ingestion.

### Open questions / gaps

- Visual skill packages require image assets; AMOS skills are mostly text/code today.
- Requires Python 3.10+ and OSWorld; current host is 3.9.6.
- No explicit benchmark numbers in README.

### Recommended next step

Add an `assets/` directory and visual-keyframe support to one AMOS skill (e.g., `amos-llm-wiki`) to prototype MMSkills-style multimodal evidence gating.

Raw source: [[MMSKILLS_README_2026_08_29]]

## 2026-08-29 | AgentSkillOS deep-dive

Read the `main` branch README of `songfang/AgentSkillOS` and mapped it to AMOS skill tree, retrieval, and DAG orchestration.

### Verified shape

- MIT License, Python 3.10+, 90,000+ skill ecosystem.
- Three pillars: skill tree construction, skill retrieval, skill orchestration.
- Capability tree organizes skills hierarchically for coarse-to-fine discovery.
- Complementarity-aware retrieval selects diverse skill sets.
- Graph-based orchestration executes skills as a DAG with human-in-the-loop GUI.
- Observability and debugging with step logs and metadata.
- Pre-built trees: `skill_seeds` (~50), `top500`, `top1000`.
- Future work: interactive agent execution, plan refinement, auto skill import, dependency detection, recipe generation.

### Integration points for AMOS

1. **Skill tree / capability hierarchy → `SKILL_INDEX.md` and `07_SKILLS_MOC`**
   - AgentSkillOS skill tree directly maps to the AMOS `.devin/SKILL_INDEX.md` hierarchical router. AMOS can model the 642 skills as a capability tree with `parent_skill` and `domain`.

2. **Complementarity-aware retrieval → `amos-routing-audit` and `amos-agent-orchestrator`**
   - Selecting a diverse, task-relevant skill set is a natural extension of `amos-routing-audit` intent classification and `amos-agent-orchestrator` agent discovery.

3. **DAG-based skill orchestration → `amos-workflow-builder` and `amos-workflow-runner`**
   - AgentSkillOS DAG execution maps to AMOS workflow `steps` and the `amos-workflow-runner`. Human-in-the-loop checkpoints mirror `amos-promotion-gates`.

4. **Human-in-the-loop GUI → `amos-human-interaction-engine` and `amos-promotion-gates`**
   - Step-level human approval can be added to `amos-workflow-runner` and `amos-promotion-gates`.

5. **Observability / step logs → `amos-observability-driven-harness-evolution-rscf` and `amos-decision-logger`**
   - Per-step logs and metadata for debugging are already partially in `amos-observability-driven-harness-evolution-rscf`.

### Open questions / gaps

- Requires Python 3.10+ and Claude Code; current host is 3.9.6.
- 90,000+ skill ecosystem is larger than AMOS; bridging is a long-term mapping effort.
- The skill tree is a curated, pre-built artifact; AMOS needs a runtime tree builder.

### Recommended next step

Generate a capability tree from the existing 642 AMOS skills using `parent_skill` and `domain` fields and compare it to AgentSkillOS `skill_seeds` / `top500` tree format.

Raw source: [[AGENTSKILLOS_README_2026_08_29]]

## 2026-08-29 | Production skill marketplaces and hardened registries

### `tech-leads-club/agent-skills` — 5,087 stars, production skill catalog

- Hardened, human-curated skill library with Snyk Agent Scan, lockfiles, content hashing.
- Multi-agent installer for Claude Code, Cursor, Cline, GitHub Copilot, Windsurf, Aider, etc.
- Skills grouped in categories (`(development)`, `(cloud)`, `(security)`, etc.); `SKILL.md` + `references/` + `scripts/` + `templates/`.
- CLI `npx @tech-leads-club/agent-skills` with install/update/list, copy or symlink scope.
- Strong governance: Verifier pattern (author != verifier), deterministic `scripts/*.py` gates, `STATE.md` decision log.
- AMOS importables:
  1. **Snyk Agent Scan / content hashing → `skill_guardrail_checker.py` and `skill_security_scanner.py`**
  2. **Category-based skill tree → `SKILL_TREE.json` category expansion**
  3. **Verifier pattern (author != verifier) → `amos-promotion-gates` and `skill-check`**
  4. **`STATE.md` decision log → `amos-decision-logger` and `11_KNOWLEDGE/LLM_WIKI/wiki/LLM_WIKI_LOG.md`**

### `ivanzwb/agent-skills` — TypeScript skill lifecycle framework

- Open [Agent Skills Specification](https://agentskills.io/specification) implementation.
- Progressive loading L0/L1/L2, `manifest.json` tool declarations, dependency installers (npm/pip/extensible).
- CLI `skill` with install/uninstall/preview/search; GitHub + ClawHub network install.
- Security: zip-slip detection, path traversal prevention, atomic lockfile, JSON persistent registry.
- AMOS importables:
  1. **`manifest.json` tool declarations → `amos-skill-builder` tool contracts**
  2. **L0/L1/L2 progressive loading → `amos-skill-builder/references/progressive_loading.md`**
  3. **Dependency installers → `amos-skill-builder/scripts/dependency_installer.py`**
  4. **Atomic lockfile / JSON registry → `skill_integrity_lock.py` and `amos-skill-registry-gateway`**

### `ComeOnOliver/skillshub` — Token-efficient skill resolver API

- `skillshub.wtf` search/resolve endpoints: 1 API call returns the best-fit skill for a task.
- 10,000+ skills indexed from 230+ repos; no auth required for search/fetch; raw `SKILL.md` via `?format=md`.
- AMOS importables:
  1. **Skill resolver API → `amos-skill-registry-gateway` MCP tool**
  2. **`/api/v1/skills/resolve` → `amos-routing-audit` and `amos-agent-orchestrator` route selection**
  3. **No-auth fetch endpoint → `amos-llm-wiki` remote source ingestion**

Raw sources: [[TECH_LEADS_CLUB_AGENT_SKILLS_README_2026_08_29]] · [[IVANZWB_AGENT_SKILLS_README_2026_08_29]] · [[SKILLSHUB_README_2026_08_29]]

## 2026-08-29 | Anthropic Skills (canonical Claude skill library) deep-dive

Read the `main` branch README of `anthropics/skills` and mapped it to AMOS Claude Code integration and skill marketplace.

### Verified shape

- Official Anthropic skill examples. Includes `skills/`, `spec/`, `template/`.
- Document skills (`docx`, `pdf`, `pptx`, `xlsx`) are source-available production skills.
- Claude Code plugin marketplace: `/plugin marketplace add anthropics/skills`.
- Claude API supports pre-built and custom skills.
- Basic skill only requires `name` and `description` frontmatter.

### Integration points for AMOS

1. **Document skills → `amos-pdfs`, `amos-docx`, `amos-slides`, `spreadsheets`**
   - AMOS already has `pdfs`, `docx`, `slides`, `spreadsheets` skills. Can compare to `anthropics/skills/skills/docx`, `pdf`, `pptx`, `xlsx` for production patterns.

2. **Claude Code plugin marketplace → `amos-skill-registry-gateway` and `amos-mcp-connector`**
   - AMOS can expose `.devin/skills/` as a Claude Code `/plugin marketplace` compatible catalog.

3. **Basic skill template → `amos-skill-builder` reference template**
   - The minimal frontmatter is exactly what AMOS `sota_skill_validator` enforces. Add `anthropics/skills/template` as a reference to `amos-skill-builder/references/`.

4. **Skills API → `amos-skill-registry-gateway` REST endpoints**
   - The Claude API Skills API can be mirrored for AMOS skill upload/retrieve.

### Open questions / gaps

- Source-available document skills are not fully open source.
- Plugin marketplace is Claude-specific; AMOS needs an agent-agnostic registry.

### Recommended next step

Fetch the `anthropics/skills/template` and `spec` directories and compare the canonical template to the AMOS `CONTRACT_TEMPLATE.yaml`.

Raw source: [[ANTHROPICS_SKILLS_README_2026_08_29]]

## 2026-08-29 | Anthropic Skills template and spec comparison

Captured the canonical `anthropics/skills/template/SKILL.md` and `spec/agent-skills-spec.md` and compared to AMOS `CONTRACT_TEMPLATE.yaml`.

### Verified shape

- `anthropics/skills/template/SKILL.md` requires only `name` and `description`.
- `anthropics/skills/spec/agent-skills-spec.md` is a pointer to `https://agentskills.io/specification` (already captured).
- The spec frontmatter fields are: `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`.

### Comparison to AMOS `CONTRACT_TEMPLATE.yaml`

AMOS is already a strict superset:

| Field | Anthropic spec | AMOS `CONTRACT_TEMPLATE.yaml` | Status |
|---|---|---|---|
| `name` | yes, 64 chars | yes, 64 chars, `name`/`name` | covered |
| `description` | yes, 1024 chars | yes, 1024 chars | covered |
| `license` | optional | yes, `license` | covered |
| `compatibility` | optional | yes, `compatibility` | covered |
| `metadata` | optional map | `rscf`, `status`, `category`, `tags` | covered + more |
| `allowed-tools` | optional | yes, `allowed-tools` | covered |
| `references` loading modes | N/A | explicit/implicit/always, `path` + `mode` | exceeds spec |
| `triggers` | N/A | yes | exceeds spec |
| `capabilities` typed I/O | N/A | yes | exceeds spec |
| `input`/`output` typed schema | N/A | yes | exceeds spec |
| `rscf` epistemic metadata | N/A | yes | exceeds spec |

### Conclusion

AMOS `amos-skill-builder` already produces skill bundles that satisfy the canonical Agent Skills spec and adds progressive disclosure, typed I/O, epistemic metadata, and governance fields beyond it.

Raw sources: [[ANTHROPICS_SKILLS_TEMPLATE_2026_08_29]] · [[AGENTSKILLS_SPECIFICATION_2026_08_29]]

## 2026-08-29 | SkillOS and ai-os deep-dive

Read the canonical `EvolvingAgentsLabs/skillos` README and the active successor `EvolvingAgentsLabs/ai-os` README.

### Verified shape

- `skillos` is frozen as of 2026-08-01; the concept continues in `ai-os`.
- Pure Markdown OS: every component is an agent or tool defined in markdown; LLM is the interpreter.
- `boot skillos` command; `setup_agents.sh`/`setup_agents.ps1`; `projects/[ProjectName]/` structure.
- 3-level hierarchy: Domain → Family → Skill; 4-step lazy loading; ~61% token reduction.
- HWM planning (arXiv:2604.03208); dialects (14 token-compression formats up to 99% reduction); compounding knowledge wiki; structured memory.
- `ai-os` is an agent-based operating system on `QM` with external `truth/` gates, hash-chained ledger, `make reproduce`, nightly provenance checks.
- `ai-os` has `ai-base/`, `ai-flows/`, `ai-memory/`, `ai-ui/`, `projects/`, `truth/`.

### Integration points for AMOS

1. **Pure Markdown OS → `amos-skill-builder`, `amos-agent-orchestrator`, and `stitch_project_cosmo/.devin/AMOS_BOOT.md`**
   - AMOS already uses markdown specs (`SKILL.md`, `CLAUDE.md`, `AGENTS.md`). The `SkillOS` boot structure reinforces the `AMOS_BOOT.md` + `SKILL_INDEX.md` pattern.

2. **Hierarchical skill tree → `stitch_project_cosmo/.devin/SKILL_TREE.json`**
   - Domain → Family → Skill maps to AMOS `domain` → `parent_skill` → `name`. The `SKILL_TREE.json` can be extended with a 3-level view.

3. **4-step lazy loading → `amos-skill-builder/references/progressive_loading.md`**
   - AMOS already has L0/L1/L2; add explicit 4-step lazy loading (metadata → instruction → reference → script) if needed.

4. **Dialects / token compression → `amos-cognitive-compression-kernel` and `amos-llm-wiki`**
   - Token compression is similar to `amos-cognitive-compression-kernel`. Could import `strict-patch`, `formal-proof`, `system-dynamics` as dialect examples.

5. **Memory wiki and structured memory → `amos-memory-systems-master` and `amos-llm-wiki`**
   - `short_term/` and `long_term/` memory structure mirrors `11_KNOWLEDGE/LLM_WIKI/` and `memory/`.

6. **ai-os `truth/` external gates → `amos-claim-verifier`, `amos-audit-repair-master`, `enforcement_root_attestation.py`**
   - The principle that `truth/` must not import `src/` is exactly the AMOS `enforcement_root_attestation` / RSCF epistemic separation.

7. **Nightly provenance / hash-chained ledger → `amos-decision-logger` and `skill_integrity_lock.py`**
   - AMOS can adopt `make reproduce` and nightly provenance checks for `sota_skill_validator.py` and `agent_sync_validator.py`.

### Open questions / gaps

- `skillos` is frozen; do not build on it directly. Use `ai-os` patterns instead.
- `ai-os` requires Node.js/TypeScript runtime; AMOS is Python-centric.
- `ai-os` has 828 tests and 3,768 upstream tests; AMOS SOTA validator is smaller.

### Recommended next step

Add a 3-level Domain → Family → Skill view to `.devin/SKILL_TREE.json` and a `make reproduce` target for the AMOS SOTA validator.

Raw sources: [[SKILL_OS_README_2026_08_29]] · [[AI_OS_README_2026_08_29]]

## 2026-08-30 | addyosmani/agent-skills deep-dive

Read the `addyosmani/agent-skills` README — production-grade engineering skills for AI coding agents.

### Verified shape

- 25 skills covering the full dev lifecycle: `/spec`, `/plan`, `/build`, `/test`, `/constraints`, `/review`, `/webperf`, `/code-simplify`, `/ship`.
- `/build auto` generates plan + implements in one approved pass, commits each task, pauses on failures.
- Auto-activation: API design → `api-and-interface-design`, UI → `frontend-ui-engineering`, etc.
- CLI `npx skills add addyosmani/agent-skills` supports 70+ agents (Claude Code, Cursor, Codex, Copilot, Cline).
- Each skill is self-contained in `skills/<name>/SKILL.md` with `references/` for shared checklists.

### Integration points for AMOS

1. **Lifecycle slash commands → `amos-workflow-runner` and `amos-agent-orchestrator`**
   - `/spec`, `/plan`, `/build`, `/test`, `/review`, `/ship` map to AMOS workflow names. AMOS can expose the same 9 commands as canonical workflow invocations.

2. **Per-skill SKILL.md pattern → `amos-skill-builder` and `CONTRACT_TEMPLATE.yaml`**
   - Addy uses `skills/<name>/SKILL.md` + `references/` pattern. AMOS already uses this. The `references/` shared checklists mirror AMOS `references/` with loading modes.

3. **Auto-activation by context → `amos-routing-audit` and `amos-c10-tech-engineering-master`**
   - AMOS can adopt trigger-based auto-activation: `api-and-interface-design` for API changes, `frontend-ui-engineering` for UI changes.

4. **`/build auto` autonomous pass → `amos-autonomous-evolution` and `amos-evolution-loop`**
   - Plan generation, implementation per task, individual commits, failure pause. AMOS already has `AMOS_AUTONOMOUS_EVOLUTION_LAYER.py` and `evolution-loop` skill.

5. **Quality gates (constraints, review, webperf, code-simplify) → `software-engineering-qa`, `amos-code-agent-harness-rscf`, `amos-structured-document-parsing-rscf`**
   - Addy's five-axis review and TDD constraints can strengthen AMOS QA and code harness skills.

6. **Claude Code `/plugin` marketplace → `amos-skill-registry-gateway` and `agent-registry`**
   - AMOS `.devin/skills/` can be exposed as a Claude Code / Cursor / Copilot plugin marketplace.

### Conclusion

`addyosmani/agent-skills` is the most production-aligned engineering skill catalog captured so far. Its lifecycle commands and auto-activation directly map to AMOS workflow and routing capabilities. The AMOS `software-engineering-qa` and `amos-skill-builder` can be enriched with Addy's five-axis review, `/build auto` commit pattern, and constraints checklist.

Raw source: [[ADDYOSMANI_AGENT_SKILLS_README_2026_08_30]]

## 2026-08-30 | Context Engineering & Agent Skills Standard deep-dive

Captured two high-signal skill frameworks: `muratcankoylan/Agent-Skills-for-Context-Engineering` (17,857 stars, academic-cited) and `HoangNguyen0403/agent-skills-standard` (539 stars, SDLC standards CLI).

### muratcankoylan/Agent-Skills-for-Context-Engineering

Verified shape:
- 16+ skills across Foundational, Architectural, Operational, Methodology, Cognitive Architecture.
- Progressive disclosure: skill names/descriptions loaded first, full content on activation.
- Platform agnostic; Claude Code plugin marketplace.
- Cited in arxiv Meta Context Engineering and Agent Harness Engineering survey.

Integration points for AMOS:
- `context-fundamentals`, `context-degradation`, `context-compression` → `amos-context-budget-governor-rscf`, `amos-context-compaction-recoverability-rscf`, `amos-long-context-ci-repository-reasoning-rscf`.
- `multi-agent-patterns`, `harness-engineering` → `amos-agent-systems-master`, `amos-agent-orchestrator`.
- `memory-systems` → `amos-memory-systems-master`.
- `self-improvement-loops` → `amos-autonomous-evolution`, `amos-evolution-loop`.
- `evaluation`, `advanced-evaluation` → `amos-evaluation`, `amos-formal-agent-skill-verification-rscf`.
- `project-development` → `amos-workflow-builder`, `amos-c10-tech-engineering-master`.

### HoangNguyen0403/agent-skills-standard

Verified shape:
- `npx agent-skills-standard init/sync` CLI; 280 coding standards for 8+ agents.
- `AGENTS.md` router → `_INDEX.md` trigger table → `SKILL.md` progressive loading.
- MCP server runtime enforcement, lockfile (`ags verify`), pre-edit hooks, secret/dependency scanning.
- Zero-Trust / Rust Token Killer inspired token economy.

Integration points for AMOS:
- `AGENTS.md` → `_INDEX.md` → `SKILL.md` hierarchy → AMOS `SKILL_INDEX.md` and `SKILL_TREE.json` already mirror this.
- `ags verify` lockfile pattern → `sota_skill_validator.py` and `skill_integrity_lock.py`.
- MCP `load_skills_for_files` → `amos-mcp-connector`, `amos-skill-registry-gateway`.
- Pre-edit hooks → `amos-skill-builder/scripts/hooks/pre_tool_use.py` and `post_tool_use.py`.
- Secret/dependency scanning → `skill_security_scanner.py`, `amos-provenance-trust-firewall`.

### Conclusion

`muratcankoylan/Agent-Skills-for-Context-Engineering` is the strongest academic-backed context-engineering catalog; `HoangNguyen0403/agent-skills-standard` is the strongest CLI-governed SDLC standards system with lockfiles, MCP, and hooks. AMOS can adopt the `AGENTS.md` → `_INDEX.md` → `SKILL.md` progressive lookup and the `ags verify` lockfile/audit model.

Raw sources: [[AGENT_SKILLS_FOR_CONTEXT_ENGINEERING_README_2026_08_30]] · [[AGENT_SKILLS_STANDARD_README_2026_08_30]]

## 2026-08-30 | Curated skill marketplaces and large-scale catalogs captured

Captured three additional high-coverage skill distribution patterns: `pedronauck/skills` (131 skills, 4 buckets), `heyimcarlos/agent-skills` (skills + subagents, QRSPI workflow), and `netresearch/claude-code-marketplace` (39 stack-specific skills, Agent Plugins 1.0.0).

### pedronauck/skills

Verified shape:
- 131 skills in `skills/mine/`, `skills/curated/`, `skills/marketing/`, `skills/community/`.
- `npx skills add https://github.com/pedronauck/skills` with bucket subpaths.
- Agent Skills spec, Claude Code native, `description`-driven activation.

Integration points for AMOS:
- Bucket-based skill storage → `SKILL_TREE.json` `domain_family_tree` and `.devin/skills/<domain>/<skill>/SKILL.md`.
- Curated/community/original distinction → `amos-skill-builder/references/eval-harness-template.md` and `amos-skill-registry-gateway`.
- `description` frontmatter trigger routing → `amos-routing-audit`.

### heyimcarlos/agent-skills

Verified shape:
- Skills in `skills/engineering/`, `skills/qrspi/`, `skills/misc/`, plus `agents/` subagents.
- QRSPI workflow: Question → Research → Spec → Plan → Implement → Setup.
- `disable-model-invocation: true` for deliberate human phase invocation.
- HTML output mode for reveal.js slide decks alongside markdown.
- `/plugin` install with subagent support.

Integration points for AMOS:
- QRSPI stages → `amos-workflow-builder` named workflows `qrspi-*`.
- Subagents in `agents/` → `amos-agent-orchestrator` and `amos-agent-externalization-architecture-rscf`.
- `disable-model-invocation` → `amos-mode-ontology` / `amos-prompt-domain-control-rscf-engine`.
- HTML slide output → `amos-multimodal-perception-layer` visual keyframes, `amos-slides`.

### netresearch/claude-code-marketplace

Verified shape:
- 39 curated skills for TYPO3, PHP, Go, Docker, Jira, security, documentation.
- Agent Plugins 1.0.0 packaging: `plugin.json` + `skills/`.
- Marketplace site with per-skill pages in English + German.
- Host-side tooling: Composer plugin and npm coordinator.

Integration points for AMOS:
- `plugin.json` + `skills/` → `amos-skill-builder/manifest.json` and `MANIFEST.yaml` bundle format.
- Marketplace site/catalog → `amos-skill-registry-gateway` and `AMOS_SKILL_REGISTRY`.
- `AGENTS.md` generated by `agent-rules-skill` → `amos-agent-orchestrator/CLAUDE.md` and `AMOS_BOOT.md`.
- Composer/npm distribution → `agent-registry` OCI/manifest promotion.

Raw sources: [[PEDRONAUCK_SKILLS_README_2026_08_30]] · [[HEYIMCARLOS_AGENT_SKILLS_README_2026_08_30]] · [[NETRESEARCH_CLAUDE_CODE_MARKETPLACE_README_2026_08_30]]
