---
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
title: references MOC
type: moc
source: 07_SKILLS
tags:
  - references
  - skills
  - type/skill
  - law-hierarchy
  - trang-framework-recursive-ontology-dynamics
moc: true
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

```text
TABLE file.mtime AS Updated, file.tags AS Tags
FROM "07_SKILLS"
WHERE contains(file.path, "references/")
SORT file.name ASC
```

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]] · [[07_SKILLS/SKILLS_README|SKILLS_README]]

**MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: references_moc
node_type: moc
path: 07_SKILLS/references_MOC.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
