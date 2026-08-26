---
tags: ['canon', 'universe_canon', 'note']
---

# P6 — Execution & Agency Plane

STATUS: PROPOSED_SPECIFICATION
epistemic_class: AMOS_MODEL
canonical_status: CONDITIONAL
updated: 2026-08-26

## 1. Scope
Turning authorized intent into effects: workers, transactions, receipts, idempotency, budgets.

## 2. Canonical questions
- What stands between "allowed" and "done"?
- How are effects made accountable and reversible?

## 3. Laws
- **P6-1 Worker Gate**: consequential effects only via governed worker paths (I-RPOL-017).
- **P6-2 Receipt Everything**: commits emit digests to append-only ledger (INV-031/035).
- **P6-3 Budgeted Action**: cumulative cost accounting per principal (INV-041).

## 4. Boundaries
Execution authority remains NONE until promotion process runs.

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[AMOS_7_PART_UNIVERSE_CANON]] · [[HML_CANON]] · [[00-Home]]

---
RSCF-NODE
node_id: p6_execution_agency
node_type: note
path: 01_CANON/02_UNIVERSE_CANON/P6_EXECUTION_AGENCY.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - CHILD_OF: [[AMOS_7_PART_UNIVERSE_CANON]]
claim_class: AMOS_MODEL
