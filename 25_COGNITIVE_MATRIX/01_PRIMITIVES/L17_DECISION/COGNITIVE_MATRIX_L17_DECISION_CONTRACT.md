---
title: COGNITIVE MATRIX L17 DECISION CONTRACT
tags: ['cognitive_matrix', 'primitives', 'l17_decision', 'contract']
---


# L17_DECISION — Decision Contract

STATUS: PROPOSED_SPECIFICATION
epistemic_class: AMOS_MODEL
canonical_status: CONDITIONAL
updated: 2026-08-26

## 0. Purpose
Selection under uncertainty with explicit defer option; fail-closed on critical unknowns..

## 1. Canonical home
Related canon: GMEF gates.

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
node_id: cognitive_matrix_l17_decision_contract
node_type: note
path: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L17_DECISION/COGNITIVE_MATRIX_L17_DECISION_CONTRACT.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - CHILD_OF: [[COGNITIVE_MATRIX_PRIMITIVES_CONTRACT]]
claim_class: AMOS_MODEL

---
**MOC:** [[L17_DECISION_MOC]]
