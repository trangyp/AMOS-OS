---
title: CAPABILITY MANIFEST
type: manifest
source: 03_CONTROL_PLANE/02_CAPABILITY
tags:
- control_plane
- capability
- note
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

# AMOS Capability Manifest

## 0. Status

This document defines the AMOS OS manifest structure for discovering, indexing, resolving, validating, governing, versioning, and auditing capabilities.

It is the machine-oriented companion to:

```text
CAPABILITY_CONTRACT.md
```

The contract defines what a valid AMOS capability means.

The manifest defines how capability declarations are represented as an addressable governed inventory.

This document provides a complete structural specification.

It does **not** assert that:

* every capability listed or addressable in AMOS is implemented;
* every provider exists at runtime;
* every declared interface has been tested;
* every capability has been canonically approved;
* every capability is currently available;
* every capability is authorized for invocation;
* every capability is authorized to create effects;
* every capability has passed empirical validation;
* every proposed capability entry may be promoted into active runtime state.

The governing distinctions are:

```text
MANIFEST_ENTRY != IMPLEMENTATION
DECLARED != AVAILABLE
ADDRESSABLE != VALIDATED
DISCOVERABLE != AUTHORIZED
CAPABILITY != AUTHORITY
CAPABILITY != PERMISSION
COMPATIBLE != SELECTED
SELECTED != INVOKED
INVOKED != SUCCEEDED
SUCCEEDED != VALIDATED
VALIDATED != COMMITTED
PROPOSAL != COMMIT
UNKNOWN/GAP != PASS
```

---

# 1. Purpose

The AMOS Capability Manifest provides the canonical inventory surface through which AMOS components can determine:

```text
what capabilities are declared;
who or what provides them;
which version is being referenced;
what functional class they belong to;
which inputs and outputs they expose;
what dependencies they require;
what scopes and regimes they support;
what effects they may create;
which authority they require;
which policies constrain them;
which control planes govern them;
what validation state they occupy;
what evidence supports them;
what provenance they carry;
whether they are fresh;
whether they have been revoked;
whether they supersede another capability;
and whether they are eligible for runtime consideration.
```

The manifest exists to make capability topology explicit rather than allowing capability assumptions to remain embedded implicitly inside agents, Skills, prompts, workflows, or code.

---

# 2. Manifest Role in AMOS

The capability layer SHOULD be separated into at least four conceptual artifacts:

```text
CAPABILITY_CONTRACT.md
        ↓
defines capability semantics

CAPABILITY_MANIFEST.md
        ↓
defines manifest semantics and registry structure

CAPABILITY_REGISTRY
        ↓
contains instantiated capability records

CONTROL PLANE
        ↓
resolves and governs runtime use
```

Therefore:

```text
CONTRACT = rules

MANIFEST = governed inventory representation

REGISTRY = instantiated state

CONTROL PLANE = enforcement and resolution
```

These objects MUST NOT be silently conflated.

---

# 3. Non-Purpose

The capability manifest is not:

```text
an authorization list;
an access-control list;
a runtime scheduler;
a Skill registry replacement;
an agent registry replacement;
a policy registry replacement;
a workflow definition;
a tool implementation;
an empirical benchmark;
a proof of capability;
a proof of provider availability;
a proof of provider trustworthiness;
a commit ledger.
```

It may reference these structures.

It MUST NOT impersonate them.

---

# 4. Manifest Object

Conceptually:

```text
CapabilityManifest :=
    ManifestIdentity
  × ManifestVersion
  × CapabilityEntries
  × ProviderIndex
  × DependencyTopology
  × GovernanceBindings
  × ValidationBindings
  × ProvenanceBindings
  × SupersessionTopology
  × GapState
```

Canonical top-level representation:

```yaml
capability_manifest:
  manifest_id: "AMOS_CAPABILITY_MANIFEST"
  version: "1.0.0"
  schema_version: "1.0.0"

  origin_architect: "Trang Phan"
  steward: "Trang Phan"

  system: "AMOS OS"

  status: "PROPOSED"
  epistemic_class: "MODEL"

  generated_at: null
  updated_at: "2026-08-26"

  capabilities: []
  providers: []
  dependencies: []
  policies: []
  control_planes: []
  validators: []
  supersession: []
  gaps: []
```

---

# 5. Manifest Identity

Every manifest instance MUST possess a stable identity.

```yaml
manifest_identity:
  manifest_id: string
  canonical_name: "AMOS Capability Manifest"
  version: string
  schema_version: string
  origin_architect: "Trang Phan"
  steward: "Trang Phan"
```

Manifest identity MUST remain separate from the identities of individual capabilities.

---

# 6. Capability Entry

The atomic manifest unit is a `CapabilityEntry`.

Minimum form:

```yaml
capability:
  capability_id: string
  canonical_name: string
  version: string

  provider_id: string
  provider_type: string

  status: string
  validation_state: string

  capability_classes: []

  input_contract: []
  output_contract: []

  dependencies: []

  scope: {}
  regime: {}

  authority_requirements: {}
  effect_class: string

  provenance: {}
```

A manifest entry is a **declaration record**.

Its existence does not establish implementation.

---

# 7. Canonical Full Capability Record

Recommended full record:

```yaml
capability:
  identity:
    capability_id: "CAP_*"
    canonical_name: string
    aliases: []
    version: string
    schema_version: string

  ownership:
    origin_architect: "Trang Phan"
    steward: "Trang Phan"

  provider:
    provider_id: string
    provider_type: AGENT | SKILL | TOOL | WORKFLOW | SERVICE | MODEL | RUNTIME | CONTROL_PLANE | DETERMINISTIC_FUNCTION
    provider_version: null

  classification:
    capability_classes: []
    epistemic_class: MODEL
    consequence_class: null
    sensitivity_class: null

  lifecycle:
    declaration_state: DECLARED
    implementation_state: UNKNOWN
    availability_state: UNKNOWN
    validation_state: UNVALIDATED
    governance_state: UNREVIEWED
    revocation_state: ACTIVE

  inputs: []

  outputs: []

  state_requirements: []

  preconditions: []

  postconditions: []

  dependencies: []

  scope:
    domains: []
    systems: []
    populations: []
    environments: []
    scales: []
    observers: []
    exclusions: []

  regime:
    allowed: []
    prohibited: []
    assumptions: []

  hml:
    H: false
    M: false
    L: false

  effects:
    maximum_effect_class: E0_READ_ONLY
    possible_effects: []
    reversible: null
    rollback_contract: null

  authority:
    invocation_required: true
    effect_authority_required: true
    commit_authority_required: true
    authority_classes: []

  governance:
    policy_refs: []
    control_plane_refs: []
    escalation_refs: []

  validation:
    level: V0_DECLARED
    validators: []
    evidence_refs: []
    last_validated_at: null
    expires_at: null

  provenance:
    source_refs: []
    ancestry: []
    derivation_refs: []
    independence_status: UNKNOWN

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

  repair:
    supported: null
    strategy_refs: []

  tests: []

  falsifiers: []

  supersession:
    supersedes: []
    superseded_by: null

  gaps: []
```

---

# 8. Capability Classes

The manifest SHOULD support the following base classes:

```text
PERCEPTION
OBSERVATION
INGESTION
RETRIEVAL
SEARCH
MEMORY_READ
MEMORY_WRITE

TRANSFORMATION
TRANSLATION
NORMALIZATION
CLASSIFICATION
EXTRACTION
COMPRESSION

REASONING
ANALYSIS
INFERENCE
CAUSAL_ANALYSIS
COUNTERFACTUAL_ANALYSIS

PREDICTION
FORECASTING
SIMULATION

PLANNING
DECISION_SUPPORT
OPTIMIZATION

GENERATION
SYNTHESIS
CODE_GENERATION
DOCUMENT_GENERATION

VALIDATION
VERIFICATION
TESTING
AUDIT

ORCHESTRATION
ROUTING
COORDINATION

CONTROL
POLICY_EVALUATION
AUTHORITY_EVALUATION
COMMIT_CONTROL

REPAIR
RECOVERY
ROLLBACK

COMMUNICATION
EXTERNAL_ACTION
EXECUTION

OBSERVABILITY
PROVENANCE
GOVERNANCE
```

Capability class assignment is descriptive.

It does not grant authority.

---

# 9. Provider Manifest

Providers SHOULD be independently registered.

```yaml
provider:
  provider_id: string
  canonical_name: string
  provider_type: string
  version: string

  status:
    registered: true
    implementation: UNKNOWN
    availability: UNKNOWN
    validation: UNVALIDATED

  capabilities: []

  provenance:
    source_refs: []

  supersession:
    supersedes: []
    superseded_by: null
```

This prevents provider metadata from being duplicated inconsistently across capability entries.

---

# 10. Provider Types

Supported provider types SHOULD include:

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
HUMAN_AUTHORITY
```

`HUMAN_AUTHORITY` may provide governance decisions but SHOULD NOT automatically be represented as equivalent to computational providers.

---

# 11. Capability-to-Provider Relation

Canonical relation:

```text
Provider(P) --PROVIDES--> Capability(C)
```

A provider may expose many capabilities:

```text
P → {C1, C2, C3}
```

A capability may have multiple providers:

```text
C ← {P1, P2, P3}
```

However:

```text
P1 provides C
AND
P2 provides C
```

does NOT establish:

```text
behavior(P1) = behavior(P2)
```

Provider substitution requires compatibility evidence.

---

# 12. Input Manifest

Each input MUST be typed.

```yaml
input:
  name: string
  type: string

  required: true
  nullable: false

  schema_ref: null

  units: null
  domain: null

  scope_requirement: null
  regime_requirement: null

  provenance_required: true
  freshness_requirement: null

  sensitivity_class: null
```

Input types SHOULD be sufficiently precise to prevent unsafe coercion.

---

# 13. Output Manifest

Each output SHOULD declare:

```yaml
output:
  name: string
  type: string

  schema_ref: null

  epistemic_class:
    - OBSERVATION
    - SOURCE_CLAIM
    - DERIVED
    - MODEL
    - PREDICTION
    - PROPOSAL
    - DECISION
    - EFFECT
    - UNKNOWN/GAP

  provenance_required: true
  uncertainty_required: true
```

Outputs MUST NOT silently change epistemic class downstream.

---

# 14. Capability State Model

Manifest state MUST distinguish independent lifecycle dimensions.

## Declaration

```text
PLACEHOLDER
DECLARED
STRUCTURALLY_COMPLETE
```

## Implementation

```text
UNKNOWN
NOT_IMPLEMENTED
PARTIALLY_IMPLEMENTED
IMPLEMENTED
```

## Availability

```text
UNKNOWN
AVAILABLE
DEGRADED
UNAVAILABLE
```

## Validation

```text
UNVALIDATED
PARTIALLY_VALIDATED
VALIDATED
INVALIDATED
```

## Governance

```text
UNREVIEWED
CONDITIONAL
APPROVED
DENIED
QUARANTINED
```

## Revocation

```text
ACTIVE
SUSPENDED
REVOKED
```

These axes MUST remain independent.

For example:

```yaml
implementation_state: IMPLEMENTED
validation_state: UNVALIDATED
governance_state: UNREVIEWED
```

is valid.

It MUST NOT be automatically normalized to `VALIDATED`.

---

# 15. Manifest State Invariant

No convenience status field may erase the underlying state vector.

Conceptually:

```text
CapabilityState =
(
 declaration,
 implementation,
 availability,
 validation,
 governance,
 revocation
)
```

A summary label MAY be generated.

The original vector MUST remain recoverable.

---

# 16. Dependency Manifest

Dependencies SHOULD be explicit edges.

```yaml
dependency:
  dependency_id: string

  from_capability: string
  to_object: string

  dependency_type:
    - CAPABILITY
    - PROVIDER
    - SKILL
    - TOOL
    - DATA
    - MODEL
    - POLICY
    - AUTHORITY
    - CONTROL_PLANE
    - SCHEMA
    - MEMORY
    - SERVICE
    - VALIDATOR
    - ENVIRONMENT

  required: true

  version_constraint: null
  freshness_constraint: null

  validation_required: true

  failure_behavior:
    - FAIL_CLOSED
    - DEGRADE
    - ESCALATE
```

---

# 17. Dependency Invariant

For required dependency `d`:

```text
required(d)
AND
unsatisfied(d)
→
capability not fully eligible
```

Unless an explicitly declared fallback exists.

---

# 18. Optional Dependencies

Optional dependencies MUST NOT be disguised as mandatory requirements.

```yaml
required: false
```

The manifest SHOULD describe what changes when the dependency is unavailable.

Example:

```yaml
degradation:
  without_dependency:
    capability_scope_reduced: true
    unavailable_outputs:
      - "high_confidence_validation"
```

---

# 19. Capability Composition Graph

The manifest MAY describe compositional relationships:

```text
CAP_A
  ↓
CAP_B
  ↓
CAP_C
```

or:

```text
CAP_A ─┐
       ├→ CAP_D
CAP_B ─┘
```

Graph edges MUST distinguish:

```text
REQUIRES
OPTIONALLY_USES
VALIDATES
SUPERVISES
PRODUCES_INPUT_FOR
CONSUMES_OUTPUT_OF
REPAIRS
FALLBACK_FOR
SUPERSEDES
CONFLICTS_WITH
```

---

# 20. Circular Dependency Detection

Cycles MUST be visible.

Example:

```text
CAP_A requires CAP_B
CAP_B requires CAP_C
CAP_C requires CAP_A
```

The registry MUST NOT interpret such a cycle as satisfied merely because every capability is addressable.

Cycle resolution requires:

```text
external base condition;
cycle-breaking provider;
lazy dependency;
or explicit recursive semantics.
```

Otherwise:

```text
dependency_state = GAP
```

---

# 21. H/M/L Manifest

Each capability SHOULD declare scale applicability.

```yaml
hml:
  H:
    applicable: true
    role: "system-level governance"

  M:
    applicable: true
    role: "workflow/subsystem coordination"

  L:
    applicable: false
```

H/M/L applicability does not mean the same implementation is valid at every scale.

---

# 22. Cross-Scale Capability Relations

The manifest MAY declare:

```text
H constrains M
M constrains L
L produces evidence for M
M aggregates evidence for H
```

Cross-scale mappings MUST preserve:

```text
scope
meaning
provenance
confidence
authority
```

A local result MUST NOT automatically become a global system claim.

---

# 23. Scope Manifest

Capabilities MUST declare an applicability envelope when material.

```yaml
scope:
  domains: []
  systems: []
  populations: []
  resources: []
  environments: []
  scales: []
  observers: []
  time_horizons: []
  exclusions: []
```

Empty scope fields mean:

```text
UNKNOWN / UNSPECIFIED
```

unless the schema explicitly defines a universal wildcard.

They MUST NOT silently mean:

```text
ALL
```

---

# 24. Regime Manifest

Capabilities SHOULD declare regime assumptions.

```yaml
regime:
  allowed:
    - development
    - simulation

  prohibited:
    - production

  assumptions:
    - string

  transition_revalidation_required: true
```

A capability validated in simulation MUST NOT automatically inherit production validity.

---

# 25. Effect Manifest

Every capability MUST declare its maximum possible effect class.

Recommended classes:

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

Example:

```yaml
effects:
  maximum_effect_class: E3_PERSISTENT_WRITE

  possible_effects:
    - "memory_write"
    - "artifact_update"

  irreversible_effects: []

  rollback:
    supported: true
```

---

# 26. Effect-Class Invariant

A capability MUST NOT produce an effect stronger than its manifest permits.

```text
actual_effect_class
≤
declared_maximum_effect_class
```

Any violation is a contract breach.

---

# 27. Capability and Authority

Authority metadata MUST be separate from capability metadata.

```yaml
authority:
  invocation_required: true

  required_scopes: []

  effect_authority_required: true

  commit_authority_required: true

  authority_registry_refs: []

  freshness_required: true
```

The manifest MUST NOT contain:

```yaml
capability:
  authorized: true
```

without an external authority basis and applicability context.

Authority is contextual.

---

# 28. Authority Invariant

```text
CAPABILITY(C)
+
PROVIDER(P)
+
AVAILABLE(P)
```

does NOT entail:

```text
AUTHORIZED(P, C)
```

Authorization requires an independent authority evaluation.

---

# 29. Policy Binding

Capabilities SHOULD reference applicable policy rather than embedding all policy logic locally.

```yaml
governance:
  policy_refs:
    - "POLICY_*"

  control_plane_refs:
    - "CONTROL_PLANE_*"

  authority_refs: []

  escalation_refs: []
```

Policy references MUST be version-aware when policy changes could alter eligibility.

---

# 30. Control-Plane Binding

A capability MAY be governed by one or more control planes.

Examples:

```text
SESSION_CONTROL
AUTHORITY_CONTROL
POLICY_CONTROL
PROVENANCE_CONTROL
MEMORY_CONTROL
INFORMATION_EXPOSURE_CONTROL
COMMIT_CONTROL
RECOVERY_CONTROL
OBSERVABILITY_CONTROL
```

Manifest entry:

```yaml
control_planes:
  required:
    - CONTROL_PLANE_AUTHORITY
    - CONTROL_PLANE_PROVENANCE

  optional:
    - CONTROL_PLANE_OBSERVABILITY
```

A capability MUST NOT silently bypass a required control plane.

---

# 31. Agent Binding

Agent relationships SHOULD be explicit.

```yaml
agents:
  providers: []
  consumers: []
  validators: []
  supervisors: []
```

Roles MUST remain distinguishable.

An agent that consumes a capability does not thereby become its provider.

An agent that provides a capability does not thereby become its validator.

---

# 32. Skill Binding

Capability-to-Skill relations SHOULD include:

```yaml
skills:
  provided_by: []
  required_by: []
  validated_by: []
  composed_with: []
```

A Skill MAY expose multiple capabilities.

The capability manifest SHOULD remain the authority-neutral description of those capabilities.

---

# 33. Workflow Binding

Capabilities MAY declare workflow participation:

```yaml
workflows:
  entrypoints: []
  used_by: []
  predecessor_capabilities: []
  successor_capabilities: []
  rollback_workflows: []
  recovery_workflows: []
```

Workflow membership does not imply universal capability availability.

---

# 34. Protocol Binding

A capability SHOULD declare its invocation protocol.

```yaml
protocol:
  request_schema_ref: null
  response_schema_ref: null

  timeout_policy_ref: null
  retry_policy_ref: null

  transaction_required: false
  idempotent: null

  streaming_supported: false

  cancellation_supported: null
```

Protocol compatibility SHOULD be checked during provider resolution.

---

# 35. Validation Manifest

Each capability SHOULD expose validation evidence separately from declaration state.

```yaml
validation:
  level: V0_DECLARED

  evidence_refs: []

  validators: []

  test_refs: []

  environment_refs: []

  last_validated_at: null

  expires_at: null

  unresolved_failures: []
```

Recommended validation ladder:

```text
V0_DECLARED
V1_STRUCTURALLY_VALID
V2_STATICALLY_CHECKED
V3_LOCALLY_TESTED
V4_INTEGRATION_TESTED
V5_ENVIRONMENT_VALIDATED
V6_INDEPENDENTLY_VALIDATED
V7_GOVERNED_PRODUCTION_VALIDATED
```

These are proposed manifest states, not empirical claims about existing AMOS runtime coverage.

---

# 36. Validation Scope

Validation MUST carry scope.

Example:

```yaml
validation_scope:
  provider_version: "1.2.0"
  environment: "development"
  operating_system: null
  dependency_versions: {}
  input_classes: []
  output_classes: []
  regime: []
```

A validation result outside its envelope becomes:

```text
NON-APPLICABLE
```

rather than automatically false or true.

---

# 37. Evidence Manifest

Evidence record:

```yaml
evidence:
  evidence_id: string

  evidence_class:
    - SOURCE_CLAIM
    - DOCUMENTED_INTERFACE
    - STATIC_INSPECTION
    - UNIT_TEST
    - INTEGRATION_TEST
    - RUNTIME_OBSERVATION
    - BENCHMARK
    - FORMAL_CHECK
    - INDEPENDENT_VALIDATION
    - PRODUCTION_OBSERVATION

  source_id: string
  source_version: null

  observed_at: null

  environment: null

  supports: []
  contradicts: []

  ancestry: []

  independence_status:
    - INDEPENDENT
    - CORRELATED
    - SHARED_ORIGIN
    - UNKNOWN
```

---

# 38. Provenance Manifest

Each capability SHOULD preserve:

```yaml
provenance:
  source_refs: []
  source_versions: []

  origin_refs: []

  derivation_refs: []

  ancestry: []

  hashes: []

  generated_by: null

  generated_at: null

  independence_status: UNKNOWN
```

A capability synthesized from multiple files SHOULD preserve those source relations rather than presenting itself as source-independent canon.

---

# 39. Provenance Independence

Evidence multiplicity is not independence.

For evidence:

```text
E1
E2
E3
```

if:

```text
ancestor(E1) = ancestor(E2) = ancestor(E3)
```

then three entries do not constitute three independent confirmations.

The manifest SHOULD preserve this topology.

---

# 40. Freshness Manifest

Capability validity may decay when its environment changes.

```yaml
freshness:
  manifest_checked_at: null
  provider_checked_at: null
  validation_checked_at: null
  authority_checked_at: null
  policy_checked_at: null

  expires_at: null

  invalidation_events:
    - provider_version_change
    - schema_change
    - policy_change
    - authority_revocation
    - dependency_change
    - environment_change
```

---

# 41. Supersession Manifest

Version lineage MUST be explicit.

```yaml
supersession:
  capability_id: string
  version: string

  supersedes:
    - capability_id: string
      version: string

  superseded_by: null

  reason: string

  compatibility:
    backward_compatible: null
    semantic_equivalence: null

  validation_inherited: false
```

Validation SHOULD NOT automatically transfer across a material semantic change.

---

# 42. Aliases

Aliases MAY support discovery.

```yaml
aliases:
  - name: string
    type:
      - LEGACY_NAME
      - SHORT_NAME
      - HUMAN_LABEL
      - MIGRATION_ALIAS
```

Aliases MUST resolve to one canonical capability identity within a declared version context.

---

# 43. Capability Conflict Registry

Capabilities MAY conflict.

```yaml
conflicts:
  - capability_id: string
    conflict_type:
      - MUTUALLY_EXCLUSIVE
      - POLICY_CONFLICT
      - STATE_CONFLICT
      - RESOURCE_CONFLICT
      - SEMANTIC_CONFLICT
    reason: string
```

Conflict MUST NOT be silently resolved through arbitrary provider ordering.

---

# 44. Fallback Manifest

Fallbacks SHOULD be explicit.

```yaml
fallbacks:
  - capability_id: string

    conditions:
      - "primary unavailable"

    equivalence:
      semantic: UNKNOWN
      output_schema: COMPATIBLE

    validation_required: true
```

A fallback is not assumed equivalent merely because it accepts the same inputs.

---

# 45. Capability Resolution

Resolution SHOULD produce candidate capabilities.

Conceptually:

```text
Resolve(requirement, context, manifest)
    →
CandidateSet
```

Candidate eligibility SHOULD consider:

```text
semantic match
input compatibility
output compatibility
scope
regime
dependencies
availability
validation
freshness
effect class
governance requirements
```

Authority SHOULD remain a separate gate.

---

# 46. Candidate Record

```yaml
candidate:
  capability_id: string
  provider_id: string

  match:
    semantic: null
    input: null
    output: null
    scope: null
    regime: null

  validation_state: string
  availability_state: string

  unresolved_dependencies: []

  governance_requirements: []

  authority_state: UNKNOWN

  eligible_for_consideration: null
```

`eligible_for_consideration` is not `authorized`.

---

# 47. Capability Selection

Selection SHOULD preserve why a candidate was selected.

```yaml
selection:
  requirement_id: string

  selected_capability: string
  selected_provider: string

  alternatives: []

  reasons: []

  rejected_candidates:
    - capability_id: string
      reason: string

  unresolved_uncertainty: []

  decision_class:
    - VERIFIED
    - DERIVED
    - MODEL
    - CONDITIONAL
    - COMPETING
    - UNKNOWN/GAP
```

---

# 48. Competing Providers

When two providers are materially incomparable:

```text
P1 → C
P2 → C
```

and no evidence establishes dominance, the manifest/resolver SHOULD preserve:

```text
COMPETING
```

rather than inventing convergence.

Discriminating evidence may include:

```text
validation strength
scope match
freshness
failure rate
cost
latency
effect surface
security posture
dependency burden
```

---

# 49. Uncertainty Vector

Each capability MAY carry:

```yaml
uncertainty:
  evidence: 1.0
  model: 1.0
  scope: 1.0
  temporal: 1.0
  causal: 1.0
  execution: 1.0
  provenance_independence: 1.0
```

The numerical representation is optional.

If used, its scale MUST be explicitly defined.

The manifest MUST NOT pretend undefined confidence numbers are objective measurements.

---

# 50. Confidence Ceiling

A capability confidence ceiling MAY be derived from load-bearing validation premises.

Conceptually:

```text
C_cap ≤ min(
    C_identity,
    C_provider,
    C_interface,
    C_dependencies,
    C_scope,
    C_regime,
    C_validation,
    C_freshness
)
```

unless independently validated evidence changes the dependency structure.

This is an AMOS MODEL governance equation.

---

# 51. Manifest Operators

The capability manifest SHOULD support these logical operations.

## `REGISTER`

```text
REGISTER(entry)
```

Adds an addressable declaration.

---

## `UPDATE`

```text
UPDATE(entry, revision)
```

Creates a new governed state while preserving lineage.

---

## `RESOLVE`

```text
RESOLVE(requirement)
```

Returns candidate entries.

---

## `VALIDATE`

```text
VALIDATE(entry, evidence)
```

Updates validation state if evidence warrants it.

---

## `INVALIDATE`

```text
INVALIDATE(entry, failed_premise)
```

Invalidates dependent claims.

---

## `SUSPEND`

```text
SUSPEND(entry)
```

Temporarily removes active eligibility.

---

## `REVOKE`

```text
REVOKE(entry)
```

Blocks governed future use.

---

## `SUPERSEDE`

```text
SUPERSEDE(old, new)
```

Preserves version lineage.

---

## `QUARANTINE`

```text
QUARANTINE(entry, reason)
```

Removes uncertain or suspect entries from normal resolution without deleting evidence.

---

## `REVALIDATE`

```text
REVALIDATE(entry, current_context)
```

Checks stale capability assumptions.

---

# 52. Manifest Invariants

## INV-MAN-001 — Stable Identity

Every active entry MUST have a stable capability ID and version.

## INV-MAN-002 — No Implicit Authority

Manifest presence grants no authority.

## INV-MAN-003 — No Implicit Implementation

Declaration does not prove implementation.

## INV-MAN-004 — No Implicit Validation

Implementation does not prove correctness.

## INV-MAN-005 — No Unknown-as-Pass

Required unknown fields remain gaps.

## INV-MAN-006 — Provenance Required

Material entries require provenance.

## INV-MAN-007 — Version Lineage

Material semantic changes require version/supersession treatment.

## INV-MAN-008 — Scope Preservation

Scope restrictions survive resolution and composition.

## INV-MAN-009 — Regime Preservation

Regime restrictions survive resolution and composition.

## INV-MAN-010 — Effect Bound

Actual effect cannot exceed declared maximum effect.

## INV-MAN-011 — Revocation Dominance

Revoked entries cannot remain normally eligible.

## INV-MAN-012 — Validation Locality

Validation applies only to its validated provider/version/scope/regime.

## INV-MAN-013 — Dependency Visibility

Load-bearing dependencies cannot be hidden.

## INV-MAN-014 — Correlated Provenance

Shared ancestry cannot masquerade as independent evidence.

## INV-MAN-015 — Proposal/Commit Separation

No manifest state may convert an effect proposal into commit authority.

---

# 53. Manifest Failure Modes

## FM-MAN-001 — Ghost Entry

Manifest references a provider or implementation that does not exist.

## FM-MAN-002 — Duplicate Identity

Different capabilities occupy the same ID/version.

## FM-MAN-003 — Semantic Alias Collision

One alias resolves to incompatible capability meanings.

## FM-MAN-004 — Stale Provider

Manifest references an obsolete provider version.

## FM-MAN-005 — Stale Validation

Validation remains marked current after invalidating changes.

## FM-MAN-006 — Orphan Capability

Capability has no resolvable provider.

## FM-MAN-007 — Orphan Dependency

Required dependency cannot be resolved.

## FM-MAN-008 — Circular Dependency

Dependency graph cannot reach a valid base state.

## FM-MAN-009 — Capability Inflation

Manifest scope exceeds evidence.

## FM-MAN-010 — Effect Understatement

Actual side effects exceed declared effect class.

## FM-MAN-011 — Authority Smuggling

Permission is encoded as capability metadata.

## FM-MAN-012 — Provenance Collapse

Source ancestry is lost.

## FM-MAN-013 — Validation Laundering

Validation from one provider/version is transferred to another without evidence.

## FM-MAN-014 — Supersession Loss

New entry silently replaces an older capability without lineage.

## FM-MAN-015 — Quarantine Bypass

Quarantined capability remains resolvable through alias or fallback.

## FM-MAN-016 — Revocation Bypass

Revoked provider remains reachable through cached resolution.

## FM-MAN-017 — Scope Wildcard Error

Empty scope is interpreted as universal applicability.

## FM-MAN-018 — Regime Wildcard Error

Unknown regime becomes universal regime.

## FM-MAN-019 — Confidence Inflation

Repeated dependent evidence raises confidence as if independent.

## FM-MAN-020 — Manifest/Runtime Divergence

Manifest declares behavior different from actual runtime behavior.

---

# 54. Repair / Recovery

Canonical repair sequence:

```text
DETECT
  ↓
FREEZE AFFECTED ENTRY
  ↓
PRESERVE EVIDENCE
  ↓
IDENTIFY FAILED FIELD / EDGE
  ↓
QUARANTINE IF NECESSARY
  ↓
INVALIDATE DEPENDENTS
  ↓
PRESERVE UNAFFECTED ENTRIES
  ↓
RECONSTRUCT PROVIDER / DEPENDENCY STATE
  ↓
REVALIDATE
  ↓
RESTORE OR SUPERSEDE
```

Global registry reconstruction SHOULD be a last resort.

---

# 55. Selective Invalidation

If:

```text
CAP_A depends on CAP_B
CAP_C does not depend on CAP_B
```

and `CAP_B` becomes invalid:

```text
invalidate CAP_A-derived eligibility
preserve CAP_C
```

This is preferred over global invalidation.

---

# 56. Quarantine

Quarantine SHOULD preserve the entry for investigation.

```yaml
quarantine:
  active: true
  reason: string
  entered_at: timestamp
  triggering_evidence: []
  affected_versions: []
  release_conditions: []
```

Quarantine is not deletion.

---

# 57. Tests / Validators

Minimum manifest tests:

```text
T-MAN-001 schema validity
T-MAN-002 unique capability identity
T-MAN-003 unique provider identity
T-MAN-004 alias resolution
T-MAN-005 provider resolution
T-MAN-006 dependency resolution
T-MAN-007 cycle detection
T-MAN-008 scope preservation
T-MAN-009 regime preservation
T-MAN-010 effect-bound validation
T-MAN-011 authority-separation validation
T-MAN-012 revocation enforcement
T-MAN-013 quarantine enforcement
T-MAN-014 supersession lineage
T-MAN-015 provenance ancestry
T-MAN-016 correlated-evidence detection
T-MAN-017 freshness invalidation
T-MAN-018 validation-scope isolation
T-MAN-019 provider substitution protection
T-MAN-020 unknown-not-pass
T-MAN-021 stale-cache rejection
T-MAN-022 capability/implementation distinction
T-MAN-023 proposal/commit distinction
T-MAN-024 selective invalidation
T-MAN-025 runtime-manifest consistency
```

---

# 58. Schema Validator

A structural validator SHOULD reject entries missing critical fields such as:

```text
capability_id
version
provider_id
provider_type
declaration state
effect class
authority requirement
provenance
```

unless the entry is explicitly classified:

```text
PLACEHOLDER / UNKNOWN/GAP
```

---

# 59. Semantic Validator

Schema validity is insufficient.

A semantic validator SHOULD inspect:

```text
contradictory lifecycle states;
invalid provider relationships;
scope contradictions;
regime contradictions;
impossible dependency constraints;
effect-class contradictions;
authority leakage;
invalid supersession;
unresolved canonical aliases.
```

---

# 60. Runtime Validator

Where implementation exists, runtime validation SHOULD compare:

```text
manifest declaration
vs
observed behavior
```

Including:

```text
accepted input types
returned output types
side effects
dependency usage
failure behavior
latency assumptions where relevant
rollback behavior
provider identity
```

A mismatch becomes evidence against the manifest claim.

---

# 61. Falsifiers

A manifest capability claim is falsified when reliable evidence demonstrates that:

```text
the provider does not expose the capability;
the declared interface is materially wrong;
the provider cannot accept declared valid inputs;
the provider cannot produce declared outputs;
the capability violates declared scope;
the capability violates declared regime restrictions;
actual side effects exceed declared effects;
required dependencies are missing;
validation evidence cannot be reproduced;
provider identity is wrong;
version lineage is wrong;
authority can be bypassed contrary to contract;
revocation is ineffective;
quarantine is ineffective;
provenance cannot be reconstructed.
```

Falsification SHOULD remain claim-local unless broader evidence supports systemic invalidation.

---

# 62. Manifest Query Surface

The registry SHOULD support conceptual queries such as:

```text
find capability by ID
find capability by alias
find capabilities by class
find providers for capability
find capabilities by Skill
find capabilities by agent
find capabilities by workflow
find capabilities by effect class
find capabilities by control plane
find capabilities by validation state
find capabilities with unresolved gaps
find stale capabilities
find revoked capabilities
find quarantined capabilities
find dependency descendants
find supersession lineage
```

Queryability is part of addressability.

It is not validation.

---

# 63. Capability Discovery Response

Recommended response:

```yaml
capability_discovery:
  query: {}

  candidates: []

  unresolved:
    - requirement: null
      reason: null

  excluded:
    - capability_id: null
      reason: null

  epistemic_class: DERIVED
```

Discovery MUST preserve exclusions when they materially explain why a seemingly relevant capability was not selected.

---

# 64. Capability Promotion

Recommended promotion path:

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

Promotion gates MUST be explicit.

---

# 65. Promotion Requirements

## PLACEHOLDER → DECLARED

Requires:

```text
identity
purpose
provider hypothesis
basic capability class
```

## DECLARED → STRUCTURALLY_COMPLETE

Requires:

```text
input/output contract
scope
regime
dependencies
effects
authority requirements
failure contract
provenance
```

## STRUCTURALLY_COMPLETE → ADDRESSABLE

Requires:

```text
registry admission
unique identity
schema validation
```

## ADDRESSABLE → IMPLEMENTED

Requires:

```text
resolvable implementation evidence
```

## IMPLEMENTED → TESTED

Requires:

```text
executed test evidence
```

## TESTED → VALIDATED

Requires:

```text
scope-specific validation
```

## VALIDATED → GOVERNED_ACTIVE

Requires:

```text
policy compatibility
control-plane compatibility
authority model
freshness
no unresolved critical gaps
```

---

# 66. No Automatic Promotion

The following transitions are prohibited:

```text
PLACEHOLDER → VALIDATED

DECLARED → GOVERNED_ACTIVE

ADDRESSABLE → VALIDATED

IMPLEMENTED → GOVERNED_ACTIVE
```

without intermediate evidence satisfying the missing gates.

---

# 67. Gap Classification

Manifest gaps SHOULD be typed:

```text
CRITICAL
DECISION_RELEVANT
EXPLANATORY
COSMETIC
```

Example:

```yaml
gap:
  gap_id: string
  capability_id: string

  class: CRITICAL

  field: "authority.commit"

  description: string

  blocks:
    - GOVERNED_ACTIVE

  resolution_requirement: string
```

---

# 68. Critical Gaps

Critical gaps SHOULD block promotion where they affect:

```text
identity
provider resolution
authority
security
effect class
critical dependency
provenance
commit semantics
irreversible action
```

A critical gap cannot be waived merely for completeness.

---

# 69. Manifest Gap Matrix

| Manifest Surface              |                      Required | Specification State |
| ----------------------------- | ----------------------------: | ------------------- |
| Manifest identity             |                           Yes | Defined             |
| Capability identity           |                           Yes | Defined             |
| Provider model                |                           Yes | Defined             |
| Capability classes            |                           Yes | Defined             |
| Input schema                  |                           Yes | Defined             |
| Output schema                 |                           Yes | Defined             |
| Lifecycle state               |                           Yes | Defined             |
| Dependency model              |                           Yes | Defined             |
| H/M/L                         |                           Yes | Defined             |
| Scope                         |                           Yes | Defined             |
| Regime                        |                           Yes | Defined             |
| Effects                       |                           Yes | Defined             |
| Authority boundary            |                           Yes | Defined             |
| Policy binding                |                           Yes | Defined             |
| Control-plane binding         |                           Yes | Defined             |
| Agent binding                 |                           Yes | Defined             |
| Skill binding                 |                           Yes | Defined             |
| Workflow binding              |                           Yes | Defined             |
| Protocol binding              |                           Yes | Defined             |
| Validation                    |                           Yes | Defined             |
| Evidence                      |                           Yes | Defined             |
| Provenance                    |                           Yes | Defined             |
| Freshness                     |                           Yes | Defined             |
| Supersession                  |                           Yes | Defined             |
| Uncertainty                   |                           Yes | Defined             |
| Failure modes                 |                           Yes | Defined             |
| Repair                        |                           Yes | Defined             |
| Tests                         |                           Yes | Defined             |
| Falsifiers                    |                           Yes | Defined             |
| Runtime capability population |        Required for operation | UNKNOWN/GAP         |
| Provider-specific evidence    |       Required for validation | UNKNOWN/GAP         |
| Executed validation suite     |       Required for validation | UNKNOWN/GAP         |
| Canon approval                | Required for canonical status | UNKNOWN/GAP         |

---

# 70. RSCF Binding

Capability manifest entries SHOULD support an RSCF projection.

```yaml
rscf:
  claim:
    id: "RSCF_CAP_MANIFEST_*"
    class: MODEL
    text: >
      Provider P declares capability C under scope S,
      regime R, dependency set D, and governance envelope G.

  premises:
    - manifest_identity_valid
    - capability_identity_valid
    - provider_identity_valid
    - interface_structurally_valid

  evidence: []

  provenance: []

  scope: null

  regime: null

  freshness: null

  dependencies: []

  competing: []

  falsifiers: []

  confidence_ceiling: 0
```

---

# 71. Capability Evidence Promotion

RSCF class SHOULD strengthen only as evidence strengthens.

Example:

```text
manifest declaration
    →
SOURCE_CLAIM / MODEL

static implementation inspection
    →
DERIVED

executed test
    →
DERIVED with runtime evidence

independent scoped validation
    →
potential VERIFIED claim within tested envelope
```

No artifact should be labeled `VERIFIED` merely because its manifest entry is structurally complete.

---

# 72. GMEF Binding

Capability changes SHOULD enter governed evolution when they modify:

```text
semantic behavior
input access
output semantics
side-effect class
authority requirements
memory access
network access
policy dependency
control-plane dependency
security boundary
rollback semantics
validation requirements
provider substitution
```

Manifest diff alone is not sufficient evidence that a change is safe.

---

# 73. Manifest Change Record

Recommended change object:

```yaml
manifest_change:
  change_id: string

  capability_id: string

  from_version: string
  to_version: string

  change_class:
    - PATCH
    - MINOR
    - MAJOR

  semantic_change: null
  authority_change: null
  effect_change: null
  dependency_change: null
  security_change: null

  evidence_refs: []

  validation_required: true

  rollback_plan: null
```

---

# 74. Commit Boundary

The capability manifest may inform commit governance.

It MUST NOT execute commit merely because:

```text
capability exists;
provider is available;
capability is validated;
provider succeeded;
proposal passed schema validation.
```

Commit still requires the relevant:

```text
authority
policy
constraint
freshness
target-state
transaction
```

checks.

---

# 75. Manifest / Control-Plane Separation

The manifest answers:

```text
"What capability records exist?"
```

The control plane answers:

```text
"May this capability be used here, now, by this principal,
against this resource, for this effect?"
```

This separation is mandatory.

---

# 76. Manifest / Policy Separation

The manifest may say:

```yaml
policy_refs:
  - POLICY_MEMORY_WRITE
```

The policy registry defines what that policy means.

The capability manifest MUST NOT silently redefine referenced policy semantics.

---

# 77. Manifest / Agent Separation

An agent may query the manifest.

An agent may propose a capability.

An agent may execute a capability when permitted.

But:

```text
agent preference
!=
capability validity

agent selection
!=
authority

agent confidence
!=
validation
```

---

# 78. Manifest / Skill Separation

A Skill may declare capability exposure.

The manifest provides the system-level representation.

A Skill MUST NOT be treated as universally safe merely because its capability appears in the manifest.

---

# 79. Manifest / Memory Separation

Capability metadata MAY be persisted.

Persistent memory about capability behavior MUST preserve:

```text
source
provider version
environment
time
scope
validation state
```

Historical success MUST NOT silently become permanent capability truth.

---

# 80. Manifest / Provenance Separation

The manifest references provenance.

It is not itself the complete provenance ledger.

The provenance layer SHOULD retain detailed evidence ancestry beyond what the manifest needs for efficient capability resolution.

---

# 81. Caching

Capability resolution MAY be cached.

Cache entries SHOULD include:

```yaml
cache:
  capability_id: string
  provider_id: string
  version: string

  resolved_at: timestamp
  expires_at: timestamp

  policy_version: null
  dependency_versions: {}
  validation_epoch: null
```

Cached resolution MUST be invalidated when load-bearing state changes.

---

# 82. Cache Invalidation Events

Examples:

```text
provider update
capability revocation
policy change
authority change
dependency change
schema change
validation failure
security incident
regime transition
supersession
```

---

# 83. Manifest Security Requirements

Capability metadata itself can become a security boundary.

The system SHOULD protect against:

```text
malicious capability registration;
provider impersonation;
alias hijacking;
effect-class understatement;
authority metadata injection;
validation forgery;
provenance stripping;
revocation rollback;
registry rollback;
stale-cache resurrection.
```

---

# 84. Registration Authority

Not every provider SHOULD necessarily be allowed to register itself as active.

Registration authority MAY distinguish:

```text
PROPOSE_ENTRY
REGISTER_ENTRY
VALIDATE_ENTRY
ACTIVATE_ENTRY
REVOKE_ENTRY
```

A provider SHOULD NOT automatically possess all five.

---

# 85. Two-Phase Admission

For higher-consequence capabilities, admission SHOULD conceptually separate:

```text
PHASE 1 — PROPOSE

PHASE 2 — VALIDATE / ADMIT
```

Thus:

```text
PROPOSED_ENTRY != ACTIVE_ENTRY
```

---

# 86. Manifest Observability

Material manifest operations SHOULD produce events:

```text
CAPABILITY_REGISTERED
CAPABILITY_UPDATED
CAPABILITY_VALIDATED
CAPABILITY_INVALIDATED
CAPABILITY_QUARANTINED
CAPABILITY_RESTORED
CAPABILITY_REVOKED
CAPABILITY_SUPERSEDED
PROVIDER_CHANGED
DEPENDENCY_CHANGED
```

Events SHOULD preserve actor, timestamp, affected identity, and reason where available.

---

# 87. Audit Questions

A manifest audit SHOULD be able to answer:

1. Which capabilities exist?
2. Which are placeholders?
3. Which have implementations?
4. Which have executed evidence?
5. Which are validated?
6. Under what scope?
7. Under what regime?
8. Which are stale?
9. Which are revoked?
10. Which are quarantined?
11. Who provides them?
12. What do they depend on?
13. Which policies govern them?
14. Which control planes govern them?
15. Which can create persistent effects?
16. Which can communicate externally?
17. Which require commit authority?
18. Which have unresolved critical gaps?
19. Which entries share evidence ancestry?
20. Which capabilities have supersession conflicts?

---

# 88. Minimum Active Entry

A capability SHOULD NOT become `GOVERNED_ACTIVE` without at least:

```yaml
minimum_active_entry:
  capability_id: required
  version: required

  provider_id: required
  provider_version: required

  inputs: required
  outputs: required

  scope: required
  regime: required

  dependencies: required

  effects:
    maximum_effect_class: required

  authority:
    invocation_required: required
    commit_authority_required: required

  governance:
    policy_refs: required
    control_plane_refs: required

  provenance:
    source_refs: required

  validation:
    state: required

  freshness:
    checked_at: required
```

---

# 89. Example Read-Only Capability

```yaml
capability:
  identity:
    capability_id: "CAP_EXAMPLE_READ"
    canonical_name: "Example Read Capability"
    version: "1.0.0"

  provider:
    provider_id: "PROVIDER_EXAMPLE"
    provider_type: TOOL
    provider_version: "1.0.0"

  classification:
    capability_classes:
      - RETRIEVAL

    epistemic_class: MODEL

  lifecycle:
    declaration_state: STRUCTURALLY_COMPLETE
    implementation_state: UNKNOWN
    availability_state: UNKNOWN
    validation_state: UNVALIDATED
    governance_state: UNREVIEWED
    revocation_state: ACTIVE

  inputs:
    - name: query
      type: string
      required: true
      provenance_required: false

  outputs:
    - name: results
      type: array
      epistemic_class: OBSERVATION
      provenance_required: true

  dependencies: []

  scope:
    domains: []
    environments: []
    exclusions: []

  regime:
    allowed: []
    prohibited: []

  hml:
    H: false
    M: true
    L: true

  effects:
    maximum_effect_class: E0_READ_ONLY
    possible_effects: []

  authority:
    invocation_required: true
    effect_authority_required: false
    commit_authority_required: false

  governance:
    policy_refs: []
    control_plane_refs: []

  validation:
    level: V0_DECLARED
    evidence_refs: []

  provenance:
    source_refs: []
    ancestry: []
    independence_status: UNKNOWN

  uncertainty:
    evidence: 1.0
    model: 1.0
    scope: 1.0
    temporal: 1.0
    causal: 1.0
    execution: 1.0
    provenance_independence: 1.0

  confidence_ceiling: 0

  gaps:
    - implementation evidence
    - runtime validation
```

This example is intentionally unvalidated.

---

# 90. Example Persistent-Write Capability

```yaml
capability:
  identity:
    capability_id: "CAP_EXAMPLE_WRITE"
    canonical_name: "Example Persistent Write"
    version: "1.0.0"

  provider:
    provider_id: "PROVIDER_EXAMPLE"
    provider_type: TOOL

  classification:
    capability_classes:
      - EXECUTION

  lifecycle:
    declaration_state: STRUCTURALLY_COMPLETE
    implementation_state: UNKNOWN
    availability_state: UNKNOWN
    validation_state: UNVALIDATED
    governance_state: UNREVIEWED
    revocation_state: ACTIVE

  inputs:
    - name: target
      type: resource_identifier
      required: true

    - name: payload
      type: object
      required: true

  outputs:
    - name: proposal
      type: effect_proposal
      epistemic_class: PROPOSAL

  effects:
    maximum_effect_class: E3_PERSISTENT_WRITE

    possible_effects:
      - persistent_write

    rollback:
      supported: UNKNOWN

  authority:
    invocation_required: true
    effect_authority_required: true
    commit_authority_required: true

  governance:
    policy_refs:
      - POLICY_PERSISTENT_WRITE

    control_plane_refs:
      - CONTROL_PLANE_AUTHORITY
      - CONTROL_PLANE_COMMIT
      - CONTROL_PLANE_PROVENANCE

  validation:
    level: V0_DECLARED

  confidence_ceiling: 0

  gaps:
    - implementation
    - validation
    - rollback verification
```

Again:

```text
manifest declaration != operational permission
```

---

# 91. RSCF Completion State

```yaml
claim_class: MODEL

claim:
  text: >
    CAPABILITY_MANIFEST.md defines the proposed governed inventory
    and registry semantics for AMOS capability declarations.

evidence:
  - structural derivation from AMOS capability/control-plane requirements

provenance:
  origin_architect: "Trang Phan"
  artifact: "CAPABILITY_MANIFEST.md"
  derivation_class: "AMOS MODEL synthesis"

scope:
  system: "AMOS OS"
  layer: "Capability registry / infrastructure"
  function:
    - capability inventory
    - discovery
    - resolution
    - lifecycle representation
    - governance binding

regime:
  - architecture
  - implementation
  - governed_runtime

freshness:
  reviewed_at: "2026-08-26"

  invalidation_triggers:
    - capability contract supersession
    - registry architecture change
    - authority architecture change
    - control-plane architecture change
    - canon supersession

dependencies:
  - CAPABILITY_CONTRACT.md
  - POLICY_REGISTRY.md
  - CONTROL_PLANE_MAP.md
  - provenance architecture
  - authority architecture

competing:
  - >
    Runtime implementation may require a smaller physical manifest
    with this document serving as the normative logical schema.

  - >
    Individual domain runtimes may require stricter capability
    metadata than this base manifest.

falsifiers:
  - >
    Source canon establishes incompatible capability-manifest semantics.

  - >
    Runtime requirements demonstrate that a proposed mandatory field
    violates an existing canonical AMOS invariant.

  - >
    Governance review rejects a proposed manifest invariant.

confidence_ceiling:
  structural_model: 0.90
  canonical_status: 0.00
  implementation_status: 0.00
  executed_validation: 0.00
```

---

# 92. Current Completion State

```yaml
completion:
  definition: COMPLETE_AS_MODEL
  manifest_schema: COMPLETE_AS_MODEL
  provider_model: COMPLETE_AS_MODEL
  lifecycle_model: COMPLETE_AS_MODEL
  dependency_model: COMPLETE_AS_MODEL
  governance_boundary: COMPLETE_AS_MODEL
  provenance_model: COMPLETE_AS_MODEL
  validation_model: COMPLETE_AS_MODEL
  failure_model: COMPLETE_AS_MODEL
  repair_model: COMPLETE_AS_MODEL
  test_surface: COMPLETE_AS_MODEL

  runtime_population: UNKNOWN/GAP
  implementation: UNKNOWN/GAP
  executed_tests: UNKNOWN/GAP
  empirical_validation: UNKNOWN/GAP
  canon_approval: UNKNOWN/GAP
```

---

# 93. Hard Boundary Block

```text
MANIFEST != RUNTIME

MANIFEST_ENTRY != IMPLEMENTATION

PLACEHOLDER != IMPLEMENTED

DECLARED != IMPLEMENTED

ADDRESSABLE != AVAILABLE

AVAILABLE != VALIDATED

CAPABILITY != AUTHORITY

CAPABILITY != PERMISSION

DISCOVERABLE != AUTHORIZED

COMPATIBLE != AUTHORIZED

SELECTED != AUTHORIZED

PROPOSAL != COMMIT

EXECUTION_SUCCESS != CLAIM_TRUTH

VALIDATION != UNIVERSAL_VALIDITY

UNKNOWN/GAP != PASS

CORRELATED_EVIDENCE != INDEPENDENT_CONFIRMATION

MODEL != EMPIRICAL_FACT
```

---

# 94. Canon Boundary

Trang Phan remains the origin architect / steward of AMOS.

This artifact is a substantive AMOS architecture proposal derived to complete the capability-manifest surface.

Its structural completeness MUST NOT be confused with canonical admission.

Until separately admitted through the appropriate canon/provenance/supersession process:

```text
artifact_status:
    PROPOSED

epistemic_class:
    MODEL

canonical_status:
    UNKNOWN/GAP

runtime_status:
    UNKNOWN/GAP

validation_status:
    UNKNOWN/GAP
```

Where verified source canon conflicts with generated manifest structure:

```text
applicable SOURCE CANON
        >
generated MODEL
```

subject to version, scope, and supersession resolution.

---

# 95. Final Manifest Law

The AMOS Capability Manifest SHALL preserve the following rule:

> The manifest describes what capabilities are declared and how they are governed as addressable system objects. It does not grant permission, prove implementation, prove correctness, or authorize durable effects.

Therefore:

```text
DECLARATION
    ↓
MANIFEST ENTRY
    ↓
STRUCTURAL VALIDATION
    ↓
REGISTRATION
    ↓
DISCOVERY
    ↓
RESOLUTION
    ↓
DEPENDENCY / SCOPE / REGIME CHECK
    ↓
PROVIDER VALIDATION
    ↓
AUTHORITY CHECK
    ↓
INVOCATION
    ↓
RESULT VALIDATION
    ↓
EFFECT PROPOSAL
    ↓
COMMIT-TIME REVALIDATION
    ↓
AUTHORIZED COMMIT
    ↓
PROVENANCE-PRESERVED EFFECT
```

No earlier state in this chain implies a later state.

Any unresolved load-bearing requirement remains:

```text
UNKNOWN/GAP
```

until evidence, authority, or governance resolves it.

---

# END — CAPABILITY_MANIFEST.md

```
```

---

[[00_ROOT_MOC]]|[[AMOS MOC]]

---
**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: capability_manifest
node_type: note
path: 03_CONTROL_PLANE/02_CAPABILITY/CAPABILITY_MANIFEST.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[02_CAPABILITY_MOC]]
