---
title: "INV-AUTHZ-027 — Memory Decay without Evidence"
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
  - inv-authz-027
---

# INV-AUTHZ-027 — Memory Decay without Evidence

## 1. Formal Specification

> **Invariant Statement:**
> `Semantic memory associations unsupported by fresh evidence decay according to the phi-exponential curve.`

## 2. Invariant Rule & Mathematical Formulation

Let $m$ be a semantic memory association, $\text{LastEvidence}(m)$ the timestamp of the last supporting evidence, and $\text{Strength}(m, t)$ the memory strength at time $t$:

$$\text{Strength}(m, t) = \text{Strength}_0 \cdot e^{-\phi \cdot (t - \text{LastEvidence}(m))}$$

where $\phi$ is the decay rate constant and $\text{Strength}_0$ is the initial strength.

The decay triggers when no fresh evidence has been received:

$$t - \text{LastEvidence}(m) > \tau_{\text{fresh}} \implies \text{Decaying}(m) = \text{True}$$

Memory is purged when strength falls below the retention threshold:

$$\text{Strength}(m, t) < \theta_{\text{retain}} \implies \text{Purge}(m)$$

Fresh evidence resets the decay:

$$\text{NewEvidence}(m, t) \implies \text{LastEvidence}(m) \leftarrow t \land \text{Strength}(m, t) \leftarrow \text{Strength}_0$$

The phi-exponential decay curve ensures gradual, not abrupt, forgetting:

$$\frac{d}{dt} \text{Strength}(m, t) = -\phi \cdot \text{Strength}(m, t)$$

## 3. Enforcement & Verification

- **Evaluation Point:** Evaluated by the memory management system at periodic intervals. The system computes the current strength of all semantic memory associations and purges those below the retention threshold.
- **Violation Consequence:** If a memory association is retained despite being below the threshold without fresh evidence, a `MEMORY_RETENTION_VIOLATION` receipt is emitted to `17_OBSERVABILITY`. The memory is force-purged.
- **Recovery Procedure:** Purged memories can be re-established if fresh evidence is presented. The re-establishment follows the standard evidence verification pipeline per [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-012|INV-AUTHZ-012]].
- **Verification Cadence:** Periodic evaluation at configurable intervals (default: every epoch). On-demand evaluation triggered when memory pressure is detected.
- **Governed By:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

## 4. Attack Vectors & Mitigations

- **Evidence Starvation:** An attacker suppresses fresh evidence for a target memory to cause its decay and eventual purge. Mitigated by the gradual decay curve that provides time for evidence to arrive, and by the evidence verification pipeline that detects suppression attempts.
- **Decay Rate Manipulation:** An attacker modifies the decay rate constant to accelerate forgetting. Mitigated by the constant being stored in canon, protected by [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-006|INV-AUTHZ-006]].
- **False Evidence Injection:** An attacker injects false evidence to keep a decaying memory alive. Mitigated by [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-012|INV-AUTHZ-012]] which requires direct evidence for verification.
- **Threshold Manipulation:** An attacker lowers the retention threshold to cause premature purging. Mitigated by the threshold being stored in canon with multi-party authorization protection.

## 5. Dependencies & Prerequisites

- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-012|INV-AUTHZ-012]] — Reality grounding requirement ensures that evidence refreshing is properly verified.
- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-034|INV-AUTHZ-034]] — Epistemic drift threshold monitors knowledge drift that may result from memory decay.
- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-035|INV-AUTHZ-035]] — Bounded context attention manages working memory under token budget constraints.
- **Requires:** A memory management system with strength tracking and decay computation.
- **Requires:** An evidence timestamp tracking mechanism.

## 6. Provenance & Audit Trail

- **Receipt Type:** `MEMORY_DECAY_RECEIPT` — emitted for every memory purge due to decay, recording the memory ID, last evidence timestamp, strength at purge, and decay duration.
- **Storage Location:** `17_OBSERVABILITY` with memory-ID-indexed partitions.
- **Receipt Fields:** Memory ID, initial strength, final strength, last evidence timestamp, decay duration, purge timestamp, BLAKE3 hash.
- **Immutability:** Memory decay receipts are append-only per [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-014|INV-AUTHZ-014]].

## 7. Related Invariants

- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-012|INV-AUTHZ-012]] — Reality Grounding Requirement
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-034|INV-AUTHZ-034]] — Epistemic Drift Threshold
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-035|INV-AUTHZ-035]] — Bounded Context Attention
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-041|INV-AUTHZ-041]] — Episodic Trace Retention
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-047|INV-AUTHZ-047]] — Selective Invalidation Granularity

## 8. Navigation & Bindings

- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
- **Control Plane Contract:** [[03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT|CONTROL_PLANE_CONTRACT]]
- **Canon Law Hierarchy:** [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- **Kernel:** [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]]
- **Observability:** [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY_MOC]]
