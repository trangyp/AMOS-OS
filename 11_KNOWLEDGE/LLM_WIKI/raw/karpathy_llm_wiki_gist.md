---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Karpathy Llm Wiki Gist
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# Karpathy LLM Wiki Gist (Raw)

**URL:** https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

**Excerpt (not a substitute for the original source):**

> Instead of just retrieving from raw documents at query time, the LLM incrementally builds and maintains a persistent wiki — a structured, interlinked collection of markdown files. The wiki is a persistent, compounding artifact. The cross-references are already there; the contradictions have already been flagged; the synthesis already reflects everything you’ve read.

**Architecture**

1. Raw sources — immutable source documents.
1. The wiki — LLM-generated markdown pages.
1. The schema — a document telling the LLM how the wiki is structured.

**Operations**

- Ingest — read source, write summary, update pages, update index, append log.
- Query — read index, synthesize answer, file valuable answers back into the wiki.
- Lint — check contradictions, orphans, stale claims, missing pages.

**Indexing**

- `index.md` — content catalog.
- `log.md` — chronological activity log.

See [[11_KNOWLEDGE/LLM_WIKI/wiki/karpathy_llm_wiki_summary|karpathy_llm_wiki_summary]] for an AMOS-vault interpretation.

______________________________________________________________________

RSCF-NODE
node_id: karpathy_llm_wiki_gist
node_type: source
path: 11_KNOWLEDGE/LLM_WIKI/raw/karpathy_llm_wiki_gist.md
RSCF-RELATIONS:

- INDEXED_BY: [[11_KNOWLEDGE/LLM_WIKI/raw/LLM_WIKI_RAW_README|LLM_WIKI_RAW_README]]
- SUMMARIZED_BY: [[11_KNOWLEDGE/LLM_WIKI/wiki/karpathy_llm_wiki_summary|karpathy_llm_wiki_summary]]
  claim_class: SOURCE_CLAIM

______________________________________________________________________

**MOC:** [[11_KNOWLEDGE/LLM_WIKI/LLM_WIKI_MOC|LLM_WIKI_MOC]]
