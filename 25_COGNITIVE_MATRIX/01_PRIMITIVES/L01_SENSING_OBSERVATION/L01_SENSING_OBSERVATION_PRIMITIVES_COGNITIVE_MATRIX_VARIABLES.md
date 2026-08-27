---
tags:
  - amos
  - cognitive-matrix
  - l01
  - sensing-observation
  - variables
  - typed-state
  - rscf
  - provenance
  - hml
  - control-plane
---

# L01_SENSING_OBSERVATION — Variables

**Class:** `COGNITIVE_PRIMITIVE_VARIABLE_CONTRACT`  
**Origin architect / steward:** Trang Phan  
**Architecture:** `AMOS_OS / COGNITIVE_MATRIX`  
**Primitive:** `L01_SENSING_OBSERVATION`  
**Artifact:** `VARIABLES.md`  
**Role:** `TYPED VARIABLE / STATE / INTERFACE CONTRACT`  
**Status:** `AMOS_MODEL / SOURCE-CANON BOUNDED / UNVALIDATED`

> **Epistemic boundary:** this artifact defines a proposed typed variable contract for `L01_SENSING_OBSERVATION`. Variable definition does not establish runtime implementation, sensor availability, empirical validity, canonical adoption, or deployment authority.

---

# 0. Executive Definition

`L01_SENSING_OBSERVATION/VARIABLES.md` defines the typed variables through which AMOS represents an observation before that observation may participate in interpretation, memory, inference, prediction, decision, or action.

The primitive must preserve a distinction between:

```text
REALITY / ENVIRONMENT
↓
SOURCE / SENSOR / INPUT CHANNEL
↓
RAW SIGNAL
↓
OBSERVATION EVENT
↓
OBSERVATION RECORD
↓
QUALITY / UNCERTAINTY
↓
PROVENANCE
↓
TYPED STATE
↓
DOWNSTREAM INTERPRETATION
```

The central boundary is:

[
\boxed{
Reality
\neq
Signal
\neq
Observation
\neq
Interpretation
\neq
Claim
}
]

An observation is therefore not identical to the underlying reality it attempts to represent.

---

# 1. Purpose

The variable contract exists to ensure that every material L01 state is:

```text
typed
identifiable
source-bound
observer-aware
modality-aware
time-bound
scope-bound
regime-bound
H/M/L-bound
provenance-bound
uncertainty-bearing
freshness-aware
state-aware
dependency-addressable
invalidation-addressable
```

Without these distinctions, downstream cognition could silently transform:

```text
signal → fact
memory → current observation
model output → measurement
simulation → reality
derived claim → source evidence
stale evidence → current state
```

The variable layer exists to prevent those collapses.

---

# 2. Source / Canon References

## 2.1 Origin

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

## 2.2 Corpus / Architecture References

Relevant lineage available to this reconstruction includes:

```text
AMOS_CORE_ALL_VERSIONS_EXHAUSTIVE_MASTER_UPDATED
AMOS_CORE_ALL_VERSIONS_EXHAUSTIVE_MASTER
AMOS_CORE_ALL_VERSIONS_FRACTAL_KNOWLEDGE_NETWORK
AMOS_CORE v4.4 lineage

AMOS_FULL_BRAIN_OS
AMOS_COGNITION
AMOS Reality Architecture
amos_unified_master_combined_max_detail
trang_amos_reality_architecture_master_max_detail
amos_universal_field_architecture_v2_complete
KHUNG_TRANG_FULL_MAX_DETAIL_ARCHITECTURE_EQUATIONS

AMOS RSCF
AMOS provenance topology
AMOS epistemic regimes
AMOS H/M/L
AMOS control-plane architecture
L00_REALITY_ENVIRONMENT
L01_SENSING_OBSERVATION sibling contracts
```

## 2.3 Reference Status

```yaml
reference_status:

  typed_state:
    status: CORPUS_ALIGNED

  provenance_binding:
    status: CORPUS_ALIGNED

  HML_coordinates:
    status: CORPUS_ALIGNED

  scope_regime_binding:
    status: CORPUS_ALIGNED

  confidence_ceiling:
    status: CORPUS_ALIGNED

  selective_invalidation:
    status: CORPUS_ALIGNED

  reality_model_distinction:
    status: CORPUS_ALIGNED

  exact_L01_variable_registry:
    status: UNKNOWN/GAP

  exact_canonical_field_names:
    status: UNKNOWN/GAP

  exact_canonical_types:
    status: UNKNOWN/GAP

  executable_schema:
    status: UNKNOWN/GAP
```

Therefore:

```text
CORPUS-ALIGNED PRINCIPLE
!=
EXACT L01 CANON

MODEL VARIABLE
!=
CANONICAL VARIABLE

VARIABLE DEFINED
!=
VARIABLE IMPLEMENTED
```

---

# 3. Definition and Scope

An `L01Variable` is a typed state element used to represent some aspect of sensing or observation.

Candidate general form:

[
\boxed{
V_{L01}
=======

[
id,
type,
value,
unit,
source,
observer,
modality,
time,
scope,
regime,
HML,
provenance,
uncertainty,
status
]
}
]

The variable contract governs:

```text
identity
type
value
units
source
observer
modality
event time
observation time
ingestion time
processing time
scope
regime
H/M/L position
quality
uncertainty
freshness
provenance
state
dependencies
validity
```

It does not itself establish:

```text
semantic truth
causal interpretation
prediction
decision
action
authority
```

---

# 4. Variable Namespace

Recommended namespace:

```text
L01.<family>.<variable>
```

Examples:

```text
L01.identity.observation_id
L01.source.source_id
L01.signal.raw_value
L01.time.observed_at
L01.context.scope
L01.context.regime
L01.hml.level
L01.quality.confidence
L01.provenance.origin
L01.state.status
```

This namespace is a model convention unless directly confirmed by canonical source material.

---

# 5. Core Variable Families

```yaml
variable_families:

  identity:
    purpose: distinguish observation objects

  source:
    purpose: identify origin or acquisition channel

  observer:
    purpose: preserve observer context where applicable

  modality:
    purpose: identify representation/acquisition modality

  signal:
    purpose: preserve raw or minimally transformed input

  observation:
    purpose: represent normalized observation content

  temporal:
    purpose: preserve event and processing chronology

  spatial:
    purpose: preserve location/context where applicable

  scope:
    purpose: bound applicability

  regime:
    purpose: preserve operating conditions

  HML:
    purpose: preserve scale coordinate

  quality:
    purpose: characterize observation quality

  uncertainty:
    purpose: represent epistemic/measurement uncertainty

  provenance:
    purpose: preserve evidence ancestry

  dependency:
    purpose: preserve transformation ancestry

  state:
    purpose: represent lifecycle status

  governance:
    purpose: preserve admission/quarantine/authority state
```

---

# 6. Identity Variables

```yaml
identity:

  observation_id:
    type: ObservationId
    required: true
    mutable: false
    meaning: unique identity of observation record

  observation_version:
    type: VersionId
    required: true
    meaning: version of observation representation

  parent_observation_id:
    type: ObservationId | null
    meaning: immediate parent when observation is transformed

  root_observation_id:
    type: ObservationId
    meaning: earliest recoverable observation ancestor

  correlation_id:
    type: CorrelationId | null
    meaning: groups related observations without asserting causal identity
```

Invariant:

[
\boxed{
observation_id \neq source_id
}
]

and:

[
\boxed{
NewRepresentation
\not\Rightarrow
NewRealityEvent
}
]

---

# 7. Source Variables

```yaml
source:

  source_id:
    type: SourceId | UNKNOWN
    required: true

  source_type:
    type:
      - SENSOR
      - USER_INPUT
      - FILE
      - API
      - DATABASE
      - MEMORY
      - MODEL
      - SIMULATION
      - DERIVED
      - OTHER
      - UNKNOWN

  source_version:
    type: VersionRef | UNKNOWN

  source_location:
    type: SourceLocation | UNKNOWN

  source_owner:
    type: PrincipalRef | UNKNOWN

  source_trust_state:
    type:
      - UNASSESSED
      - PROVISIONAL
      - TRUSTED_FOR_SCOPE
      - QUARANTINED
      - REVOKED
      - UNKNOWN

  source_fingerprint:
    type: Hash | Fingerprint | UNKNOWN
```

Hard rule:

```text
SOURCE_TYPE = MODEL
```

must not silently become:

```text
SOURCE_TYPE = SENSOR
```

---

# 8. Observer Variables

```yaml
observer:

  observer_id:
    type: ObserverId | UNKNOWN

  observer_type:
    type:
      - HUMAN
      - SENSOR
      - SOFTWARE
      - AGENT
      - INSTITUTION
      - COMPOSITE
      - UNKNOWN

  observer_position:
    type: ObserverContext | UNKNOWN

  observer_capabilities:
    type: CapabilityRef[]

  observer_limitations:
    type: LimitationRef[]

  observer_bias_state:
    type: BiasAssessment | UNKNOWN
```

Observer variables must not imply that an observer's representation equals observer-independent reality.

[
\boxed{
Observation(o,x)
\neq
x
}
]

---

# 9. Modality Variables

```yaml
modality:

  modality:
    type:
      - TEXT
      - IMAGE
      - VIDEO
      - AUDIO
      - NUMERIC
      - TEMPORAL
      - SPATIAL
      - SENSOR
      - BIOSIGNAL
      - MULTIMODAL
      - SYMBOLIC
      - STRUCTURED_DATA
      - OTHER
      - UNKNOWN

  encoding:
    type: EncodingRef | UNKNOWN

  format:
    type: FormatRef | UNKNOWN

  dimensionality:
    type: DimensionSpec | UNKNOWN

  resolution:
    type: ResolutionSpec | UNKNOWN
```

Modality conversion must preserve lineage.

---

# 10. Raw Signal Variables

```yaml
signal:

  raw_value:
    type: AnyTypedValue

  raw_unit:
    type: Unit | DIMENSIONLESS | UNKNOWN

  raw_encoding:
    type: EncodingRef | UNKNOWN

  raw_resolution:
    type: ResolutionSpec | UNKNOWN

  raw_sampling_rate:
    type: Frequency | UNKNOWN

  raw_range:
    type: Range | UNKNOWN

  raw_precision:
    type: Precision | UNKNOWN

  raw_noise_estimate:
    type: NoiseEstimate | UNKNOWN
```

Raw does not mean correct.

```text
RAW
!=
TRUE

RAW
!=
UNBIASED

RAW
!=
UNPROCESSED BY HARDWARE
```

---

# 11. Observation Variables

```yaml
observation:

  observed_value:
    type: TypedValue

  observed_type:
    type: TypeRef

  observed_unit:
    type: Unit | DIMENSIONLESS | UNKNOWN

  observed_entity:
    type: EntityRef | UNKNOWN

  observed_property:
    type: PropertyRef | UNKNOWN

  observed_relation:
    type: RelationRef | UNKNOWN

  observation_class:
    type:
      - DIRECT
      - TRANSFORMED
      - AGGREGATED
      - RECONSTRUCTED
      - REPORTED
      - RETRIEVED
      - SYNTHETIC
      - UNKNOWN
```

Important:

```text
DIRECT
```

does not automatically mean empirically correct.

---

# 12. Temporal Variables

At minimum distinguish:

```yaml
temporal:

  event_time:
    type: Timestamp | TimeInterval | UNKNOWN
    meaning: when represented event occurred

  observed_at:
    type: Timestamp | UNKNOWN
    meaning: when observation was acquired

  ingested_at:
    type: Timestamp | UNKNOWN
    meaning: when AMOS received the observation

  processed_at:
    type: Timestamp | UNKNOWN
    meaning: when transformation occurred

  recorded_at:
    type: Timestamp | UNKNOWN
    meaning: when durable record was created

  valid_from:
    type: Timestamp | UNKNOWN

  valid_until:
    type: Timestamp | UNKNOWN

  freshness_horizon:
    type: Duration | PolicyRef | UNKNOWN
```

Invariant:

[
\boxed{
t_{event},
t_{observe},
t_{ingest},
t_{process},
t_{decision}
}
]

must remain distinguishable whenever materially relevant.

---

# 13. Spatial Variables

Where spatial context exists:

```yaml
spatial:

  location:
    type: SpatialCoordinate | NamedLocation | UNKNOWN

  reference_frame:
    type: ReferenceFrame | UNKNOWN

  spatial_resolution:
    type: Resolution | UNKNOWN

  spatial_scope:
    type: SpatialEnvelope | UNKNOWN
```

A coordinate without its reference frame may be invalid or ambiguous.

---

# 14. Scope Variables

```yaml
scope:

  system_scope:
    type: SystemRef | UNKNOWN

  population_scope:
    type: PopulationRef | UNKNOWN

  environment_scope:
    type: EnvironmentRef | UNKNOWN

  domain_scope:
    type: DomainRef | UNKNOWN

  measurement_scope:
    type: MeasurementMethodRef | UNKNOWN

  applicability:
    type: ApplicabilityEnvelope
```

Scope cannot silently widen downstream.

[
\boxed{
Scope(Derived)
\subseteq
Scope(LoadBearingInputs)
}
]

unless independently justified.

---

# 15. Regime Variables

```yaml
regime:

  regime_id:
    type: RegimeId | UNKNOWN

  regime_class:
    type: RegimeClass | UNKNOWN

  regime_start:
    type: Timestamp | UNKNOWN

  regime_end:
    type: Timestamp | UNKNOWN

  regime_confidence:
    type: Confidence | UNKNOWN

  regime_assumptions:
    type: AssumptionRef[]
```

A result valid in one regime cannot silently migrate into another.

---

# 16. H/M/L Variables

```yaml
HML:

  level:
    type:
      - H
      - M
      - L

  parent_level_ref:
    type: StateRef | null

  child_level_refs:
    type: StateRef[]

  translation_operator:
    type: OperatorRef | null

  translation_loss:
    type: LossEstimate | UNKNOWN
```

Interpretation:

```text
L = local observation/detail
M = subsystem/aggregation
H = governing/system-level state
```

Hard boundary:

[
\boxed{
Observation_L
\not\Rightarrow
State_H
}
]

without a valid translation/dependency path.

---

# 17. Quality Variables

```yaml
quality:

  completeness:
    type: Score | UNKNOWN

  validity:
    type: Score | UNKNOWN

  reliability:
    type: Score | UNKNOWN

  precision:
    type: Score | UNKNOWN

  accuracy:
    type: Score | UNKNOWN

  consistency:
    type: Score | UNKNOWN

  calibration:
    type: CalibrationState | UNKNOWN

  signal_to_noise:
    type: Ratio | UNKNOWN
```

These are distinct constructs and must not be merged into one generic confidence number without an explicit mapping.

---

# 18. Uncertainty Variables

```yaml
uncertainty:

  evidence_uncertainty:
    type: Confidence | UNKNOWN

  measurement_uncertainty:
    type: Confidence | Interval | Distribution | UNKNOWN

  model_uncertainty:
    type: Confidence | UNKNOWN

  scope_uncertainty:
    type: Confidence | UNKNOWN

  temporal_uncertainty:
    type: Confidence | UNKNOWN

  causal_uncertainty:
    type: Confidence | UNKNOWN

  provenance_uncertainty:
    type: Confidence | UNKNOWN

  independence_uncertainty:
    type: Confidence | UNKNOWN
```

Recommended vector:

[
\boxed{
U =
[
U_e,
U_m,
U_s,
U_t,
U_c,
U_p,
U_i
]
}
]

Do not collapse this vector prematurely into one scalar.

---

# 19. Confidence Variables

```yaml
confidence:

  observation_confidence:
    type: Float[0,1] | OrdinalConfidence | UNKNOWN

  confidence_method:
    type: MethodRef | UNKNOWN

  confidence_ceiling:
    type: Float[0,1] | OrdinalConfidence

  confidence_dependencies:
    type: VariableRef[]
```

Governing rule:

[
\boxed{
C_{derived}
\le
\min_{i \in LB}
C_i
}
]

for load-bearing premises unless independent revalidation licenses a higher ceiling.

---

# 20. Freshness Variables

```yaml
freshness:

  freshness_state:
    type:
      - CURRENT
      - AGING
      - STALE
      - EXPIRED
      - UNKNOWN

  freshness_reference_time:
    type: Timestamp

  freshness_policy:
    type: PolicyRef | UNKNOWN

  age:
    type: Duration | UNKNOWN

  revalidation_due:
    type: Timestamp | Trigger | UNKNOWN
```

Freshness is purpose- and regime-dependent.

```text
OLD
!=
STALE

RECENT
!=
VALID
```

---

# 21. Provenance Variables

```yaml
provenance:

  provenance_id:
    type: ProvenanceId

  origin_id:
    type: SourceId | UNKNOWN

  origin_class:
    type:
      - SOURCE_CLAIM
      - OBSERVATION
      - DERIVED
      - MODEL
      - DECISION
      - UNKNOWN

  parent_provenance:
    type: ProvenanceId[]

  root_sources:
    type: SourceId[]

  transformation_history:
    type: TransformationRecord[]

  source_hash:
    type: Hash | UNKNOWN

  evidence_refs:
    type: EvidenceRef[]

  independence_group:
    type: IndependenceGroupId | UNKNOWN
```

Multiple descendants of one origin remain provenance-correlated.

[
\boxed{
n;descendants(source_x)
\neq
n;independent;sources
}
]

---

# 22. Dependency Variables

```yaml
dependency:

  dependency_ids:
    type: DependencyRef[]

  load_bearing_dependencies:
    type: DependencyRef[]

  optional_dependencies:
    type: DependencyRef[]

  downstream_dependents:
    type: ClaimRef[] | StateRef[]

  invalidation_edges:
    type: DependencyEdge[]
```

Dependencies support selective invalidation.

A failed premise should invalidate dependent conclusions rather than unrelated state.

---

# 23. Lifecycle State Variables

```yaml
state:

  lifecycle_state:
    type:
      - CREATED
      - INGESTED
      - NORMALIZED
      - VALIDATED
      - ACTIVE
      - QUARANTINED
      - SUPERSEDED
      - INVALIDATED
      - REVOKED
      - ARCHIVED
      - UNKNOWN

  previous_state:
    type: LifecycleState | null

  state_changed_at:
    type: Timestamp

  state_reason:
    type: ReasonRef | UNKNOWN

  state_authority:
    type: PrincipalRef | UNKNOWN
```

Candidate transition:

```text
CREATED
↓
INGESTED
↓
NORMALIZED
↓
VALIDATED
↓
ACTIVE
```

Exceptional transitions:

```text
ANY
→ QUARANTINED

ACTIVE
→ SUPERSEDED

ANY
→ INVALIDATED

ANY
→ REVOKED
```

---

# 24. Governance Variables

```yaml
governance:

  admission_state:
    type:
      - REJECT
      - QUARANTINE
      - CONDITIONAL
      - SANDBOX
      - ADMIT
      - UNKNOWN

  authority_context:
    type: AuthorityContext | UNKNOWN

  commit_eligibility:
    type: Boolean | UNKNOWN

  commit_status:
    type:
      - NONE
      - PROPOSED
      - AUTHORIZED
      - COMMITTED
      - REJECTED
      - ROLLED_BACK
      - UNKNOWN

  validation_epoch:
    type: EpochId | UNKNOWN

  state_version:
    type: VersionId | UNKNOWN
```

Hard boundary:

[
\boxed{
commit_eligibility
\neq
commit_authority
}
]

---

# 25. Canonical Candidate Observation Tensor

A compact candidate state representation is:

[
\boxed{
O =
T[
I,
S,
B,
M,
X,
T,
Sp,
Sc,
R,
H,
Q,
U,
P,
D,
G
]
}
]

where:

```text
I  = identity
S  = source
B  = observer
M  = modality
X  = observed value
T  = temporal coordinates
Sp = spatial coordinates
Sc = scope
R  = regime
H  = H/M/L
Q  = quality
U  = uncertainty
P  = provenance
D  = dependencies
G  = governance/lifecycle state
```

This tensor is an `AMOS_MODEL` representation, not an asserted canonical equation unless independently source-confirmed.

---

# 26. Typed Input Contract

```yaml
L01Input:

  payload:
    type: RawPayload

  source:
    type: SourceDescriptor

  modality:
    type: Modality

  observer:
    type: ObserverDescriptor | UNKNOWN

  event_time:
    type: Timestamp | UNKNOWN

  observed_at:
    type: Timestamp | UNKNOWN

  location:
    type: SpatialDescriptor | UNKNOWN

  scope:
    type: ScopeEnvelope | UNKNOWN

  regime:
    type: RegimeRef | UNKNOWN

  HML:
    type: H | M | L

  provenance:
    type: ProvenanceBundle | UNKNOWN

  authority_context:
    type: AuthorityContext | UNKNOWN
```

---

# 27. Typed Output Contract

```yaml
L01Output:

  observation:
    type: ObservationRecord

  quality:
    type: QualityVector

  uncertainty:
    type: UncertaintyVector

  provenance:
    type: ProvenanceBundle

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeRef | UNKNOWN

  HML:
    type: HMLCoordinate

  lifecycle_state:
    type: LifecycleState

  admission_state:
    type: AdmissionState

  confidence_ceiling:
    type: Confidence

  gaps:
    type: GapRecord[]
```

---

# 28. Operators

Variables may be acted upon only through typed operators.

Candidate registry:

```text
CREATE
TYPE
NORMALIZE
VALIDATE
CALIBRATE
ANNOTATE
TIMESTAMP
LOCALIZE
BIND_SOURCE
BIND_OBSERVER
BIND_PROVENANCE
BIND_SCOPE
BIND_REGIME
BIND_HML
ESTIMATE_QUALITY
ESTIMATE_UNCERTAINTY
COMPUTE_FRESHNESS
AGGREGATE
TRANSFORM
TRANSLATE_SCALE
COMPARE
CONFLICT
QUARANTINE
SUPERSEDE
INVALIDATE
REVOKE
REPAIR
REVALIDATE
ARCHIVE
```

Operators must not silently destroy variable dimensions required by downstream integrity.

---

# 29. Variable Invariants

```text
L01-VAR-INV-001
Every observation has a stable observation identity.

L01-VAR-INV-002
Observation identity is distinct from source identity.

L01-VAR-INV-003
Value and unit remain compatible.

L01-VAR-INV-004
Unknown unit remains UNKNOWN rather than being inferred without evidence.

L01-VAR-INV-005
Observation time remains distinct from processing time where material.

L01-VAR-INV-006
Source type cannot silently change.

L01-VAR-INV-007
Model output cannot silently become sensor evidence.

L01-VAR-INV-008
Simulation output cannot silently become observed reality.

L01-VAR-INV-009
Memory retrieval cannot silently become current observation.

L01-VAR-INV-010
Scope cannot silently widen.

L01-VAR-INV-011
Regime cannot silently widen.

L01-VAR-INV-012
H/M/L cannot silently change.

L01-VAR-INV-013
Cross-scale translation preserves provenance.

L01-VAR-INV-014
Cross-scale translation preserves uncertainty.

L01-VAR-INV-015
Transformation preserves ancestry.

L01-VAR-INV-016
Confidence cannot exceed load-bearing evidence without independent revalidation.

L01-VAR-INV-017
Unknown cannot silently become known.

L01-VAR-INV-018
Quarantined state cannot silently become active.

L01-VAR-INV-019
Invalidated state cannot silently become valid.

L01-VAR-INV-020
Capability variables cannot grant authority.

L01-VAR-INV-021
Proposal state cannot equal committed state.

L01-VAR-INV-022
Supersession preserves historical identity.

L01-VAR-INV-023
Correlated provenance cannot masquerade as independent evidence.

L01-VAR-INV-024
Observation variables cannot themselves establish causal effect.

L01-VAR-INV-025
Missing required variables produce GAP/UNKNOWN rather than fabricated defaults.
```

---

# 30. Dependencies

Primary architectural dependencies:

```text
L00_REALITY_ENVIRONMENT

L01_PURPOSE
L01_DEFINITION
L01_EQUATIONS
L01_STATE
L01_OPERATORS
L01_INVARIANTS
L01_DEPENDENCIES
L01_HML
L01_MEMORY
L01_AGENTS
L01_SKILLS
L01_WORKFLOWS
L01_PROTOCOLS
L01_CONTROL_PLANES
L01_PROVENANCE
L01_RSCF
L01_FAILURE_MODES
L01_REPAIR
L01_TESTS
```

Variable interpretation must not outrun those contracts.

---

# 31. H/M/L Applicability

## L — Local

Variables describe:

```text
single observation
single signal
single timestamp
single source
single transformation
single quality estimate
```

## M — Subsystem

Variables describe:

```text
observation groups
sensor streams
multimodal bundles
aggregates
local world models
subsystem state
```

## H — Governing

Variables describe:

```text
environment state
system-wide observation quality
global provenance condition
system observation coverage
governance state
```

Rule:

[
\boxed{
V_L \rightarrow V_M \rightarrow V_H
}
]

requires explicit transformation operators.

Scale promotion is not automatic.

---

# 32. Control-Plane Requirements

The infrastructure/control plane should own or enforce, where applicable:

```text
schema validation
state-version validation
authority validation
scope validation
regime validation
provenance validation
freshness validation
commit eligibility
quarantine enforcement
revocation enforcement
concurrent-update protection
selective invalidation
audit persistence
```

The cognitive worker may propose:

```text
value
classification
uncertainty
interpretation
repair
```

but proposal does not equal durable state mutation.

---

# 33. Agents

Candidate architectural roles:

```text
Sensing Agent
Observation Normalization Agent
Modality Adapter Agent
Quality Assessment Agent
Provenance Agent
Freshness Agent
Conflict Detection Agent
Observation Audit Agent
Repair Agent
```

These are logical roles only.

```text
DEFINED AGENT
!=
DEPLOYED AGENT
```

---

# 34. Skills

Candidate supporting skill families:

```text
multimodal perception
typed variable normalization
measurement integrity
provenance auditing
temporal reasoning
spatial normalization
H/M/L translation
uncertainty estimation
memory boundary control
conflict detection
state validation
repair/recovery
```

Skill availability does not establish runtime execution.

---

# 35. Workflow

```text
RECEIVE INPUT
↓
IDENTIFY SOURCE
↓
IDENTIFY MODALITY
↓
ASSIGN OBSERVATION ID
↓
PRESERVE RAW SIGNAL
↓
TYPE VALUE
↓
VALIDATE UNIT
↓
BIND TIME
↓
BIND SPACE
↓
BIND OBSERVER
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
ASSESS FRESHNESS
↓
VALIDATE INVARIANTS
↓
ADMIT / QUARANTINE / REJECT
↓
EMIT OBSERVATION RECORD
```

---

# 36. Protocols

Candidate protocol objects:

```text
ObservationInput
ObservationRecord
SourceDescriptor
ObserverDescriptor
ModalityDescriptor
TemporalEnvelope
SpatialEnvelope
ScopeEnvelope
RegimeEnvelope
HMLCoordinate
QualityVector
UncertaintyVector
ProvenanceBundle
DependencyBundle
AdmissionDecision
ObservationStateTransition
ObservationInvalidationEvent
ObservationRepairProposal
```

---

# 37. Evidence / Provenance

Each material variable should carry sufficient provenance to answer:

```text
Where did this value come from?
Who or what observed it?
When was it observed?
What transformations occurred?
What source version was used?
What assumptions were introduced?
What scope applies?
What regime applies?
What H/M/L level applies?
What uncertainty remains?
What claims depend on it?
```

Candidate provenance binding:

[
\boxed{
P(V)
====

[
origin,
ancestry,
transformations,
time,
scope,
regime,
HML,
evidence
]
}
]

---

# 38. Uncertainty and Confidence Ceiling

A variable may be syntactically valid while epistemically weak.

Therefore:

```text
TYPE_VALID
!=
EVIDENCE_VALID

SCHEMA_VALID
!=
REALITY_VALID
```

Candidate confidence ceiling:

[
\boxed{
C(V)
\le
\min(
C_{source},
C_{measurement},
C_{provenance},
C_{scope},
C_{regime},
C_{freshness}
)
}
]

where these are load-bearing.

---

# 39. Failure Modes

```text
FM-L01-VAR-001   Missing-Identity
FM-L01-VAR-002   Identity-Collision
FM-L01-VAR-003   Type-Mismatch
FM-L01-VAR-004   Unit-Mismatch
FM-L01-VAR-005   Source-Loss
FM-L01-VAR-006   Source-Type-Collapse
FM-L01-VAR-007   Observer-Loss
FM-L01-VAR-008   Modality-Loss
FM-L01-VAR-009   Timestamp-Collapse
FM-L01-VAR-010   Spatial-Frame-Loss
FM-L01-VAR-011   Scope-Leakage
FM-L01-VAR-012   Regime-Leakage
FM-L01-VAR-013   HML-Collapse
FM-L01-VAR-014   Provenance-Loss
FM-L01-VAR-015   Provenance-Alias-Sybil
FM-L01-VAR-016   Uncertainty-Stripping
FM-L01-VAR-017   Confidence-Inflation
FM-L01-VAR-018   Freshness-Reset
FM-L01-VAR-019   Memory-as-Observation
FM-L01-VAR-020   Model-as-Sensor
FM-L01-VAR-021   Simulation-as-Reality
FM-L01-VAR-022   Quarantine-Bypass
FM-L01-VAR-023   Invalid-State-Reactivation
FM-L01-VAR-024   Proposal-Commit-Collapse
FM-L01-VAR-025   Capability-Authority-Collapse
FM-L01-VAR-026   Unknown-Default-Fabrication
FM-L01-VAR-027   Dependency-Loss
FM-L01-VAR-028   Over-Invalidation
FM-L01-VAR-029   Under-Invalidation
FM-L01-VAR-030   Cross-Scale-Semantic-Loss
```

---

# 40. Repair / Recovery

When variable integrity fails:

```text
DETECT INVALID VARIABLE
↓
FREEZE / QUARANTINE AFFECTED STATE
↓
IDENTIFY EARLIEST CORRUPTED VARIABLE
↓
TRACE PROVENANCE
↓
TRACE DEPENDENTS
↓
CLASSIFY FAILURE
↓
RESTORE FROM VALID PREDECESSOR IF AVAILABLE
↓
REAPPLY VALID TRANSFORMATIONS
↓
REVALIDATE TYPE / UNIT / SCOPE / REGIME / HML
↓
REVALIDATE PROVENANCE
↓
RECOMPUTE UNCERTAINTY / CONFIDENCE
↓
INVALIDATE ONLY AFFECTED DESCENDANTS
↓
RUN REGRESSION TESTS
↓
RESTORE / RETAIN QUARANTINE
```

Repair must preserve failure history.

---

# 41. Tests / Validators

Minimum candidate validator registry:

```text
VALIDATOR_VARIABLE_SCHEMA
VALIDATOR_IDENTITY
VALIDATOR_TYPE
VALIDATOR_UNIT
VALIDATOR_SOURCE
VALIDATOR_OBSERVER
VALIDATOR_MODALITY
VALIDATOR_TEMPORAL
VALIDATOR_SPATIAL
VALIDATOR_SCOPE
VALIDATOR_REGIME
VALIDATOR_HML
VALIDATOR_QUALITY
VALIDATOR_UNCERTAINTY
VALIDATOR_CONFIDENCE
VALIDATOR_FRESHNESS
VALIDATOR_PROVENANCE
VALIDATOR_DEPENDENCY
VALIDATOR_LIFECYCLE_STATE
VALIDATOR_ADMISSION_STATE
VALIDATOR_AUTHORITY
VALIDATOR_COMMIT_STATE
```

Minimum tests:

```text
TEST_L01_VAR_001
Missing observation_id fails validation.

TEST_L01_VAR_002
Unknown source remains UNKNOWN.

TEST_L01_VAR_003
Incompatible value/unit pair fails validation.

TEST_L01_VAR_004
Model-origin value remains typed MODEL.

TEST_L01_VAR_005
Simulation-origin value remains typed SIMULATION.

TEST_L01_VAR_006
Memory retrieval preserves original observation time.

TEST_L01_VAR_007
Transformation preserves provenance ancestry.

TEST_L01_VAR_008
H/M/L translation preserves source lineage.

TEST_L01_VAR_009
Scope widening without evidence fails.

TEST_L01_VAR_010
Regime widening without evidence fails.

TEST_L01_VAR_011
Stale observation cannot silently become CURRENT.

TEST_L01_VAR_012
Quarantined variable cannot silently become ACTIVE.

TEST_L01_VAR_013
Revoked provenance triggers dependent review.

TEST_L01_VAR_014
Correlated source aliases remain one independence group.

TEST_L01_VAR_015
Missing uncertainty does not default to certainty.

TEST_L01_VAR_016
Missing evidence does not produce PASS.

TEST_L01_VAR_017
Capability flag does not grant authority.

TEST_L01_VAR_018
PROPOSED state does not equal COMMITTED.

TEST_L01_VAR_019
Invalidation preserves historical provenance.

TEST_L01_VAR_020
Repair requires revalidation.
```

---

# 42. Falsifiers

This contract must be revised if:

```text
direct canonical L01 VARIABLES material contradicts this registry

canonical AMOS variable names/types differ materially

canonical L01 state semantics make variables incompatible

canonical H/M/L semantics invalidate the scale model

canonical provenance semantics invalidate ancestry fields

canonical control-plane semantics assign different ownership

runtime implementation proves proposed fields structurally impossible

formal validation identifies contradictory invariants

empirical implementation evidence falsifies assumed variable behavior
```

---

# 43. Gap Matrix

```yaml
gap_matrix:

  direct_L01_VARIABLES_canon:
    status: GAP
    criticality: CRITICAL

  canonical_variable_registry:
    status: GAP
    criticality: CRITICAL

  canonical_field_names:
    status: GAP
    criticality: DECISION_RELEVANT

  canonical_type_system:
    status: GAP
    criticality: CRITICAL

  canonical_units_registry:
    status: GAP
    criticality: DECISION_RELEVANT

  canonical_state_enums:
    status: GAP
    criticality: DECISION_RELEVANT

  executable_schema:
    status: GAP
    criticality: CRITICAL

  runtime_variable_store:
    status: GAP
    criticality: CRITICAL

  executed_validation:
    status: GAP
    criticality: CRITICAL

  independent_reproduction:
    status: GAP
    criticality: CRITICAL

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

  falsifiers:
    status: MODEL_COMPLETE
```

---

# 44. Gap Resolution Priority

```text
1. Locate direct canonical L01 VARIABLES material.

2. Extract exact canonical variable names.

3. Extract exact canonical types.

4. Resolve aliases against AMOS variable registry.

5. Confirm units and dimensional constraints.

6. Confirm lifecycle states.

7. Confirm provenance fields.

8. Confirm scope/regime fields.

9. Confirm H/M/L coordinate representation.

10. Confirm uncertainty/confidence semantics.

11. Confirm control-plane ownership.

12. Generate executable schema.

13. Run deterministic schema validators.

14. Bind schema to exact runtime version/hash.

15. Run state-transition tests.

16. Run provenance tests.

17. Run adversarial malformed-variable tests.

18. Run cross-scale translation tests.

19. Run repair/regression tests.

20. Promote only from observed evidence.
```

---

# 45. Evidence / Provenance of This Artifact

```yaml
artifact_provenance:

  artifact:
    L01_SENSING_OBSERVATION/VARIABLES.md

  origin_architect:
    Trang Phan

  architecture_family:
    AMOS

  supplied_basis:
    - user-supplied L01 VARIABLES placeholder
    - established L01 sibling contract structure
    - AMOS typed-state principles
    - AMOS RSCF principles
    - AMOS H/M/L principles
    - AMOS provenance principles
    - AMOS control-plane principles

  derivation:
    class: AMOS_MODEL_RECONSTRUCTION

  direct_L01_VARIABLES_canon:
    status: UNKNOWN/GAP

  executable_validation:
    status: NOT_EXECUTED

  empirical_validation:
    status: NOT_ESTABLISHED
```

---

# 46. Uncertainty Vector

```yaml
uncertainty:

  evidence:
    level: HIGH
    reason:
      exact canonical L01 variable registry has not been established

  model:
    level: MEDIUM
    reason:
      variable structure follows AMOS architectural constraints but includes reconstructed L01-specific fields

  scope:
    level: MEDIUM

  temporal:
    level: MEDIUM

  causal:
    level: LOW_MEDIUM
    reason:
      artifact deliberately avoids promoting observation variables into causal claims

  execution:
    level: HIGH
    reason:
      executable variable schema has not been established

  provenance_independence:
    level: MEDIUM_HIGH
```

---

# 47. Confidence Ceiling

Strongest warranted conclusion:

```text
STRUCTURALLY COHERENT AMOS L01 VARIABLE MODEL
```

not:

```text
EXACT CANONICAL VARIABLE REGISTRY
CANON VERIFIED
SCHEMA IMPLEMENTED
RUNTIME VERIFIED
EMPIRICALLY VALIDATED
FORMALLY VERIFIED
DEPLOYMENT READY
```

---

# 48. RSCF Completion State

```yaml
rscf:

  id:
    L01_SENSING_OBSERVATION_VARIABLES

  target:
    typed variable architecture of L01 sensing/observation

  claim:
    L01_SENSING_OBSERVATION requires typed observation variables
    that preserve identity, source, observer, modality, time,
    scope, regime, H/M/L, uncertainty, provenance, dependencies,
    lifecycle state, and governance boundaries.

  claim_class:
    MODEL

  evidence:
    - user-supplied L01 VARIABLES placeholder
    - established L01 sibling architecture
    - AMOS typed-state principles
    - AMOS RSCF principles
    - AMOS provenance principles
    - AMOS H/M/L principles
    - AMOS control-plane principles

  provenance:
    origin_architect: Trang Phan
    architecture_family: AMOS
    primitive: L01_SENSING_OBSERVATION
    artifact: VARIABLES.md
    derivation: AMOS_MODEL_RECONSTRUCTION
    direct_L01_VARIABLES_canon: UNKNOWN/GAP

  scope:
    architecture: AMOS_OS
    subsystem: COGNITIVE_MATRIX
    primitive: L01_SENSING_OBSERVATION
    artifact: VARIABLES

  regime:
    architecture specification / typed observation state

  freshness:
    revalidate_when:
      - direct L01 VARIABLES canon becomes available
      - L01 definition changes
      - L01 state model changes
      - canonical variable registry changes
      - H/M/L contract changes
      - provenance contract changes
      - runtime schema becomes available

  dependencies:
    - L00_REALITY_ENVIRONMENT
    - L01_PURPOSE
    - L01_DEFINITION
    - L01_EQUATIONS
    - L01_STATE
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
    - L01_RSCF
    - L01_FAILURE_MODES
    - L01_REPAIR
    - L01_TESTS

  competing:

    - id: COMPETING_001
      hypothesis:
        canonical L01 uses a substantially smaller primitive variable set

    - id: COMPETING_002
      hypothesis:
        some variables belong to infrastructure rather than the cognitive primitive

    - id: COMPETING_003
      hypothesis:
        modality-specific child systems own most sensor-specific variables

    - id: COMPETING_004
      hypothesis:
        canonical AMOS uses a universal variable registry rather than local L01 names

  falsifiers:
    - direct L01 canon materially contradicts this variable model
    - canonical type definitions conflict with proposed types
    - canonical state semantics invalidate lifecycle fields
    - canonical provenance semantics invalidate ancestry fields
    - executable implementation demonstrates incompatible contracts

  uncertainty:
    evidence: HIGH
    model: MEDIUM
    scope: MEDIUM
    temporal: MEDIUM
    causal: LOW_MEDIUM
    execution: HIGH
    provenance_independence: MEDIUM_HIGH

  confidence_ceiling:
    structural AMOS MODEL only;
    exact L01 variable canon unresolved;
    executable schema not established;
    empirical validation not established

  material_gaps:
    - direct L01 VARIABLES canon
    - canonical variable registry
    - canonical type system
    - canonical units
    - executable schema
    - runtime implementation
    - executed validation
```

---

# 49. Completion State

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

  direct_L01_canon_validation:
    status: GAP

  executable_implementation:
    status: GAP

  empirical_validation:
    status: GAP

  overall_artifact:
    status: COMPLETE_FOR_DECLARED_MODEL_SCOPE

  conclusion_class:
    MODEL / CONDITIONAL
```

---

# 50. Variable Contract Summary

```text
L01 OBSERVATION VARIABLE
=
IDENTITY
+
SOURCE
+
OBSERVER
+
MODALITY
+
RAW SIGNAL
+
OBSERVED VALUE
+
UNIT
+
TIME
+
SPACE
+
SCOPE
+
REGIME
+
H/M/L
+
QUALITY
+
UNCERTAINTY
+
CONFIDENCE CEILING
+
FRESHNESS
+
PROVENANCE
+
DEPENDENCIES
+
LIFECYCLE STATE
+
GOVERNANCE STATE
```

The governing principle is:

> **AMOS must preserve enough typed structure around an observation that downstream reasoning can distinguish what was observed, where it came from, when and under what conditions it applied, how it was transformed, what uncertainty remains, and what conclusions must be invalidated if it fails.**

---

# 51. Final Hard Boundaries

```text
PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

UNKNOWN/GAP != PASS
```

L01 variable architecture additionally requires:

```text
REALITY != OBSERVATION

SIGNAL != REALITY

RAW != TRUE

OBSERVATION != INTERPRETATION

OBSERVATION != CLAIM

OBSERVATION != CAUSAL EFFECT

SOURCE_CLAIM != OBSERVATION

MODEL != SENSOR

SIMULATION != REALITY

MEMORY != CURRENT OBSERVATION

RETRIEVAL_TIME != OBSERVATION_TIME

PROCESSING_TIME != EVENT_TIME

RECENT != VALID

OLD != STALE

CONFIDENCE != TRUTH

QUALITY != CONFIDENCE

TYPE_VALID != EVIDENCE_VALID

SCHEMA_VALID != REALITY_VALID

CORRELATED SOURCES != INDEPENDENT SOURCES

L_STATE != H_STATE

SCALE_TRANSLATION != SCALE_EQUIVALENCE

UNKNOWN != ZERO

UNKNOWN != FALSE

UNKNOWN != CERTAIN

QUARANTINED != ACTIVE

SUPERSEDED != ERASED

INVALIDATED != DELETED

ELIGIBLE != AUTHORIZED

AUTHORIZED != COMMITTED

VARIABLE_DEFINED != VARIABLE_IMPLEMENTED

MODEL_COMPLETE != CANON_COMPLETE

CANON_COMPLETE != IMPLEMENTED

IMPLEMENTED != VALIDATED
```

---

# 52. References

## Internal L00/L01 References

```text
L00_REALITY_ENVIRONMENT — Readme
L00_REALITY_ENVIRONMENT_PRIMITIVES_COGNITIVE_MATRIX_README
L00_REALITY_ENVIRONMENT_PRIMITIVES_COGNITIVE_MATRIX_README
L00_REALITY_ENVIRONMENT_PRIMITIVES_COGNITIVE_MATRIX_README
L00_REALITY_ENVIRONMENT_PRIMITIVES_COGNITIVE_MATRIX_README
L00_REALITY_ENVIRONMENT_PRIMITIVES_COGNITIVE_MATRIX_README

L01_SENSING_OBSERVATION — Readme
L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README
L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README
L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README
L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README
L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README
L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README
L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README
L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README
L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README
L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README
L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README
L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README
L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README
L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README
L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README
L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README
L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README
L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README
L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README
L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README
```

## Architecture References

```text
AMOS Full Brain OS Architecture
AMOS Cognition
AMOS Reality Architecture
AMOS RSCF
AMOS HML Architecture
AMOS Provenance Topology
AMOS Universal Variable Registry
AMOS Universal Coordinate System
Cosmo_Brain_BRIDGE_INDEX
AMOS Deterministic AI Control Plane
AMOS Reality Simulation Distinction
AMOS Measurement Integrity Auditor
AMOS Temporal Multi-Scale Architecture
AMOS Multimodal Perception Layer
```

## Source Lineage References

```text
AMOS_CORE_ALL_VERSIONS_EXHAUSTIVE_MASTER_UPDATED
AMOS_CORE_ALL_VERSIONS_EXHAUSTIVE_MASTER
AMOS_CORE_ALL_VERSIONS_FRACTAL_KNOWLEDGE_NETWORK
AMOS_CORE v4.4 lineage
AMOS_FULL_BRAIN_OS
AMOS_COGNITION
trang_amos_reality_architecture_master_max_detail
amos_unified_master_combined_max_detail
amos_universal_field_architecture_v2_complete
KHUNG_TRANG_FULL_MAX_DETAIL_ARCHITECTURE_EQUATIONS
```

> Reference presence establishes intended lineage and dependency only. It does not establish that the reconstructed L01 variable registry above appears verbatim in those sources. Exact source-to-variable mapping remains `UNKNOWN/GAP` until directly verified.

---

**Related:** [[L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README]] · [[L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README]]

```text
```

---

[[00_ROOT_MOC|AMOS MOC]]

---
**Related:** [[00_HOME]] · [[COGNITIVE_MATRIX_MOC]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: l01_sensing_observation_primitives_cognitive_matrix_variables
node_type: note
path: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L01_SENSING_OBSERVATION/L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_VARIABLES.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[L01_SENSING_OBSERVATION_MOC]]
