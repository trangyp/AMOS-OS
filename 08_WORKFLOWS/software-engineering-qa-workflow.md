---
title: software-engineering-qa-workflow
type: workflow
source: 08_WORKFLOWS
Type: Workflow
Skill: software-engineering-qa
Agent: software-engineering-qa-agent
Trigger: When repository-scale software diagnosis, repair, testing, architecture validation,
  UI/accessibility QA, API/database QA, release validation, drift detection, provenance
  tracing, claim assessment, gap escalation, or commit-time validation is needed.
Version: 1.0.0
tags:
- type/workflow
- canon/workflow
- domain/tech-engineering
- rscf/source_claim
- hml/m
- epistemic/source_claim
- amos_os
- 08-workflows-moc
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
domain: c10
---

# Workflow: Software Engineering QA

## Identity

Origin architect: **Trang Phan**. Domain: workflow. Parent: none. Epistemic class: SOURCE_CLAIM. H/M/L: M.


## Governing Repair Loop

```
reproduce -> localize -> modify minimal state -> re-run failing check
  -> broader regression checks -> package/release only after tested artifact passes
```

## Preconditions

- The `software-engineering-qa` skill exists and is loaded.
- The `software-engineering-qa-agent` agent is available and has valid content_hash.
- The query falls within the skill's declared scope and domain.
- All required vault sources (if any) are accessible.
- Epistemic class labeling is enabled (SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL).

## Steps

1. **ORIENT**: Identify the problem and confirm it matches software QA scope.
   - Classify the query against the 14 `software.*` capabilities
   - Confirm the target repository, framework, and language
   - Gate: `scope_confirmed` — problem is within software QA scope

2. **ACQUIRE**: Read repository structure, dependencies, and relevant code.
   - Parse repository identity (revision, branch, framework, lockfile, runtime)
   - Collect repository facts with epistemic class labels
   - Map dependency edges (parent, child, edge_type, load_bearing)
   - Gate: `repository_acquired` — repository identity and facts recorded

3. **DIAGNOSE**: Understand failure mechanism, design contract, location, and ecosystem.
   - Verify 4 understanding dimensions: mechanism, design_contract, location_structure, ecosystem
   - Require at least one falsifiable repair hypothesis
   - Flag knowledge gaps as `knowledge_gap:{dimension}`
   - Gate: `mechanism_understood` — all 4 dimensions confirmed, hypothesis present
   - **Failure path**: If any dimension is unknown, mark as GAP and block editing

4. **HYPOTHESIZE**: Propose falsifiable repair hypotheses with expected observations and falsifiers.
   - Each hypothesis must have: failure_mechanism, expected_observation, falsifier
   - Record affected_files and affected_symbols
   - Tag confidence with claim ceiling (max 0.95)
   - Gate: `hypothesis_falsifiable` — every hypothesis has a falsifier
   - **Failure path**: If no falsifiable hypothesis, raise GapError and fail closed

5. **PLAN**: Create bounded change boundary and QA command plan.
   - Define files_allowed, files_forbidden, symbols_allowed
   - List schema_changes and migration_required flag
   - Generate default QA plan (syntax, lint, focused-tests, regression)
   - Add frontend checks (accessibility, visual, production-build) for React/Vite/Next
   - Gate: `boundary_bounded` — files_allowed is non-empty, QA plan generated
   - **Failure path**: If files_allowed is empty, raise GapError

6. **PATCH**: Apply minimal state modification within the change boundary.
   - Modify only files in files_allowed
   - Do not touch files_forbidden
   - Record the patch as evidence
   - Gate: `patch_within_boundary` — all changes within declared boundary

7. **STATIC_CHECK**: Run syntax, typecheck, and lint checks.
   - Execute syntax/type check (timeout 120s)
   - Execute linter (timeout 180s)
   - Record exit codes, stdout/stderr hashes
   - Gate: `static_pass` — syntax, typecheck, and lint all PASS
   - **Failure path**: If static check FAIL, block progression, return to DIAGNOSE

8. **FOCUSED_TEST**: Run focused tests verifying the requested behavior.
   - Execute focused tests (timeout 300s)
   - Record check_state as PASS/FAIL/GAP/INCONCLUSIVE
   - Gate: `focused_pass` — focused tests PASS
   - **Failure path**: If focused tests FAIL, return to PATCH

9. **INTEGRATION_TEST**: Run integration tests for cross-module contracts.
   - Execute integration tests for affected module boundaries
   - Verify contract compatibility
   - Gate: `integration_pass` — integration tests PASS
   - **Failure path**: If integration FAIL, return to PATCH or DIAGNOSE

10. **ACCESSIBILITY**: Run accessibility checks (axe, keyboard, contrast, ARIA).
    - Required for React/Vite/Next frameworks
    - Check focus visibility, contrast, keyboard navigation
    - Gate: `accessibility_pass` — accessibility checks PASS
    - **Failure path**: If accessibility FAIL, flag as IMPORTANT finding

11. **VISUAL**: Run viewport screenshot tests across required widths.
    - Test widths: 1440, 1280, 1024, 768, 430, 375
    - Check: horizontal_scroll, clipping, overlap, hidden_controls, layout_jump
    - Verify component states: default, hover, focus, disabled, loading, empty, error, long-content, narrow-container
    - Gate: `visual_pass` — no viewport issues, state matrix complete
    - **Failure path**: If visual FAIL, flag as IMPORTANT; do not claim browser-perfect without screenshot evidence

12. **PERFORMANCE**: R

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

- **Skill**: ``
- **Agent**: `software-engineering-qa-agent`
- **Parent workflow**: Routes via `AMOS_HOME` or parent skill workflow
- **Chain depth**: Maximum 3 workflows in sequence without orchestrator approval
- **Parallel execution**: Supported when independent capabilities are invoked
