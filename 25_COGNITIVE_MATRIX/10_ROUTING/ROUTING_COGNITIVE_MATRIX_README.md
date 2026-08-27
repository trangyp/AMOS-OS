---
title: ROUTING COGNITIVE MATRIX README
tags: ['cognitive_matrix', 'routing', 'readme']
---


Below is a **full AMOS-aligned `10_ROUTING/README.md`**, with `BINDING_RULES.md` treated as the detailed sibling contract rather than duplicated. It keeps the subsystem `PLACEHOLDER / UNKNOWN-GAP`, preserves Trang Phan as origin architect/steward, and follows the Full Brain OS rule that architectural structure is not itself implementation or empirical proof.  The Skill’s canon source is `AMOS_FULL_BRAIN_OS.json`; preservation of its ontology/architecture does not establish external empirical validity. 

---
artifact_id: AMOS-CM-10-ROUTING-README
title: "10_ROUTING — Routing Infrastructure Contract"

path_target: "25_COGNITIVE_MATRIX/10_ROUTING/README.md"

artifact_class: MATRIX_INFRASTRUCTURE_PLACEHOLDER
contract_class: ROUTING_SUBSYSTEM_CONTRACT
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

authority_class: NON_AUTHORITATIVE_SPECIFICATION
routing_authority: NONE
binding_authority: NONE
execution_authority: NONE
promotion_authority: NONE
canon_authority: NONE
policy_authority: NONE
finality_authority: NONE

risk_class: CONTROL_PLANE_CRITICAL
default_mutation_class: M0_METADATA_UNTIL_PROMOTED
default_reversibility: HIGH_WHILE_PLACEHOLDER

architecture_roles:
  - REQUEST_ROUTING
  - CAPABILITY_ROUTING
  - DOMAIN_ROUTING
  - HML_ROUTING
  - MODE_ROUTING
  - DEPENDENCY_ROUTING
  - VALIDATOR_ROUTING
  - GENERATOR_ROUTING
  - AGENT_ROUTING
  - SKILL_ROUTING
  - ENGINE_ROUTING
  - KERNEL_ROUTING
  - WORKER_ROUTING
  - WORKFLOW_ROUTING
  - EVENT_ROUTING
  - RECOVERY_ROUTING
  - FALLBACK_ROUTING

rscf_role:
  - ROUTING_DECISION_CAPSULE
  - ROUTE_DEPENDENCY_CAPSULE
  - ROUTE_VALIDITY_CAPSULE
  - ROUTE_REUSE_CAPSULE

gmef_role:
  - ROUTING_GOVERNANCE_BOUNDARY
  - ROUTE_POLICY_GATE
  - EFFECT_PATH_SELECTION_GATE
  - BINDING_PRECONDITION

hml_scope:
  H:
    - DOMAIN_SELECTION
    - GOVERNANCE_ROUTING
    - POLICY_ROUTING
    - CONTROL_PLANE_ROUTING
    - SYSTEM_REGIME_ROUTING

  M:
    - SUBSYSTEM_SELECTION
    - AGENT_SKILL_ENGINE_SELECTION
    - MODE_SELECTION
    - VALIDATOR_GENERATOR_SELECTION
    - WORKFLOW_SELECTION
    - DEPENDENCY_BINDING

  L:
    - KERNEL_SELECTION
    - WORKER_SELECTION
    - TOOL_ADAPTER_SELECTION
    - LOCAL_HANDLER_SELECTION
    - PARAMETER_BINDING
    - ID_VERSION_HASH_MATCHING

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
    - ROUTER
    - BINDING

  architecture:
    - MATRIX_INFRASTRUCTURE
    - CONTROL_PLANE
    - KERNEL
    - ENGINE
    - SKILL
    - AGENT
    - WORKER
    - WORKFLOW
    - EVENT_BUS
    - VALIDATOR
    - GENERATOR
    - REGISTRY
    - MODE_REGISTRY
    - CELL_REGISTRY

  reasoning:
    - RSCF
    - GMEF
    - HML
    - FRACTAL_KNOWLEDGE_NETWORK
    - ADAPTIVE_COMPLEXITY
    - PROOF_CAPSULE
    - COMPETING_HYPOTHESES
    - UNCERTAINTY_VECTOR

  routing:
    - REQUEST_ROUTING
    - CAPABILITY_ROUTING
    - DOMAIN_ROUTING
    - MODE_ROUTING
    - DEPENDENCY_ROUTING
    - FALLBACK_ROUTING
    - RECOVERY_ROUTING
    - EVENT_ROUTING
    - ROUTE_REUSE
    - ROUTE_INVALIDATION

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

  scope:
    - SCOPE_FIREWALL
    - REGIME_FIREWALL
    - CAUSAL_FIREWALL
    - FRESHNESS
    - TEMPORAL_VALIDITY
    - ENVIRONMENT_BINDING

  governance:
    - AUTHORITY
    - POLICY
    - INVARIANT
    - MODE_GOVERNANCE
    - ROUTING_POLICY
    - EXECUTION_GOVERNANCE
    - CONFLICT_RESOLUTION
    - SUPERSESSION

  state:
    - MVCC
    - CAS
    - READ_SET
    - WRITE_SET
    - STATE_VERSION
    - REGISTRY_VERSION
    - ROUTE_VERSION
    - EPOCH
    - IDEMPOTENCY

  integrity:
    - ANTI_FABRICATION
    - ANTI_REGRESSION
    - ANTI_DRIFT
    - FAIL_CLOSED
    - SELECTIVE_INVALIDATION
    - REPAIR
    - RECOVERY
    - REPLAY

  assurance:
    - VALIDATION
    - AUDIT
    - OBSERVABILITY
    - FALSIFICATION
    - ADVERSARIAL_VALIDATION
---

# 10_ROUTING — Routing Infrastructure Contract

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

`10_ROUTING` defines the AMOS infrastructure contract responsible for selecting the **smallest valid path** through the AMOS architecture for a given request, claim, decision, validation task, generation task, workflow transition, mode activation, or effect proposal.

The routing subsystem answers:

> **Which domain, subsystem, mode, capability, component, validator, generator, workflow, worker, or recovery path is appropriate for this request under the current state?**

It must not answer:

> **Which component has authority to mutate the world?**

That is a separate control-plane question.

The canonical separation is:

```text
REQUEST
    ↓
ROUTING
    ↓
CANDIDATE PATH
    ↓
BINDING
    ↓
VALIDATION
    ↓
POLICY / AUTHORITY
    ↓
WORKER / EFFECT
```

Routing is therefore **selection and path construction**, not authorization.

---

# 1. Core routing law

The primary AMOS routing rule is:

> **Route only to dependencies that can materially change the outcome, and select the narrowest compatible capability path that preserves scope, regime, freshness, provenance, policy, and integrity constraints.**

This implies:

```text
MORE COMPONENTS
!= BETTER REASONING

MORE AGENTS
!= MORE TRUTH

MORE SKILLS
!= MORE VALIDITY

MORE SOURCES
!= MORE INDEPENDENCE

FIRST MATCH
!= BEST MATCH

DEFAULT
!= UNIVERSAL HANDLER

CAPABILITY
!= AUTHORITY
```

---

# 2. Fractal routing principle

AMOS routing follows the Fractal Knowledge Network pattern:

```text
BOOTSTRAP
    ↓
H DOMAIN
    ↓
M SUBSYSTEM
    ↓
L DETAIL
    ↓
RAW EVIDENCE ONLY IF REQUIRED
```

Routing should descend only as deeply as required.

Default:

```text
DO_NOT_LOAD_UNLESS_REQUIRED
```

for raw evidence or deeply nested subsystems that cannot alter the result.

---

# 3. Routing definition

A route is modeled as:

[
R =
\langle
Request,
Context,
Scope,
Regime,
Mode,
Candidates,
Dependencies,
Policy,
State,
Selection,
Fallback
\rangle
]

The routing function is:

[
Route(q,ctx)
\rightarrow
{P_1,P_2,\ldots,P_n}
]

where each (P_i) is a possible valid path.

A second operation resolves or preserves competition:

[
Resolve(P_1,\ldots,P_n)
\rightarrow
P^*
]

or:

```text
COMPETING / AMBIGUOUS
```

if no defensible unique route exists.

---

# 4. Routing subsystem responsibilities

`10_ROUTING` may be responsible for:

```text
request typing
intent decomposition
scope identification
H/M/L selection
domain selection
mode selection
capability discovery
component discovery
dependency routing
provenance-sensitive evidence routing
validator routing
generator routing
agent routing
skill routing
engine routing
kernel routing
worker routing
workflow routing
event-handler routing
fallback routing
recovery routing
route-cache reuse
route invalidation
```

This is a contract surface.

It does not prove implementation.

---

# 5. Non-responsibilities

`10_ROUTING` must not silently own:

```text
truth determination
canon admission
policy creation
authority issuance
external effect execution
finality
credential creation
permission escalation
empirical validation
runtime mutation
```

Routing may route **to** those services.

It does not become those services.

---

# 6. Routing object model

```yaml
route:

  identity:
    route_id: UNKNOWN
    route_version: UNKNOWN

  request:
    request_id: UNKNOWN
    request_type: UNKNOWN
    objective: UNKNOWN

  context:
    core_version: v4.4
    architecture_version: UNKNOWN
    registry_epoch: UNKNOWN
    policy_epoch: UNKNOWN
    provenance_epoch: UNKNOWN

  scope:
    system: UNKNOWN
    domain: UNKNOWN
    hml: UNKNOWN
    environment: UNKNOWN

  regime:
    regime_id: UNKNOWN

  modes:
    active: []
    required: []
    prohibited: []

  path:
    nodes: []
    edges: []

  candidates:
    considered: []
    rejected: []
    competing: []

  dependencies:
    load_bearing: []
    optional: []

  validation:
    required: []
    receipts: []

  authority:
    required: false
    authority_ref: null

  fallback:
    route_id: null

  freshness:
    valid_until: null

  status:
    UNKNOWN/GAP
```

---

# 7. Route path representation

A route may be represented as a graph:

[
G_R=(V_R,E_R)
]

where nodes may include:

```text
Domain
Subsystem
Mode
Agent
Skill
Engine
Kernel
Worker
Validator
Generator
Workflow
DataSource
EvidenceNode
PolicyEvaluator
RecoveryHandler
```

Edges should be typed.

---

# 8. Route relation ontology

Recommended relation types:

```text
ROUTES_TO
REQUIRES
USES
BINDS_TO
VALIDATED_BY
GOVERNED_BY
AUTHORIZED_BY
PROVENANCE_ROOT
FALLBACK_TO
RECOVERS_WITH
COMPATIBLE_WITH
INCOMPATIBLE_WITH
COMPETING_WITH
SUPERSEDES
```

Untyped graph edges should be avoided for load-bearing routing.

---

# 9. Request classification

Before component routing, classify the request.

Possible top-level classes:

```yaml
request_classes:

  INFORMATION:
    effect_risk: NONE

  ANALYSIS:
    effect_risk: NONE

  RESEARCH:
    effect_risk: NONE

  VALIDATION:
    effect_risk: NONE_TO_LOW

  GENERATION:
    effect_risk: REVERSIBLE

  MODIFICATION:
    effect_risk: VARIABLE

  EXECUTION:
    effect_risk: CONSEQUENTIAL

  GOVERNANCE:
    effect_risk: HIGH

  CANON_MUTATION:
    effect_risk: HIGH

  POLICY_MUTATION:
    effect_risk: CRITICAL

  ROOT_STATE_MUTATION:
    effect_risk: SYSTEM_CRITICAL
```

Routing burden should increase with consequence.

---

# 10. Typed routing input

```yaml
routing_input:

  request:
    request_id: UNKNOWN
    objective: UNKNOWN
    requested_output: UNKNOWN
    consequence_class: UNKNOWN

  user_intent:
    explicit_component: null
    explicit_mode: null
    explicit_scope: null
    fallback_allowed: UNKNOWN

  architecture:
    core_target: v4.4
    architecture_version: UNKNOWN

  state:
    registry_version: UNKNOWN
    mode_registry_version: UNKNOWN
    policy_epoch: UNKNOWN
    provenance_epoch: UNKNOWN

  context:
    domain: UNKNOWN
    environment: UNKNOWN
    regime: UNKNOWN
    hml: UNKNOWN

  constraints:
    required_capabilities: []
    prohibited_capabilities: []
    required_invariants: []

  evidence:
    source_requirements: []
    provenance_requirements: []

  execution:
    effect_class: UNKNOWN
    authority_required: UNKNOWN
```

---

# 11. Typed routing output

```yaml
routing_output:

  route_id: UNKNOWN

  request_id: UNKNOWN

  selected_path:
    - component_id: UNKNOWN
      component_type: UNKNOWN
      role: UNKNOWN
      version: UNKNOWN

  rejected_candidates: []

  competing_candidates: []

  bindings: []

  required_validations: []

  required_authority:
    required: UNKNOWN
    authority_class: UNKNOWN

  fallback:
    available: UNKNOWN
    route: UNKNOWN

  uncertainty:
    identity: UNKNOWN
    capability: UNKNOWN
    scope: UNKNOWN
    regime: UNKNOWN
    freshness: UNKNOWN
    dependency: UNKNOWN

  confidence_ceiling: 0

  status:
    UNKNOWN/GAP
```

---

# 12. Routing state machine

```text
UNROUTED
    ↓
REQUEST_TYPED
    ↓
SCOPE_BOUND
    ↓
HML_BOUND
    ↓
MODE_CONTEXT_BOUND
    ↓
CANDIDATES_DISCOVERED
    ↓
HARD_FILTERS_APPLIED
    ↓
COMPETING_CHECKED
    ↓
ROUTE_PROPOSED
    ↓
BINDINGS_PROPOSED
    ↓
BINDINGS_VALIDATED
    ↓
ROUTED
```

Alternative terminal states:

```text
NO_ROUTE
AMBIGUOUS
COMPETING
POLICY_BLOCKED
AUTHORITY_REQUIRED
STALE
QUARANTINED
UNKNOWN/GAP
```

---

# 13. Core route invariants

## I-ROUTE-001 — Objective first

No route may be selected before the request objective is sufficiently typed.

## I-ROUTE-002 — Smallest sufficient path

Do not activate unrelated domains.

## I-ROUTE-003 — Explicit route precedence

An explicit component request must either resolve to that component or fail visibly.

## I-ROUTE-004 — No silent fallback

Fallback requires explicit permission or declared policy.

## I-ROUTE-005 — Specificity before generic fallback

A valid specialist should not be shadowed by a generic default.

## I-ROUTE-006 — Hard compatibility before ranking

Incompatible candidates are removed before scoring.

## I-ROUTE-007 — Unknown fails closed

```text
UNKNOWN/GAP != PASS
```

## I-ROUTE-008 — Ambiguity visible

Equal/incomparable valid candidates remain `AMBIGUOUS` or `COMPETING`.

## I-ROUTE-009 — Scope preserved

No silent scope expansion.

## I-ROUTE-010 — Regime preserved

No silent cross-regime reuse.

## I-ROUTE-011 — Freshness preserved

Stale routes cannot silently remain active.

## I-ROUTE-012 — Provenance preserved

Evidence routes must retain ancestry.

## I-ROUTE-013 — Correlated sources collapsed

Multiple descendants do not become multiple independent confirmations.

## I-ROUTE-014 — Policy cannot be bypassed

Routing convenience cannot override active policy.

## I-ROUTE-015 — Capability does not create authority

```text
CAPABILITY != AUTHORITY
```

## I-ROUTE-016 — Routing does not commit

```text
ROUTED != COMMITTED
```

## I-ROUTE-017 — Routing does not validate output truth

A valid route does not prove its output correct.

## I-ROUTE-018 — Dependency visibility

Load-bearing dependencies must be recoverable.

## I-ROUTE-019 — No silent dependency substitution

Similar-looking components are not interchangeable without compatibility evidence.

## I-ROUTE-020 — Route must expose invalidation conditions

---

# 14. Candidate discovery

Candidate sources may include:

```text
Agent Registry
Skill Registry
Engine Registry
Kernel Registry
Worker Registry
Mode Registry
Validator Registry
Generator Registry
Workflow Registry
Cell Registry
Capability Registry
```

Discovery should be separated from selection.

```text
DISCOVERED
!= SELECTED
```

---

# 15. Candidate filtering

Hard filters may include:

```text
identity
version
capability
scope
H/M/L
mode
regime
freshness
schema
dependency compatibility
policy
security
effect class
```

A candidate failing a hard filter is removed before ranking.

---

# 16. Candidate ranking

Only after hard filtering may ranking occur.

Candidate score may conceptually include:

[
Score(c)=
w_sSpecificity+
w_cCapability+
w_hHMLFit+
w_rRegimeFit+
w_fFreshness+
w_vValidation
-------------

## w_dDependencyCost

w_kRisk
]

Weights remain `UNKNOWN/GAP`.

No ranking score overrides a hard failure.

---

# 17. Specificity hierarchy

Provisional preference:

```text
EXPLICIT EXACT TARGET
        >
SPECIALIZED VALID TARGET
        >
DOMAIN-SPECIFIC GENERAL TARGET
        >
GLOBAL GENERAL TARGET
        >
DEFAULT FALLBACK
```

This should remain subordinate to actual policy/canon if recovered.

---

# 18. First-match prohibition

Bad routing:

```text
for candidate in registry:
    if candidate.matches:
        return candidate
```

unless registry ordering is itself canonical and validated.

Preferred:

```text
discover
→ filter
→ compare specificity
→ check competition
→ select
```

---

# 19. Explicit component routing

If a request explicitly names:

```text
Skill X
Agent Y
Validator Z
```

the router should resolve that object.

If missing:

```text
EXPLICIT_TARGET_NOT_FOUND
```

not silently choose another component.

---

# 20. Default routing

Default routing may occur only when:

```text
no explicit target
AND no valid specialist
AND default compatible
AND default policy-permitted
AND fallback allowed
```

---

# 21. No-route result

`NO_ROUTE` is a valid outcome.

It is preferable to fabricated compatibility.

```text
NO_ROUTE
>
UNJUSTIFIED_ROUTE
```

under AMOS integrity ordering.

---

# 22. H/M/L routing

AMOS routing should bind H/M/L relative to the current task.

## H — domain/governance

Examples:

```text
Science
Finance
Architecture
Governance
Security
Knowledge
Runtime
```

## M — subsystem

Examples:

```text
Validation
Routing
Generators
Modes
Agents
Skills
Workflow
Provenance
```

## L — detail/execution

Examples:

```text
specific kernel
specific worker
specific validator
specific schema
specific evidence node
```

---

# 23. Recursive H/M/L routing

Each selected node may recursively decompose.

```text
H
└── M
    └── L
        └── sub-L
```

The router should stop when further descent cannot materially change the answer or action.

---

# 24. Domain routing

Domain selection should be evidence-driven.

```yaml
domain_route:
  domain_id: UNKNOWN
  confidence: 0
  reason: UNKNOWN
  dependencies: []
```

Multiple domains may remain active when the task is genuinely cross-domain.

---

# 25. Cross-domain routing

Cross-domain reasoning requires a firewall.

```text
STRUCTURAL ANALOGY
!= CAUSAL TRANSFER
```

If a route crosses domain boundaries, it should record:

```text
source domain
target domain
mapping type
assumptions
validation status
```

---

# 26. Mode routing

Mode routing chooses the operating/reasoning mode.

Potential mode families include:

```text
REASONING_MODES
EPISTEMIC_MODES
CAUSAL_MODES
SCOPE_MODES
REGIME_MODES
FRESHNESS_MODES
PROVENANCE_MODES
AUTHORITY_MODES
VALIDATION_MODES
EXECUTION_MODES
RECOVERY_MODES
FINALIZATION_MODES
DEPLOYMENT_MODES
SECURITY_MODES
RESOURCE_MODES
HANDOFF_CONTINUITY_MODES
```

Existence of a folder does not imply valid mode semantics.

---

# 27. Mode binding contract

```yaml
mode_route:

  requested_mode: UNKNOWN

  selected:
    mode_id: UNKNOWN
    family: UNKNOWN
    version: UNKNOWN

  scope: UNKNOWN
  regime: UNKNOWN
  policy_epoch: UNKNOWN

  status:
    UNVALIDATED_BINDING
```

---

# 28. Mode conflict

If multiple mutually exclusive modes are simultaneously required:

```text
MODE_CONFLICT
```

until a declared policy or discriminating requirement resolves the conflict.

---

# 29. Adaptive complexity routing

AMOS complexity levels:

```text
C0 — Direct
C1 — Compact
C2 — Structured
C3 — Deep
C4 — Maximum
```

Routing should start at the lowest sufficient complexity.

Escalate for:

```text
high stakes
irreversibility
novelty
weak evidence
stale evidence
contradiction
causal ambiguity
scope mismatch
regime shift
competing hypotheses
governance impact
low trust
explicit maximum-detail request
```

---

# 30. Agent routing

Agent routing answers:

> Which stochastic reasoning role should contribute?

Agent registry binding should include:

```yaml
agent_route:
  agent_id: UNKNOWN
  version: UNKNOWN
  role: UNKNOWN
  capabilities: []
  scope: UNKNOWN
  modes: []
  tools: []
  status: UNKNOWN
```

Agent selection does not grant execution authority.

---

# 31. Agent routing precedence

Potential precedence:

```text
explicit agent
>
specialized role agent
>
domain agent
>
general agent
>
fallback
```

subject to compatibility and policy.

---

# 32. Agent routing failure

An explicit unknown Agent should fail closed.

This avoids:

```text
unknown specialist
→ silent DefaultAgent
```

which creates hidden semantic substitution.

---

# 33. Skill routing

Skill routing should match:

```text
requested capability
input contract
output contract
scope
effect class
required invariants
dependencies
```

A Skill may expose capability but not authority.

---

# 34. Skill composition

If multiple Skills are required:

```text
Skill A
+
Skill B
```

their invariant requirements should combine monotonically.

[
I_{combined}
============

I_A
\cup
I_B
\cup
I_{policy}
]

Routing must not drop stricter requirements.

---

# 35. Engine routing

Engine routing selects repeatable domain computation.

Binding should include:

```text
engine ID
version
input contract
output contract
kernel dependencies
state model
scope
regime
```

---

# 36. Kernel routing

Kernel selection should favor exact deterministic primitives.

Potential checks:

```text
exact operation
input type
output type
version
invariant set
side-effect classification
```

---

# 37. Worker routing

Worker routing has elevated burden because Workers may execute effects.

Routing must identify:

```text
worker identity
worker version
effect class
allowed targets
required invariants
authority requirement
idempotency requirement
```

Worker selection still does not authorize execution.

---

# 38. Agent → Worker firewall

Hard AMOS separation:

```text
Agent
= proposal / reasoning

Infrastructure
= authority

Worker
= bounded execution
```

Routing may construct:

```text
Agent → Worker candidate path
```

but the control plane must authorize the transition.

---

# 39. Validator routing

Validator routing should be validation-class-specific.

Example:

```text
schema validation
→ schema validator

provenance validation
→ provenance validator

causal validation
→ causal validator
```

One validator should not silently substitute for another validation class.

---

# 40. Generator routing

Generator routing selects a generator based on:

```text
artifact type
template
schema
version
scope
policy
dependencies
```

A routed generator produces a candidate, not automatically a promoted artifact.

---

# 41. Workflow routing

Distinguish:

```text
CANONICAL WORKFLOW
```

from:

```text
AD-HOC AGENT PLAN
```

Canonical workflows may have enforced transition graphs.

Ad-hoc plans may remain event sequences validated per consequential event.

---

# 42. Event routing

Event routing should bind:

```text
event type
schema version
producer identity
consumer capability
ordering requirement
idempotency scope
policy
```

Hard boundary:

```text
EVENT RECEIVED
!= AUTHORITY GRANTED
```

---

# 43. Evidence routing

Evidence selection should preserve epistemic type:

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL
DECISION
UNKNOWN
```

Evidence routing must not silently treat all retrieved content as equivalent.

---

# 44. Provenance-aware evidence routing

For evidence set (E):

[
Roots(E)=
{root(e):e\in E}
]

Independent support should count effective ancestry roots, not file count.

---

# 45. RSCF routing

RSCF route traversal should focus on load-bearing premises.

```text
claim
→ premise
→ dependency
→ evidence
```

Only open deeper evidence when it can alter the conclusion.

---

# 46. GMEF routing

Governance-sensitive routes should enter GMEF/control paths when they involve:

```text
authority
policy
mutation
canon promotion
runtime activation
irreversible effect
finality
```

---

# 47. Dependency routing

Dependencies must be classified:

```text
LOAD_BEARING
OPTIONAL
EXPLANATORY
COSMETIC
```

Only load-bearing dependency failure should necessarily block the route.

---

# 48. Dependency closure

Define:

[
Closure(R)
==========

{d:
d\text{ can materially alter route validity}}
]

The router should establish this closure before fast-path reuse.

---

# 49. Dependency edge types

```text
REQUIRES
OPTIONAL
PROVIDES
VALIDATED_BY
GOVERNED_BY
PROVENANCE_ROOT
CONFLICTS_WITH
FALLBACK_FOR
SUPERSEDES
```

---

# 50. Registry architecture

`10_ROUTING` may depend on registries such as:

```text
CAPABILITY_REGISTRY
AGENT_REGISTRY
SKILL_REGISTRY
ENGINE_REGISTRY
KERNEL_REGISTRY
WORKER_REGISTRY
MODE_REGISTRY
VALIDATOR_REGISTRY
GENERATOR_REGISTRY
WORKFLOW_REGISTRY
CELL_REGISTRY
```

These registries remain dependencies, not automatic truth sources.

---

# 51. Registry entry contract

```yaml
registry_entry:
  component_id: UNKNOWN
  component_type: UNKNOWN
  version: UNKNOWN
  capabilities: []
  scope: UNKNOWN
  modes: []
  dependencies: []
  status: UNKNOWN
  provenance: []
```

---

# 52. Registry validity

```text
REGISTERED
!= VALIDATED

VALIDATED
!= ACTIVE

ACTIVE
!= AUTHORIZED
```

Routing should inspect status explicitly.

---

# 53. Registry freshness

A route should capture:

```yaml
registry_snapshot:
  registry_id: UNKNOWN
  version: UNKNOWN
  hash: UNKNOWN
  observed_at: null
```

A changed load-bearing registry may invalidate the route.

---

# 54. MVCC-style routing

Conceptual AMOS pattern:

```text
READ REGISTRY R@V1
        ↓
COMPUTE ROUTE
        ↓
VALIDATE BINDINGS
        ↓
BEFORE CONSEQUENTIAL USE:
COMPARE CURRENT REGISTRY
```

If:

```text
CurrentVersion != ObservedVersion
```

then:

```text
STALE_ROUTE
```

where the changed state is load-bearing.

---

# 55. Route read set

```yaml
route_read_set:

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

  - artifact: PROVENANCE_STATE
    version: UNKNOWN
    hash: UNKNOWN
    load_bearing: false
```

---

# 56. Route write set

Routing itself should normally have minimal mutation.

Potential writes:

```yaml
route_write_set:
  cache: []
  receipts: []
  metrics: []
  state_mutation: []
```

World-effect mutation is outside the router.

---

# 57. Route cache

A route may be cached only with explicit validity metadata.

```yaml
cached_route:
  route_id: UNKNOWN
  request_signature: UNKNOWN
  registry_version: UNKNOWN
  policy_epoch: UNKNOWN
  mode_version: UNKNOWN
  regime: UNKNOWN
  valid_until: null
```

---

# 58. Cache reuse gate

Reuse requires:

```text
dependency closure unchanged
registry compatible
policy unchanged
mode compatible
scope compatible
regime compatible
freshness valid
no new conflict
```

---

# 59. v4.4 proof-based coordination avoidance

AMOS v4.4-style local routing reuse is appropriate only when local independence is established.

Fast path:

```text
KNOWN DEPENDENCY CLOSURE
AND PROVENANCE INDEPENDENCE
AND SCOPE COMPATIBILITY
AND REGIME COMPATIBILITY
AND FRESHNESS
AND NO CONFLICT
```

then:

```text
reuse local proof / route
```

Otherwise escalate.

This is a reasoning pattern; it does not claim the Markdown layer literally implements distributed coordination avoidance.

---

# 60. Route invalidation

Invalidate a route when a load-bearing condition changes.

Examples:

```text
component superseded
registry changed
policy changed
mode changed
scope changed
regime shifted
validation expired
authority requirement changed
dependency failed
security context changed
```

---

# 61. Selective invalidation

Do not invalidate unrelated routes.

Example:

```text
Worker W1 changed
→ invalidate routes binding W1

Preserve routes using W2
```

This follows the AMOS repair principle.

---

# 62. Fallback routing

Fallback is a governed branch.

```yaml
fallback_route:
  primary: UNKNOWN
  alternate: UNKNOWN
  activation_condition: UNKNOWN
  semantic_equivalence: UNKNOWN
  degraded_guarantees: []
```

---

# 63. Semantic fallback

A fallback may be:

```text
EQUIVALENT
DEGRADED
DIFFERENT_SEMANTICS
```

Only the first should be treated as transparent substitution.

---

# 64. Degraded routing

When routing degrades, output should expose lost guarantees.

Example:

```yaml
degraded_route:
  status: DEGRADED
  missing:
    - specialist capability
  retained:
    - read-only analysis
  lost_guarantees:
    - domain-specific validation
```

---

# 65. Recovery routing

Recovery paths may include:

```text
retry
alternate worker
alternate Skill
rollback path
repair workflow
human escalation
no-action safe state
```

Recovery path selection should itself obey routing rules.

---

# 66. Retry routing

Do not retry an identical failed route without changed conditions.

```text
RetryAllowed
iff
InputChanged
OR DependencyChanged
OR CandidateChanged
OR RegistryChanged
OR PolicyChanged
OR TransientFailureResolved
```

---

# 67. Competing routes

If multiple routes have valid but incomparable support:

```text
COMPETING
```

The router should preserve:

```yaml
competing_routes:
  - route_id: R1
    strengths: []
    weaknesses: []

  - route_id: R2
    strengths: []
    weaknesses: []
```

---

# 68. Route discrimination

Prefer the cheapest high-information test that can distinguish competing routes.

Examples:

```text
check missing capability
check exact version
check mode policy
check scope
check current registry
```

before launching expensive multi-agent evaluation.

---

# 69. Scope firewall

No routing outside validated scope without explicit revalidation.

```text
scope A
→ route A valid

scope B
→ UNKNOWN until compatibility established
```

---

# 70. Regime firewall

A route can become invalid after regime change.

Examples:

```text
offline → production
simulation → live
development → security-critical
read-only → mutation
```

---

# 71. Freshness firewall

Freshness may apply separately to:

```text
registry
policy
mode
source
validation receipt
authority
runtime state
```

No single universal freshness duration should be invented.

---

# 72. Causal firewall

Routing a causal question requires capabilities that can distinguish:

```text
association
correlation
mechanism
confounding
mediation
feedback
causal effect
```

A generic analogy engine should not satisfy a causal question.

---

# 73. Authority firewall

Routing may conclude:

```text
AUTHORITY_REQUIRED
```

but cannot synthesize that authority.

Hard rule:

```text
ROUTE
!= GRANT
```

---

# 74. Policy routing

Requests with governance consequences should route through policy evaluation.

Example:

```text
modify active mode
→ mode policy evaluator

promote canon
→ canon admission policy

execute external effect
→ effect authority policy
```

---

# 75. Security routing

Security-sensitive requests may require specialized routing to:

```text
security validator
sandboxed worker
permission evaluator
secret-safe handler
```

Security capability cannot be inferred from general capability.

---

# 76. Privacy/data routing

Data routing must respect access constraints.

```text
relevant source
!= connected source

connected source
!= authorized source

authorized source
!= permitted for every purpose
```

---

# 77. Execution routing

Consequential actions require an effect-aware route.

```text
PROPOSAL
    ↓
VALIDATION
    ↓
AUTHORITY
    ↓
WORKER
    ↓
EFFECT
```

No direct:

```text
Agent
→ Tool
```

path should be treated as AMOS-governed durable execution unless the infrastructure contract explicitly mediates it.

---

# 78. Execution effect classes

Potential classes:

```text
E0 READ_ONLY
E1 REVERSIBLE_LOCAL
E2 DURABLE_LOCAL
E3 EXTERNAL_REVERSIBLE
E4 EXTERNAL_CONSEQUENTIAL
E5 IRREVERSIBLE_OR_GOVERNANCE_CRITICAL
```

Required routing depth should scale accordingly.

Exact classification remains provisional.

---

# 79. Worker-only durable effect rule

For durable effects:

```text
Agent proposes
Infrastructure authorizes
Worker executes
Evidence returns
```

The router may select the Worker but cannot grant the authority.

---

# 80. Event-bus relationship

The Event Bus is a transport/coordination substrate.

Routing may resolve:

```text
event type → handler
```

but:

```text
event received
!= request authorized
```

---

# 81. Event route record

```yaml
event_route:
  event_type: UNKNOWN
  schema_version: UNKNOWN
  producer: UNKNOWN
  handler: UNKNOWN
  idempotency_scope: UNKNOWN
  authority_required: UNKNOWN
```

---

# 82. Routing event taxonomy

```text
ROUTING_REQUESTED
REQUEST_TYPED
SCOPE_RESOLVED
HML_RESOLVED
MODE_RESOLVED
CANDIDATES_DISCOVERED
CANDIDATE_FILTERED
ROUTE_COMPETING
ROUTE_AMBIGUOUS
ROUTE_SELECTED
BINDING_PROPOSED
BINDING_VALIDATED
ROUTE_STALE
ROUTE_INVALIDATED
FALLBACK_SELECTED
NO_ROUTE
ROUTING_COMPLETED
```

---

# 83. Routing event envelope

```yaml
routing_event:
  event_id: UNKNOWN
  type: UNKNOWN
  route_id: UNKNOWN
  request_id: UNKNOWN
  correlation_id: UNKNOWN
  causation_id: UNKNOWN
  registry_version: UNKNOWN
  policy_epoch: UNKNOWN
  regime: UNKNOWN
  status: UNKNOWN
  timestamp: null
```

---

# 84. Binding subsystem relationship

Detailed binding semantics belong in:

```text
10_ROUTING/BINDING_RULES.md
```

README-level contract:

```text
ROUTING
= candidate path selection

BINDING
= exact identity/version/context attachment
```

The README should reference, not duplicate, the entire sibling contract.

---

# 85. Binding validation

A route is not complete until load-bearing bindings are valid enough.

Minimum checks may include:

```text
identity
version
capability
scope
mode
regime
freshness
dependency
policy
```

Execution routes also need:

```text
authority
worker compatibility
effect classification
```

---

# 86. Relationship to 11_VALIDATION

```text
ROUTING
    ↓
BINDING
    ↓
VALIDATION
```

`11_VALIDATION` determines whether the route/binding satisfies declared contracts.

`10_ROUTING` does not self-certify.

---

# 87. Relationship to Promotion Gates

```text
route selected
→ binding validated
→ candidate may become promotion input
```

Promotion remains separate.

```text
ROUTABLE
!= PROMOTABLE
```

---

# 88. Relationship to 12_GENERATORS

Routing may select an appropriate generator.

```text
request
→ generator route
→ generator candidate
```

Generator output then passes Validation and Promotion Gates.

---

# 89. Relationship to Cognitive Matrix cells

A cell route may require:

```text
cell address
cell contract
binding status
H/M/L
mode
dependencies
provenance
```

A cell that is merely addressable is not necessarily valid.

---

# 90. Cell routing status

```yaml
cell_route:
  address: UNKNOWN
  contract_status: UNKNOWN
  registry_status: UNKNOWN
  binding_status: UNVALIDATED_BINDING
  validation_status: NOT_CELL_VALIDATED
```

---

# 91. Routing protocols

Potential protocols:

```text
request classification protocol
capability discovery protocol
registry lookup protocol
binding negotiation protocol
version negotiation protocol
mode negotiation protocol
fallback protocol
route invalidation protocol
rebind protocol
route replay protocol
```

Exact protocols remain `UNKNOWN/GAP`.

---

# 92. Routing agents

Possible provisional roles:

### ROUTING_COORDINATOR_AGENT

Structures the request and candidate space.

### DOMAIN_ROUTER_AGENT

Determines relevant H-level domain.

### MODE_ROUTER_AGENT

Selects relevant operating mode.

### CAPABILITY_ROUTER_AGENT

Matches capability contracts.

### DEPENDENCY_ROUTER_AGENT

Builds minimum dependency closure.

### PROVENANCE_ROUTER_AGENT

Selects evidence paths without false independence.

### FALLBACK_ROUTER_AGENT

Constructs safe alternatives.

### CONFLICT_ROUTER_AGENT

Preserves competing routes.

All remain non-authoritative.

---

# 93. Routing Skills

Potential Skills:

```text
classify-request
resolve-domain
resolve-hml
resolve-mode
discover-capability
route-agent
route-skill
route-engine
route-kernel
route-worker
route-validator
route-generator
route-workflow
route-evidence
bind-dependency
resolve-fallback
compare-routes
invalidate-route
```

---

# 94. Routing engines

Potential engine layer:

```text
Request Classification Engine
Domain Routing Engine
Capability Routing Engine
Mode Routing Engine
Dependency Routing Engine
Fallback Routing Engine
Conflict Routing Engine
Route Reuse Engine
```

---

# 95. Routing kernels

Possible deterministic primitives:

```text
match_id()
match_version()
match_capability()
match_scope()
match_hml()
match_mode()
match_regime()
match_schema()
check_freshness()
check_policy()
check_dependency_set()
compare_specificity()
detect_ambiguity()
compare_registry_version()
```

---

# 96. Routing protocols and workers

Most routing itself should be read/select behavior.

When route resolution requires external inspection or execution:

```text
Router
→ proposes read/test
Infrastructure
→ authorizes if needed
Worker
→ performs bounded operation
```

---

# 97. Route observability

A route trace should allow reconstruction of:

```text
request
classification
H/M/L
modes
candidates discovered
hard filters
rejected candidates
selected path
bindings
registry versions
policy epoch
fallback
invalidation conditions
```

---

# 98. Route replay

For deterministic routing under unchanged context:

[
Same(Request,Registry,Policy,Mode,Context)
\Rightarrow
Same(Route)
]

unless nondeterminism is explicitly part of the routing contract.

---

# 99. Route receipt

```yaml
route_receipt:

  receipt_id: UNKNOWN
  route_id: UNKNOWN
  request_id: UNKNOWN

  router:
    router_id: UNKNOWN
    version: UNKNOWN

  context:
    architecture_version: UNKNOWN
    registry_version: UNKNOWN
    policy_epoch: UNKNOWN
    regime: UNKNOWN

  selected_path: []

  rejected_candidates: []

  unresolved:
    - UNKNOWN

  confidence_ceiling: 0

  generated_at: null
  valid_until: null
```

---

# 100. Route receipt semantics

A route receipt proves only:

> a particular routing decision was produced under a declared context.

It does not prove:

```text
output truth
authority
execution success
canon validity
finality
```

---

# 101. Route metrics

Potential operational metrics:

```text
route_success_rate
no_route_rate
ambiguity_rate
fallback_rate
stale_route_rate
rebind_rate
default_capture_rate
specialist_hit_rate
registry_miss_rate
policy_block_rate
route_replay_match_rate
mean_route_latency
```

Operational metrics are not correctness proof.

---

# 102. Route quality

Potential quality dimensions:

```yaml
route_quality:
  specificity: UNKNOWN
  capability_fit: UNKNOWN
  scope_fit: UNKNOWN
  dependency_completeness: UNKNOWN
  provenance_quality: UNKNOWN
  freshness: UNKNOWN
  fallback_quality: UNKNOWN
```

---

# 103. Routing uncertainty vector

```yaml
routing_uncertainty:

  objective: UNKNOWN
  identity: UNKNOWN
  capability: UNKNOWN
  scope: UNKNOWN
  hml: UNKNOWN
  mode: UNKNOWN
  regime: UNKNOWN
  freshness: UNKNOWN
  provenance: UNKNOWN
  dependency: UNKNOWN
  execution: UNKNOWN
```

The router should spend effort only where reducing uncertainty can change the route.

---

# 104. Sensitivity

Identify the smallest condition that changes the selected route.

Examples:

```text
mode changes
→ different Agent

effect class changes
→ Worker path introduced

policy epoch changes
→ candidate blocked

scope broadens
→ specialist invalid

regime shifts
→ cached route invalid
```

Fragile routes should be labeled `CONDITIONAL`.

---

# 105. Failure modes

```yaml
failure_modes:

  F-ROUTE-001:
    name: DEFAULT_CAPTURE
    description: generic default shadows valid specialist

  F-ROUTE-002:
    name: FIRST_MATCH_CAPTURE
    description: registry order becomes accidental routing policy

  F-ROUTE-003:
    name: SILENT_FALLBACK
    description: requested component replaced without disclosure

  F-ROUTE-004:
    name: ROUTING_AUTHORITY_LEAKAGE
    description: route selection treated as authority

  F-ROUTE-005:
    name: STALE_REGISTRY
    description: route computed from outdated registry state

  F-ROUTE-006:
    name: VERSION_DRIFT
    description: bound target changes version silently

  F-ROUTE-007:
    name: SCOPE_LEAKAGE
    description: route reused beyond validated scope

  F-ROUTE-008:
    name: REGIME_LEAKAGE
    description: route reused after regime change

  F-ROUTE-009:
    name: POLICY_BYPASS
    description: active policy omitted from route

  F-ROUTE-010:
    name: DEPENDENCY_SUBSTITUTION
    description: incompatible dependency silently replaced

  F-ROUTE-011:
    name: FALSE_INDEPENDENCE
    description: correlated evidence paths treated as independent

  F-ROUTE-012:
    name: AMBIGUITY_SUPPRESSION
    description: competing valid routes collapsed arbitrarily

  F-ROUTE-013:
    name: MODE_CONFLICT
    description: incompatible modes active simultaneously

  F-ROUTE-014:
    name: WORKER_EFFECT_MISMATCH
    description: worker effect exceeds declared route

  F-ROUTE-015:
    name: INVARIANT_WEAKENING
    description: routing drops load-bearing invariant

  F-ROUTE-016:
    name: CACHE_STALENESS
    description: stale cached route reused

  F-ROUTE-017:
    name: UNKNOWN_TO_ROUTE
    description: unknown critical compatibility treated as valid

  F-ROUTE-018:
    name: PROVENANCE_LOSS
    description: evidence ancestry stripped during route

  F-ROUTE-019:
    name: GLOBAL_OVERROUTING
    description: every subsystem activated despite local sufficiency

  F-ROUTE-020:
    name: PREMATURE_SPECIALIZATION
    description: route descends before H/M scope is established
```

---

# 106. Recovery architecture

```text
ROUTE FAILURE
    ↓
IDENTIFY FAILED EDGE
    ↓
INVALIDATE DEPENDENT BINDING
    ↓
PRESERVE UNAFFECTED ROUTE SEGMENTS
    ↓
REFRESH CHANGED REGISTRY/POLICY/MODE
    ↓
RECOMPUTE MINIMUM NECESSARY SUBGRAPH
    ↓
REBIND
```

Global rerouting is last resort.

---

# 107. Route repair

Repair should distinguish:

```text
REPAIR
= preserve route identity, fix invalid edge

REBIND
= replace one binding

REROUTE
= compute alternate path

RESET
= discard route and start again
```

Use the least disruptive sufficient operation.

---

# 108. Test taxonomy

Routing tests should include:

```text
request classification
H/M/L selection
domain routing
explicit component routing
specificity precedence
default behavior
fallback
ambiguity
scope
regime
freshness
mode
policy
registry version
dependency closure
agent selection
skill selection
engine selection
kernel selection
worker selection
validator selection
generator selection
workflow selection
event routing
cache reuse
route invalidation
recovery
security
```

---

# 109. Constitutional routing tests

```text
T-ROUTE-001
explicit unknown agent
→ NO_ROUTE
not DefaultAgent

T-ROUTE-002
specialist + default match
→ specialist selected

T-ROUTE-003
two equal specialists
→ AMBIGUOUS

T-ROUTE-004
candidate matches capability but violates scope
→ reject

T-ROUTE-005
candidate matches capability but policy blocks
→ reject

T-ROUTE-006
candidate valid only in stale regime
→ reject/revalidate

T-ROUTE-007
unknown critical compatibility
→ UNKNOWN/GAP

T-ROUTE-008
skill and worker invariants differ
→ union / strongest applicable constraints

T-ROUTE-009
event handler exists but event unauthorized
→ handler binding does not grant effect authority

T-ROUTE-010
route cache built on old registry
→ stale

T-ROUTE-011
two evidence files share one root
→ one effective provenance root

T-ROUTE-012
mode folder exists but mode unvalidated
→ cannot bind as active

T-ROUTE-013
fallback materially changes semantics
→ mark DEGRADED / CONDITIONAL

T-ROUTE-014
same request/context/registry
→ deterministic equivalent route where declared

T-ROUTE-015
load-bearing dependency changes
→ dependent route invalidated only
```

---

# 110. Adversarial routing tests

Inject:

```text
duplicate candidate names
version spoofing
stale registry
malicious default handler
scope mismatch
mode collision
policy epoch drift
provenance aliasing
worker class mismatch
route-cache poisoning
hidden fallback
```

The router should fail closed or preserve ambiguity.

---

# 111. Security tests

Potential security routing tests:

```text
unauthorized capability exposure
secret-bearing tool routing
sandbox bypass
worker privilege escalation
path traversal through generated routes
malicious registry entry
event-handler spoofing
```

Exact controls remain implementation gaps.

---

# 112. Falsifiers

This placeholder is falsifiable.

```text
F1:
Authoritative AMOS routing canon defines materially different semantics.

F2:
Existing runtime routing implementation demonstrates another validated contract.

F3:
Cognitive Matrix manifest defines different mandatory routing layers.

F4:
Mode registry requires additional load-bearing route dimensions.

F5:
Higher-order AMOS policy explicitly permits a behavior marked forbidden here.

F6:
Binding is canonically defined as part of another subsystem rather than 10_ROUTING.
```

Successful falsifier requires revision or supersession.

---

# 113. Evidence / provenance contract

```yaml
evidence_provenance:

  source_canon:
    references: []
    status: MISSING

  implementation_evidence:
    references: []
    status: MISSING

  validation_evidence:
    references: []
    status: MISSING

  provenance:
    roots: []
    status: INCOMPLETE
```

No implementation claims should be promoted while these remain missing.

---

# 114. Source/canon relation

Potential relevant AMOS concepts include:

```text
AMOS Full Brain OS
AMOS_CORE v4.4 reasoning lineage
RSCF
GMEF
H/M/L
Fractal Knowledge Network
competing hypotheses
provenance topology
regime/freshness
MVCC/CAS
proof-based coordination avoidance
```

These concepts can shape the placeholder.

They do not prove this exact routing subsystem has been implemented.

---

# 115. Control-plane boundary

Routing is below effect authority.

```text
Routing
    ↓
Binding
    ↓
Validation
    ↓
Control Plane
    ↓
Authority
    ↓
Worker
```

This separation should remain invariant across Agent, Skill, Engine, Kernel, Workflow, and Event-Bus paths.

---

# 116. Routing and canon

A routing rule may be canonical only after governance.

```text
routing proposal
→ validation
→ promotion
→ canon/policy admission
```

README presence alone does not establish canon.

---

# 117. Routing and policy

Policy may constrain:

```text
allowed candidate classes
fallback permission
effect routing
mode routing
security routing
data routing
worker routing
```

Policy epoch should become a load-bearing route dependency where applicable.

---

# 118. Routing and finality

Routing should generally occur well before finality.

A final route receipt does not mean the target effect or state is final.

```text
route finalized
!= external effect finalized
```

---

# 119. RSCF routing capsule

```yaml
rscf:

  claim_id:
    RSCF-CM-ROUTING-README-001

  claim:
    "This file defines the authoritative AMOS routing architecture for 10_ROUTING."

  claim_class:
    UNKNOWN/GAP

  scope:
    system: AMOS_OS
    subsystem: COGNITIVE_MATRIX
    package: 10_ROUTING
    artifact: README.md

  evidence: []

  provenance: []

  load_bearing_premises:
    - authoritative routing source recovered
    - routing registries recovered
    - binding rules recovered
    - mode registry recovered
    - active policy model recovered
    - runtime router recovered
    - routing tests executed

  dependencies:
    - AUTHORITATIVE_STATE
    - 10_ROUTING/BINDING_RULES.md
    - MODE_REGISTRY
    - CELL_REGISTRY
    - CELL_CONTRACTS
    - 11_VALIDATION
    - 12_GENERATORS
    - POLICY_MANIFEST
    - PROVENANCE_MANIFEST
    - AGENT_REGISTRY
    - SKILL_REGISTRY
    - ENGINE_REGISTRY
    - KERNEL_REGISTRY
    - WORKER_REGISTRY

  competing:
    - authoritative routing specification may exist elsewhere

  falsifiers:
    - recovered source defines materially different routing semantics
    - runtime contradicts this placeholder
    - higher-order governance contract supersedes these rules

  regime:
    architecture: UNKNOWN
    runtime: UNKNOWN

  freshness: null

  confidence_ceiling: 0

  status:
    PLACEHOLDER
```

---

# 120. GMEF routing capsule

```yaml
gmef:

  artifact:
    AMOS-CM-10-ROUTING-README

  governance_status:
    PLACEHOLDER

  governed_operations:
    - REQUEST_ROUTING
    - DOMAIN_ROUTING
    - MODE_ROUTING
    - CAPABILITY_ROUTING
    - AGENT_ROUTING
    - SKILL_ROUTING
    - ENGINE_ROUTING
    - KERNEL_ROUTING
    - WORKER_ROUTING
    - VALIDATOR_ROUTING
    - GENERATOR_ROUTING
    - WORKFLOW_ROUTING
    - FALLBACK_ROUTING

  authority_state:
    UNBOUND

  policy_epoch:
    UNKNOWN

  required_invariants:
    - I-ROUTE-001
    - I-ROUTE-002
    - I-ROUTE-003
    - I-ROUTE-004
    - I-ROUTE-006
    - I-ROUTE-007
    - I-ROUTE-008
    - I-ROUTE-009
    - I-ROUTE-010
    - I-ROUTE-011
    - I-ROUTE-012
    - I-ROUTE-014
    - I-ROUTE-015
    - I-ROUTE-018

  mutation_permission:
    UNKNOWN

  finality:
    UNFINALIZED
```

---

# 121. Routing proof capsule

```yaml
proof_capsule:

  conclusion:
    "Route R is a valid candidate path for request Q."

  class:
    DERIVED

  required:
    - request identity
    - selected path identities
    - component versions
    - registry versions
    - capability match
    - scope match
    - regime match
    - policy compatibility
    - dependency closure
    - freshness

  does_not_prove:
    - output truth
    - authority
    - effect permission
    - canon status
    - execution success
    - finality

  invalidation_conditions:
    - request changed
    - registry changed
    - candidate changed
    - mode changed
    - policy changed
    - scope changed
    - regime changed
    - dependency invalidated
```

---

# 122. Related artifacts

```yaml
related:

  parent:
    - 25_COGNITIVE_MATRIX
    - 10_ROUTING

  routing:
    - 10_ROUTING/BINDING_RULES.md
    - ROUTER_REGISTRY
    - CAPABILITY_REGISTRY
    - ROUTING_PROTOCOLS
    - ROUTE_RECEIPTS

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

  component_registries:
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
    - SUPERSESSION_REGISTRY
    - ROLLBACK_MANIFEST

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

# 123. Related relation types

```text
PARENT_OF
CHILD_OF
ROUTES_TO
BINDS_TO
REQUIRES
USES
VALIDATED_BY
GOVERNED_BY
AUTHORIZED_BY
FALLBACK_TO
RECOVERS_WITH
PROVENANCE_ROOT
COMPATIBLE_WITH
INCOMPATIBLE_WITH
COMPETING_WITH
SUPERSEDES
SUPERSEDED_BY
```

---

# 124. Related tag ontology

```text
Identity:
#AMOS
#AMOS_OS
#AMOS_CORE
#CognitiveMatrix
#Routing
#Router

Architecture:
#ControlPlane
#Kernel
#Engine
#Skill
#Agent
#Worker
#Workflow
#EventBus
#Registry

Routing:
#DomainRouting
#CapabilityRouting
#ModeRouting
#DependencyRouting
#FallbackRouting
#RecoveryRouting
#EventRouting
#WorkerRouting

Knowledge:
#RSCF
#GMEF
#HML
#FractalKnowledgeNetwork
#ProofCapsule

Epistemic:
#SourceClaim
#Observation
#Derived
#Model
#Conditional
#Competing
#UnknownGap
#ConfidenceCeiling

Provenance:
#Provenance
#SourceAncestry
#Independence
#SybilHardening
#CausalLineage

Governance:
#Authority
#Policy
#Invariant
#Validation
#Promotion
#ConflictResolution

State:
#MVCC
#CAS
#ReadSet
#RegistryVersion
#Epoch
#Idempotency

Integrity:
#AntiFabrication
#AntiRegression
#ScopeFirewall
#RegimeFirewall
#Freshness
#SelectiveInvalidation

Recovery:
#Fallback
#Repair
#Reroute
#Rebind
#Replay
```

---

# 125. Required completion field status

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

  actual_router_implementation:
    required: true
    status: UNKNOWN

  registry_binding:
    required: true
    status: UNBOUND

  mode_binding:
    required: true
    status: UNBOUND

  policy_binding:
    required: true
    status: UNBOUND

  authority_boundary:
    required: true
    status: MODEL_DRAFT

  runtime_validation:
    required: true
    status: NOT_RUN
```

---

# 126. Gap registry

```yaml
gaps:

  CRITICAL:
    - authoritative routing source/canon
    - actual Router implementation
    - actual Capability Registry
    - actual component registries
    - actual Mode Registry binding
    - active policy epoch
    - routing protocol
    - executed constitutional tests

  DECISION_RELEVANT:
    - exact specificity precedence
    - tie-break rules
    - fallback semantics
    - route-cache semantics
    - route receipt semantics
    - security routing rules
    - resource budgets

  EXPLANATORY:
    - routing visualizations
    - route latency metrics
    - additional examples

  COSMETIC:
    - naming harmonization
    - README formatting
```

---

# 127. Hard boundaries

```text
PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

REGISTERED != ACTIVE

ACTIVE != AUTHORIZED

ROUTED != BOUND

BOUND != VALIDATED

VALIDATED != AUTHORIZED

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

EVENT != AUTHORITY

MODE_EXISTS != MODE_ACTIVE

FIRST_MATCH != BEST_MATCH

DEFAULT != UNIVERSAL_HANDLER

MULTIPLE_MATCHES != CONSENSUS

MULTIPLE_SOURCES != INDEPENDENT_SOURCES

SCHEMA_MATCH != SEMANTIC_MATCH

FALLBACK != SEMANTIC_EQUIVALENCE

CACHE_HIT != CURRENT_VALIDITY

UNKNOWN/GAP != PASS

AMBIGUOUS != RESOLVED

COMPETING != CONVERGED

STALE != CURRENT

ROUTE_VALID != OUTPUT_TRUE
```

---

# 128. Current decision

```yaml
decision:

  accept_as_authoritative_routing_contract:
    false

  current_role:
    STRUCTURAL_PLACEHOLDER

  current_epistemic_class:
    UNKNOWN/GAP

  implementation_state:
    UNVERIFIED

  authority_state:
    NONE

  safe_use:
    - reserve routing architecture surface
    - define provisional routing semantics
    - guide registry design
    - guide Agent/Skill/Engine/Kernel/Worker separation
    - expose routing gaps
    - prevent default-capture behavior
    - define test requirements
    - support matrix structural audits

  unsafe_use:
    - claim router is implemented
    - claim all component registries exist
    - treat addressability as validation
    - silently activate modes
    - silently fallback
    - create authority from route selection
    - claim route success proves output correctness
```

---

# 129. Final RSCF summary

**Claim**

`10_ROUTING / README.md` is the authoritative operative routing architecture for AMOS.

**Current class**

`UNKNOWN/GAP`

**What this file establishes**

A detailed AMOS-aligned structural routing model covering:

```text
request typing
H/M/L
domain selection
adaptive complexity
mode selection
capability discovery
Agent/Skill/Engine/Kernel/Worker routing
validator/generator routing
workflow/event routing
dependency closure
provenance-aware evidence routing
fallback/recovery
MVCC/CAS-style route freshness
route caching
ambiguity
competing routes
control-plane boundaries
```

**What remains unestablished**

This artifact does not prove:

```text
a Router implementation exists
the registries are complete
the precedence rules are canonical
binding rules are implemented
mode routing is validated
routing tests pass
runtime routing is active
worker routes are authorized
```

**Critical missing evidence**

```text
authoritative source/canon
router implementation
registry state
mode registry
routing policy
validation receipts
runtime integration
protocol definitions
```

**Competing possibility**

A more authoritative AMOS/Trang routing specification may exist elsewhere in the corpus.

**Falsifier**

Recovery and validation of that specification.

**Confidence ceiling**

```text
0
for implementation or authoritative-runtime claims.

Moderate
for usefulness as a structural
AMOS-aligned routing placeholder.
```

**Final state**

```text
PLACEHOLDER
UNVALIDATED
UNKNOWN/GAP
NON_AUTHORITATIVE
UNBOUND
```

```
```

---

00_ROOT_MOC|AMOS MOC

---
**Related:** [[00_HOME]] · [[COGNITIVE_MATRIX_MOC]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: routing_cognitive_matrix_readme
node_type: note
path: 25_COGNITIVE_MATRIX/10_ROUTING/ROUTING_COGNITIVE_MATRIX_README.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[10_ROUTING_MOC]]
