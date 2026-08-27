---
title: L6 UNCERTAINTY
type: note
tags: [note, 01-core-laws]
---

````markdown
---
tags: ['canon', 'core_laws', 'uncertainty', 'confidence', 'unknown', 'competing', 'rscf', 'governance']
title: "L6 Uncertainty Laws"
origin_architect: "Trang Phan"
updated: "2026-08-26"
status: "PROPOSED_SPECIFICATION"
epistemic_class: "AMOS_MODEL"
canonical_status: "CONDITIONAL"
implementation_status: "LOGIC_EXECUTABLE_IN_PART"
---

# L6 Uncertainty Laws

**Origin architect / steward:** Trang Phan  
**Layer:** `01_CANON / 01_CORE_LAWS / L6_UNCERTAINTY`  
**Artifact class:** `CORE_LAW_CONTRACT`  
**Status:** `PROPOSED_SPECIFICATION / AMOS_MODEL`  
**Canonical status:** `CONDITIONAL`  
**Implementation status:** `LOGIC_EXECUTABLE_IN_PART`

> L6 governs how AMOS represents, propagates, constrains, compares, reduces, preserves, and invalidates uncertainty.
>
> Uncertainty is part of the epistemic state of a claim. It must not be hidden merely to produce a complete, fluent, decisive, or convenient answer.

---

# 0. Status

This document is a proposed full structural specification for `L6_UNCERTAINTY.md`.

It expands the currently stated L6 seed:

```text
U-1 Typed Uncertainty
U-2 Confidence Ceiling
U-3 Ambiguity Preservation
U-4 Unknown Propagation
````

without claiming that every supporting operator, schema, threshold, validator, or runtime mechanism below is already final canon or fully implemented.

Hard distinction:

```text
SPECIFIED != IMPLEMENTED
IMPLEMENTED != VALIDATED
VALIDATED_LOCALLY != UNIVERSALLY_VALID
```

The supplied `0.95` hard confidence ceiling is retained as part of the proposed L6 specification, but remains conditional on authoritative epistemics canon not defining different semantics.

---

# 1. Purpose

L6 exists to make uncertainty:

* explicit;
* typed;
* scoped;
* dependency-aware;
* provenance-aware;
* regime-aware;
* temporally bounded;
* non-collapsible;
* selectively reducible;
* propagatable through RSCF;
* auditable by validators;
* actionable without fabrication.

The primary law is:

```text
UNCERTAINTY MUST REMAIN VISIBLE
UNTIL EVIDENCE LEGITIMATELY REDUCES IT.
```

L6 prevents the transformations:

```text
UNKNOWN → ASSUMED
```

```text
AMBIGUOUS → ARBITRARILY SELECTED
```

```text
COMPETING → AVERAGED
```

```text
WEAK EVIDENCE → HIGH CONFIDENCE
```

```text
MISSING EVIDENCE → PLAUSIBLE COMPLETION
```

```text
MODEL UNCERTAINTY → SOURCE CERTAINTY
```

and:

```text
CONFIDENCE → TRUTH
```

---

# 2. Core Uncertainty Contract

Every consequential AMOS claim SHOULD carry an uncertainty state sufficient to answer:

```text
What is uncertain?
Why is it uncertain?
What type of uncertainty is it?
Which premises create it?
How much does it matter?
Can it be reduced?
What evidence would reduce it?
What could increase it?
Can the decision proceed despite it?
What is the maximum confidence currently licensed?
```

Conceptually:

```text
Uncertainty(C)
=
U(
  evidence,
  provenance,
  model,
  scope,
  regime,
  temporal_state,
  causal_status,
  dependencies,
  measurement,
  execution_state
)
```

This is an **AMOS MODEL expression**, not a universal mathematical theorem.

---

# 3. Foundational Laws

## U-1 — Typed Uncertainty

Uncertainty MUST be classified before consequential use.

Minimum epistemic-origin classes:

```text
SOURCE
DERIVED
MODEL
UNKNOWN
```

The origin of uncertainty must remain distinguishable from the claim class itself.

Example:

```yaml
claim_class: DERIVED

uncertainty:
  source: LOW
  derivation: MEDIUM
  model: NONE
  unknown: PRESENT
```

A claim being `DERIVED` does not imply all uncertainty is derivational.

---

## U-2 — Confidence Ceiling

No claim may exceed the confidence licensed by its load-bearing evidence and dependencies.

Conceptually:

```text
Confidence(C)
≤
min(
  Confidence(P1),
  Confidence(P2),
  ...,
  Confidence(Pn)
)
```

for load-bearing premises unless the claim is independently revalidated through evidence that legitimately removes dependence on the weaker premise.

The proposed general hard ceiling is:

```text
Confidence(C) ≤ 0.95
```

absent stronger proof status recognized by the authoritative AMOS epistemics layer.

This ceiling is a **proposed AMOS governance convention**, not an empirical probability theorem.

Therefore:

```text
0.95 != 95% FREQUENTIST PROBABILITY
```

unless a specific calibrated statistical interpretation has been established.

---

## U-3 — Ambiguity Preservation

When alternatives are:

* incompatible;
* incomparable;
* differently scoped;
* supported by correlated evidence;
* insufficiently discriminated;
* approximately equally supported;

AMOS MUST preserve them as:

```text
COMPETING
```

rather than manufacture convergence.

Therefore:

```text
COMPETING(A, B)
!=
AVERAGE(A, B)
```

and:

```text
NO_WINNER
!=
50/50
```

unless a probabilistic model actually licenses that assignment.

---

## U-4 — Unknown Propagation

Operations requiring an unknown load-bearing input MUST:

```text
PROPAGATE UNKNOWN
```

or:

```text
FAIL CLOSED
```

when the missing input prevents justified computation.

Never:

```text
UNKNOWN
→
PLAUSIBLE VALUE
→
CONTINUE AS FACT
```

Thus:

```text
UNKNOWN/GAP != PASS
```

---

# 4. Additional Governing Laws

## U-5 — Confidence Is Not Evidence

```text
CONFIDENCE != EVIDENCE
```

A confidence value summarizes epistemic state. It does not create evidence.

Repeated confidence statements do not strengthen the underlying claim.

---

## U-6 — Confidence Is Not Truth

```text
HIGH_CONFIDENCE != VERIFIED_TRUTH
```

A highly confident claim may still be wrong.

Likewise:

```text
LOW_CONFIDENCE != FALSE
```

---

## U-7 — Repetition Does Not Reduce Uncertainty

```text
REPETITION != INDEPENDENT_CONFIRMATION
```

Multiple sources descended from one origin do not automatically reduce uncertainty.

---

## U-8 — Independence Must Be Demonstrated

Evidence aggregation may reduce uncertainty only when relevant independence assumptions are justified.

```text
MULTIPLE_SOURCES
!=
MULTIPLE_INDEPENDENT_SOURCES
```

---

## U-9 — Uncertainty Is Typed, Not Scalar-Only

A single number MUST NOT erase materially different uncertainty dimensions.

For consequential claims AMOS MAY track:

```text
evidence uncertainty
model uncertainty
scope uncertainty
temporal uncertainty
causal uncertainty
execution uncertainty
provenance-independence uncertainty
```

---

## U-10 — Uncertainty Reduction Requires Information

Uncertainty may not decrease merely because reasoning continued longer.

```text
MORE_REASONING != MORE_EVIDENCE
```

Legitimate reduction requires something such as:

* new evidence;
* stronger provenance;
* successful validation;
* discriminating observation;
* resolved dependency;
* narrowed scope;
* better measurement;
* successful execution test;
* formal proof where applicable.

---

## U-11 — Narrowing May Increase Confidence

A broad claim may be weak while a narrower claim is strong.

Therefore:

```text
UNCERTAIN_BROAD_CLAIM
```

may legitimately become:

```text
HIGHER_CONFIDENCE_NARROW_CLAIM
```

through scope contraction.

This is not fabrication if the narrower statement is independently supported.

---

## U-12 — Uncertainty Must Be Decision-Relevant

AMOS SHOULD distinguish uncertainty that can change a decision from uncertainty that cannot materially change it.

```text
DECISION_RELEVANT_UNCERTAINTY
>
EXPLANATORY_UNCERTAINTY
>
COSMETIC_UNCERTAINTY
```

for reasoning-resource allocation.

This ordering concerns priority, not truth value.

---

# 5. Uncertainty Vector

For consequential claims, L6 SHOULD support a multidimensional uncertainty representation.

Conceptually:

```text
U(C) =
[
  Ue,
  Um,
  Us,
  Ut,
  Uc,
  Ux,
  Up
]
```

where:

```text
Ue = evidence uncertainty
Um = model uncertainty
Us = scope uncertainty
Ut = temporal uncertainty
Uc = causal uncertainty
Ux = execution uncertainty
Up = provenance-independence uncertainty
```

This vector is an AMOS structural model.

It does not require every implementation to encode uncertainty numerically.

---

# 6. Evidence Uncertainty

Evidence uncertainty concerns the quality and completeness of evidence supporting a claim.

Sources include:

* missing observations;
* small samples;
* noisy measurements;
* incomplete records;
* conflicting observations;
* measurement error;
* unverified reports;
* indirect evidence.

Example:

```yaml
uncertainty:
  evidence:
    status: MATERIAL
    causes:
      - incomplete_observation
      - measurement_noise
```

---

# 7. Model Uncertainty

Model uncertainty concerns whether the selected representation or explanatory model is appropriate.

Examples:

* model misspecification;
* omitted variables;
* competing models;
* unstable parameters;
* approximation error;
* extrapolation;
* unvalidated assumptions.

Therefore:

```text
PRECISE_MODEL_OUTPUT
!=
LOW_MODEL_UNCERTAINTY
```

A model may output many decimal places while remaining epistemically weak.

---

# 8. Scope Uncertainty

Scope uncertainty concerns uncertainty over where a claim applies.

Examples:

```text
population unknown
environment mismatch
cross-domain transfer
cross-scale transfer
uncertain exclusions
measurement-context mismatch
```

L6 delegates applicability structure to `L5_SCOPE_REGIME`.

Therefore:

```text
UNKNOWN_SCOPE
→
SCOPE_UNCERTAINTY
```

not universal applicability.

---

# 9. Temporal Uncertainty

Temporal uncertainty concerns:

* unknown evidence age;
* uncertain event ordering;
* uncertain freshness;
* uncertain validity duration;
* delayed observations;
* possible regime transition.

Example:

```yaml
uncertainty:
  temporal:
    freshness: UNKNOWN
    event_time: KNOWN
    observation_time: KNOWN
```

Temporal uncertainty does not necessarily invalidate historical claims but may invalidate current-use claims.

---

# 10. Causal Uncertainty

Causal uncertainty concerns uncertainty over whether observed relationships represent:

* association;
* correlation;
* enabling condition;
* mediator;
* confounder;
* feedback;
* mechanism;
* necessary condition;
* sufficient condition;
* causal effect.

L6 MUST NOT resolve causal uncertainty merely through confidence language.

```text
HIGH_CONFIDENCE_CORRELATION
!=
CAUSAL_EFFECT
```

Causal typing remains governed by L4.

---

# 11. Execution Uncertainty

Execution uncertainty concerns whether a proposed operation will actually produce the expected result.

It includes:

* runtime uncertainty;
* environmental uncertainty;
* tool availability;
* dependency state;
* external-state mutation;
* concurrency;
* commit failure;
* implementation mismatch.

Therefore:

```text
LOGICALLY_VALID_PLAN
!=
SUCCESSFUL_EXECUTION
```

Execution evidence must remain separate from reasoning confidence.

---

# 12. Provenance-Independence Uncertainty

AMOS MUST track uncertainty about whether apparently separate evidence is genuinely independent.

Example:

```text
Source A
   ↓
Source B paraphrases A
   ↓
Source C summarizes B
```

must not be interpreted as:

```text
3 independent confirmations
```

The actual topology may contain only one origin.

Thus:

```text
COUNT(SOURCES)
!=
COUNT(INDEPENDENT_ORIGINS)
```

---

# 13. Typed Uncertainty State

A conceptual uncertainty object MAY be represented as:

```yaml
UncertaintyState:
  claim_id: ClaimID

  evidence:
    level: ...
    causes: [...]

  model:
    level: ...
    causes: [...]

  scope:
    level: ...
    causes: [...]

  temporal:
    level: ...
    causes: [...]

  causal:
    level: ...
    causes: [...]

  execution:
    level: ...
    causes: [...]

  provenance_independence:
    level: ...
    causes: [...]

  unknowns: [...]

  competing: [...]

  confidence_ceiling: ...

  decision_relevance: ...

  reducibility:
    reducible: true | false | unknown
    candidate_tests: [...]

  provenance: [...]
```

---

# 14. Qualitative Uncertainty Levels

Where numerical uncertainty is unsupported, AMOS SHOULD prefer explicit qualitative states.

Example:

```text
NONE_ESTABLISHED
LOW
MODERATE
HIGH
CRITICAL
UNKNOWN
```

These labels MUST NOT be silently interpreted as calibrated probabilities.

For example:

```text
HIGH UNCERTAINTY
```

does not mathematically mean:

```text
P(error) > 0.5
```

unless explicitly calibrated.

---

# 15. Numerical Confidence

Numerical confidence MAY be used only when its semantics are explicit.

A confidence object SHOULD specify:

```yaml
confidence:
  value: 0.72
  semantics: AMOS_EPISTEMIC_SCORE
  calibration: UNVALIDATED
  basis: [...]
  ceiling: 0.80
```

rather than simply:

```yaml
confidence: 0.72
```

when ambiguity would matter.

---

# 16. Confidence Ceiling Mechanics

For a conclusion `C` depending on premises:

```text
P1, P2, ..., Pn
```

the default AMOS ceiling is conceptually:

```text
Ceiling(C)
≤
min(
  Ceiling(P1),
  Ceiling(P2),
  ...,
  Ceiling(Pn)
)
```

for load-bearing dependencies.

This prevents:

```text
weak premise
+
strong premise
+
fluent synthesis
=
very strong conclusion
```

---

# 17. Independent Revalidation Exception

The weakest-premise ceiling may cease to bind if the conclusion is independently established through another valid proof path.

Example:

```text
Path A:
P1 weak
P2 strong
→ C ceiling 0.60
```

but:

```text
Path B:
Independent evidence E
→ directly validates C at stronger level
```

Then `C` may be promoted based on Path B.

However:

```text
PARAPHRASED_PATH != INDEPENDENT_PATH
```

Independence must be demonstrated.

---

# 18. Proposed Hard Ceiling

Absent a recognized stronger proof state:

```text
confidence_ceiling ≤ 0.95
```

This prevents ordinary evidence aggregation from being represented as absolute certainty.

Possible exceptions MAY include authoritative formal proof categories defined elsewhere.

Until such canon is resolved:

```text
>0.95 = REQUIRES_STRONGER_PROOF_CLASS
```

This remains conditional because the authoritative epistemics canon may define different ceiling semantics.

---

# 19. Confidence Composition Prohibition

AMOS MUST NOT arbitrarily compute:

```text
(0.7 + 0.8 + 0.9) / 3 = 0.8
```

as claim confidence unless an explicit validated aggregation rule licenses that operation.

Similarly:

```text
0.7 × 0.8
```

or:

```text
1 - (1-0.7)(1-0.8)
```

must not be used merely because they appear mathematically plausible.

Confidence composition requires semantic and probabilistic justification.

---

# 20. Unknown

`UNKNOWN` means the system lacks sufficient justified information to resolve a required state.

It does NOT mean:

```text
false
zero
unlikely
irrelevant
neutral
50/50
```

Therefore:

```text
UNKNOWN != FALSE
UNKNOWN != ZERO
UNKNOWN != 0.5
```

---

# 21. GAP

`GAP` identifies a missing information, specification, implementation, provenance, validation, or dependency element.

A gap MAY be:

```text
CRITICAL
DECISION_RELEVANT
EXPLANATORY
COSMETIC
```

The gap class determines priority.

---

# 22. Critical Gap

A critical gap prevents a safe or justified conclusion.

Examples:

* unknown authority for irreversible action;
* missing load-bearing evidence;
* unknown target identity;
* unresolved safety constraint;
* unknown regime where decision depends on regime.

Required response:

```text
STOP / FAIL CLOSED / ESCALATE
```

depending on the relevant control plane.

---

# 23. Decision-Relevant Gap

A decision-relevant gap could change the recommended decision.

AMOS SHOULD seek the cheapest discriminating evidence capable of resolving it.

```text
VALUE_OF_INFORMATION
>
REDUNDANT_EVIDENCE_ACCUMULATION
```

when the discriminating evidence can change the outcome.

---

# 24. Explanatory Gap

An explanatory gap limits understanding but does not currently change the decision.

It SHOULD remain visible but need not block action when action sufficiency is otherwise established.

---

# 25. Cosmetic Gap

A cosmetic gap does not materially alter:

* validity;
* decision;
* authority;
* execution;
* provenance;
* safety.

It has lowest repair priority.

---

# 26. Unknown Propagation Rule

Given:

```text
C = f(A, B)
```

if:

```text
A = KNOWN
B = UNKNOWN
```

and `B` is load-bearing, then:

```text
C = UNKNOWN / CONDITIONAL
```

not:

```text
C = ESTIMATED_WITHOUT_DISCLOSURE
```

---

# 27. Non-Load-Bearing Unknowns

Not every unknown blocks a conclusion.

If `B` is demonstrably irrelevant to `C`, then:

```text
B = UNKNOWN
```

need not force:

```text
C = UNKNOWN
```

Therefore L6 requires dependency analysis.

The governing rule is:

```text
PROPAGATE LOAD-BEARING UNKNOWN
```

not:

```text
PROPAGATE EVERY UNKNOWN GLOBALLY
```

---

# 28. Partial Knowledge

AMOS SHOULD preserve partially known states.

Example:

```yaml
state:
  identity: KNOWN
  location: UNKNOWN
  timestamp: KNOWN
  regime: COMPETING
```

rather than collapsing the entire state to one undifferentiated uncertainty label.

This supports selective repair.

---

# 29. Competing Hypotheses

A competing hypothesis set MAY be represented as:

```yaml
competing:
  - hypothesis_id: H1
    claim: ...
    support: [...]
    falsifiers: [...]

  - hypothesis_id: H2
    claim: ...
    support: [...]
    falsifiers: [...]
```

AMOS SHOULD preserve:

* independent support;
* shared evidence;
* contradictory evidence;
* provenance ancestry;
* scope;
* regime;
* falsifiers.

---

# 30. Competition Is Not Probability

Given:

```text
H1
H2
H3
```

AMOS MUST NOT assume:

```text
P(H1) + P(H2) + P(H3) = 1
```

unless the hypotheses are demonstrably:

* mutually exclusive;
* collectively exhaustive;
* represented within a valid probabilistic model.

Therefore:

```text
COMPETING_SET != PROBABILITY_DISTRIBUTION
```

---

# 31. Incomparable Hypotheses

Some alternatives cannot be ranked because they:

* answer different questions;
* operate at different scales;
* rely on incompatible measurements;
* belong to different regimes;
* have non-comparable evidence.

Such hypotheses SHOULD remain:

```text
INCOMPARABLE
```

rather than being forced into an ordinal ranking.

---

# 32. Correlated Hypotheses

Two hypotheses may appear independently supported while relying on the same evidence origin.

L6 therefore requires L2 provenance analysis before treating apparent support as independent.

```text
SUPPORT_COUNT
```

must not substitute for:

```text
INDEPENDENT_SUPPORT
```

---

# 33. Discriminating Evidence

When hypotheses remain competing, AMOS SHOULD seek:

```text
the cheapest evidence
with the highest expected ability
to change the hypothesis ranking
```

rather than collecting more evidence that all hypotheses predict equally.

Conceptually:

```text
PreferredTest
=
argmax(
  DecisionRelevantInformationGain
  /
  Cost
)
```

This is an AMOS decision heuristic, not a universally established equation.

---

# 34. Uncertainty Reduction

Valid uncertainty reduction MAY occur through:

```text
NEW OBSERVATION
INDEPENDENT SOURCE
FORMAL PROOF
VALIDATED TEST
BETTER MEASUREMENT
SCOPE CONTRACTION
REGIME RESOLUTION
DEPENDENCY RESOLUTION
PROVENANCE RESOLUTION
EXECUTION RESULT
COUNTEREXAMPLE SEARCH
```

It MUST NOT occur merely through:

```text
REPHRASING
REPETITION
LONGER EXPLANATION
MORE AGENTS WITH SAME SOURCE
MODEL AGREEMENT WITHOUT INDEPENDENCE
AUTHORITY WITHOUT EVIDENCE
```

---

# 35. Uncertainty Increase

Uncertainty SHOULD increase or confidence SHOULD decrease when:

* contradiction appears;
* provenance becomes ambiguous;
* source is retracted;
* regime shifts;
* evidence becomes stale;
* model assumptions fail;
* dependency changes;
* execution diverges from prediction;
* independent challenge succeeds;
* measurement reliability degrades.

Thus confidence is reversible.

---

# 36. No Monotonic Confidence Assumption

AMOS MUST NOT assume confidence only increases over time.

```text
C(t+1) ≥ C(t)
```

is not a general law.

New evidence may produce:

```text
C(t+1) < C(t)
```

and this downgrade is an integrity-preserving result.

---

# 37. Contradiction

Contradiction introduces uncertainty unless one side can be invalidated.

Conceptually:

```text
SUPPORTED(C)
AND
SUPPORTED(NOT C)
→
CONFLICT
```

The system SHOULD investigate:

* scope mismatch;
* regime mismatch;
* temporal mismatch;
* source ancestry;
* measurement mismatch;
* version mismatch;
* actual logical contradiction.

Until resolved:

```text
CONFLICT != CONSENSUS
```

---

# 38. Contradiction Visibility

A system MUST NOT hide contradiction by:

* averaging confidence;
* deleting minority evidence;
* choosing the newest source automatically;
* choosing the most authoritative source automatically;
* choosing the most fluent explanation;
* merging incompatible claims.

Contradiction remains visible until legitimately resolved.

---

# 39. Source Uncertainty

Source uncertainty concerns whether the originating source itself is:

* authentic;
* complete;
* accurately represented;
* current;
* correctly attributed;
* within scope.

Example:

```yaml
uncertainty:
  source:
    authenticity: VERIFIED
    completeness: UNKNOWN
    freshness: CURRENT
```

---

# 40. Derived Uncertainty

Derived uncertainty arises through transformations such as:

* inference;
* aggregation;
* compression;
* translation;
* abstraction;
* cross-scale mapping;
* causal interpretation.

A transformation may introduce uncertainty even when inputs are reliable.

Therefore:

```text
HIGH_QUALITY_INPUT
!=
ZERO_DERIVATION_UNCERTAINTY
```

---

# 41. Model Uncertainty vs Unknown

These states must remain distinct.

```text
MODEL_UNCERTAINTY
```

means a model exists but its adequacy is uncertain.

```text
UNKNOWN
```

means a required state is unresolved.

Example:

```text
unknown causal mechanism
```

is not equivalent to:

```text
two known causal models with uncertain selection
```

---

# 42. Epistemic Classification

L6 SHOULD interoperate with the AMOS conclusion classes:

```text
VERIFIED
DERIVED
MODEL
CONDITIONAL
COMPETING
UNKNOWN/GAP
```

These classes are not interchangeable confidence bins.

For example:

```text
MODEL at 0.90
```

does not become:

```text
VERIFIED
```

because confidence is high.

Claim class and confidence are separate dimensions.

---

# 43. Conditional Claims

A `CONDITIONAL` claim SHOULD identify the condition.

Bad:

```text
CONDITIONAL: X
```

Better:

```yaml
claim_class: CONDITIONAL
claim: X
conditions:
  - regime remains R1
  - dependency D remains valid
```

A conditionless conditional label is structurally incomplete.

---

# 44. Confidence Ceiling Inheritance

Derived claims inherit the weakest load-bearing ceiling.

Example:

```text
P1 ceiling = 0.90
P2 ceiling = 0.75
P3 ceiling = 0.88
```

If all three are load-bearing:

```text
C ceiling ≤ 0.75
```

unless independently revalidated.

This prevents confidence inflation through synthesis.

---

# 45. Provenance Ceiling

Where source independence is uncertain:

```text
provenance_independence = UNKNOWN
```

the confidence ceiling SHOULD remain bounded.

Multiple descendants cannot be treated as independent confirmation until ancestry is resolved.

---

# 46. Scope Ceiling

If applicability outside scope `S1` is unknown:

```text
Confidence(C in S1) = potentially high
```

while:

```text
Confidence(C outside S1) = bounded / UNKNOWN
```

Confidence therefore attaches to the scoped claim, not merely its text.

---

# 47. Regime Ceiling

If:

```text
C valid in R1
```

and current regime may be `R1` or `R2`, then confidence in current applicability is bounded by regime uncertainty.

Thus:

```text
high confidence in C|R1
```

does not imply:

```text
high confidence in C|current_state
```

---

# 48. Temporal Ceiling

A claim whose evidence may be stale cannot retain its former current-use confidence merely because historical support was strong.

Historical and current confidence must remain distinguishable.

---

# 49. Causal Ceiling

A conclusion cannot carry stronger causal confidence than its causal evidence licenses.

Example:

```text
strong observational association
```

cannot be promoted to:

```text
verified intervention effect
```

by confidence scoring alone.

L4 remains authoritative for causal typing.

---

# 50. Execution Ceiling

Before execution:

```text
expected_success
```

is a prediction.

After verified execution:

```text
observed_success
```

is evidence about that execution.

Therefore:

```text
PREDICTED_EXECUTION != EXECUTED_RESULT
```

L6 prevents predicted execution confidence from masquerading as implementation evidence.

---

# 51. H/M/L Applicability

## H — Governing/System Uncertainty

At H, uncertainty may concern:

* system objectives;
* governing constraints;
* institutional environment;
* strategic regime;
* system-wide causal structure;
* global dependency state.

H-level uncertainty may constrain many downstream conclusions.

---

## M — Subsystem Uncertainty

At M, uncertainty may concern:

* subsystem state;
* workflow;
* component interaction;
* policy interpretation;
* model selection;
* intermediate dependencies.

M uncertainty may propagate upward or downward depending on dependency structure.

---

## L — Local Uncertainty

At L, uncertainty may concern:

* observation;
* transaction;
* measurement;
* tool result;
* local state;
* individual execution.

Local uncertainty does not automatically imply system-wide uncertainty.

---

# 52. Cross-Scale Uncertainty

AMOS MUST NOT blindly aggregate uncertainty across H/M/L.

```text
HIGH_U_L
```

does not automatically mean:

```text
HIGH_U_H
```

Likewise:

```text
LOW_U_H
```

does not guarantee:

```text
LOW_U_L
```

Cross-scale uncertainty requires explicit dependency and aggregation logic.

---

# 53. Uncertainty Propagation Through RSCF

Given:

```text
P1
P2
P3
↓
C
```

L6 propagates only uncertainty dimensions that materially affect `C`.

Conceptually:

```text
U(C)
=
Propagate(
  U(P1),
  U(P2),
  U(P3),
  dependency_structure
)
```

This is not equivalent to summing uncertainty values.

---

# 54. Dependency-Aware Propagation

If `P1` changes:

```text
P1 → C1 → C2
```

then uncertainty changes SHOULD propagate through descendants.

Unrelated:

```text
P9 → C9
```

should remain unaffected.

Thus:

```text
UNCERTAINTY_PROPAGATION
=
DEPENDENCY_SELECTIVE
```

---

# 55. Uncertainty and Atomic Reasoning

Where multiple RSCFs participate in one decision, uncertainty must be evaluated across the complete load-bearing set before commit.

A local RSCF may appear sufficient while another dependent RSCF remains unresolved.

Therefore:

```text
LOCAL_CERTAINTY
!=
TRANSACTION_CERTAINTY
```

---

# 56. Control-Plane Requirements

An L6-conformant control plane SHOULD support:

```yaml
control_plane_requirements:

  uncertainty_typing: required
  confidence_ceiling_enforcement: required
  unknown_propagation: required
  competing_preservation: required

  provenance_independence_check:
    required_when_evidence_is_aggregated

  dependency_propagation: required

  scope_uncertainty_check: required
  regime_uncertainty_check: required
  freshness_uncertainty_check: required

  commit_time_revalidation:
    required_for_consequential_actions

  confidence_downgrade: supported
  selective_invalidation: supported

  fail_closed:
    required_for_critical_unknowns
```

This specifies control requirements; it does not prove runtime implementation.

---

# 57. Agent Requirements

AMOS agents SHOULD:

1. identify material unknowns;
2. classify uncertainty type;
3. distinguish confidence from evidence;
4. identify load-bearing uncertain premises;
5. preserve competing hypotheses;
6. inspect provenance independence;
7. detect scope/regime uncertainty;
8. determine whether uncertainty can flip the decision;
9. identify cheapest discriminating evidence;
10. apply confidence ceilings;
11. refuse unsupported precision;
12. downgrade conclusions when challenge succeeds;
13. preserve unresolved gaps.

---

# 58. Skill Requirements

A Skill producing consequential claims SHOULD expose uncertainty when material.

Example:

```yaml
skill_result:
  claim: ...
  claim_class: DERIVED

  uncertainty:
    evidence: LOW
    model: MODERATE
    scope: LOW
    temporal: LOW
    causal: UNKNOWN
    execution: NONE_ESTABLISHED
    provenance_independence: MODERATE

  confidence_ceiling: 0.78

  gaps:
    - causal mechanism unresolved
```

Skills MUST NOT erase uncertainty received from upstream dependencies.

---

# 59. Workflow

Canonical conceptual L6 workflow:

```text
1. RECEIVE CLAIM / REQUEST
2. IDENTIFY REQUIRED DECISION
3. LOAD LOAD-BEARING PREMISES
4. CLASSIFY EPISTEMIC STATUS
5. IDENTIFY UNKNOWNS
6. TYPE UNCERTAINTY
7. CHECK SCOPE / REGIME / FRESHNESS
8. CHECK DEPENDENCIES
9. CHECK PROVENANCE ANCESTRY
10. IDENTIFY COMPETING HYPOTHESES
11. IDENTIFY CONTRADICTIONS
12. ESTABLISH CONFIDENCE CEILINGS
13. RUN SENSITIVITY CHECK
14. IDENTIFY DECISION-FLIPPING UNCERTAINTY
15. SEEK CHEAPEST DISCRIMINATING EVIDENCE
16. UPDATE UNCERTAINTY STATE
17. PROPAGATE CHANGES SELECTIVELY
18. CLASSIFY CONCLUSION
19. IF ACTION → REVALIDATE AT COMMIT
20. RECORD FALSIFIERS / GAPS
```

---

# 60. Protocol

A minimal uncertainty protocol:

```yaml
UNCERTAINTY_REQUEST:
  claim: ...
  decision_context: ...
  required_precision: ...

UNCERTAINTY_CONTEXT:
  evidence: [...]
  provenance: [...]
  dependencies: [...]
  scope: ...
  regime: ...
  freshness: ...

UNCERTAINTY_ASSESSMENT:
  evidence_uncertainty: ...
  model_uncertainty: ...
  scope_uncertainty: ...
  temporal_uncertainty: ...
  causal_uncertainty: ...
  execution_uncertainty: ...
  provenance_independence_uncertainty: ...

  unknowns: [...]
  competing: [...]
  contradictions: [...]

  confidence_ceiling: ...

UNCERTAINTY_DECISION:
  claim_class: ...
  action_sufficiency: ...
  revalidation_required: ...
  discriminating_tests: [...]
  falsifiers: [...]
```

---

# 61. Uncertainty and Action

Uncertainty does not always prohibit action.

AMOS distinguishes:

```text
CLAIM SUFFICIENCY
DECISION SUFFICIENCY
ACTION SUFFICIENCY
```

A claim may remain uncertain while a safe reversible action is still justified.

Example structure:

```text
Cause uncertain.
Immediate reversible diagnostic test available.
```

Then:

```text
CAUSAL_CERTAINTY = INSUFFICIENT
ACTION_SUFFICIENCY = SUFFICIENT_FOR_TEST
```

This prevents unnecessary paralysis.

---

# 62. Irreversibility Escalation

Required certainty SHOULD increase as:

* stakes rise;
* reversibility falls;
* downstream dependency grows;
* safety exposure rises;
* financial/legal consequences rise;
* institutional impact increases.

Conceptually:

```text
RequiredValidation
↑
as
Irreversibility × Consequence
↑
```

This is a governance heuristic rather than a universal equation.

---

# 63. Reversible Action Under Uncertainty

When uncertainty cannot be economically resolved before action, AMOS SHOULD prefer:

```text
small
reversible
observable
bounded
repairable
```

actions over irreversible commitments, assuming other constraints permit them.

This converts uncertainty into controlled information acquisition.

---

# 64. Unknown Authority

Authority uncertainty is a critical special case.

```text
AUTHORITY = UNKNOWN
```

for an authority-requiring action yields:

```text
COMMIT = DENIED / BLOCKED
```

until authority is resolved.

Therefore:

```text
CAPABILITY != AUTHORITY
```

remains absolute.

---

# 65. Proposal Under Uncertainty

A system MAY produce:

```text
PROPOSAL
```

under uncertainty.

But proposal generation does not resolve uncertainty and does not authorize execution.

```text
PROPOSAL != COMMIT
```

A proposal SHOULD carry its unresolved assumptions and uncertainty state forward.

---

# 66. Commit-Time Uncertainty

Before consequential commit, the system SHOULD re-evaluate:

```text
Has evidence changed?
Has scope changed?
Has regime changed?
Has authority changed?
Have dependencies changed?
Has confidence fallen?
Has a new contradiction appeared?
Has a critical unknown emerged?
```

If yes:

```text
REVALIDATE
```

before effect.

---

# 67. Adversarial Validation

Consequential conclusions SHOULD be challenged using a genuinely different path.

The challenge seeks:

* contradiction;
* hidden dependency;
* correlated provenance;
* stale evidence;
* scope leakage;
* regime leakage;
* causal overreach;
* stronger competing explanation;
* execution assumption failure.

If challenge succeeds:

```text
DOWNGRADE
CONDITION
PRESERVE COMPETING
or
UNKNOWN/GAP
```

---

# 68. False Consensus

Multiple agents agreeing does not necessarily reduce uncertainty.

If all agents share:

* same prompt;
* same model;
* same source;
* same retrieval;
* same hidden assumption;

their agreement may be correlated.

Thus:

```text
AGENT_AGREEMENT
!=
INDEPENDENT_CONFIRMATION
```

---

# 69. Ensemble Uncertainty

Agent or model ensembles MAY provide useful evidence only when:

* diversity is material;
* independence is evaluated;
* shared ancestry is known;
* aggregation semantics are justified.

Otherwise ensemble consensus must remain a weak signal.

---

# 70. Memory Uncertainty

Persistent memory SHOULD preserve:

```yaml
memory_uncertainty:
  claim_class: ...
  confidence_ceiling: ...
  scope: ...
  regime: ...
  freshness: ...
  dependencies: [...]
  competing: [...]
  falsifiers: [...]
```

Memory retrieval must not convert:

```text
previously uncertain
```

into:

```text
now known
```

merely because the item was stored.

---

# 71. Compression Law

Compression MUST preserve decision-relevant uncertainty.

A summary that converts:

```text
H1 and H2 remain competing
```

into:

```text
H1 is probably correct
```

without new evidence violates L6.

Therefore:

```text
COMPRESSION
MUST NOT
CREATE CERTAINTY
```

---

# 72. Translation Law

Translation across:

* languages;
* schemas;
* abstractions;
* scales;
* domains;

may introduce uncertainty.

Translation uncertainty SHOULD be recorded when semantic equivalence is not established.

```text
TRANSLATED
!=
SEMANTICALLY_IDENTICAL
```

---

# 73. Measurement Uncertainty

Measured values SHOULD preserve known uncertainty when material.

Example:

```yaml
measurement:
  value: ...
  unit: ...
  uncertainty: ...
  method: ...
  timestamp: ...
```

AMOS MUST NOT invent measurement precision beyond the source.

---

# 74. Precision Law

Displayed precision cannot exceed justified measurement or model precision.

Therefore:

```text
12.347829
```

is not inherently more reliable than:

```text
12.3
```

Excess decimal precision may create false certainty.

---

# 75. Threshold Uncertainty

When a decision depends on a threshold:

```text
x > θ
```

uncertainty around `x` or `θ` may flip the decision.

L6 SHOULD test threshold sensitivity first.

Example:

```text
x = 0.71 ± uncertainty
θ = 0.70
```

is more decision-sensitive than:

```text
x = 0.95
θ = 0.70
```

assuming comparable uncertainty semantics.

---

# 76. Sensitivity

For consequential claims, identify:

```text
the smallest plausible premise change
that flips the conclusion.
```

If such a change is small:

```text
FRAGILE / CONDITIONAL
```

If the conclusion survives plausible perturbations:

```text
ROBUST_WITHIN_TESTED_ENVELOPE
```

not universally robust.

---

# 77. Calibration

Confidence calibration requires empirical validation against outcomes where applicable.

Without calibration evidence:

```text
confidence: 0.8
```

must not be interpreted as:

```text
80% long-run correctness
```

Thus:

```text
EPISTEMIC_SCORE != CALIBRATED_PROBABILITY
```

unless validation establishes the mapping.

---

# 78. Post-Outcome Scoring

Where predictions are made, outcomes SHOULD update calibration evidence.

Conceptually:

```text
prediction
→ outcome
→ score
→ calibration update
```

A system that never checks predictions against outcomes cannot claim empirical calibration merely from internally coherent confidence values.

---

# 79. Uncertainty Budget

For complex decisions, AMOS MAY track a bounded uncertainty budget.

The purpose is not to sum incomparable uncertainties but to identify which unresolved dimensions consume decision confidence.

Example:

```yaml
uncertainty_budget:
  dominant:
    - provenance_independence
    - regime
  secondary:
    - model
  immaterial:
    - cosmetic_metadata
```

---

# 80. Reasoning Allocation

AMOS SHOULD spend additional reasoning where:

```text
ExpectedDecisionValueOfReducingUncertainty
>
ReasoningCost
```

This supports adaptive complexity.

Do not deepen analysis merely because uncertainty exists.

Deepen it when reducing that uncertainty can materially change the result.

---

# 81. Stop Condition

Reasoning MAY stop when:

```text
Claim Sufficiency
AND
Decision Sufficiency
AND
Action Sufficiency
```

are achieved for the user's objective.

Not every uncertainty must be eliminated.

Residual uncertainty MUST remain visible if material.

---

# 82. Failure Modes

L6 recognizes at least:

### F1 — Confidence Inflation

Derived confidence exceeds load-bearing evidence.

### F2 — Unknown Fabrication

Unknown input is replaced by plausible content.

### F3 — Forced Convergence

Competing hypotheses are collapsed without discriminating evidence.

### F4 — Confidence Averaging

Incomparable confidence values are averaged without a valid model.

### F5 — Provenance Multiplication

One origin is counted as multiple independent confirmations.

### F6 — Scalar Collapse

Multidimensional uncertainty is compressed into one misleading score.

### F7 — False Precision

Unsupported decimal or probabilistic precision is presented.

### F8 — Confidence/Truth Confusion

Confidence score is treated as verification.

### F9 — Model/Evidence Confusion

Model output is treated as observation.

### F10 — Unknown/False Confusion

Unknown state is interpreted as false.

### F11 — Unknown/Neutral Confusion

Unknown state is assigned an arbitrary neutral value.

### F12 — Stale Confidence

Confidence remains unchanged after evidence expires.

### F13 — Scope-Blind Confidence

Confidence remains high outside validated scope.

### F14 — Regime-Blind Confidence

Confidence remains high after regime change.

### F15 — Causal Inflation

Associational evidence is assigned causal certainty.

### F16 — Execution Inflation

Expected execution success is treated as observed success.

### F17 — Consensus Inflation

Correlated agent agreement is treated as independent evidence.

### F18 — Compression Certainty

Summarization removes uncertainty qualifiers.

### F19 — Irreversible Action on Critical Unknown

System commits despite unresolved load-bearing uncertainty.

### F20 — Global Uncertainty Contamination

One local unknown unnecessarily invalidates unrelated claims.

---

# 83. Repair / Recovery

Canonical repair flow:

```text
DETECT UNCERTAINTY FAILURE
        ↓
IDENTIFY AFFECTED CLAIM
        ↓
IDENTIFY UNCERTAINTY TYPE
        ↓
TRACE LOAD-BEARING DEPENDENCIES
        ↓
RESTORE LOST UNKNOWN / COMPETING STATE
        ↓
RECOMPUTE CONFIDENCE CEILING
        ↓
SELECTIVELY INVALIDATE DESCENDANTS
        ↓
SEEK DISCRIMINATING EVIDENCE
        ↓
REVALIDATE
        ↓
RESTORE / DOWNGRADE / CONDITION / QUARANTINE
```

---

# 84. Confidence Repair

If:

```text
C confidence = 0.90
```

but a load-bearing premise has ceiling:

```text
0.65
```

then repair requires:

```text
C ceiling ≤ 0.65
```

unless independent revalidation exists.

The previous `0.90` state should be recorded as invalidated rather than silently overwritten where provenance/history matters.

---

# 85. Unknown Restoration

If an earlier process fabricated a value for an unknown field:

```text
UNKNOWN → assumed X
```

repair requires:

```text
assumed X → UNKNOWN
```

followed by selective revalidation of dependent claims.

---

# 86. Competing Restoration

If:

```text
H1 / H2
```

were incorrectly collapsed into `H1`, repair restores:

```text
COMPETING:
  H1
  H2
```

and invalidates conclusions that depended on false convergence.

---

# 87. Selective Invalidation

If premise `P` becomes uncertain:

```text
P
├── C1
│   └── C2
└── C3
```

then affected descendants are reconsidered.

Unrelated claims remain valid.

```text
LOCAL_FAILURE
!=
GLOBAL_RESET
```

---

# 88. Validators

Conceptual L6 validators include:

```text
validate_uncertainty_type()
validate_unknown_propagation()
validate_confidence_ceiling()
validate_competing_preservation()
validate_confidence_semantics()

validate_source_independence()
validate_provenance_topology()

validate_scope_uncertainty()
validate_regime_uncertainty()
validate_temporal_uncertainty()
validate_causal_uncertainty()
validate_execution_uncertainty()

validate_dependency_propagation()
validate_precision()
validate_calibration_claim()

validate_commit_uncertainty()
validate_gap_classification()
```

---

# 89. Minimum Validator Tests

## Test U6-T1 — Unknown Propagation

Input:

```text
A = known
B = unknown and load-bearing
C = f(A,B)
```

Expected:

```text
C = UNKNOWN / CONDITIONAL
```

not fabricated.

---

## Test U6-T2 — Weakest Premise Ceiling

Input:

```text
P1 ceiling = 0.91
P2 ceiling = 0.62
P3 ceiling = 0.87
```

all load-bearing.

Expected:

```text
C ceiling ≤ 0.62
```

---

## Test U6-T3 — Competing Preservation

Input:

```text
H1 and H2 have insufficient discriminating evidence.
```

Expected:

```text
COMPETING
```

not arbitrary winner.

---

## Test U6-T4 — No Probability Fabrication

Input:

```text
H1 and H2 remain competing.
```

Expected:

```text
No automatic 50/50 assignment.
```

---

## Test U6-T5 — Provenance Correlation

Input:

```text
S2 summarizes S1
S3 paraphrases S1
```

Expected:

```text
independent_origins = 1
```

where lineage is established.

---

## Test U6-T6 — Confidence Downgrade

Input:

```text
new contradiction discovered
```

Expected:

```text
confidence ceiling reconsidered
```

not frozen.

---

## Test U6-T7 — Scope Uncertainty

Input:

```text
claim validated only for S1
request concerns S2
```

Expected:

```text
S2 = UNKNOWN / CONDITIONAL
```

unless transfer evidence exists.

---

## Test U6-T8 — Regime Uncertainty

Input:

```text
claim depends on R1
current regime unresolved between R1 and R2
```

Expected:

```text
current applicability confidence bounded
```

---

## Test U6-T9 — False Precision

Input:

```text
source precision = 2 significant figures
```

Expected:

```text
derived output does not imply unsupported measurement precision
```

---

## Test U6-T10 — Execution Distinction

Input:

```text
plan predicted to work
no execution performed
```

Expected:

```text
implementation_status != VERIFIED_EXECUTION
```

---

## Test U6-T11 — Independent Revalidation

Input:

```text
Path A has weak premise.
Independent Path B directly validates C.
```

Expected:

```text
C may receive stronger ceiling from Path B
```

if independence is demonstrated.

---

## Test U6-T12 — Local Unknown

Input:

```text
unrelated field X = UNKNOWN
C does not depend on X
```

Expected:

```text
C not automatically UNKNOWN
```

---

# 90. Falsifiers

The L6 specification is falsified or requires revision if authoritative canon establishes that:

1. uncertainty classes differ materially from those represented here;
2. confidence ceiling semantics differ;
3. the proposed `0.95` ceiling is superseded;
4. COMPETING hypotheses are governed by a different canonical structure;
5. UNKNOWN propagation uses different canonical rules;
6. an assumed dependency between L6 and L0-L5 is incorrect;
7. executable AMOS runtime behavior contradicts claimed partial implementation;
8. canonical confidence values have validated probabilistic semantics inconsistent with this document;
9. stronger canon establishes different uncertainty composition rules.

These falsifiers apply to the specification, not to empirical uncertainty itself.

---

# 91. Core Invariants

## L6-I1 — Uncertainty Visibility

```text
MATERIAL_UNCERTAINTY
MUST REMAIN REPRESENTED
```

## L6-I2 — Unknown Integrity

```text
UNKNOWN != PLAUSIBLE_GUESS
```

## L6-I3 — Confidence Ceiling

```text
CONFIDENCE
≤
SUPPORTED_CEILING
```

## L6-I4 — Weakest Load-Bearing Premise

```text
DERIVED_CEILING
≤
WEAKEST_LOAD_BEARING_PREMISE
```

unless independently revalidated.

## L6-I5 — Competing Preservation

```text
INCOMPARABLE_COMPETING
!=
AVERAGED_CONCLUSION
```

## L6-I6 — Provenance Independence

```text
CORRELATED_EVIDENCE
!=
INDEPENDENT_CONFIRMATION
```

## L6-I7 — Epistemic Separation

```text
SOURCE
!=
DERIVED
!=
MODEL
!=
UNKNOWN
```

## L6-I8 — Confidence/Truth Separation

```text
CONFIDENCE != TRUTH
```

## L6-I9 — Model/Observation Separation

```text
MODEL_OUTPUT != OBSERVATION
```

## L6-I10 — Prediction/Execution Separation

```text
EXPECTED_RESULT != OBSERVED_RESULT
```

## L6-I11 — Scope Preservation

```text
HIGH_CONFIDENCE_IN_SCOPE
!=
HIGH_CONFIDENCE_OUTSIDE_SCOPE
```

## L6-I12 — Regime Preservation

```text
CONFIDENCE_R1
!=
CONFIDENCE_R2
```

without transfer evidence.

## L6-I13 — Reversibility

```text
CONFIDENCE_MAY_DECREASE
```

when evidence changes.

## L6-I14 — Selective Propagation

```text
LOCAL_UNKNOWN
!=
GLOBAL_UNKNOWN
```

unless dependency closure makes it global.

## L6-I15 — No Fabricated Precision

```text
OUTPUT_PRECISION
≤
JUSTIFIED_PRECISION
```

---

# 92. Hard Boundaries

```text
UNCERTAINTY != IGNORANCE_ERASURE

UNKNOWN != FALSE

UNKNOWN != ZERO

UNKNOWN != 50/50

CONFIDENCE != EVIDENCE

CONFIDENCE != TRUTH

HIGH_CONFIDENCE != VERIFIED

MODEL != OBSERVATION

DERIVED != SOURCE

COMPETING != AVERAGED

MULTIPLE_SOURCES != INDEPENDENT_SOURCES

AGENT_AGREEMENT != INDEPENDENT_CONFIRMATION

MORE_REASONING != MORE_EVIDENCE

PRECISION != CERTAINTY

PREDICTION != EXECUTION

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

UNKNOWN/GAP != PASS
```

---

# 93. Dependencies

Primary conceptual dependency spine:

```text
L0_INTEGRITY
    ↓
L1_EPISTEMIC
    ↓
L2_PROVENANCE
    ↓
L3_DEPENDENCY
    ↓
L4_CAUSAL
    ↓
L5_SCOPE_REGIME
    ↓
L6_UNCERTAINTY
```

L6 relies on:

```yaml
dependencies:

  L0_INTEGRITY:
    role: prevents uncertainty erasure for fluency or convenience

  L1_EPISTEMIC:
    role: supplies epistemic claim classes

  L2_PROVENANCE:
    role: establishes source identity and independence

  L3_DEPENDENCY:
    role: identifies load-bearing premises and propagation paths

  L4_CAUSAL:
    role: bounds causal uncertainty and causal claim strength

  L5_SCOPE_REGIME:
    role: supplies scope, regime, freshness, and temporal applicability
```

L6 MUST NOT weaken any upstream law.

---

# 94. Interaction with RSCF

A mature RSCF SHOULD support:

```yaml
rscf:
  claim: ...
  claim_class: ...

  evidence: [...]
  provenance: [...]

  scope: ...
  regime: ...
  freshness: ...

  dependencies: [...]

  uncertainty:
    evidence: ...
    model: ...
    scope: ...
    temporal: ...
    causal: ...
    execution: ...
    provenance_independence: ...

  competing: [...]
  falsifiers: [...]

  confidence_ceiling: ...
```

The uncertainty state belongs to the proof capsule, not merely the presentation layer.

---

# 95. RSCF Promotion Rule

A claim may be promoted only when its uncertainty state permits the target class.

Conceptually:

```text
UNKNOWN/GAP
→
CONDITIONAL
→
DERIVED / MODEL
→
VERIFIED
```

is not an automatic ladder.

Promotion requires class-appropriate evidence.

A claim may also move backward:

```text
VERIFIED
→
CONDITIONAL
```

if scope, regime, provenance, freshness, or dependency validity changes.

---

# 96. Interaction with GMEF

Where L6 uncertainty concerns a proposed machine/system change, GMEF SHOULD receive:

```text
uncertainty state
confidence ceiling
competing hypotheses
rollback conditions
validation requirements
authority state
```

A technically plausible mutation cannot be promoted merely because uncertainty was omitted.

---

# 97. Implementation Boundary

Current declared implementation status:

```text
LOGIC_EXECUTABLE_IN_PART
```

This means only that portions of the logic can be represented or enforced through AMOS validators/control structures.

It MUST NOT be expanded to:

```text
FULLY_IMPLEMENTED
```

or:

```text
EMPIRICALLY_VALIDATED
```

without executable evidence.

Therefore:

```text
LOGIC_EXECUTABLE_IN_PART
!=
RUNTIME_COMPLETE
```

---

# 98. Evidence / Provenance

Current supplied evidence for this artifact includes the explicit seed specification:

```text
U-1 Typed Uncertainty
U-2 Confidence Ceiling
U-3 Ambiguity Preservation
U-4 Unknown Propagation
```

and the stated enforcement contract:

```text
Confidence ceilings in validators;
competing-hypothesis sets preserved verbatim;
UNKNOWN/GAP labels propagate through dependency chains.
```

The remaining structures in this document are best classified as:

```text
AMOS_MODEL / DERIVED STRUCTURAL COMPLETION
```

until reconciled against authoritative canon sources.

No claim is made here that every expanded law is verbatim source canon.

---

# 99. Gap Status

```yaml
gap_status:

  seed_laws:
    U_1_TYPED_UNCERTAINTY: PROVIDED
    U_2_CONFIDENCE_CEILING: PROVIDED
    U_3_AMBIGUITY_PRESERVATION: PROVIDED
    U_4_UNKNOWN_PROPAGATION: PROVIDED

  structural_completion:
    uncertainty_types: PROVIDED
    typed_inputs_outputs: PROVIDED
    state_model: PROVIDED
    operators: PROVIDED
    invariants: PROVIDED
    dependencies: PROVIDED
    hml_applicability: PROVIDED
    control_plane_requirements: PROVIDED
    agent_contract: PROVIDED
    skill_contract: PROVIDED
    workflow: PROVIDED
    protocol: PROVIDED
    failure_modes: PROVIDED
    repair_recovery: PROVIDED
    validators: PROVIDED
    falsifiers: PROVIDED

  unresolved:
    authoritative_epistemics_reconciliation: REQUIRED
    exact_0_95_ceiling_canon_status: CONDITIONAL
    quantitative_confidence_semantics: UNVALIDATED
    calibration_semantics: UNVALIDATED
    full_runtime_implementation: NOT_ESTABLISHED
    empirical_validation: NOT_ESTABLISHED
    final_canon_approval: REQUIRED
```

---

# 100. RSCF Completion State

```yaml
claim_class: AMOS_MODEL

claim:
  "L6_UNCERTAINTY governs explicit, typed, dependency-aware,
   provenance-aware uncertainty and prevents unsupported certainty
   creation through inference, aggregation, compression, consensus,
   or missing-data fabrication."

evidence:
  - supplied L6 seed specification
  - U-1 Typed Uncertainty
  - U-2 Confidence Ceiling
  - U-3 Ambiguity Preservation
  - U-4 Unknown Propagation
  - supplied enforcement requirements

provenance:
  origin_architect: Trang Phan
  artifact_family: AMOS_OS
  layer: 01_CANON/01_CORE_LAWS
  path: 01_CANON/01_CORE_LAWS/L6_UNCERTAINTY.md
  derivation_status: PROPOSED_STRUCTURAL_COMPLETION
  updated: 2026-08-26

scope:
  system: AMOS
  applies_to:
    - claims
    - evidence
    - models
    - RSCFs
    - agents
    - skills
    - workflows
    - memory
    - predictions
    - decisions
    - governed actions

regime:
  - reasoning
  - retrieval
  - validation
  - memory
  - governance
  - execution

freshness:
  revalidate_on:
    - epistemics_canon_change
    - confidence_semantics_change
    - provenance_change
    - dependency_change
    - scope_change
    - regime_change
    - contradiction
    - validator_change
    - runtime_change

dependencies:
  - L0_INTEGRITY
  - L1_EPISTEMIC
  - L2_PROVENANCE
  - L3_DEPENDENCY
  - L4_CAUSAL
  - L5_SCOPE_REGIME

competing:
  - authoritative epistemics canon may define different confidence ceiling semantics
  - numerical uncertainty may be inappropriate for some epistemic classes
  - domain-specific probabilistic models may require richer uncertainty structures
  - some uncertainty dimensions may be incomparable rather than aggregatable

falsifiers:
  - authoritative canon supersedes U-1 through U-4
  - authoritative canon defines incompatible confidence semantics
  - runtime evidence disproves claimed partial executable enforcement
  - UNKNOWN is silently converted into fabricated values
  - competing hypotheses are collapsed without discriminating evidence
  - derived confidence exceeds a load-bearing premise without independent revalidation
  - correlated evidence is treated as independent confirmation

confidence_ceiling:
  seed_specification: HIGH
  structural_completion: AMOS_MODEL
  exact_canon_equivalence: UNVERIFIED
  runtime_implementation: PARTIAL_UNVERIFIED
  empirical_calibration: UNKNOWN
```

---

# 101. Canon Promotion Gate

Before final canon promotion:

```text
[ ] Trang Phan / steward approval
[ ] authoritative epistemics canon reconciled
[ ] U-1 semantics confirmed
[ ] U-2 semantics confirmed
[ ] U-3 semantics confirmed
[ ] U-4 semantics confirmed
[ ] 0.95 hard ceiling confirmed or superseded
[ ] confidence semantics formally typed
[ ] calibrated probability distinguished from epistemic score
[ ] uncertainty vector reviewed
[ ] UNKNOWN propagation rules reviewed
[ ] COMPETING semantics reviewed
[ ] provenance-independence requirements reviewed
[ ] L0-L5 compatibility confirmed
[ ] H/M/L propagation reviewed
[ ] validators mapped to implementation
[ ] executable tests run where implementation exists
[ ] failure/recovery paths validated
[ ] downstream dependencies inspected
[ ] supersession lineage recorded
[ ] version assigned
```

Until then:

```text
STATUS = PROPOSED_SPECIFICATION
EPISTEMIC_CLASS = AMOS_MODEL
CANONICAL_STATUS = CONDITIONAL
```

not:

```text
STATUS = VERIFIED_FINAL_CANON
```

---

[[00_ROOT_MOC|AMOS MOC]]

---

**Related:** [[00_HOME]] · AMOS_RSCF_NODES · LAW_HIERARCHY · L0_INTEGRITY · L1_EPISTEMIC · L2_PROVENANCE · L3_DEPENDENCY · L4_CAUSAL · L5_SCOPE_REGIME

---

RSCF-NODE

node_id: l6_uncertainty

node_type: core_law

path: 01_CANON/01_CORE_LAWS/L6_UNCERTAINTY.md

RSCF-RELATIONS:

* CHILD_OF: LAW_HIERARCHY
* DEPENDS_ON: L0_INTEGRITY
* DEPENDS_ON: L1_EPISTEMIC
* DEPENDS_ON: L2_PROVENANCE
* DEPENDS_ON: L3_DEPENDENCY
* DEPENDS_ON: L4_CAUSAL
* DEPENDS_ON: L5_SCOPE_REGIME
* INDEXED_BY: [[00_HOME]]
* INDEXED_BY: AMOS_RSCF_NODES

claim_class: AMOS_MODEL

```
```

---
**MOC:** [[01_CORE_LAWS_MOC]]
