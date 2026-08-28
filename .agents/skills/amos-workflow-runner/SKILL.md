---
name: amos-workflow-runner
description: >-
  Executes, validates, and coordinates multi-step procedures from the 200+ AMOS workflows in .devin/workflows/.
  Use when the user requests multi-step AMOS workflows (e.g. gap closure, epistemic audit, quantum fractal synthesis,
  canon integration, verification pipelines, code refactoring).
---

# AMOS Workflow Runner

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
