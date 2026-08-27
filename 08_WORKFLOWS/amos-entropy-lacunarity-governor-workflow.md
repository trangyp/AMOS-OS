---
title: amos-entropy-lacunarity-governor-workflow
Type: Workflow
Skill: amos-entropy-lacunarity-governor
Agent: amos-entropy-lacunarity-governor-agent
Trigger: When information governance engine is needed within the info domain
Version: 1.0.0
tags: [note, vault]
---


# Workflow: Entropy Lacunarity Governor

## Preconditions

- The `amos-entropy-lacunarity-governor` skill exists and is loaded.
- The `amos-entropy-lacunarity-governor-agent` agent is available and has valid content_hash.
- The query falls within the skill's declared scope and domain.
- All required vault sources (if any) are accessible.
- Epistemic class labeling is enabled (SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL).

## Steps

1. **Intake**: Identify the problem and confirm it matches the Entropy Lacunarity Governor scope.
   - Classify the query against the info domain
   - Route to the appropriate capability
2. **Skill Invocation**: Load the `amos-entropy-lacunarity-governor` skill.
   - Read the skill content and validation gates
   - Identify which capability is most relevant
3. **Application**: Apply the Entropy Lacunarity Governor capability.
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

- **G1 (Intake)**: Problem confirmed within Entropy Lacunarity Governor scope.
- **G2 (Application)**: Outputs carry correct epistemic status tags.
- **G3 (Validation)**: Results pass Law of Law and epistemic class checks.
- **G4 (Output)**: Output format matches specification; provenance recorded.

## Failure Paths

- If validation fails: downgrade confidence, flag the gap, escalate — do not force-fit.
- If skill content is insufficient: mark as UNKNOWN/GAP and fail closed.

## Provenance

- **Workflow**: `amos-entropy-lacunarity-governor-workflow.md`
- **Skill**: `amos-entropy-lacunarity-governor`
- **Agent**: `amos-entropy-lacunarity-governor-agent`

---
**MOC:** [[08_WORKFLOWS_MOC]]
