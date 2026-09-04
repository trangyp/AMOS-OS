---
title: "INV-AUTHZ-028 — Single Writer per Shard"
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
  - inv-authz-028
---

# INV-AUTHZ-028 — Single Writer per Shard

## 1. Formal Specification

> **Invariant Statement:**
> `Within a single shard, concurrent write mutations must acquire a local mutex or execute via CAS.`

## 2. Invariant Rule & Mathematical Formulation

Let $s$ be a shard, $\text{Writer}(s, t)$ the active writer on shard $s$ at time $t$, and $\text{Lock}(s)$ the local mutex:

$$\forall s \in \mathcal{S}, \forall t, \quad |\text{Writer}(s, t)| \le 1 \lor \text{CAS}(\text{Writer}(s, t))$$

The mutex acquisition requires:

$$\text{Acquire}(\text{Lock}(s), w) \implies \text{Writer}(s, t) = \{ w \} \quad \text{for duration of write}$$

The CAS (Compare-And-Swap) alternative:

$$\text{CAS}(s, \text{expected}, \text{new}) = \begin{cases} \text{True} & \text{if } \text{State}(s) = \text{expected} \\ \text{False} & \text{otherwise} \end{cases}$$

$$\text{CAS}(s, \text{expected}, \text{new}) = \text{True} \implies \text{State}(s) \leftarrow \text{new}$$

No two writers may hold the mutex simultaneously:

$$\forall w_1 \neq w_2, \quad \text{Holds}(w_1, \text{Lock}(s)) \implies \neg \text{Holds}(w_2, \text{Lock}(s))$$

## 3. Enforcement & Verification

- **Evaluation Point:** Evaluated at the shard-level write gate. Every write mutation must either hold the local mutex or use a CAS operation that atomically checks and updates the state.
- **Violation Consequence:** If a write mutation is attempted without holding the mutex or using CAS, the write is rejected. A `CONCURRENT_WRITE_VIOLATION` receipt is emitted to `17_OBSERVABILITY`.
- **Recovery Procedure:** The write must be retried with proper mutex acquisition or CAS. If a deadlock is detected, the deadlock resolution protocol aborts one of the conflicting writers.
- **Verification Cadence:** Synchronous at every write mutation. A periodic audit verifies that no shard has multiple concurrent writers.
- **Governed By:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

## 4. Attack Vectors & Mitigations

- **Mutex Bypass:** An agent writes to a shard without acquiring the mutex. Mitigated by the shard-level write gate that checks mutex ownership before accepting writes.
- **Mutex Hijacking:** An agent steals the mutex from the current holder. Mitigated by the mutex implementation being non-preemptive — only the holder can release the mutex.
- **CAS Race Exploitation:** An attacker exploits a race in the CAS implementation to create inconsistent state. Mitigated by the CAS being implemented as an atomic hardware instruction.
- **Deadlock Induction:** An attacker creates a deadlock by acquiring mutexes in a circular pattern. Mitigated by the deadlock detection protocol with timeout-based resolution.

## 5. Dependencies & Prerequisites

- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-007|INV-AUTHZ-007]] — Atomic state transition barrier coordinates multi-shard writes.
- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-015|INV-AUTHZ-015]] — Coordination avoidance verification determines when CAS is sufficient vs. mutex.
- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-043|INV-AUTHZ-043]] — Non-interference in shard reads ensures reads do not block writes.
- **Requires:** A mutex implementation with deadlock detection.
- **Requires:** A CAS primitive at the hardware or runtime level.

## 6. Provenance & Audit Trail

- **Receipt Type:** `SHARD_WRITE_RECEIPT` — emitted for every shard write, recording the writer identity, lock type (mutex or CAS), and write result.
- **Storage Location:** `17_OBSERVABILITY` with shard-ID-indexed partitions.
- **Receipt Fields:** Shard ID, writer identity, lock type, lock acquisition timestamp, write result, state hash before and after, BLAKE3 hash.
- **Immutability:** Shard write receipts are append-only per [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-014|INV-AUTHZ-014]].

## 7. Related Invariants

- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-007|INV-AUTHZ-007]] — Atomic State Transition Barrier
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-015|INV-AUTHZ-015]] — Coordination Avoidance Verification
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-029|INV-AUTHZ-029]] — Snapshot Isolation Consistency
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-043|INV-AUTHZ-043]] — Non-Interference in Shard Reads
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-049|INV-AUTHZ-049]] — Global Finality Horizon Check

## 8. Navigation & Bindings

- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
- **Control Plane Contract:** [[03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT|CONTROL_PLANE_CONTRACT]]
- **Canon Law Hierarchy:** [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- **Kernel:** [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]]
- **Observability:** [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY_MOC]]
