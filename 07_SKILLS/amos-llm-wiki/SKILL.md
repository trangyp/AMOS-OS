---
schema_version: 1.0
title: SKILL
name: amos-llm-wiki
description: AMOS LLM Wiki — ingest, query, lint, and maintain a compounding LLM-maintained
  markdown wiki inside the AMOS Obsidian vault. Use when adding a new source to the
  wiki, answering questions from the wiki, running a wiki health check, or filing
  a synthesized answer back into 11_KNOWLEDGE/LLM_WIKI/. Do not use for generic note
  taking, non-AMOS vaults, or tasks outside the LLM_WIKI subsystem.
license: MIT
parent_skill: amos-knowledge-research-master
domain: knowledge
origin_architect: Trang Phan
epistemic_class: AMOS_MODEL
version: 1.1.0
rscf_state: DERIVED
hml_level: M
gmef_gates:
- L0_integrity
- L1_epistemic
- L5_scope
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance:
- L0
- L1
- L5
tags:
- type/skill
- type/skill
- domain/knowledge-research
- epistemic/source_claim
- hml/m
- epistemic/source_claim
- amos-os
- amos-llm-wiki-workflow
- amos-llm-wiki-agent
steward: Trang Phan
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
type: skill
source: 07_SKILLS/amos-llm-wiki
---

# AMOS LLM Wiki

## Identity

Origin architect: **Trang Phan**.
Skill for maintaining an LLM-managed, compounding knowledge wiki inside the AMOS Obsidian vault, adapted from Karpathy's LLM Wiki pattern.

**Epistemic class**: AMOS_MODEL (operational wiki-maintenance workflow).

## When to Use

- Ingest a new source into `11_KNOWLEDGE/LLM_WIKI/raw/` and update the wiki
- Answer a question by reading `LLM_WIKI_INDEX` and relevant wiki pages
- Lint the wiki for orphans, broken wikilinks, stale claims, and missing concept pages
- File a synthesized answer back into the wiki as a new page
- Update `LLM_WIKI_INDEX` and `LLM_WIKI_LOG` after any wiki operation

## Do not use

- For generic note-taking outside the AMOS vault
- For RAG-style one-off retrieval that does not update the wiki
- For modifying raw-source files (those are immutable)
- For tasks outside `11_KNOWLEDGE/LLM_WIKI/` scope

## Examples

- **User says:** "Ingest this PDF into the LLM Wiki"
  → Place it in `11_KNOWLEDGE/LLM_WIKI/raw/`, write a source-summary, update concept/entity pages, update `LLM_WIKI_INDEX`, and append `LLM_WIKI_LOG`.

- **User says:** "What does the wiki say about X?"
  → Read `LLM_WIKI_INDEX`, collect relevant pages, synthesize an answer with citations, optionally file the result into the wiki.

- **User says:** "Lint the LLM Wiki"
  → Scan for orphans, broken wikilinks, stale claims, and missing concept pages; append findings to `LLM_WIKI_LOG`.

## Capabilities

- `wiki.ingest`: Read a raw source and integrate it into the wiki
- `wiki.query`: Answer questions from the wiki and optionally file the answer
- `wiki.lint`: Health-check the wiki and flag issues
- `wiki.index`: Maintain `LLM_WIKI_INDEX` content catalog
- `wiki.log`: Append structured entries to `LLM_WIKI_LOG`
- `wiki.clip`: Convert a web source into a raw-source markdown file ready for ingest

## Operations

1. `wiki.ingest`: Read a raw source and integrate it into the wiki
2. `wiki.query`: Answer questions from the wiki and optionally file the answer
3. `wiki.lint`: Health-check the wiki and flag issues
4. `wiki.index`: Maintain `LLM_WIKI_INDEX` content catalog
5. `wiki.log`: Append structured entries to `LLM_WIKI_LOG`
6. `wiki.clip`: Convert a web source into a raw-source markdown file ready for ingest

## Validation Gates

- **L0 Integrity**: Raw sources remain unmodified; only wiki files are edited
- **L1 Epistemic**: Every wiki page is labeled `SOURCE_CLAIM` or `DERIVED`/`AMOS_MODEL` with provenance
- **L5 Scope**: Operations stay within `11_KNOWLEDGE/LLM_WIKI/`
- **L7 Authority**: Batch or irreversible wiki changes require steward review

## Failure Modes

- **Source not found**: Flag as GAP and ask the user to place it in `raw/`
- **Scope violation**: Reject the query and route back to the parent skill
- **Contradiction**: Flag as CRITICAL_GAP and halt until resolved
- **Missing concept page**: Flag as GAP or create a stub only when explicitly authorized

## AMOS Canon Grounding

This skill is governed by the AMOS constitutional law hierarchy. See `01_CANON/01_CORE_LAWS/AMOS_CORE_LAWS.md`.

### Law Compliance

| Law | Family | This Skill's Obligation |
|-----|--------|------------------------|
| **L0.01** Integrity Dominance | Integrity | RAW > WIKI; raw sources are immutable |
| **L0.02** No Fabricated Closure | Integrity | Missing evidence stays missing; no placeholder concept pages |
| **L1.01** Evidence Typing | Epistemic | Distinguish `SOURCE_CLAIM` from `DERIVED` / `AMOS_MODEL` |
| **L1.03** Model ≠ Reality | Epistemic | Wiki syntheses are AMOS_MODEL, not empirical truth |
| **L1.05** Competing Hypotheses | Epistemic | Incompatible source claims stay `COMPETING` |
| **L2** Provenance | Provenance | Every derived claim traces to a raw source |
| **L5** Scope/Regime | Scope | Valid only within the LLM_WIKI subsystem |

## References

- `00_ROOT/AMOS_LLM_WIKI.md` — schema
- `11_KNOWLEDGE/LLM_WIKI/LLM_WIKI_MOC.md` — MOC
- `11_KNOWLEDGE/LLM_WIKI/wiki/LLM_WIKI_INDEX.md` — index
- `11_KNOWLEDGE/LLM_WIKI/wiki/LLM_WIKI_LOG.md` — log
- [[08_WORKFLOWS/amos-llm-wiki-workflow|amos-llm-wiki-workflow]] — bound workflow
- [[11_KNOWLEDGE/stubs/amos-llm-wiki-agent|amos-llm-wiki-agent]] — bound agent

---

**MOC:** references_MOC · [[00_ROOT/00_HOME|00_HOME]]
