---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Llm Wiki Pattern
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

# LLM Wiki Pattern

A compounding-knowledge architecture in which an LLM incrementally builds and maintains a structured, interlinked markdown wiki instead of re-deriving answers from raw documents on every query. The cross-references, contradiction flags, and synthesis are already embedded in the artifact; each new source updates the whole, so the marginal cost of answering a question falls and the marginal value of the corpus rises.

## Core mechanism

- **Ingest** — the LLM reads a raw source, writes a source summary, updates or creates concept/entity pages, then updates the index and log.
- **Query** — the LLM reads the index, gathers relevant pages, and returns a synthesized, cited answer. Valuable answers are filed back into the wiki as new pages.
- **Lint** — the LLM scans for contradictions, orphans, stale claims, missing concept pages, and broken cross-references.

## Why it differs from RAG

RAG retrieves raw text at query time and re-reasons each time. A wiki is a persistent, revisable artifact: each new source updates the global state, and the accumulated structure becomes the reasoning substrate.

## Key design invariants

- Raw sources are immutable once placed in `raw/`.
- Wiki pages are synthesized, cited, and epistemically typed.
- The index and log are append-only / overwrite for catalog updates.
- Cross-references are first-class; orphan pages are a lint failure.

## AMOS instantiation

The AMOS vault realizes this pattern as the `LLM_WIKI` subsystem under `11_KNOWLEDGE/LLM_WIKI/`, governed by `and supported by the` guide.

______________________________________________________________________

RSCF-NODE
node_id: llm_wiki_pattern
node_type: concept
path: 11_KNOWLEDGE/LLM_WIKI/wiki/llm_wiki_pattern.md
RSCF-RELATIONS:

- INDEXED_BY: [[11_KNOWLEDGE/LLM_WIKI/wiki/LLM_WIKI_INDEX|LLM_WIKI_INDEX]]
- DERIVED_FROM: [[11_KNOWLEDGE/LLM_WIKI/wiki/karpathy_llm_wiki_summary|karpathy_llm_wiki_summary]]
  claim_class: DERIVED

______________________________________________________________________

**MOC:** [[11_KNOWLEDGE/LLM_WIKI/LLM_WIKI_MOC]]
