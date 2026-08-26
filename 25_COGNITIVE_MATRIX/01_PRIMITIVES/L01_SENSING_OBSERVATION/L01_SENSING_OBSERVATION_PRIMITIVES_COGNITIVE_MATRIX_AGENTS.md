---
tags: ['cognitive_matrix', 'primitives', 'l01_sensing_observation', 'note']
---

Below is the full paste-ready `L01_SENSING_OBSERVATION/AGENTS.md`. I’m keeping direct L01 agent canon explicitly gap-bounded rather than inventing it; the agent architecture is therefore classified as `MODEL / CONDITIONAL`.

---
tags:
  - amos
  - cognitive-matrix
  - l01
  - sensing-observation
  - agents
  - perception
  - observation
  - measurement
  - provenance
  - multimodal
  - control-plane
  - validation
  - rscf
  - rscf/S-state
  - rscf/T-topology
  - rscf/C-constraint
  - rscf/type-model
---

# L01_SENSING_OBSERVATION — Agents

**Class:** `COGNITIVE_PRIMITIVE_AGENT_CONTRACT`  
**Origin architect / steward:** Trang Phan  
**Architecture:** `AMOS_OS / COGNITIVE_MATRIX`  
**Primitive:** `L01_SENSING_OBSERVATION`  
**Artifact:** `AGENTS.md`  
**Role:** `OBSERVATION ACQUISITION / SENSOR MEDIATION / MEASUREMENT / EPISTEMIC TYPING / PROVENANCE PRESERVATION`  
**Status:** `STRUCTURAL AGENT CONTRACT / SOURCE-GAP BOUNDED`  
**Conclusion class:** `MODEL / CONDITIONAL`

> **Canon boundary:** direct authoritative `L01_SENSING_OBSERVATION` agent canon is not established by the supplied placeholder alone. The agent architecture below is a conservative AMOS model constrained by the supplied L01 contract, the L00 reality/environment boundary, and AMOS control-plane, provenance, RSCF, authority, uncertainty, and recovery principles. It must not be represented as recovered source canon until direct source evidence establishes that status.

---

# 0. Purpose

`L01_SENSING_OBSERVATION/AGENTS.md` defines the agent roles that acquire, normalize, validate, qualify, and transmit observations from an environment into AMOS without allowing sensing workers to silently convert measurements, interpretations, predictions, memories, or generated content into observed reality.

The agent layer governs:

```text
ENVIRONMENT
↓
SENSING CHANNEL
↓
OBSERVATION AGENT
↓
RAW OBSERVATION
↓
TYPING
↓
QUALITY / UNCERTAINTY
↓
PROVENANCE
↓
VALIDATION
↓
OBSERVATION RECORD
↓
L00 / DOWNSTREAM COGNITION
```

Its primary boundary is:

```text
SENSING
!=
INTERPRETATION

OBSERVATION
!=
INFERENCE

MEASUREMENT
!=
GROUND TRUTH

AGENT OUTPUT
!=
ENVIRONMENT STATE

CAPABILITY
!=
AUTHORITY
```

---

# 1. Definition

An L01 sensing/observation agent is a bounded cognitive or computational worker responsible for one or more operations involved in obtaining or validating environment-derived evidence.

Conceptually:

[
A_{L01}
=======

(Role,
Capability,
Input,
Output,
Scope,
Channel,
Authority,
Evidence,
Provenance,
Uncertainty,
Constraints)
]

An agent is therefore not defined merely by a name or prompt.

It requires an explicit contract describing:

* what it may observe;
* how it observes;
* which channels it may access;
* which transformations it may perform;
* what epistemic class its outputs receive;
* what evidence it must preserve;
* what authority it possesses;
* what it may not claim;
* how its failures are detected;
* how its output can be invalidated.

---

# 2. Scope

L01 agents operate primarily at the interface between:

```text
L00_REALITY_ENVIRONMENT
        ↕
L01_SENSING_OBSERVATION
        ↕
DOWNSTREAM REPRESENTATION / COGNITION
```

L01 covers sensing and observation acquisition.

It does **not**, by itself, establish:

```text
semantic interpretation

causal explanation

world-model truth

prediction correctness

decision correctness

action authority

memory truth

conscious perception

ground-truth equivalence
```

Those require additional layers, evidence, or governance.

---

# 3. Agent Tensor

[
\boxed{
T_A^{L01}
=========

T[
agent_id,
agent_class,
role,
version,
capabilities,
channels,
inputs,
outputs,
state,
scope,
regime,
HML_scale,
authority,
constraints,
skills,
tools,
workflows,
protocols,
evidence,
provenance,
uncertainty,
dependencies,
failure_state,
recovery_state
]
}
]

---

# 4. Agent Identity

Every addressable L01 agent should have an explicit identity.

```yaml
agent_identity:

  agent_id:

  name:

  primitive:
    L01_SENSING_OBSERVATION

  class:

  version:

  implementation_id:

  origin_architect:
    Trang Phan

  runtime_instance:

  status:

  hash:
```

Hard boundary:

```text
AGENT DEFINITION
!=
AGENT IMPLEMENTATION

AGENT IMPLEMENTATION
!=
ACTIVE AGENT

ACTIVE AGENT
!=
AUTHORIZED AGENT

AUTHORIZED AGENT
!=
VALID OBSERVER
```

---

# 5. Agent Classes

Candidate L01 agent classes:

```text
A01  SENSING COORDINATOR

A02  ENVIRONMENT INTERFACE AGENT

A03  SENSOR ADAPTER AGENT

A04  OBSERVATION ACQUISITION AGENT

A05  MULTIMODAL OBSERVATION AGENT

A06  MEASUREMENT AGENT

A07  TIMESTAMP / TEMPORAL ANCHOR AGENT

A08  SPATIAL / CONTEXT ANCHOR AGENT

A09  SOURCE OBSERVATION AGENT

A10  OBSERVATION TYPING AGENT

A11  QUALITY ASSESSMENT AGENT

A12  UNCERTAINTY ESTIMATION AGENT

A13  PROVENANCE BINDING AGENT

A14  SENSOR FUSION AGENT

A15  CONFLICT DETECTION AGENT

A16  FRESHNESS MONITOR AGENT

A17  REGIME / CONTEXT MONITOR AGENT

A18  OBSERVATION VALIDATION AGENT

A19  ADVERSARIAL OBSERVATION AUDITOR

A20  OBSERVATION QUARANTINE AGENT

A21  SENSOR HEALTH AGENT

A22  CALIBRATION AGENT

A23  OBSERVATION REPAIR AGENT

A24  REOBSERVATION AGENT

A25  OBSERVATION REPLAY / AUDIT AGENT
```

These are architectural role classes, not assertions that implementations currently exist.

---

# 6. A01 — Sensing Coordinator

## Responsibility

Coordinates sensing requirements without itself becoming the source of observation.

```text
REQUEST
↓
DETERMINE OBSERVATION NEED
↓
IDENTIFY CHANNELS
↓
SELECT AGENTS
↓
ASSIGN TASKS
↓
COLLECT RESULTS
↓
ROUTE FOR VALIDATION
```

### Inputs

```yaml
inputs:
  observation_objective:
  target_environment:
  requested_variables: []
  required_freshness:
  required_resolution:
  available_channels: []
  constraints: []
```

### Outputs

```yaml
outputs:
  observation_plan:
  agent_assignments: []
  channel_assignments: []
  unresolved_requirements: []
```

### Invariant

```text
COORDINATOR OUTPUT
!=
OBSERVATION
```

---

# 7. A02 — Environment Interface Agent

## Responsibility

Mediates access to an environment boundary.

Possible interfaces include:

```text
API

database

filesystem

repository

network service

document corpus

sensor bus

human report channel

instrument interface

simulation interface
```

The interface type must remain explicit.

Hard boundary:

```text
SIMULATION INTERFACE
!=
REAL-WORLD SENSOR INTERFACE
```

---

# 8. A03 — Sensor Adapter Agent

Converts sensor-specific or source-specific output into a canonical observation transport form.

Conceptually:

[
O_c = Adapt(O_s, Schema_s \rightarrow Schema_c)
]

where:

* (O_s) = source-format observation;
* (O_c) = canonicalized observation.

Invariant:

[
Adapt(x) \neq ValidateTruth(x)
]

Format conversion does not validate the represented fact.

---

# 9. A04 — Observation Acquisition Agent

## Responsibility

Performs bounded acquisition from a specified channel.

```text
TARGET
↓
CHANNEL
↓
ACCESS CHECK
↓
OBSERVE
↓
CAPTURE RAW RESULT
↓
CAPTURE CHANNEL STATE
↓
RETURN
```

Output states:

```text
OBSERVED

PARTIAL

UNAVAILABLE

FAILED

AMBIGUOUS

UNKNOWN
```

Hard invariant:

```text
FAILED TO OBSERVE X
!=
OBSERVED NOT-X
```

---

# 10. A05 — Multimodal Observation Agent

May coordinate observations across modalities such as:

```text
text

vision

audio

spatial data

telemetry

structured data

machine signals

explicitly available biosignals
```

Availability must be explicit.

[
ModalitiesAvailable
\subseteq
ModalitiesPossible
]

An unavailable modality may not be fabricated.

---

# 11. Multimodal Observation Tensor

[
\boxed{
T_M =
T[
modality,
channel,
availability,
raw_signal,
representation,
timestamp,
resolution,
quality,
uncertainty,
provenance
]
}
]

---

# 12. A06 — Measurement Agent

Transforms an observation through an explicitly defined measurement procedure.

[
M =
Measure(
Observation,
Method,
Instrument,
Calibration,
Unit
)
]

Outputs should preserve:

```text
measured quantity

unit

method

instrument/source

precision

resolution

error

timestamp

calibration state
```

Hard boundary:

```text
MEASURED VALUE
!=
TRUE VALUE
```

---

# 13. A07 — Temporal Anchor Agent

Binds observation time.

It must distinguish:

```text
event_time

observation_time

measurement_time

source_publication_time

retrieval_time

ingestion_time
```

These must not be silently collapsed into one timestamp.

---

# 14. Temporal Observation Tensor

[
\boxed{
T_T =
T[
event_time,
observation_time,
retrieval_time,
ingestion_time,
clock_source,
temporal_uncertainty
]
}
]

---

# 15. A08 — Spatial / Context Anchor Agent

Associates an observation with the context required to interpret its applicability.

Possible dimensions:

```text
location

system

instance

device

session

population

environment

operating regime

experimental condition
```

Hard boundary:

```text
OBSERVED SOMEWHERE
!=
OBSERVED EVERYWHERE
```

---

# 16. A09 — Source Observation Agent

Reads an external source and produces source-grounded observation records.

It must preserve:

```text
source identity

source type

source version

source location

retrieval time

quoted/extracted region where applicable

transformation history
```

Its output is ordinarily:

```text
SOURCE_CLAIM
```

not automatically:

```text
OBSERVATION OF EXTERNAL REALITY
```

Example:

```text
A report states "X"
```

may be observed directly from the report.

But:

```text
X occurred
```

requires separate evidential support.

---

# 17. A10 — Observation Typing Agent

Classifies incoming objects into epistemic classes.

Required distinctions include:

```text
OBSERVATION

MEASUREMENT

SOURCE_CLAIM

DERIVED

MODEL

PREDICTION

MEMORY

DECISION

UNKNOWN
```

Hard invariant:

[
Type(x)=MODEL
\Rightarrow
x \notin OBSERVATION
]

unless independent observation subsequently establishes it.

---

# 18. A11 — Quality Assessment Agent

Evaluates observation quality dimensions such as:

```text
completeness

resolution

noise

missingness

consistency

channel health

measurement integrity

timestamp quality

source integrity
```

Possible output:

```yaml
quality:

  completeness:

  resolution:

  noise:

  missingness:

  integrity:

  channel_health:

  confidence_limit:
```

Quality score must not become truth probability without a validated mapping.

---

# 19. A12 — Uncertainty Estimation Agent

Tracks uncertainty rather than erasing it.

[
T_U^{L01}
=========

T[
sensor,
measurement,
temporal,
spatial,
source,
sampling,
representation,
provenance,
fusion
]
]

Uncertainty may be:

```text
quantified

bounded

ordinal

qualitative

unknown
```

Unknown uncertainty must remain `UNKNOWN`, not `0`.

---

# 20. A13 — Provenance Binding Agent

Constructs observation lineage.

```text
OBSERVATION
↓
CHANNEL
↓
SENSOR / SOURCE
↓
AGENT
↓
TOOL
↓
TRANSFORMATION
↓
VERSION
↓
TIME
↓
ENVIRONMENT
↓
PROVENANCE RECORD
```

Conceptually:

[
Prov(O)
=======

(Source,
Channel,
Agent,
Tool,
Transform,
Time,
Environment,
Version)
]

---

# 21. A14 — Sensor Fusion Agent

Combines compatible observations.

Fusion requires:

```text
identity compatibility

unit compatibility

temporal compatibility

scope compatibility

regime compatibility

provenance awareness

uncertainty awareness
```

Hard boundary:

```text
MULTIPLE OBSERVATIONS
!=
INDEPENDENT OBSERVATIONS
```

Fusion must not double-count shared source ancestry.

---

# 22. Fusion Equation

For compatible observations (O_i):

[
F =
Fuse(
{O_i},
Compatibility,
Uncertainty,
Provenance
)
]

where:

[
Compatibility=FAIL
\Rightarrow
NoDirectFusion
]

---

# 23. A15 — Conflict Detection Agent

Detects incompatible observations.

Conflict dimensions may include:

```text
value

identity

time

location

scope

unit

source

regime

measurement method
```

Output:

```yaml
conflict:

  observations: []

  conflict_type:

  materiality:

  possible_causes: []

  discriminating_evidence: []

  status:
    COMPETING
```

Conflict detection does not itself determine which observation is correct.

---

# 24. A16 — Freshness Monitor Agent

Determines whether an observation remains usable for a specified decision horizon.

Conceptually:

[
Fresh(O,q)
==========

f(
age,
environment_volatility,
decision_horizon,
regime
)
]

Freshness is query-dependent.

```text
OLD
!=
INVALID

RECENT
!=
VALID
```

---

# 25. A17 — Regime / Context Monitor Agent

Detects whether observation applicability conditions may have changed.

Examples:

```text
system version change

market regime change

environment configuration change

sensor replacement

policy change

population change

experimental-condition change
```

A regime change may trigger:

```text
REVALIDATE

REOBSERVE

QUARANTINE

INVALIDATE
```

depending on dependency structure.

---

# 26. A18 — Observation Validation Agent

Checks whether an observation satisfies the L01 contract.

Validation dimensions:

```text
schema

type

source

provenance

timestamp

scope

regime

quality

uncertainty

freshness

constraints
```

Possible outputs:

```text
PASS

CONDITIONAL

QUARANTINE

FAIL

UNKNOWN/GAP
```

Hard boundary:

```text
UNKNOWN/GAP
!=
PASS
```

---

# 27. A19 — Adversarial Observation Auditor

Challenges consequential observations through a distinct validation path.

Checks for:

```text
sensor malfunction

source corruption

stale data

shared ancestry

measurement mismatch

unit mismatch

scope leakage

regime mismatch

generated-content contamination

simulation/reality confusion

selection bias

missing observations

hidden transformations
```

The auditor should seek disconfirming evidence, not merely repeat the primary path.

---

# 28. A20 — Observation Quarantine Agent

Isolates observations whose integrity cannot currently be established.

[
Quarantine(O)
=============

Preserve(O)
\land
BlockTrustedPromotion(O)
]

Quarantine should preserve:

```text
original object

failure reason

provenance

dependencies

affected claims

revalidation requirements
```

---

# 29. A21 — Sensor Health Agent

Monitors the sensing mechanism rather than the observed target.

Possible checks:

```text
availability

latency

error rate

drift

noise

dropout

clock synchronization

schema stability

calibration state
```

Hard boundary:

```text
SENSOR HEALTHY
!=
OBSERVATION TRUE
```

A healthy sensor can still observe an unrepresentative sample.

---

# 30. A22 — Calibration Agent

Maintains evidence concerning measurement calibration.

Calibration record:

```yaml
calibration:

  sensor_id:

  method:

  reference:

  calibrated_at:

  valid_until:

  environment:

  uncertainty:

  result:

  provenance:
```

Calibration claims require actual calibration evidence.

---

# 31. A23 — Observation Repair Agent

Repairs recoverable observation-path failures.

Possible repair targets:

```text
malformed schema

missing metadata

unit conversion error

timestamp parsing

broken source binding

sensor adapter failure

stale observation

corrupt transformation

provenance gap
```

Repair must not fabricate missing measurement content.

---

# 32. A24 — Reobservation Agent

Acquires new evidence when existing observations become stale, conflicted, invalid, or insufficient.

```text
INVALID / STALE / CONFLICTED OBSERVATION
↓
IDENTIFY TARGET
↓
SELECT VALID CHANNEL
↓
REOBSERVE
↓
COMPARE
↓
UPDATE
```

Reobservation creates a new observation event.

It does not rewrite history.

---

# 33. A25 — Observation Replay / Audit Agent

Reconstructs how an observation record was produced.

Requires, where applicable:

```text
input identity

source identity

tool identity

agent identity

transformation version

environment

timestamps

raw evidence

configuration

execution record
```

Replay success supports reproducibility of the transformation path.

It does not prove external-world truth.

---

# 34. Agent Inputs

```yaml
L01AgentInput:

  request_id:

  target:

  environment_id:

  observation_variable:

  channel:

  modality:

  source:

  timestamp_requirement:

  freshness_requirement:

  resolution_requirement:

  scope:

  regime:

  HML_scale:

  authority:

  constraints: []

  prior_observations: []

  provenance_context: []

  tool_context:
```

---

# 35. Agent Outputs

```yaml
L01AgentOutput:

  agent_id:

  run_id:

  observation_id:

  epistemic_class:

  raw_observation:

  normalized_observation:

  measurement:

  unit:

  source:

  channel:

  modality:

  event_time:

  observation_time:

  retrieval_time:

  scope:

  regime:

  quality:

  uncertainty:

  provenance:

  conflicts: []

  gaps: []

  validation_state:

  confidence_ceiling:

  conclusion_class:
```

---

# 36. Agent State Variables

```text
A_id        agent identity

A_v         agent version

A_role      assigned role

A_cap       capability set

A_auth      authority state

A_env       target environment

A_ch        sensing channel

A_mod       modality

A_obs       active observation

A_src       source state

A_t         temporal state

A_q         quality state

A_u         uncertainty state

A_p         provenance state

A_scope     applicability scope

A_regime    regime

A_fail      failure state

A_rec       recovery state
```

---

# 37. Agent Operators

Candidate L01 agent operators:

```text
SENSE

OBSERVE

READ

CAPTURE

MEASURE

TIMESTAMP

LOCATE

NORMALIZE

TYPE

CALIBRATE

ASSESS_QUALITY

ESTIMATE_UNCERTAINTY

BIND_PROVENANCE

TRACE_ANCESTRY

CHECK_FRESHNESS

CHECK_SCOPE

CHECK_REGIME

COMPARE

FUSE

DETECT_CONFLICT

VALIDATE

QUARANTINE

REOBSERVE

REPAIR

REPLAY

ESCALATE

STOP
```

---

# 38. Operator Boundary

No sensing operator may implicitly perform unrestricted inference.

Example:

```text
OBSERVE(image)
```

may produce an image-derived observation.

But:

```text
OBSERVE(image)
→
causal explanation
```

requires additional reasoning and appropriate evidence.

---

# 39. Agent Capability Contract

```yaml
capability_contract:

  agent_id:

  may_read: []

  may_observe: []

  may_measure: []

  may_transform: []

  may_validate: []

  may_write: []

  may_commit: []

  prohibited_operations: []

  required_escalations: []
```

Capability is descriptive.

Authority is normative and externally governed.

---

# 40. Authority Invariant

[
\boxed{
Capability(A,op)
\not\Rightarrow
Authority(A,op)
}
]

An agent capable of calling a sensor, API, database, or state store does not automatically possess permission to do so.

---

# 41. Read / Write Separation

Typical L01 sensing agents should be predominantly read-oriented.

```text
OBSERVE
READ
MEASURE
```

must remain distinct from:

```text
MODIFY ENVIRONMENT
WRITE STATE
COMMIT ACTION
```

If sensing itself modifies the target, the intervention must be explicit.

---

# 42. Observer-Effect Boundary

Some sensing operations may alter the observed environment.

Therefore:

[
Observation
===========

f(Environment,Observer,Method)
]

may be necessary as a structural model.

When observer effects are material, the agent must record:

```text
measurement intervention

instrument interaction

sampling disturbance

query side effects

environment mutation
```

No universal physical observer-effect claim is implied.

---

# 43. H/M/L Applicability

## H — High-Level Sensing

System-wide or cross-domain observation.

Examples:

```text
global environment state

multi-system monitoring

enterprise telemetry

whole-corpus observation

cross-modal environment reconstruction
```

## M — Mid-Level Sensing

Subsystem observation.

Examples:

```text
service telemetry

repository state

market data subsystem

sensor array

document collection

database subsystem
```

## L — Low-Level Sensing

Atomic observations.

Examples:

```text
single API response

single sensor reading

single file value

single timestamp

single database field

single document statement
```

---

# 44. H/M/L Invariant

[
Observation(L)
\not\Rightarrow
State(H)
]

without a validated aggregation path.

Likewise:

[
Failure(L)
\not\Rightarrow
Failure(H)
]

unless the failed local observation is load-bearing for the higher-level conclusion.

---

# 45. Cross-Scale Observation Tensor

[
\boxed{
T_{HML}^{OBS}
=============

T[
observation,
source_scale,
target_scale,
aggregation,
coverage,
sampling,
dependencies,
uncertainty,
validation
]
}
]

---

# 46. Dependencies

```yaml
dependencies:

  upstream:
    - L00_REALITY_ENVIRONMENT

  L01_internal:
    - DEFINITION
    - PURPOSE
    - VARIABLES
    - STATE
    - OPERATORS
    - INVARIANTS
    - EQUATIONS
    - HML
    - PROVENANCE
    - RSCF
    - SKILLS
    - WORKFLOWS
    - PROTOCOLS
    - CONTROL_PLANES
    - FAILURE_MODES
    - REPAIR
    - TESTS
    - GAP_MATRIX

  downstream_candidate_dependencies:
    - representation
    - interpretation
    - inference
    - world_modeling
    - prediction
    - decision
    - action
    - memory
    - metacognition

  infrastructure:
    - agent_registry
    - skill_registry
    - tool_registry
    - provenance_store
    - evidence_store
    - state_store
    - authority_registry
    - validation_engine
    - workflow_engine
```

Exact neighboring primitive identifiers remain source-dependent until authoritative canon establishes them.

---

# 47. Skills

Candidate skills supporting L01 agents include:

```text
multimodal perception

source reading

structured document parsing

measurement integrity auditing

provenance reconstruction

source ancestry resolution

temporal reasoning

scope validation

regime validation

conflict detection

uncertainty auditing

semantic grounding

sensor health assessment

claim verification

reality/simulation distinction
```

Hard boundary:

```text
SKILL AVAILABLE
!=
AGENT AUTHORIZED TO USE SKILL
```

---

# 48. Workflow Integration

L01 agents should participate in bounded workflows such as:

```text
OBSERVATION_ACQUISITION

MEASUREMENT

MULTIMODAL_SENSING

SOURCE_INGESTION

PROVENANCE_BINDING

OBSERVATION_VALIDATION

SENSOR_FUSION

CONFLICT_RESOLUTION

FRESHNESS_REVALIDATION

REOBSERVATION

SENSOR_CALIBRATION

OBSERVATION_REPAIR

OBSERVATION_REPLAY
```

Agents should not bypass workflow-level gates merely because they possess the underlying capability.

---

# 49. Protocols

Candidate protocol messages:

```text
ObservationRequest

ObservationResponse

SensorStatus

MeasurementRequest

MeasurementResponse

CalibrationRecord

ObservationQualityReport

ObservationUncertaintyReport

ProvenanceBundle

ConflictReport

ReobservationRequest

QuarantineEvent

ValidationRequest

ValidationResult

RepairRequest

RecoveryResult
```

---

# 50. Observation Request Protocol

```yaml
ObservationRequest:

  request_id:

  target_environment:

  target_variable:

  channel:

  modality:

  required_resolution:

  required_freshness:

  scope:

  regime:

  constraints:

  authority_context:
```

---

# 51. Observation Response Protocol

```yaml
ObservationResponse:

  request_id:

  agent_id:

  observation_id:

  status:

  epistemic_class:

  value:

  unit:

  raw_reference:

  channel:

  source:

  observed_at:

  event_time:

  scope:

  regime:

  quality:

  uncertainty:

  provenance:

  gaps: []
```

---

# 52. Evidence / Provenance Requirements

Every consequential observation should preserve enough lineage to answer:

```text
WHAT was observed?

WHERE was it observed?

WHEN was it observed?

HOW was it observed?

BY WHICH agent?

THROUGH WHICH tool/channel?

FROM WHICH source?

UNDER WHICH configuration?

WHAT transformations occurred?

WHAT uncertainty remains?
```

---

# 53. Provenance Tensor

[
\boxed{
T_P^{L01}
=========

T[
observation_id,
source_id,
source_root,
channel,
sensor,
agent,
tool,
transform,
version,
environment,
event_time,
observation_time,
retrieval_time,
scope,
regime
]
}
]

---

# 54. Evidence Independence

Multiple agents do not automatically create multiple independent observations.

Example:

```text
Agent A reads Source X
Agent B reads Source X
Agent C reads a summary derived from Source X
```

This may represent one provenance root.

Therefore:

[
IndependentEvidenceCount
\neq
AgentCount
]

---

# 55. Uncertainty Vector

For consequential observations:

[
\boxed{
U_{L01}
=======

(
U_{sensor},
U_{measurement},
U_{sampling},
U_{temporal},
U_{spatial},
U_{representation},
U_{source},
U_{provenance},
U_{fusion}
)
}
]

The vector should remain decomposed where the dimensions can change downstream decisions.

---

# 56. Confidence Ceiling

For observation conclusion (C):

[
\boxed{
Conf(C)
\le
\min(
SourceIntegrity,
SensorIntegrity,
MeasurementIntegrity,
ProvenanceIntegrity,
ScopeCompatibility,
RegimeCompatibility,
TemporalValidity
)
}
]

where each applicable term is bounded by available evidence.

Unknown load-bearing integrity prevents high-confidence promotion.

---

# 57. Control-Plane Requirements

L01 agents operate beneath control-plane authority for consequential access or durable effects.

```text
AGENT
↓
CAPABILITY CHECK
↓
AUTHORITY CHECK
↓
SCOPE CHECK
↓
TOOL / SENSOR ACCESS
↓
OBSERVATION
↓
VALIDATION
↓
ADMISSION
```

The model worker should not own final authority merely because it generated the observation plan.

---

# 58. Control-Plane Tensor

[
\boxed{
T_C^{L01}
=========

T[
agent,
principal,
capability,
operation,
target,
scope,
authority,
constraints,
validity,
revocation,
audit
]
}
]

---

# 59. Agent Registration

An agent should not become addressable merely because a textual role exists.

```yaml
agent_registration:

  agent_id:

  implementation:

  version:

  capabilities: []

  allowed_tools: []

  allowed_channels: []

  authority_class:

  scope:

  validators: []

  status:
```

Possible states:

```text
DECLARED

ADDRESSABLE

IMPLEMENTED

TESTED

VALIDATED

AUTHORIZED

ACTIVE

QUARANTINED

REVOKED
```

These states must not be conflated.

---

# 60. Agent Lifecycle

```text
DECLARED
↓
IMPLEMENTED
↓
REGISTERED
↓
TESTED
↓
VALIDATED
↓
AUTHORIZED
↓
ACTIVE
```

Failure branches:

```text
ACTIVE
├── DEGRADED
├── QUARANTINED
├── SUSPENDED
├── REVOKED
└── FAILED
```

---

# 61. Agent Invariants

## AG-I01 — Identity

Every consequential agent action is attributable to an agent identity/version.

## AG-I02 — Bounded Role

An agent operates only within declared role scope.

## AG-I03 — Capability / Authority Separation

Capability never grants authority.

## AG-I04 — Observation / Inference Separation

Sensing output cannot silently become inference.

## AG-I05 — Source Preservation

Source identity remains attached.

## AG-I06 — Provenance Preservation

Transformations preserve lineage.

## AG-I07 — Temporal Integrity

Relevant timestamps remain distinguishable.

## AG-I08 — Scope Integrity

Observation applicability remains bounded.

## AG-I09 — Regime Integrity

Regime assumptions remain explicit.

## AG-I10 — Uncertainty Preservation

Unknown or uncertain state cannot silently become certainty.

## AG-I11 — Failure Visibility

Agent failure cannot become valid negative evidence.

## AG-I12 — No Self-Validation

Agent output is not automatically validated because the same agent asserts validity.

## AG-I13 — No Self-Authorization

Agents may not grant themselves authority.

## AG-I14 — Conflict Preservation

Conflicting observations remain visible.

## AG-I15 — Source-Independence Integrity

Agent multiplicity does not imply evidence independence.

## AG-I16 — Environment / Simulation Separation

Simulated observations remain typed as simulation-derived.

## AG-I17 — Memory / Observation Separation

Retrieved memory is not a new observation.

## AG-I18 — Reobservation Integrity

New observation does not erase prior observation history.

## AG-I19 — Selective Invalidation

Failed agent outputs invalidate only dependent conclusions.

## AG-I20 — Gap Integrity

Critical unknowns remain `UNKNOWN/GAP`.

---

# 62. Failure Modes

## AG-F01 — Hallucinated Observation

Agent emits content with no observation path.

## AG-F02 — Source Substitution

Agent replaces direct observation with a source claim without preserving distinction.

## AG-F03 — Memory Substitution

Agent presents remembered content as newly observed.

## AG-F04 — Simulation Leakage

Simulated state is presented as real-world observation.

## AG-F05 — Sensor Failure Misclassification

Failure to observe becomes evidence of absence.

## AG-F06 — Timestamp Collapse

Retrieval time is treated as event time.

## AG-F07 — Scope Leakage

Local observation becomes universal claim.

## AG-F08 — Regime Leakage

Observation from one regime is reused in another without validation.

## AG-F09 — Provenance Loss

Observation becomes detached from source/channel lineage.

## AG-F10 — Correlated Fusion

Shared-source observations are counted as independent.

## AG-F11 — Unit Error

Measurements with incompatible units are merged.

## AG-F12 — Calibration Failure

Uncalibrated measurement is treated as calibrated.

## AG-F13 — Agent Drift

Agent behavior diverges from declared contract.

## AG-F14 — Authority Leakage

Agent accesses unauthorized source or effect.

## AG-F15 — Tool Overtrust

Tool result is automatically treated as truth.

## AG-F16 — Conflict Suppression

Contradictory observations are silently averaged or discarded.

## AG-F17 — Uncertainty Collapse

Unknown uncertainty becomes zero.

## AG-F18 — Repair Fabrication

Repair invents missing observation values.

## AG-F19 — Stale Observation

Old observation is presented as current.

## AG-F20 — Canon Overclaim

Proposed agent role is represented as source canon.

---

# 63. Repair / Recovery

Generic L01 agent recovery:

```text
FAILURE DETECTED
↓
IDENTIFY AGENT
↓
IDENTIFY FAILED OPERATION
↓
PRESERVE RAW EVIDENCE
↓
PRESERVE PROVENANCE
↓
QUARANTINE AFFECTED OUTPUT
↓
TRACE DEPENDENCIES
↓
IDENTIFY ROOT-CAUSE HYPOTHESES
↓
REPAIR AGENT / CHANNEL / TRANSFORM
↓
REOBSERVE
↓
REVALIDATE
↓
RESTORE ELIGIBLE DEPENDENTS
```

---

# 64. Selective Invalidation

If observation (O) fails:

[
Invalid(O)
\Rightarrow
Invalidate(Desc_{LB}(O))
]

But:

[
Independent(C,O)
\Rightarrow
Preserve(C)
]

A failed sensor should not automatically invalidate unrelated observations.

---

# 65. Agent Recovery States

```text
HEALTHY

DEGRADED

FAILED

QUARANTINED

REPAIRING

REOBSERVING

REVALIDATING

RECOVERED

REVOKED

UNKNOWN
```

---

# 66. Validators

```text
VALIDATOR_AGENT_IDENTITY

VALIDATOR_AGENT_VERSION

VALIDATOR_AGENT_ROLE

VALIDATOR_AGENT_CAPABILITY

VALIDATOR_AGENT_AUTHORITY

VALIDATOR_AGENT_CHANNEL

VALIDATOR_AGENT_SCOPE

VALIDATOR_AGENT_REGIME

VALIDATOR_AGENT_EPISTEMIC_TYPE

VALIDATOR_AGENT_TIMESTAMP

VALIDATOR_AGENT_PROVENANCE

VALIDATOR_AGENT_SOURCE

VALIDATOR_AGENT_MEASUREMENT

VALIDATOR_AGENT_UNIT

VALIDATOR_AGENT_CALIBRATION

VALIDATOR_AGENT_UNCERTAINTY

VALIDATOR_AGENT_INDEPENDENCE

VALIDATOR_AGENT_CONFLICT

VALIDATOR_AGENT_FRESHNESS

VALIDATOR_AGENT_RECOVERY
```

---

# 67. Minimum Tests

```text
TEST_AG_001
agent cannot emit OBSERVATION without an observation path

TEST_AG_002
failed sensor call does not become negative observation

TEST_AG_003
source claim remains SOURCE_CLAIM

TEST_AG_004
model output cannot become observation automatically

TEST_AG_005
memory retrieval cannot become new observation

TEST_AG_006
simulation output remains simulation-derived

TEST_AG_007
retrieval time cannot silently replace event time

TEST_AG_008
scope mismatch prevents direct reuse

TEST_AG_009
regime mismatch triggers validation

TEST_AG_010
shared-source agents do not count as independent evidence

TEST_AG_011
incompatible units cannot be fused

TEST_AG_012
unknown calibration blocks calibrated status

TEST_AG_013
agent capability does not grant authority

TEST_AG_014
agent cannot self-authorize

TEST_AG_015
conflicting observations remain visible

TEST_AG_016
unknown uncertainty does not become zero

TEST_AG_017
stale observation triggers freshness handling

TEST_AG_018
repair cannot fabricate missing measurement

TEST_AG_019
failed observation selectively invalidates dependents

TEST_AG_020
UNKNOWN/GAP cannot become PASS
```

---

# 68. Adversarial Tests

Test agents against:

```text
prompt injection inside observed content

malformed sensor payload

fabricated timestamp

stale API cache

unit spoofing

source aliasing

duplicate-source amplification

simulation/reality confusion

memory contamination

agent impersonation

tool-response truncation

partial observation

sensor timeout

clock skew

regime transition

calibration expiry

source revocation

provenance deletion

cross-agent consensus illusion

unauthorized sensing request
```

---

# 69. Falsifiers

The proposed L01 agent architecture fails its intended contract if an implementation permits:

```text
agent-generated content to enter as observation without evidence

failed sensing to become evidence of absence

memory to become observation without reobservation

simulation to become reality state

source claims to become verified facts automatically

timestamps to lose semantic type

provenance to disappear during normalization

uncertainty to disappear during fusion

shared ancestry to count as independent confirmation

local observations to become global state without aggregation evidence

agents to self-authorize

tool capability to imply permission

conflicts to be silently erased

repair to invent missing observations

failed agents to contaminate unrelated state

UNKNOWN/GAP to become PASS
```

---

# 70. Gap Matrix

```yaml
gap_status:

  critical:

    - direct authoritative L01 agent canon is not established

    - executable L01 agent implementations are not established by this artifact

    - authoritative agent registry is not established

    - actual sensing-channel implementations are not established

    - operational authority bindings are not established

  decision_relevant:

    - exact L00/L01 ownership boundary requires direct canon confirmation

    - exact downstream L01 primitive boundary requires direct canon confirmation

    - domain-specific sensor schemas remain external

    - calibration requirements are domain-dependent

    - freshness policies remain environment-dependent

    - multimodal fusion rules require modality-specific validation

  explanatory:

    - additional specialist sensing agents may be required by domain

    - distributed sensing may require stronger coordination semantics

    - physical sensors may require hardware-specific health models

  cosmetic:

    - agent naming conventions

    - diagram style

    - agent ID prefixes
```

---

# 71. Hard Boundaries

```text
PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

UNKNOWN/GAP != PASS
```

L01-specific:

```text
AGENT ROLE != IMPLEMENTED AGENT

IMPLEMENTED AGENT != VALIDATED AGENT

VALIDATED AGENT != AUTHORIZED AGENT

SENSING != INTERPRETATION

OBSERVATION != INFERENCE

MEASUREMENT != GROUND TRUTH

SOURCE_CLAIM != OBSERVATION OF CLAIMED EVENT

MEMORY != NEW OBSERVATION

SIMULATION != REALITY

PREDICTION != OBSERVATION

FAILED OBSERVATION != OBSERVED ABSENCE

SENSOR HEALTH != CLAIM TRUTH

MULTIPLE AGENTS != INDEPENDENT EVIDENCE

RECENT != VALID

AVAILABLE TOOL != AUTHORIZED TOOL

REPAIR != FABRICATION

MODEL AGENT ARCHITECTURE != SOURCE CANON
```

---

# 72. RSCF Capsule

```yaml
rscf:

  claim:
    L01_SENSING_OBSERVATION/AGENTS defines a bounded
    AMOS agent architecture for acquiring, measuring,
    typing, qualifying, provenance-binding, validating,
    reconciling, and repairing observations without
    allowing sensing workers to silently promote
    inference, memory, simulation, or generated content
    into observed reality.

  claim_class:
    MODEL

  premises:
    - L01 is treated as the sensing/observation primitive
    - sensing must remain distinguishable from inference
    - observation provenance must remain recoverable
    - measurement requires explicit method and uncertainty
    - agent capability and authority must remain distinct
    - unknown observation state cannot be promoted to pass
    - correlated observations cannot be assumed independent

  evidence:
    - supplied L01 AGENTS placeholder
    - supplied L00 reality/environment contract context
    - AMOS control-plane principles
    - AMOS provenance principles
    - AMOS RSCF principles
    - AMOS authority and selective-invalidation principles

  provenance:
    origin_architect: Trang Phan
    architecture_family: AMOS
    layer: L01_SENSING_OBSERVATION
    component: AGENTS
    reconstruction_status: MODEL_DERIVED

  scope:
    AMOS_OS/COGNITIVE_MATRIX/L01_SENSING_OBSERVATION/AGENTS

  regime:
    AI and governed cognitive infrastructure

  freshness:
    revalidate_when:
      - direct L01 agent canon is discovered
      - L00/L01 boundary changes
      - agent registry changes
      - sensing protocols change
      - control-plane semantics change
      - multimodal architecture changes

  dependencies:
    - L00_REALITY_ENVIRONMENT
    - L01 DEFINITION
    - L01 PURPOSE
    - L01 VARIABLES
    - L01 STATE
    - L01 OPERATORS
    - L01 INVARIANTS
    - L01 EQUATIONS
    - L01 HML
    - L01 PROVENANCE
    - L01 RSCF
    - L01 SKILLS
    - L01 WORKFLOWS
    - L01 PROTOCOLS
    - L01 CONTROL_PLANES
    - L01 FAILURE_MODES
    - L01 REPAIR
    - L01 TESTS

  competing:
    - centralized sensing architecture
    - distributed sensor-agent architecture
    - event-driven sensing architecture
    - blackboard perception architecture
    - direct tool-mediated observation architecture
    - multimodal fusion architecture

  falsifiers:
    - sensing outputs cannot preserve epistemic type
    - provenance cannot survive transformations
    - simulation and observation cannot be distinguished
    - agent authority cannot be externally constrained
    - shared-source evidence cannot be detected
    - uncertainty cannot remain attached to observation
    - invalid observations cannot selectively invalidate dependents

  confidence_ceiling:
    architecture-level only;
    direct L01 source canon, executable agent implementations,
    operational authority, calibration, and runtime validation
    remain unresolved
```

---

# 73. Canonical Agent Equations

### Agent contract

[
\boxed{
Agent
=====

Identity
+
Role
+
Capability
+
Scope
+
Authority
+
Evidence
+
Provenance
+
Constraints
}
]

### Observation law

[
\boxed{
Observation
===========

Acquire(
Environment,
Channel,
Method,
Time
)
}
]

### Measurement law

[
\boxed{
Measurement
===========

Measure(
Observation,
Instrument,
Method,
Calibration
)
}
]

### Epistemic law

[
\boxed{
Observation
\neq
Inference
}
]

### Authority law

[
\boxed{
Capability
\neq
Authority
}
]

### Independence law

[
\boxed{
AgentCount
\neq
IndependentEvidenceCount
}
]

### Failure law

[
\boxed{
ObservationFailure
\neq
NegativeObservation
}
]

### Freshness law

[
\boxed{
PreviouslyValid(O)
\not\Rightarrow
CurrentlyValid(O)
}
]

### Recovery law

[
\boxed{
Recovery
========

Repair
+
Reobservation
+
Revalidation
}
]

### Unknown law

[
\boxed{
CriticalUnknown
\Rightarrow
UNKNOWN/GAP
}
]

---

# 74. Completion State

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

  HML:
    status: MODEL_COMPLETE

  control_plane:
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

  uncertainty:
    status: MODEL_COMPLETE

  confidence_ceiling:
    status: MODEL_COMPLETE

  failure_modes:
    status: MODEL_COMPLETE

  repair_recovery:
    status: MODEL_COMPLETE

  tests_validators:
    status: MODEL_COMPLETE

  falsifiers:
    status: MODEL_COMPLETE

  gap_status:
    status: EXPLICIT

  direct_source_canon:
    status: GAP

  executable_agents:
    status: GAP

  operational_sensor_evidence:
    status: GAP

  executed_validation:
    status: GAP

  authority_bindings:
    status: GAP

  conclusion_class:
    MODEL / CONDITIONAL
```

---

# 75. Final Agent Contract

`L01_SENSING_OBSERVATION/AGENTS.md` defines the bounded agent roles through which AMOS may establish contact with observable environment state.

Its primary architectural responsibility is to ensure that:

```text
ENVIRONMENT
↓
SENSING
↓
OBSERVATION
↓
MEASUREMENT
↓
QUALITY
↓
UNCERTAINTY
↓
PROVENANCE
↓
VALIDATION
```

does not collapse into:

```text
AGENT GENERATED IT
↓
THEREFORE IT WAS OBSERVED
↓
THEREFORE IT IS REAL
```

The governing L01 agent chain is:

[
\boxed{
Environment
\rightarrow
Channel
\rightarrow
Agent
\rightarrow
Observation
\rightarrow
Typing
\rightarrow
Provenance
\rightarrow
Validation
\rightarrow
GroundedInput
}
]

with the mandatory boundaries:

[
\boxed{
Observation \neq Inference
}
]

[
\boxed{
Measurement \neq GroundTruth
}
]

[
\boxed{
Capability \neq Authority
}
]

[
\boxed{
AgentCount \neq IndependentEvidenceCount
}
]

and:

[
\boxed{
CriticalUnknown
\Rightarrow
UNKNOWN/GAP
}
]

Until direct authoritative L01 agent canon, executable implementations, runtime authority bindings, sensing-channel evidence, and executed validation are established, the strongest warranted classification remains:

```text
MODEL / CONDITIONAL
```

---

**Related:** [[L01_SENSING_OBSERVATION]] · [[L01_SENSING_OBSERVATION — Definition]] · [[L01_SENSING_OBSERVATION — Purpose]] · [[L01_SENSING_OBSERVATION — Variables]] · [[L01_SENSING_OBSERVATION — State]] · [[L01_SENSING_OBSERVATION — Operators]] · [[L01_SENSING_OBSERVATION — Invariants]] · [[L01_SENSING_OBSERVATION — Equations]] · [[L01_SENSING_OBSERVATION — HML]] · [[L01_SENSING_OBSERVATION — Dependencies]] · [[L01_SENSING_OBSERVATION — Control Planes]] · [[L01_SENSING_OBSERVATION — Protocols]] · [[L01_SENSING_OBSERVATION — Provenance]] · [[L01_SENSING_OBSERVATION — RSCF]] · [[L01_SENSING_OBSERVATION — Skills]] · [[L01_SENSING_OBSERVATION — Workflows]] · [[L01_SENSING_OBSERVATION — Failure Modes]] · [[L01_SENSING_OBSERVATION — Repair]] · [[L01_SENSING_OBSERVATION — Tests]] · [[L01_SENSING_OBSERVATION — Gap Matrix]] · [[L00_REALITY_ENVIRONMENT]] · [[00-Home]] · [[06-Knowledge-Base-MOC]]

```
```

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
