---
title: Agent Delegation Lifecycle Specification
type: agent_system_specification
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
status: ACTIVE_SPECIFICATION
conclusion_class: DERIVED
epistemic_class: AMOS_MODEL
tags:
  - agent-systems
  - delegation-lifecycle
  - capability-attenuation
  - 06-agent-systems
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 06_AGENT_SYSTEMS/06_AGENT_SYSTEMS_MOC
    - 03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT
  scope: active__06_AGENT_SYSTEMS
---

# Agent Delegation Lifecycle Specification

## 1. Lifecycle State Machine

Every agent instance within AMOS OS strictly transitions through a finite, deterministic 6-state lifecycle:

$$\mathcal{S}_{\text{lifecycle}} \in \{\text{PROPOSED}, \text{ADMITTED}, \text{ACTIVE}, \text{DELEGATING}, \text{REVOKED}, \text{ARCHIVED}\}$$

```mermaid
stateDiagram-v2
    [*] --> PROPOSED: Admission Proposal
    PROPOSED --> ADMITTED: Schema & Invariant Gate Pass
    ADMITTED --> ACTIVE: Execution Dispatch
    ACTIVE --> DELEGATING: Spawn Child Subagent
    DELEGATING --> ACTIVE: Subagent Loop Closure
    ACTIVE --> REVOKED: Invariant Violation / Timeout
    ACTIVE --> ARCHIVED: Task Completion & Receipt Emission
    REVOKED --> ARCHIVED: Quarantined Archival
    ARCHIVED --> [*]
```

## 2. Invariant: Strict Monotonic Capability Attenuation

When an agent $\mathcal{A}_{\text{parent}}$ delegates a subtask to $\mathcal{A}_{\text{child}}$, the child's capability envelope $\mathcal{C}(\mathcal{A}_{\text{child}})$ and authority token $\Phi(\mathcal{A}_{\text{child}})$ must be a strictly bounded sub-algebra of the parent:

$$\mathcal{C}(\mathcal{A}_{\text{child}}, t) \subseteq \mathcal{C}(\mathcal{A}_{\text{parent}}, t) \quad \text{and} \quad \tau_{\text{expiry}}(\mathcal{A}_{\text{child}}) \le \tau_{\text{expiry}}(\mathcal{A}_{\text{parent}})$$

$$\text{CAPABILITY} \neq \text{AUTHORITY} \neq \text{AGENCY} \neq \text{CONSEQUENCE}$$

No child agent can inherit or generate permissions exceeding its immediate progenitor.
