---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Amos Active Inference Governor Workflow
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# Workflow: Active Inference Governor

## Identity

Origin architect: **Trang Phan**. Domain: workflow. Parent: none. Epistemic class: SOURCE_CLAIM. H/M/L: M.

## 10-Step Governed Loop

```
OBSERVE -> INFER -> COMPARE -> GENERATE -> GOVERN
  -> SELECT -> ACT_OR_OBSERVE -> MEASURE -> UPDATE -> STOP_OR_CONTINUE
```

## Preconditions

- The bound skill exists and is loaded.
- The bound agent is available and has valid content_hash `2a3ad14129e44647`.
- The query falls within the skill's declared scope and domain.
- All required vault sources (if any) are accessible.
- Epistemic class labeling is enabled (SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL).

## Steps

1. **OBSERVE**: Collect observations from the environment.

   - Record observations with epistemic class labels
   - Gate: `observations_collected` — at least one observation recorded

1. **INFER**: Update beliefs based on observations.

   - Update belief state with competing hypotheses
   - Preserve at least one competing hypothesis under uncertainty
   - Gate: `beliefs_updated` — beliefs recorded with epistemic class

1. **COMPARE**: Compute prediction error against expected state.

   - Calculate prediction error (not objective error)
   - Gate: `prediction_error_computed` — prediction error recorded

1. **GENERATE**: Generate candidate actions.

   - Include NO_ACTION as a valid candidate
   - Gate: `candidates_generated` — at least one candidate action generated

1. **GOVERN**: Evaluate governance gates.

   - Check 7 gates: ConstraintPass, AuthorityPass, SafetyPass, PolicyPass, ScopePass, EvidencePass, ReversibilityPass
   - Reject actions that fail any gate regardless of predicted benefit
   - Gate: `governance_evaluated` — all 7 gates evaluated

1. **SELECT**: Select smallest sufficient admissible action.

   - Prefer reversible information-gathering actions under uncertainty
   - NO_ACTION is a valid governed outcome
   - Gate: `action_selected` — action selected with rationale

1. **ACT_OR_OBSERVE**: Execute action or continue observing.

   - If selected action is NO_ACTION, continue observing
   - Gate: `decision_made` — ACT or OBSERVE decision recorded

1. **MEASURE**: Measure outcome and prediction error.

   - Record actual outcome vs predicted outcome
   - Gate: `outcome_measured` — outcome recorded

1. **UPDATE**: Update beliefs and model based on outcome.

   - Update belief confidences based on evidence
   - Invalidate dependent descendants if premises change
   - Gate: `model_updated` — beliefs updated with provenance

1. **STOP_OR_CONTINUE**: Decide whether to stop or continue the loop.

   - Check stop conditions: goal achieved, authority expired, safety threshold, max iterations
   - Gate: `loop_decision` — STOP or CONTINUE decision recorded

## Operations

1. **OBSERVE**: Collect observations from the environment. - Record observations with epistemic class labels - Gate: `observations_collected` — at least one observation recorded
1. **INFER**: Update beliefs based on observations. - Update belief state with competing hypotheses - Preserve at least one competing hypothesis under uncertainty - Gate: `beliefs_updated` — beliefs recorded with epistemic class
1. **COMPARE**: Compute prediction error against expected state. - Calculate prediction error (not objective error) - Gate: `prediction_error_computed` — prediction error recorded
1. **GENERATE**: Generate candidate actions. - Include NO_ACTION as a valid candidate - Gate: `candidates_generated` — at least one candidate action generated
1. **GOVERN**: Evaluate governance gates. - Check 7 gates: ConstraintPass, AuthorityPass, SafetyPass, PolicyPass, ScopePass, EvidencePass, ReversibilityPass - Reject actions that fail any gate regardless of predicted benefit - Gate: \`govern...
1. **SELECT**: Select smallest sufficient admissible action. - Prefer reversible information-gathering actions under uncertainty - NO_ACTION is a valid governed outcome - Gate: `action_selected` — action selected with rationale
1. **ACT_OR_OBSERVE**: Execute action or continue observing. - If selected action is NO_ACTION, continue observing - Gate: `decision_made` — ACT or OBSERVE decision recorded
1. **MEASURE**: Measure outcome and prediction error. - Record actual outcome vs predicted outcome - Gate: `outcome_measured` — outcome recorded
1. **UPDATE**: Update beliefs and model based on outcome. - Update belief confidences based on evidence - Invalidate dependent descendants if premises change - Gate: `model_updated` — beliefs updated with provenance
1. **STOP_OR_CONTINUE**: Decide whether to stop or continue the loop. - Check stop conditions: goal achieved, authority expired, safety threshold, max iterations - Gate: `loop_decision` — STOP or CONTINUE decision recorded

## Validation Gates

- **G1 (Observations)**: At least one observation collected with epistemic class.
- **G2 (Beliefs)**: Beliefs updated with competing hypotheses preserved under uncertainty.
- **G3 (Governance)**: All 7 governance gates evaluated; failed gates block action.
- **G4 (Selection)**: Smallest sufficient admissible action selected; NO_ACTION is valid.
- **G5 (Epistemic Firewall)**: ACTIVE_INFERENCE_MODEL != BIOLOGICAL_PROOF, PREDICTION_ERROR != OBJECTIVE_ERROR.
- **G6 (Authority)**: Write-classified operations require authorized_write.
- **G7 (Provenance)**: All beliefs and actions trace to provenance.

## Failure Paths

- **No observations**: Flag as GAP, block inference loop.
- **Governance failure**: Reject action if any gate fails, regardless of predicted benefit.
- **Epistemic overreach**: If AMOS_MODEL is asserted as BIOLOGICAL_PROOF, flag and block.
- **Confirmation loop**: If CONFIRMATION_LOOP drift detected, FREEZE and preserve competing hypotheses.
- **Authority failure**: Write-classified operations without authority raise AuthorizationError.
- **Endless loop**: If ENDLESS_LOOP drift detected, force STOP decision.
- **Unknown execution**: Mark as GAP, do not fabricate to remove placeholders.

## Output

The workflow produces an `AgentResult` containing:

- `status` — VERIFIED / CONDITIONAL / COMPETING / UNKNOWN/GAP / REJECTED
- `capability` — the `c05.*` capability that was executed
- `summary` — human-readable summary of the loop execution
- `data` — phases, selected action, governance gates, belief state
- `gaps` — list of unresolved gap identifiers
- `warnings` — epistemic firewall reminders
- `confidence_ceiling` — maximum confidence (capped at 0.95)
- `provenance` — list of ProvenanceRef tracing to source evidence

## Authority

- **Bound skill**: `amos-active-inference-governor`
- **Bound agent**: `amos-active-inference-governor-agent`
- **Skill path**: `.devin/skills/amos-active-inference-governor/SKILL.md`
- **Agent path**: \`.devin/agents/amos-active-inferen

______________________________________________________________________

**MOC:** [[26_WORKFLOWS/26_WORKFLOWS_MOC|26_WORKFLOWS_MOC]]

## Orchestration Pattern

**Pattern**: Single-Agent with Validation Gates

This workflow follows a single-agent orchestration with explicit validation gates between steps:

1. **Intake** -> validation gate -> **Skill Invocation** -> validation gate -> **Application** -> validation gate -> **Output**
1. Each gate checks: epistemic labeling, provenance, scope compliance, confidence ceiling
1. On gate failure: route to error handling or escalate to parent workflow

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

| Error Type       | Detection                    | Recovery                              |
| ---------------- | ---------------------------- | ------------------------------------- |
| Scope violation  | Gate 1 check                 | Route to parent skill                 |
| Missing evidence | Gate 3 check                 | Flag as GAP, reduce confidence to 0.5 |
| Contradiction    | Gate 3 check                 | Flag as CRITICAL_GAP, halt            |
| Provenance loss  | Gate 3 check                 | Mark as UNKNOWN, request human review |
| Timeout          | Step budget exceeded         | Return partial result with warnings   |
| Drift            | Confidence calibration check | Trigger drift alignment governor      |

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

- **Skill**: `amos-active-inference-governor`
- **Agent**: `amos-active-inference-governor-agent`
- **Parent workflow**: Routes via `AMOS_HOME` or parent skill workflow
- **Chain depth**: Maximum 3 workflows in sequence without orchestrator approval
- **Parallel execution**: Supported when independent capabilities are invoked
