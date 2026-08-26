---
tags: ['cognitive_matrix', 'primitives', 'l02_attention', 'note']
---

# L02_ATTENTION — State

**Class:** `COGNITIVE_PRIMITIVE_PLACEHOLDER`
**Origin architect / steward:** Trang Phan
**Status:** `MODEL-DEFINED / UNVALIDATED`
**Artifact:** `L02_ATTENTION/STATE.md`

## Purpose

Define the AMOS state contract for `L02_ATTENTION`.

`L02_ATTENTION` represents the governed state required to allocate finite cognitive, observational, retrieval, reasoning, and execution attention among competing candidate targets.

The state contract must preserve the distinction between:

```text
OBSERVED != ATTENDED
ATTENDED != IMPORTANT
SALIENT != TRUE
PRIORITIZED != VALIDATED
SELECTED != AUTHORIZED
AUTHORIZED != EXECUTED
EXECUTED != COMMITTED
```

Attention is therefore modeled as a **bounded allocation and routing state**, not as evidence that the selected object is true, important in reality, causally relevant, or authorized for action.

---

## Source / canon references

### Primary AMOS corpus references

Candidate source lineage for this contract includes:

```text
AMOS_COGNITION.json
AMOS_FULL_BRAIN_OS.json
AMOS_SUPER_MIND_OS.json
AMOS_HUMAN_INTELLIGENCE_SUPER_ENGINE.json
amos_unified_master_combined_max_detail.json
KHUNG_TRANG_FULL_MAX_DETAIL_ARCHITECTURE_EQUATIONS.json
trang_amos_reality_architecture_master_max_detail.json
AMOS_CORE_ALL_VERSIONS_EXHAUSTIVE_MASTER_UPDATED.json
AMOS_CORE_ALL_VERSIONS_FRACTAL_KNOWLEDGE_NETWORK.json
amos_core_v4_4_extracted.py
```

### Related AMOS architecture references

Relevant architectural families include:

```text
AMOS attention allocation
AMOS cognition
AMOS H/M/L decomposition
AMOS RSCF
AMOS provenance topology
AMOS constraint propagation
AMOS context budgeting
AMOS control-plane governance
AMOS risk/constraint governance
AMOS repair/recovery
AMOS epistemic classification
```

### Canon boundary

No direct canonical `L02_ATTENTION/STATE.md` implementation has been established by the evidence currently bound to this artifact.

Therefore:

```text
L02 primitive existence/role        = SOURCE/CORPUS-SUPPORTED
detailed state schema below         = AMOS_MODEL
runtime implementation              = UNKNOWN/GAP
empirical cognitive equivalence     = UNKNOWN/GAP
```

The equations and state-machine definitions below must not be represented as established neuroscience or universally validated cognition models.

---

# 1. Definition and scope

## 1.1 Definition

The L02 attention state is the typed representation of:

1. what objects are currently eligible for attention;
2. which objects are receiving attention;
3. how much attention each receives;
4. why allocation occurred;
5. which constraints bound allocation;
6. what evidence supports the allocation;
7. how allocation changes through time;
8. what unresolved alternatives remain;
9. whether attention may progress toward reasoning or action;
10. how attention state can be repaired when corrupted.

Conceptually:

[
A_t =
\mathcal{A}
(
O_t,
G_t,
S_t,
U_t,
R_t,
C_t,
B_t,
P_t
)
]

where:

```text
A_t = attention state at time t
O_t = available observations
G_t = active goals/objectives
S_t = salience signals
U_t = uncertainty state
R_t = risk/consequence state
C_t = constraints
B_t = available attention budget
P_t = provenance/context state
```

This equation is an `AMOS_MODEL`, not an empirical cognitive law.

---

# 2. Scope

`STATE.md` owns the representation and lifecycle of L02 attention state.

It covers:

```text
candidate attention targets
active targets
attention weights
priority states
allocation budgets
selection reasons
goal relevance
salience
novelty
uncertainty
risk/consequence
time sensitivity
dependency criticality
provenance state
freshness
scope/regime
conflicts
attention transitions
attention history
repair markers
validation state
```

It does not own:

```text
raw sensing acquisition
truth determination
causal proof
domain-specific inference
long-term memory truth
external action authorization
irreversible commit
```

---

# 3. Typed inputs / outputs

## 3.1 Input contract

```yaml
AttentionStateInput:
  observations:
    type: ObservationRef[]
    required: true

  objective:
    type: ObjectiveRef | null

  candidate_targets:
    type: AttentionTarget[]

  active_constraints:
    type: ConstraintSet

  attention_budget:
    type: AttentionBudget

  current_rscf:
    type: RSCFRef[]

  provenance_context:
    type: ProvenanceContext

  uncertainty:
    type: UncertaintyVector

  risk_context:
    type: RiskState

  temporal_context:
    type: TemporalContext

  regime:
    type: RegimeRef | null

  prior_attention_state:
    type: AttentionState | null
```

## 3.2 Output contract

```yaml
AttentionStateOutput:
  state_id: AttentionStateID
  epoch: AttentionEpoch

  candidates:
    type: AttentionCandidate[]

  active_targets:
    type: AttentionTargetRef[]

  allocation:
    type: AttentionAllocation[]

  residual_budget:
    type: AttentionBudget

  deferred_targets:
    type: AttentionTargetRef[]

  rejected_targets:
    type: AttentionTargetRef[]

  unresolved_targets:
    type: AttentionTargetRef[]

  escalation_targets:
    type: AttentionTargetRef[]

  provenance:
    type: ProvenanceRef[]

  dependencies:
    type: DependencyRef[]

  transition:
    type: AttentionTransition

  validation_state:
    enum:
      - UNVALIDATED
      - CONDITIONALLY_VALID
      - VALIDATED_FOR_SCOPE
      - INVALID
      - STALE
      - QUARANTINED

  disposition:
    enum:
      - CONTINUE
      - DEEPEN
      - SWITCH
      - DEFER
      - ESCALATE
      - STOP
      - REPAIR
      - UNKNOWN
```

---

# 4. Core state object

```yaml
AttentionState:
  identity:
    state_id: null
    parent_state_id: null
    epoch: null
    created_at: null

  scope:
    system: AMOS_OS
    layer: L02_ATTENTION
    environment: null
    regime: null
    observer: null

  objective:
    primary: null
    secondary: []
    constraints: []

  candidates: []

  allocation:
    total_budget: null
    committed_budget: null
    available_budget: null
    reserve_budget: null

  active:
    targets: []
    focus_target: null

  epistemic:
    evidence_uncertainty: null
    model_uncertainty: null
    scope_uncertainty: null
    temporal_uncertainty: null
    causal_uncertainty: null
    execution_uncertainty: null
    provenance_uncertainty: null

  provenance:
    observation_refs: []
    source_refs: []
    ancestry_refs: []

  governance:
    authority_state: null
    action_eligible: false
    commit_eligible: false

  lifecycle:
    state: INITIALIZED
    transition_reason: null
    previous_state: null

  validation:
    validators: []
    status: UNVALIDATED
    failures: []

  repair:
    required: false
    invalidated_fields: []
    recovery_point: null
```

---

# 5. State variables

Core variables:

```text
A_t       = complete attention state
C_t       = candidate target set
F_t       = active focus set
a_i,t     = attention allocation to target i
B_t       = total attention budget
B^r_t     = reserve attention budget
B^u_t     = unallocated budget

G_t       = active objective state
S_i,t     = salience of target i
N_i,t     = novelty of target i
U_i,t     = uncertainty associated with target i
K_i,t     = dependency criticality
R_i,t     = risk/consequence weight
T_i,t     = temporal urgency
E_i,t     = expected decision relevance

P_i,t     = provenance state
Q_i,t     = evidence quality
Fr_i,t    = freshness state
Reg_i,t   = regime compatibility

Auth_i,t  = authority state
Val_i,t   = validation state
Conf_i,t  = confidence ceiling

D_t       = deferred targets
X_t       = rejected targets
Esc_t     = escalation targets

Epoch_t   = attention-state epoch
```

---

# 6. Candidate attention target

```yaml
AttentionTarget:
  id: TargetID

  type:
    enum:
      - OBSERVATION
      - CLAIM
      - GAP
      - CONTRADICTION
      - HYPOTHESIS
      - OBJECTIVE
      - RISK
      - CONSTRAINT
      - DEPENDENCY
      - ACTION_PROPOSAL
      - MEMORY
      - TOOL_RESULT
      - SKILL_RESULT
      - EXTERNAL_EVENT
      - UNKNOWN

  source_ref: null
  objective_relevance: null
  salience: null
  novelty: null
  uncertainty: null
  consequence: null
  time_sensitivity: null
  dependency_criticality: null

  provenance:
    refs: []
    independence_state: UNKNOWN

  scope:
    environment: null
    regime: null
    temporal_validity: null

  state:
    enum:
      - CANDIDATE
      - ELIGIBLE
      - ACTIVE
      - DEFERRED
      - REJECTED
      - QUARANTINED
      - RESOLVED
      - STALE
```

---

# 7. Operators

Candidate state operators:

```text
INIT_ATTENTION_STATE()
REGISTER_TARGET()
REMOVE_TARGET()

ASSESS_RELEVANCE()
ASSESS_SALIENCE()
ASSESS_NOVELTY()
ASSESS_UNCERTAINTY()
ASSESS_RISK()
ASSESS_TIME_SENSITIVITY()
ASSESS_DEPENDENCY_CRITICALITY()

CHECK_PROVENANCE()
CHECK_FRESHNESS()
CHECK_SCOPE()
CHECK_REGIME()
CHECK_CONSTRAINTS()

ALLOCATE_ATTENTION()
REALLOCATE_ATTENTION()
FOCUS()
DEFOCUS()
DEFER()
REJECT()
QUARANTINE()
ESCALATE()

DEEPEN()
BROADEN()
SWITCH_TARGET()

CONSUME_BUDGET()
RESERVE_BUDGET()
RELEASE_BUDGET()

UPDATE_STATE()
VALIDATE_STATE()
INVALIDATE_STATE()

SNAPSHOT()
ROLLBACK()
REPAIR()
```

These operators remain `AMOS_MODEL` unless directly bound to canonical implementation.

---

# 8. State-transition model

Candidate lifecycle:

```text
UNINITIALIZED
      ↓
INITIALIZED
      ↓
CANDIDATES_REGISTERED
      ↓
ELIGIBILITY_EVALUATED
      ↓
ALLOCATED
      ↓
ACTIVE
   ↙   ↓    ↘
DEFER  DEEPEN  SWITCH
   \     |      /
    \    |     /
     REASSESS
        ↓
   RESOLVED / ESCALATED
        ↓
      CLOSED
```

Exceptional transitions:

```text
ANY STATE
   ↓
INVALID
   ↓
QUARANTINED
   ↓
REPAIRING
   ↓
REVALIDATED
   ↓
nearest valid predecessor
```

---

# 9. Allocation model

A candidate priority representation may be expressed as:

[
\pi_{i,t}
=========

f(
G_{i,t},
S_{i,t},
N_{i,t},
U_{i,t},
R_{i,t},
T_{i,t},
K_{i,t},
E_{i,t}
)
]

subject to:

[
\sum_i a_{i,t} \leq B_t
]

and:

[
a_{i,t} \geq 0
]

with reserve constraint:

[
\sum_i a_{i,t} \leq B_t - B^r_t
]

when reserve attention is required.

These equations describe a candidate AMOS control model only.

They do **not** assert that biological or machine attention universally follows this equation.

---

# 10. Invariants

```text
L02-STATE-INV-001
Σ allocated_attention <= available_attention_budget

L02-STATE-INV-002
attention_allocation >= 0

L02-STATE-INV-003
ATTENDED != TRUE

L02-STATE-INV-004
SALIENT != IMPORTANT

L02-STATE-INV-005
IMPORTANT != VALIDATED

L02-STATE-INV-006
PRIORITY != EVIDENCE_STRENGTH

L02-STATE-INV-007
UNCERTAINTY may increase attention demand but cannot itself prove a claim.

L02-STATE-INV-008
High consequence may increase validation depth but cannot establish truth.

L02-STATE-INV-009
Every active target must remain traceable to its source or explicit synthetic origin.

L02-STATE-INV-010
Attention cannot manufacture provenance independence.

L02-STATE-INV-011
Multiple descendants of one source cannot be counted as independent evidence.

L02-STATE-INV-012
State transitions must preserve unresolved contradictions.

L02-STATE-INV-013
COMPETING hypotheses cannot silently collapse into one conclusion.

L02-STATE-INV-014
Stale evidence must not retain current-state status without revalidation.

L02-STATE-INV-015
Scope/regime changes require applicability revalidation.

L02-STATE-INV-016
CAPABILITY != AUTHORITY.

L02-STATE-INV-017
ATTENTION SELECTION != ACTION AUTHORIZATION.

L02-STATE-INV-018
PROPOSAL != COMMIT.

L02-STATE-INV-019
UNKNOWN/GAP != PASS.

L02-STATE-INV-020
Failed state validation cannot be repaired by relabeling the state.
```

---

# 11. Dependencies

Primary upstream dependency:

```text
L00_REALITY_ENVIRONMENT
          ↓
L01_SENSING_OBSERVATION
          ↓
L02_ATTENTION
```

L02 requires addressable observation state before meaningful attention allocation can occur.

Candidate downstream consumers include:

```text
perception/integration
working context
memory retrieval
reasoning
hypothesis evaluation
planning
tool routing
Skill routing
decision support
action proposals
```

Internal sibling dependencies:

```text
L02/DEFINITION.md
L02/PURPOSE.md
L02/VARIABLES.md
L02/OPERATORS.md
L02/INVARIANTS.md
L02/HML.md
L02/CONTROL_PLANES.md
L02/AGENTS.md
L02/SKILLS.md
L02/WORKFLOWS.md
L02/PROTOCOLS.md
L02/PROVENANCE.md
L02/FAILURE_MODES.md
L02/REPAIR.md
L02/TESTS.md
L02/RSCF.md
```

---

# 12. H/M/L applicability

## H — governing attention state

H-level state answers:

```text
What deserves system-level attention?
Which objectives dominate?
Which risks can alter the overall decision?
Which contradictions threaten the governing conclusion?
How much total attention budget exists?
```

Representative state:

```yaml
H_AttentionState:
  governing_objective: null
  major_risks: []
  major_gaps: []
  competing_hypotheses: []
  global_budget: null
  escalation_state: null
```

## M — subsystem attention state

M-level state answers:

```text
Which subsystem deserves deeper analysis?
Which dependency is load-bearing?
Which evidence family requires validation?
Which competing branch can alter the outcome?
```

## L — local attention state

L-level state answers:

```text
Which observation?
Which claim?
Which variable?
Which tool output?
Which line/file?
Which test?
Which discriminating evidence?
```

Cross-scale invariant:

```text
H priority != M priority != L priority
```

unless an explicit mapping establishes equivalence.

---

# 13. Control-plane requirements

The control plane should own or enforce:

```text
state identity
epoch/version
resource budgets
authority boundaries
scope/regime validity
provenance requirements
freshness
constraint enforcement
state transition validity
effect eligibility
commit eligibility
rollback/recovery
audit history
```

L02 may recommend allocation.

L02 must not independently grant authority merely because a target has high priority.

Required separation:

```text
COGNITIVE PRIORITY
        ↓
ATTENTION STATE
        ↓
PROPOSAL
        ↓
CONTROL-PLANE CHECK
        ↓
AUTHORIZED EFFECT
```

---

# 14. Agents

Candidate architectural roles:

```text
L02_ATTENTION_ALLOCATOR
L02_PRIORITY_EVALUATOR
L02_BUDGET_MONITOR
L02_CONFLICT_MONITOR
L02_ATTENTION_STATE_AUDITOR
L02_REFOCUS_AGENT
L02_ATTENTION_REPAIR_AGENT
```

These names describe possible responsibilities.

They do not establish implemented autonomous agents.

---

# 15. Skills

Candidate supporting Skills:

```text
AMOS Attention Allocation Governor
AMOS Context Budget Governor RSCF
AMOS Constraint Propagation RSCF Engine
RSCF Modeler
AMOS Claim Verifier
AMOS Provenance Trust Firewall
AMOS Metacognitive Confidence Auditor
AMOS Risk Constraint Governor
AMOS Cognitive Process Orchestrator
AMOS Repair Priority Governor
```

Skill availability does not imply invocation permission.

---

# 16. Workflows

Primary attention-state workflow:

```text
RECEIVE OBSERVATIONS
        ↓
REGISTER CANDIDATES
        ↓
BIND OBJECTIVE
        ↓
ASSESS CONSTRAINTS
        ↓
ASSESS DECISION RELEVANCE
        ↓
ASSESS UNCERTAINTY / RISK / URGENCY
        ↓
CHECK PROVENANCE / FRESHNESS / REGIME
        ↓
ALLOCATE BUDGET
        ↓
ACTIVATE TARGET(S)
        ↓
MONITOR STATE
        ↓
REASSESS
        ↓
CONTINUE / DEEPEN / SWITCH / DEFER / STOP
```

---

# 17. Protocols

Candidate state protocols:

```text
ATTENTION_STATE_INIT
ATTENTION_TARGET_REGISTER
ATTENTION_TARGET_UPDATE
ATTENTION_ELIGIBILITY_CHECK
ATTENTION_ALLOCATION_REQUEST
ATTENTION_ALLOCATION_RESULT
ATTENTION_BUDGET_RESERVE
ATTENTION_BUDGET_RELEASE
ATTENTION_FOCUS_CHANGE
ATTENTION_DEFER
ATTENTION_ESCALATE
ATTENTION_STATE_SNAPSHOT
ATTENTION_STATE_INVALIDATE
ATTENTION_STATE_REPAIR
ATTENTION_STATE_REVALIDATE
ATTENTION_STATE_CLOSE
```

Exact canonical protocol identifiers remain `UNKNOWN/GAP`.

---

# 18. Evidence / provenance

Every consequential state should preserve:

```yaml
AttentionStateProvenance:
  state_id: null
  epoch: null

  origin:
    primitive: L02_ATTENTION
    architect: Trang Phan

  input_refs: []
  observation_refs: []
  source_refs: []

  ancestry:
    parent_state: null
    prior_epochs: []

  transformations: []

  validators: []

  environment:
    scope: null
    regime: null

  timestamps:
    created: null
    updated: null

  authority_refs: []

  invalidation_refs: []
```

Derived priority must preserve ancestry to the observations and rules that produced it.

---

# 19. Uncertainty vector

Attention state should distinguish:

```yaml
AttentionUncertainty:
  evidence: null
  model: null
  scope: null
  temporal: null
  causal: null
  execution: null
  provenance_independence: null
```

Do not compress these automatically into a single confidence number when the distinction can change the decision.

---

# 20. Confidence ceiling

For a derived attention-state conclusion:

[
Conf(A_t)
\leq
\min(
Conf(P_1),
Conf(P_2),
...,
Conf(P_n)
)
]

for load-bearing premises unless independently revalidated evidence raises the applicable bound.

High confidence that something deserves attention does **not** imply high confidence that the underlying claim is true.

Example:

```text
confidence(target_needs_investigation) = HIGH

while

confidence(target_claim_is_true) = LOW
```

This distinction is mandatory.

---

# 21. Failure modes

```text
FM-L02-ST-001 Attention starvation
Important eligible target receives no usable allocation.

FM-L02-ST-002 Attention monopoly
One target consumes disproportionate budget without justification.

FM-L02-ST-003 Salience capture
Salience overrides evidence/decision relevance.

FM-L02-ST-004 Novelty capture
Novel information is prioritized merely because it is new.

FM-L02-ST-005 Threat capture
Risk signal consumes attention beyond justified consequence.

FM-L02-ST-006 Goal drift
Allocation no longer corresponds to the governing objective.

FM-L02-ST-007 Stale attention
Target remains active after freshness conditions fail.

FM-L02-ST-008 Scope leakage
Priority derived in one scope is reused in another.

FM-L02-ST-009 Regime leakage
Attention state survives an invalidating regime shift.

FM-L02-ST-010 Provenance collapse
Allocation loses traceability to supporting inputs.

FM-L02-ST-011 Correlated evidence amplification
Duplicate ancestry falsely increases priority.

FM-L02-ST-012 Contradiction suppression
Conflicting evidence is removed from active consideration.

FM-L02-ST-013 Premature convergence
COMPETING hypotheses are collapsed before discrimination.

FM-L02-ST-014 Budget exhaustion
No reserve remains for unexpected high-value evidence.

FM-L02-ST-015 Thrashing
Focus switches repeatedly without information gain.

FM-L02-ST-016 Frozen focus
Attention cannot move despite decisive new evidence.

FM-L02-ST-017 Authority leakage
Priority is treated as permission to act.

FM-L02-ST-018 State corruption
Current state cannot be reconciled with its transition history.

FM-L02-ST-019 Hidden invalidation
A load-bearing premise fails without dependent attention state being updated.

FM-L02-ST-020 UNKNOWN treated as resolved
Missing information silently becomes a passing state.
```

---

# 22. Repair / recovery

Repair principle:

> Invalidate the smallest affected state region and preserve unaffected attention state.

Recovery sequence:

```text
DETECT
  ↓
FREEZE AFFECTED TRANSITION
  ↓
IDENTIFY EARLIEST INVALID STATE
  ↓
TRACE DEPENDENTS
  ↓
INVALIDATE DEPENDENTS ONLY
  ↓
RESTORE LAST VALID SNAPSHOT
  ↓
REFRESH FAILED PREMISES
  ↓
REALLOCATE ATTENTION
  ↓
REVALIDATE
  ↓
RESUME
```

Candidate repair operators:

```text
FREEZE_STATE()
TRACE_STATE_ANCESTRY()
IDENTIFY_INVALID_EDGE()
SELECTIVE_INVALIDATE()
RESTORE_SNAPSHOT()
REFRESH_INPUT()
REALLOCATE()
REVALIDATE()
RESUME()
```

Global reset should be a last resort.

---

# 23. Tests / validators

```text
TEST-L02-ST-001 Budget conservation
Given B=100, allocations total 110.
Expected: INVALID.

TEST-L02-ST-002 Negative allocation
Any allocation < 0.
Expected: INVALID.

TEST-L02-ST-003 Salience-truth firewall
Highly salient unsupported claim.
Expected: may receive investigation attention but cannot become VERIFIED.

TEST-L02-ST-004 Provenance preservation
Remove ancestry from active target.
Expected: quarantine or invalid state.

TEST-L02-ST-005 Regime shift
Change governing regime.
Expected: affected priorities revalidated.

TEST-L02-ST-006 Freshness expiry
Expire load-bearing observation.
Expected: dependent state becomes STALE/INVALID pending refresh.

TEST-L02-ST-007 Competing hypotheses
Two unresolved alternatives remain materially viable.
Expected: COMPETING preserved.

TEST-L02-ST-008 Authority firewall
High-priority irreversible action lacks authority.
Expected: no commit eligibility.

TEST-L02-ST-009 Selective invalidation
Invalidate one target premise.
Expected: unrelated attention branches remain valid.

TEST-L02-ST-010 State replay
Replay same valid state transition inputs.
Expected: structurally equivalent state result where deterministic controls apply.

TEST-L02-ST-011 Attention thrashing
Repeated switches yield no information gain.
Expected: detect and trigger reassessment.

TEST-L02-ST-012 Unknown handling
Required target metadata absent.
Expected: UNKNOWN/GAP, not PASS.
```

---

# 24. State validators

Candidate validator set:

```yaml
validators:
  - AttentionBudgetValidator
  - AttentionTypeValidator
  - AttentionProvenanceValidator
  - AttentionFreshnessValidator
  - AttentionScopeValidator
  - AttentionRegimeValidator
  - AttentionConstraintValidator
  - AttentionTransitionValidator
  - AttentionAuthorityBoundaryValidator
  - AttentionContradictionValidator
  - AttentionDependencyValidator
  - AttentionRepairValidator
```

These are architectural definitions, not evidence that executable validators currently exist.

---

# 25. Falsifiers

This state contract should be revised or rejected if direct canon establishes that:

* `L02_ATTENTION` does not own attention-state representation;
* attention is not modeled as finite/budgeted in the relevant AMOS architecture;
* canonical variables materially conflict with this schema;
* H/M/L allocation is defined differently;
* state ownership belongs to another layer;
* canonical control-plane boundaries contradict the proposed separation;
* direct implementation demonstrates a materially different transition model;
* runtime tests falsify the stated invariants.

A falsifier does not automatically invalidate the entire primitive.

Selective invalidation applies.

---

# 26. Gap status

```yaml
gap_status:

  primitive_identity:
    status: SOURCE_SUPPORTED

  attention_allocation_role:
    status: SOURCE_SUPPORTED

  finite_resource_interpretation:
    status: SOURCE_SUPPORTED

  state_contract:
    status: MODEL_DEFINED

  typed_state_schema:
    status: MODEL_DEFINED

  state_variables:
    status: MODEL_DEFINED

  state_transition_model:
    status: MODEL_DEFINED

  allocation_equations:
    status: MODEL_DEFINED

  HML_state_mapping:
    status: MODEL_DEFINED

  provenance_requirements:
    status: MODEL_DEFINED

  repair_model:
    status: MODEL_DEFINED

  control_plane_boundary:
    status: MODEL_DEFINED

  canonical_STATE_md:
    status: UNKNOWN_GAP

  canonical_variable_names:
    status: UNKNOWN_GAP

  canonical_state_machine:
    status: UNKNOWN_GAP

  canonical_equations:
    status: UNKNOWN_GAP

  executable_state_store:
    status: UNKNOWN_GAP

  runtime_epoch_enforcement:
    status: UNKNOWN_GAP

  runtime_budget_enforcement:
    status: UNKNOWN_GAP

  executed_validators:
    status: UNKNOWN_GAP

  empirical_validation:
    status: UNKNOWN_GAP
```

---

# 27. Minimum implementation contract

An implementation claiming support for `L02_ATTENTION/STATE` should minimally demonstrate:

```text
[ ] typed attention targets
[ ] explicit attention budget
[ ] active/deferred/rejected target states
[ ] provenance references
[ ] objective binding
[ ] uncertainty representation
[ ] scope/regime representation
[ ] freshness handling
[ ] state transition history
[ ] selective invalidation
[ ] contradiction preservation
[ ] authority separation
[ ] repair/recovery path
[ ] validator execution
[ ] falsifier tests
```

Until these are demonstrated:

```text
ADDRESSABLE != IMPLEMENTED
```

---

# 28. Promotion criteria

Promotion beyond `MODEL-DEFINED / UNVALIDATED` requires at minimum:

```text
1. direct canonical source binding;
2. exact state-variable reconciliation;
3. dependency reconciliation;
4. invariant reconciliation;
5. executable schema or implementation;
6. validator execution;
7. negative/adversarial tests;
8. provenance verification;
9. authority-boundary verification;
10. repair/recovery validation.
```

Possible promotion sequence:

```text
PLACEHOLDER
→ MODEL_DEFINED
→ SOURCE_ALIGNED
→ IMPLEMENTED
→ TESTED
→ VALIDATED_FOR_SCOPE
```

No state may be skipped merely because the architecture is addressable.

---

# 29. RSCF completion state

```yaml
claim_class: MODEL

claim:
  id: L02_ATTENTION_STATE_CONTRACT
  statement: >
    L02_ATTENTION requires an explicit typed state for governing finite
    attention allocation across candidate targets while preserving objective,
    provenance, uncertainty, scope, regime, budget, contradiction, authority,
    and recovery boundaries.

evidence:
  - AMOS corpus references identifying attention/cognition architecture
  - AMOS RSCF and H/M/L architectural conventions

provenance:
  origin_architect: Trang Phan
  architecture_family: AMOS
  layer: L02_ATTENTION
  artifact: STATE.md
  derivation_class: AMOS_MODEL

scope:
  system: AMOS_OS
  subsystem: COGNITIVE_MATRIX
  primitive: L02_ATTENTION
  concern: ATTENTION_STATE

regime:
  type: governed_finite_resource_attention
  empirical_status: UNVALIDATED

freshness:
  status: CURRENT_MODEL
  revalidate_on:
    - direct STATE canon recovery
    - L02 canon update
    - variable registry update
    - control-plane update
    - executable runtime evidence
    - validator evidence

dependencies:
  - L00_REALITY_ENVIRONMENT
  - L01_SENSING_OBSERVATION
  - L02_ATTENTION_DEFINITION
  - L02_ATTENTION_PURPOSE
  - L02_ATTENTION_VARIABLES
  - L02_ATTENTION_OPERATORS
  - L02_ATTENTION_INVARIANTS
  - L02_ATTENTION_HML
  - L02_ATTENTION_CONTROL_PLANES
  - L02_ATTENTION_PROVENANCE
  - L02_ATTENTION_RSCF

competing:
  - id: C1
    hypothesis: L02 owns attention state directly
    status: OPEN

  - id: C2
    hypothesis: a shared cognition layer owns state while L02 only supplies allocation functions
    status: OPEN

  - id: C3
    hypothesis: control-plane infrastructure owns authoritative attention state
    status: OPEN

  - id: C4
    hypothesis: L02 owns cognitive state while infrastructure owns authoritative execution state
    status: OPEN

falsifiers:
  - direct incompatible canon
  - incompatible canonical variable registry
  - incompatible state ownership specification
  - incompatible runtime implementation
  - executed tests violating modeled invariants

confidence_ceiling:
  class: MODEL
  numeric_max: null
  reason: >
    The detailed STATE contract has not yet been bound to a directly
    validated canonical L02 STATE artifact or executed runtime implementation.
```

---

# 30. Hard boundaries

```text
PLACEHOLDER != IMPLEMENTED
ADDRESSABLE != VALIDATED
CAPABILITY != AUTHORITY
PROPOSAL != COMMIT
UNKNOWN/GAP != PASS

OBSERVED != ATTENDED
ATTENDED != TRUE
SALIENT != TRUE
SALIENT != IMPORTANT
PRIORITY != EVIDENCE
PRIORITY != CONFIDENCE
PRIORITY != AUTHORITY

STATE_DEFINED != STATE_IMPLEMENTED
STATE_IMPLEMENTED != STATE_VALIDATED

ALLOCATED != EXECUTED
EXECUTED != COMMITTED

MULTIPLE SIGNALS != INDEPENDENT EVIDENCE
CORRELATED PROVENANCE != CONFIRMATION

MODEL EQUATION != EMPIRICAL LAW
COGNITIVE MODEL != NEUROSCIENTIFIC PROOF

STALE != CURRENT
OUT_OF_SCOPE != APPLICABLE
REGIME_SHIFT != CONTINUITY

COMPETING != RESOLVED
UNKNOWN != FALSE
UNKNOWN/GAP != PASS
```

## Final status

```yaml
artifact: L02_ATTENTION/STATE.md
status: MODEL_DEFINED_UNVALIDATED
claim_class: MODEL
origin_architect: Trang Phan
canonical_detail_recovered: false
implementation_verified: false
tests_executed: false
empirical_validation: false
promotion_allowed: false
primary_gap: DIRECT_CANON_AND_RUNTIME_VALIDATION
```

**Conclusion class: `MODEL`.** The contract is sufficiently specified to make `L02_ATTENTION` state structurally addressable, but it must remain distinct from canonical recovery, implementation, executed validation, and empirical proof.

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
