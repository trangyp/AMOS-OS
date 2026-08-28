---
title: Causal Integrity Canon
type: canon
source: 01_CANON/01_CORE_LAWS
artifact: CAUSAL_INTEGRITY_CANON.md
artifact_id: amos_01_canon_01_core_laws_causal_integrity_canon
origin_architect: Trang Phan
steward: Trang Phan
system: AMOS OS
plane: 01_CANON
segment: 01_CANON/01_CORE_LAWS
artifact_kind: CANON
path: 01_CANON/01_CORE_LAWS/CAUSAL_INTEGRITY_CANON.md
canon_group: amos_core
schema_family: RSCF
schema_role: CAUSAL_INTEGRITY_RSCF
schema_version: AMOS_CORE_v4.4-compatible-conceptual
tags:
- amos_os
- canon
- universe
- 01_canon
- core_laws
- causal_integrity
- causal_firewall
- causal_lineage
- provenance
- provenance_topology
- competing_hypotheses
- epistemic_regimes
- scope
- regime
- dependency_graph
- falsification
- validation
- rscf
- canon/universe
- placeholder_expanded
- architecture
- l19-proof-capsule
- law-hierarchy
- 00-home
- amos-rscf-nodes
- canon-law-crosswalk
- routing-policy-validation-receipt
- authz-engine-validation-receipt
version: 0.2.0
updated: '2026-08-27'
status: PLACEHOLDER_EXPANDED
epistemic_class: AMOS_MODEL
canonical_status: UNKNOWN/GAP
implementation_status: NOT_ESTABLISHED
validation_status: NOT_ESTABLISHED
executable_binding: NOT_ESTABLISHED
ingestion_action: ADD_ONLY
native_causal_law_status: NOT_ESTABLISHED
causal_inference_engine_status: NOT_ESTABLISHED
causal_validation_status: NOT_ESTABLISHED
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: core_laws
  regime: canon_placeholder
  confidence_ceiling: source_supported
  provenance_independence: NOT_ESTABLISHED
---

# Causal Integrity Canon

## 0. Status

`CAUSAL_INTEGRITY_CANON.md` is an **ADD-ONLY placeholder-expanded artifact** for:

```text
01_CANON/01_CORE_LAWS

It reserves the canonical slot for the AMOS framework family concerned with **causal integrity**.

This expansion defines a conservative target contract for causal reasoning, provenance, dependency typing, competing explanations, scope/regime validity, falsification, and causal claim governance.

It does **not** establish that a substantive native Causal Integrity Canon has yet been recovered, validated, promoted, or implemented.

Current state:

```yaml
status: PLACEHOLDER_EXPANDED
epistemic_class: AMOS_MODEL
canonical_status: UNKNOWN/GAP
implementation_status: NOT_ESTABLISHED
validation_status: NOT_ESTABLISHED
executable_binding: NOT_ESTABLISHED

native_causal_law_status: NOT_ESTABLISHED
causal_inference_engine_status: NOT_ESTABLISHED
causal_validation_status: NOT_ESTABLISHED
```

Origin architect / steward:

**Trang Phan**

System:

**AMOS OS**

---

# 1. Governing Integrity Boundary

The Causal Integrity Canon MUST preserve:

```text
PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

DOCUMENTED != ENFORCED

MODEL != OBSERVATION

SOURCE_CLAIM != VERIFIED

CANON_CANDIDATE != CANONICAL

CANONICAL != EMPIRICAL_TRUTH

ASSOCIATION != CAUSATION

CORRELATION != CAUSATION

CO-OCCURRENCE != CAUSATION

TEMPORAL PRECEDENCE != CAUSATION

STRUCTURAL SIMILARITY != CAUSATION

PREDICTION != CAUSATION

MECHANISM MODEL != VERIFIED MECHANISM

DEPENDENCY != CAUSATION

ENABLING CONDITION != SUFFICIENT CAUSE

NECESSARY CONDITION != SUFFICIENT CONDITION

MEDIATION != CONFOUNDING

INTERVENTION != VALID CAUSAL IDENTIFICATION

ABSENCE OF CONTRADICTION != CAUSAL PROOF

MULTIPLE REPORTS != INDEPENDENT CONFIRMATION

CAPABILITY != AUTHORITY

AUTHORIZATION != COMMIT

PROPOSAL != COMMIT

IMPLEMENTED != VALIDATED

LOGGED != APPROVED

UNKNOWN/GAP != PASS
```

These distinctions are mandatory.

---

# 2. Purpose

The **Causal Integrity Canon** is intended to govern how AMOS represents, evaluates, propagates, challenges, and invalidates causal claims.

Its target function is:

```text
OBSERVE
↓
TYPE
↓
BOUND
↓
TRACE
↓
COMPARE EXPLANATIONS
↓
TEST IDENTIFICATION
↓
CHALLENGE
↓
CLASSIFY
↓
ACT OR HOLD
```

The governing objective is not maximum causal explanation.

It is:

```text
MAXIMUM CAUSAL INTEGRITY
UNDER AVAILABLE EVIDENCE
```

---

# 3. Core Causal Law

The target governing principle is:

```text
DO NOT PROMOTE A RELATION
TO A STRONGER CAUSAL CLASS
THAN THE EVIDENCE LICENSES
```

Conceptually:

```text
EVIDENCE STRENGTH
≥
REQUIRED SUPPORT FOR CLAIM CLASS
```

must hold before promotion.

This is a reasoning discipline, not a claim of a universally established mathematical law.

---

# 4. Non-Purpose

This artifact MUST NOT be used to claim:

* universal causal laws of reality;
* scientific proof from architectural coherence;
* biological causation from analogy;
* causal necessity from correlation;
* causal sufficiency from temporal ordering;
* mechanisms merely because a model can describe observations;
* intervention validity without identification assumptions;
* universal applicability from success in one regime;
* causal independence from duplicated sources;
* empirical validation from simulation alone;
* mathematical theoremhood where no proof exists;
* runtime enforcement where executable binding is absent.

---

# 5. Ingestion Rule

```yaml
AMOS_CANON_INGESTION_RULE:

  existing_folder:
    preserve: true

  existing_file:
    preserve: true
    overwrite: false

  new_framework:
    action: ADD_FILE_TO_EXISTING_FOLDER

  master_source:
    action: NORMALIZE_TO_RSCF_FILE

  framework_existing_in_multiple_sources:
    action:
      - CREATE_ONE_CANONICAL_NODE
      - LINK_ALL_SOURCE_PROVENANCE
      - DO_NOT_CREATE_DUPLICATE_CANON

  historical_source:
    action:
      - LINK_TO_CANON
      - RECORD_LINEAGE
      - PRESERVE_HERITAGE

  external_research:
    action:
      - KEEP_OUT_OF_NATIVE_CANON
      - LINK_AS_EVIDENCE

  duplicate_filename:
    action:
      - COMPARE_CONTENT_AND_LINEAGE
      - DO_NOT_OVERWRITE

  uncertainty:
    action:
      - MARK_GAP_OR_COMPETING
      - NEVER_INVENT_CANON
```

---

# 6. Causal Firewall

AMOS causal reasoning SHOULD distinguish at minimum:

```text
ASSOCIATION

CORRELATION

TEMPORAL PRECEDENCE

DEPENDENCY

ENABLING CONDITION

NECESSARY CONDITION

SUFFICIENT CONDITION

MECHANISM

MEDIATION

CONFOUNDING

FEEDBACK

INTERVENTION EFFECT

CAUSAL EFFECT

UNKNOWN
```

These relation classes MUST NOT be silently collapsed.

---

# 7. Association

Association means variables, states, or events exhibit a relationship under a declared observation process.

Conceptually:

```text
A ↔ B
```

may be observed.

This does not establish:

```text
A → B
```

nor:

```text
B → A
```

nor:

```text
C → {A,B}
```

The causal structure remains unresolved.

---

# 8. Correlation

A correlation is an association represented by an appropriate statistical relationship.

Canonical boundary:

```text
CORRELATION
!=
CAUSATION
```

A correlation may arise from:

```text
A → B

B → A

C → A
C → B

A ↔ B FEEDBACK

SELECTION

MEASUREMENT ARTIFACT

CHANCE

MODEL MISSPECIFICATION
```

until discriminating evidence resolves alternatives.

---

# 9. Temporal Precedence

If:

```text
A occurs before B
```

then temporal ordering may be consistent with:

```text
A → B
```

but temporal precedence alone does not establish it.

Possible alternatives include:

```text
C → A
C → B

A ← latent process → B

measurement delay

selection artifact

common trend

feedback with delayed observation
```

Therefore:

```text
BEFORE
!=
CAUSE
```

---

# 10. Dependency

A logical, computational, architectural, or evidential dependency is not automatically a causal relation in the empirical sense.

```text
CLAIM_B
DEPENDS_ON
CLAIM_A
```

means failure of `CLAIM_A` may invalidate `CLAIM_B`.

It does not necessarily mean:

```text
CLAIM_A
CAUSES
CLAIM_B
```

in the world being modeled.

---

# 11. Enabling Condition

An enabling condition permits or facilitates an outcome.

```text
E enables Y
```

does not establish:

```text
E is sufficient for Y
```

nor necessarily:

```text
E is necessary for Y
```

The exact relation must remain typed.

---

# 12. Necessary Condition

A target semantic form:

```text
Y → X
```

may represent that `X` is required whenever `Y` occurs.

But:

```text
X NECESSARY_FOR Y
```

does not establish:

```text
X SUFFICIENT_FOR Y
```

---

# 13. Sufficient Condition

A target semantic form:

```text
X → Y
```

under declared assumptions may represent sufficiency.

But sufficiency is scope-bound.

```text
X sufficient under R1
```

does not establish:

```text
X sufficient under R2
```

---

# 14. Necessary and Sufficient

A biconditional causal or logical relationship requires stronger support than either direction independently.

```text
X ↔ Y
```

MUST NOT be inferred merely because both frequently co-occur.

Each direction requires support appropriate to its semantics.

---

# 15. Mechanism

A mechanism describes an intermediate process by which an antecedent may produce an outcome.

Target representation:

```text
X
↓
M1
↓
M2
↓
Y
```

A proposed mechanism remains:

```text
MODEL
```

until appropriately validated.

Mechanistic plausibility strengthens explanation but is not itself universal proof of causal effect.

---

# 16. Mediation

A mediation structure may be represented:

```text
X → M → Y
```

The claim that `M` mediates an effect requires more than observing correlations among `X`, `M`, and `Y`.

Alternative structures MUST remain visible when supported.

---

# 17. Confounding

A confounding structure may be represented:

```text
      C
     / \
    ↓   ↓
    X   Y
```

An observed relationship:

```text
X ↔ Y
```

may therefore arise without:

```text
X → Y
```

A causal claim SHOULD identify material confounders or explicitly register their uncertainty.

---

# 18. Collider Boundary

A target causal model may contain:

```text
X → C ← Y
```

Conditioning on `C` can alter observed relationships between `X` and `Y`.

Therefore conditioning decisions are themselves part of causal integrity.

The presence and treatment of colliders must not be invented when the causal structure is unknown.

---

# 19. Feedback

Causal systems may contain feedback:

```text
A → B
↑   ↓
└── C
```

In such systems, static one-direction causal descriptions may be insufficient.

Target representations SHOULD declare:

```text
TIME
STATE
DIRECTION
DELAY
REGIME
```

when material.

---

# 20. Direct and Indirect Effects

Target distinction:

```text
X ─────────→ Y
 \
  → M →────→ Y
```

Potentially:

```text
DIRECT EFFECT
INDIRECT EFFECT
TOTAL EFFECT
```

These MUST NOT be conflated when the distinction changes interpretation or action.

---

# 21. Causal Effect

A causal effect concerns how an outcome would differ under appropriately defined changes or interventions in a cause.

A causal-effect claim SHOULD identify:

```text
CAUSE VARIABLE

OUTCOME VARIABLE

INTERVENTION / CONTRAST

POPULATION OR SYSTEM

TIME HORIZON

REGIME

ASSUMPTIONS

IDENTIFICATION BASIS
```

Without these, the claim may be under-specified.

---

# 22. Counterfactual Boundary

Counterfactual reasoning conceptually compares:

```text
Y under X = x1
```

with:

```text
Y under X = x0
```

for an appropriately defined unit, system, or population.

The unobserved counterfactual is not directly observed merely because the factual outcome is known.

Therefore counterfactual conclusions remain dependent on assumptions, design, or validated causal models.

---

# 23. Intervention Boundary

An intervention is not automatically a valid causal experiment.

Potential failures include:

```text
INTERVENTION CHANGES MULTIPLE VARIABLES

NONCOMPLIANCE

SELECTION

SPILLOVER

MEASUREMENT CHANGE

REGIME CHANGE

INTERFERENCE

INSUFFICIENT RANDOMIZATION

UNCONTROLLED CONFOUNDING
```

Thus:

```text
INTERVENTION OCCURRED
!=
CAUSAL EFFECT IDENTIFIED
```

---

# 24. Experimental Evidence

Randomized intervention evidence may support causal inference when the design and execution satisfy the relevant assumptions.

However:

```text
RANDOMIZED
!=
UNIVERSALLY VALID
```

External validity remains bounded by:

```text
POPULATION

ENVIRONMENT

TIME

IMPLEMENTATION

MEASUREMENT

REGIME
```

---

# 25. Observational Evidence

Observational evidence can support causal inference only under appropriately justified assumptions and methods.

It MUST NOT be automatically downgraded to useless evidence.

It MUST also not be automatically upgraded to experimental equivalence.

Correct class:

```text
METHOD- AND ASSUMPTION-DEPENDENT
```

---

# 26. Natural Experiments

A natural experiment may strengthen causal identification when assignment or exposure approximates a suitable exogenous variation.

The causal license depends on whether the relevant assumptions actually hold.

The label:

```text
NATURAL EXPERIMENT
```

does not itself prove validity.

---

# 27. Quasi-Experimental Evidence

Methods such as:

```text
REGRESSION DISCONTINUITY

DIFFERENCE-IN-DIFFERENCES

INSTRUMENTAL VARIABLES

MATCHING

SYNTHETIC CONTROL
```

may support causal inference under method-specific assumptions.

This canon does not declare those assumptions universally satisfied.

---

# 28. Simulation Boundary

Simulation can test consequences of a model.

It cannot by itself prove that the model is an empirically correct causal representation.

```text
SIMULATION CONSISTENT
!=
REAL-WORLD CAUSAL [[VALIDATION]]
```

---

# 29. Prediction Boundary

A model may predict `Y` accurately from `X` without `X` causing `Y`.

Therefore:

```text
HIGH PREDICTIVE ACCURACY
!=
CAUSAL IDENTIFICATION
```

Predictive evidence and causal evidence remain distinct.

---

# 30. Explanation Boundary

A coherent explanation may organize observations well.

But:

```text
COHERENT STORY
!=
VERIFIED CAUSAL MODEL
```

Narrative coherence must not bridge missing causal evidence.

---

# 31. Causal Claim Classes

Target causal claim vocabulary:

```text
ASSOCIATED_WITH

CORRELATED_WITH

PRECEDES

DEPENDS_ON

ENABLES

NECESSARY_FOR

SUFFICIENT_FOR

MEDIATES

CONFOUNDS

MODERATES

CAUSES

CAUSAL_EFFECT_OF

FEEDBACK_WITH

UNKNOWN_CAUSAL_RELATION
```

Every consequential causal edge SHOULD use the weakest accurate class.

---

# 32. Epistemic Classes

Causal conclusions remain separately classified as:

```text
VERIFIED

DERIVED

MODEL

CONDITIONAL

COMPETING

UNKNOWN/GAP
```

Thus a relation can conceptually be:

```text
relation_type: CAUSES
epistemic_class: CONDITIONAL
```

if its causal interpretation depends materially on unresolved assumptions.

---

# 33. Causal Claim Target Schema

```yaml
causal_claim:

  claim_id: stable_identifier

  source:
    variable_or_state: required

  target:
    variable_or_state: required

  relation_type:
    required

  epistemic_class:
    required

  provenance:
    - source_ref

  evidence:
    - evidence_ref

  scope:
    system: required
    population: optional
    environment: optional
    scale: optional
    time: optional

  regime:
    value: required

  mechanism:
    status: established | proposed | unknown
    ref: optional

  confounders:
    known:
      - ref
    unresolved:
      - ref

  assumptions:
    - assumption

  competing_hypotheses:
    - hypothesis_ref

  falsifiers:
    - invalidation_condition

  dependencies:
    - dependency_ref

  confidence_ceiling:
    value: required

  validation:
    status: required
    receipt: optional
```

This is a target schema.

It is not evidence of an implemented causal engine.

---

# 34. Evidence Typing

Causal support SHOULD distinguish:

```text
SOURCE_CLAIM

OBSERVATION

DERIVED

MODEL

DECISION

UNKNOWN
```

These classes answer different questions.

For example:

```text
SOURCE_CLAIM:
"A causes B"
```

is evidence that a source made the claim.

It is not itself an observation establishing that causal relation.

---

# 35. Observation Boundary

An observation may establish:

```text
A observed
B observed
```

or:

```text
A and B co-occurred
```

depending on measurement.

It does not automatically establish:

```text
A caused B
```

The causal step must be separately licensed.

---

# 36. Source Claim Boundary

If ten documents state:

```text
A causes B
```

but all descend from one original source, the topology may contain:

```text
1 ROOT CLAIM
+
10 DESCENDANT REPORTS
```

not ten independent causal confirmations.

---

# 37. Provenance Topology

Target representation:

```text
ROOT SOURCE
     ↓
OBSERVATION / CLAIM
     ↓
TRANSFORMATION
     ↓
DERIVED RESULT
     ↓
CAUSAL CONCLUSION
```

Each consequential conclusion SHOULD retain enough lineage to recover its load-bearing ancestry.

---

# 38. Provenance Independence

Independent causal confirmation MUST be demonstrated rather than inferred from file count, popularity, authority, or repetition.

Check shared:

```text
DATA

SOURCE

AUTHORSHIP

MEASUREMENT PIPELINE

MODEL

TRANSFORMATION

ASSUMPTIONS

DOCUMENT LINEAGE
```

when material.

---

# 39. Anti-Sybil Causal Evidence Rule

Invalid:

```text
SOURCE A
├── REPORT 1
├── REPORT 2
├── REPORT 3
└── REPORT 4

THEREFORE:
4 INDEPENDENT CAUSAL CONFIRMATIONS
```

Correct:

```text
1 ROOT ANCESTRY
+
4 DESCENDANTS
```

unless independent evidence paths are demonstrated.

---

# 40. Causal Lineage

A causal conclusion SHOULD retain lineage:

```text
RAW EVIDENCE
↓
OBSERVATION
↓
DERIVED ASSOCIATION
↓
CAUSAL MODEL
↓
CAUSAL CLAIM
↓
DECISION
```

This permits selective invalidation.

---

# 41. Dependency Closure

For causal conclusion `C`, traverse only dependencies that can materially alter `C`.

Target:

```text
CAUSAL CLAIM
↓
IDENTIFICATION PREMISES
↓
LOAD-BEARING EVIDENCE
↓
PROVENANCE
↓
SCOPE / REGIME
↓
COMPETING EXPLANATIONS
```

Raw evidence defaults to:

```text
DO_NOT_LOAD_UNLESS_REQUIRED
```

---

# 42. Confidence Ceiling

For a causal conclusion depending on premises:

```text
P1 ... Pn
```

the conclusion SHOULD NOT receive stronger confidence than its weakest load-bearing premise unless independent revalidation repairs that weakness.

Conceptually:

```text
CONFIDENCE(C)
<=
MIN_LOAD_BEARING_CONFIDENCE(P1...Pn)
```

This is a reasoning constraint, not a universal probability theorem.

---

# 43. Causal Identification

A causal claim requires an identification path appropriate to its evidence and design.

Target question:

```text
WHAT DISTINGUISHES
THE PROPOSED CAUSAL MODEL
FROM PLAUSIBLE ALTERNATIVES?
```

If no answer exists:

```text
CAUSAL IDENTIFICATION = UNKNOWN/GAP
```

---

# 44. Competing Hypotheses

Suppose observation:

```text
A associated with B
```

Candidate explanations may include:

```text
H1: A → B

H2: B → A

H3: C → A and C → B

H4: A ↔ B through feedback

H5: selection artifact

H6: measurement artifact

H7: chance / instability
```

The system MUST NOT force convergence while multiple explanations remain viable.

---

# 45. COMPETING State

When hypotheses have:

```text
EQUAL SUPPORT

INCOMPARABLE SUPPORT

CORRELATED SUPPORT

INSUFFICIENT SUPPORT
```

preserve:

```text
COMPETING
```

until discriminating evidence exists.

---

# 46. Discriminating Evidence

The preferred next action is not necessarily more evidence.

It is the cheapest high-information test that separates plausible causal models.

Conceptually:

```text
MAXIMIZE:
EXPECTED DISCRIMINATION

MINIMIZE:
COST + RISK + IRREVERSIBILITY
```

---

# 47. Falsifiers

Every consequential causal model SHOULD identify conditions that would weaken or invalidate it.

Examples:

```text
CAUSE OCCURS WITHOUT EXPECTED EFFECT

EFFECT OCCURS WITHOUT REQUIRED CAUSE

INTERVENTION FAILS UNDER EXPECTED CONDITIONS

ALTERNATIVE MODEL PREDICTS DISCRIMINATING RESULT

MECHANISM MEASUREMENT CONTRADICTS MODEL

REGIME CHANGE INVALIDATES ASSUMPTIONS
```

---

# 48. Absence of Falsification

Canonical boundary:

```text
NOT YET FALSIFIED
!=
VERIFIED
```

A model may survive because discriminating tests have not been performed.

---

# 49. Scope Firewall

Every important causal claim SHOULD inherit an applicability envelope:

```yaml
scope:
  system: required
  population: optional
  environment: optional
  scale: optional
  time: optional
  measurement_method: optional
  assumptions:
    - assumption
```

Causal validity outside this envelope is not automatically established.

---

# 50. Regime Firewall

A causal relation valid under:

```text
REGIME R1
```

may fail under:

```text
REGIME R2
```

because mechanisms, constraints, incentives, environment, or system topology may change.

Therefore:

```text
VALID_CAUSAL_CLAIM(R1)
!=
VALID_CAUSAL_CLAIM(R2)
```

unless transfer is established.

---

# 51. Regime Shift

A regime shift SHOULD trigger revalidation when it changes any load-bearing causal premise.

Examples:

```text
POLICY CHANGE

ENVIRONMENT CHANGE

[[ARCHITECTURE]] CHANGE

POPULATION CHANGE

MEASUREMENT CHANGE

BEHAVIORAL ADAPTATION

FEEDBACK STRUCTURE CHANGE
```

---

# 52. Temporal Validity

Causal relations may change over time.

Therefore a claim SHOULD declare temporal validity when material.

```text
CAUSE AT t1
```

does not universally imply:

```text
CAUSE AT t2
```

---

# 53. Scale Firewall

A relation observed at one scale may not hold at another.

Examples:

```text
INDIVIDUAL
GROUP
ORGANIZATION
SYSTEM
POPULATION
```

Cross-scale inference remains `MODEL` unless independently validated.

---

# 54. Aggregation Boundary

Aggregate relationships do not automatically establish unit-level causal relationships.

Likewise unit-level relationships do not automatically determine aggregate outcomes.

Therefore:

```text
AGGREGATE PATTERN
!=
INDIVIDUAL CAUSAL EFFECT
```

---

# 55. Cross-Domain Firewall

Structural correspondence between:

```text
BIOLOGY
COMPUTATION
ECONOMICS
COGNITION
PHYSICS
SOCIAL SYSTEMS
```

does not establish shared causal mechanisms.

Cross-domain causal mappings default to:

```text
MODEL
```

until independently validated.

---

# 56. Structural Similarity Firewall

If two systems share:

```text
FEEDBACK LOOPS

NETWORK TOPOLOGY

OPTIMIZATION STRUCTURE

EQUATION FORM

STATE TRANSITIONS
```

the safe conclusion is structural similarity.

Not:

```text
SAME CAUSAL LAW
```

unless supported independently.

---

# 57. Causal Direction

When direction is unresolved:

```text
A ↔ B
```

SHOULD remain non-directional or competing.

Do not silently choose:

```text
A → B
```

because it produces a cleaner narrative.

---

# 58. Hidden Variables

Potential unobserved variables SHOULD remain represented as uncertainty rather than silently excluded.

Conceptually:

```text
U
↙ ↘
A   B
```

If `U` cannot be ruled out and matters to identification:

```text
CAUSAL CLAIM = CONDITIONAL
```

or:

```text
UNKNOWN/GAP
```

depending on severity.

---

# 59. Selection Effects

Selection into observation, treatment, survival, publication, or analysis may alter apparent relationships.

A causal claim SHOULD test selection mechanisms when they can change the conclusion.

---

# 60. Measurement Integrity

Causal integrity depends on measurement integrity.

Potential failures include:

```text
MISCLASSIFICATION

MEASUREMENT DRIFT

PROXY FAILURE

INSTRUMENT CHANGE

DIFFERENTIAL ERROR

MISSINGNESS

POST-TREATMENT MEASUREMENT
```

A causal conclusion cannot be stronger than load-bearing measurement validity.

---

# 61. Proxy Boundary

A proxy variable:

```text
P
```

used for latent construct:

```text
L
```

does not establish:

```text
P = L
```

Causal interpretation must preserve proxy uncertainty.

---

# 62. Intervention Fidelity

If an intervention is intended to modify:

```text
X
```

but actually changes:

```text
X + Z + environment
```

then attributing all effects to `X` may be invalid.

Intervention fidelity is therefore load-bearing.

---

# 63. Interference

If one unit's treatment affects another unit's outcome, naive independent-unit assumptions may fail.

Target systems SHOULD represent interference when material rather than silently assume independence.

---

# 64. Heterogeneous Effects

A causal effect may differ by:

```text
POPULATION

CONTEXT

TIME

BASELINE STATE

ENVIRONMENT

REGIME

SUBSYSTEM
```

Therefore an average effect MUST NOT automatically be interpreted as a universal individual effect.

---

# 65. Nonlinearity

Causal response may be nonlinear:

```text
small ΔX → small ΔY
```

does not establish:

```text
large ΔX → proportionally large ΔY
```

Extrapolation beyond observed or validated ranges remains conditional.

---

# 66. Threshold Effects

A causal mechanism may activate only beyond:

```text
X ≥ θ
```

A target claim SHOULD preserve threshold assumptions where they materially affect outcomes.

---

# 67. Saturation

Effects may plateau:

```text
X ↑
Y ↑
then
Y ≈ constant
```

Linear extrapolation beyond saturation can produce invalid causal predictions.

---

# 68. Interaction Effects

Potential structure:

```text
EFFECT(X → Y)
depends on
Z
```

Then `Z` is an effect modifier or interaction variable under the model.

A marginal causal statement may be misleading if interaction is load-bearing.

---

# 69. Feedback Adaptation

Interventions may change the system that generated the original evidence.

Conceptually:

```text
POLICY
↓
BEHAVIOR CHANGE
↓
SYSTEM ADAPTATION
↓
NEW CAUSAL REGIME
```

Thus historical causal estimates may become stale after deployment.

---

# 70. Reflexive Systems

In systems where agents react to predictions, policies, or measurements:

```text
MODEL OUTPUT
↓
AGENT RESPONSE
↓
ENVIRONMENT CHANGE
↓
MODEL VALIDITY CHANGE
```

The causal model may participate in its own invalidation.

This requires regime-aware revalidation.

---

# 71. Sensitivity

For every consequential causal conclusion, identify the smallest premise capable of flipping the result.

Examples:

```text
ONE CONFOUNDER

ONE IDENTIFICATION ASSUMPTION

ONE MEASUREMENT ERROR

ONE REGIME BOUNDARY

ONE PROVENANCE DEPENDENCY

ONE EFFECT-MODIFICATION THRESHOLD
```

Test these first.

---

# 72. Fragility

If plausible perturbation of one assumption changes:

```text
CAUSES
```

to:

```text
ASSOCIATED_WITH
```

the causal result is fragile.

Correct class:

```text
CONDITIONAL
```

---

# 73. Robustness

A causal conclusion is more robust when it survives plausible changes to noncritical:

```text
MODEL SPECIFICATION

MEASUREMENT CHOICE

SAMPLE

THRESHOLD

ASSUMPTION

ESTIMATION PATH
```

without changing the decision-relevant result.

Robustness does not eliminate scope boundaries.

---

# 74. Proof Capsule — Causal Claim

A consequential causal conclusion SHOULD conceptually carry:

```yaml
proof_capsule:

  claim:
    cause: X
    relation: CAUSES
    outcome: Y

  claim_class:
    CONDITIONAL

  load_bearing_premises:
    - premise_ref

  evidence:
    - evidence_ref

  provenance:
    - source_ref

  identification:
    method: declared
    assumptions:
      - assumption

  scope:
    system: declared
    population: declared
    environment: declared

  regime:
    value: declared

  temporal_validity:
    value: declared

  competing_explanations:
    - hypothesis_ref

  falsifiers:
    - invalidation_condition

  dependencies:
    - dependency_ref

  confidence_ceiling:
    value: declared

  provenance_independence:
    state: established | partial | unknown
```

---

# 75. Proof Capsule Reuse

A causal proof capsule may be reused only while:

```text
DEPENDENCIES VALID

SCOPE MATCHES

REGIME MATCHES

FRESHNESS VALID

PROVENANCE VALID

NO NEW MATERIAL CONFLICT
```

If any fail:

```text
REVALIDATE
```

---

# 76. Selective Invalidation

Suppose:

```text
C3 depends on C2
C2 depends on C1
```

and `C1` fails.

Invalidate:

```text
C1
↓
C2
↓
C3
```

but preserve unrelated conclusions.

This is causal lineage repair, not global erasure.

---

# 77. Causal Epoch

A causal model may be treated as valid only for a bounded causal epoch:

```text
EPOCH E
```

where its:

```text
REGIME
DEPENDENCIES
SCOPE
MEASUREMENT
ASSUMPTIONS
```

remain stable enough for reuse.

A new regime may require a new causal epoch.

This is a conceptual governance model, not a claim that the current ChatGPT runtime implements distributed causal epochs.

---

# 78. Epoch Finality Boundary

A finalized causal conclusion for epoch `E` means only that it satisfied the declared governance conditions for that epoch.

It does not mean:

```text
TRUE FOR ALL FUTURE EPOCHS
```

---

# 79. H/M/L Fractal Target

```text
H — CAUSAL INTEGRITY SYSTEM
      ↓
M — CAUSAL SUBSYSTEM / CLAIM FAMILY
      ↓
L — CLAIM / EDGE / ASSUMPTION / FALSIFIER
      ↓
RAW EVIDENCE
```

Raw evidence:

```text
DO_NOT_LOAD_UNLESS_REQUIRED
```

---

# 80. H-Layer

Target node:

```text
RSCF.AMOS.[[CANON]].CAUSAL_INTEGRITY.H.SYSTEM
```

Responsibilities:

```text
CAUSAL ROUTING

CLAIM TYPING

SCOPE CONTROL

REGIME CONTROL

PROVENANCE CONTROL

CONFLICT VISIBILITY

[[VALIDATION]] ROUTING
```

---

# 81. Candidate M-Layer Families

Target organization:

```text
M.ASSOCIATION

M.CAUSAL_DIRECTION

M.MECHANISM

M.CONFOUNDING

M.MEDIATION

M.INTERVENTION

M.COUNTERFACTUAL

M.FEEDBACK

M.PROVENANCE

M.COMPETING_HYPOTHESES

M.SCOPE_REGIME

M.FALSIFICATION

M.[[VALIDATION]]
```

These are organizational target categories, not claims of already populated native canon.

---

# 82. Candidate L-Layer Nodes

```text
L.CAUSAL_CLAIM

L.CAUSAL_EDGE

L.EVIDENCE

L.CONFOUNDER

L.MEDIATOR

L.MODERATOR

L.MECHANISM

L.INTERVENTION

L.ASSUMPTION

L.SCOPE_ENVELOPE

L.REGIME_ENVELOPE

L.COMPETING_HYPOTHESIS

L.FALSIFIER

L.[[L19_PROOF_CAPSULE]]

L.VALIDATION_RECEIPT

L.GAP
```

---

# 83. RSCF Causal Graph

Target:

```text
CAUSAL_CLAIM
     │
     ├── SUPPORTED_BY ───────> EVIDENCE
     │
     ├── DEPENDS_ON ─────────> PREMISE
     │
     ├── BOUNDED_BY ─────────> SCOPE
     │
     ├── VALID_IN ───────────> REGIME
     │
     ├── COMPETES_WITH ──────> HYPOTHESIS
     │
     ├── CHALLENGED_BY ──────> FALSIFIER
     │
     ├── DERIVED_FROM ───────> MODEL
     │
     ├── PROVENANCE_FROM ────> SOURCE
     │
     └── VALIDATED_BY ───────> RECEIPT
```

---

# 84. Fast Path

Local causal reasoning is allowed only when:

```text
DEPENDENCY CLOSURE ESTABLISHED

PROVENANCE INDEPENDENCE SUFFICIENT

SCOPE COMPATIBLE

REGIME COMPATIBLE

FRESHNESS ACCEPTABLE

NO MATERIAL CONFLICT

CAUSAL TYPE DOES NOT EXCEED EVIDENCE
```

Otherwise escalate.

---

# 85. Escalation Conditions

Escalate when:

```text
SHARED EVIDENCE ANCESTRY

CONFLICTING OBSERVATIONS

STALE DATA

REGIME SHIFT

CROSS-DOMAIN TRANSFER

CROSS-SCALE TRANSFER

CAUSAL DIRECTION UNCLEAR

HIDDEN CONFOUNDING PLAUSIBLE

FEEDBACK MATERIAL

GOVERNANCE IMPACT

IRREVERSIBLE STAKES

AMBIGUOUS DEPENDENCIES
```

---

# 86. Adversarial Validation

For consequential causal claims:

1. construct the strongest supported conclusion;
2. independently search for a contradictory causal path;
3. test correlated provenance;
4. test stale premises;
5. test scope leakage;
6. test regime mismatch;
7. test hidden dependency;
8. test causal-direction reversal;
9. test confounding;
10. test stronger competing explanations.

If challenge succeeds:

```text
DOWNGRADE
```

or:

```text
CONDITION
```

or:

```text
COMPETING
```

or:

```text
UNKNOWN/GAP
```

---

# 87. Causal Challenge Matrix

Target challenge questions:

```text
COULD B CAUSE A?

COULD C CAUSE BOTH?

COULD SELECTION CREATE THE PATTERN?

COULD MEASUREMENT CREATE THE PATTERN?

COULD FEEDBACK REVERSE DIRECTION?

COULD THE EFFECT EXIST ONLY IN THIS REGIME?

COULD SHARED PROVENANCE CREATE FALSE CONFIRMATION?

COULD THE MECHANISM BE WRONG?

COULD THE INTERVENTION HAVE CHANGED ANOTHER VARIABLE?

COULD ONE ASSUMPTION FLIP THE CONCLUSION?
```

---

# 88. Worked Semantics — Correlation

Given:

```text
A correlated with B
```

valid immediate conclusion:

```text
ASSOCIATED_WITH / CORRELATED_WITH
```

Invalid immediate conclusion:

```text
A CAUSES B
```

unless additional evidence licenses promotion.

---

# 89. Worked Semantics — Temporal Sequence

Given:

```text
A occurs
then
B occurs
```

valid:

```text
A PRECEDES B
```

Invalid without more support:

```text
A CAUSES B
```

---

# 90. Worked Semantics — Mechanism

Given:

```text
A
↓
proposed M
↓
B
```

and the mechanism is theoretically coherent but unvalidated:

```text
relation: CAUSAL_MODEL
epistemic_class: MODEL
```

not:

```text
VERIFIED
```

---

# 91. Worked Semantics — Confounder

Observed:

```text
A ↔ B
```

Possible:

```text
C → A
C → B
```

If `C` is plausible and unresolved:

```text
A → B
```

cannot be treated as verified.

Preserve:

```text
COMPETING
```

or:

```text
CONDITIONAL
```

as appropriate.

---

# 92. Worked Semantics — Intervention

Suppose an intervention changes `A` and then `B` changes.

Before concluding:

```text
A CAUSES B
```

check:

```text
ASSIGNMENT

INTERVENTION FIDELITY

OTHER VARIABLES CHANGED

MEASUREMENT

SELECTION

INTERFERENCE

REGIME

TIME
```

---

# 93. Worked Semantics — Cross-Regime Transfer

Suppose:

```text
A → B
```

is supported in:

```text
REGIME R1
```

The system is now in:

```text
REGIME R2
```

Correct:

```text
REVALIDATE
```

not automatic causal reuse.

---

# 94. Worked Semantics — Shared Provenance

Suppose three studies derive from the same underlying dataset.

Then:

```text
3 PUBLICATIONS
```

do not necessarily equal:

```text
3 INDEPENDENT DATA SOURCES
```

Causal confidence must reflect ancestry.

---

# 95. Worked Semantics — Structural Analogy

Suppose biological system `B` and computational system `C` share a feedback architecture.

Supported:

```text
B ANALOGOUS_TO C
```

Potentially supported:

```text
SHARED STRUCTURAL MODEL
```

Not established:

```text
SAME CAUSAL LAW
```

---

# 96. Worked Semantics — Prediction

Suppose model `M` predicts outcome `Y` from variable `X` with high accuracy.

Supported:

```text
X PREDICTS Y
```

Not automatically supported:

```text
X CAUSES Y
```

---

# 97. Worked Semantics — Dependency Failure

Suppose:

```text
CAUSAL_CLAIM_C
DEPENDS_ON
IDENTIFICATION_ASSUMPTION_A
```

If `A` fails:

```text
INVALIDATE C
```

or downgrade it to the strongest remaining supported class.

Do not invalidate unrelated claims.

---

# 98. Worked Semantics — Competing Direction

Evidence supports both:

```text
H1: A → B
```

and:

```text
H2: B → A
```

with no discriminating evidence.

Correct:

```text
COMPETING
```

not arbitrary direction selection.

---

# 99. Worked Semantics — Feedback

Suppose:

```text
A_t → B_t+1
B_t → A_t+1
```

A static statement:

```text
A causes B
```

may be incomplete.

The causal model SHOULD preserve bidirectional temporal feedback.

---

# 100. Worked Semantics — Threshold

Suppose evidence supports:

```text
A → B
```

only when:

```text
A > θ
```

The causal claim MUST preserve the threshold.

It MUST NOT be generalized to all `A`.

---

# 101. Worked Semantics — Heterogeneity

Suppose an average treatment effect is positive but effects vary across subgroups.

Valid:

```text
AVERAGE EFFECT POSITIVE
within declared population
```

Invalid:

```text
POSITIVE EFFECT FOR EVERY UNIT
```

unless separately established.

---

# 102. Worked Semantics — Missing Counterfactual

Observed:

```text
treated system improved
```

Without a credible counterfactual, possible explanations include:

```text
TREATMENT

TIME TREND

REGRESSION TO MEAN

EXTERNAL EVENT

SELECTION

MEASUREMENT CHANGE
```

Causal attribution remains limited.

---

# 103. Worked Semantics — Causal Decision

Suppose action `A` is recommended because:

```text
A → BENEFIT
```

but the causal premise is fragile.

The decision layer SHOULD expose:

```text
KNOWN FACT

CAUSAL INFERENCE

LOAD-BEARING ASSUMPTION

FALSIFIER

REVERSIBLE ACTION
```

rather than presenting the causal model as certainty.

---

# 104. Action Governance

Validation depth SHOULD increase with:

```text
IRREVERSIBLE COST

LEGAL EXPOSURE

FINANCIAL EXPOSURE

HEALTH / SAFETY EXPOSURE

INSTITUTIONAL IMPACT

LARGE DOWNSTREAM DEPENDENCY
```

When causal uncertainty is material, prefer staged and reversible action.

---

# 105. Reversibility

Under unresolved causal uncertainty:

```text
REVERSIBLE TEST
>
IRREVERSIBLE COMMITMENT
```

when expected information value and risk permit.

This is a governance preference, not a universal optimization theorem.

---

# 106. Causal Decision Sufficiency

Perfect causal knowledge is not always necessary for action.

A decision may be sufficient when:

```text
MATERIAL ALTERNATIVES CONSIDERED

DOWNSIDE BOUNDED

ACTION REVERSIBLE

EXPECTED INFORMATION GAIN POSITIVE

CRITICAL GAPS EXPOSED
```

But the causal claim itself must remain correctly classified.

---

# 107. Claim Sufficiency

A causal analysis may stop when the strongest decision-relevant conclusion has been established and remaining uncertainty cannot materially change the outcome.

Do not continue accumulating redundant evidence merely for completeness.

---

# 108. Gap Taxonomy

```text
CRITICAL

DECISION-RELEVANT

EXPLANATORY

COSMETIC
```

Priority:

```text
CRITICAL
>
DECISION-RELEVANT
>
EXPLANATORY
>
COSMETIC
```

---

# 109. Critical Gap — Native Canon

```yaml
gap:
  id: GAP_CAUSAL_INTEGRITY_NATIVE_CANON
  class: CRITICAL
  state: UNKNOWN/GAP

  description: >
    The substantive native-canon source defining the canonical
    Causal Integrity framework has not been established from
    the supplied placeholder alone.

  required:
    - verified_native_canon_source
    - provenance
    - version
    - lineage
```

---

# 110. Critical Gap — Executable Binding

```yaml
gap:
  id: GAP_CAUSAL_INTEGRITY_EXECUTABLE_BINDING
  class: CRITICAL
  state: UNKNOWN/GAP

  description: >
    No executable causal-integrity enforcement or causal
    inference binding has been established.
```

---

# 111. Critical Gap — Validation

```yaml
gap:
  id: GAP_CAUSAL_INTEGRITY_VALIDATION
  class: CRITICAL
  state: UNKNOWN/GAP

  description: >
    No artifact-specific executed validation receipt proving
    the Causal Integrity Canon has been established.
```

---

# 112. Critical Gap — Relation Registry

```yaml
gap:
  id: GAP_CAUSAL_RELATION_REGISTRY
  class: DECISION-RELEVANT
  state: UNKNOWN/GAP

  description: >
    Final native-canon definitions for the causal relation
    vocabulary and their promotion requirements remain
    unestablished.
```

---

# 113. Promotion Gates

Before promotion from placeholder to populated canon:

* [ ] substantive native-canon content recovered;
* [ ] provenance and lineage established;
* [ ] causal relation registry established;
* [ ] epistemic claim classes bound;
* [ ] scope schema bound;
* [ ] regime schema bound;
* [ ] causal provenance topology persisted;
* [ ] competing-hypothesis representation implemented;
* [ ] falsifier representation implemented;
* [ ] dependency invalidation implemented;
* [ ] confidence-ceiling behavior validated;
* [ ] causal-direction negative cases tested;
* [ ] confounding negative cases tested;
* [ ] scope leakage tested;
* [ ] regime shifts tested;
* [ ] correlated provenance tested;
* [ ] rollback basin demonstrated;
* [ ] artifact-specific validation receipt executed;
* [ ] critical UNKNOWN/GAP entries remain visible.

---

# 114. Negative Validation Matrix

Required target cases:

```text
CORRELATION PROMOTED TO CAUSATION

TEMPORAL ORDER PROMOTED TO CAUSATION

PREDICTION PROMOTED TO CAUSATION

STRUCTURAL ANALOGY PROMOTED TO CAUSATION

DEPENDENCY PROMOTED TO CAUSATION

UNRESOLVED CONFOUNDER IGNORED

REVERSE CAUSATION IGNORED

FEEDBACK COLLAPSED TO ONE DIRECTION

SHARED PROVENANCE COUNTED AS INDEPENDENT

STALE EVIDENCE REUSED

SCOPE LEAKAGE

REGIME LEAKAGE

CROSS-SCALE GENERALIZATION

CROSS-DOMAIN GENERALIZATION

MISSING FALSIFIER

MISSING PROVENANCE

MISSING VERSION

FAILED IDENTIFICATION ASSUMPTION

FAILED [[VALIDATION]] RECEIPT

UNKNOWN/GAP TREATED AS PASS
```

---

# 115. Mutation Discipline

For any consequential causal-canon mutation:

```text
ADMIT
↓
RESOLVE ARTIFACT + VERSION
↓
BIND SCOPE
↓
BIND REGIME
↓
CHECK AUTHORITY
↓
TYPE CLAIM
↓
RESOLVE PROVENANCE
↓
RESOLVE DEPENDENCIES
↓
CHECK COMPETING EXPLANATIONS
↓
CHECK FALSIFIERS
↓
PROPOSE
↓
VALIDATE
↓
COMMIT OR HOLD
↓
RECEIPT
```

---

# 116. Fail-Closed Rule

If any load-bearing causal field is unresolved:

```text
UNKNOWN/GAP
```

MUST NOT be interpreted as:

```text
PASS
```

For consequential operations, fail closed unless governance explicitly defines a safe reversible fallback.

---

# 117. Rollback Basin

Before consequential mutation preserve enough state to reverse:

```text
CLAIM PROMOTION

CLAIM DOWNGRADE

CAUSAL EDGE ADDITION

CAUSAL EDGE REMOVAL

IDENTIFICATION CHANGE

SCOPE CHANGE

REGIME CHANGE

CANONICAL PROMOTION
```

---

# 118. Repair Semantics

When a causal premise fails:

```text
FAILED PREMISE
↓
INVALIDATE DEPENDENT EDGES
↓
INVALIDATE DEPENDENT CONCLUSIONS
↓
PRESERVE UNAFFECTED GRAPH
↓
RECOMPUTE LOCAL CLOSURE
```

Do not recompute the entire system unless dependency ambiguity makes local repair unsafe.

---

# 119. Observability Boundary

Observability MAY report:

```text
CAUSAL CLAIM CREATED

CLAIM PROMOTED

CLAIM DOWNGRADED

CONFLICT DETECTED

FALSIFIER TRIGGERED

REGIME SHIFT DETECTED

PROVENANCE CORRELATION DETECTED
```

but:

```text
OBSERVABILITY
!=
AUTHORITY
```

A monitoring event cannot itself authorize canonical mutation.

---

# 120. Cross-Plane Bindings

Target:

```text
CAUSAL_INTEGRITY_CANON
        │
        ├─ GOVERNED_BY ─────> [[LAW_HIERARCHY]]
        │
        ├─ INDEXED_BY ──────> [[00_HOME]]
        │
        ├─ INDEXED_BY ──────> [[AMOS_RSCF_NODES]]
        │
        ├─ CROSSWALKED_BY ──> [[CANON_LAW_CROSSWALK]]
        │
        ├─ INTERACTS_WITH ──> KERNEL
        │
        ├─ CONTROLLED_BY ───> CONTROL_PLANE
        │
        ├─ OBSERVED_BY ─────> OBSERVABILITY
        │
        └─ RECOVERED_BY ────> OPERATIONS
```

References:

* 
* 
* 
* 
* 
* 
* 
* 

The `CROSSWALKED_BY` relation above is a **target relation** until independently established in native canon.

---

# 121. Validation Receipt Boundary

The placeholder references:

```text
[[ROUTING_POLICY_VALIDATION_RECEIPT]]

[[AUTHZ_ENGINE_VALIDATION_RECEIPT]]
```

These do not establish causal-integrity validation.

A dedicated artifact-specific receipt is required.

---

# 122. Target Validation Receipt

```yaml
validation_receipt:

  artifact_id:
    amos_01_canon_01_core_laws_causal_integrity_canon

  artifact_version:
    required

  executed_at:
    required

  validator:
    required

  tests:

    causal_typing:
      required

    correlation_firewall:
      required

    temporal_precedence_firewall:
      required

    prediction_firewall:
      required

    confounding:
      required

    reverse_causation:
      required

    feedback:
      required

    provenance_independence:
      required

    scope:
      required

    regime:
      required

    falsification:
      required

    selective_invalidation:
      required

    rollback:
      required

  result:
    PASS | FAIL | CONDITIONAL

  unresolved_gaps:
    - gap_ref
```

No executed receipt of this form is established by the supplied placeholder.

---

# 123. Causal Proof-State Transition

Target:

```text
SOURCE_CLAIM
↓
OBSERVED ASSOCIATION
↓
DERIVED RELATION
↓
CAUSAL MODEL
↓
CONDITIONAL CAUSAL CLAIM
↓
VALIDATED CAUSAL CLAIM
```

Promotion between states is not automatic.

Every transition requires evidence appropriate to the stronger state.

---

# 124. No Monotonic Promotion Assumption

Knowledge state can move backward.

Example:

```text
VALIDATED
↓
NEW CONFOUNDER DISCOVERED
↓
CONDITIONAL
```

or:

```text
CONDITIONAL
↓
REGIME SHIFT
↓
UNKNOWN/GAP
```

Downgrade is integrity preservation, not failure.

---

# 125. Causal State Machine

Target conceptual state machine:

```text
UNKNOWN/GAP
   ↓
SOURCE_CLAIM
   ↓
ASSOCIATION
   ↓
MODEL
   ↓
CONDITIONAL
   ↓
VERIFIED
```

with allowed backward transitions whenever dependencies fail.

Not every claim must traverse every state.

---

# 126. Causal Contradiction

Suppose:

```text
MODEL_A:
X → Y
```

and:

```text
MODEL_B:
X has no causal effect on Y
```

If they apply to the same:

```text
POPULATION
REGIME
TIME
INTERVENTION
OUTCOME DEFINITION
```

they may genuinely conflict.

If scopes differ, both may remain valid.

---

# 127. Contradiction Visibility

Unresolved causal contradiction MUST remain visible.

Do not average incompatible models into a synthetic compromise unless that synthesis itself has evidence.

```text
CONTRADICTION
!=
INVITATION TO INVENT CONSENSUS
```

---

# 128. Causal Model Selection

A model SHOULD NOT be preferred merely because it is:

```text
SIMPLER

MORE POPULAR

MORE ELEGANT

MORE RECENT

MORE AUTHORITATIVE-SOUNDING
```

Preference requires decision-relevant evidence, assumptions, predictive discrimination, causal identification, or governance criteria appropriate to the task.

---

# 129. Parsimony Boundary

Parsimony may be a model-selection consideration.

It is not a causal proof rule.

```text
SIMPLER MODEL
!=
TRUE CAUSAL MODEL
```

---

# 130. Authority Boundary

Expert or institutional authority may affect source reliability assessment.

It does not independently establish causation.

```text
AUTHORITY CLAIMS X→Y
```

remains:

```text
SOURCE_CLAIM
```

until evidence and provenance justify stronger classification.

---

# 131. Consensus Boundary

Consensus may indicate convergence of expert judgment.

But:

```text
CONSENSUS
!=
INDEPENDENT CAUSAL PROOF
```

The evidentiary topology beneath consensus remains relevant.

---

# 132. Replication Boundary

Replication strengthens causal confidence only to the extent that replications are sufficiently independent and applicable.

Shared:

```text
DATA

PIPELINE

ASSUMPTIONS

POPULATION

MEASUREMENT FAILURE
```

can create correlated replication.

---

# 133. External Validity

A causal effect established in one environment may not transfer.

Transfer SHOULD test:

```text
MECHANISM STABILITY

POPULATION DIFFERENCE

ENVIRONMENT DIFFERENCE

INTERACTION STRUCTURE

REGIME

TIME
```

before generalization.

---

# 134. Transportability State

Target classifications:

```text
TRANSFER_VALIDATED

TRANSFER_CONDITIONAL

TRANSFER_MODEL

TRANSFER_UNKNOWN
```

A causal effect can be internally valid yet externally uncertain.

---

# 135. Causal Uncertainty Vector

When material, causal uncertainty SHOULD be decomposed into:

```text
EVIDENCE UNCERTAINTY

MODEL UNCERTAINTY

SCOPE UNCERTAINTY

TEMPORAL UNCERTAINTY

CAUSAL-DIRECTION UNCERTAINTY

EXECUTION UNCERTAINTY

PROVENANCE-INDEPENDENCE UNCERTAINTY
```

Do not compress materially different uncertainty sources into one opaque score.

---

# 136. Decision-Relevant Uncertainty

Reasoning effort SHOULD prioritize uncertainty that can change:

```text
CLAIM CLASS

ACTION

RISK

SCOPE

REVERSIBILITY

GOVERNANCE REQUIREMENT
```

Low-impact uncertainty may remain unresolved.

---

# 137. Causal Action Ladder

Under uncertainty:

```text
OBSERVE
↓
LOW-COST TEST
↓
REVERSIBLE INTERVENTION
↓
LIMITED DEPLOYMENT
↓
BROADER DEPLOYMENT
↓
IRREVERSIBLE COMMITMENT
```

Validation burden rises with downstream consequence.

---

# 138. Causal Governance Invariant

Optimization MUST NOT weaken:

```text
CAUSAL TYPING

PROVENANCE

SCOPE

REGIME

CONTRADICTION VISIBILITY

FALSIFIABILITY

ROLLBACK

[[VALIDATION]]
```

A faster causal inference that silently removes these protections is a regression.

---

# 139. Anti-Regression Gate

A causal optimization is admissible only if it preserves or improves:

```text
FACTUAL SUPPORT

CAUSAL DISCIPLINE

SCOPE CORRECTNESS

REGIME CORRECTNESS

PROVENANCE RECOVERABILITY

CONTRADICTION VISIBILITY

SAFETY

EFFICIENCY

USER FIT
```

Otherwise:

```text
ROLL BACK
```

---

# 140. Current Supported Canonical Claim

From the supplied artifact itself, the strongest supported native statement is:

```text
AMOS OS reserves an ADD-ONLY canonical slot named
CAUSAL_INTEGRITY_CANON.md
within 01_CANON/01_CORE_LAWS.
```

Class:

```text
SOURCE_CLAIM
```

The supplied placeholder does **not** establish that the substantive causal rules defined in this expansion are already native canonical content.

They remain:

```text
AMOS_MODEL / TARGET CONTRACT
```

pending native-canon ingestion and validation.

---

# 141. Current Proof Capsule

```yaml
proof_capsule:

  id: PC_CAUSAL_INTEGRITY_CURRENT

  claim: >
    AMOS OS reserves a Canon-plane artifact named
    CAUSAL_INTEGRITY_CANON.md for the Causal Integrity
    framework family.

  claim_class: SOURCE_CLAIM

  evidence:
    - CAUSAL_INTEGRITY_CANON placeholder artifact

  provenance:
    - AMOS_corpus

  scope:
    system: AMOS_OS
    plane: 01_CANON
    segment: 01_CANON/01_CORE_LAWS

  dependencies:
    - AMOS_CANON_INGESTION_RULE

  competing_explanations: []

  falsifiers:
    - verified native manifest establishes otherwise
    - provenance establishes the artifact is not part of AMOS corpus

  confidence_ceiling:
    source_supported

  substantive_native_causal_canon_established:
    false

  executable_binding_established:
    false

  validation_established:
    false
```

---

# 142. Canonical Knowledge Capsule

**Class: AMOS_MODEL / SOURCE_CLAIM**

The **Causal Integrity Canon** is a reserved AMOS Core-Law artifact intended to govern disciplined causal reasoning.

Its target integrity firewall preserves distinctions among:

```text
ASSOCIATION

CORRELATION

TEMPORAL PRECEDENCE

DEPENDENCY

ENABLING CONDITION

NECESSITY

SUFFICIENCY

MECHANISM

MEDIATION

CONFOUNDING

FEEDBACK

INTERVENTION

CAUSAL EFFECT
```

The central target discipline is:

```text
NEVER PROMOTE
A RELATION
TO A STRONGER CAUSAL CLASS
THAN ITS EVIDENCE LICENSES
```

Causal conclusions remain bounded by:

```text
PROVENANCE

DEPENDENCIES

SCOPE

REGIME

TIME

MEASUREMENT

IDENTIFICATION ASSUMPTIONS

COMPETING EXPLANATIONS

FALSIFIERS

CONFIDENCE CEILING
```

Structural similarity, prediction, temporal order, dependency, popularity, repetition, or architectural coherence do not independently establish causation.

When competing causal models remain viable:

```text
PRESERVE COMPETING
```

When a load-bearing premise is unresolved:

```text
UNKNOWN/GAP != PASS
```

When a premise fails:

```text
INVALIDATE DEPENDENT DESCENDANTS ONLY
```

The substantive native Causal Integrity Canon, executable binding, and artifact-specific validation remain:

```text
UNKNOWN/GAP
```

until verified native-canon sources and validation receipts establish otherwise.

---

# 143. Final Integrity Rule

Until substantive native canon is recovered:

```text
DO NOT INVENT
MISSING CAUSAL LAW
```

Instead:

```text
PRESERVE PLACEHOLDER
+
PRESERVE PROVENANCE
+
PRESERVE VERSION
+
PRESERVE LINEAGE
+
TYPE RELATIONS CONSERVATIVELY
+
PRESERVE COMPETING HYPOTHESES
+
EXPOSE UNKNOWN/GAP
+
RETRIEVE NATIVE SOURCE
+
NORMALIZE
+
VALIDATE
+
PROMOTE WITH RECEIPTS
```

---

# 144. Canonical Invariants

```text
INTEGRITY > COMPLETENESS > FLUENCY > SPEED > TOKEN SAVINGS

PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

DOCUMENTED != ENFORCED

MODEL != OBSERVATION

SOURCE_CLAIM != VERIFIED

CANON_CANDIDATE != CANONICAL

CANONICAL != EMPIRICAL_TRUTH

ASSOCIATION != CAUSATION

CORRELATION != CAUSATION

TEMPORAL PRECEDENCE != CAUSATION

PREDICTION != CAUSATION

DEPENDENCY != CAUSATION

STRUCTURAL SIMILARITY != CAUSATION

ANALOGY != CAUSATION

MECHANISM MODEL != VERIFIED MECHANISM

ENABLING CONDITION != SUFFICIENT CAUSE

NECESSARY CONDITION != SUFFICIENT CONDITION

INTERVENTION != AUTOMATIC IDENTIFICATION

MULTIPLE DESCENDANTS != INDEPENDENT CONFIRMATION

NO CONTRADICTION FOUND != VERIFIED CAUSATION

REFERENCE != AUTHORITY

CENTRALITY != AUTHORITY

IMPLEMENTED != VALIDATED

CAPABILITY != AUTHORITY

AUTHORIZATION != COMMIT

PROPOSAL != COMMIT

LOGGED != APPROVED

UNKNOWN/GAP != PASS
```

---

00_ROOT_MOC|AMOS MOC

---

**Related:**  · 

---

RSCF-NODE

node_id: amos_01_canon_01_core_laws_causal_integrity_canon

node_type: canon

path: 01_CANON/01_CORE_LAWS/CAUSAL_INTEGRITY_CANON.md

origin_architect: Trang Phan

steward: Trang Phan

system: AMOS OS

claim_class: AMOS_MODEL

rscf_state: placeholder_expanded

canonical_status: UNKNOWN/GAP

implementation_status: NOT_ESTABLISHED

validation_status: NOT_ESTABLISHED

executable_binding: NOT_ESTABLISHED

native_causal_law_status: NOT_ESTABLISHED

causal_inference_engine_status: NOT_ESTABLISHED

RSCF-RELATIONS:

* INDEXED_BY: 

* INDEXED_BY: 

* GOVERNED_BY: 

* TARGET_CROSSWALKED_BY: 

* INTERACTS_WITH: 

* CONTROLLED_BY: 

* OBSERVED_BY: 

* RECOVERED_BY: 

---

**MOC:** 

---

**Origin Architect / Steward:** Trang Phan

**System:** AMOS OS

**Epistemic Class:** AMOS_MODEL

**Canonical Status:** UNKNOWN/GAP

**Substantive native causal canon:** NOT_ESTABLISHED

**Executable binding:** NOT_ESTABLISHED

**Validation:** NOT_ESTABLISHED

```
