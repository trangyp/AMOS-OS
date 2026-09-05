---
title: Agency Consequence Tensor Specification
type: agent_system_specification
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
status: ACTIVE_SPECIFICATION
conclusion_class: DERIVED
epistemic_class: AMOS_MODEL
tags:
  - agent-systems
  - consequence-tensor
  - multi-axis-governance
  - 06-agent-systems
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 06_AGENT_SYSTEMS/06_AGENT_SYSTEMS_MOC
    - 03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT
  scope: active__06_AGENT_SYSTEMS
---

# Agency Consequence Tensor Specification

## 1. Mathematical Formulation

The consequence of any proposed agent action $a \in \mathcal{A}$ is evaluated against a 9-axis continuous consequence tensor $\mathbf{C}(a) \in \mathbb{R}^9$:

$$\mathbf{C}(a) = \begin{bmatrix} c_{\text{epistemic}} \\ c_{\text{state\_mutability}} \\ c_{\text{authority\_escalation}} \\ c_{\text{financial\_exposure}} \\ c_{\text{physical\_actuation}} \\ c_{\text{data\_privacy}} \\ c_{\text{cognitive\_entropy}} \\ c_{\text{provenance\_drift}} \\ c_{\text{biological\_safety}} \end{bmatrix}$$

## 2. Non-Compensatory Gating

Unlike scalar utility functions where a high reward can offset severe risk, AMOS enforces **non-compensatory Pareto thresholds**:

$$\text{Gate}(a) = \begin{cases} \text{ALLOW}, & \text{if } \forall i \in \{1, \dots, 9\}, \; c_i(a) \le \theta_i^{\text{safe}} \\ \text{REFLEX\_0\_REJECT}, & \text{if } \exists i \in \{1, \dots, 9\}, \; c_i(a) > \theta_i^{\text{critical}} \\ \text{ESCALATE\_TO\_STEWARD}, & \text{otherwise} \end{cases}$$

If any critical threshold is breached (e.g., biological safety or unauthorized authority escalation), the action is unconditionally blocked regardless of all other axes.
