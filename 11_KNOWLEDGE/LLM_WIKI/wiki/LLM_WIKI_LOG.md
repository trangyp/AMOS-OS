---
title: LLM Wiki Log
type: log
source: 11_KNOWLEDGE/LLM_WIKI
tags:
- log
- llm-wiki
- canon/knowledge
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
- Added links to `[[_MOC]]` and `[[KNOWLEDGE_MOC]]`
- First raw source: [Karpathy LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- First wiki page: [[karpathy_llm_wiki_summary]]

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
