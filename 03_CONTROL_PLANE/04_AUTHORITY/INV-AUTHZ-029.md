---
title: "INV-AUTHZ-029 — Snapshot Isolation Consistency"
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
  - inv-authz-029
---

# INV-AUTHZ-029 — Snapshot Isolation Consistency

## 1. Formal Specification

> **Invariant Statement:**
> `Transactions read exclusively from immutable committed snapshots at epoch E_read.`

## 2. Invariant Rule & Mathematical Formulation

Let $T$ be a transaction with read epoch $E_{\text{read}}(T)$, and $\text{Snapshot}(E_k)$ the immutable committed state at epoch $E_k$:

$$\forall T \in \mathcal{T}, \forall r \in \text{Reads}(T), \quad \text{Source}(r) = \text{Snapshot}(E_{\text{read}}(T))$$

The snapshot is immutable — no concurrent writes may modify it:

$$\text{Immutable}(\text{Snapshot}(E_k)) \implies \forall w, \quad \text{Write}(w, \text{Snapshot}(E_k)) = \text{False}$$

The read epoch is fixed at transaction start:

$$E_{\text{read}}(T) = E_{\text{start}}(T) \quad \text{(fixed for transaction lifetime)}$$

Transactions do not observe uncommitted changes:

$$\forall T, \forall w \in \text{Writes}(\text{concurrent}(T)), \quad \text{Visible}(w, T) = \text{False} \text{ if } \text{Commit}(w) > E_{\text{read}}(T)$$

## 3. Enforcement & Verification

- **Evaluation Point:** Evaluated at the transaction read gate. Every read operation is directed to the immutable snapshot at the transaction's read epoch.
- **Violation Consequence:** If a read operation attempts to access uncommitted or post-epoch state, the read is redirected to the correct snapshot. A `SNAPSHOT_ISOLATION_VIOLATION` receipt is emitted to `17_OBSERVABILITY`.
- **Recovery Procedure:** The transaction continues with reads from the correct snapshot. If the snapshot is no longer available (garbage collected), the transaction is aborted and must be retried with a newer read epoch.
- **Verification Cadence:** Synchronous at every read operation. A periodic audit verifies that all active transactions are reading from their designated snapshots.
- **Governed By:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

## 4. Attack Vectors & Mitigations

- **Snapshot Bypass:** An agent reads from the live state instead of the committed snapshot to observe uncommitted changes. Mitigated by the read gate that directs all reads to the immutable snapshot.
- **Snapshot Manipulation:** An attacker modifies a committed snapshot to alter the transaction's view. Mitigated by the immutability of committed snapshots and by [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-044|INV-AUTHZ-044]] Merkle tree verification.
- **Epoch Advancement Race:** A transaction's read epoch becomes stale as the system advances. Mitigated by the read epoch being fixed at transaction start, ensuring consistent reads throughout the transaction.
- **Snapshot Garbage Collection Race:** A snapshot is garbage collected while a transaction is still reading from it. Mitigated by the garbage collection protocol that checks for active transactions before removing snapshots.

## 5. Dependencies & Prerequisites

- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-028|INV-AUTHZ-028]] — Single writer per shard ensures writes are serialized, supporting snapshot creation.
- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-044|INV-AUTHZ-044]] — Merkle tree proof verification enables snapshot integrity verification.
- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-002|INV-AUTHZ-002]] — Epoch expiration defines snapshot boundaries.
- **Requires:** A snapshot management system with immutable snapshot creation and retention.
- **Requires:** A garbage collection protocol that respects active transactions.

## 6. Provenance & Audit Trail

- **Receipt Type:** `SNAPSHOT_READ_RECEIPT` — emitted for every transaction read, recording the read epoch, snapshot hash, and read path.
- **Storage Location:** `17_OBSERVABILITY` with transaction-ID-indexed and epoch-indexed partitions.
- **Receipt Fields:** Transaction ID, read epoch, snapshot hash, read path, read result hash, BLAKE3 hash.
- **Immutability:** Snapshot read receipts are append-only per [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-014|INV-AUTHZ-014]].

## 7. Related Invariants

- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-002|INV-AUTHZ-002]] — Capability Token Epoch Expiration
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-007|INV-AUTHZ-007]] — Atomic State Transition Barrier
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-015|INV-AUTHZ-015]] — Coordination Avoidance Verification
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-028|INV-AUTHZ-028]] — Single Writer per Shard
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-043|INV-AUTHZ-043]] — Non-Interference in Shard Reads

## 8. Navigation & Bindings

- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
- **Control Plane Contract:** [[03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT|CONTROL_PLANE_CONTRACT]]
- **Canon Law Hierarchy:** [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- **Kernel:** [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]]
- **Observability:** [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY_MOC]]
