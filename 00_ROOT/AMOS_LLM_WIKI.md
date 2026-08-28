---
artifact_id: AMOS-LLM-WIKI
conclusion_class: DECISION / AMOS_MODEL
confidence: DERIVED
name: AMOS LLM Wiki
origin_architect: Trang Phan
provenance: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
status: active
steward: Trang Phan
tags:
- wiki
- llm-wiki
- knowledge
- obsidian
- amos_os
- canon-group/tech-ai
- canon/tooling
title: AMOS LLM Wiki
type: schema
source: 00_ROOT
rscf:
  state: SOURCE_CLAIM
  claim_class: AMOS_MODEL
  provenance: karpathy_gist
  scope: AMOS_knowledge
---


# AMOS LLM Wiki

Schema for an LLM-maintained, compounding knowledge wiki inside the AMOS Obsidian vault, adapted from Andrej Karpathy's [LLM Wiki gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

## Core idea

The AMOS vault is already a structured knowledge base. This schema adds a dedicated *compounding wiki* subsystem where the LLM reads a source once, extracts the key information, and integrates it into an evolving, cross-linked set of markdown pages. Queries are answered from the wiki, not by re-parsing raw sources. Good answers are filed back into the wiki so explorations also compound.

## Layers

| Layer | Path | Owner | Rule |
|-------|------|-------|------|
| Raw sources | `11_KNOWLEDGE/LLM_WIKI/raw/` | Human / clipping tools | Immutable. Source of truth. Do not edit after first write. |
| The wiki | `11_KNOWLEDGE/LLM_WIKI/wiki/` | LLM | Generated and maintained by the LLM on every ingest, query, and lint. |
| The schema | `00_ROOT/AMOS_LLM_WIKI.md` | Human + LLM | Conventions, workflows, and file formats. |

## Conventions

- Use the standard AMOS YAML frontmatter: `title`, `type`, `source`, `tags`, `rscf`.
- Use Obsidian wikilinks (`[[...]]`) for cross-references.
- One concept per page. Keep pages focused enough to link.
- Raw-source pages use `rscf.state: SOURCE_CLAIM` and `rscf.claim_class: SOURCE_CLAIM`.
- Synthesized/derived pages use `rscf.state: DERIVED` and `rscf.claim_class: AMOS_MODEL`.
- Store attachments under `raw/assets/`.
- Use the `LLM_WIKI_` filename prefix for wiki-wide files to avoid name collisions.

## Operations

### Ingest
1. Place or clip the source into `11_KNOWLEDGE/LLM_WIKI/raw/`.
2. Create or update a source-summary page in `11_KNOWLEDGE/LLM_WIKI/wiki/`.
3. Update relevant entity, concept, and synthesis pages.
4. Update `[[LLM_WIKI_INDEX]]`.
5. Append an entry to `[[LLM_WIKI_LOG]]`.

### Query
1. Read `[[LLM_WIKI_INDEX]]` to find relevant pages.
2. Read those pages and synthesize an answer with citations.
3. If the answer has lasting value, file it back as a new wiki page and update the index/log.

### Lint
1. Scan for orphan pages, broken wikilinks, and missing concept pages.
2. Flag contradictions between pages and stale claims that newer sources have superseded.
3. Suggest new questions or sources to close gaps.
4. Append findings to `[[LLM_WIKI_LOG]]`.

## Special files

- `11_KNOWLEDGE/LLM_WIKI/wiki/LLM_WIKI_INDEX.md` — content-oriented catalog of all wiki pages.
- `11_KNOWLEDGE/LLM_WIKI/wiki/LLM_WIKI_LOG.md` — chronological, append-only activity log.

## Optional tooling

- Obsidian Web Clipper for clipping web sources to markdown.
- `qmd` (local hybrid search) when the wiki grows beyond a few hundred pages.
- Dataview for dynamic tables over YAML frontmatter.

## AMOS canonical bindings

The LLM Wiki is operationalized through AMOS canonical skill/workflow/agent bindings:

- Skill: `.devin/skills/amos-llm-wiki/SKILL.md` — runtime capability
- Workflow: `.devin/workflows/amos-llm-wiki-workflow.md` — operational sequence
- Agent: `.devin/agents/amos-llm-wiki-agent.json` — execution contract
- Tools: `14_TOOLS/AMOS_LLM_WIKI_TOOL.md` — supporting tooling

## Related

- [[_MOC]]
- [[00_ROOT_MOC]]
- [[KNOWLEDGE_MOC]]
- [[LLM_WIKI_MOC]]
- [[LLM_WIKI_INDEX]]
- [[LLM_WIKI_LOG]]

---
RSCF-NODE
node_id: amos_llm_wiki
node_type: schema
path: 00_ROOT/AMOS_LLM_WIKI.md
RSCF-RELATIONS:
  - INDEXED_BY: [[_MOC]]
  - INDEXED_BY: [[00_ROOT_MOC]]
  - INDEXED_BY: [[KNOWLEDGE_MOC]]
  - INDEXED_BY: [[LLM_WIKI_MOC]]
claim_class: AMOS_MODEL

---
**MOC:** [[LLM_WIKI_MOC]]
