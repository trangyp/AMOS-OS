---
tags: ['cognitive_matrix', 'primitives', 'l01_sensing_observation', 'note']
---

Below is the full paste-ready `L01_SENSING_OBSERVATION / OPERATORS.md`. I’m keeping the exact L01 operator registry explicitly **MODEL / canon-bounded**, rather than presenting reconstructed operators as validated canon.

---
tags:
  - amos
  - cognitive-matrix
  - l01
  - sensing-observation
  - operators
  - provenance
  - control-plane
  - rscf
---

# L01_SENSING_OBSERVATION — Operators

**Class:** `COGNITIVE_PRIMITIVE_OPERATOR_CONTRACT`  
**Origin architect / steward:** Trang Phan  
**Architecture:** `AMOS_OS / COGNITIVE_MATRIX`  
**Primitive:** `L01_SENSING_OBSERVATION`  
**Artifact:** `OPERATORS.md`  
**Role:** `OBSERVATION TRANSFORMATION / VALIDATION / ROUTING CONTRACT`  
**Status:** `AMOS_MODEL / SOURCE-CANON BOUNDED / UNVALIDATED`

> **Epistemic boundary:** this document defines the proposed operator contract for `L01_SENSING_OBSERVATION`. It specifies admissible transformations over sensing and observation state while preserving provenance, scope, time, regime, uncertainty, H/M/L scale, epistemic class, and control-plane authority. Exact canonical L01 operator names, signatures, ordering, and implementation semantics remain subject to direct-canon confirmation and executable validation.

---

# 0. Purpose

`L01_SENSING_OBSERVATION/OPERATORS.md` defines the AMOS operator surface by which raw or already-structured sensing inputs may be transformed into governed observation records.

The operator layer exists to answer:

```text
what operation is being performed
on what typed input
under what scope
at what time
under which regime
by which observer/source
with what provenance
with what uncertainty
at which H/M/L scale
under whose authority
with what resulting epistemic class
```

The core transformation is conceptually:

[
\boxed{
SensingInput
\xrightarrow{Operator}
ObservationState
}
]

but never:

[
\boxed{
SensingInput
\xrightarrow{Operator}
Reality
}
]

Operators manipulate representations of observations.

They do not create ontological truth merely by execution.

---

# 1. Source / Canon References

## 1.1 Origin

```yaml
origin_architect:
  name: Trang Phan

architecture_family:
  - AMOS
  - AMOS OS
  - AMOS Cognitive Matrix
  - AMOS RSCF
  - AMOS H/M/L
```

## 1.2 Relevant Architecture Families

Relevant source/canon families include:

```text
AMOS_CORE lineage
AMOS Full Brain OS
AMOS Cognition architecture
AMOS Reality architecture
AMOS information/operator architecture
AMOS multimodal perception architecture
AMOS provenance topology
AMOS RSCF
AMOS H/M/L
AMOS temporal architecture
AMOS uncertainty governance
AMOS control-plane architecture
AMOS selective invalidation / repair architecture
L00_REALITY_ENVIRONMENT
L01_SENSING_OBSERVATION sibling contracts
```

## 1.3 Source Status

```yaml
source_status:

  typed_operations:
    class: CORPUS_ALIGNED

  provenance_preservation:
    class: CORPUS_ALIGNED

  scope_regime_preservation:
    class: CORPUS_ALIGNED

  temporal_preservation:
    class: CORPUS_ALIGNED

  uncertainty_preservation:
    class: CORPUS_ALIGNED

  HML_preservation:
    class: CORPUS_ALIGNED

  proposal_commit_separation:
    class: CORPUS_ALIGNED

  capability_authority_separation:
    class: CORPUS_ALIGNED

  exact_L01_operator_registry:
    class: AMOS_MODEL

  exact_operator_signatures:
    class: AMOS_MODEL

  exact_operator_order:
    class: UNKNOWN/GAP

  executable_operator_runtime:
    class: UNKNOWN/GAP

  empirical_validation:
    class: UNKNOWN/GAP
```

Therefore:

```text
CORPUS ALIGNMENT
!=
DIRECT L01 CANON

PROPOSED OPERATOR
!=
CANONICAL OPERATOR

OPERATOR CONTRACT
!=
IMPLEMENTED RUNTIME
```

---

# 2. Definition

An `L01 Operator` is a typed transformation, validation, classification, routing, comparison, or state-transition function applied to sensing or observation state.

General form:

[
\boxed{
O_i:
(X,C,A)
\rightarrow
(Y,E)
}
]

where:

```text
O_i = operator
X   = typed input state
C   = execution context
A   = authority context
Y   = typed output state
E   = evidence/provenance effects
```

Every material operator should expose or preserve sufficient information to determine:

```text
input identity
output identity
operator identity
operator version
source
observer
time
scope
regime
H/M/L scale
uncertainty
provenance
dependencies
authority
validation result
```

---

# 3. Scope

This contract governs operators acting on:

```text
raw sensing inputs
sensor outputs
human-reported observations
tool outputs
API observations
multimodal inputs
structured observations
observation candidates
observation sets
conflicting observations
historical observation records
derived observation representations
observation quality states
observation provenance
observation uncertainty
```

It covers:

```text
acquisition
normalization
typing
timestamping
scope binding
regime binding
source binding
observer binding
provenance binding
quality assessment
uncertainty attachment
validation
comparison
aggregation
decomposition
filtering
conflict detection
deduplication
freshness checking
reobservation
quarantine
invalidation
supersession
routing
```

It does not independently authorize:

```text
persistent memory writes
external disclosure
physical actuation
policy decisions
irreversible actions
cross-boundary information release
```

Those require appropriate control-plane authority.

---

# 4. Typed Inputs

```yaml
L01OperatorInput:

  payload:
    type:
      - RawSignal
      - SensorRecord
      - ToolObservation
      - HumanObservation
      - APIObservation
      - MultimodalObservation
      - ObservationCandidate
      - ObservationRecord
      - ObservationSet

  source:
    type: SourceRef | UNKNOWN

  observer:
    type: ObserverRef | UNKNOWN

  observed_at:
    type: Timestamp | TimeEnvelope | UNKNOWN

  received_at:
    type: Timestamp

  scope:
    type: ScopeEnvelope | UNKNOWN

  regime:
    type: RegimeRef | UNKNOWN

  modality:
    type: ModalityRef | UNKNOWN

  HML:
    type: H | M | L | UNKNOWN

  uncertainty:
    type: UncertaintyVector | UNKNOWN

  provenance:
    type: ProvenanceBundle

  dependencies:
    type: DependencySet

  epistemic_class:
    type:
      - OBSERVATION
      - SOURCE_CLAIM
      - DERIVED
      - MODEL
      - UNKNOWN

  authority:
    type: AuthorityContext

  execution_context:
    type: ExecutionContext
```

---

# 5. Typed Outputs

```yaml
L01OperatorOutput:

  result:
    type:
      - ObservationCandidate
      - ObservationRecord
      - ObservationSet
      - ValidationResult
      - ConflictSet
      - QualityAssessment
      - FreshnessAssessment
      - GapSet
      - QuarantineRecord
      - ReobservationRequest
      - OperatorFailure

  operator:
    type: OperatorRef

  input_refs:
    type: InputRef[]

  source:
    type: SourceRef | UNKNOWN

  observer:
    type: ObserverRef | UNKNOWN

  observed_at:
    type: Timestamp | TimeEnvelope | UNKNOWN

  processed_at:
    type: Timestamp

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeRef | UNKNOWN

  HML:
    type: H | M | L

  uncertainty:
    type: UncertaintyVector

  provenance:
    type: ProvenanceBundle

  dependencies:
    type: DependencySet

  validation:
    type: ValidationState

  epistemic_class:
    type: EpistemicClass

  confidence_ceiling:
    type: ConfidenceCeiling

  commit_state:
    type:
      - PROPOSED
      - VALIDATED
      - COMMITTED
      - REJECTED
      - QUARANTINED
```

---

# 6. State Variables

```text
X = input state

Y = output state

O = operator identity

V = operator version

S = source state

B = observer state

T = temporal state

C = scope/context state

R = regime state

H = H/M/L scale

P = provenance state

U = uncertainty state

Q = quality state

E = epistemic class

D = dependency state

A = authority state

F = freshness state

K = conflict state

G = gap state

Z = lifecycle / commit state
```

Operator-state tensor:

[
\boxed{
T_O =
T[
operator,
version,
input,
output,
source,
observer,
time,
scope,
regime,
HML,
provenance,
uncertainty,
quality,
authority,
status
]
}
]

---

# 7. Operator Families

The proposed L01 operator surface is divided into the following families:

```text
1. Acquisition operators
2. Representation operators
3. Binding operators
4. Validation operators
5. Quality operators
6. Comparison operators
7. Aggregation operators
8. Temporal operators
9. Provenance operators
10. Uncertainty operators
11. Conflict operators
12. Lifecycle operators
13. Routing operators
14. Recovery operators
```

These families are architectural organization.

They are not direct-canon claims unless independently confirmed.

---

# 8. Candidate Operator Registry

```text
SENSE
OBSERVE
CAPTURE
INGEST

TYPE
PARSE
NORMALIZE
CANONICALIZE

BIND_SOURCE
BIND_OBSERVER
BIND_TIME
BIND_SCOPE
BIND_REGIME
BIND_HML
BIND_PROVENANCE

VALIDATE
VERIFY_TYPE
VERIFY_SOURCE
VERIFY_TIME
VERIFY_SCOPE
VERIFY_REGIME
VERIFY_PROVENANCE

ASSESS_QUALITY
ASSESS_UNCERTAINTY
ASSESS_FRESHNESS

COMPARE
CORRELATE
MATCH
DIFFERENCE

FILTER
SELECT
PARTITION
DEDUPLICATE

AGGREGATE
DECOMPOSE
PROJECT
ALIGN

DETECT_CONFLICT
PRESERVE_COMPETING
DISCRIMINATE

QUARANTINE
INVALIDATE
SUPERSEDE
REVOKE

REOBSERVE
REVALIDATE
REPAIR

ROUTE
EMIT
PROPOSE
COMMIT
```

Important:

```text
OPERATOR NAME PRESENT HERE
!=
DIRECT CANON CONFIRMATION
```

---

# 9. SENSE

Conceptual acquisition:

[
\boxed{
SENSE(E,M,C)
\rightarrow
S
}
]

where:

```text
E = accessible environment/interface
M = sensing method
C = context
S = sensing state
```

`SENSE` does not imply accurate observation.

It only denotes acquisition through an available sensing channel.

---

# 10. OBSERVE

Conceptually:

[
\boxed{
OBSERVE(S,C)
\rightarrow
O_c
}
]

where `O_c` is an observation candidate.

The operator must not silently convert:

```text
signal
→
verified fact
```

---

# 11. CAPTURE

`CAPTURE` records a bounded representation of accessible sensing state.

```text
environment/interface
↓
CAPTURE
↓
raw representation
```

Required distinctions:

```text
CAPTURED
!=
COMPLETE

CAPTURED
!=
ACCURATE

CAPTURED
!=
VALIDATED
```

---

# 12. INGEST

`INGEST` accepts an observation-bearing input from an external or upstream source.

[
\boxed{
INGEST(X)
\rightarrow
X'
}
]

Ingestion is an admission into processing, not validation.

```text
INGESTED
!=
TRUSTED

INGESTED
!=
TRUE
```

---

# 13. TYPE

`TYPE` assigns or verifies a semantic/structural type.

Example:

```text
input
↓
TYPE
↓
SensorRecord
HumanReport
ToolObservation
ModelOutput
Unknown
```

Typing must preserve uncertainty when classification is ambiguous.

---

# 14. PARSE

[
\boxed{
PARSE(X,\Sigma)
\rightarrow
X_p
}
]

where (\Sigma) is an expected schema or grammar.

Parse success establishes structural compatibility only.

```text
PARSE_SUCCESS
!=
SEMANTIC_VALIDITY

PARSE_SUCCESS
!=
TRUTH
```

---

# 15. NORMALIZE

`NORMALIZE` maps equivalent representations into a common representation.

[
\boxed{
N:
X
\rightarrow
X_n
}
]

Normalization must preserve semantic identity or explicitly record loss.

Examples:

```text
unit normalization
timestamp normalization
coordinate normalization
field normalization
encoding normalization
```

---

# 16. CANONICALIZE

`CANONICALIZE` selects a canonical representation where multiple equivalent encodings exist.

It must not erase:

```text
source representation
transformation lineage
uncertainty introduced by conversion
```

Thus:

[
\boxed{
Canonical(X)
\neq
Original(X)
}
]

even when semantically equivalent within a declared scope.

---

# 17. BIND_SOURCE

[
\boxed{
BIND_SOURCE(O,S)
\rightarrow
O'
}
]

Attaches source identity and ancestry.

If source identity is unknown:

```text
source = UNKNOWN
```

not an inferred source presented as observed fact.

---

# 18. BIND_OBSERVER

Attaches the observer or acquisition actor where relevant.

```text
observer
sensor
agent
human reporter
tool
system
```

Observer identity must remain distinct from source identity when they differ.

---

# 19. BIND_TIME

Attaches temporal coordinates.

At minimum distinguish when available:

```text
event time
observation time
acquisition time
ingestion time
processing time
```

[
\boxed{
ObservationTime
\neq
ProcessingTime
}
]

unless explicitly equal.

---

# 20. BIND_SCOPE

[
\boxed{
BIND_SCOPE(O,S_c)
\rightarrow
O'
}
]

Scope may include:

```text
entity
population
location
system
subsystem
measurement boundary
domain
environment
```

Unknown scope must remain explicit.

---

# 21. BIND_REGIME

Attaches regime information such as:

```text
NORMAL
STRESS
TRANSITION
DEGRADED
SIMULATED
UNKNOWN
```

when relevant.

Regime binding prevents observations from being silently generalized across incompatible operating conditions.

---

# 22. BIND_HML

Assigns observation scale:

```text
L = local / atomic
M = subsystem / intermediate
H = system / global
```

The operator must not infer a higher scale solely from repetition.

---

# 23. BIND_PROVENANCE

Conceptually:

[
\boxed{
BIND_PROVENANCE(O,P)
\rightarrow
O_P
}
]

The resulting observation must retain ancestry to its input evidence.

---

# 24. VALIDATE

Generic validation:

[
\boxed{
VALIDATE(O,I)
\rightarrow
V
}
]

where `I` is the applicable invariant set.

Possible result:

```text
PASS
FAIL
CONDITIONAL
UNKNOWN
QUARANTINE
```

Hard boundary:

```text
UNKNOWN
!=
PASS
```

---

# 25. VERIFY_TYPE

Checks that the observation representation satisfies the required type contract.

Failure should produce:

```text
TYPE_FAILURE
```

or:

```text
UNKNOWN_TYPE
```

rather than silent coercion when semantics may change.

---

# 26. VERIFY_SOURCE

Checks:

```text
source presence
source identity
source lineage
source status
revocation state
```

where applicable.

Source verification does not establish observation correctness by itself.

---

# 27. VERIFY_TIME

Checks:

```text
timestamp presence
timestamp ordering
future-date anomalies
time-zone consistency
event/observation distinction
freshness relevance
```

---

# 28. VERIFY_SCOPE

Checks whether:

```text
claimed scope
```

is supported by:

```text
actual observation coverage
```

A local observation cannot automatically satisfy a global scope claim.

---

# 29. VERIFY_REGIME

Checks whether observation use remains inside its regime-validity envelope.

```text
observed in regime R1
used in regime R2
```

requires explicit compatibility or revalidation.

---

# 30. VERIFY_PROVENANCE

Checks:

```text
ancestry completeness
source identity
transformation chain
duplicate ancestry
revocation
correlated evidence
missing lineage
```

---

# 31. ASSESS_QUALITY

Candidate quality dimensions include:

```text
completeness
resolution
precision
consistency
signal integrity
coverage
source reliability
measurement reliability
```

Quality must remain multidimensional where collapsing dimensions would hide important weakness.

---

# 32. ASSESS_UNCERTAINTY

Produces or updates an uncertainty vector.

```yaml
uncertainty:

  observation:

  measurement:

  source:

  temporal:

  scope:

  regime:

  provenance_independence:

  transformation:

  execution:
```

No numerical value should be fabricated merely because an operator expects one.

---

# 33. ASSESS_FRESHNESS

Conceptually:

[
\boxed{
Freshness =
f(
observation_time,
current_time,
regime,
purpose,
change_rate
)
}
]

This is an AMOS MODEL relationship, not a universal empirical equation.

Possible outputs:

```text
FRESH
STALE
CONDITIONAL
UNKNOWN
```

---

# 34. COMPARE

[
\boxed{
COMPARE(O_1,O_2)
\rightarrow
C
}
]

Comparison requires compatibility checks for:

```text
type
unit
scope
time
regime
H/M/L
measurement method
```

before differences are interpreted.

---

# 35. CORRELATE

`CORRELATE` identifies association between observation states.

Hard causal firewall:

[
\boxed{
Correlation
\neq
Causation
}
]

The operator must not emit causal conclusions unless separately supported by causally typed evidence.

---

# 36. MATCH

Determines whether observations may refer to the same:

```text
entity
event
source
measurement
phenomenon
```

Matching confidence must remain explicit when identity is uncertain.

---

# 37. DIFFERENCE

Conceptually:

[
\boxed{
DIFF(O_1,O_2)
\rightarrow
\Delta O
}
]

The difference must preserve the coordinate frame under which the comparison is meaningful.

---

# 38. FILTER

[
\boxed{
FILTER(O,P)
\rightarrow
O'
}
]

where `P` is an explicit predicate.

Filtering must preserve knowledge that excluded observations existed when exclusion materially affects interpretation.

---

# 39. SELECT

Selects observations satisfying declared criteria.

Selection criteria must be provenance-visible for consequential downstream use.

---

# 40. PARTITION

[
\boxed{
PARTITION(O,K)
\rightarrow
{O_1,\dots,O_n}
}
]

Possible keys:

```text
source
time
scope
regime
modality
H/M/L
quality
epistemic class
```

---

# 41. DEDUPLICATE

Deduplication identifies redundant representations.

Critical invariant:

```text
DUPLICATE
!=
INDEPENDENT CONFIRMATION
```

Deduplication should preserve ancestry information rather than merely deleting copies.

---

# 42. AGGREGATE

[
\boxed{
AGGREGATE({O_i},A)
\rightarrow
O_A
}
]

Aggregation requires explicit:

```text
aggregation rule
input membership
scope
time
regime
weighting
uncertainty treatment
provenance treatment
```

Aggregation must not erase material disagreement.

---

# 43. DECOMPOSE

[
\boxed{
DECOMPOSE(O,D)
\rightarrow
{O_1,\dots,O_n}
}
]

Used where a composite observation contains separable sub-observations.

Decomposition must preserve parent-child lineage.

---

# 44. PROJECT

Maps an observation into a reduced representation or coordinate space.

[
\boxed{
PROJECT(O,\Pi)
\rightarrow
O_\Pi
}
]

Projection loss must be explicit where decision-relevant.

---

# 45. ALIGN

Aligns observations across:

```text
time
coordinate systems
schemas
modalities
units
H/M/L levels
```

Alignment is a transformation.

It is not proof that aligned observations describe the same underlying cause.

---

# 46. DETECT_CONFLICT

[
\boxed{
DETECT_CONFLICT({O_i})
\rightarrow
K
}
]

Conflict may arise from:

```text
different values
different sources
different times
different regimes
different scopes
different methods
different interpretations
```

Not every apparent conflict is a true contradiction.

---

# 47. PRESERVE_COMPETING

When observations cannot yet be reconciled:

```text
O1 = X
O2 = NOT X
```

the operator should produce:

```text
COMPETING {
  O1,
  O2
}
```

rather than unsupported convergence.

---

# 48. DISCRIMINATE

Identifies the cheapest high-information observation or test capable of distinguishing competing hypotheses.

Conceptually:

[
\boxed{
D^*
===

\arg\max_D
\frac{
ExpectedDiscrimination(D)
}{
Cost(D)
}
}
]

This is a decision-model expression, not an established universal law.

---

# 49. QUARANTINE

Moves an observation into an isolated unresolved state.

Reasons may include:

```text
missing provenance
schema ambiguity
source conflict
possible contamination
regime mismatch
authority uncertainty
integrity failure
```

Quarantine is neither rejection nor validation.

---

# 50. INVALIDATE

Marks an observation as unusable for specified dependent claims or decisions.

Invalidation must preserve:

```text
reason
evidence
time
validator
dependency impact
```

---

# 51. SUPERSEDE

Links a newer or corrected observation to an older observation.

```text
O_old
↓
SUPERSEDED_BY
↓
O_new
```

Historical lineage remains available unless governance requires deletion.

---

# 52. REVOKE

Marks an observation or source as no longer authorized/trusted for specified uses.

Revocation should propagate only through affected dependency closure.

---

# 53. REOBSERVE

[
\boxed{
REOBSERVE(Target,C)
\rightarrow
O_{new}
}
]

`REOBSERVE` must create a new temporal observation state.

It must not silently rewrite the old observation.

---

# 54. REVALIDATE

[
\boxed{
REVALIDATE(O,C_{new})
\rightarrow
V_{new}
}
]

Required when material validity conditions change, including:

```text
time
regime
scope
source status
dependency status
operator version
control policy
```

---

# 55. REPAIR

`REPAIR` addresses malformed, incomplete, corrupted, or invalid observation state.

Preferred pattern:

```text
detect
↓
quarantine
↓
identify failed premise/operator
↓
repair locally
↓
revalidate
↓
restore or reject
```

Repair must not fabricate missing evidence.

---

# 56. ROUTE

Routes observation state to the appropriate next primitive, validator, memory layer, or control plane.

[
\boxed{
ROUTE(O,C)
\rightarrow
Destination
}
]

Routing eligibility does not grant the destination authority to act.

---

# 57. EMIT

Produces an observation result for downstream consumption.

`EMIT` should include the validity envelope required to interpret the observation.

Forbidden:

```text
emit(value)
```

when downstream correctness depends on omitted:

```text
scope
time
regime
uncertainty
provenance
```

---

# 58. PROPOSE

Creates a proposed state transition or downstream action.

```text
PROPOSE
!=
COMMIT
```

Example:

```text
PROPOSE_MEMORY_WRITE
PROPOSE_REOBSERVATION
PROPOSE_INVALIDATION
```

---

# 59. COMMIT

`COMMIT` creates an authoritative durable state change only after applicable control-plane checks.

Conceptually:

[
\boxed{
CommitEligible
==============

Validated
\land
Authorized
\land
Fresh
\land
ConstraintCompatible
}
]

This is an AMOS MODEL gate.

The operator contract does not claim that ChatGPT itself implements transactional commit semantics.

---

# 60. Operator Composition

Operators may compose:

[
O_n \circ O_{n-1} \circ \cdots \circ O_1
]

but composition is valid only when:

```text
output type of O_i
compatible with
input type of O_{i+1}
```

and when required:

```text
scope compatibility
regime compatibility
temporal compatibility
authority compatibility
provenance continuity
```

hold.

---

# 61. Operator Composition Invariant

For composed transformation:

[
X
\xrightarrow{O_1}
X_1
\xrightarrow{O_2}
X_2
\xrightarrow{O_3}
Y
]

provenance must retain:

```text
X
O1
X1
O2
X2
O3
Y
```

at sufficient resolution for audit and repair.

---

# 62. Non-Commutativity

Operator order may matter.

Generally:

[
O_a(O_b(X))
\neq
O_b(O_a(X))
]

Example:

```text
FILTER → AGGREGATE
```

may differ from:

```text
AGGREGATE → FILTER
```

Therefore operator ordering must be explicit where semantically material.

---

# 63. Idempotence

Some operators may be expected to be idempotent under fixed context:

[
O(O(X)) = O(X)
]

Candidate examples:

```text
canonicalization
deduplication
some validation operations
```

But idempotence must not be assumed universally.

Exact idempotence contracts remain:

```text
UNKNOWN/GAP
```

until operator-specific semantics are canonicalized.

---

# 64. Reversibility

Operators should declare whether they are:

```text
REVERSIBLE
PARTIALLY_REVERSIBLE
IRREVERSIBLE
UNKNOWN
```

Examples:

```text
projection may lose information
aggregation may lose local detail
filtering may remove records
normalization may be reversible or lossy
```

Irreversible transformations require stronger governance when source data cannot be reconstructed.

---

# 65. Information-Loss Boundary

For transformation (O):

[
\boxed{
Loss(O)
=======

## InformationRequiredBefore

InformationRecoverableAfter
}
]

conceptually.

No numerical interpretation is implied unless a domain-specific metric is defined.

Decision-relevant loss must be recorded.

---

# 66. Core Operator Invariants

Minimum proposed invariant registry:

```text
L01-OP-INV-001  Typed Input/Output
L01-OP-INV-002  Observation != Reality
L01-OP-INV-003  Transformation Traceability
L01-OP-INV-004  Provenance Preservation
L01-OP-INV-005  Temporal Preservation
L01-OP-INV-006  Scope Preservation
L01-OP-INV-007  Regime Preservation
L01-OP-INV-008  H/M/L Preservation
L01-OP-INV-009  Uncertainty Preservation
L01-OP-INV-010  Epistemic-Class Preservation
L01-OP-INV-011  Unknown Preservation
L01-OP-INV-012  Contradiction Visibility
L01-OP-INV-013  Causal Firewall
L01-OP-INV-014  Provenance Independence
L01-OP-INV-015  Capability/Authority Separation
L01-OP-INV-016  Proposal/Commit Separation
L01-OP-INV-017  Selective Invalidation
L01-OP-INV-018  Simulation Separation
L01-OP-INV-019  Operator-Version Traceability
L01-OP-INV-020  Loss Visibility
```

---

# 67. Typed Input / Output Invariant

Every operator must either:

```text
accept declared input type
```

or:

```text
fail / return UNKNOWN
```

It must not silently reinterpret incompatible data.

---

# 68. Observation != Reality

No operator may promote:

```text
representation
```

directly into:

```text
reality
```

without an explicit epistemic boundary.

[
\boxed{
OperatorOutput
\neq
RealityByDefinition
}
]

---

# 69. Transformation Traceability

Every material transformation should be reconstructable as:

```text
input
↓
operator
↓
parameters/context
↓
output
```

---

# 70. Provenance Preservation

Conceptually:

[
\boxed{
P(Y)
\supseteq
P(X)
+
P(O)
}
]

where lineage to both input and transformation is retained.

---

# 71. Temporal Preservation

Operators must not silently substitute:

```text
processing time
```

for:

```text
observation time
```

or:

```text
event time
```

---

# 72. Scope Preservation

Transformation may narrow scope explicitly.

It may not silently widen scope.

[
\boxed{
Scope(Y)
\subseteq
Scope(X)
}
]

for ordinary filtering/projection unless a valid aggregation/generalization rule explicitly licenses broader scope.

---

# 73. Regime Preservation

Operators must preserve regime identity unless they explicitly perform regime translation or revalidation.

---

# 74. H/M/L Preservation

Cross-scale transformation requires explicit mapping.

```text
L
→
M
```

or:

```text
M
→
H
```

must not occur merely because multiple observations are present.

---

# 75. Uncertainty Preservation

Transformation cannot legitimately increase certainty solely because data has been processed.

[
\boxed{
Processing
\neq
IndependentEvidence
}
]

---

# 76. Epistemic-Class Preservation

Examples:

```text
MODEL
→ normalization
→ MODEL

SOURCE_CLAIM
→ parsing
→ SOURCE_CLAIM

OBSERVATION
→ canonicalization
→ OBSERVATION-derived representation
```

A transformation must not silently upgrade epistemic class.

---

# 77. Unknown Preservation

```text
UNKNOWN
```

must remain explicit until evidence resolves it.

Forbidden:

```text
UNKNOWN
→ PASS

UNKNOWN
→ ZERO

UNKNOWN
→ FALSE

UNKNOWN
→ NORMAL
```

without declared policy and justification.

---

# 78. Contradiction Visibility

Operators must not suppress material disagreement merely to produce a single clean output.

```text
COMPETING
```

is a valid terminal state.

---

# 79. Causal Firewall

Observation operators may establish:

```text
association
difference
temporal sequence
co-occurrence
```

but those do not independently establish:

```text
causal mechanism
necessary condition
sufficient condition
intervention effect
```

---

# 80. Provenance Independence

If:

```text
O1 ← Source A
O2 ← copy(Source A)
O3 ← summary(O2)
```

then:

```text
O1 + O2 + O3
```

do not automatically constitute three independent observations.

---

# 81. Operator-Version Traceability

If operator behavior changes between versions:

```text
Operator v1
Operator v2
```

outputs must remain attributable to the version that produced them when the difference can affect interpretation.

---

# 82. Dependencies

Primary dependencies:

```text
L00_REALITY_ENVIRONMENT
L01_DEFINITION
L01_VARIABLES
L01_EQUATIONS
L01_INVARIANTS
L01_DEPENDENCIES
L01_HML
L01_MEMORY
L01_PROVENANCE
L01_CONTROL_PLANES
L01_RSCF
L01_FAILURE_MODES
L01_REPAIR
L01_PROTOCOLS
```

Conceptual dependency chain:

```text
L00 REALITY / ENVIRONMENT
↓
L01 INPUT CONTRACT
↓
L01 OPERATORS
↓
L01 OBSERVATION STATE
↓
VALIDATION
↓
MEMORY / ROUTING / DOWNSTREAM COGNITION
```

---

# 83. H/M/L Applicability

## L — Local Operators

Operate on:

```text
single signals
single sensor readings
single tool outputs
single observation candidates
atomic provenance
local validation
```

Examples:

```text
TYPE
PARSE
BIND_TIME
BIND_SOURCE
VALIDATE
```

## M — Subsystem Operators

Operate on:

```text
observation groups
sensor clusters
cross-source comparisons
temporal windows
subsystem state
```

Examples:

```text
COMPARE
ALIGN
DEDUPLICATE
DETECT_CONFLICT
AGGREGATE
```

## H — System Operators

Operate on:

```text
system-level observation coverage
cross-subsystem synthesis
global regime assessment
high-level observation state
```

Examples:

```text
AGGREGATE
PROJECT
ROUTE
ASSESS_COVERAGE
```

provided valid cross-scale transformation exists.

---

# 84. Cross-Scale Rule

[
O_L
\xrightarrow{A_{L\rightarrow M}}
O_M
\xrightarrow{A_{M\rightarrow H}}
O_H
]

requires explicit aggregation/translation functions.

Hard boundary:

```text
MANY LOCAL OBSERVATIONS
!=
AUTOMATIC GLOBAL TRUTH
```

---

# 85. Control-Plane Requirements

The control plane should govern:

```text
which operators may execute
which sources may be accessed
which scopes may be observed
which observations may persist
which operators may mutate state
which operations require approval
which observations may cross boundaries
which operators may trigger reobservation
which invalidations may commit
which external effects may occur
```

---

# 86. Capability / Authority Boundary

An agent may possess:

```text
SENSE capability
READ capability
WRITE capability
INVALIDATE capability
ROUTE capability
```

without possessing authority to exercise those capabilities in a given context.

[
\boxed{
Capability
\neq
Authority
}
]

---

# 87. Proposal / Commit Boundary

Potential state-changing operators should distinguish:

```text
PROPOSE_INVALIDATION
```

from:

```text
COMMIT_INVALIDATION
```

and:

```text
PROPOSE_WRITE
```

from:

```text
COMMIT_WRITE
```

---

# 88. Commit-Time Revalidation

For consequential state changes, eligibility should be rechecked at commit time.

Conceptually:

[
\boxed{
Commit(O)
\Rightarrow
Revalidate(
authority,
constraints,
freshness,
dependencies
)
}
]

This prevents stale preconditions from silently authorizing a later effect.

---

# 89. Agents

Candidate architectural roles:

```text
Sensing Agent
Observation Agent
Observation Parsing Agent
Observation Validation Agent
Provenance Agent
Freshness Agent
Conflict Detection Agent
Observation Aggregation Agent
Observation Routing Agent
Reobservation Agent
Repair Agent
Audit Agent
```

These are roles.

```text
ROLE
!=
DEPLOYED AGENT
```

---

# 90. Skills

Candidate supporting capabilities:

```text
multimodal perception
structured parsing
information operators
provenance validation
scope/regime checking
temporal alignment
uncertainty assessment
H/M/L mapping
conflict detection
claim verification
memory admission
repair/recovery
```

Skill availability does not imply authorization.

---

# 91. Workflow — Basic Observation

```text
ACCESS INPUT
↓
SENSE / INGEST
↓
CAPTURE
↓
TYPE
↓
PARSE
↓
NORMALIZE
↓
BIND SOURCE
↓
BIND OBSERVER
↓
BIND TIME
↓
BIND SCOPE
↓
BIND REGIME
↓
BIND H/M/L
↓
BIND PROVENANCE
↓
ASSESS QUALITY
↓
ASSESS UNCERTAINTY
↓
VALIDATE
↓
EMIT / QUARANTINE
```

---

# 92. Workflow — Multi-Source Observation

```text
INGEST OBSERVATIONS
↓
TYPE / NORMALIZE
↓
VERIFY PROVENANCE
↓
CHECK INDEPENDENCE
↓
ALIGN TIME / SCOPE / REGIME
↓
COMPARE
↓
DETECT CONFLICT
↓
AGGREGATE IF LICENSED
OR
PRESERVE COMPETING
↓
VALIDATE
↓
EMIT
```

---

# 93. Workflow — Stale Observation

```text
RETRIEVE OBSERVATION
↓
ASSESS FRESHNESS
↓
FRESH?
├── YES
│   ↓
│   VALIDATE FOR CURRENT USE
│
└── NO / UNKNOWN
    ↓
    REOBSERVE
    ↓
    CREATE NEW OBSERVATION
    ↓
    COMPARE WITH HISTORICAL STATE
```

---

# 94. Workflow — Operator Failure

```text
OPERATOR EXECUTION
↓
FAILURE DETECTED
↓
FREEZE AFFECTED OUTPUT
↓
CLASSIFY FAILURE
↓
TRACE INPUT + OPERATOR VERSION
↓
QUARANTINE AFFECTED STATE
↓
REPAIR OR SUBSTITUTE OPERATOR
↓
REEXECUTE
↓
REVALIDATE
```

---

# 95. Protocols

Candidate protocol messages:

```text
SensingRequest
SensingResult

ObservationCandidate

OperatorExecutionRequest
OperatorExecutionResult
OperatorFailure

ObservationValidationRequest
ObservationValidationResult

ObservationConflictEvent

ObservationRevalidationRequest

ObservationReobservationRequest

ObservationInvalidationProposal
ObservationInvalidationCommit

ObservationRoutingRequest
ObservationRoutingResult
```

Example:

```yaml
OperatorExecutionResult:

  execution_id:

  operator:
    id:
    version:

  inputs: []

  output:

  scope:

  regime:

  HML:

  provenance:

  uncertainty:

  validation:

  authority:

  status:

  confidence_ceiling:
```

---

# 96. Evidence / Provenance

Every consequential operator execution should preserve or reference:

```text
input identities
input source ancestry
operator identity
operator version
parameters
execution context
execution time
scope
regime
H/M/L
output identity
validation state
uncertainty changes
authority context
```

---

# 97. Operator Provenance Tensor

[
\boxed{
P_O =
T[
execution,
operator,
version,
input,
source,
transform,
output,
time,
scope,
regime,
validator,
authority
]
}
]

---

# 98. Uncertainty Vector

Material uncertainty may include:

```yaml
uncertainty:

  sensing:

  measurement:

  source:

  parsing:

  transformation:

  temporal:

  scope:

  regime:

  HML:

  provenance_independence:

  operator:

  execution:
```

No unsupported numeric uncertainty should be invented.

---

# 99. Confidence Ceiling

For output (Y) produced from load-bearing inputs (X_i):

[
\boxed{
Conf(Y)
\le
\min_i Conf(X_i)
}
]

unless an independent validating observation legitimately raises the evidential basis.

Transformation alone does not constitute independent confirmation.

---

# 100. Failure Modes

## FM-OP-01 — Untyped Transformation

Operator consumes semantically incompatible input.

## FM-OP-02 — Silent Coercion

Invalid type is silently converted into another meaning.

## FM-OP-03 — Observation-as-Reality

Operator output is presented as reality itself.

## FM-OP-04 — Provenance Loss

Transformation severs input ancestry.

## FM-OP-05 — Timestamp Collapse

Processing time replaces observation time.

## FM-OP-06 — Scope Inflation

Local observation becomes global claim.

## FM-OP-07 — Regime Leakage

Observation is reused across incompatible regimes.

## FM-OP-08 — H/M/L Inflation

Local evidence is promoted to higher scale without valid aggregation.

## FM-OP-09 — Uncertainty Collapse

Transformation removes uncertainty without evidence.

## FM-OP-10 — Epistemic Upgrade

Model/source claim becomes observation through processing.

## FM-OP-11 — False Independence

Copies or transformations are counted as independent evidence.

## FM-OP-12 — Conflict Erasure

Aggregation hides disagreement.

## FM-OP-13 — Causal Overreach

Correlation/comparison operator produces unsupported causal conclusion.

## FM-OP-14 — Operator-Version Drift

Output cannot be tied to the operator version that produced it.

## FM-OP-15 — Unauthorized Execution

Agent executes operator without authority.

## FM-OP-16 — Proposal-as-Commit

Proposed mutation becomes durable effect.

## FM-OP-17 — Stale Preconditions

Operator commits after authority/constraints changed.

## FM-OP-18 — Lossy Transformation Hidden

Projection/aggregation destroys material information without declaration.

## FM-OP-19 — Simulation Contamination

Synthetic state enters observation pipeline as real observation.

## FM-OP-20 — Unknown-as-Pass

Unresolved validation is accepted as success.

## FM-OP-21 — Over-Invalidation

Failure causes unnecessary global rollback.

## FM-OP-22 — Under-Invalidation

Dependent outputs survive invalid operator/input state.

---

# 101. Repair / Recovery

General recovery:

```text
DETECT FAILURE
↓
IDENTIFY OPERATOR EXECUTION
↓
IDENTIFY INPUTS
↓
IDENTIFY OPERATOR VERSION
↓
TRACE PROVENANCE
↓
TRACE DEPENDENTS
↓
QUARANTINE AFFECTED STATE
↓
PRESERVE UNAFFECTED STATE
↓
REPAIR INPUT / OPERATOR / CONTEXT
↓
REEXECUTE
↓
REVALIDATE
↓
RESTORE OR REJECT
```

---

# 102. Selective Recovery

If:

```text
X
↓
O1
↓
Y
↓
O2
↓
Z
```

and `O1` is invalidated:

```text
invalidate:
  Y
  Z
```

but unrelated observation branches remain valid.

[
\boxed{
RepairScope
===========

AffectedDependencyClosure
}
]

---

# 103. Operator Substitution

If operator (O_a) fails, substitution with (O_b) is allowed only when:

```text
input contract compatible
output contract compatible
scope compatible
regime compatible
semantic intent preserved
authority valid
provenance preserved
```

Similarity of function names is insufficient.

---

# 104. Validators

Minimum proposed validators:

```text
VALIDATOR_OPERATOR_IDENTITY

VALIDATOR_OPERATOR_VERSION

VALIDATOR_INPUT_TYPE

VALIDATOR_OUTPUT_TYPE

VALIDATOR_OPERATOR_PRECONDITION

VALIDATOR_OPERATOR_POSTCONDITION

VALIDATOR_SOURCE

VALIDATOR_TIME

VALIDATOR_SCOPE

VALIDATOR_REGIME

VALIDATOR_HML

VALIDATOR_PROVENANCE

VALIDATOR_UNCERTAINTY

VALIDATOR_EPISTEMIC_CLASS

VALIDATOR_CONFLICT

VALIDATOR_INDEPENDENCE

VALIDATOR_AUTHORITY

VALIDATOR_COMMIT_ELIGIBILITY

VALIDATOR_INFORMATION_LOSS

VALIDATOR_SIMULATION_BOUNDARY
```

---

# 105. Minimum Tests

```text
TEST_OP_001
invalid input type fails or remains UNKNOWN

TEST_OP_002
parse success cannot become truth validation

TEST_OP_003
normalization preserves provenance

TEST_OP_004
normalization records material loss

TEST_OP_005
observation time survives transformation

TEST_OP_006
processing time cannot replace observation time

TEST_OP_007
local scope cannot silently become global

TEST_OP_008
regime survives operator composition

TEST_OP_009
H/M/L survives transformation

TEST_OP_010
uncertainty survives transformation

TEST_OP_011
epistemic class cannot silently upgrade

TEST_OP_012
unknown cannot silently become PASS

TEST_OP_013
conflicting observations remain visible

TEST_OP_014
duplicate ancestry cannot create independent confirmation

TEST_OP_015
correlation cannot automatically produce causal claim

TEST_OP_016
operator version is recoverable

TEST_OP_017
operator composition preserves lineage

TEST_OP_018
lossy projection records loss

TEST_OP_019
aggregation preserves material disagreement

TEST_OP_020
simulation cannot enter observation class without explicit boundary

TEST_OP_021
capability cannot substitute for authority

TEST_OP_022
proposal cannot substitute for commit

TEST_OP_023
commit-time stale authority causes failure

TEST_OP_024
invalid operator selectively invalidates dependents

TEST_OP_025
unaffected branches survive repair
```

---

# 106. Adversarial Tests

Test against:

```text
malformed input

valid schema with false semantic content

missing source

forged source

missing timestamp

future timestamp

timestamp substitution

unknown scope

scope inflation

regime mismatch

cross-scale overgeneralization

duplicated observations

multiple summaries from one source

conflicting observations

model output labeled observation

simulation labeled reality

lossy normalization

lossy aggregation

operator version mismatch

revoked source

expired authority

stale commit preconditions

unknown validation result

unauthorized write

unauthorized external route
```

---

# 107. Falsifiers

This contract must be revised if:

```text
direct AMOS canon defines materially different L01 operators

canonical architecture places these transformations in another primitive

canonical operator signatures conflict with proposed types

canonical H/M/L semantics require different scale transformations

canonical provenance semantics require different lineage behavior

canonical control-plane semantics prohibit proposed operator ownership

runtime implementation establishes materially different operator lifecycle

tests show proposed invariants prevent required legitimate observation behavior

domain-specific sensing requires stronger semantics than this generic contract
```

---

# 108. Gap Matrix

```yaml
operator_gap_status:

  direct_L01_operator_canon:
    status: GAP
    criticality: CRITICAL

  canonical_operator_registry:
    status: GAP
    criticality: CRITICAL

  canonical_operator_signatures:
    status: GAP
    criticality: CRITICAL

  canonical_operator_order:
    status: GAP
    criticality: DECISION_RELEVANT

  operator_definition:
    status: MODEL_COMPLETE

  typed_inputs_outputs:
    status: MODEL_COMPLETE

  operator_families:
    status: MODEL_COMPLETE

  provenance_rules:
    status: MODEL_COMPLETE

  temporal_rules:
    status: MODEL_COMPLETE

  scope_regime_rules:
    status: MODEL_COMPLETE

  HML_rules:
    status: MODEL_COMPLETE

  uncertainty_rules:
    status: MODEL_COMPLETE

  causal_firewall:
    status: MODEL_COMPLETE

  authority_boundary:
    status: MODEL_COMPLETE

  proposal_commit_boundary:
    status: MODEL_COMPLETE

  selective_invalidation:
    status: MODEL_COMPLETE

  exact_idempotence_contracts:
    status: GAP

  exact_reversibility_contracts:
    status: GAP

  exact_operator_cost_models:
    status: GAP

  executable_runtime:
    status: GAP

  executed_tests:
    status: GAP

  empirical_validation:
    status: GAP

  operational_validation:
    status: GAP
```

---

# 109. Gap Priority

Highest-priority unresolved items:

```text
1. Locate direct canonical L01 operator definitions.

2. Determine the authoritative canonical operator registry.

3. Confirm exact operator names and signatures.

4. Confirm operator ownership boundaries between L01 and infrastructure.

5. Confirm canonical operator ordering constraints.

6. Confirm H/M/L transformation operators.

7. Confirm provenance transformation requirements.

8. Confirm exact validation-result state machine.

9. Confirm commit-authority boundary.

10. Define operator-specific reversibility/idempotence.

11. Implement deterministic validators.

12. Execute adversarial and regression tests.
```

---

# 110. Hard Boundaries

```text
PLACEHOLDER
!=
IMPLEMENTED

ADDRESSABLE
!=
VALIDATED

CAPABILITY
!=
AUTHORITY

PROPOSAL
!=
COMMIT

UNKNOWN/GAP
!=
PASS
```

Additional L01 operator boundaries:

```text
SENSED
!=
TRUE

CAPTURED
!=
COMPLETE

INGESTED
!=
TRUSTED

PARSED
!=
VALIDATED

NORMALIZED
!=
UNCHANGED

CANONICALIZED
!=
ORIGINAL

OBSERVATION
!=
REALITY

CORRELATION
!=
CAUSATION

AGGREGATED
!=
UNANIMOUS

REPEATED
!=
INDEPENDENT

LOCAL
!=
GLOBAL

HISTORICAL
!=
CURRENT

SIMULATED
!=
OBSERVED

TRANSFORMED
!=
INDEPENDENTLY CONFIRMED

QUARANTINED
!=
REJECTED

SUPERSEDED
!=
ERASED

VALID
!=
AUTHORIZED
```

---

# 111. RSCF Completion State

```yaml
rscf:

  claim:
    L01_SENSING_OBSERVATION requires a typed operator contract for
    acquiring, parsing, normalizing, binding, validating, comparing,
    aggregating, filtering, conflict-checking, reobserving, routing,
    and repairing observation state while preserving provenance,
    time, scope, regime, H/M/L scale, uncertainty, epistemic class,
    dependency lineage, and control-plane authority.

  claim_class:
    MODEL

  evidence:
    - supplied L01 operator placeholder
    - AMOS integrity principles
    - AMOS RSCF architecture
    - AMOS H/M/L architecture
    - AMOS provenance principles
    - AMOS information/operator patterns
    - AMOS control-plane patterns
    - L01 sibling contract structure

  provenance:
    origin_architect: Trang Phan
    architecture_family: AMOS
    primitive: L01_SENSING_OBSERVATION
    artifact: OPERATORS.md
    reconstruction_status: MODEL_DERIVED
    direct_L01_canon_status: GAP

  scope:
    AMOS_OS/COGNITIVE_MATRIX/L01_SENSING_OBSERVATION/OPERATORS

  regime:
    architecture specification / observation operator governance

  freshness:
    revalidate_when:
      - direct L01 operator canon becomes available
      - L01 definition changes
      - L01 variable contract changes
      - L01 H/M/L contract changes
      - L01 provenance contract changes
      - AMOS operator architecture changes
      - control-plane architecture changes
      - executable runtime becomes available

  dependencies:
    - L00_REALITY_ENVIRONMENT
    - L01_DEFINITION
    - L01_VARIABLES
    - L01_EQUATIONS
    - L01_INVARIANTS
    - L01_DEPENDENCIES
    - L01_HML
    - L01_MEMORY
    - L01_PROVENANCE
    - L01_CONTROL_PLANES
    - L01_RSCF
    - L01_FAILURE_MODES
    - L01_REPAIR
    - L01_PROTOCOLS

  competing:
    - direct canon may define a smaller operator registry
    - some proposed operators may belong to infrastructure rather than L01
    - multimodal/domain-specific observation may require specialized operators
    - persistent mutation operators may belong exclusively to control-plane layers

  falsifiers:
    - direct canon materially contradicts this operator contract
    - canonical dependency analysis assigns these operations elsewhere
    - executable tests demonstrate incompatible operator semantics
    - proposed operator composition violates canonical invariants
    - canonical authority rules prohibit proposed state transitions

  uncertainty:
    evidence: high
    model: medium
    scope: medium_high
    temporal: medium
    causal: medium
    execution: high
    provenance_independence: medium_high

  confidence_ceiling:
    structural AMOS MODEL only;
    not direct-canon-complete,
    not runtime-validated,
    not empirically universal
```

---

# 112. Completion State

```yaml
completion_state:

  source_canon_references:
    status: PARTIAL / GAP_BOUNDED

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
    status: MODEL_COMPLETE

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
    status: MODEL_COMPLETE

  uncertainty_confidence:
    status: MODEL_COMPLETE

  failure_modes:
    status: MODEL_COMPLETE

  repair_recovery:
    status: MODEL_COMPLETE

  tests_validators:
    status: MODEL_COMPLETE / UNEXECUTED

  falsifiers:
    status: MODEL_COMPLETE

  direct_canon_validation:
    status: GAP

  executable_implementation:
    status: GAP

  empirical_validation:
    status: GAP

  operational_validation:
    status: GAP

  overall_artifact:
    status: COMPLETE_FOR_DECLARED_MODEL_SCOPE

  conclusion_class:
    MODEL / CONDITIONAL
```

---

# 113. Final Contract

`L01_SENSING_OBSERVATION/OPERATORS.md` defines the proposed transformation surface between accessible sensing inputs and governed observation state.

The conceptual chain is:

```text
REALITY / ENVIRONMENT
↓
ACCESSIBLE SIGNAL
↓
SENSE / INGEST
↓
CAPTURE
↓
TYPE / PARSE
↓
NORMALIZE
↓
BIND CONTEXT
↓
BIND PROVENANCE
↓
ASSESS QUALITY / UNCERTAINTY
↓
VALIDATE
↓
COMPARE / AGGREGATE / PRESERVE COMPETING
↓
EMIT / QUARANTINE / REOBSERVE
↓
MEMORY OR DOWNSTREAM COGNITION
```

The operator layer must preserve:

```text
input identity
operator identity
operator version
source
observer
time
scope
regime
H/M/L scale
provenance
uncertainty
epistemic class
dependencies
conflicts
authority
information loss
```

Its strongest governing distinctions are:

[
\boxed{
Observation \neq Reality
}
]

[
\boxed{
Parsing \neq Validation
}
]

[
\boxed{
Transformation \neq IndependentEvidence
}
]

[
\boxed{
Correlation \neq Causation
}
]

[
\boxed{
Aggregation \neq Consensus
}
]

[
\boxed{
Local \neq Global
}
]

[
\boxed{
Capability \neq Authority
}
]

[
\boxed{
Proposal \neq Commit
}
]

[
\boxed{
Unknown \neq Pass
}
]

The strongest warranted status is:

```text
L01 OPERATOR CONTRACT
=
AMOS_MODEL
+
TYPED
+
PROVENANCE-BOUND
+
TEMPORALLY-BOUND
+
SCOPE/REGIME-BOUND
+
H/M/L-AWARE
+
UNCERTAINTY-PRESERVING
+
CONTROL-PLANE-GOVERNED
+
REPAIRABLE
+
SOURCE-CANON BOUNDED
+
RUNTIME UNVALIDATED
```

Accordingly:

```text
COMPLETE_FOR_DECLARED_MODEL_SCOPE
!=
DIRECT-CANON COMPLETE

DIRECT-CANON COMPLETE
!=
IMPLEMENTED

IMPLEMENTED
!=
VALIDATED
```

---

**Related:** [[L01_SENSING_OBSERVATION]] · [[L01_SENSING_OBSERVATION — Definition]] · [[L01_SENSING_OBSERVATION — Variables]] · [[L01_SENSING_OBSERVATION — Equations]] · [[L01_SENSING_OBSERVATION — Invariants]] · [[L01_SENSING_OBSERVATION — Dependencies]] · [[L01_SENSING_OBSERVATION — Hml]] · [[L01_SENSING_OBSERVATION — Memory]] · [[L01_SENSING_OBSERVATION — Control Planes]] · [[L01_SENSING_OBSERVATION — Provenance]] · [[L01_SENSING_OBSERVATION — Rscf]] · [[L01_SENSING_OBSERVATION — Failure Modes]] · [[L01_SENSING_OBSERVATION — Repair]] · [[L01_SENSING_OBSERVATION — Gap Matrix]] · [[L00_REALITY_ENVIRONMENT]] · [[00-Home]] · [[06-Knowledge-Base-MOC]]

```
```

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[COGNITIVE_MATRIX_MOC]] · [[00-Home]] · [[AMOS_RSCF_NODES]]
