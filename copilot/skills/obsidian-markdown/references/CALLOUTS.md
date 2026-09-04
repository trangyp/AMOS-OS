---
title: Callouts
type: note
source: .
tags:
  - note
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# Callouts reference

## Folding and nesting

```markdown
> [!faq]- Collapsed by default
> Hidden until expanded.

> [!faq]+ Expanded by default
> Visible but collapsible.

> [!question] Outer
> > [!note] Inner
> > Nested content.
```

## Built-in types

| Type     | Aliases            |
| -------- | ------------------ |
| note     | —                  |
| abstract | summary, tldr      |
| info     | —                  |
| todo     | —                  |
| tip      | hint, important    |
| success  | check, done        |
| question | help, faq          |
| warning  | caution, attention |
| failure  | fail, missing      |
| danger   | error              |
| bug      | —                  |
| example  | —                  |
| quote    | cite               |

______________________________________________________________________

**MOC:** [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] · [[00_ROOT/00_HOME|00_HOME]]
