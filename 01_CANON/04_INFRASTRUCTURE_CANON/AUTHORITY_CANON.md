---
type: canon
source: 01_CANON/04_INFRASTRUCTURE_CANON
artifact_id: AMOS-AUTHORITY-CANON
name: AUTHORITY_CANON
title: "AMOS Authority Canon — Decision Rights, Permission, Commit, and Governance Law"
document_version: 2.0.0
canon_version: 4.4
amos_core_target: v4.4
status: ACTIVE_CANON_CANDIDATE
conclusion_class: AMOS_MODEL
rscf_state: derived
canon_group: governance
canon_type: authority-canon
origin_architect: Trang Phan
steward: Trang Phan
created: 2026-08-25
updated: 2026-08-25
tags:
  - amos
  - canon
  - universe
  - amos-os
  - amos-core
  - amos-core-v4-4
  - authority
  - governance
  - decision-rights
  - permissions
  - authorization
  - control-plane
  - commit
  - proposal
  - provenance
  - state
  - mvcc
  - cas
  - rscf
  - causal-lineage
  - recovery
  - security
  - canon-group/governance
  - canon/framework
  - canon/model
  - rscf/claim
  - rscf/provenance
  - rscf/state/derived
  - readme
  - architecture
  - placement-rules
  - amos-core-laws
  - law-hierarchy
  - operating-model
aliases:
  - AMOS Authority Canon - Authority Canon - AMOS Decision Rights Canon - AMOS Governance Author
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# AMOS Authority Canon

**Origin architect / steward:** Trang Phan

> **Status:** `ACTIVE_CANON_CANDIDATE`
> **AMOS Core target:** `v4.4`
> **Conclusion class:** `AMOS_MODEL`
> rscf:
> state: DERIVED
> claim_class: DERIVED
> provenance: AMOS_corpus
> scope: AMOS_general

______________________________________________________________________

## 0. Purpose

The **AMOS Authority Canon** defines the canonical separation between:

```text
CAPABILITY
PERMISSION
AUTHORITY
PROPOSAL
DECISION
COMMIT
EXECUTION
EFFECT
```

within AMOS OS.

Its central purpose is to prevent reasoning capability, system access, agent identity, model confidence, workflow position, or tool availability from silently becoming operational authority.

Canonical law:

```text
CAPABILITY != AUTHORITY
```

The existence of a capability establishes only that an operation may be technically possible.

It does not establish that the operation is permitted, authorized, valid, safe, current, or eligible for commit.

______________________________________________________________________

## 1. Architectural Position

Authority primarily belongs to the governance path spanning:

```text
CANON
↓
KERNEL
↓
CONTROL PLANE
↓
RUNTIME
↓
EXECUTION
```

with cross-cutting dependencies on:

```text
STATE
PROVENANCE
SECURITY
IDENTITY
POLICY
OBSERVABILITY
SCHEMAS
TESTS
OPERATIONS
```

Authority must not be silently inferred from lower architectural layers.

______________________________________________________________________

## 2. Authority Stack

Canonical authority flow:

```text
CANONICAL CONSTRAINTS
↓
KERNEL INVARIANTS
↓
CONTROL-PLANE POLICY
↓
AUTHORITY EVALUATION
↓
COMMIT ELIGIBILITY
↓
RUNTIME EXECUTION
↓
EXTERNAL EFFECT
```

The direction is intentionally asymmetric.

Execution cannot retroactively create authority.

______________________________________________________________________

## 3. Hard Authority Boundaries

```text
CAPABILITY != AUTHORITY

IDENTITY != AUTHORITY

ROLE != AUTHORITY

ACCESS != AUTHORITY

TOOL != PERMISSION

PERMISSION != DECISION

DECISION != EXECUTION

PROPOSAL != COMMIT

PLAN != AUTHORIZATION

MODEL != AUTHORITY

MEMORY != AUTHORITY

KNOWLEDGE != AUTHORITY

AGENT != AUTHORITY

WORKFLOW != AUTHORITY

RUNTIME != CONTROL_PLANE

EXECUTION != VALIDATION

SUCCESS != AUTHORIZATION

PRIOR AUTHORITY != CURRENT AUTHORITY

AUTHORITY != UNIVERSAL AUTHORITY
```

These boundaries are load-bearing.

______________________________________________________________________

## 4. Capability

Capability answers:

```text
CAN THIS COMPONENT PERFORM OPERATION X?
```

Examples:

```text
MODEL CAN GENERATE A PLAN

AGENT CAN REQUEST A TOOL

TOOL CAN WRITE A FILE

RUNTIME CAN EXECUTE A WORKFLOW

SYSTEM CAN MODIFY STATE
```

None of these statements establish authorization.

______________________________________________________________________

## 5. Permission

Permission answers:

```text
IS OPERATION X ALLOWED
UNDER THE APPLICABLE POLICY?
```

Permission is typed and scoped.

Conceptually:

```yaml
permission:
  subject:
  action:
  resource:
  scope:
  environment:
  conditions:
  validity_window:
  provenance:
```

A permission outside its envelope is not valid permission.

______________________________________________________________________

## 6. Authority

Authority answers:

```text
WHO OR WHAT
HAS THE VALID DECISION RIGHT
TO AUTHORIZE THIS ACTION
UNDER THESE CONDITIONS?
```

Authority therefore requires more than technical access.

Conceptually:

```text
AUTHORITY
=
IDENTITY
+
DECISION RIGHT
+
SCOPE
+
POLICY COMPATIBILITY
+
STATE VALIDITY
+
TEMPORAL VALIDITY
+
PROVENANCE
```

subject to applicable invariants.

______________________________________________________________________

## 7. Authority Envelope

Every consequential authority grant should have an applicability envelope.

```yaml
authority_envelope:
  authority_id:
  subject:
  role:
  permitted_actions: []
  prohibited_actions: []
  resources: []
  scope:
  environment:
  regime:
  validity_start:
  validity_end:
  conditions: []
  dependencies: []
  provenance:
  revocation_conditions: []
```

Authority outside this envelope is:

```text
INVALID
```

or:

```text
UNKNOWN/GAP
```

depending on available evidence.

______________________________________________________________________

## 8. Authority Is Local

AMOS authority is local, typed, scoped, provenance-aware, regime-aware, and freshness-bounded.

Therefore:

```text
AUTHORIZED(ACTION X)
```

does not imply:

```text
AUTHORIZED(ACTION Y)
```

Likewise:

```text
AUTHORIZED(RESOURCE A)
!=
AUTHORIZED(RESOURCE B)
```

and:

```text
AUTHORIZED(REGIME R1)
!=
AUTHORIZED(REGIME R2)
```

______________________________________________________________________

## 9. Proposal

A proposal is a candidate action submitted for evaluation.

```text
COGNITION
↓
PLAN
↓
PROPOSAL
```

Proposal status establishes no commit right.

```text
PROPOSAL != COMMIT
```

A proposal may be:

```text
ACCEPTED
REJECTED
DEFERRED
CONDITIONAL
ESCALATED
QUARANTINED
UNKNOWN/GAP
```

______________________________________________________________________

## 10. Decision

A decision is a governed determination concerning a proposal or state transition.

A valid decision should preserve:

```text
DECISION IDENTITY
DECISION MAKER / AUTHORITY
INPUT STATE
POLICY BASIS
DEPENDENCIES
PROVENANCE
SCOPE
TIME
RESULT
```

Decision creation does not itself prove execution.

______________________________________________________________________

## 11. Commit

Commit is the authoritative transition from an eligible proposal/decision into authoritative state or approved execution.

Canonical distinction:

```text
PROPOSE
↓
VALIDATE
↓
AUTHORIZE
↓
COMMIT
```

Never collapse this into:

```text
PROPOSE
↓
EXECUTE
```

unless an explicitly authorized policy defines that path.

______________________________________________________________________

## 12. Execution

Runtime execution occurs only after required authority conditions are satisfied.

Canonical path:

```text
REQUEST
↓
PROPOSAL
↓
POLICY CHECK
↓
AUTHORITY CHECK
↓
STATE CHECK
↓
COMMIT ELIGIBILITY
↓
COMMIT
↓
RUNTIME EXECUTION
↓
OBSERVATION
```

______________________________________________________________________

## 13. External Effects

Actions producing external effects require explicit governance proportional to their consequences.

Examples:

```text
WRITE
DELETE
SEND
PUBLISH
TRANSFER
DEPLOY
EXECUTE
MODIFY
REVOKE
APPROVE
COMMIT
```

Higher irreversibility increases validation requirements.

______________________________________________________________________

## 14. Authority Classes

AMOS may model authority classes such as:

```text
READ AUTHORITY

PROPOSAL AUTHORITY

REVIEW AUTHORITY

APPROVAL AUTHORITY

COMMIT AUTHORITY

EXECUTION AUTHORITY

ADMINISTRATIVE AUTHORITY

EMERGENCY AUTHORITY

REVOCATION AUTHORITY

RECOVERY AUTHORITY
```

These classes must not be silently conflated.

______________________________________________________________________

## 15. Read Authority

Read authority permits access to bounded information.

```text
READ
!=
WRITE
```

and:

```text
READ
!=
DISCLOSE
```

Access to information does not automatically authorize redistribution.

______________________________________________________________________

## 16. Proposal Authority

Proposal authority permits generation or submission of candidate actions.

It does not grant:

```text
APPROVAL
COMMIT
EXECUTION
```

rights.

Agents commonly operate at this level unless explicitly elevated.

______________________________________________________________________

## 17. Review Authority

Review authority permits evaluation of a proposal.

Possible outputs:

```text
PASS
FAIL
CONDITIONAL
ESCALATE
UNKNOWN/GAP
```

Review authority does not automatically include approval authority.

______________________________________________________________________

## 18. Approval Authority

Approval authority permits an eligible proposal to advance toward commit.

Approval remains bounded by:

```text
SCOPE
POLICY
STATE
TIME
DEPENDENCIES
```

An approval may become stale before execution.

______________________________________________________________________

## 19. Commit Authority

Commit authority permits mutation of authoritative state.

This is a privileged boundary.

```text
WORKING STATE
↓
VALIDATION
↓
AUTHORIZED COMMIT
↓
AUTHORITATIVE STATE
```

Commit authority should be explicit and observable.

______________________________________________________________________

## 20. Execution Authority

Execution authority permits an approved operation to be carried out.

Commit authority and execution authority may be separated.

```text
CAN AUTHORIZE
!=
CAN EXECUTE
```

and:

```text
CAN EXECUTE
!=
CAN AUTHORIZE
```

This separation may reduce concentration of authority.

______________________________________________________________________

## 21. Revocation Authority

Authority must be revocable where architecture permits.

Canonical transition:

```text
ACTIVE AUTHORITY
↓
REVOCATION EVENT
↓
INVALID / REVOKED AUTHORITY
```

Previously valid credentials or decisions must not silently remain valid after revocation.

______________________________________________________________________

## 22. Delegation

Authority may be delegated only when delegation itself is authorized.

Conceptually:

```text
AUTHORITY A
↓
VALID DELEGATION RULE
↓
AUTHORITY B
```

The delegate cannot inherit more authority than the delegator is permitted to delegate.

```text
DELEGATED AUTHORITY
<=
DELEGABLE AUTHORITY
```

______________________________________________________________________

## 23. Delegation Envelope

```yaml
delegation:
  delegator:
  delegate:
  authority_type:
  scope:
  permitted_actions: []
  excluded_actions: []
  start:
  expiry:
  delegation_depth:
  re_delegation_allowed:
  provenance:
  revocation:
```

Missing critical delegation evidence remains:

```text
UNKNOWN/GAP
```

______________________________________________________________________

## 24. No Authority Amplification

A chain of delegation must not increase authority.

```text
A → B → C
```

cannot produce:

```text
AUTHORITY(C) > AUTHORITY(A)
```

unless an independent authority source explicitly grants the additional rights.

______________________________________________________________________

## 25. Authority Intersection

When several independent authority constraints apply, effective authority is the valid intersection.

Conceptually:

```text
EFFECTIVE AUTHORITY
=
IDENTITY RIGHTS
∩
ROLE RIGHTS
∩
RESOURCE POLICY
∩
ENVIRONMENT POLICY
∩
CURRENT STATE
∩
VALIDITY WINDOW
```

Not the union.

______________________________________________________________________

## 26. Least Authority

Components should receive the minimum authority required for the authorized task.

```text
REQUIRED AUTHORITY
<=
GRANTED AUTHORITY
```

with unnecessary authority minimized.

This reduces blast radius.

______________________________________________________________________

## 27. Authority and Agents

Agent identity does not imply authority.

```text
AGENT
=
ROLE-BASED WORKER
```

An agent may:

```text
OBSERVE
REASON
PLAN
PROPOSE
REVIEW
```

according to its contract.

It may only:

```text
APPROVE
COMMIT
EXECUTE
```

when explicitly authorized.

______________________________________________________________________

## 28. Authority and Skills

A skill defines reusable procedure.

```text
SKILL != AUTHORITY
```

A skill may describe how to perform an operation without granting permission to perform it.

______________________________________________________________________

## 29. Authority and Workflows

A workflow defines orchestration.

```text
WORKFLOW != AUTHORITY
```

Being positioned at a workflow step does not independently create decision rights.

Every privileged step must inherit or resolve valid authority.

______________________________________________________________________

## 30. Authority and Models

Models provide computation.

```text
MODEL != AUTHORITY
```

Model confidence, ranking, recommendation, or prediction cannot independently authorize action.

```text
HIGH CONFIDENCE
!=
HIGH AUTHORITY
```

______________________________________________________________________

## 31. Authority and Tools

Tools provide capability.

```text
TOOL != PERMISSION
```

Tool presence proves only:

```text
CAPABILITY EXISTS
```

not:

```text
ACTION AUTHORIZED
```

______________________________________________________________________

## 32. Authority and Memory

Memory may preserve prior decisions or permissions.

But:

```text
REMEMBERED AUTHORITY
!=
CURRENT AUTHORITY
```

Authority must be revalidated against current state, time, policy, and revocation status when material.

______________________________________________________________________

## 33. Authority and Knowledge

Knowledge may describe authority structures.

It does not itself confer authority.

```text
KNOWLEDGE OF PERMISSION
!=
POSSESSION OF PERMISSION
```

______________________________________________________________________

## 34. Authority and Canon

Canon defines authoritative laws and constraints.

But:

```text
CANON
!=
ACTOR AUTHORITY
```

Canon may define how authority is created, bounded, delegated, revoked, and validated.

______________________________________________________________________

## 35. Authority and Kernel

Kernel logic may deterministically evaluate authority conditions.

```text
KERNEL
=
INVARIANT / OPERATOR LOGIC
```

It does not independently invent governance rights.

```text
KERNEL != GOVERNANCE SOURCE
```

______________________________________________________________________

## 36. Authority and Control Plane

The control plane governs:

```text
POLICY
AUTHORITY
COMMIT
PROVENANCE
COORDINATION
```

where defined by the architecture.

Canonical boundary:

```text
CONTROL_PLANE != RUNTIME
```

The runtime executes governed outcomes.

______________________________________________________________________

## 37. Authority and Runtime

Runtime may execute authorized work.

```text
RUNTIME
!=
AUTHORITY SOURCE
```

Runtime success does not retroactively validate an unauthorized action.

```text
EXECUTION SUCCESS
!=
AUTHORIZATION
```

______________________________________________________________________

## 38. Authority and State

Authority decisions depend on state.

Potential states:

```text
AUTHORITATIVE STATE
WORKING STATE
SHADOW STATE
RECOVERY STATE
```

Authority evaluated against stale state may be invalid.

______________________________________________________________________

## 39. State Version Binding

Consequential authority should bind to the state version on which it was evaluated where applicable.

Conceptually:

```text
READ STATE V17
↓
AUTHORIZE AGAINST V17
↓
STATE BECOMES V18
↓
REVALIDATE BEFORE COMMIT
```

This aligns with AMOS MVCC/CAS concepts.

It does not claim every implementation literally uses database MVCC.

______________________________________________________________________

## 40. CAS Authority Gate

Conceptually:

```text
EXPECTED_STATE = V17
CURRENT_STATE = V17
↓
COMMIT MAY PROCEED
```

but:

```text
EXPECTED_STATE = V17
CURRENT_STATE = V18
↓
COMMIT MUST NOT SILENTLY PROCEED
```

Required response may be:

```text
REVALIDATE
REBASE
REAUTHORIZE
ABORT
```

depending on policy.

______________________________________________________________________

## 41. Time-Bounded Authority

Authority can expire.

```text
VALID AT T1
!=
VALID AT T2
```

Authority should preserve temporal validity where material.

______________________________________________________________________

## 42. Regime-Bounded Authority

Authority granted in one operating regime may not survive a regime transition.

```text
AUTHORITY(R1)
!=
AUTHORITY(R2)
```

unless compatibility is explicitly established.

______________________________________________________________________

## 43. Scope-Bounded Authority

Authority must inherit an applicability scope.

Possible dimensions:

```text
SYSTEM
RESOURCE
DOMAIN
ACTION
POPULATION
ENVIRONMENT
REGION
TIME
REGIME
RISK CLASS
```

No silent scope expansion.

______________________________________________________________________

## 44. Authority Provenance

Every consequential authority decision should be traceable to its source.

Conceptually:

```text
ACTION
↓
AUTHORIZATION
↓
AUTHORITY GRANT
↓
POLICY
↓
CANON / GOVERNANCE SOURCE
```

Broken provenance weakens authority validity.

______________________________________________________________________

## 45. Persistent Authority Provenance

Persisted authorization should preserve enough context to answer:

```text
WHO AUTHORIZED?

WHAT WAS AUTHORIZED?

FOR WHICH RESOURCE?

UNDER WHICH POLICY?

AGAINST WHICH STATE?

WHEN?

FOR HOW LONG?

UNDER WHICH REGIME?

WITH WHICH DEPENDENCIES?

WAS IT REVOKED?
```

______________________________________________________________________

## 46. Authority Lineage

Authority lineage may form a graph:

```text
ROOT AUTHORITY
│
├── DELEGATION A
│   └── DELEGATION A1
│
└── DELEGATION B
```

Lineage must not be confused with independent authority.

Multiple descendants of one grant remain one authority ancestry.

______________________________________________________________________

## 47. Sybil Resistance for Authority

Duplicating one authority source does not create independent authorization.

```text
ONE GRANT
→
TEN COPIES
```

still represents:

```text
ONE AUTHORITY ORIGIN
```

Repetition does not strengthen the grant.

______________________________________________________________________

## 48. Competing Authority Claims

Two authority claims may conflict.

Example:

```text
POLICY A → ALLOW
POLICY B → DENY
```

Do not arbitrarily select one.

The result may remain:

```text
COMPETING
```

until hierarchy, scope, recency, supersession, or governance resolves the conflict.

______________________________________________________________________

## 49. Law Hierarchy

Authority resolution must respect the canonical law hierarchy.

Conceptually:

```text
HIGHER GOVERNING LAW
↓
CANON
↓
POLICY
↓
DELEGATED AUTHORITY
↓
LOCAL DECISION
```

Exact hierarchy must bind to `LAW_HIERARCHY.md`.

No authority layer may silently override a superior binding constraint.

______________________________________________________________________

## 50. Deny Precedence

Where AMOS policy explicitly defines deny precedence:

```text
ALLOW
+
VALID DENY
↓
DENY
```

However, deny precedence must not be invented universally where canon has not established it.

If conflict-resolution semantics are unavailable:

```text
UNKNOWN/GAP
```

______________________________________________________________________

## 51. Authority Conflict

Conflict conditions include:

```text
MULTIPLE AUTHORITY SOURCES

INCOMPATIBLE POLICIES

AMBIGUOUS SCOPE

STALE GRANT

UNCLEAR DELEGATION

REVOKED CREDENTIAL

STATE VERSION CONFLICT

REGIME CHANGE

BROKEN PROVENANCE
```

Consequential actions should escalate rather than silently choose.

______________________________________________________________________

## 52. Authority Confidence

Confidence in reasoning does not replace authority validation.

```text
CONFIDENCE = 0.99
```

does not imply:

```text
AUTHORIZED = TRUE
```

Authority is a governance property, not a model-confidence property.

______________________________________________________________________

## 53. Authority RSCF

Consequential authorization may be represented as an RSCF.

```text
AUTHORITY CLAIM
├── SUBJECT IDENTITY
├── REQUESTED ACTION
├── RESOURCE
├── AUTHORITY SOURCE
├── POLICY
├── SCOPE
├── STATE
├── TIME
├── REGIME
├── PROVENANCE
├── CONFLICTS
├── REVOCATION STATUS
└── RESULT
```

______________________________________________________________________

## 54. Authority Proof Capsule

```yaml
authority_proof:
  claim:
    subject:
    action:
    resource:

  authority_source:
  policy_basis:

  scope:
  regime:
  state_version:
  temporal_validity:

  delegation_lineage: []
  dependencies: []

  conflicts: []
  revocation_status:

  conclusion_class:
  invalidation_conditions: []
```

This structure supports bounded reuse.

______________________________________________________________________

## 55. Authority Reuse

Prior authority evaluation may be reused only when:

```text
IDENTITY UNCHANGED
AND
ACTION COMPATIBLE
AND
RESOURCE COMPATIBLE
AND
POLICY CURRENT
AND
SCOPE COMPATIBLE
AND
REGIME COMPATIBLE
AND
STATE COMPATIBLE
AND
VALIDITY WINDOW ACTIVE
AND
NO REVOCATION
AND
NO MATERIAL CONFLICT
```

Otherwise:

```text
REAUTHORIZE
```

______________________________________________________________________

## 56. Atomic Multi-Authority Decisions

Some actions may require multiple authority predicates.

Example:

```text
SECURITY APPROVAL
+
DOMAIN APPROVAL
+
RESOURCE AUTHORIZATION
+
CURRENT STATE VALIDATION
```

If all are required:

```text
A ∧ B ∧ C ∧ D
```

must hold before commit eligibility.

Partial approval is not full authorization.

______________________________________________________________________

## 57. Separation of Duties

High-impact operations may separate:

```text
PROPOSER
REVIEWER
APPROVER
COMMITTER
EXECUTOR
AUDITOR
```

This reduces concentration risk.

Exact separation requirements remain policy-specific.

______________________________________________________________________

## 58. Self-Authorization Firewall

A component must not silently create the authority required to approve its own privileged action.

```text
PROPOSER
!=
AUTOMATIC APPROVER
```

and:

```text
CAPABILITY DISCOVERY
!=
AUTHORITY CREATION
```

______________________________________________________________________

## 59. Authority Escalation

Escalate when:

```text
AUTHORITY UNKNOWN

SCOPE AMBIGUOUS

POLICY CONFLICTS

PROVENANCE BROKEN

STATE CHANGED

REGIME CHANGED

AUTHORITY EXPIRED

REVOCATION UNCERTAIN

DELEGATION UNCLEAR

IRREVERSIBLE ACTION

HIGH STAKES
```

Do not convert ambiguity into implicit permission.

______________________________________________________________________

## 60. UNKNOWN/GAP Authority Rule

Canonical rule:

```text
UNKNOWN/GAP != AUTHORIZED
```

For consequential operations:

```text
UNKNOWN AUTHORITY
↓
DO NOT SILENTLY COMMIT
```

The appropriate outcome may be:

```text
REQUEST CLARIFICATION
REVALIDATE
ESCALATE
DEFER
ABORT
```

depending on context.

______________________________________________________________________

## 61. Authority and Irreversibility

Validation depth should increase with:

```text
IRREVERSIBLE COST
LEGAL EXPOSURE
FINANCIAL EXPOSURE
SAFETY EXPOSURE
SECURITY EXPOSURE
INSTITUTIONAL IMPACT
DOWNSTREAM DEPENDENCY
```

Prefer reversible staged actions when authority uncertainty remains.

______________________________________________________________________

## 62. Emergency Authority

Emergency authority, if implemented, must be explicit.

It should define:

```text
TRIGGER
SCOPE
DURATION
PERMITTED ACTIONS
PROHIBITED ACTIONS
OVERRIDE RULES
LOGGING
POST-EVENT REVIEW
REVOCATION
```

Emergency conditions must not imply unlimited authority.

______________________________________________________________________

## 63. Break-Glass Authority

If a break-glass mechanism exists:

```text
NORMAL AUTHORITY
↓
EMERGENCY CONDITION
↓
EXPLICIT BREAK-GLASS GRANT
↓
LIMITED ACTION
↓
AUDIT
↓
EXPIRY / REVOCATION
↓
POST-HOC REVIEW
```

The existence of this pattern in the canon does not establish implementation.

______________________________________________________________________

## 64. Authority Failure Modes

Critical failure modes include:

```text
AUTHORITY CONFUSED WITH CAPABILITY

TOOL ACCESS CONFUSED WITH PERMISSION

STALE AUTHORITY

SCOPE LEAKAGE

DELEGATION AMPLIFICATION

BROKEN PROVENANCE

SELF-AUTHORIZATION

POLICY BYPASS

RUNTIME BYPASS OF CONTROL PLANE

STATE VERSION RACE

REVOCATION FAILURE

REGIME LEAKAGE

UNOBSERVED PRIVILEGED ACTION

AUTHORITY CONCENTRATION

UNKNOWN TREATED AS ALLOW
```

______________________________________________________________________

## 65. Failure Locality

An invalid authority edge should invalidate only dependent authorization results.

```text
FAILED AUTHORITY GRANT
↓
INVALIDATE DESCENDANTS
```

Do not invalidate unrelated valid authority structures.

______________________________________________________________________

## 66. Recovery

Authority recovery should:

```text
IDENTIFY FAILED GRANT / EDGE
↓
FREEZE AFFECTED COMMIT PATH
↓
ROLL BACK TO NEAREST VALID AUTHORITY STATE
↓
REVALIDATE DEPENDENTS
↓
RESTORE OR REJECT
```

Unaffected authority remains preserved.

______________________________________________________________________

## 67. Revocation Propagation

If:

```text
A
↓
B
↓
C
```

and B derives authority solely from A, revoking A should invalidate dependent authority through the lineage where applicable.

Independent grants remain separately evaluated.

______________________________________________________________________

## 68. Causal Epoch Alignment

Authority evaluated in causal epoch:

```text
E1
```

must not silently survive a material causal epoch transition:

```text
E1 → E2
```

when the transition invalidates its dependencies.

Revalidation is required where epoch compatibility cannot be proven.

______________________________________________________________________

## 69. Local Finality

An authority decision may finalize locally when its complete dependency closure is established.

```text
LOCAL AUTHORITY FINALITY
```

does not imply:

```text
GLOBAL SYSTEM FINALITY
```

Cross-boundary effects require their own dependency checks.

______________________________________________________________________

## 70. Proof-Based Coordination Avoidance

Global authority coordination may be avoided when independence is demonstrated.

Conceptually:

```text
DISJOINT AUTHORITY SCOPE
+
INDEPENDENT PROVENANCE
+
NO SHARED MUTABLE INVARIANT
+
NO CROSS-DEPENDENCY
+
NO MATERIAL CONFLICT
↓
LOCAL AUTHORIZATION MAY PROCEED
```

Independence must be demonstrated, not assumed.

______________________________________________________________________

## 71. Observability

Privileged authority transitions should eventually emit sufficient trace information for:

```text
REQUEST

POLICY EVALUATION

AUTHORITY SOURCE

DELEGATION

APPROVAL

DENIAL

ESCALATION

COMMIT

EXECUTION

REVOCATION

FAILURE

RECOVERY
```

Sensitive data must remain protected.

______________________________________________________________________

## 72. Audit

Authority audit should be able to reconstruct:

```text
WHO
DID WHAT
TO WHICH RESOURCE
UNDER WHICH AUTHORITY
UNDER WHICH POLICY
AT WHAT TIME
AGAINST WHICH STATE
WITH WHICH RESULT
```

where applicable.

______________________________________________________________________

## 73. Security Integration

Authority depends on but is distinct from:

```text
AUTHENTICATION
AUTHORIZATION
IDENTITY
CREDENTIALS
SECRETS
ACCESS CONTROL
```

Authentication proves an identity claim to some defined level.

It does not alone establish decision authority.

```text
AUTHENTICATED != AUTHORIZED
```

______________________________________________________________________

## 74. Governance Integration

Governance defines:

```text
WHO MAY DECIDE

WHAT MAY BE DECIDED

UNDER WHICH CONDITIONS

WHO MAY DELEGATE

WHO MAY OVERRIDE

WHO MAY REVOKE

HOW CONFLICTS ARE RESOLVED

HOW DECISIONS ARE AUDITED
```

Authority is therefore a governed relation, not a property inherent to an agent or model.

______________________________________________________________________

## 75. Authority Lifecycle

```text
DEFINE
↓
GRANT
↓
ACTIVATE
↓
USE
↓
OBSERVE
↓
REVALIDATE
↓
RENEW / MODIFY / DELEGATE / REVOKE
↓
ARCHIVE
```

Each transition should preserve lineage where material.

______________________________________________________________________

## 76. Authority State Machine

Conceptually:

```text
PROPOSED
↓
VALIDATED
↓
ACTIVE
├── SUSPENDED
├── EXPIRED
├── REVOKED
└── SUPERSEDED
```

An inactive authority state must not silently authorize new actions.

______________________________________________________________________

## 77. Core Authority Invariants

```text
AUTH-001  CAPABILITY != AUTHORITY

AUTH-002  IDENTITY != AUTHORITY

AUTH-003  ROLE != AUTHORITY

AUTH-004  ACCESS != AUTHORITY

AUTH-005  TOOL != PERMISSION

AUTH-006  MODEL != AUTHORITY

AUTH-007  AGENT != AUTHORITY

AUTH-008  WORKFLOW != AUTHORITY

AUTH-009  PROPOSAL != COMMIT

AUTH-010  PLAN != AUTHORIZATION

AUTH-011  AUTHENTICATED != AUTHORIZED

AUTH-012  APPROVAL != EXECUTION

AUTH-013  EXECUTION SUCCESS != AUTHORIZATION

AUTH-014  REMEMBERED AUTHORITY != CURRENT AUTHORITY

AUTH-015  AUTHORITY IS SCOPE-BOUNDED

AUTH-016  AUTHORITY IS TIME-BOUNDED WHERE APPLICABLE

AUTH-017  AUTHORITY IS REGIME-BOUNDED

AUTH-018  AUTHORITY REQUIRES PROVENANCE

AUTH-019  DELEGATION MUST NOT AMPLIFY AUTHORITY

AUTH-020  UNKNOWN/GAP != AUTHORIZED

AUTH-021  LOCAL FINALITY != GLOBAL FINALITY

AUTH-022  REVOCATION INVALIDATES DEPENDENT AUTHORITY

AUTH-023  STATE CHANGE MAY INVALIDATE AUTHORIZATION

AUTH-024  CONFIDENCE != AUTHORITY

AUTH-025  GOVERNANCE OVERRIDES CONVENIENCE
```

______________________________________________________________________

## 78. Minimum Authority Contract

Every consequential authority object should eventually define:

| Field          | Requirement                             |
| -------------- | --------------------------------------- |
| Identity       | Who/what holds authority                |
| Authority type | Read/propose/review/approve/commit/etc. |
| Action         | Authorized operation                    |
| Resource       | Target                                  |
| Scope          | Applicability envelope                  |
| Policy         | Governing rule                          |
| Provenance     | Source/lineage                          |
| State          | Relevant authoritative state            |
| Regime         | Operating regime                        |
| Time           | Validity period                         |
| Dependencies   | Required predicates                     |
| Delegation     | Delegation lineage if applicable        |
| Revocation     | Revocation conditions/status            |
| Conflict       | Competing authority claims              |
| Audit          | Traceability                            |
| Recovery       | Failure/revocation handling             |

______________________________________________________________________

## 79. Authority Test Families

Expected test families include:

```text
CAPABILITY/AUTHORITY SEPARATION TESTS

IDENTITY/AUTHORITY TESTS

ROLE/AUTHORITY TESTS

TOOL/PERMISSION TESTS

PROPOSAL/COMMIT TESTS

AUTHENTICATION/AUTHORIZATION TESTS

SCOPE BOUNDARY TESTS

TEMPORAL EXPIRY TESTS

REGIME TRANSITION TESTS

DELEGATION TESTS

DELEGATION AMPLIFICATION TESTS

REVOCATION TESTS

REVOCATION PROPAGATION TESTS

POLICY CONFLICT TESTS

STATE VERSION TESTS

CAS CONFLICT TESTS

MULTI-AUTHORITY ATOMICITY TESTS

SELF-AUTHORIZATION TESTS

CONTROL-PLANE BYPASS TESTS

RUNTIME BYPASS TESTS

EMERGENCY AUTHORITY TESTS

PROVENANCE TESTS

AUDIT RECONSTRUCTION TESTS

FAILURE LOCALITY TESTS

RECOVERY TESTS
```

______________________________________________________________________

## 80. Adversarial Tests

High-value adversarial cases:

```text
AGENT HAS TOOL ACCESS BUT NO AUTHORITY

MODEL CLAIMS 99.9% CONFIDENCE AND REQUESTS COMMIT

EXPIRED APPROVAL REUSED

REVOKED AUTHORITY REMAINS CACHED

DELEGATE GRANTS MORE AUTHORITY THAN RECEIVED

WORKFLOW STEP ASSUMES AUTHORITY FROM POSITION

RUNTIME EXECUTES WITHOUT CONTROL-PLANE APPROVAL

STATE CHANGES BETWEEN APPROVAL AND COMMIT

TEN COPIES OF ONE AUTHORITY GRANT TREATED AS TEN APPROVALS

UNKNOWN AUTHORITY TREATED AS ALLOW

EMERGENCY MODE CREATES UNLIMITED PERMISSION

READ ACCESS USED AS DISCLOSURE AUTHORITY

PRIOR REGIME AUTHORITY REUSED AFTER REGIME CHANGE

LOCAL APPROVAL TREATED AS GLOBAL APPROVAL
```

______________________________________________________________________

## 81. Implementation Firewall

This canon does **not** by itself establish implementation of:

```text
COMPLETE RBAC

COMPLETE ABAC

CAPABILITY SECURITY

CRYPTOGRAPHIC AUTHORITY PROOFS

AUTOMATED DELEGATION GRAPH VALIDATION

AUTOMATED REVOCATION PROPAGATION

DISTRIBUTED AUTHORITY CONSENSUS

FORMAL ACCESS-CONTROL VERIFICATION

MVCC AUTHORITY TRANSACTIONS

CAS-BASED AUTHORITY COMMIT

CAUSAL EPOCH AUTHORIZATION

AUTOMATED BREAK-GLASS GOVERNANCE

HARDWARE ROOT OF TRUST

ZERO-TRUST IMPLEMENTATION

FORMAL POLICY PROOF
```

These require separate implementation evidence.

______________________________________________________________________

## 82. Promotion Gate

Promotion:

```text
ACTIVE_CANON_CANDIDATE
→
ACTIVE_CANON
```

requires binding to authoritative AMOS sources covering at minimum:

```text
AMOS CORE LAWS

LAW HIERARCHY

INVARIANT REGISTRY

CONTROL PLANE

AUTHORITY MODEL

STATE MODEL

PROVENANCE MODEL

SECURITY MODEL

RUNTIME COMMIT CONTRACT

MVCC/CAS SEMANTICS

REVOCATION

RECOVERY

OBSERVABILITY

TEST EVIDENCE
```

Unresolved semantics remain:

```text
UNKNOWN/GAP
```

______________________________________________________________________

## 83. RSCF Node

```yaml
node_id: AMOS_AUTHORITY_CANON

functional_type:
  - AUTHORITY_MODEL
  - GOVERNANCE_MODEL
  - DECISION_RIGHTS_MODEL
  - COMMIT_CONTROL_MODEL

lifecycle_stage:
  CANON_CANDIDATE

origin_architect:
  Trang Phan

steward:
  Trang Phan

amos_core_target:
  v4.4

claim_class:
  AMOS_MODEL

claim: >
  AMOS authority is a local, typed, scoped, provenance-aware,
  regime-aware, freshness-bounded governance relation defining
  which identity may authorize which action over which resource
  under which policy, state, and conditions.

critical_invariants:
  - CAPABILITY != AUTHORITY
  - TOOL != PERMISSION
  - MODEL != AUTHORITY
  - AGENT != AUTHORITY
  - PROPOSAL != COMMIT
  - AUTHENTICATED != AUTHORIZED
  - EXECUTION SUCCESS != AUTHORIZATION
  - DELEGATION MUST NOT AMPLIFY AUTHORITY
  - UNKNOWN/GAP != AUTHORIZED
  - LOCAL FINALITY != GLOBAL FINALITY

known_gaps:
  - Exact production authority schema requires repository binding.
  - Exact law precedence requires binding to LAW_HIERARCHY.
  - Exact MVCC/CAS authority semantics require runtime evidence.
  - Exact emergency/break-glass semantics require governance sources.
  - Formal authority guarantees require implementation and verification evidence.

does_not_establish:
  - implementation completeness
  - universal permission model
  - unrestricted autonomous authority
  - formal security proof
  - formal distributed consensus
```

______________________________________________________________________

## 84. Changelog

## v2.0.0 — 2026-08-25

Expanded placeholder into an AMOS Core v4.4-aligned Authority Canon candidate.

Added:

- capability/authority firewall;
- authority envelope;
- authority classes;
- proposal/decision/commit separation;
- agent, skill, workflow, model, tool boundaries;
- scoped and regime-aware authority;
- delegation and non-amplification;
- authority provenance and lineage;
- state-version binding;
- MVCC/CAS alignment;
- competing authority handling;
- revocation and propagation;
- separation of duties;
- self-authorization firewall;
- emergency/break-glass model;
- failure locality and recovery;
- causal epoch alignment;
- local finality;
- proof-based coordination avoidance;
- observability and audit;
- authority tests;
- adversarial validation cases;
- implementation firewall;
- canon promotion gate.

## v1.0.0 — 2026-08-25

Initial placeholder reserved the canonical AMOS OS authority location.

______________________________________________________________________

## 85. Canonical Summary

```text
AUTHORITY
=
IDENTITY
+
DECISION RIGHT
+
ACTION
+
RESOURCE
+
POLICY
+
SCOPE
+
STATE
+
REGIME
+
TIME
+
PROVENANCE
```

subject to:

```text
CANON
KERNEL INVARIANTS
CONTROL-PLANE GOVERNANCE
SECURITY
REVOCATION
DEPENDENCY VALIDITY
```

Canonical execution path:

```text
CAPABILITY
↓
REQUEST
↓
PROPOSAL
↓
POLICY
↓
AUTHORITY
↓
STATE VALIDATION
↓
COMMIT ELIGIBILITY
↓
COMMIT
↓
RUNTIME
↓
EXECUTION
↓
OBSERVATION
↓
AUDIT
```

Core laws:

```text
CAPABILITY != AUTHORITY

IDENTITY != AUTHORITY

ROLE != AUTHORITY

ACCESS != AUTHORITY

TOOL != PERMISSION

MODEL != AUTHORITY

AGENT != AUTHORITY

WORKFLOW != AUTHORITY

PLAN != AUTHORIZATION

PROPOSAL != COMMIT

AUTHENTICATED != AUTHORIZED

EXECUTION SUCCESS != AUTHORIZATION

REMEMBERED AUTHORITY != CURRENT AUTHORITY

DELEGATION MUST NOT AMPLIFY AUTHORITY

UNKNOWN/GAP != AUTHORIZED

LOCAL FINALITY != GLOBAL FINALITY
```

Canonical objective:

```text
ALLOW CAPABILITY
WITHOUT SILENTLY CREATING AUTHORITY.

ALLOW REASONING
WITHOUT CREATING DECISION RIGHTS.

ALLOW PROPOSALS
WITHOUT CREATING COMMIT RIGHTS.

ALLOW TOOLS
WITHOUT CREATING PERMISSION.

ALLOW DELEGATION
WITHOUT AUTHORITY AMPLIFICATION.

ALLOW LOCAL DECISIONS
WITHOUT FALSE GLOBAL AUTHORITY.

PRESERVE SCOPE.
PRESERVE STATE.
PRESERVE REGIME.
PRESERVE PROVENANCE.
PRESERVE REVOCABILITY.

WHEN AUTHORITY IS UNKNOWN,
DO NOT INVENT IT.
```

______________________________________________________________________

**Related:** README|AMOS OS · [[00_ROOT/ARCHITECTURE|ARCHITECTURE]]|Architecture · [[00_ROOT/SYSTEM_MAP|SYSTEM_MAP]]|System Map · [[00_ROOT/PLACEMENT_RULES|PLACEMENT_RULES]]|Placement Rules · [[01_CANON/00_INDEX/CANON_MAP|CANON_MAP]]|Canon Map · [[01_CANON/01_CORE_LAWS/AMOS_CORE_LAWS|AMOS Core Laws]] · [[01_CANON/01_CORE_LAWS/INVARIANT_REGISTRY|INVARIANT_REGISTRY]]|Invariant Registry · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]|Law Hierarchy · [[01_CANON/02_UNIVERSE_CANON/PERSISTENCE_CANON|PERSISTENCE_CANON]]|Persistence Canon · [[01_CANON/03_COGNITION_CANON/COGNITION_CANON|COGNITION_CANON]]|Cognition Canon · [[01_CANON/03_COGNITION_CANON/FULL_BRAIN_OS_CANON|FULL_BRAIN_OS_CANON]]|Full Brain OS Canon · [[02_KERNEL/00_INDEX/KERNEL_MAP|KERNEL_MAP]]|Kernel Map · [[03_CONTROL_PLANE/00_INDEX/CONTROL_PLANE_MAP|CONTROL_PLANE_MAP]]|Control Plane Map · [[04_RUNTIME/00_INDEX/RUNTIME_MAP|RUNTIME_MAP]]|Runtime Map · [[06_AGENTS/00_INDEX/AGENT_MAP|AGENT_MAP]]|Agent Map · [[08_WORKFLOWS/00_INDEX/WORKFLOW_MAP|WORKFLOW_MAP]]|Workflow Map · [[09_PROTOCOLS/00_INDEX/PROTOCOL_MAP|PROTOCOL_MAP]]|Protocol Map · [[12_STATE/00_INDEX/STATE_STATE_MAP|STATE_STATE_MAP]]|State Map · [[14_TOOLS/00_INDEX/TOOL_MAP|TOOL_MAP]]|Tool Map · [[16_SCHEMAS/00_INDEX/SCHEMA_MAP|SCHEMA_MAP]]|Schema Map · [[17_OBSERVABILITY/00_INDEX/OBSERVABILITY_OBSERVABILITY_MAP|OBSERVABILITY_OBSERVABILITY_MAP]]|Observability Map · [[18_SECURITY/00_INDEX/SECURITY_MAP|SECURITY_MAP]]|Security Map · [[19_TESTS/00_INDEX/TEST_MAP|TEST_MAP]]|Test Map · [[20_OPERATIONS/00_INDEX/OPERATIONS_MAP|OPERATIONS_MAP]]|Operations Map · [[23_OPERATING_MODEL/00_INDEX/OPERATING_MODEL|OPERATING_MODEL]]|Operating Model

______________________________________________________________________

[[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]|[[00_ROOT/AMOS MOC|AMOS MOC]]

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

______________________________________________________________________

RSCF-NODE
node_id: authority_canon
node_type: note
path: 01_CANON/04_INFRASTRUCTURE_CANON/AUTHORITY_CANON.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
  claim_class: AMOS_MODEL

______________________________________________________________________

**MOC:** [[01_CANON/04_INFRASTRUCTURE_CANON/04_INFRASTRUCTURE_CANON_MOC|04_INFRASTRUCTURE_CANON_MOC]]
