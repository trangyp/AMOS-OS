---
title: AMOS LLM Wiki Tool
type: note
source: 14_TOOLS
tags:
- tool
- llm-wiki
- obsidian
- amos-os
- amos-llm-wiki
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: AMOS_knowledge
---

# AMOS LLM Wiki — Tools

The LLM Wiki subsystem is supported by a small set of tools that make ingest, query, and lint easier.

## Obsidian Web Clipper

Browser extension that converts web articles to markdown. Save clips to `11_KNOWLEDGE/LLM_WIKI/raw/`.

## Local attachment download

In Obsidian → Settings → Files and links, set "Attachment folder path" to `11_KNOWLEDGE/LLM_WIKI/raw/assets/`. After clipping, use the "Download attachments for current file" command.

## qmd (optional)

When the wiki grows past a few hundred pages, install `qmd` for hybrid BM25/vector search over markdown. Use only the official repository the user provides; do not guess a URL.

## grep / tail

At small scale the `LLM_WIKI_LOG` is grep-parseable:

```sh
grep "^## \[" 11_KNOWLEDGE/LLM_WIKI/wiki/LLM_WIKI_LOG.md | tail -5
```

## Dataview

If YAML frontmatter is added to wiki pages, Dataview can render dynamic tables of sources, concepts, and entities.

## Related

- [[AMOS_LLM_WIKI]]
- [[LLM_WIKI_MOC]]
- [[_MOC]]

---
**MOC:** [[14_TOOLS_MOC]]
