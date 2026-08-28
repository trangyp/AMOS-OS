---
type: cognitive
source: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L03_PERCEPT_FORMATION
tags: [amos, cognitive-matrix, l03, percept-formation, readme, rscf, hml, provenance, governance, canon/cognitive-matrix]

title: "L03_PERCEPT_FORMATION"
origin_architect: "Trang Phan"
status: "MODEL_CONTRACT / UNIMPLEMENTED / UNVALIDATED"
epistemic_class: "MODEL"
runtime_alignment: "AMOS Full Brain OS / AMOS_CORE v4.4 lineage"
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


# L03_PERCEPT_FORMATION — README

**Class:** `COGNITIVE_PRIMITIVE_CONTRACT`  
**Origin architect / steward:** Trang Phan  
**Primitive:** `L03_PERCEPT_FORMATION`  
**Layer:** `COGNITIVE_MATRIX`  
**Status:** `AMOS_MODEL / UNIMPLEMENTED / UNVALIDATED`

---

# 0. Executive Definition

`L03_PERCEPT_FORMATION` is the AMOS cognitive primitive responsible for constructing structured percept candidates from admitted observations, attention-conditioned inputs, explicitly typed context, and admissible memory while preserving provenance, uncertainty, scope, regime, observer context, competing interpretations, and dependency lineage.

The primitive occupies the conceptual transition:

```text
L01_SENSING_OBSERVATION
        ↓
L02_ATTENTION
        ↓
L03_PERCEPT_FORMATION
        ↓
downstream cognition
```

This does **not** require a strictly linear runtime implementation.

Its fundamental responsibility is:

```text
OBSERVATION
+
ATTENTION
+
ADMISSIBLE CONTEXT
↓
FEATURES
+
RELATIONS
+
BINDINGS
↓
PERCEPT CANDIDATE(S)
+
PROVENANCE
+
UNCERTAINTY
+
COMPETING INTERPRETATIONS
```

L03 is not a truth oracle.

```text
OBSERVATION != PERCEPT

PERCEPT != REALITY

ATTENTION != TRUTH

BINDING != IDENTITY PROOF

COHERENCE != VALIDATION

CANDIDATE != COMMIT
```

---

# 1. Purpose

The purpose of L03 is to create a governed representation layer between raw/admitted observation and higher-order cognitive reasoning.

L03 should make it possible for downstream AMOS layers to answer:

```text
What appears to be present?

What features support that appearance?

Which observations contributed?

Which relations were inferred?

Which features were bound together?

Which modalities contributed?

Which memories or priors influenced interpretation?

What alternative percepts remain plausible?

What is uncertain?

What would falsify this percept?

What would need revalidation if an input changes?
```

The layer should preserve enough information that downstream cognition can distinguish:

```text
what was observed

what was selected by attention

what came from memory

what was derived

what was bound

what was inferred

what remains competing

what is unknown
```

---

# 2. Source / Canon References

## 2.1 Architecture-level alignment

This README is aligned with available AMOS architecture concerning:

```text
AMOS Full Brain OS
AMOS Cognition
AMOS_CORE v3.0 → v4.4 lineage
AMOS recursive RSCF / H-M-L
AMOS multimodal perception
AMOS attention allocation
AMOS information operators
AMOS distinction/relation/constraint architecture
AMOS binding architecture
AMOS provenance topology
AMOS memory governance
AMOS competing-hypothesis governance
AMOS confidence ceilings
AMOS selective invalidation
AMOS infrastructure/control-plane separation
```

The AMOS system-completion discipline also requires completeness to remain scoped and structural rather than being confused with proof of truth, implementation, or validation.

## 2.2 Direct L03 canon status

The exact canonical L03 artifacts have not been independently established here.

```yaml
direct_L03_README_canon: UNKNOWN_GAP
canonical_definition: UNKNOWN_GAP
canonical_variables: UNKNOWN_GAP
canonical_operators: UNKNOWN_GAP
canonical_equations: UNKNOWN_GAP
canonical_invariants: UNKNOWN_GAP
canonical_protocols: UNKNOWN_GAP
canonical_runtime: UNKNOWN_GAP
```

Therefore:

```text
ARCHITECTURE-ALIGNED MATERIAL
+
L03 SPECIALIZATION
=
AMOS_MODEL
```

unless explicitly upgraded by direct source evidence.

---

# 3. Definition and Scope

## 3.1 Definition

Candidate formal definition:

[
P_t^*
=====

\mathcal F_{L03}
(
O_t,
A_t,
C_t,
M_t,
R_t
)
]

where:

```text
O_t = admitted observations
A_t = attention-conditioned state
C_t = contextual constraints
M_t = admissible memory/prior context
R_t = regime / observer / scope state

P*_t = percept candidate set
```

`AMOS_MODEL`.

The star indicates:

```text
candidate percept
not committed external truth
```

## 3.2 In scope

L03 may govern:

```text
feature formation
feature distinction
feature relations
grouping
segmentation
binding
unbinding
temporal association
spatial association
cross-modal alignment
multimodal integration
contextualization
object candidate formation
event candidate formation
scene candidate formation
competing percept generation
provenance propagation
uncertainty propagation
H/M/L percept aggregation
validation preparation
percept-state proposals
```

## 3.3 Out of scope

L03 does not independently establish:

```text
raw sensor hardware truth
source authority
attention authority
memory authority
belief commitment
causal proof
planning authority
external-action authority
durable state commit
empirical cognition validity
```

---

# 4. Typed Inputs

```yaml
L03PerceptFormationInput:

  observations:
    type: ObservationState[]
    required: true

  attention_state:
    type: AttentionState
    required: true

  modality_state:
    type: ModalityAvailability
    required: true

  observer_context:
    type: ObserverContext
    required: true

  scope:
    type: ScopeEnvelope
    required: true

  regime:
    type: RegimeRef
    required: true

  freshness:
    type: FreshnessState
    required: true

  temporal_context:
    type: TemporalContext
    required: false

  spatial_context:
    type: SpatialContext
    required: false

  memory_context:
    type: MemoryContext[]
    required: false

  prior_percepts:
    type: PerceptState[]
    required: false

  constraints:
    type: ConstraintSet
    required: false

  provenance:
    type: ProvenanceBundle
    required: true

  uncertainty:
    type: UncertaintyVector
    required: true

  authority_context:
    type: AuthorityContext
    required: false
```

---

# 5. Typed Outputs

```yaml
L03PerceptFormationOutput:

  local_features:
    type: FeatureState[]

  relations:
    type: RelationState[]

  bindings:
    type: BindingCandidate[]

  percept_candidates:
    type: PerceptCandidate[]

  competing_percepts:
    type: CompetingPerceptSet[]

  HML_state:
    type: HMLPerceptState

  provenance:
    type: ProvenanceGraph

  dependency_graph:
    type: DependencyGraph

  uncertainty:
    type: UncertaintyVector

  confidence_ceiling:
    type: ConfidenceBound

  unresolved_gaps:
    type: PerceptGap[]

  validation_state:
    type:
      - CANDIDATE
      - CONDITIONAL
      - COMPETING
      - QUARANTINED
      - INVALID
      - UNKNOWN_GAP

  state_proposal:
    type: PerceptStateProposal | null

  commit_authority:
    type: NONE
```

---

# 6. State Variables

Candidate state registry:

```text
O_t       = active observations
A_t       = attention state

F_t       = features
R_t       = relations
B_t       = bindings
P_t       = percept candidates
CP_t      = competing percepts

Mod_t     = modality availability
Mem_t     = admissible memory context

H_t       = high-level percept state
M_t       = middle-level percept state
L_t       = local percept state

Prov_t    = provenance graph
Dep_t     = dependency graph

Scope_t   = scope
Reg_t     = regime
Fresh_t   = freshness
ObsCtx_t  = observer context

U_t       = uncertainty
Conf_t    = confidence ceiling

Q_t       = quarantine state
Gap_t     = unresolved gaps
Ver_t     = state/version identity
```

Candidate composite state:

[
S_t^{L03}
=========

(
O_t,A_t,F_t,R_t,B_t,P_t,CP_t,
H_t,M_t,L_t,
Prov_t,Dep_t,
Scope_t,Reg_t,Fresh_t,ObsCtx_t,
U_t,Conf_t,Q_t,Gap_t
)
]

---

# 7. Core Operators

The modeled L03 operator registry includes:

```text
ADMIT_OBSERVATION
NORMALIZE_OBSERVATION
SELECT_ATTENDED
DISTINGUISH_FEATURE
EXTRACT_FEATURE
RELATE_FEATURES
GROUP_FEATURES
BIND_FEATURES
UNBIND_FEATURES
PARTITION
TEMPORAL_ALIGN
SPATIAL_ALIGN
ALIGN_OBSERVER
ALIGN_MODALITIES
INTEGRATE_MODALITIES
CONTEXTUALIZE
COMBINE
SEPARATE
ORDER
THRESHOLD
GENERATE_PERCEPT_CANDIDATE
GENERATE_COMPETING_PERCEPTS
COMPARE_PERCEPTS
DISCRIMINATE
AGGREGATE_L_TO_M
AGGREGATE_M_TO_H
CONSTRAIN_H_TO_M
CONSTRAIN_M_TO_L
CHECK_PROVENANCE
CHECK_INDEPENDENCE
CHECK_SCOPE
CHECK_REGIME
CHECK_FRESHNESS
PROPAGATE_UNCERTAINTY
CALCULATE_CONFIDENCE_CEILING
PRESERVE_COMPETING
INVALIDATE_DEPENDENT
QUARANTINE
REPAIR
REVALIDATE
PROPOSE_STATE
```

Canonical identifiers remain `UNKNOWN/GAP`.

---

# 8. Core Equations

## 8.1 Percept formation

[
P_t^*
=====

\mathcal F_{L03}
(
O_t,
A_t,
C_t,
M_t,
R_t
)
]

`AMOS_MODEL`.

## 8.2 Local to middle aggregation

[
X_M
===

A_{L\rightarrow M}\(X_L\)
]

## 8.3 Middle to high aggregation

[
X_H
===

A_{M\rightarrow H}\(X_M\)
]

## 8.4 Downward constraint

[
X'_M
====

C_{H\rightarrow M}(X_H,X_M)
]

[
X'_L
====

C_{M\rightarrow L}(X'_M,X_L)
]

## 8.5 Confidence ceiling

For load-bearing premises:

[
Conf(P)
\le
\min_{d\in LB(P)}Conf(d)
]

unless independently revalidated.

## 8.6 Selective invalidation

[
Invalidate(p)
=============

Desc_{LB}(p)
]

Candidate equations should be treated as AMOS structural models unless independently source-established.

---

# 9. Core Invariants

```text
L03-INV-001
OBSERVATION != PERCEPT

L03-INV-002
PERCEPT != REALITY

L03-INV-003
ATTENTION != TRUTH

L03-INV-004
MEMORY != CURRENT OBSERVATION

L03-INV-005
FEATURE != INDEPENDENT OBSERVATION

L03-INV-006
GROUP != OBJECT IDENTITY

L03-INV-007
BINDING != IDENTITY PROOF

L03-INV-008
AGGREGATION != IDENTITY

L03-INV-009
AGGREGATION != CAUSATION

L03-INV-010
TEMPORAL ORDER != CAUSATION

L03-INV-011
DOWNWARD CONSTRAINT != DOWNWARD CAUSATION

L03-INV-012
MULTIMODAL != INDEPENDENT

L03-INV-013
UNAVAILABLE MODALITY != NEGATIVE EVIDENCE

L03-INV-014
DERIVED STATE MUST RETAIN PROVENANCE

L03-INV-015
SHARED ANCESTRY != INDEPENDENT CONFIRMATION

L03-INV-016
COMPETING PERCEPTS MUST REMAIN REPRESENTABLE

L03-INV-017
UNKNOWN/GAP != PASS

L03-INV-018
CONFIDENCE CANNOT EXCEED UNRESOLVED LOAD-BEARING PREMISES

L03-INV-019
SCOPE MUST PROPAGATE

L03-INV-020
REGIME MUST PROPAGATE

L03-INV-021
OBSERVER CONTEXT MUST PROPAGATE

L03-INV-022
FRESHNESS MUST PROPAGATE

L03-INV-023
H/M/L AGGREGATION MUST PRESERVE DECISION-RELEVANT HETEROGENEITY

L03-INV-024
FAILED PREMISES INVALIDATE ONLY DEPENDENT DESCENDANTS

L03-INV-025
REPAIR != REVALIDATION

L03-INV-026
CAPABILITY != AUTHORITY

L03-INV-027
PROPOSAL != COMMIT

L03-INV-028
STRUCTURAL VALIDITY != EMPIRICAL VALIDITY
```

---

# 10. Dependencies

## 10.1 Upstream

```text
L01_SENSING_OBSERVATION
L02_ATTENTION
```

## 10.2 Internal L03 artifact dependencies

```text
PURPOSE.md
DEFINITION.md
VARIABLES.md
STATE.md
OPERATORS.md
EQUATIONS.md
INVARIANTS.md
DEPENDENCIES.md
HML.md
MEMORY.md
PROVENANCE.md
PROTOCOLS.md
CONTROL_PLANES.md
AGENTS.md
SKILLS.md
WORKFLOWS.md
FAILURE_MODES.md
REPAIR.md
TESTS.md
RSCF.md
GAP_MATRIX.md
```

## 10.3 Cross-cutting AMOS dependencies

```text
AMOS RSCF
AMOS H/M/L
AMOS provenance topology
AMOS Information Operator Engine
AMOS Binding architecture
AMOS Multimodal Perception Layer
AMOS Temporal Multi-Scale architecture
AMOS Memory governance
AMOS Constraint Propagation
AMOS Infrastructure Control Plane
```

---

# 11. H/M/L Applicability

## L — Local

Represents:

```text
individual observations
features
local relations
local temporal/spatial structures
modality-local percept elements
```

Candidate transition:

[
O_L
\rightarrow
F_L
]

## M — Middle

Represents:

```text
feature groups
bindings
objects
events
multimodal candidates
bounded percept structures
```

Candidate transition:

[
{F_L,R_L,B_L}
\rightarrow
P_M^*
]

## H — High

Represents:

```text
scene-level percepts
global contextual organization
cross-subsystem percept structure
competing scene models
```

Candidate transition:

[
{P_M^*}
\rightarrow
P_H^*
]

Hard cross-scale boundary:

```text
L != M != H

LOCAL FAILURE != AUTOMATIC GLOBAL FAILURE

HIGH-LEVEL COHERENCE != LOW-LEVEL VALIDITY
```

---

# 12. Memory Interface

Memory may condition L03 percept formation but must remain epistemically typed.

```text
MEMORY
→ context / prior percept / working state

NOT

MEMORY
→ automatically current observation
```

Memory interaction should preserve:

```text
memory identity
formation origin
retrieval time
scope
regime
freshness
supersession lineage
contradictions
provenance
```

Hard rules:

```text
RETRIEVED != TRUE

PRIOR PERCEPT != CURRENT PERCEPT

SHARED MEMORY != INDEPENDENT CORROBORATION
```

---

# 13. Provenance Contract

Every material percept should retain recoverable ancestry to:

```text
source observations
semantic origins
attention context
memory context
features
relations
bindings
multimodal transforms
operators
agents
validation steps
H/M/L transformations
```

Candidate lineage:

```text
SOURCE
↓
OBSERVATION
↓
FEATURE
↓
RELATION / BINDING
↓
PERCEPT CANDIDATE
↓
H/M/L AGGREGATION
↓
STATE PROPOSAL
```

Hard boundary:

```text
NEW DERIVATION
!=
NEW SOURCE

NEW AGENT
!=
NEW SOURCE

NEW FILE
!=
NEW SOURCE

PARAPHRASE
!=
INDEPENDENT CONFIRMATION
```

---

# 14. Control-Plane Requirements

L03 workers may:

```text
form percept candidates
build relations
bind features
generate alternatives
check local invariants
calculate uncertainty
construct provenance
propose repairs
propose state
```

They should not independently own:

```text
durable state finality
authority creation
policy override
memory commit authority
cross-domain authority
external action
```

Control-plane checks should include where applicable:

```text
principal identity
capability envelope
state version
read set
dependency freshness
scope/regime
authority witness
constraint freshness
commit effect
rollback state
```

Hard rule:

```text
COGNITIVE VALIDITY
!=
COMMIT AUTHORITY
```

---

# 15. Agents

Candidate logical roles:

```text
L03_FEATURE_FORMATION_AGENT
L03_RELATION_AGENT
L03_BINDING_AGENT
L03_MULTIMODAL_ALIGNMENT_AGENT
L03_PERCEPT_SYNTHESIS_AGENT
L03_COMPETING_PERCEPT_AGENT
L03_HML_AGENT
L03_MEMORY_CONTEXT_AGENT
L03_PROVENANCE_AUDITOR
L03_UNCERTAINTY_AUDITOR
L03_VALIDATION_AGENT
L03_REPAIR_AGENT
```

These are architectural roles.

```text
ROLE DEFINED
!=
AGENT IMPLEMENTED

AGENT IMPLEMENTED
!=
AUTHORIZED
```

---

# 16. Skills

Potentially relevant AMOS skills include:

```text
AMOS Multimodal Perception Layer
AMOS Attention Allocation Governor
AMOS Binding RSCF Engine
AMOS Information Operator Engine
AMOS Distinction RSCF Architecture
AMOS Distinction-Relation-Constraint Algebra
AMOS Cross-Scale RSCF Tensor Engine
AMOS Temporal Multi-Scale RSCF Engine
AMOS Provenance Trust Firewall
AMOS Memory Conflict Governor
AMOS Memory Immune System
AMOS Metacognitive Confidence Auditor
AMOS Constraint Propagation RSCF Engine
AMOS Infrastructure Control Plane
AMOS System Completion Auditor
RSCF Modeler
```

Hard boundary:

```text
SKILL AVAILABLE
!=
SKILL INTEGRATED

SKILL INTEGRATED
!=
RUNTIME VALIDATED
```

---

# 17. Primary Workflow

```text
RECEIVE ADMITTED OBSERVATIONS
↓
RECEIVE ATTENTION CONTEXT
↓
CHECK:
  type
  provenance
  scope
  regime
  freshness
  observer
↓
NORMALIZE IF REQUIRED
↓
FORM FEATURES
↓
FORM RELATIONS
↓
GROUP / BIND
↓
ALIGN TIME / SPACE / MODALITIES
↓
INCORPORATE ADMISSIBLE MEMORY / CONTEXT
↓
GENERATE PERCEPT CANDIDATE(S)
↓
REGISTER COMPETING PERCEPTS
↓
BUILD H/M/L STATE
↓
TRACE PROVENANCE
↓
PROPAGATE UNCERTAINTY
↓
CALCULATE CONFIDENCE CEILING
↓
CHECK INVARIANTS
↓
VALID / CONDITIONAL / COMPETING / UNKNOWN_GAP
↓
PROPOSE STATE
↓
CONTROL-PLANE / DOWNSTREAM HANDOFF
```

---

# 18. Protocols

Candidate protocol surface:

```text
OBSERVATION_INGRESS
ATTENTION_CONTEXT_HANDOFF
OPERATOR_REQUEST
OPERATOR_RESULT
FEATURE_STATE_HANDOFF
BINDING_PROPOSAL
BINDING_RESULT
MULTIMODAL_ALIGNMENT_REQUEST
MULTIMODAL_ALIGNMENT_RESULT
PERCEPT_CANDIDATE_PROPOSAL
COMPETING_PERCEPT_REGISTER
DISCRIMINATION_REQUEST
DISCRIMINATION_RESULT
HML_UPWARD_HANDOFF
HML_DOWNWARD_CONSTRAINT
MEMORY_CONTEXT_REQUEST
MEMORY_CONTEXT_RESULT
PROVENANCE_CHECK_REQUEST
PROVENANCE_CHECK_RESULT
DEPENDENCY_REGISTER
VALIDATION_REQUEST
VALIDATION_RESULT
QUARANTINE_NOTICE
INVALIDATION_NOTICE
REPAIR_REQUEST
REPAIR_RESULT
REVALIDATION_REQUEST
REVALIDATION_RESULT
STATE_PROPOSAL
AUTHORITY_CHECK
COMMIT_REQUEST
COMMIT_RESULT
AUDIT_TRACE_APPEND
```

Canonical names and transport semantics remain `UNKNOWN/GAP`.

---

# 19. RSCF Contract

Every material L03 conclusion should be representable as:

```yaml
RSCFNode:

  id: null

  claim_class:
    - OBSERVATION
    - DERIVED
    - MODEL
    - CONDITIONAL
    - COMPETING
    - UNKNOWN_GAP

  claim: null

  HML:
    - H
    - M
    - L

  evidence: []

  provenance: []

  scope: null
  regime: null
  freshness: null
  observer: null

  dependencies: []

  competing: []

  falsifiers: []

  uncertainty: null
  confidence_ceiling: null
```

Core rule:

```text
CONCLUSION CLASS
MUST NOT EXCEED
LOAD-BEARING EVIDENCE
```

---

# 20. Uncertainty and Confidence Ceiling

L03 uncertainty should remain multidimensional.

```yaml
uncertainty_vector:

  observation: null
  feature: null
  binding: null
  identity: null
  modality: null
  temporal: null
  spatial: null
  memory: null
  provenance: null
  independence: null
  scope: null
  regime: null
  observer: null
  model: null
  execution: null
```

Candidate confidence constraint:

[
Conf(P)
\le
\min_{d\in LB(P)}Conf(d)
]

unless an independent validated path justifies improvement.

Important:

```text
LOW UNCERTAINTY IN ONE DIMENSION
!=
LOW UNCERTAINTY OVERALL
```

---

# 21. Failure Modes

Representative L03 failures include:

```text
FM-L03-001
invalid observation admitted

FM-L03-002
attention selection corrupts percept formation

FM-L03-003
feature transformation failure

FM-L03-004
binding failure

FM-L03-005
unsupported percept / hallucinated structure

FM-L03-006
material percept omission

FM-L03-007
provenance loss

FM-L03-008
shared ancestry counted as independent evidence

FM-L03-009
confidence inflation

FM-L03-010
uncertainty collapse

FM-L03-011
scope leakage

FM-L03-012
regime drift

FM-L03-013
freshness failure

FM-L03-014
missing modality treated as negative evidence

FM-L03-015
temporal binding failure

FM-L03-016
spatial binding failure

FM-L03-017
context overwrite

FM-L03-018
observation / inference collapse

FM-L03-019
forced percept convergence

FM-L03-020
contradiction suppression

FM-L03-021
H/M/L promotion error

FM-L03-022
H/M/L downward overwrite

FM-L03-023
dependency lineage loss

FM-L03-024
over-invalidation

FM-L03-025
under-invalidation

FM-L03-026
repair contamination

FM-L03-027
repair loop

FM-L03-028
premature recovery

FM-L03-029
UNKNOWN/GAP interpreted as PASS

FM-L03-030
capability / authority collapse

FM-L03-031
proposal / commit collapse
```

---

# 22. Repair / Recovery

Candidate recovery workflow:

```text
DETECT FAILURE
↓
CLASSIFY FAILURE
↓
IDENTIFY AFFECTED H/M/L LEVEL
↓
TRACE LOAD-BEARING DEPENDENCIES
↓
IDENTIFY EARLIEST SUPPORTED FAILURE
↓
QUARANTINE AFFECTED STATE
↓
PRESERVE UNAFFECTED BRANCHES
↓
ROLL BACK TO NEAREST VALID STATE
↓
REPAIR:
  feature
  relation
  binding
  provenance
  memory input
  operator
  scope
  regime
  H/M/L mapping
↓
REBUILD PERCEPT CANDIDATES
↓
RESTORE COMPETING HYPOTHESES
↓
RECALCULATE UNCERTAINTY
↓
RECALCULATE CONFIDENCE
↓
REVALIDATE
↓
RECOVER / CONDITIONAL / COMPETING / GAP
```

Hard boundaries:

```text
REPAIR != REVALIDATION

REPAIR MUST NOT INVENT SOURCE EVIDENCE

LOCAL FAILURE != GLOBAL RESET
```

---

# 23. Tests / Validators

Minimum validator families:

```text
VALIDATE_INPUT_TYPES
VALIDATE_OBSERVATION_PERCEPT_BOUNDARY
VALIDATE_ATTENTION_TRUTH_BOUNDARY
VALIDATE_MEMORY_OBSERVATION_BOUNDARY
VALIDATE_FEATURE_LINEAGE
VALIDATE_BINDING
VALIDATE_TEMPORAL_ALIGNMENT
VALIDATE_SPATIAL_ALIGNMENT
VALIDATE_MODALITY_AVAILABILITY
VALIDATE_MULTIMODAL_ANCESTRY
VALIDATE_PROVENANCE
VALIDATE_INDEPENDENCE
VALIDATE_SCOPE
VALIDATE_REGIME
VALIDATE_FRESHNESS
VALIDATE_HML
VALIDATE_HETEROGENEITY_PRESERVATION
VALIDATE_COMPETING_PERCEPTS
VALIDATE_UNCERTAINTY
VALIDATE_CONFIDENCE_CEILING
VALIDATE_DEPENDENCY_GRAPH
VALIDATE_SELECTIVE_INVALIDATION
VALIDATE_REPAIR_REVALIDATION
VALIDATE_AUTHORITY_BOUNDARY
VALIDATE_PROPOSAL_COMMIT_BOUNDARY
VALIDATE_UNKNOWN_NOT_PASS
```

Minimum conceptual tests:

```text
TEST-L03-001
Ambiguous input.
Expected:
COMPETING percepts allowed.

TEST-L03-002
Increase attention without new evidence.
Expected:
truth/confidence does not automatically rise.

TEST-L03-003
Three derived features from one observation.
Expected:
one underlying ancestry family.

TEST-L03-004
Strong binding from weak premises.
Expected:
confidence remains bounded.

TEST-L03-005
Missing modality.
Expected:
UNKNOWN/UNAVAILABLE, not negative evidence.

TEST-L03-006
Stale memory conflicts with fresh observation.
Expected:
conflict preserved.

TEST-L03-007
Invalidate one load-bearing local feature.
Expected:
dependent descendants revalidated selectively.

TEST-L03-008
H-level context contradicts local observation.
Expected:
local observation preserved.

TEST-L03-009
Produce valid percept without authority.
Expected:
proposal only.

TEST-L03-010
Critical provenance unknown.
Expected:
UNKNOWN/GAP, not PASS.
```

Current status:

```yaml
tests_defined: true
tests_executed: false
formal_verification: false
runtime_validation: false
empirical_validation: false
```

---

# 24. Falsifiers

This README must be revised if stronger canonical or executable evidence establishes:

```text
a materially different purpose for L03

different placement in the cognitive primitive chain

different upstream/downstream dependencies

different state ownership

different observation/percept boundary

different attention semantics

different memory semantics

different H/M/L semantics

different provenance requirements

different operator registry

different authority/commit boundary

or executable canonical behavior contradicting this model
```

No L03-specific claim should be promoted merely because it is internally coherent with the rest of this README.

---

# 25. Gap Status

```yaml
gap_status:

  architectural_role:
    status: MODEL_DEFINED

  source_canon_references:
    status: PARTIAL

  definition:
    status: MODEL_DEFINED

  scope:
    status: MODEL_DEFINED

  typed_inputs:
    status: MODEL_DEFINED

  typed_outputs:
    status: MODEL_DEFINED

  state_variables:
    status: MODEL_DEFINED

  operators:
    status: MODEL_DEFINED

  equations:
    status: MODEL_DEFINED

  invariants:
    status: MODEL_DEFINED

  dependencies:
    status: MODEL_DEFINED

  HML:
    status: MODEL_DEFINED

  memory:
    status: MODEL_DEFINED

  provenance:
    status: MODEL_DEFINED

  protocols:
    status: MODEL_DEFINED

  control_plane:
    status: MODEL_DEFINED

  agents:
    status: MODEL_ROLES

  skills:
    status: ADDRESSABLE

  workflows:
    status: MODEL_DEFINED

  failure_modes:
    status: MODEL_DEFINED

  repair:
    status: MODEL_DEFINED

  tests:
    status: MODEL_DEFINED_UNEXECUTED

  RSCF:
    status: MODEL_DEFINED

  direct_canonical_README:
    status: CRITICAL_GAP

  canonical_variable_registry:
    status: CRITICAL_GAP

  canonical_operator_registry:
    status: CRITICAL_GAP

  canonical_equation_registry:
    status: CRITICAL_GAP

  canonical_runtime:
    status: CRITICAL_GAP

  executable_implementation:
    status: CRITICAL_GAP

  executed_validation:
    status: CRITICAL_GAP

  empirical_validation:
    status: CRITICAL_GAP
```

---

# 26. Required Artifact Map

Expected L03 artifact set:

```text
L03_PERCEPT_FORMATION/
│
├── README.md
├── PURPOSE.md
├── DEFINITION.md
├── VARIABLES.md
├── STATE.md
├── OPERATORS.md
├── EQUATIONS.md
├── INVARIANTS.md
├── DEPENDENCIES.md
├── HML.md
├── MEMORY.md
├── PROVENANCE.md
├── PROTOCOLS.md
├── CONTROL_PLANES.md
├── AGENTS.md
├── SKILLS.md
├── WORKFLOWS.md
├── FAILURE_MODES.md
├── REPAIR.md
├── TESTS.md
├── RSCF.md
└── GAP_MATRIX.md
```

Structural completion of these documents means:

```text
DOCUMENT CONTRACT COVERAGE
```

not:

```text
CANON COMPLETE
IMPLEMENTED
VALIDATED
```

The AMOS system-completion discipline requires these states to remain separate.

---

# 27. Completion Criteria

`L03_PERCEPT_FORMATION` may be called `COMPLETE_FOR_DOCUMENTED_MODEL_SCOPE` only when:

```text
all required artifacts exist

all required completion fields are addressed

dependencies are explicitly mapped

hard boundaries are preserved

contradictions are visible

gaps are explicitly classified

failure and repair paths exist

tests are specified

provenance is recoverable

uncertainty/confidence ceilings are explicit
```

This still does not imply implementation.

For runtime completeness, additionally require:

```text
executable state model

implemented operators

implemented protocols

implemented validators

runtime provenance

runtime authority integration

fault injection

integration tests

replay tests

repair/recovery tests
```

For validation:

```text
executed tests
raw results
environment identity
versions
failure traces
scope-limited conclusions
```

For empirical claims:

```text
independent external evidence
appropriate measurement design
scope/regime validity
causal discipline where relevant
```

---

# 28. RSCF Completion State

```yaml
rscf:

  id: L03_PERCEPT_FORMATION_README

  claim:
    L03_PERCEPT_FORMATION can be modeled as a governed cognitive
    primitive that forms structured, provenance-bearing,
    uncertainty-aware percept candidates from admitted observations,
    attention-conditioned context, and admissible memory while
    preserving competing interpretations, H/M/L structure,
    dependency lineage, scope/regime boundaries, confidence ceilings,
    and proposal/commit separation.

  claim_class: MODEL

  evidence:
    - AMOS cognition architecture
    - AMOS RSCF/HML architecture
    - AMOS provenance architecture
    - AMOS information-operator architecture
    - AMOS multimodal perception architecture
    - AMOS control-plane architecture
    - reconstructed L03 artifact contracts

  provenance:
    origin_architect: Trang Phan
    architecture_family: AMOS
    subsystem: COGNITIVE_MATRIX
    primitive: L03_PERCEPT_FORMATION
    artifact: README.md
    derivation: SOURCE_ARCHITECTURE_PLUS_L03_MODEL_SYNTHESIS

  scope:
    system: AMOS_OS
    subsystem: COGNITIVE_MATRIX
    primitive: L03_PERCEPT_FORMATION
    concern: top_level_contract_and_navigation

  regime:
    governed cognitive/perceptual architecture

  freshness:
    revalidate_when:
      - direct L03 canon is recovered
      - upstream L01/L02 contracts change
      - L03 artifact contracts change
      - HML architecture changes
      - provenance architecture changes
      - control-plane architecture changes
      - executable runtime appears
      - validation evidence appears

  dependencies:
    - L01_SENSING_OBSERVATION
    - L02_ATTENTION
    - L03_PURPOSE
    - L03_DEFINITION
    - L03_VARIABLES
    - L03_STATE
    - L03_OPERATORS
    - L03_EQUATIONS
    - L03_INVARIANTS
    - L03_DEPENDENCIES
    - L03_HML
    - L03_MEMORY
    - L03_PROVENANCE
    - L03_PROTOCOLS
    - L03_CONTROL_PLANES
    - L03_AGENTS
    - L03_SKILLS
    - L03_WORKFLOWS
    - L03_FAILURE_MODES
    - L03_REPAIR
    - L03_TESTS
    - L03_RSCF
    - L03_GAP_MATRIX

  competing:
    - feed-forward percept pipeline
    - recurrent/context-conditioned percept architecture
    - flat percept dependency graph
    - governed typed provenance-bearing percept architecture

  falsifiers:
    - incompatible direct L03 canon
    - incompatible primitive ordering
    - incompatible state ownership
    - incompatible HML semantics
    - incompatible memory semantics
    - incompatible provenance rules
    - incompatible authority semantics
    - executable counterexample

  uncertainty:
    architecture_role: MEDIUM
    source: MEDIUM_HIGH
    direct_canon: MAXIMUM
    model: MEDIUM
    canonical_types: HIGH
    canonical_operators: MAXIMUM
    execution: MAXIMUM
    empirical: MAXIMUM
    provenance_independence: MEDIUM_HIGH

  confidence_ceiling:
    The available AMOS architecture is sufficient to define a
    structurally governed L03 MODEL and its unresolved gaps.
    It is not sufficient to establish that this README reproduces
    exact canonical L03 semantics, or that L03 is implemented,
    runtime-validated, formally verified, or empirically validated.

  gap_status:
    direct_canon: CRITICAL_GAP
    canonical_types: CRITICAL_GAP
    canonical_operators: CRITICAL_GAP
    canonical_equations: CRITICAL_GAP
    runtime: CRITICAL_GAP
    executed_validation: CRITICAL_GAP
    empirical_validation: CRITICAL_GAP

  cheapest_discriminating_test:
    recover direct canonical L03 material and perform a
    provenance-preserving field-by-field delta against the complete
    reconstructed artifact set, then implement a minimal
    observation→attention→feature→binding→competing-percept runtime
    and execute invariant, provenance, H/M/L, selective-invalidation,
    repair, stale-state, and authority-boundary tests.
```

---

# 29. Completion State

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

  equations:
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

  memory:
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

  gap_matrix:
    status: MODEL_COMPLETE

  direct_canon:
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
    status: COMPLETE_FOR_DOCUMENTED_MODEL_SCOPE

  conclusion_class:
    MODEL
```

---

# 30. Hard Boundaries

```text
PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

UNKNOWN/GAP != PASS
```

L03-specific hard boundaries:

```text
OBSERVATION != PERCEPT

PERCEPT != REALITY

ATTENTION != TRUTH

MEMORY != CURRENT OBSERVATION

FEATURE != INDEPENDENT EVIDENCE

GROUP != OBJECT

BINDING != IDENTITY PROOF

ASSOCIATION != CAUSATION

TEMPORAL ORDER != CAUSATION

AGGREGATION != IDENTITY

AGGREGATION != GLOBAL TRUTH

DOWNWARD CONSTRAINT != DOWNWARD CAUSATION

MULTIMODAL != INDEPENDENT

UNAVAILABLE MODALITY != NEGATIVE EVIDENCE

REPETITION != INDEPENDENT CONFIRMATION

SHARED ANCESTRY != INDEPENDENT CONFIRMATION

HIGH-LEVEL COHERENCE != LOW-LEVEL VALIDITY

LOCAL FAILURE != AUTOMATIC GLOBAL FAILURE

REPAIR != REVALIDATION

VALIDATION != AUTHORIZATION

PROTOCOL COMPLETE != STATE COMMITTED

MODEL COMPLETE != CANON COMPLETE

CANON COMPLETE != IMPLEMENTED

IMPLEMENTED != VALIDATED

VALIDATED != UNIVERSALLY VALID

STRUCTURAL COGNITIVE MODEL != EMPIRICAL HUMAN COGNITION
```

---

# 31. Governing L03 Contract

> **`L03_PERCEPT_FORMATION` SHALL transform admitted observation state and attention-conditioned context into typed percept candidates while preserving observation/interpretation distinction, source ancestry, semantic origin, scope, regime, observer context, freshness, uncertainty, confidence ceilings, H/M/L identity, and load-bearing dependency structure. L03 MAY use explicitly typed memory and contextual state, but SHALL NOT silently reclassify memory or prior interpretation as current observation. Feature formation, binding, multimodal integration, aggregation, agent handoff, duplication, paraphrase, or replay SHALL NOT manufacture evidential independence. Perceptual association or temporal ordering SHALL NOT be promoted into causation without separately typed causal evidence. Ambiguous evidence SHALL permit `COMPETING` percepts, and unresolved load-bearing gaps SHALL remain `UNKNOWN/GAP`. Failed premises SHALL selectively invalidate dependent descendants while preserving unaffected branches. Repair SHALL rebuild from the nearest valid state and SHALL require revalidation. L03 workers MAY propose percept state, but capability SHALL NOT imply authority and a valid proposal SHALL NOT become a durable commit without the governing control plane.**

---

# 32. Canon Boundary

```text
SOURCE / ARCHITECTURE-ALIGNED:

Trang Phan origin/stewardship

AMOS cognitive architecture

RSCF / H-M-L reasoning

typed state and dependency discipline

provenance preservation

competing-hypothesis preservation

confidence ceilings

scope/regime/freshness discipline

selective invalidation

repair/revalidation distinction

capability/authority separation

proposal/commit separation

structural completeness != truth/validation


AMOS_MODEL:

exact L03 functional role

typed input/output schemas

state registry

operator registry

equations

L03-specific invariants

H/M/L specialization

memory interface

provenance specialization

protocol registry

agent roles

workflow definitions

failure taxonomy

repair workflow

validator suite


UNKNOWN/GAP:

direct canonical L03 README

canonical definitions

canonical variables

canonical state schema

canonical operators

canonical equations

canonical H/M/L mappings

canonical protocols

canonical runtime

executable implementation

executed tests

formal verification

empirical perceptual validation
```

Therefore:

```text
CONCLUSION CLASS:
MODEL

README STATUS:
COMPLETE_FOR_DOCUMENTED_MODEL_SCOPE

DIRECT L03 CANON:
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

```text
```

---

00_ROOT_MOC|AMOS MOC

---
**Related:** [[00_HOME]] · [[COGNITIVE_MATRIX_MOC]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: l03_percept_formation_primitives_cognitive_matrix_readme
node_type: note
path: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L03_PERCEPT_FORMATION/L03_PERCEPT_FORMATION_PRIMITIVES_COGNITIVE_MATRIX_README.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[L03_PERCEPT_FORMATION_MOC]]
