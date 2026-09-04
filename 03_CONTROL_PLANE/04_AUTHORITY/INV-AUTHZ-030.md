---
title: "INV-AUTHZ-030 — Byzantine Tolerance Threshold"
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
  - inv-authz-030
---

# INV-AUTHZ-030 — Byzantine Tolerance Threshold

## 1. Formal Specification

> **Invariant Statement:**
> `Consensus across federated cognitive matrix cells requires >= 3f + 1 agreement.`

## 2. Invariant Rule & Mathematical Formulation

Let $N$ be the total number of federated cognitive matrix cells, $f$ the maximum number of Byzantine (faulty) cells, and $\text{Quorum}(N, f)$ the required agreement threshold:

$$\text{Quorum}(N, f) \ge 3f + 1$$

The relationship between total cells and tolerable faults:

$$N \ge 3f + 1 \implies f \le \lfloor \frac{N - 1}{3} \rfloor$$

The consensus condition requires:

$$\text{Consensus}(\text{decision}) \implies |\{ c \in \mathcal{C} : \text{Agree}(c, \text{decision}) \}| \ge 2f + 1$$

where $\mathcal{C}$ is the set of participating cells.

No decision may be finalized with fewer than $2f + 1$ agreements:

$$|\text{Agreements}(\text{decision})| < 2f + 1 \implies \text{Finalize}(\text{decision}) = \text{False}$$

## 3. Enforcement & Verification

- **Evaluation Point:** Evaluated at the consensus protocol layer when a decision is submitted for finalization. The protocol counts agreements from participating cells and checks the quorum threshold.
- **Violation Consequence:** If fewer than $2f + 1$ agreements are received, the decision is not finalized. The consensus protocol retries with additional rounds or aborts. A `CONSENSUS_QUORUM_FAILURE` receipt is emitted to `17_OBSERVABILITY`.
- **Recovery Procedure:** The consensus protocol enters a view-change phase to select a new leader and retry the consensus round. If the Byzantine cells are identified, they are excluded from subsequent rounds.
- **Verification Cadence:** Synchronous at every consensus finalization attempt. The quorum threshold is verified at each consensus round.
- **Governed By:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

## 4. Attack Vectors & Mitigations

- **Byzantine Quorum Block:** Byzantine cells refuse to agree, preventing the quorum from being reached. Mitigated by the view-change protocol that selects a new leader and retries, eventually excluding unresponsive cells.
- **Sybil Attack:** An attacker creates many fake cells to exceed the fault tolerance bound. Mitigated by cell identity being cryptographically verified per [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-042|INV-AUTHZ-042]].
- **Quorum Threshold Manipulation:** An attacker modifies the quorum threshold to lower the required agreements. Mitigated by the threshold being computed from $N$ and $f$, which are stored in canon.
- **Split-Brain Consensus:** A network partition causes two subgroups to each reach quorum independently. Mitigated by [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-017|INV-AUTHZ-017]] fail-closed on desync, which halts consensus during partitions.

## 5. Dependencies & Prerequisites

- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-017|INV-AUTHZ-017]] — Fail-closed on desync prevents split-brain consensus.
- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-042|INV-AUTHZ-042]] — Strict identity continuity prevents Sybil attacks.
- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-049|INV-AUTHZ-049]] — Global finality horizon check ensures all shards acknowledge before finalization.
- **Requires:** A Byzantine-fault-tolerant consensus protocol (e.g., PBFT, Raft with Byzantine extensions).
- **Requires:** A cell identity verification system.

## 6. Provenance & Audit Trail

- **Receipt Type:** `CONSENSUS_RECEIPT` — emitted for every consensus decision, recording the participating cells, agreements, dissents, and quorum verification.
- **Storage Location:** `17_OBSERVABILITY` with decision-ID-indexed partitions.
- **Receipt Fields:** Decision ID, participating cell set, agreement count, dissent count, quorum threshold, finalization status, view-change count, BLAKE3 hash.
- **Immutability:** Consensus receipts are append-only per [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-014|INV-AUTHZ-014]].

## 7. Related Invariants

- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-007|INV-AUTHZ-007]] — Atomic State Transition Barrier
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-017|INV-AUTHZ-017]] — Fail-Closed on Desync
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-042|INV-AUTHZ-042]] — Strict Identity Continuity
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-049|INV-AUTHZ-049]] — Global Finality Horizon Check
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-022|INV-AUTHZ-022]] — No Silent Failure

## 8. Navigation & Bindings

- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
- **Control Plane Contract:** [[03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT|CONTROL_PLANE_CONTRACT]]
- **Canon Law Hierarchy:** [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- **Kernel:** [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]]
- **Observability:** [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY_MOC]]
