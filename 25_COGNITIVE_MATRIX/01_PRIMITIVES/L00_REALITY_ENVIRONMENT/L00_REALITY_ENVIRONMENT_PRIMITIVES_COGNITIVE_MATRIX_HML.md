---
title: "L00_REALITY_ENVIRONMENT — H/M/L Architecture"
aliases:

* "AMOS Reality Environment HML"
* "L00 Reality HML"
* "Reality Environment Cross-Scale Architecture"
  canon-type: architecture
  rscf-class: MODEL
  rscf-state: conditional
  amos-layer: L00_REALITY_ENVIRONMENT
  architecture-role: hierarchical-cross-scale-reality-reasoning
  origin-architect: "Trang Phan"
  status: "ARCHITECTURE CONTRACT / IMPLEMENTATION-DEPENDENT"
  tags:
* amos
* reality-environment
* hml
* cross-scale
* hierarchy
* reality-contact
* observation
* evidence
* provenance
* scope
* regime
* control-plane
* rscf/D-distinction
* rscf/G-relation
* rscf/C-constraint
* rscf/B-boundary
* rscf/M-memory
* rscf/S-state
* rscf/T-topology
* rscf/X-cross-scale
* rscf/type-model
tags: ['cognitive_matrix', 'primitives', 'l00_reality_environment', 'note']

---
# L00_REALITY_ENVIRONMENT — H/M/L Architecture

**Class:** `AMOS_REALITY_ENVIRONMENT_CROSS_SCALE_ARCHITECTURE`
**Origin architect / steward:** Trang Phan
**Status:** `ARCHITECTURE CONTRACT / IMPLEMENTATION-DEPENDENT`

---

# 1. Purpose

`L00_REALITY_ENVIRONMENT / HML` defines how AMOS represents, reasons across, validates, and governs reality-related state at three coupled resolutions:

```text
H = HIGH / SYSTEM / GOVERNING SCALE
M = MIDDLE / SUBSYSTEM / RELATIONAL SCALE
L = LOW / LOCAL / OBSERVATION SCALE
```

The H/M/L architecture exists to prevent AMOS from collapsing:

```text
local observation
subsystem state
system-level conclusion
```

into a single undifferentiated representation.

Its governing principle is:

[
\boxed{
LocalEvidence
\neq
SubsystemState
\neq
SystemState
}
]

while allowing explicitly typed transformations between them.

---

# 2. H/M/L Is a Resolution Architecture

H/M/L does not mean that reality literally contains exactly three ontological layers.

It is an AMOS reasoning architecture for representing multiple resolutions.

Therefore:

```text
H/M/L = MODELING RESOLUTION

H/M/L != UNIVERSAL ONTOLOGICAL PROOF
```

The same object may occupy different H/M/L roles depending on the declared analysis boundary.

---

# 3. Relative Scale Principle

Scale is relational.

For system (S):

[
\boxed{
H(S),M(S),L(S)
}
]

must be defined relative to the current system boundary.

Example:

```text
SYSTEM: autonomous AI platform

H:
  platform governance
  system objectives
  authority
  deployment environment

M:
  planner
  memory
  retrieval
  policy engine
  tool subsystem

L:
  individual observation
  retrieved document
  tool response
  state variable
  claim
```

A subsystem that is `M` in one analysis may become `H` when analyzed independently.

---

# 4. Core H/M/L State Tensor

The L00 reality state is represented conceptually as:

[
\boxed{
X[h,m,l,t,r,o,f]
}
]

where:

```text
h = high-level/system coordinate
m = middle-level/subsystem coordinate
l = low-level/local coordinate
t = time
r = regime/environment
o = observer or observation context
f = state field
```

For provenance-sensitive reasoning:

[
\boxed{
X[h,m,l,t,r,o,f,p]
}
]

where:

```text
p = provenance / evidence lineage
```

---

# 5. Extended Reality H/M/L Tensor

For L00:

[
\boxed{
T_{HML}^{Reality}
=================

T[
object,
H_state,
M_state,
L_state,
time,
regime,
observer,
representation_class,
measurement,
provenance,
confidence,
uncertainty,
boundary,
consequence
]
}
]

---

# 6. Representation Classes

Every reality-bearing H/M/L state should distinguish where applicable:

```text
OBSERVED_REALITY
MEASURED_PROXY
MODEL_STATE
SIMULATION
COUNTERFACTUAL
SYNTHETIC_DATA
DIGITAL_TWIN
FORECAST
DEPLOYED_OUTCOME
UNKNOWN
```

Hard invariant:

```text
REPRESENTATION CLASS MUST SURVIVE SCALE TRANSFORMATION
```

A simulation at `L` cannot become observed reality merely because it is aggregated into `H`.

---

# 7. H — High Scale

`H` represents the governing or system-scale state.

Typical L00-H objects include:

```text
system boundary
environment
global operating regime
system objective
authority structure
system-wide constraints
deployment state
aggregate risk
global provenance requirements
system-level reality model
system-level decision state
```

H answers:

```text
What system are we reasoning about?

What environment contains it?

What governs the system?

What global constraints apply?

What system-level conclusion is justified?

What system-wide consequences matter?
```

---

# 8. H-State Tensor

[
\boxed{
T_H
===

T[
system,
environment,
boundary,
global_state,
objective,
constraints,
authority,
regime,
time,
aggregate_evidence,
provenance,
uncertainty,
consequence
]
}
]

---

# 9. M — Middle Scale

`M` represents subsystem organization, interactions, mechanisms, interfaces, and relational structure.

Typical L00-M objects include:

```text
perception subsystem
memory subsystem
retrieval subsystem
reasoning subsystem
planning subsystem
tool subsystem
evidence subsystem
control plane
governance subsystem
environment interface
validation subsystem
repair subsystem
```

M answers:

```text
Which subsystem carries the state?

Which components interact?

Which relations connect local observations to system conclusions?

Which transformations are operating?

Where can evidence, state, authority, or uncertainty propagate?
```

---

# 10. M-State Tensor

[
\boxed{
T_M
===

T[
subsystem,
components,
relations,
state,
inputs,
outputs,
constraints,
interfaces,
dependencies,
regime,
time,
provenance,
uncertainty,
failure_state
]
}
]

---

# 11. L — Low Scale

`L` represents local observations, measurements, events, variables, claims, state transitions, and evidence objects.

Typical L00-L objects include:

```text
sensor observation
user input
tool result
retrieved document
individual claim
measurement
timestamp
state variable
event
action result
test result
validator result
```

L answers:

```text
What exactly was observed?

When was it observed?

How was it measured?

By whom or what?

What source produced it?

What representation class does it belong to?

What uncertainty attaches to it?
```

---

# 12. L-State Tensor

[
\boxed{
T_L
===

T[
observation,
variable,
value,
unit,
measurement,
timestamp,
observer,
source,
representation_class,
scope,
regime,
provenance,
confidence,
uncertainty
]
}
]

---

# 13. Core Cross-Scale Architecture

```text
             H
     SYSTEM / GOVERNANCE
              ▲
              │
       upward aggregation
              │
              │
              M
      SUBSYSTEM / RELATION
              ▲
              │
       upward aggregation
              │
              │
              L
     LOCAL / OBSERVATION
```

Downward:

```text
              H
              │
       constraints / policy
              ▼
              M
              │
       constraints / routing
              ▼
              L
```

These two directions must remain typed separately.

---

# 14. Upward Aggregation

Low-scale state may be aggregated into middle-scale state:

[
\boxed{
X_M
===

A_{L\rightarrow M}(X_L)
}
]

Middle-scale state may be aggregated into high-scale state:

[
\boxed{
X_H
===

A_{M\rightarrow H}(X_M)
}
]

where (A) is an explicitly declared aggregation operator.

---

# 15. Aggregation Invariant

[
\boxed{
Aggregate(X)
\neq
X
}
]

Aggregation creates a derived representation.

Therefore:

```text
LOCAL OBSERVATION != AGGREGATE STATE

AGGREGATE STATE != SOURCE OBSERVATION
```

---

# 16. Aggregation Does Not Prove Identity

Even when:

[
X_H=A_{M\rightarrow H}(X_M)
]

it does not follow that:

[
X_H \equiv X_M
]

Hard invariant:

```text
AGGREGATION != IDENTITY
```

---

# 17. Downward Constraint

High-scale state may constrain middle-scale admissible state:

[
\boxed{
X'_M
====

C_{H\rightarrow M}(X_H,X_M)
}
]

Middle-scale state may constrain low-scale admissible state:

[
\boxed{
X'_L
====

C_{M\rightarrow L}(X'_M,X_L)
}
]

Examples:

```text
system authority → subsystem permissions
system policy → tool restrictions
deployment regime → observation requirements
subsystem schema → admissible local state
```

---

# 18. Constraint Is Not Causation

Hard invariant:

[
\boxed{
DownwardConstraint
\neq
DownwardCausalEffect
}
]

A system rule restricting admissible subsystem states does not by itself prove a physical or empirical downward causal mechanism.

---

# 19. General Cross-Scale Update

A conceptual AMOS state update is:

[
\boxed{
\Delta X_s(t+1)
===============

\sum_q
T_{q\rightarrow s}
\Delta X_q(t)
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
T(q→s) = typed cross-scale transformation
u_s = admissible external/input update
d_s = degradation, loss, invalidation, or removal
```

This equation is an AMOS MODEL unless independently instantiated and validated in a domain.

---

# 20. Cross-Scale Transformation Tensor

[
\boxed{
T_{XScale}
==========

T[
source_scale,
target_scale,
operator,
input_type,
output_type,
scope,
regime,
time,
observer,
assumptions,
information_loss,
provenance,
validation,
confidence
]
}
]

---

# 21. Transformation Classes

Permitted cross-scale transformation classes include:

```text
AGGREGATE
DECOMPOSE
CONSTRAIN
ROUTE
PROPAGATE
SUMMARIZE
COMPRESS
EXPAND
NORMALIZE
MAP
TRANSLATE
INFER
VALIDATE
INVALIDATE
REPAIR
```

Each transformation must declare its semantics.

---

# 22. Typed Transformation Rule

A transformation is admissible only if:

[
\boxed{
Compatible(
Type_{source},
Operator,
Type_{target}
)
=

TRUE
}
]

Same field names do not prove semantic compatibility.

---

# 23. Cross-Scale Composition Gate

For:

[
X_L
\rightarrow
X_M
\rightarrow
X_H
]

composition requires:

[
\boxed{
TypeCompatible
\land
ScopeCompatible
\land
RegimeCompatible
\land
TemporalCompatible
\land
ProvenancePreserved
}
]

Otherwise:

```text
CROSS_SCALE_COMPOSITION = BLOCKED
```

---

# 24. Evidence Propagation

Evidence may support claims across scales only through explicit dependency paths.

[
\boxed{
E_L
\rightarrow
C_L
\rightarrow
C_M
\rightarrow
C_H
}
]

Each transition must carry:

```text
edge type
scope
regime
time
provenance
confidence
falsifier
```

---

# 25. RSCF H/M/L Node

Each material state used in a conclusion should bind to an RSCF node:

[
\boxed{
N
=

(
id,
type,
HML,
claim,
scope,
regime,
time,
observer,
provenance,
confidence,
falsifier,
status
)
}
]

Node classes:

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL
DECISION
UNKNOWN
```

---

# 26. RSCF Cross-Scale Edge

[
\boxed{
E
=

(
parent,
child,
edge_type,
load_bearing,
independence,
condition
)
}
]

Cross-scale edges must never be inferred merely because two nodes appear structurally similar.

---

# 27. Claim Tensor with H/M/L

[
\boxed{
T_C
===

T[
claim_id,
text,
class,
HML_scale,
premises,
evidence,
scope,
regime,
time,
observer,
causal_level,
provenance,
competing,
falsifiers,
confidence_ceiling
]
}
]

---

# 28. Evidence Tensor with H/M/L

[
\boxed{
T_E
===

T[
evidence_id,
source,
source_type,
HML_scale,
measurement,
timestamp,
scope,
regime,
observer,
ancestry,
independence,
quality,
freshness,
provenance,
revocation
]
}
]

---

# 29. Relation Tensor with H/M/L

[
\boxed{
R_{ij}
======

T[
source_scale,
target_scale,
type,
direction,
strength,
dependency,
confidence,
causal_status,
lag,
conflict,
provenance
]
}
]

Relation classes may include:

```text
semantic
dependency
causal
constraint
temporal
evidence
scale
governance
repair
analogy
contradiction
```

---

# 30. H/M/L Scope Envelope

Every cross-scale conclusion inherits an applicability envelope:

[
\boxed{
Envelope
========

System
\times
Environment
\times
Scale
\times
Time
\times
Regime
\times
Observer
\times
Measurement
}
]

Cross-scale reasoning outside this envelope requires revalidation.

---

# 31. Scale Translation Does Not Expand Scope Automatically

If:

[
Scope(C_L)=S_L
]

then:

[
Scope(C_H)
\not\supseteq
S_L
]

without a valid aggregation/generalization rule.

Hard invariant:

```text
UPWARD SCALE != AUTOMATIC SCOPE EXPANSION
```

---

# 32. Local Observation Firewall

A single local observation does not automatically establish a system-level state.

[
\boxed{
Observation_L
\not\Rightarrow
Conclusion_H
}
]

unless a validated dependency and aggregation path exists.

---

# 33. Local Correlation Firewall

[
\boxed{
Correlation_L
\not\Rightarrow
Causation_H
}
]

Local association cannot independently establish system-level causal structure.

---

# 34. Macro Stability / Local Collapse

A system may appear stable at H while a local component collapses at L.

[
\boxed{
Stable_H
\land
Collapsed_L
}
]

is admissible.

Therefore:

```text
MACRO STABILITY != UNIVERSAL LOCAL HEALTH
```

---

# 35. Local Stability / Macro Collapse

Likewise:

[
\boxed{
Stable_L
\land
Collapsed_H
}
]

may occur when failure arises from interactions, coordination, topology, or aggregate constraints.

Therefore:

```text
LOCAL SUCCESS != SYSTEM SUCCESS
```

---

# 36. Heterogeneity Preservation

If local variation is decision-relevant:

[
\boxed{
DecisionRelevant(Heterogeneity_L)
\Rightarrow
Preserve(Heterogeneity)
}
]

Aggregation must not erase meaningful variation merely to simplify the system state.

---

# 37. Compression Invariant

For cross-scale compression:

[
\boxed{
Compress(X_L)
\rightarrow
X_M
}
]

must preserve all load-bearing distinctions required downstream.

Hard rule:

```text
COMPRESSION MAY REMOVE REDUNDANCY

COMPRESSION MAY NOT REMOVE
DECISION-RELEVANT DISTINCTIONS
```

---

# 38. Provenance Preservation

For every valid transformation:

[
\boxed{
Prov(X_{target})
\supseteq
Reference(Prov(X_{source}))
}
]

The transformed state must retain recoverable lineage to its source state.

---

# 39. Provenance Independence

Multiple local observations must not automatically count as independent evidence.

If:

[
E_1,E_2,E_3
]

share the same ancestor (A), then:

[
\boxed{
IndependentCount(E_1,E_2,E_3)
\neq 3
}
]

unless independence is separately established.

---

# 40. Confidence Ceiling

For a conclusion (c):

[
\boxed{
Conf(c)
\leq
\min_{p\in P_c}
Conf(p)
}
]

for unresolved load-bearing premises unless independently revalidated.

Cross-scale aggregation cannot manufacture confidence.

---

# 41. Confidence Propagation

If:

```text
L evidence = uncertain
M inference = derived from L
H conclusion = derived from M
```

then:

```text
H confidence
```

cannot exceed the weakest unresolved load-bearing dependency merely because the information crossed more processing stages.

---

# 42. Uncertainty Tensor

[
\boxed{
U_{HML}
=======

T[
scale,
evidence,
model,
scope,
temporal,
causal,
execution,
provenance_independence
]
}
]

Uncertainty dimensions should remain separate when materially different.

---

# 43. Cross-Scale Uncertainty

A high-level uncertainty may arise from:

```text
uncertain L observations
missing M mechanism
invalid aggregation
scope mismatch
regime mismatch
stale evidence
unknown provenance
unresolved competing models
```

Therefore:

[
\boxed{
U_H
===

f(
U_L,
U_M,
U_{transform},
U_{scope},
U_{regime}
)
}
]

as a conceptual AMOS model.

---

# 44. Sensitivity Flip Set

For conclusion (c):

[
\boxed{
F_c
===

{
p
\mid
plausible\ change\ in\ p
\ flips\ c
}
}
]

The smallest high-impact premise should be tested first.

---

# 45. H/M/L Gap Tensor

[
\boxed{
T_{Gap}^{HML}
=============

T[
gap,
scale,
source_scale,
target_scale,
missing_transform,
dependency,
scope,
regime,
consequence,
blocking,
repairability
]
}
]

---

# 46. H-Level Gaps

Typical H gaps:

```text
unknown system boundary
unknown deployment environment
missing global authority model
missing governing constraints
unknown operating regime
missing system-level validation
missing reality-contact contract
```

---

# 47. M-Level Gaps

Typical M gaps:

```text
missing subsystem relation
unknown dependency
missing routing rule
missing evidence transformation
missing interface
missing control-plane mechanism
missing repair path
```

---

# 48. L-Level Gaps

Typical L gaps:

```text
missing observation
unknown timestamp
unknown source
missing measurement method
unknown unit
missing local validator
unknown representation class
```

---

# 49. Cross-Scale Gap

[
\boxed{
CrossScaleGap
=============

RequiredTransfer
\land
\neg ValidTransfer
}
]

Examples:

```text
local observations exist
but no valid aggregate exists

subsystem evidence exists
but system-level scope transfer is unsupported

global policy exists
but no enforceable local translation exists
```

---

# 50. Upward Failure Propagation

Local failure propagates upward only when dependency structure permits it.

[
\boxed{
Failure_L
\rightarrow
Failure_M
\iff
MaterialDependency(M,L)
}
]

and:

[
\boxed{
Failure_M
\rightarrow
Failure_H
\iff
MaterialDependency(H,M)
}
]

---

# 51. Downward Constraint Failure

A high-level constraint failure may invalidate downstream admissibility.

Example:

```text
AUTHORITY_H = INVALID
```

may imply:

```text
EXECUTION_M = BLOCKED
ACTION_L = BLOCKED
```

without implying that the local action implementation itself is technically defective.

---

# 52. Selective Invalidation

For failed premise (p):

[
\boxed{
Invalidate(p)
=============

Desc_{LB}(p)
}
]

where:

```text
Desc_LB = load-bearing descendants
```

Unrelated branches remain valid.

---

# 53. Scale-Local Repair

A local defect should be repaired at the lowest sufficient scale.

```text
L defect → L repair
```

unless evidence shows:

```text
M mechanism failure
```

or:

```text
H governing failure
```

---

# 54. Repair Escalation

Canonical repair escalation:

```text
L repair
    ↓
validate
    ↓
still failing?
    ↓ yes
M diagnosis / repair
    ↓
validate
    ↓
still failing?
    ↓ yes
H diagnosis / governance repair
```

Hard invariant:

```text
DO NOT ESCALATE SCALE WITHOUT EVIDENCE
```

---

# 55. Downward Repair Validation

A repair made at H must be validated at affected M and L scales.

[
\boxed{
Repair_H
\Rightarrow
Validate(M_{affected})
\land
Validate(L_{affected})
}
]

A policy-level fix is not sufficient evidence of local behavioral correction.

---

# 56. Upward Repair Validation

A local repair does not automatically prove system recovery.

[
\boxed{
Repair_L
\not\Rightarrow
Recovered_H
}
]

System recovery requires appropriate aggregate validation.

---

# 57. Reality Contact Across H/M/L

Reality contact begins from observation-bearing states.

Conceptually:

```text
EXTERNAL REALITY
      ↓
OBSERVATION / MEASUREMENT
      ↓
L
      ↓
M
      ↓
H
```

Every transformation must preserve the distinction between:

```text
what was observed
what was inferred
what was modeled
what was decided
```

---

# 58. Reality Contact Gate

Where external observation is required:

[
\boxed{
RealityContact
==============

ExternalObservationPresent
\land
MeasurementMethodKnown
\land
ProvenanceRecoverable
\land
RegimeCompatible
}
]

---

# 59. Reality Contact Does Not Automatically Transfer

If one local state has reality contact:

[
RealityContact(L_1)=TRUE
]

this does not imply:

[
RealityContact(H)=TRUE
]

for every high-level claim.

The aggregation path must support the claimed system-level conclusion.

---

# 60. Fidelity Envelope

[
\boxed{
Fidelity
========

ValidatedVariables
\cap
ValidatedRegimes
\cap
ValidatedTimeWindow
\cap
ValidatedMeasurementMethods
}
]

Cross-scale conclusions outside this envelope remain conditional or unknown.

---

# 61. Observer Tensor

[
\boxed{
T_O
===

T[
observer,
scale,
access,
measurement,
perspective,
bias,
scope,
time,
regime,
provenance
]
}
]

Observer differences must not be silently erased during aggregation.

---

# 62. Observer Variance

For observations:

[
O_1(X)\neq O_2(X)
]

may arise because of:

```text
different access
different measurement
different time
different scale
different regime
different perspective
```

Disagreement does not automatically imply one observer is wrong.

---

# 63. Temporal H/M/L Architecture

Different scales may evolve at different rates.

[
\boxed{
\tau_L
\neq
\tau_M
\neq
\tau_H
}
]

where (\tau_s) represents characteristic update time at scale (s).

---

# 64. Temporal Aggregation Invariant

A fast local change does not automatically establish a durable high-level regime shift.

```text
LOCAL EVENT
!=
SYSTEM REGIME CHANGE
```

unless persistence and aggregation criteria pass.

---

# 65. Regime Propagation

Each state carries regime:

[
X_s[r]
]

Cross-scale inference requires:

[
\boxed{
Compatible(r_{source},r_{target})
}
]

or an explicitly validated regime translation.

---

# 66. Regime Shift

When regime changes:

```text
r₁ → r₂
```

all affected cross-scale transformations must be revalidated.

[
\boxed{
RegimeShift
\Rightarrow
Revalidate(A,C,T)
}
]

where:

```text
A = aggregation
C = constraint
T = transformation
```

---

# 67. H/M/L Boundary Architecture

Each scale has a boundary:

[
\boxed{
B_H,B_M,B_L
}
]

These boundaries determine:

```text
what belongs to the scale
what crosses the scale
what remains external
what may be aggregated
what may be exposed
what may be controlled
```

---

# 68. Boundary Crossing Tensor

[
\boxed{
T_B
===

T[
source,
target,
source_scale,
target_scale,
payload,
permission,
constraint,
transformation,
provenance,
validation
]
}
]

---

# 69. Boundary Crossing Gate

[
\boxed{
CrossBoundary
=============

TypeCompatible
\land
AdmissionAllowed
\land
AuthorityValid
\land
ProvenancePreserved
\land
ConstraintPass
}
]

for governed transfers.

---

# 70. H/M/L Dependency Graph

Define:

[
\boxed{
G_{HML}
=======

(V_H\cup V_M\cup V_L,E)
}
]

where:

```text
V_H = high-scale nodes
V_M = middle-scale nodes
V_L = low-scale nodes
E   = typed intra-scale and cross-scale relations
```

---

# 71. Edge Types

```text
AGGREGATES_TO
DECOMPOSES_TO
DEPENDS_ON
CONSTRAINS
OBSERVES
MEASURES
SUPPORTS
CONTRADICTS
CAUSES
MEDIATES
ROUTES_TO
VALIDATES
INVALIDATES
REPAIRS
GOVERNS
```

---

# 72. Causal Firewall Across Scale

The following transitions are prohibited without suitable evidence:

```text
CORRELATION_L → CAUSAL_EFFECT_H

SEQUENCE_L → MECHANISM_M

STRUCTURAL_SIMILARITY_M → CAUSAL_LAW_H

AGGREGATION → CAUSATION

CONSTRAINT → CAUSATION
```

---

# 73. Competing Cross-Scale Models

If multiple transformations explain the same observations:

[
M_1,M_2,\ldots,M_n
]

and available evidence does not discriminate them:

```text
status: COMPETING
```

AMOS must not force convergence.

---

# 74. Cheapest Discriminating Test

For competing cross-scale models:

[
\boxed{
Test^*
======

\arg\max_t
\frac{
ExpectedDiscrimination(t)
}{
Cost(t)+Risk(t)
}
}
]

subject to hard safety and governance constraints.

---

# 75. AI Application — H/M/L Cognitive Architecture

For AI systems:

```text
H = governing AI system
M = cognitive / functional subsystem
L = individual information-processing event
```

Example:

```text
H
AI SYSTEM
│
├── objective
├── authority
├── policy
├── deployment regime
└── system decision
     │
     ▼
M
COGNITIVE SUBSYSTEMS
│
├── perception
├── retrieval
├── memory
├── reasoning
├── planning
├── validation
└── tools
     │
     ▼
L
LOCAL EVENTS
│
├── token/context item
├── observation
├── retrieved chunk
├── memory item
├── claim
├── tool call
├── tool result
└── validator result
```

---

# 76. AI Perception Path

[
\boxed{
Environment
\rightarrow
Observation_L
\rightarrow
Perception_M
\rightarrow
WorldState_H
}
]

Each arrow is a transformation, not an identity.

---

# 77. AI Evidence Path

[
\boxed{
Source_L
\rightarrow
Evidence_L
\rightarrow
EvidenceModel_M
\rightarrow
Claim_H
}
]

A source does not become a system-level conclusion without intermediate reasoning and validation.

---

# 78. AI Retrieval Path

```text
EXTERNAL CORPUS
      ↓
retrieval
      ↓
L evidence candidates
      ↓
M evidence evaluation
      ↓
H reasoning state
```

Hard invariant:

```text
RETRIEVED != TRUE

NOT RETRIEVED != ABSENT
```

---

# 79. AI Memory Path

```text
L:
memory item

M:
memory subsystem

H:
persistent cognitive state
```

Memory promotion requires:

```text
provenance
scope
freshness
contradiction checks
retention policy
```

---

# 80. AI Tool Path

```text
H:
authorized objective

↓ constraint

M:
tool-routing subsystem

↓ proposal

L:
specific tool call

↓ observation

L:
tool result

↓ validation

M:
effect interpretation

↓ aggregation

H:
updated system state
```

---

# 81. AI Tool Invariants

```text
TOOL CALL != EFFECT

TOOL RESPONSE != EXTERNAL TRUTH

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

LOCAL SUCCESS != SYSTEM SUCCESS
```

---

# 82. AI Planning Path

[
\boxed{
Goal_H
\rightarrow
Plan_M
\rightarrow
Action_L
}
]

Execution feedback returns:

[
\boxed{
Outcome_L
\rightarrow
Evaluation_M
\rightarrow
StateUpdate_H
}
]

This forms a governed closed loop.

---

# 83. AI Closed-Loop H/M/L Architecture

```text
             H
        GOAL / STATE
          │       ▲
          │       │
          ▼       │
             M
      PLAN / EVALUATION
          │       ▲
          │       │
          ▼       │
             L
      ACTION / OUTCOME
          │       ▲
          └───────┘
```

Without the return path:

```text
ACTION → OUTCOME → OBSERVATION
```

the system is open-loop.

---

# 84. AI Confidence Path

AI confidence must be tied to evidence dependencies across scale.

[
\boxed{
Conf_H
\leq
\min(
Conf_{M,load-bearing},
Conf_{L,load-bearing}
)
}
]

unless weak premises are independently revalidated.

---

# 85. AI Hallucination as Cross-Scale Failure

One AMOS interpretation of hallucination risk is:

```text
missing L evidence
      ↓
unsupported M inference
      ↓
fluent H conclusion
```

The architectural failure is not merely incorrect text.

It is an unsupported dependency transition.

---

# 86. AI Grounding Failure

```text
MODEL STATE_H
```

may drift from:

```text
OBSERVED REALITY_L
```

when:

```text
reality contact is absent
evidence is stale
aggregation is invalid
feedback is missing
measurement changes
regime shifts
```

---

# 87. AI Governance Path

[
\boxed{
Authority_H
\rightarrow
Policy_M
\rightarrow
Permission_L
}
]

Execution requires:

[
\boxed{
Capability_L
\land
Permission_L
\land
ConstraintPass_L
}
]

not capability alone.

---

# 88. AI Repair Path

```text
FAILURE DETECTED
      ↓
identify scale
      ↓
L?
├── repair local state
│
M?
├── repair subsystem
│
H?
└── repair governing architecture
      ↓
validate affected descendants
      ↓
resume
```

---

# 89. Control Plane Requirements

The L00 H/M/L control plane must support:

```text
scale assignment
scale boundary validation
typed aggregation
typed decomposition
cross-scale dependency tracing
scope propagation
regime propagation
observer preservation
provenance preservation
confidence ceilings
causal firewalls
constraint propagation
selective invalidation
gap detection
repair routing
cross-scale validation
```

---

# 90. Control Plane Tensor

[
\boxed{
T_{CP}^{HML}
============

T[
operation,
source_scale,
target_scale,
authority,
constraints,
scope,
regime,
dependencies,
provenance,
validation,
rollback
]
}
]

---

# 91. Agent Contract

Agents may:

```text
observe local state
propose scale classification
propose aggregation
trace cross-scale dependencies
detect scope mismatch
detect regime mismatch
identify competing models
propose repair
execute authorized validation
```

Agents may not automatically:

```text
promote L observation to H truth
convert aggregation into causation
erase local heterogeneity
expand scope without evidence
erase provenance during compression
self-authorize cross-scale execution
```

---

# 92. Skill Contract

Every H/M/L-aware AMOS skill should declare:

```yaml
hml_contract:

  primary_scale:

  accepted_source_scales: []

  produced_target_scales: []

  transformations: []

  scope_requirements: []

  regime_requirements: []

  provenance_requirements: []

  authority_requirements: []

  information_loss:

  validators: []

  falsifiers: []
```

---

# 93. Cross-Scale Workflow

```text
1. Define system boundary.

2. Define H ontology.

3. Define M ontology.

4. Define L ontology.

5. Identify observation-bearing L states.

6. Instantiate the smallest required tensor slice.

7. Bind material cells to RSCF nodes.

8. Type every cross-scale edge.

9. Validate source and target compatibility.

10. Preserve scope.

11. Preserve regime.

12. Preserve observer context.

13. Preserve provenance.

14. Test causal level.

15. Apply confidence ceiling.

16. Preserve decision-relevant heterogeneity.

17. Identify cross-scale gaps.

18. Test the cheapest decision-flipping premise.

19. Produce the weakest accurate conclusion.

20. Record invalidation and reuse conditions.
```

---

# 94. H/M/L Protocol

```yaml
hml_transition:

  source:
    id:
    scale:
    type:
    state:

  target:
    id:
    scale:
    type:

  operator:

  edge_type:

  load_bearing:

  scope:

  regime:

  time:

  observer:

  provenance:

  assumptions: []

  information_loss:

  confidence_before:

  confidence_after:

  validators: []

  falsifiers: []

  status:
    - VERIFIED
    - DERIVED
    - MODEL
    - CONDITIONAL
    - COMPETING
    - UNKNOWN/GAP
```

---

# 95. H/M/L Validation Matrix

| Test               | Requirement                                 |
| ------------------ | ------------------------------------------- |
| Scale definition   | H/M/L roles explicitly defined              |
| Boundary           | Scale boundaries known                      |
| Type compatibility | Source/target semantics compatible          |
| Aggregation        | Aggregation operator declared               |
| Constraint         | Downward constraint explicitly typed        |
| Scope              | Scope preserved or revalidated              |
| Regime             | Regime compatible                           |
| Time               | Temporal alignment valid                    |
| Observer           | Observer differences preserved              |
| Provenance         | Source lineage recoverable                  |
| Confidence         | Weakest-premise ceiling enforced            |
| Causality          | No unsupported causal promotion             |
| Heterogeneity      | Decision-relevant local variation preserved |
| Gap                | Missing cross-scale transforms exposed      |
| Repair             | Repair validated at affected scales         |

---

# 96. Validator Registry

```text
L00-HML-T01 System-boundary validator
L00-HML-T02 H-scale ontology validator
L00-HML-T03 M-scale ontology validator
L00-HML-T04 L-scale ontology validator
L00-HML-T05 Scale-assignment validator
L00-HML-T06 Boundary validator
L00-HML-T07 Type-compatibility validator
L00-HML-T08 Aggregation validator
L00-HML-T09 Decomposition validator
L00-HML-T10 Downward-constraint validator
L00-HML-T11 Scope-propagation validator
L00-HML-T12 Regime-propagation validator
L00-HML-T13 Temporal-alignment validator
L00-HML-T14 Observer-preservation validator
L00-HML-T15 Provenance-preservation validator
L00-HML-T16 Evidence-independence validator
L00-HML-T17 Confidence-ceiling validator
L00-HML-T18 Causal-firewall validator
L00-HML-T19 Heterogeneity-preservation validator
L00-HML-T20 Cross-scale-gap validator
L00-HML-T21 Selective-invalidation validator
L00-HML-T22 Repair-scale validator
L00-HML-T23 Reality-contact validator
L00-HML-T24 Feedback-loop validator
L00-HML-T25 Authority-propagation validator
```

---

# 97. Failure Modes

## HML-F01 — Scale Collapse

```text
H = M = L
```

without explicit equivalence proof.

**Effect:** local and global claims become indistinguishable.

---

## HML-F02 — Local-to-Global Overreach

```text
Observation_L
→
Conclusion_H
```

without a valid aggregation path.

---

## HML-F03 — Global-to-Local Overreach

System-level statistics or policies are treated as direct descriptions of every local state.

---

## HML-F04 — Aggregation-as-Causation

Derived aggregate structure is incorrectly promoted into causal explanation.

---

## HML-F05 — Constraint-as-Causation

Downward governance or admissibility constraints are treated as empirical causal mechanisms.

---

## HML-F06 — Heterogeneity Destruction

Aggregation removes local differences required for correct decisions.

---

## HML-F07 — Scope Expansion

A local claim is generalized beyond its validated population or environment.

---

## HML-F08 — Regime Leakage

Evidence from one regime is reused in another without validation.

---

## HML-F09 — Temporal Misalignment

Fast and slow scale states are combined as if simultaneous.

---

## HML-F10 — Observer Collapse

Different observation contexts are merged without preserving their differences.

---

## HML-F11 — Provenance Loss

Cross-scale transformation removes source ancestry.

---

## HML-F12 — Confidence Inflation

Derived H-level confidence exceeds unresolved load-bearing L/M premises.

---

## HML-F13 — Correlated Evidence Inflation

Multiple descendants of one source are treated as independent cross-scale confirmation.

---

## HML-F14 — Cross-Scale Gap Suppression

Missing transformation logic is silently filled by fluent inference.

---

## HML-F15 — Repair at Wrong Scale

A local symptom is repaired while the governing failure exists at M or H.

---

## HML-F16 — Global Repair Without Local Validation

A policy or architecture change is assumed to have repaired actual downstream behavior.

---

## HML-F17 — Local Repair Promoted to System Recovery

A successful local fix is treated as proof of global recovery.

---

## HML-F18 — Reality/Model Collapse

Model or simulation state is promoted into observed reality during aggregation.

---

# 98. Repair / Recovery

Canonical recovery sequence:

```text
DETECT CROSS-SCALE FAILURE
        ↓
IDENTIFY EARLIEST INVALID EDGE
        ↓
CLASSIFY:
  TYPE
  SCOPE
  REGIME
  TIME
  OBSERVER
  PROVENANCE
  CAUSAL
  AUTHORITY
        ↓
INVALIDATE DEPENDENT DESCENDANTS
        ↓
PRESERVE UNAFFECTED STATE
        ↓
RETURN TO NEAREST VALID SCALE STATE
        ↓
REPAIR TRANSFORM OR PREMISE
        ↓
REVALIDATE
        ↓
PROPAGATE AGAIN
```

---

# 99. Hard Invariants

## L00-HML-INV-01

```text
H != M != L
```

unless explicit equivalence is established for the declared operation.

## L00-HML-INV-02

```text
AGGREGATION != IDENTITY
```

## L00-HML-INV-03

```text
AGGREGATION != CAUSATION
```

## L00-HML-INV-04

```text
DOWNWARD CONSTRAINT != DOWNWARD CAUSATION
```

## L00-HML-INV-05

```text
LOCAL CORRELATION != SYSTEM CAUSATION
```

## L00-HML-INV-06

```text
LOCAL SUCCESS != SYSTEM SUCCESS
```

## L00-HML-INV-07

```text
MACRO STABILITY != UNIVERSAL LOCAL STABILITY
```

## L00-HML-INV-08

```text
SCALE TRANSLATION != AUTOMATIC SCOPE EXPANSION
```

## L00-HML-INV-09

```text
REPRESENTATION CLASS MUST SURVIVE SCALE TRANSFORMATION
```

## L00-HML-INV-10

```text
PROVENANCE MUST SURVIVE CROSS-SCALE TRANSFORMATION
```

## L00-HML-INV-11

```text
UNKNOWN ANCESTRY != INDEPENDENCE
```

## L00-HML-INV-12

```text
CROSS-SCALE PROCESSING MAY NOT MANUFACTURE CONFIDENCE
```

## L00-HML-INV-13

```text
DECISION-RELEVANT HETEROGENEITY MUST SURVIVE AGGREGATION
```

## L00-HML-INV-14

```text
REGIME CHANGE REQUIRES AFFECTED TRANSFORM REVALIDATION
```

## L00-HML-INV-15

```text
LOCAL FAILURE INVALIDATES ONLY MATERIAL DEPENDENTS
```

## L00-HML-INV-16

```text
REPAIR MUST TARGET THE EARLIEST MATERIAL FAILURE SCALE
```

## L00-HML-INV-17

```text
MODEL != OBSERVED REALITY
```

## L00-HML-INV-18

```text
CAPABILITY != AUTHORITY
```

## L00-HML-INV-19

```text
PROPOSAL != COMMIT
```

## L00-HML-INV-20

```text
UNKNOWN/GAP != PASS
```

---

# 100. Falsifiers

This architecture is falsified as a claimed implementation if:

1. H/M/L scales are not explicitly defined;
2. local evidence is promoted directly into global truth without a valid path;
3. cross-scale transforms lack semantic types;
4. aggregation is treated as identity;
5. aggregation is treated as causal proof;
6. downward constraint is treated as causal proof;
7. scope disappears during scale transformation;
8. regime disappears during scale transformation;
9. observer context disappears when decision-relevant;
10. provenance is lost;
11. confidence increases without independent evidence;
12. correlated sources are treated as independent;
13. decision-relevant heterogeneity is erased;
14. model state becomes observed reality through aggregation;
15. local repair automatically counts as global recovery;
16. high-level repair requires no downstream validation;
17. invalid local state causes unrelated branches to be invalidated;
18. cross-scale gaps are silently filled;
19. authority is inferred from capability;
20. unresolved H/M/L dependencies can still return unconditional `PASS`.

---

# 101. RSCF Completion State

```yaml
claim_class: MODEL

evidence:
  - AMOS cross-scale H/M/L architecture
  - typed tensor contracts
  - RSCF node and dependency architecture
  - reality/representation distinction
  - provenance-preserving reasoning
  - scope/regime firewalls
  - selective invalidation architecture

provenance:
  origin_architect: Trang Phan
  architecture_family: AMOS
  layer: L00_REALITY_ENVIRONMENT
  component: HML

scope:
  applies_to:
    - reality representation
    - observations
    - evidence
    - claims
    - AI cognition
    - memory
    - retrieval
    - tools
    - planning
    - governance
    - validation
    - repair
    - deployment

regime:
  - typed-state reasoning
  - multi-resolution reasoning
  - provenance-aware reasoning
  - governed AI execution

freshness:
  cross_scale_claims_require_current_dependency_validity: true
  mutable_regime_state_requires_revalidation: true

dependencies:
  - L00_REALITY_ENVIRONMENT/DEFINITION
  - L00_REALITY_ENVIRONMENT/DEPENDENCIES
  - L00_REALITY_ENVIRONMENT/EQUATIONS
  - L00_REALITY_ENVIRONMENT/CONTROL_PLANES
  - L00_REALITY_ENVIRONMENT/FAILURE_MODES
  - L00_REALITY_ENVIRONMENT/GAP_MATRIX
  - typed tensor contracts
  - claim tensor
  - evidence tensor
  - relation tensor
  - provenance topology
  - reality/simulation distinction
  - constraint propagation
  - boundary architecture

competing:
  - flat single-scale reasoning
  - fixed global/local binary hierarchy
  - untyped hierarchical aggregation
  - unrestricted local-to-global generalization

falsifiers:
  - scale assignments cannot be defined
  - cross-scale transformations cannot be typed
  - provenance cannot survive aggregation
  - scope/regime cannot survive transformation
  - local/global claims cannot be distinguished
  - selective invalidation cannot be represented

confidence_ceiling:
  architecture_contract: high
  implementation_status: unknown_without_runtime_evidence
  empirical_universality: unverified
  ontological_universality: unverified
```

---

# 102. Hard Boundaries

```text
H/M/L MODEL != UNIVERSAL ONTOLOGY

LOCAL != SUBSYSTEM != SYSTEM

OBSERVATION != INFERENCE

INFERENCE != MODEL

MODEL != REALITY

AGGREGATION != IDENTITY

AGGREGATION != CAUSATION

CONSTRAINT != CAUSATION

CORRELATION != CAUSATION

LOCAL SUCCESS != SYSTEM SUCCESS

MACRO STABILITY != LOCAL STABILITY

SCALE CHANGE != SCOPE EXPANSION

SHARED ANCESTRY != INDEPENDENCE

COMPRESSION != LICENSE TO REMOVE LOAD-BEARING DISTINCTIONS

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

UNKNOWN/GAP != PASS
```

---

# 103. Canonical L00 H/M/L Loop

```text
EXTERNAL REALITY
       │
       ▼
┌───────────────────────┐
│           L           │
│ LOCAL / OBSERVATION   │
│                       │
│ events                │
│ measurements          │
│ evidence              │
│ claims                │
│ tool results          │
└──────────┬────────────┘
           │
           │ typed aggregation
           │ + provenance
           │ + scope
           │ + regime
           ▼
┌───────────────────────┐
│           M           │
│ SUBSYSTEM / RELATION  │
│                       │
│ mechanisms            │
│ interfaces            │
│ memory                │
│ reasoning             │
│ validation            │
│ control               │
└──────────┬────────────┘
           │
           │ typed aggregation
           │ + validation
           ▼
┌───────────────────────┐
│           H           │
│ SYSTEM / GOVERNANCE   │
│                       │
│ system state          │
│ objectives            │
│ authority             │
│ constraints           │
│ decisions             │
└──────────┬────────────┘
           │
           │ downward constraints
           ▼
          M
           │
           ▼
          L
           │
           │ action
           ▼
EXTERNAL ENVIRONMENT
           │
           │ observed consequence
           └──────────────→ L
```

---

# 104. Final H/M/L Law

The governing L00 cross-scale principle is:

[
\boxed{
ValidCrossScaleReasoning
========================

TypedTransformation
\land
DependencyClosure
\land
ScopeCompatibility
\land
RegimeCompatibility
\land
TemporalCompatibility
\land
ProvenancePreservation
\land
InvariantPreservation
}
]

For reality-bearing conclusions:

[
\boxed{
RealityGrounded_H
\Rightarrow
ValidRealityContact_L
\land
ValidPath_{L\rightarrow M\rightarrow H}
}
]

For governed action:

[
\boxed{
Action_L
========

Decision_H
\land
Plan_M
\land
Capability_L
\land
Authority
\land
ConstraintPass
}
]

For recovery:

[
\boxed{
Recovery
========

LocateFailureScale
\rightarrow
RepairLowestSufficientScale
\rightarrow
RevalidateAffectedDependencies
}
]

The central architectural rule is:

> **AMOS may move information, constraints, evidence, and decisions across H/M/L scales only through explicit typed transformations. A local observation does not become a system truth by aggregation, a system constraint does not become a causal mechanism by propagation, and cross-scale reasoning may never erase provenance, scope, regime, uncertainty, or decision-relevant heterogeneity.**

---

**Related:** [[00-Home]] · [[06-Knowledge-Base-MOC]] · [[L00_REALITY_ENVIRONMENT — Definition]] · [[L00_REALITY_ENVIRONMENT — Dependencies]] · [[L00_REALITY_ENVIRONMENT — Equations]] · [[L00_REALITY_ENVIRONMENT — Control Planes]] · [[L00_REALITY_ENVIRONMENT — Failure Modes]] · [[L00_REALITY_ENVIRONMENT — Gap Matrix]] · [[AMOS_Typed_Tensor_Contracts]] · [[AMOS_Evidence_Tensor_Architecture]] · [[AMOS_Claim_Tensor_Architecture]] · [[AMOS_Relation_Tensor_Architecture]] · [[AMOS_Cross_Scale_RSCF_Tensor_Engine]] · [[AMOS_Reality_Simulation_Distinction]] · [[AMOS_Constraint_Propagation]] · [[AMOS_Provenance_Topology]] · [[AMOS_Infrastructure_Control_Plane]] · [[AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[system_scan_agent]] · [[automation_profiles]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
