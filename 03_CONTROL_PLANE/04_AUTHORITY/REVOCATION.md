---
tags: ['control_plane', 'authority', 'note']
---

# REVOCATION.md

---
title: "AMOS Revocation Architecture"
artifact: "REVOCATION.md"
origin_architect: "Trang Phan"
steward: "Trang Phan"
system: "AMOS OS"
artifact_class: "GOVERNED_AUTHORITY_REVOCATION_CONTRACT"
status: "PROPOSED / STRUCTURALLY_COMPLETE / IMPLEMENTATION-UNVALIDATED"
epistemic_class: "MODEL"
version: "1.0.0"
updated: "2026-08-26"
default_state: "UNKNOWN_GAP"
---

# AMOS Revocation Architecture

## 0. Status

`REVOCATION.md` defines the AMOS OS contract for withdrawing, narrowing, suspending, superseding, or invalidating previously recognized authority and for propagating that change through every dependent authority, delegation, witness, authorization, reservation, transaction, cache, and proposed effect that relies upon the revoked state.

Revocation is a control-plane authority operation.

It is not merely:

```text
deleting a record;

changing a role label;

removing a UI permission;

clearing a cache;

stopping an agent;

changing a policy;

marking an object inactive;

or writing "revoked" into memory.
```

The canonical revocation path is:

```text
REVOCATION TRIGGER
      ↓
REVOCATION REQUEST
      ↓
REVOCATION AUTHORITY
      ↓
TARGET RESOLUTION
      ↓
CURRENT STATE / VERSION
      ↓
DEPENDENCY CLOSURE
      ↓
INDEPENDENT-PATH ANALYSIS
      ↓
REVOCATION DECISION
      ↓
ATOMIC STATE TRANSITION
      ↓
DEPENDENT INVALIDATION
      ↓
WITNESS INVALIDATION
      ↓
AUTHORIZATION INVALIDATION
      ↓
RESERVATION / TRANSACTION REVIEW
      ↓
COMMIT-TIME REVALIDATION
      ↓
AUDIT / PROVENANCE
```

Never:

```text
REVOCATION_REQUEST
=
REVOCATION_COMMIT
```

---

# 1. Purpose

The purpose of revocation is to ensure that authority which is no longer valid cannot continue producing governed effects through stale state, descendants, cached witnesses, previously allowed policy decisions, delegated agents, queued workflows, or transactions that have not yet crossed their authoritative commit boundary.

Revocation MUST preserve:

```text
identity;

authority lineage;

revocation authority;

target precision;

scope;

time;

reason;

dependency closure;

independent authority paths;

transaction state;

provenance;

auditability;

and recovery semantics.
```

The governing question is:

> **Has this authority or authority-bearing object ceased to be valid, for whom, for what scope, from what effective time, under whose authority, and which dependent states must therefore be invalidated before further effects may commit?**

---

# 2. Core Revocation Laws

```text
REVOCATION != DELETION

REVOCATION != EXPIRATION

REVOCATION != SUSPENSION

REVOCATION != SUPERSESSION

REVOCATION != POLICY_DENY

REVOCATION != AUTHORIZATION_DENY

REVOCATION != CAPABILITY_REMOVAL

REVOCATION != AGENT_TERMINATION

REVOCATION != MEMORY_ERASURE

REVOCATION_REQUEST != REVOCATION_COMMIT

REVOCATION_AUTHORITY != TARGET_AUTHORITY

CAPABILITY_TO_REVOKE != AUTHORITY_TO_REVOKE

ROLE != REVOCATION_AUTHORITY

POLICY_ALLOW != REVOCATION_AUTHORITY

STALE_ALLOW != CURRENT_AUTHORITY

REVOKED_PARENT != VALID_DEPENDENT_CHILD

REVOKED_ROOT != VALID_DEPENDENT_BRANCH

REVOKED_DELEGATION != VALID_DEPENDENT_WITNESS

REVOKED_AUTHORITY != VALID_NEW_COMMIT

INDEPENDENT_AUTHORITY_PATH != REVOKED_DEPENDENT_PATH

PARTIAL_REVOCATION != TOTAL_REVOCATION

SUSPENSION != PERMANENT_REVOCATION

SUPERSESSION != SILENT MUTATION

UNKNOWN_REVOCATION_STATE != ACTIVE

CONFLICTING_REVOCATION_STATE != ALLOW

PROPOSAL != COMMIT

UNKNOWN/GAP != PASS
```

---

# 3. Definition

A revocation is a provenance-bound authority state transition that removes or restricts the future validity of a previously recognized authority object or authority path.

Conceptually:

```text
R =
(
    revocation_id,
    revoker,
    revocation_authority,
    target,
    target_version,
    mode,
    scope,
    effective_time,
    reason,
    dependency_policy,
    transaction_policy,
    recovery_policy,
    provenance
)
```

The result is not necessarily destruction of the historical object.

Instead:

```text
historical authority record
+
revocation state
=
historically reconstructable but no longer currently usable authority
```

---

# 4. Revocation Equation

AMOS MODEL:

```text
ValidRevocation(R,t)
=
RevokerIdentityValid(R,t)
∧ RevocationAuthorityValid(R,t)
∧ TargetExists(R)
∧ TargetVersionValid(R)
∧ RevocationScopeAuthorized(R)
∧ RevocationModeValid(R)
∧ EffectiveTimeValid(R,t)
∧ DependencyRulesValid(R)
∧ ProvenanceValid(R)
∧ ConflictFreeOrFailClosed(R)
```

For dependent authority:

```text
ValidDependentAuthority(A,t)
=
ValidOwnAuthority(A,t)
∧
∀ p ∈ LoadBearingParents(A):
    Valid(p,t)
```

unless another independently valid authority path supports the same effective authority.

---

# 5. Architectural Position

```text
IDENTITY
   ↓
AUTHORITY REGISTRY
   ↓
DELEGATION
   ↓
AUTHORITY GRAPH
   ↓
REVOCATION REGISTRY
   ↓
REVOCATION ENGINE
   ↓
AUTHORITY RESOLVER
   ↓
AUTHORITY WITNESS
   ↓
POLICY ENGINE
   ↓
AUTHORIZATION ENGINE
   ↓
TRANSACTION CONTROL
   ↓
COMMIT GUARD
```

Revocation modifies authority validity.

The authority resolver consumes that validity.

Authorization consumes the resulting current authority witness.

---

# 6. Responsibility Boundary

The revocation subsystem owns or governs:

```text
revocation requests;

revocation authority validation;

target resolution;

revocation state;

partial revocation;

full revocation;

branch revocation;

suspension where configured;

revocation effective time;

revocation propagation;

dependency invalidation;

authority-witness invalidation;

revocation provenance;

revocation conflict detection;

revocation versioning;

revocation audit state.
```

It does not inherently own:

```text
identity issuance;

authentication;

root authority creation;

delegation issuance;

policy authorship;

capability implementation;

business-domain execution;

transaction execution;

or external effect completion.
```

---

# 7. Revocation Targets

A revocation target MAY be:

```text
ROOT_AUTHORITY

AUTHORITY_GRANT

DELEGATION

DELEGATED_OPERATION

DELEGATED_RESOURCE

DELEGATED_EFFECT

DELEGATED_RECIPIENT

PURPOSE_BOUND_AUTHORITY

ROLE_AUTHORITY_BINDING

AUTHORITY_WITNESS

AUTHORIZATION

RESERVATION

SESSION_AUTHORITY

TEMPORARY_AUTHORITY

EMERGENCY_AUTHORITY

BREAK_GLASS_AUTHORITY

AGENT_AUTHORITY

SKILL_AUTHORITY

WORKFLOW_AUTHORITY

TRANSACTION_AUTHORITY
```

Target classes MUST be typed.

---

# 8. Revocation Modes

Canonical modes:

```text
FULL

PARTIAL

SUBTREE

SUSPEND

SUPERSEDE

EMERGENCY

COMPROMISE

EXPIRE_BY_RULE
```

These modes MUST NOT be silently treated as equivalent.

---

# 9. Full Revocation

Full revocation invalidates the complete targeted authority envelope.

```text
Authority_target
→ REVOKED
```

No new action may rely solely on that authority.

---

# 10. Partial Revocation

Partial revocation removes only a subset.

Example:

```text
Before:
{READ, UPDATE, DELETE}

Revoke:
{DELETE}

After:
{READ, UPDATE}
```

The surviving authority MUST be explicitly recomputed.

Never infer:

```text
partial revoke
→ entire authority invalid
```

unless policy requires total invalidation.

---

# 11. Scope Revocation

A revocation may narrow resource scope.

Example:

```text
Before:
PROJECT_A/*
```

Revoke:

```text
PROJECT_A/FINANCE/*
```

Effective authority:

```text
PROJECT_A/*
EXCEPT
PROJECT_A/FINANCE/*
```

provided the authority model supports exclusions.

---

# 12. Operation Revocation

Example:

```text
Authority:
READ
UPDATE
DELETE
```

Revocation:

```text
DELETE
```

Result:

```text
READ
UPDATE
```

subject to dependency and policy recomputation.

---

# 13. Effect Revocation

Revocation may apply to effects independently of technical operations.

Example:

```text
CREATE_DRAFT = still permitted

SEND_EXTERNAL = revoked
```

This distinction is critical because:

```text
CAPABILITY_OPERATION
!=
GOVERNED_EFFECT
```

---

# 14. Recipient Revocation

Example:

```text
Before:
SEND to INTERNAL + PARTNER_A

Revoke:
PARTNER_A

After:
SEND to INTERNAL only
```

Recipient restrictions MUST propagate into authorization.

---

# 15. Purpose Revocation

Authority may be revoked for one purpose while remaining valid for another if the original authority was purpose-partitioned.

Example:

```text
READ customer record
FOR SUPPORT
```

may remain valid while:

```text
READ customer record
FOR MARKETING
```

is revoked.

---

# 16. Suspension

Suspension is temporary non-usability.

```text
ACTIVE
→ SUSPENDED
→ ACTIVE
```

A suspended authority MUST fail authorization while suspended.

Restoration MUST be governed.

---

# 17. Revocation vs Suspension

```text
SUSPENSION:
temporary invalidity with possible governed restoration

REVOCATION:
withdrawal requiring explicit reissuance or another valid authority path for restoration
```

Systems MUST NOT silently convert revocation into suspension.

---

# 18. Revocation vs Expiration

Expiration occurs because a temporal validity condition naturally fails.

```text
now > valid_until
→ EXPIRED
```

Revocation is an explicit or rule-triggered invalidation event.

Both invalidate authority, but their provenance differs.

---

# 19. Revocation vs Supersession

Supersession means:

```text
old authority version
→ SUPERSEDED

new authority version
→ CURRENT
```

Supersession MAY preserve some authority.

Revocation MAY remove authority entirely.

The transition MUST be explicit.

---

# 20. Revocation vs Policy Deny

A policy may deny one requested action while authority remains valid.

```text
AUTHORITY = VALID
POLICY = DENY
```

does not necessarily mean:

```text
AUTHORITY = REVOKED
```

Policy decision and authority lifecycle remain separate.

---

# 21. Revocation vs Authorization Deny

Authorization denial applies to a request.

Revocation changes authority state.

```text
DENY(action)
!=
REVOKE(authority)
```

---

# 22. Revocation Authority

Not every authority holder may revoke authority.

A valid revoker MUST possess an applicable revocation authority.

Conceptually:

```text
MayRevoke(P,T)
=
Authority(P,REVOKE,T)
∧ ScopeCompatible(P,T)
∧ TemporalValid(P)
∧ ConstraintsSatisfied(P,T)
```

---

# 23. Revocation Authority Sources

Revocation authority MAY derive from:

```text
original issuer;

root authority;

delegator;

designated revocation authority;

higher-order control plane;

explicit policy-bound authority;

emergency authority;

or another canonically recognized source.
```

The source MUST be explicit.

---

# 24. Delegator Revocation

A delegator MAY revoke a delegation only if the authority model grants that revocation right.

Do not assume:

```text
MAY_DELEGATE
=
MAY_REVOKE
```

although many authority regimes may intentionally bind them.

---

# 25. Revocation Request

```yaml
revocation_request:
  schema: "AMOS.REVOCATION_REQUEST"
  schema_version: "1.0"

  request_id: string
  requested_at: timestamp

  revoker:
    principal_id: string
    authority_witness_ref: string

  target:
    target_type: string
    target_id: string
    target_version: null
    target_digest: null

  mode:
    - FULL
    - PARTIAL
    - SUBTREE
    - SUSPEND
    - SUPERSEDE
    - EMERGENCY
    - COMPROMISE

  authority_subset:
    operations: []
    capabilities: []
    resources: []
    effects: []
    recipients: []
    purposes: []

  effective_at: timestamp

  reason:
    code: string
    description: string

  dependency_policy: {}

  transaction_policy: {}

  provenance: {}
```

---

# 26. Revocation Decision

```yaml
revocation_decision:
  schema: "AMOS.REVOCATION_DECISION"
  schema_version: "1.0"

  decision_id: string
  request_id: string

  state:
    - ALLOW
    - ALLOW_PARTIAL
    - DENY
    - BLOCK_AUTHORITY
    - BLOCK_SCOPE
    - BLOCK_CONFLICT
    - BLOCK_STALE
    - REVALIDATE
    - UNKNOWN_GAP

  target_state_before: string
  target_state_after: string

  effective_revocation: {}

  affected_dependencies: []
  preserved_independent_paths: []

  failed_invariants: []
  gaps: []

  evaluated_at: timestamp

  provenance: {}
```

---

# 27. Revocation Record

```yaml
revocation_record:
  schema: "AMOS.REVOCATION_RECORD"
  schema_version: "1.0"

  revocation_id: string

  target:
    type: string
    id: string
    version: null
    digest: null

  revoker:
    principal_id: string
    authority_witness_ref: string

  mode: string

  effective_scope: {}

  authority_removed:
    operations: []
    capabilities: []
    resources: []
    effects: []
    recipients: []
    purposes: []

  temporal:
    requested_at: timestamp
    committed_at: timestamp
    effective_at: timestamp

  reason:
    code: string
    description: string

  dependency_effects:
    invalidated: []
    revalidation_required: []
    preserved: []

  integrity:
    parent_state_digest: string
    revocation_digest: string

  provenance: {}
```

---

# 28. Revocation State Machine

```text
ACTIVE
  │
  ├──→ SUSPENDED
  │       │
  │       ├──→ ACTIVE
  │       └──→ REVOKED
  │
  ├──→ PARTIALLY_REVOKED
  │       │
  │       ├──→ PARTIALLY_REVOKED
  │       └──→ REVOKED
  │
  ├──→ SUPERSEDED
  │
  ├──→ EXPIRED
  │
  └──→ REVOKED
```

Additional control states:

```text
QUARANTINED

CONFLICT

REVALIDATION_REQUIRED

UNKNOWN_GAP
```

---

# 29. Terminality

A fully revoked authority SHOULD NOT transition directly back to active.

Preferred restoration:

```text
REVOKED OLD AUTHORITY
      ↓
NEW AUTHORITY ISSUANCE
      ↓
NEW AUTHORITY ID / VERSION
```

This preserves history.

---

# 30. Historical Preservation

Revocation SHOULD preserve the historical authority record.

Never require:

```text
REVOKE
→ DELETE ALL EVIDENCE
```

Historical provenance may be required for:

```text
audit;

incident reconstruction;

accountability;

replay;

dispute resolution;

or compliance.
```

---

# 31. Dependency Closure

Revocation MUST identify downstream objects whose validity depends on the target.

Potential descendants include:

```text
delegations;

redelegations;

authority witnesses;

authorization decisions;

reservations;

queued actions;

workflow states;

agent authority;

Skill authority;

transactions;

derived permissions;

cached authority decisions.
```

---

# 32. Dependency Equation

AMOS MODEL:

```text
Affected(R)
=
Descendants(Target(R))
∩
AuthorityDependentObjects
```

But:

```text
Affected
!=
all reachable objects
```

Only load-bearing dependent states should be invalidated.

---

# 33. Selective Invalidation

Core law:

```text
INVALIDATE DEPENDENTS
PRESERVE INDEPENDENTS
```

If:

```text
A depends on R1

B depends on R2
```

and:

```text
R1 revoked
```

then:

```text
A → INVALID / REVALIDATE

B → PRESERVE
```

provided no hidden dependency exists.

---

# 34. Independent Authority Paths

Suppose:

```text
ROOT_A → D1 → P

ROOT_B → D2 → P
```

Revoking:

```text
D1
```

does not necessarily eliminate P's effective authority if:

```text
D2
```

independently supports the requested action.

The authority resolver MUST recompute the result.

---

# 35. Correlated Authority Paths

Multiple paths may share ancestry.

```text
ROOT_A
 ├── D1 → P
 └── D2 → P
```

D1 and D2 are not independent roots.

If `ROOT_A` is revoked, both branches fail.

---

# 36. Root Revocation

Root revocation is high-impact.

```text
ROOT
 ├── D1
 │    └── D2
 └── D3
```

If ROOT is revoked:

```text
D1 invalid
D2 invalid
D3 invalid
```

unless separately supported by another valid root.

---

# 37. Parent Delegation Revocation

```text
ROOT
 ↓
D1
 ↓
A
 ↓
D2
 ↓
B
```

Revoke:

```text
D1
```

Then:

```text
D1 = REVOKED
D2 = INVALID_DEPENDENT
```

unless an independent authority path exists.

---

# 38. Partial Parent Revocation

Parent:

```text
READ
UPDATE
DELETE
```

Child:

```text
READ
DELETE
```

Parent revocation removes:

```text
DELETE
```

Child recomputes to:

```text
READ
```

not necessarily total invalidation.

---

# 39. Constraint Revocation Interaction

Some authority may exist only because a constraint is present.

If the governing constraint disappears or becomes invalid, the dependent authority MUST be re-evaluated.

A system MUST NOT assume that removing a constraint always increases authority.

---

# 40. Revocation Propagation

Propagation SHOULD be dependency-aware.

```text
REVOKE TARGET
      ↓
FIND DIRECT DEPENDENTS
      ↓
INVALIDATE / REVALIDATE
      ↓
FIND THEIR DEPENDENTS
      ↓
CONTINUE UNTIL CLOSURE
```

The process MUST avoid uncontrolled global invalidation where dependency structure permits narrower repair.

---

# 41. Propagation Ordering

Where causal dependencies exist, parent invalidation SHOULD precede child finalization.

Conceptually:

```text
ancestor revocation
before
dependent authority re-finalization
```

This prevents stale descendants from being revalidated against an already-invalid ancestor.

---

# 42. Revocation Epoch

An implementation MAY maintain:

```text
revocation_epoch
```

or equivalent generation/version state.

Example:

```text
authority validated at epoch 41

revocation committed at epoch 42

commit attempted at epoch 43
```

The epoch-41 witness requires revalidation.

---

# 43. Causal Epoch Finality

AMOS MODEL:

A revocation is final for dependent reasoning only after the relevant authority state has entered an authoritative committed epoch.

```text
PROPOSED_REVOCATION
!=
FINAL_REVOCATION
```

Workers MUST NOT independently infer finality from an uncommitted proposal.

---

# 44. Hardened Local Finalization

Where authority state is sharded or partitioned, a shard-local revocation MAY finalize locally only if:

```text
dependency closure is local;

authority ancestry is resolved;

no external authority edge can change the result;

provenance is sufficient;

current version is known;

and no unresolved conflict exists.
```

Otherwise escalation is required.

---

# 45. Proof-Based Coordination Avoidance

Global coordination SHOULD NOT be required when the control plane can prove that:

```text
the revocation target;

all load-bearing dependents;

all relevant authority roots;

and all affected reservations
```

are contained within a closed local dependency set.

If that proof cannot be established:

```text
LOCAL_FINALIZATION
→ BLOCK / ESCALATE
```

---

# 46. Authority Witness Invalidation

Any authority witness relying on revoked authority becomes stale.

```text
WITNESS
depends_on
AUTHORITY_A
```

If:

```text
AUTHORITY_A → REVOKED
```

then:

```text
WITNESS → INVALID / STALE
```

---

# 47. Witness Dependency Set

Authority witnesses SHOULD carry sufficient dependency information to support selective invalidation.

Example:

```yaml
authority_witness:
  witness_id: "AW-100"

  dependencies:
    - authority_id: "A-1"
      version: "7"
    - delegation_id: "D-9"
      version: "2"
```

---

# 48. Authorization Invalidation

A historical authorization decision may remain historically true:

```text
ALLOW at T0
```

while no longer being valid for future commit:

```text
REVOKED at T1
```

Therefore:

```text
HISTORICAL_ALLOW
!=
CURRENT_COMMIT_AUTHORITY
```

---

# 49. Authorization Cache Invalidation

Cached authorization decisions MUST NOT survive relevant revocation unless the cache is explicitly bounded by a validity mechanism proving continued applicability.

At minimum:

```text
revocation
→ invalidate dependent authorization cache
```

---

# 50. Policy Decision Interaction

Policy evaluation does not rescue revoked authority.

```text
AUTHORITY = REVOKED
POLICY = ALLOW
```

Result:

```text
BLOCK_AUTHORITY
```

---

# 51. Capability Interaction

Capability availability does not rescue revoked authority.

```text
CAPABILITY = AVAILABLE
AUTHORITY = REVOKED
```

Result:

```text
NO AUTHORIZED EFFECT
```

---

# 52. Agent Revocation

An agent's delegated authority may be revoked independently of the agent process.

```text
AGENT_RUNNING
+
AUTHORITY_REVOKED
```

means:

```text
agent may continue computation
but must not perform revoked governed effects
```

unless the agent itself is separately terminated.

---

# 53. Agent Termination

```text
TERMINATE_AGENT
!=
REVOKE_AUTHORITY
```

An authority object may survive process termination unless explicitly revoked or expired.

Likewise, restarting an agent does not restore revoked authority.

---

# 54. Child Agents

Revocation of a parent's authority MUST propagate to child agents whose authority depends on that parent delegation.

Agent spawning cannot create a revocation-resistant authority branch.

---

# 55. Skill Revocation

A Skill may lose authority to perform certain governed effects without the Skill itself being removed.

```text
SKILL_AVAILABLE
+
AUTHORITY_REVOKED
=
SKILL_NOT_AUTHORIZED_FOR_REVOKED_EFFECT
```

---

# 56. Cross-Skill Revocation

Revocation MUST survive Skill composition.

Example:

```text
Skill A authority:
READ

Skill B authority:
TRANSFORM

Skill C authority:
SEND
```

If external `SEND` authority is revoked, chaining A → B → C MUST NOT recreate disclosure authority.

---

# 57. Workflow Revocation

Queued workflows MUST revalidate authority when relevant authority is revoked.

A workflow created before revocation does not acquire permanent immunity from future authority changes.

---

# 58. Queue Invalidation

Queued effects SHOULD carry authority dependencies.

Example:

```yaml
queued_action:
  action_id: "Q-17"

  authority_dependencies:
    - "D-100"
    - "AW-51"
```

Revoking `D-100` allows targeted invalidation.

---

# 59. Reservation Revocation

A reservation created under valid authority may need cancellation when that authority is revoked before commit.

Possible states:

```text
RESERVED
→ RELEASED

RESERVED
→ BLOCKED

RESERVED
→ REVALIDATION_REQUIRED
```

depending on transaction semantics.

---

# 60. Transaction Boundary

Revocation semantics depend critically on transaction finality.

Distinguish:

```text
PROPOSED

AUTHORIZED

RESERVED

PREPARED

COMMITTED

EXTERNALLY_EFFECTED
```

Revocation effects differ by state.

---

# 61. Pre-Commit Revocation

Canonical rule:

```text
authority revoked before commit
→ block commit
```

for consequential effects requiring current authority.

---

# 62. Post-Commit Revocation

Revocation generally cannot make an already-final historical commit "never have happened."

Instead:

```text
COMMITTED_EFFECT
+
LATER_REVOCATION
=
HISTORICAL_EFFECT_REMAINS
+
NO NEW AUTHORITY
```

Compensating action may be required.

---

# 63. External Irreversibility

If an external effect is irreversible:

```text
money transferred;

message delivered;

data disclosed;

physical action completed;
```

later revocation cannot automatically reverse reality.

The system MUST distinguish:

```text
authority invalidation
```

from:

```text
effect compensation / remediation
```

---

# 64. Compensation

Where an already-committed effect can be compensated:

```text
REVOCATION
→ COMPENSATION PROPOSAL
→ AUTHORIZATION
→ COMPENSATING COMMIT
```

The compensating action requires its own authority.

---

# 65. No Retroactive Fiction

Never represent:

```text
revoked at T1
```

as proving:

```text
action at T0 was unauthorized
```

unless the authority was invalid at T0 or the revocation explicitly has valid retroactive semantics.

---

# 66. Retroactive Revocation

Retroactive revocation is dangerous and SHOULD require explicit governance.

It MUST distinguish:

```text
current authority withdrawal;

historical validity reassessment;

record correction;

fraud/compromise invalidation;

legal retroactivity.
```

These are not equivalent.

---

# 67. Compromise Revocation

Compromise may trigger emergency revocation.

Examples:

```text
credential compromise;

authority-token theft;

principal compromise;

signing-key compromise;

malicious delegation;

provenance corruption.
```

Emergency action SHOULD favor rapid containment while preserving audit evidence.

---

# 68. Trust-Root Compromise

If a root authority or authority-signing mechanism is compromised, descendants may require quarantine even if no individual descendant has yet been proven malicious.

State:

```text
QUARANTINED_PENDING_REVALIDATION
```

may be appropriate.

---

# 69. Key Revocation

If authority depends on cryptographic identity or signatures:

```text
KEY_REVOKED
```

does not necessarily mean every historically signed object was invalid when signed.

Temporal verification matters.

---

# 70. Effective Time

Every revocation MUST have an effective-time interpretation.

```yaml
temporal:
  requested_at: timestamp
  committed_at: timestamp
  effective_at: timestamp
```

These timestamps may differ.

---

# 71. Future Revocation

A revocation MAY be scheduled:

```text
effective_at > now
```

Until the effective time, authority remains governed by the existing state unless policy says otherwise.

---

# 72. Immediate Revocation

For immediate revocation:

```text
effective_at <= committed_at
```

New dependent effects MUST fail once the committed revocation becomes authoritative.

---

# 73. Freshness

Authority resolution MUST use sufficiently fresh revocation state.

```text
REVOCATION_FRESHNESS
```

is a load-bearing authority property.

---

# 74. Freshness Ceiling

A witness cannot remain trusted beyond the freshness of its revocation dependencies.

AMOS MODEL:

```text
Freshness(W)
≤
min(
    Freshness(authority),
    Freshness(delegation),
    Freshness(revocation_state),
    Freshness(policy_dependencies)
)
```

---

# 75. Commit-Time Revalidation

Before consequential commit, validate:

```text
root authority still valid;

parent authority still valid;

delegation still active;

revocation target unchanged;

no relevant revocation has committed;

authority witness still current;

policy still compatible;

constraints still satisfied;

reservation still valid;

transaction state still valid.
```

---

# 76. TOCTOU Protection

Revocation creates a classic time-of-check/time-of-use risk.

```text
T0 CHECK authority
T1 authority valid

T2 REVOCATION commits

T3 USE stale authority
```

T3 MUST fail when current authority is required.

---

# 77. MVCC Boundary

A mutable authority object SHOULD carry a version or generation.

Example:

```text
READ:
authority_version = V7

VALIDATE:
allow

REVOCATION:
authority_version = V8

COMMIT:
requires V7
```

Result:

```text
VERSION_CONFLICT
→ REVALIDATE
```

---

# 78. CAS Boundary

Conceptually:

```text
CAS(
    expected_authority_version = V7,
    current_authority_version = V7
)
```

If false:

```text
COMMIT_DENIED
→ REVALIDATE
```

---

# 79. Revocation Read Set

```yaml
revocation_read_set:
  - object_id: string
    object_type: string
    version: string
    generation: null
    content_hash: string

    role:
      - TARGET
      - ROOT_AUTHORITY
      - PARENT_AUTHORITY
      - PARENT_DELEGATION
      - REVOCATION_POLICY
      - REVOCATION_AUTHORITY
      - CONSTRAINT
      - TRANSACTION
      - RESERVATION
      - PRINCIPAL
```

---

# 80. Atomic Revocation

A revocation may require atomic changes to:

```text
target state;

revocation registry;

authority graph;

delegation graph;

witness validity;

authorization cache;

reservation state;

transaction eligibility;

provenance ledger.
```

Partial application can create phantom authority.

---

# 81. Partial Revocation Commit Failure

Example:

```text
revocation record written
BUT
authority graph unchanged
```

must not be treated as a clean completed state.

Likewise:

```text
authority graph invalidated
BUT
revocation provenance absent
```

requires reconciliation.

---

# 82. Fail-Closed State

When atomicity cannot be established:

```text
AFFECTED_AUTHORITY
→ QUARANTINED / REVALIDATION_REQUIRED
```

until reconciliation completes.

---

# 83. Revocation Digest

Conceptually:

```text
RevocationDigest =
H(
    revoker
    + target
    + target_version
    + mode
    + scope
    + authority_removed
    + effective_time
    + reason
    + dependency_policy
)
```

Material mutation requires a new version/digest.

---

# 84. Immutable History

Committed revocation history SHOULD be append-preserving.

Corrections SHOULD use:

```text
SUPERSEDING_RECORD
```

rather than silently rewriting historical authority state.

---

# 85. Revocation Registry

A revocation registry SHOULD answer:

```text
is target revoked?

is target partially revoked?

is target suspended?

when did state change?

who authorized the change?

what scope was affected?

what version was targeted?

which descendants were affected?

which independent paths survived?

what superseded this record?
```

---

# 86. Registry Lookup

Conceptually:

```text
RevocationState(target,t)
→
ACTIVE
| PARTIALLY_REVOKED
| SUSPENDED
| REVOKED
| SUPERSEDED
| EXPIRED
| CONFLICT
| UNKNOWN_GAP
```

---

# 87. Unknown State

If authoritative revocation state cannot be resolved:

```text
UNKNOWN_GAP
```

must not be silently mapped to:

```text
ACTIVE
```

for consequential actions.

---

# 88. Conflict State

Example:

```text
Registry A:
ACTIVE

Registry B:
REVOKED
```

Without authoritative precedence:

```text
BLOCK_CONFLICT
```

or:

```text
UNKNOWN_GAP
```

not optimistic selection.

---

# 89. Split-Brain Revocation

Distributed replicas may disagree temporarily.

```text
Replica A = ACTIVE
Replica B = REVOKED
```

The control plane MUST apply its finality/consistency rules before consequential commit.

---

# 90. Stale Replica

A stale replica cannot overrule a fresher authoritative revocation merely because it returns `ACTIVE`.

Freshness and authority of the state source matter.

---

# 91. Revocation Precedence

Where multiple revocation records exist, precedence MUST be governed by:

```text
authority;

scope;

effective time;

version;

supersession;

regime;

and provenance.
```

Do not use arbitrary "latest text wins" semantics.

---

# 92. Revocation Composition

Multiple partial revocations MAY compose.

Example:

```text
R1 removes DELETE

R2 removes SEND_EXTERNAL
```

Effective authority removes both if both remain applicable.

---

# 93. Revocation Cancellation

Cancellation of a pending future revocation is not equivalent to restoring already revoked authority.

Only non-effective or explicitly reversible transitions may be cancelled according to policy.

---

# 94. Revocation of Revocation

A system SHOULD avoid semantic ambiguity such as:

```text
revoke the revocation
```

Prefer explicit operations:

```text
CANCEL_PENDING_REVOCATION

RESTORE_SUSPENDED_AUTHORITY

ISSUE_NEW_AUTHORITY

SUPERSEDE_REVOCATION_RECORD
```

---

# 95. H/M/L Applicability

## H — Governing Layer

H-level revocation concerns:

```text
root authority;

institutional authority;

trust roots;

authority issuers;

global revocation rules;

jurisdiction;

emergency governance;

revocation precedence;

system-wide authority constraints.
```

## M — Operational Layer

M-level revocation concerns:

```text
delegations;

roles;

services;

projects;

resource classes;

workflows;

agents;

Skills;

budgets;

operational capabilities.
```

## L — Effect Layer

L-level revocation concerns:

```text
exact operation;

exact resource;

exact recipient;

exact transaction;

exact reservation;

exact authority witness;

exact queued action;

exact commit attempt.
```

---

# 96. Cross-Scale Rule

An H-level revocation may invalidate many M/L descendants.

An L-level revocation MUST NOT automatically invalidate an H-level authority root unless a valid dependency relationship exists.

---

# 97. Revocation Workflow

```text
01 RECEIVE REVOCATION REQUEST

02 RESOLVE REVOCATION PRINCIPAL

03 VALIDATE PRINCIPAL IDENTITY

04 RESOLVE REVOCATION AUTHORITY

05 RESOLVE TARGET

06 LOAD CURRENT TARGET VERSION

07 LOAD TARGET AUTHORITY ANCESTRY

08 VALIDATE REVOCATION SCOPE

09 VALIDATE MODE

10 DETERMINE EFFECTIVE TIME

11 BUILD DIRECT DEPENDENCY SET

12 BUILD REQUIRED DEPENDENCY CLOSURE

13 IDENTIFY INDEPENDENT AUTHORITY PATHS

14 IDENTIFY ACTIVE WITNESSES

15 IDENTIFY CACHED AUTHORIZATIONS

16 IDENTIFY RESERVATIONS

17 IDENTIFY IN-FLIGHT TRANSACTIONS

18 CHECK CONFLICTS

19 CHECK FRESHNESS

20 PRODUCE REVOCATION DECISION

21 RESERVE / LOCK REQUIRED STATE

22 COMMIT REVOCATION

23 UPDATE AUTHORITY GRAPH

24 INVALIDATE DEPENDENT DELEGATIONS

25 INVALIDATE DEPENDENT WITNESSES

26 INVALIDATE DEPENDENT AUTHORIZATIONS

27 REVIEW RESERVATIONS

28 MARK IN-FLIGHT TRANSACTIONS FOR REVALIDATION

29 PRESERVE INDEPENDENT AUTHORITY PATHS

30 WRITE PROVENANCE

31 WRITE AUDIT RECORD

32 RELEASE LOCK / FINALIZE EPOCH
```

---

# 98. Emergency Revocation Workflow

```text
COMPROMISE SIGNAL
      ↓
VERIFY MINIMUM EMERGENCY THRESHOLD
      ↓
IDENTIFY HIGH-RISK AUTHORITY
      ↓
TEMPORARY QUARANTINE
      ↓
BLOCK NEW CONSEQUENTIAL COMMIT
      ↓
RESOLVE REVOCATION AUTHORITY
      ↓
COMMIT EMERGENCY REVOCATION
      ↓
PROPAGATE DEPENDENCY INVALIDATION
      ↓
INVESTIGATE
      ↓
RESTORE / REISSUE / PERMANENTLY REVOKE
```

Quarantine MUST NOT be misrepresented as proof of compromise.

---

# 99. Partial Revocation Workflow

```text
LOAD CURRENT AUTHORITY
      ↓
NORMALIZE REMOVAL SUBSET
      ↓
VERIFY SUBSET
      ↓
SUBTRACT REVOKED AUTHORITY
      ↓
RECOMPUTE CONSTRAINTS
      ↓
RECOMPUTE DESCENDANTS
      ↓
INVALIDATE ONLY AFFECTED DEPENDENCIES
      ↓
VERSION NEW EFFECTIVE STATE
```

---

# 100. Suspension Workflow

```text
ACTIVE
  ↓
VALID SUSPENSION AUTHORITY
  ↓
SUSPENDED
  ↓
BLOCK NEW AUTHORIZED EFFECTS
  ↓
INVALIDATE / PAUSE DEPENDENT WITNESSES
  ↓
RESTORATION DECISION
  ├──→ ACTIVE
  └──→ REVOKED
```

---

# 101. Transaction Revocation Workflow

```text
REVOCATION COMMITTED
      ↓
FIND IN-FLIGHT TRANSACTIONS
      ↓
CLASSIFY EACH:
PROPOSED / AUTHORIZED / RESERVED / PREPARED / COMMITTED
      ↓
IF PRE-COMMIT:
REVALIDATE OR BLOCK
      ↓
IF COMMITTED:
PRESERVE HISTORY
      ↓
IF REMEDIATION REQUIRED:
PROPOSE COMPENSATING ACTION
```

---

# 102. Revocation Protocol

```yaml
revoke:
  revoker:
    principal_id: string
    authority_witness_ref: string

  target:
    type: string
    id: string
    version: null

  mode: FULL

  scope: {}

  authority_subset: {}

  effective_at: timestamp

  reason: {}

  dependency_policy: {}

  transaction_policy: {}

  provenance: {}
```

---

# 103. Revocation Response Protocol

```yaml
revoke_result:
  state:
    - REVOKED
    - PARTIALLY_REVOKED
    - SUSPENDED
    - SUPERSEDED
    - DENIED
    - BLOCK_AUTHORITY
    - BLOCK_SCOPE
    - BLOCK_CONFLICT
    - REVALIDATE
    - UNKNOWN_GAP

  revocation_id: null

  affected:
    delegations: []
    witnesses: []
    authorizations: []
    reservations: []
    transactions: []
    workflows: []
    agents: []
    skills: []

  preserved_independent_paths: []

  failed_invariants: []
  gaps: []

  provenance: {}
```

---

# 104. Control-Plane Requirements

The revocation subsystem SHOULD integrate with:

```text
AUTHORITY_RESOLVER.md

AUTHORITY_WITNESS.md

AUTHORIZATION_SPEC.md

DELEGATION.md

POLICY_ENGINE.md

POLICY_REGISTRY.md

CAPABILITY_CONTRACT.md

CAPABILITY_MANIFEST.md

CONTROL_PLANE_MAP.md

PRINCIPAL / IDENTITY REGISTRY

AUTHORITY REGISTRY

REVOCATION REGISTRY

TRANSACTION CONTROL

COMMIT GUARD

PROVENANCE STORE

AUDIT LOG

OBSERVABILITY ENVELOPE

MVCC / CAS STATE
```

---

# 105. Control-Plane Ownership

Revocation is infrastructure authority logic.

Domain agents and Skills MAY:

```text
request revocation;

surface compromise evidence;

consume revocation state;

stop domain operations after revocation.
```

They MUST NOT silently create authoritative revocation state unless explicitly designated and authorized by the control plane.

---

# 106. Agent Responsibilities

Potential agents:

```text
REVOCATION_REQUEST_AGENT

AUTHORITY_RESOLUTION_AGENT

DEPENDENCY_ANALYSIS_AGENT

CONFLICT_ANALYSIS_AGENT

TRANSACTION_REVALIDATION_AGENT

AUDIT_AGENT
```

These names describe roles, not automatically implemented agents.

---

# 107. Skill Responsibilities

Potential Skills:

```text
revocation-request-normalization

revocation-authority-resolution

authority-dependency-analysis

revocation-propagation

authority-witness-invalidation

transaction-revalidation

revocation-audit

revocation-recovery
```

Skill existence does not confer revocation authority.

---

# 108. Revocation Invariants

## INV-REV-001 — Explicit Revocation Authority

Every committed revocation MUST have a valid authority basis.

## INV-REV-002 — Target Identity

The target MUST be unambiguously resolved.

## INV-REV-003 — Target Version

Materially mutable targets MUST be version-bound.

## INV-REV-004 — Scope Bound

Revocation cannot exceed the revoker's authorized scope.

## INV-REV-005 — Provenance Preservation

Revocation provenance MUST remain recoverable.

## INV-REV-006 — Historical Preservation

Revocation MUST NOT silently erase historical authority evidence.

## INV-REV-007 — Dependent Invalidation

Solely dependent descendants cannot remain valid after their load-bearing parent is revoked.

## INV-REV-008 — Independent Path Preservation

Independent valid authority MUST not be invalidated merely because another path is revoked.

## INV-REV-009 — Witness Freshness

Witnesses depending on revoked state MUST become invalid or stale.

## INV-REV-010 — Authorization Freshness

Historical authorization cannot substitute for current authority at commit.

---

# 109. Revocation Invariants — Continued

## INV-REV-011 — Capability Separation

```text
CAN_REVOKE
!=
MAY_REVOKE
```

## INV-REV-012 — Policy Separation

```text
POLICY_ALLOW_REVOKE
!=
REVOCATION_AUTHORITY
```

## INV-REV-013 — Agent Separation

```text
AGENT_TERMINATION
!=
AUTHORITY_REVOCATION
```

## INV-REV-014 — Skill Separation

Skill availability does not establish revocation authority.

## INV-REV-015 — Partial Precision

Partial revocation MUST preserve unaffected authority where independently valid.

## INV-REV-016 — Suspension Precision

Suspension MUST NOT silently become permanent revocation.

## INV-REV-017 — Supersession Precision

Supersession MUST preserve explicit lineage.

## INV-REV-018 — Expiration Precision

Expiration and revocation MUST remain provenance-distinct.

## INV-REV-019 — Conflict Fail-Closed

Conflicting authoritative revocation states MUST NOT be resolved optimistically.

## INV-REV-020 — Unknown Fail-Closed

Unknown revocation state MUST NOT be interpreted as active for consequential effects.

---

# 110. Revocation Invariants — Transactional

## INV-REV-021 — Pre-Commit Freshness

Consequential commits MUST validate current authority where revocation can occur between authorization and commit.

## INV-REV-022 — Version Conflict

A changed load-bearing authority version requires revalidation.

## INV-REV-023 — Atomic State

Partial revocation persistence MUST NOT create phantom authority.

## INV-REV-024 — Reservation Review

Reservations depending on revoked authority MUST be reviewed before use.

## INV-REV-025 — Queue Review

Queued actions depending on revoked authority MUST revalidate.

## INV-REV-026 — No Retroactive Fiction

Later revocation alone does not falsify historically valid authority.

## INV-REV-027 — External Reality Preservation

Revocation cannot erase already-realized external effects.

## INV-REV-028 — Compensation Authorization

Compensation requires its own valid authority.

## INV-REV-029 — Selective Cache Invalidation

Only caches dependent on changed authority SHOULD be invalidated when dependency precision permits.

## INV-REV-030 — Current State Dominance

Current authoritative revocation state outranks stale cached allow state.

---

# 111. Revocation Invariants — Provenance / Topology

## INV-REV-031

Shared descendants do not constitute independent roots.

## INV-REV-032

Revocation of a shared root invalidates all solely dependent descendant paths.

## INV-REV-033

Multiple independent roots MUST remain separately traceable.

## INV-REV-034

Revocation records MUST preserve source identity.

## INV-REV-035

Revocation supersession MUST preserve previous record lineage.

## INV-REV-036

Revocation evidence MUST NOT be counted as independent when derived from the same origin.

## INV-REV-037

A stale replica cannot overrule a finalized revocation.

## INV-REV-038

Split-brain state requires governed resolution.

## INV-REV-039

Unresolved provenance conflict lowers confidence and may block commit.

## INV-REV-040

No revocation claim may exceed the confidence of its load-bearing authority evidence.

---

# 112. Failure Modes

```text
FM-REV-001 revoker unresolved

FM-REV-002 revocation authority missing

FM-REV-003 revocation authority expired

FM-REV-004 revocation authority revoked

FM-REV-005 target missing

FM-REV-006 target ambiguous

FM-REV-007 target version stale

FM-REV-008 target digest mismatch

FM-REV-009 revocation scope exceeds authority

FM-REV-010 invalid revocation mode

FM-REV-011 invalid effective time

FM-REV-012 provenance missing

FM-REV-013 dependency closure incomplete

FM-REV-014 independent path misclassified

FM-REV-015 correlated path misclassified as independent

FM-REV-016 descendant remains active after sole parent revoked

FM-REV-017 independent authority wrongly invalidated

FM-REV-018 witness not invalidated

FM-REV-019 authorization cache not invalidated

FM-REV-020 queued action uses stale authority

FM-REV-021 reservation uses revoked authority

FM-REV-022 pre-commit transaction uses revoked authority

FM-REV-023 partial revocation treated as total

FM-REV-024 total revocation treated as partial

FM-REV-025 suspension treated as revocation

FM-REV-026 revocation treated as suspension

FM-REV-027 expiration treated as explicit revocation

FM-REV-028 supersession loses lineage

FM-REV-029 historical record deleted

FM-REV-030 stale replica reports ACTIVE

FM-REV-031 split-brain state ignored

FM-REV-032 partial commit

FM-REV-033 graph/registry divergence

FM-REV-034 agent restart restores revoked authority

FM-REV-035 child agent bypasses revocation

FM-REV-036 Skill composition recreates revoked effect

FM-REV-037 policy allow overrides revoked authority

FM-REV-038 capability availability overrides revoked authority

FM-REV-039 historical allow reused after revocation

FM-REV-040 UNKNOWN/GAP treated as ACTIVE
```

---

# 113. Adversarial Failure Modes

```text
replay a stale authority witness after revocation;

route through another Skill to recreate revoked effect;

spawn a child agent before revocation and claim independent authority;

duplicate a delegation before revocation;

rename a revoked operation;

move a resource into another identifier;

use an alias of a revoked recipient;

replay an authorization decision from before revocation;

delay revocation propagation until after commit;

write revocation to one replica while reading ACTIVE from another;

forge a newer-looking ACTIVE record;

remove ancestry linking a child to revoked parent;

claim multiple descendants as independent authority;

split one revoked effect into several individually allowed steps;

restore authority by restarting a session;

restore authority from memory;

restore authority by role change;

cancel an already-final revocation without new authority;

rewrite effective_at;

rewrite target version;

hide revocation provenance.
```

---

# 114. Repair / Recovery

```text
DETECT REVOCATION FAILURE
      ↓
FREEZE AFFECTED AUTHORITY
      ↓
BLOCK CONSEQUENTIAL COMMIT
      ↓
IDENTIFY AUTHORITATIVE TARGET STATE
      ↓
RECONSTRUCT DEPENDENCY CLOSURE
      ↓
IDENTIFY INDEPENDENT AUTHORITY PATHS
      ↓
RECONCILE REGISTRY / GRAPH / CACHE
      ↓
INVALIDATE DEPENDENT WITNESSES
      ↓
REVALIDATE TRANSACTIONS
      ↓
PRESERVE VALID INDEPENDENT STATE
      ↓
WRITE REPAIR PROVENANCE
      ↓
RESUME ONLY AFTER VALIDATION
```

---

# 115. Broken Propagation Recovery

If a revoked parent has active descendants:

```text
DESCENDANTS
→ REVALIDATION_REQUIRED
```

Then:

```text
recompute authority ancestry;

invalidate solely dependent descendants;

preserve independently authorized descendants;

invalidate affected witnesses;

revalidate queued transactions.
```

---

# 116. Registry / Graph Divergence Recovery

If:

```text
REVOCATION_REGISTRY = REVOKED

AUTHORITY_GRAPH = ACTIVE
```

then the system MUST NOT select the permissive interpretation.

Preferred state:

```text
BLOCK_CONFLICT
```

until authoritative reconciliation.

---

# 117. Stale Cache Recovery

```text
detect stale dependency;

invalidate affected cache entry;

load current authority state;

re-run authority resolution;

re-run authorization;

update cache only from validated result.
```

---

# 118. Transaction Recovery

If a transaction was prepared using authority later revoked before commit:

```text
PREPARED
→ BLOCKED / REVALIDATION_REQUIRED
```

Release or quarantine associated reservations according to transaction policy.

---

# 119. Compromise Recovery

```text
QUARANTINE

REVOKE HIGH-RISK AUTHORITY

ROTATE COMPROMISED CREDENTIALS WHERE APPLICABLE

REBUILD AUTHORITY GRAPH

REISSUE VALID AUTHORITY

INVALIDATE STALE WITNESSES

REVALIDATE DEPENDENTS

AUDIT ACTIONS DURING COMPROMISE WINDOW
```

Do not automatically classify all actions during the window as malicious.

---

# 120. Validators

Minimum validator surface:

```text
validate_revocation_request

validate_revoker_identity

validate_revocation_authority

validate_target_identity

validate_target_version

validate_target_digest

validate_revocation_mode

validate_revocation_scope

validate_effective_time

validate_dependency_closure

validate_independent_paths

validate_provenance_independence

validate_revocation_registry

validate_authority_graph_consistency

validate_witness_invalidation

validate_authorization_invalidation

validate_queue_invalidation

validate_reservation_state

validate_transaction_state

validate_mvcc_version

validate_cas_precondition

validate_revocation_digest

validate_commit_freshness

validate_recovery_state
```

---

# 121. Minimum Test Suite

```text
T-REV-001 valid full revocation

T-REV-002 valid partial revocation

T-REV-003 valid suspension

T-REV-004 valid supersession

T-REV-005 unresolved revoker

T-REV-006 unauthorized revoker

T-REV-007 expired revocation authority

T-REV-008 revoked revocation authority

T-REV-009 missing target

T-REV-010 ambiguous target

T-REV-011 stale target version

T-REV-012 target digest mismatch

T-REV-013 scope-bounded revocation

T-REV-014 overbroad revocation rejected

T-REV-015 immediate effective time

T-REV-016 future effective time

T-REV-017 parent revocation cascade

T-REV-018 root revocation cascade

T-REV-019 partial parent revocation

T-REV-020 independent authority preservation

T-REV-021 correlated ancestry detection

T-REV-022 witness invalidation

T-REV-023 authorization cache invalidation

T-REV-024 queued action invalidation

T-REV-025 reservation invalidation

T-REV-026 pre-commit transaction block

T-REV-027 post-commit historical preservation

T-REV-028 compensation requires authority

T-REV-029 no retroactive fiction

T-REV-030 agent authority revocation

T-REV-031 agent termination separation

T-REV-032 child-agent revocation propagation

T-REV-033 Skill authority revocation

T-REV-034 cross-Skill bypass rejection

T-REV-035 policy-allow bypass rejection

T-REV-036 capability bypass rejection

T-REV-037 role bypass rejection

T-REV-038 stale witness replay rejection

T-REV-039 stale authorization replay rejection

T-REV-040 stale replica rejection

T-REV-041 split-brain conflict

T-REV-042 registry/graph divergence

T-REV-043 MVCC conflict

T-REV-044 CAS failure

T-REV-045 atomic revocation

T-REV-046 partial commit quarantine

T-REV-047 provenance preservation

T-REV-048 supersession lineage

T-REV-049 historical record preservation

T-REV-050 multiple partial revocations

T-REV-051 purpose-specific revocation

T-REV-052 recipient-specific revocation

T-REV-053 effect-specific revocation

T-REV-054 resource-specific revocation

T-REV-055 operation-specific revocation

T-REV-056 suspension restoration

T-REV-057 revoked authority cannot restore directly

T-REV-058 compromise quarantine

T-REV-059 trust-root compromise

T-REV-060 emergency revocation

T-REV-061 scheduled revocation

T-REV-062 revocation epoch invalidation

T-REV-063 selective invalidation

T-REV-064 dependency closure

T-REV-065 proof-based local finalization

T-REV-066 cross-shard escalation when closure unknown

T-REV-067 cached ACTIVE after revocation

T-REV-068 transaction TOCTOU

T-REV-069 unknown revocation state

T-REV-070 UNKNOWN/GAP fail-closed
```

---

# 122. Adversarial Tests

```text
T-REV-A01 stale witness replay

T-REV-A02 stale policy allow replay

T-REV-A03 alias-based target bypass

T-REV-A04 operation rename bypass

T-REV-A05 resource rename bypass

T-REV-A06 recipient alias bypass

T-REV-A07 child-agent laundering

T-REV-A08 cross-Skill effect laundering

T-REV-A09 delegation duplication before revocation

T-REV-A10 correlated descendants claimed independent

T-REV-A11 stale replica ACTIVE response

T-REV-A12 forged authority version

T-REV-A13 delayed revocation propagation

T-REV-A14 partial commit exploitation

T-REV-A15 memory-based authority restoration

T-REV-A16 session restart restoration

T-REV-A17 role-change restoration

T-REV-A18 unauthorized revocation cancellation

T-REV-A19 effective-time mutation

T-REV-A20 provenance-edge removal
```

---

# 123. Falsifiers

A claim that authority remains valid is falsified by reliable evidence that:

```text
the authority itself was validly revoked;

its sole load-bearing parent was revoked;

its root authority was revoked;

its required delegation was revoked;

its authority witness depends on revoked state;

its validity period expired;

its scope was partially revoked for the requested target;

its operation was revoked;

its effect was revoked;

its recipient was revoked;

its purpose authority was revoked;

or its required authority path is no longer valid.
```

A claim that a revocation is valid is falsified by reliable evidence that:

```text
the revoker lacked revocation authority;

the target was incorrectly resolved;

the targeted version was not applicable;

the revocation exceeded authorized scope;

the revocation never committed;

the revocation effective time has not arrived;

the revocation record is forged or invalid;

or a higher-authority valid supersession cancels a still-pending revocation under an applicable rule.
```

---

# 124. Confidence Ceiling

AMOS MODEL:

```text
C_revocation
≤
min(
    C_revoker_identity,
    C_revocation_authority,
    C_target_identity,
    C_target_version,
    C_scope,
    C_effective_time,
    C_dependency_closure,
    C_provenance,
    C_finality,
    C_freshness
)
```

For descendant invalidation:

```text
C_descendant_invalidation
≤
min(
    C_revocation,
    C_dependency_edge,
    C_no_independent_path
)
```

---

# 125. Uncertainty Vector

```yaml
revocation_uncertainty:
  revoker_identity: null
  revocation_authority: null
  target_identity: null
  target_version: null
  target_digest: null
  scope: null
  effective_time: null
  dependency_closure: null
  independent_paths: null
  provenance: null
  freshness: null
  finality: null
  transaction_state: null
  external_effect_state: null
  recovery_state: null
```

---

# 126. RSCF Capsule

```yaml
rscf:
  claim:
    id: "AMOS_REVOCATION_ARCHITECTURE"
    class: MODEL

    text: >
      AMOS revocation withdraws or restricts authority through an
      explicit, provenance-bound control-plane transition and invalidates
      only authority states that materially depend upon the revoked
      authority, while preserving independently valid authority paths,
      historical provenance, and transaction-finality distinctions.

  premises:
    - revoker_identity_valid
    - revocation_authority_valid
    - target_resolved
    - target_version_current
    - scope_authorized
    - effective_time_valid
    - dependency_closure_known
    - independent_paths_resolved
    - provenance_valid
    - finality_known

  provenance:
    origin_architect: "Trang Phan"
    steward: "Trang Phan"

  scope:
    system: "AMOS OS"
    component: "Authority Revocation"

  regime:
    - DESIGN
    - ARCHITECTURE
    - GOVERNANCE_MODEL

  dependencies:
    - AUTHORITY_RESOLVER.md
    - AUTHORITY_WITNESS.md
    - AUTHORIZATION_SPEC.md
    - DELEGATION.md
    - POLICY_ENGINE.md
    - POLICY_REGISTRY.md
    - CAPABILITY_CONTRACT.md
    - CAPABILITY_MANIFEST.md
    - CONTROL_PLANE_MAP.md

  competing:
    - deletion-based revocation
    - cache-only invalidation
    - role-only revocation
    - policy-deny-as-revocation
    - global invalidation without dependency analysis

  falsifiers:
    - unauthorized principal can revoke authority
    - revoked parent leaves solely dependent child valid
    - independent authority is destroyed without dependency
    - stale witness remains usable after revocation
    - pre-commit transaction commits against revoked authority
    - revocation destroys historical provenance

  confidence_ceiling: 0
```

---

# 127. GMEF Change Governance

Changes to revocation semantics SHOULD be treated as governance-sensitive when they affect:

```text
who may revoke;

what may be revoked;

revocation precedence;

effective-time semantics;

dependency propagation;

independent-path preservation;

transaction finality;

revocation freshness;

emergency revocation;

trust-root compromise;

or restoration semantics.
```

Such changes SHOULD require:

```text
change classification;

affected-invariant analysis;

migration plan;

backward-compatibility analysis;

test evidence;

rollback plan;

authority approval;

and provenance.
```

---

# 128. Revocation Change Manifest

```yaml
revocation_change:
  change_id: string

  from_version: string
  to_version: string

  class:
    - COSMETIC
    - SCHEMA
    - SEMANTIC
    - AUTHORITY
    - SECURITY
    - GOVERNANCE

  affected_invariants: []
  affected_authority_paths: []
  affected_delegations: []
  affected_transactions: []

  migration_requirements: []
  validation_requirements: []

  rollback_plan: null

  approval_state: PROPOSED
```

---

# 129. Promotion Model

```text
STRUCTURAL_MODEL
      ↓
SCHEMA_VALIDATED
      ↓
REVOCATION_REGISTRY_IMPLEMENTED
      ↓
AUTHORITY_GRAPH_INTEGRATED
      ↓
DEPENDENCY_INVALIDATION_IMPLEMENTED
      ↓
WITNESS_INVALIDATION_IMPLEMENTED
      ↓
TRANSACTION_REVALIDATION_IMPLEMENTED
      ↓
MVCC/CAS_IMPLEMENTED
      ↓
PROVENANCE_IMPLEMENTED
      ↓
UNIT_TESTED
      ↓
INTEGRATION_TESTED
      ↓
ADVERSARIALLY_TESTED
      ↓
SECURITY_REVIEWED
      ↓
GOVERNED_ACTIVE
```

No transition is automatic.

---

# 130. Implementation Requirements

An executable revocation implementation SHOULD provide:

```text
typed revocation requests;

typed revocation decisions;

typed revocation records;

revoker identity resolution;

revocation-authority resolution;

target resolution;

version binding;

digest binding;

full revocation;

partial revocation;

suspension;

supersession;

effective-time handling;

authority dependency graph traversal;

independent-path detection;

selective invalidation;

authority-witness invalidation;

authorization-cache invalidation;

queue invalidation;

reservation review;

transaction revalidation;

MVCC/CAS or equivalent freshness control;

atomic state transition;

provenance logging;

audit reconstruction;

recovery / reconciliation.
```

This specification does not claim these mechanisms are currently implemented.

---

# 131. Example — Direct Delegation Revocation

Authority graph:

```text
ROOT
 ↓
D1
 ↓
Agent-A
```

Request:

```yaml
target:
  type: DELEGATION
  id: D1

mode: FULL
```

After valid commit:

```text
D1 = REVOKED

Agent-A authority from D1 = INVALID
```

---

# 132. Example — Descendant Cascade

```text
ROOT
 ↓
D1
 ↓
A
 ↓
D2
 ↓
B
 ↓
D3
 ↓
C
```

Revoke:

```text
D1
```

Result:

```text
D1 = REVOKED

D2 = INVALID_DEPENDENT

D3 = INVALID_DEPENDENT
```

provided no independent authority paths exist.

---

# 133. Example — Independent Path Preservation

```text
ROOT_A → D1 → P

ROOT_B → D2 → P
```

Revoke:

```text
D1
```

Result:

```text
Path D1 = INVALID

Path D2 = RE-EVALUATE / PRESERVE IF VALID
```

Never automatically:

```text
P has zero authority
```

without resolving D2.

---

# 134. Example — Partial Operation Revocation

Before:

```text
READ
UPDATE
DELETE
```

Revoke:

```text
DELETE
```

After:

```text
READ
UPDATE
```

The new effective authority state SHOULD receive a new version or equivalent state identity.

---

# 135. Example — Resource Revocation

Before:

```text
READ:
PROJECT_A/*
```

Revoke:

```text
PROJECT_A/SECRET/*
```

Request:

```text
READ PROJECT_A/PUBLIC/report.txt
```

may remain authorized.

Request:

```text
READ PROJECT_A/SECRET/key.txt
```

must fail authority resolution.

---

# 136. Example — Effect Revocation

Before:

```text
DRAFT_EMAIL
SEND_EMAIL
```

Revoke:

```text
SEND_EMAIL
```

Agent may still draft if separately valid.

It cannot send.

---

# 137. Example — Stale Witness

```text
T0 authority active

T1 witness AW-10 generated

T2 authority revoked

T3 AW-10 presented

T4 action requested
```

Result:

```text
AW-10 = STALE / INVALID

ACTION = BLOCK_AUTHORITY
```

---

# 138. Example — Stale Authorization

```text
T0:
AUTHORIZATION = ALLOW

T1:
AUTHORITY = REVOKED

T2:
COMMIT attempted
```

Result:

```text
COMMIT = BLOCK
```

if current authority is required.

---

# 139. Example — Already Committed Effect

```text
T0 authority valid

T1 transaction committed

T2 external payment finalized

T3 authority revoked
```

Correct interpretation:

```text
future authority = revoked

historical transaction = remains historical fact
```

Revocation does not magically reverse T2.

---

# 140. Example — Compensation

If the payment can be reversed:

```text
REVOCATION
      ↓
DETECT PRIOR EFFECT
      ↓
PROPOSE REVERSAL
      ↓
AUTHORIZE REVERSAL
      ↓
COMMIT REVERSAL
```

The reversal is a new governed action.

---

# 141. Example — Agent Restart

```text
Agent-A authority revoked

Agent-A process restarted
```

Result:

```text
authority remains revoked
```

Never:

```text
new process
=
new authority
```

---

# 142. Example — Skill Bypass

Authority revoked:

```text
SEND_EXTERNAL
```

Attempt:

```text
Skill A:
WRITE FILE

Skill B:
UPLOAD FILE

Skill C:
SHARE LINK EXTERNALLY
```

If the composition produces the revoked external disclosure effect:

```text
BLOCK
```

The system evaluates the semantic effect, not merely individual operation labels.

---

# 143. Example — Revocation Conflict

Evidence A:

```text
D1 ACTIVE
```

Evidence B:

```text
D1 REVOKED
```

If neither source can be established as authoritative/fresher:

```text
BLOCK_CONFLICT
```

not:

```text
choose ACTIVE because it permits progress
```

---

# 144. Example — Scheduled Revocation

```yaml
revocation:
  target: D1
  effective_at: "2026-09-01T00:00:00Z"
```

Before effective time:

```text
D1 governed by current authority state
```

After effective time:

```text
D1 = REVOKED
```

subject to finality of the scheduled revocation record.

---

# 145. Example — Emergency Compromise

Signal:

```text
possible signing-key compromise
```

Correct response MAY be:

```text
QUARANTINE affected authority

BLOCK high-risk commits

VERIFY compromise

REVOKE / ROTATE as authorized

REVALIDATE descendants
```

Incorrect inference:

```text
signal
=
proof every descendant was malicious
```

---

# 146. Revocation Decision Matrix

| Revoker Authority | Target        | Scope     | Conflict | Result          |
| ----------------- | ------------- | --------- | -------- | --------------- |
| Valid             | Valid         | Valid     | No       | ALLOW           |
| Valid             | Valid         | Partial   | No       | ALLOW_PARTIAL   |
| Invalid           | Valid         | Valid     | No       | BLOCK_AUTHORITY |
| Unknown           | Valid         | Valid     | No       | UNKNOWN_GAP     |
| Valid             | Missing       | Valid     | No       | UNKNOWN_GAP     |
| Valid             | Valid         | Too Broad | No       | BLOCK_SCOPE     |
| Valid             | Valid         | Valid     | Yes      | BLOCK_CONFLICT  |
| Valid             | Stale Version | Valid     | No       | REVALIDATE      |

---

# 147. Dependent Authority Matrix

| Parent    | Child Dependency | Independent Path | Result          |
| --------- | ---------------- | ---------------- | --------------- |
| Active    | Yes              | No               | ACTIVE          |
| Revoked   | Yes              | No               | INVALID         |
| Expired   | Yes              | No               | INVALID         |
| Suspended | Yes              | No               | SUSPENDED/BLOCK |
| Revoked   | Yes              | Yes              | RE-RESOLVE      |
| Revoked   | No               | N/A              | PRESERVE        |
| Conflict  | Yes              | Unknown          | BLOCK_CONFLICT  |
| Unknown   | Yes              | Unknown          | UNKNOWN_GAP     |

---

# 148. Transaction Matrix

| Transaction State   | Revocation Timing    | Default Treatment                   |
| ------------------- | -------------------- | ----------------------------------- |
| PROPOSED            | Before authorization | Resolve current authority           |
| AUTHORIZED          | Before reservation   | Revalidate                          |
| RESERVED            | Before commit        | Revalidate / release                |
| PREPARED            | Before commit        | Block or revalidate                 |
| COMMITTED           | After commit         | Preserve historical commit          |
| EXTERNALLY_EFFECTED | After effect         | Compensation if authorized/possible |

---

# 149. Audit Questions

A revocation audit SHOULD answer:

1. What authority was revoked?
2. What exact object/version was targeted?
3. Who requested revocation?
4. Who possessed authority to revoke?
5. What evidence established that authority?
6. Was the revocation full or partial?
7. What operations were removed?
8. What resources were removed?
9. What effects were removed?
10. What recipients were removed?
11. What purposes were removed?
12. When was revocation requested?
13. When was it committed?
14. When did it become effective?
15. What authority descendants depended on the target?
16. Which descendants were invalidated?
17. Which independent paths survived?
18. Which witnesses became stale?
19. Which authorizations became stale?
20. Which cached decisions were invalidated?
21. Which reservations were affected?
22. Which transactions were in flight?
23. Did any transaction commit after revocation?
24. Were external effects already completed?
25. Was compensation required?
26. Did registry and graph agree?
27. Was the revocation atomically committed?
28. Was provenance preserved?
29. Were conflicts present?
30. What remains UNKNOWN/GAP?

---

# 150. Observability Requirements

Revocation observability SHOULD expose at least:

```text
revocation_id;

target_id;

target_type;

target_version;

revoker_id;

revocation_authority_ref;

mode;

scope;

requested_at;

committed_at;

effective_at;

affected descendant count;

invalidated witness count;

invalidated authorization count;

affected reservation count;

affected transaction count;

conflict state;

revalidation state;

provenance reference.
```

Sensitive authority data MUST remain subject to disclosure controls.

---

# 151. Metrics

Possible operational metrics:

```text
revocation propagation latency;

stale-witness detection rate;

stale-authorization rejection rate;

dependency-invalidation precision;

independent-path preservation rate;

revocation conflict rate;

partial-commit recovery rate;

revocation reconciliation latency;

pre-commit stale-authority rejection rate.
```

Metrics do not themselves prove security or correctness.

---

# 152. Security Properties

The architecture seeks to preserve:

```text
NO AUTHORITY RESURRECTION

NO STALE-WITNESS COMMIT

NO CHILD AUTHORITY AFTER SOLE PARENT REVOCATION

NO POLICY OVERRIDE OF REVOKED AUTHORITY

NO CAPABILITY OVERRIDE OF REVOKED AUTHORITY

NO ROLE OVERRIDE OF REVOKED AUTHORITY

NO AGENT-RESTART AUTHORITY RESET

NO SKILL-COMPOSITION REVOCATION BYPASS

NO SILENT HISTORICAL ERASURE

NO UNAUTHORIZED REVOCATION

NO OVERBROAD REVOCATION

NO UNJUSTIFIED GLOBAL INVALIDATION
```

These remain architectural objectives until validated by implementation evidence.

---

# 153. Completion Matrix

| Surface                      | Specification State |
| ---------------------------- | ------------------- |
| Definition                   | COMPLETE_AS_MODEL   |
| Scope                        | COMPLETE_AS_MODEL   |
| Revocation targets           | COMPLETE_AS_MODEL   |
| Revocation modes             | COMPLETE_AS_MODEL   |
| Revocation authority         | COMPLETE_AS_MODEL   |
| Request schema               | COMPLETE_AS_MODEL   |
| Decision schema              | COMPLETE_AS_MODEL   |
| Record schema                | COMPLETE_AS_MODEL   |
| State machine                | COMPLETE_AS_MODEL   |
| Full revocation              | COMPLETE_AS_MODEL   |
| Partial revocation           | COMPLETE_AS_MODEL   |
| Suspension                   | COMPLETE_AS_MODEL   |
| Expiration distinction       | COMPLETE_AS_MODEL   |
| Supersession distinction     | COMPLETE_AS_MODEL   |
| Dependency closure           | COMPLETE_AS_MODEL   |
| Selective invalidation       | COMPLETE_AS_MODEL   |
| Independent paths            | COMPLETE_AS_MODEL   |
| Provenance topology          | COMPLETE_AS_MODEL   |
| Delegation propagation       | COMPLETE_AS_MODEL   |
| Witness invalidation         | COMPLETE_AS_MODEL   |
| Authorization invalidation   | COMPLETE_AS_MODEL   |
| Agent boundary               | COMPLETE_AS_MODEL   |
| Skill boundary               | COMPLETE_AS_MODEL   |
| Workflow boundary            | COMPLETE_AS_MODEL   |
| Transaction boundary         | COMPLETE_AS_MODEL   |
| Commit-time revalidation     | COMPLETE_AS_MODEL   |
| MVCC/CAS                     | COMPLETE_AS_MODEL   |
| Atomicity                    | COMPLETE_AS_MODEL   |
| H/M/L                        | COMPLETE_AS_MODEL   |
| Workflows                    | COMPLETE_AS_MODEL   |
| Protocols                    | COMPLETE_AS_MODEL   |
| Invariants                   | COMPLETE_AS_MODEL   |
| Failure modes                | COMPLETE_AS_MODEL   |
| Recovery                     | COMPLETE_AS_MODEL   |
| Validators                   | COMPLETE_AS_MODEL   |
| Tests                        | COMPLETE_AS_MODEL   |
| Falsifiers                   | COMPLETE_AS_MODEL   |
| RSCF                         | COMPLETE_AS_MODEL   |
| GMEF                         | COMPLETE_AS_MODEL   |
| Executable revocation engine | UNKNOWN/GAP         |
| Executed test evidence       | UNKNOWN/GAP         |
| Production validation        | UNKNOWN/GAP         |
| Formal verification          | UNKNOWN/GAP         |
| Canon admission              | UNKNOWN/GAP         |

---

# 154. Hard Boundary Block

```text
REVOCATION != DELETION

REVOCATION != EXPIRATION

REVOCATION != SUSPENSION

REVOCATION != SUPERSESSION

REVOCATION != POLICY_DENY

REVOCATION != AUTHORIZATION_DENY

REVOCATION != AGENT_TERMINATION

REVOCATION != CAPABILITY_REMOVAL

REVOCATION != MEMORY_ERASURE

REVOCATION_REQUEST != REVOCATION_COMMIT

CAPABILITY_TO_REVOKE != AUTHORITY_TO_REVOKE

POLICY_ALLOW != AUTHORITY_TO_REVOKE

ROLE != AUTHORITY_TO_REVOKE

HISTORICAL_ALLOW != CURRENT_AUTHORITY

REVOKED_PARENT != VALID_DEPENDENT_CHILD

REVOKED_ROOT != VALID_DEPENDENT_BRANCH

REVOKED_DELEGATION != VALID_DEPENDENT_WITNESS

STALE_WITNESS != CURRENT_AUTHORITY

STALE_AUTHORIZATION != CURRENT_COMMIT_PERMISSION

PARTIAL_REVOCATION != TOTAL_REVOCATION

INDEPENDENT_PATH != DEPENDENT_PATH

MULTIPLE_DESCENDANTS != MULTIPLE_INDEPENDENT_ROOTS

QUARANTINE != PROOF_OF_COMPROMISE

REVOCATION != RETROACTIVE_PROOF_OF_INVALIDITY

REVOCATION != EFFECT_REVERSAL

COMPENSATION != AUTOMATIC

PROPOSAL != COMMIT

UNKNOWN/GAP != ACTIVE

UNKNOWN/GAP != PASS

CONFLICT != ALLOW

STRUCTURAL_MODEL != IMPLEMENTED_RUNTIME

IMPLEMENTED != VALIDATED

TESTED != FORMALLY_VERIFIED

MODEL != EMPIRICAL_FACT
```

---

# 155. Canon Boundary

Trang Phan remains the origin architect and steward of AMOS.

This artifact defines a proposed structural revocation architecture.

It does not establish that AMOS currently possesses:

```text
an executable revocation engine;

a production revocation registry;

a production authority dependency graph;

atomic revocation propagation;

distributed revocation finality;

MVCC/CAS enforcement;

transaction-level revocation barriers;

cryptographic revocation infrastructure;

executed adversarial validation;

formal security proofs;

or canonical admission of every rule herein.
```

Therefore:

```yaml
artifact_status: PROPOSED
epistemic_class: MODEL
structural_status: COMPLETE_AS_MODEL
runtime_status: UNKNOWN/GAP
validation_status: UNKNOWN/GAP
canonical_status: UNKNOWN/GAP
```

Applicable validated AMOS source canon outranks generated model additions subject to:

```text
version;

scope;

regime;

provenance;

freshness;

supersession;

and dependency compatibility.
```

---

# 156. Final Revocation Contract

AMOS SHALL preserve:

```text
REVOCATION TRIGGER
      ↓
REVOCATION REQUEST
      ↓
REVOCATION AUTHORITY
      ↓
TARGET IDENTITY
      ↓
TARGET VERSION
      ↓
REVOCATION MODE
      ↓
REVOCATION SCOPE
      ↓
EFFECTIVE TIME
      ↓
DEPENDENCY CLOSURE
      ↓
INDEPENDENT-PATH ANALYSIS
      ↓
REVOCATION DECISION
      ↓
ATOMIC COMMIT
      ↓
AUTHORITY GRAPH UPDATE
      ↓
DELEGATION INVALIDATION
      ↓
AUTHORITY-WITNESS INVALIDATION
      ↓
AUTHORIZATION INVALIDATION
      ↓
QUEUE / RESERVATION REVIEW
      ↓
TRANSACTION REVALIDATION
      ↓
PROVENANCE / AUDIT
```

The central invariant is:

> **Once authority has been validly revoked, no future consequential effect may rely solely on that revoked authority; dependent authority must be invalidated or revalidated, while genuinely independent authority paths and historical provenance must be preserved.**

Therefore:

```text
AUTHORITY A
      ↓
DELEGATION B
      ↓
WITNESS C
      ↓
AUTHORIZATION D
```

with:

```text
A → REVOKED
```

requires:

```text
B → INVALID / REVALIDATE

C → STALE / INVALID

D → NOT SUFFICIENT FOR NEW COMMIT
```

unless an independently valid authority path supports the action.

Likewise:

```text
ALLOW at T0
```

cannot override:

```text
REVOCATION at T1
```

for:

```text
COMMIT at T2
```

when current authority is required.

AMOS MUST NOT resurrect revoked authority through:

```text
stale caches;

old witnesses;

old authorization decisions;

role changes;

memory;

agent restart;

child-agent spawning;

Skill composition;

capability routing;

aliasing;

delegation duplication;

or correlated descendant paths.
```

AMOS MUST preserve the distinction between:

```text
revoking authority;

invalidating dependent authority;

stopping execution;

reversing an effect;

and compensating for a completed effect.
```

AMOS SHOULD invalidate only the smallest proven dependency closure necessary to restore integrity.

AMOS SHOULD preserve independent authority rather than globally destroying unrelated valid state.

AMOS MUST preserve revocation provenance and authority ancestry.

AMOS SHOULD bind consequential authorization to sufficiently fresh revocation state.

AMOS SHOULD use versioned, atomic, concurrency-safe state transitions where mutable authority can change between check and commit.

Where revocation state, revocation authority, dependency closure, finality, or provenance cannot be established, the correct result is:

```text
UNKNOWN_GAP
```

or, where conflicting authoritative evidence exists:

```text
BLOCK_CONFLICT
```

—not permissive inference.

Integrity remains prior to completeness, fluency, convenience, speed, availability, or optimization.

---

# END — REVOCATION.md

```
```

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
