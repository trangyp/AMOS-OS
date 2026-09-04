---
title: "INV-AUTHZ-012 — Reality Grounding Requirement"
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
  - inv-authz-012
---

# INV-AUTHZ-012 — Reality Grounding Requirement

## 1. Formal Specification

> **Invariant Statement:**
> `Claims cannot be promoted to verified state without direct empirical or mathematical evidence.`

## 2. Invariant Rule & Mathematical Formulation

Let $\mathcal{C}$ be the set of claims, $\text{State}(c)$ the epistemic state of claim $c$, and $\text{Evidence}(c)$ the evidence set supporting $c$:

$$\forall c \in \mathcal{C}, \quad \text{Promote}(c, \text{VERIFIED}) \implies |\text{Evidence}(c)| \ge 1 \land \text{Direct}(\text{Evidence}(c))$$

The evidence must be either empirical or mathematical:

$$\text{Valid}(e) \iff \text{Empirical}(e) \lor \text{Mathematical}(e)$$

where $\text{Empirical}(e)$ requires observable measurement and $\text{Mathematical}(e)$ requires formal proof.

The promotion function is guarded:

$$\text{Promote}(c, \text{VERIFIED}) = \begin{cases} \text{True} & \text{if } \exists e \in \text{Evidence}(c) : \text{Valid}(e) \land \text{Direct}(e, c) \\ \text{False} & \text{otherwise} \end{cases}$$

Indirect or circumstantial evidence alone is insufficient:

$$\text{Indirect}(\text{Evidence}(c)) \land \neg \text{Direct}(\text{Evidence}(c)) \implies \text{State}(c) \neq \text{VERIFIED}$$

## 3. Enforcement & Verification

- **Evaluation Point:** Evaluated at the epistemic state transition gate when a claim is submitted for promotion from SOURCE_CLAIM or DERIVED to VERIFIED status.
- **Violation Consequence:** If a claim is submitted for promotion without direct evidence, the promotion is refused. The claim remains in its current epistemic state. A `REALITY_GROUNDING_VIOLATION` receipt is emitted to `17_OBSERVABILITY`.
- **Recovery Procedure:** The claim must be resubmitted with direct empirical or mathematical evidence attached. The evidence must pass validation by the evidence verification pipeline.
- **Verification Cadence:** Synchronous at every claim promotion attempt. A periodic audit samples verified claims to confirm that their supporting evidence remains valid and accessible.
- **Governed By:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

## 4. Attack Vectors & Mitigations

- **Evidence-Free Promotion:** An agent attempts to promote its own claim to verified status without any supporting evidence. Mitigated by the mandatory evidence check at the promotion gate.
- **Fabricated Evidence:** An agent submits fabricated empirical data as evidence. Mitigated by the evidence verification pipeline that cross-checks empirical claims against independent observation channels.
- **Circular Evidence:** A claim is supported by evidence that itself depends on the claim being true. Mitigated by the directness requirement that evidence must be independently verifiable.
- **Evidence Dilution:** A large volume of indirect evidence is presented to overwhelm the directness requirement. Mitigated by the formal check that at least one piece of evidence must be direct, regardless of the volume of indirect evidence.

## 5. Dependencies & Prerequisites

- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-021|INV-AUTHZ-021]] — Confidence ceiling capping ensures that verified claims cannot assert confidence beyond their evidence.
- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-024|INV-AUTHZ-024]] — Competing hypotheses preservation ensures alternative explanations are retained.
- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-048|INV-AUTHZ-048]] — Popperian falsification floor ensures claims must be falsifiable to enter canon.
- **Requires:** An evidence verification pipeline capable of distinguishing empirical, mathematical, and indirect evidence.
- **Requires:** An epistemic state machine that tracks claim provenance and evidence chains.

## 6. Provenance & Audit Trail

- **Receipt Type:** `CLAIM_PROMOTION_RECEIPT` — emitted for every claim promotion attempt, recording the evidence set, directness verification, and promotion decision.
- **Storage Location:** `17_OBSERVABILITY` with claim-ID-indexed and epistemic-state-indexed partitions.
- **Receipt Fields:** Claim ID, prior epistemic state, target epistemic state, evidence set, directness check result, promotion decision, evidence hashes, epoch, BLAKE3 hash.
- **Immutability:** Promotion receipts are append-only per [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-014|INV-AUTHZ-014]].

## 7. Related Invariants

- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-021|INV-AUTHZ-021]] — Confidence Ceiling Capping
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
