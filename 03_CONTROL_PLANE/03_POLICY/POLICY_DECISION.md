Below is the **full paste-ready `K_COUNTERFACTUAL` artifact**, not a placeholder. I’m keeping a strict provenance boundary: the historical Drive artifact explicitly defines `Counterfactual_Reasoning_Kernel` v1.0.0 as required Meta-Cognition logic, with four counterfactual types, five validity criteria, three core functions, safety constraints, tests, and dependencies on Meta Logic, Meta Epistemology, and Probability/Statistics.  The expanded v4.4 portions below are therefore marked as normalized/integrated specification rather than misrepresented as verbatim historical canon.

---
artifact_id: AMOS-OS-K-COUNTERFACTUAL
canonical_name: K_COUNTERFACTUAL
title: K COUNTERFACTUAL
artifact_class: KERNEL
kernel_family: META_COGNITION
plane: KERNEL

origin_architect: Trang Phan
steward: Trang Phan

amos_core_target: v4.4

status: CANDIDATE_CANON
conclusion_class: DERIVED

historical_kernel:
  kernel_id: Counterfactual_Reasoning_Kernel
  version: "1.0.0"
  category: Meta_Cognition
  priority: 9
  required: true
  historical_status: defined

supersedes:
  - K_COUNTERFACTUAL_PLACEHOLDER

implementation_status: UNKNOWN/GAP
empirical_validation_status: UNKNOWN/GAP
formal_verification_status: UNKNOWN/GAP
promotion_required: true

updated: 2026-08-26
---

# K COUNTERFACTUAL

> STATUS: `CANDIDATE_CANON`
>
> CONCLUSION CLASS: `DERIVED`
>
> AMOS CORE TARGET: `v4.4`
>
> ORIGIN ARCHITECT: `Trang Phan`
>
> SUPERSEDES: `K_COUNTERFACTUAL PLACEHOLDER`

# 0. PURPOSE

`K_COUNTERFACTUAL` is the AMOS OS kernel for disciplined reasoning about
alternative states of reality.

It governs reasoning of the form:

- What would have happened if X had been different?
- What could happen if X changes?
- What would happen under a different system condition?
- Would Y still have occurred without X?
- Is X necessary for Y?
- Is X sufficient for Y?
- What causal information can be obtained by comparing actuality with a
  hypothetical alternative?
- Which intervention is most likely to alter an outcome?
- Which assumptions determine the counterfactual result?
- Which competing causal explanation survives intervention?
- What observation could discriminate between competing models?

The kernel exists to prevent hypothetical reasoning from silently becoming:

- invented fact;
- unsupported prediction;
- causal overclaim;
- hidden multi-variable intervention;
- false probability;
- false precision;
- unbounded scenario generation;
- scope leakage;
- regime leakage;
- provenance laundering;
- decision authority.

The fundamental object is:

    ACTUAL WORLD
          ↓
    EXPLICIT INTERVENTION
          ↓
    CAUSAL / STRUCTURAL MODEL
          ↓
    COUNTERFACTUAL WORLD
          ↓
    COMPARISON
          ↓
    UNCERTAINTY
          ↓
    CONCLUSION

The counterfactual world remains epistemically distinct from the actual world.

# 1. HISTORICAL AMOS CONTRACT

The historical AMOS kernel defines:

    kernel_id = Counterfactual_Reasoning_Kernel
    version   = 1.0.0
    category  = Meta_Cognition
    priority  = 9
    required  = true

Historical domains:

    counterfactual
    what_if
    alternative_scenarios
    causal_inference
    hypothetical_reasoning
    scenario_analysis

Historical dependencies:

    Meta_Logic_Kernel
    Meta_Epistemology_Kernel
    Probability_Statistics_Kernel

Historical binding rules:

    Law_of_Law
    Rule_of_2
    Rule_of_4
    Absolute_Integrity

This v4.4 artifact preserves that spine while integrating it with the later
AMOS integrity, provenance, RSCF, H/M/L, causal-regime, and governed-evolution
architecture.

# 2. EPISTEMIC FIREWALL

Hard distinctions:

    COUNTERFACTUAL != FACT

    HYPOTHETICAL != OBSERVATION

    MODEL != OBSERVATION

    SOURCE_CLAIM != VERIFIED

    ASSOCIATION != CAUSATION

    CORRELATION != CAUSATION

    TEMPORAL PRECEDENCE != CAUSATION

    PREDICTION != INTERVENTION

    INTERVENTION != COUNTERFACTUAL

    SIMULATION != EMPIRICAL VALIDATION

    PLAUSIBILITY != PROBABILITY

    PROBABILITY != CERTAINTY

    MODEL AGREEMENT != INDEPENDENT EVIDENCE

    STRUCTURAL SIMILARITY != CAUSAL EQUIVALENCE

Therefore a counterfactual result normally carries one of:

    DERIVED
    MODEL
    CONDITIONAL
    COMPETING
    UNKNOWN/GAP

A stronger classification requires independent validation appropriate to the
claim.

# 3. HISTORICAL COUNTERFACTUAL TYPES

AMOS recognizes four primary counterfactual types.

## 3.1 PAST COUNTERFACTUAL

Question:

    What would have happened if something in the past
    had been different?

Structure:

    ACTUAL HISTORY
          ↓
    DIVERGENCE POINT
          ↓
    ALTERNATIVE EVENT
          ↓
    CAUSAL PROPAGATION
          ↓
    ALTERNATIVE HISTORY

Schema:

    PastCounterfactual:
      actual_history
      divergence_time
      intervention
      preserved_history
      affected_dependencies
      alternative_trajectory
      queried_outcome
      assumptions
      uncertainty

Default rule:

    HISTORY BEFORE DIVERGENCE
    REMAINS FACTUAL

unless the intervention explicitly changes an earlier state.

## 3.2 FUTURE COUNTERFACTUAL

Question:

    What could happen if something changes in the future?

Structure:

    CURRENT STATE
         ↓
    PROPOSED INTERVENTION
         ↓
    RESPONSE
         ↓
    ADAPTATION
         ↓
    POSSIBLE FUTURE STATES

Schema:

    FutureCounterfactual:
      current_state
      intervention
      intervention_time
      horizon
      causal_model
      system_response
      scenarios
      uncertainty
      early_warning_signals

A future counterfactual is not automatically a forecast.

## 3.3 STRUCTURAL COUNTERFACTUAL

Question:

    What does the system structure imply would happen
    under different conditions?

Schema:

    StructuralCounterfactual:
      factual_structure
      structural_intervention
      preserved_mechanisms
      changed_mechanisms
      constraints
      feedback
      thresholds
      regime
      resulting_structure

Structural interventions may alter dependency topology itself.

They therefore require deeper validation than simple parameter changes.

## 3.4 CAUSAL COUNTERFACTUAL

Question:

    What can be inferred about causation by comparing
    what happened with what would have happened
    under another intervention?

Schema:

    CausalCounterfactual:
      factual_cause
      factual_outcome
      alternative_intervention
      alternative_outcome
      causal_model
      confounders
      mediators
      moderators
      competing_explanations
      attribution_confidence

# 4. VALID COUNTERFACTUAL CRITERIA

The historical kernel establishes five load-bearing criteria.

## 4.1 PLAUSIBLE INITIAL STATE

The counterfactual starting point must be:

    PLAUSIBLE

or explicitly marked:

    IMPLAUSIBLE
    MODEL-ONLY
    STRESS-TEST
    UNKNOWN

The kernel must not smuggle an impossible initial state into a seemingly
realistic conclusion.

## 4.2 MINIMAL CHANGE PRINCIPLE

Change only what is necessary for the counterfactual.

Do not silently modify unrelated variables.

## 4.3 CAUSAL CHAIN CONSERVATION

If:

    A → B → C

then an intervention on A should normally propagate through:

    A'
     ↓
    B'
     ↓
    C'

rather than jumping directly from A' to C' without an independently supported
direct path.

## 4.4 UNCERTAINTY PROPORTIONAL TO DISTANCE

Near counterfactuals generally require fewer assumptions than far
counterfactuals.

Therefore:

    COUNTERFACTUAL DISTANCE ↑
              ⇒
    UNCERTAINTY SHOULD NOT DECREASE
    WITHOUT NEW INFORMATION

This is a qualitative integrity constraint, not a universal numerical law.

## 4.5 ASSUMPTION TRANSPARENCY

Every load-bearing assumption must be exposed.

Hidden assumptions cannot silently function as evidence.

# 5. COUNTERFACTUAL OBJECT

Normalized v4.4 representation:

    CF = <F, I, M, E, C, Q, S, R, T, P, U, A>

where:

    F = factual anchor
    I = intervention
    M = causal / structural model
    E = evidence
    C = counterfactual state
    Q = queried outcome
    S = scope
    R = regime
    T = temporal envelope
    P = provenance topology
    U = uncertainty
    A = assumptions

A decision-grade counterfactual requires each load-bearing component to be:

    KNOWN

    EXPLICITLY MODELED

or

    UNKNOWN/GAP

Missing structure must not be filled with fluent speculation.

# 6. FACTUAL ANCHOR

Every counterfactual begins with an actual-state anchor.

    FactualAnchor:

      anchor_id

      system
      entity
      population
      environment

      observed_state

      observations

      source_claims

      derived_state

      temporal:
        observed_at
        valid_from
        valid_until

      scope

      regime

      measurement_method

      provenance

      uncertainty

      contradictions

Hard law:

    NO DEFENSIBLE FACTUAL ANCHOR
              ↓
    NO DECISION-GRADE COUNTERFACTUAL

# 7. ACTUAL / COUNTERFACTUAL SEPARATION

World topology:

    W0 = ACTUAL WORLD

    W0
    ├── CF1
    ├── CF2
    ├── CF3
    └── CFn

A branch does not mutate its factual parent.

Invariant:

    FACTUAL PARENT MUST REMAIN RECOVERABLE

Forbidden transition:

    COUNTERFACTUAL
          ↓
    MEMORY / SUMMARY
          ↓
    FACT

without independent observation.

# 8. INTERVENTION

An intervention explicitly modifies one or more components of the factual or
modeled world.

    Intervention:

      intervention_id

      type:
        VALUE_CHANGE
        ACTION_ADDITION
        ACTION_REMOVAL
        ACTION_SUBSTITUTION
        TIMING_CHANGE
        ORDER_CHANGE
        INFORMATION_CHANGE
        BELIEF_CHANGE
        POLICY_CHANGE
        RESOURCE_CHANGE
        PARAMETER_CHANGE
        STRUCTURAL_CHANGE
        ENVIRONMENT_CHANGE
        CONSTRAINT_CHANGE
        EVENT_INJECTION
        EVENT_REMOVAL

      target

      factual_value

      counterfactual_value

      intervention_time

      duration

      magnitude

      scope

      explicit_auxiliary_changes

      assumptions

# 9. INTERVENTION BINDING

A materially consequential intervention should bind:

    TARGET
    ORIGINAL VALUE
    ALTERNATIVE VALUE
    MAGNITUDE
    TIME
    DURATION
    SCOPE
    ENVIRONMENT
    REGIME

Example:

    "What if investment increases?"

may be underdetermined.

Decision-relevant missing fields may include:

    investment in what?
    increase by how much?
    when?
    for how long?
    funded from where?
    under what market conditions?
    what other constraints remain fixed?

If unresolved values can flip the result:

    CONDITIONAL

or:

    UNKNOWN/GAP

is required.

# 10. MINIMAL INTERVENTION

Let:

    Changed(CF)

denote all variables that differ from actuality.

Then the default integrity condition is:

    Changed(CF)
      ⊆
    DeclaredIntervention
      ∪
    LicensedCausalDescendants
      ∪
    ExplicitAuxiliaryChanges

Any unexplained alteration is:

    E_CF_HIDDEN_CHANGE

# 11. MINIMAL SURGERY FORMALIZATION

For structural equations:

    Vi = fi(PAi, Ui)

an intervention:

    do(X = x')

conceptually replaces the generating mechanism for X with:

    X := x'

while preserving unaffected mechanisms.

Thus:

    M =
    {f1, f2, ..., fX, ..., fn}

becomes:

    MI =
    {f1, f2, ..., X:=x', ..., fn}

unless additional structural changes are explicitly declared.

This is a formal specification pattern.

It is not a claim that every AMOS runtime literally executes a structural
causal model implementation.

# 12. HIDDEN CO-INTERVENTION

Suppose:

    X := x'

is declared.

But the generated scenario also changes:

    Z := z'

Then Z's change must be classified as:

    CAUSALLY_ENTAILED

    SYSTEM_REACTION

    EXPLICIT_AUXILIARY_INTERVENTION

or:

    HIDDEN_CHANGE

`HIDDEN_CHANGE` invalidates the branch until corrected.

# 13. CAUSAL MODEL REQUIREMENT

Historical AMOS rule:

    VALID COUNTERFACTUAL REASONING
    REQUIRES A CAUSAL MODEL
    OF HOW RELEVANT THINGS ARE CONNECTED.

Without adequate causal structure, the output is speculative.

Normalized representation:

    CausalModel:

      model_id
      version
      causal_epoch

      nodes

      edges:
        source
        target
        relation_type
        evidence
        provenance
        scope
        regime
        freshness
        confidence
        falsifier

      exogenous_variables

      endogenous_variables

      assumptions

      validity_envelope

      competing_models

# 14. CAUSAL RELATION TYPES

AMOS must distinguish:

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

These are not interchangeable.

# 15. CAUSAL FIREWALL

Forbidden:

    A happened before B
          ↓
    A caused B

Forbidden:

    A correlates with B
          ↓
    changing A changes B

Forbidden:

    A resembles C
          ↓
    A and C share causal behavior

Forbidden:

    model predicts Y
          ↓
    Y certainly occurs

Forbidden:

    source says X caused Y
          ↓
    causal relation verified

Causal inference requires appropriately typed evidence.

# 16. OBSERVATION / INTERVENTION / COUNTERFACTUAL

Observational quantity:

    P(Y | X=x)

Interventional quantity:

    P(Y | do(X=x))

Counterfactual quantity:

    P(Yx' | X=x, Y=y, E=e)

These answer different questions.

AMOS must not silently substitute one level for another.

# 17. ABDUCTION

Given evidence:

    E = e

infer plausible background or latent states:

    P(U | E=e, M)

where probabilistic semantics are justified.

If several latent states remain materially possible:

    U1
    U2
    U3

preserve them.

Do not silently choose whichever latent state produces the preferred
counterfactual.

# 18. ACTION

Apply the intervention:

    MI = Intervene(M, I)

Only explicitly licensed intervention semantics may alter the causal model.

# 19. PROJECTION

Propagate the modified model.

Conceptually:

    YCF = Predict(MI, U)

or, where probabilistically justified:

    P(YCF)
      =
    ΣU P(YCF | U, MI) P(U | E)

If probability semantics are not justified, return:

    possible outcomes
    ordering
    qualitative likelihood
    bounds
    or UNKNOWN

rather than invented numerical probability.

# 20. CORE RUNTIME

    FACTUAL STATE
          ↓
    ABDUCTION
          ↓
    BACKGROUND STATE
          ↓
    INTERVENTION
          ↓
    MODIFIED MODEL
          ↓
    CAUSAL PROPAGATION
          ↓
    SYSTEM RESPONSE
          ↓
    COUNTERFACTUAL STATE
          ↓
    UNCERTAINTY
          ↓
    ADVERSARIAL VALIDATION
          ↓
    CONCLUSION

# 21. CAUSAL CHAIN CONSERVATION

Given:

    A → B → C → D

intervening on A requires evaluating affected descendants:

    A'
     ↓
    B'
     ↓
    C'
     ↓
    D'

unless an edge is independently shown to be irrelevant or blocked.

The kernel must not skip B and C merely because D is the queried outcome.

# 22. DEPENDENCY CLOSURE

Define:

    Closure(I,Q)

as the smallest set of variables, mechanisms, premises, evidence, and
dependencies capable of changing the answer to query Q under intervention I.

Example:

    X → A → B → Y

requires consideration of:

    X
    A
    B
    Y

but an independently irrelevant Z need not be loaded.

This implements the v4.4 smallest-sufficient-proof principle.

# 23. CAUSAL CLOSURE FAILURE

If:

    X → ? → Y

contains an unknown load-bearing mechanism:

    DO NOT INVENT THE EDGE.

Return:

    UNKNOWN/GAP

or, if an explicit hypothetical assumption is useful:

    CONDITIONAL

with that assumption exposed.

# 24. CONFOUNDING

Pattern:

        Z
       / \
      ↓   ↓
      X   Y

may create observed association between X and Y without:

    X → Y

Track:

    confounding:
      known
      suspected
      unresolved
      ruled_out

Material unresolved confounding caps causal attribution.

# 25. MEDIATION

For:

    X → M → Y

the following interventions differ:

    CHANGE X
    AND ALLOW M TO RESPOND

versus:

    CHANGE X
    WHILE HOLDING M FIXED

They represent different counterfactual worlds.

AMOS must preserve the distinction.

# 26. MODERATION

If:

    Effect(X → Y | Z=z1)
        !=
    Effect(X → Y | Z=z2)

then Z is decision-relevant.

The conclusion inherits the condition.

# 27. NECESSITY

Question:

    Would Y have occurred without X?

Compare:

    Yx

with:

    Yx'

where x' removes or changes X.

Necessity is always bounded by:

    model
    scope
    regime
    time
    assumptions

# 28. SUFFICIENCY

Question:

    Would introducing X be enough to produce Y?

Possible classifications:

    NECESSARY BUT NOT SUFFICIENT

    SUFFICIENT BUT NOT NECESSARY

    BOTH NECESSARY AND SUFFICIENT

    NEITHER

These categories must remain distinct.

# 29. OVERDETERMINATION

Suppose:

    A → Y
    B → Y

and either A or B is sufficient.

Removing A may leave Y unchanged because B remains.

Therefore:

    Y still occurs without A

does not necessarily imply:

    A had no causal role.

# 30. PREEMPTION

Suppose:

    A causes Y first

while:

    B would have caused Y
    if A had not done so.

Removing A can activate B.

Simple but-for analysis may therefore mischaracterize causal contribution.

# 31. SYSTEM REACTION

Historical AMOS explicitly warns against treating reactive systems as static.

Full reaction chain:

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

Responses may include:

    adaptation
    substitution
    compensation
    gaming
    competitive response
    policy response
    behavioral change
    resource reallocation
    equilibrium change

If a model freezes a reactive system, that must be an explicit assumption.

# 32. FEEDBACK

If:

    Xt → Yt+1

and:

    Yt → Xt+1

static one-step reasoning may be inadequate.

Dynamic form:

    SCF(t+1)
      =
    F(SCF(t), It, Et, M)

may be required.

# 33. TEMPORAL STATE

    TemporalCounterfactual:

      factual_time
      intervention_time
      divergence_time
      outcome_horizon
      lag_structure
      persistence
      delayed_effects
      feedback_period

# 34. PRE-INTERVENTION INVARIANCE

Default:

    for t < intervention_time:

        WorldCF(t)
          =
        WorldActual(t)

unless earlier history is explicitly intervened upon.

# 35. COUNTERFACTUAL DISTANCE

Define qualitative counterfactual distance as a function of:

    intervention distance
    structural distance
    temporal distance
    regime distance
    assumption distance

Conceptually:

    DCF =
    f(DI, DS, DT, DR, DA)

No universal weighting is asserted.

# 36. DISTANCE CLASSES

    NEAR

      small intervention
      stable regime
      limited dependency change
      low assumption burden

    MID

      several dependencies
      possible adaptation
      moderate assumption burden

    FAR

      structural change
      possible regime change
      long horizon
      high assumption burden

    INCOHERENT

      violates hard constraints
      internally inconsistent
      impossible under declared model

# 37. UNCERTAINTY-DISTANCE LAW

Historical AMOS principle:

    FARTHER FROM ACTUALITY
            ↓
    GREATER UNCERTAINTY

Normalized law:

    if DCF2 > DCF1

then confidence in CF2 must not exceed CF1 merely because CF2 is narrated in
greater detail.

Detail is not evidence.

# 38. STRUCTURAL INTERVENTION

A structural intervention changes a mechanism:

    fY → f'Y

rather than only changing a variable value:

    Y := y'

Structural changes may invalidate broad dependency closures.

Therefore:

    STRUCTURAL CHANGE
          ↓
    DEEPER REVALIDATION

# 39. PARAMETRIC INTERVENTION

A parametric intervention changes:

    θ → θ'

while potentially preserving model topology.

Local reasoning may remain valid if:

    scope stable
    regime stable
    topology stable
    mechanism stable
    dependency closure stable

# 40. REGIME

    Regime:

      regime_id
      environment
      constraints
      dominant_mechanisms
      thresholds
      validity_conditions

# 41. REGIME FIREWALL

If:

    RegimeActual
      !=
    RegimeCounterfactual

then inherited causal relations require revalidation.

Examples:

    NORMAL → CRISIS

    LOW LOAD → SATURATION

    STABLE MARKET → PANIC

    PEACE → CONFLICT

    NORMAL GOVERNANCE → EMERGENCY GOVERNANCE

# 42. SCOPE

    Scope:

      system
      entity
      population
      geography
      environment
      scale
      time
      measurement
      assumptions

Counterfactual conclusions inherit their applicability envelope.

# 43. CROSS-SCALE FIREWALL

    MICRO EFFECT
       !=
    MACRO EFFECT

without justified aggregation.

Emergent system effects can invalidate naive composition.

# 44. CROSS-DOMAIN FIREWALL

    STRUCTURAL RESEMBLANCE
           !=
    CAUSAL TRANSFER

Cross-domain mappings remain:

    MODEL

until independently validated.

# 45. MULTI-AGENT COUNTERFACTUAL

For strategic systems:

    A acts
      ↓
    B responds
      ↓
    A adapts
      ↓
    C responds

Schema:

    MultiAgentCounterfactual:

      focal_intervention
      agents
      agent_models
      information_states
      response_rules
      strategic_dependencies
      equilibrium_or_trajectory
      uncertainty

Holding all agents fixed can itself be an unrealistic assumption.

# 46. INFORMATION COUNTERFACTUAL

Question:

    What if agent A knew information F?

Requires:

    INFORMATION
       ↓
    BELIEF UPDATE
       ↓
    DECISION
       ↓
    ACTION
       ↓
    SYSTEM RESPONSE
       ↓
    OUTCOME

Information does not automatically determine action.

# 47. BELIEF COUNTERFACTUAL

Changing:

    Belief(A) := B'

does not change:

    WorldTruth

Hard distinction:

    WORLD STATE
        !=
    BELIEF STATE

# 48. REFLEXIVE COUNTERFACTUAL

A prediction may itself enter the causal system:

    PREDICTION
       ↓
    AGENT RESPONSE
       ↓
    SYSTEM CHANGE
       ↓
    OUTCOME

The forecast cannot then be treated as causally external.

# 49. SELF-MODIFYING SYSTEMS

If:

    Mt → Mt+1

then intervention may alter future causal structure.

Projection may require:

    M0
     ↓ intervention
    M1'
     ↓
    M2'
     ↓
    M3'

rather than a permanently fixed M.

# 50. MULTIPLE INTERVENTIONS

For:

    I = {I1, I2, ..., In}

do not assume:

    Effect(I1 + I2)
       =
    Effect(I1) + Effect(I2)

Interactions may be:

    INDEPENDENT
    SYNERGISTIC
    ANTAGONISTIC
    THRESHOLD_DEPENDENT
    ORDER_DEPENDENT

# 51. ORDER EFFECT

In path-dependent systems:

    CF(CF(W,I1),I2)

may differ from:

    CF(CF(W,I2),I1)

Therefore intervention ordering may itself be load-bearing.

# 52. COMPETING CAUSAL MODELS

Let:

    M = {M1, M2, ..., Mn}

Then evaluate:

    CF1 = CF(W,I,M1)
    CF2 = CF(W,I,M2)
    ...
    CFn = CF(W,I,Mn)

If supported models produce materially incompatible outcomes:

    CONCLUSION CLASS = COMPETING

until discriminating evidence resolves them.

# 53. MODEL ROBUSTNESS

Suppose:

    M1 → conclusion A
    M2 → conclusion A
    M3 → conclusion A

This increases robustness only if M1, M2, and M3 are genuinely distinct in
their load-bearing assumptions or evidence.

Shared ancestry reduces independence.

# 54. PROVENANCE TOPOLOGY

    ProvenanceItem:

      evidence_id
      evidence_type
      source
      source_identity
      ancestry
      collected_at
      freshness
      scope
      regime
      method
      dependencies

Counterfactual confidence must account for evidence ancestry.

# 55. SYBIL HARDENING

    ONE ORIGINAL CLAIM
          ↓
    10 SUMMARIES
          ↓
    100 DERIVED NOTES
          ↓
    1000 SCENARIO BRANCHES

does not become:

    1000 INDEPENDENT CONFIRMATIONS

Generated branches are reasoning products, not independent evidence.

# 56. EVIDENCE TYPES

Evidence topology distinguishes:

    SOURCE_CLAIM
    OBSERVATION
    DERIVED
    MODEL
    DECISION
    UNKNOWN

Counterfactual states are normally:

    MODEL

or:

    DERIVED

not observation.

# 57. CONFIDENCE CEILING

For load-bearing premises:

    P1 ... Pn

candidate v4.4 rule:

    Confidence(CF)
      <=
    min(
      Confidence(P1),
      ...
      Confidence(Pn)
    )

unless a weak premise is independently revalidated or removed from the proof
path.

Reasoning fluency cannot increase evidential confidence.

# 58. UNCERTAINTY VECTOR

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

These should remain separate where they could change a decision.

# 59. IDENTIFIABILITY

Distinguish:

    DEFINED

    IDENTIFIABLE

    ESTIMABLE

    ESTIMATED

    VALIDATED

A counterfactual can be conceptually meaningful but not identifiable from
available evidence.

Correct response:

    COUNTERFACTUAL DEFINED
    BUT NOT IDENTIFIED
    FROM AVAILABLE EVIDENCE

# 60. PARTIAL IDENTIFICATION

If exact value is unavailable but defensible bounds exist:

    L <= CF <= U

return the interval.

Do not invent a point estimate.

If every value within the interval produces the same decision, decision
sufficiency may nevertheless be achieved.

# 61. PLAUSIBILITY / PROBABILITY FIREWALL

    POSSIBLE
       !=
    PLAUSIBLE
       !=
    PROBABLE

Also:

    BRANCH COUNT
       !=
    PROBABILITY

and:

    GENERATED FREQUENCY
       !=
    EMPIRICAL FREQUENCY

Without a justified probability model:

    DO NOT INVENT NUMERIC PROBABILITIES

# 62. CONSTRUCT_COUNTERFACTUAL

Historical function contract:

    construct_counterfactual

Inputs:

    actual_state
    intervention_description
    causal_model
    plausibility_constraints

Outputs:

    counterfactual_state
    causal_chain
    uncertainties
    assumption_list
    plausibility_assessment
    alternative_outcomes

Expanded contract:

    FUNCTION construct_counterfactual(
        actual_state,
        intervention,
        causal_model,
        plausibility_constraints
    ):

        validate actual_state

        validate intervention

        establish scope

        establish regime

        establish temporal envelope

        determine dependency closure

        verify causal model sufficiency

        identify assumptions

        identify confounders

        apply minimal intervention

        propagate causal descendants

        model system reactions

        construct counterfactual state

        generate materially distinct alternatives

        assess uncertainty

        identify sensitivity

        identify falsifiers

        return CounterfactualResult

# 63. COMPARE_ACTUAL_VS_COUNTERFACTUAL

Historical inputs:

    actual_outcome
    counterfactual_outcome
    causal_model
    confidence_levels

Historical outputs:

    difference_analysis
    causal_attribution
    confounding_factors
    attribution_confidence
    alternative_explanation

Expanded comparison:

    ACTUAL
      vs
    COUNTERFACTUAL

along:

    outcome
    causal pathway
    timing
    magnitude
    system response
    uncertainty
    distributional effect
    assumptions
    provenance
    competing explanation

# 64. SCENARIO_ANALYSIS

Historical inputs:

    current_state
    scenario_list
    uncertainty_model
    decision_criteria

Historical outputs:

    scenario_outcomes
    probability_assignments_if_available
    recommended_preparation
    early_warning_signals
    scenario_comparison

The phrase:

    IF AVAILABLE

is load-bearing.

No justified probability model means:

    NO FABRICATED PROBABILITY ASSIGNMENT

# 65. SCENARIO SET

    ScenarioSet:

      factual_anchor

      scenarios:
        - scenario_id
          intervention
          assumptions
          causal_model
          outcome
          uncertainty
          early_warning_signals

      comparison_dimensions

      discriminating_evidence

      decision_criteria

# 66. SCENARIO DIVERSITY

Do not generate many cosmetic variants.

Branches should differ only where the difference can materially alter:

    causal mechanism
    outcome
    risk
    decision
    action
    governance

Equivalent branches should be merged.

# 67. FULL COUNTERFACTUAL RUNTIME

    FUNCTION K_COUNTERFACTUAL(query):

      1. Parse objective.

      2. Determine:
           scope,
           stakes,
           horizon,
           deliverable.

      3. Classify:
           PAST,
           FUTURE,
           STRUCTURAL,
           CAUSAL.

      4. Bind factual anchor.

      5. Bind intervention.

      6. Bind queried outcome.

      7. Identify decision-changing uncertainty.

      8. Retrieve smallest sufficient dependency closure.

      9. Retrieve causal model.

     10. Type evidence.

     11. Resolve provenance ancestry.

     12. Check freshness.

     13. Check scope.

     14. Check regime.

     15. Check causal epoch.

     16. Check causal-model sufficiency.

     17. Check confounding.

     18. Check mediation.

     19. Check moderation.

     20. Check feedback.

     21. Check system / strategic response.

     22. If critical causal gap:
           return UNKNOWN/GAP.

     23. Perform abduction if required.

     24. Apply minimal intervention.

     25. Propagate licensed descendants.

     26. Construct alternative state.

     27. Generate only materially distinct alternatives.

     28. Preserve competing models.

     29. Assess plausibility.

     30. Represent uncertainty.

     31. Apply confidence ceiling.

     32. Find smallest result-flipping premise.

     33. Run adversarial validation when consequential.

     34. Identify falsifiers.

     35. Classify conclusion.

     36. Apply action governance if action is requested.

     37. Return proof-capsule-compatible result.

# 68. COUNTERFACTUAL RSCF

    CounterfactualRSCF:

      claim:
        statement
        class

      factual_anchor

      intervention

      queried_outcome

      premises

      evidence

      provenance

      causal_model

      dependency_closure

      scope

      regime

      causal_epoch

      freshness

      assumptions

      competing_hypotheses

      contradictions

      falsifiers

      sensitivity

      uncertainty

      confidence_ceiling

      invalidation_conditions

# 69. RECURSIVE RSCF

    COUNTERFACTUAL RSCF
    │
    ├── FACTUAL STATE RSCF
    │
    ├── CAUSAL EDGE RSCF
    │
    ├── INTERVENTION VALIDITY RSCF
    │
    ├── SCOPE VALIDITY RSCF
    │
    ├── REGIME VALIDITY RSCF
    │
    └── PROVENANCE RSCF

If a premise fails:

    INVALIDATE ONLY
    DEPENDENT DESCENDANTS

# 70. ATOMIC MULTI-RSCF REASONING

A consequential counterfactual decision may depend simultaneously on:

    causal validity
    technical feasibility
    financial feasibility
    safety
    authorization
    governance

These load-bearing views should not be composed from mutually incompatible
state snapshots.

# 71. H/M/L INTEGRATION

Retrieval path:

    BOOTSTRAP CAPSULE
          ↓
    H DOMAIN
          ↓
    M SUBSYSTEM
          ↓
    L LOAD-BEARING DETAIL
          ↓
    RAW EVIDENCE
    ONLY IF REQUIRED

Raw evidence defaults:

    DO_NOT_LOAD_UNLESS_REQUIRED

The counterfactual kernel should not retrieve unrelated material merely to
increase apparent depth.

# 72. GMEF INTEGRATION

Counterfactual reasoning may support governed evolution:

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

A favorable counterfactual does not itself authorize evolution.

# 73. WORLD MODEL INTEGRATION

Conceptual relation:

    K_SYSTEM_STATE
          ↓
    K_WORLD_MODEL
          ↓
    K_COUNTERFACTUAL
          ↓
    COUNTERFACTUAL WORLD

If required world-model mechanics are unavailable:

    UNKNOWN/GAP

must be preserved.

# 74. CONTEXT STATE INTEGRATION

    CounterfactualContext:

      active_world:
        ACTUAL
        COUNTERFACTUAL

      factual_parent

      branch_id

      intervention

      goal

      scope

      regime

      causal_epoch

Leaving counterfactual mode restores factual context.

# 75. MEMORY ADMISSION

Counterfactual outputs retain their epistemic type.

Forbidden:

    COUNTERFACTUAL MODEL
          ↓
    MEMORY
          ↓
    FACT

Correct memory representation:

    MemoryRecord:

      type: COUNTERFACTUAL_MODEL

      factual_anchor

      intervention

      causal_model

      assumptions

      conclusion_class

      scope

      regime

      provenance

      freshness

# 76. MEMORY RETRIEVAL

Before reuse ask:

    Is factual anchor still valid?

    Is causal model compatible?

    Is causal epoch compatible?

    Is scope compatible?

    Is regime compatible?

    Is evidence fresh?

    Has contradictory evidence appeared?

    Did a load-bearing premise change?

If yes to an invalidating condition:

    REVALIDATION_REQUIRED

# 77. CAUSAL EPOCH

    CausalEpoch:

      epoch_id
      causal_model_version
      evidence_snapshot
      dependency_snapshot
      provenance_snapshot
      regime
      validity_conditions

Counterfactual capsules are reusable only across compatible causal epochs.

# 78. CAUSAL EPOCH FINALITY

A counterfactual conclusion finalized under epoch:

    CE0

cannot silently inherit validity under:

    CE1

if CE1 changes a load-bearing:

    causal edge
    mechanism
    dependency
    regime
    evidence basis
    provenance relation

Revalidate affected closure only.

# 79. MVCC / CAS REASONING PATTERN

Conceptually:

    READ FACTUAL STATE @ V0
          ↓
    COMPUTE COUNTERFACTUAL
          ↓
    BEFORE CONSEQUENTIAL USE:
    CHECK LOAD-BEARING DEPENDENCIES
          ↓
       UNCHANGED?
       /      \
     YES      NO
      ↓        ↓
    REUSE   REVALIDATE
            AFFECTED CLOSURE

This is a reasoning pattern.

It is not a claim that the conversational runtime literally implements a
distributed MVCC database.

# 80. FAST PATH

Local reasoning is permitted only when:

    factual_anchor_valid = true

    intervention_unambiguous = true

    dependency_closure_established = true

    causal_model_adequate = true

    provenance_independence_adequate = true

    scope_compatible = true

    regime_compatible = true

    causal_epoch_compatible = true

    freshness_valid = true

    material_conflict_absent = true

    stakes_reversible_or_limited = true

# 81. FAST-PATH INVALIDATORS

Escalate when any material condition exists:

    causal ambiguity
    confounding
    correlated provenance
    contradiction
    stale premise
    regime shift
    scope transfer
    structural intervention
    feedback
    nonlinearity
    multi-agent response
    irreversible consequence
    safety exposure
    legal exposure
    financial exposure
    institutional impact
    governance impact
    ambiguous dependency

# 82. ADVERSARIAL VALIDATION

For consequential claims, challenge the strongest supported counterfactual.

Ask:

    Is the factual baseline wrong?

    Is the intervention ambiguous?

    Is a causal edge only correlational?

    Could reverse causality explain the observation?

    Is there hidden confounding?

    Was a mediator incorrectly frozen?

    Was a moderator ignored?

    Was feedback ignored?

    Was system reaction ignored?

    Did the regime change?

    Did scope expand silently?

    Are multiple sources descendants of one origin?

    Is evidence stale?

    Does another supported causal model reverse the result?

    What is the smallest assumption that flips the conclusion?

If the challenge succeeds:

    DOWNGRADE

    CONDITION

    PRESERVE COMPETING

or:

    RETURN UNKNOWN/GAP

# 83. SENSITIVITY

Find the smallest premise, threshold, assumption, or observation capable of
flipping the result.

Conceptually:

    p*
      =
    minimum decision-relevant perturbation
    capable of changing conclusion C

Record:

    Sensitivity:

      flip_premise
      flip_threshold
      flip_observation
      decision_impact

If a small plausible perturbation changes the conclusion:

    CONCLUSION CLASS = CONDITIONAL

# 84. FALSIFIERS

    Falsifiers:

      observation:
        threshold
        affected_premise
        affected_edge
        affected_conclusion

      regime_change

      confounder_discovered

      intervention_failure

      mechanism_disconfirmed

      provenance_failure

      factual_anchor_invalidated

A counterfactual should expose what could invalidate it.

# 85. LOCAL INVALIDATION

Core law:

    Invalid(p)
        ⇒
    Invalidate(
      dependent descendants of p
    )

not:

    Invalid(p)
        ⇒
    Invalidate entire knowledge state

This preserves unaffected reasoning.

# 86. FAILURE RECOVERY

    DETECT FAILED PREMISE
          ↓
    TRACE DEPENDENCY EDGES
          ↓
    INVALIDATE DEPENDENT DESCENDANTS
          ↓
    ROLLBACK TO NEAREST VALID STATE
          ↓
    CHANGE EVIDENCE / MODEL / ASSUMPTION
          ↓
    RECOMPUTE LOCAL CLOSURE
          ↓
    REVALIDATE

Do not repeat the same failed path without changed evidence or assumptions.

# 87. COUNTERFACTUAL HARM

    CounterfactualHarm:

      direct_harm
      indirect_harm
      distributional_harm
      opportunity_harm
      irreversible_harm
      informational_harm
      governance_harm
      uncertainty_harm

Potential harm is itself model-dependent and retains its appropriate
epistemic classification.

# 88. ACTION GOVERNANCE

Validation burden increases with:

    irreversibility
    cost
    legal exposure
    financial exposure
    health / safety exposure
    institutional impact
    downstream dependency
    uncertainty
    causal ambiguity

Prefer, where feasible:

    OBSERVATION
        ↓
    SIMULATION
        ↓
    SANDBOX
        ↓
    LIMITED EXPERIMENT
        ↓
    REVERSIBLE PILOT
        ↓
    STAGED ROLLOUT
        ↓
    MONITORED DEPLOYMENT

before irreversible commitment.

# 89. ACTION AUTHORITY FIREWALL

Hard invariant:

    COUNTERFACTUAL RECOMMENDATION
            !=
    EXECUTION AUTHORITY

Before real action:

    CHECK CAPABILITY

    CHECK AUTHORIZATION

    CHECK EFFECT CLASS

    CHECK RISK

    CHECK CURRENT STATE

    CHECK COMMIT-TIME AUTHORITY

# 90. VALUE OF INFORMATION

When uncertainty matters, prefer evidence that can change the decision.

Conceptually:

    VOI(test)
      =
    expected decision improvement
      -
    test cost
      -
    test risk

No universal numeric VOI formula is asserted.

# 91. DISCRIMINATING TEST

For competing models:

    M1
    M2

prefer a test T whose predicted observations differ materially.

    T*
      =
    highest-information feasible
    discriminating test

subject to:

    cost
    risk
    authorization
    reversibility
    time

# 92. PROOF CAPSULE

    CounterfactualProofCapsule:

      capsule_id

      claim:
        text
        class

      factual_anchor

      intervention

      queried_outcome

      causal_model:
        model_id
        version
        causal_epoch

      load_bearing_premises

      evidence

      provenance

      dependency_closure

      causal_structure:
        mechanisms
        mediators
        moderators
        confounders
        feedback

      counterfactual_state

      alternative_outcomes

      competing_explanations

      scope

      regime

      freshness

      uncertainty:
        evidence
        model
        scope
        temporal
        causal
        intervention
        execution
        provenance_independence

      sensitivity:
        flip_premise
        flip_threshold

      falsifiers

      confidence_ceiling

      invalidation_conditions

# 93. HISTORICAL COMMON ERRORS

Historical AMOS identifies:

    OVER_DETERMINATION

Assuming the counterfactual outcome would definitely be X without considering
other influencing factors.

    IGNORING_SYSTEM_REACTIONS

Treating the system as static when it would react to the intervention.

    CONFUSING_CORRELATION_WITH_CAUSATION

Assuming that because B followed A, changing A would necessarily change B.

    UNREALISTIC_BASELINE

Comparing actuality against an unrealistic or cherry-picked baseline.

    HIDDEN_CHANGES

Silently changing multiple variables in the counterfactual.

# 94. EXTENDED FAILURE MODES

    CF-F01 — OVERDETERMINATION

    CF-F02 — SYSTEM REACTION FAILURE

    CF-F03 — CORRELATION / CAUSATION COLLAPSE

    CF-F04 — UNREALISTIC BASELINE

    CF-F05 — HIDDEN CHANGE

    CF-F06 — FALSE PRECISION

    CF-F07 — FALSE PROBABILITY

    CF-F08 — REGIME LEAK

    CF-F09 — SCOPE LEAK

    CF-F10 — PROVENANCE COLLAPSE

    CF-F11 — STALE REUSE

    CF-F12 — COMPETING COLLAPSE

    CF-F13 — FACTUAL CONTAMINATION

    CF-F14 — AUTHORITY ESCALATION

    CF-F15 — CAUSAL CHAIN SKIP

    CF-F16 — MEDIATOR FREEZE

    CF-F17 — MODERATOR OMISSION

    CF-F18 — FEEDBACK OMISSION

    CF-F19 — IDENTIFIABILITY OVERCLAIM

    CF-F20 — BRANCH SYBIL

# 95. HISTORICAL SAFETY CONSTRAINTS

The historical kernel requires:

    never_present_counterfactual_as_fact = true

    never_ignore_uncertainty_in_far_counterfactuals = true

    always_state_assumptions_explicitly = true

    always_label_counterfactual_as_counterfactual = true

    never_use_counterfactual_to_over_determine_outcomes = true

# 96. V4.4 HARD SAFETY CONSTRAINTS

Additionally:

    never_invent_missing_causal_edges = true

    never_convert_correlation_into_causation_without_evidence = true

    never_silently_change_unrelated_variables = true

    never_invent_probability = true

    never_force_competing_models_into_false_consensus = true

    never_generalize_across_scope_without_validation = true

    never_generalize_across_regime_without_validation = true

    never_count_shared_provenance_as_independent_confirmation = true

    never_treat_counterfactual_output_as_execution_authority = true

    never_allow_fluency_to_raise_confidence = true

# 97. INTEGRATION CONTRACT

Historical integration provides to:

    Meta_Logic_Kernel
    Multi_Perspective_Reasoning_Kernel
    Strategy_Game_Engine
    Risk_Assessment

Historical use contexts include:

    Decision analysis
    Risk assessment
    Strategic planning
    Causal inference
    Policy evaluation

Routing:

    ROUTE_DEFAULT

or specialized domain routes when the counterfactual is domain-specific.

v4.4 integration additionally includes:

    RSCF
    H/M/L
    GMEF
    K_WORLD_MODEL
    K_SYSTEM_STATE
    K_CONTEXT_STATE
    K_MEMORY_ADMISSION
    K_MEMORY_RETRIEVAL
    K_CAUSAL_EPOCH
    K_PROVENANCE
    K_PROVENANCE_TOPOLOGY
    K_SYBIL_HARDENING
    K_RISK_CONSTRAINT
    K_CAPABILITY_AUTHORIZATION
    K_COMMIT_TIME_AUTHORITY

where those canonical artifacts exist and are compatible.

# 98. HISTORICAL UNIT TESTS

Required historical behaviors include:

    TEST 1

    Construct past counterfactual with causal model.

    EXPECT:

      counterfactual_state
      causal_chain
      uncertainties

    TEST 2

    Compare actual vs counterfactual.

    EXPECT:

      difference_analysis
      causal_attribution
      confounding_factors

    TEST 3

    Detect over-determination.

    EXPECT:

      error_flagged

    TEST 4

    Scenario analysis with three alternatives.

    EXPECT:

      scenario_outcomes
      recommended_preparation

# 99. EXTENDED VALIDATION SUITE

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

# 100. NEGATIVE TESTS

    CORRELATION
       ↓
    CAUSAL COUNTERFACTUAL

    MUST FAIL

---

    MODEL OUTPUT
       ↓
    OBSERVED FACT

    MUST FAIL

---

    ONE SOURCE
       ↓
    TEN SUMMARIES
       ↓
    TEN INDEPENDENT SOURCES

    MUST FAIL

---

    CHANGE X
       ↓
    SILENTLY CHANGE Z

    MUST FAIL

---

    NO PROBABILITY MODEL
       ↓
    "73.8% PROBABILITY"

    MUST FAIL

---

    SUPPORTED COMPETING MODELS
       ↓
    ONE CERTAIN CONCLUSION

    MUST FAIL

---

    STALE CAUSAL MODEL
       ↓
    CURRENT VALIDITY

    MUST FAIL WITHOUT REVALIDATION

---

    COUNTERFACTUAL RECOMMENDATION
       ↓
    EXECUTION AUTHORITY

    MUST FAIL

# 101. PROPERTY INVARIANTS

    Observed(Counterfactual) = false

unless the previously counterfactual state later becomes actual and is
independently observed.

    Confidence(CF)
      <=
    WeakestLoadBearingPremise

unless independently revalidated.

    Changed(CF)
      ⊆
    Intervention
      ∪
    LicensedDescendants
      ∪
    ExplicitAuxiliaryChanges

    BranchCount
      !=
    EvidenceCount

    Correlation
      !=
    CounterfactualCausation

    ModelAgreement
      !=
    IndependentEvidence

# 102. METAMORPHIC TESTS

If independently irrelevant Z changes:

    TARGET COUNTERFACTUAL
    SHOULD NOT CHANGE

when independence is established.

If load-bearing edge:

    X → Y

is removed and no alternative path exists:

    EFFECT ON Y
    MUST DISAPPEAR
    OR BECOME UNKNOWN

If regime changes outside validated scope:

    CONFIDENCE MUST FALL
    OR REVALIDATION MUST OCCUR

If multiple apparent evidence sources collapse to one ancestor:

    PROVENANCE-INDEPENDENCE CONFIDENCE
    MUST FALL

# 103. ERROR REGISTRY

    E_CF_NO_BASELINE

      factual anchor unavailable

    E_CF_AMBIGUOUS_INTERVENTION

      intervention insufficiently specified

    E_CF_HIDDEN_CHANGE

      undeclared world modification

    E_CF_CAUSAL_MODEL_MISSING

      required causal structure unavailable

    E_CF_CAUSAL_OVERREACH

      causal conclusion exceeds evidence

    E_CF_CONFOUNDING

      unresolved material confounding

    E_CF_MEDIATOR_ERROR

      mediation incorrectly modeled

    E_CF_MODERATOR_ERROR

      conditional effect ignored

    E_CF_FEEDBACK_IGNORED

      material feedback omitted

    E_CF_SYSTEM_REACTION_IGNORED

      adaptive response omitted

    E_CF_SCOPE_LEAK

      conclusion exceeds supported scope

    E_CF_REGIME_LEAK

      unsupported regime transfer

    E_CF_TEMPORAL_ERROR

      temporal structure invalid

    E_CF_PROVENANCE_COLLAPSE

      ancestry treated as independence

    E_CF_BRANCH_SYBIL

      generated branches treated as independent evidence

    E_CF_FALSE_PROBABILITY

      unsupported probability assignment

    E_CF_FALSE_PRECISION

      unsupported numerical precision

    E_CF_COMPETING_COLLAPSE

      unresolved models falsely merged

    E_CF_STALE_REUSE

      invalid counterfactual reused

    E_CF_AUTHORITY_ESCALATION

      reasoning result treated as execution authority

    E_CF_IDENTIFIABILITY_GAP

      target counterfactual not identifiable

    E_CF_UNKNOWN

      unresolved counterfactual failure

# 104. LAW REGISTRY

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

These KCF identifiers are normalized candidate-canon identifiers.

They are not asserted to be historical v1.0 numbering.

# 105. OUTPUT CONTRACT

    CounterfactualResult:

      label: COUNTERFACTUAL

      type:
        PAST
        FUTURE
        STRUCTURAL
        CAUSAL

      factual_baseline

      intervention

      queried_outcome

      conclusion:
        statement
        class:
          VERIFIED
          DERIVED
          MODEL
          CONDITIONAL
          COMPETING
          UNKNOWN/GAP

      causal_basis

      assumptions

      system_reactions

      competing_outcomes

      alternative_explanations

      confounders

      scope

      regime

      temporal_validity

      uncertainty

      confidence_ceiling

      sensitivity

      falsifiers

      invalidation_conditions

      discriminating_test

      reversible_action

# 106. ADAPTIVE COMPLEXITY

    C0 — DIRECT

Simple, local, low-stakes counterfactual.

    C1 — COMPACT

Small dependency chain with explicit assumptions.

    C2 — STRUCTURED

Multiple causal dependencies or meaningful uncertainty.

    C3 — DEEP

Competing models, causal ambiguity, regime sensitivity, consequential
decision.

    C4 — MAXIMUM

Irreversible, high-impact, governance-relevant, safety-critical, highly
uncertain, or structurally novel counterfactual.

Escalate for:

    high stakes
    irreversibility
    novelty
    weak evidence
    stale evidence
    contradiction
    causal ambiguity
    scope mismatch
    regime shift
    competing models
    governance impact
    provenance uncertainty

De-escalate when decision-changing uncertainty has been resolved.

# 107. STOP CONDITIONS

Stop expansion when:

    CLAIM SUFFICIENCY
          AND
    DECISION SUFFICIENCY
          AND
    ACTION SUFFICIENCY

are achieved.

More branches do not automatically produce more knowledge.

# 108. PROVENANCE STRATA

    S0_DIRECT_SOURCE

Historical AMOS Counterfactual Reasoning Kernel material directly recovered
from corpus.

    S1_AMOS_LINEAGE

Material explicitly inherited from broader AMOS architecture.

    S2_V4_4_INTEGRATION

Integration needed to align K_COUNTERFACTUAL with the v4.4 integrity,
provenance, scope, regime, RSCF, causal-epoch, and governance architecture.

    S3_DERIVED_FORMALIZATION

Schemas, algorithms, equations, test structures, normalized laws, and
contracts derived from AMOS principles but not represented as verbatim
historical source.

    S4_EXTERNAL_REFERENCE

External causal/counterfactual research used only where explicitly cited and
not silently promoted into AMOS canon.

    S5_UNKNOWN_GAP

Canonical, implementation, formal, or empirical detail not established.

# 109. HISTORICAL / DERIVED BOUNDARY

SOURCE-SUPPORTED HISTORICAL SPINE:

    Counterfactual_Reasoning_Kernel

    version 1.0.0

    Meta_Cognition

    priority 9

    required = true

    past counterfactual

    future counterfactual

    structural counterfactual

    causal counterfactual

    plausible initial state

    minimal change principle

    causal chain conservation

    uncertainty proportionate to distance

    assumption transparency

    construct_counterfactual

    compare_actual_vs_counterfactual

    scenario_analysis

    common counterfactual errors

    counterfactual safety constraints

V4.4 INTEGRATION:

    RSCF

    H/M/L

    GMEF

    typed evidence

    competing hypotheses

    provenance topology

    Sybil hardening

    scope firewall

    regime firewall

    causal epoch

    weakest-premise confidence ceiling

    local invalidation

    atomic multi-RSCF reasoning

    proof-based local reasoning

    reversible-action governance

DERIVED FORMALIZATION:

    structural-equation notation

    abduction → action → projection

    causal relation taxonomy

    counterfactual distance decomposition

    uncertainty vector

    identifiability states

    partial-identification contract

    proof capsule schema

    fast-path schema

    error registry

    KCF law identifiers

    metamorphic tests

These derived structures must not be misrepresented as byte-identical
historical AMOS source.

# 110. KNOWN GAPS

    KCF-GAP-001

    CLASS:
      DECISION-RELEVANT

    ISSUE:
      Exact byte-identical correspondence between every historical
      counterfactual artifact and this normalized K_COUNTERFACTUAL
      specification has not been established.

---

    KCF-GAP-002

    CLASS:
      DECISION-RELEVANT

    ISSUE:
      An executable implementation corresponding exactly to every
      mechanism specified here is not established.

---

    KCF-GAP-003

    CLASS:
      EXPLANATORY

    ISSUE:
      Complete supersession history between all historical
      counterfactual filenames and the normalized canonical name
      remains incomplete.

---

    KCF-GAP-004

    CLASS:
      DECISION-RELEVANT

    ISSUE:
      No universal calibrated probability model exists for every
      counterfactual domain.

---

    KCF-GAP-005

    CLASS:
      UNKNOWN/GAP

    ISSUE:
      Universal empirical validity is not established.

---

    KCF-GAP-006

    CLASS:
      UNKNOWN/GAP

    ISSUE:
      Universal formal proof of counterfactual correctness is not
      established.

# 111. PROMOTION GATE

Before promotion from:

    CANDIDATE_CANON

to an authoritative canon state:

    [ ] historical source registered

    [ ] provenance lineage recorded

    [ ] duplicate artifacts resolved

    [ ] supersession graph recorded

    [ ] dependencies verified

    [ ] conflicts registered

    [ ] Meta Logic compatibility checked

    [ ] Meta Epistemology compatibility checked

    [ ] Probability / Statistics dependency checked

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

Existence of this artifact does not satisfy those gates.

# 112. CANONICAL COMPRESSION

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

      RETURN BOUNDS

      OR

      UNKNOWN/GAP.

    WHEN
    A PREMISE FAILS:

      INVALIDATE ONLY
      DEPENDENT DESCENDANTS.

    WHEN
    THE RESULT IS FRAGILE:

      RETURN CONDITIONAL.

    WHEN
    SUPPORTED MODELS DISAGREE:

      RETURN COMPETING.

    WHEN
    A CHEAP,
    REVERSIBLE,
    HIGH-INFORMATION
    DISCRIMINATING TEST EXISTS:

      PREFER THE TEST
      OVER MORE SPECULATION.

    NEVER LET

      COMPLETENESS,
      FLUENCY,
      SPEED,
      OR NUMERICAL PRECISION

    OUTRUN

      INTEGRITY.

# 113. FORMAL KERNEL CONTRACT

Conceptually:

    K_COUNTERFACTUAL:

      (
        F,
        I,
        M,
        E,
        S,
        R,
        T,
        P
      )

      →

      (
        C,
        Class,
        U,
        D,
        Falsifiers
      )

where:

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

subject to:

    FACTUAL INTEGRITY

    MINIMAL INTERVENTION

    CAUSAL VALIDITY

    SCOPE INTEGRITY

    REGIME INTEGRITY

    TEMPORAL INTEGRITY

    PROVENANCE INTEGRITY

    ASSUMPTION TRANSPARENCY

and:

    Confidence(C)
      <=
    WeakestLoadBearingPremise

unless independently revalidated.

# 114. CANONICAL STATE

    K_COUNTERFACTUAL:

      historical_lineage:

        kernel:
          Counterfactual_Reasoning_Kernel

        historical_version:
          1.0.0

        historical_category:
          Meta_Cognition

        historical_state:
          SOURCE_SUPPORTED

      normalized_artifact:

        name:
          K_COUNTERFACTUAL

        status:
          CANDIDATE_CANON

        conclusion_class:
          DERIVED

      amos_core_target:

        version:
          v4.4

        alignment:
          INTEGRATED_MODEL

      executable_implementation:

        status:
          UNKNOWN/GAP

      empirical_validation:

        status:
          UNKNOWN/GAP

      universal_formal_verification:

        status:
          UNKNOWN/GAP

      supersession:

        K_COUNTERFACTUAL_PLACEHOLDER:

          status:
            SUPERSEDED_BY_CANDIDATE

        authoritative_final_canon:

          status:
            NOT_YET_PROMOTED

# 115. TERMINAL INTEGRITY LAW

The governing counterfactual law:

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

The governing intervention law:

    CHANGE ONLY WHAT
    THE DECLARED INTERVENTION
    AND DEFENSIBLE
    CAUSAL CONSEQUENCES
    REQUIRE.

The governing causal law:

    STRUCTURE,
    SEQUENCE,
    ASSOCIATION,
    ANALOGY,
    AND CORRELATION
    DO NOT BY THEMSELVES
    ESTABLISH
    COUNTERFACTUAL CAUSATION.

The governing epistemic law:

    WHEN THE EVIDENCE
    CANNOT DISTINGUISH
    THE ALTERNATIVE WORLDS,

    PRESERVE COMPETING

    OR

    RETURN UNKNOWN/GAP.

The governing uncertainty law:

    THE FARTHER
    THE COUNTERFACTUAL WORLD
    MOVES FROM ACTUALITY,

    THE MORE ASSUMPTION BURDEN
    MUST BE EXPOSED,

    AND CONFIDENCE
    MUST NOT INCREASE
    WITHOUT NEW SUPPORT.

The governing provenance law:

    MANY DESCENDANTS
    OF ONE EVIDENTIAL ANCESTOR

    DO NOT BECOME

    MANY INDEPENDENT
    CONFIRMATIONS.

The governing recovery law:

    WHEN A LOAD-BEARING
    PREMISE FAILS,

    INVALIDATE
    ONLY THE CONCLUSIONS
    THAT DEPEND ON IT.

The governing operational law:

    UNDER CONSEQUENTIAL
    UNCERTAINTY,

    PREFER THE CHEAPEST
    SAFE,
    REVERSIBLE,
    HIGH-INFORMATION
    DISCRIMINATING TEST

    OVER

    UNSUPPORTED CERTAINTY.

The governing AMOS law:

    INTEGRITY
    >
    COMPLETENESS
    >
    FLUENCY
    >
    SPEED
    >
    TOKEN SAVINGS.

# END — K COUNTERFACTUAL

The source boundary here is materially stronger than the original placeholder: the Drive corpus directly supports the kernel's identity, purpose, dependencies, four counterfactual classes, validity criteria, errors, functions, integration points, safety constraints, and original evaluation requirements.  I have **not** promoted the reconstructed v4.4 extensions to verified implementation or final canon; those remain `DERIVED`/`CANDIDATE_CANON` pending the promotion process.
