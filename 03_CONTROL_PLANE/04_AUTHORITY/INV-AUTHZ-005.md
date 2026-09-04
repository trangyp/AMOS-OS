---
title: "INV-AUTHZ-005 — No Self-Escalation"
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
  - inv-authz-005
---

# INV-AUTHZ-005 — No Self-Escalation

## 1. Formal Specification

> **Invariant Statement:**
> `An agent process cannot alter its own capability grant tensor or privilege tier.`

## 2. Invariant Rule & Mathematical Formulation

Let $\text{Agent}(a)$ denote the identity of agent $a$, $\text{Grant}(a)$ the capability grant tensor of $a$, and $\text{Tier}(a)$ the privilege tier of $a$:

$$\forall a \in \mathcal{A}, \quad \text{Actor}(\text{Mutate}(\text{Grant}(a))) \neq \text{Agent}(a)$$

$$\forall a \in \mathcal{A}, \quad \text{Actor}(\text{Mutate}(\text{Tier}(a))) \neq \text{Agent}(a)$$

The self-mutation prohibition extends to transitive self-delegation:

$$\nexists C = (a_0, a_1, \ldots, a_n) : a_0 = a_n \land \text{Mutate}(\text{Grant}(a_0)) \in C$$

The grant tensor mutation requires an external authority $b \neq a$:

$$\text{ValidMutation}(\text{Grant}(a), b) \iff b \neq a \land \text{HasAuthority}(b, \text{GRANT_MODIFY})$$

## 3. Enforcement & Verification

- **Evaluation Point:** Evaluated at the Control Plane gate whenever a capability grant tensor or privilege tier mutation is requested. The actor identity is compared against the target agent identity.
- **Violation Consequence:** If the actor and target are the same agent, the mutation is immediately refused. A `SELF_ESCALATION_VIOLATION` receipt is emitted to `17_OBSERVABILITY`. The agent is flagged for quarantine under [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-009|INV-AUTHZ-009]].
- **Recovery Procedure:** The agent must request privilege changes through the standard delegation flow, which requires an external authority to approve and execute the grant modification.
- **Verification Cadence:** Synchronous at every grant or tier mutation. A periodic audit also checks for indirect self-escalation attempts through delegation chains.
- **Governed By:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

## 4. Attack Vectors & Mitigations

- **Direct Self-Modification:** An agent directly writes to its own capability grant tensor in the authority ledger. Mitigated by the actor-identity check at the Control Plane gate, which rejects any mutation where actor equals target.
- **Indirect Self-Escalation via Delegation Cycle:** An agent delegates to a second agent, which then delegates elevated permissions back to the first. Mitigated by the transitive self-delegation check that detects cycles in the delegation graph.
- **Privilege Tier Bypass:** An agent modifies its tier classification to gain access to restricted operations. Mitigated by the tier mutation requiring external authority, same as grant tensor mutations.
- **Grant Tensor Shadow Copy:** An agent creates a local copy of its grant tensor and modifies it, then presents the modified copy for authorization. Mitigated by the Control Plane only accepting grant tensors from the authoritative authority ledger, not from agent-supplied copies.

## 5. Dependencies & Prerequisites

- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-001|INV-AUTHZ-001]] — Root authority must be established for any external authority to have grant-modification power.
- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-003|INV-AUTHZ-003]] — Least privilege ensures agents cannot have grant-modification authority over themselves.
- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-042|INV-AUTHZ-042]] — Identity continuity ensures agents cannot impersonate another agent to bypass the self-escalation check.
- **Requires:** A reliable actor-identity mechanism that cannot be spoofed by the acting agent.

## 6. Provenance & Audit Trail

- **Receipt Type:** `GRANT_MUTATION_RECEIPT` — emitted for every successful grant tensor or tier mutation, recording the actor and target identities.
- **Storage Location:** `17_OBSERVABILITY` with actor-indexed and target-indexed partitions.
- **Receipt Fields:** Actor identity, target identity, mutation type (grant or tier), old value, new value, authorizing authority, epoch, BLAKE3 hash.
- **Immutability:** Mutation receipts are append-only per [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-014|INV-AUTHZ-014]].

## 7. Related Invariants

- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-001|INV-AUTHZ-001]] — Root Authority Non-Transferability
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-003|INV-AUTHZ-003]] — Least Privilege Scope Bounding
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-009|INV-AUTHZ-009]] — Quarantine on Anomaly
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-016|INV-AUTHZ-016]] — Strict Role Separation
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-042|INV-AUTHZ-042]] — Strict Identity Continuity

## 8. Navigation & Bindings

- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
- **Control Plane Contract:** [[03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT|CONTROL_PLANE_CONTRACT]]
- **Canon Law Hierarchy:** [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- **Kernel:** [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]]
- **Observability:** [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY_MOC]]
