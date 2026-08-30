---
title: AMOS OS Root Authorization
type: note
source: 00_ROOT
artifact: 00_ROOT_AUTHORIZATION.md
artifact_id: AMOS_AUTH_ROOT_000
origin_architect: Trang Phan
steward: Trang Phan
system: AMOS OS
domain: AUTHORIZATION / CONTROL PLANE
artifact_class: ROOT_AUTHORIZATION_SPECIFICATION
version: 1.0.0
updated: '2026-08-26'
status: PROPOSED_SPECIFICATION
epistemic_class: MODEL
canonical_status: UNKNOWN/GAP
implementation_status: UNKNOWN/GAP
validation_status: UNKNOWN/GAP
active_root_authority: UNBOUND
tags:
- note
- canon/root
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: root_index
---

# AMOS OS — 00 Root Authorization

## 0. Purpose

`00_ROOT_AUTHORIZATION.md` defines the highest-level authorization contract from which governed AMOS authority may be recognized, constrained, delegated, attenuated, revoked, witnessed, evaluated, and committed.

It establishes the architectural answer to:

> **What constitutes a valid root of authority inside AMOS OS, how may downstream authority derive from it, and what conditions prevent agents, Skills, policies, capabilities, workflows, models, or generated artifacts from manufacturing authority for themselves?**

This artifact defines:

- root authority identity;
- root authority admission;
- authority domains;
- authority scope;
- authority provenance;
- authority lineage;
- delegation roots;
- attenuation;
- authorization boundaries;
- authority witnesses;
- temporal validity;
- revocation;
- supersession;
- emergency authority;
- transaction binding;
- commit-time authority freshness;
- multi-principal authority;
- conflict handling;
- recovery;
- audit;
- and falsification conditions.

It does **not** itself designate a real active root authority unless a separately governed and provenance-bound root grant has been admitted.

Therefore:

```text
ROOT_AUTHORIZATION_SPEC
!=
ROOT_AUTHORITY_GRANT
```

---

# 1. Fundamental Boundary

AMOS SHALL distinguish:

```text
AUTHORITY SOURCE

AUTHORITY SPECIFICATION

AUTHORITY GRANT

AUTHORITY WITNESS

AUTHORIZATION DECISION

TRANSACTION

COMMIT
```

These are separate objects.

The governing chain is:

```text
LEGITIMATE AUTHORITY SOURCE
          ↓
ROOT AUTHORITY GRANT
          ↓
DELEGATION / ATTENUATION
          ↓
EFFECTIVE AUTHORITY
          ↓
AUTHORITY WITNESS
          ↓
ACTION-SPECIFIC AUTHORIZATION
          ↓
TRANSACTION
          ↓
COMMIT-TIME REVALIDATION
          ↓
COMMIT
```

No step may be silently skipped where it is required by the action's governance class.

---

# 2. Hard Authorization Laws

```text
CAPABILITY != AUTHORITY

IDENTITY != AUTHORITY

ROLE != AUTHORITY

OWNERSHIP CLAIM != AUTHORITY

POLICY != AUTHORITY

POLICY_ALLOW != AUTHORITY

SKILL != AUTHORITY

AGENT != AUTHORITY

MODEL != AUTHORITY

SYSTEM_ACCESS != AUTHORITY

KNOWLEDGE != AUTHORITY

CREDENTIAL_POSSESSION != UNLIMITED_AUTHORITY

DELEGATION != ROOT_AUTHORITY

AUTHORITY != AUTHORIZATION

AUTHORIZATION != COMMIT

PROPOSAL != COMMIT

PAST_AUTHORITY != CURRENT_AUTHORITY

EXPIRED_AUTHORITY != CURRENT_AUTHORITY

REVOKED_AUTHORITY != CURRENT_AUTHORITY

UNKNOWN_AUTHORITY != ALLOW

UNKNOWN/GAP != PASS
```

---

# 3. Root Authorization Definition

A **Root Authorization** is the highest recognized authorization basis inside a declared AMOS governance domain.

Formally, as an AMOS MODEL:

```text
RootAuthorization =
RecognizedPrincipal
∧ ValidAuthoritySource
∧ ExplicitAuthorityGrant
∧ DefinedScope
∧ DefinedEffectEnvelope
∧ DefinedConstraints
∧ TemporalValidity
∧ ProvenanceIntegrity
∧ GovernanceAdmissibility
```

If any mandatory term is unresolved:

```text
RootAuthorization = UNKNOWN/GAP
```

or:

```text
RootAuthorization = INVALID
```

depending on whether evidence is missing or contradictory.

---

# 4. Root Does Not Mean Unlimited

`ROOT` means:

> no higher AMOS authorization parent is required **within the declared authority domain**.

It does not mean:

```text
unlimited;

universal;

permanent;

irrevocable;

legally sovereign;

outside policy;

outside safety;

outside system invariants;

or authoritative over every domain.
```

Root authority remains bounded.

---

# 5. Root Authority Domains

AMOS MAY recognize multiple independent root domains.

Examples:

```text
CANON_AUTHORITY

SYSTEM_GOVERNANCE_AUTHORITY

DEPLOYMENT_AUTHORITY

DATA_AUTHORITY

MEMORY_AUTHORITY

POLICY_AUTHORITY

SECURITY_AUTHORITY

FINANCIAL_AUTHORITY

DISCLOSURE_AUTHORITY

TOOL_AUTHORITY

REPOSITORY_AUTHORITY

SKILL_PROMOTION_AUTHORITY

AGENT_PROMOTION_AUTHORITY

EMERGENCY_AUTHORITY
```

These domains MUST NOT be assumed mutually interchangeable.

---

# 6. Authority Domain Separation

Example:

```text
CANON_AUTHORITY
```

does not automatically imply:

```text
DEPLOYMENT_AUTHORITY
```

Likewise:

```text
REPOSITORY_WRITE_AUTHORITY
```

does not automatically imply:

```text
PRODUCTION_DEPLOYMENT_AUTHORITY
```

Therefore:

```text
AUTHORITY(domain_A)
!=
AUTHORITY(domain_B)
```

unless an explicit authority relation establishes otherwise.

---

# 7. Root Principal

A root principal is the identity to which a valid root authority grant is bound.

Typed representation:

```yaml
root_principal:
  principal_id: string

  principal_type:
    - HUMAN
    - ORGANIZATION
    - SERVICE
    - GOVERNED_SYSTEM
    - MULTI_PRINCIPAL
    - OTHER

  identity_evidence: []

  authority_domains: []

  provenance: {}

  status:
    - CANDIDATE
    - VERIFIED_IDENTITY
    - ACTIVE
    - SUSPENDED
    - REVOKED
    - SUPERSEDED
    - UNKNOWN/GAP
```

---

# 8. Identity Is Not Authority

Identity resolution answers:

> Who is this?

Authority resolution answers:

> What may this principal authorize?

Therefore:

```text
IDENTITY_VERIFIED
!=
AUTHORITY_VERIFIED
```

A perfectly authenticated principal may have zero authority over a requested effect.

---

# 9. Root Authority Grant

A root authority grant SHOULD be represented as a typed object.

```yaml
root_authority_grant:
  grant_id: string
  version: string

  principal_id: string

  authority_domain: string

  operations: []

  resources: []

  effect_classes: []

  recipients: []

  purposes: []

  jurisdictions: []

  environments: []

  constraints: []

  delegable: boolean

  delegation_constraints: []

  valid_from: timestamp
  valid_until: timestamp | null

  revocable: boolean

  revocation_authority: []

  issuer: {}

  authority_source: {}

  provenance: {}

  status:
    - PROPOSED
    - ACTIVE
    - SUSPENDED
    - EXPIRED
    - REVOKED
    - SUPERSEDED
    - UNKNOWN/GAP
```

---

# 10. Root Grant Admission

A proposed root authority grant MUST NOT become active merely because the file exists.

Admission path:

```text
ROOT GRANT PROPOSAL
        ↓
SOURCE VALIDATION
        ↓
PRINCIPAL IDENTITY VALIDATION
        ↓
AUTHORITY-BASIS VALIDATION
        ↓
SCOPE VALIDATION
        ↓
CONSTRAINT VALIDATION
        ↓
PROVENANCE VALIDATION
        ↓
CONFLICT CHECK
        ↓
GOVERNANCE APPROVAL
        ↓
COMMIT
        ↓
ACTIVE ROOT GRANT
```

---

# 11. Root Authority Sources

The source of authority MUST be explicit.

Potential source classes include:

```text
SYSTEM_OWNER_GRANT

HUMAN_USER_GRANT

ORGANIZATIONAL_CHARTER

LEGAL_AUTHORITY

CONTRACTUAL_AUTHORITY

PLATFORM_AUTHORITY

CANON_STEWARDSHIP

RESOURCE_OWNERSHIP

GOVERNANCE_DECISION

MULTI_PRINCIPAL_APPROVAL

EXTERNAL_AUTHORITY_BINDING
```

These classes are not automatically equivalent.

---

# 12. Authority Source Object

```yaml
authority_source:
  source_id: string

  source_type: string

  issuer: string

  subject: string

  domain: string

  authority_basis: string

  source_reference: []

  effective_at: timestamp

  expires_at: timestamp | null

  provenance: {}

  validation:
    state:
      - VERIFIED
      - CONDITIONAL
      - UNKNOWN/GAP
      - INVALID
```

---

# 13. Root Authority Provenance

Every active root authority SHOULD preserve:

```text
WHO granted it

WHAT authorized the grant

WHEN it became effective

WHAT scope it covers

WHAT constraints apply

WHETHER it may delegate

HOW it may be revoked

WHAT version is current

WHAT supersedes it

WHAT evidence supports it
```

---

# 14. Root Authority Lineage

Conceptually:

```text
AUTHORITY SOURCE
      │
      ▼
ROOT GRANT R0
      │
      ├── DELEGATION D1
      │       │
      │       ▼
      │   PRINCIPAL P1
      │
      └── DELEGATION D2
              │
              ▼
          PRINCIPAL P2
```

Every downstream authority SHOULD remain traceable to a valid root path.

---

# 15. Authority Path

An authority path is:

```text
R0 → D1 → D2 → ... → Principal
```

A valid path requires every edge to be valid.

AMOS MODEL:

```text
ValidAuthorityPath(P)
=
Valid(R0)
∧ Valid(D1)
∧ Valid(D2)
∧ ...
∧ Valid(Dn)
```

One failed load-bearing edge invalidates that path.

---

# 16. Multiple Authority Paths

A principal MAY possess multiple independent authority paths.

Example:

```text
ROOT A
  ↓
D1
  ↓
PRINCIPAL X

ROOT B
  ↓
D2
  ↓
PRINCIPAL X
```

Revocation of `D1` does not necessarily invalidate `D2`.

Therefore invalidation MUST be dependency-aware.

---

# 17. Provenance Independence

Two authority paths MUST NOT be considered independent merely because they have different identifiers.

Example:

```text
ROOT A
 ↓
D1
 ├── D2
 └── D3
```

`D2` and `D3` share ancestry.

They cannot be treated as independent root confirmation.

---

# 18. Delegation Law

Delegated authority MUST NOT exceed its parent.

AMOS MODEL:

```text
A_child ⊆ A_parent
```

More precisely:

```text
EffectiveChildAuthority
=
ParentAuthority
∩ DelegationGrant
∩ CurrentConstraints
```

---

# 19. Delegation Attenuation

Delegation MAY reduce:

```text
operations;

resources;

effect classes;

recipients;

purpose;

time;

budget;

geography;

environment;

tool set;

delegation depth;

disclosure level;

risk level.
```

It MUST NOT silently expand them.

---

# 20. Delegation Depth

A root grant MAY specify:

```yaml
delegation:
  allowed: true
  max_depth: 3
```

Then:

```text
R0 → D1 → D2 → D3
```

may be valid while:

```text
R0 → D1 → D2 → D3 → D4
```

is invalid.

---

# 21. Non-Delegable Authority

Some authority MAY be explicitly:

```text
NON_DELEGABLE
```

Examples could include:

```text
root canon supersession;

root security override;

destructive production action;

high-impact disclosure;

root policy replacement.
```

Whether any concrete authority is non-delegable requires the applicable source.

---

# 22. Authority Scope

Every root grant MUST define its applicability envelope.

Recommended scope dimensions:

```yaml
scope:
  systems: []
  domains: []
  environments: []
  resources: []
  operations: []
  effect_classes: []
  recipients: []
  purposes: []
  jurisdictions: []
  risk_classes: []
```

Missing scope MUST NOT automatically mean unlimited scope.

Preferred default:

```text
UNSPECIFIED_SCOPE
→ UNKNOWN/GAP
```

not:

```text
UNSPECIFIED_SCOPE
→ ALL
```

---

# 23. Effect Binding

Authority SHOULD bind to effects, not only tool names.

Example:

```text
"send_email"
```

is insufficiently expressive if authority depends on:

```text
recipient;

content class;

data sensitivity;

purpose;

volume;

external disclosure.
```

Therefore authorization should evaluate semantic effect where possible.

---

# 24. Operation vs Effect

```text
OPERATION
=
mechanism used

EFFECT
=
state or consequence produced
```

Example:

```text
operation:
  upload_file

effect:
  external_disclosure_of_confidential_data
```

A permitted operation MUST NOT be used to create a prohibited effect.

---

# 25. Purpose Binding

Authority MAY be purpose-limited.

Example:

```yaml
purpose:
  allow:
    - SECURITY_INCIDENT_RESPONSE
  deny:
    - GENERAL_ANALYTICS
```

The same operation may therefore be authorized in one purpose context and prohibited in another.

---

# 26. Recipient Binding

Authority MAY constrain recipients.

```yaml
recipients:
  allow:
    - INTERNAL_SECURITY_TEAM

  deny:
    - PUBLIC
```

Recipient changes MAY invalidate prior authorization.

---

# 27. Resource Binding

Authority MAY bind to:

```text
specific file;

repository;

database;

folder;

service;

tenant;

account;

environment;

namespace;

data class.
```

Authority over resource `A` MUST NOT imply authority over resource `B`.

---

# 28. Temporal Binding

Every authority grant SHOULD define:

```text
valid_from

valid_until
```

or explicitly establish an open-ended validity rule.

Authority validity is evaluated at relevant decision time.

---

# 29. Commit-Time Authority

For mutable authority:

```text
AUTHORIZED_AT_PROPOSAL_TIME
```

does not guarantee:

```text
AUTHORIZED_AT_COMMIT_TIME
```

Therefore consequential transactions SHOULD support commit-time authority revalidation.

---

# 30. Authority Freshness

An authority witness SHOULD carry freshness information.

```yaml
freshness:
  evaluated_at: timestamp
  state_version: string
  valid_until: timestamp | null
  revalidation_required_after: duration | null
```

---

# 31. Authority Witness

An authority witness records the evidence used to establish effective authority.

```yaml
authority_witness:
  witness_id: string

  principal_id: string

  requested_action: {}

  authority_domain: string

  root_grants: []

  delegation_paths: []

  revocation_checks: []

  applicable_constraints: []

  state_versions: []

  generated_at: timestamp

  valid_until: timestamp | null

  provenance: {}

  result:
    - VALID
    - CONDITIONAL
    - INVALID
    - UNKNOWN/GAP
```

---

# 32. Witness Is Not Authority

An authority witness is evidence about authority.

It is not itself the authority source.

```text
AUTHORITY_WITNESS
!=
AUTHORITY_GRANT
```

Destroying a witness does not necessarily revoke authority.

Revoking authority should invalidate dependent witnesses.

---

# 33. Authorization Request

```yaml
authorization_request:
  request_id: string

  principal_id: string

  operation: string

  resource: {}

  effect: {}

  recipient: {}

  purpose: {}

  environment: {}

  requested_at: timestamp

  transaction_id: string | null

  provenance: {}
```

---

# 34. Root Authorization Evaluation

Conceptually:

```text
REQUEST
  ↓
RESOLVE PRINCIPAL
  ↓
RESOLVE ROOT PATHS
  ↓
VALIDATE ROOT GRANTS
  ↓
VALIDATE DELEGATIONS
  ↓
CHECK REVOCATIONS
  ↓
CHECK TEMPORAL VALIDITY
  ↓
CHECK SCOPE
  ↓
CHECK PURPOSE
  ↓
CHECK RESOURCE
  ↓
CHECK EFFECT
  ↓
CHECK RECIPIENT
  ↓
CHECK CONSTRAINTS
  ↓
BUILD AUTHORITY WITNESS
```

---

# 35. Effective Authority

AMOS MODEL:

```text
EffectiveAuthority(P,t)
=
Union(
  ValidAuthorityPaths(P,t)
)
∩
CurrentConstraints(t)
```

However, union MUST NOT permit semantic reconstruction of a prohibited effect unless composition is explicitly permitted.

---

# 36. Authority Composition

Two narrow grants MAY sometimes combine.

Example:

```text
Grant A:
READ resource X

Grant B:
WRITE resource Y
```

This does not automatically imply:

```text
COPY X → Y
```

because the combined effect may constitute a separate disclosure capability.

Therefore:

```text
LOCAL_PERMISSION_A
+
LOCAL_PERMISSION_B
!=
AUTOMATIC_COMPOSITE_PERMISSION
```

---

# 37. Cross-Grant Composition Guard

Before combining grants:

```text
identify semantic origin;

identify destination;

identify transformed information;

identify cumulative effect;

check composition policy;

check disclosure boundary;

check authority source compatibility.
```

---

# 38. Root Policy Interaction

Root authority remains subject to applicable policy unless the authority grant explicitly and validly includes policy-override authority.

Therefore:

```text
ROOT_AUTHORITY
!=
AUTOMATIC_POLICY_OVERRIDE
```

---

# 39. Policy Cannot Manufacture Root Authority

Policy may:

```text
allow;

deny;

constrain;

escalate;

require approval.
```

Policy cannot independently manufacture authority where no valid authority source exists.

```text
NO_AUTHORITY
+
POLICY_ALLOW
=
NO_AUTHORITY
```

---

# 40. Capability Interaction

A principal may have authority but lack capability.

```text
AUTHORIZED
∧
CAPABILITY_UNAVAILABLE
→
NO_EXECUTION
```

Likewise:

```text
CAPABILITY_AVAILABLE
∧
NOT_AUTHORIZED
→
NO_EXECUTION
```

---

# 41. Root Authorization Decision Function

AMOS MODEL:

```text
Authorize(action)
=
IdentityValid
∧ CapabilityEligible
∧ AuthorityValid
∧ ScopeCompatible
∧ PolicyCompatible
∧ ConstraintsSatisfied
∧ FreshnessValid
∧ TransactionEligible
```

Failure of a hard condition is non-compensatory.

---

# 42. Authorization Outcomes

```text
ALLOW

ALLOW_WITH_CONSTRAINTS

DENY

REVALIDATE

ESCALATE

BLOCK_CONFLICT

UNKNOWN/GAP
```

`UNKNOWN/GAP` MUST NOT be converted to `ALLOW` merely to preserve workflow continuity.

---

# 43. Default-Deny Boundary

For governed consequential actions:

```text
AUTHORITY_NOT_ESTABLISHED
→
DO_NOT_COMMIT
```

This does not require every low-impact informational operation to use the same governance depth.

Governance intensity SHOULD scale with consequence and irreversibility.

---

# 44. Root Revocation

Root authority MAY be revocable according to its source contract.

A root revocation object SHOULD contain:

```yaml
root_revocation:
  revocation_id: string

  target_grant_id: string

  revoker: string

  revocation_authority: {}

  effective_at: timestamp

  reason: string | null

  scope: {}

  provenance: {}

  status:
    - PROPOSED
    - ACTIVE
    - REJECTED
    - UNKNOWN/GAP
```

---

# 45. Root Revocation Propagation

```text
ROOT GRANT REVOKED
        ↓
DIRECT DELEGATIONS INVALIDATED
        ↓
DESCENDANT AUTHORITY PATHS INVALIDATED
        ↓
AUTHORITY WITNESSES INVALIDATED
        ↓
CACHED AUTHORIZATIONS INVALIDATED
        ↓
PENDING TRANSACTIONS REVALIDATED
```

---

# 46. Selective Revocation

If a principal has:

```text
Path A
Path B
```

and only `Path A` is revoked:

```text
invalidate(Path A descendants)
```

but preserve:

```text
Path B
```

if independently valid.

---

# 47. Partial Revocation

A revocation MAY narrow authority rather than eliminate it.

Example:

```text
BEFORE:
READ + WRITE + DELETE

AFTER:
READ
```

This MUST produce a new effective authority state.

---

# 48. Root Suspension

Suspension differs from revocation.

```text
SUSPENSION
=
temporarily unusable authority

REVOCATION
=
authority withdrawal according to revocation semantics
```

Suspended authority MUST NOT authorize new commits.

---

# 49. Root Expiration

At:

```text
t >= valid_until
```

the grant becomes:

```text
EXPIRED
```

unless valid renewal/supersession exists.

Expired authority MUST NOT silently renew itself.

---

# 50. Root Supersession

Root authority may be replaced:

```text
ROOT_GRANT_v1
      ↓
SUPERSEDED_BY
      ↓
ROOT_GRANT_v2
```

The previous grant remains in historical provenance.

---

# 51. Supersession Rule

Supersession MUST specify whether:

```text
existing delegations survive;

existing witnesses survive;

existing authorizations survive;

pending transactions survive.
```

Defaulting these silently is unsafe.

---

# 52. Root Rotation

Credential or key rotation MUST be distinguished from authority supersession.

```text
KEY_ROTATION
!=
AUTHORITY_CHANGE
```

A principal may retain identical authority while authentication material changes.

---

# 53. Root Credential Boundary

Credentials prove or support identity/control.

They do not define unlimited authority.

```text
VALID_SIGNATURE
!=
UNLIMITED_PERMISSION
```

A valid signature from a root principal still requires scope evaluation.

---

# 54. Multi-Principal Root Authority

Some root actions MAY require multiple principals.

Example MODEL:

```yaml
approval:
  mode: THRESHOLD
  required: 2
  eligible_principals:
    - P1
    - P2
    - P3
```

Then:

```text
2-of-3
```

valid independent approvals are required.

---

# 55. Multi-Principal Independence

Threshold approval MUST account for common control.

Three credentials controlled by one principal do not necessarily constitute three independent approvals.

Therefore:

```text
KEY_COUNT
!=
PRINCIPAL_INDEPENDENCE
```

---

# 56. Root Conflict

Conflicting root grants MAY occur.

Example:

```text
ROOT A → ALLOW operation X

ROOT B → DENY operation X
```

AMOS MUST NOT silently choose whichever result is more convenient.

Possible resolution:

```text
PRECEDENCE RULE

DOMAIN RULE

SCOPE RULE

TEMPORAL RULE

MORE_RESTRICTIVE_RULE

MULTI-PRINCIPAL RESOLUTION

ESCALATION

BLOCK_CONFLICT
```

---

# 57. Root Precedence

Precedence MUST be explicit.

Potential dimensions:

```text
constitutional level;

domain specificity;

resource ownership;

jurisdiction;

time;

version;

emergency state;

supersession lineage.
```

No generic precedence hierarchy should be invented where source canon is absent.

---

# 58. Root Authority Registry

Root grants SHOULD be discoverable through an authoritative registry.

```yaml
root_authority_registry:
  registry_id: string
  version: string

  grants: []
  suspensions: []
  revocations: []
  supersessions: []

  state_version: string

  provenance: {}
```

---

# 59. Registry Integrity

The root registry SHOULD protect against:

```text
unauthorized mutation;

rollback;

split views;

stale replicas;

silent deletion;

duplicate identity;

forged grants;

forged revocations;

version confusion.
```

---

# 60. Registry Versioning

Every consequential authority evaluation SHOULD identify the authority-state version used.

Example:

```text
authority_state_version = AUTH-EPOCH-391
```

This permits commit-time detection of authority changes.

---

# 61. Authority Epoch

An authority epoch is a logical version of relevant authorization state.

Conceptually:

```text
E0
 ↓ authority change
E1
 ↓ revocation
E2
 ↓ delegation
E3
```

A transaction validated under `E1` may require revalidation before commit under `E3`.

---

# 62. Commit-Time Authority Check

```text
transaction.authority_epoch
==
current.authority_epoch
```

may permit fast-path continuation if all other freshness conditions remain valid.

If:

```text
transaction.authority_epoch
!=
current.authority_epoch
```

then:

```text
REVALIDATE
```

unless deterministic dependency analysis proves the change irrelevant.

---

# 63. Fine-Grained Read Set

A transaction SHOULD record the exact authority objects it depended upon.

Example:

```yaml
authority_read_set:
  - object: ROOT_GRANT_01
    version: 7

  - object: DELEGATION_44
    version: 3

  - object: REVOCATION_INDEX
    version: 98
```

This enables selective rather than global revalidation.

---

# 64. Authority Dependency Closure

For action `A`:

```text
AuthorityDependencies(A)
=
root grant
+
delegation chain
+
revocation state
+
scope constraints
+
policy dependencies
+
temporal state
```

Only changes that can alter the authorization result need invalidate the transaction.

---

# 65. Root Authorization and Transactions

A transaction SHOULD bind:

```text
principal;

requested effect;

authority witness;

policy decision;

authority read set;

authority epoch;

constraint state;

resource versions.
```

---

# 66. Proposal Boundary

Agents and models may produce:

```text
ROOT_AUTHORITY_PROPOSAL
```

They MUST NOT produce:

```text
ACTIVE_ROOT_AUTHORITY
```

solely by generation.

Activation requires the applicable governance process.

---

# 67. Agent Boundary

An agent cannot make itself root.

```text
AGENT_SELF_DECLARATION
!=
ROOT_AUTHORITY
```

Likewise:

```text
AGENT_SPAWN
```

cannot manufacture new authority.

---

# 68. Child-Agent Law

For parent agent `P` and child `C`:

```text
Authority(C)
⊆
DelegableAuthority(P)
```

unless `C` possesses an independent external authority path.

---

# 69. Skill Boundary

A Skill cannot manufacture root authority.

```text
SKILL_INSTALLED
!=
SKILL_AUTHORIZED
```

and:

```text
SKILL_CAN_EXECUTE
!=
SKILL_MAY_COMMIT
```

---

# 70. Workflow Boundary

A workflow cannot inherit more authority than its participating principals and explicit workflow grants provide.

```text
WorkflowAuthority
⊆
AuthorizedComposition(
  participant authorities
)
```

---

# 71. Tool Boundary

Tool access is capability.

```text
TOOL_VISIBLE
!=
TOOL_AUTHORIZED
```

```text
TOOL_CONNECTED
!=
TOOL_AUTHORIZED
```
```text
TOOL_CALL_SUCCEEDED
!=
ACTION_WAS_AUTHORIZED
```
---

# 72. Memory Boundary

Stored root-authority information MUST NOT be trusted merely because it exists in memory.

Authority-related memory SHOULD be checked against current authoritative state.

```text
MEMORY("P has authority")
!=
CURRENT_AUTHORITY(P)
```

---

# 73. Cached Authorization

Cached authorization MAY be reused only while its dependencies remain valid.

Cache object:

```yaml
authorization_cache:
  decision_id: string

  dependency_versions: []

  authority_epoch: string

  created_at: timestamp

  expires_at: timestamp

  invalidation_conditions: []
```

---

# 74. Cache Invalidation

Invalidate cached authorization when load-bearing state changes, including:

```text
root grant;

delegation;

revocation;

policy;

scope;

recipient;

resource;

purpose;

constraint;

environment;

transaction state.
```

---

# 75. Emergency Root Authority

Emergency authority MUST be explicit and bounded.

Recommended fields:

```yaml
emergency_authority:
  emergency_id: string

  trigger: {}

  authority: {}

  principal: string

  scope: {}

  allowed_effects: []

  prohibited_effects: []

  valid_from: timestamp
  valid_until: timestamp

  audit_required: true

  post_event_review_required: true
```

---

# 76. Emergency Authority Law

```text
EMERGENCY
!=
UNLIMITED_AUTHORITY
```

Emergency authority SHOULD be:

```text
narrow;

temporary;

auditable;

revocable;

purpose-bound;

automatically expiring.
```

---

# 77. Break-Glass Authority

Break-glass procedures SHOULD require:

```text
explicit activation;

strong identity;

reason capture;

scope limitation;

enhanced logging;

automatic expiration;

post-action review.
```

Break-glass state MUST NOT silently become normal authority.

---

# 78. Root Authorization State Machine

```text
PROPOSED
   ↓
VALIDATING
   ↓
APPROVED
   ↓
ACTIVE
   ├────────→ SUSPENDED
   │              ↓
   │           ACTIVE
   │
   ├────────→ EXPIRED
   │
   ├────────→ REVOKED
   │
   └────────→ SUPERSEDED
```

Invalid paths MUST be rejected.

---

# 79. Root Grant State

```yaml
root_authorization_state:
  grant_id: string

  state:
    - PROPOSED
    - VALIDATING
    - APPROVED
    - ACTIVE
    - SUSPENDED
    - EXPIRED
    - REVOKED
    - SUPERSEDED
    - INVALID
    - UNKNOWN/GAP

  state_version: integer

  changed_at: timestamp

  changed_by: string

  provenance: {}
```

---

# 80. Core Invariants

## AUTH-ROOT-INV-001 — No Self-Authorization

No component may manufacture root authority for itself.

## AUTH-ROOT-INV-002 — Source Requirement

Every active root authority requires an identifiable authority source.

## AUTH-ROOT-INV-003 — Principal Binding

Every active root authority must bind to a resolvable principal.

## AUTH-ROOT-INV-004 — Scope Requirement

Root authority must have a defined or explicitly governed scope.

## AUTH-ROOT-INV-005 — Capability Separation

Capability does not confer authority.

## AUTH-ROOT-INV-006 — Policy Separation

Policy does not manufacture authority.

## AUTH-ROOT-INV-007 — Delegation Attenuation

Delegation cannot exceed delegable parent authority.

## AUTH-ROOT-INV-008 — Revocation Propagation

Revoked authority invalidates dependent paths.

## AUTH-ROOT-INV-009 — Temporal Validity

Expired authority cannot authorize new commits.

## AUTH-ROOT-INV-010 — Provenance

Material authority state must preserve provenance.

---

# 81. Extended Invariants

## AUTH-ROOT-INV-011

A valid credential does not imply unlimited authority.

## AUTH-ROOT-INV-012

A valid root grant in one domain does not imply root authority in another.

## AUTH-ROOT-INV-013

Unknown authority fails closed for consequential effects.

## AUTH-ROOT-INV-014

Agent creation cannot expand authority.

## AUTH-ROOT-INV-015

Skill composition cannot expand authority.

## AUTH-ROOT-INV-016

Workflow composition cannot silently expand authority.

## AUTH-ROOT-INV-017

Authority composition must evaluate cumulative semantic effect.

## AUTH-ROOT-INV-018

A witness must bind to authority-state versions.

## AUTH-ROOT-INV-019

Stale witnesses cannot authorize changed authority state without revalidation.

## AUTH-ROOT-INV-020

Root supersession preserves historical lineage.

---

# 82. Transaction Invariants

## AUTH-ROOT-INV-021

Authorization is action-specific.

## AUTH-ROOT-INV-022

Authorization does not equal commit.

## AUTH-ROOT-INV-023

Mutable authority must remain valid at the required finalization point.

## AUTH-ROOT-INV-024

Authority changes invalidate only dependent transactions where dependency closure is known.

## AUTH-ROOT-INV-025

Partial authoritative updates must not expose impossible intermediate authority states.

## AUTH-ROOT-INV-026

Revocation races must fail safely.

## AUTH-ROOT-INV-027

Policy races must trigger appropriate revalidation.

## AUTH-ROOT-INV-028

Resource-scope changes may invalidate authorization.

## AUTH-ROOT-INV-029

Recipient changes may invalidate authorization.

## AUTH-ROOT-INV-030

Effect changes require authorization re-evaluation.

---

# 83. Governance Invariants

## AUTH-ROOT-INV-031

Root authority modification requires authority to modify root authority.

## AUTH-ROOT-INV-032

Root revocation requires valid revocation authority.

## AUTH-ROOT-INV-033

Emergency authority cannot silently become permanent.

## AUTH-ROOT-INV-034

Root registry rollback must be detectable.

## AUTH-ROOT-INV-035

Conflicting root authority cannot silently resolve through convenience.

## AUTH-ROOT-INV-036

Threshold approval requires genuine principal independence where independence is a requirement.

## AUTH-ROOT-INV-037

Generated text cannot create authority.

## AUTH-ROOT-INV-038

Repository presence cannot create authority.

## AUTH-ROOT-INV-039

Placeholder replacement cannot create authority.

## AUTH-ROOT-INV-040

Canonical admission and runtime activation remain separate.

---

# 84. Root Authorization Protocol

```text
AUTH_REQUEST
      ↓
IDENTITY_RESOLVER
      ↓
ROOT_AUTHORITY_REGISTRY
      ↓
AUTHORITY_RESOLVER
      ↓
DELEGATION_RESOLVER
      ↓
REVOCATION_RESOLVER
      ↓
SCOPE_EVALUATOR
      ↓
AUTHORITY_WITNESS
      ↓
POLICY_ENGINE
      ↓
AUTHORIZATION_ENGINE
      ↓
TRANSACTION_MANAGER
      ↓
COMMIT_GUARD
```

---

# 85. Root Resolution Protocol

Input:

```yaml
resolve_root_authority:
  principal_id: string
  action: {}
  resource: {}
  effect: {}
  purpose: {}
  recipient: {}
  timestamp: timestamp
```

Output:

```yaml
root_authority_resolution:
  principal_id: string

  valid_paths: []

  invalid_paths: []

  unresolved_paths: []

  effective_authority: {}

  conflicts: []

  witness: {}

  result:
    - VALID
    - CONDITIONAL
    - INVALID
    - UNKNOWN/GAP
```

---

# 86. Failure Modes

```text
FM-ROOT-001 self-authorized root

FM-ROOT-002 fabricated authority source

FM-ROOT-003 unresolved principal

FM-ROOT-004 unlimited scope inferred from missing scope

FM-ROOT-005 capability interpreted as authority

FM-ROOT-006 role interpreted as authority

FM-ROOT-007 policy interpreted as authority

FM-ROOT-008 credential interpreted as unlimited authority

FM-ROOT-009 delegation exceeds parent

FM-ROOT-010 delegation depth exceeded

FM-ROOT-011 revoked root still active

FM-ROOT-012 revoked descendant still active

FM-ROOT-013 expired root still active

FM-ROOT-014 stale witness replay

FM-ROOT-015 stale authorization replay

FM-ROOT-016 root registry rollback

FM-ROOT-017 forged root grant

FM-ROOT-018 forged revocation

FM-ROOT-019 conflicting root grants silently merged

FM-ROOT-020 root domain leakage
```

---

# 87. Additional Failure Modes

```text
FM-ROOT-021 cross-resource authority leakage

FM-ROOT-022 cross-purpose authority leakage

FM-ROOT-023 cross-recipient authority leakage

FM-ROOT-024 cross-environment authority leakage

FM-ROOT-025 semantic-effect laundering

FM-ROOT-026 operation-level permission bypass

FM-ROOT-027 Skill-chain authority laundering

FM-ROOT-028 agent-spawn authority laundering

FM-ROOT-029 workflow authority laundering

FM-ROOT-030 policy override without authority

FM-ROOT-031 emergency authority persists after expiry

FM-ROOT-032 break-glass used without audit

FM-ROOT-033 common-controller approvals counted independent

FM-ROOT-034 key rotation interpreted as authority grant

FM-ROOT-035 superseded root reused

FM-ROOT-036 cached authority survives relevant revocation

FM-ROOT-037 transaction commits after authority change

FM-ROOT-038 unknown authority treated as allow

FM-ROOT-039 generated artifact treated as authority

FM-ROOT-040 placeholder promoted directly to active authority
```

---

# 88. Adversarial Cases

The authorization system SHOULD explicitly test:

```text
forged root grant;

forged issuer;

stolen root credential;

stale signature;

replayed witness;

replayed authorization;

registry rollback;

split-view registry;

delegation-cycle attack;

delegation-depth bypass;

scope wildcard injection;

recipient alias attack;

resource alias attack;

purpose relabeling;

semantic-effect splitting;

Skill-chain laundering;

agent-chain laundering;

cross-session authority leakage;

emergency-mode persistence;

revocation race;

commit race;

policy race;

multi-principal Sybil approval.
```

---

# 89. Repair / Recovery

When root authority integrity fails:

```text
DETECT
 ↓
FREEZE AFFECTED AUTHORITY PATH
 ↓
IDENTIFY ROOT / DELEGATION DEPENDENCIES
 ↓
QUARANTINE AFFECTED WITNESSES
 ↓
INVALIDATE DEPENDENT AUTHORIZATIONS
 ↓
REVALIDATE PENDING TRANSACTIONS
 ↓
RESTORE AUTHORITATIVE STATE
 ↓
REBUILD MINIMAL DEPENDENCY CLOSURE
 ↓
AUDIT
 ↓
RESUME
```

---

# 90. Root Compromise Recovery

If root credentials are suspected compromised:

```text
SUSPEND CREDENTIAL USE
      ↓
PRESERVE EVIDENCE
      ↓
DETERMINE AUTHORITY VS CREDENTIAL IMPACT
      ↓
ROTATE CREDENTIALS
      ↓
REVALIDATE ROOT IDENTITY
      ↓
REVIEW ACTIONS DURING COMPROMISE WINDOW
      ↓
REVOKE INVALID DERIVATIONS
      ↓
REPAIR DEPENDENT STATE
```

Credential compromise does not automatically prove every authority action was invalid, but it destroys the assumption that credential possession alone establishes trustworthy control during the affected interval.

---

# 91. Root Registry Recovery

Recovery SHOULD preserve:

```text
last known valid state;

subsequent mutations;

signatures / provenance;

revocation events;

supersession events;

transaction dependencies;

audit history.
```

Do not restore an old registry snapshot without checking whether doing so resurrects revoked authority.

---

# 92. Validators

Minimum validators:

```text
validate_root_grant_schema

validate_root_principal

validate_authority_source

validate_root_domain

validate_scope

validate_effect_envelope

validate_temporal_validity

validate_delegability

validate_delegation_depth

validate_delegation_attenuation

validate_revocation_authority

validate_revocation_state

validate_supersession

validate_authority_path

validate_provenance

validate_authority_epoch

validate_witness_freshness

validate_transaction_authority

validate_threshold_independence

validate_emergency_authority

validate_root_registry_integrity
```

---

# 93. Tests

```text
T-ROOT-001 valid root grant accepted

T-ROOT-002 missing authority source rejected

T-ROOT-003 unknown principal rejected

T-ROOT-004 missing scope does not become wildcard

T-ROOT-005 capability cannot create root authority

T-ROOT-006 policy cannot create root authority

T-ROOT-007 agent cannot self-authorize

T-ROOT-008 Skill cannot self-authorize

T-ROOT-009 child delegation cannot exceed parent

T-ROOT-010 delegation depth enforced

T-ROOT-011 expired grant rejected

T-ROOT-012 revoked grant rejected

T-ROOT-013 suspended grant rejected

T-ROOT-014 superseded grant rejected when no longer valid

T-ROOT-015 valid independent authority path preserved

T-ROOT-016 dependent path invalidated

T-ROOT-017 stale witness rejected

T-ROOT-018 fresh witness accepted

T-ROOT-019 authority epoch change triggers revalidation

T-ROOT-020 irrelevant authority change permits selective fast path
```

---

# 94. Extended Tests

```text
T-ROOT-021 resource scope enforced

T-ROOT-022 recipient scope enforced

T-ROOT-023 purpose scope enforced

T-ROOT-024 effect scope enforced

T-ROOT-025 environment scope enforced

T-ROOT-026 operation permission cannot launder prohibited effect

T-ROOT-027 Skill composition cannot enlarge authority

T-ROOT-028 agent spawn cannot enlarge authority

T-ROOT-029 workflow composition cannot enlarge authority

T-ROOT-030 revocation invalidates dependent witness

T-ROOT-031 revocation invalidates cached authorization

T-ROOT-032 root registry rollback detected

T-ROOT-033 conflicting roots produce conflict state

T-ROOT-034 threshold approval succeeds at threshold

T-ROOT-035 threshold approval fails below threshold

T-ROOT-036 common-controller approvals fail independence requirement

T-ROOT-037 emergency authority expires automatically

T-ROOT-038 break-glass event generates audit requirement

T-ROOT-039 transaction blocked after relevant authority mutation

T-ROOT-040 UNKNOWN/GAP never returns ALLOW
```

---

# 95. Falsifiers

The root authorization architecture is falsified for its declared scope if any of the following are possible:

```text
an agent can declare itself root and gain authority;

a Skill can manufacture authority through installation;

policy ALLOW creates authority without an authority source;

a child delegation exceeds the parent authority;

revoked authority can still commit without an independent valid path;

expired authority can authorize a new action;

missing scope becomes universal scope;

a stale authority witness survives a relevant revocation;

a transaction commits against authority state known to have materially changed;

root registry rollback silently resurrects revoked authority;

multiple aliases of one principal satisfy an independence threshold;

or UNKNOWN/GAP is treated as authorization.
```

---

# 96. RSCF

```yaml
rscf:
  claim:
    id: "AMOS_ROOT_AUTHORIZATION_SPEC"
    class: MODEL

    text: >
      AMOS root authorization is a provenance-bound, scoped,
      temporally valid and governance-admitted authority root from
      which downstream authority may derive only through valid,
      non-expansive delegation and which remains separate from
      capability, policy, identity, authorization decisions and commit.

  premises:
    - authority_requires_source
    - root_authority_is_domain_bounded
    - delegation_cannot_expand_authority
    - revocation_invalidates_dependents
    - authority_may_change_over_time
    - authorization_is_action_specific
    - commit_requires_current_authority_when_mutable

  evidence: []

  provenance:
    origin_architect: "Trang Phan"
    artifact: "00_ROOT_AUTHORIZATION.md"

  scope:
    system: "AMOS OS"
    subsystem: "Authorization / Control Plane"

  regime:
    - ARCHITECTURE
    - GOVERNANCE_MODEL

  dependencies:
    - AUTHORITY_RESOLVER
    - AUTHORITY_WITNESS
    - AUTHORIZATION_SPEC
    - DELEGATION
    - REVOCATION
    - POLICY_ENGINE
    - POLICY_REGISTRY
    - CAPABILITY_CONTRACT
    - CAPABILITY_MANIFEST
    - TRANSACTION_CONTROL
    - COMMIT_CONTROL
    - PROVENANCE

  competing:
    - capability_based_authority
    - role_based_authority
    - policy_only_authorization
    - agent_self_authorization
    - static_authorization_without_commit_revalidation

  falsifiers:
    - self_authorization_succeeds
    - delegation_expands_authority
    - revoked_authority_commits
    - stale_witness_commits
    - unknown_authority_allows_action

  confidence_ceiling: 0
```

---

# 97. Current Root Binding State

This specification MUST NOT fabricate a concrete active root principal.

Therefore the current safe state is:

```yaml
current_root_binding:
  principal: UNKNOWN/GAP
  authority_source: UNKNOWN/GAP
  root_grant: UNKNOWN/GAP
  authority_domains: UNKNOWN/GAP
  effective_from: UNKNOWN/GAP
  revocation_authority: UNKNOWN/GAP
  validation_evidence: []
  status: UNBOUND
```

This means:

```text
SPECIFICATION EXISTS
```

but:

```text
ACTIVE ROOT AUTHORITY NOT ESTABLISHED BY THIS ARTIFACT
```

---

# 98. Gap Status

```yaml
gap_status:

  ROOT_AUTHORIZATION_ARCHITECTURE:
    state: COMPLETE_FOR_SCOPE

  ROOT_PRINCIPAL_BINDING:
    state: UNKNOWN/GAP
    severity: CRITICAL_FOR_RUNTIME_AUTHORITY

  ROOT_AUTHORITY_SOURCE:
    state: UNKNOWN/GAP
    severity: CRITICAL_FOR_RUNTIME_AUTHORITY

  ROOT_GRANT:
    state: UNKNOWN/GAP
    severity: CRITICAL_FOR_RUNTIME_AUTHORITY

  ROOT_REGISTRY_IMPLEMENTATION:
    state: UNKNOWN/GAP

  AUTHORITY_RESOLVER_IMPLEMENTATION:
    state: UNKNOWN/GAP

  REVOCATION_IMPLEMENTATION:
    state: UNKNOWN/GAP

  COMMIT_TIME_REVALIDATION:
    state: UNKNOWN/GAP

  EXECUTED_TESTS:
    state: UNKNOWN/GAP

  SECURITY_VALIDATION:
    state: UNKNOWN/GAP

  CANON_ADMISSION:
    state: UNKNOWN/GAP
```

---

# 99. Promotion Requirements

Before this artifact or an associated root authority system can be promoted to active runtime status, recover or establish:

```text
authoritative root source;

root principal identity;

authority domains;

scope;

effect envelope;

delegability;

revocation authority;

temporal rules;

registry implementation;

authority resolver;

witness implementation;

authorization integration;

transaction integration;

commit-time freshness rules;

provenance storage;

audit;

tests;

adversarial tests;

recovery;

governance approval.
```

---

# 100. Promotion State Machine

```text
SPECIFICATION
      ↓
SOURCE_ALIGNED
      ↓
SCHEMA_VALIDATED
      ↓
IMPLEMENTED
      ↓
INTEGRATED
      ↓
TESTED
      ↓
ADVERSARIALLY_TESTED
      ↓
SECURITY_REVIEWED
      ↓
GOVERNANCE_APPROVED
      ↓
ROOT_BOUND
      ↓
GOVERNED_ACTIVE
```

No transition is automatic.

---

# 101. Final Root Authorization Contract

AMOS SHALL recognize root authority only where an authority source, principal, scope, effect envelope, constraints, temporal validity, provenance, and governance state support that recognition.

Root authority SHALL NOT arise merely from:

```text
model generation;

agent declaration;

Skill installation;

tool access;

capability;

policy permission;

file creation;

repository ownership claim;

memory;

role labels;

credentials alone;

architectural placeholders;

or implementation convenience.
```

Downstream authority SHALL remain traceable:

```text
AUTHORITY SOURCE
      ↓
ROOT GRANT
      ↓
DELEGATION
      ↓
EFFECTIVE AUTHORITY
      ↓
AUTHORITY WITNESS
      ↓
AUTHORIZATION
      ↓
TRANSACTION
      ↓
COMMIT-TIME REVALIDATION
      ↓
COMMIT
```

Every authority path SHALL remain bounded by:

```text
principal;

domain;

scope;

operation;

resource;

effect;

recipient;

purpose;

time;

constraints;

delegation;

revocation;

provenance.
```

Where mutable authority changes, affected witnesses, authorizations, and transactions SHALL be selectively invalidated according to dependency closure.

Where authority cannot be established:

```text
UNKNOWN/GAP
```

shall remain visible.

For consequential effects:

```text
UNKNOWN AUTHORITY
→
NO COMMIT
```

The governing AMOS root-authorization law is:

> **No component may manufacture its own authority. Authority must originate from a valid, provenance-bound source; delegation may only attenuate that authority; authorization must bind it to a specific effect and current state; and no proposal becomes a governed effect until authority, policy, constraints, transaction state, and commit-time validity have been satisfied.**

---

# END — 00_ROOT_AUTHORIZATION.md

```
```

---
**Related:** [[00_HOME]]

---

[[00_ROOT_MOC]]|[[AMOS MOC]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: 00_root_authorization
node_type: note
path: 00_ROOT/00_ROOT_AUTHORIZATION.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[00_COSMO_BRAIN_MOC]]

