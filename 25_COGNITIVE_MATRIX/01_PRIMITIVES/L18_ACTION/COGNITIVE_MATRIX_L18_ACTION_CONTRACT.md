---
title: COGNITIVE MATRIX L18 ACTION CONTRACT
type: cognitive
tags: [cognitive_matrix, primitives, l18_action, contract]
---



# L18_ACTION — Action Contract

STATUS: PROPOSED_SPECIFICATION
epistemic_class: AMOS_MODEL
canonical_status: CONDITIONAL
updated: 2026-08-26

## 0. Purpose
Authorized effect execution via worker paths only; receipts emitted..

## 1. Canonical home
Related canon: P6 plane; INV-005/030.

## 2. Contract surface
- **Inputs**: upstream layer outputs (typed, provenance-stamped)
- **Outputs**: typed artifacts carrying SOURCE/DERIVED/MODEL/UNKNOWN class + confidence ceiling
- **Invariants**: scope containment, regime isolation, freshness, fail-closed on unknown
- **Failure modes**: stale input, class mixing, silent scope expansion — each fails closed

## 3. H/M/L applicability
- **H**: contract integrity, epistemic class discipline
- **M**: domain-specific tuning
- **L**: mechanical checks (types, epochs, digests)

## 4. Gaps
Runtime binding to executable engines is PARTIAL; see subsystem validation receipts.

---

00_ROOT_MOC|AMOS MOC

---
**Related:** [[COGNITIVE_MATRIX_MOC]] · [[00_HOME]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: cognitive_matrix_l18_action_contract
node_type: note
path: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L18_ACTION/COGNITIVE_MATRIX_L18_ACTION_CONTRACT.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - CHILD_OF: [[COGNITIVE_MATRIX_PRIMITIVES_CONTRACT]]
claim_class: AMOS_MODEL

---
**MOC:** [[L18_ACTION_MOC]]
