---
tags: ['control_plane', 'authority', 'note']
---

# Witness Invalidation

STATUS: PROPOSED_SPECIFICATION
epistemic_class: AMOS_MODEL
canonical_status: CONDITIONAL
updated: 2026-08-26

## 0. Contract
Witness invalidation propagates to dependent attestations.

## 1. Invariants
Fail-closed · UNKNOWN ≠ PERMISSION · receipts for consequential acts · append-only logs.

## 2. Executed reference
`authz_invariant_engine.py` — 17/17 probes across separation/binding/freshness/delegation/provenance/budget/emergency families.

## 3. Gaps
Full ledger/receipt paths (INV-035..037) and multi-origin composition (044..046) remain OPEN.

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]] · [[authz_invariant_engine]]

---
RSCF-NODE
node_id: authz_witness_invalidation
node_type: note
path: 03_CONTROL_PLANE/04_AUTHORITY/WITNESS_INVALIDATION.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
claim_class: AMOS_MODEL
