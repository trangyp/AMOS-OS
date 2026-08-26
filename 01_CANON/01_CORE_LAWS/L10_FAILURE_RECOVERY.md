---
tags: ['canon', 'core_laws', 'note']
---

# L10 Failure & Recovery Laws

STATUS: PROPOSED_SPECIFICATION
epistemic_class: AMOS_MODEL
canonical_status: CONDITIONAL
updated: 2026-08-26

## 0. Status
Proposed specification replacing placeholder. AMOS_MODEL. Canonical status: CONDITIONAL.

## 2. Laws
- **FR-1 Collapse Precedes Visible Failure**: detect degradation before user-visible breakage (critical slowing down signals).
- **FR-2 Repair Capacity Bounds**: recovery is bounded by independent repair capacity per failure mode; correlated damage amplifies (DMER L5).
- **FR-3 Fail Closed on Critical Unknown**: missing authority/provenance/validation blocks execution rather than defaulting open.
- **FR-4 Recovery Basins**: every consequential subsystem declares a rollback target (git, snapshots, receipts) before mutation.

## 4. Falsifiers
F1: authoritative failure canon defines different recovery semantics.

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]]

---
RSCF-NODE
node_id: l10_failure_recovery
node_type: note
path: 01_CANON/01_CORE_LAWS/L10_FAILURE_RECOVERY.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
  - CHILD_OF: [[LAW_HIERARCHY]]
claim_class: AMOS_MODEL
