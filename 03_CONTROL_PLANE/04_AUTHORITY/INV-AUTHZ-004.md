---
title: INV-AUTHZ-004 — Explicit Revocation Immediacy
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
  - inv-authz-004
---

# INV-AUTHZ-004 — Explicit Revocation Immediacy

## 1. Formal Specification

> **Invariant Statement:**
> `A revocation request takes effect immediately across all active shards without waiting for epoch sync.`

## 2. Invariant Rule & Mathematical Formulation

Let $\text{Revoke}(\tau, t)$ denote the revocation of token $\tau$ at logical time $t$, and $\text{Shards}(\tau)$ the set of shards where $\tau$ is currently active:

$$\forall \tau \in \mathcal{T}, \forall s \in \text{Shards}(\tau), \quad \text{Revoke}(\tau, t) \implies \text{Invalid}(\tau, s, t + \epsilon_{\text{prop}})$$

where $\epsilon_{\text{prop}} \to 0$ is the propagation delay, which must be negligible (sub-millisecond):

$$\epsilon_{\text{prop}} < \epsilon_{\text{transport}}$$

The revocation is globally consistent — no shard may accept $\tau$ after the revocation logical time:

$$\forall s \in \mathcal{S}, \quad \text{Valid}(\tau, s, t') \land t' > t \implies \text{False}$$

The revocation vector $\mathbf{R}$ is a bloom-filter-indexed structure propagated via a low-latency gossip protocol:

$$\mathbf{R}(t) = \mathbf{R}(t^-) \cup \{ \text{hash}(\tau) \}$$

## 3. Enforcement & Verification

- **Evaluation Point:** Evaluated at every capability token validation call in every shard. The revocation list is checked synchronously before any token is accepted.
- **Violation Consequence:** If a revoked token is presented, the transaction is immediately aborted. A `REVOKED_TOKEN_VIOLATION` receipt is emitted to `17_OBSERVABILITY`. The presenting agent is flagged for investigation.
- **Recovery Procedure:** The agent must obtain a new capability token through the standard authorization flow. The revocation itself is irreversible — once revoked, a token cannot be un-revoked; a new token must be issued.
- **Verification Cadence:** Synchronous at every token validation. The revocation list is continuously gossiped across shards with sub-millisecond propagation targets.
- **Governed By:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

## 4. Attack Vectors & Mitigations

- **Revocation Delay Exploitation:** An attacker exploits a window between revocation issuance and shard-level enforcement to perform unauthorized actions. Mitigated by the gossip-based propagation protocol with sub-millisecond targets and synchronous revocation list checks.
- **Revocation List Tampering:** An attacker modifies the revocation list to remove their token. Mitigated by the bloom-filter structure being content-addressed and cryptographically signed by the revoking authority.
- **Split-Brain Revocation:** A network partition causes some shards to miss the revocation. Mitigated by [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-017|INV-AUTHZ-017]] which halts all state promotions on clock divergence, preventing partitioned shards from accepting revoked tokens.
- **Revocation Replay:** A revocation message is replayed to cause denial of service. Mitigated by logical-time stamping on revocation messages, which prevents stale revocations from affecting newly issued tokens.

## 5. Dependencies & Prerequisites

- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-002|INV-AUTHZ-002]] — Epoch expiration provides a secondary safety net for token invalidation.
- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-017|INV-AUTHZ-017]] — Fail-closed on desync prevents partitioned shards from missing revocations.
- **Requires:** A low-latency gossip protocol for revocation list propagation across all shards.
- **Requires:** A content-addressed revocation list structure with cryptographic integrity.

## 6. Provenance & Audit Trail

- **Receipt Type:** `REVOCATION_RECEIPT` — emitted for every revocation event, recording the revoked token, revoking authority, logical time, and propagation acknowledgment from all shards.
- **Storage Location:** `17_OBSERVABILITY` with time-indexed and token-indexed partitions.
- **Receipt Fields:** Revoked token ID, revoking authority identity, logical timestamp, shard acknowledgment vector, reason code, BLAKE3 hash.
- **Immutability:** Revocation receipts are append-only per [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-014|INV-AUTHZ-014]].

## 7. Related Invariants

- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-002|INV-AUTHZ-002]] — Capability Token Epoch Expiration
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-009|INV-AUTHZ-009]] — Quarantine on Anomaly
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-017|INV-AUTHZ-017]] — Fail-Closed on Desync
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-019|INV-AUTHZ-019]] — Emergency Kill-Switch Supremacy
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-032|INV-AUTHZ-032]] — No Token Replay

## 8. Navigation & Bindings

- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
- **Control Plane Contract:** [[03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT|CONTROL_PLANE_CONTRACT]]
- **Canon Law Hierarchy:** [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- **Kernel:** [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]]
- **Observability:** [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY_MOC]]
