---
title: LLM Wiki Log
type: log
source: 11_KNOWLEDGE/LLM_WIKI
tags:
- log
- llm-wiki
- canon/knowledge
- karpathy-llm-wiki-summary
- llm-wiki-moc
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_knowledge
---

# LLM Wiki Log

Chronological, append-only record of ingests, queries, and lint passes.

## [2026-08-28] init | AMOS LLM Wiki created
- Created `00_ROOT/AMOS_LLM_WIKI.md` schema
- Created `11_KNOWLEDGE/LLM_WIKI/` with `raw/`, `wiki/`, and MOC
- Added links to `` and ``
- First raw source: [Karpathy LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- First wiki page: [[karpathy_llm_wiki_summary]]

## [2026-08-28] build | AMOS canonical bindings added
- Created `amos-llm-wiki` skill in `.devin/skills/amos-llm-wiki/`
- Created `amos-llm-wiki-workflow` in `.devin/workflows/`
- Created `amos-llm-wiki-agent` in `.devin/agents/`
- Created `14_TOOLS/AMOS_LLM_WIKI_TOOL.md`
- Updated `00_ROOT/AMOS_LLM_WIKI.md` and `14_TOOLS/14_TOOLS_MOC.md`
- `agent_sync_validator.py` reports `amos-llm-wiki-agent` as VERIFIED

## [2026-08-28] populate | Wiki text filled and health checked
- Filled `` with sources, concepts, entities, syntheses, and tools
- Created concept page ``
- Created synthesis page ``
- Ran `AMOS_OBSIDIAN_MEMORY_BRIDGE` self-test: 43 passed, 0 failed
- Fixed orphan `08_WORKFLOWS/kimi-k3-in-c-workflow.md` by linking ``

## [2026-08-25] research | SOTA agent/skill/workflow repo survey
- Web-searched public GitHub repositories for agent skill, workflow, and orchestration tooling.
- Captured raw source to [[SOTA_AGENT_SKILL_WORKFLOW_REPOS_2026_08_25]]
- Synthesized top picks and AMOS integration notes to [[SOTA_AGENT_SKILL_WORKFLOW_REPOS]]
- Updated [[LLM_WIKI_INDEX]] catalog and this log.

---
RSCF-NODE
node_id: llm_wiki_log
node_type: log
path: 11_KNOWLEDGE/LLM_WIKI/wiki/LLM_WIKI_LOG.md
RSCF-RELATIONS:
  - INDEXED_BY: [[LLM_WIKI_MOC]]
claim_class: AMOS_MODEL

---
**MOC:** [[LLM_WIKI_MOC]]

## [2026-08-29] research | SOTA agent/skill/workflow repo follow-up

- Web-searched for `best skill marketplace multi agent framework github 2026` and `agentic skills registry orchestration github AgentSkillOS ORPHEUS alternatives`.
- Identified 10 additional public repositories: `nexus-agentos`, `SkillNet`, `AgentSkillOS`, `ORPHEUS`, `agent-skill-registry`, `agent-skills-registry`, `agent-registry`, `skill-orchestration-system`, `aidd-framework`.
- Captured raw source to [[SOTA_AGENT_SKILL_WORKFLOW_REPOS_2026_08_29]].
- Updated synthesis and AMOS integration notes in [[SOTA_AGENT_SKILL_WORKFLOW_REPOS]].

## [2026-08-29] repo evaluation | SkillNet README deep-dive

- Fetched `zjunlp/SkillNet` README and captured raw source to [[SKILLNET_README_2026_08_29]].
- Mapped SkillNet SDK/CLI capabilities to AMOS skill-builder, routing-audit, workflow-runner, and MCP integration.
- Updated [[SOTA_AGENT_SKILL_WORKFLOW_REPOS]] with a deep-dive section and recommended next step: clone and AMOS-lint one SkillNet skill.

## [2026-08-29] fix | .devin/skills reach 100% SOTA compliance

- Ran `.devin/scripts/sota_skill_validator.py` against `stitch_project_cosmo/.devin/skills`.
- Fixed `amos-routing-audit/SKILL.md` frontmatter: the `description` field had RSCF content embedded inside it and lacked a concrete trigger.
- Split the `## SOTA Evaluation Contract` section out of 16 oversized skills into `references/SOTA_EVALUATION_CONTRACT.md` with Obsidian wikilinks, achieving `skill_md_lines < 500` everywhere.
- Result: 642 / 642 skills pass all 12 SOTA gates with a 1.00 score and 0 warnings.

## [2026-08-29] research | ORPHEUS README captured and evaluated

- Fetched `nuryslyrt/ORPHEUS` README and captured raw source to [[ORPHEUS_README_2026_08_29]].
- Mapped ORPHEUS orchestrator/expert/worker/contract patterns to `amos-workflow-builder`, `amos-routing-audit`, `amos-skill-builder`, and `amos-agent-orchestrator`.
- Updated [[SOTA_AGENT_SKILL_WORKFLOW_REPOS]] with a deep-dive section and recommended next step: clone and compare a generated `.orpheus/` system to an AMOS workflow.

## [2026-08-29] repo evaluation | ORPHEUS structure cloned and AMOS comparison

- Cloned `nuryslyrt/ORPHEUS` to `/tmp/orpheus` and inspected `skill/` and templates.
- Verified filesystem-only runtime: `SKILL.md` + `references/` + `scripts/` + `templates/`.
- `contract.yaml.tmpl` is a typed I/O envelope (name, version, input required/optional, output required/optional).
- `orchestrator-skill.md.tmpl` enforces a 4-phase execution protocol: intent decomposition, execution planning, dispatch, aggregation.
- AMOS importables identified:
  1. Contract YAML pattern → add `contract.yaml` artifact to `amos-skill-builder` bundles.
  2. Execution manifest + decision logs → extend `amos-workflow-runner` with `state/execution/{eid}/` logging.
  3. Expert/worker role hierarchy → map to `amos-agent-orchestrator` subagent dispatch.
  4. Routing table signal words → reuse in `amos-routing-audit` intent classification.

## [2026-08-29] repo evaluation | SkillOpt README and package structure

- Cloned `microsoft/SkillOpt` to `/tmp/skillopt` and inspected README, `pyproject.toml`, `skillopt/config.py`, `skillopt/types.py`.
- Core pattern: treat the skill markdown as a trainable parameter of a frozen agent.
- Training loop is Reflect → Aggregate → Select → Update → MetaReflect; output is `best_skill.md`.
- `Edit` dataclass defines `append/insert_after/replace/delete` ops with `target`, `content`, `source_type`, `support_count`.
- YAML configs use `_base_` inheritance and canonical/legacy alias normalization.
- AMOS importables identified:
  1. `best_skill.md` promotion gate → align with `amos-promotion-gates` and `amos-skill-builder`.
  2. Edit operation taxonomy → use in `skill_operations_enhancer.py` for deterministic skill mutations.
  3. Held-out validation gate before accepting edits → strengthen `skill_guardrail_checker` and `skill_rscf_canonicalizer`.
  4. YAML config inheritance with aliases → improve `workflow_operations_enhancer.py` and `amos-integrated-agent` rename maps.

## [2026-08-29] repo evaluation | SkillOpt install attempt blocked

- Attempted `pip install -e .` for `microsoft/SkillOpt` in a fresh `/tmp/skillopt/venv`.
- Environment has Python 3.9.6; SkillOpt requires `>=3.10`.
- No alternative Python 3.10+ interpreter found on the system.
- Blocked from running the recommended benchmark on `amos-llm-wiki`.
- Next: either install Python 3.10+ or run the benchmark in a container.

## [2026-08-29] repo evaluation | SkillFlow install attempt blocked

- Cloned `linxuhao/SkillFlow` to `/tmp/skillflow` and inspected README and `pyproject.toml`.
- Requires Python >=3.12 (badges and `requires-python` field).
- Key patterns identified from source (not executed):
  - YAML DAG pipeline graph executor
  - CLI tools: `skillflow-lint`, `skillflow-run`, `skillflow-convert`, `skillflow-mcp`
  - Capability-gated I/O with auto-generated `write_*` / `edit_*` tools
  - Immutable SQLite audit trace keyed by `step_instance_id`
- AMOS importables:
  1. `skillflow-lint` → add `skill-check` lint for workflow YAML
  2. `edit_*` staging-first baseline model → strengthen `amos_rename_engine.py`
  3. `step_instance_id` audit trace → extend `amos-observability-driven-harness-evolution-rscf`
  4. `skillflow-mcp` typed MCP tools → export AMOS `amos-workflow-runner` as MCP
- Install blocked by Python 3.12 requirement; host has 3.9.6.

## [2026-08-29] repo evaluation | SkillOS pure-markdown OS

- Cloned `EvolvingAgentsLabs/skillos` to `/tmp/skillos` and inspected `README.md`, `Boot.md`, `skillos.py`, `system/skills/` layout.
- Pure markdown OS: every agent, tool, memory, and orchestration component is a markdown file.
- `Boot.md` is the runtime manifest; `SkillIndex.md` is the hierarchical skill router.
- Runtime requires Python 3.11+; host has 3.9.6, so boot not executed.
- AMOS importables identified:
  1. `Boot.md` + `SkillIndex.md` manifest/router pattern → add `AMOS_BOOT.md` / `SKILL_INDEX.md` to `.devin/` root.
  2. Hierarchical `system/skills/{domain}/{base,index,...}.md` tree → mirror in `07_SKILLS` domain taxonomies.
  3. `memory/short_term/` and `memory/long_term/` → extend `11_KNOWLEDGE/LLM_WIKI/` log and synthesis split.
  4. `projects/[ProjectName]/{components,input,output,memory,state}` workspace template → `amos-integrated-agent` project scaffold.

## [2026-08-29] enhance | SkillOpt/SkillOpt-style Edit/Patch engine in `AMOS_OS/scripts`

- Created `scripts/skill_patch_engine.py` (mirrored from `stitch_project_cosmo` design).
- Provides `Edit` and `Patch` dataclasses with `append`, `insert_after`, `replace`, `delete`.
- Held-out validation gate: rejects candidate edits that break frontmatter delimiters or top heading.
- CLI supports `--patch` JSON or single `--op` with `--target`/`--content`.
- Successful dry-run and real test on `amos-skill-builder/SKILL.md` copy.

## [2026-08-29] lint | LLM_WIKI wikilink scan

- Invoked `amos-llm-wiki` skill and ran a lightweight wikilink lint over `11_KNOWLEDGE/LLM_WIKI/wiki/`.
- Scanned 15 wiki files; found 14 `[[...]]` references whose targets do not exist as sibling `*.md` stems in `wiki/` or `raw/`.
- Most are cross-directory canonical links (`LLM_WIKI_MOC`, `AMOS_LLM_WIKI`, `07_SKILLS_MOC`, `AMOS_RSCF_NODES`) that resolve to other vault directories in Obsidian, so the linter's file-stem check is too strict.
- No true orphan pages found; no contradictions or stale claims flagged in this pass.

## [2026-08-29] repo evaluation | AgentFactory bundle format inspection

- Cloned `zzatpku/AgentFactory` to `/tmp/agentfactory` and inspected `prompt4cc.txt` and sample skills.
- Bundle format confirmed: `SKILL.md` (frontmatter: name, description, entry_file) + `<skill_name>.py` + optional helper scripts.
- `skills_utils.py` parses frontmatter and loads instructions on demand; meta/tools/subagents are organized under `skills/{meta,tools,subagents}/`.
- `prompt4cc.txt` tells Claude Code to read each `SKILL.md` before invoking the Python code.
- AMOS importables:
  1. `entry_file` frontmatter → add to `amos-skill-builder/SKILL.md` frontmatter and `MANIFEST.yaml`.
  2. `skills/{meta,tools,subagents}/` taxonomy → mirror in `.devin/skills/{meta,tools,subagents}/`.
  3. On-demand instructions loading → support progressive disclosure already in `references/`.
  4. `prompt4cc.txt`-style Claude Code prompt → `CLAUDE.md` for `amos-agent-orchestrator`.

## [2026-08-29] repo evaluation | Agent Skill Registry catalog generation and comparison

- Cloned `gfernandf/agent-skill-registry` to `/tmp/agent-skill-registry`.
- Ran `tools/generate_catalog.py` on the host Python 3.9.6; it generated `catalog/capabilities.json` (184 entries) and `catalog/skills.json` (40 entries) successfully.
- Capability schema: `id`, `version`, `description`, `inputs`, `outputs`, `metadata`, `properties`, `cognitive_hints`.
- Skill schema: `id`, `version`, `name`, `description`, `channel`, `domain`, `slug`, `inputs`, `outputs`, `steps`, `uses_capabilities`, `uses_skills`, `metadata`.
- Comparison to AMOS `SKILL.md` frontmatter:
  - Registry `id` uses `domain.noun.verb` dot-notation; AMOS uses `name` as a slug.
  - Registry has typed `inputs`/`outputs` blocks per capability; AMOS has free-form `## Inputs` / `## Outputs` sections in `references/build.md`.
  - Registry `metadata.status` and `metadata.category` are first-class; AMOS has `rscf.state`, `rscf.scope`, `hml_level`, `tags`.
  - Registry skills are dataflow `steps` referencing capabilities by ID; AMOS workflows are narrative `## Steps`.
- AMOS importables:
  1. Dot-notation `capability.id` → add to `amos-skill-builder` capability naming contract.
  2. Typed `inputs`/`outputs` → extend `CONTRACT_TEMPLATE.yaml` with per-capability schema.
  3. `metadata.status` and `metadata.category` → add to `SKILL.md` frontmatter as `status` and `category`.
  4. Dataflow `steps` referencing capability IDs → `amos-workflow-builder` machine-readable output.

## [2026-08-29] repo evaluation | AgentSkills Registry bundle and supply chain

- Cloned `kai98k/agent-skills-registry` to `/tmp/agent-skills-registry`.
- Go/Cobra CLI + HTTP server; `agentskills push|pull|search|vendor` commands.
- Skill bundle: `SKILL.md` + `scripts/` + `references/` + `assets/`.
- Supply chain: `agentskills vendor` locks checksums in a lockfile and restores on new machine.
- Example `SKILL.md` frontmatter: `name`, `version`, `description`, `author`, `tags`.
- AMOS importables:
  1. Bundle structure (`SKILL.md` + `scripts/` + `references/` + `assets/`) → already close to AMOS skill bundles; formalize in `amos-skill-builder` package spec.
  2. `agentskills vendor` checksum lock → extend `skill_guardrail_checker.py` to verify `content_hash` lockfiles.
  3. CLI `push|pull|search` → `amos-skill-registry-gateway` could expose these for `.devin/skills/`.
  4. Semver versioned skills → `skill_version_manager` and `amos-promotion-gates`.

## [2026-08-29] research | SkillOpt README captured and evaluated

- Fetched `microsoft/SkillOpt` README and captured raw source to [[SKILLOPT_README_2026_08_29]].
- Mapped SkillOpt trainable-skill loop, held-out validation gates, and multi-harness evaluation to `amos-skill-builder`, `skill-check`, `amos-validation-pipeline`, and `amos-agent-orchestrator`.
- Updated [[SOTA_AGENT_SKILL_WORKFLOW_REPOS]] with a deep-dive section and recommended next step: sandbox `skillopt` on one AMOS skill.

## [2026-08-29] enhance | Implemented ORPHEUS + SkillOpt importables in `amos-skill-builder`

- Created `stitch_project_cosmo/.devin/scripts/skill_operations_enhancer.py`:
  - `Edit`/`Patch` dataclasses with `append`, `insert_after`, `replace`, `delete` operations.
  - Held-out validation gate: reject candidate edits that break SKILL.md frontmatter or top-heading invariants.
  - CLI supports `--patch` JSON or single `--op` with `--target`/`--content`.
- Added `stitch_project_cosmo/.devin/skills/amos-skill-builder/references/CONTRACT_TEMPLATE.yaml` from ORPHEUS typed I/O contract pattern.
- Re-ran `sota_skill_validator.py`: 642 / 642 skills still 100% SOTA; no regressions.
- Committed to `stitch_project_cosmo`.

## [2026-08-29] research | SkillFlow README captured and evaluated

- Fetched `linxuhao/SkillFlow` README and captured raw source to [[SKILLFLOW_README_2026_08_29]].
- Mapped SkillFlow YAML DAG executor, capability-gated I/O, human checkpoints, and MCP transport to `amos-workflow-runner`, `amos-skill-builder`, `amos-routing-audit`, `amos-promotion-gates`, and `amos-observability-driven-harness-evolution-rscf`.
- Updated [[SOTA_AGENT_SKILL_WORKFLOW_REPOS]] with a deep-dive section and recommended next step: install `skillflow-py` and convert one AMOS workflow.

## [2026-08-29] enhance | Imported SkillOS `Boot.md` + `SkillIndex.md` pattern into AMOS `.devin/`

- Created `stitch_project_cosmo/.devin/AMOS_BOOT.md` as the runtime manifest (boot checklist, capabilities, invariants).
- Created `stitch_project_cosmo/.devin/SKILL_INDEX.md` as the hierarchical skill router with:
  - 642 total skills across 45 unique `domain` values
  - 24 parent-skill roots
  - Usage protocol and canonical tree links to `[[07_SKILLS_MOC]]` / `[[AMOS_RSCF_NODES]]`
- Re-ran `sota_skill_validator.py`: 642 / 642 skills still 100%.
- Committed to `stitch_project_cosmo`.

## [2026-08-29] research | AgentFactory README captured and evaluated

- Fetched `zzatpku/AgentFactory` README and captured raw source to [[AGENTFACTORY_README_2026_08_29]].
- Mapped AgentFactory meta-agent, subagent skill library, and self-evolution loop to `amos-agent-orchestrator`, `amos-skill-builder`, `amos-evolution-loop`, and `amos-brain-model-integration`.
- Updated [[SOTA_AGENT_SKILL_WORKFLOW_REPOS]] with a deep-dive section and recommended next step: inspect `prompt4cc.txt` for bundle format comparison.

## [2026-08-29] research | Agent Skill Registry README captured and evaluated

- Fetched `gfernandf/agent-skill-registry` README and captured raw source to [[AGENT_SKILL_REGISTRY_README_2026_08_29]].
- Mapped controlled vocabulary, declarative skill dataflow, machine-readable catalog, and governance guardrails to `amos-skill-builder`, `amos-workflow-builder`, `amos-skill-catalog-generator`, `skill_guardrail_checker`, and `skill_version_manager`.
- Updated [[SOTA_AGENT_SKILL_WORKFLOW_REPOS]] with a deep-dive section and recommended next step: generate and compare registry catalog to AMOS `SKILL.md` frontmatter.

## [2026-08-29] enhance | Imported AgentFactory bundle conventions into AMOS skill builder and agent orchestrator

- Added `entry_file: scripts/validate.py` to `stitch_project_cosmo/.devin/skills/amos-skill-builder/SKILL.md` frontmatter and `MANIFEST.yaml` to align with AgentFactory `SKILL.md` + Python `entry_file` pattern.
- Added `stitch_project_cosmo/.devin/skills/amos-agent-orchestrator/CLAUDE.md` as a Claude Code prompt enforcing boot checklist, dispatch protocol, content-hash verification, and provenance logging.
- Re-ran `sota_skill_validator.py`: 642 / 642 skills still 100%.
- Committed to `stitch_project_cosmo`.

## [2026-08-29] research | AgentSkills Registry README captured and evaluated

- Fetched `kai98k/agent-skills-registry` README and captured raw source to [[AGENTSKILLS_REGISTRY_README_2026_08_29]].
- Mapped Skill Bundle format, `vendor`/`lock` supply-chain model, semver, and self-hosted registry to `amos-skill-builder`, `skill_integrity_lock.py`, `skill_version_manager.py`, `amos-skill-registry-gateway`, and `amos-mcp-connector`.
- Updated [[SOTA_AGENT_SKILL_WORKFLOW_REPOS]] with a deep-dive section and recommended next step: package one AMOS skill as AgentSkills-compatible `.tar.gz`.

## [2026-08-29] enhance | Imported Agent Skill Registry and AgentSkills Registry conventions into `amos-skill-builder`

- Extended `stitch_project_cosmo/.devin/skills/amos-skill-builder/references/CONTRACT_TEMPLATE.yaml` with `capabilities` typed I/O schema, dot-notation `id`, and `metadata.status/category`.
- Added `stitch_project_cosmo/.devin/skills/amos-skill-builder/references/CAPABILITY_NAMING_CONTRACT.md` formalizing `domain.noun.verb` capability identifiers.
- Added `status`, `category`, `bundle_format`, and `assets_dir` to `amos-skill-builder/SKILL.md` and `MANIFEST.yaml`.
- Re-ran `sota_skill_validator.py`: 642 / 642 skills still 100%.
- Committed to `stitch_project_cosmo`.

## [2026-08-29] research | XSkill README captured and evaluated

- Fetched `XSkill-Agent/XSkill` README and captured raw source to [[XSKILL_README_2026_08_29]].
- Mapped XSkill two-phase accumulation/inference loop, experience/skill memory bank, and trajectory-to-skill document builder to `amos-memory-systems-master`, `amos-llm-wiki`, `amos-observability-driven-harness-evolution-rscf`, `amos-agent-orchestrator`, `amos-skill-builder`, and `amos-multimodal-perception-layer`.
- Updated [[SOTA_AGENT_SKILL_WORKFLOW_REPOS]] with a deep-dive section and recommended next step: compare XSkill `skill_builder.py` output to AMOS `SKILL.md` frontmatter.

## [2026-08-29] audit | AMOS skill names and descriptions already comply with Agent Skills spec

- Fetched the canonical `agentskills/agentskills` README and `https://agentskills.io/specification`.
- Captured raw sources to `[[AGENTSKILLS_SPEC_README_2026_08_29]]` and `[[AGENTSKILLS_SPECIFICATION_2026_08_29]]`.
- Ran a programmatic check of all 642 `stitch_project_cosmo/.devin/skills/*/SKILL.md` frontmatters against the spec:
  - `name`: 1-64 chars, lowercase alphanumeric + hyphens, no leading/trailing/consecutive hyphens.
  - `description`: max 1024 chars.
- Result: 0 violations. AMOS skill bundles already follow the Agent Skills naming and size conventions.
- Progressive disclosure (metadata → instructions → resources) already matches AMOS `references/` and `scripts/` pattern.

## [2026-08-29] enhance | Aligned `amos-skill-builder` with canonical Agent Skills spec optional frontmatter

- Added `compatibility` and `allowed-tools` optional frontmatter fields to `stitch_project_cosmo/.devin/skills/amos-skill-builder/SKILL.md` and `references/CONTRACT_TEMPLATE.yaml` per agentskills.io.
- Re-ran `sota_skill_validator.py`: 642 / 642 skills still 100%.
- Committed to `stitch_project_cosmo`.

## [2026-08-29] research | OpenSkills SDK README captured and evaluated

- Fetched `ljluestc/OpenSkills` README and captured raw source to [[OPENSKILLS_README_2026_08_29]].
- Mapped three-layer progressive disclosure, reference loading modes, auto-discovery, and `[INVOKE:name]` script execution to `amos-skill-builder`, `amos-workflow-runner`, `amos-agent-orchestrator`, `amos-security-safety-master`, and `amos-os-runtime-master`.
- Updated [[SOTA_AGENT_SKILL_WORKFLOW_REPOS]] with a deep-dive section and recommended next step: add `triggers` and `references` loading-mode metadata to AMOS `SKILL.md` frontmatter.

## [2026-08-29] enhance | Aligned `amos-skill-builder` with OpenSkills `triggers` and `references` loading modes

- Added `triggers` and `references` (with `path` and `mode`) optional frontmatter fields to `stitch_project_cosmo/.devin/skills/amos-skill-builder/SKILL.md` and `references/CONTRACT_TEMPLATE.yaml` per OpenSkills SDK.
- Re-ran `sota_skill_validator.py`: 642 / 642 skills still 100%.
- Committed to `stitch_project_cosmo`.

## [2026-08-29] research | MMSkills for Visual Agents README captured and evaluated

- Fetched `zkangning/MMSkills_for_Visual_Agents` README and captured raw source to [[MMSKILLS_README_2026_08_29]].
- Mapped self-contained multimodal skill packages, visual keyframes, evidence gating, and branch-loaded planning to `amos-multimodal-perception-layer`, `amos-structured-document-parsing-rscf`, `amos-boundary-scope-master`, `amos-context-budget-governor-rscf`, `amos-agent-orchestrator`, `amos-workflow-runner`, `amos-mcp-connector`, and `amos-skill-registry-gateway`.
- Updated [[SOTA_AGENT_SKILL_WORKFLOW_REPOS]] with a deep-dive section and recommended next step: prototype `assets/` and visual keyframes in one AMOS skill.

## [2026-08-29] research | AgentSkillOS README captured and evaluated

- Fetched `songfang/AgentSkillOS` README and captured raw source to [[AGENTSKILLOS_README_2026_08_29]].
- Mapped 90,000+ skill ecosystem, skill tree construction, complementarity-aware retrieval, and DAG-based orchestration to `SKILL_INDEX.md`, `07_SKILLS_MOC`, `amos-routing-audit`, `amos-agent-orchestrator`, `amos-workflow-builder`, `amos-workflow-runner`, `amos-promotion-gates`, `amos-human-interaction-engine`, `amos-observability-driven-harness-evolution-rscf`, and `amos-decision-logger`.
- Updated [[SOTA_AGENT_SKILL_WORKFLOW_REPOS]] with a deep-dive section and recommended next step: generate a capability tree from 642 AMOS skills and compare to AgentSkillOS pre-built trees.

## [2026-08-29] enhance | Generated AMOS skill capability tree `SKILL_TREE.json` for AgentSkillOS comparison

- Parsed all 642 `stitch_project_cosmo/.devin/skills/*/SKILL.md` frontmatters.
- Generated `.devin/SKILL_TREE.json` with `by_parent` (24 roots) and `by_domain` (45 domains) views.
- Re-ran `sota_skill_validator.py`: 642 / 642 skills still 100%.
- Committed to `stitch_project_cosmo`.

## [2026-08-29] research | Production skill marketplaces and hardened registries captured

- Fetched `tech-leads-club/agent-skills` README and captured raw source to [[TECH_LEADS_CLUB_AGENT_SKILLS_README_2026_08_29]].
- Fetched `ivanzwb/agent-skills` README and captured raw source to [[IVANZWB_AGENT_SKILLS_README_2026_08_29]].
- Fetched `ComeOnOliver/skillshub` README and captured raw source to [[SKILLSHUB_README_2026_08_29]].
- Updated [[SOTA_AGENT_SKILL_WORKFLOW_REPOS]] with a Search 4 section mapping hardened registries, TypeScript skill lifecycle, and token-efficient resolver to `skill_guardrail_checker.py`, `skill_security_scanner.py`, `SKILL_TREE.json`, `amos-promotion-gates`, `skill-check`, `amos-skill-builder`, `amos-skill-registry-gateway`, `amos-routing-audit`, `amos-agent-orchestrator`, and `amos-llm-wiki`.

## [2026-08-29] enhance | Added Agent Skills-compatible `manifest.json` to `amos-skill-builder`

- Created `stitch_project_cosmo/.devin/skills/amos-skill-builder/manifest.json` with tool declarations for `validate_skill`, `package_skill`, and `list_skills` aligned with `ivanzwb/agent-skills` Agent Skills Specification implementation.
- Re-ran `sota_skill_validator.py`: 642 / 642 skills still 100%.
- Committed to `stitch_project_cosmo`.

## [2026-08-29] fix + enhance | Added `amos-skill-builder/scripts/validate.py` and wired visual keyframes into `amos-multimodal-perception-layer`

- Created `stitch_project_cosmo/.devin/skills/amos-skill-builder/scripts/validate.py` to validate `SKILL.md` frontmatter against Agent Skills `name`/`description`/`version` rules and AMOS SOTA constraints. Resolves the missing `entry_file: scripts/validate.py`.
- Added `multimodal_perception.gate_visual_keyframe` capability and `assets/visual_keyframe_template.md` reference to `amos-multimodal-perception-layer/SKILL.md`.
- Re-ran `sota_skill_validator.py`: 642 / 642 skills still 100%.
- Committed to `stitch_project_cosmo`.

## [2026-08-29] research | Anthropic Skills README captured and evaluated

- Fetched `anthropics/skills` README and captured raw source to [[ANTHROPICS_SKILLS_README_2026_08_29]].
- Mapped canonical Claude Code plugin marketplace, document skills, and basic skill template to `amos-pdfs`, `amos-docx`, `amos-slides`, `spreadsheets`, `amos-skill-builder`, `amos-skill-registry-gateway`, and `amos-mcp-connector`.
- Updated [[SOTA_AGENT_SKILL_WORKFLOW_REPOS]] with a deep-dive section and recommended next step: compare `anthropics/skills/template` and `spec` to AMOS `CONTRACT_TEMPLATE.yaml`.

## [2026-08-29] research | Anthropic Skills template and spec captured

- Fetched `anthropics/skills/template/SKILL.md` and `spec/agent-skills-spec.md`.
- Captured raw sources to `[[ANTHROPICS_SKILLS_TEMPLATE_2026_08_29]]` and noted the spec is canonical `agentskills.io/specification` (already captured as `[[AGENTSKILLS_SPECIFICATION_2026_08_29]]`).
- Comparison to `amos-skill-builder/references/CONTRACT_TEMPLATE.yaml`:
  - Anthropic template only requires `name` and `description` frontmatter.
  - AMOS `CONTRACT_TEMPLATE.yaml` is already a strict superset: `schema_version`, `version`, `status`, `category`, `compatibility`, `allowed-tools`, `triggers`, `references`, typed `input`/`output`, `capabilities`, `rscf` metadata, and governance fields.
- No changes needed; AMOS skill frontmatter already exceeds the canonical minimal template and covers the full `agentskills.io` specification.

## [2026-08-29] research | SkillOS and ai-os READMEs captured and evaluated

- Fetched `EvolvingAgentsLabs/skillos` README (frozen 2026-08-01) and captured raw source to [[SKILL_OS_README_2026_08_29]].
- Fetched `EvolvingAgentsLabs/ai-os` README (active successor) and captured raw source to [[AI_OS_README_2026_08_29]].
- Mapped pure markdown OS, hierarchical skill tree, 4-step lazy loading, HWM planning, dialects, memory wiki, and `truth/` external gates to `amos-skill-builder`, `amos-agent-orchestrator`, `amos-cognitive-compression-kernel`, `amos-memory-systems-master`, `amos-llm-wiki`, `amos-claim-verifier`, `amos-audit-repair-master`, `amos-decision-logger`, and `sota_skill_validator.py`.
- Updated [[SOTA_AGENT_SKILL_WORKFLOW_REPOS]] with a deep-dive section and recommended next step: add 3-level Domain → Family → Skill view to `.devin/SKILL_TREE.json` and a `make reproduce` target for the AMOS SOTA validator.

## [2026-08-30] fix + enhance | Resolved vault orphan graph and captured addyosmani/agent-skills

- Ran `AMOS_OBSIDIAN_MEMORY_BRIDGE.py` and found 2 orphan notes: `Agent Skills` (Addy Osmani raw capture) and `AMOS Global Contract for AI Coding Agents` (`.github/copilot-instructions.md`).
- Fixed `cosmo-brain/AMOS_OBSIDIAN_MEMORY_BRIDGE.py` wikilink resolution to match `[[Title]]` against note H1/frontmatter title (`title_to_path`), not only file paths/basenames.
- Re-linked the two orphans into `00_ROOT/00_COSMO_BRAIN_MOC.md`.
- Re-verified orphan count: 0; vault graph connected.
- Captured `addyosmani/agent-skills` README and stored raw source in `11_KNOWLEDGE/LLM_WIKI/raw/ADDYOSMANI_AGENT_SKILLS_README_2026_08_30.md`.
- Committed to `stitch_project_cosmo` and `AMOS_OS`.

## [2026-08-30] research | Captured context-engineering and SDLC-standards skill frameworks

- Fetched `muratcankoylan/Agent-Skills-for-Context-Engineering` README and captured raw source to [[AGENT_SKILLS_FOR_CONTEXT_ENGINEERING_README_2026_08_30]].
- Fetched `HoangNguyen0403/agent-skills-standard` README and captured raw source to [[AGENT_SKILLS_STANDARD_README_2026_08_30]].
- Updated [[SOTA_AGENT_SKILL_WORKFLOW_REPOS]] with deep dives mapping context engineering, harness engineering, progressive disclosure, Claude Code plugin marketplace, `ags` CLI, lockfile verification, MCP runtime enforcement, and pre-edit hooks to AMOS skills.

## [2026-08-30] research | Captured three curated skill marketplaces and catalogs

- Fetched `pedronauck/skills` README and captured raw source to [[PEDRONAUCK_SKILLS_README_2026_08_30]].
- Fetched `heyimcarlos/agent-skills` README and captured raw source to [[HEYIMCARLOS_AGENT_SKILLS_README_2026_08_30]].
- Fetched `netresearch/claude-code-marketplace` README and captured raw source to [[NETRESEARCH_CLAUDE_CODE_MARKETPLACE_README_2026_08_30]].
- Updated [[SOTA_AGENT_SKILL_WORKFLOW_REPOS]] with deep dives covering bucket-based storage, QRSPI workflows, subagents, `disable-model-invocation`, `plugin.json` + `skills/` packaging, and multi-language marketplace sites.

## [2026-08-30] research | Fetched zjunlp/SkillNet README for direct AMOS trial

- Web-fetched `https://raw.githubusercontent.com/zjunlp/SkillNet/main/README.md` and placed raw source at `11_KNOWLEDGE/LLM_WIKI/raw/ZJUNLP_SKILLNET_README_2026_08_30.md`.
- Noted 500K+ indexed GitHub skills, 5-dimension skill quality scoring, and a portable `skills/skillnet/` agent skill for Claude Code / Codex / MCP.
- Recommended next step: clone the `skills/skillnet` package into AMOS `.devin/skills/amos-skillnet/` and run `sota_skill_validator.py` on it.

## [2026-08-30] implement | Imported SkillOS `SkillIndex.md` and wired it into AMOS boot

- Copied `SkillOS` `CLAUDE.md` to `11_KNOWLEDGE/LLM_WIKI/raw/SKILLOS_CLAUDE_MD_2026_08_30.md`.
- Created `.devin/skills/SkillIndex.md` (~51 lines) as the SkillOS-style top-level skill routing index, listing the 24 root/master domains from `.devin/SKILL_TREE.json` and cross-cutting skills.
- Updated `.devin/AMOS_BOOT.md` to load `.devin/skills/SkillIndex.md` first, then `.devin/SKILL_TREE.json`.

## [2026-08-30] implement | Cloned zjunlp/SkillNet and imported `amos-skillnet` into AMOS

- Cloned `zjunlp/SkillNet` and copied `skills/skillnet/` into `.devin/skills/amos-skillnet/`.
- AMOS-linted `SKILL.md` frontmatter and appended governance sections (regression prevention, grounding, verification, data trustworthiness).
- Created `.devin/agents/amos-skillnet-agent.json` and `.devin/workflows/amos-skillnet-workflow.md`.
- Updated `.devin/skills/SkillIndex.md` to 643 skills and added `amos-skillnet` cross-cutting route.
- `make validate`: 643/643 skills at 100% SOTA.
- `agent_sync_validator.py`: 670/670 agents valid, 0 invalid.

## [2026-08-30] close | amos-skillnet SOTA validated and committed

- Re-ran `.devin/scripts/sota_skill_validator.py` against full `.devin/skills` corpus: 643/643 skills at 100% SOTA, 0 critical, 0 warnings.
- Wired `amos-skillnet` cross-cutting route into `.devin/skills/SkillIndex.md`.
- Re-ran `agent_sync_validator.py`: 670/670 agents valid, 0 invalid.
- Committed `amos-skillnet` skill package, agent JSON, workflow, and `SkillIndex.md` to `stitch_project_cosmo`.

## [2026-08-30] research | Captured Vercel Labs `skills` CLI README

- Fetched `vercel-labs/skills` README and captured raw source to [[VERCEL_LABS_SKILLS_README_2026_08_30]].
- Added deep-dive to [[SOTA_AGENT_SKILL_WORKFLOW_REPOS]] mapping `npx skills add/use/find/init`, source formats, installation scope, symlink vs copy, and 73+ supported agents to AMOS skills.

## [2026-08-30] research | Captured canonical Agent Skills spec and Anthropic skills template

- Fetched `agentskills.io/specification` and captured to [[AGENTSKILLS_IO_SPECIFICATION_2026_08_30]].
- Fetched `anthropics/skills` README, template `SKILL.md`, and `spec/agent-skills-spec.md` to `ANTHROPICS_SKILLS_*` raw captures.
- Added deep-dive to [[SOTA_AGENT_SKILL_WORKFLOW_REPOS]] comparing `name`/`description`/`compatibility`/`allowed-tools`/`metadata`/`references` progressive disclosure to AMOS `CONTRACT_TEMPLATE.yaml` and `sota_skill_validator.py`.
- Recommended next step: add `allowed-tools` scoping examples to `CONTRACT_TEMPLATE.yaml` and evaluate enforcing `name` (64) and `description` (1024) length limits.

## [2026-08-30] implement | Added Agent Skills spec G13/G14 gates to `sota_skill_validator.py`

- Added `G13` — name format per `agentskills.io` spec (<=64 chars, lowercase alnum/hyphen, no leading/trailing/consecutive hyphens).
- Added `G14` — description length <=1024 chars per `agentskills.io` spec.
- Updated gate list, gate names table, and fix-actions in the validator.
- Ran `make validate`: 643/643 skills at 100% SOTA, 0 critical, 0 warnings.
- Out of 643 skills, 0 have name or description length/format drift against the spec.

## [2026-08-30] implement | Added G15/G16 to `sota_skill_validator.py`

- Added `G15` — `compatibility` <=500 chars.
- Added `G16` — `allowed-tools` format (known tools or `Bash(scope:*)` scoping).
- Fixed `amos-0704-3643v1-sabbath-day-home-automation-it-s-like-mixing-te` `allowed-tools` from `Read skill` to `Read`.
- `make validate`: 643/643 skills, 100% SOTA across 16 gates.
- New recommended next step in `SOTA_AGENT_SKILL_WORKFLOW_REPOS`: capture and AMOS-lint the `SkillOS` `CLAUDE.md` pattern as `amos-skillos`.

## [2026-08-30] implement | Imported SkillOS `CLAUDE.md` as `amos-skillos` and wired into AMOS

- Copied `/private/tmp/skillos/CLAUDE.md` to `.devin/skills/amos-skillos/references/skillos-claude.md`.
- Wrote `SKILL.md` with SkillOS boot, scaffold, execute, and agent/tool creation instructions.
- Added `references/skillos-manifest.md` and `scripts/skillos_setup.sh`.
- Created `.devin/agents/amos-skillos-agent.json` and `.devin/workflows/amos-skillos-workflow.md`.
- Updated `.devin/skills/SkillIndex.md` to 644 skills and added `amos-skillos` cross-cutting route.
- `make validate`: 644/644 skills at 100% SOTA.
- `agent_sync_validator.py`: 671/671 agents valid.

## [2026-08-30] research | Captured Microsoft SkillOpt latest README

- Fetched `microsoft/SkillOpt` `main` README and captured to [[MICROSOFT_SKILLOPT_README_2026_08_30]].
- Added deep-dive to [[SOTA_AGENT_SKILL_WORKFLOW_REPOS]] covering v0.2.0, `SkillOpt-Sleep`, supported backends, integration shells for Claude Code/Codex/Copilot/Devin, and AMOS integration points.

## [2026-08-30] research | Captured ORPHEUS latest README

- Fetched `nuryslyrt/ORPHEUS` main README and captured to [[ORPHEUS_README_2026_08_30]].
- Added deep-dive to [[SOTA_AGENT_SKILL_WORKFLOW_REPOS]] covering the `.orpheus/` tree, Builder/Doctor/Auditor/Surgeon meta-roles, decision logs, error chain preservation, and AMOS integration points.

## [2026-08-30] implement | Imported XSkill as `amos-xskill`

- Fetched `XSkill-Agent/XSkill` README and captured to `11_KNOWLEDGE/LLM_WIKI/raw/XSKILL_README_2026_08_30.md`.
- Created `amos-xskill` skill with references and scaffold script.
- Added `amos-xskill-agent.json` and `amos-xskill-workflow.md`.
- Updated `SkillIndex.md` to 645 skills.
- `make validate`: 645/645 skills at 100% SOTA; `agent_sync_validator.py`: 672/672 agents valid.
- Logged implementation and next steps in `SOTA_AGENT_SKILL_WORKFLOW_REPOS`.

## 2026-08-30 | implement | Added G17/G18 to `sota_skill_validator.py` and aligned AMOS contract with OpenSkills progressive disclosure

Implemented the vault recommendation from OpenSkills to add `triggers` and `references` loading-mode metadata to the AMOS `SKILL.md` frontmatter and `CONTRACT_TEMPLATE.yaml`.

### Results

- Added `G17` — `triggers` must be a YAML list of strings.
- Added `G18` — `references` must be a YAML list of dicts with `path` and `mode` (`explicit`, `implicit`, `always`); `explicit` requires a `condition`.
- Fixed `amos-skillnet/SKILL.md`:
  - `triggers` converted from comma-separated string to YAML list.
  - `references` converted from comma-separated string to YAML list with `mode: implicit/always/implicit`.
  - `allowed-tools` normalized `Exec` → `exec`.
- Updated `amos-skill-builder/references/CONTRACT_TEMPLATE.yaml`:
  - Added an `explicit` reference entry with a `condition` example.
  - Added `scripts` block with `name`, `path`, `description`, `timeout`.
  - Added `assets` block with `path` and `description`.
- `make validate`: 645/645 skills at 100% SOTA across 18 gates.
- `agent_sync_validator.py`: 672/672 agents valid.

### AMOS integration points

- `CONTRACT_TEMPLATE.yaml` now matches OpenSkills L1/L2/L3 progressive disclosure and Agent Skills bundle format.
- `sota_skill_validator.py` G17/G18 enforce these frontmatter conventions corpus-wide.
- `amos-skillnet` is now a clean example of the new `triggers`/`references` list format.

### Recommended next step

Continue scanning for the next SOTA repo to capture, or implement the next vault hardening task such as adding `assets/` directory support to `sota_skill_validator.py` or creating an `amos-openskills` skill that wraps the `openskills-sdk` progressive disclosure runtime.

## [2026-08-30] implement | Added G19 and imported MMSkills as `amos-mmskills`

- Added `G19` (`assets` frontmatter format) to `sota_skill_validator.py`.
- Fetched `zkangning/MMSkills_for_Visual_Agents` README and captured to `11_KNOWLEDGE/LLM_WIKI/raw/MMSKILLS_README_2026_08_30.md`.
- Created `amos-mmskills` skill with references and scaffold script.
- Added `amos-mmskills-agent.json` and `amos-mmskills-workflow.md`.
- Updated `SkillIndex.md` to 646 skills.
- `make validate`: 646/646 skills at 100% SOTA; `agent_sync_validator.py`: 673/673 agents valid.
- Logged implementation and next steps in `SOTA_AGENT_SKILL_WORKFLOW_REPOS`.

## [2026-08-30] implement | Imported AgentSkillOS as `amos-agentskillos`

- Fetched `ynulihao/AgentSkillOS` README and captured to `11_KNOWLEDGE/LLM_WIKI/raw/AGENTSKILLOS_README_2026_08_30.md`.
- Created `amos-agentskillos` skill with references and scaffold script.
- Added `amos-agentskillos-agent.json` and `amos-agentskillos-workflow.md`.
- Updated `SkillIndex.md` to 647 skills.
- `make validate`: 647/647 skills at 100% SOTA; `agent_sync_validator.py`: 674/674 agents valid.
- Logged implementation and next steps in `SOTA_AGENT_SKILL_WORKFLOW_REPOS`.

## [2026-08-30] implement | Added AMOS workflow validator and `make workflows` target

- Created `.devin/scripts/workflow_validator.py` to validate 683 AMOS workflow files for binding and structure.
- Added `make workflows` target to `Makefile`.
- `make validate`: 649/649 skills at 100% SOTA; `make workflows`: 683/683 workflows pass; `agent_sync_validator.py`: 676/676 agents valid.
- Logged next step (auto-add titles/sections to close 676 warnings) in `SOTA_AGENT_SKILL_WORKFLOW_REPOS`.

## [2026-08-30] finalize | Workflow validator passes with 8 warnings; 650 skills, 677 agents, 684 workflows

- Improved `workflow_validator.py` title detection to support YAML frontmatter `title`.
- `make validate`: 650/650 skills at 100% SOTA.
- `make workflows`: 684/684 workflows pass with 8 structural warnings.
- `agent_sync_validator.py`: 677/677 agents valid.
- Clean working tree.
- Logged next steps in `SOTA_AGENT_SKILL_WORKFLOW_REPOS`.
