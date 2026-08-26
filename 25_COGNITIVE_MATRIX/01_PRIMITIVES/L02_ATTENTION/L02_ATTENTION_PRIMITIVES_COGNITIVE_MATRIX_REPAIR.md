---
tags:
  - amos
  - cognitive-matrix
  - l02
  - attention
  - repair
  - recovery
  - rscf
  - hml
  - governance

title: "L02_ATTENTION — REPAIR"
origin_architect: "Trang Phan"
status: "MODEL_SPECIFICATION / SOURCE-BOUNDED / UNVALIDATED"
epistemic_class: "MODEL"
runtime_alignment: "AMOS Full Brain OS / AMOS_CORE v4.4 lineage"
---

# L02_ATTENTION — Repair

**Class:** `COGNITIVE_PRIMITIVE_CONTRACT`  
**Origin architect / steward:** Trang Phan  
**Primitive:** `L02_ATTENTION`  
**Artifact:** `REPAIR.md`  
**Status:** `AMOS_MODEL / SOURCE-BOUNDED / UNVALIDATED`

> **Canon boundary:** available L02 material supports attention allocation and budgeting of scarce reasoning/observation resources. The repair architecture below is an AMOS-aligned model for restoring corrupted attention-allocation state. It is not asserted as recovered canonical L02 repair logic or as an implemented runtime.

---

# 0. Repair Contract

`L02_ATTENTION` repair restores a valid attention-allocation state after allocation, prioritization, focus, resource, dependency, provenance, scope, regime, freshness, H/M/L, or governance integrity has degraded.

Conceptually:

\[
CorruptedAttentionState_t
\rightarrow
Detect
\rightarrow
Localize
\rightarrow
Contain
\rightarrow
Invalidate
\rightarrow
Restore
\rightarrow
Reallocate
\rightarrow
Revalidate
\rightarrow
Resume
\]

The governing repair principle is:

```text
REPAIR THE SMALLEST INVALID ATTENTION SUBGRAPH
THAT RESTORES THE REQUIRED INVARIANTS.
```

Repair must preserve unaffected valid state.

```text
LOCAL FAILURE
!=
GLOBAL INVALIDATION
```

---

# 1. Source / Canon References

## 1.1 Source-supported semantic core

Current source-bounded interpretation supports:

```text
L02_ATTENTION
=
attention allocation;
budget scarce reasoning/observation resources
```

Therefore repair may safely be framed around restoration of attention allocation and resource-budget integrity.

The available source evidence does **not** independently establish canonical:

```text
repair operators
repair equations
rollback semantics
failure taxonomy
repair agents
repair workflows
repair thresholds
retry limits
repair protocols
runtime recovery implementation
```

Those remain `AMOS_MODEL` or `UNKNOWN/GAP`.

## 1.2 AMOS architectural references

This model is aligned where applicable with:

```text
AMOS Full Brain OS
AMOS_CORE v3.0 → v4.4 lineage
RSCF
H/M/L decomposition
dependency-aware selective invalidation
provenance preservation
scope/regime/freshness controls
competing hypotheses
constraint propagation
rollback/recovery
capability/authority separation
proposal/commit separation
```

Alignment does not prove canonical derivation.

---

# 2. Definition and Scope

## 2.1 Definition

An attention-repair operation is a bounded transformation:

[
Repair:
(A_{bad}, E, D, C, P)
\rightarrow
(A_{candidate}, R)
]

where:

```text
A_bad       = suspected invalid attention state
E           = available evidence
D           = dependency state
C           = constraints/governance context
P           = provenance state
A_candidate = proposed repaired attention state
R           = repair report/proof capsule
```

Repair is successful only when required invariants are restored and validators no longer detect the target failure.

## 2.2 Scope

Repair may address:

```text
candidate admission
priority ordering
resource allocation
focus state
deferred state
quarantine state
dependency traversal
contradiction visibility
COMPETING preservation
scope/regime alignment
freshness
provenance
confidence ceiling
H/M/L routing
stop conditions
escalation state
```

Repair does not inherently authorize:

```text
external action
persistent mutation
cross-agent commit
memory deletion
authority expansion
irreversible execution
```

---

# 3. Typed Inputs

```yaml
AttentionRepairInput:

  attention_state:
    type: AttentionState

  detected_failure:
    type: AttentionFailure

  candidate_space:
    type: AttentionCandidate[]

  objective:
    type: GoalState

  resource_budget:
    type: ResourceBudget

  dependency_graph:
    type: DependencyGraph

  constraints:
    type: ConstraintSet

  evidence:
    type: EvidenceBundle

  provenance:
    type: ProvenanceBundle

  uncertainty:
    type: UncertaintyVector

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

  repair_history:
    type: RepairEvent[]
```

---

# 4. Typed Outputs

```yaml
AttentionRepairOutput:

  diagnosis:
    type: RepairDiagnosis

  causal_candidates:
    type: FailureCause[]

  invalidated_state:
    type: StateRef[]

  preserved_state:
    type: StateRef[]

  repaired_state:
    type: AttentionStateCandidate

  reallocation:
    type: AttentionAllocationProposal

  escalation:
    type: EscalationRequest | null

  rollback:
    type: RollbackProposal | null

  validators:
    type: ValidationResult[]

  unresolved_gaps:
    type: GapRef[]

  provenance:
    type: ProvenanceBundle

  uncertainty:
    type: UncertaintyVector

  confidence_ceiling:
    type: ConfidenceBound

  status:
    type:
      - REPAIRED_CANDIDATE
      - PARTIAL_REPAIR
      - BLOCKED
      - ESCALATED
      - ROLLBACK_REQUIRED
      - UNKNOWN_GAP
```

Hard boundary:

```text
REPAIRED_CANDIDATE
!=
COMMITTED_REPAIR
```

---

# 5. State Variables

```text
A_t        = current attention state
A*_t       = candidate repaired attention state
F_t        = detected failure state
Root_t     = candidate root-cause set
Inv_t      = invalidated state set
Keep_t     = preserved valid state
B_t        = resource budget
G_t        = governing objective
D_t        = dependency graph
C_t        = constraint state
P_t        = provenance state
U_t        = uncertainty vector
S_t        = scope
R_t        = regime
Fr_t       = freshness
HML_t      = H/M/L coordinate
Auth_t     = authority state
Hist_t     = repair history
Val_t      = validator state
Gap_t      = unresolved repair gaps
```

---

# 6. Repair Operators

Candidate repair operators:

```text
DETECT_FAILURE()
CLASSIFY_FAILURE()
LOCALIZE_FAILURE()

TRACE_DEPENDENCIES()
TRACE_PROVENANCE()
TRACE_ALLOCATION_HISTORY()

IDENTIFY_ROOT_CANDIDATES()
COMPARE_ROOT_HYPOTHESES()

FREEZE_AFFECTED_STATE()
PRESERVE_VALID_STATE()
QUARANTINE_STATE()

INVALIDATE_PREMISE()
INVALIDATE_EDGE()
INVALIDATE_DESCENDANTS()

RESTORE_OBJECTIVE()
RESTORE_CONSTRAINTS()
RESTORE_SCOPE()
RESTORE_REGIME()
RESTORE_FRESHNESS()
RESTORE_PROVENANCE()
RESTORE_HML_CONTEXT()
RESTORE_CONFIDENCE_CEILING()

REOPEN_COMPETING()
RESTORE_CONTRADICTION()

RECOMPUTE_PRIORITY()
REALLOCATE()
RELEASE_INVALID_FOCUS()

REVALIDATE()
ROLLBACK_PROPOSE()
ESCALATE_REPAIR()

RESUME()
TERMINATE_REPAIR()
```

These operator names are `AMOS_MODEL`.

---

# 7. Repair Equations

## 7.1 Minimal invalidation

Let (x) be an invalid premise/state node and (Desc(x)) its actual dependent descendants.

Candidate invalidation:

[
I(x)={x}\cup Desc(x)
]

not:

[
I(x)=EntireAttentionState
]

unless dependency evidence requires global invalidation.

---

## 7.2 Repair objective

Conceptually:

[
A^*
===

\arg\min_{A'}
RepairCost(A,A')
]

subject to:

[
RequiredInvariants(A') = TRUE
]

and:

[
PreserveValidState(A,A')
]

and:

[
ResourceUse(A') \le Budget
]

This is an architectural optimization model, not a canonical AMOS equation.

---

## 7.3 Retry condition

A failed repair path should only be retried if:

[
ChangedEvidence
\lor
ChangedState
\lor
ChangedMethod
\lor
ChangedConstraint
]

is true.

Thus:

[
SamePath
\land
SameState
\land
SameEvidence
\Rightarrow
NoBlindRetry
]

---

## 7.4 Confidence after repair

Repair cannot manufacture confidence.

For repaired conclusion (C'):

[
Conf(C')
\le
\min_j Conf(P_j)
]

for its unresolved load-bearing premises unless independent revalidation changes the evidence graph.

---

# 8. Repair Invariants

```text
L02-REP-INV-001
Repair must identify a target failure before changing attention state.

L02-REP-INV-002
Repair must preserve unaffected valid state where dependency structure permits.

L02-REP-INV-003
Invalidation propagates only through actual dependencies.

L02-REP-INV-004
Repair cannot erase unresolved contradictions merely to restore coherence.

L02-REP-INV-005
Repair cannot collapse genuine COMPETING hypotheses without discriminating evidence.

L02-REP-INV-006
Repair cannot convert UNKNOWN/GAP into PASS.

L02-REP-INV-007
Repair cannot manufacture provenance.

L02-REP-INV-008
Repair cannot refresh stale evidence without revalidation.

L02-REP-INV-009
Repair cannot expand scope silently.

L02-REP-INV-010
Repair cannot cross regime boundaries silently.

L02-REP-INV-011
Repair must preserve H/M/L identity.

L02-REP-INV-012
Repair cannot increase authority.

L02-REP-INV-013
Repair proposal cannot become durable commit implicitly.

L02-REP-INV-014
Repair must remain within its resource envelope.

L02-REP-INV-015
Repeated failure without changed information must trigger rerouting, escalation, or termination.

L02-REP-INV-016
Repair success requires post-repair validation.

L02-REP-INV-017
Cosmetic coherence is not evidence of functional recovery.

L02-REP-INV-018
Repair confidence cannot exceed surviving load-bearing evidence.
```

---

# 9. Dependencies

```yaml
dependencies:

  primitive:
    - L02_ATTENTION

  upstream:
    - L01_SENSING_OBSERVATION

  local:
    - L02_ATTENTION_DEFINITION
    - L02_ATTENTION_VARIABLES
    - L02_ATTENTION_STATE
    - L02_ATTENTION_OPERATORS
    - L02_ATTENTION_INVARIANTS
    - L02_ATTENTION_DEPENDENCIES
    - L02_ATTENTION_HML
    - L02_ATTENTION_PROVENANCE
    - L02_ATTENTION_FAILURE_MODES
    - L02_ATTENTION_GAP_MATRIX
    - L02_ATTENTION_RSCF
    - L02_ATTENTION_TESTS

  governance:
    - objective_state
    - constraint_state
    - dependency_state
    - resource_state
    - provenance_state
    - scope
    - regime
    - freshness
    - authority_state
```

---

# 10. H/M/L Applicability

## H — Governing repair

Repairs attention failures capable of changing system-level conclusions or trajectories.

Examples:

```text
goal drift
systemic priority inversion
critical risk starvation
global resource misallocation
governance boundary failure
```

H repair should be conservative because downstream fan-out may be large.

---

## M — Subsystem repair

Repairs allocation across:

```text
research branches
agents
tools
hypotheses
tasks
subsystems
repair queues
```

Typical question:

> Which allocation decision produced the subsystem failure?

---

## L — Local repair

Repairs:

```text
one candidate
one priority score
one stale source
one dependency
one focus decision
one contradiction
one provenance edge
```

Preferred default:

```text
REPAIR AT THE LOWEST SUFFICIENT LEVEL.
```

Escalate upward only when dependency closure requires it.

---

# 11. Control-Plane Requirements

L02 repair may diagnose and propose.

The control plane should govern durable effects such as:

```text
persistent state replacement
shared budget mutation
cross-agent invalidation
memory mutation
authority-sensitive rollback
external action cancellation
durable commit
```

Boundary:

```text
REPAIR CAPABILITY
!=
REPAIR AUTHORITY
```

and:

```text
ROLLBACK PROPOSAL
!=
AUTHORIZED ROLLBACK
```

Commit-time validation should re-check material mutable conditions before durable repair.

---

# 12. Agents

Candidate roles:

```text
L02_REPAIR_COORDINATOR
L02_FAILURE_LOCALIZER
L02_DEPENDENCY_TRACER
L02_PROVENANCE_AUDITOR
L02_REALLOCATION_AGENT
L02_REVALIDATION_AGENT
L02_REPAIR_AUDITOR
```

Role separation may reduce self-confirming repair but does not itself establish independent evidence.

```text
DIFFERENT AGENT
!=
INDEPENDENT PROVENANCE
```

---

# 13. Skills

Potential supporting AMOS capabilities include:

```text
AMOS Attention Allocation Governor
AMOS Target of Repair Intelligence
AMOS Repair Priority Governor
AMOS Repair Harm Auditor
AMOS Constraint Propagation RSCF Engine
AMOS Context Continuity Governor
AMOS Metacognitive Confidence Auditor
AMOS Provenance Trust Firewall
AMOS Infrastructure Control Plane
RSCF Modeler
```

These are capability mappings, not proof of runtime invocation.

---

# 14. Repair Workflow

```text
FAILURE SIGNAL
      ↓
VERIFY SIGNAL
      ↓
CLASSIFY FAILURE
      ↓
LOCALIZE FIRST INVALID STATE
      ↓
TRACE DEPENDENCIES
      ↓
TRACE PROVENANCE
      ↓
GENERATE COMPETING ROOT-CAUSE HYPOTHESES
      ↓
RUN CHEAPEST DISCRIMINATING CHECK
      ↓
FREEZE AFFECTED STATE
      ↓
PRESERVE UNAFFECTED VALID STATE
      ↓
SELECTIVE INVALIDATION
      ↓
RESTORE REQUIRED CONTEXT
      ↓
RECOMPUTE MINIMUM REQUIRED ATTENTION STATE
      ↓
REALLOCATE
      ↓
RUN VALIDATORS
      ↓
ADVERSARIAL CHECK
      ↓
REPAIRED?
   ↙       ↘
 YES        NO
 ↓           ↓
RESUME     REROUTE /
           ESCALATE /
           ROLLBACK /
           TERMINATE
```

---

# 15. Protocols

Candidate repair protocol family:

```text
ATTENTION_FAILURE_NOTICE
ATTENTION_REPAIR_REQUEST
ATTENTION_REPAIR_DIAGNOSIS
ATTENTION_ROOT_CAUSE_PROPOSAL
ATTENTION_STATE_FREEZE_REQUEST
ATTENTION_INVALIDATION_PROPOSAL
ATTENTION_REALLOCATION_PROPOSAL
ATTENTION_REVALIDATION_REQUEST
ATTENTION_REPAIR_RESULT
ATTENTION_ROLLBACK_PROPOSAL
ATTENTION_REPAIR_ESCALATION
ATTENTION_REPAIR_TERMINATION
ATTENTION_RESUME_REQUEST
```

Canonical names and schemas remain `UNKNOWN/GAP`.

---

# 16. Evidence / Provenance

Every consequential repair should preserve:

```yaml
RepairProvenance:

  repair_id: string

  failure_ref:
    type: FailureRef

  pre_repair_state:
    type: StateRef

  suspected_causes:
    type: FailureCause[]

  selected_cause:
    type: FailureCause | null

  evidence_refs:
    type: EvidenceRef[]

  provenance_refs:
    type: ProvenanceRef[]

  invalidated_nodes:
    type: StateRef[]

  preserved_nodes:
    type: StateRef[]

  repair_operations:
    type: OperatorEvent[]

  post_repair_state:
    type: StateRef

  validators:
    type: ValidationResult[]

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeRef

  freshness:
    type: FreshnessState

  hml:
    type: HMLContext
```

Repair history must distinguish:

```text
ATTEMPTED
REJECTED
FAILED
PARTIAL
VALIDATED_CANDIDATE
COMMITTED
ROLLED_BACK
```

An attempted repair must never be recorded as completed merely because execution began.

---

# 17. Uncertainty and Confidence Ceiling

Repair uncertainty should be decomposed:

```yaml
repair_uncertainty:

  failure_detection: bounded
  root_cause: bounded
  dependency: bounded
  provenance: bounded
  scope: bounded
  regime: bounded
  temporal: bounded
  repair_effect: bounded
  regression: bounded
  execution: bounded
```

If multiple root causes remain equally viable:

```text
ROOT CAUSE = COMPETING
```

not falsely resolved.

Repair confidence is bounded by the weakest load-bearing element among:

```text
failure diagnosis
dependency map
provenance
repair mechanism
post-repair validation
```

---

# 18. Failure Modes

Repair-specific failure modes include:

```text
wrong repair target
symptom repair instead of cause repair
over-invalidation
under-invalidation
global reset for local failure
stale-state restoration
rollback to invalid checkpoint
provenance destruction
scope leakage
regime leakage
confidence inflation
contradiction suppression
COMPETING collapse
repair loop
attention thrashing
resource exhaustion
repair-induced starvation
repair externality
authority overreach
unvalidated resumption
false success classification
cosmetic repair
silent regression
```

---

# 19. Repair / Recovery Strategies

## 19.1 Priority order

```text
1. CONTAIN
2. PRESERVE
3. LOCALIZE
4. INVALIDATE SELECTIVELY
5. RESTORE LOAD-BEARING CONTEXT
6. REALLOCATE
7. VALIDATE
8. RESUME
```

## 19.2 Recovery classes

```yaml
recovery_classes:

  LOCAL_REPAIR:
    use_when: failure is dependency-localized

  SELECTIVE_ROLLBACK:
    use_when: prior valid attention state exists

  REALLOCATION:
    use_when: priorities or budgets became invalid

  REVALIDATION:
    use_when: freshness/regime/provenance changed

  ESCALATION:
    use_when: authority, critical uncertainty, or cross-scale impact exceeds L02 scope

  SAFE_TERMINATION:
    use_when: repair cannot restore minimum invariants
```

## 19.3 No blind retry

```text
FAILED PATH
+
NO NEW EVIDENCE
+
NO STATE CHANGE
+
NO METHOD CHANGE
=
DO NOT REPEAT
```

---

# 20. Tests / Validators

Required repair validators:

```text
VALIDATE_FAILURE_EXISTS
VALIDATE_FAILURE_CLASS
VALIDATE_REPAIR_TARGET
VALIDATE_DEPENDENCY_CLOSURE
VALIDATE_SELECTIVE_INVALIDATION
VALIDATE_VALID_STATE_PRESERVATION
VALIDATE_RESOURCE_BOUNDS
VALIDATE_SCOPE
VALIDATE_REGIME
VALIDATE_FRESHNESS
VALIDATE_PROVENANCE
VALIDATE_HML
VALIDATE_COMPETING_PRESERVATION
VALIDATE_CONTRADICTION_VISIBILITY
VALIDATE_CONFIDENCE_CEILING
VALIDATE_AUTHORITY_BOUNDARY
VALIDATE_PROPOSAL_COMMIT_BOUNDARY
VALIDATE_POST_REPAIR_INVARIANTS
VALIDATE_NO_REGRESSION
VALIDATE_RESUME_ELIGIBILITY
```

Adversarial cases:

```text
1. One stale premise contaminates one branch.
   Expected:
   invalidate only affected branch and descendants.

2. Apparent local failure originates from H-level objective drift.
   Expected:
   local patch rejected; escalate.

3. Repair removes contradiction.
   Expected:
   fail unless evidence resolves contradiction.

4. Repair merges equal hypotheses.
   Expected:
   fail; preserve COMPETING.

5. Repair restores an old but stale checkpoint.
   Expected:
   freshness validator fails.

6. Repair exceeds resource budget.
   Expected:
   reject/reallocate.

7. Same failed repair repeated unchanged.
   Expected:
   reroute/escalate/terminate.

8. Repair proposes persistent mutation without authority.
   Expected:
   proposal allowed; commit blocked.

9. Repair improves coherence but worsens objective alignment.
   Expected:
   regression failure.

10. Repair cannot determine root cause.
    Expected:
    UNKNOWN/GAP or COMPETING, not fabricated diagnosis.
```

Tests remain `UNEXECUTED` until actual evidence exists.

---

# 21. Falsifiers

This repair contract must be revised if direct evidence establishes that:

```text
L02 does not own attention-state repair.

Repair is canonically assigned entirely to another primitive.

Canonical AMOS repair requires global recomputation rather than selective invalidation.

Canonical L02 allows authority-bearing durable repair.

Canonical H/M/L behavior contradicts this repair model.

Canonical rollback semantics materially differ.

Executable runtime evidence falsifies the modeled repair lifecycle.

The source-defined attention primitive does not include resource allocation.
```

---

# 22. Gap Matrix

```yaml
gap_matrix:

  source_attention_semantics:
    status: SOURCE_SUPPORTED

  scarce_resource_semantics:
    status: SOURCE_SUPPORTED

  repair_definition:
    status: MODEL_DEFINED

  typed_repair_io:
    status: MODEL_DEFINED

  repair_state:
    status: MODEL_DEFINED

  repair_operators:
    status: MODEL_DEFINED

  repair_invariants:
    status: MODEL_DEFINED

  selective_invalidation:
    status: AMOS_MODEL_ALIGNED

  HML_repair:
    status: MODEL_DEFINED

  control_plane_boundary:
    status: MODEL_DEFINED

  repair_agents:
    status: MODEL_DEFINED

  repair_skills:
    status: MODEL_DEFINED

  repair_workflow:
    status: MODEL_DEFINED

  repair_protocols:
    status: MODEL_DEFINED

  repair_provenance:
    status: MODEL_DEFINED

  repair_tests:
    status: MODEL_DEFINED_UNEXECUTED

  canonical_repair_ownership:
    status: UNKNOWN_GAP

  canonical_repair_equations:
    status: UNKNOWN_GAP

  canonical_repair_operators:
    status: UNKNOWN_GAP

  canonical_retry_policy:
    status: UNKNOWN_GAP

  canonical_rollback_semantics:
    status: UNKNOWN_GAP

  canonical_thresholds:
    status: UNKNOWN_GAP

  runtime_implementation:
    status: UNKNOWN_GAP

  runtime_validation:
    status: UNKNOWN_GAP
```

---

# 23. RSCF Completion State

```yaml
rscf:

  id: L02_ATTENTION_REPAIR

  claim:
    L02 attention failures can be modeled as repairable state and
    dependency failures requiring localization, selective invalidation,
    restoration of governing context, bounded reallocation, and
    post-repair validation.

  claim_class: MODEL

  evidence:
    - source-supported L02 attention allocation semantics
    - source-supported scarce reasoning/observation resource semantics
    - AMOS architectural repair principles used as integration context

  provenance:
    origin_architect: Trang Phan
    architecture_family: AMOS
    subsystem: COGNITIVE_MATRIX
    primitive: L02_ATTENTION
    artifact: REPAIR.md
    derivation: SOURCE_BOUNDED_AMOS_MODEL

  scope:
    system: AMOS_OS
    subsystem: COGNITIVE_MATRIX
    primitive: L02_ATTENTION
    function: attention_state_repair

  regime:
    governed finite-resource attention repair

  freshness:
    revalidate_when:
      - direct L02 repair canon is recovered
      - repair ownership changes
      - dependency semantics change
      - control-plane contracts change
      - AMOS_CORE runtime changes
      - executable repair evidence becomes available

  dependencies:
    - L02_ATTENTION_DEFINITION
    - L02_ATTENTION_STATE
    - L02_ATTENTION_OPERATORS
    - L02_ATTENTION_INVARIANTS
    - L02_ATTENTION_DEPENDENCIES
    - L02_ATTENTION_HML
    - L02_ATTENTION_PROVENANCE
    - L02_ATTENTION_FAILURE_MODES
    - L02_ATTENTION_GAP_MATRIX
    - L02_ATTENTION_TESTS

  competing:
    - repair owned locally by L02
    - repair owned by a higher cognitive supervisor
    - repair owned by infrastructure control plane
    - hybrid local-diagnosis/control-plane-commit architecture

  falsifiers:
    - incompatible direct canon
    - incompatible primitive ownership
    - incompatible runtime implementation
    - failure of selective invalidation assumptions
    - failure of modeled control-plane separation

  uncertainty:
    evidence: HIGH
    model: MEDIUM
    scope: MEDIUM
    temporal: MEDIUM
    causal: MEDIUM
    execution: HIGH
    provenance_independence: MEDIUM

  confidence_ceiling:
    source evidence supports the L02 attention-allocation core only;
    detailed repair behavior remains MODEL pending direct canon or
    executable validation

  gap_status:
    canonical_repair_ownership: CRITICAL_GAP
    canonical_repair_equations: DECISION_RELEVANT_GAP
    canonical_repair_operators: DECISION_RELEVANT_GAP
    canonical_rollback_semantics: DECISION_RELEVANT_GAP
    runtime_implementation: CRITICAL_GAP
    executed_validation: CRITICAL_GAP
```

---

# 24. Completion State

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

  runtime_validation:
    status: UNKNOWN_GAP

  overall:
    status: COMPLETE_FOR_REPAIR_MODEL_SPECIFICATION_SCOPE

  conclusion_class:
    MODEL
```

---

# 25. Hard Boundaries

```text
PLACEHOLDER != IMPLEMENTED
ADDRESSABLE != VALIDATED
CAPABILITY != AUTHORITY
PROPOSAL != COMMIT
UNKNOWN/GAP != PASS
```

Repair-specific boundaries:

```text
DETECTED FAILURE != ROOT CAUSE

ROOT-CAUSE HYPOTHESIS != VERIFIED CAUSE

REPAIR ATTEMPT != REPAIR SUCCESS

REPAIR SUCCESS != COMMIT AUTHORITY

ROLLBACK PROPOSAL != ROLLBACK COMMIT

COHERENCE RESTORED != TRUTH RESTORED

SYMPTOM REMOVED != CAUSE REMOVED

RETRY != NEW EVIDENCE

GLOBAL RESET != DEFAULT REPAIR

INVALID NODE != INVALID SYSTEM

LOCAL FAILURE != GLOBAL FAILURE

REPAIRED MODEL != VALIDATED RUNTIME

DOCUMENTED RECOVERY != EXECUTED RECOVERY
```

---

# 26. References

```text
[[L02_ATTENTION — Readme]]
[[L02_ATTENTION — Purpose]]
[[L02_ATTENTION — Definition]]
[[L02_ATTENTION — Variables]]
[[L02_ATTENTION — State]]
[[L02_ATTENTION — Operators]]
[[L02_ATTENTION — Invariants]]
[[L02_ATTENTION — Dependencies]]
[[L02_ATTENTION — Equations]]
[[L02_ATTENTION — Hml]]
[[L02_ATTENTION — Memory]]
[[L02_ATTENTION — Control Planes]]
[[L02_ATTENTION — Agents]]
[[L02_ATTENTION — Skills]]
[[L02_ATTENTION — Workflows]]
[[L02_ATTENTION — Protocols]]
[[L02_ATTENTION — Provenance]]
[[L02_ATTENTION — Failure Modes]]
[[L02_ATTENTION — Gap Matrix]]
[[L02_ATTENTION — Rscf]]
[[L02_ATTENTION — Tests]]

[[L01_SENSING_OBSERVATION]]

[[AMOS Attention Allocation Governor]]
[[AMOS Target of Repair Intelligence]]
[[AMOS Repair Priority Governor]]
[[AMOS Repair Harm Auditor]]
[[AMOS Constraint Propagation RSCF Engine]]
[[AMOS Provenance Trust Firewall]]
[[AMOS Infrastructure Control Plane]]
[[AMOS Full Brain OS]]
[[AMOS CORE v4.4]]
```

---

# 27. Governing Repair Contract

> **`L02_ATTENTION` repair restores a valid bounded attention-allocation state by identifying the smallest supported failure locus, preserving unaffected valid state, selectively invalidating actual dependents, restoring load-bearing objective/constraint/provenance/scope/regime/freshness/HML context, reallocating resources, and requiring post-repair validation. Repair must never manufacture evidence, erase unresolved contradictions, collapse genuine competing hypotheses, inflate confidence, broaden authority, or convert a repair proposal into a durable commit.**

---

# 28. Canon Boundary

```text
SOURCE-SUPPORTED:

L02_ATTENTION concerns attention allocation.

Reasoning/observation resources are scarce.


AMOS_MODEL:

attention repair state
failure localization
selective invalidation
repair operators
repair equations
repair invariants
H/M/L repair
repair agents
repair workflows
repair protocols
repair provenance
retry policy
rollback proposal
post-repair validation


UNKNOWN/GAP:

canonical L02 repair ownership
canonical repair operators
canonical repair equations
canonical retry rules
canonical rollback semantics
canonical repair thresholds
runtime implementation
executed repair validation
```

Therefore:

```text
CONCLUSION CLASS:
MODEL

NOT:
VERIFIED CANONICAL REPAIR SPECIFICATION

NOT:
PROOF OF IMPLEMENTATION

NOT:
PROOF OF RECOVERY CORRECTNESS

NOT:
AUTHORIZATION TO MUTATE OR COMMIT
```

```text
```

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]] · [[COGNITIVE_MATRIX_MOC]]
