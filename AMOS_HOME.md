---
title: AMOS HOME
type: note
source: .
aliases:
- AMOS Home
tags:
- note
- vault
- epistemic/amos_model
- amos-obsidian-linking-plugins
- amos-templates
- amos-layer-maps
- readme
- architecture
- agents
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# AMOS Home

## Vault MOCs and tools

- [[00_ROOT/00_ROOT_MOC|AMOS MOC — AMOS OS master map]]
- [[11_KNOWLEDGE/KNOWLEDGE_MOC|11_KNOWLEDGE MOC — knowledge layer index]]
- [[11_KNOWLEDGE/COSMO_BRAIN_MOC|00 Cosmo Brain MOC — Cosmo Brain index]]
- [[11_KNOWLEDGE/AMOS_OBSIDIAN_LINKING_PLUGINS|AMOS_OBSIDIAN_LINKING_PLUGINS]] — Obsidian linking plugin stack
- [[00_ROOT/AMOS_TEMPLATES|AMOS_TEMPLATES]] — AMOS template index

---

- [[00_ROOT/AMOS_LAYER_MAPS|AMOS_LAYER_MAPS]] — top-level layer map index
## Related

- [[00_ROOT/00_HOME|Home]]
- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] — AMOS OS master map
- [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

---

## README and architecture stubs

- README — root README
- [[00_ROOT/ARCHITECTURE|ARCHITECTURE]] — root architecture overview
- README — observability layer README
- README — tests layer README

---

RSCF-NODE
node_id: 00_home_root
node_type: note
path: AMOS Home.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
  - INDEXED_BY: [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
  - INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---

## Vault dashboard

```dataview
LIST FROM #moc OR #index OR #templates
SORT file.name ASC
```

### Layer map index

```dataview
LIST
WHERE file.path = "00_ROOT/AMOS_Layer_Maps.md"
```

### Backlink leaderboard

```dataview
TABLE length(file.inlinks) as Backlinks
FROM #moc OR #index OR #map OR #templates
SORT length(file.inlinks) DESC
LIMIT 15
```

### Recent changes

```dataview
LIST
FROM ""
SORT file.mtime DESC
LIMIT 10
```

### Orphan watch

```dataview
LIST
FROM ""
WHERE length(file.inlinks) = 0 AND length(file.outlinks) = 0
LIMIT 20
```
- [[AGENTS|AGENTS]]

---
**MOC:** [[_MOC|_MOC]]

