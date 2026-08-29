---
title: LLM Wiki Index
type: index
source: 11_KNOWLEDGE/LLM_WIKI
tags:
- index
- llm-wiki
- canon/knowledge
- karpathy-llm-wiki-summary
- llm-wiki-pattern
- amos-llm-wiki
- llm-wiki-index
- llm-wiki-log
- amos-llm-wiki-operations
- amos-llm-wiki-tool
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_knowledge
---

# LLM Wiki Index

Content catalog for the AMOS LLM Wiki. Updated on every ingest, query, and lint.

## Sources

| Page | Summary | Source count |
|------|---------|--------------|
| [[karpathy_llm_wiki_summary]] | Karpathy's LLM Wiki pattern, adapted for AMOS | 1 |
| [[SOTA_AGENT_SKILL_WORKFLOW_REPOS_2026_08_25]] | Raw capture of SOTA agent, skill and workflow repos | 2 |
| [[ZJUNLP_SKILLNET_README_2026_08_30]] | zjunlp/SkillNet README, re-fetched for AMOS trial | 1 |

## Concepts

| Page | Summary |
|------|---------|
| [[llm_wiki_pattern]] | The compounding-knowledge wiki architecture |

## Entities

| Page | Summary |
|------|---------|
| [[AMOS_LLM_WIKI]] | Schema and directory layout for the AMOS LLM Wiki |
| [[LLM_WIKI_MOC]] | Map of Content for the wiki subsystem |
| [[LLM_WIKI_INDEX]] | This content catalog |
| [[LLM_WIKI_LOG]] | Chronological activity log |

## Syntheses

| Page | Summary |
|------|---------|
| [[karpathy_llm_wiki_summary]] | AMOS interpretation of Karpathy's gist |
| [[amos_llm_wiki_operations]] | Ingest, query, lint, and clip for the AMOS wiki |
| [[SOTA_AGENT_SKILL_WORKFLOW_REPOS]] | Synthesized SOTA agent/skill/workflow repo guide |

## Tools

| Page | Summary |
|------|---------|
| [[AMOS_LLM_WIKI_TOOL]] | Obsidian Web Clipper, qmd, grep, Dataview guide |

## Activity
- [[LLM_WIKI_LOG]] — Chronological log

---
RSCF-NODE
node_id: llm_wiki_index
node_type: index
path: 11_KNOWLEDGE/LLM_WIKI/wiki/LLM_WIKI_INDEX.md
RSCF-RELATIONS:
  - INDEXED_BY: [[LLM_WIKI_MOC]]
claim_class: AMOS_MODEL

---
**MOC:** [[LLM_WIKI_MOC]]

## 2026-08-29 updates

- New raw source: [[SOTA_AGENT_SKILL_WORKFLOW_REPOS_2026_08_29]] · [[SKILLNET_README_2026_08_29]]
- Updated synthesis: [[SOTA_AGENT_SKILL_WORKFLOW_REPOS]]
- Activity logged: [[LLM_WIKI_LOG]]

## 2026-08-30 updates

- New raw source: [[ZJUNLP_SKILLNET_README_2026_08_30]]
- Updated index and log: [[LLM_WIKI_INDEX]] · [[LLM_WIKI_LOG]]
- Done: `amos-skillnet` cloned, AMOS-linted, SOTA-validated, and wired into `SkillIndex.md`; logged in [[LLM_WIKI_LOG]]
