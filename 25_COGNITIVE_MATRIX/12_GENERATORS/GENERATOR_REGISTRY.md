---
title: GENERATOR REGISTRY
type: note
source: 25_COGNITIVE_MATRIX/12_GENERATORS
rscf:
  state: SOURCE_CLAIM
  class: STRUCTURAL
  provenance:
  - internal
  freshness: EVERGREEN
  falsifiers: []
tags:
- note
- 12-generators
- readme
- generators-map
- generator-output
- generator-falsification
- generator-promotion
- task-contract
- task-resolver
- capability-resolver
- mode-admission-queue
- mode-composition-registry
- mode-conflict-registry
- mode-coverage-matrix
- mode-dependency-graph
canon-group: canon/cognitive-matrix
---

---title: "GENERATOR REGISTRY"
type: document
tags: [note]
---


# Generator Registry

**STATUS:** CANDIDATE_CANON — SUBSTANTIVE SPECIFICATION
**Artifact Type:** Generator Registry Contract / Generator Identity Authority
**System:** AMOS OS
**Path:** `25_COGNITIVE_MATRIX/12_GENERATORS/GENERATOR_REGISTRY.md`
**Lineage Compatibility:** AMOS_CORE v3.0 → v4.4
**Origin Architect / Steward:** Trang Phan
**Claim Class:** `AMOS_MODEL`
**Implementation Status:** NOT ESTABLISHED BY THIS DOCUMENT
**Population Status:** NOT ESTABLISHED BY THIS DOCUMENT
**Empirical Validation Status:** NOT ESTABLISHED BY THIS DOCUMENT
**Final Canon Status:** NOT ESTABLISHED BY THIS DOCUMENT

---

# 0. Registry Declaration

The Generator Registry is the governed AMOS OS index of recognized generator identities, versions, contracts, capabilities, dependencies, lifecycle states, provenance, validation state, promotion state, compatibility envelopes, constraints, and resolution metadata.

It answers:

> **What generators does AMOS know about, exactly which versions are recognized, what are they permitted to claim or produce, under what conditions may they be considered, and what evidence supports their current status?**

The registry is not merely a list of generator names.

It is a typed control surface between:

```text
GENERATOR IDENTITY
        │
        ▼
VERSION / LINEAGE
        │
        ▼
CONTRACT
        │
        ▼
CAPABILITIES
        │
        ▼
DEPENDENCIES
        │
        ▼
VALIDATION
        │
        ▼
PROMOTION STATE
        │
        ▼
MODE / TASK ADMISSIBILITY
        │
        ▼
RESOLUTION
        │
        ▼
GENERATION
```

The governing distinction is:

$$\boxed{ Registered \neq Validated \neq Promoted \neq Selected \neq Executed \neq Canonical }$$

No registry entry acquires stronger epistemic or operational status merely by existing in the registry.

---

# 1. Purpose

The Generator Registry exists to provide a deterministic, provenance-aware and inspectable generator namespace for AMOS.

Its responsibilities include:

1. uniquely identifying generators;
2. distinguishing generator families from versions;
3. preserving generator lineage;
4. binding generators to contracts;
5. recording generator capabilities;
6. recording task compatibility;
7. recording mode compatibility;
8. representing dependencies;
9. representing conflicts;
10. representing compositions;
11. preserving provenance;
12. preserving validation state;
13. preserving falsification state;
14. preserving promotion state;
15. preserving supersession;
16. representing scope and regime;
17. representing freshness;
18. exposing resolution metadata;
19. preventing ambiguous generator selection;
20. preventing stale or invalidated generators from silently resolving;
21. preserving historical generator identities;
22. supporting targeted invalidation and rollback.

---

# 2. Registry Non-Goals

The registry does **not** itself prove:

```text
generator correctness
generator quality
generator safety
generator effectiveness
generator implementation
generator availability
generator execution authority
generator empirical validity
generator canonical status
```

The registry stores and exposes relevant state.

It does not manufacture that state.

Therefore:

$$Entry(G) \not\Rightarrow Valid(G)$$

and:

$$Entry(G) \not\Rightarrow Executable(G)$$

---

# 3. Core Registry Law

For generator $G$:

$$Registry(G) = Identity + Version + Lineage + Contract + Capability + Dependency + Scope + Regime + Provenance + Validation + Promotion + Lifecycle + ResolutionMetadata$$

subject to applicable constraints.

A registry record is valid only to the extent that its load-bearing fields are valid.

---

# 4. Registry Identity Law

Every generator MUST have a stable generator identifier.

Example:

```yaml
generator_id: generator.counterfactual.core
```

A generator identifier SHOULD NOT encode mutable properties that would cause identity drift.

Good:

```text
generator.counterfactual.core
```

Potentially unstable:

```text
best_counterfactual_generator_2026
```

Identity must survive ordinary version evolution.

---

# 5. Generator Family vs Generator Version

AMOS distinguishes:

```text
GENERATOR FAMILY
        │
        ├── VERSION 1
        ├── VERSION 2
        └── VERSION 3
```

Formally:

$$Family(G) \neq Version(G)$$

Example:

```yaml
generator_family: counterfactual
generator_id: generator.counterfactual.core
version: 4.4.0
```

A new version does not require a new conceptual family unless the identity boundary itself changes.

---

# 6. Registry Key

A fully qualified generator registry key SHOULD conceptually bind:

$$K_G = (generator\_id,\ version)$$

and MAY additionally bind an immutable artifact digest:

$$K_G^* = (generator\_id,\ version,\ hash)$$

Example:

```yaml
registry_key:
  generator_id: generator.counterfactual.core
  version: 4.4.0
  artifact_hash: null
```

When a hash is unavailable:

```text
HASH_STATUS = UNKNOWN
```

not fabricated.

---

# 7. Identity Envelope

A generator entry SHOULD support:

```yaml
identity:
  generator_id: null
  generator_family: null
  display_name: null

  version: null
  version_hash: null

  artifact_type: GENERATOR

  origin:
    architect: null
    steward: null
    source_artifact: null

  namespace: null

  aliases: []
```

Aliases MUST NOT create independent generator identities.

---

# 8. Alias Law

If:

```text
A
B
C
```

are aliases of the same generator:

$$A \equiv B \equiv C$$

for identity resolution.

Aliases MUST NOT be counted as multiple generators during:

```text
coverage analysis
competition analysis
provenance analysis
capability counting
validation counting
```

---

# 9. Registry Entry Classes

Entries MAY represent:

```text
GENERATOR
GENERATOR_VERSION
GENERATOR_PROFILE
GENERATOR_CONFIGURATION
GENERATOR_COMPOSITION
GENERATOR_ADAPTER
GENERATOR_WRAPPER
GENERATOR_ALIAS
```

The entry class MUST be explicit.

A wrapper around a generator is not automatically identical to the underlying generator.

---

# 10. Lifecycle State

Each generator SHOULD expose a lifecycle state.

Recommended conceptual states:

```text
UNREGISTERED
REGISTERED
EXPERIMENTAL
CANDIDATE
VALIDATION_PENDING
VALIDATED
PROMOTION_CANDIDATE
ADMITTED
ACTIVE
CANON_ELIGIBLE
SUSPENDED
QUARANTINED
DEPRECATED
SUPERSEDED
REJECTED
INVALIDATED
RETIRED
```

The registry MUST distinguish lifecycle state from epistemic claim class.

---

# 11. Registry State Machine

Conceptually:

```text
UNREGISTERED
     │
     ▼
REGISTERED
     │
     ▼
EXPERIMENTAL
     │
     ▼
CANDIDATE
     │
     ▼
VALIDATED
     │
     ▼
ADMITTED
     │
     ▼
ACTIVE
```

Side transitions include:

```text
ANY STATE ──► SUSPENDED
ANY STATE ──► QUARANTINED
ANY STATE ──► INVALIDATED

ACTIVE ─────► DEPRECATED
ACTIVE ─────► SUPERSEDED
DEPRECATED ─► RETIRED
```

Transitions require the applicable governance process.

---

# 12. Registration

Registration means:

> AMOS recognizes this generator identity.

Registration SHOULD require at minimum:

```text
generator_id
generator_family
version
declared purpose
source/provenance reference
contract reference or contract status
lifecycle state
```

Registration alone establishes no performance claim.

---

# 13. Registry Admission

An entry SHOULD NOT become operationally admissible merely because it is registered.

Operational admission may depend on:

$$Admissible(G,T,M,E)$$

where:

* $G$ = generator;
* $T$ = task;
* $M$ = mode;
* $E$ = environment/regime.

Conceptually:

$$Admissible = Registered \land VersionValid \land ContractCompatible \land CapabilitySufficient \land DependencyValid \land ScopeCompatible \land RegimeCompatible \land NotInvalidated$$

plus task-specific governance.

---

# 14. Generator Contract Binding

Every operational generator SHOULD bind to an applicable Generator Contract.

Example:

```yaml
contract:
  contract_ref: "12_GENERATORS_CONTRACT"
  contract_version: null
  compliance_state: UNKNOWN
```

Possible compliance states:

```text
UNKNOWN
UNASSESSED
PARTIAL
COMPLIANT
NONCOMPLIANT
INVALIDATED
```

`UNKNOWN` and `UNASSESSED` MUST NOT be silently converted to `COMPLIANT`.

---

# 15. Output Contract Binding

A registry entry SHOULD identify its applicable output contract.

Example:

```yaml
output_contract:
  ref: ""
  output_schema: null
  compliance_state: UNKNOWN
```

The registry SHOULD expose whether generated outputs preserve required:

```text
claim class
provenance
scope
regime
freshness
dependencies
uncertainty
falsifiers
```

---

# 16. Generator Purpose

Each generator SHOULD declare its intended purpose.

Example:

```yaml
purpose:
  primary: "Construct bounded counterfactual alternatives."
  secondary: []
  exclusions: []
```

Purpose is descriptive.

It does not itself authorize use.

---

# 17. Capability Declaration

A generator MAY declare capabilities.

Example:

```yaml
capabilities:
  provides:
    - counterfactual_generation
    - alternative_world_construction

  requires:
    - structured_reasoning
    - provenance_access

  optional:
    - external_evidence
```

Declared capability is:

```text
SOURCE_CLAIM
```

until independently established.

---

# 18. Capability State

Capability claims SHOULD have state.

Example:

```yaml
capability:
  capability_id: counterfactual_generation

  declared: true

  validation:
    status: UNKNOWN

  scope: {}

  provenance: []
```

Thus:

$$DeclaredCapability \neq ValidatedCapability$$

---

# 19. Task Compatibility

The registry SHOULD identify task classes for which a generator is:

```text
PREFERRED
COMPATIBLE
CONDITIONAL
EXPERIMENTAL
INCOMPATIBLE
UNKNOWN
```

Example:

```yaml
task_compatibility:
  - task_class: causal_counterfactual
    state: CONDITIONAL

  - task_class: text_summarization
    state: INCOMPATIBLE
```

---

# 20. Mode Compatibility

Generator admissibility MAY depend on AMOS mode.

Example:

```yaml
mode_compatibility:
  analysis: COMPATIBLE
  research: COMPATIBLE
  planning: CONDITIONAL
  execution: PROHIBITED
```

This SHOULD integrate with:

```text
MODE_ADMISSION_QUEUE
MODE_COMPOSITION_REGISTRY
MODE_CONFLICT_REGISTRY
MODE_COVERAGE_MATRIX
MODE_DEPENDENCY_GRAPH
```

---

# 21. Capability Resolver Integration

The Capability Resolver SHOULD be able to query the registry for:

```text
Which generators claim capability C?
Which versions provide C?
Which are validated?
Which are admissible in mode M?
Which satisfy task T?
Which remain fresh?
Which have valid dependencies?
```

Conceptually:

$$Candidates(C) = \{G \mid Provides(G,C)\}$$

followed by admissibility filtering.

---

# 22. Task Resolver Integration

The Task Resolver SHOULD NOT select a generator from name similarity alone.

Resolution SHOULD conceptually operate:

```text
TASK
 │
 ▼
REQUIRED CAPABILITIES
 │
 ▼
REGISTRY QUERY
 │
 ▼
CANDIDATE GENERATORS
 │
 ▼
CONSTRAINT FILTER
 │
 ▼
MODE FILTER
 │
 ▼
DEPENDENCY FILTER
 │
 ▼
VALIDATION FILTER
 │
 ▼
COMPETING CANDIDATES
 │
 ▼
SELECTION / COMPETING / GAP
```

---

# 23. Resolution Is Not Registry Mutation

Selecting generator $G$ for a task does not automatically modify $G$'s registry status.

$$Selected(G,T) \not\Rightarrow Promoted(G)$$

and:

$$SuccessfulRun(G,T) \not\Rightarrow Validated(G)$$

Evidence from execution MAY later enter an appropriate validation process.

---

# 24. Scope Envelope

Every material generator claim SHOULD inherit a scope.

Example:

```yaml
scope:
  domains: []
  task_classes: []
  populations: []
  environments: []
  scales: []
  languages: []
  data_types: []

  excluded: []
```

A generator validated under $S_1$ is not automatically validated under $S_2$.

---

# 25. Regime Envelope

A generator SHOULD identify regime dependencies.

Example:

```yaml
regime:
  model_family: null
  runtime: null
  software_version: null
  policy_version: null
  environment: null
  measurement_method: null
```

Material regime changes may invalidate prior generator conclusions.

---

# 26. Freshness

Registry entries SHOULD carry temporal state.

```yaml
freshness:
  registered_at: null
  updated_at: null
  validated_at: null
  evidence_as_of: null
  revalidation_due: null
  expiry_conditions: []
```

A registry record can remain historically valid while its operational evidence becomes stale.

---

# 27. Provenance

Every generator SHOULD preserve provenance sufficient to reconstruct its origin and lifecycle.

Example:

```yaml
provenance:
  source_artifacts: []
  source_versions: []
  source_hashes: []
  derived_from: []
  authorship: []
  steward: null
  evidence_refs: []
```

Missing provenance MUST remain visible.

---

# 28. Provenance Topology

The registry SHOULD represent ancestry rather than only flat source lists.

Conceptually:

```text
SOURCE A
   │
   ├──► GENERATOR G1
   │
   └──► GENERATOR G2

SOURCE B ──► GENERATOR G3
```

This matters when comparing apparently independent generators.

---

# 29. Sybil Hardening

If:

```text
G1
G2
G3
```

all descend from the same underlying generator or evidence base, the registry SHOULD preserve that ancestry.

Three registry entries do not necessarily imply three independent generators.

$$EntryCount \neq IndependentGeneratorCount$$

---

# 30. Dependency Declaration

Generators SHOULD declare dependencies.

Example:

```yaml
dependencies:
  hard:
    - generator_id: null
      version_constraint: null

  soft: []

  informational: []

  governance: []
```

Dependencies SHOULD be typed.

---

# 31. Dependency Types

Useful dependency classes include:

```text
HARD
SOFT
OPTIONAL
INFORMATIONAL
CAPABILITY
MODE
DATA
MODEL
POLICY
GOVERNANCE
GENERATOR
```

A hard dependency failure can invalidate generator admissibility.

---

# 32. Dependency Graph

The registry SHOULD support generator dependency topology.

```text
G1 ─────► G3
          ▲
          │
G2 ───────┘
```

For generator $G$:

$$D(G) = D_{direct}(G) \cup D_{material-transitive}(G)$$

Only material dependency closure needs to be traversed for a given decision.

---

# 33. Dependency Cycles

Generator cycles MUST be detectable.

Example:

```text
G1 → G2 → G3 → G1
```

A cycle is not automatically invalid, but it requires explicit semantics.

Unresolved circular dependency that prevents admissibility determination SHOULD produce:

```text
UNKNOWN/GAP
```

or block resolution.

---

# 34. Conflict Registry

Generator conflicts SHOULD be explicit.

Example:

```yaml
conflicts:
  - generator_id: generator.example
    class: MUTUALLY_EXCLUSIVE
    reason: null
```

Possible conflict classes:

```text
MUTUALLY_EXCLUSIVE
OUTPUT_CONTRACT_CONFLICT
MODE_CONFLICT
CAPABILITY_CONFLICT
DEPENDENCY_CONFLICT
POLICY_CONFLICT
REGIME_CONFLICT
UNKNOWN
```

---

# 35. Composition

The registry MAY represent generator compositions.

Example:

```yaml
composition:
  composition_id: generator.composition.example

  members:
    - G1
    - G2
    - G3

  orchestration: null

  validation_state: UNKNOWN
```

Composition identity is distinct from member identities.

---

# 36. Composition Law

$$Validated(G_1) \land Validated(G_2) \not\Rightarrow Validated(Compose(G_1,G_2))$$

because composition may introduce:

```text
feedback
ordering effects
information loss
conflict
emergent behavior
new dependencies
```

The registry MUST preserve composition-level validation separately.

---

# 37. Versioning

Generator versions SHOULD follow the applicable versioning contract.

Registry entries SHOULD support:

```yaml
versioning:
  current_version: null
  previous_versions: []
  compatible_with: []
  incompatible_with: []
  supersedes: []
  superseded_by: []
```

---

# 38. Version Mutation Law

An existing immutable version record SHOULD NOT be silently rewritten into a materially different generator.

If semantics materially change:

```text
CREATE NEW VERSION
```

rather than:

```text
MUTATE HISTORY
```

---

# 39. Supersession

Supersession MUST be explicit.

```text
G_v1
  │
  └── SUPERSEDED_BY ──► G_v2
```

The registry SHOULD preserve:

```yaml
supersession:
  supersedes: []
  superseded_by: []
  reason: null
  effective_at: null
```

Historical records remain recoverable.

---

# 40. Deprecation

Deprecated generators SHOULD remain discoverable for lineage and compatibility.

A deprecated entry SHOULD state:

```text
why deprecated
replacement
remaining valid scope
migration path
retirement condition
```

Deprecation does not equal deletion.

---

# 41. Retirement

A retired generator SHOULD not normally be selected by the resolver.

However:

```text
historical provenance
past decisions
supersession lineage
audit evidence
```

SHOULD remain accessible.

---

# 42. Validation Binding

The registry SHOULD link to generator validation artifacts.

Example:

```yaml
validation:
  status: UNKNOWN
  validation_refs: []
  validated_scope: []
  validated_regimes: []
  known_failures: []
```

Possible states:

```text
NOT_RUN
IN_PROGRESS
PASSED
PASSED_CONDITIONALLY
FAILED
STALE
INVALIDATED
UNKNOWN
```

---

# 43. Falsification Binding

Every consequential generator SHOULD expose falsification state.

```yaml
falsification:
  ref: ""

  status: NOT_RUN

  falsifiers: []
  challenges: []
  failures: []
  unresolved: []
```

Failure to find a falsifier does not prove universal validity.

---

# 44. Promotion Binding

The registry SHOULD bind to the generator promotion process.

Example:

```yaml
promotion:
  ref: ""

  current_level: REGISTERED
  requested_level: null

  promotion_record_refs: []
```

Promotion state MUST NOT be inferred from registry age or use frequency.

---

# 45. Epistemic Classification

Generator-related claims SHOULD preserve their class.

Relevant classes include:

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL
DECISION
UNKNOWN
```

Example:

```yaml
claim:
  proposition: "Generator G supports capability C."
  class: SOURCE_CLAIM
```

until validated.

---

# 46. Conclusion Classes

Registry-derived conclusions SHOULD use:

```text
VERIFIED
DERIVED
MODEL
CONDITIONAL
COMPETING
UNKNOWN/GAP
```

The weakest accurate class governs.

---

# 47. Confidence Ceiling

If generator admissibility depends on:

$$P_1,P_2,\ldots,P_n$$

then:

$$Confidence(Admissibility) \leq \min Confidence(P_i)$$

for load-bearing premises unless independently revalidated.

Registry metadata MUST NOT inflate confidence.

---

# 48. Generator Competition

Multiple generators MAY satisfy the same requested capability.

Example:

```text
CAPABILITY C
   │
   ├──► G1
   ├──► G2
   └──► G3
```

The registry SHOULD expose all materially viable candidates.

---

# 49. Competition State

Candidate generators MAY be:

```text
DOMINANT
PREFERRED
VIABLE
CONDITIONAL
COMPETING
INFERIOR_FOR_SCOPE
INADMISSIBLE
UNKNOWN
```

When evidence cannot discriminate:

```text
COMPETING
```

MUST be preserved.

---

# 50. No Forced Winner

If:

$$Support(G_1) \approx Support(G_2)$$

or the evidence is incomparable:

$$Select(G_1)$$

MUST NOT be manufactured merely to produce a single answer.

The resolver may return:

```yaml
resolution:
  status: COMPETING
  candidates:
    - G1
    - G2
```

---

# 51. Discriminating Tests

Where competition matters, the system SHOULD seek a high-information discriminating test.

$$T^* = \arg\max_T \frac{ExpectedDecisionInformation(T)} {Cost(T)}$$

subject to safety and governance constraints.

---

# 52. Generator Coverage

The registry SHOULD support coverage analysis.

For capability set:

$$C=\{c_1,c_2,\ldots,c_n\}$$

define:

$$Coverage(c_i) = \{G \mid Provides(G,c_i)\}$$

This enables detection of:

```text
NO COVERAGE
SINGLE-POINT COVERAGE
REDUNDANT COVERAGE
COMPETING COVERAGE
UNVALIDATED COVERAGE
```

---

# 53. Coverage Is Not Reliability

If five generators claim a capability:

$$|\ Coverage(C)\ |=5$$

this does not mean the capability has five independently reliable implementations.

Ancestry and validation must be considered.

---

# 54. Generator Selection Score

Implementations MAY use a resolution score, but scoring MUST NOT override hard integrity constraints.

Conceptually:

$$Score(G,T) = w_cC + w_vV + w_sS + w_rR + w_fF - w_kK$$

where dimensions MAY represent:

```text
capability fit
validation
scope fit
regime fit
freshness
cost/risk
```

But:

$$HardConstraintViolation(G) \Rightarrow Inadmissible(G)$$

regardless of score.

---

# 55. Deterministic Resolution

Given equivalent registry state, policy, scope, and task requirements, generator resolution SHOULD be deterministic where the governing rules fully order candidates.

If legitimate competing hypotheses remain, deterministic behavior means deterministic preservation of:

```text
COMPETING
```

rather than arbitrary tie-breaking.

---

# 56. Registry Query Contract

Conceptual query:

```yaml
generator_query:
  task: null

  required_capabilities: []
  optional_capabilities: []

  mode: null
  scope: {}
  regime: {}

  minimum_validation: null
  maximum_risk: null

  include_experimental: false
  include_deprecated: false
  include_invalidated: false
```

---

# 57. Registry Query Result

```yaml
generator_query_result:
  status: null

  candidates: []

  excluded:
    - generator: null
      reason: null

  competing: []

  gaps: []

  provenance: []

  freshness: null
```

---

# 58. Resolution Status

Possible query outcomes include:

```text
RESOLVED
RESOLVED_CONDITIONALLY
COMPETING
NO_CAPABILITY
NO_ADMISSIBLE_GENERATOR
BLOCKED
STALE
UNKNOWN/GAP
```

---

# 59. Resolver Failure Transparency

If no generator satisfies the requirements:

```text
NO_ADMISSIBLE_GENERATOR
```

is preferable to silently selecting an incompatible generator.

If generator state is unknown:

```text
UNKNOWN/GAP
```

is preferable to assuming compatibility.

---

# 60. Registry and RSCF

The Generator Registry SHOULD integrate with RSCF reasoning.

A generator-selection RSCF may contain:

```yaml
rscf:
  objective: "Resolve generator for task T"

  state:
    registry_snapshot: null

  constraints: []
  candidates: []
  dependencies: []
  competing: []
  evidence: []

  decision: null
```

---

# 61. RSCF Node Identity

This artifact is itself represented as an RSCF knowledge node:

```yaml
RSCF-NODE:
  node_id: generator_registry
  node_type: note
  path: 25_COGNITIVE_MATRIX/12_GENERATORS/GENERATOR_REGISTRY.md

  claim_class: AMOS_MODEL
```

---

# 62. RSCF Relations

```yaml
RSCF-RELATIONS:
  - INDEXED_BY: ""
  - INDEXED_BY: ""

  - PART_OF: ""
  - PART_OF: ""

  - GOVERNED_BY: "12_GENERATORS_CONTRACT"
  - VERSIONED_BY: "12_GENERATORS_VERSIONING"

  - VALIDATED_BY: ""
  - PROMOTED_BY: ""

  - PRODUCES_ACCORDING_TO: ""

  - QUERIED_BY: ""
  - QUERIED_BY: ""

  - INTERACTS_WITH: ""
  - INTERACTS_WITH: ""
  - INTERACTS_WITH: ""
  - INTERACTS_WITH: ""
  - INTERACTS_WITH: ""
```

These relations describe intended architecture unless separately verified as implemented.

---

# 63. H/M/L Representation

Registry retrieval SHOULD follow AMOS fractal knowledge principles.

```text
H — Registry Summary
    generator family
    current version
    lifecycle
    capabilities
    admissibility

M — Generator Subsystem
    contract
    dependencies
    validation
    promotion
    compatibility

L — Detailed Evidence
    tests
    provenance
    falsifiers
    version diffs
    dependency details

RAW
    original implementation
    raw evaluation evidence
    raw source artifacts
```

Raw evidence defaults to:

```text
DO_NOT_LOAD_UNLESS_REQUIRED
```

---

# 64. Smallest Sufficient Registry Query

A registry query SHOULD retrieve only fields capable of changing the decision.

For simple capability lookup:

```text
identity
capability
lifecycle
```

may suffice.

For consequential activation:

```text
identity
version
contract
capability
dependencies
validation
provenance
scope
regime
freshness
governance
```

may be required.

---

# 65. Fast-Path Resolution

Localized registry resolution is admissible only when:

$$DependencyClosure \land ProvenanceIndependence \land ScopeCompatibility \land RegimeCompatibility \land Freshness \land NonConflict$$

are sufficiently established for the decision.

Otherwise resolution escalates.

---

# 66. Mandatory Escalation

Registry resolution SHOULD escalate when:

```text
candidate provenance is correlated
versions conflict
dependencies are ambiguous
evidence is stale
scope changes
regime changes
generator composition is required
governance impact increases
irreversible effects are possible
```

---

# 67. Information Exposure

Registry queries MUST respect information exposure rules.

A generator's existence MAY be visible while some fields remain restricted.

Conceptually:

```yaml
exposure:
  identity: PUBLIC_WITHIN_SCOPE
  capabilities: PUBLIC_WITHIN_SCOPE
  implementation_details: RESTRICTED
  sensitive_dependencies: RESTRICTED
  raw_provenance: CONDITIONAL
```

The registry MUST NOT treat retrievability as disclosure authorization.

---

# 68. Binding

Generator selection SHOULD produce an explicit binding.

Example:

```yaml
generator_binding:
  task_id: null

  generator_id: null
  version: null

  capability: null

  scope: {}
  regime: {}

  registry_snapshot: null

  binding_status: PROVISIONAL
```

Binding is not execution.

---

# 69. Binding Stability

If the generator version or load-bearing registry state changes after binding but before consequential execution, the binding SHOULD be rechecked.

$$State_{bind} \neq State_{commit} \Rightarrow Revalidate$$

when the difference is material.

---

# 70. MVCC Pattern

A registry implementation MAY use MVCC-like semantics:

```text
READ REGISTRY @ R_n
        │
        ▼
RESOLVE GENERATOR
        │
        ▼
PREPARE BINDING
        │
        ▼
COMPARE CURRENT REGISTRY
        │
        ├── unchanged ─► COMMIT
        │
        └── changed ───► RECHECK
```

This is a conceptual consistency pattern, not a claim about literal implementation.

---

# 71. CAS Pattern

A generator transition MAY use compare-and-swap semantics:

$$CAS( expected\_state, new\_state )$$

If expected state no longer matches:

```text
TRANSITION_ABORTED
```

followed by targeted revalidation.

---

# 72. Atomic Multi-Generator Resolution

Some tasks require multiple generators as one reasoning unit.

Example:

$$G_A + G_B + G_C$$

If correctness depends on the complete set:

```text
partial resolution ≠ complete resolution
```

AMOS SHOULD validate the relevant composition atomically.

---

# 73. Causal Epoch

Registry decisions MAY be associated with a causal epoch.

Example:

```yaml
registry_snapshot:
  epoch: E42
```

A binding valid under $E_{42}$ does not automatically survive a material causal change in $E_{43}$.

---

# 74. Persistent Provenance

Historical registry state SHOULD remain reconstructable.

AMOS SHOULD be able to determine:

```text
which generator existed
which version was active
what contract applied
what dependencies existed
what validation existed
what scope was allowed
what promotion state applied
what superseded it
```

for a relevant historical decision.

---

# 75. Registry Mutation

Material mutation SHOULD be governed.

Mutation classes include:

```text
REGISTER
UPDATE_METADATA
ADD_VERSION
CHANGE_CAPABILITY
CHANGE_DEPENDENCY
CHANGE_SCOPE
CHANGE_REGIME
PROMOTE
DOWNGRADE
DEPRECATE
SUPERSEDE
QUARANTINE
INVALIDATE
RETIRE
```

Each mutation SHOULD preserve provenance.

---

# 76. No Silent Mutation

The registry MUST NOT silently change a load-bearing field such as:

```text
version
capability
dependency
validation
scope
regime
promotion state
```

without corresponding lifecycle/provenance treatment.

---

# 77. Invalidation

A generator may become invalid when:

```text
critical premise fails
contract violation is discovered
dependency becomes invalid
falsifier succeeds
provenance is corrupted
scope assumption fails
regime changes materially
```

Invalidation SHOULD be targeted.

---

# 78. Targeted Invalidation

If dependency $D$ fails:

$$Invalidate(D)$$

then only generator states dependent on $D$ should be reconsidered.

$$Invalidate(D) \Rightarrow Invalidate(Descendants(D))$$

not:

$$Invalidate(AllGenerators)$$

---

# 79. Quarantine

`QUARANTINED` indicates unresolved integrity risk.

A quarantined generator SHOULD NOT normally be selected.

Registry record:

```yaml
quarantine:
  active: true
  reason: null
  entered_at: null
  release_conditions: []
```

---

# 80. Registry Integrity Checks

The registry SHOULD detect:

```text
duplicate IDs
version collisions
dangling dependencies
unknown contract references
cycles
invalid supersession chains
multiple active versions where forbidden
stale validation
scope contradictions
mode conflicts
missing provenance
orphaned aliases
```

---

# 81. Duplicate Identity

If two artifacts claim:

```text
generator_id = G
version = V
```

but have materially different content:

```text
IDENTITY_COLLISION
```

must be raised.

AMOS MUST NOT arbitrarily merge them.

---

# 82. Version Collision

If:

$$Hash(G,V,A) \neq Hash(G,V,B)$$

for two artifacts claiming identical identity/version:

```text
VERSION_COLLISION
```

The entries remain competing/ambiguous until resolved through provenance.

---

# 83. Supersession Integrity

A valid supersession chain SHOULD be acyclic.

Invalid:

```text
G1 supersedes G2
G2 supersedes G1
```

unless a distinct explicitly modeled semantic relation explains it.

---

# 84. Provenance Independence

When comparing generators, the registry SHOULD expose provenance correlation.

Example:

```yaml
independence:
  G1_vs_G2:
    state: CORRELATED
    common_ancestor: A
```

This prevents false confidence from apparent redundancy.

---

# 85. Registry Proof Capsule

Important registry conclusions SHOULD conceptually produce a Proof Capsule.

```yaml
registry_proof_capsule:
  claim: null
  class: null

  generator_id: null
  version: null

  premises: []
  evidence: []
  provenance: []

  dependencies: []

  scope: {}
  regime: {}
  freshness: {}

  competing_generators: []
  falsifiers: []

  confidence_ceiling: null
  invalidation_conditions: []
```

---

# 86. Proof Capsule Reuse

A prior registry resolution may be reused only while:

```text
generator version unchanged
dependencies valid
scope compatible
regime compatible
freshness valid
policy compatible
no material contradiction
```

Otherwise targeted re-resolution is required.

---

# 87. Registry Snapshot

A consequential resolution SHOULD be capable of referencing a registry snapshot.

Example:

```yaml
registry_snapshot:
  snapshot_id: null
  timestamp: null
  epoch: null
  registry_version: null
```

This supports reproducibility and causal lineage.

---

# 88. Canonical Entry Shape

A maximum-detail generator record MAY use:

```yaml
generator_registry_entry:

  identity:
    generator_id: null
    generator_family: null
    display_name: null
    aliases: []

  artifact:
    type: GENERATOR
    path: null
    source_ref: null
    hash: null

  versioning:
    version: null
    previous_versions: []
    compatible_with: []
    incompatible_with: []
    supersedes: []
    superseded_by: []

  origin:
    architect: null
    steward: null
    created_at: null

  lifecycle:
    state: REGISTERED
    state_since: null
    history: []

  contract:
    generator_contract_ref: null
    output_contract_ref: null
    compliance_state: UNKNOWN

  purpose:
    primary: null
    secondary: []
    exclusions: []

  capabilities:
    declared: []
    validated: []
    conditional: []
    prohibited: []

  tasks:
    compatible: []
    conditional: []
    incompatible: []

  modes:
    compatible: []
    conditional: []
    prohibited: []

  dependencies:
    hard: []
    soft: []
    optional: []
    material_transitive: []
    closure_state: UNKNOWN

  conflicts: []

  compositions:
    member_of: []
    composition_validation: []

  scope:
    admitted: []
    excluded: []

  regime:
    admitted: []
    excluded: []

  freshness:
    registered_at: null
    updated_at: null
    evidence_as_of: null
    revalidation_due: null
    expiry_conditions: []

  provenance:
    sources: []
    ancestry: []
    evidence_refs: []
    independence_state: UNKNOWN

  validation:
    status: NOT_RUN
    refs: []
    failures: []
    validated_scope: []
    validated_regimes: []

  falsification:
    status: NOT_RUN
    refs: []
    successful_falsifiers: []
    unresolved: []

  promotion:
    level: REGISTERED
    refs: []

  risk:
    class: null
    reversibility: null

  governance:
    registration_authority: null
    promotion_authority: null
    execution_authority: null

  exposure:
    classification: null

  resolution:
    selectable: false
    priority: null
    conditions: []

  epistemic:
    claim_class: AMOS_MODEL
    confidence_ceiling: null

  invalidation:
    conditions: []
    invalidated_at: null
    invalidated_by: null

  proof_capsule_ref: null
```

---

# 89. Registry Collection Shape

The entire registry MAY conceptually be represented as:

```yaml
generator_registry:

  registry_version: null
  registry_hash: null
  generated_at: null

  entries: []

  aliases: {}

  families: {}

  capabilities_index: {}

  task_index: {}

  mode_index: {}

  dependency_graph: {}

  conflict_graph: {}

  composition_graph: {}

  supersession_graph: {}

  provenance_graph: {}

  validation_index: {}

  promotion_index: {}

  quarantined: []
  deprecated: []
  retired: []

  unresolved_collisions: []
  gaps: []
```

---

# 90. Derived Indexes

The registry MAY maintain derived indexes for efficiency.

Examples:

```text
CAPABILITY → GENERATORS
TASK → GENERATORS
MODE → GENERATORS
GENERATOR → DEPENDENCIES
GENERATOR → CONFLICTS
GENERATOR → VERSIONS
GENERATOR → PROVENANCE
```

Derived indexes MUST remain subordinate to authoritative registry records.

---

# 91. Index Consistency

If:

```text
PRIMARY RECORD
```

and:

```text
DERIVED INDEX
```

conflict, the discrepancy MUST be surfaced.

The system MUST NOT silently choose whichever produces a convenient result.

---

# 92. Registry Rebuild

Derived indexes MAY be rebuilt from authoritative records.

Conceptually:

```text
AUTHORITATIVE ENTRIES
        │
        ├──► capability index
        ├──► task index
        ├──► mode index
        ├──► dependency graph
        └──► provenance graph
```

This enables repair without rewriting generator identity history.

---

# 93. Failure Recovery

If registry corruption is detected:

```text
IDENTIFY FAILED RECORD / EDGE
        │
        ▼
ISOLATE
        │
        ▼
INVALIDATE DEPENDENTS
        │
        ▼
PRESERVE UNAFFECTED ENTRIES
        │
        ▼
RESTORE FROM VALID PROVENANCE
        │
        ▼
REBUILD DERIVED INDEXES
        │
        ▼
REVALIDATE AFFECTED RESOLUTIONS
```

Global recomputation is a last resort.

---

# 94. Registry Gap Classes

Missing registry information SHOULD be classified:

```text
CRITICAL
DECISION-RELEVANT
EXPLANATORY
COSMETIC
```

Examples:

```text
Missing generator identity:
CRITICAL

Unknown validation for consequential selection:
DECISION-RELEVANT

Missing historical description:
EXPLANATORY

Missing display icon:
COSMETIC
```

---

# 95. Critical Gap Law

If a critical field required for resolution is missing:

```text
RESOLUTION = BLOCKED
```

or:

```text
UNKNOWN/GAP
```

depending on the context.

AMOS MUST NOT fabricate the missing value.

---

# 96. Registry Invariants

```text
GR-I01
Every registered generator has a stable identity.

GR-I02
Generator identity and generator version are distinct.

GR-I03
Aliases do not create independent generators.

GR-I04
Registration does not imply validation.

GR-I05
Validation does not imply promotion.

GR-I06
Promotion does not imply execution authority.

GR-I07
Registry presence does not establish canon.

GR-I08
Capability declaration does not establish capability validation.

GR-I09
Generator versions preserve lineage.

GR-I10
Material version changes cannot silently rewrite history.

GR-I11
Supersession is explicit.

GR-I12
Deprecated and retired generators preserve historical provenance.

GR-I13
Hard dependency failure blocks dependent admissibility.

GR-I14
Composition requires composition-level validation.

GR-I15
Shared ancestry does not count as independent confirmation.

GR-I16
Scope cannot silently expand.

GR-I17
Regime cannot silently expand.

GR-I18
Stale validation cannot be treated as fresh.

GR-I19
Unknown metadata remains UNKNOWN.

GR-I20
Conflicting registry records remain visible until resolved.

GR-I21
Competing generators remain COMPETING when evidence cannot discriminate.

GR-I22
Hard constraints dominate ranking.

GR-I23
Resolver convenience cannot override integrity.

GR-I24
Invalidation propagates only through actual dependency edges.

GR-I25
Historical registry state remains recoverable where required.

GR-I26
Derived indexes cannot override authoritative records.

GR-I27
Registry mutations preserve provenance.

GR-I28
Commit-time state changes trigger recheck when material.

GR-I29
Generator output cannot self-certify registry promotion.

GR-I30
Integrity > completeness > fluency > speed > token savings.
```

---

# 97. Reference Registration Flow

```text
GENERATOR ARTIFACT
      │
      ▼
IDENTITY EXTRACTION
      │
      ▼
VERSION BINDING
      │
      ▼
PROVENANCE CHECK
      │
      ▼
COLLISION CHECK
      │
      ├── collision ──► QUARANTINE / COMPETING
      │
      ▼
CONTRACT BINDING
      │
      ▼
CAPABILITY DECLARATION
      │
      ▼
DEPENDENCY REGISTRATION
      │
      ▼
SCOPE / REGIME DECLARATION
      │
      ▼
REGISTERED
```

---

# 98. Reference Resolution Flow

```text
TASK REQUEST
     │
     ▼
TASK CONTRACT
     │
     ▼
REQUIRED CAPABILITIES
     │
     ▼
GENERATOR REGISTRY
     │
     ▼
CANDIDATE SET
     │
     ▼
VERSION FILTER
     │
     ▼
LIFECYCLE FILTER
     │
     ▼
MODE FILTER
     │
     ▼
SCOPE / REGIME FILTER
     │
     ▼
DEPENDENCY CLOSURE
     │
     ▼
VALIDATION / FRESHNESS
     │
     ▼
CONFLICT ANALYSIS
     │
     ▼
COMPETING GENERATORS
     │
     ├── insufficient evidence ─► COMPETING
     │
     ├── no candidate ──────────► GAP
     │
     ▼
GENERATOR BINDING
```

---

# 99. Reference Mutation Flow

```text
REQUESTED CHANGE
      │
      ▼
CURRENT REGISTRY STATE
      │
      ▼
AUTHORITY CHECK
      │
      ▼
PROVENANCE CHECK
      │
      ▼
DEPENDENCY IMPACT
      │
      ▼
CONFLICT CHECK
      │
      ▼
VERSION / SUPERSESSION DECISION
      │
      ▼
COMMIT-TIME RECHECK
      │
      ▼
ATOMIC MUTATION
      │
      ▼
DERIVED INDEX UPDATE
      │
      ▼
PERSIST PROVENANCE
```

---

# 100. Anti-Fabrication Rules

The registry MUST NOT infer:

```text
implementation from documentation
validation from registration
correctness from output quality
independence from multiple names
freshness from recent indexing
canon from folder placement
execution authority from promotion
compatibility from structural similarity
```

These require their own evidence.

---

# 101. Documentation Firewall

README, registry, architecture, or specification claims are:

```text
SOURCE_CLAIM
```

unless independently validated.

Therefore:

$$Documented(G,C) \not\Rightarrow EmpiricallyVerified(G,C)$$

---

# 102. Structural Similarity Firewall

If generator $G_1$ resembles validated generator $G_2$:

$$Similar(G_1,G_2)$$

this does not establish:

$$Valid(G_1)$$

Structural similarity may justify a hypothesis or test strategy, not automatic promotion.

---

# 103. Authority Boundary

The Generator Registry may answer:

> Which generator is registered and apparently admissible?

It does not independently answer:

> Is the generator authorized to perform this external action?

That remains governed by:

```text
Task Contract
Capability Resolver
Effect Classification
Information Exposure
Mode Governance
Execution Authority
Commit-Time Validation
```

---

# 104. Canon Boundary

This document defines the candidate substantive architecture for `GENERATOR_REGISTRY.md`.

It does **not** establish that:

```text
a runtime registry currently implements this schema;
all generator artifacts have been registered;
all generator versions have been validated;
all listed relations exist physically;
all dependencies have been resolved;
all generators are operational;
the registry has been empirically validated;
this specification has completed final canon promotion.
```

Those require independent evidence and governance.

---

# 105. Artifact Declaration

```yaml
artifact:
  name: GENERATOR_REGISTRY
  path: 25_COGNITIVE_MATRIX/12_GENERATORS/GENERATOR_REGISTRY.md

  family: COGNITIVE_MATRIX/GENERATORS

  artifact_type:
    - REGISTRY_CONTRACT
    - GENERATOR_IDENTITY_INDEX
    - RESOLUTION_CONTROL_SURFACE

  node_id: generator_registry
  node_type: note

  claim_class: AMOS_MODEL

  status: CANDIDATE_CANON
  content_state: SUBSTANTIVE_SPECIFICATION

  origin_architect_steward: Trang Phan

  implementation:
    established: false

  population:
    established: false

  empirical_validation:
    established: false

  final_canon:
    established: false

  governing_principle:
    >
      Registry presence establishes recognized identity only.
      Generator validity, promotion, admissibility, selection,
      execution authority, and canonical status remain separate,
      evidence-bearing states.
```

---

# 106. Final Registry Law

$$\boxed{ Registry = Identity + Lineage + Evidence\ State + Operational\ Constraints }$$

but:

$$\boxed{ Registry\ Presence \neq Trust }$$

The registry exists so AMOS can know not merely that a generator has a name, but:

```text
WHAT it is
WHICH version it is
WHERE it came from
WHAT it claims to do
WHAT it has actually validated
WHAT it depends upon
WHERE it is applicable
WHEN its evidence remains valid
WHAT conflicts with it
WHAT supersedes it
WHEN it may be selected
WHY it may be selected
WHAT would invalidate that selection
```

When these cannot be established, the registry preserves the gap.

It does not invent completion.

---

[[00_ROOT_MOC]]|[[AMOS MOC]]

---

**Related:** [[00_HOME]] · [[GENERATORS_MAP]] · [[COGNITIVE_MATRIX_MOC]] · [[AMOS_RSCF_NODES]] · 12_GENERATORS_CONTRACT · 12_GENERATORS_VERSIONING · [[GENERATOR_OUTPUT]] · [[GENERATOR_FALSIFICATION]] · [[GENERATOR_PROMOTION]] · [[TASK_CONTRACT]] · [[TASK_RESOLVER]] · [[CAPABILITY_RESOLVER]] · [[MODE_ADMISSION_QUEUE]] · [[MODE_COMPOSITION_REGISTRY]] · [[MODE_CONFLICT_REGISTRY]] · [[MODE_COVERAGE_MATRIX]] · [[MODE_DEPENDENCY_GRAPH]]

---

RSCF-NODE

node_id: generator_registry

node_type: note

path: 25_COGNITIVE_MATRIX/12_GENERATORS/GENERATOR_REGISTRY.md

claim_class: AMOS_MODEL

RSCF-RELATIONS:

* INDEXED_BY: [[00_HOME]]
* INDEXED_BY: [[AMOS_RSCF_NODES]]
* PART_OF: [[GENERATORS_MAP]]
* PART_OF: [[COGNITIVE_MATRIX_MOC]]
* GOVERNED_BY: 12_GENERATORS_CONTRACT
* VERSIONED_BY: 12_GENERATORS_VERSIONING
* VALIDATED_BY: [[GENERATOR_FALSIFICATION]]
* PROMOTED_BY: [[GENERATOR_PROMOTION]]
* PRODUCES_ACCORDING_TO: [[GENERATOR_OUTPUT]]
* QUERIED_BY: [[TASK_RESOLVER]]
* QUERIED_BY: [[CAPABILITY_RESOLVER]]

```

The key integrity distinction is that this file is now **substantive architecture rather than a placeholder**, but it remains `AMOS_MODEL / CANDIDATE_CANON`: it does not falsely assert that the registry is already populated or implemented.
```

---
**MOC:** [[12_GENERATORS_MOC]]

