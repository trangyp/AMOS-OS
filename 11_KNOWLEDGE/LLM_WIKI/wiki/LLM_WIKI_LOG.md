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
