---
title: INV-AUTHZ-016 — Strict Role Separation
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
  - inv-authz-016
---

# INV-AUTHZ-016 — Strict Role Separation

## 1. Formal Specification

> **Invariant Statement:**
> `An agent assigned as an Auditor cannot execute worker tasks within the same transaction.`

## 2. Invariant Rule & Mathematical Formulation

Let $\text{Role}(a, T)$ be the role of agent $a$ in transaction $T$, and $\mathcal{R}_{\text{audit}}, \mathcal{R}_{\text{worker}}$ the audit and worker role sets:

$$\forall a \in \mathcal{A}, \forall T \in \mathcal{T}, \quad \text{Role}(a, T) = \text{AUDITOR} \implies \text{Role}(a, T) \neq \text{WORKER}$$

The role separation is enforced per transaction, not just per epoch:

$$\forall T, \quad \text{Roles}(T) \cap \mathcal{R}_{\text{audit}} \cap \mathcal{R}_{\text{worker}} = \emptyset$$

The mutual exclusion constraint on agent-role assignments:

$$\forall a, \forall T, \quad |\text{Roles}(a, T) \cap (\mathcal{R}_{\text{audit}} \cup \mathcal{R}_{\text{worker}})| \le 1$$

An agent may switch roles across transactions but never hold both simultaneously:

$$\text{Role}(a, T_1) = \text{AUDITOR} \land \text{Role}(a, T_2) = \text{WORKER} \implies T_1 \neq T_2$$

## 3. Enforcement & Verification

- **Evaluation Point:** Evaluated at the Control Plane gate when an agent is assigned a role within a transaction. The gate checks that the agent does not already hold a conflicting role in the same transaction.
- **Violation Consequence:** If an agent attempts to hold both auditor and worker roles in the same transaction, the role assignment is refused. A `ROLE_SEPARATION_VIOLATION` receipt is emitted to `17_OBSERVABILITY`.
- **Recovery Procedure:** The transaction must be restructured with separate agents for audit and worker roles. Alternatively, the agent may be reassigned to a single role for the transaction.
- **Verification Cadence:** Synchronous at every role assignment. A periodic audit verifies that no transaction has agents holding conflicting roles.
- **Governed By:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

## 4. Attack Vectors & Mitigations

- **Dual-Role Exploitation:** An agent assigned as auditor also executes worker tasks, allowing it to audit its own work and suppress findings. Mitigated by the strict role separation check that prevents dual-role assignment within a transaction.
- **Role Switching Mid-Transaction:** An agent switches from auditor to worker (or vice versa) during a transaction to exploit both roles. Mitigated by the per-transaction role binding that prevents mid-transaction role changes.
- **Shadow Role Assumption:** An agent informally assumes a second role without formal assignment. Mitigated by the Control Plane only recognizing formally assigned roles for authorization decisions.
- **Collusion via Role Sharing:** Two agents share role information to coordinate audit evasion. Mitigated by [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-042|INV-AUTHZ-042]] identity continuity and by audit trail review.

## 5. Dependencies & Prerequisites

- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-003|INV-AUTHZ-003]] — Least privilege scope bounding ensures agents are only assigned roles within their task scope.
- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-005|INV-AUTHZ-005]] — No self-escalation prevents agents from self-assigning conflicting roles.
- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-042|INV-AUTHZ-042]] — Strict identity continuity prevents role impersonation.
- **Requires:** A role assignment registry with per-transaction role tracking.
- **Requires:** A mutual exclusion enforcement mechanism for conflicting roles.

## 6. Provenance & Audit Trail

- **Receipt Type:** `ROLE_ASSIGNMENT_RECEIPT` — emitted for every role assignment within a transaction, recording the agent, role, transaction ID, and separation check result.
- **Storage Location:** `17_OBSERVABILITY` with transaction-ID-indexed and agent-indexed partitions.
- **Receipt Fields:** Agent identity, assigned role, transaction ID, separation check result, assigning authority, epoch, BLAKE3 hash.
- **Immutability:** Role assignment receipts are append-only per [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-014|INV-AUTHZ-014]].

## 7. Related Invariants

- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-003|INV-AUTHZ-003]] — Least Privilege Scope Bounding
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-005|INV-AUTHZ-005]] — No Self-Escalation
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-006|INV-AUTHZ-006]] — Multi-Party Authorization for Canon
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-042|INV-AUTHZ-042]] — Strict Identity Continuity
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-050|INV-AUTHZ-050]] — Master Stewardship Immutable Binding

## 8. Navigation & Bindings

- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
- **Control Plane Contract:** [[03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT|CONTROL_PLANE_CONTRACT]]
- **Canon Law Hierarchy:** [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- **Kernel:** [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]]
- **Observability:** [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY_MOC]]
