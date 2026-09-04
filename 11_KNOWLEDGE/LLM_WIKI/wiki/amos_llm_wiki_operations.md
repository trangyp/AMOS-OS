---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Amos Llm Wiki Operations
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

# AMOS LLM Wiki Operations

The `LLM_WIKI` subsystem is maintained through four canonical operations. Each operation is RSCF-governed, git-reversible, and scope-bound to `11_KNOWLEDGE/LLM_WIKI/`.

## 1. Ingest

1. Receive or place a raw source in `11_KNOWLEDGE/LLM_WIKI/raw/`.
1. Read the source without modifying it.
1. Write a source-summary under `wiki/`.
1. Create or update concept/entity pages.
1. Update \`\`.
1. Append a timestamped entry to \`\`.

**Skill capability**: `llmwiki.ingest`
**Bound workflow**: `amos-llm-wiki-workflow.md`
**Bound agent**: `amos-llm-wiki-agent.json`

## 2. Query

1. Read \`\` to locate relevant pages.
1. Collect concept/entity/source pages.
1. Synthesize a cited answer with epistemic class labels.
1. Optionally file the answer as a new wiki page and update the index/log.

**Skill capability**: `llmwiki.query`

## 3. Lint

1. Scan `wiki/` for orphan pages, broken wikilinks, stale claims, and missing concept pages.
1. Record findings in \`\`.
1. Do not auto-delete; either link or explicitly deprecate.

**Skill capability**: `llmwiki.lint`

## 4. Clip

1. Convert a web article or document to markdown (Obsidian Web Clipper, copy-paste, or `qmd`).
1. Place the markdown in `raw/`.
1. Trigger `llmwiki.ingest`.

**Skill capability**: `llmwiki.clip`
**Supporting tool**: \`\`

## Canonical AMOS bindings

| Layer     | Artifact                 | Path                                         |
| --------- | ------------------------ | -------------------------------------------- |
| Skill     | `amos-llm-wiki`          | `.devin/skills/amos-llm-wiki/SKILL.md`       |
| Workflow  | `amos-llm-wiki-workflow` | `.devin/workflows/amos-llm-wiki-workflow.md` |
| Agent     | `amos-llm-wiki-agent`    | `.devin/agents/amos-llm-wiki-agent.json`     |
| Tool note | `AMOS_LLM_WIKI_TOOL`     | `14_TOOLS/AMOS_LLM_WIKI_TOOL.md`             |

______________________________________________________________________

RSCF-NODE
node_id: amos_llm_wiki_operations
node_type: synthesis
path: 11_KNOWLEDGE/LLM_WIKI/wiki/amos_llm_wiki_operations.md
RSCF-RELATIONS:

- INDEXED_BY: [[11_KNOWLEDGE/LLM_WIKI/wiki/LLM_WIKI_INDEX|LLM_WIKI_INDEX]]
- DERIVED_FROM: [[00_ROOT/AMOS_LLM_WIKI]]
  claim_class: AMOS_MODEL

______________________________________________________________________

**MOC:** [[11_KNOWLEDGE/LLM_WIKI/LLM_WIKI_MOC]]
