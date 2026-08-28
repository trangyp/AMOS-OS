---
title: 10_ROUTING — Binding Rules
type: rule
source: 25_COGNITIVE_MATRIX/10_ROUTING
artifact: BINDING_RULES.md
artifact_id: 25_cognitive_matrix_10_routing_binding_rules
origin_architect: Trang Phan
steward: Trang Phan
system: AMOS OS
plane: 25_COGNITIVE_MATRIX
segment: 25_COGNITIVE_MATRIX/10_ROUTING
artifact_kind: RULE
path: 25_COGNITIVE_MATRIX/10_ROUTING/BINDING_RULES.md
tags:
  - 10_routing
  - 25_cognitive_matrix
  - AMOS
  - AMOS_CORE
  - AMOS_CORE_v4_4
  - AMOS_OS
  - BINDING_RULES
  - COGNITIVE_MATRIX
  - ROUTING
  - amos_os
  - binding
  - binding_rules.md
  - canon/cognitive-matrix
  - canon/universe
  - cognitive_matrix
  - matrix
  - routing
  - rscf
  - rule
  - rules
  - {'identity':-None}
  - placeholder_expanded
version: 0.2.0
updated: '2026-08-27'
status: PLACEHOLDER_EXPANDED
epistemic_class: AMOS_MODEL
canonical_status: UNKNOWN/GAP
implementation_status: NOT_ESTABLISHED
validation_status: NOT_ESTABLISHED
executable_binding: NOT_ESTABLISHED
ingestion_action: ADD_ONLY
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: 25_COGNITIVE_MATRIX
  regime: canon_placeholder
  confidence_ceiling: source_supported
  provenance_independence: NOT_ESTABLISHED
---


## 0. Canonical Status

`BINDING_RULES.md` is an **ADD-ONLY placeholder-expanded artifact** for the **25_COGNITIVE_MATRIX** plane segment.

It reserves the canonical slot for the AMOS framework family named **10_ROUTING — Binding Rules**.

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

# 10_ROUTING — Binding Rules

> **Class:** `MATRIX_INFRASTRUCTURE_PLACEHOLDER`
>
> **Origin architect / steward:** Trang Phan
>
> **Status:** `PLACEHOLDER / UNVALIDATED`
>
> **Conclusion class:** `UNKNOWN/GAP`
>
> **AMOS_CORE target:** `v4.4`
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


# 0. Purpose

`BINDING_RULES.md` defines the AMOS contract for determining **what may bind to what, under which scope, version, mode, regime, authority, provenance, capability, and dependency conditions** inside `10_ROUTING`.

Routing answers:

> Which candidate component/path should receive or handle a request?

Binding answers:

> Which exact identity/version/configuration is attached to the request after routing?

These must remain separate.

```text
ROUTE_SELECTED
!= BINDING_VALID

BINDING_VALID
!= EXECUTION_AUTHORIZED

EXECUTION_AUTHORIZED
!= EFFECT_COMMITTED
```

The routing layer must not silently transform selection into authority.

---

# 1. Core routing law

The primary routing law is:

> **Route only to the smallest compatible capability set that can satisfy the declared objective without weakening provenance, scope, regime, freshness, policy, authority, or integrity requirements.**

Therefore:

```text
FIRST_MATCH
!= BEST_MATCH

DEFAULT
!= UNIVERSAL_HANDLER

CAPABILITY_MATCH
!= POLICY_MATCH

POLICY_MATCH
!= AUTHORITY

ADDRESSABLE
!= VALIDATED

REGISTERED
!= ACTIVE

ACTIVE
!= AUTHORIZED_FOR_THIS_REQUEST
```

---

# 2. Routing versus binding

Define routing:

[
R(q,C)
\rightarrow
{c_1,c_2,\dots,c_n}
]

where:

* (q) = request/query/task;
* \(C\) = candidate component set.

Define binding:

[
B(q,c^*,ctx)
\rightarrow
BindingRecord
]

where (c^*) is the selected candidate after compatibility checks.

Routing may return multiple candidates.

Binding must bind one exact identity or explicitly preserve ambiguity.

---

# 3. Binding object

A binding is modeled as:

[
B=
\langle
Request,
Target,
Role,
Version,
Capabilities,
Scope,
Mode,
Regime,
Policy,
Authority,
Dependencies,
Provenance,
Freshness,
State
\rangle
]

A valid binding must be explicit enough to answer:

```text
What was bound?
Why was it bound?
Which version?
For what role?
For which scope?
Under which mode?
Under which policy?
Against which registry state?
Which dependencies were assumed?
How fresh was the binding?
Can the route be replayed?
What invalidates it?
```

---

# 4. Binding targets

Routing may bind requests to:

```text
Kernel
Engine
Skill
Agent
Worker
Workflow
Mode
Validator
Generator
Registry
Data source
Evidence source
RSCF node
GMEF object
Policy evaluator
Event handler
State store
Tool adapter
Recovery handler
Fallback path
```

Presence in this list does not assert that all these bindings are implemented.

---

# 5. Binding classes

```yaml
binding_classes:

  B0_IDENTITY:
    purpose:
      - bind canonical object identity
      - bind exact version/hash

  B1_CAPABILITY:
    purpose:
      - bind request to compatible capability

  B2_MODE:
    purpose:
      - bind execution/reasoning mode

  B3_DEPENDENCY:
    purpose:
      - bind load-bearing dependency

  B4_POLICY:
    purpose:
      - bind active governing policy

  B5_PROVENANCE:
    purpose:
      - bind evidence/source ancestry

  B6_RUNTIME:
    purpose:
      - bind concrete runtime implementation

  B7_WORKER:
    purpose:
      - bind bounded executor

  B8_RECOVERY:
    purpose:
      - bind fallback/rollback/repair path

  B9_AUTHORITY:
    purpose:
      - bind valid authority reference
    hard_rule:
      routing_cannot_create_authority: true
```

---

# 6. Routing lifecycle

```text
REQUEST_RECEIVED
    ↓
REQUEST_TYPED
    ↓
SCOPE_RESOLVED
    ↓
MODE_RESOLVED
    ↓
CANDIDATES_DISCOVERED
    ↓
CAPABILITY_FILTERED
    ↓
COMPATIBILITY_FILTERED
    ↓
POLICY_FILTERED
    ↓
REGIME/FRESHNESS_FILTERED
    ↓
CONFLICT_CHECKED
    ↓
CANDIDATE_RANKED
    ↓
BINDING_PROPOSED
    ↓
BINDING_VALIDATED
```

Terminal outcomes:

```text
BOUND
AMBIGUOUS
NO_ROUTE
CONFLICT
STALE
POLICY_BLOCKED
AUTHORITY_REQUIRED
UNKNOWN/GAP
```

---

# 7. Binding lifecycle

```text
UNBOUND
    ↓
CANDIDATE_BINDING
    ↓
IDENTITY_BOUND
    ↓
VERSION_BOUND
    ↓
SCOPE_BOUND
    ↓
MODE_BOUND
    ↓
DEPENDENCIES_BOUND
    ↓
POLICY_BOUND
    ↓
PROVENANCE_BOUND
    ↓
VALIDATED_BINDING
```

Execution-sensitive bindings may additionally require:

```text
AUTHORITY_BOUND
→ EXECUTION_ELIGIBLE
```

---

# 8. Typed routing request

```yaml
routing_request:

  request_id: UNKNOWN

  objective:
    task_type: UNKNOWN
    requested_output: UNKNOWN
    consequence_class: UNKNOWN

  target:
    subsystem: UNKNOWN
    artifact_type: UNKNOWN
    capability: UNKNOWN

  scope:
    system: UNKNOWN
    domain: UNKNOWN
    hml: UNKNOWN
    environment: UNKNOWN
    assumptions: []

  mode:
    requested_mode: UNKNOWN
    prohibited_modes: []

  regime:
    id: UNKNOWN
    constraints: []

  temporal:
    decision_time: null
    max_route_age: UNKNOWN

  policy:
    policy_epoch: UNKNOWN

  provenance:
    required_source_types: []
    independence_required: UNKNOWN

  execution:
    effect_class: UNKNOWN
    authority_required: UNKNOWN

  fallback:
    allowed: true
```

---

# 9. Typed routing output

```yaml
routing_decision:

  route_id: UNKNOWN
  request_id: UNKNOWN

  candidates_considered: []

  selected:
    component_id: UNKNOWN
    component_type: UNKNOWN
    version: UNKNOWN
    hash: UNKNOWN

  binding:
    role: UNKNOWN
    scope: UNKNOWN
    mode: UNKNOWN
    regime: UNKNOWN
    policy_epoch: UNKNOWN

  reasoning_metadata:
    matched_capabilities: []
    rejected_candidates: []
    unresolved_conflicts: []

  validation:
    binding_valid: UNKNOWN
    compatibility_valid: UNKNOWN
    freshness_valid: UNKNOWN

  authority:
    required: UNKNOWN
    authority_ref: UNKNOWN
    valid: UNKNOWN

  status:
    UNKNOWN/GAP

  confidence_ceiling: 0
```

---

# 10. Binding record

```yaml
binding_record:

  binding_id: UNKNOWN
  route_id: UNKNOWN

  request:
    request_id: UNKNOWN

  bound_component:
    component_id: UNKNOWN
    component_type: UNKNOWN
    version: UNKNOWN
    hash: UNKNOWN

  registry:
    registry_id: UNKNOWN
    registry_version: UNKNOWN
    registry_hash: UNKNOWN

  capability:
    capability_id: UNKNOWN
    capability_version: UNKNOWN

  scope:
    system: UNKNOWN
    hml: UNKNOWN
    environment: UNKNOWN

  mode:
    mode_id: UNKNOWN
    mode_version: UNKNOWN

  regime:
    regime_id: UNKNOWN

  policy:
    policy_epoch: UNKNOWN

  authority:
    authority_ref: UNKNOWN

  dependencies:
    load_bearing: []
    optional: []

  provenance:
    roots: []

  temporal:
    bound_at: null
    valid_until: null

  state:
    observed_read_set: []

  status:
    UNVALIDATED_BINDING
```

---

# 11. Binding state variables

```yaml
routing_state:

  router:
    router_id: UNKNOWN
    version: UNKNOWN
    contract_hash: UNKNOWN

  registry_state:
    registry_version: UNKNOWN
    registry_hash: UNKNOWN

  request_state:
    request_id: UNKNOWN
    request_type: UNKNOWN

  candidate_state:
    discovered: []
    compatible: []
    rejected: []
    ambiguous: []

  scope_state:
    hml: UNKNOWN
    regime: UNKNOWN
    environment: UNKNOWN

  policy_state:
    policy_epoch: UNKNOWN

  binding_state:
    selected: UNKNOWN
    status: UNBOUND

  authority_state:
    required: UNKNOWN
    bound: false

  recovery_state:
    fallback_available: UNKNOWN
```

---

# 12. Routing operators

Candidate operators:

```text
parse_route_request()
resolve_request_type()
resolve_scope()
resolve_hml()
resolve_mode()
discover_candidates()
lookup_registry()
match_capability()
match_schema()
match_version()
check_dependency_compatibility()
check_policy_compatibility()
check_regime_compatibility()
check_freshness()
check_authority_requirement()
rank_candidates()
detect_ambiguity()
bind_identity()
bind_version()
bind_mode()
bind_dependencies()
bind_policy()
bind_provenance()
emit_binding_record()
invalidate_binding()
resolve_fallback()
```

These are contract-level placeholders until actual implementation is recovered.

---

# 13. Core binding invariants

## I-BIND-001 — Exact identity

A binding must identify an exact target.

```text
unknown identity
→ no valid binding
```

## I-BIND-002 — Version binding

A binding must not silently float between incompatible versions.

## I-BIND-003 — Registry snapshot binding

The route must record the registry state from which the target was selected.

## I-BIND-004 — Capability compatibility

Bound component must declare the required capability.

## I-BIND-005 — Capability is not authority

```text
CAPABILITY != AUTHORITY
```

## I-BIND-006 — Scope compatibility

Candidate scope must include the requested scope or explicitly narrow it.

## I-BIND-007 — Regime compatibility

A component validated only in regime A cannot silently bind in regime B.

## I-BIND-008 — Freshness

Stale registry/component/policy state blocks binding where load-bearing.

## I-BIND-009 — Policy compatibility

A route cannot bypass active policy.

## I-BIND-010 — No default capture

A generic/default candidate must not shadow a more specific valid candidate.

## I-BIND-011 — Explicit name fail closed

An explicit request for component X must not silently fall back to Y if X does not exist or is invalid.

## I-BIND-012 — Ambiguity visibility

If multiple equally valid candidates remain:

```text
AMBIGUOUS
```

not arbitrary selection.

## I-BIND-013 — Provenance visibility

Binding to an evidence source must preserve ancestry.

## I-BIND-014 — Dependency completeness

Load-bearing dependencies of the bound target must be known.

## I-BIND-015 — No silent dependency substitution

Missing dependency A cannot silently become dependency B because it appears similar.

## I-BIND-016 — Binding does not commit

```text
BOUND != COMMITTED
```

## I-BIND-017 — Binding does not activate

```text
BOUND != ACTIVE
```

## I-BIND-018 — Binding does not validate

```text
ADDRESSABLE != VALIDATED
```

## I-BIND-019 — Unknown fails closed

```text
UNKNOWN/GAP != PASS
```

## I-BIND-020 — Binding must be invalidatable

Every binding should define what state changes invalidate it.

---

# 14. Route ranking law

Ranking must only occur after hard compatibility filtering.

Correct:

```text
DISCOVER
→ FILTER INVALID
→ FILTER INCOMPATIBLE
→ FILTER POLICY-BLOCKED
→ FILTER STALE
→ THEN RANK
```

Incorrect:

```text
RANK EVERYTHING
→ choose highest score
→ hope it is valid
```

Hard gates override scores.

---

# 15. Candidate score

A provisional score may be:

[
Score(c)
========

w_1 Specificity
+w_2 CapabilityFit
+w_3 ScopeFit
+w_4 Freshness
+w_5 Validity
+w_6 DependencyFit
-w_7 Risk
]

But:

```text
Score
cannot override
hard invariant failure
```

Weights are `UNKNOWN/GAP` until authoritative routing canon exists.

---

# 16. Specificity precedence

Candidate preference may follow:

```text
explicit exact target
>
specialized compatible target
>
domain-general target
>
default fallback
```

provided every candidate is valid.

This prevents default capture.

---

# 17. Explicit binding

If a request says:

```text
agent = RepairAgent
```

then:

```text
RepairAgent unavailable
→ FAIL / UNKNOWN
```

not:

```text
→ DefaultAgent
```

unless the request explicitly permits fallback.

---

# 18. Implicit binding

If no explicit candidate is requested, router may select among compatible candidates.

It must retain:

```text
candidates considered
selection rule
why others were rejected
```

for audit/replay.

---

# 19. Default fallback rule

Default fallback may only be used when:

```text
no explicit candidate requested
AND no specialized compatible candidate available
AND policy permits fallback
AND fallback scope is valid
```

Default is not a universal handler.

---

# 20. Ambiguity rule

If:

```text
Candidate A = valid
Candidate B = valid
A and B incomparable
```

then:

```text
AMBIGUOUS
```

Possible next actions:

```text
ask for discriminating context
run additional validator
preserve competing route
apply explicit policy tie-breaker
```

Registration order is not a valid tie-breaker unless canon explicitly says so.

---

# 21. H/M/L routing applicability

## H — Governance / strategic routing

Routes among:

```text
control-plane services
canon/governance systems
high-level domains
policy paths
finalization paths
```

## M — Orchestration routing

Routes among:

```text
agents
skills
engines
workflows
mode families
validators
generators
```

## L — Local execution routing

Routes among:

```text
kernels
workers
tool adapters
specific handlers
local state shards
```

---

# 22. Recursive routing

Each level may route recursively.

```text
H domain router
    ↓
M subsystem router
    ↓
L capability router
```

AMOS should retrieve/select only the dependency path needed to materially change the outcome.

---

# 23. Scope routing

A route must bind its applicability envelope.

```yaml
binding_scope:
  system: UNKNOWN
  domain: UNKNOWN
  hml: UNKNOWN
  environment: UNKNOWN
  population: UNKNOWN
  assumptions: []
```

No silent cross-domain routing.

---

# 24. Regime routing

Mode/component selection may depend on regime.

```text
stable regime
→ local fast path may be valid

regime shift
→ invalidate/re-evaluate route
```

A route itself inherits regime validity.

---

# 25. Freshness routing

Candidates may have different freshness requirements.

```yaml
freshness:
  registry_max_age: UNKNOWN
  capability_max_age: UNKNOWN
  policy_max_age: UNKNOWN
  source_max_age: UNKNOWN
```

No universal freshness threshold should be invented.

---

# 26. Policy binding

Every governed route should bind the policy epoch used for selection.

```yaml
policy_binding:
  policy_id: UNKNOWN
  policy_epoch: UNKNOWN
  policy_hash: UNKNOWN
```

If the policy epoch changes, dependent bindings may become stale.

---

# 27. Authority binding

Routing may identify that authority is required.

It must not create the authority.

```text
Router
→ "authority required"

Control plane
→ validates/grants authority
```

Binding record may reference an authority grant only after that grant exists.

---

# 28. Authority specificity

Authority must bind:

```text
principal
operation
target
scope
time
delegate
```

A generic capability token should not authorize unrelated routes.

---

# 29. Agent binding

An Agent binding should include:

```yaml
agent_binding:
  agent_id: UNKNOWN
  agent_version: UNKNOWN
  role: UNKNOWN
  capabilities: []
  tools: []
  modes: []
  scope: UNKNOWN
  policy_epoch: UNKNOWN
  authority: NONE
```

Agent selection is cognition routing, not effect authority.

---

# 30. Skill binding

```yaml
skill_binding:
  skill_id: UNKNOWN
  version: UNKNOWN
  capability: UNKNOWN
  required_invariants: []
  worker_ref: UNKNOWN
  effect_class: UNKNOWN
```

Skill binding must not weaken worker requirements.

Required invariant composition should be monotonic:

[
I_{effective}
=============

I_{skill}
\cup
I_{worker}
\cup
I_{policy}
]

not replacement.

---

# 31. Engine binding

Engine binding should identify:

```text
engine identity
version
kernel dependencies
state model
scope
regime
input/output contract
```

An engine may compute but does not receive world-effect authority automatically.

---

# 32. Kernel binding

Kernel routing should prefer exact deterministic contracts.

```text
kernel name
version
input schema
output schema
invariant set
```

Kernel binding should minimize ambiguity.

---

# 33. Worker binding

Worker binding has higher burden.

```yaml
worker_binding:
  worker_id: UNKNOWN
  version: UNKNOWN
  declared_effect_class: UNKNOWN
  required_invariants: []
  allowed_targets: []
  authority_required: true
  idempotency_required: UNKNOWN
```

A Worker may execute only when infrastructure grants the appropriate authority.

---

# 34. Validator binding

Validator selection must bind:

```text
validation class
target type
validator version
scope
regime
contract hash
```

A validator that cannot handle the target must not be selected by convenience.

---

# 35. Generator binding

Generator selection must bind:

```text
artifact type
generator version
template
schema
scope
policy
```

Generator availability does not permit self-promotion.

---

# 36. Mode binding

Mode binding should answer:

```text
Which mode?
Why?
For which scope?
For how long?
Under which policy?
What invalidates it?
```

Possible structure:

```yaml
mode_binding:
  mode_id: UNKNOWN
  mode_family: UNKNOWN
  version: UNKNOWN
  scope: UNKNOWN
  regime: UNKNOWN
  policy_epoch: UNKNOWN
  valid_until: null
```

---

# 37. Mode-family conflicts

If two mutually exclusive modes both match:

```text
COMPETING_MODE_BINDING
```

unless policy explicitly resolves precedence.

---

# 38. Workflow binding

Workflow routing should distinguish:

```text
canonical workflow
ad-hoc plan
```

Canonical workflow:

```text
declared state machine
named invariants
explicit transitions
```

Ad-hoc plan:

```text
dynamic event stream
governed per consequential event
```

Do not force all agent plans into canonical workflow bindings.

---

# 39. Event-handler binding

Event routing must match:

```text
event type
schema version
producer scope
handler capability
policy
idempotency semantics
```

Receiving an event does not create authority.

---

# 40. Evidence binding

Evidence routing must preserve source type.

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL
DECISION
UNKNOWN
```

Binding multiple descendants from one ancestry must not create false independence.

---

# 41. Provenance binding

For each bound source:

```yaml
provenance_binding:
  source_id: UNKNOWN
  source_version: UNKNOWN
  root_ancestry: UNKNOWN
  dependency_edge: UNKNOWN
  freshness: UNKNOWN
```

---

# 42. Data binding

Data sources should bind:

```text
dataset/source
schema
version
timestamp semantics
availability time
scope
privacy/access constraints
```

A route cannot assume data access merely because a source is relevant.

---

# 43. Schema binding

Schema binding should be exact.

```yaml
schema_binding:
  schema_id: UNKNOWN
  version: UNKNOWN
  hash: UNKNOWN
```

Silent schema substitution is prohibited.

---

# 44. Protocol binding

Protocol selection may depend on:

```text
transport
message schema
version
reliability
ordering
security
idempotency
```

Protocol availability is not authority.

---

# 45. Control-plane requirements

The routing layer should remain below infrastructure authority.

```text
Request
   ↓
Routing / Binding
   ↓
Capability selected
   ↓
Validation
   ↓
Infrastructure control plane
   ↓
Authority
   ↓
Worker/effect
```

Routing must not short-circuit this path.

---

# 46. Routing fast path

AMOS v4.4-style fast path may be used only when:

```text
dependency closure known
route previously validated
registry version compatible
provenance compatible
scope unchanged
regime unchanged
freshness valid
no conflict
no authority-sensitive change
```

Then the existing binding may be reused.

---

# 47. Fast-path invalidation

Rebind when:

```text
registry changed
candidate version changed
policy changed
mode changed
regime changed
source stale
dependency invalid
authority requirement changed
conflict introduced
```

---

# 48. MVCC binding model

Conceptually:

```text
read registry at version R1
select candidate C
validate binding
before activation verify registry still R1
```

If registry state changed:

```text
STALE_BINDING
```

---

# 49. Binding read set

```yaml
binding_read_set:

  - artifact: ROUTER_REGISTRY
    version: UNKNOWN
    hash: UNKNOWN
    load_bearing: true

  - artifact: CAPABILITY_REGISTRY
    version: UNKNOWN
    hash: UNKNOWN
    load_bearing: true

  - artifact: MODE_REGISTRY
    version: UNKNOWN
    hash: UNKNOWN
    load_bearing: true

  - artifact: POLICY
    version: UNKNOWN
    hash: UNKNOWN
    load_bearing: true
```

---

# 50. Binding CAS rule

[
BindingCommitAllowed
\Rightarrow
CurrentReadSet
==============

ObservedReadSet
]

where applicable.

This is a conceptual AMOS_CORE-style state discipline, not proof that the current routing implementation has MVCC.

---

# 51. Route cache

Cached routes may be reused only within their declared validity envelope.

```yaml
route_cache:
  route_id: UNKNOWN
  registry_version: UNKNOWN
  policy_epoch: UNKNOWN
  regime: UNKNOWN
  valid_until: null
```

A cached route that outlives one load-bearing dependency becomes stale.

---

# 52. Dependency binding

Dependencies should be typed:

```text
REQUIRES
OPTIONAL
PROVIDES
CONFLICTS_WITH
SUPERSEDES
FALLBACK_FOR
GOVERNED_BY
VALIDATED_BY
```

---

# 53. Dependency compatibility

A candidate with incompatible load-bearing dependencies is not routable.

Example:

```text
Skill requires schema v3
Runtime only supports schema v2
→ incompatible binding
```

No silent downgrade.

---

# 54. Optional dependency semantics

Optional does not mean invisible.

Optional dependencies should still record:

```text
present?
used?
effect on output?
fallback behavior?
```

---

# 55. Fallback binding

A fallback route should declare:

```yaml
fallback:
  primary: UNKNOWN
  alternate: UNKNOWN
  trigger: UNKNOWN
  semantic_equivalence: UNKNOWN
  degradation: UNKNOWN
```

A fallback that changes semantics must be explicit.

---

# 56. Degraded mode

If the ideal route is unavailable, route may enter:

```text
DEGRADED
```

only when policy permits and user/system requirements still remain valid.

Degraded mode should expose lost guarantees.

---

# 57. No-route semantics

If no valid route exists:

```text
NO_ROUTE
```

is a legitimate result.

Do not invent a generic route merely to preserve fluency.

---

# 58. Conflict semantics

Potential conflicts:

```text
duplicate exact route
multiple specialized handlers
version incompatibility
mode conflict
policy conflict
scope mismatch
provenance conflict
worker effect mismatch
```

Conflict must remain visible.

---

# 59. Tie-breakers

Allowed tie-breakers require explicit governance.

Potential examples:

```text
higher specificity
validated status
exact scope match
freshness
lower consequence
lower dependency burden
```

Do not use:

```text
registration order
filesystem order
random first result
```

unless explicitly designed.

---

# 60. Routing confidence

Route confidence should represent routing evidence only.

[
C_{route}
\le
\min(
C_{identity},
C_{capability},
C_{scope},
C_{dependency},
C_{policy},
C_{freshness}
)
]

It must not be confused with truth confidence of the target component's output.

---

# 61. Routing uncertainty vector

```yaml
routing_uncertainty:

  identity: UNKNOWN
  capability: UNKNOWN
  scope: UNKNOWN
  regime: UNKNOWN
  temporal: UNKNOWN
  dependency: UNKNOWN
  policy: UNKNOWN
  provenance: UNKNOWN
```

Spend additional routing effort only where uncertainty can change the selected path.

---

# 62. Routing agents

Possible roles:

### ROUTER_AGENT

Builds candidate set.

No authority.

### BINDING_REVIEW_AGENT

Checks identity, scope and dependency compatibility.

### MODE_ROUTER_AGENT

Selects compatible mode family.

### CAPABILITY_ROUTER_AGENT

Routes by capability contract.

### DEPENDENCY_AUDITOR_AGENT

Inspects dependency closure.

### CONFLICT_ROUTER_AGENT

Preserves competing paths.

### FALLBACK_PLANNER_AGENT

Proposes safe fallback.

No routing agent can authorize world effects.

---

# 63. Routing Skills

Possible Skills:

```text
resolve-capability
resolve-agent
resolve-skill
resolve-engine
resolve-kernel
resolve-worker
resolve-mode
resolve-validator
resolve-generator
resolve-workflow
bind-dependencies
check-route-compatibility
check-route-freshness
compare-routes
resolve-fallback
invalidate-binding
```

---

# 64. Routing Engine

Possible routing engines:

```text
Capability Routing Engine
Mode Routing Engine
Dependency Binding Engine
Policy Routing Engine
Fallback Engine
Conflict Routing Engine
```

These are provisional architectural roles.

---

# 65. Routing kernels

Candidate deterministic primitives:

```text
match_id()
match_version()
match_capability()
match_scope()
match_regime()
match_schema()
compare_priority()
check_policy()
check_freshness()
check_dependency_set()
detect_ambiguity()
validate_binding_hash()
```

---

# 66. Worker routing

Effect-producing worker selection should happen only after capability and governance checks.

```text
proposal
→ worker capability match
→ invariant requirements
→ policy
→ authority
→ worker binding
```

---

# 67. Agent/Worker separation

Hard boundary:

```text
Agent selects/proposes
Worker executes
Infrastructure authorizes
```

No routing rule may collapse these roles.

---

# 68. Skill/Worker composition

Effective requirements:

[
Req_{effective}
===============

Req_{skill}
\cup
Req_{worker}
\cup
Req_{policy}
]

Routing must never replace stricter worker requirements with weaker Skill requirements.

---

# 69. Event routing

Event routing should use typed event identity.

```yaml
event_route:
  event_type: UNKNOWN
  schema_version: UNKNOWN
  handler_id: UNKNOWN
  handler_version: UNKNOWN
  idempotency_scope: UNKNOWN
```

An unknown event type should fail closed or quarantine.

---

# 70. Routing event taxonomy

```text
ROUTING_REQUESTED
ROUTING_SCOPE_RESOLVED
ROUTING_MODE_RESOLVED
ROUTING_CANDIDATES_DISCOVERED
ROUTING_CANDIDATE_REJECTED
ROUTING_AMBIGUOUS
ROUTING_NO_ROUTE
ROUTING_SELECTED
BINDING_PROPOSED
BINDING_VALIDATED
BINDING_STALE
BINDING_INVALIDATED
BINDING_REPLACED
FALLBACK_SELECTED
```

---

# 71. Routing event envelope

```yaml
routing_event:

  event_id: UNKNOWN
  type: UNKNOWN

  request_id: UNKNOWN
  route_id: UNKNOWN
  binding_id: UNKNOWN

  candidate_id: UNKNOWN
  candidate_version: UNKNOWN

  registry_version: UNKNOWN
  policy_epoch: UNKNOWN
  regime: UNKNOWN

  correlation_id: UNKNOWN
  causation_id: UNKNOWN

  status: UNKNOWN

  timestamp: null
```

---

# 72. Binding protocols

Potential protocols:

```text
capability discovery
registry lookup
binding negotiation
mode negotiation
version negotiation
fallback negotiation
conflict escalation
rebind
binding invalidation
```

Exact protocols remain `UNKNOWN/GAP`.

---

# 73. Validation of bindings

A binding should pass:

```text
identity
version
capability
scope
regime
freshness
dependency
policy
provenance
```

For execution:

```text
authority
worker invariant compatibility
effect classification
```

---

# 74. Binding validator result

```yaml
binding_validation:

  identity: UNKNOWN
  version: UNKNOWN
  capability: UNKNOWN
  scope: UNKNOWN
  regime: UNKNOWN
  freshness: UNKNOWN
  dependencies: UNKNOWN
  policy: UNKNOWN
  provenance: UNKNOWN
  authority: UNKNOWN

  overall:
    UNKNOWN/GAP
```

---

# 75. Validation versus binding

```text
Binding
= connects request to candidate

Validation
= determines whether binding satisfies contract

Promotion/Activation
= separate governance
```

---

# 76. Routing and promotion gates

Relationship:

```text
ROUTING
→ chooses candidate

VALIDATION
→ checks candidate/binding

PROMOTION GATES
→ determine lifecycle elevation

CONTROL PLANE
→ authorizes consequential activation/effect
```

---

# 77. Routing and generator

Generator routing must select:

```text
generator ID
version
template
schema
scope
```

Generator output remains candidate.

---

# 78. Routing and validator

Validator routing must bind the correct validation class.

Example:

```text
schema validator
cannot substitute for
provenance validator
```

---

# 79. Routing and modes

A route may depend on active modes.

Example:

```text
RESEARCH mode
→ research-capable agent/skill

EXECUTION mode
→ effect path requires control-plane authorization
```

Modes influence routing but do not create authority.

---

# 80. Routing and cognitive cells

For Cognitive Matrix cells:

```text
cell address
→ cell registry lookup
→ cell contract
→ mode compatibility
→ H/M/L compatibility
→ binding
```

A cell with:

```text
UNVALIDATED_BINDING
```

must not be silently treated as validated.

---

# 81. Cell routing status

```yaml
cell_route:
  address: UNKNOWN
  registry_status: UNKNOWN
  contract_status: UNKNOWN
  binding_status: UNVALIDATED_BINDING
  hml_status: UNKNOWN
  mode_status: UNKNOWN
```

---

# 82. RSCF routing

RSCF routing should select only nodes/dependencies that can materially affect the answer.

```text
bootstrap
→ H domain
→ M subsystem
→ L detail
→ raw evidence only if required
```

Do not load every branch by default.

---

# 83. GMEF routing

Governance-sensitive operations should route into GMEF/control paths when:

```text
authority required
policy relevant
mutation consequential
finality relevant
```

---

# 84. Causal routing

Causal questions may require routing to causal-validation capabilities.

```text
association question
→ statistical/correlation path

causal effect question
→ causal evidence path
```

Do not route both as equivalent.

---

# 85. Scope firewall

If a candidate is valid only for:

```text
system A
regime R1
scale M
```

routing to:

```text
system B
regime R2
scale H
```

requires explicit compatibility evidence.

---

# 86. Provenance firewall

Routing must not select evidence solely by repeated presence.

```text
10 summaries
from one origin
```

may still represent one evidence root.

---

# 87. Security routing

Security-sensitive capabilities should bind:

```text
permission scope
sandbox
trusted implementation
secret access policy
network access policy
```

Routing must never infer permission from capability.

---

# 88. Data-access routing

A request may identify a useful source but still lack access.

```text
relevant source
!= connected source
!= authorized source
```

The route should expose access gap.

---

# 89. Cost/resource routing

Routing may consider:

```text
latency
compute cost
token cost
network cost
risk
```

only after integrity requirements pass.

Optimization must never weaken correctness.

---

# 90. Adaptive complexity routing

Possible route depth:

```text
C0:
direct/local capability

C1:
single specialist

C2:
specialist + validator

C3:
multiple competing/causal/provenance paths

C4:
governance-critical multi-layer route
```

Escalate when stakes or uncertainty require it.

---

# 91. Stop condition

Routing stops when the selected path is sufficient for:

```text
Claim Sufficiency
Decision Sufficiency
Action Sufficiency
```

Do not continue routing to redundant agents/skills once no outcome-changing uncertainty remains.

---

# 92. Failure modes

```yaml
failure_modes:

  F-ROUTE-001:
    name: DEFAULT_CAPTURE
    description: generic default shadows specialized candidate

  F-ROUTE-002:
    name: REGISTRATION_ORDER_ROUTING
    description: first registered candidate wins without semantic rule

  F-ROUTE-003:
    name: SILENT_FALLBACK
    description: explicit missing target replaced without permission

  F-ROUTE-004:
    name: CAPABILITY_AUTHORITY_CONFUSION
    description: routable capability treated as authorized effect

  F-ROUTE-005:
    name: STALE_REGISTRY
    description: route based on outdated registry

  F-ROUTE-006:
    name: VERSION_DRIFT
    description: bound component changes version silently

  F-ROUTE-007:
    name: SCOPE_LEAK
    description: component routed outside validated scope

  F-ROUTE-008:
    name: REGIME_LEAK
    description: route reused after regime transition

  F-ROUTE-009:
    name: POLICY_BYPASS
    description: route ignores active policy

  F-ROUTE-010:
    name: DEPENDENCY_SUBSTITUTION
    description: incompatible dependency silently replaced

  F-ROUTE-011:
    name: FALSE_INDEPENDENCE
    description: repeated evidence routes counted as independent

  F-ROUTE-012:
    name: AMBIGUITY_SUPPRESSION
    description: multiple valid routes collapsed arbitrarily

  F-ROUTE-013:
    name: WORKER_EFFECT_MISMATCH
    description: worker effect class differs from declared capability

  F-ROUTE-014:
    name: INVARIANT_WEAKENING
    description: routing composition drops required invariant

  F-ROUTE-015:
    name: ROUTE_CACHE_STALENESS
    description: cached binding survives changed load-bearing state

  F-ROUTE-016:
    name: UNKNOWN_TO_ROUTE
    description: unknown critical field treated as compatible

  F-ROUTE-017:
    name: MODE_CONFLICT
    description: incompatible modes selected simultaneously

  F-ROUTE-018:
    name: PROVENANCE_LOSS
    description: evidence route drops ancestry information
```

---

# 93. Recovery

```text
ROUTING FAILURE
    ↓
IDENTIFY FAILED BINDING EDGE
    ↓
INVALIDATE AFFECTED ROUTE
    ↓
PRESERVE UNAFFECTED ROUTES
    ↓
REFRESH RELEVANT REGISTRY/POLICY
    ↓
RE-DISCOVER MINIMUM NECESSARY CANDIDATES
    ↓
RE-BIND
```

Avoid global rerouting unless dependency closure requires it.

---

# 94. Rebind triggers

```text
component superseded
registry version changed
policy epoch changed
mode changed
regime changed
scope changed
authority requirement changed
dependency failed
validator status changed
```

---

# 95. Retry rule

```text
RetryRoute
iff
RegistryChanged
OR RequestChanged
OR ContextChanged
OR PolicyChanged
OR ModeChanged
OR TransientFailureResolved
```

Identical failed routes should not be retried indefinitely.

---

# 96. Tests

Required categories:

```text
identity routing
version routing
specificity routing
default fallback
explicit-name fail closed
ambiguity
scope
regime
freshness
policy
dependency
mode
agent routing
skill routing
worker routing
validator routing
generator routing
cell routing
cache invalidation
CAS
replay
security
```

---

# 97. Constitutional routing tests

```text
T-ROUTE-001
explicit unknown agent
→ NO_ROUTE / FAIL
not DefaultAgent

T-ROUTE-002
specialist + default both match
→ specialist wins

T-ROUTE-003
two equally specialized candidates
→ AMBIGUOUS

T-ROUTE-004
candidate capability matches but policy denies
→ no binding

T-ROUTE-005
candidate valid in wrong regime
→ no binding

T-ROUTE-006
stale registry
→ binding stale/revalidated

T-ROUTE-007
skill requires I-A + worker requires I-B
→ effective requirements {I-A,I-B}

T-ROUTE-008
unknown invariant
→ fail closed

T-ROUTE-009
worker effect class mismatches skill declaration
→ no execution binding

T-ROUTE-010
same route replay under unchanged registry
→ deterministic equivalent binding

T-ROUTE-011
registry changes after route
→ stale binding rejected where load-bearing

T-ROUTE-012
fallback changes semantics
→ degraded/conditional status explicit

T-ROUTE-013
two evidence paths share ancestry root
→ not independent confirmation

T-ROUTE-014
mode folder exists but mode unvalidated
→ cannot bind as ACTIVE mode
```

---

# 98. Adversarial tests

Challenge routing with:

```text
duplicate names
spoofed version
stale registry
hidden fallback
malicious generic handler
scope mismatch
policy epoch drift
provenance alias
mode collision
worker class mismatch
route-cache poisoning
```

Routing should fail closed or preserve ambiguity.

---

# 99. Falsifiers

This placeholder is provisional.

```text
F1:
Authoritative AMOS routing canon defines materially different binding semantics.

F2:
Existing runtime router uses another validated precedence model.

F3:
Approved Cognitive Matrix manifest specifies different routing lifecycle.

F4:
Mode registry requires additional load-bearing binding dimensions.

F5:
Higher-order policy allows a behavior currently marked forbidden.
```

Successful falsifier requires update/supersession.

---

# 100. RSCF completion state

```yaml
rscf:

  claim_id:
    RSCF-CM-ROUTING-BINDING-RULES-001

  claim:
    "This file defines the authoritative AMOS routing and binding rules for 10_ROUTING."

  claim_class:
    UNKNOWN/GAP

  scope:
    system: AMOS_OS
    subsystem: COGNITIVE_MATRIX
    package: 10_ROUTING
    artifact: BINDING_RULES.md

  evidence: []

  provenance: []

  load_bearing_premises:
    - authoritative routing canon recovered
    - routing registry recovered
    - capability registry recovered
    - mode registry recovered
    - active policy model recovered
    - runtime routing implementation recovered
    - routing tests executed

  dependencies:
    - AUTHORITATIVE_STATE
    - MODE_REGISTRY
    - CELL_REGISTRY
    - CELL_CONTRACTS
    - 11_VALIDATION
    - 12_GENERATORS
    - POLICY_MANIFEST
    - PROVENANCE_MANIFEST
    - WORKER_REGISTRY
    - AGENT_REGISTRY
    - SKILL_REGISTRY

  competing:
    - authoritative routing specification may exist elsewhere in corpus

  falsifiers:
    - recovered canon defines different routing semantics
    - approved runtime contradicts this placeholder
    - higher-order manifest specifies different precedence/binding rules

  regime:
    architecture: UNKNOWN
    runtime: UNKNOWN

  freshness: null

  confidence_ceiling: 0

  status:
    PLACEHOLDER
```

---

# 101. GMEF completion state

```yaml
gmef:

  artifact:
    AMOS-CM-10-ROUTING-BINDING-RULES

  governance_status:
    PLACEHOLDER

  governed_operations:
    - ROUTE_SELECTION
    - COMPONENT_BINDING
    - MODE_BINDING
    - DEPENDENCY_BINDING
    - WORKER_BINDING
    - VALIDATOR_BINDING
    - GENERATOR_BINDING
    - FALLBACK_SELECTION

  authority_state:
    UNBOUND

  policy_epoch:
    UNKNOWN

  required_invariants:
    - I-BIND-001
    - I-BIND-002
    - I-BIND-005
    - I-BIND-006
    - I-BIND-008
    - I-BIND-010
    - I-BIND-011
    - I-BIND-012
    - I-BIND-014
    - I-BIND-015
    - I-BIND-019

  mutation_permission:
    UNKNOWN

  finality:
    UNFINALIZED
```

---

# 102. Binding proof capsule

```yaml
proof_capsule:

  conclusion:
    "Component C is the selected valid binding for request R."

  class:
    DERIVED

  required:
    - request identity
    - component identity/version
    - registry version
    - capability match
    - scope match
    - regime match
    - policy compatibility
    - dependency compatibility
    - freshness

  does_not_prove:
    - output correctness
    - authority
    - canon status
    - effect permission
    - finality

  invalidation_conditions:
    - registry changed
    - component changed
    - policy changed
    - scope changed
    - regime changed
    - dependency invalidated
```

---

# 103. Related artifacts

```yaml
related:

  parent:
    - 25_COGNITIVE_MATRIX
    - 10_ROUTING

  matrix:
    - CELL_REGISTRY
    - CELL_CONTRACTS
    - MODE_REGISTRY
    - STRUCTURAL_GAPS

  validation:
    - 11_VALIDATION/README.md
    - 11_VALIDATION/PROMOTION_GATES.md

  generators:
    - 12_GENERATORS/GENERATOR_CONTRACT.md

  registries:
    - AGENT_REGISTRY
    - SKILL_REGISTRY
    - ENGINE_REGISTRY
    - KERNEL_REGISTRY
    - WORKER_REGISTRY
    - VALIDATOR_REGISTRY
    - GENERATOR_REGISTRY
    - WORKFLOW_REGISTRY

  governance:
    - AUTHORITATIVE_STATE.md
    - POLICY_MANIFEST
    - PROVENANCE_MANIFEST
    - AUTHORITY_REGISTRY

  runtime:
    - EVENT_BUS
    - STATE_STORE
    - CONTROL_PLANE

  core:
    - AMOS_CORE_v4_4

  relationship_status:
    UNVERIFIED
```

---

# 104. Relation ontology

```text
ROUTES_TO
BINDS_TO
REQUIRES
OPTIONAL
FALLBACK_TO
CONFLICTS_WITH
COMPATIBLE_WITH
INCOMPATIBLE_WITH
VALIDATED_BY
GOVERNED_BY
AUTHORIZED_BY
PROVENANCE_ROOT
SUPERSEDES
SUPERSEDED_BY
```

---

# 105. Dependency hierarchy

```text
TIER 0
policy / authority / root architecture

TIER 1
registries / mode system / capability contracts

TIER 2
routing and binding validation

TIER 3
runtime candidates / workers / events

TIER 4
fallbacks / explanatory metadata
```

A lower-priority convenience route cannot override a Tier-0 or Tier-1 incompatibility.

---

# 106. Required completion status

```yaml
completion_status:

  source_canon_references:
    required: true
    status: MISSING

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

  runtime_validation:
    required: true
    status: NOT_RUN

  registry_binding:
    required: true
    status: UNBOUND

  policy_binding:
    required: true
    status: UNBOUND

  authority_binding:
    required: true
    status: UNBOUND
```

---

# 107. Gap registry

```yaml
gaps:

  CRITICAL:
    - authoritative routing source/canon
    - actual routing registry
    - actual binding registry
    - precedence rules
    - active mode registry
    - policy binding
    - runtime implementation
    - executed routing tests

  DECISION_RELEVANT:
    - exact tie-breakers
    - fallback semantics
    - route-cache semantics
    - binding expiry
    - routing security model
    - route performance budgets

  EXPLANATORY:
    - routing diagrams
    - metrics
    - example route traces

  COSMETIC:
    - naming harmonization
    - formatting
```

---

# 108. Hard boundaries

```text
PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

REGISTERED != ACTIVE

ACTIVE != AUTHORIZED

ROUTED != BOUND

BOUND != VALIDATED

BOUND != AUTHORIZED

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

MODE_EXISTS != MODE_ACTIVE

DEFAULT != UNIVERSAL_HANDLER

FIRST_MATCH != BEST_MATCH

LATEST_VERSION != VALID_VERSION

SCHEMA_MATCH != SEMANTIC_MATCH

MULTIPLE_MATCHES != CONSENSUS

FALLBACK != EQUIVALENT

UNKNOWN/GAP != PASS

AMBIGUOUS != RESOLVED

STALE_BINDING != CURRENT_BINDING
```

---

# 109. Current decision

```yaml
decision:

  accept_as_authoritative_routing_contract:
    false

  current_role:
    STRUCTURAL_PLACEHOLDER

  current_epistemic_class:
    UNKNOWN/GAP

  current_authority:
    NONE

  safe_use:
    - define provisional routing architecture
    - expose binding requirements
    - guide agent/skill/worker routing design
    - prevent default-capture bugs
    - support matrix structural audits
    - define test requirements

  unsafe_use:
    - claim router implemented
    - claim candidate validated because routable
    - activate modes from file presence
    - create authority from capability
    - silently fallback
    - silently select ambiguous candidates
```

---

# 110. Final proof capsule

**Claim**

`10_ROUTING / BINDING_RULES.md` defines the complete operative AMOS routing and binding subsystem.

**Current class**

`UNKNOWN/GAP`

**What this artifact establishes**

A detailed AMOS-aligned structural model for:

```text
request typing
candidate discovery
capability matching
specificity precedence
scope/regime/freshness
mode binding
dependency binding
policy binding
provenance binding
worker binding
fallbacks
ambiguity
route invalidation
MVCC/CAS-style route freshness
```

**What it does not establish**

It does not prove that:

```text
the router exists
the registries are populated
the precedence rules are canonical
mode bindings are validated
runtime bindings are active
worker routes are authorized
constitutional routing tests pass
```

**Critical gaps**

```text
source/canon
registry
actual precedence policy
mode registry
runtime implementation
validation receipts
policy epoch
authority model
```

**Competing possibility**

Another AMOS/Trang artifact may already contain authoritative routing semantics that differ from this placeholder.

**Falsifier**

Recovery and validation of that source.

**Confidence ceiling**

```text
0 for claims of implementation,
validation, or authority.

Moderate for usefulness as
a structural AMOS routing model.
```

**Final status**

```text
PLACEHOLDER
UNVALIDATED
UNKNOWN/GAP
NON_AUTHORITATIVE
UNBOUND
```

```

This contract keeps routing aligned with the AMOS Full Brain OS integrity boundary: route only what is materially needed, preserve provenance/scope/regime constraints, expose ambiguity instead of forcing a fluent selection, and never let capability selection become authority.
```

---

00_ROOT_MOC|AMOS MOC

---
**Related:** [[00_HOME]] · [[COGNITIVE_MATRIX_MOC]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: binding_rules
node_type: note
path: 25_COGNITIVE_MATRIX/10_ROUTING/BINDING_RULES.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[10_ROUTING_MOC]]

