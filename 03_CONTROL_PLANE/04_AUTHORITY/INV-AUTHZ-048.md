---
title: INV-AUTHZ-048 — Popperian Falsification Floor
type: authority_invariant
source: 03_CONTROL_PLANE/04_AUTHORITY
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_INVARIANT
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT
    - 01_CANON/01_CORE_LAWS/LAW_HIERARCHY
  scope: authority_governance
tags:
  - amos-os
  - authority
  - invariant
  - control-plane
  - inv-authz-048
---

# INV-AUTHZ-048 — Popperian Falsification Floor

## 1. Formal Specification

> **Invariant Statement:**
> `Unfalsifiable claims cannot be admitted into 01_CANON or 22_RESEARCH.`

## 2. Invariant Rule & Mathematical Formulation

Let $\mathcal{A}$ be the action space, $\mathcal{S}$ the state space, and $\mathcal{P}$ the active permission policy:

$$\forall a \in \mathcal{A}, \quad \text{Valid}(a, \mathcal{S}) \implies \text{Enforce}_{INV-AUTHZ-048}(a) = \text{True}$$

## 3. Enforcement & Verification

- **Evaluation Point:** Evaluated at the Control Plane gate prior to state mutation.
- **Violation Consequence:** Immediate transaction abort, error receipt emission to `17_OBSERVABILITY`, and routing to `ROLLBACK_BASIN`.
- **Governed By:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
