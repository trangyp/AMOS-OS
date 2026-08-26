---
tags: ['canon', 'core_laws', 'note']
---

# L7 Authority Boundary Laws

STATUS: PROPOSED_SPECIFICATION
epistemic_class: AMOS_MODEL
canonical_status: CONDITIONAL
implementation_status: LOGIC_EXECUTABLE_IN_PART
updated: 2026-08-26

## 0. Status
Proposed specification. AMOS_MODEL.

## 1. Purpose
Separate capability from authority; keep authority typed, scoped, revocable.

## 2. Laws
- **A-1 Separation**: CAPABILITY != AUTHORITY != POLICY_ALLOW != EVENT != COMMITMENT.
- **A-2 Typed & Scoped**: authority is granted per principal per scope per epoch; never ambient.
- **A-3 Revocable**: revocation takes effect at the current epoch without grace drift.
- **A-4 Non-Self-Issued**: agents cannot self-authorize; delegation chains terminate at a human root.

## 3. Enforcement
authz_invariant_engine.py executes these families (INV-001..050): 17/17 probes pass.

## 4. Falsifiers
F1: authoritative authority canon defines materially different grant lifecycle.

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]]

---
RSCF-NODE
node_id: l7_authority
node_type: note
path: 01_CANON/01_CORE_LAWS/L7_AUTHORITY.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
  - CHILD_OF: [[LAW_HIERARCHY]]
claim_class: AMOS_MODEL
