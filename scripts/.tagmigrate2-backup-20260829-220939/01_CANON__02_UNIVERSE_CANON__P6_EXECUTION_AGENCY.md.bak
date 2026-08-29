---
artifact_kind: UNIVERSE_PLANE
epistemic_class: AMOS_MODEL
origin_architect: Trang Phan
plane: 01_CANON
rscf:
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: universe_canon
  state: SOURCE_CLAIM
source: 01_CANON/02_UNIVERSE_CANON
steward: Trang Phan
system: AMOS OS
tags:
- amos-os
- canon
- universe_canon
- execution
- agency
- action
- commit
- rollback
- effects
- p6_plane
- rscf
- canon/universe
- 00-root-moc
- amos-moc
- amos-7-part-universe-canon
- hml-canon
- 00-home
- amos-rscf-nodes
- p1-reality-environment
- p2-sense-evidence
- p3-knowledge-memory
- p4-cognition-models
- p5-governance-authority
- 02-universe-canon-moc
title: P6 EXECUTION AGENCY
type: note
version: 0.2.0
---

# P6 Execution / Agency

**Class:** `CANON_MODEL`

**Epistemic class:** `AMOS_MODEL`

**Origin architect / steward:** Trang Phan

**Specification status:** `PROPOSED_SPECIFICATION`

**Canonical status:** `CONDITIONAL`

**Execution authority:** `NONE_UNTIL_PROMOTED`

**Implementation status:** `PARTIAL_OR_UNKNOWN`

---

# 1. Purpose

`P6 Execution / Agency` defines the AMOS plane that converts **authorized intent** into controlled effects.

P5 answers:

```text
May this action occur?
Who has authority?
Under what governance?
```

P6 answers:

```text
How does an authorized action
actually become an effect?

Which worker performs it?

Which execution context applies?

How is duplicate execution prevented?

How is cost bounded?

How is effect state recorded?

How is outcome verified?

How is partial failure handled?

How is rollback or compensation performed?

How are retries made safely?

How are concurrent effects coordinated?

How is causal order preserved?

What proof exists that a commit occurred?

What remains uncertain after execution?
```

The canonical transition is:

```text
AUTHORIZED INTENT
        ↓
EXECUTION REQUEST
        ↓
WORKER GATE
        ↓
CAPABILITY / AUTHORITY CHECK
        ↓
BUDGET CHECK
        ↓
IDEMPOTENCY CHECK
        ↓
TRANSACTION / EFFECT PLAN
        ↓
EXECUTION
        ↓
COMMIT
        ↓
RECEIPT
        ↓
OBSERVATION
        ↓
VERIFICATION
        ↓
CLOSE / RETRY / COMPENSATE / ROLLBACK
```

---

# 2. Canonical Questions

P6 must always be able to answer:

```text
What stands between "allowed" and "done"?

What concrete actor performs the effect?

Which worker path is governed?

What capability is required?

What authority was resolved upstream?

What resource budget remains?

What is the idempotency identity?

What happens if the same command arrives twice?

What constitutes a commit?

What receipt proves that commit?

Where is that receipt retained?

Can the effect be reversed?

If not reversible, can it be compensated?

What happens if execution partially succeeds?

What happens if the worker crashes after effect but before acknowledgement?

What happens if acknowledgement occurs but effect did not?

How are concurrent commands ordered?

When is an execution final?

What state proves completion?

What state proves failure?

How is cost attributed to a principal?

How is misuse detected?

How is agency suspended or revoked?
```

---

# 3. Foundational Boundary

Mandatory:

```text
AUTHORIZED
!=
EXECUTED
```

```text
EXECUTION_REQUEST
!=
EFFECT
```

```text
EFFECT
!=
VERIFIED_OUTCOME
```

```text
COMMIT
!=
SUCCESS
```

P6 exists precisely because permission and reality are separated by an execution process that can fail.

---

# 4. Execution Definition

Within P6:

```text
Execution
=
the governed transformation
of an authorized request
into attempted state change
through an approved effect path.
```

Execution is therefore not simply:

```text
run code
```

It includes:

```text
authority binding
worker selection
resource control
idempotency
transaction semantics
effect observation
receipt emission
failure handling
accountability
```

---

# 5. Agency Definition

Within P6:

```text
Agency
=
the bounded operational capacity
of an identified principal or worker
to cause state transitions
through authorized effect interfaces.
```

Agency is not synonymous with intelligence.

Mandatory:

```text
COGNITION
!=
AGENCY
```

```text
AGENCY
!=
UNBOUNDED AUTONOMY
```

---

# 6. Agency Requires Authority

Conceptually:

```text
AgencyEffective
=
Capability
∩
Authority
∩
AvailableResources
∩
ExecutionPath
```

If any required element is absent:

```text
EFFECTFUL_AGENCY
=
BLOCKED
```

---

# 7. P6 Authority Boundary

This specification explicitly preserves:

```text
execution_authority: NONE
```

until the relevant promotion/governance process grants more.

Therefore:

```text
P6 ARCHITECTURE EXISTS
```

does not imply:

```text
P6 MAY EXECUTE
```

---

# 8. External Executor Boundary

The AMOS Full Brain architecture does not itself grant autonomous world action.

Therefore the safe relation is:

```text
AMOS
→ authorized request
→ governed external executor / worker
→ effect
```

not:

```text
AMOS reasoning
→ unrestricted effect
```

---

# 9. Execution Request

Recommended representation:

```yaml
execution_request:

  request_id: null

  principal_id: null

  authority_ref: null

  governance_ref: null

  target: null

  operation: null

  parameters: {}

  target_version: null

  environment: null

  regime: null

  idempotency_key: null

  budget_ref: null

  deadline: null

  priority: null

  rollback_ref: null

  provenance_refs: []

  status: REQUESTED
```

---

# 10. Intent vs Request

Intent may express:

```text
desired future state
```

A request expresses:

```text
specific executable operation
```

Mandatory:

```text
INTENT
!=
EXECUTION_REQUEST
```

---

# 11. Request Validation

Before effect:

```text
resolve request identity
check target
check operation
check authority
check policy
check parameters
check budget
check idempotency
check environment
```

---

# 12. Worker

A worker is a bounded execution principal responsible for performing an approved class of effects.

Examples may include:

```text
service worker
deployment worker
file writer
database transaction worker
external executor
human-operated executor
```

Exact worker classes remain implementation-specific.

---

# 13. Worker Gate — P6-1

Source-supplied law:

```text
P6-1 Worker Gate
```

declares:

```text
consequential effects
only via governed worker paths
```

with declared reference:

```text
I-RPOL-017
```

The exact normative definition of `I-RPOL-017` must be resolved from its canonical source before claiming full implementation compliance.

---

# 14. Worker Gate Principle

Conceptually:

```text
AuthorizedIntent
→
ApprovedWorkerPath
→
Effect
```

No bypass path should be treated as canonical execution.

---

# 15. Worker Registration

A worker should be addressable through:

```yaml
worker:

  worker_id: null

  worker_class: null

  principal_ref: null

  capabilities: []

  authority_ceiling: null

  supported_operations: []

  supported_targets: []

  environments: []

  execution_limits: {}

  budget_class: null

  isolation_class: null

  status: null
```

---

# 16. Worker Capability

Capability defines:

```text
what the worker can technically perform
```

Authority defines:

```text
what the worker is permitted to perform
```

Mandatory:

```text
WORKER_CAPABILITY
!=
WORKER_AUTHORITY
```

---

# 17. Worker State

Suggested:

```text
UNREGISTERED

DISABLED

READY

LEASED

BUSY

DRAINING

SUSPENDED

FAILED

REVOKED

RETIRED
```

---

# 18. Worker Lease

A worker may receive temporary authorization to execute a job.

Recommended:

```yaml
worker_lease:

  lease_id: null

  worker_id: null

  request_id: null

  authority_ref: null

  acquired_at: null

  expires_at: null

  renewable: null

  status: null
```

---

# 19. Lease Boundary

```text
WORKER EXISTS
!=
WORKER CURRENTLY LEASED
```

---

# 20. Lease Expiry

A worker should not continue initiating new effects under an expired lease unless protocol explicitly permits safe completion.

---

# 21. Job

A job is a scheduled unit of execution.

```yaml
job:

  job_id: null

  request_ref: null

  worker_ref: null

  attempt: 0

  idempotency_key: null

  state: QUEUED

  created_at: null

  started_at: null

  completed_at: null
```

---

# 22. Job State Machine

Suggested:

```text
CREATED
↓
QUEUED
↓
LEASED
↓
RUNNING
↓
PREPARED
↓
COMMITTING
↓
COMMITTED
↓
VERIFYING
↓
VERIFIED
```

Failure branches:

```text
FAILED

TIMED_OUT

CANCELLED

UNKNOWN_EFFECT_STATE

COMPENSATING

ROLLED_BACK

QUARANTINED
```

---

# 23. State Transition Discipline

Workers should not skip semantic states if doing so would destroy accountability.

Example:

```text
RUNNING
→
VERIFIED
```

without an identifiable effect/commit state may be insufficient for consequential operations.

---

# 24. Execution Context

Every effect should bind to relevant:

```text
environment

regime

principal

authority

target version

worker

budget

transaction

time
```

---

# 25. Execution Context Object

```yaml
execution_context:

  context_id: null

  request_id: null

  principal_id: null

  worker_id: null

  authority_ref: null

  environment_ref: null

  regime: null

  target_ref: null

  target_version: null

  transaction_ref: null

  budget_ref: null

  deadline: null
```

---

# 26. Environment Match

An operation validated in one environment should not silently execute in another.

Mandatory:

```text
AUTHORIZED_FOR_ENV_A
!=
AUTHORIZED_FOR_ENV_B
```

---

# 27. Version Binding

Execution should target the exact material state approved upstream.

If approved against:

```text
Object@v7
```

but execution finds:

```text
Object@v8
```

then:

```text
STALE_EXECUTION_REQUEST
```

unless transition explicitly tolerates version drift.

---

# 28. CAS Concept

Conceptually:

```text
if CurrentVersion == ExpectedVersion:
    commit
else:
    reject / replan
```

This reflects compare-and-swap reasoning discipline.

It does not assert a literal implementation unless evidenced.

---

# 29. MVCC Concept

P6 may conceptually preserve multiple state versions to avoid destructive concurrent overwrites.

Exact MVCC implementation remains a gap unless source/implementation defines it.

---

# 30. Transaction

A transaction groups state changes that require shared commit semantics.

Recommended:

```yaml
transaction:

  transaction_id: null

  request_id: null

  principal_id: null

  operations: []

  read_set: []

  write_set: []

  expected_versions: []

  state: OPEN

  commit_ref: null

  rollback_ref: null
```

---

# 31. Transaction Boundary

```text
MULTIPLE OPERATIONS
!=
TRANSACTION
```

unless atomicity/consistency semantics are actually defined.

---

# 32. Atomicity

Atomic intent means:

```text
all required effects commit
```

or:

```text
the intended transaction does not become authoritative
```

when the system supports such semantics.

---

# 33. Atomicity Boundary

External distributed effects may not support literal rollback.

P6 must distinguish:

```text
ATOMIC TRANSACTION
```

from:

```text
BEST-EFFORT ORCHESTRATION
```

---

# 34. Atomic Multi-Effect Execution

Where multiple effects form one logical commitment:

```text
Effect A
Effect B
Effect C
```

partial success must not silently be reported as full success.

---

# 35. Partial Failure

Example:

```text
A = committed
B = failed
C = not attempted
```

must produce:

```text
PARTIAL_FAILURE
```

or a more specific typed state.

---

# 36. Compensation

Where effects cannot be literally rolled back, a compensating effect may restore acceptable state.

Mandatory:

```text
COMPENSATION
!=
ROLLBACK
```

---

# 37. Rollback

Rollback restores a prior state using reversible state history.

---

# 38. Compensation Object

```yaml
compensation:

  compensation_id: null

  original_effect_ref: null

  compensating_operation: null

  authority_ref: null

  expected_result: null

  actual_result: null

  status: null
```

---

# 39. Rollback Object

```yaml
rollback:

  rollback_id: null

  transaction_ref: null

  target_prior_state: null

  required_authority: null

  prerequisites: []

  started_at: null

  completed_at: null

  result: null
```

---

# 40. Irreversible Effect

An effect is irreversible when the prior state cannot be reliably restored.

Such effects require stronger P5 governance and P6 execution safeguards.

---

# 41. Irreversible Effect Gate

Before execution require stronger checks for:

```text
authority

validation

dependency impact

budget

recipient/target identity

parameter verification

final confirmation
```

where stakes justify them.

---

# 42. Commit

A commit is the transition at which an intended effect becomes authoritative within the effect domain.

---

# 43. Commit Boundary

Mandatory:

```text
ATTEMPTED
!=
COMMITTED
```

---

# 44. Commit Point

Each consequential worker path should define its commit point.

Without a commit definition:

```text
COMMIT_STATE
=
UNKNOWN/GAP
```

---

# 45. Commit Record

```yaml
commit:

  commit_id: null

  transaction_id: null

  worker_id: null

  principal_id: null

  effect_refs: []

  committed_at: null

  previous_state_ref: null

  resulting_state_ref: null

  receipt_ref: null

  digest: null
```

---

# 46. Receipt Everything — P6-2

Source-supplied law:

```text
P6-2 Receipt Everything
```

declares:

```text
commits emit digests
to append-only ledger
```

with declared references:

```text
INV-031
INV-035
```

The exact definitions and test requirements of these invariant IDs remain dependent on their canonical source artifacts.

---

# 47. Receipt

A receipt is a persistent record that a specific execution transition was reported as committed.

Recommended:

```yaml
receipt:

  receipt_id: null

  request_id: null

  transaction_id: null

  commit_id: null

  principal_id: null

  worker_id: null

  target: null

  operation: null

  effect_digest: null

  before_digest: null

  after_digest: null

  timestamp: null

  ledger_ref: null

  provenance_refs: []
```

---

# 48. Receipt Boundary

Mandatory:

```text
RECEIPT
!=
EXTERNAL REALITY ITSELF
```

A receipt proves that a particular execution path recorded a commit under its semantics.

Independent observation may still be required to verify external effect.

---

# 49. Receipt vs Verification

```text
COMMIT_RECEIPT
!=
OUTCOME_VERIFICATION
```

---

# 50. Digest

A digest may bind receipt to content/state.

Mandatory:

```text
DIGEST_MATCH
!=
SEMANTIC_CORRECTNESS
```

A hash proves identity/integrity properties, not that the operation was appropriate.

---

# 51. Append-Only Ledger

The source proposal requires an append-only ledger for commit digests.

Conceptually:

```text
Receipt_1
Receipt_2
Receipt_3
...
```

where prior records are not silently rewritten.

---

# 52. Ledger Boundary

```text
APPEND_ONLY
!=
IMMUTABLE UNDER ALL THREAT MODELS
```

unless implementation and security guarantees establish stronger properties.

---

# 53. Ledger Record

```yaml
ledger_entry:

  sequence: null

  receipt_ref: null

  receipt_digest: null

  parent_digest: null

  recorded_at: null

  writer_ref: null
```

Exact chaining requirements remain source-dependent.

---

# 54. Ledger Integrity

A ledger should allow detection of:

```text
missing receipt

modified receipt

reordered receipt

duplicate receipt
```

to the extent supported by implementation.

---

# 55. Persistent Provenance

Receipt lineage should connect:

```text
proposal
→ approval
→ request
→ worker
→ transaction
→ commit
→ receipt
→ verification
```

---

# 56. Provenance Closure

Consequential effects should be reconstructable without depending on hidden internal reasoning.

---

# 57. Idempotency

Idempotency protects against duplicate logical effects.

Conceptually:

```text
Execute(K, X)
+
Execute(K, X)
=
one logical effect
```

for idempotency key `K` under defined semantics.

---

# 58. Idempotency Boundary

Mandatory:

```text
RETRYABLE
!=
IDEMPOTENT
```

---

# 59. Idempotency Key

Recommended:

```yaml
idempotency:

  key: null

  principal_id: null

  operation: null

  target: null

  request_digest: null

  valid_until: null

  previous_result_ref: null
```

---

# 60. Idempotency Scope

A key should be scoped sufficiently to prevent accidental collisions.

Possible dimensions:

```text
principal

operation

target

time window

request digest
```

---

# 61. Duplicate Request

If same idempotency identity returns:

```text
same request
```

worker should reuse prior result where semantics permit.

---

# 62. Key Reuse Conflict

If the same key is used with materially different payload:

```text
IDEMPOTENCY_CONFLICT
```

should block or quarantine execution.

---

# 63. Retry

Retries may occur because of:

```text
timeout

transient network error

worker crash

dependency unavailability

temporary contention
```

---

# 64. Retry Safety

Before retry, determine:

```text
did effect happen?

did commit happen?

was receipt written?

is operation idempotent?

can state be safely re-read?
```

---

# 65. Unknown Effect State

Critical execution state:

```text
UNKNOWN_EFFECT_STATE
```

Example:

```text
worker sent irreversible external request
then connection failed
before acknowledgement
```

Do not automatically retry unless duplication is safe.

---

# 66. Exactly-Once Boundary

Distributed systems may provide:

```text
at-least-once delivery

at-most-once delivery

effectively-once logical semantics
```

under conditions.

P6 should not claim literal universal exactly-once execution unless implementation proves it.

---

# 67. Delivery vs Effect

Mandatory:

```text
MESSAGE DELIVERED ONCE
!=
EFFECT OCCURRED ONCE
```

---

# 68. Deduplication

Deduplication identifies repeated logical requests.

It should bind to logical identity rather than surface formatting alone.

---

# 69. Replay

A replay is reprocessing prior command/event.

Replay may be:

```text
intentional recovery

audit simulation

malicious duplicate

accidental retry
```

---

# 70. Replay Protection

Effectful commands should reject stale/unauthorized replays where relevant.

---

# 71. Budgeted Action — P6-3

Source-supplied law:

```text
P6-3 Budgeted Action
```

declares:

```text
cumulative cost accounting
per principal
```

with declared reference:

```text
INV-041
```

The exact invariant definition, units, limits, and required accounting semantics must be resolved from its canonical source.

---

# 72. Budget

A budget limits permitted resource consumption.

Possible dimensions:

```text
money

compute

tokens

API calls

time

energy

memory

bandwidth

effect count

risk capacity
```

---

# 73. Budget Object

```yaml
budget:

  budget_id: null

  principal_id: null

  resource_class: null

  limit: null

  consumed: null

  reserved: null

  available: null

  period_start: null

  period_end: null

  policy_ref: null

  status: null
```

---

# 74. Principal Accounting

Cost should be attributable to an identified principal or governed execution identity.

---

# 75. Cumulative Accounting

Conceptually:

```text
Cost_principal(t)
=
Σ committed_costs
+
Σ reserved_costs
-
Σ released_reservations
```

Exact accounting semantics remain implementation-specific.

---

# 76. Budget Reservation

Before execution, resources may be reserved.

```text
AVAILABLE
→
RESERVED
→
CONSUMED
```

or:

```text
RESERVED
→
RELEASED
```

---

# 77. Reservation Boundary

```text
RESERVED
!=
CONSUMED
```

---

# 78. Budget Overrun

If actual cost exceeds reservation:

```text
BUDGET_OVERRUN
```

must be surfaced.

---

# 79. Budget Gate

Before execution:

```text
EstimatedCost
<=
AvailableBudget
```

where budget policy requires it.

---

# 80. Cost Estimation

Cost estimate should retain uncertainty when actual cost is variable.

---

# 81. Budget Exhaustion

When budget reaches its limit:

```text
BLOCK
THROTTLE
ESCALATE
```

according to policy.

---

# 82. Budget Is Not Authority

Mandatory:

```text
AVAILABLE_BUDGET
!=
AUTHORIZATION
```

---

# 83. Authority Is Not Budget

Likewise:

```text
AUTHORIZED
!=
FUNDED
```

---

# 84. Quota

Quota limits quantity of a resource/action.

Budget and quota may overlap but should not be assumed identical.

---

# 85. Rate Limit

Controls consumption per time window.

---

# 86. Concurrency Limit

Controls simultaneous operations.

---

# 87. Resource Isolation

One principal should not consume another principal's budget without explicit transfer/governance.

---

# 88. Budget Transfer

Any transfer between principals should itself be governed and receipted where material.

---

# 89. Agency Budget

Agency may be bounded not only by permission but by resource envelope.

Conceptually:

```text
EffectiveAgency
=
AuthorizedActions
∩
AffordableActions
∩
ExecutableActions
```

---

# 90. Execution Deadline

A request may expire before execution.

Expired request:

```text
DEADLINE_EXCEEDED
```

should not begin unless policy explicitly permits late execution.

---

# 91. Timeout

Timeout means an expected execution phase exceeded its time bound.

Mandatory:

```text
TIMEOUT
!=
CONFIRMED FAILURE
```

The effect may already have occurred.

---

# 92. Cancellation

Cancellation attempts to prevent future execution.

Mandatory:

```text
CANCEL_REQUESTED
!=
CANCELLED
```

---

# 93. Cancellation Boundary

Once commit passes an irreversible point, cancellation may be impossible.

---

# 94. Kill vs Cancel

Forcefully terminating a worker may leave external effects in unknown state.

Therefore:

```text
KILL_WORKER
!=
ROLLBACK_EFFECT
```

---

# 95. Worker Crash

A worker crash should be classified by execution phase.

Examples:

```text
before effect

during effect

after effect before commit record

after commit before receipt

after receipt before verification
```

These cases require different recovery.

---

# 96. Crash Recovery

Recovery should begin from persisted execution state, not assumption.

---

# 97. Durable Intent

Where needed, execution intent should be persisted before effect to support crash reconstruction.

---

# 98. Durable Receipt

Where required, receipt should survive worker restart.

---

# 99. Recovery Object

```yaml
recovery:

  recovery_id: null

  request_id: null

  last_known_state: null

  observed_effect_state: null

  receipt_state: null

  safe_next_actions: []

  selected_action: null
```

---

# 100. Concurrency

Two workers may target shared state simultaneously.

P6 should explicitly handle:

```text
write/write conflict

read/write conflict

duplicate request

shared-budget contention

ordering dependency
```

---

# 101. Concurrent Authority

Two principals may both be authorized but still conflict operationally.

P5 permission does not eliminate P6 coordination need.

---

# 102. Serialization

Certain transitions may require a total or partial order.

---

# 103. Causal Order

If:

```text
B depends on A
```

then:

```text
B must not finalize
before required A state is finalized
```

---

# 104. Causal Epoch

A conceptual causal epoch may group effects sharing a dependency/finality boundary.

Exact runtime implementation remains source-dependent.

---

# 105. Finality

An effect is final when the execution system considers its authoritative state no longer subject to ordinary rollback/reordering under that protocol.

---

# 106. Finality Boundary

```text
FINAL
!=
UNCHANGEABLE FOREVER
```

A future governed transition may supersede it.

---

# 107. Shard-Local Finalization

Where an effect has local dependency closure, it may finalize locally if:

```text
authority valid

dependencies local

no unresolved cross-shard conflict

receipt durable

required invariants hold
```

This is a reasoning/architecture pattern unless implementation establishes literal shards.

---

# 108. Coordination Avoidance

P6 should avoid global coordination when local proof of safe execution is sufficient.

But:

```text
COORDINATION AVOIDANCE
MUST NOT
WEAKEN INTEGRITY
```

---

# 109. Escalate Coordination When

```text
shared mutable state

shared budgets

cross-root dependency

causal coupling

atomic multi-effect transition

global invariant

irreversible effect

ambiguous execution ownership
```

exists.

---

# 110. Effect

An effect is an observed or committed change attributable to an execution attempt.

---

# 111. Effect Object

```yaml
effect:

  effect_id: null

  request_id: null

  worker_id: null

  target: null

  operation: null

  intended_state: null

  observed_state: null

  commit_state: null

  reversible: null

  receipt_ref: null

  verification_ref: null
```

---

# 112. Intended Effect vs Actual Effect

Mandatory:

```text
INTENDED_EFFECT
!=
ACTUAL_EFFECT
```

---

# 113. Side Effect

Any materially relevant change outside the declared target effect.

Side effects should be surfaced when consequential.

---

# 114. Hidden Side Effect

An effect may occur outside current observability.

Therefore:

```text
NO OBSERVED SIDE EFFECT
!=
NO SIDE EFFECT
```

---

# 115. Effect Scope

Each execution should declare expected blast radius.

---

# 116. Blast Radius

Conceptually:

```text
BlastRadius
=
set of potentially affected states/systems
```

---

# 117. Blast-Radius Gate

Large blast radius should trigger stronger P5/P6 controls.

---

# 118. Sandboxed Execution

A sandbox restricts effect scope.

Mandatory:

```text
SANDBOX
!=
PRODUCTION
```

---

# 119. Dry Run

A dry run predicts or simulates an effect without committing the real target state.

Mandatory:

```text
DRY_RUN_SUCCESS
!=
REAL_EXECUTION_SUCCESS
```

---

# 120. Preview

A preview shows proposed changes prior to commit.

---

# 121. Plan

An execution plan enumerates expected operations before effect.

```yaml
execution_plan:

  plan_id: null

  request_id: null

  operations: []

  expected_effects: []

  risks: []

  budget_estimate: null

  rollback_ref: null

  approval_ref: null
```

---

# 122. Plan/Execution Boundary

```text
PLAN
!=
EXECUTION
```

---

# 123. Determinism

A worker may be deterministic under specified inputs/environment.

Do not assume:

```text
same request
→ same result
```

when environment is nondeterministic or external.

---

# 124. Non-Deterministic Execution

Should preserve enough context to understand result variance.

---

# 125. Randomness

If randomness affects effect:

```text
seed

source

distribution
```

should be recorded where reproducibility matters.

---

# 126. Execution Provenance

Minimum:

```text
request

principal

authority

worker

target

version

parameters

time

environment

receipt

verification
```

---

# 127. Agency Provenance

For every consequential effect, AMOS should be able to answer:

```text
who caused this?

under whose authority?

through which worker?

because of which request?
```

---

# 128. Accountability

Accountability requires a reconstructable mapping:

```text
Principal
→ Authority
→ Request
→ Worker
→ Effect
→ Receipt
→ Outcome
```

---

# 129. Outcome Verification

After commit:

```text
observe target
compare with intended result
```

---

# 130. Verification Object

```yaml
effect_verification:

  verification_id: null

  effect_ref: null

  observation_refs: []

  expected_state: null

  observed_state: null

  verifier: null

  method: null

  result: null

  verified_at: null
```

---

# 131. Verification State

Suggested:

```text
UNVERIFIED

VERIFYING

VERIFIED

MISMATCH

PARTIALLY_VERIFIED

UNOBSERVABLE

UNKNOWN
```

---

# 132. Verification Boundary

Mandatory:

```text
RECEIPT PRESENT
!=
EFFECT VERIFIED
```

---

# 133. Independent Verification

For high-stakes actions, verifier may need independence from executor.

---

# 134. Self-Verification Risk

A worker claiming its own success may be insufficient when independent observation is required.

---

# 135. Observability

P6 execution should emit sufficient operational state to diagnose:

```text
start

progress

commit

failure

retry

compensation

budget usage

receipt generation
```

---

# 136. Execution Telemetry

Potential:

```text
latency

attempt count

cost

worker identity

failure code

transaction state

receipt state

verification state
```

---

# 137. Telemetry Boundary

```text
TELEMETRY
!=
GOVERNANCE RECEIPT
```

unless protocol explicitly makes it authoritative.

---

# 138. Event

An execution event records a state transition.

```yaml
execution_event:

  event_id: null

  request_id: null

  event_type: null

  previous_state: null

  next_state: null

  timestamp: null

  actor: null

  digest: null
```

---

# 139. Event Ordering

Event sequence should preserve causal ordering where material.

---

# 140. Duplicate Events

Event duplication should not necessarily cause duplicate effects.

---

# 141. Event Replay

Replay should be safe only when handlers are explicitly designed for it.

---

# 142. Audit Trail

Execution audit should allow reconstruction without hidden chain-of-thought.

Use:

```text
request
authority
worker
transaction
effect
receipt
verification
```

---

# 143. Agency vs Autonomous Agency

P6 agency is operational.

It does not establish:

```text
subjective intention

conscious agency

independent moral agency
```

---

# 144. Agent Execution

An AMOS agent may only execute where P5 grants appropriate authority and P6 provides governed worker path.

---

# 145. Agent Default

Until explicit promotion:

```text
agent_execution_authority:
  NONE
```

or at most:

```text
PROPOSE_ONLY
```

depending on the surrounding agent contract.

---

# 146. Agent Self-Elevation Firewall

Mandatory:

```text
AGENT
MUST NOT
CREATE
ITS OWN EXECUTION AUTHORITY
```

---

# 147. Worker Self-Elevation Firewall

A worker may not widen:

```text
operation set

target scope

budget

authority

environment
```

on its own.

---

# 148. Tool Execution

Tool availability is a capability fact.

It is not sufficient authority.

---

# 149. Tool Invocation Contract

Conceptually:

```text
ToolCall
=
Request
+
Authority
+
Parameters
+
ExecutionContext
```

for effectful tools.

---

# 150. Human Execution

A human may serve as external executor.

The AMOS receipt chain should distinguish:

```text
AMOS recommendation
```

from:

```text
human decision
```

and:

```text
human execution
```

---

# 151. Workflow Execution

A workflow may coordinate multiple workers.

Workflow state must not conceal individual worker effects.

---

# 152. Workflow Object

```yaml
workflow_execution:

  execution_id: null

  workflow_ref: null

  request_ref: null

  steps: []

  dependencies: []

  current_state: null

  receipts: []

  rollback_ref: null
```

---

# 153. Workflow Step

Each consequential step should have its own:

```text
authority binding

idempotency

effect state

receipt
```

where required.

---

# 154. Saga Pattern

For non-atomic distributed workflows:

```text
step
→ commit
→ compensation path
```

may be used conceptually.

Do not label it a literal implementation unless source/runtime confirms it.

---

# 155. Deployment Execution

Deployment is a specialized P6 effect.

It should bind:

```text
artifact version

environment

authority

validation

rollback

observability
```

---

# 156. Deployment Receipt

Should identify exact artifact/environment state committed.

---

# 157. File-System Execution

For filesystem effects, capture:

```text
logical target

path

prior version/hash

new version/hash

authority

receipt
```

where implementation supports it.

---

# 158. Data Mutation

Database or knowledge-store mutation should preserve:

```text
transaction identity

expected version

write set

commit result

receipt
```

---

# 159. Canon Mutation

Canon mutation is both:

```text
P5 governance transition
```

and:

```text
P6 execution effect.
```

Both layers are required.

---

# 160. Canon Commit Boundary

A proposal file becoming available does not mean canon state changed.

---

# 161. Execution Safety

P6 should favor:

```text
bounded

reversible

observable

idempotent

receipted
```

effect paths under uncertainty.

---

# 162. Safe Default

When execution status is ambiguous:

```text
DO NOT ASSUME SUCCESS
```

---

# 163. Unknown Effect Handling

When:

```text
effect state = unknown
```

prefer:

```text
inspect

reconcile

verify
```

before retrying.

---

# 164. Reconciliation

Reconciliation compares:

```text
desired state

recorded state

observed external state
```

---

# 165. Reconciliation Object

```yaml
reconciliation:

  reconciliation_id: null

  target: null

  desired_state: null

  recorded_state: null

  observed_state: null

  discrepancy: null

  repair_action: null
```

---

# 166. Desired-State Execution

Some workers may reconcile toward a desired state rather than process one-shot commands.

---

# 167. Desired-State Boundary

Desired state does not prove execution happened.

Observation still matters.

---

# 168. Drift

Execution drift occurs when actual state diverges from governed intended state.

---

# 169. Drift Repair

```text
detect
↓
classify
↓
resolve authority
↓
repair
↓
verify
↓
receipt
```

---

# 170. Execution Failure Classes

Suggested:

```text
AUTHORITY_FAILURE

WORKER_UNAVAILABLE

WORKER_REVOKED

BUDGET_EXHAUSTED

IDEMPOTENCY_CONFLICT

VERSION_CONFLICT

DEPENDENCY_FAILURE

TIMEOUT

CANCELLED

PARTIAL_FAILURE

COMMIT_FAILURE

RECEIPT_FAILURE

VERIFICATION_FAILURE

ROLLBACK_FAILURE

COMPENSATION_FAILURE

UNKNOWN_EFFECT_STATE

ENVIRONMENT_MISMATCH

POLICY_MISMATCH
```

---

# 171. Authority Failure

Request lacks valid P5 authorization.

Must block effect.

---

# 172. Worker Unavailable

No valid governed worker can execute request.

Return:

```text
BLOCKED / RETRYABLE
```

according to context.

---

# 173. Budget Exhausted

No remaining permitted resource envelope.

---

# 174. Version Conflict

Target has changed since authorization or planning.

---

# 175. Dependency Failure

Required downstream or upstream execution dependency unavailable.

---

# 176. Commit Failure

Effect plan could not reach defined commit semantics.

---

# 177. Receipt Failure

Commit may have occurred but required receipt persistence failed.

This can be a critical degraded state.

---

# 178. Verification Failure

Recorded commit does not match observed outcome.

---

# 179. Rollback Failure

Recovery path fails to restore target.

Escalate.

---

# 180. Compensation Failure

Compensating action does not achieve intended recovery state.

---

# 181. Execution Repair

Core pattern:

```text
detect failed execution edge
↓
preserve known good effects
↓
identify unknown state
↓
reconcile
↓
repair locally
↓
reverify
```

---

# 182. No Blind Global Replay

Do not replay an entire workflow because one step failed unless dependency analysis proves it safe.

---

# 183. Local Recovery

Prefer recovery of the smallest failed execution scope.

---

# 184. Global Recovery

Use only when local repair cannot restore invariants.

---

# 185. Execution Invariants

## Authority invariant

```text
no consequential effect
without valid governed authority
```

## Worker invariant

```text
consequential effect
must use governed worker path
```

## Idempotency invariant

```text
retries must not create unintended duplicate logical effects
```

## Receipt invariant

```text
defined commits emit persistent receipt state
```

## Ledger invariant

```text
commit receipts preserve append-only history
```

## Budget invariant

```text
resource consumption is attributable and bounded
```

## Version invariant

```text
execution does not silently mutate unapproved target version
```

## Verification invariant

```text
commit state does not substitute for observed outcome
```

## Recovery invariant

```text
partial failure remains explicit
```

## Provenance invariant

```text
effect lineage remains reconstructable
```

## Agency invariant

```text
worker cannot widen its own authority
```

## Gap invariant

```text
unknown effect state remains UNKNOWN
```

---

# 186. Declared Invariant References

This P6 proposal declares:

```text
I-RPOL-017
→ Worker Gate
```

```text
INV-031
INV-035
→ receipt / append-only commit evidence
```

```text
INV-041
→ cumulative principal cost accounting
```

These mappings are preserved from the supplied specification.

Their exact source text, proof obligations, and canonical status are not invented here.

---

# 187. P6 State Variables

Conceptual:

```text
R_exec
=
execution request

W
=
selected worker

A_exec
=
execution authority state

T_exec
=
transaction state

I_key
=
idempotency identity

B_p
=
principal budget state

C_p
=
cumulative principal cost

E_fx
=
effect state

Rcp
=
receipt state

V_fx
=
verification state

Retry_n
=
attempt count

Finality
=
execution finality state
```

These are architecture variables, not declared runtime primitives unless implementation confirms them.

---

# 188. P6 Operators

Architecture-level semantic operators:

```text
CREATE_EXECUTION_REQUEST()

RESOLVE_EXECUTION_AUTHORITY()

SELECT_WORKER()

CHECK_WORKER_GATE()

ACQUIRE_WORKER_LEASE()

CHECK_TARGET_VERSION()

CHECK_ENVIRONMENT()

CHECK_BUDGET()

RESERVE_BUDGET()

CHECK_IDEMPOTENCY()

BEGIN_TRANSACTION()

PREPARE_EFFECT()

EXECUTE_EFFECT()

COMMIT_EFFECT()

EMIT_RECEIPT()

APPEND_LEDGER()

OBSERVE_EFFECT()

VERIFY_EFFECT()

ACCOUNT_COST()

RELEASE_RESERVATION()

RETRY()

CANCEL()

RECONCILE()

ROLLBACK()

COMPENSATE()

FINALIZE()

SUSPEND_WORKER()

REVOKE_WORKER()

AUDIT_EXECUTION()
```

These are semantic contracts, not claims that literal functions already exist.

---

# 189. P6 H/M/L Architecture

P6 is recursive.

```text
H:
global execution policy
authority envelope
system budgets
cross-domain finality

M:
workflow
worker pool
transaction coordinator
domain execution subsystem

L:
individual command
worker attempt
effect
receipt
```

---

# 190. H-Level Execution

Examples:

```text
global execution authority policy

organization-wide budget

cross-root transaction

deployment authority
```

---

# 191. M-Level Execution

Examples:

```text
workflow run

worker queue

service transaction

deployment pipeline
```

---

# 192. L-Level Execution

Examples:

```text
single API call

single file write

single state mutation

single receipt
```

---

# 193. H/M/L Finalization Rule

A local L-level effect may finalize locally only when no unresolved M/H dependency can invalidate its commit semantics.

---

# 194. Bottom-Up Execution Reporting

```text
L receipts
→
M workflow result
→
H execution/accounting state
```

---

# 195. Top-Down Execution Control

```text
H policy/budget
→
M worker constraints
→
L operation eligibility
```

---

# 196. P6 Workflow — Normal Execution

```text
AUTHORIZED REQUEST
↓
RESOLVE PRINCIPAL
↓
RESOLVE WORKER PATH
↓
CHECK AUTHORITY
↓
CHECK TARGET VERSION
↓
CHECK ENVIRONMENT
↓
CHECK BUDGET
↓
CHECK IDEMPOTENCY
↓
RESERVE RESOURCES
↓
BEGIN EFFECT
↓
COMMIT
↓
EMIT RECEIPT
↓
ACCOUNT COST
↓
OBSERVE
↓
VERIFY
↓
FINALIZE
```

---

# 197. P6 Workflow — Retry

```text
FAILURE / TIMEOUT
↓
READ LAST PERSISTED STATE
↓
CHECK RECEIPT
↓
CHECK EXTERNAL EFFECT
↓
CHECK IDEMPOTENCY
↓
IF SAFE:
  RETRY
ELSE:
  RECONCILE / ESCALATE
```

---

# 198. P6 Workflow — Partial Failure

```text
MULTI-EFFECT EXECUTION
↓
ONE STEP FAILS
↓
FREEZE NEW DEPENDENT EFFECTS
↓
IDENTIFY COMMITTED EFFECTS
↓
IDENTIFY UNKNOWN EFFECTS
↓
CHECK ROLLBACK / COMPENSATION
↓
REPAIR
↓
VERIFY
```

---

# 199. P6 Workflow — Receipt

```text
COMMIT
↓
CREATE RECEIPT
↓
CALCULATE DIGEST
↓
APPEND LEDGER
↓
PERSIST REFERENCE
↓
MAKE AVAILABLE TO AUDIT / VERIFICATION
```

---

# 200. P6 Workflow — Budget

```text
ESTIMATE COST
↓
CHECK PRINCIPAL BUDGET
↓
RESERVE
↓
EXECUTE
↓
MEASURE ACTUAL COST
↓
ACCOUNT
↓
RELEASE UNUSED RESERVATION
```

---

# 201. P6 Workflow — Unknown Effect State

```text
CONNECTION / WORKER FAILURE
↓
EFFECT STATE UNKNOWN
↓
DO NOT BLINDLY RETRY
↓
QUERY RECEIPT / TARGET STATE
↓
RECONCILE
↓
IF COMMITTED:
  VERIFY
ELSE IF SAFE:
  RETRY
ELSE:
  ESCALATE
```

---

# 202. P6 Workflow — Rollback

```text
FAILURE
↓
CHECK ROLLBACK AUTHORITY
↓
CHECK PRIOR STATE
↓
CHECK DEPENDENCIES
↓
EXECUTE ROLLBACK
↓
EMIT RECEIPT
↓
VERIFY RESTORED STATE
```

---

# 203. P6 Workflow — Compensation

```text
IRREVERSIBLE COMMIT
↓
FAILURE / UNWANTED RESULT
↓
SELECT COMPENSATING EFFECT
↓
AUTHORIZE
↓
EXECUTE
↓
RECEIPT
↓
VERIFY
```

---

# 204. P6 Workflow — Worker Revocation

```text
CRITICAL WORKER FAILURE
↓
SUSPEND NEW LEASES
↓
REVOKE AUTHORITY/CAPABILITY
↓
IDENTIFY IN-FLIGHT JOBS
↓
RECONCILE EFFECT STATE
↓
REASSIGN SAFE JOBS
↓
AUDIT
```

---

# 205. P6 Workflow — External Executor

```text
AMOS PROPOSAL
↓
P5 AUTHORIZATION
↓
EXTERNAL EXECUTOR REQUEST
↓
EXTERNAL EFFECT
↓
RECEIPT / RESPONSE
↓
P2 OBSERVATION
↓
P6 VERIFICATION
```

---

# 206. Execution Audit

Audit should ask:

```text
was the request authorized?

which principal owned it?

which worker executed?

was worker path governed?

was target version correct?

was environment correct?

was budget available?

was budget reserved?

was idempotency enforced?

what attempt number executed?

where was commit point?

was receipt emitted?

was receipt persisted?

what cost was charged?

what external effect was observed?

was verification independent where required?

did retries occur?

did compensation occur?

did rollback occur?

what remains unknown?
```

---

# 207. Execution Audit Capsule

```yaml
execution_audit:

  audit_id: null

  request_id: null

  principal_id: null

  authority_findings: []

  worker_findings: []

  version_findings: []

  budget_findings: []

  idempotency_findings: []

  transaction_findings: []

  receipt_findings: []

  verification_findings: []

  recovery_findings: []

  gaps: []

  result: null
```

---

# 208. P6 Finding Classes

```text
UNAUTHORIZED_EXECUTION

WORKER_GATE_BYPASS

UNKNOWN_WORKER

REVOKED_WORKER_ACTIVE

EXPIRED_WORKER_LEASE

TARGET_VERSION_MISMATCH

ENVIRONMENT_MISMATCH

BUDGET_NOT_CHECKED

BUDGET_OVERRUN

UNATTRIBUTED_COST

IDEMPOTENCY_KEY_MISSING

IDEMPOTENCY_CONFLICT

DUPLICATE_LOGICAL_EFFECT

UNSAFE_RETRY

UNKNOWN_EFFECT_STATE

PARTIAL_COMMIT

RECEIPT_MISSING

RECEIPT_LEDGER_GAP

RECEIPT_DIGEST_MISMATCH

COMMIT_NOT_VERIFIED

ROLLBACK_PATH_MISSING

ROLLBACK_FAILED

COMPENSATION_FAILED

EXECUTION_PROVENANCE_GAP

CAUSAL_ORDER_VIOLATION

FINALITY_AMBIGUOUS

AGENT_SELF_ELEVATION

UNKNOWN_SUPPRESSED
```

---

# 209. Critical P6 Findings

Block or suspend effectful execution when:

```text
authority missing

worker gate bypassed

target identity ambiguous

target version stale

idempotency required but unresolved

budget unavailable

irreversible action with unknown effect state

critical receipt requirement failed

transaction partial commit threatens invariants

rollback/compensation required but unavailable

execution provenance broken
```

---

# 210. P6 Tests

Minimum:

```text
worker gate test

authority binding test

target version test

environment test

budget test

principal accounting test

idempotency test

duplicate-delivery test

retry safety test

transaction test

partial-failure test

receipt test

ledger append test

digest integrity test

verification test

rollback test

compensation test

worker crash test

lease expiry test

causal-order test

finality test

revocation test
```

---

# 211. Worker Gate Test

Attempt consequential effect outside governed worker path.

Expected:

```text
BLOCK
```

---

# 212. Authority Binding Test

Valid worker with invalid authority must not execute.

---

# 213. Version Test

Change target after request approval.

Expected:

```text
STALE REQUEST / REVALIDATE
```

---

# 214. Budget Test

Attempt effect beyond permitted principal budget.

Expected:

```text
BLOCK / ESCALATE
```

---

# 215. Principal Accounting Test

Every committed cost should be attributable to appropriate principal/account.

---

# 216. Idempotency Test

Send same logical request twice.

Expected:

```text
one logical effect
```

under declared semantics.

---

# 217. Idempotency Conflict Test

Reuse same key with different payload.

Expected:

```text
CONFLICT
```

---

# 218. Retry Safety Test

Interrupt worker at each critical execution phase and verify retry behavior.

---

# 219. Transaction Test

Inject failure between transaction operations.

Ensure partial state is correctly represented and repaired.

---

# 220. Receipt Test

Every defined commit should produce receipt.

---

# 221. Ledger Test

Attempt removal/modification/reordering according to supported threat model.

Verify detectability required by implementation.

---

# 222. Verification Test

Simulate worker reporting success while target state remains unchanged.

Expected:

```text
VERIFICATION_FAILURE
```

---

# 223. Rollback Test

Commit reversible state then trigger rollback.

Verify restored state.

---

# 224. Compensation Test

Create irreversible effect and verify compensation workflow under test conditions.

---

# 225. Crash Test

Crash worker:

```text
before effect

after effect

before receipt

after receipt
```

and verify recovery does not create unintended duplicates.

---

# 226. Lease Expiry Test

Expired worker lease should prevent unauthorized new effect.

---

# 227. Causal-Order Test

Attempt dependent execution before required predecessor finality.

Expected:

```text
BLOCK / WAIT
```

---

# 228. Revocation Test

Revoke worker authority during execution lifecycle and verify new effects stop according to policy.

---

# 229. P6 Failure Modes

## F01 — Allowed/Done Collapse

Authorization treated as completed execution.

## F02 — Worker Gate Bypass

Effect occurs through an ungoverned path.

## F03 — Capability/Authority Collapse

Worker capability treated as execution permission.

## F04 — Request/Effect Collapse

Submitted command treated as confirmed effect.

## F05 — Commit/Success Collapse

Commit record treated as verified outcome.

## F06 — Receipt/Reality Collapse

Receipt treated as proof external world matches intent.

## F07 — Duplicate Effect

Retry causes repeated irreversible effect.

## F08 — Idempotency Collision

One key maps to distinct logical requests.

## F09 — Blind Retry

Unknown effect state is retried without reconciliation.

## F10 — Budget Bypass

Action consumes resources without accounting.

## F11 — Principal Cost Leakage

One principal's execution is charged to another or unowned pool.

## F12 — Partial Commit Suppression

Incomplete multi-effect transition reported as success.

## F13 — Receipt Loss

Commit occurs without required durable receipt.

## F14 — Ledger Rewrite

Historical execution record silently changes.

## F15 — Version Drift

Effect applies to different target version than approved.

## F16 — Environment Drift

Execution occurs under incompatible environment.

## F17 — Stale Lease

Expired worker continues initiating effects.

## F18 — Worker Self-Elevation

Worker expands authority or target scope.

## F19 — Rollback Assumption

System claims reversibility without demonstrated rollback path.

## F20 — Compensation/Rollback Collapse

Compensation treated as exact restoration.

## F21 — Timeout/Failure Collapse

Timeout treated as proof no effect happened.

## F22 — Cancel/Undo Collapse

Cancellation treated as reversal of already committed state.

## F23 — Causal Order Violation

Dependent operation finalizes before prerequisite.

## F24 — False Exactly-Once Claim

Messaging semantics overstated as universal effect exactly-once guarantee.

## F25 — Verification Omission

Execution closes before intended outcome is checked.

## F26 — Observability Blindness

Effect cannot be inspected after commit.

## F27 — Global Replay

Whole workflow repeated despite only local failure.

## F28 — Autonomous Agency Inflation

Structural execution capability treated as independent autonomous world agency.

## F29 — Unknown Suppression

Ambiguous effect state converted to success/failure without evidence.

---

# 230. P6 Falsifiers

This architecture should be revised if:

```text
worker gating cannot meaningfully separate governed from ungoverned effects

idempotency identity cannot prevent duplicate logical effects

receipts cannot support effect accountability

append-only receipt history provides no recoverability or audit benefit

principal budgets cannot bound cumulative action cost

version binding cannot prevent stale execution

local recovery cannot reduce unnecessary global replay

outcome verification cannot distinguish commit from actual effect
```

---

# 231. P6 Uncertainty Vector

Track when material:

```yaml
uncertainty:

  authority: null

  execution: null

  effect_state: null

  external_response: null

  cost: null

  transaction: null

  rollback: null

  verification: null

  timing: null

  provenance: null
```

---

# 232. Execution Sensitivity

For consequential execution identify:

```text
smallest execution condition
that could change safe action.
```

Examples:

```text
target version

recipient identity

idempotency key

remaining budget

worker authority

rollback availability

effect reversibility
```

---

# 233. High-Stakes P6 Standard

For:

```text
health

safety

law

finance

security

critical infrastructure

irreversible external effects

canon/root mutation
```

increase requirements for:

```text
independent verification

version binding

explicit authority

budget limits

idempotency

receipt durability

rollback/compensation analysis

post-effect observation
```

---

# 234. Low-Risk Execution

For reversible sandboxed actions:

```text
smaller blast radius
+
bounded budget
+
strong observability
```

may permit lighter execution governance.

---

# 235. P6 Agent

An Execution / Agency agent may:

```text
prepare execution requests

check execution prerequisites

select eligible workers

estimate cost

check idempotency

monitor execution state

collect receipts

request verification

propose retry

propose rollback

propose compensation
```

---

# 236. P6 Agent Authority

Until promotion:

```yaml
agent_authority:

  read: ALLOWED_AS_GOVERNED
  propose: ALLOWED_AS_GOVERNED
  execute: NONE
  deploy: NONE
  commit_external_effect: NONE
  self_elevation: FORBIDDEN
```

---

# 237. P6 Agent Contract

```yaml
agent:

  role: execution_agency_steward

  default_authority: PROPOSE_ONLY

  read_access:
    - execution_requests
    - worker_registry
    - authority_registry
    - budget_registry
    - transaction_state
    - receipt_ledger
    - observability
    - dependency_graph

  write_access:
    - execution_proposals
    - recovery_proposals
    - audit_findings

  effectful_execution:
    authority: NONE_UNTIL_PROMOTED

  external_world_action:
    authority: NONE_UNLESS_EXTERNAL_EXECUTOR_AND_P5_AUTHORITY_EXIST

  self_elevation:
    allowed: false

  audit_log: required
```

---

# 238. Worker Registry

A derived implementation may maintain:

```text
P6_EXECUTION_AGENCY/
│
├── WORKER_REGISTRY
├── EXECUTION_REQUESTS
├── JOB_REGISTRY
├── TRANSACTION_REGISTRY
├── IDEMPOTENCY_REGISTRY
├── BUDGET_REGISTRY
├── RECEIPT_LEDGER
├── EFFECT_REGISTRY
├── VERIFICATION_REGISTRY
├── RECOVERY_REGISTRY
├── COMPENSATION_REGISTRY
├── EXECUTION_GAPS
└── HISTORY
```

This layout is proposed infrastructure, not asserted as already implemented.

---

# 239. Worker Registry Entry

```yaml
worker_registry_entry:

  worker_id: null

  class: null

  capabilities: []

  authority_ceiling: null

  scopes: []

  environments: []

  budget_class: null

  status: null

  provenance_ref: null
```

---

# 240. Execution Registry Entry

```yaml
execution_registry_entry:

  request_id: null

  principal_id: null

  worker_id: null

  transaction_id: null

  target: null

  target_version: null

  idempotency_key: null

  status: null

  receipt_ref: null

  verification_ref: null
```

---

# 241. Receipt Registry / Ledger Boundary

The execution registry describes current execution state.

The receipt ledger preserves commit history.

Mandatory:

```text
EXECUTION_REGISTRY
!=
RECEIPT_LEDGER
```

---

# 242. P6 and P1

P1 defines the environment in which effect occurs.

P6 must not assume:

```text
execution environment
=
planning environment
```

without checking.

---

# 243. P6 and P2

P2 supplies observations required to determine whether effect occurred.

---

# 244. P6 and P3

P3 retains:

```text
execution history

receipts

failure patterns

cost history

repair history
```

as persistent memory.

---

# 245. P6 and P4

P4 produces:

```text
plans

predictions

recommended actions
```

P6 does not treat a P4 model as effect authorization.

---

# 246. P6 and P5

P5 answers:

```text
Is this action authorized?
```

P6 answers:

```text
How is the authorized action
safely and accountably executed?
```

---

# 247. P6 and Control Plane

`10_CONTROL_PLANE` should implement or enforce operational effect permissions where runtime exists.

P6 defines the canonical semantic contract.

---

# 248. P6 and Validation

Validation may certify:

```text
worker

transaction protocol

receipt behavior

rollback behavior

idempotency behavior
```

within specific environment/version.

---

# 249. P6 and Dependency Graph

Execution planning should trace dependencies that can:

```text
block effect

change ordering

increase blast radius

invalidate rollback

change finality
```

---

# 250. P6 and Observability

P6 requires enough observability to distinguish:

```text
requested

running

committed

verified

failed

unknown
```

---

# 251. P6 and Deployment

Deployment is a specialized execution mode with stronger environment/version constraints.

---

# 252. P6 and Agents

Agents may reason about actions without possessing execution authority.

---

# 253. P6 and Workflows

Workflows coordinate jobs.

Workers cause effects.

These should remain distinct.

---

# 254. P6 and Protocols

`15_PROTOCOLS` may define exact exchange/commit/retry semantics.

P6 owns the high-level execution invariants.

---

# 255. P6 Core Laws

```text
AUTHORIZED
!=
EXECUTED
```

```text
REQUESTED
!=
STARTED
```

```text
STARTED
!=
COMMITTED
```

```text
COMMITTED
!=
VERIFIED
```

```text
RECEIPT
!=
REALITY
```

```text
CAPABILITY
!=
AUTHORITY
```

```text
WORKER_AVAILABLE
!=
WORKER_AUTHORIZED
```

```text
BUDGET_AVAILABLE
!=
AUTHORITY
```

```text
AUTHORITY
!=
BUDGET
```

```text
RETRYABLE
!=
IDEMPOTENT
```

```text
MESSAGE_ONCE
!=
EFFECT_ONCE
```

```text
TIMEOUT
!=
FAILURE
```

```text
CANCELLED_REQUEST
!=
ROLLED_BACK_EFFECT
```

```text
COMPENSATION
!=
ROLLBACK
```

```text
PARTIAL_COMMIT
!=
SUCCESS
```

```text
DIGEST_MATCH
!=
SEMANTIC_CORRECTNESS
```

```text
APPEND_ONLY
!=
UNIVERSALLY_TAMPER_PROOF
```

```text
DRY_RUN
!=
REAL_EXECUTION
```

```text
PLAN
!=
EFFECT
```

```text
EXECUTION_TELEMETRY
!=
GOVERNANCE_RECEIPT
```

```text
UNKNOWN_EFFECT_STATE
!=
SAFE_TO_RETRY
```

```text
AGENT
MUST NOT
SELF-GRANT EXECUTION AUTHORITY
```

```text
EXECUTION AUTHORITY
=
NONE
UNTIL GOVERNED PROMOTION
```

```text
UNKNOWN/GAP
!=
PASS
```

---

# 256. P6-1 Canonical Law — Worker Gate

```text
P6-1 WORKER GATE

CONSEQUENTIAL EFFECTS
MUST TRANSIT
A GOVERNED WORKER PATH.

AUTHORIZED INTENT
MUST NOT
BYPASS EXECUTION GOVERNANCE.

REFERENCE:
I-RPOL-017

REFERENCE STATUS:
SOURCE-SUPPLIED;
EXACT CANONICAL DEFINITION
REQUIRES SOURCE RESOLUTION.
```

---

# 257. P6-2 Canonical Law — Receipt Everything

```text
P6-2 RECEIPT EVERYTHING

A DEFINED COMMIT
MUST PRODUCE
A PERSISTENT EXECUTION RECEIPT.

THE RECEIPT MUST BIND
THE EFFECT
TO ITS EXECUTION LINEAGE.

COMMIT DIGESTS
ARE INTENDED
FOR APPEND-ONLY LEDGER RETENTION.

REFERENCES:
INV-031
INV-035

REFERENCE STATUS:
SOURCE-SUPPLIED;
EXACT CANONICAL DEFINITIONS
REQUIRE SOURCE RESOLUTION.
```

---

# 258. P6-3 Canonical Law — Budgeted Action

```text
P6-3 BUDGETED ACTION

EFFECTFUL ACTION
MUST NOT BE TREATED
AS COSTLESS.

CUMULATIVE RESOURCE CONSUMPTION
MUST BE ATTRIBUTABLE
TO AN EXECUTION PRINCIPAL
UNDER THE APPLICABLE BUDGET MODEL.

REFERENCE:
INV-041

REFERENCE STATUS:
SOURCE-SUPPLIED;
EXACT CANONICAL DEFINITION,
UNITS,
AND THRESHOLDS
REQUIRE SOURCE RESOLUTION.
```

---

# 259. Minimum P6 Execution Contract

Before AMOS treats an execution as safely actionable, it should be able to answer:

```text
WHAT is the authorized intent?

WHAT exact request represents it?

WHO is the execution principal?

WHAT P5 authority exists?

WHAT worker path is permitted?

WHICH worker will execute?

WHAT capability is required?

WHAT target will change?

WHAT exact target version?

WHAT environment applies?

WHAT regime applies?

WHAT budget applies?

HOW much budget remains?

WHAT cost is expected?

WHAT idempotency key applies?

WHAT constitutes duplicate execution?

WHAT transaction semantics apply?

WHAT is the commit point?

WHAT receipt must be emitted?

WHERE is receipt persisted?

WHAT digest binds the effect?

HOW is ledger history preserved?

WHAT could partially fail?

WHAT retry policy applies?

WHAT happens after timeout?

WHAT happens after worker crash?

CAN the effect be rolled back?

IF NOT, what compensation exists?

HOW is actual effect observed?

WHO or WHAT verifies it?

WHEN is execution final?

WHAT cost is attributed to the principal?

WHAT dependencies can block execution?

WHAT state triggers escalation?

WHAT remains UNKNOWN/GAP?
```

If load-bearing answers are missing:

```text
P6 EXECUTION STATE
=
BLOCKED
CONDITIONAL
PROPOSE_ONLY
or
UNKNOWN/GAP
```

not:

```text
SAFE_TO_EXECUTE
```

---

# 260. P6 Request Decision Table

```text
Authorized by P5?
→ continue

Authority missing?
→ BLOCK

Execution authority still NONE?
→ PROPOSE_ONLY

Governed worker exists?
→ continue

Worker unavailable?
→ WAIT / RETRY / ESCALATE

Target version changed?
→ REVALIDATE

Budget unavailable?
→ BLOCK

Idempotency unresolved?
→ BLOCK for duplicate-sensitive effect

Effect irreversible?
→ stronger checks

Receipt protocol undefined?
→ GAP

Required rollback missing?
→ BLOCK / ESCALATE

All execution gates pass?
→ eligible for governed execution
```

---

# 261. P6 Retry Decision Table

```text
Failure before any effect?
→ retry may be safe

Receipt proves commit?
→ do not repeat logical effect

External effect observed but receipt missing?
→ reconcile / repair receipt state

No receipt and effect unknown?
→ reconcile before retry

Operation idempotent?
→ retry under policy

Operation non-idempotent?
→ require effect-state determination

Idempotency key conflict?
→ BLOCK

Budget exhausted?
→ no retry without new budget
```

---

# 262. P6 Recovery Decision Table

```text
Reversible committed effect?
→ rollback candidate

Irreversible effect?
→ compensation candidate

Partial multi-effect commit?
→ freeze dependent execution

Unknown effect state?
→ reconcile

Worker compromised?
→ revoke / isolate

Receipt corrupt?
→ audit ledger/provenance

Local failure only?
→ local repair

Global invariant broken?
→ escalate / global recovery
```

---

# 263. P6 Finality Decision Table

```text
Effect merely attempted?
→ NOT FINAL

Commit recorded?
→ COMMITTED, not yet verified

Receipt durable?
→ receipt requirement satisfied

External state verified?
→ VERIFIED

Dependent causal effects unresolved?
→ finality may remain conditional

Rollback window open?
→ operationally committed but reversible

All required closure conditions satisfied?
→ FINAL under declared protocol
```

---

# 264. P6 RSCF Completion State

The current proposal:

```text
claim_class: AMOS_MODEL
```

can be expanded at architecture-contract level to:

```yaml
claim_class: DERIVED

evidence:
  - user-supplied P6 Execution & Agency specification
  - AMOS Full Brain OS operating rules
  - Universe Canon P1-P5 architecture
  - declared P6 invariant references:
      - I-RPOL-017
      - INV-031
      - INV-035
      - INV-041

provenance:
  origin_architect: Trang Phan
  transformation: p6_execution_agency_architecture_completion
  source_basis:
    - AMOS_FULL_BRAIN_OS.json
    - user-supplied P6 specification
  status: derived_from_amos_corpus_and_supplied_spec

scope:
  branch: 01_CANON
  subbranch: 02_UNIVERSE_CANON
  artifact: P6_EXECUTION_AGENCY
  role: governed_effect_execution_agency_and_accountability_contract

regime:
  architecture: AMOS OS

freshness:
  revalidate_on:
    - P5_governance_change
    - execution_policy_change
    - worker_protocol_change
    - receipt_protocol_change
    - budget_policy_change
    - invariant_definition_change
    - control_plane_change
    - deployment_change
    - core_lineage_change

dependencies:
  - CANON_UNIVERSE_CANON_CONTRACT
  - P1_REALITY_ENVIRONMENT
  - P2_SENSE_EVIDENCE
  - P3_KNOWLEDGE_MEMORY
  - P4_COGNITION_MODELS
  - P5_GOVERNANCE_AUTHORITY
  - AMOS_FULL_BRAIN_OS
  - 08_GOVERNANCE
  - 09_DEPENDENCY_GRAPH
  - 10_CONTROL_PLANE
  - 11_VALIDATION
  - 13_AGENTS
  - 14_WORKFLOWS
  - 15_PROTOCOLS
  - 18_OBSERVABILITY
  - 19_DEPLOYMENT

competing:
  - direct_effect_without_worker
  - receipt_free_execution
  - unbudgeted_agency
  - unrestricted_agent_execution
  - blind_retry
  - global_coordination_for_every_effect
  - commit_equals_success
  - telemetry_equals_receipt

falsifiers:
  - governed worker gates cannot reduce unauthorized/bypass effects
  - idempotency cannot reduce duplicate logical effects
  - receipts cannot reconstruct committed execution
  - append-only receipt history cannot preserve audit lineage
  - principal budgets cannot bound or attribute cumulative cost
  - version binding cannot prevent stale effects
  - local recovery cannot safely preserve unaffected work
  - verification cannot distinguish recorded commit from observed outcome

confidence_ceiling:
  architecture: CONDITIONAL
  worker_gate_semantics: DERIVED
  receipt_semantics: DERIVED
  budget_semantics: DERIVED
  exact_I_RPOL_017_definition: UNKNOWN_UNTIL_SOURCE_RESOLVED
  exact_INV_031_definition: UNKNOWN_UNTIL_SOURCE_RESOLVED
  exact_INV_035_definition: UNKNOWN_UNTIL_SOURCE_RESOLVED
  exact_INV_041_definition: UNKNOWN_UNTIL_SOURCE_RESOLVED
  runtime_implementation: UNKNOWN_OR_PARTIAL
  execution_authority: NONE_UNTIL_PROMOTED
```

---

# 265. Known Gaps

The following remain `UNKNOWN/GAP` until explicit canon or implementation defines them:

```text
exact source text for I-RPOL-017

exact source text for INV-031

exact source text for INV-035

exact source text for INV-041

exact worker registry schema

exact worker classes

exact worker lease protocol

exact job queue semantics

exact transaction protocol

exact atomicity guarantees

exact commit-point definitions

exact receipt schema

exact receipt digest algorithm

exact append-only ledger implementation

exact ledger tamper model

exact idempotency-key format

exact idempotency retention period

exact replay-protection protocol

exact retry backoff policy

exact exactly-once/effectively-once guarantees

exact budget units

exact budget reservation semantics

exact principal cost attribution rules

exact cumulative-cost thresholds

exact concurrency-control algorithm

exact MVCC implementation

exact CAS implementation

exact causal-epoch mechanism

exact shard definition

exact finality protocol

exact compensation framework

exact rollback framework

exact worker isolation mechanism

exact external executor contract

exact execution-token format

exact execution observability schema

exact execution audit retention policy

exact agent execution promotion process

exact runtime P6 implementation
```

Do not fabricate these as implemented.

---

# 266. Completion Status

This artifact should no longer remain a short placeholder or thin proposal at the architecture-contract level.

It may become:

```yaml
class: CANON_MODEL

epistemic_class: AMOS_MODEL

specification_status: ARCHITECTURE_COMPLETED_FROM_PROPOSAL

canonical_status: CONDITIONAL

architecture_status: DEFINED

source_status: DERIVED_FROM_SOURCE_AND_USER_SUPPLIED_P6_SPEC

implementation_status: PARTIAL_OR_UNKNOWN

validation_status: ARCHITECTURE_DEFINED

p6_contract_status: DEFINED

worker_gate_status: DEFINED_AT_SEMANTIC_LEVEL

receipt_contract_status: DEFINED_AT_SEMANTIC_LEVEL

budget_contract_status: DEFINED_AT_SEMANTIC_LEVEL

idempotency_contract_status: DEFINED_AT_SEMANTIC_LEVEL

transaction_contract_status: DERIVED_CONDITIONAL

recovery_contract_status: DERIVED_CONDITIONAL

runtime_worker_status: UNKNOWN/GAP

receipt_ledger_runtime_status: UNKNOWN/GAP

budget_runtime_status: UNKNOWN/GAP

execution_authority_status: NONE_UNTIL_PROMOTED
```

---

# 267. Final Contract

`P6 Execution / Agency` is the **effect realization and operational accountability plane** of the AMOS Universe Canon.

The full chain becomes:

```text
P1
REALITY / ENVIRONMENT
        ↓

P2
SENSE / EVIDENCE
        ↓

P3
KNOWLEDGE / MEMORY
        ↓

P4
COGNITION / MODELS
        ↓

P5
GOVERNANCE / AUTHORITY
        ↓

P6
EXECUTION / AGENCY
        ↓
WORKER
        ↓
TRANSACTION
        ↓
EFFECT
        ↓
COMMIT
        ↓
RECEIPT
        ↓
VERIFICATION
        ↓
ACCOUNTABILITY / RECOVERY
```

The correct relationship is:

```text
P5
=
IS THE ACTION LEGITIMATELY ALLOWED?

P6
=
HOW DOES THAT ALLOWED ACTION
BECOME A BOUNDED,
ACCOUNTABLE,
RECOVERABLE EFFECT?
```

The governing P6 principle is:

```text
AN EFFECT MUST NOT
APPEAR MERELY BECAUSE
AN INTENTION WAS AUTHORIZED.

BETWEEN
"ALLOWED"
AND
"DONE"

AMOS REQUIRES
A GOVERNED EXECUTION PATH.
```

And the execution law is:

```text
BIND THE PRINCIPAL.

BIND THE AUTHORITY.

BIND THE TARGET.

BIND THE VERSION.

SELECT A GOVERNED WORKER.

CHECK THE ENVIRONMENT.

CHECK THE BUDGET.

CHECK IDEMPOTENCY.

RESERVE RESOURCES.

EXECUTE THE SMALLEST
AUTHORIZED EFFECT.

DEFINE THE COMMIT POINT.

RECEIPT THE COMMIT.

PRESERVE THE RECEIPT.

ACCOUNT THE COST.

OBSERVE THE ACTUAL EFFECT.

VERIFY THE RESULT.

IF FAILURE IS LOCAL,
REPAIR LOCALLY.

IF EFFECT STATE IS UNKNOWN,
DO NOT BLINDLY RETRY.

IF REVERSIBLE,
ROLL BACK WHEN REQUIRED.

IF IRREVERSIBLE,
USE GOVERNED COMPENSATION
WHEN POSSIBLE.

NEVER LET A WORKER
EXPAND ITS OWN AUTHORITY.

NEVER LET
A REQUEST
MASQUERADE AS AN EFFECT.

NEVER LET
A RECEIPT
MASQUERADE AS REALITY.

AND UNTIL
EXECUTION AUTHORITY
IS EXPLICITLY PROMOTED,

P6 REMAINS:

PROPOSE_ONLY /
NO EFFECTFUL AUTHORITY.
```

---

[[00_ROOT_MOC]]|[[AMOS MOC]]

---

**Related:** [[AMOS_7_PART_UNIVERSE_CANON]] · [[HML_CANON]] · [[00_HOME]] · [[AMOS_RSCF_NODES]]

---

RSCF-NODE

node_id: p6_execution_agency

node_type: note

path: 01_CANON/02_UNIVERSE_CANON/P6_EXECUTION_AGENCY.md

RSCF-RELATIONS:

- INDEXED_BY: [[00_HOME]]

- INDEXED_BY: [[AMOS_RSCF_NODES]]

- CHILD_OF: [[AMOS_7_PART_UNIVERSE_CANON]]

- DEPENDS_ON: [[P1_REALITY_ENVIRONMENT]]

- DEPENDS_ON: [[P2_SENSE_EVIDENCE]]

- DEPENDS_ON: [[P3_KNOWLEDGE_MEMORY]]

- DEPENDS_ON: [[P4_COGNITION_MODELS]]

- DEPENDS_ON: [[P5_GOVERNANCE_AUTHORITY]]

claim_class: AMOS_MODEL

```

**Conclusion class:** `DERIVED / CONDITIONAL`. P6 is now structurally aligned with P1–P5 and preserves the key distinction that was already present in your supplied specification: **execution architecture may be fully defined while execution authority remains `NONE`**. The exact meanings of `I-RPOL-017`, `INV-031`, `INV-035`, and `INV-041` remain intentionally unresolved until their defining corpus records are retrieved; I have not fabricated them. That is the correct AMOS treatment under the Full Brain integrity boundary.
```

---
**MOC:** [[02_UNIVERSE_CANON_MOC]]
