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
