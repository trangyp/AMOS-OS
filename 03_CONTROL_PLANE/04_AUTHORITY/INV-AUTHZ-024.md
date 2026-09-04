---
title: INV-AUTHZ-024 — Competing Hypotheses Preservation
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
  - inv-authz-024
---

# INV-AUTHZ-024 — Competing Hypotheses Preservation

## 1. Formal Specification

> **Invariant Statement:**
> `Unresolved scientific or empirical debates must retain all non-refuted competing models.`

## 2. Invariant Rule & Mathematical Formulation

Let $\mathcal{H} = \{ h_1, h_2, \ldots, h_n \}$ be the set of competing hypotheses for a question $q$, and $\text{Refuted}(h)$ the refutation status:

$$\forall q, \forall \mathcal{H}(q), \quad \neg \text{Resolved}(q) \implies \forall h_i \in \mathcal{H}(q) : \neg \text{Refuted}(h_i), \quad \text{Retain}(h_i) = \text{True}$$

A hypothesis may only be removed when explicitly refuted:

$$\text{Remove}(h_i) \implies \text{Refuted}(h_i) = \text{True} \land \exists e : \text{RefutingEvidence}(e, h_i)$$

The resolution condition requires that all but one hypothesis are refuted:

$$\text{Resolved}(q) \iff |\{ h \in \mathcal{H}(q) : \neg \text{Refuted}(h) \}| \le 1$$

No hypothesis may be suppressed without explicit refutation:

$$\nexists h_i \in \mathcal{H}(q) : \text{Suppressed}(h_i) \land \neg \text{Refuted}(h_i)$$

## 3. Enforcement & Verification

- **Evaluation Point:** Evaluated at the hypothesis management gate when a hypothesis is submitted for removal or suppression. The gate checks that the hypothesis has been explicitly refuted with evidence.
- **Violation Consequence:** If a non-refuted hypothesis is submitted for removal, the removal is refused. A `HYPOTHESIS_SUPPRESSION_VIOLATION` receipt is emitted to `17_OBSERVABILITY`.
- **Recovery Procedure:** The hypothesis must remain in the competing set until it is explicitly refuted with evidence. No rollback is needed since the removal was blocked.
- **Verification Cadence:** Synchronous at every hypothesis removal request. A periodic audit verifies that all unresolved questions retain their full non-refuted hypothesis sets.
- **Governed By:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

## 4. Attack Vectors & Mitigations

- **Hypothesis Suppression:** An agent suppresses a competing hypothesis to promote its preferred model. Mitigated by the mandatory refutation check that prevents removal of non-refuted hypotheses.
- **Premature Resolution Declaration:** An agent declares a question resolved while multiple non-refuted hypotheses remain. Mitigated by the resolution condition that requires all but one hypothesis to be explicitly refuted.
- **Refutation Fabrication:** An agent fabricates refuting evidence to eliminate a competing hypothesis. Mitigated by [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-012|INV-AUTHZ-012]] which requires direct evidence for claims.
- **Hypothesis Set Truncation:** An agent truncates the hypothesis set to remove inconvenient alternatives. Mitigated by the periodic audit that verifies hypothesis set completeness.

## 5. Dependencies & Prerequisites

- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-012|INV-AUTHZ-012]] — Reality grounding requirement ensures refutations are backed by evidence.
- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-021|INV-AUTHZ-021]] — Confidence ceiling capping ensures no hypothesis is over-credited.
- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-039|INV-AUTHZ-039]] — Falsification obligation ensures hypotheses have testable refutation conditions.
- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-048|INV-AUTHZ-048]] — Popperian falsification floor ensures hypotheses are falsifiable.
- **Requires:** A hypothesis registry with refutation tracking.
- **Requires:** An evidence verification pipeline for refuting claims.

## 6. Provenance & Audit Trail

- **Receipt Type:** `HYPOTHESIS_MANAGEMENT_RECEIPT` — emitted for every hypothesis addition, refutation, or removal attempt, recording the question, hypothesis, and action.
- **Storage Location:** `17_OBSERVABILITY` with question-ID-indexed partitions.
- **Receipt Fields:** Question ID, hypothesis ID, action type (add, refute, remove), refuting evidence (if applicable), resolution status, epoch, BLAKE3 hash.
- **Immutability:** Hypothesis management receipts are append-only per [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-014|INV-AUTHZ-014]].

## 7. Related Invariants

- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-012|INV-AUTHZ-012]] — Reality Grounding Requirement
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-021|INV-AUTHZ-021]] — Confidence Ceiling Capping
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-034|INV-AUTHZ-034]] — Epistemic Drift Threshold
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-039|INV-AUTHZ-039]] — Invariant Falsification Obligation
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-048|INV-AUTHZ-048]] — Popperian Falsification Floor

## 8. Navigation & Bindings

- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
- **Control Plane Contract:** [[03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT|CONTROL_PLANE_CONTRACT]]
- **Canon Law Hierarchy:** [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- **Kernel:** [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]]
- **Observability:** [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY_MOC]]
