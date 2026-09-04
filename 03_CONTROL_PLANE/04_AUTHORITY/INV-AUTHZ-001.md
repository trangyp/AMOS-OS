---
title: INV-AUTHZ-001 — Root Authority Non-Transferability
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
  - inv-authz-001
---

# INV-AUTHZ-001 — Root Authority Non-Transferability

## 1. Formal Specification

> **Invariant Statement:**
> `Root authority originates exclusively from Origin Architect Trang Phan and cannot be delegated without a signed cryptographic receipt.`

## 2. Invariant Rule & Mathematical Formulation

Let $\mathcal{R}$ denote the root authority set, $\mathcal{D}$ the delegation graph, and $\sigma_{TP}$ the Ed25519 signature of the Origin Architect:

$$\forall r \in \mathcal{R}, \quad r = \text{TrangPhan} \implies \neg \exists d \in \mathcal{D} : \text{Transfer}(r, d) \land \neg \text{VerifySig}(\sigma_{TP}, d)$$

The root authority grant tensor $\mathbf{G}_{root}$ is a singleton bound to the Origin Architect identity:

$$\mathbf{G}_{root} = \{ (\text{TrangPhan}, \text{ROOT}, \infty) \}$$

Any delegation chain $C = (r_0, r_1, \ldots, r_n)$ must satisfy $r_0 = \text{TrangPhan}$ and each edge must carry a valid cryptographic receipt:

$$\forall i \in [1, n], \quad \text{ValidReceipt}(C[i-1], C[i]) = \text{True}$$

## 3. Enforcement & Verification

- **Evaluation Point:** Evaluated at the Control Plane gate prior to any state mutation that touches authority grants or delegation chains. Additionally checked at epoch transitions and during capability token issuance.
- **Violation Consequence:** Immediate transaction abort, error receipt emission to `17_OBSERVABILITY`, and routing to `ROLLBACK_BASIN`. The offending agent is flagged for quarantine under [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-009|INV-AUTHZ-009]].
- **Recovery Procedure:** The system reverts to the last known-good authority state snapshot. The Origin Architect must manually inspect the violation receipt and issue a signed clearance before the offending agent may resume operation.
- **Verification Cadence:** Continuous — every authority-grant mutation triggers a synchronous check. A periodic background audit also verifies the full delegation chain integrity every epoch boundary.
- **Governed By:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

## 4. Attack Vectors & Mitigations

- **Unauthorized Root Transfer:** An agent attempts to self-assign root authority by directly mutating the authority ledger. Mitigated by the Control Plane gate requiring Ed25519 signature verification from the Origin Architect for any root-level grant change.
- **Delegation Chain Forgery:** An attacker fabricates an intermediate delegation receipt to impersonate root authority. Mitigated by the cryptographic chain validation that verifies every link back to the Origin Architect's known public key.
- **Replay of Old Delegation Receipts:** A stale delegation receipt is replayed to gain unauthorized root-level access. Mitigated by epoch-bound nonces in delegation receipts, enforced by [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-002|INV-AUTHZ-002]] and [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-032|INV-AUTHZ-032]].
- **Privilege Escalation via Self-Modification:** An agent modifies its own authority tier. Prevented by [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-005|INV-AUTHZ-005]].

## 5. Dependencies & Prerequisites

- **Depends On:** [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] — the core law hierarchy establishes the primacy of root authority.
- **Depends On:** [[03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT|CONTROL_PLANE_CONTRACT]] — defines the authority delegation protocol.
- **Requires:** Ed25519 cryptographic infrastructure for signature generation and verification.
- **Requires:** The Origin Architect's public key to be provisioned in the kernel trust anchor before system initialization.

## 6. Provenance & Audit Trail

- **Receipt Type:** `AUTHORITY_GRANT_RECEIPT` — emitted for every successful root authority delegation.
- **Storage Location:** `17_OBSERVABILITY` audit ledger with BLAKE3 content-addressed storage.
- **Receipt Fields:** Origin Architect signature, delegatee identity, delegation scope, epoch boundary, nonce, BLAKE3 hash of the prior receipt in the chain.
- **Immutability:** Receipts are append-only per [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-014|INV-AUTHZ-014]] and cannot be modified per [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-020|INV-AUTHZ-020]].

## 7. Related Invariants

- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-002|INV-AUTHZ-002]] — Capability Token Epoch Expiration
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-005|INV-AUTHZ-005]] — No Self-Escalation
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-018|INV-AUTHZ-018]] — Cryptographic Token Integrity
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-032|INV-AUTHZ-032]] — No Token Replay
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-050|INV-AUTHZ-050]] — Master Stewardship Immutable Binding

## 8. Navigation & Bindings

- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
- **Control Plane Contract:** [[03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT|CONTROL_PLANE_CONTRACT]]
- **Canon Law Hierarchy:** [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- **Kernel:** [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]]
- **Observability:** [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY_MOC]]
