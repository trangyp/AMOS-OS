---
title: AMOS LLM Wiki — Skill Map of Content
type: moc
skill_id: amos-llm-wiki
source: 07_SKILLS/amos-llm-wiki
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_MOC
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  provenance: authoritative_AMOS_OS_structure
  scope: active__AMOS_OS
---
# AMOS LLM Wiki — Skill Map of Content

**Path:** `07_SKILLS/amos-llm-wiki`
**Domain:** knowledge
**Parent skill:** [[07_SKILLS/amos-knowledge-research-master/amos-knowledge-research-master_MOC|amos-knowledge-research-master]]
**Epistemic class:** AMOS_MODEL · **H/M/L:** M · **Version:** 1.1.0

## Purpose

AMOS LLM Wiki — ingest, query, lint, and maintain a compounding LLM-maintained markdown wiki inside the AMOS Obsidian vault. Use when adding a new source to the wiki, answering questions from the wiki, running a wiki health check, or filing a synthesized answer back into 11_KNOWLEDGE/LLM_WIKI/. Do not use for generic note taking, non-AMOS vaults, or tasks outside the LLM_WIKI subsystem.

## When To Use

- Ingest a new source into `11_KNOWLEDGE/LLM_WIKI/raw/` and update the wiki
- Answer a question by reading `LLM_WIKI_INDEX` and relevant wiki pages
- Lint the wiki for orphans, broken wikilinks, stale claims, and missing concept pages
- File a synthesized answer back into the wiki as a new page
- Update `LLM_WIKI_INDEX` and `LLM_WIKI_LOG` after any wiki operation

## Do Not Use

- For generic note-taking outside the AMOS vault
- For RAG-style one-off retrieval that does not update the wiki
- For modifying raw-source files (those are immutable)
- For tasks outside `11_KNOWLEDGE/LLM_WIKI/` scope

## Capabilities / Operations

- `wiki.ingest`: Read a raw source and integrate it into the wiki
- `wiki.query`: Answer questions from the wiki and optionally file the answer
- `wiki.lint`: Health-check the wiki and flag issues
- `wiki.index`: Maintain `LLM_WIKI_INDEX` content catalog
- `wiki.log`: Append structured entries to `LLM_WIKI_LOG`
- `wiki.clip`: Convert a web source into a raw-source markdown file ready for ingest

## Validation Gates

- **L0 Integrity**: Raw sources remain unmodified; only wiki files are edited
- **L1 Epistemic**: Every wiki page is labeled `SOURCE_CLAIM` or `DERIVED`/`AMOS_MODEL` with provenance
- **L5 Scope**: Operations stay within `11_KNOWLEDGE/LLM_WIKI/`
- **L7 Authority**: Batch or irreversible wiki changes require steward review

## Files in this skill

- [[07_SKILLS/amos-llm-wiki/SKILL.md|SKILL]]
- `07_SKILLS/amos-llm-wiki/scripts/hooks/hooks_config.yaml`
- `07_SKILLS/amos-llm-wiki/scripts/hooks/post_tool_use.py`
- `07_SKILLS/amos-llm-wiki/scripts/hooks/pre_tool_use.py`
- `07_SKILLS/amos-llm-wiki/scripts/hooks/stop.py`

## Examples

- **User says:** "Ingest this PDF into the LLM Wiki"
  → Place it in `11_KNOWLEDGE/LLM_WIKI/raw/`, write a source-summary, update concept/entity pages, update `LLM_WIKI_INDEX`, and append `LLM_WIKI_LOG`.

- **User says:** "What does the wiki say about X?"
  → Read `LLM_WIKI_INDEX`, collect relevant pages, synthesize an answer with citations, optionally file the result into the wiki.

- **User says:** "Lint the LLM Wiki"
  → Scan for orphans, broken wikilinks, stale claims, and missing concept pages; append findings to `LLM_WIKI_LOG`.


## Related

- **Parent MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
