---
title: amos-7-part-universe-canon-full-workflow
type: workflow
source: 08_WORKFLOWS
Type: Workflow
Skill: amos-7-part-universe-canon-full
Agent: amos-7-part-universe-canon-full-agent
Trigger: When canon and universe engine is needed within the canon domain, including structural coverage
  analysis, persistence function mapping, canon compliance validation, or 7-part canon testing.
Version: 1.0.0
tags:
- type/workflow
- canon/workflow
- domain/canon-universe
- rscf/source_claim
- hml/m
- epistemic/source_claim
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
domain: canon
---


# Workflow: 7 Part Universe Canon Full

## Identity

Origin architect: **Trang Phan**. Domain: workflow. Parent: none. Epistemic class: SOURCE_CLAIM. H/M/L: M.


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

- **Skill**: `amos-7-part-universe-canon-full`
- **Agent**: `amos-7-part-universe-canon-full-agent`
- **Parent workflow**: Routes via `AMOS_HOME` or parent skill workflow
- **Chain depth**: Maximum 3 workflows in sequence without orchestrator approval
- **Parallel execution**: Supported when independent capabilities are invoked

