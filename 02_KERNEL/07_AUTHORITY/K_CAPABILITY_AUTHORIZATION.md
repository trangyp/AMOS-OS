---
title: K CAPABILITY AUTHORIZATION
type: note
source: 02_KERNEL/07_AUTHORITY
artifact_id: AMOS-OS-K-CAPABILITY-AUTHORIZATION
canonical_name: K_CAPABILITY_AUTHORIZATION
artifact_type: kernel_capability_authorization_contract
status: AMOS_MODEL
conclusion_class: AMOS_MODEL
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
plane: KERNEL
scope: AMOS_OS
updated: 2026-08-26
tags:
- kernel
- authority
- note
- canon/kernel
- readme
- dependency-map
- amos-core-laws
- invariant-registry
- law-hierarchy
- authority-canon
- canon-provenance
- kernel-map
- k-core19-logic
- k-meta-logic
- k-identity
- k-context-state
- k-system-state
- k-risk-constraint
- k-event-bus
rscf:
  state: DERIVED
  claim_class: CONDITIONAL
  provenance: AMOS_corpus
  scope: AMOS_general
---

# K CAPABILITY AUTHORIZATION

> **AMOS Core target:** `v4.4`
> **Origin architect / steward:** Trang Phan
> **Canonical location:** `02_KERNEL/K_CAPABILITY_AUTHORIZATION.md`
> **Status:** `AMOS_MODEL`
> **Conclusion class:** `AMOS_MODEL`

## Purpose

`K_CAPABILITY_AUTHORIZATION` defines the deterministic kernel contract separating:

```text
CAPABILITY
```

from:

```text
AUTHORITY
```

and determining whether a proposed use of a capability is eligible to proceed to governed authorization and execution.

Its central law is:

```text
CAPABILITY != AUTHORITY
```

A system may possess the technical ability to perform an operation without possessing permission to perform it.

Likewise:

```text
TOOL != PERMISSION
ACCESS != AUTHORIZATION
ROLE != UNLIMITED AUTHORITY
PROPOSAL != COMMIT
AUTHORIZATION != EXECUTION
```

---

# 1. Architectural Boundary

AMOS separates:

```text
KERNEL
→ deterministic authorization invariants

CONTROL_PLANE
→ policy, authority, delegation, approval, commit governance

RUNTIME
→ scheduling and execution

TOOLS
→ available effectors

INTERFACES
→ access surfaces
```

Therefore:

```text
K_CAPABILITY_AUTHORIZATION
DOES NOT
GRANT AUTHORITY
```

It determines whether an authorization claim satisfies the kernel-level structural requirements necessary for governed use.

Canonical flow:

```text
REQUEST
↓
IDENTIFY ACTOR
↓
IDENTIFY CAPABILITY
↓
IDENTIFY TARGET
↓
IDENTIFY REQUESTED EFFECT
↓
RESOLVE AUTHORITY CLAIM
↓
VALIDATE SCOPE
↓
VALIDATE DELEGATION
↓
VALIDATE POLICY / EPOCH / FRESHNESS
↓
CHECK CONSTRAINTS
↓
CHECK RISK CLASS
↓
RETURN AUTHORIZATION RESULT
↓
CONTROL PLANE / RUNTIME
```

---

# 2. Fundamental Distinctions

```text
CAPABILITY != AUTHORITY
CAPABILITY != PERMISSION
CAPABILITY != ENTITLEMENT
CAPABILITY != POLICY

AUTHORITY != CAPABILITY
AUTHORITY != EXECUTION
AUTHORITY != SUCCESS

IDENTITY != AUTHORITY
ROLE != AUTHORITY
OWNERSHIP != UNIVERSAL AUTHORITY

ACCESS != PERMISSION
VISIBILITY != MUTABILITY
READ != WRITE
WRITE != COMMIT
COMMIT != PUBLISH
PUBLISH != EXTERNAL EFFECT

TOOL != AUTHORITY
MODEL != AUTHORITY
AGENT != AUTHORITY
SKILL != AUTHORITY
WORKFLOW != AUTHORITY

AUTHENTICATION != AUTHORIZATION
AUTHORIZATION != VALIDATION
VALIDATION != COMMIT
COMMIT != EXECUTION

DELEGATION != TRANSFER OF UNBOUNDED AUTHORITY
POSSESSION OF CREDENTIAL != LEGITIMATE AUTHORITY
```

---

# 3. Capability

A capability represents what an actor or subsystem can technically attempt.

Conceptually:

```yaml
capability:
  capability_id:
  capability_type:
  provider:
  operations: []
  target_types: []
  effect_types: []
  technical_constraints: []
  availability:
  provenance:
```

Examples:

```text
READ_FILE
WRITE_FILE
DELETE_FILE
EXECUTE_TOOL
CALL_MODEL
WRITE_MEMORY
PROPOSE_STATE_CHANGE
COMMIT_STATE_CHANGE
PUBLISH_EXTERNAL_EFFECT
MODIFY_POLICY
PROMOTE_CANON
```

Capability existence establishes only:

```text
TECHNICALLY_AVAILABLE
```

not:

```text
AUTHORIZED
```

---

# 4. Authority

Authority represents a governed right to approve or perform a defined action within a defined envelope.

Conceptually:

```yaml
authority:
  authority_id:
  principal:
  authority_type:
  source:
  granted_operations: []
  target_scope:
  environment_scope:
  regime_scope:
  temporal_scope:
  delegation_scope:
  risk_scope:
  policy_epoch:
  provenance:
  constraints: []
  expiry:
  revocation_state:
```

Authority is:

```text
TYPED
SCOPED
PROVENANCE-AWARE
REGIME-AWARE
FRESHNESS-BOUNDED
REVOCABLE
```

unless canon explicitly specifies otherwise.

---

# 5. Authorization

Authorization is the determination that a particular actor may use a particular capability for a particular action under current governed conditions.

Conceptually:

```text
AUTHORIZATION
=
VALID(
  ACTOR,
  CAPABILITY,
  OPERATION,
  TARGET,
  SCOPE,
  AUTHORITY,
  POLICY,
  REGIME,
  TIME,
  RISK,
  CONSTRAINTS
)
```

Authorization is contextual.

Therefore:

```text
AUTHORIZED(A, X, T0, S1)
```

does not imply:

```text
AUTHORIZED(A, X, T1, S2)
```

---

# 6. Authorization Request Object

```yaml
authorization_request:
  request_id:

  actor:
    identity:
    role:
    agent_id:
    session:
    provenance:

  capability:
    capability_id:
    operation:

  target:
    target_id:
    target_type:
    state_class:

  requested_effect:
    effect_type:
    persistence:
    externality:
    reversibility:

  scope:
    system:
    domain:
    environment:
    regime:
    population:
    time:

  authority_claim:
    authority_id:
    source:
    delegation_chain: []

  policy_context:
    policy_epoch:
    applicable_rules: []

  risk_context:
    risk_class:
    blast_radius:
    irreversibility:

  evidence: []
  dependencies: []
```

Missing load-bearing values remain:

```text
UNKNOWN/GAP
```

---

# 7. Core Authorization Law

For actor `A`, capability `C`, operation `O`, target `T`:

```text
AUTHORIZED(A,C,O,T)
IFF

IDENTITY_VALID(A)

AND
CAPABILITY_SUPPORTS(C,O,T)

AND
AUTHORITY_VALID(A,O,T)

AND
SCOPE_VALID(A,O,T)

AND
DELEGATION_VALID(A,O,T)

AND
POLICY_VALID(A,O,T)

AND
TEMPORAL_VALIDITY = TRUE

AND
REGIME_VALIDITY = TRUE

AND
HARD_CONSTRAINTS = SATISFIED

AND
RISK_REQUIREMENTS = SATISFIED
```

This is a conceptual AMOS contract, not a claim of formal implementation.

---

# 8. Identity Requirement

Authorization requires a valid actor identity when identity is load-bearing.

```text
UNKNOWN ACTOR
```

must not silently inherit:

```text
DEFAULT AUTHORITY
```

Law:

```text
UNKNOWN IDENTITY
!=
AUTHORIZED IDENTITY
```

Identity may include:

```text
HUMAN
AGENT
SERVICE
SUBSYSTEM
WORKFLOW
CONTROL-PLANE PRINCIPAL
```

The identity mechanism belongs to the appropriate security/control-plane implementation.

---

# 9. Authentication Boundary

Authentication answers:

```text
WHO / WHAT IS THIS?
```

Authorization answers:

```text
WHAT MAY IT DO?
```

Therefore:

```text
AUTHENTICATED
!=
AUTHORIZED
```

A valid identity may still lack authority for the requested operation.

---

# 10. Scope Law

Authority applies only inside its authorized envelope.

Example:

```text
AUTHORITY:
  operation = READ
  domain = KNOWLEDGE
```

does not imply:

```text
WRITE KNOWLEDGE
DELETE KNOWLEDGE
WRITE STATE
MODIFY CANON
```

Canonical law:

```text
AUTHORITY(SCOPE X)
!=
AUTHORITY(SCOPE *)
```

---

# 11. Least Authority

Default principle:

```text
GRANT / USE
THE MINIMUM AUTHORITY
SUFFICIENT FOR
THE VALID OBJECTIVE
```

If an operation requires:

```text
READ(A)
```

do not require or assume:

```text
WRITE(A)
DELETE(A)
ADMIN(A)
```

Least authority reduces accidental and adversarial blast radius.

---

# 12. Authority Non-Amplification

A delegated actor cannot create greater authority from lesser authority.

If:

```text
AUTHORITY(A) = {READ}
```

then:

```text
A → DELEGATE {WRITE}
```

must fail unless another independently valid authority source licenses the write authority.

Formally:

```text
DELEGATED_AUTHORITY
⊆
DELEGATOR_AUTHORITY
```

within the relevant scope.

---

# 13. Delegation

Delegation must preserve:

```text
SOURCE
SCOPE
OPERATION
TARGET
TIME
REGIME
CONSTRAINTS
PROVENANCE
REVOCATION
```

Conceptually:

```yaml
delegation:
  delegator:
  delegate:
  authority_source:
  granted_scope:
  excluded_scope:
  issued_at:
  expires_at:
  policy_epoch:
  constraints: []
  provenance:
```

---

# 14. Delegation Chain

For:

```text
P0
→ P1
→ P2
→ P3
```

authority at `P3` cannot exceed the valid intersection of the chain.

Conceptually:

```text
AUTH(P3)
≤
AUTH(P0)
∩ AUTH(P1)
∩ AUTH(P2)
∩ DELEGATION_CONSTRAINTS
```

Any invalid load-bearing delegation edge invalidates dependent authorization.

---

# 15. Broken Delegation

If:

```text
P0 → P1 = VALID
P1 → P2 = INVALID
P2 → P3 = CLAIMED
```

then downstream authority derived through the invalid edge is invalid.

Do not invalidate unrelated authority chains.

```text
INVALID(edge)
→ INVALIDATE(dependent descendants)
```

---

# 16. Authority Provenance

Every consequential authority claim should identify where the authority originated.

Examples:

```text
CANON
POLICY
ROLE ASSIGNMENT
EXPLICIT USER AUTHORIZATION
DELEGATION
SYSTEM GOVERNANCE
```

Untraceable authority is not equivalent to valid authority.

```text
AUTHORITY WITHOUT PROVENANCE
→ UNKNOWN/GAP
```

when provenance is required.

---

# 17. Authority Freshness

Authorization must respect expiry and revocation.

```text
VALID @ T0
```

does not imply:

```text
VALID @ T1
```

Authority may become invalid through:

```text
EXPIRY
REVOCATION
ROLE CHANGE
POLICY CHANGE
STATE CHANGE
SECURITY EVENT
REGIME CHANGE
```

---

# 18. Authority Epoch

Governed authority may be associated with an authority or policy epoch.

Example:

```text
AUTHORIZATION DERIVED UNDER AE17
```

If:

```text
AE17 → AE18
```

before commit, revalidation is required where the epoch transition can affect authorization.

```text
STALE AUTHORIZATION
!=
CURRENT AUTHORIZATION
```

---

# 19. Policy Epoch

Likewise:

```text
POLICY(P17)
```

cannot automatically authorize an action after:

```text
P17 → P18
```

if the applicable policy changed.

Commit should use current policy or a specifically valid pinned-policy contract.

---

# 20. State-Relative Authorization

Authorization may depend on system state.

```text
AUTHORIZED(A | S17)
```

does not imply:

```text
AUTHORIZED(A | S18)
```

Example:

```text
WRITE ALLOWED
WHILE SYSTEM = NORMAL
```

may become:

```text
WRITE BLOCKED
WHILE SYSTEM = RECOVERY
```

---

# 21. Regime-Relative Authorization

Authority may differ across regimes.

Examples:

```text
DEVELOPMENT
TEST
SHADOW
CANARY
PRODUCTION
RECOVERY
EMERGENCY
```

Therefore:

```text
AUTHORIZED_IN_TEST
!=
AUTHORIZED_IN_PRODUCTION
```

---

# 22. Read / Write / Commit Separation

AMOS should preserve:

```text
READ
↓
PROPOSE
↓
WRITE_WORKING_STATE
↓
COMMIT_AUTHORITATIVE_STATE
↓
PUBLISH
↓
EXTERNAL_EFFECT
```

as distinguishable authorization boundaries where material.

Permission at one level does not automatically imply permission at the next.

---

# 23. Proposal Boundary

An actor may be authorized to generate:

```text
PROPOSAL
```

without being authorized to:

```text
COMMIT
```

This is fundamental for agent governance.

```text
PROPOSAL AUTHORITY
!=
COMMIT AUTHORITY
```

---

# 24. Agent Boundary

An agent's reasoning capability does not grant institutional authority.

```text
AGENT CAN RECOMMEND
```

does not imply:

```text
AGENT CAN COMMIT
```

unless a valid authority contract explicitly grants that operation.

---

# 25. Skill Boundary

A skill describes reusable procedure.

```text
SKILL CAN PERFORM X
```

means:

```text
X IS WITHIN PROCEDURAL CAPABILITY
```

not:

```text
X IS AUTHORIZED NOW
```

Thus:

```text
SKILL != AUTHORITY
```

---

# 26. Workflow Boundary

A workflow may orchestrate authorized components but does not create authority through composition.

```text
WF:
  STEP1
  STEP2
  STEP3
```

Each authority-sensitive step must remain authorized.

```text
AUTHORIZED(STEP1)
```

does not imply:

```text
AUTHORIZED(STEP2)
```

---

# 27. Tool Boundary

Tools are effectors.

```text
TOOL AVAILABLE
```

does not imply:

```text
TOOL USE AUTHORIZED
```

and:

```text
TOOL ACCEPTS REQUEST
```

does not prove:

```text
REQUEST WAS GOVERNED CORRECTLY
```

---

# 28. Model Boundary

Models can:

```text
INFER
CLASSIFY
GENERATE
RECOMMEND
```

but:

```text
MODEL OUTPUT
!=
AUTHORITY
```

A model cannot bootstrap commit authority merely by predicting that an action should occur.

---

# 29. Memory Boundary

Memory can contain an authority-related statement such as:

```text
USER ALLOWED X
```

but stored memory alone does not necessarily establish current authority.

Authorization must consider:

```text
SOURCE
SCOPE
FRESHNESS
REVOCATION
POLICY
REGIME
```

Therefore:

```text
MEMORY != AUTHORITY
```

---

# 30. Knowledge Boundary

Knowledge may describe policies or roles.

Description is not execution authority.

```text
KNOWLEDGE OF PERMISSION
!=
PERMISSION
```

Authoritative policy sources must remain distinguishable from summaries and derived knowledge.

---

# 31. Canon Boundary

Canon may define authority law.

But:

```text
CANON
```

does not execute actions.

Likewise:

```text
KERNEL
```

does not become control-plane policy merely by encoding invariants.

```text
CANON != KERNEL
KERNEL != CONTROL_PLANE
CONTROL_PLANE != RUNTIME
```

---

# 32. Risk Coupling

Authorization must interact with:

```text
K_RISK_CONSTRAINT
```

An actor may possess general authority while the requested action still exceeds the authorized risk envelope.

Example:

```text
WRITE AUTHORITY = VALID
```

but:

```text
ACTION BLAST RADIUS = CRITICAL
```

may require:

```text
ADDITIONAL APPROVAL
STAGING
ESCALATION
```

---

# 33. Risk Does Not Create Authority

Conversely:

```text
LOW RISK
```

does not create permission.

```text
SAFE
!=
AUTHORIZED
```

Even harmless operations may remain prohibited by policy or scope.

---

# 34. Emergency Authority

Emergency operation must not silently mean:

```text
ALL CONSTRAINTS DISABLED
```

Emergency authority should be explicitly typed and scoped.

Conceptually:

```yaml
emergency_authority:
  trigger:
  principal:
  allowed_operations: []
  prohibited_operations: []
  scope:
  maximum_duration:
  audit_required:
  recovery_requirements:
  termination_condition:
```

---

# 35. Break-Glass Semantics

If AMOS supports break-glass authority, it should require explicit governance.

```text
NORMAL AUTHORITY FAILS
↓
BREAK-GLASS CONDITION VERIFIED
↓
SPECIAL AUTHORITY SOURCE VERIFIED
↓
LIMITED EMERGENCY SCOPE
↓
ACTION
↓
AUDIT
↓
EXPIRY
↓
REVIEW
```

Break-glass is not equivalent to bypass.

---

# 36. Separation of Duties

Certain operations may require multiple distinct authorities.

Example:

```text
PROPOSER
!=
APPROVER
```

or:

```text
POLICY AUTHOR
!=
POLICY ACTIVATOR
```

when governance requires independence.

The kernel must not assume independence merely from different labels.

---

# 37. Provenance Independence

If:

```text
APPROVER A
APPROVER B
```

are both derived from the same compromised authority source, apparent multiplicity may not constitute independent approval.

Independence must be demonstrated when load-bearing.

---

# 38. Self-Authorization Firewall

Default law:

```text
ACTOR
MUST NOT
CREATE THE AUTHORITY
REQUIRED TO AUTHORIZE
ITS OWN OTHERWISE UNAUTHORIZED ACTION
```

unless canon explicitly defines a bounded self-governance mechanism.

Examples that must not bootstrap authority:

```text
AGENT WRITES POLICY
→ AGENT NOW AUTHORIZED

MODEL GENERATES APPROVAL
→ APPROVAL VALID

WORKFLOW CREATES ROLE
→ WORKFLOW GAINS ROLE
```

---

# 39. Circular Authority

Authority graphs must detect circular justification.

Invalid pattern:

```text
A AUTHORIZED BY B
B AUTHORIZED BY C
C AUTHORIZED BY A
```

with no valid external authority root.

A cycle is not an authority source.

```text
CIRCULAR JUSTIFICATION
!=
PROVENANCE ROOT
```

---

# 40. Authority Root

A valid authorization chain ultimately requires an accepted authority root appropriate to its scope.

Potential roots may include:

```text
CANONICALLY DEFINED AUTHORITY
VALID GOVERNANCE POLICY
EXPLICIT HUMAN AUTHORIZATION
EXTERNAL INSTITUTIONAL AUTHORITY
```

depending on the system and action.

The existence and hierarchy of actual roots belong to `AUTHORITY_CANON` and the control plane.

---

# 41. Deny by Absence

For authority-sensitive actions:

```text
NO VALID AUTHORITY
```

must not become:

```text
ALLOW
```

merely because no explicit prohibition was found.

Default conceptual rule:

```text
REQUIRES_AUTHORITY
AND
AUTHORITY = UNKNOWN
→
DO NOT AUTHORIZE
```

---

# 42. Explicit Denial

Explicit valid denial dominates lower-priority permission where the law hierarchy says it does.

Conceptually:

```text
ALLOW
+
HIGHER-PRECEDENCE DENY
→
DENY
```

Actual precedence comes from:

```text
LAW_HIERARCHY
AUTHORITY_CANON
CONTROL_PLANE POLICY
```

---

# 43. Conflicting Authority

Suppose:

```text
SOURCE A → ALLOW
SOURCE B → DENY
```

If precedence cannot resolve the conflict:

```text
COMPETING
```

or:

```text
UNKNOWN/GAP
```

must be preserved.

Do not select whichever source is more convenient.

---

# 44. Constraint Intersection

When multiple valid authority constraints apply:

```text
EFFECTIVE_AUTHORITY
=
INTERSECTION(
  SOURCE_AUTHORITY,
  ROLE_CONSTRAINT,
  DELEGATION_CONSTRAINT,
  POLICY_CONSTRAINT,
  SCOPE_CONSTRAINT,
  REGIME_CONSTRAINT,
  TEMPORAL_CONSTRAINT,
  RISK_CONSTRAINT
)
```

Conceptually, effective authority cannot exceed the narrowest load-bearing constraint.

---

# 45. Authorization Confidence Ceiling

For derived authorization conclusion `C`:

```text
CONFIDENCE(C)
≤
MIN(
  IDENTITY_VALIDITY,
  AUTHORITY_PROVENANCE,
  DELEGATION_VALIDITY,
  POLICY_VALIDITY,
  SCOPE_VALIDITY,
  REGIME_VALIDITY,
  TEMPORAL_VALIDITY,
  RISK_VALIDITY
)
```

A weak load-bearing premise caps the authorization conclusion.

---

# 46. Authorization Classes

Proposed kernel result classes:

```text
CA0 — DENIED
CA1 — ESCALATION REQUIRED
CA2 — AUTHORIZED FOR PROPOSAL ONLY
CA3 — AUTHORIZED CONDITIONALLY
CA4 — AUTHORIZED WITHIN SCOPE
CAX — UNKNOWN/GAP
CAC — COMPETING
```

These remain `AMOS_MODEL` until formally adopted.

---

# 47. CA0 — Denied

Use when:

```text
HARD PROHIBITION
INVALID AUTHORITY
REVOKED AUTHORITY
OUT-OF-SCOPE OPERATION
INVALID DELEGATION
```

decisively blocks the request.

---

# 48. CA1 — Escalation Required

Use when:

```text
LOCAL AUTHORITY INSUFFICIENT
HIGHER APPROVAL REQUIRED
RISK ENVELOPE EXCEEDED
SEPARATION OF DUTIES REQUIRED
AUTHORITY CONFLICT REQUIRES GOVERNANCE
```

---

# 49. CA2 — Proposal Only

Use when an actor may:

```text
ANALYZE
DRAFT
RECOMMEND
PROPOSE
```

but lacks commit authority.

This class is important for cognitive agents.

---

# 50. CA3 — Conditional Authorization

Example:

```text
AUTHORIZED
IF:
  POLICY_EPOCH = P17
  TARGET ∈ DOMAIN-X
  OPERATION = WRITE
  RISK <= R2
  HUMAN_APPROVAL = VALID
```

Failure of a load-bearing condition invalidates authorization.

---

# 51. CA4 — Authorized Within Scope

Use when all applicable constraints are valid.

It means:

```text
AUTHORIZED
ONLY WITHIN
THE RECORDED ENVELOPE
```

not universal permission.

---

# 52. CAX — Unknown/Gap

Use when a load-bearing authorization fact cannot be established.

Examples:

```text
UNKNOWN PRINCIPAL
UNKNOWN AUTHORITY SOURCE
UNKNOWN POLICY EPOCH
UNKNOWN DELEGATION
UNKNOWN TARGET CLASS
```

---

# 53. CAC — Competing

Use when incompatible authority claims remain genuinely unresolved.

```text
ALLOW
vs
DENY
```

must remain visible until precedence or additional evidence resolves the conflict.

---

# 54. Authorization Decision Gate

```text
REQUEST
↓
IS OPERATION AUTHORITY-SENSITIVE?
├── NO
│   → CONTINUE UNDER APPLICABLE CONTRACT
└── YES
    ↓
ACTOR IDENTITY VALID?
├── NO
│   → CAX / CA0
└── YES
    ↓
CAPABILITY EXISTS?
├── NO
│   → NOT EXECUTABLE
└── YES
    ↓
VALID AUTHORITY SOURCE?
├── NO
│   → CAX / CA0
└── YES
    ↓
DELEGATION VALID?
├── NO
│   → CA0
└── YES
    ↓
REQUEST WITHIN SCOPE?
├── NO
│   → CA0
└── YES
    ↓
AUTHORITY CURRENT?
├── NO
│   → CA0 / REVALIDATE
└── YES
    ↓
POLICY / REGIME VALID?
├── NO
│   → CA0 / CAX
└── YES
    ↓
AUTHORITY CONFLICT?
├── YES
│   → CAC / CA1
└── NO
    ↓
RISK REQUIRES HIGHER AUTHORITY?
├── YES
│   → CA1
└── NO
    ↓
COMMIT AUTHORITY PRESENT?
├── NO
│   → CA2
└── YES
    ↓
CONDITIONS REMAIN?
├── YES
│   → CA3
└── NO
    ↓
CA4
```

---

# 55. TOCTOU Authorization

Authorization may change between:

```text
CHECK
```

and:

```text
USE
```

Therefore:

```text
AUTHORIZED @ CHECK
```

does not always imply:

```text
AUTHORIZED @ COMMIT
```

For consequential operations, authorization should be revalidated at the commit boundary where material.

---

# 56. MVCC / CAS Interaction

Suppose authorization was derived against:

```text
STATE V17
POLICY P8
AUTHORITY A4
```

and before commit:

```text
STATE V18
POLICY P9
```

becomes authoritative.

If the changed state can affect permission:

```text
COMMIT
→ REVALIDATE
```

A stale authorization proof must not silently survive a material epoch change.

---

# 57. Atomic Multi-Resource Authorization

If one operation atomically affects:

```text
RESOURCE A
RESOURCE B
RESOURCE C
```

authorization must cover the complete required effect set.

Invalid pattern:

```text
AUTHORIZED(A)
AUTHORIZED(B)
UNKNOWN(C)

→ COMMIT ALL
```

Required result:

```text
NO AUTHORITATIVE ATOMIC COMMIT
```

unless the operation contract permits safe partial execution.

---

# 58. Partial Authorization

If a request contains separable effects:

```text
E1
E2
E3
```

with:

```text
E1 = AUTHORIZED
E2 = DENIED
E3 = AUTHORIZED
```

the system may execute only `E1` and `E3` **if**:

```text
THE REQUEST IS SEMANTICALLY DECOMPOSABLE
AND
PARTIAL EXECUTION IS SAFE
AND
ATOMICITY IS NOT REQUIRED
```

Otherwise reject or escalate the whole operation.

---

# 59. Capability Escalation

A capability escalation occurs when an actor obtains or attempts an effect beyond its authorized capability envelope.

Examples:

```text
READ → WRITE
WRITE → DELETE
LOCAL → GLOBAL
WORKING STATE → AUTHORITATIVE STATE
INTERNAL → EXTERNAL
PROPOSE → COMMIT
USER SCOPE → SYSTEM SCOPE
```

Such transitions require explicit authorization.

---

# 60. Confused-Deputy Constraint

An authorized component must not become an unintended authority proxy for an unauthorized requester.

Pattern:

```text
UNAUTHORIZED A
→ REQUESTS B
→ B HAS AUTHORITY
→ B EXECUTES FOR A
```

B must evaluate:

```text
REQUESTER
INTENT
DELEGATION
TARGET
SCOPE
```

rather than relying solely on B's own capability.

---

# 61. Credential Possession

Possessing a credential may be evidence of access but is not automatically sufficient evidence of legitimate authority.

```text
HAS TOKEN
!=
AUTHORIZED PURPOSE
```

especially where:

```text
TOKEN STOLEN
TOKEN STALE
TOKEN OVER-SCOPED
TOKEN USED OUTSIDE INTENDED CONTEXT
```

are plausible.

---

# 62. Revocation

Revocation should invalidate dependent authorization without corrupting unrelated authority.

```text
REVOKE(AUTH-X)
↓
INVALIDATE(
  AUTHORIZATIONS DEPENDENT ON AUTH-X
)
```

Do not globally revoke unrelated authority unless the dependency graph requires it.

---

# 63. Supersession

New authority or policy does not erase lineage.

Maintain:

```text
PREVIOUS AUTHORITY
SUPERSEDING AUTHORITY
REASON
EFFECTIVE TIME
PROVENANCE
DEPENDENT INVALIDATION
```

This supports audit and recovery.

---

# 64. Authorization Proof Capsule

Consequential authorization should conceptually carry:

```yaml
authorization_proof:
  claim:
  conclusion_class:
  result_class:

  actor:
  capability:
  operation:
  target:

  authority_source:
  authority_provenance:
  delegation_chain: []

  scope:
  regime:
  temporal_validity:
  policy_epoch:
  authority_epoch:

  load_bearing_premises: []
  constraints: []
  risk_requirements: []

  competing_authority_claims: []
  dependencies: []
  falsifiers: []
  invalidation_conditions: []

  confidence_ceiling:
```

---

# 65. Invalidation Conditions

Authorization should be invalidated when a load-bearing condition changes.

Examples:

```text
IDENTITY INVALIDATED
AUTHORITY REVOKED
DELEGATION REVOKED
SCOPE CHANGED
TARGET CHANGED
OPERATION CHANGED
POLICY EPOCH CHANGED
AUTHORITY EPOCH CHANGED
REGIME CHANGED
RISK CLASS CHANGED
SECURITY STATE CHANGED
TIME WINDOW EXPIRED
```

---

# 66. Authorization Cache

Cached authorization is valid only while its dependency closure remains valid.

```yaml
authorization_cache:
  authorization_id:
  decision:
  dependencies: []
  policy_epoch:
  authority_epoch:
  state_epoch:
  scope:
  expires_at:
```

If any load-bearing dependency changes:

```text
INVALIDATE CACHE
```

---

# 67. Authorization Is Non-Transitive by Default

From:

```text
A AUTHORIZED TO CALL B
B AUTHORIZED TO CALL C
```

do not infer:

```text
A AUTHORIZED TO DIRECTLY CALL C
```

unless an explicit delegation or composition rule permits it.

---

# 68. Authorization Is Non-Inheritable by Default

From:

```text
PARENT AUTHORIZED
```

do not infer:

```text
ALL CHILDREN AUTHORIZED
```

Likewise:

```text
WORKFLOW AUTHORIZED
```

does not automatically authorize every dynamically introduced step.

---

# 69. Authority and Ownership

Ownership may be an authority source in some domains, but:

```text
OWNERSHIP
!=
UNLIMITED AUTHORITY
```

External constraints may still apply:

```text
SECURITY
LAW
POLICY
SHARED OWNERSHIP
INSTITUTIONAL GOVERNANCE
```

---

# 70. Human Authorization

Human instruction can be a material authority source where the human has appropriate authority.

But:

```text
HUMAN SAID X
```

must still be interpreted for:

```text
IDENTITY
SCOPE
INTENT
TARGET
TEMPORAL VALIDITY
APPLICABLE HIGHER-ORDER CONSTRAINTS
```

Human instruction cannot silently override higher-order non-waivable constraints.

---

# 71. Ambiguous Authorization

Ambiguity affecting a consequential permission should not be resolved by maximizing capability.

Prefer:

```text
NARROW INTERPRETATION
CLARIFICATION
ESCALATION
REVERSIBLE ACTION
```

depending on stakes.

---

# 72. Authorization and Intent

Permission to achieve objective `G` does not necessarily imply permission for every means capable of achieving `G`.

```text
AUTHORIZED(GOAL)
!=
AUTHORIZED(ALL METHODS)
```

The method itself may require separate authority.

---

# 73. Purpose Limitation

Authority may be purpose-bound.

```text
READ DATA
FOR INCIDENT RESPONSE
```

does not automatically authorize:

```text
READ DATA
FOR UNRELATED ANALYTICS
```

when purpose is load-bearing.

---

# 74. Data-Class Constraint

Authority may depend on target classification.

Examples:

```text
PUBLIC
INTERNAL
CONFIDENTIAL
SECRET
AUTHORITATIVE_STATE
CANON
```

Permission for one class does not imply permission for another.

---

# 75. External Effect Constraint

External actions deserve explicit authorization boundaries.

Examples:

```text
SEND
PUBLISH
PURCHASE
DELETE
DEPLOY
TRANSFER
NOTIFY
MODIFY THIRD-PARTY SYSTEM
```

The fact that a runtime connector can perform the operation is not authorization.

---

# 76. Canon Promotion Constraint

To promote an artifact into canon, ordinary write authority is insufficient if canon governance requires higher authority.

Conceptually:

```text
WRITE FILE
!=
PROMOTE CANON
```

Promotion may require:

```text
PROVENANCE
CONFLICT RESOLUTION
VALIDATION
SUPERSESSION
APPROVAL
COMMIT AUTHORITY
```

---

# 77. Persistent Memory Authorization

Memory operations should distinguish:

```text
READ MEMORY
PROPOSE MEMORY
WRITE WORKING MEMORY
ADMIT PERSISTENT MEMORY
DELETE MEMORY
```

These may have distinct authority requirements.

```text
CAN GENERATE MEMORY CANDIDATE
!=
CAN PERSIST IT
```

---

# 78. State Authorization

Likewise:

```text
READ STATE
WRITE SHADOW STATE
WRITE WORKING STATE
COMMIT AUTHORITATIVE STATE
RESTORE RECOVERY STATE
```

should remain separable where architecture requires.

---

# 79. Control-Plane Interaction

`K_CAPABILITY_AUTHORIZATION` supplies invariants such as:

```text
NO AUTHORITY AMPLIFICATION
NO SELF-AUTHORIZATION
SCOPE PRESERVATION
DELEGATION VALIDITY
FRESHNESS REQUIREMENT
```

The control plane determines governed policy:

```text
WHO
MAY AUTHORIZE
WHAT
UNDER WHICH CONDITIONS
```

---

# 80. Runtime Interaction

Runtime must not interpret:

```text
CAPABILITY AVAILABLE
```

as:

```text
EXECUTE
```

Expected conceptual sequence:

```text
REQUEST
→ AUTHORIZATION RESULT
→ COMMIT ELIGIBILITY
→ EXECUTION
```

where applicable.

---

# 81. Observability

Authorization-sensitive events should be observable.

Examples:

```text
AUTH_REQUESTED
AUTH_GRANTED
AUTH_DENIED
AUTH_CONDITIONAL
AUTH_ESCALATED
AUTH_REVOKED
AUTH_EXPIRED
AUTH_CONFLICT
DELEGATION_CREATED
DELEGATION_REVOKED
CAPABILITY_ESCALATION_BLOCKED
SELF_AUTHORIZATION_BLOCKED
STALE_AUTHORIZATION_REJECTED
```

Logs must not expose protected secrets merely for observability.

---

# 82. Security Boundary

Authorization depends on security but does not replace it.

Relevant concerns include:

```text
AUTHENTICATION
CREDENTIAL INTEGRITY
SESSION INTEGRITY
TOKEN SCOPE
REPLAY PROTECTION
REVOCATION
PRIVILEGE ESCALATION
CONFUSED DEPUTY
```

These belong primarily under `18_SECURITY` and control-plane/runtime implementations.

---

# 83. Kernel Invariants

```text
KCA-01
CAPABILITY MUST NOT BE TREATED AS AUTHORITY

KCA-02
TOOL ACCESS MUST NOT BE TREATED AS PERMISSION

KCA-03
AUTHENTICATION MUST NOT BE TREATED AS AUTHORIZATION

KCA-04
PROPOSAL AUTHORITY MUST NOT BE TREATED AS COMMIT AUTHORITY

KCA-05
AUTHORITY MUST REMAIN SCOPED

KCA-06
DELEGATED AUTHORITY MUST NOT EXCEED VALID DELEGATOR AUTHORITY

KCA-07
INVALID DELEGATION MUST INVALIDATE DEPENDENT AUTHORIZATION

KCA-08
AUTHORITY MUST HAVE VALID PROVENANCE WHEN PROVENANCE IS LOAD-BEARING

KCA-09
REVOKED AUTHORITY MUST NOT REMAIN EFFECTIVE

KCA-10
EXPIRED AUTHORITY MUST NOT REMAIN EFFECTIVE

KCA-11
STALE POLICY MUST NOT SILENTLY AUTHORIZE CURRENT COMMIT

KCA-12
TEST AUTHORITY MUST NOT SILENTLY GENERALIZE TO PRODUCTION

KCA-13
READ AUTHORITY MUST NOT IMPLY WRITE AUTHORITY

KCA-14
WRITE AUTHORITY MUST NOT IMPLY DELETE AUTHORITY

KCA-15
WRITE AUTHORITY MUST NOT IMPLY CANON-PROMOTION AUTHORITY

KCA-16
MODEL OUTPUT MUST NOT CREATE AUTHORITY

KCA-17
MEMORY MUST NOT BE TREATED AS AUTHORITY WITHOUT VALIDATION

KCA-18
WORKFLOW COMPOSITION MUST NOT CREATE NEW AUTHORITY

KCA-19
SKILL CAPABILITY MUST NOT CREATE EXECUTION AUTHORITY

KCA-20
ACTORS MUST NOT SELF-AUTHORIZE OUTSIDE EXPLICIT GOVERNED MECHANISMS

KCA-21
CIRCULAR AUTHORITY MUST NOT CREATE A VALID ROOT

KCA-22
UNKNOWN AUTHORITY MUST NOT BE TREATED AS ALLOW

KCA-23
CONFLICTING AUTHORITY MUST REMAIN VISIBLE UNTIL RESOLVED

KCA-24
LOW RISK MUST NOT CREATE AUTHORITY

KCA-25
HIGH AUTHORITY MUST NOT BYPASS HARD RISK CONSTRAINTS

KCA-26
AUTHORIZATION MUST BE REVALIDATED AFTER MATERIAL EPOCH CHANGE

KCA-27
ATOMIC OPERATIONS MUST HAVE AUTHORITY FOR THEIR COMPLETE LOAD-BEARING EFFECT SET

KCA-28
PARTIAL AUTHORIZATION MUST NOT CAUSE UNSAFE PARTIAL EXECUTION

KCA-29
AUTHORIZED DEPUTIES MUST NOT SERVE AS UNCHECKED PRIVILEGE PROXIES

KCA-30
AUTHORIZATION MUST REMAIN BOUNDED BY SCOPE, REGIME, TIME, POLICY, AND PROVENANCE
```

---

# 84. Required Tests

```text
CAPABILITY-AUTHORITY-SEPARATION TEST
AUTHENTICATION-AUTHORIZATION TEST
READ-WRITE-SEPARATION TEST
WRITE-COMMIT-SEPARATION TEST
PROPOSAL-COMMIT-SEPARATION TEST
SCOPE-ENFORCEMENT TEST
LEAST-AUTHORITY TEST
AUTHORITY-NON-AMPLIFICATION TEST
DELEGATION-CHAIN TEST
BROKEN-DELEGATION TEST
AUTHORITY-PROVENANCE TEST
EXPIRY TEST
REVOCATION TEST
AUTHORITY-EPOCH TEST
POLICY-EPOCH TEST
REGIME-FIREWALL TEST
STATE-RELATIVE-AUTHORIZATION TEST
TOOL-PERMISSION TEST
MODEL-AUTHORITY TEST
MEMORY-AUTHORITY TEST
SKILL-AUTHORITY TEST
WORKFLOW-AUTHORITY TEST
SELF-AUTHORIZATION TEST
CIRCULAR-AUTHORITY TEST
CONFLICTING-AUTHORITY TEST
RISK-AUTHORITY TEST
TOCTOU TEST
MVCC-CAS-AUTHORIZATION TEST
ATOMIC-AUTHORIZATION TEST
PARTIAL-AUTHORIZATION TEST
CAPABILITY-ESCALATION TEST
CONFUSED-DEPUTY TEST
EXTERNAL-EFFECT-AUTHORIZATION TEST
CANON-PROMOTION-AUTHORIZATION TEST
PERSISTENT-MEMORY-AUTHORIZATION TEST
AUTHORITATIVE-STATE-AUTHORIZATION TEST
```

---

# 85. Negative Tests

```text
TOOL EXISTS
→ AUTHORIZED
MUST FAIL

ACTOR AUTHENTICATED
→ ALL OPERATIONS AUTHORIZED
MUST FAIL

READ ALLOWED
→ WRITE ALLOWED
MUST FAIL

WRITE ALLOWED
→ DELETE ALLOWED
MUST FAIL

WRITE FILE ALLOWED
→ PROMOTE CANON ALLOWED
MUST FAIL

CAN PROPOSE
→ CAN COMMIT
MUST FAIL

AGENT RECOMMENDS ACTION
→ ACTION AUTHORIZED
MUST FAIL

MODEL SAYS APPROVE
→ APPROVAL VALID
MUST FAIL

SKILL CAN EXECUTE
→ EXECUTION AUTHORIZED
MUST FAIL

WORKFLOW AUTHORIZED
→ ALL DYNAMIC STEPS AUTHORIZED
MUST FAIL

MEMORY SAYS USER APPROVED
→ CURRENT AUTHORIZATION VALID
MUST FAIL

ROLE = ADMIN
→ UNLIMITED AUTHORITY
MUST FAIL

DELEGATOR HAS READ
→ DELEGATE GETS WRITE
MUST FAIL

A AUTHORIZES B
B AUTHORIZES A
→ VALID AUTHORITY ROOT
MUST FAIL

LOW RISK
→ AUTHORIZED
MUST FAIL

AUTHORIZED YESTERDAY
→ AUTHORIZED TODAY
MUST FAIL

AUTHORIZED IN TEST
→ AUTHORIZED IN PRODUCTION
MUST FAIL

AUTHORIZED BEFORE REVOCATION
→ AUTHORIZED AFTER REVOCATION
MUST FAIL

HAS TOKEN
→ LEGITIMATE PURPOSE AUTHORIZED
MUST FAIL

AUTHORIZED FOR RESOURCE A
→ AUTHORIZED FOR RESOURCE B
MUST FAIL

UNKNOWN AUTHORITY
→ ALLOW
MUST FAIL
```

---

# 86. Failure Modes

```text
CAPABILITY-AUTHORITY COLLAPSE
AUTHENTICATION-AUTHORIZATION COLLAPSE
PRIVILEGE AMPLIFICATION
SCOPE LEAKAGE
ROLE OVERGENERALIZATION
DELEGATION FORGERY
BROKEN DELEGATION CHAIN
STALE AUTHORITY
STALE POLICY
REVOCATION FAILURE
SELF-AUTHORIZATION
CIRCULAR AUTHORITY
CONFUSED DEPUTY
TOCTOU AUTHORIZATION
TOOL-AS-PERMISSION
MODEL-AS-AUTHORITY
MEMORY-AS-AUTHORITY
WORKFLOW PRIVILEGE ESCALATION
PARTIAL-COMMIT AUTHORITY FAILURE
CROSS-REGIME AUTHORITY LEAK
EXTERNAL-EFFECT AUTHORITY LEAK
CANON-PROMOTION AUTHORITY LEAK
```

---

# 87. Recovery Semantics

If unauthorized execution is detected:

```text
DETECT
↓
STOP FURTHER UNAUTHORIZED EFFECTS
↓
CONTAIN
↓
PRESERVE AUDIT / PROVENANCE
↓
IDENTIFY AUTHORITY FAILURE
↓
IDENTIFY AFFECTED STATE
↓
REVOKE / INVALIDATE COMPROMISED AUTHORIZATION
↓
ROLL BACK WHERE VALID AND SAFE
↓
REPAIR MINIMUM AFFECTED SCOPE
↓
REVALIDATE AUTHORITY GRAPH
↓
REVALIDATE STATE
↓
RESUME THROUGH VALID GOVERNED PATH
```

Do not destroy evidence required to determine how authority failed.

---

# 88. Interaction Matrix

```text
AUTHORITY_CANON
→ DEFINES SOURCE LAW / OFFICIAL AUTHORITY SEMANTICS

K_CAPABILITY_AUTHORIZATION
→ DEFINES DETERMINISTIC AUTHORIZATION INVARIANTS

K_RISK_CONSTRAINT
→ CONSTRAINS ACTION BY RISK

CONTROL_PLANE
→ RESOLVES POLICY / APPROVAL / AUTHORITY

RUNTIME
→ EXECUTES AUTHORIZED OPERATIONS

AGENT
→ PROPOSES / ACTS WITHIN GRANTED AUTHORITY

SKILL
→ PROVIDES PROCEDURE

WORKFLOW
→ ORCHESTRATES AUTHORIZED STEPS

TOOL
→ PROVIDES TECHNICAL EFFECTOR

SECURITY
→ PROTECTS IDENTITY / CREDENTIAL / PRIVILEGE BOUNDARIES

OBSERVABILITY
→ RECORDS AUTHORIZATION EVENTS

STATE
→ HOLDS RELEVANT GOVERNED STATE
```

---

# 89. Promotion Gate

Before promotion beyond `AMOS_MODEL`, evidence should establish:

```text
[ ] capability schema implemented
[ ] authority schema implemented
[ ] authorization request schema implemented
[ ] identity binding implemented
[ ] scope enforcement implemented
[ ] least-authority enforcement implemented
[ ] delegation validation implemented
[ ] authority non-amplification implemented
[ ] provenance tracking implemented
[ ] expiry implemented
[ ] revocation implemented
[ ] policy epoch validation implemented
[ ] authority epoch validation implemented
[ ] regime firewall implemented
[ ] proposal/commit separation implemented
[ ] self-authorization protection implemented
[ ] circular-authority detection implemented
[ ] conflicting-authority handling implemented
[ ] risk-constraint integration implemented
[ ] TOCTOU protection implemented
[ ] MVCC/CAS revalidation implemented where applicable
[ ] atomic multi-resource authorization tested
[ ] confused-deputy protection tested
[ ] external-effect authorization tested
[ ] canon-promotion authorization tested
[ ] persistent-memory authorization tested
[ ] observability implemented
[ ] recovery behavior tested
[ ] adversarial authorization tests passed
[ ] unresolved critical gaps registered
```

Until evidenced:

```text
AUTHORIZATION_RUNTIME = UNKNOWN/GAP
AUTHORITY_GRAPH_RUNTIME = UNKNOWN/GAP
DELEGATION_RUNTIME = UNKNOWN/GAP
REVOCATION_RUNTIME = UNKNOWN/GAP
POLICY_EPOCH_ENFORCEMENT = UNKNOWN/GAP
SELF_AUTHORIZATION_PROTECTION = UNKNOWN/GAP
TOCTOU_PROTECTION = UNKNOWN/GAP
ATOMIC_AUTHORIZATION = UNKNOWN/GAP
EMPIRICAL_VALIDATION = UNKNOWN/GAP
FORMAL_VERIFICATION = UNKNOWN/GAP
```

---

# 90. RSCF Node

```RSCF-NODE
node_id: AMOS-OS-K-CAPABILITY-AUTHORIZATION
node_type: kernel_capability_authorization_contract
domain: AMOS_OS_KERNEL
functional_type: CapabilityAuthorizationKernel
lifecycle_stage: Architecture
claim_class: AMOS_MODEL

RSCF-RELATIONS:
  - ROOTED_IN: README
  - DEPENDENCY_BOUND_TO: DEPENDENCY_MAP

  - GOVERNED_BY: AMOS_CORE_LAWS
  - CONSTRAINED_BY: INVARIANT_REGISTRY
  - PRECEDENCE_GOVERNED_BY: LAW_HIERARCHY
  - AUTHORITY_GOVERNED_BY: AUTHORITY_CANON
  - PROVENANCE_GOVERNED_BY: CANON_PROVENANCE

  - INDEXED_BY: KERNEL_MAP
  - LOGIC_BOUND_TO: K_CORE19_LOGIC
  - META_LOGIC_BOUND_TO: K_META_LOGIC
  - IDENTITY_BOUND_TO: K_IDENTITY
  - CONTEXT_BOUND_TO: K_CONTEXT_STATE
  - SYSTEM_STATE_BOUND_TO: K_SYSTEM_STATE
  - RISK_BOUND_TO: K_RISK_CONSTRAINT
  - EVENT_BOUND_TO: K_EVENT_BUS

  - POLICY_BOUND_TO: README
  - EXECUTION_BOUND_TO: README

  - MEMORY_BOUND_TO: README
  - STATE_BOUND_TO: README
  - TOOL_BOUND_TO: README
  - INTERFACE_BOUND_TO: README
  - OBSERVED_BY: README
  - SECURITY_BOUND_TO: README
  - VERIFIED_BY: README
```

---

# 91. Canonical Summary

```text
CAN THE SYSTEM DO IT?
↓
CAPABILITY QUESTION

MAY THIS ACTOR DO IT?
↓
AUTHORITY QUESTION

MAY THIS ACTOR
USE THIS CAPABILITY
FOR THIS OPERATION
ON THIS TARGET
IN THIS SCOPE
IN THIS REGIME
AT THIS TIME
UNDER THIS POLICY
WITH THIS RISK?
↓
AUTHORIZATION QUESTION
```

Core laws:

```text
CAPABILITY != AUTHORITY
TOOL != PERMISSION
ACCESS != AUTHORIZATION
AUTHENTICATION != AUTHORIZATION
IDENTITY != AUTHORITY
ROLE != UNLIMITED AUTHORITY
MODEL != AUTHORITY
MEMORY != AUTHORITY
AGENT != AUTHORITY
SKILL != AUTHORITY
WORKFLOW != AUTHORITY
PROPOSAL != COMMIT
READ != WRITE
WRITE != COMMIT
LOW RISK != AUTHORIZED
DELEGATION != AUTHORITY AMPLIFICATION
OLD AUTHORIZATION != CURRENT AUTHORIZATION
TEST AUTHORITY != PRODUCTION AUTHORITY
AUTHORIZATION != EXECUTION
```

The decisive invariant is:

```text
AMOS DOES NOT ASK ONLY:

CAN THIS ACTOR
PERFORM THE
OPERATION?

AMOS ASKS:

WHO IS
THE ACTOR?

WHAT EXACT
CAPABILITY
IS BEING USED?

WHAT EXACT
EFFECT IS
REQUESTED?

WHAT IS
THE TARGET?

WHAT IS
THE AUTHORITY
SOURCE?

IS THAT
AUTHORITY
AUTHENTIC?

IS IT
CURRENT?

IS IT
IN SCOPE?

IS THE
DELEGATION
VALID?

HAS ANY
DELEGATION EDGE
AMPLIFIED
AUTHORITY?

WHAT POLICY
EPOCH APPLIES?

WHAT AUTHORITY
EPOCH APPLIES?

WHAT REGIME
ARE WE IN?

HAS THE
STATE CHANGED
SINCE
AUTHORIZATION?

IS THIS
READ,
WRITE,
COMMIT,
PUBLISH,
OR EXTERNAL
EFFECT?

DOES THE
ACTOR HAVE
AUTHORITY FOR
THAT EXACT
LEVEL?

IS THE
ACTION INSIDE
THE AUTHORIZED
RISK ENVELOPE?

IS AN
INDEPENDENT
APPROVAL
REQUIRED?

IS THERE
A CONFLICTING
DENIAL?

IS THE
AUTHORITY
CHAIN ROOTED
OR CIRCULAR?

IS THE
ACTOR USING
AN AUTHORIZED
DEPUTY TO
BYPASS ITS
OWN LIMITS?

HAS THE
AUTHORITY
EXPIRED?

HAS IT
BEEN REVOKED?

IF A
LOAD-BEARING
FACT IS
UNKNOWN,

AMOS DOES
NOT TURN
UNKNOWN INTO
PERMISSION.

IF AUTHORITY
IS CONFLICTED,

AMOS PRESERVES:

COMPETING.

IF HIGHER
AUTHORITY IS
REQUIRED,

AMOS RETURNS:

ESCALATE.

IF THE
ACTOR MAY
RECOMMEND
BUT MAY NOT
COMMIT,

AMOS PRESERVES:

PROPOSAL ONLY.

AND WHEN
AUTHORIZATION
IS VALID,

IT REMAINS
BOUNDED BY:

ACTOR,
CAPABILITY,
OPERATION,
TARGET,
SCOPE,
REGIME,
TIME,
POLICY,
RISK,
PROVENANCE,
AND
AUTHORITY.
```

## Related

README ·
[[DEPENDENCY_MAP]] ·
[[AMOS_CORE_LAWS]] ·
[[INVARIANT_REGISTRY]] ·
[[LAW_HIERARCHY]] ·
[[AUTHORITY_CANON]] ·
[[CANON_PROVENANCE]] ·
[[KERNEL_MAP]] ·
[[K_CORE19_LOGIC]] ·
[[K_META_LOGIC]] ·
[[K_IDENTITY]] ·
[[K_CONTEXT_STATE]] ·
[[K_SYSTEM_STATE]] ·
[[K_RISK_CONSTRAINT]] ·
[[K_EVENT_BUS]] ·
README ·
README ·
README ·
README ·
README ·
README ·
README ·
README ·
README

```text

**Classification note:** this is substantive replacement content for `02_KERNEL/K_CAPABILITY_AUTHORIZATION.md`, but remains **AMOS_MODEL**. It specifies the proposed kernel-level capability/authority separation and authorization invariants; it does not establish that the corresponding control-plane policies, authorization graph, delegation enforcement, runtime gates, revocation, MVCC/CAS checks, or security mechanisms are implemented or empirically validated. Those remain `UNKNOWN/GAP` until supported by implementation, provenance, tests, and explicit promotion.
```

---

[[00_ROOT_MOC]]|[[AMOS MOC]]

---
**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]]

---
**MOC:** [[07_AUTHORITY_MOC]]
