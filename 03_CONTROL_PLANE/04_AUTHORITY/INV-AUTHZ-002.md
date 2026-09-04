---
title: INV-AUTHZ-002 — Capability Token Epoch Expiration
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
  - inv-authz-002
---

# INV-AUTHZ-002 — Capability Token Epoch Expiration

## 1. Formal Specification

> **Invariant Statement:**
> `Every capability token expires strictly at the boundary of the current causal epoch E_k.`

## 2. Invariant Rule & Mathematical Formulation

Let $\mathcal{T}$ be the set of all capability tokens, $E_k$ the current causal epoch, and $\text{exp}(\tau)$ the expiration epoch of token $\tau$:

$$\forall \tau \in \mathcal{T}, \quad \text{exp}(\tau) = E_k \implies \text{Valid}(\tau, E_{k+1}) = \text{False}$$

A token $\tau$ is valid only within its issuing epoch:

$$\text{Valid}(\tau, E_j) \iff \text{issued}(\tau) \le j \le \text{exp}(\tau) \land \text{exp}(\tau) = \text{issued}(\tau)$$

The token validity window is thus a singleton epoch:

$$\text{Window}(\tau) = \{ E_{\text{issued}(\tau)} \}$$

No token may span multiple epochs. At epoch transition $E_k \to E_{k+1}$, all tokens from $E_k$ are invalidated:

$$|\{ \tau \in \mathcal{T} : \text{exp}(\tau) = E_k \}| \ge 0 \implies \forall \tau : \text{exp}(\tau) = E_k, \; \text{Purge}(\tau)$$

## 3. Enforcement & Verification

- **Evaluation Point:** Evaluated at every capability token validation call within the Control Plane gate. Additionally, a batch purge is executed at each epoch transition boundary.
- **Violation Consequence:** If a token from a prior epoch is presented, the transaction is immediately aborted. An `EXPIRED_TOKEN_VIOLATION` receipt is emitted to `17_OBSERVABILITY`. The presenting agent is flagged for re-authorization.
- **Recovery Procedure:** The agent must request a new capability token for the current epoch through the standard authorization flow. No state rollback is needed if the token was rejected before any mutation occurred.
- **Verification Cadence:** Synchronous at every token presentation. The epoch transition purge runs as a background batch operation triggered by the consensus clock.
- **Governed By:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

## 4. Attack Vectors & Mitigations

- **Stale Token Reuse:** An agent retains a token from a previous epoch and attempts to use it for state mutation. Mitigated by the epoch-boundary purge and synchronous validation that checks the token's expiration epoch against the current epoch.
- **Token Lifetime Extension:** An agent attempts to modify the expiration field of its capability token. Mitigated by cryptographic signatures on tokens per [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-018|INV-AUTHZ-018]] — any modification invalidates the signature.
- **Epoch Boundary Race:** An agent exploits the transition window between epochs to use an expiring token. Mitigated by the atomic epoch transition protocol that invalidates all prior-epoch tokens before accepting any new-epoch operations.
- **Token Replay Across Epochs:** A captured token is replayed in a later epoch. Mitigated by single-use nonces per [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-032|INV-AUTHZ-032]] in addition to epoch expiration.

## 5. Dependencies & Prerequisites

- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-001|INV-AUTHZ-001]] — Root authority must be established to issue capability tokens.
- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-018|INV-AUTHZ-018]] — Cryptographic token integrity ensures expiration fields cannot be tampered with.
- **Requires:** A monotonically increasing epoch counter maintained by the consensus layer.
- **Requires:** Synchronized epoch transitions across all shards, enforced by [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-017|INV-AUTHZ-017]].

## 6. Provenance & Audit Trail

- **Receipt Type:** `TOKEN_EXPIRATION_RECEIPT` — emitted for each token purged at epoch boundary.
- **Storage Location:** `17_OBSERVABILITY` with epoch-indexed partitioning for efficient historical queries.
- **Receipt Fields:** Token ID, issuing epoch, expiration epoch, purging epoch, agent identity, BLAKE3 hash chain link.
- **Immutability:** Purge receipts are append-only per [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-014|INV-AUTHZ-014]].

## 7. Related Invariants

- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-001|INV-AUTHZ-001]] — Root Authority Non-Transferability
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-018|INV-AUTHZ-018]] — Cryptographic Token Integrity
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-032|INV-AUTHZ-032]] — No Token Replay
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-017|INV-AUTHZ-017]] — Fail-Closed on Desync
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-004|INV-AUTHZ-004]] — Explicit Revocation Immediacy

## 8. Navigation & Bindings

- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
- **Control Plane Contract:** [[03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT|CONTROL_PLANE_CONTRACT]]
- **Canon Law Hierarchy:** [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- **Kernel:** [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]]
- **Observability:** [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY_MOC]]
