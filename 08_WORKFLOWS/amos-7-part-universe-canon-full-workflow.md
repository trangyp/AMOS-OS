---
title: amos-7-part-universe-canon-full-workflow
Type: Workflow
Skill: amos-7-part-universe-canon-full
Agent: amos-7-part-universe-canon-full-agent
Trigger: When canon and universe engine is needed within the canon domain, including structural coverage analysis, persistence function mapping, canon compliance validation, or 7-part canon testing.
Version: 1.0.0
tags: [note, vault]
---


# Workflow: 7 Part Universe Canon Full

## Preconditions

- The bound skill exists and is loaded.
- The bound agent is available and has valid content_hash.
- The query falls within the skill's declared scope and domain.
- All required vault sources (if any) are accessible.
- Epistemic class labeling is enabled (SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL).

## Runtime

```
ORIENT -> MAP -> TEST -> CHALLENGE -> SYNTHESIZE
```

## Steps

1. **ORIENT**: Identify the target system and confirm canon scope.
   - Classify the query against the 8 `canon.*` capabilities
   - Confirm target system, scope, scale, regime, and time horizon
   - Gate: `scope_confirmed` — target and scope identified

2. **MAP**: Map the target to the seven persistence functions.
   - Map each of the 7 parts: Constraint, Flow, Structure, Enforcement, Time, Adaptation, Termination
   - For each part: record evidence, scope, mechanism, gap, confidence, epistemic_class
   - Gate: `seven_parts_mapped` — all 7 parts have state records

3. **TEST**: Test each part for evidence, scope, mechanism, and gap.
   - Verify each part has evidence, mechanism, and scope
   - Flag parts with UNKNOWN/GAP epistemic class
   - Identify missing parts
   - Gate: `parts_tested` — all parts tested for completeness

4. **CHALLENGE**: Challenge epistemic firewall.
   - Verify SOURCE_CANON != EMPIRICAL_LAW
   - Verify STRUCTURAL_MAPPING != CAUSAL_PROOF
   - Verify FORMAL_ELEGANCE != VALIDATION
   - Verify ALL_SEVEN_PRESENT != SYSTEM_TRUE
   - Verify CROSS_DOMAIN_ANALOGY != MECHANISM
   - Gate: `firewall_passed` — no epistemic firewall violations

5. **SYNTHESIZE**: Synthesize canon test result with provenance and confidence ceiling.
   - Build canon test result: all_seven_present, missing_parts, structural_validity
   - Record provenance for every claim
   - Set confidence ceiling (max 0.95)
   - Gate: `result_synthesized` — canon test result finalized

## Validation Gates

- **G1 (Scope)**: Target system and scope confirmed within canon domain.
- **G2 (Mapping)**: All 7 persistence functions mapped with state records.
- **G3 (Completeness)**: Each part tested for evidence, mechanism, and scope.
- **G4 (Firewall)**: Epistemic firewall passed — no canon promotion or overclaim.
- **G5 (Synthesis)**: Canon test result synthesized with provenance and confidence ceiling.

## Failure Paths

- **Scope failure**: If target or scope is missing, raise GapError and fail closed.
- **Mapping failure**: If parts are missing, flag as `missing_part:{name}` and mark CONDITIONAL.
- **Firewall failure**: If SOURCE_CANON is promoted to EMPIRICAL_LAW, flag violation and block.
- **Authority failure**: Write-classified operations (manage_lifecycle, escalate_gaps) require authorized_write.
- **Unknown execution**: Mark as GAP, do not fabricate to remove placeholders.

## Output

The workflow produces an `AgentResult` containing:

- `status` — VERIFIED / CONDITIONAL / UNKNOWN/GAP / REJECTED
- `capability` — the `canon.*` capability that was executed
- `summary` — human-readable summary of the canon test
- `data` — canon map, part states, missing parts, structural validity
- `gaps` — list of unresolved gap identifiers
- `warnings` — epistemic firewall reminders
- `confidence_ceiling` — maximum confidence (capped at 0.95)
- `provenance` — list of ProvenanceRef tracing to source evidence

## Provenance

- **Workflow**: `amos-7-part-universe-canon-full-workflow.md`
- **Skill**: `amos-7-part-universe-canon-full`
- **Agent**: `amos-7-part-universe-canon-full-agent`
- **Implementation**: `cosmo-brain/amos_v1_production/seven_part_universe_canon_agent.py`
- **Origin architect**: Trang Phan

---
**MOC:** [[08_WORKFLOWS_MOC]]
