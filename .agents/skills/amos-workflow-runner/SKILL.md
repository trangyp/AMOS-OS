---
name: amos-workflow-runner
description: Executes, validates, and coordinates multi-step procedures from the 200+
  AMOS workflows in .devin/workflows/. Use when the user requests multi-step AMOS
  workflows (e.g. gap closure, epistemic audit, quantum fractal synthesis, canon integration,
  verification pipelines, code refactoring).
parent_skill: amos-os-runtime-master
domain: runtime
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
version: 1.1.0
rscf_state: SOURCE_CLAIM
hml_level: M
gmef_gates:
- L0_integrity
- L1_epistemic
- L2_provenance
- L5_scope
- L7_authority
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance:
- L0
- L1
- L2
- L4
- L5
- L7
- L16
- L17
- L18
tags:
- type/skill
- canon/skill
- domain/os-runtime
- rscf/source_claim
- hml/m
- epistemic/source_claim
- amos_os
---


# AMOS Workflow Runner

## Identity

Origin architect: **Trang Phan**. Domain: runtime. Parent: amos-os-runtime-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.

## When to Use

- When the user requests multi-step AMOS workflows (gap closure, epistemic audit, quantum fractal synthesis)
- When executing canon integration, verification pipelines, or code refactoring workflows
- When coordinating sequential workflow steps with validation gates
- When parsing and executing any of the 200+ canonical workflows in .devin/workflows/

This skill allows Antigravity to parse and execute any of the 200+ canonical workflows in `.devin/workflows/`.

## Capabilities

- **workflow_discovery**: Search and list workflows by domain, trigger, or step count
- **workflow_execution**: Execute workflow steps in sequence with gate enforcement
- **workflow_validation**: Perform promotion-gate checklists and invariant checks between steps
- **workflow_failure_handling**: Activate failure paths and rollback when gates fail
- **workflow_state_tracking**: Track workflow progress, receipts, and provenance
- **workflow_binding_resolution**: Resolve workflow-to-agent and workflow-to-skill bindings

## Execution Lifecycle

1. **Trigger & Preconditions**: Verify inputs, required permissions, and prerequisites.
2. **Retrieve**: Read relevant notes from `00_ROOT/`, `01_CANON/`, `02_KERNEL/`, `03_CONTROL_PLANE/`, `11_KNOWLEDGE/`, or `25_COGNITIVE_MATRIX/`.
3. **Transform / Compute**: Execute the step-by-step instructions defined in `amos-*-workflow.md`.
4. **Validate**: Perform promotion-gate checklists, receipt logging, and invariant checks.
5. **Commit / Export**: Update vault notes, indexes, or state registries following AMOS standards.

## Examples

- **Scenario**: User says "Run the gap closure workflow"
  - **Input**: Request to execute multi-step AMOS workflow
  - **Output**: Load `amos-gap-closure-workflow.md`, execute steps in sequence with gate checks between each, return structured result with provenance and epistemic labels

- **Scenario**: User says "Execute the epistemic audit pipeline"
  - **Input**: Audit pipeline request
  - **Output**: Sequential execution of audit workflow steps, gate enforcement at each checkpoint, failure-path activation if any gate fails, final audit report with confidence ceiling

## Do not use

- For generic task execution outside AMOS workflow framework
- To create or modify workflows (use amos-workflow-builder instead)
- As a substitute for the domain skill that the workflow invokes
- Outside workflow orchestration domain reasoning
