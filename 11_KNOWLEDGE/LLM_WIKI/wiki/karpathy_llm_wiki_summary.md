---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Karpathy Llm Wiki Summary
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

# Karpathy LLM Wiki Pattern

**Source:** [llm-wiki.md](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)

## Core idea

Most LLM-document workflows are RAG: the LLM re-derives answers from raw documents each time. Karpathy's pattern instead builds a persistent, compounding markdown wiki. The LLM ingests a source once, updates entity and concept pages, and maintains an evolving synthesis. Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.

## Architecture

1. **Raw sources** — immutable source documents.
1. **The wiki** — LLM-generated markdown pages, cross-linked.
1. **The schema** — a document (e.g., `CLAUDE.md` or `AGENTS.md`) that tells the LLM how to maintain the wiki.

## Operations

- **Ingest** — read the source, write a summary, update relevant concept/entity pages, update `index.md`, append `log.md`.
- **Query** — read `index.md`, synthesize an answer from relevant pages, optionally file the answer back into the wiki.
- **Lint** — check for contradictions, stale claims, orphan pages, missing concept pages, and data gaps.

## Indexing and logging

- `index.md` — content-oriented catalog of all wiki pages.
- `log.md` — chronological, append-only record of ingests, queries, and lint passes.

## Practical tips

- Use Obsidian Web Clipper to get web articles into markdown.
- Download images locally to a fixed attachment folder.
- Use Obsidian's graph view to see wiki structure.
- Marp and Dataview can produce decks and dynamic tables.
- `qmd` is a local search option for larger wikis.

## AMOS integration

The AMOS vault instantiates this pattern as the `LLM_WIKI` subsystem under `11_KNOWLEDGE/LLM_WIKI/`, governed by \`\`.

______________________________________________________________________

RSCF-NODE
node_id: karpathy_llm_wiki_summary
node_type: note
path: 11_KNOWLEDGE/LLM_WIKI/wiki/karpathy_llm_wiki_summary.md
RSCF-RELATIONS:

- INDEXED_BY: [[11_KNOWLEDGE/LLM_WIKI/wiki/LLM_WIKI_INDEX|LLM_WIKI_INDEX]]
- DERIVED_FROM: [https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
  claim_class: SOURCE_CLAIM

______________________________________________________________________

**MOC:** [[11_KNOWLEDGE/LLM_WIKI/LLM_WIKI_MOC]]
