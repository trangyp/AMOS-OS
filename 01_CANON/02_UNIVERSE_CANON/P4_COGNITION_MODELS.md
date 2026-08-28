---
title: P4 Cognition & Models
type: model
source: 01_CANON/02_UNIVERSE_CANON
artifact: P4_COGNITION_MODELS.md
artifact_id: amos_01_canon_02_universe_canon_p4_cognition_models
origin_architect: Trang Phan
steward: Trang Phan
system: AMOS OS
plane: 01_CANON
segment: 01_CANON/02_UNIVERSE_CANON
artifact_kind: UNIVERSE_PLANE
path: 01_CANON/02_UNIVERSE_CANON/P4_COGNITION_MODELS.md
tags:
  - amos_os
  - canon
  - universe_canon
  - cognition
  - models
  - inference
  - prediction
  - hypothesis
  - competing
  - derivation
  - speculation
  - epistemic_discipline
  - provenance
  - falsification
  - uncertainty
  - rscf
  - p4_plane
  - canon/universe
version: 0.2.0
updated: '2026-08-26'
status: PROPOSED_SPECIFICATION
epistemic_class: AMOS_MODEL
canonical_status: CONDITIONAL
implementation_status: NOT_ESTABLISHED
validation_status: NOT_ESTABLISHED
executable_binding: NOT_ESTABLISHED
ingestion_action: NATIVE_CANON_NORMALIZATION
raw_source_policy: DO_NOT_LOAD_UNLESS_REQUIRED
rscf:
  state: SOURCE_GROUNDED
  claim_class: AMOS_MODEL
  provenance:
    - AMOS_corpus
    - 01_CANON/02_UNIVERSE_CANON/AMOS_7_PART_UNIVERSE_CANON
    - 01_CANON/02_UNIVERSE_CANON/HML_CANON
    - 01_CANON/02_UNIVERSE_CANON/P3_KNOWLEDGE_MEMORY
    - TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS
  scope:
    - UNIVERSE_CANON
    - P4_COGNITION_MODELS
---

# P4 — Cognition & Models Plane

## 0. Status

`P4_COGNITION_MODELS.md` defines the proposed **P4 Cognition & Models Plane** of the AMOS Universe Canon.

P4 governs the structural machinery for:

- inference;
- prediction;
- model construction;
- hypothesis generation;
- hypothesis comparison;
- competing-model preservation;
- derivation;
- bounded speculation;
- epistemic classification.

Its central firewall is:

```text
REASONING != EVIDENCE

Current classification:

```text
SPECIFICATION
=
PROPOSED

EPISTEMIC CLASS
=
AMOS_MODEL

CANONICAL STATUS
=
CONDITIONAL

IMPLEMENTATION
=
NOT ESTABLISHED

RUNTIME VALIDATION
=
NOT ESTABLISHED
```

**Origin architect / steward:** **Trang Phan**

---

# 1. Purpose

P4 transforms admitted and retained information into structured candidate understanding.

Conceptually:

$$
Evidence + Knowledge
\rightarrow
Models
\rightarrow
Inference
\rightarrow
Predictions
\rightarrow
Hypotheses
$$

But no transformation inside P4 automatically upgrades a model-generated result into observation.

Therefore:

$$
Reasoning(E)
\not\Rightarrow
NewEvidence
$$

unless new external evidence is actually acquired and admitted through the appropriate evidence path.

---

# 2. Scope

P4 governs:

* reasoning machinery;
* inference;
* prediction;
* abstraction;
* model construction;
* model comparison;
* hypothesis management;
* competing explanations;
* derivation;
* uncertainty;
* bounded speculation;
* frontier reasoning;
* falsifier generation;
* sensitivity analysis;
* epistemic classification;
* contradiction-aware reasoning.

P4 does **not** establish neuroscience claims about biological cognition.

---

# 3. Position in the Universe Canon

P4 follows P3.

```text
P1 — REALITY / ENVIRONMENT
        ↓
P2 — SENSE / EVIDENCE
        ↓
P3 — KNOWLEDGE / MEMORY
        ↓
P4 — COGNITION / MODELS
```

P3 answers:

```text
WHAT KNOWLEDGE IS AVAILABLE?
```

P4 answers:

```text
WHAT MODELS, INFERENCES,
PREDICTIONS, OR HYPOTHESES
CAN BE CONSTRUCTED FROM IT?
```

Thus, at the architectural-model level:

$$
P4
=
Cognition(P2Evidence,P3Knowledge)
$$

subject to inherited provenance, scope, freshness, and confidence ceilings.

---

# 4. Canonical Questions

## P4-Q1 — Competing Models

> How are competing models maintained rather than collapsed prematurely?

P4 must preserve genuinely viable incompatible hypotheses until discriminating evidence supports resolution.

---

## P4-Q2 — Derivation vs Speculation

> What separates derivation from speculation?

The distinction depends on whether the conclusion follows from admitted premises under declared transformations, versus requiring unsupported assumptions, extrapolation, analogy, or frontier modeling.

---

# 5. P4-1 — Competing Preservation

## Law

```text
P4-1 COMPETING PRESERVATION

Incompatible viable hypotheses
stay COMPETING.
```

The supplied source associates this law with:

```text
U-3
```

The exact definition of `U-3` is not supplied here and must therefore remain an explicit dependency rather than being reconstructed.

Formally:

$$
Viable(H_1)
\land
Viable(H_2)
\land
Incompatible(H_1,H_2)
\land
\neg Discriminator
$$

implies:

$$
State(H_1,H_2)=COMPETING
$$

---

# 6. Competing Is a Valid Terminal State

P4 does not require every reasoning process to converge to one answer.

Valid outcomes include:

```text
VERIFIED

DERIVED

MODEL

CONDITIONAL

COMPETING

UNKNOWN/GAP
```

Therefore:

```text
NO WINNER
!=
REASONING FAILURE
```

When available evidence cannot discriminate between viable alternatives, `COMPETING` is the integrity-preserving result.

---

# 7. Hypothesis Contract

```yaml
P4_HYPOTHESIS:

  hypothesis_id:

  proposition:

  claim_class:

  premises: []

  evidence_refs: []

  provenance: []

  assumptions: []

  dependencies: []

  scope:

  regime:

  temporal_validity:

  predicted_observations: []

  competing_hypotheses: []

  falsifiers: []

  confidence_ceiling:

  status:
```

This is a conceptual normalization contract until executable binding is established.

---

# 8. Competing Set

```yaml
P4_COMPETING_SET:

  subject:

  hypotheses:

    - hypothesis_id:
      claim:
      support: []
      provenance: []
      assumptions: []
      confidence_ceiling:

    - hypothesis_id:
      claim:
      support: []
      provenance: []
      assumptions: []
      confidence_ceiling:

  shared_dependencies: []

  independent_dependencies: []

  discriminating_tests: []

  status:
    COMPETING
```

---

# 9. Preservation Rule

P4 must not collapse alternatives merely because one is:

* more fluent;
* simpler to describe;
* more familiar;
* more popular;
* repeated more often;
* produced first;
* aligned with prior expectation.

These properties may sometimes inform model selection under explicit criteria, but they do not themselves establish truth.

---

# 10. Evidence Topology in Competition

Suppose:

$$
H_1 \leftarrow E_1,E_2
$$

and:

$$
H_2 \leftarrow E_3,E_4
$$

Raw source count alone is insufficient.

P4 must ask whether:

$$
E_1,E_2,E_3,E_4
$$

are genuinely independent or share ancestry.

Example:

```text
SOURCE A
  ├── E1
  ├── E2
  └── E3
```

Three descendants do not constitute three independent origins.

Therefore:

```text
REPETITION
!=
INDEPENDENT CONFIRMATION
```

---

# 11. Cheapest Discriminating Test

When hypotheses remain competing, P4 should prefer the cheapest high-information test capable of changing the outcome.

```text
H1 ─┐
    ├── COMPETING
H2 ─┘
     ↓
IDENTIFY DIFFERENT PREDICTIONS
     ↓
FIND CHEAPEST VALID TEST
     ↓
OBSERVE
     ↓
RECLASSIFY
```

The objective is not maximal evidence accumulation.

The objective is decision-relevant discrimination.

---

# 12. P4-2 — Class Discipline

## Law

```text
P4-2 CLASS DISCIPLINE

SOURCE / DERIVED / MODEL / UNKNOWN
demarcation is enforced on every output.
```

The source explicitly associates this discipline with RSCF.

A normalized AMOS classification vocabulary may preserve the more granular classes:

```text
SOURCE_CLAIM

OBSERVATION

DERIVED

MODEL

DECISION

CONDITIONAL

COMPETING

UNKNOWN/GAP
```

without erasing the supplied P4 distinction.

---

# 13. SOURCE_CLAIM

A `SOURCE_CLAIM` records what a source states.

```text
SOURCE S STATES X
```

does not imply:

```text
X IS VERIFIED
```

Therefore:

$$
SourceClaims(X)
\not\Rightarrow
Verified(X)
$$

---

# 14. OBSERVATION

An `OBSERVATION` records admitted measurement or directly captured evidence.

It remains bounded by:

* measurement method;
* instrument;
* observer;
* sampling;
* environment;
* timestamp;
* uncertainty.

Thus:

```text
OBSERVED
!=
UNIVERSALLY TRUE
```

---

# 15. DERIVED

A `DERIVED` claim follows from explicit premises through an admissible transformation.

Conceptually:

$$
P_1,P_2,\ldots,P_n
\vdash
C
$$

But the confidence ceiling of \(C\) cannot silently exceed its load-bearing premises.

Therefore:

$$
Conf(C)
\le
Conf(P_{weakest})
$$

unless \(C\) receives independent revalidation.

---

# 16. MODEL

A `MODEL` is an explanatory, predictive, representational, or structural construct.

A model may be:

* useful;
* coherent;
* predictive;
* computationally effective;

without becoming observation.

Therefore:

```text
MODEL SUCCESS
!=
MODEL ONTOLOGICAL TRUTH
```

---

# 17. UNKNOWN/GAP

`UNKNOWN/GAP` is required when a load-bearing premise cannot be established.

```text
MISSING CRITICAL PREMISE
        ↓
UNKNOWN/GAP
```

P4 must not fill the missing edge with fluent prose.

---

# 18. Class Transition Discipline

A claim may move between epistemic states only through an explicit justification.

Example:

```text
SOURCE_CLAIM
     ↓
VALIDATION
     ↓
SUPPORTED MODEL
```

or:

```text
MODEL PREDICTION
     ↓
EXTERNAL TEST
     ↓
OBSERVATION
```

The prediction itself does not become the observation.

---

# 19. No Epistemic Laundering

Forbidden transformation:

```text
MODEL
  ↓
REPEATED
  ↓
SUMMARIZED
  ↓
STORED
  ↓
"FACT"
```

Neither repetition, storage, nor summarization changes epistemic class by itself.

Thus:

$$
Persistence(Model)
\not\Rightarrow
Observation
$$

---

# 20. Derivation Contract

```yaml
P4_DERIVATION:

  derivation_id:

  conclusion:

  conclusion_class:
    DERIVED

  premises: []

  premise_classes: []

  transformations: []

  assumptions: []

  provenance: []

  scope:

  regime:

  dependencies: []

  falsifiers: []

  confidence_ceiling:

  validation_state:
```

---

# 21. Derivation Validity

A derivation is only as valid as:

1. its premises;
2. the applicability of its transformation rules;
3. its scope;
4. its regime;
5. its dependency coherence.

Therefore:

$$
ValidDerivation
=
ValidPremises
\land
ValidTransformation
\land
CompatibleScope
\land
CompatibleRegime
$$

conceptually.

---

# 22. Hidden-Premise Firewall

P4 should expose material assumptions rather than bury them.

Forbidden pattern:

```text
P1
  ↓
[UNSTATED ASSUMPTION]
  ↓
C
```

Preferred:

```text
P1
 +
A1 [ASSUMPTION]
  ↓
C [CONDITIONAL]
```

If \(A_1\) can flip the result, the conclusion is fragile and should remain conditional.

---

# 23. P4-3 — Bounded Speculation

## Law

```text
P4-3 BOUNDED SPECULATION

Frontier reasoning is tagged and isolated,
never blended into established results.
```

Speculation is permitted.

Epistemic blending is not.

---

# 24. Frontier Reasoning

Frontier reasoning may include:

* exploratory hypotheses;
* analogy;
* extrapolation;
* speculative mechanisms;
* cross-domain mappings;
* unvalidated structural correspondences.

These may be useful for generating tests or models.

They remain:

```text
MODEL
```

or:

```text
CONDITIONAL
```

until independently validated.

---

# 25. Speculation Boundary

```text
ESTABLISHED RESULT
────────────────────
SPECULATIVE FRONTIER
```

The boundary must remain visible.

A speculative branch must not silently contaminate an established proof capsule.

---

# 26. Speculation Contract

```yaml
P4_SPECULATION:

  speculation_id:

  proposition:

  class:
    MODEL

  speculative: true

  grounding_refs: []

  extrapolations: []

  assumptions: []

  analogies: []

  unsupported_edges: []

  scope:

  falsifiers: []

  discriminating_tests: []

  confidence_ceiling:
```

---

# 27. Isolation Rule

If:

$$
C_1
$$

is derived from established premises and:

$$
C_2
$$

requires speculative premise \(A_s\),

then P4 should preserve:

```text
C1 = DERIVED

C2 = MODEL / CONDITIONAL
```

rather than assigning both the stronger class.

---

# 28. Speculation Cannot Back-Propagate Confidence

Suppose:

$$
E \rightarrow D \rightarrow M_s
$$

where:

* \(E\) = evidence;
* \(D\) = derivation;
* \(M_s\) = speculative model.

The existence of \(M_s\) cannot increase confidence in \(E\) or \(D\).

Likewise, elegance of \(M_s\) does not independently validate the chain.

---

# 29. Prediction

A model may generate prediction:

$$
M
\rightarrow
\hat{O}
$$

where \(\hat{O}\) is a predicted observation.

But:

$$
\hat{O}
\neq
O
$$

until observation occurs.

Therefore:

```text
PREDICTED
!=
OBSERVED
```

---

# 30. Prediction Contract

```yaml
P4_PREDICTION:

  prediction_id:

  originating_model:

  prediction:

  expected_scope:

  expected_regime:

  expected_time:

  measurement_method:

  falsification_condition:

  observation_ref:

  validation_state:
```

---

# 31. Prediction Validation

Possible states:

```text
UNTESTED

SUPPORTED

CONTRADICTED

INCONCLUSIVE

OUT_OF_SCOPE

REGIME_SHIFTED
```

A successful prediction may increase support for a model.

It does not automatically establish uniqueness of mechanism.

Multiple models may predict the same observation.

---

# 32. Underdetermination

If:

$$
M_1\rightarrow O
$$

and:

$$
M_2\rightarrow O
$$

then observing \(O\) does not necessarily discriminate between \(M_1\) and \(M_2\).

Thus:

```text
PREDICTION CONFIRMED
!=
MODEL UNIQUELY PROVEN
```

Competing preservation remains active.

---

# 33. Causal Firewall

P4 must distinguish:

```text
ASSOCIATION

CORRELATION

MECHANISM

ENABLING CONDITION

NECESSARY CONDITION

SUFFICIENT CONDITION

MEDIATION

CONFOUNDING

FEEDBACK

CAUSAL EFFECT
```

Structural similarity or temporal sequence alone does not license causal inference.

---

# 34. Causal Claim Contract

```yaml
P4_CAUSAL_CLAIM:

  claim:

  causal_type:

  evidence_refs: []

  mechanism:

  confounders: []

  mediators: []

  alternative_explanations: []

  scope:

  regime:

  falsifiers: []

  confidence_ceiling:
```

---

# 35. Structural Similarity Firewall

Given:

$$
Structure(A)\approx Structure(B)
$$

P4 may generate:

```text
POSSIBLE ANALOGY
```

or:

```text
MODEL
```

but not:

```text
A CAUSES B
```

or:

```text
A AND B SHARE THE SAME MECHANISM
```

without appropriate evidence.

---

# 36. Cross-Domain Mapping

Cross-domain mappings remain model-level unless independently validated.

```text
DOMAIN A
   ⇄
STRUCTURAL MAPPING
   ⇄
DOMAIN B
```

Classification:

```text
MODEL
```

not automatically:

```text
VERIFIED CAUSAL LAW
```

---

# 37. Scope Firewall

Every consequential model should carry an applicability envelope.

```yaml
P4_SCOPE:

  system_or_population:

  environment:

  scale:

  time:

  regime:

  measurement_method:

  assumptions:
```

A result derived within scope \(S_1\) cannot silently generalize to \(S_2\).

---

# 38. Regime Firewall

A model may perform well under regime:

$$
R_1
$$

and fail under:

$$
R_2
$$

Therefore:

```text
VALID IN R1
!=
VALID IN ALL REGIMES
```

Regime shifts can invalidate prior model reuse.

---

# 39. Sensitivity

For consequential conclusions, P4 should identify the smallest premise, threshold, or assumption capable of changing the result.

Suppose:

$$
C=f(P_1,P_2,\theta)
$$

and small variation in \(\theta\) flips \(C\).

Then:

```text
C = CONDITIONAL / FRAGILE
```

rather than robust.

---

# 40. Sensitivity Contract

```yaml
P4_SENSITIVITY:

  conclusion:

  load_bearing_inputs: []

  flip_variables: []

  thresholds: []

  plausible_perturbations: []

  result_stability:

  classification:
    ROBUST | FRAGILE | UNKNOWN
```

---

# 41. Robustness

A conclusion is structurally stronger when it survives plausible perturbations of noncritical assumptions.

Conceptually:

$$
Robust(C)
\iff
C
\text{ survives relevant perturbations}
$$

This is a reasoning criterion, not a universal empirical equation.

---

# 42. Adversarial Validation

For consequential conclusions P4 should attempt a genuinely different challenge path.

Primary path:

```text
EVIDENCE
   ↓
MODEL
   ↓
CONCLUSION
```

Challenge path:

```text
CONCLUSION
   ↓
SEARCH FOR:
- contradiction
- correlated provenance
- stale premise
- scope leakage
- hidden dependency
- causal overreach
- stronger alternative
```

---

# 43. Challenge Outcomes

```text
CHALLENGE FAILS
→ retain current class

CHALLENGE SUCCEEDS
→ downgrade

DEPENDENCY UNCERTAIN
→ CONDITIONAL

ALTERNATIVE SURVIVES
→ COMPETING

CRITICAL PREMISE MISSING
→ UNKNOWN/GAP
```

Adversarial validation must not manufacture objections unsupported by evidence.

---

# 44. Proof Capsule

Important P4 conclusions should conceptually carry:

```yaml
P4_[[L19_PROOF_CAPSULE]]:

  claim:

  conclusion_class:

  premises: []

  evidence_refs: []

  provenance: []

  assumptions: []

  scope:

  regime:

  temporal_validity:

  dependencies: []

  competing_explanations: []

  falsifiers: []

  sensitivity:

  confidence_ceiling:

  revalidation_conditions:
```

---

# 45. Proof Capsule Reuse

A prior result may be reused only if its dependency closure remains valid.

Conceptually:

$$
Reuse(C)
\iff
DependenciesValid
\land
ScopeCompatible
\land
RegimeCompatible
\land
Fresh
\land
NonConflicting
$$

Otherwise the affected proof branch must be reopened.

---

# 46. Weakest Load-Bearing Premise

Suppose:

$$
P_1,P_2,P_3 \rightarrow C
$$

with confidence ceilings:

$$
0.95,\ 0.91,\ 0.60
$$

Without independent revalidation of \(C\):

$$
Conf(C)\le0.60
$$

Conceptually:

```text
DERIVED CONFIDENCE
CANNOT SILENTLY EXCEED
THE WEAKEST LOAD-BEARING PREMISE
```

---

# 47. Provenance-Aware Inference

P4 must distinguish:

```text
THREE INDEPENDENT PREMISES
```

from:

```text
THREE REPRESENTATIONS
OF ONE PREMISE
```

If:

```text
SOURCE A
 ├── P1
 ├── P2
 └── P3
```

the support topology remains correlated.

---

# 48. Provenance Topology

```yaml
P4_PROVENANCE_TOPOLOGY:

  claims: []

  sources: []

  ancestry_edges: []

  derivation_edges: []

  shared_origins: []

  correlation_risk:

  independence_state:
```

Independence must be demonstrated where it materially affects confidence.

---

# 49. Sybil / Duplication Hardening

P4 should resist apparent support inflation caused by:

* mirrors;
* reposts;
* summaries;
* syndicated copies;
* generated restatements;
* duplicated datasets;
* descendant reports.

Thus:

```text
MANY NODES
!=
MANY INDEPENDENT SOURCES
```

---

# 50. Inference Graph

```text
EVIDENCE
   ↓
PREMISES
   ↓
DERIVATIONS
   ↓
MODELS
   ↓
PREDICTIONS
   ↓
TESTS
   ↓
MODEL UPDATE
```

Each edge should remain epistemically typed.

---

# 51. Atomic Multi-Premise Reasoning

Some conclusions require multiple premises simultaneously:

$$
C=f(P_1,P_2,P_3)
$$

P4 must establish joint compatibility where necessary.

Individually valid premises from incompatible epochs or regimes may not form a valid joint inference.

---

# 52. Coherence Contract

```yaml
P4_JOINT_COHERENCE:

  premise_refs: []

  epochs: []

  regimes: []

  scopes: []

  dependency_compatibility:

  provenance_independence:

  contradiction_state:

  jointly_usable:
```

---

# 53. Smallest Sufficient Proof Scope

P4 should reason over the smallest dependency closure capable of changing the conclusion.

```text
QUESTION
   ↓
LOAD-BEARING PREMISES
   ↓
DEPENDENCIES
   ↓
MINIMUM REQUIRED EVIDENCE
```

Not:

```text
QUESTION
   ↓
LOAD EVERYTHING
```

This reduces irrelevant context and correlated evidence inflation.

---

# 54. Escalation Conditions

Local reasoning should escalate when:

```text
PROVENANCE SHARED

EVIDENCE CONFLICTS

PREMISES STALE

REGIME CHANGES

CAUSAL COUPLING EXISTS

DEPENDENCIES AMBIGUOUS

GOVERNANCE IMPACT EXISTS

IRREVERSIBLE STAKES EXIST
```

Fast-path reasoning must never weaken integrity.

---

# 55. Model Update

New evidence may:

```text
SUPPORT MODEL

WEAKEN MODEL

FALSIFY MODEL

NARROW SCOPE

CHANGE REGIME

CREATE COMPETING MODEL

LEAVE MODEL UNCHANGED
```

Model update should affect only dependent conclusions.

---

# 56. Selective Invalidation

Given:

```text
M1
├── C1
├── C2
└── C3
```

if only the premise supporting `C2` fails:

```text
INVALIDATE:
C2

PRESERVE:
C1
C3
```

provided no hidden dependency exists.

Thus:

```text
LOCAL FAILURE
!=
GLOBAL COGNITIVE RESET
```

---

# 57. Failure Recovery

```text
FAILED PREMISE
      ↓
INVALIDATE EDGE
      ↓
TRACE DESCENDANTS
      ↓
PRESERVE UNAFFECTED WORK
      ↓
REROUTE LOCALLY
```

Repeating the failed reasoning path without changed evidence is not recovery.

---

# 58. Null / Reset Boundary

A full reset should remain a last resort.

P4 should first attempt:

```text
LOCAL INVALIDATION
→ LOCAL REPAIR
→ ALTERNATIVE MODEL
→ REVALIDATION
```

before global recomputation where architecture permits.

This section is a compatibility rule with broader AMOS reasoning patterns, not evidence that an executable reset mechanism exists in P4.

---

# 59. Model Selection

When competing models can be compared, relevant dimensions may include:

```text
EVIDENTIAL SUPPORT

PROVENANCE INDEPENDENCE

PREDICTIVE PERFORMANCE

FALSIFIABILITY

SCOPE FIT

REGIME FIT

ASSUMPTION BURDEN

ROBUSTNESS

CAUSAL ADEQUACY
```

No single criterion automatically dominates across every domain.

---

# 60. Simplicity Boundary

Model simplicity can be useful.

But:

```text
SIMPLER
!=
TRUE
```

A simpler model may be preferred provisionally under declared criteria without being epistemically upgraded to verified truth.

---

# 61. Benchmark Boundary

A model performing well on benchmark \(B\) supports a claim scoped to that benchmark and its validity envelope.

It does not establish:

```text
UNIVERSAL MODEL VALIDITY
```

Thus:

$$
Success(B)
\not\Rightarrow
Success(AllDomains)
$$

---

# 62. Frontier / Established Separation

```yaml
P4_REASONING_OUTPUT:

  established:
    claims: []

  derived:
    claims: []

  models:
    claims: []

  speculative_frontier:
    claims: []

  competing:
    sets: []

  unknown_gaps: []
```

This prevents speculative content from becoming indistinguishable from stronger conclusions.

---

# 63. Uncertainty Vector

Where material, P4 may track uncertainty separately across:

```text
EVIDENCE

MODEL

SCOPE

TEMPORAL

CAUSAL

EXECUTION

PROVENANCE INDEPENDENCE
```

A single scalar confidence can hide materially different failure modes.

---

# 64. Decision-Relevant Uncertainty

Reasoning effort should focus on uncertainty capable of changing the outcome.

```text
UNCERTAINTY
   ↓
CAN IT FLIP RESULT?
   ├── NO → DEFER
   └── YES → INVESTIGATE
```

This is an efficiency rule subordinate to integrity.

---

# 65. Gap Classes

P4 may classify unresolved gaps as:

```text
CRITICAL

DECISION-RELEVANT

EXPLANATORY

COSMETIC
```

Resolve in that order.

A critical unresolved gap yields:

```text
UNKNOWN/GAP
```

for conclusions dependent on it.

---

# 66. Negative Cases

```yaml
P4_NEGATIVE_CASES:

  competing:
    - viable_hypothesis_silently_deleted
    - disagreement_forced_into_false_consensus
    - popularity_used_as_discriminator

  class_discipline:
    - source_claim_labeled_verified
    - model_labeled_observation
    - speculation_labeled_derived
    - unknown_gap_labeled_pass

  derivation:
    - hidden_load_bearing_assumption
    - invalid_transformation
    - stale_premise
    - incompatible_regime
    - confidence_exceeds_weakest_premise

  speculation:
    - frontier_reasoning_blended_into_established_result
    - analogy_treated_as_proof
    - extrapolation_unlabeled

  prediction:
    - predicted_event_treated_as_observed
    - successful_prediction_treated_as_unique_mechanism_proof

  causality:
    - correlation_treated_as_causal_effect
    - temporal_sequence_treated_as_causation
    - structural_similarity_treated_as_mechanism

  provenance:
    - descendants_counted_as_independent_sources
    - duplicated_source_support_inflation
    - ancestry_not_recoverable

  scope:
    - local_result_generalized_universally
    - regime_shift_ignored

  recovery:
    - entire_model_graph_invalidated_by_local_failure
    - failed_path_repeated_without_new_evidence

  boundary:
    - structural_cognition_model_presented_as_neuroscience_fact
```

---

# 67. Gap Register

```yaml
P4_GAPS:

  - id: P4-G001
    subject: U_3_exact_semantics
    class: DECISION_RELEVANT
    status: SOURCE_REFERENCE_PRESENT_DEFINITION_NOT_SUPPLIED

  - id: P4-G002
    subject: executable_hypothesis_manager
    class: DECISION_RELEVANT
    status: NOT_ESTABLISHED

  - id: P4-G003
    subject: executable_epistemic_classifier
    class: DECISION_RELEVANT
    status: NOT_ESTABLISHED

  - id: P4-G004
    subject: executable_competing_preservation_validator
    class: DECISION_RELEVANT
    status: NOT_ESTABLISHED

  - id: P4-G005
    subject: executable_speculation_isolation
    class: DECISION_RELEVANT
    status: NOT_ESTABLISHED

  - id: P4-G006
    subject: artifact_specific_validation_receipt
    class: DECISION_RELEVANT
    status: NOT_ESTABLISHED

  - id: P4-G007
    subject: neuroscience_equivalence
    class: EXPLANATORY
    status: OUT_OF_SCOPE
```

---

# 68. Falsifiers / Invalidation Conditions

P4 requires revision if:

### F1 — Higher canon supersedes its epistemic classes

A higher-authority canonical source establishes incompatible classifications.

### F2 — Viable competing models are destroyed without discrimination

An implementation forces convergence without sufficient evidence.

### F3 — Model output becomes observation by relabeling

A reasoning result is treated as externally observed merely because it was generated confidently.

### F4 — Speculation contaminates established results

Unsupported frontier assumptions become hidden premises in stronger claims.

### F5 — Provenance correlation is ignored

Repeated descendants are treated as independent confirmation.

### F6 — Structural cognition becomes neuroscience claim

The architecture is presented as a validated model of biological neural cognition without corresponding empirical evidence.

---

# 69. Promotion Gate

Promotion beyond `CONDITIONAL` requires:

* [ ] `U-3` semantics resolved from authoritative native source;
* [ ] hypothesis identity implemented;
* [ ] competing-set persistence implemented;
* [ ] epistemic class enforcement implemented;
* [ ] derivation/premise lineage persisted;
* [ ] bounded-speculation isolation implemented;
* [ ] provenance independence checks implemented;
* [ ] causal typing enforced where required;
* [ ] scope/regime envelopes implemented;
* [ ] sensitivity checks implemented for consequential conclusions;
* [ ] selective invalidation demonstrated;
* [ ] negative cases executed;
* [ ] artifact-specific validation receipt persisted;
* [ ] unresolved critical gaps remain visible.

Until then:

```text
CANONICAL STATUS
=
CONDITIONAL
```

---

# 70. Cross-Plane Bindings

```yaml
P4_BINDINGS:

  parent:
    - "[[AMOS_7_PART_UNIVERSE_CANON]]"

  predecessor:
    - "[[P3_KNOWLEDGE_MEMORY]]"

  evidence_origin:
    - "[[P2_SENSE_EVIDENCE]]"

  reality_boundary:
    - "[[P1_REALITY_ENVIRONMENT]]"

  hierarchy:
    - "[[HML_CANON]]"

  universe_canon:
    - "[[02_UNIVERSE_CANON_MOC]]"

  related_framework:
    - "[[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]"

  indexed_by:
    - "[[00_HOME]]"
    - "[[AMOS_RSCF_NODES]]"
```

---

# 71. P3 → P4 Transition

```text
P3
KNOWLEDGE / MEMORY
       │
       ▼
RETRIEVE VALID SUPPORT
       │
       ▼
P4
MODEL CONSTRUCTION
       │
       ├── DERIVATION
       ├── PREDICTION
       ├── HYPOTHESIS
       └── SPECULATION
       │
       ▼
CLASSIFY
       │
       ├── DERIVED
       ├── MODEL
       ├── CONDITIONAL
       ├── COMPETING
       └── UNKNOWN/GAP
```

The epistemic firewall remains:

$$
Reasoning
\not\Rightarrow
Observation
$$

---

# 72. Pre-Symbolic Spine Compatibility

Within the supplied Khung Trang model, P4 operates downstream of structural constraints.

The broader conceptual sequence is:

$$
\mathcal{P}
\rightarrow
\mathcal{D}
\rightarrow
\mathcal{R}
\rightarrow
\mathcal{C}
\rightarrow
\mathcal{F}
\rightarrow
\mathcal{M}
$$

P4 model-building must therefore not use semantic interpretation to silently override lower-level admitted constraints.

This is an AMOS-model compatibility mapping, not an empirical cognition claim.

---

# 73. H-Level RSCF

```yaml
H:

  identity:
    "P4 Cognition & Models Plane"

  role:
    "Reasoning, inference, prediction, model-building, and hypothesis-management plane"

  origin_architect:
    Trang_Phan

  steward:
    Trang_Phan

  system:
    AMOS_OS

  plane:
    01_CANON

  canonical_status:
    CONDITIONAL
```

---

# 74. M-Level RSCF

```yaml
M:

  laws:
    - P4_1_COMPETING_PRESERVATION
    - P4_2_CLASS_DISCIPLINE
    - P4_3_BOUNDED_SPECULATION

  subsystems:
    - inference
    - prediction
    - model_building
    - hypothesis_management
    - competing_preservation
    - epistemic_classification
    - derivation
    - speculation_isolation
    - causal_analysis
    - sensitivity
    - adversarial_validation

  firewalls:
    - REASONING_NE_EVIDENCE
    - MODEL_NE_OBSERVATION
    - PREDICTION_NE_OBSERVATION
    - CORRELATION_NE_CAUSATION
    - STRUCTURAL_SIMILARITY_NE_CAUSATION
    - SPECULATION_NE_DERIVATION
```

---

# 75. L-Level RSCF

```yaml
L:

  hypotheses:
    preserve_competing: true

  outputs:
    epistemically_typed: true

  derivations:
    premises_explicit: true
    dependencies_explicit: true

  speculation:
    tagged: true
    isolated: true

  provenance:
    ancestry_preserved: true

  independence:
    demonstrated_not_assumed: true

  scope:
    explicit_when_material: true

  regime:
    explicit_when_material: true

  causal_claims:
    typed: true

  sensitivity:
    required_when_consequential: true

  contradictions:
    preserve_when_unresolved: true

  invalidation:
    dependency_local: true
```

---

# 76. Full RSCF Contract

```yaml
RSCF:

  node_id:
    amos_01_canon_02_universe_canon_p4_cognition_models

  node_type:
    universe_plane

  functional_type:
    CognitionModelsPlane

  claim_class:
    AMOS_MODEL

  state:
    SOURCE_GROUNDED

  H:

    identity:
      "P4 Cognition & Models Plane"

    role:
      "Inference, prediction, model-building, and hypothesis-management layer"

  M:

    laws:
      - P4_1_COMPETING_PRESERVATION
      - P4_2_CLASS_DISCIPLINE
      - P4_3_BOUNDED_SPECULATION

    primitives:
      - inference
      - prediction
      - model
      - hypothesis
      - derivation
      - speculation
      - competing
      - falsifier
      - uncertainty
      - sensitivity

  L:

    competing:
      preserve: true

    class_discipline:
      required: true

    speculation:
      bounded: true
      isolated: true

    model_observation_boundary:
      enforced: true

    causal_firewall:
      required: true

    provenance_independence:
      demonstrated_not_assumed: true

  provenance:
    - AMOS_corpus
    - AMOS_7_PART_UNIVERSE_CANON
    - HML_CANON
    - P3_KNOWLEDGE_MEMORY
    - TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS

  scope:
    - UNIVERSE_CANON
    - P4_COGNITION_MODELS

  confidence_ceiling:

    architectural_model:
      SOURCE_GROUNDED

    implementation:
      UNKNOWN

    runtime:
      UNKNOWN

    neuroscience:
      NOT_CLAIMED

    empirical_claims:
      CLAIM_SPECIFIC
```

---

# 77. Canonical Compression

P4 reduces to three primary laws:

$$
\boxed{
Viable(H_1)\land Viable(H_2)\land
NoDiscriminator
\Rightarrow
COMPETING
}
$$

$$
\boxed{
EveryOutput
\Rightarrow
EpistemicClass
}
$$

and:

$$
\boxed{
Speculation
\Rightarrow
Tagged + Isolated
}
$$

The derivation firewall is:

$$
\boxed{
DERIVED
\neq
SPECULATIVE
}
$$

The observation firewall is:

$$
\boxed{
MODEL
\neq
OBSERVATION
}
$$

The causal firewall is:

$$
\boxed{
Similarity/Correlation
\not\Rightarrow
Causation
}
$$

The confidence firewall is:

$$
\boxed{
Conf(Derived)
\le
Conf(WeakestLoadBearingPremise)
}
$$

unless independently revalidated.

The operational chain is:

```text
P2 EVIDENCE + P3 KNOWLEDGE
            ↓
      P4 COGNITION
            ↓
   MODEL / INFERENCE
            ↓
       HYPOTHESES
            ↓
 ┌──────────┼──────────┐
 ↓          ↓          ↓
DERIVED    MODEL    COMPETING
                       │
                       ▼
             DISCRIMINATING TEST
```

Strongest current aggregate classification:

```text
P4 COGNITION & MODELS
=
SOURCE-GROUNDED
CONDITIONAL
AMOS MODEL
REASONING / MODELING PLANE

IMPLEMENTATION
=
NOT ESTABLISHED

RUNTIME VALIDATION
=
NOT ESTABLISHED

NEUROSCIENCE EQUIVALENCE
=
NOT CLAIMED

U-3 EXACT SEMANTICS
=
GAP IN SUPPLIED SOURCE
```

---

# 78. RSCF Node

RSCF-NODE

node_id:
amos_01_canon_02_universe_canon_p4_cognition_models

node_type:
universe_plane

functional_type:
CognitionModelsPlane

path:
01_CANON/02_UNIVERSE_CANON/P4_COGNITION_MODELS.md

origin_architect:
Trang Phan

steward:
Trang Phan

system:
AMOS OS

claim_class:
AMOS_MODEL

rscf_state:
SOURCE_GROUNDED

canonical_status:
CONDITIONAL

implementation_status:
NOT_ESTABLISHED

validation_status:
NOT_ESTABLISHED

RSCF-RELATIONS:

* INDEXED_BY: [[00_HOME]]

* INDEXED_BY: [[AMOS_RSCF_NODES]]

* INDEXED_BY: [[02_UNIVERSE_CANON_MOC]]

* CHILD_OF: [[AMOS_7_PART_UNIVERSE_CANON]]

* RECEIVES_FROM: [[P3_KNOWLEDGE_MEMORY]]

* USES_EVIDENCE_FROM: [[P2_SENSE_EVIDENCE]]

* INHERITS_REALITY_BOUNDARY_FROM: [[P1_REALITY_ENVIRONMENT]]

* RELATED_HIERARCHY: [[HML_CANON]]

* RELATED_FRAMEWORK: [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

* GOVERNS:
  INFERENCE

* GOVERNS:
  PREDICTION

* GOVERNS:
  MODEL_BUILDING

* GOVERNS:
  HYPOTHESIS_MANAGEMENT

* GOVERNS:
  COMPETING_PRESERVATION

* GOVERNS:
  EPISTEMIC_CLASS_DISCIPLINE

* GOVERNS:
  BOUNDED_SPECULATION

---

00_ROOT_MOC|AMOS MOC

---

**Related:** [[AMOS_7_PART_UNIVERSE_CANON]] · [[P1_REALITY_ENVIRONMENT]] · [[P2_SENSE_EVIDENCE]] · [[P3_KNOWLEDGE_MEMORY]] · [[HML_CANON]] · [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]] · [[00_HOME]] · [[AMOS_RSCF_NODES]]

---

**MOC:** [[02_UNIVERSE_CANON_MOC]]

---

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---

**Origin architect / steward:** **Trang Phan**

```

The normalized P4 keeps the supplied three-law spine intact: **preserve viable competing hypotheses, type every epistemic output, and isolate speculative frontier reasoning**. Two boundaries are deliberately not promoted beyond the source: the exact semantics of **`U-3` remain a gap**, and the cognition architecture remains an **AMOS structural model, not a neuroscience claim**.
