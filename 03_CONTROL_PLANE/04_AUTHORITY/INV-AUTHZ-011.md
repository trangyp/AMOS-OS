---
title: "INV-AUTHZ-011 — Sandboxed Execution Confinement"
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
  - inv-authz-011
---

# INV-AUTHZ-011 — Sandboxed Execution Confinement

## 1. Formal Specification

> **Invariant Statement:**
> `Tier 2 and Tier 3 tools must execute inside isolated ephemeral environments with strict memory and CPU caps.`

## 2. Invariant Rule & Mathematical Formulation

Let $\text{Tier}(t)$ denote the risk tier of tool $t$, and $\text{Env}(t)$ the execution environment of tool $t$:

$$\forall t \in \mathcal{T}, \quad \text{Tier}(t) \in \{2, 3\} \implies \text{Isolated}(\text{Env}(t)) \land \text{Ephemeral}(\text{Env}(t))$$

The resource cap constraints are:

$$\text{Mem}(\text{Env}(t)) \le M_{\max}(\text{Tier}(t)) \quad \land \quad \text{CPU}(\text{Env}(t)) \le C_{\max}(\text{Tier}(t))$$

where $M_{\max}(2) = 512\text{MB}$, $M_{\max}(3) = 256\text{MB}$, $C_{\max}(2) = 2\text{vCPU}$, $C_{\max}(3) = 1\text{vCPU}$.

The ephemeral property requires environment destruction after execution:

$$\text{Complete}(t) \implies \text{Destroy}(\text{Env}(t)) \land \neg \text{Persist}(\text{Env}(t))$$

The isolation property requires no shared filesystem or memory with the host:

$$\text{Isolated}(\text{Env}(t)) \iff \text{Namespace}(\text{Env}(t)) \neq \text{Namespace}(\text{Host}) \land \text{NoSharedMem}(\text{Env}(t), \text{Host})$$

## 3. Enforcement & Verification

- **Evaluation Point:** Evaluated at the Control Plane gate when a Tier 2 or Tier 3 tool is dispatched. The gate verifies that an isolated ephemeral environment has been provisioned with the correct resource caps.
- **Violation Consequence:** If a Tier 2/3 tool is dispatched without sandbox confinement, the execution is refused. A `SANDBOX_VIOLATION` receipt is emitted to `17_OBSERVABILITY`. The tool's capability token is flagged.
- **Recovery Procedure:** The tool must be re-dispatched with a properly provisioned sandbox environment. The provisioning is automatic through the runtime layer.
- **Verification Cadence:** Synchronous at tool dispatch. Continuous monitoring of resource usage during execution to detect cap violations. Post-execution verification that the environment was destroyed.
- **Governed By:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

## 4. Attack Vectors & Mitigations

- **Sandbox Escape:** A tool exploits a vulnerability in the isolation layer to access host resources. Mitigated by using hardware-backed isolation (gVisor/Firecracker class) and by the ephemeral environment being destroyed after execution.
- **Resource Cap Bypass:** A tool exceeds its memory or CPU caps by exploiting cgroup misconfiguration. Mitigated by continuous resource monitoring during execution and immediate termination on cap exceedance.
- **Persistent Environment Reuse:** A tool's sandbox environment is not destroyed after execution, allowing subsequent tools to access residual state. Mitigated by the post-execution destruction verification and the ephemeral property enforcement.
- **Inter-Sandbox Communication:** Two sandboxed tools communicate through a shared channel to coordinate an attack. Mitigated by network namespace isolation that prevents inter-sandbox communication unless explicitly authorized.

## 5. Dependencies & Prerequisites

- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-008|INV-AUTHZ-008]] — Non-repudiation of tool receipts ensures sandboxed executions are properly recorded.
- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-040|INV-AUTHZ-040]] — Resource exhaustion failsafe prevents sandbox resource caps from being exceeded by system-wide pressure.
- **Requires:** A container or microVM orchestration system (gVisor, Firecracker, or equivalent).
- **Requires:** cgroup or equivalent resource control mechanism for memory and CPU caps.

## 6. Provenance & Audit Trail

- **Receipt Type:** `SANDBOX_PROVISIONING_RECEIPT` — emitted for every sandboxed tool execution, recording the environment configuration, resource caps, and destruction verification.
- **Storage Location:** `17_OBSERVABILITY` with tool-ID-indexed and tier-indexed partitions.
- **Receipt Fields:** Tool ID, tier, environment ID, memory cap, CPU cap, isolation type, provisioning timestamp, destruction timestamp, resource usage summary, BLAKE3 hash.
- **Immutability:** Sandbox receipts are append-only per [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-014|INV-AUTHZ-014]].

## 7. Related Invariants

- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-008|INV-AUTHZ-008]] — Non-Repudiation of Tool Receipts
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-013|INV-AUTHZ-013]] — Anti-Poisoning Invariant
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-037|INV-AUTHZ-037]] — Zero Unchecked Autonomous Action
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-040|INV-AUTHZ-040]] — Resource Exhaustion Failsafe
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-042|INV-AUTHZ-042]] — Strict Identity Continuity

## 8. Navigation & Bindings

- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
- **Control Plane Contract:** [[03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT|CONTROL_PLANE_CONTRACT]]
- **Canon Law Hierarchy:** [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- **Kernel:** [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]]
- **Observability:** [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY_MOC]]
