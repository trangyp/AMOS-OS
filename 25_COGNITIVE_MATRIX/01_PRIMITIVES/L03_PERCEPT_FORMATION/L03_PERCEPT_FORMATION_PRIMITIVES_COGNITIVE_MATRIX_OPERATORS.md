---
type: cognitive
source: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L03_PERCEPT_FORMATION
tags:
- amos
- cognitive-matrix
- l03
- percept-formation
- operators
- rscf
- provenance
- hml
- governance
- canon/cognitive-matrix
title: L03_PERCEPT_FORMATION — Operators
origin_architect: Trang Phan
status: MODEL_OPERATOR_CONTRACT / UNIMPLEMENTED / UNVALIDATED
epistemic_class: MODEL
runtime_alignment: AMOS Full Brain OS / AMOS_CORE v4.4 lineage
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


# L03_PERCEPT_FORMATION — Operators

**Class:** `COGNITIVE_PRIMITIVE_OPERATOR_CONTRACT`
**Origin architect / steward:** Trang Phan
**Primitive:** `L03_PERCEPT_FORMATION`
**Artifact:** `OPERATORS.md`
**Status:** `AMOS_MODEL / UNIMPLEMENTED / UNVALIDATED`

> **Source boundary:** The AMOS Information Operator Engine treats information operators as structural transformations unless a domain-specific mechanism is independently established. Its source-aligned workflow requires explicit input state, target state, representation, minimal operator selection, ordered application, invariant tracking, information-loss/reversibility tracking, invalid-composition detection, and an explicit operator trace with output state and failure conditions.

---

# 0. Purpose

Define the operator contract for `L03_PERCEPT_FORMATION`.

L03 operators transform admissible observation- and attention-conditioned state into structured percept candidates while preserving:

```text
input identity
representation type
observation ancestry
operator ordering
scope
regime
observer context
time
modality
provenance
uncertainty
H/M/L position
reversibility
information loss
competing percepts
authority boundaries
```

The operator layer answers:

> **What transformations may occur during percept formation, in what order, under what preconditions, with what outputs, what information may be lost or introduced, and what must remain invariant?**

Core boundary:

```text
OPERATOR != EMPIRICAL MECHANISM

TRANSFORMATION != CAUSATION

OPERATOR AVAILABLE != OPERATOR EXECUTED

OPERATOR EXECUTED != RESULT VALIDATED

VALID RESULT != AUTHORIZED COMMIT
```

---

# 1. Source / Canon References

## 1.1 Source-aligned operator requirements

The AMOS Information Operator Engine requires the following operator discipline:

```text
1. define input state
2. define target state
3. define representation
4. select only necessary operators
5. apply operators in explicit order
6. track invariants
7. track information loss
8. track reversibility
9. detect invalid compositions
10. expose hidden assumptions
11. emit operator trace
12. emit failure conditions
```

Information operators remain structural transformations unless a domain-specific mechanism is independently established.

## 1.2 Related AMOS architecture

Relevant supporting architecture includes:

```text
AMOS Full Brain OS
AMOS Cognition architecture
AMOS Information Operator Engine
AMOS Multimodal Perception Layer
AMOS Binding architecture
AMOS Cross-Scale H/M/L architecture
AMOS RSCF
AMOS provenance topology
AMOS constraint propagation
AMOS infrastructure control plane
AMOS_CORE v3.0 → v4.4 lineage
```

## 1.3 Direct L03 operator canon status

```yaml
canonical_L03_operator_registry: UNKNOWN_GAP
canonical_operator_names: UNKNOWN_GAP
canonical_operator_signatures: UNKNOWN_GAP
canonical_operator_ordering: UNKNOWN_GAP
canonical_operator_preconditions: UNKNOWN_GAP
canonical_operator_postconditions: UNKNOWN_GAP
canonical_operator_composition_rules: UNKNOWN_GAP
canonical_operator_reversibility: UNKNOWN_GAP
canonical_runtime_operators: UNKNOWN_GAP
```

Therefore, L03-specific operators below are `AMOS_MODEL` unless explicitly identified as generic source-aligned operator principles.

---

# 2. Definition and Scope

An L03 operator is a typed transformation:

[
\mathcal O_i :
(X,\Gamma)
\rightarrow
(Y,\Delta)
]

where:

```text
X = typed input state
Γ = context / constraints / operator parameters
Y = typed output state
Δ = trace metadata, provenance, loss, uncertainty,
    dependencies, reversibility state, failures
```

An operator must define:

```yaml
OperatorContract:
  id: string
  name: string
  class: string

  input_type: TypeRef[]
  output_type: TypeRef[]

  preconditions: []
  postconditions: []

  invariants_preserved: []
  invariants_checked: []

  dependencies: []

  scope: null
  regime: null
  observer: null

  information_loss:
    type:
      - NONE
      - LOSSLESS_REPRESENTATIONAL
      - LOSSY
      - UNKNOWN

  reversibility:
    type:
      - REVERSIBLE
      - CONDITIONALLY_REVERSIBLE
      - IRREVERSIBLE
      - UNKNOWN

  provenance_effect: null

  uncertainty_effect: null

  authority_required: null

  falsifiers: []

  implementation_status:
    type:
      - MODEL
      - ADDRESSABLE
      - IMPLEMENTED
      - VALIDATED
      - UNKNOWN_GAP
```

---

# 3. Typed Inputs

```yaml
L03OperatorInput:

  observations:
    type: ObservationRef[]

  attention_state:
    type: AttentionStateRef

  feature_state:
    type: FeatureState[]

  binding_state:
    type: BindingState[]

  percept_candidates:
    type: PerceptCandidate[]

  modality_state:
    type: ModalityAvailability

  temporal_context:
    type: TemporalContext

  spatial_context:
    type: SpatialContext | null

  observer_context:
    type: ObserverContext

  memory_context:
    type: MemoryContext | null

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeRef

  freshness:
    type: FreshnessState

  constraints:
    type: ConstraintSet

  provenance:
    type: ProvenanceBundle

  dependencies:
    type: DependencyGraph

  hml:
    type: HMLContext

  authority:
    type: AuthorityContext
```

---

# 4. Typed Outputs

```yaml
L03OperatorOutput:

  transformed_state:
    type: PerceptFormationState

  percept_candidates:
    type: PerceptCandidate[]

  competing_percepts:
    type: CompetingPercept[]

  operator_trace:
    type: OperatorTrace

  dependencies_added:
    type: DependencyEdge[]

  dependencies_removed:
    type: DependencyEdge[]

  provenance_delta:
    type: ProvenanceDelta

  information_loss:
    type: InformationLossReport

  reversibility:
    type: ReversibilityReport

  uncertainty_delta:
    type: UncertaintyDelta

  confidence_ceiling:
    type: ConfidenceBound

  failures:
    type: OperatorFailure[]

  status:
    type:
      - PASS
      - CONDITIONAL
      - COMPETING
      - FAIL
      - UNKNOWN_GAP

  proposal:
    type: PerceptStateProposal | null

  commit_authority:
    type: NONE
```

---

# 5. State Variables

```text
O_t       = admitted observation state
A_t       = attention state
F_t       = feature state
B_t       = binding state
P_t       = percept candidate state
Comp_t    = competing percept state

M_t       = modality state
T_t       = temporal context
X_t       = spatial context
ObsCtx_t  = observer context
Mem_t     = admissible memory context

Scope_t   = scope
Reg_t     = regime
Fresh_t   = freshness
Prov_t    = provenance topology
Dep_t     = dependency graph
U_t       = uncertainty
Conf_t    = confidence ceiling

Op_t      = operator registry
Trace_t   = operator trace
Loss_t    = information-loss state
Rev_t     = reversibility state
Gap_t     = unresolved gaps
```

Candidate composite:

[
S_t^{L03}
=========

(
O_t,A_t,F_t,B_t,P_t,Comp_t,
M_t,T_t,X_t,ObsCtx_t,Mem_t,
Scope_t,Reg_t,Fresh_t,
Prov_t,Dep_t,U_t,Conf_t
)
]

---

# 6. Operator Classes

Candidate operator taxonomy:

```text
ADMISSION
NORMALIZATION
SELECTION
EXTRACTION
DISTINCTION
RELATION
GROUPING
BINDING
PARTITION
TEMPORAL_ALIGNMENT
SPATIAL_ALIGNMENT
MULTIMODAL_ALIGNMENT
CONTEXTUALIZATION
COMBINATION
SEPARATION
INVERSION
ORDERING
THRESHOLDING
PROPAGATION
UPDATE
HYPOTHESIS_GENERATION
COMPARISON
DISCRIMINATION
AGGREGATION
DECOMPOSITION
CONSTRAINT
VALIDATION
INVALIDATION
QUARANTINE
REPAIR
REVALIDATION
PROPOSAL
```

Not every L03 runtime needs every operator.

Source-aligned principle:

```text
SELECT ONLY OPERATORS REQUIRED
FOR THE TRANSFORMATION
```

---

# 7. OP-L03-001 — `ADMIT_OBSERVATION`

Purpose:

> Determine whether an observation is eligible to enter L03 percept processing.

Signature:

[
ADMIT_OBSERVATION :
Observation
\rightarrow
AdmittedObservation ;|; Reject
]

Preconditions:

```text
valid type
known epistemic class
scope known or explicitly UNKNOWN
provenance sufficient for declared use
modality state known where required
```

Postconditions:

```text
observation identity preserved
no new percept semantics introduced
```

Hard boundary:

```text
ADMITTED != TRUE
```

---

# 8. OP-L03-002 — `NORMALIZE_OBSERVATION`

Purpose:

> Convert heterogeneous observations into a compatible processing representation.

Signature:

[
NORMALIZE(O,R_s,R_t)
\rightarrow
O'
]

where \(R_s\) and \(R_t\) are source and target representations.

Invariant:

```text
SEMANTIC CONTENT MAY BE RE-ENCODED
BUT SOURCE IDENTITY MUST REMAIN RECOVERABLE
```

Information loss must be declared.

---

# 9. OP-L03-003 — `SELECT_ATTENDED`

Purpose:

> Select or weight observation state using L02 attention.

Signature:

[
SELECT(O,A)
\rightarrow
O^{att}
]

Hard boundaries:

```text
SELECTED != TRUE
UNSELECTED != FALSE
```

Attention modifies processing allocation, not epistemic status.

---

# 10. OP-L03-004 — `DISTINGUISH_FEATURE`

Purpose:

> Create an explicit distinction between perceptually relevant local states.

Signature:

[
DISTINGUISH(O,c)
\rightarrow
F
]

where (c) is the distinction criterion.

Examples:

```text
edge / non-edge
moving / stationary cue
token A / token B
pitch class difference
spatial boundary
```

Hard boundary:

```text
DISTINCTION != ENTITY
```

---

# 11. OP-L03-005 — `EXTRACT_FEATURE`

Purpose:

> Produce a typed feature representation from observation state.

Signature:

[
EXTRACT(O,\phi)
\rightarrow
F
]

Required trace:

```text
source observation
transformation function
parameters
output feature
loss
uncertainty
```

Hard invariant:

```text
FEATURE != INDEPENDENT OBSERVATION
```

when derived from one observation.

---

# 12. OP-L03-006 — `RELATE_FEATURES`

Purpose:

> Represent typed relations among features.

Signature:

[
RELATE(F_i,F_j,r)
\rightarrow
R_{ij}
]

Relation types may include:

```text
temporal
spatial
similarity
contrast
co-occurrence
continuity
containment
adjacency
cross-modal correspondence
```

Hard boundary:

```text
RELATION != CAUSAL EFFECT
```

unless independently evidenced.

---

# 13. OP-L03-007 — `GROUP_FEATURES`

Purpose:

> Form candidate groups without yet asserting object identity.

Signature:

[
GROUP({F_i},g)
\rightarrow
G
]

Hard invariant:

```text
GROUP != OBJECT
```

Group membership must retain individual feature identities where decision-relevant.

---

# 14. OP-L03-008 — `BIND_FEATURES`

Purpose:

> Propose that multiple features jointly support one percept candidate.

Signature:

[
BIND(F_{1:n},R,C)
\rightarrow
B
]

where:

```text
R = relations
C = contextual compatibility conditions
```

Preconditions may include:

```text
temporal compatibility
spatial compatibility
modality compatibility
scope compatibility
observer compatibility
```

Hard boundary:

```text
BINDING != IDENTITY PROOF
```

---

# 15. OP-L03-009 — `UNBIND_FEATURES`

Purpose:

> Reverse or dissolve a prior feature binding when evidence no longer supports it.

Signature:

[
UNBIND(B,e)
\rightarrow
{F_i}
]

where (e) identifies the invalidated binding basis.

Required:

```text
preserve original source features
preserve prior binding history
record reason for unbinding
```

---

# 16. OP-L03-010 — `PARTITION`

Purpose:

> Split one observation/feature collection into multiple candidate percept regions or hypotheses.

Signature:

[
PARTITION(X,\pi)
\rightarrow
{X_1,\ldots,X_n}
]

Information-loss status must be explicit.

Partitioning does not prove that the partitions correspond to real-world entities.

---

# 17. OP-L03-011 — `TEMPORAL_ALIGN`

Purpose:

> Place features/observations into a typed temporal relation.

Signature:

[
TEMPORAL_ALIGN(F_{1:n},T)
\rightarrow
A_T
]

Must distinguish:

```text
event time
observation time
processing time
retrieval time
```

Hard boundary:

```text
TEMPORAL ORDER != CAUSATION
```

---

# 18. OP-L03-012 — `SPATIAL_ALIGN`

Purpose:

> Align spatially typed observations or features within a declared coordinate frame.

Signature:

[
SPATIAL_ALIGN(F_{1:n},\mathcal F)
\rightarrow
A_X
]

where (\mathcal F) is the spatial frame.

If spatial state is unavailable:

```text
return UNKNOWN / NOT_AVAILABLE
```

not fabricated compatibility.

---

# 19. OP-L03-013 — `ALIGN_OBSERVER`

Purpose:

> Normalize or preserve observer-relative state before percept integration.

Signature:

[
ALIGN_OBSERVER(X,O_s,O_t)
\rightarrow
X'
]

Hard rule:

```text
OBSERVER TRANSFORM
MUST NOT SILENTLY REMOVE OBSERVER DEPENDENCE
```

---

# 20. OP-L03-014 — `ALIGN_MODALITIES`

Purpose:

> Align compatible representations across modalities.

Signature:

[
ALIGN_MODALITIES
(
X^{(1)},\ldots,X^{(k)}
)
\rightarrow
A_M
]

Precondition:

```text
modality identities known
availability masks known
representation mapping known or explicitly modeled
```

Hard boundaries:

```text
MULTIMODAL != INDEPENDENT

UNAVAILABLE MODALITY != NEGATIVE EVIDENCE
```

---

# 21. OP-L03-015 — `INTEGRATE_MODALITIES`

Purpose:

> Create a candidate multimodal percept representation from aligned modality evidence.

Signature:

[
INTEGRATE(A_M,C)
\rightarrow
P^{multi}
]

Required output:

```text
contributing modalities
missing modalities
conflicting modalities
shared provenance ancestry
confidence ceiling
```

Cross-modal conflict must not be silently removed.

---

# 22. OP-L03-016 — `CONTEXTUALIZE`

Purpose:

> Condition percept formation using admissible context without converting context into observation.

Signature:

[
CONTEXTUALIZE(P,C)
\rightarrow
P'
]

Possible context:

```text
scene context
task context
language context
memory context
observer context
historical context
```

Hard boundary:

```text
CONTEXT != OBSERVATION
```

---

# 23. OP-L03-017 — `COMBINE`

Purpose:

> Combine compatible percept components.

Signature:

[
COMBINE(X_1,\ldots,X_n,c)
\rightarrow
Y
]

Must track:

```text
component ancestry
combination rule
loss
irreversibility
confidence ceiling
```

Hard boundary:

```text
COMBINATION != INDEPENDENT CONFIRMATION
```

---

# 24. OP-L03-018 — `SEPARATE`

Purpose:

> Split a composite percept state when evidence indicates multiple structures.

Signature:

[
SEPARATE(P,s)
\rightarrow
{P_1,\ldots,P_n}
]

Required:

```text
preserve prior composite history
preserve source ancestry
do not duplicate evidence confidence
```

---

# 25. OP-L03-019 — `ORDER`

Purpose:

> Establish a typed ordering among percept features or events.

Signature:

[
ORDER(X,\prec)
\rightarrow
X'
]

Order can represent:

```text
temporal order
spatial order
priority order
processing order
containment order
```

Must not be confused across domains.

---

# 26. OP-L03-020 — `THRESHOLD`

Purpose:

> Apply a declared threshold to a typed percept quantity.

Signature:

[
THRESHOLD(x,\theta)
\rightarrow
class(x)
]

Preconditions:

```text
quantity semantics defined
threshold provenance known
scope known
regime known
```

Hard boundary:

```text
ARBITRARY THRESHOLD
!=
CANONICAL THRESHOLD
```

All numeric thresholds remain `UNKNOWN/GAP` unless sourced.

---

# 27. OP-L03-021 — `GENERATE_PERCEPT_CANDIDATE`

Purpose:

> Construct one bounded percept candidate from admissible inputs.

Signature:

[
GENERATE_PERCEPT
(
O^{att},
F,
B,
C
)
\rightarrow
P_i
]

Required fields:

```yaml
PerceptCandidate:
  percept_id: null
  observations: []
  features: []
  bindings: []
  context: []
  modality_state: null
  temporal_context: null
  spatial_context: null
  observer: null
  scope: null
  regime: null
  provenance: []
  uncertainty: null
  confidence_ceiling: null
  epistemic_class: MODEL
```

Hard boundary:

```text
GENERATED PERCEPT != FACT
```

---

# 28. OP-L03-022 — `GENERATE_COMPETING_PERCEPTS`

Purpose:

> Generate materially different interpretations where evidence supports more than one.

Signature:

[
GEN_COMPETING(X)
\rightarrow
\Omega
======

{P_1,\ldots,P_n}
]

Hard rule:

```text
ALTERNATIVE HYPOTHESES
MUST NOT BE REMOVED
MERELY FOR FLUENCY OR SIMPLICITY
```

---

# 29. OP-L03-023 — `COMPARE_PERCEPTS`

Purpose:

> Compare competing percept candidates without forcing convergence.

Signature:

[
COMPARE(P_i,P_j)
\rightarrow
Comparison
]

Comparison dimensions:

```text
supporting observations
contradicting observations
shared ancestry
scope
regime
observer
freshness
uncertainty
falsifiers
```

---

# 30. OP-L03-024 — `DISCRIMINATE`

Purpose:

> Identify evidence or tests capable of resolving competing percepts.

Signature:

[
DISCRIMINATE(\Omega,E)
\rightarrow
D
]

Output:

```text
candidate discriminator
expected hypothesis split
cost
information value
remaining ambiguity
```

If no discriminator is available:

```text
COMPETING remains
```

---

# 31. OP-L03-025 — `AGGREGATE_L_TO_M`

Purpose:

> Aggregate local percept state into a middle-scale object/event candidate.

Signature:

[
A_{L\rightarrow M}\(X_L\)
\rightarrow
X_M
]

Hard boundaries:

```text
AGGREGATION != IDENTITY
LOCAL CORRELATION != MACRO CAUSATION
```

Decision-relevant heterogeneity must remain recoverable.

---

# 32. OP-L03-026 — `AGGREGATE_M_TO_H`

Purpose:

> Aggregate middle-scale percepts into a high-level scene/global percept.

Signature:

[
A_{M\rightarrow H}\(X_M\)
\rightarrow
X_H
]

Hard boundary:

```text
HIGH-LEVEL COHERENCE != GLOBAL TRUTH
```

---

# 33. OP-L03-027 — `CONSTRAIN_H_TO_M`

Purpose:

> Apply high-level contextual constraints to middle-level candidate space.

Signature:

[
C_{H\rightarrow M}(X_H,X_M)
\rightarrow
X'_M
]

Hard boundary:

```text
DOWNWARD CONSTRAINT != DOWNWARD CAUSATION
```

---

# 34. OP-L03-028 — `CONSTRAIN_M_TO_L`

Purpose:

> Apply middle-level contextual constraints to interpretation of local features.

Signature:

[
C_{M\rightarrow L}(X_M,X_L)
\rightarrow
X'_L
]

Hard boundary:

```text
CONSTRAINT != OBSERVATION REWRITE
```

---

# 35. OP-L03-029 — `CHECK_PROVENANCE`

Purpose:

> Verify that a percept's ancestry is sufficiently known for its intended use.

Signature:

[
CHECK_PROVENANCE(P)
\rightarrow
PASS|CONDITIONAL|FAIL|UNKNOWN
]

Checks:

```text
semantic origin
source identity
transform lineage
ancestry collisions
correlation risk
version/freshness
```

---

# 36. OP-L03-030 — `CHECK_INDEPENDENCE`

Purpose:

> Determine whether multiple supporting items represent independent evidential ancestry.

Signature:

[
CHECK_INDEPENDENCE(e_i,e_j)
\rightarrow
INDEPENDENT|CORRELATED|UNKNOWN
]

Hard boundary:

```text
DIFFERENT FILE
DIFFERENT AGENT
DIFFERENT WORDING
DIFFERENT FEATURE
```

do not independently establish evidential independence.

---

# 37. OP-L03-031 — `CHECK_SCOPE`

Purpose:

> Verify that the percept remains inside the applicability envelope of load-bearing inputs.

Candidate:

[
Scope(P)
\subseteq
\bigcap_i Scope(d_i)
]

unless a validated scope-transfer operation exists.

---

# 38. OP-L03-032 — `CHECK_REGIME`

Purpose:

> Verify that supporting inputs and percept state share a compatible regime.

Signature:

[
CHECK_REGIME(P,R_t)
\rightarrow
PASS|REVALIDATE|FAIL|UNKNOWN
]

---

# 39. OP-L03-033 — `CHECK_FRESHNESS`

Purpose:

> Determine whether load-bearing evidence remains sufficiently current.

Hard rule:

```text
NEW COMPUTATION != NEW EVIDENCE
```

A stale input cannot be made fresh simply by rerunning an operator.

---

# 40. OP-L03-034 — `PROPAGATE_UNCERTAINTY`

Purpose:

> Carry material uncertainty through percept dependencies.

Signature:

[
U(P)
====

PROPAGATE(U(d_1),\ldots,U(d_n))
]

No canonical scalarization is asserted.

Hard boundary:

```text
UNCERTAINTY PROPAGATION
MUST NOT SILENTLY DROP MATERIAL DIMENSIONS
```

---

# 41. OP-L03-035 — `CALCULATE_CONFIDENCE_CEILING`

Purpose:

> Bound percept confidence by its load-bearing premises.

Candidate:

[
Conf(P)
\le
\min_{d\in LB(P)} Conf(d)
]

unless independent revalidation establishes a stronger path.

Hard rule:

```text
AGGREGATION
REPETITION
AGENT CONSENSUS
```

cannot independently raise the ceiling.

---

# 42. OP-L03-036 — `PRESERVE_COMPETING`

Purpose:

> Prevent unresolved percept hypotheses from being prematurely collapsed.

Signature:

[
PRESERVE_COMPETING(\Omega)
\rightarrow
\Omega'
]

where unresolved material alternatives remain explicitly represented.

---

# 43. OP-L03-037 — `INVALIDATE_DEPENDENT`

Purpose:

> Invalidate only states dependent on a failed premise.

Candidate:

[
INVALIDATE(d)
\rightarrow
Desc_{LB}(d)
]

Hard boundary:

```text
LOCAL FAILURE != GLOBAL RESET
```

unless dependency closure establishes global impact.

---

# 44. OP-L03-038 — `QUARANTINE`

Purpose:

> Isolate uncertain or structurally invalid state without deleting it.

Signature:

[
QUARANTINE(X,reason)
\rightarrow
Q(X)
]

Use when:

```text
provenance unknown
scope uncertain
contradiction unresolved
memory contamination suspected
operator chain invalid
```

Quarantine is reversible by revalidation.

---

# 45. OP-L03-039 — `REPAIR`

Purpose:

> Correct an invalid percept transformation, binding, dependency, or metadata state while preserving valid evidence.

Signature:

[
REPAIR(P,E_{bad},E_{new})
\rightarrow
P'
]

Hard boundaries:

```text
REPAIR != EVIDENCE REWRITE

REPAIR != REVALIDATION
```

---

# 46. OP-L03-040 — `REVALIDATE`

Purpose:

> Re-run required validation after repair, freshness change, regime change, or dependency mutation.

Signature:

[
REVALIDATE(P,t)
\rightarrow
Status(P,t)
]

Possible status:

```text
VALID
CONDITIONAL
COMPETING
INVALID
UNKNOWN/GAP
```

---

# 47. OP-L03-041 — `PROPOSE_STATE`

Purpose:

> Package validated cognitive results into a state proposal.

Signature:

[
PROPOSE_STATE(P,D,Prov,U)
\rightarrow
Proposal
]

Hard boundary:

```text
PROPOSAL != COMMIT
```

---

# 48. Operator Ordering

Candidate default sequence:

```text
ADMIT_OBSERVATION
↓
NORMALIZE_OBSERVATION
↓
SELECT_ATTENDED
↓
DISTINGUISH / EXTRACT_FEATURE
↓
RELATE_FEATURES
↓
TEMPORAL_ALIGN / SPATIAL_ALIGN / ALIGN_OBSERVER
↓
ALIGN_MODALITIES
↓
GROUP / BIND
↓
CONTEXTUALIZE
↓
GENERATE_PERCEPT_CANDIDATE
↓
GENERATE_COMPETING_PERCEPTS
↓
COMPARE / DISCRIMINATE
↓
AGGREGATE H/M/L WHERE REQUIRED
↓
CHECK_PROVENANCE
↓
CHECK_INDEPENDENCE
↓
CHECK_SCOPE
↓
CHECK_REGIME
↓
CHECK_FRESHNESS
↓
PROPAGATE_UNCERTAINTY
↓
CALCULATE_CONFIDENCE_CEILING
↓
PRESERVE_COMPETING
↓
PROPOSE_STATE
↓
CONTROL-PLANE VALIDATION
```

This is `AMOS_MODEL`.

Not every problem requires every operator.

Source-aligned principle:

```text
USE THE SMALLEST SUFFICIENT OPERATOR CHAIN
```

---

# 49. Operator Composition

Let:

[
\mathcal O
==========

O_n\circ O_{n-1}\circ\dots\circ O_1
]

A composition is admissible only when:

```text
output type of O_i
is compatible with
input type of O_(i+1)
```

and all load-bearing invariants remain valid.

Candidate:

[
Admissible(O_j\circ O_i)
========================

TypeCompatible
\land
InvariantCompatible
\land
ScopeCompatible
\land
RegimeCompatible
]

`AMOS_MODEL`.

---

# 50. Invalid Operator Compositions

Examples:

```text
THRESHOLD before variable semantics defined

BIND before temporal/spatial compatibility check where required

AGGREGATE before provenance lineage established

COMMIT immediately after GENERATE_PERCEPT

REPAIR without identifying failed dependency

REVALIDATE without changed evidence after identical failed path

MEMORY RETRIEVAL → OBSERVATION without epistemic conversion boundary
```

Invalid compositions must produce:

```text
FAIL
or
UNKNOWN/GAP
```

not implicit repair.

---

# 51. Information-Loss Contract

Every lossy operator must report:

```yaml
InformationLossReport:

  operator_id: null

  input_information_classes: []
  retained_information_classes: []
  discarded_information_classes: []

  decision_relevant_loss:
    type: boolean

  recoverable:
    type: boolean

  recovery_reference: null

  impact_on_confidence: null

  impact_on_falsifiability: null
```

Hard rule:

```text
LOSSY TRANSFORM
MUST NOT CLAIM LOSSLESS REVERSIBILITY
```

---

# 52. Reversibility Contract

Operator reversibility classes:

```text
REVERSIBLE
CONDITIONALLY_REVERSIBLE
IRREVERSIBLE
UNKNOWN
```

Examples:

```text
GROUP
often conditionally reversible if members retained

BIND
reversible if source members and relation graph retained

AGGREGATE
may be lossy unless lower-level state remains recoverable

COMMIT
may be irreversible or externally consequential
```

L03 cognitive operators should prefer reversible representations where practical.

---

# 53. Operator Trace

Required candidate trace:

```yaml
OperatorTrace:

  trace_id: null

  initial_state_ref: null

  steps:

    - operator_id: null
      input_refs: []
      parameters: {}
      preconditions: []
      precondition_results: []

      output_refs: []

      provenance_delta: null
      dependency_delta: null

      information_loss: null
      reversibility: null

      uncertainty_delta: null
      confidence_ceiling: null

      invariant_results: []

      status: null

  final_state_ref: null

  unresolved_gaps: []

  failures: []
```

This directly follows the source operator principle that explicit operator ordering, invariant preservation, loss, reversibility, and failure conditions must be traceable.

---

# 54. Core Operator Invariants

```text
L03-OP-INV-001
Every material transformation must name its operator.

L03-OP-INV-002
Every operator must declare typed inputs and outputs.

L03-OP-INV-003
Every operator must declare preconditions.

L03-OP-INV-004
Every operator must declare postconditions.

L03-OP-INV-005
Operator order must be explicit when order changes semantics.

L03-OP-INV-006
Operator execution must preserve source ancestry.

L03-OP-INV-007
Lossy transformations must expose information loss.

L03-OP-INV-008
Irreversible transformations must not be represented as reversible.

L03-OP-INV-009
Structural transformations do not establish domain causal mechanisms.

L03-OP-INV-010
Observation remains distinct from percept.

L03-OP-INV-011
Attention selection remains distinct from truth.

L03-OP-INV-012
Feature extraction does not create independent evidence.

L03-OP-INV-013
Binding does not prove identity.

L03-OP-INV-014
Temporal ordering does not prove causation.

L03-OP-INV-015
Aggregation does not prove identity or global truth.

L03-OP-INV-016
Downward constraint does not establish downward causation.

L03-OP-INV-017
Context cannot manufacture observation.

L03-OP-INV-018
Unavailable modality cannot become negative evidence.

L03-OP-INV-019
Correlated provenance cannot become independent confirmation.

L03-OP-INV-020
Decision-relevant heterogeneity must survive aggregation.

L03-OP-INV-021
Scope propagates through transformation.

L03-OP-INV-022
Regime propagates through transformation.

L03-OP-INV-023
Observer context propagates through transformation.

L03-OP-INV-024
Freshness propagates through load-bearing dependencies.

L03-OP-INV-025
Confidence cannot exceed weakest unresolved load-bearing premise.

L03-OP-INV-026
COMPETING state cannot be collapsed without discriminating evidence.

L03-OP-INV-027
UNKNOWN/GAP cannot satisfy a hard gate.

L03-OP-INV-028
Invalidation propagates only through dependency-connected descendants.

L03-OP-INV-029
Repair must not alter valid source evidence merely to preserve a percept.

L03-OP-INV-030
Repair requires revalidation.

L03-OP-INV-031
Operator capability does not grant authority.

L03-OP-INV-032
Operator completion does not equal state commit.
```

---

# 55. Dependencies

Upstream:

```text
L01_SENSING_OBSERVATION
L02_ATTENTION
```

Internal L03 dependencies:

```text
L03_PERCEPT_FORMATION/DEFINITION
L03_PERCEPT_FORMATION/VARIABLES
L03_PERCEPT_FORMATION/STATE
L03_PERCEPT_FORMATION/INVARIANTS
L03_PERCEPT_FORMATION/DEPENDENCIES
L03_PERCEPT_FORMATION/EQUATIONS
L03_PERCEPT_FORMATION/HML
L03_PERCEPT_FORMATION/MEMORY
L03_PERCEPT_FORMATION/PROVENANCE
L03_PERCEPT_FORMATION/FAILURE_MODES
L03_PERCEPT_FORMATION/REPAIR
L03_PERCEPT_FORMATION/CONTROL_PLANES
L03_PERCEPT_FORMATION/TESTS
```

Cross-cutting:

```text
AMOS Information Operator Engine
AMOS RSCF
AMOS provenance controls
AMOS binding architecture
AMOS cross-scale H/M/L architecture
AMOS constraint propagation
AMOS infrastructure control plane
```

---

# 56. H/M/L Applicability

## L — Local operators

```text
ADMIT_OBSERVATION
NORMALIZE_OBSERVATION
DISTINGUISH_FEATURE
EXTRACT_FEATURE
RELATE_FEATURES
TEMPORAL_ALIGN
SPATIAL_ALIGN
ALIGN_OBSERVER
```

Operate mainly on:

```text
individual observations
features
timestamps
local relations
```

## M — Middle operators

```text
GROUP_FEATURES
BIND_FEATURES
UNBIND_FEATURES
PARTITION
ALIGN_MODALITIES
INTEGRATE_MODALITIES
GENERATE_PERCEPT_CANDIDATE
COMPARE_PERCEPTS
```

Operate mainly on:

```text
objects
events
multimodal groups
subsystem percepts
```

## H — High operators

```text
AGGREGATE_M_TO_H
CONSTRAIN_H_TO_M
PRESERVE_COMPETING
CHECK_SCOPE
CHECK_REGIME
PROPOSE_STATE
```

Operate mainly on:

```text
scene/global percepts
governing context
cross-object consistency
```

## Cross-scale

```text
AGGREGATE_L_TO_M
AGGREGATE_M_TO_H
CONSTRAIN_H_TO_M
CONSTRAIN_M_TO_L
INVALIDATE_DEPENDENT
REVALIDATE
```

Cross-scale operators must preserve provenance and typed scale transitions.

---

# 57. Control-Plane Requirements

L03 operators may transform cognitive state and emit proposals.

They should not own durable authority by default.

Control plane should govern:

```text
operator allow-list
capability manifest
state version/freshness
operator preconditions
constraint context
read-set identity
authority
commit effect
rollback
audit trace
```

Candidate:

```text
COGNITIVE OPERATOR
→ PROPOSED STATE

CONTROL PLANE
→ VALIDATION

AUTHORITY
→ EFFECT ELIGIBILITY

COMMIT
→ DURABLE STATE
```

Hard rule:

```text
OPERATOR INVOCATION
!=
AUTHORITY TO COMMIT
```

---

# 58. Agents

Candidate operator-related roles:

```text
L03_OPERATOR_COORDINATOR
L03_OPERATOR_SELECTOR
L03_FEATURE_OPERATOR_AGENT
L03_BINDING_OPERATOR_AGENT
L03_MULTIMODAL_OPERATOR_AGENT
L03_HML_OPERATOR_AGENT
L03_OPERATOR_TRACE_AUDITOR
L03_OPERATOR_INVARIANT_AUDITOR
L03_OPERATOR_REPAIR_AGENT
```

These are `AMOS_MODEL` roles.

No implemented-agent claim is made.

---

# 59. Skills

Relevant capability families:

```text
AMOS Information Operator Engine
AMOS Multimodal Perception Layer
AMOS Binding RSCF Engine
AMOS Cross-Scale RSCF Tensor Engine
AMOS Temporal Multi-Scale RSCF Engine
AMOS Constraint Propagation RSCF Engine
AMOS Provenance Trust Firewall
AMOS Mathematical Rigor RSCF Kernel
AMOS Infrastructure Control Plane
RSCF Modeler
```

Hard boundary:

```text
SKILL AVAILABLE
!=
OPERATOR IMPLEMENTED

OPERATOR IMPLEMENTED
!=
OPERATOR VALIDATED
```

---

# 60. Workflow

Source-aligned operator workflow:

```text
DEFINE INPUT STATE
↓
DEFINE TARGET STATE
↓
DEFINE REPRESENTATION
↓
SELECT MINIMUM REQUIRED OPERATORS
↓
CHECK PRECONDITIONS
↓
EXECUTE IN EXPLICIT ORDER
↓
TRACK INVARIANTS
↓
TRACK INFORMATION LOSS
↓
TRACK REVERSIBILITY
↓
DETECT INVALID COMPOSITIONS
↓
DETECT HIDDEN ASSUMPTIONS
↓
EMIT OPERATOR TRACE
↓
EMIT OUTPUT + FAILURE CONDITIONS
```

L03 specialization:

```text
RECEIVE ATTENDED OBSERVATION STATE
↓
ADMIT + NORMALIZE
↓
DISTINGUISH / EXTRACT
↓
RELATE / ALIGN
↓
GROUP / BIND
↓
CONTEXTUALIZE
↓
GENERATE PERCEPT CANDIDATES
↓
PRESERVE ALTERNATIVES
↓
AGGREGATE H/M/L IF REQUIRED
↓
CHECK PROVENANCE / INDEPENDENCE
↓
CHECK SCOPE / REGIME / FRESHNESS
↓
PROPAGATE UNCERTAINTY
↓
APPLY CONFIDENCE CEILING
↓
TRACE OPERATORS
↓
PROPOSE STATE
```

---

# 61. Protocols

Candidate operator protocol surface:

```text
L03_OP_REGISTER
L03_OP_DISCOVER
L03_OP_SELECT

L03_OP_PRECONDITION_CHECK
L03_OP_EXECUTE
L03_OP_RESULT

L03_OP_TRACE_APPEND

L03_OP_INVARIANT_FAIL
L03_OP_INFORMATION_LOSS_NOTICE
L03_OP_IRREVERSIBILITY_NOTICE

L03_OP_QUARANTINE
L03_OP_INVALIDATE
L03_OP_REPAIR
L03_OP_REVALIDATE

L03_OP_STATE_PROPOSAL
```

Canonical protocol names remain `UNKNOWN/GAP`.

---

# 62. Evidence / Provenance

Every operator result should preserve:

```yaml
OperatorEvidence:

  operator_id: null
  operator_version: null

  execution_id: null

  input_refs: []
  output_refs: []

  parameter_refs: []

  parent_trace_id: null

  source_ancestry: []
  semantic_origins: []

  dependency_reads: []
  dependency_writes: []

  scope: null
  regime: null
  observer: null

  execution_time: null

  information_loss: null
  reversibility: null

  uncertainty_before: null
  uncertainty_after: null

  confidence_before: null
  confidence_after: null

  validator_results: []

  failures: []
```

---

# 63. Uncertainty and Confidence Ceiling

Operator uncertainty may arise from:

```yaml
operator_uncertainty:

  input:
    description: uncertainty in input state

  transformation:
    description: uncertainty in operator semantics

  parameters:
    description: uncertain configuration/threshold

  representation:
    description: uncertainty from representation mapping

  provenance:
    description: uncertain ancestry

  scope:
    description: applicability uncertainty

  regime:
    description: runtime/regime uncertainty

  loss:
    description: uncertain information loss

  reversibility:
    description: uncertainty about recovery

  execution:
    description: runtime execution uncertainty
```

Candidate propagation:

[
Conf(Output)
\le
\min
(
Conf(Input),
Conf(Operator),
Conf(Parameters),
Conf(Context)
)
]

for unresolved load-bearing components.

`AMOS_MODEL`.

No confidence increase is licensed merely because many operators have been applied.

---

# 64. Failure Modes

```text
FM-L03-OP-001
Operator receives wrong input type.

FM-L03-OP-002
Operator emits wrong output type.

FM-L03-OP-003
Required precondition omitted.

FM-L03-OP-004
Operator ordering changes semantics but order is not recorded.

FM-L03-OP-005
Operator chain loses source ancestry.

FM-L03-OP-006
Lossy transform described as lossless.

FM-L03-OP-007
Irreversible operator described as reversible.

FM-L03-OP-008
Attention-selection operator changes truth status.

FM-L03-OP-009
Feature extraction creates false independent evidence.

FM-L03-OP-010
Binding promotes candidate to identity proof.

FM-L03-OP-011
Temporal alignment becomes causal claim.

FM-L03-OP-012
Missing spatial state becomes false spatial agreement.

FM-L03-OP-013
Observer alignment erases observer dependence.

FM-L03-OP-014
Multimodal integration suppresses material conflict.

FM-L03-OP-015
Contextualization overwrites observation.

FM-L03-OP-016
Combination double-counts correlated ancestry.

FM-L03-OP-017
Partition duplicates confidence/evidence.

FM-L03-OP-018
Threshold used without threshold provenance.

FM-L03-OP-019
Percept candidate promoted directly to fact.

FM-L03-OP-020
Competing percepts forced to converge.

FM-L03-OP-021
H/M/L aggregation erases decision-relevant heterogeneity.

FM-L03-OP-022
Downward constraint becomes causal assertion.

FM-L03-OP-023
Scope lost in operator chain.

FM-L03-OP-024
Regime lost in operator chain.

FM-L03-OP-025
Freshness lost in operator chain.

FM-L03-OP-026
Confidence rises above weakest load-bearing premise.

FM-L03-OP-027
UNKNOWN/GAP satisfies hard gate.

FM-L03-OP-028
Invalidation spreads beyond true descendants.

FM-L03-OP-029
Failed descendant remains valid after load-bearing premise invalidation.

FM-L03-OP-030
Repair alters valid source evidence to preserve percept.

FM-L03-OP-031
Repair marked valid without revalidation.

FM-L03-OP-032
Operator availability represented as implementation.

FM-L03-OP-033
Operator execution represented as empirical validation.

FM-L03-OP-034
Operator capability represented as authority.

FM-L03-OP-035
Proposal operator treated as commit.
```

---

# 65. Repair / Recovery

Operator repair workflow:

```text
DETECT OPERATOR FAILURE
↓
IDENTIFY FAILED OPERATOR
↓
IDENTIFY INPUT STATE
↓
IDENTIFY PRECONDITION VIOLATION
↓
TRACE OPERATOR DESCENDANTS
↓
FREEZE AFFECTED STATE
↓
PRESERVE VALID SOURCE INPUTS
↓
PRESERVE UNAFFECTED BRANCHES
↓
REPAIR:
  operator semantics
  parameter
  ordering
  representation mapping
  dependency edge
  provenance edge
↓
REEXECUTE FROM NEAREST VALID STATE
↓
RECHECK INFORMATION LOSS
↓
RECHECK REVERSIBILITY
↓
RECHECK INVARIANTS
↓
RECALCULATE UNCERTAINTY / CONFIDENCE
↓
REVALIDATE DESCENDANTS
↓
PROPOSE RECOVERED STATE
```

Hard recovery rule:

```text
DO NOT REPEAT IDENTICAL FAILED OPERATOR PATH
WITHOUT CHANGED EVIDENCE, STATE, PARAMETER,
OR TRANSFORMATION SEMANTICS
```

---

# 66. Tests / Validators

Minimum validators:

```text
VALIDATE_OPERATOR_REGISTRY
VALIDATE_OPERATOR_INPUT_TYPES
VALIDATE_OPERATOR_OUTPUT_TYPES
VALIDATE_PRECONDITIONS
VALIDATE_POSTCONDITIONS
VALIDATE_OPERATOR_ORDER
VALIDATE_OPERATOR_COMPOSITION
VALIDATE_INFORMATION_LOSS
VALIDATE_REVERSIBILITY
VALIDATE_PROVENANCE_PRESERVATION
VALIDATE_DEPENDENCY_DELTA
VALIDATE_SCOPE_PROPAGATION
VALIDATE_REGIME_PROPAGATION
VALIDATE_OBSERVER_PROPAGATION
VALIDATE_CONFIDENCE_CEILING
VALIDATE_COMPETING_PRESERVATION
VALIDATE_HML_OPERATOR_MAPPING
VALIDATE_REPAIR
VALIDATE_REVALIDATION
VALIDATE_AUTHORITY_BOUNDARY
VALIDATE_UNKNOWN_NOT_PASS
```

Conceptual tests:

```text
TEST-L03-OP-001
Run EXTRACT_FEATURE on incompatible input type.
Expected:
FAIL.

TEST-L03-OP-002
Normalize an observation.
Expected:
source ancestry remains recoverable.

TEST-L03-OP-003
Select one observation via attention.
Expected:
truth status unchanged.

TEST-L03-OP-004
Bind three features.
Expected:
object identity remains candidate/model.

TEST-L03-OP-005
Aggregate L→M.
Expected:
material lower-level heterogeneity remains recoverable.

TEST-L03-OP-006
Apply H→M constraint.
Expected:
result classified as constraint, not causation.

TEST-L03-OP-007
Integrate modalities sharing one source.
Expected:
independence count not inflated.

TEST-L03-OP-008
Mark modality unavailable.
Expected:
no negative observation generated.

TEST-L03-OP-009
Use a lossy aggregation.
Expected:
information-loss report required.

TEST-L03-OP-010
Use irreversible transform.
Expected:
reversibility marked IRREVERSIBLE.

TEST-L03-OP-011
Invalidate one load-bearing feature.
Expected:
dependent descendants revalidated/invalidated only.

TEST-L03-OP-012
Unknown threshold provenance.
Expected:
UNKNOWN/GAP or FAIL, not PASS.

TEST-L03-OP-013
Repair an invalid binding.
Expected:
old binding remains in history; repaired state revalidated.

TEST-L03-OP-014
Run structurally valid operator chain.
Expected:
no authoritative commit without control-plane authority.

TEST-L03-OP-015
All operator tests pass.
Expected:
does not establish empirical perception validity.
```

Current state:

```yaml
tests_defined: true
tests_executed: false
runtime_validation: false
formal_verification: false
empirical_validation: false
```

---

# 67. Falsifiers

Revise this contract if direct canonical evidence establishes:

```text
different canonical L03 operator set;

different operator ordering;

different feature/binding semantics;

different multimodal operator semantics;

different H/M/L transforms;

different provenance requirements;

different information-loss handling;

different reversibility semantics;

different repair/revalidation contract;

different proposal/commit boundary;

or executable runtime evidence contradicts these modeled operators.
```

A modeled operator claim is falsified within its stated scope if an executable counterexample shows that the operator cannot preserve the declared postconditions or invariants under admissible input.

---

# 68. Gap Matrix

```yaml
gap_status:

  generic_information_operator_workflow:
    status: SOURCE_ALIGNED

  explicit_operator_order:
    status: SOURCE_ALIGNED

  invariant_tracking:
    status: SOURCE_ALIGNED

  information_loss_tracking:
    status: SOURCE_ALIGNED

  reversibility_tracking:
    status: SOURCE_ALIGNED

  invalid_composition_detection:
    status: SOURCE_ALIGNED

  operator_trace:
    status: SOURCE_ALIGNED

  L03_admission_operator:
    status: MODEL_DEFINED

  L03_normalization_operator:
    status: MODEL_DEFINED

  L03_attention_selection_operator:
    status: MODEL_DEFINED

  L03_feature_operators:
    status: MODEL_DEFINED

  L03_relation_operators:
    status: MODEL_DEFINED

  L03_binding_operators:
    status: MODEL_DEFINED

  L03_temporal_spatial_operators:
    status: MODEL_DEFINED

  L03_multimodal_operators:
    status: MODEL_DEFINED

  L03_percept_generation_operators:
    status: MODEL_DEFINED

  L03_competing_percept_operators:
    status: MODEL_DEFINED

  L03_HML_operators:
    status: MODEL_DEFINED

  L03_validation_operators:
    status: MODEL_DEFINED

  L03_repair_operators:
    status: MODEL_DEFINED

  canonical_L03_operator_registry:
    status: CRITICAL_GAP

  canonical_operator_signatures:
    status: CRITICAL_GAP

  canonical_operator_order:
    status: DECISION_RELEVANT_GAP

  canonical_operator_thresholds:
    status: DECISION_RELEVANT_GAP

  executable_operator_runtime:
    status: CRITICAL_GAP

  executed_tests:
    status: CRITICAL_GAP

  empirical_validation:
    status: CRITICAL_GAP
```

---

# 69. Competing Operator Architectures

## COMPETING-001 — Fixed Linear Pipeline

```text
OBSERVATION
→ FEATURE
→ BIND
→ PERCEPT
```

Advantages:

```text
simple
replayable
easy to validate
```

Risks:

```text
poor ambiguity handling
weak feedback support
```

---

## COMPETING-002 — Dynamic Operator Graph

```text
operator selected based on current state
```

Advantages:

```text
flexible
efficient
```

Risks:

```text
harder provenance
operator-selection instability
```

---

## COMPETING-003 — Bidirectional Percept Graph

```text
bottom-up operators
+
top-down constraint operators
```

Advantages:

```text
supports contextual perception
```

Risks:

```text
source/inference contamination
feedback loops
```

---

## COMPETING-004 — Governed Typed Operator DAG

```text
typed state
+
minimal operator selection
+
explicit ordered operator DAG
+
H/M/L transforms
+
provenance
+
invariant gates
+
loss/reversibility tracking
+
control-plane finalization
```

Current model preference:

```text
COMPETING-004
```

because it best aligns with the AMOS Information Operator Engine's explicit-state, explicit-order, invariant, information-loss, reversibility, and operator-trace requirements.

This remains `MODEL`.

---

# 70. RSCF Completion State

```yaml
rscf:

  id: L03_PERCEPT_FORMATION_OPERATORS

  claim:
    L03_PERCEPT_FORMATION can be represented as a governed
    sequence or DAG of typed information operators that transform
    admitted observations and attention-conditioned state into
    percept candidates while preserving provenance, scope, regime,
    observer context, H/M/L identity, uncertainty, competing
    alternatives, information-loss metadata, reversibility,
    confidence ceilings, and proposal/commit separation.

  claim_class: MODEL

  evidence:
    - AMOS Information Operator Engine
    - AMOS percept-formation contracts
    - AMOS H/M/L and RSCF architecture

  provenance:
    origin_architect: Trang Phan
    architecture_family: AMOS
    subsystem: COGNITIVE_MATRIX
    primitive: L03_PERCEPT_FORMATION
    artifact: OPERATORS.md
    derivation: SOURCE_ALIGNED_OPERATOR_DISCIPLINE_PLUS_L03_MODEL

  scope:
    system: AMOS_OS
    subsystem: COGNITIVE_MATRIX
    primitive: L03_PERCEPT_FORMATION
    concern: operator_architecture

  regime:
    governed percept formation

  freshness:
    revalidate_when:
      - direct L03 operator canon is recovered
      - L03 definition changes
      - L03 state schema changes
      - HML transforms change
      - control-plane contract changes
      - executable operator runtime appears

  dependencies:
    - L01_SENSING_OBSERVATION
    - L02_ATTENTION
    - L03_PERCEPT_FORMATION_DEFINITION
    - L03_PERCEPT_FORMATION_VARIABLES
    - L03_PERCEPT_FORMATION_STATE
    - L03_PERCEPT_FORMATION_INVARIANTS
    - L03_PERCEPT_FORMATION_DEPENDENCIES
    - L03_PERCEPT_FORMATION_EQUATIONS
    - L03_PERCEPT_FORMATION_HML
    - L03_PERCEPT_FORMATION_MEMORY
    - L03_PERCEPT_FORMATION_PROVENANCE
    - L03_PERCEPT_FORMATION_CONTROL_PLANES
    - AMOS_INFORMATION_OPERATOR_ENGINE
    - AMOS_RSCF

  competing:
    - fixed linear operator pipeline
    - dynamic operator graph
    - bidirectional percept operator graph
    - governed typed operator DAG

  falsifiers:
    - incompatible direct canonical operator registry
    - incompatible canonical ordering
    - incompatible operator semantics
    - incompatible HML transformation rules
    - runtime counterexample
    - operator trace unable to preserve required invariants

  uncertainty:
    source: MEDIUM
    L03_mapping: HIGH
    operator_semantics: HIGH
    thresholds: MAXIMUM
    scope: MEDIUM
    regime: MEDIUM
    causal: HIGH
    execution: MAXIMUM
    empirical: MAXIMUM
    provenance_independence: MEDIUM

  confidence_ceiling:
    Generic operator discipline is source-aligned.
    The complete L03 operator registry, names, signatures,
    ordering, thresholds, and runtime semantics remain MODEL
    pending direct canon and executable validation.

  gap_status:
    canonical_operator_registry: CRITICAL_GAP
    canonical_signatures: CRITICAL_GAP
    canonical_ordering: DECISION_RELEVANT_GAP
    canonical_thresholds: DECISION_RELEVANT_GAP
    executable_operator_runtime: CRITICAL_GAP
    executed_validation: CRITICAL_GAP
    empirical_validation: CRITICAL_GAP

  cheapest_discriminating_test:
    recover direct canonical L03 operator material and compare
    operator identities, signatures, preconditions, postconditions,
    composition rules, loss/reversibility semantics, and authority
    boundaries; then implement a minimal observation→feature→binding
    →competing-percept operator DAG with full trace and fault injection.
```

---

# 71. Completion State

```yaml
completion_state:

  source_canon_references:
    status: PARTIAL_SOURCE_BOUND

  definition_scope:
    status: MODEL_COMPLETE

  typed_inputs_outputs:
    status: MODEL_COMPLETE

  state_variables:
    status: MODEL_COMPLETE

  operators:
    status: MODEL_COMPLETE

  invariants:
    status: MODEL_COMPLETE

  dependencies:
    status: MODEL_COMPLETE_WITH_GAPS

  HML_applicability:
    status: MODEL_COMPLETE

  control_plane_requirements:
    status: MODEL_COMPLETE

  agents:
    status: MODEL_COMPLETE

  skills:
    status: MODEL_COMPLETE

  workflows:
    status: MODEL_COMPLETE

  protocols:
    status: MODEL_COMPLETE

  evidence_provenance:
    status: MODEL_COMPLETE_SOURCE_PARTIAL

  uncertainty_confidence:
    status: MODEL_COMPLETE

  failure_modes:
    status: MODEL_COMPLETE

  repair_recovery:
    status: MODEL_COMPLETE

  tests_validators:
    status: MODEL_COMPLETE_UNEXECUTED

  falsifiers:
    status: MODEL_COMPLETE

  canonical_operator_registry:
    status: UNKNOWN_GAP

  executable_operator_runtime:
    status: UNKNOWN_GAP

  runtime_validation:
    status: UNKNOWN_GAP

  empirical_validation:
    status: UNKNOWN_GAP

  overall:
    status: COMPLETE_FOR_OPERATOR_CONTRACT_SCOPE

  conclusion_class:
    MODEL
```

---

# 72. Hard Boundaries

```text
PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

UNKNOWN/GAP != PASS
```

Operator-specific:

```text
OPERATOR != EMPIRICAL MECHANISM

TRANSFORMATION != CAUSATION

SELECTED != TRUE

FEATURE != OBSERVATION

FEATURE != INDEPENDENT EVIDENCE

GROUP != OBJECT

BINDING != IDENTITY

TEMPORAL ORDER != CAUSATION

SPATIAL ALIGNMENT != ENTITY IDENTITY

MULTIMODAL != INDEPENDENT

UNAVAILABLE MODALITY != NEGATIVE EVIDENCE

CONTEXT != OBSERVATION

AGGREGATION != IDENTITY

AGGREGATION != GLOBAL TRUTH

DOWNWARD CONSTRAINT != DOWNWARD CAUSATION

LOSSY != LOSSLESS

IRREVERSIBLE != REVERSIBLE

REPAIR != REVALIDATION

OPERATOR AVAILABLE != OPERATOR IMPLEMENTED

OPERATOR IMPLEMENTED != OPERATOR VALIDATED

VALIDATED OPERATOR != EMPIRICAL PERCEPTUAL LAW

OPERATOR EXECUTION != AUTHORIZED COMMIT
```

---

# 73. Governing Operator Contract

> **`L03_PERCEPT_FORMATION` SHALL represent percept formation through explicit typed operators whose inputs, outputs, preconditions, postconditions, ordering, provenance effects, dependency effects, information loss, reversibility, uncertainty effects, invariant requirements, and failure conditions remain inspectable. Operators SHALL be selected only as required for the current transformation and SHALL execute in an explicit order when order affects semantics. Observation admission, feature extraction, relation formation, grouping, binding, temporal/spatial alignment, multimodal integration, contextualization, percept generation, competing-hypothesis handling, H/M/L aggregation, validation, invalidation, repair, and revalidation SHALL preserve the distinction between observation, derived representation, percept, and external reality. Structural transformations SHALL NOT be promoted into causal claims without independently typed causal evidence. Aggregation or binding SHALL NOT prove identity. Repeated or correlated derivations SHALL NOT become independent corroboration. Material information loss and irreversibility SHALL be declared. `UNKNOWN/GAP` SHALL not satisfy a hard operator precondition. Operator capability SHALL NOT confer authority, and a completed percept-state proposal SHALL NOT become a durable commit without the governing control plane.**

---

# 74. Canon Boundary

```text
SOURCE-ALIGNED:

Trang Phan origin/stewardship

information operators are structural transformations
unless domain mechanism independently established

define input state

define target state

define representation

select only required operators

explicit operator order

track invariants

track information loss

track reversibility

detect invalid compositions

detect hidden assumptions

return operator trace

return failure conditions


AMOS_MODEL:

L03 operator taxonomy

ADMIT_OBSERVATION

NORMALIZE_OBSERVATION

SELECT_ATTENDED

DISTINGUISH_FEATURE

EXTRACT_FEATURE

RELATE_FEATURES

GROUP_FEATURES

BIND_FEATURES

UNBIND_FEATURES

PARTITION

TEMPORAL_ALIGN

SPATIAL_ALIGN

ALIGN_OBSERVER

ALIGN_MODALITIES

INTEGRATE_MODALITIES

CONTEXTUALIZE

COMBINE

SEPARATE

ORDER

THRESHOLD

GENERATE_PERCEPT_CANDIDATE

GENERATE_COMPETING_PERCEPTS

COMPARE_PERCEPTS

DISCRIMINATE

AGGREGATE_L_TO_M

AGGREGATE_M_TO_H

CONSTRAIN_H_TO_M

CONSTRAIN_M_TO_L

CHECK_PROVENANCE

CHECK_INDEPENDENCE

CHECK_SCOPE

CHECK_REGIME

CHECK_FRESHNESS

PROPAGATE_UNCERTAINTY

CALCULATE_CONFIDENCE_CEILING

PRESERVE_COMPETING

INVALIDATE_DEPENDENT

QUARANTINE

REPAIR

REVALIDATE

PROPOSE_STATE

operator ordering

operator composition rules

L03 operator failure taxonomy

L03 operator test suite


UNKNOWN/GAP:

direct canonical L03 operator registry

canonical operator identifiers

canonical operator signatures

canonical preconditions

canonical postconditions

canonical operator ordering

canonical composition rules

canonical thresholds

canonical reversibility classifications

canonical runtime implementation

executed tests

formal verification

empirical perceptual validation
```

Therefore:

```text
CONCLUSION CLASS:
MODEL

GENERIC INFORMATION-OPERATOR DISCIPLINE:
SOURCE-ALIGNED

L03-SPECIFIC OPERATOR REGISTRY:
MODEL

DIRECT L03 CANON:
UNKNOWN/GAP

IMPLEMENTATION:
UNKNOWN/GAP

VALIDATION:
UNKNOWN/GAP

EMPIRICAL HUMAN-PERCEPTION CLAIM:
NOT ESTABLISHED
```

```text
```

---

00_ROOT_MOC|AMOS MOC

---
**Related:** [[00_HOME]] · [[COGNITIVE_MATRIX_MOC]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: l03_percept_formation_primitives_cognitive_matrix_operators
node_type: note
path: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L03_PERCEPT_FORMATION/L03_PERCEPT_FORMATION_PRIMITIVES_COGNITIVE_MATRIX_OPERATORS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[L03_PERCEPT_FORMATION_MOC]]
