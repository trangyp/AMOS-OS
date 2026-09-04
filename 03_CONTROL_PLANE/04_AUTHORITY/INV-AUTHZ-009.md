---
title: INV-AUTHZ-009 — Quarantine on Anomaly
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
  - inv-authz-009
---

# INV-AUTHZ-009 — Quarantine on Anomaly

## 1. Formal Specification

> **Invariant Statement:**
> `Any agent exhibiting epistemic drift > delta_threshold is immediately moved to QUARANTINED status.`

## 2. Invariant Rule & Mathematical Formulation

Let $\text{Drift}(a, E_k)$ be the epistemic drift of agent $a$ at epoch $E_k$, measured as the KL-divergence between the agent's belief state and the canonical reference:

$$\text{Drift}(a, E_k) = D_{\text{KL}}(\text{Belief}(a, E_k) \| \text{Canon}(E_k))$$

The quarantine condition is:

$$\forall a \in \mathcal{A}, \quad \text{Drift}(a, E_k) > \delta_{\text{threshold}} \implies \text{Status}(a) \leftarrow \text{QUARANTINED}$$

where $\delta_{\text{threshold}}$ is the configurable drift threshold (default: 0.05).

Once quarantined, the agent's capability tokens are suspended:

$$\text{Status}(a) = \text{QUARANTINED} \implies \forall \tau \in \text{Tokens}(a), \quad \text{Valid}(\tau) = \text{False}$$

The quarantine transition is immediate and atomic:

$$\text{Drift}(a, E_k) > \delta_{\text{threshold}} \implies \text{Quarantine}(a, t_{\text{detect}})$$

## 3. Enforcement & Verification

- **Evaluation Point:** Evaluated continuously by the epistemic drift monitor, which computes drift scores for all active agents at every epoch boundary and on-demand after significant state changes.
- **Violation Consequence:** The agent is immediately moved to QUARANTINED status. All capability tokens are suspended. A `QUARANTINE_EVENT` receipt is emitted to `17_OBSERVABILITY`. The agent's pending transactions are aborted and routed to `ROLLBACK_BASIN`.
- **Recovery Procedure:** A quarantined agent must undergo a manual review by the Origin Architect or a designated gatekeeper. After review, the agent may be cleared, re-initialized, or permanently retired. Clearance requires a signed release receipt.
- **Verification Cadence:** Continuous drift monitoring at every epoch boundary. On-demand drift checks can be triggered by anomaly detection systems or by other invariants that flag suspicious behavior.
- **Governed By:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

## 4. Attack Vectors & Mitigations

- **Gradual Epistemic Drift:** An agent slowly drifts from canonical beliefs over multiple epochs, staying below the per-epoch threshold but accumulating significant deviation. Mitigated by cumulative drift tracking that sums per-epoch drift and triggers quarantine on cumulative exceedance.
- **Drift Threshold Manipulation:** An attacker modifies the drift threshold to avoid quarantine. Mitigated by the threshold being stored in the canon, protected by [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-006|INV-AUTHZ-006]] multi-party authorization.
- **Quarantine Evasion:** A drifting agent avoids detection by manipulating its reported belief state. Mitigated by the drift computation using the agent's observable outputs, not self-reported beliefs.
- **False Positive Quarantine:** A legitimate agent is quarantined due to a transient drift spike. Mitigated by the recovery procedure allowing manual review and clearance, with rollback of any incorrectly aborted transactions.

## 5. Dependencies & Prerequisites

- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-004|INV-AUTHZ-004]] — Revocation immediacy ensures quarantined agents' tokens are instantly suspended.
- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-034|INV-AUTHZ-034]] — Epistemic drift threshold defines the automated audit trigger.
- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-022|INV-AUTHZ-022]] — No silent failure ensures quarantine events are properly logged.
- **Requires:** A canonical reference belief state maintained in `01_CANON`.
- **Requires:** A KL-divergence computation engine for drift measurement.

## 6. Provenance & Audit Trail

- **Receipt Type:** `QUARANTINE_EVENT_RECEIPT` — emitted for every quarantine transition, recording the drift score, threshold, agent identity, and triggering epoch.
- **Storage Location:** `17_OBSERVABILITY` with agent-indexed and epoch-indexed partitions.
- **Receipt Fields:** Agent identity, drift score, threshold value, triggering epoch, suspended token IDs, quarantine timestamp, BLAKE3 hash.
- **Immutability:** Quarantine receipts are append-only per [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-014|INV-AUTHZ-014]].

## 7. Related Invariants

- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-004|INV-AUTHZ-004]] — Explicit Revocation Immediacy
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-005|INV-AUTHZ-005]] — No Self-Escalation
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-019|INV-AUTHZ-019]] — Emergency Kill-Switch Supremacy
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-022|INV-AUTHZ-022]] — No Silent Failure
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-034|INV-AUTHZ-034]] — Epistemic Drift Threshold

## 8. Navigation & Bindings

- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
- **Control Plane Contract:** [[03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT|CONTROL_PLANE_CONTRACT]]
- **Canon Law Hierarchy:** [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- **Kernel:** [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]]
- **Observability:** [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY_MOC]]
