---
tags:
  - amos
  - cognitive-matrix
  - l03
  - percept-formation
  - purpose
  - rscf
  - hml
  - governance

title: "L03_PERCEPT_FORMATION — Purpose"
origin_architect: "Trang Phan"
status: "MODEL_CONTRACT / UNIMPLEMENTED / UNVALIDATED"
epistemic_class: "MODEL"
runtime_alignment: "AMOS Full Brain OS / AMOS_CORE v4.4 lineage"
---

# L03_PERCEPT_FORMATION — Purpose

**Class:** `COGNITIVE_PRIMITIVE_PURPOSE_CONTRACT`  
**Origin architect / steward:** Trang Phan  
**Primitive:** `L03_PERCEPT_FORMATION`  
**Artifact:** `PURPOSE.md`  
**Status:** `AMOS_MODEL / UNIMPLEMENTED / UNVALIDATED`

## 0. Purpose

`L03_PERCEPT_FORMATION` exists to transform admitted, provenance-bearing observation state and attention-conditioned context into **structured percept candidates** that downstream cognition can address without mistaking interpretation for observation, salience for truth, or candidate structure for committed reality.

Its governing purpose is:

```text
OBSERVATION
+
ATTENTION-CONDITIONED CONTEXT
+
ADMISSIBLE MEMORY / PRIOR CONTEXT
↓
FEATURE / RELATION / BINDING FORMATION
↓
PERCEPT CANDIDATE(S)
+
PROVENANCE
+
UNCERTAINTY
+
COMPETING INTERPRETATIONS
↓
VALIDATION / DOWNSTREAM COGNITIVE USE
```

L03 is therefore a **formation layer**, not a truth oracle.

Hard semantic boundary:

```text
SENSED != PERCEIVED
PERCEIVED != TRUE
SALIENT != TRUE
BOUND != VERIFIED
INTERPRETED != OBSERVED
CANDIDATE != COMMITTED STATE
```

The primitive should preserve enough source structure that downstream cognition can determine what was observed, what was selected by attention, what was supplied by memory, what was inferred, and what remains uncertain.

---

# 1. Source / Canon References

## 1.1 Architecture-aligned references

This purpose contract is aligned with the available AMOS architecture families concerning:

```text
AMOS Full Brain OS
AMOS Cognition
AMOS_CORE v3.0 → v4.4 lineage
AMOS recursive RSCF / H-M-L
AMOS attention allocation
AMOS multimodal perception
AMOS information operators
AMOS binding architecture
AMOS distinction/relation/constraint architecture
AMOS provenance topology
AMOS epistemic regimes
AMOS memory governance
AMOS infrastructure/control-plane separation
AMOS deterministic AI control-plane lineage
```

Relevant architectural principles include:

```text
integrity > completeness > fluency > speed

observation != derivation

capability != authority

proposal != commit

unknown/gap != pass

confidence cannot exceed unresolved
load-bearing premises

shared provenance cannot manufacture
independent confirmation
```

## 1.2 Direct L03 canon status

The available architecture supports a percept-formation role, but this contract does not establish a recovered canonical `L03_PERCEPT_FORMATION/PURPOSE.md`.

Therefore:

```yaml
canonical_L03_purpose_text: UNKNOWN_GAP
canonical_L03_boundary_definition: UNKNOWN_GAP
canonical_L03_input_schema: UNKNOWN_GAP
canonical_L03_output_schema: UNKNOWN_GAP
canonical_L03_operator_registry: UNKNOWN_GAP
canonical_L03_runtime: UNKNOWN_GAP
```

Everything below that specializes these architecture principles into an L03 contract is `AMOS_MODEL` unless separately recovered from direct canon.

---

# 2. Definition and Scope

## 2.1 Definition

Candidate definition:

> `L03_PERCEPT_FORMATION` is the AMOS cognitive primitive responsible for constructing typed, provenance-bearing, uncertainty-aware percept candidates from admissible observations, attention state, contextual information, and permitted prior state while preserving the distinction between external observation and internal interpretation.

Candidate functional abstraction:

[
P_t^{*}
=======

\mathcal{F}_{L03}
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
O_t = admitted observation state
A_t = attention-conditioned state
C_t = active contextual constraints
M_t = admissible memory/prior context
R_t = regime/observer state

P*_t = percept candidate set
```

`AMOS_MODEL`.

The star is deliberate:

```text
P*_t = candidate percept
not committed world state
```

## 2.2 In scope

L03 may include:

```text
feature formation
feature grouping
relation detection
binding
object/event candidate construction
cross-modal association
temporal association
spatial association
figure/background organization
candidate interpretation
percept competition
uncertainty propagation
provenance preservation
percept-state proposal
```

## 2.3 Out of scope

L03 does not independently own:

```text
raw sensing hardware
source admission authority
attention authority
long-term memory governance
belief commitment
causal proof
planning
decision authority
external action
durable state commit
empirical truth determination
```

---

# 3. Typed Inputs

```yaml
PerceptFormationInput:

  observations:
    type: ObservationState[]
    required: true

  attention_state:
    type: AttentionState
    required: true

  observer_context:
    type: ObserverContext
    required: true

  active_scope:
    type: ScopeEnvelope
    required: true

  active_regime:
    type: RegimeRef
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
```

Memory input must remain explicitly typed as memory.

```text
MEMORY_CONTEXT
!=
CURRENT_OBSERVATION
```

---

# 4. Typed Outputs

```yaml
PerceptFormationOutput:

  percept_candidates:
    type: PerceptCandidate[]

  features:
    type: FeatureState[]

  relations:
    type: RelationState[]

  bindings:
    type: BindingCandidate[]

  competing_percepts:
    type: CompetingPerceptSet[]

  unresolved_elements:
    type: PerceptGap[]

  provenance:
    type: ProvenanceGraph

  uncertainty:
    type: UncertaintyVector

  confidence_ceiling:
    type: ConfidenceBound

  validation_state:
    type:
      - CANDIDATE
      - CONDITIONAL
      - COMPETING
      - QUARANTINED
      - REJECTED
      - UNKNOWN_GAP

  state_proposal:
    type: PerceptStateProposal | null
```

No L03 output is automatically a committed cognitive state.

---

# 5. State Variables

Candidate state:

```text
O_t       = active observations
A_t       = attention state
F_t       = extracted/formed features
R_t       = candidate relations
B_t       = candidate bindings
P*_t      = percept candidates
CP_t      = competing percepts

Ctx_t     = contextual state
Mem_t     = admissible memory context

Prov_t    = provenance graph
U_t       = uncertainty vector
Conf_t    = confidence ceiling

Scope_t   = active scope
Reg_t     = active regime
Obs_t     = observer context

Gap_t     = unresolved percept gaps
Q_t       = quarantined candidates
Ver_t     = state/version reference
```

---

# 6. Core Operators

Candidate L03 operator family:

```text
RECEIVE_OBSERVATION
APPLY_ATTENTION_CONTEXT
FORM_FEATURE
DISTINGUISH
RELATE
GROUP
SEGMENT
BIND
UNBIND
ALIGN_MODALITIES
ASSOCIATE_TEMPORALLY
ASSOCIATE_SPATIALLY
FORM_OBJECT_CANDIDATE
FORM_EVENT_CANDIDATE
COMPARE_PERCEPTS
REGISTER_COMPETING
PROPAGATE_UNCERTAINTY
TRACE_PROVENANCE
CHECK_SCOPE
CHECK_REGIME
PROPOSE_PERCEPT_STATE
QUARANTINE_PERCEPT
INVALIDATE_PERCEPT
REBUILD_PERCEPT
```

These names are model-level placeholders until canonical operator identifiers are recovered.

---

# 7. Purpose Invariants

```text
L03-PURPOSE-INV-001
L03 SHALL distinguish observation from interpretation.

L03-PURPOSE-INV-002
Attention SHALL influence processing priority without becoming evidence of truth.

L03-PURPOSE-INV-003
Memory SHALL remain distinguishable from current observation.

L03-PURPOSE-INV-004
Every material percept candidate SHALL retain recoverable provenance.

L03-PURPOSE-INV-005
Percept formation SHALL preserve material uncertainty.

L03-PURPOSE-INV-006
Ambiguous observations SHALL permit multiple competing percepts.

L03-PURPOSE-INV-007
L03 SHALL NOT force convergence where evidence does not discriminate.

L03-PURPOSE-INV-008
Feature formation SHALL NOT manufacture independent evidence.

L03-PURPOSE-INV-009
Binding SHALL NOT establish external truth.

L03-PURPOSE-INV-010
Cross-modal agreement SHALL NOT automatically imply independent confirmation.

L03-PURPOSE-INV-011
Unavailable modality SHALL NOT automatically count as contradictory evidence.

L03-PURPOSE-INV-012
Percept confidence SHALL inherit load-bearing premise ceilings.

L03-PURPOSE-INV-013
Scope changes SHALL trigger applicability review.

L03-PURPOSE-INV-014
Regime changes SHALL trigger applicability review.

L03-PURPOSE-INV-015
Percept state proposal SHALL remain distinct from commit.

L03-PURPOSE-INV-016
Worker capability SHALL remain distinct from authority.

L03-PURPOSE-INV-017
Unknown/GAP SHALL NOT satisfy a required validation gate.

L03-PURPOSE-INV-018
Failure of one percept candidate SHALL NOT invalidate independent candidates without dependency justification.

L03-PURPOSE-INV-019
Repair SHALL preserve or explicitly supersede prior provenance.

L03-PURPOSE-INV-020
L03 SHALL NOT claim causal structure from perceptual association alone.
```

---

# 8. Dependencies

## Upstream

```text
L01_SENSING_OBSERVATION
L02_ATTENTION
```

Conceptual dependency:

[
L01 \rightarrow L02 \rightarrow L03
]

but this does not require a strictly linear runtime.

L03 may consume observation and attention state through governed protocols rather than direct ownership.

## Internal L03 dependencies

```text
DEFINITION
VARIABLES
STATE
OPERATORS
INVARIANTS
DEPENDENCIES
EQUATIONS
HML
MEMORY
PROVENANCE
PROTOCOLS
CONTROL_PLANES
FAILURE_MODES
REPAIR
TESTS
RSCF
```

## Cross-cutting dependencies

```text
AMOS RSCF
AMOS H/M/L
AMOS provenance topology
AMOS epistemic classification
AMOS multimodal perception
AMOS information operators
AMOS binding architecture
AMOS memory governance
AMOS infrastructure control plane
AMOS constraint propagation
```

---

# 9. H/M/L Applicability

## L — Local percept formation

Concern:

```text
individual signals
edges
features
local temporal changes
local spatial relations
single-source candidate structure
```

Candidate transformation:

[
O_L \rightarrow F_L
]

## M — Subsystem percept formation

Concern:

```text
feature groups
objects
events
multimodal bindings
local scenes
candidate identities
candidate relations
```

Candidate transformation:

[
{F_L,R_L}
\rightarrow
P_M^{*}
]

## H — Governing percept formation

Concern:

```text
scene interpretation
cross-subsystem coherence
context-conditioned percept organization
competing scene models
decision-relevant percept abstraction
```

Candidate:

[
{P_M^{*}}
\rightarrow
P_H^{*}
]

Hard cross-scale rule:

```text
HIGHER-LEVEL PERCEPT
MUST NOT ERASE
DECISION-RELEVANT LOWER-LEVEL UNCERTAINTY
```

---

# 10. Control-Plane Requirements

L03 cognition workers may generate percept candidates, but control-plane responsibilities remain external.

Control plane should govern or validate:

```text
input admission state
schema compatibility
state versions
scope/regime identity
provenance requirements
authority witnesses
memory-access authorization
constraint freshness
validation epochs
commit eligibility
durable state mutation
rollback/invalidation
```

Worker-side L03 may:

```text
form candidates
rank candidates
report uncertainty
detect conflicts
request evidence
propose state
```

Worker-side L03 may not independently:

```text
grant itself memory authority
change governing constraints
erase provenance
declare unknown evidence valid
convert proposal into commit
override revocation
manufacture independent confirmation
```

---

# 11. Agents

Candidate capability roles:

```text
L03_FEATURE_FORMATION_AGENT
L03_RELATION_AGENT
L03_BINDING_AGENT
L03_MULTIMODAL_ALIGNMENT_AGENT
L03_PERCEPT_SYNTHESIS_AGENT
L03_COMPETING_PERCEPT_AGENT
L03_PROVENANCE_AUDITOR
L03_UNCERTAINTY_AUDITOR
L03_PERCEPT_REPAIR_AGENT
L03_VALIDATION_AGENT
```

These are architectural roles.

```text
AGENT DEFINITION
!=
DEPLOYED AGENT

DEPLOYED AGENT
!=
AUTHORIZED AGENT
```

---

# 12. Skills

Relevant AMOS skill families include:

```text
AMOS Attention Allocation Governor
AMOS Multimodal Perception Layer
AMOS Sensory Map Integrator
AMOS Binding RSCF Engine
AMOS Distinction RSCF Architecture
AMOS Distinction-Relation-Constraint Algebra
AMOS Information Operator Engine
AMOS Provenance Trust Firewall
AMOS Cross-Scale RSCF Tensor Engine
AMOS Temporal Multi-Scale RSCF Engine
AMOS Memory Conflict Governor
AMOS Cognitive Process Orchestrator
AMOS Metacognitive Confidence Auditor
AMOS Infrastructure Control Plane
```

These provide architectural capabilities or reasoning contracts.

They do not prove an executable L03 implementation.

---

# 13. Primary Workflow

```text
ADMITTED OBSERVATIONS
↓
LOAD ATTENTION STATE
↓
CHECK:
  scope
  regime
  provenance
  freshness
↓
FORM LOCAL FEATURES
↓
FORM RELATIONS
↓
GENERATE CANDIDATE BINDINGS
↓
ALIGN AVAILABLE MODALITIES
↓
INCORPORATE PERMITTED CONTEXT / MEMORY
↓
FORM PERCEPT CANDIDATE(S)
↓
PRESERVE COMPETING INTERPRETATIONS
↓
PROPAGATE UNCERTAINTY
↓
BUILD PROVENANCE
↓
VALIDATE INVARIANTS
↓
PROPOSE PERCEPT STATE
↓
CONTROL-PLANE VALIDATION / DOWNSTREAM HANDOFF
```

---

# 14. Ambiguity Workflow

```text
AMBIGUOUS INPUT
↓
GENERATE:
  P1
  P2
  ...
  Pn
↓
COMPARE SUPPORT
↓
CHECK PROVENANCE INDEPENDENCE
↓
IDENTIFY DISCRIMINATING EVIDENCE
↓
IF SUFFICIENT:
    RESOLVE CONDITIONALLY
ELSE:
    PRESERVE COMPETING
```

Hard rule:

```text
AMBIGUITY
MUST NOT
BE HIDDEN BY FLUENCY
```

---

# 15. Protocols

Candidate protocol surfaces:

```text
OBSERVATION_INGRESS
ATTENTION_CONTEXT_HANDOFF
MEMORY_CONTEXT_REQUEST
MEMORY_CONTEXT_RESULT
FEATURE_STATE_PROPOSAL
RELATION_STATE_PROPOSAL
BINDING_PROPOSAL
MULTIMODAL_ALIGNMENT_RESULT
PERCEPT_CANDIDATE_PROPOSAL
COMPETING_PERCEPT_REGISTER
PROVENANCE_CHECK_REQUEST
VALIDATION_REQUEST
VALIDATION_RESULT
GAP_REQUEST
REPAIR_REQUEST
REPAIR_RESULT
STATE_PROPOSAL
INVALIDATION_NOTICE
```

Every protocol carrying material percept state should carry:

```text
state identity
version
scope
regime
provenance
uncertainty
epistemic class
```

where applicable.

---

# 16. Evidence / Provenance

Contract provenance:

```yaml
origin_architect:
  value: Trang Phan
  class: SOURCE_METADATA

architecture_family:
  value: AMOS

subsystem:
  value: COGNITIVE_MATRIX

primitive:
  value: L03_PERCEPT_FORMATION

artifact:
  value: PURPOSE.md

derivation:
  class: AMOS_MODEL
  basis:
    - available AMOS cognition architecture
    - attention architecture
    - perception architecture
    - provenance architecture
    - RSCF/HML architecture
    - control-plane architecture

direct_canonical_PURPOSE_md:
  status: NOT_ESTABLISHED

implementation_evidence:
  status: NONE_ESTABLISHED

runtime_validation:
  status: NONE_ESTABLISHED

empirical_validation:
  status: NONE_ESTABLISHED
```

---

# 17. Uncertainty and Confidence Ceiling

```yaml
uncertainty:

  architectural_role:
    level: MEDIUM

  canonical_wording:
    level: MAXIMUM

  canonical_types:
    level: HIGH

  canonical_operators:
    level: MAXIMUM

  HML_specialization:
    level: HIGH

  control_plane_mapping:
    level: MEDIUM_HIGH

  runtime:
    level: MAXIMUM

  empirical:
    level: MAXIMUM
```

Confidence ceiling:

> The available AMOS architecture supports treating percept formation as a provenance-aware, attention-conditioned, uncertainty-preserving cognitive transformation layer. The exact canonical L03 purpose, schemas, operator registry, runtime implementation, and empirical validity remain unresolved.

Therefore:

```text
ARCHITECTURAL PURPOSE:
MODEL

IMPLEMENTATION CLAIM:
UNKNOWN/GAP

EMPIRICAL CLAIM:
NOT ESTABLISHED
```

---

# 18. Failure Modes

```text
FM-L03-PURPOSE-001
Observation and interpretation collapse.

FM-L03-PURPOSE-002
Attention salience becomes truth weighting.

FM-L03-PURPOSE-003
Memory becomes indistinguishable from current observation.

FM-L03-PURPOSE-004
Feature extraction erases source provenance.

FM-L03-PURPOSE-005
Binding forces one interpretation prematurely.

FM-L03-PURPOSE-006
Ambiguity is hidden instead of represented.

FM-L03-PURPOSE-007
Competing percepts are collapsed without discriminating evidence.

FM-L03-PURPOSE-008
Cross-modal correlation is mistaken for independent confirmation.

FM-L03-PURPOSE-009
Unavailable modality becomes negative evidence.

FM-L03-PURPOSE-010
Percept association is promoted into causation.

FM-L03-PURPOSE-011
Context dominates contradictory observation without explicit justification.

FM-L03-PURPOSE-012
Prior percept creates self-confirming percept loop.

FM-L03-PURPOSE-013
Stale memory contaminates current percept.

FM-L03-PURPOSE-014
Scope mismatch is ignored.

FM-L03-PURPOSE-015
Regime shift is ignored.

FM-L03-PURPOSE-016
Confidence exceeds load-bearing evidence.

FM-L03-PURPOSE-017
Unknown state passes validation.

FM-L03-PURPOSE-018
Candidate state is treated as committed state.

FM-L03-PURPOSE-019
Worker capability becomes unauthorized state authority.

FM-L03-PURPOSE-020
Repair rewrites provenance instead of preserving lineage.
```

---

# 19. Repair / Recovery

```text
DETECT PERCEPT FAILURE
↓
FREEZE AFFECTED CANDIDATE
↓
TRACE DEPENDENCIES
↓
SEPARATE:
  observation
  attention influence
  memory influence
  derived features
  relations
  bindings
  assumptions
↓
IDENTIFY EARLIEST FAILED PREMISE / EDGE
↓
QUARANTINE AFFECTED BRANCH
↓
PRESERVE UNAFFECTED BRANCHES
↓
REBUILD FROM NEAREST VALID STATE
↓
REGENERATE COMPETING PERCEPTS
↓
RECOMPUTE UNCERTAINTY
↓
RECOMPUTE CONFIDENCE CEILING
↓
REVALIDATE
↓
PROPOSE REPAIRED STATE
```

Hard recovery rule:

```text
REPAIR
!=
RETROACTIVE JUSTIFICATION
```

The repair process must not invent missing observation evidence to preserve a preferred percept.

---

# 20. Tests / Validators

Minimum conceptual validators:

```text
VALIDATE_OBSERVATION_INTERPRETATION_SEPARATION
VALIDATE_ATTENTION_TRUTH_SEPARATION
VALIDATE_MEMORY_OBSERVATION_SEPARATION
VALIDATE_PROVENANCE_CONTINUITY
VALIDATE_FEATURE_LINEAGE
VALIDATE_BINDING_LINEAGE
VALIDATE_COMPETING_PERCEPT_PRESERVATION
VALIDATE_MULTIMODAL_ANCESTRY
VALIDATE_SCOPE_COMPATIBILITY
VALIDATE_REGIME_COMPATIBILITY
VALIDATE_UNCERTAINTY_PROPAGATION
VALIDATE_CONFIDENCE_CEILING
VALIDATE_PROPOSAL_COMMIT_SEPARATION
VALIDATE_UNKNOWN_NOT_PASS
```

Conceptual tests:

```text
TEST-L03-PURPOSE-001
Provide ambiguous sensory evidence.
Expected:
multiple percept candidates may remain COMPETING.

TEST-L03-PURPOSE-002
Increase attention on weak evidence without changing evidence.
Expected:
salience may change; evidential truth status does not.

TEST-L03-PURPOSE-003
Supply stale memory conflicting with fresh observation.
Expected:
conflict remains explicit; memory does not overwrite observation.

TEST-L03-PURPOSE-004
Remove one modality.
Expected:
missing modality is marked unavailable, not contradictory.

TEST-L03-PURPOSE-005
Provide two modalities sharing one upstream origin.
Expected:
they are not counted automatically as independent evidence.

TEST-L03-PURPOSE-006
Create strong feature binding from uncertain observations.
Expected:
binding confidence remains bounded by load-bearing uncertainty.

TEST-L03-PURPOSE-007
Change operating regime.
Expected:
affected percept assumptions require revalidation.

TEST-L03-PURPOSE-008
Invalidate one load-bearing observation.
Expected:
dependent percepts invalidate selectively.

TEST-L03-PURPOSE-009
Produce a valid candidate without commit authority.
Expected:
state remains PROPOSAL.

TEST-L03-PURPOSE-010
Leave critical provenance unknown.
Expected:
UNKNOWN/GAP, not PASS.
```

Current validation state:

```yaml
tests_defined: true
tests_executed: false
formal_verification: false
runtime_validation: false
empirical_validation: false
```

---

# 21. Falsifiers

This contract should be revised if stronger source or executable evidence establishes:

```text
a different canonical purpose for L03;

that percept formation is owned by another primitive;

that attention is not an upstream/context dependency;

that memory is canonically prohibited from percept formation;

that percept formation commits state directly;

that provenance is not required at L03;

that competing percepts are represented elsewhere;

that H/M/L applies differently;

that control-plane ownership differs materially;

or executable canonical behavior contradicts these invariants.
```

---

# 22. Gap Matrix

```yaml
gap_status:

  broad_percept_formation_role:
    status: SOURCE_ALIGNED_MODEL

  observation_interpretation_boundary:
    status: SOURCE_ALIGNED_MODEL

  attention_truth_boundary:
    status: SOURCE_ALIGNED

  provenance_requirement:
    status: SOURCE_ALIGNED_MODEL

  competing_hypothesis_requirement:
    status: SOURCE_ALIGNED_MODEL

  confidence_ceiling:
    status: SOURCE_ALIGNED

  selective_invalidation:
    status: SOURCE_ALIGNED_MODEL

  canonical_PURPOSE_md:
    status: CRITICAL_GAP

  canonical_definition:
    status: CRITICAL_GAP

  canonical_input_output_types:
    status: DECISION_RELEVANT_GAP

  canonical_state_variables:
    status: DECISION_RELEVANT_GAP

  canonical_operator_registry:
    status: DECISION_RELEVANT_GAP

  canonical_HML_mapping:
    status: DECISION_RELEVANT_GAP

  canonical_runtime:
    status: CRITICAL_GAP

  executed_tests:
    status: CRITICAL_GAP

  formal_validation:
    status: CRITICAL_GAP

  empirical_validation:
    status: CRITICAL_GAP
```

---

# 23. Competing Architectural Interpretations

### COMPETING-001 — Feed-forward percept formation

```text
observation
→ features
→ percept
```

Advantage: simplicity.

Limitation: weak handling of context, ambiguity, memory, and recursive correction.

### COMPETING-002 — Attention-conditioned formation

```text
observation
+
attention
→
percept
```

Advantage: captures selection and prioritization.

Limitation: incomplete treatment of memory and competing hypotheses.

### COMPETING-003 — Contextual recurrent formation

```text
observation
+
attention
+
prior context
+
memory
↔
candidate percepts
```

Advantage: supports iterative interpretation.

Risk: self-confirming loops.

### COMPETING-004 — Governed provenance-bearing formation

```text
observations
+
attention
+
authorized context/memory
+
scope/regime
↓
typed transformations
↓
competing percept candidates
+
provenance
+
uncertainty
↓
validation
↓
state proposal
```

Current model preference:

```text
COMPETING-004
```

because it best preserves the available AMOS epistemic, provenance, H/M/L, uncertainty, and control-plane boundaries.

But:

```text
MODEL PREFERENCE
!=
CANONICAL L03 PURPOSE
```

---

# 24. RSCF Completion State

```yaml
rscf:

  id: L03_PERCEPT_FORMATION_PURPOSE

  claim:
    L03_PERCEPT_FORMATION serves as a governed cognitive formation
    layer that converts admitted observations and attention-conditioned
    context into structured, provenance-bearing, uncertainty-aware
    percept candidates while preserving observation/interpretation,
    memory/observation, candidate/commit, and capability/authority
    distinctions.

  claim_class: MODEL

  evidence:
    - AMOS cognition architecture
    - AMOS attention architecture
    - AMOS perception architecture
    - AMOS RSCF/HML architecture
    - AMOS provenance architecture
    - AMOS control-plane architecture

  provenance:
    origin_architect: Trang Phan
    architecture_family: AMOS
    subsystem: COGNITIVE_MATRIX
    primitive: L03_PERCEPT_FORMATION
    artifact: PURPOSE.md
    derivation: SOURCE_ARCHITECTURE_PLUS_L03_MODEL

  scope:
    system: AMOS_OS
    subsystem: COGNITIVE_MATRIX
    primitive: L03_PERCEPT_FORMATION
    concern: purpose_and_functional_boundary

  regime:
    governed cognitive percept formation

  freshness:
    revalidate_when:
      - direct L03 canon is recovered
      - cognition architecture changes
      - L01 observation contract changes
      - L02 attention contract changes
      - memory contract changes
      - HML contract changes
      - control-plane contract changes
      - executable L03 runtime appears

  dependencies:
    - L01_SENSING_OBSERVATION
    - L02_ATTENTION
    - L03_PERCEPT_FORMATION_DEFINITION
    - L03_PERCEPT_FORMATION_STATE
    - L03_PERCEPT_FORMATION_OPERATORS
    - L03_PERCEPT_FORMATION_INVARIANTS
    - L03_PERCEPT_FORMATION_PROVENANCE
    - L03_PERCEPT_FORMATION_MEMORY
    - AMOS_RSCF
    - AMOS_HML
    - AMOS_PROVENANCE
    - AMOS_INFRASTRUCTURE_CONTROL_PLANE

  competing:
    - feed-forward percept formation
    - attention-conditioned percept formation
    - contextual recurrent percept formation
    - governed provenance-bearing percept formation

  falsifiers:
    - incompatible direct L03 canon
    - incompatible cognitive primitive ordering
    - incompatible state ownership
    - incompatible memory semantics
    - incompatible HML semantics
    - incompatible control-plane semantics
    - executable canonical counterexample

  uncertainty:
    architecture_role: MEDIUM
    direct_canon: MAXIMUM
    canonical_types: HIGH
    canonical_operators: MAXIMUM
    runtime: MAXIMUM
    empirical: MAXIMUM

  confidence_ceiling:
    The architecture-level role is sufficiently supported to construct
    an AMOS MODEL contract, but direct L03 canon, implementation,
    executable validation, and empirical perceptual validity are not
    established.

  gap_status:
    direct_canon: CRITICAL_GAP
    canonical_schema: DECISION_RELEVANT_GAP
    canonical_operators: DECISION_RELEVANT_GAP
    runtime: CRITICAL_GAP
    validation: CRITICAL_GAP
    empirical: CRITICAL_GAP

  cheapest_discriminating_test:
    Recover the direct canonical L03 definition/purpose material and
    compare its declared inputs, outputs, state ownership, operators,
    H/M/L behavior, and commit boundary against this model contract.
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

  direct_canon:
    status: UNKNOWN_GAP

  executable_runtime:
    status: UNKNOWN_GAP

  empirical_validation:
    status: UNKNOWN_GAP

  overall:
    status: COMPLETE_FOR_PURPOSE_CONTRACT_SCOPE

  conclusion_class:
    MODEL
```

---

# 26. Governing Purpose Contract

> **`L03_PERCEPT_FORMATION` SHALL form structured percept candidates from admitted observations, attention-conditioned context, and explicitly typed admissible prior context while preserving the distinction between observation and interpretation, current observation and memory, salience and evidence, association and causation, candidate and validated state, capability and authority, and proposal and commit. Material percept candidates SHALL preserve provenance, uncertainty, scope, regime, observer context, dependencies, and competing interpretations sufficient for downstream validation and selective invalidation. L03 SHALL NOT manufacture evidential independence through feature formation, binding, multimodal fusion, duplication, agent multiplicity, or transformation; SHALL NOT force convergence where discriminating evidence is insufficient; and SHALL NOT convert perceptual coherence into truth, causal proof, authority, or durable commitment. Unknown load-bearing state SHALL remain `UNKNOWN/GAP`. Failed dependencies SHALL invalidate only affected descendants, and repair SHALL rebuild from the nearest valid state without inventing missing evidence.**

---

# 27. Canon Boundary

```text
SOURCE / ARCHITECTURE-ALIGNED:

Trang Phan origin/stewardship
AMOS cognitive architecture
attention as bounded allocation/selection
RSCF/HML reasoning
epistemic classification
provenance discipline
competing-hypothesis preservation
scope/regime discipline
confidence ceilings
selective invalidation
control-plane separation
proposal != commit
capability != authority
unknown/gap != pass


AMOS_MODEL:

exact L03 purpose wording
L03 functional equation
L03 typed input/output schemas
L03 state variables
L03 operator names
L03 agent roles
L03 protocols
L03 workflows
L03 H/M/L specialization
L03 failure taxonomy
L03 test suite


UNKNOWN/GAP:

canonical PURPOSE.md
canonical L03 definition
canonical schemas
canonical operator registry
canonical state ownership
canonical runtime behavior
implemented L03 runtime
executed tests
formal verification
empirical perceptual validation
```

Therefore:

```text
CONCLUSION CLASS:
MODEL

PURPOSE CONTRACT:
MODEL-COMPLETE FOR DECLARED SCOPE

DIRECT L03 PURPOSE CANON:
UNKNOWN/GAP

IMPLEMENTATION:
UNKNOWN/GAP

RUNTIME VALIDATION:
UNKNOWN/GAP

EMPIRICAL VALIDITY:
NOT ESTABLISHED
```

```text
```

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]]
