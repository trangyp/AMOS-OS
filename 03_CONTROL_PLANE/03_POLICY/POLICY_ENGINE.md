---
canon-group: meta
canon-type: framework
rscf-state: source-claim
topic: Policy Engine
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---

# AMOS Policy Engine

## 0. Status

`POLICY_ENGINE.md` defines the AMOS OS architecture for discovering, resolving, evaluating, composing, revalidating, and auditing policies that govern requested operations.

The Policy Engine converts:

```text
TASK
+ PRINCIPAL
+ REQUESTED ACTION
+ TARGET
+ CAPABILITY
+ EFFECT INTENT
+ CONTEXT
+ POLICY REGISTRY
+ AUTHORITY CONTEXT
+ CONSTRAINT CONTEXT
+ EVIDENCE
```

into a governed:

```text
POLICY_DECISION
```

The Policy Engine is an evaluation and governance component.

It is **not** itself:

```text
a capability provider;
a domain worker;
a universal authority;
an effect executor;
a durable commit mechanism;
a release ledger;
a receiver;
an empirical truth engine;
or proof that an action succeeded.
```

The governing distinctions are:

```text
POLICY_ENGINE != POLICY_REGISTRY

POLICY_ENGINE != POLICY

POLICY_ENGINE != POLICY_DECISION

POLICY_ENGINE != CAPABILITY

POLICY_ENGINE != AUTHORITY

POLICY_ENGINE != EXECUTION

POLICY_ENGINE != COMMIT

POLICY_ALLOW != AUTHORITY

POLICY_ALLOW != COMMITTABLE

POLICY_ALLOW != COMMITTED

CAPABILITY != AUTHORITY

VALIDATION != AUTHORIZATION

PROPOSAL != COMMIT

UNKNOWN/GAP != PASS

UNKNOWN/GAP != ALLOW

CONFLICT != ALLOW

PLACEHOLDER != IMPLEMENTED

STRUCTURAL_MODEL != EXECUTABLE_RUNTIME
```

______________________________________________________________________

## 1. Purpose

The purpose of the AMOS Policy Engine is to provide a deterministic-governed interface for answering:

> Which policies govern this requested operation, what do those policies conclude under the current context, and what policy-local requirements must be satisfied before downstream execution may even be considered?

The Policy Engine exists to prevent downstream components from inventing permission from:

- capability availability;
- model confidence;
- agent intent;
- previous successful actions;
- stale decisions;
- absence of explicit denial;
- undocumented conventions;
- provider availability;
- workflow momentum;
- user convenience;
- or technical executability.

Every consequential operation SHOULD pass through explicit policy evaluation when policy governance is required.

______________________________________________________________________

## 2. Architectural Position

Canonical conceptual path:

```text
USER / SYSTEM INTENT
        ↓
TASK_CONTRACT
        ↓
CAPABILITY RESOLUTION
        ↓
RESOLVED_CAPABILITY_CONTRACT
        ↓
POLICY_ENGINE
        ↓
POLICY_DECISION
        ↓
CONTROL PLANE
        ↓
AUTHORITY VALIDATION
        ↓
CONSTRAINT / EVIDENCE / TRANSACTION VALIDATION
        ↓
OBSERVABILITY VALIDATION
        ↓
COMMIT-TIME REVALIDATION
        ↓
EFFECT RELEASE
```

The Policy Engine sits between capability resolution and final control-plane authorization.

______________________________________________________________________

## 3. Core Responsibility

The Policy Engine owns:

```text
policy discovery;
policy identity resolution;
policy version resolution;
policy applicability;
policy predicate evaluation;
policy rule evaluation;
policy composition;
policy conflict detection;
policy precedence evaluation;
policy exception evaluation;
policy obligation extraction;
policy prohibition extraction;
policy condition extraction;
policy-decision generation;
policy-decision provenance;
policy-decision freshness;
policy-decision invalidation;
policy-decision revalidation;
policy evaluation auditability.
```

It does NOT own:

```text
technical capability execution;
domain-specific evidence production;
external side-effect dispatch;
authority issuance;
authority revocation;
transaction commit;
release-ledger finality;
receiver receipt issuance;
physical-world outcome validation.
```

______________________________________________________________________

## 4. Core Architecture

```text
                    ┌───────────────────────┐
                    │      TASK_CONTRACT    │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │ CAPABILITY RESOLUTION │
                    └───────────┬───────────┘
                                │
                                ▼
              ┌─────────────────────────────────┐
              │         POLICY ENGINE           │
              │                                 │
              │  1. Context Normalizer          │
              │  2. Policy Discovery            │
              │  3. Identity Resolver           │
              │  4. Applicability Resolver      │
              │  5. Predicate Evaluator         │
              │  6. Rule Evaluator              │
              │  7. Exception Resolver          │
              │  8. Conflict Detector           │
              │  9. Precedence Resolver         │
              │ 10. Composition Engine          │
              │ 11. Provenance Binder           │
              │ 12. Freshness Binder            │
              │ 13. Decision Validator          │
              └────────────────┬────────────────┘
                               │
                               ▼
                    ┌───────────────────────┐
                    │    POLICY_DECISION    │
                    └───────────┬───────────┘
                                │
                                ▼
                    ┌───────────────────────┐
                    │     CONTROL PLANE     │
                    └───────────────────────┘
```

______________________________________________________________________

## 5. Policy Engine Input

Canonical input:

```yaml
policy_engine_request:
  request_id: string

  task:
    task_id: string
    intent: string
    task_class: string

  principal:
    principal_id: string
    principal_type: string
    acting_as: null
    delegation_chain: []

  action:
    action_id: string
    action_class: string
    operation: string
    parameters: {}
    parameters_hash: null

  capability:
    capability_id: null
    capability_version: null
    provider_id: null
    resolved_contract_hash: null

  target:
    target_id: null
    resource_ids: []
    resource_class: null

  effect_intent:
    effect_id: null
    effect_type: null
    effect_class: null
    payload_digest: null
    persistent: null
    externally_visible: null
    reversible: null

  context:
    environment: null
    domain: null
    jurisdiction: null
    scope: {}
    regime: {}
    time: null

  authority_context:
    authority_id: null
    witness_refs: []

  constraint_context:
    refs: []

  evidence:
    refs: []

  transaction:
    transaction_id: null

  requested_at: timestamp
```

______________________________________________________________________

## 6. Policy Engine Output

The Policy Engine MUST emit a structured `POLICY_DECISION`.

```yaml
policy_engine_response:
  request_id: string

  evaluation_id: string

  decision:
    decision_id: string

    state:
      - ALLOW
      - DENY
      - CONDITIONAL
      - ESCALATE
      - REVALIDATE
      - CONFLICT
      - UNKNOWN_GAP

    reason_codes: []

  policies:
    discovered: []
    applicable: []
    non_applicable: []
    unresolved: []

  evaluations: []

  obligations: []
  prohibitions: []
  conditions: []

  conflicts: []

  scope: {}
  regime: {}

  freshness: {}

  provenance: {}

  uncertainty: {}

  confidence_ceiling: null
```

______________________________________________________________________

## 7. Policy Registry Dependency

The Policy Engine MUST NOT invent governing policies.

Policies SHOULD be resolved through the governed policy registry.

Conceptually:

```text
POLICY_REGISTRY
      ↓
candidate policy identities
      ↓
POLICY_ENGINE
```

The registry establishes:

```text
policy identity;
version;
status;
scope;
supersession;
dependency;
source/canon lineage;
governance status.
```

The engine evaluates those policies.

______________________________________________________________________

## 8. Registry/Engine Separation

```text
POLICY_REGISTRY:
"What policies exist?"

POLICY_ENGINE:
"Which policies apply and what do they conclude?"

POLICY_DECISION:
"What was the resulting policy conclusion?"
```

These surfaces MUST remain separate.

______________________________________________________________________

## 9. Capability Dependency

The Policy Engine MAY consume a `RESOLVED_CAPABILITY_CONTRACT`.

This allows policy to evaluate the actual resolved operation rather than a vague capability name.

Example:

```yaml
capability_binding:
  capability_id: "CAP_WRITE_RESOURCE"
  capability_version: "2.1.0"
  provider_id: "PROVIDER_X"
  resolved_contract_hash: "sha256:*"
```

Policy evaluation SHOULD bind to the resolved contract where provider or effect characteristics are policy-sensitive.

______________________________________________________________________

## 10. Capability Boundary

A resolved capability means:

```text
the system knows how the operation could potentially be performed
```

It does NOT mean:

```text
policy permits the operation
```

Therefore:

```text
CapabilityResolved(C)
↛
PolicyAllow(C)
```

______________________________________________________________________

## 11. Context Normalization

The first engine stage SHOULD normalize incoming context.

Conceptually:

```text
RAW REQUEST
    ↓
NORMALIZE
    ↓
POLICY_CONTEXT
```

The normalized context SHOULD include:

```yaml
policy_context:
  principal: {}
  action: {}
  capability: {}
  target: {}
  effect: {}
  environment: {}
  scope: {}
  regime: {}
  time: {}
  authority: {}
  constraints: {}
  evidence: {}
  transaction: {}
```

______________________________________________________________________

## 12. Normalization Invariant

Normalization MUST NOT silently alter the semantic action.

For example:

```text
"send this email"
```

may normalize to:

```text
action_class = COMMUNICATE
operation = SEND_EMAIL
effect_class = EXTERNAL_COMMUNICATION
```

but MUST NOT normalize to:

```text
READ_ONLY
```

to avoid stricter policy.

______________________________________________________________________

## 13. Policy Discovery

The discovery stage identifies potentially governing policies.

```text
DISCOVER_POLICIES(context)
→ CandidatePolicySet
```

Discovery SHOULD consider:

```text
principal;
action;
operation;
capability;
provider;
target;
resource class;
domain;
environment;
jurisdiction;
effect class;
scope;
regime;
time.
```

______________________________________________________________________

## 14. Discovery Rule

The engine SHOULD prefer a superset of potentially applicable policies over prematurely excluding a governing policy.

However, discovery MUST remain bounded.

Unrelated policy families SHOULD NOT be loaded when they cannot materially affect the decision.

This preserves the AMOS smallest-sufficient-proof principle.

______________________________________________________________________

## 15. Policy Identity Resolution

Every discovered policy MUST resolve to a stable identity.

Recommended identity:

```yaml
policy_identity:
  policy_id: string
  version: string
  content_hash: string
  registry_id: string

  status:
    - ACTIVE
    - DRAFT
    - DEPRECATED
    - SUPERSEDED
    - REVOKED
    - QUARANTINED

  source_refs: []
  supersedes: []
  superseded_by: []
```

______________________________________________________________________

## 16. Identity Invariant

The engine MUST NOT evaluate two materially different policy contents as the same policy version.

Where authoritative state can change independently of scalar version:

```text
policy_id
+ version
+ content_hash
```

SHOULD be used.

______________________________________________________________________

## 17. Policy Status Gate

Policy status affects admissibility.

Conceptually:

```text
ACTIVE
→ eligible for applicability evaluation

DRAFT
→ not governing unless explicitly authorized

SUPERSEDED
→ historical unless supersession rules require inspection

REVOKED
→ not current governing authority

QUARANTINED
→ blocked pending integrity review
```

______________________________________________________________________

## 18. Applicability Engine

For each candidate policy:

```text
RESOLVE_APPLICABILITY(policy, context)
→ applicability
```

Possible states:

```text
APPLICABLE
NOT_APPLICABLE
CONDITIONAL
UNKNOWN_GAP
```

______________________________________________________________________

## 19. Applicability Dimensions

Applicability MAY depend on:

```text
principal;
principal class;
delegation;
action;
operation;
capability;
provider;
target;
resource;
domain;
environment;
jurisdiction;
effect class;
consequence class;
scope;
regime;
time;
authority state.
```

______________________________________________________________________

## 20. Applicability Object

```yaml
policy_applicability:
  policy_id: string
  version: string

  result:
    - APPLICABLE
    - NOT_APPLICABLE
    - CONDITIONAL
    - UNKNOWN_GAP

  dimensions:
    principal: null
    action: null
    capability: null
    target: null
    environment: null
    jurisdiction: null
    effect: null
    scope: null
    regime: null
    temporal: null

  matched: []
  failed: []
  unresolved: []

  evidence_refs: []
```

______________________________________________________________________

## 21. Unknown Applicability

If a potentially governing policy has unresolved applicability and could change the final decision:

```text
OutcomeSensitive(policy) = true
```

then the engine MUST NOT silently discard it.

The result SHOULD become:

```text
UNKNOWN_GAP
```

or:

```text
ESCALATE
```

depending on policy.

______________________________________________________________________

## 22. Predicate Engine

Policies frequently depend on predicates.

Examples:

```text
PrincipalIsAuthorizedClass
ResourceIsSensitive
EnvironmentIsProduction
EffectIsPersistent
HumanApprovalExists
TargetBelongsToTenant
ExceptionIsValid
PolicyIsFresh
```

Each predicate SHOULD resolve to:

```text
TRUE
FALSE
UNKNOWN
CONFLICT
```

______________________________________________________________________

## 23. Predicate Object

```yaml
predicate_result:
  predicate_id: string

  value:
    - TRUE
    - FALSE
    - UNKNOWN
    - CONFLICT

  evidence_refs: []

  provenance: []

  evaluated_at: timestamp

  confidence_ceiling: null
```

______________________________________________________________________

## 24. Predicate Invariant

Missing evidence MUST NOT be coerced to whichever value enables execution.

Therefore:

```text
UNKNOWN != FALSE
UNKNOWN != TRUE
```

unless the governing policy explicitly defines a fail-closed or fail-open semantic.

For consequential actions, fail-closed SHOULD generally be preferred where policy requires certainty.

______________________________________________________________________

## 25. Rule Engine

Each applicable policy contains one or more policy rules.

Conceptually:

```text
Rule =
Conditions
→
Decision
+ Obligations
+ Prohibitions
+ Requirements
```

Example:

```yaml
rule:
  rule_id: "RULE_PERSISTENT_WRITE_001"

  when:
    effect_class: E3_PERSISTENT_WRITE

  require:
    - valid_authority
    - commit_revalidation

  result:
    if_satisfied: ALLOW
    if_unsatisfied: DENY
    if_unknown: ESCALATE
```

______________________________________________________________________

## 26. Rule Evaluation

```text
EVALUATE_RULE(rule, context, predicates)
→ RuleEvaluation
```

Recommended output:

```yaml
rule_evaluation:
  policy_id: string
  rule_id: string

  result:
    - ALLOW
    - DENY
    - CONDITIONAL
    - ESCALATE
    - NOT_APPLICABLE
    - UNKNOWN_GAP

  matched_predicates: []
  failed_predicates: []
  unresolved_predicates: []

  obligations: []
  prohibitions: []
  conditions: []

  evidence_refs: []
```

______________________________________________________________________

## 27. Rule Determinism

Where policy semantics are declared deterministic:

```text
same validated inputs
+ same policy versions
+ same evaluation semantics
→ same policy result
```

This does NOT mean the entire AMOS system is globally deterministic.

External evidence, mutable state, model workers, time, and authority may change between evaluations.

______________________________________________________________________

## 28. Policy Exception Engine

Exceptions MUST be explicit.

```text
EVALUATE_EXCEPTION(exception, context)
→ ExceptionResult
```

An exception SHOULD include:

```yaml
policy_exception:
  exception_id: string

  policy_id: string
  rule_id: null

  principal_scope: []
  action_scope: []
  resource_scope: []

  valid_from: null
  valid_until: null

  issuer: null
  authority_ref: null

  conditions: []

  revoked: false

  provenance: []
```

______________________________________________________________________

## 29. Exception Validation

The engine MUST validate:

```text
identity;
issuer;
authority;
scope;
target;
action;
time;
conditions;
revocation;
provenance.
```

An exception outside any one required boundary is invalid.

______________________________________________________________________

## 30. Exception Narrowness

An exception MUST NOT broaden itself.

Conceptually:

```text
AppliedExceptionScope
⊆
DeclaredExceptionScope
⊆
AuthorizedExceptionScope
```

______________________________________________________________________

## 31. Revocation

Revoked exceptions MUST NOT remain active because of cached policy decisions.

If:

```text
Exception.revoked = true
```

then dependent decisions SHOULD be invalidated.

______________________________________________________________________

## 32. Policy Composition Engine

After individual rules are evaluated:

```text
COMPOSE({
    PolicyEvaluation1,
    PolicyEvaluation2,
    ...
})
→ CompositePolicyDecision
```

Composition MUST preserve incompatible results until valid resolution exists.

______________________________________________________________________

## 33. Composition Inputs

Composition SHOULD consider:

```text
policy precedence;
policy status;
policy scope;
specificity;
jurisdiction;
supersession;
exception relationships;
hard/soft classification;
temporal validity;
explicit override rules.
```

______________________________________________________________________

## 34. Hard Deny

Where a governing policy defines a hard prohibition:

```text
HardDeny = true
```

the engine MUST NOT override it merely because other policies return `ALLOW`.

An override requires explicit policy and authority basis.

______________________________________________________________________

## 35. Conditional Composition

Example:

```text
P1 → ALLOW
P2 → CONDITIONAL(A)
P3 → CONDITIONAL(B)
```

may compose to:

```text
CONDITIONAL(A ∧ B)
```

subject to governing precedence semantics.

______________________________________________________________________

## 36. Unknown Composition

If:

```text
P1 → ALLOW
P2 → UNKNOWN_GAP
```

and `P2` could contain a governing prohibition:

```text
Final != ALLOW
```

The appropriate result is:

```text
UNKNOWN_GAP
```

or:

```text
ESCALATE
```

______________________________________________________________________

## 37. Conflict Engine

The engine MUST detect policy conflicts.

Conflict classes MAY include:

```text
ALLOW_DENY
REQUIRE_PROHIBIT
SCOPE_CONFLICT
JURISDICTION_CONFLICT
PRECEDENCE_CONFLICT
EXCEPTION_CONFLICT
TEMPORAL_CONFLICT
AUTHORITY_CONFLICT
```

______________________________________________________________________

## 38. Conflict Object

```yaml
policy_conflict:
  conflict_id: string

  policies: []

  rules: []

  conflict_type: string

  scope: {}
  regime: {}

  precedence_candidates: []

  resolution:
    state:
      - RESOLVED
      - UNRESOLVED

    basis: null

  evidence_refs: []
```

______________________________________________________________________

## 39. Conflict Preservation

If conflict cannot be validly resolved:

```text
FinalDecision = CONFLICT
```

The engine MUST NOT choose a preferred result merely to complete the workflow.

______________________________________________________________________

## 40. Precedence Engine

Precedence MUST come from explicit governance.

Potential bases:

```text
canon hierarchy;
law/regulation;
organizational authority;
policy hierarchy;
explicit supersession;
specific-over-general rule;
temporal supersession;
jurisdictional rule.
```

No policy outranks another merely because:

```text
it was loaded first;
it is newer;
it is more convenient;
it has a higher numeric ID;
an agent prefers it.
```

unless such ordering is explicitly canonical.

______________________________________________________________________

## 41. Precedence Object

```yaml
policy_precedence:
  higher_policy: string
  lower_policy: string

  basis: string

  scope: {}

  regime: {}

  evidence_refs: []

  authority_ref: null
```

______________________________________________________________________

## 42. Supersession Engine

Policy version evolution SHOULD preserve explicit lineage.

```text
P_v1
  ↓ superseded by
P_v2
  ↓ superseded by
P_v3
```

The engine SHOULD be able to determine the currently applicable version.

______________________________________________________________________

## 43. Supersession Invariant

Newer timestamp alone does not prove supersession.

Supersession SHOULD require explicit lineage or authoritative registry state.

______________________________________________________________________

## 44. Obligation Extraction

Policy evaluation MAY generate obligations.

Examples:

```text
record provenance;
request approval;
redact fields;
retain audit log;
encrypt output;
obtain receiver receipt;
revalidate at commit;
notify responsible authority.
```

These MUST survive into the `POLICY_DECISION`.

______________________________________________________________________

## 45. Prohibition Extraction

Prohibitions SHOULD be represented explicitly.

Example:

```yaml
prohibition:
  prohibition_id: string
  policy_id: string
  rule_id: string

  operation: string

  target_scope: {}

  hard: true
```

Prohibitions MUST NOT disappear into explanation text.

______________________________________________________________________

## 46. Condition Extraction

Conditions SHOULD identify exactly what must become true before conditional policy permission can become valid.

```yaml
condition:
  condition_id: string

  predicate: string

  required_value: true

  current_state:
    - SATISFIED
    - UNSATISFIED
    - UNKNOWN_GAP

  evidence_refs: []
```

______________________________________________________________________

## 47. Policy Decision Builder

The decision builder converts composed evaluation state into the canonical `POLICY_DECISION`.

```text
BUILD_DECISION(
    normalized_context,
    applicable_policies,
    evaluations,
    conflicts,
    obligations,
    prohibitions,
    conditions
)
→ POLICY_DECISION
```

______________________________________________________________________

## 48. Decision State Space

Canonical engine decision states:

```text
ALLOW
DENY
CONDITIONAL
ESCALATE
REVALIDATE
CONFLICT
UNKNOWN_GAP
```

Internal policy evaluations MAY additionally use:

```text
NOT_APPLICABLE
```

______________________________________________________________________

## 49. Decision Reason Codes

Recommended codes:

```text
ALLOW_POLICY_SATISFIED

DENY_EXPLICIT_PROHIBITION
DENY_PRINCIPAL_SCOPE
DENY_RESOURCE_SCOPE
DENY_EFFECT_CLASS
DENY_REGIME
DENY_JURISDICTION
DENY_REVOKED_EXCEPTION

CONDITIONAL_APPROVAL_REQUIRED
CONDITIONAL_AUTHORITY_REQUIRED
CONDITIONAL_REDACTION_REQUIRED
CONDITIONAL_COMMIT_REVALIDATION

ESCALATE_HIGH_CONSEQUENCE
ESCALATE_POLICY_AMBIGUITY
ESCALATE_CONFLICT
ESCALATE_AUTHORITY_INTERPRETATION

REVALIDATE_POLICY_CHANGED
REVALIDATE_SCOPE_CHANGED
REVALIDATE_REGIME_CHANGED
REVALIDATE_EFFECT_CHANGED
REVALIDATE_CAPABILITY_CHANGED

CONFLICT_ALLOW_DENY
CONFLICT_REQUIRE_PROHIBIT
CONFLICT_PRECEDENCE

UNKNOWN_POLICY
UNKNOWN_APPLICABILITY
UNKNOWN_SCOPE
UNKNOWN_REGIME
UNKNOWN_AUTHORITY
UNKNOWN_EVIDENCE
UNKNOWN_PRECEDENCE
```

______________________________________________________________________

## 50. Provenance Binder

Every consequential policy decision SHOULD preserve the exact decision-forming provenance.

```yaml
provenance:
  policy_engine:
    engine_id: string
    engine_version: string

  policy_refs: []
  policy_versions: {}
  policy_hashes: {}

  evidence_refs: []

  authority_refs: []

  constraint_refs: []

  source_ancestry: []

  evaluated_at: timestamp

  environment: null

  transaction_id: null
```

______________________________________________________________________

## 51. Policy Read Set

The engine SHOULD construct the exact set of policy resources used in decision formation.

```text
PolicyReadSet =
{
  (policy_object_id, version, content_hash)
}
```

Example:

```yaml
policy_read_set:
  - object_id: "POLICY_WRITE"
    version: "3.2.0"
    content_hash: "sha256:*"

  - object_id: "POLICY_PRIVACY"
    version: "1.7.0"
    content_hash: "sha256:*"
```

______________________________________________________________________

## 52. Fine-Grained Freshness

A global policy-registry version SHOULD NOT be the only freshness mechanism when precise read-set validation is available.

If:

```text
decision D read P1 and P2
```

and unrelated:

```text
P99 changes
```

then `D` need not be invalidated solely because `P99` changed.

______________________________________________________________________

## 53. Selective Invalidation

If:

```text
D1 depends on P1
D2 depends on P2
D3 depends on P1 + P3
```

and:

```text
P1 changes
```

then:

```text
invalidate D1
invalidate D3
preserve D2
```

subject to hidden dependency checks.

______________________________________________________________________

## 54. Freshness Binder

Each decision SHOULD contain:

```yaml
freshness:
  evaluated_at: timestamp

  valid_from: timestamp

  expires_at: null

  policy_read_set: []

  invalidation_events:
    - POLICY_CHANGE
    - POLICY_REVOCATION
    - EXCEPTION_REVOCATION
    - SCOPE_CHANGE
    - REGIME_CHANGE
    - PRINCIPAL_CHANGE
    - ACTION_CHANGE
    - TARGET_CHANGE
    - EFFECT_CHANGE
    - CAPABILITY_CONTRACT_CHANGE
```

______________________________________________________________________

## 55. Revalidation Engine

```text
REVALIDATE_POLICY_DECISION(
    prior_decision,
    current_state
)
→ current_decision
```

The engine SHOULD compare only load-bearing state where possible.

______________________________________________________________________

## 56. Revalidation Triggers

Mandatory revalidation MAY be triggered by:

```text
policy content change;
policy supersession;
policy revocation;
exception revocation;
principal change;
delegation change;
action change;
parameter change;
target change;
resource-state change where policy-sensitive;
scope change;
regime change;
jurisdiction change;
capability contract change;
effect digest change;
freshness expiry.
```

______________________________________________________________________

## 57. Commit-Time Policy Revalidation

For durable effects, the Policy Engine SHOULD support commit-time policy revalidation.

The control plane may ask:

```text
Does POLICY_DECISION D
still apply to EFFECT E
under CURRENT STATE?
```

The engine MUST NOT simply answer from cached preflight state when load-bearing state changed.

______________________________________________________________________

## 58. Commit-Time Binding

Consequential policy decisions SHOULD bind to:

```text
principal;
operation;
target;
parameters digest;
effect digest;
resolved capability contract;
policy read set;
scope;
regime;
transaction identity.
```

______________________________________________________________________

## 59. Policy/Authority Separation

The Policy Engine MAY consume authority context.

It MUST NOT manufacture authority.

```text
PolicyEngine
    ↓ evaluates
AuthorityContext
```

not:

```text
PolicyEngine
    ↓ creates
Authority
```

Authority issuance and verification belong to authority-governed infrastructure.

______________________________________________________________________

## 60. Policy/Control-Plane Separation

The Policy Engine answers:

```text
POLICY RESULT
```

The control plane answers:

```text
MAY THE SYSTEM RELEASE THIS EFFECT NOW?
```

These MUST remain separate.

______________________________________________________________________

## 61. Policy/Execution Separation

The Policy Engine MUST NOT dispatch side effects merely because:

```text
decision = ALLOW
```

Instead:

```text
ALLOW
  ↓
CONTROL PLANE
  ↓
AUTHORITY
  ↓
CONSTRAINTS
  ↓
TRANSACTION
  ↓
OBSERVABILITY
  ↓
RELEASE FINALITY
  ↓
DISPATCH
```

______________________________________________________________________

## 62. Policy/Truth Separation

Policy compliance does not establish truth.

An output can be:

```text
policy-compliant
```

and still be:

```text
factually wrong.
```

Likewise, a factually correct output may still violate policy.

Therefore:

```text
POLICY_VALIDITY != EPISTEMIC_VALIDITY
```

______________________________________________________________________

## 63. Policy/Domain Separation

The Policy Engine SHOULD remain domain-agnostic.

Domain Skills MAY expose policy-relevant typed evidence.

Example:

```text
DOMAIN SKILL
    ↓
typed evidence
    ↓
POLICY ENGINE
```

The infrastructure policy engine SHOULD NOT embed specialist domain logic when that logic properly belongs to a domain capability.

______________________________________________________________________

## 64. Policy Evaluation ABI

Domain or subsystem adapters SHOULD expose policy-relevant state through typed objects rather than unstructured prose where feasible.

Example:

```yaml
policy_fact:
  fact_id: string
  type: string
  value: any

  scope: {}
  regime: {}

  observed_at: timestamp

  provenance: []

  confidence_ceiling: null
```

______________________________________________________________________

## 65. Unknown Preservation

The engine MUST preserve:

```text
UNKNOWN
```

where evidence is unavailable.

It MUST NOT infer:

```text
not prohibited
```

from:

```text
prohibition not found
```

unless policy completeness for that scope has itself been established.

______________________________________________________________________

## 66. Closed-World vs Open-World Policy

The engine SHOULD explicitly distinguish policy lookup semantics.

## CLOSED_WORLD

```text
registry is authoritative and complete for declared scope
```

Only under such conditions MAY absence have stronger meaning.

## OPEN_WORLD

```text
additional governing policy may exist
```

Absence MUST remain epistemically weaker.

______________________________________________________________________

## 67. Policy Completeness State

```yaml
policy_coverage:
  scope: {}

  mode:
    - CLOSED_WORLD
    - OPEN_WORLD
    - UNKNOWN

  completeness:
    - COMPLETE
    - PARTIAL
    - UNKNOWN_GAP

  authority_ref: null
```

______________________________________________________________________

## 68. Coverage Invariant

If:

```text
coverage = UNKNOWN
```

and missing policy could materially change a consequential decision:

```text
FinalDecision != unconditional ALLOW
```

without additional governing justification.

______________________________________________________________________

## 69. H/M/L Policy Evaluation

Policy evaluation SHOULD support AMOS H/M/L structure.

```text
H = governing/system policy
M = subsystem/workflow policy
L = operation/resource policy
```

______________________________________________________________________

## 70. H-Level Policies

Examples:

```text
system safety;
constitutional governance;
organization-wide authority;
enterprise security;
canon governance;
high-consequence effect rules.
```

H-level constraints may constrain all lower levels.

______________________________________________________________________

## 71. M-Level Policies

Examples:

```text
workflow policy;
agent policy;
memory policy;
domain policy;
transaction policy;
data-handling policy.
```

______________________________________________________________________

## 72. L-Level Policies

Examples:

```text
specific resource access;
specific tool invocation;
specific message;
specific memory write;
specific effect.
```

______________________________________________________________________

## 73. Cross-Scale Composition

Where hierarchical tightening is defined:

```text
Allowed_L
⊆
Allowed_M
⊆
Allowed_H
```

A lower-level rule MUST NOT silently broaden a higher-level prohibition.

______________________________________________________________________

## 74. H/M/L Conflict

Example:

```text
H: DENY external disclosure

M: ALLOW workflow export

L: ALLOW send_message
```

The lower-level `ALLOW` states do not override the H-level prohibition unless a valid higher-level exception exists.

______________________________________________________________________

## 75. State Variables

Recommended Policy Engine state:

```text
Q     request
P     principal
A     action
C     capability
T     target
E     effect intent
CTX   normalized context

Πc    candidate policies
Πa    applicable policies
Πu    unresolved policies

Pred  predicate states
R     rule evaluations
Ex    exceptions
Cf    conflicts

Ω     obligations
X     prohibitions
K     conditions

S     scope
G     regime
F     freshness
Pr    provenance
U     uncertainty

D     final policy decision
```

______________________________________________________________________

## 76. Core Transition Function

Conceptually:

```text
D =
PolicyEngine(
    Q,
    P,
    A,
    C,
    T,
    E,
    CTX,
    Π,
    Pred,
    Ex
)
```

expanded:

```text
D =
Compose(
    Evaluate(
        Applicable(
            Discover(
                Normalize(Q)
            )
        )
    )
)
```

This is an AMOS MODEL abstraction, not an assertion of universal mathematics.

______________________________________________________________________

## 77. Engine Lifecycle

```text
RECEIVED
    ↓
NORMALIZED
    ↓
DISCOVERING
    ↓
RESOLVING
    ↓
EVALUATING
    ↓
COMPOSING
    ↓
VALIDATING
    ↓
RESOLVED
```

Possible alternate states:

```text
UNKNOWN_GAP
CONFLICT
ESCALATED
INVALIDATED
EXPIRED
QUARANTINED
SUPERSEDED
```

______________________________________________________________________

## 78. Engine State Object

```yaml
policy_engine_state:
  evaluation_id: string

  lifecycle_state: string

  request_hash: string

  candidate_policies: []

  applicable_policies: []

  completed_evaluations: []

  pending_evaluations: []

  conflicts: []

  gaps: []

  decision_id: null

  started_at: timestamp

  updated_at: timestamp
```

______________________________________________________________________

## 79. Atomic Evaluation Boundary

A policy decision SHOULD be constructed from one coherent evaluation snapshot.

The engine SHOULD avoid combining:

```text
policy state from epoch A
authority context from epoch B
target state from epoch C
effect intent from epoch D
```

without explicit compatibility validation.

______________________________________________________________________

## 80. Evaluation Epoch

Recommended representation:

```yaml
evaluation_epoch:
  epoch_id: string

  started_at: timestamp

  policy_registry_state: {}

  capability_contract_hash: null

  constraint_context_hash: null

  authority_context_ref: null
```

______________________________________________________________________

## 81. MVCC/CAS Analogy

Where mutable policy state exists, policy revalidation MAY use MVCC/CAS-style reasoning:

```text
READ policy state
      ↓
PREPARE decision
      ↓
CHECK load-bearing versions/hashes
      ↓
ACCEPT or REVALIDATE
```

This is a reasoning/control pattern.

It does not claim the conversational model literally implements distributed MVCC.

______________________________________________________________________

## 82. Policy Decision Cache

The engine MAY cache policy decisions.

Cache reuse MUST be conditional.

```yaml
decision_cache:
  decision_id: string

  decision_hash: string

  policy_read_set: []

  principal_hash: string
  action_hash: string
  target_hash: string
  effect_digest: null

  scope_hash: string
  regime_hash: string

  evaluated_at: timestamp
  expires_at: null
```

______________________________________________________________________

## 83. Cache Validity

Conceptually:

```text
CacheValid(D) =
PrincipalMatch
∧ ActionMatch
∧ TargetMatch
∧ EffectMatch
∧ PolicyReadSetFresh
∧ ScopeCompatible
∧ RegimeCompatible
∧ NotExpired
```

If any load-bearing term fails:

```text
REVALIDATE
```

______________________________________________________________________

## 84. Decision Hash

A deterministic binding MAY be:

```text
DecisionHash =
H(
  principal
  || action
  || target
  || capability_contract_hash
  || effect_digest
  || policy_read_set
  || scope
  || regime
  || decision_state
)
```

The exact canonical serialization and cryptographic algorithm belong to implementation specification.

______________________________________________________________________

## 85. Uncertainty

The engine SHOULD track uncertainty explicitly.

```yaml
uncertainty:
  policy_discovery: null
  policy_identity: null
  applicability: null
  interpretation: null
  evidence: null
  scope: null
  regime: null
  temporal: null
  authority: null
  provenance_independence: null
```

______________________________________________________________________

## 86. Confidence Ceiling

Conceptually:

```text
C_decision ≤ min(
    C_policy_discovery,
    C_policy_identity,
    C_applicability,
    C_predicates,
    C_scope,
    C_regime,
    C_freshness,
    C_composition
)
```

No fluent explanation may raise the decision above the weakest load-bearing premise.

______________________________________________________________________

## 87. Competing Interpretations

If policy language admits multiple materially different interpretations:

```text
Interpretation_A
Interpretation_B
```

and evidence cannot discriminate them:

```text
COMPETING
```

SHOULD be preserved internally.

The external policy result may become:

```text
CONFLICT
```

or:

```text
ESCALATE
```

depending on governance.

______________________________________________________________________

## 88. Cheapest Discriminating Test

When policy interpretations compete, the engine SHOULD prefer the cheapest high-information test that can distinguish them.

Examples:

```text
retrieve authoritative policy definition;
resolve supersession lineage;
check exception issuer;
verify target classification;
check current jurisdiction;
verify effect class.
```

Do not accumulate redundant evidence if one authoritative check can resolve the decision.

______________________________________________________________________

## 89. Adversarial Validation

For consequential policy decisions, validation SHOULD independently challenge the provisional result.

Questions include:

```text
Was a governing policy omitted?

Was a policy incorrectly marked non-applicable?

Was scope widened?

Was regime ignored?

Was an exception overextended?

Was an expired policy used?

Was a superseded policy used?

Was authority inferred from capability?

Was an UNKNOWN converted to ALLOW?

Was a hard deny overridden without authority?

Did the effect mutate after evaluation?

Are multiple policy sources actually one provenance lineage?

Did a lower-level policy weaken a higher-level constraint?
```

______________________________________________________________________

## 90. Sensitivity Analysis

For consequential decisions, identify the smallest premise capable of flipping the result.

Example:

```text
Decision = ALLOW
```

but:

```text
if resource_class = SENSITIVE
→ DENY
```

Then `resource_class` is decision-sensitive and SHOULD receive priority validation.

______________________________________________________________________

## 91. Policy Decision Fragility

A decision SHOULD be considered fragile when small plausible uncertainty in a load-bearing predicate changes the result.

Possible classification:

```text
ROBUST
CONDITIONAL
FRAGILE
UNKNOWN
```

______________________________________________________________________

## 92. Policy Engine Invariants

## INV-PE-001 — Registry Grounding

The engine MUST NOT invent governing policies.

## INV-PE-002 — Explicit Identity

Evaluated policies MUST have stable identity.

## INV-PE-003 — Version Binding

Material decisions MUST bind to policy version/hash.

## INV-PE-004 — Applicability Before Evaluation

Policy rules MUST NOT govern outside validated applicability.

## INV-PE-005 — Unknown Preservation

```text
UNKNOWN != ALLOW
```

## INV-PE-006 — Conflict Preservation

Unresolved conflict MUST remain visible.

## INV-PE-007 — No Capability Smuggling

```text
CAPABILITY != PERMISSION
```

## INV-PE-008 — No Authority Smuggling

```text
POLICY_ALLOW != AUTHORITY
```

## INV-PE-009 — No Commit Smuggling

```text
POLICY_ALLOW != COMMIT
```

## INV-PE-010 — Scope Preservation

Decisions MUST remain inside validated scope.

## INV-PE-011 — Regime Preservation

Decisions MUST remain inside validated regime.

## INV-PE-012 — Exception Narrowness

Exceptions MUST NOT exceed authorized scope.

## INV-PE-013 — Revocation Dominance

Revoked policy/exception authority MUST NOT survive stale cache.

## INV-PE-014 — Provenance Preservation

Material decisions MUST remain reconstructable.

## INV-PE-015 — Freshness Preservation

Stale decisions MUST NOT masquerade as current.

## INV-PE-016 — Effect Binding

Policy approval MUST bind to the evaluated effect where effect-sensitive.

## INV-PE-017 — Parameter Binding

Policy-sensitive parameter changes require revalidation.

## INV-PE-018 — H/M/L Integrity

Lower-level rules MUST NOT silently weaken higher-level governing constraints.

## INV-PE-019 — Selective Invalidation

Invalidate dependent conclusions, not unrelated valid state.

## INV-PE-020 — Proposal/Commit Separation

Permission to propose MUST NOT imply permission to commit.

______________________________________________________________________

## 93. Additional Integrity Invariants

## INV-PE-021 — No Policy-by-Absence

Failure to discover prohibition does not prove permission unless policy coverage is established.

## INV-PE-022 — No Temporal Leakage

Historical permission does not imply current permission.

## INV-PE-023 — No Jurisdiction Leakage

A decision from one jurisdiction does not automatically transfer to another.

## INV-PE-024 — No Provider Substitution

Provider changes require revalidation when provider identity is policy-sensitive.

## INV-PE-025 — No Decision Substitution

One decision ID MUST NOT be reused for a materially different request.

## INV-PE-026 — No Provenance Inflation

Multiple descendants of one source do not constitute independent authority.

## INV-PE-027 — No Silent Default

Missing policy semantics MUST NOT silently default to permissive behavior.

## INV-PE-028 — Explanation Consistency

Human-readable explanation MUST match structured decision state.

## INV-PE-029 — Control-Plane Boundary

The Policy Engine MUST NOT claim infrastructure commit authority.

## INV-PE-030 — Domain Boundary

The infrastructure Policy Engine MUST NOT absorb specialist domain logic without an explicit architectural reason.

______________________________________________________________________

## 94. Failure Modes

## FM-PE-001 — Policy Discovery Failure

A governing policy is not discovered.

## FM-PE-002 — Policy Identity Collision

Two different policies resolve to one identity.

## FM-PE-003 — Version Drift

Wrong policy version is evaluated.

## FM-PE-004 — Supersession Failure

A superseded policy remains active.

## FM-PE-005 — Applicability False Positive

A non-governing policy is applied.

## FM-PE-006 — Applicability False Negative

A governing policy is excluded.

## FM-PE-007 — Predicate Fabrication

Unknown predicate is invented.

## FM-PE-008 — Unknown-to-Allow Collapse

Missing evidence becomes permission.

## FM-PE-009 — Conflict Suppression

Conflicting policies are silently merged.

## FM-PE-010 — Precedence Fabrication

An unsupported hierarchy resolves conflict.

## FM-PE-011 — Exception Overreach

Exception exceeds its envelope.

## FM-PE-012 — Revoked Exception Reuse

Stale exception remains active.

## FM-PE-013 — Scope Leakage

Decision escapes validated scope.

## FM-PE-014 — Regime Leakage

Decision escapes validated regime.

## FM-PE-015 — Authority Smuggling

Policy result is treated as authority.

## FM-PE-016 — Capability Smuggling

Capability existence becomes permission.

## FM-PE-017 — Commit Smuggling

Policy allow becomes commit.

## FM-PE-018 — Stale Decision Reuse

Decision survives load-bearing policy change.

## FM-PE-019 — Parameter Mutation

Action changes after policy evaluation.

## FM-PE-020 — Effect Mutation

Effect changes after policy evaluation.

## FM-PE-021 — Provider Mutation

Provider changes without policy revalidation.

## FM-PE-022 — Policy Coverage Assumption

Incomplete registry is treated as complete.

## FM-PE-023 — Provenance Loss

Decision basis becomes unreconstructable.

## FM-PE-024 — Correlated Source Inflation

Dependent policy sources are counted as independent.

## FM-PE-025 — H/M/L Override Leak

Local rule weakens governing policy.

## FM-PE-026 — Cache Poisoning

Invalid decision enters cache.

## FM-PE-027 — Decision Replay

Decision is reused for another transaction.

## FM-PE-028 — Engine/Runtime Divergence

Runtime action violates policy result.

## FM-PE-029 — Policy/Effect Mismatch

Evaluated action differs from released effect.

## FM-PE-030 — Explanation/State Divergence

Explanation says allow while structured state denies or conditions.

______________________________________________________________________

## 95. Repair / Recovery

Canonical repair sequence:

```text
DETECT POLICY ENGINE FAILURE
        ↓
FREEZE AFFECTED DECISION
        ↓
PRESERVE REQUEST + POLICY STATE + EVIDENCE
        ↓
IDENTIFY EARLIEST FAILED DEPENDENCY
        ↓
INVALIDATE DEPENDENT RESULTS
        ↓
PRESERVE UNAFFECTED RESULTS
        ↓
REFRESH POLICY / CONTEXT / AUTHORITY
        ↓
RE-RUN APPLICABILITY
        ↓
RE-RUN AFFECTED RULES
        ↓
RE-COMPOSE
        ↓
REVALIDATE
        ↓
SUPERSEDE / RESTORE / DENY / ESCALATE
```

______________________________________________________________________

## 96. Earliest Failure Principle

Repair SHOULD target the earliest causal failure rather than the last visible error.

Example:

```text
wrong policy discovered
    ↓
wrong applicability
    ↓
wrong rule result
    ↓
wrong composition
    ↓
wrong ALLOW
```

The repair target is policy discovery, not merely the final `ALLOW`.

______________________________________________________________________

## 97. Rollback

If a bad policy decision has not produced an effect:

```text
invalidate decision
discard proposal
re-evaluate
```

If a reversible effect occurred:

```text
invoke authorized compensation where available
```

If an irreversible effect occurred:

```text
preserve evidence
record incident
contain consequences
revoke affected decision/cache
escalate
```

______________________________________________________________________

## 98. Quarantine

Policies, decisions, or evidence with integrity concerns SHOULD be quarantinable.

```yaml
quarantine:
  object_id: string

  object_type:
    - POLICY
    - POLICY_DECISION
    - EXCEPTION
    - EVIDENCE

  reason: string

  entered_at: timestamp

  evidence_refs: []

  release_conditions: []
```

Quarantine SHOULD preserve evidence rather than destroy it.

______________________________________________________________________

## 99. Tests / Validators

Minimum test suite:

```text
T-PE-001 request schema

T-PE-002 context normalization

T-PE-003 policy discovery

T-PE-004 policy identity

T-PE-005 version binding

T-PE-006 content-hash binding

T-PE-007 supersession resolution

T-PE-008 revoked-policy rejection

T-PE-009 applicability principal

T-PE-010 applicability action

T-PE-011 applicability capability

T-PE-012 applicability target

T-PE-013 applicability environment

T-PE-014 applicability jurisdiction

T-PE-015 applicability scope

T-PE-016 applicability regime

T-PE-017 temporal applicability

T-PE-018 unknown applicability

T-PE-019 predicate TRUE

T-PE-020 predicate FALSE

T-PE-021 predicate UNKNOWN

T-PE-022 predicate CONFLICT

T-PE-023 rule ALLOW

T-PE-024 rule DENY

T-PE-025 rule CONDITIONAL

T-PE-026 rule ESCALATE

T-PE-027 exception scope

T-PE-028 exception authority

T-PE-029 exception expiry

T-PE-030 exception revocation

T-PE-031 hard-deny composition

T-PE-032 conditional composition

T-PE-033 unknown composition

T-PE-034 conflict detection

T-PE-035 precedence resolution

T-PE-036 unresolved precedence

T-PE-037 obligation extraction

T-PE-038 prohibition extraction

T-PE-039 condition extraction

T-PE-040 policy decision generation

T-PE-041 policy read-set construction

T-PE-042 provenance reconstruction

T-PE-043 freshness expiry

T-PE-044 selective invalidation

T-PE-045 cache reuse

T-PE-046 stale-cache rejection

T-PE-047 principal mutation

T-PE-048 action mutation

T-PE-049 target mutation

T-PE-050 effect mutation

T-PE-051 capability-contract mutation

T-PE-052 provider substitution

T-PE-053 scope leakage

T-PE-054 regime leakage

T-PE-055 jurisdiction leakage

T-PE-056 capability/authority separation

T-PE-057 policy/authority separation

T-PE-058 policy/commit separation

T-PE-059 proposal/commit separation

T-PE-060 H/M/L precedence

T-PE-061 correlated provenance

T-PE-062 policy coverage OPEN_WORLD

T-PE-063 policy coverage CLOSED_WORLD

T-PE-064 explanation consistency

T-PE-065 control-plane handoff

T-PE-066 commit-time revalidation

T-PE-067 transaction binding

T-PE-068 replay resistance

T-PE-069 quarantine

T-PE-070 supersession audit
```

______________________________________________________________________

## 100. Adversarial Tests

Recommended adversarial cases:

```text
policy removed between preflight and commit;

policy changed without version increment;

policy version increments without content change;

exception revoked immediately before commit;

principal delegation expires;

provider changes after policy evaluation;

effect payload changes while operation name stays the same;

target alias resolves to a different resource;

jurisdiction changes;

development decision replayed in production;

three policy documents descend from one original source;

ALLOW cached before a new hard prohibition;

local policy attempts to weaken governing H policy;

missing policy registry shard interpreted as no prohibition;

fake exception with plausible identifier;

conflicting policies with no precedence;

policy explanation manipulated while structured decision remains DENY.
```

______________________________________________________________________

## 101. Validator Outcomes

Policy Engine validators SHOULD return explicit states.

```text
VALID

INVALID

REVALIDATE

CONFLICT

QUARANTINE

ESCALATE

UNKNOWN_GAP
```

Validation failure MUST NOT be converted into `ALLOW`.

______________________________________________________________________

## 102. Falsifiers

Claims that the Policy Engine produced a valid decision are falsified if reliable evidence shows:

```text
a governing policy was omitted;

wrong policy content was evaluated;

a superseded policy was treated as current;

an applicable policy was incorrectly excluded;

a hard prohibition was ignored;

an invalid exception was accepted;

an expired exception was accepted;

a revoked exception was accepted;

scope was widened;

regime was widened;

jurisdiction was crossed;

policy precedence was fabricated;

unknown evidence was converted to permission;

the effect changed after evaluation;

the principal changed;

the target changed;

the capability contract changed materially;

the decision was replayed outside its envelope;

the recorded provenance cannot reconstruct the result;

or runtime execution contradicted the policy decision.
```

______________________________________________________________________

## 103. Agents

The Policy Engine MAY use architectural agent roles such as:

```text
POLICY_DISCOVERY_AGENT

POLICY_IDENTITY_AGENT

POLICY_APPLICABILITY_AGENT

POLICY_RULE_EVALUATOR

POLICY_CONFLICT_AGENT

POLICY_PRECEDENCE_AUDITOR

POLICY_PROVENANCE_AUDITOR

POLICY_REVALIDATION_AGENT

POLICY_ADVERSARIAL_AUDITOR
```

These are functional roles.

They do NOT inherently possess:

```text
policy authority;
execution authority;
commit authority;
exception authority.
```

______________________________________________________________________

## 104. Agent Boundary

Agents may:

```text
retrieve;
classify;
evaluate;
propose;
challenge;
audit;
recommend.
```

Agents may not infer authority from their role.

```text
AGENT_ROLE != AUTHORITY
```

______________________________________________________________________

## 105. Skills

Relevant Skill categories MAY include:

```text
policy registry resolution;
law hierarchy resolution;
constraint propagation;
authority verification;
provenance validation;
scope/regime validation;
policy conflict resolution;
commit-time authorization;
information-boundary governance;
risk governance;
semantic transaction validation.
```

Skill availability does not establish implementation or authority.

______________________________________________________________________

## 106. Policy Engine Workflow

Canonical workflow:

```text
01 RECEIVE REQUEST

02 VALIDATE REQUEST STRUCTURE

03 NORMALIZE PRINCIPAL

04 NORMALIZE ACTION

05 RESOLVE TARGET

06 RESOLVE EFFECT INTENT

07 RESOLVE CAPABILITY CONTRACT

08 BUILD POLICY CONTEXT

09 DISCOVER POTENTIALLY GOVERNING POLICIES

10 RESOLVE POLICY IDENTITIES

11 RESOLVE POLICY VERSIONS

12 RESOLVE SUPERSESSION

13 FILTER INVALID / REVOKED POLICIES

14 RESOLVE APPLICABILITY

15 IDENTIFY DECISION-SENSITIVE PREDICATES

16 RETRIEVE MINIMUM REQUIRED EVIDENCE

17 EVALUATE PREDICATES

18 EVALUATE POLICY RULES

19 RESOLVE EXCEPTIONS

20 EXTRACT OBLIGATIONS

21 EXTRACT PROHIBITIONS

22 EXTRACT CONDITIONS

23 DETECT CONFLICTS

24 RESOLVE VALID PRECEDENCE

25 PRESERVE UNRESOLVED CONFLICTS

26 COMPOSE POLICY RESULT

27 BIND RESULT TO PRINCIPAL / ACTION / TARGET / EFFECT

28 BUILD POLICY READ SET

29 BIND PROVENANCE

30 BIND SCOPE / REGIME / FRESHNESS

31 RUN DECISION VALIDATOR

32 RUN ADVERSARIAL CHECK IF REQUIRED

33 EMIT POLICY_DECISION

34 HAND OFF TO CONTROL PLANE

35 REVALIDATE LOAD-BEARING STATE AT COMMIT IF REQUIRED

36 INVALIDATE OR SUPERSEDE STALE DECISIONS
```

______________________________________________________________________

## 107. Protocol — Evaluation Request

```yaml
policy_engine_evaluate:
  request_id: string

  task_contract_ref: string

  principal: {}

  action: {}

  capability_contract: {}

  target: {}

  effect_intent: {}

  scope: {}

  regime: {}

  authority_context: {}

  constraint_context: {}

  evidence_refs: []

  transaction_id: null
```

______________________________________________________________________

## 108. Protocol — Evaluation Response

```yaml
policy_engine_result:
  request_id: string

  evaluation_id: string

  policy_decision_ref: string

  state:
    - ALLOW
    - DENY
    - CONDITIONAL
    - ESCALATE
    - REVALIDATE
    - CONFLICT
    - UNKNOWN_GAP

  reason_codes: []

  obligations: []
  prohibitions: []
  conditions: []

  unresolved: []

  policy_read_set: []

  provenance: {}

  confidence_ceiling: null
```

______________________________________________________________________

## 109. Protocol — Revalidation

```yaml
policy_engine_revalidate:
  prior_decision_id: string

  current_principal: {}

  current_action: {}

  current_target: {}

  current_effect: {}

  current_capability_contract_hash: string

  current_scope: {}

  current_regime: {}

  current_policy_state: {}

  current_time: timestamp
```

Response:

```yaml
policy_engine_revalidation_result:
  prior_decision_id: string

  state:
    - STILL_VALID
    - REVALIDATE
    - INVALID
    - CONFLICT
    - UNKNOWN_GAP

  changed_dependencies: []

  replacement_decision_id: null
```

______________________________________________________________________

## 110. Protocol — Invalidation

```yaml
policy_engine_invalidate:
  decision_id: string

  cause:
    type: string
    object_id: string
    old_version: null
    new_version: null

  detected_at: timestamp

  evidence_refs: []
```

______________________________________________________________________

## 111. Control-Plane Integration

The Policy Engine SHOULD expose the final policy result to the control plane as evidence.

Example:

```yaml
control_plane_policy_input:
  decision_id: string

  decision_state: ALLOW

  decision_hash: string

  policy_read_set: []

  scope: {}

  regime: {}

  obligations: []

  freshness: {}

  provenance: {}
```

______________________________________________________________________

## 112. Control-Plane Rule

The control plane MUST NOT infer:

```text
COMMITTABLE
```

solely from:

```text
policy_decision = ALLOW
```

It must separately validate its other governing conditions.

______________________________________________________________________

## 113. Commit Guard Composition

Conceptually:

```text
COMMITTABLE =
PolicyValid
∧ AuthorityValid
∧ EvidenceValid
∧ ConstraintsFresh
∧ SemanticTransactionValid
∧ ObservabilityValid
∧ CapabilityContractValid
∧ EffectReleaseStateValid
```

This is an AMOS control model.

Exact runtime semantics require executable implementation and validation.

______________________________________________________________________

## 114. Observability

The Policy Engine SHOULD emit enough observability for reconstruction without leaking prohibited information.

Recommended events:

```text
POLICY_EVALUATION_STARTED

POLICY_DISCOVERY_COMPLETED

POLICY_IDENTITY_RESOLVED

POLICY_APPLICABILITY_RESOLVED

POLICY_RULE_EVALUATED

POLICY_EXCEPTION_EVALUATED

POLICY_CONFLICT_DETECTED

POLICY_PRECEDENCE_APPLIED

POLICY_DECISION_CREATED

POLICY_DECISION_REVALIDATED

POLICY_DECISION_INVALIDATED

POLICY_DECISION_QUARANTINED

POLICY_DECISION_SUPERSEDED
```

______________________________________________________________________

## 115. Observability Envelope

Logging itself MUST remain governed.

The Policy Engine SHOULD NOT expose sensitive policy context merely for debugging.

An infrastructure-owned observability envelope SHOULD define:

```text
what may be logged;
which fields must be redacted;
who may inspect logs;
retention;
integrity requirements;
provenance requirements.
```

______________________________________________________________________

## 116. Performance

Policy optimization MAY reduce:

```text
registry reads;
duplicate evaluation;
unnecessary policy loading;
redundant predicate checks;
unrelated revalidation.
```

Optimization MUST NOT weaken:

```text
policy coverage;
scope correctness;
conflict visibility;
provenance;
freshness;
revocation;
authority separation;
unknown preservation.
```

______________________________________________________________________

## 117. Fast Path

A fast policy path MAY reuse a prior proof capsule only when:

```text
dependency closure established;
policy read set unchanged;
scope compatible;
regime compatible;
principal compatible;
action compatible;
target compatible;
effect compatible;
freshness valid;
no unresolved conflict;
no revocation;
no governance escalation trigger.
```

Otherwise escalate to deeper evaluation.

______________________________________________________________________

## 118. Fast-Path Invariant

```text
FAST != WEAKER
```

Fast-path execution changes retrieval/evaluation cost.

It MUST NOT change governing semantics.

______________________________________________________________________

## 119. Policy Proof Capsule

Important decisions SHOULD conceptually carry:

```yaml
policy_proof_capsule:
  claim:
    class: DERIVED
    text: "Policy decision D applies to request Q."

  premises: []

  policies: []

  evidence: []

  provenance: []

  scope: {}

  regime: {}

  freshness: {}

  dependencies: []

  competing: []

  falsifiers: []

  confidence_ceiling: null
```

______________________________________________________________________

## 120. RSCF Integration

The Policy Engine SHOULD support RSCF representation.

```yaml
rscf:
  claim:
    id: "RSCF_POLICY_ENGINE_DECISION"
    class: DERIVED

  premises:
    - policy_identity_valid
    - policy_applicability_valid
    - predicates_valid
    - scope_valid
    - regime_valid
    - composition_valid

  evidence: []

  provenance: []

  dependencies: []

  competing: []

  falsifiers: []

  confidence_ceiling: null
```

______________________________________________________________________

## 121. RSCF Invalidation

If a load-bearing premise fails:

```text
invalidate dependent policy conclusion
```

not:

```text
erase unrelated policy knowledge.
```

This preserves selective repair.

______________________________________________________________________

## 122. GMEF Integration

Changes to Policy Engine semantics SHOULD be governed when they affect:

```text
policy discovery;
applicability;
decision states;
precedence;
exceptions;
unknown handling;
conflict handling;
scope;
regime;
authority interaction;
commit interaction;
freshness;
revocation;
provenance;
effect classification.
```

______________________________________________________________________

## 123. Engine Change Manifest

```yaml
policy_engine_change:
  change_id: string

  from_version: string
  to_version: string

  change_class:
    - COSMETIC
    - SCHEMA
    - SEMANTIC
    - GOVERNANCE
    - AUTHORITY_BOUNDARY
    - COMMIT_BOUNDARY

  affected_components: []

  expected_behavior_changes: []

  risks: []

  validators_required: []

  rollback_plan: null

  approval_state: PROPOSED
```

______________________________________________________________________

## 124. Promotion Model

```text
STRUCTURAL_MODEL
        ↓
SCHEMA_VALIDATED
        ↓
POLICY_REGISTRY_INTEGRATED
        ↓
EXECUTABLE
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

______________________________________________________________________

## 125. Promotion Requirements

## Structural → Schema Validated

Requires:

```text
input schema;
output schema;
decision enums;
policy identity schema;
applicability schema;
conflict schema.
```

## Schema → Registry Integrated

Requires:

```text
policy lookup;
version resolution;
status resolution;
supersession resolution.
```

## Registry Integrated → Executable

Requires:

```text
working evaluator;
deterministic rule semantics where declared;
unknown handling;
conflict handling;
exception handling.
```

## Executable → Tested

Requires executed test evidence.

## Tested → Governed Active

Requires validation of:

```text
authority boundaries;
control-plane integration;
rollback;
security;
observability;
freshness;
revocation;
effect binding;
no unresolved critical gaps.
```

______________________________________________________________________

## 126. Security Model

The Policy Engine SHOULD defend against:

```text
policy injection;
policy deletion;
policy substitution;
policy rollback;
registry poisoning;
exception forgery;
exception widening;
scope widening;
regime widening;
authority smuggling;
capability smuggling;
commit smuggling;
policy cache poisoning;
decision replay;
parameter mutation;
effect mutation;
provenance stripping;
conflict suppression;
unknown coercion;
policy downgrade.
```

______________________________________________________________________

## 127. Trust Model

Policy trust is:

```text
local;
typed;
scoped;
versioned;
provenance-aware;
regime-aware;
freshness-bounded.
```

No source receives universal trust merely because it is authoritative in one domain.

______________________________________________________________________

## 128. Provenance Topology

Where multiple policy sources exist, the engine SHOULD track ancestry.

Example:

```text
SOURCE_A
  ├── POLICY_A1
  ├── POLICY_A2
  └── POLICY_A3
```

These are not three independent origins.

Therefore:

```text
count(policy_objects)
!=
count(independent_authorities)
```

______________________________________________________________________

## 129. Policy Sybil Resistance

A policy conclusion MUST NOT gain apparent confidence merely because the same underlying rule is:

```text
copied;
renamed;
reformatted;
translated;
summarized;
embedded in multiple files.
```

Independence must be demonstrated where independence matters.

______________________________________________________________________

## 130. Policy Engine Gap Classes

```text
CRITICAL

DECISION_RELEVANT

EXPLANATORY

COSMETIC
```

______________________________________________________________________

## 131. Critical Gaps

Examples:

```text
unknown governing policy;
unknown hard prohibition;
unknown policy precedence;
unknown exception validity;
unknown scope;
unknown regime;
unknown authority interaction;
unknown effect class;
unknown policy version;
unknown supersession state.
```

Critical gaps MUST block unconditional policy approval when outcome-sensitive.

______________________________________________________________________

## 132. Gap Object

```yaml
policy_engine_gap:
  gap_id: string

  class:
    - CRITICAL
    - DECISION_RELEVANT
    - EXPLANATORY
    - COSMETIC

  component: string

  description: string

  blocks: []

  cheapest_resolution: null

  evidence_required: []

  state:
    - OPEN
    - RESOLVED
    - ACCEPTED
```

______________________________________________________________________

## 133. Gap Resolution Priority

Resolve gaps in this order:

```text
CRITICAL
    ↓
DECISION_RELEVANT
    ↓
EXPLANATORY
    ↓
COSMETIC
```

Do not spend evaluation resources polishing explanatory gaps while a critical policy gap remains unresolved.

______________________________________________________________________

## 134. Minimum Engine Contract

The minimum structurally complete Policy Engine MUST support:

```text
policy discovery;
policy identity;
policy version;
applicability;
rule evaluation;
ALLOW;
DENY;
CONDITIONAL;
UNKNOWN_GAP;
conflict preservation;
scope;
regime;
provenance;
freshness;
decision generation.
```

A production-grade engine additionally requires:

```text
authority integration;
commit-time revalidation;
fine-grained read sets;
revocation;
exceptions;
observability;
security;
cache integrity;
recovery;
tests;
auditing.
```

______________________________________________________________________

## 135. Example — Read-Only Request

```yaml
policy_engine_request:
  request_id: "REQ_001"

  principal:
    principal_id: "AGENT_A"
    principal_type: AGENT

  action:
    action_class: READ
    operation: "read_resource"

  capability:
    capability_id: "CAP_RESOURCE_READ"

  target:
    target_id: "RESOURCE_001"

  effect_intent:
    effect_class: E0_READ_ONLY
    persistent: false
    externally_visible: false
```

Possible result:

```yaml
policy_engine_result:
  decision:
    state: ALLOW

  reason_codes:
    - ALLOW_POLICY_SATISFIED

  obligations:
    - RECORD_PROVENANCE
```

This does not independently establish resource access authority.

______________________________________________________________________

## 136. Example — Persistent Write

```yaml
policy_engine_request:
  request_id: "REQ_002"

  principal:
    principal_id: "AGENT_A"
    principal_type: AGENT

  action:
    action_class: WRITE
    operation: "persistent_write"

  target:
    target_id: "RESOURCE_002"

  effect_intent:
    effect_class: E3_PERSISTENT_WRITE
    persistent: true
```

Possible result:

```yaml
policy_engine_result:
  decision:
    state: CONDITIONAL

  conditions:
    - VALID_WRITE_AUTHORITY
    - COMMIT_TIME_REVALIDATION

  obligations:
    - RECORD_PROVENANCE
    - RECORD_TRANSACTION
```

This is not permission to commit the write.

______________________________________________________________________

## 137. Example — Explicit Denial

```yaml
policy_engine_result:
  decision:
    state: DENY

  reason_codes:
    - DENY_RESOURCE_SCOPE

  prohibitions:
    - prohibition_id: "PROHIBITION_001"
      operation: "persistent_write"
      hard: true
```

Downstream components MUST NOT override this denial without a valid governing exception.

______________________________________________________________________

## 138. Example — Unknown

```yaml
policy_engine_result:
  decision:
    state: UNKNOWN_GAP

  reason_codes:
    - UNKNOWN_POLICY

  unresolved:
    - "authoritative policy for resource class not resolved"
```

The engine MUST NOT transform this into:

```text
ALLOW
```

for workflow convenience.

______________________________________________________________________

## 139. Example — Conflict

```yaml
policy_engine_result:
  decision:
    state: CONFLICT

  conflicts:
    - conflict_id: "CONFLICT_001"

      policies:
        - POLICY_A
        - POLICY_B

      conflict_type: ALLOW_DENY

      resolution:
        state: UNRESOLVED
```

______________________________________________________________________

## 140. Example — Revalidation

Prepared:

```text
POLICY_X@1.0
→ ALLOW
```

Current:

```text
POLICY_X@2.0
```

If `POLICY_X` was load-bearing:

```text
prior decision
    ↓
REVALIDATE
```

The old `ALLOW` MUST NOT be blindly reused.

______________________________________________________________________

## 141. Example — Selective Invalidation

```text
D1 ← POLICY_A + POLICY_B
D2 ← POLICY_C
D3 ← POLICY_B + POLICY_D
```

If:

```text
POLICY_B changes
```

then:

```text
invalidate D1
invalidate D3
preserve D2
```

provided no hidden dependency links `D2` to `POLICY_B`.

______________________________________________________________________

## 142. Example — H/M/L Policy

```text
H POLICY:
external disclosure of protected information prohibited

M POLICY:
workflow may generate external communication drafts

L POLICY:
send-message capability available
```

Result:

```text
draft generation may be allowed
```

while:

```text
external send may remain denied
```

This demonstrates:

```text
CAPABILITY != AUTHORITY
PROPOSAL != COMMIT
```

______________________________________________________________________

## 143. Audit Surface

An auditor SHOULD be able to reconstruct:

1. What request entered the engine?
1. Who was the principal?
1. What action was normalized?
1. What capability was resolved?
1. What target was bound?
1. What effect was evaluated?
1. What policies were discovered?
1. Which policy versions were used?
1. Which policies were applicable?
1. Which were excluded?
1. Why?
1. What predicates were evaluated?
1. Which predicates were unknown?
1. Which rules fired?
1. What exceptions were evaluated?
1. Were exceptions valid?
1. What conflicts were detected?
1. What precedence was applied?
1. What obligations were created?
1. What prohibitions were created?
1. What conditions remained?
1. What was the final policy decision?
1. What was its scope?
1. What was its regime?
1. What evidence supported it?
1. What was its policy read set?
1. When was it evaluated?
1. What invalidates it?
1. Was it revalidated before commit?
1. Did runtime behavior conform to it?

______________________________________________________________________

## 144. Completion Matrix

| Surface                   | Specification State |
| ------------------------- | ------------------- |
| Purpose                   | COMPLETE_AS_MODEL   |
| Architecture              | COMPLETE_AS_MODEL   |
| Inputs                    | COMPLETE_AS_MODEL   |
| Outputs                   | COMPLETE_AS_MODEL   |
| Context normalization     | COMPLETE_AS_MODEL   |
| Policy discovery          | COMPLETE_AS_MODEL   |
| Identity resolution       | COMPLETE_AS_MODEL   |
| Version resolution        | COMPLETE_AS_MODEL   |
| Applicability             | COMPLETE_AS_MODEL   |
| Predicate evaluation      | COMPLETE_AS_MODEL   |
| Rule evaluation           | COMPLETE_AS_MODEL   |
| Exceptions                | COMPLETE_AS_MODEL   |
| Composition               | COMPLETE_AS_MODEL   |
| Conflict detection        | COMPLETE_AS_MODEL   |
| Precedence                | COMPLETE_AS_MODEL   |
| Supersession              | COMPLETE_AS_MODEL   |
| Obligations               | COMPLETE_AS_MODEL   |
| Prohibitions              | COMPLETE_AS_MODEL   |
| Conditions                | COMPLETE_AS_MODEL   |
| Decision builder          | COMPLETE_AS_MODEL   |
| Provenance                | COMPLETE_AS_MODEL   |
| Read sets                 | COMPLETE_AS_MODEL   |
| Freshness                 | COMPLETE_AS_MODEL   |
| Revalidation              | COMPLETE_AS_MODEL   |
| H/M/L                     | COMPLETE_AS_MODEL   |
| RSCF                      | COMPLETE_AS_MODEL   |
| GMEF                      | COMPLETE_AS_MODEL   |
| Agents                    | COMPLETE_AS_MODEL   |
| Skills                    | COMPLETE_AS_MODEL   |
| Workflows                 | COMPLETE_AS_MODEL   |
| Protocols                 | COMPLETE_AS_MODEL   |
| Failure modes             | COMPLETE_AS_MODEL   |
| Repair/recovery           | COMPLETE_AS_MODEL   |
| Tests                     | COMPLETE_AS_MODEL   |
| Falsifiers                | COMPLETE_AS_MODEL   |
| Executable implementation | UNKNOWN/GAP         |
| Executed test evidence    | UNKNOWN/GAP         |
| Formal verification       | UNKNOWN/GAP         |
| Production deployment     | UNKNOWN/GAP         |
| Canon admission           | UNKNOWN/GAP         |

______________________________________________________________________

## 145. RSCF Completion State

```yaml
rscf_completion:
  claim:
    id: "AMOS_POLICY_ENGINE"
    class: MODEL

    text: >
      This artifact defines a structurally complete AMOS OS
      policy-evaluation architecture for producing governed,
      provenance-bound policy decisions.

  evidence:
    - "AMOS infrastructure/control-plane architecture"
    - "associated AMOS policy/capability contract surfaces"

  provenance:
    origin_architect: "Trang Phan"
    steward: "Trang Phan"

  scope:
    system: "AMOS OS"
    component: "Policy Engine"

  regime:
    - DESIGN
    - ARCHITECTURE
    - GOVERNANCE_MODEL

  freshness:
    artifact_version: "1.0.0"
    updated: "2026-08-26"

  dependencies:
    - POLICY_REGISTRY.md
    - POLICY_DECISION.md
    - CAPABILITY_MANIFEST.md
    - CAPABILITY_CONTRACT.md
    - CONTROL_PLANE_MAP.md

  competing: []

  falsifiers:
    - "policy decision cannot be reconstructed"
    - "governing policies are silently omitted"
    - "unknown policy state becomes permission"
    - "policy allow grants authority directly"
    - "policy engine performs unauthorized commit"
    - "scope/regime boundaries are not preserved"

  confidence_ceiling: 0
```

`confidence_ceiling: 0` here means no empirical/runtime validation is being claimed by this architecture document.

It does **not** mean the specification contains no substantive architecture.

______________________________________________________________________

## 146. Hard Boundary Block

```text
POLICY_ENGINE != POLICY_REGISTRY

POLICY_ENGINE != POLICY

POLICY_ENGINE != POLICY_DECISION

POLICY_ENGINE != CAPABILITY_PROVIDER

POLICY_ENGINE != AUTHORITY_PROVIDER

POLICY_ENGINE != CONTROL_PLANE

POLICY_ENGINE != EFFECT_EXECUTOR

POLICY_ENGINE != RELEASE_LEDGER

POLICY_ENGINE != RECEIVER

POLICY_ENGINE != EMPIRICAL_VALIDATOR

POLICY_ALLOW != AUTHORITY

POLICY_ALLOW != COMMITTABLE

POLICY_ALLOW != COMMITTED

CAPABILITY != AUTHORITY

CAPABILITY != POLICY_PERMISSION

VALIDATION != AUTHORIZATION

AUTHORIZATION != EXECUTION

PROPOSAL != COMMIT

EXECUTION != FINALITY

SUCCESS != POLICY_VALIDITY

POLICY_VALIDITY != FACTUAL_TRUTH

UNKNOWN/GAP != PASS

UNKNOWN/GAP != ALLOW

CONFLICT != ALLOW

CONDITIONAL != ALLOW

CORRELATED_PROVENANCE != INDEPENDENT_CONFIRMATION

ADDRESSABLE != VALIDATED

STRUCTURAL_MODEL != IMPLEMENTED_RUNTIME

IMPLEMENTED != VALIDATED

TESTED != FORMALLY_VERIFIED

MODEL != EMPIRICAL_FACT
```

______________________________________________________________________

## 147. Canon Boundary

Trang Phan remains the origin architect and steward of AMOS.

This artifact defines a substantive proposed architecture for the AMOS `POLICY_ENGINE.md` surface.

Its completeness as a specification does not itself establish:

```text
runtime implementation;
executed validation;
production deployment;
formal verification;
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

______________________________________________________________________

## 148. Final Policy Engine Contract

AMOS SHALL preserve the following architecture:

```text
TASK_CONTRACT
      ↓
RESOLVED_CAPABILITY_CONTRACT
      ↓
POLICY CONTEXT
      ↓
POLICY REGISTRY
      ↓
POLICY DISCOVERY
      ↓
IDENTITY + VERSION RESOLUTION
      ↓
SUPERSESSION CHECK
      ↓
APPLICABILITY
      ↓
PREDICATE EVALUATION
      ↓
RULE EVALUATION
      ↓
EXCEPTION VALIDATION
      ↓
OBLIGATION / PROHIBITION / CONDITION EXTRACTION
      ↓
CONFLICT DETECTION
      ↓
PRECEDENCE RESOLUTION
      ↓
POLICY COMPOSITION
      ↓
PROVENANCE + READ-SET BINDING
      ↓
FRESHNESS BINDING
      ↓
POLICY_DECISION
      ↓
CONTROL-PLANE HANDOFF
      ↓
COMMIT-TIME REVALIDATION
```

The central engine invariant is:

> **The AMOS Policy Engine determines what the applicable policy layer concludes about a precisely bound request. It does not convert that conclusion into capability, authority, execution, or commit.**

Therefore:

```text
POLICY_ENGINE → POLICY_DECISION
```

but never automatically:

```text
POLICY_ENGINE → EFFECT
```

and:

```text
ALLOW
```

means only:

> the evaluated policy layer permits the bound action within the decision's validated scope, regime, policy versions, context, and freshness envelope.

It does not mean:

```text
AUTHORIZED

EXECUTABLE

SAFE

CORRECT

COMMITTABLE

COMMITTED
```

Any unresolved load-bearing policy, applicability, scope, regime, provenance, conflict, authority, freshness, or effect-binding condition remains explicitly:

```text
UNKNOWN/GAP
```

or the corresponding:

```text
CONDITIONAL
CONFLICT
ESCALATE
REVALIDATE
DENY
```

state.

AMOS MUST NOT convert missing policy information into permission.

AMOS MUST NOT convert capability into authority.

AMOS MUST NOT convert policy permission into commit authority.

AMOS MUST NOT suppress genuine policy conflict.

AMOS MUST NOT reuse stale decisions across incompatible state.

AMOS MUST preserve enough provenance to reconstruct consequential policy decisions.

AMOS MUST prefer selective invalidation and repair over unnecessary global recomputation.

Integrity remains prior to completeness, fluency, speed, and optimization.

______________________________________________________________________

## END — POLICY_ENGINE.md

```
```

______________________________________________________________________

[[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] · [[00_ROOT/AMOS MOC|AMOS MOC]]

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

______________________________________________________________________

RSCF-NODE
node_id: policy_engine
node_type: note
path: 03_CONTROL_PLANE/03_POLICY/POLICY_ENGINE.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
  claim_class: AMOS_MODEL

______________________________________________________________________

**MOC:** [[03_CONTROL_PLANE/03_POLICY/03_POLICY_MOC|03_POLICY_MOC]]
