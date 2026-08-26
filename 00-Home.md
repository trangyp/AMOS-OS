---
aliases:
- AMOS Home
---

# AMOS Home

## Vault MOCs and tools

- [[00_ROOT/00_ROOT_MOC.md|AMOS MOC]] — AMOS OS master map
- [[11_KNOWLEDGE/11_KNOWLEDGE_MOC.md|11_KNOWLEDGE MOC]] — knowledge layer index
- [[11_KNOWLEDGE/Cosmo_Brain_MOC.md|00 Cosmo Brain MOC]] — Cosmo Brain index
- [[AMOS_Obsidian_Linking_Plugins]] — Obsidian linking plugin stack
- [[AMOS_Templates]] — AMOS template index

---

- [[AMOS_Layer_Maps]] — top-level layer map index
## Related

- [[00_ROOT/00-Home.md|Home]]
- [[00_ROOT_MOC]] — AMOS OS master map
- [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: 00_home_root
node_type: note
path: 00-Home.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_ROOT/00-Home.md]]
  - INDEXED_BY: [[00_ROOT_MOC]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
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
