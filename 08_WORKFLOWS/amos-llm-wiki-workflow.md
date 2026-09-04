---
Type: Workflow
Skill: amos-llm-wiki
Agent: amos-llm-wiki-agent
Trigger: When the user asks to ingest, query, lint, or maintain the AMOS LLM Wiki in 11_KNOWLEDGE/LLM_WIKI/
Version: 1.0.0
title: AMOS LLM Wiki
tags:
  - type/workflow
  - domain/knowledge
  - amos-os
type: workflow
source: 08_WORKFLOWS
rscf:
  state: AMOS_MODEL
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: workflow_process
---

# Workflow: AMOS LLM Wiki

## Preconditions

- The `amos-llm-wiki` skill exists and is loaded.
- The `amos-llm-wiki-agent` is available and has a valid content_hash.
- The target paths are within `11_KNOWLEDGE/LLM_WIKI/`.
- `00_ROOT/AMOS_LLM_WIKI.md` schema is available.

## Steps

1. **Intake**: Identify the requested wiki operation (ingest, query, lint, clip) and confirm scope.
   - Classify the operation
   - Verify the target is within `11_KNOWLEDGE/LLM_WIKI/`
1. **Load Schema**: Read `00_ROOT/AMOS_LLM_WIKI.md` and the relevant `LLM_WIKI_INDEX` / `LLM_WIKI_LOG`.
1. **Execute Operation**:
   - **Ingest**: read the raw source, write a source-summary, update concept/entity pages, update `LLM_WIKI_INDEX`, append `LLM_WIKI_LOG`
   - **Query**: read `LLM_WIKI_INDEX`, collect relevant pages, synthesize an answer with citations, optionally file the result as a new wiki page
   - **Lint**: scan for orphans, broken wikilinks, stale claims, and missing concept pages; append findings to `LLM_WIKI_LOG`
   - **Clip**: convert a web source or document into a raw-source markdown file in `11_KNOWLEDGE/LLM_WIKI/raw/`
1. **Validation**: Check that raw sources were not modified, wiki pages have proper frontmatter, and all cross-references resolve.
1. **Finalization**: Update `LLM_WIKI_INDEX` and `LLM_WIKI_LOG`, produce an operation report.

## Operations

1. **Intake**: Identify the requested wiki operation (ingest, query, lint, clip) and confirm scope. - Classify the operation - Verify the target is within `11_KNOWLEDGE/LLM_WIKI/`
1. **Load Schema**: Read `00_ROOT/AMOS_LLM_WIKI.md` and the relevant `LLM_WIKI_INDEX` / `LLM_WIKI_LOG`.
1. **Execute Operation**: - **Ingest**: read the raw source, write a source-summary, update concept/entity pages, update `LLM_WIKI_INDEX`, append `LLM_WIKI_LOG` - **Query**: read `LLM_WIKI_INDEX`, collect relevant pages, synthesize an answe...
1. **Validation**: Check that raw sources were not modified, wiki pages have proper frontmatter, and all cross-references resolve.
1. **Finalization**: Update `LLM_WIKI_INDEX` and `LLM_WIKI_LOG`, produce an operation report.

## Validation Gates

### Gate 1: Intake Validation

- Operation is one of `ingest`, `query`, `lint`, `clip`
- Target path is within `11_KNOWLEDGE/LLM_WIKI/`

### Gate 2: Skill Load Validation

- `amos-llm-wiki` skill loaded successfully
- `amos-llm-wiki-agent` capabilities match the operation

### Gate 3: Output Validation

- Raw source files remain unchanged
- New/updated wiki pages have valid AMOS frontmatter
- All wikilinks resolve to existing targets
- `LLM_WIKI_INDEX` and `LLM_WIKI_LOG` are updated

## Error Recovery

- **Parse error in raw source**: log the error and skip the source
- **Missing concept page**: flag as GAP and ask for authorization to create a stub
- **Broken wikilink**: flag and, if authorized, create a redirect or stub
- **Max retries**: 2 per file before skipping

## Failure Paths

- If a validation gate fails: revert unintended changes and report the failure
- If a raw source is modified: abort and restore from git
- If a scope violation occurs: stop immediately and escalate to the user
- If an irreversible change is requested: require steward review

## AMOS Canon Workflow Governance

### GMEF Gate Sequence (L18)

- `L0_integrity`: Raw sources are never edited; only wiki files change
- `L1_epistemic`: All changes tagged with epistemic class
- `L5_scope`: Only `11_KNOWLEDGE/LLM_WIKI/` is processed

### H/M/L Rigor Assignment (L16)

- H-level: Batch ingest of many sources or restructuring the wiki schema
- M-level: Single-source ingest or query with filing
- L-level: Reading the index or log

### RSCF Propagation (L17)

- Raw-source summaries are `SOURCE_CLAIM`
- Synthesized concept/entity pages are `DERIVED` / `AMOS_MODEL`
- Provenance: raw source path + schema reference

______________________________________________________________________

**MOC:** [[08_WORKFLOWS/law-stack-enforcement-pipeline/law-stack-enforcement-pipeline_MOC|law-stack-enforcement-pipeline_MOC]] · [[00_ROOT/00_HOME|00_HOME]]
