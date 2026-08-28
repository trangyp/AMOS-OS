---
title: amos-vietnamese-global-cultural-bridge-governor-workflow
type: workflow
source: 08_WORKFLOWS
Type: Workflow
Skill: amos-vietnamese-global-cultural-bridge-governor
Agent: amos-vietnamese-global-cultural-bridge-governor-agent
Trigger: When bridging Vietnamese-specific cultural analysis with global sociological frameworks, or when
  validating that global models apply to Vietnamese contexts, or when translating Vietnamese-specific
  insights for global comparison, or when detecting cultural context mismatch between Vietnamese and global
  claims, or when amos-c06-society-culture-master routes to cross-domain Vietnamese-global cultural bridge
  governance
Version: 1.0.0
tags:
- type/workflow
- canon/workflow
- domain/cross-domain
- rscf/source_claim
- hml/m
- epistemic/source_claim
- amos_os
rscf:
  state: AMOS_MODEL
  claim_class: AMOS_MODEL
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

# Workflow: Vietnamese-Global Cultural Bridge Governor

## Identity

Origin architect: **Trang Phan**. Domain: workflow. Parent: none. Epistemic class: SOURCE_CLAIM. H/M/L: M.


## Preconditions

- The `amos-vietnamese-global-cultural-bridge-governor` skill exists and is loaded.
- The `amos-vietnamese-global-cultural-bridge-governor-agent` agent is available and has valid content_hash.
- The query involves at least one direction of the Vietnamese-global cultural bridge.
- C06 F07 (Vietnam Regional Systems) knowledge is available.
- C06 F01-F06, F08-F10 (global frameworks) are available.
- Epistemic class labeling is enabled.

## Steps

1. **Intake** (`vgc_bridge.manage_lifecycle`): Identify the problem and confirm it matches the Vietnamese-Global Cultural Bridge Governor scope.
   - Classify the query: which bridge direction is needed?
     - VN_TO_GLOBAL: translate Vietnamese-specific claims to global framework terms
     - GLOBAL_TO_VN: validate global model for Vietnamese context
     - COMPARE: compare Vietnamese and global cultural systems
     - GOVERN: full bidirectional bridge governance
     - DETECT_DRIFT: cultural drift detection
   - **Gate G1**: scope_confirmed — query involves at least one bridge direction

2. **Bridge Transition Execution** (`vgc_bridge.translate_vietnamese_to_global`, `vgc_bridge.validate_global_for_vietnamese`): Execute the requested bridge transition.
   - VN_TO_GLOBAL: map Vietnamese concepts to global sociological categories
   - GLOBAL_TO_VN: check for cultural context mismatch, missing Vietnamese variables
   - COMPARE: identify structural similarities, differences, incommensurable elements
   - GOVERN: execute all transitions in sequence
   - DETECT_DRIFT: check for Vietnamese context changes and global model changes
   - Tag every output with epistemic status (CONDITIONAL for VN-specific, MODEL for global)
   - **Gate G2**: transition_executed — transition completed or marked UNKNOWN/GAP

3. **Cultural Specificity Validation** (`vgc_bridge.govern_bridge`): Validate that cultural specificity is preserved.
   - Check G7: Vietnamese cultural specificity preserved during translation
   - Check G8: no universalization of Vietnamese-specific claims without evidence
   - Flag any flattening as CULTURAL_FLATTENING
   - Flag any universalization as UNIVERSALIZATION_RISK
   - **Gate G3**: cultural_validated — no violations; violations flagged and transition blocked if critical

4. **Provenance Chain Tracing** (`vgc_bridge.trace_cultural_provenance`): Trace the full provenance chain across the bridge.
   - Record Vietnamese source path, cultural context, epistemic class
   - Record global framework mapping, translation step, epistemic class
   - Record any UNKNOWN/GAP markers from source domains
   - **Gate G4**: provenance_traced — full provenance chain recorded in both directions

5. **Cultural Drift Detection** (`vgc_bridge.detect_cultural_drift`, `vgc_bridge.detect_drift`): Detect cultural drift between Vietnamese and global models.
   - Check: Vietnamese context changes not reflected in global mappings
   - Check: global model changes that invalidate Vietnamese applications
   - Flag any drift as CULTURAL_DRIFT
   - **Gate G5**: drift_checked — no drift detected; drift flagged and bridge blocked if critical

6. **Cultural Claim Assessment** (`vgc_bridge.assess_cultural_claim`): Assess cultural claim for epistemic class and universalization risk.
   - Verify: Vietnamese-specific claims are CONDITIONAL on Vietnamese context
   - Verify: global claims are MODEL unless independently validated
   - Verify: cultural ritual energy equations (gia hệ) are MODEL/structural metaphor
   - Block if universalization risk is detected
   - **Gate G6**: claim_assessed — claim assessment completed

7. **Bridge Governance** (`vgc_bridge.compare_cultural_systems`): Govern the full bidirectional bridge if GOVERN was requested.
   - Verify all transitions completed successfully
   - Verify cultural specificity preserved
   - Verify provenance chain unbroken in both directions
   - Verify no cultural drift detected
   - Verify claim assessment passed
   - Return BRIDGE_PERMITTED / BRIDGE_BLOCKED / BRIDGE_CONDITIONAL
   - **Gate G7**: bridge_governed — bridge verdict returned with justification

8. **Validation** (`vgc_bridge.validate_outputs`): Check results against all 10 validation gates (G1-G10).
   - G1: No contradictions across Vietnamese-global bridge
   - G2: All claims labeled (CONDITIONAL for VN-specific, MODEL for global)
   - G3: Pr

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

- **Skill**: `amos-vietnamese-global-cultural-bridge-governor`
- **Agent**: `amos-vietnamese-global-cultural-bridge-governor-agent`
- **Parent workflow**: Routes via `AMOS_HOME` or parent skill workflow
- **Chain depth**: Maximum 3 workflows in sequence without orchestrator approval
- **Parallel execution**: Supported when independent capabilities are invoked
