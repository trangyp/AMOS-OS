---
title: "INV-AUTHZ-018 — Cryptographic Token Integrity"
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
  - inv-authz-018
---

# INV-AUTHZ-018 — Cryptographic Token Integrity

## 1. Formal Specification

> **Invariant Statement:**
> `Capability tokens must use HMAC-SHA256 or Ed25519 signatures bound to task IDs.`

## 2. Invariant Rule & Mathematical Formulation

Let $\tau$ be a capability token, $\text{Sig}(\tau)$ the signature on $\tau$, and $\text{TaskID}(\tau)$ the bound task identifier:

$$\forall \tau \in \mathcal{T}, \quad \text{Valid}(\tau) \implies \text{SigScheme}(\tau) \in \{\text{HMAC-SHA256}, \text{Ed25519}\}$$

The signature binds the token to its task ID:

$$\text{Sig}(\tau) = \text{Sign}_{\text{sk}}(\text{TaskID}(\tau) \parallel \text{Scope}(\tau) \parallel \text{Epoch}(\tau) \parallel \text{Nonce}(\tau))$$

Verification requires the correct public key and task ID binding:

$$\text{Verify}(\tau) = \text{VerifySig}_{\text{pk}}(\text{Sig}(\tau), \text{TaskID}(\tau) \parallel \text{Scope}(\tau) \parallel \text{Epoch}(\tau) \parallel \text{Nonce}(\tau))$$

Any modification to the token invalidates the signature:

$$\text{Modify}(\tau) \implies \text{Verify}(\tau') = \text{False}$$

where $\tau'$ is the modified token.

## 3. Enforcement & Verification

- **Evaluation Point:** Evaluated at every capability token presentation to the Control Plane gate. The signature is verified against the issuing authority's public key and the bound task ID.
- **Violation Consequence:** If the signature is invalid or the signing scheme is not HMAC-SHA256 or Ed25519, the token is rejected. A `TOKEN_INTEGRITY_VIOLATION` receipt is emitted to `17_OBSERVABILITY`. The presenting agent must re-authenticate.
- **Recovery Procedure:** The agent must request a new capability token from the issuing authority with a valid signature. The old token is invalidated.
- **Verification Cadence:** Synchronous at every token presentation. The issuing authority's public key is verified at system initialization and periodically rotated.
- **Governed By:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

## 4. Attack Vectors & Mitigations

- **Token Forgery:** An attacker forges a capability token with a fake signature. Mitigated by the Ed25519 signature verification against the issuing authority's known public key.
- **Token Tampering:** An attacker modifies a valid token's scope or epoch to gain unauthorized access. Mitigated by the signature binding that covers all token fields, making any modification detectable.
- **Task ID Substitution:** An attacker substitutes the task ID in a token to apply it to a different task. Mitigated by the task ID being included in the signed payload, making substitution detectable.
- **Weak Signature Scheme:** An attacker exploits a weak signature scheme to forge tokens. Mitigated by the restriction to HMAC-SHA256 and Ed25519, both of which are considered cryptographically secure.

## 5. Dependencies & Prerequisites

- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-001|INV-AUTHZ-001]] — Root authority establishes the public key infrastructure for token signing.
- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-002|INV-AUTHZ-002]] — Epoch expiration is encoded in the signed token payload.
- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-032|INV-AUTHZ-032]] — No token replay uses nonces that are part of the signed payload.
- **Requires:** Ed25519 and HMAC-SHA256 cryptographic libraries.
- **Requires:** A secure key management system for signing keys.

## 6. Provenance & Audit Trail

- **Receipt Type:** `TOKEN_VERIFICATION_RECEIPT` — emitted for every token verification, recording the signature scheme, verification result, and bound task ID.
- **Storage Location:** `17_OBSERVABILITY` with token-ID-indexed and task-ID-indexed partitions.
- **Receipt Fields:** Token ID, signature scheme, verification result, task ID, scope, epoch, nonce, issuing authority, BLAKE3 hash.
- **Immutability:** Token verification receipts are append-only per [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-014|INV-AUTHZ-014]].

## 7. Related Invariants

- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-001|INV-AUTHZ-001]] — Root Authority Non-Transferability
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-002|INV-AUTHZ-002]] — Capability Token Epoch Expiration
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-008|INV-AUTHZ-008]] — Non-Repudiation of Tool Receipts
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-032|INV-AUTHZ-032]] — No Token Replay
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-044|INV-AUTHZ-044]] — Merkle Tree Proof Verification

## 8. Navigation & Bindings

- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
- **Control Plane Contract:** [[03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT|CONTROL_PLANE_CONTRACT]]
- **Canon Law Hierarchy:** [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- **Kernel:** [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]]
- **Observability:** [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY_MOC]]
