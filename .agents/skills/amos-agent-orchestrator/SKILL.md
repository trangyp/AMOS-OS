---
name: amos-agent-orchestrator
description: >-
  Orchestrates, queries, and assumes roles from the 678 AMOS canonical agents in .devin/agents/.
  Use when the user asks to run an AMOS agent, execute specialized reasoning (quantum fractal math,
  logic kernel, RSCF proofs, governance, biology, finance, legal), or inspect agent capabilities.
parent_skill: amos-agent-systems-master
domain: agent
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
version: "1.1.0"
rscf_state: SOURCE_CLAIM
hml_level: M
gmef_gates: [L0_integrity, L1_epistemic, L2_provenance, L5_scope, L7_authority]
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance: [L0, L1, L2, L4, L5, L7, L16, L17, L18]
---

# AMOS Agent Orchestrator

## Identity

Origin architect: **Trang Phan**. Domain: agent. Parent: amos-agent-systems-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.

## When to Use

- When the user asks to run or invoke a specific AMOS agent
- When specialized reasoning is needed (quantum fractal math, logic kernel, RSCF proofs, governance, biology, finance, legal)
- When inspecting agent capabilities, bindings, or system routing
- When discovering which agent handles a particular task type

## Capabilities

- **agent_discovery**: Search and list agents by system, role, or capability
- **agent_inspection**: Load and display agent JSON structure, capabilities, and bindings
- **agent_role_assumption**: Adopt an agent's role for task execution
- **agent_capability_check**: Verify agent capabilities match task requirements
- **agent_workflow_binding**: Map agents to their bound workflows and skills
- **agent_system_routing**: Route requests to the correct system (BRAIN, EXECUTION, MONEY, LEGAL, LIFE, SENSE, WORLD_MODEL, GOVERNANCE)

## Agent Architecture

All canonical AMOS agents are defined as JSON structures with:
- `system`: One of BRAIN_SYSTEM, EXECUTION_SYSTEM, MONEY_SYSTEM, LEGAL_SYSTEM, LIFE_SYSTEM, SENSE_SYSTEM, WORLD_MODEL_SYSTEM, GOVERNANCE_SYSTEM.
- `role`: Canonical role definition.
- `capabilities`: Explicit input/output contracts.
- `operations`: Entry point, protocol, scope, exclusions.
- `integrity_requirements`: Normative constraints.
- `depends_on_skills` and `depends_on_workflows`.

## Workflow

1. **Locate the Agent**: Search `.devin/agents/` for `amos-{name}-agent.json` or check `.devin/agents/amos-agent-registry-index.md`.
2. **Load Specifications**: Read the agent JSON to inspect its entry point, invariants, and declared workflows.
3. **Execute Matching Workflow**: Check `.devin/workflows/amos-{name}-workflow.md` to perform the exact multi-step protocol.
4. **Enforce Epistemic Gates**: Ensure `PROPOSAL != COMMIT` and `MODEL != OBSERVATION`.

## Examples

- **Scenario**: User says "Run the quantum fractal math agent"
  - **Input**: Request to execute specialized reasoning
  - **Output**: Load `amos-quantum-fractal-math-engine-agent.json`, verify capabilities, execute matching workflow, return results with epistemic labels

- **Scenario**: User says "What agents do we have for governance?"
  - **Input**: Agent discovery query
  - **Output**: List governance-domain agents (amos-ethics-os-governor, amos-trust-formation-governor, amos-risk-constraint-governor) with their capabilities and bound workflows

## Do not use

- For generic agent fabrication (use amos-agent-systems-master instead)
- To modify agent JSON structures (use amos-skill-builder or manual editing)
- As a substitute for executing the actual domain skill
- Outside agent systems domain reasoning
