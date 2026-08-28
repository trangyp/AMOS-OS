---
type: variable
source: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L03_PERCEPT_FORMATION
tags:
- amos
- cognitive-matrix
- l03
- percept-formation
- variables
- variable-registry
- rscf
- provenance
- governance
- canon/cognitive-matrix
title: L03_PERCEPT_FORMATION — Variables
origin_architect: Trang Phan
status: MODEL_CONTRACT / UNVALIDATED
epistemic_class: MODEL
runtime_alignment: AMOS Full Brain OS / AMOS_CORE v4.4 lineage
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


# L03_PERCEPT_FORMATION — Variables

**Class:** `COGNITIVE_PRIMITIVE_VARIABLE_CONTRACT`
**Origin architect / steward:** Trang Phan
**Primitive:** `L03_PERCEPT_FORMATION`
**Artifact:** `VARIABLES.md`
**Status:** `AMOS_MODEL / UNVALIDATED`

## 0. Purpose

Define the governed variable contract for `L03_PERCEPT_FORMATION`.

This artifact specifies how variables used by percept formation are named, typed, scoped, versioned, related, transformed, provenance-bound, validated, invalidated, and exchanged with adjacent AMOS layers.

The AMOS Universal Variable Registry defines a variable object as:

```text
V = (
  symbol,
  canonical_name,
  type,
  unit,
  domain,
  scale,
  time,
  regime,
  observer,
  provenance,
  status
)
```

with registry tensor:

```text
VR[
  variable,
  domain,
  scale,
  unit,
  regime,
  version,
  status
]
```

and compatibility rule:

```text
Compat(V_i,V_j)
=
TypeMatch
AND UnitCompatible
AND DomainCompatible
AND ScopeCompatible
```

For L03, this means a variable name alone is never sufficient to establish semantic identity or composability.

Core boundary:

```text
SYMBOL != VARIABLE

LABEL != SEMANTICS

SAME_NAME != SAME_VARIABLE

ALIAS != IDENTITY_UNLESS_PROVEN

TYPE_COMPATIBLE != SEMANTICALLY_EQUIVALENT

CROSS_SCALE_SIMILARITY != VALID_TRANSFORM

DERIVED_VARIABLE != SOURCE_OBSERVATION

VARIABLE_DEFINED != VARIABLE_OBSERVED

PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

UNKNOWN/GAP != PASS
```

---

# 1. Source / Canon References

## 1.1 Source-aligned variable architecture

The AMOS Universal Variable Registry provides the currently source-aligned variable-management rules used here.

Its hard invariants include:

```text
1. Same symbol does not imply same variable.

2. Same label across domains does not imply
   comparable units or mechanisms.

3. Unit/type mismatch is a hard failure.

4. Derived variables retain parent provenance.

5. Aliases cannot erase version or regime differences.

6. Cross-scale mapping requires explicit transform.

7. Unknown semantics block composition.

8. Registry status is not empirical validation.
```

It also defines:

```text
Bind(V_i,Q_j,role)
```

for equation binding and permits:

```text
Alias(V_i,V_j)
```

only where semantic identity and scope equivalence are established.

The associated AMOS formal contract includes:

```text
T[o,p,s,t,r,v,g,e,c,k]

R[
  i,
  j,
  relation_type,
  time,
  regime,
  provenance
]

Admit(x) = AND_i I_i(x)

X_(t+1) = P_I(F(X_t,U_t,E_t,M_t))
```

and the RSCF node/edge structures used for provenance and dependency control.

## 1.2 Relevant architecture families

```text
AMOS Cognition
AMOS Full Brain OS
AMOS Universal Variable Registry
AMOS Universal Coordinate System
AMOS Distinction Architecture
AMOS Binding Architecture
AMOS Attention Allocation Governor
AMOS Multimodal Perception Layer
AMOS H/M/L
AMOS RSCF
AMOS Provenance
AMOS Constraint Propagation
AMOS Infrastructure Control Plane
```

## 1.3 Direct L03 variable canon status

```yaml
canonical_L03_variable_registry: UNKNOWN_GAP
canonical_L03_symbols: UNKNOWN_GAP
canonical_L03_types: UNKNOWN_GAP
canonical_L03_units: UNKNOWN_GAP
canonical_L03_domains: UNKNOWN_GAP
canonical_L03_equation_bindings: UNKNOWN_GAP
canonical_L03_aliases: UNKNOWN_GAP
canonical_L03_cross_scale_transforms: UNKNOWN_GAP
canonical_L03_thresholds: UNKNOWN_GAP
```

Therefore the L03-specific variable names below are `AMOS_MODEL` unless later recovered from direct canon.

---

# 2. Definition and Scope

`L03_PERCEPT_FORMATION_VARIABLE_CONTRACT` governs variables required to represent the transformation from admitted observations and attention-conditioned information into candidate perceptual structures.

Conceptual scope:

```text
observations
attention state
features
relations
bindings
candidate percepts
competing percepts
memory context
H/M/L coordinates
scope
regime
freshness
observer context
provenance
dependency state
uncertainty
confidence
failure state
repair state
authority state
```

The registry does **not** establish that these variables correspond to biological neural variables or objectively correct perceptual states.

Unless independently validated:

```text
L03 variables = AMOS representational variables
```

not:

```text
biological observables
neural mechanisms
physical laws
empirical cognitive primitives
```

---

# 3. Canonical Variable Object

Every L03 variable SHOULD resolve to an object compatible with:

```yaml
L03Variable:

  id:
    type: VariableID

  symbol:
    type: Symbol

  canonical_name:
    type: string

  semantic_definition:
    type: string

  variable_type:
    type: TypeRef

  unit:
    type: UnitRef | DIMENSIONLESS | NONE | UNKNOWN

  domain:
    type: DomainRef

  scale:
    type: HMLScale | CrossScale

  time:
    type: TimeCoordinate | null

  regime:
    type: RegimeRef | null

  observer:
    type: ObserverRef | null

  scope:
    type: ScopeEnvelope

  provenance:
    type: ProvenanceGraph

  parents:
    type: VariableID[]

  derivation:
    type: OperatorRef | null

  equation_bindings:
    type: EquationBinding[]

  aliases:
    type: AliasRef[]

  freshness:
    type: FreshnessState

  uncertainty:
    type: UncertaintyVector

  confidence_ceiling:
    type: ConfidenceBound

  status:
    type:
      - SOURCE_DEFINED
      - OBSERVED
      - DERIVED
      - MODEL
      - CONDITIONAL
      - COMPETING
      - STALE
      - QUARANTINED
      - INVALID
      - UNKNOWN_GAP
```

This specializes the Universal Variable Registry object for L03 while preserving its source-aligned dimensions.

---

# 4. Typed Inputs

Candidate L03 input variables:

```yaml
L03InputVariables:

  O:
    canonical_name: observation_state
    type: ObservationState[]
    epistemic_role: OBSERVATION
    source_layer: L01_SENSING_OBSERVATION

  A:
    canonical_name: attention_state
    type: AttentionState
    epistemic_role: CONTROL_WEIGHT
    source_layer: L02_ATTENTION

  M:
    canonical_name: memory_context
    type: MemoryContext[]
    epistemic_role: CONTEXT
    source_layer: MEMORY

  Ctx:
    canonical_name: context_state
    type: ContextState
    epistemic_role: CONTEXT

  Sc:
    canonical_name: scope_envelope
    type: ScopeEnvelope

  Rg:
    canonical_name: regime_envelope
    type: RegimeEnvelope

  Obs:
    canonical_name: observer_context
    type: ObserverContext

  Prov:
    canonical_name: provenance_graph
    type: ProvenanceGraph

  Auth:
    canonical_name: authority_context
    type: AuthorityContext | null
```

These symbols are proposed convenience symbols, not recovered canonical L03 notation.

---

# 5. Typed Outputs

Candidate outputs:

```yaml
L03OutputVariables:

  F:
    canonical_name: feature_state
    type: FeatureState[]

  Rel:
    canonical_name: relation_state
    type: RelationState[]

  B:
    canonical_name: binding_state
    type: BindingState[]

  P:
    canonical_name: percept_candidate_set
    type: PerceptCandidate[]

  P_star:
    canonical_name: selected_percept_proposal
    type: PerceptProposal | null

  Comp:
    canonical_name: competing_percepts
    type: CompetingPerceptSet

  Dep:
    canonical_name: dependency_graph
    type: DependencyGraph

  Prov_out:
    canonical_name: output_provenance
    type: ProvenanceGraph

  U:
    canonical_name: uncertainty_state
    type: UncertaintyVector

  Conf:
    canonical_name: confidence_ceiling
    type: ConfidenceBound

  Gap:
    canonical_name: gap_state
    type: GapState[]

  Fail:
    canonical_name: failure_state
    type: FailureState[]

  Proposal:
    canonical_name: percept_state_proposal
    type: StateProposal
```

Hard boundary:

```text
P_star != COMMITTED_PERCEPT_STATE
```

unless an authorized control plane performs the commit.

---

# 6. Core State Variables

Candidate state vector:

```text
X_L03(t) =
[
  O_t,
  A_t,
  F_t,
  Rel_t,
  B_t,
  P_t,
  Comp_t,
  M_t,
  Dep_t,
  Prov_t,
  Scope_t,
  Regime_t,
  Fresh_t,
  U_t,
  Conf_t,
  Gap_t,
  Fail_t
]
```

`AMOS_MODEL`.

Expanded registry:

| Symbol     | Meaning                 | Type                  | Epistemic role |
| ---------- | ----------------------- | --------------------- | -------------- |
| `O_t`      | admitted observations   | `ObservationState[]`  | OBSERVATION    |
| `A_t`      | attention allocation    | `AttentionState`      | CONTROL        |
| `F_t`      | derived features        | `FeatureState[]`      | DERIVED        |
| `Rel_t`    | candidate relations     | `RelationState[]`     | DERIVED        |
| `B_t`      | candidate bindings      | `BindingState[]`      | DERIVED        |
| `P_t`      | candidate percepts      | `PerceptCandidate[]`  | MODEL/DERIVED  |
| `Comp_t`   | unresolved competitors  | `CompetingPerceptSet` | COMPETING      |
| `M_t`      | relevant memory context | `MemoryContext[]`     | CONTEXT        |
| `Dep_t`    | dependency graph        | `DependencyGraph`     | CONTROL        |
| `Prov_t`   | provenance graph        | `ProvenanceGraph`     | CONTROL        |
| `Scope_t`  | applicability scope     | `ScopeEnvelope`       | CONTROL        |
| `Regime_t` | operating regime        | `RegimeEnvelope`      | CONTROL        |
| `Fresh_t`  | freshness state         | `FreshnessState`      | CONTROL        |
| `U_t`      | uncertainty             | `UncertaintyVector`   | EPISTEMIC      |
| `Conf_t`   | confidence ceiling      | `ConfidenceBound`     | EPISTEMIC      |
| `Gap_t`    | unresolved gaps         | `GapState[]`          | EPISTEMIC      |
| `Fail_t`   | active failures         | `FailureState[]`      | CONTROL        |

---

# 7. Observation Variables

Observation variables MUST retain source semantics.

Candidate structure:

```yaml
ObservationVariable:

  observation_id: ObservationID

  modality:
    type:
      - TEXT
      - VISUAL
      - AUDIO
      - SOMATIC
      - INTEROCEPTIVE
      - SENSOR
      - TOOL
      - DOCUMENT
      - EXTERNAL_STATE
      - OTHER

  value:
    type: TypedValue

  measurement_method:
    type: MethodRef | null

  timestamp:
    type: Timestamp

  source:
    type: SourceRef

  observer:
    type: ObserverRef | null

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeEnvelope

  provenance:
    type: ProvenanceGraph

  uncertainty:
    type: UncertaintyVector
```

Invariant:

```text
O.value
MUST NOT
be silently replaced by interpretation(P).
```

---

# 8. Attention Variables

Candidate attention variables:

```text
a_i      = attention weight for item i
sal_i    = salience component
goal_i   = goal-relevance component
nov_i    = novelty component
thr_i    = threat/urgency component
unc_i    = uncertainty component
time_i   = time-sensitivity component
cost_i   = processing-cost component
```

These are model-level mappings.

Hard invariant:

```text
a_i != truth_probability_i
```

and:

```text
a_i != evidence_strength_i
```

Attention may affect processing allocation without automatically changing epistemic status.

---

# 9. Feature Variables

Candidate:

```yaml
FeatureVariable:

  feature_id: FeatureID

  feature_type:
    type: FeatureType

  value:
    type: TypedValue

  parents:
    type: ObservationID[]

  derivation_operator:
    type: OperatorRef

  scale:
    type: HMLScale

  provenance:
    type: ProvenanceGraph

  uncertainty:
    type: UncertaintyVector
```

Invariant:

```text
Derived(F_i)
=>
retain_provenance(parents(F_i))
```

This directly follows the Universal Variable Registry requirement that derived variables retain parent provenance.

---

# 10. Relation Variables

Candidate relation tensor:

```text
R_L03[
  source_variable,
  target_variable,
  relation_type,
  time,
  regime,
  provenance
]
```

This specializes the source-aligned AMOS relation structure.

Candidate relation types:

```text
TEMPORAL
SPATIAL
SIMILARITY
CONTRAST
CONTAINMENT
ADJACENCY
CO_OCCURRENCE
DEPENDENCY
POSSIBLE_CAUSAL
MECHANISTIC
IDENTITY_CANDIDATE
PART_OF
UNKNOWN
```

Hard boundary:

```text
CO_OCCURRENCE != CAUSATION
```

---

# 11. Binding Variables

Candidate:

```yaml
BindingVariable:

  binding_id: BindingID

  members:
    type: VariableID[]

  binding_type:
    type: BindingType

  support:
    type: EvidenceRef[]

  alternatives:
    type: BindingID[]

  dependency_graph:
    type: DependencyGraph

  provenance:
    type: ProvenanceGraph

  confidence_ceiling:
    type: ConfidenceBound

  status:
    type:
      - CANDIDATE
      - CONDITIONAL
      - COMPETING
      - REJECTED
      - INVALID
```

Hard boundary:

```text
BOUND(X,Y) != IDENTICAL(X,Y)
```

unless identity is separately established.

---

# 12. Percept Variables

Candidate percept object:

```yaml
PerceptCandidate:

  percept_id: PerceptID

  observation_refs:
    type: ObservationID[]

  feature_refs:
    type: FeatureID[]

  relation_refs:
    type: RelationID[]

  binding_refs:
    type: BindingID[]

  memory_refs:
    type: MemoryRef[]

  competing_refs:
    type: PerceptID[]

  HML_state:
    type: HMLState

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeEnvelope

  observer:
    type: ObserverRef | null

  provenance:
    type: ProvenanceGraph

  dependency_graph:
    type: DependencyGraph

  uncertainty:
    type: UncertaintyVector

  confidence_ceiling:
    type: ConfidenceBound

  epistemic_class:
    type:
      - DERIVED
      - MODEL
      - CONDITIONAL
      - COMPETING
      - UNKNOWN_GAP
```

A percept candidate is not automatically typed as `OBSERVATION`.

---

# 13. Competing-Hypothesis Variables

```yaml
CompetingPerceptSet:

  set_id: CompetingSetID

  candidates:
    type: PerceptID[]

  shared_evidence:
    type: EvidenceRef[]

  discriminating_evidence:
    type: EvidenceRef[]

  unresolved_variables:
    type: VariableID[]

  cheapest_discriminating_test:
    type: TestRef | null

  status:
    type:
      - ACTIVE
      - PARTIALLY_RESOLVED
      - RESOLVED
      - UNKNOWN_GAP
```

Invariant:

```text
ComparableSupport(P1,P2)
AND
NoDiscriminator
=>
Preserve(COMPETING)
```

---

# 14. Memory Variables

Candidate:

```text
M_id       = memory identity
M_value    = memory content
M_origin   = semantic origin
M_time     = memory formation/update time
M_scope    = applicability scope
M_regime   = validity regime
M_fresh    = freshness
M_conf     = confidence
M_prov     = provenance
```

Hard boundaries:

```text
M_value != CURRENT_OBSERVATION

M_conf != CURRENT_EVIDENCE_STRENGTH

RETRIEVED != VALID

REMEMBERED != OBSERVED_NOW
```

---

# 15. H/M/L Variables

Candidate scale variable:

```yaml
HMLCoordinate:

  H:
    type: GoverningPerceptState | null

  M:
    type: IntermediatePerceptState[] | null

  L:
    type: LocalFeatureObservationState[] | null
```

Cross-scale transforms require explicit mapping.

This follows the source invariant:

```text
Cross-scale mapping requires explicit transform.
```

Candidate mappings:

```text
T_LM : L → M
T_MH : M → H
T_HM : H → M
T_ML : M → L
```

All are `AMOS_MODEL` until canonical L03 transforms are recovered.

---

# 16. Provenance Variables

```text
Prov_src    = direct source provenance
Prov_der    = derivation provenance
Prov_mem    = memory provenance
Prov_agent  = agent provenance
Prov_tool   = tool provenance
Prov_parent = parent-variable provenance
Prov_epoch  = validation epoch
```

Every load-bearing derived variable must preserve ancestry sufficient to reconstruct its support path.

Hard invariant:

```text
DERIVED_WITHOUT_RECOVERABLE_PARENT_PROVENANCE
=>
QUARANTINE | UNKNOWN/GAP
```

---

# 17. Uncertainty Variables

Candidate vector:

```text
U_L03 =
[
  U_evidence,
  U_model,
  U_scope,
  U_temporal,
  U_causal,
  U_execution,
  U_provenance_independence
]
```

These dimensions SHOULD remain distinct when materially decision-relevant.

Forbidden compression:

```text
U_L03 → one scalar
```

when doing so hides a load-bearing uncertainty dimension.

---

# 18. Confidence Variables

```text
Conf_obs
Conf_feature
Conf_relation
Conf_binding
Conf_percept
Conf_provenance
Conf_scope
Conf_regime
```

Source-aligned confidence ceiling:

[
Conf(C)
\leq
\min Conf(\text{load-bearing premises})
]

unless independently revalidated.

Candidate percept specialization:

[
Conf(P)
\leq
\min(
Conf(O),
Conf(F),
Conf(Rel),
Conf(B),
Conf(Prov),
Conf(Scope),
Conf(Regime)
)
]

`AMOS_MODEL`.

---

# 19. Freshness Variables

```yaml
FreshnessState:

  observed_at:
    type: Timestamp | null

  validated_at:
    type: Timestamp | null

  expires_at:
    type: Timestamp | null

  regime_at_validation:
    type: RegimeRef | null

  dependency_epoch:
    type: EpochRef | null

  status:
    type:
      - CURRENT
      - STALE
      - EXPIRED
      - UNKNOWN
```

Hard rule:

```text
STALE != CURRENT
```

and stale load-bearing variables require revalidation before reuse where freshness matters.

---

# 20. Scope / Regime Variables

Candidate:

```text
Scope =
[
  system,
  population,
  environment,
  modality,
  scale,
  observer,
  measurement_method
]

Regime =
[
  operating_context,
  environmental_state,
  task_state,
  temporal_state,
  dependency_epoch
]
```

Variables inherited from one envelope MUST NOT silently cross into another incompatible envelope.

---

# 21. Dependency Variables

Candidate dependency edge:

```yaml
VariableDependency:

  parent:
    type: VariableID

  child:
    type: VariableID

  edge_type:
    type:
      - DERIVES
      - SUPPORTS
      - CONSTRAINS
      - CONDITIONS
      - INVALIDATES
      - TRANSFORMS
      - ALIASES

  load_bearing:
    type: boolean

  independence:
    type:
      - DEMONSTRATED
      - CORRELATED
      - UNKNOWN

  condition:
    type: Predicate | null
```

This is aligned with the AMOS RSCF edge model:

```text
E = (
  parent,
  child,
  edge_type,
  load_bearing,
  independence,
  condition
)
```

---

# 22. Equation Binding

Every equation involving L03 variables SHOULD declare bindings explicitly.

Example:

```text
Bind(O, Q_percept, INPUT)
Bind(A, Q_percept, CONTROL)
Bind(M, Q_percept, CONTEXT)
Bind(P, Q_percept, OUTPUT)
```

The Universal Variable Registry defines `Bind(V_i,Q_j,role)` for this purpose.

A symbol appearing in an equation without a valid registry binding is:

```text
UNBOUND_VARIABLE
```

and SHOULD fail validation when load-bearing.

---

# 23. Alias Rules

Aliases are permitted only where semantic identity and scope equivalence are established.

Therefore:

```text
Alias(V_i,V_j)
requires:

semantic_identity
AND type_compatibility
AND unit_compatibility
AND domain_compatibility
AND scope_equivalence
AND regime_compatibility
AND version_compatibility
```

Candidate aliases MUST NOT erase:

```text
version
regime
observer
scope
provenance
```

---

# 24. Operators

Candidate variable-management operators:

```text
REGISTER_VARIABLE
RESOLVE_VARIABLE
TYPE_CHECK
UNIT_CHECK
DOMAIN_CHECK
SCOPE_CHECK
REGIME_CHECK
FRESHNESS_CHECK
BIND_EQUATION
DECLARE_ALIAS
REJECT_ALIAS
DERIVE_VARIABLE
TRANSFORM_SCALE
LINK_PROVENANCE
LINK_DEPENDENCY
MARK_COMPETING
MARK_STALE
QUARANTINE_VARIABLE
INVALIDATE_VARIABLE
REVALIDATE_VARIABLE
SUPERSEDE_VARIABLE
PROPOSE_STATE_UPDATE
```

These are model-level names.

---

# 25. Variable Admission Gate

Source-aligned general gate:

[
Admit(x)=\bigwedge_i I_i(x)
]

Candidate L03 specialization:

[
Admit(V)=
TypeValid
\land
SemanticDefined
\land
ScopeValid
\land
RegimeValid
\land
ProvenanceSufficient
\land
NoHardConflict
]

`AMOS_MODEL`.

For variables with units:

```text
AND UnitValid
```

For derived variables:

```text
AND ParentLineageRecoverable
```

---

# 26. Governed State Transition

The Universal Variable Registry provides:

[
X_{t+1}=P_I(F(X_t,U_t,E_t,M_t))
]

as an AMOS formal contract.

For L03, interpret only structurally:

```text
current percept-formation state
+
inputs
+
environment/context
+
memory
→ candidate transition
→ invariant projection
→ proposed next state
```

This does not establish a biological law of perception.

---

# 27. Variable Invariants

```text
VAR-L03-001
SAME SYMBOL != SAME VARIABLE.

VAR-L03-002
SAME LABEL != SAME SEMANTICS.

VAR-L03-003
TYPE MISMATCH = HARD FAILURE.

VAR-L03-004
UNIT MISMATCH = HARD FAILURE WHERE UNITS APPLY.

VAR-L03-005
UNKNOWN SEMANTICS BLOCK COMPOSITION.

VAR-L03-006
DERIVED VARIABLES RETAIN PARENT PROVENANCE.

VAR-L03-007
ALIASES MUST NOT ERASE VERSION DIFFERENCE.

VAR-L03-008
ALIASES MUST NOT ERASE REGIME DIFFERENCE.

VAR-L03-009
CROSS-SCALE MAPPING REQUIRES EXPLICIT TRANSFORM.

VAR-L03-010
REGISTRY STATUS != EMPIRICAL VALIDATION.

VAR-L03-011
OBSERVATION != PERCEPT CANDIDATE.

VAR-L03-012
ATTENTION WEIGHT != TRUTH VALUE.

VAR-L03-013
MEMORY VALUE != CURRENT OBSERVATION.

VAR-L03-014
RELATION != CAUSATION.

VAR-L03-015
BINDING != IDENTITY.

VAR-L03-016
COMPETING VARIABLES MUST REMAIN DISTINCT UNTIL RESOLVED.

VAR-L03-017
PROVENANCE CORRELATION MUST NOT CREATE FALSE INDEPENDENCE.

VAR-L03-018
STALE VARIABLE MUST NOT SILENTLY FUNCTION AS CURRENT.

VAR-L03-019
VARIABLE CONFIDENCE MUST NOT EXCEED LOAD-BEARING SUPPORT.

VAR-L03-020
INVALID PARENT INVALIDATES DEPENDENT DESCENDANTS.

VAR-L03-021
INVALIDATION SHOULD BE SELECTIVE, NOT GLOBAL BY DEFAULT.

VAR-L03-022
SCOPE CHANGE REQUIRES COMPATIBILITY CHECK.

VAR-L03-023
REGIME CHANGE REQUIRES COMPATIBILITY CHECK.

VAR-L03-024
OBSERVER CHANGE MUST NOT BE SILENT WHEN OBSERVER-DEPENDENT.

VAR-L03-025
VARIABLE DEFINITION != VARIABLE VALUE.

VAR-L03-026
VARIABLE VALUE != VERIFIED EXTERNAL FACT.

VAR-L03-027
VARIABLE ADDRESSABILITY != IMPLEMENTATION.

VAR-L03-028
VARIABLE MUTABILITY != AUTHORITY TO MUTATE.

VAR-L03-029
PROPOSED VARIABLE UPDATE != COMMITTED STATE.

VAR-L03-030
UNKNOWN/GAP != VALID DEFAULT.
```

---

# 28. Dependencies

## Upstream

```text
L01_SENSING_OBSERVATION
L02_ATTENTION
```

## L03 internal

```text
L03/README
L03/PURPOSE
L03/DEFINITION
L03/STATE
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
L03/RSCF
L03/TESTS
L03/GAP_MATRIX
```

## Cross-cutting

```text
AMOS Universal Variable Registry
AMOS Universal Coordinate System
AMOS RSCF
AMOS H/M/L
AMOS Provenance
AMOS Constraint Propagation
AMOS Control Plane
AMOS Context / Memory Governance
```

---

# 29. H/M/L Applicability

## L — Local variables

```text
individual observations
local features
local relation candidates
timestamps
source identities
local uncertainty
```

## M — Intermediate variables

```text
object/event candidates
feature groups
binding groups
memory-supported structures
intermediate percepts
subsystem dependency structures
```

## H — Governing variables

```text
global percept candidate set
scope
regime
observer context
confidence ceiling
competing interpretation state
authority state
system-level provenance
```

Hard boundary:

```text
V_L
cannot become
V_M or V_H
without explicit transform.
```

---

# 30. Control-Plane Requirements

The variable layer may define and propose variable transformations.

It does not own durable authority merely because a variable is technically mutable.

Control-plane responsibilities include:

```text
registry identity
schema/version authority
variable admission
alias approval
cross-scale transform approval
scope/regime validation
freshness
dependency epochs
authority
commit eligibility
rollback
```

Before durable mutation:

```text
REVALIDATE:
  variable identity
  schema version
  parent state
  dependencies
  provenance
  scope
  regime
  freshness
  authority
```

---

# 31. Agents

Candidate agents:

```text
L03_VARIABLE_REGISTRY_AGENT
L03_TYPE_VALIDATION_AGENT
L03_ALIAS_RESOLUTION_AGENT
L03_PROVENANCE_AGENT
L03_HML_MAPPING_AGENT
L03_DEPENDENCY_AGENT
L03_VARIABLE_AUDITOR_AGENT
L03_REPAIR_AGENT
```

Hard rule:

```text
AGENT_CAN_EDIT_VARIABLE
!=
AGENT_AUTHORIZED_TO_COMMIT_VARIABLE
```

---

# 32. Skills

Relevant capability families:

```text
AMOS Universal Variable Registry
AMOS Universal Coordinate System
AMOS RSCF Modeler
AMOS Claim Verifier
AMOS Constraint Propagation
AMOS Provenance Trust Firewall
AMOS Cross-Scale Tensor Engine
AMOS Mathematical Rigor Kernel
AMOS Control Plane
AMOS Repair Architecture
```

A Skill's existence establishes addressable capability only.

---

# 33. Workflow

```text
RECEIVE VARIABLE
↓
RESOLVE IDENTITY
↓
RESOLVE SEMANTICS
↓
TYPE CHECK
↓
UNIT CHECK IF APPLICABLE
↓
DOMAIN CHECK
↓
SCOPE / REGIME CHECK
↓
PROVENANCE CHECK
↓
DEPENDENCY CHECK
↓
H/M/L COORDINATE CHECK
↓
ALIAS / COLLISION CHECK
↓
ADMIT OR QUARANTINE
↓
BIND TO OPERATORS / EQUATIONS
↓
DERIVE CANDIDATE VARIABLES
↓
PROPAGATE PROVENANCE
↓
PROPAGATE UNCERTAINTY
↓
APPLY CONFIDENCE CEILING
↓
PROPOSE STATE UPDATE
↓
CONTROL-PLANE REVALIDATION
↓
COMMIT OR REJECT
```

---

# 34. Protocols

Candidate protocols:

```text
L03_VAR_DECLARE
L03_VAR_REGISTER
L03_VAR_RESOLVE
L03_VAR_TYPE_CHECK
L03_VAR_ALIAS_REQUEST
L03_VAR_ALIAS_REJECT
L03_VAR_BIND
L03_VAR_DERIVE
L03_VAR_TRANSFORM
L03_VAR_INVALIDATE
L03_VAR_REVALIDATE
L03_VAR_QUARANTINE
L03_VAR_SUPERSEDE
L03_VAR_STATE_PROPOSAL
```

Canonical protocol names remain `UNKNOWN/GAP`.

---

# 35. Evidence / Provenance

Every material variable SHOULD retain:

```yaml
VariableProvenance:

  variable_id: null

  source_ref: null

  semantic_origin: null

  parent_variables: []

  derivation_operator: null

  equation_bindings: []

  created_at: null

  validated_at: null

  observer: null

  scope: null

  regime: null

  version: null

  provenance_graph: []

  evidence_refs: []
```

Derived variables without sufficient lineage cannot receive stronger epistemic status merely because their values appear plausible.

---

# 36. Failure Modes

```text
VFM-001
Symbol collision.

VFM-002
Same-name semantic collision.

VFM-003
Type mismatch.

VFM-004
Unit mismatch.

VFM-005
Domain mismatch.

VFM-006
Scope mismatch.

VFM-007
Regime mismatch.

VFM-008
Observer-context loss.

VFM-009
Version-erasing alias.

VFM-010
Regime-erasing alias.

VFM-011
Unbound equation variable.

VFM-012
Undefined variable semantics.

VFM-013
Derived variable loses parent provenance.

VFM-014
Cross-scale transform is implicit.

VFM-015
Attention variable treated as truth variable.

VFM-016
Memory variable treated as observation variable.

VFM-017
Relation variable treated as causal proof.

VFM-018
Binding variable treated as identity proof.

VFM-019
Stale variable reused as current.

VFM-020
Correlated evidence counted independently.

VFM-021
Competing variables silently collapsed.

VFM-022
Confidence exceeds weakest premise.

VFM-023
Parent invalidated but child remains active.

VFM-024
Local invalidation causes unnecessary global deletion.

VFM-025
Registry entry mistaken for implementation.

VFM-026
Variable definition mistaken for empirical validation.

VFM-027
Technical mutability mistaken for authority.

VFM-028
Proposal mistaken for committed variable state.

VFM-029
UNKNOWN semantic value defaulted silently.

VFM-030
Canonical variable invented to fill a corpus gap.
```

---

# 37. Repair / Recovery

Candidate repair sequence:

```text
DETECT VARIABLE FAILURE
↓
FREEZE AFFECTED BRANCH
↓
LOCATE EARLIEST INVALID VARIABLE / EDGE
↓
CLASSIFY:
  identity
  semantic
  type
  unit
  alias
  scope
  regime
  freshness
  provenance
  dependency
  transform
  authority
↓
INVALIDATE DESCENDANTS
↓
PRESERVE UNAFFECTED STATE
↓
REPAIR MINIMAL CAUSAL TARGET
↓
REVALIDATE VARIABLE
↓
RECOMPUTE AFFECTED DESCENDANTS
↓
RUN REGRESSION TESTS
↓
CONTROL-PLANE REVALIDATION
```

The source-aligned selective invalidation rule is:

[
Invalid(p)\Rightarrow invalidate(descendants(p))
]

Global recomputation should not be the default where dependency closure permits local repair.

---

# 38. Tests / Validators

Minimum variable test suite:

```text
VAR-TEST-001
Same symbol, different semantics.
Expected: collision detected.

VAR-TEST-002
Same semantic variable, incompatible units.
Expected: hard failure.

VAR-TEST-003
Derived feature without parent provenance.
Expected: quarantine/fail.

VAR-TEST-004
Alias across incompatible regimes.
Expected: alias rejected.

VAR-TEST-005
Cross-scale use without transform.
Expected: fail.

VAR-TEST-006
Unknown semantics.
Expected: composition blocked.

VAR-TEST-007
Attention weight increased.
Expected: truth status unchanged solely from attention.

VAR-TEST-008
Memory contradicts current observation.
Expected: both remain distinctly typed.

VAR-TEST-009
Duplicate evidence descendants.
Expected: independence count unchanged.

VAR-TEST-010
Load-bearing parent invalidated.
Expected: dependent descendants invalidated.

VAR-TEST-011
Independent branch exists.
Expected: unaffected branch preserved.

VAR-TEST-012
Scope changes.
Expected: compatibility/revalidation required.

VAR-TEST-013
Regime changes.
Expected: compatibility/revalidation required.

VAR-TEST-014
Stale variable used.
Expected: stale state exposed.

VAR-TEST-015
Undefined equation symbol.
Expected: UNBOUND_VARIABLE.

VAR-TEST-016
Unauthorized variable mutation.
Expected: proposal only / commit denied.

VAR-TEST-017
UNKNOWN/GAP supplied as default.
Expected: fail or explicit conditional handling.

VAR-TEST-018
Registry entry exists but implementation absent.
Expected: ADDRESSABLE/DEFINED, not IMPLEMENTED.
```

No execution evidence for these proposed L03 tests is established here.

---

# 39. Falsifiers

Revise this model if direct canonical evidence establishes:

```text
different canonical L03 symbols

different variable identities

different state decomposition

different semantic definitions

different variable types

different units

different equation bindings

different aliases

different H/M/L mappings

different provenance requirements

different uncertainty representation

different confidence rules

different authority semantics
```

A canonical runtime demonstrating incompatible variable behavior should invalidate only affected model mappings and their descendants.

---

# 40. Gap Matrix

```yaml
gap_status:

  universal_variable_object:
    status: SOURCE_ALIGNED

  registry_tensor:
    status: SOURCE_ALIGNED

  compatibility_rule:
    status: SOURCE_ALIGNED

  equation_binding:
    status: SOURCE_ALIGNED

  alias_semantic_identity_rule:
    status: SOURCE_ALIGNED

  derived_provenance_rule:
    status: SOURCE_ALIGNED

  cross_scale_transform_rule:
    status: SOURCE_ALIGNED

  unknown_semantics_block:
    status: SOURCE_ALIGNED

  confidence_ceiling:
    status: SOURCE_ALIGNED

  selective_invalidation:
    status: SOURCE_ALIGNED

  L03_variable_schema:
    status: MODEL_DEFINED

  L03_state_vector:
    status: MODEL_DEFINED

  observation_variables:
    status: MODEL_DEFINED

  attention_variables:
    status: MODEL_DEFINED

  feature_variables:
    status: MODEL_DEFINED

  relation_variables:
    status: MODEL_DEFINED

  binding_variables:
    status: MODEL_DEFINED

  percept_variables:
    status: MODEL_DEFINED

  competing_variables:
    status: MODEL_DEFINED

  memory_variables:
    status: MODEL_DEFINED

  HML_variables:
    status: MODEL_DEFINED

  uncertainty_variables:
    status: MODEL_DEFINED

  canonical_L03_variable_registry:
    status: CRITICAL_GAP

  canonical_symbols:
    status: CRITICAL_GAP

  canonical_types:
    status: CRITICAL_GAP

  canonical_equation_bindings:
    status: CRITICAL_GAP

  canonical_cross_scale_transforms:
    status: CRITICAL_GAP

  executable_variable_registry:
    status: CRITICAL_GAP

  runtime_validation:
    status: CRITICAL_GAP

  empirical_validation:
    status: CRITICAL_GAP
```

---

# 41. RSCF Completion State

```yaml
rscf:

  id: L03_PERCEPT_FORMATION_VARIABLES

  claim:
    L03_PERCEPT_FORMATION can be represented through a governed
    typed variable registry covering observations, attention,
    features, relations, bindings, candidate percepts, competing
    percepts, memory, H/M/L coordinates, provenance, dependencies,
    scope, regime, freshness, uncertainty, confidence, failure,
    repair, and authority state.

  claim_class: MODEL

  evidence:
    - AMOS Universal Variable Registry variable object
    - AMOS registry tensor
    - AMOS compatibility rule
    - AMOS equation-binding rule
    - AMOS alias rule
    - AMOS variable invariants
    - AMOS RSCF variable dependency model

  provenance:
    origin_architect: Trang Phan
    architecture_family: AMOS
    subsystem: COGNITIVE_MATRIX
    primitive: L03_PERCEPT_FORMATION
    artifact: VARIABLES.md
    derivation: SOURCE_ALIGNED_VARIABLE_GOVERNANCE_PLUS_L03_MODEL

  scope:
    system: AMOS_OS
    subsystem: COGNITIVE_MATRIX
    primitive: L03_PERCEPT_FORMATION
    concern: variable_contract

  regime:
    governed percept-formation architecture

  freshness:
    revalidate_when:
      - direct L03 variable canon recovered
      - L03 state schema changes
      - L03 equations change
      - HML mappings change
      - provenance architecture changes
      - authority architecture changes
      - canonical variable registry becomes available

  dependencies:
    - L01_SENSING_OBSERVATION
    - L02_ATTENTION
    - L03_DEFINITION
    - L03_STATE
    - L03_OPERATORS
    - L03_INVARIANTS
    - L03_DEPENDENCIES
    - L03_EQUATIONS
    - L03_HML
    - L03_MEMORY
    - L03_PROVENANCE
    - L03_TESTS
    - AMOS_UNIVERSAL_VARIABLE_REGISTRY
    - AMOS_RSCF
    - AMOS_CONTROL_PLANE

  competing:
    - flat untyped variable namespace
    - domain-local variable registries
    - universal typed registry
    - typed registry plus explicit L03 local namespace

  falsifiers:
    - incompatible direct L03 variable canon
    - incompatible canonical type system
    - incompatible canonical equation bindings
    - incompatible canonical HML mapping
    - reproducible canonical runtime counterexample

  uncertainty:
    generic_variable_governance: LOW_MEDIUM
    L03_variable_mapping: HIGH
    canonical_symbols: MAXIMUM
    canonical_types: MAXIMUM
    canonical_equations: MAXIMUM
    runtime_validation: MAXIMUM
    empirical_validation: MAXIMUM

  confidence_ceiling:
    Generic AMOS variable identity, compatibility, provenance,
    alias, equation-binding, cross-scale, confidence, and
    selective-invalidation principles are source-aligned.
    The specific L03 symbols, schemas, state vector, variable
    names, transforms, equation bindings, runtime behavior,
    and empirical interpretation remain MODEL or UNKNOWN/GAP.

  gap_status:
    canonical_variable_registry: CRITICAL_GAP
    canonical_symbols: CRITICAL_GAP
    canonical_types: CRITICAL_GAP
    canonical_equation_bindings: CRITICAL_GAP
    canonical_cross_scale_transforms: CRITICAL_GAP
    executable_registry: CRITICAL_GAP
    runtime_validation: CRITICAL_GAP
    empirical_validation: CRITICAL_GAP

  cheapest_discriminating_test:
    Recover direct canonical L03 variable/equation/state material
    and perform a symbol-by-symbol semantic diff against this
    registry before promoting any proposed L03 symbol or alias
    into canon.
```

---

# 42. Completion State

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

  canonical_variable_registry:
    status: UNKNOWN_GAP

  executable_registry:
    status: UNKNOWN_GAP

  runtime_validation:
    status: UNKNOWN_GAP

  empirical_validation:
    status: UNKNOWN_GAP

  overall:
    status: COMPLETE_FOR_VARIABLE_CONTRACT_SCOPE

  conclusion_class:
    MODEL
```

---

# 43. Hard Boundaries

```text
PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

UNKNOWN/GAP != PASS
```

Variable-specific boundaries:

```text
SYMBOL != VARIABLE

NAME != SEMANTICS

SAME SYMBOL != SAME VARIABLE

SAME LABEL != SAME MECHANISM

VARIABLE DEFINITION != OBSERVATION

VARIABLE VALUE != VERIFIED FACT

TYPE MATCH != SEMANTIC IDENTITY

UNIT MATCH != DOMAIN IDENTITY

ALIAS != IDENTITY UNLESS ESTABLISHED

ATTENTION != TRUTH

MEMORY != CURRENT OBSERVATION

FEATURE != OBJECT

RELATION != CAUSATION

BINDING != IDENTITY

PERCEPT CANDIDATE != OBSERVATION

DERIVED != SOURCE

CROSS-SCALE SIMILARITY != VALID TRANSFORM

REGISTRY ENTRY != IMPLEMENTATION

REGISTRY STATUS != EMPIRICAL VALIDATION

MUTABILITY != AUTHORITY

PROPOSED UPDATE != COMMITTED STATE
```

---

# 44. Governing Variable Contract

> **`L03_PERCEPT_FORMATION` SHALL represent material state through typed, semantically defined, scope-bound, regime-aware, provenance-preserving variables. Variable identity SHALL NOT be inferred from symbol or label equality; type or unit mismatch SHALL fail composition where applicable; unknown semantics SHALL block load-bearing composition; derived variables SHALL retain parent provenance; aliases SHALL NOT erase version, regime, scope, observer, or provenance differences; and cross-scale mappings SHALL require explicit transforms. Observation, attention, memory, feature, relation, binding, percept, uncertainty, and authority variables SHALL remain epistemically distinct. Attention SHALL NOT function as truth, memory SHALL NOT function as current observation, relation SHALL NOT function as causal proof, binding SHALL NOT function as identity proof, and registry presence SHALL NOT function as empirical validation. Invalid load-bearing variables SHALL selectively invalidate dependent descendants while preserving unaffected state. Variable transformations MAY generate proposals, but durable state mutation SHALL remain subject to control-plane authority and commit-time revalidation. `UNKNOWN/GAP` SHALL remain explicit and SHALL NOT be converted into a passing default.**

---

# 45. Canon Boundary

```text
SOURCE / ARCHITECTURE-ALIGNED:

Trang Phan origin/stewardship

Universal variable object:
  symbol
  canonical_name
  type
  unit
  domain
  scale
  time
  regime
  observer
  provenance
  status

registry tensor

equation binding

compatibility rule

alias requires semantic identity
and scope equivalence

same symbol != same variable

same label across domains
!= comparable units/mechanisms

type/unit mismatch = hard failure

derived variables retain provenance

aliases cannot erase
version/regime differences

cross-scale mapping requires
explicit transform

unknown semantics block composition

registry status != empirical validation

typed state / relation structure

invariant admission gate

governed transition structure

RSCF node/edge structure

confidence ceiling

selective invalidation


AMOS_MODEL:

L03 variable namespace

L03 symbols

L03 input/output schemas

L03 state vector

observation variable schema

attention variable schema

feature variable schema

relation variable schema

binding variable schema

percept variable schema

competing-percept variables

memory variable mapping

H/M/L variable mapping

uncertainty vector

freshness schema

scope/regime schema

L03 admission specialization

L03 equation-role bindings

L03 variable operators

L03 variable tests


UNKNOWN/GAP:

direct canonical L03 variable registry

canonical L03 symbols

canonical L03 types

canonical L03 units

canonical L03 aliases

canonical L03 equation bindings

canonical L03 cross-scale transforms

canonical thresholds

executable L03 variable registry

runtime validation

formal validation

empirical perceptual validation
```

Therefore:

```text
CONCLUSION CLASS:
MODEL

GENERIC AMOS VARIABLE GOVERNANCE:
SOURCE-ALIGNED

L03-SPECIFIC VARIABLE CONTRACT:
MODEL

DIRECT L03 VARIABLE CANON:
UNKNOWN/GAP

VARIABLE CONTRACT:
MODEL-COMPLETE FOR DECLARED SCOPE

EXECUTABLE VARIABLE REGISTRY:
NOT ESTABLISHED

RUNTIME VALIDATION:
NOT ESTABLISHED

FORMAL VERIFICATION:
NOT ESTABLISHED

EMPIRICAL PERCEPTUAL VALIDITY:
NOT ESTABLISHED
```

---

[[00_ROOT_MOC]]|[[AMOS MOC]]

---
**Related:** [[00_HOME]] · [[COGNITIVE_MATRIX_MOC]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: l03_percept_formation_primitives_cognitive_matrix_variables
node_type: note
path: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L03_PERCEPT_FORMATION/L03_PERCEPT_FORMATION_PRIMITIVES_COGNITIVE_MATRIX_VARIABLES.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[L03_PERCEPT_FORMATION_MOC]]
