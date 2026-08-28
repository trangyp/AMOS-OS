---
title: amos-emotion-cognition-decision-bridge-governor-workflow
type: workflow
source: 08_WORKFLOWS
Type: Workflow
Skill: amos-emotion-cognition-decision-bridge-governor
Agent: amos-emotion-cognition-decision-bridge-governor-agent
Trigger: When a decision requires both emotional state awareness from C05 (mind/behavior)
  and cognitive/technical rigor from C01 (meta-logic) or C10 (tech/engineering), or
  when routing a query based on emotional state, or when validating that emotion influence
  gating is preserved across domain boundaries, or when amos-c05-mind-behavior-master
  routes to cross-domain emotion-cognition-decision bridge governance
Version: 1.0.0
tags:
- type/workflow
- canon/workflow
- domain/os-runtime
- canon-group/tech-ai
- topic/runtime
- capability/governance
- capability/emotion
- capability/cognition
- capability/preconditions
- capability/orchestration_pattern
- capability/evaluation_gates
- capability/monitoring
- rscf/epistemic
- rscf/C-constraint
- rscf/G-relation
- rscf/B-boundary
- rscf/S-state
- rscf/type-system
- orchestration/event-driven
- sota/evaluation-gates
- sota/human-in-the-loop
- amos_os
rscf:
  state: AMOS_MODEL
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: workflow_process
---






# Workflow: Emotion-Cognition-Decision Bridge Governor

## Preconditions

- The `amos-emotion-cognition-decision-bridge-governor` skill exists and is loaded.
- The `amos-emotion-cognition-decision-bridge-governor-agent` agent is available and has valid content_hash.
- The query spans C05 (emotion/personality/behavior) and at least one of C01 (meta-logic) or C10 (tech/engineering).
- C05 Emotion Law v0 is available (5-axis emotion space, influence gating rules).
- C01 decision gates are available (G1-G4, reasoning mode governance).
- C10 core invariants are available (diagnose-before-edit, capability bounds).
- Epistemic class labeling is enabled (SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL).

## Steps

1. **Intake**: Identify the problem and confirm it matches the Emotion-Cognition-Decision Bridge Governor scope.
   - Classify the query: does it span C05 + C01 and/or C10?
   - Identify the decision being made
   - Identify the emotional context (if any)
   - Gate: `scope_confirmed` — query spans C05 + at least one of C01/C10; fail closed if intra-C05 only

2. **Emotion State Computation**: Compute or retrieve the C05 5-axis emotion state.
   - Extract emotional markers from input (TEXT_MARKER evidence)
   - Compute bounded state: care_alignment, risk_alert, curiosity_focus, respect_weighting, confidence_level ∈ [0,1]
   - If markers are missing: mark emotion state as UNKNOWN/GAP, proceed with conservative default
   - Tag emotion state as MODEL (inference from TEXT_MARKER evidence)
   - Gate: `emotion_state_computed` — 5-axis state computed or marked UNKNOWN/GAP; no fabricated state

3. **Cognitive Mode Routing**: Route to C01 cognitive mode using the emotion-to-cognition routing map.
   - Check risk_alert: if > 0.7, force CONSERVATIVE/DEFENSIVE mode (overrides all other axes)
   - Check curiosity_focus: if > 0.7, route to EXPLORATORY mode
   - Check confidence_level + risk_alert: if confidence > 0.8 AND risk < 0.3, permit EXECUTION mode
   - Check care_alignment and respect_weighting for COLLABORATIVE/DEFERENTIAL modes
   - Record routing rationale with emotion state snapshot
   - Gate: `cognitive_mode_routed` — mode selected per routing map; high risk_alert forces conservative mode

4. **Emotion Influence Gating**: Gate emotion influence when crossing from C05 into C01/C10.
   - Determine PERMITTED influences: pacing, verbosity, caution flags, routing decisions, load-awareness
   - Determine BLOCKED influences: factual content, logical structure, claims of felt experience, empirical assertions, mathematical/formal correctness, technical diagnosis, architecture decisions
   - Record the gating decision for audit
   - Gate: `influence_gated` — permitted and blocked influence lists computed; invariant enforced

5. **Decision Style Unification**: Unify C05/C01/C10 decision style orderings.
   - Apply unified ordering: integrity > safety > correctness > completeness > usefulness_within_policy > future_operability > fluency > speed
   - Check for priority inversions (e.g., speed overriding integrity → BLOCKED)
   - Apply C10's diagnose-before-edit at the integrity/safety level
   - Apply C01's mode-declared-pre-inference at the correctness level
   - Gate: `decision_style_unified` — unified ordering applied; no priority inversions detected

6. **Combined Risk Assessment**: Assess risk from all three domains.
   - C05 risk_alert: emotional risk perception
   - C01 uncertainty/risk: logical uncertainty budget
   - C10 risk gating: technical risk under uncertainty
   - Composite risk = weighted combination, confidence bounded by weakest domain
   - If any domain reports UNKNOWN/GAP risk: composite risk = UNKNOWN/GAP, proceed conservatively
   - Gate: `risk_assessed` — composite risk computed or marked UNKNOWN/GAP; conservative default if unknown

7. **Influence Violation Detection**: Detect violations of the emotion influence gating invariant.
   - Check C01/C10 outputs: does factual content correlate with emotion state beyond permitted channels?
   - Check C01/C10 outputs: does logical structure change based on emotion state?
   - Check for claims of felt experience ("fake feelings") in any output
   - Flag any violation as INFLUENCE_VIOLATION
   - Gate: `violations_checked` — no violations detected; violations flagged and output blocked if critical

8. **Decision Trace Production**: Produce unified, auditable decision trace.
   - Record C05 emotion state (5

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

- **Skill**: `amos-emotion-cognition-decision-bridge-governor`
- **Agent**: `amos-emotion-cognition-decision-bridge-governor-agent`
- **Parent workflow**: Routes via `AMOS_HOME` or parent skill workflow
- **Chain depth**: Maximum 3 workflows in sequence without orchestrator approval
- **Parallel execution**: Supported when independent capabilities are invoked

