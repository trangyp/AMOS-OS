---
tags: ['cognitive_matrix', 'primitives', 'l13_prediction', 'contract']
---

# L13_PREDICTION — Prediction Contract

STATUS: PROPOSED_SPECIFICATION
epistemic_class: AMOS_MODEL
canonical_status: CONDITIONAL
updated: 2026-08-26

## 0. Purpose
Forecasts carry confidence ceilings, sample-size honesty, regime declarations..

## 1. Canonical home
Related canon: TPE prediction engine.

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

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[COGNITIVE_MATRIX_MOC]] · [[00_ROOT/00-Home]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: cognitive_matrix_l13_prediction_contract
node_type: note
path: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L13_PREDICTION/COGNITIVE_MATRIX_L13_PREDICTION_CONTRACT.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_ROOT/00-Home]]
  - CHILD_OF: [[COGNITIVE_MATRIX_PRIMITIVES_CONTRACT]]
claim_class: AMOS_MODEL
