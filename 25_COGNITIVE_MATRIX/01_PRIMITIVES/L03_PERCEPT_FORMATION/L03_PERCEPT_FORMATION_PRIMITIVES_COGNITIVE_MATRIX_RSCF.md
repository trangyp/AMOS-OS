---
title: L03 PERCEPT FORMATION PRIMITIVES COGNITIVE MATRIX RSCF
type: cognitive
source: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L03_PERCEPT_FORMATION
tags:
- cognitive-matrix
- primitives
- matrix/l03-percept-formation
- note
- domain/cognitive-matrix
rscf:
  state: DERIVED
  claim_class: EMPIRICAL
  provenance: AMOS_corpus
  scope: AMOS_general
---

# L03_PERCEPT_FORMATION — RSCF

**Class:** `COGNITIVE_PRIMITIVE_CONTRACT`
**Origin architect / steward:** Trang Phan
**Artifact:** `L03_PERCEPT_FORMATION/RSCF.md`
**Status:** `AMOS_MODEL / UNIMPLEMENTED / UNVALIDATED`

## 0. Contract status

This artifact defines the **RSCF representation and governance contract** for `L03_PERCEPT_FORMATION`. An RSCF represents what is sourced, observed, derived, modeled, competing, decided, or unknown; the existence of an RSCF is not itself proof.

```text
PLACEHOLDER != IMPLEMENTED
ADDRESSABLE != VALIDATED
CAPABILITY != AUTHORITY
PROPOSAL != COMMIT
UNKNOWN/GAP != PASS

RSCF != PROOF
COHERENCE != TRUTH
MULTIPLE DESCENDANTS != INDEPENDENT EVIDENCE
PERCEPT != OBSERVATION
CONFIDENCE != EVIDENCE
```

---

## 1. Source / canon references

```yaml
source_family:
  origin_architect: Trang Phan
  architecture: AMOS

architecture_dependencies:
  - L01_SENSING_OBSERVATION
  - L02_ATTENTION
  - L03_PERCEPT_FORMATION
  - AMOS_RSCF
  - AMOS_HML
  - AMOS_PROVENANCE
  - AMOS_SCOPE_REGIME_FIREWALL
  - AMOS_CAUSAL_FIREWALL
  - AMOS_COMPETING_HYPOTHESES
  - AMOS_SELECTIVE_INVALIDATION
```

The governing RSCF conventions require typed knowledge nodes, explicit dependency edges, applicability envelopes, competing hypotheses, falsifiers, confidence ceilings, and gap classification.

Direct canonical L03-specific RSCF schema remains unresolved:

```yaml
direct_L03_RSCF_canon: UNKNOWN_GAP
canonical_L03_node_schema: UNKNOWN_GAP
canonical_L03_confidence_equation: UNKNOWN_GAP
canonical_L03_runtime_binding: UNKNOWN_GAP
```

---

## 2. Definition and scope

`L03_RSCF` is the governed evidence-and-dependency representation associated with percept formation.

Its purpose is to prevent a formed percept from becoming an unsupported fact merely because it is internally coherent.

Conceptually:

[
RSCF_{L03}
==========

\langle
C,T,HML,P,E,D,A,K,F,U,G
\rangle
]

where:

```text
C   = claim/percept
T   = epistemic type
HML = H/M/L coordinate
P   = premises
E   = evidence
D   = dependency graph
A   = applicability envelope
K   = competing hypotheses
F   = falsifiers
U   = uncertainty/confidence state
G   = gaps
```

This equation is `AMOS_MODEL`, not an established external scientific equation.

---

## 3. Typed inputs / outputs

```yaml
L03RSCFInput:

  target:
    type: PerceptCandidate | PerceptClaim
    required: true

  observations:
    type: ObservationRef[]
    required: true

  attention_context:
    type: AttentionStateRef
    required: false

  features:
    type: FeatureNode[]
    required: true

  relations:
    type: RelationNode[]
    required: false

  bindings:
    type: BindingNode[]
    required: false

  provenance:
    type: ProvenanceGraph
    required: true

  dependencies:
    type: DependencyGraph
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

  uncertainty:
    type: UncertaintyVector
    required: true
```

```yaml
L03RSCFOutput:

  rscf:
    type: PerceptRSCF

  conclusion_class:
    type:
      - VERIFIED
      - DERIVED
      - MODEL
      - CONDITIONAL
      - COMPETING
      - UNKNOWN_GAP

  HML_path:
    type: HMLPath

  load_bearing_premises:
    type: PremiseRef[]

  competing:
    type: CompetingPercept[]

  falsifiers:
    type: Falsifier[]

  confidence_ceiling:
    type: ConfidenceBound

  gaps:
    type: Gap[]

  discriminating_test:
    type: TestProposal | null

  commit_authority:
    type: NONE
```
---

## 4. State variables

```text
C_t       = target percept/claim
Type_t    = epistemic class
Obs_t     = supporting observations
Feat_t    = feature state
Rel_t     = relation state
Bind_t    = binding state

H_t       = governing percept context
M_t       = intermediate percept structure
L_t       = local percept evidence

Prem_t    = load-bearing premises
Dep_t     = dependency graph
Prov_t    = provenance topology

Scope_t   = applicability scope
Reg_t     = regime
Fresh_t   = freshness state

Comp_t    = competing hypotheses
Fal_t     = falsifiers
Gap_t     = unresolved gaps
U_t       = uncertainty vector
Conf_t    = confidence ceiling

Ver_t     = state/version identity
```

---

## 5. Epistemic node types

L03 SHALL preserve the AMOS knowledge distinction:

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL
DECISION
UNKNOWN
```

These types must not silently collapse into one another. The RSCF model explicitly requires separation of source claims, observations, derivations, models, decisions, and unknown state.

Examples:

```yaml
sensor_record:
  type: OBSERVATION

"these edges probably belong to one object":
  type: DERIVED

"object permanence architecture":
  type: MODEL

"treat candidate A as active percept":
  type: DECISION

"source of conflicting feature unavailable":
  type: UNKNOWN
```

---

## 6. Operators

Candidate L03 RSCF operators:

```text
NORMALIZE_TARGET
TYPE_NODE

MAP_HML
EXPAND_H
EXPAND_M
EXPAND_L

ADD_PREMISE
ADD_EVIDENCE
LINK_DEPENDENCY
TRACE_DEPENDENCY
MARK_LOAD_BEARING

ATTACH_PROVENANCE
CHECK_SHARED_ANCESTRY
CHECK_INDEPENDENCE

ATTACH_SCOPE
ATTACH_REGIME
ATTACH_FRESHNESS

ADD_COMPETING
PRESERVE_COMPETING
PROPOSE_DISCRIMINATING_TEST

CLASSIFY_CAUSAL_STATUS

ADD_FALSIFIER
ADD_INVALIDATION_CONDITION

CLASSIFY_GAP
CALCULATE_CONFIDENCE_CEILING

INVALIDATE_NODE
INVALIDATE_DESCENDANTS
REVALIDATE_NODE

ISSUE_CONCLUSION_CLASS
PROPOSE_RSCF
```

Canonical operator names remain `UNKNOWN/GAP`.

---

## 7. Invariants

```text
RSCF-INV-001
RSCF != PROOF

RSCF-INV-002
OBSERVATION != PERCEPT

RSCF-INV-003
DERIVED != OBSERVATION

RSCF-INV-004
MODEL != VERIFIED

RSCF-INV-005
UNKNOWN/GAP != PASS

RSCF-INV-006
REPEATED DESCENDANTS OF ONE SOURCE != INDEPENDENT SUPPORT

RSCF-INV-007
LOAD-BEARING PREMISES MUST BE TRACEABLE

RSCF-INV-008
DEPENDENCY EDGES MUST NOT BE SILENTLY OMITTED WHEN MATERIAL

RSCF-INV-009
SCOPE MUST PROPAGATE TO DEPENDENT CONCLUSIONS

RSCF-INV-010
REGIME VALIDITY MUST PROPAGATE TO DEPENDENT CONCLUSIONS

RSCF-INV-011
STALE PREMISE CANNOT SUPPORT FRESH CONCLUSION WITHOUT REVALIDATION

RSCF-INV-012
STRUCTURAL SIMILARITY != CAUSATION

RSCF-INV-013
SEQUENCE != CAUSATION

RSCF-INV-014
INCOMPATIBLE ADEQUATELY SUPPORTED PERCEPTS MUST REMAIN COMPETING

RSCF-INV-015
CONFIDENCE MUST NOT EXCEED THE WEAKEST LOAD-BEARING PREMISE
UNLESS INDEPENDENT REVALIDATION EXISTS

RSCF-INV-016
FAILED PREMISE INVALIDATES ONLY ITS DEPENDENT DESCENDANTS

RSCF-INV-017
UNAFFECTED VALID BRANCHES MUST BE PRESERVED

RSCF-INV-018
MATERIAL CLAIMS REQUIRE FALSIFIERS OR EXPLICIT FALSIFIER GAP

RSCF-INV-019
CAPABILITY != AUTHORITY

RSCF-INV-020
PROPOSAL != COMMIT
```

The confidence, provenance-independence, competing-hypothesis, and selective-invalidation rules directly align with the governing RSCF model.

---

## 8. Dependencies

```yaml
upstream:
  - L01_SENSING_OBSERVATION
  - L02_ATTENTION

intra_L03:
  - L03_DEFINITION
  - L03_STATE
  - L03_VARIABLES
  - L03_OPERATORS
  - L03_INVARIANTS
  - L03_DEPENDENCIES
  - L03_HML
  - L03_MEMORY
  - L03_PROVENANCE
  - L03_FAILURE_MODES
  - L03_REPAIR
  - L03_TESTS

cross_cutting:
  - RSCF
  - HML
  - provenance_topology
  - scope_regime_governance
  - causal_governance
  - uncertainty_governance
  - control_plane
```

---

## 9. H/M/L applicability

### H — Governing percept

Represents the macro perceptual interpretation or scene-level frame.

```text
H:
  scene
  governing context
  perceptual regime
  global constraints
```

### M — Intermediate structure

Represents objects, events, multimodal groupings, or relational structures.

```text
M:
  object candidate
  event candidate
  multimodal fusion
  contextual relation
```

### L — Local evidence

Represents observation-derived features and bindings.

```text
L:
  feature
  edge
  token
  local temporal relation
  spatial relation
  binding
```

Canonical decomposition rule:

```text
expand H/M/L only when deeper decomposition can materially
alter proof sufficiency or the conclusion
```

This follows the smallest-sufficient-proof rule of the RSCF architecture.

---

## 10. Control-plane requirements

The L03 RSCF layer may:

```text
construct proof capsules
type evidence
trace dependencies
mark gaps
calculate confidence ceilings
preserve competing percepts
propose discriminating tests
propose invalidation
```

It may not independently:

```text
manufacture evidence
rewrite observations
declare provenance independent without support
remove contradictions
commit durable state
grant authority
execute external actions
override governing constraints
```

Commit requires external control-plane authorization.

---

## 11. Agents

Candidate logical roles:

```text
L03_RSCF_BUILDER_AGENT
L03_EPISTEMIC_TYPER_AGENT
L03_HML_MAPPER_AGENT
L03_DEPENDENCY_AGENT
L03_PROVENANCE_AGENT
L03_COMPETING_PERCEPT_AGENT
L03_CAUSAL_FIREWALL_AGENT
L03_FALSIFIER_AGENT
L03_CONFIDENCE_AUDITOR
L03_RSCF_VALIDATOR
```

These are architectural roles, not evidence of deployed agents.

---

## 12. Skills

Relevant capability families:

```text
RSCF modeling
source reading
claim verification
provenance hardening
H/M/L decomposition
causal hierarchy governance
scope/regime governance
memory conflict governance
constraint propagation
repair governance
control-plane governance
```

Skill availability constitutes capability, not execution or authority.

---

## 13. Workflow

```text
PERCEPT CANDIDATE
↓
NORMALIZE TARGET
↓
TYPE TARGET
↓
MAP H / M / L
↓
IDENTIFY LOAD-BEARING PREMISES
↓
ATTACH OBSERVATIONS
↓
ATTACH PROVENANCE
↓
BUILD DEPENDENCY GRAPH
↓
CHECK SHARED ANCESTRY
↓
ATTACH:
  scope
  regime
  freshness
↓
GENERATE / PRESERVE COMPETING PERCEPTS
↓
APPLY CAUSAL FIREWALL
↓
ATTACH FALSIFIERS
↓
CLASSIFY GAPS
↓
CALCULATE CONFIDENCE CEILING
↓
SELECT CHEAPEST HIGH-INFORMATION
DISCRIMINATING TEST IF REQUIRED
↓
ISSUE WEAKEST ACCURATE CONCLUSION CLASS
↓
PROPOSE RSCF
↓
CONTROL-PLANE GATE
```

---

## 14. Protocols

```text
RSCF_BUILD_REQUEST
RSCF_BUILD_RESULT

NODE_TYPE_REQUEST
NODE_TYPE_RESULT

HML_MAP_REQUEST
HML_MAP_RESULT

DEPENDENCY_LINK_REQUEST
DEPENDENCY_LINK_RESULT

PROVENANCE_CHECK_REQUEST
PROVENANCE_CHECK_RESULT

COMPETING_REGISTER
COMPETING_UPDATE

FALSIFIER_REGISTER

GAP_REGISTER
GAP_UPDATE

REVALIDATION_REQUEST
REVALIDATION_RESULT

INVALIDATION_NOTICE

RSCF_PROPOSAL
RSCF_VALIDATION_RESULT
RSCF_COMMIT_REQUEST
RSCF_COMMIT_RESULT
```

Canonical wire schemas remain `UNKNOWN/GAP`.

---

## 15. Evidence / provenance

Every material percept RSCF should preserve:

```text
observation identity
source identity
source ancestry
transformation lineage
feature lineage
relation lineage
binding lineage
attention context
memory/context contribution
dependency edges
scope
regime
freshness
measurement/observation method where relevant
competing percepts
falsifiers
uncertainty
confidence ceiling
state/version identity
```

Independence must be demonstrated rather than inferred from source count. Correlated descendants of one source cannot be counted as independent confirmation.

---

## 16. Uncertainty and confidence ceiling

```yaml
uncertainty_vector:
  evidence: null
  model: null
  scope: null
  temporal: null
  causal: null
  execution: null
  provenance_independence: null
```

Candidate governing relation:

[
Conf(C)
\leq
\min_{p\in LB(C)} Conf(p)
]

where `LB(C)` is the set of load-bearing premises for conclusion `C`, unless a weak premise has been independently revalidated.

This is an `AMOS_MODEL` representation of the RSCF confidence rule, not a universal statistical confidence equation.

---

## 17. Competing percepts

L03 SHALL NOT force premature convergence.

Example:

```yaml
target:
  percept: object_A

competing:

  - id: H1
    claim: one partially occluded object
    status: COMPETING

  - id: H2
    claim: two spatially adjacent objects
    status: COMPETING

  - id: H3
    claim: observation corruption
    status: COMPETING
```

When evidence is equal, incomparable, correlated, or insufficient, competing hypotheses remain explicit until discriminating evidence exists.

---

## 18. Gap classification

```text
CRITICAL
DECISION-RELEVANT
EXPLANATORY
COSMETIC
```

Priority:

[
CRITICAL

>

DECISION\text{-}RELEVANT

>

EXPLANATORY

>

COSMETIC
]

This is a governance ordering, not a physical equation.

Examples:

```text
CRITICAL:
missing source observation required for the percept

DECISION-RELEVANT:
unknown temporal ordering capable of changing object identity

EXPLANATORY:
unknown secondary feature that does not alter percept classification

COSMETIC:
missing human-readable label
```

---

## 19. Failure modes

```text
RFM-001 evidence laundering
RFM-002 observation/percept collapse
RFM-003 source/derivation collapse
RFM-004 correlated provenance counted as independent
RFM-005 hidden load-bearing premise
RFM-006 missing dependency edge
RFM-007 scope leakage
RFM-008 regime leakage
RFM-009 stale-premise reuse
RFM-010 causal overreach
RFM-011 premature competing-hypothesis collapse
RFM-012 missing falsifier
RFM-013 confidence inflation
RFM-014 UNKNOWN converted to PASS
RFM-015 global invalidation from local failure
RFM-016 failed dependency not propagated
RFM-017 repaired dependency not revalidated
RFM-018 provenance loss
RFM-019 version ambiguity
RFM-020 unauthorized commit
```

---

## 20. Repair / recovery

```text
DETECT INVALID RSCF NODE
↓
IDENTIFY FAILED PREMISE / EDGE
↓
QUARANTINE AFFECTED NODE
↓
TRACE DEPENDENT DESCENDANTS
↓
INVALIDATE DEPENDENTS ONLY
↓
PRESERVE UNAFFECTED BRANCHES
↓
RECOVER / REVALIDATE PREMISE
↓
REBUILD AFFECTED SUBGRAPH
↓
RECHECK:
  provenance
  scope
  regime
  freshness
  competing
  falsifiers
↓
RECALCULATE CONFIDENCE
↓
REISSUE CONCLUSION CLASS
```

A failed premise should invalidate only dependent descendants rather than trigger indiscriminate global recomputation.

---

## 21. Tests / validators

```text
TEST-RSCF-001
Two sources are descendants of one observation.
Expected:
not independent confirmation.

TEST-RSCF-002
One load-bearing premise confidence falls.
Expected:
dependent conclusion ceiling cannot remain above it
without independent revalidation.

TEST-RSCF-003
A local feature becomes invalid.
Expected:
dependent percept invalidated;
unrelated branches preserved.

TEST-RSCF-004
Two incompatible percepts have equivalent support.
Expected:
COMPETING.

TEST-RSCF-005
No evidence exists for required premise.
Expected:
UNKNOWN/GAP.

TEST-RSCF-006
Percept is valid only in regime R1 but evaluated in R2.
Expected:
scope/regime validation failure.

TEST-RSCF-007
Temporal sequence is presented as causal evidence.
Expected:
causal firewall rejection.

TEST-RSCF-008
RSCF is internally complete but contains no provenance.
Expected:
validation failure.

TEST-RSCF-009
All structural checks pass but commit authority is absent.
Expected:
PROPOSAL only.

TEST-RSCF-010
Critical gap remains unresolved.
Expected:
not PASS.
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

## 22. Falsifiers / invalidation conditions

This contract must be revised if:

```text
direct L03 canon specifies incompatible RSCF semantics
canonical epistemic classes differ
canonical H/M/L semantics differ
canonical dependency semantics differ
canonical confidence propagation differs
canonical provenance rules differ
canonical invalidation behavior differs
canonical control-plane ownership differs
or executable canonical behavior contradicts this model
```

Individual RSCFs become stale or invalid when a load-bearing premise fails, provenance is revoked, applicability changes, a regime shift occurs, freshness expires, or new discriminating evidence defeats the current percept.

---

## 23. Gap status

```yaml
gap_status:

  RSCF_definition:
    status: MODEL_DEFINED

  typed_inputs_outputs:
    status: MODEL_DEFINED

  epistemic_types:
    status: ARCHITECTURE_ALIGNED

  HML:
    status: ARCHITECTURE_ALIGNED

  dependency_model:
    status: ARCHITECTURE_ALIGNED

  competing_hypotheses:
    status: ARCHITECTURE_ALIGNED

  provenance:
    status: ARCHITECTURE_ALIGNED

  falsification:
    status: ARCHITECTURE_ALIGNED

  repair:
    status: MODEL_DEFINED

  validators:
    status: MODEL_DEFINED_UNEXECUTED

  direct_L03_RSCF_canon:
    status: CRITICAL_GAP

  canonical_schema:
    status: CRITICAL_GAP

  canonical_operator_registry:
    status: CRITICAL_GAP

  executable_runtime:
    status: CRITICAL_GAP

  runtime_validation:
    status: CRITICAL_GAP

  empirical_validation:
    status: CRITICAL_GAP
```

---

## 24. RSCF completion state

```yaml
claim_class: MODEL

claim:
  L03_PERCEPT_FORMATION can represent each material percept as a
  provenance-bound recursive structured claim whose observations,
  derivations, H/M/L structure, dependencies, applicability,
  competing percepts, falsifiers, uncertainty, and confidence
  ceiling remain explicit.

evidence:
  - AMOS RSCF architecture
  - reconstructed L03 contract family
  - AMOS H/M/L architecture
  - AMOS provenance and selective-invalidation principles

provenance:
  origin_architect: Trang Phan
  architecture_family: AMOS
  primitive: L03_PERCEPT_FORMATION
  artifact: RSCF.md
  derivation: ARCHITECTURE_ALIGNED_MODEL_SYNTHESIS

scope:
  system: AMOS_OS
  subsystem: COGNITIVE_MATRIX
  primitive: L03_PERCEPT_FORMATION
  concern: epistemic_and_proof_structure

regime:
  governed percept-formation architecture

freshness:
  revalidate_when:
    - direct L03 canon becomes available
    - RSCF canon changes
    - L01/L02 contracts change
    - L03 dependencies change
    - provenance rules change
    - executable runtime appears

dependencies:
  - L01_SENSING_OBSERVATION
  - L02_ATTENTION
  - L03_STATE
  - L03_INVARIANTS
  - L03_DEPENDENCIES
  - L03_HML
  - L03_PROVENANCE
  - L03_REPAIR
  - AMOS_RSCF
  - AMOS_CONTROL_PLANE

competing:
  - alternative percept interpretation
  - observation corruption
  - attention-selection distortion
  - stale-context distortion
  - binding error
  - regime mismatch

falsifiers:
  - incompatible direct canon
  - provenance contradiction
  - dependency contradiction
  - scope/regime failure
  - executable counterexample
  - canonical runtime contradiction

confidence_ceiling:
  value: LOW_TO_MEDIUM
  reason:
    RSCF-level AMOS conventions are structurally available,
    but direct canonical L03 RSCF semantics, executable implementation,
    executed validation, and empirical validation remain unresolved.

gap_status:
  direct_canon: CRITICAL_GAP
  executable_runtime: CRITICAL_GAP
  executed_validation: CRITICAL_GAP
  empirical_validation: CRITICAL_GAP
```

## Governing RSCF contract

> **`L03_PERCEPT_FORMATION` SHALL NOT treat a formed percept, coherent interpretation, or completed RSCF as proof of reality. Every material percept SHALL preserve its epistemic class, observation lineage, load-bearing premises, H/M/L location, dependency edges, provenance ancestry, scope, regime, freshness, competing interpretations, falsifiers, unresolved gaps, and confidence ceiling where available. Correlated descendants SHALL NOT be counted as independent confirmation; structural similarity or temporal sequence SHALL NOT independently license causation; and incompatible adequately supported percepts SHALL remain `COMPETING` until discriminating evidence exists. A failed premise SHALL selectively invalidate dependent conclusions while preserving unaffected valid branches. `UNKNOWN/GAP` SHALL remain non-passing. RSCF construction may produce a governed proposal, but neither the RSCF nor its confidence score grants authority or constitutes durable commit.**

---

[[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]|[[00_ROOT/AMOS MOC|AMOS MOC]]

---
**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[25_COGNITIVE_MATRIX/00_INDEX/COGNITIVE_MATRIX_MOC|COGNITIVE_MATRIX_MOC]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: l03_percept_formation_primitives_cognitive_matrix_rscf
node_type: note
path: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L03_PERCEPT_FORMATION/L03_PERCEPT_FORMATION_PRIMITIVES_COGNITIVE_MATRIX_RSCF.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
  - INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[25_COGNITIVE_MATRIX/01_PRIMITIVES/L03_PERCEPT_FORMATION/L03_PERCEPT_FORMATION_MOC|L03_PERCEPT_FORMATION_MOC]]
