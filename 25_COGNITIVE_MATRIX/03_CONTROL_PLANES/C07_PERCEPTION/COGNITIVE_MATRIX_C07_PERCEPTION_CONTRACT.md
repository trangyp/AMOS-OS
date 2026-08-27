---
tags: ['cognitive_matrix', 'control_planes', 'c07_perception', 'contract']
---

# C07_PERCEPTION — Perception control: reality gate, evidence admission typing, observer-effect logging.

STATUS: PROPOSED_SPECIFICATION
epistemic_class: AMOS_MODEL
canonical_status: CONDITIONAL
updated: 2026-08-26

## 0. Purpose
Perception control: reality gate, evidence admission typing, observer-effect logging..

## 1. Contract surface
- **Owns**: gate decisions for its plane; receipts emitted per decision
- **Preconditions**: upstream plane states fresh at epoch; authority present for consequential acts
- **Fail-closed**: undecided = DENY; audit pass never grants authority
- **Interfaces**: declared only — no ambient cross-plane access (P5-1..4)

## 2. Gaps
Executable binding PARTIAL.

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[COGNITIVE_MATRIX_MOC]] · [[00_ROOT/00-Home]]

---
RSCF-NODE
node_id: cognitive_matrix_c07_perception_contract
node_type: note
path: 25_COGNITIVE_MATRIX/03_CONTROL_PLANES/C07_PERCEPTION/COGNITIVE_MATRIX_C07_PERCEPTION_CONTRACT.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_ROOT/00-Home]]
  - CHILD_OF: [[COGNITIVE_MATRIX_CONTROL_PLANES_CONTRACT]]
claim_class: AMOS_MODEL
