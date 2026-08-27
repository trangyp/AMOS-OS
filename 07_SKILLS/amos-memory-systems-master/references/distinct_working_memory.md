---
title: distinct working memory
type: reference
tags: [reference, amos-memory-systems-master]
---

# Distinct Working Memory

> Source: `_00_Cosmo brain/memory/WORKING_MEMORY.md`
> Epistemic class: SOURCE_CANON

## Three Carrier Types

Separate:
- **recall-carried state**: information retrieved from long-term memory
- **summary-carried state**: compressed representations of prior context
- **locality-carried state**: environment/position-dependent context

Do not count duplicate information across carriers as independent support.

## Working Memory Slot Schema

Each working-memory slot should record:

```
[content, carrier, provenance, novelty, dependency_role, expiry, contradiction_state]
```

- **content**: the actual information
- **carrier**: recall, summary, or locality
- **provenance**: source ancestry
- **novelty**: is this new or repeated?
- **dependency_role**: what does this support?
- **expiry**: when does this become stale?
- **contradiction_state**: unresolved conflicts?

---
**MOC:** [[references_MOC]]
