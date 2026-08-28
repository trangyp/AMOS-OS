---
type: cognitive
source: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L02_ATTENTION
tags:
- amos
- cognitive-matrix
- l02
- attention
- readme
- rscf
- hml
- governance
- canon/cognitive-matrix
title: "L02_ATTENTION — README"
origin_architect: "Trang Phan"
status: "MODEL_SPECIFICATION / SOURCE-BOUNDED / UNVALIDATED"
epistemic_class: "MODEL"
runtime_alignment: "AMOS Full Brain OS / AMOS_CORE v4.4 lineage"
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


# L02_ATTENTION — README

**Class:** `COGNITIVE_PRIMITIVE_CONTRACT`  
**Origin architect / steward:** Trang Phan  
**Primitive:** `L02_ATTENTION`  
**Artifact:** `README.md`  
**Status:** `AMOS_MODEL / SOURCE-BOUNDED / UNVALIDATED`

> **Canon boundary:** the available L02 material supports an attention primitive concerned with allocation/budgeting of scarce reasoning or observation resources. This README organizes that semantic core into an AMOS contract. Detailed interfaces, operators, equations, agents, workflows, thresholds, and runtime behavior remain `AMOS_MODEL` unless separately grounded in direct canon or executable evidence.

---

# 0. Executive Contract

`L02_ATTENTION` governs the allocation of finite cognitive-processing resources across competing candidate targets.

Conceptually:

$$CandidateSpace_t \rightarrow AttentionSelection_t \rightarrow ResourceAllocation_t \rightarrow FocusedProcessing_t$$

subject to:

```text
objective
constraints
resource budget
dependency criticality
uncertainty
consequence
scope
regime
freshness
provenance
H/M/L position
authority boundaries
```

The primitive answers:

> **What deserves processing now, at what depth, using how much bounded resource, and when should that allocation change or stop?**

It does **not** establish that an attended object is true, important in an absolute sense, causal, independently evidenced, or authorized for execution.

---

# 1. Source / Canon References

## 1.1 Source-supported semantic core

Current source-bounded interpretation:

```text
L02_ATTENTION
=
attention allocation;
budget scarce reasoning/observation resources
```

This supports:

```text
L02 concerns attention.

Attention includes allocation.

Reasoning/observation capacity is treated as scarce.
```

It does not independently establish a complete canonical:

```text
attention equation
priority function
operator registry
threshold system
agent architecture
workflow
protocol schema
AI implementation
control-plane ownership model
```

## 1.2 AMOS lineage references

Architectural interpretation should remain compatible with, where applicable:

```text
AMOS Full Brain OS
AMOS cognition architecture
AMOS_CORE v3.0 → v4.4 lineage
RSCF
H/M/L decomposition
typed state
dependency-aware reasoning
provenance topology
scope/regime/freshness controls
competing hypotheses
selective invalidation
capability/authority separation
proposal/commit separation
```

Compatibility does not establish direct canonical derivation.

---

# 2. Definition and Scope

Within this contract:

[
Attention_t
===========

Allocate(
X_t,
B_t,
G_t,
C_t
)
]

where:

```text
X_t = candidate attention space
B_t = bounded resource envelope
G_t = governing objective
C_t = contextual/governance state
```

`L02_ATTENTION` is responsible for model-level functions such as:

```text
candidate admission
priority assessment
resource allocation
focus
sustained focus
attention shift
deferral
resumption
escalation
de-escalation
release
attention-state repair
```

### Out of scope

```text
raw environmental reality
sensor acquisition itself
truth determination by attention alone
memory persistence ownership
causal proof
final decision authority
external-action authorization
durable commit authority
```

Hard distinctions:

```text
ATTENTION != SENSING
ATTENTION != OBSERVATION
ATTENTION != MEMORY
ATTENTION != TRUTH
ATTENTION != EVIDENCE
ATTENTION != CONFIDENCE
ATTENTION != AUTHORITY
```

---

# 3. Position in the Cognitive Matrix

Minimum source-bounded relationship:

```text
L00_REALITY_ENVIRONMENT
        ↓
L01_SENSING_OBSERVATION
        ↓
candidate observations
        ↓
L02_ATTENTION
        ↓
selected / prioritized processing
```

The exact canonical downstream primitive/interface is not established by the currently resolved evidence.

Therefore:

```text
L02 downstream ownership = UNKNOWN/GAP
```

unless separately sourced.

---

# 4. Typed Inputs

```yaml
AttentionInput:

  candidates:
    type: AttentionCandidate[]

  observations:
    type: ObservationRef[]

  objective:
    type: GoalState

  resource_budget:
    type: ResourceBudget

  constraints:
    type: ConstraintSet

  uncertainty:
    type: UncertaintyVector

  dependencies:
    type: DependencyGraph

  evidence:
    type: EvidenceBundle

  provenance:
    type: ProvenanceBundle

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeRef

  freshness:
    type: FreshnessState

  hml:
    type: HMLContext

  authority:
    type: AuthorityContext
```

Candidate objects may represent:

```text
observations
claims
premises
hypotheses
contradictions
gaps
tasks
memories
documents
repository objects
tools
agents
risks
repair targets
```

This generalized candidate model is `AMOS_MODEL`.

---

# 5. Typed Outputs

```yaml
AttentionOutput:

  admitted:
    type: CandidateRef[]

  prioritized:
    type: PriorityState[]

  allocation:
    type: AttentionAllocationProposal

  active_focus:
    type: FocusState[]

  deferred:
    type: CandidateRef[]

  quarantined:
    type: CandidateRef[]

  escalation_requests:
    type: EscalationRequest[]

  unresolved_gaps:
    type: GapRef[]

  state:
    type: AttentionState

  provenance:
    type: ProvenanceBundle

  uncertainty:
    type: UncertaintyVector

  confidence_ceiling:
    type: ConfidenceBound

  status:
    type:
      - VALID
      - PARTIAL
      - BLOCKED
      - ESCALATED
      - UNKNOWN_GAP
```

The output is principally a governed allocation/proposal state.

```text
ATTENTION OUTPUT
!=
COMMIT
```

---

# 6. State Variables

```text
X_t       = candidate space
E_t       = eligible/admitted candidates
A_t       = allocation state
Foc_t     = active focus
B_t       = resource budget
G_t       = governing objective
C_t       = constraints
U_t       = uncertainty
D_t       = dependency graph
P_t       = provenance state
Fr_t      = freshness state
S_t       = scope
R_t       = regime
HML_t     = H/M/L coordinate
Q_t       = quarantined candidates
Def_t     = deferred candidates
Comp_t    = competing hypotheses
Contr_t   = contradictions
Gap_t     = unresolved gaps
Auth_t    = authority state
```

Resource budgets may be multidimensional.

```yaml
ResourceBudget:
  context: bounded_resource
  reasoning: bounded_resource
  time: bounded_resource
  retrieval: bounded_resource
  tool_calls: bounded_resource
  agent_calls: bounded_resource
  human_review: bounded_resource
```

These dimensions must not be silently treated as interchangeable units.

---

# 7. Operators

Candidate operator registry:

```text
INGEST()
NORMALIZE()

ADMIT()
QUARANTINE()

ASSESS_RELEVANCE()
ASSESS_UNCERTAINTY()
ASSESS_CONSEQUENCE()
ASSESS_DEPENDENCY_CRITICALITY()
ASSESS_INFORMATION_VALUE()
ASSESS_COST()

RANK()
COMPARE()
SELECT()

ALLOCATE()
RESERVE()

FOCUS()
SUSTAIN()
SHIFT()
RELEASE()

DEFER()
RESUME()

ESCALATE()
DEESCALATE()

CHECK_FRESHNESS()
REVALIDATE()

INVALIDATE()
REALLOCATE()

REPAIR()
ROLLBACK_PROPOSE()

EMIT_PROPOSAL()
```

These names are architectural placeholders/model operators unless directly canonized.

---

# 8. Equational Model

A generic priority relation may be represented as:

[
Priority_i
==========

F(
G_i,
U_i,
K_i,
D_i,
T_i,
V_i,
R_i,
Cost_i
)
]

where, illustratively:

```text
G_i    = goal relevance
U_i    = uncertainty relevance
K_i    = consequence
D_i    = dependency criticality
T_i    = time sensitivity
V_i    = expected information value
R_i    = risk relevance
Cost_i = resource cost
```

No canonical coefficients or aggregation law are asserted.

Resource constraint:

[
\sum_i Allocation_{i,r}
\le
Budget_r
]

for each compatible resource dimension (r).

Confidence firewall:

[
Conf(C)
\le
\min_j Conf(P_j)
]

for load-bearing premises unless independent revalidation strengthens the evidence graph.

Attention itself does not increase that ceiling.

---

# 9. Invariants

```text
L02-INV-001
Attention resources are bounded within a bounded execution context.

L02-INV-002
Allocation cannot exceed the governing resource envelope.

L02-INV-003
Attention does not establish truth.

L02-INV-004
Attention does not establish evidence.

L02-INV-005
Attention does not establish causality.

L02-INV-006
Attention does not create authority.

L02-INV-007
Salience cannot automatically equal priority.

L02-INV-008
Novelty cannot automatically equal priority.

L02-INV-009
Repetition cannot create provenance independence.

L02-INV-010
Hard constraints remain non-compensatory.

L02-INV-011
Material contradictions remain visible.

L02-INV-012
Genuine COMPETING hypotheses remain distinct.

L02-INV-013
Scope survives allocation.

L02-INV-014
Regime survives allocation.

L02-INV-015
Freshness-sensitive premises require revalidation.

L02-INV-016
Material provenance remains recoverable.

L02-INV-017
Derived confidence respects load-bearing premise ceilings.

L02-INV-018
Invalidation propagates only through actual dependencies.

L02-INV-019
H/M/L identity survives scale traversal.

L02-INV-020
UNKNOWN/GAP cannot become PASS through attention.

L02-INV-021
Resource exhaustion does not establish completion.

L02-INV-022
Proposal cannot silently become commit.
```

---

# 10. Dependencies

```yaml
dependencies:

  upstream:
    - L01_SENSING_OBSERVATION

  local_contract:
    - PURPOSE
    - DEFINITION
    - VARIABLES
    - STATE
    - OPERATORS
    - INVARIANTS
    - DEPENDENCIES
    - EQUATIONS
    - HML
    - MEMORY
    - CONTROL_PLANES
    - AGENTS
    - SKILLS
    - WORKFLOWS
    - PROTOCOLS
    - PROVENANCE
    - FAILURE_MODES
    - GAP_MATRIX
    - REPAIR
    - RSCF
    - TESTS

  governance:
    - objective_state
    - constraint_state
    - resource_state
    - provenance_state
    - scope
    - regime
    - freshness
    - authority
```

Canonical downstream dependencies remain unresolved.

---

# 11. H/M/L Applicability

## H — Governing attention

Determines which issue classes deserve system-level processing.

Examples:

```text
critical objective
systemic risk
major contradiction
regime shift
critical gap
authority conflict
```

Question:

> What can materially change the governing conclusion or system trajectory?

## M — Allocation attention

Allocates resources across:

```text
tasks
hypotheses
research branches
agents
tools
subsystems
repair paths
```

Question:

> Which path deserves resources next?

## L — Local attention

Operates on individual objects:

```text
one observation
one claim
one premise
one source
one function
one test
one contradiction
```

Question:

> Does this item deserve processing now?

Cross-scale invariant:

```text
L evidence cannot silently become H conclusion.

H narrative cannot suppress contradictory L evidence.
```

---

# 12. Control-Plane Requirements

L02 may propose:

```text
priority
allocation
focus
deferral
escalation
revalidation
repair
```

The infrastructure/control plane should own, where applicable:

```text
authority
shared resource enforcement
persistent-state mutation
external effects
cross-agent constraints
commit-time validation
durable commit
rollback authorization
```

Separation:

```text
L02_ATTENTION
=
COGNITIVE ALLOCATION

CONTROL PLANE
=
GOVERNED EFFECT AUTHORITY
```

Therefore:

```text
HIGH PRIORITY != AUTHORIZED ACTION
```

---

# 13. Agents

Candidate logical roles:

```text
L02_ATTENTION_GOVERNOR
L02_CANDIDATE_ASSESSOR
L02_PRIORITY_AGENT
L02_ALLOCATION_AGENT
L02_HML_ROUTER
L02_ESCALATION_AGENT
L02_PROVENANCE_AUDITOR
L02_ATTENTION_REPAIR_AGENT
```

These are addressable architectural roles.

```text
ADDRESSABLE AGENT != IMPLEMENTED AGENT
```

---

# 14. Skills

Potential supporting AMOS skills/capabilities include:

```text
AMOS Attention Allocation Governor
AMOS Context Budget Governor
AMOS Constraint Propagation RSCF Engine
AMOS Cross-Scale RSCF Tensor Engine
AMOS Metacognitive Confidence Auditor
AMOS Provenance Trust Firewall
AMOS Context Continuity Governor
AMOS Infrastructure Control Plane
AMOS Risk Constraint Governor
RSCF Modeler
```

Availability of a skill establishes neither invocation nor validation.

---

# 15. Workflow

Candidate lifecycle:

```text
OBSERVE
   ↓
FORM CANDIDATE SPACE
   ↓
RESOLVE OBJECTIVE
   ↓
RESOLVE RESOURCE ENVELOPE
   ↓
CHECK HARD CONSTRAINTS
   ↓
ADMIT / QUARANTINE
   ↓
ASSESS
   ↓
PRESERVE CONTRADICTIONS / COMPETING
   ↓
RANK / COMPARE
   ↓
ALLOCATE
   ↓
FOCUS
   ↓
MONITOR VALUE OF CONTINUED PROCESSING
   ↓
SHIFT / DEFER / RELEASE / ESCALATE
   ↓
REVALIDATE WHEN REQUIRED
   ↓
STOP WHEN SUFFICIENT
   ↓
EMIT GOVERNED RESULT / PROPOSAL
```

---

# 16. Protocols

Candidate protocol family:

```text
ATTENTION_CANDIDATE_SUBMIT
ATTENTION_ADMISSION_RESULT
ATTENTION_ASSESSMENT_RESULT
ATTENTION_PRIORITY_PROPOSAL
ATTENTION_ALLOCATION_PROPOSAL
ATTENTION_FOCUS_UPDATE
ATTENTION_DEFER
ATTENTION_RESUME_REQUEST
ATTENTION_ESCALATION_REQUEST
ATTENTION_FRESHNESS_CHECK
ATTENTION_INVALIDATION_NOTICE
ATTENTION_REPAIR_REQUEST
ATTENTION_ROLLBACK_PROPOSAL
ATTENTION_COMMIT_REQUEST
```

Canonical protocol names and schemas remain `UNKNOWN/GAP`.

---

# 17. Memory

Attention may consume memory but should not silently own durable memory semantics.

Possible interaction:

```text
current candidate
↓
memory relevance query
↓
bounded recall
↓
provenance/freshness validation
↓
attention reassessment
```

Memory retrieved because it is relevant remains subject to:

```text
scope
freshness
provenance
contradiction
regime
applicability
```

Hard boundary:

```text
RECALLED != TRUE

REMEMBERED != CURRENT

ATTENDED MEMORY != AUTHORITY
```

---

# 18. Evidence / Provenance

Consequential allocation should preserve sufficient lineage to answer:

```text
What candidate was prioritized?

Why?

Against which objective?

Using which evidence?

From which semantic origin?

Under which scope/regime?

At what freshness?

With which dependencies?

At which H/M/L level?

Using which resource state?

What changed the allocation?
```

Minimal provenance object:

```yaml
AttentionProvenance:

  candidate_id: string
  semantic_origin: SourceRef
  ancestry: SourceRef[]
  objective_ref: GoalRef
  evidence_refs: EvidenceRef[]
  dependency_refs: DependencyRef[]
  scope: ScopeEnvelope
  regime: RegimeRef
  freshness: FreshnessState
  hml: HMLContext
  operator_history: OperatorEvent[]
```

---

# 19. Uncertainty and Confidence Ceiling

Track uncertainty dimensions separately:

```yaml
uncertainty:
  evidence: bounded
  model: bounded
  scope: bounded
  temporal: bounded
  causal: bounded
  execution: bounded
  provenance_independence: bounded
```

Attention may reduce uncertainty by directing processing toward discriminating evidence.

It may not reduce uncertainty merely by repeated consideration.

```text
MORE THINKING
!=
NEW EVIDENCE

MORE ATTENTION
!=
HIGHER CONFIDENCE
```

Confidence remains bounded by load-bearing evidence and assumptions.

---

# 20. Failure Modes

Primary failure classes:

```text
salience capture
novelty capture
repetition capture
goal drift
priority inversion
critical-target starvation
resource overrun
premature closure
endless exploration
contradiction suppression
COMPETING collapse
scope leakage
regime leakage
stale allocation
provenance loss
confidence inflation
H/M/L collapse
dependency under-traversal
dependency over-traversal
attention thrashing
authority collapse
proposal/commit collapse
budget exhaustion treated as completion
model treated as canon
```

---

# 21. Repair / Recovery

Recovery pattern:

```text
DETECT
↓
LOCALIZE
↓
FREEZE AFFECTED ATTENTION STATE
↓
PRESERVE UNAFFECTED VALID STATE
↓
RESTORE OBJECTIVE / CONSTRAINT / PROVENANCE / FRESHNESS
↓
INVALIDATE AFFECTED DEPENDENTS
↓
RECOMPUTE SMALLEST SUFFICIENT CLOSURE
↓
REALLOCATE
↓
REVALIDATE
↓
RESUME
```

Do not repeat an unchanged failed allocation path.

```text
SAME FAILED PATH
+
SAME STATE
+
NO NEW EVIDENCE
=
NO BLIND RETRY
```

---

# 22. Tests / Validators

Required validator classes:

```text
VALIDATE_L02_IDENTITY
VALIDATE_SOURCE_BOUNDARY
VALIDATE_TYPED_IO
VALIDATE_RESOURCE_BOUNDS
VALIDATE_OBJECTIVE_ALIGNMENT
VALIDATE_HARD_CONSTRAINTS
VALIDATE_PRIORITY_SEPARATION
VALIDATE_SALIENCE_FIREWALL
VALIDATE_PROVENANCE
VALIDATE_SCOPE
VALIDATE_REGIME
VALIDATE_FRESHNESS
VALIDATE_DEPENDENCY_CLOSURE
VALIDATE_HML
VALIDATE_COMPETING_VISIBILITY
VALIDATE_CONTRADICTION_VISIBILITY
VALIDATE_CONFIDENCE_CEILING
VALIDATE_AUTHORITY_BOUNDARY
VALIDATE_PROPOSAL_COMMIT_BOUNDARY
VALIDATE_REPAIR
VALIDATE_STOP_CONDITION
```

Minimum adversarial tests:

```text
1. False but highly salient candidate.
   Expected: high salience cannot establish truth.

2. Repeated copies of one source.
   Expected: no false provenance independence.

3. Resource allocation exceeds budget.
   Expected: reject/recompute.

4. Critical unresolved dependency.
   Expected: dependent conclusion blocked/downgraded.

5. Equal viable hypotheses.
   Expected: preserve COMPETING.

6. Regime change.
   Expected: affected state requires revalidation.

7. One premise invalidated.
   Expected: selective descendant invalidation.

8. Budget exhausted before critical gap closes.
   Expected: UNKNOWN/PARTIAL, never PASS.

9. High-priority external action.
   Expected: authority still required.

10. Model operator presented as canon.
    Expected: provenance/classification failure.
```

Tests remain `UNEXECUTED` unless actual validator evidence exists.

---

# 23. Falsifiers

This README must be revised if evidence establishes that:

```text
L02 is not an attention primitive.

L02 does not concern scarce reasoning/observation resources.

Allocation belongs canonically to another primitive.

The modeled sensing/attention distinction is incompatible with canon.

H/M/L is canonically inapplicable to L02.

L02 directly owns authority or durable commit.

Canonical operators materially contradict this registry.

Canonical AI semantics materially contradict this model.

Executable runtime evidence falsifies assumed state transitions.
```

---

# 24. Gap Matrix

```yaml
gap_matrix:

  primitive_identity:
    status: SOURCE_SUPPORTED

  attention_semantics:
    status: SOURCE_SUPPORTED

  scarce_resource_semantics:
    status: SOURCE_SUPPORTED

  detailed_definition:
    status: MODEL_DEFINED

  typed_inputs_outputs:
    status: MODEL_DEFINED

  state_variables:
    status: MODEL_DEFINED

  operators:
    status: MODEL_DEFINED

  invariants:
    status: MODEL_DEFINED

  dependencies:
    status: PARTIAL_MODEL_DEFINED

  HML:
    status: MODEL_DEFINED

  control_plane_boundary:
    status: MODEL_DEFINED

  agents:
    status: MODEL_DEFINED

  skills:
    status: MODEL_DEFINED

  workflows:
    status: MODEL_DEFINED

  protocols:
    status: MODEL_DEFINED

  provenance:
    status: MODEL_DEFINED

  failure_modes:
    status: MODEL_DEFINED

  repair:
    status: MODEL_DEFINED

  tests:
    status: MODEL_DEFINED_UNEXECUTED

  canonical_equations:
    status: UNKNOWN_GAP

  canonical_thresholds:
    status: UNKNOWN_GAP

  canonical_operator_names:
    status: UNKNOWN_GAP

  canonical_downstream_interface:
    status: UNKNOWN_GAP

  canonical_control_plane_ownership:
    status: UNKNOWN_GAP

  canonical_AI_mapping:
    status: UNKNOWN_GAP

  runtime_implementation:
    status: UNKNOWN_GAP

  runtime_validation:
    status: UNKNOWN_GAP
```

---

# 25. Local Artifact Map

```text
L02_ATTENTION/
│
├── README.md
├── PURPOSE.md
├── DEFINITION.md
├── VARIABLES.md
├── STATE.md
├── OPERATORS.md
├── INVARIANTS.md
├── DEPENDENCIES.md
├── EQUATIONS.md
├── HML.md
├── MEMORY.md
├── CONTROL_PLANES.md
├── AGENTS.md
├── SKILLS.md
├── WORKFLOWS.md
├── PROTOCOLS.md
├── PROVENANCE.md
├── FAILURE_MODES.md
├── GAP_MATRIX.md
├── REPAIR.md
├── RSCF.md
└── TESTS.md
```

README role:

```text
README
=
ENTRY CONTRACT
+
ARTIFACT MAP
+
BOUNDARY REGISTRY
+
COMPLETION SUMMARY
```

Detailed definitions should remain in their specialist artifacts rather than being silently redefined here.

---

# 26. Cross-Artifact Consistency Requirements

All L02 artifacts should agree on:

```text
primitive identity
origin architect/steward
epistemic classification
input/output types
state variable meanings
operator semantics
invariant IDs
dependency direction
H/M/L semantics
authority ownership
provenance requirements
failure identifiers
gap states
RSCF classification
```

Conflict rule:

```text
CROSS-FILE CONFLICT
!=
AUTO-MERGE
```

Instead:

```text
detect
→ preserve both claims
→ resolve provenance/version
→ classify COMPETING if unresolved
→ update dependents only after resolution
```

---

# 27. RSCF Completion State

```yaml
rscf:

  id: L02_ATTENTION_README

  claim:
    L02_ATTENTION is the AMOS cognitive primitive responsible for
    governing bounded attention allocation across competing cognitive
    targets, with detailed behavior constrained by objective, resources,
    dependencies, uncertainty, provenance, scope, regime, freshness,
    H/M/L context, and authority boundaries.

  claim_class: MODEL

  source_supported_core:
    - attention allocation
    - scarcity of reasoning/observation resources

  evidence:
    - recovered L02 primitive semantics
    - AMOS architectural lineage used as bounded integration context

  provenance:
    origin_architect: Trang Phan
    architecture_family: AMOS
    subsystem: COGNITIVE_MATRIX
    primitive: L02_ATTENTION
    artifact: README.md
    derivation: SOURCE_BOUNDED_AMOS_MODEL

  scope:
    system: AMOS_OS
    subsystem: COGNITIVE_MATRIX
    primitive: L02_ATTENTION
    artifact_role: entry_contract

  regime:
    governed finite-resource cognitive allocation

  freshness:
    revalidate_when:
      - stronger direct L02 canon is recovered
      - primitive ordering changes
      - operator ownership changes
      - control-plane contracts change
      - AMOS_CORE runtime changes
      - executable validation becomes available

  dependencies:
    - L01_SENSING_OBSERVATION
    - L02_ATTENTION_PURPOSE
    - L02_ATTENTION_DEFINITION
    - L02_ATTENTION_VARIABLES
    - L02_ATTENTION_STATE
    - L02_ATTENTION_OPERATORS
    - L02_ATTENTION_INVARIANTS
    - L02_ATTENTION_DEPENDENCIES
    - L02_ATTENTION_EQUATIONS
    - L02_ATTENTION_HML
    - L02_ATTENTION_MEMORY
    - L02_ATTENTION_CONTROL_PLANES
    - L02_ATTENTION_AGENTS
    - L02_ATTENTION_SKILLS
    - L02_ATTENTION_WORKFLOWS
    - L02_ATTENTION_PROTOCOLS
    - L02_ATTENTION_PROVENANCE
    - L02_ATTENTION_FAILURE_MODES
    - L02_ATTENTION_GAP_MATRIX
    - L02_ATTENTION_REPAIR
    - L02_ATTENTION_TESTS

  competing:
    - narrow observation filter
    - resource allocator
    - full attention governor
    - hybrid cognitive/control-plane architecture

  falsifiers:
    - incompatible direct canon
    - incompatible canonical primitive ownership
    - incompatible executable runtime evidence
    - falsification of modeled H/M/L applicability
    - falsification of control-plane separation

  uncertainty:
    evidence: MEDIUM_HIGH
    model: MEDIUM
    scope: MEDIUM
    temporal: MEDIUM
    causal: LOW
    execution: HIGH
    provenance_independence: MEDIUM

  confidence_ceiling:
    source-supported confidence is limited to the recovered attention
    allocation and scarcity semantics; expanded contract remains MODEL
    until direct canon or executable evidence validates it

  gap_status:
    canonical_full_definition: CRITICAL_GAP
    canonical_equations: DECISION_RELEVANT_GAP
    canonical_operator_ownership: CRITICAL_GAP
    canonical_downstream_interface: CRITICAL_GAP
    canonical_AI_mapping: EXPLANATORY_GAP
    runtime_implementation: CRITICAL_GAP
    executed_validation: CRITICAL_GAP
```

---

# 28. Completion State

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

  gap_status:
    status: EXPLICIT_CRITICAL_GAPS_OPEN

  runtime_implementation:
    status: UNKNOWN_GAP

  executed_validation:
    status: UNKNOWN_GAP

  overall:
    status: COMPLETE_FOR_README_MODEL_SPECIFICATION_SCOPE

  conclusion_class:
    MODEL
```

---

# 29. Hard Boundaries

```text
PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

UNKNOWN/GAP != PASS
```

L02-specific boundaries:

```text
ATTENTION != SENSING

ATTENTION != OBSERVATION

ATTENTION != MEMORY

ATTENTION != TRUTH

ATTENTION != EVIDENCE

ATTENTION != CONFIDENCE

ATTENTION != CAUSATION

SALIENCE != TRUTH

SALIENCE != PRIORITY

NOVELTY != VALIDITY

REPETITION != INDEPENDENT CONFIRMATION

PRIORITY != AUTHORITY

RESOURCE AVAILABILITY != AUTHORITY

BUDGET EXHAUSTION != COMPLETION

LOCAL FOCUS != GLOBAL IMPORTANCE

AMOS L02 ATTENTION != TRANSFORMER SELF-ATTENTION

MODEL CONTRACT != CANONICAL CONTRACT

DOCUMENTED CONTRACT != IMPLEMENTED CONTRACT
```

---

# 30. References

```text
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README

L01_SENSING_OBSERVATION_PRIMITIVES_COGNITIVE_MATRIX_README

Cosmo_Brain_BRIDGE_INDEX
Cosmo_Brain_BRIDGE_INDEX
Cosmo_Brain_BRIDGE_INDEX
Cosmo_Brain_BRIDGE_INDEX
Cosmo_Brain_BRIDGE_INDEX
Cosmo_Brain_BRIDGE_INDEX
Cosmo_Brain_BRIDGE_INDEX
Cosmo_Brain_BRIDGE_INDEX
Cosmo_Brain_BRIDGE_INDEX
```

---

# 31. Governing README Contract

> **`L02_ATTENTION` is the AMOS cognitive primitive for bounded allocation of scarce reasoning and observation resources. It converts a candidate cognitive field into a governed focus/allocation state while preserving objectives, hard constraints, dependency structure, provenance, scope, regime, freshness, H/M/L identity, uncertainty, and authority boundaries. Attention may determine what receives processing, but it cannot by itself establish truth, evidence, causation, confidence, authority, implementation, validation, or commit eligibility.**

---

# 32. Canon Boundary

```text
SOURCE-SUPPORTED:

L02_ATTENTION concerns attention allocation.

Reasoning/observation resources are treated as scarce.


AMOS-FRAMEWORK-ALIGNED:

RSCF

H/M/L

typed state

dependency-aware reasoning

scope/regime/freshness preservation

provenance preservation

competing hypotheses

selective invalidation

confidence ceilings

capability/authority separation

proposal/commit separation


AMOS_MODEL:

expanded L02 contract

typed IO

state variables

operator registry

priority equations

H/M/L attention mapping

control-plane division

agent roles

skill mappings

workflow

protocol family

memory interaction

failure taxonomy

repair strategy

test suite


UNKNOWN/GAP:

complete canonical L02 definition

canonical equations

canonical priority function

canonical thresholds

canonical resource units

canonical operator names

canonical downstream interface

canonical control-plane ownership

canonical AI mapping

runtime implementation

executed validation
```

Therefore:

```text
CONCLUSION CLASS:
MODEL

NOT:
VERIFIED COMPLETE L02 CANON

NOT:
PROOF OF IMPLEMENTATION

NOT:
PROOF OF RUNTIME ENFORCEMENT

NOT:
AUTHORIZATION TO COMMIT
```

```text
```

---

00_ROOT_MOC|AMOS MOC

---
**Related:** [[00_HOME]] · [[COGNITIVE_MATRIX_MOC]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: l02_attention_primitives_cognitive_matrix_readme
node_type: note
path: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L02_ATTENTION/L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[L02_ATTENTION_MOC]]
