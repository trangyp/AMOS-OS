---
title: amos-mark-operator-rscf-engine-workflow
type: workflow
source: 08_WORKFLOWS
Type: Workflow
Skill: amos-mark-operator-rscf-engine
Agent: amos-mark-operator-rscf-engine-agent
Trigger: When runtime and os engine is needed within the runtime domain
Version: 1.0.0
tags:
- type/workflow
- canon/workflow
- domain/os-runtime
- canon-group/tech-ai
- topic/runtime
- capability/workflow
- capability/preconditions
- capability/output
- capability/failure_paths
- capability/provenance
- rscf/epistemic
- rscf/T-topology
- rscf/C-constraint
- rscf/G-relation
- rscf/D-distinction
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







# Workflow: Mark Operator Rscf Engine

## Preconditions

- The `amos-mark-operator-rscf-engine` skill exists and is loaded.
- The `amos-mark-operator-rscf-engine-agent` agent is available and has valid content_hash.
- The query falls within the skill's declared scope and domain.
- All required vault sources (if any) are accessible.
- Epistemic class labeling is enabled (SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL).

## Steps

1. **Intake**: Identify the problem and confirm it matches the Mark Operator Rscf Engine scope.
   - Classify the query against the runtime domain
   - Route to the appropriate capability
2. **Skill Invocation**: Load the `amos-mark-operator-rscf-engine` skill.
   - Read the skill content and validation gates
   - Identify which capability is most relevant
3. **Application**: Apply the Mark Operator Rscf Engine capability.
   - Tag every output with its epistemic status (SOURCE / DERIVED / AMOS_MODEL)
   - Record provenance for every derived claim
4. **Validation**: Check results against validation gates.
   - Law of Law: no unresolved contradictions
   - Epistemic class labels present
   - Provenance recorded
5. **Output**: Present results with full provenance and epistemic labeling.
   - Include confidence ceiling
   - Record source path for every derived claim


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

- **G1 (Intake)**: Problem confirmed within Mark Operator Rscf Engine scope.
- **G2 (Application)**: Outputs carry correct epistemic status tags.
- **G3 (Validation)**: Results pass Law of Law and epistemic class checks.
- **G4 (Output)**: Output format matches specification; provenance recorded.

## Failure Paths

- If validation fails: downgrade confidence, flag the gap, escalate — do not force-fit.
- If skill content is insufficient: mark as UNKNOWN/GAP and fail closed.

## Provenance

- **Workflow**: `amos-mark-operator-rscf-engine-workflow.md`
- **Skill**: `amos-mark-operator-rscf-engine`
- **Agent**: `amos-mark-operator-rscf-engine-agent`

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

- **Skill**: `amos-mark-operator-rscf-engine`
- **Agent**: `amos-mark-operator-rscf-engine-agent`
- **Parent workflow**: Routes via `AMOS_HOME` or parent skill workflow
- **Chain depth**: Maximum 3 workflows in sequence without orchestrator approval
- **Parallel execution**: Supported when independent capabilities are invoked

