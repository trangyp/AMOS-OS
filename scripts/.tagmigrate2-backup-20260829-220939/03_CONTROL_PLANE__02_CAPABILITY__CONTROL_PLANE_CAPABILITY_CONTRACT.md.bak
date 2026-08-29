---
title: CONTROL PLANE CAPABILITY CONTRACT
type: control-plane
source: 03_CONTROL_PLANE/02_CAPABILITY
tags:
- control-plane
- capability
- contract
- canon/control-plane
- 00-root-moc
- amos-moc
- 00-home
- amos-rscf-nodes
- 02-capability-moc
rscf:
  state: DERIVED
  claim_class: CONDITIONAL
  provenance: AMOS_corpus
  scope: AMOS_general
---

# CONTROL PLANE CAPABILITY CONTRACT

Yes. The placeholder should be replaced by a substantive contract. Below is a **full paste-ready `CAPABILITY_CONTRACT.md`**. It is intentionally classified as an **AMOS MODEL / proposed governed contract**, not falsely presented as already implemented or canonically validated.

---
title: AMOS Capability Contract
artifact: "CAPABILITY_CONTRACT.md"
origin_architect: "Trang Phan"
steward: "Trang Phan"
system: "AMOS OS"
contract_class: "GOVERNED_CAPABILITY_CONTRACT"
status: "PROPOSED / STRUCTURALLY COMPLETE / IMPLEMENTATION-UNVALIDATED"
epistemic_class: "MODEL"
version: "1.0.0"
updated: "2026-08-26"
authority: "NONE_BY_DEFAULT"
---

# AMOS Capability Contract

## 0. Status and Interpretation

This document defines the governed contract by which a capability may be represented, discovered, selected, invoked, supervised, validated, and—where separately authorized—used to propose effects inside AMOS OS.

It replaces the structurally inadequate placeholder previously occupying `CAPABILITY_CONTRACT.md`.

This document is a **contract specification**, not evidence that every described mechanism is currently implemented.

The following distinctions are mandatory:

```text
CAPABILITY != AUTHORITY
CAPABILITY != PERMISSION
CAPABILITY != AGENT
CAPABILITY != SKILL
CAPABILITY != TOOL
CAPABILITY != WORKFLOW
CAPABILITY != CONTROL_PLANE
CAPABILITY != IMPLEMENTATION
CAPABILITY != VALIDATION

DECLARED != AVAILABLE
AVAILABLE != COMPATIBLE
COMPATIBLE != SELECTED
SELECTED != AUTHORIZED
AUTHORIZED != EXECUTED
EXECUTED != VALIDATED
VALIDATED != COMMITTED

PROPOSAL != COMMIT
ADDRESSABLE != VALIDATED
PLACEHOLDER != IMPLEMENTED
UNKNOWN/GAP != PASS
```

No capability declaration grants authority merely by existing.

---

# 1. Purpose

The AMOS Capability Contract exists to answer, in a deterministic and auditable form:

1. What can this component potentially do?
2. What exact inputs does it accept?
3. What outputs may it produce?
4. Under what scope and regime is it applicable?
5. What dependencies must exist before invocation?
6. Which invariants constrain its operation?
7. Which agent, Skill, tool, workflow, or runtime provides it?
8. Which control plane governs it?
9. What evidence supports its claimed capability?
10. What authority, if any, permits its use?
11. What side effects can it create?
12. What validation must occur before its result may be trusted?
13. What additional validation must occur before an effect may be committed?
14. How is failure detected?
15. How is failure contained, repaired, retried, rolled back, or escalated?
16. What provenance must survive execution?
17. Under what conditions does the capability become stale or invalid?
18. What would falsify the capability claim?

The contract therefore acts as the boundary between:

```text
potential functionality
        ↓
declared capability
        ↓
resolved implementation
        ↓
validated applicability
        ↓
authorized invocation
        ↓
execution
        ↓
result validation
        ↓
effect proposal
        ↓
commit authorization
        ↓
durable effect
```

No stage may silently imply a later stage.

---

# 2. Non-Purpose

This contract does **not**:

* grant authority;
* create permissions;
* prove implementation;
* prove correctness;
* establish empirical validity;
* establish canonical AMOS status by itself;
* allow an agent to self-authorize;
* allow a Skill to self-promote;
* allow capability discovery to bypass policy;
* convert model confidence into permission;
* convert successful execution into scientific validation;
* convert a proposal into a durable commit;
* permit provenance-free execution;
* permit unknown dependencies to be interpreted as satisfied;
* permit unsupported cross-domain generalization.

---

# 3. Core Definition

An AMOS capability is a typed, scoped, provenance-bound declaration that a provider can attempt a defined transformation under explicit preconditions, constraints, evidence, governance, and validation requirements.

Conceptually:

```text
Capability :=
    Identity
  × Provider
  × InputContract
  × OutputContract
  × Preconditions
  × Scope
  × Regime
  × Dependencies
  × Constraints
  × AuthorityRequirements
  × EffectClass
  × ValidationContract
  × ProvenanceContract
  × FailureContract
  × RecoveryContract
  × Freshness
  × Version
```

A capability is therefore not simply:

```text
"something the system can do"
```

It is:

```text
a governed claim that a particular provider can attempt
a particular transformation over particular typed inputs,
within a particular applicability envelope,
subject to particular constraints and validation.
```

---

# 4. Capability Identity

Every capability MUST possess a stable identity.

Minimum identity:

```yaml
capability_id: string
name: string
version: string
provider_id: string
provider_type: enum
status: enum
epistemic_class: enum
```

Recommended extended identity:

```yaml
identity:
  capability_id: "CAP_*"
  canonical_name: string
  aliases: []
  version: string
  schema_version: string
  origin_architect: "Trang Phan"
  steward: string
  provider_id: string
  provider_type: AGENT | SKILL | TOOL | WORKFLOW | SERVICE | RUNTIME | MODEL
  created_at: timestamp
  updated_at: timestamp
  supersedes: []
  superseded_by: null
```

Aliases MUST NOT create separate capability identities unless their behavior or contract differs materially.

---

# 5. Capability Classes

Capabilities SHOULD be typed by functional class.

```text
PERCEPTION
RETRIEVAL
TRANSFORMATION
REASONING
ANALYSIS
PREDICTION
SIMULATION
PLANNING
GENERATION
VALIDATION
VERIFICATION
MEMORY_READ
MEMORY_WRITE
COMMUNICATION
ORCHESTRATION
CONTROL
REPAIR
RECOVERY
GOVERNANCE
EXECUTION
COMMIT
OBSERVABILITY
AUDIT
```

A capability may occupy multiple classes, but each class MUST remain explicitly declared.

Example:

```yaml
capability_classes:
  - RETRIEVAL
  - ANALYSIS
```

must not silently imply:

```yaml
capability_classes:
  - EXECUTION
  - COMMIT
```

---

# 6. Provider Types

A capability may be supplied by:

```text
AGENT
SKILL
TOOL
WORKFLOW
SERVICE
MODEL
RUNTIME
CONTROL_PLANE
DETERMINISTIC_FUNCTION
EXTERNAL_SYSTEM
```

Provider identity MUST remain separate from capability identity.

One provider may expose multiple capabilities.

One capability may have multiple providers.

Provider equivalence MUST NOT be assumed.

```text
same capability name
    !=
same implementation

same implementation
    !=
same validation state

same output type
    !=
same semantics

same behavior
    !=
same authority
```

---

# 7. Typed Input Contract

Every capability MUST declare accepted inputs.

Canonical form:

```yaml
inputs:
  - name: string
    type: string
    required: true
    nullable: false
    units: null
    domain: null
    schema: null
    provenance_required: true
    freshness_requirement: null
    sensitivity_class: null
```

Inputs SHOULD carry, where relevant:

```text
type
shape
units
domain
scale
time
observer
regime
source
provenance
freshness
confidence
sensitivity
authority context
```

An input that cannot be typed sufficiently for safe invocation MUST be:

```text
REJECTED
or
QUARANTINED
or
marked UNKNOWN/GAP
```

It MUST NOT be silently coerced.

---

# 8. Typed Output Contract

Every capability MUST declare possible outputs.

```yaml
outputs:
  - name: string
    type: string
    nullable: false
    epistemic_class: DERIVED
    schema: null
    provenance_required: true
    confidence_required: true
```

Outputs SHOULD distinguish:

```text
OBSERVATION
SOURCE_CLAIM
DERIVED
MODEL
PREDICTION
PROPOSAL
DECISION
EFFECT
UNKNOWN/GAP
```

A generated output MUST NOT automatically be classified as `VERIFIED`.

---

# 9. State Variables

A capability MAY be stateful or stateless.

Minimum runtime state model:

```yaml
state:
  capability_state:
    - UNRESOLVED
    - RESOLVED
    - AVAILABLE
    - UNAVAILABLE
    - ELIGIBLE
    - INELIGIBLE
    - AUTHORIZED
    - DENIED
    - EXECUTING
    - SUCCEEDED
    - FAILED
    - QUARANTINED
    - STALE
    - REVOKED

  validation_state:
    - UNVALIDATED
    - PARTIALLY_VALIDATED
    - VALIDATED
    - INVALIDATED

  effect_state:
    - NONE
    - PROPOSED
    - PREPARED
    - COMMITTED
    - ROLLED_BACK
```

Additional state MAY include:

```yaml
runtime:
  invocation_id: string
  parent_invocation_id: null
  session_id: string
  causal_epoch: null
  validation_epoch: null
  retry_count: 0
  started_at: null
  completed_at: null
  last_error: null
```

---

# 10. Capability Lifecycle

The canonical lifecycle is:

```text
DECLARE
  ↓
REGISTER
  ↓
RESOLVE
  ↓
CHECK AVAILABILITY
  ↓
CHECK COMPATIBILITY
  ↓
CHECK PRECONDITIONS
  ↓
CHECK DEPENDENCIES
  ↓
CHECK FRESHNESS
  ↓
CHECK POLICY
  ↓
CHECK AUTHORITY
  ↓
INVOKE
  ↓
OBSERVE
  ↓
VALIDATE RESULT
  ↓
PROPOSE EFFECT
  ↓
REVALIDATE COMMIT CONDITIONS
  ↓
COMMIT / REJECT / QUARANTINE
  ↓
RECORD PROVENANCE
```

A failure at any gate prevents silent advancement.

---

# 11. Operators

The capability layer requires at least the following conceptual operators.

## 11.1 `DECLARE`

```text
DECLARE(provider, specification) → CapabilityDeclaration
```

Creates a capability claim.

Does not prove the claim.

---

## 11.2 `REGISTER`

```text
REGISTER(declaration, registry) → RegistrationResult
```

Makes the capability addressable.

```text
REGISTERED != VALIDATED
```

---

## 11.3 `RESOLVE`

```text
RESOLVE(requirement, registry, context) → CandidateCapabilities
```

Finds providers whose declared contracts may satisfy a requirement.

Resolution is candidate discovery, not authorization.

---

## 11.4 `MATCH`

```text
MATCH(requirement, capability) → CompatibilityAssessment
```

Checks semantic and typed compatibility.

---

## 11.5 `VALIDATE_INPUT`

```text
VALIDATE_INPUT(input, input_contract) → PASS | FAIL | GAP
```

`GAP` MUST NOT be collapsed into `PASS`.

---

## 11.6 `CHECK_PRECONDITIONS`

```text
CHECK_PRECONDITIONS(capability, state) → EligibilityResult
```

---

## 11.7 `CHECK_DEPENDENCIES`

```text
CHECK_DEPENDENCIES(capability, dependency_graph) → DependencyResult
```

All load-bearing dependencies must resolve sufficiently for the requested operation.

---

## 11.8 `CHECK_AUTHORITY`

```text
CHECK_AUTHORITY(
    principal,
    capability,
    action,
    resource,
    context
) → ALLOW | DENY | ESCALATE
```

Capability possession does not participate as a substitute for authority evidence.

---

## 11.9 `INVOKE`

```text
INVOKE(capability, validated_input, execution_context)
    → ExecutionResult
```

Invocation requires the relevant gates to have passed.

---

## 11.10 `VALIDATE_OUTPUT`

```text
VALIDATE_OUTPUT(result, output_contract)
    → ValidatedResult | InvalidResult | Gap
```

---

## 11.11 `PROPOSE_EFFECT`

```text
PROPOSE_EFFECT(validated_result, intended_effect)
    → EffectProposal
```

No durable effect follows automatically.

---

## 11.12 `COMMIT`

```text
COMMIT(effect_proposal, fresh_authority, fresh_constraints)
    → CommitResult
```

Commit MUST remain separately governed.

---

## 11.13 `REVOKE`

```text
REVOKE(capability_id, reason)
```

Prevents future eligible use subject to system policy.

---

## 11.14 `QUARANTINE`

```text
QUARANTINE(capability_id | invocation_id, evidence)
```

Isolates suspect capability state without requiring deletion.

---

## 11.15 `INVALIDATE`

```text
INVALIDATE(claim_or_validation, failed_dependency)
```

Invalidation SHOULD propagate only to dependent conclusions.

---

# 12. Core Invariants

## INV-CAP-001 — Capability/Authority Separation

```text
Capability(c, a) ↛ Authorized(a)
```

A capability can exist without permission to invoke it.

---

## INV-CAP-002 — Proposal/Commit Separation

```text
PROPOSE(x) != COMMIT(x)
```

No proposal may produce a durable effect without the applicable commit gate.

---

## INV-CAP-003 — Unknown Is Not Pass

```text
UNKNOWN/GAP != PASS
```

Unresolved requirements cannot be silently accepted.

---

## INV-CAP-004 — Addressability Is Not Validation

```text
registered(c) != validated(c)
```

---

## INV-CAP-005 — Provider Identity Preservation

Capability results MUST retain provider identity and version.

---

## INV-CAP-006 — Provenance Preservation

A capability invocation MUST preserve enough lineage to answer:

```text
who/what produced this?
from which inputs?
using which capability?
which provider/version?
under which policy?
under which authority?
under which validation state?
at what time?
```

---

## INV-CAP-007 — Scope Preservation

A capability validated for scope `S1` cannot silently be treated as validated for `S2`.

---

## INV-CAP-008 — Regime Preservation

Capability validity MUST be reevaluated when material regime assumptions change.

---

## INV-CAP-009 — Freshness

Stale capability state MUST NOT be represented as current.

---

## INV-CAP-010 — Dependency Closure

No capability result may be promoted beyond the confidence permitted by unresolved load-bearing dependencies.

---

## INV-CAP-011 — Confidence Ceiling

For load-bearing premises:

```text
C(result) ≤ min(C(p1), C(p2), ..., C(pn))
```

unless an independent validation path justifies a higher bounded confidence.

---

## INV-CAP-012 — Side-Effect Declaration

A capability MUST NOT create undeclared external or durable side effects.

---

## INV-CAP-013 — Least Necessary Capability

When multiple capabilities satisfy a requirement, selection SHOULD prefer the smallest capability surface sufficient for the task, subject to quality and safety requirements.

---

## INV-CAP-014 — Revocation Dominance

A revoked capability MUST fail closed for new governed invocation unless an explicitly authorized restoration process supersedes the revocation.

---

## INV-CAP-015 — Validation Non-Transitivity

```text
validated(provider_A)
    !=
validated(provider_B)
```

even if both claim the same capability.

---

# 13. Preconditions

A capability may declare preconditions such as:

```yaml
preconditions:
  required_context: []
  required_state: []
  required_resources: []
  required_permissions: []
  required_dependencies: []
  minimum_evidence_class: null
  minimum_confidence: null
  maximum_input_age: null
  allowed_regimes: []
  prohibited_regimes: []
```

Preconditions MUST be evaluated before execution where materially possible.

---

# 14. Dependencies

Capability dependencies MUST be explicit.

Dependency classes include:

```text
DATA
MODEL
SKILL
TOOL
AGENT
WORKFLOW
POLICY
AUTHORITY
CONTROL_PLANE
MEMORY
STATE
SERVICE
SCHEMA
ONTOLOGY
PROVENANCE
VALIDATOR
ENVIRONMENT
```

Canonical representation:

```yaml
dependencies:
  - dependency_id: string
    dependency_type: string
    required: true
    version_constraint: null
    freshness_constraint: null
    validation_required: true
    failure_behavior: FAIL_CLOSED
```

Circular dependencies MUST be detected rather than silently traversed forever.

---

# 15. H/M/L Applicability

Capabilities MAY exist at High, Medium, and Low reasoning scales.

## H — Governing / System Level

Examples:

```text
capability-family selection
cross-domain orchestration
policy applicability
authority boundaries
global dependency constraints
system-level risk
```

## M — Subsystem / Workflow Level

Examples:

```text
workflow selection
Skill orchestration
agent assignment
validation routing
memory/retrieval strategy
repair strategy
```

## L — Execution / Operation Level

Examples:

```text
individual tool call
single transformation
schema validation
retrieval query
specific computation
single write proposal
```

Cross-scale invocation MUST preserve dependency and authority relationships.

```text
H policy may constrain M selection.
M workflow may constrain L invocation.
L execution may provide evidence upward.
L capability may not silently override H authority.
```

---

# 16. Control-Plane Requirements

Capabilities operate beneath control-plane governance where applicable.

Required control-plane functions MAY include:

```text
capability registry
provider resolution
schema validation
policy evaluation
authority validation
dependency checking
freshness checking
provenance capture
transaction management
commit gating
observability
retry governance
quarantine
revocation
rollback
audit
```

The control plane SHOULD own governance semantics rather than delegating them to stochastic workers.

A worker may propose:

```text
"invoke capability X"
```

but the governing layer determines whether invocation is admissible.

---

# 17. Agent Contract

Agents consume capabilities; they do not inherently own the authority represented by those capabilities.

Agent-capability binding:

```yaml
agent_capability_binding:
  agent_id: string
  capability_id: string
  role: PROVIDER | CONSUMER | VALIDATOR | SUPERVISOR
  allowed_operations: []
  authority_reference: null
  constraints: []
```

An agent MUST NOT infer:

```text
I can call X
therefore
I am allowed to call X.
```

---

# 18. Skill Contract

Skills MAY package one or more capabilities.

```yaml
skill_binding:
  skill_id: string
  skill_version: string
  exposed_capabilities: []
  required_capabilities: []
  deterministic_components: []
  model_components: []
  side_effect_classes: []
  validators: []
```

Installing or discovering a Skill does not grant permission to execute all of its capabilities.

Skill capability boundaries MUST remain explicit.

---

# 19. Workflow Contract

A workflow composes capabilities into an ordered or graph-structured process.

```yaml
workflow:
  workflow_id: string
  nodes: []
  edges: []
  entry_conditions: []
  exit_conditions: []
  rollback_edges: []
  escalation_edges: []
```

Each node SHOULD specify:

```yaml
node:
  node_id: string
  capability_required: string
  provider: null
  input_contract: {}
  output_contract: {}
  authority_requirement: {}
  validation_requirement: {}
  failure_transition: null
```

Workflow success does not automatically prove each scientific or factual claim generated within the workflow.

---

# 20. Protocol Contract

Capability interactions SHOULD use typed protocols.

Minimum invocation envelope:

```yaml
capability_invocation:
  invocation_id: string
  capability_id: string
  capability_version: string
  provider_id: string

  requester:
    principal_id: string
    agent_id: null

  input:
    payload: {}
    schema_id: null
    provenance: []

  context:
    session_id: null
    scope: null
    regime: null
    timestamp: null

  governance:
    policy_refs: []
    authority_witnesses: []
    constraints: []

  expected_output:
    schema_id: null

  effect_class: NONE
```

Minimum result envelope:

```yaml
capability_result:
  invocation_id: string
  status: SUCCESS | FAILURE | PARTIAL | GAP

  output:
    payload: null
    schema_id: null

  epistemic:
    class: DERIVED
    confidence: null
    uncertainty: {}

  provenance:
    provider_id: string
    capability_version: string
    input_refs: []
    execution_refs: []

  validation:
    state: UNVALIDATED
    validators: []

  effects:
    proposed: []
    committed: []

  errors: []
```

---

# 21. Effect Classes

Every capability MUST declare its possible effect class.

```text
E0_READ_ONLY
E1_EPHEMERAL_STATE
E2_REVERSIBLE_LOCAL_WRITE
E3_PERSISTENT_WRITE
E4_EXTERNAL_COMMUNICATION
E5_FINANCIAL_OR_RESOURCE_EFFECT
E6_SECURITY_OR_AUTHORITY_EFFECT
E7_IRREVERSIBLE_OR_HIGH_CONSEQUENCE_EFFECT
```

Higher-consequence effects require stronger governance.

Conceptually:

```text
required_validation ∝ consequence × irreversibility × uncertainty
```

This is a governance relation, not an empirical physical law.

---

# 22. Authority Requirements

Authority MUST be represented independently.

Example:

```yaml
authority_requirements:
  invocation:
    required: true
    allowed_principals: []
    required_scopes: []

  effect:
    required: true
    allowed_effect_classes: []

  commit:
    required: true
    freshness_required: true
    revalidation_required: true
```

Authority MAY be:

```text
USER_GRANTED
SYSTEM_POLICY
ROLE_BOUND
DELEGATED
TEMPORARY
RESOURCE_SCOPED
TRANSACTION_SCOPED
DENIED
UNKNOWN
```

Unknown authority MUST fail closed for consequential actions.

---

# 23. Evidence and Provenance

Capability claims SHOULD carry evidence appropriate to the strength of the claim.

Evidence classes:

```text
SOURCE_CLAIM
DOCUMENTED_INTERFACE
STATIC_INSPECTION
UNIT_TEST
INTEGRATION_TEST
RUNTIME_OBSERVATION
BENCHMARK
FORMAL_CHECK
INDEPENDENT_VALIDATION
PRODUCTION_OBSERVATION
```

Canonical evidence record:

```yaml
evidence:
  evidence_id: string
  type: string
  source_id: string
  source_version: null
  timestamp: null
  environment: null
  supports: []
  contradicts: []
  ancestry: []
  independence_status: UNKNOWN
```

Multiple pieces of evidence derived from the same origin MUST NOT automatically be counted as independent confirmation.

---

# 24. Provenance Topology

For material capability claims, provenance SHOULD preserve ancestry.

```text
source
  ↓
declaration
  ↓
registration
  ↓
resolution
  ↓
invocation
  ↓
result
  ↓
validation
  ↓
proposal
  ↓
commit
```

Where branches merge, correlated ancestry MUST remain visible.

A capability result SHOULD be traceable to its load-bearing evidence.

---

# 25. Uncertainty Vector

Capability confidence SHOULD NOT be represented by one undifferentiated scalar when multiple uncertainty classes matter.

Recommended vector:

```yaml
uncertainty:
  evidence: null
  model: null
  scope: null
  temporal: null
  causal: null
  execution: null
  provenance_independence: null
```

Examples:

* implementation may be known while scope remains uncertain;
* output may be reproducible while causal interpretation remains uncertain;
* interface may be documented while execution availability remains unknown;
* provider may work while authority remains absent.

These conditions MUST remain distinguishable.

---

# 26. Confidence Ceiling

A capability claim's confidence cannot exceed its weakest load-bearing unresolved premise.

Conceptually:

```text
C_capability ≤ min(
    C_provider_identity,
    C_interface,
    C_dependencies,
    C_environment,
    C_validation,
    C_scope,
    C_freshness
)
```

Authority is not merely another confidence term.

Even:

```text
C_capability = 1.0
```

does not imply:

```text
authorized = true
```

---

# 27. Capability Validation Levels

Recommended validation ladder:

```text
V0 DECLARED
V1 STRUCTURALLY_VALID
V2 STATICALLY_CHECKED
V3 LOCALLY_TESTED
V4 INTEGRATION_TESTED
V5 ENVIRONMENT_VALIDATED
V6 INDEPENDENTLY_VALIDATED
V7 GOVERNED_PRODUCTION_VALIDATED
```

These levels are proposed AMOS contract states unless separately adopted into canon.

A provider MUST NOT claim a higher validation level without supporting evidence.

---

# 28. Capability Availability

Availability is runtime-specific.

```yaml
availability:
  state: AVAILABLE | UNAVAILABLE | DEGRADED | UNKNOWN
  checked_at: timestamp
  environment_id: string
  expires_at: null
```

Historical availability does not guarantee present availability.

---

# 29. Freshness

Capabilities and their dependencies may become stale.

Freshness can apply to:

```text
provider version
schema
policy
authority
dependency
model
data
environment
validation
security posture
external API
```

A freshness requirement SHOULD declare:

```yaml
freshness:
  checked_at: timestamp
  ttl: null
  invalidation_events: []
  revalidation_required_on_change: true
```

---

# 30. Regime Validity

Capabilities MAY only be valid under specific operating regimes.

Examples:

```text
offline
online
simulation
production
development
high-liquidity
low-latency
regulated
unregulated
trusted-input
adversarial-input
```

A regime transition MUST trigger revalidation when the contract depends on the changed regime.

---

# 31. Capability Selection

Given candidates:

```text
C = {c1, c2, ..., cn}
```

selection SHOULD consider:

```text
contract compatibility
validation strength
authority compatibility
dependency satisfaction
freshness
scope fit
regime fit
cost
latency
risk
reversibility
provenance quality
```

A conceptual selection score MAY be used:

```text
S(c) =
    Fit(c)
  × Validity(c)
  × Freshness(c)
  × GovernanceCompatibility(c)
  - Risk(c)
  - Cost(c)
```

This equation is an AMOS MODEL heuristic unless a specific implementation defines and validates its terms.

No scalar score may override a hard invariant.

---

# 32. Least-Privilege Capability Selection

When several providers can satisfy a requirement, prefer the least powerful sufficient provider where quality is not materially degraded.

Example:

```text
read-only search
```

should not require:

```text
filesystem write + network write + commit authority
```

if a narrower read capability suffices.

---

# 33. Capability Composition

Capabilities may compose:

```text
c1 → c2 → c3
```

Composition is valid only if output/input contracts are compatible.

For:

```text
output(c1) → input(c2)
```

the following may require compatibility checks:

```text
type
schema
units
scope
regime
time
provenance
confidence
authority context
sensitivity
```

Syntactic compatibility is insufficient when semantics differ.

---

# 34. Cross-Skill Composition

Cross-Skill composition MUST preserve:

```text
semantic meaning
provenance
authority
constraints
scope
regime
freshness
effect class
validation state
```

No Skill may erase restrictions attached upstream merely because it transforms the data.

---

# 35. Atomic Multi-Capability Operations

Where multiple capabilities jointly produce one governed effect:

```text
c1 + c2 + ... + cn → effect
```

the system SHOULD treat load-bearing operations as one semantic transaction where partial execution would violate invariants.

Possible states:

```text
PREPARE
VALIDATE
AUTHORIZE
EXECUTE
REVALIDATE
COMMIT
ABORT
ROLLBACK
```

Partial success MUST remain visible.

---

# 36. Commit-Time Revalidation

For mutable or consequential systems, authorization and relevant constraints SHOULD be checked again near commit.

Reason:

```text
valid_at_planning_time
    != necessarily
valid_at_commit_time
```

Commit validation may include:

```text
authority freshness
resource state
policy freshness
dependency state
target identity
effect payload
concurrency state
revocation state
```

---

# 37. Memory Interaction

Capabilities that read or write persistent memory require explicit declaration.

```yaml
memory_effects:
  reads:
    allowed: false
    scopes: []

  writes:
    allowed: false
    scopes: []

  deletes:
    allowed: false

  retention_class: null
```

Memory retrieval MUST NOT silently become action authority.

Memory writes SHOULD preserve:

```text
semantic origin
source provenance
timestamp
scope
confidence
validation state
supersession relation
```

---

# 38. Information Boundary Requirements

Capability invocation must respect information boundaries.

Before information crosses:

```text
agent
Skill
tool
memory
recipient
external service
organizational boundary
```

the system SHOULD verify:

```text
recipient
purpose
scope
sensitivity
authority
provenance
transformation history
cumulative exposure
```

A technically callable recipient is not automatically an authorized recipient.

---

# 39. Observability

Every material invocation SHOULD emit an auditable execution record.

Minimum:

```yaml
observation:
  invocation_id: string
  capability_id: string
  provider_id: string
  started_at: timestamp
  completed_at: timestamp
  status: string
  validation_state: string
  effect_state: string
  error_codes: []
```

Higher-consequence capabilities SHOULD additionally preserve:

```text
input hashes/references
output hashes/references
authority witness
policy version
dependency versions
environment identity
validation results
rollback state
```

---

# 40. Failure Modes

## FM-CAP-001 — Phantom Capability

Registry claims a capability whose implementation does not exist.

Response:

```text
INVALIDATE
QUARANTINE REGISTRY ENTRY
FAIL CLOSED
```

---

## FM-CAP-002 — Capability Inflation

A narrow capability is represented as broader than validated.

Example:

```text
can summarize text
→ incorrectly promoted to
can verify factual truth
```

Response:

```text
restore original scope
invalidate derived claims
```

---

## FM-CAP-003 — Authority Confusion

Agent interprets capability availability as permission.

Response:

```text
DENY EFFECT
AUDIT AUTHORITY PATH
```

---

## FM-CAP-004 — Provider Drift

Provider behavior changes while capability version remains unchanged.

Response:

```text
STALE
REVALIDATE
possibly QUARANTINE
```

---

## FM-CAP-005 — Schema Drift

Inputs or outputs no longer match contract.

Response:

```text
FAIL VALIDATION
DO NOT SILENTLY COERCE
```

---

## FM-CAP-006 — Dependency Drift

A dependency changes semantics, version, policy, or availability.

Response:

```text
selectively invalidate dependent capability validation
```

---

## FM-CAP-007 — Scope Leakage

Capability is applied outside validated scope.

Response:

```text
CONDITIONAL / GAP
or reject invocation
```

---

## FM-CAP-008 — Regime Leakage

Capability validated under one regime is reused under another without revalidation.

---

## FM-CAP-009 — Provenance Loss

Output cannot be traced to provider/input/evidence.

Response:

```text
QUARANTINE OUTPUT
```

for provenance-sensitive operations.

---

## FM-CAP-010 — Correlated Validation

Multiple apparent validators share the same underlying source or implementation.

Response:

```text
downgrade independence
recalculate confidence ceiling
```

---

## FM-CAP-011 — Stale Authority

Authority was valid when planned but revoked before commit.

Response:

```text
ABORT COMMIT
```

---

## FM-CAP-012 — Partial Transaction

Some capabilities execute while the semantic transaction fails.

Response:

```text
ROLLBACK where possible
otherwise enter recovery
record partial effect
```

---

## FM-CAP-013 — Side-Effect Escape

Capability produces an undeclared effect.

Response:

```text
contain
revoke/quarantine
audit
repair affected state
```

---

## FM-CAP-014 — Validation Bypass

Output is consumed downstream before required validation.

Response:

```text
invalidate dependent results
restore last valid state
```

---

## FM-CAP-015 — Recursive Capability Loop

Capabilities repeatedly invoke each other without progress.

Response:

```text
detect cycle
stop
surface dependency loop
```

---

## FM-CAP-016 — Capability Shadowing

An alias or newer provider silently replaces a capability with different semantics.

Response:

```text
require explicit version/provider resolution
```

---

## FM-CAP-017 — Confidence Laundering

Low-confidence output passes through multiple components and emerges labeled high-confidence without independent evidence.

Response:

```text
restore dependency-bound confidence ceiling
```

---

## FM-CAP-018 — Tool Result Equals Truth

Successful API/tool execution is mistaken for correctness of the underlying claim.

Response:

```text
separate EXECUTION_SUCCESS from CLAIM_VALIDATION
```

---

# 41. Repair and Recovery

Capability recovery SHOULD use the smallest affected dependency closure.

Canonical recovery sequence:

```text
1. DETECT
2. CONTAIN
3. IDENTIFY FAILED PREMISE
4. INVALIDATE DEPENDENTS
5. PRESERVE UNAFFECTED STATE
6. RESTORE LAST VALID STATE
7. RE-RESOLVE PROVIDER/DEPENDENCY
8. REVALIDATE
9. RETRY IF JUSTIFIED
10. ESCALATE IF UNRESOLVED
```

Do not globally recompute if selective invalidation is sufficient.

---

# 42. Retry Policy

Retry is allowed only when the reason for failure can plausibly change.

Bad retry:

```text
same provider
same input
same state
same dependency
same failure
→ retry indefinitely
```

Valid retry may follow:

```text
transient network recovery
dependency restoration
fresh credentials
corrected schema
changed provider
repaired state
```

Retry count SHOULD be bounded.

---

# 43. Rollback

Capabilities with mutable effects SHOULD declare rollback properties.

```yaml
rollback:
  supported: true | false
  strategy: null
  maximum_window: null
  compensating_action: null
  irreversible_components: []
```

`rollback_supported: true` MUST itself be validated.

---

# 44. Escalation

Escalation SHOULD occur when:

```text
authority is ambiguous
critical dependency is unresolved
high-consequence effect is irreversible
validation paths conflict
provider behavior deviates materially
provenance is insufficient
repair repeatedly fails
policy conflict exists
regime applicability is unknown
```

Escalation target may include:

```text
higher control plane
human steward
specialist validator
security review
governance review
```

---

# 45. Tests and Validators

Minimum contract tests SHOULD include:

### T-CAP-001 — Identity uniqueness

Two materially different capability contracts must not share the same canonical identity/version.

### T-CAP-002 — Input rejection

Malformed required input must fail.

### T-CAP-003 — Unknown handling

Unknown mandatory precondition must not return PASS.

### T-CAP-004 — Authority separation

Callable capability without authority must not produce governed effect.

### T-CAP-005 — Proposal/commit separation

Effect proposal must not mutate durable state before commit.

### T-CAP-006 — Provenance retention

Output must retain required provider/input lineage.

### T-CAP-007 — Revocation

Revoked capability must fail new governed invocations.

### T-CAP-008 — Scope mismatch

Out-of-scope invocation must fail or downgrade.

### T-CAP-009 — Regime mismatch

Invalid regime must trigger revalidation/failure.

### T-CAP-010 — Stale dependency

Expired load-bearing dependency must invalidate eligibility.

### T-CAP-011 — Provider substitution

Provider replacement must not occur silently when semantic equivalence is unverified.

### T-CAP-012 — Side-effect containment

Read-only capability must not create persistent writes.

### T-CAP-013 — Confidence propagation

Derived confidence must respect load-bearing premise ceilings.

### T-CAP-014 — Correlated evidence

Duplicate ancestry must not be counted as independent confirmation.

### T-CAP-015 — Rollback

Declared reversible effects must pass rollback validation.

### T-CAP-016 — Commit freshness

Revocation between proposal and commit must block commit.

### T-CAP-017 — Dependency cycle

Circular capability dependencies must be detected.

### T-CAP-018 — Failure provenance

Failed invocation must retain sufficient diagnostic provenance.

---

# 46. Falsifiers

The capability contract is falsified for a specific provider if evidence demonstrates, within the claimed scope/regime, that:

```text
declared inputs cannot be accepted;
declared outputs cannot be produced;
required invariants are violated;
undeclared side effects occur;
provider identity cannot be established;
dependency assumptions are false;
claimed validation cannot be reproduced;
scope claims exceed observed behavior;
rollback claims fail;
revocation is ignored;
authority checks can be bypassed;
provenance cannot be reconstructed;
commit occurs without required authorization.
```

A falsifier SHOULD invalidate only the affected claim and its dependents unless evidence supports broader invalidation.

---

# 47. Capability Registry Record

Canonical proposed registry object:

```yaml
capability:
  capability_id: "CAP_EXAMPLE"
  name: "Example Capability"
  version: "1.0.0"

  provider:
    provider_id: "PROVIDER_EXAMPLE"
    provider_type: "SKILL"

  status:
    declaration: DECLARED
    availability: UNKNOWN
    validation: UNVALIDATED
    revocation: ACTIVE

  classes:
    - ANALYSIS

  inputs: []

  outputs: []

  preconditions: []

  dependencies: []

  scope:
    systems: []
    domains: []
    scales: []
    environments: []

  regime:
    allowed: []
    prohibited: []

  authority:
    invocation_required: true
    commit_required: true

  effects:
    maximum_effect_class: E0_READ_ONLY

  provenance:
    sources: []
    ancestry: []

  validation:
    evidence: []
    validators: []
    last_validated_at: null

  freshness:
    checked_at: null
    expires_at: null

  uncertainty:
    evidence: null
    model: null
    scope: null
    temporal: null
    causal: null
    execution: null
    provenance_independence: null

  confidence_ceiling: 0

  failures: []

  rollback:
    supported: false

  supersession:
    supersedes: []
    superseded_by: null
```

---

# 48. RSCF Binding

Every consequential capability claim SHOULD be representable as an RSCF capsule.

```yaml
rscf:
  claim:
    id: "RSCF_CAPABILITY_*"
    text: "Provider P can perform capability C under scope S and regime R."
    class: MODEL

  premises:
    - provider_identity_valid
    - interface_contract_valid
    - dependencies_satisfied
    - environment_compatible

  evidence: []

  provenance: []

  scope: null

  regime: null

  freshness: null

  dependencies: []

  competing:
    - provider_unavailable
    - capability_scope_narrower_than_declared
    - dependency_incompatible

  falsifiers: []

  confidence_ceiling: 0
```

Promotion requires evidence.

---

# 49. GMEF Binding

A capability change may require governed evolution review when it modifies:

```text
permissions
effect class
input access
memory access
external communication
authority requirements
commit behavior
security boundary
validation requirements
rollback semantics
dependency topology
```

Capability evolution MUST NOT silently weaken existing constraints.

A new version that expands capability surface SHOULD be treated as a governed change rather than an innocuous metadata update.

---

# 50. Versioning and Supersession

Capability contracts MUST preserve version lineage.

Recommended semantic interpretation:

```text
PATCH:
non-semantic clarification or compatible repair

MINOR:
backward-compatible capability extension

MAJOR:
breaking semantic, authority, effect, schema, or governance change
```

Supersession record:

```yaml
supersession:
  previous_version: null
  reason: null
  migration_required: false
  invalidates_prior_validation: false
```

A new version MUST NOT automatically inherit validation when material semantics changed.

---

# 51. Security Boundary

Capabilities SHOULD declare security-sensitive operations.

Examples:

```text
credential access
secret access
privileged filesystem access
code execution
network access
external communication
identity management
policy modification
permission modification
persistent memory mutation
financial action
deployment
```

Security-sensitive capabilities require stronger authority and observability.

---

# 52. Capability Discovery Protocol

Discovery SHOULD return candidates rather than executable authority.

```yaml
discovery_result:
  requirement_id: string
  candidates:
    - capability_id: string
      provider_id: string
      match_strength: null
      validation_state: string
      availability: string
      authority_state: UNKNOWN
      unresolved_requirements: []
```

The resolver MUST NOT hide unresolved requirements merely to return a candidate.

---

# 53. Capability Resolution Protocol

Resolution SHOULD follow:

```text
REQUIREMENT
    ↓
TYPE MATCH
    ↓
SEMANTIC MATCH
    ↓
SCOPE MATCH
    ↓
REGIME MATCH
    ↓
DEPENDENCY CHECK
    ↓
VALIDATION CHECK
    ↓
FRESHNESS CHECK
    ↓
GOVERNANCE CHECK
    ↓
CANDIDATE SET
```

Authority validation may occur after candidate resolution but before invocation.

---

# 54. Adversarial Validation

For consequential capabilities, validation SHOULD challenge the capability using a genuinely different path.

Challenge questions include:

```text
Is the provider actually the provider claimed?
Are multiple validation results correlated?
Is the interface documented but unimplemented?
Did the provider change after validation?
Does the capability work only on the happy path?
Does it violate scope under edge cases?
Can authority be bypassed?
Can side effects escape the declared envelope?
Can malformed inputs create unsafe behavior?
Does rollback actually restore prior state?
```

A failed challenge downgrades or invalidates the relevant capability claim.

---

# 55. Sensitivity Analysis

For consequential capability selection, identify the smallest assumption capable of changing the selection or authorization result.

Examples:

```text
provider availability
dependency version
authority expiration
policy version
confidence threshold
effect classification
scope boundary
```

Fragile selections SHOULD be marked `CONDITIONAL`.

---

# 56. Capability Decision States

Canonical decision outputs:

```text
ALLOW
ALLOW_CONDITIONAL
DENY
QUARANTINE
ESCALATE
UNKNOWN/GAP
```

`UNKNOWN/GAP` is never an alias for `ALLOW`.

---

# 57. Minimum Capability Admission Gate

A capability SHOULD NOT enter an active governed registry unless it has at least:

```text
stable identity
provider identity
declared input contract
declared output contract
scope
effect class
dependency list
authority requirements
failure behavior
provenance source
validation state
version
```

Missing noncritical fields MAY remain gaps.

Missing critical governance fields SHOULD block active promotion.

---

# 58. Promotion States

Recommended lifecycle:

```text
PLACEHOLDER
    ↓
DECLARED
    ↓
STRUCTURALLY_COMPLETE
    ↓
ADDRESSABLE
    ↓
IMPLEMENTED
    ↓
TESTED
    ↓
VALIDATED
    ↓
GOVERNED_ACTIVE
```

These states MUST NOT collapse into one another.

For example:

```text
STRUCTURALLY_COMPLETE != IMPLEMENTED
IMPLEMENTED != VALIDATED
VALIDATED != AUTHORIZED_FOR_ALL_USES
```

---

# 59. Gap Matrix

| Field                         |                    Required | Current contract status |
| ----------------------------- | --------------------------: | ----------------------- |
| Definition                    |                         Yes | Specified               |
| Scope model                   |                         Yes | Specified               |
| Typed inputs                  |                         Yes | Schema specified        |
| Typed outputs                 |                         Yes | Schema specified        |
| State variables               |                         Yes | Specified               |
| Operators                     |                         Yes | Specified               |
| Invariants                    |                         Yes | Specified               |
| Dependencies                  |                         Yes | Specified               |
| H/M/L                         |                         Yes | Specified               |
| Control-plane requirements    |                         Yes | Specified               |
| Agent binding                 |                         Yes | Specified               |
| Skill binding                 |                         Yes | Specified               |
| Workflow binding              |                         Yes | Specified               |
| Protocols                     |                         Yes | Specified               |
| Provenance                    |                         Yes | Specified               |
| Uncertainty                   |                         Yes | Specified               |
| Confidence ceiling            |                         Yes | Specified               |
| Failure modes                 |                         Yes | Specified               |
| Repair                        |                         Yes | Specified               |
| Tests                         |                         Yes | Specified               |
| Falsifiers                    |                         Yes | Specified               |
| Actual runtime implementation |           Yes for promotion | UNKNOWN/GAP             |
| Executed test evidence        |          Yes for validation | UNKNOWN/GAP             |
| Canon approval                | Yes for canonical promotion | UNKNOWN/GAP             |
| Production validation         |           Context-dependent | UNKNOWN/GAP             |

---

# 60. Current Gap Status

This document closes the **structural contract-definition gap** for the proposed capability architecture.

It does NOT close:

```text
runtime implementation gap
executed-test gap
empirical-validation gap
canon-admission gap
provider-specific validation gaps
authority configuration gaps
production-readiness gap
```

Therefore:

```yaml
gap_status:
  structural_definition: CLOSED_AS_MODEL
  implementation: UNKNOWN/GAP
  executed_validation: UNKNOWN/GAP
  canon_status: UNKNOWN/GAP
  production_status: UNKNOWN/GAP
```

---

# 61. RSCF Completion State

```yaml
claim_class: MODEL

claim:
  "This document defines a proposed governed AMOS capability contract."

evidence:
  - "Existing AMOS architecture/capability materials require explicit separation of capability, governance, provenance, validation, and execution."

provenance:
  origin_architect: "Trang Phan"
  artifact: "CAPABILITY_CONTRACT.md"
  derivation: "AMOS contract synthesis"
  generated_status: "PROPOSED"

scope:
  system: "AMOS OS"
  layer: "Capability / infrastructure governance"
  applicability: "Capability declaration, resolution, invocation, validation and effect governance"

regime:
  - design
  - implementation
  - runtime_governance

freshness:
  reviewed_at: "2026-08-26"
  revalidation_trigger:
    - capability architecture change
    - control-plane architecture change
    - authority model change
    - canon supersession

dependencies:
  - capability_registry
  - policy_registry
  - control_plane_map
  - provenance_model
  - authority_model
  - validation_model

competing:
  - "A simpler capability interface may be sufficient for low-consequence local execution."
  - "Provider-specific contracts may require stricter domain rules."
  - "Future AMOS canon may define different canonical field names or lifecycle states."

falsifiers:
  - "Canonical AMOS source explicitly defines an incompatible capability contract."
  - "Runtime implementation demonstrates materially different required semantics."
  - "Governance review rejects one or more proposed invariants."

confidence_ceiling:
  structural_model: 0.90
  canonical_status: 0.00
  implementation_status: 0.00
  empirical_validation: 0.00
```

---

# 62. Hard Boundary Block

The following boundary block is normative for this contract:

```text
PLACEHOLDER != IMPLEMENTED
DECLARED != IMPLEMENTED
ADDRESSABLE != VALIDATED
IMPLEMENTED != VALIDATED
CAPABILITY != AUTHORITY
CAPABILITY != PERMISSION
AVAILABILITY != AUTHORIZATION
PROPOSAL != COMMIT
EXECUTION_SUCCESS != CLAIM_TRUTH
VALIDATION != UNIVERSAL_VALIDITY
UNKNOWN/GAP != PASS
CORRELATED_EVIDENCE != INDEPENDENT_CONFIRMATION
MODEL != EMPIRICAL_FACT
```

---

# 63. Canon and Provenance Boundary

Trang Phan remains the origin architect / steward for AMOS material represented by this artifact.

This generated contract MUST NOT be interpreted merely from its completeness as proof that every definition, operator, lifecycle state, equation, threshold, or field name already exists in source canon.

Until separately admitted through the appropriate AMOS canon/provenance/supersession process:

```text
document status = PROPOSED AMOS MODEL CONTRACT
canonical status = UNKNOWN/GAP
implementation status = UNKNOWN/GAP
validation status = UNKNOWN/GAP
```

Where future canonical source conflicts with this document:

```text
SOURCE CANON
    >
GENERATED MODEL
```

subject to version and supersession resolution.

---

# 64. Final Contract Law

The AMOS capability layer SHALL preserve the following governing principle:

> A capability describes a bounded potential transformation. It does not grant the authority to perform that transformation, establish that the transformation is currently available, prove that its result is correct, or authorize the resulting effect to become durable.

Therefore the canonical governed path is:

```text
CAPABILITY
    ↓
COMPATIBILITY
    ↓
VALIDATION
    ↓
AUTHORITY
    ↓
INVOCATION
    ↓
OBSERVATION
    ↓
RESULT VALIDATION
    ↓
PROPOSAL
    ↓
COMMIT-TIME REVALIDATION
    ↓
AUTHORIZED COMMIT
    ↓
PROVENANCE-PRESERVED EFFECT
```

Any path that bypasses a load-bearing gate MUST fail closed, remain `UNKNOWN/GAP`, or escalate according to consequence and authority requirements.

---

# END — CAPABILITY_CONTRACT.md

```

This is substantially different from the existing Drive file, which currently contains only the unrelated `K COUNTERFACTUAL` placeholder.

The important epistemic boundary is that the content above **completes the architecture as a proposed contract**, but does not pretend the runtime, tests, or canon approval already exist.
```

---

[[00_ROOT_MOC]]|[[AMOS MOC]]

---
**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: control_plane_capability_contract
node_type: note
path: 03_CONTROL_PLANE/02_CAPABILITY/CONTROL_PLANE_CAPABILITY_CONTRACT.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[02_CAPABILITY_MOC]]
