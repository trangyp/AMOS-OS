---
title: L18 GMEF
type: note
tags: [canon, core_laws, note]
---



# L18 GMEF Gate Laws

STATUS: PROPOSED_SPECIFICATION
epistemic_class: AMOS_MODEL
canonical_status: CONDITIONAL
updated: 2026-08-26

## 0. Status
Proposed specification replacing placeholder. AMOS_MODEL. Canonical status: CONDITIONAL.

## 2. Laws
- **GMEF-1 Gate Composition**: governance gates evaluate before state transitions; passing one gate grants no others.
- **GMEF-2 Fail Closed**: gate cannot decide = DENY, never ALLOW-by-default.
- **GMEF-3 Receipt Required**: every gate decision emits a receipt (decision, inputs, epoch, digest).
- **GMEF-4 Authority Separation**: audit pass does not grant authority; promotion requires the promotion process.

## 4. Falsifiers
F1: authoritative GMEF canon defines different gate semantics.

---

00_ROOT_MOC|AMOS MOC

---
**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]]

---
RSCF-NODE
node_id: l18_gmef
node_type: note
path: 01_CANON/01_CORE_LAWS/L18_GMEF.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
  - CHILD_OF: [[LAW_HIERARCHY]]
claim_class: AMOS_MODEL

---
**MOC:** [[01_CORE_LAWS_MOC]]
