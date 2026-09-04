---
title: INV-AUTHZ-021 — Confidence Ceiling Capping
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
  - inv-authz-021
---

# INV-AUTHZ-021 — Confidence Ceiling Capping

## 1. Formal Specification

> **Invariant Statement:**
> `Conclusions cannot assert confidence exceeding the weakest supporting premise (ceiling 0.95).`

## 2. Invariant Rule & Mathematical Formulation

Let $c$ be a conclusion with supporting premises $P = \{ p_1, p_2, \ldots, p_n \}$, and $\text{Conf}(x)$ the confidence of $x$:

$$\text{Conf}(c) \le \min_{p_i \in P} \text{Conf}(p_i)$$

The absolute ceiling is:

$$\text{Conf}(c) \le 0.95$$

The confidence propagation function is:

$$\text{Conf}(c) = \min\left( \min_{p_i \in P} \text{Conf}(p_i), \; 0.95 \right)$$

No aggregation method may produce a conclusion confidence exceeding the weakest premise:

$$\nexists f : \text{Conf}(f(P)) > \min_{p_i \in P} \text{Conf}(p_i)$$

The ceiling is strict — even with infinite supporting premises of confidence 0.95, the conclusion cannot exceed 0.95:

$$\forall P : |P| \to \infty, \quad \text{Conf}(c) \le 0.95$$

## 3. Enforcement & Verification

- **Evaluation Point:** Evaluated at the epistemic state transition gate when a conclusion is derived from premises. The gate computes the minimum premise confidence and caps the conclusion confidence accordingly.
- **Violation Consequence:** If a conclusion asserts confidence exceeding the ceiling, the confidence value is clamped to the ceiling. A `CONFIDENCE_CEILING_VIOLATION` receipt is emitted to `17_OBSERVABILITY`.
- **Recovery Procedure:** The conclusion's confidence is automatically clamped. No rollback is needed. The conclusion remains valid but with corrected confidence.
- **Verification Cadence:** Synchronous at every conclusion derivation. A periodic audit samples conclusions to verify that their confidence values respect the ceiling.
- **Governed By:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

## 4. Attack Vectors & Mitigations

- **Confidence Inflation:** An agent inflates a conclusion's confidence beyond its weakest premise to gain unwarranted authority. Mitigated by the ceiling check that clamps confidence at derivation time.
- **Ceiling Evasion via Aggregation:** An agent uses an aggregation method that claims to produce higher confidence than the weakest premise. Mitigated by the formal constraint that no aggregation method may exceed the minimum premise confidence.
- **Premise Confidence Fabrication:** An agent fabricates high-confidence premises to raise the ceiling for its conclusion. Mitigated by [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-012|INV-AUTHZ-012]] which requires evidence for verified claims.
- **Ceiling Modification:** An attacker modifies the ceiling value to allow higher confidence. Mitigated by the ceiling being stored in canon, protected by [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-006|INV-AUTHZ-006]].

## 5. Dependencies & Prerequisites

- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-012|INV-AUTHZ-012]] — Reality grounding requirement ensures premises have supporting evidence.
- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-024|INV-AUTHZ-024]] — Competing hypotheses preservation ensures alternative conclusions are retained.
- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-034|INV-AUTHZ-034]] — Epistemic drift threshold monitors confidence drift over time.
- **Requires:** A confidence tracking system that propagates confidence from premises to conclusions.
- **Requires:** A canonical ceiling value stored in `01_CANON`.

## 6. Provenance & Audit Trail

- **Receipt Type:** `CONFIDENCE_CEILING_RECEIPT` — emitted for every conclusion derivation, recording the premise confidences, computed ceiling, and final confidence.
- **Storage Location:** `17_OBSERVABILITY` with conclusion-ID-indexed partitions.
- **Receipt Fields:** Conclusion ID, premise set with confidences, minimum premise confidence, ceiling value, final confidence, clamping flag, epoch, BLAKE3 hash.
- **Immutability:** Confidence ceiling receipts are append-only per [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-014|INV-AUTHZ-014]].

## 7. Related Invariants

- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-012|INV-AUTHZ-012]] — Reality Grounding Requirement
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-024|INV-AUTHZ-024]] — Competing Hypotheses Preservation
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-034|INV-AUTHZ-034]] — Epistemic Drift Threshold
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-039|INV-AUTHZ-039]] — Invariant Falsification Obligation
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-048|INV-AUTHZ-048]] — Popperian Falsification Floor

## 8. Navigation & Bindings

- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
- **Control Plane Contract:** [[03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT|CONTROL_PLANE_CONTRACT]]
- **Canon Law Hierarchy:** [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- **Kernel:** [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]]
- **Observability:** [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY_MOC]]
