---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Skill
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

# Obsidian Markdown

Use Obsidian-specific syntax accurately. Do not spend tokens explaining ordinary
CommonMark or GFM unless the user asks.

## Workflow

1. Preserve existing frontmatter keys and formatting when editing a note.
1. Use wikilinks for vault notes and Markdown links for external URLs.
1. Use embeds, callouts, properties, tags, comments, and block references only
   when they improve the requested note.
1. Check link targets, YAML validity, and block IDs after editing.
1. Read the focused reference file when the task needs more syntax detail.

## Wikilinks and block references

```markdown
Note Name
Display Text
Note Name > Heading
Note Name > ^block-id
[[#Heading in this note]]

This paragraph is addressable. ^block-id
```

Put a block ID on its own line after a list or quote block.

## Embeds

Prefix a wikilink with <code>!</code>:

```markdown
!Note Name
!Note Name > Heading
![[11_KNOWLEDGE/stubs/image.png|300]]
![[11_KNOWLEDGE/stubs/document.pdf#page=3|document.pdf]]
```

See [Embeds](references/EMBEDS.md) for media, PDF, and query forms.

## Callouts

```markdown
> [!warning] Custom title
> Important content.

> [!faq]- Collapsed by default
> Foldable content.
```

See [Callouts](references/CALLOUTS.md) for types, aliases, folding, and nesting.

## Properties, tags, and comments

```yaml
---
title: My Note
date: 2026-07-21
tags:
  - project
aliases:
  - Alternate Name
related: "Other Note"
---
```

Quote wikilinks used as YAML values. See
[Properties](references/PROPERTIES.md) for supported property types and tag rules.

Use <code>#nested/tag</code> for inline tags. Hide content from reading view with
<code>%%inline comments%%</code> or a matching pair of <code>%%</code> markers on
separate lines.

## Attribution

Adapted from <code>kepano/obsidian-skills</code> at revision
<code>a1dc48e68138490d522c04cbf5822214c6eb1202</code>. See <code>LICENSE</code>.

______________________________________________________________________

**MOC:** [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] · [[00_ROOT/00_HOME|00_HOME]]
