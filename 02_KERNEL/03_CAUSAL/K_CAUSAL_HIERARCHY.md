---
title: K CAUSAL HIERARCHY
type: note
source: 02_KERNEL/03_CAUSAL
artifact_id: AMOS-OS-K-CAUSAL-HIERARCHY
canonical_name: K_CAUSAL_HIERARCHY
artifact_type: kernel_causal_hierarchy_contract
status: AMOS_MODEL
conclusion_class: AMOS_MODEL
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
plane: KERNEL
kernel_family: CAUSAL
domain: causal-hierarchy
scope: AMOS_OS
created: 2026-08-25
updated: 2026-08-25
tags:
- amos-os
- kernel
- core
- canon-group/tech-ai
- canon/model
- kernel/causal
- kernel/causal-hierarchy
- kernel/causal-closure
- kernel/causal-epoch
- kernel/dependency
- kernel/provenance
- kernel/regime
- kernel/scope
- kernel/multi-hypothesis
- kernel/validation
- rscf/state/model
- causal/hierarchy
- causal/mechanism
- causal/confounding
- causal/mediation
- causal/feedback
- causal/effect
- topic/causal-hierarchy
- topic/causal-inference
aliases:
- AMOS Causal Hierarchy Kernel - Causal Hierarchy Kernel - K Causal Hierarchy - K_CAUSAL_HIERA
---

# K CAUSAL HIERARCHY
> **AMOS Core target:** `v4.4`
> **Origin architect / steward:** Trang Phan
> **Plane:** `02_KERNEL`
> **Status:** `AMOS_MODEL`
> **Conclusion class:** `AMOS_MODEL`
## Purpose
`K_CAUSAL_HIERARCHY` defines the AMOS kernel contract for distinguishing levels and types of causal knowledge.
Its central purpose is to prevent weaker evidence from being silently promoted into stronger causal claims.
The governing rule is:
```text
OBSERVATION
!=
ASSOCIATION
!=
CORRELATION
!=
TEMPORAL ORDER
!=
DEPENDENCY
!=
MECHANISM
!=
INTERVENTIONAL EFFECT
!=
COUNTERFACTUAL EFFECT
```
A claim may move upward in the causal hierarchy only when evidence appropriate to the stronger causal class is available.
Structural similarity, sequence, repetition, authority, model confidence, or fluent explanation cannot substitute for causal evidence.
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


# 1. Core Law

For evidence state `E` and causal claim `C`:

```text
LICENSE(E, C)
```

must hold before `C` can be accepted at its claimed causal level.

Therefore:

```text
CAUSAL CLAIM STRENGTH
<=
CAUSAL LICENSE OF LOAD-BEARING EVIDENCE
```

A stronger conclusion cannot be derived merely because it is compatible with weaker evidence.

---

# 2. Causal Firewall

AMOS distinguishes at minimum:

```text
OBSERVATION
ASSOCIATION
CORRELATION
TEMPORAL PRECEDENCE
STRUCTURAL DEPENDENCY
ENABLING CONDITION
MECHANISM
MEDIATION
CONFOUNDING
NECESSARY CONDITION
SUFFICIENT CONDITION
CAUSAL CONTRIBUTION
INTERVENTIONAL EFFECT
COUNTERFACTUAL EFFECT
FEEDBACK
```

These relations are not interchangeable.

---

# 3. Base Hierarchy

A useful conceptual hierarchy is:

```text
L0  OBSERVATION
↓
L1  ASSOCIATION
↓
L2  CORRELATION
↓
L3  TEMPORAL / STRUCTURAL DEPENDENCY
↓
L4  CAUSAL CANDIDATE
↓
L5  MECHANISM-SUPPORTED RELATION
↓
L6  INTERVENTIONAL CAUSAL EFFECT
↓
L7  COUNTERFACTUAL CAUSAL EFFECT
```

This hierarchy represents increasing causal commitment.

It is not a claim that every causal problem follows a single linear ladder.

Some causal relation types are orthogonal and require separate typing.

---

# 4. L0 — Observation

An observation records what was measured, reported, or detected.

Example:

```text
X = 7
Y = 12
```

or:

```text
EVENT A OCCURRED
EVENT B OCCURRED
```

Observation alone licenses no causal relation.

```text
OBSERVED(X)
+
OBSERVED(Y)

↛

X CAUSES Y
```

---

# 5. L1 — Association

Association means variables or events appear related under a defined measurement context.

```text
ASSOC(X, Y | S, R, T)
```

where:

```text
S = scope
R = regime
T = temporal context
```

Association may motivate causal investigation.

It does not establish causation.

---

# 6. L2 — Correlation

Correlation is a typed statistical relationship.

Conceptually:

```text
CORR(X, Y) != 0
```

may support:

```text
X and Y covary
```

but does not alone support:

```text
X → Y
```

because alternatives include:

```text
Y → X
Z → X AND Z → Y
SELECTION BIAS
MEASUREMENT BIAS
FEEDBACK
CHANCE
MODEL MISSPECIFICATION
```

---

# 7. Correlation Firewall

```text
CORRELATION
!=
CAUSATION
```

remains a hard invariant.

Likewise:

```text
HIGH CORRELATION
!=
STRONG CAUSAL PROOF
```

and:

```text
REPEATED CORRELATION
!=
INDEPENDENT CAUSAL CONFIRMATION
```

when the observations share provenance or confounding structure.

---

# 8. L3 — Temporal Precedence

Suppose:

```text
X occurs before Y
```

This may satisfy one condition needed by some causal hypotheses.

It does not establish:

```text
X → Y
```

Therefore:

```text
BEFORE(X, Y)
!=
CAUSES(X, Y)
```

Temporal precedence is evidence about ordering, not sufficient causal evidence.

---

# 9. Structural Dependency

A structural dependency means one component depends on another according to a system model.

```text
A DEPENDS_ON B
```

does not necessarily mean:

```text
B CAUSES A
```

in the empirical causal sense.

Examples include:

```text
software dependency
logical dependency
schema dependency
authority dependency
derivation dependency
execution dependency
```

These must remain typed.

---

# 10. Dependency Firewall

```text
DEPENDENCY
!=
CAUSATION
```

A dependency edge may become part of a causal model only when the semantics of the edge justify causal interpretation.

---

# 11. L4 — Causal Candidate

A causal candidate is a hypothesis such as:

```text
H1: X → Y
```

supported enough to investigate but not yet licensed as a validated causal conclusion.

Candidate state should preserve alternatives:

```text
H1: X → Y
H2: Y → X
H3: Z → {X, Y}
H4: X ↔ Y
H5: ASSOCIATION WITHOUT CAUSAL EFFECT
```

Until discriminating evidence exists:

```text
STATE = COMPETING
```

where appropriate.

---

# 12. L5 — Mechanism-Supported Relation

A mechanism describes a plausible process through which one state influences another.

```text
X
↓
M
↓
Y
```

A mechanism may substantially strengthen a causal hypothesis.

But:

```text
PLAUSIBLE MECHANISM
!=
DEMONSTRATED CAUSAL EFFECT
```

A mechanism can be real while its effect is negligible, context-dependent, blocked, or dominated by other pathways.

---

# 13. Mechanism Typing

A mechanism claim should identify:

```yaml
mechanism:
  source:
  target:
  mediator:
  conditions:
  scope:
  regime:
  evidence:
  competing_mechanisms:
  falsifiers:
```

Mechanisms without explicit conditions risk scope leakage.

---

# 14. Enabling Condition

An enabling condition makes an outcome or mechanism possible.

```text
E ENABLES Y
```

does not imply:

```text
E IS SUFFICIENT FOR Y
```

or:

```text
E IS THE PRIMARY CAUSE OF Y
```

Therefore:

```text
ENABLING
!=
SUFFICIENT
```

---

# 15. Necessary Condition

`X` is necessary for `Y` under scope `S` when:

```text
¬X → ¬Y
```

within the defined applicability envelope.

This does not mean:

```text
X → Y
```

Therefore:

```text
NECESSARY
!=
SUFFICIENT
```

---

# 16. Sufficient Condition

`X` is sufficient for `Y` under conditions `C` when:

```text
X ∧ C → Y
```

within the relevant scope and regime.

Sufficiency must not be generalized beyond those conditions.

---

# 17. Necessary and Sufficient

When both are established:

```text
X ↔ Y
```

may represent a necessary-and-sufficient relation under explicit conditions.

This is a strong claim.

It requires correspondingly strong evidence.

---

# 18. Causal Contribution

Many real systems have multiple contributing causes.

```text
X contributes to Y
```

is weaker than:

```text
X is necessary for Y
```

or:

```text
X is sufficient for Y
```

AMOS should preserve this distinction rather than forcing binary causation.

---

# 19. Mediation

Mediation represents an intermediate causal path:

```text
X → M → Y
```

where `M` transmits some or all of the causal influence of `X` on `Y`.

A mediation claim requires evidence distinguishing:

```text
DIRECT EFFECT
INDIRECT EFFECT
TOTAL EFFECT
```

when those distinctions are material.

---

# 20. Mediation Firewall

Observing:

```text
X associated with M
M associated with Y
```

does not alone prove:

```text
X → M → Y
```

The path remains a model until appropriately validated.

---

# 21. Confounding

A confounder `Z` may produce:

```text
Z → X
Z → Y
```

creating an apparent relation:

```text
X ↔ Y
```

without the proposed direct causal relation.

Therefore every consequential causal claim should consider material confounding alternatives.

---

# 22. Hidden Confounding

Unknown or unmeasured variables may remain possible.

Therefore:

```text
NO KNOWN CONFOUNDER
!=
NO CONFOUNDER EXISTS
```

Confidence must respect the evidence available.

---

# 23. Selection Effects

Selection may induce misleading associations.

Conceptually:

```text
X → S ← Y
```

Conditioning on `S` can create an apparent relation between `X` and `Y`.

AMOS causal reasoning must therefore distinguish:

```text
OBSERVED ASSOCIATION
```

from:

```text
ASSOCIATION AFTER SELECTION
```

when selection is material.

---

# 24. Collider Structure

A collider:

```text
X → Z ← Y
```

requires special treatment.

Conditioning on `Z` can create dependence between otherwise independent causes.

Therefore:

```text
CONDITIONING
```

is not automatically harmless.

---

# 25. Common Cause

A common cause structure:

```text
Z
├──→ X
└──→ Y
```

is a primary competing explanation for apparent `X → Y` relations.

Causal analysis should explicitly test it when plausible.

---

# 26. Common Effect

A common effect structure:

```text
X ──→ Z
Y ──→ Z
```

must not be confused with:

```text
X → Y
```

or:

```text
Y → X
```

---

# 27. Chain

A causal chain:

```text
X → M → Y
```

may support transitive causal influence under appropriate conditions.

But:

```text
X → M
M → Y
```

does not automatically imply a simple invariant effect of `X` on `Y`.

Intervention semantics, blockers, nonlinearities, regimes, and feedback may matter.

---

# 28. Fork

A causal fork:

```text
X ← Z → Y
```

represents common-cause structure.

This must remain distinguishable from:

```text
X → Y
```

---

# 29. Feedback

Feedback occurs when causal influence participates in a loop.

Conceptually:

```text
X → Y
↑   ↓
└── Z
```

or:

```text
X ↔ Y
```

over time.

Feedback requires temporal or state indexing to avoid treating cyclic influence as an instantaneous contradiction.

---

# 30. Feedback Firewall

```text
FEEDBACK
!=
SIMPLE BIDIRECTIONAL CORRELATION
```

A feedback claim requires evidence that reciprocal causal influence actually occurs.

---

# 31. Positive Feedback

Positive feedback amplifies change.

Conceptually:

```text
ΔX
→
ΔY
→
further ΔX
```

The label `positive` refers to amplification structure, not desirability.

---

# 32. Negative Feedback

Negative feedback counteracts deviation.

```text
ΔX
→
response
→
reduce ΔX
```

Again:

```text
NEGATIVE
!=
BAD
```

It describes causal control structure.

---

# 33. Direct Cause

A direct causal edge:

```text
X → Y
```

means the modeled causal relationship is not represented as mediated by another variable in the relevant model.

But directness is model-relative.

A more detailed model may reveal mediators.

Therefore:

```text
DIRECT
```

must inherit the model's granularity and scope.

---

# 34. Indirect Cause

An indirect effect occurs through one or more mediators:

```text
X → M1 → M2 → Y
```

The path should remain explicit when it matters to intervention or explanation.

---

# 35. Total Causal Effect

Conceptually:

```text
TOTAL_EFFECT
=
DIRECT_EFFECT
+
INDIRECT_EFFECTS
```

where the mathematical decomposition is valid for the model used.

AMOS must not assume additive decomposition universally.

---

# 36. L6 — Interventional Effect

An interventional causal claim concerns what changes when an intervention changes `X`.

Conceptually:

```text
P(Y | do(X=x1))
!=
P(Y | do(X=x0))
```

supports a causal effect under the relevant assumptions.

This is stronger than observational association.

---

# 37. Intervention Firewall

```text
P(Y | X)
```

is not generally equivalent to:

```text
P(Y | do(X))
```

Therefore observational prediction and causal intervention must remain distinct.

---

# 38. Intervention Scope

An intervention effect inherits:

```text
POPULATION
ENVIRONMENT
TIME
REGIME
INTERVENTION TYPE
MEASUREMENT METHOD
ASSUMPTIONS
```

An intervention validated in one envelope must not silently generalize to another.

---

# 39. Natural vs Artificial Intervention

Different interventions on nominally the same variable may produce different effects.

Therefore:

```text
SET X
```

is insufficiently precise when intervention mechanism matters.

The intervention should be typed where necessary.

---

# 40. L7 — Counterfactual Effect

Counterfactual reasoning concerns alternative outcomes for the same modeled unit or state under different interventions.

Conceptually:

```text
Y_x
```

versus:

```text
Y_x'
```

The counterfactual level makes stronger assumptions than ordinary association.

---

# 41. Counterfactual Firewall

```text
OBSERVED Y AFTER X
```

does not directly reveal:

```text
WHAT Y WOULD HAVE BEEN
WITHOUT X
```

The missing counterfactual must be inferred through an appropriately justified model or design.

---

# 42. Relationship to K_COUNTERFACTUAL

`K_COUNTERFACTUAL` governs the logical construction and evaluation of counterfactual branches.

`K_CAUSAL_HIERARCHY` determines what causal strength those branches can support.

```text
COUNTERFACTUAL BRANCH
!=
COUNTERFACTUAL PROOF
```

---

# 43. Causal Direction

Given association:

```text
X — Y
```

possible directions include:

```text
X → Y
Y → X
X ← Z → Y
X ↔ Y
NO CAUSAL EDGE
```

AMOS must not select direction from association alone unless additional evidence licenses it.

---

# 44. Causal Graph

A causal model may be represented as:

```text
G = (V, E)
```

where:

```text
V = typed variables / states
E = typed causal edges
```

Each causal edge should carry sufficient metadata to identify its epistemic status.

---

# 45. Typed Causal Edge

Recommended conceptual representation:

```yaml
causal_edge:
  source:
  target:

  relation_type:
  direction:

  conclusion_class:

  evidence: []
  provenance: []

  scope:
  regime:
  temporal_validity:

  assumptions: []
  confounders: []
  mediators: []

  falsifiers: []
  invalidation_conditions: []

  confidence_ceiling:
```

---

# 46. Relation Types

Recommended relation vocabulary:

```text
ASSOCIATED_WITH
CORRELATED_WITH
PRECEDES
DEPENDS_ON
ENABLES
INHIBITS
CONTRIBUTES_TO
MEDIATES
CONFOUNDS
NECESSARY_FOR
SUFFICIENT_FOR
CAUSES
DIRECTLY_CAUSES
INDIRECTLY_CAUSES
MODERATES
FEEDBACKS_WITH
```

Do not collapse these into a generic `RELATED_TO` when causal semantics matter.

---

# 47. Epistemic Classes

Causal claims retain AMOS conclusion classes:

```text
VERIFIED
DERIVED
MODEL
CONDITIONAL
COMPETING
UNKNOWN/GAP
```

A causal relation represented in a model is not automatically `VERIFIED`.

---

# 48. Source Claims

A document may assert:

```text
X causes Y
```

Without independent validation, AMOS records:

```text
SOURCE_CLAIM:
"source asserts X causes Y"
```

not automatically:

```text
VERIFIED:
X causes Y
```

---

# 49. Evidence Typing

Relevant evidence classes include:

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL
DECISION
UNKNOWN
```

The evidence type determines what causal inference it can support.

---

# 50. Evidence Strength Firewall

A useful constraint is:

```text
CAUSAL CONCLUSION
<=
WEAKEST LOAD-BEARING CAUSAL PREMISE
```

unless the weak premise has been independently revalidated or replaced.

---

# 51. Provenance Independence

Suppose three claims all descend from one source:

```text
SOURCE A
├── REPORT B
├── REPORT C
└── REPORT D
```

Then:

```text
B + C + D
```

do not constitute three independent causal confirmations.

---

# 52. Provenance Topology

Causal validation should preserve:

```text
SOURCE IDENTITY
ANCESTRY
DEPENDENCY
CORRELATION RISK
FRESHNESS
REGIME
```

when these can affect causal confidence.

---

# 53. Causal Sybil Hardening

Repeated claims can create false apparent confirmation.

Therefore:

```text
REPETITION
!=
INDEPENDENT VALIDATION
```

and:

```text
POPULARITY
!=
CAUSAL PROOF
```

---

# 54. Scope Firewall

Every important causal claim inherits an applicability envelope.

```yaml
causal_scope:
  system:
  population:
  environment:
  scale:
  time:
  regime:
  measurement_method:
  assumptions: []
```

Causal validity outside this envelope remains unestablished.

---

# 55. Cross-Scale Causation

A causal relation at one scale:

```text
MICRO
```

does not automatically establish the analogous relation at:

```text
MACRO
```

and vice versa.

Therefore:

```text
STRUCTURAL SIMILARITY ACROSS SCALE
!=
CAUSAL TRANSFER
```

---

# 56. Cross-Domain Causation

A causal pattern validated in domain `D1` may inspire a model for `D2`.

But:

```text
D1 CAUSAL MODEL
→
D2 CAUSAL MODEL
```

remains:

```text
MODEL
```

until independently validated in `D2`.

---

# 57. Regime Firewall

Suppose:

```text
R0:
X → Y
```

A regime transition may produce:

```text
R1:
X ↛ Y
```

or:

```text
R1:
X → Z → Y
```

Therefore causal conclusions must bind to regime where material.

---

# 58. Causal Epoch Integration

`K_CAUSAL_EPOCH` binds causal validity to bounded causal states.

Thus:

```text
CAUSAL HIERARCHY
=
WHAT LEVEL OF CAUSAL CLAIM?

CAUSAL EPOCH
=
WHEN / UNDER WHAT STATE IS IT VALID?
```

---

# 59. Causal Closure Integration

`K_CAUSAL_CLOSURE` determines which causal dependencies are load-bearing.

`K_CAUSAL_HIERARCHY` determines how strongly each edge may be interpreted.

Together:

```text
EDGE TYPE
+
EVIDENCE LICENSE
+
DEPENDENCY CLOSURE
+
EPOCH
=
BOUNDED CAUSAL PROOF STRUCTURE
```

---

# 60. Structural Reasoning Integration

`K_STRUCTURAL_REASONING` may identify:

```text
A connected to B
A depends on B
A precedes B
A resembles B
```

None of these automatically license:

```text
A causes B
```

`K_CAUSAL_HIERARCHY` provides the causal firewall between structure and causation.

---

# 61. Multi-Hypothesis Integration

When causal direction is unresolved:

```text
H1: X → Y
H2: Y → X
H3: Z → X,Y
```

`K_MULTI_HYPOTHESIS` preserves alternatives.

`K_CAUSAL_HIERARCHY` prevents premature promotion of one hypothesis.

---

# 62. Metacognitive Challenge

`K_METACOGNITION` should challenge consequential causal conclusions for:

```text
CAUSAL OVERREACH
HIDDEN CONFOUNDING
PROVENANCE CORRELATION
REGIME LEAKAGE
SCOPE LEAKAGE
STALE PREMISES
DIRECTION REVERSAL
MEDIATOR OMISSION
SELECTION EFFECT
FEEDBACK
MODEL MISSPECIFICATION
```

---

# 63. Strongest Supported Conclusion

AMOS should choose:

```text
STRONGEST SUPPORTED CAUSAL CLASS
```

not:

```text
STRONGEST IMAGINABLE CAUSAL CLASS
```

Example:

Evidence supports correlation only.

Correct:

```text
X AND Y ARE CORRELATED
```

Incorrect:

```text
X CAUSES Y
```

---

# 64. Causal Promotion

Conceptually:

```text
OBSERVATION
↓ evidence
ASSOCIATION
↓ discriminating evidence
CAUSAL CANDIDATE
↓ mechanism / design / intervention evidence
CAUSAL EFFECT
↓ stronger assumptions + validation
COUNTERFACTUAL EFFECT
```

Promotion is governed by evidence, not prose.

---

# 65. Causal Demotion

New evidence may weaken an existing causal conclusion.

```text
CAUSES
↓
CONDITIONAL
```

or:

```text
CAUSES
↓
COMPETING
```

or:

```text
CAUSES
↓
UNKNOWN/GAP
```

This is a valid epistemic transition.

---

# 66. Causal Invalidation

If a load-bearing causal premise fails:

```text
INVALID(P)
```

invalidate only conclusions dependent on `P`.

```text
P → C1 → C2

P ↛ C3
```

Then:

```text
INVALIDATE C1
INVALIDATE C2
PRESERVE C3
```

---

# 67. Causal Confidence Ceiling

For conclusion `C` with load-bearing premises:

```text
P1 ... Pn
```

conceptually:

```text
CONFIDENCE(C)
<=
MIN(
  confidence(P1),
  ...
  confidence(Pn)
)
```

unless independent evidence revalidates the relevant dependency.

This is a reasoning constraint, not necessarily a literal numerical formula.

---

# 68. Sensitivity

For consequential causal claims identify:

```text
SMALLEST PREMISE
SMALLEST THRESHOLD
SMALLEST ASSUMPTION
SMALLEST OBSERVATION
```

capable of flipping the causal conclusion.

Test that condition first when practical.

---

# 69. Fragile Causation

A causal conclusion should be marked:

```text
CONDITIONAL
```

when plausible perturbation of a load-bearing assumption changes:

```text
DIRECTION
EXISTENCE
MAGNITUDE
SCOPE
REGIME
```

of the claimed causal effect.

---

# 70. Robust Causation

A causal conclusion is comparatively robust when it survives plausible perturbations of noncritical assumptions.

Robustness does not expand its validated scope automatically.

---

# 71. Adversarial Validation

For consequential causal claims:

```text
BUILD STRONGEST SUPPORTED CAUSAL MODEL
↓
CHALLENGE THROUGH DIFFERENT PATH
↓
SEARCH FOR:
  CONFOUNDER
  REVERSE CAUSATION
  SELECTION
  MEDIATION ERROR
  FEEDBACK
  PROVENANCE CORRELATION
  STALE PREMISE
  SCOPE LEAK
  REGIME SHIFT
  STRONGER ALTERNATIVE
```

If the challenge succeeds:

```text
DOWNGRADE
CONDITION
PRESERVE COMPETING
OR
RETURN UNKNOWN/GAP
```

---

# 72. Causal Proof Capsule

Important causal conclusions should conceptually carry:

```yaml
causal_proof_capsule:
  claim:
  claim_class:
  causal_relation_type:

  source:
  target:

  load_bearing_premises: []
  evidence: []
  provenance: []

  mechanism:
  intervention_evidence:
  counterfactual_basis:

  confounders: []
  mediators: []
  competing_explanations: []

  scope:
  regime:
  temporal_validity:

  falsifiers: []
  invalidation_conditions: []

  confidence_ceiling:
```

---

# 73. Causal Hierarchy Invariants

```text
CH-01
OBSERVATION MUST NOT BE PROMOTED DIRECTLY TO CAUSATION

CH-02
ASSOCIATION MUST NOT BE EQUATED WITH CAUSATION

CH-03
CORRELATION MUST NOT BE EQUATED WITH CAUSATION

CH-04
TEMPORAL PRECEDENCE MUST NOT BE EQUATED WITH CAUSATION

CH-05
STRUCTURAL DEPENDENCY MUST NOT BE EQUATED WITH CAUSATION

CH-06
AN ENABLING CONDITION MUST NOT BE EQUATED WITH A SUFFICIENT CONDITION

CH-07
A NECESSARY CONDITION MUST NOT BE EQUATED WITH A SUFFICIENT CONDITION

CH-08
A PLAUSIBLE MECHANISM MUST NOT BE EQUATED WITH A DEMONSTRATED EFFECT

CH-09
MEDIATION MUST NOT BE INFERRED FROM ASSOCIATION ALONE

CH-10
MATERIAL CONFOUNDING ALTERNATIVES MUST REMAIN VISIBLE

CH-11
ABSENCE OF KNOWN CONFOUNDERS MUST NOT BE TREATED AS PROOF OF NO CONFOUNDING

CH-12
OBSERVATIONAL CONDITIONING MUST ACCOUNT FOR COLLIDER / SELECTION RISK WHEN MATERIAL

CH-13
FEEDBACK MUST NOT BE REDUCED TO SIMPLE CORRELATION

CH-14
P(Y|X) MUST NOT BE SILENTLY TREATED AS P(Y|do(X))

CH-15
COUNTERFACTUAL OUTCOMES MUST NOT BE CLAIMED AS DIRECT OBSERVATIONS

CH-16
CAUSAL DIRECTION MUST NOT BE INFERRED FROM ASSOCIATION ALONE

CH-17
CAUSAL CLAIMS MUST INHERIT SCOPE

CH-18
CAUSAL CLAIMS MUST INHERIT REGIME WHEN MATERIAL

CH-19
CROSS-DOMAIN ANALOGY MUST REMAIN MODEL UNTIL VALIDATED

CH-20
CROSS-SCALE ANALOGY MUST REMAIN MODEL UNTIL VALIDATED

CH-21
PROVENANCE CORRELATION MUST NOT BE COUNTED AS INDEPENDENT CONFIRMATION

CH-22
THE CAUSAL CONCLUSION MUST NOT EXCEED ITS LOAD-BEARING EVIDENCE

CH-23
COMPETING CAUSAL HYPOTHESES MUST NOT BE FORCED TO CONVERGE

CH-24
INVALIDATION MUST FOLLOW CAUSAL DEPENDENCY

CH-25
UNKNOWN/GAP MUST NOT BECOME PASS
```

---

# 74. Failure Modes

```text
CORRELATION_AS_CAUSATION
SEQUENCE_AS_CAUSATION
DEPENDENCY_AS_CAUSATION
ANALOGY_AS_CAUSATION
MECHANISM_AS_PROOF
REVERSE_CAUSATION_IGNORED
CONFOUNDER_OMISSION
HIDDEN_CONFOUNDER_OVERCONFIDENCE
MEDIATOR_CONFUSION
COLLIDER_BIAS
SELECTION_BIAS
FEEDBACK_COLLAPSE
NECESSITY_SUFFICIENCY_CONFUSION
SCOPE_LEAKAGE
REGIME_LEAKAGE
CROSS_SCALE_OVERREACH
CROSS_DOMAIN_OVERREACH
PROVENANCE_SYBIL
FALSE_INDEPENDENCE
OBSERVATIONAL_INTERVENTIONAL_COLLAPSE
COUNTERFACTUAL_OVERREACH
CAUSAL_DIRECTION_OVERCLAIM
FALSE_CONVERGENCE
GLOBAL_INVALIDATION
UNKNOWN_AS_PASS
```

---

# 75. Conceptual Classification Algorithm

```python
def classify_causal_claim(claim, evidence):
    if evidence is None:
        return "UNKNOWN/GAP"

    if supports_observation_only(evidence):
        return "OBSERVATION"

    if supports_association(evidence):
        level = "ASSOCIATION"

    if supports_correlation(evidence):
        level = "CORRELATION"

    if supports_temporal_or_structural_dependency(evidence):
        level = "DEPENDENCY"

    if supports_causal_candidate(evidence):
        level = "CAUSAL_CANDIDATE"

    if supports_mechanism(evidence):
        level = "MECHANISM_SUPPORTED"

    if supports_interventional_effect(evidence):
        level = "INTERVENTIONAL_CAUSAL_EFFECT"

    if supports_counterfactual_effect(evidence):
        level = "COUNTERFACTUAL_CAUSAL_EFFECT"

    return level
```

This is architectural pseudocode, not a claim of deployed implementation.

---

# 76. Conceptual Causal Challenge

```python
def challenge_causal_claim(claim):
    alternatives = [
        reverse_causation(claim),
        common_cause(claim),
        selection_effect(claim),
        mediation_error(claim),
        feedback(claim),
        provenance_correlation(claim),
        scope_failure(claim),
        regime_failure(claim),
        stale_premise(claim),
    ]

    for alternative in alternatives:
        if materially_supported(alternative):
            preserve_competing(claim, alternative)

    return strongest_supported_class(claim)
```

---

# 77. Relationship to Law Hierarchy

`K_LAW_HIERARCHY` governs precedence among applicable AMOS laws.

`K_CAUSAL_HIERARCHY` governs precedence among causal interpretations.

Therefore:

```text
LAW HIERARCHY
!=
CAUSAL HIERARCHY
```

They solve different ordering problems.

---

# 78. Relationship to K_CORE19_LOGIC

Core logical consistency is prerequisite to causal reasoning.

A causal model that violates applicable logical invariants cannot be promoted merely because empirical observations appear compatible.

Conceptually:

```text
LOGICAL VALIDITY
↓
CAUSAL CLASSIFICATION
↓
CAUSAL VALIDATION
```

---

# 79. Relationship to K_META_LOGIC

`K_META_LOGIC` governs reasoning about reasoning structures.

It may determine whether the causal inference procedure itself is valid under the current epistemic regime.

`K_CAUSAL_HIERARCHY` remains responsible for causal claim typing.

---

# 80. Relationship to Provenance

Causal evidence cannot be interpreted independently of provenance when source ancestry affects independence or reliability.

Therefore:

```text
CAUSAL EVIDENCE
+
PROVENANCE TOPOLOGY
```

must be jointly evaluated when material.

---

# 81. Relationship to Authority

Causal validity does not grant action authority.

```text
VERIFIED CAUSAL CLAIM
!=
PERMISSION TO ACT
```

Authority remains a control-plane concern.

---

# 82. Relationship to Models

A model may encode:

```text
X → Y
```

This means:

```text
MODEL ASSERTS X → Y
```

unless independent evidence establishes a stronger conclusion class.

Therefore:

```text
MODEL EDGE
!=
VERIFIED CAUSAL EDGE
```

---

# 83. Relationship to Agents

Agents may:

```text
PROPOSE CAUSAL HYPOTHESES
SEARCH FOR EVIDENCE
RUN TESTS
CHALLENGE CLAIMS
```

but agent capability does not create causal authority.

```text
AGENT OUTPUT
!=
CANONICAL CAUSAL TRUTH
```

---

# 84. Relationship to Research

External papers, experiments, datasets, benchmarks, and reports may supply causal evidence.

They remain subject to:

```text
SOURCE PROVENANCE
DESIGN QUALITY
SCOPE
REGIME
FRESHNESS
REPLICATION / INDEPENDENCE
ASSUMPTIONS
```

before AMOS promotes causal conclusions.

---

# 85. Required Tests

Future implementation verification should include:

```text
OBSERVATION-CAUSATION FIREWALL TEST
CORRELATION-CAUSATION FIREWALL TEST
TEMPORAL-CAUSATION FIREWALL TEST
DEPENDENCY-CAUSATION FIREWALL TEST
MECHANISM-PROOF FIREWALL TEST
NECESSITY-SUFFICIENCY TEST
CONFOUNDER TEST
REVERSE-CAUSATION TEST
MEDIATION TEST
COLLIDER TEST
SELECTION-BIAS TEST
FEEDBACK TEST
INTERVENTION TEST
COUNTERFACTUAL TEST
CAUSAL-DIRECTION TEST
PROVENANCE-INDEPENDENCE TEST
SCOPE-TRANSFER TEST
REGIME-SHIFT TEST
CROSS-SCALE TEST
CROSS-DOMAIN TEST
COMPETING-HYPOTHESIS TEST
SELECTIVE-INVALIDATION TEST
UNKNOWN-PRESERVATION TEST
```

---

# 86. Negative Tests

```text
X BEFORE Y
→
X CAUSES Y
MUST FAIL

X CORRELATED WITH Y
→
X CAUSES Y
MUST FAIL

A DEPENDS ON B
→
B EMPIRICALLY CAUSES A
MUST FAIL

PLAUSIBLE MECHANISM
→
VERIFIED EFFECT
MUST FAIL

NO KNOWN CONFOUNDER
→
NO CONFOUNDER EXISTS
MUST FAIL

X ASSOCIATED WITH M
AND
M ASSOCIATED WITH Y
→
X → M → Y
MUST FAIL

P(Y|X)
→
P(Y|do(X))
MUST FAIL

MODEL SAYS X → Y
→
VERIFIED X → Y
MUST FAIL

THREE REPORTS FROM ONE SOURCE
→
THREE INDEPENDENT CAUSAL CONFIRMATIONS
MUST FAIL

CAUSAL EFFECT IN DOMAIN A
→
SAME EFFECT IN DOMAIN B
MUST FAIL

CAUSAL EFFECT AT MICRO SCALE
→
SAME EFFECT AT MACRO SCALE
MUST FAIL

VERIFIED CAUSAL CLAIM
→
AUTHORITY TO ACT
MUST FAIL

UNKNOWN/GAP
→
PASS
MUST FAIL
```

---

# 87. Lifecycle

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

These states are distinct.

```text
MODEL
!=
IMPLEMENTATION

IMPLEMENTATION
!=
VALIDATION

VALIDATION
!=
AUTHORITY
```

---

# 88. Promotion Gate

Before promotion beyond `AMOS_MODEL`:

```text
[ ] causal relation vocabulary bound to canon
[ ] hierarchy levels canonically reviewed
[ ] causal firewall rules validated
[ ] causal closure integration confirmed
[ ] causal epoch integration confirmed
[ ] counterfactual integration confirmed
[ ] multi-hypothesis integration confirmed
[ ] provenance topology integration confirmed
[ ] scope firewall tested
[ ] regime firewall tested
[ ] confounding behavior tested
[ ] mediation behavior tested
[ ] collider / selection behavior tested
[ ] feedback semantics tested
[ ] intervention semantics tested
[ ] counterfactual semantics tested
[ ] cross-domain transfer rules tested
[ ] cross-scale transfer rules tested
[ ] selective invalidation tested
[ ] negative tests implemented
[ ] unresolved conflicts registered
```

Until evidenced:

```text
IMPLEMENTATION_STATUS = UNKNOWN/GAP
EMPIRICAL_VALIDATION = UNKNOWN/GAP
FORMAL_VERIFICATION = UNKNOWN/GAP
```

---

# 89. Integrity Note

This artifact replaces the repository placeholder with an AMOS v4.4-aligned causal hierarchy model.

It formalizes reasoning constraints around:

```text
ASSOCIATION
CORRELATION
CAUSAL DIRECTION
MECHANISM
ENABLING CONDITIONS
NECESSITY
SUFFICIENCY
MEDIATION
CONFOUNDING
SELECTION
FEEDBACK
INTERVENTION
COUNTERFACTUALS
CAUSAL CLOSURE
CAUSAL EPOCHS
PROVENANCE
SCOPE
REGIME
```

It does **not** assert that a corresponding causal inference engine is implemented, deployed, empirically validated, or formally verified.

Therefore:

```text
DOCUMENT_CLASS = AMOS_MODEL
IMPLEMENTATION = UNKNOWN/GAP
EMPIRICAL_VALIDATION = UNKNOWN/GAP
FORMAL_VERIFICATION = UNKNOWN/GAP
RUNTIME_AUTHORITY = NONE
```

---

# 90. RSCF Node

```RSCF-NODE
node_id: AMOS-OS-K-CAUSAL-HIERARCHY
node_type: kernel_causal_hierarchy_contract
domain: AMOS_OS_KERNEL
functional_type: CausalHierarchyKernel
lifecycle_stage: Architecture
claim_class: AMOS_MODEL

RSCF-RELATIONS:
  - ROOTED_IN: README
  - DEPENDENCY_BOUND_TO: DEPENDENCY_MAP
  - STATE_BOUND_TO: AUTHORITATIVE_STATE

  - GOVERNED_BY: AMOS_CORE_LAWS
  - CONSTRAINED_BY: INVARIANT_REGISTRY
  - PRECEDENCE_GOVERNED_BY: LAW_HIERARCHY
  - AUTHORITY_GOVERNED_BY: AUTHORITY_CANON

  - PROVENANCE_GOVERNED_BY: CANON_PROVENANCE
  - LINEAGE_TRACKED_BY: SOURCE_LINEAGE
  - CONFLICTS_TRACKED_BY: CONFLICT_REGISTRY

  - INDEXED_BY: KERNEL_MAP

  - LOGIC_DEPENDS_ON: K_CORE19_LOGIC
  - META_LOGIC_DEPENDS_ON: K_META_LOGIC
  - STRUCTURE_DEPENDS_ON: K_STRUCTURAL_REASONING

  - CAUSAL_CLOSURE_INTERACTS_WITH: K_CAUSAL_CLOSURE
  - CAUSAL_EPOCH_INTERACTS_WITH: K_CAUSAL_EPOCH
  - COUNTERFACTUAL_INTERACTS_WITH: K_COUNTERFACTUAL
  - METACOGNITION_INTERACTS_WITH: K_METACOGNITION
  - HYPOTHESIS_INTERACTS_WITH: K_MULTI_HYPOTHESIS

  - PROVENANCE_DEPENDS_ON: README
  - CAUSAL_DEPENDS_ON: README
  - DEPENDENCY_DEPENDS_ON: README
  - VALIDATED_BY: README

  - AUTHORIZED_THROUGH: CONTROL_PLANE_MAP
  - EXECUTED_THROUGH: RUNTIME_MAP

  - EVIDENCE_BOUND_TO: 11_KNOWLEDGE/00_AMOS_Full_Brain_OS_Architecture
  - STATE_RECORDED_IN: AUTHORITATIVE_STATE
  - OBSERVED_BY: README
  - VERIFIED_BY: README
```

---

# 91. Canonical Summary

```text
OBSERVE
↓
TYPE EVIDENCE
↓
IDENTIFY ASSOCIATION
↓
GENERATE CAUSAL HYPOTHESES
↓
PRESERVE COMPETING DIRECTIONS
↓
CHECK PROVENANCE
↓
CHECK CONFOUNDERS
↓
CHECK SELECTION / COLLIDERS
↓
CHECK MEDIATION
↓
CHECK FEEDBACK
↓
CHECK MECHANISM
↓
CHECK INTERVENTIONAL EVIDENCE
↓
CHECK COUNTERFACTUAL BASIS
↓
BIND SCOPE
↓
BIND REGIME
↓
BIND CAUSAL EPOCH
↓
ASSIGN WEAKEST ACCURATE
CAUSAL CONCLUSION CLASS
```

Core laws:

```text
ASSOCIATION != CAUSATION

CORRELATION != CAUSATION

TEMPORAL ORDER != CAUSATION

DEPENDENCY != CAUSATION

MECHANISM != DEMONSTRATED EFFECT

ENABLING != SUFFICIENT

NECESSARY != SUFFICIENT

OBSERVATION != INTERVENTION

P(Y|X) != P(Y|do(X))

COUNTERFACTUAL != OBSERVATION

STRUCTURAL SIMILARITY != CAUSAL TRANSFER

MODEL EDGE != VERIFIED CAUSAL EDGE

REPETITION != INDEPENDENT CONFIRMATION

CAUSAL VALIDITY != AUTHORITY

UNKNOWN/GAP != PASS
```

The decisive invariant is:

```text
AMOS MUST NEVER
PROMOTE A RELATION

TO A STRONGER
CAUSAL CLASS

THAN ITS
LOAD-BEARING EVIDENCE,
PROVENANCE,
SCOPE,
REGIME,
AND EPOCH

CAN SUPPORT.

WHEN MULTIPLE
CAUSAL EXPLANATIONS
REMAIN VIABLE,

PRESERVE COMPETING.

WHEN CAUSAL SUPPORT
IS MISSING,

RETURN UNKNOWN/GAP

RATHER THAN
BRIDGING THE GAP
WITH FLUENT EXPLANATION.
```

## Related

[[README]] ·
00_ROOT_MOC|AMOS MOC ·
[[ARCHITECTURE]] ·
[[DEPENDENCY_MAP]] ·
[[AUTHORITATIVE_STATE]] ·
[[CANON_MAP]] ·
[[AMOS_CORE_LAWS]] ·
[[INVARIANT_REGISTRY]] ·
[[LAW_HIERARCHY]] ·
[[AUTHORITY_CANON]] ·
[[CANON_PROVENANCE]] ·
[[SOURCE_LINEAGE]] ·
[[CONFLICT_REGISTRY]] ·
[[KERNEL_MAP]] ·
[[K_CORE19_LOGIC]] ·
[[K_META_LOGIC]] ·
[[K_STRUCTURAL_REASONING]] ·
[[K_CAUSAL_CLOSURE]] ·
[[K_CAUSAL_EPOCH]] ·
[[K_COUNTERFACTUAL]] ·
[[K_METACOGNITION]] ·
[[K_MULTI_HYPOTHESIS]] ·
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
**MOC:** [[03_CAUSAL_MOC]]
