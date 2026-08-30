---
title: POLICY REGISTRY
type: registry
source: 03_CONTROL_PLANE/03_POLICY
tags:
- control-plane
- policy
- note
- canon/control-plane
rscf:
  state: DERIVED
  claim_class: CONDITIONAL
  provenance: AMOS_corpus
  scope: AMOS_general
---

# AMOS Policy Registry

## 0. Status

`POLICY_REGISTRY.md` defines the AMOS OS contract for registering, identifying, versioning, discovering, scoping, superseding, revoking, quarantining, and resolving policies used by governed AMOS infrastructure.

The Policy Registry is the authoritative **policy-addressing and policy-metadata surface** for a declared registry scope.

It answers:

> What policy objects are known to this registry, what are their identities and versions, what scope do they claim, what state are they in, how are they related, and which objects should the Policy Engine inspect for a particular request?

The Policy Registry does **not** itself decide whether an action is permitted.

The governing distinctions are:

```text
POLICY_REGISTRY != POLICY_ENGINE

POLICY_REGISTRY != POLICY_DECISION

POLICY_REGISTRY != POLICY_AUTHORITY

POLICY_REGISTRY != CAPABILITY_REGISTRY

POLICY_REGISTRY != CONTROL_PLANE

POLICY_REGISTRY != EXECUTION_ENGINE

POLICY_REGISTRY != COMMIT_ENGINE

REGISTERED != APPLICABLE

REGISTERED != ACTIVE

ACTIVE != APPLICABLE

APPLICABLE != ALLOW

DISCOVERED != GOVERNING

POLICY_EXISTS != POLICY_PERMITS

POLICY_METADATA != POLICY_TRUTH

POLICY_SOURCE != CANONICAL_STATUS

CAPABILITY != AUTHORITY

POLICY_ALLOW != AUTHORITY

PROPOSAL != COMMIT

UNKNOWN/GAP != PASS
```

---

# 1. Purpose

The purpose of the AMOS Policy Registry is to provide a governed, provenance-preserving namespace and resolution layer for policy objects.

It exists so AMOS components do not need to infer policy identity from:

- filenames;
- directory position;
- human-readable titles;
- agent memory;
- cached prose;
- duplicated documents;
- latest-modified timestamps;
- semantic similarity;
- undocumented conventions;
- or model-generated interpretation.

Instead:

```text
POLICY SOURCE
      ↓
REGISTRATION
      ↓
POLICY IDENTITY
      ↓
VERSION
      ↓
STATUS
      ↓
SCOPE
      ↓
PROVENANCE
      ↓
DEPENDENCY / SUPERSESSION
      ↓
DISCOVERY
      ↓
POLICY ENGINE
```

The registry provides identity and discovery.

The Policy Engine provides evaluation.

---

# 2. Architectural Position

Canonical conceptual path:

```text
SOURCE / CANON / GOVERNANCE MATERIAL
                ↓
         POLICY INGESTION
                ↓
        POLICY REGISTRY
                ↓
       POLICY DISCOVERY
                ↓
        POLICY ENGINE
                ↓
       POLICY_DECISION
                ↓
        CONTROL PLANE
                ↓
     COMMIT-TIME GOVERNANCE
```

The registry sits upstream of policy evaluation.

---

# 3. Core Responsibility

The Policy Registry owns:

```text
policy identifiers;
policy namespaces;
policy metadata;
policy versions;
policy content identities;
policy source references;
policy status;
policy scope declarations;
policy regime declarations;
policy temporal envelopes;
policy dependencies;
policy aliases;
policy family membership;
policy hierarchy metadata;
policy supersession lineage;
policy revocation state;
policy quarantine state;
policy discovery metadata;
policy coverage declarations;
policy provenance;
policy integrity metadata.
```

It does NOT own:

```text
policy interpretation;
policy predicate evaluation;
policy rule execution;
final policy decisions;
capability execution;
authority issuance;
authority validation;
effect dispatch;
durable commit;
release-ledger finality;
receiver receipt validation;
empirical truth.
```

---

# 4. Core Architecture

```text
              ┌────────────────────────┐
              │ POLICY SOURCE MATERIAL │
              └────────────┬───────────┘
                           │
                           ▼
              ┌────────────────────────┐
              │   INGESTION / ADMISSION│
              └────────────┬───────────┘
                           │
                           ▼
        ┌────────────────────────────────────┐
        │         POLICY REGISTRY            │
        │                                    │
        │  1. Namespace Manager              │
        │  2. Identity Resolver              │
        │  3. Version Manager                │
        │  4. Content-Hash Binder            │
        │  5. Status Manager                 │
        │  6. Scope Index                    │
        │  7. Regime Index                   │
        │  8. Dependency Graph               │
        │  9. Supersession Graph             │
        │ 10. Alias Resolver                 │
        │ 11. Revocation Registry            │
        │ 12. Quarantine Registry            │
        │ 13. Provenance Registry            │
        │ 14. Coverage Registry              │
        │ 15. Discovery Index                │
        └──────────────────┬─────────────────┘
                           │
                           ▼
                  POLICY ENGINE
```

---

# 5. Policy Object

The canonical registry unit is a `POLICY_OBJECT`.

```yaml
policy_object:
  policy_id: string
  namespace: string
  version: string
  content_hash: string

  title: string
  description: string

  policy_class: string

  status:
    - DRAFT
    - ACTIVE
    - DEPRECATED
    - SUPERSEDED
    - REVOKED
    - QUARANTINED
    - ARCHIVED

  source:
    source_type: string
    source_id: string
    source_version: null
    source_hash: null
    source_refs: []

  scope: {}

  regime: {}

  temporal:
    valid_from: null
    valid_until: null

  applies_to:
    principal_classes: []
    action_classes: []
    capability_ids: []
    provider_ids: []
    resource_classes: []
    effect_classes: []
    environments: []
    jurisdictions: []

  hierarchy:
    level: null
    parent_policy_ids: []
    child_policy_ids: []

  dependencies: []

  supersedes: []
  superseded_by: []

  aliases: []

  exceptions: []

  provenance: {}

  governance: {}

  registered_at: timestamp
  updated_at: timestamp
```

---

# 6. Policy Identity

Every policy MUST have a stable identifier.

Recommended form:

```text
POLICY::<namespace>::<policy_name>
```

Example:

```text
POLICY::AMOS_CORE::EXTERNAL_EFFECT_RELEASE
```

or:

```text
POLICY::MEMORY::PERSISTENT_WRITE
```

The exact naming syntax may evolve, but identity MUST remain explicit.

---

# 7. Identity Tuple

A material policy instance SHOULD be identified by:

```text
PolicyIdentity =
(
    policy_id,
    version,
    content_hash
)
```

A filename alone is insufficient.

A title alone is insufficient.

A version alone may be insufficient if authoritative content can mutate without a version bump.

---

# 8. Identity Invariant

```text
same policy_id
+ same version
+ different material content
```

MUST be detected as an integrity conflict unless explicitly supported by the storage/version model.

It MUST NOT silently resolve as the same immutable policy instance.

---

# 9. Namespace Model

Namespaces prevent unrelated policies from colliding.

Recommended namespace families:

```text
AMOS_CORE

CONTROL_PLANE

AUTHORITY

CAPABILITY

MEMORY

INFORMATION

SECURITY

PRIVACY

OBSERVABILITY

PROVENANCE

TRANSACTION

EFFECT_RELEASE

AGENT

SKILL

DOMAIN::<domain>

ORGANIZATION::<organization>

JURISDICTION::<jurisdiction>
```

These are architectural examples, not claims that every namespace already exists.

---

# 10. Namespace Object

```yaml
policy_namespace:
  namespace_id: string

  title: string

  owner: null

  authority_ref: null

  scope: {}

  parent_namespace: null

  child_namespaces: []

  status:
    - ACTIVE
    - DEPRECATED
    - QUARANTINED

  provenance: {}
```

---

# 11. Namespace Invariant

Two namespaces MUST NOT be treated as equivalent merely because they contain policies with similar names.

Example:

```text
SECURITY::WRITE_POLICY
```

and:

```text
DOMAIN::FX::WRITE_POLICY
```

may have completely different meanings.

---

# 12. Policy Classes

Recommended policy classes include:

```text
PERMISSION

PROHIBITION

OBLIGATION

CONSTRAINT

AUTHORITY_REQUIREMENT

DISCLOSURE

RETENTION

PRIVACY

SECURITY

OBSERVABILITY

PROVENANCE

TRANSACTION

EFFECT_RELEASE

RESOURCE_ACCESS

CAPABILITY_USE

AGENT_OPERATION

SKILL_OPERATION

DOMAIN

EXCEPTION

ESCALATION

GOVERNANCE

CANON
```

A policy MAY belong to more than one classification where the schema explicitly supports it.

---

# 13. Policy Status

Canonical status states:

```text
DRAFT

ACTIVE

DEPRECATED

SUPERSEDED

REVOKED

QUARANTINED

ARCHIVED
```

---

# 14. Status Semantics

## DRAFT

Exists but is not automatically governing.

## ACTIVE

Eligible for policy discovery and applicability evaluation.

## DEPRECATED

Still identifiable but discouraged or scheduled for replacement.

## SUPERSEDED

Replaced by another policy through explicit supersession lineage.

## REVOKED

No longer valid as current governing policy.

## QUARANTINED

Excluded from ordinary evaluation pending integrity/governance review.

## ARCHIVED

Retained for provenance/history but not current governance.

---

# 15. Status Boundary

```text
REGISTERED != ACTIVE

ACTIVE != APPLICABLE

APPLICABLE != ALLOW
```

The registry records status.

The Policy Engine evaluates applicability.

---

# 16. Registration Contract

A policy SHOULD NOT become `ACTIVE` merely because a file exists.

Registration SHOULD include:

```text
identity;
version;
content identity;
source;
scope;
regime;
status;
provenance;
governance basis;
dependency metadata;
supersession metadata;
temporal validity.
```

---

# 17. Registration Request

```yaml
policy_registration_request:
  registration_id: string

  candidate_policy:
    policy_id: string
    namespace: string
    version: string
    content_hash: string

  source:
    source_type: string
    source_ref: string
    source_version: null
    source_hash: null

  proposed_status: DRAFT

  scope: {}

  regime: {}

  temporal: {}

  dependencies: []

  supersedes: []

  aliases: []

  provenance: {}

  governance:
    submitted_by: null
    authority_ref: null
```

---

# 18. Registration Result

```yaml
policy_registration_result:
  registration_id: string

  state:
    - REGISTERED
    - REJECTED
    - QUARANTINED
    - CONFLICT
    - UNKNOWN_GAP

  policy_id: null
  version: null
  content_hash: null

  reason_codes: []

  conflicts: []

  gaps: []

  provenance: {}
```

---

# 19. Registration Is Not Canon Admission

A policy may be registered as:

```text
DRAFT
```

or:

```text
MODEL
```

without being canonically admitted.

Therefore:

```text
REGISTERED != CANONICAL
```

and:

```text
DISCOVERABLE != CANONICAL
```

---

# 20. Source / Canon Boundary

Every policy SHOULD preserve its source classification.

Recommended source classes:

```text
SOURCE_CANON

SOURCE_CLAIM

GOVERNANCE_RULE

MODEL

DERIVED

EXTERNAL_POLICY

LEGAL_SOURCE

ORGANIZATIONAL_POLICY

UNKNOWN
```

A model-generated policy MUST NOT be silently relabeled `SOURCE_CANON`.

---

# 21. Source Object

```yaml
policy_source:
  source_id: string

  source_class: string

  title: string

  version: null

  content_hash: null

  origin: null

  steward: null

  source_refs: []

  retrieved_at: null

  provenance: {}
```

---

# 22. Provenance

Policy provenance SHOULD preserve:

```text
origin;
source identity;
source version;
source hash;
registration event;
transformation history;
supersession lineage;
authority basis;
review history;
admission history.
```

---

# 23. Provenance Object

```yaml
policy_provenance:
  policy_id: string
  version: string

  origin_architect: null
  steward: null

  source_ids: []

  source_hashes: {}

  transformations: []

  derived_from: []

  registered_by: null

  registered_at: timestamp

  reviewed_by: []

  governance_refs: []

  ancestry: []
```

---

# 24. Provenance Topology

The registry SHOULD preserve ancestry rather than merely source count.

Example:

```text
SOURCE_A
   ↓
POLICY_A
   ├── SUMMARY_A
   ├── TRANSLATION_A
   └── POLICY_ALIAS_A
```

These are descendants of one source lineage.

They MUST NOT be counted as independent confirmations.

---

# 25. Sybil-Hardening Rule

```text
multiple artifacts
!=
multiple independent authorities
```

when the artifacts share the same underlying provenance.

Aliases, copies, translations, summaries, or regenerated files MUST preserve ancestry where known.

---

# 26. Content Identity

A policy SHOULD have a canonical content digest.

```text
content_hash =
H(canonical_policy_content)
```

The exact serialization and hashing algorithm belong to implementation specification.

The conceptual requirement is stable material-content identity.

---

# 27. Content Mutation

If material policy content changes:

```text
old_content_hash != new_content_hash
```

the registry MUST NOT silently preserve immutable identity assumptions.

Depending on governance:

```text
new version;
new revision;
conflict;
quarantine;
or explicit mutable-state transition
```

is required.

---

# 28. Version Model

Recommended semantic version:

```text
MAJOR.MINOR.PATCH
```

Interpretation MAY be:

```text
MAJOR
= incompatible semantic/governance change

MINOR
= backward-compatible policy expansion or clarification

PATCH
= non-semantic correction
```

The exact scheme is governance-defined.

---

# 29. Version Invariant

A version label MUST NOT be used as a substitute for content identity.

```text
version equality
```

does not establish:

```text
content equality
```

unless the storage/governance model guarantees immutability.

---

# 30. Version Record

```yaml
policy_version:
  policy_id: string

  version: string

  content_hash: string

  created_at: timestamp

  valid_from: null
  valid_until: null

  status: string

  previous_version: null
  next_version: null

  change_class:
    - INITIAL
    - PATCH
    - SEMANTIC
    - GOVERNANCE
    - BREAKING
    - REVOCATION

  change_summary: null

  provenance: {}
```

---

# 31. Supersession

Supersession MUST be explicit.

Example:

```text
POLICY_A@1
      ↓
superseded_by
      ↓
POLICY_A@2
```

or:

```text
POLICY_A
   ↓
superseded_by
   ↓
POLICY_B
```

---

# 32. Supersession Object

```yaml
policy_supersession:
  supersession_id: string

  predecessor:
    policy_id: string
    version: string

  successor:
    policy_id: string
    version: string

  effective_at: timestamp

  scope: {}

  regime: {}

  reason: null

  authority_ref: null

  provenance: {}
```

---

# 33. Supersession Invariant

Newer timestamp alone does not establish supersession.

Higher version number alone does not necessarily establish supersession across distinct policy IDs.

Explicit lineage SHOULD exist.

---

# 34. Partial Supersession

A successor MAY supersede only part of a predecessor's scope.

Example:

```text
POLICY_A
scope = GLOBAL

POLICY_B
supersedes POLICY_A
only for RESOURCE_CLASS_X
```

The registry MUST preserve the remaining valid envelope of `POLICY_A`.

---

# 35. Supersession Scope

```yaml
supersession_scope:
  principal_classes: []
  action_classes: []
  capability_ids: []
  resource_classes: []
  environments: []
  jurisdictions: []
  regimes: []
```

---

# 36. Revocation

Revocation is distinct from supersession.

```text
SUPERSEDED
= replaced

REVOKED
= withdrawn
```

A revoked policy may have no replacement.

---

# 37. Revocation Object

```yaml
policy_revocation:
  revocation_id: string

  policy_id: string
  version: string

  revoked_at: timestamp

  effective_at: timestamp

  reason: string

  authority_ref: string

  scope: {}

  provenance: {}
```

---

# 38. Revocation Invariant

A cached `ACTIVE` status MUST NOT override current authoritative revocation state.

If a load-bearing policy is revoked:

```text
dependent policy decisions
→ REVALIDATE / INVALIDATE
```

as appropriate.

---

# 39. Historical Validity

Revocation does not erase history.

A policy may have been valid during:

```text
[t0, t1)
```

and revoked at:

```text
t1
```

Historical decisions MAY remain reconstructable against the policy state that existed at their decision time.

This does not restore present authority.

---

# 40. Quarantine

A policy SHOULD enter quarantine when integrity is unresolved.

Examples:

```text
content hash mismatch;
unknown provenance;
identity collision;
forged authority;
conflicting versions;
corrupt source;
unresolved canon conflict;
malformed schema;
ambiguous supersession;
registry poisoning suspicion.
```

---

# 41. Quarantine Object

```yaml
policy_quarantine:
  quarantine_id: string

  policy_id: string
  version: string

  reason_code: string
  description: string

  entered_at: timestamp

  evidence_refs: []

  release_conditions: []

  state:
    - ACTIVE
    - RELEASED
    - REJECTED
```

---

# 42. Quarantine Boundary

```text
QUARANTINED != ACTIVE
```

A quarantined policy SHOULD NOT govern ordinary evaluation unless an explicit emergency/governance rule states otherwise.

---

# 43. Scope

Every policy SHOULD declare an applicability envelope where known.

```yaml
policy_scope:
  system: null
  organization: null
  domain: null

  principal_classes: []
  action_classes: []
  capability_ids: []
  provider_ids: []
  resource_classes: []
  resource_ids: []
  effect_classes: []

  environments: []
  jurisdictions: []

  hml:
    H: null
    M: null
    L: null
```

---

# 44. Scope Invariant

A policy MUST NOT silently expand beyond its declared or validated scope.

```text
AppliedScope
⊆
PolicyScope
```

---

# 45. Unknown Scope

If scope is missing:

```text
scope = UNKNOWN
```

not:

```text
scope = UNIVERSAL
```

unless universal applicability is explicitly established.

---

# 46. Regime

Policies MAY vary by regime.

Examples:

```text
development;
testing;
production;
incident;
emergency;
normal operation;
degraded mode;
recovery mode.
```

---

# 47. Regime Object

```yaml
policy_regime:
  allowed_regimes: []

  excluded_regimes: []

  transition_rules: []

  unknown_behavior:
    - DENY
    - ESCALATE
    - UNKNOWN_GAP
```

---

# 48. Regime Invariant

A policy validated in one regime MUST NOT automatically transfer to another.

```text
Valid(P, DEVELOPMENT)
↛
Valid(P, PRODUCTION)
```

---

# 49. Temporal Envelope

Policies SHOULD support:

```yaml
temporal:
  created_at: timestamp
  valid_from: null
  valid_until: null
  revoked_at: null
  superseded_at: null
```

---

# 50. Temporal Invariant

Policy validity is evaluated against trusted time where temporal semantics matter.

A policy expired at `t1` MUST NOT be treated as active at `t2 > t1`.

---

# 51. Dependencies

Policies MAY depend on other policy or governance objects.

Example:

```text
POLICY_A
depends_on
POLICY_B
```

Dependency does not necessarily mean precedence.

---

# 52. Dependency Object

```yaml
policy_dependency:
  dependency_id: string

  from_policy: string

  to_object:
    object_type: string
    object_id: string
    version_constraint: null

  dependency_type:
    - REQUIRES
    - REFERENCES
    - EXTENDS
    - CONSTRAINS
    - OVERRIDES
    - IMPLEMENTS
    - INTERPRETS

  scope: {}

  provenance: {}
```

---

# 53. Dependency Invariant

The registry MUST distinguish:

```text
DEPENDS_ON
```

from:

```text
SUPERSEDES
```

from:

```text
OVERRIDES
```

from:

```text
REFERENCES
```

These relations are not interchangeable.

---

# 54. Dependency Graph

Conceptually:

```text
PolicyGraph =
(V, E)

V = policy/governance objects

E = typed dependency edges
```

The graph SHOULD preserve edge types.

---

# 55. Circular Dependencies

Circular policy dependencies MUST be detectable.

Example:

```text
P1 requires P2
P2 requires P1
```

may represent:

```text
valid mutual dependency;
bad decomposition;
or unresolved governance cycle.
```

The registry SHOULD expose the cycle rather than silently flatten it.

---

# 56. Aliases

Policies MAY have aliases.

```yaml
policy_alias:
  alias: string

  canonical_policy_id: string

  namespace: string

  valid_from: null
  valid_until: null

  provenance: {}
```

---

# 57. Alias Invariant

```text
alias
```

is not a second policy.

Therefore:

```text
AliasCount
!=
IndependentPolicyCount
```

---

# 58. Alias Collision

If one alias resolves to multiple active policy IDs within the same resolution context:

```text
CONFLICT
```

unless explicit disambiguation rules exist.

---

# 59. Policy Families

Policies MAY be grouped into families.

Examples:

```text
AUTHORITY_FAMILY

MEMORY_FAMILY

EFFECT_RELEASE_FAMILY

OBSERVABILITY_FAMILY

PRIVACY_FAMILY

SECURITY_FAMILY
```

---

# 60. Family Object

```yaml
policy_family:
  family_id: string

  title: string

  policy_ids: []

  scope: {}

  parent_family: null

  dependencies: []

  provenance: {}
```

---

# 61. H/M/L Registry Structure

The registry SHOULD support AMOS H/M/L policy organization.

```text
H = governing/system-level policies

M = subsystem/workflow/domain policies

L = operation/resource-specific policies
```

---

# 62. H-Level Registry Entries

Examples:

```text
system governance;
global authority boundaries;
canon governance;
high-consequence effect rules;
system-wide provenance requirements.
```

---

# 63. M-Level Registry Entries

Examples:

```text
memory subsystem;
agent subsystem;
workflow subsystem;
domain runtime;
observability subsystem;
transaction subsystem.
```

---

# 64. L-Level Registry Entries

Examples:

```text
specific capability;
specific resource;
specific effect;
specific operation;
specific tool.
```

---

# 65. H/M/L Metadata

```yaml
hml:
  level:
    - H
    - M
    - L

  parent_policy_ids: []

  child_policy_ids: []

  inheritance_mode:
    - NONE
    - CONSTRAIN_ONLY
    - EXPLICIT
```

---

# 66. H/M/L Invariant

Hierarchy MUST NOT automatically imply semantic inheritance.

If inheritance exists, it MUST be explicit.

A child policy MUST NOT silently weaken a governing parent policy.

---

# 67. Policy Discovery

The registry SHOULD expose policy discovery based on typed context.

Input:

```yaml
policy_discovery_request:
  principal: {}
  action: {}
  capability: {}
  provider: {}
  target: {}
  effect: {}
  environment: {}
  jurisdiction: {}
  scope: {}
  regime: {}
  time: null
```

---

# 68. Discovery Output

```yaml
policy_discovery_result:
  candidate_policies: []

  excluded_policies: []

  unresolved_policies: []

  coverage: {}

  provenance: {}

  registry_snapshot: {}
```

---

# 69. Candidate Policy

```yaml
candidate_policy:
  policy_id: string
  version: string
  content_hash: string

  discovery_basis:
    - ACTION
    - CAPABILITY
    - TARGET
    - EFFECT
    - PRINCIPAL
    - ENVIRONMENT
    - JURISDICTION
    - SCOPE
    - REGIME
    - DEPENDENCY

  status: ACTIVE

  applicability_hint: null
```

---

# 70. Discovery Boundary

The registry returns **candidates**.

It MUST NOT claim:

```text
candidate_policy
=
applicable_policy
```

Applicability belongs to the Policy Engine.

---

# 71. Discovery Completeness

The registry SHOULD expose whether discovery is believed complete for the requested scope.

```yaml
policy_coverage:
  scope: {}

  world_assumption:
    - CLOSED_WORLD
    - OPEN_WORLD
    - UNKNOWN

  completeness:
    - COMPLETE
    - PARTIAL
    - UNKNOWN_GAP

  authority_ref: null

  evidence_refs: []
```

---

# 72. Closed-World Registry

A registry MAY claim:

```text
CLOSED_WORLD
```

only for an explicitly governed scope.

Meaning:

> This registry is authoritative and complete for the declared policy namespace/scope under the specified conditions.

It MUST NOT imply global completeness.

---

# 73. Open-World Registry

```text
OPEN_WORLD
```

means additional governing policies may exist outside the registry.

Therefore:

```text
not found
!=
does not exist
```

---

# 74. Unknown Coverage

If registry completeness cannot be established:

```text
world_assumption = UNKNOWN
completeness = UNKNOWN_GAP
```

This uncertainty SHOULD propagate to the Policy Engine when decision-relevant.

---

# 75. Discovery Indexes

The registry MAY index policies by:

```text
policy_id;
namespace;
alias;
class;
principal;
action;
capability;
provider;
resource;
effect;
environment;
jurisdiction;
scope;
regime;
H/M/L level;
status;
dependency;
source;
provenance.
```

Indexes are retrieval aids.

They are not policy authority.

---

# 76. Registry Snapshot

A policy discovery response SHOULD be bindable to a registry snapshot.

```yaml
registry_snapshot:
  registry_id: string

  generation: string

  version: string

  snapshot_hash: string

  observed_at: timestamp
```

---

# 77. Snapshot Boundary

A global registry snapshot may support integrity and auditability.

However, when precise policy read sets exist, unrelated registry changes SHOULD NOT automatically invalidate every decision.

---

# 78. Fine-Grained Read Sets

The Policy Engine SHOULD ultimately bind decisions to the exact policy objects used:

```text
PolicyReadSet =
{
  (policy_id, version, content_hash)
}
```

This permits selective invalidation.

---

# 79. Registry Generation

A registry MAY maintain a generation identifier to detect destructive reset, rollback, or replacement.

Example identity:

```text
registry_id
+ generation
+ version
+ snapshot_hash
```

This is stronger than scalar version alone.

---

# 80. Registry Rollback Detection

If:

```text
generation changes unexpectedly
```

or:

```text
snapshot hash contradicts expected state
```

the registry SHOULD surface:

```text
REVALIDATE
```

or:

```text
QUARANTINE
```

rather than silently accepting the state.

---

# 81. Registry State

Recommended registry states:

```text
INITIALIZING

ACTIVE

DEGRADED

READ_ONLY

QUARANTINED

REBUILDING

SUPERSEDED

RETIRED
```

---

# 82. Registry State Object

```yaml
policy_registry_state:
  registry_id: string

  generation: string
  version: string
  snapshot_hash: string

  state: ACTIVE

  coverage: {}

  last_validated_at: timestamp

  provenance: {}
```

---

# 83. Registry Mutation

Registry mutations include:

```text
REGISTER_POLICY

UPDATE_METADATA

ADD_VERSION

SUPERSEDE_POLICY

REVOKE_POLICY

QUARANTINE_POLICY

RELEASE_POLICY

ADD_ALIAS

REMOVE_ALIAS

ADD_DEPENDENCY

REMOVE_DEPENDENCY

CHANGE_SCOPE

CHANGE_REGIME

CHANGE_STATUS
```

---

# 84. Mutation Governance

Registry mutation SHOULD require explicit authority.

```text
CAN_READ_REGISTRY
!=
CAN_MUTATE_REGISTRY
```

and:

```text
CAN_REGISTER_DRAFT
!=
CAN_ACTIVATE_POLICY
```

and:

```text
CAN_ACTIVATE_POLICY
!=
CAN_REVOKE_POLICY
```

unless authority explicitly grants those operations.

---

# 85. Registry Mutation Request

```yaml
policy_registry_mutation:
  mutation_id: string

  operation: string

  target_policy_id: null

  proposed_change: {}

  principal: {}

  authority_ref: null

  expected_registry_state:
    generation: null
    version: null
    snapshot_hash: null

  provenance: {}

  requested_at: timestamp
```

---

# 86. Mutation Result

```yaml
policy_registry_mutation_result:
  mutation_id: string

  state:
    - COMMITTED
    - REJECTED
    - CONFLICT
    - REVALIDATE
    - UNKNOWN_GAP

  old_registry_state: {}

  new_registry_state: {}

  affected_policy_ids: []

  provenance: {}
```

---

# 87. CAS-Style Mutation

Where mutable concurrent registry state exists:

```text
READ expected registry identity
        ↓
PREPARE mutation
        ↓
COMPARE current identity
        ↓
COMMIT or REVALIDATE
```

This is an AMOS control pattern.

It does not claim conversational ChatGPT literally provides distributed CAS.

---

# 88. Atomic Mutation

A logically single policy mutation SHOULD avoid partial registry state.

Example:

```text
activate POLICY_B
+
supersede POLICY_A
```

may need atomic treatment if either change without the other creates invalid governance state.

---

# 89. Multi-Policy Transaction

```yaml
policy_registry_transaction:
  transaction_id: string

  mutations: []

  expected_state: {}

  atomic: true

  authority_ref: string

  provenance: {}
```

Possible results:

```text
COMMITTED

CONFLICT

REVALIDATE

REJECTED

UNKNOWN_GAP
```

---

# 90. Policy Admission

The registry SHOULD distinguish:

```text
STORED
REGISTERED
ADMITTED
ACTIVE
```

Suggested lifecycle:

```text
SOURCE
  ↓
CANDIDATE
  ↓
REGISTERED_DRAFT
  ↓
VALIDATED
  ↓
ADMITTED
  ↓
ACTIVE
```

No transition is automatic.

---

# 91. Admission Checks

Policy admission MAY require:

```text
schema validation;
identity validation;
content-hash validation;
source/provenance validation;
scope validation;
regime validation;
dependency validation;
conflict analysis;
canon consistency;
authority validation;
supersession validation;
test evidence.
```

The required set depends on governance class.

---

# 92. Canon Admission

AMOS canon admission is stricter than registry registration.

Conceptually:

```text
REGISTERED
↛
CANON
```

Canon admission SHOULD use the appropriate canon/provenance/supersession process.

---

# 93. Canon Conflict

If a candidate policy conflicts with applicable source canon:

```text
candidate policy
→ QUARANTINE / REJECT / COMPETING
```

depending on governance.

The registry MUST NOT silently overwrite source canon.

---

# 94. Policy Precedence Metadata

The registry MAY store explicit precedence relationships.

```yaml
policy_precedence_edge:
  higher_policy_id: string
  lower_policy_id: string

  basis:
    - CANON
    - LAW
    - AUTHORITY
    - EXPLICIT_OVERRIDE
    - SPECIFICITY
    - SUPERSESSION

  scope: {}

  regime: {}

  authority_ref: null

  provenance: {}
```

---

# 95. Precedence Boundary

The registry stores precedence metadata.

The Policy Engine evaluates how precedence affects a concrete request.

---

# 96. Precedence Invariant

The registry MUST NOT infer precedence merely from:

```text
file order;
directory depth;
numeric filename;
timestamp;
policy ID;
registration order;
retrieval rank.
```

unless explicit governance defines such semantics.

---

# 97. Exceptions Registry

Policy exceptions MAY be registered as first-class objects.

```yaml
policy_exception:
  exception_id: string

  policy_id: string

  version: string

  status:
    - ACTIVE
    - EXPIRED
    - REVOKED
    - QUARANTINED

  principal_scope: []
  action_scope: []
  resource_scope: []
  effect_scope: []

  valid_from: null
  valid_until: null

  issuer: null
  authority_ref: null

  conditions: []

  provenance: {}
```

---

# 98. Exception Boundary

```text
EXCEPTION_EXISTS
!=
EXCEPTION_APPLIES
```

Applicability is evaluated by the Policy Engine.

---

# 99. Exception Revocation

Exception revocation MUST propagate to dependent policy decisions.

A stale cached exception MUST NOT remain effective after authoritative revocation.

---

# 100. Policy Integrity

Registry integrity SHOULD detect:

```text
duplicate immutable identity;

content-hash mismatch;

broken supersession;

dangling dependency;

alias collision;

invalid status transition;

missing provenance;

scope contradiction;

regime contradiction;

unauthorized mutation;

registry rollback;

version/content inconsistency.
```

---

# 101. Integrity Result

```yaml
policy_integrity_result:
  policy_id: string
  version: string

  state:
    - VALID
    - INVALID
    - CONFLICT
    - QUARANTINE
    - UNKNOWN_GAP

  violations: []

  evidence_refs: []
```

---

# 102. Registry Invariants

## INV-PR-001 — Stable Identity

Every policy has a stable identifier.

## INV-PR-002 — Version Binding

Material versions bind to content identity.

## INV-PR-003 — No Identity Collision

Different material policies MUST NOT silently share immutable identity.

## INV-PR-004 — Source Preservation

Source lineage MUST remain recoverable.

## INV-PR-005 — Canon Boundary

```text
REGISTERED != CANONICAL
```

## INV-PR-006 — Status Explicitness

Policy status MUST be explicit.

## INV-PR-007 — Revocation Visibility

Revoked policies MUST remain visibly revoked.

## INV-PR-008 — Supersession Visibility

Supersession lineage MUST remain reconstructable.

## INV-PR-009 — Scope Preservation

Unknown scope MUST NOT become universal scope.

## INV-PR-010 — Regime Preservation

Unknown regime MUST NOT become universal regime.

## INV-PR-011 — Temporal Integrity

Expired policies MUST NOT appear current.

## INV-PR-012 — Dependency Typing

Policy relations MUST remain typed.

## INV-PR-013 — Alias Integrity

Aliases MUST NOT become independent policy identities.

## INV-PR-014 — Provenance Integrity

Derived/copied policies MUST preserve ancestry where known.

## INV-PR-015 — Sybil Hardening

Correlated descendants MUST NOT be treated as independent authority.

## INV-PR-016 — Discovery/Evaluation Separation

```text
DISCOVERED != APPLICABLE
```

## INV-PR-017 — Registry/Engine Separation

Registry MUST NOT issue final policy decisions.

## INV-PR-018 — Capability Separation

```text
POLICY_REGISTRY != CAPABILITY_REGISTRY
```

## INV-PR-019 — Authority Separation

Registry membership MUST NOT confer execution authority.

## INV-PR-020 — Commit Separation

Registry mutation authority MUST NOT imply effect commit authority.

---

# 103. Additional Invariants

## INV-PR-021 — No Policy-by-Filename

Filename MUST NOT be sole authoritative identity.

## INV-PR-022 — No Latest-Wins Assumption

Newest timestamp MUST NOT automatically determine governing policy.

## INV-PR-023 — No Version-Wins Assumption

Highest version MUST NOT automatically override unrelated policies.

## INV-PR-024 — No Silent Supersession

Supersession MUST be explicit.

## INV-PR-025 — No Silent Revocation

Revocation MUST be explicit and auditable.

## INV-PR-026 — No Silent Scope Expansion

Policy updates MUST NOT widen scope without governance-visible change.

## INV-PR-027 — No Silent Regime Expansion

Policy updates MUST NOT widen regimes without governance-visible change.

## INV-PR-028 — No Quarantine Bypass

Quarantined policies MUST NOT enter ordinary active discovery.

## INV-PR-029 — No Coverage Inflation

Partial registry coverage MUST NOT be labeled complete.

## INV-PR-030 — No Read/Write Authority Collapse

Read access to registry does not imply mutation authority.

---

# 104. Failure Modes

## FM-PR-001 — Identity Collision

Two material policies share one immutable identity.

## FM-PR-002 — Orphan Policy

Policy has no resolvable source/provenance where provenance is required.

## FM-PR-003 — Version Drift

Version metadata and content disagree.

## FM-PR-004 — Hash Drift

Content changes without corresponding identity change.

## FM-PR-005 — Broken Supersession

Predecessor/successor lineage is inconsistent.

## FM-PR-006 — Supersession Cycle

Policies supersede each other cyclically.

## FM-PR-007 — Dangling Dependency

Dependency target cannot be resolved.

## FM-PR-008 — Dependency Type Loss

Typed relation becomes generic reference.

## FM-PR-009 — Alias Collision

Alias resolves ambiguously.

## FM-PR-010 — Alias Fork

Alias changes target without governed lineage.

## FM-PR-011 — Revocation Loss

Revoked policy appears active.

## FM-PR-012 — Stale Status Cache

Old policy state survives authoritative change.

## FM-PR-013 — Quarantine Bypass

Quarantined policy is discovered as active.

## FM-PR-014 — Scope Loss

Scope metadata is missing or corrupted.

## FM-PR-015 — Scope Inflation

Narrow policy becomes globally discoverable.

## FM-PR-016 — Regime Loss

Regime metadata disappears.

## FM-PR-017 — Regime Inflation

Development policy becomes production policy.

## FM-PR-018 — Temporal Leakage

Expired policy appears current.

## FM-PR-019 — Registry Rollback

Older registry state replaces newer authoritative state.

## FM-PR-020 — Unauthorized Mutation

Registry changes without valid authority.

## FM-PR-021 — Partial Transaction

Multi-policy update only partially commits.

## FM-PR-022 — Provenance Loss

Source ancestry cannot be reconstructed.

## FM-PR-023 — Provenance Sybil

Copies are counted as independent authority.

## FM-PR-024 — Coverage Inflation

Open-world registry is treated as complete.

## FM-PR-025 — Discovery Omission

Relevant candidate policy is not returned.

## FM-PR-026 — Discovery Pollution

Irrelevant policy explosion overwhelms evaluation.

## FM-PR-027 — Policy/Capability Collision

Policy ID is confused with capability ID.

## FM-PR-028 — Policy/Authority Collision

Registry state is treated as authority.

## FM-PR-029 — Canon Overwrite

Generated policy silently replaces source canon.

## FM-PR-030 — Audit Failure

Historical governing state cannot be reconstructed.

---

# 105. Repair / Recovery

Canonical recovery:

```text
DETECT REGISTRY FAILURE
        ↓
FREEZE AFFECTED MUTATIONS
        ↓
PRESERVE CURRENT + PRIOR STATE
        ↓
IDENTIFY EARLIEST CORRUPT OBJECT / EDGE
        ↓
QUARANTINE SUSPECT STATE
        ↓
INVALIDATE DEPENDENT INDEXES / DECISIONS
        ↓
PRESERVE UNAFFECTED STATE
        ↓
RECONSTRUCT FROM PROVENANCE
        ↓
REVALIDATE IDENTITY / VERSION / HASH
        ↓
REVALIDATE DEPENDENCIES
        ↓
REVALIDATE SUPERSESSION
        ↓
REBUILD AFFECTED INDEXES
        ↓
ISSUE NEW REGISTRY STATE
```

---

# 106. Selective Recovery

If only one policy object is corrupted:

```text
quarantine affected policy
invalidate dependent decisions
preserve unrelated policies
```

Do not rebuild the entire registry unless dependency uncertainty requires it.

---

# 107. Rollback

Registry rollback SHOULD target the nearest validated state.

```text
Current invalid state
        ↓
nearest valid registry snapshot
        ↓
replay validated mutations
        ↓
exclude corrupt mutation
        ↓
revalidate
```

Rollback itself requires governance.

---

# 108. Recovery Provenance

Recovery MUST preserve:

```text
what failed;
when it failed;
what state was affected;
what was invalidated;
what was restored;
what was replayed;
what remained quarantined.
```

---

# 109. Tests / Validators

Minimum test suite:

```text
T-PR-001 policy schema

T-PR-002 policy ID uniqueness

T-PR-003 namespace resolution

T-PR-004 version parsing

T-PR-005 content-hash binding

T-PR-006 duplicate identity rejection

T-PR-007 status transition

T-PR-008 active policy discovery

T-PR-009 draft exclusion

T-PR-010 revoked exclusion

T-PR-011 quarantined exclusion

T-PR-012 archived exclusion

T-PR-013 supersession resolution

T-PR-014 partial supersession

T-PR-015 supersession cycle detection

T-PR-016 revocation

T-PR-017 historical validity

T-PR-018 scope resolution

T-PR-019 unknown scope

T-PR-020 regime resolution

T-PR-021 unknown regime

T-PR-022 temporal validity

T-PR-023 expiration

T-PR-024 dependency resolution

T-PR-025 dangling dependency

T-PR-026 dependency cycle

T-PR-027 alias resolution

T-PR-028 alias collision

T-PR-029 family resolution

T-PR-030 H/M/L mapping

T-PR-031 provenance preservation

T-PR-032 ancestry preservation

T-PR-033 correlated-source detection

T-PR-034 policy coverage CLOSED_WORLD

T-PR-035 policy coverage OPEN_WORLD

T-PR-036 policy coverage UNKNOWN

T-PR-037 candidate discovery by action

T-PR-038 candidate discovery by capability

T-PR-039 candidate discovery by target

T-PR-040 candidate discovery by effect

T-PR-041 candidate discovery by principal

T-PR-042 candidate discovery by environment

T-PR-043 candidate discovery by jurisdiction

T-PR-044 candidate discovery by regime

T-PR-045 registry snapshot

T-PR-046 generation change

T-PR-047 rollback detection

T-PR-048 unauthorized mutation

T-PR-049 CAS conflict

T-PR-050 atomic multi-policy mutation

T-PR-051 quarantine

T-PR-052 quarantine release

T-PR-053 canon boundary

T-PR-054 model/source separation

T-PR-055 precedence metadata

T-PR-056 exception registration

T-PR-057 exception revocation

T-PR-058 audit reconstruction

T-PR-059 selective invalidation

T-PR-060 policy-engine handoff
```

---

# 110. Adversarial Tests

Recommended adversarial cases:

```text
same policy ID and version with different content;

different policy IDs pointing to identical copied source;

policy file renamed to impersonate canonical policy;

newest timestamp used to override explicit supersession;

higher version number used to override unrelated policy;

revoked policy restored from stale cache;

quarantined policy returned as active;

alias redirected without provenance;

supersession graph contains cycle;

scope removed from narrow policy;

development policy relabeled production;

registry snapshot rolled back;

policy inserted without authority;

three copies of one policy counted as independent authority;

generated MODEL policy labeled SOURCE_CANON;

partial multi-policy activation leaves two policies active;

missing registry partition interpreted as no governing policy;

open-world coverage mislabeled complete.
```

---

# 111. Validator Outcomes

Registry validators SHOULD return:

```text
VALID

INVALID

CONFLICT

REVALIDATE

QUARANTINE

UNKNOWN_GAP
```

No validator failure should silently become `VALID`.

---

# 112. Falsifiers

Claims that the registry is valid for a particular operation are falsified if reliable evidence shows:

```text
policy identity cannot be resolved;

material content differs from recorded hash;

version identity is inconsistent;

source provenance is false;

revoked policy appears active;

quarantined policy appears active;

supersession lineage is wrong;

scope is wider than authorized;

regime is wider than authorized;

expired policy appears current;

registry coverage was overstated;

alias resolves incorrectly;

dependency graph is corrupted;

registry state was rolled back;

unauthorized mutation occurred;

or historical policy state cannot be reconstructed.
```

---

# 113. Agents

The registry MAY use functional agent roles such as:

```text
POLICY_INGESTION_AGENT

POLICY_IDENTITY_AGENT

POLICY_PROVENANCE_AGENT

POLICY_VERSION_AGENT

POLICY_DEPENDENCY_AGENT

POLICY_SUPERSESSION_AGENT

POLICY_DISCOVERY_AGENT

POLICY_INTEGRITY_AUDITOR

POLICY_REGISTRY_REPAIR_AGENT
```

These are architectural roles.

They do NOT automatically possess mutation authority.

---

# 114. Agent Boundary

```text
AGENT_CAN_PROPOSE_REGISTRATION
!=
AGENT_CAN_ACTIVATE_POLICY
```

and:

```text
AGENT_CAN_DISCOVER_POLICY
!=
AGENT_CAN_MUTATE_REGISTRY
```

and:

```text
AGENT_ROLE
!=
AUTHORITY
```

---

# 115. Skills

Relevant Skill classes MAY include:

```text
canon consistency;
policy parsing;
ontology compilation;
provenance validation;
source reading;
policy conflict analysis;
law hierarchy resolution;
constraint propagation;
registry integrity;
commit-time authorization;
governed evolution;
repair/recovery.
```

Skill presence establishes addressable capability only.

```text
SKILL_AVAILABLE != AUTHORITY
```

---

# 116. Canonical Registry Workflow

```text
01 RECEIVE POLICY SOURCE

02 CLASSIFY SOURCE

03 PRESERVE SOURCE IDENTITY

04 PRESERVE SOURCE HASH / VERSION WHERE AVAILABLE

05 ASSIGN CANDIDATE POLICY ID

06 ASSIGN NAMESPACE

07 VALIDATE SCHEMA

08 VALIDATE IDENTITY

09 VALIDATE CONTENT IDENTITY

10 VALIDATE PROVENANCE

11 VALIDATE SOURCE/CANON CLASS

12 DECLARE SCOPE

13 DECLARE REGIME

14 DECLARE TEMPORAL ENVELOPE

15 RESOLVE DEPENDENCIES

16 RESOLVE ALIASES

17 RESOLVE POLICY FAMILY

18 RESOLVE H/M/L POSITION

19 CHECK EXISTING POLICY COLLISIONS

20 CHECK SUPERSESSION

21 CHECK REVOCATION

22 CHECK CANON CONFLICT

23 CHECK GOVERNANCE AUTHORITY

24 REGISTER AS DRAFT / QUARANTINE / REJECT

25 RUN VALIDATORS

26 ADMIT IF AUTHORIZED

27 ACTIVATE IF AUTHORIZED

28 BUILD DISCOVERY INDEXES

29 UPDATE REGISTRY SNAPSHOT

30 INVALIDATE AFFECTED DEPENDENTS

31 PRESERVE AUDIT EVENT
```

---

# 117. Discovery Workflow

```text
01 RECEIVE DISCOVERY CONTEXT

02 VALIDATE REQUEST

03 RESOLVE REGISTRY SCOPE

04 DETERMINE COVERAGE MODE

05 QUERY ACTION INDEX

06 QUERY CAPABILITY INDEX

07 QUERY TARGET INDEX

08 QUERY EFFECT INDEX

09 QUERY PRINCIPAL INDEX

10 QUERY ENVIRONMENT INDEX

11 QUERY JURISDICTION INDEX

12 QUERY REGIME INDEX

13 EXPAND REQUIRED DEPENDENCIES

14 REMOVE INVALID STATUS OBJECTS

15 PRESERVE UNRESOLVED OBJECTS

16 RETURN CANDIDATE POLICY SET

17 RETURN COVERAGE STATE

18 RETURN REGISTRY SNAPSHOT
```

---

# 118. Protocol — Lookup

```yaml
policy_registry_lookup:
  policy_id: string
  version: null
```

Response:

```yaml
policy_registry_lookup_result:
  state:
    - FOUND
    - NOT_FOUND
    - CONFLICT
    - UNKNOWN_GAP

  policy: null

  registry_snapshot: {}
```

---

# 119. Protocol — Resolve Alias

```yaml
policy_registry_resolve_alias:
  alias: string
  namespace: null
  context: {}
```

Response:

```yaml
policy_alias_result:
  state:
    - RESOLVED
    - AMBIGUOUS
    - NOT_FOUND
    - UNKNOWN_GAP

  canonical_policy_ids: []
```

---

# 120. Protocol — Discover

```yaml
policy_registry_discover:
  principal: {}
  action: {}
  capability: {}
  target: {}
  effect: {}
  environment: {}
  jurisdiction: {}
  scope: {}
  regime: {}
  time: null
```

Response:

```yaml
policy_registry_discovery_result:
  candidates: []
  unresolved: []
  coverage: {}
  registry_snapshot: {}
```

---

# 121. Protocol — Register

```yaml
policy_registry_register:
  candidate_policy: {}
  source: {}
  provenance: {}
  authority_ref: null
```

Response:

```yaml
policy_registry_register_result:
  state:
    - REGISTERED
    - REJECTED
    - QUARANTINED
    - CONFLICT
    - UNKNOWN_GAP

  policy_ref: null
```

---

# 122. Protocol — Supersede

```yaml
policy_registry_supersede:
  predecessor: {}
  successor: {}

  scope: {}

  effective_at: timestamp

  authority_ref: string

  provenance: {}
```

---

# 123. Protocol — Revoke

```yaml
policy_registry_revoke:
  policy_id: string
  version: string

  effective_at: timestamp

  reason: string

  authority_ref: string

  provenance: {}
```

---

# 124. Protocol — Quarantine

```yaml
policy_registry_quarantine:
  policy_id: string
  version: string

  reason_code: string

  evidence_refs: []

  authority_ref: null
```

---

# 125. Policy Engine Handoff

The registry SHOULD hand the Policy Engine:

```yaml
policy_engine_registry_bundle:
  registry_id: string

  registry_snapshot: {}

  candidates:
    - policy_id: string
      version: string
      content_hash: string
      status: ACTIVE
      scope: {}
      regime: {}
      source_refs: []
      dependency_refs: []

  unresolved: []

  coverage: {}
```

---

# 126. Handoff Boundary

The registry MUST NOT send:

```text
final_decision = ALLOW
```

as a registry conclusion.

The Policy Engine determines concrete policy decisions.

---

# 127. Policy Read-Set Support

The registry SHOULD support exact retrieval identity:

```yaml
policy_read_identity:
  policy_id: string
  version: string
  content_hash: string
```

This enables the control plane and Policy Engine to revalidate only decision-forming policy objects.

---

# 128. Fine-Grained Freshness

Suppose:

```text
D1 reads P1 + P2
D2 reads P3
```

If:

```text
P2 changes
```

then:

```text
D1 → REVALIDATE
D2 → unchanged
```

unless a dependency graph proves `D2` is indirectly affected.

---

# 129. Registry-to-Control-Plane Boundary

The control plane MAY inspect registry state for freshness or provenance.

It SHOULD NOT use registry presence alone as authority.

```text
REGISTERED POLICY
!=
AUTHORITY WITNESS
```

---

# 130. Authority

Registry mutations SHOULD bind to explicit authority where required.

Recommended mutation authority fields:

```yaml
mutation_authority:
  authority_id: string

  principal: string

  permitted_operation: string

  registry_scope: {}

  policy_scope: {}

  valid_from: timestamp
  valid_until: timestamp

  provenance: {}
```

---

# 131. Authority Freshness

Authority used for policy mutation SHOULD be checked at mutation commit time when authority can change.

A valid historical authorization does not automatically establish present mutation authority.

---

# 132. Registry Observability

Recommended registry events:

```text
POLICY_REGISTERED

POLICY_VALIDATED

POLICY_ADMITTED

POLICY_ACTIVATED

POLICY_DEPRECATED

POLICY_SUPERSEDED

POLICY_REVOKED

POLICY_QUARANTINED

POLICY_RELEASED_FROM_QUARANTINE

POLICY_ALIAS_ADDED

POLICY_ALIAS_REMOVED

POLICY_DEPENDENCY_ADDED

POLICY_DEPENDENCY_REMOVED

POLICY_SCOPE_CHANGED

POLICY_REGIME_CHANGED

REGISTRY_GENERATION_CHANGED

REGISTRY_ROLLBACK_DETECTED

REGISTRY_REBUILT
```

---

# 133. Observability Boundary

Registry logs MUST remain inside the infrastructure-owned observability envelope.

Sensitive policy material MUST NOT be exposed merely for convenience.

---

# 134. Audit Record

```yaml
policy_registry_audit_event:
  event_id: string

  event_type: string

  policy_id: null
  version: null

  actor: null

  authority_ref: null

  old_state: null
  new_state: null

  timestamp: timestamp

  provenance: {}
```

---

# 135. Registry Performance

Optimization MAY use:

```text
indexes;
caches;
incremental dependency graphs;
incremental hashes;
precomputed alias maps;
policy-family indexes;
H/M/L indexes.
```

Optimization MUST NOT weaken:

```text
identity;
provenance;
revocation;
supersession;
scope;
regime;
conflict visibility;
coverage honesty;
auditability.
```

---

# 136. Cache Model

Registry cache entries SHOULD bind to authoritative object identity.

```yaml
registry_cache_entry:
  policy_id: string
  version: string
  content_hash: string

  registry_generation: string

  cached_at: timestamp

  expires_at: null
```

---

# 137. Cache Invariant

Cached state MUST NOT override authoritative:

```text
revocation;
supersession;
quarantine;
generation change;
content-hash mismatch.
```

---

# 138. Security Model

The registry SHOULD defend against:

```text
policy injection;

policy deletion;

policy substitution;

policy rollback;

policy downgrade;

policy duplication;

alias hijacking;

namespace collision;

version spoofing;

hash spoofing;

source spoofing;

provenance stripping;

scope widening;

regime widening;

revocation suppression;

quarantine bypass;

supersession manipulation;

coverage inflation;

unauthorized mutation;

registry snapshot rollback.
```

---

# 139. Trust Model

Trust is:

```text
local;
typed;
scoped;
provenance-aware;
version-aware;
regime-aware;
freshness-bounded.
```

The registry MUST NOT establish universal trust merely from inclusion.

---

# 140. Uncertainty

Registry uncertainty SHOULD be explicit.

```yaml
registry_uncertainty:
  identity: null
  version: null
  content_integrity: null
  provenance: null
  scope: null
  regime: null
  temporal: null
  dependency: null
  supersession: null
  coverage: null
```

---

# 141. Confidence Ceiling

For a registry-derived identity claim:

```text
C_registry ≤ min(
    C_identity,
    C_content,
    C_provenance,
    C_version,
    C_scope,
    C_regime,
    C_freshness
)
```

This is an AMOS MODEL confidence constraint.

---

# 142. RSCF Registry Capsule

```yaml
rscf:
  claim:
    id: "RSCF_POLICY_REGISTRY_OBJECT"
    class: DERIVED

  premises:
    - identity_valid
    - content_identity_valid
    - provenance_valid
    - status_valid
    - scope_valid
    - regime_valid
    - freshness_valid

  evidence: []

  provenance: []

  scope: {}

  regime: {}

  dependencies: []

  competing: []

  falsifiers: []

  confidence_ceiling: null
```

---

# 143. RSCF Selective Invalidation

If:

```text
policy provenance fails
```

invalidate claims dependent on that provenance.

Do not erase unrelated policy objects.

---

# 144. GMEF Integration

Changes to registry semantics SHOULD be governed when they affect:

```text
identity;
versioning;
status;
scope;
regime;
supersession;
revocation;
quarantine;
discovery;
coverage;
provenance;
authority;
mutation semantics.
```

---

# 145. Registry Change Manifest

```yaml
policy_registry_change:
  change_id: string

  from_version: string
  to_version: string

  change_class:
    - COSMETIC
    - SCHEMA
    - SEMANTIC
    - GOVERNANCE
    - AUTHORITY_BOUNDARY

  affected_contracts: []

  expected_behavior_changes: []

  risks: []

  validators_required: []

  rollback_plan: null

  approval_state: PROPOSED
```

---

# 146. Promotion Model

```text
STRUCTURAL_MODEL
        ↓
SCHEMA_VALIDATED
        ↓
STORAGE_IMPLEMENTED
        ↓
LOOKUP_IMPLEMENTED
        ↓
DISCOVERY_IMPLEMENTED
        ↓
MUTATION_IMPLEMENTED
        ↓
UNIT_TESTED
        ↓
INTEGRATION_TESTED
        ↓
ADVERSARIALLY_TESTED
        ↓
CONTROL_PLANE_VALIDATED
        ↓
GOVERNED_ACTIVE
```

No transition is automatic.

---

# 147. Implementation Requirements

An executable registry SHOULD eventually provide:

```text
persistent policy store;

stable IDs;

version store;

content hashing;

status transitions;

scope/regime indexes;

dependency graph;

supersession graph;

revocation store;

quarantine store;

alias resolver;

discovery API;

audit ledger;

freshness/read-set support;

mutation authorization;

atomic mutation support;

rollback/recovery.
```

This document does not claim those components currently exist.

---

# 148. Example Policy Object

```yaml
policy_object:
  policy_id: "POLICY::CONTROL_PLANE::DURABLE_EFFECT_RELEASE"

  namespace: "CONTROL_PLANE"

  version: "1.0.0"

  content_hash: "sha256:<digest>"

  title: "Durable Effect Release Policy"

  policy_class:
    - EFFECT_RELEASE
    - GOVERNANCE

  status: ACTIVE

  source:
    source_type: MODEL
    source_id: "AMOS_CONTROL_PLANE_POLICY"
    source_refs: []

  scope:
    system: "AMOS OS"

    effect_classes:
      - DURABLE
      - EXTERNAL

  regime:
    allowed_regimes:
      - GOVERNED_RUNTIME

  applies_to:
    principal_classes:
      - AGENT
      - SYSTEM

    effect_classes:
      - DURABLE
      - EXTERNAL

  dependencies:
    - "CAPABILITY_CONTRACT"
    - "AUTHORITY_WITNESS"
    - "EFFECT_RELEASE_STATE"

  supersedes: []

  superseded_by: []

  provenance:
    origin_architect: "Trang Phan"
    steward: "Trang Phan"
```

The example is an architectural illustration, not evidence that this exact policy is already canonically registered.

---

# 149. Example Supersession

```yaml
policy_supersession:
  supersession_id: "SUP_001"

  predecessor:
    policy_id: "POLICY::MEMORY::WRITE"
    version: "1.0.0"

  successor:
    policy_id: "POLICY::MEMORY::WRITE"
    version: "2.0.0"

  effective_at: "2026-08-26T00:00:00Z"

  scope:
    system: "AMOS OS"

  authority_ref: "AUTHORITY_REF"

  provenance: {}
```

---

# 150. Example Revocation

```yaml
policy_revocation:
  revocation_id: "REV_001"

  policy_id: "POLICY::AGENT::LEGACY_EXTERNAL_WRITE"

  version: "1.2.0"

  revoked_at: "2026-08-26T00:00:00Z"

  effective_at: "2026-08-26T00:00:00Z"

  reason: "Policy withdrawn"

  authority_ref: "AUTHORITY_REF"

  scope:
    system: "AMOS OS"

  provenance: {}
```

---

# 151. Example Discovery

Request:

```yaml
policy_registry_discover:
  principal:
    principal_type: AGENT

  action:
    action_class: WRITE

  capability:
    capability_id: "CAP_RESOURCE_WRITE"

  target:
    resource_class: PERSISTENT_RESOURCE

  effect:
    effect_class: DURABLE

  environment:
    name: PRODUCTION

  scope:
    system: "AMOS OS"
```

Possible registry response:

```yaml
policy_registry_discovery_result:
  candidates:
    - policy_id: "POLICY::CONTROL_PLANE::DURABLE_EFFECT_RELEASE"
      version: "1.0.0"
      content_hash: "sha256:<digest>"

    - policy_id: "POLICY::AUTHORITY::PERSISTENT_WRITE"
      version: "1.0.0"
      content_hash: "sha256:<digest>"

  unresolved: []

  coverage:
    world_assumption: CLOSED_WORLD
    completeness: COMPLETE

  registry_snapshot:
    registry_id: "AMOS_POLICY_REGISTRY"
    generation: "G1"
    version: "1"
    snapshot_hash: "sha256:<registry-digest>"
```

The response identifies candidates.

It does not issue `ALLOW`.

---

# 152. Example Open-World Discovery

```yaml
policy_registry_discovery_result:
  candidates:
    - policy_id: "POLICY::DOMAIN::RESOURCE_ACCESS"
      version: "1.0.0"

  unresolved:
    - "external jurisdiction policy may apply"

  coverage:
    world_assumption: OPEN_WORLD
    completeness: PARTIAL
```

The Policy Engine MUST preserve the unresolved coverage if it could change the decision.

---

# 153. Example Identity Conflict

Observed:

```text
policy_id = POLICY::SECURITY::WRITE
version = 2.0.0
hash = HASH_A
```

then another object claims:

```text
policy_id = POLICY::SECURITY::WRITE
version = 2.0.0
hash = HASH_B
```

with:

```text
HASH_A != HASH_B
```

Registry result:

```text
CONFLICT
```

or:

```text
QUARANTINE
```

until authoritative identity is resolved.

---

# 154. Example Provenance Sybil

Suppose:

```text
POLICY_A
POLICY_B
POLICY_C
```

all derive from:

```text
SOURCE_X
```

Then:

```text
IndependentSourceCount = 1
```

unless additional independent authority exists.

---

# 155. Example Selective Invalidation

```text
D1 ← P1 + P2
D2 ← P3
D3 ← P2 + P4
```

If registry mutation changes:

```text
P2
```

then the system SHOULD identify:

```text
D1 → REVALIDATE
D3 → REVALIDATE
D2 → PRESERVE
```

subject to hidden dependency checks.

---

# 156. Audit Surface

An auditor SHOULD be able to answer:

1. What policy IDs exist?
2. In which namespaces?
3. Which versions exist?
4. What content hash belongs to each version?
5. What source produced each policy?
6. What source class does it have?
7. Who registered it?
8. Under what authority?
9. What is its current status?
10. When did that status change?
11. What is its scope?
12. What is its regime?
13. What is its temporal validity?
14. What dependencies does it have?
15. What aliases resolve to it?
16. What policies does it supersede?
17. What supersedes it?
18. Has it been revoked?
19. Has it been quarantined?
20. What policy family contains it?
21. What H/M/L level does it occupy?
22. What registry coverage claims exist?
23. Is coverage closed-world or open-world?
24. What registry snapshot exposed it?
25. What mutations affected it?
26. Can historical state be reconstructed?
27. Are its provenance sources independent?
28. What decisions depend on it?
29. What invalidation events affect those decisions?
30. What unresolved gaps remain?

---

# 157. Completion Matrix

| Surface                | Specification State |
| ---------------------- | ------------------- |
| Purpose                | COMPLETE_AS_MODEL   |
| Architecture           | COMPLETE_AS_MODEL   |
| Policy object          | COMPLETE_AS_MODEL   |
| Identity               | COMPLETE_AS_MODEL   |
| Namespace              | COMPLETE_AS_MODEL   |
| Classification         | COMPLETE_AS_MODEL   |
| Status                 | COMPLETE_AS_MODEL   |
| Registration           | COMPLETE_AS_MODEL   |
| Source/canon boundary  | COMPLETE_AS_MODEL   |
| Provenance             | COMPLETE_AS_MODEL   |
| Content identity       | COMPLETE_AS_MODEL   |
| Versioning             | COMPLETE_AS_MODEL   |
| Supersession           | COMPLETE_AS_MODEL   |
| Partial supersession   | COMPLETE_AS_MODEL   |
| Revocation             | COMPLETE_AS_MODEL   |
| Quarantine             | COMPLETE_AS_MODEL   |
| Scope                  | COMPLETE_AS_MODEL   |
| Regime                 | COMPLETE_AS_MODEL   |
| Temporal validity      | COMPLETE_AS_MODEL   |
| Dependencies           | COMPLETE_AS_MODEL   |
| Aliases                | COMPLETE_AS_MODEL   |
| Families               | COMPLETE_AS_MODEL   |
| H/M/L                  | COMPLETE_AS_MODEL   |
| Discovery              | COMPLETE_AS_MODEL   |
| Coverage               | COMPLETE_AS_MODEL   |
| Registry snapshot      | COMPLETE_AS_MODEL   |
| Fine-grained read sets | COMPLETE_AS_MODEL   |
| Registry generation    | COMPLETE_AS_MODEL   |
| Mutation               | COMPLETE_AS_MODEL   |
| Atomic mutation        | COMPLETE_AS_MODEL   |
| Admission              | COMPLETE_AS_MODEL   |
| Precedence metadata    | COMPLETE_AS_MODEL   |
| Exceptions             | COMPLETE_AS_MODEL   |
| Integrity              | COMPLETE_AS_MODEL   |
| Agents                 | COMPLETE_AS_MODEL   |
| Skills                 | COMPLETE_AS_MODEL   |
| Workflows              | COMPLETE_AS_MODEL   |
| Protocols              | COMPLETE_AS_MODEL   |
| Failure modes          | COMPLETE_AS_MODEL   |
| Repair/recovery        | COMPLETE_AS_MODEL   |
| Tests                  | COMPLETE_AS_MODEL   |
| Falsifiers             | COMPLETE_AS_MODEL   |
| RSCF                   | COMPLETE_AS_MODEL   |
| GMEF                   | COMPLETE_AS_MODEL   |
| Executable registry    | UNKNOWN/GAP         |
| Persistent storage     | UNKNOWN/GAP         |
| Executed validators    | UNKNOWN/GAP         |
| Production deployment  | UNKNOWN/GAP         |
| Formal verification    | UNKNOWN/GAP         |
| Canon admission        | UNKNOWN/GAP         |

---

# 158. RSCF Completion State

```yaml
rscf_completion:
  claim:
    id: "AMOS_POLICY_REGISTRY"
    class: MODEL

    text: >
      This artifact defines a structurally complete AMOS OS
      policy identity, versioning, provenance, discovery,
      supersession, revocation, and registry-governance architecture.

  evidence:
    - "AMOS infrastructure/control-plane architecture"
    - "associated policy-engine and policy-decision surfaces"

  provenance:
    origin_architect: "Trang Phan"
    steward: "Trang Phan"

  scope:
    system: "AMOS OS"
    component: "Policy Registry"

  regime:
    - DESIGN
    - ARCHITECTURE
    - GOVERNANCE_MODEL

  freshness:
    artifact_version: "1.0.0"
    updated: "2026-08-26"

  dependencies:
    - POLICY_ENGINE.md
    - POLICY_DECISION.md
    - CAPABILITY_MANIFEST.md
    - CAPABILITY_CONTRACT.md
    - CONTROL_PLANE_MAP.md

  competing: []

  falsifiers:
    - "policy identity cannot be reconstructed"
    - "policy version/content identity diverges silently"
    - "revoked policies remain active"
    - "supersession lineage is lost"
    - "registry coverage is overstated"
    - "registered policy is treated as authority"
    - "registry issues final policy decisions"

  confidence_ceiling: 0
```

`confidence_ceiling: 0` means this document does not claim empirical/runtime validation.

It does not mean the architecture is empty.

---

# 159. Hard Boundary Block

```text
POLICY_REGISTRY != POLICY_ENGINE

POLICY_REGISTRY != POLICY_DECISION

POLICY_REGISTRY != AUTHORITY_REGISTRY

POLICY_REGISTRY != CAPABILITY_REGISTRY

POLICY_REGISTRY != CONTROL_PLANE

POLICY_REGISTRY != EXECUTION_ENGINE

POLICY_REGISTRY != COMMIT_ENGINE

POLICY_REGISTRY != EFFECT_RELEASE_LEDGER

REGISTERED != ACTIVE

REGISTERED != CANONICAL

ACTIVE != APPLICABLE

APPLICABLE != ALLOW

DISCOVERED != GOVERNING

DISCOVERED != APPLICABLE

POLICY_EXISTS != POLICY_PERMITS

POLICY_METADATA != POLICY_TRUTH

POLICY_SOURCE != CANONICAL_STATUS

POLICY_ALIAS != INDEPENDENT_POLICY

COPY != INDEPENDENT_SOURCE

CORRELATED_PROVENANCE != INDEPENDENT_CONFIRMATION

NEWER != SUPERSEDING

HIGHER_VERSION != HIGHER_AUTHORITY

CAPABILITY != AUTHORITY

POLICY_ALLOW != AUTHORITY

VALIDATION != AUTHORIZATION

AUTHORIZATION != EXECUTION

PROPOSAL != COMMIT

EXECUTION != FINALITY

UNKNOWN/GAP != PASS

UNKNOWN/GAP != ACTIVE

UNKNOWN/GAP != ALLOW

CONFLICT != RESOLVED

PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

STRUCTURAL_MODEL != EXECUTABLE_RUNTIME

IMPLEMENTED != VALIDATED

TESTED != FORMALLY_VERIFIED

MODEL != EMPIRICAL_FACT
```

---

# 160. Canon Boundary

Trang Phan remains the origin architect and steward of AMOS.

This artifact defines a substantive proposed architecture for the AMOS `POLICY_REGISTRY.md` surface.

Its structural completeness does not itself establish:

```text
runtime implementation;

persistent storage implementation;

executed validation;

formal verification;

production deployment;

or canonical admission.
```

Until separately admitted through the appropriate AMOS canon/provenance/governance/supersession process:

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

# 161. Final Policy Registry Contract

AMOS SHALL preserve the following conceptual registry chain:

```text
SOURCE / GOVERNANCE MATERIAL
        ↓
SOURCE CLASSIFICATION
        ↓
PROVENANCE BINDING
        ↓
POLICY IDENTITY
        ↓
NAMESPACE
        ↓
VERSION
        ↓
CONTENT IDENTITY
        ↓
STATUS
        ↓
SCOPE / REGIME / TIME
        ↓
DEPENDENCIES
        ↓
SUPERSESSION / REVOCATION
        ↓
QUARANTINE / ADMISSION
        ↓
DISCOVERY INDEX
        ↓
POLICY CANDIDATE SET
        ↓
POLICY ENGINE
```

The central registry invariant is:

> **The AMOS Policy Registry establishes what policy objects are addressable, identifiable, versioned, provenance-bound, discoverable, and currently represented within a declared registry scope. It does not decide whether a concrete action is permitted.**

Therefore:

```text
POLICY_REGISTRY
    ↓
POLICY CANDIDATES
    ↓
POLICY_ENGINE
    ↓
POLICY_DECISION
```

and never automatically:

```text
POLICY_REGISTRY
    ↓
ALLOW
```

nor:

```text
POLICY_REGISTRY
    ↓
AUTHORITY
```

nor:

```text
POLICY_REGISTRY
    ↓
COMMIT
```

A policy's presence in the registry means only that the registry can identify and reason about that policy according to its recorded status, provenance, scope, regime, temporal envelope, and governance state.

AMOS MUST NOT convert registration into applicability.

AMOS MUST NOT convert applicability metadata into permission.

AMOS MUST NOT convert policy presence into authority.

AMOS MUST NOT convert newest timestamp into supersession.

AMOS MUST NOT convert higher version number into higher authority.

AMOS MUST NOT convert duplicated provenance into independent confirmation.

AMOS MUST NOT erase revocation or supersession history.

AMOS MUST NOT silently widen scope or regime.

AMOS MUST preserve exact policy identity wherever decisions depend upon policy state.

AMOS SHOULD invalidate only conclusions dependent on changed policy objects where dependency closure is known.

AMOS MUST preserve unresolved policy identity, provenance, scope, coverage, dependency, supersession, or authority uncertainty as:

```text
UNKNOWN/GAP
```

or the appropriate:

```text
CONFLICT
QUARANTINE
REVALIDATE
```

state.

Integrity remains prior to completeness, fluency, speed, and optimization.

---

# END — POLICY_REGISTRY.md

```
```

---

[[00_ROOT_MOC]]|[[AMOS MOC]]

---
**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: policy_registry
node_type: note
path: 03_CONTROL_PLANE/03_POLICY/POLICY_REGISTRY.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[03_POLICY_MOC]]
