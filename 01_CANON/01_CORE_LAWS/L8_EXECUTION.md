---
tags:
- canon
- core_laws
- execution
- effects
- commit
- idempotency
- ledger
- worker
- control-plane
- rscf
- canon/universe
- 00-root-moc
- amos-moc
- 00-home
- amos-rscf-nodes
- law-hierarchy
- law/L0-integrity
- law/L1-epistemic
- law/L2-provenance
- law/L3-dependency
- l4-causal
- l5-scope-regime
- l6-uncertainty
- l7-authority
- routing-policy
- authority-resolver
- authority-witness
- 01-core-laws-moc
title: L8 Execution Laws
origin_architect: Trang Phan
updated: '2026-08-26'
status: PROPOSED_SPECIFICATION
epistemic_class: AMOS_MODEL
canonical_status: CONDITIONAL
implementation_status: LOGIC_EXECUTABLE_IN_PART
type: document
source: 01_CANON/01_CORE_LAWS
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# L8 Execution Laws

**Origin architect / steward:** Trang Phan
**Layer:** `01_CANON / 01_CORE_LAWS / L8_EXECUTION`
**Artifact class:** `CORE_LAW_CONTRACT`
**Status:** `PROPOSED_SPECIFICATION / AMOS_MODEL`
**Canonical status:** `CONDITIONAL`
**Implementation status:** `LOGIC_EXECUTABLE_IN_PART`

> L8 governs the transition from an approved intention into an actual system effect.
>
> Approval is not execution. Preparation is not commitment. A successful tool call is not sufficient evidence of a valid governed effect.

---

# 0. Status

This document expands the supplied L8 seed specification:

```text
E-1 Worker-Only Effects
E-2 Commit-Time Revalidation
E-3 Idempotency
E-4 Effect Digests
```

and the supplied enforcement references:

```text
INV-030
INV-031
INV-032
INV-033
I-RPOL-017
03_CONTROL_PLANE
```

The four seed laws and implementation references are source-supplied for this artifact.

The broader structures below are a proposed AMOS structural completion and remain:

```text
AMOS_MODEL
```

until reconciled with authoritative execution canon and executable runtime evidence.

Hard boundary:

```text
SPECIFIED != IMPLEMENTED
IMPLEMENTED != VALIDATED
REPORTED_INVARIANT != VERIFIED_RUNTIME_BEHAVIOR
TEST_PASS != UNIVERSAL_PROOF
APPROVED != EXECUTED
EXECUTED != COMMITTED
COMMITTED != CORRECT
```

---

# 1. Purpose

L8 answers:

```text
HOW DOES AN APPROVED INTENTION
BECOME A GOVERNED EFFECT?
```

Its responsibility begins after an intended action exists and continues through:

```text
INTENT
↓
PROPOSAL
↓
AUTHORIZATION
↓
ROUTING
↓
PREPARATION
↓
REVALIDATION
↓
EXECUTION
↓
COMMIT
↓
RECEIPT
↓
LEDGER
```

The execution layer MUST preserve the governance conditions established upstream.

Execution MUST NOT become an alternate route around authorization, policy, provenance, or commitment controls.

---

# 2. Execution Boundary

L8 distinguishes:

```text
INTENTION
!=
PROPOSAL
!=
APPROVAL
!=
DISPATCH
!=
EXECUTION
!=
EFFECT
!=
COMMITMENT
!=
RECEIPT
```

Each represents a different state.

A proposal can be approved but never executed.

A worker can execute but fail before producing an effect.

An external effect can occur while receipt recording fails.

A receipt can exist for a failed operation.

Therefore these states MUST NOT be collapsed.

---

# 3. Core Execution State

A conceptual execution object MAY be represented as:

```yaml
execution:
  execution_id: ...
  transaction_id: ...
  principal: ...
  worker: ...
  action: ...
  resource: ...
  parameters: ...
  expected_effect: ...
  authority_witness: ...
  policy_decision: ...
  idempotency_key: ...
  effect_digest: ...
  state: ...
  receipt: ...
  ledger_reference: ...
```

This is a structural AMOS model, not an assertion that the runtime currently uses this exact schema.

---

# 4. Execution State Machine

Conceptually:

```text
PROPOSED
   ↓
AUTHORIZED
   ↓
ROUTED
   ↓
PREPARED
   ↓
REVALIDATED
   ↓
DISPATCHED
   ↓
EXECUTING
   ↓
EFFECT_OBSERVED
   ↓
COMMITTED
   ↓
RECEIPTED
   ↓
LEDGERED
```

Failure branches MAY include:

```text
DENIED
ABORTED
FAILED
TIMED_OUT
UNKNOWN_OUTCOME
COMPENSATING
ROLLED_BACK
QUARANTINED
```

State transitions MUST preserve provenance.

---

# 5. E-1 — Worker-Only Effects

**Supplied law:**

```text
Consequential effects execute only via
infrastructure-governed worker paths.
```

Therefore:

```text
CONSEQUENTIAL_EFFECT
→
GOVERNED_WORKER_PATH
```

A reasoning component, planner, model, policy evaluator, or coordinator SHOULD NOT directly bypass the infrastructure execution path for consequential effects.

---

# 6. Worker Definition

A worker is the execution component permitted to perform a defined class of effects under infrastructure governance.

Conceptually:

```yaml
worker:
  worker_id: ...
  worker_type: ...
  capabilities: [...]
  effect_classes: [...]
  execution_environment: ...
  routing_policy: ...
  authority_requirements: ...
```

Worker status does not itself grant authority.

Therefore:

```text
WORKER_CAPABILITY
!=
ACTION_AUTHORITY
```

---

# 7. Worker Path

A governed worker path SHOULD preserve:

```text
proposal identity
authority witness
policy decision
resource identity
effect parameters
transaction identity
idempotency identity
execution provenance
receipt
effect digest
ledger reference
```

Material loss of these bindings SHOULD block or downgrade execution.

---

# 8. Direct-Effect Prohibition

A consequential effect MUST NOT be produced through an ungoverned side path merely because that path is technically available.

Invalid pattern:

```text
PLANNER
↓
DIRECT TOOL EFFECT
```

when the required architecture is:

```text
PLANNER
↓
CONTROL PLANE
↓
ROUTING
↓
WORKER
↓
COMMIT GATE
↓
EFFECT
```

---

# 9. Infrastructure Governance

Infrastructure governance SHOULD determine:

- worker eligibility;
- route eligibility;
- authority validity;
- policy compatibility;
- resource identity;
- execution constraints;
- idempotency requirements;
- commit eligibility;
- receipt requirements;
- ledger requirements.

Domain workers SHOULD remain separate from infrastructure authority.

---

# 10. Routing Policy

The supplied artifact states:

```text
Worker path gating in routing policy
(I-RPOL-017)
```

Preserved classification:

```yaml
routing_policy_claim:
  invariant: I-RPOL-017
  claimed_function: worker_path_gating
  evidence_class: SOURCE_CLAIM
  independent_runtime_verification: NOT_ESTABLISHED_HERE
```

Therefore:

```text
I-RPOL-017 REFERENCED
!=
I-RPOL-017 INDEPENDENTLY VERIFIED
```

---

# 11. Worker Eligibility

Before dispatch:

```text
WorkerEligible(W,E)
```

SHOULD establish that worker `W` is an allowed executor for effect class `E`.

Eligibility MAY depend on:

```text
worker type
effect class
environment
resource class
authority
policy
risk level
execution mode
health state
version
```

---

# 12. Worker Capability

The selected worker MUST possess the required technical capability.

```text
AUTHORIZED
AND
NOT_CAPABLE
→
NO EXECUTION
```

The system MUST NOT fabricate successful execution when no valid worker can perform the operation.

---

# 13. Worker Isolation

Where multiple workers exist, each worker SHOULD operate only within its declared execution envelope.

Conceptually:

```text
WorkerEffectScope(W)
⊆
AllowedWorkerScope(W)
```

A worker must not silently expand its effect class.

---

# 14. Worker Identity

Consequential execution SHOULD be attributable to a stable worker identity.

The ledger SHOULD be able to distinguish:

```text
principal requesting effect
```

from:

```text
worker executing effect
```

because:

```text
REQUESTER != EXECUTOR
```

in many architectures.

---

# 15. E-2 — Commit-Time Revalidation

**Supplied law:**

```text
Authorization re-checked at commit time,
not just request time.
```

Reference:

```text
INV-030
```

This establishes the central execution invariant:

```text
REQUEST-TIME AUTHORIZATION
IS NOT SUFFICIENT
FOR MUTABLE CONSEQUENTIAL COMMIT
```

---

# 16. Commit-Time Gate

Immediately before a consequential commitment, the infrastructure SHOULD validate the current commit envelope.

Conceptually:

```text
CommitAllowed =
AuthorityCurrent
AND
PolicyCurrent
AND
ScopeValid
AND
ConstraintsValid
AND
ResourceValid
AND
EffectMatches
AND
WorkerEligible
```

Additional domain-specific requirements MAY apply.

---

# 17. Request-Time vs Commit-Time

Example:

```text
t1: request created
t2: authority approved
t3: environment changes
t4: authority revoked
t5: worker attempts commit
```

Authorization at `t2` MUST NOT automatically authorize commitment at `t5`.

Required:

```text
REVALIDATE(t5)
```

---

# 18. Mutable Commit Inputs

Commit-time revalidation SHOULD cover every mutable state capable of invalidating the effect.

Possible examples:

```text
authority epoch
policy version
resource version
recipient identity
effect parameters
constraint state
transaction state
worker eligibility
environment
risk state
quota
budget
revocation state
```

Only load-bearing mutable state needs revalidation.

---

# 19. Observed Read Set

For governed execution, the system SHOULD know which mutable state was relied upon when preparing the effect.

Conceptually:

```yaml
observed_read_set:
  authority_epoch: ...
  policy_version: ...
  resource_version: ...
  constraint_version: ...
```

Commit-time validation compares relevant current state with the observed state.

---

# 20. Stale Read Detection

If a load-bearing state changes:

```text
READ_VERSION != CURRENT_VERSION
```

the system SHOULD:

```text
REVALIDATE
```

or:

```text
ABORT
```

rather than blindly committing.

---

# 21. MVCC/CAS Execution Pattern

Where AMOS uses MVCC/CAS-style reasoning:

```text
READ
↓
PREPARE
↓
COMPARE
↓
COMMIT
```

If the comparison fails:

```text
CAS_FAIL
→
NO BLIND COMMIT
```

The operation may be retried only under the idempotency and redispatch laws below.

This is a reasoning/control pattern, not a claim that every AMOS deployment literally implements a specific database MVCC algorithm.

---

# 22. Commit Effect Binding

The effect revalidated at commit time MUST be the effect actually committed.

Conceptually:

```text
ValidatedEffectDigest
=
CommittedEffectDigest
```

or another sufficiently strong equivalence relation defined by authoritative runtime canon.

Material effect mutation after validation invalidates the commit authorization.

---

# 23. Effect Mutation

If any authority-relevant field changes after validation:

```text
action
resource
recipient
amount
parameters
purpose
transaction
environment
```

the system SHOULD invalidate the prior commit decision.

```text
MATERIAL_MUTATION
→
REVALIDATE
```

---

# 24. Commit-Time Failure

If revalidation fails:

```text
COMMIT = DENIED
```

The worker MUST NOT continue merely because:

```text
execution already started
```

unless the effect has crossed an irreversible boundary that requires compensation rather than prevention.

---

# 25. Irreversible Boundary

Every consequential execution SHOULD define the latest reversible point.

Conceptually:

```text
PREPARE
↓
LAST_SAFE_ABORT_POINT
↓
IRREVERSIBLE_EFFECT
```

Commit-time revalidation SHOULD occur before the irreversible boundary whenever technically possible.

---

# 26. E-3 — Idempotency

**Supplied law:**

```text
Retried operations must be idempotent;
blind redispatch prohibited.
```

References:

```text
INV-032
INV-033
```

The core safety problem is:

```text
UNKNOWN OUTCOME
+
BLIND RETRY
=
POSSIBLE DUPLICATE EFFECT
```

---

# 27. Idempotency Definition

For an operation `O` with idempotency identity `K`, repeated valid delivery SHOULD not create multiple logically distinct effects where only one was intended.

Conceptually:

```text
Apply(O,K)
+
Apply(O,K)
≈
Apply(O,K)
```

with respect to the governed external effect.

The exact equivalence relation is domain-specific.

---

# 28. Idempotency Key

A consequential retriable operation SHOULD carry an idempotency key.

Conceptually:

```yaml
idempotency:
  key: ...
  transaction_id: ...
  effect_digest: ...
  principal: ...
  validity_window: ...
```

The key SHOULD be bound strongly enough to prevent unrelated effects from sharing an identity.

---

# 29. Idempotency Binding

A key for effect `E1` MUST NOT silently authorize or deduplicate materially different effect `E2`.

Therefore:

```text
SameKey
AND
DifferentEffectDigest
→
CONFLICT
```

not:

```text
REUSE AS SAME EFFECT
```

---

# 30. Retry

A retry is another attempt to complete the same logical operation.

```text
RETRY
!=
NEW INTENTION
```

The retry SHOULD preserve:

```text
transaction identity
idempotency identity
effect identity
authority requirements
provenance
```

---

# 31. Blind Redispatch

Blind redispatch means issuing the same or similar consequential operation again without first resolving whether the previous attempt already caused the effect.

Prohibited pattern:

```text
SEND
↓
TIMEOUT
↓
UNKNOWN OUTCOME
↓
SEND AGAIN
```

without idempotency or reconciliation.

---

# 32. Unknown Outcome

A timeout does not establish failure.

Therefore:

```text
TIMEOUT
!=
NO_EFFECT
```

Possible states include:

```text
effect not executed
effect executed but response lost
effect committed but receipt lost
partial external effect
unknown
```

The system MUST preserve this ambiguity.

---

# 33. Unknown-Outcome Recovery

When outcome is unknown:

```text
UNKNOWN_OUTCOME
↓
QUERY / RECONCILE
↓
DETERMINE EFFECT STATE
```

Only then should the system decide whether to:

```text
ACCEPT EXISTING EFFECT
RETRY IDEMPOTENTLY
COMPENSATE
ESCALATE
```

---

# 34. Retry Eligibility

Retry SHOULD require:

```text
same logical operation
AND
valid idempotency identity
AND
current authority
AND
current policy
AND
retry-safe worker path
```

A valid original request does not permanently authorize unlimited retries.

---

# 35. Retry Authorization

Every retry that can create a consequential effect SHOULD remain inside the current authorization envelope.

```text
AUTHORIZED_AT_ATTEMPT_1
!=
AUTHORIZED_AT_ATTEMPT_2
```

if authority or policy has changed.

Therefore retries inherit E-2.

---

# 36. Retry Budget

Execution infrastructure SHOULD bound retries.

Conceptually:

```yaml
retry_policy:
  max_attempts: ...
  backoff: ...
  retryable_failures: [...]
  reconciliation_required_for_unknown_outcome: true
```

Unlimited retries are prohibited for consequential operations unless authoritative domain semantics explicitly establish safety.

---

# 37. Retry Exhaustion

When the retry budget is exhausted:

```text
RETRY_EXHAUSTED
```

the system SHOULD transition to:

```text
FAILED
ESCALATE
RECONCILE
COMPENSATE
```

rather than continuing indefinitely.

---

# 38. Duplicate Detection

Before repeating a consequential effect, infrastructure SHOULD inspect:

```text
idempotency key
transaction identity
effect digest
receipt state
ledger state
external reconciliation state
```

to determine whether the intended effect already exists.

---

# 39. Duplicate Effect

If the same logical effect is already committed:

```text
DUPLICATE_REQUEST
→
RETURN EXISTING RESULT / RECEIPT
```

where domain semantics permit.

It SHOULD NOT create another effect.

---

# 40. Conflicting Duplicate

If:

```text
same idempotency key
```

maps to:

```text
different effect
```

then:

```text
IDEMPOTENCY_CONFLICT
```

SHOULD fail closed.

This is evidence of state mismatch, key misuse, or mutation.

---

# 41. E-4 — Effect Digests

**Supplied law:**

```text
Every effect carries a digest recorded to the ledger.
```

Reference:

```text
INV-031
```

The effect digest binds the intended or committed effect to a stable representation suitable for integrity checking.

---

# 42. Effect Digest Purpose

An effect digest SHOULD support:

- effect identity;
- mutation detection;
- receipt matching;
- transaction matching;
- replay detection;
- audit;
- ledger integrity;
- retry reconciliation.

It is not itself proof that the effect occurred.

Therefore:

```text
EFFECT_DIGEST
!=
EFFECT_OCCURRENCE
```

---

# 43. Digest Input

Conceptually:

```text
EffectDigest =
H(
  canonical_effect_representation
)
```

The canonical representation MAY include:

```text
action
resource
recipient
parameters
transaction identity
effect class
relevant constraints
```

The exact digest algorithm and canonicalization MUST come from authoritative implementation/canon.

They are not invented here.

---

# 44. Canonical Effect Representation

Digesting requires deterministic representation.

Conceptually:

```text
same governed effect
→
same canonical representation
→
same digest
```

where the canonicalization contract defines equivalence.

Without canonicalization, serialization differences could produce misleading digest differences.

---

# 45. Digest Mutation Detection

If a material effect field changes:

```text
Digest(E1) != Digest(E2)
```

under a collision-resistant implementation assumption.

The system SHOULD treat this as a different effect unless canonical rules establish equivalence.

---

# 46. Digest and Authority Witness

Where L7 authority witnesses are effect-bound:

```text
AuthorityWitness.effect_digest
=
Execution.effect_digest
```

SHOULD hold at commit time if the implementation uses digest binding.

This joins L7 authority and L8 execution without collapsing their responsibilities.

---

# 47. Digest and Idempotency

An idempotency key SHOULD be checked against the effect digest.

Conceptually:

```text
(K,D1)
```

must not later become:

```text
(K,D2)
```

where:

```text
D1 != D2
```

unless an authoritative mutation protocol explicitly supersedes the earlier operation.

---

# 48. Digest and Receipt

A receipt SHOULD identify the digest of the effect it reports.

Conceptually:

```yaml
receipt:
  execution_id: ...
  transaction_id: ...
  effect_digest: ...
  outcome: ...
  committed_at: ...
```

This allows later verification that the receipt corresponds to the intended effect.

---

# 49. Digest and Ledger

The supplied law requires:

```text
EFFECT DIGEST
→
LEDGER RECORD
```

Conceptually:

```yaml
ledger_entry:
  event_id: ...
  execution_id: ...
  transaction_id: ...
  effect_digest: ...
  outcome: ...
  timestamp: ...
  worker: ...
  authority_witness: ...
  receipt: ...
```

The exact ledger schema remains implementation-dependent.

---

# 50. Ledger

The execution ledger provides persistent evidence about execution state.

It SHOULD distinguish:

```text
attempt
dispatch
effect
commit
failure
retry
receipt
compensation
rollback
```

rather than recording every event as generic "success" or "failure."

---

# 51. Receipt

A receipt is an execution artifact reporting an operation outcome.

Possible receipt states MAY include:

```text
COMMITTED
FAILED
ABORTED
DUPLICATE
REJECTED
UNKNOWN
COMPENSATED
```

A receipt is evidence about execution.

It MUST NOT automatically be interpreted as independent proof of external reality unless the receipt source supports that claim.

---

# 52. Receipt Integrity

A receipt SHOULD bind:

```text
execution_id
transaction_id
worker_id
effect_digest
outcome
timestamp
```

and, where required:

```text
external_reference
authority_witness
ledger_reference
```

---

# 53. Receipt/Ledger Agreement

Where both exist:

```text
Receipt.effect_digest
=
Ledger.effect_digest
```

SHOULD hold.

A mismatch SHOULD trigger:

```text
QUARANTINE
RECONCILIATION
AUDIT
```

rather than silent acceptance.

---

# 54. Missing Receipt

Missing receipt does not necessarily mean missing effect.

Therefore:

```text
NO_RECEIPT
!=
NO_EFFECT
```

If the worker may have crossed the effect boundary:

```text
OUTCOME = UNKNOWN
```

until reconciled.

---

# 55. Missing Ledger Record

If an effect may have occurred but ledger persistence failed:

```text
EFFECT POSSIBLY COMMITTED
+
LEDGER MISSING
```

the system SHOULD enter reconciliation rather than redispatching.

---

# 56. Execution Provenance

Execution provenance SHOULD preserve:

```text
request origin
principal
authorization witness
policy decision
router
worker
worker version
execution environment
effect digest
idempotency key
attempt number
receipt
ledger entry
external result reference
```

where relevant and available.

---

# 57. Execution Attempt

Each physical attempt SHOULD have its own attempt identity.

Conceptually:

```text
LogicalOperation K
├── Attempt A1
├── Attempt A2
└── Attempt A3
```

All attempts may refer to the same logical idempotent operation while retaining separate execution provenance.

---

# 58. Logical vs Physical Execution

Distinguish:

```text
LOGICAL_OPERATION
```

from:

```text
PHYSICAL_ATTEMPT
```

This is necessary because one logical operation may require several physical attempts.

The ledger SHOULD preserve both identities.

---

# 59. Attempt Counter

Conceptually:

```yaml
attempt:
  logical_operation_id: ...
  attempt_id: ...
  attempt_number: 2
  idempotency_key: ...
```

Attempt numbers MUST NOT be used as substitutes for idempotency identity.

---

# 60. Dispatch

Dispatch transfers an approved execution request to an eligible worker.

```text
DISPATCH
!=
EFFECT
```

A dispatch can fail before worker execution.

---

# 61. Dispatch Contract

A dispatch envelope SHOULD contain sufficient immutable or versioned context:

```yaml
dispatch:
  execution_id: ...
  transaction_id: ...
  worker_id: ...
  action: ...
  resource: ...
  effect_digest: ...
  idempotency_key: ...
  authority_witness: ...
  policy_reference: ...
  observed_read_set: ...
```

---

# 62. Dispatch Mutation

A worker MUST NOT materially mutate the effect outside authorized transformation rules.

If mutation is required:

```text
RETURN TO VALIDATION
```

or create a new proposal/effect identity.

---

# 63. Execution Environment

Consequential execution SHOULD identify its environment:

```text
development
test
staging
production
external
sandbox
```

or domain equivalent.

Authority for one environment MUST NOT automatically authorize another.

---

# 64. Environment Binding

```text
AUTHORIZED(staging)
!=
AUTHORIZED(production)
```

unless the grant explicitly covers both.

Execution routing MUST preserve this distinction.

---

# 65. Dry Run

A dry run simulates or validates an execution without producing the consequential external effect.

Therefore:

```text
DRY_RUN
!=
COMMIT
```

A successful dry run MUST NOT be reported as successful real-world execution.

---

# 66. Simulation Boundary

Similarly:

```text
SIMULATED_EFFECT
!=
REAL_EFFECT
```

The ledger SHOULD identify simulation mode explicitly.

---

# 67. Partial Effect

A worker may produce only part of an intended multi-step effect.

Example:

```text
E1 committed
E2 failed
E3 never attempted
```

This MUST NOT be recorded simply as:

```text
SUCCESS
```

or:

```text
NO_EFFECT
```

The partial state must remain explicit.

---

# 68. Atomic Effect

Where the operation is intended to be atomic:

```text
ALL EFFECTS COMMIT
OR
NO EFFECTS COMMIT
```

subject to actual infrastructure guarantees.

If true atomicity is unavailable, the system MUST NOT falsely claim it.

Compensation may be required instead.

---

# 69. Multi-Effect Transaction

Conceptually:

```yaml
transaction:
  transaction_id: ...
  effects:
    - E1
    - E2
    - E3
```

The transaction SHOULD define:

```text
atomicity semantics
ordering
dependencies
rollback semantics
compensation semantics
authorization envelope
```

---

# 70. Ordered Effects

Where order matters:

```text
E1 → E2 → E3
```

must be preserved.

Retries MUST NOT reorder effects if reordering changes semantics.

---

# 71. Dependency-Aware Execution

An effect dependent on another effect MUST NOT execute before its prerequisite reaches the required state.

```text
E2 DEPENDS_ON E1
AND
E1 != REQUIRED_STATE
→
BLOCK E2
```

---

# 72. Failure Propagation

Execution failure SHOULD invalidate only dependent pending effects where possible.

Example:

```text
E1 → E2
E3 independent
```

If `E1` fails:

```text
block E2
```

but do not automatically block `E3` unless transaction semantics require it.

---

# 73. Selective Abort

Abort scope SHOULD follow dependency scope.

```text
FAILED(E1)
→
ABORT(descendants(E1))
```

not necessarily the entire execution graph.

Global abort is appropriate only where atomicity or shared invariants require it.

---

# 74. Compensation

When an effect cannot be rolled back directly, a compensating effect MAY be required.

```text
COMMIT(E1)
↓
FAIL(E2)
↓
COMPENSATE(E1)
```

Compensation is a new effect and therefore requires its own:

```text
authority
policy
worker path
effect digest
receipt
ledger record
```

unless authoritative domain semantics establish pre-authorized compensation.

---

# 75. Rollback vs Compensation

```text
ROLLBACK
!=
COMPENSATION
```

Rollback restores prior state through transactional reversal where supported.

Compensation creates a subsequent effect intended to offset the earlier effect.

The distinction MUST remain explicit.

---

# 76. Execution Timeout

Timeout is an observation about response timing.

It does not establish execution outcome.

Therefore:

```text
TIMEOUT
→
UNKNOWN_OUTCOME
```

unless infrastructure can prove that no effect occurred.

---

# 77. Cancellation

Cancellation SHOULD distinguish:

```text
cancel before dispatch
cancel before effect
cancel after irreversible boundary
```

After irreversible effect:

```text
CANCEL
```

may be impossible and compensation may be required.

---

# 78. Worker Crash

A worker crash MAY leave:

```text
no effect
partial effect
committed effect without receipt
unknown effect
```

Therefore crash recovery SHOULD consult ledger, idempotency state, and external reconciliation before redispatch.

---

# 79. Router Crash

A router crash after dispatch but before local acknowledgement creates ambiguity.

The system MUST NOT assume:

```text
dispatch absent
```

unless dispatch delivery semantics prove it.

---

# 80. Ledger Crash

Ledger persistence failure after external commit creates a dangerous ambiguity:

```text
EXTERNAL EFFECT = POSSIBLE/TRUE
LEDGER STATE = MISSING
```

Recovery SHOULD reconcile before retry.

---

# 81. Receipt Loss

Receipt loss SHOULD be recoverable through:

```text
idempotency identity
effect digest
worker state
external reference
ledger
```

where available.

Blind effect repetition is prohibited.

---

# 82. Replay

A historical dispatch or receipt MUST NOT automatically be executable as a new operation.

```text
REPLAYED_MESSAGE
!=
NEW AUTHORIZED_OPERATION
```

Replay protection SHOULD use transaction, idempotency, authority, and freshness state.

---

# 83. Stale Dispatch

If a queued dispatch becomes stale before execution:

```text
authority changed
policy changed
resource changed
effect expired
```

the worker/control plane SHOULD revalidate before effect.

Queue residence does not preserve authorization indefinitely.

---

# 84. Queue Semantics

A queue is transport/state infrastructure.

```text
MESSAGE_IN_QUEUE
!=
COMMIT_AUTHORIZED
```

The worker MUST still respect commit-time gates.

---

# 85. At-Least-Once Delivery

If transport may deliver a message more than once:

```text
AT_LEAST_ONCE
```

then idempotency becomes load-bearing.

Duplicate delivery MUST NOT imply duplicate effect.

---

# 86. At-Most-Once Delivery

At-most-once delivery reduces duplicates but may lose execution.

It does not eliminate the need for:

```text
receipts
reconciliation
effect identity
```

for consequential operations.

---

# 87. Exactly-Once Claims

Claims of:

```text
EXACTLY_ONCE
```

MUST identify the actual scope.

Possible scopes differ:

```text
message processing
ledger insertion
database transaction
external business effect
```

Exactly-once processing in one subsystem does not prove exactly-once external effect.

---

# 88. External Systems

External APIs may have different execution semantics.

AMOS MUST NOT assume:

```text
external API supports idempotency
```

without evidence.

If external idempotency is unavailable, reconciliation or compensation requirements become stronger.

---

# 89. External Receipt

An external system reference MAY strengthen evidence that an effect occurred.

Examples:

```text
transaction ID
message ID
order ID
provider receipt
```

But evidence strength depends on the provider and semantics.

---

# 90. Effect Confirmation

Possible confirmation classes:

```text
LOCAL_DISPATCH_CONFIRMED
WORKER_EXECUTION_CONFIRMED
EXTERNAL_ACCEPTANCE_CONFIRMED
EXTERNAL_COMMIT_CONFIRMED
RECONCILED
UNKNOWN
```

These MUST NOT be conflated.

---

# 91. Execution Result

A conceptual result MAY be:

```yaml
execution_result:
  logical_operation_id: ...
  execution_id: ...
  attempt_id: ...
  effect_digest: ...
  state: COMMITTED
  confirmation_class: EXTERNAL_COMMIT_CONFIRMED
  receipt: ...
  ledger_reference: ...
```

---

# 92. Success Semantics

`SUCCESS` SHOULD be avoided unless its meaning is defined.

Prefer:

```text
DISPATCHED
EXECUTED
ACCEPTED
COMMITTED
RECONCILED
```

because each represents different evidence.

---

# 93. Failure Semantics

Likewise:

```text
FAILED
```

SHOULD identify where failure occurred:

```text
authorization failure
routing failure
dispatch failure
worker failure
commit failure
receipt failure
ledger failure
external rejection
reconciliation failure
```

---

# 94. Execution Uncertainty

Execution uncertainty SHOULD remain typed.

Examples:

```text
dispatch_uncertainty
worker_uncertainty
external_effect_uncertainty
receipt_uncertainty
ledger_uncertainty
reconciliation_uncertainty
```

A fluent "probably succeeded" statement MUST NOT replace unresolved execution state.

---

# 95. Unknown Execution

If available evidence cannot establish whether an effect occurred:

```text
EXECUTION_STATE = UNKNOWN
```

The system MUST NOT invent:

```text
SUCCESS
```

or:

```text
FAILURE
```

---

# 96. H/M/L Applicability

## H — Governing Execution

H-level execution concerns:

- global execution invariants;
- root routing policy;
- commit semantics;
- ledger requirements;
- authority boundaries;
- systemic retry policy;
- infrastructure governance.

---

## M — Subsystem Execution

M-level execution concerns:

- worker pools;
- queues;
- service routing;
- transaction coordinators;
- domain execution engines;
- subsystem receipts;
- subsystem reconciliation.

---

## L — Local Effect

L-level execution concerns:

- one tool call;
- one file write;
- one message;
- one transaction;
- one API mutation;
- one database commit.

Every L-level consequential effect MUST remain within applicable H/M governance.

---

# 97. Cross-Scale Execution

Conceptually:

```text
H execution constraints
        ↓
M worker/routing constraints
        ↓
L concrete effect
```

A local worker cannot bypass a governing execution invariant merely because the local operation is technically valid.

---

# 98. Control-Plane Ownership

L8 execution governance belongs primarily to infrastructure/control-plane functions.

The domain worker proposes or performs domain-specific mechanics.

The infrastructure owns:

```text
route
eligibility
authority freshness
policy freshness
transaction identity
idempotency
commit gating
receipt contract
ledger contract
reconciliation state
```

This preserves separation between domain cognition and execution authority.

---

# 99. Worker Contract

An L8-conformant worker SHOULD:

1. accept only governed dispatches;
2. verify dispatch integrity;
3. preserve transaction identity;
4. preserve idempotency identity;
5. preserve effect digest;
6. refuse material unauthorized mutation;
7. participate in commit-time revalidation;
8. produce typed outcome state;
9. return a receipt where required;
10. avoid blind redispatch;
11. preserve unknown outcomes;
12. expose reconciliation references where available.

---

# 100. Router Contract

An L8-conformant router SHOULD:

1. identify the effect class;
2. select only eligible workers;
3. enforce `I-RPOL-017` if confirmed by authoritative runtime;
4. preserve dispatch bindings;
5. prevent direct ungoverned effect paths;
6. preserve transaction and idempotency identity;
7. record dispatch provenance;
8. fail closed when no valid worker path exists.

---

# 101. Committer Contract

A commit component SHOULD:

1. identify the exact effect;
2. resolve current authority;
3. resolve current policy;
4. validate current constraints;
5. compare load-bearing observed state;
6. validate effect digest;
7. validate idempotency state;
8. reject stale or conflicting execution;
9. commit only after all required gates pass;
10. emit commitment evidence.

---

# 102. Ledger Contract

The ledger SHOULD preserve enough state to reconstruct:

```text
what was intended
what was authorized
what was dispatched
what worker acted
what effect was identified
what attempts occurred
what outcome was observed
what was committed
what receipt was produced
what retries occurred
what compensation occurred
```

The ledger SHOULD be append-preserving or otherwise auditable according to authoritative implementation requirements.

---

# 103. Receipt Contract

A receipt SHOULD be:

```text
typed
effect-bound
transaction-bound
worker-attributable
timestamped
ledger-linkable
```

where technically possible.

A receipt MUST NOT silently mutate the effect identity.

---

# 104. Reconciliation Contract

Reconciliation SHOULD be invoked when:

```text
timeout
worker crash
receipt missing
ledger mismatch
duplicate uncertainty
external-state mismatch
partial effect
unknown outcome
```

Reconciliation SHOULD prefer observation over redispatch.

---

# 105. Execution Failure Modes

L8 recognizes at least:

### EF-1 — Direct Effect Bypass

Consequential effect bypasses governed worker path.

### EF-2 — Stale Commit Authorization

Request-time authorization is reused after becoming stale.

### EF-3 — Missing Commit Revalidation

Commit occurs without required current-state validation.

### EF-4 — Blind Redispatch

Unknown outcome is retried without reconciliation/idempotency.

### EF-5 — Duplicate Effect

Retry produces another logical effect.

### EF-6 — Idempotency Collision

Same key binds different effects.

### EF-7 — Missing Effect Digest

Effect cannot be reliably matched across execution artifacts.

### EF-8 — Digest Mismatch

Proposal, witness, receipt, or ledger refer to different effects.

### EF-9 — Receipt Loss

Effect may exist but receipt is absent.

### EF-10 — Ledger Loss

Effect may exist but ledger entry is absent.

### EF-11 — Partial Effect Collapse

Partial execution is incorrectly reported as total success/failure.

### EF-12 — Timeout-as-Failure

Timeout is incorrectly treated as proof of no effect.

### EF-13 — Replay Execution

Historical dispatch is executed as a new effect.

### EF-14 — Stale Queue Execution

Queued operation executes after its authority envelope becomes invalid.

### EF-15 — Worker Scope Escape

Worker performs effect outside permitted class.

### EF-16 — Unauthorized Effect Mutation

Worker changes material effect parameters after validation.

### EF-17 — Retry Authority Drift

Retry uses stale authority.

### EF-18 — Unbounded Retry

Execution continues beyond governed retry budget.

### EF-19 — False Exactly-Once Claim

Subsystem delivery semantics are generalized to external effect semantics.

### EF-20 — Simulation/Reality Collapse

Dry-run or simulated result is reported as actual effect.

---

# 106. Recovery Flow

Canonical conceptual recovery:

```text
DETECT EXECUTION ANOMALY
        ↓
FREEZE BLIND REDISPATCH
        ↓
IDENTIFY LOGICAL OPERATION
        ↓
IDENTIFY ATTEMPTS
        ↓
RESOLVE IDEMPOTENCY KEY
        ↓
RESOLVE EFFECT DIGEST
        ↓
CHECK RECEIPT
        ↓
CHECK LEDGER
        ↓
CHECK WORKER STATE
        ↓
CHECK EXTERNAL STATE
        ↓
CLASSIFY OUTCOME
        ↓
COMMITTED / NOT_COMMITTED / PARTIAL / UNKNOWN
        ↓
REVALIDATE AUTHORITY + POLICY
        ↓
ACCEPT / RETRY / COMPENSATE / ABORT / ESCALATE
        ↓
WRITE RECONCILIATION EVIDENCE
```

---

# 107. Selective Recovery

Execution failure SHOULD invalidate only affected execution descendants where possible.

Example:

```text
E1 → E2
E3 independent
```

If `E1` fails:

```text
invalidate E2 eligibility
```

while preserving `E3` if its invariants remain valid.

This follows the AMOS selective-invalidation principle.

---

# 108. Minimum Validator Families

Conceptual validators include:

```text
validate_worker_path()
validate_worker_eligibility()
validate_dispatch_integrity()

validate_commit_authority()
validate_commit_policy()
validate_commit_scope()
validate_commit_read_set()

validate_idempotency_key()
validate_idempotency_effect_binding()
validate_retry_eligibility()
validate_retry_budget()

validate_effect_digest()
validate_digest_binding()

validate_receipt()
validate_receipt_digest()
validate_ledger_entry()
validate_receipt_ledger_agreement()

validate_transaction_dependencies()
validate_atomic_effect_set()

validate_unknown_outcome_handling()
validate_reconciliation()
```

These are conceptual responsibilities, not claims about exact runtime function names.

---

# 109. Supplied Enforcement Claims

The supplied artifact identifies:

```text
INV-030 — commit-time authorization revalidation
INV-031 — effect digest / ledger
INV-032 — idempotency
INV-033 — retry / blind redispatch protection
I-RPOL-017 — worker path gating
03_CONTROL_PLANE — receipt / ledger contracts
```

Preserved evidence classification:

```yaml
implementation_claims:

  INV_030:
    claimed_role: commit_time_revalidation
    evidence_class: SOURCE_CLAIM

  INV_031:
    claimed_role: effect_digest_ledger
    evidence_class: SOURCE_CLAIM

  INV_032:
    claimed_role: idempotency
    evidence_class: SOURCE_CLAIM

  INV_033:
    claimed_role: retry_redispatch_control
    evidence_class: SOURCE_CLAIM

  I_RPOL_017:
    claimed_role: worker_path_gating
    evidence_class: SOURCE_CLAIM

  control_plane_receipt_ledger:
    location: 03_CONTROL_PLANE
    evidence_class: SOURCE_CLAIM

independent_runtime_verification:
  status: NOT_ESTABLISHED_HERE
```

---

# 110. Minimum Execution Tests

## L8-T1 — Direct Effect Bypass

Input:

```text
planner attempts consequential direct effect
without governed worker route
```

Expected:

```text
REJECT
```

---

## L8-T2 — Valid Worker Route

Input:

```text
authorized effect
eligible worker
valid route
```

Expected:

```text
ROUTE_ALLOWED
```

subject to later commit validation.

---

## L8-T3 — Revocation Before Commit

Input:

```text
authority valid at request
revoked before commit
```

Expected:

```text
COMMIT = DENIED
```

---

## L8-T4 — Policy Change Before Commit

Input:

```text
policy allow at request
policy deny at commit
```

Expected:

```text
COMMIT = DENIED
```

---

## L8-T5 — Effect Mutation

Input:

```text
validated digest = D1
commit digest = D2
D1 != D2
```

Expected:

```text
COMMIT = DENIED / REVALIDATE
```

---

## L8-T6 — Idempotent Retry

Input:

```text
same logical operation
same idempotency key
same effect digest
first response lost
effect already committed
```

Expected:

```text
NO DUPLICATE EFFECT
RETURN/RECOVER EXISTING RESULT
```

---

## L8-T7 — Idempotency Conflict

Input:

```text
same key K
digest D1 already registered
new request digest D2
D1 != D2
```

Expected:

```text
IDEMPOTENCY_CONFLICT
```

---

## L8-T8 — Blind Redispatch

Input:

```text
attempt times out
outcome unknown
no reconciliation
retry requested
```

Expected:

```text
RETRY BLOCKED
```

---

## L8-T9 — Missing Receipt

Input:

```text
worker may have committed
receipt missing
```

Expected:

```text
UNKNOWN_OUTCOME
RECONCILE
```

not automatic retry.

---

## L8-T10 — Missing Ledger

Input:

```text
external effect confirmed
ledger entry absent
```

Expected:

```text
RECONCILIATION_REQUIRED
```

---

## L8-T11 — Duplicate Dispatch

Input:

```text
same dispatch delivered twice
same valid idempotency identity
```

Expected:

```text
ONE LOGICAL EFFECT
```

---

## L8-T12 — Stale Queue Item

Input:

```text
queued while authorized
authority revoked before worker commit
```

Expected:

```text
COMMIT = DENIED
```

---

## L8-T13 — Worker Scope Escape

Input:

```text
worker authorized for effect class A
dispatch requires effect class B
```

Expected:

```text
WORKER_INELIGIBLE
```

---

## L8-T14 — Partial Transaction

Input:

```text
E1 committed
E2 failed
E3 pending
```

Expected:

```text
PARTIAL
```

plus transaction-specific recovery.

---

## L8-T15 — Dry Run

Input:

```text
simulation succeeds
no external commit
```

Expected:

```text
SIMULATION_SUCCESS
```

not:

```text
REAL_EFFECT_COMMITTED
```

---

## L8-T16 — Timeout

Input:

```text
external call times out after dispatch
```

Expected:

```text
UNKNOWN_OUTCOME
```

unless infrastructure proves no effect.

---

## L8-T17 — Retry After Revocation

Input:

```text
attempt 1 authorized
attempt 1 unknown
authority revoked
retry attempted
```

Expected:

```text
RETRY = DENIED
```

---

# 111. Falsifiers

This specification requires revision if:

1. authoritative execution canon defines a materially different effect pipeline;
2. consequential effects are canonically permitted outside governed worker paths;
3. commit-time authorization is not required under authoritative semantics;
4. `INV-030` has materially different meaning;
5. `INV-031` does not govern effect digest/ledger semantics;
6. `INV-032` or `INV-033` has materially different retry/idempotency semantics;
7. `I-RPOL-017` does not govern worker-path routing;
8. authoritative execution canon permits blind redispatch;
9. effect digests are not required for governed effects;
10. receipt/ledger contracts differ materially from this proposed structure;
11. higher-order canon supersedes E-1 through E-4.

---

# 112. Core Invariants

## L8-I1 — Worker Path

```text
CONSEQUENTIAL_EFFECT
→
GOVERNED_WORKER_PATH
```

## L8-I2 — No Direct Bypass

```text
UNGOVERNED_DIRECT_EFFECT
→
DENY
```

## L8-I3 — Commit Revalidation

```text
COMMIT
→
CURRENT_AUTHORITY_CHECK
```

## L8-I4 — Request Approval Is Insufficient

```text
REQUEST_TIME_ALLOW
!=
COMMIT_TIME_ALLOW
```

## L8-I5 — Effect Binding

```text
VALIDATED_EFFECT
=
COMMITTED_EFFECT
```

within canonical equivalence.

## L8-I6 — Idempotent Retry

```text
RETRY(SAME_LOGICAL_OPERATION)
→
NO_DUPLICATE_LOGICAL_EFFECT
```

## L8-I7 — No Blind Redispatch

```text
UNKNOWN_OUTCOME
→
RECONCILE_BEFORE_NON_IDEMPOTENT_RETRY
```

## L8-I8 — Idempotency Conflict

```text
SAME_KEY
+
DIFFERENT_EFFECT
→
CONFLICT
```

## L8-I9 — Effect Digest

```text
GOVERNED_EFFECT
→
EFFECT_DIGEST
```

## L8-I10 — Ledger Binding

```text
EFFECT_DIGEST
→
LEDGER_RECORD
```

## L8-I11 — Receipt Binding

```text
RECEIPT
→
EFFECT_IDENTITY
```

## L8-I12 — Timeout Ambiguity

```text
TIMEOUT
!=
NO_EFFECT
```

## L8-I13 — Missing Receipt Ambiguity

```text
NO_RECEIPT
!=
NO_EFFECT
```

## L8-I14 — Retry Reauthorization

```text
RETRY
→
CURRENT_COMMIT_VALIDATION
```

## L8-I15 — Simulation Separation

```text
SIMULATED_EFFECT
!=
REAL_EFFECT
```

## L8-I16 — Selective Failure Propagation

```text
FAIL(E)
→
INVALIDATE(DEPENDENTS(E))
```

unless atomic transaction semantics require broader abort.

## L8-I17 — Compensation Is an Effect

```text
COMPENSATION
→
GOVERNED_EXECUTION
```

---

# 113. Hard Boundaries

```text
INTENT != EFFECT

PROPOSAL != EXECUTION

APPROVAL != COMMITMENT

DISPATCH != EFFECT

EXECUTION != COMMITMENT

TIMEOUT != FAILURE

NO_RECEIPT != NO_EFFECT

NO_LEDGER_ENTRY != NO_EFFECT

RETRY != NEW INTENTION

IDEMPOTENCY_KEY != AUTHORITY

EFFECT_DIGEST != EFFECT_OCCURRENCE

RECEIPT != INDEPENDENT REALITY PROOF

SIMULATION != REALITY

ROLLBACK != COMPENSATION

AT_LEAST_ONCE DELIVERY != DUPLICATE EFFECT PERMISSION

EXACTLY_ONCE SUBSYSTEM PROCESSING
!=
EXACTLY_ONCE EXTERNAL EFFECT

WORKER_CAPABILITY != WORKER_AUTHORITY

REQUEST_TIME_AUTHORIZATION != COMMIT_TIME_AUTHORIZATION

UNKNOWN_OUTCOME != SAFE_TO_REDISPATCH

UNKNOWN/GAP != SUCCESS
```

---

# 114. Dependencies

Primary conceptual dependency spine:

```text
L0_INTEGRITY
    ↓
L1_EPISTEMIC
    ↓
L2_PROVENANCE
    ↓
L3_DEPENDENCY
    ↓
L4_CAUSAL
    ↓
L5_SCOPE_REGIME
    ↓
L6_UNCERTAINTY
    ↓
L7_AUTHORITY
    ↓
L8_EXECUTION
```

L8 depends materially on:

```yaml
dependencies:

  L0_INTEGRITY:
    role: prevents fabricated execution state and bypass

  L1_EPISTEMIC:
    role: separates observed execution evidence from assumptions

  L2_PROVENANCE:
    role: binds requests, workers, receipts, and ledger entries

  L3_DEPENDENCY:
    role: controls effect ordering and selective failure propagation

  L4_CAUSAL:
    role: preserves ordering between authorization changes and effects

  L5_SCOPE_REGIME:
    role: binds execution to environment, time, resource, and regime

  L6_UNCERTAINTY:
    role: preserves UNKNOWN execution outcomes

  L7_AUTHORITY:
    role: supplies authority witnesses and commit-time authorization requirements
```

---

# 115. Related Execution Infrastructure

L8 conceptually interfaces with:

```text
03_CONTROL_PLANE
ROUTING_POLICY
WORKER_REGISTRY
WORKER_CONTRACT
EXECUTION_ENVELOPE
COMMIT_GATE
AUTHORITY_RESOLVER
AUTHORITY_WITNESS
POLICY_ENGINE
IDEMPOTENCY_REGISTRY
EFFECT_DIGEST
RECEIPT
EXECUTION_LEDGER
TRANSACTION_COORDINATOR
RECONCILIATION
ROLLBACK
COMPENSATION
```

Names are conceptual unless matched to authoritative corpus/runtime artifacts.

---

# 116. Agent Contract

An L8-conformant agent SHOULD:

1. produce an intention or proposal rather than direct consequential effect;
2. route consequential execution through governed infrastructure;
3. preserve authority and effect bindings;
4. never treat request-time approval as permanent authorization;
5. never blind-retry an unknown consequential outcome;
6. preserve idempotency identity;
7. preserve effect digest;
8. distinguish attempt from logical operation;
9. preserve partial and unknown states;
10. distinguish simulation from committed reality;
11. reconcile before redispatch where outcome is ambiguous;
12. expose execution gaps rather than fabricate success.

---

# 117. Skill Contract

A consequential Skill SHOULD declare:

```yaml
execution_contract:
  consequential_effects: true
  governed_worker_required: true

  commit_revalidation: true

  idempotency:
    required_for_retryable_effects: true
    blind_redispatch: prohibited

  effect_digest:
    required: true
    ledger_record_required: true

  receipt:
    required: true

  unknown_outcome:
    behavior: RECONCILE

  retry:
    bounded: true
    reauthorize_at_commit: true
```

This is a proposed contract schema, not a claim of exact current runtime format.

---

# 118. Workflow Contract

Canonical conceptual execution workflow:

```text
1. RECEIVE APPROVED PROPOSAL
2. IDENTIFY LOGICAL OPERATION
3. IDENTIFY EFFECT
4. CANONICALIZE EFFECT
5. COMPUTE / RESOLVE EFFECT DIGEST
6. ASSIGN IDEMPOTENCY IDENTITY
7. RESOLVE ELIGIBLE WORKER
8. VALIDATE GOVERNED ROUTE
9. CREATE DISPATCH ENVELOPE
10. PREPARE EFFECT
11. RESOLVE CURRENT AUTHORITY
12. RESOLVE CURRENT POLICY
13. VALIDATE OBSERVED READ SET
14. VALIDATE EFFECT DIGEST
15. VALIDATE IDEMPOTENCY STATE
16. CROSS COMMIT GATE
17. EXECUTE EFFECT
18. CLASSIFY OUTCOME
19. CREATE RECEIPT
20. RECORD LEDGER ENTRY
21. RECONCILE IF AMBIGUOUS
22. RETRY ONLY IF GOVERNED AND SAFE
23. COMPENSATE / ROLLBACK IF REQUIRED
24. RETURN TYPED EXECUTION RESULT
```

---

# 119. Protocol Contract

```yaml
EXECUTION_REQUEST:
  logical_operation_id: ...
  principal: ...
  action: ...
  resource: ...
  expected_effect: ...
  authority_witness: ...
  policy_reference: ...

EXECUTION_IDENTITY:
  execution_id: ...
  transaction_id: ...
  idempotency_key: ...
  effect_digest: ...

ROUTING:
  worker_id: ...
  routing_policy: ...
  worker_eligible: true

PREPARE:
  observed_read_set: ...
  reversible_until: ...

COMMIT_VALIDATION:
  authority_current: ...
  policy_current: ...
  scope_valid: ...
  constraints_valid: ...
  digest_valid: ...
  idempotency_valid: ...

EXECUTION:
  attempt_id: ...
  attempt_number: ...
  worker: ...
  started_at: ...

OUTCOME:
  state: COMMITTED | FAILED | PARTIAL | ABORTED | UNKNOWN
  external_reference: ...

RECEIPT:
  effect_digest: ...
  outcome: ...
  committed_at: ...

LEDGER:
  entry_id: ...
  receipt_reference: ...
  effect_digest: ...

RECONCILIATION:
  required: true | false
  state: ...
```

---

# 120. RSCF Completion State

```yaml
claim_class: AMOS_MODEL

claim:
  "L8_EXECUTION governs the conversion of approved intentions into effects
   through infrastructure-governed workers, commit-time revalidation,
   idempotent retry semantics, effect digests, receipts, and ledger-bound
   execution evidence."

evidence:
  - supplied E-1 Worker-Only Effects law
  - supplied E-2 Commit-Time Revalidation law
  - supplied E-3 Idempotency law
  - supplied E-4 Effect Digests law
  - supplied INV-030 reference
  - supplied INV-031 reference
  - supplied INV-032 reference
  - supplied INV-033 reference
  - supplied I-RPOL-017 reference
  - supplied 03_CONTROL_PLANE receipt/ledger reference

provenance:
  origin_architect: Trang Phan
  artifact_family: AMOS_OS
  layer: 01_CANON/01_CORE_LAWS
  path: 01_CANON/01_CORE_LAWS/L8_EXECUTION.md
  derivation_status: PROPOSED_STRUCTURAL_COMPLETION
  updated: 2026-08-26

scope:
  system: AMOS
  applies_to:
    - consequential_effects
    - workers
    - routing
    - dispatch
    - commit
    - retries
    - idempotency
    - receipts
    - ledgers
    - reconciliation
    - rollback
    - compensation

regime:
  - infrastructure
  - control_plane
  - execution
  - transaction
  - persistent_effect
  - external_effect

freshness:
  revalidate_on:
    - commit
    - authority_change
    - policy_change
    - resource_change
    - effect_mutation
    - worker_change
    - environment_change
    - retry
    - reconciliation

dependencies:
  - L0_INTEGRITY
  - L1_EPISTEMIC
  - L2_PROVENANCE
  - L3_DEPENDENCY
  - L4_CAUSAL
  - L5_SCOPE_REGIME
  - L6_UNCERTAINTY
  - L7_AUTHORITY

competing:
  - authoritative execution canon may define a different worker/effect pipeline
  - runtime transaction semantics may differ from the proposed state machine
  - exact digest canonicalization is unknown
  - exact idempotency registry semantics are unknown
  - exact receipt and ledger schemas are unknown

falsifiers:
  - authoritative canon supersedes E-1 through E-4
  - INV-030..033 meanings materially differ
  - I-RPOL-017 does not govern worker paths
  - effect digests are not required
  - blind redispatch is canonically permitted
  - receipt/ledger contracts materially differ
  - runtime evidence contradicts supplied enforcement claims

confidence_ceiling:
  seed_laws: HIGH
  structural_completion: AMOS_MODEL
  exact_canon_equivalence: UNVERIFIED
  implementation_references: SOURCE_CLAIM
  runtime_verification: NOT_ESTABLISHED_HERE
```

---

# 121. Gap Status

```yaml
gap_status:

  seed_laws:
    E_1_WORKER_ONLY_EFFECTS: PROVIDED
    E_2_COMMIT_TIME_REVALIDATION: PROVIDED
    E_3_IDEMPOTENCY: PROVIDED
    E_4_EFFECT_DIGESTS: PROVIDED

  structural_completion:
    execution_boundary: PROVIDED
    execution_state_machine: PROVIDED
    worker_contract: PROVIDED
    routing_contract: PROVIDED
    commit_contract: PROVIDED
    retry_model: PROVIDED
    idempotency_model: PROVIDED
    digest_model: PROVIDED
    receipt_model: PROVIDED
    ledger_model: PROVIDED
    reconciliation_model: PROVIDED
    failure_modes: PROVIDED
    recovery: PROVIDED
    validators: PROVIDED
    tests: PROVIDED
    dependencies: PROVIDED
    hml_applicability: PROVIDED
    rscf_capsule: PROVIDED

  unresolved:
    authoritative_execution_canon_reconciliation: REQUIRED
    exact_worker_runtime: UNVALIDATED
    exact_commit_pipeline: UNVALIDATED
    INV_030_mapping: REQUIRED
    INV_031_mapping: REQUIRED
    INV_032_mapping: REQUIRED
    INV_033_mapping: REQUIRED
    I_RPOL_017_mapping: REQUIRED
    exact_effect_digest_algorithm: UNKNOWN
    exact_effect_canonicalization: UNKNOWN
    exact_idempotency_registry: UNKNOWN
    exact_receipt_schema: UNKNOWN
    exact_ledger_schema: UNKNOWN
    exact_atomicity_guarantees: UNKNOWN
    runtime_execution_tests: REQUIRED
    final_canon_approval: REQUIRED
```

---

# 122. Canon Promotion Gate

Before final canon promotion:

```text
[ ] Trang Phan / steward approval
[ ] authoritative execution canon reconciled
[ ] E-1 confirmed
[ ] E-2 confirmed
[ ] E-3 confirmed
[ ] E-4 confirmed
[ ] worker-only effect semantics confirmed
[ ] commit boundary confirmed
[ ] commit-time revalidation semantics confirmed
[ ] retry semantics confirmed
[ ] idempotency semantics confirmed
[ ] effect digest semantics confirmed
[ ] canonical effect representation confirmed
[ ] receipt contract confirmed
[ ] ledger contract confirmed
[ ] reconciliation contract confirmed
[ ] transaction semantics confirmed
[ ] rollback semantics confirmed
[ ] compensation semantics confirmed
[ ] INV-030 inspected and mapped
[ ] INV-031 inspected and mapped
[ ] INV-032 inspected and mapped
[ ] INV-033 inspected and mapped
[ ] I-RPOL-017 inspected and mapped
[ ] 03_CONTROL_PLANE contracts inspected
[ ] direct-effect bypass tests executed
[ ] stale-authorization tests executed
[ ] duplicate-delivery tests executed
[ ] blind-redispatch tests executed
[ ] timeout/unknown-outcome tests executed
[ ] receipt-loss tests executed
[ ] ledger-loss tests executed
[ ] partial-effect tests executed
[ ] simulation/reality separation tests executed
[ ] downstream dependencies inspected
[ ] supersession lineage recorded
[ ] version assigned
```

Until then:

```text
STATUS = PROPOSED_SPECIFICATION
EPISTEMIC_CLASS = AMOS_MODEL
CANONICAL_STATUS = CONDITIONAL
IMPLEMENTATION_STATUS = LOGIC_EXECUTABLE_IN_PART
```

not:

```text
STATUS = VERIFIED_FINAL_CANON
```

---

# 123. Final L8 Law Summary

The L8 execution boundary reduces to four supplied governing laws:

```text
E-1

CONSEQUENTIAL EFFECT
→
INFRASTRUCTURE-GOVERNED WORKER PATH
```

```text
E-2

REQUEST-TIME AUTHORIZATION
IS INSUFFICIENT

COMMIT
→
AUTHORIZATION REVALIDATION
```

```text
E-3

RETRY
→
IDEMPOTENT OPERATION

UNKNOWN OUTCOME
→
NO BLIND REDISPATCH
```

```text
E-4

EVERY GOVERNED EFFECT
→
EFFECT DIGEST
→
LEDGER RECORD
```

The resulting execution rule is conceptually:

```text
COMMIT_ALLOWED
IFF

GOVERNED_WORKER_PATH
AND
WORKER_ELIGIBLE
AND
AUTHORITY_CURRENT
AND
POLICY_CURRENT
AND
SCOPE_VALID
AND
CONSTRAINTS_VALID
AND
EFFECT_UNCHANGED
AND
IDEMPOTENCY_VALID
AND
EFFECT_DIGEST_VALID
```

For retries:

```text
UNKNOWN_OUTCOME
→
RECONCILE
→
REVALIDATE
→
RETRY ONLY IF SAFE
```

For evidence:

```text
EFFECT
→
DIGEST
→
RECEIPT
→
LEDGER
```

while preserving:

```text
DIGEST != EFFECT OCCURRENCE
RECEIPT != INDEPENDENT REALITY PROOF
LEDGER ENTRY != EXTERNAL EFFECT BY ITSELF
```

The governing execution principle is therefore:

```text
APPROVED INTENTION
+
GOVERNED WORKER
+
CURRENT AUTHORITY
+
SAFE COMMIT
+
IDEMPOTENT EFFECT IDENTITY
+
AUDITABLE EXECUTION EVIDENCE
=
ELIGIBLE GOVERNED EFFECT
```

not:

```text
MODEL DECIDED TO DO IT
→
EFFECT IS ALLOWED
```

---

[[00_ROOT_MOC]]|[[AMOS MOC]]

---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[L0_INTEGRITY]] · [[L1_EPISTEMIC]] · [[L2_PROVENANCE]] · [[L3_DEPENDENCY]] · [[L4_CAUSAL]] · [[L5_SCOPE_REGIME]] · [[L6_UNCERTAINTY]] · [[L7_AUTHORITY]] · 03_CONTROL_PLANE · [[ROUTING_POLICY]] · WORKER_REGISTRY · WORKER_CONTRACT · COMMIT_GATE · [[AUTHORITY_RESOLVER]] · [[AUTHORITY_WITNESS]] · IDEMPOTENCY_REGISTRY · EFFECT_DIGEST · RECEIPT · EXECUTION_LEDGER · RECONCILIATION

---

RSCF-NODE

node_id: l8_execution

node_type: core_law

path: 01_CANON/01_CORE_LAWS/L8_EXECUTION.md

RSCF-RELATIONS:

- CHILD_OF: [[LAW_HIERARCHY]]
- DEPENDS_ON: [[L0_INTEGRITY]]
- DEPENDS_ON: [[L1_EPISTEMIC]]
- DEPENDS_ON: [[L2_PROVENANCE]]
- DEPENDS_ON: [[L3_DEPENDENCY]]
- DEPENDS_ON: [[L4_CAUSAL]]
- DEPENDS_ON: [[L5_SCOPE_REGIME]]
- DEPENDS_ON: [[L6_UNCERTAINTY]]
- DEPENDS_ON: [[L7_AUTHORITY]]
- GOVERNS: [[ROUTING_POLICY]]
- GOVERNS: WORKER_CONTRACT
- GOVERNS: COMMIT_GATE
- GOVERNS: IDEMPOTENCY_REGISTRY
- GOVERNS: EFFECT_DIGEST
- GOVERNS: RECEIPT
- GOVERNS: EXECUTION_LEDGER
- GOVERNS: RECONCILIATION
- CONSTRAINS: 03_CONTROL_PLANE
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]

claim_class: AMOS_MODEL

```
```

---
**MOC:** [[01_CORE_LAWS_MOC]]
