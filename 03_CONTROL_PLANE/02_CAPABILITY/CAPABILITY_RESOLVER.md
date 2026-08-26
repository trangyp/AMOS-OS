Yes. Below is the **complete paste-ready file**, with the placeholder removed and the status kept at `CANDIDATE_CANON` rather than falsely asserting implementation or final canon. The Drive corpus contains both a dedicated historical counterfactual kernel file and a larger Meta-Cognition version, so the artifact preserves that historical lineage rather than treating the placeholder as the source.  

---
artifact_id: AMOS-OS-K-COUNTERFACTUAL
canonical_name: K_COUNTERFACTUAL
title: K COUNTERFACTUAL

artifact_class: KERNEL
kernel_family: META_COGNITION
plane: KERNEL
canonical_location: 02_KERNEL/K_COUNTERFACTUAL.md

origin_architect: Trang Phan
steward: Trang Phan

amos_core_target: v4.4

status: CANDIDATE_CANON
conclusion_class: DERIVED

historical_kernel:
  id: Counterfactual_Reasoning_Kernel
  historical_version: "1.0.0"
  historical_category: Meta_Cognition
  historical_priority: 9
  historical_required: true

supersedes:
  - K_COUNTERFACTUAL_PLACEHOLDER

promotion_required: true
implementation_status: UNKNOWN/GAP
formal_verification_status: UNKNOWN/GAP
empirical_validation_status: UNKNOWN/GAP

updated: 2026-08-26
---

# K COUNTERFACTUAL

> **Status:** `CANDIDATE_CANON`
>
> **Conclusion class:** `DERIVED`
>
> **AMOS_CORE target:** `v4.4`
>
> **Origin architect:** Trang Phan
>
> **Supersedes:** `K_COUNTERFACTUAL_PLACEHOLDER`

---

# 0. PURPOSE

`K_COUNTERFACTUAL` is the AMOS OS kernel for disciplined reasoning over
alternative worlds.

Its purpose is to construct, evaluate, compare, challenge, and govern
counterfactual states while preserving:

- factual anchoring;
- explicit intervention semantics;
- minimal-change discipline;
- causal-chain conservation;
- causal-model integrity;
- uncertainty;
- assumption transparency;
- competing hypotheses;
- provenance;
- scope;
- regime;
- temporal validity;
- dependency closure;
- falsifiability;
- sensitivity;
- reversibility;
- action governance.

The kernel answers questions of the form:

- What would have happened if X had been different?
- What might happen if X changes?
- Would Y still have occurred without X?
- Would introducing X be sufficient for Y?
- What changes if a structural assumption changes?
- Which intervention could alter Y?
- Which causal explanation best survives counterfactual testing?
- Which premise carries the result?
- What observation would distinguish competing counterfactual models?

`K_COUNTERFACTUAL` does not create facts about unrealized worlds.

It creates explicitly typed reasoning artifacts about them.

---

# 1. CANONICAL EPISTEMIC BOUNDARY

The following distinctions are hard boundaries:

```text
COUNTERFACTUAL != FACT

HYPOTHETICAL != OBSERVED

MODEL != OBSERVATION

SOURCE_CLAIM != VERIFIED FACT

ASSOCIATION != CAUSATION

CORRELATION != CAUSATION

TEMPORAL ORDER != CAUSATION

PREDICTION != INTERVENTION

INTERVENTION != COUNTERFACTUAL

SIMULATION != EMPIRICAL VALIDATION

PLAUSIBILITY != PROBABILITY

PROBABILITY != CERTAINTY

STRUCTURAL SIMILARITY != CAUSAL EQUIVALENCE

MULTIPLE DERIVATIONS != INDEPENDENT EVIDENCE
```

A counterfactual output must therefore remain typed as:

```text
MODEL

DERIVED

CONDITIONAL

COMPETING

or

UNKNOWN/GAP
```

unless independent evidence licenses a stronger classification.

---

# 2. HISTORICAL KERNEL SPINE

The historical AMOS counterfactual lineage defines four principal
counterfactual classes:

```text
PAST

FUTURE

STRUCTURAL

CAUSAL
```

The historical validity spine contains:

```text
PLAUSIBLE INITIAL STATE

MINIMAL CHANGE

CAUSAL CHAIN CONSERVATION

UNCERTAINTY PROPORTIONAL TO DISTANCE

ASSUMPTION TRANSPARENCY
```

These principles remain load-bearing in the v4.4 integration.

---

# 3. COUNTERFACTUAL TYPES

## 3.1 PAST COUNTERFACTUAL

Question:

```text
What would have happened if a past event,
decision, condition, or variable had been different?
```

Canonical structure:

```yaml
PastCounterfactual:
  factual_history:
  divergence_time:
  intervention:
  preserved_history:
  affected_dependencies:
  recomputed_history:
  queried_outcome:
  assumptions:
  uncertainty:
```

Default law:

```text
HISTORY BEFORE THE DECLARED DIVERGENCE
REMAINS FACTUAL
UNLESS THE COUNTERFACTUAL EXPLICITLY
INTERVENES EARLIER.
```

---

## 3.2 FUTURE COUNTERFACTUAL

Question:

```text
What could happen if a future intervention occurs?
```

Canonical structure:

```yaml
FutureCounterfactual:
  current_state:
  intervention:
  intervention_time:
  horizon:
  causal_model:
  response_model:
  scenarios:
  uncertainty:
  early_warning_signals:
```

A future counterfactual is not automatically a forecast.

---

## 3.3 STRUCTURAL COUNTERFACTUAL

Question:

```text
What would the system do if its structure,
constraint, mechanism, topology, or operating
condition were different?
```

Canonical structure:

```yaml
StructuralCounterfactual:
  factual_structure:
  structural_intervention:
  preserved_mechanisms:
  modified_mechanisms:
  constraints:
  thresholds:
  feedback:
  regime:
  resulting_structure:
```

Structural interventions receive a higher validation burden because they can
invalidate wide dependency closures.

---

## 3.4 CAUSAL COUNTERFACTUAL

Question:

```text
Would the outcome have been different
under another intervention?
```

Canonical structure:

```yaml
CausalCounterfactual:
  factual_cause:
  factual_outcome:
  alternative_intervention:
  counterfactual_outcome:
  causal_model:
  confounders:
  mediators:
  moderators:
  competing_explanations:
  attribution_confidence:
```

---

# 4. FUNDAMENTAL COUNTERFACTUAL OBJECT

Define:

CF = <F, I, M, E, C, Q, S, R, T, P, U, A>

where:

```text
F = factual anchor
I = intervention
M = causal / structural model
E = evidence
C = counterfactual world
Q = queried outcome
S = scope
R = regime
T = temporal envelope
P = provenance topology
U = uncertainty
A = assumptions
```

A consequential counterfactual is valid only to the extent that its
load-bearing components are:

```text
KNOWN

MODELED EXPLICITLY

or

MARKED UNKNOWN/GAP
```

Missing causal structure must never be silently bridged with fluent prose.

---

# 5. FACTUAL ANCHOR

Every counterfactual begins from a factual or explicitly assumed baseline.

```yaml
FactualAnchor:

  anchor_id:

  system:

  entity:

  population:

  environment:

  observed_state: {}

  observations: []

  source_claims: []

  derived_state: []

  temporal:
    observed_at:
    valid_from:
    valid_until:

  scope:

  regime:

  measurement_method:

  provenance: []

  uncertainty:

  contradictions: []
```

Hard law:

```text
NO FACTUAL ANCHOR
→
NO DECISION-GRADE COUNTERFACTUAL
```

---

# 6. ACTUAL / COUNTERFACTUAL SEPARATION

Counterfactual reasoning branches from actuality.

```text
W0 — ACTUAL WORLD
│
├── CF1
├── CF2
├── CF3
└── CFn
```

It must never overwrite actuality:

```text
ACTUAL
↓
COUNTERFACTUAL
↓
COUNTERFACTUAL STORED AS FACT
```

is invalid.

Invariant:

```text
THE FACTUAL PARENT MUST REMAIN RECOVERABLE.
```

---

# 7. INTERVENTION

An intervention is an explicit alteration of the factual or modeled world.

```yaml
Intervention:

  intervention_id:

  type:
    - VALUE_CHANGE
    - ACTION_ADDITION
    - ACTION_REMOVAL
    - ACTION_SUBSTITUTION
    - TIMING_CHANGE
    - ORDER_CHANGE
    - INFORMATION_CHANGE
    - BELIEF_CHANGE
    - POLICY_CHANGE
    - RESOURCE_CHANGE
    - PARAMETER_CHANGE
    - STRUCTURAL_CHANGE
    - ENVIRONMENT_CHANGE
    - CONSTRAINT_CHANGE
    - EVENT_INJECTION
    - EVENT_REMOVAL

  target:

  factual_value:

  counterfactual_value:

  intervention_time:

  duration:

  magnitude:

  scope:

  explicit_auxiliary_changes: []

  assumptions: []
```

---

# 8. INTERVENTION BINDING

A counterfactual intervention should bind, when material:

```text
TARGET

ORIGINAL VALUE

ALTERNATIVE VALUE

MAGNITUDE

TIME

DURATION

SCOPE

ENVIRONMENT

REGIME
```

Example:

```text
"What if investment increased?"
```

may remain underspecified if the answer depends on:

```text
how much?

what investment?

when?

for how long?

funded how?

what else changes?
```

If missing intervention parameters can flip the result:

```text
CONCLUSION = CONDITIONAL
```

or:

```text
UNKNOWN/GAP
```

---

# 9. MINIMAL CHANGE PRINCIPLE

The intervention must alter only:

```text
1. explicitly intervened variables;

2. explicitly declared auxiliary variables;

3. consequences licensed by the causal model.
```

Define:

Changed(CF)

as all variables differing from actuality.

Then:

```text
Changed(CF)
⊆
Intervention
∪
LicensedDescendants
∪
ExplicitAuxiliaryChanges
```

by default.

Any unexplained alteration is:

```text
E_CF_HIDDEN_CHANGE
```

---

# 10. MINIMAL SURGERY

For structural equations:

```text
Vi = fi(PAi, Ui)
```

an intervention:

```text
do(X = x')
```

conceptually replaces the generating mechanism for X with:

```text
X := x'
```

while preserving unaffected mechanisms.

Thus:

```text
M = {f1 ... fX ... fn}
```

becomes:

```text
MI = {f1 ... X:=x' ... fn}
```

unless additional structural changes are explicitly declared.

This is a formalization of the minimal-change principle, not a claim that all
AMOS implementations literally execute SCM code.

---

# 11. HIDDEN CO-INTERVENTION

Suppose the declared intervention is:

```text
X := x'
```

but generated world state also changes:

```text
Z := z'
```

The change in Z must be classified as:

```text
CAUSALLY_ENTAILED

SYSTEM_REACTION

EXPLICIT_AUXILIARY_INTERVENTION

or

HIDDEN_CHANGE
```

`HIDDEN_CHANGE` is invalid.

---

# 12. CAUSAL MODEL

```yaml
CausalModel:

  model_id:

  version:

  causal_epoch:

  nodes: []

  edges:
    - source:
      target:
      relation_type:
      evidence:
      provenance:
      scope:
      regime:
      freshness:
      confidence:
      falsifier:

  exogenous_variables: []

  endogenous_variables: []

  assumptions: []

  validity_envelope:

  competing_models: []
```

---

# 13. CAUSAL RELATION TYPES

AMOS must distinguish:

```text
ASSOCIATION

CORRELATION

TEMPORAL_PRECEDENCE

MECHANISM

ENABLEMENT

NECESSITY

SUFFICIENCY

MEDIATION

MODERATION

CONFOUNDING

FEEDBACK

CAUSAL_EFFECT
```

They are not interchangeable.

---

# 14. CAUSAL FIREWALL

Forbidden transformations include:

```text
A occurs before B
→
A caused B
```

```text
A correlates with B
→
changing A changes B
```

```text
A resembles C
→
A and C have the same causal effect
```

```text
model predicts Y
→
Y would certainly occur
```

```text
source claims X caused Y
→
causal relation verified
```

A causal bridge requires appropriately typed evidence.

---

# 15. ASSOCIATIONAL / INTERVENTIONAL / COUNTERFACTUAL LEVELS

Observational:

```text
P(Y | X=x)
```

Interventional:

```text
P(Y | do(X=x))
```

Counterfactual:

```text
P(Yx' | X=x, Y=y, E=e)
```

These answer different questions.

AMOS must not silently substitute one for another.

---

# 16. ABDUCTION

Given evidence:

```text
E = e
```

infer plausible latent/background state:

```text
P(U | E=e, M)
```

where probabilistic semantics are justified.

If several latent states remain possible:

```text
U1
U2
U3
```

all decision-relevant alternatives must be preserved.

---

# 17. ACTION

Apply the intervention:

```text
MI = Intervene(M, I)
```

Only explicitly licensed intervention semantics may modify the causal model.

---

# 18. PROJECTION

Propagate the modified model to obtain the counterfactual outcome.

Conceptually:

```text
YCF = Predict(MI, U)
```

or:

```text
P(YCF)
=
ΣU P(YCF | U, MI) P(U | E)
```

when probability is justified.

Without justified probability semantics, preserve:

```text
possible outcomes

ordering

bounds

or

UNKNOWN
```

rather than inventing numerical probability.

---

# 19. CORE RUNTIME

```text
FACTUAL STATE
      ↓
ABDUCTION
      ↓
BACKGROUND / LATENT STATE
      ↓
INTERVENTION
      ↓
MODIFIED MODEL
      ↓
CAUSAL PROPAGATION
      ↓
SYSTEM REACTION
      ↓
COUNTERFACTUAL STATE
      ↓
UNCERTAINTY
      ↓
ADVERSARIAL VALIDATION
      ↓
CONCLUSION
```

---

# 20. CAUSAL CHAIN CONSERVATION

If:

```text
A → B → C
```

and A changes, the default propagation is:

```text
A'
↓
B'
↓
C'
```

not:

```text
A'
────────→ C'
```

unless an independent direct path is established.

This prevents causal-chain skipping.

---

# 21. DEPENDENCY CLOSURE

For intervention X and queried outcome Y, define:

```text
Closure(X,Y)
```

as the smallest set of load-bearing variables, mechanisms, premises, and
evidence needed to evaluate X's effect on Y.

Example:

```text
X → A → B → Y
```

requires:

```text
X
A
B
Y
```

but not unrelated:

```text
Z
```

when Z is independently established as irrelevant.

---

# 22. CAUSAL CLOSURE FAILURE

If:

```text
X → ? → Y
```

contains a load-bearing unknown mechanism:

```text
DO NOT INVENT THE MISSING EDGE.
```

Return:

```text
UNKNOWN/GAP
```

or, where an explicit assumption is useful:

```text
CONDITIONAL
```

---

# 23. CONFOUNDING

Pattern:

```text
Z → X
Z → Y
```

can produce:

```text
X ↔ Y
```

without:

```text
X → Y
```

Counterfactual causal inference therefore tracks:

```yaml
confounding:
  known: []
  suspected: []
  unresolved: []
  ruled_out: []
```

Unresolved material confounding limits causal confidence.

---

# 24. MEDIATION

For:

```text
X → M → Y
```

changing X may change M and therefore Y.

The following are different counterfactuals:

```text
change X and allow M to respond
```

versus:

```text
change X while holding M fixed
```

AMOS must preserve this distinction.

---

# 25. MODERATION

If the effect of X on Y depends on Z:

```text
Effect(X → Y | Z=z1)
!=
Effect(X → Y | Z=z2)
```

the result is conditional on Z.

---

# 26. NECESSITY

Question:

```text
Would Y have occurred without X?
```

A candidate test compares:

```text
Yx
```

with:

```text
Yx'
```

where x' removes or changes X.

Necessity is always model-, scope-, and regime-bounded.

---

# 27. SUFFICIENCY

Question:

```text
Would introducing X be enough to produce Y?
```

A factor may be:

```text
NECESSARY BUT NOT SUFFICIENT

SUFFICIENT BUT NOT NECESSARY

BOTH

NEITHER
```

These categories must not be collapsed.

---

# 28. OVERDETERMINATION

Suppose:

```text
A → Y
B → Y
```

and either is sufficient.

Removing A may leave Y unchanged because B remains active.

Therefore:

```text
Y survives removal of A
```

does not necessarily imply:

```text
A had no causal role.
```

---

# 29. PREEMPTION

Suppose:

```text
A causes Y first
```

while:

```text
B would have caused Y otherwise.
```

Removing A can activate B.

Simple but-for reasoning may therefore understate causal contribution.

Consequential attribution requires deeper causal analysis.

---

# 30. SYSTEM REACTION

A counterfactual involving an adaptive system should consider:

```text
INTERVENTION
↓
DIRECT EFFECT
↓
SYSTEM RESPONSE
↓
SECOND-ORDER EFFECT
↓
FEEDBACK
↓
NEW TRAJECTORY
```

Possible responses include:

```text
adaptation

substitution

compensation

gaming

competitive response

policy response

behavioral change

resource reallocation

equilibrium shift
```

Holding reactive systems artificially static is a model assumption and must
be exposed.

---

# 31. FEEDBACK

If:

```text
Xt → Yt+1
```

and:

```text
Yt → Xt+1
```

then static propagation may be invalid.

Dynamic candidate:

```text
SCF(t+1)
=
F(SCF(t), It, Et, M)
```

---

# 32. TEMPORAL COUNTERFACTUAL STATE

```yaml
TemporalCounterfactual:
  factual_time:
  intervention_time:
  divergence_time:
  outcome_horizon:
  lag_structure:
  persistence:
  delayed_effects:
  feedback_period:
```

---

# 33. PRE-INTERVENTION INVARIANCE

Default law:

```text
for t < intervention_time:

WorldCF(t) = WorldFactual(t)
```

unless the counterfactual explicitly changes earlier history.

---

# 34. COUNTERFACTUAL DISTANCE

Historical AMOS doctrine states:

```text
UNCERTAINTY INCREASES
AS THE COUNTERFACTUAL MOVES
FARTHER FROM ACTUALITY.
```

Candidate decomposition:

```text
DCF =
f(
  intervention_distance,
  structural_distance,
  temporal_distance,
  regime_distance,
  assumption_distance
)
```

No universal numeric weighting is asserted.

---

# 35. DISTANCE CLASSES

```yaml
CounterfactualDistance:

  NEAR:
    small_intervention: true
    same_regime: usually
    limited_dependency_change: true

  MID:
    multiple_dependencies: possible
    adaptation: possible
    moderate_assumption_burden: true

  FAR:
    structural_change: possible
    regime_change: possible
    long_horizon: possible
    high_assumption_burden: true

  INCOHERENT:
    hard_constraint_violation: true
```

---

# 36. STRUCTURAL INTERVENTION

A structural counterfactual changes:

```text
fY → f'Y
```

rather than merely:

```text
Y := y'
```

Structural intervention can invalidate broad dependency closures.

Therefore:

```text
STRUCTURAL CHANGE
→
DEEPER REVALIDATION
```

by default.

---

# 37. PARAMETRIC INTERVENTION

A parametric counterfactual changes:

```text
θ → θ'
```

while potentially preserving model topology.

Local reasoning may remain valid if:

```text
scope stable

regime stable

dependency closure stable

mechanisms stable
```

---

# 38. REGIME

```yaml
Regime:
  regime_id:
  environment:
  constraints:
  dominant_mechanisms:
  thresholds:
  validity_conditions:
```

---

# 39. REGIME FIREWALL

If:

```text
RegimeFactual != RegimeCounterfactual
```

then inherited causal relationships require revalidation.

Examples:

```text
NORMAL → CRISIS

LOW LOAD → SATURATION

STABLE MARKET → PANIC

PEACE → CONFLICT

NORMAL GOVERNANCE → EMERGENCY GOVERNANCE
```

---

# 40. SCOPE

```yaml
Scope:
  system:
  entity:
  population:
  geography:
  environment:
  scale:
  time:
  measurement:
  assumptions:
```

A counterfactual conclusion inherits this applicability envelope.

---

# 41. CROSS-SCALE FIREWALL

```text
MICRO EFFECT
!=
MACRO EFFECT
```

unless aggregation is independently justified.

System-level emergence may defeat simple composition.

---

# 42. CROSS-DOMAIN FIREWALL

```text
STRUCTURAL RESEMBLANCE
!=
CAUSAL TRANSFER
```

Cross-domain analogies remain:

```text
MODEL
```

until independently validated.

---

# 43. MULTI-AGENT COUNTERFACTUALS

For strategic systems:

```text
A acts
↓
B responds
↓
A adapts
↓
C responds
```

holding all agents fixed may be invalid.

```yaml
MultiAgentCounterfactual:
  focal_intervention:
  agents:
  agent_models:
  information_states:
  response_rules:
  strategic_dependencies:
  equilibrium_or_trajectory:
  uncertainty:
```

---

# 44. INFORMATION COUNTERFACTUALS

Question:

```text
What if agent A knew fact F?
```

requires modeling:

```text
INFORMATION
↓
BELIEF
↓
DECISION
↓
ACTION
↓
SYSTEM RESPONSE
↓
OUTCOME
```

Information does not automatically determine behavior.

---

# 45. BELIEF COUNTERFACTUALS

Changing:

```text
Belief(A) := B'
```

does not change:

```text
WorldTruth
```

Hard distinction:

```text
WORLD STATE
!=
BELIEF STATE
```

---

# 46. REFLEXIVE COUNTERFACTUALS

A prediction can alter the system:

```text
PREDICTION
↓
AGENT RESPONSE
↓
OUTCOME
```

The prediction itself may therefore become part of the causal environment.

---

# 47. SELF-MODIFYING SYSTEMS

If:

```text
Mt → Mt+1
```

then intervention may alter future causal structure.

Projection may require:

```text
M0
↓ intervention
M1'
↓
M2'
↓
M3'
```

rather than assuming one fixed model.

---

# 48. MULTIPLE INTERVENTIONS

For:

```text
I = {I1, I2, ... In}
```

do not assume:

```text
Effect(I1 + I2)
=
Effect(I1) + Effect(I2)
```

Interactions may be:

```text
INDEPENDENT

SYNERGISTIC

ANTAGONISTIC

THRESHOLD-DEPENDENT

ORDER-DEPENDENT
```

---

# 49. ORDER EFFECTS

In path-dependent systems:

```text
CF(CF(W,I1),I2)
```

may differ from:

```text
CF(CF(W,I2),I1)
```

Order is therefore a potentially load-bearing variable.

---

# 50. COMPETING CAUSAL MODELS

Let:

```text
M = {M1, M2, ... Mn}
```

Evaluate:

```text
CF1 = CF(W,I,M1)

CF2 = CF(W,I,M2)

...

CFn = CF(W,I,Mn)
```

If supported models yield materially different outcomes:

```text
CONCLUSION CLASS = COMPETING
```

until discriminating evidence exists.

---

# 51. MODEL ROBUSTNESS

Suppose:

```text
M1 → A

M2 → A

M3 → A
```

This supports robustness only to the degree that:

```text
M1
M2
M3
```

are genuinely distinct and independently supported.

Shared provenance ancestry reduces independence.

---

# 52. PROVENANCE TOPOLOGY

```yaml
ProvenanceItem:
  evidence_id:
  evidence_type:
  source:
  source_identity:
  ancestry:
  collected_at:
  freshness:
  scope:
  regime:
  method:
  dependencies:
```

Counterfactual confidence must account for ancestry, not merely source count.

---

# 53. SYBIL HARDENING

Example:

```text
ONE ORIGINAL SOURCE
↓
10 SUMMARIES
↓
50 DERIVED NOTES
↓
100 COUNTERFACTUAL BRANCHES
```

does not become:

```text
100 INDEPENDENT CONFIRMATIONS.
```

All descendants may share one evidential ancestor.

---

# 54. EVIDENCE TYPES

Counterfactual reasoning uses typed evidence:

```text
SOURCE_CLAIM

OBSERVATION

DERIVED

MODEL

DECISION

UNKNOWN
```

A counterfactual output normally remains:

```text
MODEL
```

or:

```text
DERIVED
```

unless separately validated.

---

# 55. CONFIDENCE CEILING

For load-bearing premises:

```text
P1 ... Pn
```

candidate AMOS rule:

```text
Confidence(CF)
<=
minimum confidence of load-bearing premises
```

unless the weak premise is independently revalidated or removed from the
proof path.

Fluent reasoning must never increase confidence beyond its evidential base.

---

# 56. UNCERTAINTY VECTOR

```text
UCF =
(
  evidence_uncertainty,
  model_uncertainty,
  scope_uncertainty,
  temporal_uncertainty,
  causal_uncertainty,
  intervention_uncertainty,
  execution_uncertainty,
  provenance_independence_uncertainty
)
```

These uncertainties should remain distinguishable when decision-relevant.

---

# 57. IDENTIFIABILITY

Distinguish:

```text
DEFINED

IDENTIFIABLE

ESTIMABLE

ESTIMATED

VALIDATED
```

A counterfactual can be meaningful but not identifiable from available
evidence.

Correct result:

```text
The counterfactual is defined,
but available evidence does not identify it.
```

---

# 58. PARTIAL IDENTIFICATION

If exact value cannot be established but defensible bounds exist:

```text
L <= CF <= U
```

return the interval.

Do not invent a point estimate.

If the same decision follows throughout the interval, decision sufficiency
may still be achieved.

---

# 59. PLAUSIBILITY / PROBABILITY FIREWALL

```text
POSSIBLE
!=
PLAUSIBLE
!=
PROBABLE
```

Also:

```text
BRANCH COUNT
!=
PROBABILITY
```

and:

```text
GENERATED FREQUENCY
!=
EMPIRICAL FREQUENCY
```

Without a justified probability model:

```text
DO NOT INVENT NUMERIC PROBABILITIES.
```

---

# 60. HISTORICAL CONSTRUCT_COUNTERFACTUAL CONTRACT

```yaml
construct_counterfactual:

  inputs:
    - actual_state
    - intervention_description
    - causal_model
    - plausibility_constraints

  outputs:
    - counterfactual_state
    - causal_chain
    - uncertainties
    - assumption_list
    - plausibility_assessment
    - alternative_outcomes
```

---

# 61. HISTORICAL ACTUAL/COUNTERFACTUAL COMPARISON

```yaml
compare_actual_vs_counterfactual:

  inputs:
    - actual_outcome
    - counterfactual_outcome
    - causal_model
    - confidence_levels

  outputs:
    - difference_analysis
    - causal_attribution
    - confounding_factors
    - attribution_confidence
    - alternative_explanation
```

---

# 62. HISTORICAL SCENARIO ANALYSIS

```yaml
scenario_analysis:

  inputs:
    - current_state
    - scenario_list
    - uncertainty_model
    - decision_criteria

  outputs:
    - scenario_outcomes
    - probability_assignments_if_available
    - recommended_preparation
    - early_warning_signals
    - scenario_comparison
```

The phrase:

```text
if available
```

is load-bearing.

No justified probability model means no fabricated probability assignment.

---

# 63. FULL RUNTIME ALGORITHM

```text
FUNCTION K_COUNTERFACTUAL(query):

  1. Parse objective.

  2. Determine:
       scope
       stakes
       temporal horizon
       deliverable.

  3. Classify counterfactual:
       PAST
       FUTURE
       STRUCTURAL
       CAUSAL.

  4. Bind factual anchor.

  5. Bind intervention.

  6. Bind queried outcome.

  7. Identify decision-changing uncertainty.

  8. Retrieve smallest sufficient dependency closure.

  9. Retrieve causal model.

 10. Type evidence.

 11. Resolve provenance ancestry.

 12. Check evidence freshness.

 13. Check scope.

 14. Check regime.

 15. Check causal epoch.

 16. Check causal model sufficiency.

 17. Check confounding.

 18. Check mediation.

 19. Check moderation.

 20. Check feedback.

 21. Check strategic/system reaction.

 22. If critical causal gap exists:
       return UNKNOWN/GAP.

 23. Infer latent/background state if required.

 24. Apply minimal intervention.

 25. Propagate only licensed descendants.

 26. Generate materially distinct outcomes.

 27. Preserve competing models.

 28. Assess plausibility.

 29. Represent uncertainty.

 30. Apply weakest-premise confidence ceiling.

 31. Find smallest result-flipping premise.

 32. If consequential:
       run adversarial validation.

 33. Identify falsifiers.

 34. Classify conclusion.

 35. If action requested:
       apply governance,
       authorization,
       risk,
       reversibility,
       commit-time checks.

 36. Return proof-capsule-compatible result.
```

---

# 64. COUNTERFACTUAL RSCF

```yaml
CounterfactualRSCF:

  claim:
    statement:
    class:

  factual_anchor:

  intervention:

  queried_outcome:

  premises: []

  evidence: []

  provenance:

  causal_model:

  dependency_closure: []

  scope:

  regime:

  causal_epoch:

  freshness:

  assumptions: []

  competing_hypotheses: []

  contradictions: []

  falsifiers: []

  sensitivity:

  uncertainty:

  confidence_ceiling:

  invalidation_conditions: []
```

---

# 65. RSCF RECURSION

A counterfactual RSCF can depend on:

```text
COUNTERFACTUAL RSCF
│
├── FACTUAL-STATE RSCF
├── CAUSAL-EDGE RSCF
├── INTERVENTION-VALIDITY RSCF
├── REGIME-VALIDITY RSCF
├── SCOPE-VALIDITY RSCF
└── PROVENANCE RSCF
```

If one premise fails:

```text
INVALIDATE ONLY DEPENDENT DESCENDANTS.
```

---

# 66. ATOMIC MULTI-RSCF REASONING

A consequential counterfactual may depend jointly on:

```text
technical feasibility

financial feasibility

safety

governance

authorization

causal validity
```

The decision boundary must not combine incompatible snapshots or causal
epochs.

---

# 67. H/M/L INTEGRATION

Counterfactual retrieval follows:

```text
BOOTSTRAP CAPSULE
↓
H DOMAIN
↓
M SUBSYSTEM
↓
L LOAD-BEARING DETAIL
↓
RAW EVIDENCE ONLY IF REQUIRED
```

Raw evidence defaults to:

```text
DO_NOT_LOAD_UNLESS_REQUIRED
```

The kernel should not retrieve irrelevant corpus material merely to appear
comprehensive.

---

# 68. GMEF INTEGRATION

Counterfactual reasoning can support governed evolution:

```text
PROPOSED CHANGE
↓
COUNTERFACTUAL CONSEQUENCES
↓
COMPETING OUTCOMES
↓
RISK / BENEFIT
↓
GMEF
↓
GOVERNED DECISION
```

A favorable counterfactual does not itself authorize evolution.

---

# 69. WORLD MODEL INTEGRATION

Conceptual dependency:

```text
K_SYSTEM_STATE
↓
K_WORLD_MODEL
↓
K_COUNTERFACTUAL
↓
COUNTERFACTUAL WORLD
```

Missing world-model mechanics remain:

```text
UNKNOWN/GAP
```

rather than being fabricated.

---

# 70. CONTEXT STATE INTEGRATION

```yaml
CounterfactualContext:

  active_world:
    ACTUAL | COUNTERFACTUAL

  factual_parent:

  branch_id:

  intervention:

  goal:

  scope:

  regime:

  causal_epoch:
```

Leaving counterfactual mode must restore factual context.

---

# 71. MEMORY ADMISSION

Counterfactual outputs must retain their epistemic type.

Forbidden:

```text
COUNTERFACTUAL MODEL
↓
MEMORY
↓
FACT
```

Correct:

```yaml
MemoryRecord:
  type: COUNTERFACTUAL_MODEL
  factual_anchor:
  intervention:
  causal_model:
  assumptions:
  conclusion_class:
  scope:
  regime:
  provenance:
  freshness:
```

---

# 72. MEMORY RETRIEVAL

Before reuse check:

```text
Is the factual anchor still valid?

Is the model version compatible?

Is the causal epoch compatible?

Is scope compatible?

Is regime compatible?

Is evidence fresh?

Did new contradictory evidence appear?

Did a load-bearing premise change?
```

If not:

```text
STALE
```

or:

```text
REVALIDATION_REQUIRED
```

---

# 73. CAUSAL EPOCH

```yaml
CausalEpoch:
  epoch_id:
  causal_model_version:
  evidence_snapshot:
  dependency_snapshot:
  provenance_snapshot:
  regime:
  validity_conditions:
```

Counterfactual proof capsules may be reused only across compatible causal
epochs.

---

# 74. MVCC / CAS REASONING PATTERN

Conceptually:

```text
READ FACTUAL STATE @ VERSION V0
↓
COMPUTE COUNTERFACTUAL
↓
CHECK LOAD-BEARING DEPENDENCIES
BEFORE CONSEQUENTIAL REUSE
↓
UNCHANGED?
   YES → REUSE
   NO  → REVALIDATE AFFECTED CLOSURE
```

This is an AMOS reasoning pattern, not a claim that the conversational
runtime literally implements distributed MVCC.

---

# 75. FAST PATH

Local counterfactual reasoning is permitted only when:

```yaml
CounterfactualFastPath:

  factual_anchor_valid: true

  intervention_unambiguous: true

  dependency_closure_established: true

  causal_model_adequate: true

  provenance_independence_adequate: true

  scope_compatible: true

  regime_compatible: true

  causal_epoch_compatible: true

  freshness_valid: true

  material_conflict_absent: true

  stakes_reversible_or_limited: true
```

---

# 76. ESCALATION CONDITIONS

Escalate reasoning depth when any of the following is material:

```text
CAUSAL AMBIGUITY

CONFOUNDING

CORRELATED PROVENANCE

CONTRADICTION

STALE PREMISE

REGIME SHIFT

SCOPE TRANSFER

STRUCTURAL INTERVENTION

FEEDBACK

NONLINEARITY

MULTI-AGENT RESPONSE

IRREVERSIBILITY

SAFETY IMPACT

LEGAL IMPACT

FINANCIAL IMPACT

INSTITUTIONAL IMPACT

GOVERNANCE IMPACT

AMBIGUOUS DEPENDENCY
```

---

# 77. ADVERSARIAL VALIDATION

For consequential counterfactuals, challenge the strongest supported result.

Ask:

```text
Is the factual baseline wrong?

Is the intervention ambiguous?

Is the causal edge merely correlational?

Could reverse causality explain the pattern?

Is there hidden confounding?

Was a mediator incorrectly frozen?

Was a moderator ignored?

Was feedback ignored?

Were system reactions ignored?

Did the regime change?

Did scope silently expand?

Are apparently independent sources actually descendants
of the same source?

Is evidence stale?

Does another supported causal model reverse the result?

What is the smallest assumption that flips the conclusion?
```

If challenge succeeds:

```text
DOWNGRADE

CONDITION

PRESERVE COMPETING

or

RETURN UNKNOWN/GAP
```

---

# 78. SENSITIVITY

Identify the smallest premise, threshold, assumption, or observation capable
of changing the result.

Conceptually:

```text
p*
=
smallest load-bearing change
that flips the conclusion
```

Record:

```yaml
Sensitivity:
  flip_premise:
  flip_threshold:
  flip_observation:
  decision_impact:
```

If a small plausible perturbation flips the result:

```text
CONCLUSION = CONDITIONAL
```

---

# 79. FALSIFIERS

```yaml
Falsifiers:

  - observation:
    threshold:
    affected_premise:
    affected_edge:
    affected_conclusion:

  - regime_change:

  - confounder_discovered:

  - intervention_failure:

  - mechanism_disconfirmed:

  - provenance_failure:

  - factual_anchor_invalidated:
```

A meaningful counterfactual should expose what would invalidate it.

---

# 80. LOCAL INVALIDATION

Core law:

```text
Invalid(p)
→
Invalidate dependent descendants(p)
```

not:

```text
Invalid(p)
→
Invalidate everything
```

This preserves unaffected reasoning.

---

# 81. FAILURE RECOVERY

```text
DETECT FAILED PREMISE
↓
TRACE DEPENDENCY EDGES
↓
INVALIDATE DEPENDENT DESCENDANTS
↓
ROLL BACK TO NEAREST VALID STATE
↓
CHANGE EVIDENCE / MODEL / ASSUMPTION
↓
RECOMPUTE LOCAL CLOSURE
↓
REVALIDATE
```

Never repeat a failed reasoning path without changed evidence or assumptions.

---

# 82. COUNTERFACTUAL HARM

Consequential counterfactual decisions should consider:

```yaml
CounterfactualHarm:
  direct_harm:
  indirect_harm:
  distributional_harm:
  opportunity_harm:
  irreversible_harm:
  informational_harm:
  governance_harm:
  uncertainty_harm:
```

Potential harm is itself model-dependent and must retain appropriate
epistemic typing.

---

# 83. ACTION GOVERNANCE

Validation burden increases with:

```text
IRREVERSIBILITY

COST

LEGAL EXPOSURE

FINANCIAL EXPOSURE

HEALTH / SAFETY EXPOSURE

INSTITUTIONAL IMPACT

DOWNSTREAM DEPENDENCY

UNCERTAINTY

CAUSAL AMBIGUITY
```

When feasible, prefer:

```text
OBSERVATION

SIMULATION

SANDBOX

LIMITED EXPERIMENT

REVERSIBLE PILOT

STAGED ROLLOUT

MONITORED DEPLOYMENT
```

before irreversible commitment.

---

# 84. ACTION AUTHORITY FIREWALL

Hard invariant:

```text
COUNTERFACTUAL RECOMMENDATION
!=
EXECUTION AUTHORITY
```

Before real action:

```text
CHECK CAPABILITY

CHECK AUTHORIZATION

CHECK EFFECT CLASS

CHECK RISK

CHECK CURRENT STATE

CHECK COMMIT-TIME AUTHORITY
```

---

# 85. VALUE OF INFORMATION

When uncertainty matters, seek evidence that can change the decision.

Candidate representation:

```text
VOI(test)
=
expected decision improvement
-
test cost
-
test risk
```

The kernel prefers high-information discriminating tests over redundant
evidence accumulation.

---

# 86. DISCRIMINATING TEST

For competing models:

```text
M1
M2
```

prefer a test whose predicted observations diverge materially:

```text
T*
=
highest-value feasible discriminating test
```

subject to:

```text
cost

risk

authority

reversibility
```

---

# 87. COUNTERFACTUAL PROOF CAPSULE

```yaml
CounterfactualProofCapsule:

  capsule_id:

  claim:
    text:
    class:

  factual_anchor:

  intervention:

  queried_outcome:

  causal_model:
    model_id:
    version:
    causal_epoch:

  load_bearing_premises: []

  evidence: []

  provenance: []

  dependency_closure: []

  causal_structure:
    mechanisms:
    mediators:
    moderators:
    confounders:
    feedback:

  counterfactual_state:

  alternative_outcomes: []

  competing_explanations: []

  scope:

  regime:

  freshness:

  uncertainty:
    evidence:
    model:
    scope:
    temporal:
    causal:
    intervention:
    execution:
    provenance_independence:

  sensitivity:
    flip_premise:
    flip_threshold:

  falsifiers: []

  confidence_ceiling:

  invalidation_conditions: []
```

---

# 88. COMMON FAILURE MODES

## CF-F01 — OVERDETERMINATION ERROR

Treating one hypothetical result as inevitable while ignoring other causal
paths.

## CF-F02 — SYSTEM REACTION FAILURE

Holding an adaptive system artificially static.

## CF-F03 — CORRELATION/CAUSATION COLLAPSE

Treating association as intervention evidence.

## CF-F04 — UNREALISTIC BASELINE

Comparing actuality against an implausible or cherry-picked alternative.

## CF-F05 — HIDDEN CHANGE

Changing multiple variables while claiming a single intervention.

## CF-F06 — FALSE PRECISION

Assigning exact numbers unsupported by the model or evidence.

## CF-F07 — FALSE PROBABILITY

Assigning probability without a justified probability model.

## CF-F08 — REGIME LEAK

Applying causal relations outside their validated regime.

## CF-F09 — SCOPE LEAK

Generalizing beyond the system/population/environment supported.

## CF-F10 — PROVENANCE COLLAPSE

Counting correlated descendants as independent evidence.

## CF-F11 — STALE REUSE

Reusing a counterfactual after a load-bearing dependency has changed.

## CF-F12 — COMPETING COLLAPSE

Forcing one conclusion where supported models remain unresolved.

## CF-F13 — FACTUAL CONTAMINATION

Storing a counterfactual branch as actual history.

## CF-F14 — AUTHORITY ESCALATION

Treating a modeled recommendation as authorization for action.

---

# 89. HARD SAFETY CONSTRAINTS

```yaml
CounterfactualSafety:

  never_present_counterfactual_as_fact: true

  never_hide_load_bearing_assumptions: true

  never_ignore_material_uncertainty: true

  never_invent_missing_causal_edges: true

  never_convert_correlation_into_causation_without_evidence: true

  never_silently_change_unrelated_variables: true

  never_invent_probability: true

  never_force_competing_models_into_false_consensus: true

  never_generalize_across_scope_without_validation: true

  never_generalize_across_regime_without_validation: true

  never_count_shared_provenance_as_independent_confirmation: true

  never_treat_counterfactual_output_as_execution_authority: true
```

---

# 90. INTEGRATION

Historical integration includes:

```text
META LOGIC

META EPISTEMOLOGY

MULTI-PERSPECTIVE REASONING

STRATEGY / GAME REASONING

RISK ASSESSMENT

DECISION ANALYSIS

STRATEGIC PLANNING

CAUSAL INFERENCE

POLICY EVALUATION
```

v4.4 integration additionally binds counterfactual reasoning to:

```text
RSCF

GMEF

H/M/L

PROVENANCE TOPOLOGY

SYBIL HARDENING

EPISTEMIC REGIMES

COMPETING HYPOTHESES

CAUSAL EPOCH

LOCAL INVALIDATION

GOVERNED ACTION
```

---

# 91. CORE UNIT TESTS

```yaml
tests:

  past_counterfactual:
    input:
      factual_history:
      intervention:
      causal_model:
    expect:
      - counterfactual_state
      - causal_chain
      - assumptions
      - uncertainties

  actual_vs_counterfactual:
    expect:
      - difference_analysis
      - causal_attribution
      - confounding_factors
      - alternative_explanation

  overdetermination_detection:
    expect:
      - overdetermination_flag

  scenario_analysis:
    expect:
      - scenario_outcomes
      - comparison
      - preparation
      - early_warning_signals
```

---

# 92. EXTENDED VALIDATION SUITE

```text
FACTUAL_ANCHOR_TEST

INTERVENTION_BINDING_TEST

MINIMAL_CHANGE_TEST

HIDDEN_CHANGE_TEST

CAUSAL_CHAIN_TEST

CAUSAL_CLOSURE_TEST

CONFOUNDING_TEST

MEDIATION_TEST

MODERATION_TEST

OVERDETERMINATION_TEST

PREEMPTION_TEST

FEEDBACK_TEST

SYSTEM_REACTION_TEST

REGIME_SHIFT_TEST

SCOPE_TRANSFER_TEST

TEMPORAL_VALIDITY_TEST

PROVENANCE_INDEPENDENCE_TEST

SYBIL_HARDENING_TEST

COMPETING_MODEL_TEST

PARTIAL_IDENTIFICATION_TEST

FALSE_PROBABILITY_TEST

FALSE_PRECISION_TEST

UNCERTAINTY_DISTANCE_TEST

CONFIDENCE_CEILING_TEST

SENSITIVITY_TEST

FALSIFIER_TEST

ADVERSARIAL_CHALLENGE_TEST

LOCAL_INVALIDATION_TEST

MEMORY_TYPING_TEST

STALE_REUSE_TEST

CAUSAL_EPOCH_TEST

ACTION_AUTHORITY_TEST

REVERSIBILITY_TEST
```

---

# 93. NEGATIVE TESTS

```text
CORRELATION
→
CAUSAL COUNTERFACTUAL

MUST FAIL
```

```text
MODEL OUTPUT
→
OBSERVED FACT

MUST FAIL
```

```text
ONE SOURCE
→
TEN SUMMARIES
→
TEN INDEPENDENT SOURCES

MUST FAIL
```

```text
CHANGE X
→
SILENTLY CHANGE Z

MUST FAIL
```

```text
NO PROBABILITY MODEL
→
73.8% PROBABILITY

MUST FAIL
```

```text
SUPPORTED COMPETING MODELS
→
ONE CERTAIN CONCLUSION

MUST FAIL
```

```text
STALE CAUSAL MODEL
→
CURRENT VALIDITY

MUST FAIL WITHOUT REVALIDATION
```

```text
COUNTERFACTUAL RECOMMENDATION
→
EXECUTION AUTHORITY

MUST FAIL
```

---

# 94. PROPERTY INVARIANTS

```text
Observed(Counterfactual) = false
```

unless that formerly counterfactual world later becomes actual and is
independently observed.

```text
Confidence(CF)
<=
WeakestLoadBearingPremise
```

unless independently revalidated.

```text
Changed(CF)
⊆
Intervention
∪
LicensedDescendants
∪
ExplicitAuxiliaryChanges
```

```text
BranchCount
!=
EvidenceCount
```

```text
Correlation
!=
CounterfactualCausation
```

```text
ModelAgreement
!=
IndependentEvidence
```

---

# 95. METAMORPHIC TESTS

If independently irrelevant variable Z changes:

```text
TARGET COUNTERFACTUAL SHOULD NOT CHANGE
```

when independence is established.

If load-bearing edge:

```text
X → Y
```

is removed and no alternative path remains:

```text
EFFECT ON Y
MUST DISAPPEAR
OR BECOME UNKNOWN
```

If regime shifts outside validated scope:

```text
CONFIDENCE MUST FALL
OR REVALIDATION MUST OCCUR
```

If evidence ancestry collapses from multiple apparent sources to one origin:

```text
INDEPENDENCE CONFIDENCE MUST FALL
```

---

# 96. ERROR REGISTRY

```yaml
CounterfactualErrors:

  E_CF_NO_BASELINE:
    meaning: factual anchor unavailable

  E_CF_AMBIGUOUS_INTERVENTION:
    meaning: intervention insufficiently specified

  E_CF_HIDDEN_CHANGE:
    meaning: undeclared world change

  E_CF_CAUSAL_MODEL_MISSING:
    meaning: required causal structure unavailable

  E_CF_CAUSAL_OVERREACH:
    meaning: causal conclusion exceeds evidence

  E_CF_CONFOUNDING:
    meaning: unresolved material confounding

  E_CF_MEDIATOR_ERROR:
    meaning: mediation handled incorrectly

  E_CF_MODERATOR_ERROR:
    meaning: conditional effect ignored

  E_CF_FEEDBACK_IGNORED:
    meaning: material feedback omitted

  E_CF_SYSTEM_REACTION_IGNORED:
    meaning: adaptive response omitted

  E_CF_SCOPE_LEAK:
    meaning: conclusion exceeds scope

  E_CF_REGIME_LEAK:
    meaning: conclusion crosses unsupported regime

  E_CF_TEMPORAL_ERROR:
    meaning: temporal structure invalid

  E_CF_PROVENANCE_COLLAPSE:
    meaning: ancestry incorrectly treated as independence

  E_CF_BRANCH_SYBIL:
    meaning: generated branches treated as independent evidence

  E_CF_FALSE_PROBABILITY:
    meaning: probability invented

  E_CF_FALSE_PRECISION:
    meaning: unsupported numerical precision

  E_CF_COMPETING_COLLAPSE:
    meaning: unresolved models falsely merged

  E_CF_STALE_REUSE:
    meaning: invalid cached counterfactual reused

  E_CF_AUTHORITY_ESCALATION:
    meaning: reasoning result treated as action authority

  E_CF_IDENTIFIABILITY_GAP:
    meaning: counterfactual not identifiable

  E_CF_UNKNOWN:
    meaning: unresolved counterfactual failure
```

---

# 97. LAW REGISTRY

```text
KCF-001  FACTUAL ANCHOR

KCF-002  ACTUAL / COUNTERFACTUAL SEPARATION

KCF-003  EXPLICIT INTERVENTION

KCF-004  MINIMAL CHANGE

KCF-005  CAUSAL CHAIN CONSERVATION

KCF-006  NO HIDDEN CHANGE

KCF-007  CAUSAL MODEL REQUIREMENT

KCF-008  CORRELATION FIREWALL

KCF-009  SYSTEM REACTION AWARENESS

KCF-010  UNCERTAINTY-DISTANCE DISCIPLINE

KCF-011  ASSUMPTION TRANSPARENCY

KCF-012  SCOPE PRESERVATION

KCF-013  REGIME REVALIDATION

KCF-014  TEMPORAL VALIDITY

KCF-015  PROVENANCE CONTINUITY

KCF-016  SYBIL HARDENING

KCF-017  COMPETING PRESERVATION

KCF-018  IDENTIFIABILITY DISCIPLINE

KCF-019  CONFIDENCE CEILING

KCF-020  SENSITIVITY FIRST

KCF-021  FALSIFIER VISIBILITY

KCF-022  LOCAL INVALIDATION

KCF-023  MEMORY TYPING

KCF-024  ACTION NON-AUTHORIZATION

KCF-025  REVERSIBILITY PREFERENCE

KCF-026  MINIMUM SUFFICIENT PROOF

KCF-027  NO FALSE PRECISION

KCF-028  NO PROBABILITY INVENTION

KCF-029  CAUSAL-EPOCH BINDING

KCF-030  INTEGRITY OVER FLUENCY
```

These identifiers are normalized candidate-canon identifiers. They are not
asserted to be historical AMOS v1.0 numbering.

---

# 98. USER-FACING OUTPUT CONTRACT

```yaml
CounterfactualResult:

  label: COUNTERFACTUAL

  type:
    PAST | FUTURE | STRUCTURAL | CAUSAL

  factual_baseline:

  intervention:

  queried_outcome:

  conclusion:
    statement:
    class:
      VERIFIED |
      DERIVED |
      MODEL |
      CONDITIONAL |
      COMPETING |
      UNKNOWN/GAP

  causal_basis: []

  assumptions: []

  system_reactions: []

  competing_outcomes: []

  alternative_explanations: []

  confounders: []

  scope:

  regime:

  temporal_validity:

  uncertainty:

  confidence_ceiling:

  sensitivity:

  falsifiers: []

  invalidation_conditions: []

  discriminating_test:

  reversible_action:
```

---

# 99. ADAPTIVE COMPLEXITY

```text
C0 — DIRECT

C1 — COMPACT

C2 — STRUCTURED

C3 — DEEP

C4 — MAXIMUM
```

Escalate for:

```text
HIGH STAKES

IRREVERSIBILITY

NOVELTY

WEAK EVIDENCE

STALE EVIDENCE

CONTRADICTION

CAUSAL AMBIGUITY

SCOPE MISMATCH

REGIME SHIFT

COMPETING MODELS

GOVERNANCE IMPACT

PROVENANCE UNCERTAINTY
```

De-escalate once outcome-changing uncertainty has been resolved.

---

# 100. STOP CONDITIONS

Stop counterfactual expansion when:

```text
CLAIM SUFFICIENCY
AND
DECISION SUFFICIENCY
AND
ACTION SUFFICIENCY
```

have been achieved.

More scenarios are not automatically more knowledge.

---

# 101. PROVENANCE STRATA

```yaml
ProvenanceStrata:

  S0_DIRECT_SOURCE:
    meaning: >
      Explicitly supported by recovered historical
      AMOS counterfactual kernel material.

  S1_AMOS_LINEAGE:
    meaning: >
      Explicitly inherited from broader AMOS architecture
      and kernel relationships.

  S2_V4_4_INTEGRATION:
    meaning: >
      Integration required to align K_COUNTERFACTUAL with
      AMOS_CORE v4.4 integrity, provenance, scope,
      regime, RSCF, causal epoch, and governance doctrine.

  S3_DERIVED_FORMALIZATION:
    meaning: >
      Formal schemas, algorithms, equations, test structures,
      and normalized contracts derived from AMOS principles
      but not claimed as verbatim historical source.

  S4_EXTERNAL_REFERENCE:
    meaning: >
      External counterfactual/causal research used for
      comparison or validation only.

  S5_UNKNOWN_GAP:
    meaning: >
      Canonical or empirical detail not currently established.
```

---

# 102. HISTORICAL / DERIVED BOUNDARY

## SOURCE-SUPPORTED HISTORICAL SPINE

The recovered historical lineage supports the existence and role of a
dedicated counterfactual reasoning kernel and its placement within the
Meta-Cognition architecture.

Historical content includes the core concepts of:

```text
PAST COUNTERFACTUALS

FUTURE COUNTERFACTUALS

STRUCTURAL COUNTERFACTUALS

CAUSAL COUNTERFACTUALS

PLAUSIBLE INITIAL STATE

MINIMAL CHANGE

CAUSAL CHAIN CONSERVATION

UNCERTAINTY WITH COUNTERFACTUAL DISTANCE

ASSUMPTION TRANSPARENCY

ACTUAL / COUNTERFACTUAL COMPARISON

SCENARIO ANALYSIS

COMMON FAILURE MODES

SAFETY CONSTRAINTS
```

## V4.4 INTEGRATION

The current artifact integrates the counterfactual kernel with:

```text
RSCF

H/M/L

GMEF

TYPED EVIDENCE

EPISTEMIC REGIMES

COMPETING HYPOTHESES

PROVENANCE TOPOLOGY

SYBIL HARDENING

SCOPE / REGIME FIREWALL

CAUSAL EPOCH

WEAKEST-PREMISE CONFIDENCE CEILING

LOCAL INVALIDATION

ATOMIC MULTI-RSCF REASONING

PROOF-BASED LOCAL REASONING

REVERSIBILITY GOVERNANCE
```

## DERIVED FORMALIZATION

The following are normalized formalizations rather than claims of verbatim
historical implementation:

```text
SCM-STYLE EQUATIONS

ABDUCTION → ACTION → PROJECTION

CAUSAL RELATION TAXONOMY

COUNTERFACTUAL DISTANCE DECOMPOSITION

UNCERTAINTY VECTOR

IDENTIFIABILITY STATES

PARTIAL IDENTIFICATION CONTRACT

PROOF CAPSULE SCHEMA

FAST-PATH SCHEMA

ERROR REGISTRY

PROPERTY TESTS

METAMORPHIC TESTS

KCF LAW IDENTIFIERS
```

---

# 103. KNOWN GAPS

```yaml
KnownGaps:

  - id: KCF-GAP-001
    class: DECISION-RELEVANT
    issue: >
      Exact byte-identical correspondence between every
      recovered historical counterfactual artifact and the
      present normalized K_COUNTERFACTUAL file has not been
      established.

  - id: KCF-GAP-002
    class: DECISION-RELEVANT
    issue: >
      A complete executable implementation corresponding
      exactly to the reconstructed specification is not
      established.

  - id: KCF-GAP-003
    class: EXPLANATORY
    issue: >
      Formal supersession history between every historical
      counterfactual filename/version and the canonical
      K_COUNTERFACTUAL name remains incomplete.

  - id: KCF-GAP-004
    class: DECISION-RELEVANT
    issue: >
      No universal calibrated probability model exists for
      all counterfactual domains.

  - id: KCF-GAP-005
    class: UNKNOWN/GAP
    issue: >
      Universal empirical validity is not established.

  - id: KCF-GAP-006
    class: UNKNOWN/GAP
    issue: >
      Universal formal proof of causal correctness is not
      established.
```

---

# 104. PROMOTION GATE

Before promotion from:

```text
CANDIDATE_CANON
```

to an authoritative canon state:

```text
[ ] historical sources registered

[ ] source lineage recorded

[ ] duplicates resolved

[ ] supersession graph recorded

[ ] dependencies verified

[ ] conflicts registered

[ ] Meta Logic compatibility checked

[ ] Meta Epistemology compatibility checked

[ ] Probability/Statistics dependency checked

[ ] RSCF integration tested

[ ] H/M/L integration tested

[ ] GMEF integration tested

[ ] causal firewall tested

[ ] scope firewall tested

[ ] regime firewall tested

[ ] provenance topology tested

[ ] Sybil hardening tested

[ ] causal-model gap behavior tested

[ ] hidden-change detection tested

[ ] competing-model behavior tested

[ ] confidence ceiling tested

[ ] partial-identification behavior tested

[ ] memory typing tested

[ ] causal epoch behavior tested

[ ] local invalidation tested

[ ] action-authority firewall tested

[ ] failure recovery tested

[ ] authoritative-state record updated

[ ] steward approval completed
```

Existence of this file alone does not satisfy those gates.

---

# 105. CANONICAL COMPRESSION

```text
K_COUNTERFACTUAL
=
DISCIPLINED
ALTERNATIVE-WORLD
REASONING.

ANCHOR
THE FACTUAL WORLD.

DECLARE
THE INTERVENTION.

CHANGE ONLY
WHAT THE INTERVENTION
AND DEFENSIBLE
CAUSAL CONSEQUENCES
REQUIRE.

PRESERVE
CAUSAL STRUCTURE.

MODEL
SYSTEM REACTIONS.

EXPOSE
ASSUMPTIONS.

PRESERVE
UNCERTAINTY.

KEEP
COUNTERFACTUAL
SEPARATE FROM FACT.

KEEP
PREDICTION
SEPARATE FROM
INTERVENTION.

KEEP
CORRELATION
SEPARATE FROM
CAUSATION.

INCREASE
UNCERTAINTY
AS THE ALTERNATIVE WORLD
MOVES FARTHER
FROM ACTUALITY.

PRESERVE
COMPETING MODELS.

PRESERVE
PROVENANCE ANCESTRY.

DO NOT
COUNT DERIVED COPIES
AS INDEPENDENT EVIDENCE.

DO NOT
GENERALIZE
OUTSIDE SCOPE.

DO NOT
TRANSFER
ACROSS REGIMES
WITHOUT REVALIDATION.

DO NOT
INVENT
MISSING CAUSAL EDGES.

DO NOT
INVENT
PROBABILITIES.

WHEN
IDENTIFICATION FAILS:

RETURN
BOUNDS
OR
UNKNOWN/GAP.

WHEN
A PREMISE FAILS:

INVALIDATE
ONLY DEPENDENT
DESCENDANTS.

WHEN
THE RESULT
IS FRAGILE:

RETURN
CONDITIONAL.

WHEN
SUPPORTED MODELS
DISAGREE:

RETURN
COMPETING.

WHEN
A CHEAP,
REVERSIBLE,
HIGH-INFORMATION
DISCRIMINATING TEST
EXISTS:

PREFER
THE TEST
OVER
MORE SPECULATION.

NEVER
LET
COMPLETENESS,
FLUENCY,
SPEED,
OR NUMERICAL PRECISION
OUTRUN
INTEGRITY.
```

---

# 106. FORMAL KERNEL CONTRACT

Conceptually:

```text
K_COUNTERFACTUAL:

(F, I, M, E, S, R, T, P)

→

(C, Class, U, D, Falsifiers)
```

where:

```text
F = factual state

I = intervention

M = causal model

E = evidence

S = scope

R = regime

T = temporal state

P = provenance topology

C = counterfactual conclusion

Class = epistemic conclusion class

U = uncertainty vector

D = dependency / invalidation topology
```

subject to:

```text
FACTUAL INTEGRITY

MINIMAL INTERVENTION

CAUSAL VALIDITY

SCOPE INTEGRITY

REGIME INTEGRITY

TEMPORAL INTEGRITY

PROVENANCE INTEGRITY

ASSUMPTION TRANSPARENCY
```

and:

```text
Confidence(C)
<=
WeakestLoadBearingPremise
```

unless independently revalidated.

---

# 107. FINAL STATE

```yaml
K_COUNTERFACTUAL:

  historical_lineage:
    kernel: Counterfactual_Reasoning_Kernel
    state: SOURCE_SUPPORTED

  current_artifact:
    name: K_COUNTERFACTUAL
    status: CANDIDATE_CANON
    conclusion_class: DERIVED

  amos_core_target:
    version: v4.4
    alignment: INTEGRATED_MODEL

  executable_implementation:
    status: UNKNOWN/GAP

  empirical_validation:
    status: UNKNOWN/GAP

  universal_formal_verification:
    status: UNKNOWN/GAP

  supersession:
    K_COUNTERFACTUAL_PLACEHOLDER:
      status: SUPERSEDED_BY_CANDIDATE

    authoritative_final_canon:
      status: NOT_YET_PROMOTED
```

---

# 108. TERMINAL INTEGRITY LAW

The governing counterfactual law is:

```text
NEVER CLAIM AN UNREALIZED WORLD
MORE STRONGLY THAN
THE CAUSAL MODEL,
EVIDENCE,
PROVENANCE,
SCOPE,
REGIME,
TEMPORAL VALIDITY,
AND UNCERTAINTY
PERMIT.
```

The governing intervention law is:

```text
CHANGE ONLY WHAT
THE DECLARED INTERVENTION
AND DEFENSIBLE
CAUSAL CONSEQUENCES
REQUIRE.
```

The governing epistemic law is:

```text
WHEN THE EVIDENCE CANNOT
DISTINGUISH THE WORLDS,

PRESERVE COMPETING

OR RETURN UNKNOWN/GAP.
```

The governing operational law is:

```text
UNDER CONSEQUENTIAL UNCERTAINTY,

PREFER THE CHEAPEST
SAFE,
REVERSIBLE,
HIGH-INFORMATION
DISCRIMINATING TEST

OVER
UNSUPPORTED CERTAINTY.
```

# END — K COUNTERFACTUAL

```

This is the complete replacement artifact rather than a placeholder stub. The Drive search also confirms that AMOS has a dedicated `Counterfactual_Reasoning_Kernel` folder and a historical `AMOS_Counterfactual_Reasoning_Kernel_v0_Meta_Cognition4_2.md`, which should remain part of the provenance/supersession record rather than being silently collapsed into this normalized file. :contentReference[oaicite:2]{index=2} :contentReference[oaicite:3]{index=3}
```
