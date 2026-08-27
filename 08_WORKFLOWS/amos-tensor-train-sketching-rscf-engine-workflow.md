---
title: amos-tensor-train-sketching-rscf-engine-workflow
Type: Workflow
Skill: amos-tensor-train-sketching-rscf-engine
Agent: amos-tensor-train-sketching-rscf-engine-agent
Trigger: When runtime and os engine is needed within the runtime domain
Version: 1.0.0
tags: [note, vault]
---


# Workflow: Tensor Train Sketching Rscf Engine

## Preconditions

- The `amos-tensor-train-sketching-rscf-engine` skill exists and is loaded.
- The `amos-tensor-train-sketching-rscf-engine-agent` agent is available and has valid content_hash.
- The query falls within the skill's declared scope and domain.
- All required vault sources (if any) are accessible.
- Epistemic class labeling is enabled (SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL).

## Steps

1. **Intake**: Identify the problem and confirm it matches the Tensor Train Sketching Rscf Engine scope.
   - Classify the query against the runtime domain
   - Route to the appropriate capability
2. **Skill Invocation**: Load the `amos-tensor-train-sketching-rscf-engine` skill.
   - Read the skill content and validation gates
   - Identify which capability is most relevant
3. **Application**: Apply the Tensor Train Sketching Rscf Engine capability.
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

- **G1 (Intake)**: Problem confirmed within Tensor Train Sketching Rscf Engine scope.
- **G2 (Application)**: Outputs carry correct epistemic status tags.
- **G3 (Validation)**: Results pass Law of Law and epistemic class checks.
- **G4 (Output)**: Output format matches specification; provenance recorded.

## Failure Paths

- If validation fails: downgrade confidence, flag the gap, escalate — do not force-fit.
- If skill content is insufficient: mark as UNKNOWN/GAP and fail closed.

## Provenance

- **Workflow**: `amos-tensor-train-sketching-rscf-engine-workflow.md`
- **Skill**: `amos-tensor-train-sketching-rscf-engine`
- **Agent**: `amos-tensor-train-sketching-rscf-engine-agent`

---
**MOC:** [[08_WORKFLOWS_MOC]]
