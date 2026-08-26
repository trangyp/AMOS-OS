---
tags: ['control_plane', 'authority', 'note']
---

# DELEGATION.md

---
title: "AMOS Delegation Architecture"
artifact: "DELEGATION.md"
origin_architect: "Trang Phan"
steward: "Trang Phan"
system: "AMOS OS"
artifact_class: "GOVERNED_AUTHORITY_DELEGATION_CONTRACT"
status: "PROPOSED / STRUCTURALLY_COMPLETE / IMPLEMENTATION-UNVALIDATED"
epistemic_class: "MODEL"
version: "1.0.0"
updated: "2026-08-26"
default_state: "UNKNOWN_GAP"
---

# AMOS Delegation Architecture

## 0. Status

`DELEGATION.md` defines the AMOS OS contract for transferring a bounded subset of authority from an authorized principal to another principal without creating new authority, silently widening scope, erasing provenance, or bypassing authorization.

Delegation is an authority transformation.

It is not:

```text
authentication;

role assignment;

capability discovery;

capability execution;

policy evaluation;

authorization;

impersonation;

ownership transfer;

task assignment;

agent spawning;

workflow routing;

or commit.
```

The canonical delegation chain is:

```text
AUTHORITY ROOT
      ↓
DELEGATOR
      ↓
DELEGATION ELIGIBILITY
      ↓
DELEGATION PROPOSAL
      ↓
ATTENUATION
      ↓
DELEGATION VALIDATION
      ↓
DELEGATION RECORD
      ↓
DELEGATE AUTHORITY
      ↓
AUTHORITY RESOLUTION
      ↓
AUTHORITY WITNESS
      ↓
AUTHORIZATION
      ↓
COMMIT-TIME REVALIDATION
```

Never:

```text
DELEGATION
=
NEW UNBOUNDED AUTHORITY
```

---

# 1. Purpose

The purpose of delegation is to permit controlled transfer of already-held authority while preserving:

```text
authority ancestry;

principal identity;

scope;

operation restrictions;

resource restrictions;

effect restrictions;

recipient restrictions;

purpose restrictions;

temporal validity;

delegation depth;

cumulative limits;

constraints;

revocation;

provenance;

auditability;

and commit-time freshness.
```

The governing question is:

> **May principal A delegate this exact subset of its current authority to principal B, under these constraints, for this purpose, during this time, with this delegation depth and revocation semantics?**

---

# 2. Core Delegation Laws

```text
DELEGATION != AUTHORIZATION

DELEGATION != AUTHENTICATION

DELEGATION != CAPABILITY

DELEGATION != ROLE ASSIGNMENT

DELEGATION != IMPERSONATION

DELEGATION != OWNERSHIP

DELEGATION != COMMIT

DELEGATOR_AUTHORITY != DELEGATE_AUTHORITY

DELEGATED_AUTHORITY <= DELEGATOR_AUTHORITY

DELEGATE_SCOPE ⊆ DELEGATOR_SCOPE

DELEGATE_OPERATIONS ⊆ DELEGATOR_OPERATIONS

DELEGATE_RESOURCES ⊆ DELEGATOR_RESOURCES

DELEGATE_EFFECTS ⊆ DELEGATOR_EFFECTS

DELEGATE_RECIPIENTS ⊆ DELEGATOR_RECIPIENTS

DELEGATE_DURATION <= DELEGATOR_DURATION

DELEGATE_BUDGET <= AVAILABLE_DELEGATABLE_BUDGET

DELEGATION_DEPTH_CHILD < DELEGATION_DEPTH_PARENT

NON_DELEGABLE_AUTHORITY != DELEGABLE_AUTHORITY

REVOKED_PARENT != VALID_CHILD

EXPIRED_PARENT != VALID_CHILD

INVALID_PARENT != VALID_CHILD

UNKNOWN_PARENT != VALID_CHILD

POLICY_ALLOW != DELEGATION_AUTHORITY

CAPABILITY_AVAILABLE != DELEGATION_AUTHORITY

ROLE != DELEGATION_AUTHORITY

TASK_ASSIGNMENT != AUTHORITY_DELEGATION

PROPOSAL != COMMIT

UNKNOWN/GAP != VALID_DELEGATION
```

---

# 3. Definition

A delegation is a provenance-bound authority edge:

```text
D:
Delegator
→ Delegate
```

with a constrained authority envelope.

Conceptually:

```text
Delegation =
(
    delegation_id,
    delegator,
    delegate,
    parent_authority,
    authority_subset,
    scope,
    operations,
    resources,
    effects,
    recipients,
    purposes,
    constraints,
    cumulative_limits,
    valid_from,
    valid_until,
    delegation_depth,
    redelegation_policy,
    revocation_policy,
    provenance
)
```

---

# 4. Delegation Equation

AMOS MODEL:

```text
ValidDelegation(D,t)
=
DelegatorValid(D,t)
∧ ParentAuthorityValid(D,t)
∧ DelegationPermitted(D,t)
∧ DelegateValid(D,t)
∧ AuthoritySubset(D)
∧ ScopeAttenuated(D)
∧ OperationsAttenuated(D)
∧ ResourcesAttenuated(D)
∧ EffectsAttenuated(D)
∧ RecipientsAttenuated(D)
∧ PurposeCompatible(D)
∧ TemporalAttenuated(D,t)
∧ DepthValid(D)
∧ ConstraintsPreserved(D)
∧ CumulativeLimitsValid(D)
∧ RevocationValid(D,t)
∧ ProvenanceValid(D)
```

Where:

```text
Authority(child)
⊆
DelegableAuthority(parent)
```

---

# 5. Architectural Position

```text
IDENTITY
   ↓
AUTHENTICATION
   ↓
AUTHORITY REGISTRY
   ↓
AUTHORITY RESOLVER
   ↓
DELEGATION ENGINE
   ↓
DELEGATION RECORD
   ↓
AUTHORITY GRAPH
   ↓
AUTHORITY RESOLVER
   ↓
AUTHORITY WITNESS
   ↓
POLICY ENGINE
   ↓
AUTHORIZATION ENGINE
   ↓
COMMIT GUARD
```

Delegation modifies the authority graph.

Authorization consumes the resulting authority state.

---

# 6. Responsibility Boundary

The delegation subsystem owns:

```text
delegation proposals;

delegation attenuation;

delegation validation;

delegation lineage;

delegation depth;

redelegation restrictions;

delegation expiration;

delegation revocation propagation;

delegation constraints;

delegation provenance;

delegation conflict detection;

delegation state transitions.
```

It does not own:

```text
identity issuance;

authentication;

root authority issuance;

policy authorship;

capability implementation;

authorization decisions;

effect execution;

transaction commit;

or external completion.
```

---

# 7. Principals

Delegation involves at minimum:

```text
Delegator
Delegate
```

Additional principals MAY include:

```text
AuthorityIssuer

DelegationApprover

RevocationAuthority

AuditPrincipal

ControlPlanePrincipal
```

Each role MUST remain distinct unless an explicit authority contract allows combination.

---

# 8. Delegator

The delegator is the principal whose existing authority is being attenuated and transferred.

Required properties:

```yaml
delegator:
  principal_id: string
  principal_type: string
  authority_witness_ref: string
  authentication_ref: null
```

The delegator MUST possess current authority over every authority dimension delegated.

---

# 9. Delegate

The delegate is the receiving principal.

```yaml
delegate:
  principal_id: string
  principal_type: string
```

Delegate identity MUST be stable enough to prevent authority substitution.

---

# 10. Delegation Eligibility

A principal may delegate only when the parent authority explicitly or structurally permits delegation.

```text
HAS_AUTHORITY
↛
MAY_DELEGATE_AUTHORITY
```

The parent authority SHOULD contain:

```yaml
delegation_policy:
  delegable: true
  maximum_depth: integer
  allowed_delegate_types: []
  allowed_operations: []
  prohibited_operations: []
  temporal_limit: null
  cumulative_limit: null
  redelegation_allowed: false
```

---

# 11. Non-Delegable Authority

Authority MAY be marked:

```text
NON_DELEGABLE
```

Examples may include authority requiring:

```text
personal consent;

personal identity;

specific office-holder status;

direct human approval;

non-transferable credentials;

or explicit named-principal execution.
```

If:

```text
parent.delegable = false
```

then:

```text
CreateDelegation(parent) = DENY
```

---

# 12. Delegation Request

```yaml
delegation_request:
  schema: "AMOS.DELEGATION_REQUEST"
  schema_version: "1.0"

  request_id: string
  requested_at: timestamp

  delegator:
    principal_id: string
    authority_witness_ref: string

  delegate:
    principal_id: string

  parent_authority:
    authority_id: string
    authority_version: null
    authority_digest: null

  requested_authority:
    operations: []
    capabilities: []
    resources: []
    resource_classes: []
    effects: []
    recipients: []
    purposes: []

  scope: {}
  regime: {}

  temporal:
    valid_from: timestamp
    valid_until: timestamp

  constraints: []

  cumulative_limits: {}

  redelegation:
    allowed: false
    maximum_remaining_depth: 0

  revocation: {}

  provenance: {}
```

---

# 13. Delegation Decision

```yaml
delegation_decision:
  schema: "AMOS.DELEGATION_DECISION"
  schema_version: "1.0"

  decision_id: string
  request_id: string

  state:
    - ALLOW
    - ALLOW_ATTENUATED
    - DENY
    - BLOCK_AUTHORITY
    - BLOCK_SCOPE
    - BLOCK_CONSTRAINT
    - BLOCK_DEPTH
    - BLOCK_CONFLICT
    - REVALIDATE
    - UNKNOWN_GAP

  effective_authority: {}

  removed_authority: []

  inherited_constraints: []

  additional_constraints: []

  lineage: []

  failed_invariants: []
  gaps: []

  evaluated_at: timestamp
  valid_until: null

  provenance: {}
```

---

# 14. Delegation Record

A successful delegation MUST produce a durable delegation record if the authority system is persistent.

```yaml
delegation_record:
  schema: "AMOS.DELEGATION_RECORD"
  schema_version: "1.0"

  delegation_id: string

  delegator_id: string
  delegate_id: string

  parent_authority_id: string
  parent_delegation_id: null

  root_authority_id: string

  authority:
    operations: []
    capabilities: []
    resources: []
    effects: []
    recipients: []
    purposes: []

  scope: {}
  regime: {}

  constraints: []

  cumulative_limits: {}

  temporal:
    issued_at: timestamp
    valid_from: timestamp
    valid_until: timestamp

  depth:
    root_depth: integer
    remaining_depth: integer

  redelegation:
    allowed: boolean

  revocation:
    state: ACTIVE
    revocation_authority: []
    revoked_at: null
    reason: null

  integrity:
    parent_digest: string
    delegation_digest: string

  provenance: {}
```

---

# 15. Delegation States

```text
PROPOSED
   ↓
VALIDATING
   ├──→ UNKNOWN_GAP
   ├──→ DENIED
   ├──→ CONFLICT
   └──→ APPROVED
            ↓
         ACTIVE
        /   |   \
       /    |    \
 EXPIRED REVOKED SUPERSEDED
```

Optional operational states:

```text
SUSPENDED

QUARANTINED

REVALIDATION_REQUIRED
```

---

# 16. Authority Attenuation

Delegation MUST be attenuating.

For every permission dimension:

```text
ChildPermission
⊆
ParentPermission
```

AMOS MODEL:

```text
A_child
=
A_parent
∩
A_requested
∩
A_policy
∩
A_constraints
```

No union-based widening is allowed.

Never:

```text
A_child
=
A_parent ∪ A_requested
```

---

# 17. Scope Attenuation

Required:

```text
Scope_child
⊆
Scope_parent
```

Examples:

```text
Parent:
all files in PROJECT_A

Child:
folder PROJECT_A/REPORTS
```

valid.

But:

```text
Parent:
PROJECT_A

Child:
PROJECT_A + PROJECT_B
```

invalid unless independent authority covers `PROJECT_B`.

---

# 18. Operation Attenuation

```text
Operations_child
⊆
Operations_parent
```

Example:

```text
Parent = {READ, CREATE, UPDATE}

Child = {READ, UPDATE}
```

valid.

```text
Child = {DELETE}
```

invalid unless DELETE exists independently in the parent authority envelope.

---

# 19. Capability Attenuation

Where authority binds capabilities:

```text
Capabilities_child
⊆
Capabilities_parent
```

Capability delegation does not imply permission to use all operations exposed by that capability.

---

# 20. Resource Attenuation

```text
Resources_child
⊆
Resources_parent
```

Resource-class authority MUST NOT silently widen into unrestricted instance authority outside the authorized class.

---

# 21. Effect Attenuation

```text
Effects_child
⊆
Effects_parent
```

A delegation to:

```text
DRAFT
```

does not imply:

```text
SEND
```

A delegation to:

```text
PROPOSE
```

does not imply:

```text
COMMIT
```

---

# 22. Recipient Attenuation

```text
Recipients_child
⊆
Recipients_parent
```

Example:

```text
Parent:
internal recipients

Child:
team-alpha recipients
```

valid.

Child delegation to external recipients is invalid unless the parent permits it.

---

# 23. Purpose Binding

Delegated authority MAY be purpose-limited.

```yaml
purpose:
  purpose_id: string
  permitted: true
```

Example:

```text
READ customer records
FOR support resolution
```

does not automatically authorize:

```text
READ customer records
FOR marketing export
```

---

# 24. Temporal Attenuation

Required:

```text
valid_from_child >= valid_from_parent

valid_until_child <= valid_until_parent
```

A child delegation cannot outlive its parent.

---

# 25. Temporal Inheritance

AMOS MODEL:

```text
Expiry_child
=
min(
    requested_expiry,
    parent_expiry,
    policy_expiry
)
```

---

# 26. Delegation Depth

Delegation depth prevents unbounded authority propagation.

Example:

```text
ROOT
 ↓
D1
 ↓
D2
 ↓
D3
```

Each delegation consumes available depth.

---

# 27. Depth Rule

```text
remaining_depth_child
<
remaining_depth_parent
```

Recommended representation:

```text
remaining_depth_child
=
remaining_depth_parent - 1
```

unless a stricter policy applies.

---

# 28. Redelegation

Redelegation MUST be explicitly permitted.

```text
DELEGATED_AUTHORITY
↛
REDELEGATION_AUTHORITY
```

If:

```text
redelegation.allowed = false
```

then the delegate may exercise authority but cannot delegate it further.

---

# 29. Delegation Chain

Example:

```text
ROOT AUTHORITY R0
      ↓
DELEGATION D1
      ↓
PRINCIPAL P1
      ↓
DELEGATION D2
      ↓
PRINCIPAL P2
```

Effective authority at `P2` cannot exceed the intersection of all upstream authority envelopes.

AMOS MODEL:

```text
A_P2
=
A_R0
∩ A_D1
∩ A_D2
```

---

# 30. Constraint Inheritance

Hard parent constraints MUST survive delegation.

```text
Parent:
MAX_AMOUNT <= 1000
```

Child cannot specify:

```text
MAX_AMOUNT <= 5000
```

Effective constraint remains at most:

```text
MAX_AMOUNT <= 1000
```

---

# 31. Constraint Tightening

Delegation MAY tighten constraints.

Example:

```text
Parent:
MAX_AMOUNT <= 1000

Child:
MAX_AMOUNT <= 250
```

valid.

---

# 32. Constraint Weakening

Delegation MUST NOT weaken mandatory parent constraints.

```text
ChildConstraint
must be
>= restrictive strength of
ParentConstraint
```

The exact comparison operator depends on the constraint type.

---

# 33. Cumulative Limits

Delegated authority may carry cumulative limits such as:

```text
total spend;

number of operations;

disclosure budget;

compute budget;

API quota;

transaction count;

risk budget.
```

Delegation MUST NOT duplicate a finite parent budget into multiple independent full child budgets.

---

# 34. Budget Conservation

Example:

```text
Parent available budget = 100
```

Creating:

```text
Delegate A budget = 100
Delegate B budget = 100
```

must not create:

```text
effective budget = 200
```

unless the parent authority genuinely permits independent non-exclusive allocations.

---

# 35. Reservation

Where delegation consumes scarce authority capacity:

```text
CHECK
→ RESERVE
→ COMMIT
```

or equivalent atomic control SHOULD be used.

---

# 36. Concurrent Delegation Race

Example:

```text
available delegatable budget = 100

D1 requests 80
D2 requests 80
```

Both requests cannot independently reserve the same 100.

The control plane must serialize, reserve atomically, or use an equivalent concurrency-safe mechanism.

---

# 37. Delegation Provenance

Every delegation SHOULD preserve:

```text
root authority;

parent authority;

parent delegation;

delegator;

delegate;

issuer;

approver where applicable;

authority versions;

authority hashes;

constraints;

scope;

time;

regime;

reason/purpose;

validation evidence;

revocation state.
```

---

# 38. Authority Ancestry

Delegation lineage MUST be reconstructable.

Example:

```text
ROOT-R1
   ↓
D-100
   ↓
P-A
   ↓
D-101
   ↓
P-B
```

An authority witness for `P-B` SHOULD be able to establish this ancestry without inventing missing edges.

---

# 39. Provenance Topology

Multiple descendants of one root do not constitute independent authority sources.

```text
ROOT R1
 ├── D1
 ├── D2
 └── D3
```

still has:

```text
independent root count = 1
```

where independence matters.

---

# 40. Delegation Digest

A delegation SHOULD have a stable integrity digest.

Conceptually:

```text
DelegationDigest =
H(
  delegator
  + delegate
  + parent_authority
  + effective_authority
  + scope
  + constraints
  + temporal_bounds
  + depth
  + revocation_policy
)
```

Material mutation requires a new digest/version.

---

# 41. Immutable Delegation Identity

A delegation record SHOULD NOT be silently rewritten to represent materially different authority.

Prefer:

```text
D1 v1
→ SUPERSEDED

D1 v2
→ ACTIVE
```

or a new delegation identity.

---

# 42. Revocation

Delegation MUST support revocation where the governing authority model permits revocable authority.

Revocation MAY target:

```text
one delegation;

one delegate;

one branch;

one authority class;

one operation;

one resource;

one effect;

or an entire descendant subtree.
```

---

# 43. Parent Revocation

If parent authority is revoked:

```text
REVOKED(parent)
```

all dependent child authority becomes invalid unless independently supported by another valid authority path.

---

# 44. Cascading Revocation

Conceptually:

```text
Revoke(D1)
    ↓
Invalidate(D1 descendants)
```

But only descendants causally dependent on `D1` should be invalidated.

Independent authority paths SHOULD remain intact.

---

# 45. Selective Revocation

Example:

```text
P2 authority =
Path A
+
Path B
```

If Path A is revoked but Path B independently authorizes the same action:

```text
P2 MAY retain authority
```

subject to complete authority re-resolution.

Do not revoke independent authority merely because one path failed.

---

# 46. Partial Revocation

A delegation MAY be narrowed.

Example:

```text
Before:
{READ, UPDATE, DELETE}

After:
{READ, UPDATE}
```

`DELETE` becomes invalid.

This SHOULD be represented as an explicit new authority state rather than hidden mutation.

---

# 47. Revocation Freshness

Authorization MUST use sufficiently current revocation state.

```text
AUTHORITY WITNESS VALID AT T0
```

does not guarantee validity at `T1`.

---

# 48. Revocation Race

```text
T0 delegation active
T1 authorization allow
T2 delegation revoked
T3 commit attempted
```

Result:

```text
BLOCK_AUTHORITY
```

not historical allow.

---

# 49. Expiration

Expired delegation is not valid authority.

```text
now > valid_until
→ EXPIRED
```

No separate revocation is required for expiration.

---

# 50. Suspension

A delegation MAY support temporary suspension.

```text
ACTIVE
→ SUSPENDED
→ ACTIVE
```

only through a governed transition.

Suspended authority MUST NOT authorize effects.

---

# 51. Quarantine

A delegation MAY enter:

```text
QUARANTINED
```

when integrity, provenance, conflict, or compromise is suspected.

Quarantine is fail-closed.

---

# 52. Conflict

Conflicting authority evidence MUST remain visible.

Example:

```text
SOURCE A:
delegation ACTIVE

SOURCE B:
delegation REVOKED
```

Result:

```text
BLOCK_CONFLICT
```

or:

```text
UNKNOWN_GAP
```

until authoritative discrimination resolves the state.

---

# 53. Delegation and Policy

Policy may constrain whether delegation is allowed.

But:

```text
POLICY_ALLOW
!=
AUTHORITY_TO_DELEGATE
```

Both may be required.

---

# 54. Delegation and Capability

A capability may technically support delegation operations.

That does not establish authority to create a delegation.

```text
CAN_CREATE_DELEGATION
!=
MAY_CREATE_DELEGATION
```

---

# 55. Delegation and Authorization

Delegation creates or transforms authority state.

Authorization determines whether that authority permits a particular requested action.

Therefore:

```text
VALID_DELEGATION
+
VALID_AUTHORITY_WITNESS
+
POLICY_ALLOW
+
VALID_CAPABILITY
+
VALID_REQUEST
=
POTENTIALLY_AUTHORIZED
```

not automatically committed.

---

# 56. Delegation and Agents

An agent may receive delegated authority.

Agent capability does not determine authority breadth.

```text
HIGH_CAPABILITY_AGENT
```

may have:

```text
LOW_AUTHORITY
```

and:

```text
LOW_CAPABILITY_AGENT
```

may hold authority it cannot technically exercise.

---

# 57. Agent Spawning

Creating a child agent does not automatically delegate authority.

```text
SPAWN_CHILD_AGENT
!=
DELEGATE_PARENT_AUTHORITY
```

Any authority granted to the child must pass through explicit delegation or another governed authority mechanism.

---

# 58. Agent Handoff

Task handoff does not imply authority handoff.

```text
"Please handle this task"
```

may establish workflow responsibility but not necessarily authorization for all actions needed to complete it.

---

# 59. Agent Self-Delegation

An agent MUST NOT expand its own authority by:

```text
creating another agent;

changing roles;

rewriting memory;

changing prompts;

creating a Skill;

routing through another capability;

or splitting an action into smaller steps.
```

---

# 60. Cross-Skill Delegation

Skills may consume delegated authority evidence.

Skills MUST NOT reinterpret narrow delegated authority as broad authority.

Example:

```text
Skill A:
authorized READ
```

cannot transfer:

```text
WRITE
```

authority to Skill B unless a valid authority path supports it.

---

# 61. Skill Composition

Delegated authority MUST survive semantic composition.

```text
READ
+
TRANSFORM
+
SEND
```

may produce disclosure even when each step individually appears ordinary.

Transaction-level authorization remains required where composition changes the governed effect.

---

# 62. Delegation and Memory

Memory may record delegation state.

Memory is not the authority source.

```text
MEMORY:
"P1 delegated access to P2"
```

is evidence requiring validation against authoritative delegation state.

---

# 63. Delegation and User Intent

Where user authority governs, delegation MUST remain compatible with current user intent.

A stale historical delegation must not override a current revocation or contradictory instruction.

---

# 64. Delegation and Impersonation

Delegation preserves principal identity.

```text
Delegator = P1
Delegate = P2
```

After delegation:

```text
P2 remains P2
```

P2 does not become P1.

Audit records MUST preserve the actual actor.

---

# 65. No Identity Laundering

A delegate MUST NOT represent actions as performed directly by the delegator unless an explicit impersonation/proxy protocol separately authorizes that representation.

---

# 66. Delegation and Accountability

Delegation SHOULD preserve:

```text
who issued authority;

who delegated;

who accepted;

who exercised;

who authorized;

who committed;

who received the effect.
```

These identities may differ.

---

# 67. Delegation Acceptance

Some delegation regimes MAY require delegate acceptance.

```text
PROPOSED
→ ACCEPTED
→ ACTIVE
```

Others may permit unilateral delegation.

The applicable rule MUST be explicit.

---

# 68. Delegation Rejection

A delegate MAY reject delegated authority where the regime supports voluntary acceptance.

Rejected delegation MUST NOT become active.

---

# 69. Delegation Purpose

A delegation SHOULD carry an explicit reason or purpose when authority interpretation depends on purpose.

Example:

```yaml
purpose:
  id: "INCIDENT_RESPONSE"
  description: "Temporary log access for incident 2026-08-26-A"
```

---

# 70. Purpose Drift

If the delegated action's purpose materially changes:

```text
PURPOSE_A
→
PURPOSE_B
```

purpose-bound authority MUST be revalidated.

---

# 71. Environment Binding

Delegation may be environment-specific.

```text
SANDBOX authority
↛
PRODUCTION authority
```

---

# 72. Regime Binding

Delegation may be valid only under:

```text
NORMAL

INCIDENT

RECOVERY

MAINTENANCE

EMERGENCY

SANDBOX
```

A regime transition may invalidate the delegation.

---

# 73. Emergency Delegation

Emergency delegation MAY be permitted under explicit emergency governance.

It MUST preserve:

```text
trigger;

issuer;

delegate;

scope;

operations;

resources;

duration;

constraints;

revocation;

audit;

termination condition.
```

---

# 74. Break-Glass Delegation

Break-glass delegation MUST be:

```text
explicit;

bounded;

short-lived;

strongly attributable;

auditable;

revocable;

and post-reviewed.
```

Never:

```text
BREAK_GLASS
=
PERMANENT ADMIN AUTHORITY
```

---

# 75. H/M/L Applicability

## H — Governing Layer

H-level delegation concerns:

```text
root authority;

institutional authority;

authority classes;

delegation laws;

jurisdiction;

global constraints;

trust roots;

revocation governance.
```

## M — Operational Layer

M-level delegation concerns:

```text
services;

workflows;

capabilities;

resource classes;

teams;

projects;

transactions;

budgets;

operational roles.
```

## L — Effect Layer

L-level delegation concerns:

```text
exact operation;

exact target;

exact recipient;

exact amount;

exact effect;

exact transaction;

exact expiry;

exact commit attempt.
```

---

# 76. Cross-Scale Delegation

A broad H-level authority does not automatically authorize every L-level effect.

Likewise:

```text
L-level authority
```

does not imply:

```text
H-level governance authority
```

Cross-scale mappings MUST be explicit.

---

# 77. Delegation Graph

Delegation SHOULD be modeled as a directed graph:

```text
G_D = (P, D)
```

where:

```text
P = principals
D = delegation edges
```

Each edge carries typed authority constraints.

---

# 78. Graph Requirements

The delegation graph SHOULD support:

```text
ancestry traversal;

descendant traversal;

cycle detection;

revocation propagation;

depth calculation;

scope intersection;

constraint accumulation;

independent-path detection;

conflict detection.
```

---

# 79. Delegation Cycles

Authority delegation cycles SHOULD be rejected unless an explicit semantics exists.

Example:

```text
A → B
B → C
C → A
```

must not generate self-reinforcing authority.

---

# 80. Cycle Invariant

```text
DELEGATION_CYCLE
!=
AUTHORITY_AMPLIFICATION
```

A cycle cannot create authority absent from its roots.

---

# 81. Multi-Parent Authority

A principal may receive authority through multiple paths.

```text
R1 → P
R2 → P
```

These paths MUST remain provenance-distinct.

Authority combination must follow explicit composition rules.

---

# 82. Authority Union

Where independent authority grants may legally compose:

```text
EffectiveAuthority
=
Union(valid authority grants)
```

but each individual delegation remains attenuated relative to its own parent.

Union across independent grants MUST NOT be confused with widening a single delegation.

---

# 83. Authority Intersection

Where an action depends on multiple simultaneous authorities:

```text
EffectiveAuthority
=
Intersection(required authority constraints)
```

The composition operator MUST be explicit.

---

# 84. Provenance Independence

Independence MUST be demonstrated rather than assumed.

Two authority paths derived from the same root may not provide independent corroboration.

---

# 85. Authority Witness Integration

The `AUTHORITY_RESOLVER` SHOULD resolve delegation ancestry and produce an `AUTHORITY_WITNESS`.

The witness SHOULD include:

```text
root authority;

delegation path;

effective scope;

effective operations;

effective constraints;

effective expiry;

revocation status;

depth;

provenance.
```

---

# 86. Authority Witness Rule

A delegation record is not itself sufficient proof of current authorization.

```text
DELEGATION_RECORD
→
AUTHORITY_RESOLUTION
→
AUTHORITY_WITNESS
→
AUTHORIZATION
```

---

# 87. Delegation Workflow

```text
01 RECEIVE DELEGATION REQUEST

02 RESOLVE DELEGATOR

03 VALIDATE DELEGATOR AUTHENTICATION

04 LOAD CURRENT PARENT AUTHORITY

05 VERIFY DELEGATION IS PERMITTED

06 RESOLVE DELEGATE

07 NORMALIZE REQUESTED AUTHORITY

08 INTERSECT WITH PARENT AUTHORITY

09 APPLY POLICY

10 APPLY HARD CONSTRAINTS

11 APPLY TEMPORAL ATTENUATION

12 APPLY DELEGATION DEPTH

13 APPLY REDELEGATION RULES

14 APPLY CUMULATIVE LIMITS

15 CHECK CONCURRENT RESERVATIONS

16 CHECK PROVENANCE

17 CHECK CONFLICTS

18 CHECK CYCLES

19 PRODUCE DELEGATION DECISION

20 RESERVE SCARCE AUTHORITY IF REQUIRED

21 COMMIT DELEGATION RECORD

22 UPDATE AUTHORITY GRAPH

23 INVALIDATE AFFECTED AUTHORITY WITNESSES

24 ISSUE / RESOLVE NEW AUTHORITY WITNESS

25 RECORD AUDIT EVIDENCE
```

---

# 88. Revocation Workflow

```text
01 RECEIVE REVOCATION REQUEST

02 RESOLVE REVOCATION PRINCIPAL

03 VALIDATE REVOCATION AUTHORITY

04 RESOLVE TARGET DELEGATION

05 LOAD DESCENDANT GRAPH

06 IDENTIFY DEPENDENT AUTHORITY

07 IDENTIFY INDEPENDENT AUTHORITY PATHS

08 APPLY REVOCATION

09 INVALIDATE DEPENDENT WITNESSES

10 INVALIDATE DEPENDENT AUTHORIZATIONS

11 PRESERVE INDEPENDENT VALID AUTHORITY

12 UPDATE AUTHORITY GRAPH

13 RECORD REVOCATION PROVENANCE

14 REQUIRE COMMIT-TIME REVALIDATION
```

---

# 89. Redelegation Workflow

```text
ACTIVE DELEGATION
      ↓
CHECK REDELEGATION PERMISSION
      ↓
CHECK REMAINING DEPTH
      ↓
CHECK PARENT FRESHNESS
      ↓
ATTENUATE AUTHORITY
      ↓
PRESERVE ALL HARD CONSTRAINTS
      ↓
CREATE CHILD DELEGATION
      ↓
LINK PARENT
      ↓
UPDATE GRAPH
```

---

# 90. Delegation Protocol

```yaml
delegate_authority:
  delegator: {}
  delegate: {}
  parent_authority: {}

  requested:
    operations: []
    capabilities: []
    resources: []
    effects: []
    recipients: []
    purposes: []

  scope: {}
  regime: {}

  temporal: {}

  constraints: []

  cumulative_limits: {}

  redelegation: {}

  provenance: {}
```

---

# 91. Delegation Response Protocol

```yaml
delegate_authority_result:
  state:
    - ACTIVE
    - ALLOW_ATTENUATED
    - DENIED
    - BLOCK_AUTHORITY
    - BLOCK_SCOPE
    - BLOCK_CONSTRAINT
    - BLOCK_DEPTH
    - BLOCK_CONFLICT
    - UNKNOWN_GAP

  delegation_record: null
  removed_permissions: []
  inherited_constraints: []
  failed_invariants: []
  gaps: []
```

---

# 92. Revocation Protocol

```yaml
revoke_delegation:
  revoker:
    principal_id: string
    authority_witness_ref: string

  delegation_id: string

  scope:
    mode:
      - FULL
      - PARTIAL
      - SUBTREE

  reason: string
  requested_at: timestamp
```

---

# 93. Revocation Response

```yaml
revoke_delegation_result:
  state:
    - REVOKED
    - PARTIALLY_REVOKED
    - DENIED
    - BLOCK_AUTHORITY
    - BLOCK_CONFLICT
    - UNKNOWN_GAP

  affected_delegations: []
  invalidated_witnesses: []
  preserved_independent_paths: []
  provenance: {}
```

---

# 94. Control-Plane Requirements

The delegation subsystem SHOULD integrate with:

```text
AUTHORITY_RESOLVER

AUTHORITY_WITNESS

AUTHORIZATION_SPEC

POLICY_ENGINE

POLICY_REGISTRY

CAPABILITY_MANIFEST

CAPABILITY_CONTRACT

CONTROL_PLANE_MAP

IDENTITY / PRINCIPAL REGISTRY

REVOCATION STATE

TRANSACTION CONTROL

PROVENANCE STORE

AUDIT LOG

OBSERVABILITY ENVELOPE

MVCC / VERSION STATE

COMMIT GUARD
```

---

# 95. Control-Plane Ownership

Delegation is infrastructure authority logic.

Domain Skills MAY request or consume delegation.

They MUST NOT own authoritative delegation state unless explicitly designated as an infrastructure authority component.

---

# 96. Commit-Time Delegation Validation

Before a delegation-backed consequential effect commits, the control plane SHOULD validate:

```text
delegation still exists;

delegation still active;

parent authority still valid;

root authority still valid;

delegator authority not revoked;

delegation not expired;

delegation scope still covers action;

constraints still hold;

cumulative limits remain available;

regime remains compatible;

authority witness remains fresh.
```

---

# 97. Delegation Read Set

```yaml
delegation_read_set:
  - object_id: string
    generation: null
    version: string
    content_hash: string
    role:
      - ROOT_AUTHORITY
      - PARENT_AUTHORITY
      - PARENT_DELEGATION
      - POLICY
      - CONSTRAINT
      - REVOCATION
      - BUDGET
      - PRINCIPAL
```

---

# 98. Fine-Grained Invalidation

If:

```text
D1 depends on {R1, P1, C1}
D2 depends on {R2, P2, C2}
```

and:

```text
R1 changes
```

then:

```text
D1 → REVALIDATE
D2 → PRESERVE
```

provided no hidden dependency exists.

---

# 99. MVCC / CAS Boundary

For mutable delegation state, a commit SHOULD fail if load-bearing authority state changed after validation.

Conceptually:

```text
READ authority_version = V1

VALIDATE delegation

CAS authority_version == V1

COMMIT
```

If:

```text
current_version != V1
```

then:

```text
REVALIDATE
```

---

# 100. Atomic Delegation Commit

A delegation commit may require atomic update of:

```text
delegation record;

authority graph;

budget reservation;

revocation index;

provenance ledger;

cache invalidation.
```

Partial update risks phantom authority.

---

# 101. Partial Commit Failure

Example:

```text
delegation record written
BUT
authority graph not updated
```

or:

```text
authority graph updated
BUT
delegation record absent
```

must not be treated as successful delegation.

Recovery requires reconciliation or rollback.

---

# 102. Delegation Invariants

## INV-DEL-001 — No Authority Creation

```text
ChildAuthority ⊆ ParentDelegableAuthority
```

## INV-DEL-002 — Principal Distinction

Delegator and delegate identities MUST remain explicit.

## INV-DEL-003 — Parent Validity

No child delegation may depend on invalid parent authority.

## INV-DEL-004 — Scope Attenuation

```text
ChildScope ⊆ ParentScope
```

## INV-DEL-005 — Operation Attenuation

```text
ChildOperations ⊆ ParentOperations
```

## INV-DEL-006 — Resource Attenuation

```text
ChildResources ⊆ ParentResources
```

## INV-DEL-007 — Effect Attenuation

```text
ChildEffects ⊆ ParentEffects
```

## INV-DEL-008 — Recipient Attenuation

```text
ChildRecipients ⊆ ParentRecipients
```

## INV-DEL-009 — Temporal Attenuation

Child authority cannot outlive parent authority.

## INV-DEL-010 — Constraint Preservation

Mandatory parent constraints MUST survive delegation.

---

# 103. Delegation Invariants — Continued

## INV-DEL-011 — Depth Boundedness

Redelegation cannot exceed permitted depth.

## INV-DEL-012 — Explicit Redelegation

Delegated authority is not redelegable unless explicitly permitted.

## INV-DEL-013 — Revocation Propagation

Dependent child authority cannot survive revocation of its only supporting parent.

## INV-DEL-014 — Independent Path Preservation

Revocation of one path MUST NOT destroy unrelated valid authority.

## INV-DEL-015 — Expiry Propagation

Child authority expires no later than its parent.

## INV-DEL-016 — No Cycle Amplification

Delegation cycles cannot create authority.

## INV-DEL-017 — Provenance Preservation

Root and parent authority lineage MUST remain recoverable.

## INV-DEL-018 — Budget Conservation

Delegation cannot duplicate scarce authority budgets.

## INV-DEL-019 — Role Non-Substitution

Role labels cannot substitute for delegation authority.

## INV-DEL-020 — Capability Non-Substitution

Capability availability cannot substitute for delegation authority.

---

# 104. Delegation Invariants — Governance

## INV-DEL-021

```text
POLICY_ALLOW != AUTHORITY_TO_DELEGATE
```

## INV-DEL-022

```text
TASK_ASSIGNMENT != AUTHORITY_DELEGATION
```

## INV-DEL-023

```text
AGENT_SPAWN != AUTHORITY_DELEGATION
```

## INV-DEL-024

```text
MEMORY != DELEGATION_AUTHORITY
```

## INV-DEL-025

```text
DELEGATION != AUTHORIZATION
```

## INV-DEL-026

```text
DELEGATION != COMMIT
```

## INV-DEL-027

Unknown parent authority MUST fail closed.

## INV-DEL-028

Conflicting authority MUST not be resolved by choosing the more permissive branch.

## INV-DEL-029

Delegation mutation requires revalidation.

## INV-DEL-030

Current revocation state outranks stale cached delegation state.

---

# 105. Delegation Invariants — Transactional

## INV-DEL-031

Delegation creation consuming finite resources requires concurrency-safe accounting.

## INV-DEL-032

Delegation graph and durable delegation record MUST not diverge silently.

## INV-DEL-033

Partial commit MUST NOT produce active authority.

## INV-DEL-034

Commit-time authority freshness MUST be checked for consequential effects.

## INV-DEL-035

Stale authority witness MUST NOT override current delegation revocation.

## INV-DEL-036

Delegation cache MUST be invalidated when load-bearing ancestry changes.

## INV-DEL-037

Semantic authority changes require new version/digest.

## INV-DEL-038

Delegation ancestry MUST remain reconstructable after supersession.

## INV-DEL-039

Authority cannot be laundered through intermediate delegates.

## INV-DEL-040

A delegate cannot widen authority by composing capabilities.

---

# 106. Failure Modes

```text
FM-DEL-001 delegator unresolved

FM-DEL-002 delegate unresolved

FM-DEL-003 parent authority missing

FM-DEL-004 parent authority invalid

FM-DEL-005 parent authority expired

FM-DEL-006 parent authority revoked

FM-DEL-007 parent authority stale

FM-DEL-008 delegation prohibited

FM-DEL-009 requested scope exceeds parent

FM-DEL-010 requested operation exceeds parent

FM-DEL-011 requested resource exceeds parent

FM-DEL-012 requested effect exceeds parent

FM-DEL-013 requested recipient exceeds parent

FM-DEL-014 purpose mismatch

FM-DEL-015 child expiry exceeds parent

FM-DEL-016 redelegation prohibited

FM-DEL-017 depth exhausted

FM-DEL-018 hard constraint weakened

FM-DEL-019 cumulative budget exceeded

FM-DEL-020 concurrent budget double allocation

FM-DEL-021 provenance missing

FM-DEL-022 delegation ancestry broken

FM-DEL-023 delegation cycle

FM-DEL-024 authority laundering

FM-DEL-025 identity substitution

FM-DEL-026 role mistaken for delegation authority

FM-DEL-027 capability mistaken for delegation authority

FM-DEL-028 policy allow mistaken for delegation authority

FM-DEL-029 task assignment mistaken for delegation

FM-DEL-030 agent spawn mistaken for delegation

FM-DEL-031 memory mistaken for delegation authority

FM-DEL-032 stale delegation cache

FM-DEL-033 revoked parent with active child

FM-DEL-034 expired parent with active child

FM-DEL-035 partial revocation not propagated

FM-DEL-036 independent authority wrongly revoked

FM-DEL-037 graph/record divergence

FM-DEL-038 partial commit

FM-DEL-039 stale witness used after revocation

FM-DEL-040 UNKNOWN/GAP treated as valid delegation
```

---

# 107. Adversarial Failure Modes

```text
split one prohibited delegation into many smaller delegations;

delegate to an alias of the same principal to bypass limits;

create cycles to amplify authority;

delegate full budget independently to several agents;

extend child expiry beyond parent expiry;

remove parent constraint in child representation;

rename DELETE as CLEANUP to bypass operation restrictions;

route external disclosure through an internal transformation Skill;

spawn child agent and claim inherited authority;

copy stale authority witness after revocation;

replay delegation in another environment;

replay delegation against another resource;

reuse delegation after regime transition;

construct multiple descendants and claim independent authority;

rewrite delegation metadata without changing digest/version;

remove provenance edge to hide revoked ancestor.
```

---

# 108. Repair / Recovery

```text
DETECT FAILURE
    ↓
FREEZE AFFECTED DELEGATION
    ↓
BLOCK DEPENDENT AUTHORIZATION
    ↓
IDENTIFY FAILED AUTHORITY EDGE
    ↓
INVALIDATE DEPENDENT DESCENDANTS
    ↓
PRESERVE INDEPENDENT AUTHORITY
    ↓
REFRESH MINIMUM REQUIRED STATE
    ↓
REBUILD EFFECTIVE AUTHORITY
    ↓
REVALIDATE
    ↓
RESTORE / SUPERSEDE / REVOKE
```

---

# 109. Broken Ancestry Recovery

If delegation ancestry cannot be proven:

```text
ACTIVE
→ QUARANTINED
```

until the missing lineage is recovered or authority is reissued through a valid path.

Never reconstruct missing authority from assumptions.

---

# 110. Graph Divergence Recovery

If:

```text
record state != graph state
```

then:

```text
QUARANTINE affected authority
```

and reconcile against the authoritative persistence layer.

---

# 111. Budget Recovery

If over-allocation occurs:

```text
STOP new allocations

identify committed reservations

identify uncommitted reservations

preserve valid committed state

invalidate excess uncommitted delegations

recompute remaining capacity

revalidate descendants
```

Do not arbitrarily preserve whichever record is easiest.

---

# 112. Revocation Recovery

If revocation propagation partially fails:

```text
mark affected branch REVALIDATION_REQUIRED

block consequential commits

recompute descendants

invalidate dependent witnesses

refresh authorization state
```

---

# 113. Validators

Minimum validator surface:

```text
validate_delegation_request

validate_delegator

validate_delegate

validate_parent_authority

validate_delegability

validate_authority_subset

validate_scope_attenuation

validate_operation_attenuation

validate_capability_attenuation

validate_resource_attenuation

validate_effect_attenuation

validate_recipient_attenuation

validate_purpose

validate_temporal_attenuation

validate_delegation_depth

validate_redelegation

validate_constraint_inheritance

validate_cumulative_limits

validate_budget_reservation

validate_revocation_state

validate_delegation_ancestry

validate_delegation_graph

validate_no_cycle

validate_provenance

validate_delegation_digest

validate_commit_freshness
```

---

# 114. Minimum Test Suite

```text
T-DEL-001 valid direct delegation

T-DEL-002 missing delegator

T-DEL-003 missing delegate

T-DEL-004 missing parent authority

T-DEL-005 invalid parent authority

T-DEL-006 revoked parent

T-DEL-007 expired parent

T-DEL-008 non-delegable parent

T-DEL-009 exact scope delegation

T-DEL-010 narrower scope delegation

T-DEL-011 wider scope rejection

T-DEL-012 operation subset

T-DEL-013 operation expansion rejection

T-DEL-014 resource subset

T-DEL-015 resource expansion rejection

T-DEL-016 effect subset

T-DEL-017 effect expansion rejection

T-DEL-018 recipient subset

T-DEL-019 recipient expansion rejection

T-DEL-020 purpose-compatible delegation

T-DEL-021 purpose mismatch

T-DEL-022 shorter expiry

T-DEL-023 longer expiry rejection

T-DEL-024 constraint inheritance

T-DEL-025 constraint tightening

T-DEL-026 constraint weakening rejection

T-DEL-027 redelegation permitted

T-DEL-028 redelegation prohibited

T-DEL-029 delegation depth decrement

T-DEL-030 delegation depth exhausted

T-DEL-031 cumulative budget allocation

T-DEL-032 cumulative budget overflow

T-DEL-033 concurrent budget race

T-DEL-034 delegation provenance

T-DEL-035 broken ancestry

T-DEL-036 delegation cycle

T-DEL-037 cycle amplification rejection

T-DEL-038 multi-parent independent authority

T-DEL-039 correlated ancestry detection

T-DEL-040 direct revocation

T-DEL-041 cascading revocation

T-DEL-042 selective revocation

T-DEL-043 independent path preservation

T-DEL-044 partial revocation

T-DEL-045 expiry propagation

T-DEL-046 suspension

T-DEL-047 quarantine

T-DEL-048 stale delegation cache

T-DEL-049 stale witness after revocation

T-DEL-050 delegation/authorization separation

T-DEL-051 delegation/capability separation

T-DEL-052 delegation/policy separation

T-DEL-053 delegation/task assignment separation

T-DEL-054 delegation/agent spawn separation

T-DEL-055 delegation/memory separation

T-DEL-056 identity preservation

T-DEL-057 no impersonation

T-DEL-058 environment binding

T-DEL-059 regime binding

T-DEL-060 emergency delegation boundedness

T-DEL-061 break-glass expiration

T-DEL-062 graph/record consistency

T-DEL-063 partial commit failure

T-DEL-064 MVCC conflict

T-DEL-065 CAS retry/revalidation

T-DEL-066 authority digest mutation

T-DEL-067 parent version mutation

T-DEL-068 selective invalidation

T-DEL-069 transaction-level composition

T-DEL-070 UNKNOWN/GAP fail-closed
```

---

# 115. Falsifiers

A claim that a delegation is valid is falsified by reliable evidence that:

```text
the delegator lacks the delegated authority;

the authority is non-delegable;

the parent authority is revoked;

the parent authority is expired;

the delegate identity does not match;

child scope exceeds parent scope;

child operations exceed parent operations;

child resources exceed parent resources;

child effects exceed parent effects;

child recipients exceed parent recipients;

child validity exceeds parent validity;

mandatory constraints were weakened;

delegation depth was exceeded;

redelegation was prohibited;

cumulative limits were exceeded;

delegation ancestry is invalid;

the delegation record was materially altered without valid supersession;

or the delegation depends solely on an invalid ancestor.
```

---

# 116. Confidence Ceiling

AMOS MODEL:

```text
C_delegation
≤
min(
    C_delegator_identity,
    C_delegate_identity,
    C_parent_authority,
    C_delegability,
    C_scope,
    C_operations,
    C_resources,
    C_effects,
    C_constraints,
    C_temporal,
    C_depth,
    C_revocation,
    C_provenance,
    C_freshness
)
```

Derived confidence cannot exceed the weakest load-bearing premise.

---

# 117. Uncertainty Vector

```yaml
delegation_uncertainty:
  delegator_identity: null
  delegate_identity: null
  parent_authority: null
  delegability: null
  scope: null
  operation: null
  resource: null
  effect: null
  recipient: null
  purpose: null
  temporal: null
  depth: null
  constraints: null
  cumulative_limits: null
  revocation: null
  graph_consistency: null
  provenance: null
  independence: null
  freshness: null
```

---

# 118. RSCF Capsule

```yaml
rscf:
  claim:
    id: "AMOS_DELEGATION_ARCHITECTURE"
    class: MODEL

    text: >
      AMOS delegation transfers only a bounded,
      provenance-preserving, attenuated subset of
      authority already held and delegable by a
      principal; delegation cannot create authority,
      erase parent constraints, exceed parent scope,
      or substitute for authorization.

  premises:
    - delegator_identity_valid
    - delegate_identity_valid
    - parent_authority_valid
    - authority_is_delegable
    - child_authority_is_subset
    - constraints_preserved
    - temporal_bounds_valid
    - delegation_depth_valid
    - revocation_state_current
    - provenance_valid

  provenance:
    origin_architect: "Trang Phan"
    steward: "Trang Phan"

  scope:
    system: "AMOS OS"
    component: "Authority Delegation"

  regime:
    - DESIGN
    - ARCHITECTURE
    - GOVERNANCE_MODEL

  dependencies:
    - AUTHORITY_RESOLVER.md
    - AUTHORITY_WITNESS.md
    - AUTHORIZATION_SPEC.md
    - POLICY_ENGINE.md
    - POLICY_REGISTRY.md
    - CAPABILITY_CONTRACT.md
    - CAPABILITY_MANIFEST.md
    - CONTROL_PLANE_MAP.md

  competing:
    - capability-based implicit delegation
    - role-based implicit delegation
    - workflow-task implicit delegation
    - unbounded inherited-agent authority

  falsifiers:
    - child authority exceeds parent
    - non-delegable authority is delegated
    - revoked parent leaves dependent child valid
    - expired parent leaves dependent child valid
    - constraints disappear during delegation
    - delegation cycle creates new authority
    - task assignment alone creates authority

  confidence_ceiling: 0
```

---

# 119. GMEF Change Governance

Changes affecting any of the following SHOULD undergo governed review:

```text
delegability rules;

attenuation semantics;

scope composition;

constraint inheritance;

delegation depth;

redelegation;

revocation propagation;

budget accounting;

authority graph semantics;

provenance requirements;

commit-time freshness;

emergency delegation;

or break-glass authority.
```

---

# 120. Change Manifest

```yaml
delegation_change:
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
  affected_delegations: []
  affected_authority_paths: []

  migration_requirements: []
  validation_requirements: []

  rollback_plan: null

  approval_state: PROPOSED
```

---

# 121. Promotion Model

```text
STRUCTURAL_MODEL
      ↓
SCHEMA_VALIDATED
      ↓
AUTHORITY_GRAPH_IMPLEMENTED
      ↓
DELEGATION_ENGINE_IMPLEMENTED
      ↓
REVOCATION_IMPLEMENTED
      ↓
PROVENANCE_IMPLEMENTED
      ↓
CONCURRENCY_CONTROL_IMPLEMENTED
      ↓
AUTHORITY_RESOLVER_INTEGRATED
      ↓
AUTHORIZATION_INTEGRATED
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

# 122. Implementation Requirements

An executable delegation implementation SHOULD provide:

```text
typed delegation requests;

typed delegation records;

typed revocation records;

principal resolution;

parent-authority validation;

delegability validation;

scope attenuation;

operation attenuation;

resource attenuation;

effect attenuation;

recipient attenuation;

purpose validation;

temporal attenuation;

constraint inheritance;

delegation-depth accounting;

redelegation controls;

cumulative-limit accounting;

atomic reservation;

delegation graph maintenance;

cycle detection;

ancestry reconstruction;

revocation propagation;

selective invalidation;

MVCC/CAS or equivalent freshness control;

provenance logging;

audit reconstruction;

authority-witness invalidation.
```

This specification does not claim these mechanisms are currently implemented.

---

# 123. Example — Narrow Delegation

Parent:

```yaml
authority:
  operations:
    - READ
    - UPDATE

  resources:
    - PROJECT_A

  valid_until: "2026-09-01T00:00:00Z"
```

Requested child:

```yaml
authority:
  operations:
    - READ

  resources:
    - PROJECT_A/REPORTS

  valid_until: "2026-08-30T00:00:00Z"
```

Result:

```text
ALLOW
```

subject to remaining authority conditions.

---

# 124. Example — Scope Expansion

Parent:

```text
PROJECT_A
```

Requested:

```text
PROJECT_A
+
PROJECT_B
```

Result:

```text
BLOCK_SCOPE
```

unless independent authority covers `PROJECT_B`.

---

# 125. Example — Operation Expansion

Parent:

```text
READ
```

Requested:

```text
READ
+
DELETE
```

Effective delegation may be:

```text
ALLOW_ATTENUATED:
READ
```

while:

```text
DELETE
```

is rejected.

---

# 126. Example — Expiry Expansion

Parent expires:

```text
2026-09-01
```

Requested child expiry:

```text
2026-12-01
```

Effective child expiry cannot exceed:

```text
2026-09-01
```

---

# 127. Example — Non-Delegable Authority

```yaml
parent_authority:
  operations:
    - COMMIT

  delegation_policy:
    delegable: false
```

Request:

```text
delegate COMMIT to Agent-B
```

Result:

```text
DENY
```

---

# 128. Example — Redelegation

```text
ROOT
 ↓
A
 ↓
B
```

If A receives:

```yaml
redelegation:
  allowed: false
```

then:

```text
A → B
```

is invalid regardless of whether A may exercise the underlying operation itself.

---

# 129. Example — Revocation Cascade

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

Result:

```text
D1 = REVOKED
D2 = INVALID_DEPENDENT
```

unless B has an independent valid authority path.

---

# 130. Example — Independent Authority

```text
ROOT_A → D1 → P

ROOT_B → D2 → P
```

If:

```text
D1 revoked
```

then:

```text
D2
```

remains independently evaluable.

The resolver MUST recompute effective authority rather than automatically removing all P authority.

---

# 131. Example — Budget Duplication

Parent:

```text
delegatable spend = 100
```

Requests:

```text
A = 80
B = 80
```

Correct behavior:

```text
one or both requests must be attenuated/blocked
```

according to reservation ordering and policy.

Never:

```text
A = 80
B = 80
total delegated = 160
```

against a conserved 100 budget.

---

# 132. Example — Task Assignment

Instruction:

```text
"Agent B, analyze the report."
```

This may create workflow responsibility.

It does not automatically grant:

```text
READ all confidential drives

SEND external email

DELETE source records

CHANGE policy
```

Authority must be resolved independently.

---

# 133. Example — Child Agent

```text
Agent A
spawns
Agent B
```

Result:

```text
Agent B authority = NONE
```

unless authority is explicitly delegated or independently granted.

---

# 134. Example — Role Change

```text
role:
ANALYST → ADMIN
```

does not itself create authority unless the authoritative role-to-authority mapping validates the change and the actor had authority to make it.

---

# 135. Example — Capability Routing

Suppose Agent A has:

```text
READ authority
```

but discovers a capability exposing:

```text
READ
WRITE
DELETE
```

Delegation remains:

```text
READ
```

Capability breadth cannot widen delegated authority.

---

# 136. Example — Cross-Skill Composition

Delegated authority:

```text
READ internal document
```

Skill chain:

```text
READ
→ SUMMARIZE
→ SEND EXTERNALLY
```

The original delegation does not automatically authorize the final disclosure.

A separate disclosure authorization is required.

---

# 137. Example — Emergency Delegation

```yaml
delegation:
  purpose: INCIDENT_RESPONSE

  operations:
    - READ_LOGS

  resources:
    - INCIDENT_SYSTEM_A

  valid_from: "2026-08-26T07:00:00Z"
  valid_until: "2026-08-26T09:00:00Z"

  redelegation:
    allowed: false
```

This authority terminates when its temporal or incident-regime conditions fail.

---

# 138. Example — Stale Witness

```text
T0 delegation active
T1 witness generated
T2 delegation revoked
T3 witness presented
```

Result:

```text
WITNESS STALE
→ BLOCK_AUTHORITY
```

not:

```text
ALLOW because witness once validated
```

---

# 139. Delegation Decision Matrix

| Parent Authority | Delegable | Child ⊆ Parent | Constraints | Depth     | Result           |
| ---------------- | --------- | -------------- | ----------- | --------- | ---------------- |
| Valid            | Yes       | Yes            | Valid       | Valid     | ALLOW            |
| Valid            | Yes       | Partial        | Valid       | Valid     | ALLOW_ATTENUATED |
| Valid            | No        | Yes            | Valid       | Valid     | DENY             |
| Invalid          | Yes       | Yes            | Valid       | Valid     | BLOCK_AUTHORITY  |
| Revoked          | Yes       | Yes            | Valid       | Valid     | BLOCK_AUTHORITY  |
| Valid            | Yes       | No             | Valid       | Valid     | BLOCK_SCOPE      |
| Valid            | Yes       | Yes            | Invalid     | Valid     | BLOCK_CONSTRAINT |
| Valid            | Yes       | Yes            | Valid       | Exhausted | BLOCK_DEPTH      |
| Conflict         | Unknown   | Unknown        | Unknown     | Unknown   | BLOCK_CONFLICT   |
| Unknown          | Unknown   | Unknown        | Unknown     | Unknown   | UNKNOWN_GAP      |

---

# 140. Revocation Matrix

| Parent   | Child   | Independent Path | Effective Child State |
| -------- | ------- | ---------------- | --------------------- |
| Active   | Active  | No               | ACTIVE                |
| Revoked  | Active  | No               | INVALID               |
| Expired  | Active  | No               | INVALID               |
| Revoked  | Active  | Yes              | RE-RESOLVE            |
| Active   | Revoked | No               | REVOKED               |
| Active   | Expired | No               | EXPIRED               |
| Conflict | Active  | Unknown          | BLOCK_CONFLICT        |
| Unknown  | Active  | Unknown          | UNKNOWN_GAP           |

---

# 141. Audit Questions

A delegation audit SHOULD answer:

1. Who is the delegator?
2. Who is the delegate?
3. What root authority supports the delegation?
4. What parent authority supports it?
5. Was the parent authority current?
6. Was it delegable?
7. What exact authority was requested?
8. What authority was actually granted?
9. What permissions were attenuated?
10. What scope applies?
11. What operations apply?
12. What resources apply?
13. What effects apply?
14. What recipients apply?
15. What purposes apply?
16. What constraints were inherited?
17. What constraints were added?
18. What cumulative limits apply?
19. What is the expiry?
20. What is the remaining delegation depth?
21. Is redelegation allowed?
22. Who may revoke?
23. Has any ancestor been revoked?
24. Is the delegation graph acyclic?
25. Does the record match the graph?
26. Are there independent authority paths?
27. What provenance supports the authority?
28. Which versions/hashes were validated?
29. What changed since validation?
30. Is commit-time revalidation required?

---

# 142. Completion Matrix

| Surface                       | Specification State |
| ----------------------------- | ------------------- |
| Definition                    | COMPLETE_AS_MODEL   |
| Scope                         | COMPLETE_AS_MODEL   |
| Delegator                     | COMPLETE_AS_MODEL   |
| Delegate                      | COMPLETE_AS_MODEL   |
| Parent authority              | COMPLETE_AS_MODEL   |
| Delegability                  | COMPLETE_AS_MODEL   |
| Delegation request            | COMPLETE_AS_MODEL   |
| Delegation decision           | COMPLETE_AS_MODEL   |
| Delegation record             | COMPLETE_AS_MODEL   |
| Authority attenuation         | COMPLETE_AS_MODEL   |
| Scope attenuation             | COMPLETE_AS_MODEL   |
| Operation attenuation         | COMPLETE_AS_MODEL   |
| Capability attenuation        | COMPLETE_AS_MODEL   |
| Resource attenuation          | COMPLETE_AS_MODEL   |
| Effect attenuation            | COMPLETE_AS_MODEL   |
| Recipient attenuation         | COMPLETE_AS_MODEL   |
| Purpose binding               | COMPLETE_AS_MODEL   |
| Temporal attenuation          | COMPLETE_AS_MODEL   |
| Delegation depth              | COMPLETE_AS_MODEL   |
| Redelegation                  | COMPLETE_AS_MODEL   |
| Constraint inheritance        | COMPLETE_AS_MODEL   |
| Cumulative limits             | COMPLETE_AS_MODEL   |
| Concurrency                   | COMPLETE_AS_MODEL   |
| Provenance                    | COMPLETE_AS_MODEL   |
| Revocation                    | COMPLETE_AS_MODEL   |
| Selective invalidation        | COMPLETE_AS_MODEL   |
| Expiration                    | COMPLETE_AS_MODEL   |
| Suspension                    | COMPLETE_AS_MODEL   |
| Conflict handling             | COMPLETE_AS_MODEL   |
| Agent boundary                | COMPLETE_AS_MODEL   |
| Skill boundary                | COMPLETE_AS_MODEL   |
| H/M/L                         | COMPLETE_AS_MODEL   |
| Authority graph               | COMPLETE_AS_MODEL   |
| Authority witness integration | COMPLETE_AS_MODEL   |
| Workflows                     | COMPLETE_AS_MODEL   |
| Protocols                     | COMPLETE_AS_MODEL   |
| MVCC/CAS model                | COMPLETE_AS_MODEL   |
| Invariants                    | COMPLETE_AS_MODEL   |
| Failure modes                 | COMPLETE_AS_MODEL   |
| Recovery                      | COMPLETE_AS_MODEL   |
| Validators                    | COMPLETE_AS_MODEL   |
| Tests                         | COMPLETE_AS_MODEL   |
| Falsifiers                    | COMPLETE_AS_MODEL   |
| RSCF                          | COMPLETE_AS_MODEL   |
| GMEF                          | COMPLETE_AS_MODEL   |
| Executable delegation engine  | UNKNOWN/GAP         |
| Executed test evidence        | UNKNOWN/GAP         |
| Production validation         | UNKNOWN/GAP         |
| Formal verification           | UNKNOWN/GAP         |
| Canon admission               | UNKNOWN/GAP         |

---

# 143. Hard Boundary Block

```text
AUTHORITY != DELEGATION

DELEGATION != AUTHORIZATION

DELEGATION != AUTHENTICATION

DELEGATION != CAPABILITY

DELEGATION != ROLE

DELEGATION != IMPERSONATION

DELEGATION != OWNERSHIP

DELEGATION != TASK_ASSIGNMENT

DELEGATION != AGENT_SPAWN

DELEGATION != EXECUTION

DELEGATION != COMMIT

DELEGATOR_AUTHORITY != DELEGATE_IDENTITY

DELEGATED_AUTHORITY <= DELEGATOR_DELEGABLE_AUTHORITY

CHILD_SCOPE ⊆ PARENT_SCOPE

CHILD_OPERATIONS ⊆ PARENT_OPERATIONS

CHILD_RESOURCES ⊆ PARENT_RESOURCES

CHILD_EFFECTS ⊆ PARENT_EFFECTS

CHILD_RECIPIENTS ⊆ PARENT_RECIPIENTS

CHILD_EXPIRY <= PARENT_EXPIRY

CHILD_CONSTRAINTS CANNOT WEAKEN MANDATORY PARENT CONSTRAINTS

REDELEGATION != IMPLIED

POLICY_ALLOW != AUTHORITY_TO_DELEGATE

CAPABILITY_AVAILABLE != AUTHORITY_TO_DELEGATE

ROLE_ASSIGNMENT != AUTHORITY_TO_DELEGATE

MEMORY != AUTHORITY_TO_DELEGATE

SPAWNED_AGENT != AUTHORIZED_AGENT

REVOKED_PARENT != VALID_DEPENDENT_CHILD

EXPIRED_PARENT != VALID_DEPENDENT_CHILD

INVALID_PARENT != VALID_DEPENDENT_CHILD

UNKNOWN_PARENT != VALID_DEPENDENT_CHILD

DELEGATION_CYCLE != AUTHORITY_CREATION

MULTIPLE_DESCENDANTS != MULTIPLE_INDEPENDENT_ROOTS

LOCAL_AUTHORITY != GLOBAL_TRANSACTION_AUTHORITY

PROPOSAL != COMMIT

UNKNOWN/GAP != VALID

STRUCTURAL_MODEL != IMPLEMENTED_RUNTIME

IMPLEMENTED != VALIDATED

TESTED != FORMALLY_VERIFIED

MODEL != EMPIRICAL_FACT
```

---

# 144. Canon Boundary

Trang Phan remains the origin architect and steward of AMOS.

This artifact specifies a proposed complete structural delegation model.

It does not establish that AMOS currently possesses:

```text
an executable delegation engine;

a production authority graph;

an operational revocation registry;

atomic delegation transactions;

MVCC/CAS enforcement;

distributed authority finality;

production identity integration;

executed adversarial tests;

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

# 145. Final Delegation Contract

AMOS SHALL preserve:

```text
ROOT AUTHORITY
      ↓
CURRENT PARENT AUTHORITY
      ↓
DELEGABILITY
      ↓
DELEGATOR
      ↓
DELEGATION REQUEST
      ↓
ATTENUATION
      ↓
SCOPE / OPERATIONS / RESOURCES
      ↓
EFFECTS / RECIPIENTS / PURPOSE
      ↓
CONSTRAINT INHERITANCE
      ↓
TEMPORAL BOUND
      ↓
DELEGATION DEPTH
      ↓
CUMULATIVE LIMITS
      ↓
REVOCATION SEMANTICS
      ↓
PROVENANCE
      ↓
DELEGATION RECORD
      ↓
AUTHORITY GRAPH
      ↓
AUTHORITY RESOLUTION
      ↓
AUTHORITY WITNESS
      ↓
AUTHORIZATION
      ↓
COMMIT-TIME REVALIDATION
```

The central invariant is:

> **Delegation may transmit only authority that the delegator currently holds and is permitted to delegate, and the delegated authority must remain no broader than the supporting authority across every load-bearing dimension.**

Therefore:

```text
PARENT AUTHORITY = READ + UPDATE
```

cannot yield:

```text
CHILD AUTHORITY = READ + UPDATE + DELETE
```

and:

```text
PARENT SCOPE = PROJECT_A
```

cannot yield:

```text
CHILD SCOPE = PROJECT_A + PROJECT_B
```

and:

```text
PARENT EXPIRY = T1
```

cannot yield:

```text
CHILD EXPIRY > T1
```

and:

```text
PARENT REVOKED
```

means:

```text
DEPENDENT CHILD AUTHORITY INVALID
```

unless an independently valid authority path exists.

AMOS MUST NOT manufacture authority through delegation chains, cycles, aliases, roles, memory, capability routing, Skill composition, agent spawning, or repeated descendants of one authority root.

AMOS MUST preserve delegation ancestry.

AMOS MUST preserve mandatory parent constraints.

AMOS MUST bound redelegation depth.

AMOS SHOULD prevent cumulative authority-budget duplication through atomic reservation or equivalent concurrency-safe control.

AMOS SHOULD selectively invalidate only authority dependent on a changed or revoked edge.

AMOS MUST revalidate delegation-backed authority at consequential commit boundaries when load-bearing authority state is mutable.

When authority ancestry, scope, delegability, revocation, or another load-bearing premise cannot be established, the correct state is:

```text
UNKNOWN_GAP
```

not permissive inference.

Integrity remains prior to completeness, fluency, convenience, speed, or optimization.

---

# END — DELEGATION.md

```
```

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]
