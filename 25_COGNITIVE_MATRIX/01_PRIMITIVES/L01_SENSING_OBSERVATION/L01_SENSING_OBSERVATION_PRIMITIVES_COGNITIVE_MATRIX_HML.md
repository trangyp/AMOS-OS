---
tags:
  - amos
  - cognitive-matrix
  - l01
  - sensing-observation
  - hml
  - cross-scale
  - observation
  - provenance
  - rscf
  - control-plane
---

# L01_SENSING_OBSERVATION — HML

**Class:** `COGNITIVE_PRIMITIVE_HML_CONTRACT`  
**Origin architect / steward:** Trang Phan  
**Architecture:** `AMOS_OS / COGNITIVE_MATRIX`  
**Primitive:** `L01_SENSING_OBSERVATION`  
**Artifact:** `HML.md`  
**Role:** `H/M/L SENSING / OBSERVATION SCALE CONTRACT`  
**Status:** `AMOS_MODEL / SOURCE-CANON BOUNDED / UNVALIDATED`

> **Epistemic boundary:** this document defines the proposed H/M/L contract for `L01_SENSING_OBSERVATION`. H/M/L is used as an AMOS multiscale reasoning architecture. It does not establish that every empirical sensing system naturally decomposes into exactly three levels, nor that aggregation across those levels preserves meaning, identity, causality, or completeness.

---

# 0. Purpose

`L01_SENSING_OBSERVATION/HML.md` defines how sensing and observation are represented across AMOS High / Medium / Low (`H/M/L`) scales.

The contract governs:

```text
L — atomic/local observation
M — subsystem/composite observation
H — system/environment observation
```

and the transformations:

```text
L → M
M → H

H → M
M → L
```

while preserving:

```text
scope
regime
time
observer
provenance
uncertainty
resolution
heterogeneity
epistemic class
```

The central objective is to prevent:

```text
LOCAL OBSERVATION
→
UNJUSTIFIED GLOBAL CLAIM
```

and:

```text
SYSTEM-LEVEL EXPECTATION
→
FABRICATED LOCAL OBSERVATION
```

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
  - AMOS H/M/L
  - AMOS RSCF
```

## 1.2 Relevant AMOS Source Families

Relevant architectural source families include:

```text
AMOS_CORE lineage

AMOS Full Brain OS

AMOS Cognition architecture

AMOS Cross-Scale RSCF structures

AMOS typed tensor architecture

AMOS provenance architecture

AMOS control-plane architecture

AMOS Reality / Environment architecture

L00_REALITY_ENVIRONMENT

L01_SENSING_OBSERVATION sibling contracts
```

## 1.3 Source Classification

The following distinction is mandatory:

```text
DIRECT SOURCE CANON
!=
AMOS MODEL RECONSTRUCTION
```

This H/M/L contract is therefore classified:

```yaml
source_status:

  HML_principle:
    class: AMOS_MODEL / CORPUS_ALIGNED

  exact_L01_HML_mapping:
    class: AMOS_MODEL

  canonical_L01_scale_boundaries:
    class: UNKNOWN/GAP

  executable_HML_runtime:
    class: UNKNOWN/GAP

  empirical_validation:
    class: UNKNOWN/GAP
```

No proposed L01-specific H/M/L equation in this artifact should be promoted to `SOURCE_CANON` without direct source evidence.

---

# 2. Definition

`L01_SENSING_OBSERVATION` H/M/L is a typed multiscale observation architecture in which observations are represented at different resolutions without assuming that information can be losslessly or causally transferred between them.

Define the scale set:

[
\boxed{
S = {H,M,L}
}
]

where:

```text
H = system / environment / governing observational scale

M = subsystem / composite / regional observational scale

L = atomic / local / event / channel observational scale
```

These labels are relational.

They do not imply fixed physical size.

A subsystem may be `H` relative to its own components while being `M` or `L` relative to a larger system.

---

# 3. Scope

This contract applies to multiscale handling of:

```text
sensor observations

tool observations

environment measurements

human reports

machine observations

multimodal observations

distributed observations

temporal observations

spatial observations

subsystem observations

system-level observational summaries
```

It governs how evidence moves between scales.

It does **not** by itself define:

```text
physical sensor hardware

domain-specific measurement theory

statistical estimator validity

causal inference

semantic interpretation

world-model construction

memory truth

authority to act
```

---

# 4. Core H/M/L Law

The core relation is:

[
\boxed{
O_L
\rightarrow
O_M
\rightarrow
O_H
}
]

only when valid aggregation mappings exist.

The reverse relation:

[
\boxed{
C_H
\rightarrow
C_M
\rightarrow
C_L
}
]

represents constraints, expectations, query scopes, or observational requirements flowing downward.

It does **not** mean that high-level state manufactures lower-level evidence.

Therefore:

```text
UPWARD AGGREGATION
!=
IDENTITY

DOWNWARD CONSTRAINT
!=
DOWNWARD CAUSATION

MACRO EXPECTATION
!=
MICRO OBSERVATION
```

---

# 5. H/M/L Observation Tensor

Define:

[
\boxed{
O[s,t,r,o,f]
}
]

where:

```text
s = H/M/L scale

t = time

r = regime

o = observer / observation source

f = observed feature / field
```

Extended L01 representation:

[
\boxed{
T_{OBS}^{L01}
=============

T[
scale,
target,
feature,
value,
unit,
time,
location,
resolution,
scope,
regime,
observer,
source,
method,
provenance,
quality,
uncertainty,
freshness,
validation
]
}
]

Every decision-relevant tensor cell should remain bound to an RSCF evidence node.

---

# 6. Typed Inputs

```yaml
HMLObservationInput:

  target:
    type: EntityRef

  requested_scale:
    type: H | M | L

  feature:
    type: ObservableRef

  source:
    type: SourceRef | SensorRef | ToolRef | AgentRef

  time:
    type: TimeEnvelope

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeRef | UNKNOWN

  observer:
    type: ObserverRef

  resolution:
    type: ResolutionEnvelope

  provenance:
    type: ProvenanceRef

  authority:
    type: AuthorityContext

  uncertainty:
    type: UncertaintyVector | UNKNOWN
```

---

# 7. Typed Outputs

```yaml
HMLObservationOutput:

  observation_id:
    type: ObservationRef

  scale:
    type: H | M | L

  target:
    type: EntityRef

  value:
    type: TypedValue

  epistemic_class:
    type:
      - OBSERVATION
      - DERIVED
      - MODEL
      - UNKNOWN

  source_scale:
    type: H | M | L

  transformation:
    type: TransformationRef | NONE

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeRef | UNKNOWN

  time:
    type: TimeEnvelope

  resolution:
    type: ResolutionEnvelope

  provenance:
    type: ProvenanceBundle

  uncertainty:
    type: UncertaintyVector

  confidence_ceiling:
    type: ConfidenceCeiling

  validation_state:
    type:
      - UNVALIDATED
      - CONDITIONAL
      - VALIDATED_FOR_SCOPE
      - QUARANTINED
      - REJECTED
```

---

# 8. State Variables

```text
O_L = local observation state

O_M = subsystem observation state

O_H = system observation state

A_LM = L→M aggregation operator

A_MH = M→H aggregation operator

C_HM = H→M constraint operator

C_ML = M→L constraint operator

R_s = resolution at scale s

U_s = uncertainty at scale s

P_s = provenance state at scale s

Q_s = quality state at scale s

F_s = freshness state at scale s

G_s = regime at scale s

S_s = scope envelope at scale s

V_s = validation state at scale s

X_s = observation coverage at scale s

D_s = dependency state at scale s
```

---

# 9. Low Scale — L

`L` represents the smallest observation unit currently relevant to the reasoning task.

Examples may include:

```text
single sensor reading

single API response

single detected event

single timestamped measurement

single field observation

single document statement

single image region observation

single local subsystem state
```

Canonical conceptual form:

[
\boxed{
O_L
===

(value,
feature,
target,
time,
source,
method,
scope,
provenance,
uncertainty)
}
]

An L observation should remain local unless an explicit transformation licenses promotion.

---

# 10. L-Level Invariants

```text
L01-L-INV-01
A local observation retains its source identity.

L01-L-INV-02
A local observation retains its timestamp.

L01-L-INV-03
A local observation retains its measurement method where material.

L01-L-INV-04
A local observation does not imply subsystem coverage.

L01-L-INV-05
A local observation does not imply system coverage.

L01-L-INV-06
Missing local observation is not evidence of local absence unless coverage licenses that inference.

L01-L-INV-07
Local correlation does not establish higher-scale causation.
```

---

# 11. Medium Scale — M

`M` represents an observational state composed from or referring to a subsystem, region, cluster, modality group, or intermediate structure.

Examples:

```text
sensor-array state

regional environmental state

multimodal observation bundle

service subsystem state

machine subsystem state

department-level observation

time-window observation summary
```

Conceptual form:

[
\boxed{
O_M
===

A_{L\rightarrow M}
(
O_{L,1},...,O_{L,n}
)
}
]

provided aggregation is admissible.

---

# 12. M-Level Requirements

Before L observations may form M state, check:

```text
target compatibility

scope compatibility

time compatibility

regime compatibility

unit compatibility

coordinate compatibility

resolution compatibility

measurement-method compatibility

provenance compatibility

coverage sufficiency

dependency structure

uncertainty propagation
```

---

# 13. M-Level Invariants

```text
L01-M-INV-01
M-level state identifies its contributing L evidence.

L01-M-INV-02
Aggregation preserves provenance lineage.

L01-M-INV-03
Aggregation does not convert DERIVED into OBSERVATION.

L01-M-INV-04
Heterogeneous L states remain visible when decision-relevant.

L01-M-INV-05
Conflicting L evidence cannot be silently averaged away.

L01-M-INV-06
M confidence cannot exceed load-bearing evidence without independent validation.

L01-M-INV-07
M scope cannot silently exceed contributing evidence coverage.
```

---

# 14. High Scale — H

`H` represents system-level, environment-level, governing, population-level, or global observational state relative to the declared analysis.

Examples:

```text
overall environment state

system health state

population-level observation

enterprise state

whole-machine state

global sensing summary

high-level situational picture
```

Conceptual form:

[
\boxed{
O_H
===

A_{M\rightarrow H}
(
O_{M,1},...,O_{M,k}
)
}
]

subject to admissibility.

---

# 15. H-Level Invariants

```text
L01-H-INV-01
H-level state preserves the scope of supporting evidence.

L01-H-INV-02
H-level summaries do not erase decision-relevant subsystem heterogeneity.

L01-H-INV-03
H-level stability may coexist with M/L instability.

L01-H-INV-04
H-level observations cannot be treated as complete merely because aggregation succeeded.

L01-H-INV-05
H-level claims inherit provenance and uncertainty from load-bearing M/L evidence.

L01-H-INV-06
H-level claims remain regime bounded.

L01-H-INV-07
H-level conclusions must expose incomplete coverage when material.
```

---

# 16. Upward Aggregation

The generic AMOS multiscale structure is:

[
\boxed{
O_M=A_{L\rightarrow M}(O_L)
}
]

[
\boxed{
O_H=A_{M\rightarrow H}(O_M)
}
]

where each (A) is typed.

An aggregation operator should bind:

```text
input scales

output scale

method

coverage assumptions

weights

scope

regime

time

provenance

uncertainty transform

validation state
```

---

# 17. Aggregation Is a Transformation

If:

[
O_M=A_{L\rightarrow M}(O_L)
]

then generally:

```text
O_M.class = DERIVED
```

unless `O_M` is independently observed at M scale.

Similarly:

[
O_H=A_{M\rightarrow H}(O_M)
]

generally yields:

```text
O_H.class = DERIVED
```

not:

```text
OBSERVATION
```

merely because its inputs were observations.

---

# 18. Direct vs Derived Scale Observation

AMOS must distinguish:

```text
DIRECT_H_OBSERVATION

DERIVED_H_FROM_M

DIRECT_M_OBSERVATION

DERIVED_M_FROM_L

DIRECT_L_OBSERVATION
```

Example:

```yaml
observation:

  value: X

  scale: H

  epistemic_class: DERIVED

  derived_from:
    - M_001
    - M_002

  transform:
    A_M_TO_H_01
```

This distinction is mandatory.

---

# 19. Downward Constraint

The generic downward AMOS structure is:

[
\boxed{
O'_M
====

C_{H\rightarrow M}(O_H,O_M)
}
]

[
\boxed{
O'_L
====

C_{M\rightarrow L}(O'_M,O_L)
}
]

For L01, `C` should normally be interpreted as:

```text
observation requirement

query restriction

expected domain

measurement constraint

validation constraint

attention allocation

sampling instruction
```

not as fabricated evidence.

---

# 20. Downward Constraint Invariant

A high-level expectation may request:

```text
"inspect subsystem M"
```

but cannot generate:

```text
"subsystem M was observed to have value X"
```

without observation.

Therefore:

[
\boxed{
Constraint_H
\not\Rightarrow
Observation_L
}
]

---

# 21. Cross-Scale General Update

A general AMOS MODEL representation is:

[
\boxed{
\Delta O_s(t+1)
===============

\sum_q
T_{q\rightarrow s}\Delta O_q(t)
+
u_s
---

d_s
}
]

where:

```text
s = target scale

q = contributing scale

T_q→s = typed cross-scale transform

u_s = newly acquired observation contribution

d_s = invalidated / decayed / revoked contribution
```

This equation is an AMOS structural model, not a universal empirical law of sensing.

---

# 22. Cross-Scale Transformation Tensor

[
\boxed{
T_{HML}
=======

T[
source_scale,
target_scale,
operator,
scope,
regime,
time,
resolution,
coverage,
provenance,
uncertainty,
validation
]
}
]

A transformation is admissible only if its required dimensions are compatible.

---

# 23. Scale Translation Contract

```yaml
ScaleTransform:

  transform_id:

  source_scale:
    H | M | L

  target_scale:
    H | M | L

  operator:

  source_nodes: []

  scope:

  regime:

  time:

  coverage:

  resolution:

  assumptions: []

  provenance:

  uncertainty_transform:

  output_class:

  validators: []

  falsifiers: []
```

---

# 24. Scope Propagation

If evidence has scope (S_L), aggregation must not silently produce broader scope (S_H).

[
\boxed{
Scope(O_H)
\subseteq
LicensedScope(Evidence)
}
]

unless independent evidence justifies expansion.

Hard boundary:

```text
OBSERVED SAMPLE
!=
UNOBSERVED POPULATION
```

---

# 25. Regime Propagation

Each scale state inherits regime applicability.

```text
normal operation

degraded operation

stress regime

transition regime

unknown regime
```

If supporting evidence comes from incompatible regimes:

```text
DO NOT AUTO-AGGREGATE
```

unless the transformation explicitly models regime differences.

---

# 26. Temporal Alignment

For cross-scale aggregation:

[
\boxed{
CompatibleTime(O_i,O_j)
}
]

must hold to the degree required by the domain.

Potential temporal states:

```text
SIMULTANEOUS

ALIGNED_WINDOW

LAGGED

STALE

ASYNCHRONOUS

UNKNOWN
```

Asynchronous observations must not be presented as simultaneous state without a valid temporal model.

---

# 27. Resolution Compatibility

Higher-scale summaries often compress lower-scale resolution.

Define:

[
R_L \rightarrow R_M \rightarrow R_H
]

but:

```text
LOWER RESOLUTION
!=
LOWER TRUTH

HIGHER RESOLUTION
!=
HIGHER SYSTEM COVERAGE
```

Resolution and coverage are distinct variables.

---

# 28. Coverage

Define conceptual coverage:

[
\boxed{
Cov_s
=====

\frac{
ObservedRelevantRegion_s
}{
DeclaredRelevantRegion_s
}
}
]

only when numerator and denominator are operationally definable.

Otherwise:

```text
coverage = UNKNOWN
```

Do not invent a percentage.

---

# 29. Coverage Invariant

[
\boxed{
Unobserved
\neq
Absent
}
]

unless observation design guarantees detection.

At every scale:

```text
MISSING DATA
!=
NEGATIVE EVIDENCE
```

without a detection/coverage model.

---

# 30. Heterogeneity Preservation

Suppose:

```text
L1 = high

L2 = high

L3 = low

L4 = critical failure
```

An M summary:

```text
average = moderate
```

may conceal the decision-relevant `L4` failure.

Therefore:

[
\boxed{
Aggregate
\neq
PermissionToEraseCriticalVariation
}
]

---

# 31. Cross-Scale Exception Channel

Every aggregation should support:

```text
dominant summary

exceptions

outliers

critical local failures

unknown regions

conflicts
```

Example:

```yaml
M_state:

  summary:
    nominal

  exceptions:
    - L_004:
        state: CRITICAL

  coverage:
    partial

  confidence:
    conditional
```

---

# 32. Macro Stability / Local Collapse

Mandatory invariant:

```text
MACRO STABILITY
MAY COEXIST WITH
LOCAL COLLAPSE
```

Therefore:

[
Stable(O_H)
\not\Rightarrow
\forall l,\ Stable(O_l)
]

This is a structural logical safeguard.

---

# 33. Local Failure / Macro Stability

Conversely:

[
Failure(O_l)
\not\Rightarrow
Failure(O_H)
]

unless the local node is load-bearing for the high-scale state.

Dependency topology determines propagation.

---

# 34. Cross-Scale Causal Firewall

Observation propagation must not become causal inference.

From:

```text
L changes

then M changes

then H changes
```

AMOS may record:

```text
temporal association
```

but not automatically:

```text
L caused H
```

Causal promotion requires separately typed causal evidence.

---

# 35. Downward Causal Firewall

Likewise:

```text
H-level policy changed

L-level state later changed
```

does not by itself establish:

```text
H caused L
```

Possible alternatives include:

```text
common cause

mediator

confounder

independent environmental change

measurement change

selection effect
```

---

# 36. Provenance Across Scales

Each cross-scale state should preserve ancestry.

Example:

```text
H_01
├── M_01
│   ├── L_01
│   └── L_02
└── M_02
    ├── L_03
    └── L_04
```

This allows downstream claims to recover their evidence lineage.

---

# 37. Provenance Tensor

[
\boxed{
P_{HML}
=======

T[
node,
scale,
source,
parent,
root,
method,
transform,
time,
scope,
regime,
version
]
}
]

---

# 38. Provenance Independence

If:

```text
L1

L2

L3
```

all descend from the same source root, they do not provide three independent confirmations.

Therefore:

[
\boxed{
IndependentSupport
\neq
Count(Observations)
}
]

Ancestry must be checked before confidence aggregation.

---

# 39. Uncertainty Vector

At each scale:

[
\boxed{
U_s
===

(
U_e,
U_m,
U_s,
U_t,
U_c,
U_x,
U_p
)
}
]

where:

```text
U_e = evidence uncertainty

U_m = model / transformation uncertainty

U_s = scope uncertainty

U_t = temporal uncertainty

U_c = causal uncertainty

U_x = execution uncertainty

U_p = provenance-independence uncertainty
```

---

# 40. Uncertainty Propagation

For derived M/H states:

```text
output uncertainty
```

must include uncertainty introduced by:

```text
input evidence

aggregation

missing coverage

cross-scale transformation

regime mismatch

time mismatch

resolution loss

provenance correlation
```

Therefore:

```text
AGGREGATION
DOES NOT
AUTOMATICALLY REDUCE UNCERTAINTY
```

---

# 41. Confidence Ceiling

For a derived cross-scale conclusion (C):

[
\boxed{
Conf(C)
\le
\min_{p\in LB(C)} Conf(p)
}
]

unless an independent validation path provides stronger evidence.

This prevents aggregation itself from manufacturing confidence.

---

# 42. Cross-Scale RSCF Node

```yaml
RSCFNode:

  id:

  type:
    SOURCE_CLAIM | OBSERVATION | DERIVED | MODEL | DECISION | UNKNOWN

  HML:
    H | M | L

  claim:

  scope:

  regime:

  time:

  observer:

  provenance:

  confidence:

  falsifier:

  status:
```

Every decision-relevant H/M/L state should map to such a node.

---

# 43. Cross-Scale RSCF Edge

```yaml
RSCFEdge:

  from:

  to:

  transform_type:
    AGGREGATES
    CONSTRAINS
    SUPPORTS
    CONTRADICTS
    INVALIDATES
    REFINES

  source_scale:

  target_scale:

  assumptions: []

  scope:

  regime:

  provenance:

  validation:
```

---

# 44. Dependency Model

Core dependencies:

```text
L00_REALITY_ENVIRONMENT

L01 Definition

L01 Variables

L01 State

L01 Operators

L01 Equations

L01 Invariants

L01 Dependencies

L01 Control Planes

L01 Agents

L01 Skills

L01 Workflows

L01 Protocols

L01 Provenance

L01 RSCF

L01 Failure Modes

L01 Repair

L01 Tests
```

Cross-architecture dependencies may include:

```text
AMOS RSCF

AMOS provenance topology

AMOS cross-scale tensor architecture

AMOS constraint propagation

AMOS uncertainty governance

AMOS control plane
```

---

# 45. L00 Dependency

L01 observations require a declared observation environment.

Conceptually:

```text
L00
↓
defines observable environment / target boundary
↓
L01
performs sensing / observation
```

L01 must not silently redefine reality/environment state merely because an observation conflicts with expectation.

---

# 46. H/M/L Dependency Closure

Before scale promotion:

```text
source evidence available

source scale known

target scale known

aggregation method defined

scope compatible

regime compatible

time compatible

provenance preserved

uncertainty propagated

critical contradictions surfaced
```

If not:

```text
PROMOTION = CONDITIONAL
```

or:

```text
PROMOTION = UNKNOWN/GAP
```

---

# 47. Control-Plane Requirements

The control plane should govern:

```text
which scale may be queried

which sensors/tools may be used

who may perform aggregation

which transformations are allowed

which state may be persisted

which state may be promoted

which state requires revalidation

which state must be quarantined
```

---

# 48. Control-Plane Tensor

[
\boxed{
CP_{HML}
========

T[
actor,
capability,
authority,
source_scale,
target_scale,
operation,
scope,
regime,
time,
constraints,
commit_state
]
}
]

---

# 49. Capability / Authority Boundary

An agent may have technical capability to aggregate:

```text
L → M
```

without authority to commit the resulting M state.

Therefore:

```text
CAN_AGGREGATE
!=
MAY_COMMIT
```

and:

```text
CAPABILITY
!=
AUTHORITY
```

---

# 50. Proposal / Commit Boundary

Cross-scale output should pass:

```text
OBSERVE
↓
TRANSFORM
↓
PROPOSE
↓
VALIDATE
↓
AUTHORIZE
↓
COMMIT
```

not:

```text
TRANSFORM
↓
COMMIT
```

---

# 51. Commit-Time Revalidation

Before durable H/M/L state admission, validate:

```text
source still valid

scope still compatible

regime still compatible

authority still valid

provenance still intact

dependencies still fresh

critical contradictions unresolved?
```

If a load-bearing premise changed:

```text
FAIL CLOSED
```

or return:

```text
REVALIDATE
```

---

# 52. Agents

Candidate architectural roles:

```text
HML Observation Coordinator

L-Level Acquisition Agent

M-Level Aggregation Agent

H-Level Synthesis Agent

Cross-Scale Validator

Provenance Agent

Conflict Agent

Coverage Agent

Reobservation Agent

Repair Agent
```

These are roles.

```text
ROLE
!=
IMPLEMENTED AGENT
```

---

# 53. HML Observation Coordinator

Responsibilities:

```text
determine requested scale

decompose observation need

select appropriate evidence scale

prevent unnecessary scale expansion

route aggregation

preserve dependency lineage
```

---

# 54. L-Level Acquisition Agent

Responsibilities:

```text
acquire local observations

bind source identity

bind timestamps

bind measurement method

bind provenance

report uncertainty

avoid unsupported aggregation
```

---

# 55. M-Level Aggregation Agent

Responsibilities:

```text
validate L compatibility

aggregate only admissible inputs

preserve exceptions

preserve provenance

propagate uncertainty

mark output DERIVED where applicable
```

---

# 56. H-Level Synthesis Agent

Responsibilities:

```text
compose M states

preserve subsystem heterogeneity

expose coverage

identify critical exceptions

avoid false global completeness

produce system-level synthesis
```

---

# 57. Cross-Scale Validator

Checks:

```text
scale typing

scope compatibility

regime compatibility

temporal alignment

coverage

provenance ancestry

uncertainty propagation

epistemic-class preservation

critical exception preservation
```

---

# 58. Skills

Candidate relevant Skill capabilities:

```text
cross-scale reasoning

typed tensor modeling

RSCF construction

provenance validation

scope/regime validation

constraint propagation

uncertainty auditing

system completion auditing

repair auditing
```

Skill invocation must not imply authority.

---

# 59. Skill Contract

```yaml
HMLSkillBinding:

  skill_id:

  role:

  input_scales: []

  output_scales: []

  permitted_transforms: []

  scope:

  regime:

  authority_requirement:

  validators: []

  failure_behavior:

  provenance_behavior:
```

---

# 60. Workflow — Bottom-Up Observation

```text
DEFINE TARGET
↓
ACQUIRE L OBSERVATIONS
↓
TYPE / PROVENANCE-BIND
↓
VALIDATE L
↓
CHECK COVERAGE
↓
CHECK COMPATIBILITY
↓
AGGREGATE L → M
↓
PRESERVE EXCEPTIONS
↓
VALIDATE M
↓
AGGREGATE M → H
↓
PRESERVE HETEROGENEITY
↓
VALIDATE H
↓
PROPOSE
↓
COMMIT IF AUTHORIZED
```

---

# 61. Workflow — Top-Down Observation Planning

```text
DEFINE H QUESTION
↓
DECOMPOSE H → M OBSERVATION REQUIREMENTS
↓
DECOMPOSE M → L REQUIREMENTS
↓
ALLOCATE SENSORS / TOOLS
↓
ACQUIRE L EVIDENCE
↓
RETURN UPWARD THROUGH VALIDATED TRANSFORMS
```

Important:

```text
TOP-DOWN PLANNING
!=
TOP-DOWN EVIDENCE GENERATION
```

---

# 62. Workflow — Cross-Scale Conflict

```text
DETECT H/M/L INCONSISTENCY
↓
CHECK TIME
↓
CHECK SCOPE
↓
CHECK REGIME
↓
CHECK RESOLUTION
↓
CHECK COVERAGE
↓
CHECK PROVENANCE
↓
CHECK TRANSFORMATION
↓
PRESERVE COMPETING STATES
↓
IDENTIFY CHEAPEST DISCRIMINATING OBSERVATION
↓
REOBSERVE
↓
REVALIDATE
```

---

# 63. Workflow — Selective Invalidation

```text
PREMISE FAILS
↓
LOCATE RSCF NODE
↓
TRACE DEPENDENT H/M/L EDGES
↓
INVALIDATE DEPENDENTS
↓
PRESERVE UNAFFECTED NODES
↓
REOBSERVE MINIMUM REQUIRED REGION
↓
RECOMPUTE ONLY AFFECTED TRANSFORMS
```

---

# 64. Protocols

Candidate messages:

```text
HMLObservationRequest

LocalObservationRecord

ScaleAggregationRequest

ScaleAggregationResult

CrossScaleValidationRequest

CrossScaleValidationResult

CoverageReport

ScaleConflictReport

ReobservationRequest

ScaleInvalidationEvent

HMLCommitProposal

HMLCommitDecision
```

---

# 65. Protocol Example

```yaml
ScaleAggregationRequest:

  request_id:

  source_scale:
    L

  target_scale:
    M

  source_observations: []

  operator:

  target_scope:

  target_regime:

  target_time:

  required_coverage:

  provenance_refs: []

  authority_context:

  validation_requirements: []
```

---

# 66. Evidence / Provenance

Every scale transformation should preserve:

```text
source observations

source roots

transformation operator

agent/tool identity

time

scope

regime

version

validation result

uncertainty transform
```

Derived H/M/L state without recoverable ancestry should be treated as degraded evidence.

---

# 67. Evidence Classes

Allowed epistemic classes:

```text
SOURCE_CLAIM

OBSERVATION

DERIVED

MODEL

DECISION

UNKNOWN
```

Scale does not change epistemic class automatically.

Examples:

```text
H OBSERVATION

H DERIVED

H MODEL

M OBSERVATION

M DERIVED

L OBSERVATION
```

are distinct.

---

# 68. Direct Observation Invariant

If an H-level measurement directly observes an H-level quantity:

```text
class = OBSERVATION
```

may be valid.

But if H state is computed from M/L evidence:

```text
class = DERIVED
```

unless independently observed.

---

# 69. Competing Cross-Scale States

AMOS must preserve:

```text
HYPOTHESIS_A:
local anomaly only

HYPOTHESIS_B:
subsystem degradation

HYPOTHESIS_C:
system-wide regime change

HYPOTHESIS_D:
measurement artifact
```

until discriminating evidence exists.

Do not force convergence because one hypothesis is narratively cleaner.

---

# 70. Sensitivity Flip Set

For conclusion (c):

[
\boxed{
F_c
===

{
p\mid
plausible\ change\ in\ p
\ flips\ c
}
}
]

For H/M/L observation, likely flip premises include:

```text
coverage threshold

critical local observation

source reliability

time alignment

regime classification

aggregation method

provenance independence

outlier treatment
```

Test these before accumulating redundant evidence.

---

# 71. Failure Modes

## FM-HML-01 — Scale Collapse

Different scales are merged into one undifferentiated state.

Example:

```text
L observation
=
H conclusion
```

without transformation.

---

## FM-HML-02 — Local-to-Global Overreach

```text
one local observation
→
whole system claim
```

without coverage.

---

## FM-HML-03 — Ecological Inference Error

Group/system-level observation is incorrectly applied to individual/local state.

---

## FM-HML-04 — Aggregation Masking

Critical local variation disappears inside averages or summaries.

---

## FM-HML-05 — Provenance Loss

Derived M/H state cannot recover contributing evidence.

---

## FM-HML-06 — Regime Mixing

Evidence from incompatible regimes is aggregated as one state.

---

## FM-HML-07 — Temporal Mixing

Observations from materially different times are represented as simultaneous.

---

## FM-HML-08 — Resolution Confusion

High measurement precision is mistaken for broad coverage.

---

## FM-HML-09 — Confidence Inflation

Aggregation creates higher confidence without independent support.

---

## FM-HML-10 — Downward Fabrication

High-level expectation becomes alleged low-level evidence.

---

## FM-HML-11 — False Independence

Multiple observations derived from one source are counted as independent.

---

## FM-HML-12 — Cross-Scale Causal Overreach

Scale association is promoted to causation.

---

## FM-HML-13 — Over-Invalidation

One local failure causes the entire H state to be discarded despite limited dependency.

---

## FM-HML-14 — Under-Invalidation

A load-bearing local failure does not invalidate dependent M/H state.

---

## FM-HML-15 — Unknown-to-Pass

Missing scale evidence is treated as normal state.

---

# 72. Failure Detection Tensor

[
\boxed{
F_{HML}
=======

T[
failure_id,
scale,
source_scale,
target_scale,
affected_nodes,
severity,
dependency_fanout,
detectability,
repairability,
status
]
}
]

---

# 73. Repair / Recovery

General recovery:

```text
DETECT
↓
LOCALIZE SCALE
↓
IDENTIFY FAILED PREMISE / TRANSFORM
↓
QUARANTINE AFFECTED STATE
↓
TRACE DEPENDENCIES
↓
INVALIDATE ONLY DEPENDENTS
↓
PRESERVE UNAFFECTED STATE
↓
REOBSERVE / RECOMPUTE
↓
REVALIDATE
↓
RESTORE
```

---

# 74. Scale Repair Invariant

Repair should target the smallest causal failure region.

```text
LOCAL FAILURE
→
LOCAL REPAIR FIRST
```

unless dependency fanout requires broader recovery.

Global recomputation is a last resort.

---

# 75. Repair Examples

### Bad aggregation

```text
invalidate aggregation operator
↓
preserve source observations
↓
apply corrected transform
↓
revalidate M/H
```

### Stale L evidence

```text
invalidate stale L nodes
↓
reobserve affected target
↓
recompute dependent M
↓
recompute dependent H only if necessary
```

### Provenance corruption

```text
quarantine affected ancestry branch
↓
recover source lineage
↓
revalidate dependent nodes
```

---

# 76. Validators

```text
VALIDATOR_HML_SCALE_TYPE

VALIDATOR_HML_SCOPE

VALIDATOR_HML_REGIME

VALIDATOR_HML_TIME

VALIDATOR_HML_RESOLUTION

VALIDATOR_HML_COVERAGE

VALIDATOR_HML_PROVENANCE

VALIDATOR_HML_INDEPENDENCE

VALIDATOR_HML_UNCERTAINTY

VALIDATOR_HML_EPISTEMIC_CLASS

VALIDATOR_HML_AGGREGATION

VALIDATOR_HML_EXCEPTION_PRESERVATION

VALIDATOR_HML_AUTHORITY

VALIDATOR_HML_DEPENDENCY_CLOSURE
```

---

# 77. Minimum Tests

```text
TEST_HML_001
L observation cannot become H observation merely through relabeling

TEST_HML_002
L→M aggregation produces DERIVED state unless M is independently observed

TEST_HML_003
M→H aggregation preserves contributing provenance

TEST_HML_004
critical L exception survives M aggregation

TEST_HML_005
critical M exception survives H aggregation

TEST_HML_006
H stability does not imply every L node is stable

TEST_HML_007
one L failure does not invalidate unrelated H state

TEST_HML_008
load-bearing L failure invalidates dependent M/H state

TEST_HML_009
incompatible regimes block automatic aggregation

TEST_HML_010
materially asynchronous observations cannot masquerade as simultaneous

TEST_HML_011
shared provenance ancestry blocks false independence

TEST_HML_012
missing coverage remains UNKNOWN rather than PASS

TEST_HML_013
downward constraint cannot create an observation

TEST_HML_014
aggregation cannot increase confidence solely by transformation

TEST_HML_015
cross-scale correlation cannot be labeled causal without causal evidence

TEST_HML_016
selective invalidation preserves unaffected evidence

TEST_HML_017
scope expansion requires explicit support

TEST_HML_018
resolution and coverage remain distinct

TEST_HML_019
proposal cannot become commit without authority

TEST_HML_020
unknown transform validity blocks validated promotion
```

---

# 78. Adversarial Tests

Test against:

```text
single anomalous L value dominating H incorrectly

critical L value hidden by averaging

duplicated source presented as independent sensors

stale L data mixed with current M data

different regimes combined

different units combined

simulated L data presented as observed

retrieved memory presented as current L observation

H expectation injected into L evidence

authority revoked before commit

source revoked after H aggregation

partial coverage presented as full coverage
```

---

# 79. Falsifiers

This H/M/L contract must be revised if:

```text
direct AMOS canon defines materially different L01 H/M/L semantics

L01 is canonically defined without H/M/L applicability

canonical scale boundaries differ materially

source evidence establishes different aggregation rules

runtime implementation uses incompatible state semantics

tests show proposed invariants are internally inconsistent

a proposed transformation cannot preserve required provenance or scope

domain evidence demonstrates an assumed scale mapping is invalid
```

---

# 80. Gap Matrix

```yaml
HML_gap_status:

  direct_source_canon:
    status: GAP
    criticality: CRITICAL

  exact_L01_HML_boundaries:
    status: GAP
    criticality: CRITICAL

  HML_structural_model:
    status: COMPLETE_FOR_MODEL_SCOPE
    criticality: NONE

  typed_inputs_outputs:
    status: MODEL_COMPLETE

  state_variables:
    status: MODEL_COMPLETE

  upward_aggregation:
    status: MODEL_COMPLETE

  downward_constraint:
    status: MODEL_COMPLETE

  scope_propagation:
    status: MODEL_COMPLETE

  regime_propagation:
    status: MODEL_COMPLETE

  provenance_propagation:
    status: MODEL_COMPLETE

  uncertainty_propagation:
    status: MODEL_PARTIAL

  calibrated_aggregation_rules:
    status: GAP

  coverage_thresholds:
    status: GAP

  temporal_alignment_thresholds:
    status: GAP

  resolution_compatibility_rules:
    status: GAP

  runtime_control_plane:
    status: GAP

  executable_agents:
    status: GAP

  executable_skills:
    status: GAP

  executable_workflows:
    status: GAP

  executable_protocols:
    status: GAP

  validators:
    status: MODEL_ONLY

  executed_tests:
    status: GAP

  empirical_validation:
    status: GAP

  operational_validation:
    status: GAP
```

---

# 81. Gap Priority

Current highest-priority gaps:

```text
1. Confirm direct canonical L01 H/M/L definition.

2. Confirm exact H/M/L boundaries for sensing/observation.

3. Resolve L00 → L01 → downstream scale interfaces.

4. Establish canonical aggregation operators.

5. Establish coverage semantics.

6. Establish scope/regime compatibility rules.

7. Establish executable provenance-preserving transforms.

8. Establish control-plane authority rules.

9. Implement validators.

10. Execute H/M/L adversarial and regression tests.
```

---

# 82. Hard Boundaries

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

Additional L01 H/M/L boundaries:

```text
LOCAL
!=
GLOBAL

AGGREGATED
!=
OBSERVED

SUMMARY
!=
COMPLETE COVERAGE

PRECISION
!=
COVERAGE

DOWNWARD CONSTRAINT
!=
DOWNWARD CAUSATION

CORRELATION ACROSS SCALE
!=
CAUSATION

MULTIPLE OBSERVATIONS
!=
INDEPENDENT EVIDENCE

MACRO STABILITY
!=
LOCAL STABILITY

LOCAL FAILURE
!=
GLOBAL FAILURE

UNOBSERVED
!=
ABSENT

MODEL
!=
REALITY
```

---

# 83. RSCF Completion State

```yaml
rscf:

  claim:
    L01_SENSING_OBSERVATION can be represented as an H/M/L
    multiscale observation architecture in which local evidence,
    subsystem synthesis, and system-level synthesis remain typed,
    provenance-bound, scope/regime bounded, and protected against
    unjustified cross-scale promotion.

  claim_class:
    MODEL

  evidence:
    - supplied L01 HML placeholder
    - AMOS H/M/L reasoning architecture
    - AMOS cross-scale tensor architecture
    - AMOS RSCF architecture
    - AMOS provenance principles
    - related L01 structural contracts

  provenance:
    origin_architect: Trang Phan
    architecture_family: AMOS
    primitive: L01_SENSING_OBSERVATION
    artifact: HML.md
    reconstruction_status: MODEL_DERIVED
    direct_L01_canon_status: GAP

  scope:
    AMOS_OS/COGNITIVE_MATRIX/L01_SENSING_OBSERVATION/HML

  regime:
    architecture specification / multiscale observation modeling

  freshness:
    revalidate_when:
      - direct L01 canon becomes available
      - L01 scale boundaries change
      - L00 interface changes
      - downstream primitive topology changes
      - H/M/L canon changes
      - executable runtime becomes available
      - empirical validation becomes available

  dependencies:
    - L00_REALITY_ENVIRONMENT
    - L01_DEFINITION
    - L01_VARIABLES
    - L01_STATE
    - L01_OPERATORS
    - L01_EQUATIONS
    - L01_INVARIANTS
    - L01_DEPENDENCIES
    - L01_CONTROL_PLANES
    - L01_AGENTS
    - L01_SKILLS
    - L01_WORKFLOWS
    - L01_PROTOCOLS
    - L01_PROVENANCE
    - L01_RSCF
    - L01_FAILURE_MODES
    - L01_REPAIR
    - L01_TESTS

  competing:
    - direct AMOS canon may define different L01 scale boundaries
    - some M-level operations may belong to later perception/representation primitives
    - some domains may require more than three operational resolution levels
    - domain-specific sensing architectures may require different aggregation semantics

  falsifiers:
    - direct canon materially contradicts this H/M/L mapping
    - dependency analysis places aggregation outside L01
    - executable tests violate required invariants
    - proposed scale transforms cannot preserve scope/provenance
    - domain-specific validation disproves an assumed aggregation rule

  uncertainty:
    evidence: medium_high
    model: medium
    scope: medium
    temporal: medium
    causal: high_for_cross_scale_causal_claims
    execution: high
    provenance_independence: medium_high

  confidence_ceiling:
    structural AMOS MODEL only;
    not source-canon-complete,
    not runtime-validated,
    not empirically universal
```

---

# 84. Completion State

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

# 85. Final Contract

`L01_SENSING_OBSERVATION/HML.md` defines a multiscale sensing and observation architecture in which:

```text
L
=
local / atomic evidence

M
=
subsystem / composite observational state

H
=
system / environment observational state
```

with controlled upward transformation:

[
\boxed{
O_L
\xrightarrow{A_{L\rightarrow M}}
O_M
\xrightarrow{A_{M\rightarrow H}}
O_H
}
]

and controlled downward observational constraint:

[
\boxed{
C_H
\rightarrow
C_M
\rightarrow
C_L
}
]

subject to the decisive invariants:

```text
aggregation does not prove identity

aggregation does not create observation status

macro stability may coexist with local collapse

local failure does not automatically imply global failure

local correlation does not establish macro causation

downward constraint does not establish downward causation

heterogeneity survives when decision-relevant

scope/regime/observer envelopes propagate

provenance survives scale transformation

unknown remains unknown

confidence cannot be manufactured by aggregation
```

The strongest warranted status is therefore:

```text
L01 H/M/L STRUCTURAL CONTRACT
=
AMOS_MODEL
+
PROVENANCE-BOUND
+
CROSS-SCALE GUARDED
+
SOURCE-CANON BOUNDED
+
RUNTIME UNVALIDATED
+
EMPIRICALLY UNVALIDATED
```

Accordingly:

```text
COMPLETE_FOR_DECLARED_MODEL_SCOPE
!=
IMPLEMENTED

IMPLEMENTED
!=
VALIDATED

VALIDATED_FOR_ONE_SCOPE
!=
UNIVERSALLY VALID
```

---

**Related:** [[L01_SENSING_OBSERVATION]] · [[L01_SENSING_OBSERVATION — Definition]] · [[L01_SENSING_OBSERVATION — Variables]] · [[L01_SENSING_OBSERVATION — Equations]] · [[L01_SENSING_OBSERVATION — Dependencies]] · [[L01_SENSING_OBSERVATION — Control Planes]] · [[L01_SENSING_OBSERVATION — Agents]] · [[L01_SENSING_OBSERVATION — Skills]] · [[L01_SENSING_OBSERVATION — Workflows]] · [[L01_SENSING_OBSERVATION — Protocols]] · [[L01_SENSING_OBSERVATION — Provenance]] · [[L01_SENSING_OBSERVATION — Failure Modes]] · [[L01_SENSING_OBSERVATION — Repair]] · [[L01_SENSING_OBSERVATION — Gap Matrix]] · [[L00_REALITY_ENVIRONMENT]] · [[00-Home]] · [[06-Knowledge-Base-MOC]]

```
```

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[COGNITIVE_MATRIX_MOC]] · [[00-Home]]
