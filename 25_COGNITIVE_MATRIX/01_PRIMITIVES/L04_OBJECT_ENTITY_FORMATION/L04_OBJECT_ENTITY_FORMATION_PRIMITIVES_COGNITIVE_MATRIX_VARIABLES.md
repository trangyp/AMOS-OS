---
title: "L04_OBJECT_ENTITY_FORMATION — Variables"
type: variable
origin_architect: "Trang Phan"
class: "COGNITIVE_PRIMITIVE_VARIABLE_CONTRACT"
status: "AMOS_MODEL / UNVALIDATED"
epistemic_class: "MODEL"
primitive: "L04_OBJECT_ENTITY_FORMATION"
artifact: "VARIABLES.md"
tags: [cognitive_matrix, primitives, l04_object_entity_formation, note]

---

# L04_OBJECT_ENTITY_FORMATION — Variables

**Class:** `COGNITIVE_PRIMITIVE_VARIABLE_CONTRACT`  
**Origin architect / steward:** Trang Phan  
**Primitive:** `L04_OBJECT_ENTITY_FORMATION`  
**Artifact:** `VARIABLES.md`  
**Status:** `AMOS_MODEL / UNVALIDATED`

## 0. Purpose

Define the typed variable contract for `L04_OBJECT_ENTITY_FORMATION`.

L04 variables represent the state needed to transform admitted perceptual evidence into bounded **object candidates** and, only where sufficient continuity/identity evidence exists, **entity candidates**.

This contract preserves the distinctions:

```text
percept != object

object_candidate != validated_object

object != entity

continuity != identity

similarity != identity

label != referent

candidate != committed state
```

The variables below are candidate AMOS model variables. Their presence in this specification does not establish that an authoritative L04 runtime currently implements them.

---

# 1. Source / Canon References

## 1.1 Source-aligned basis

AMOS cognition canon identifies Trang Phan as origin architect/steward and identifies the `AMOS_COGNITION` layer as including process orchestration and attention allocation. Corpus models must remain distinct from independently verified empirical claims.

The broader AMOS reasoning contract additionally requires preservation of:

```text
typed state
distinctions
relations
constraints
provenance
scope
regime
freshness
dependencies
competing hypotheses
confidence ceilings
authority boundaries
proposal/commit separation
selective invalidation
```

## 1.2 Candidate sibling dependencies

```text
L03_PERCEPT_FORMATION
L04_DEFINITION
L04_STATE
L04_OPERATORS
L04_INVARIANTS
L04_DEPENDENCIES
L04_HML
L04_MEMORY
L04_PROVENANCE
L04_RSCF
L04_CONTROL_PLANES
```

## 1.3 Canon gaps

No retrieved authoritative source establishes the exact canonical variable registry for `L04_OBJECT_ENTITY_FORMATION`.

Therefore:

```yaml
canonical_variable_names: UNKNOWN_GAP
canonical_types: UNKNOWN_GAP
canonical_domains: UNKNOWN_GAP
canonical_equations: UNKNOWN_GAP
canonical_thresholds: UNKNOWN_GAP
```

Everything newly specified below is `AMOS_MODEL`, not recovered canon.

---

# 2. Definition and Scope

An `L04Variable` is a typed state-bearing value used to represent or govern:

```text
admitted perceptual evidence
features
distinctions
relations
candidate boundaries
bindings
object hypotheses
continuity hypotheses
identity hypotheses
entity hypotheses
provenance
scope/regime
uncertainty
confidence
dependencies
revision state
authority state
```

Variables MAY describe:

```text
OBSERVATION
SOURCE_CLAIM
DERIVED
MODEL
PROPOSAL
UNKNOWN/GAP
```

A variable MUST NOT silently change epistemic class.

Excluded from this contract:

```text
claims that L04 models biological object recognition
claims of neuroscientific validity
claims of conscious object perception
production implementation claims
empirical benchmark claims
```

---

# 3. Root Typed State

```yaml
L04ObjectEntityState:

  state_id:
    type: StateID

  revision:
    type: RevisionID

  percepts:
    type: Map<PerceptID, PerceptRecord>

  features:
    type: Map<FeatureID, FeatureRecord>

  distinctions:
    type: Map<DistinctionID, DistinctionRecord>

  relations:
    type: Map<RelationID, RelationRecord>

  boundaries:
    type: Map<BoundaryID, BoundaryHypothesis>

  bindings:
    type: Map<BindingID, BindingHypothesis>

  object_candidates:
    type: Map<ObjectID, ObjectCandidate>

  continuity_hypotheses:
    type: Map<ContinuityID, ContinuityHypothesis>

  identity_hypotheses:
    type: Map<IdentityID, IdentityHypothesis>

  entity_candidates:
    type: Map<EntityID, EntityCandidate>

  contradictions:
    type: Map<ContradictionID, ContradictionRecord>

  competing_sets:
    type: Map<CompetitionID, CompetingHypothesisSet>

  dependency_graph:
    type: DependencyGraph

  provenance_graph:
    type: ProvenanceGraph

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeEnvelope

  freshness:
    type: FreshnessState

  uncertainty:
    type: L04UncertaintyVector

  authority:
    type: AuthorityState

  lifecycle:
    type: L04LifecycleState
```

---

# 4. Input Variables

## 4.1 Percept input

```yaml
PerceptRecord:

  percept_id:
    type: PerceptID

  payload_ref:
    type: EvidenceRef

  modality:
    type: Modality

  observer:
    type: ObserverID | null

  observation_time:
    type: Timestamp | null

  event_time:
    type: Timestamp | null

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeEnvelope

  provenance:
    type: ProvenanceRef[]

  epistemic_class:
    type:
      - OBSERVATION
      - SOURCE_CLAIM
      - DERIVED
      - UNKNOWN_GAP

  confidence:
    type: ConfidenceBound

  admission_state:
    type:
      - PROPOSED
      - ADMITTED
      - QUARANTINED
      - REJECTED
      - STALE
```

Invariant:

```text
percept admission
requires provenance + applicability evaluation
where those are load-bearing.
```

---

# 5. Feature Variables

```yaml
FeatureRecord:

  feature_id:
    type: FeatureID

  percept_refs:
    type: PerceptID[]

  feature_type:
    type: FeatureType

  value:
    type: TypedValue

  units:
    type: Unit | null

  extraction_method:
    type: MethodRef | null

  provenance:
    type: ProvenanceRef[]

  scope:
    type: ScopeEnvelope

  confidence:
    type: ConfidenceBound
```

Hard invariant:

```text
FEATURE != OBJECT
```

A feature may support object formation but cannot by itself instantiate an object unless authoritative canon explicitly defines such an operator.

---

# 6. Distinction Variables

```yaml
DistinctionRecord:

  distinction_id:
    type: DistinctionID

  lhs:
    type: StateRef

  rhs:
    type: StateRef

  criterion:
    type: DistinctionCriterion

  strength:
    type: ConfidenceBound

  provenance:
    type: ProvenanceRef[]

  status:
    type:
      - PROPOSED
      - SUPPORTED
      - CONTESTED
      - INVALIDATED
```

Candidate conceptual notation:

[
D(a,b\mid c)
]

where `c` is the declared distinction criterion.

This notation is `AMOS_MODEL`.

Invariant:

```text
D(a,b) does not imply causal independence.
```

---

# 7. Relation Variables

```yaml
RelationRecord:

  relation_id:
    type: RelationID

  source:
    type: StateRef

  target:
    type: StateRef

  relation_type:
    type: RelationType

  direction:
    type:
      - DIRECTED
      - UNDIRECTED

  temporal_extent:
    type: TimeInterval | null

  confidence:
    type: ConfidenceBound

  provenance:
    type: ProvenanceRef[]
```

Examples of candidate relation classes:

```text
spatial
temporal
structural
part_of
adjacent_to
similar_to
co_occurs_with
derived_from
```

No relation class automatically licenses causation.

---

# 8. Boundary Variables

```yaml
BoundaryHypothesis:

  boundary_id:
    type: BoundaryID

  members:
    type: StateRef[]

  excluded:
    type: StateRef[]

  criterion:
    type: BoundaryCriterion

  permeability:
    type: Scalar | null

  stability:
    type: ConfidenceBound

  scope:
    type: ScopeEnvelope

  provenance:
    type: ProvenanceRef[]

  status:
    type:
      - PROPOSED
      - SUPPORTED
      - COMPETING
      - REJECTED
      - INVALIDATED
```

Boundary invariant:

```text
boundary confidence
cannot exceed its weakest unresolved
load-bearing distinction/relation evidence.
```

---

# 9. Binding Variables

```yaml
BindingHypothesis:

  binding_id:
    type: BindingID

  components:
    type: StateRef[]

  binding_basis:
    type: BindingCriterion[]

  strength:
    type: ConfidenceBound

  alternatives:
    type: BindingID[]

  provenance:
    type: ProvenanceRef[]

  status:
    type:
      - PROPOSED
      - SUPPORTED
      - COMPETING
      - REJECTED
      - INVALIDATED
```

Hard boundaries:

```text
CO_OCCURRENCE != BINDING

ADJACENCY != BINDING

SIMILARITY != BINDING
```

---

# 10. Object Candidate Variables

```yaml
ObjectCandidate:

  object_id:
    type: ObjectID

  member_refs:
    type: StateRef[]

  feature_refs:
    type: FeatureID[]

  distinction_refs:
    type: DistinctionID[]

  relation_refs:
    type: RelationID[]

  boundary_refs:
    type: BoundaryID[]

  binding_refs:
    type: BindingID[]

  object_class:
    type: OntologyRef | null

  confidence:
    type: ConfidenceBound

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeEnvelope

  freshness:
    type: FreshnessState

  provenance:
    type: ProvenanceRef[]

  dependencies:
    type: DependencyRef[]

  status:
    type:
      - PROPOSED
      - CANDIDATE
      - SUPPORTED
      - COMPETING
      - QUARANTINED
      - INVALIDATED
```

Hard invariant:

```text
ObjectCandidate.status == SUPPORTED
does not imply
persistent entity identity.
```

---

# 11. Continuity Variables

```yaml
ContinuityHypothesis:

  continuity_id:
    type: ContinuityID

  object_refs:
    type: ObjectID[]

  temporal_order:
    type: Timestamp[]

  continuity_basis:
    type: ContinuityCriterion[]

  discontinuities:
    type: DiscontinuityRecord[]

  confidence:
    type: ConfidenceBound

  provenance:
    type: ProvenanceRef[]

  status:
    type:
      - PROPOSED
      - SUPPORTED
      - COMPETING
      - REJECTED
```

Hard boundary:

```text
CONTINUITY != IDENTITY
```

---

# 12. Identity Variables

```yaml
IdentityHypothesis:

  identity_id:
    type: IdentityID

  candidate_refs:
    type: ObjectID[]

  hypothesis:
    type:
      - SAME_ENTITY
      - DIFFERENT_ENTITIES
      - PART_WHOLE
      - UNKNOWN

  supporting_evidence:
    type: EvidenceRef[]

  opposing_evidence:
    type: EvidenceRef[]

  continuity_refs:
    type: ContinuityID[]

  competing_identity_refs:
    type: IdentityID[]

  confidence:
    type: ConfidenceBound

  provenance:
    type: ProvenanceRef[]

  status:
    type:
      - PROPOSED
      - SUPPORTED
      - COMPETING
      - REJECTED
      - INVALIDATED
```

Identity invariants:

```text
SIMILARITY != IDENTITY

NAME_MATCH != IDENTITY

TEMPORAL_SEQUENCE != IDENTITY

CONTINUITY alone != IDENTITY
unless canonical semantics explicitly license it.
```

---

# 13. Entity Candidate Variables

```yaml
EntityCandidate:

  entity_id:
    type: EntityID

  object_refs:
    type: ObjectID[]

  identity_refs:
    type: IdentityID[]

  continuity_refs:
    type: ContinuityID[]

  ontology_refs:
    type: OntologyRef[]

  aliases:
    type: AliasRecord[]

  attributes:
    type: Map<AttributeID, AttributeRecord>

  confidence:
    type: ConfidenceBound

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeEnvelope

  freshness:
    type: FreshnessState

  provenance:
    type: ProvenanceRef[]

  dependencies:
    type: DependencyRef[]

  status:
    type:
      - PROPOSED
      - CANDIDATE
      - SUPPORTED
      - COMPETING
      - QUARANTINED
      - INVALIDATED
```

Critical invariant:

```text
ENTITY CANDIDATE != ONTOLOGICALLY VERIFIED ENTITY
```

---

# 14. Contradiction Variables

```yaml
ContradictionRecord:

  contradiction_id:
    type: ContradictionID

  claim_a:
    type: ClaimRef

  claim_b:
    type: ClaimRef

  relation:
    type:
      - LOGICAL_CONFLICT
      - IDENTITY_CONFLICT
      - BOUNDARY_CONFLICT
      - TEMPORAL_CONFLICT
      - SCOPE_CONFLICT
      - REGIME_CONFLICT
      - PROVENANCE_CONFLICT

  severity:
    type: Severity

  resolution_state:
    type:
      - OPEN
      - COMPETING
      - RESOLVED
      - UNRESOLVED_GAP
```

Invariant:

```text
contradiction existence
must remain queryable until legitimately resolved.
```

---

# 15. Competing Hypothesis Variables

```yaml
CompetingHypothesisSet:

  competition_id:
    type: CompetitionID

  hypotheses:
    type: HypothesisRef[]

  evidence_by_hypothesis:
    type: Map<HypothesisRef, EvidenceRef[]>

  independence_state:
    type:
      - ESTABLISHED
      - CORRELATED
      - UNKNOWN

  discriminating_tests:
    type: TestRef[]

  status:
    type:
      - OPEN
      - DISCRIMINATING
      - RESOLVED
      - INCOMPARABLE
```

Invariant:

```text
equal/incomparable support
must not be converted into arbitrary convergence.
```

---

# 16. Provenance Variables

```yaml
ProvenanceNode:

  provenance_id:
    type: ProvenanceID

  source_id:
    type: SourceID

  source_class:
    type:
      - PRIMARY
      - DERIVED
      - MODEL
      - SYNTHETIC
      - UNKNOWN

  parent_refs:
    type: ProvenanceID[]

  transformation_refs:
    type: TransformationID[]

  source_version:
    type: VersionID | null

  timestamp:
    type: Timestamp | null

  trust_state:
    type: TrustState

  independence_state:
    type:
      - INDEPENDENT
      - SHARED_ANCESTRY
      - UNKNOWN
```

Hard invariant:

```text
MULTIPLE RECORDS != MULTIPLE INDEPENDENT SOURCES
```

---

# 17. Dependency Variables

```yaml
DependencyEdge:

  parent:
    type: StateRef

  child:
    type: StateRef

  dependency_type:
    type:
      - REQUIRED
      - SUPPORTING
      - DERIVED_FROM
      - CONSTRAINS
      - INVALIDATES

  load_bearing:
    type: boolean
```

Required property:

```text
invalidate(parent)
→ re-evaluate dependent descendants

not
→ globally invalidate unrelated state
```

---

# 18. Scope Variables

```yaml
ScopeEnvelope:

  system:
    type: ScopeValue | null

  population:
    type: ScopeValue | null

  environment:
    type: ScopeValue | null

  observer:
    type: ObserverID | null

  scale:
    type: ScaleID | null

  modality:
    type: Modality | null

  assumptions:
    type: AssumptionRef[]
```

Invariant:

```text
scope(derived)
⊆ compatible support envelope
```

unless explicit independent evidence widens applicability.

---

# 19. Regime Variables

```yaml
RegimeEnvelope:

  regime_id:
    type: RegimeID | null

  conditions:
    type: Condition[]

  valid_from:
    type: Timestamp | null

  valid_until:
    type: Timestamp | null

  regime_confidence:
    type: ConfidenceBound

  transition_state:
    type:
      - STABLE
      - SHIFT_SUSPECTED
      - SHIFT_CONFIRMED
      - UNKNOWN
```

A regime transition may invalidate only conclusions whose applicability depends on the changed regime.

---

# 20. Freshness Variables

```yaml
FreshnessState:

  observed_at:
    type: Timestamp | null

  validated_at:
    type: Timestamp | null

  expires_at:
    type: Timestamp | null

  freshness_class:
    type:
      - CURRENT
      - AGING
      - STALE
      - UNKNOWN
```

Hard boundary:

```text
previously valid != currently valid
```

---

# 21. Uncertainty Variables

```yaml
L04UncertaintyVector:

  evidence_uncertainty:
    type: ProbabilityLikeBound | OrdinalUncertainty

  percept_uncertainty:
    type: ProbabilityLikeBound | OrdinalUncertainty

  boundary_uncertainty:
    type: ProbabilityLikeBound | OrdinalUncertainty

  binding_uncertainty:
    type: ProbabilityLikeBound | OrdinalUncertainty

  object_uncertainty:
    type: ProbabilityLikeBound | OrdinalUncertainty

  continuity_uncertainty:
    type: ProbabilityLikeBound | OrdinalUncertainty

  identity_uncertainty:
    type: ProbabilityLikeBound | OrdinalUncertainty

  entity_uncertainty:
    type: ProbabilityLikeBound | OrdinalUncertainty

  scope_uncertainty:
    type: ProbabilityLikeBound | OrdinalUncertainty

  temporal_uncertainty:
    type: ProbabilityLikeBound | OrdinalUncertainty

  causal_uncertainty:
    type: ProbabilityLikeBound | OrdinalUncertainty

  provenance_independence_uncertainty:
    type: ProbabilityLikeBound | OrdinalUncertainty
```

These components SHOULD remain separate where their distinction affects downstream decisions.

---

# 22. Confidence Variables

```yaml
ConfidenceBound:

  value:
    type: float | null

  lower:
    type: float | null

  upper:
    type: float | null

  basis:
    type: EvidenceRef[]

  ceiling:
    type: float | null

  calibration_status:
    type:
      - CALIBRATED
      - HEURISTIC
      - ORDINAL
      - UNKNOWN
```

Candidate AMOS confidence rule:

[
C(y)
\le
\min_{x\in LB(y)} C(x)
]

where `LB(y)` denotes unresolved load-bearing premises for `y`.

This is a governance/model equation, not a validated probabilistic law.

---

# 23. Lifecycle Variables

```yaml
L04LifecycleState:

  phase:
    type:
      - EMPTY
      - PERCEPT_ADMISSION
      - DISTINCTION_FORMATION
      - RELATION_FORMATION
      - BOUNDARY_PROPOSAL
      - BINDING_PROPOSAL
      - OBJECT_CANDIDACY
      - CONTINUITY_EVALUATION
      - IDENTITY_EVALUATION
      - ENTITY_CANDIDACY
      - VALIDATION
      - COMMIT_PENDING
      - COMMITTED
      - QUARANTINED
      - REPAIR
      - ROLLED_BACK
```

This ordering MUST NOT be interpreted as canonical mandatory serial execution. A recurrent/joint constraint architecture remains a competing implementation model until canon resolves the issue.

---

# 24. Authority Variables

```yaml
AuthorityState:

  proposer:
    type: PrincipalID | AgentID | null

  permitted_operations:
    type: CapabilityRef[]

  commit_authority:
    type: AuthorityRef | null

  authority_witness:
    type: EvidenceRef | null

  valid_from:
    type: Timestamp | null

  valid_until:
    type: Timestamp | null

  revoked:
    type: boolean

  authority_revision:
    type: RevisionID | null
```

Hard invariant:

```text
operator_available == true
does not imply
operator_authorized == true
```

---

# 25. Revision / Transaction Variables

```yaml
L04RevisionState:

  base_revision:
    type: RevisionID

  proposed_revision:
    type: RevisionID | null

  authoritative_revision:
    type: RevisionID

  proposal_id:
    type: ProposalID | null

  validation_epoch:
    type: EpochID | null

  commit_state:
    type:
      - NONE
      - PROPOSED
      - VALIDATING
      - COMMIT_READY
      - COMMITTED
      - REJECTED
      - STALE
      - ROLLED_BACK
```

Critical invariant:

```text
proposed_revision != authoritative_revision
until governed commit succeeds.
```

---

# 26. Typed Outputs

Primary candidate outputs:

```yaml
L04Output:

  object_candidates:
    type: ObjectCandidate[]

  entity_candidates:
    type: EntityCandidate[]

  competing_hypotheses:
    type: CompetingHypothesisSet[]

  contradictions:
    type: ContradictionRecord[]

  unresolved_gaps:
    type: GapRecord[]

  provenance:
    type: ProvenanceGraph

  uncertainty:
    type: L04UncertaintyVector

  proposal:
    type: StateTransitionProposal | null
```

No output automatically implies durable mutation.

---

# 27. Operators

Candidate variable-mutating operators:

```text
ADMIT_PERCEPT
QUARANTINE_PERCEPT
ADD_FEATURE

CREATE_DISTINCTION
REMOVE_DISTINCTION

RELATE
UNRELATE

PROPOSE_BOUNDARY
UPDATE_BOUNDARY
INVALIDATE_BOUNDARY

BIND
UNBIND

FORM_OBJECT_CANDIDATE
SPLIT_OBJECT
MERGE_OBJECTS
INVALIDATE_OBJECT

PROPOSE_CONTINUITY
INVALIDATE_CONTINUITY

PROPOSE_IDENTITY
SPLIT_IDENTITY
MERGE_IDENTITY
INVALIDATE_IDENTITY

FORM_ENTITY_CANDIDATE
INVALIDATE_ENTITY

REGISTER_CONTRADICTION
REGISTER_COMPETING

ATTACH_PROVENANCE

UPDATE_SCOPE
UPDATE_REGIME
UPDATE_FRESHNESS

RECALCULATE_CONFIDENCE

INVALIDATE_DEPENDENTS

PROPOSE_TRANSITION
VALIDATE_TRANSITION
REQUEST_COMMIT
ROLLBACK
```

These names are `MODEL` unless recovered from authoritative canon.

---

# 28. Variable Invariants

```text
V01
EVERY ADDRESSABLE VARIABLE MUST HAVE A TYPE.

V02
EVERY DERIVED OBJECT/ENTITY VARIABLE MUST
HAVE TRACEABLE DEPENDENCIES.

V03
LOAD-BEARING DERIVATIONS MUST RETAIN
PROVENANCE.

V04
OBJECT AND ENTITY IDENTIFIERS MUST NOT BE
SILENTLY REUSED FOR INCOMPATIBLE REFERENTS.

V05
MERGE MUST PRESERVE PRE-MERGE LINEAGE.

V06
SPLIT MUST PRESERVE PARENT LINEAGE.

V07
CONTRADICTIONS MUST NOT BE OVERWRITTEN
BY A SINGLE PREFERRED VALUE.

V08
COMPETING HYPOTHESES REQUIRE EXPLICIT STATE.

V09
UNKNOWN VALUES MUST NOT BE COERCED TO FALSE,
ZERO, EMPTY, OR PASS WHEN THOSE MEANINGS DIFFER.

V10
STALE VALUES MUST NOT BE TREATED AS CURRENT.

V11
SCOPE AND REGIME MUST PROPAGATE THROUGH
LOAD-BEARING DERIVATIONS.

V12
DERIVED CONFIDENCE MUST RESPECT THE
LOAD-BEARING CONFIDENCE CEILING.

V13
PROVENANCE INDEPENDENCE MUST NOT BE ASSUMED.

V14
VARIABLE MUTABILITY DOES NOT CONFER
COMMIT AUTHORITY.

V15
PROPOSAL STATE MUST REMAIN DISTINCT FROM
AUTHORITATIVE STATE.

V16
INVALIDATION MUST FOLLOW DEPENDENCY EDGES
RATHER THAN GLOBAL DELETION.

V17
LABELS AND ALIASES MUST NOT CREATE REFERENTS.

V18
SIMILARITY MUST NOT SILENTLY CREATE IDENTITY.

V19
CONTINUITY MUST NOT SILENTLY CREATE IDENTITY.

V20
UNKNOWN/GAP MUST REMAIN REPRESENTABLE.
```

---

# 29. Dependencies

Candidate upstream dependency chain:

```text
L03_PERCEPT_FORMATION
        ↓
admitted percepts
        ↓
L04 feature/distinction/relation state
        ↓
boundary + binding hypotheses
        ↓
object candidates
        ↓
continuity hypotheses
        ↓
identity hypotheses
        ↓
entity candidates
```

Cross-cutting dependencies:

```text
provenance
scope
regime
freshness
ontology
memory
RSCF
authority
control-plane state
```

The apparent chain is architectural, not evidence that cognition itself proceeds strictly serially.

---

# 30. H/M/L Applicability

## L — Local evidence variables

```text
PerceptRecord
FeatureRecord
DistinctionRecord
RelationRecord
ProvenanceNode
```

Question:

```text
What local evidence is actually present?
```

## M — Object-formation variables

```text
BoundaryHypothesis
BindingHypothesis
ObjectCandidate
local ContinuityHypothesis
```

Question:

```text
Which local evidence can legitimately compose into an object candidate?
```

## H — Persistent entity variables

```text
IdentityHypothesis
EntityCandidate
cross-context continuity
ontology references
long-horizon provenance
```

Question:

```text
What licenses treating object observations as the same persistent entity?
```

Hard invariant:

```text
L support != M support != H support
```

---

# 31. Control-Plane Requirements

The control plane SHOULD own or validate:

```text
authoritative revision
mutation authority
commit authority
provenance requirements
scope/regime compatibility
freshness
dependency validity
confidence ceilings
contradiction state
validation epoch
rollback lineage
```

Workers MAY propose:

```text
new distinction
new boundary
new binding
new object
new identity
new entity
```

Workers MUST NOT obtain durable authority merely because they generated a valid proposal.

---

# 32. Agents

Candidate logical roles:

```text
L04_PERCEPT_ADMISSION_AGENT
L04_DISTINCTION_AGENT
L04_BOUNDARY_AGENT
L04_BINDING_AGENT
L04_OBJECT_FORMATION_AGENT
L04_CONTINUITY_AGENT
L04_IDENTITY_AGENT
L04_ENTITY_FORMATION_AGENT
L04_PROVENANCE_AUDITOR
L04_CONTRADICTION_AUDITOR
L04_REPAIR_AGENT
```

These are role specifications, not claims of deployed agents.

---

# 33. Skills

Candidate supporting AMOS capabilities:

```text
amos-distinction-rscf-architecture
amos-binding-rscf-engine
amos-boundary-architecture-rscf-calculus
amos-persistence-dissolution-rscf-dynamics
amos-ontology-compiler
amos-provenance-trust-firewall
amos-provenance-sybil-hardening-rscf-engine
amos-constraint-propagation-rscf-engine
amos-infrastructure-control-plane
rscf-modeler
amos-claim-verifier
```

Skill availability does not establish L04 implementation.

---

# 34. Workflow

Candidate state workflow:

```text
RECEIVE L03 OUTPUT
↓
VALIDATE TYPES / PROVENANCE
↓
ADMIT OR QUARANTINE PERCEPTS
↓
EXTRACT / REGISTER FEATURES
↓
ESTABLISH DISTINCTIONS
↓
REGISTER RELATIONS
↓
PROPOSE BOUNDARIES
↓
PROPOSE BINDINGS
↓
FORM OBJECT CANDIDATES
↓
PRESERVE COMPETING OBJECT HYPOTHESES
↓
TEST CONTINUITY
↓
TEST IDENTITY
↓
FORM ENTITY CANDIDATES IF LICENSED
↓
PROPAGATE UNCERTAINTY
↓
VALIDATE DEPENDENCIES
↓
PROPOSE STATE TRANSITION
↓
CONTROL-PLANE VALIDATION
↓
COMMIT OR REJECT
```

---

# 35. Protocols

Candidate variable-facing protocols:

```text
L04_VAR_REGISTER
L04_VAR_TYPECHECK
L04_VAR_READ
L04_VAR_PROPOSE_WRITE
L04_VAR_VALIDATE_WRITE
L04_VAR_ATTACH_PROVENANCE
L04_VAR_REGISTER_DEPENDENCY
L04_VAR_MARK_COMPETING
L04_VAR_INVALIDATE
L04_VAR_REVALIDATE
L04_VAR_ROLLBACK
L04_VAR_COMMIT
```

Protocol identifiers are `MODEL`.

---

# 36. Evidence / Provenance

Every consequential variable SHOULD support reconstruction of:

```yaml
VariableEvidence:

  variable_id: null
  variable_type: null
  value: null

  epistemic_class: null

  source_refs: []

  parent_variables: []

  transformations: []

  source_versions: []

  timestamps: []

  scope: null
  regime: null
  freshness: null

  confidence_basis: []

  competing_refs: []

  contradiction_refs: []

  authority_context: null
```

No derived object/entity claim should become stronger merely because provenance metadata was omitted.

---

# 37. Uncertainty and Confidence Ceiling

The L04 confidence ceiling is governed by load-bearing evidence rather than representational completeness.

Candidate rule:

[
C(E)
\le
\min(
C(P),
C(D),
C(Bnd),
C(Bind),
C(Cont),
C(Id),
C(Prov)
)
]

only for components that are actually load-bearing for the entity claim.

Missing non-load-bearing components need not lower confidence.

Current specification-level ceiling:

```yaml
variable_architecture:
  claim_class: MODEL

canonical_variable_registry:
  claim_class: UNKNOWN/GAP
  confidence_ceiling: 0

implementation:
  claim_class: UNKNOWN/GAP
  confidence_ceiling: 0

empirical_cognitive_validity:
  claim_class: UNKNOWN/GAP
  confidence_ceiling: 0
```

---

# 38. Failure Modes

```yaml
failure_modes:

  untyped_variable:
    severity: HIGH

  identifier_collision:
    severity: CRITICAL

  object_entity_conflation:
    severity: CRITICAL

  similarity_identity_conflation:
    severity: HIGH

  continuity_identity_conflation:
    severity: HIGH

  label_referent_conflation:
    severity: HIGH

  provenance_loss:
    severity: CRITICAL

  correlated_source_inflation:
    severity: HIGH

  scope_loss:
    severity: HIGH

  regime_loss:
    severity: HIGH

  stale_state_reuse:
    severity: HIGH

  contradiction_overwrite:
    severity: CRITICAL

  competing_state_collapse:
    severity: HIGH

  confidence_inflation:
    severity: HIGH

  global_invalidation:
    severity: HIGH

  destructive_merge:
    severity: HIGH

  destructive_split:
    severity: HIGH

  proposal_commit_collapse:
    severity: CRITICAL

  authority_inference_from_capability:
    severity: CRITICAL
```

---

# 39. Repair / Recovery

Variable repair SHOULD follow:

```text
DETECT INVALID VARIABLE
↓
FREEZE AFFECTED MUTATION
↓
IDENTIFY TYPE / VALUE / PROVENANCE / DEPENDENCY FAILURE
↓
TRACE DEPENDENT DESCENDANTS
↓
PRESERVE UNAFFECTED VARIABLES
↓
QUARANTINE INVALID NODE
↓
RESTORE NEAREST VALID REVISION IF REQUIRED
↓
RECONSTRUCT FROM VALID PARENTS
↓
REVALIDATE DESCENDANTS
↓
RUN REGRESSION TESTS
↓
PROPOSE RECOMMIT
```

Repair MUST NOT erase the failed value's provenance merely to restore apparent consistency.

---

# 40. Tests / Validators

Minimum validators:

```text
L04_VARIABLE_SCHEMA_VALIDATOR
L04_TYPE_VALIDATOR
L04_IDENTIFIER_UNIQUENESS_VALIDATOR
L04_PROVENANCE_VALIDATOR
L04_DEPENDENCY_VALIDATOR
L04_SCOPE_VALIDATOR
L04_REGIME_VALIDATOR
L04_FRESHNESS_VALIDATOR
L04_CONFIDENCE_VALIDATOR
L04_DISTINCTION_VALIDATOR
L04_BOUNDARY_VALIDATOR
L04_BINDING_VALIDATOR
L04_OBJECT_VALIDATOR
L04_CONTINUITY_VALIDATOR
L04_IDENTITY_VALIDATOR
L04_ENTITY_VALIDATOR
L04_CONTRADICTION_VALIDATOR
L04_AUTHORITY_VALIDATOR
L04_REVISION_VALIDATOR
```

Required negative tests include:

```text
missing provenance
wrong variable type
duplicate incompatible ID
unsupported object creation
unsupported entity creation
false identity merge
stale evidence reuse
scope mismatch
regime mismatch
confidence inflation
correlated provenance inflation
unauthorized mutation
stale revision commit
```

These tests are specifications until executed.

---

# 41. Falsifiers

Revise this contract if authoritative canon demonstrates:

```text
different canonical variable names/types
different object/entity distinction
different identity semantics
different boundary/binding semantics
different H/M/L mapping
different provenance requirements
different state architecture
different authority architecture
different confidence semantics
```

Specific falsifier:

```text
If authoritative L04 canon defines
object and entity as the same primitive type,
the object/entity type separation here is invalid.
```

Another:

```text
If canonical L04 uses joint probabilistic state
rather than individually addressable hypotheses,
the candidate record decomposition must be
treated as an interface projection rather than
canonical internal representation.
```

---

# 42. Gap Status

```yaml
gap_status:

  source_governance:
    status: SOURCE_ALIGNED

  variable_architecture:
    status: MODEL_DEFINED

  percept_variables:
    status: MODEL_DEFINED

  feature_variables:
    status: MODEL_DEFINED

  distinction_variables:
    status: MODEL_DEFINED

  relation_variables:
    status: MODEL_DEFINED

  boundary_variables:
    status: MODEL_DEFINED

  binding_variables:
    status: MODEL_DEFINED

  object_variables:
    status: MODEL_DEFINED

  continuity_variables:
    status: MODEL_DEFINED

  identity_variables:
    status: MODEL_DEFINED

  entity_variables:
    status: MODEL_DEFINED

  provenance_variables:
    status: MODEL_DEFINED

  uncertainty_variables:
    status: MODEL_DEFINED

  authority_variables:
    status: MODEL_DEFINED

  canonical_variable_registry:
    status: UNKNOWN_GAP

  canonical_types:
    status: UNKNOWN_GAP

  canonical_equations:
    status: UNKNOWN_GAP

  canonical_thresholds:
    status: UNKNOWN_GAP

  executable_implementation:
    status: UNKNOWN_GAP

  runtime_validation:
    status: UNKNOWN_GAP

  empirical_validation:
    status: UNKNOWN_GAP
```

---

# 43. RSCF Capsule

```yaml
rscf:

  id: L04_OBJECT_ENTITY_FORMATION_VARIABLES

  claim:
    L04 requires a typed representation capable of
    preserving percept evidence, distinctions, relations,
    boundaries, bindings, object hypotheses, continuity,
    identity, entity hypotheses, provenance, uncertainty,
    dependencies, scope/regime, and authority state.

  claim_class: MODEL

  evidence:
    - AMOS_cognition_governance_constraints

  provenance:
    origin_architect: Trang Phan
    framework: AMOS
    primitive: L04_OBJECT_ENTITY_FORMATION
    artifact: VARIABLES.md

  scope:
    candidate_L04_variable_contract

  regime:
    governed_cognitive_primitive_architecture

  freshness:
    current_document_revision

  dependencies:
    - L03_PERCEPT_FORMATION
    - L04_DEFINITION
    - L04_STATE
    - L04_INVARIANTS
    - L04_PROVENANCE
    - L04_CONTROL_PLANES

  competing:
    - staged_variable_model
    - recurrent_state_model
    - joint_constraint_model
    - probabilistic_object_entity_model

  falsifiers:
    - authoritative_L04_variable_canon_conflict
    - canonical_object_entity_semantic_conflict
    - incompatible_runtime_state_model

  confidence_ceiling:
    MODEL only. Exact canonical variables and runtime
    implementation remain unresolved.

  gap_status:
    canonical_variables: UNKNOWN_GAP
    implementation: UNKNOWN_GAP
    empirical_validation: UNKNOWN_GAP
```

---

# 44. Completion State

```yaml
completion_state:

  source_canon_references:
    status: SOURCE_BOUND_WITH_CANON_GAP

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

  gap_status:
    status: MODEL_COMPLETE

  canonical_variable_registry:
    status: UNKNOWN_GAP

  implementation:
    status: UNKNOWN_GAP

  validation:
    status: UNKNOWN_GAP

  claim_class:
    MODEL
```

---

# 45. Hard Boundaries

```text
PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

UNKNOWN/GAP != PASS
```

Variable-specific boundaries:

```text
VARIABLE != OBSERVATION

LABEL != REFERENT

FEATURE != OBJECT

OBJECT != ENTITY

OBJECT_CANDIDATE != VALIDATED_OBJECT

ENTITY_CANDIDATE != VERIFIED_ENTITY

SIMILARITY != IDENTITY

CONTINUITY != IDENTITY

RELATION != CAUSATION

BOUNDARY != PROOF_OF_OBJECTHOOD

BINDING != PROOF_OF_IDENTITY

MULTIPLE SOURCES != INDEPENDENT SOURCES

CONFIDENCE != EVIDENCE

STALE != CURRENT

MISSING != FALSE

UNKNOWN != ZERO

COMPETING != RESOLVED

MUTABLE != AUTHORIZED

PROPOSED_REVISION != AUTHORITATIVE_REVISION
```

---

# 46. Governing Variable Contract

> **`L04_OBJECT_ENTITY_FORMATION` SHALL preserve typed separation among percepts, features, distinctions, relations, boundaries, bindings, object candidates, continuity hypotheses, identity hypotheses, and entity candidates. Every consequential derived variable SHALL retain sufficient provenance, dependency, scope, regime, freshness, epistemic-class, and uncertainty information to determine whether downstream reuse remains licensed. Similarity, naming, adjacency, temporal sequence, or structural resemblance SHALL NOT silently establish identity. Contradictions and genuinely competing object/entity hypotheses SHALL remain representable. Derived confidence SHALL NOT exceed unresolved load-bearing support without independent revalidation. Invalidating one variable SHALL selectively invalidate its dependent descendants rather than unrelated state. Variable mutability SHALL NOT imply authority, and proposed state SHALL remain distinct from authoritative committed state. Missing canonical semantics SHALL remain `UNKNOWN/GAP` rather than being filled by implementation convenience.**

---

# 47. Final Classification

```text
CONCLUSION CLASS:
MODEL

VARIABLE CONTRACT:
MODEL-COMPLETE FOR DOCUMENTATION SCOPE

AUTHORITATIVE L04 VARIABLE REGISTRY:
UNKNOWN/GAP

CANONICAL TYPES / THRESHOLDS:
UNKNOWN/GAP

EXECUTABLE IMPLEMENTATION:
NOT ESTABLISHED

RUNTIME VALIDATION:
NOT ESTABLISHED

EMPIRICAL COGNITIVE VALIDATION:
NOT ESTABLISHED

PROMOTION TO IMPLEMENTED / VALIDATED:
BLOCKED
```

```
```

---

00_ROOT_MOC|AMOS MOC

---
**Related:** [[00_HOME]] · [[COGNITIVE_MATRIX_MOC]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: l04_object_entity_formation_primitives_cognitive_matrix_variables
node_type: note
path: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L04_OBJECT_ENTITY_FORMATION/L04_OBJECT_ENTITY_FORMATION_PRIMITIVES_COGNITIVE_MATRIX_VARIABLES.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[L04_OBJECT_ENTITY_FORMATION_MOC]]
