---
title: INDEX COGNITIVE MATRIX README
type: index
tags: [cognitive_matrix, index, readme]
---



# AMOS Cognitive Matrix

**Origin architect / steward:** Trang Phan  
**Class:** AMOS architecture / matrix runtime specification

This package turns the AMOS Cognitive Architecture Matrix into an addressable OS coordinate system.

## Address

`CELL_<Primitive>_<Operation>_<ControlPlane>_<Scale>`

Example:

`CELL_L10_O08_C04_H`

means:

World Modeling × Prediction × Reasoning Control Plane × High scale.

## Cardinality

30 primitives × 17 lifecycle operations × 9 control planes × 3 scales = **13,770 cells**.

## Critical separation

CANON != KERNEL != PRIMITIVE != AGENT != SKILL != WORKFLOW != CONTROL_PLANE

A cell does not claim implementation merely because a candidate kernel/agent/skill/workflow can be routed to it.
Each binding is `UNVALIDATED_BINDING` until validated by tests and provenance.

---

00_ROOT_MOC|AMOS MOC

---
**Related:** [[00_HOME]] · [[COGNITIVE_MATRIX_MOC]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: index_cognitive_matrix_readme
node_type: note
path: 25_COGNITIVE_MATRIX/00_INDEX/INDEX_COGNITIVE_MATRIX_README.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
