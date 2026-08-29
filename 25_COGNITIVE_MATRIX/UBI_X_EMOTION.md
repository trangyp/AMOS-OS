---
title: UBI x Emotion Cognitive Matrix Specification
type: cognitive_matrix
source: 25_COGNITIVE_MATRIX
artifact: UBI_X_EMOTION.md
artifact_id: amos_25_cognitive_matrix_ubi_x_emotion
origin_architect: Trang Phan
steward: Trang Phan
system: AMOS OS
plane: 25_COGNITIVE_MATRIX
segment: 25_COGNITIVE_MATRIX
artifact_kind: MATRIX_SPEC
path: 25_COGNITIVE_MATRIX/UBI_X_EMOTION.md
tags:
- amos-os
- cognitive-matrix
- vault
- 25_cognitive_matrix
- ubi_x_emotion
- emotion_engine
- affective_computing
- affective_vector
- nei
- valence
- arousal
- dominance
- cooling_circuit
- substrate_refusal
- rscf
- ubi-x-emotion-matrix
- ubi-emotion-binding
- unified-biological-intelligence
- 25-cognitive-matrix-moc
version: 2.0.0
updated: '2026-08-28'
status: ACTIVE_REFERENCE
epistemic_class: AMOS_MODEL
canonical_status: SOURCE_GROUNDED_CANON_CANDIDATE
implementation_status: CONCEPTUAL_SOURCE_DEFINED
validation_status: PASSED_CONSTITUTIONAL_TESTS
executable_binding: ESTABLISHED
framework_binding:
  matrix_counterpart:
    artifact:
    - - UBI_X_EMOTION_MATRIX
  knowledge_binding:
    artifact:
    - - UBI_EMOTION_BINDING
source_integrity:
  equation_rendering: PARTIALLY_CORRUPTED
  recoverable_equation: E_t = <v_t, a_t, d_t> ∈ [-1,1] × [0,1] × [-1,1]
  component_semantics: RECOVERABLE_FROM_LOCAL_SOURCE_CONTEXT
  unresolved_matrix_fields:
  - FIRST_TRIGGER_VARIABLES
  - TARGET_PLANES
  reconstruction_policy: DO_NOT_INVENT_MISSING_CANON
---

# UBI × Emotion Cognitive Matrix Specification — Canon Recovery

This specification resolves several important gaps from the preceding matrix table. The strongest source-supported recovery is:

$$
\boxed{
\vec E_t=\langle v_t,a_t,d_t\rangle
\in[-1,1]\times[0,1]\times[-1,1]
}
$$

with the intended component semantics recoverable from the supplied “Where” section despite rendering corruption:

$$
v_t=\text{Valence},\qquad
a_t=\text{Arousal},\qquad
d_t=\text{Dominance}
$$

The specification also directly adds two invariant guards:

$$
a_t>0.90\Rightarrow ActivateCoolingCircuit
$$

$$
v_t<-0.70\Rightarrow EngageSubstrateRefusal
$$

This materially resolves the earlier uncertainty around \(v_t\) and \(a_t\), but **does not recover the matrix table's missing first trigger variables or Target Plane cells**.

---

# 5. Dimensional Invariant

Every source-valid affective vector satisfies:

$$
-1\le v_t\le1
$$

$$
0\le a_t\le1
$$

$$
-1\le d_t\le1
$$

Therefore:

$$
\boxed{
\vec E_t\in
[-1,1]\times[0,1]\times[-1,1]
}
$$

is a structural invariant of this specification.

---

# 6. Valence

Valence occupies:

$$
v_t\in[-1,1]
$$

The source describes it as:

`Hedonic tone`.

The artifact does not further define the calibration of the endpoints.

Thus it establishes the mathematical range, but not an empirical
measurement protocol.

---

# 7. Arousal

Arousal occupies:

$$
a_t\in[0,1]
$$

and is source-described as:

`Metabolic activation`.

This resolves the earlier matrix-table ambiguity around \(a_t\).

---

# 8. Dominance

Dominance occupies:

$$
d_t\in[-1,1]
$$

and is source-described as:

`Agency / Autonomy sense`.

This dimension was not visible in the preceding matrix table but is
explicitly part of the underlying affective vector.

---

# 9. Invariant Guard — High Arousal

The source explicitly defines:

$$
\boxed{
Arousal>0.90
\Rightarrow
ActivateCoolingCircuit
}
$$

Using the now-resolved symbol:

$$
\boxed{
a_t>0.90
\Rightarrow
ActivateCoolingCircuit
}
$$

---

# 10. Strict Arousal Threshold

The source uses:

$$
>
$$

rather than:

$$
\ge
$$

Therefore:

$$
a_t=0.90
$$

does **not** satisfy the displayed cooling predicate.

Whereas:

$$
a_t=0.91
$$

does.

---

# 11. Cooling Circuit

The source establishes the control action:

`ActivateCoolingCircuit`.

It does not establish within this artifact:

- implementation mechanism;
- duration;
- release threshold;
- hysteresis;
- pacing function;
- biological substrate;
- target plane;
- relationship to Metabolic Pacing.

Those remain dependencies.

---

# 12. Invariant Guard — Negative Valence

The source explicitly defines:

$$
\boxed{
Valence<-0.70
\Rightarrow
EngageSubstrateRefusal
}
$$

Using the resolved source symbol:

$$
\boxed{
v_t<-0.70
\Rightarrow
EngageSubstrateRefusal
}
$$

---

# 13. Strict Valence Threshold

Again the operator is strict:

$$
<
$$

Therefore:

$$
v_t=-0.70
$$

does not satisfy the displayed invariant.

But:

$$
v_t=-0.71
$$

does.

---

# 14. Substrate Refusal

The source establishes the named action:

`EngageSubstrateRefusal`.

This artifact does not independently define its implementation.

Therefore:

$$
EngageSubstrateRefusal
\neq
AutomaticallyKnownImplementation
$$

---

# 15. Substrate Refusal ≠ Refusal Firewall

The matrix counterpart previously associates:

`Refusal Firewall`

with:

`High Threat / Anxiety`.

This specification introduces:

`EngageSubstrateRefusal`

under:

$$
v_t<-0.70
$$

The two terms are structurally related but **not proven identical**.

Therefore:

$$
\boxed{
SubstrateRefusal
\stackrel{?}{=}
RefusalFirewall
}
$$

remains unresolved.

---

# 16. Cross-Artifact Valence Recovery

The matrix table contained:

$$
v_t<-0.5
$$

inside the High Threat / Anxiety trigger.

This specification establishes:

$$
v_t=\text{Valence}
$$

Therefore the earlier row can now safely be read as containing the
condition:

$$
\boxed{
Valence_t<-0.5
}
$$

This is a genuine source-grounded recovery.

---

# 17. Two Valence Thresholds

The combined source now contains at least two distinct valence
thresholds:

$$
v_t<-0.5
$$

for the visible High Threat / Anxiety matrix condition, and:

$$
v_t<-0.70
$$

for `EngageSubstrateRefusal`.

These thresholds must not be collapsed.

---

# 18. Nested Valence Region

Mathematically:

$$
v_t<-0.70
\Rightarrow
v_t<-0.5
$$

Thus any valence satisfying the Substrate Refusal invariant also
satisfies the **valence component** of the High Threat matrix row.

It does not necessarily satisfy the complete High Threat predicate,
because that row still contains an unresolved first trigger variable.

---

# 19. Valence Control Topology

The source-supported topology is:

```text
v_t = VALENCE
      │
      ├── v_t < -0.5
      │       ↓
      │   HIGH-THREAT ROW
      │   VALENCE COMPONENT
      │
      └── v_t < -0.70
              ↓
      ENGAGE SUBSTRATE REFUSAL
```

---

# 20. Cross-Artifact Arousal Recovery

The matrix table contains:

$$
a_t\in[0.4,0.7]
$$

inside Optimal Flow.

The current specification establishes:

$$
a_t=\text{Arousal}
$$

and:

$$
a_t\in[0,1].
$$

Therefore the earlier row can now safely be interpreted as:

$$
\boxed{
Arousal_t\in[0.4,0.7]
}
$$

within the Optimal Flow predicate.

---

# 21. Optimal-Flow Arousal Band

The source therefore defines an Optimal Flow arousal component:

$$
0.4\le a_t\le0.7
$$

This occupies a middle portion of the full arousal domain:

$$
0\le a_t\le1.
$$

---

# 22. Cooling vs Optimal Flow

Cooling activates at:

$$
a_t>0.90.
$$

Optimal Flow requires:

$$
a_t\in[0.4,0.7].
$$

These arousal conditions are disjoint:

$$
[0.4,0.7]\cap(0.90,1]=\varnothing.
$$

Therefore, **on the arousal dimension alone**, Optimal Flow's visible
arousal condition and the Cooling Circuit invariant cannot both be
true simultaneously.

This is a mathematically VERIFIED consequence of the supplied source.

---

# 23. Important Scope Boundary

That disjointness applies specifically to:

- the Optimal Flow row's \(a_t\) component; and
- the Cooling Circuit invariant.

It does not prove that all aspects of Optimal Flow and cooling are
globally mutually exclusive under every future specification.

---

# 24. Arousal Operating Regions

The source now establishes:

```text
0.00 ─────────────────────────────── 1.00
          │              │      │
         0.4            0.7    0.90
          ├──────────────┤      │
          OPTIMAL-FLOW           │
          AROUSAL BAND           │
                                 ▼
                         COOLING CIRCUIT
                         when a_t > 0.90
```

No special behavior is specified here for:

$$
a_t\in(0.7,0.90].
$$

---

# 25. Dominance Has No Visible Guard

The specification defines:

$$
d_t=\text{Dominance}
$$

but supplies no invariant threshold involving \(d_t\).

Therefore:

```yaml
DOMINANCE:

  definition:
    SOURCE_DEFINED

  range:
    SOURCE_DEFINED

  invariant_guard:
    NOT_PRESENT_IN_SUPPLIED_SPEC

  matrix_row_usage:
    NOT_VISIBLE_IN_SUPPLIED_MATRIX
```

---

# 26. Do Not Invent a Dominance Threshold

No canonical rule such as:

$$
d_t<x
$$

or:

$$
d_t>x
$$

may be added from symmetry or affective-model expectations.

---

# 27. NEI Binding

The introductory statement says the artifact formalizes integration
between:

`affective state dynamics (NEI)`

and:

`cognitive appraisal mechanisms`.

Therefore NEI is explicitly associated with affective-state dynamics
in this artifact.

The expansion or complete definition of `NEI` is not supplied here.

---

# 28. NEI Must Remain Source Terminology

Do not invent an expansion for `NEI` from acronym similarity.

The authoritative expansion should come from the relevant AMOS
knowledge artifact.

---

# 29. Core Source Model

The specification can be compactly represented as:

$$
\boxed{
NEI
\rightarrow
\vec E_t
=
\langle v_t,a_t,d_t\rangle
\rightarrow
CognitiveAppraisal
}
$$

with invariant guards:

$$
a_t>0.90
\Rightarrow
Cooling
$$

$$
v_t<-0.70
\Rightarrow
SubstrateRefusal.
$$

---

# 30. Affect-to-Cognition Integration

The source explicitly states that affective dynamics are mathematically
integrated with cognitive appraisal mechanisms.

Therefore:

$$
\boxed{
AffectiveState
\leftrightarrow
CognitiveAppraisalIntegration
}
$$

is source-grounded at the AMOS model level.

The exact mathematical appraisal function is not supplied.

---

# 31. No Full Transition Equation

The specification defines the affective state vector but does not
provide a state-transition law such as:

$$
\vec E_{t+1}=F(\vec E_t,\ldots).
$$

Therefore the phrase:

`affective state dynamics`

does not license invention of a missing dynamical equation.

---

# 32. No Cognitive Appraisal Equation

Likewise, no explicit function:

$$
C_t=G(\vec E_t)
$$

is supplied.

The existence of integration is stated, but its complete functional
form remains unspecified.

---

# 33. Matrix Counterpart Binding

The specification explicitly binds:

```yaml
matrix_counterpart:
  artifact: ""
```

Thus the specification and matrix table are authoritative counterparts
within the supplied corpus.

---

# 34. Knowledge Binding

The specification explicitly binds:

```yaml
knowledge_binding:
  artifact: ""
```

This remains the primary unresolved semantic dependency.

---

# 35. Biological Master

The specification explicitly connects:

``.

This establishes a declared architectural connection between the
affective specification and the biological master.

It does not by itself specify the exact dependency direction.

---

# 36. Cognitive Matrix Plane

The artifact explicitly connects to:

``.

Thus its placement within the Cognitive Matrix plane is directly
source-grounded.

---

# 37. Updated Matrix Recovery

The earlier matrix can now be safely strengthened to:

| State                 | Source-visible condition      | Resolved semantics                    | Impact                                             | Guard                |
| --------------------- | ----------------------------- | ------------------------------------- | -------------------------------------------------- | -------------------- |
| High Threat / Anxiety | (X_H>0.8,;v_t\<-0.5)          | (v_t=) Valence                        | Prune speculative branches; tighten safety margins | Refusal Firewall     |
| Fatigue / Apathy      | (X_F\<0.2,;\\tau\_{bio}\<0.4) | (\\tau\_{bio}) still externally bound | Reduce reasoning horizon; queue non-critical tasks | Metabolic Pacing     |
| Optimal Flow          | (X_O>0.4,;a_t\\in[0.4,0.7])   | (a_t=) Arousal                        | Authorize complex multi-agent proofs               | Gamma Coherence Lock |

where:

$$
X_H,X_F,X_O
$$

remain noncanonical placeholders.

---

# 38. What This Specification Resolves

```yaml
RESOLVED:

  v_t:
    VALENCE

  v_t_description:
    HEDONIC_TONE

  v_t_domain:
    [-1, 1]

  a_t:
    AROUSAL

  a_t_description:
    METABOLIC_ACTIVATION

  a_t_domain:
    [0, 1]

  d_t:
    DOMINANCE

  d_t_description:
    AGENCY_AUTONOMY_SENSE

  d_t_domain:
    [-1, 1]

  affective_vector:
    "<v_t, a_t, d_t>"

  cooling_threshold:
    "a_t > 0.90"

  cooling_action:
    ACTIVATE_COOLING_CIRCUIT

  substrate_refusal_threshold:
    "v_t < -0.70"

  substrate_refusal_action:
    ENGAGE_SUBSTRATE_REFUSAL
```

---

# 39. What Remains Unresolved

```yaml
UNRESOLVED:

  - MATRIX_HIGH_THREAT_FIRST_VARIABLE
  - MATRIX_FATIGUE_FIRST_VARIABLE
  - MATRIX_OPTIMAL_FLOW_FIRST_VARIABLE

  - MATRIX_HIGH_THREAT_TARGET_PLANE
  - MATRIX_FATIGUE_TARGET_PLANE
  - MATRIX_OPTIMAL_FLOW_TARGET_PLANE

  - MATRIX_ROW_LOGICAL_CONNECTIVES

  - tau_bio_DEFINITION

  - NEI_FULL_DEFINITION

  - COGNITIVE_APPRAISAL_FUNCTION

  - AFFECTIVE_STATE_TRANSITION_FUNCTION

  - COOLING_CIRCUIT_IMPLEMENTATION

  - SUBSTRATE_REFUSAL_IMPLEMENTATION

  - REFUSAL_FIREWALL_RELATION_TO_SUBSTRATE_REFUSAL

  - METABOLIC_PACING_RELATION_TO_COOLING_CIRCUIT

  - GAMMA_COHERENCE_LOCK_IMPLEMENTATION

  - MULTI_STATE_ARBITRATION

  - CROSS_PLANE_PRECEDENCE
```

---

# 40. Corrected Retrieval Priority

The previous matrix analysis identified `UBI_X_EMOTION` as the first
retrieval target.

That dependency is now available.

It resolves \(v_t\) and \(a_t\), but not the missing matrix variables
or target planes.

Therefore the next smallest sufficient retrieval target becomes:

$$
\boxed{
[[UBI_EMOTION_BINDING]]
}
$$

followed only as required by:

$$
[[UNIFIED_BIOLOGICAL_INTELLIGENCE]].
$$

---

# 41. Source Topology

```text
         UNIFIED BIOLOGICAL INTELLIGENCE
                      │
                      ▼
             UBI_EMOTION_BINDING
                      │
                      ▼
               UBI_X_EMOTION
                SPECIFICATION
                      │
                      ▼
             AFFECTIVE VECTOR
           <v_t, a_t, d_t>
                      │
            ┌─────────┴─────────┐
            ▼                   ▼
   UBI_X_EMOTION_MATRIX   INVARIANT GUARDS
            │                   │
            ▼                   ├─ a_t > .90
   COGNITIVE POLICIES           │    → Cooling
                                │
                                └─ v_t < -.70
                                     → Substrate Refusal
```

The dependency directions beyond explicit links are **DERIVED** and
should be revalidated against the binding.

---

# 42. Cross-Plane Proof Capsule

```yaml
PROOF_CAPSULE:

  claim:
    >
      UBI_X_EMOTION v2.0.0 defines a three-component affective
      state vector consisting of valence, arousal, and dominance,
      together with high-arousal cooling and strongly-negative-
      valence substrate-refusal invariants.

  class:
    SOURCE_CLAIM

  load_bearing_premises:

    - supplied artifact is UBI_X_EMOTION v2.0.0
    - locally corrupted mathematical rendering is recoverable
      from adjacent source text
    - v_t corresponds to Valence
    - a_t corresponds to Arousal
    - d_t corresponds to Dominance
    - source operators > and < are preserved
    - ranges are preserved

  evidence:

    affective_vector:
      "<v_t, a_t, d_t>"

    ranges:
      "[-1,1] × [0,1] × [-1,1]"

    semantics:
      v_t: "Valence (Hedonic tone)"
      a_t: "Arousal (Metabolic activation)"
      d_t: "Dominance (Agency / Autonomy sense)"

    invariants:
      - "Arousal > 0.90 => ActivateCoolingCircuit"
      - "Valence < -0.70 => EngageSubstrateRefusal"

  scope:
    AMOS_MODEL

  dependencies:

    - ""
    - ""
    - ""

  competing_explanations:

    refusal_relation:

      H1:
        >
          EngageSubstrateRefusal is the mechanism underlying
          Refusal Firewall.

      H2:
        >
          EngageSubstrateRefusal and Refusal Firewall are
          distinct but coordinated mechanisms.

      H3:
        >
          They operate at different planes or control levels.

    cooling_relation:

      H1:
        >
          ActivateCoolingCircuit participates directly in
          Metabolic Pacing.

      H2:
        >
          Cooling Circuit and Metabolic Pacing are separate
          mechanisms sharing affective/biological inputs.

  falsifiers:

    - authoritative intact source contradicts vector reconstruction
    - component definitions change
    - component ranges change
    - invariant thresholds change
    - invariant actions change
    - artifact is superseded

  confidence_ceiling:

    vector_structure:
      SOURCE_GROUNDED

    component_semantics:
      SOURCE_GROUNDED

    component_ranges:
      SOURCE_GROUNDED

    invariant_thresholds:
      SOURCE_GROUNDED

    mechanism_semantics:
      PARTIALLY_UNKNOWN

    runtime:
      SOURCE_DECLARED_ONLY

    empirical_validity:
      NOT_ESTABLISHED
```

---

# 43. Boundary Tests

```yaml
VALENCE_TESTS:

  lower_domain:
    v_t: -1
    valid: true

  upper_domain:
    v_t: 1
    valid: true

  substrate_refusal_boundary:
    v_t: -0.70
    engage: false

  substrate_refusal_below:
    v_t: -0.71
    engage: true


AROUSAL_TESTS:

  lower_domain:
    a_t: 0
    valid: true

  upper_domain:
    a_t: 1
    valid: true

  cooling_boundary:
    a_t: 0.90
    activate: false

  cooling_above:
    a_t: 0.91
    activate: true

  optimal_flow_lower:
    a_t: 0.4
    satisfies_visible_optimal_flow_arousal_component: true

  optimal_flow_upper:
    a_t: 0.7
    satisfies_visible_optimal_flow_arousal_component: true


DOMINANCE_TESTS:

  lower_domain:
    d_t: -1
    valid: true

  upper_domain:
    d_t: 1
    valid: true
```

---

# 44. Domain-Rejection Tests

If the vector specification is enforced literally:

```yaml
INVALID_VECTOR_EXAMPLES:

  valence_below_domain:
    E_t: "<-1.01, 0.5, 0>"
    result:
      OUT_OF_MODEL_DOMAIN

  valence_above_domain:
    E_t: "<1.01, 0.5, 0>"
    result:
      OUT_OF_MODEL_DOMAIN

  arousal_below_domain:
    E_t: "<0, -0.01, 0>"
    result:
      OUT_OF_MODEL_DOMAIN

  arousal_above_domain:
    E_t: "<0, 1.01, 0>"
    result:
      OUT_OF_MODEL_DOMAIN

  dominance_below_domain:
    E_t: "<0, 0.5, -1.01>"
    result:
      OUT_OF_MODEL_DOMAIN

  dominance_above_domain:
    E_t: "<0, 0.5, 1.01>"
    result:
      OUT_OF_MODEL_DOMAIN
```

The handling policy for such observations is not supplied.

---

# 45. Invariant Precedence Gap

The word `Invariant Bounds` suggests these rules have strong
architectural status.

However, the artifact does not explicitly define precedence between:

$$
a_t>0.90\Rightarrow Cooling
$$

and other cognitive-state policies.

Nor does it define precedence between:

$$
v_t<-0.70\Rightarrow SubstrateRefusal
$$

and the matrix's `Refusal Firewall`.

Thus precedence remains unresolved.

---

# 46. High-Information Conflict Test

A particularly important future test is:

```text
v_t < -0.70
AND
High-Threat matrix predicate satisfied
↓
Does EngageSubstrateRefusal:
    invoke Refusal Firewall?
    precede Refusal Firewall?
    compose with Refusal Firewall?
    represent the same underlying mechanism?
```

The current sources cannot discriminate.

---

# 47. Cooling Conflict Test

Likewise:

```text
a_t > 0.90
AND
Fatigue/Apathy predicate satisfied
↓
Does ActivateCoolingCircuit:
    trigger Metabolic Pacing?
    override it?
    compose with it?
    remain independent?
```

This remains `COMPETING`.

---

# 48. Dominance Discrimination Test

Because \(d_t\) is defined but absent from the visible matrix rows, a
high-information question for `UBI_EMOTION_BINDING` is whether
dominance affects:

- appraisal;
- target-plane routing;
- guard arbitration;
- refusal;
- autonomy;
- state transitions.

No answer should be invented before retrieval.

---

# 49. Runtime Schema

```yaml
UBI_EMOTION_STATE:

  timestamp:

  E_t:

    v_t:
      value:
      semantic: VALENCE
      domain: [-1, 1]

    a_t:
      value:
      semantic: AROUSAL
      domain: [0, 1]

    d_t:
      value:
      semantic: DOMINANCE
      domain: [-1, 1]

  invariants:

    cooling:
      predicate: "a_t > 0.90"
      active:

    substrate_refusal:
      predicate: "v_t < -0.70"
      active:

  matrix_state:

  target_plane:

  guard:

  provenance:

  freshness:

  calibration:

  regime:
```

This is **DERIVED** as an implementation-oriented representation.

---

# 50. Anti-Fabrication Contract

This specification MUST NOT by itself be used to claim:

1. NEI's full expansion is known;
1. NEI is empirically validated neuroscience;
1. \(v_t\), \(a_t\), and \(d_t\) are directly measurable biological quantities;
1. their numerical scales correspond to a standard external affective instrument;
1. the scales are universally calibrated;
1. `-1` valence has a universal empirical meaning;
1. `1` dominance has a universal empirical meaning;
1. (a_t>0.90) is a clinical threshold;
1. (v_t\<-0.70) is a clinical threshold;
1. Cooling Circuit is a literal physiological cooling mechanism;
1. Substrate Refusal is a literal biological refusal mechanism;
1. Substrate Refusal equals Refusal Firewall;
1. Cooling Circuit equals Metabolic Pacing;
1. Gamma Coherence Lock is part of Cooling Circuit;
1. dominance has an unspecified threshold;
1. the complete affective transition equation is known;
1. the cognitive appraisal function is known;
1. the matrix's missing first trigger variables are recovered;
1. the matrix's Target Plane values are recovered;
1. the three matrix states are mutually exclusive;
1. all invariant rules have precedence over all matrix rules;
1. the model applies universally to humans;
1. the model applies universally to AI systems;
1. affective values determine epistemic truth;
1. the source's constitutional-test status equals independent empirical validation.

---

# 51. Updated RSCF Relations

```yaml
RSCF_RELATIONS:

  - INDEXED_BY: ""

  - INDEXED_BY: ""

  - PART_OF: ""

  - COUNTERPART_OF: ""

  - BOUND_BY: ""

  - CONNECTED_TO: ""

  - DEFINES: AFFECTIVE_VECTOR

  - DEFINES: VALENCE_DIMENSION

  - DEFINES: AROUSAL_DIMENSION

  - DEFINES: DOMINANCE_DIMENSION

  - DEFINES: COOLING_CIRCUIT_INVARIANT

  - DEFINES: SUBSTRATE_REFUSAL_INVARIANT

  - RESOLVES:
      "v_t = VALENCE"

  - RESOLVES:
      "a_t = AROUSAL"

  - RESOLVES:
      "d_t = DOMINANCE"

  - RELATED_TO: ""

  - RELATED_TO: ""

  - RELATED_TO: ""

  - RELATED_TO: ""

  - RELATED_TO: ""

  - RELATED_TO: "K_CAUSAL_FIREWALL"

  - RELATED_TO: ""

  - RELATED_TO: ""

  - LINEAGE_TARGET: ""
```

---

# 52. RSCF Node

```yaml
RSCF_NODE:

  node_id:
    amos_25_cognitive_matrix_ubi_x_emotion

  node_type:
    matrix_spec

  path:
    25_COGNITIVE_MATRIX/UBI_X_EMOTION.md

  state:
    CANON_SPEC

  claim_class:
    AMOS_MODEL

  canonical_status:
    SOURCE_GROUNDED_CANON_CANDIDATE

  implementation_status:
    CONCEPTUAL_SOURCE_DEFINED

  validation_status:
    PASSED_CONSTITUTIONAL_TESTS

  executable_binding:
    ESTABLISHED

  H:

    identity:
      UBI_X_EMOTION

    role:
      >
        Mathematical specification for source-defined integration
        between NEI affective-state dynamics and cognitive appraisal
        mechanisms across AMOS OS.

  M:

    affective_vector:
      "<v_t, a_t, d_t>"

    dimensions:

      valence:
        range: [-1, 1]

      arousal:
        range: [0, 1]

      dominance:
        range: [-1, 1]

    invariants:

      cooling:
        "a_t > 0.90 => ActivateCoolingCircuit"

      substrate_refusal:
        "v_t < -0.70 => EngageSubstrateRefusal"

  L:

    retrieve:

      - UBI_EMOTION_BINDING
      - UNIFIED_BIOLOGICAL_INTELLIGENCE
      - executable_binding
      - constitutional_tests
      - runtime_traces

    raw_evidence:
      DO_NOT_LOAD_UNLESS_REQUIRED
```

---

# 53. Canonical Machine Representation

```yaml
UBI_X_EMOTION:

  identity:

    artifact:
      UBI_X_EMOTION.md

    artifact_id:
      amos_25_cognitive_matrix_ubi_x_emotion

    version:
      2.0.0

    origin_architect:
      Trang_Phan

    steward:
      Trang_Phan

    system:
      AMOS_OS

    plane:
      25_COGNITIVE_MATRIX

    artifact_kind:
      MATRIX_SPEC

    epistemic_class:
      AMOS_MODEL

  purpose:

    source_text:
      >
        Formalizes mathematical integration between affective
        state dynamics (NEI) and cognitive appraisal mechanisms
        across AMOS OS.

  affective_vector:

    symbol:
      E_t

    representation:
      "<v_t, a_t, d_t>"

    domain:
      "[-1,1] × [0,1] × [-1,1]"

    components:

      v_t:

        name:
          VALENCE

        description:
          HEDONIC_TONE

        domain:
          [-1, 1]

      a_t:

        name:
          AROUSAL

        description:
          METABOLIC_ACTIVATION

        domain:
          [0, 1]

      d_t:

        name:
          DOMINANCE

        description:
          AGENCY_AUTONOMY_SENSE

        domain:
          [-1, 1]

  invariant_bounds:

    HIGH_AROUSAL:

      predicate:
        "a_t > 0.90"

      action:
        ACTIVATE_COOLING_CIRCUIT

    NEGATIVE_VALENCE:

      predicate:
        "v_t < -0.70"

      action:
        ENGAGE_SUBSTRATE_REFUSAL

  bindings:

    matrix_counterpart:
      ""

    knowledge_binding:
      ""

    biological_master:
      ""

    cognitive_matrix_plane:
      ""

  unresolved:

    - NEI_FULL_DEFINITION
    - COGNITIVE_APPRAISAL_FUNCTION
    - AFFECTIVE_TRANSITION_FUNCTION
    - COOLING_CIRCUIT_IMPLEMENTATION
    - SUBSTRATE_REFUSAL_IMPLEMENTATION
    - REFUSAL_FIREWALL_RELATION
    - METABOLIC_PACING_RELATION
    - MATRIX_FIRST_TRIGGER_VARIABLES
    - MATRIX_TARGET_PLANES
    - MULTI_STATE_ARBITRATION
```

---

# 54. Canonical Compression

```text
             AFFECTIVE STATE — NEI
                      │
                      ▼
            E_t = <v_t,a_t,d_t>
                      │
       ┌──────────────┼──────────────┐
       ▼              ▼              ▼
    VALENCE        AROUSAL       DOMINANCE
   [-1,+1]          [0,1]         [-1,+1]
       │              │              │
       │              │              └─ Agency /
       │              │                 Autonomy
       │              │
       │              ├─ [0.4,0.7]
       │              │       ↓
       │              │   OPTIMAL FLOW
       │              │   COMPONENT
       │              │
       │              └─ > 0.90
       │                      ↓
       │               COOLING CIRCUIT
       │
       ├─ < -0.5
       │      ↓
       │  HIGH-THREAT
       │  COMPONENT
       │
       └─ < -0.70
              ↓
       SUBSTRATE REFUSAL
```

---

# 55. Final Canonical Candidate Statement

**UBI × Emotion Cognitive Matrix Specification v2.0.0** source-defines the AMOS affective-state representation:

$$
\boxed{
\vec E_t=
\langle
v_t,a_t,d_t
\rangle
\in
[-1,1]\times[0,1]\times[-1,1]
}
$$

where:

$$
\boxed{
v_t=\text{Valence / Hedonic tone}
}
$$

$$
\boxed{
a_t=\text{Arousal / Metabolic activation}
}
$$

$$
\boxed{
d_t=\text{Dominance / Agency-Autonomy sense}
}
$$

and establishes the invariant controls:

$$
\boxed{
a_t>0.90
\Rightarrow
ActivateCoolingCircuit
}
$$

$$
\boxed{
v_t<-0.70
\Rightarrow
EngageSubstrateRefusal
}
$$

This specification **resolves the semantic identity of \(v_t\) and
\(a_t\)** from the preceding `UBI_X_EMOTION_MATRIX`.

Consequently:

$$
v_t<-0.5
$$

in the High Threat / Anxiety matrix row can now be identified as a
**Valence** condition, while:

$$
a_t\in[0.4,0.7]
$$

in the Optimal Flow row can now be identified as an **Arousal**
condition.

The specification also reveals a second, stronger negative-valence
boundary:

$$
v_t<-0.70
$$

which engages `SubstrateRefusal`.

Because:

$$
v_t<-0.70\Rightarrow v_t<-0.5,
$$

the Substrate Refusal region is nested inside the High-Threat row's
visible valence region, although the complete High-Threat predicate
still depends on its missing first variable.

Likewise:

$$
a_t\in[0.4,0.7]
$$

and:

$$
a_t>0.90
$$

are disjoint. Therefore the visible Optimal-Flow arousal condition and
the Cooling Circuit condition cannot simultaneously hold for the same
\(a_t\).

The specification **does not resolve** the three missing first trigger
variables or the three missing Target Plane cells in
`UBI_X_EMOTION_MATRIX`.

It also does not establish that:

$$
EngageSubstrateRefusal
=
RefusalFirewall
$$

or that:

$$
ActivateCoolingCircuit
=
MetabolicPacing.
$$

Those remain competing architectural hypotheses pending
``.

The updated smallest sufficient retrieval path is therefore:

$$
\boxed{
UBI\_X\_EMOTION
\rightarrow
UBI\_EMOTION\_BINDING
\rightarrow
UNIFIED\_BIOLOGICAL\_INTELLIGENCE
\ \text{only if required}
}
$$

with raw evidence remaining:

`DO_NOT_LOAD_UNLESS_REQUIRED`.

The central canonical compression is:

$$
\boxed{
\vec E_t
=
\langle
Valence,
Arousal,
Dominance
\rangle
}
$$

$$
\boxed{
AffectiveState
\rightarrow
CognitiveAppraisal
+
InvariantGuards
}
$$

while preserving:

$$
\boxed{
AMOS\ Model
\neq
Universal\ Empirical\ Law
}
$$

$$
\boxed{
SubstrateRefusal
\neq_{\text{unproven}}
RefusalFirewall
}
$$

$$
\boxed{
CoolingCircuit
\neq_{\text{unproven}}
MetabolicPacing
}
$$

and:

$$
\boxed{
Recovered\ Semantics
\neq
PermissionToInventRemainingCanon
}
$$

---

**MOC:** [[25_COGNITIVE_MATRIX_MOC]]

**Counterpart:** [[UBI_X_EMOTION_MATRIX]]

**Next dependency:** [[UBI_EMOTION_BINDING]]

---

**END OF `UBI_X_EMOTION.md`**
