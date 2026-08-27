---
title: amos-workflow-builder-workflow
Type: Workflow
Skill: amos-workflow-builder
Agent: amos-workflow-builder-agent
Trigger: When creating, updating, auditing, or packaging AMOS-aligned workflows with validation gates and agent bindings
Version: 1.0.0
tags: [note, vault]
---


# AMOS Workflow Builder Workflow

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
