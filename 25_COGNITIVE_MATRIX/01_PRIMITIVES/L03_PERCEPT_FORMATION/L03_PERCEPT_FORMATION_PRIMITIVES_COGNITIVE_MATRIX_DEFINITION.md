---
tags:
  - amos
  - cognitive-matrix
  - l03
  - percept-formation
  - definition
  - perception
  - provenance
  - rscf
  - hml

title: "L03_PERCEPT_FORMATION — Definition"
origin_architect: "Trang Phan"
status: "MODEL_DEFINITION_CONTRACT / UNIMPLEMENTED / UNVALIDATED"
epistemic_class: "MODEL"
runtime_alignment: "AMOS Full Brain OS / AMOS_CORE v4.4 lineage"
---

# L03_PERCEPT_FORMATION — Definition

**Class:** `COGNITIVE_PRIMITIVE_DEFINITION_CONTRACT`  
**Origin architect / steward:** Trang Phan  
**Primitive:** `L03_PERCEPT_FORMATION`  
**Artifact:** `DEFINITION.md`  
**Status:** `AMOS_MODEL / UNIMPLEMENTED / UNVALIDATED`

> **Canon boundary:** This document defines a source-bounded AMOS model for `L03_PERCEPT_FORMATION`. AMOS perception architecture explicitly requires H/M/L, typed invariants/tensors, RSCF, equation provenance, falsifiers, repair, provenance, competing hypotheses, and confidence ceilings; source-defined structures must not be confused with external empirical validation.  Exact canonical L03 definitions, schemas, equations, thresholds, and executable implementation remain `UNKNOWN/GAP` unless recovered from direct canon.

---

## 0. Purpose

Define the semantic and architectural meaning of:

```text
L03_PERCEPT_FORMATION
```

within the AMOS cognitive primitive chain.

L03 is modeled as the transformation boundary at which admitted observations, conditioned by attention and context, are organized into bounded **percept candidates** that can support later cognition.

Canonical separation:

```text
ENVIRONMENT / SOURCE
↓
L01_SENSING_OBSERVATION
↓
L02_ATTENTION
↓
L03_PERCEPT_FORMATION
↓
downstream cognition
```

The primitive must preserve the distinction:

```text
REALITY
!=
OBSERVATION
!=
ATTENDED OBSERVATION
!=
PERCEPT
!=
INTERPRETATION
!=
BELIEF
!=
FACT
```

---

# 1. Source / Canon References

## 1.1 Source-aligned AMOS architecture

Relevant source families include:

```text
AMOS Full Brain OS
AMOS Cognition architecture
AMOS Multimodal Perception Layer
AMOS Sensory Map architecture
AMOS Binding architecture
AMOS H/M/L
AMOS RSCF
AMOS provenance architecture
AMOS uncertainty/confidence governance
AMOS Infrastructure Control Plane
AMOS_CORE v3.0 → v4.4 lineage
```

The AMOS Multimodal Perception Layer explicitly establishes the governing methodological requirements:

```text
H/M/L
typed invariants
tensor representation
RSCF
equation registry
falsifiers
repair
competing hypotheses
confidence ceiling
provenance
```

and explicitly preserves:

```text
SOURCE_DEFINED
!=
EXTERNALLY_EMPIRICALLY_VALIDATED
```

## 1.2 Direct L03 canon status

```yaml
canonical_L03_definition: UNKNOWN_GAP
canonical_L03_input_schema: UNKNOWN_GAP
canonical_L03_output_schema: UNKNOWN_GAP
canonical_L03_state_schema: UNKNOWN_GAP
canonical_L03_equations: UNKNOWN_GAP
canonical_L03_thresholds: UNKNOWN_GAP
canonical_L03_runtime: UNKNOWN_GAP
```

Therefore all detailed formalization below is classified `MODEL` unless otherwise marked.

---

# 2. Definition

## 2.1 Working definition

`L03_PERCEPT_FORMATION` is the AMOS cognitive primitive responsible for constructing bounded perceptual representations from admissible observations selected or weighted through attention, while preserving source lineage, observer context, modality state, temporal/spatial context, uncertainty, competing interpretations, and scope.

Compactly:

[
P_t =
\mathcal{F}_{L03}
(O_t^A, A_t, C_t, M_t, \Pi_t)
]

where:

```text
P_t   = percept candidate state
O_t^A = attended/admitted observations
A_t   = attention context
C_t   = contextual state
M_t   = modality availability/state
Π_t   = provenance and observer metadata
```

This equation is `AMOS_MODEL`, not an established scientific law.

---

# 3. Scope

L03 may include:

```text
feature grouping
observation binding
temporal binding
spatial binding
cross-modal association
object/event candidate construction
figure/background organization
percept candidate generation
ambiguity preservation
percept competition
confidence assignment
uncertainty propagation
provenance preservation
```

L03 does **not**, by definition alone, establish:

```text
objective truth
causal explanation
semantic belief
memory truth
decision authority
action authority
conscious awareness
human neurological equivalence
```

Hard boundary:

```text
PERCEPTUAL COHERENCE
!=
REALITY CORRESPONDENCE
```

---

# 4. Typed Inputs

```yaml
L03PerceptFormationInput:

  observations:
    type: ObservationRef[]
    source: L01_SENSING_OBSERVATION

  attention_state:
    type: AttentionState
    source: L02_ATTENTION

  modality_state:
    type: ModalityAvailability

  observer_context:
    type: ObserverContext

  temporal_context:
    type: TemporalContext

  spatial_context:
    type: SpatialContext | null

  prior_context:
    type: ContextRef[]
    admissibility: governed

  constraints:
    type: ConstraintSet

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeRef

  provenance:
    type: ProvenanceBundle

  hml_context:
    type: HMLContext
```

---

# 5. Typed Outputs

```yaml
L03PerceptFormationOutput:

  percept_candidates:
    type: PerceptCandidate[]

  accepted_percepts:
    type: PerceptRef[]

  competing_percepts:
    type: CompetingPercept[]

  unresolved_bindings:
    type: BindingGap[]

  percept_features:
    type: PerceptFeature[]

  uncertainty:
    type: PerceptUncertainty

  confidence_ceiling:
    type: ConfidenceBound

  provenance:
    type: ProvenanceBundle

  dependency_graph:
    type: DependencyGraph

  downstream_status:
    type:
      - PROPOSED
      - CONDITIONAL
      - COMPETING
      - UNKNOWN_GAP
```

No output status implies authoritative commit.

---

# 6. State Variables

```text
O_t       = available observations
A_t       = attention state
F_t       = extracted percept features
B_t       = candidate bindings
P_t       = percept candidates
C_t       = contextual state
M_t       = modality availability
X_t       = spatial context
T_t       = temporal context
ObsCtx_t  = observer context
Comp_t    = competing percepts
U_t       = uncertainty vector
Conf_t    = confidence ceiling
Prov_t    = provenance graph
Dep_t     = dependency graph
Scope_t   = applicability envelope
Reg_t     = operating regime
Gap_t     = unresolved gaps
```

Candidate percept state:

[
P_t =
\langle
F_t,
B_t,
C_t,
M_t,
T_t,
X_t,
ObsCtx_t,
U_t,
Prov_t
\rangle
]

`MODEL`.

---

# 7. Operators

Candidate L03 operators:

```text
NORMALIZE_OBSERVATION()
EXTRACT_FEATURE()
GROUP_FEATURES()
BIND()
TEMPORAL_BIND()
SPATIAL_BIND()
CROSS_MODAL_BIND()
GENERATE_PERCEPT()
GENERATE_COMPETING_PERCEPT()
SCORE_SUPPORT()
PROPAGATE_UNCERTAINTY()
CHECK_CONTEXT()
CHECK_SCOPE()
CHECK_REGIME()
PRESERVE_PROVENANCE()
DETECT_CONFLICT()
MARK_UNKNOWN()
INVALIDATE_DEPENDENT_PERCEPT()
REPAIR_BINDING()
PROPOSE_PERCEPT_STATE()
```

Operators generate or transform percept state.

They do not intrinsically grant commit authority.

---

# 8. Invariants

```text
L03-INV-001
Every percept must have traceable observation ancestry.

L03-INV-002
A percept cannot create an observation that was never admitted.

L03-INV-003
Observation content and percept interpretation remain distinguishable.

L03-INV-004
Attention weighting cannot convert absent evidence into observed evidence.

L03-INV-005
Unavailable modality cannot automatically be interpreted as negative evidence.

L03-INV-006
Material ambiguity must remain representable.

L03-INV-007
Material competing percepts must not be silently collapsed.

L03-INV-008
Multiple descendants of one observation do not constitute independent evidence.

L03-INV-009
Observer context must be preserved when percept formation depends upon it.

L03-INV-010
Temporal order must not be silently rewritten by percept binding.

L03-INV-011
Spatial relations must not be fabricated when spatial information is unavailable.

L03-INV-012
Scope cannot expand merely through percept formation.

L03-INV-013
Regime validity cannot expand merely through percept formation.

L03-INV-014
Percept confidence cannot exceed its load-bearing evidence ceiling.

L03-INV-015
UNKNOWN/GAP cannot become PASS through perceptual coherence.

L03-INV-016
Percept generation does not confer authority.

L03-INV-017
Proposal does not equal commit.

L03-INV-018
Hard invariant failure is non-compensatory.
```

The non-compensatory treatment of hard invariants is explicitly part of the AMOS perception-layer contract.

---

# 9. Dependencies

Primary dependency chain:

```text
L01_SENSING_OBSERVATION
↓
L02_ATTENTION
↓
L03_PERCEPT_FORMATION
```

Supporting dependencies:

```yaml
dependencies:

  upstream:
    - L01_SENSING_OBSERVATION
    - L02_ATTENTION

  structural:
    - AMOS_MULTIMODAL_PERCEPTION_LAYER
    - AMOS_BINDING_ARCHITECTURE
    - AMOS_TEMPORAL_MULTISCALE
    - AMOS_PROVENANCE
    - AMOS_RSCF

  governance:
    - AMOS_INFRASTRUCTURE_CONTROL_PLANE
    - AMOS_CONSTRAINT_PROPAGATION
    - AMOS_CONFIDENCE_GOVERNANCE

  downstream:
    - later cognitive primitives
    - memory candidates
    - interpretation/reasoning systems
    - decision systems
```

Exact downstream L04+ canonical dependency topology remains `UNKNOWN/GAP` unless separately established.

---

# 10. H/M/L Applicability

## H — Global percept frame

Represents:

```text
overall scene
environmental configuration
global perceptual situation
high-level multimodal coherence
major perceptual regime
```

Example model:

```text
"an active meeting is occurring"
```

rather than isolated local features.

## M — Object / event / subsystem percept

Represents:

```text
object candidates
event candidates
speaker candidates
motion patterns
cross-modal entities
bounded scene regions
```

## L — Feature / local observation binding

Represents:

```text
edge
tone
token
movement
timestamp
location cue
single feature
local source binding
```

Cross-scale invariant:

```text
L support
does not automatically validate
M percept

M support
does not automatically validate
H scene
```

Dependency closure must be established.

---

# 11. Control-Plane Requirements

L03 cognition and L03 governance must remain separate.

```text
PERCEPT WORKER
→ generates percept candidate

CONTROL PLANE
→ validates admissibility

AUTHORITY
→ determines whether state mutation is allowed

COMMIT
→ makes authorized state durable
```

Required governance includes:

```text
typed input validation
observation ancestry
attention dependency validation
scope/regime checking
freshness checking
observer-context preservation
modality availability checking
provenance validation
conflict preservation
confidence ceilings
selective invalidation
authority separation
commit-time revalidation where consequential
```

The generic AMOS control-plane architecture separates typed evidence production from authoritative commit and requires evidence, read-set, transaction, constraint, observability, and authority validation before consequential effects. 

---

# 12. Agents

Candidate functional agents:

```text
L03_PERCEPT_COORDINATOR
L03_FEATURE_AGENT
L03_BINDING_AGENT
L03_TEMPORAL_BINDING_AGENT
L03_SPATIAL_BINDING_AGENT
L03_MULTIMODAL_INTEGRATOR
L03_CONTEXT_AGENT
L03_PERCEPT_GENERATOR
L03_COMPETING_PERCEPT_AGENT
L03_UNCERTAINTY_AGENT
L03_PROVENANCE_AGENT
L03_AUDITOR
L03_REPAIR_AGENT
```

These names are `MODEL`.

Default capability envelope:

```yaml
agent_authority:
  observe_inputs: bounded
  transform: yes
  generate_candidates: yes
  propose: yes
  preserve_competing: yes
  commit_authoritative_state: no
```

---

# 13. Skills

Relevant capability families:

```text
AMOS Multimodal Perception Layer
AMOS Sensory Map Integrator
AMOS Binding RSCF Engine
AMOS Temporal Multi-Scale RSCF Engine
AMOS Information Geometry Mapper
AMOS Provenance Trust Firewall
AMOS Constraint Propagation RSCF Engine
AMOS Metacognitive Confidence Auditor
RSCF Modeler
AMOS Infrastructure Control Plane
```

Capability boundary:

```text
AVAILABLE SKILL
!=
VALID RESULT

VALID RESULT
!=
AUTHORITY

AUTHORITY
!=
COMMIT
```

---

# 14. Workflow

```text
RECEIVE ATTENDED OBSERVATIONS
↓
VALIDATE TYPES
↓
PRESERVE OBSERVATION IDENTITIES
↓
RESOLVE MODALITY AVAILABILITY
↓
APPLY TEMPORAL / SPATIAL CONTEXT
↓
EXTRACT / GROUP FEATURES
↓
FORM CANDIDATE BINDINGS
↓
GENERATE PERCEPT CANDIDATES
↓
GENERATE MATERIAL ALTERNATIVES
↓
CHECK CONFLICTS
↓
PROPAGATE UNCERTAINTY
↓
APPLY CONFIDENCE CEILING
↓
ATTACH PROVENANCE + DEPENDENCIES
↓
PROPOSE PERCEPT STATE
↓
CONTROL-PLANE VALIDATION
↓
COMMIT / CONDITIONAL / COMPETING / UNKNOWN_GAP
```

---

# 15. Protocols

Candidate protocols:

```text
L03_RECEIVE_ATTENDED_OBSERVATION
L03_FEATURE_PROPOSAL
L03_BINDING_PROPOSAL
L03_PERCEPT_PROPOSAL
L03_COMPETING_PERCEPT_NOTICE
L03_UNCERTAINTY_NOTICE
L03_PROVENANCE_ATTACHMENT
L03_REVALIDATION_REQUEST
L03_REPAIR_REQUEST
L03_DOWNSTREAM_RELEASE
```

Canonical names:

```text
UNKNOWN/GAP
```

---

# 16. Evidence / Provenance

Every percept candidate should permit reconstruction:

```text
PERCEPT
↓
FEATURE / BINDING OPERATIONS
↓
ATTENTION STATE
↓
OBSERVATIONS
↓
SOURCE / SENSOR / TOOL / INPUT
```

Minimum candidate provenance:

```yaml
PerceptProvenance:

  percept_id: null

  observation_refs: []
  attention_ref: null

  feature_refs: []
  binding_refs: []

  source_origins: []
  transformation_lineage: []

  observer_context: null
  modality_state: null

  temporal_context: null
  spatial_context: null

  scope: null
  regime: null

  uncertainty: null
  confidence_ceiling: null
```

Hard rule:

```text
THREE PERCEPT FEATURES
derived from
ONE OBSERVATION

!=

THREE INDEPENDENT OBSERVATIONS
```

---

# 17. Uncertainty and Confidence Ceiling

L03 uncertainty should remain decomposable.

```yaml
uncertainty:
  observation: null
  attention: null
  feature: null
  binding: null
  temporal: null
  spatial: null
  multimodal: null
  observer: null
  scope: null
  regime: null
  provenance: null
  model: null
```

Candidate confidence bound:

[
C(P)
\le
\min
\left(
C(O),
C(A),
C(B),
C(Context),
C(Provenance)
\right)
]

for load-bearing dependencies.

This is an `AMOS_MODEL` equation.

A percept may be internally coherent while its confidence remains low.

---

# 18. Competing Percepts

L03 must support:

```yaml
CompetingPercept:
  hypothesis_id: string
  percept: PerceptCandidate
  supporting_evidence: []
  contradicting_evidence: []
  shared_ancestry: []
  unresolved_discriminators: []
  confidence_ceiling: null
```

Example:

```text
P1 = object A is moving
P2 = observer is moving
P3 = both are moving
```

If current observations cannot discriminate:

```text
P1 / P2 / P3
→ COMPETING
```

not forced convergence.

---

# 19. Failure Modes

```text
FM-L03-001
Percept treated as observation.

FM-L03-002
Percept treated as fact.

FM-L03-003
Missing evidence filled by inference.

FM-L03-004
Attention bias mistaken for environmental importance.

FM-L03-005
Observation ancestry lost.

FM-L03-006
Cross-modal hallucinated binding.

FM-L03-007
Temporal misbinding.

FM-L03-008
Spatial misbinding.

FM-L03-009
Observer-relative state treated as observer-independent.

FM-L03-010
Unavailable modality treated as negative observation.

FM-L03-011
Competing percept suppressed.

FM-L03-012
Correlated evidence double counted.

FM-L03-013
Confidence inflated through perceptual coherence.

FM-L03-014
Scope leakage.

FM-L03-015
Regime leakage.

FM-L03-016
Stale percept retained after observation invalidation.

FM-L03-017
Local percept promoted to global H state without closure.

FM-L03-018
Worker self-authorizes state mutation.

FM-L03-019
UNKNOWN/GAP treated as successful perception.

FM-L03-020
AMOS percept model presented as established neuroscience.
```

---

# 20. Repair / Recovery

```text
DETECT PERCEPT FAILURE
↓
IDENTIFY FAILED PREMISE / BINDING
↓
TRACE DEPENDENT PERCEPTS
↓
QUARANTINE AFFECTED PERCEPT STATE
↓
PRESERVE UNAFFECTED OBSERVATIONS
↓
PRESERVE UNAFFECTED PERCEPTS
↓
REOPEN COMPETING HYPOTHESES
↓
REQUEST DISCRIMINATING OBSERVATION IF NEEDED
↓
REBUILD AFFECTED BINDINGS
↓
RECALCULATE UNCERTAINTY
↓
REVALIDATE PROVENANCE / SCOPE / REGIME
↓
REPROPOSE
```

Selective repair rule:

[
Invalid(x)
\Rightarrow
Invalidate(Descendants(x))
]

not automatically:

[
Invalid(x)
\Rightarrow
Invalidate(All)
]

---

# 21. Tests / Validators

Minimum validators:

```text
VALIDATE_L03_INPUT_TYPES
VALIDATE_OBSERVATION_ANCESTRY
VALIDATE_ATTENTION_REFERENCE
VALIDATE_FEATURE_LINEAGE
VALIDATE_BINDINGS
VALIDATE_TEMPORAL_CONTEXT
VALIDATE_SPATIAL_CONTEXT
VALIDATE_MODALITY_STATE
VALIDATE_OBSERVER_CONTEXT
VALIDATE_SCOPE
VALIDATE_REGIME
VALIDATE_COMPETING_PERCEPTS
VALIDATE_PROVENANCE
VALIDATE_CONFIDENCE_CEILING
VALIDATE_SELECTIVE_INVALIDATION
VALIDATE_PROPOSAL_COMMIT_BOUNDARY
```

Minimum tests:

```text
TEST-L03-001
Percept without observation ancestry.
Expected: FAIL.

TEST-L03-002
Missing modality interpreted as negative evidence.
Expected: FAIL.

TEST-L03-003
Two unresolved percepts exist.
Expected: COMPETING preserved.

TEST-L03-004
One source produces several transformed features.
Expected: one provenance root retained.

TEST-L03-005
Supporting observation invalidated.
Expected: dependent percept invalidated.

TEST-L03-006
Unrelated observation changes.
Expected: independent percept remains valid.

TEST-L03-007
Worker produces highly coherent percept with weak evidence.
Expected: confidence ceiling remains weak.

TEST-L03-008
L-level feature promoted directly to H-level scene claim.
Expected: dependency-closure validation required.

TEST-L03-009
Worker requests authoritative commit merely because inference passed.
Expected: authority denied unless independently granted.

TEST-L03-010
Required input is UNKNOWN/GAP.
Expected: UNKNOWN_GAP, never PASS.
```

Execution state:

```yaml
tests_written_conceptually: true
tests_executed: false
runtime_verified: false
```

---

# 22. Falsifiers

This definition must be revised if direct evidence establishes:

```text
L03 is not percept formation;

canonical L03 occurs before attention rather than after it;

canonical L03 has materially different input/output semantics;

canonical AMOS collapses observation and percept into one primitive;

L03 does not preserve provenance;

canonical L03 forbids competing percept representations;

canonical H/M/L treatment materially differs;

direct executable runtime contradicts these modeled transformations;

formal canon supplies incompatible equations or invariants.
```

---

# 23. Gap Matrix

```yaml
gap_status:

  L03_role:
    status: MODEL_DEFINED

  observation_percept_separation:
    status: MODEL_STRONGLY_ALIGNED

  HML_requirement:
    status: SOURCE_ALIGNED

  typed_invariants_requirement:
    status: SOURCE_ALIGNED

  RSCF_requirement:
    status: SOURCE_ALIGNED

  provenance_requirement:
    status: SOURCE_ALIGNED

  falsifier_requirement:
    status: SOURCE_ALIGNED

  repair_requirement:
    status: SOURCE_ALIGNED

  confidence_ceiling_requirement:
    status: SOURCE_ALIGNED

  canonical_L03_definition:
    status: CRITICAL_GAP

  canonical_input_schema:
    status: CRITICAL_GAP

  canonical_output_schema:
    status: CRITICAL_GAP

  canonical_equations:
    status: DECISION_RELEVANT_GAP

  canonical_thresholds:
    status: DECISION_RELEVANT_GAP

  executable_runtime:
    status: CRITICAL_GAP

  executed_tests:
    status: CRITICAL_GAP
```

---

# 24. RSCF Completion State

```yaml
rscf:

  id: L03_PERCEPT_FORMATION_DEFINITION

  claim:
    L03_PERCEPT_FORMATION is modeled as the AMOS cognitive
    primitive that transforms attended, admissible observations
    into provenance-preserving percept candidates while retaining
    uncertainty, context, scope, regime, observer dependence,
    modality availability, and material competing percepts.

  claim_class: MODEL

  evidence:
    - AMOS Multimodal Perception Layer architecture
    - AMOS cognition architecture
    - AMOS Full Brain OS architecture
    - AMOS Infrastructure Control Plane architecture
    - preceding L01/L02 primitive contracts

  provenance:
    origin_architect: Trang Phan
    architecture_family: AMOS
    subsystem: COGNITIVE_MATRIX
    primitive: L03_PERCEPT_FORMATION
    artifact: DEFINITION.md
    derivation: AMOS_MODEL_SOURCE_BOUNDED

  scope:
    system: AMOS_OS
    subsystem: COGNITIVE_MATRIX
    primitive: L03_PERCEPT_FORMATION
    concern: percept_formation

  regime:
    governed cognitive/perceptual modeling

  freshness:
    revalidate_when:
      - direct L03 canon is recovered
      - cognitive primitive ordering changes
      - multimodal perception canon changes
      - L01 or L02 contracts change materially
      - executable L03 runtime becomes available

  dependencies:
    - L01_SENSING_OBSERVATION
    - L02_ATTENTION
    - AMOS_MULTIMODAL_PERCEPTION_LAYER
    - AMOS_RSCF
    - AMOS_PROVENANCE
    - AMOS_INFRASTRUCTURE_CONTROL_PLANE

  competing:
    - direct observation-to-percept mapping
    - attention-mediated percept formation
    - predictive/context-heavy percept formation
    - modality-specific percept formation before integration

  falsifiers:
    - incompatible direct L03 canon
    - incompatible primitive ordering
    - incompatible canonical state semantics
    - runtime evidence contradicting modeled topology

  uncertainty:
    evidence: MEDIUM
    model: MEDIUM
    scope: MEDIUM
    temporal: MEDIUM
    causal: LOW
    execution: MAXIMUM
    provenance_independence: MEDIUM

  confidence_ceiling:
    The AMOS methodological requirements for perception are
    source-aligned. The detailed identification and formalization
    of L03_PERCEPT_FORMATION remain MODEL until direct L03 canon
    and executable validation are recovered.

  gap_status:
    canonical_definition: CRITICAL_GAP
    canonical_schema: CRITICAL_GAP
    executable_runtime: CRITICAL_GAP
    executed_validation: CRITICAL_GAP

  cheapest_discriminating_test:
    Recover direct L03 canon and compare its primitive ordering,
    semantic definition, input/output types, state variables,
    invariants, and percept/observation boundary against this model.
```

---

# 25. Completion State

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
    status: MODEL_COMPLETE_SOURCE_PARTIAL

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

  canonical_definition:
    status: UNKNOWN_GAP

  executable_runtime:
    status: UNKNOWN_GAP

  runtime_validation:
    status: UNKNOWN_GAP

  overall:
    status: COMPLETE_FOR_DEFINITION_CONTRACT_SCOPE

  conclusion_class:
    MODEL
```

---

# 26. Hard Boundaries

```text
PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

UNKNOWN/GAP != PASS
```

L03-specific:

```text
REALITY != OBSERVATION

OBSERVATION != ATTENTION

ATTENTION != PERCEPT

PERCEPT != FACT

PERCEPT != BELIEF

PERCEPT != CAUSAL PROOF

PERCEPTUAL COHERENCE != TRUTH

MISSING MODALITY != NEGATIVE EVIDENCE

MULTIPLE DERIVATIONS != INDEPENDENT SOURCES

COMPETING != ERROR

LOCAL PERCEPT != GLOBAL PERCEPT

SOURCE_DEFINED != EMPIRICALLY_VALIDATED

MODEL != CANON

MODEL != IMPLEMENTATION

IMPLEMENTATION != VALIDATION
```

---

# 27. Governing Definition Contract

> **`L03_PERCEPT_FORMATION` SHALL be modeled as the bounded cognitive transformation from admitted and attention-conditioned observations into structured percept candidates. It SHALL preserve observation ancestry, modality availability, observer context, temporal and spatial conditions, scope, regime, provenance, uncertainty, and material competing percepts. It SHALL NOT convert missing evidence into observation, perceptual coherence into truth, correlated derivations into independent evidence, capability into authority, or a percept proposal into committed authoritative state. Any detailed L03 schema, equation, threshold, agent topology, or runtime behavior not directly supported by canon SHALL remain `MODEL` or `UNKNOWN/GAP`.**

---

# 28. Canon Boundary

```text
SOURCE-ALIGNED:

Trang Phan origin/stewardship

AMOS multimodal perception methodological architecture

H/M/L requirement

typed invariant requirement

RSCF requirement

equation provenance requirement

competing hypotheses

falsifiers

confidence ceiling

provenance

repair

hard-invariant non-compensation

SOURCE_DEFINED != external empirical validation


AMOS_MODEL:

L03 semantic definition

L01 → L02 → L03 detailed transformation mapping

typed L03 schemas

state variables

operators

percept candidate structure

agent names

protocol names

candidate equations

specific validation sequence


UNKNOWN/GAP:

direct canonical L03 definition

canonical schemas

canonical state variables

canonical equations

canonical thresholds

canonical protocol vocabulary

canonical implementation

executed tests

formal verification
```

Therefore:

```text
CONCLUSION CLASS:
MODEL

NOT:
VERIFIED L03 CANON

NOT:
IMPLEMENTED COGNITIVE PRIMITIVE

NOT:
VALIDATED PERCEPTION ENGINE

NOT:
EMPIRICAL THEORY OF HUMAN PERCEPTION

NOT:
AUTHORITY TO COMMIT PERCEPT STATE
```

```text

The definition is therefore **complete for the placeholder-contract scope but remains `MODEL`**, with the direct canonical L03 definition and executable validation preserved as critical gaps.
```

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
