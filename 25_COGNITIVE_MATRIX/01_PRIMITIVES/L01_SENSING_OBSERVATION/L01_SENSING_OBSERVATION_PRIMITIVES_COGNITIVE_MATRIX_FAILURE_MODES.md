---
tags: ['cognitive_matrix', 'primitives', 'l01_sensing_observation', 'note']
---

Below is the full paste-ready `L01_SENSING_OBSERVATION/FAILURE_MODES.md`. I’m keeping the failure taxonomy as an **AMOS structural contract**, not claiming that these failure modes are already implemented, runtime-validated, or exhaustive empirical laws.

---
tags:
  - amos
  - cognitive-matrix
  - l01
  - sensing-observation
  - failure-modes
  - detection
  - quarantine
  - recovery
  - provenance
  - uncertainty
  - control-plane
  - rscf
  - rscf/type-model
---

# L01_SENSING_OBSERVATION — Failure Modes

**Class:** `COGNITIVE_PRIMITIVE_FAILURE_CONTRACT`  
**Origin architect / steward:** Trang Phan  
**Architecture:** `AMOS_OS / COGNITIVE_MATRIX`  
**Primitive:** `L01_SENSING_OBSERVATION`  
**Artifact:** `FAILURE_MODES.md`  
**Role:** `SENSING / OBSERVATION / MEASUREMENT / PROVENANCE / VALIDATION / FAILURE / RECOVERY CONTRACT`  
**Status:** `STRUCTURAL FAILURE CONTRACT / SOURCE-GAP BOUNDED`  
**Conclusion class:** `AMOS_MODEL / CONDITIONAL`

> **Epistemic boundary:** this document defines a governed AMOS failure taxonomy for `L01_SENSING_OBSERVATION`. It does not establish that every listed failure has an executable detector, validated runtime implementation, calibrated probability model, or universal empirical applicability.

---

# 0. Purpose

`L01_SENSING_OBSERVATION/FAILURE_MODES.md` defines how AMOS identifies, classifies, contains, propagates, repairs, and revalidates failures occurring between an addressable environment and a trusted observation.

The failure spine is:

```text
environment
↓
access
↓
sensing
↓
acquisition
↓
raw observation
↓
typing
↓
normalization
↓
measurement
↓
provenance binding
↓
scope / regime binding
↓
validation
↓
admission
↓
downstream use
```

A failure may occur at any edge or state.

The central safety rule is:

```text
OBSERVATION FAILURE
!=
NEGATIVE OBSERVATION
```

and:

```text
MISSING
!=
FALSE

UNAVAILABLE
!=
ABSENT

CORRUPTED
!=
NEGATIVE

UNKNOWN
!=
ZERO

FAILED SENSOR
!=
FAILED ENVIRONMENT

FAILED RETRIEVAL
!=
NONEXISTENCE
```

The failure layer therefore prevents sensing defects from being silently converted into claims about reality.

---

# 1. Source / Canon References

Current structural source classes include:

```text
supplied L01_SENSING_OBSERVATION placeholder family

L01 Definition contract

L01 Dependencies contract

L01 Equations contract

L01 Control Planes contract

L01 Agents contract

L00_REALITY_ENVIRONMENT contract family

AMOS cognition/evaluation architecture

AMOS metacognition / confidence architecture

AMOS typed tensor architecture

AMOS H/M/L architecture

AMOS RSCF architecture

AMOS provenance architecture

AMOS selective invalidation architecture

AMOS repair / recovery principles

AMOS control-plane governance
```

The AMOS metacognitive architecture preserves the distinction:

```text
CONFIDENCE
!=
EVIDENCE
```

and requires separation of:

```text
evidence strength
model confidence
scope confidence
execution confidence
```

with attention to hidden assumptions, contradiction, alternatives, falsifiers, and the weakest load-bearing premise.

Direct authoritative source recovery for a canonical exhaustive `L01` failure registry remains incomplete.

Therefore:

```text
THIS FAILURE TAXONOMY
=
AMOS STRUCTURAL RECONSTRUCTION

THIS FAILURE TAXONOMY
!=
PROVEN COMPLETE SOURCE CANON

THIS FAILURE TAXONOMY
!=
EMPIRICALLY EXHAUSTIVE FAILURE LAW
```

---

# 2. Definition

An `L01` failure is any condition that prevents an observation from safely satisfying its declared sensing, semantic, provenance, temporal, scope, regime, quality, authority, validation, or downstream-use contract.

Formally:

```text
Failure_L01(x)
=
Violation(
  sensing_contract
  OR observation_contract
  OR measurement_contract
  OR provenance_contract
  OR temporal_contract
  OR scope_contract
  OR regime_contract
  OR validation_contract
  OR governance_contract
)
```

This is an `AMOS_MODEL` relation.

---

# 3. Failure Is Not Necessarily Falsity

A failed observation process does not necessarily mean that the observation value is false.

Likewise, a correct value produced by a failed process does not automatically become trusted.

```text
PROCESS_FAILURE
!=
VALUE_FALSE

VALUE_CORRECT
!=
PROCESS_VALID
```

A value may accidentally be correct while its provenance or acquisition process is invalid.

AMOS therefore distinguishes:

```text
outcome correctness

process validity

evidence sufficiency

provenance integrity

scope validity

authority validity
```

---

# 4. Scope

This failure contract covers:

```text
environment addressability

source accessibility

sensor/tool availability

sensor configuration

observation acquisition

measurement

sampling

normalization

typing

units

timestamps

freshness

scope

regime

resolution

provenance

source identity

ancestry

evidence independence

observation fusion

conflict handling

agent behavior

Skill behavior

workflow execution

protocol exchange

control-plane enforcement

commit/admission

persistent reuse

reobservation

repair

selective invalidation
```

It does not by itself define domain-specific failure physics for every sensor, scientific instrument, biological sense, API, database, multimodal model, or external environment.

---

# 5. Typed Inputs

```yaml
L01FailureInput:

  observation_id:
    type: ObservationID | null

  target:
    type: EnvironmentTarget | SourceTarget | null

  raw_observation:
    type: RawObservation | null

  typed_observation:
    type: TypedObservation | null

  measurement:
    type: Measurement | null

  observer:
    type: AgentID | SystemID | HumanID | null

  channel:
    type: ChannelID | null

  modality:
    type: Modality | null

  instrument:
    type: InstrumentID | ToolID | null

  method:
    type: MethodID | null

  event_time:
    type: Timestamp | UNKNOWN

  observation_time:
    type: Timestamp | UNKNOWN

  retrieval_time:
    type: Timestamp | UNKNOWN

  scope:
    type: ScopeEnvelope | UNKNOWN

  regime:
    type: RegimeID | UNKNOWN

  provenance:
    type: ProvenanceGraph | UNKNOWN

  uncertainty:
    type: UncertaintyTensor | UNKNOWN

  validation_state:
    type: ValidationState

  authority_state:
    type: AuthorityState | UNKNOWN

  dependency_graph:
    type: DependencyGraph | null
```

---

# 6. Typed Outputs

```yaml
L01FailureOutput:

  failure_id:
    type: FailureID

  failure_class:
    type: FailureClass

  failure_subclass:
    type: FailureSubclass

  severity:
    type:
      - INFO
      - LOW
      - MODERATE
      - HIGH
      - CRITICAL
      - UNKNOWN

  epistemic_effect:
    type:
      - NONE
      - DOWNGRADE
      - CONDITIONAL
      - COMPETING
      - QUARANTINE
      - REJECT
      - UNKNOWN_GAP

  affected_objects:
    type: list[ObjectID]

  affected_dependencies:
    type: list[DependencyEdge]

  propagation_scope:
    type:
      - LOCAL
      - SUBSYSTEM
      - HML_CROSS_SCALE
      - GLOBAL_CANDIDATE
      - UNKNOWN

  recoverability:
    type:
      - IMMEDIATE
      - REOBSERVABLE
      - REPAIRABLE
      - REQUIRES_EXTERNAL_EVIDENCE
      - IRRECOVERABLE_CURRENTLY
      - UNKNOWN

  containment_action:
    type: ContainmentAction

  repair_action:
    type: RepairAction | null

  revalidation_required:
    type: boolean

  provenance:
    type: ProvenanceRecord

  confidence_ceiling:
    type: Confidence | UNKNOWN

  falsifiers:
    type: list[Falsifier]
```

---

# 7. Failure State Variables

```text
F_id
F_class
F_subclass
F_severity
F_time
F_origin
F_target
F_channel
F_agent
F_tool
F_scope
F_regime
F_provenance
F_uncertainty
F_detectability
F_recoverability
F_propagation
F_dependencies
F_containment
F_repair_state
F_revalidation_state
F_confidence
```

Canonical state tensor:

```text
T_F[
  failure,
  class,
  severity,
  origin,
  time,
  scope,
  regime,
  provenance,
  uncertainty,
  dependencies,
  propagation,
  containment,
  recoverability,
  validation
]
```

---

# 8. Failure Lifecycle

```text
NORMAL
↓
ANOMALY_CANDIDATE
↓
DETECTED
↓
CLASSIFIED
↓
SCOPED
↓
CONTAINED
↓
DEPENDENCY_TRACED
↓
REPAIR_CANDIDATE
↓
REPAIRED
↓
REOBSERVED
↓
REVALIDATED
↓
RESTORED
```

Alternative terminal states:

```text
QUARANTINED

REJECTED

UNRESOLVED

IRRECOVERABLE_CURRENTLY

UNKNOWN/GAP
```

---

# 9. Failure Detection Operator

```text
DetectFailure(
  observation,
  expected_contract,
  current_state
)
→
FailureCandidate
```

Detection does not itself prove root cause.

```text
DETECTED_ANOMALY
!=
ROOT_CAUSE
```

---

# 10. Failure Classification Operator

```text
ClassifyFailure(
  failure_candidate,
  evidence,
  context
)
→
FailureClass
```

Classification must remain:

```text
CONDITIONAL
```

when discriminating evidence is insufficient.

---

# 11. Failure Localization Operator

```text
LocalizeFailure(F)
→
{
  layer,
  component,
  edge,
  earliest_supported_failure_point
}
```

The earliest observed symptom must not automatically be treated as the causal origin.

```text
FIRST_VISIBLE_FAILURE
!=
ROOT_CAUSE
```

---

# 12. Failure Containment Operator

```text
Contain(F)
→
{
  quarantine,
  block_reuse,
  suspend_transition,
  restrict_scope,
  trigger_revalidation
}
```

Containment should minimize unnecessary invalidation.

---

# 13. Dependency Trace Operator

```text
TraceDependents(F)
→
Descendants(F)
```

Only load-bearing descendants should be automatically invalidated.

```text
FAILED_PREMISE
→
INVALIDATE_DEPENDENTS

FAILED_PREMISE
!=
INVALIDATE_EVERYTHING
```

---

# 14. Reobservation Operator

```text
Reobserve(
  target,
  channel,
  method,
  time
)
→
NewObservation
```

Reobservation creates a new observation state.

It does not rewrite the historical observation.

---

# 15. Repair Operator

```text
Repair(F)
→
RepairCandidate
```

A repair proposal must remain separate from committed repair state.

```text
REPAIR_PROPOSAL
!=
REPAIR_COMMIT
```

---

# 16. Revalidation Operator

```text
Revalidate(
  repaired_state,
  affected_dependencies
)
→
ValidationResult
```

Successful repair alone does not restore trusted use.

```text
REPAIR_SUCCESS
!=
REVALIDATION_SUCCESS
```

---

# 17. Core Failure Invariants

## INV-F01 — Observation Failure Is Not Absence

```text
FAILED_OBSERVATION
!=
TARGET_ABSENT
```

## INV-F02 — Missing Is Not Zero

```text
MISSING
!=
0
```

## INV-F03 — Unknown Is Not False

```text
UNKNOWN
!=
FALSE
```

## INV-F04 — Retrieval Failure Is Not Nonexistence

```text
RETRIEVAL_FAILED
!=
SOURCE_DOES_NOT_EXIST
```

## INV-F05 — Sensor Failure Is Not Environment Failure

```text
SENSOR_FAILED
!=
ENVIRONMENT_FAILED
```

## INV-F06 — Stale Is Not Necessarily False

```text
STALE
!=
FALSE
```

## INV-F07 — Conflict Is Not Automatic Corruption

```text
CONFLICT
!=
CORRUPTION
```

## INV-F08 — Repair Does Not Erase History

```text
REPAIR
!=
HISTORY_DELETION
```

## INV-F09 — Quarantine Is Not Deletion

```text
QUARANTINE
!=
DELETE
```

## INV-F10 — Detection Is Not Causal Proof

```text
FAILURE_DETECTED
!=
CAUSE_IDENTIFIED
```

## INV-F11 — Capability Is Not Authority

```text
CAPABILITY
!=
AUTHORITY
```

## INV-F12 — Proposal Is Not Commit

```text
PROPOSAL
!=
COMMIT
```

## INV-F13 — Unknown Cannot Pass

```text
UNKNOWN/GAP
!=
PASS
```

## INV-F14 — Local Failure Does Not Imply Global Failure

```text
LOCAL_FAILURE
!=
GLOBAL_INVALIDITY
```

## INV-F15 — Confidence Cannot Override Evidence

```text
MODEL_CONFIDENCE
!=
EVIDENCE_STRENGTH
```

---

# 18. Top-Level Failure Taxonomy

```text
F01  TARGET / ENVIRONMENT FAILURE

F02  ACCESS / ADDRESSABILITY FAILURE

F03  SENSOR / TOOL FAILURE

F04  CHANNEL / MODALITY FAILURE

F05  ACQUISITION FAILURE

F06  SAMPLING / COVERAGE FAILURE

F07  MEASUREMENT FAILURE

F08  CALIBRATION FAILURE

F09  TYPING / SCHEMA FAILURE

F10  UNIT / SCALE FAILURE

F11  NORMALIZATION / TRANSFORMATION FAILURE

F12  TEMPORAL FAILURE

F13  FRESHNESS FAILURE

F14  SCOPE FAILURE

F15  REGIME FAILURE

F16  RESOLUTION FAILURE

F17  PROVENANCE FAILURE

F18  SOURCE IDENTITY FAILURE

F19  INDEPENDENCE / SYBIL FAILURE

F20  QUALITY FAILURE

F21  UNCERTAINTY FAILURE

F22  FUSION FAILURE

F23  CONFLICT FAILURE

F24  EPISTEMIC CLASSIFICATION FAILURE

F25  CAUSAL OVERREACH FAILURE

F26  AGENT FAILURE

F27  SKILL FAILURE

F28  WORKFLOW FAILURE

F29  PROTOCOL FAILURE

F30  CONTROL-PLANE FAILURE

F31  AUTHORITY FAILURE

F32  TRANSACTION / COMMIT FAILURE

F33  MEMORY / PERSISTENCE FAILURE

F34  H/M/L SCALE FAILURE

F35  DEPENDENCY / INVALIDATION FAILURE

F36  REPAIR FAILURE

F37  REVALIDATION FAILURE

F38  OBSERVABILITY FAILURE

F39  ADVERSARIAL / DECEPTIVE INPUT FAILURE

F40  UNKNOWN / UNCLASSIFIED FAILURE
```

---

# 19. F01 — Target / Environment Failure

Occurs when the target environment itself cannot satisfy the assumed observation contract.

Examples:

```text
target disappeared

target changed identity

target became inaccessible

target state transitioned during observation

target definition was ambiguous

wrong target was observed
```

Detection:

```text
target identity checks

environment version checks

temporal consistency

cross-reference against target contract
```

Response:

```text
STOP

REIDENTIFY TARGET

REOBSERVE

QUARANTINE PRIOR OBSERVATION
```

---

# 20. F02 — Access / Addressability Failure

Examples:

```text
permission denied

endpoint unavailable

resource inaccessible

source cannot be resolved

network path unavailable

address points to wrong object
```

Critical invariant:

```text
NOT ACCESSIBLE
!=
DOES NOT EXIST
```

Response:

```text
RETRY if justified

USE authorized alternative path

ESCALATE

UNKNOWN/GAP
```

---

# 21. F03 — Sensor / Tool Failure

Examples:

```text
sensor offline

tool execution failed

instrument malfunction

API failure

parser crash

camera unavailable

microphone unavailable

connector failure
```

Critical invariant:

```text
TOOL_FAILURE
!=
NEGATIVE_OBSERVATION
```

---

# 22. F04 — Channel / Modality Failure

Examples:

```text
wrong modality selected

channel unavailable

channel too noisy

modality cannot represent target property

channel mismatch

cross-modal translation failure
```

Response may include:

```text
switch channel

add independent modality

reduce claim scope

mark UNKNOWN
```

---

# 23. F05 — Acquisition Failure

Examples:

```text
partial capture

truncated response

incomplete file

dropped frames

interrupted stream

timeout

malformed acquisition
```

State:

```text
PARTIAL
```

must remain distinguishable from:

```text
COMPLETE
```

---

# 24. F06 — Sampling / Coverage Failure

Examples:

```text
sample too narrow

selection bias

missing regions

temporal undercoverage

spatial undercoverage

population mismatch

systematic exclusion
```

Hard boundary:

```text
NOT OBSERVED
!=
OBSERVED ABSENT
```

A negative conclusion requires adequate coverage.

---

# 25. F07 — Measurement Failure

Examples:

```text
measurement unavailable

wrong quantity measured

measurement noise too high

incorrect transformation

instrument output misread

derived metric substituted for direct measurement
```

Critical distinction:

```text
MEASUREMENT
!=
UNDERLYING REALITY
```

---

# 26. F08 — Calibration Failure

Examples:

```text
expired calibration

unknown calibration state

wrong calibration coefficients

calibration drift

calibration outside valid regime
```

Response:

```text
DOWNGRADE

RECALIBRATE

REOBSERVE

QUARANTINE affected measurements
```

---

# 27. F09 — Typing / Schema Failure

Examples:

```text
unknown variable type

wrong schema

field collision

semantic alias collision

string interpreted as numeric

measurement interpreted as claim

prediction interpreted as observation
```

Hard failure:

```text
TYPE_MISMATCH
→
NO TRUSTED PROMOTION
```

---

# 28. F10 — Unit / Scale Failure

Examples:

```text
meters vs feet

seconds vs milliseconds

percentage vs proportion

nominal vs real quantity

local scale vs aggregate scale
```

Hard invariant:

```text
UNIT_MISMATCH
→
FAIL
```

unless valid conversion occurs.

---

# 29. F11 — Normalization / Transformation Failure

Examples:

```text
semantic content lost

precision lost

provenance stripped

timestamps removed

units removed

scope removed

transformation changes meaning

compression deletes load-bearing detail
```

Response:

```text
ROLL BACK transformation

restore raw source

reprocess

compare transformed/raw representations
```

---

# 30. F12 — Temporal Failure

Examples:

```text
event time confused with observation time

retrieval time treated as event time

clock mismatch

timestamp absent

future leakage

out-of-order events
```

Hard boundary:

```text
EVENT_TIME
!=
OBSERVATION_TIME
!=
RETRIEVAL_TIME
```

unless explicitly established.

---

# 31. F13 — Freshness Failure

Examples:

```text
stale observation

freshness unknown

environment changed after observation

reused old evidence after regime shift
```

Response:

```text
REOBSERVE

REVALIDATE

DOWNGRADE

UNKNOWN/GAP
```

depending on decision relevance.

---

# 32. F14 — Scope Failure

Examples:

```text
sample generalized to population

one subsystem generalized to entire system

one geography generalized globally

one instrument generalized across methods

one task generalized across domains
```

Hard invariant:

```text
VALID_IN_SCOPE_A
!=
VALID_IN_SCOPE_B
```

without evidence supporting transfer.

---

# 33. F15 — Regime Failure

Examples:

```text
normal-state model reused during stress

pre-change evidence reused after structural shift

sensor valid in one operating condition only

historical relation reused after system redesign
```

Response:

```text
DETECT REGIME SHIFT

INVALIDATE REGIME-DEPENDENT DESCENDANTS

REOBSERVE / REVALIDATE
```

---

# 34. F16 — Resolution Failure

Examples:

```text
claim finer than measurement resolution

aggregation hides local variation

low-frequency sampling used for high-frequency claim

semantic summary treated as raw detail
```

Invariant:

```text
CLAIM_RESOLUTION
<=
SUPPORTED_OBSERVATION_RESOLUTION
```

unless a separately validated model supplies additional resolution.

---

# 35. F17 — Provenance Failure

Examples:

```text
source missing

source identity lost

transformation ancestry missing

tool provenance missing

version unknown

time unknown

scope provenance missing

derivation path broken
```

Critical response:

```text
QUARANTINE
```

when provenance is load-bearing.

---

# 36. F18 — Source Identity Failure

Examples:

```text
two sources accidentally merged

same source treated as two entities

alias not resolved

wrong document version

wrong repository

wrong branch

wrong sensor identity
```

Response:

```text
RESOLVE IDENTITY

REBUILD ANCESTRY

RECALCULATE DEPENDENT CONFIDENCE
```

---

# 37. F19 — Independence / Sybil Failure

Occurs when apparently distinct evidence sources share hidden ancestry.

Examples:

```text
multiple articles copying one source

multiple agents reading same evidence

mirrored datasets

repackaged benchmark

same API exposed through different interfaces
```

Hard law:

```text
MULTIPLE ARTIFACTS
!=
MULTIPLE INDEPENDENT SOURCES
```

Response:

```text
collapse shared ancestry

recompute independent support count

downgrade confidence where required
```

---

# 38. F20 — Quality Failure

Dimensions may include:

```text
noise

completeness

precision

coverage

consistency

calibration

resolution

source integrity
```

Important:

```text
LOW QUALITY
!=
FALSE

HIGH QUALITY
!=
TRUE
```

---

# 39. F21 — Uncertainty Failure

Examples:

```text
uncertainty omitted

uncertainty collapsed to one scalar

source uncertainty ignored

scope uncertainty ignored

temporal uncertainty ignored

execution uncertainty ignored
```

AMOS uncertainty should remain typed where material.

Suggested vector:

```text
U[
  evidence,
  model,
  scope,
  temporal,
  causal,
  execution,
  provenance_independence
]
```

---

# 40. F22 — Fusion Failure

Examples:

```text
incompatible units merged

different regimes merged

different populations merged

different temporal windows merged

dependent sources averaged as independent

different modalities fused without mapping
```

Response:

```text
BLOCK FUSION

SEPARATE OBSERVATIONS

TRANSLATE only with validated mapping
```

---

# 41. F23 — Conflict Failure

A conflict becomes a failure when the system:

```text
hides contradiction

forces consensus

chooses one source without justification

averages incompatible observations

deletes minority evidence

fails to seek discriminating evidence
```

Correct state may be:

```text
COMPETING
```

---

# 42. F24 — Epistemic Classification Failure

Examples:

```text
SOURCE_CLAIM → OBSERVATION

MODEL → OBSERVATION

PREDICTION → OUTCOME

SIMULATION → REALITY

MEMORY → CURRENT_OBSERVATION

DERIVED → DIRECT
```

Hard firewall:

```text
EPISTEMIC CLASS
MUST REMAIN EXPLICIT
```

---

# 43. F25 — Causal Overreach Failure

Examples:

```text
correlation interpreted as cause

sequence interpreted as cause

structural similarity interpreted as cause

observation interpreted as intervention evidence
```

Hard boundary:

```text
OBSERVATION
!=
CAUSAL PROOF
```

---

# 44. F26 — Agent Failure

Examples:

```text
wrong target

wrong tool

wrong parameters

premature conclusion

unsupported inference

failure hidden

scope ignored

authority exceeded

provenance omitted
```

Agent failure may be:

```text
COGNITIVE

EXECUTION

GOVERNANCE

PROVENANCE

COMMUNICATION
```

---

# 45. F27 — Skill Failure

Examples:

```text
wrong Skill selected

Skill applied outside scope

Skill output incorrectly promoted

Skill strips provenance

Skill changes variable meaning

Skill assumes authority it does not possess
```

Hard rule:

```text
SKILL CAPABILITY
!=
CONTROL-PLANE AUTHORITY
```

---

# 46. F28 — Workflow Failure

Examples:

```text
required stage skipped

validation skipped

steps reordered incorrectly

failed stage ignored

loop never terminates

reobservation omitted

commit occurs before validation
```

Workflow state should fail closed on unresolved hard gates.

---

# 47. F29 — Protocol Failure

Examples:

```text
message lost

schema mismatch

version mismatch

receipt missing

duplicate message

replay

out-of-order transition

provenance dropped in handoff
```

Protocol failure must not silently mutate observation semantics.

---

# 48. F30 — Control-Plane Failure

Examples:

```text
validator bypass

authority check omitted

stale state accepted

commit-time check skipped

read-set mismatch ignored

constraint enforcement missing
```

This is a high-severity class because local cognition may appear correct while governance is invalid.

---

# 49. F31 — Authority Failure

Examples:

```text
agent has tool but lacks permission

scope exceeded

authority expired

delegation revoked

wrong principal

unauthorized persistent write
```

Hard invariant:

```text
CAPABILITY
!=
AUTHORITY
```

---

# 50. F32 — Transaction / Commit Failure

Examples:

```text
stale read

concurrent modification

partial commit

proposal mistaken for commit

validation changed before commit

authority changed before commit
```

Required response:

```text
ABORT

REFRESH

REVALIDATE

REPROPOSE
```

---

# 51. F33 — Memory / Persistence Failure

Examples:

```text
stale observation reused as current

historical context lost

memory overwritten

provenance stripped

contradictory memory silently merged

revoked evidence remains trusted
```

Hard boundary:

```text
MEMORY RETRIEVAL
!=
NEW OBSERVATION
```

---

# 52. F34 — H/M/L Scale Failure

Examples:

```text
local observation generalized globally

global aggregate imposed on local state

mid-level subsystem ignored

cross-scale mapping assumed

aggregation destroys heterogeneity
```

Hard boundary:

```text
L
!=
M
!=
H
```

and:

```text
L → H
```

requires explicit aggregation evidence.

---

# 53. F35 — Dependency / Invalidation Failure

Two major forms:

### Under-invalidation

Failed premise remains trusted downstream.

### Over-invalidation

Unrelated state is destroyed because one premise failed.

Correct rule:

```text
INVALID(p)
→
INVALIDATE(load-bearing descendants(p))
```

while preserving independent state.

---

# 54. F36 — Repair Failure

Examples:

```text
repair targets symptom not cause

repair changes specification

repair deletes contradictory evidence

repair creates new scope leakage

repair introduces new provenance gap

repair repeats failed path without changed evidence
```

Hard rule:

```text
REPAIR
!=
MAKE TEST GREEN AT ANY COST
```

---

# 55. F37 — Revalidation Failure

Examples:

```text
repair accepted without testing

old validator reused after regime change

dependent conclusions not recomputed

only repaired component tested

cross-scale effects ignored
```

Repair remains incomplete until required revalidation succeeds.

---

# 56. F38 — Observability Failure

Some failures may exist but be undetectable with current instrumentation.

```text
FAILURE_EXISTS
AND
DETECTOR_UNAVAILABLE
```

must remain possible.

Therefore:

```text
NO DETECTED FAILURE
!=
NO FAILURE
```

---

# 57. F39 — Adversarial / Deceptive Input Failure

Examples:

```text
spoofed sensor input

fabricated source

provenance forgery

replay attack

selective evidence presentation

maliciously malformed data

Sybil evidence

adversarially induced ambiguity
```

Response may require:

```text
QUARANTINE

INDEPENDENT VERIFICATION

SOURCE IDENTITY CHECK

PROVENANCE ROOT CHECK

AUTHORITY ESCALATION
```

---

# 58. F40 — Unknown / Unclassified Failure

When evidence establishes that something is wrong but the class is unresolved:

```text
failure_class:
  UNKNOWN
```

The system must not fabricate a cause.

```text
UNKNOWN ROOT CAUSE
!=
NO ROOT CAUSE
```

---

# 59. Severity Model

```yaml
severity:

  INFO:
    definition:
      anomaly with no demonstrated decision effect

  LOW:
    definition:
      bounded degradation with easy recovery

  MODERATE:
    definition:
      material observation quality degradation

  HIGH:
    definition:
      trusted downstream conclusions may be affected

  CRITICAL:
    definition:
      integrity, authority, safety, or irreversible
      downstream effects may be compromised

  UNKNOWN:
    definition:
      severity cannot yet be established
```

Severity must be evidence-based.

It must not be inferred solely from dramatic appearance.

---

# 60. Failure Impact Tensor

```text
T_Impact[
  failure,
  epistemic_impact,
  operational_impact,
  scope,
  HML_scale,
  reversibility,
  downstream_fanout,
  authority_impact,
  safety_impact,
  persistence_impact
]
```

---

# 61. Recoverability Tensor

```text
T_Recovery[
  failure,
  target,
  repairability,
  reobservability,
  rollback_available,
  alternative_channel,
  evidence_needed,
  cost,
  delay,
  residual_uncertainty
]
```

---

# 62. H/M/L Applicability

## L — Local

Examples:

```text
one sensor reading

one API call

one image frame

one measurement

one parsed field

one timestamp
```

## M — Subsystem

Examples:

```text
sensor array

retrieval subsystem

multimodal observation pipeline

measurement workflow

provenance subsystem
```

## H — System

Examples:

```text
global environment model

system-wide observation architecture

shared evidence layer

cross-agent sensing state

governed cognitive state
```

---

# 63. H/M/L Propagation Rule

A local failure propagates upward only through demonstrated dependencies.

```text
L failure
→
M impact
```

only when the M state depends materially on that L observation.

Likewise:

```text
M failure
→
H impact
```

requires a load-bearing dependency.

Hard boundary:

```text
LOCAL FAILURE
!=
SYSTEM FAILURE
```

---

# 64. Cross-Scale Failure Tensor

```text
T_HML_F[
  failure_id,
  origin_scale,
  affected_scale,
  propagation_edge,
  load_bearing,
  aggregation_dependency,
  confidence,
  containment
]
```

---

# 65. Control-Plane Requirements

The control plane must be able to represent:

```text
failure identity

failure class

affected observation

affected dependency edges

scope

regime

authority state

provenance

severity

containment state

repair state

revalidation state
```

Mandatory governance functions:

```text
detect

classify

quarantine

block unsafe promotion

trace dependency

invalidate selectively

authorize repair

revalidate

restore

preserve history
```

---

# 66. Fail-Closed Conditions

Trusted use should fail closed when any load-bearing field is unresolved:

```text
authority UNKNOWN

provenance critically missing

target identity unresolved

scope incompatible

regime incompatible

critical timestamp unknown

hard validator failed

critical conflict unresolved
```

Fail closed does not necessarily mean delete.

Preferred state is often:

```text
QUARANTINE
```

or:

```text
UNKNOWN/GAP
```

---

# 67. Agents

Candidate logical roles:

```text
SENSOR_AGENT

OBSERVATION_AGENT

MEASUREMENT_AGENT

PROVENANCE_AGENT

VALIDATION_AGENT

FAILURE_DETECTOR_AGENT

CONFLICT_AGENT

REOBSERVATION_AGENT

REPAIR_AGENT

AUDITOR_AGENT
```

These are architectural roles.

They are not claims that corresponding executable autonomous agents currently exist.

---

# 68. Agent Failure Contract

Each agent should expose:

```yaml
agent_failure_contract:

  agent_id:

  allowed_operations: []

  authority_scope:

  input_types: []

  output_types: []

  detectable_failures: []

  escalation_conditions: []

  quarantine_conditions: []

  validators: []

  provenance_requirements: []

  rollback_support:
```

---

# 69. Skills

Candidate relevant capability classes include:

```text
multimodal perception

sensory-map integration

semantic grounding

provenance auditing

confidence auditing

measurement integrity

information-boundary governance

risk/constraint governance

causal hierarchy checking

repair targeting

repair-harm auditing

context continuity

RSCF modeling
```

Skill invocation remains governed by:

```text
SKILL AVAILABLE
!=
SKILL VALID FOR THIS SCOPE

SKILL VALID
!=
SKILL AUTHORIZED

SKILL OUTPUT
!=
COMMITTED STATE
```

---

# 70. Workflows

Canonical failure workflow:

```text
OBSERVE
↓
VALIDATE
↓
DETECT ANOMALY
↓
CLASSIFY
↓
LOCALIZE
↓
TRACE DEPENDENCIES
↓
ASSESS SEVERITY
↓
CONTAIN
↓
SELECT REPAIR
↓
AUTHORIZE
↓
REPAIR
↓
REOBSERVE
↓
REVALIDATE
↓
RESTORE / QUARANTINE
```

---

# 71. Cheap Discriminating Evidence First

When several failure hypotheses compete:

```text
H1 sensor failure

H2 target change

H3 stale observation

H4 parsing failure

H5 provenance mismatch
```

the workflow should prefer the cheapest safe test capable of distinguishing them.

Conceptually:

```text
Test*
=
argmax(
  expected_discrimination
  /
  cost_risk_delay
)
```

This is an `AMOS_MODEL` decision heuristic.

---

# 72. Protocols

Failure protocol payload:

```yaml
L01FailureMessage:

  protocol_version:

  failure_id:

  observation_id:

  failure_class:

  severity:

  detected_at:

  origin:

  affected_scope:

  affected_regime:

  affected_dependencies: []

  provenance:

  uncertainty:

  containment_state:

  proposed_repair:

  authority_required:

  revalidation_required:

  falsifiers: []
```

---

# 73. Protocol Invariants

```text
failure messages preserve provenance

failure messages preserve observation identity

failure messages preserve failure status

repair proposals are explicitly proposals

commit receipts are explicit

duplicate/replayed messages are detectable

version mismatches are surfaced

UNKNOWN fields remain UNKNOWN
```

---

# 74. Evidence / Provenance

Every material failure claim should carry:

```yaml
FailureEvidence:

  claim:

  claim_class:

  observation:

  failure_signal:

  source:

  root_source:

  detection_method:

  event_time:

  detection_time:

  scope:

  regime:

  dependencies:

  independent_confirmation:

  competing_explanations:

  uncertainty:

  falsifiers:

  confidence_ceiling:
```

---

# 75. Failure Provenance Graph

```text
Observation
↓
AnomalySignal
↓
FailureCandidate
↓
Classification
↓
Containment
↓
RepairProposal
↓
RepairExecution
↓
Reobservation
↓
Revalidation
```

Each edge should remain traceable.

---

# 76. Competing Failure Hypotheses

Example:

```yaml
competing:

  H1:
    claim: sensor malfunction
    status: CONDITIONAL

  H2:
    claim: environment genuinely changed
    status: CONDITIONAL

  H3:
    claim: parsing/normalization corruption
    status: CONDITIONAL

  H4:
    claim: stale observation
    status: CONDITIONAL
```

Do not force convergence until discriminating evidence exists.

---

# 77. Confidence Ceiling

For failure conclusion `F`:

```text
Conf(F)
<=
min(
  anomaly_evidence,
  localization_evidence,
  provenance_integrity,
  scope_validity,
  regime_validity,
  causal_support
)
```

where those dimensions are load-bearing.

A high-confidence anomaly does not imply high-confidence root cause.

Example:

```text
Conf(failure_exists) = high

Conf(root_cause = sensor) = low
```

These must remain separate.

---

# 78. Uncertainty Vector

Material failure analysis should distinguish:

```text
U_evidence

U_model

U_scope

U_temporal

U_causal

U_execution

U_provenance_independence

U_repair
```

Do not collapse these dimensions unless a justified aggregation model exists.

---

# 79. Premature Closure Failure

A special metacognitive failure occurs when:

```text
one plausible explanation
→
accepted root cause
```

without testing alternatives.

Detection:

```text
missing competing hypotheses

missing falsifier

missing discriminating test

confidence exceeds evidence
```

Response:

```text
DOWNGRADE

REVISE

ESCALATE

UNKNOWN/GAP
```

---

# 80. Hidden-Assumption Failure

Examples:

```text
assuming sensor health

assuming source independence

assuming current freshness

assuming unchanged regime

assuming scope equivalence

assuming calibration

assuming target identity
```

Every load-bearing hidden assumption should either be:

```text
validated

made explicit

or converted to uncertainty
```

---

# 81. Contradiction Suppression Failure

Occurs when conflicting observations are silently reconciled.

Correct response:

```text
PRESERVE CONTRADICTION

CHECK SCOPE

CHECK TIME

CHECK REGIME

CHECK PROVENANCE

CHECK METHOD

SEEK DISCRIMINATING EVIDENCE
```

---

# 82. Failure Propagation

Let:

```text
G_D = dependency graph
```

For failed premise `p`:

```text
Affected(p)
=
load-bearing descendants(p)
```

Then:

```text
Invalid(p)
→
Invalidate(Affected(p))
```

Independent branches remain valid.

---

# 83. Selective Invalidation

Example:

```text
Observation O1 fails
│
├── Claim C1 depends on O1 → invalidate
├── Claim C2 depends on O1 → invalidate
└── Claim C3 depends only on O2 → preserve
```

This prevents both contamination and unnecessary recomputation.

---

# 84. Failure Containment States

```text
NONE

MONITOR

RESTRICT_USE

DOWNGRADE

QUARANTINE

SUSPEND_WORKFLOW

BLOCK_COMMIT

REVOKE_TRUST

ESCALATE
```

Containment strength should track actual risk and dependency impact.

---

# 85. Repair / Recovery

Canonical recovery sequence:

```text
DETECT
↓
PRESERVE EVIDENCE
↓
LOCALIZE
↓
CLASSIFY
↓
CONTAIN
↓
TRACE DEPENDENCIES
↓
IDENTIFY MINIMAL REPAIR TARGET
↓
CHECK REPAIR AUTHORITY
↓
APPLY REPAIR
↓
REOBSERVE
↓
REVALIDATE
↓
CHECK REGRESSION
↓
RESTORE TRUSTED USE
```

---

# 86. Minimal Repair Principle

Repair should target the smallest causal component supported by evidence.

```text
MINIMAL CAUSAL REPAIR
>
GLOBAL RESET
```

when local repair is sufficient.

This preserves unaffected valid state.

---

# 87. Repair Must Not Hide Evidence

Prohibited repair:

```text
delete contradiction

overwrite failure trace

replace UNKNOWN with guessed value

rewrite historical observation

remove provenance

change expected result to match output
```

Repair should preserve failure history.

---

# 88. Reobservation After Repair

Where the failure affected acquisition:

```text
REPAIR
→
REOBSERVE
```

A repaired sensor does not retroactively validate its prior measurements.

---

# 89. Revalidation After Repair

Required checks may include:

```text
target identity

sensor/tool health

schema

units

time

freshness

scope

regime

provenance

dependency closure

confidence ceiling

authority
```

---

# 90. Rollback

If repair worsens the state:

```text
ROLLBACK
→
nearest known valid configuration
```

Rollback must preserve:

```text
failure evidence

repair attempt

version lineage

affected outputs
```

---

# 91. Failed Repair

If repair does not restore validity:

```text
REPAIR_FAILED
```

Then:

```text
DO NOT repeat identical repair
```

unless evidence or conditions changed.

Possible next states:

```text
ALTERNATIVE_REPAIR

ESCALATE

QUARANTINE

UNKNOWN/GAP
```

---

# 92. Recovery Without Root Cause

Some failures may be operationally recoverable without definitive root-cause identification.

Example:

```text
channel A failed
→
authorized independent channel B succeeds
```

This may restore observation capability while root cause remains:

```text
UNKNOWN
```

Do not falsely promote operational recovery to causal explanation.

---

# 93. Tests / Validators

Minimum validator set:

```text
VALIDATOR_TARGET_IDENTITY

VALIDATOR_ACCESS

VALIDATOR_SENSOR_HEALTH

VALIDATOR_CHANNEL

VALIDATOR_ACQUISITION_COMPLETENESS

VALIDATOR_SCHEMA

VALIDATOR_TYPES

VALIDATOR_UNITS

VALIDATOR_TIMESTAMP

VALIDATOR_FRESHNESS

VALIDATOR_SCOPE

VALIDATOR_REGIME

VALIDATOR_RESOLUTION

VALIDATOR_PROVENANCE

VALIDATOR_SOURCE_IDENTITY

VALIDATOR_INDEPENDENCE

VALIDATOR_QUALITY

VALIDATOR_UNCERTAINTY

VALIDATOR_FUSION

VALIDATOR_CONFLICT

VALIDATOR_EPISTEMIC_CLASS

VALIDATOR_CAUSAL_FIREWALL

VALIDATOR_AUTHORITY

VALIDATOR_COMMIT

VALIDATOR_DEPENDENCY_GRAPH

VALIDATOR_HML_PROPAGATION

VALIDATOR_REPAIR

VALIDATOR_REVALIDATION
```

---

# 94. Minimum Failure Tests

```text
TEST_F001
sensor failure does not become negative observation

TEST_F002
retrieval failure does not become source nonexistence

TEST_F003
missing value does not become zero

TEST_F004
UNKNOWN does not become false

TEST_F005
stale evidence triggers freshness handling

TEST_F006
scope mismatch prevents unrestricted reuse

TEST_F007
regime mismatch triggers revalidation

TEST_F008
unit mismatch fails

TEST_F009
type mismatch fails

TEST_F010
prediction cannot become observation

TEST_F011
simulation cannot become reality state

TEST_F012
memory retrieval cannot become current observation

TEST_F013
source claim cannot become verified observation automatically

TEST_F014
shared ancestry reduces claimed independence

TEST_F015
conflicting evidence remains COMPETING when unresolved

TEST_F016
local failure invalidates only dependent conclusions

TEST_F017
independent conclusions survive unrelated failure

TEST_F018
repair preserves historical failure evidence

TEST_F019
repair requires revalidation

TEST_F020
failed repair is not automatically repeated

TEST_F021
capability does not imply authority

TEST_F022
proposal does not imply commit

TEST_F023
critical UNKNOWN cannot pass

TEST_F024
no detected failure does not prove no failure

TEST_F025
root-cause confidence cannot exceed supporting evidence

TEST_F026
quarantine does not delete source evidence

TEST_F027
reobservation creates new observation identity

TEST_F028
regime-dependent descendants invalidate after regime change

TEST_F029
adversarial provenance mismatch triggers quarantine

TEST_F030
failure detector itself can return UNKNOWN
```

---

# 95. Validator Output

```yaml
FailureValidationResult:

  validator_id:

  target:

  status:
    - PASS
    - FAIL
    - UNKNOWN

  failure_candidates: []

  affected_dependencies: []

  evidence: []

  provenance: []

  uncertainty:

  recommended_action:

  confidence_ceiling:
```

---

# 96. Meta-Validation

Failure detectors themselves may fail.

Therefore:

```text
DetectorResult
```

must not be assumed infallible.

Meta-checks include:

```text
detector version

detector scope

detector regime

detector provenance

false-positive evidence

false-negative evidence

coverage

calibration where applicable
```

---

# 97. Falsifiers

This failure architecture is materially falsified or requires revision if authoritative canon or validated implementation establishes that:

```text
L01 has materially different primitive boundaries

sensing failure is governed entirely outside L01

observation provenance is not an L01 responsibility

failure propagation does not follow dependency structure

H/M/L is not applicable to L01

repair/reobservation belongs to a different primitive

the proposed taxonomy contradicts direct source canon

critical failure classes cannot be typed coherently

failure state cannot preserve provenance

selective invalidation cannot preserve integrity

the proposed failure lifecycle is incompatible with runtime semantics
```

---

# 98. Runtime Falsifiers

An implementation violates this contract if it:

```text
turns failed observation into absence

turns UNKNOWN into PASS

turns missing into zero

turns retrieval failure into nonexistence

turns sensor failure into environmental conclusion

hides stale evidence

drops scope

drops regime

drops provenance

inflates independent-source count

silently resolves contradiction

allows unauthorized repair

allows proposal to become commit

accepts stale reads at commit

globally invalidates unrelated state

repairs without revalidation

rewrites historical observations

deletes failure evidence

repeats failed repair without changed evidence

claims causal root cause from anomaly alone
```

---

# 99. Gap Status

```yaml
gap_status:

  critical:

    - direct authoritative exhaustive L01 failure-mode canon has not been conclusively recovered

    - executable L01 failure detector implementation has not been established

    - runtime mappings from failure classes to actual AMOS components remain unresolved

    - empirical false-positive and false-negative rates are unavailable

    - operational severity thresholds are not validated

  decision_relevant:

    - exact failure severity scoring remains undefined

    - exact recovery-cost function remains undefined

    - exact modality-specific failure detectors remain undefined

    - exact sensor-health models remain domain dependent

    - exact reobservation thresholds remain domain dependent

    - exact H/M/L propagation rules require runtime dependency mappings

    - exact commit-time behavior requires implementation evidence

  explanatory:

    - some failure classes may overlap in real systems

    - domain-specific subclasses may be required

    - probabilistic failure diagnosis may be useful

    - adversarial sensing requires deeper threat-specific models

  cosmetic:

    - failure numbering

    - naming conventions

    - severity labels

    - diagram formatting
```

---

# 100. Failure Registry

```yaml
failure_registry:

  F01:
    name: TARGET_ENVIRONMENT_FAILURE

  F02:
    name: ACCESS_ADDRESSABILITY_FAILURE

  F03:
    name: SENSOR_TOOL_FAILURE

  F04:
    name: CHANNEL_MODALITY_FAILURE

  F05:
    name: ACQUISITION_FAILURE

  F06:
    name: SAMPLING_COVERAGE_FAILURE

  F07:
    name: MEASUREMENT_FAILURE

  F08:
    name: CALIBRATION_FAILURE

  F09:
    name: TYPING_SCHEMA_FAILURE

  F10:
    name: UNIT_SCALE_FAILURE

  F11:
    name: NORMALIZATION_TRANSFORMATION_FAILURE

  F12:
    name: TEMPORAL_FAILURE

  F13:
    name: FRESHNESS_FAILURE

  F14:
    name: SCOPE_FAILURE

  F15:
    name: REGIME_FAILURE

  F16:
    name: RESOLUTION_FAILURE

  F17:
    name: PROVENANCE_FAILURE

  F18:
    name: SOURCE_IDENTITY_FAILURE

  F19:
    name: INDEPENDENCE_SYBIL_FAILURE

  F20:
    name: QUALITY_FAILURE

  F21:
    name: UNCERTAINTY_FAILURE

  F22:
    name: FUSION_FAILURE

  F23:
    name: CONFLICT_FAILURE

  F24:
    name: EPISTEMIC_CLASSIFICATION_FAILURE

  F25:
    name: CAUSAL_OVERREACH_FAILURE

  F26:
    name: AGENT_FAILURE

  F27:
    name: SKILL_FAILURE

  F28:
    name: WORKFLOW_FAILURE

  F29:
    name: PROTOCOL_FAILURE

  F30:
    name: CONTROL_PLANE_FAILURE

  F31:
    name: AUTHORITY_FAILURE

  F32:
    name: TRANSACTION_COMMIT_FAILURE

  F33:
    name: MEMORY_PERSISTENCE_FAILURE

  F34:
    name: HML_SCALE_FAILURE

  F35:
    name: DEPENDENCY_INVALIDATION_FAILURE

  F36:
    name: REPAIR_FAILURE

  F37:
    name: REVALIDATION_FAILURE

  F38:
    name: OBSERVABILITY_FAILURE

  F39:
    name: ADVERSARIAL_DECEPTIVE_INPUT_FAILURE

  F40:
    name: UNKNOWN_UNCLASSIFIED_FAILURE
```

---

# 101. RSCF Completion State

```yaml
rscf:

  claim:
    L01_SENSING_OBSERVATION requires an explicit failure
    architecture capable of distinguishing failures of
    sensing, access, measurement, provenance, scope, regime,
    validation, governance, and downstream dependency use
    without converting observation failure into unsupported
    claims about reality.

  claim_class:
    AMOS_MODEL

  evidence:
    - supplied L01 failure-mode placeholder
    - supplied L01 definition architecture
    - supplied L01 dependency architecture
    - supplied L01 equation architecture
    - supplied L01 control-plane architecture
    - supplied L01 agent architecture
    - L00 reality/environment architecture
    - AMOS RSCF architecture
    - AMOS provenance principles
    - AMOS metacognitive confidence principles
    - AMOS selective invalidation principles

  provenance:
    origin_architect: Trang Phan
    architecture_family: AMOS
    primitive: L01_SENSING_OBSERVATION
    artifact: FAILURE_MODES.md
    reconstruction_status: MODEL_DERIVED
    direct_failure_canon_status: GAP_BOUNDED

  scope:
    AMOS_OS/COGNITIVE_MATRIX/L01_SENSING_OBSERVATION/FAILURE_MODES

  regime:
    governed sensing / observation / measurement architecture

  freshness:
    revalidate_when:
      - direct L01 failure canon is recovered
      - L01 primitive boundaries change
      - observation schema changes
      - provenance architecture changes
      - control-plane semantics change
      - H/M/L dependency structure changes
      - runtime implementation becomes available
      - empirical failure evidence becomes available

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
    - L01 DEPENDENCIES
    - L01 CONTROL_PLANES
    - L01 AGENTS
    - L01 SKILLS
    - L01 WORKFLOWS
    - L01 PROTOCOLS
    - L01 PROVENANCE
    - L01 MEMORY
    - L01 RSCF
    - L01 REPAIR
    - L01 TESTS

  competing:
    - sensor-specific failure taxonomies
    - probabilistic fault diagnosis
    - Bayesian fault localization
    - anomaly-detection architectures
    - reliability-engineering taxonomies
    - observability/incident-management models
    - modality-specific error architectures

  falsifiers:
    - authoritative canon defines materially different failure boundaries
    - L01 does not own sensing failure semantics
    - failure classes cannot be mapped to typed states
    - provenance cannot be preserved across failure handling
    - selective invalidation is incompatible with runtime dependency semantics
    - H/M/L failure propagation is unsupported by the architecture

  confidence_ceiling:
    structural failure architecture only;
    direct exhaustive canon,
    executable detectors,
    empirical detector accuracy,
    calibrated severity thresholds,
    runtime dependency mappings,
    and operational recovery evidence remain unresolved
```

---

# 102. Completion State

```yaml
completion_state:

  source_canon_references:
    status: PARTIAL / GAP_BOUNDED

  definition_and_scope:
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
    status: MODEL_COMPLETE

  falsifiers:
    status: MODEL_COMPLETE

  gap_status:
    status: EXPLICIT

  direct_source_failure_canon:
    status: GAP

  executable_failure_detection:
    status: GAP

  empirical_validation:
    status: GAP

  operational_runtime_validation:
    status: GAP

  conclusion_class:
    AMOS_MODEL / CONDITIONAL
```

---

# 103. Hard Boundaries

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

L01 adds the following sensing-specific boundaries:

```text
REALITY
!=
OBSERVATION

OBSERVATION
!=
INTERPRETATION

OBSERVATION
!=
INFERENCE

MEASUREMENT
!=
GROUND_TRUTH

SOURCE_CLAIM
!=
VERIFIED_FACT

PREDICTION
!=
OBSERVATION

SIMULATION
!=
REALITY

MEMORY
!=
CURRENT_OBSERVATION

MISSING
!=
ZERO

UNKNOWN
!=
FALSE

NOT_OBSERVED
!=
OBSERVED_ABSENT

SENSOR_FAILURE
!=
ENVIRONMENT_FAILURE

RETRIEVAL_FAILURE
!=
NONEXISTENCE

DETECTED_ANOMALY
!=
ROOT_CAUSE

REPAIR
!=
REVALIDATION

NO_DETECTED_FAILURE
!=
NO_FAILURE
```

---

# 104. Final Failure Contract

The core L01 failure relation is:

```text
ENVIRONMENT
↓
SENSING
↓
OBSERVATION
↓
VALIDATION
↓
ADMISSION
```

with failure branches possible at every stage:

```text
ENVIRONMENT
├── target failure
├── access failure
│
SENSING
├── sensor failure
├── channel failure
├── acquisition failure
├── sampling failure
│
OBSERVATION
├── measurement failure
├── calibration failure
├── type failure
├── unit failure
├── transformation failure
├── temporal failure
├── freshness failure
├── scope failure
├── regime failure
├── resolution failure
│
EVIDENCE
├── provenance failure
├── identity failure
├── independence failure
├── quality failure
├── uncertainty failure
├── fusion failure
├── conflict failure
├── epistemic-class failure
├── causal-overreach failure
│
EXECUTION
├── agent failure
├── Skill failure
├── workflow failure
├── protocol failure
├── control-plane failure
├── authority failure
├── commit failure
├── memory failure
├── H/M/L failure
└── dependency failure
```

Recovery is:

```text
FAILURE
↓
DETECT
↓
CLASSIFY
↓
LOCALIZE
↓
PRESERVE EVIDENCE
↓
TRACE DEPENDENCIES
↓
CONTAIN
↓
REPAIR
↓
REOBSERVE
↓
REVALIDATE
↓
RESTORE
```

with the central invariant:

```text
FAILURE
DOES NOT AUTHORIZE FABRICATION
```

If observation cannot be recovered:

```text
UNKNOWN/GAP
```

must remain available as a valid terminal epistemic state.

If root cause cannot be established:

```text
ROOT_CAUSE = UNKNOWN
```

must be preserved even when operational recovery succeeds.

If contradictory observations remain comparably supported:

```text
COMPETING
```

must be preserved.

If one premise fails:

```text
INVALIDATE ONLY ITS LOAD-BEARING DESCENDANTS
```

unless broader dependency evidence establishes wider impact.

Until direct authoritative L01 failure canon, executable failure detectors, empirical detector performance, calibrated severity thresholds, and operational runtime validation are established, the strongest warranted classification remains:

```text
AMOS_MODEL / CONDITIONAL
```

---

**Related:** [[L01_SENSING_OBSERVATION]] · [[L01_SENSING_OBSERVATION — Definition]] · [[L01_SENSING_OBSERVATION — Purpose]] · [[L01_SENSING_OBSERVATION — Variables]] · [[L01_SENSING_OBSERVATION — State]] · [[L01_SENSING_OBSERVATION — Operators]] · [[L01_SENSING_OBSERVATION — Invariants]] · [[L01_SENSING_OBSERVATION — Equations]] · [[L01_SENSING_OBSERVATION — HML]] · [[L01_SENSING_OBSERVATION — Dependencies]] · [[L01_SENSING_OBSERVATION — Control Planes]] · [[L01_SENSING_OBSERVATION — Agents]] · [[L01_SENSING_OBSERVATION — Skills]] · [[L01_SENSING_OBSERVATION — Workflows]] · [[L01_SENSING_OBSERVATION — Protocols]] · [[L01_SENSING_OBSERVATION — Provenance]] · [[L01_SENSING_OBSERVATION — Memory]] · [[L01_SENSING_OBSERVATION — RSCF]] · [[L01_SENSING_OBSERVATION — Repair]] · [[L01_SENSING_OBSERVATION — Tests]] · [[L01_SENSING_OBSERVATION — Gap Matrix]] · [[L00_REALITY_ENVIRONMENT]] · [[00-Home]] · [[06-Knowledge-Base-MOC]]

```
```

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[COGNITIVE_MATRIX_MOC]] · [[00-Home]] · [[AMOS_RSCF_NODES]]
