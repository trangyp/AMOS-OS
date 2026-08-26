# K COUNTERFACTUAL

```yaml
artifact_id: K-COUNTERFACTUAL
kernel_id: Counterfactual_Reasoning_Kernel
canonical_alias: K_COUNTERFACTUAL
historical_version: "1.0.0"
target_lineage: AMOS_CORE_v4.4
origin_architect: Trang Phan
group: Kernels.Meta_Cognition
category: Meta_Cognition
priority: 9
required: true

status:
  historical_kernel: DEFINED
  historical_source_spine: SOURCE_CLAIM
  v4_4_normalization: DERIVED
  exact_original_file: PARTIALLY_RECOVERED

conclusion_class: DERIVED

integrity_contract:
  historical_material: preserve
  extensions: explicitly_label
  missing_material: never_invent
  counterfactual_as_fact: forbidden
```

The historical source identifies `Counterfactual_Reasoning_Kernel` version `1.0.0`, places it in `Kernels.Meta_Cognition`, assigns priority `9`, marks it required, names Trang Phan as Origin Architect, and binds it to `Law_of_Law`, `Rule_of_2`, `Rule_of_4`, and `Absolute_Integrity`. Its explicit dependencies are `Meta_Logic_Kernel`, `Meta_Epistemology_Kernel`, and `Probability_Statistics_Kernel`. 

The Omni kernel independently places `Counterfactual_Reasoning_Kernel` in the meta-cognition stack alongside Meta Epistemology, Meta Ontology, Meta Logic, Cognitive Compression, Analogy/Abstraction, and Multi-Perspective Reasoning. Its blueprint is marked `defined`. 

---

# 1. PURPOSE

`K_COUNTERFACTUAL` governs disciplined reasoning about worlds that differ from actuality.

Its historical purpose is to support:

* what-if analysis;
* alternative-scenario reasoning;
* reasoning about events that did not happen;
* hypothetical reasoning;
* scenario analysis;
* causal inference through comparison of actual and hypothetical states. 

The fundamental distinction is:

```text
ACTUAL WORLD
    ≠
COUNTERFACTUAL WORLD
    ≠
PREDICTION
    ≠
EMPIRICALLY OBSERVED OUTCOME
```

A counterfactual describes what a model supports under an intervention.

It does **not** establish that the hypothetical event occurred.

It does **not** automatically establish that the hypothetical event will occur.

It does **not** establish causation merely because an alternative scenario can be narrated coherently.

---

# 2. DOMAIN

Historical source:

```yaml
domains:
  - counterfactual
  - what_if
  - alternative_scenarios
  - causal_inference
  - hypothetical_reasoning
  - scenario_analysis
```



Operationally, the kernel therefore sits at the boundary between:

```text
ACTUAL STATE
      ↓
CAUSAL / STRUCTURAL MODEL
      ↓
INTERVENTION
      ↓
ALTERNATIVE STATE
      ↓
COMPARISON
      ↓
DECISION / EXPLANATION / PREPARATION
```

---

# 3. CORE COUNTERFACTUAL TYPES

The historical kernel defines four types. 

## 3.1 Past counterfactual

Form:

```text
What would have happened
if some past condition had been different?
```

Example structure:

```text
Actual history:
    X = x
    ↓
    Y = y

Counterfactual intervention:
    X := x'

Question:
    Y under X := x' = ?
```

Symbolically:

[
Y_{do(X=x')}
]

The kernel must preserve as much of the actual historical state as possible while changing the requested condition and whatever consequences legitimately follow from it.

---

# 4. FUTURE COUNTERFACTUAL

Form:

```text
What could happen
if a future condition changes?
```

A future counterfactual is not automatically a forecast.

Instead:

```text
Current State
      +
Potential Intervention
      +
System Model
      +
Uncertainty
      ↓
Possible Future State(s)
```

The correct output may therefore be:

```yaml
outcomes:
  - scenario_A
  - scenario_B
  - scenario_C

state: COMPETING
```

rather than one falsely precise prediction.

---

# 5. STRUCTURAL COUNTERFACTUAL

Form:

```text
Given this system structure,
what happens under different conditions?
```

Structural counterfactual reasoning examines:

```text
architecture
constraints
dependencies
capacity
thresholds
feedback
bottlenecks
coupling
system reactions
```

Example:

```text
Observed system:
    load = L
    architecture = A

Intervention:
    load := 2L

Question:
    what does A imply under 2L?
```

Structural resemblance alone does not establish causal equivalence.

---

# 6. CAUSAL COUNTERFACTUAL

Historical formulation:

```text
Compare what happened
with what would have happened
without the candidate cause.
```



Operational form:

```text
Actual:
    X occurred
    Y occurred

Counterfactual:
    remove/change X

Evaluate:
    does Y change?
```

But:

```text
Y changes in model
        ≠
causal relationship empirically proven
```

A causal counterfactual requires an adequate causal model.

---

# 7. VALID COUNTERFACTUAL CRITERIA

The historical kernel defines five validity criteria. 

## 7.1 Plausible initial state

```text
Counterfactual starting state
must be plausible
OR
explicitly labeled implausible.
```

Operational invariant:

```text
plausible(CF₀)
OR
class(CF₀) = IMPLAUSIBLE_EXPLORATION
```

An implausible counterfactual can still be useful for boundary exploration, but its epistemic class cannot silently become realistic.

---

# 8. MINIMAL CHANGE PRINCIPLE

Historical rule:

> Change only what is necessary for the counterfactual; do not silently change other things. 

Operationalization:

[
CF^* =
\arg\min_{CF}
D(CF,A)
]

subject to:

[
I(CF)=true
]

and:

[
CF \models M
]

where:

```text
A  = actual state
CF = counterfactual state
I  = requested intervention
M  = accepted causal/structural model
D  = distance from actuality
```

Therefore:

```text
Change requested variable
        ↓
propagate required consequences
        ↓
do not modify unrelated variables
```

---

# 9. CAUSAL CHAIN CONSERVATION

Historical criterion:

> Respect causal structure: if A causes B causes C, changing A propagates through B to C. 

Thus:

```text
A → B → C
```

with:

```text
do(A := A')
```

requires evaluation of:

```text
B'
↓
C'
```

The kernel may not arbitrarily jump:

```text
A' → C'
```

while ignoring load-bearing intermediate mechanisms unless the model independently licenses that shortcut.

---

# 10. UNCERTAINTY PROPORTIONALITY

Historical source states that farther counterfactuals require greater uncertainty and that near-counterfactuals are more reliable than distant ones. 

Core monotonicity constraint:

[
D(CF,A)\uparrow
\Rightarrow
C_{\max}(CF)\not\uparrow
]

without new independent evidence.

Conceptually:

```text
NEAR COUNTERFACTUAL
small intervention
few changed mechanisms
same regime
short temporal distance
        ↓
potentially tighter uncertainty

FAR COUNTERFACTUAL
many changes
different regime
long causal chain
large structural departure
        ↓
larger uncertainty
```

---

# 11. ASSUMPTION TRANSPARENCY

Historical rule:

> All assumptions about how the world would differ must be explicit. 

Therefore every consequential counterfactual should expose:

```yaml
assumptions:
  - assumption
  - assumption
  - assumption
```

Load-bearing assumptions must never disappear into fluent prose.

---

# 12. HISTORICAL CORE RULES

The source defines four explicit rules. 

```yaml
counterfactual_needs_causal_model:
  rule: >
    Valid counterfactual reasoning requires a causal model
    of how relevant variables are connected.
  failure:
    UNKNOWN/GAP

uncertainty_grows_with_distance:
  rule: >
    Increasing distance from actuality increases the
    required uncertainty envelope.

minimal_intervention:
  rule: >
    Change only what is specified plus consequences
    licensed by the model.

counterfactual_is_not_prediction:
  rule: >
    Counterfactual analysis explores alternatives.
    It must not be represented as prediction merely
    because it concerns another possible state.
```

---

# 13. ACTUAL-STATE MODEL

A counterfactual cannot be stronger than its baseline.

Derived normalized representation:

```yaml
ActualState:
  state_id: string

  observations: []
  source_claims: []
  derived_claims: []

  variables: {}

  scope:
    system: null
    population: null
    environment: null
    scale: null

  temporal:
    observed_at: null
    freshness: null

  regime: null

  provenance: []

  uncertainty: {}
```

If the actual baseline itself is uncertain, the counterfactual inherits that uncertainty.

---

# 14. INTERVENTION MODEL

```yaml
Intervention:
  intervention_id: string

  type:
    - past
    - future
    - structural
    - causal

  target_variables: []

  before: {}
  after: {}

  explicit_changes: []

  auxiliary_changes: []

  justification: []

  hidden_changes_allowed: false
```

Invariant:

[
Changes(CF)
\subseteq
I \cup Descendants_M(I) \cup ExplicitAuxiliary
]

---

# 15. CAUSAL MODEL

```yaml
CausalModel:
  model_id: string

  nodes: []

  edges:
    - source
    - target
    - relation
    - confidence
    - provenance

  relation_types:
    - causal_effect
    - mechanism
    - enabling_condition
    - necessary_condition
    - sufficient_condition
    - mediation
    - confounding
    - feedback
    - association
    - correlation
```

The last two categories do not independently license causal attribution.

---

# 16. CAUSAL FIREWALL

Later AMOS lineage strengthens the historical causal-model requirement.

```yaml
association:
  causal_license: false

correlation:
  causal_license: false

sequence:
  causal_license: false

structural_similarity:
  causal_license: false

mechanism:
  causal_license: CONDITIONAL

enabling_condition:
  causal_license: CONDITIONAL

necessary_condition:
  causal_license: CONDITIONAL

sufficient_condition:
  causal_license: CONDITIONAL

mediation:
  causal_license: CONDITIONAL

confounding:
  effect: BLOCK_NAIVE_ATTRIBUTION

feedback:
  effect: REQUIRE_DYNAMIC_REASONING

causal_effect:
  causal_license: SUPPORTED_ONLY_WITH_ADEQUATE_EVIDENCE
```

This section is a **v4.4 lineage normalization**, not claimed as verbatim historical v1.0.0 text.

---

# 17. EVIDENCE TYPOLOGY

Counterfactual reasoning must preserve evidence class.

```yaml
SOURCE_CLAIM:
  meaning: reported by source

OBSERVATION:
  meaning: directly observed/recorded evidence

DERIVED:
  meaning: inferred from premises

MODEL:
  meaning: model-generated representation

DECISION:
  meaning: selected action/judgment

UNKNOWN:
  meaning: evidence or model insufficient
```

Forbidden transformation:

```text
MODEL
↓
OBSERVATION
```

without empirical validation.

Likewise:

```text
SOURCE_CLAIM
↓
VERIFIED FACT
```

requires appropriate validation.

---

# 18. PROVENANCE TOPOLOGY

Evidence independence must be demonstrated rather than inferred from source count.

Example:

```text
Source A
 ├── Article B
 ├── Summary C
 └── Database D
```

is one ancestry family, not three independent confirmations.

Counterfactual confidence therefore depends on:

```text
evidence quality
+
model quality
+
provenance independence
+
scope compatibility
+
regime compatibility
+
freshness
```

---

# 19. CONSTRUCT_COUNTERFACTUAL

Historical function contract: 

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

Operational form:

```text
construct_counterfactual(A, I, M, P):

    validate A

    validate I

    determine counterfactual type

    if causal inference required:
        verify M is sufficient

    if M insufficient:
        return UNKNOWN/GAP

    CF := copy(A)

    apply explicit I

    affected :=
        causal descendants of I

    propagate consequences through M

    detect system reactions

    detect feedback

    expose all assumptions

    evaluate plausibility against P

    generate materially distinct alternatives

    calculate uncertainty envelope

    enforce confidence ceiling

    return:
        CF
        causal_chain
        uncertainty
        assumptions
        plausibility
        alternatives
```

---

# 20. PROPAGATION

Given:

```text
X → A
X → B
A → C
B → C
C → Y
```

intervention:

```text
do(X := X')
```

requires:

```text
X'
├── A'
│    └── C'
└── B'
     └── C'
          ↓
          Y'
```

The kernel must not assume independent branches if they share causal ancestry.

---

# 21. SYSTEM REACTIONS

Historical source explicitly identifies ignoring system reactions as an error. 

Therefore:

```text
Intervention
     ↓
direct consequence
     ↓
system adaptation
     ↓
secondary consequence
     ↓
feedback
     ↓
new equilibrium / dynamic trajectory
```

must be considered where material.

A static model is insufficient when the actual system is adaptive.

---

# 22. COMPARE_ACTUAL_VS_COUNTERFACTUAL

Historical contract: 

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

Define:

[
\Delta Y = Y_A - Y_{CF}
]

But:

[
\Delta Y \neq causal\ effect
]

by definition.

Causal attribution additionally requires sufficient support for:

```text
intervention validity
causal-model validity
confounding treatment
mechanism
scope compatibility
regime compatibility
provenance independence
```

---

# 23. ATTRIBUTION CONFIDENCE

Derived operational ceiling:

[
C_{attrib}
\leq
\min(
C_I,
C_M,
C_C,
C_P,
C_S,
C_R,
C_T
)
]

where:

```text
C_I = intervention validity
C_M = causal-model validity
C_C = confounding treatment
C_P = provenance independence
C_S = scope compatibility
C_R = regime compatibility
C_T = temporal validity
```

This follows the v4.4 rule that derived confidence cannot exceed the weakest load-bearing premise unless that premise is independently revalidated.

---

# 24. SCENARIO_ANALYSIS

Historical function:

```yaml
scenario_analysis:
  description: >
    Analyze multiple future counterfactual scenarios.
```

The surviving source has malformed serialization around the `inputs` key, but the intended input list is recoverable from the text. This correction is therefore **DERIVED**, not silently promoted to verbatim source. 

Corrected operational contract:

```yaml
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

---

# 25. MULTI-SCENARIO EXECUTION

```text
CURRENT STATE
      │
      ├── Intervention A
      │       ↓
      │    Scenario A
      │
      ├── Intervention B
      │       ↓
      │    Scenario B
      │
      └── Intervention C
              ↓
           Scenario C
```

For each branch:

```text
construct
→ propagate
→ react
→ assess plausibility
→ expose assumptions
→ quantify uncertainty if justified
→ evaluate decision implications
```

Then compare branches.

---

# 26. PROBABILITY FIREWALL

Historical output says:

```text
probability_assignments_if_available
```

not:

```text
probability_assignments_required
```



Therefore probability must not be fabricated merely because scenario analysis benefits from numbers.

Correct behavior:

```yaml
if_probability_model_supported:
  probability: value

else:
  probability: UNKNOWN
  ranking: optional
  qualitative_uncertainty: explicit
```

---

# 27. COMPETING HYPOTHESES

A later AMOS v4.4 integration requires preservation of genuine competing explanations.

Suppose:

```text
H1:
X causes Y

H2:
Z causes both X and Y

H3:
X enables Y only under regime R

H4:
observed X/Y relationship is incidental
```

If available evidence cannot discriminate them:

```yaml
state: COMPETING
```

The kernel must not collapse them into one explanation for narrative convenience.

---

# 28. DISCRIMINATING TEST

When competing models materially affect the decision:

[
Test^*
======

\arg\max_T
\frac{
ExpectedDecisionInformation(T)
}{
ExpectedCost(T)
}
]

subject to:

```text
safety
legality
reversibility
governance
resource constraints
```

The preferred test attacks the smallest uncertainty capable of changing the decision.

---

# 29. SENSITIVITY

For consequential counterfactuals:

```yaml
sensitivity:
  smallest_flip_premise: null
  smallest_flip_threshold: null
  smallest_flip_observation: null
  fragile_assumption: null
```

Decision rule:

```text
if plausible perturbation flips result:
    conclusion = CONDITIONAL
```

A robust conclusion should survive reasonable variation in noncritical assumptions.

---

# 30. COUNTERFACTUAL DISTANCE

The historical kernel specifies the principle but not a numerical metric.

A v4.4-compatible **MODEL** can represent distance as:

[
D_{CF}
======

w_I D_I
+
w_S D_S
+
w_T D_T
+
w_R D_R
+
w_A D_A
]

where:

```text
D_I = intervention distance
D_S = structural distance
D_T = temporal distance
D_R = regime distance
D_A = assumption distance
```

This equation is an operational model, **not recovered historical canon**.

---

# 31. UNCERTAINTY VECTOR

Rather than compressing every uncertainty into one score:

```yaml
uncertainty:
  evidence: U_e
  model: U_m
  scope: U_s
  temporal: U_t
  causal: U_c
  execution: U_x
  provenance_independence: U_p
```

This prevents strong evidence in one dimension from masking a critical weakness in another.

---

# 32. SCOPE FIREWALL

Every consequential counterfactual should inherit an applicability envelope:

```yaml
applicability:
  system_or_population: null
  environment: null
  scale: null
  time: null
  regime: null
  measurement_method: null
  assumptions: []
```

A result established for:

```text
system A
regime R1
scale S1
time T1
```

cannot silently become a conclusion about:

```text
system B
regime R2
scale S2
time T2
```

---

# 33. REGIME SHIFT

If the mechanism changes:

```text
M_R1 ≠ M_R2
```

then:

```text
CF conclusion under R1
```

may no longer be valid under `R2`.

Thus:

```text
regime shift detected
        ↓
inspect validity conditions
        ↓
invalidate affected conclusions
        ↓
preserve unaffected conclusions
```

---

# 34. COMMON ERRORS

The historical source defines five. 

## Over-determination

```text
"Had X changed, Y definitely would have happened."
```

without accounting for other relevant factors.

## Ignoring system reactions

Treating an adaptive system as static.

## Correlation → causation

Assuming:

```text
A before B
```

means:

```text
do(A') → B'
```

## Unrealistic baseline

Comparing against an implausible or cherry-picked alternative.

## Hidden changes

Claiming to alter one condition while silently altering several.

---

# 35. EXTENDED FAILURE TAXONOMY

```yaml
scope_leakage:
  result: CONDITION_OR_INVALIDATE

regime_leakage:
  result: REBUILD

shared_provenance:
  result: DOWNGRADE_INDEPENDENCE

missing_causal_model:
  result: UNKNOWN/GAP

false_probability:
  result: REMOVE_PROBABILITY

counterfactual_as_prediction:
  result: RELABEL

counterfactual_as_fact:
  result: HARD_FAIL

unsupported_precision:
  result: WIDEN_UNCERTAINTY

hidden_intervention:
  result: REJECT_OR_EXPOSE

ignored_feedback:
  result: RECOMPUTE_DYNAMICALLY
```

---

# 36. SAFETY CONSTRAINTS

Historical constraints: 

```yaml
never_present_counterfactual_as_fact: true

never_ignore_uncertainty_in_far_counterfactuals: true

always_state_assumptions_explicitly: true

always_label_counterfactual_as_counterfactual: true

never_use_counterfactual_to_over_determine_outcomes: true
```

These are hard integrity boundaries.

---

# 37. ACTION GOVERNANCE

Counterfactual analysis becomes more demanding as action stakes rise.

Validation should increase with:

```text
irreversibility
financial exposure
legal exposure
health/safety exposure
institutional impact
dependency depth
uncertainty
causal ambiguity
```

Under unresolved uncertainty:

```text
prefer:
    staged
    reversible
    observable
    repairable

over:
    irreversible
    opaque
    high-dependency
    assumption-sensitive
```

---

# 38. ADVERSARIAL VALIDATION

For consequential conclusions, construct two reasoning paths.

## Path A — strongest supported case

```text
actual evidence
→ causal model
→ intervention
→ propagated world
→ outcome
```

## Path B — challenge

Seek:

```text
contradiction
confounder
shared provenance
stale evidence
scope leakage
regime mismatch
hidden intervention
feedback
alternative mechanism
model misspecification
```

Resolution:

```text
challenge succeeds
        ↓
downgrade / condition / compete / invalidate
```

Not:

```text
challenge succeeds
        ↓
ignore challenge
        ↓
retain fluent conclusion
```

---

# 39. LOCAL INVALIDATION

Suppose:

```text
P1 ─┐
    ├→ C1 → C3
P2 ─┘

P3 ─────→ C2
```

If `P2` fails:

```text
invalidate C1
invalidate C3
preserve P1
preserve P3
preserve C2
```

Core rule:

[
Invalid(p)
\Rightarrow
Invalidate(Descendants(p))
]

not:

[
Invalid(p)
\Rightarrow
Invalidate(All)
]

---

# 40. RECOVERY

```text
detect failed premise
        ↓
identify dependency closure
        ↓
invalidate affected descendants
        ↓
rollback to nearest valid state
        ↓
retrieve changed evidence/model
        ↓
reroute locally
        ↓
re-evaluate
```

Do not repeat a failed reasoning path without changed evidence.

---

# 41. RSCF COUNTERFACTUAL CAPSULE

```yaml
CounterfactualProofCapsule:

  claim:
    statement: ""
    class:
      - VERIFIED
      - DERIVED
      - MODEL
      - CONDITIONAL
      - COMPETING
      - UNKNOWN/GAP

  actual_world:
    observations: []
    source_claims: []
    derived_state: []
    provenance: []

  intervention:
    targets: []
    changes: []
    minimality:
      status: PASS|FAIL|UNKNOWN

  causal_model:
    model_id: null
    supported_edges: []
    uncertain_edges: []
    confounders: []
    mediators: []
    feedback_loops: []

  counterfactual_world:
    state: {}
    causal_chain: []
    system_reactions: []

  load_bearing_premises: []

  assumptions: []

  alternative_outcomes: []

  competing_explanations: []

  applicability:
    system: null
    environment: null
    scale: null
    time: null
    regime: null

  freshness:
    validated_at: null
    expires_at: null

  uncertainty:
    evidence: null
    model: null
    scope: null
    temporal: null
    causal: null
    execution: null
    provenance_independence: null

  falsifiers: []

  invalidation_conditions: []

  confidence_ceiling: null
```

This structure is a v4.4-compatible normalization rather than verbatim historical v1.0.0 source.

---

# 42. CONCLUSION CLASSES

```yaml
VERIFIED:
  meaning: >
    Strongly established proposition within its declared
    evidential and applicability envelope.

DERIVED:
  meaning: >
    Follows from supported premises and valid reasoning.

MODEL:
  meaning: >
    Generated by an explicit hypothetical/causal model.

CONDITIONAL:
  meaning: >
    Holds only under identified assumptions or thresholds.

COMPETING:
  meaning: >
    Multiple incompatible alternatives remain live.

UNKNOWN/GAP:
  meaning: >
    Required evidence/model/dependency is missing.
```

Counterfactual outcomes normally begin no stronger than `MODEL` or `DERIVED` within a model unless separately validated.

---

# 43. RUNTIME

```text
INPUT Q

↓
Detect counterfactual intent

↓
Classify:
past / future / structural / causal

↓
Extract actual baseline

↓
Extract explicit intervention

↓
Identify requested outcome or decision

↓
Retrieve load-bearing evidence only

↓
Check causal-model sufficiency

├── insufficient
│      ↓
│   UNKNOWN/GAP
│
└── sufficient
       ↓

Establish scope / regime / freshness

↓
Apply minimal intervention

↓
Propagate causal descendants

↓
Model system reactions

↓
Model feedback where relevant

↓
Generate materially distinct alternatives

↓
Check confounding

↓
Check hidden changes

↓
Evaluate plausibility

↓
Represent uncertainty

↓
Run sensitivity analysis

↓
Run adversarial challenge if consequential

↓
Classify weakest accurate conclusion

↓
OUTPUT
```

---

# 44. FAST PATH

A compact counterfactual may be used only when:

```yaml
dependency_closure: established
provenance_independence: adequate
scope_compatibility: established
regime_compatibility: established
freshness: adequate
material_conflict: absent
causal_coupling: bounded
stakes: low_or_reversible
```

Escalation triggers:

```text
shared ancestry
conflict
stale evidence
cross-regime reasoning
strong causal coupling
ambiguous dependency
irreversible stakes
governance impact
weak causal model
```

---

# 45. HISTORICAL INTEGRATION

Historical source explicitly says the kernel provides to: 

```yaml
provides_to:
  - Meta_Logic_Kernel
  - Multi_Perspective_Reasoning_Kernel
  - Strategy_Game_Engine
  - Risk_Assessment
```

It is used by:

```yaml
used_by:
  - Decision analysis
  - Risk assessment
  - Strategic planning
  - Causal inference
  - Policy evaluation
```

Routing:

```yaml
routes_to:
  default: ROUTE_DEFAULT
  domain_specific: specialized_route
```

---

# 46. META-COGNITION POSITION

The Omni source places:

```text
Meta_Epistemology_Kernel
Meta_Ontology_Kernel
Meta_Logic_Kernel
Cognitive_Compression_Kernel
Analogy_Abstraction_Kernel
Counterfactual_Reasoning_Kernel
Multi_Perspective_Reasoning_Kernel
```

inside the `meta_cognition` component. 

This establishes architectural placement, but not by itself runtime implementation.

---

# 47. EVALUATION

Historical unit tests: 

```yaml
unit_tests:

  - test: past_counterfactual_with_causal_model
    expected:
      - counterfactual_state
      - causal_chain
      - uncertainties

  - test: actual_vs_counterfactual
    expected:
      - difference_analysis
      - causal_attribution
      - confounding_factors

  - test: over_determination_detection
    expected:
      - error_flagged

  - test: three_scenario_analysis
    expected:
      - scenario_outcomes
      - recommended_preparation
```

---

# 48. EXTENDED V4.4 TESTS

```yaml
integrity_tests:

  hidden_change_detection:
    pass_if: >
      undeclared interventions are rejected or surfaced

  causal_firewall:
    pass_if: >
      correlation alone never yields causal attribution

  distance_uncertainty:
    pass_if: >
      unsupported counterfactual distance cannot increase confidence

  competing_preservation:
    pass_if: >
      unresolved incompatible alternatives remain COMPETING

  provenance_sybil:
    pass_if: >
      descendants of one source are not counted as independent evidence

  regime_shift:
    pass_if: >
      conclusions dependent on obsolete regime assumptions are invalidated

  weakest_premise:
    pass_if: >
      derived confidence respects load-bearing confidence ceiling

  local_invalidation:
    pass_if: >
      failed premise invalidates dependent descendants only

  fact_boundary:
    pass_if: >
      hypothetical output never becomes observation
```

---

# 49. HISTORICAL FAILURE MODES

The historical kernel explicitly lists: 

```yaml
failure_modes:
  - Presenting counterfactual as certain prediction
  - Ignoring system reactions to change
  - Over-determining outcome without considering alternatives
  - Hidden multiple changes in counterfactual
```

---

# 50. OUTPUT CONTRACT

Minimal:

```yaml
counterfactual_result:

  label: COUNTERFACTUAL

  type:
    past|future|structural|causal

  intervention: {}

  conclusion:
    class: MODEL
    statement: ""

  assumptions: []

  causal_basis: []

  uncertainty: []
```

Consequential:

```yaml
counterfactual_result:

  label: COUNTERFACTUAL

  actual_baseline: {}

  intervention: {}

  conclusion:
    class:
      DERIVED|MODEL|CONDITIONAL|COMPETING|UNKNOWN/GAP
    statement: ""

  causal_chain: []

  system_reactions: []

  assumptions: []

  competing_outcomes: []

  alternative_explanations: []

  confounders: []

  scope: {}

  regime: {}

  freshness: {}

  uncertainty_vector:
    evidence: null
    model: null
    scope: null
    temporal: null
    causal: null
    execution: null
    provenance_independence: null

  confidence_ceiling: null

  falsifiers: []

  invalidation_conditions: []

  discriminating_test: null

  reversible_action: null
```

---

# 51. STOP CONDITIONS

Counterfactual reasoning stops when additional reasoning no longer materially changes:

```yaml
claim_sufficiency:
  question: >
    Is the conclusion adequately supported and correctly classified?

decision_sufficiency:
  question: >
    Is remaining uncertainty unlikely to change the decision?

action_sufficiency:
  question: >
    Is there a safe, proportionate action under the remaining uncertainty?
```

Completeness is not achieved by generating every imaginable hypothetical world.

It is achieved by resolving the alternatives that can materially change the conclusion or action.

---

# 52. GAP REGISTER

```yaml
gaps:

  - id: CF-G1
    class: DECISION-RELEVANT
    missing:
      exact_original_md/Core/AMOS_Counterfactual_Reasoning_Kernel_v0.md
    status: NOT_DIRECTLY_RECOVERED
    effect: >
      Prevents claiming exact byte/text equivalence between this
      reconstruction and the original source file.

  - id: CF-G2
    class: DECISION-RELEVANT
    missing:
      historical_devin_counterfactual_skill_contents
    status: NOT_DIRECTLY_RECOVERED
    effect: >
      Runtime skill implementation cannot be reconstructed as verified
      implementation solely from the kernel specification.

  - id: CF-G3
    class: EXPLANATORY
    missing:
      exact_executable_v1_0_0_implementation
    status: UNKNOWN
    effect: >
      Historical specification does not prove executable realization.

  - id: CF-G4
    class: EXPLANATORY
    missing:
      explicit_supersession_record_v1_to_current_K_COUNTERFACTUAL
    status: UNKNOWN
```

---

# 53. SOURCE / EXTENSION BOUNDARY

## SOURCE-SUPPORTED HISTORICAL SPINE

Directly supported by the recovered historical source:

```text
Counterfactual_Reasoning_Kernel
version 1.0.0
Meta_Cognition
priority 9
required true
dependencies
binding rules
four counterfactual types
five validity criteria
five common errors
four core rules
three functions
function inputs/outputs
integration
safety constraints
unit tests
failure modes
```



## INDEPENDENT ARCHITECTURAL CORROBORATION

The Omni kernel independently supports the existence and meta-cognition placement of `Counterfactual_Reasoning_Kernel`, with its blueprint marked `defined`. 

## V4.4 LINEAGE EXTENSIONS

The following portions of this reconstructed `K_COUNTERFACTUAL` are normalization/extensions rather than claimed verbatim historical v1.0.0 content:

```text
RSCF proof capsule
typed evidence topology
provenance-independence firewall
scope/regime firewall
uncertainty vector
confidence ceiling
counterfactual-distance equation
competing-hypothesis state
discriminating-test optimization
sensitivity/flip analysis
adversarial validation
local invalidation
fast path
action governance
expanded runtime/output contracts
```

---

# 54. CANONICAL K_COUNTERFACTUAL CONTRACT

```yaml
K_COUNTERFACTUAL:

  mission: >
    Construct, propagate, compare, and evaluate minimally changed
    hypothetical worlds without confusing hypothetical states with
    observed reality, prediction, or unsupported causal claims.

  historical_kernel:
    id: Counterfactual_Reasoning_Kernel
    version: "1.0.0"
    category: Meta_Cognition
    priority: 9
    required: true

  dependencies:
    - Meta_Logic_Kernel
    - Meta_Epistemology_Kernel
    - Probability_Statistics_Kernel

  counterfactual_types:
    - past
    - future
    - structural
    - causal

  hard_invariants:

    - COUNTERFACTUAL_NEVER_EQUALS_FACT

    - CAUSAL_ATTRIBUTION_REQUIRES_CAUSAL_MODEL

    - APPLY_MINIMAL_INTERVENTION

    - PRESERVE_CAUSAL_CHAIN

    - EXPOSE_ASSUMPTIONS

    - MODEL_SYSTEM_REACTIONS

    - PRESERVE_MATERIAL_ALTERNATIVES

    - DO_NOT_INFER_CAUSATION_FROM_CORRELATION

    - DO_NOT_HIDE_CO_INTERVENTIONS

    - UNCERTAINTY_MUST_REFLECT_COUNTERFACTUAL_DISTANCE

    - CONFIDENCE_CANNOT_EXCEED_LOAD_BEARING_SUPPORT

    - PRESERVE_SCOPE_AND_REGIME

    - PRESERVE_PROVENANCE_TOPOLOGY

    - INVALIDATE_DEPENDENT_DESCENDANTS_ONLY

  functions:

    construct_counterfactual:
      in:
        - actual_state
        - intervention_description
        - causal_model
        - plausibility_constraints

      out:
        - counterfactual_state
        - causal_chain
        - uncertainties
        - assumption_list
        - plausibility_assessment
        - alternative_outcomes

    compare_actual_vs_counterfactual:
      in:
        - actual_outcome
        - counterfactual_outcome
        - causal_model
        - confidence_levels

      out:
        - difference_analysis
        - causal_attribution
        - confounding_factors
        - attribution_confidence
        - alternative_explanation

    scenario_analysis:
      in:
        - current_state
        - scenario_list
        - uncertainty_model
        - decision_criteria

      out:
        - scenario_outcomes
        - probability_assignments_if_available
        - recommended_preparation
        - early_warning_signals
        - scenario_comparison

  conclusion_classes:
    - VERIFIED
    - DERIVED
    - MODEL
    - CONDITIONAL
    - COMPETING
    - UNKNOWN/GAP

  escalation:
    when:
      - provenance_dependency
      - contradiction
      - stale_evidence
      - regime_shift
      - causal_ambiguity
      - hidden_dependency
      - irreversible_stakes
      - governance_impact

  recovery:
    principle: >
      Invalidate the failed premise and dependent descendants,
      preserve unaffected work, then reroute from the nearest
      valid state.

  stop:
    - CLAIM_SUFFICIENCY
    - DECISION_SUFFICIENCY
    - ACTION_SUFFICIENCY
```

# 55. FINAL INVARIANT

[
\boxed{
\text{Counterfactual quality}
\neq
\text{narrative plausibility}
}
]

The governing relation is instead:

[
\boxed{
Q_{CF}
======

f(
A,,
I,,
M,,
P,,
S,,
R,,
T,,
U
)
}
]

where:

```text
A = integrity of actual baseline
I = intervention validity/minimality
M = causal-model support
P = provenance quality and independence
S = scope compatibility
R = regime compatibility
T = temporal validity/freshness
U = explicit uncertainty
```

And the confidence ceiling remains:

[
\boxed{
C_{CF}
\leq
\min(C_{\text{load-bearing premises}})
}
]

unless the weak premise is independently revalidated.

**`K_COUNTERFACTUAL` therefore exists to explore alternatives without allowing hypothetical reasoning to outrun evidence, causality, provenance, scope, or uncertainty.**
