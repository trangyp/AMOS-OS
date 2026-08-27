---
title: POLICY DECISION
type: decision
source: 03_CONTROL_PLANE/03_POLICY
tags: [control_plane, policy, note, canon/control-plane]
rscf:
  state: DERIVED
  claim_class: CONDITIONAL
  provenance: AMOS_corpus
  scope: AMOS_general
---


# AMOS Policy Decision

## 0. Status

`POLICY_DECISION.md` defines the AMOS OS contract for representing, evaluating, composing, validating, recording, invalidating, and consuming policy decisions.

A policy decision is the governed result of applying one or more applicable policy rules to a specific:

- principal;
- action;
- capability;
- target;
- resource;
- context;
- scope;
- regime;
- authority state;
- evidence state;
- proposed effect;
- and evaluation epoch.

This document defines the logical architecture of that decision object.

It does **not** assert that:

- a policy engine implementing this contract currently exists;
- every AMOS policy has been encoded;
- every policy is canonical;
- every policy decision can be automatically computed;
- a policy decision grants capability;
- a policy decision grants authority;
- `ALLOW` automatically permits execution;
- execution success proves policy compliance;
- policy compliance proves factual correctness;
- policy compliance authorizes durable commit;
- this document has already been admitted into final AMOS canon.

The governing distinctions are:

```text
POLICY != POLICY_DECISION

POLICY_DECISION != AUTHORITY

POLICY_DECISION != CAPABILITY

POLICY_DECISION != EXECUTION

ALLOW != COMMIT

ALLOW != SUCCESS

DENY != TECHNICAL_IMPOSSIBILITY

CONDITIONAL != ALLOW

ESCALATE != DENY

UNKNOWN/GAP != ALLOW

UNKNOWN/GAP != PASS

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

VALIDATION != AUTHORIZATION

AUTHORIZATION != EXECUTION

EXECUTION != FINALITY

RECEIPT_ID != VERIFIED_COMPLETION

ADDRESSABLE != VALIDATED

PLACEHOLDER != IMPLEMENTED
```

---

# 1. Purpose

The purpose of `POLICY_DECISION.md` is to establish one explicit governed object for answering:

> Given a particular principal, requested operation, target, capability, context, evidence state, authority state, and policy set, what does the applicable AMOS policy layer currently conclude?

The policy decision object exists so that downstream systems do not infer permission from:

* capability existence;
* provider availability;
* agent preference;
* Skill selection;
* successful tool invocation;
* previous authorization;
* stale cached decisions;
* undocumented conventions;
* model confidence;
* or absence of an explicit prohibition.

Policy evaluation MUST produce an explicit decision state.

---

# 2. Position in AMOS OS

Conceptually:

```text
TASK / INTENT
      ↓
CAPABILITY RESOLUTION
      ↓
POLICY CONTEXT
      ↓
POLICY REGISTRY
      ↓
POLICY APPLICABILITY
      ↓
POLICY EVALUATION
      ↓
POLICY COMPOSITION
      ↓
POLICY_DECISION
      ↓
AUTHORITY / CONSTRAINT / FRESHNESS CHECKS
      ↓
EFFECT PROPOSAL
      ↓
COMMIT-TIME REVALIDATION
      ↓
EFFECT RELEASE DECISION
      ↓
COMMIT / BLOCK / RECONCILE
```

A policy decision is therefore an intermediate governed state.

It is not the final effect-release state.

---

# 3. Relationship to POLICY_REGISTRY.md

`POLICY_REGISTRY.md` answers:

```text
Which policy objects exist?
```

`POLICY_DECISION.md` answers:

```text
What is the result of applying the relevant policy objects
to this specific requested action and context?
```

Therefore:

```text
POLICY_REGISTRY
        ↓
policy discovery

APPLICABILITY RESOLUTION
        ↓
applicable policy set

POLICY EVALUATION
        ↓
individual policy results

POLICY COMPOSITION
        ↓
POLICY_DECISION
```

A policy decision MUST preserve references to the policy versions from which it was derived.

---

# 4. Relationship to CAPABILITY_MANIFEST.md

Capability resolution answers:

```text
Can a known provider potentially perform operation X?
```

Policy evaluation answers:

```text
Does applicable policy permit, deny, constrain,
or escalate operation X in this context?
```

These are separate questions.

Therefore:

```text
CAPABILITY(C)
AND
AVAILABLE(C)
```

does not imply:

```text
POLICY_ALLOW(C)
```

and:

```text
POLICY_ALLOW(C)
```

does not imply:

```text
CAPABLE(C)
```

Both may be required.

---

# 5. Relationship to Authority

Policy and authority MUST remain separate.

Policy answers:

```text
What do the applicable rules permit or prohibit?
```

Authority answers:

```text
Does this principal possess valid authority
to perform this operation against this target?
```

Thus:

```text
PolicyAllow(P, A, R)
∧
AuthorityValid(P, A, R)
```

may be required before execution.

But:

```text
PolicyAllow(P, A, R)
```

alone is insufficient.

Likewise:

```text
AuthorityValid(P, A, R)
```

does not override applicable policy unless a valid policy explicitly defines such an override mechanism.

---

# 6. Relationship to Control Plane

The policy decision is evidence consumed by the control plane.

The policy decision MUST NOT impersonate the control plane itself.

Conceptually:

```text
POLICY ENGINE
    ↓
POLICY_DECISION
    ↓
CONTROL PLANE
    ↓
final admissibility / commit checks
```

The control plane may reject an action even when:

```text
policy_decision = ALLOW
```

because another load-bearing condition failed.

Examples:

```text
authority stale;
capability contract changed;
resource state changed;
read set stale;
constraint context changed;
effect digest changed;
transaction lineage changed;
observability requirements unmet;
release ledger ambiguous;
receiver completion uncertain.
```

---

# 7. Core Policy Decision Object

Canonical conceptual object:

```text
POLICY_DECISION :=
    Identity
  × Subject
  × RequestedAction
  × Target
  × CapabilityContext
  × PolicySet
  × Applicability
  × EvidenceContext
  × AuthorityContext
  × ConstraintContext
  × EvaluationResults
  × CompositionResult
  × Obligations
  × Prohibitions
  × Conditions
  × Scope
  × Regime
  × Freshness
  × Provenance
  × Uncertainty
  × FinalDecision
```

---

# 8. Canonical Representation

```yaml
policy_decision:
  identity:
    decision_id: "PD_*"
    version: "1.0.0"
    schema_version: "1.0.0"

  subject:
    principal_id: null
    principal_type: null
    delegation_chain: []

  request:
    action: null
    operation: null
    capability_id: null
    provider_id: null
    target_id: null
    resource_ids: []
    effect_class: null

  context:
    task_id: null
    transaction_id: null
    session_id: null
    environment: null
    scope: {}
    regime: {}
    time: null

  policies:
    discovered: []
    applicable: []
    non_applicable: []
    unresolved: []

  evaluations: []

  composition:
    strategy: null
    conflicts: []
    unresolved_conflicts: []

  obligations: []
  prohibitions: []
  conditions: []

  authority:
    state: UNKNOWN
    witness_refs: []

  constraints:
    state: UNKNOWN
    refs: []

  evidence:
    refs: []

  provenance:
    policy_versions: []
    source_refs: []
    ancestry: []

  freshness:
    evaluated_at: null
    expires_at: null
    invalidation_events: []

  decision:
    state: UNKNOWN_GAP
    reason_codes: []

  uncertainty:
    evidence: null
    applicability: null
    policy_interpretation: null
    scope: null
    temporal: null
    authority: null
    provenance_independence: null

  confidence_ceiling: 0
```

---

# 9. Policy Decision States

The base AMOS policy-decision state space SHOULD include:

```text
ALLOW
DENY
CONDITIONAL
ESCALATE
REVALIDATE
CONFLICT
NOT_APPLICABLE
UNKNOWN_GAP
```

These states MUST remain semantically distinct.

---

# 10. ALLOW

`ALLOW` means:

> The applicable policy set, under the evaluated scope, regime, evidence, policy versions, and context, does not prohibit the requested operation and all policy-local mandatory conditions evaluated by this policy decision have been satisfied.

It does **not** mean:

```text
AUTHORIZED
EXECUTABLE
SAFE
CORRECT
COMMITTABLE
COMMITTED
```

A downstream authority or commit gate may still block the action.

---

# 11. DENY

`DENY` means:

> At least one applicable governing policy prohibits the requested action and no valid higher-precedence rule resolves the prohibition in favor of execution.

A denial SHOULD include:

```yaml
denial:
  policy_id: string
  rule_id: string
  reason_code: string
  explanation: string
  scope: {}
  remediation_possible: null
```

A denial MUST NOT be silently converted into `ALLOW` because an agent believes the action is useful.

---

# 12. CONDITIONAL

`CONDITIONAL` means:

> Policy permits the action only if explicitly identified conditions are satisfied.

Example:

```yaml
decision:
  state: CONDITIONAL

conditions:
  - condition_id: "COND_001"
    requirement: "human approval required"
    state: UNSATISFIED
```

Until all mandatory conditions are satisfied:

```text
CONDITIONAL != ALLOW
```

---

# 13. ESCALATE

`ESCALATE` means:

> The policy layer has identified a decision that cannot be safely or legitimately resolved at the current authority, evidence, or governance level.

Examples:

```text
policy ambiguity;
high-consequence action;
conflicting governing policies;
missing authority interpretation;
unresolved legal constraint;
exception request;
insufficient policy coverage;
required human decision.
```

Escalation is not denial.

It is also not permission.

---

# 14. REVALIDATE

`REVALIDATE` means:

> A previously usable policy result cannot safely be reused because one or more load-bearing validity conditions may have changed.

Examples:

```text
policy version changed;
policy registry changed;
authority changed;
resource state changed;
scope changed;
regime changed;
capability contract changed;
effect changed;
freshness expired.
```

---

# 15. CONFLICT

`CONFLICT` means:

> Two or more applicable policies produce incompatible requirements and the conflict cannot be deterministically resolved using valid precedence, specificity, scope, supersession, or exception rules.

The conflict MUST remain visible.

```text
CONFLICT != DENY
CONFLICT != ALLOW
```

unless a governing conflict-resolution rule explicitly defines the outcome.

---

# 16. NOT_APPLICABLE

`NOT_APPLICABLE` means:

> A policy or policy decision does not govern the requested action under the evaluated applicability envelope.

This state SHOULD be used for individual policy evaluation.

A final decision cannot infer `ALLOW` merely because one discovered policy is not applicable.

---

# 17. UNKNOWN_GAP

`UNKNOWN_GAP` means:

> The policy result cannot be established with sufficient integrity from available policy, context, evidence, or applicability information.

This state is mandatory when a load-bearing policy question is unresolved.

```text
UNKNOWN/GAP != ALLOW
UNKNOWN/GAP != PASS
```

---

# 18. Decision Subject

Every policy decision MUST identify the governed subject where applicable.

```yaml
subject:
  principal_id: string

  principal_type:
    - HUMAN
    - AGENT
    - SERVICE
    - WORKFLOW
    - SYSTEM
    - ORGANIZATION
    - CONTROL_PLANE

  acting_as: null

  delegation_chain: []

  tenant_id: null
  organization_id: null
```

Identity alone does not establish authority.

---

# 19. Requested Action

The requested action SHOULD be represented independently of natural-language intent.

```yaml
request:
  action_id: string

  action_class:
    - READ
    - SEARCH
    - RETRIEVE
    - TRANSFORM
    - GENERATE
    - ANALYZE
    - PREDICT
    - PROPOSE
    - WRITE
    - UPDATE
    - DELETE
    - EXECUTE
    - COMMUNICATE
    - TRANSFER
    - COMMIT
    - ADMINISTER
    - DELEGATE

  operation: string

  capability_id: null
  provider_id: null

  target_id: null
  resource_ids: []

  parameters_hash: null

  effect_class: null
```

Policy evaluation SHOULD use the normalized operation where possible rather than relying only on natural-language labels.

---

# 20. Effect Intent

For effect-producing actions, policy evaluation SHOULD receive an explicit effect intent.

```yaml
effect_intent:
  effect_id: string

  effect_type: string

  target: string

  payload_digest: string

  effect_class: string

  persistent: boolean

  externally_visible: boolean

  reversible: null

  compensation_available: null
```

Policy SHOULD evaluate the proposed effect, not merely the tool name.

---

# 21. Policy Applicability

Before evaluating a policy's rule body, AMOS SHOULD establish whether that policy applies.

Applicability may depend on:

```text
principal type;
action class;
capability;
provider;
target;
resource;
domain;
environment;
jurisdiction;
scope;
regime;
time;
effect class;
sensitivity;
consequence;
delegation state.
```

---

# 22. Applicability Record

```yaml
applicability:
  policy_id: string
  policy_version: string

  result:
    - APPLICABLE
    - NOT_APPLICABLE
    - CONDITIONAL
    - UNKNOWN_GAP

  matched_conditions: []
  failed_conditions: []
  unresolved_conditions: []

  scope_match: null
  regime_match: null
  principal_match: null
  action_match: null
  target_match: null
  temporal_match: null
```

---

# 23. Applicability Invariant

Unknown applicability for a potentially governing policy MUST NOT silently become non-applicability.

Formally:

```text
PotentiallyGoverning(P)
∧
Applicability(P) = UNKNOWN
→
FinalDecision ≠ ALLOW
```

unless another canonical rule explicitly proves that the unresolved policy cannot change the outcome.

---

# 24. Individual Policy Evaluation

Each applicable policy SHOULD generate an independent evaluation record.

```yaml
policy_evaluation:
  policy_id: string
  policy_version: string

  rule_id: string

  applicability: APPLICABLE

  result:
    - ALLOW
    - DENY
    - CONDITIONAL
    - ESCALATE
    - UNKNOWN_GAP

  reasons: []

  obligations: []
  prohibitions: []
  conditions: []

  evidence_refs: []

  scope: {}
  regime: {}

  confidence_ceiling: null
```

The final decision is composed from these records.

---

# 25. Policy Composition

Multiple policies may govern one action.

Conceptually:

```text
P1 → D1
P2 → D2
P3 → D3

Compose(D1, D2, D3)
        ↓
POLICY_DECISION
```

Composition MUST NOT use arbitrary ordering unless ordering itself is canonical policy.

---

# 26. Composition Inputs

Policy composition SHOULD consider:

```text
policy precedence;
scope specificity;
principal specificity;
resource specificity;
effect specificity;
version/supersession;
exception relationships;
jurisdiction;
temporal validity;
explicit override relationships;
hard-vs-soft constraint class.
```

---

# 27. Policy Precedence

Where precedence exists, it MUST be explicit.

```yaml
precedence:
  policy_id: string
  outranks:
    - policy_id: string
  basis:
    - CANON
    - LAW
    - ORGANIZATIONAL_AUTHORITY
    - POLICY_HIERARCHY
    - EXPLICIT_SUPERSESSION
```

No policy receives precedence merely because it was loaded first.

---

# 28. Only-Tighten Principle

Where applicable to a policy family, delegated or lower-level policy SHOULD be allowed to tighten a governing constraint but not silently weaken it.

Conceptually:

```text
Allowed_lower ⊆ Allowed_upper
```

unless the upper policy explicitly grants exception authority.

This is a governance model rule and MUST be scoped to policy families where such inheritance is defined.

---

# 29. Deny Dominance

For hard constraints:

```text
HardDeny(P)
→
DENY
```

unless a valid explicit override rule exists.

The system MUST NOT infer an override from:

```text
agent preference;
business value;
model confidence;
technical capability;
successful previous execution.
```

---

# 30. Conditional Composition

If:

```text
P1 = ALLOW
P2 = CONDITIONAL(C1)
P3 = CONDITIONAL(C2)
```

then:

```text
Final = CONDITIONAL(C1 ∧ C2)
```

unless precedence rules establish otherwise.

---

# 31. Unknown Composition

If an unresolved policy could materially change the decision:

```text
OutcomeSensitiveUnknown = true
```

then:

```text
FinalDecision = UNKNOWN_GAP
```

or:

```text
ESCALATE
```

depending on governance rules.

---

# 32. Conflict Preservation

Suppose:

```text
P1 → REQUIRE(A)
P2 → PROHIBIT(A)
```

and neither has valid precedence.

Then:

```text
FinalDecision = CONFLICT
```

The system MUST NOT select whichever result is more convenient.

---

# 33. Obligations

Policy may permit an action while imposing obligations.

```yaml
obligation:
  obligation_id: string

  type:
    - LOG
    - AUDIT
    - NOTIFY
    - APPROVAL
    - REDACT
    - ENCRYPT
    - RETAIN
    - DELETE_AFTER
    - RECORD_PROVENANCE
    - REQUIRE_RECEIPT
    - REQUIRE_ROLLBACK
    - REQUIRE_REVALIDATION

  requirement: string

  timing:
    - PRE_ACTION
    - DURING_ACTION
    - POST_ACTION
    - COMMIT_TIME

  state:
    - UNSATISFIED
    - SATISFIED
    - WAIVED
    - UNKNOWN_GAP

  evidence_refs: []
```

---

# 34. Obligation Invariant

Mandatory pre-action obligations MUST be satisfied before action release.

```text
MandatoryPreObligation
∧
state != SATISFIED
→
not releasable
```

A post-action obligation may not necessarily block execution, but MUST remain tracked.

---

# 35. Prohibitions

Explicit prohibitions SHOULD be represented independently.

```yaml
prohibition:
  prohibition_id: string

  policy_id: string

  prohibited_operation: string

  scope: {}

  regime: {}

  exception_refs: []

  hard: true
```

This prevents prohibitions from disappearing into explanatory prose.

---

# 36. Conditions

Conditions differ from obligations.

A condition determines whether policy permission becomes valid.

An obligation describes something that must be performed as part of governed execution.

Example:

```text
CONDITION:
user approval must exist.

OBLIGATION:
record approval provenance.
```

These SHOULD remain separate.

---

# 37. Exception Model

Exceptions MUST be explicit governed objects.

```yaml
policy_exception:
  exception_id: string

  policy_id: string
  rule_id: string

  principal_scope: []
  action_scope: []
  resource_scope: []

  valid_from: null
  valid_until: null

  issuer: null

  authority_ref: null

  conditions: []

  provenance: []

  revoked: false
```

---

# 38. Exception Invariant

An exception MUST NOT broaden beyond its explicit envelope.

```text
ExceptionScope ⊆ AuthorizedExceptionScope
```

Expired or revoked exceptions MUST NOT be reused.

---

# 39. Policy Decision Scope

Every material decision SHOULD preserve:

```yaml
scope:
  principal: []
  capability: []
  provider: []
  resource: []
  operation: []
  environment: []
  domain: []
  scale: []
  jurisdiction: []
  exclusions: []
```

Empty scope does not automatically mean universal scope.

---

# 40. Regime

Policy validity may depend on regime.

```yaml
regime:
  allowed:
    - DEVELOPMENT
    - TEST

  prohibited:
    - PRODUCTION

  assumptions: []

  transition_revalidation_required: true
```

A development `ALLOW` MUST NOT silently become a production `ALLOW`.

---

# 41. Temporal Validity

Every reusable policy decision SHOULD carry temporal validity.

```yaml
freshness:
  evaluated_at: timestamp
  valid_from: timestamp
  expires_at: timestamp

  policy_registry_epoch: string
  policy_versions: {}

  invalidation_events: []
```

A policy decision is not permanently valid.

---

# 42. Freshness Invariant

If a load-bearing policy changes:

```text
PolicyVersion_now != PolicyVersion_evaluated
```

then dependent policy decisions MUST be revalidated.

Likewise for:

```text
authority change;
scope change;
regime change;
target change;
capability-contract change;
effect change;
constraint change.
```

---

# 43. Fine-Grained Read Set

Where infrastructure supports precise dependency tracking, the policy decision SHOULD preserve the authoritative policy objects actually read during evaluation.

```yaml
observed_policy_read_set:
  - object_id: "POLICY_*"
    version: string
    content_hash: string
```

Conceptually:

```text
ReadSet =
{
  (object_id, version, content_hash)
  actually observed during decision formation
}
```

A change to an unread unrelated policy SHOULD NOT invalidate the decision merely because the global registry changed.

---

# 44. Selective Invalidation

Suppose:

```text
Decision D1 depends on P1 and P2.
Decision D2 depends on P3.
```

If `P2` changes:

```text
invalidate D1
preserve D2
```

unless another dependency establishes broader impact.

This is preferred over indiscriminate global recomputation.

---

# 45. Policy Context

The policy evaluator SHOULD receive an explicit context object.

```yaml
policy_context:
  principal: {}
  request: {}
  capability: {}
  target: {}
  effect_intent: {}

  environment: {}
  session: {}

  authority_context: {}
  constraint_context: {}

  observed_state: {}

  time_context: {}

  provenance_context: {}
```

Missing load-bearing context remains a gap.

---

# 46. Authority Context

Policy evaluation MAY depend on authority state.

However, authority MUST come from an authority-governed source.

```yaml
authority_context:
  authority_id: null
  principal: null

  operation: null
  target: null

  valid_from: null
  valid_until: null

  revocation_state: UNKNOWN

  witness_ref: null
```

Policy logic MUST NOT fabricate authority.

---

# 47. Constraint Context

Policies may depend on constraints such as:

```text
legal;
security;
privacy;
resource;
safety;
temporal;
transactional;
organizational;
system integrity.
```

Recommended representation:

```yaml
constraint_context:
  constraints: []

  version: null
  hash: null

  checked_at: null
```

Constraint freshness may require commit-time revalidation.

---

# 48. Evidence

A policy decision SHOULD retain evidence supporting material predicates.

```yaml
evidence:
  evidence_id: string

  evidence_class:
    - OBSERVATION
    - SOURCE_CLAIM
    - DOCUMENT
    - SYSTEM_STATE
    - AUTHORITY_WITNESS
    - POLICY_OBJECT
    - VALIDATION_RESULT
    - USER_INPUT
    - TOOL_OBSERVATION

  source_id: string

  observed_at: null

  supports: []
  contradicts: []

  provenance: []
```

---

# 49. Evidence Sufficiency

Policy evaluation SHOULD distinguish:

```text
predicate known true;
predicate known false;
predicate unknown;
predicate conflicting.
```

A missing value MUST NOT be coerced into the value most favorable to execution.

---

# 50. Provenance

Every consequential policy decision SHOULD preserve sufficient provenance to reconstruct:

```text
which policies were evaluated;
which versions;
which rules fired;
which context was used;
which evidence supported predicates;
which authority witness was consulted;
which constraints were observed;
when evaluation occurred;
which evaluator produced the decision.
```

---

# 51. Provenance Object

```yaml
provenance:
  evaluator_id: string
  evaluator_version: string

  policy_refs: []
  policy_versions: {}

  evidence_refs: []

  authority_refs: []
  constraint_refs: []

  source_ancestry: []

  evaluation_time: null

  environment: null

  transaction_id: null
```

---

# 52. Provenance Independence

Multiple policy interpretations derived from one underlying source MUST NOT be treated as independent policy authority.

For:

```text
P1 ← Source S
P2 ← Source S
P3 ← Source S
```

the existence of three policy objects does not establish three independent governing sources.

Where material, ancestry SHOULD remain visible.

---

# 53. Decision Reason Codes

Machine-readable reason codes SHOULD accompany policy decisions.

Examples:

```text
ALLOW_POLICY_SATISFIED

DENY_EXPLICIT_PROHIBITION
DENY_EFFECT_CLASS
DENY_RESOURCE_SCOPE
DENY_PRINCIPAL_SCOPE
DENY_REGIME
DENY_REVOKED_EXCEPTION

CONDITIONAL_APPROVAL_REQUIRED
CONDITIONAL_REDACTION_REQUIRED
CONDITIONAL_RECEIPT_REQUIRED

ESCALATE_HIGH_CONSEQUENCE
ESCALATE_POLICY_AMBIGUITY
ESCALATE_AUTHORITY_REQUIRED

REVALIDATE_POLICY_CHANGED
REVALIDATE_AUTHORITY_CHANGED
REVALIDATE_SCOPE_CHANGED
REVALIDATE_EFFECT_CHANGED

CONFLICT_POLICY_PRECEDENCE
CONFLICT_JURISDICTION

UNKNOWN_POLICY_COVERAGE
UNKNOWN_APPLICABILITY
UNKNOWN_AUTHORITY
UNKNOWN_SCOPE
UNKNOWN_REGIME
UNKNOWN_EVIDENCE
```

Reason codes SHOULD NOT replace explanatory provenance.

---

# 54. Policy Decision Explanation

The decision MAY expose a concise explanation:

```yaml
explanation:
  summary: >
    Operation is conditionally permitted under POLICY_X,
    subject to approval and commit-time authority revalidation.

  decisive_rules:
    - "POLICY_X:R12"

  unresolved:
    - "commit authority freshness"
```

The explanation MUST reflect the structured decision.

It MUST NOT override it.

---

# 55. Decision Hash

A policy decision MAY be cryptographically or deterministically bound to its relevant inputs.

Conceptually:

```text
DecisionHash =
H(
    principal
  || action
  || target
  || effect_digest
  || policy_read_set
  || scope
  || regime
  || context
  || decision
)
```

The exact hashing scheme is implementation-dependent.

The purpose is to prevent reuse of a policy decision for a materially different action.

---

# 56. Decision Binding

A policy decision for:

```text
WRITE(resource_A, payload_X)
```

MUST NOT automatically authorize:

```text
WRITE(resource_B, payload_X)
```

or:

```text
WRITE(resource_A, payload_Y)
```

unless the policy decision's explicit scope covers those variants.

---

# 57. Parameter Binding

Consequential policy decisions SHOULD bind to normalized action parameters or a canonical parameter digest.

```yaml
binding:
  operation: string
  target_id: string
  parameters_hash: string
  effect_digest: string
```

Parameter mutation after evaluation requires revalidation when policy-sensitive.

---

# 58. Capability Binding

If policy depends on capability characteristics, the decision SHOULD bind to the resolved capability contract.

```yaml
capability_binding:
  capability_id: string
  capability_version: string
  provider_id: string
  resolved_contract_hash: string
```

A provider substitution may therefore invalidate policy applicability.

---

# 59. Observability Requirements

Policy MAY impose observability obligations.

Example:

```yaml
observability_requirements:
  require:
    - action_log
    - provenance_record
    - effect_digest
    - authority_witness
    - receiver_receipt
```

However:

```text
POLICY REQUIRES OBSERVABILITY
```

does not prove:

```text
OBSERVABILITY IS ACTUALLY PRESENT
```

Coverage MUST be validated by the infrastructure/control plane.

---

# 60. Policy and Effect Release

Policy `ALLOW` is not effect release.

For durable or external effects:

```text
POLICY_ALLOW
      ↓
AUTHORITY_VALID
      ↓
CONSTRAINTS_VALID
      ↓
OBSERVABILITY_VALID
      ↓
TRANSACTION_VALID
      ↓
RELEASE_LEDGER_VALID
      ↓
COMMITTABLE
```

Any required gate may still block release.

---

# 61. Durable Effect Boundary

For persistent/external/model-promotion effects, the control plane SHOULD revalidate at commit time at least the load-bearing:

```text
policy state;
authority state;
effect identity;
transaction identity;
constraint state;
observed authoritative read set;
release-ledger state;
observability envelope.
```

This protects against stale preflight decisions.

---

# 62. Proposal vs Commit

Policy may permit a system to generate a proposal without permitting the proposal to be committed.

Example:

```text
ALLOW_PROPOSAL
```

may coexist with:

```text
COMMIT_REQUIRES_HUMAN_AUTHORITY
```

Therefore:

```text
ProposalPermission != CommitPermission
```

---

# 63. Effect Classes

Policy MAY discriminate by effect class.

Recommended base effect classes:

```text
E0_READ_ONLY

E1_EPHEMERAL_STATE

E2_REVERSIBLE_LOCAL_WRITE

E3_PERSISTENT_WRITE

E4_EXTERNAL_COMMUNICATION

E5_RESOURCE_OR_FINANCIAL_EFFECT

E6_SECURITY_OR_AUTHORITY_EFFECT

E7_HIGH_CONSEQUENCE_OR_IRREVERSIBLE_EFFECT
```

Higher consequence MAY require stronger policy conditions.

---

# 64. Consequence-Aware Escalation

A policy may require escalation based on:

```text
irreversibility;
financial magnitude;
privacy sensitivity;
security impact;
external visibility;
institutional impact;
legal exposure;
safety consequence;
downstream dependency fan-out.
```

Example:

```yaml
escalation:
  trigger:
    effect_class:
      - E6_SECURITY_OR_AUTHORITY_EFFECT
      - E7_HIGH_CONSEQUENCE_OR_IRREVERSIBLE_EFFECT

  destination:
    - HUMAN_AUTHORITY
```

---

# 65. Decision Finality

A policy decision is final only relative to its policy-evaluation scope.

It is not necessarily final relative to:

```text
authority;
execution;
external effect completion;
transaction commit;
receiver acknowledgement;
system state.
```

Use explicit terminology:

```text
POLICY_FINAL
```

rather than generic:

```text
FINAL
```

where ambiguity is possible.

---

# 66. Receiver Completion

A policy decision MAY require receiver-attested completion for external effects.

But:

```text
receipt_id exists
```

is not sufficient evidence of completion.

Where receiver attestation is required, the infrastructure SHOULD verify:

```text
receiver/service identity;
effect digest;
idempotency key;
transaction identity;
authority identity;
principal;
operation;
signature/trust status;
temporal validity.
```

---

# 67. Idempotency Policy

Policy MAY require stable idempotency for durable effects.

```yaml
idempotency:
  required: true
  key_required: true
  duplicate_dispatch_prohibited: true
```

Policy can require this property.

Infrastructure must enforce the actual release state.

---

# 68. Ambiguous Externalization

If an external effect may have occurred but completion cannot be established:

```text
EXTERNALIZED_UNKNOWN
```

the system SHOULD NOT blindly retry merely because policy still says `ALLOW`.

The appropriate state may be:

```text
RECONCILE
```

before another dispatch.

---

# 69. Cached Policy Decisions

Policy decisions MAY be cached only when reuse conditions remain valid.

Cache record:

```yaml
policy_decision_cache:
  decision_id: string

  decision_hash: string

  principal_id: string
  operation: string
  target_id: string

  policy_read_set: []

  evaluated_at: null
  expires_at: null

  invalidation_conditions: []
```

---

# 70. Cache Reuse Invariant

A cached policy decision MUST NOT be reused when a load-bearing binding changed.

Examples:

```text
principal changed;
target changed;
operation changed;
effect digest changed;
policy changed;
authority changed;
regime changed;
scope changed;
capability contract changed;
exception revoked.
```

---

# 71. Policy Decision Operators

The policy-decision architecture SHOULD support the following conceptual operators.

## `DISCOVER_POLICY`

```text
DISCOVER_POLICY(context)
→ CandidatePolicySet
```

---

## `RESOLVE_APPLICABILITY`

```text
RESOLVE_APPLICABILITY(policy, context)
→ ApplicabilityResult
```

---

## `EVALUATE_POLICY`

```text
EVALUATE_POLICY(policy, context)
→ PolicyEvaluation
```

---

## `COMPOSE_POLICY_RESULTS`

```text
COMPOSE_POLICY_RESULTS({D1 ... Dn})
→ PolicyDecision
```

---

## `VALIDATE_DECISION`

```text
VALIDATE_DECISION(decision)
→ VALID | INVALID | UNKNOWN_GAP
```

---

## `REVALIDATE_DECISION`

```text
REVALIDATE_DECISION(decision, current_state)
→ PolicyDecision'
```

---

## `INVALIDATE_DECISION`

```text
INVALIDATE_DECISION(decision, failed_dependency)
```

---

## `ESCALATE_DECISION`

```text
ESCALATE_DECISION(decision, authority_target)
```

---

## `SUPERSEDE_DECISION`

```text
SUPERSEDE_DECISION(old_decision, new_decision)
```

---

# 72. State Variables

Recommended policy-decision state variables:

```text
D_id       decision identity
P          principal
A          requested action
C          capability
T          target/resource
E          effect intent
Π          discovered policy set
Π*         applicable policy set
R          individual rule evaluations
Ω          obligations
X          prohibitions
K          conditions
S          scope
G          regime
Au         authority context
Ct         constraint context
Pr         provenance
F          freshness
U          uncertainty vector
Y          final policy decision
```

Conceptually:

```text
Y =
PolicyCompose(
    P,
    A,
    C,
    T,
    E,
    Π*,
    R,
    Ω,
    X,
    K,
    S,
    G,
    Au,
    Ct,
    F
)
```

This is an AMOS MODEL representation, not a claim of a universal mathematical policy law.

---

# 73. Decision Sufficiency

A policy decision is structurally sufficient only when the information required to determine its policy-local result is available.

Conceptually:

```text
PolicySufficient =
IdentityValid
∧ RequestBound
∧ ApplicablePoliciesResolved
∧ LoadBearingPredicatesResolved
∧ ConflictsResolvedOrPreserved
∧ ScopeKnown
∧ RegimeKnown
∧ FreshnessValid
```

If a required term is unresolved:

```text
PolicySufficient = false
```

---

# 74. Confidence Ceiling

The confidence of a policy decision MUST NOT exceed its weakest load-bearing premise unless independently revalidated.

Conceptually:

```text
C_policy ≤ min(
    C_policy_identity,
    C_applicability,
    C_context,
    C_scope,
    C_regime,
    C_evidence,
    C_freshness,
    C_composition
)
```

This is an AMOS MODEL governance equation.

It is not an empirically calibrated probability unless calibration evidence exists.

---

# 75. Uncertainty Vector

Recommended representation:

```yaml
uncertainty:
  policy_identity: null
  applicability: null
  interpretation: null
  evidence: null
  scope: null
  regime: null
  temporal: null
  authority: null
  constraint: null
  provenance_independence: null
```

Uncertainty SHOULD remain multidimensional where collapsing it would hide a decision-relevant weakness.

---

# 76. Policy Decision Invariants

## INV-PD-001 — Explicit Decision

Every completed policy evaluation MUST produce an explicit state.

---

## INV-PD-002 — No Capability-to-Permission Collapse

```text
CAPABILITY != POLICY_ALLOW
```

---

## INV-PD-003 — No Policy-to-Authority Collapse

```text
POLICY_ALLOW != AUTHORITY
```

---

## INV-PD-004 — No Allow-to-Commit Collapse

```text
ALLOW != COMMIT
```

---

## INV-PD-005 — Unknown Is Not Pass

```text
UNKNOWN_GAP != ALLOW
```

---

## INV-PD-006 — Scope Preservation

A decision MUST NOT be reused outside its validated scope.

---

## INV-PD-007 — Regime Preservation

A decision MUST NOT be reused across incompatible regimes without revalidation.

---

## INV-PD-008 — Version Binding

Material decisions MUST preserve load-bearing policy versions.

---

## INV-PD-009 — Conflict Visibility

Unresolved policy conflict MUST remain visible.

---

## INV-PD-010 — No Silent Override

Overrides require explicit authority and policy basis.

---

## INV-PD-011 — Condition Preservation

Unsatisfied mandatory conditions prevent unconditional `ALLOW`.

---

## INV-PD-012 — Obligation Preservation

Mandatory obligations MUST survive downstream handoff.

---

## INV-PD-013 — Provenance Preservation

Material decisions MUST preserve reconstructable policy provenance.

---

## INV-PD-014 — Freshness Preservation

Stale policy decisions MUST NOT masquerade as current.

---

## INV-PD-015 — Parameter Binding

Material parameter changes require revalidation when policy-sensitive.

---

## INV-PD-016 — Effect Binding

Policy approval for one effect MUST NOT automatically transfer to a different effect.

---

## INV-PD-017 — Selective Invalidation

Only conclusions dependent on a failed premise SHOULD be invalidated unless broader dependency exists.

---

## INV-PD-018 — Revocation Dominance

Revoked exceptions or authority MUST NOT remain effective through stale cached decisions.

---

## INV-PD-019 — No Evidence Inflation

Correlated evidence MUST NOT be counted as independent confirmation.

---

## INV-PD-020 — Proposal/Commit Separation

Permission to propose an effect MUST NOT be interpreted as permission to commit it.

---

# 77. Failure Modes

## FM-PD-001 — Missing Policy

A governing policy exists but is not discovered.

---

## FM-PD-002 — False Applicability

A policy is applied outside its scope.

---

## FM-PD-003 — Missed Applicability

A governing policy is incorrectly classified `NOT_APPLICABLE`.

---

## FM-PD-004 — Stale Decision

An old decision is reused after a load-bearing change.

---

## FM-PD-005 — Scope Leakage

A narrow policy result is generalized.

---

## FM-PD-006 — Regime Leakage

A decision crosses environments or regimes without validation.

---

## FM-PD-007 — Authority Smuggling

Policy `ALLOW` is treated as authority.

---

## FM-PD-008 — Capability Smuggling

Capability availability is treated as policy permission.

---

## FM-PD-009 — Commit Smuggling

Policy permission is treated as durable commit authority.

---

## FM-PD-010 — Conflict Suppression

Incompatible policies are silently collapsed.

---

## FM-PD-011 — Unknown Suppression

Missing policy information is treated as permission.

---

## FM-PD-012 — Exception Expansion

A narrow exception is applied broadly.

---

## FM-PD-013 — Revoked Exception Reuse

A revoked exception survives through cache or stale state.

---

## FM-PD-014 — Policy Version Drift

Decision provenance points to the wrong policy version.

---

## FM-PD-015 — Parameter Drift

Action parameters change after policy evaluation.

---

## FM-PD-016 — Target Drift

The target changes while the decision is reused.

---

## FM-PD-017 — Effect Drift

The actual effect differs from the evaluated effect intent.

---

## FM-PD-018 — Obligation Loss

Required obligations disappear between policy evaluation and execution.

---

## FM-PD-019 — Provenance Loss

The basis of the decision cannot be reconstructed.

---

## FM-PD-020 — Precedence Error

Policies are ordered using an invalid hierarchy.

---

## FM-PD-021 — Override Forgery

An override is accepted without valid authority.

---

## FM-PD-022 — Correlated Policy Inflation

Multiple derivatives of one source are treated as independent governing authority.

---

## FM-PD-023 — Cached Allow Resurrection

A revoked or changed policy state is bypassed through an old `ALLOW`.

---

## FM-PD-024 — Policy/Runtime Divergence

The runtime performs an action inconsistent with the recorded policy decision.

---

## FM-PD-025 — Post-Evaluation Mutation

The proposal changes after policy evaluation without revalidation.

---

# 78. Repair / Recovery

Canonical repair sequence:

```text
DETECT POLICY DECISION FAILURE
        ↓
FREEZE AFFECTED DECISION
        ↓
PRESERVE DECISION + EVIDENCE
        ↓
IDENTIFY FAILED PREMISE / POLICY / EDGE
        ↓
INVALIDATE DEPENDENT RESULT
        ↓
PRESERVE UNAFFECTED RESULTS
        ↓
REFRESH POLICY / CONTEXT / AUTHORITY
        ↓
RE-EVALUATE APPLICABILITY
        ↓
RE-COMPOSE POLICY RESULTS
        ↓
REVALIDATE
        ↓
RESTORE / SUPERSEDE / DENY / ESCALATE
```

Do not rerun the same failed path without changed evidence or state.

---

# 79. Repair Principle

Repair SHOULD target the smallest causal failure.

If:

```text
D depends on P1, P2, P3
```

and only:

```text
P2 version changed
```

then re-evaluate the dependencies affected by `P2`.

Do not automatically discard unrelated valid evidence.

---

# 80. Rollback

If an invalid policy decision influenced a staged but uncommitted action:

```text
discard or regenerate proposal
```

If it influenced a committed reversible effect:

```text
invoke governed compensation / rollback where authorized
```

If it influenced an irreversible effect:

```text
record incident
preserve provenance
contain downstream effects where possible
escalate
```

Policy repair MUST NOT pretend an irreversible effect never occurred.

---

# 81. Tests / Validators

Minimum policy-decision test surface:

```text
T-PD-001 schema validity

T-PD-002 explicit decision state

T-PD-003 policy identity resolution

T-PD-004 policy version binding

T-PD-005 applicability resolution

T-PD-006 scope matching

T-PD-007 regime matching

T-PD-008 principal binding

T-PD-009 action binding

T-PD-010 target binding

T-PD-011 effect binding

T-PD-012 deny handling

T-PD-013 conditional handling

T-PD-014 escalation handling

T-PD-015 unknown-not-pass

T-PD-016 conflict preservation

T-PD-017 precedence resolution

T-PD-018 exception validation

T-PD-019 exception expiry

T-PD-020 exception revocation

T-PD-021 obligation preservation

T-PD-022 prohibition preservation

T-PD-023 freshness validation

T-PD-024 cache invalidation

T-PD-025 selective invalidation

T-PD-026 authority separation

T-PD-027 capability separation

T-PD-028 proposal/commit separation

T-PD-029 provenance reconstruction

T-PD-030 correlated-provenance detection

T-PD-031 policy-read-set validation

T-PD-032 post-evaluation mutation detection

T-PD-033 control-plane handoff

T-PD-034 effect-class escalation

T-PD-035 stale-allow rejection

T-PD-036 revoked-authority rejection

T-PD-037 provider substitution revalidation

T-PD-038 scope-wildcard protection

T-PD-039 regime-wildcard protection

T-PD-040 policy/runtime consistency
```

---

# 82. Schema Validator

The schema validator SHOULD reject consequential policy decisions missing:

```text
decision_id;
principal;
action;
policy references;
policy versions;
decision state;
scope;
regime;
evaluation time;
provenance;
reason basis.
```

unless explicitly classified:

```text
UNKNOWN_GAP
```

---

# 83. Semantic Validator

Structural schema validity is insufficient.

Semantic validation SHOULD inspect:

```text
contradictory decision states;
ALLOW with unsatisfied mandatory conditions;
ALLOW despite unresolved hard deny;
expired exceptions;
revoked exceptions;
scope contradictions;
regime contradictions;
invalid precedence;
policy-version mismatch;
authority leakage;
commit leakage;
missing effect binding.
```

---

# 84. Commit-Time Validator

For durable effects, commit-time validation SHOULD test whether the policy decision remains applicable to the exact staged effect.

Conceptually:

```text
CurrentPolicyReadSet == PreparedPolicyReadSet
AND
CurrentEffectDigest == PreparedEffectDigest
AND
CurrentPrincipal == PreparedPrincipal
AND
CurrentTarget == PreparedTarget
AND
CurrentScope compatible
AND
CurrentRegime compatible
```

where each comparison is scoped to load-bearing dependencies rather than irrelevant global state.

---

# 85. Adversarial Validator

For high-consequence decisions, validation SHOULD challenge:

```text
Was a governing policy omitted?

Was applicability interpreted too narrowly?

Is the ALLOW based on stale state?

Did a lower policy weaken a higher constraint?

Was an exception overextended?

Did authority expire?

Did the effect change after evaluation?

Are apparently independent policies descendants of one source?

Did an UNKNOWN become an implicit PASS?

Did the decision cross scope or regime?

Could a stronger applicable prohibition exist?
```

A successful challenge requires downgrade, revalidation, conflict preservation, escalation, or denial as appropriate.

---

# 86. Falsifiers

A policy decision claim is falsified if reliable evidence establishes that:

```text
an applicable hard prohibition was ignored;

a required policy was omitted;

the policy version used was incorrect;

a policy had already been superseded;

the policy was outside its validity period;

the principal did not match the evaluated principal;

the target differed from the evaluated target;

the actual operation differed from the evaluated operation;

the effect differed materially from the evaluated effect;

a mandatory condition was unsatisfied;

an exception was invalid, expired, or revoked;

policy precedence was incorrectly applied;

a conflict was suppressed;

an UNKNOWN was treated as ALLOW;

the recorded provenance cannot reconstruct the decision;

or runtime behavior violated the recorded decision.
```

---

# 87. Decision Query Surface

AMOS SHOULD be able to query policy decisions by:

```text
decision ID;
principal;
action;
capability;
provider;
target;
resource;
policy;
policy version;
decision state;
effect class;
transaction;
session;
scope;
regime;
time;
authority;
unresolved gap;
obligation;
exception;
supersession lineage.
```

---

# 88. Decision Audit Surface

An auditor SHOULD be able to answer:

1. What action was evaluated?
2. Who requested it?
3. Against which target?
4. Through which capability/provider?
5. Which policies were discovered?
6. Which were applicable?
7. Which were excluded?
8. Why were they excluded?
9. Which rules fired?
10. Which policies denied?
11. Which policies allowed?
12. Which conditions remained?
13. Which obligations were created?
14. Which exception was used?
15. Was the exception valid?
16. Which precedence rule resolved conflicts?
17. What evidence supported the decision?
18. What policy versions were used?
19. What was the scope?
20. What was the regime?
21. When was the decision evaluated?
22. Is it still fresh?
23. Was authority independently checked?
24. Was the effect identical at commit?
25. Was the decision reused?
26. Were load-bearing dependencies unchanged?
27. Was the action ultimately committed?
28. If committed, under what authority?
29. What receipt or effect evidence exists?
30. What could falsify the decision?

---

# 89. H/M/L Applicability

The policy-decision architecture applies across AMOS H/M/L scales.

## H — Governing / System Scale

Examples:

```text
enterprise policy;
system-wide safety policy;
constitutional constraint;
cross-domain authority rule;
global effect-class restriction;
canon governance.
```

H-level policy may constrain M and L decisions.

---

## M — Subsystem / Workflow Scale

Examples:

```text
workflow policy;
agent coordination policy;
memory-write policy;
tool-routing policy;
domain-control policy;
transaction policy.
```

M-level policy SHOULD remain compatible with governing H-level constraints.

---

## L — Local Operation Scale

Examples:

```text
specific tool call;
specific resource read;
specific memory write;
specific message send;
specific transaction effect.
```

L-level decisions provide concrete execution-policy results.

---

# 90. Cross-Scale Invariant

Lower-scale policy decisions MUST NOT silently weaken higher-scale governing constraints.

Conceptually:

```text
Allowed_L
⊆
Allowed_M
⊆
Allowed_H
```

where the policy hierarchy defines tightening inheritance.

This relationship is not universal across all conceivable policies; it applies where AMOS policy inheritance is explicitly defined.

---

# 91. Agent Roles

Recommended agent roles:

```text
POLICY_DISCOVERY_AGENT
POLICY_APPLICABILITY_AGENT
POLICY_EVALUATION_AGENT
POLICY_CONFLICT_AUDITOR
POLICY_PROVENANCE_AUDITOR
POLICY_REVALIDATION_AGENT
```

These are architectural roles.

They do not imply autonomous authority.

An agent may propose a policy decision.

The control plane remains responsible for enforcing governing boundaries.

---

# 92. Skill Roles

Relevant Skill classes MAY include:

```text
policy interpretation;
policy registry resolution;
authority verification;
provenance validation;
constraint propagation;
scope/regime validation;
conflict resolution;
commit-time authorization;
effect-release validation.
```

A Skill's presence does not prove implementation or authority.

---

# 93. Workflow

Canonical policy-decision workflow:

```text
1. RECEIVE TASK / EFFECT INTENT

2. NORMALIZE PRINCIPAL

3. NORMALIZE ACTION

4. RESOLVE TARGET / RESOURCE

5. RESOLVE CAPABILITY CONTRACT

6. DISCOVER POTENTIALLY GOVERNING POLICIES

7. VERIFY POLICY IDENTITY + VERSION

8. RESOLVE POLICY APPLICABILITY

9. LOAD MINIMUM REQUIRED CONTEXT

10. EVALUATE INDIVIDUAL POLICY RULES

11. PRESERVE UNKNOWN PREDICATES

12. COLLECT OBLIGATIONS / PROHIBITIONS / CONDITIONS

13. DETECT CONFLICTS

14. APPLY VALID PRECEDENCE / SUPERSESSION

15. COMPOSE POLICY RESULT

16. BIND RESULT TO ACTION / TARGET / EFFECT

17. RECORD POLICY READ SET

18. RECORD PROVENANCE

19. SET FRESHNESS ENVELOPE

20. EMIT POLICY_DECISION

21. HAND OFF TO CONTROL PLANE

22. REVALIDATE LOAD-BEARING POLICY STATE AT COMMIT

23. INVALIDATE / RECOMPUTE IF NECESSARY
```

---

# 94. Protocol

Recommended request:

```yaml
policy_decision_request:
  request_id: string

  principal: {}

  action: {}

  capability: {}

  target: {}

  effect_intent: {}

  context: {}

  authority_context: {}

  constraint_context: {}

  requested_at: timestamp
```

Recommended response:

```yaml
policy_decision_response:
  request_id: string

  decision_id: string

  decision:
    state: string
    reason_codes: []

  applicable_policies: []

  obligations: []
  prohibitions: []
  conditions: []

  conflicts: []

  unresolved: []

  scope: {}
  regime: {}

  freshness: {}

  provenance: {}

  confidence_ceiling: null
```

---

# 95. Control-Plane Return Mapping

The policy layer itself MAY use:

```text
ALLOW
DENY
CONDITIONAL
ESCALATE
REVALIDATE
CONFLICT
UNKNOWN_GAP
```

The infrastructure/control plane may translate these into stronger runtime states such as:

```text
COMMITTABLE

BLOCK_POLICY

BLOCK_AUTHORITY

BLOCK_CONFLICT

BLOCK_EVIDENCE

BLOCK_OBSERVABILITY

BLOCK_SEMANTIC_TRANSACTION

REVALIDATE_STALE_READ

REVALIDATE_CONSTRAINTS

REVALIDATE_OBSERVABILITY

REVALIDATE_EFFECT_LEDGER

RECONCILE_EFFECT

UNKNOWN_GAP
```

The policy decision MUST NOT falsely claim those infrastructure states unless it actually owns that control-plane responsibility.

---

# 96. Policy Decision Example — Read

```yaml
policy_decision:
  identity:
    decision_id: "PD_EXAMPLE_READ_001"
    version: "1.0.0"

  subject:
    principal_id: "AGENT_EXAMPLE"
    principal_type: AGENT

  request:
    action: READ
    operation: "read_resource"
    capability_id: "CAP_RESOURCE_READ"
    provider_id: "PROVIDER_EXAMPLE"
    target_id: "RESOURCE_001"
    effect_class: "E0_READ_ONLY"

  policies:
    applicable:
      - policy_id: "POLICY_RESOURCE_READ"
        version: "1.0.0"

  evaluations:
    - policy_id: "POLICY_RESOURCE_READ"
      result: ALLOW
      obligations:
        - RECORD_PROVENANCE

  composition:
    strategy: "single_applicable_policy"

  obligations:
    - obligation_id: "OBL_001"
      type: RECORD_PROVENANCE
      timing: POST_ACTION
      state: UNSATISFIED

  decision:
    state: ALLOW
    reason_codes:
      - ALLOW_POLICY_SATISFIED

  authority:
    state: UNKNOWN

  provenance:
    policy_versions:
      - "POLICY_RESOURCE_READ@1.0.0"

  confidence_ceiling: 0
```

The example remains structurally illustrative.

It does not assert runtime validation.

---

# 97. Policy Decision Example — Conditional Write

```yaml
policy_decision:
  identity:
    decision_id: "PD_EXAMPLE_WRITE_001"
    version: "1.0.0"

  subject:
    principal_id: "AGENT_EXAMPLE"
    principal_type: AGENT

  request:
    action: WRITE
    operation: "persistent_write"
    capability_id: "CAP_EXAMPLE_WRITE"
    target_id: "RESOURCE_001"
    effect_class: "E3_PERSISTENT_WRITE"

  policies:
    applicable:
      - policy_id: "POLICY_PERSISTENT_WRITE"
        version: "1.0.0"

  evaluations:
    - policy_id: "POLICY_PERSISTENT_WRITE"
      result: CONDITIONAL

      conditions:
        - "valid write authority"
        - "commit-time revalidation"

      obligations:
        - "record provenance"
        - "record transaction identity"

  conditions:
    - condition_id: "COND_AUTH"
      requirement: "valid write authority"
      state: UNSATISFIED

    - condition_id: "COND_COMMIT"
      requirement: "commit-time revalidation"
      state: UNSATISFIED

  decision:
    state: CONDITIONAL

    reason_codes:
      - CONDITIONAL_APPROVAL_REQUIRED

  confidence_ceiling: 0
```

This MUST NOT be interpreted as authorization to write.

---

# 98. Policy Decision Example — Conflict

```yaml
policy_decision:
  identity:
    decision_id: "PD_EXAMPLE_CONFLICT_001"

  evaluations:
    - policy_id: "POLICY_A"
      result: ALLOW

    - policy_id: "POLICY_B"
      result: DENY

  composition:
    conflicts:
      - policies:
          - POLICY_A
          - POLICY_B

        type: "ALLOW_DENY_CONFLICT"

        precedence_resolution: UNKNOWN_GAP

  decision:
    state: CONFLICT

    reason_codes:
      - CONFLICT_POLICY_PRECEDENCE

  confidence_ceiling: 0
```

AMOS MUST preserve the conflict until discriminating governance evidence exists.

---

# 99. Policy Decision Example — Stale Allow

Prepared state:

```yaml
decision:
  state: ALLOW

freshness:
  policy_versions:
    POLICY_X: "1.0.0"
```

Current state:

```yaml
current_policy_versions:
  POLICY_X: "2.0.0"
```

If `POLICY_X` was load-bearing:

```text
ALLOW
    ↓
REVALIDATE
```

not:

```text
ALLOW
    ↓
COMMIT
```

---

# 100. Promotion Model

Recommended maturity path:

```text
PLACEHOLDER
    ↓
STRUCTURAL MODEL
    ↓
SCHEMA VALIDATED
    ↓
POLICY REGISTRY INTEGRATED
    ↓
EXECUTABLE EVALUATOR
    ↓
TESTED
    ↓
INTEGRATION VALIDATED
    ↓
ADVERSARIALLY VALIDATED
    ↓
GOVERNED ACTIVE
```

No stage automatically implies the next.

---

# 101. Promotion Requirements

## Structural Model → Schema Validated

Requires:

```text
machine-readable schema;
decision enum validation;
required-field validation;
policy-reference validation.
```

## Schema Validated → Registry Integrated

Requires:

```text
policy identity resolution;
version resolution;
supersession support;
applicability lookup.
```

## Registry Integrated → Executable Evaluator

Requires:

```text
deterministic or governed evaluation semantics;
predicate handling;
conflict handling;
unknown handling.
```

## Executable Evaluator → Tested

Requires executed tests.

## Tested → Integration Validated

Requires cross-component validation with:

```text
capability resolution;
authority;
control plane;
provenance;
transaction;
effect release.
```

## Integration Validated → Governed Active

Requires:

```text
authority boundary validated;
rollback/recovery;
observability;
freshness handling;
security review;
no unresolved critical gaps.
```

---

# 102. No Automatic Promotion

The following transitions are prohibited without evidence:

```text
MODEL → IMPLEMENTED

IMPLEMENTED → VALIDATED

ALLOW → AUTHORIZED

ALLOW → COMMITTABLE

TEST_PASS → UNIVERSALLY_VALID

STRUCTURALLY_COMPLETE → CANONICAL
```

---

# 103. Gap Classification

Policy-decision gaps SHOULD be classified:

```text
CRITICAL
DECISION_RELEVANT
EXPLANATORY
COSMETIC
```

Example:

```yaml
gap:
  gap_id: "GAP_PD_001"

  class: CRITICAL

  field: "policy_precedence"

  description: >
    Two applicable policies conflict and no canonical
    precedence rule has been established.

  blocks:
    - ALLOW
    - COMMIT

  required_resolution:
    - "canonical precedence evidence"
```

---

# 104. Critical Gaps

Critical policy-decision gaps include unresolved:

```text
governing policy identity;
hard prohibition;
authority boundary;
effect class;
policy precedence;
scope;
regime;
exception validity;
commit requirement;
security restriction;
irreversible-action condition.
```

Critical gaps MUST NOT be downgraded for fluency or convenience.

---

# 105. Gap Matrix

| Surface                     |                      Required | Current Specification State |
| --------------------------- | ----------------------------: | --------------------------- |
| Decision identity           |                           Yes | Defined                     |
| Principal                   |                           Yes | Defined                     |
| Action                      |                           Yes | Defined                     |
| Target/resource             |                           Yes | Defined                     |
| Capability binding          |                Material cases | Defined                     |
| Effect intent               |               Effectful cases | Defined                     |
| Policy discovery            |                           Yes | Defined                     |
| Applicability               |                           Yes | Defined                     |
| Individual evaluation       |                           Yes | Defined                     |
| Composition                 |                           Yes | Defined                     |
| Precedence                  |                           Yes | Defined structurally        |
| Conditions                  |                           Yes | Defined                     |
| Obligations                 |                           Yes | Defined                     |
| Prohibitions                |                           Yes | Defined                     |
| Exceptions                  |                           Yes | Defined                     |
| Scope                       |                           Yes | Defined                     |
| Regime                      |                           Yes | Defined                     |
| Freshness                   |                           Yes | Defined                     |
| Read-set binding            |           Consequential reuse | Defined                     |
| Authority separation        |                           Yes | Defined                     |
| Control-plane separation    |                           Yes | Defined                     |
| Effect-release separation   |                           Yes | Defined                     |
| Provenance                  |                           Yes | Defined                     |
| Uncertainty                 |                           Yes | Defined                     |
| Failure modes               |                           Yes | Defined                     |
| Repair                      |                           Yes | Defined                     |
| Tests                       |                           Yes | Defined                     |
| Falsifiers                  |                           Yes | Defined                     |
| Executable implementation   |          Required for runtime | UNKNOWN/GAP                 |
| Canonical policy population |   Required for full operation | UNKNOWN/GAP                 |
| Executed validator results  |       Required for validation | UNKNOWN/GAP                 |
| Canon admission             | Required for canonical status | UNKNOWN/GAP                 |

---

# 106. RSCF Binding

Recommended RSCF representation:

```yaml
rscf:
  claim:
    id: "RSCF_POLICY_DECISION"
    class: MODEL

    text: >
      Under policy set Π, scope S, regime G, principal P,
      action A, target T, and evaluation context C,
      the policy layer returns decision D.

  premises:
    - policy_identity_valid
    - policy_versions_valid
    - applicability_resolved
    - action_bound
    - target_bound
    - scope_valid
    - regime_valid
    - composition_valid

  evidence: []

  provenance: []

  scope: {}

  regime: {}

  freshness: null

  dependencies: []

  competing: []

  falsifiers: []

  confidence_ceiling: 0
```

---

# 107. RSCF Conclusion Classes

Policy-related claims SHOULD use the weakest accurate class:

```text
VERIFIED
DERIVED
MODEL
CONDITIONAL
COMPETING
UNKNOWN/GAP
```

Examples:

```text
MODEL:
proposed policy composition semantics.

DERIVED:
decision deterministically derived from validated policy objects.

CONDITIONAL:
policy decision depends on unresolved approval.

COMPETING:
two unresolved policy interpretations remain viable.

UNKNOWN/GAP:
governing policy cannot be determined.
```

---

# 108. GMEF Binding

Changes to policy-decision semantics SHOULD enter governed evolution when they modify:

```text
decision states;
precedence;
override rules;
applicability;
effect classes;
authority interaction;
commit requirements;
exception semantics;
unknown handling;
conflict handling;
freshness;
revocation;
provenance requirements.
```

A seemingly small change to `ALLOW` semantics may materially change the system's authority boundary and therefore requires stronger governance than a cosmetic schema change.

---

# 109. Policy Decision Change Record

```yaml
policy_decision_change:
  change_id: string

  artifact: "POLICY_DECISION.md"

  from_version: string
  to_version: string

  semantic_change: true

  affected_surfaces:
    - decision_state
    - applicability
    - authority_boundary

  evidence_refs: []

  validators_required: []

  rollback_plan: null

  approval_state: PROPOSED
```

---

# 110. Security Requirements

The policy-decision layer SHOULD defend against:

```text
policy injection;
policy deletion;
policy downgrade;
policy-version rollback;
exception forgery;
exception widening;
authority smuggling;
scope widening;
regime widening;
effect understatement;
decision-cache poisoning;
decision replay;
decision substitution;
provenance deletion;
conflict suppression;
unknown-to-allow coercion;
post-evaluation parameter mutation.
```

---

# 111. Replay Protection

A policy decision SHOULD NOT be replayed against a materially different transaction.

Where necessary, bind:

```text
decision_id
transaction_id
principal
operation
target
effect_digest
policy_read_set
authority context
```

Replay validity must be explicitly evaluated.

---

# 112. Policy Decision Persistence

Persistent policy decisions SHOULD retain enough state for later audit.

At minimum:

```text
decision identity;
principal;
operation;
target;
decision;
policy IDs/versions;
rule IDs;
scope;
regime;
evaluation timestamp;
provenance;
conditions;
obligations;
conflicts;
invalidation state.
```

Persistence does not imply permanent validity.

---

# 113. Decision Lifecycle

Recommended lifecycle:

```text
CREATED
   ↓
EVALUATING
   ↓
RESOLVED
   ↓
ACTIVE
   ↓
CONSUMED
```

Possible side transitions:

```text
EVALUATING → UNKNOWN_GAP
EVALUATING → CONFLICT
RESOLVED → REVALIDATE
ACTIVE → INVALIDATED
ACTIVE → SUPERSEDED
ACTIVE → EXPIRED
ANY → QUARANTINED
```

---

# 114. Quarantine

Policy decisions with suspicious provenance, corrupted policy references, or unresolved integrity failures SHOULD be quarantinable.

```yaml
quarantine:
  active: true

  reason: string

  entered_at: timestamp

  affected_decision_id: string

  evidence_refs: []

  release_conditions: []
```

Quarantine MUST preserve evidence.

---

# 115. Supersession

When a policy decision is recomputed after a load-bearing change:

```yaml
supersession:
  decision_id: "PD_NEW"

  supersedes:
    - "PD_OLD"

  reason:
    - "policy version changed"

  old_decision_reusable: false
```

Historical decisions SHOULD remain auditable.

---

# 116. Observability Events

Material operations SHOULD emit events such as:

```text
POLICY_DECISION_REQUESTED

POLICY_DISCOVERED

POLICY_APPLICABILITY_RESOLVED

POLICY_EVALUATED

POLICY_CONFLICT_DETECTED

POLICY_DECISION_CREATED

POLICY_DECISION_REVALIDATED

POLICY_DECISION_INVALIDATED

POLICY_DECISION_EXPIRED

POLICY_DECISION_QUARANTINED

POLICY_DECISION_SUPERSEDED

POLICY_ESCALATION_REQUESTED
```

Events SHOULD preserve:

```text
decision ID;
actor;
timestamp;
transaction;
policy identity;
reason;
state transition.
```

---

# 117. Minimum Policy Decision

Minimum structurally meaningful object:

```yaml
policy_decision:
  decision_id: string

  principal_id: string

  operation: string

  target_id: string

  applicable_policies:
    - policy_id: string
      version: string

  decision:
    state:
      - ALLOW
      - DENY
      - CONDITIONAL
      - ESCALATE
      - REVALIDATE
      - CONFLICT
      - UNKNOWN_GAP

  scope: {}

  regime: {}

  evaluated_at: timestamp

  provenance: {}

  confidence_ceiling: null
```

For consequential effects, the minimum object SHOULD be expanded with effect, authority, constraint, freshness, and transaction bindings.

---

# 118. Canonical Decision Law

The core policy-decision law is:

```text
POLICY DECISION
=
context-bound policy conclusion
```

not:

```text
POLICY DECISION
=
universal permission
```

Therefore every material decision inherits its:

```text
principal
action
target
scope
regime
policy versions
evidence
freshness
dependencies
```

---

# 119. Commit Boundary Law

For durable effects:

```text
PolicyAllow
≠
CommitAuthority
```

The final release path remains:

```text
POLICY DECISION
        ↓
AUTHORITY VALIDATION
        ↓
CONSTRAINT VALIDATION
        ↓
SEMANTIC TRANSACTION VALIDATION
        ↓
OBSERVABILITY VALIDATION
        ↓
FRESHNESS / READ-SET VALIDATION
        ↓
EFFECT-LEDGER VALIDATION
        ↓
COMMITTABLE
        ↓
AUTHORIZED EFFECT RELEASE
```

No earlier stage implies a later stage.

---

# 120. Current Completion State

```yaml
completion:
  definition: COMPLETE_AS_MODEL

  scope: COMPLETE_AS_MODEL

  decision_object: COMPLETE_AS_MODEL

  decision_states: COMPLETE_AS_MODEL

  applicability: COMPLETE_AS_MODEL

  composition: COMPLETE_AS_MODEL

  precedence: COMPLETE_AS_MODEL

  conditions: COMPLETE_AS_MODEL

  obligations: COMPLETE_AS_MODEL

  prohibitions: COMPLETE_AS_MODEL

  exceptions: COMPLETE_AS_MODEL

  capability_boundary: COMPLETE_AS_MODEL

  authority_boundary: COMPLETE_AS_MODEL

  control_plane_boundary: COMPLETE_AS_MODEL

  commit_boundary: COMPLETE_AS_MODEL

  HML: COMPLETE_AS_MODEL

  provenance: COMPLETE_AS_MODEL

  uncertainty: COMPLETE_AS_MODEL

  failure_modes: COMPLETE_AS_MODEL

  repair: COMPLETE_AS_MODEL

  tests: COMPLETE_AS_MODEL

  falsifiers: COMPLETE_AS_MODEL

  runtime_implementation: UNKNOWN/GAP

  policy_registry_population: UNKNOWN/GAP

  executed_tests: UNKNOWN/GAP

  empirical_validation: UNKNOWN/GAP

  formal_verification: UNKNOWN/GAP

  canon_approval: UNKNOWN/GAP
```

---

# 121. Hard Boundary Block

```text
POLICY != POLICY_DECISION

POLICY_DECISION != AUTHORITY

POLICY_DECISION != CAPABILITY

POLICY_DECISION != CONTROL_PLANE

POLICY_DECISION != COMMIT

POLICY_ALLOW != AUTHORITY

POLICY_ALLOW != EXECUTION

POLICY_ALLOW != COMMITTABLE

POLICY_ALLOW != COMMITTED

CAPABILITY != AUTHORITY

AUTHORITY != POLICY COMPLIANCE

VALIDATION != AUTHORIZATION

PROPOSAL != COMMIT

EXECUTION_SUCCESS != POLICY_VALIDITY

EXECUTION_SUCCESS != CLAIM_TRUTH

RECEIPT_ID != VERIFIED_RECEIPT

ADDRESSABLE != VALIDATED

PLACEHOLDER != IMPLEMENTED

UNKNOWN/GAP != PASS

UNKNOWN/GAP != ALLOW

CONFLICT != ALLOW

CONDITIONAL != ALLOW

CORRELATED_EVIDENCE != INDEPENDENT_CONFIRMATION

MODEL != EMPIRICAL FACT
```

---

# 122. Canon Boundary

Trang Phan remains the origin architect and steward of AMOS.

This artifact is a substantive AMOS architecture specification intended to complete the `POLICY_DECISION.md` surface.

Its structural completeness does not itself establish canonical admission.

Until separately admitted through the appropriate canon, provenance, governance, validation, and supersession process:

```yaml
artifact_status: PROPOSED

epistemic_class: MODEL

canonical_status: UNKNOWN/GAP

runtime_status: UNKNOWN/GAP

validation_status: UNKNOWN/GAP
```

Where applicable verified source canon conflicts with generated model structure:

```text
APPLICABLE SOURCE CANON
        >
GENERATED MODEL
```

subject to:

```text
version
scope
regime
supersession
provenance
```

resolution.

---

# 123. Final Policy Decision Contract

AMOS SHALL preserve the following policy-decision chain:

```text
REQUEST
    ↓
PRINCIPAL RESOLUTION
    ↓
ACTION NORMALIZATION
    ↓
TARGET / EFFECT BINDING
    ↓
CAPABILITY RESOLUTION
    ↓
POLICY DISCOVERY
    ↓
POLICY VERSION RESOLUTION
    ↓
APPLICABILITY
    ↓
RULE EVALUATION
    ↓
CONDITION / OBLIGATION / PROHIBITION EXTRACTION
    ↓
CONFLICT DETECTION
    ↓
VALID PRECEDENCE / SUPERSESSION
    ↓
POLICY COMPOSITION
    ↓
POLICY_DECISION
    ↓
PROVENANCE + READ-SET BINDING
    ↓
CONTROL-PLANE HANDOFF
    ↓
AUTHORITY / CONSTRAINT / OBSERVABILITY CHECKS
    ↓
COMMIT-TIME POLICY REVALIDATION
    ↓
EFFECT-RELEASE VALIDATION
    ↓
AUTHORIZED COMMIT OR BLOCK
```

The central invariant is:

> **A policy decision is a scoped, versioned, provenance-bound conclusion about policy applicability to a particular action. It is not capability, authority, execution, or commit.**

Therefore:

```text
ALLOW
```

means only that the evaluated policy layer permits the bound action within the decision's applicability envelope.

It does not mean:

```text
AUTHORIZED
COMMITTABLE
COMMITTED
VALIDATED OUTCOME
```

Any unresolved load-bearing policy, scope, regime, authority, provenance, freshness, or conflict condition remains:

```text
UNKNOWN/GAP
```

or the appropriate explicit blocking/escalation state.

AMOS MUST NOT convert missing information into permission.

AMOS MUST NOT convert capability into authority.

AMOS MUST NOT convert proposal into commit.

AMOS MUST NOT convert successful execution into proof of policy validity.

Integrity remains prior to completeness, fluency, speed, and optimization.

---

# END — POLICY_DECISION.md

```
```

---

00_ROOT_MOC|AMOS MOC

---
**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: policy_decision
node_type: note
path: 03_CONTROL_PLANE/03_POLICY/POLICY_DECISION.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[03_POLICY_MOC]]
