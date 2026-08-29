---
title: Karpathy LLM Wiki Gist
type: raw
source: 11_KNOWLEDGE/LLM_WIKI/raw
tags:
- raw
- source
- llm-wiki
- karpathy-llm-wiki-summary
- llm-wiki-raw-readme
- llm-wiki-moc
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
  scope: AMOS_knowledge
---

# Karpathy LLM Wiki Gist (Raw)

**URL:** https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

**Excerpt (not a substitute for the original source):**

> Instead of just retrieving from raw documents at query time, the LLM incrementally builds and maintains a persistent wiki — a structured, interlinked collection of markdown files. The wiki is a persistent, compounding artifact. The cross-references are already there; the contradictions have already been flagged; the synthesis already reflects everything you’ve read.

**Architecture**
1. Raw sources — immutable source documents.
2. The wiki — LLM-generated markdown pages.
3. The schema — a document telling the LLM how the wiki is structured.

**Operations**
- Ingest — read source, write summary, update pages, update index, append log.
- Query — read index, synthesize answer, file valuable answers back into the wiki.
- Lint — check contradictions, orphans, stale claims, missing pages.

**Indexing**
- `index.md` — content catalog.
- `log.md` — chronological activity log.

See [[karpathy_llm_wiki_summary]] for an AMOS-vault interpretation.

---
RSCF-NODE
node_id: karpathy_llm_wiki_gist
node_type: source
path: 11_KNOWLEDGE/LLM_WIKI/raw/karpathy_llm_wiki_gist.md
RSCF-RELATIONS:
  - INDEXED_BY: [[LLM_WIKI_RAW_README]]
  - SUMMARIZED_BY: [[karpathy_llm_wiki_summary]]
claim_class: SOURCE_CLAIM

---
**MOC:** [[LLM_WIKI_MOC]]
