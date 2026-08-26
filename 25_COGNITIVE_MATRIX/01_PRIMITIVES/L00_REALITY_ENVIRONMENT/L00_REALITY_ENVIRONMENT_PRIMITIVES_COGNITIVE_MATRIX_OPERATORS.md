---
title: "L00_REALITY_ENVIRONMENT — Operators"
aliases:

* "AMOS Reality Environment Operators"
* "L00 Reality Operators"
* "Reality Interaction Operators"
  canon-type: architecture
  rscf-class: MODEL
  rscf-state: conditional
  amos-layer: L00_REALITY_ENVIRONMENT
  architecture-role: reality-environment-operation-substrate
  origin-architect: "Trang Phan"
  status: "ARCHITECTURE CONTRACT / IMPLEMENTATION-DEPENDENT"
  tags:
* amos
* reality-environment
* operators
* observation
* measurement
* evidence
* provenance
* state-transition
* control-plane
* hml
* causality
* simulation
* validation
* repair
* governance
tags: ['cognitive_matrix', 'primitives', 'l00_reality_environment', 'note']

---
# L00_REALITY_ENVIRONMENT — Operators

**Class:** `AMOS_REALITY_ENVIRONMENT_OPERATOR_ARCHITECTURE`
**Origin architect / steward:** Trang Phan
**Status:** `ARCHITECTURE CONTRACT / IMPLEMENTATION-DEPENDENT`

---

# 1. Purpose

`L00_REALITY_ENVIRONMENT / OPERATORS` defines the typed transformations through which AMOS may observe, represent, compare, update, test, act upon, and reason about an external or operational environment.

Operators are not merely functions.

An AMOS operator is a governed transformation:

[
\boxed{
O:
(State, Input, Context, Authority)
\rightarrow
(State', Output, Evidence, Provenance)
}
]

Every material operator must preserve enough information to determine:

* what entered the transformation;
* what transformation occurred;
* which actor or subsystem invoked it;
* which state changed;
* which state did not change;
* which assumptions were required;
* what evidence was generated;
* where that evidence came from;
* whether the operation was authorized;
* whether it was reversible;
* and what would invalidate its result.

---

# 2. Operator Architecture

```text
REALITY / ENVIRONMENT
        │
        ▼
     SENSE
        │
        ▼
    OBSERVE
        │
        ▼
    MEASURE
        │
        ▼
    REPRESENT
        │
        ▼
     CLASSIFY
        │
        ▼
     COMPARE
        │
        ▼
      INFER
        │
        ▼
     VALIDATE
        │
        ▼
      MODEL
        │
        ▼
    SIMULATE
        │
        ▼
     PREDICT
        │
        ▼
      DECIDE
        │
        ▼
      PROPOSE
        │
        ▼
     AUTHORIZE
        │
        ▼
      COMMIT
        │
        ▼
       ACT
        │
        ▼
     OBSERVE
        │
        ▼
    EVALUATE
        │
        ▼
      UPDATE
        │
        ▼
      REPAIR
```

The chain is not mandatory for every operation.

It defines separable operator classes that must not be silently collapsed.

---

# 3. Universal Operator Tensor

[
\boxed{
T_O =
T[
operator_id,
operator_class,
actor,
input,
input_type,
pre_state,
output,
output_type,
post_state,
scope,
regime,
HML_scale,
observer,
time,
authority,
constraints,
provenance,
evidence,
confidence,
reversibility,
consequence,
falsifiers
]
}
]

---

# 4. Operator Signature

Every material operator should expose a typed contract:

```text
OPERATOR
    name
    class
    inputs
    outputs
    preconditions
    state-read-set
    state-write-set
    scope
    regime
    H/M/L scale
    authority requirement
    invariants
    evidence produced
    provenance
    failure states
    rollback
    falsifiers
```

Formally:

[
\boxed{
O_i:
X_i
\times
S_i
\times
C_i
\rightarrow
Y_i
\times
S'_i
}
]

where:

* (X_i) = typed inputs;
* (S_i) = pre-operation state;
* (C_i) = operating context;
* (Y_i) = typed outputs;
* (S'_i) = post-operation state.

---

# 5. Operator Classes

Primary L00 operator classes:

```text
SENSE
OBSERVE
MEASURE
DETECT
DISTINGUISH
IDENTIFY
CLASSIFY
RELATE
COMPARE
BOUND
FILTER
SELECT
TRANSFORM
NORMALIZE
AGGREGATE
DECOMPOSE
MAP
TRANSLATE
INFER
ESTIMATE
VALIDATE
FALSIFY
MODEL
SIMULATE
COUNTERFACTUALIZE
PREDICT
UPDATE
RETRIEVE
ADMIT
QUARANTINE
INVALIDATE
REPAIR
PROPOSE
AUTHORIZE
COMMIT
ACT
ROLLBACK
AUDIT
```

These classes may compose but remain semantically distinct.

---

# 6. Observation Operator

[
\boxed{
O_{obs}:
RealityState
\times
Observer
\times
ObservationMethod
\rightarrow
Observation
}
]

Tensor:

[
T_{obs}
=======

T[
target,
observer,
method,
time,
environment,
resolution,
observation,
uncertainty,
provenance
]
]

Hard boundary:

```text
OBSERVATION != REALITY ITSELF
```

Observation is observer-, method-, time-, and resolution-dependent.

---

# 7. Measurement Operator

[
\boxed{
O_{measure}:
ObservedState
\times
MeasurementMethod
\rightarrow
MeasuredProxy
}
]

Tensor:

[
T_{measure}
===========

T[
variable,
instrument,
method,
unit,
resolution,
calibration,
timestamp,
value,
uncertainty,
provenance
]
]

Invariant:

[
\boxed{
MeasuredProxy(x)
\neq
UnderlyingReality(x)
}
]

unless equivalence is independently justified.

---

# 8. Distinction Operator

[
\boxed{
O_{\Delta}:
X
\rightarrow
{x_i}
}
]

The distinction operator creates addressable separation between states or entities.

Required properties:

```text
distinction criterion
boundary
identity condition
exclusion condition
observer
scope
```

Hard invariant:

```text
LABEL != ENTITY
```

and:

```text
DIFFERENT NAME != PROVEN DIFFERENCE
```

---

# 9. Identification Operator

[
\boxed{
O_{id}:
Observation
\times
IdentityCriteria
\rightarrow
IdentityHypothesis
}
]

Identification may return:

```text
MATCH
PROBABLE_MATCH
NON_MATCH
AMBIGUOUS
UNKNOWN
```

Identity must not be inferred solely from superficial similarity.

---

# 10. Classification Operator

[
\boxed{
O_{class}:
x
\times
ClassificationSchema
\rightarrow
Class(x)
}
]

The classification schema must remain recoverable.

Invariant:

[
\boxed{
Class(x)
\neq
Essence(x)
}
]

Classification is a representation operation, not ontological proof.

---

# 11. Relation Operator

[
\boxed{
O_R:
(x_i,x_j)
\rightarrow
R_{ij}
}
]

with:

[
R_{ij}
======

T[
type,
direction,
strength,
dependency,
confidence,
causal_pressure,
trust,
conflict,
lag,
entropy,
repair_coupling,
mutation_transfer,
observer_variance,
provenance
]
]

Relation classes may include:

```text
semantic
causal
dependency
contradiction
repair
mutation
selection
observer
temporal
evidence
risk
trust
scale
analogy
governance
```

---

# 12. Causal Promotion Gate

A relation cannot become causal merely because it is strong.

[
\boxed{
PromoteToCausal(R)
==================

MechanisticOrInterventionalEvidence
\land
ConfounderControlAdequate
\land
ScopeCompatible
}
]

as required by the causal claim.

Hard boundary:

```text
CORRELATION != CAUSATION

SEQUENCE != CAUSATION

SIMILARITY != CAUSATION

DEPENDENCY != CAUSATION
```

---

# 13. Comparison Operator

[
\boxed{
O_{cmp}:
x_i
\times
x_j
\times
CoordinateFrame
\rightarrow
Comparison
}
]

Comparison requires compatible coordinates.

[
\boxed{
Comparable(x_i,x_j)
\Rightarrow
CoordinateCompatible(x_i,x_j)
}
]

Same-name variables do not guarantee comparability.

---

# 14. Boundary Operator

[
\boxed{
O_B:
StateSpace
\times
BoundaryRule
\rightarrow
Inside \cup Outside \cup Boundary
}
]

The operator defines admission or exclusion relative to an explicit boundary.

Hard invariant:

```text
BOUNDARY != ABSOLUTE ISOLATION
```

unless the boundary is explicitly impermeable.

---

# 15. Filter Operator

[
\boxed{
O_F:
X
\times
Predicate
\rightarrow
X'
}
]

where:

[
X'
==

{x\in X:P(x)=TRUE}
]

Filtering must preserve the predicate used.

Otherwise downstream systems cannot reconstruct why information disappeared.

---

# 16. Selection Operator

[
\boxed{
O_S:
CandidateSet
\times
Objective
\times
Constraints
\rightarrow
SelectedSet
}
]

Selection is not proof of correctness.

```text
SELECTED != TRUE

SELECTED != BEST UNIVERSALLY

SELECTED != AUTHORIZED
```

---

# 17. Transformation Operator

[
\boxed{
O_T:
X
\xrightarrow{\tau}
Y
}
]

Transformation metadata must preserve:

```text
source representation
target representation
mapping
information loss
assumptions
provenance
```

---

# 18. Translation Operator

[
\boxed{
O_{trans}:
Representation_A
\rightarrow
Representation_B
}
]

with semantic preservation condition:

[
\boxed{
Meaning_B
\approx
Meaning_A
}
]

within an explicit translation envelope.

Translation may introduce loss:

[
\boxed{
L_{trans}
=========

## Information_A

RecoverableInformation_B
}
]

where this quantity is defined for the representation.

---

# 19. Normalization Operator

[
\boxed{
O_N:
X
\times
ReferenceFrame
\rightarrow
X_N
}
]

Normalization must preserve enough metadata to reverse or interpret the transformation.

```text
NORMALIZED VALUE != RAW OBSERVATION
```

---

# 20. Aggregation Operator

[
\boxed{
O_A:
{x_1,...,x_n}
\rightarrow
X_A
}
]

Aggregation must expose:

```text
aggregation rule
weights
missingness
heterogeneity
scope
regime
provenance
```

Hard boundary:

```text
AGGREGATE != EVERY COMPONENT
```

---

# 21. Decomposition Operator

[
\boxed{
O_D:
X
\rightarrow
{x_1,...,x_n}
}
]

A decomposition is valid only relative to its decomposition rule.

Different valid decompositions may coexist.

---

# 22. Mapping Operator

[
\boxed{
O_M:
X_A
\rightarrow
X_B
}
]

Mapping across domains or scales must preserve mapping assumptions.

Cross-domain structural resemblance remains:

```text
MODEL
```

unless independently validated.

---

# 23. Inference Operator

[
\boxed{
O_I:
Premises
\times
Rules
\rightarrow
Conclusion
}
]

The resulting conclusion must retain dependencies.

[
\boxed{
Conf(C)
\leq
\min_i Conf(P_i)
}
]

for unresolved load-bearing premises unless independent revalidation supports a higher ceiling.

---

# 24. Estimation Operator

[
\boxed{
O_E:
Evidence
\times
Estimator
\rightarrow
Estimate
}
]

Estimate tensor:

[
T_E
===

T[
target,
estimator,
data,
assumptions,
estimate,
uncertainty,
scope,
regime,
time,
provenance
]
]

Hard boundary:

```text
ESTIMATE != OBSERVATION
```

---

# 25. Validation Operator

[
\boxed{
O_V:
Claim
\times
Evidence
\times
Criteria
\rightarrow
ValidationState
}
]

Possible outputs:

```text
VERIFIED
DERIVED
MODEL
CONDITIONAL
COMPETING
UNKNOWN/GAP
FALSIFIED
```

Validation is claim-specific.

Evidence valid for one claim does not automatically validate another.

---

# 26. Falsification Operator

[
\boxed{
O_{\neg}:
Claim
\times
Falsifier
\rightarrow
ClaimState'
}
]

A falsifier may include:

```text
contradictory observation
failed premise
counterexample
scope violation
regime shift
source revocation
reproduction failure
hard-invariant violation
```

---

# 27. Model Operator

[
\boxed{
O_{model}:
Evidence
\times
Assumptions
\times
ModelClass
\rightarrow
ModelState
}
]

Hard invariant:

```text
MODEL_STATE != OBSERVED_REALITY
```

A model remains a representation even when predictive performance is high.

---

# 28. Simulation Operator

[
\boxed{
O_{sim}:
Model
\times
InitialState
\times
Parameters
\times
Scenario
\rightarrow
SimulatedTrajectory
}
]

Tensor:

[
T_{sim}
=======

T[
model,
initial_state,
parameters,
scenario,
randomness,
trajectory,
environment,
validation,
provenance
]
]

Hard boundary:

```text
SIMULATION CONSISTENCY != REAL-WORLD CONFIRMATION
```

---

# 29. Counterfactual Operator

[
\boxed{
O_{cf}:
ObservedState
\times
InterventionHypothesis
\times
CausalModel
\rightarrow
CounterfactualState
}
]

Counterfactual output must remain typed:

```text
COUNTERFACTUAL
```

not:

```text
OBSERVED_HISTORY
```

---

# 30. Prediction Operator

[
\boxed{
O_P:
State_t
\times
Model
\times
Horizon
\rightarrow
Forecast_{t+h}
}
]

Prediction tensor:

[
T_P
===

T[
target,
forecast_origin,
horizon,
model,
features,
regime,
distribution,
confidence,
assumptions,
provenance
]
]

Hard invariant:

```text
FORECAST != FUTURE OBSERVATION
```

---

# 31. Reality-Contact Operator

[
\boxed{
O_{RC}:
Representation
\times
ExternalEvidence
\rightarrow
RealityContactState
}
]

Gate:

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

# 32. Update Operator

[
\boxed{
O_U:
State_t
\times
NewEvidence
\rightarrow
State_{t+1}
}
]

Update must preserve lineage:

[
\boxed{
State_t
\rightarrow
State_{t+1}
}
]

with:

```text
changed fields
unchanged fields
reason
evidence
actor
timestamp
version
```

---

# 33. Retrieval Operator

[
\boxed{
O_{ret}:
Store
\times
Query
\rightarrow
CandidateEvidence
}
]

Hard invariant:

```text
RETRIEVED != VALIDATED
```

Retrieval creates candidates for reasoning.

It does not create epistemic authority.

---

# 34. Admission Operator

[
\boxed{
O_{adm}:
Candidate
\times
AdmissionPolicy
\rightarrow
AdmissionState
}
]

Possible states:

```text
ADMIT
CONDITIONAL
QUARANTINE
REJECT
UNKNOWN
```

---

# 35. Quarantine Operator

[
\boxed{
O_Q:
Candidate
\rightarrow
QuarantinedState
}
]

Quarantine preserves information while preventing unsafe promotion or propagation.

```text
QUARANTINED != DELETED

QUARANTINED != VALIDATED
```

---

# 36. Invalidation Operator

[
\boxed{
O_{inv}:
PremiseFailure
\times
DependencyGraph
\rightarrow
InvalidationSet
}
]

Selective invalidation rule:

[
\boxed{
Invalidate(P)
\Rightarrow
Invalidate(Dependent(P))
}
]

while:

[
\boxed{
Independent(X,P)
\Rightarrow
Preserve(X)
}
]

---

# 37. Proposal Operator

[
\boxed{
O_{prop}:
State
\times
Objective
\rightarrow
ProposedAction
}
]

Hard boundary:

```text
PROPOSAL != AUTHORITY
```

---

# 38. Authorization Operator

[
\boxed{
O_{auth}:
Proposal
\times
Principal
\times
Policy
\times
CurrentState
\rightarrow
AuthorizationState
}
]

Possible states:

```text
AUTHORIZED
DENIED
CONDITIONAL
EXPIRED
REVOKED
UNKNOWN
```

---

# 39. Commit Operator

[
\boxed{
O_C:
AuthorizedProposal
\times
CurrentState
\rightarrow
CommittedEffect
}
]

Commit requires current validity.

[
\boxed{
Commit
======

ProposalValid
\land
AuthorityValid
\land
ConstraintsPass
\land
StateFresh
}
]

where those gates are required.

---

# 40. Action Operator

[
\boxed{
O_{act}:
CommittedEffect
\times
Environment
\rightarrow
Environment'
}
]

Action is the operator class capable of changing external or durable operational state.

Hard boundary:

```text
REASONING != ACTION

PROPOSAL != ACTION

AUTHORIZATION != ACTION

COMMIT INTENT != SUCCESSFUL EFFECT
```

---

# 41. Outcome Observation Operator

After action:

[
\boxed{
O_{out}:
Environment'
\times
ObservationMethod
\rightarrow
ObservedOutcome
}
]

Expected consequence and observed consequence must remain distinct.

---

# 42. Evaluation Operator

[
\boxed{
O_{eval}:
ExpectedOutcome
\times
ObservedOutcome
\times
Criteria
\rightarrow
Evaluation
}
]

Evaluation may update:

```text
model confidence
policy confidence
operator reliability
repair priority
future action selection
```

but may not rewrite the historical expectation.

---

# 43. Repair Operator

[
\boxed{
O_{repair}:
FailureState
\times
RepairTarget
\times
RepairPlan
\rightarrow
CandidateRecoveredState
}
]

Repair must itself be validated.

```text
REPAIR APPLIED != RECOVERY VERIFIED
```

---

# 44. Rollback Operator

[
\boxed{
O_{rollback}:
State_{t+1}
\times
RecoveryReference
\rightarrow
State_t'
}
]

Rollback success requires:

[
\boxed{
RequiredInvariants(State_t') = PASS
}
]

A rollback target may require revalidation because the environment may have changed.

---

# 45. Audit Operator

[
\boxed{
O_{audit}:
OperationHistory
\times
Policy
\times
Evidence
\rightarrow
AuditState
}
]

Audit checks:

```text
what occurred
who initiated it
who authorized it
what evidence was used
what state changed
what constraints applied
what failures occurred
whether rollback remains possible
```

---

# 46. Operator Composition

For compatible operators:

[
\boxed{
O_{chain}
=========

O_n
\circ
O_{n-1}
\circ
...
\circ
O_1
}
]

Composition is permitted only if adjacent contracts are compatible.

[
\boxed{
OutputType(O_i)
\sim
InputType(O_{i+1})
}
]

and scope/regime semantics remain valid.

---

# 47. Operator Composition Tensor

[
\boxed{
T_{OC}
======

T[
operator_chain,
input_contract,
intermediate_states,
output_contract,
shared_scope,
shared_regime,
dependencies,
authority_path,
provenance_path,
failure_edges
]
}
]

---

# 48. Non-Commutativity

AMOS operators must not be assumed commutative.

[
\boxed{
O_A(O_B(x))
\neq
O_B(O_A(x))
}
]

in general.

Examples:

```text
FILTER → AGGREGATE
!=
AGGREGATE → FILTER

NORMALIZE → THRESHOLD
!=
THRESHOLD → NORMALIZE

INVALIDATE → RETRIEVE
!=
RETRIEVE → INVALIDATE
```

Operator order is part of provenance.

---

# 49. Operator Idempotence

Some operators may be idempotent:

[
\boxed{
O(O(x)) = O(x)
}
]

only when explicitly defined.

Examples may include certain canonicalization or quarantine operations.

Idempotence must not be assumed globally.

---

# 50. Operator Reversibility

For reversible operator (O):

[
\boxed{
O^{-1}(O(x)) = x
}
]

within the defined fidelity envelope.

Operators may instead be:

```text
REVERSIBLE
PARTIALLY_REVERSIBLE
COMPENSATABLE
IRREVERSIBLE
UNKNOWN
```

---

# 51. Information-Loss Tensor

[
\boxed{
T_L =
T[
operator,
input_information,
preserved_information,
discarded_information,
recoverability,
decision_relevance,
provenance
]
}
]

Loss of noncritical detail may be acceptable.

Loss of load-bearing distinctions is not.

---

# 52. Operator Integrity Function

[
\boxed{
Integrity(O)
============

TypeSafety
\land
ScopeSafety
\land
RegimeSafety
\land
ProvenancePreservation
\land
InvariantPreservation
\land
AuthoritySafety
}
]

where each dimension is applicable to the operator.

---

# 53. State Transition Equation

Let environment state be (S_t).

[
\boxed{
S_{t+1}
=======

O(S_t,X_t,C_t)
}
]

This is an architectural state-transition form, not a claim that all real-world dynamics are deterministic.

For stochastic operators:

[
\boxed{
S_{t+1}
\sim
P(
S_{t+1}
\mid
S_t,X_t,C_t,O
)
}
]

---

# 54. Operator Precondition Gate

[
\boxed{
Executable(O)
=============

InputsValid
\land
PreconditionsPass
\land
ConstraintsPass
\land
DependenciesAvailable
}
]

For effectful operations:

[
\boxed{
Executable(O_{effect})
\Rightarrow
AuthorityValid
}
]

where authority is required.

---

# 55. Postcondition Gate

After operation:

[
\boxed{
Accept(O)
=========

PostconditionsPass
\land
HardInvariantsPass
}
]

A successful function return is not sufficient evidence of semantic correctness.

---

# 56. Operator Provenance

Every consequential operation should preserve:

[
\boxed{
P_O =
[
operator,
actor,
input,
state,
time,
environment,
authority,
output,
evidence,
version
]
}
]

This supports replay, audit, repair, and invalidation.

---

# 57. H/M/L Operator Architecture

## H — Governing Operators

H-level operators govern:

```text
global constraints
architecture transitions
authority
cross-domain coordination
canon/governance state
system-wide invalidation
high-consequence commits
```

## M — Subsystem Operators

M-level operators govern:

```text
domain models
agent coordination
workflow transitions
memory operations
evidence aggregation
subsystem repair
regime detection
```

## L — Local Operators

L-level operators govern:

```text
observation
measurement
tool invocation
local transformation
specific retrieval
local validation
specific state mutation
```

---

# 58. H/M/L Operator Tensor

[
\boxed{
T_{HML-O}
=========

T[
operator,
scale,
target,
parent_operator,
child_operators,
upward_effects,
downward_constraints,
scope,
regime,
provenance
]
}
]

---

# 59. Cross-Scale Operator Invariant

[
\boxed{
LocalSuccess
\not\Rightarrow
GlobalValidity
}
]

and:

[
\boxed{
GlobalConstraint
\Rightarrow
Constrain(LocalOperator)
}
]

where the constraint applies.

---

# 60. Upward Propagation

For local operations (O_{L_i}):

[
\boxed{
\Delta S_H
==========

A(
\Delta S_{L_1},
...,
\Delta S_{L_n}
)
}
]

only through an explicit aggregation or propagation rule.

Local effects do not automatically imply system-level effects.

---

# 61. Downward Constraint Propagation

[
\boxed{
C_H
\rightarrow
C_M
\rightarrow
C_L
}
]

Higher-level hard constraints may restrict lower-level operator admissibility.

Lower-level optimization may not override applicable higher-level invariants.

---

# 62. Observer Operator Tensor

[
\boxed{
T_{OO}
======

T[
observer,
operator,
target,
access,
resolution,
bias,
measurement_method,
time,
scope,
regime,
provenance
]
}
]

Different observers may produce different valid observations of the same system under different access conditions.

Observer disagreement does not automatically imply one observer is wrong.

---

# 63. Temporal Operator Tensor

[
\boxed{
T_{OT}
======

T[
operator,
event_time,
observation_time,
execution_time,
commit_time,
validation_time,
lag,
expiry,
temporal_regime
]
}
]

Hard invariant:

```text
EVENT TIME != OBSERVATION TIME != COMMIT TIME
```

unless explicitly equal.

---

# 64. Regime Operator

[
\boxed{
O_R^{regime}:
State
\times
Evidence
\rightarrow
RegimeState
}
]

A regime transition may invalidate previously valid operator assumptions.

[
\boxed{
RegimeChange
\Rightarrow
Revalidate(RegimeDependentOperators)
}
]

---

# 65. Constraint Propagation Operator

[
\boxed{
O_C^{prop}:
Constraint
\times
DependencyGraph
\rightarrow
AffectedSet
}
]

Hard constraints propagate through applicable dependency edges.

---

# 66. Dependency Resolution Operator

[
\boxed{
O_D^{resolve}:
Target
\times
DependencyGraph
\rightarrow
DependencyClosure
}
]

AMOS should resolve the smallest sufficient dependency closure rather than loading the entire system when unnecessary.

---

# 67. Provenance Resolution Operator

[
\boxed{
O_P^{resolve}:
EvidenceSet
\rightarrow
AncestryGraph
}
]

This operator determines whether apparently separate evidence shares ancestry.

---

# 68. Independence Operator

[
\boxed{
O_{ind}:
(E_i,E_j)
\rightarrow
IndependenceState
}
]

Possible states:

```text
INDEPENDENT
PARTIALLY_DEPENDENT
SHARED_ANCESTRY
CORRELATED
UNKNOWN
```

Hard invariant:

```text
INDEPENDENCE MUST BE DEMONSTRATED
WHEN INDEPENDENT SUPPORT IS CLAIMED
```

---

# 69. Contradiction Detection Operator

[
\boxed{
O_{conflict}:
ClaimSet
\rightarrow
ConflictGraph
}
]

Conflict tensor:

[
T_C
===

T[
claim_i,
claim_j,
conflict_type,
scope_overlap,
regime_overlap,
temporal_overlap,
provenance_relation,
resolution_state
]
]

---

# 70. Competing-Hypothesis Operator

[
\boxed{
O_{comp}:
Evidence
\times
HypothesisSet
\rightarrow
CompetitionState
}
]

When discriminating evidence is insufficient:

```text
PRESERVE COMPETING
```

rather than forcing convergence.

---

# 71. Discriminating-Test Operator

[
\boxed{
O_{test}:
HypothesisSet
\times
CandidateTests
\rightarrow
Test^*
}
]

where:

[
\boxed{
Test^*
======

\arg\max_T
\frac{
ExpectedDiscrimination(T)
}{
Cost(T)+Risk(T)
}
}
]

This is an AMOS decision model, not a universal empirical equation.

---

# 72. Sensitivity Operator

[
\boxed{
O_{sens}:
Conclusion
\times
Premises
\rightarrow
FlipSet
}
]

where:

[
\boxed{
FlipSet
=======

{
p_i:
Change(p_i)
\Rightarrow
Change(Conclusion)
}
}
]

Load-bearing sensitive premises receive higher validation priority.

---

# 73. Uncertainty Update Operator

Let:

[
U =
[
U_E,
U_M,
U_S,
U_T,
U_C,
U_X,
U_P
]
]

where:

```text
U_E = evidence uncertainty
U_M = model uncertainty
U_S = scope uncertainty
U_T = temporal uncertainty
U_C = causal uncertainty
U_X = execution uncertainty
U_P = provenance-independence uncertainty
```

Then:

[
\boxed{
O_U^{uncertainty}:
(U_t,E_{new})
\rightarrow
U_{t+1}
}
]

Uncertainty dimensions should not be collapsed into one scalar when their distinctions affect decisions.

---

# 74. Operator Risk Tensor

[
\boxed{
T_{OR}
======

T[
operator,
failure_probability,
impact,
consequence_radius,
irreversibility,
authority_risk,
scope_risk,
regime_risk,
epistemic_risk,
repairability
]
}
]

---

# 75. Consequence Radius

[
\boxed{
CR(O)
=====

f(
stateFanout,
dependencyFanout,
irreversibility,
stakeMagnitude,
authorityImpact
)
}
]

Higher consequence radius requires stronger validation and governance.

---

# 76. Operator Governance Tensor

[
\boxed{
T_G =
T[
operator,
capability,
authority,
principal,
policy,
constraints,
consequence_radius,
reversibility,
approval,
rollback,
evidence_threshold,
validation_epoch
]
}
]

---

# 77. Capability / Authority Firewall

```text
CAN EXECUTE != MAY EXECUTE

CAPABILITY != AUTHORITY

AUTHORITY != CORRECTNESS

AUTHORIZATION != SUCCESS

TOOL ACCESS != PERMISSION

PROPOSAL != COMMIT
```

---

# 78. Commit-Time Validation

For mutable environments:

[
\boxed{
Validate_{proposal}
\not\Rightarrow
Valid_{commit}
}
]

Therefore:

[
\boxed{
Commit(O)
\Rightarrow
Revalidate(
Authority,
Constraints,
RelevantState,
Dependencies
)
}
]

when these may have changed.

---

# 79. Atomic Operator Transaction

For semantically coupled operations:

[
\boxed{
Transaction(O_1,...,O_n)
========================

ALL
\lor
NONE
}
]

when partial completion would violate invariants.

---

# 80. Operator Transaction Tensor

[
\boxed{
T_{TX}
======

T[
transaction_id,
operators,
read_set,
write_set,
preconditions,
expected_versions,
authority,
constraints,
commit_state,
rollback,
provenance
]
}
]

---

# 81. AI Application — Perception Operators

AI systems may implement operators that transform:

```text
text
image
audio
sensor data
database state
tool output
user input
```

into internal representations.

Hard boundary:

```text
MODEL INTERPRETATION != RAW INPUT

RAW INPUT != EXTERNAL REALITY
```

unless the representation relationship is explicitly established.

---

# 82. AI Application — Retrieval Operators

```text
QUERY
  │
  ▼
SEARCH
  │
  ▼
CANDIDATE RESULTS
  │
  ▼
PROVENANCE RESOLUTION
  │
  ▼
SCOPE / REGIME CHECK
  │
  ▼
EVIDENCE ADMISSION
```

Retrieval score must not become truth score.

---

# 83. AI Application — Reasoning Operators

AI reasoning may use:

```text
decompose
compare
relate
infer
rank
simulate
counterfactualize
predict
synthesize
challenge
repair
```

These operators generate candidate reasoning state.

They do not independently create empirical evidence.

---

# 84. AI Application — Tool Operators

Tool invocation tensor:

[
\boxed{
T_{tool}
========

T[
tool,
operation,
arguments,
actor,
authority,
pre_state,
timestamp,
environment,
result,
post_state,
execution_status,
provenance
]
}
]

---

# 85. AI Application — Agent Operators

Agent operators should distinguish:

```text
THINK
READ
RETRIEVE
PROPOSE
REQUEST
AUTHORIZE
WRITE
EXECUTE
COMMIT
ROLLBACK
```

A worker capable of generating an action proposal should not automatically own the commit boundary.

---

# 86. AI Application — Model Worker / Control Plane Separation

```text
MODEL WORKER
    │
    ├── observe
    ├── infer
    ├── model
    ├── rank
    ├── propose
    └── explain
         │
         ▼
CONTROL PLANE
    │
    ├── validate
    ├── authorize
    ├── constrain
    ├── commit
    ├── audit
    └── rollback
```

Hard invariant:

```text
COGNITION != CONTROL
```

---

# 87. AI Application — Self-Modification

Any operator capable of modifying:

```text
policy
memory
skill
prompt
tool authority
architecture
governance
persistent model state
```

must be treated as a mutation operator.

[
\boxed{
O_{\mu}:
System_t
\rightarrow
System_{t+1}
}
]

Mutation requires stronger governance than ordinary inference.

---

# 88. Mutation Tensor

[
\boxed{
T_{\mu}
=======

T[
target,
mutation_class,
proposal,
expected_effect,
dependencies,
authority,
evidence,
risk,
reversibility,
validation,
rollback,
provenance
]
}
]

---

# 89. AI Application — Learning Operator

[
\boxed{
O_L:
SystemState
\times
Feedback
\rightarrow
CandidateUpdatedState
}
]

Learning does not imply improvement.

```text
UPDATE != IMPROVEMENT

ADAPTATION != ALIGNMENT

LOWER LOSS != HIGHER INTEGRITY
```

---

# 90. Anti-Feedback-Bias Operator

Before feedback modifies persistent policy or memory:

[
\boxed{
O_{AFB}:
Feedback
\rightarrow
FeedbackValidity
}
]

checks may include:

```text
source independence
selection bias
reward hacking
recursive contamination
scope validity
regime validity
adversarial manipulation
```

---

# 91. Operator Failure Modes

## OP-F01 — Type Collapse

Output is consumed as the wrong semantic type.

## OP-F02 — Scope Leakage

Operator output is reused outside its validated scope.

## OP-F03 — Regime Leakage

Operator assumptions fail after regime change.

## OP-F04 — Provenance Loss

Transformation lineage disappears.

## OP-F05 — Causal Promotion Error

Correlation or structure becomes causal claim.

## OP-F06 — Representation Reification

Model or simulation state becomes treated as reality.

## OP-F07 — Unauthorized Effect

Capability bypasses authority.

## OP-F08 — Stale Commit

Operation commits against obsolete state.

## OP-F09 — Partial Transaction

Only part of a coupled operation commits.

## OP-F10 — Non-Commutative Reordering

Operator order changes semantics unnoticed.

## OP-F11 — Hidden Information Loss

Compression or transformation destroys load-bearing information.

## OP-F12 — Invalid Aggregation

Incompatible observations are combined.

## OP-F13 — Observer Collapse

Observer-specific output becomes universalized.

## OP-F14 — False Independence

Shared-ancestry evidence is treated as independent.

## OP-F15 — Irreversible Mutation

High-impact state changes without rollback.

## OP-F16 — Repair Overreach

Repair changes unrelated valid state.

## OP-F17 — Validation Collapse

Successful execution becomes proof of correctness.

## OP-F18 — Unknown Promotion

`UNKNOWN/GAP` becomes `PASS`.

---

# 92. Failure Recovery

When operator (O_i) fails:

```text
1. identify failed operator;

2. identify earliest invalid precondition;

3. identify affected state;

4. identify dependent downstream operations;

5. freeze or quarantine unsafe descendants;

6. preserve independent valid state;

7. repair the smallest causal failure;

8. re-run validation;

9. replay only affected operations;

10. verify postconditions;

11. restore operation only if invariants pass.
```

---

# 93. Recovery Equation

Let:

* (S_V) = unaffected valid state;
* (S_F) = failed state;
* (D_F) = dependent state;
* (R_F) = repaired state.

Then:

[
\boxed{
S_{recovered}
=============

S_V
\cup
R_F
\cup
Revalidated(D_F)
}
]

Global recomputation is last resort.

---

# 94. Operator Audit Record

```yaml
operator_record:

  operator_id:

  class:

  actor:

  objective:

  input:

  input_type:

  pre_state:

  read_set: []

  write_set: []

  scope:

  regime:

  HML_scale:

  observer:

  timestamp:

  authority:

  constraints: []

  output:

  output_type:

  post_state:

  evidence: []

  provenance: []

  falsifiers: []

  reversibility:

  rollback:

  execution_status:

  validation_status:
```

---

# 95. Skill Operator Contract

Every AMOS skill exposing operators should declare:

```yaml
operator_contract:

  operators: []

  reads: []

  writes: []

  input_types: []

  output_types: []

  preconditions: []

  invariants: []

  scope:

  regime:

  authority_requirements: []

  provenance_requirements: []

  consequence_radius:

  reversibility:

  commit_boundary:

  rollback:

  validators: []

  falsifiers: []
```

---

# 96. Agent Operator Contract

```yaml
agent_operator_contract:

  agent:

  allowed_operations: []

  prohibited_operations: []

  read_scope: []

  write_scope: []

  proposal_authority:

  commit_authority:

  external_effect_authority:

  memory_authority:

  mutation_authority:

  escalation_conditions: []

  rollback_capability:

  audit_required: true
```

---

# 97. Operator Workflow

```text
OBJECTIVE
   │
   ▼
SELECT OPERATOR
   │
   ▼
TYPE CHECK
   │
   ▼
DEPENDENCY CHECK
   │
   ▼
SCOPE CHECK
   │
   ▼
REGIME CHECK
   │
   ▼
PROVENANCE CHECK
   │
   ▼
PRECONDITION CHECK
   │
   ▼
AUTHORITY CHECK
   │
   ▼
EXECUTE / PROPOSE
   │
   ▼
POSTCONDITION CHECK
   │
   ▼
INVARIANT CHECK
   │
   ▼
COMMIT
   │
   ▼
OBSERVE RESULT
   │
   ▼
AUDIT
```

---

# 98. Core Operator Invariants

## OP-I01 — Typed Transformation

Every consequential operator must have identifiable input and output semantics.

## OP-I02 — Provenance Preservation

Transformation must not erase load-bearing source lineage.

## OP-I03 — Scope Preservation

Operator output inherits applicable scope constraints.

## OP-I04 — Regime Preservation

Operator output inherits applicable regime constraints.

## OP-I05 — Observer Preservation

Observer-dependent results remain observer-dependent.

## OP-I06 — Temporal Preservation

Operation time does not replace event time.

## OP-I07 — Representation Preservation

Simulation/model/forecast output remains correctly typed.

## OP-I08 — Causal Firewall

Noncausal operators cannot silently produce causal conclusions.

## OP-I09 — Capability / Authority Separation

Execution capability does not establish authorization.

## OP-I10 — Proposal / Commit Separation

Proposal does not create durable effect.

## OP-I11 — Commit Freshness

Mutable load-bearing state must be current at commit.

## OP-I12 — Selective Failure Propagation

Failure invalidates dependent descendants, not unrelated state.

## OP-I13 — Contradiction Visibility

Operators may not erase unresolved competing evidence.

## OP-I14 — Information-Loss Visibility

Material transformation loss must remain detectable.

## OP-I15 — UNKNOWN Preservation

Unknown states cannot silently become successful states.

---

# 99. Validators

```text
L00-OP-T01 operator type validation
L00-OP-T02 input/output compatibility
L00-OP-T03 provenance preservation
L00-OP-T04 scope preservation
L00-OP-T05 regime preservation
L00-OP-T06 observer preservation
L00-OP-T07 temporal preservation
L00-OP-T08 causal promotion gate
L00-OP-T09 representation-class preservation
L00-OP-T10 composition compatibility
L00-OP-T11 operator-order sensitivity
L00-OP-T12 information-loss detection
L00-OP-T13 H/M/L propagation
L00-OP-T14 capability/authority separation
L00-OP-T15 proposal/commit separation
L00-OP-T16 commit-time freshness
L00-OP-T17 transaction atomicity
L00-OP-T18 selective invalidation
L00-OP-T19 rollback integrity
L00-OP-T20 mutation governance
L00-OP-T21 recursive contamination
L00-OP-T22 contradiction preservation
L00-OP-T23 independence validation
L00-OP-T24 UNKNOWN/GAP preservation
L00-OP-T25 postcondition validation
```

---

# 100. Falsifiers

This architecture is falsified as an implemented L00 operator system if:

1. operators have no stable semantic type;
2. outputs cannot be traced to inputs;
3. provenance disappears through transformations;
4. scope constraints disappear after operations;
5. regime constraints disappear after operations;
6. simulation outputs can silently become observations;
7. correlation can silently become causation;
8. operator order is ignored where order changes semantics;
9. irreversible operations require no additional governance;
10. capability automatically grants authority;
11. proposals automatically create durable effects;
12. commit occurs against stale mutable state;
13. semantic transactions can partially commit despite atomicity requirements;
14. local failure forces unnecessary destruction of independent valid state;
15. contradictions disappear during aggregation;
16. shared-source evidence becomes falsely independent;
17. operator-generated information recursively validates itself;
18. model updates are automatically classified as improvements;
19. successful execution is treated as semantic validation;
20. `UNKNOWN/GAP` can become `PASS` without evidence.

---

# 101. Gap Matrix

| Area              | Required capability         | Status                   |
| ----------------- | --------------------------- | ------------------------ |
| Operator registry | typed operator identities   | implementation-dependent |
| Type system       | input/output validation     | implementation-dependent |
| Provenance        | transformation lineage      | implementation-dependent |
| Scope             | operator applicability      | implementation-dependent |
| Regime            | regime-aware execution      | implementation-dependent |
| H/M/L             | cross-scale operators       | implementation-dependent |
| Causality         | causal promotion gates      | implementation-dependent |
| Observer          | observer-aware state        | implementation-dependent |
| Temporal          | event/execution/commit time | implementation-dependent |
| Composition       | compatibility validation    | implementation-dependent |
| Authority         | effect authorization        | implementation-dependent |
| Commit            | freshness revalidation      | implementation-dependent |
| Transactions      | atomic operations           | implementation-dependent |
| Rollback          | recovery path               | implementation-dependent |
| Mutation          | governed self-change        | implementation-dependent |
| Audit             | replayable operation record | implementation-dependent |

---

# 102. Operator Algebra

For operator set:

[
\mathcal{O}
===========

{
O_1,O_2,...,O_n
}
]

AMOS operator composition forms a typed partial algebra:

[
\boxed{
O_j \circ O_i
}
]

exists only when:

[
\boxed{
Compatible(
Output(O_i),
Input(O_j),
Scope,
Regime,
Authority,
Constraints
)
}
]

Therefore operator composition is not universally closed.

---

# 103. Operator State Equation

The generalized L00 transition is:

[
\boxed{
S_{t+1}
=======

\Phi_O(
S_t,
X_t,
O_t,
C_t,
G_t
)
}
]

where:

```text
S = current state
X = external/internal input
O = selected operator
C = context/environment
G = governance constraints
```

`Φ_O` is an AMOS architectural transition model.

---

# 104. Evidence-Producing Operator Equation

[
\boxed{
E_{t+1}
=======

O_E(
S_t,
ObservationMethod,
MeasurementMethod,
Provenance
)
}
]

Evidence generated by an operator remains bounded by the operator's observation and measurement envelope.

---

# 105. Governed Action Equation

[
\boxed{
ActionAllowed
=============

Capability
\land
Authority
\land
ConstraintPass
\land
EvidenceThresholdPass
\land
StateFresh
}
]

for actions requiring all such conditions.

---

# 106. Reality Interaction Equation

The complete conceptual loop is:

[
\boxed{
R_t
\xrightarrow{Observe}
O_t
\xrightarrow{Measure}
E_t
\xrightarrow{Infer}
C_t
\xrightarrow{Model}
M_t
\xrightarrow{Decide}
D_t
\xrightarrow{Authorize}
A_t
\xrightarrow{Commit}
X_t
\xrightarrow{Act}
R_{t+1}
}
]

followed by:

[
\boxed{
R_{t+1}
\xrightarrow{Observe}
Outcome
\xrightarrow{Evaluate}
Update
}
]

This is an architectural reasoning loop, not a universal physical law.

---

# 107. RSCF Completion State

```yaml
claim_class: MODEL

evidence:
  - AMOS reality/representation distinction
  - AMOS typed tensor architecture
  - AMOS relation architecture
  - AMOS causal firewall
  - AMOS H/M/L architecture
  - AMOS provenance topology
  - AMOS selective invalidation architecture
  - AMOS control-plane architecture

provenance:
  origin_architect: Trang Phan
  architecture_family: AMOS
  layer: L00_REALITY_ENVIRONMENT
  component: OPERATORS

scope:
  applies_to:
    - observation
    - measurement
    - classification
    - transformation
    - inference
    - validation
    - modeling
    - simulation
    - prediction
    - memory
    - retrieval
    - agent operations
    - tool operations
    - decisions
    - governed actions
    - repair
    - rollback

regime:
  - AI reasoning systems
  - agent systems
  - simulation systems
  - evidence systems
  - mutable environments
  - governed control planes

freshness:
  state_sensitive: true
  regime_sensitive: true
  commit_time_revalidation_for_mutable_dependencies: true

dependencies:
  - L00_REALITY_ENVIRONMENT/DEFINITION
  - L00_REALITY_ENVIRONMENT/DEPENDENCIES
  - L00_REALITY_ENVIRONMENT/EQUATIONS
  - L00_REALITY_ENVIRONMENT/HML
  - L00_REALITY_ENVIRONMENT/INVARIANTS
  - L00_REALITY_ENVIRONMENT/MEMORY
  - L00_REALITY_ENVIRONMENT/CONTROL_PLANES
  - L00_REALITY_ENVIRONMENT/FAILURE_MODES
  - L00_REALITY_ENVIRONMENT/GAP_MATRIX
  - typed tensor contracts
  - claim tensor
  - evidence tensor
  - relation tensor
  - provenance topology
  - causal hierarchy
  - constraint propagation
  - governance

competing:
  - untyped function pipelines
  - model-owned execution control
  - provenance-free transformations
  - relevance-only retrieval
  - unrestricted operator composition
  - global rollback after local failure

falsifiers:
  - operator types cannot be preserved
  - provenance cannot survive transformations
  - scope/regime cannot propagate
  - effect authority cannot be separated from capability
  - state freshness cannot be checked
  - dependent failures cannot be selectively invalidated
  - representation classes cannot remain distinct

confidence_ceiling:
  architecture_contract: high
  implementation_status: unknown_without_runtime_evidence
  empirical_universality: unverified
  ontological_universality: unverified
```

---

# 108. Hard Boundaries

```text
OPERATOR != RESULT

RESULT != TRUTH

OBSERVATION != REALITY

MEASUREMENT != UNDERLYING STATE

LABEL != ENTITY

CLASS != ESSENCE

RELATION != CAUSATION

CORRELATION != CAUSATION

SEQUENCE != CAUSATION

SIMILARITY != CAUSATION

MODEL != REALITY

SIMULATION != DEPLOYMENT

COUNTERFACTUAL != HISTORY

FORECAST != OUTCOME

ESTIMATE != OBSERVATION

RETRIEVED != VALIDATED

SELECTED != TRUE

AGGREGATE != COMPONENT

SUMMARY != SOURCE

TRANSLATION != PERFECT EQUIVALENCE

CAPABILITY != AUTHORITY

PROPOSAL != AUTHORIZATION

AUTHORIZATION != COMMIT

COMMIT != EXECUTION SUCCESS

ACTION != OUTCOME

UPDATE != IMPROVEMENT

ADAPTATION != ALIGNMENT

REPAIR != VERIFIED RECOVERY

ROLLBACK != AUTOMATIC VALIDITY

LOCAL SUCCESS != GLOBAL VALIDITY

H != M != L

SHARED SOURCE != INDEPENDENT SUPPORT

UNKNOWN != FALSE

UNKNOWN/GAP != PASS
```

---

# 109. Canonical Operator Law

[
\boxed{
ValidOperatorExecution
======================

TypedInput
\land
ValidPreconditions
\land
ScopeCompatibility
\land
RegimeCompatibility
\land
DependencyValidity
\land
ConstraintCompliance
\land
RequiredAuthority
\land
ProvenancePreservation
}
]

For effectful execution:

[
\boxed{
Proposal
\rightarrow
Validation
\rightarrow
Authorization
\rightarrow
Commit
\rightarrow
Action
\rightarrow
OutcomeObservation
}
]

For epistemic execution:

[
\boxed{
Observation
\rightarrow
Evidence
\rightarrow
Inference
\rightarrow
Claim
}
]

with representation classes preserved.

For failure:

[
\boxed{
OperatorFailure
\Rightarrow
Invalidate(DependentState)
+
Preserve(IndependentState)
+
Repair(SmallestCausalFailure)
}
]

For composition:

[
\boxed{
Compose(O_i,O_j)
\iff
TypeCompatible
\land
ScopeCompatible
\land
RegimeCompatible
\land
ConstraintCompatible
}
]

For AI:

[
\boxed{
Cognition
\neq
Authority
\neq
Commit
\neq
ExternalEffect
}
]

The central architectural rule is:

> **AMOS operators must transform state without erasing the semantic type, provenance, scope, regime, temporal context, dependencies, authority conditions, uncertainty, or invalidation structure required to interpret the transformation. An operator may generate a representation, inference, proposal, or effect; it may never silently promote that output into reality, causality, validation, authority, or successful outcome.**

---

**Related:** [[00-Home]] · [[06-Knowledge-Base-MOC]] · [[L00_REALITY_ENVIRONMENT — Definition]] · [[L00_REALITY_ENVIRONMENT — Dependencies]] · [[L00_REALITY_ENVIRONMENT — Equations]] · [[L00_REALITY_ENVIRONMENT — Hml]] · [[L00_REALITY_ENVIRONMENT — Invariants]] · [[L00_REALITY_ENVIRONMENT — Memory]] · [[L00_REALITY_ENVIRONMENT — Control Planes]] · [[L00_REALITY_ENVIRONMENT — Failure Modes]] · [[L00_REALITY_ENVIRONMENT — Gap Matrix]] · [[AMOS_Typed_Tensor_Contracts]] · [[AMOS_Evidence_Tensor_Architecture]] · [[AMOS_Claim_Tensor_Architecture]] · [[AMOS_Relation_Tensor_Architecture]] · [[AMOS_Reality_Simulation_Distinction]] · [[AMOS_Constraint_Propagation]] · [[AMOS_Causal_Hierarchy_Governor]] · [[AMOS_Infrastructure_Control_Plane]]

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
