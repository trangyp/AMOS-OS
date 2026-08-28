---
title: references MOC
type: moc
source: 07_SKILLS
tags:
- moc
- references
- skills
- canon/skill
rscf:
  state: SOURCE_CLAIM
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: skills
  node_id: references_moc
  node_type: moc
---

# references MOC

Map-of-content for skill reference notes.

```dataview
TABLE file.mtime AS Updated, file.tags AS Tags
FROM "07_SKILLS"
WHERE contains(file.path, "references/")
SORT file.name ASC
```

---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[SKILLS_README]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: references_moc
node_type: moc
path: 07_SKILLS/references_MOC.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
  - CHILD_OF: [[07_SKILLS_MOC]]
