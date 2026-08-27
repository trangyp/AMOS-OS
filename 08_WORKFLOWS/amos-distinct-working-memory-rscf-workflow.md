---
title: amos-distinct-working-memory-rscf-workflow
Type: Workflow
Skill: amos-distinct-working-memory-rscf
Agent: amos-distinct-working-memory-rscf-agent
Trigger: When memory system engine is needed within the memory domain
Version: 1.0.0
tags: [note, vault]
---


# Workflow: Distinct Working Memory Rscf

## Preconditions

- The `amos-distinct-working-memory-rscf` skill exists and is loaded.
- The `amos-distinct-working-memory-rscf-agent` agent is available and has valid content_hash.
- The query falls within the skill's declared scope and domain.
- All required vault sources (if any) are accessible.
- Epistemic class labeling is enabled (SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL).

## Steps

1. **Intake**: Identify the problem and confirm it matches the Distinct Working Memory Rscf scope.
   - Classify the query against the memory domain
   - Route to the appropriate capability
2. **Skill Invocation**: Load the `amos-distinct-working-memory-rscf` skill.
   - Read the skill content and validation gates
   - Identify which capability is most relevant
3. **Application**: Apply the Distinct Working Memory Rscf capability.
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

- **G1 (Intake)**: Problem confirmed within Distinct Working Memory Rscf scope.
- **G2 (Application)**: Outputs carry correct epistemic status tags.
- **G3 (Validation)**: Results pass Law of Law and epistemic class checks.
- **G4 (Output)**: Output format matches specification; provenance recorded.

## Failure Paths

- If validation fails: downgrade confidence, flag the gap, escalate — do not force-fit.
- If skill content is insufficient: mark as UNKNOWN/GAP and fail closed.

## Provenance

- **Workflow**: `amos-distinct-working-memory-rscf-workflow.md`
- **Skill**: `amos-distinct-working-memory-rscf`
- **Agent**: `amos-distinct-working-memory-rscf-agent`

---
**MOC:** [[08_WORKFLOWS_MOC]]
