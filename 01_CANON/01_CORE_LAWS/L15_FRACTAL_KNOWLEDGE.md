---
title: L15 FRACTAL KNOWLEDGE
type: fractal
source: 01_CANON/01_CORE_LAWS
tags:
  - canon
  - core_laws
  - fractal
  - fractal_knowledge
  - family_taxonomy
  - statistical_validation
  - generative_systems
  - constructive_trace
  - analogy_firewall
  - bridge_governance
  - epistemic_governance
  - canon/universe
rscf:
  state: SOURCE_CLAIM
  claim_class: CONDITIONAL
  provenance: AMOS_corpus
  scope: core_laws
  canonical_status: CONDITIONAL
  specification_status: PROPOSED_SPECIFICATION
  node_id: l15_fractal_knowledge
  node_type: note
---

# L15 Fractal Knowledge Laws

**STATUS:** PROPOSED_SPECIFICATION  
**epistemic_class:** AMOS_MODEL  
**canonical_status:** CONDITIONAL  
**updated:** 2026-08-26

---

# 0. Status

L15 defines the proposed AMOS governance layer for claims involving fractals, fractal families, scale structure, statistical heavy-tail families, recursive generators, self-similarity, constructive systems, and cross-domain structural analogy.

It replaces the prior placeholder with a structured specification governing:

- canonical fractal-family declaration,
- FR001–FR025 family identity,
- validation-method declaration,
- statistical fitting,
- parameter estimation,
- uncertainty reporting,
- lower-bound selection,
- alternative-model comparison,
- rejection of log-log visual inference,
- constructive rule traces,
- recursive generation,
- convergence evidence,
- visual-similarity rejection,
- structural analogy,
- isomorphism claims,
- semantic-transfer restrictions,
- bridge governance,
- scope and regime preservation,
- provenance of fractal claims,
- falsification,
- competing family hypotheses.

L15 remains:

```text
PROPOSED_SPECIFICATION
        │
        ▼
    AMOS_MODEL
        │
        ▼
    CONDITIONAL

until authoritative fractal canon validates, revises, supersedes, or rejects the proposed specification.

The central epistemic firewall is:

```text
PATTERN
≠
FRACTAL PROOF

VISUAL SIMILARITY
≠
CONSTRUCTIVE EQUIVALENCE

LOG-LOG LINEARITY
≠
POWER-LAW VALIDATION

STRUCTURAL RESEMBLANCE
≠
SEMANTIC ISOMORPHISM

ANALOGY
≠
CAUSATION
```

---

# 1. Governing Objective

L15 exists to prevent the word **fractal** from becoming an unrestricted metaphor or an inference shortcut.

A valid fractal claim must identify:

```text
WHAT FAMILY?

WHAT VALIDATION METHOD?

WHAT EVIDENCE?

WHAT SCALE / DOMAIN?

WHAT ALTERNATIVES?

WHAT WOULD FALSIFY IT?
```

Conceptually:

```text
FRACTAL CLAIM AUTHORITY
=
FAMILY SPECIFICITY
× VALIDATION QUALITY
× PROVENANCE
× SCOPE FIT
× ALTERNATIVE DISCRIMINATION
```

This is an AMOS conceptual model, not an empirical equation.

---

# 2. Core Fractal Knowledge Laws

```text
FK-1
FAMILY DECLARATION

FK-2
FIT BEFORE CLAIM

FK-3
CONSTRUCTIVE TRACE

FK-4
ANALOGY ≠ ISOMORPHISM
```

Unified:

```text
OBSERVED STRUCTURE
       ↓
DECLARE FAMILY
       ↓
DECLARE VALIDATION METHOD
       ↓
RUN FAMILY-APPROPRIATE TEST
       ↓
CHALLENGE ALTERNATIVES
       ↓
PRESERVE SCOPE
       ↓
CLASSIFY CLAIM
```

No step may be replaced merely by visual resemblance.

---

# 3. FK-1 — Family Declaration

**Law**

Every consequential fractal claim MUST identify:

1. its canonical fractal family,
2. its family identifier within the FR001–FR025 taxonomy,
3. the validation method appropriate to that family.

Conceptually:

```yaml
fractal_claim:
  claim_id: string

  family:
    canonical_id: FR001-FR025
    canonical_name: string

  validation:
    method: string

  evidence:
    references: []

  claim_class:
    VERIFIED |
    DERIVED |
    MODEL |
    CONDITIONAL |
    COMPETING |
    UNKNOWN
```

The exact FR001–FR025 mappings are not supplied by the L15 source itself.

Therefore:

```yaml
fractal_family_taxonomy:
  required: true
  family_range: FR001-FR025
  exact_mapping:
    status: GAP_IF_CANON_NOT_LOADED
```

AMOS MUST NOT invent missing family definitions.

---

# 4. Why Family Declaration Is Required

The term:

```text
FRACTAL
```

can refer to materially different structures.

Possible classes may involve:

* statistical scaling,
* geometric self-similarity,
* recursive construction,
* iterated function systems,
* L-systems,
* substitution systems,
* tilings,
* multifractal structure,
* scale-dependent measures,
* graph or network scaling,
* temporal scaling,
* other canonical FR families.

But L15 does **not** establish that these correspond to particular FR identifiers unless authoritative taxonomy does so.

Therefore:

```text
GENERIC "THIS IS FRACTAL"
```

is epistemically weaker than:

```text
THIS CLAIM TARGETS FAMILY FRxxx
AND IS TESTED BY METHOD M
```

---

# 5. Family-Specific Validation

Different families require different proof obligations.

Conceptually:

```text
FAMILY
  │
  ├── statistical
  │      ↓
  │   audited fit
  │
  ├── generative
  │      ↓
  │   constructive trace
  │
  ├── geometric
  │      ↓
  │   family-specific structural test
  │
  └── other canonical family
         ↓
      canonical validator
```

Therefore:

```text
ONE UNIVERSAL "FRACTAL TEST"
```

is rejected unless authoritative canon explicitly defines one.

---

# 6. Fractal Claim Schema

```yaml
fractal_claim:

  claim_id: string

  proposition: string

  epistemic_type:
    SOURCE_CLAIM |
    OBSERVATION |
    DERIVED |
    MODEL |
    DECISION |
    UNKNOWN

  family:
    id: FR001-FR025
    name: string|null
    taxonomy_version: string|null

  validation:
    method: string
    implementation: string|null
    result:
      PASS |
      FAIL |
      CONDITIONAL |
      INCONCLUSIVE

  provenance:
    sources: []
    ancestry: []

  scope:
    system: string|null
    scale_range: string|null
    environment: string|null
    regime: string|null

  alternatives: []

  falsifiers: []

  confidence_ceiling:
    VERIFIED |
    DERIVED |
    MODEL |
    CONDITIONAL |
    COMPETING |
    UNKNOWN
```

---

# 7. Family Taxonomy Versioning

Fractal family identity SHOULD be bound to a taxonomy version where relevant.

```yaml
family_reference:
  id: FR007
  taxonomy_version: string
  canonical_source: string
```

This prevents:

```text
FR007@taxonomy_V1
```

from silently becoming equivalent to:

```text
FR007@taxonomy_V2
```

if authoritative taxonomy changes.

---

# 8. Unknown Family

If a pattern appears fractal-like but cannot be assigned to a canonical family:

```yaml
family:
  id: UNKNOWN
```

The claim should remain:

```text
UNKNOWN
```

or:

```text
MODEL
```

depending on what is actually supported.

Do not fabricate the nearest FR identifier.

---

# 9. Competing Family Assignment

A structure may plausibly fit multiple families.

Example:

```text
OBSERVATION O
     │
     ├── H1: FR00x
     ├── H2: FR00y
     └── H3: non-fractal alternative
```

If available evidence cannot discriminate:

```yaml
claim_class: COMPETING
```

rather than forcing a single family.

---

# 10. Family Declaration Invariant

```text
NO FAMILY
   ↓
NO FAMILY-SPECIFIC VALIDATION
   ↓
NO STRONG FRACTAL CLAIM
```

Thus:

> **Classification precedes validation, but classification itself remains falsifiable.**

---

# 11. FK-2 — Fit Before Claim

**Law**

Statistical fractal families require audited fits.

The source explicitly requires:

```text
MLE alpha
+
confidence interval
+
declared x_min
+
alternative-model duel
```

and explicitly rejects:

```text
LOG-LOG EYEBALLING
```

as sufficient evidence.

---

# 12. Statistical Claim Pipeline

```text
DATA
 ↓
DATA QUALITY CHECK
 ↓
DECLARE CANDIDATE FAMILY
 ↓
DECLARE x_min
 ↓
FIT PARAMETERS
 ↓
ESTIMATE alpha
 ↓
COMPUTE UNCERTAINTY / CI
 ↓
GOODNESS-OF-FIT
 ↓
ALTERNATIVE-MODEL DUEL
 ↓
SENSITIVITY ANALYSIS
 ↓
CLASSIFY RESULT
```

A visually straight line on log-log axes cannot replace this process.

---

# 13. Power-Law Candidate Model

Where the canonical family is a power-law-type statistical model, a conceptual form may be:

```text
p(x) ∝ x^(-α)
```

for:

```text
x ≥ x_min
```

The exact continuous/discrete likelihood formulation depends on the data and canonical validator.

L15 does not authorize one universal estimator for every statistical family.

---

# 14. Alpha Estimation

The source requires:

```text
MLE alpha
```

for statistical families where alpha is the relevant parameter.

Conceptually:

```yaml
fit:
  estimator: MLE
  parameter:
    alpha:
      estimate: number
      confidence_interval:
        lower: number
        upper: number
```

The estimator MUST correspond to the actual model and data type.

Do not apply a continuous estimator blindly to discrete data or vice versa.

---

# 15. Confidence Interval Requirement

A point estimate alone is insufficient.

Invalid minimal representation:

```yaml
alpha: 2.31
```

Preferred:

```yaml
alpha:
  estimate: 2.31
  confidence_interval:
    level: 0.95
    lower: value
    upper: value
```

The numerical interval must come from the actual fitted data.

AMOS must never fabricate CI values.

---

# 16. x_min Declaration

The lower bound:

```text
x_min
```

defines the region over which the candidate scaling law is asserted.

Therefore it is load-bearing.

Conceptually:

```yaml
fit_domain:
  x_min:
    value: number
    selection_method: string

  x_max:
    value: number|null
```

A fit that silently chooses its favorable scaling region is not adequately auditable.

---

# 17. x_min Sensitivity

Because the conclusion may depend strongly on `x_min`, L15 requires sensitivity awareness.

Conceptually:

```text
x_min - δ
   ↓
FIT

x_min
   ↓
FIT

x_min + δ
   ↓
FIT
```

If the family conclusion flips under small plausible changes:

```yaml
robustness: FRAGILE
claim_class: CONDITIONAL
```

---

# 18. Log-Log Eyeballing Rejection

A common weak inference is:

```text
PLOT DATA ON LOG-LOG AXES
         ↓
LOOKS APPROXIMATELY STRAIGHT
         ↓
DECLARE POWER LAW
```

L15 rejects this.

Formally:

```text
APPARENT LINEARITY
ON LOG-LOG PLOT
≠
VALIDATED POWER-LAW FIT
```

because alternative distributions can produce visually similar regions.

---

# 19. Alternative-Model Duel

A statistical family must be challenged against credible alternatives.

Conceptually:

```text
CANDIDATE FRACTAL MODEL F
          │
          ├── versus A1
          ├── versus A2
          ├── versus A3
          └── versus A_n
```

The exact alternatives depend on family and domain.

L15 source does not enumerate the canonical alternative set.

Therefore:

```yaml
alternative_model_set:
  status: FAMILY_DEPENDENT
  exact_required_models: GAP_IF_CANON_NOT_LOADED
```

---

# 20. Alternative Comparison Record

```yaml
model_duel:

  candidate:
    family_id: FRxxx
    model: string

  alternative:
    model: string

  comparison_method:
    string

  result:
    candidate_preferred |
    alternative_preferred |
    indistinguishable |
    inconclusive

  uncertainty:
    string|null
```

---

# 21. Competing Statistical Models

If:

```text
POWER LAW
```

and:

```text
ALTERNATIVE MODEL
```

fit comparably well, the correct state is:

```yaml
claim_class: COMPETING
```

not:

```yaml
claim_class: VERIFIED
```

The cheapest high-information discriminating test should be preferred over accumulating redundant plots.

---

# 22. Statistical Provenance

Every audited fit SHOULD preserve:

```yaml
statistical_provenance:

  dataset:
    id: string
    version: string|null
    hash: string|null

  preprocessing:
    operations: []

  sample:
    n: integer|null

  fitting:
    method: string
    implementation: string|null
    software_version: string|null

  parameters:
    x_min: number|null
    alpha: number|null

  uncertainty:
    method: string|null

  alternatives:
    tested: []

  timestamp:
    string|null
```

This allows later reconstruction.

---

# 23. Fit Reproducibility

A statistical fractal claim SHOULD be reproducible from:

```text
DATA
+
PREPROCESSING
+
MODEL
+
PARAMETERS
+
FIT METHOD
+
ALTERNATIVE TESTS
```

If any load-bearing component is unavailable:

```yaml
reproducibility:
  status: PARTIAL|UNKNOWN
```

and confidence must reflect that gap.

---

# 24. Statistical Scope

A validated statistical fit applies only to its tested domain.

```yaml
fit_scope:
  population: string|null
  sample: string|null
  x_min: number|null
  x_max: number|null
  time_window: string|null
  environment: string|null
```

Do not infer:

```text
POWER LAW IN RANGE R
```

therefore:

```text
POWER LAW AT ALL SCALES
```

unless independently established.

---

# 25. Finite-Range Scaling

Observed scaling over a finite range must remain explicitly finite-range.

```text
SCALING OBSERVED
FROM a TO b
```

does not imply:

```text
SCALE FREE
FROM 0 TO ∞
```

Thus:

```yaml
scale_claim:
  observed_range:
    lower: a
    upper: b
  extrapolation:
    authorized: false
```

unless separately validated.

---

# 26. Sample-Size Sensitivity

Small samples may produce unstable apparent scaling.

Conceptually:

```text
N SMALL
  ↓
PARAMETER UNCERTAINTY ↑
MODEL DISCRIMINATION ↓
```

Therefore sample adequacy should be considered in confidence classification.

L15 does not specify a universal minimum sample size.

---

# 27. Preprocessing Sensitivity

A fractal fit may depend on:

* filtering,
* binning,
* thresholding,
* aggregation,
* missing-data treatment,
* temporal resolution,
* normalization.

Therefore:

```text
FIT(DATA)
```

and:

```text
FIT(PREPROCESSED DATA)
```

must not be assumed equivalent.

Load-bearing preprocessing should be recorded.

---

# 28. Statistical Failure Conditions

A statistical family claim should be downgraded when:

```text
FIT FAILS
OR
CI IS TOO BROAD FOR THE CLAIM
OR
x_min IS UNSTABLE
OR
ALTERNATIVE MODEL WINS
OR
ALTERNATIVES ARE INDISTINGUISHABLE
OR
DATA PROVENANCE FAILS
OR
RESULT DEPENDS ON UNDISCLOSED PREPROCESSING
```

Possible outcomes:

```text
VERIFIED
DERIVED
CONDITIONAL
COMPETING
UNKNOWN
```

using the weakest accurate class.

---

# 29. FK-3 — Constructive Trace

**Law**

Generative fractal families such as:

```text
IFS
L-SYSTEM
TILING
```

require:

```text
RULE TRACE
+
CONVERGENCE EVIDENCE
```

not visual similarity.

The source names these examples explicitly but does not claim they exhaust all generative FR families.

---

# 30. Generative Validation Pipeline

```text
CLAIMED GENERATIVE FAMILY
          ↓
DECLARE GENERATOR
          ↓
DECLARE INITIAL STATE
          ↓
DECLARE RULES
          ↓
TRACE ITERATIONS
          ↓
VERIFY RULE APPLICATION
          ↓
TEST CONVERGENCE / LIMIT BEHAVIOR
          ↓
COMPARE GENERATED STRUCTURE
          ↓
CLASSIFY CLAIM
```

---

# 31. Constructive Proof Principle

For a generative family, evidence should answer:

```text
CAN THE CLAIMED OBJECT
ACTUALLY BE GENERATED
BY THE CLAIMED RULES?
```

This is stronger than:

```text
DOES IT LOOK SIMILAR?
```

Therefore:

```text
VISUAL MATCH
≠
CONSTRUCTIVE TRACE
```

---

# 32. Generator Schema

```yaml
fractal_generator:

  family:
    id: FRxxx
    type:
      IFS |
      L_SYSTEM |
      TILING |
      OTHER_CANONICAL

  initial_state:
    description: string

  rules:
    - rule_id: string
      definition: string

  iteration:
    count: integer|null

  termination:
    condition: string|null

  convergence:
    method: string|null
    evidence: []

  output:
    artifact: string|null

  provenance:
    source: string|null
```

---

# 33. Rule Trace

A constructive trace SHOULD preserve the sequence:

```text
S0
 ↓ R1
S1
 ↓ R2
S2
 ↓ R3
S3
 ...
 ↓
Sn
```

or the appropriate recursive structure.

Conceptually:

```yaml
trace:
  - step: 0
    state: S0

  - step: 1
    rule: R1
    state: S1

  - step: 2
    rule: R2
    state: S2
```

The exact representation depends on the generative family.

---

# 34. Deterministic Generators

For deterministic rules:

```text
S_n + R
→ S_(n+1)
```

the trace should be reproducible from:

```text
INITIAL STATE
+
RULE SET
+
ITERATION ORDER
+
PARAMETERS
```

If the claimed output cannot be reconstructed:

```yaml
constructive_validation:
  status: FAIL
```

or:

```yaml
status: UNKNOWN
```

if evidence is incomplete.

---

# 35. Stochastic Generators

If a canonical generative family contains stochastic rules, reproducibility may require:

```yaml
stochastic_trace:
  distribution_parameters: []
  random_seed: string|null
  sampling_method: string|null
  realization_id: string|null
```

However, stochastic family semantics are not supplied in the source.

Therefore this remains a generic AMOS_MODEL extension rather than recovered fractal canon.

---

# 36. IFS Validation

For an iterated-function-system-type claim, the conceptual proof obligation includes:

```text
DECLARE MAPS
+
DECLARE PARAMETERS
+
DECLARE ITERATION
+
SHOW GENERATED TRAJECTORY / SET
+
PROVIDE CONVERGENCE EVIDENCE
```

A visually similar object without the map trace remains:

```text
MODEL / ANALOGY
```

not a validated IFS identification.

---

# 37. L-System Validation

For an L-system-type claim, conceptually preserve:

```yaml
l_system:
  alphabet: []
  axiom: string
  production_rules: []
  iterations: integer
  interpretation_rules: []
```

Then:

```text
AXIOM
 ↓
REWRITE 1
 ↓
REWRITE 2
 ↓
...
 ↓
GENERATED STRUCTURE
```

The resulting object must be linked to the actual rewrite trace.

---

# 38. Tiling Validation

For a generative tiling claim, evidence should preserve the relevant canonical rules, such as:

```text
TILE TYPES
+
MATCHING / SUBSTITUTION RULES
+
ITERATION OR CONSTRUCTION
+
RESULTING CONFIGURATION
```

Exact canonical requirements depend on the relevant FR family and must not be invented.

---

# 39. Convergence Evidence

FK-3 requires convergence evidence.

Conceptually:

```yaml
convergence:
  target: string
  metric: string
  sequence: []
  tolerance: number|null
  result:
    CONVERGED |
    NOT_CONVERGED |
    INCONCLUSIVE
```

The appropriate notion of convergence is family-dependent.

Examples may include:

* geometric convergence,
* measure convergence,
* iterative stabilization,
* invariant-set convergence,
* substitution convergence.

But the authoritative family validator controls which one applies.

---

# 40. Finite Approximation vs Limit Object

A finite generated approximation:

```text
S_n
```

must not silently be identified with the mathematical limit:

```text
S_∞
```

unless convergence has been established.

Thus:

```text
FINITE ITERATION
≠
PROOF OF LIMIT OBJECT
```

---

# 41. Visual Similarity Firewall

A pattern may visually resemble a canonical fractal without sharing its generating mechanism.

```text
OBJECT A
≈ visually ≈
OBJECT B
```

does not imply:

```text
GENERATOR(A)
=
GENERATOR(B)
```

nor:

```text
FAMILY(A)
=
FAMILY(B)
```

Therefore visual resemblance can generate a hypothesis but not complete the validation.

---

# 42. Constructive Provenance

A generative claim SHOULD preserve:

```yaml
constructive_provenance:

  generator_id: string

  rule_version: string|null

  initial_state_hash: string|null

  rule_set_hash: string|null

  implementation_version: string|null

  trace_hash: string|null

  output_hash: string|null

  validation_timestamp: string|null
```

This enables later audit of whether the output actually came from the claimed generator.

---

# 43. Rule Mutation

If a generator changes:

```text
RULESET R1
   ↓
MUTATION
   ↓
RULESET R2
```

claims validated under `R1` do not automatically transfer to `R2`.

```text
CLAIM@R1
≠
CLAIM@R2
```

unless invariant under the change and independently demonstrated.

---

# 44. Generative Failure Conditions

A generative fractal claim fails or downgrades when:

```text
RULES UNAVAILABLE
OR
TRACE CANNOT BE REPRODUCED
OR
OUTPUT DOES NOT FOLLOW RULES
OR
CONVERGENCE FAILS
OR
CONVERGENCE IS UNKNOWN
OR
ONLY VISUAL SIMILARITY EXISTS
```

---

# 45. FK-4 — Analogy ≠ Isomorphism

**Law**

Structural resemblance never licenses semantic transfer without bridge governance.

This creates a hard firewall:

```text
A RESEMBLES B
```

does not entail:

```text
A IS B
```

and does not entail:

```text
PROPERTY P OF A
MUST HOLD FOR B
```

---

# 46. Analogy Hierarchy

Conceptually:

```text
VISUAL SIMILARITY
        ↓
STRUCTURAL RESEMBLANCE
        ↓
FORMAL CORRESPONDENCE
        ↓
ISOMORPHISM
        ↓
SEMANTIC TRANSFER
```

Each arrow requires additional evidence.

No stage may be skipped by rhetoric.

---

# 47. Visual Similarity

Weakest form:

```text
A looks like B
```

Classification:

```yaml
relation: VISUAL_SIMILARITY
epistemic_class: MODEL
```

This supports hypothesis generation, not semantic transfer.

---

# 48. Structural Resemblance

A stronger statement:

```text
A and B share structural feature S
```

may support:

```yaml
relation: STRUCTURAL_RESEMBLANCE
```

but still does not establish:

```text
ISOMORPHISM
```

---

# 49. Formal Isomorphism

An isomorphism claim requires a formally specified mapping preserving the relevant structure.

Conceptually:

```text
f : A → B
```

with preservation conditions appropriate to the structure.

A valid isomorphism claim requires more than superficial similarity.

The exact mathematical preservation rules depend on the structures involved.

---

# 50. Semantic Transfer

Even formal structural equivalence does not automatically license transfer of every domain meaning.

For example:

```text
STRUCTURE A
≅
STRUCTURE B
```

does not necessarily imply:

```text
SEMANTICS(A)
=
SEMANTICS(B)
```

because semantics may depend on:

* interpretation,
* measurement,
* causal mechanism,
* physical substrate,
* scale,
* regime,
* boundary conditions,
* domain ontology.

---

# 51. Bridge Governance

Semantic transfer requires an explicit bridge.

Conceptually:

```yaml
bridge:

  source_domain: A

  target_domain: B

  mapped_structure:
    source: string
    target: string

  mapping:
    definition: string

  preserved_properties: []

  non_preserved_properties: []

  assumptions: []

  scope: string

  validation:
    method: string
    evidence: []

  falsifiers: []
```

Without this bridge:

```text
SEMANTIC TRANSFER
=
UNLICENSED
```

---

# 52. Bridge Proof Obligations

A bridge should answer:

```text
WHAT EXACTLY MAPS?

WHAT DOES NOT MAP?

WHY SHOULD THE MAPPING PRESERVE THIS PROPERTY?

AT WHAT SCALE?

IN WHAT REGIME?

UNDER WHAT ASSUMPTIONS?

WHAT WOULD BREAK THE MAPPING?
```

If these are unresolved, the cross-domain statement remains:

```text
MODEL
```

or:

```text
CONDITIONAL
```

---

# 53. Cross-Domain Fractal Analogy

Suppose:

```text
BIOLOGICAL NETWORK
```

resembles:

```text
COMPUTATIONAL NETWORK
```

in some scaling property.

That alone does not prove:

```text
same causal mechanism
same semantics
same optimization principle
same dynamics
same governance law
```

The only licensed conclusion may be:

```text
STRUCTURAL RESEMBLANCE UNDER METRIC M
```

within the observed scope.

---

# 54. Cross-Scale Transfer

A fractal claim at one scale does not automatically license another scale.

```text
MICRO SCALE
     ↓
structural pattern
```

does not automatically imply:

```text
MACRO SCALE
     ↓
same law
```

even when self-similarity is hypothesized.

Cross-scale invariance must be tested.

---

# 55. Causal Firewall

Fractal structure is not itself a causal explanation.

```text
OBSERVED SCALE STRUCTURE
```

does not imply:

```text
CAUSE = FRACTALITY
```

Likewise:

```text
A AND B SHARE FRACTAL DIMENSION
```

does not imply:

```text
A AND B SHARE GENERATIVE CAUSE
```

The causal evidence must be independently typed.

---

# 56. Fractal Dimension Firewall

Even where two objects share a measured fractal dimension:

```text
D(A) ≈ D(B)
```

this alone does not establish:

```text
A ≅ B
```

or:

```text
GENERATOR(A) = GENERATOR(B)
```

or:

```text
SEMANTICS(A) = SEMANTICS(B)
```

A scalar descriptor cannot carry the full structural or semantic identity.

---

# 57. Metric Dependence

Fractal measurements may depend on:

* metric,
* estimator,
* scale range,
* resolution,
* sampling,
* embedding,
* preprocessing.

Therefore:

```yaml
fractal_measurement:
  metric: string
  estimator: string
  scale_range: string
  resolution: string|null
  preprocessing: []
```

should accompany consequential claims where relevant.

---

# 58. Measurement Method Preservation

If:

```text
D1
```

was estimated using method `M1` and:

```text
D2
```

using method `M2`, direct comparison may require calibration.

Thus:

```text
SAME LABEL
≠
SAME MEASUREMENT PROCESS
```

Measurement provenance is part of scope.

---

# 59. Scope Envelope

Every consequential fractal claim SHOULD inherit:

```yaml
scope:

  system: string|null

  population: string|null

  environment: string|null

  scale:
    lower: string|null
    upper: string|null

  time:
    start: string|null
    end: string|null

  regime: string|null

  measurement_method: string|null

  assumptions: []
```

No silent generalization outside this envelope.

---

# 60. Regime Firewall

A fractal property observed in regime `R1` may fail in regime `R2`.

```text
SYSTEM
  │
  ├── R1 → scaling family F
  │
  └── R2 → scaling family G
```

Therefore:

```text
F@R1
```

cannot silently become:

```text
F@ALL_REGIMES
```

---

# 61. Scale Break Detection

A system may show different behavior at different scales.

```text
SMALL SCALE
    ↓
FAMILY F1

MID SCALE
    ↓
FAMILY F2

LARGE SCALE
    ↓
NON-FRACTAL
```

A single-family claim across all scales would be invalid.

Therefore scale breaks should be explicitly searched for where material.

---

# 62. Fractal Claim Provenance

```yaml
fractal_provenance:

  claim_id: string

  source:
    id: string
    type:
      SOURCE_CLAIM |
      OBSERVATION |
      DERIVED |
      MODEL

  dataset:
    id: string|null
    version: string|null

  family_taxonomy:
    version: string|null

  validation:
    method: string
    implementation: string|null

  transformations: []

  dependencies: []

  timestamp: string|null
```

---

# 63. Descendant Repetition

Suppose one paper claims a fractal pattern and ten later documents repeat it.

```text
SOURCE S
   │
   ├── D1
   ├── D2
   ├── D3
   └── ...
```

This is not ten independent validations.

L15 inherits the provenance rule:

```text
REPEATED FRACTAL CLAIMS
FROM SHARED ANCESTRY
≠
INDEPENDENT CONFIRMATION
```

---

# 64. Family Claim Confidence Ceiling

Conceptually:

```text
C_fractal
≤
min(
  C_family_identification,
  C_data,
  C_validation_method,
  C_fit_or_trace,
  C_alternative_discrimination,
  C_scope,
  C_provenance
)
```

If any load-bearing component is `UNKNOWN`, the final claim cannot exceed that limitation without independent validation.

---

# 65. Statistical Proof Capsule

```yaml
statistical_fractal_proof_capsule:

  claim:
    text: string
    class:
      VERIFIED |
      DERIVED |
      MODEL |
      CONDITIONAL |
      COMPETING |
      UNKNOWN

  family:
    id: FRxxx
    taxonomy_version: string|null

  dataset:
    id: string
    version: string|null

  fit:
    method: MLE
    alpha:
      estimate: number|null
      confidence_interval:
        lower: number|null
        upper: number|null

    x_min:
      value: number|null
      method: string|null

  alternatives:
    - model: string
      comparison_result: string

  scope:
    scale_range: string|null
    regime: string|null

  provenance:
    roots: []

  falsifiers: []

  confidence_ceiling:
    string
```

---

# 66. Constructive Proof Capsule

```yaml
constructive_fractal_proof_capsule:

  claim:
    text: string
    class:
      VERIFIED |
      DERIVED |
      MODEL |
      CONDITIONAL |
      COMPETING |
      UNKNOWN

  family:
    id: FRxxx
    type:
      IFS |
      L_SYSTEM |
      TILING |
      OTHER

  generator:
    initial_state: string
    rules: []
    parameters: []

  trace:
    available: true|false
    steps: []

  convergence:
    method: string|null
    result:
      PASS |
      FAIL |
      INCONCLUSIVE

  provenance:
    roots: []

  scope:
    string|null

  falsifiers: []

  confidence_ceiling:
    string
```

---

# 67. Analogy Proof Capsule

```yaml
fractal_analogy_proof_capsule:

  claim:
    text: string

  relation:
    VISUAL_SIMILARITY |
    STRUCTURAL_RESEMBLANCE |
    FORMAL_MAPPING |
    ISOMORPHISM |
    SEMANTIC_TRANSFER

  source_domain:
    string

  target_domain:
    string

  bridge:
    defined: true|false

  preserved_properties: []

  non_preserved_properties: []

  assumptions: []

  scope:
    string|null

  causal_transfer:
    licensed: false

  semantic_transfer:
    licensed: true|false|conditional

  falsifiers: []

  claim_class:
    MODEL |
    CONDITIONAL |
    DERIVED |
    VERIFIED |
    UNKNOWN
```

---

# 68. Validation Method Registry

Conceptually:

```yaml
fractal_validation_registry:

  FR001:
    family_name: GAP
    validator: GAP

  FR002:
    family_name: GAP
    validator: GAP

  FR003:
    family_name: GAP
    validator: GAP

  # ...

  FR025:
    family_name: GAP
    validator: GAP
```

This intentionally preserves the missing taxonomy.

The L15 source establishes the existence of:

```text
FR001–FR025
```

but does not supply the mapping.

Filling these entries without authoritative fractal canon would violate anti-fabrication.

---

# 69. Family Validator Interface

```python
class FractalFamilyValidator:

    family_id: str

    def validate(self, claim, evidence):
        raise NotImplementedError
```

Conceptually:

```python
def validate_fractal_claim(claim, evidence):
    family = require_family(claim)

    validator = registry.get(family)

    if validator is None:
        return UNKNOWN

    return validator.validate(
        claim,
        evidence
    )
```

Semantic pseudocode only.

---

# 70. Statistical Validator Interface

```python
class StatisticalFractalValidator:

    def validate(self, data, model):

        x_min = declare_x_min(data, model)

        fit = mle_fit(
            data=data,
            model=model,
            x_min=x_min
        )

        uncertainty = confidence_interval(fit)

        alternatives = duel_alternative_models(
            data=data,
            candidate=model,
            x_min=x_min
        )

        sensitivity = test_sensitivity(
            fit,
            x_min
        )

        return classify(
            fit=fit,
            uncertainty=uncertainty,
            alternatives=alternatives,
            sensitivity=sensitivity
        )
```

This encodes FK-2 semantics without claiming one implementation fits every FR family.

---

# 71. Constructive Validator Interface

```python
class ConstructiveFractalValidator:

    def validate(self, generator, claimed_output):

        trace = execute_rules(generator)

        if not trace.valid:
            return FAIL

        convergence = test_convergence(
            trace,
            generator
        )

        if convergence is UNKNOWN:
            return CONDITIONAL

        if not matches_claim(
            trace,
            claimed_output
        ):
            return FAIL

        return PASS
```

---

# 72. Bridge Validator Interface

```python
class StructuralBridgeValidator:

    def validate(self, source, target, bridge):

        if bridge is None:
            return MODEL

        if not mapping_defined(bridge):
            return CONDITIONAL

        if not preserved_properties_verified(bridge):
            return CONDITIONAL

        if scope_leak_detected(bridge):
            return FAIL

        return supported_claim_class(bridge)
```

---

# 73. Fractal Claim State Machine

```text
OBSERVED PATTERN
      ↓
HYPOTHESIS
      ↓
FAMILY DECLARED
      ↓
VALIDATOR DECLARED
      ↓
EVIDENCE TESTED
      ↓
ALTERNATIVES CHALLENGED
      ↓
      ├── PASS
      │     ↓
      │  SUPPORTED
      │
      ├── AMBIGUOUS
      │     ↓
      │  COMPETING
      │
      ├── INSUFFICIENT
      │     ↓
      │  CONDITIONAL / UNKNOWN
      │
      └── FAIL
            ↓
         INVALIDATE
```

---

# 74. Statistical State Machine

```text
DATA
 ↓
CANDIDATE FAMILY
 ↓
x_min
 ↓
MLE
 ↓
CI
 ↓
GOODNESS OF FIT
 ↓
ALTERNATIVE DUEL
 ↓
 ├── candidate clearly supported
 │       ↓
 │   SUPPORTED
 │
 ├── alternatives comparable
 │       ↓
 │   COMPETING
 │
 ├── fit unstable
 │       ↓
 │   CONDITIONAL
 │
 └── candidate rejected
         ↓
      INVALID
```

---

# 75. Constructive State Machine

```text
VISUAL CANDIDATE
      ↓
DECLARE GENERATOR
      ↓
RULE TRACE
      ↓
TRACE VALID?
  ├── NO → FAIL
  └── YES
       ↓
CONVERGENCE EVIDENCE
       ↓
CONVERGED?
  ├── NO → FAIL
  ├── UNKNOWN → CONDITIONAL
  └── YES
       ↓
OUTPUT MATCH?
  ├── NO → FAIL
  └── YES → SUPPORTED
```

---

# 76. Analogy State Machine

```text
RESEMBLANCE
    ↓
STRUCTURAL FEATURE IDENTIFIED?
    ├── NO → VISUAL ANALOGY
    └── YES
          ↓
FORMAL MAPPING?
    ├── NO → STRUCTURAL MODEL
    └── YES
          ↓
PRESERVATION PROVED?
    ├── NO → CONDITIONAL
    └── YES
          ↓
ISOMORPHISM IN DECLARED STRUCTURE
          ↓
SEMANTIC BRIDGE?
    ├── NO → NO SEMANTIC TRANSFER
    └── YES
          ↓
VALIDATE BRIDGE
```

---

# 77. Adversarial Validation

For a consequential fractal claim, first construct the strongest supported version.

Then challenge it through a genuinely different path.

For statistical claims:

```text
Could another distribution explain the data?

Is x_min cherry-picked?

Is alpha unstable?

Is the confidence interval broad?

Is the sample too small?

Did preprocessing create the apparent scaling?

Is the scaling range too narrow?

Are sources actually independent?
```

For constructive claims:

```text
Can the output actually be regenerated?

Were the stated rules really used?

Does convergence hold?

Could another generator produce the same appearance?

Is the trace complete?
```

For analogy claims:

```text
What exactly is preserved?

What fails to map?

Is semantic transfer being smuggled through structural similarity?

Is causation being inferred from shape?

Does the mapping survive regime or scale changes?
```

---

# 78. Cheapest Discriminating Test

When two family hypotheses compete:

```text
H1: family F1
H2: family F2
```

prefer:

```text
TEST T
```

that maximizes discrimination between `H1` and `H2`.

Do not simply accumulate more evidence that both hypotheses already predict.

Conceptually:

```text
VALUE(T)
≈
EXPECTED REDUCTION
IN DECISION-RELEVANT UNCERTAINTY
```

This is an AMOS reasoning heuristic, not an empirical formula.

---

# 79. Fractal Sensitivity

A consequential claim should identify the smallest assumption capable of flipping its class.

For statistical models this may be:

```text
x_min
alpha uncertainty
sample window
preprocessing
alternative family
```

For constructive systems:

```text
rule parameter
initial condition
iteration semantics
convergence criterion
```

For analogy:

```text
bridge assumption
preserved property
scale boundary
regime condition
```

Fragile results should remain:

```text
CONDITIONAL
```

---

# 80. Fractal Uncertainty Vector

```yaml
fractal_uncertainty:

  evidence:
    question:
      Is the underlying observation reliable?

  family:
    question:
      Is the canonical family assignment correct?

  model:
    question:
      Is the fitted or constructive model adequate?

  scope:
    question:
      Over what scales and environments does it apply?

  temporal:
    question:
      Does the structure persist over time?

  causal:
    question:
      Does the fractal structure license any causal claim?

  provenance:
    question:
      Are confirmations independently sourced?

  bridge:
    question:
      Is cross-domain semantic transfer valid?
```

These dimensions should not be collapsed into one confidence number when the distinction matters.

---

# 81. Fractal Knowledge and Memory

Validated fractal knowledge stored in memory SHOULD preserve:

```yaml
fractal_memory:

  family_id: FRxxx

  taxonomy_version: string|null

  validation_method: string

  evidence_refs: []

  fit_or_trace:
    reference: string|null

  scope:
    scale_range: string|null
    regime: string|null

  alternatives: []

  provenance_roots: []

  freshness:
    state: string

  falsifiers: []
```

A remembered family assignment is not permanently authoritative.

If taxonomy or evidence changes:

```text
REVALIDATE
```

---

# 82. Fractal Knowledge Harvest

```text
RAW PATTERN
    ↓
OBSERVATION
    ↓
FAMILY HYPOTHESIS
    ↓
VALIDATION
    ↓
PROVENANCED RESULT
    ↓
VALIDATED KNOWLEDGE
    ↓
PERSISTENCE
```

Do not harvest:

```text
VISUAL IMPRESSION
```

directly as:

```text
VERIFIED FRACTAL KNOWLEDGE
```

---

# 83. Fractal Retrieval

AMOS fractal retrieval should follow the smallest sufficient dependency path.

```text
BOOTSTRAP CAPSULE
      ↓
FAMILY
      ↓
VALIDATOR
      ↓
FIT / TRACE / BRIDGE
      ↓
RAW DATA OR RULE EVIDENCE
ONLY IF REQUIRED
```

Raw evidence defaults:

```text
DO_NOT_LOAD_UNLESS_REQUIRED
```

unless the conclusion depends on unresolved detail.

---

# 84. Fractal Bootstrap Capsule

```yaml
fractal_bootstrap_capsule:

  claim:
    string

  family:
    id: FRxxx

  validation:
    method: string

  result:
    string

  provenance:
    roots: []

  scope:
    string

  alternatives:
    status: string

  falsifiers: []

  confidence_ceiling:
    string
```

This is the smallest reusable proof representation.

---

# 85. Dependency Closure

A fractal conclusion may depend on:

```text
DATASET
  ↓
PREPROCESSING
  ↓
FAMILY ASSIGNMENT
  ↓
VALIDATOR
  ↓
PARAMETERS
  ↓
ALTERNATIVE TEST
  ↓
CONCLUSION
```

If the load-bearing dataset changes:

```text
INVALIDATE DEPENDENT FIT
```

not unrelated fractal knowledge.

---

# 86. Local Invalidation

Suppose:

```text
FAMILY CLAIM C
depends on:
D1 dataset
M1 fit
A1 alternative duel
```

and:

```text
M1 invalidates
```

Then:

```text
C → REVALIDATION_REQUIRED
```

but independent:

```text
CONSTRUCTIVE CLAIM C2
```

remains untouched.

Fractal recovery follows dependency-local repair.

---

# 87. Taxonomy Change

If authoritative fractal canon changes:

```text
FR001–FR025 taxonomy V1
             ↓
          V2
```

then only claims dependent on changed family semantics require invalidation.

```text
UNCHANGED FAMILY
→ preserve if compatible

CHANGED FAMILY
→ revalidate

REMOVED FAMILY
→ invalidate / remap

NEW FAMILY
→ no retroactive assignment without validation
```

---

# 88. Provenance Topology

```text
DATASET D
    │
    ├── PAPER P1
    │      └── SUMMARY S1
    │
    └── PAPER P2
           └── SUMMARY S2
```

If `P1` and `P2` both derive from the same underlying dataset `D`, their statistical evidence may remain correlated.

Therefore:

```text
MULTIPLE PAPERS
≠
AUTOMATICALLY MULTIPLE INDEPENDENT DATASETS
```

Independence must be demonstrated.

---

# 89. Sybil Hardening

A fractal claim repeated across:

```text
BLOGS
PAPERS
NOTES
AI SUMMARIES
DATABASE ENTRIES
```

may still descend from one original claim.

L15 therefore inherits:

```text
POPULARITY
≠
INDEPENDENT VALIDATION
```

and:

```text
REPETITION
≠
STATISTICAL SUPPORT
```

---

# 90. Causal Overreach Detection

Reject transformations of the form:

```text
SYSTEM IS FRACTAL
      ↓
THEREFORE SYSTEM SELF-ORGANIZES
```

or:

```text
SYSTEM HAS POWER-LAW DISTRIBUTION
      ↓
THEREFORE MECHANISM M CAUSED IT
```

unless mechanism-specific evidence exists.

A distribution may be compatible with multiple mechanisms.

Thus:

```yaml
causal_status:
  licensed_by_fractal_fit_alone: false
```

---

# 91. Semantic Overreach Detection

Reject:

```text
BRAIN HAS STRUCTURE S
AMOS HAS STRUCTURE S
THEREFORE AMOS IS A BRAIN
```

unless bridge governance independently establishes the relevant semantic equivalence.

The strongest supported conclusion may only be:

```text
THE TWO SYSTEMS SHARE
DECLARED STRUCTURAL PROPERTY S
UNDER MAPPING M
```

---

# 92. Recursive Architecture Claims

AMOS may use recursive or fractal organizational patterns as architecture models.

Such claims remain:

```text
AMOS_MODEL
```

unless empirical or formal validation supports stronger classification.

For example:

```text
H → M → L
```

may be described as a fractal knowledge organization pattern.

This does not itself prove mathematical fractality.

---

# 93. Fractal Knowledge Network Firewall

The phrase:

```text
AMOS FRACTAL KNOWLEDGE NETWORK
```

may denote an architectural knowledge-retrieval model.

It must not automatically be interpreted as a verified mathematical fractal.

Distinguish:

```yaml
AMOS_Fractal_Knowledge_Network:
  architectural_class: MODEL
  mathematical_fractal_status:
    UNKNOWN_UNLESS_VALIDATED
```

This preserves AMOS terminology without converting architecture metaphor into empirical proof.

---

# 94. Recursive RSCF Firewall

Recursive RSCF structures may exhibit repeated organizational motifs.

But:

```text
RECURSIVE
≠
FRACTAL
```

unless a canonical fractal family and validator establish the stronger claim.

Likewise:

```text
SELF-SIMILAR
```

must specify:

```text
under what mapping?
over what scales?
with what metric?
with what tolerance?
```

---

# 95. Fractal vs Recursive

Conceptually:

```text
RECURSION
=
rule refers to or generates repeated structure

FRACTAL CLAIM
=
family-specific structure satisfying
family-specific validation
```

Therefore recursion may be relevant evidence but is not sufficient by itself.

---

# 96. Fractal vs Hierarchical

A hierarchy:

```text
H
├── M
│   ├── L
│   └── L
└── M
```

is not automatically fractal.

Hierarchical nesting can exist without self-similarity or fractal scaling.

Thus:

```text
HIERARCHICAL
≠
FRACTAL
```

---

# 97. Fractal vs Modular

Likewise:

```text
MODULARITY
≠
FRACTALITY
```

A modular system can lack scale invariance, self-similarity, or any canonical FR-family property.

---

# 98. Fractal vs Complex

```text
COMPLEX
≠
FRACTAL
```

Complexity alone does not identify a fractal family.

---

# 99. Fractal vs Emergent

```text
EMERGENT
≠
FRACTAL
```

Emergent behavior may or may not exhibit fractal properties.

The relationship requires evidence.

---

# 100. Fractal vs Scale-Free

```text
SCALE-FREE
```

and:

```text
FRACTAL
```

must not be treated as universal synonyms.

Their relationship depends on the canonical family and definitions.

Where authoritative taxonomy is unavailable:

```yaml
relationship:
  status: DO_NOT_INVENT
```

---

# 101. Fractal vs Power Law

Likewise:

```text
POWER LAW
≠
ALL FRACTALS
```

and:

```text
FRACTAL
≠
ALWAYS POWER LAW
```

unless a specific family definition establishes the relationship.

---

# 102. Fractal Knowledge Integrity Invariants

```yaml
fractal_knowledge_invariants:

  FKI_1_FAMILY:
    requirement:
      consequential_fractal_claims_declare_family

  FKI_2_VALIDATOR:
    requirement:
      family_appropriate_validation_method_declared

  FKI_3_STATISTICAL_FIT:
    requirement:
      statistical_claims_use_audited_fit

  FKI_4_XMIN:
    requirement:
      lower_fit_boundary_is_explicit_where_applicable

  FKI_5_UNCERTAINTY:
    requirement:
      parameter_uncertainty_is_visible

  FKI_6_ALTERNATIVES:
    requirement:
      credible_alternative_models_are_challenged

  FKI_7_NO_EYEBALL:
    requirement:
      log_log_visual_similarity_is_not_sufficient

  FKI_8_TRACE:
    requirement:
      generative_claims_preserve_constructive_trace

  FKI_9_CONVERGENCE:
    requirement:
      generative_limit_claims_require_convergence_evidence

  FKI_10_ANALOGY:
    requirement:
      structural_similarity_does_not_imply_isomorphism

  FKI_11_BRIDGE:
    requirement:
      semantic_transfer_requires_governed_bridge

  FKI_12_SCOPE:
    requirement:
      claims_remain_scale_and_regime_bound

  FKI_13_CAUSAL:
    requirement:
      fractal_structure_alone_does_not_license_causal_inference

  FKI_14_PROVENANCE:
    requirement:
      repeated_descendants_do_not_create_independence
```

---

# 103. Anti-Patterns

## FK-A1 — Family-Free Fractal Claim

```text
"THIS IS FRACTAL"
```

without canonical family declaration.

Rejected for consequential use.

---

## FK-A2 — Log-Log Eyeballing

```text
LOOKS STRAIGHT
→ POWER LAW
```

Rejected.

---

## FK-A3 — Parameter Without Uncertainty

```text
alpha = 2.4
```

with no uncertainty or fit context.

Insufficient for audited claim.

---

## FK-A4 — Hidden x_min

Selecting only the region that appears linear without declaring the threshold.

Rejected.

---

## FK-A5 — No Alternative Duel

Fitting one candidate and declaring victory without testing plausible alternatives.

Rejected.

---

## FK-A6 — Visual Generator Matching

```text
LOOKS LIKE MANDELBROT / IFS / L-SYSTEM
```

therefore:

```text
IS GENERATED BY THAT SYSTEM
```

Rejected.

---

## FK-A7 — Finite Iteration Equals Limit

```text
S_10 LOOKS CONVERGED
```

therefore:

```text
S_∞ PROVED
```

Rejected.

---

## FK-A8 — Analogy Laundering

```text
A resembles B
→ A is structurally equivalent to B
→ A has B's semantics
```

without bridge validation.

Rejected.

---

## FK-A9 — Causal Laundering

```text
POWER LAW OBSERVED
→ SPECIFIC CAUSAL MECHANISM PROVED
```

Rejected.

---

## FK-A10 — Scale Leakage

```text
FRACTAL OVER RANGE R
→ FRACTAL AT ALL SCALES
```

Rejected.

---

## FK-A11 — Taxonomy Fabrication

Inventing definitions for missing `FR001–FR025` identifiers.

Strictly prohibited.

---

## FK-A12 — Echo Confirmation

Multiple descendants of one fractal claim treated as independent validations.

Rejected.

---

# 104. Fractal Claim Algorithm

```python
def evaluate_fractal_claim(claim, evidence):

    family = claim.family

    if family is None:
        return UNKNOWN

    validator = canonical_validator(family)

    if validator is None:
        return GAP

    result = validator.validate(
        claim=claim,
        evidence=evidence
    )

    alternatives = adversarial_alternatives(
        family=family,
        evidence=evidence
    )

    scope = validate_scope(
        claim,
        evidence
    )

    provenance = validate_provenance(
        evidence
    )

    return classify_with_confidence_ceiling(
        result=result,
        alternatives=alternatives,
        scope=scope,
        provenance=provenance
    )
```

Semantic pseudocode only.

---

# 105. Statistical Claim Algorithm

```python
def evaluate_statistical_fractal(
    data,
    family,
    x_min
):

    require_declared_family(family)
    require_declared_xmin(x_min)

    fit = mle_fit(
        data=data,
        family=family,
        x_min=x_min
    )

    ci = estimate_confidence_interval(
        fit
    )

    alternatives = compare_alternative_models(
        data=data,
        candidate=family,
        x_min=x_min
    )

    sensitivity = sensitivity_test(
        data=data,
        family=family,
        x_min=x_min
    )

    if alternatives.prefer_other:
        return REJECTED

    if alternatives.indistinguishable:
        return COMPETING

    if sensitivity.fragile:
        return CONDITIONAL

    return supported_class(
        fit,
        ci
    )
```

---

# 106. Constructive Claim Algorithm

```python
def evaluate_constructive_fractal(
    generator,
    claimed_structure
):

    if generator.rules is None:
        return UNKNOWN

    trace = generate_trace(generator)

    if not trace.rule_valid:
        return REJECTED

    convergence = validate_convergence(
        generator,
        trace
    )

    if convergence == FAIL:
        return REJECTED

    if convergence == UNKNOWN:
        return CONDITIONAL

    if not structure_match(
        trace,
        claimed_structure
    ):
        return REJECTED

    return SUPPORTED
```

---

# 107. Analogy Governance Algorithm

```python
def evaluate_fractal_analogy(
    source,
    target,
    bridge=None
):

    resemblance = detect_declared_structure(
        source,
        target
    )

    if resemblance is None:
        return UNKNOWN

    if bridge is None:
        return MODEL

    mapping = validate_mapping(
        bridge
    )

    if not mapping.valid:
        return CONDITIONAL

    if not scope_compatible(
        source,
        target,
        bridge
    ):
        return REJECTED

    return classify_bridge(
        mapping
    )
```

---

# 108. Claim Classes

L15 uses the weakest accurate class.

```yaml
fractal_claim_classes:

  VERIFIED:
    meaning:
      family and relevant validation obligations established
      within declared scope

  DERIVED:
    meaning:
      conclusion follows from validated premises

  MODEL:
    meaning:
      useful structural or explanatory representation
      without sufficient validation for stronger class

  CONDITIONAL:
    meaning:
      valid only under explicit unresolved assumptions
      or incomplete validation

  COMPETING:
    meaning:
      multiple family/model hypotheses remain viable

  UNKNOWN:
    meaning:
      evidence or canon insufficient
```

---

# 109. Falsifiers

## F1 — Recovered Fractal Canon Defines Different Family Taxonomy

Original falsifier:

> **Recovered fractal canon defines different family taxonomy.**

If authoritative canon establishes:

```text
FR001–FR025 taxonomy T_authoritative
```

different from assumptions in L15:

```text
AUTHORITATIVE TAXONOMY
        ↓
COMPARE
        ↓
CONFLICT?
  ├── NO → preserve
  └── YES
        ↓
invalidate affected family assignments
        ↓
revalidate dependent claims
```

---

## F2 — Statistical Validation Canon Conflict

If authoritative family canon defines different statistical validation obligations than:

```text
MLE alpha
CI
x_min
alternative duel
```

the affected FK-2 interpretation must be revised.

The supplied source currently explicitly specifies those requirements, so any conflict requires authoritative supersession.

---

## F3 — Constructive Validation Canon Conflict

If authoritative generative-family canon defines a different proof obligation than rule trace plus convergence evidence, FK-3 must be updated accordingly.

---

## F4 — Bridge Governance Conflict

If authoritative canon defines formal conditions under which semantic transfer is licensed without the bridge model proposed here, FK-4 extensions must be revised.

---

# 110. Known Gaps

```yaml
gaps:

  G1:
    severity: CRITICAL
    description:
      Exact FR001-FR025 family taxonomy is not supplied by the L15 source.

  G2:
    severity: CRITICAL
    description:
      Family-specific validator mapping for FR001-FR025 is not supplied.

  G3:
    severity: DECISION_RELEVANT
    description:
      Exact statistical alternative-model sets are family-dependent and unspecified.

  G4:
    severity: DECISION_RELEVANT
    description:
      Exact confidence-interval method is not defined.

  G5:
    severity: DECISION_RELEVANT
    description:
      Exact x_min selection procedure is not defined.

  G6:
    severity: DECISION_RELEVANT
    description:
      Exact convergence criteria for each generative family are not defined.

  G7:
    severity: EXPLANATORY
    description:
      Formal bridge-governance schema is not supplied by the source.

  G8:
    severity: EXPLANATORY
    description:
      Exact relationship between RSCF and canonical fractal families is not supplied.

  G9:
    severity: EXPLANATORY
    description:
      Exact relationship between the AMOS Fractal Knowledge Network and mathematical fractal families remains unverified unless separately defined by canon.
```

These gaps must remain explicit.

---

# 111. Canonical Safety Boundary

L15 does **not** establish that:

* AMOS itself is a mathematical fractal,
* RSCF is mathematically fractal,
* H/M/L recursion proves fractality,
* recursive reasoning is fractal in the formal mathematical sense,
* power-law appearance proves a power law,
* every scale-free structure is fractal,
* every fractal structure is scale-free,
* shared fractal dimension proves common mechanism,
* visual similarity proves common generator,
* structural similarity proves semantic identity,
* structural similarity proves causation,
* FR001–FR025 definitions can be reconstructed from their identifiers alone.

Unless separately validated, these remain:

```text
MODEL
UNKNOWN
or
GAP
```

as appropriate.

---

# 112. RSCF Claim Graph

```yaml
claim_graph:

  FK_C001:
    class: AMOS_MODEL
    claim:
      Consequential fractal claims should declare a canonical family and validator.

  FK_C002:
    class: CONDITIONAL
    claim:
      Canonical family identifiers belong to the FR001-FR025 taxonomy.

  FK_C003:
    class: AMOS_MODEL
    claim:
      Statistical fractal claims require audited fits rather than visual log-log inference.

  FK_C004:
    class: CONDITIONAL
    claim:
      Statistical family validation requires MLE alpha with confidence interval and declared x_min where specified by FK-2.

  FK_C005:
    class: AMOS_MODEL
    claim:
      Credible alternative statistical models must be compared.

  FK_C006:
    class: AMOS_MODEL
    claim:
      Generative fractal claims require constructive rule traces.

  FK_C007:
    class: AMOS_MODEL
    claim:
      Generative limit claims require convergence evidence.

  FK_C008:
    class: DERIVED
    claim:
      Visual similarity alone cannot establish a common generator.

  FK_C009:
    class: DERIVED
    claim:
      Structural resemblance alone cannot establish semantic isomorphism.

  FK_C010:
    class: DERIVED
    claim:
      Fractal structure alone cannot establish causal mechanism.

  FK_C011:
    class: DERIVED
    claim:
      Fractal claims remain bounded by their validated scale and regime.

  FK_C012:
    class: CONDITIONAL
    claim:
      Exact FR001-FR025 mappings remain unknown until authoritative taxonomy is recovered.
```

---

# 113. Dependency Graph

```yaml
dependency_graph:

  FK_1:
    depends_on:
      - FR001_FR025_taxonomy
      - family_validator_registry
      - provenance

  FK_2:
    depends_on:
      - statistical_family_definition
      - dataset
      - MLE_method
      - confidence_interval_method
      - x_min_method
      - alternative_model_comparison

  FK_3:
    depends_on:
      - generative_family_definition
      - initial_state
      - rule_set
      - trace
      - convergence_validator

  FK_4:
    depends_on:
      - structural_mapping
      - bridge_governance
      - scope
      - regime
      - semantic_preservation_conditions
```

---

# 114. Unified FK-1 → FK-4 Architecture

```text
                 FRACTAL CLAIM
                       │
                       ▼
             ┌───────────────────┐
             │ FK-1 FAMILY       │
             │ DECLARATION       │
             └─────────┬─────────┘
                       ↓
               FAMILY TYPE?
            ┌──────────┼──────────┐
            ↓          ↓          ↓
       STATISTICAL  GENERATIVE  ANALOGICAL/
                              CROSS-DOMAIN
            │          │          │
            ↓          ↓          ↓
         FK-2       FK-3       FK-4
       AUDITED    RULE TRACE    BRIDGE
         FIT      + CONVERGENCE GOVERNANCE
            │          │          │
            └──────────┼──────────┘
                       ↓
              ADVERSARIAL CHECK
                       ↓
             ALTERNATIVE MODELS
                       ↓
                 SCOPE CHECK
                       ↓
              PROVENANCE CHECK
                       ↓
               CLAIM CLASS
```

---

# 115. Fractal Validation Contract

```yaml
fractal_validation_contract:

  identity:
    claim_id: string

  family:
    canonical_id: FR001-FR025
    taxonomy_version: string|null

  method:
    validator: string

  evidence:
    references: []

  provenance:
    roots: []

  scope:
    scale: string|null
    regime: string|null

  statistical:
    alpha: number|null
    confidence_interval: null
    x_min: number|null
    alternatives: []

  constructive:
    rules: []
    trace: []
    convergence: null

  bridge:
    mapping: null
    preserved_properties: []

  falsifiers: []

  claim_class:
    string

  confidence_ceiling:
    string
```

Only the family-relevant sections need be populated.

---

# 116. Minimal Statistical Contract

```text
FAMILY KNOWN?
   ↓
DATA PROVENANCE VALID?
   ↓
x_min DECLARED?
   ↓
MLE FIT?
   ↓
CI AVAILABLE?
   ↓
ALTERNATIVE DUEL?
   ↓
SCOPE DECLARED?
   ↓
CLAIM
```

Missing critical element:

```text
→ CONDITIONAL / UNKNOWN
```

rather than unsupported certainty.

---

# 117. Minimal Constructive Contract

```text
FAMILY KNOWN?
   ↓
INITIAL STATE KNOWN?
   ↓
RULES KNOWN?
   ↓
TRACE REPRODUCIBLE?
   ↓
CONVERGENCE SUPPORTED?
   ↓
OUTPUT MATCHES?
   ↓
CLAIM
```

Visual similarity cannot substitute for the trace.

---

# 118. Minimal Analogy Contract

```text
STRUCTURAL PROPERTY IDENTIFIED?
   ↓
MAPPING DECLARED?
   ↓
PRESERVATION CONDITIONS KNOWN?
   ↓
SCOPE COMPATIBLE?
   ↓
SEMANTIC BRIDGE VALID?
   ↓
TRANSFER ONLY LICENSED PROPERTIES
```

Without bridge validation:

```text
ANALOGY REMAINS MODEL
```

---

# 119. Core Compression

```text
FK-1
NAME THE FAMILY.
NAME THE VALIDATOR.

FK-2
FIT BEFORE CLAIM.
NO LOG-LOG EYEBALLING.

FK-3
TRACE THE GENERATOR.
SHOW CONVERGENCE.

FK-4
RESEMBLANCE IS NOT ISOMORPHISM.
ISOMORPHISM IS NOT AUTOMATIC SEMANTIC TRANSFER.
```

---

# 120. Canonical One-Line Law

> **A fractal claim is only as strong as its declared family, family-appropriate validation, provenance, scope, and successful discrimination from competing explanations; visual or structural resemblance alone never licenses mathematical, semantic, or causal equivalence.**

---

# 121. Canonical Equations

Conceptual AMOS models:

```text
FRACTAL CLAIM CONFIDENCE
≤
min(
  FAMILY,
  VALIDATOR,
  EVIDENCE,
  PROVENANCE,
  SCOPE,
  ALTERNATIVE DISCRIMINATION
)
```

For statistical families:

```text
STATISTICAL SUPPORT
≠
LOG-LOG APPEARANCE
```

and:

```text
AUDITED FIT
=
DECLARED MODEL
+
MLE PARAMETERS
+
UNCERTAINTY
+
DECLARED x_min
+
ALTERNATIVE DUEL
```

where family-appropriate.

For generative families:

```text
GENERATIVE SUPPORT
=
RULE TRACE
+
CONVERGENCE EVIDENCE
```

not:

```text
VISUAL SIMILARITY
```

For cross-domain mapping:

```text
ANALOGY
≠
ISOMORPHISM
```

and:

```text
ISOMORPHISM
≠
UNIVERSAL SEMANTIC TRANSFER
```

and:

```text
STRUCTURAL SIMILARITY
≠
CAUSATION
```

---

# 122. Final Proof Capsule

```yaml
proof_capsule:

  claim:
    class: CONDITIONAL
    text:
      >
        AMOS L15 models fractal knowledge as family-specific,
        validation-bound knowledge. Fractal claims declare a canonical
        FR001-FR025 family and its validation method. Statistical families
        require audited fitting rather than log-log visual inference,
        including MLE alpha with confidence interval, declared x_min,
        and alternative-model comparison where FK-2 applies. Generative
        families such as IFS, L-system, and tiling require constructive
        rule traces and convergence evidence rather than visual similarity.
        Structural resemblance does not establish isomorphism, semantic
        transfer, or causation without separately governed bridges.

  source:
    provenance:
      AMOS_corpus

    scope:
      core_laws

  load_bearing_premises:
    - canonical_fractal_families_exist
    - FR001_FR025_is_the_referenced_family_range
    - family_specific_validation_is_required
    - statistical_claims_can_be_audited
    - constructive_generators_can_be_traced
    - convergence_can_be_evaluated
    - semantic_transfer_requires_bridge_governance

  dependencies:
    - FR001_FR025_taxonomy
    - statistical_validation
    - provenance_topology
    - scope_regime_firewall
    - competing_hypotheses
    - causal_firewall
    - RSCF
    - fractal_knowledge_network

  competing_explanations:
    - apparent_scaling_may_be_generated_by_non_fractal_models
    - multiple_statistical_families_may_fit_the_same_finite_sample
    - visual_similarity_may_arise_from_different_generators
    - structural_similarity_may_not_preserve_semantics
    - apparent_self_similarity_may_exist_only_over_a_limited_scale_range
    - repeated_claims_may_share_common_provenance

  falsifiers:
    - recovered_fractal_canon_defines_different_family_taxonomy
    - authoritative_statistical_family_validators_supersede_FK2
    - authoritative_constructive_family_validators_supersede_FK3
    - authoritative_bridge_governance_supersedes_FK4_extensions

  gaps:
    - exact_FR001_FR025_mapping_not_supplied
    - family_specific_validator_registry_not_supplied
    - family_specific_convergence_criteria_not_supplied
    - exact_bridge_governance_schema_not_supplied

  confidence_ceiling:
    CONDITIONAL

  canonical_status:
    CONDITIONAL

  specification_status:
    PROPOSED_SPECIFICATION
```

---

# 123. RSCF Node

```yaml
RSCF-NODE:

  node_id:
    l15_fractal_knowledge

  node_type:
    note

  path:
    01_CANON/01_CORE_LAWS/L15_FRACTAL_KNOWLEDGE.md

  epistemic_class:
    AMOS_MODEL

  claim_class:
    CONDITIONAL

  canonical_status:
    CONDITIONAL

  specification_status:
    PROPOSED_SPECIFICATION

RSCF-RELATIONS:

  - INDEXED_BY: [[00_HOME]]

  - INDEXED_BY: [[AMOS_RSCF_NODES]]

  - CHILD_OF: [[LAW_HIERARCHY]]

  - MEMBER_OF: [[01_CORE_LAWS_MOC]]

  - RELATED_TO: [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

  - RELATED_TO: [[AMOS_CORE_ALL_VERSIONS_FRACTAL_KNOWLEDGE_NETWORK]]

  - RELATED_TO: [[RSCF]]

  - RELATED_TO: [[GMEF]]

  - RELATED_TO: [[PROVENANCE_TOPOLOGY]]

  - RELATED_TO: [[COMPETING_HYPOTHESES]]

  - RELATED_TO: [[CAUSAL_FIREWALL]]

  - RELATED_TO: [[SCOPE_REGIME_FIREWALL]]

  - RELATED_TO: [[L11_KNOWLEDGE_MEMORY]]
```

---

**00_ROOT_MOC:** [[AMOS MOC]]

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]]

**MOC:** [[01_CORE_LAWS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---

# 124. L15 Final Invariant

```text
FRACTAL KNOWLEDGE
MUST REMAIN

FAMILY-TYPED
+
VALIDATOR-BOUND
+
PROVENANCE-AWARE
+
SCALE-BOUND
+
REGIME-AWARE
+
ALTERNATIVE-TESTED
```

For statistical families:

```text
FIT
BEFORE
CLAIM
```

For generative families:

```text
TRACE
BEFORE
IDENTIFICATION
```

For cross-domain reasoning:

```text
BRIDGE
BEFORE
SEMANTIC TRANSFER
```

The operational invariant is:

```text
OBSERVE
→ DECLARE FAMILY
→ DECLARE VALIDATOR
→ TEST
→ CHALLENGE ALTERNATIVES
→ CHECK SCOPE
→ CHECK PROVENANCE
→ CLASSIFY
→ PRESERVE FALSIFIERS
```

with the hard firewalls:

```text
LOG-LOG EYEBALLING
≠
STATISTICAL PROOF

VISUAL SIMILARITY
≠
GENERATIVE PROOF

RECURSION
≠
AUTOMATIC FRACTALITY

ANALOGY
≠
ISOMORPHISM

ISOMORPHISM
≠
AUTOMATIC SEMANTIC IDENTITY

FRACTAL STRUCTURE
≠
CAUSAL PROOF
```

**Conclusion class: CONDITIONAL / AMOS_MODEL.**

```
