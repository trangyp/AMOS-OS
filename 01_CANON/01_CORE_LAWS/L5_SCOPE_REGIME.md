---
tags: ['canon', 'core_laws', 'note']
---

# L5 Scope, Regime, and Temporal Laws

STATUS: PROPOSED_SPECIFICATION
epistemic_class: AMOS_MODEL
canonical_status: CONDITIONAL
implementation_status: LOGIC_EXECUTABLE_IN_PART
updated: 2026-08-26

## 0. Status
Proposed specification. Epistemic class: AMOS_MODEL. Canonical status: CONDITIONAL.

## 1. Purpose
Constrain every claim and operation by its declared scope, regime, and temporal validity.

## 2. Laws
- **SRL-1 Scope Containment**: a claim valid in scope S is not silently valid outside S.
- **SRL-2 Regime Isolation**: claims validated in regime A require revalidation in regime B.
- **SRL-3 Temporal Validity**: every load-bearing claim carries an epoch; stale claims do not silently remain active (freshness).
- **SRL-4 No Silent Expansion**: neither scope nor regime may widen without explicit policy.

## 3. Enforcement
Executable checks: scope subset tests, regime equality gates, epoch freshness comparisons (see routing validator I-RPOL-008..010; AUTHZ INV-011/017/021).

## 4. Falsifiers
F1: authoritative canon defines materially different scope/regime semantics.
F2: accepted implementation enforces different temporal model.

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]]

---
RSCF-NODE
node_id: l5_scope_regime
node_type: note
path: 01_CANON/01_CORE_LAWS/L5_SCOPE_REGIME.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
  - CHILD_OF: [[LAW_HIERARCHY]]
claim_class: AMOS_MODEL
