---
name: amos-workflow-runner
description: >-
  Executes, validates, and coordinates multi-step procedures from the 200+ AMOS workflows in .devin/workflows/.
  Use when the user requests multi-step AMOS workflows (e.g. gap closure, epistemic audit, quantum fractal synthesis,
  canon integration, verification pipelines, code refactoring).
---

# AMOS Workflow Runner

This skill allows Antigravity to parse and execute any of the 200+ canonical workflows in `.devin/workflows/`.

## Execution Lifecycle

1. **Trigger & Preconditions**: Verify inputs, required permissions, and prerequisites.
2. **Retrieve**: Read relevant notes from `00_ROOT/`, `01_CANON/`, `02_KERNEL/`, `03_CONTROL_PLANE/`, `11_KNOWLEDGE/`, or `25_COGNITIVE_MATRIX/`.
3. **Transform / Compute**: Execute the step-by-step instructions defined in `amos-*-workflow.md`.
4. **Validate**: Perform promotion-gate checklists, receipt logging, and invariant checks.
5. **Commit / Export**: Update vault notes, indexes, or state registries following AMOS standards.
