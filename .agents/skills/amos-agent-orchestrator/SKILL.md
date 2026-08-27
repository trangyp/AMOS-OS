---
name: amos-agent-orchestrator
description: >-
  Orchestrates, queries, and assumes roles from the 678 AMOS canonical agents in .devin/agents/.
  Use when the user asks to run an AMOS agent, execute specialized reasoning (quantum fractal math,
  logic kernel, RSCF proofs, governance, biology, finance, legal), or inspect agent capabilities.
---

# AMOS Agent Orchestrator

This skill allows Antigravity to discover, configure, and operate any of the 678 canonical AMOS agents located in `.devin/agents/`.

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
