---
tags: ['control_plane', 'authority', 'note']
---

# AUTHORITY_RESOLVER.md

---
title: "AMOS Authority Resolver"
artifact: "AUTHORITY_RESOLVER.md"
origin_architect: "Trang Phan"
steward: "Trang Phan"
system: "AMOS OS"
artifact_class: "GOVERNED_AUTHORITY_RESOLUTION_CONTROL_COMPONENT"
status: "PROPOSED / STRUCTURALLY_COMPLETE / IMPLEMENTATION-UNVALIDATED"
epistemic_class: "MODEL"
version: "1.0.0"
updated: "2026-08-26"
default_authority: "NONE"
default_resolution: "UNRESOLVED"
---

# AMOS Authority Resolver

## 0. Status

`AUTHORITY_RESOLVER.md` defines the AMOS OS contract for determining whether a principal possesses valid, current, sufficiently scoped authority for a proposed operation.

The Authority Resolver answers:

> **Does this principal possess a valid authority basis for this exact operation, capability, target, effect, scope, regime, and time—and what evidence establishes that authority?**

It does not create authority.

It does not grant authority.

It does not execute capabilities.

It does not make policy by itself.

It does not commit effects.

It does not infer authority merely because an operation is technically possible.

The central distinction is:

```text
IDENTITY
    ↓
AUTHORITY CANDIDATES
    ↓
AUTHORITY VALIDATION
    ↓
SCOPE / CONSTRAINT RESOLUTION
    ↓
FRESHNESS / REVOCATION CHECK
    ↓
AUTHORITY RESOLUTION
```

never:

```text
CAPABILITY
    ↓
AUTHORITY
```

---

# 1. Purpose

The Authority Resolver exists to prevent AMOS from confusing:

```text
identity;
authentication;
role;
capability;
policy permission;
technical access;
tool availability;
historical permission;
agent confidence;
or successful execution
```

with actual authority.

Its purpose is to transform potentially fragmented authority evidence into a typed resolution result suitable for downstream governance.

Canonical flow:

```text
PRINCIPAL
    +
PROPOSED OPERATION
    +
TARGET
    +
CAPABILITY
    +
EFFECT
    +
CONTEXT
    +
AUTHORITY EVIDENCE
        ↓
AUTHORITY RESOLVER
        ↓
RESOLVED AUTHORITY CONTRACT
        ↓
POLICY / CONTROL-PLANE VALIDATION
        ↓
COMMIT-TIME REVALIDATION
```

---

# 2. Core Laws

```text
IDENTITY != AUTHORITY

AUTHENTICATION != AUTHORITY

ROLE != AUTHORITY

CAPABILITY != AUTHORITY

ACCESS != AUTHORITY

POLICY_ALLOW != AUTHORITY

TOOL_AVAILABLE != AUTHORITY

SKILL_AVAILABLE != AUTHORITY

AGENT_ROLE != AUTHORITY

PRIOR_AUTHORITY != CURRENT_AUTHORITY

AUTHORITY_CANDIDATE != RESOLVED_AUTHORITY

AUTHORITY_REFERENCE != VALID_AUTHORITY

AUTHORITY_SIGNATURE != CURRENT_AUTHORITY

AUTHORITY_TO_PROPOSE != AUTHORITY_TO_EXECUTE

AUTHORITY_TO_EXECUTE != AUTHORITY_TO_COMMIT

AUTHORITY_TO_READ != AUTHORITY_TO_WRITE

AUTHORITY_TO_WRITE != AUTHORITY_TO_DELETE

AUTHORITY_TO_CREATE != AUTHORITY_TO_SHARE

AUTHORITY_TO_MUTATE != AUTHORITY_TO_PROMOTE

AUTHORITY_TO_PROMOTE != AUTHORITY_TO_RELEASE

AUTHORITY_AT_PLAN_TIME != AUTHORITY_AT_COMMIT_TIME

DELEGATED_AUTHORITY <= DELEGATING_AUTHORITY

DERIVED_AUTHORITY <= LOAD_BEARING_AUTHORITY

UNKNOWN/GAP != AUTHORIZED

CONFLICT != AUTHORIZED

EXPIRED != AUTHORIZED

REVOKED != AUTHORIZED

PROPOSAL != COMMIT
```

---

# 3. Architectural Position

```text
IDENTITY / PRINCIPAL REGISTRY
            ↓
AUTHORITY SOURCES
            ↓
AUTHORITY REGISTRY
            ↓
AUTHORITY RESOLVER
            ↓
RESOLVED AUTHORITY CONTRACT
            ↓
POLICY ENGINE
            ↓
POLICY DECISION
            ↓
CONTROL PLANE
            ↓
COMMIT-TIME AUTHORITY REVALIDATION
            ↓
EFFECT RELEASE
```

The Authority Resolver is an infrastructure governance component.

It sits between raw authority evidence and effectful execution.

---

# 4. Responsibilities

The Authority Resolver owns the resolution of:

```text
principal identity binding;

authority candidate discovery;

issuer identity;

authority type;

delegation lineage;

authority scope;

operation scope;

capability scope;

resource scope;

effect scope;

recipient scope;

environment scope;

jurisdiction scope;

temporal validity;

regime validity;

constraints;

cumulative limits;

delegation restrictions;

revocation state;

supersession state;

authority freshness;

authority conflicts;

authority provenance;

resolution evidence;

confidence ceiling;

unresolved authority gaps.
```

It does NOT own:

```text
credential issuance;

authentication;

policy authorship;

policy registration;

capability implementation;

capability execution;

resource mutation;

effect dispatch;

durable commit;

receiver receipt verification;

release-ledger finality;

domain-specific business logic.
```

---

# 5. Authority Resolution Function

Conceptually:

```text
ResolveAuthority(
    principal,
    operation,
    capability,
    target,
    effect,
    recipient,
    environment,
    jurisdiction,
    scope,
    regime,
    time,
    authority_candidates
)
→ AuthorityResolution
```

The resolver MUST evaluate authority against the requested operation, not merely against the principal.

---

# 6. Authority Request

```yaml
authority_resolution_request:
  request_id: string

  principal:
    principal_id: string
    principal_type:
      - HUMAN
      - AGENT
      - SERVICE
      - ORGANIZATION
      - SYSTEM

    authenticated_identity_ref: null

  operation:
    operation_id: string
    operation_class: string

  capability:
    capability_id: null
    capability_version: null

  target:
    resource_id: null
    resource_class: null
    owner: null

  effect:
    effect_class:
      - READ_ONLY
      - REVERSIBLE
      - MUTATING
      - DURABLE
      - EXTERNAL
      - IRREVERSIBLE
      - MODEL_PROMOTION

  recipient:
    recipient_id: null
    recipient_class: null

  environment:
    environment_id: null
    environment_class: null

  jurisdiction:
    jurisdiction_id: null

  scope: {}

  regime: {}

  requested_at: timestamp

  authority_candidates: []

  policy_context: {}

  provenance: {}
```

---

# 7. Authority Resolution Result

```yaml
authority_resolution:
  resolution_id: string
  request_id: string

  state:
    - AUTHORIZED
    - AUTHORIZED_CONDITIONAL
    - DENIED
    - EXPIRED
    - REVOKED
    - CONFLICT
    - REVALIDATE
    - ESCALATE
    - UNKNOWN_GAP

  principal_id: string

  operation_id: string

  authority_id: null

  authority_version: null

  authority_digest: null

  issuer: null

  authority_class: null

  effective_scope: {}

  effective_constraints: []

  delegation_lineage: []

  temporal:
    valid_from: null
    valid_until: null
    evaluated_at: timestamp

  regime: {}

  dependencies: []

  policy_refs: []

  evidence_refs: []

  provenance: {}

  falsifiers: []

  confidence_ceiling: null

  commit_revalidation_required: true
```

---

# 8. Resolution States

## AUTHORIZED

Authority has been resolved for the exact requested operation within the declared scope and current evaluation context.

It does NOT mean the operation has been committed.

## AUTHORIZED_CONDITIONAL

Authority exists only if explicit unresolved conditions are discharged before execution or commit.

## DENIED

Available authority evidence establishes that the requested operation is outside permitted authority.

## EXPIRED

The relevant authority existed but is outside its valid temporal envelope.

## REVOKED

The authority has been authoritatively withdrawn.

## CONFLICT

Material authority sources disagree in a way that prevents safe resolution.

## REVALIDATE

Authority may have been valid, but one or more freshness-sensitive premises must be checked again.

## ESCALATE

Resolution requires a higher authority or governance process.

## UNKNOWN_GAP

Evidence is insufficient to establish authority.

---

# 9. Fail-Closed Rule

For effectful operations:

```text
UNKNOWN/GAP
CONFLICT
EXPIRED
REVOKED
```

MUST NOT silently become:

```text
AUTHORIZED
```

Recommended governing rule:

```text
IF authority cannot be established
THEN do not perform authority-dependent effect.
```

---

# 10. Authority Object

```yaml
authority_object:
  authority_id: string

  authority_version: string

  authority_digest: string

  authority_class:
    - DIRECT
    - DELEGATED
    - ROLE_BOUND
    - RESOURCE_BOUND
    - CAPABILITY_BOUND
    - OPERATION_BOUND
    - TEMPORARY
    - EMERGENCY
    - TRANSACTION_BOUND
    - EFFECT_BOUND

  issuer:
    issuer_id: string
    issuer_type: string
    issuer_authority_ref: null

  subject:
    principal_id: string
    principal_type: string

  permissions:
    operations: []
    capabilities: []
    resources: []
    resource_classes: []
    effect_classes: []
    recipients: []
    environments: []
    jurisdictions: []

  constraints: []

  delegation:
    delegable: false
    max_depth: 0
    allowed_delegate_classes: []
    attenuation_required: true

  temporal:
    issued_at: timestamp
    valid_from: timestamp
    valid_until: timestamp
    revoked_at: null

  regime:
    allowed: []
    excluded: []

  cumulative_limits: {}

  provenance: {}

  signatures: []

  status:
    - ACTIVE
    - EXPIRED
    - REVOKED
    - SUSPENDED
    - QUARANTINED
```

---

# 11. Authority Identity

Material authority SHOULD bind:

```text
AuthorityIdentity =
(
    authority_id,
    authority_version,
    authority_digest
)
```

A textual authority ID alone is insufficient where authority state is mutable or versioned.

---

# 12. Authority Digest

Conceptually:

```text
authority_digest =
H(
    issuer
    + subject
    + permissions
    + constraints
    + delegation
    + temporal envelope
    + regime
    + cumulative limits
)
```

Exact serialization and cryptographic algorithms belong to implementation specifications.

---

# 13. Principal Binding

Authority MUST bind to the actual principal requesting the action.

```text
Authority.subject
=
Request.principal
```

or a validated delegation/impersonation mechanism MUST explain the difference.

---

# 14. Principal Invariant

```text
similar name
!=
same principal
```

and:

```text
same role
!=
same principal
```

and:

```text
same agent class
!=
same authority
```

---

# 15. Authentication Boundary

Authentication answers:

> Who is this principal?

Authority answers:

> What may this principal do?

Therefore:

```text
AUTHENTICATED
↛
AUTHORIZED
```

Authentication may be necessary but is not sufficient.

---

# 16. Authority Sources

Potential authority sources MAY include:

```text
explicit user authorization;

organizational delegation;

service-account grants;

resource ownership;

capability-specific grants;

transaction-specific authority;

system governance rules;

temporary operational authority;

emergency authority;

signed delegation objects;

external platform authorization.
```

Their existence does not automatically establish applicability.

---

# 17. Authority Candidate

```yaml
authority_candidate:
  authority_id: string
  authority_version: string
  authority_digest: string

  source_ref: string

  issuer: string

  subject: string

  authority_class: string

  status: string

  scope: {}

  temporal: {}

  regime: {}

  provenance: {}
```

---

# 18. Candidate Discovery

Authority candidates MAY be discovered by:

```text
principal;
operation;
capability;
resource;
effect;
recipient;
environment;
jurisdiction;
transaction;
delegation lineage.
```

Discovery produces candidates only.

```text
DISCOVERED_AUTHORITY
!=
VALID_AUTHORITY
```

---

# 19. Authority Applicability

For candidate authority `A` and request `R`:

```text
Applicable(A,R)
=
PrincipalMatch
∧ OperationMatch
∧ CapabilityMatch
∧ ResourceMatch
∧ EffectMatch
∧ RecipientMatch
∧ EnvironmentMatch
∧ JurisdictionMatch
∧ ScopeMatch
∧ RegimeMatch
∧ TemporalValid
∧ NotRevoked
∧ ConstraintSatisfied
```

This is an AMOS MODEL expression.

Implementations may represent the predicate differently.

---

# 20. Scope Resolution

Authority SHOULD be resolved across typed dimensions.

```yaml
authority_scope:
  principal: []

  operations: []

  capabilities: []

  resources: []

  resource_classes: []

  effects: []

  recipients: []

  environments: []

  jurisdictions: []

  transactions: []

  hml:
    H: null
    M: null
    L: null
```

---

# 21. Scope Containment

Required:

```text
RequestedScope
⊆
AuthorizedScope
```

If not:

```text
DENIED
```

or:

```text
ESCALATE
```

depending on governance.

---

# 22. Unknown Scope

Unknown authority scope MUST NOT become universal authority.

```text
scope = UNKNOWN
```

means:

```text
UNKNOWN/GAP
```

not:

```text
GLOBAL
```

---

# 23. Operation Binding

Authority SHOULD name or structurally bind the allowed operation class.

Examples:

```text
READ

CREATE

UPDATE

DELETE

MOVE

SHARE

SEND

EXECUTE

PROMOTE

PUBLISH

COMMIT

REVOKE

ADMINISTER
```

---

# 24. Operation Non-Equivalence

```text
READ != WRITE

WRITE != DELETE

CREATE != SHARE

EXECUTE != COMMIT

COMMIT != RELEASE

RELEASE != ADMINISTER
```

Authority for one MUST NOT silently imply another.

---

# 25. Capability Binding

An authority MAY constrain which capability may exercise it.

Example:

```yaml
capability_binding:
  capability_id: "CAP_RESOURCE_WRITE"
  version_constraint: ">=1.0 <2.0"
```

This prevents generic authority from being silently exercised through an incompatible capability.

---

# 26. Capability Boundary

```text
CAPABILITY_AVAILABLE
```

means:

> The system may know how to perform an operation.

It does NOT mean:

> The principal may perform it.

Therefore:

```text
Capability(R)
∧ ¬Authority(R)
→ NO_EFFECT
```

---

# 27. Resource Binding

Authority SHOULD bind resources sufficiently to prevent scope substitution.

Examples:

```text
specific resource ID;

folder/subtree;

resource class;

namespace;

tenant;

project;

organization.
```

---

# 28. Resource Ownership

Ownership MAY contribute to authority where governance explicitly recognizes ownership.

But:

```text
OWNER
```

must not automatically imply:

```text
UNLIMITED_AUTHORITY
```

because external policies, organizational controls, privacy rules, or platform constraints may still apply.

---

# 29. Effect Binding

Authority SHOULD distinguish effect classes.

```text
READ_ONLY

REVERSIBLE

MUTATING

DURABLE

EXTERNAL

IRREVERSIBLE

MODEL_PROMOTION
```

Higher-consequence effects SHOULD require stronger authority evidence.

---

# 30. Effect Escalation

Conceptually:

```text
AuthorityRequirement
↑
as
Irreversibility
+
Externality
+
Persistence
+
Consequence
↑
```

This is a governance model, not an empirical law.

---

# 31. Recipient Binding

For disclosure or transfer operations, authority SHOULD bind allowed recipients.

```yaml
recipient_scope:
  recipient_ids: []
  recipient_classes: []
  domains: []
  organizations: []
```

Authority to access information does not necessarily imply authority to disclose it.

---

# 32. Disclosure Boundary

```text
CAN_READ
!=
CAN_DISCLOSE
```

and:

```text
CAN_DISCLOSE_TO_A
!=
CAN_DISCLOSE_TO_B
```

---

# 33. Environment Binding

Authority MAY differ across:

```text
DEVELOPMENT

TEST

STAGING

PRODUCTION

SANDBOX

INCIDENT

RECOVERY
```

---

# 34. Environment Invariant

```text
AUTHORIZED(TEST)
↛
AUTHORIZED(PRODUCTION)
```

unless explicitly granted.

---

# 35. Jurisdiction Binding

Authority MAY depend on jurisdiction.

The resolver SHOULD preserve jurisdictional scope where relevant.

Unknown jurisdiction must not silently become unrestricted jurisdiction.

---

# 36. Temporal Validity

Every time-bounded authority SHOULD expose:

```text
valid_from

valid_until

revoked_at
```

Resolution time MUST fall inside the valid interval.

Conceptually:

```text
valid_from
≤
evaluation_time
<
valid_until
```

where `valid_until` exists.

---

# 37. Trusted Time

When authority validity depends materially on time, evaluation SHOULD use an infrastructure-trusted time source.

A principal's self-asserted timestamp is insufficient for high-consequence authority validation.

---

# 38. Expiry

If:

```text
evaluation_time >= valid_until
```

then:

```text
EXPIRED
```

unless a valid successor authority independently applies.

---

# 39. Revocation

If authoritative revocation establishes:

```text
revoked_at <= evaluation_time
```

the authority MUST NOT be treated as current.

Result:

```text
REVOKED
```

---

# 40. Historical Authority

Historical validity MAY remain reconstructable.

Example:

```text
authority valid at t0
revoked at t1
```

A historical action at:

```text
t0 < t1
```

may be auditable as authorized at that time.

That does not restore current authority.

---

# 41. Revocation Freshness

A previously validated authority MUST NOT remain trusted indefinitely if revocation state is mutable.

High-consequence effects SHOULD re-check current authority state before commit.

---

# 42. Authority Freshness

Authority freshness MAY depend on:

```text
authority registry generation;

authority object version;

authority digest;

revocation registry state;

issuer status;

delegation lineage;

policy state;

resource ownership;

transaction state.
```

---

# 43. Freshness Result

```yaml
authority_freshness:
  state:
    - FRESH
    - STALE
    - CONFLICT
    - UNKNOWN_GAP

  checked_at: timestamp

  authority_identity: {}

  registry_identity: {}

  dependencies: []
```

---

# 44. Commit-Time Revalidation

For durable, external, irreversible, or promotion effects:

```text
AUTHORITY AT PLAN TIME
        ↓
PREPARE
        ↓
REVALIDATE AUTHORITY
        ↓
COMMIT
```

Authority must remain valid at the commit boundary.

---

# 45. Commit-Time Invariant

```text
Authorized(t_plan)
```

does not imply:

```text
Authorized(t_commit)
```

when mutable authority state exists.

---

# 46. Authority Witness

Downstream control-plane components SHOULD receive an explicit authority witness.

```yaml
authority_witness:
  witness_id: string

  authority_id: string
  authority_version: string
  authority_digest: string

  principal: string

  operation: string

  capability_id: null

  target_digest: null

  effect_digest: null

  transaction_id: null

  scope: {}

  constraints: []

  evaluated_at: timestamp

  valid_until: null

  authority_registry:
    registry_id: null
    generation: null
    version: null
    snapshot_hash: null

  provenance: {}

  resolver_version: string
```

---

# 47. Witness Binding

The authority witness SHOULD bind to the actual proposed operation.

For consequential effects:

```text
AuthorityWitness
→ principal
→ operation
→ target
→ effect
→ transaction
```

where those dimensions are material.

---

# 48. Witness Replay Prevention

An authority witness valid for:

```text
operation A
```

MUST NOT automatically authorize:

```text
operation B
```

Likewise:

```text
target A
```

must not silently become:

```text
target B
```

---

# 49. Effect Digest Binding

For durable effects, authority MAY bind:

```text
effect_digest
```

so authorization applies to the exact proposed effect.

Conceptually:

```text
AuthorizedEffectDigest
=
CommitEffectDigest
```

must hold where effect-bound authority is required.

---

# 50. Transaction Binding

Authority MAY be transaction-specific.

```yaml
transaction_binding:
  transaction_id: string
  reusable: false
```

A transaction-bound authority MUST NOT silently migrate to another transaction.

---

# 51. Delegated Authority

Authority MAY be delegated only if the upstream authority permits delegation.

```text
Delegate(A_parent)
→ A_child
```

requires:

```text
A_parent.delegable = true
```

plus all applicable governance conditions.

---

# 52. Delegation Attenuation

Delegation MUST NOT widen authority.

```text
Scope(child)
⊆
Scope(parent)
```

and:

```text
Permissions(child)
⊆
Permissions(parent)
```

and:

```text
Validity(child)
⊆
Validity(parent)
```

---

# 53. Delegation Law

Canonical law:

```text
DELEGATED_AUTHORITY
<=
DELEGATING_AUTHORITY
```

No delegation step may create authority absent from its parent.

---

# 54. Delegation Chain

```yaml
delegation_chain:
  root_authority_id: string

  hops:
    - authority_id: string
      issuer: string
      subject: string
      scope: {}
      valid_from: timestamp
      valid_until: timestamp

  depth: integer
```

---

# 55. Delegation Depth

Authority MAY specify:

```text
max_delegation_depth
```

If:

```text
actual_depth > max_delegation_depth
```

resolution fails.

---

# 56. Delegation Chain Validation

Every hop SHOULD validate:

```text
issuer identity;

issuer authority;

delegation permission;

scope attenuation;

temporal containment;

regime containment;

recipient eligibility;

revocation state;

provenance.
```

One invalid load-bearing hop invalidates descendant authority dependent upon it.

---

# 57. Delegation Chain Failure

```text
A0 → A1 → A2 → A3
```

If:

```text
A1 revoked
```

then authority derived exclusively through:

```text
A1
```

must be re-evaluated.

Do not automatically invalidate unrelated independent authority paths.

---

# 58. Multiple Authority Paths

A principal MAY have multiple authority paths.

Example:

```text
DIRECT AUTHORITY
        +
ROLE AUTHORITY
        +
DELEGATED AUTHORITY
```

The resolver MUST preserve them separately until their applicability and provenance are understood.

---

# 59. Independent Authority

Two authority paths are independent only if their load-bearing authority ancestry is independent.

```text
two documents
```

does not establish:

```text
two independent authority sources
```

if both derive from one grant.

---

# 60. Authority Provenance

Authority provenance SHOULD preserve:

```text
issuer;

subject;

source grant;

delegation lineage;

authority version;

authority digest;

registry identity;

revocation source;

transformation history;

resolution event.
```

---

# 61. Provenance Topology

Example:

```text
ROOT_GRANT
   ↓
DELEGATION_A
   ├── COPY_A
   └── SUMMARY_A
```

`COPY_A` and `SUMMARY_A` do not create independent authority.

---

# 62. Authority Sybil Hardening

```text
multiple authority artifacts
!=
multiple independent grants
```

when they share authority ancestry.

The resolver SHOULD reason over ancestry, not document count.

---

# 63. Authority Constraints

Authority MAY carry constraints such as:

```text
maximum amount;

maximum count;

maximum duration;

maximum data volume;

specific recipient;

specific purpose;

specific environment;

specific resource;

specific transaction;

specific effect;

required approval;

required human review;

required policy decision;

required observability;

required audit event.
```

---

# 64. Constraint Object

```yaml
authority_constraint:
  constraint_id: string

  type: string

  operator: string

  value: any

  scope: {}

  temporal: {}

  provenance: {}
```

---

# 65. Constraint Composition

When multiple applicable authority constraints exist, the effective authority SHOULD preserve the most restrictive compatible envelope unless explicit governance defines otherwise.

Conceptually:

```text
EffectiveAuthority
=
Intersection(
    ApplicableAuthorityConstraints
)
```

where intersection semantics are well-defined.

---

# 66. Only-Tighten Rule

Delegation and authority composition MUST NOT silently weaken upstream restrictions.

```text
child restriction
>=
parent restriction
```

in strictness, where the constraint domain permits ordering.

---

# 67. Incompatible Constraints

If two load-bearing authority sources impose incompatible requirements:

```text
CONFLICT
```

unless a valid precedence rule resolves them.

---

# 68. Cumulative Authority Limits

Authority MAY include cumulative budgets.

Examples:

```text
maximum spend;

maximum transactions;

maximum disclosure volume;

maximum resource mutations;

maximum external calls.
```

---

# 69. Cumulative Limit State

```yaml
authority_budget:
  authority_id: string

  metric: string

  limit: number

  consumed: number

  reserved: number

  remaining: number

  state_version: string
```

---

# 70. Reservation

Where concurrent actions can consume the same authority budget:

```text
CHECK
    ↓
RESERVE
    ↓
COMMIT / RELEASE RESERVATION
```

is safer than:

```text
CHECK
    ↓
ACT
```

because concurrent actions may otherwise oversubscribe authority.

---

# 71. Budget Invariant

```text
consumed
+
reserved
<=
limit
```

for valid authority budget state.

---

# 72. Authority Registry

The resolver MAY consume an infrastructure-owned authority registry.

```yaml
authority_registry_snapshot:
  registry_id: string
  generation: string
  version: string
  snapshot_hash: string
  observed_at: timestamp
```

---

# 73. Registry Identity

Where mutable authority state matters, resolution SHOULD preserve:

```text
registry_id
+
generation
+
version
+
snapshot_hash
```

rather than relying on a scalar version alone.

---

# 74. Registry Rollback

Unexpected authority-registry rollback SHOULD trigger:

```text
REVALIDATE
```

or:

```text
CONFLICT
```

rather than silently restoring old authority.

---

# 75. Fine-Grained Authority Read Set

Resolution SHOULD preserve exact authority objects consulted:

```text
AuthorityReadSet =
{
  (
    authority_id,
    authority_version,
    authority_digest
  )
}
```

This supports selective invalidation.

---

# 76. Selective Invalidation

Suppose:

```text
R1 ← A1 + A2

R2 ← A3
```

If:

```text
A2 revoked
```

then:

```text
R1 → REVALIDATE
R2 → PRESERVE
```

unless hidden dependency closure proves otherwise.

---

# 77. Policy Relationship

Authority and policy are separate.

```text
AUTHORITY
```

answers:

> Is this principal empowered to perform the operation?

```text
POLICY
```

answers:

> Is the operation permitted under governing rules?

Both may be required.

---

# 78. Policy/Authority Matrix

```text
POLICY ALLOW + AUTHORITY VALID
→ MAY PROCEED TO OTHER GATES

POLICY ALLOW + AUTHORITY MISSING
→ BLOCK / UNKNOWN

POLICY DENY + AUTHORITY VALID
→ DENY

POLICY UNKNOWN + AUTHORITY VALID
→ REVALIDATE / UNKNOWN

POLICY CONFLICT + AUTHORITY VALID
→ CONFLICT / ESCALATE
```

Authority cannot override policy merely by existing unless explicit higher-order governance says so.

---

# 79. Capability Relationship

Three distinct questions:

```text
CAN the system do it?
→ capability

MAY the principal do it?
→ authority

SHOULD governing rules permit it?
→ policy
```

These MUST remain separate.

---

# 80. Three-Gate Model

```text
CAPABILITY GATE
      +
AUTHORITY GATE
      +
POLICY GATE
      ↓
CONTROL-PLANE ELIGIBILITY
```

Passing these gates still does not equal commit.

---

# 81. Commit Relationship

```text
AUTHORIZED
```

means:

> authority gate satisfied for the evaluated request.

It does NOT mean:

```text
EFFECT_COMMITTED
```

Commit remains downstream.

---

# 82. Release Relationship

For durable/external effects:

```text
AUTHORITY
    ↓
POLICY
    ↓
CAPABILITY
    ↓
TRANSACTION VALIDATION
    ↓
COMMIT-TIME FRESHNESS
    ↓
EFFECT RELEASE
    ↓
RECEIVER-ATTESTED COMPLETION
```

The Authority Resolver owns only its part of this chain.

---

# 83. Emergency Authority

Emergency authority MUST be explicit.

It SHOULD specify:

```text
trigger conditions;

scope;

operations;

resources;

duration;

delegation rights;

audit requirements;

termination conditions;

post-event review.
```

---

# 84. Emergency Boundary

```text
EMERGENCY
```

must not silently become:

```text
UNLIMITED AUTHORITY
```

Emergency authority SHOULD normally be narrower and more observable, not less governed.

---

# 85. Break-Glass Authority

A break-glass authority object MAY contain:

```yaml
break_glass_authority:
  authority_id: string

  trigger: string

  principal: string

  allowed_operations: []

  resources: []

  valid_for_seconds: integer

  required_reason: true

  required_audit: true

  post_action_review: true

  delegable: false
```

---

# 86. Break-Glass Invariant

Break-glass authority MUST NOT bypass provenance, logging, expiry, or post-action review requirements unless explicit higher-order governance says otherwise.

---

# 87. Human Authority

Human instruction MAY constitute authority where:

```text
the user controls the relevant resource;
the requested action is within the user's authority;
the instruction is sufficiently specific;
no higher-order constraint blocks it.
```

The resolver MUST NOT assume all user requests imply universal authority over external resources.

---

# 88. Agent Authority

Agents possess only authority explicitly delegated or otherwise established by governance.

```text
AGENT CAPABILITY
!=
AGENT AUTHORITY
```

An agent cannot manufacture its own authority by reasoning that an action is useful.

---

# 89. Service Authority

Service credentials may establish authenticated service identity.

They do not automatically establish authorization for every operation exposed by that service.

---

# 90. Organizational Authority

Organizational roles MAY contribute authority, but role membership SHOULD resolve through explicit governance.

```text
ROLE = ADMIN
```

is insufficient without knowing:

```text
admin of what;
for which operation;
under which scope;
for what period;
under which constraints.
```

---

# 91. Authority Conflict Classes

```text
SUBJECT_CONFLICT

ISSUER_CONFLICT

SCOPE_CONFLICT

OPERATION_CONFLICT

CAPABILITY_CONFLICT

RESOURCE_CONFLICT

EFFECT_CONFLICT

RECIPIENT_CONFLICT

TEMPORAL_CONFLICT

REGIME_CONFLICT

DELEGATION_CONFLICT

REVOCATION_CONFLICT

PROVENANCE_CONFLICT

REGISTRY_CONFLICT
```

---

# 92. Conflict Resolution

Authority conflicts SHOULD use explicit precedence/governance rules.

Never resolve by:

```text
latest file;

longest document;

most repeated claim;

highest confidence prose;

agent preference;

retrieval rank.
```

---

# 93. Strongest Supported Resolution

The resolver SHOULD return the narrowest authority envelope actually supported.

If authority supports:

```text
READ resource X
```

do not return:

```text
MANAGE resource X
```

---

# 94. Least-Authority Principle

Where multiple resolutions are possible:

```text
EffectiveAuthority
=
smallest sufficient valid authority
```

for the requested operation.

This reduces unintended privilege expansion.

---

# 95. Authority Intersection

Suppose:

```text
A1:
WRITE resources {X,Y}

A2:
WRITE resources {Y,Z}
```

If both are simultaneously load-bearing constraints:

```text
EffectiveScope = {Y}
```

where governance defines intersection semantics.

---

# 96. Authority Union

Authority SHOULD NOT be unioned automatically.

Union is allowed only when multiple grants independently and validly contribute distinct permissions under applicable governance.

---

# 97. No Authority Laundering

The resolver MUST prevent authority laundering such as:

```text
A may read X

A delegates to B

B claims permission to publish X
```

unless publishing was inside the delegable upstream authority.

---

# 98. No Capability Laundering

A more powerful capability MUST NOT expand a principal's authority.

```text
principal authority = READ

tool capability = DELETE
```

still resolves to:

```text
READ
```

not `DELETE`.

---

# 99. No Policy Laundering

A policy saying:

```text
operation is allowed
```

does not create a principal-specific grant.

---

# 100. No Success Laundering

Successful historical execution does not prove valid authority.

```text
ACTION_SUCCEEDED
!=
ACTION_AUTHORIZED
```

---

# 101. No Memory Laundering

Stored memory saying:

```text
"user usually permits this"
```

does not establish current authority for consequential actions.

Authority-dependent actions require appropriate current evidence.

---

# 102. Authority and Memory

Persistent memory MAY provide:

```text
candidate context;
prior grant reference;
resource relationship;
historical preference.
```

It MUST NOT silently manufacture current authorization.

---

# 103. Authority and Consent

Where user consent is part of the authority model, consent SHOULD be:

```text
specific enough;
current enough;
applicable to the action;
within the user's own authority;
revocable where relevant.
```

---

# 104. Authority Resolution Pipeline

```text
01 RECEIVE REQUEST

02 NORMALIZE PRINCIPAL

03 NORMALIZE OPERATION

04 NORMALIZE CAPABILITY

05 NORMALIZE TARGET

06 CLASSIFY EFFECT

07 NORMALIZE RECIPIENT

08 NORMALIZE ENVIRONMENT

09 NORMALIZE JURISDICTION

10 DETERMINE REQUIRED AUTHORITY DIMENSIONS

11 DISCOVER AUTHORITY CANDIDATES

12 VALIDATE CANDIDATE IDENTITIES

13 VALIDATE ISSUERS

14 VALIDATE SUBJECT BINDING

15 VALIDATE DELEGATION CHAINS

16 VALIDATE OPERATION SCOPE

17 VALIDATE CAPABILITY SCOPE

18 VALIDATE RESOURCE SCOPE

19 VALIDATE EFFECT SCOPE

20 VALIDATE RECIPIENT SCOPE

21 VALIDATE ENVIRONMENT

22 VALIDATE JURISDICTION

23 VALIDATE REGIME

24 VALIDATE TEMPORAL ENVELOPE

25 CHECK REVOCATION

26 CHECK SUPERSESSION

27 CHECK CUMULATIVE LIMITS

28 APPLY AUTHORITY CONSTRAINTS

29 DETECT CONFLICTS

30 APPLY PRECEDENCE IF GOVERNED

31 COMPUTE EFFECTIVE AUTHORITY

32 COMPUTE AUTHORITY READ SET

33 COMPUTE CONFIDENCE CEILING

34 ISSUE RESOLUTION

35 EMIT AUTHORITY WITNESS

36 MARK COMMIT-TIME REVALIDATION REQUIREMENTS
```

---

# 105. Fast Path

A fast authority path MAY be used only when:

```text
principal identity is stable;

authority identity is known;

scope matches exactly;

authority is fresh;

revocation state is fresh;

no delegation ambiguity exists;

no authority conflict exists;

effect is within permitted consequence class;

no relevant mutable dependency is unresolved.
```

Otherwise escalate to full resolution.

---

# 106. Fast-Path Boundary

Optimization MUST NOT remove:

```text
revocation checking;

scope checking;

subject binding;

operation binding;

effect binding;

commit-time revalidation where required.
```

---

# 107. Authority Cache

Resolved authority MAY be cached only with its validity envelope.

```yaml
authority_cache_entry:
  resolution_id: string

  authority_id: string
  authority_version: string
  authority_digest: string

  principal: string

  scope: {}

  regime: {}

  valid_until: null

  registry_identity: {}

  dependency_hashes: []

  cached_at: timestamp
```

---

# 108. Cache Invalidation

Authority cache MUST invalidate or revalidate on relevant:

```text
revocation;

expiry;

authority version change;

authority digest change;

delegation change;

registry generation change;

resource ownership change;

policy dependency change;

transaction change;

scope change;

regime change.
```

---

# 109. Cache Boundary

```text
CACHED_AUTHORITY
!=
CURRENT_AUTHORITY
```

unless freshness conditions remain valid.

---

# 110. Resolution Provenance

Every consequential authority resolution SHOULD preserve:

```text
request identity;

principal identity;

authority candidates;

authority object identities;

delegation lineage;

revocation evidence;

scope evaluation;

constraint evaluation;

resolution state;

resolver version;

evaluation time.
```

---

# 111. Audit Record

```yaml
authority_resolution_audit:
  audit_id: string

  resolution_id: string

  request_id: string

  principal_id: string

  operation_id: string

  authority_ids: []

  state: string

  effective_scope: {}

  constraints: []

  authority_read_set: []

  registry_snapshot: {}

  evaluated_at: timestamp

  commit_revalidation_required: boolean

  provenance: {}
```

---

# 112. Observability Events

Recommended events:

```text
AUTHORITY_RESOLUTION_REQUESTED

AUTHORITY_CANDIDATE_DISCOVERED

AUTHORITY_VALIDATED

AUTHORITY_REJECTED

AUTHORITY_EXPIRED

AUTHORITY_REVOKED

AUTHORITY_CONFLICT_DETECTED

AUTHORITY_DELEGATION_VALIDATED

AUTHORITY_DELEGATION_FAILED

AUTHORITY_SCOPE_MISMATCH

AUTHORITY_CONSTRAINT_FAILED

AUTHORITY_REVALIDATION_REQUIRED

AUTHORITY_WITNESS_ISSUED

AUTHORITY_RESOLUTION_ESCALATED
```

---

# 113. Privacy Boundary

Authority evidence may contain sensitive:

```text
identity;

organizational role;

resource ownership;

delegation;

recipient;

security;

legal;

transaction
```

information.

Observability MUST expose only the minimum necessary information.

---

# 114. Core Invariants

## INV-AR-001 — Identity/Authority Separation

```text
IDENTITY != AUTHORITY
```

## INV-AR-002 — Authentication/Authority Separation

```text
AUTHENTICATION != AUTHORITY
```

## INV-AR-003 — Capability/Authority Separation

```text
CAPABILITY != AUTHORITY
```

## INV-AR-004 — Policy/Authority Separation

```text
POLICY_ALLOW != AUTHORITY
```

## INV-AR-005 — Subject Binding

Authority MUST resolve to the requesting principal or valid delegation chain.

## INV-AR-006 — Operation Binding

Authority MUST cover the requested operation.

## INV-AR-007 — Scope Containment

```text
RequestedScope ⊆ AuthorizedScope
```

## INV-AR-008 — Effect Binding

Authority MUST cover the requested effect class where effect scope is material.

## INV-AR-009 — Temporal Validity

Expired authority MUST NOT authorize current actions.

## INV-AR-010 — Revocation

Revoked authority MUST NOT authorize current actions.

---

# 115. Additional Invariants

## INV-AR-011 — Delegation Attenuation

Delegated authority MUST NOT exceed upstream authority.

## INV-AR-012 — Delegation Provenance

Delegation ancestry MUST remain reconstructable.

## INV-AR-013 — No Authority Sybil

Copies do not create independent authority.

## INV-AR-014 — Regime Containment

Authority MUST remain within its allowed regime.

## INV-AR-015 — Environment Containment

Environment-specific authority MUST NOT silently cross environments.

## INV-AR-016 — Recipient Containment

Disclosure authority MUST preserve recipient restrictions.

## INV-AR-017 — Jurisdiction Containment

Jurisdiction-bound authority MUST remain bounded.

## INV-AR-018 — Constraint Preservation

Downstream authority MUST preserve applicable constraints.

## INV-AR-019 — Budget Preservation

Cumulative authority limits MUST NOT be exceeded.

## INV-AR-020 — Freshness

Mutable authority MUST be revalidated when freshness assumptions expire.

---

# 116. Commit Invariants

## INV-AR-021 — Plan/Commit Separation

```text
AUTHORIZED_AT_PLAN
!=
AUTHORIZED_AT_COMMIT
```

when authority can change.

## INV-AR-022 — Witness Binding

Authority witness MUST bind to decision-relevant action identity.

## INV-AR-023 — Transaction Binding

Transaction-specific authority MUST NOT migrate across transactions.

## INV-AR-024 — No Replay Expansion

A witness MUST NOT authorize a broader action than the one evaluated.

## INV-AR-025 — No Authority Self-Issuance

An agent MUST NOT create authority for itself absent an authorized authority-issuance mechanism.

---

# 117. Governance Invariants

## INV-AR-026 — Unknown Is Not Authority

```text
UNKNOWN/GAP != AUTHORIZED
```

## INV-AR-027 — Conflict Is Not Authority

```text
CONFLICT != AUTHORIZED
```

## INV-AR-028 — Technical Success Is Not Authority

```text
EXECUTION_SUCCESS != AUTHORIZED
```

## INV-AR-029 — Historical Success Is Not Authority

Historical execution does not establish current authority.

## INV-AR-030 — Authority Does Not Equal Commit

```text
AUTHORIZED != COMMITTED
```

---

# 118. Failure Modes

```text
FM-AR-001 principal mismatch

FM-AR-002 authority ID collision

FM-AR-003 authority digest mismatch

FM-AR-004 forged authority

FM-AR-005 untrusted issuer

FM-AR-006 issuer authority missing

FM-AR-007 delegation not permitted

FM-AR-008 delegation scope expansion

FM-AR-009 delegation depth exceeded

FM-AR-010 broken delegation lineage

FM-AR-011 revoked ancestor

FM-AR-012 expired authority

FM-AR-013 stale revocation state

FM-AR-014 operation mismatch

FM-AR-015 capability mismatch

FM-AR-016 resource mismatch

FM-AR-017 effect mismatch

FM-AR-018 recipient mismatch

FM-AR-019 environment mismatch

FM-AR-020 jurisdiction mismatch

FM-AR-021 regime mismatch

FM-AR-022 unknown scope

FM-AR-023 conflicting authority

FM-AR-024 cumulative budget exceeded

FM-AR-025 concurrent budget oversubscription

FM-AR-026 stale authority cache

FM-AR-027 registry rollback

FM-AR-028 authority witness replay

FM-AR-029 transaction substitution

FM-AR-030 effect substitution

FM-AR-031 authority laundering

FM-AR-032 capability laundering

FM-AR-033 policy laundering

FM-AR-034 memory laundering

FM-AR-035 agent self-authorization

FM-AR-036 missing provenance

FM-AR-037 correlated authority counted independently

FM-AR-038 commit after authority revocation

FM-AR-039 authority widened during normalization

FM-AR-040 unknown treated as authorized
```

---

# 119. Recovery

Canonical recovery:

```text
DETECT AUTHORITY FAILURE
        ↓
BLOCK AFFECTED EFFECT
        ↓
PRESERVE REQUEST + EVIDENCE
        ↓
IDENTIFY FAILED AUTHORITY PREMISE
        ↓
INVALIDATE DEPENDENT RESOLUTION
        ↓
PRESERVE INDEPENDENT AUTHORITY PATHS
        ↓
REFRESH AUTHORITY STATE
        ↓
REFRESH REVOCATION STATE
        ↓
REVALIDATE DELEGATION
        ↓
REVALIDATE SCOPE
        ↓
RECOMPUTE EFFECTIVE AUTHORITY
        ↓
ISSUE NEW RESOLUTION OR DENY
```

---

# 120. Selective Recovery

If one authority path fails:

```text
A1 invalid
A2 independently valid
```

do not automatically discard `A2`.

Revalidate only affected dependency closure.

---

# 121. Revocation Recovery

If authority is revoked after planning but before commit:

```text
PREPARED ACTION
    ↓
AUTHORITY REVOKED
    ↓
COMMIT REVALIDATION FAILS
    ↓
BLOCK EFFECT
```

The prepared action does not preserve expired authority.

---

# 122. Conflict Recovery

For unresolved conflict:

```text
CONFLICT
    ↓
IDENTIFY MINIMUM DISCRIMINATING EVIDENCE
    ↓
RESOLVE ISSUER / SCOPE / VERSION / REVOCATION
    ↓
RE-EVALUATE
```

Do not accumulate redundant copies of the same authority source.

---

# 123. Tests

Minimum validator suite:

```text
T-AR-001 request schema

T-AR-002 principal identity

T-AR-003 authority identity

T-AR-004 authority digest

T-AR-005 issuer identity

T-AR-006 subject binding

T-AR-007 direct authority

T-AR-008 delegated authority

T-AR-009 delegation permission

T-AR-010 delegation attenuation

T-AR-011 delegation depth

T-AR-012 delegation temporal containment

T-AR-013 revoked delegation ancestor

T-AR-014 operation match

T-AR-015 operation mismatch

T-AR-016 capability match

T-AR-017 capability mismatch

T-AR-018 resource match

T-AR-019 resource mismatch

T-AR-020 effect match

T-AR-021 effect mismatch

T-AR-022 recipient match

T-AR-023 recipient mismatch

T-AR-024 environment match

T-AR-025 environment mismatch

T-AR-026 jurisdiction match

T-AR-027 jurisdiction mismatch

T-AR-028 regime match

T-AR-029 regime mismatch

T-AR-030 valid temporal authority

T-AR-031 expired authority

T-AR-032 revoked authority

T-AR-033 future authority

T-AR-034 authority constraint

T-AR-035 cumulative limit

T-AR-036 concurrent reservation

T-AR-037 multiple independent grants

T-AR-038 correlated grants

T-AR-039 authority conflict

T-AR-040 authority precedence

T-AR-041 authority cache

T-AR-042 cache invalidation

T-AR-043 registry generation change

T-AR-044 registry rollback

T-AR-045 authority witness

T-AR-046 witness principal binding

T-AR-047 witness operation binding

T-AR-048 witness target binding

T-AR-049 witness effect binding

T-AR-050 witness transaction binding

T-AR-051 witness replay rejection

T-AR-052 plan-time authority

T-AR-053 commit-time revalidation

T-AR-054 revocation between plan and commit

T-AR-055 capability/authority separation

T-AR-056 policy/authority separation

T-AR-057 unknown authority

T-AR-058 agent self-authorization rejection

T-AR-059 selective invalidation

T-AR-060 audit reconstruction
```

---

# 124. Adversarial Tests

```text
authenticated admin with no resource authority;

authority copied into three files;

expired grant presented with valid signature;

revoked grant retrieved from cache;

delegated grant wider than parent;

delegation chain hides revoked ancestor;

authority for READ reused for DELETE;

authority for resource A reused for resource B;

authority for TEST reused in PRODUCTION;

authority for recipient A reused for recipient B;

transaction-bound grant replayed in another transaction;

effect-bound witness used with changed effect payload;

policy ALLOW treated as authority;

available tool treated as authority;

agent claims self-authority because task is beneficial;

old user permission stored in memory reused for current external action;

registry rollback restores revoked authority;

concurrent operations exceed cumulative authority limit;

unknown jurisdiction treated as global authority;

missing scope treated as wildcard.
```

---

# 125. Validator Outcomes

Authority validators SHOULD return:

```text
VALID

INVALID

EXPIRED

REVOKED

CONFLICT

REVALIDATE

ESCALATE

UNKNOWN_GAP
```

No failed validator becomes `VALID` by default.

---

# 126. Falsifiers

A claim of valid authority is falsified if reliable evidence establishes any load-bearing failure such as:

```text
principal mismatch;

issuer invalidity;

authority forgery;

authority expiry;

authority revocation;

operation outside scope;

capability outside scope;

target outside scope;

effect outside scope;

recipient outside scope;

environment outside scope;

jurisdiction outside scope;

regime mismatch;

invalid delegation;

delegation widening;

authority budget exceeded;

authority witness mismatch;

transaction mismatch;

effect digest mismatch;

registry rollback;

or unresolved authority conflict.
```

---

# 127. Agents

Functional agent roles MAY include:

```text
AUTHORITY_DISCOVERY_AGENT

AUTHORITY_VALIDATION_AGENT

DELEGATION_AUDITOR

REVOCATION_MONITOR

AUTHORITY_SCOPE_RESOLVER

AUTHORITY_CONFLICT_AUDITOR

AUTHORITY_PROVENANCE_AUDITOR

AUTHORITY_REPAIR_AGENT
```

These roles do not themselves confer authority.

---

# 128. Agent Boundary

```text
AUTHORITY_RESOLVER_AGENT
!=
AUTHORITY_ISSUER
```

unless an independently governed authority-issuance capability explicitly grants that role.

---

# 129. Skills

Relevant Skills MAY include:

```text
portable agent authorization;

commit-time authorization;

infrastructure control plane;

principal trust governance;

constraint propagation;

information boundary governance;

provenance hardening;

policy resolution;

transaction governance;

repair/recovery.
```

Skill availability does not grant action authority.

---

# 130. Protocol — Resolve Authority

```yaml
resolve_authority:
  request: {}
```

Response:

```yaml
resolve_authority_result:
  resolution: {}
  witness: null
  gaps: []
```

---

# 131. Protocol — Validate Authority

```yaml
validate_authority:
  authority_id: string
  authority_version: string
  authority_digest: string

  principal: string

  operation: string

  context: {}
```

---

# 132. Protocol — Revalidate Authority

```yaml
revalidate_authority:
  resolution_id: string

  prior_witness: {}

  current_context: {}

  current_time: timestamp
```

Possible result:

```text
STILL_AUTHORIZED

AUTHORIZED_CONDITIONAL

REVOKED

EXPIRED

CONFLICT

REVALIDATE

DENIED

UNKNOWN_GAP
```

---

# 133. Protocol — Validate Delegation

```yaml
validate_delegation:
  root_authority: {}

  delegation_chain: []

  requested_operation: {}

  requested_scope: {}

  evaluation_time: timestamp
```

---

# 134. Protocol — Check Revocation

```yaml
check_authority_revocation:
  authority_id: string
  authority_version: string
  authority_digest: string

  evaluation_time: timestamp
```

---

# 135. Protocol — Reserve Authority Budget

```yaml
reserve_authority_budget:
  authority_id: string

  metric: string

  amount: number

  transaction_id: string

  expected_state_version: string
```

Possible result:

```text
RESERVED

INSUFFICIENT_AUTHORITY

CONFLICT

REVALIDATE

UNKNOWN_GAP
```

---

# 136. Protocol — Release Reservation

```yaml
release_authority_reservation:
  authority_id: string

  reservation_id: string

  transaction_id: string
```

---

# 137. Protocol — Consume Reservation

```yaml
consume_authority_reservation:
  authority_id: string

  reservation_id: string

  transaction_id: string

  committed_effect_ref: string
```

---

# 138. Authority Resolver / Policy Engine Interface

```yaml
authority_policy_interface:
  authority_resolution_id: string

  principal: string

  operation: string

  authority_state: string

  effective_scope: {}

  constraints: []

  authority_witness: {}

  policy_context: {}
```

The Policy Engine may use the authority state as an input.

It MUST NOT rewrite authority evidence.

---

# 139. Authority Resolver / Capability Interface

```yaml
authority_capability_interface:
  capability_id: string

  operation: string

  required_authority_dimensions: []

  authority_resolution: {}
```

Capability providers may declare authority requirements.

They do not self-certify that those requirements are satisfied.

---

# 140. Authority Resolver / Control Plane Interface

```yaml
authority_control_plane_bundle:
  resolution_id: string

  authority_witness: {}

  authority_read_set: []

  registry_snapshot: {}

  commit_revalidation_required: true

  unresolved_conditions: []
```

---

# 141. Commit-Time Resolver Input

```yaml
commit_authority_check:
  transaction_id: string

  principal: string

  operation: string

  capability_id: string

  target_digest: string

  effect_digest: string

  prior_authority_witness: {}

  current_time: timestamp

  current_authority_registry: {}
```

---

# 142. Commit-Time Resolver Output

```yaml
commit_authority_result:
  state:
    - AUTHORIZED_CURRENT
    - AUTHORITY_CHANGED
    - AUTHORITY_REVOKED
    - AUTHORITY_EXPIRED
    - AUTHORITY_SCOPE_CHANGED
    - CONFLICT
    - REVALIDATE
    - DENIED
    - UNKNOWN_GAP

  current_witness: null

  changed_dependencies: []

  reason_codes: []
```

---

# 143. Commit Gate

Effect release MAY proceed only if required authority checks resolve successfully.

Conceptually:

```text
CommitEligible
=
AuthorityCurrent
∧ PolicyCurrent
∧ CapabilityCurrent
∧ TransactionValid
∧ RequiredConstraintsSatisfied
```

Additional gates may exist.

---

# 144. Authority Resolution Confidence

For an authority conclusion:

```text
C_authority
≤
min(
    C_principal,
    C_issuer,
    C_authority_identity,
    C_delegation,
    C_scope,
    C_temporal,
    C_revocation,
    C_regime,
    C_provenance
)
```

AMOS MODEL constraint.

Derived authority confidence cannot exceed its weakest load-bearing premise.

---

# 145. Uncertainty Vector

```yaml
authority_uncertainty:
  principal: null

  issuer: null

  identity: null

  scope: null

  temporal: null

  revocation: null

  delegation: null

  regime: null

  provenance: null

  execution: null
```

Material uncertainty SHOULD remain visible.

---

# 146. Sensitivity

For consequential authority decisions, identify the smallest premise capable of changing:

```text
AUTHORIZED
↔
DENIED / UNKNOWN / REVALIDATE
```

Typical high-sensitivity premises:

```text
revocation state;

expiry;

resource scope;

operation scope;

delegation validity;

recipient;

effect digest;

transaction identity.
```

Check these before low-value contextual details.

---

# 147. Adversarial Validation

For consequential authority resolutions, challenge the strongest supported authority conclusion by asking:

```text
Is the authority stale?

Was it revoked?

Is the issuer actually authorized?

Did delegation widen scope?

Does the grant cover this exact operation?

Does it cover this exact resource?

Does it cover this recipient?

Does it cover this effect?

Does it cover this environment?

Does it cover this transaction?

Are supposedly independent grants actually descendants of one source?

Did a cached witness survive a relevant state change?
```

If a challenge succeeds, downgrade the resolution.

---

# 148. RSCF Authority Capsule

```yaml
rscf:
  claim:
    id: "RSCF_AUTHORITY_RESOLUTION"
    class: DERIVED

  premises:
    - principal_identity_valid
    - issuer_valid
    - authority_identity_valid
    - delegation_valid
    - operation_in_scope
    - resource_in_scope
    - effect_in_scope
    - temporal_valid
    - not_revoked
    - regime_valid
    - constraints_satisfied

  evidence: []

  provenance: []

  scope: {}

  regime: {}

  dependencies: []

  competing: []

  falsifiers:
    - principal_mismatch
    - issuer_invalid
    - revoked
    - expired
    - scope_mismatch
    - delegation_invalid

  confidence_ceiling: null
```

---

# 149. RSCF Invalidation

If:

```text
not_revoked
```

becomes false:

```text
AUTHORITY RESOLUTION
→ INVALIDATE
```

and dependent commit eligibility must be re-evaluated.

Unrelated resolutions remain intact where dependency closure is known.

---

# 150. GMEF Integration

Changes affecting:

```text
authority semantics;

delegation;

revocation;

scope resolution;

commit-time authority;

authority witness format;

authority budget;

registry identity;

conflict resolution
```

SHOULD be governed changes.

---

# 151. Change Manifest

```yaml
authority_resolver_change:
  change_id: string

  from_version: string
  to_version: string

  change_class:
    - COSMETIC
    - SCHEMA
    - SEMANTIC
    - SECURITY
    - GOVERNANCE
    - AUTHORITY_BOUNDARY

  affected_invariants: []

  affected_protocols: []

  expected_behavior_changes: []

  risks: []

  validators_required: []

  rollback_plan: null

  approval_state: PROPOSED
```

---

# 152. Promotion Model

```text
STRUCTURAL_MODEL
        ↓
SCHEMA_VALIDATED
        ↓
AUTHORITY_STORE_CONNECTED
        ↓
IDENTITY_VALIDATION_IMPLEMENTED
        ↓
DELEGATION_VALIDATION_IMPLEMENTED
        ↓
REVOCATION_IMPLEMENTED
        ↓
SCOPE_RESOLUTION_IMPLEMENTED
        ↓
UNIT_TESTED
        ↓
INTEGRATION_TESTED
        ↓
ADVERSARIALLY_TESTED
        ↓
COMMIT-TIME_VALIDATED
        ↓
GOVERNED_ACTIVE
```

No transition is automatic.

---

# 153. Implementation Requirements

An executable Authority Resolver SHOULD eventually provide:

```text
principal resolution;

authority discovery;

authority object validation;

issuer validation;

delegation-chain validation;

scope intersection;

operation binding;

resource binding;

effect binding;

recipient binding;

temporal validation;

trusted-time integration;

revocation lookup;

registry freshness;

constraint evaluation;

cumulative-budget handling;

conflict detection;

authority witness generation;

fine-grained read sets;

commit-time revalidation;

audit events;

selective invalidation.
```

This document does not claim those components are currently implemented.

---

# 154. Example — Direct Authority

```yaml
authority_object:
  authority_id: "AUTH::RESOURCE::WRITE_PROJECT_A"

  authority_version: "1.0.0"

  authority_digest: "sha256:<digest>"

  authority_class: DIRECT

  issuer:
    issuer_id: "PRINCIPAL_OWNER"

  subject:
    principal_id: "AGENT_A"
    principal_type: AGENT

  permissions:
    operations:
      - UPDATE

    resources:
      - "PROJECT_A"

    effect_classes:
      - MUTATING

  delegation:
    delegable: false

  temporal:
    issued_at: "2026-08-26T00:00:00Z"
    valid_from: "2026-08-26T00:00:00Z"
    valid_until: "2026-08-27T00:00:00Z"

  status: ACTIVE
```

This is an architectural example, not evidence that this grant exists.

---

# 155. Example — Delegated Authority

```text
HUMAN_OWNER
    ↓
AUTHORITY_A
    ↓ delegates
SERVICE_A
    ↓
AUTHORITY_B
    ↓ delegates
AGENT_A
```

Required:

```text
A permits delegation;

B scope ⊆ A scope;

B duration ⊆ A duration;

AGENT_A operation ∈ B permissions;

neither A nor B revoked.
```

---

# 156. Example — Scope Failure

Authority:

```text
READ PROJECT_A
```

Request:

```text
DELETE PROJECT_A
```

Resolution:

```yaml
state: DENIED

reason_codes:
  - OPERATION_OUT_OF_SCOPE
```

---

# 157. Example — Resource Failure

Authority:

```text
WRITE PROJECT_A
```

Request:

```text
WRITE PROJECT_B
```

Result:

```text
DENIED
```

unless another valid authority independently covers `PROJECT_B`.

---

# 158. Example — Expired Authority

```text
valid_until = 2026-08-25T00:00:00Z

evaluation_time = 2026-08-26T00:00:00Z
```

Result:

```text
EXPIRED
```

A valid historical signature does not restore current authority.

---

# 159. Example — Revocation Between Plan and Commit

At planning:

```text
AUTHORITY_A = ACTIVE
```

Action prepared.

Before commit:

```text
AUTHORITY_A = REVOKED
```

Commit-time result:

```text
AUTHORITY_REVOKED
```

Effect:

```text
BLOCK
```

---

# 160. Example — Capability Without Authority

```text
CAPABILITY:
DELETE_RESOURCE = AVAILABLE

AUTHORITY:
DELETE_RESOURCE = NONE
```

Result:

```text
NO AUTHORIZED DELETE
```

The capability remains addressable but unusable for this principal/request.

---

# 161. Example — Policy Without Authority

```text
POLICY:
DELETE may be performed by authorized administrators.

PRINCIPAL:
not proven to be authorized administrator.
```

Result:

```text
UNKNOWN_GAP
```

or:

```text
DENIED
```

depending on the governing policy semantics.

Never infer authority from the policy statement alone.

---

# 162. Example — Authority Without Policy Permission

```text
AUTHORITY:
principal may mutate resource.

POLICY:
mutation prohibited in current regime.
```

Result:

```text
POLICY DENY
```

Authority does not erase the policy gate.

---

# 163. Example — Authority Sybil

Three records:

```text
AUTH_A_COPY_1

AUTH_A_COPY_2

AUTH_A_SUMMARY
```

all derive from:

```text
AUTH_A
```

Then:

```text
IndependentAuthorityRoots = 1
```

not `3`.

---

# 164. Example — Selective Invalidation

```text
R1 ← AUTH_A + AUTH_B

R2 ← AUTH_C

R3 ← AUTH_B + AUTH_D
```

If:

```text
AUTH_B revoked
```

then:

```text
R1 → REVALIDATE

R3 → REVALIDATE

R2 → PRESERVE
```

subject to dependency closure.

---

# 165. Example — Cumulative Authority

Authority:

```text
maximum external sends = 10
```

State:

```text
consumed = 8
reserved = 1
remaining = 1
```

Two concurrent requests each attempt to reserve `1`.

Only one may succeed if reservation is atomic.

Otherwise both may incorrectly observe available capacity.

---

# 166. Authority Resolution Decision Table

| Condition                   | Resolution             |
| --------------------------- | ---------------------- |
| Valid exact authority       | AUTHORIZED             |
| Valid but conditions remain | AUTHORIZED_CONDITIONAL |
| Operation outside scope     | DENIED                 |
| Resource outside scope      | DENIED                 |
| Effect outside scope        | DENIED                 |
| Recipient outside scope     | DENIED                 |
| Expired                     | EXPIRED                |
| Revoked                     | REVOKED                |
| Conflicting grants          | CONFLICT               |
| Stale authority state       | REVALIDATE             |
| Higher authority required   | ESCALATE               |
| Evidence insufficient       | UNKNOWN_GAP            |

---

# 167. Control-Plane Decision Table

| Authority | Policy  | Capability  | Result                      |
| --------- | ------- | ----------- | --------------------------- |
| VALID     | ALLOW   | AVAILABLE   | continue to remaining gates |
| VALID     | DENY    | AVAILABLE   | BLOCK                       |
| VALID     | UNKNOWN | AVAILABLE   | REVALIDATE / BLOCK          |
| MISSING   | ALLOW   | AVAILABLE   | BLOCK                       |
| REVOKED   | ALLOW   | AVAILABLE   | BLOCK                       |
| EXPIRED   | ALLOW   | AVAILABLE   | BLOCK                       |
| CONFLICT  | ALLOW   | AVAILABLE   | BLOCK / ESCALATE            |
| VALID     | ALLOW   | UNAVAILABLE | NO_EXECUTION                |
| VALID     | ALLOW   | UNKNOWN     | REVALIDATE                  |

---

# 168. Audit Questions

An auditor SHOULD be able to answer:

1. Who requested the operation?
2. How was principal identity established?
3. What operation was requested?
4. What capability would perform it?
5. What target would be affected?
6. What effect class applies?
7. Who would receive information/effects?
8. What environment applies?
9. What jurisdiction applies?
10. What authority candidates were discovered?
11. What authority object was selected?
12. Who issued it?
13. Did the issuer possess authority to issue/delegate it?
14. What delegation chain exists?
15. Did every delegation attenuate authority?
16. Is the operation within scope?
17. Is the resource within scope?
18. Is the capability within scope?
19. Is the effect within scope?
20. Is the recipient within scope?
21. Is the environment within scope?
22. Is the jurisdiction within scope?
23. Is the authority temporally valid?
24. Has it been revoked?
25. What authority registry state was observed?
26. What exact authority objects formed the read set?
27. What constraints apply?
28. What cumulative limits apply?
29. Were limits reserved atomically where necessary?
30. Were competing authority paths preserved?
31. Were correlated authority artifacts deduplicated by ancestry?
32. What authority witness was issued?
33. What action identity does the witness bind?
34. Is commit-time revalidation required?
35. Was authority still current at commit?
36. What unresolved gaps remain?

---

# 169. Completion Matrix

| Surface                                  | Specification State |
| ---------------------------------------- | ------------------- |
| Purpose                                  | COMPLETE_AS_MODEL   |
| Architecture                             | COMPLETE_AS_MODEL   |
| Request schema                           | COMPLETE_AS_MODEL   |
| Resolution schema                        | COMPLETE_AS_MODEL   |
| Authority object                         | COMPLETE_AS_MODEL   |
| Authority identity                       | COMPLETE_AS_MODEL   |
| Principal binding                        | COMPLETE_AS_MODEL   |
| Authentication boundary                  | COMPLETE_AS_MODEL   |
| Candidate discovery                      | COMPLETE_AS_MODEL   |
| Scope resolution                         | COMPLETE_AS_MODEL   |
| Operation binding                        | COMPLETE_AS_MODEL   |
| Capability binding                       | COMPLETE_AS_MODEL   |
| Resource binding                         | COMPLETE_AS_MODEL   |
| Effect binding                           | COMPLETE_AS_MODEL   |
| Recipient binding                        | COMPLETE_AS_MODEL   |
| Environment binding                      | COMPLETE_AS_MODEL   |
| Jurisdiction binding                     | COMPLETE_AS_MODEL   |
| Temporal validity                        | COMPLETE_AS_MODEL   |
| Revocation                               | COMPLETE_AS_MODEL   |
| Freshness                                | COMPLETE_AS_MODEL   |
| Authority witness                        | COMPLETE_AS_MODEL   |
| Transaction binding                      | COMPLETE_AS_MODEL   |
| Delegation                               | COMPLETE_AS_MODEL   |
| Delegation attenuation                   | COMPLETE_AS_MODEL   |
| Provenance topology                      | COMPLETE_AS_MODEL   |
| Constraint composition                   | COMPLETE_AS_MODEL   |
| Cumulative limits                        | COMPLETE_AS_MODEL   |
| Fine-grained read sets                   | COMPLETE_AS_MODEL   |
| Selective invalidation                   | COMPLETE_AS_MODEL   |
| Policy interface                         | COMPLETE_AS_MODEL   |
| Capability interface                     | COMPLETE_AS_MODEL   |
| Control-plane interface                  | COMPLETE_AS_MODEL   |
| Commit-time revalidation                 | COMPLETE_AS_MODEL   |
| Emergency authority                      | COMPLETE_AS_MODEL   |
| Agents                                   | COMPLETE_AS_MODEL   |
| Skills                                   | COMPLETE_AS_MODEL   |
| Protocols                                | COMPLETE_AS_MODEL   |
| Invariants                               | COMPLETE_AS_MODEL   |
| Failure modes                            | COMPLETE_AS_MODEL   |
| Recovery                                 | COMPLETE_AS_MODEL   |
| Tests                                    | COMPLETE_AS_MODEL   |
| Falsifiers                               | COMPLETE_AS_MODEL   |
| RSCF                                     | COMPLETE_AS_MODEL   |
| GMEF                                     | COMPLETE_AS_MODEL   |
| Executable resolver                      | UNKNOWN/GAP         |
| Authority registry implementation        | UNKNOWN/GAP         |
| Cryptographic authority verification     | UNKNOWN/GAP         |
| Atomic budget reservation implementation | UNKNOWN/GAP         |
| Executed validators                      | UNKNOWN/GAP         |
| Production deployment                    | UNKNOWN/GAP         |
| Formal verification                      | UNKNOWN/GAP         |
| Canon admission                          | UNKNOWN/GAP         |

---

# 170. RSCF Completion State

```yaml
rscf_completion:
  claim:
    id: "AMOS_AUTHORITY_RESOLVER"
    class: MODEL

    text: >
      This artifact defines a structurally complete AMOS OS
      authority-resolution architecture separating identity,
      capability, policy, authority, execution, and commit.

  evidence:
    - "AMOS infrastructure/control-plane architecture"
    - "authority-resolution architecture defined in this artifact"

  provenance:
    origin_architect: "Trang Phan"
    steward: "Trang Phan"

  scope:
    system: "AMOS OS"
    component: "Authority Resolver"

  regime:
    - DESIGN
    - ARCHITECTURE
    - GOVERNANCE_MODEL

  freshness:
    artifact_version: "1.0.0"
    updated: "2026-08-26"

  dependencies:
    - CONTROL_PLANE_MAP.md
    - POLICY_REGISTRY.md
    - POLICY_ENGINE.md
    - POLICY_DECISION.md
    - CAPABILITY_MANIFEST.md
    - CAPABILITY_CONTRACT.md

  competing: []

  falsifiers:
    - "identity is accepted as authority"
    - "capability creates authority"
    - "policy ALLOW creates authority"
    - "delegation expands upstream authority"
    - "revoked authority remains valid"
    - "expired authority remains valid"
    - "authority is not revalidated when mutable state changes"
    - "authority witness can be replayed for a different effect"

  confidence_ceiling: 0
```

`confidence_ceiling: 0` indicates that runtime implementation and validation are not being claimed by this architecture document.

---

# 171. Hard Boundary Block

```text
IDENTITY != AUTHORITY

AUTHENTICATION != AUTHORITY

ROLE != AUTHORITY

CAPABILITY != AUTHORITY

ACCESS != AUTHORITY

POLICY != AUTHORITY

POLICY_ALLOW != AUTHORITY

TOOL_AVAILABLE != AUTHORITY

SKILL_AVAILABLE != AUTHORITY

AGENT_ROLE != AUTHORITY

AUTHORITY_REFERENCE != VALID_AUTHORITY

AUTHORITY_CANDIDATE != RESOLVED_AUTHORITY

AUTHORITY_SIGNATURE != CURRENT_AUTHORITY

HISTORICAL_AUTHORITY != CURRENT_AUTHORITY

AUTHORITY_TO_READ != AUTHORITY_TO_WRITE

AUTHORITY_TO_WRITE != AUTHORITY_TO_DELETE

AUTHORITY_TO_EXECUTE != AUTHORITY_TO_COMMIT

AUTHORITY_TO_COMMIT != AUTHORITY_TO_RELEASE

AUTHORITY_TO_ACCESS != AUTHORITY_TO_DISCLOSE

AUTHORITY_TO_DISCLOSE_TO_A != AUTHORITY_TO_DISCLOSE_TO_B

DELEGATED_AUTHORITY <= DELEGATING_AUTHORITY

DELEGATION != AUTHORITY_EXPANSION

AUTHORITY_AT_PLAN_TIME != AUTHORITY_AT_COMMIT_TIME

AUTHORIZED != EXECUTED

AUTHORIZED != COMMITTED

EXECUTED != AUTHORIZED

SUCCESS != AUTHORIZED

MEMORY != AUTHORITY

PRIOR_CONSENT != CURRENT_UNIVERSAL_AUTHORITY

DISCOVERED != VALIDATED

REGISTERED != APPLICABLE

UNKNOWN/GAP != AUTHORIZED

CONFLICT != AUTHORIZED

EXPIRED != AUTHORIZED

REVOKED != AUTHORIZED

PROPOSAL != COMMIT

PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

STRUCTURAL_MODEL != EXECUTABLE_RUNTIME

IMPLEMENTED != VALIDATED

TESTED != FORMALLY_VERIFIED

MODEL != EMPIRICAL_FACT
```

---

# 172. Canon Boundary

Trang Phan remains the origin architect and steward of AMOS.

This document defines a substantive proposed architecture for the AMOS `AUTHORITY_RESOLVER.md` surface.

Its structural completeness does not establish:

```text
runtime implementation;

authority-store implementation;

cryptographic verification;

executed tests;

production deployment;

formal verification;

or canonical admission.
```

Until separately admitted through the appropriate AMOS canon, provenance, governance, and supersession process:

```yaml
artifact_status: PROPOSED

epistemic_class: MODEL

structural_status: COMPLETE_AS_MODEL

runtime_status: UNKNOWN/GAP

validation_status: UNKNOWN/GAP

canonical_status: UNKNOWN/GAP
```

Applicable validated source canon outranks generated model additions, subject to:

```text
version;
scope;
regime;
provenance;
supersession;
and dependency compatibility.
```

---

# 173. Final Authority Resolver Contract

AMOS SHALL preserve the conceptual authority chain:

```text
PRINCIPAL
    ↓
AUTHENTICATED IDENTITY
    ↓
PROPOSED OPERATION
    ↓
CAPABILITY / TARGET / EFFECT CONTEXT
    ↓
AUTHORITY CANDIDATE DISCOVERY
    ↓
AUTHORITY IDENTITY VALIDATION
    ↓
ISSUER VALIDATION
    ↓
DELEGATION VALIDATION
    ↓
SCOPE RESOLUTION
    ↓
TEMPORAL / REGIME VALIDATION
    ↓
REVOCATION CHECK
    ↓
CONSTRAINT RESOLUTION
    ↓
AUTHORITY RESOLUTION
    ↓
AUTHORITY WITNESS
    ↓
POLICY + CAPABILITY + CONTROL-PLANE GATES
    ↓
COMMIT-TIME AUTHORITY REVALIDATION
    ↓
EFFECT ELIGIBILITY
```

The central invariant is:

> **AMOS authority is not inferred from identity, capability, access, policy permission, historical success, role labels, or agent confidence. Authority must be explicitly resolved from valid, scoped, current, provenance-bound authority evidence for the exact consequential operation being considered.**

Therefore:

```text
CAPABILITY
+
POLICY ALLOW
+
NO AUTHORITY
=
NO AUTHORIZED EFFECT
```

and:

```text
AUTHORITY
+
POLICY DENY
=
NO PERMITTED EFFECT
```

and:

```text
AUTHORITY
+
POLICY ALLOW
+
CAPABILITY
!=
COMMIT
```

because transaction, freshness, observability, effect-release, and other governing gates may still remain.

For mutable authority:

```text
PLAN-TIME AUTHORITY
        ↓
PREPARE
        ↓
COMMIT-TIME REVALIDATION
        ↓
CURRENT AUTHORITY
```

is required before consequential durable release where applicable.

AMOS MUST NOT create authority from missing evidence.

AMOS MUST NOT widen authority during delegation.

AMOS MUST NOT silently convert unknown scope into universal scope.

AMOS MUST NOT preserve authority after authoritative revocation.

AMOS MUST NOT treat a valid signature as sufficient evidence of current authority when expiry, revocation, issuer status, or delegation validity can change.

AMOS MUST NOT count copies or descendants of one authority source as independent authority.

AMOS MUST preserve unresolved authority conflicts.

AMOS SHOULD resolve to the smallest sufficient authority envelope.

AMOS SHOULD invalidate only dependent authority conclusions when one authority premise changes.

AMOS MUST preserve authority provenance sufficiently to reconstruct:

```text
who authorized whom;

for what;

over what;

through which delegation;

under which constraints;

for what period;

under which regime;

and on what evidence.
```

When those questions cannot be answered for a consequential operation, the correct authority state is:

```text
UNKNOWN/GAP
```

or, where applicable:

```text
CONFLICT

REVALIDATE

ESCALATE

DENIED

EXPIRED

REVOKED
```

—not `AUTHORIZED`.

Integrity remains prior to completeness, fluency, speed, convenience, and optimization.

---

# END — AUTHORITY_RESOLVER.md

```
```

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00_ROOT/00-Home]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: authority_resolver
node_type: note
path: 03_CONTROL_PLANE/04_AUTHORITY/AUTHORITY_RESOLVER.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_ROOT/00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
