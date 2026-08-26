Confirmed: the current Drive `TASK_CONTRACT.md` is only a **275-byte erroneous placeholder** containing `# K COUNTERFACTUAL`; it has no actual Task Contract specification.  

Below is the substantive replacement for:

`03_CONTROL_PLANE/01_TASK_CONTRACT/TASK_CONTRACT.md`

---
artifact_id: AMOS-OS-CP-TASK-CONTRACT
title: AMOS OS Task Contract
canonical_name: TASK_CONTRACT

artifact_class: CONTROL_PLANE_CONTRACT
plane: CONTROL_PLANE
subsystem: TASK_CONTRACT
canonical_location: 03_CONTROL_PLANE/01_TASK_CONTRACT/TASK_CONTRACT.md

origin_architect: Trang Phan
amos_core_target: v4.4

status: CANDIDATE_CANON
conclusion_class: DERIVED

parent:
  - 03_CONTROL_PLANE

siblings:
  - TASK_RESOLVER.md

upstream:
  - 00_ROOT
  - 01_CANON
  - 02_KERNEL
  - 03_CONTROL_PLANE/00_INDEX/README.md
  - 03_CONTROL_PLANE/00_INDEX/CONTROL_PLANE_MAP.md

downstream:
  - 03_CONTROL_PLANE/02_CAPABILITY
  - 03_CONTROL_PLANE/03_POLICY
  - 03_CONTROL_PLANE/04_AUTHORITY
  - 03_CONTROL_PLANE/05_PROVENANCE
  - 03_CONTROL_PLANE/06_SEMANTIC_TRANSACTION
  - 03_CONTROL_PLANE/07_OBSERVABILITY
  - 03_CONTROL_PLANE/08_EFFECTS
  - 03_CONTROL_PLANE/09_COMMIT
  - 04_RUNTIME

implementation_status: SPECIFICATION
empirical_validation_status: NOT_CLAIMED
formal_verification_status: NOT_CLAIMED

updated: 2026-08-26
---

# AMOS OS — TASK CONTRACT

> **Layer:** `03_CONTROL_PLANE/01_TASK_CONTRACT`
>
> **Artifact:** `TASK_CONTRACT.md`
>
> **Status:** `CANDIDATE_CANON`
>
> **AMOS CORE target:** `v4.4`
>
> **Origin Architect:** Trang Phan

---

# 0. Purpose

The Task Contract is the canonical Control Plane representation of a bounded
piece of requested work.

It converts an interpreted request into an explicit execution-facing semantic
contract.

The Task Contract answers:

```text
WHAT is being requested?

WHY is it being requested?

WHAT counts as completion?

WHAT is inside scope?

WHAT is outside scope?

WHAT inputs may be used?

WHAT outputs are expected?

WHAT constraints govern execution?

WHAT assumptions are load-bearing?

WHAT uncertainties remain?

WHAT freshness is required?

WHAT effects may occur?

WHAT effects must not occur?

WHAT authority may eventually be required?

WHAT evidence must be preserved?

WHAT conditions invalidate the task?
```

The Task Contract is therefore the first major governance boundary between:

```text
REQUEST
```

and:

```text
CONTROLLED EXECUTION
```

---

# 1. Core Law

```text
NO CONSEQUENTIAL EXECUTION
WITHOUT A SUFFICIENTLY BOUNDED TASK.
```

Expanded:

```text
REQUEST
    ↓
INTERPRET
    ↓
BOUND OBJECTIVE
    ↓
BOUND SCOPE
    ↓
BOUND CONSTRAINTS
    ↓
BOUND COMPLETION CONDITION
    ↓
TASK CONTRACT
    ↓
CONTROL-PLANE RESOLUTION
```

A request is not automatically a valid Task Contract.

---

# 2. Fundamental Distinctions

The following must remain separate:

```text
REQUEST
!=
TASK

TASK
!=
PLAN

PLAN
!=
ACTION

ACTION
!=
EFFECT

EFFECT
!=
SUCCESS

SUCCESS
!=
OBJECTIVE SATISFACTION
```

Likewise:

```text
USER WORDING
!=
RESOLVED INTENT
```

and:

```text
RESOLVED INTENT
!=
UNLIMITED AUTHORITY
```

---

# 3. Role in the Control Plane

The Task Contract is the first typed object consumed by downstream Control
Plane components.

Conceptually:

```text
REQUEST
   ↓
TASK_RESOLVER
   ↓
TASK_CONTRACT
   ↓
┌──────────────────────────────┐
│ CAPABILITY RESOLUTION        │
│ POLICY EVALUATION            │
│ AUTHORITY RESOLUTION         │
│ PROVENANCE BINDING           │
│ SEMANTIC TRANSACTION         │
│ OBSERVABILITY                │
│ EFFECT CLASSIFICATION        │
│ COMMIT GOVERNANCE            │
└──────────────────────────────┘
```

The Task Contract establishes the semantic boundary within which those
systems operate.

---

# 4. Task Contract Principle

A valid Task Contract must be:

```text
IDENTIFIABLE

BOUNDED

SCOPED

TYPED

TRACEABLE

VERSIONED

CONSTRAINT-AWARE

FRESHNESS-AWARE

EFFECT-AWARE

INVALIDATABLE
```

when those dimensions are material.

---

# 5. Canonical Conceptual Structure

```yaml
TaskContract:

  identity:
    task_id:
    task_version:
    parent_task_id:
    correlation_id:
    created_at:
    created_by:

  origin:
    request_source:
    request_reference:
    request_timestamp:
    provenance:

  objective:
    primary_objective:
    secondary_objectives: []
    objective_class:
    success_definition:

  deliverable:
    type:
    format:
    destination:
    required_properties: []
    acceptance_criteria: []

  scope:
    included: []
    excluded: []
    system_scope:
    population_scope:
    environment_scope:
    temporal_scope:
    regime_scope:

  inputs:
    required: []
    optional: []
    prohibited: []

  assumptions:
    load_bearing: []
    noncritical: []

  constraints:
    hard: []
    soft: []
    policy_constraints: []
    resource_constraints: []
    temporal_constraints: []

  freshness:
    required:
    maximum_age:
    revalidation_trigger:

  uncertainty:
    evidence:
    model:
    scope:
    temporal:
    causal:
    execution:
    provenance_independence:

  stakes:
    level:
    irreversible:
    financial:
    legal:
    health:
    safety:
    institutional:
    downstream_dependency:

  effects:
    allowed_classes: []
    prohibited_classes: []
    expected_effects: []
    reversibility_requirement:

  authority:
    anticipated_requirement:
    principal:
    scope:

  dependencies:
    tasks: []
    evidence: []
    state: []
    capabilities: []

  completion:
    claim_sufficiency:
    decision_sufficiency:
    action_sufficiency:
    completion_conditions: []

  invalidation:
    conditions: []
    expiry:
    regime_shift_conditions: []

  provenance:
    source_lineage:
    derivation:
    transformations: []

  state:
    status:
    blocking_gaps: []
```

This schema is conceptual unless separately bound to an implementation
schema.

---

# 6. Task Identity

Every governed task should have stable identity.

Minimum conceptual identity:

```text
TASK_ID
TASK_VERSION
```

Potential extended identity:

```text
TASK_ID
TASK_VERSION
PARENT_TASK_ID
ROOT_TASK_ID
CORRELATION_ID
TRANSACTION_ID
SESSION_ID
```

These fields permit task lineage without assuming every runtime uses all
identifiers.

---

# 7. Task ID

`task_id` identifies one logical task instance.

Required property:

```text
TASK_ID(A) = TASK_ID(B)
```

should mean:

```text
A and B refer to the same logical task lineage
```

unless explicitly versioned otherwise.

Task IDs should not silently be reused for semantically unrelated work.

---

# 8. Task Version

Tasks may evolve.

Therefore:

```text
TASK
=
IDENTITY + VERSIONED SEMANTICS
```

Example:

```text
TASK-001 @ V1
```

may request:

```text
summarize report
```

while:

```text
TASK-001 @ V2
```

may add:

```text
include external verification
```

Those versions are not semantically identical.

---

# 9. Parent / Child Tasks

Complex work may decompose:

```text
ROOT TASK
   │
   ├── SUBTASK A
   │
   ├── SUBTASK B
   │
   └── SUBTASK C
```

Each child should retain lineage to the parent.

Candidate invariant:

```text
CHILD_SCOPE
⊆
AUTHORIZED_PARENT_SCOPE
```

unless explicit expansion is separately authorized.

---

# 10. Task Origin

A Task Contract must retain where the task came from.

Possible origins include:

```text
USER_REQUEST

SYSTEM_REQUIREMENT

PARENT_TASK

AGENT_DELEGATION

RECOVERY_PROCESS

SCHEDULED_OPERATION

EVENT_TRIGGER

POLICY_REQUIREMENT

GOVERNANCE_ACTION
```

Origin affects provenance and potentially authority.

---

# 11. Request Preservation

The source request should remain recoverable where practical.

Do not transform:

```text
SOURCE REQUEST
```

into:

```text
RESOLVED TASK
```

and discard the original semantic source.

Preserve:

```text
SOURCE
+
RESOLUTION
```

so divergence can later be audited.

---

# 12. Objective

The objective defines the desired semantic outcome.

Example:

```yaml
objective:
  primary_objective:
    "Determine whether candidate architecture satisfies specified invariants."
```

An objective should describe:

```text
DESIRED RESULT
```

rather than merely:

```text
ACTIVITY
```

Example:

Weak:

```text
research X
```

Stronger:

```text
determine whether X satisfies conditions A, B, and C
using evidence current to T
```

---

# 13. Primary Objective

Every task should have one identifiable primary objective.

Multiple outputs may exist.

Multiple subtasks may exist.

But execution must be able to answer:

```text
WHAT IS THIS TASK FUNDAMENTALLY TRYING TO ACHIEVE?
```

If no answer exists, the task is under-specified.

---

# 14. Secondary Objectives

Secondary objectives are subordinate goals.

They must not silently override the primary objective.

Conceptually:

```text
PRIMARY OBJECTIVE
>
SECONDARY OBJECTIVES
>
COSMETIC PREFERENCES
```

subject to hard constraints.

---

# 15. Objective Conflict

If objectives conflict:

```text
O1
↔
O2
```

the contract must not silently optimize one while pretending both were
satisfied.

Instead:

```text
CONFLICT
→
RESOLVE
OR
PRESERVE COMPETING
OR
ESCALATE
```

depending on materiality.

---

# 16. Deliverable

The deliverable defines what must be produced.

Examples:

```text
ANSWER

REPORT

FILE

PLAN

DECISION

ANALYSIS

CODE

STATE CHANGE

TOOL EFFECT

MESSAGE

DATASET

PROOF CAPSULE
```

The deliverable is not identical to the objective.

---

# 17. Objective vs Deliverable

Example:

```text
OBJECTIVE:
determine which option is safest
```

```text
DELIVERABLE:
comparison table + recommendation
```

Therefore:

```text
OBJECTIVE
!=
OUTPUT FORMAT
```

The distinction must remain explicit.

---

# 18. Acceptance Criteria

A deliverable should define what qualifies as acceptable.

Conceptually:

```yaml
acceptance_criteria:

  - satisfies requested scope
  - uses required sources
  - identifies critical uncertainty
  - preserves contradictions
  - meets requested format
  - avoids prohibited effects
```

Acceptance criteria should be testable where possible.

---

# 19. Scope

Scope defines the applicability envelope of the task.

A robust scope may include:

```text
SYSTEM

POPULATION

ENVIRONMENT

DOMAIN

SCALE

TIME

REGIME

MEASUREMENT METHOD

ASSUMPTIONS
```

Not every task requires every dimension.

Only material dimensions should be activated.

---

# 20. Included Scope

Explicitly define what is included.

Example:

```yaml
scope:
  included:
    - uploaded AMOS corpus
    - current architecture tree
    - v4.4 reasoning lineage
```

This prevents uncontrolled expansion.

---

# 21. Excluded Scope

Explicit exclusion is important.

Example:

```yaml
scope:
  excluded:
    - implementation claims not supported by evidence
    - unrelated legacy architecture
    - external empirical claims unless separately verified
```

An excluded item must not silently enter the conclusion as a premise.

---

# 22. Scope Expansion

Scope expansion is a semantic task mutation.

Conceptually:

```text
SCOPE V1
   ↓
NEW REQUIREMENT
   ↓
SCOPE V2
```

Material scope expansion should create:

```text
TASK VERSION CHANGE
```

or a child task.

It should not occur invisibly.

---

# 23. Scope Contraction

Scope may also contract.

When scope contracts:

```text
REMOVE OUT-OF-SCOPE DEPENDENCIES
```

and invalidate conclusions that relied on removed scope where necessary.

---

# 24. Regime Scope

A task may only be valid under a specific regime.

Examples:

```text
policy regime

market regime

software version

legal regime

hardware environment

experimental condition

organizational state
```

A regime shift may invalidate the Task Contract.

---

# 25. Temporal Scope

The task should identify relevant time semantics.

Examples:

```text
CURRENT

AS OF T

BETWEEN T1 AND T2

HISTORICAL

FORECAST

TIME-INVARIANT ASSUMPTION
```

A task asking:

```text
what is true now?
```

has different freshness requirements from:

```text
what was documented in v3.0?
```

---

# 26. Inputs

Task inputs are the resources required or permitted for resolution.

Classify:

```text
REQUIRED

OPTIONAL

PROHIBITED
```

Potential inputs:

```text
documents

database records

user statements

tool outputs

web evidence

sensor observations

prior proof capsules

runtime state

canonical artifacts
```

---

# 27. Required Inputs

If a required input is missing:

```text
REQUIRED INPUT ABSENT
```

then the system should classify the resulting gap.

Possible outcomes:

```text
BLOCK

REQUEST INPUT

RETRIEVE INPUT

USE SAFE SUBSTITUTE IF AUTHORIZED

RETURN UNKNOWN/GAP
```

Do not invent the missing input.

---

# 28. Optional Inputs

Optional inputs may improve quality but are not load-bearing.

If omitted:

```text
TASK MAY STILL COMPLETE
```

provided acceptance criteria remain satisfied.

---

# 29. Prohibited Inputs

Some inputs must not be used.

Reasons may include:

```text
privacy

policy

scope

licensing

confidentiality

contamination

evaluation isolation

user instruction
```

The Task Contract should preserve such restrictions.

---

# 30. Assumptions

Assumptions must be explicit when load-bearing.

Classify:

```text
LOAD_BEARING

NONCRITICAL
```

Load-bearing assumption:

```text
if false,
the conclusion or action may materially change
```

Noncritical assumption:

```text
plausible changes do not materially alter the result
```

---

# 31. Assumption Ceiling

A derived conclusion cannot silently exceed the reliability of a
load-bearing assumption.

Conceptually:

```text
CONFIDENCE(CONCLUSION)
≤
MIN(
  CONFIDENCE(LOAD_BEARING_PREMISES)
)
```

unless independently revalidated.

---

# 32. Constraints

Constraints define what execution must respect.

Classify:

```text
HARD CONSTRAINT

SOFT CONSTRAINT
```

Hard constraint:

```text
MUST NOT BE VIOLATED
```

Soft constraint:

```text
OPTIMIZE IF POSSIBLE
```

---

# 33. Hard Constraints

Examples:

```text
DO NOT DELETE DATA

DO NOT EXPOSE PRIVATE INFORMATION

USE ONLY PROVIDED SOURCES

MUST FINISH BEFORE DEADLINE

DO NOT MODIFY PRODUCTION STATE

MUST PRESERVE CANONICAL TERMINOLOGY
```

Hard constraints dominate ordinary optimization preferences.

---

# 34. Soft Constraints

Examples:

```text
prefer concise output

minimize latency

minimize cost

prefer fewer tool calls

prefer reversible action

prefer local computation
```

Soft constraints may be traded against one another.

They may not override hard integrity constraints.

---

# 35. Constraint Hierarchy

Conceptually:

```text
CANON / SAFETY / GOVERNANCE
        ↓
HARD TASK CONSTRAINTS
        ↓
OBJECTIVE REQUIREMENTS
        ↓
SOFT CONSTRAINTS
        ↓
OPTIMIZATION
```

Exact law hierarchy remains governed by upstream canon.

---

# 36. Constraint Conflict

If:

```text
C1
AND
C2
```

cannot simultaneously hold:

```text
DO NOT SILENTLY DROP ONE
```

Instead:

```text
IDENTIFY CONFLICT

DETERMINE PRECEDENCE IF CANONICAL

OTHERWISE ESCALATE / PRESERVE GAP
```

---

# 37. Freshness

Tasks that depend on mutable state require freshness semantics.

Conceptual fields:

```yaml
freshness:
  required: true
  observed_at:
  maximum_age:
  valid_until:
  refresh_trigger:
```

---

# 38. Freshness Is Local

Not every premise has the same freshness requirement.

Example:

```text
mathematical definition
```

may be stable while:

```text
current account balance
```

may require immediate revalidation.

Therefore:

```text
FRESHNESS
IS
PREMISE-SPECIFIC
```

---

# 39. Freshness Failure

If a load-bearing premise exceeds its freshness bound:

```text
STALE(P)
```

then:

```text
INVALIDATE DEPENDENT CONCLUSIONS
```

not necessarily the entire task.

---

# 40. Stakes

The Task Contract should classify stakes where they affect governance depth.

Potential dimensions:

```text
REVERSIBILITY

FINANCIAL

LEGAL

HEALTH

SAFETY

INSTITUTIONAL

REPUTATIONAL

INFORMATION EXPOSURE

DOWNSTREAM DEPENDENCY
```

---

# 41. Stakes Are Multi-Dimensional

Do not reduce all stakes to one number when dimensions matter.

Example:

```yaml
stakes:
  financial: LOW
  safety: LOW
  information_exposure: HIGH
  reversibility: LOW
```

may require different governance than a simple `MEDIUM` label suggests.

---

# 42. Irreversibility

Irreversibility increases required validation.

Conceptually:

```text
VALIDATION_DEPTH
↑
AS
IRREVERSIBILITY
↑
```

all else equal.

---

# 43. Reversible Preference

When two paths satisfy the objective:

```text
PATH A = irreversible

PATH B = reversible
```

and expected utility is otherwise comparable:

```text
PREFER B
```

under unresolved uncertainty.

---

# 44. Uncertainty Vector

Material uncertainty should not be collapsed into one vague confidence score.

Track separately where relevant:

```text
EVIDENCE UNCERTAINTY

MODEL UNCERTAINTY

SCOPE UNCERTAINTY

TEMPORAL UNCERTAINTY

CAUSAL UNCERTAINTY

EXECUTION UNCERTAINTY

PROVENANCE-INDEPENDENCE UNCERTAINTY
```

---

# 45. Evidence Uncertainty

Question:

```text
DO WE HAVE ENOUGH RELIABLE EVIDENCE?
```

This differs from model uncertainty.

Strong evidence may still support multiple models.

---

# 46. Model Uncertainty

Question:

```text
IS OUR INTERPRETIVE MODEL ADEQUATE?
```

Examples:

```text
multiple plausible mechanisms

unknown model misspecification

insufficient abstraction fit
```

---

# 47. Scope Uncertainty

Question:

```text
DOES THE EVIDENCE APPLY TO THIS TASK'S ACTUAL SCOPE?
```

Scope uncertainty prevents silent generalization.

---

# 48. Temporal Uncertainty

Question:

```text
IS THE EVIDENCE STILL CURRENT?
```

This may trigger retrieval or commit-time revalidation.

---

# 49. Causal Uncertainty

Question:

```text
DO WE KNOW THE CAUSAL RELATIONSHIP REQUIRED BY THE TASK?
```

Association must not be silently upgraded to causation.

---

# 50. Execution Uncertainty

Question:

```text
CAN THE PLANNED ACTION ACTUALLY PRODUCE THE INTENDED EFFECT?
```

This concerns execution semantics rather than epistemic truth alone.

---

# 51. Provenance-Independence Uncertainty

Question:

```text
ARE MULTIPLE SUPPORTING SOURCES ACTUALLY INDEPENDENT?
```

Repeated descendants of one origin do not constitute independent
confirmation.

---

# 52. Gap Classification

Task gaps should be classified:

```text
CRITICAL

DECISION-RELEVANT

EXPLANATORY

COSMETIC
```

Priority:

```text
CRITICAL
>
DECISION-RELEVANT
>
EXPLANATORY
>
COSMETIC
```

---

# 53. Critical Gap

A critical gap prevents safe or valid completion.

Examples:

```text
target unknown for irreversible operation

authority unknown

required evidence missing

scope cannot be determined

hard constraint unresolved
```

A critical gap generally blocks consequential execution.

---

# 54. Decision-Relevant Gap

A gap is decision-relevant when resolving it could flip:

```text
RECOMMENDATION

ACTION

CLASSIFICATION

AUTHORIZATION

EFFECT
```

Such gaps deserve priority.

---

# 55. Explanatory Gap

An explanatory gap affects understanding but not the decision.

It may remain unresolved if further investigation has low decision value.

---

# 56. Cosmetic Gap

A cosmetic gap affects presentation but not substance.

Examples:

```text
minor formatting

nonessential wording

optional metadata
```

Do not spend high-cost reasoning on cosmetic gaps before critical ones.

---

# 57. Decision-Changing Uncertainty

The Task Contract should identify:

```text
WHAT UNKNOWN,
IF RESOLVED,
IS MOST LIKELY TO CHANGE THE OUTCOME?
```

This drives efficient retrieval and reasoning.

---

# 58. Sensitivity

For consequential tasks, identify the smallest premise or threshold capable
of flipping the result.

Conceptually:

```text
RESULT = f(P1, P2, P3, ...)
```

Find:

```text
argmin ΔPi
such that
RESULT changes
```

in conceptual terms.

Test that premise first when feasible.

---

# 59. Fragility

A task result is fragile when small plausible perturbations in a
load-bearing premise change the outcome.

Mark:

```text
CONDITIONAL
```

rather than presenting the result as robust.

---

# 60. Robustness

A result is more robust when it survives plausible changes to noncritical
assumptions.

Robustness does not imply universal validity.

It remains bounded by task scope and regime.

---

# 61. Effect Envelope

The Task Contract should anticipate what kinds of effects are allowed.

Conceptually:

```yaml
effects:
  allowed:
    - read
    - analyze
    - generate_draft

  prohibited:
    - external_send
    - destructive_write

  conditional:
    - persistent_write
```

Actual effect classification remains downstream.

---

# 62. Effect Expansion

If execution discovers a required effect outside the Task Contract:

```text
NEW EFFECT
∉
AUTHORIZED TASK EFFECT ENVELOPE
```

then:

```text
DO NOT SILENTLY EXECUTE
```

Instead:

```text
RECONTRACT

REAUTHORIZE

OR
ESCALATE
```

as appropriate.

---

# 63. Side Effects

The task should identify known material side effects.

Unknown side effects should not be represented as nonexistent.

Use:

```text
UNKNOWN
```

when necessary.

---

# 64. Authority Anticipation

The Task Contract does not itself grant authority.

It may record expected authority requirements.

Example:

```yaml
authority:
  anticipated_requirement:
    - read_repository
    - write_branch
```

Actual authorization belongs to the authority subsystem.

---

# 65. Task Contract ≠ Authorization

Critical invariant:

```text
VALID TASK CONTRACT
!=
AUTHORIZED EXECUTION
```

A perfectly specified task may still be denied.

---

# 66. Capability Anticipation

The Task Contract may specify required semantic capabilities.

Example:

```text
READ SOURCE

COMPARE CLAIMS

WRITE FILE

SEND MESSAGE
```

Capability resolution determines whether such capabilities exist.

---

# 67. Task Contract ≠ Capability

Likewise:

```text
TASK REQUIRES X
```

does not imply:

```text
SYSTEM CAN DO X
```

The distinction must remain explicit.

---

# 68. Dependencies

A task may depend on:

```text
OTHER TASKS

EVIDENCE

STATE

CAPABILITIES

POLICIES

AUTHORITIES

EXTERNAL SYSTEMS
```

Dependencies should be explicit when load-bearing.

---

# 69. Dependency Closure

Before local fast-path execution, the system should know the material
dependency closure.

Conceptually:

```text
TASK
 ↓
D1
 ↓
D2
```

If `D2` can materially alter the task result, it belongs in the closure.

---

# 70. Hidden Dependency

A hidden dependency is a load-bearing dependency not represented in the
contract.

Example:

```text
task assumes current policy
```

but policy version is not tracked.

Hidden dependencies create stale-result risk.

---

# 71. Dependency Independence

Independent subtasks may execute locally or concurrently when independence is
demonstrated.

Do not infer:

```text
DIFFERENT FILE
=
INDEPENDENT TASK
```

Shared provenance, state, authority, or effects may couple them.

---

# 72. Competing Hypotheses

Some tasks require evaluating incompatible hypotheses.

The Task Contract should allow:

```text
H1

H2

H3
```

to remain:

```text
COMPETING
```

until discriminating evidence exists.

---

# 73. No Forced Convergence

If support is:

```text
EQUAL

INCOMPARABLE

CORRELATED

OR INSUFFICIENT
```

do not force a winner merely to satisfy output fluency.

Return:

```text
COMPETING
```

or:

```text
UNKNOWN/GAP
```

as appropriate.

---

# 74. Discriminating Test

When hypotheses compete, seek the cheapest high-information test capable of
changing the outcome.

Prefer:

```text
DISCRIMINATING EVIDENCE
```

over:

```text
MORE REDUNDANT EVIDENCE
```

---

# 75. Causal Requirement

If the task asks a causal question, the contract should say so.

Example:

```yaml
objective_class: CAUSAL
```

Then evidence requirements differ from descriptive or predictive tasks.

---

# 76. Causal Firewall

The Task Contract must not allow a downstream process to silently substitute:

```text
CORRELATION
```

for:

```text
CAUSAL EFFECT
```

when causation is load-bearing.

Relevant distinctions include:

```text
ASSOCIATION

CORRELATION

MECHANISM

ENABLING CONDITION

NECESSARY CONDITION

SUFFICIENT CONDITION

MEDIATION

CONFOUNDING

FEEDBACK

CAUSAL EFFECT
```

---

# 77. Epistemic Requirement

A task may require a specific conclusion class.

AMOS classes:

```text
VERIFIED

DERIVED

MODEL

CONDITIONAL

COMPETING

UNKNOWN/GAP
```

The system must use the weakest accurate class.

---

# 78. Verified

Use `VERIFIED` only where the required claim has appropriate direct
validation within its scope.

Do not use `VERIFIED` merely because a source asserts something.

---

# 79. Derived

Use `DERIVED` when the conclusion follows from supported premises but is not
itself directly observed or validated.

---

# 80. Model

Use `MODEL` for:

```text
conceptual architecture

simulation

cross-domain mapping

structural analogy

proposed mechanism
```

unless independently validated.

---

# 81. Conditional

Use `CONDITIONAL` when:

```text
IF P
THEN C
```

and `P` remains uncertain, bounded, or regime-specific.

---

# 82. Competing

Use `COMPETING` when incompatible hypotheses remain materially viable.

---

# 83. Unknown / Gap

Use:

```text
UNKNOWN/GAP
```

when evidence is insufficient.

This is a valid Task Contract outcome.

---

# 84. Proof Requirement

Important task conclusions should conceptually carry a proof capsule.

```yaml
proof_capsule:

  claim:
  class:
  premises:
  evidence:
  provenance:
  scope:
  temporal_validity:
  regime_validity:
  dependencies:
  competing_explanations:
  falsifiers:
  invalidation_conditions:
  confidence_ceiling:
```

---

# 85. Proof Capsule Reuse

A prior proof capsule may be reused only while:

```text
DEPENDENCIES VALID

SCOPE COMPATIBLE

REGIME COMPATIBLE

FRESHNESS VALID

PROVENANCE SUFFICIENT

NO MATERIAL CONFLICT
```

remain true.

---

# 86. Task Mutation

A Task Contract changes when a load-bearing field changes.

Examples:

```text
OBJECTIVE CHANGE

SCOPE CHANGE

CONSTRAINT CHANGE

TARGET CHANGE

DELIVERABLE CHANGE

STAKE CHANGE

EFFECT CHANGE

FRESHNESS CHANGE
```

Material mutation should increment task version or generate a successor task.

---

# 87. Non-Material Mutation

Changes such as:

```text
formatting

nonsemantic wording

cosmetic ordering
```

may not require semantic task version changes.

Implementation-specific version policy belongs elsewhere.

---

# 88. Task Supersession

A task may supersede an earlier task.

Preserve:

```text
PREDECESSOR

SUCCESSOR

REASON

CHANGED FIELDS

INVALIDATED DEPENDENCIES

PRESERVED DEPENDENCIES
```

Do not erase the historical contract.

---

# 89. Task Cancellation

Cancellation means:

```text
FUTURE EXECUTION UNDER THIS CONTRACT
IS NO LONGER AUTHORIZED BY TASK INTENT
```

It does not automatically reverse effects already committed.

Those require recovery/rollback semantics.

---

# 90. Task Expiration

A Task Contract may expire.

Examples:

```text
deadline passed

freshness bound exceeded

authority window closed

regime changed

input state changed materially
```

Expiration should block stale execution where material.

---

# 91. Task State

Candidate conceptual states:

```text
DRAFT

RESOLVING

READY

BLOCKED

ACTIVE

WAITING

REVALIDATION_REQUIRED

COMPLETED

FAILED

CANCELLED

EXPIRED

SUPERSEDED
```

These labels remain candidate states unless separately registered.

---

# 92. Draft

`DRAFT` means the contract exists but is not yet sufficient for governed
execution.

---

# 93. Resolving

`RESOLVING` means ambiguity or dependencies are still being resolved.

---

# 94. Ready

`READY` means Task Contract sufficiency has been achieved.

It does not mean:

```text
COMMIT AUTHORIZED
```

---

# 95. Blocked

`BLOCKED` means at least one load-bearing gap prevents progression.

A blocked contract should identify the blocker.

---

# 96. Active

`ACTIVE` means downstream work is occurring under the contract.

---

# 97. Waiting

`WAITING` means progress depends on an external condition or unresolved
dependency.

---

# 98. Revalidation Required

Use when previously valid task state may have become stale.

---

# 99. Completed

`COMPLETED` means the Task Contract's defined completion conditions have been
met.

It does not necessarily mean every possible related activity is finished.

---

# 100. Failed

A task fails when required completion cannot be achieved under the active
contract.

Failure should retain reason and recoverability.

---

# 101. Cancelled

Cancelled tasks should not continue effectful execution.

Already committed effects remain separately governed.

---

# 102. Expired

Expired means temporal validity has ended.

---

# 103. Superseded

Superseded means another Task Contract now governs the intended work.

---

# 104. Completion Model

AMOS task completion should distinguish:

```text
CLAIM SUFFICIENCY

DECISION SUFFICIENCY

ACTION SUFFICIENCY
```

---

# 105. Claim Sufficiency

Question:

```text
DO WE HAVE ENOUGH SUPPORT
TO STATE THE REQUIRED CLAIM?
```

A research task may stop here.

---

# 106. Decision Sufficiency

Question:

```text
DO WE HAVE ENOUGH INFORMATION
TO CHOOSE BETWEEN RELEVANT OPTIONS?
```

Perfect knowledge is not required if further uncertainty reduction would not
change the decision.

---

# 107. Action Sufficiency

Question:

```text
DO WE HAVE ENOUGH VALIDATION,
AUTHORITY,
AND EXECUTION READINESS
TO ACT?
```

This is stricter than claim sufficiency.

---

# 108. Completion Condition

A task should specify explicit completion conditions.

Example:

```yaml
completion_conditions:

  - requested comparison completed
  - decisive evidence cited
  - unresolved material contradiction exposed
  - recommendation classified
  - no consequential effect requested
```

---

# 109. Stop Rule

Stop expanding the task when:

```text
CLAIM SUFFICIENCY
AND/OR
DECISION SUFFICIENCY
AND/OR
ACTION SUFFICIENCY
```

required by the task has been reached.

Do not retrieve or reason indefinitely merely because more information
exists.

---

# 110. Smallest Sufficient Proof Scope

AMOS v4.4 principle:

```text
USE THE SMALLEST PROOF SCOPE
THAT CAN SAFELY SATISFY THE TASK.
```

This means:

```text
LOAD ONLY DECISION-RELEVANT DEPENDENCIES
```

rather than the entire knowledge universe.

---

# 111. H/M/L Retrieval Contract

Where AMOS Fractal Knowledge Network retrieval is used:

```text
BOOTSTRAP CAPSULE
       ↓
H DOMAIN
       ↓
M SUBSYSTEM
       ↓
L DETAIL
       ↓
RAW EVIDENCE
ONLY IF REQUIRED
```

Raw evidence defaults:

```text
DO_NOT_LOAD_UNLESS_REQUIRED
```

The Task Contract should indicate the depth required when material.

---

# 112. Retrieval Escalation

Escalate retrieval when:

```text
LOAD-BEARING DETAIL MISSING

CONTRADICTION EXISTS

PROVENANCE UNCLEAR

FRESHNESS FAILED

REGIME MISMATCH

HIGH-STAKES EFFECT

CAUSAL CLAIM REQUIRES SUPPORT
```

---

# 113. Retrieval De-Escalation

Stop deeper retrieval once additional evidence cannot materially change:

```text
CLAIM

DECISION

ACTION
```

within the Task Contract.

---

# 114. Adaptive Complexity

Candidate task complexity classes:

```text
C0 DIRECT

C1 COMPACT

C2 STRUCTURED

C3 DEEP

C4 MAXIMUM
```

Start at the lowest sufficient level.

---

# 115. Complexity Escalation

Escalate for:

```text
HIGH STAKES

IRREVERSIBILITY

NOVELTY

WEAK EVIDENCE

STALE EVIDENCE

CONTRADICTION

CAUSAL AMBIGUITY

SCOPE MISMATCH

COMPETING MODELS

GOVERNANCE IMPACT

LOW TRUST

EXPLICIT DEEP REQUEST
```

---

# 116. Complexity De-Escalation

Once outcome-changing uncertainty is resolved:

```text
DE-ESCALATE
```

Do not retain maximum reasoning depth without decision value.

---

# 117. Task Budget

A task may carry resource budgets.

Examples:

```yaml
budget:

  time:
  token:
  monetary:
  tool_calls:
  context:
  external_requests:
```

Budget is subordinate to hard integrity requirements.

---

# 118. Budget Exhaustion

If budget becomes insufficient:

```text
DO NOT FABRICATE COMPLETION
```

Instead:

```text
RETURN BEST VALID PARTIAL RESULT

IDENTIFY MISSING WORK

CLASSIFY REMAINING GAP
```

where allowed.

---

# 119. Partial Completion

Partial completion must be explicit.

Conceptually:

```yaml
completion:
  state: PARTIAL
  completed:
    - A
    - B
  unresolved:
    - C
```

Never present partial work as total completion.

---

# 120. Task Delegation

A task may be delegated.

Delegation should preserve:

```text
OBJECTIVE

SCOPE

CONSTRAINTS

PROVENANCE

AUTHORITY LIMITS

EXPECTED OUTPUT

RETURN CONTRACT
```

---

# 121. Delegation Narrowing

A delegated subtask may be narrower than its parent.

It must not silently become broader.

Candidate invariant:

```text
DELEGATED_TASK_SCOPE
⊆
PARENT_TASK_SCOPE
```

unless separately authorized.

---

# 122. Return Contract

A delegated task should define what must return.

Examples:

```text
RESULT

EVIDENCE

UNCERTAINTY

PROVENANCE

FAILURE

GAPS

EFFECT STATE
```

This prevents agents from returning only fluent conclusions without support.

---

# 123. Multi-Agent Task Contract

For multi-agent work:

```yaml
multi_agent:

  coordinator:
  agents:

    - role:
      subtask:
      scope:
      dependencies:
      return_contract:

  merge_policy:
  conflict_policy:
```

The coordinator must not assume agents are independent merely because they
are separate agents.

---

# 124. Atomic Multi-Task Reasoning

Several subtasks may need to be treated atomically when their conclusions
share load-bearing state.

Example:

```text
SUBTASK A reads V1
SUBTASK B reads V2
```

If A and B must jointly support one irreversible decision:

```text
V1/V2 compatibility
```

must be established.

---

# 125. Task Snapshot

A consequential task should be bound to an appropriate state snapshot.

Conceptually:

```yaml
snapshot:

  task_version:
  policy_epoch:
  authority_epoch:
  evidence_versions:
  relevant_state_versions:
```

Not every task needs all fields.

---

# 126. MVCC/CAS Pattern

AMOS may use MVCC/CAS concepts as reasoning patterns.

Conceptually:

```text
READ STATE @ V
       ↓
REASON
       ↓
BEFORE COMMIT:
COMPARE CURRENT STATE TO V
```

If compatible:

```text
CONTINUE
```

If materially changed:

```text
REVALIDATE DEPENDENT CLOSURE
```

This specification does not claim a particular database implementation.

---

# 127. Task Read Set

The Task Contract may identify expected evidence dependencies.

The actual observed read set belongs to Control Plane provenance.

Distinction:

```text
EXPECTED INPUT SET
!=
OBSERVED READ SET
```

---

# 128. Provenance Requirement

Important task inputs should preserve:

```text
SOURCE IDENTITY

ANCESTRY

VERSION

TIMESTAMP

SCOPE

REGIME

TRANSFORMATION

DEPENDENCY ROLE
```

where material.

---

# 129. Source Claim vs Observation

The Task Contract must allow downstream reasoning to distinguish:

```text
SOURCE_CLAIM

OBSERVATION

DERIVED

MODEL

DECISION

UNKNOWN
```

A source assertion is not automatically an observation.

---

# 130. Correlated Provenance

Multiple sources may share ancestry.

Conceptually:

```text
SOURCE A
   ├── SOURCE B
   ├── SOURCE C
   └── SOURCE D
```

Then:

```text
B + C + D
```

does not necessarily equal three independent confirmations.

---

# 131. Sybil Resistance

Task evidence counting must not treat identity multiplication as evidence
multiplication.

```text
MANY IDENTITIES
!=
MANY INDEPENDENT ORIGINS
```

when ancestry is shared.

---

# 132. Conflict Preservation

If task evidence contains unresolved contradictions:

```text
DO NOT HIDE THEM
```

The Task Contract result should expose contradictions that can alter the
outcome.

---

# 133. Contradiction Classes

Potential task-level contradiction classes:

```text
FACTUAL

TEMPORAL

SCOPE

REGIME

CAUSAL

POLICY

AUTHORITY

SEMANTIC

PROVENANCE
```

Different contradictions require different resolution paths.

---

# 134. Adversarial Validation

Consequential task conclusions should be challenged using a genuinely
different path.

Test for:

```text
CONTRADICTION

CORRELATED PROVENANCE

STALE PREMISE

SCOPE LEAKAGE

HIDDEN DEPENDENCY

CAUSAL OVERREACH

STRONGER ALTERNATIVE
```

---

# 135. Challenge Success

If adversarial validation succeeds:

```text
DOWNGRADE

CONDITION

PRESERVE COMPETING

OR
RETURN UNKNOWN/GAP
```

Do not defend the original conclusion merely because it was generated first.

---

# 136. Challenge Failure

Failure to find a contradiction is not proof.

```text
NO CONTRADICTION FOUND
!=
VERIFIED
```

Conclusion class remains governed by actual evidence.

---

# 137. Task Safety Envelope

A task should preserve an action safety envelope.

Conceptually:

```yaml
safety_envelope:

  permitted_actions: []
  prohibited_actions: []
  escalation_actions: []
  recovery_requirements: []
```

This is not a replacement for policy or authority.

---

# 138. Information Exposure

If a task can disclose information, exposure becomes part of the contract.

Potential fields:

```yaml
information_exposure:

  allowed_recipients:
  prohibited_recipients:
  allowed_classes:
  declassification_required:
```

Actual exposure governance remains downstream.

---

# 139. Privacy Boundary

The Task Contract should not expand information use beyond what the task
requires.

Conceptually:

```text
MINIMUM NECESSARY INFORMATION
```

should be preferred when equivalent.

---

# 140. Execution Environment

Tasks may be environment-specific.

Example:

```yaml
environment:

  production: false
  sandbox: true
  repository:
  branch:
  workspace:
```

Environment mismatch may invalidate an execution plan.

---

# 141. Dry Run

A task may require:

```text
DRY_RUN_ONLY
```

A dry-run task must not silently transition into real effect.

---

# 142. Preview

A preview is informational.

```text
PREVIEW
!=
COMMIT
```

A downstream system must preserve that distinction.

---

# 143. Simulation

Simulation output is:

```text
MODEL
```

unless separately validated against real execution.

Simulation success does not authorize execution.

---

# 144. Tool Use

The Task Contract may permit tool use.

It should distinguish:

```text
READ-ONLY TOOL

REVERSIBLE WRITE

PERSISTENT WRITE

EXTERNAL EFFECT

IRREVERSIBLE EFFECT
```

where material.

---

# 145. Tool Success

Critical invariant:

```text
TOOL SUCCESS
!=
TASK SUCCESS
```

A tool can execute correctly while solving the wrong task.

---

# 146. External Finality

For tasks involving external systems:

```text
REQUEST SENT
!=
RECEIVED
!=
APPLIED
!=
FINAL
```

Completion conditions must specify the required finality level.

---

# 147. Retry

Retry must preserve task semantics.

Do not retry a failed path unchanged when failure cause remains unchanged.

Conceptually:

```text
FAIL
↓
LOCALIZE CAUSE
↓
CHANGE RELEVANT CONDITION
↓
RETRY
```

---

# 148. Idempotence

Where retries are possible, the Task Contract should indicate whether the
effect is expected to be idempotent.

```text
RETRY(X)
```

must not be assumed safe if:

```text
X
```

is non-idempotent.

---

# 149. Recovery

Tasks with consequential effects should anticipate recovery.

Potential recovery classes:

```text
RETRY

ROLLBACK

COMPENSATE

REPAIR

QUARANTINE

FORWARD RECOVERY

SELECTIVE INVALIDATION
```

---

# 150. Selective Invalidation

If premise `P` fails:

```text
INVALIDATE
DESCENDANTS(P)
```

not unrelated task state.

Example:

```text
P1 → C1 → C3

P2 → C1

P3 → C2
```

If:

```text
P2 = INVALID
```

then:

```text
INVALIDATE C1
INVALIDATE C3

PRESERVE P1
PRESERVE P3
PRESERVE C2
```

unless other dependencies require otherwise.

---

# 151. Task Rollback Boundary

Task rollback is distinct from effect rollback.

```text
TASK STATE ROLLBACK
```

may mean restoring a prior reasoning state.

```text
EFFECT ROLLBACK
```

means changing external or persistent state.

The latter requires separate governance.

---

# 152. Task Failure Recovery

Recovery sequence:

```text
FAILURE
   ↓
LOCALIZE FAILED PREMISE / EDGE
   ↓
INVALIDATE DEPENDENTS
   ↓
ROLL BACK TO NEAREST VALID STATE
   ↓
REROUTE
   ↓
REVALIDATE
   ↓
CONTINUE IF SUFFICIENT
```

Global recomputation is a last resort.

---

# 153. Task Contract Validation

Before marking a Task Contract `READY`, validate at minimum:

```text
OBJECTIVE

DELIVERABLE

SCOPE

HARD CONSTRAINTS

LOAD-BEARING INPUTS

CRITICAL GAPS

COMPLETION CONDITION
```

and additional dimensions when material.

---

# 154. Structural Validation

Check:

```text
REQUIRED FIELDS PRESENT

TYPES VALID

DEPENDENCY REFERENCES VALID

NO IMPOSSIBLE INTERNAL STATE
```

Structural validity does not prove semantic validity.

---

# 155. Semantic Validation

Check:

```text
OBJECTIVE MATCHES REQUEST

DELIVERABLE MATCHES OBJECTIVE

SCOPE MATCHES INTENT

CONSTRAINTS MATCH INTENT

EFFECT ENVELOPE MATCHES INTENT
```

---

# 156. Provenance Validation

Check that material contract fields can be traced to their origin.

Particularly:

```text
OBJECTIVE

TARGET

SCOPE

CONSTRAINTS

EFFECTS

PARAMETERS
```

---

# 157. Conflict Validation

Check whether the contract contains mutually incompatible requirements.

Example:

```text
MUST SEND MESSAGE
```

and:

```text
MUST NOT CREATE EXTERNAL EFFECT
```

cannot both hold without additional interpretation.

---

# 158. Feasibility Validation

A task may be well specified but infeasible.

Feasibility belongs partly to capability resolution.

Task Contract state may therefore become:

```text
VALID_BUT_INFEASIBLE
```

conceptually, rather than mutating the objective.

---

# 159. Authority Validation Boundary

Task validation does not grant authority.

Authority is checked downstream.

Therefore:

```text
TASK_READY
```

does not imply:

```text
EXECUTION_READY
```

---

# 160. Policy Validation Boundary

Likewise:

```text
TASK_VALID
```

does not imply:

```text
POLICY_ALLOWED
```

Policy is a separate decision.

---

# 161. Commit Boundary

The Task Contract contributes to commit validation.

Before commit, verify:

```text
TASK STILL ACTIVE

TASK VERSION CURRENT

OBJECTIVE UNCHANGED

TARGET UNCHANGED

HARD CONSTRAINTS UNCHANGED

MATERIAL SCOPE UNCHANGED

TASK NOT CANCELLED

TASK NOT EXPIRED

TASK NOT SUPERSEDED
```

where relevant.

---

# 162. Commit-Time Task Mutation

If task semantics change after planning:

```text
PLAN @ TASK V1

TASK → V2

COMMIT
```

must not silently execute the V1 plan under V2 intent.

Instead:

```text
COMPARE

INVALIDATE AFFECTED PLAN

REVALIDATE
```

---

# 163. Task Finality

A task reaches finality only according to its completion conditions.

Examples:

Research:

```text
VALID ANSWER DELIVERED
```

File creation:

```text
FILE CREATED + VALIDATED
```

External transaction:

```text
EFFECT COMMITTED + REQUIRED RECEIPT OBSERVED
```

The finality definition must match the task.

---

# 164. Task Result

Conceptual result:

```yaml
TaskResult:

  task_id:
  task_version:

  status:

  objective_state:

  deliverable_state:

  claims:
    - claim:
      class:
      confidence_ceiling:

  unresolved:
    - gap:
      class:

  effects:
    intended:
    observed:

  completion:
    claim_sufficiency:
    decision_sufficiency:
    action_sufficiency:

  provenance:

  invalidation_conditions:
```

---

# 165. Task Result Integrity

The result must not claim more than was achieved.

Forbidden:

```text
PARTIAL
→
COMPLETE
```

```text
DERIVED
→
VERIFIED
```

```text
SIMULATED
→
OBSERVED
```

```text
REQUESTED
→
AUTHORIZED
```

```text
SENT
→
RECEIVED
```

without supporting evidence.

---

# 166. Task Contract Invariants

```text
TC-I01
EVERY CONSEQUENTIAL TASK MUST HAVE A BOUNDED OBJECTIVE.

TC-I02
TASK INTENT MUST REMAIN TRACEABLE TO ITS ORIGIN.

TC-I03
OBJECTIVE AND DELIVERABLE MUST REMAIN DISTINCT.

TC-I04
SCOPE MUST NOT EXPAND SILENTLY.

TC-I05
HARD CONSTRAINTS MUST NOT BE SILENTLY DROPPED.

TC-I06
LOAD-BEARING ASSUMPTIONS MUST BE EXPLICIT WHEN MATERIAL.

TC-I07
MISSING REQUIRED INPUT MUST NOT BE FABRICATED.

TC-I08
TASK CONTRACT DOES NOT GRANT AUTHORITY.

TC-I09
TASK CONTRACT DOES NOT GUARANTEE CAPABILITY.

TC-I10
TASK VALIDITY DOES NOT IMPLY POLICY ALLOWANCE.

TC-I11
TASK VERSION MUST CHANGE WHEN LOAD-BEARING SEMANTICS CHANGE.

TC-I12
STALE LOAD-BEARING PREMISES MUST BE REVALIDATED.

TC-I13
CONTRADICTIONS MUST REMAIN VISIBLE UNTIL RESOLVED.

TC-I14
COMPETING HYPOTHESES MUST NOT BE FORCED TO CONVERGE.

TC-I15
CAUSAL REQUIREMENTS MUST NOT BE SATISFIED BY STRUCTURAL SIMILARITY ALONE.

TC-I16
DERIVED CONFIDENCE MUST RESPECT LOAD-BEARING PREMISE CEILINGS.

TC-I17
PROVENANCE INDEPENDENCE MUST NOT BE ASSUMED.

TC-I18
TOOL SUCCESS MUST NOT BE EQUATED WITH TASK SUCCESS.

TC-I19
IRREVERSIBLE EFFECTS REQUIRE GREATER VALIDATION.

TC-I20
TASK COMPLETION MUST USE EXPLICIT COMPLETION CONDITIONS.

TC-I21
UNKNOWN MUST REMAIN UNKNOWN WHEN EVIDENCE IS INSUFFICIENT.

TC-I22
FAILURE SHOULD INVALIDATE ONLY DEPENDENT STATE.

TC-I23
RETRY MUST NOT REPEAT AN UNCHANGED FAILED PATH WITHOUT JUSTIFICATION.

TC-I24
LOCAL FAST PATH REQUIRES SUFFICIENT DEPENDENCY CLOSURE.

TC-I25
OPTIMIZATION MUST NEVER WEAKEN TASK INTEGRITY.
```

These identifiers are candidate specification IDs until separately registered
as canonical invariants.

---

# 167. Invalid Task Examples

## 167.1 Missing Objective

```yaml
task:
  objective: null
  instruction: "do it"
```

without recoverable context.

Result:

```text
INSUFFICIENT TASK BINDING
```

---

# 168. Unbounded Scope

```yaml
objective:
  "analyze everything"
```

with no defined domain or completion condition.

Result:

```text
SCOPE GAP
```

unless context supplies the bounds.

---

# 169. Contradictory Constraints

```yaml
constraints:
  - send the message
  - create no external effects
```

Result:

```text
CONSTRAINT CONFLICT
```

---

# 170. Missing Target

```yaml
objective:
  "delete the file"
target:
  UNKNOWN
```

Result:

```text
CRITICAL GAP
```

Do not infer a destructive target.

---

# 171. Stale Task

```text
TASK V1
↓
TARGET CHANGED
↓
PLAN V1 STILL EXECUTED
```

Invalid.

The plan must be revalidated.

---

# 172. Unauthorized Expansion

Original:

```text
read repository
```

Expanded execution:

```text
modify repository
```

Invalid unless the task is explicitly expanded and downstream authority
permits it.

---

# 173. Valid Minimal Read-Only Task

```yaml
task:

  objective:
    "Summarize the supplied document."

  deliverable:
    type: TEXT_RESPONSE

  scope:
    included:
      - supplied document

  effects:
    allowed:
      - read
      - analyze
      - respond

    prohibited:
      - external write

  completion:
    - accurate summary produced
```

This may be sufficient for a low-stakes direct task.

---

# 174. Valid Research Task

```yaml
task:

  objective:
    "Determine whether claim X is supported."

  evidence:
    required:
      - primary source
      - current supporting evidence

  freshness:
    required: true

  uncertainty:
    provenance_independence: MATERIAL

  deliverable:
    - conclusion
    - evidence
    - competing explanations
    - falsifiers

  completion:
    - decision-relevant evidence evaluated
    - material contradiction exposed
    - conclusion class assigned
```

---

# 175. Valid Effectful Task

```yaml
task:

  objective:
    "Apply approved configuration change X."

  scope:
    environment: PRODUCTION

  effects:
    expected:
      - configuration_write

  stakes:
    irreversible: false
    institutional: material

  constraints:
    hard:
      - validate target
      - preserve rollback state
      - revalidate authority at commit

  completion:
    - configuration committed
    - resulting state verified
```

Actual execution still requires downstream policy, authority, capability, and
commit approval.

---

# 176. Task Contract Proof Capsule

A consequential Task Contract should conceptually carry:

```yaml
TaskContractProofCapsule:

  contract:
    task_id:
    task_version:

  source:
    request:
    provenance:

  objective:
    primary:
    interpretation_basis:

  scope:
    included:
    excluded:

  constraints:
    hard:
    soft:

  assumptions:
    load_bearing:

  evidence_dependencies:

  uncertainty_vector:

  stakes:

  effect_envelope:

  competing_interpretations:

  falsifiers:

  invalidation_conditions:

  conclusion_class:

  confidence_ceiling:
```

---

# 177. Task Contract Fast Path

A compact Task Contract may be sufficient when:

```text
OBJECTIVE CLEAR

SCOPE LOCAL

EFFECT READ-ONLY OR REVERSIBLE

NO MATERIAL POLICY AMBIGUITY

NO MATERIAL AUTHORITY AMBIGUITY

NO MATERIAL PROVENANCE CONFLICT

LOW STAKES

NO CAUSAL OVERREACH

NO REGIME SHIFT

NO CRITICAL GAP
```

---

# 178. Fast Path Minimum

Even on the fast path, preserve:

```text
OBJECTIVE

SCOPE

DELIVERABLE

HARD CONSTRAINTS

COMPLETION CONDITION
```

and any additional load-bearing dimensions.

---

# 179. Deep Path

Escalate Task Contract depth when:

```text
HIGH STAKES

IRREVERSIBLE EFFECT

MULTIPLE SYSTEMS

MULTIPLE AGENTS

EXTERNAL COMMIT

SENSITIVE EXPOSURE

COMPLEX AUTHORITY

PROVENANCE CONFLICT

STALE STATE

CAUSAL CLAIM

COMPETING HYPOTHESES

REGIME CHANGE

LARGE DEPENDENCY GRAPH
```

---

# 180. Task Contract / RSCF Integration

Where RSCF is used, the Task Contract supplies the task-specific boundary
conditions for recursive reasoning.

Conceptually:

```text
TASK CONTRACT
     ↓
RSCF INSTANCE
     ↓
CLAIMS / RELATIONS / CONSTRAINTS
     ↓
DEPENDENCY CLOSURE
     ↓
RESULT
```

RSCF must not silently escape Task Contract scope.

---

# 181. Task Contract / HML Integration

H/M/L decomposition should be task-driven.

```text
TASK
 ↓
RELEVANT H DOMAIN
 ↓
RELEVANT M SUBSYSTEM
 ↓
RELEVANT L DETAIL
```

Not:

```text
LOAD ALL H/M/L
THEN SEARCH FOR RELEVANCE
```

unless the task explicitly requires exhaustive coverage.

---

# 182. Task Contract / GMEF Integration

A task that proposes structural evolution should identify that governance
impact.

Such tasks may require GMEF review.

Conceptually:

```text
TASK
→
PROPOSED SYSTEM CHANGE
→
GOVERNANCE IMPACT?
      |
      +-- NO → ordinary path
      |
      +-- YES → GMEF review path
```

---

# 183. Task Contract / Provenance Topology

Task evidence must preserve source ancestry when independence affects the
conclusion.

```text
TASK
 ↓
EVIDENCE A ──┐
EVIDENCE B ──┼→ PROVENANCE TOPOLOGY
EVIDENCE C ──┘
```

The task must not count descendants as independent merely because they have
different filenames or publishers.

---

# 184. Task Contract / Counterfactual Integration

Counterfactual analysis may be required for:

```text
PLANNING

RISK

CAUSAL ANALYSIS

RECOVERY

DECISION COMPARISON
```

But:

```text
COUNTERFACTUAL RESULT
=
MODEL / DERIVED RESULT
```

unless independently validated.

It does not itself grant permission to act.

---

# 185. Task Contract / Memory

Task context may depend on memory.

Memory must still satisfy:

```text
RELEVANCE

PROVENANCE

FRESHNESS

SCOPE

CONFLICT
```

before becoming load-bearing.

Remembered state is not automatically current state.

---

# 186. Task Contract / World Model

World-model state may support planning.

But:

```text
WORLD MODEL
!=
WORLD
```

The Task Contract should preserve this distinction when real-world action
depends on model state.

---

# 187. Task Contract / Runtime

Runtime receives governed work derived from the Task Contract.

The runtime must not reinterpret the objective in a way that materially
changes:

```text
TARGET

SCOPE

CONSTRAINT

EFFECT

COMPLETION
```

without returning to the Control Plane.

---

# 188. Task Contract / Finalizer

The finalizer should evaluate completion against the contract.

Not against:

```text
"something was produced"
```

but against:

```text
DEFINED ACCEPTANCE CRITERIA
```

---

# 189. Task Contract / Replay

Replay should preserve the Task Contract version used during the original
execution.

Otherwise a replay may unknowingly compare:

```text
EXECUTION UNDER TASK V1
```

against:

```text
EXPECTATIONS FROM TASK V2
```

and falsely classify divergence.

---

# 190. Task Contract / Rollback

If a Task Contract is invalidated after effects occurred:

```text
TASK INVALIDATION
```

must be connected to:

```text
EFFECT DEPENDENCY GRAPH
```

to determine which effects require repair.

---

# 191. Observability Requirements

Consequential tasks should identify what must be observable to determine
completion.

Example:

```yaml
observability:

  required:
    - target state before execution
    - commit response
    - target state after execution
```

If completion cannot be observed, confidence must be bounded accordingly.

---

# 192. Blind Spots

Known blind spots should be preserved.

Example:

```yaml
blind_spots:
  - downstream receiver state unavailable
```

Then:

```text
SEND SUCCESS
```

must not become:

```text
RECEIVER SUCCESS
```

---

# 193. Task Audit Record

A completed consequential task should be auditable through at least:

```text
TASK ID

TASK VERSION

SOURCE REQUEST

OBJECTIVE

SCOPE

CONSTRAINTS

INPUT PROVENANCE

KEY DECISIONS

EFFECTS

COMPLETION STATE

INVALIDATION CONDITIONS
```

where applicable.

---

# 194. Anti-Fabrication Rules

Never perform these transformations:

```text
MISSING OBJECTIVE
→
INVENTED OBJECTIVE
```

```text
UNKNOWN TARGET
→
GUESSED TARGET
```

```text
MISSING AUTHORITY
→
ASSUMED AUTHORITY
```

```text
MISSING EVIDENCE
→
PLAUSIBLE STORY
```

```text
UNCLEAR SCOPE
→
UNBOUNDED SCOPE
```

```text
SOURCE CLAIM
→
VERIFIED FACT
```

```text
MODEL
→
EMPIRICAL OBSERVATION
```

```text
NO CONTRADICTION FOUND
→
PROOF
```

---

# 195. Anti-Overreach Rules

Never silently generalize:

```text
ONE SYSTEM
→
ALL SYSTEMS
```

```text
ONE REGIME
→
ALL REGIMES
```

```text
ONE SCALE
→
ALL SCALES
```

```text
ONE TIME
→
ALL TIMES
```

```text
STRUCTURAL SIMILARITY
→
CAUSATION
```

---

# 196. Optimization Law

Optimization occurs only after integrity constraints are satisfied.

```text
INTEGRITY
>
COMPLETENESS
>
FLUENCY
>
SPEED
>
TOKEN SAVINGS
```

Optimization may reduce:

```text
latency

retrieval

reasoning branches

tool calls

context
```

but must not weaken task correctness.

---

# 197. Task Contract Anti-Regression Gate

A Task Contract optimization is acceptable only if it preserves or improves:

```text
OBJECTIVE FIDELITY

SCOPE CORRECTNESS

CONSTRAINT VISIBILITY

PROVENANCE

CONTRADICTION VISIBILITY

CAUSAL DISCIPLINE

AUTHORITY BOUNDARIES

SAFETY

REPAIRABILITY

COMPLETION ACCURACY

USER FIT
```

---

# 198. Minimal Machine-Oriented Form

```yaml
task_contract:

  id:
  version:

  objective:

  deliverable:

  scope:
    include: []
    exclude: []

  inputs:
    required: []

  constraints:
    hard: []
    soft: []

  freshness:

  stakes:

  effects:
    allowed: []
    prohibited: []

  dependencies: []

  gaps: []

  completion_conditions: []

  invalidation_conditions: []

  status:
```

---

# 199. Extended Machine-Oriented Form

```yaml
task_contract:

  schema_version:

  identity:
    task_id:
    task_version:
    root_task_id:
    parent_task_id:
    correlation_id:

  source:
    type:
    principal:
    timestamp:
    reference:
    provenance:

  objective:
    primary:
    secondary: []
    class:
    success_definition:

  deliverable:
    type:
    format:
    destination:
    acceptance_criteria: []

  scope:
    include: []
    exclude: []
    system:
    population:
    environment:
    scale:
    time:
    regime:
    measurement:
    assumptions:

  inputs:
    required: []
    optional: []
    prohibited: []

  assumptions:
    load_bearing: []
    noncritical: []

  constraints:
    hard: []
    soft: []

  freshness:
    requirement:
    maximum_age:
    valid_until:
    triggers: []

  stakes:
    reversibility:
    financial:
    legal:
    health:
    safety:
    institutional:
    exposure:
    dependency_fanout:

  uncertainty:
    evidence:
    model:
    scope:
    temporal:
    causal:
    execution:
    provenance_independence:

  epistemic:
    required_conclusion_class:
    causal_requirement:
    competing_hypotheses_allowed:

  capabilities:
    anticipated: []

  authority:
    anticipated: []

  effects:
    allowed: []
    prohibited: []
    expected: []
    reversibility_requirement:

  information_exposure:
    allowed:
    prohibited:
    declassification_required:

  dependencies:
    tasks: []
    evidence: []
    state: []
    systems: []

  observability:
    required: []
    blind_spots: []

  recovery:
    required:
    allowed_classes: []

  completion:
    claim_sufficiency:
    decision_sufficiency:
    action_sufficiency:
    conditions: []

  invalidation:
    conditions: []
    expiry:
    regime_shift: []

  provenance:
    lineage:
    transformations: []

  state:
    status:
    blocking_gaps: []
```

---

# 200. Canonical Compression

```text
TASK CONTRACT
=
THE BOUNDED SEMANTIC AGREEMENT
THAT DEFINES
WHAT WORK AMOS OS
IS ACTUALLY ATTEMPTING TO PERFORM.

A REQUEST
IS NOT YET A TASK.

A TASK
MUST IDENTIFY
ITS OBJECTIVE,
DELIVERABLE,
SCOPE,
CONSTRAINTS,
INPUTS,
LOAD-BEARING ASSUMPTIONS,
FRESHNESS,
STAKES,
EFFECT ENVELOPE,
DEPENDENCIES,
AND COMPLETION CONDITIONS
WHEN THOSE DIMENSIONS ARE MATERIAL.

THE TASK MUST PRESERVE
ITS ORIGIN.

IT MUST NOT
SILENTLY EXPAND SCOPE.

IT MUST NOT
INVENT MISSING INPUTS.

IT MUST NOT
DROP HARD CONSTRAINTS.

IT MUST NOT
CONFUSE CAPABILITY
WITH AUTHORITY.

IT MUST NOT
CONFUSE TASK VALIDITY
WITH POLICY PERMISSION.

IT MUST NOT
CONFUSE TOOL SUCCESS
WITH OBJECTIVE SUCCESS.

IT MUST NOT
FORCE COMPETING HYPOTHESES
TO CONVERGE.

IT MUST NOT
GENERALIZE BEYOND
ITS APPLICABILITY ENVELOPE.

WHEN LOAD-BEARING STATE CHANGES,
REVALIDATE
ONLY THE DEPENDENT CLOSURE.

WHEN A CRITICAL GAP EXISTS,
BLOCK CONSEQUENTIAL EXECUTION
UNTIL THE GAP IS CLOSED
OR A SAFE GOVERNED ALTERNATIVE EXISTS.

WHEN UNCERTAINTY REMAINS,
PREFER
REVERSIBLE,
OBSERVABLE,
REPAIRABLE ACTION.

USE
THE SMALLEST SUFFICIENT
PROOF SCOPE.

STOP
WHEN THE REQUIRED
CLAIM,
DECISION,
OR ACTION
IS SUFFICIENTLY SUPPORTED.

AND NEVER ALLOW
SPEED,
FLUENCY,
OR OPTIMIZATION
TO CHANGE
WHAT THE TASK
ACTUALLY MEANS.
```

---

# 201. Master Contract

Formally, at the conceptual level:

```text
TaskContract
=
(
  Identity,
  Origin,
  Objective,
  Deliverable,
  Scope,
  Inputs,
  Assumptions,
  Constraints,
  Freshness,
  Stakes,
  Uncertainty,
  Effects,
  Dependencies,
  Completion,
  Invalidation,
  Provenance
)
```

The Task Contract is sufficient only when:

```text
ObjectiveBound
∧
ScopeBound
∧
HardConstraintsKnown
∧
CriticalInputsResolved
∧
CriticalGapsResolved
∧
CompletionDefined
```

with additional conditions activated according to stakes and effect class.

---

# 202. Final Law

```text
NO TASK MAY BECOME
A CONSEQUENTIAL EFFECT
MERELY BECAUSE
THE REQUEST SOUNDS CLEAR.

FIRST BIND
THE OBJECTIVE.

THEN BIND
THE SCOPE.

THEN BIND
THE CONSTRAINTS.

THEN IDENTIFY
THE LOAD-BEARING DEPENDENCIES.

THEN EXPOSE
THE GAPS.

THEN DETERMINE
WHAT COMPLETION MEANS.

ONLY THEN
MAY THE REST OF
THE CONTROL PLANE
DECIDE
WHETHER,
HOW,
AND UNDER WHOSE AUTHORITY
THE TASK MAY PROCEED.
```

# END — AMOS OS TASK CONTRACT

```

This is a **substantive candidate specification**, not a claim that these structures are already implemented or empirically validated. That distinction matters because the current repository file contains only the misplaced `K COUNTERFACTUAL` placeholder, so there is no existing substantive `TASK_CONTRACT.md` canon to reproduce verbatim. :contentReference[oaicite:2]{index=2}

The placement itself is supported by the repository: `TASK_CONTRACT.md` belongs in `03_CONTROL_PLANE/01_TASK_CONTRACT`, paired with `TASK_RESOLVER.md`, rather than in the Kernel cognition area. :contentReference[oaicite:3]{index=3}
```
