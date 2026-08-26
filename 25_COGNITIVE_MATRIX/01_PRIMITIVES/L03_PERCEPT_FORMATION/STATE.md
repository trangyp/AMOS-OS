---
tags:
  - amos
  - cognitive-matrix
  - l03
  - percept-formation
  - state
  - rscf
  - provenance
  - governance

title: "L03_PERCEPT_FORMATION — State"
origin_architect: "Trang Phan"
status: "MODEL_STATE_CONTRACT / UNIMPLEMENTED / UNVALIDATED"
epistemic_class: "MODEL"
runtime_alignment: "AMOS Full Brain OS / AMOS_CORE v4.4 lineage"
---

# L03_PERCEPT_FORMATION — State

**Class:** `COGNITIVE_PRIMITIVE_STATE_CONTRACT`  
**Origin architect / steward:** Trang Phan  
**Primitive:** `L03_PERCEPT_FORMATION`  
**Artifact:** `STATE.md`  
**Status:** `AMOS_MODEL / UNIMPLEMENTED / UNVALIDATED`

## 0. Purpose

Define the governed state contract for `L03_PERCEPT_FORMATION`.

The L03 state layer represents the bounded, typed, provenance-aware state required to transform admitted observations and attention state into candidate percept structures without silently converting salience, memory, interpretation, binding, aggregation, or model output into observed truth.

AMOS architecture requires state to remain typed. The Skill Builder defines the canonical reasoning tensor as:

```text
X = T[
  object,
  primitive,
  scale,
  time,
  regime,
  observer,
  provenance,
  epistemic_class,
  confidence,
  consequence
]
```

and explicitly states that tensor axes are non-interchangeable and that `UNKNOWN` is not equivalent to false, zero, absent, or contradicted.

The continuity architecture separately requires objective, execution, artifact, and persistence state to remain distinct and requires explicit statuses such as `COMPLETED`, `ACTIVE`, `BLOCKED`, `FAILED`, and `NOT_STARTED`.

Core boundary:

```text
STATE != REALITY

OBSERVATION != PERCEPT

ATTENTION != TRUTH

FEATURE != OBJECT

RELATION != CAUSATION

BINDING != IDENTITY

MEMORY != CURRENT OBSERVATION

CANDIDATE != ACCEPTED PERCEPT

ACCEPTED PERCEPT != EXTERNAL FACT

STATE TRANSITION != DURABLE COMMIT

PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

UNKNOWN/GAP != PASS
```

---

# 1. Source / Canon References

## 1.1 Source-aligned AMOS state principles

The AMOS Skill Builder requires:

```text
structure before prose
typed state
explicit dependencies
explicit scope
explicit regime
explicit provenance
explicit epistemic class
explicit confidence
explicit consequence
hard invariant admission
smallest sufficient dependency closure
selective repair
```

It models claim state as:

```text
CLAIM[
  id,
  class,
  premise,
  dependency,
  scope,
  regime,
  falsifier,
  status
]
```

and system state as:

```text
SYS[
  component,
  interface,
  dependency,
  data_contract,
  config,
  resource,
  runtime,
  policy,
  owner,
  risk,
  provenance
]
```

The AMOS Context Continuity Governor additionally requires maintained state of the form:

```text
STATE[
  objective,
  lock_hash,
  scope,
  constraints,
  non_goals,
  completed,
  active,
  blocked,
  failed_paths,
  retry_conditions,
  gaps,
  artifacts,
  lineage,
  last_user_intent,
  last_decision,
  next_valid_actions,
  status
]
```

and requires failed actions to change the plan rather than silently changing the governing objective.

## 1.2 Related architecture families

Relevant architecture dependencies include:

```text
AMOS Cognition
AMOS Full Brain OS
AMOS Multimodal Perception Layer
AMOS Attention Allocation Governor
AMOS Binding Architecture
AMOS Distinction Architecture
AMOS Information Operator Engine
AMOS H/M/L
AMOS RSCF
AMOS Provenance
AMOS Memory Governance
AMOS Constraint Propagation
AMOS Infrastructure Control Plane
AMOS Deterministic AI Control Plane
```

## 1.3 Direct L03 state canon status

```yaml
canonical_L03_state_schema: UNKNOWN_GAP
canonical_state_variable_names: UNKNOWN_GAP
canonical_state_transition_table: UNKNOWN_GAP
canonical_acceptance_thresholds: UNKNOWN_GAP
canonical_percept_representation: UNKNOWN_GAP
canonical_state_persistence_semantics: UNKNOWN_GAP
canonical_commit_semantics: UNKNOWN_GAP
```

Therefore all L03-specific state structures introduced below remain `AMOS_MODEL` unless separately source-bound.

---

# 2. Definition and Scope

`L03_PERCEPT_FORMATION_STATE` is the typed working state describing the current condition of percept construction.

It may contain:

```text
admitted observations
attention allocation
feature hypotheses
relation hypotheses
binding hypotheses
candidate percepts
competing percepts
H/M/L representations
memory/context references
provenance
dependency lineage
scope/regime state
freshness
uncertainty
confidence ceilings
validation state
repair state
```

It does **not** establish that the percept corresponds to external reality.

Candidate abstraction:

[
S^{L03}_t =
(
O_t,
A_t,
F_t,
R_t,
B_t,
P_t,
C_t,
HML_t,
M_t,
Prov_t,
Dep_t,
U_t,
V_t
)
]

where the variables are typed state components defined below.

`AMOS_MODEL`.

---

# 3. Governing State Separation

L03 must preserve at least four distinct state domains:

```text
1. SOURCE / OBSERVATION STATE
2. WORKING PERCEPT STATE
3. EXECUTION / VALIDATION STATE
4. PERSISTENCE / COMMIT STATE
```

Candidate separation:

```text
ObservationState
      ↓
WorkingPerceptState
      ↓
ValidationState
      ↓
PerceptProposal
      ↓
Control-plane decision
      ↓
CommittedState
```

Hard invariant:

```text
WorkingPerceptState
!=
CommittedState
```

This follows the broader AMOS continuity requirement that conversation, runtime, artifact, and persistence state remain distinct.

---

# 4. Top-Level Typed State

```yaml
L03PerceptFormationState:

  state_id:
    type: StateID

  primitive:
    const: L03_PERCEPT_FORMATION

  version:
    type: VersionRef

  lifecycle_status:
    type:
      - NOT_STARTED
      - ACTIVE
      - BLOCKED
      - FAILED
      - CONDITIONAL
      - COMPETING
      - COMPLETED
      - INVALIDATED
      - QUARANTINED
      - UNKNOWN_GAP

  observations:
    type: ObservationState[]

  attention:
    type: AttentionState

  features:
    type: FeatureState[]

  relations:
    type: RelationState[]

  bindings:
    type: BindingState[]

  percept_candidates:
    type: PerceptCandidate[]

  competing_percepts:
    type: CompetingPerceptSet[]

  selected_percept:
    type: PerceptCandidate | null

  HML:
    type: HMLPerceptState

  memory_context:
    type: MemoryContext[]

  provenance:
    type: ProvenanceGraph

  dependencies:
    type: DependencyGraph

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeEnvelope

  freshness:
    type: FreshnessState

  uncertainty:
    type: UncertaintyVector

  confidence_ceiling:
    type: ConfidenceBound

  validation:
    type: ValidationState

  repair:
    type: RepairState

  authority:
    type: AuthorityState

  persistence:
    type: PersistenceState
```

---

# 5. Typed Inputs

```yaml
L03StateInput:

  observation_refs:
    type: ObservationRef[]
    source: L01_SENSING_OBSERVATION

  attention_state:
    type: AttentionState
    source: L02_ATTENTION

  memory_context:
    type: MemoryContext[]
    optional: true

  observer_context:
    type: ObserverContext

  temporal_context:
    type: TemporalContext

  spatial_context:
    type: SpatialContext | null

  HML_context:
    type: HMLContext

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeEnvelope

  provenance:
    type: ProvenanceGraph

  constraints:
    type: ConstraintSet

  authority_context:
    type: AuthorityContext
```

Input admission condition:

[
InputAdmissible
===============

TypeValid
\land
ScopeValid
\land
RegimeValid
\land
ProvenanceSufficient
\land
HardConstraintsPass
]

`AMOS_MODEL`.

Failure of a load-bearing hard condition yields:

```text
BLOCKED
FAIL
QUARANTINED
or
UNKNOWN/GAP
```

—not implicit acceptance.

---

# 6. Typed Outputs

```yaml
L03StateOutput:

  state_ref:
    type: StateRef

  candidate_percepts:
    type: PerceptCandidate[]

  selected_candidate:
    type: PerceptCandidate | null

  competing:
    type: CompetingPerceptSet[]

  HML_state:
    type: HMLPerceptState

  provenance:
    type: ProvenanceGraph

  dependencies:
    type: DependencyGraph

  uncertainty:
    type: UncertaintyVector

  confidence_ceiling:
    type: ConfidenceBound

  validation:
    type: ValidationResult

  repair_requirements:
    type: RepairRequirement[]

  proposal:
    type: PerceptStateProposal | null

  commit_authority:
    const: NONE
```

---

# 7. Core State Variables

```text
O_t      = admitted observation state
A_t      = attention allocation state

F_t      = feature state
R_t      = relation state
B_t      = binding state

P_t      = percept candidate state
C_t      = competing percept state

H_t      = H-level percept state
M_t      = M-level percept state
L_t      = L-level percept state

Mem_t    = memory/context state

Prov_t   = provenance graph
Dep_t    = dependency graph

Scope_t  = applicability scope
Reg_t    = operating regime
Fresh_t  = freshness state

U_t      = uncertainty vector
Conf_t   = confidence ceiling

Inv_t    = invariant state
Val_t    = validation state

Fail_t   = failure state
Rep_t    = repair state

Auth_t   = authority state
Persist_t = persistence state

Epoch_t  = state epoch/version
```

---

# 8. Observation State

```yaml
ObservationState:

  observation_id:
    type: ObservationID

  source_ref:
    type: SourceRef

  modality:
    type: ModalityRef

  value:
    type: ObservationPayload

  measurement_context:
    type: MeasurementContext

  observed_at:
    type: Timestamp | null

  received_at:
    type: Timestamp

  observer:
    type: ObserverRef

  provenance:
    type: ProvenanceRef

  epistemic_class:
    const: OBSERVATION

  uncertainty:
    type: UncertaintyState

  freshness:
    type: FreshnessState
```

Invariant:

```text
ObservationState
MUST NOT
be rewritten into interpretation state.
```

If normalization occurs, the original observation reference remains preserved.

---

# 9. Attention State

```yaml
AttentionState:

  allocation_id:
    type: StateID

  target_refs:
    type: StateRef[]

  weights:
    type: AttentionWeight[]

  selection_basis:
    type:
      - SALIENCE
      - GOAL
      - NOVELTY
      - THREAT
      - UNCERTAINTY
      - TIME_SENSITIVITY
      - USER_DIRECTIVE
      - CONTROL_POLICY
      - OTHER

  scope:
    type: ScopeEnvelope

  provenance:
    type: ProvenanceGraph

  uncertainty:
    type: UncertaintyState
```

Hard boundary:

```text
AttentionWeight(x) > AttentionWeight(y)
DOES NOT IMPLY
Truth(x) > Truth(y)
```

---

# 10. Feature State

```yaml
FeatureState:

  feature_id:
    type: FeatureID

  source_refs:
    type: ObservationRef[]

  feature_type:
    type: FeatureType

  representation:
    type: FeatureRepresentation

  scale:
    type: HMLScale

  temporal_extent:
    type: TemporalExtent

  spatial_extent:
    type: SpatialExtent | null

  provenance:
    type: ProvenanceGraph

  epistemic_class:
    type:
      - OBSERVATION_DERIVED
      - MODEL
      - UNKNOWN_GAP

  uncertainty:
    type: UncertaintyState

  confidence_ceiling:
    type: ConfidenceBound
```

Boundary:

```text
FEATURE DETECTED
!=
OBJECT ESTABLISHED
```

---

# 11. Relation State

```yaml
RelationState:

  relation_id:
    type: RelationID

  source_nodes:
    type: StateRef[]

  relation_type:
    type:
      - TEMPORAL
      - SPATIAL
      - SIMILARITY
      - CONTRAST
      - CONTAINMENT
      - ADJACENCY
      - CO_OCCURRENCE
      - TRANSFORMATION
      - CAUSAL_CANDIDATE
      - UNKNOWN

  direction:
    type:
      - DIRECTED
      - UNDIRECTED
      - UNKNOWN

  provenance:
    type: ProvenanceGraph

  epistemic_class:
    type:
      - OBSERVATION_DERIVED
      - MODEL
      - COMPETING
      - UNKNOWN_GAP

  uncertainty:
    type: UncertaintyState
```

Causal firewall:

```text
CO_OCCURRENCE != CAUSATION

TEMPORAL PRECEDENCE != CAUSATION

SPATIAL ADJACENCY != CAUSATION

RELATIONAL FIT != MECHANISM
```

---

# 12. Binding State

```yaml
BindingState:

  binding_id:
    type: BindingID

  member_refs:
    type: StateRef[]

  binding_basis:
    type:
      - SPATIAL
      - TEMPORAL
      - FEATURE_SIMILARITY
      - CONTINUITY
      - COMMON_SOURCE
      - MODEL_INFERENCE
      - OTHER

  strength:
    type: BoundedScore | null

  alternatives:
    type: BindingCandidate[]

  provenance:
    type: ProvenanceGraph

  uncertainty:
    type: UncertaintyState

  status:
    type:
      - PROPOSED
      - CONDITIONAL
      - COMPETING
      - ACCEPTED_FOR_WORKING_STATE
      - REJECTED
      - UNKNOWN_GAP
```

Hard boundary:

```text
BOUND TOGETHER
!=
SAME ENTITY
```

---

# 13. Percept Candidate State

```yaml
PerceptCandidate:

  percept_id:
    type: PerceptID

  feature_refs:
    type: FeatureRef[]

  relation_refs:
    type: RelationRef[]

  binding_refs:
    type: BindingRef[]

  observation_refs:
    type: ObservationRef[]

  memory_refs:
    type: MemoryRef[]

  HML:
    type: HMLCoordinate

  interpretation:
    type: PerceptRepresentation

  epistemic_class:
    type:
      - DERIVED
      - MODEL
      - COMPETING
      - UNKNOWN_GAP

  provenance:
    type: ProvenanceGraph

  dependencies:
    type: DependencyGraph

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeEnvelope

  uncertainty:
    type: UncertaintyVector

  confidence_ceiling:
    type: ConfidenceBound

  status:
    type:
      - CANDIDATE
      - CONDITIONAL
      - COMPETING
      - ACCEPTED_FOR_WORKING_STATE
      - REJECTED
      - INVALIDATED
      - UNKNOWN_GAP
```

---

# 14. Competing Percept State

```yaml
CompetingPerceptSet:

  set_id:
    type: CompetitionID

  candidates:
    type: PerceptRef[]

  discriminating_variables:
    type: VariableRef[]

  discriminating_tests:
    type: TestRef[]

  shared_evidence:
    type: EvidenceRef[]

  independent_evidence:
    type: EvidenceRef[]

  unresolved_conflicts:
    type: ConflictRef[]

  status:
    type:
      - ACTIVE_COMPETITION
      - PARTIALLY_RESOLVED
      - RESOLVED
      - UNKNOWN_GAP
```

Invariant:

```text
NO UNIQUE WINNER
→
PRESERVE COMPETING
```

Absence of contradiction is not sufficient to collapse competing percepts.

---

# 15. H/M/L State

```yaml
HMLPerceptState:

  H:
    type: HighLevelPerceptState

  M:
    type: MidLevelPerceptState[]

  L:
    type: LowLevelPerceptState[]

  upward_dependencies:
    type: DependencyEdge[]

  downward_constraints:
    type: ConstraintEdge[]

  unresolved_cross_scale_conflicts:
    type: ConflictRef[]

  provenance:
    type: ProvenanceGraph
```

Candidate semantics:

```text
L
local features / local relations / local bindings

M
objects / events / intermediate structures

H
scene / governing interpretation / global percept organization
```

Hard boundaries:

```text
L AGREEMENT != H TRUTH

H EXPECTATION != L OBSERVATION

HYPOTHESIS AT H
MUST NOT
REWRITE SOURCE STATE AT L
```

---

# 16. Memory State

```yaml
MemoryContext:

  memory_id:
    type: MemoryID

  content_ref:
    type: StateRef

  memory_class:
    type:
      - FACTUAL
      - EPISODIC
      - EXPERIENTIAL
      - WORKING
      - MODEL_DERIVED
      - UNKNOWN

  source_time:
    type: Timestamp | null

  retrieval_time:
    type: Timestamp

  provenance:
    type: ProvenanceGraph

  freshness:
    type: FreshnessState

  applicability:
    type: ScopeEnvelope

  uncertainty:
    type: UncertaintyState
```

Invariant:

```text
MEMORY-CARRIED INFORMATION
MUST REMAIN DISTINGUISHABLE FROM
CURRENT OBSERVATION
```

---

# 17. Provenance State

```yaml
ProvenanceState:

  graph_id:
    type: ProvenanceGraphID

  source_nodes:
    type: SourceNode[]

  derivation_nodes:
    type: DerivationNode[]

  transformation_edges:
    type: TransformationEdge[]

  shared_ancestry:
    type: AncestryRelation[]

  independence_status:
    type:
      - INDEPENDENT
      - CORRELATED
      - SHARED_ANCESTRY
      - UNKNOWN

  unresolved_origin:
    type: SourceRef[]
```

Invariant:

```text
MULTIPLE DESCENDANTS
OF ONE SOURCE
!=
MULTIPLE INDEPENDENT SOURCES
```

---

# 18. Dependency State

```yaml
DependencyState:

  nodes:
    type: StateRef[]

  edges:
    type: DependencyEdge[]

  load_bearing:
    type: StateRef[]

  optional:
    type: StateRef[]

  invalidated:
    type: StateRef[]

  stale:
    type: StateRef[]

  unresolved:
    type: StateRef[]
```

Candidate dependency rule:

[
Invalidate(x)
\Rightarrow
Invalidate(Descendants_{load-bearing}(x))
]

while unrelated state remains preserved.

`AMOS_MODEL`.

---

# 19. Scope / Regime State

```yaml
ApplicabilityState:

  system:
    type: SystemRef

  environment:
    type: EnvironmentRef

  observer:
    type: ObserverRef

  modality:
    type: ModalityRef[]

  scale:
    type: HMLScale[]

  time_window:
    type: TemporalEnvelope

  regime:
    type: RegimeRef

  assumptions:
    type: AssumptionRef[]
```

Any percept candidate inherits its applicability envelope from load-bearing dependencies unless independently revalidated.

---

# 20. Freshness State

```yaml
FreshnessState:

  observed_at:
    type: Timestamp | null

  validated_at:
    type: Timestamp | null

  epoch:
    type: EpochRef

  expiry_condition:
    type: Predicate[]

  stale:
    type: boolean

  stale_reason:
    type: string | null
```

Hard boundary:

```text
PREVIOUSLY VALID
!=
CURRENTLY VALID
```

---

# 21. Uncertainty State

```yaml
L03UncertaintyVector:

  observation:
    type: BoundedUncertainty

  attention:
    type: BoundedUncertainty

  feature:
    type: BoundedUncertainty

  binding:
    type: BoundedUncertainty

  interpretation:
    type: BoundedUncertainty

  memory:
    type: BoundedUncertainty

  scope:
    type: BoundedUncertainty

  temporal:
    type: BoundedUncertainty

  causal:
    type: BoundedUncertainty

  provenance_independence:
    type: BoundedUncertainty

  execution:
    type: BoundedUncertainty
```

Uncertainty dimensions shall not be silently collapsed into one scalar when doing so would erase decision-relevant distinctions.

---

# 22. Confidence Ceiling State

Candidate load-bearing rule:

[
Conf(P)
\leq
\min_{x \in LB(P)} Conf(x)
]

unless an affected premise has been independently revalidated.

`AMOS_MODEL`.

Therefore:

```text
MORE FEATURES
!=
AUTOMATICALLY MORE CONFIDENCE

MORE AGENTS
!=
AUTOMATICALLY MORE CONFIDENCE

MORE SKILLS
!=
AUTOMATICALLY MORE CONFIDENCE

MORE DERIVED NODES
!=
MORE INDEPENDENT EVIDENCE
```

---

# 23. Validation State

```yaml
ValidationState:

  schema:
    type: PASS_FAIL_UNKNOWN

  types:
    type: PASS_FAIL_UNKNOWN

  invariants:
    type: PASS_FAIL_UNKNOWN

  provenance:
    type: PASS_FAIL_UNKNOWN

  dependencies:
    type: PASS_FAIL_UNKNOWN

  scope:
    type: PASS_FAIL_UNKNOWN

  regime:
    type: PASS_FAIL_UNKNOWN

  freshness:
    type: PASS_FAIL_UNKNOWN

  HML:
    type: PASS_FAIL_UNKNOWN

  competing_preservation:
    type: PASS_FAIL_UNKNOWN

  confidence_ceiling:
    type: PASS_FAIL_UNKNOWN

  authority:
    type: PASS_FAIL_UNKNOWN

  overall:
    type:
      - PASS
      - CONDITIONAL
      - COMPETING
      - FAIL
      - UNKNOWN_GAP
```

Rule:

```text
ANY LOAD-BEARING UNKNOWN/GAP
CANNOT BE SILENTLY COERCED TO PASS
```

---

# 24. Repair State

```yaml
RepairState:

  repair_id:
    type: RepairID

  failed_state_refs:
    type: StateRef[]

  causal_failure_candidates:
    type: StateRef[]

  affected_descendants:
    type: StateRef[]

  preserved_state:
    type: StateRef[]

  rollback_point:
    type: StateRef | null

  repair_strategy:
    type:
      - REOBSERVE
      - REALLOCATE_ATTENTION
      - REEXTRACT_FEATURES
      - REBIND
      - RESTORE_COMPETING
      - INVALIDATE_MEMORY
      - REFRESH_DEPENDENCY
      - REDUCE_SCOPE
      - CHANGE_REGIME_MODEL
      - ROLLBACK
      - ESCALATE
      - UNKNOWN

  retry_condition:
    type: Predicate[]

  status:
    type:
      - NOT_STARTED
      - ACTIVE
      - BLOCKED
      - FAILED
      - COMPLETED
      - UNKNOWN_GAP
```

---

# 25. Authority State

```yaml
AuthorityState:

  requester:
    type: PrincipalRef

  capability:
    type: CapabilityEnvelope

  permissions:
    type: PermissionSet

  proposed_effect:
    type: EffectRef | null

  durable_effect_allowed:
    type: boolean

  commit_authority:
    type: AuthorityWitness | null
```

L03 itself defaults to:

```yaml
durable_effect_allowed: false
commit_authority: null
```

unless an external governing control plane explicitly supplies valid authority.

---

# 26. Persistence State

```yaml
PersistenceState:

  working_state:
    type: StateRef

  proposal_state:
    type: StateRef | null

  committed_state:
    type: StateRef | null

  previous_committed_state:
    type: StateRef | null

  epoch:
    type: EpochRef

  validation_epoch:
    type: EpochRef | null

  commit_status:
    type:
      - NOT_PROPOSED
      - PROPOSED
      - VALIDATING
      - COMMITTED
      - REJECTED
      - STALE
      - ROLLED_BACK
      - UNKNOWN_GAP
```

Hard boundary:

```text
WORKING
→ PROPOSAL
→ VALIDATION
→ COMMIT
```

No transition may be inferred merely because the previous state exists.

---

# 27. Operators

Candidate state operators:

```text
INIT_STATE
ADMIT_OBSERVATION
SET_ATTENTION
ADD_FEATURE
REMOVE_FEATURE
ADD_RELATION
REMOVE_RELATION
BIND
UNBIND
CREATE_PERCEPT_CANDIDATE
ADD_COMPETING_PERCEPT
SELECT_WORKING_PERCEPT
MAP_HML
ATTACH_MEMORY_CONTEXT
ATTACH_PROVENANCE
ADD_DEPENDENCY
MARK_STALE
MARK_INVALID
QUARANTINE
UPDATE_UNCERTAINTY
LOWER_CONFIDENCE_CEILING
VALIDATE_STATE
PROPOSE_STATE
ROLLBACK
REPAIR
```

These are `AMOS_MODEL` operator names pending direct L03 canon.

---

# 28. Candidate State Transition Function

[
S_{t+1}
=======

T(
S_t,
I_t,
Op_t,
C_t
)
]

where:

```text
S_t  = current L03 state
I_t  = admitted input
Op_t = authorized operator
C_t  = constraints/context
```

subject to:

[
ValidTransition
===============

TypeValid
\land
InvariantValid
\land
ScopeValid
\land
RegimeValid
\land
AuthorityValid
]

`AMOS_MODEL`.

A transition failure does not imply the previous valid state ceases to exist.

---

# 29. Lifecycle State Machine

Candidate:

```text
NOT_STARTED
    ↓
INITIALIZED
    ↓
ACTIVE
    ├──→ COMPETING
    ├──→ CONDITIONAL
    ├──→ BLOCKED
    ├──→ FAILED
    └──→ VALIDATING
              ↓
           COMPLETED
              ↓
           PROPOSED
```

External control-plane branch:

```text
PROPOSED
↓
COMMIT-TIME VALIDATION
├── REJECTED
├── STALE
├── REPAIR_REQUIRED
└── COMMITTED
```

`COMMITTED` is not owned by the L03 worker state itself.

---

# 30. Invariants

```text
STATE-INV-001
STATE != REALITY

STATE-INV-002
OBSERVATION != PERCEPT

STATE-INV-003
ATTENTION != TRUTH

STATE-INV-004
FEATURE != OBJECT

STATE-INV-005
RELATION != CAUSATION

STATE-INV-006
BINDING != IDENTITY

STATE-INV-007
MEMORY != CURRENT OBSERVATION

STATE-INV-008
DERIVED STATE MUST RETAIN SOURCE LINEAGE

STATE-INV-009
EPISTEMIC CLASS MUST NOT CHANGE SILENTLY

STATE-INV-010
H/M/L SCALE IDENTITY MUST BE PRESERVED

STATE-INV-011
H-LEVEL EXPECTATION MUST NOT REWRITE L-LEVEL SOURCE OBSERVATION

STATE-INV-012
COMPETING PERCEPTS MUST REMAIN VISIBLE UNTIL DISCRIMINATING EVIDENCE EXISTS

STATE-INV-013
SHARED ANCESTRY MUST NOT COUNT AS INDEPENDENT CONFIRMATION

STATE-INV-014
CONFIDENCE SHALL NOT EXCEED THE WEAKEST LOAD-BEARING PREMISE WITHOUT REVALIDATION

STATE-INV-015
SCOPE MUST PROPAGATE TO DERIVED STATE

STATE-INV-016
REGIME MUST PROPAGATE TO DERIVED STATE

STATE-INV-017
STALE STATE MUST NOT BE TREATED AS FRESH

STATE-INV-018
UNKNOWN/GAP MUST NOT PASS HARD VALIDATION

STATE-INV-019
FAILED TRANSITION MUST NOT CORRUPT LAST VALID STATE

STATE-INV-020
INVALIDATION SHOULD BE SELECTIVE TO DEPENDENTS

STATE-INV-021
REPAIR MUST NOT ALTER SOURCE EVIDENCE

STATE-INV-022
REPAIR REQUIRES REVALIDATION

STATE-INV-023
WORKING STATE != COMMITTED STATE

STATE-INV-024
PROPOSAL != COMMIT

STATE-INV-025
CAPABILITY != AUTHORITY

STATE-INV-026
PLACEHOLDER != IMPLEMENTED

STATE-INV-027
ADDRESSABLE != VALIDATED
```

---

# 31. Dependencies

## Upstream

```text
L01_SENSING_OBSERVATION
L02_ATTENTION
```

## Internal L03

```text
L03/README
L03/PURPOSE
L03/DEFINITION
L03/VARIABLES
L03/OPERATORS
L03/INVARIANTS
L03/DEPENDENCIES
L03/EQUATIONS
L03/HML
L03/MEMORY
L03/PROVENANCE
L03/PROTOCOLS
L03/AGENTS
L03/SKILLS
L03/WORKFLOWS
L03/FAILURE_MODES
L03/REPAIR
L03/TESTS
L03/RSCF
```

## Cross-cutting

```text
AMOS RSCF
AMOS H/M/L
AMOS provenance topology
AMOS epistemic governance
AMOS memory governance
AMOS constraint propagation
AMOS infrastructure control plane
AMOS deterministic control plane
AMOS context continuity
```

---

# 32. H/M/L Applicability

## L — Local percept state

```text
observations
features
local temporal relations
local spatial relations
local binding candidates
local uncertainty
```

## M — Intermediate percept state

```text
objects
events
clusters
multimodal bindings
memory-conditioned alternatives
intermediate percept candidates
```

## H — Governing percept state

```text
scene interpretation
global candidate organization
cross-scale constraints
overall competing percept set
global confidence ceiling
state validation
```

Cross-scale invariant:

```text
H MAY CONSTRAIN SEARCH
BUT MUST NOT FABRICATE L EVIDENCE
```

---

# 33. Control-Plane Requirements

L03 workers may manipulate working state only inside an admitted capability envelope.

The control plane should govern:

```text
state identity
version/epoch
authorized reads
authorized transformations
scope
regime
freshness
dependency validity
authority
protected-state effects
commit eligibility
rollback
```

Before durable effects:

```text
REVALIDATE:
  state epoch
  load-bearing dependencies
  provenance
  scope
  regime
  freshness
  authority
  constraints
```

The cognitive worker may return:

```text
STATE_PROPOSAL
```

but not silently create:

```text
DURABLE_COMMIT
```

---

# 34. Agents

Candidate state participants:

```text
L03_FEATURE_AGENT
L03_RELATION_AGENT
L03_BINDING_AGENT
L03_MULTIMODAL_AGENT
L03_HML_AGENT
L03_MEMORY_AGENT
L03_PROVENANCE_AGENT
L03_VALIDATION_AGENT
L03_REPAIR_AGENT
```

Each agent receives a bounded view or typed state reference.

Hard rule:

```text
AGENT LOCAL STATE
!=
AUTHORITATIVE GLOBAL STATE
```

---

# 35. Skills

Candidate Skills interacting with state include:

```text
AMOS Multimodal Perception Layer
AMOS Attention Allocation Governor
AMOS Binding RSCF Engine
AMOS Distinction RSCF Architecture
AMOS Information Operator Engine
AMOS Cross-Scale RSCF Tensor Engine
AMOS Temporal Multi-Scale RSCF Engine
AMOS Provenance Trust Firewall
AMOS Memory Conflict Governor
AMOS Metacognitive Confidence Auditor
RSCF Modeler
AMOS Constraint Propagation RSCF Engine
```

Skill availability does not prove implementation or validation.

---

# 36. Workflow

```text
RECEIVE OBSERVATION REFERENCES
↓
VALIDATE INPUT TYPES
↓
IMPORT ATTENTION STATE
↓
INITIALIZE L03 WORKING STATE
↓
FORM FEATURES
↓
FORM RELATIONS
↓
FORM BINDINGS
↓
GENERATE PERCEPT CANDIDATES
↓
PRESERVE COMPETING CANDIDATES
↓
MAP H/M/L
↓
ATTACH MEMORY CONTEXT
↓
ATTACH PROVENANCE
↓
BUILD DEPENDENCY GRAPH
↓
PROPAGATE SCOPE / REGIME / FRESHNESS
↓
COMPUTE UNCERTAINTY / CONFIDENCE CEILING
↓
VALIDATE INVARIANTS
↓
CHALLENGE STATE
↓
REPAIR IF REQUIRED
↓
RETURN WORKING PERCEPT STATE / PROPOSAL
```

---

# 37. Protocols

Candidate state protocols:

```text
L03_STATE_INIT
L03_STATE_READ
L03_STATE_TRANSFORM
L03_STATE_VALIDATE

L03_FEATURE_ADD
L03_RELATION_ADD
L03_BINDING_ADD

L03_PERCEPT_CANDIDATE_ADD
L03_COMPETING_ADD

L03_STATE_INVALIDATE
L03_STATE_QUARANTINE
L03_STATE_REPAIR
L03_STATE_ROLLBACK

L03_STATE_PROPOSAL
L03_STATE_COMMIT_REQUEST
L03_STATE_COMMIT_RESULT
```

Canonical protocol names remain `UNKNOWN/GAP`.

---

# 38. Evidence / Provenance

Every material state mutation should be attributable to:

```yaml
StateMutationEvidence:

  mutation_id: null

  prior_state_ref: null

  resulting_state_ref: null

  operator: null

  actor: null

  skill: null

  input_refs: []

  dependency_refs: []

  provenance_refs: []

  scope: null

  regime: null

  timestamp: null

  epoch: null

  validation_ref: null

  uncertainty_delta: null

  confidence_delta: null
```

Hard rule:

```text
UNATTRIBUTABLE MATERIAL STATE MUTATION
→
QUARANTINE / GAP
```

---

# 39. Uncertainty and Confidence Ceiling

State confidence is bounded by the weakest load-bearing state required to support the percept.

Candidate:

[
Conf(S^{percept})
\le
\min(
Conf(O),
Conf(F),
Conf(R),
Conf(B),
Conf(Prov),
Conf(Scope),
Conf(Regime)
)
]

where only load-bearing dimensions are included.

`AMOS_MODEL`.

Material uncertainty should remain vectorized rather than being hidden behind one aggregate score.

---

# 40. Failure Modes

```text
SFM-001
Observation state missing.

SFM-002
Attention state missing or stale.

SFM-003
Observation rewritten as interpretation.

SFM-004
Feature state loses source reference.

SFM-005
Relation state overclaims causality.

SFM-006
Binding collapses distinct entities.

SFM-007
Competing percept disappears without discriminating evidence.

SFM-008
Memory overwrites current observation.

SFM-009
H-level hypothesis contaminates L-level evidence.

SFM-010
Scope is lost during derivation.

SFM-011
Regime mismatch is ignored.

SFM-012
Stale state treated as current.

SFM-013
Provenance ancestry is lost.

SFM-014
Correlated evidence counted independently.

SFM-015
Confidence exceeds load-bearing premise.

SFM-016
UNKNOWN/GAP coerced to PASS.

SFM-017
Failed mutation corrupts last valid state.

SFM-018
Global invalidation occurs when selective invalidation was sufficient.

SFM-019
Repair mutates source evidence.

SFM-020
Repair skips revalidation.

SFM-021
Working state represented as committed state.

SFM-022
State proposal self-authorizes commit.

SFM-023
State epoch becomes stale before effect.

SFM-024
Implementation status inferred from schema existence.

SFM-025
Validation status inferred from addressability.
```

---

# 41. Repair / Recovery

The continuity architecture requires failed paths not to be repeated until retry conditions change and preserves the nearest valid checkpoint rather than allowing failure to redefine the objective.

Candidate L03 recovery:

```text
DETECT INVALID STATE
↓
IDENTIFY EARLIEST FAILED LOAD-BEARING NODE
↓
COMPUTE DEPENDENT DESCENDANTS
↓
QUARANTINE FAILED BRANCH
↓
RESTORE LAST VALID STATE
↓
PRESERVE UNAFFECTED BRANCHES
↓
SELECT REPAIR:
  refresh observation
  reallocate attention
  reconstruct feature
  reconstruct relation
  unbind/rebind
  restore competing candidate
  invalidate stale memory
  refresh provenance
  reduce scope
  update regime
  rollback
↓
REEXECUTE ONLY AFFECTED PATH
↓
REVALIDATE
↓
CHALLENGE
↓
RESTORE / CONDITIONAL / COMPETING / GAP
```

Hard recovery rule:

```text
FAILED_PATH
MAY NOT BE REPEATED
UNTIL RETRY_CONDITION CHANGES
```

---

# 42. Tests / Validators

Minimum validators:

```text
VALIDATE_STATE_SCHEMA
VALIDATE_STATE_TYPES
VALIDATE_OBSERVATION_IMMUTABILITY
VALIDATE_ATTENTION_TRUTH_SEPARATION
VALIDATE_FEATURE_LINEAGE
VALIDATE_RELATION_CAUSAL_FIREWALL
VALIDATE_BINDING_IDENTITY_FIREWALL
VALIDATE_MEMORY_OBSERVATION_SEPARATION
VALIDATE_COMPETING_PRESERVATION
VALIDATE_HML_INTEGRITY
VALIDATE_PROVENANCE_GRAPH
VALIDATE_DEPENDENCY_GRAPH
VALIDATE_SCOPE
VALIDATE_REGIME
VALIDATE_FRESHNESS
VALIDATE_CONFIDENCE_CEILING
VALIDATE_SELECTIVE_INVALIDATION
VALIDATE_REPAIR_REVALIDATION
VALIDATE_AUTHORITY
VALIDATE_PROPOSAL_COMMIT_BOUNDARY
VALIDATE_UNKNOWN_NOT_PASS
```

Conceptual tests:

```text
TEST-L03-STATE-001
Input lacks provenance.
Expected:
BLOCKED / UNKNOWN_GAP.

TEST-L03-STATE-002
High-attention feature has weak evidence.
Expected:
confidence remains evidence-bounded.

TEST-L03-STATE-003
Two bindings fit equally well.
Expected:
COMPETING retained.

TEST-L03-STATE-004
Memory conflicts with current observation.
Expected:
both states remain distinguishable.

TEST-L03-STATE-005
One load-bearing feature is invalidated.
Expected:
only dependent percept branches invalidate.

TEST-L03-STATE-006
H-level scene hypothesis conflicts with L observation.
Expected:
L observation preserved.

TEST-L03-STATE-007
State regime changes after validation.
Expected:
revalidation required.

TEST-L03-STATE-008
Source descendants appear as three confirmations.
Expected:
shared ancestry detected.

TEST-L03-STATE-009
Worker attempts durable mutation without authority.
Expected:
proposal only / reject commit.

TEST-L03-STATE-010
Repair restores state but skips validators.
Expected:
not VALIDATED.

TEST-L03-STATE-011
UNKNOWN exists in load-bearing invariant.
Expected:
overall state cannot PASS.

TEST-L03-STATE-012
All structural validators pass.
Expected:
does not establish empirical perceptual correctness.
```

Current validation status:

```yaml
tests_defined: true
tests_executed: false
runtime_validation: false
formal_verification: false
empirical_validation: false
```

---

# 43. Falsifiers

This state contract should be revised if direct canonical evidence establishes:

```text
a different canonical L03 state schema

different canonical state variables

different percept lifecycle states

different H/M/L state semantics

different observation/percept boundaries

different memory integration semantics

different provenance requirements

different state transition rules

different persistence semantics

different commit authority ownership
```

Runtime falsifier:

```text
a reproducible canonical L03 implementation
whose valid state transitions contradict
one or more MODEL-level assumptions here
```

does not falsify source-level AMOS principles unless those principles themselves are contradicted.

---

# 44. Gap Matrix

```yaml
gap_status:

  generic_typed_state_governance:
    status: SOURCE_ALIGNED

  epistemic_state_separation:
    status: SOURCE_ALIGNED

  context_state_distinction:
    status: SOURCE_ALIGNED

  failure_status_distinction:
    status: SOURCE_ALIGNED

  selective_recovery_principle:
    status: SOURCE_ALIGNED

  L03_top_level_state:
    status: MODEL_DEFINED

  observation_state:
    status: MODEL_DEFINED

  attention_state:
    status: MODEL_DEFINED

  feature_state:
    status: MODEL_DEFINED

  relation_state:
    status: MODEL_DEFINED

  binding_state:
    status: MODEL_DEFINED

  percept_candidate_state:
    status: MODEL_DEFINED

  competing_state:
    status: MODEL_DEFINED

  HML_state:
    status: MODEL_DEFINED

  memory_state:
    status: MODEL_DEFINED

  provenance_state:
    status: MODEL_DEFINED

  uncertainty_state:
    status: MODEL_DEFINED

  validation_state:
    status: MODEL_DEFINED

  repair_state:
    status: MODEL_DEFINED

  persistence_state:
    status: MODEL_DEFINED

  canonical_L03_state_schema:
    status: CRITICAL_GAP

  canonical_variable_names:
    status: DECISION_RELEVANT_GAP

  canonical_transition_table:
    status: CRITICAL_GAP

  canonical_acceptance_thresholds:
    status: CRITICAL_GAP

  canonical_persistence_semantics:
    status: CRITICAL_GAP

  executable_runtime:
    status: CRITICAL_GAP

  executed_tests:
    status: CRITICAL_GAP

  formal_verification:
    status: CRITICAL_GAP

  empirical_validation:
    status: CRITICAL_GAP
```

---

# 45. Competing State Architectures

## COMPETING-001 — Flat Mutable State

```text
single shared percept object
continuously mutated
```

Risk:

```text
weak provenance
poor rollback
hidden contamination
```

## COMPETING-002 — Immutable Event-Derived State

```text
observation/events
→ transformations
→ reconstructed current state
```

Strength:

```text
strong lineage
replayability
```

Risk:

```text
storage and reconstruction overhead
```

## COMPETING-003 — Versioned Graph State

```text
typed state nodes
+
dependency graph
+
epochs
+
selective invalidation
```

Strength:

```text
localized repair
explicit dependencies
```

## COMPETING-004 — Governed Versioned H/M/L State Graph

```text
typed versioned graph
+
H/M/L coordinates
+
epistemic classes
+
provenance ancestry
+
competing hypotheses
+
scope/regime/freshness
+
uncertainty vector
+
external commit authority
```

Current model preference:

```text
COMPETING-004
```

because it best preserves the source-aligned AMOS requirements for typed state, provenance, dependency closure, uncertainty, selective repair, and state separation.

This remains:

```text
MODEL PREFERENCE
!=
CANONICAL L03 STATE ARCHITECTURE
```

---

# 46. RSCF Completion State

```yaml
rscf:

  id: L03_PERCEPT_FORMATION_STATE

  claim:
    L03_PERCEPT_FORMATION can be represented as a governed,
    typed, versioned working-state graph that preserves observations,
    attention, features, relations, bindings, percept candidates,
    competing interpretations, H/M/L structure, memory context,
    provenance, dependencies, scope, regime, freshness, uncertainty,
    validation, repair, authority, and persistence boundaries.

  claim_class: MODEL

  evidence:
    - AMOS Skill Builder typed-state requirements
    - AMOS Context Continuity Governor state-separation requirements
    - reconstructed L03 contract family

  provenance:
    origin_architect: Trang Phan
    architecture_family: AMOS
    subsystem: COGNITIVE_MATRIX
    primitive: L03_PERCEPT_FORMATION
    artifact: STATE.md
    derivation: SOURCE_ALIGNED_STATE_PRINCIPLES_PLUS_L03_MODEL

  scope:
    system: AMOS_OS
    subsystem: COGNITIVE_MATRIX
    primitive: L03_PERCEPT_FORMATION
    concern: working_state_and_state_governance

  regime:
    governed percept-formation architecture

  freshness:
    revalidate_when:
      - direct L03 state canon recovered
      - L01 observation contract changes
      - L02 attention contract changes
      - L03 variable/operator schemas change
      - HML semantics change
      - provenance architecture changes
      - control-plane architecture changes
      - executable L03 runtime appears

  dependencies:
    - L01_SENSING_OBSERVATION
    - L02_ATTENTION
    - L03_DEFINITION
    - L03_VARIABLES
    - L03_OPERATORS
    - L03_INVARIANTS
    - L03_DEPENDENCIES
    - L03_HML
    - L03_MEMORY
    - L03_PROVENANCE
    - L03_PROTOCOLS
    - L03_SKILLS
    - L03_REPAIR
    - L03_TESTS
    - L03_RSCF
    - AMOS_SKILL_BUILDER
    - AMOS_CONTEXT_CONTINUITY_GOVERNOR
    - AMOS_INFRASTRUCTURE_CONTROL_PLANE

  competing:
    - flat mutable state
    - immutable event-derived state
    - versioned graph state
    - governed versioned HML state graph

  falsifiers:
    - incompatible direct L03 state canon
    - incompatible state transition semantics
    - incompatible HML semantics
    - incompatible persistence semantics
    - executable canonical runtime counterexample

  uncertainty:
    generic_state_governance: LOW_MEDIUM
    L03_mapping: HIGH
    canonical_schema: MAXIMUM
    transition_semantics: HIGH
    persistence_semantics: HIGH
    execution: MAXIMUM
    empirical: MAXIMUM

  confidence_ceiling:
    Generic AMOS typed-state and continuity principles are
    source-aligned. The specific L03 state schema, variables,
    transitions, persistence semantics, runtime behavior, and
    empirical perceptual validity remain MODEL or UNKNOWN/GAP.

  gap_status:
    canonical_state_schema: CRITICAL_GAP
    canonical_variables: DECISION_RELEVANT_GAP
    canonical_transitions: CRITICAL_GAP
    canonical_persistence: CRITICAL_GAP
    executable_runtime: CRITICAL_GAP
    executed_validation: CRITICAL_GAP
    empirical_validation: CRITICAL_GAP

  cheapest_discriminating_test:
    Recover direct canonical L03 state material and compare its
    variables and transition semantics field-by-field against this
    model; then execute a minimal observation→attention→feature→
    binding→candidate→validation trajectory with provenance,
    competing-state preservation, selective invalidation, rollback,
    stale-epoch injection, and unauthorized-commit tests.
```

---

# 47. Completion State

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

  canonical_state_schema:
    status: UNKNOWN_GAP

  executable_runtime:
    status: UNKNOWN_GAP

  runtime_validation:
    status: UNKNOWN_GAP

  formal_verification:
    status: UNKNOWN_GAP

  empirical_validation:
    status: UNKNOWN_GAP

  overall:
    status: COMPLETE_FOR_STATE_CONTRACT_SCOPE

  conclusion_class:
    MODEL
```

---

# 48. Hard Boundaries

```text
PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

UNKNOWN/GAP != PASS
```

State-specific boundaries:

```text
STATE != REALITY

OBSERVATION != PERCEPT

ATTENTION != TRUTH

FEATURE != OBJECT

RELATION != CAUSATION

BINDING != IDENTITY

MEMORY != CURRENT OBSERVATION

DERIVED STATE != SOURCE STATE

CANDIDATE != ACCEPTED PERCEPT

ACCEPTED WORKING PERCEPT != VERIFIED EXTERNAL FACT

H-LEVEL EXPECTATION != L-LEVEL OBSERVATION

MULTIPLE DERIVED NODES != INDEPENDENT EVIDENCE

VALID STATE != AUTHORIZED STATE

WORKING STATE != PERSISTENT STATE

VALIDATION != COMMIT AUTHORITY

STATE TRANSITION != DURABLE COMMIT

REPAIR != REVALIDATION

STRUCTURAL VALIDITY != EMPIRICAL PERCEPTUAL VALIDITY

MODEL STATE SCHEMA != IMPLEMENTED STATE SCHEMA
```

---

# 49. Governing State Contract

> **`L03_PERCEPT_FORMATION` SHALL maintain percept formation as typed, versioned, provenance-bound working state rather than as an unqualified representation of reality. Source observations, attention allocation, derived features, relations, bindings, memory context, percept candidates, competing interpretations, H/M/L state, provenance, dependencies, scope, regime, freshness, uncertainty, validation, repair, authority, and persistence status SHALL remain distinguishable wherever material. State transformations SHALL preserve semantic origin and dependency lineage; attention SHALL NOT become truth, binding SHALL NOT become identity, memory SHALL NOT overwrite current observation, H-level hypotheses SHALL NOT rewrite L-level evidence, and shared provenance SHALL NOT manufacture independent confirmation. Competing percepts SHALL remain explicit until discriminating evidence warrants resolution. Confidence SHALL remain bounded by load-bearing premises. Failed or stale state SHALL be selectively invalidated while unaffected valid state is preserved. Repair SHALL return to the nearest valid state and require revalidation before promotion. Working-state correctness SHALL NOT imply durable authority: L03 MAY construct and propose percept state, while authoritative persistence remains externally governed. `UNKNOWN/GAP` SHALL remain non-passing.**

---

# 50. Canon Boundary

```text
SOURCE / ARCHITECTURE-ALIGNED:

Trang Phan origin/stewardship

AMOS typed-state requirement

canonical tensor axes:
  object
  primitive
  scale
  time
  regime
  observer
  provenance
  epistemic_class
  confidence
  consequence

UNKNOWN is distinct from:
  false
  zero
  absent
  contradicted

explicit claim state

explicit system state

smallest sufficient dependency closure

hard invariant admission

conversation/runtime/artifact/persistence
state separation

explicit lifecycle distinctions:
  COMPLETED
  ACTIVE
  BLOCKED
  FAILED
  NOT_STARTED

failed action changes plan,
not governing objective

failed paths require changed
retry conditions before repetition


AMOS_MODEL:

L03 top-level state schema

observation state

attention state

feature state

relation state

binding state

percept candidate state

competing percept state

H/M/L percept state

memory context state

provenance state

dependency state

freshness state

uncertainty vector

confidence ceiling relation

validation state

repair state

authority state

persistence state

state operators

state-transition function

L03 lifecycle state machine

failure taxonomy

test suite


UNKNOWN/GAP:

direct canonical L03 state schema

canonical L03 state-variable identifiers

canonical percept representation

canonical transition table

canonical acceptance thresholds

canonical persistence semantics

canonical commit semantics

executable L03 state runtime

executed validation

formal verification

empirical perceptual validation
```

Therefore:

```text
CONCLUSION CLASS:
MODEL

GENERIC AMOS STATE GOVERNANCE:
SOURCE-ALIGNED

L03-SPECIFIC STATE CONTRACT:
MODEL

DIRECT L03 STATE CANON:
UNKNOWN/GAP

IMPLEMENTATION:
UNKNOWN/GAP

RUNTIME VALIDATION:
UNKNOWN/GAP

FORMAL VERIFICATION:
UNKNOWN/GAP

EMPIRICAL HUMAN-PERCEPTION CLAIM:
NOT ESTABLISHED
```
