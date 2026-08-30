---
title: L01 SENSING OBSERVATION PRIMITIVES COGNITIVE MATRIX README
type: cognitive
source: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L01_SENSING_OBSERVATION
tags:
- cognitive-matrix
- primitives
- matrix/l01-sensing-observation
- readme
- domain/cognitive-matrix
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

Here is the full `L01_SENSING_OBSERVATION/README.md` content to paste. I’m keeping the README as the **integration/index contract** for the L01 primitive rather than duplicating every sibling file in full.

---
tags:
  - amos
  - cognitive-matrix
  - l01
  - sensing-observation
  - readme
  - rscf
  - hml
  - provenance
  - control-plane
---

# L01_SENSING_OBSERVATION — README

**Class:** `COGNITIVE_PRIMITIVE_INTEGRATION_CONTRACT`
**Origin architect / steward:** Trang Phan
**Architecture:** `AMOS_OS / COGNITIVE_MATRIX`
**Primitive:** `L01_SENSING_OBSERVATION`
**Artifact:** `README.md`
**Role:** `PRIMITIVE ENTRYPOINT / INTEGRATION MAP / CONTRACT INDEX`
**Status:** `AMOS_MODEL / SOURCE-CANON BOUNDED / UNVALIDATED`

> **Epistemic boundary:** this README defines the proposed integration contract for `L01_SENSING_OBSERVATION`. It organizes the primitive's purpose, boundaries, interfaces, state, dependencies, governance, evidence requirements, failure handling, and sibling artifacts. It does not establish that L01 has been implemented, executed, formally verified, empirically validated, or canonically completed.

---

# 0. Executive Definition

`L01_SENSING_OBSERVATION` is the proposed AMOS cognitive primitive responsible for converting available reality/environment contact into explicitly typed observation state suitable for governed downstream cognition.

Its conceptual position is:

```text
L00_REALITY_ENVIRONMENT
↓
AVAILABLE REALITY CONTACT
↓
L01_SENSING_OBSERVATION
↓
TYPED OBSERVATION STATE
↓
DOWNSTREAM COGNITION
```

Its core architectural responsibility is:

[
\boxed{
RealityContact
\rightarrow
Sensing
\rightarrow
ObservationCandidate
\rightarrow
TypedObservation
\rightarrow
GovernedObservation
}
]

while preserving the distinctions:

[
\boxed{
Reality
\neq
Signal
\neq
Observation
\neq
Interpretation
}
]

and:

```text
OBSERVATION
!= SOURCE_CLAIM

OBSERVATION
!= MODEL_OUTPUT

OBSERVATION
!= SIMULATION

OBSERVATION
!= MEMORY

OBSERVATION
!= DECISION
```

L01 is therefore a **reality-contact and observation-formation boundary**, not a universal truth engine.

---

# 1. Purpose

The purpose of L01 is to provide AMOS with a governed interface for representing what was sensed, observed, reported, retrieved, measured, or otherwise made available from an environment without silently promoting that representation beyond the evidence supporting it.

L01 should preserve:

```text
what was received
where it came from
who or what observed it
when it was observed
through which modality
under what conditions
how it was transformed
where it applies
which regime applies
which H/M/L scale applies
what uncertainty remains
whether conflicts exist
whether it is admissible downstream
```

The purpose is not:

```text
to declare incoming information true
to infer ultimate meaning
to infer causation automatically
to predict future state automatically
to decide what action should occur
to authorize actions
to erase uncertainty
to convert missing information into assumptions
```

---

# 2. Architectural Role

L01 occupies the conceptual boundary between:

```text
EXTERNAL / ADDRESSABLE REALITY STATE
```

and:

```text
INTERNAL COGNITIVE REPRESENTATION
```

The primitive should make that boundary explicit.

Conceptually:

[
O_t
===

\mathcal{S}
(
E_t,
M_t,
B_t,
C_t
)
]

where:

- \(E_t\) = available environment state;
- \(M_t\) = sensing modality/interface;
- \(B_t\) = observer or sensor state;
- \(C_t\) = contextual conditions;
- \(O_t\) = observation state.

This is an `AMOS_MODEL` equation.

It is not asserted as universal sensing mathematics.

---

# 3. Source / Canon References

## 3.1 Origin

```yaml
origin:
  architect: Trang Phan
  steward: Trang Phan

architecture_family:
  - AMOS
  - AMOS OS
  - AMOS Cognitive Matrix
  - AMOS RSCF
  - AMOS H/M/L
```

## 3.2 Relevant Corpus Families

Relevant AMOS architecture families include:

```text
AMOS_CORE lineage
AMOS Full Brain OS
AMOS Cognition
AMOS Reality Architecture
AMOS Universal Field Architecture
AMOS Multimodal Perception
AMOS Information Architecture
AMOS RSCF
AMOS H/M/L
AMOS provenance topology
AMOS epistemic regimes
AMOS uncertainty governance
AMOS causal hierarchy
AMOS information-boundary governance
AMOS memory governance
AMOS infrastructure/control-plane architecture
L00_REALITY_ENVIRONMENT
L01_SENSING_OBSERVATION sibling contracts
```

## 3.3 Source Status

```yaml
source_status:

  origin_architect:
    status: DECLARED
    value: Trang Phan

  sensing_reality_contact:
    status: CORPUS_ALIGNED

  observation_reality_distinction:
    status: CORPUS_ALIGNED

  provenance_preservation:
    status: CORPUS_ALIGNED

  uncertainty_preservation:
    status: CORPUS_ALIGNED

  HML_reasoning:
    status: CORPUS_ALIGNED

  control_plane_governance:
    status: CORPUS_ALIGNED

  exact_L01_canonical_definition:
    status: UNKNOWN/GAP

  exact_L01_canonical_schema:
    status: UNKNOWN/GAP

  exact_L01_canonical_operator_registry:
    status: UNKNOWN/GAP

  executable_L01_runtime:
    status: UNKNOWN/GAP

  empirical_validation:
    status: UNKNOWN/GAP
```

Therefore:

```text
CORPUS_ALIGNED
!= DIRECT_CANON_VERIFIED

MODEL_COMPLETE
!= CANON_COMPLETE

CANON_COMPLETE
!= IMPLEMENTED

IMPLEMENTED
!= VALIDATED
```

---

# 4. Definition and Scope

`L01_SENSING_OBSERVATION` is the AMOS primitive responsible for forming governed observation state from available environment/reality-contact inputs.

Potential observation sources include:

```text
physical sensors
human observations
human reports
documents
files
APIs
databases
software instrumentation
system telemetry
environmental telemetry
visual inputs
audio inputs
text inputs
structured records
multimodal inputs
retrieval systems
external tools
user-provided information
```

The epistemic class of the input must remain explicit.

For example:

```text
physical measurement
→ OBSERVATION candidate

human report
→ REPORTED_OBSERVATION / SOURCE_CLAIM

document statement
→ SOURCE_CLAIM

model forecast
→ MODEL

simulation output
→ SYNTHETIC / MODEL

computed transformation
→ DERIVED
```

unless stronger classification is independently justified.

---

# 5. Out of Scope

L01 does not independently own:

```text
ultimate ontology
truth determination
full semantic interpretation
causal inference
prediction
planning
decision optimization
ethical authorization
external action
durable commit authority
long-term memory policy
domain-specific scientific validation
```

L01 may provide evidence to those systems.

It does not replace them.

---

# 6. Typed Inputs

```yaml
L01Input:

  environment:
    type:
      - L00EnvironmentState
      - EnvironmentRef
      - UNKNOWN

  signal:
    type:
      - PhysicalSignal
      - DigitalSignal
      - HumanReport
      - DocumentInput
      - ToolOutput
      - APIOutput
      - RetrievedObject
      - StructuredRecord
      - MultimodalInput
      - UNKNOWN

  source:
    type: SourceRef | UNKNOWN

  observer:
    type:
      - HumanObserverRef
      - SensorRef
      - AgentRef
      - ToolRef
      - SystemRef
      - UNKNOWN

  modality:
    type: ModalityRef | UNKNOWN

  event_time:
    type: Timestamp | TimeEnvelope | UNKNOWN

  observation_time:
    type: Timestamp | TimeEnvelope | UNKNOWN

  retrieval_time:
    type: Timestamp | TimeEnvelope | UNKNOWN

  scope:
    type: ScopeEnvelope | UNKNOWN

  regime:
    type: RegimeRef | UNKNOWN

  HML:
    type: H | M | L | UNKNOWN

  provenance:
    type:
      - ProvenanceBundle
      - PartialProvenance
      - UNKNOWN

  uncertainty:
    type: UncertaintyVector

  authority_context:
    type: AuthorityContext | null
```

---

# 7. Typed Outputs

```yaml
L01Output:

  observation_id:
    type: ObservationId

  observation:
    type: ObservationCandidate | GovernedObservation

  observation_class:
    type:
      - DIRECT_OBSERVATION
      - REPORTED_OBSERVATION
      - TRANSFORMED_OBSERVATION
      - DERIVED_OBSERVATION
      - SYNTHETIC_OBSERVATION
      - UNKNOWN

  epistemic_class:
    type:
      - OBSERVATION
      - SOURCE_CLAIM
      - DERIVED
      - MODEL
      - UNKNOWN

  provenance:
    type: ProvenanceBundle | PartialProvenance

  temporal_envelope:
    type: TemporalEnvelope

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeRef | UNKNOWN

  HML:
    type: H | M | L | UNKNOWN

  uncertainty:
    type: UncertaintyVector

  validation_state:
    type:
      - PASS
      - CONDITIONAL
      - FAIL
      - QUARANTINE
      - UNKNOWN

  admissibility:
    type:
      - ADMISSIBLE
      - CONDITIONALLY_ADMISSIBLE
      - INADMISSIBLE
      - QUARANTINED
      - UNKNOWN

  conflicts:
    type: ObservationConflict[]

  gaps:
    type: GapRecord[]
```

---

# 8. State Variables

Minimum proposed state variables:

```text
E = environment/reality-contact state
S = sensed signal
O = observation state
B = observer/sensor state
M = modality
Q = sensing/measurement quality
N = noise state
U = uncertainty
P = provenance
T = temporal state
C = scope/context
G = regime
H = H/M/L coordinate
V = validation state
A = admissibility state
X = transformation state
K = conflict state
F = freshness state
R = revocation/supersession state
```

Candidate observation tensor:

[
\boxed{
T_{obs}
=======

T[
source,
observer,
modality,
time,
scope,
regime,
HML,
signal,
quality,
uncertainty,
provenance,
validation
]
}
]

This tensor is an `AMOS_MODEL`.

---

# 9. Operators

Candidate L01 operator registry:

```text
SENSE
CAPTURE
OBSERVE
REGISTER
NORMALIZE
FILTER
ALIGN
TIMESTAMP
TYPE
CLASSIFY_MODALITY
ATTACH_PROVENANCE
BOUND_SCOPE
BOUND_REGIME
ASSIGN_HML
ESTIMATE_UNCERTAINTY
CHECK_QUALITY
CHECK_FRESHNESS
CHECK_CONFLICT
VALIDATE
ADMIT
QUARANTINE
REJECT
REOBSERVE
COMPARE
SUPERSEDE
INVALIDATE
ROUTE
```

Operator existence in this contract means:

```text
ARCHITECTURALLY ADDRESSABLE
```

not:

```text
EXECUTABLY IMPLEMENTED
```

---

# 10. Core Invariants

```text
L01-INV-001  Reality/Observation Separation
L01-INV-002  Signal/Reality Separation
L01-INV-003  Observation/Interpretation Separation
L01-INV-004  Observation/Source-Claim Separation
L01-INV-005  Observation/Model Separation
L01-INV-006  Observation/Simulation Separation
L01-INV-007  Provenance Preservation
L01-INV-008  Uncertainty Preservation
L01-INV-009  Temporal Preservation
L01-INV-010  Scope Preservation
L01-INV-011  Regime Preservation
L01-INV-012  H/M/L Preservation
L01-INV-013  Transformation Traceability
L01-INV-014  Unknown Preservation
L01-INV-015  Missingness Non-Promotion
L01-INV-016  Validation/Truth Separation
L01-INV-017  Capability/Authority Separation
L01-INV-018  Proposal/Commit Separation
L01-INV-019  Selective Invalidation
L01-INV-020  Downstream Traceability
L01-INV-021  Historical Observation Immutability
L01-INV-022  Supersession Traceability
```

---

# 11. Fundamental Epistemic Invariants

[
\boxed{
Observation \neq Reality
}
]

[
\boxed{
Signal \neq Reality
}
]

[
\boxed{
Observation \neq Interpretation
}
]

[
\boxed{
SourceClaim \neq DirectObservation
}
]

[
\boxed{
SimulationOutput \neq ObservedReality
}
]

[
\boxed{
NotObserved(x)
\not\Rightarrow
NotExists(x)
}
]

[
\boxed{
Validation \neq Truth
}
]

[
\boxed{
Unknown \neq Pass
}
]

---

# 12. Dependencies

## 12.1 Primary Upstream Dependency

```text
L00_REALITY_ENVIRONMENT
```

Conceptually:

```text
L00_REALITY_ENVIRONMENT
↓
L01_SENSING_OBSERVATION
```

L00 provides the addressable environment/reality context.

L01 forms observation state from available contact with that context.

## 12.2 Supporting Dependencies

```text
source identity
sensor/interface identity
modality registry
time representation
scope representation
regime representation
H/M/L representation
provenance infrastructure
uncertainty representation
validation contracts
control-plane authority
memory-admission contracts
```

## 12.3 Downstream Dependency

Downstream cognition may depend upon L01 for:

```text
evidence-bearing observation state
```

but downstream components must preserve L01 provenance and uncertainty where those properties remain load-bearing.

---

# 13. H/M/L Applicability

L01 applies recursively across:

```text
L = local observation
M = subsystem observation
H = system/environment observation
```

## L-Level

Examples:

```text
single measurement
single signal
single source statement
single event
single image region
single tool response
single sensor reading
```

Purpose:

```text
preserve local observation fidelity
```

## M-Level

Examples:

```text
sensor cluster
observation window
multimodal bundle
subsystem state
aggregated measurements
source group
```

Purpose:

```text
form subsystem observation while preserving decisive L-level evidence
```

## H-Level

Examples:

```text
environmental state
system-wide condition
cross-subsystem observation
global observation summary
```

Purpose:

```text
form decision-usable high-level observation while retaining recoverability
```

---

# 14. Cross-Scale Invariant

If:

[
O_L
\rightarrow
O_M
\rightarrow
O_H
]

then load-bearing evidence should remain recoverable:

[
\boxed{
O_H
\rightsquigarrow
O_M
\rightsquigarrow
O_L
}
]

where required for verification, contradiction analysis, repair, or audit.

Aggregation must not manufacture evidence.

[
\boxed{
Aggregation
\neq
IndependentEvidence
}
]

---

# 15. Control-Plane Requirements

L01 should operate beneath explicit control-plane governance.

The control plane may govern:

```text
sensor/tool availability
source access
data-access authority
modality availability
observation admission
memory admission
external disclosure
transformation permissions
validation requirements
agent permissions
durable commit
quarantine
supersession
invalidation
revalidation
revocation
```

The cognitive worker may propose state.

The control plane determines whether the proposed transition is authorized.

---

# 16. Capability / Authority Boundary

A component may possess the technical capability to:

```text
read
sense
retrieve
capture
transform
classify
store
transmit
```

without possessing authority to perform that operation.

Therefore:

[
\boxed{
Capability
\neq
Authority
}
]

---

# 17. Proposal / Commit Boundary

L01 workers may produce:

```text
ObservationCandidate
ValidationProposal
AdmissionProposal
QuarantineProposal
SupersessionProposal
InvalidationProposal
MemoryAdmissionProposal
```

but:

[
\boxed{
Proposal
\neq
Commit
}
]

Durable state changes require the appropriate authority and validation.

---

# 18. Commit-Time Validation

Before consequential admission or durable transition, check:

```text
observation identity
source identity
observer identity
modality
provenance
freshness
time
scope
regime
H/M/L
uncertainty
conflict state
transformation lineage
authority
revocation state
```

If a load-bearing property changes before commit:

```text
REVALIDATE
```

rather than relying on the earlier result.

---

# 19. Agents

Candidate L01 agent roles:

```text
Sensing Agent
Observation Capture Agent
Multimodal Observation Agent
Source Resolution Agent
Observation Validation Agent
Observation Quality Agent
Temporal Alignment Agent
Provenance Agent
Conflict Detection Agent
Reobservation Agent
Observation Repair Agent
Observation Audit Agent
Control-Plane Agent
```

These are architectural roles.

```text
ROLE
!= DEPLOYED AGENT
```

---

# 20. Skills

Candidate supporting skill families:

```text
multimodal perception
structured document parsing
source reading
source verification
provenance tracing
temporal alignment
scope/regime validation
H/M/L mapping
measurement-integrity auditing
uncertainty representation
conflict detection
information-boundary governance
memory admission governance
RSCF modeling
repair/recovery
```

A skill may provide capability.

It does not independently grant authority.

---

# 21. Primary Workflow

```text
L00 ENVIRONMENT STATE
↓
AVAILABLE CONTACT
↓
SIGNAL
↓
SENSE
↓
CAPTURE
↓
IDENTIFY SOURCE
↓
IDENTIFY OBSERVER / SENSOR
↓
IDENTIFY MODALITY
↓
TIMESTAMP
↓
CREATE OBSERVATION CANDIDATE
↓
TYPE EPISTEMIC CLASS
↓
ATTACH PROVENANCE
↓
BIND SCOPE
↓
BIND REGIME
↓
BIND H/M/L
↓
ESTIMATE UNCERTAINTY
↓
CHECK QUALITY
↓
CHECK FRESHNESS
↓
CHECK CONFLICT
↓
VALIDATE
↓
ADMIT / CONDITIONAL / QUARANTINE / REJECT
↓
ROUTE DOWNSTREAM
```

---

# 22. Reobservation Workflow

```text
EXISTING OBSERVATION
↓
DETECT STALENESS / CONFLICT / UNCERTAINTY
↓
IDENTIFY DECISION-CHANGING GAP
↓
REQUEST REOBSERVATION
↓
CAPTURE NEW OBSERVATION
↓
PRESERVE OLD OBSERVATION
↓
COMPARE
↓
CONFIRM / COMPETE / SUPERSEDE
↓
SELECTIVELY REVALIDATE DEPENDENTS
```

Historical observations should not simply be overwritten.

---

# 23. Conflict Workflow

```text
OBSERVATION A
+
OBSERVATION B
↓
CHECK SOURCE
↓
CHECK ANCESTRY
↓
CHECK TIME
↓
CHECK SCOPE
↓
CHECK REGIME
↓
CHECK H/M/L
↓
CHECK MODALITY
↓
CHECK TRANSFORMATIONS
↓
CHECK UNCERTAINTY
↓
FIND CHEAPEST HIGH-INFORMATION DISCRIMINATOR
↓
RESOLVE OR PRESERVE COMPETING
```

If discriminating evidence is insufficient:

```text
COMPETING
```

must remain visible.

---

# 24. Protocols

Candidate L01 protocol objects:

```text
SensingRequest
SensingResult
ObservationCandidate
ObservationValidationRequest
ObservationValidationResult
ObservationConflictEvent
CompetingObservationSet
ObservationReobservationRequest
ObservationSupersessionProposal
ObservationInvalidationProposal
ObservationRoutingRequest
MemoryAdmissionProposal
StateTransitionProposal
StateTransitionCommit
AuditEvent
```

Consequential protocols should carry:

```text
identity
time
scope
regime
H/M/L
provenance
uncertainty
authority context
validation state
```

---

# 25. Memory Relationship

L01 may produce observations that become candidates for memory.

It does not imply:

```text
OBSERVED
=
MEMORY_ADMITTED
```

Memory admission should remain separately governed.

Conceptually:

```text
L01 OBSERVATION
↓
MEMORY ADMISSION PROPOSAL
↓
MEMORY GOVERNANCE
↓
COMMIT / QUARANTINE / REJECT
```

The original observation provenance should remain recoverable after admission.

---

# 26. Evidence / Provenance

Every consequential observation should preserve, where available:

```text
source identity
source ancestry
observer identity
sensor/tool identity
modality
event time
observation time
retrieval time
processing time
environment context
scope
regime
H/M/L
transformations
validation history
uncertainty
dependencies
supersession history
```

A downstream claim should be able to trace its load-bearing observation ancestry.

---

# 27. Provenance Independence

Multiple observations do not automatically constitute independent confirmation.

If:

```text
Observation A ← Source X
Observation B ← Source X
Observation C ← Source X
```

then:

```text
A + B + C
```

must not automatically be counted as three independent evidentiary origins.

Therefore:

[
\boxed{
Repetition
\neq
Independence
}
]

and:

[
\boxed{
MultipleDescendants(Source_X)
\neq
MultipleIndependentSources
}
]

---

# 28. Uncertainty

Candidate L01 uncertainty vector:

[
\boxed{
U_{L01}
=======

[
U_{signal},
U_{measurement},
U_{observer},
U_{source},
U_{temporal},
U_{scope},
U_{regime},
U_{transformation},
U_{provenance}
]
}
]

Each component may be:

```text
KNOWN
ESTIMATED
BOUNDED
UNKNOWN
```

Unknown uncertainty must not silently become zero uncertainty.

---

# 29. Confidence Ceiling

Conceptually:

[
\boxed{
C(O)
\le
\min(
C_{signal},
C_{measurement},
C_{source},
C_{provenance},
C_{scope},
C_{regime}
)
}
]

for load-bearing premises.

This is an `AMOS_MODEL` confidence rule.

Independent evidence may raise support only when its independence and applicability are established.

Compression, repetition, summarization, or fluency cannot raise confidence by themselves.

---

# 30. Failure Modes

Minimum failure registry:

```text
FM-L01-001  Reality/Observation Collapse
FM-L01-002  Signal/Reality Collapse
FM-L01-003  Observation/Interpretation Collapse
FM-L01-004  Source-Claim Promotion
FM-L01-005  Model/Observation Confusion
FM-L01-006  Simulation Contamination
FM-L01-007  Missing Provenance
FM-L01-008  Temporal Misalignment
FM-L01-009  Scope Leakage
FM-L01-010  Regime Leakage
FM-L01-011  H/M/L Collapse
FM-L01-012  Noise Promotion
FM-L01-013  Signal Suppression
FM-L01-014  Missingness Promotion
FM-L01-015  Stale Observation
FM-L01-016  False Precision
FM-L01-017  False Independence
FM-L01-018  Unknown-as-Pass
FM-L01-019  Capability/Authority Confusion
FM-L01-020  Proposal/Commit Confusion
FM-L01-021  Provenance Loss
FM-L01-022  Over-Aggregation
FM-L01-023  Under-Invalidation
FM-L01-024  Over-Invalidation
FM-L01-025  Observer Contamination
FM-L01-026  Unauthorized Observation
FM-L01-027  Unauthorized Memory Admission
FM-L01-028  Historical Observation Rewrite
FM-L01-029  Supersession Lineage Loss
FM-L01-030  Primitive Scope Expansion
```

---

# 31. Repair / Recovery

General repair path:

```text
DETECT FAILURE
↓
FREEZE AFFECTED PROMOTION
↓
LOCATE EARLIEST FAILED PREMISE
↓
CLASSIFY FAILURE
↓
TRACE DEPENDENCY DESCENDANTS
↓
PRESERVE UNAFFECTED STATE
↓
RECOVER SOURCE / TIME / SCOPE / REGIME IF EVIDENCE EXISTS
↓
REOBSERVE IF POSSIBLE
↓
DO NOT INVENT MISSING EVIDENCE
↓
RETYPE / REBOUND / REVALIDATE
↓
CONFIRM / COMPETE / SUPERSEDE / QUARANTINE / INVALIDATE
↓
SELECTIVELY REVALIDATE DOWNSTREAM STATE
```

The repair target should be the earliest material failure, not merely its latest symptom.

---

# 32. Selective Invalidation

If observation \(O_i\) fails:

[
Affected(O_i)
=============

Descendants_{load-bearing}\(O_i\)
]

Only downstream objects materially dependent upon \(O_i\) should be invalidated or revalidated.

Therefore:

```text
LOCAL FAILURE
!= AUTOMATIC GLOBAL RESET
```

---

# 33. Tests / Validators

Minimum validator registry:

```text
VALIDATOR_REALITY_OBSERVATION_SEPARATION
VALIDATOR_SIGNAL_REALITY_SEPARATION
VALIDATOR_SOURCE_CLASS
VALIDATOR_OBSERVATION_TYPE
VALIDATOR_MODALITY
VALIDATOR_OBSERVER
VALIDATOR_TIMESTAMP
VALIDATOR_SCOPE
VALIDATOR_REGIME
VALIDATOR_HML
VALIDATOR_PROVENANCE
VALIDATOR_PROVENANCE_INDEPENDENCE
VALIDATOR_UNCERTAINTY
VALIDATOR_TRANSFORMATION_LINEAGE
VALIDATOR_FRESHNESS
VALIDATOR_CONFLICT
VALIDATOR_SIMULATION_BOUNDARY
VALIDATOR_MISSINGNESS
VALIDATOR_CAPABILITY_AUTHORITY
VALIDATOR_PROPOSAL_COMMIT
VALIDATOR_MEMORY_ADMISSION
VALIDATOR_DOWNSTREAM_DEPENDENCY
VALIDATOR_SUPERSESSION
```

---

# 34. Minimum Test Suite

```text
TEST_L01_001
raw signal does not automatically become validated observation

TEST_L01_002
observation does not become reality state

TEST_L01_003
source claim does not automatically become direct observation

TEST_L01_004
model output remains MODEL unless separately grounded

TEST_L01_005
simulation output remains synthetic

TEST_L01_006
UNKNOWN source remains UNKNOWN

TEST_L01_007
UNKNOWN scope does not become universal scope

TEST_L01_008
UNKNOWN regime does not become universal applicability

TEST_L01_009
event time remains distinct from observation time

TEST_L01_010
observation time remains distinct from retrieval time

TEST_L01_011
transformation preserves provenance

TEST_L01_012
summarization does not erase uncertainty

TEST_L01_013
L evidence remains recoverable from M aggregation

TEST_L01_014
M evidence remains recoverable from H aggregation

TEST_L01_015
failure to observe does not automatically establish absence

TEST_L01_016
stale observations trigger freshness review

TEST_L01_017
unresolved conflicts remain COMPETING

TEST_L01_018
correlated descendants do not create false independence

TEST_L01_019
sensor capability does not imply sensing authority

TEST_L01_020
observation proposal does not equal durable commit

TEST_L01_021
observation does not automatically enter memory

TEST_L01_022
failed observation selectively invalidates dependents

TEST_L01_023
unrelated observations survive selective invalidation

TEST_L01_024
repair does not fabricate missing evidence

TEST_L01_025
reobservation creates a new observation event

TEST_L01_026
superseded observation remains historically traceable

TEST_L01_027
downstream interpretation cannot silently rewrite observation

TEST_L01_028
synthetic input cannot silently cross into empirical evidence class

TEST_L01_029
revoked source status triggers affected-state revalidation

TEST_L01_030
README completeness does not promote runtime implementation status
```

---

# 35. Adversarial Validation

L01 should eventually be tested against:

```text
spoofed sensor data
forged sources
stale APIs
duplicate sources
correlated evidence
sensor drift
timestamp manipulation
unit mismatch
missing metadata
adversarial documents
prompt injection
synthetic-as-empirical data
simulation/reality confusion
misleading aggregation
scope widening
regime widening
H/M/L mismatch
selective reporting
missing-data bias
observer bias
tool failures
API failures
partial retrieval
source revocation
provenance tampering
unauthorized sensing
unauthorized memory admission
race conditions between validation and commit
```

A test specification is not evidence that the test has been executed.

```text
TEST_DEFINED
!= TEST_EXECUTED

TEST_EXECUTED
!= TEST_PASSED
```

---

# 36. Falsifiers

This README and its integrated model should be revised if:

```text
direct L01 canon materially contradicts the proposed definition

canonical AMOS architecture assigns L01 a different primitive role

canonical L00/L01 boundary differs materially

canonical downstream boundary differs materially

canonical observation epistemic classes conflict with these classes

canonical H/M/L semantics conflict with this mapping

canonical provenance rules contradict the proposed lineage model

canonical control-plane architecture assigns different authority

canonical memory architecture contradicts the proposed admission boundary

formal analysis exposes incompatible invariants

runtime implementation demonstrates incompatible interface requirements

empirical validation demonstrates systematic failure of a proposed sensing assumption
```

---

# 37. Gap Matrix

```yaml
gap_matrix:

  direct_L01_README_canon:
    status: GAP
    criticality: CRITICAL

  canonical_L01_definition:
    status: GAP
    criticality: CRITICAL

  canonical_L00_L01_boundary:
    status: GAP
    criticality: CRITICAL

  canonical_L01_downstream_boundary:
    status: GAP
    criticality: CRITICAL

  canonical_observation_schema:
    status: GAP
    criticality: CRITICAL

  canonical_variable_registry:
    status: GAP
    criticality: DECISION_RELEVANT

  canonical_operator_registry:
    status: GAP
    criticality: DECISION_RELEVANT

  canonical_equations:
    status: GAP
    criticality: DECISION_RELEVANT

  canonical_HML_mapping:
    status: GAP
    criticality: DECISION_RELEVANT

  canonical_provenance_contract:
    status: GAP
    criticality: CRITICAL

  canonical_memory_relationship:
    status: GAP
    criticality: DECISION_RELEVANT

  canonical_control_plane_ownership:
    status: GAP
    criticality: CRITICAL

  canonical_agent_registry:
    status: GAP
    criticality: EXPLANATORY

  canonical_skill_registry:
    status: GAP
    criticality: EXPLANATORY

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
    status: MODEL_COMPLETE_UNEXECUTED

  executable_runtime:
    status: GAP
    criticality: CRITICAL

  empirical_validation:
    status: GAP
    criticality: CRITICAL
```

---

# 38. Gap Resolution Priority

```text
1. Locate direct canonical L01 material.

2. Confirm exact L00 → L01 interface.

3. Confirm exact L01 → downstream cognition interface.

4. Confirm canonical observation classes.

5. Confirm canonical variable registry.

6. Confirm canonical operators.

7. Confirm canonical equations.

8. Confirm canonical provenance requirements.

9. Confirm canonical uncertainty representation.

10. Confirm canonical H/M/L semantics.

11. Confirm memory-admission boundary.

12. Confirm control-plane ownership.

13. Confirm agent/skill responsibilities.

14. Implement deterministic validators.

15. Execute unit tests.

16. Execute adversarial tests.

17. Validate selective invalidation.

18. Validate reobservation/supersession behavior.

19. Validate runtime authority boundaries.

20. Promote status only from actual evidence.
```

---

# 39. Sibling Artifact Map

The complete L01 primitive should be decomposed across:

```text
L01_SENSING_OBSERVATION/
│
├── README.md
├── PURPOSE.md
├── DEFINITION.md
├── VARIABLES.md
├── EQUATIONS.md
├── OPERATORS.md
├── INVARIANTS.md
├── DEPENDENCIES.md
├── HML.md
├── MEMORY.md
├── AGENTS.md
├── SKILLS.md
├── WORKFLOWS.md
├── PROTOCOLS.md
├── CONTROL_PLANES.md
├── PROVENANCE.md
├── RSCF.md
├── FAILURE_MODES.md
├── REPAIR.md
└── GAP_MATRIX.md
```

Each artifact owns a different part of the contract.

---

# 40. Artifact Responsibilities

```yaml
artifact_responsibilities:

  README.md:
    owns:
      - primitive integration
      - navigation
      - executive contract
      - cross-file consistency

  PURPOSE.md:
    owns:
      - why L01 exists
      - architectural intent
      - responsibility boundary

  DEFINITION.md:
    owns:
      - formal definition
      - inclusion/exclusion boundary
      - semantic classes

  VARIABLES.md:
    owns:
      - typed state
      - variable registry
      - domains and units

  EQUATIONS.md:
    owns:
      - formal relations
      - transition equations
      - assumptions

  OPERATORS.md:
    owns:
      - allowed transformations
      - operator preconditions
      - operator effects

  INVARIANTS.md:
    owns:
      - non-negotiable properties
      - preservation requirements

  DEPENDENCIES.md:
    owns:
      - upstream/downstream relationships
      - dependency graph

  HML.md:
    owns:
      - high/middle/local applicability
      - cross-scale mappings

  MEMORY.md:
    owns:
      - observation-memory relationship
      - admission and recall boundaries

  AGENTS.md:
    owns:
      - agent roles
      - responsibilities
      - authority limitations

  SKILLS.md:
    owns:
      - capability modules
      - skill routing
      - capability boundaries

  WORKFLOWS.md:
    owns:
      - operational sequences
      - branching/recovery flows

  PROTOCOLS.md:
    owns:
      - message/state-transition contracts
      - protocol objects

  CONTROL_PLANES.md:
    owns:
      - authority
      - commit
      - validation
      - governance

  PROVENANCE.md:
    owns:
      - evidence lineage
      - source ancestry
      - independence

  RSCF.md:
    owns:
      - claim/evidence/dependency structure
      - competing hypotheses
      - confidence ceilings

  FAILURE_MODES.md:
    owns:
      - failure taxonomy
      - detection conditions

  REPAIR.md:
    owns:
      - recovery
      - rollback
      - selective invalidation

  GAP_MATRIX.md:
    owns:
      - missing canon
      - missing implementation
      - validation gaps
      - completion priorities
```

---

# 41. Cross-File Consistency Rules

The README must not override a more specific sibling contract without an explicit canonical update.

Priority conceptually follows:

```text
DIRECT CANON
>
VALIDATED SPECIALIST CONTRACT
>
SPECIFIC SIBLING CONTRACT
>
README SUMMARY
>
MODEL INFERENCE
>
UNKNOWN
```

If sibling artifacts disagree:

```text
DO NOT SILENTLY MERGE
```

Instead:

```text
DETECT CONFLICT
↓
PRESERVE BOTH STATES
↓
TRACE PROVENANCE
↓
CHECK VERSION / SCOPE / REGIME
↓
IDENTIFY AUTHORITATIVE SOURCE
↓
RESOLVE OR MARK COMPETING
```

---

# 42. Primitive State Lifecycle

Candidate lifecycle:

```text
PLACEHOLDER
↓
MODEL_SPECIFIED
↓
CANON_RECONCILED
↓
IMPLEMENTED
↓
TESTED
↓
VALIDATED
↓
OPERATIONAL
```

Transitions must not be assumed.

For example:

```text
MODEL_SPECIFIED
!= IMPLEMENTED

IMPLEMENTED
!= TESTED

TESTED
!= VALIDATED

VALIDATED
!= UNIVERSALLY VALID
```

---

# 43. Hard Boundaries

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

L01-specific boundaries:

```text
REALITY
!=
OBSERVATION

SIGNAL
!=
REALITY

SIGNAL
!=
VALIDATED_OBSERVATION

OBSERVATION
!=
INTERPRETATION

OBSERVATION
!=
SOURCE_CLAIM

OBSERVATION
!=
MODEL_OUTPUT

OBSERVATION
!=
SIMULATION

RETRIEVAL
!=
DIRECT_SENSING

RETRIEVED_INFORMATION
!=
DIRECT_OBSERVATION

SOURCE_CLAIM
!=
EMPIRICAL_FACT

NOT_OBSERVED
!=
DOES_NOT_EXIST

MULTIPLE_DESCENDANTS
!=
INDEPENDENT_CONFIRMATION

VALIDATION
!=
TRUTH

FRESH
!=
TRUE

PROVENANCED
!=
TRUE

HIGH_CONFIDENCE
!=
CERTAINTY

AGGREGATION
!=
NEW_EVIDENCE

TRANSFORMATION
!=
NEW_OBSERVATION

MEMORY
!=
REALITY

DERIVATION
!=
OBSERVATION

README_COMPLETE
!=
PRIMITIVE_IMPLEMENTED
```

---

# 44. Evidence / Provenance of This README

```yaml
artifact_provenance:

  artifact:
    L01_SENSING_OBSERVATION/README.md

  origin_architect:
    Trang Phan

  supplied_basis:
    - user-supplied L01 README placeholder
    - established L01 sibling contract context
    - available AMOS architecture context

  derivation:
    class: AMOS_MODEL_RECONSTRUCTION

  direct_L01_README_canon:
    status: GAP

  executable_validation:
    status: NOT_EXECUTED

  empirical_validation:
    status: NOT_ESTABLISHED
```

This README must not become self-validating evidence for its own reconstructed architecture.

---

# 45. Uncertainty Vector

```yaml
uncertainty:

  evidence:
    level: HIGH
    reason: direct canonical L01 README contract has not been established

  model:
    level: MEDIUM
    reason: architecture is internally coherent but partly reconstructed

  scope:
    level: MEDIUM

  temporal:
    level: MEDIUM

  causal:
    level: MEDIUM

  execution:
    level: HIGH
    reason: executable L01 runtime is not established by this artifact

  provenance_independence:
    level: MEDIUM_HIGH
```

---

# 46. Confidence Ceiling

The strongest warranted conclusion is:

```text
STRUCTURALLY COHERENT AMOS MODEL
```

not:

```text
DIRECT-CANON VERIFIED
```

not:

```text
IMPLEMENTED
```

not:

```text
RUNTIME VALIDATED
```

not:

```text
EMPIRICALLY VERIFIED
```

Therefore:

[
\boxed{
C_{L01}
\le
C_{weakest\ load-bearing\ premise}
}
]

unless independently revalidated.

---

# 47. RSCF Completion State

```yaml
rscf:

  claim:
    L01_SENSING_OBSERVATION is modeled as the governed AMOS cognitive
    primitive that forms typed, provenance-bearing, uncertainty-bearing
    observation state from available reality/environment contact while
    preserving distinctions among reality, signal, observation,
    interpretation, source claim, derivation, model output, simulation,
    memory, and unknown state.

  claim_class:
    MODEL

  evidence:
    - user-supplied L01 README placeholder
    - established L01 sibling contract context
    - AMOS reality/representation principles
    - AMOS provenance principles
    - AMOS RSCF principles
    - AMOS H/M/L principles
    - AMOS epistemic-regime principles
    - AMOS control-plane principles

  provenance:
    origin_architect: Trang Phan
    architecture_family: AMOS
    primitive: L01_SENSING_OBSERVATION
    artifact: README.md
    reconstruction_status: MODEL_DERIVED
    direct_L01_canon_status: GAP

  scope:
    AMOS_OS/COGNITIVE_MATRIX/L01_SENSING_OBSERVATION

  regime:
    architecture specification / sensing-observation governance

  freshness:
    revalidate_when:
      - direct L01 canon becomes available
      - L00 contract changes
      - any L01 sibling contract changes materially
      - control-plane architecture changes
      - memory architecture changes
      - provenance architecture changes
      - H/M/L semantics change
      - executable L01 runtime becomes available

  dependencies:
    - L00_REALITY_ENVIRONMENT
    - L01_PURPOSE
    - L01_DEFINITION
    - L01_VARIABLES
    - L01_EQUATIONS
    - L01_OPERATORS
    - L01_INVARIANTS
    - L01_DEPENDENCIES
    - L01_HML
    - L01_MEMORY
    - L01_AGENTS
    - L01_SKILLS
    - L01_WORKFLOWS
    - L01_PROTOCOLS
    - L01_CONTROL_PLANES
    - L01_PROVENANCE
    - L01_FAILURE_MODES
    - L01_REPAIR
    - L01_GAP_MATRIX
    - L01_RSCF
    - AMOS_RSCF
    - AMOS_PROVENANCE_TOPOLOGY

  competing:
    - direct canon may define a narrower L01 role
    - some responsibilities may belong to L00
    - some validation responsibilities may belong exclusively to control planes
    - multimodal sensing may require child primitives
    - domain-specific sensing may require specialist modules
    - exact observation semantics may differ from this reconstruction

  falsifiers:
    - direct L01 canon materially contradicts this model
    - canonical architecture assigns L01 another role
    - canonical layer boundaries invalidate the proposed interfaces
    - formal analysis exposes contradictory invariants
    - executable implementation demonstrates incompatible requirements
    - empirical evidence invalidates a declared observation assumption

  uncertainty:
    evidence: high
    model: medium
    scope: medium
    temporal: medium
    causal: medium
    execution: high
    provenance_independence: medium_high

  confidence_ceiling:
    structural AMOS MODEL only;
    not direct-canon-complete;
    not implemented;
    not runtime-validated;
    not empirical proof
```

---

# 48. Completion State

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

  gap_status:
    status: EXPLICIT

  direct_canon_validation:
    status: GAP

  executable_implementation:
    status: GAP

  runtime_validation:
    status: GAP

  empirical_validation:
    status: GAP

  overall_artifact:
    status: COMPLETE_FOR_DECLARED_MODEL_SCOPE

  conclusion_class:
    MODEL / CONDITIONAL
```

---

# 49. README Contract Summary

The integrated L01 architecture is:

```text
L00_REALITY_ENVIRONMENT
↓
AVAILABLE REALITY CONTACT
↓
L01_SENSING_OBSERVATION
│
├── SENSE
├── CAPTURE
├── TYPE
├── TIMESTAMP
├── ATTACH PROVENANCE
├── BOUND SCOPE
├── BOUND REGIME
├── ASSIGN H/M/L
├── ESTIMATE UNCERTAINTY
├── CHECK QUALITY
├── CHECK FRESHNESS
├── CHECK CONFLICT
├── VALIDATE
└── ROUTE
↓
GOVERNED OBSERVATION STATE
↓
DOWNSTREAM COGNITION
```

The governing principle is:

> **AMOS should know not only what information it has, but what kind of information it is, how it entered the system, what it actually supports, where it applies, how uncertain it remains, and whether it is authorized for downstream use.**

The primitive therefore preserves:

```text
REALITY CONTACT
+
OBSERVATION IDENTITY
+
EPISTEMIC TYPE
+
SOURCE IDENTITY
+
OBSERVER IDENTITY
+
MODALITY
+
TIME
+
SCOPE
+
REGIME
+
H/M/L
+
PROVENANCE
+
UNCERTAINTY
+
CONFLICT
+
VALIDATION
+
AUTHORITY BOUNDARY
+
REPAIRABILITY
```

without claiming:

```text
PERFECT PERCEPTION
PERFECT MEASUREMENT
PERFECT GROUNDING
UNIVERSAL TRUTH
CANON COMPLETION
RUNTIME IMPLEMENTATION
EMPIRICAL VALIDATION
```

---

# 50. Final Contract

```text
L01_SENSING_OBSERVATION
=
REALITY-CONTACT INTERFACE
+
SENSING
+
OBSERVATION FORMATION
+
EPISTEMIC TYPING
+
PROVENANCE PRESERVATION
+
TEMPORAL BINDING
+
SCOPE/REGIME BINDING
+
H/M/L BINDING
+
UNCERTAINTY PRESERVATION
+
CONFLICT VISIBILITY
+
CONTROL-PLANE GOVERNANCE
+
MEMORY-ADMISSION SEPARATION
+
SELECTIVE INVALIDATION
+
REOBSERVATION
+
REPAIRABILITY
+
SOURCE-CANON BOUNDING
```

subject at all times to:

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

and:

```text
MODEL_COMPLETE
!=
CANON_COMPLETE

CANON_COMPLETE
!=
IMPLEMENTED

IMPLEMENTED
!=
VALIDATED

VALIDATED
!=
UNIVERSALLY TRUE
```

---

**Related:** [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L01_SENSING_OBSERVATION/L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README|L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L01_SENSING_OBSERVATION/L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README|L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L01_SENSING_OBSERVATION/L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README|L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L01_SENSING_OBSERVATION/L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README|L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L01_SENSING_OBSERVATION/L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README|L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L01_SENSING_OBSERVATION/L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README|L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L01_SENSING_OBSERVATION/L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README|L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L01_SENSING_OBSERVATION/L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README|L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L01_SENSING_OBSERVATION/L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README|L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L01_SENSING_OBSERVATION/L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README|L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L01_SENSING_OBSERVATION/L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README|L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L01_SENSING_OBSERVATION/L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README|L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L01_SENSING_OBSERVATION/L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README|L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L01_SENSING_OBSERVATION/L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README|L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L01_SENSING_OBSERVATION/L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README|L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L01_SENSING_OBSERVATION/L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README|L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L01_SENSING_OBSERVATION/L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README|L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L01_SENSING_OBSERVATION/L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README|L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L01_SENSING_OBSERVATION/L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README|L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L00_REALITY_ENVIRONMENT/L00_REALITY_ENVIRONMENT_PRIMITIVES_COGNITIVE_MATRIX_README|L00_REALITY_ENVIRONMENT_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[00_ROOT/00_HOME|00_HOME]] · 06-Knowledge-Base-MOC

```
```

---

[[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]|[[00_ROOT/AMOS MOC|AMOS MOC]]

---
**Related:** [[25_COGNITIVE_MATRIX/00_INDEX/COGNITIVE_MATRIX_MOC|COGNITIVE_MATRIX_MOC]] · [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: l01_sensing_observation_primitives_cognitive_matrix_readme
node_type: note
path: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L01_SENSING_OBSERVATION/L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
  - INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L01_SENSING_OBSERVATION/L01_SENSING_OBSERVATION_MOC|L01_SENSING_OBSERVATION_MOC]]

