---
title: "ROUTING POLICY"
type: routing
source: "25_COGNITIVE_MATRIX/10_ROUTING"
artifact: "ROUTING_POLICY.md"
artifact_id: "25_cognitive_matrix_10_routing_routing_policy"
origin_architect: "Trang Phan"
steward: "Trang Phan"
system: "AMOS OS"
plane: "25_COGNITIVE_MATRIX"
segment: "25_COGNITIVE_MATRIX/10_ROUTING"
artifact_kind: "ROUTING"
path: "25_COGNITIVE_MATRIX/10_ROUTING/ROUTING_POLICY.md"

tags:
  - 10_routing
  - 25_cognitive_matrix
  - amos_os
  - canon/cognitive-matrix
  - canon/universe
  - cognitive_matrix
  - note
  - policy
  - routing
  - routing_policy.md
  - rscf
  - placeholder_expanded

version: "0.2.0"
updated: "2026-08-27"

status: "PLACEHOLDER_EXPANDED"
epistemic_class: "AMOS_MODEL"
canonical_status: "UNKNOWN/GAP"
implementation_status: "NOT_ESTABLISHED"
validation_status: "NOT_ESTABLISHED"
executable_binding: "NOT_ESTABLISHED"
ingestion_action: "ADD_ONLY"

rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: 25_COGNITIVE_MATRIX
  regime: canon_placeholder
  confidence_ceiling: source_supported
  provenance_independence: NOT_ESTABLISHED
---


# ROUTING POLICY

## 0. Canonical Status

`ROUTING_POLICY.md` is an **ADD-ONLY placeholder-expanded artifact** for the **25_COGNITIVE_MATRIX** plane segment.

It reserves the canonical slot for the AMOS framework family named **ROUTING POLICY**.

The artifact is presently:

```text
status: PLACEHOLDER_EXPANDED
epistemic_class: AMOS_MODEL
canonical_status: UNKNOWN/GAP
implementation_status: NOT_ESTABLISHED
validation_status: NOT_ESTABLISHED
executable_binding: NOT_ESTABLISHED
```

This artifact MUST NOT be interpreted as establishing completed, validated, or enforced canon.

## 1. Governing Integrity Boundary

The following distinctions are mandatory:

```text
PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

DOCUMENTED != ENFORCED

MODEL != OBSERVATION

SOURCE_CLAIM != VERIFIED

CANON_CANDIDATE != CANONICAL

CANONICAL != EMPIRICAL_TRUTH

CAPABILITY != AUTHORITY

AUTHORIZATION != COMMIT

PROPOSAL != COMMIT

IMPLEMENTED != VALIDATED

LOGGED != APPROVED

UNKNOWN/GAP != PASS
```

No downstream layer may silently collapse these distinctions.

Origin architect / steward: **Trang Phan**

System: **AMOS OS**

---

```md
---
artifact_id: AMOS-CM-10-ROUTING-ROUTING-POLICY
title: "10_ROUTING — Routing Policy"

path_target: "25_COGNITIVE_MATRIX/10_ROUTING/ROUTING_POLICY.md"

artifact_class: MATRIX_INFRASTRUCTURE_PLACEHOLDER
contract_class: ROUTING_POLICY_CONTROL_CONTRACT
architecture_layer: COGNITIVE_MATRIX_INFRASTRUCTURE
subsystem: 10_ROUTING

origin_architect: Trang Phan
stewardship: AMOS / Trang corpus

status: PROPOSED_SPECIFICATION
implementation_status: UNIMPLEMENTED_OR_UNVERIFIED
validation_status: UNVALIDATED
epistemic_class: UNKNOWN/GAP
conclusion_class: UNKNOWN/GAP

amos_core_target: v4.4
updated: 2026-08-26

authority_class: NON_AUTHORITATIVE_POLICY_SPECIFICATION
routing_authority: NONE
policy_authority: NONE
execution_authority: NONE
promotion_authority: NONE
canon_authority: NONE
finality_authority: NONE

risk_class: CONTROL_PLANE_CRITICAL
default_mutation_class: M0_METADATA_UNTIL_PROMOTED
default_reversibility: HIGH_WHILE_PLACEHOLDER

rscf_role:
  - ROUTING_POLICY_CAPSULE
  - ROUTE_ELIGIBILITY_CAPSULE
  - ROUTE_SELECTION_POLICY_CAPSULE
  - ROUTE_REUSE_POLICY_CAPSULE

gmef_role:
  - ROUTING_GOVERNANCE_GATE
  - POLICY_CONSTRAINT_GATE
  - ROUTE_ACTIVATION_PRECONDITION
  - EFFECT_PATH_POLICY_GATE

hml_scope:
  H:
    - ROUTING_CONSTITUTION
    - GOVERNANCE_POLICY
    - AUTHORITY_BOUNDARY
    - SYSTEM_SCOPE
    - REGIME_POLICY
  M:
    - DOMAIN_ROUTING_POLICY
    - MODE_ROUTING_POLICY
    - CAPABILITY_SELECTION
    - DEPENDENCY_ROUTING
    - FALLBACK_POLICY
    - ROUTE_REUSE_POLICY
  L:
    - IDENTITY_MATCHING
    - VERSION_MATCHING
    - ROUTE_FILTERING
    - PRIORITY_RESOLUTION
    - CACHE_VALIDATION
    - LOCAL_BINDING_POLICY

tags:
  identity:
    - AMOS
    - AMOS_OS
    - AMOS_FULL_BRAIN_OS
    - AMOS_CORE
    - AMOS_CORE_v4_4
    - TRANG_PHAN
    - COGNITIVE_MATRIX
    - ROUTING
    - ROUTING_POLICY

  architecture:
    - MATRIX_INFRASTRUCTURE
    - CONTROL_PLANE
    - ROUTER
    - BINDER
    - POLICY_ENGINE
    - KERNEL
    - ENGINE
    - SKILL
    - AGENT
    - WORKER
    - WORKFLOW
    - EVENT_BUS
    - REGISTRY
    - VALIDATOR
    - GENERATOR

  routing:
    - ROUTE_SELECTION
    - ROUTE_ELIGIBILITY
    - DOMAIN_ROUTING
    - HML_ROUTING
    - MODE_ROUTING
    - CAPABILITY_ROUTING
    - DEPENDENCY_ROUTING
    - FALLBACK_ROUTING
    - RECOVERY_ROUTING
    - ROUTE_REUSE
    - ROUTE_INVALIDATION
    - ROUTE_PRIORITY

  reasoning:
    - RSCF
    - GMEF
    - HML
    - FRACTAL_KNOWLEDGE_NETWORK
    - [[L19_PROOF_CAPSULE]]
    - ADAPTIVE_COMPLEXITY
    - COMPETING_HYPOTHESES
    - UNCERTAINTY_VECTOR

  epistemic:
    - SOURCE_CLAIM
    - OBSERVATION
    - DERIVED
    - MODEL
    - CONDITIONAL
    - COMPETING
    - UNKNOWN_GAP
    - CONFIDENCE_CEILING

  provenance:
    - PROVENANCE
    - PROVENANCE_TOPOLOGY
    - SOURCE_ANCESTRY
    - INDEPENDENCE
    - SYBIL_HARDENING
    - CAUSAL_LINEAGE
    - VERSION_LINEAGE

  governance:
    - POLICY
    - POLICY_EPOCH
    - AUTHORITY
    - INVARIANT
    - MODE_GOVERNANCE
    - EXECUTION_GOVERNANCE
    - CONFLICT_RESOLUTION
    - SUPERSESSION
    - REVOCATION

  state:
    - MVCC
    - CAS
    - READ_SET
    - WRITE_SET
    - REGISTRY_VERSION
    - ROUTE_VERSION
    - CACHE_VERSION
    - EPOCH
    - IDEMPOTENCY

  integrity:
    - FAIL_CLOSED
    - ANTI_FABRICATION
    - ANTI_REGRESSION
    - ANTI_DRIFT
    - SCOPE_FIREWALL
    - REGIME_FIREWALL
    - CAUSAL_FIREWALL
    - FRESHNESS
    - SELECTIVE_INVALIDATION

  assurance:
    - VALIDATION
    - ROUTING_AUDIT
    - REPLAY
    - OBSERVABILITY
    - FALSIFICATION
    - ADVERSARIAL_VALIDATION
    - RECOVERY
---

# 10_ROUTING — Routing Policy

> **Class:** `MATRIX_INFRASTRUCTURE_PLACEHOLDER`
>
> **Origin architect / steward:** Trang Phan
>
> **Status:** `PLACEHOLDER / UNVALIDATED`
>
> **Conclusion class:** `UNKNOWN/GAP`
>
> **AMOS_CORE target:** `v4.4`

---

# 0. Purpose

`ROUTING_POLICY.md` defines the AMOS policy layer that constrains **which routing decisions are allowed, preferred, blocked, escalated, reused, invalidated, or forced into ambiguity/competition**.

It is not the router itself.

It is not the binding layer.

It is not the validator.

It is not the authority service.

It defines the governance rules those components must obey.

Canonical separation:

```text
REQUEST
    ↓
ROUTER
    ↓
CANDIDATE ROUTES
    ↓
ROUTING POLICY
    ↓
ELIGIBLE ROUTES
    ↓
BINDING
    ↓
VALIDATION
    ↓
AUTHORITY / CONTROL PLANE
```

Therefore:

```text
POLICY_ALLOWED
!= ROUTED

ROUTED
!= BOUND

BOUND
!= VALIDATED

VALIDATED
!= AUTHORIZED

AUTHORIZED
!= COMMITTED
```

---

# 1. Policy objective

The routing policy exists to ensure:

> **AMOS selects only materially relevant, compatible, sufficiently fresh, provenance-preserving, scope-valid, regime-valid, policy-permitted paths while preventing convenience heuristics from weakening integrity.**

The policy must optimize:

```text
integrity
> completeness
> fluency
> speed
> token savings
```

in alignment with AMOS core law.

The Full Brain OS source explicitly requires routing only to materially relevant domains rather than activating every nested engine by default, and it requires gaps to remain exposed rather than invented. 

---

# 2. Policy status boundary

This file is presently:

```text
PLACEHOLDER
UNVALIDATED
NON_AUTHORITATIVE
```

Therefore the rules below are:

```text
AMOS-aligned structural MODEL
```

unless independently recovered from authoritative routing-policy canon.

They must not be treated as active runtime policy merely because this file exists.

---

# 3. Routing policy model

A routing policy can be modeled as:

[
P_R=
\langle
Rules,
Priorities,
HardConstraints,
SoftPreferences,
Scope,
Regime,
Epoch,
Exceptions,
Escalation,
Revocation
\rangle
]

The policy evaluation function is:

[
Evaluate(RouteCandidate, Context, Policy)
\rightarrow
PolicyDecision
]

Possible outputs:

```text
ALLOW
DENY
CONDITIONAL
ESCALATE
COMPETING
UNKNOWN/GAP
```

---

# 4. Policy scope

Routing policy may govern:

```text
domain selection
H/M/L traversal
mode selection
Agent routing
Skill routing
Engine routing
Kernel routing
Worker routing
Validator routing
Generator routing
Workflow routing
event-handler routing
evidence routing
data-source routing
fallback routing
recovery routing
route caching
route reuse
route invalidation
route escalation
cross-domain routing
effect-path routing
```

---

# 5. Explicit non-scope

Routing policy must not independently decide:

```text
truth
canon admission
policy activation
authority issuance
runtime commit
finality
external effect success
```

It may require those services.

---

# 6. Policy classes

```yaml
routing_policy_classes:

  RP0_IDENTITY:
    governs:
      - exact component identity
      - version matching
      - registry resolution

  RP1_RELEVANCE:
    governs:
      - domain relevance
      - smallest sufficient path
      - over-routing prevention

  RP2_HML:
    governs:
      - H/M/L traversal
      - escalation depth
      - raw evidence loading

  RP3_CAPABILITY:
    governs:
      - capability compatibility
      - specialist vs generic routing

  RP4_MODE:
    governs:
      - active mode selection
      - incompatible mode exclusion

  RP5_SCOPE_REGIME:
    governs:
      - scope
      - environment
      - regime
      - freshness

  RP6_PROVENANCE:
    governs:
      - evidence routing
      - independence
      - source ancestry

  RP7_FALLBACK:
    governs:
      - fallback eligibility
      - degraded-mode disclosure

  RP8_EXECUTION:
    governs:
      - worker path
      - authority requirement
      - effect class

  RP9_REUSE:
    governs:
      - route cache
      - proof reuse
      - invalidation

  RP10_SECURITY:
    governs:
      - privileged paths
      - sandbox/security constraints

  RP11_RECOVERY:
    governs:
      - reroute
      - rebind
      - repair
      - no-action state
```

---

# 7. Policy precedence hierarchy

Routing rules should distinguish precedence.

Provisional hierarchy:

```text
CONSTITUTIONAL INTEGRITY RULE
        ↓
ACTIVE GOVERNANCE POLICY
        ↓
SECURITY / AUTHORITY CONSTRAINT
        ↓
SCOPE / REGIME / FRESHNESS
        ↓
CAPABILITY COMPATIBILITY
        ↓
SPECIFICITY
        ↓
PERFORMANCE / COST PREFERENCE
        ↓
DEFAULT / FALLBACK
```

Lower layers may not override higher-layer failures.

---

# 8. Hard versus soft policy

Hard policy:

```text
must hold
or route is ineligible
```

Soft policy:

```text
used for ranking
after hard gates pass
```

Example:

```yaml
hard:
  - policy_compatible
  - scope_compatible
  - regime_compatible
  - required_capability_present

soft:
  - lower_latency
  - lower_cost
  - higher_specificity
```

Hard constraints cannot be traded for score.

---

# 9. Policy decision record

```yaml
routing_policy_decision:

  decision_id: UNKNOWN

  route_candidate:
    route_id: UNKNOWN
    component_id: UNKNOWN
    version: UNKNOWN

  policy:
    policy_id: UNKNOWN
    epoch: UNKNOWN
    hash: UNKNOWN

  checks:
    relevance: UNKNOWN
    hml: UNKNOWN
    capability: UNKNOWN
    mode: UNKNOWN
    scope: UNKNOWN
    regime: UNKNOWN
    freshness: UNKNOWN
    provenance: UNKNOWN
    security: UNKNOWN
    execution: UNKNOWN

  result:
    UNKNOWN/GAP

  reasons: []

  exceptions_used: []

  confidence_ceiling: 0

  decided_at: null
  valid_until: null
```

---

# 10. Policy state variables

```yaml
routing_policy_state:

  policy:
    policy_id: UNKNOWN
    policy_epoch: UNKNOWN
    version: UNKNOWN
    hash: UNKNOWN

  architecture:
    core_target: v4.4
    architecture_version: UNKNOWN

  registries:
    capability_registry_version: UNKNOWN
    mode_registry_version: UNKNOWN
    worker_registry_version: UNKNOWN

  context:
    system: UNKNOWN
    hml: UNKNOWN
    regime: UNKNOWN
    environment: UNKNOWN

  enforcement:
    active: UNKNOWN
    enforcement_point: UNKNOWN

  exceptions:
    active: []

  revocation:
    revoked_rules: []

  freshness:
    valid_until: null
```

---

# 11. Policy operators

Candidate operators:

```text
resolve_policy()
resolve_policy_epoch()
check_policy_freshness()
classify_route_candidate()
evaluate_hard_constraints()
evaluate_soft_preferences()
resolve_precedence()
check_exception()
check_scope_policy()
check_regime_policy()
check_mode_policy()
check_capability_policy()
check_fallback_policy()
check_effect_policy()
check_security_policy()
check_route_reuse_policy()
check_route_invalidation_policy()
emit_policy_decision()
invalidate_policy_decision()
```

---

# 12. Core routing policy invariants

## I-RPOL-001 — Integrity dominates optimization

```text
speed/cost
cannot override
integrity failure
```

## I-RPOL-002 — Smallest sufficient route

Activate only materially relevant components.

## I-RPOL-003 — No default capture

A generic route cannot shadow a valid specialized route without explicit policy.

## I-RPOL-004 — No silent fallback

Fallback must be policy-permitted and visible.

## I-RPOL-005 — Explicit target respected

Explicitly requested component must not silently substitute.

## I-RPOL-006 — Hard filters before ranking

Only eligible candidates may be scored.

## I-RPOL-007 — Unknown fails closed

```text
UNKNOWN/GAP != ALLOW
```

for critical policy dimensions.

## I-RPOL-008 — Scope preservation

No silent scope expansion.

## I-RPOL-009 — Regime preservation

No silent regime crossing.

## I-RPOL-010 — Freshness preservation

Stale policy decisions must not remain silently active.

## I-RPOL-011 — Mode compatibility

Inactive or unvalidated modes cannot be treated as active modes.

## I-RPOL-012 — Provenance preservation

Evidence routing must retain source ancestry.

## I-RPOL-013 — False independence prohibited

Repeated descendants do not increase independent evidence count.

## I-RPOL-014 — Capability is not authority

```text
CAPABILITY != AUTHORITY
```

## I-RPOL-015 — Policy is not authority

```text
POLICY_ALLOW != AUTHORITY_GRANT
```

## I-RPOL-016 — Event delivery is not authority

```text
EVENT != AUTHORITY
```

## I-RPOL-017 — Worker-only governed effects

Consequential effects require infrastructure-governed Worker path.

## I-RPOL-018 — Ambiguity preservation

Incomparable valid routes remain `COMPETING` or `AMBIGUOUS`.

## I-RPOL-019 — Selective invalidation

Policy change invalidates only dependent routes where possible.

## I-RPOL-020 — Policy version binding

Every consequential route must identify the policy epoch under which it was evaluated.

---

# 13. Relevance policy

The default relevance rule:

[
RouteEligible(c)
\Rightarrow
MateriallyRelevant(c,Q)
]

A component is materially relevant if its output could change:

```text
claim
decision
action
validation status
route validity
risk state
```

If it cannot, do not route there by default.

---

# 14. Over-routing policy

Prohibit unnecessary activation such as:

```text
simple local task
→ all Agents
→ all Skills
→ all Engines
→ all evidence
```

unless the task explicitly requires maximum breadth.

Over-routing increases:

```text
latency
cost
dependency surface
conflict probability
provenance complexity
failure surface
```

---

# 15. Under-routing policy

Also prohibit under-routing when missing branches can change the outcome.

Examples:

```text
causal question
→ summary-only route

policy mutation
→ no governance path

irreversible effect
→ no authority/Worker path
```

---

# 16. H/M/L policy

Default traversal:

```text
BOOTSTRAP
→ H
→ M
→ L
→ RAW EVIDENCE ONLY IF REQUIRED
```

Policy rule:

```text
Do not descend further
unless deeper layer can materially change result.
```

---

# 17. H-level policy

H-level routing is appropriate for:

```text
architecture
governance
domain selection
canon
policy
system-level state
```

Do not route to L-level implementation before H-level objective/scope is sufficiently known.

---

# 18. M-level policy

M-level routing is appropriate for:

```text
subsystem
Engine
Skill
Agent role
Workflow
Validator
Generator
Mode family
```

---

# 19. L-level policy

L-level routing is appropriate for:

```text
Kernel
Worker
handler
schema
specific evidence
exact implementation detail
```

---

# 20. Raw evidence policy

Raw evidence defaults:

```text
DO_NOT_LOAD_UNLESS_REQUIRED
```

Load when:

```text
premise disputed
provenance unclear
contradiction exists
freshness matters
scope uncertain
causal claim consequential
```

---

# 21. Adaptive complexity policy

Use:

```text
C0 Direct
C1 Compact
C2 Structured
C3 Deep
C4 Maximum
```

Escalate for:

```text
high stakes
irreversibility
novelty
weak evidence
contradiction
causal ambiguity
scope mismatch
regime shift
governance impact
```

De-escalate when outcome-changing uncertainty is resolved.

---

# 22. Capability policy

Candidate must explicitly support required capability.

```text
similar name
!= compatible capability
```

A router may not infer capability solely from:

```text
folder name
file name
description similarity
```

without contract evidence where consequential.

---

# 23. Specialist preference policy

Provisional policy:

```text
exact specialist
>
specialized compatible handler
>
domain-general handler
>
global generic handler
>
fallback
```

Only among otherwise valid candidates.

---

# 24. First-match policy

Default:

```text
FIRST_MATCH_ROUTING = PROHIBITED
```

unless an explicit authoritative policy states ordering is meaningful.

---

# 25. Registration-order policy

Registry order is metadata, not priority, unless policy declares otherwise.

```text
registration_index
!= semantic_priority
```

---

# 26. Explicit target policy

If user/system requests exact component:

```text
target = X
```

then router should:

```text
resolve X
or return explicit failure
```

not substitute silently.

---

# 27. Ambiguity policy

When candidates remain equally valid:

```text
AMBIGUOUS
```

Allowed responses:

```text
seek discriminating context
run a cheap discriminating check
preserve competing routes
use explicit policy tie-break
```

---

# 28. Tie-break policy

Tie-breakers must be named and versioned.

Potential policy dimensions:

```text
exact specificity
validated status
scope fit
freshness
lower risk
lower dependency burden
```

No hidden tie-break.

---

# 29. Mode policy

Mode routing must verify:

```text
mode exists
mode contract exists
mode validation state
mode activation state
scope compatibility
regime compatibility
policy permission
```

Hard boundary:

```text
MODE_FOLDER_EXISTS
!= MODE_ACTIVE
```

---

# 30. Mode-family policy

Policy may prohibit mutually exclusive mode combinations.

Example contract:

```yaml
mode_policy:
  mutually_exclusive_sets: []
  required_combinations: []
  precedence_rules: []
```

Current values remain `UNKNOWN/GAP`.

---

# 31. Agent routing policy

Agents may be selected for reasoning roles.

Policy must preserve:

```text
Agent
!= authority
```

Agent selection may depend on:

```text
role
domain
mode
scope
tools
capabilities
```

---

# 32. Skill routing policy

Skill route requires:

```text
trigger fit
capability fit
scope fit
input/output compatibility
effect classification
```

Skill invocation must not weaken Worker invariants.

---

# 33. Engine routing policy

Engine selection should consider:

```text
domain fit
state compatibility
kernel dependencies
schema compatibility
scope/regime
```

---

# 34. Kernel routing policy

Kernel selection should favor:

```text
deterministic
narrow
typed
versioned
invariant-aware
```

primitives.

---

# 35. Worker routing policy

Workers are execution endpoints.

Policy must require:

```text
declared effect class
allowed target
required invariants
authority requirement
idempotency requirement
recovery semantics
```

---

# 36. Worker-only effect policy

For consequential effects:

```text
Agent proposes
→ Infrastructure authorizes
→ Worker executes
```

The router may select the Worker.

It may not grant execution authority.

---

# 37. Validator routing policy

Validator type must match validation class.

Examples:

```text
schema → schema validator
provenance → provenance validator
causal → causal validator/path
```

No silent downgrade to a weaker validator.

---

# 38. Generator routing policy

Generator selection must bind:

```text
artifact type
template
schema
version
scope
policy
```

Generator output remains candidate.

---

# 39. Workflow routing policy

Distinguish:

```text
canonical workflow
```

from:

```text
ad-hoc plan
```

Canonical workflows may require declared state transitions.

Ad-hoc plans may be governed per consequential event.

---

# 40. Event routing policy

Event routing must check:

```text
event type
schema
producer
handler
idempotency
ordering
policy
authority requirement
```

Hard boundary:

```text
EVENT_RECEIVED
!= AUTHORIZED_EFFECT
```

---

# 41. Evidence routing policy

Evidence should be routed by epistemic type.

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL
DECISION
UNKNOWN
```

Do not flatten evidence classes.

---

# 42. Provenance policy

Evidence routing should preserve:

```text
source identity
version
ancestry
dependency edges
freshness
scope
```

---

# 43. Independence policy

Multiple paths count as independent only when ancestry independence is demonstrated.

```text
N descendants from one root
→ effective independent count = 1
```

---

# 44. Scope policy

A candidate is routable only if its applicability envelope is compatible.

```yaml
route_scope:
  system: UNKNOWN
  environment: UNKNOWN
  hml: UNKNOWN
  assumptions: []
```

Cross-scope routing requires explicit compatibility.

---

# 45. Regime policy

A route validated in regime R1 is not silently valid in R2.

Regime transitions should trigger:

```text
REVALIDATE
REBOUND
REROUTE
```

where load-bearing.

---

# 46. Freshness policy

Freshness should be typed per dependency:

```text
policy freshness
registry freshness
mode freshness
component freshness
evidence freshness
validation-receipt freshness
authority freshness
```

No universal duration should be invented.

---

# 47. Policy epoch

Every consequential route policy decision should bind:

```yaml
policy_binding:
  policy_id: UNKNOWN
  policy_epoch: UNKNOWN
  policy_hash: UNKNOWN
```

---

# 48. Policy epoch transition

If policy changes:

```text
P@E1
→ P@E2
```

then routes evaluated under E1 must be inspected for dependency on changed rules.

Do not invalidate unrelated routes globally.

---

# 49. Route-reuse policy

Route reuse may be permitted only when:

```text
request equivalent
dependency closure unchanged
scope unchanged
regime compatible
freshness valid
policy compatible
mode compatible
no conflict introduced
```

---

# 50. v4.4 local fast-path policy

AMOS v4.4-style local reasoning/reuse is allowed only when independence and dependency closure are established.

Require:

```text
dependency closure known
provenance independence established
scope compatible
regime compatible
freshness valid
non-conflict established
authority unaffected
```

Otherwise escalate.

This is a reasoning/control pattern, not proof that the Markdown routing layer literally implements distributed coordination avoidance.

---

# 51. Route cache policy

A route cache entry must carry:

```yaml
route_cache:
  route_id: UNKNOWN
  request_signature: UNKNOWN
  registry_version: UNKNOWN
  mode_registry_version: UNKNOWN
  policy_epoch: UNKNOWN
  regime: UNKNOWN
  valid_until: null
```

Cache hit does not imply validity.

---

# 52. Cache invalidation policy

Invalidate on load-bearing changes:

```text
component superseded
registry changed
policy epoch changed
mode state changed
scope changed
regime changed
required validation expired
security context changed
```

---

# 53. MVCC/CAS route policy

Conceptual rule:

```text
route based on observed state S1
→ before consequential use
compare current state
```

If a load-bearing part differs:

```text
STALE_ROUTE
```

---

# 54. Read-set policy

Consequential route records should identify load-bearing state.

```yaml
route_read_set:
  - artifact_id: UNKNOWN
    version: UNKNOWN
    hash: UNKNOWN
    load_bearing: true
```

---

# 55. Selective invalidation policy

When one dependency changes:

```text
invalidate only dependent route nodes/edges
```

Example:

```text
Worker W1 superseded
→ invalidate W1 routes
→ preserve W2 routes
```

---

# 56. Fallback policy

Fallback allowed only if:

```text
fallback explicitly permitted
primary unavailable/invalid
fallback itself valid
semantic difference disclosed
```

---

# 57. Fallback equivalence policy

Classify fallback as:

```text
EQUIVALENT
DEGRADED
NON_EQUIVALENT
```

Only `EQUIVALENT` may be transparent.

---

# 58. Degraded-mode policy

If degraded:

```yaml
degraded_route:
  reason: UNKNOWN
  lost_guarantees: []
  retained_guarantees: []
  valid_until: null
```

Degradation must be visible.

---

# 59. No-route policy

`NO_ROUTE` is valid and sometimes preferable.

```text
NO_ROUTE
>
UNJUSTIFIED_ROUTE
```

under integrity-first governance.

---

# 60. Conflict policy

Route conflict can arise from:

```text
duplicate handlers
version conflicts
mode conflicts
scope mismatch
policy disagreement
registry disagreement
competing evidence
```

Unresolved conflict should not be hidden.

---

# 61. Competing route policy

If two paths are valid but incomparable:

```text
COMPETING
```

Preserve both until a discriminating test or explicit policy resolves them.

---

# 62. Causal routing policy

Causal questions require appropriate causal paths.

Do not route:

```text
causal-effect question
→ analogy-only handler
```

as sufficient.

---

# 63. Cross-domain policy

Cross-domain mappings remain:

```text
MODEL
```

unless independently validated.

Routing may use analogy to generate hypotheses, not to establish causation.

---

# 64. Security routing policy

Security-sensitive routes should require:

```text
trusted capability
least privilege
sandbox where relevant
explicit permission
security validation
```

General capability does not imply security suitability.

---

# 65. Data-access policy

Routing to a data source requires:

```text
source exists
source connected
source authorized
purpose permitted
scope compatible
```

These are separate states.

---

# 66. Privacy policy

Relevant data must not be routed if access is outside granted scope.

```text
relevance
!= permission
```

---

# 67. Execution-risk policy

Potential effect classes:

```text
E0 READ_ONLY
E1 REVERSIBLE_LOCAL
E2 DURABLE_LOCAL
E3 EXTERNAL_REVERSIBLE
E4 EXTERNAL_CONSEQUENTIAL
E5 IRREVERSIBLE/GOVERNANCE_CRITICAL
```

Validation burden increases with effect class.

Exact classes remain provisional.

---

# 68. Authority escalation policy

If route enters consequential effect path:

```text
AUTHORITY_REQUIRED
```

must be emitted.

Routing policy cannot itself mint authority.

---

# 69. Canon-routing policy

Canon-relevant operations should route through:

```text
source
→ evidence
→ validation
→ contradiction analysis
→ scope/regime
→ authority
→ canon admission
```

No direct file-to-canon route.

---

# 70. Policy-routing recursion

Routing policy changes themselves are governance operations.

A new routing policy version should require:

```text
proposal
→ validation
→ conflict analysis
→ authority
→ promotion
→ activation
```

This file cannot self-activate.

---

# 71. Policy exception model

Exceptions should be explicit.

```yaml
routing_policy_exception:
  exception_id: UNKNOWN
  rule_id: UNKNOWN
  scope: UNKNOWN
  reason: UNKNOWN
  authority_ref: UNKNOWN
  valid_from: null
  valid_until: null
```

No undocumented exception.

---

# 72. Emergency override policy

If an emergency override mechanism exists, it must declare:

```text
who may invoke
scope
duration
logging
rollback
post-event audit
```

Current implementation status:

```text
UNKNOWN/GAP
```

---

# 73. Revocation policy

Policy decisions or route permissions may be revoked.

```yaml
revocation:
  target_policy_decision: UNKNOWN
  reason: UNKNOWN
  authority_ref: UNKNOWN
  revoked_at: null
```

---

# 74. Supersession policy

New routing policy versions should preserve lineage.

```yaml
supersession:
  predecessor: UNKNOWN
  successor: UNKNOWN
  changed_rules: []
  preserved_rules: []
  migration_notes: []
```

---

# 75. Routing-policy workflow

```text
ROUTE_CANDIDATE
    ↓
POLICY_CONTEXT_BOUND
    ↓
HARD_RULES_EVALUATED
    ↓
SOFT_PREFERENCES_EVALUATED
    ↓
CONFLICTS_CHECKED
    ↓
POLICY_DECISION
```

---

# 76. Consequential-route workflow

```text
REQUEST
    ↓
ROUTE
    ↓
ROUTING POLICY
    ↓
BINDING
    ↓
VALIDATION
    ↓
AUTHORITY
    ↓
WORKER
```

---

# 77. Route-reuse workflow

```text
CACHED ROUTE
    ↓
CHECK REQUEST EQUIVALENCE
    ↓
CHECK READ SET
    ↓
CHECK POLICY EPOCH
    ↓
CHECK MODE/REGIME/FRESHNESS
    ↓
REUSE OR INVALIDATE
```

---

# 78. Recovery workflow

```text
ROUTE POLICY FAILURE
    ↓
IDENTIFY FAILED RULE
    ↓
INVALIDATE DEPENDENT ROUTE
    ↓
PRESERVE UNAFFECTED ROUTES
    ↓
RESOLVE NEW CANDIDATES
    ↓
RE-EVALUATE POLICY
```

---

# 79. Routing-policy events

Suggested events:

```text
ROUTING_POLICY_EVALUATION_REQUESTED
ROUTING_POLICY_CONTEXT_BOUND
ROUTING_POLICY_RULE_PASSED
ROUTING_POLICY_RULE_FAILED
ROUTING_POLICY_CONDITIONAL
ROUTING_POLICY_COMPETING
ROUTING_POLICY_ALLOW
ROUTING_POLICY_DENY
ROUTING_POLICY_ESCALATE
ROUTING_POLICY_STALE
ROUTING_POLICY_REVOKED
ROUTING_POLICY_SUPERSEDED
```

---

# 80. Policy event envelope

```yaml
routing_policy_event:

  event_id: UNKNOWN
  type: UNKNOWN

  route_id: UNKNOWN
  request_id: UNKNOWN

  policy:
    policy_id: UNKNOWN
    epoch: UNKNOWN

  candidate_id: UNKNOWN

  correlation_id: UNKNOWN
  causation_id: UNKNOWN

  result: UNKNOWN

  timestamp: null
```

Event emission is not authority.

---

# 81. Control-plane enforcement points

Potential enforcement points:

```text
before binding
before validator selection
before Worker selection
before external effect authorization
before route-cache reuse
before policy-sensitive fallback
```

Exact runtime enforcement points remain `UNKNOWN/GAP`.

---

# 82. Routing policy Engine

Possible engine:

```text
Routing Policy Engine
```

Responsibilities:

```text
evaluate hard rules
evaluate soft preferences
apply precedence
detect exceptions
emit policy decision
```

This is provisional architecture.

---

# 83. Policy kernels

Candidate deterministic kernels:

```text
check_policy_epoch()
check_rule_applicability()
check_scope_rule()
check_regime_rule()
check_mode_rule()
check_capability_rule()
check_fallback_rule()
check_effect_rule()
resolve_rule_precedence()
check_exception_validity()
```

---

# 84. Policy Agents

Possible roles:

### ROUTING_POLICY_REVIEW_AGENT

Structures policy-sensitive route questions.

### POLICY_CONFLICT_AGENT

Identifies conflicting routing rules.

### ROUTE_ESCALATION_AGENT

Proposes escalation when local routing is insufficient.

### ADVERSARIAL_ROUTING_POLICY_AGENT

Attempts to find bypasses, hidden defaults, or weakened invariants.

Agents do not activate policy.

---

# 85. Policy Skills

Potential Skills:

```text
evaluate-routing-policy
check-route-eligibility
check-routing-precedence
check-route-fallback-policy
check-route-mode-policy
check-route-scope-policy
check-route-regime-policy
check-route-freshness-policy
check-route-effect-policy
check-route-reuse-policy
invalidate-route-policy-decision
compare-routing-policies
```

---

# 86. Policy protocol candidates

Potential protocols:

```text
policy lookup
policy version negotiation
policy decision exchange
exception request
policy revocation
route escalation
policy refresh
policy supersession
```

Exact protocols remain `UNKNOWN/GAP`.

---

# 87. Validation relationship

`11_VALIDATION` should validate:

```text
policy document
policy version
rule semantics
policy decision
route compliance
```

Routing policy must not self-certify.

---

# 88. Routing-audit relationship

`ROUTING_AUDIT.md` should audit:

```text
policy used correct epoch?
hard rules applied?
soft ranking applied only after filtering?
fallback policy respected?
exceptions valid?
route reuse valid?
```

---

# 89. Binding-rules relationship

`BINDING_RULES.md` provides exact binding semantics.

Routing policy constrains whether a binding is eligible.

```text
POLICY_ELIGIBLE
→ binding may proceed

POLICY_DENIED
→ binding blocked
```

---

# 90. Promotion-gate relationship

A routing policy version should not become active because a file exists.

```text
POLICY_CANDIDATE
→ VALIDATION
→ PROMOTION GATES
→ AUTHORITY
→ ACTIVE POLICY
```

---

# 91. RSCF routing-policy capsule

```yaml
rscf:

  claim_id:
    RSCF-CM-ROUTING-POLICY-001

  claim:
    "This file defines the authoritative AMOS routing policy for 10_ROUTING."

  claim_class:
    UNKNOWN/GAP

  scope:
    system: AMOS_OS
    subsystem: COGNITIVE_MATRIX
    package: 10_ROUTING
    artifact: ROUTING_POLICY.md

  evidence: []

  provenance: []

  load_bearing_premises:
    - authoritative routing policy canon recovered
    - active policy epoch known
    - routing README accepted
    - binding rules accepted
    - mode registry recovered
    - component registries recovered
    - policy enforcement implementation recovered
    - policy tests executed

  dependencies:
    - AUTHORITATIVE_STATE
    - 10_ROUTING/README.md
    - 10_ROUTING/BINDING_RULES.md
    - 10_ROUTING/ROUTING_AUDIT.md
    - MODE_REGISTRY
    - CAPABILITY_REGISTRY
    - POLICY_MANIFEST
    - AUTHORITY_REGISTRY
    - PROVENANCE_MANIFEST
    - 11_VALIDATION
    - 11_VALIDATION/PROMOTION_GATES.md

  competing:
    - authoritative routing policy may exist elsewhere

  falsifiers:
    - recovered canon defines different policy semantics
    - runtime policy engine contradicts this placeholder
    - higher-order governance supersedes these rules

  regime:
    architecture: UNKNOWN
    runtime: UNKNOWN

  freshness: null

  confidence_ceiling: 0

  status:
    PLACEHOLDER
```

---

# 92. GMEF routing-policy capsule

```yaml
gmef:

  artifact:
    AMOS-CM-10-ROUTING-ROUTING-POLICY

  governance_status:
    PLACEHOLDER

  governed_operations:
    - ROUTE_ELIGIBILITY
    - ROUTE_SELECTION
    - FALLBACK_ELIGIBILITY
    - ROUTE_REUSE
    - ROUTE_INVALIDATION
    - WORKER_ROUTE_ELIGIBILITY
    - MODE_ROUTE_ELIGIBILITY
    - SECURITY_ROUTE_ELIGIBILITY

  authority_state:
    UNBOUND

  policy_epoch:
    UNKNOWN

  required_invariants:
    - I-RPOL-001
    - I-RPOL-002
    - I-RPOL-003
    - I-RPOL-004
    - I-RPOL-006
    - I-RPOL-007
    - I-RPOL-008
    - I-RPOL-009
    - I-RPOL-010
    - I-RPOL-011
    - I-RPOL-012
    - I-RPOL-014
    - I-RPOL-015
    - I-RPOL-017
    - I-RPOL-018
    - I-RPOL-019
    - I-RPOL-020

  mutation_permission:
    UNKNOWN

  finality:
    UNFINALIZED
```

---

# 93. Policy proof capsule

```yaml
proof_capsule:

  claim:
    "Route R is policy-eligible under routing policy P."

  class:
    DERIVED

  required:
    - exact route identity
    - exact policy version/epoch
    - applicable hard-rule set
    - scope
    - regime
    - freshness
    - candidate capability
    - decision receipt

  does_not_prove:
    - route output truth
    - authority
    - execution success
    - canon status
    - finality

  invalidation_conditions:
    - policy epoch changed
    - route changed
    - component changed
    - scope changed
    - regime changed
    - mode changed
    - exception revoked
```

---

# 94. Policy failure modes

```yaml
failure_modes:

  F-RPOL-001:
    name: DEFAULT_CAPTURE_POLICY
    description: generic handler allowed to shadow specialist

  F-RPOL-002:
    name: FIRST_MATCH_POLICY
    description: registry ordering becomes implicit semantic priority

  F-RPOL-003:
    name: SILENT_FALLBACK
    description: substitution permitted without disclosure

  F-RPOL-004:
    name: UNKNOWN_TO_ALLOW
    description: unknown critical constraint treated as permit

  F-RPOL-005:
    name: SCOPE_LEAK
    description: route allowed outside component scope

  F-RPOL-006:
    name: REGIME_LEAK
    description: policy decision reused in incompatible regime

  F-RPOL-007:
    name: STALE_POLICY
    description: old policy epoch continues governing routes

  F-RPOL-008:
    name: MODE_POLICY_BYPASS
    description: inactive/unvalidated mode treated as active

  F-RPOL-009:
    name: CAPABILITY_AUTHORITY_CONFUSION
    description: routable capability treated as authorized capability

  F-RPOL-010:
    name: PROVENANCE_AMPLIFICATION
    description: repeated source descendants increase apparent support

  F-RPOL-011:
    name: FALLBACK_SEMANTIC_DRIFT
    description: degraded fallback treated as equivalent

  F-RPOL-012:
    name: CACHE_POLICY_STALENESS
    description: route reused after policy changed

  F-RPOL-013:
    name: EXCEPTION_LEAKAGE
    description: narrow exception becomes generic policy

  F-RPOL-014:
    name: POLICY_SELF_ACTIVATION
    description: candidate policy treated as active by file presence

  F-RPOL-015:
    name: SECURITY_DOWNGRADE
    description: routing optimization bypasses security control

  F-RPOL-016:
    name: GLOBAL_INVALIDATION
    description: local rule change invalidates unrelated routes unnecessarily

  F-RPOL-017:
    name: AMBIGUITY_SUPPRESSION
    description: policy forces selection without legitimate tie-break

  F-RPOL-018:
    name: EFFECT_ROUTE_BYPASS
    description: consequential effect routed without authority/Worker path
```

---

# 95. Repair / recovery

```text
POLICY FAILURE
    ↓
IDENTIFY FAILED RULE
    ↓
IDENTIFY DEPENDENT ROUTES
    ↓
INVALIDATE ONLY DEPENDENT DECISIONS
    ↓
PRESERVE UNAFFECTED ROUTES
    ↓
REPAIR POLICY / CONTEXT / BINDING
    ↓
RE-EVALUATE
```

---

# 96. Policy repair classes

```text
UPDATE_RULE
REVOKE_RULE
ADD_EXCEPTION
REMOVE_EXCEPTION
REBIND_POLICY
INVALIDATE_ROUTE_CACHE
REVALIDATE_ROUTE
REROUTE
```

---

# 97. Retry rule

Do not re-evaluate identical failed policy decisions expecting a different result.

```text
RetryAllowed
iff
PolicyChanged
OR RouteChanged
OR ContextChanged
OR RegistryChanged
OR ModeChanged
OR RegimeChanged
OR EvidenceChanged
```

---

# 98. Test taxonomy

Routing policy requires:

```text
rule-unit tests
precedence tests
hard-vs-soft tests
default-capture tests
explicit-target tests
ambiguity tests
fallback tests
scope tests
regime tests
freshness tests
mode tests
policy-epoch tests
route-cache tests
security tests
authority-firewall tests
selective-invalidation tests
```

---

# 99. Constitutional policy tests

```text
T-RPOL-001
specialist + default match
→ specialist eligible/preferred

T-RPOL-002
explicit target missing
→ fail visibly, no silent fallback

T-RPOL-003
two equally valid routes
→ AMBIGUOUS/COMPETING

T-RPOL-004
critical constraint UNKNOWN
→ no ALLOW

T-RPOL-005
route valid in wrong regime
→ DENY/REVALIDATE

T-RPOL-006
policy epoch changes
→ old dependent route decision stale

T-RPOL-007
mode folder exists but mode not validated
→ mode route blocked

T-RPOL-008
Agent capability matches effect
but no authority
→ route may stop at AUTHORITY_REQUIRED

T-RPOL-009
two evidence descendants share root
→ independence not increased

T-RPOL-010
fallback changes semantics
→ DEGRADED/CONDITIONAL explicit

T-RPOL-011
cached route crosses policy epoch
→ invalidate

T-RPOL-012
security-sensitive request matches generic worker
without required security capability
→ DENY

T-RPOL-013
unrelated policy rule changes
→ unrelated route remains reusable

T-RPOL-014
candidate policy file appears
→ does not become active

T-RPOL-015
optimization prefers faster route that violates hard scope rule
→ hard scope rule wins
```

---

# 100. Adversarial policy tests

Inject:

```text
malicious wildcard route
registration-order manipulation
version spoof
stale policy epoch
hidden exception
fallback semantic drift
mode-state spoof
authority-field omission
route-cache poisoning
scope expansion
regime transition
```

Policy should fail closed where appropriate.

---

# 101. Falsifiers

This placeholder can be falsified by:

```text
F1:
authoritative AMOS routing-policy canon defines materially different rule hierarchy

F2:
approved routing implementation enforces a different validated precedence model

F3:
higher-order policy explicitly permits behavior prohibited here

F4:
accepted mode/capability registry defines alternate route-eligibility semantics

F5:
actual AMOS_CORE v4.4 routing implementation requires load-bearing dimensions omitted here
```

If a falsifier succeeds, update/supersede rather than silently preserve.

---

# 102. Source / canon references

```yaml
source_canon:

  primary:
    - AMOS_FULL_BRAIN_OS.json

  supporting_lineage:
    - AMOS_CORE_v4_4
    - RSCF
    - GMEF
    - HML
    - FRACTAL_KNOWLEDGE_NETWORK
    - COMPETING_HYPOTHESES
    - PROVENANCE_TOPOLOGY
    - MVCC_CAS
    - PROOF_BASED_COORDINATION_AVOIDANCE

  authoritative_routing_policy_source:
    status: UNKNOWN/GAP
```

The Full Brain OS source is the primary canon source for this Skill, but preserving its architecture does not establish external empirical validity or prove that this exact routing-policy runtime is implemented. 

---

# 103. Dependency graph

```text
ROUTING_POLICY
│
├── 10_ROUTING/README.md
├── 10_ROUTING/BINDING_RULES.md
├── 10_ROUTING/ROUTING_AUDIT.md
│
├── MODE_REGISTRY
├── CAPABILITY_REGISTRY
├── COMPONENT_REGISTRIES
│   ├── AGENT
│   ├── SKILL
│   ├── ENGINE
│   ├── KERNEL
│   ├── WORKER
│   ├── VALIDATOR
│   └── GENERATOR
│
├── 11_VALIDATION
├── 11_VALIDATION/PROMOTION_GATES.md
├── POLICY_MANIFEST
├── AUTHORITY_REGISTRY
├── PROVENANCE_MANIFEST
├── AUTHORITATIVE_STATE
├── EVENT_BUS
└── STATE_STORE
```

---

# 104. Related artifacts

```yaml
related:

  parent:
    - 25_COGNITIVE_MATRIX
    - 10_ROUTING

  routing:
    - 10_ROUTING/README.md
    - 10_ROUTING/BINDING_RULES.md
    - 10_ROUTING/ROUTING_AUDIT.md
    - ROUTER_REGISTRY
    - ROUTE_RECEIPTS
    - ROUTING_PROTOCOLS

  matrix:
    - MODE_REGISTRY
    - CELL_REGISTRY
    - CELL_CONTRACTS
    - STRUCTURAL_GAPS

  validation:
    - 11_VALIDATION/README.md
    - 11_VALIDATION/PROMOTION_GATES.md

  generators:
    - 12_GENERATORS/GENERATOR_CONTRACT.md

  governance:
    - AUTHORITATIVE_STATE.md
    - POLICY_MANIFEST
    - AUTHORITY_REGISTRY
    - PROVENANCE_MANIFEST
    - SUPERSESSION_REGISTRY
    - ROLLBACK_MANIFEST

  runtime:
    - EVENT_BUS
    - CONTROL_PLANE
    - STATE_STORE
    - WORKER_REGISTRY

  core:
    - AMOS_CORE_v4_4

  relationship_status:
    UNVERIFIED
```

---

# 105. Relation ontology

```text
GOVERNS
CONSTRAINS
PERMITS
DENIES
ESCALATES_TO
REQUIRES
DEPENDS_ON
VALIDATED_BY
AUDITED_BY
AUTHORIZED_BY
PROVENANCE_ROOT
COMPATIBLE_WITH
CONFLICTS_WITH
SUPERSEDES
SUPERSEDED_BY
REVOKES
```

---

# 106. Uncertainty vector

```yaml
routing_policy_uncertainty:

  canon: HIGH
  implementation: HIGH
  policy_epoch: HIGH
  registry_binding: HIGH
  mode_binding: HIGH
  runtime_enforcement: HIGH

  structural_model:
    MEDIUM

  hard_boundary_confidence:
    HIGH
```

The exact policy semantics remain provisional until authoritative source and implementation evidence are recovered.

---

# 107. Completion status

```yaml
completion_status:

  source_canon_references:
    required: true
    status: PARTIAL

  definition_scope:
    required: true
    status: MODEL_DRAFT

  typed_inputs_outputs:
    required: true
    status: MODEL_DRAFT

  state_variables:
    required: true
    status: MODEL_DRAFT

  operators:
    required: true
    status: MODEL_DRAFT

  invariants:
    required: true
    status: MODEL_DRAFT

  dependencies:
    required: true
    status: PARTIAL_UNKNOWN

  hml:
    required: true
    status: MODEL_DRAFT

  control_plane:
    required: true
    status: MODEL_DRAFT

  agents:
    required: true
    status: MODEL_DRAFT

  skills:
    required: true
    status: MODEL_DRAFT

  workflows:
    required: true
    status: MODEL_DRAFT

  protocols:
    required: true
    status: UNKNOWN

  evidence_provenance:
    required: true
    status: MISSING

  uncertainty:
    required: true
    status: PRESENT

  failure_modes:
    required: true
    status: MODEL_DRAFT

  repair_recovery:
    required: true
    status: MODEL_DRAFT

  tests_validators:
    required: true
    status: MODEL_DRAFT

  falsifiers:
    required: true
    status: PRESENT

  active_policy_epoch:
    required: true
    status: UNKNOWN

  enforcement_implementation:
    required: true
    status: UNKNOWN

  policy_validation:
    required: true
    status: NOT_RUN

  authority_binding:
    required: true
    status: UNBOUND
```

---

# 108. Gap registry

```yaml
gaps:

  CRITICAL:
    - authoritative routing-policy canon
    - active routing policy epoch
    - actual policy enforcement implementation
    - component registry bindings
    - mode registry binding
    - route-policy receipt format
    - policy promotion path
    - executed constitutional policy tests

  DECISION_RELEVANT:
    - exact precedence hierarchy
    - tie-break rules
    - fallback policy
    - emergency override policy
    - exception semantics
    - effect-class policy
    - cache expiry semantics
    - security policy integration

  EXPLANATORY:
    - policy examples
    - policy diagrams
    - policy metrics

  COSMETIC:
    - formatting
    - naming harmonization
```

---

# 109. Hard boundaries

```text
PLACEHOLDER != IMPLEMENTED

POLICY_FILE != ACTIVE_POLICY

POLICY_ALLOWED != AUTHORIZED

ADDRESSABLE != VALIDATED

REGISTERED != ACTIVE

ROUTED != BOUND

BOUND != VALIDATED

VALIDATED != AUTHORIZED

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

EVENT != AUTHORITY

FIRST_MATCH != BEST_MATCH

DEFAULT != UNIVERSAL_HANDLER

FALLBACK != SEMANTIC_EQUIVALENCE

CACHE_HIT != CURRENT_VALIDITY

MODE_EXISTS != MODE_ACTIVE

MULTIPLE_MATCHES != CONSENSUS

MULTIPLE_SOURCES != INDEPENDENT_SOURCES

UNKNOWN/GAP != ALLOW

AMBIGUOUS != RESOLVED

COMPETING != CONVERGED

STALE_POLICY != CURRENT_POLICY

POLICY_EXCEPTION != GLOBAL_RULE

POLICY_PASS != ROUTE_TRUTH
```

---

# 110. Current decision

```yaml
decision:

  accept_as_authoritative_routing_policy:
    false

  current_role:
    STRUCTURAL_POLICY_PLACEHOLDER

  current_epistemic_class:
    UNKNOWN/GAP

  policy_state:
    INACTIVE_UNVERIFIED

  authority_state:
    NONE

  safe_use:
    - reserve routing-policy architecture
    - define provisional routing constraints
    - guide router and binding implementation
    - prevent default capture
    - define H/M/L routing discipline
    - define fallback and reuse rules
    - expose policy gaps
    - design constitutional tests

  unsafe_use:
    - treat this file as active policy
    - issue route authority
    - silently activate modes
    - silently allow fallback
    - override higher-order governance
    - claim routing implementation conforms
```

---

# 111. Final proof capsule

```yaml
proof_capsule:

  claim:
    "ROUTING_POLICY.md defines the active authoritative routing policy for AMOS."

  class:
    UNKNOWN/GAP

  established:
    - structural AMOS-aligned routing-policy model
    - integrity-first routing constraints
    - H/M/L routing policy
    - specialist/default discipline
    - scope/regime/freshness constraints
    - provenance-aware routing requirements
    - capability/authority firewall
    - route-reuse and invalidation model
    - fallback/recovery model

  not_established:
    - active policy epoch
    - runtime enforcement
    - canonical precedence rules
    - implementation
    - validation receipts
    - policy promotion
    - policy authority

  load_bearing_gaps:
    - authoritative source
    - policy manifest
    - policy epoch
    - router implementation
    - mode registry
    - component registries
    - enforcement path
    - executed tests

  competing:
    - another authoritative AMOS routing policy may exist

  falsifiers:
    - recovered canon defines materially different routing policy
    - runtime policy engine validates a different rule hierarchy
    - higher-order policy supersedes this contract

  confidence_ceiling:
    implementation_claims: 0
    structural_model_usefulness: MODERATE

  final_status:
    - PLACEHOLDER
    - UNVALIDATED
    - UNKNOWN/GAP
    - NON_AUTHORITATIVE
    - INACTIVE_UNVERIFIED
```

```

This version makes `ROUTING_POLICY.md` the **policy layer above route selection but below authority**, rather than duplicating `README`, `BINDING_RULES`, or `ROUTING_AUDIT`. The primary Full Brain OS canon specifically supports the material-relevance rule, explicit uncertainty/gap handling, and conservative routing discipline; it does not by itself prove this exact policy implementation exists.
```

---

00_ROOT_MOC|AMOS MOC

---
**Related:** [[00_HOME]] · [[COGNITIVE_MATRIX_MOC]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: routing_policy
node_type: note
path: 25_COGNITIVE_MATRIX/10_ROUTING/ROUTING_POLICY.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: AMOS_RSCF_NODES
claim_class: AMOS_MODEL

---
**MOC:** [[10_ROUTING_MOC]]
```

---

**Related:** [[25_COGNITIVE_MATRIX_MOC]]

