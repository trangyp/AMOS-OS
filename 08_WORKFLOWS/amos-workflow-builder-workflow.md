---
title: amos-workflow-builder-workflow
type: workflow
source: 08_WORKFLOWS
Type: Workflow
Skill: amos-workflow-builder
Agent: amos-workflow-builder-agent
Trigger: When creating, updating, auditing, or packaging AMOS-aligned workflows with
  validation gates and agent bindings
Version: 1.0.0
tags:
- type/workflow
- canon/workflow
- domain/os-runtime
- canon-group/tech-ai
- topic/runtime
- capability/workflow
- capability/preconditions
- capability/phases
- capability/output
- capability/failure_paths
- capability/orchestration_pattern
- rscf/epistemic
- rscf/T-topology
- rscf/C-constraint
- rscf/G-relation
- rscf/type-system
- orchestration/event-driven
- sota/evaluation-gates
- sota/human-in-the-loop
- amos_os
rscf:
  state: AMOS_MODEL
  claim_class: EMPIRICAL
  provenance: AMOS_corpus
  scope: workflow_process
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
---







# AMOS Workflow Builder Workflow

## Identity

Origin architect: **Trang Phan**. Domain: workflow. Parent: none. Epistemic class: SOURCE_CLAIM. H/M/L: M.


## Preconditions

- The `amos-workflow-builder` skill exists and is loaded.
- The `amos-workflow-builder-agent` agent is available and has valid content_hash.
- The query falls within the skill's declared scope and domain.
- All required vault sources (if any) are accessible.
- Epistemic class labeling is enabled (SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL).

## Phases

### Phase 1: ORIENT
- **Gate**: skill_loaded
- Load the amos-workflow-builder skill and its content
- Classify the query against workflow builder sub-capabilities
- Confirm domain, scope, and binding

### Phase 2: GAP
- **Gate**: domain_confirmed
- Identify the workflow gap or requirement
- Classify gap type: missing workflow, broken workflow, incomplete workflow
- Assess severity and urgency

### Phase 3: SOURCE
- **Gate**: epistemic_labeled
- Gather source material from skill content, vault, and existing workflows
- Label all sources with epistemic class (SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL)
- Record provenance for every source

### Phase 4: ARCHITECT
- **Gate**: gates_passed
- Design workflow step sequence with validation gates
- Define 1:1:1 binding (workflow -> agent -> skill)
- Specify failure paths and fail-closed conditions
- Apply G1-G10 hard gates

### Phase 5: BUILD
- **Gate**: output_validated
- Generate workflow content with steps, gates, and bindings
- Validate against frontmatter, binding, steps, gates, failure paths, provenance
- Package with provenance and confidence ceiling
- Present results with epistemic labels


## Output

The workflow produces a structured result containing:

- `status` — VERIFIED / DERIVED / CONDITIONAL / UNKNOWN/GAP / REJECTED
- `capability` — the capability that was executed
- `summary` — human-readable summary of the result
- `data` — structured output specific to the capability
- `gaps` — list of unresolved gap identifiers
- `warnings` — non-blocking advisory messages
- `confidence_ceiling` — maximum confidence (capped at 0.95)
- `provenance` — list of provenance references tracing to source evidence

## Validation Gates
- G1: Frontmatter complete and valid
- G2: Agent and skill bindings exist (1:1:1)
- G3: Steps are ordered and non-empty
- G4: Every step has a validation gate
- G5: Failure paths defined for every step
- G6: Provenance recorded for all derived content
- G7: Epistemic class labels on all claims
- G8: Scope matches declared domain
- G9: No unresolved contradictions
- G10: Package is complete and installable

## Failure Paths

- If validation fails: downgrade confidence, flag the gap, escalate — do not force-fit.
- If skill content is insufficient: mark as UNKNOWN/GAP and fail closed.
- If 1:1:1 binding is broken: flag routing mismatch, block workflow creation.
- If failure paths are missing from target workflow: block validation, require explicit failure paths.
- If authority witness is stale or missing: block write-classified capabilities, fail closed.

---
**MOC:** [[08_WORKFLOWS_MOC]]

## Orchestration Pattern

**Pattern**: Single-Agent with Validation Gates

This workflow follows a single-agent orchestration with explicit validation gates between steps:
1. **Intake** -> validation gate -> **Skill Invocation** -> validation gate -> **Application** -> validation gate -> **Output**
2. Each gate checks: epistemic labeling, provenance, scope compliance, confidence ceiling
3. On gate failure: route to error handling or escalate to parent workflow


## Evaluation Gates

### Gate 1: Intake Validation
- Query matches skill scope
- Required inputs present
- No scope violations detected

### Gate 2: Skill Load Validation
- Skill file exists and is valid
- Agent binding is valid
- Required vault sources accessible

### Gate 3: Output Validation
- Epistemic class labels present
- Provenance recorded for all derived claims
- Confidence ceiling not exceeded
- No unresolved CRITICAL_GAPs
- Scope compliance verified


## Error Handling

| Error Type | Detection | Recovery |
|---|---|---|
| Scope violation | Gate 1 check | Route to parent skill |
| Missing evidence | Gate 3 check | Flag as GAP, reduce confidence to 0.5 |
| Contradiction | Gate 3 check | Flag as CRITICAL_GAP, halt |
| Provenance loss | Gate 3 check | Mark as UNKNOWN, request human review |
| Timeout | Step budget exceeded | Return partial result with warnings |
| Drift | Confidence calibration check | Trigger drift alignment governor |


## Human-in-the-Loop

- **Default**: Automated execution without human intervention
- **Escalation triggers**:
  - CRITICAL_GAP detected
  - Confidence below 0.3
  - Scope violation requiring reclassification
  - Contradiction that cannot be auto-resolved
- **Review checkpoint**: After Gate 3, if any warnings are present


## Monitoring

- **Trace level**: Full (inputs, outputs, intermediate steps)
- **Metrics**: Step count, token usage, confidence, gap count, execution time
- **Alerts**: CRITICAL_GAP, confidence < 0.3, scope violation, timeout
- **Provenance**: Every output traces back to source evidence via provenance chain


## Composition

- **Skill**: `amos-workflow-builder`
- **Agent**: `amos-workflow-builder-agent`
- **Parent workflow**: Routes via `AMOS_HOME` or parent skill workflow
- **Chain depth**: Maximum 3 workflows in sequence without orchestrator approval
- **Parallel execution**: Supported when independent capabilities are invoked

