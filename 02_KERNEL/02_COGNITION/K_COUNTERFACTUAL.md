---
title: K COUNTERFACTUAL
type: note
source: 02_KERNEL/02_COGNITION
artifact_id: AMOS-OS-K-COUNTERFACTUAL
canonical_name: K_COUNTERFACTUAL
artifact_type: kernel_counterfactual_contract
status: AMOS_MODEL
conclusion_class: AMOS_MODEL
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
plane: KERNEL
kernel_family: REASONING
domain: counterfactual-reasoning
scope: AMOS_OS
created: 2026-08-25
updated: 2026-08-25
tags:
- amos-os
- kernel
- core
- canon-group/tech-ai
- canon/model
- kernel/reasoning
- kernel/counterfactual
- kernel/causal
- kernel/epistemic
- kernel/provenance
- kernel/dependency
- kernel/scope
- kernel/regime
- kernel/sensitivity
- kernel/uncertainty
- kernel/simulation
- kernel/validation
- kernel/rscf
- rscf/claim
- rscf/provenance
- rscf/state/model
- topic/counterfactual-reasoning
aliases:
- AMOS Counterfactual Kernel - Counterfactual Kernel - K Counterfactual - K_COUNTERFACTUAL
---

# K_COUNTERFACTUAL
> **AMOS Core target:** `v4.4`
> **Origin architect / steward:** Trang Phan
> **Plane:** `02_KERNEL`
> **Status:** `AMOS_MODEL`
> **Conclusion class:** `AMOS_MODEL`
## Purpose
`K_COUNTERFACTUAL` defines the AMOS kernel contract for reasoning about alternatives to an observed, assumed, modeled, or proposed state.
Its central question is:
```text
GIVEN ACTUAL / BASELINE STATE X
WHAT WOULD FOLLOW
IF
A MATERIAL CONDITION WERE DIFFERENT?
```
Counterfactual reasoning is used for:
* causal discrimination
* competing-hypothesis testing
* sensitivity analysis
* intervention analysis
* failure analysis
* recovery planning
* decision comparison
* falsifier construction
* robustness testing
* scenario discrimination
It must never convert an imagined alternative into evidence that the alternative actually occurred.
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


# 1. Architectural Position

```text
CANON
↓
FOUNDATIONAL LOGIC
↓
META-LOGIC
↓
CAUSAL + DEPENDENCY STRUCTURE
↓
K_COUNTERFACTUAL
↓
VALIDATION / DECISION / RECOVERY
```

`K_COUNTERFACTUAL` consumes established distinctions, relations, constraints, provenance, scope, regime, and causal structure.

It does not create those facts merely by constructing a scenario.

---

# 2. Core Counterfactual Form

Let:

```text
W0 = baseline world/state
I  = intervention or altered condition
W1 = counterfactual world/state
Y  = outcome of interest
```

Then conceptually:

```text
W1 = INTERVENE(W0, I)
```

and:

```text
CF(Y | I, W0)
=
predicted Y under W1
```

This represents a model operation.

Unless independently validated:

```text
COUNTERFACTUAL_RESULT
=
MODEL
```

not observation.

---

# 3. Fundamental Firewall

```text
ACTUAL != COUNTERFACTUAL
OBSERVED != SIMULATED
POSSIBLE != ACTUAL
PLAUSIBLE != VERIFIED
PREDICTED != OBSERVED
INTERVENTION_MODEL != REAL INTERVENTION
ALTERNATIVE_HISTORY != HISTORICAL FACT
```

Therefore:

```text
"IF X HAD CHANGED, Y WOULD HAVE CHANGED"
```

requires stronger support than:

```text
"Y CHANGED AFTER X"
```

and neither follows automatically from the other.

---

# 4. Counterfactual Object

A counterfactual should conceptually carry:

```yaml
counterfactual:
  counterfactual_id:

  objective:
  question:

  baseline:
    state:
    evidence:
    provenance:
    timestamp:
    regime:
    scope:

  intervention:
    target:
    original_value:
    counterfactual_value:
    intervention_type:

  held_constant: []
  allowed_to_change: []

  causal_dependencies: []
  structural_dependencies: []

  assumptions: []

  predicted_consequences: []

  competing_counterfactuals: []

  falsifiers: []
  discriminating_tests: []

  conclusion_class:
  confidence_ceiling:
```

---

# 5. Baseline Requirement

Counterfactual analysis requires a baseline.

```text
COUNTERFACTUAL
=
BASELINE
+
CHANGE
+
PROPAGATION MODEL
```

Without a sufficiently specified baseline:

```text
COUNTERFACTUAL = UNDERDETERMINED
```

and the result should remain:

```text
UNKNOWN/GAP
```

or explicitly conditional.

---

# 6. Baseline Provenance

The baseline must distinguish:

```text
OBSERVED BASELINE
SOURCE-CLAIM BASELINE
DERIVED BASELINE
MODEL BASELINE
ASSUMED BASELINE
```

A modeled baseline cannot silently become an observed baseline.

---

# 7. Intervention Identity

Every counterfactual must identify what changed.

Conceptually:

```text
I:
X = x
→
X = x'
```

If the intervention cannot be specified clearly, causal interpretation is unsafe.

---

# 8. Minimal Intervention Principle

Prefer the smallest intervention sufficient to answer the question.

```text
MINIMAL COUNTERFACTUAL
=
CHANGE TARGET VARIABLE
+
PROPAGATE NECESSARY CONSEQUENCES
```

Do not silently redesign the entire system.

---

# 9. Ceteris Paribus Firewall

The phrase:

```text
ALL ELSE EQUAL
```

is an assumption, not a fact.

In coupled systems:

```text
CHANGE(X)
```

may necessarily imply:

```text
CHANGE(Y)
CHANGE(Z)
CHANGE(R)
```

Therefore variables may only be held constant when doing so is structurally admissible.

---

# 10. Dependency Propagation

If:

```text
X → A → B → Y
```

and the counterfactual changes `X`, AMOS must evaluate whether the change propagates through:

```text
A
B
Y
```

A counterfactual cannot alter an upstream variable while arbitrarily freezing downstream dependencies.

---

# 11. Structural Consistency

Counterfactual state `W1` must satisfy applicable invariants.

```text
VALID_COUNTERFACTUAL(W1)
IFF
CONSTRAINTS(W1) = SATISFIED
```

An internally impossible counterfactual is not a valid comparison state unless the explicit purpose is impossibility analysis.

---

# 12. Distinction Preservation

Counterfactual reasoning must preserve:

```text
ENTITY IDENTITY
VARIABLE IDENTITY
RELATION TYPE
CONSTRAINT TYPE
TEMPORAL ORDER
SCOPE
REGIME
```

Changing one variable does not authorize semantic mutation of unrelated entities.

---

# 13. Causal Firewall

Counterfactual reasoning is especially sensitive to causal overreach.

The kernel distinguishes:

```text
ASSOCIATION
CORRELATION
TEMPORAL ORDER
MECHANISM
ENABLING CONDITION
NECESSARY CONDITION
SUFFICIENT CONDITION
MEDIATION
CONFOUNDING
FEEDBACK
CAUSAL EFFECT
```

Only appropriately supported causal structure licenses strong causal counterfactual conclusions.

---

# 14. Correlation Is Insufficient

Given:

```text
CORR(X,Y) != 0
```

AMOS cannot infer:

```text
IF X HAD BEEN DIFFERENT
THEN Y WOULD HAVE BEEN DIFFERENT
```

without additional causal assumptions or evidence.

Possible alternatives include:

```text
Y → X
Z → X AND Y
SELECTION EFFECT
MEASUREMENT EFFECT
FEEDBACK
COINCIDENCE
```

---

# 15. Temporal Sequence Is Insufficient

```text
X BEFORE Y
```

does not establish:

```text
Y(X') != Y(X)
```

Temporal precedence may constrain causal possibilities, but does not independently establish counterfactual effect.

---

# 16. Structural Similarity Is Insufficient

```text
SYSTEM_A ≈ SYSTEM_B
```

does not prove:

```text
INTERVENTION_EFFECT_A
=
INTERVENTION_EFFECT_B
```

Cross-system transfer remains `MODEL` unless validated.

---

# 17. Necessary Condition Counterfactual

If evidence establishes:

```text
NECESSARY(X, Y)
```

then:

```text
NOT X
→
NOT Y
```

may be licensed within the validated applicability envelope.

But the necessary-condition claim itself must be established.

---

# 18. Sufficient Condition Counterfactual

If evidence establishes:

```text
SUFFICIENT(X, Y)
```

then under the validated assumptions:

```text
X
→
Y
```

may support an intervention prediction.

This does not imply that `X` is necessary.

---

# 19. Enabling Conditions

An enabling condition may permit an outcome without determining it.

Therefore:

```text
REMOVE ENABLEMENT
```

may block an outcome,

while:

```text
ADD ENABLEMENT
```

may still not guarantee it.

---

# 20. Confounding

Suppose:

```text
Z → X
Z → Y
```

Observed association:

```text
X ↔ Y
```

may disappear under intervention.

Counterfactual analysis must therefore test plausible confounders before treating observed association as intervention effect.

---

# 21. Mediation

For:

```text
X → M → Y
```

a counterfactual changing `X` must distinguish:

```text
TOTAL EFFECT
DIRECT EFFECT
MEDIATED EFFECT
```

when the distinction is decision-relevant.

---

# 22. Feedback

For:

```text
X → Y
Y → X
```

simple one-direction counterfactual propagation may be invalid.

Feedback systems may require iterative or dynamic modeling.

---

# 23. Counterfactual Time

Counterfactuals must specify temporal placement.

```text
INTERVENE AT t_i
```

is different from:

```text
INTERVENE AT t_j
```

because the dependency state may have changed between them.

---

# 24. Path Dependence

Where state evolution depends on history:

```text
STATE(t)
=
f(
  STATE(t-1),
  EVENTS(≤t)
)
```

changing an earlier event may alter later reachable states.

Therefore:

```text
SAME FINAL INPUTS
```

do not necessarily imply:

```text
SAME FINAL STATE
```

---

# 25. Regime Dependence

A counterfactual valid in:

```text
REGIME_A
```

must not automatically transfer to:

```text
REGIME_B
```

If the intervention itself changes the regime:

```text
I:
REGIME_A
→
REGIME_B
```

then regime-specific rules must be reevaluated.

---

# 26. Scope Inheritance

Counterfactual conclusions inherit the scope of their load-bearing premises.

Conceptually:

```text
SCOPE(CF)
⊆
INTERSECTION(
  SCOPE(BASELINE),
  SCOPE(CAUSAL_MODEL),
  SCOPE(INTERVENTION_MODEL)
)
```

unless independently validated beyond that envelope.

---

# 27. Freshness

A counterfactual built from stale baseline information may no longer represent the current system.

Therefore:

```text
CURRENT COUNTERFACTUAL
```

requires current-enough load-bearing premises for the relevant domain.

Freshness requirements are claim-specific.

---

# 28. Provenance

Counterfactual reasoning must retain provenance for:

```text
BASELINE
CAUSAL EDGES
CONSTRAINTS
PARAMETERS
ASSUMPTIONS
CALIBRATION DATA
```

Otherwise later revalidation cannot determine which counterfactual conclusions remain reusable.

---

# 29. Provenance Independence

Multiple sources supporting the same causal edge are not independent merely because they are separate documents.

```text
SOURCE_A
↓
REPORT_B
↓
ARTICLE_C
```

is one ancestry chain.

Therefore:

```text
DOCUMENT COUNT
!=
INDEPENDENT CAUSAL SUPPORT
```

---

# 30. Counterfactual Proof Capsule

Important counterfactual conclusions should conceptually carry:

```yaml
counterfactual_proof_capsule:
  claim:
  claim_class:

  baseline:
  intervention:

  load_bearing_premises: []

  causal_model:
  dependency_model:

  evidence: []
  provenance: []

  scope:
  regime:
  temporal_validity:

  held_constant: []
  propagated_changes: []

  competing_counterfactuals: []
  falsifiers: []

  sensitivity_points: []

  confidence_ceiling:
  invalidation_conditions: []

  conclusion_class:
```

---

# 31. Confidence Ceiling

A counterfactual conclusion cannot be more certain than its weakest load-bearing causal or baseline premise without independent revalidation.

Conceptually:

```text
CONFIDENCE(CF)
≤
MIN(
  BASELINE_CONFIDENCE,
  CAUSAL_CONFIDENCE,
  INTERVENTION_MODEL_CONFIDENCE,
  DEPENDENCY_CONFIDENCE
)
```

---

# 32. Counterfactual Classes

Counterfactual outputs should normally resolve to one of:

```text
DERIVED
MODEL
CONDITIONAL
COMPETING
UNKNOWN/GAP
```

`VERIFIED` requires unusually strong and appropriately typed validation.

A purely hypothetical scenario should not be labeled `VERIFIED`.

---

# 33. Competing Counterfactuals

Where causal structure is unresolved:

```text
H1:
X → Y

H2:
Z → X AND Y

H3:
Y → X
```

the intervention:

```text
DO(X = x')
```

may produce different predictions.

AMOS should preserve:

```text
CF_H1
CF_H2
CF_H3
```

rather than average them into artificial certainty.

---

# 34. No Forced Counterfactual Convergence

If multiple causal models remain viable:

```text
COUNTERFACTUAL_RESULT
=
COMPETING
```

may be the correct state.

Do not select the most narratively convenient alternative.

---

# 35. Discriminating Counterfactual Test

Prefer the cheapest test capable of distinguishing competing causal models.

Conceptually:

```text
TEST*
=
argmax_TEST
EXPECTED_DISCRIMINATION
/
COST
```

This is an architectural optimization principle, not a claim of literal runtime calculation.

---

# 36. Falsifiers

Every consequential counterfactual should identify evidence that would weaken or invalidate it.

Example:

```yaml
falsifiers:
  - intervention does not alter predicted mediator
  - outcome remains unchanged under controlled intervention
  - discovered confounder explains observed association
  - causal edge fails outside calibration sample
```

---

# 37. Sensitivity Analysis

Counterfactual reasoning should identify the smallest assumption capable of changing the result.

Conceptually:

```text
SENSITIVITY(CF)
=
MINIMUM PLAUSIBLE CHANGE
THAT FLIPS COUNTERFACTUAL CONCLUSION
```

---

# 38. Fragile Counterfactuals

If:

```text
SMALL ASSUMPTION CHANGE
→
OPPOSITE RESULT
```

then:

```text
COUNTERFACTUAL = FRAGILE
```

and should normally be classified:

```text
CONDITIONAL
```

---

# 39. Robust Counterfactuals

A counterfactual is comparatively robust when:

```text
CF RESULT
```

survives plausible variation in noncritical assumptions.

```text
ROBUST != CERTAIN
```

---

# 40. Intervention Feasibility

Counterfactual possibility and executable intervention are different.

```text
LOGICALLY CONCEIVABLE
!=
PHYSICALLY POSSIBLE
!=
OPERATIONALLY FEASIBLE
!=
AUTHORIZED
```

The kernel must preserve these distinctions.

---

# 41. Impossible Counterfactuals

A proposed intervention may violate:

```text
LOGICAL CONSTRAINT
PHYSICAL CONSTRAINT
SYSTEM INVARIANT
IDENTITY CONSTRAINT
TEMPORAL CONSTRAINT
```

If so:

```text
COUNTERFACTUAL_STATE = INADMISSIBLE
```

unless intentionally used as a boundary probe.

---

# 42. Boundary-Probe Counterfactuals

Impossible or extreme counterfactuals may still be useful for testing conceptual boundaries.

They must be labeled accordingly:

```text
BOUNDARY_MODEL
```

not realistic prediction.

---

# 43. Decision Counterfactuals

For candidate actions:

```text
A1
A2
A3
```

AMOS may construct:

```text
CF(A1)
CF(A2)
CF(A3)
```

and compare predicted outcomes.

But:

```text
BEST MODELED OUTCOME
!=
AUTHORIZED ACTION
```

Authority remains outside the counterfactual kernel.

---

# 44. Action Reversibility

Under uncertainty, counterfactual comparison should consider reversibility.

```text
ACTION_A:
high uncertainty
high reversibility

ACTION_B:
high uncertainty
low reversibility
```

may justify staged preference for `A` even when modeled expected outcomes are similar.

This is a governance-sensitive decision model, not a universal law.

---

# 45. Failure Counterfactual

For an observed failure `F`:

```text
WHAT MINIMAL CHANGE
WOULD HAVE PREVENTED F?
```

is a valid counterfactual query.

Candidate prevention factors must distinguish:

```text
NECESSARY PREVENTION
SUFFICIENT PREVENTION
RISK REDUCTION
CORRELATED CONDITION
```

---

# 46. Root-Cause Firewall

A factor whose removal would have prevented an event is not automatically the unique root cause.

Multiple sufficient causal pathways may exist.

Example:

```text
A → F
B → F
```

Removing `A` may prevent one pathway while `B` remains independently sufficient.

---

# 47. Recovery Counterfactual

Recovery reasoning may ask:

```text
IF FAILED PREMISE P
WERE REPLACED BY VALID P'
WHAT DESCENDANTS BECOME RECOVERABLE?
```

This integrates counterfactual reasoning with selective invalidation.

---

# 48. Selective Recalculation

If intervention affects only dependency subgraph `G_i`:

```text
RECOMPUTE(G_i)
```

rather than:

```text
RECOMPUTE(ENTIRE_SYSTEM)
```

provided dependency closure is established.

---

# 49. v4.4 Local Counterfactual Fast Path

Local counterfactual evaluation is admissible when:

```text
INTERVENTION TARGET IS LOCAL
AND
DEPENDENCY CLOSURE IS KNOWN
AND
PROVENANCE IS SUFFICIENT
AND
NO MATERIAL CONFLICT EXISTS
AND
SCOPE IS COMPATIBLE
AND
REGIME IS STABLE
AND
FRESHNESS IS VALID
```

Then:

```text
REASON LOCALLY
```

without global expansion.

---

# 50. Escalation Conditions

Escalate counterfactual reasoning when:

```text
DEPENDENCY CLOSURE UNKNOWN
CAUSAL STRUCTURE CONTESTED
PROVENANCE CORRELATED
REGIME SHIFT POSSIBLE
FEEDBACK EXISTS
INTERVENTION IS NONLOCAL
STALE BASELINE EXISTS
HIGH-STAKES ACTION DEPENDS ON RESULT
IRREVERSIBILITY IS HIGH
COMPETING MODELS DISAGREE
```

---

# 51. Counterfactual Branching

Branch only when alternative models can materially change the result.

```text
BASELINE
├── CF_MODEL_A
├── CF_MODEL_B
└── CF_MODEL_C
```

Equivalent branches should be merged.

---

# 52. Branch Explosion Firewall

Do not enumerate every imaginable world.

Counterfactual search should prioritize:

```text
DECISION-RELEVANT
CAUSALLY PLAUSIBLE
CONSTRAINT-SATISFYING
DISCRIMINATING
```

alternatives.

---

# 53. H/M/L Counterfactual Retrieval

Counterfactual analysis follows smallest-sufficient retrieval:

```text
H
domain-level causal structure
↓
M
subsystem dependency structure
↓
L
specific mechanism / parameter
↓
RAW EVIDENCE
only if required
```

Do not fabricate missing lower-level causal detail.

---

# 54. RSCF Integration

A counterfactual may operate over recursive RSCF structures.

Example:

```text
RSCF_A
├── RSCF_B
│   ├── RSCF_D
│   └── RSCF_E
└── RSCF_C
```

Intervening on `RSCF_D` requires tracing only materially dependent descendants.

---

# 55. Multi-RSCF Counterfactual

Some interventions are atomic across multiple RSCFs.

```text
I = {
  R1 → R1'
  R2 → R2'
  R3 → R3'
}
```

If partial intervention violates invariants:

```text
COUNTERFACTUAL APPLICATION
=
ALL
OR
NONE
```

---

# 56. Counterfactual and MVCC/CAS Concepts

Where AMOS reasoning models concurrent state evolution, a counterfactual must bind to an explicit baseline state or epoch.

Conceptually:

```text
CF
BASED_ON
STATE_VERSION = V
```

If authoritative state changes materially:

```text
V → V'
```

the counterfactual may require revalidation.

This is an architectural reasoning analogy and does not assert that every AMOS runtime literally implements MVCC/CAS.

---

# 57. Epoch Boundary

Counterfactuals spanning causal epochs must not silently assume unchanged system semantics.

```text
EPOCH_1
→
FINALITY_BOUNDARY
→
EPOCH_2
```

A hypothetical alteration in `EPOCH_1` may imply a different `EPOCH_2`.

That requires explicit propagation.

---

# 58. Finalized State Firewall

A counterfactual about finalized history does not rewrite authoritative history.

```text
COUNTERFACTUAL(HISTORY)
!=
MUTATION(HISTORY)
```

It creates an analytical branch only.

---

# 59. Simulation Firewall

A simulation may implement counterfactual propagation.

But:

```text
SIMULATED CF
!=
OBSERVED CF
```

Simulation validity depends on:

```text
MODEL VALIDITY
PARAMETER VALIDITY
BOUNDARY CONDITIONS
CALIBRATION
SCOPE
REGIME
```

---

# 60. Twin-World Interpretation

Conceptually:

```text
WORLD_ACTUAL
and
WORLD_COUNTERFACTUAL
```

share the same relevant pre-intervention history until the intervention boundary.

After intervention:

```text
WORLD_ACTUAL
≠
WORLD_COUNTERFACTUAL
```

where downstream dependencies diverge.

This is a reasoning model, not an empirical claim that alternate worlds physically exist.

---

# 61. Counterfactual Distance

Prefer minimal changes when identifying explanatory counterfactuals.

Conceptually:

```text
DISTANCE(W0, W1)
```

should be minimized subject to:

```text
TARGET_OUTCOME_CHANGED
AND
CONSTRAINTS_SATISFIED
```

This reduces arbitrary scenario mutation.

---

# 62. Nearest Admissible World

A useful explanatory counterfactual is often:

```text
W*
=
argmin_W
DISTANCE(W0, W)

subject to:

TARGET(W) != TARGET(W0)
AND
VALID(W)
```

The distance function is domain-dependent and must not be assumed universal.

---

# 63. Counterfactual Necessity Test

To test whether `X` is necessary for observed `Y`:

```text
ACTUAL:
X = 1
Y = 1

COUNTERFACTUAL:
X = 0
```

If a validated causal model predicts:

```text
Y = 0
```

this supports a necessity claim within that model and scope.

It does not automatically prove universal necessity.

---

# 64. Counterfactual Sufficiency Test

To test whether `X` is sufficient:

```text
BASELINE:
X = 0
Y = 0

INTERVENTION:
X = 1
```

If validated intervention evidence repeatedly produces:

```text
Y = 1
```

under applicable conditions, this may support sufficiency.

Scope and hidden enabling conditions remain material.

---

# 65. Overdetermination

Where:

```text
A → Y
B → Y
```

and both `A` and `B` independently suffice, changing only `A` may not change `Y`.

Therefore:

```text
CAUSE
```

and:

```text
BUT-FOR CAUSE
```

must not be silently equated.

---

# 66. Prevention vs Explanation

A condition useful for preventing an outcome is not necessarily the best historical explanation of why it occurred.

```text
PREVENTION LEVER
!=
HISTORICAL CAUSE
```

This distinction is essential for operational reasoning.

---

# 67. Counterfactual vs Forecast

```text
FORECAST:
WHAT WILL HAPPEN?

COUNTERFACTUAL:
WHAT WOULD HAPPEN IF X WERE DIFFERENT?
```

A forecast may assume no intervention.

A counterfactual explicitly modifies conditions.

---

# 68. Counterfactual vs Scenario

```text
SCENARIO
```

may describe a possible future without a formally defined baseline intervention.

A counterfactual requires explicit comparison against a baseline.

Therefore:

```text
COUNTERFACTUAL
⊂
STRUCTURED SCENARIO REASONING
```

conceptually, not necessarily as a repository type hierarchy.

---

# 69. Counterfactual vs Hypothesis

A hypothesis proposes an explanation or relationship.

A counterfactual evaluates implications under altered conditions.

```text
HYPOTHESIS:
X CAUSES Y

COUNTERFACTUAL TEST:
IF X WERE REMOVED,
WOULD Y CHANGE?
```

---

# 70. Counterfactual vs Falsifier

A counterfactual can generate a falsifier:

```text
IF H IS TRUE
AND
INTERVENTION I OCCURS
THEN
Y SHOULD CHANGE
```

Observed failure of that prediction may weaken `H`.

The strength of falsification depends on auxiliary assumptions.

---

# 71. Counterfactual vs Decision

```text
COUNTERFACTUAL:
IF ACTION A, THEN MODELED OUTCOME O

DECISION:
SELECT / REJECT ACTION A
```

These are separate objects.

Decision logic may additionally depend on:

```text
AUTHORITY
RISK
COST
VALUES
CONSTRAINTS
REVERSIBILITY
```

---

# 72. Uncertainty Vector

Counterfactual analysis should separately track:

```text
U_cf =
<
U_baseline,
U_causal,
U_model,
U_scope,
U_regime,
U_temporal,
U_provenance,
U_intervention,
U_execution
>
```

Do not collapse these dimensions when they imply different actions.

---

# 73. Counterfactual Gaps

Gaps should be classified:

```text
CRITICAL
DECISION-RELEVANT
EXPLANATORY
COSMETIC
```

Examples:

```text
UNKNOWN CAUSAL DIRECTION
→ CRITICAL

UNCERTAIN EFFECT MAGNITUDE
→ DECISION-RELEVANT

UNKNOWN SECONDARY MECHANISM
→ EXPLANATORY

MISSING LABEL
→ COSMETIC
```

depending on objective.

---

# 74. Unknown Handling

If the available structure cannot distinguish:

```text
CF_A
```

from:

```text
CF_B
```

return:

```text
COMPETING
```

or:

```text
UNKNOWN/GAP
```

Do not manufacture a single outcome.

---

# 75. Counterfactual Stop Condition

Counterfactual reasoning may stop when:

```text
CLAIM SUFFICIENCY
AND
DECISION SUFFICIENCY
AND
ACTION SUFFICIENCY
```

are reached.

It need not model every downstream possibility.

---

# 76. Anti-Fabrication Rules

```text
MISSING CAUSAL EDGE
MUST NOT
BECOME INVENTED MECHANISM

MISSING BASELINE
MUST NOT
BECOME ASSUMED FACT

MISSING PARAMETER
MUST NOT
BECOME PRECISE NUMBER

MISSING INTERVENTION EVIDENCE
MUST NOT
BECOME VERIFIED EFFECT

PLAUSIBLE ALTERNATIVE
MUST NOT
BECOME HISTORICAL FACT

MODELLED COUNTERFACTUAL
MUST NOT
BECOME OBSERVATION
```

---

# 77. Counterfactual Invariants

```text
CF-01
ACTUAL AND COUNTERFACTUAL STATES MUST REMAIN DISTINCT

CF-02
EVERY COUNTERFACTUAL REQUIRES A BASELINE

CF-03
EVERY MATERIAL INTERVENTION MUST BE EXPLICIT

CF-04
DEPENDENT CONSEQUENCES MUST BE PROPAGATED

CF-05
UNRELATED VARIABLES MUST NOT CHANGE WITHOUT JUSTIFICATION

CF-06
CAUSAL CLAIMS REQUIRE APPROPRIATE CAUSAL SUPPORT

CF-07
CORRELATION MUST NOT LICENSE STRONG COUNTERFACTUAL CAUSATION

CF-08
TEMPORAL ORDER MUST NOT LICENSE STRONG COUNTERFACTUAL CAUSATION

CF-09
STRUCTURAL SIMILARITY MUST NOT LICENSE EFFECT TRANSFER

CF-10
COUNTERFACTUALS MUST SATISFY APPLICABLE INVARIANTS

CF-11
SCOPE MUST PROPAGATE INTO COUNTERFACTUAL CONCLUSIONS

CF-12
REGIME CHANGES MUST TRIGGER REEVALUATION

CF-13
PROVENANCE MUST REMAIN ATTACHED TO LOAD-BEARING CAUSAL STRUCTURE

CF-14
CONFIDENCE MUST RESPECT THE WEAKEST LOAD-BEARING PREMISE

CF-15
COMPETING CAUSAL MODELS MUST REMAIN VISIBLE

CF-16
COUNTERFACTUAL SIMULATION MUST NOT BECOME OBSERVATION

CF-17
FINALIZED HISTORY MUST NOT BE MUTATED BY ANALYTICAL COUNTERFACTUALS

CF-18
IMPOSSIBLE INTERVENTIONS MUST BE IDENTIFIED

CF-19
LOCAL FAST PATH REQUIRES ESTABLISHED DEPENDENCY CLOSURE

CF-20
HIGH-STAKES COUNTERFACTUALS REQUIRE STRONGER VALIDATION

CF-21
COUNTERFACTUAL OUTPUT MUST NOT BECOME AUTHORITY

CF-22
UNKNOWN/GAP MUST NOT BECOME A DETERMINISTIC PREDICTION

CF-23
COUNTERFACTUAL BRANCHES MUST NOT MULTIPLY WITHOUT DECISION VALUE

CF-24
MODEL ASSUMPTIONS MUST REMAIN EXPLICIT
```

---

# 78. Failure Modes

```text
BASELINE_FABRICATION
INTERVENTION_AMBIGUITY
CAUSAL_OVERREACH
CORRELATION_AS_CAUSATION
SEQUENCE_AS_CAUSATION
SIMILARITY_AS_CAUSATION
DEPENDENCY_FREEZE
UNJUSTIFIED_CETERIS_PARIBUS
SCOPE_LEAKAGE
REGIME_LEAKAGE
STALE_BASELINE
PROVENANCE_COLLAPSE
FALSE_INDEPENDENCE
MODEL_AS_OBSERVATION
SIMULATION_AS_REALITY
ALTERNATIVE_HISTORY_AS_FACT
COUNTERFACTUAL_OVERCONFIDENCE
FORCED_MODEL_CONVERGENCE
BRANCH_EXPLOSION
IMPOSSIBLE_WORLD_ACCEPTANCE
FINALIZED_STATE_MUTATION
AUTHORITY_LEAKAGE
```

---

# 79. Validation Algorithm

Conceptually:

```python
def evaluate_counterfactual(cf, context):
    if not cf.baseline:
        return UNKNOWN_GAP

    if not baseline_supported(cf.baseline):
        return UNKNOWN_GAP

    if not intervention_explicit(cf.intervention):
        return UNKNOWN_GAP

    if not intervention_admissible(cf.intervention, context):
        return UNKNOWN_GAP

    if not causal_structure_sufficient(cf):
        return MODEL

    if not dependency_closure_known(cf):
        return CONDITIONAL

    if not scope_compatible(cf, context):
        return CONDITIONAL

    if not regime_compatible(cf, context):
        return CONDITIONAL

    if not freshness_valid(cf):
        return REVALIDATION_REQUIRED

    worlds = propagate_intervention(cf)

    if competing_models_disagree(worlds):
        return COMPETING

    if violates_invariants(worlds):
        return UNKNOWN_GAP

    return weakest_accurate_conclusion_class(worlds)
```

This is architectural pseudocode, not an assertion of deployed runtime behavior.

---

# 80. Lifecycle

```text
PLACEHOLDER
↓
AMOS_MODEL
↓
SOURCE_BOUND
↓
IMPLEMENTED
↓
TESTED
↓
VALIDATED
↓
AUTHORIZED
```

These states remain distinct.

```text
COUNTERFACTUAL MODEL
!=
IMPLEMENTED ENGINE

IMPLEMENTED ENGINE
!=
VALIDATED CAUSAL MODEL

VALIDATED MODEL
!=
AUTHORITY
```

---

# 81. Required Tests

Future verification should include:

```text
BASELINE PRESERVATION TEST
MINIMAL INTERVENTION TEST
DEPENDENCY PROPAGATION TEST
INVARIANT PRESERVATION TEST
CORRELATION FIREWALL TEST
CONFOUNDING TEST
MEDIATION TEST
FEEDBACK TEST
SCOPE FIREWALL TEST
REGIME-SHIFT TEST
STALE-BASELINE TEST
PROVENANCE-INDEPENDENCE TEST
COMPETING-MODEL TEST
SENSITIVITY TEST
IMPOSSIBLE-INTERVENTION TEST
FINALITY FIREWALL TEST
LOCAL FAST-PATH TEST
SELECTIVE RECOMPUTATION TEST
UNKNOWN-PRESERVATION TEST
```

---

# 82. Negative Tests

```text
CORRELATION
→
COUNTERFACTUAL CAUSATION
MUST FAIL

TEMPORAL SEQUENCE
→
COUNTERFACTUAL CAUSATION
MUST FAIL

SIMILARITY
→
TRANSFERRED INTERVENTION EFFECT
MUST FAIL

SIMULATION
→
OBSERVATION
MUST FAIL

COUNTERFACTUAL HISTORY
→
ACTUAL HISTORY
MUST FAIL

UNKNOWN BASELINE
→
PRECISE COUNTERFACTUAL
MUST FAIL

UNKNOWN DEPENDENCY
→
LOCAL FAST PATH
MUST FAIL

MODEL
→
AUTHORITY
MUST FAIL

IMPOSSIBLE INTERVENTION
→
NORMAL PREDICTION
MUST FAIL

COMPETING MODELS
→
FORCED SINGLE RESULT
MUST FAIL
```

---

# 83. Promotion Gate

Before promotion beyond `AMOS_MODEL`:

```text
[ ] canonical counterfactual source lineage bound
[ ] causal semantics confirmed
[ ] baseline semantics confirmed
[ ] intervention semantics confirmed
[ ] dependency propagation confirmed
[ ] scope inheritance confirmed
[ ] regime behavior confirmed
[ ] provenance requirements confirmed
[ ] confidence ceiling confirmed
[ ] competing-model handling confirmed
[ ] sensitivity handling confirmed
[ ] finality boundary confirmed
[ ] local fast-path conditions confirmed
[ ] simulation boundary confirmed
[ ] negative tests implemented
[ ] recovery integration tested
[ ] unresolved conflicts registered
```

Until then:

```text
IMPLEMENTATION_STATUS = UNKNOWN/GAP
```

---

# 84. Integrity Note

This artifact replaces an empty repository placeholder with a structured counterfactual reasoning model aligned with the AMOS v4.4 reasoning architecture.

It does **not** establish that a corresponding executable counterfactual kernel has been implemented or empirically validated.

Accordingly:

```text
DOCUMENT_CLASS = AMOS_MODEL
IMPLEMENTATION = UNKNOWN/GAP
EMPIRICAL_VALIDATION = UNKNOWN/GAP
```

---

# 85. RSCF Node

```RSCF-NODE
node_id: AMOS-OS-K-COUNTERFACTUAL
node_type: kernel_counterfactual_contract
domain: AMOS_OS_KERNEL
functional_type: CounterfactualKernel
lifecycle_stage: Architecture
claim_class: AMOS_MODEL

RSCF-RELATIONS:
  - INDEXED_BY: KERNEL_MAP

  - GOVERNED_BY: AMOS_CORE_LAWS
  - CONSTRAINED_BY: INVARIANT_REGISTRY
  - PRECEDENCE_GOVERNED_BY: LAW_HIERARCHY
  - AUTHORITY_GOVERNED_BY: AUTHORITY_CANON
  - HML_GOVERNED_BY: HML_CANON

  - PROVENANCE_GOVERNED_BY: CANON_PROVENANCE
  - LINEAGE_TRACKED_BY: SOURCE_LINEAGE
  - CONFLICTS_TRACKED_BY: CONFLICT_REGISTRY
  - EVOLUTION_TRACKED_BY: SUPERSESSION_LOG

  - LOGIC_DEPENDS_ON: K_CORE19_LOGIC
  - META_LOGIC_DEPENDS_ON: K_META_LOGIC
  - SEMANTICS_DEPEND_ON: K_DISTINCTION_RELATION_CONSTRAINT
  - PRECEDENCE_DEPENDS_ON: K_LAW_HIERARCHY

  - CAUSAL_DEPENDS_ON: README
  - DEPENDENCY_DEPENDS_ON: README
  - STATE_INTERACTS_WITH: README
  - CONCURRENCY_INTERACTS_WITH: README
  - ATOMICITY_INTERACTS_WITH: README
  - FINALITY_INTERACTS_WITH: README
  - VALIDATED_BY: README
  - RECOVERY_INTERACTS_WITH: README

  - AUTHORIZED_THROUGH: CONTROL_PLANE_MAP
  - EXECUTED_THROUGH: RUNTIME_MAP
  - KNOWLEDGE_BOUND_TO: 11_KNOWLEDGE/00_AMOS_Full_Brain_OS_Architecture
  - STATE_RECORDED_IN: AUTHORITATIVE_STATE
  - OBSERVED_BY: README
  - VERIFIED_BY: README
```

---

## Related

[[README]] ·
[[ARCHITECTURE]] ·
[[SYSTEM_MAP]] ·
[[CANON_MAP]] ·
[[AMOS_CORE_LAWS]] ·
[[INVARIANT_REGISTRY]] ·
[[LAW_HIERARCHY]] ·
[[HML_CANON]] ·
[[AUTHORITY_CANON]] ·
[[CANON_PROVENANCE]] ·
[[SOURCE_LINEAGE]] ·
[[CONFLICT_REGISTRY]] ·
[[SUPERSESSION_LOG]] ·
[[KERNEL_MAP]] ·
[[K_CORE19_LOGIC]] ·
[[K_DISTINCTION_RELATION_CONSTRAINT]] ·
[[K_LAW_HIERARCHY]] ·
[[K_META_LOGIC]] ·
README ·
README ·
README ·
README ·
README ·
README ·
README ·
README ·
README ·
README ·
[[CONTROL_PLANE_MAP]] ·
[[RUNTIME_MAP]] ·
11_KNOWLEDGE/00_AMOS_Full_Brain_OS_Architecture ·
[[AUTHORITATIVE_STATE]] ·
[[README]] ·
[[README]]

```text
```

---

00_ROOT_MOC|AMOS MOC

---
**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]]

---
**MOC:** [[02_COGNITION_MOC]]
