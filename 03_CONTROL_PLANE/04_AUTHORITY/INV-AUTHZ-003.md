---
title: INV-AUTHZ-003 — Least Privilege Scope Bounding
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
  - inv-authz-003
---

# INV-AUTHZ-003 — Least Privilege Scope Bounding

## 1. Formal Specification

> **Invariant Statement:**
> `An agent cannot be granted permissions broader than the smallest RSCF sub-tree required for its task.`

## 2. Invariant Rule & Mathematical Formulation

Let $\mathcal{P}(a)$ be the permission set granted to agent $a$, $\mathcal{T}(a)$ the RSCF sub-tree required for the task assigned to $a$, and $\mathcal{U}$ the universal permission universe:

$$\forall a \in \mathcal{A}, \quad \mathcal{P}(a) \subseteq \mathcal{T}(a) \subseteq \mathcal{U}$$

The minimal-scope constraint requires that the granted permission set is exactly the task-required sub-tree, not a superset:

$$\nexists p \in \mathcal{P}(a) : p \notin \mathcal{T}(a)$$

The scope excess function is defined as:

$$\text{Excess}(a) = |\mathcal{P}(a) \setminus \mathcal{T}(a)|$$

The invariant requires:

$$\forall a \in \mathcal{A}, \quad \text{Excess}(a) = 0$$

## 3. Enforcement & Verification

- **Evaluation Point:** Evaluated at capability token issuance time, when the Control Plane computes the required RSCF sub-tree for the assigned task and compares it against the requested permission set.
- **Violation Consequence:** If the requested permissions exceed the task-required sub-tree, the token issuance is refused. A `SCOPE_EXCESS_VIOLATION` receipt is emitted to `17_OBSERVABILITY`. The agent receives a minimal-scope token instead.
- **Recovery Procedure:** The agent may request additional permissions through a separate delegation flow, which requires a new task specification and justification. No rollback is needed since the violation is caught at issuance time.
- **Verification Cadence:** Synchronous at every token issuance. A periodic audit also samples active tokens to verify that their scope still matches the current task requirements.
- **Governed By:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

## 4. Attack Vectors & Mitigations

- **Overbroad Permission Request:** An agent requests permissions beyond its task scope to prepare for lateral movement. Mitigated by the scope-excess check at token issuance, which refuses any permission not in the task-required RSCF sub-tree.
- **Task Specification Manipulation:** An agent inflates its task description to justify broader permissions. Mitigated by requiring task specifications to be signed by a delegating authority, verified per [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-001|INV-AUTHZ-001]].
- **Permission Accumulation Across Tasks:** An agent accumulates permissions from multiple completed tasks without relinquishing them. Mitigated by epoch-bound token expiration per [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-002|INV-AUTHZ-002]].
- **Scope Creep via Delegation:** A delegated agent expands its scope beyond the delegator's scope. Mitigated by the delegation attenuation requirement in the capability-bound governance kernel v4.8.

## 5. Dependencies & Prerequisites

- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-001|INV-AUTHZ-001]] — Root authority must authorize the delegation that grants permissions.
- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-002|INV-AUTHZ-002]] — Epoch expiration prevents permission accumulation.
- **Requires:** The RSCF sub-tree computation engine that maps task specifications to minimal permission sets.
- **Requires:** The capability-bound governance kernel v4.8 delegation attenuation logic.

## 6. Provenance & Audit Trail

- **Receipt Type:** `SCOPE_GRANT_RECEIPT` — emitted for every capability token issuance, recording the granted scope and the task-required scope.
- **Storage Location:** `17_OBSERVABILITY` with agent-indexed and task-indexed partitions.
- **Receipt Fields:** Agent identity, task ID, granted permission set, required RSCF sub-tree, scope-excess check result, issuing authority, epoch, BLAKE3 hash.
- **Immutability:** Receipts are append-only per [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-014|INV-AUTHZ-014]].

## 7. Related Invariants

- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-001|INV-AUTHZ-001]] — Root Authority Non-Transferability
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-002|INV-AUTHZ-002]] — Capability Token Epoch Expiration
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-005|INV-AUTHZ-005]] — No Self-Escalation
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-016|INV-AUTHZ-016]] — Strict Role Separation
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-042|INV-AUTHZ-042]] — Strict Identity Continuity

## 8. Navigation & Bindings

- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
- **Control Plane Contract:** [[03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT|CONTROL_PLANE_CONTRACT]]
- **Canon Law Hierarchy:** [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- **Kernel:** [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]]
- **Observability:** [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY_MOC]]
