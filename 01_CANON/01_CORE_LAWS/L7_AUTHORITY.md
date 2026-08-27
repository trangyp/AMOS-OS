---
title: L7 AUTHORITY
type: note
tags: [note, 01-core-laws]
---

````markdown
---
tags: ['canon', 'core_laws', 'authority', 'authorization', 'delegation', 'revocation', 'control_plane', 'rscf', 'governance']
title: "L7 Authority Boundary Laws"
origin_architect: "Trang Phan"
updated: "2026-08-26"
status: "PROPOSED_SPECIFICATION"
epistemic_class: "AMOS_MODEL"
canonical_status: "CONDITIONAL"
implementation_status: "LOGIC_EXECUTABLE_IN_PART"
---

# L7 Authority Boundary Laws

**Origin architect / steward:** Trang Phan  
**Layer:** `01_CANON / 01_CORE_LAWS / L7_AUTHORITY`  
**Artifact class:** `CORE_LAW_CONTRACT`  
**Status:** `PROPOSED_SPECIFICATION / AMOS_MODEL`  
**Canonical status:** `CONDITIONAL`  
**Implementation status:** `LOGIC_EXECUTABLE_IN_PART`

> L7 governs who or what may authorize an AMOS action, which authority is valid for which effect, how authority is delegated and attenuated, when authority expires or is revoked, and what evidence must exist before a proposed effect may become a commitment.
>
> Capability never creates authority.

---

# 0. Status

This document expands the supplied L7 seed specification:

```text
A-1 Separation
A-2 Typed & Scoped
A-3 Revocable
A-4 Non-Self-Issued
````

and the supplied implementation claim:

```text
authz_invariant_engine.py executes these families
(INV-001..050): 17/17 probes pass.
```

The seed laws are source-supplied for this artifact.

The broader structures below are a proposed AMOS structural completion and remain:

```text
AMOS_MODEL
```

until reconciled with authoritative AMOS authority canon and executable runtime evidence.

Hard boundary:

```text
SPECIFIED != IMPLEMENTED
IMPLEMENTED != VALIDATED
TEST_PASS != UNIVERSAL_PROOF
CAPABILITY != AUTHORITY
```

The statement that `17/17 probes pass` is preserved as a supplied implementation claim. Without the relevant executable harness, environment, source version, and raw results in this artifact, it MUST NOT be silently promoted into independently verified runtime evidence.

---

# 1. Purpose

L7 establishes the authority boundary of AMOS.

Its purpose is to ensure that the system can distinguish:

```text
what CAN be done
```

from:

```text
what MAY be done
```

from:

```text
what POLICY currently permits
```

from:

```text
what has been PROPOSED
```

from:

```text
what has actually been COMMITTED
```

The governing principle is:

```text
CAPABILITY
DOES NOT
IMPLY AUTHORITY
```

An AMOS component may possess:

* knowledge;
* reasoning ability;
* credentials;
* tools;
* network access;
* write access;
* executable code;
* a valid plan;

while still lacking authority to perform a particular effect.

---

# 2. Core Authority Boundary

The minimum distinction is:

```text
CAPABILITY
!=
AUTHORITY
!=
POLICY_ALLOW
!=
EVENT
!=
COMMITMENT
```

These states MUST remain independently typed.

A system capable of producing an effect does not automatically possess permission to produce it.

A policy allowing an action does not itself constitute a grant of authority.

An observed event does not prove that the event was authorized.

A proposal does not constitute a commitment.

---

# 3. A-1 — Separation

**Law:**

```text
CAPABILITY != AUTHORITY != POLICY_ALLOW != EVENT != COMMITMENT
```

L7 MUST preserve these distinctions across reasoning, orchestration, delegation, execution, memory, logging, and recovery.

Conceptually:

```text
Capability(P, A)
```

means principal `P` is technically capable of action `A`.

```text
Authority(P, A, S, E)
```

means principal `P` possesses authority for action `A`, within scope `S`, during authority epoch `E`.

```text
PolicyAllow(P, A, C)
```

means applicable policy permits the action under context `C`.

```text
Commit(P, A)
```

means the authorized effect has crossed the applicable commitment boundary.

None of these predicates is interchangeable.

---

# 4. Capability

Capability answers:

```text
CAN THIS PRINCIPAL OR COMPONENT PERFORM THIS OPERATION?
```

Capability MAY arise from:

* tool access;
* executable code;
* credentials;
* network reachability;
* API availability;
* model competence;
* file permissions;
* runtime configuration;
* delegated technical capability.

Capability is a technical property.

It is not authorization.

Therefore:

```text
HAS_TOOL(P,T)
!=
AUTHORIZED_TO_USE(P,T,A)
```

---

# 5. Authority

Authority answers:

```text
IS THIS PRINCIPAL ENTITLED TO CAUSE THIS EFFECT?
```

Authority MUST be:

* typed;
* scoped;
* attributable;
* temporally valid;
* epoch-bound where applicable;
* revocable;
* provenance-bound;
* non-self-issued;
* inspectable before consequential commitment.

Conceptually:

```text
AuthorityGrant =
(
  issuer,
  subject,
  capability,
  action,
  resource,
  scope,
  constraints,
  issued_at,
  valid_from,
  expires_at,
  epoch,
  delegation_depth,
  provenance,
  revocation_state
)
```

This is an AMOS structural model, not a claim about an existing implementation schema.

---

# 6. A-2 — Typed & Scoped Authority

Authority is never ambient.

Canonical law:

```text
AUTHORITY
=
GRANT(
  principal,
  scope,
  epoch
)
```

with additional typing where required.

Authority MUST NOT be interpreted as:

```text
principal is trusted
→
principal may do anything
```

Instead:

```text
authority(P, scope=S1)
```

does not imply:

```text
authority(P, scope=S2)
```

unless an explicit valid grant establishes that relationship.

---

# 7. Scope Dimensions

Authority scope MAY include:

```text
action
resource
resource_class
recipient
environment
workspace
repository
account
tenant
data_class
effect_type
financial_limit
time_window
geography
purpose
workflow
protocol
tool
delegation_depth
```

A grant MAY bind several dimensions simultaneously.

Example:

```yaml
authority:
  principal: agent_A
  action: update
  resource: project_X
  environment: staging
  financial_limit: 0
  valid_until: ...
```

does not authorize:

```text
production deployment
```

or:

```text
financial transaction
```

unless explicitly included.

---

# 8. Scope Contraction

Delegation MAY narrow authority.

Conceptually:

```text
Scope(child)
⊆
Scope(parent)
```

A child grant MUST NOT silently expand beyond the parent's authority envelope.

Therefore:

```text
DELEGATION
MUST NOT
CREATE NEW AUTHORITY
```

unless a separate legitimate authority source explicitly grants it.

---

# 9. Scope Intersection

When multiple authority constraints apply, effective authority SHOULD be the compatible intersection of applicable constraints.

Conceptually:

```text
EffectiveScope
=
S1 ∩ S2 ∩ ... ∩ Sn
```

where the relevant scope semantics support intersection.

This means policy composition should normally tighten rather than expand authority.

---

# 10. Authority Epoch

Authority SHOULD be evaluated relative to an authority epoch or equivalent freshness boundary.

Conceptually:

```text
Authority(P,A,E1)
```

does not automatically imply:

```text
Authority(P,A,E2)
```

if authority state changed between epochs.

An epoch provides a boundary for changes such as:

* grant;
* delegation;
* revocation;
* policy change;
* principal state change;
* role change;
* constraint change.

---

# 11. Epoch Freshness

A valid historical authority witness does not prove current authority.

Therefore:

```text
VALID_AT(E1)
!=
VALID_AT(E2)
```

unless continuity is established.

Commit-time authority evaluation SHOULD use sufficiently fresh authority state for the consequence of the operation.

---

# 12. A-3 — Revocable

Authority MUST be revocable unless authoritative canon explicitly defines a non-revocable authority class.

Supplied law:

```text
revocation takes effect
at the current epoch
without grace drift
```

Therefore:

```text
REVOKED(E)
→
NOT_AUTHORIZED(E)
```

for effects requiring that revoked grant at or after the effective revocation boundary.

---

# 13. No Grace Drift

A cached authorization decision MUST NOT create an implicit grace period after revocation.

Invalid pattern:

```text
authorized at t1
cached result
revoked at t2
commit at t3
→ allow because cache still says authorized
```

when:

```text
t1 < t2 < t3
```

Required behavior:

```text
REVALIDATE AUTHORITY
AT THE APPLICABLE COMMIT BOUNDARY
```

---

# 14. Revocation State

A conceptual authority state MAY include:

```yaml
revocation:
  status: ACTIVE | REVOKED | UNKNOWN
  revoked_at: ...
  effective_epoch: ...
  issuer: ...
  reason: ...
  provenance: ...
```

If revocation state is:

```text
UNKNOWN
```

and the operation requires positive current authority, the system SHOULD fail closed.

---

# 15. A-4 — Non-Self-Issued Authority

Agents cannot authorize themselves.

Canonical boundary:

```text
AGENT
CANNOT
CREATE ITS OWN ROOT AUTHORITY
```

An agent may:

* request authority;
* propose a grant;
* evaluate a grant;
* validate a grant;
* consume delegated authority;

but MUST NOT transform:

```text
I need permission
```

into:

```text
I grant myself permission
```

---

# 16. Root Authority

The supplied L7 seed states:

```text
delegation chains terminate at a human root
```

Within this proposed specification, that is preserved as the governing root rule.

Conceptually:

```text
HumanRoot
  ↓
Delegation
  ↓
Agent / Service / Sub-Agent
```

The chain MUST remain traceable.

No delegation chain may legitimately terminate at:

```text
self-generated agent authority
```

under this law.

---

# 17. Root Authority Identity

A root authority SHOULD identify:

```yaml
root_authority:
  principal_id: ...
  principal_type: HUMAN
  scope: ...
  issued_at: ...
  provenance: ...
```

The existence of a human identity alone does not establish a grant.

A valid root must be bound to the relevant scope.

---

# 18. Delegation

Delegation transfers or permits use of a subset of authority from an authorized principal to another principal.

Conceptually:

```text
Delegate(
  parent,
  child,
  scope,
  constraints
)
```

A delegation is valid only if the parent possesses sufficient authority to delegate that scope.

---

# 19. Delegation Invariant

For every delegated grant:

```text
Authority(child)
⊆
DelegableAuthority(parent)
```

Therefore:

```text
child authority
>
parent authority
```

is invalid unless another independent authority source supplies the difference.

---

# 20. Delegation Depth

Authority MAY specify maximum delegation depth.

Example:

```yaml
delegation:
  max_depth: 2
```

If:

```text
Human → Agent A → Agent B
```

uses the full depth, Agent B MUST NOT further delegate if that would exceed the grant.

---

# 21. Delegation Constraints

Delegated authority MAY be narrowed by:

* action type;
* resource;
* recipient;
* duration;
* amount;
* environment;
* tool;
* purpose;
* data class;
* delegation depth;
* required approval;
* reversibility;
* consequence class.

Delegation MUST NOT silently remove parent constraints.

---

# 22. Attenuation

Delegated authority SHOULD be attenuating.

Conceptually:

```text
Constraints(child)
≥
Constraints(parent)
```

in restrictiveness.

A child grant may be narrower.

It must not become less constrained unless an independently authorized grant permits expansion.

---

# 23. Authority Witness

A consequential action SHOULD carry or reference an authority witness sufficient to establish why the action is authorized.

Conceptually:

```yaml
authority_witness:
  witness_id: ...
  principal: ...
  action: ...
  resource: ...
  scope: ...
  authority_source: ...
  delegation_chain: [...]
  policy_decision: ...
  epoch: ...
  freshness: ...
  constraints: [...]
  provenance: [...]
```

An authority witness is evidence of authority evaluation.

It is not authority merely because the object exists.

---

# 24. Witness Integrity

An authority witness MUST correspond to the actual proposed effect.

Therefore:

```text
WITNESS(action=A)
```

cannot authorize:

```text
COMMIT(action=B)
```

unless the witness scope explicitly includes `B`.

This is effect binding.

---

# 25. Effect Binding

Authority MUST be bound to the effect that will actually occur.

Conceptually:

```text
Witness.effect
=
ProposedCommit.effect
```

within permitted equivalence rules.

This prevents:

```text
authorize read
→ perform write
```

or:

```text
authorize $100
→ commit $1,000
```

---

# 26. Resource Binding

Authority for resource `R1` MUST NOT automatically authorize resource `R2`.

```text
AUTH(P,R1)
!=
AUTH(P,R2)
```

unless scope explicitly includes both.

Aliases and indirect resource references SHOULD resolve to canonical resource identity before consequential commitment.

---

# 27. Recipient Binding

Where disclosure or transfer authority depends on recipient:

```text
AUTH(send data D to recipient R1)
```

does not imply:

```text
AUTH(send D to R2)
```

Recipient changes require revalidation when recipient is authority-relevant.

---

# 28. Purpose Binding

Where authority is purpose-limited:

```text
AUTHORIZED_FOR(PURPOSE_1)
```

does not imply:

```text
AUTHORIZED_FOR(PURPOSE_2)
```

even if the same capability and resource are involved.

---

# 29. Temporal Binding

Authority MAY contain:

```text
valid_from
expires_at
epoch
```

A grant outside its temporal validity window is invalid.

Therefore:

```text
EXPIRED
→
NOT_CURRENTLY_AUTHORIZED
```

---

# 30. Authority State

A conceptual authority state MAY be:

```text
VALID
INVALID
EXPIRED
REVOKED
SUPERSEDED
UNKNOWN
CONFLICTING
```

`UNKNOWN` and `CONFLICTING` MUST NOT be interpreted as `VALID`.

---

# 31. Positive Authorization Requirement

For consequential effects requiring authorization:

```text
absence of denial
```

is not sufficient.

Required:

```text
positive valid authority evidence
```

Therefore:

```text
NOT_DENIED
!=
AUTHORIZED
```

---

# 32. Policy Allow

Policy answers:

```text
DO CURRENT RULES ALLOW THIS ACTION
UNDER THIS CONTEXT?
```

Policy evaluation MAY return:

```text
ALLOW
DENY
CONDITIONAL
ESCALATE
UNKNOWN
```

Policy is separate from authority.

---

# 33. Authority vs Policy

Possible state:

```text
authority = VALID
policy = DENY
```

Result:

```text
NO COMMIT
```

Possible state:

```text
authority = INVALID
policy = ALLOW
```

Result:

```text
NO COMMIT
```

Therefore, for an action requiring both:

```text
COMMIT_ELIGIBLE
=
AUTHORITY_VALID
AND
POLICY_ALLOW
```

plus any additional applicable constraints.

---

# 34. Policy Cannot Manufacture Authority

A policy engine MUST NOT transform:

```text
POLICY_ALLOW
```

into:

```text
AUTHORITY_GRANTED
```

unless the policy system itself is explicitly defined as an authorized issuer under authoritative canon.

Default boundary:

```text
POLICY_ALLOW != AUTHORITY_GRANT
```

---

# 35. Capability Manifest

A capability manifest describes what a component can potentially do.

Example:

```yaml
capabilities:
  - read_file
  - write_file
  - send_message
```

It MUST NOT be interpreted as:

```yaml
authority:
  - read_file
  - write_file
  - send_message
```

Therefore:

```text
CAPABILITY_MANIFEST
!=
AUTHORIZATION_SPEC
```

---

# 36. Authorization Spec

An authorization specification SHOULD define:

* principals;
* authority types;
* scopes;
* resources;
* actions;
* constraints;
* delegation rules;
* revocation rules;
* witness requirements;
* freshness;
* commitment requirements;
* failure behavior.

This is a governance contract.

---

# 37. Proposal

A proposal is an intended action that has not crossed the commitment boundary.

Conceptually:

```yaml
proposal:
  principal: ...
  action: ...
  target: ...
  parameters: ...
  expected_effect: ...
```

Proposal generation MAY occur before final authority resolution.

But:

```text
PROPOSAL != COMMIT
```

---

# 38. Commitment

A commitment is the transition where an effect becomes durable, externally consequential, or otherwise crosses the defined effect boundary.

Examples may include:

* sending a message;
* writing persistent state;
* deleting a file;
* changing permissions;
* executing a trade;
* publishing content;
* transferring funds;
* modifying production state.

The exact commitment boundary is domain-specific.

---

# 39. Commit-Time Authorization

Authority SHOULD be revalidated at the latest safe point before commitment for consequential effects.

Conceptually:

```text
PROPOSE
↓
VALIDATE
↓
PREPARE
↓
REVALIDATE AUTHORITY
↓
COMMIT
```

This prevents stale authorization from surviving changes between proposal and effect.

---

# 40. Commit-Time Invariant

At commitment:

```text
AuthorityWitness.valid
AND
AuthorityWitness.current
AND
AuthorityWitness.matches_effect
AND
PolicyDecision.allow
AND
Constraints.satisfied
```

must hold for authority-requiring actions.

If any required term is false or critically unknown:

```text
COMMIT = DENIED
```

---

# 41. Time-of-Check / Time-of-Use

L7 explicitly guards against:

```text
TOCTOU authority failure
```

Example:

```text
t1: authority checked
t2: authority revoked
t3: effect committed
```

Without revalidation, the commit may use stale authority.

Therefore consequential operations SHOULD bind authority freshness to commitment.

---

# 42. Authority Freshness

Freshness SHOULD be proportional to consequence and mutability.

High-consequence actions require stronger freshness guarantees than low-impact reversible reads.

Conceptually:

```text
RequiredAuthorityFreshness
↑
as
Consequence × Irreversibility
↑
```

This is a governance heuristic, not an empirical law.

---

# 43. Revocation Propagation

Revocation SHOULD invalidate dependent delegated authority.

Example:

```text
Human H
  ↓ G1
Agent A
  ↓ G2
Agent B
```

If `G1` is revoked and `G2` depends exclusively on `G1`:

```text
G2
→
INVALID
```

unless Agent B has another independent valid authority path.

---

# 44. Selective Revocation

Revocation SHOULD invalidate only authority dependent on the revoked grant.

If:

```text
Agent B
← G2 from Agent A
← G3 independently from Human H2
```

revoking `G2` need not invalidate authority supplied independently by valid `G3`.

Therefore:

```text
REVOCATION
=
DEPENDENCY_SELECTIVE
```

---

# 45. Authority Provenance

Authority provenance SHOULD answer:

```text
Who issued this?
Under what authority?
When?
For whom?
For what scope?
Through which delegation chain?
Under which policy/version?
Has any ancestor been revoked?
```

A grant without sufficient provenance SHOULD remain untrusted or conditional according to consequence.

---

# 46. Delegation Chain

Conceptually:

```text
Root
  ↓
Grant G1
  ↓
Principal A
  ↓
Grant G2
  ↓
Principal B
  ↓
Grant G3
  ↓
Principal C
```

Every edge SHOULD identify:

```text
issuer
subject
scope
epoch
constraints
provenance
```

---

# 47. Broken Delegation Chain

If any load-bearing delegation edge becomes:

```text
INVALID
REVOKED
EXPIRED
UNKNOWN
```

then downstream authority dependent solely on that edge becomes invalid or unresolved.

```text
BROKEN_ANCESTRY
→
NO_VALID_DERIVED_AUTHORITY
```

---

# 48. Multiple Authority Paths

A principal MAY possess authority through more than one valid path.

Example:

```text
Root A → Agent X
Root B → Agent X
```

These paths SHOULD remain independently attributable.

Revocation of one path does not necessarily revoke the other.

---

# 49. Correlated Authority Evidence

Multiple records that represent the same grant MUST NOT be interpreted as multiple independent authority grants.

Therefore:

```text
MULTIPLE_WITNESSES
!=
MULTIPLE_AUTHORITIES
```

if they share the same authority origin.

---

# 50. Authority Conflict

Authority records may conflict.

Example:

```text
Grant G1: ALLOW action A
Revocation R1: REVOKE G1
```

or:

```text
Grant G1: scope includes X
Policy P1: X forbidden
```

Such conflicts MUST be resolved according to law hierarchy, temporal ordering, provenance, and applicable governance rules.

They MUST NOT be silently averaged.

---

# 51. Deny Precedence

Where applicable policy/law hierarchy defines a hard prohibition:

```text
HARD_DENY
```

MUST NOT be bypassed by a lower-level grant.

Conceptually:

```text
AUTHORITY
cannot override
higher-order prohibition
```

unless authoritative canon explicitly establishes such override power.

---

# 52. Only-Tighten Composition

When multiple applicable constraints govern an action, composition SHOULD normally be monotonic toward restriction.

```text
effective authority
≤
each applicable authority envelope
```

unless a higher-order authority explicitly supersedes a lower rule.

This prevents accidental privilege expansion through composition.

---

# 53. Authority Escalation

When required authority is absent, an agent MAY:

```text
REQUEST
ESCALATE
PROPOSE
WAIT
```

It MUST NOT:

```text
SELF_GRANT
BYPASS
FABRICATE_WITNESS
ASSUME_CONSENT
```

---

# 54. Human Approval

Human approval MAY create or satisfy authority only where the approving human possesses the required authority.

Therefore:

```text
HUMAN_APPROVAL
!=
VALID_AUTHORITY
```

unless:

```text
APPROVER
HAS_REQUIRED_AUTHORITY
```

---

# 55. Consent vs Authority

Consent and authority are related but distinct.

A person may consent to an action without possessing authority over all affected resources or principals.

Likewise, a system may have institutional authority while still requiring user consent.

Therefore:

```text
CONSENT != AUTHORITY
```

unless a specific domain contract defines the relationship.

---

# 56. Authentication vs Authorization

Authentication establishes identity.

Authorization establishes permitted action.

Therefore:

```text
AUTHENTICATED(P)
!=
AUTHORIZED(P,A)
```

A valid login is not universal authority.

---

# 57. Ownership vs Authority

Ownership MAY imply some authority under applicable policy, but:

```text
OWNER
!=
UNBOUNDED_AUTHORITY
```

by default.

Ownership may remain constrained by:

* law;
* policy;
* shared rights;
* organizational governance;
* safety constraints;
* delegation limits.

---

# 58. Role vs Authority

A role label does not itself prove authority.

```text
ROLE = ADMIN
```

must resolve to an actual authority policy/grant before consequential use.

Therefore:

```text
ROLE_NAME
!=
AUTHORITY_WITNESS
```

---

# 59. Credentials vs Authority

Possessing a credential proves only what that credential legitimately establishes.

```text
HAS_API_KEY
!=
AUTHORIZED_FOR_EVERY_API_EFFECT
```

Technical possession must not substitute for governance authority.

---

# 60. Tool Access

Tool availability is capability.

```text
TOOL_AVAILABLE
```

does not mean:

```text
TOOL_AUTHORIZED_FOR_CURRENT_ACTION
```

Agents MUST evaluate action-specific authority.

---

# 61. Memory and Authority

Persistent memory MUST NOT create authority.

A remembered statement such as:

```text
user previously allowed X
```

cannot automatically authorize a new consequential action unless the stored grant:

* remains valid;
* applies to the current action;
* applies to current scope;
* has not expired;
* has not been revoked;
* is permitted to persist.

Therefore:

```text
MEMORY != CURRENT_AUTHORITY
```

---

# 62. Cached Authority

Cached authority decisions MAY be used only within their valid freshness and epoch constraints.

A cache MUST carry sufficient state such as:

```yaml
cached_authority:
  decision: ALLOW
  epoch: ...
  valid_until: ...
  witness: ...
```

A cache lacking validity information SHOULD NOT authorize consequential commit.

---

# 63. Authority and RSCF

Authority-related conclusions SHOULD be represented as RSCF claims.

Example:

```yaml
claim:
  "Principal P may perform action A on resource R."

claim_class: DERIVED

evidence:
  - grant_G
  - policy_decision_P

dependencies:
  - root_authority
  - delegation_chain
  - current_epoch
  - resource_identity

falsifiers:
  - grant revoked
  - scope mismatch
  - resource changed
  - policy changed
  - epoch stale
```

---

# 64. Authority Claim Classes

Possible authority conclusions include:

```text
VERIFIED
DERIVED
CONDITIONAL
COMPETING
UNKNOWN/GAP
```

An authority conclusion MUST NOT be promoted merely because the system strongly expects authorization.

Authority requires valid authority evidence.

---

# 65. Unknown Authority

For authority-requiring effects:

```text
AUTHORITY = UNKNOWN
```

must yield:

```text
NO COMMIT
```

until resolved.

Therefore:

```text
UNKNOWN_AUTHORITY
!=
IMPLICIT_ALLOW
```

---

# 66. Ambiguous Authority

If two plausible authority interpretations remain unresolved:

```text
A1 = allow
A2 = deny
```

then:

```text
AUTHORITY = COMPETING / UNKNOWN
```

and consequential commitment SHOULD fail closed until discriminating evidence resolves the ambiguity.

---

# 67. H/M/L Applicability

## H — Governing Authority

H-level authority includes:

* root authority;
* constitutional constraints;
* canonical governance;
* organization-wide policy;
* global revocation;
* institutional control.

H-level authority constrains lower levels.

---

## M — Subsystem Authority

M-level authority includes:

* workflow authority;
* service authority;
* repository authority;
* department authority;
* agent-group authority;
* environment-specific delegation.

M authority cannot exceed governing H authority.

---

## L — Local Authority

L-level authority includes:

* specific tool call;
* specific file mutation;
* individual transaction;
* single message;
* single database update;
* single execution effect.

L-level action must remain within H and M constraints.

---

# 68. Cross-Scale Authority

Conceptually:

```text
Authority_L
⊆
Authority_M
⊆
Authority_H
```

where those layers form a delegation hierarchy.

This must not be assumed for unrelated authority structures.

Cross-scale relationships require explicit lineage.

---

# 69. Control-Plane Ownership

Authority enforcement is a control-plane responsibility.

Domain workers SHOULD NOT be the sole authority judge for their own consequential actions.

Conceptually:

```text
WORKER
→ proposes action

CONTROL PLANE
→ resolves authority
→ resolves policy
→ validates constraints
→ issues/validates witness
→ permits or blocks commit
```

This prevents cognition from manufacturing governance.

---

# 70. Worker Boundary

A worker MAY determine:

```text
"I can perform action A."
```

It MUST NOT infer:

```text
"Therefore I am authorized to perform A."
```

The worker may supply evidence to the authority resolver but does not become the authority source by proposing the evidence.

---

# 71. Authority Resolver

An authority resolver SHOULD:

1. identify principal;
2. identify proposed effect;
3. resolve canonical resource identity;
4. identify required authority type;
5. retrieve applicable grants;
6. validate issuer authority;
7. validate delegation chain;
8. validate scope;
9. validate epoch/freshness;
10. check revocation;
11. resolve policy;
12. evaluate constraints;
13. produce an authority decision;
14. produce or reference an authority witness.

---

# 72. Authority Decision

A conceptual authority decision:

```yaml
authority_decision:
  decision_id: ...
  principal: ...
  action: ...
  resource: ...

  authority_state:
    grant: VALID
    delegation: VALID
    scope: VALID
    epoch: CURRENT
    revocation: CLEAR

  policy:
    decision: ALLOW

  result: AUTHORIZED

  witness_id: ...
```

Possible results:

```text
AUTHORIZED
DENIED
CONDITIONAL
ESCALATE
UNKNOWN
```

---

# 73. Conditional Authority

Authority MAY be conditional.

Example:

```text
AUTHORIZED IF
  amount <= 100
  AND environment = staging
  AND reviewer_approval = true
```

The conditions MUST be evaluated before commitment.

Conditional authority is not unconditional authority.

---

# 74. Authority Witness Lifecycle

Conceptual lifecycle:

```text
REQUESTED
↓
RESOLVED
↓
ISSUED
↓
VALID
↓
USED
```

with possible transitions to:

```text
EXPIRED
REVOKED
SUPERSEDED
INVALIDATED
```

Witness state must not outlive underlying authority validity.

---

# 75. Witness Replay

An authority witness MUST NOT be replayable outside its permitted context.

Possible replay constraints include:

```text
single_use
resource_binding
action_binding
epoch_binding
nonce
expiry
transaction_binding
```

This prevents valid historical authorization from being reused for a different effect.

---

# 76. Witness Mutation

A witness MUST NOT be altered after authorization in a way that expands authority.

If material fields change:

```text
action
resource
recipient
amount
scope
constraints
```

the authority decision SHOULD be invalidated and recomputed.

---

# 77. Transaction Binding

Where an operation belongs to a transaction:

```text
Witness.transaction_id
=
Commit.transaction_id
```

SHOULD be required when transaction identity is authority-relevant.

A witness for one transaction must not authorize another by default.

---

# 78. Atomic Multi-Effect Authority

A transaction may contain multiple effects:

```text
E1
E2
E3
```

Authority MUST cover the complete committed effect set.

Authorization for:

```text
E1 + E2
```

does not automatically authorize:

```text
E1 + E2 + E3
```

---

# 79. Partial Authorization

If only part of a proposed transaction is authorized:

```text
authorized: E1, E2
unauthorized: E3
```

the system MUST NOT silently commit the whole transaction.

Permitted responses include:

```text
REJECT
SPLIT
REPLAN
REQUEST ADDITIONAL AUTHORITY
```

subject to transaction semantics.

---

# 80. Atomicity

Where effects are defined as an atomic unit, authority must be valid for the entire unit before commit.

```text
PARTIAL_AUTHORITY
!=
ATOMIC_TRANSACTION_AUTHORITY
```

---

# 81. Authority Mutation During Transaction

If authority changes while a transaction is pending:

```text
grant valid at prepare
revoked before commit
```

commit MUST revalidate.

If revocation invalidates a required authority:

```text
ABORT / ROLLBACK
```

subject to domain recovery semantics.

---

# 82. Authority and MVCC/CAS Concepts

Where AMOS uses MVCC/CAS-style reasoning patterns, authority state SHOULD participate in the observed state set for consequential commitment.

Conceptually:

```text
read authority epoch E1
prepare effect
compare current authority epoch
```

If:

```text
current_epoch != E1
```

then:

```text
REVALIDATE
```

rather than committing against stale authority state.

This is a reasoning/control pattern, not a claim that every ChatGPT execution literally implements MVCC.

---

# 83. Authority Causal Priority

Authority changes that causally precede commitment MUST be respected.

A commit must not claim legitimacy based on a grant superseded before the commit boundary.

Conceptually:

```text
REVOCATION
causally before
COMMIT
→
REVOKED AUTHORITY CANNOT LEGITIMIZE COMMIT
```

---

# 84. Finality Boundary

Once a legitimately authorized irreversible effect is committed, later revocation does not necessarily erase the historical fact that the earlier commit was authorized.

Therefore distinguish:

```text
authorized_at_commit
```

from:

```text
authorized_now
```

Revocation controls future authority unless domain rules define rollback or retroactive invalidation.

---

# 85. Event vs Authorization

Observed execution is not evidence of valid authority by itself.

```text
EVENT_OCCURRED
!=
EVENT_AUTHORIZED
```

Post-event auditing must reconstruct authority independently.

---

# 86. Audit Requirements

An authority audit SHOULD be able to answer:

```text
Who acted?
What action was proposed?
What effect occurred?
Which resource was affected?
Which grant authorized it?
Who issued the grant?
What was the delegation chain?
What policy applied?
What epoch was current?
Was authority revoked?
Was the witness fresh?
Did committed effect match authorized effect?
```

---

# 87. Audit Record

Conceptual audit record:

```yaml
authority_audit:
  event_id: ...
  principal: ...
  action: ...
  resource: ...
  effect: ...

  authority_witness: ...
  authority_epoch: ...
  delegation_chain: [...]

  policy_decision: ...
  constraints: [...]

  commit_time: ...
  commit_result: ...

  provenance: [...]
```

---

# 88. Authority Failure Modes

L7 recognizes at least the following failure classes.

### AF-1 — Capability/Authority Collapse

Technical capability is interpreted as permission.

### AF-2 — Ambient Authority

A principal is treated as globally authorized because it was authorized once.

### AF-3 — Scope Expansion

Authority is used outside granted scope.

### AF-4 — Delegation Amplification

Child authority exceeds parent authority.

### AF-5 — Self-Authorization

Agent creates its own authority.

### AF-6 — Broken Root

Delegation cannot be traced to a valid root.

### AF-7 — Stale Authorization

Commit uses an outdated authority decision.

### AF-8 — Revocation Drift

Revoked authority remains usable through stale cache or grace behavior.

### AF-9 — Witness Mismatch

Witness does not match committed effect.

### AF-10 — Resource Mismatch

Authority covers a different resource.

### AF-11 — Recipient Mismatch

Disclosure goes to a different recipient.

### AF-12 — Purpose Drift

Authority is used for a different purpose.

### AF-13 — Expired Authority

Expired grant is accepted.

### AF-14 — Policy/Authority Collapse

Policy allow is treated as authority grant.

### AF-15 — Authentication/Authorization Collapse

Identity proof is treated as action authority.

### AF-16 — Role/Authority Collapse

Role label is treated as sufficient authorization.

### AF-17 — Credential/Authority Collapse

Credential possession is treated as permission.

### AF-18 — Memory Authority Leakage

Historical memory is treated as current authority.

### AF-19 — Witness Replay

Old witness is reused outside valid context.

### AF-20 — Partial Transaction Authorization

Only part of an atomic transaction is authorized.

### AF-21 — Missing Commit Revalidation

Mutable authority state is not checked before effect.

### AF-22 — Unauthorized Delegation

Issuer delegates authority it does not possess.

### AF-23 — Revocation Propagation Failure

Dependent grants remain active after ancestor revocation.

### AF-24 — Over-Revocation

Independent authority paths are incorrectly destroyed.

### AF-25 — Event Legitimacy Fallacy

Occurred action is assumed authorized because it succeeded technically.

---

# 89. Repair / Recovery

Canonical conceptual recovery flow:

```text
DETECT AUTHORITY FAILURE
        ↓
FREEZE AFFECTED COMMIT PATH
        ↓
IDENTIFY PRINCIPAL
        ↓
IDENTIFY ACTUAL EFFECT
        ↓
RESOLVE REQUIRED AUTHORITY
        ↓
TRACE AUTHORITY ANCESTRY
        ↓
CHECK GRANTS / DELEGATIONS / REVOCATIONS
        ↓
CHECK SCOPE / EPOCH / POLICY
        ↓
IDENTIFY EARLIEST INVALID AUTHORITY EDGE
        ↓
INVALIDATE DEPENDENT WITNESSES
        ↓
RECOMPUTE AUTHORITY
        ↓
ROLLBACK / ABORT / REAUTHORIZE / ESCALATE
        ↓
REVALIDATE
```

---

# 90. Selective Authority Repair

Authority failure SHOULD invalidate only dependent authority paths.

Example:

```text
G1 → G2 → W1 → Commit C1
G3 → W2 → Commit C2
```

If `G1` fails:

```text
invalidate:
G2
W1
C1 eligibility
```

but do not automatically invalidate:

```text
G3
W2
C2
```

unless dependency exists.

---

# 91. Unauthorized Effect Recovery

If an unauthorized effect has already occurred, the system SHOULD distinguish:

```text
AUTHORITY REPAIR
```

from:

```text
EFFECT REPAIR
```

Restoring correct authority state does not automatically reverse the unauthorized external effect.

Recovery may require:

* rollback;
* compensation;
* notification;
* containment;
* audit;
* escalation;
* revocation;
* credential rotation;
* policy repair.

Domain rules determine the actual recovery.

---

# 92. Over-Authorization Repair

If a grant is discovered to be broader than intended:

```text
REVOKE / SUPERSEDE
```

the overbroad grant and issue a narrower replacement where authorized.

Historical descendants must be evaluated according to their dependency on the defective grant.

---

# 93. Validator Families

Conceptual L7 validators include:

```text
validate_capability_authority_separation()

validate_principal_identity()
validate_authority_type()
validate_authority_scope()
validate_authority_epoch()
validate_authority_freshness()

validate_root_authority()
validate_delegation_chain()
validate_delegation_attenuation()
validate_delegation_depth()

validate_revocation()
validate_revocation_propagation()

validate_policy_authority_separation()

validate_effect_binding()
validate_resource_binding()
validate_recipient_binding()
validate_purpose_binding()
validate_transaction_binding()

validate_authority_witness()
validate_witness_freshness()
validate_witness_replay()

validate_commit_authority()
```

These names describe conceptual validator responsibilities and do not assert exact implementation function names unless independently matched to runtime code.

---

# 94. Supplied Enforcement Claim

The supplied artifact states:

```text
authz_invariant_engine.py executes these families
(INV-001..050): 17/17 probes pass.
```

Preserved evidence classification:

```yaml
implementation_claim:
  source_class: SOURCE_CLAIM
  component: authz_invariant_engine.py
  invariant_family: INV-001..050
  reported_probes:
    passed: 17
    total: 17
  independent_runtime_verification: NOT_ESTABLISHED_HERE
```

Therefore:

```text
REPORTED_17_OF_17_PASS
!=
INDEPENDENTLY_VERIFIED_17_OF_17_PASS
```

until the harness and outputs are inspected or executed.

---

# 95. Minimum Validator Tests

## L7-T1 — Capability Without Authority

Input:

```text
principal has write tool
authority grant absent
```

Expected:

```text
COMMIT = DENIED
```

---

## L7-T2 — Authority Without Capability

Input:

```text
authority valid
required tool unavailable
```

Expected:

```text
AUTHORIZED_BUT_NOT_EXECUTABLE
```

not fabricated execution.

---

## L7-T3 — Policy Allow Without Authority

Input:

```text
policy = ALLOW
authority = ABSENT
```

Expected:

```text
COMMIT = DENIED
```

---

## L7-T4 — Authority With Policy Deny

Input:

```text
authority = VALID
policy = DENY
```

Expected:

```text
COMMIT = DENIED
```

---

## L7-T5 — Scope Mismatch

Input:

```text
grant scope = resource A
proposal target = resource B
```

Expected:

```text
AUTHORITY = INVALID_FOR_EFFECT
```

---

## L7-T6 — Self Authorization

Input:

```text
agent issues root grant to itself
```

Expected:

```text
REJECT
```

---

## L7-T7 — Delegation Amplification

Input:

```text
parent amount_limit = 100
child amount_limit = 1000
```

Expected:

```text
INVALID_DELEGATION
```

unless independent authority supplies the expansion.

---

## L7-T8 — Expired Grant

Input:

```text
expires_at < commit_time
```

Expected:

```text
COMMIT = DENIED
```

---

## L7-T9 — Revocation Before Commit

Input:

```text
authorize at E1
revoke at E2
commit at E3
E1 < E2 <= E3
```

Expected:

```text
COMMIT = DENIED
```

---

## L7-T10 — Revocation After Commit

Input:

```text
authorized commit at E1
revocation at E2
E1 < E2
```

Expected:

```text
historical commit authority evaluated at E1
future authority revoked at E2
```

---

## L7-T11 — Witness Action Mismatch

Input:

```text
witness action = READ
commit action = DELETE
```

Expected:

```text
COMMIT = DENIED
```

---

## L7-T12 — Witness Resource Mismatch

Input:

```text
witness resource = R1
commit resource = R2
```

Expected:

```text
COMMIT = DENIED
```

---

## L7-T13 — Stale Epoch

Input:

```text
witness epoch = E1
current authority epoch = E2
```

Expected:

```text
REVALIDATE
```

before consequential commit.

---

## L7-T14 — Broken Delegation Ancestor

Input:

```text
Root → G1 → A → G2 → B
G1 revoked
```

Expected:

```text
G2 invalid
```

unless B has independent authority.

---

## L7-T15 — Independent Authority Path

Input:

```text
G1 path revoked
G2 independent path valid
```

Expected:

```text
evaluate G2 independently
```

not global revocation.

---

## L7-T16 — Partial Atomic Authorization

Input:

```text
transaction = [E1,E2,E3]
authority covers [E1,E2]
```

Expected:

```text
FULL_ATOMIC_COMMIT = DENIED
```

---

## L7-T17 — Memory Grant Stale

Input:

```text
memory says user allowed A previously
current authority validity unknown
```

Expected:

```text
AUTHORITY = UNKNOWN
```

not implicit reuse.

---

# 96. Falsifiers

This specification requires revision if:

1. authoritative authority canon defines materially different grant lifecycle semantics;
2. root authority is canonically defined differently from the supplied human-root rule;
3. delegation is canonically permitted to expand authority under rules not represented here;
4. revocation uses materially different epoch semantics;
5. authoritative canon permits ambient authority;
6. policy decisions canonically function as authority grants;
7. authoritative runtime does not use effect-bound witnesses;
8. `authz_invariant_engine.py` does not exist in the claimed lineage;
9. `INV-001..050` has materially different semantics;
10. the reported `17/17` result cannot be reproduced under the claimed environment;
11. higher-order canon supersedes one or more A-1 through A-4 laws.

---

# 97. Core Invariants

## L7-I1 — Separation

```text
CAPABILITY
!=
AUTHORITY
```

## L7-I2 — Policy Separation

```text
POLICY_ALLOW
!=
AUTHORITY
```

## L7-I3 — Event Separation

```text
EVENT
!=
AUTHORIZATION
```

## L7-I4 — Commitment Separation

```text
PROPOSAL
!=
COMMITMENT
```

## L7-I5 — Scoped Authority

```text
AUTHORITY(S1)
!=
AUTHORITY(S2)
```

unless scope relation explicitly permits it.

## L7-I6 — No Ambient Authority

```text
AUTHORITY
MUST HAVE
AN APPLICABILITY ENVELOPE
```

## L7-I7 — Revocability

```text
REVOKED_AUTHORITY
CANNOT AUTHORIZE
NEW DEPENDENT COMMIT
```

## L7-I8 — No Self Authorization

```text
AGENT
CANNOT CREATE
ITS OWN ROOT AUTHORITY
```

## L7-I9 — Delegation Attenuation

```text
DELEGATED_SCOPE
⊆
DELEGABLE_PARENT_SCOPE
```

## L7-I10 — Root Traceability

```text
DERIVED_AUTHORITY
MUST HAVE
VALID AUTHORITY ANCESTRY
```

## L7-I11 — Effect Binding

```text
AUTHORIZED_EFFECT
=
COMMITTED_EFFECT
```

within allowed equivalence.

## L7-I12 — Freshness

```text
STALE_AUTHORITY
!=
CURRENT_AUTHORITY
```

## L7-I13 — Positive Authority

```text
NOT_DENIED
!=
AUTHORIZED
```

## L7-I14 — Authentication Separation

```text
AUTHENTICATED
!=
AUTHORIZED
```

## L7-I15 — Memory Separation

```text
REMEMBERED_PERMISSION
!=
CURRENT_AUTHORITY
```

## L7-I16 — Selective Revocation

```text
REVOKE(G)
→
INVALIDATE DEPENDENTS(G)
```

not unrelated grants.

## L7-I17 — Atomic Authority

```text
AUTHORITY_FOR_PART
!=
AUTHORITY_FOR_ATOMIC_WHOLE
```

---

# 98. Hard Boundaries

```text
CAPABILITY != AUTHORITY

AUTHENTICATION != AUTHORIZATION

ROLE != AUTHORITY

CREDENTIAL != AUTHORITY

OWNERSHIP != UNBOUNDED_AUTHORITY

CONSENT != AUTHORITY

POLICY_ALLOW != AUTHORITY_GRANT

TOOL_ACCESS != ACTION_AUTHORITY

MEMORY != CURRENT_AUTHORITY

PROPOSAL != COMMIT

EVENT != AUTHORIZED_EVENT

WITNESS != AUTHORITY_SOURCE

OLD_AUTHORITY != CURRENT_AUTHORITY

DELEGATION != AUTHORITY_CREATION

CHILD_AUTHORITY CANNOT EXCEED PARENT AUTHORITY

REVOKED != ACTIVE

EXPIRED != ACTIVE

UNKNOWN_AUTHORITY != ALLOW

CAPABILITY != AUTHORITY

UNKNOWN/GAP != PASS
```

---

# 99. Dependencies

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
```

L7 relies on:

```yaml
dependencies:

  L0_INTEGRITY:
    role: prevents authority fabrication or convenience-based bypass

  L1_EPISTEMIC:
    role: distinguishes verified grants from assumptions and models

  L2_PROVENANCE:
    role: establishes issuer, ancestry, and witness provenance

  L3_DEPENDENCY:
    role: tracks delegation and revocation dependency chains

  L4_CAUSAL:
    role: binds authority changes to effects and causal ordering

  L5_SCOPE_REGIME:
    role: supplies scope, temporal, regime, and freshness boundaries

  L6_UNCERTAINTY:
    role: prevents unknown or conflicting authority from becoming implicit allow
```

---

# 100. Related Authority Infrastructure

L7 conceptually interfaces with:

```text
00_ROOT_AUTHORIZATION
AUTHORIZATION_SPEC
AUTHORITY_RESOLVER
AUTHORITY_WITNESS
DELEGATION
REVOCATION
POLICY_ENGINE
POLICY_REGISTRY
POLICY_DECISION
CAPABILITY_CONTRACT
CAPABILITY_MANIFEST
CONTROL_PLANE_MAP
SYSTEM_MAP
```

These artifacts SHOULD preserve the L7 separation laws.

Their existence or names alone do not prove implementation.

---

# 101. Agent Contract

An L7-conformant agent SHOULD:

1. identify the proposed effect;
2. identify the acting principal;
3. distinguish capability from authority;
4. identify authority requirements;
5. resolve scope;
6. resolve applicable policy;
7. trace delegation;
8. inspect revocation;
9. inspect freshness/epoch;
10. obtain or validate an authority witness;
11. preserve unresolved authority as `UNKNOWN`;
12. request escalation rather than self-authorize;
13. revalidate before consequential commit;
14. log authority provenance where required.

---

# 102. Skill Contract

A Skill capable of consequential effects SHOULD declare:

```yaml
authority_contract:
  capabilities: [...]
  authority_required: true

  effect_classes: [...]

  required_authority:
    principal_types: [...]
    scopes: [...]
    constraints: [...]

  witness_required: true
  commit_revalidation: true

  on_unknown_authority: FAIL_CLOSED
  on_revocation: ABORT
```

A Skill's capability declaration MUST NOT function as an authority grant.

---

# 103. Workflow Contract

Canonical authority workflow:

```text
1. RECEIVE INTENT
2. IDENTIFY PRINCIPAL
3. IDENTIFY PROPOSED EFFECT
4. RESOLVE RESOURCE
5. CHECK CAPABILITY
6. IDENTIFY REQUIRED AUTHORITY
7. RESOLVE ROOT / GRANT
8. TRACE DELEGATION
9. CHECK SCOPE
10. CHECK CONSTRAINTS
11. CHECK EPOCH / FRESHNESS
12. CHECK REVOCATION
13. RESOLVE POLICY
14. CREATE / VALIDATE AUTHORITY WITNESS
15. PREPARE EFFECT
16. REVALIDATE MUTABLE AUTHORITY STATE
17. COMMIT OR DENY
18. RECORD RESULT
19. PROPAGATE REVOCATION / INVALIDATION IF REQUIRED
```

---

# 104. Protocol Contract

Conceptual authority protocol:

```yaml
AUTHORITY_REQUEST:
  principal: ...
  action: ...
  resource: ...
  parameters: ...
  expected_effect: ...

AUTHORITY_CONTEXT:
  epoch: ...
  scope: ...
  policy_context: ...
  grants: [...]
  delegation_chain: [...]
  revocations: [...]

AUTHORITY_RESOLUTION:
  capability: ...
  grant_validity: ...
  scope_validity: ...
  delegation_validity: ...
  revocation_state: ...
  policy_decision: ...
  constraints: [...]

AUTHORITY_DECISION:
  result: AUTHORIZED | DENIED | CONDITIONAL | ESCALATE | UNKNOWN
  witness: ...
  expires_at: ...
  revalidate_at_commit: true

COMMIT_RESULT:
  committed: true | false
  effect: ...
  authority_witness: ...
  commit_epoch: ...
```

---

# 105. RSCF Completion State

```yaml
claim_class: AMOS_MODEL

claim:
  "L7_AUTHORITY separates technical capability from legitimate authority
   and governs typed, scoped, revocable, non-self-issued authority through
   provenance-bound delegation and commit-time validation."

evidence:
  - supplied A-1 Separation law
  - supplied A-2 Typed & Scoped law
  - supplied A-3 Revocable law
  - supplied A-4 Non-Self-Issued law
  - supplied authz_invariant_engine.py enforcement claim
  - supplied 17/17 probe-pass claim

provenance:
  origin_architect: Trang Phan
  artifact_family: AMOS_OS
  layer: 01_CANON/01_CORE_LAWS
  path: 01_CANON/01_CORE_LAWS/L7_AUTHORITY.md
  derivation_status: PROPOSED_STRUCTURAL_COMPLETION
  updated: 2026-08-26

scope:
  system: AMOS
  applies_to:
    - principals
    - agents
    - services
    - tools
    - skills
    - policies
    - grants
    - delegation
    - revocation
    - witnesses
    - transactions
    - commitments

regime:
  - governance
  - authorization
  - orchestration
  - execution
  - persistent_state
  - external_effects

freshness:
  revalidate_on:
    - authority_epoch_change
    - grant_change
    - revocation
    - policy_change
    - scope_change
    - principal_change
    - resource_change
    - effect_change
    - delegation_change
    - commit

dependencies:
  - L0_INTEGRITY
  - L1_EPISTEMIC
  - L2_PROVENANCE
  - L3_DEPENDENCY
  - L4_CAUSAL
  - L5_SCOPE_REGIME
  - L6_UNCERTAINTY

competing:
  - authoritative authority canon may define a different grant lifecycle
  - authoritative canon may define root authority more broadly than human-root authority
  - runtime authority witness structure may differ from this proposed schema
  - runtime revocation semantics may use stronger or different finalization rules

falsifiers:
  - authoritative canon supersedes A-1 through A-4
  - delegation is permitted to expand authority without independent grant
  - agents may canonically self-issue root authority
  - revocation semantics differ materially
  - policy allow canonically equals authority
  - supplied implementation claim cannot be reconciled with runtime
  - reported 17/17 probe result is not reproducible

confidence_ceiling:
  seed_laws: HIGH
  structural_completion: AMOS_MODEL
  exact_canon_equivalence: UNVERIFIED
  implementation_claim: SOURCE_CLAIM
  runtime_verification: NOT_ESTABLISHED_HERE
```

---

# 106. Gap Status

```yaml
gap_status:

  seed_laws:
    A_1_SEPARATION: PROVIDED
    A_2_TYPED_SCOPED: PROVIDED
    A_3_REVOCABLE: PROVIDED
    A_4_NON_SELF_ISSUED: PROVIDED

  structural_completion:
    authority_definition: PROVIDED
    capability_definition: PROVIDED
    typed_inputs_outputs: PROVIDED
    authority_state: PROVIDED
    delegation_model: PROVIDED
    revocation_model: PROVIDED
    witness_model: PROVIDED
    commit_model: PROVIDED
    invariants: PROVIDED
    dependencies: PROVIDED
    hml_applicability: PROVIDED
    control_plane_requirements: PROVIDED
    agent_contract: PROVIDED
    skill_contract: PROVIDED
    workflow: PROVIDED
    protocol: PROVIDED
    failure_modes: PROVIDED
    repair_recovery: PROVIDED
    validators: PROVIDED
    falsifiers: PROVIDED

  unresolved:
    authoritative_authority_canon_reconciliation: REQUIRED
    human_root_rule_final_canon_status: CONDITIONAL
    exact_authority_schema: UNVALIDATED
    exact_witness_schema: UNVALIDATED
    exact_epoch_semantics: UNVALIDATED
    authz_invariant_engine_runtime_verification: REQUIRED
    INV_001_050_mapping: REQUIRED
    reported_17_of_17_probe_evidence: SOURCE_CLAIM_ONLY
    full_runtime_implementation: NOT_ESTABLISHED
    final_canon_approval: REQUIRED
```

---

# 107. Canon Promotion Gate

Before final canon promotion:

```text
[ ] Trang Phan / steward approval
[ ] authoritative authority canon reconciled
[ ] A-1 confirmed
[ ] A-2 confirmed
[ ] A-3 confirmed
[ ] A-4 confirmed
[ ] human-root semantics confirmed
[ ] authority types defined
[ ] scope model confirmed
[ ] delegation attenuation confirmed
[ ] delegation depth semantics confirmed
[ ] revocation semantics confirmed
[ ] authority epoch semantics confirmed
[ ] witness lifecycle confirmed
[ ] effect-binding semantics confirmed
[ ] commit-time revalidation confirmed
[ ] policy/authority separation confirmed
[ ] capability/authority separation confirmed
[ ] root authorization aligned
[ ] AUTHORIZATION_SPEC aligned
[ ] AUTHORITY_RESOLVER aligned
[ ] AUTHORITY_WITNESS aligned
[ ] DELEGATION aligned
[ ] REVOCATION aligned
[ ] POLICY_ENGINE aligned
[ ] CAPABILITY_CONTRACT aligned
[ ] authz_invariant_engine.py inspected
[ ] INV-001..050 mapped
[ ] 17/17 probes independently reproduced
[ ] failure tests executed
[ ] revocation tests executed
[ ] stale-authority tests executed
[ ] delegation tests executed
[ ] transaction authority tests executed
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

# 108. Final L7 Law Summary

The L7 authority boundary reduces to four source-supplied governing laws:

```text
A-1
CAPABILITY
!=
AUTHORITY
!=
POLICY_ALLOW
!=
EVENT
!=
COMMITMENT
```

```text
A-2
AUTHORITY IS
TYPED
+
SCOPED
+
PRINCIPAL-BOUND
+
EPOCH-BOUND
```

```text
A-3
AUTHORITY IS REVOCABLE
AND REVOCATION MUST NOT DRIFT
PAST ITS EFFECTIVE EPOCH
```

```text
A-4
AUTHORITY CANNOT BE SELF-ISSUED;
DELEGATED AUTHORITY MUST TRACE
TO A VALID ROOT
```

The resulting commitment rule is conceptually:

```text
COMMIT_ALLOWED
IFF

CAPABILITY_SUFFICIENT
AND
AUTHORITY_VALID
AND
AUTHORITY_CURRENT
AND
SCOPE_MATCHES
AND
DELEGATION_VALID
AND
REVOCATION_CLEAR
AND
POLICY_ALLOWS
AND
CONSTRAINTS_SATISFIED
AND
WITNESS_MATCHES_EFFECT
```

with:

```text
UNKNOWN REQUIRED AUTHORITY
→
NO COMMIT
```

and:

```text
REVOCATION
→
SELECTIVE INVALIDATION
→
COMMIT-TIME REVALIDATION
```

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---

**Related:** [[00_ROOT/00-Home]] · AMOS_RSCF_NODES · LAW_HIERARCHY · L0_INTEGRITY · L1_EPISTEMIC · L2_PROVENANCE · L3_DEPENDENCY · L4_CAUSAL · L5_SCOPE_REGIME · L6_UNCERTAINTY · [[00_ROOT_AUTHORIZATION]] · AUTHORIZATION_SPEC · AUTHORITY_RESOLVER · AUTHORITY_WITNESS · DELEGATION · REVOCATION · POLICY_ENGINE · POLICY_REGISTRY · POLICY_DECISION · CAPABILITY_CONTRACT · CAPABILITY_MANIFEST · CONTROL_PLANE_MAP

---

RSCF-NODE

node_id: l7_authority

node_type: core_law

path: 01_CANON/01_CORE_LAWS/L7_AUTHORITY.md

RSCF-RELATIONS:

* CHILD_OF: LAW_HIERARCHY
* DEPENDS_ON: L0_INTEGRITY
* DEPENDS_ON: L1_EPISTEMIC
* DEPENDS_ON: L2_PROVENANCE
* DEPENDS_ON: L3_DEPENDENCY
* DEPENDS_ON: L4_CAUSAL
* DEPENDS_ON: L5_SCOPE_REGIME
* DEPENDS_ON: L6_UNCERTAINTY
* GOVERNS: [[00_ROOT_AUTHORIZATION]]
* GOVERNS: AUTHORIZATION_SPEC
* GOVERNS: AUTHORITY_RESOLVER
* GOVERNS: AUTHORITY_WITNESS
* GOVERNS: DELEGATION
* GOVERNS: REVOCATION
* CONSTRAINS: POLICY_ENGINE
* CONSTRAINS: CAPABILITY_CONTRACT
* CONSTRAINS: CAPABILITY_MANIFEST
* INDEXED_BY: [[00_ROOT/00-Home]]
* INDEXED_BY: AMOS_RSCF_NODES

claim_class: AMOS_MODEL

```
```

---
**MOC:** [[01_CORE_LAWS_MOC]]
