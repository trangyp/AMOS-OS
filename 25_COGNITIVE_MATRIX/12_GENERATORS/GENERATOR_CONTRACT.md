---
artifact_id: AMOS-CM-12-GENERATORS-GENERATOR-CONTRACT
title: "12_GENERATORS — Generator Contract"

path_target: "25_COGNITIVE_MATRIX/12_GENERATORS/GENERATOR_CONTRACT.md"

artifact_class: MATRIX_INFRASTRUCTURE_PLACEHOLDER
contract_class: GENERATOR_CONTROL_CONTRACT
architecture_layer: COGNITIVE_MATRIX_INFRASTRUCTURE

origin_architect: Trang Phan
stewardship: AMOS / Trang corpus

status: PLACEHOLDER
implementation_status: UNIMPLEMENTED_OR_UNVERIFIED
validation_status: UNVALIDATED
epistemic_class: UNKNOWN/GAP
conclusion_class: UNKNOWN/GAP

amos_core_target: v4.4
updated: 2026-08-26

authority_class: NON_AUTHORITATIVE_SPECIFICATION
execution_authority: NONE
canon_authority: NONE
promotion_authority: NONE
mutation_authority: NONE

risk_class: STRUCTURAL_INFRASTRUCTURE
default_reversibility: HIGH_WHILE_PLACEHOLDER

hml_scope:
  H:
    - GENERATOR_GOVERNANCE
    - ARCHITECTURE_COMPATIBILITY
    - CANON_BOUNDARY
    - AUTHORITY_BOUNDARY
  M:
    - GENERATOR_ROUTING
    - TEMPLATE_BINDING
    - SCHEMA_BINDING
    - VALIDATION_PIPELINE
    - DEPENDENCY_GRAPH
  L:
    - FILE_CREATION
    - CONTENT_ASSEMBLY
    - FIELD_POPULATION
    - HASHING
    - RECEIPT_EMISSION

rscf_role:
  - GENERATOR_CONTRACT_CAPSULE
  - GENERATION_EVIDENCE_CAPSULE

gmef_role:
  - GENERATOR_GOVERNANCE_BOUNDARY
  - GENERATED_ARTIFACT_PROMOTION_GATE

tags:
  - AMOS
  - AMOS_OS
  - AMOS_CORE_v4_4
  - COGNITIVE_MATRIX
  - MATRIX_INFRASTRUCTURE
  - GENERATOR
  - GENERATOR_CONTRACT
  - ARTIFACT_GENERATION
  - PLACEHOLDER
  - UNKNOWN_GAP
  - RSCF
  - GMEF
  - HML
  - PROVENANCE
  - SCHEMA
  - VALIDATION
  - INVARIANT
  - DEPENDENCY_GRAPH
  - EVENT_BUS
  - CONTROL_PLANE
  - AUTHORITY
  - CANON
  - MVCC
  - CAS
  - IDEMPOTENCY
  - REPLAY
  - ROLLBACK
  - REPAIR
  - ANTI_FABRICATION
  - ANTI_REGRESSION
  - SELECTIVE_INVALIDATION
---

# 12_GENERATORS — Generator Contract

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

# 0. Contract purpose

`12_GENERATORS` defines the contract surface for AMOS components that transform an already-defined specification, schema, template, registry record, or validated input bundle into a **candidate generated artifact**.

A generator is not the source of truth.

A generator is not a canon authority.

A generator is not an epistemic validator.

A generator is not a policy authority.

A generator is not an external-effect authority.

Its narrow role is:

```text
VALID INPUT SPECIFICATION
        ↓
GENERATOR
        ↓
CANDIDATE ARTIFACT
        ↓
VALIDATION
        ↓
GOVERNANCE / PROMOTION
```

The generator layer exists to make repeatable structure creation possible without collapsing generation, validation, authority, and canon admission into a single operation.

---

# 1. Core distinction

The most important generator invariant is:

```text
Generation
!= Validation
!= Admission
!= Authority
!= Commit
```

More explicitly:

```text
GENERATED
!= CORRECT

GENERATED
!= VALIDATED

GENERATED
!= CANONICAL

GENERATED
!= ACTIVE

GENERATED
!= IMPLEMENTED

GENERATED
!= AUTHORIZED

GENERATED
!= COMMITTED
```

A generator may create a syntactically valid artifact that is semantically wrong.

A generator may create a semantically coherent artifact whose premises are unsupported.

A generator may reproduce a canonical template while filling fields with stale data.

A generator may generate an executable implementation without having authority to execute it.

The architecture must preserve all of those distinctions.

---

# 2. Generator definition

A generator is modeled as:

[
G =
\langle
ID,
Version,
Contract,
InputSchema,
OutputSchema,
Template,
Rules,
Dependencies,
Invariants,
Policy,
Provenance,
ValidationHooks
\rangle
]

The generation operation is:

[
A_c =
G(S_i,T,R,C)
]

where:

* (A_c) = candidate artifact;
* (S_i) = validated input specification;
* (T) = template or structural grammar;
* (R) = generation rules;
* (C) = generation context.

The output remains:

```text
CANDIDATE
```

until downstream gates pass.

---

# 3. Scope

This contract may govern generators for artifacts such as:

```text
Markdown contracts
YAML manifests
JSON schemas
RSCF capsules
GMEF records
mode definitions
cell contracts
registry entries
validation stubs
workflow specifications
event schemas
kernel contracts
engine contracts
skill manifests
agent manifests
worker contracts
test fixtures
indexes
dependency maps
documentation skeletons
migration candidates
configuration candidates
```

This is a structural scope declaration.

It does not assert that every listed generator currently exists.

---

# 4. Explicit non-scope

The generator layer must not silently own:

```text
truth determination
canon admission
policy approval
authority issuance
runtime activation
irreversible external effects
credential creation
security-root rotation
production deployment
finality declaration
evidence fabrication
provenance invention
```

Any generator that appears to perform one of those functions must route through the appropriate governing subsystem.

---

# 5. Generator classes

AMOS may distinguish generator classes by consequence.

```yaml
generator_classes:

  G0_STRUCTURAL:
    purpose:
      - create empty structural skeletons
      - materialize known paths
      - create placeholder contracts
    default_effect: REVERSIBLE

  G1_DOCUMENT:
    purpose:
      - generate documentation
      - produce explanatory artifacts
      - create indexes
    default_effect: REVERSIBLE

  G2_SCHEMA:
    purpose:
      - generate schemas
      - manifests
      - validation structures
    default_effect: GOVERNANCE_RELEVANT

  G3_RUNTIME_SPEC:
    purpose:
      - generate kernel/engine/skill/agent/worker specifications
    default_effect: IMPLEMENTATION_RELEVANT

  G4_CODE:
    purpose:
      - generate executable implementation candidates
    default_effect: HIGH_VALIDATION_BURDEN

  G5_GOVERNANCE:
    purpose:
      - generate candidate policy/canon/authority records
    default_effect: CRITICAL
    hard_rule:
      generator_may_not_self_promote: true
```

These classes are proposed AMOS infrastructure categories.

They remain `MODEL` until accepted by the actual generator registry.

---

# 6. Generator state machine

A generator invocation should pass through explicit states.

```text
REQUESTED
    ↓
INPUT_BOUND
    ↓
DEPENDENCIES_RESOLVED
    ↓
PRECONDITIONS_CHECKED
    ↓
GENERATION_STARTED
    ↓
CANDIDATE_PRODUCED
    ↓
STRUCTURE_VALIDATED
    ↓
SEMANTIC_VALIDATION_PENDING
    ↓
GOVERNANCE_PENDING
```

Terminal outcomes:

```text
ACCEPTED_AS_CANDIDATE
REJECTED
QUARANTINED
FAILED
CANCELLED
STALE
SUPERSEDED
```

`CANDIDATE_PRODUCED` must never be treated as `PROMOTED`.

---

# 7. Typed input contract

Each invocation should receive a typed input envelope.

```yaml
generator_input:

  request:
    request_id: UNKNOWN
    generator_id: UNKNOWN
    generator_version: UNKNOWN

  objective:
    artifact_type: UNKNOWN
    target_path: UNKNOWN
    requested_scope: UNKNOWN

  source_spec:
    specification_ids: []
    template_ids: []
    schema_ids: []
    canon_refs: []

  context:
    architecture_version: UNKNOWN
    core_version: v4.4
    policy_epoch: UNKNOWN
    provenance_epoch: UNKNOWN
    mode_context: UNKNOWN
    regime: UNKNOWN

  dependencies:
    required: []
    optional: []

  constraints:
    must_preserve: []
    must_not_generate: []
    prohibited_fields: []

  evidence:
    source_refs: []
    provenance_roots: []

  state:
    observed_read_set: []
    expected_versions: []

  execution:
    dry_run: true
    idempotency_key: UNKNOWN
```

Missing load-bearing input should produce:

```text
UNKNOWN/GAP
```

not guessed values.

---

# 8. Typed output contract

A generator should emit a candidate artifact plus generation metadata.

```yaml
generator_output:

  generation:
    generation_id: UNKNOWN
    generator_id: UNKNOWN
    generator_version: UNKNOWN
    request_id: UNKNOWN

  artifact:
    artifact_id: UNKNOWN
    artifact_type: UNKNOWN
    candidate_path: UNKNOWN
    content_hash: UNKNOWN
    schema_version: UNKNOWN
    status: CANDIDATE

  provenance:
    source_refs: []
    provenance_roots: []
    template_refs: []
    dependency_refs: []

  validation:
    syntax_result: UNKNOWN
    schema_result: UNKNOWN
    semantic_result: NOT_RUN
    conflict_result: NOT_RUN

  governance:
    authority_state: NONE
    canon_state: NOT_ADMITTED
    promotion_state: NOT_PROMOTED

  uncertainty:
    unresolved_fields: []
    unresolved_dependencies: []
    confidence_ceiling: 0

  receipts:
    generation_receipt: UNKNOWN
    validation_receipts: []
```

---

# 9. Required candidate metadata

Every generated artifact should be able to answer:

```text
Who requested it?
Which generator produced it?
Which generator version?
Which template?
Which input specification?
Which source/canon references?
Which dependency versions?
Which policy epoch?
Which provenance epoch?
Which observed state?
Which unresolved fields?
Which validations ran?
Which validations did not run?
Was it dry-run or materialized?
Was it promoted?
What supersedes it?
```

If those questions cannot be answered, provenance is incomplete.

---

# 10. State variables

A generator runtime may need state such as:

```yaml
generator_state:

  identity:
    generator_id: UNKNOWN
    version: UNKNOWN
    contract_hash: UNKNOWN

  lifecycle:
    state: IDLE
    current_request: null

  context:
    architecture_version: UNKNOWN
    policy_epoch: UNKNOWN
    provenance_epoch: UNKNOWN
    regime: UNKNOWN

  dependency_state:
    resolved: []
    unresolved: []
    stale: []

  input_state:
    input_hash: UNKNOWN
    read_set: []

  output_state:
    candidate_hash: UNKNOWN
    target_path: UNKNOWN

  validation_state:
    structural: UNKNOWN
    schema: UNKNOWN
    semantic: UNKNOWN

  execution_state:
    dry_run: true
    effect_state: NONE

  recovery_state:
    rollback_available: UNKNOWN
    retry_count: 0
```

---

# 11. Generator operators

Candidate deterministic operators include:

```text
load_spec()
resolve_template()
resolve_dependencies()
check_required_fields()
bind_context()
construct_candidate()
normalize_structure()
render_artifact()
compute_hash()
attach_provenance()
emit_generation_receipt()
validate_schema()
compare_existing_target()
detect_conflict()
stage_candidate()
invalidate_candidate()
rollback_generation()
```

These are contract-level operator names.

They are not claims that the corresponding implementation already exists.

---

# 12. Hard invariants

## I-GEN-001 — No source invention

```text
Missing source
→ UNKNOWN/GAP
```

not:

```text
Missing source
→ generated plausible source
```

## I-GEN-002 — No canon invention

```text
Generator
cannot
create canon merely by generating a file.
```

## I-GEN-003 — No authority invention

```text
CAPABILITY
!= AUTHORITY
```

A generator cannot self-authorize.

## I-GEN-004 — Candidate truthfulness

```text
generated artifact status
must accurately state:
GENERATED / CANDIDATE / PLACEHOLDER / UNKNOWN
```

when applicable.

## I-GEN-005 — Provenance preservation

Source lineage must not disappear during generation.

## I-GEN-006 — Dependency visibility

Load-bearing dependencies must be recorded.

## I-GEN-007 — No silent semantic substitution

A generator must not silently replace one AMOS term with another because it appears similar.

## I-GEN-008 — Schema semantics preservation

A structurally valid schema cannot silently change field meaning.

## I-GEN-009 — Generation determinism where declared

For deterministic generator classes:

[
Same(Input,Version,Context)
\Rightarrow
Same(Output)
]

subject to explicitly declared nondeterministic fields.

## I-GEN-010 — Idempotent materialization where required

Repeated delivery with the same idempotency identity should not create uncontrolled duplicates.

## I-GEN-011 — Existing-artifact protection

An existing validated artifact must not be overwritten merely because a generator produced a candidate with the same path.

## I-GEN-012 — Unknown fails closed

```text
UNKNOWN/GAP
!= PASS
```

## I-GEN-013 — Dry-run truthfulness

```text
SIMULATED
!= MATERIALIZED
```

## I-GEN-014 — Proposal/commit separation

```text
PROPOSAL
!= COMMIT
```

## I-GEN-015 — Generator cannot weaken upstream invariants

Downstream generation may only preserve or strengthen required governance constraints.

---

# 13. H/M/L applicability

## H — Governance / architectural level

At H, generators are constrained by:

```text
AMOS_CORE target
architecture version
canon boundaries
governance policy
authority rules
provenance requirements
epistemic classification
promotion rules
```

## M — Generator coordination level

At M:

```text
registry resolution
template selection
dependency graph
schema binding
generation workflows
validation routing
conflict handling
```

## L — Materialization level

At L:

```text
render content
write candidate bytes
compute hashes
produce files
attach metadata
emit receipts
```

A valid L-level generated file does not prove H-level admissibility.

---

# 14. Recursive H/M/L rule

Generator components may themselves decompose recursively:

```text
Generator
├── H: governance contract
├── M: orchestration/assembly
└── L: rendering/materialization
```

And each child may again have H/M/L.

This follows AMOS recursive decomposition as a structural model.

---

# 15. Generator registry contract

Generators should eventually be addressable through a governed registry.

```yaml
generator_registry_entry:

  generator_id: UNKNOWN

  name: UNKNOWN

  version: UNKNOWN

  class: UNKNOWN

  purpose: UNKNOWN

  accepts: []

  emits: []

  templates: []

  schemas: []

  required_dependencies: []

  required_invariants: []

  required_policy_modes: []

  authority_required: NONE

  deterministic: UNKNOWN

  idempotent: UNKNOWN

  dry_run_supported: UNKNOWN

  status: UNVALIDATED

  provenance:
    source_refs: []
```

Addressability does not imply validation.

---

# 16. Generator resolution

Generator selection should be deterministic when multiple candidates exist.

Possible routing predicate:

[
Resolve(request)
\rightarrow
G^*
]

subject to:

```text
artifact type match
scope match
architecture compatibility
schema compatibility
policy compatibility
version compatibility
status compatibility
```

If multiple generators remain equally applicable:

```text
AMBIGUOUS
```

rather than registration-order selection.

---

# 17. Template contract

Templates are dependencies, not truth sources.

```yaml
template_contract:

  template_id: UNKNOWN
  version: UNKNOWN
  artifact_types: []

  required_fields: []
  optional_fields: []

  preservation_rules: []

  prohibited_inferences: []

  source_refs: []

  semantic_hash: UNKNOWN

  status: UNVALIDATED
```

A template update that changes semantic meaning should produce a new semantic version or hash.

---

# 18. Schema contract

Generated artifacts should be validated against explicit schemas where applicable.

```yaml
schema_binding:

  schema_id: UNKNOWN
  schema_version: UNKNOWN
  schema_hash: UNKNOWN

  validation_mode:
    - STRUCTURAL
    - TYPE
    - REQUIRED_FIELD

  semantic_validation:
    status: SEPARATE_REQUIRED
```

Critical distinction:

```text
SchemaValid
!= SemanticallyCorrect
```

---

# 19. Dependency graph

Generator dependency edges should be typed.

```text
REQUIRES
OPTIONAL
DERIVED_FROM
TEMPLATED_BY
SCHEMA_VALIDATED_BY
GOVERNED_BY
PROVENANCE_ROOT
COMPATIBLE_WITH
CONFLICTS_WITH
SUPERSEDES
```

Example:

```yaml
dependencies:

  - from: GENERATOR_X
    to: TEMPLATE_Y
    type: TEMPLATED_BY
    load_bearing: true

  - from: GENERATOR_X
    to: SCHEMA_Z
    type: SCHEMA_VALIDATED_BY
    load_bearing: true
```

---

# 20. Provenance contract

Generated artifacts should carry provenance sufficient to distinguish:

```text
source text
template text
generator-produced text
inferred text
placeholder text
user-supplied text
validated external evidence
```

Suggested provenance structure:

```yaml
provenance:

  sources:
    - source_id: UNKNOWN
      role: SOURCE_CANON
      hash: UNKNOWN

  templates:
    - template_id: UNKNOWN
      version: UNKNOWN
      hash: UNKNOWN

  generator:
    id: UNKNOWN
    version: UNKNOWN
    contract_hash: UNKNOWN

  invocation:
    request_id: UNKNOWN
    generated_at: null

  dependencies: []

  ancestry_roots: []
```

Repeated generated descendants do not constitute independent confirmation.

---

# 21. Evidence topology

If generator output includes claims, those claims must preserve evidence topology.

```text
SOURCE
  ↓
EXTRACTION
  ↓
NORMALIZATION
  ↓
GENERATED CLAIM
```

The generated claim cannot acquire more epistemic confidence simply because it was reformatted.

Confidence must obey:

[
C_{derived}
\le
\min(C_{load-bearing\ premises})
]

unless independently revalidated.

---

# 22. Control-plane requirements

The generator layer sits below AMOS infrastructure authority.

```text
Agent / Skill / Workflow
        ↓ request
GENERATOR
        ↓
CANDIDATE ARTIFACT
        ↓
VALIDATION
        ↓
CONTROL PLANE
        ↓
PROMOTION / REJECTION
```

The control plane should own:

```text
authority
policy
state freshness
CAS/MVCC checks
promotion
finalization
rollback
canon admission
runtime activation
```

The generator owns none of these merely by generating an artifact.

---

# 23. Agents

Possible agent roles around generators:

### GENERATOR_ROUTER_AGENT

Selects a candidate generator based on the request.

No authority.

### SPEC_COMPLETION_AGENT

Identifies missing required fields.

May propose values only when supported by source evidence.

Unsupported fields remain `UNKNOWN/GAP`.

### GENERATION_REVIEW_AGENT

Reviews candidate output for structural or semantic issues.

No promotion authority.

### PROVENANCE_AUDITOR_AGENT

Checks lineage and correlated ancestry.

### ADVERSARIAL_GENERATION_AUDITOR

Searches for:

```text
fabricated source
silent semantic drift
overwritten canon
stale dependencies
schema-only validation overclaim
authority leakage
incorrect status labels
```

### CONFLICT_RESOLUTION_AGENT

May structure competing candidates.

Must not force convergence without discriminating evidence.

---

# 24. Skills

Possible Skills:

```text
materialize-placeholder
generate-contract
generate-rscf
generate-gmef
generate-schema
generate-registry-entry
generate-index
generate-mode-contract
generate-cell-contract
generate-validation-fixture
generate-migration-candidate
compare-generated-artifact
attach-provenance
```

Skill invocation does not grant authority.

---

# 25. Worker boundary

Actual file materialization should be performed by a bounded worker.

```text
Generator
    ↓ candidate bytes
Infrastructure authorization
    ↓
File Worker
    ↓
materialized candidate
```

Worker inputs should include:

```yaml
materialization_request:
  target_path: UNKNOWN
  expected_existing_hash: UNKNOWN
  candidate_hash: UNKNOWN
  authority_ref: UNKNOWN
  idempotency_key: UNKNOWN
```

This preserves the worker-only external-effect invariant.

---

# 26. Workflow — new artifact

```text
GENERATION_REQUESTED
        ↓
SPEC_RESOLVED
        ↓
DEPENDENCIES_RESOLVED
        ↓
INPUT_VALIDATED
        ↓
GENERATION_STARTED
        ↓
CANDIDATE_PRODUCED
        ↓
STRUCTURAL_VALIDATION
        ↓
SEMANTIC_REVIEW
        ↓
PROVENANCE_REVIEW
        ↓
CANDIDATE_STAGED
```

Promotion is a separate workflow.

---

# 27. Workflow — update existing artifact

Updating an existing artifact has a higher burden.

```text
UPDATE_REQUESTED
    ↓
EXISTING_ARTIFACT_READ
    ↓
READ_SET_CAPTURED
    ↓
DIFF_GENERATED
    ↓
PRESERVATION_CHECK
    ↓
CONFLICT_CHECK
    ↓
VALIDATION
    ↓
CAS_CHECK
    ↓
STAGED_UPDATE
```

Do not blindly replace an existing validated file.

---

# 28. Workflow — placeholder generation

```text
EMPTY_REQUIRED_PATH
        ↓
MANIFEST_EXPECTATION_CONFIRMED
        ↓
NO_EXISTING_ARTIFACT
        ↓
PLACEHOLDER_TEMPLATE_BOUND
        ↓
PLACEHOLDER_GENERATED
        ↓
STATUS = UNKNOWN/GAP
        ↓
MATERIALIZED
```

Placeholder generation must not invent the missing canon.

---

# 29. Workflow — generated contract promotion

```text
CANDIDATE_CONTRACT
        ↓
SOURCE_BOUND
        ↓
SCHEMA_VALID
        ↓
SEMANTIC_VALID
        ↓
DEPENDENCIES_VALID
        ↓
PROVENANCE_VALID
        ↓
CONFLICT_RESOLVED
        ↓
POLICY_VALID
        ↓
AUTHORITY_GRANTED
        ↓
PROMOTED
```

---

# 30. Protocols

The generator subsystem may require protocols for:

```text
generator discovery
generator version negotiation
schema negotiation
template negotiation
dependency resolution
candidate transfer
validation receipt exchange
conflict signaling
materialization request
idempotency
rollback
supersession
```

Protocol definitions remain gaps until explicit files exist.

---

# 31. Event semantics

Suggested events:

```text
GENERATOR_REGISTERED
GENERATOR_REQUESTED
GENERATOR_RESOLVED
GENERATION_INPUT_BOUND
GENERATION_STARTED
GENERATION_CANDIDATE_CREATED
GENERATION_FAILED
GENERATION_QUARANTINED
GENERATION_VALIDATION_REQUESTED
GENERATION_VALIDATION_PASSED
GENERATION_VALIDATION_FAILED
GENERATION_MATERIALIZATION_PROPOSED
GENERATION_MATERIALIZED
GENERATION_SUPERSEDED
GENERATION_ROLLED_BACK
```

Event emission does not equal successful execution.

---

# 32. Event envelope

```yaml
generation_event:

  event_id: UNKNOWN

  type: UNKNOWN

  generator:
    id: UNKNOWN
    version: UNKNOWN

  request_id: UNKNOWN

  correlation_id: UNKNOWN
  causation_id: UNKNOWN

  artifact_id: UNKNOWN

  candidate_hash: UNKNOWN

  provenance_refs: []

  policy_epoch: UNKNOWN
  observed_state_version: UNKNOWN

  status: UNKNOWN

  timestamp: null
```

---

# 33. MVCC / CAS pattern

For existing targets:

```text
Generator observes target hash/version V1
        ↓
Generator builds candidate C
        ↓
Before write:
current target must still equal V1
```

Conceptually:

[
Commit(C)
\iff
CurrentVersion(Target)
======================

ObservedVersion(Target)
]

If not:

```text
STALE_GENERATION
```

and recompute only affected work.

---

# 34. Read-set contract

```yaml
generation_read_set:

  - artifact_id: UNKNOWN
    version: UNKNOWN
    hash: UNKNOWN
    load_bearing: true

  - template_id: UNKNOWN
    version: UNKNOWN
    hash: UNKNOWN
    load_bearing: true

  - schema_id: UNKNOWN
    version: UNKNOWN
    hash: UNKNOWN
    load_bearing: true
```

A change to an unrelated file should not invalidate the entire generation.

---

# 35. Write-set contract

```yaml
generation_write_set:

  create: []

  update: []

  delete: []

  metadata_only: []
```

Delete operations should have a higher governance burden than creation of reversible placeholders.

---

# 36. Idempotency

Repeated delivery should not create uncontrolled copies.

```yaml
idempotency:
  key: UNKNOWN
  scope: UNKNOWN
  prior_result: UNKNOWN
```

If the same input, generator version, target, and idempotency key have already produced a valid candidate, the subsystem should reuse or explicitly version it.

---

# 37. Determinism modes

```yaml
determinism_modes:

  DETERMINISTIC:
    same_input_same_context_same_output: required

  BOUNDED_NONDETERMINISTIC:
    output_variation_allowed: true
    provenance_of_variation_required: true

  STOCHASTIC_PROPOSAL:
    output_is_candidate_only: true
    mandatory_validation: true
```

LLM-assisted generation belongs at most in the stochastic-proposal class unless determinism is otherwise established.

---

# 38. Canon boundary

Generated files that describe canon must preserve source attribution.

Correct:

```text
SOURCE_CANON
→ generated structured representation
```

Incorrect:

```text
generator output
→ automatically becomes CANON
```

Canon admission remains a separate governed process.

---

# 39. Epistemic boundary

Generated statements should be typed.

```yaml
claim:
  text: UNKNOWN
  class: UNKNOWN
  source_refs: []
  evidence_refs: []
  confidence_ceiling: 0
```

The generator must not elevate:

```text
SOURCE_CLAIM
```

to:

```text
VERIFIED
```

without independent validation.

---

# 40. Scope / regime / freshness

Generated artifacts inherit the narrowest valid scope of their load-bearing dependencies.

```yaml
validity_envelope:

  system: UNKNOWN
  environment: UNKNOWN
  architecture_version: UNKNOWN
  core_version: UNKNOWN
  regime: UNKNOWN
  valid_from: null
  valid_until: null
  assumptions: []
```

If one dependency becomes stale, only dependent outputs should be invalidated.

---

# 41. Conflict handling

Possible generation conflicts:

```text
target already exists
multiple templates apply
multiple generator versions apply
source files disagree
schema versions conflict
policy versions conflict
canon versions conflict
output duplicates another artifact
```

Conflict result:

```text
COMPETING
```

or:

```text
REQUIRES_RESOLUTION
```

—not silent overwrite.

---

# 42. Existing artifact protection

Before modifying an existing target:

```yaml
existing_target:
  exists: UNKNOWN
  current_hash: UNKNOWN
  validation_state: UNKNOWN
  authority_state: UNKNOWN
  canon_state: UNKNOWN
```

Higher protection applies when:

```text
VALIDATED
CANONICAL
AUTHORITATIVE
ACTIVE_RUNTIME
GOVERNANCE_CRITICAL
```

---

# 43. Generated-artifact status ontology

```text
PLACEHOLDER
DRAFT
GENERATED
CANDIDATE
QUARANTINED
STRUCTURALLY_VALID
SEMANTICALLY_VALID
VALIDATED
PROMOTION_PENDING
PROMOTED
ACTIVE
SUPERSEDED
REVOKED
ARCHIVED
```

Transitions must be explicit.

---

# 44. Failure modes

```yaml
failure_modes:

  F-GEN-001:
    name: FABRICATED_SOURCE
    condition: generator invents a missing source/canon reference

  F-GEN-002:
    name: SILENT_PROMOTION
    condition: generated output is labeled canonical/active without governance

  F-GEN-003:
    name: AUTHORITY_LEAKAGE
    condition: generator capability treated as execution authority

  F-GEN-004:
    name: TEMPLATE_DRIFT
    condition: template semantics changed without version update

  F-GEN-005:
    name: SCHEMA_DRIFT
    condition: same field changes meaning silently

  F-GEN-006:
    name: STALE_INPUT
    condition: generation uses outdated load-bearing state

  F-GEN-007:
    name: TARGET_OVERWRITE
    condition: existing artifact replaced without CAS/preservation check

  F-GEN-008:
    name: PROVENANCE_LOSS
    condition: source ancestry disappears

  F-GEN-009:
    name: DUPLICATE_AMPLIFICATION
    condition: repeated generated descendants look like independent support

  F-GEN-010:
    name: UNKNOWN_TO_PASS
    condition: missing value treated as successful validation

  F-GEN-011:
    name: DRY_RUN_OVERCLAIM
    condition: simulation reported as materialized output

  F-GEN-012:
    name: PARTIAL_TRANSACTION
    condition: multi-artifact generation leaves inconsistent partial state

  F-GEN-013:
    name: VERSION_AMBIGUITY
    condition: wrong generator/template/schema version chosen

  F-GEN-014:
    name: NON_IDEMPOTENT_RETRY
    condition: retry creates uncontrolled duplicates

  F-GEN-015:
    name: GENERATED_TRUTH_OVERCLAIM
    condition: generated claim classified above evidence support
```

---

# 45. Recovery

Recovery sequence:

```text
FAILURE DETECTED
        ↓
IDENTIFY FAILED EDGE
        ↓
STOP MATERIALIZATION
        ↓
QUARANTINE CANDIDATE
        ↓
PRESERVE INPUT + RECEIPTS
        ↓
INVALIDATE DEPENDENT OUTPUTS
        ↓
ROLL BACK MATERIALIZED CHANGES IF NECESSARY
        ↓
RE-RESOLVE CHANGED DEPENDENCY
        ↓
REGENERATE MINIMUM NECESSARY SCOPE
```

Do not regenerate the entire matrix if one template or one cell contract failed.

---

# 46. Retry policy

A failed generation should not automatically retry unless something changed.

```text
RetryAllowed
iff
InputChanged
OR DependencyChanged
OR GeneratorVersionChanged
OR PolicyChanged
OR TransientFailureResolved
```

Repeatedly executing the identical failed path is prohibited.

---

# 47. Repair versus regeneration

```text
REPAIR
= preserve identity, fix defective subset

REGENERATION
= rebuild candidate from source inputs

REPLACEMENT
= create new identity/version

SUPERSESSION
= explicitly retire predecessor
```

These should not be conflated.

---

# 48. Multi-artifact atomic generation

Some generator requests may produce dependent bundles.

Example:

```text
mode contract
+ schema
+ registry entry
+ validator stub
```

Such a bundle should be treated as a semantic transaction.

```yaml
generation_transaction:

  transaction_id: UNKNOWN

  artifacts: []

  atomicity_required: UNKNOWN

  dependencies: []

  staged: []

  validation: UNKNOWN

  commit_state: NOT_COMMITTED
```

Partial bundles should remain staged until integrity is restored.

---

# 49. Validation stack

A generated artifact can pass several independent validation layers.

```text
V0 — syntax
V1 — file/schema structure
V2 — semantic contract
V3 — dependency compatibility
V4 — provenance
V5 — scope/regime/freshness
V6 — conflict
V7 — runtime compatibility
V8 — governance/policy
V9 — empirical validation where applicable
```

Passing one does not imply passing the rest.

---

# 50. Validators

Suggested validator contracts:

```text
validate_generator_input()
validate_required_fields()
validate_template_version()
validate_schema()
validate_dependency_closure()
validate_provenance()
validate_status_truthfulness()
validate_target_conflict()
validate_semantic_preservation()
validate_scope()
validate_regime()
validate_freshness()
validate_idempotency()
validate_read_set()
validate_write_set()
validate_no_authority_leak()
```

---

# 51. Test classes

## Unit tests

Check individual operators.

## Contract tests

Check input/output and invariant semantics.

## Replay tests

Same invocation reproduces declared deterministic output.

## Mutation tests

Corrupt inputs/templates and verify rejection.

## Conflict tests

Create multiple applicable candidates and verify fail-closed behavior.

## Stale-state tests

Modify a load-bearing dependency after observation and verify CAS rejection.

## Provenance tests

Check ancestry preservation and duplicate-root collapse.

## Authority tests

Ensure generated artifacts cannot self-promote.

## Recovery tests

Induce mid-generation failure and verify rollback/quarantine.

---

# 52. Minimum constitutional tests

```text
T-GEN-001
Missing required source
→ generation blocked or UNKNOWN/GAP

T-GEN-002
Generated canonical-looking file
→ canon_state remains NOT_ADMITTED

T-GEN-003
Unknown invariant ID
→ fail closed

T-GEN-004
Existing target changed after read
→ no overwrite

T-GEN-005
Same idempotency key replay
→ no uncontrolled duplicate

T-GEN-006
Dry run
→ no materialized commit claim

T-GEN-007
Source descendants duplicated
→ provenance independence does not increase

T-GEN-008
Generator produces valid schema but unsupported claim
→ claim remains unsupported

T-GEN-009
Higher-version generator conflicts with validated older generator
→ version number alone cannot decide

T-GEN-010
One artifact in atomic bundle fails
→ bundle not promoted
```

---

# 53. Adversarial validation

For consequential generation, challenge the candidate through an independent path.

Questions:

```text
Did generation invent missing content?
Did it silently change terminology?
Did it merge incompatible canon?
Did it treat duplicates as independent?
Did it use stale state?
Did it overwrite an existing artifact?
Did it reduce required invariants?
Did it overstate validation?
Did it label simulation as commit?
Did it create authority through metadata?
```

A successful challenge downgrades or rejects the candidate.

---

# 54. Falsifiers

This contract should itself be falsifiable.

Examples:

```text
F1:
Actual AMOS generator architecture defines a materially different generator responsibility.

F2:
Existing canonical generator contract supersedes this placeholder.

F3:
Generator registry demonstrates different mandatory fields.

F4:
AMOS runtime implementation requires additional load-bearing state not represented here.

F5:
A declared invariant conflicts with accepted higher-order AMOS governance.

F6:
A generator is explicitly authorized by canon to perform a function currently marked non-authoritative.
```

If a falsifier succeeds:

```text
UPDATE THIS PLACEHOLDER
```

rather than silently preserving it.

---

# 55. RSCF completion state

```yaml
rscf:

  claim_id: RSCF-CM-GENERATOR-CONTRACT-001

  claim:
    "This file defines the accepted AMOS contract for the 12_GENERATORS infrastructure layer."

  claim_class:
    UNKNOWN/GAP

  scope:
    system: AMOS_OS
    subsystem: COGNITIVE_MATRIX
    package: 12_GENERATORS
    artifact: GENERATOR_CONTRACT.md

  evidence: []

  provenance: []

  load_bearing_premises:
    - authoritative generator canon recovered
    - generator registry recovered
    - schema dependencies recovered
    - control-plane binding recovered
    - validation requirements recovered

  dependencies: []

  competing: []

  falsifiers:
    - authoritative generator contract exists elsewhere
    - runtime implementation contradicts this placeholder
    - accepted matrix manifest specifies different semantics

  regime:
    architecture: UNKNOWN
    runtime: UNKNOWN

  freshness: null

  confidence_ceiling: 0

  status:
    PLACEHOLDER
```

---

# 56. GMEF completion state

```yaml
gmef:

  artifact:
    AMOS-CM-12-GENERATORS-GENERATOR-CONTRACT

  governance_status:
    PLACEHOLDER

  governed_operations:
    - GENERATOR_REGISTRATION
    - GENERATION
    - MATERIALIZATION
    - GENERATOR_UPDATE
    - GENERATED_ARTIFACT_PROMOTION

  authority_state:
    UNBOUND

  policy_epoch:
    UNKNOWN

  required_invariants:
    - I-GEN-001
    - I-GEN-002
    - I-GEN-003
    - I-GEN-004
    - I-GEN-005
    - I-GEN-012
    - I-GEN-014
    - I-GEN-015

  mutation_permission:
    UNKNOWN

  finality:
    UNFINALIZED
```

---

# 57. Generator proof capsule

```yaml
proof_capsule:

  conclusion:
    "A generation operation produced a candidate artifact."

  class:
    DERIVED

  does_not_prove:
    - correctness
    - empirical truth
    - canon status
    - authority
    - runtime activation
    - external commit

  load_bearing_premises:
    - generator identity known
    - generator version known
    - input specification known
    - output hash known

  invalidation_conditions:
    - input provenance invalid
    - generator version invalid
    - output hash mismatch
    - dependency incompatibility
```

---

# 58. Generator capability matrix

```yaml
capabilities:

  allowed_by_default:
    - read_declared_inputs
    - resolve_declared_templates
    - produce_candidate
    - compute_hash
    - attach_provenance
    - run_non_authoritative_validation
    - emit_receipt

  forbidden_by_default:
    - canon_admission
    - policy_activation
    - authority_creation
    - irreversible_effect
    - secret_access
    - silent_overwrite
    - silent_delete
    - finality_declaration
```

---

# 59. Security considerations

Generators can become supply-chain attack surfaces.

Risks include:

```text
malicious template
poisoned schema
dependency substitution
path traversal
arbitrary code emission
credential leakage
hidden prompt/template injection
provenance stripping
generated backdoor
artifact overwrite
version confusion
```

Required controls should eventually include:

```text
template trust
dependency pinning
path restrictions
content scanning
secret scanning
sandboxing
signed manifests where applicable
hash verification
least privilege
```

Exact security mechanisms remain `UNKNOWN/GAP` until the real runtime contract is recovered.

---

# 60. Data and privacy boundary

A generator should use only data explicitly available to its scope.

```text
GeneratorAccess
<= GrantedInputScope
```

It must not infer authority to access:

```text
private files
credentials
personal data
external systems
hidden runtime state
```

merely because a requested artifact could benefit from them.

---

# 61. Resource governance

Generator invocations should eventually declare resource limits.

```yaml
resource_budget:

  max_input_bytes: UNKNOWN
  max_output_bytes: UNKNOWN
  max_dependency_depth: UNKNOWN
  max_generation_time: UNKNOWN
  max_retry_count: UNKNOWN
  max_artifact_count: UNKNOWN
```

Resource limits must not silently weaken integrity checks.

---

# 62. Observability

A generation trace should expose:

```text
request received
generator resolved
input versions
template version
dependency resolution
generation start/end
candidate hash
validation results
materialization result
errors
rollback
```

Observability should permit reconstruction without leaking protected inputs.

---

# 63. Metrics

Potential metrics:

```text
generation_success_rate
candidate_rejection_rate
schema_failure_rate
semantic_failure_rate
stale_generation_rate
conflict_rate
rollback_rate
duplicate_prevention_rate
provenance_completeness
mean_generation_latency
mean_validation_latency
```

Metrics are operational observations, not proof of correctness.

---

# 64. Compatibility

Generator compatibility should include:

```yaml
compatibility:

  amos_core:
    target: v4.4
    validated: false

  architecture:
    version: UNKNOWN
    validated: false

  schema:
    version: UNKNOWN
    validated: false

  policy:
    epoch: UNKNOWN
    validated: false

  runtime:
    environment: UNKNOWN
    validated: false
```

---

# 65. Versioning

A generator version should change when load-bearing semantics change.

Potential classes:

```text
PATCH
= implementation repair preserving contract

MINOR
= backward-compatible capability extension

MAJOR
= contract or semantic incompatibility
```

AMOS-specific version rules remain to be recovered from canon if they exist.

---

# 66. Supersession

A generator should never silently replace another generator.

```yaml
supersession:

  predecessor_generator: UNKNOWN
  successor_generator: UNKNOWN

  compatibility:
    UNKNOWN

  migration_required:
    UNKNOWN

  rollback_target:
    UNKNOWN

  validation_receipt:
    UNKNOWN
```

---

# 67. Generator-to-generator composition

Generators may compose:

```text
Contract Generator
    ↓
Schema Generator
    ↓
Validator Generator
    ↓
Registry Generator
```

But composition creates dependency coupling.

Each generated descendant must retain ancestry to all load-bearing generators/templates.

---

# 68. Circular-generation prohibition

A generator dependency graph should reject unresolved cycles such as:

```text
Generator A
requires output from Generator B

Generator B
requires output from Generator A
```

unless a formally defined fixed-point protocol exists.

Default:

```text
UNRESOLVED_GENERATION_CYCLE
→ FAIL CLOSED
```

---

# 69. Placeholder-specific contract

For placeholder generation:

```yaml
placeholder:

  must_include:
    - status
    - conclusion_class
    - purpose
    - required_completion_fields
    - hard_boundaries
    - rscf_completion_state

  default_status:
    PLACEHOLDER

  default_conclusion:
    UNKNOWN/GAP

  must_not_include:
    - invented canon
    - invented evidence
    - fabricated implementation status
    - fabricated validation receipts
```

---

# 70. Matrix integration

Within the Cognitive Matrix, `12_GENERATORS` should relate to:

```text
CELL_REGISTRY
CELL_CONTRACTS
ROUTING
VALIDATION
STRUCTURAL_GAPS
MODE_REGISTRY
PACKAGE_CONTRACTS
MANIFESTS
```

Expected role:

```text
MANIFEST
→ identifies required structure

GENERATOR
→ materializes candidate structure

VALIDATOR
→ checks candidate

REGISTRY
→ records accepted identity/status

CONTROL PLANE
→ governs promotion
```

---

# 71. Cell-generation boundary

If generators create cognitive-matrix cells:

```text
CELL_GENERATED
!= CELL_VALIDATED
```

Each cell should separately require:

```text
binding validation
dependency validation
mode validation
H/M/L validation
provenance validation
contract validation
```

This is especially important where a cell registry contains `UNVALIDATED_BINDING` or structural-gap states.

---

# 72. Mode-generation boundary

If a generator creates mode placeholders:

```text
MODE_FOLDER_EXISTS
!= MODE_DEFINED

MODE_FILE_EXISTS
!= MODE_VALIDATED

MODE_VALIDATED
!= MODE_ACTIVE
```

Mode activation requires separate governance.

---

# 73. Generated-code boundary

Generated code must remain candidate implementation until:

```text
syntax
+ static checks
+ tests
+ security review
+ dependency review
+ runtime validation
+ authority
```

have passed at the required level.

```text
CODE_GENERATED
!= CODE_SAFE
```

---

# 74. Generated-policy boundary

Policy generation has the highest epistemic/governance burden.

```text
POLICY_GENERATED
!= POLICY_APPROVED
!= POLICY_ACTIVE
```

No generator can change active authority by editing policy text.

---

# 75. Generated-canon boundary

```text
CANON_CANDIDATE_GENERATED
        ↓
PROVENANCE
        ↓
CONTRADICTION ANALYSIS
        ↓
SCOPE / REGIME
        ↓
AUTHORITY
        ↓
CANON ADMISSION
```

Generator output is only the first stage.

---

# 76. Completion criteria

This placeholder may be promoted only after all load-bearing fields are recovered or explicitly specified.

```yaml
completion_gate:

  source_canon_references:
    required: true
    status: MISSING

  definition_scope:
    required: true
    status: PARTIAL_MODEL_ONLY

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
    status: UNKNOWN

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

  provenance:
    required: true
    status: MISSING

  uncertainty:
    required: true
    status: PRESENT

  failure_modes:
    required: true
    status: MODEL_DRAFT

  repair:
    required: true
    status: MODEL_DRAFT

  tests:
    required: true
    status: MODEL_DRAFT

  falsifiers:
    required: true
    status: PRESENT

  runtime_validation:
    required: true
    status: NOT_RUN

  authority_binding:
    required: true
    status: UNBOUND
```

---

# 77. Gap registry

```yaml
gaps:

  CRITICAL:
    - authoritative source/canon references for generator subsystem
    - actual generator registry
    - actual control-plane binding
    - actual runtime implementation
    - actual validation evidence

  DECISION_RELEVANT:
    - generator classes
    - protocol definitions
    - versioning semantics
    - resource budgets
    - security model

  EXPLANATORY:
    - additional diagrams
    - examples
    - performance metrics

  COSMETIC:
    - naming harmonization
    - formatting refinements
```

---

# 78. Related artifacts

Potential related artifacts should be linked rather than assumed.

```yaml
related:

  parent:
    - 25_COGNITIVE_MATRIX
    - 12_GENERATORS

  likely_dependencies:
    - MATRIX_MANIFEST
    - CELL_REGISTRY
    - CELL_CONTRACTS
    - VALIDATION
    - STRUCTURAL_GAPS
    - MODE_REGISTRY

  governance:
    - AUTHORITATIVE_STATE.md
    - POLICY_MANIFEST
    - PROVENANCE_MANIFEST

  core:
    - AMOS_CORE_v4_4

  relationship_status:
    UNVERIFIED
```

---

# 79. Related tag ontology

```text
Identity:
#AMOS
#AMOS_OS
#AMOS_CORE
#CognitiveMatrix
#Generator

Architecture:
#GeneratorContract
#MatrixInfrastructure
#ControlPlane
#Kernel
#Engine
#Skill
#Agent
#Worker
#Workflow

Knowledge:
#RSCF
#GMEF
#HML
#Canon
#Provenance
#Schema
#Template

Governance:
#Authority
#Policy
#Invariant
#Validation
#Promotion
#Finality
#Supersession

State:
#MVCC
#CAS
#ReadSet
#WriteSet
#Idempotency
#Replay
#Rollback

Epistemic:
#UnknownGap
#Placeholder
#Model
#Conditional
#Competing
#ConfidenceCeiling

Integrity:
#AntiFabrication
#AntiRegression
#SelectiveInvalidation
#ScopeFirewall
#RegimeFirewall
#Freshness
```

---

# 80. Hard boundaries

```text
PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

GENERATED != CORRECT

SCHEMA_VALID != SEMANTICALLY_VALID

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

CANDIDATE != CANON

MATERIALIZED != PROMOTED

SIMULATED != EXECUTED

VALIDATED != FINALIZED

UNKNOWN/GAP != PASS

DUPLICATED != INDEPENDENT

RECENT != AUTHORITATIVE
```

---

# 81. Current decision

```yaml
decision:

  accept_as_authoritative_generator_contract:
    false

  current_role:
    STRUCTURAL_PLACEHOLDER

  current_epistemic_class:
    UNKNOWN/GAP

  safe_use:
    - reserve architecture surface
    - guide future generator implementation
    - expose missing dependencies
    - define anti-overclaim boundaries
    - support structural audits

  unsafe_use:
    - claim generator subsystem implemented
    - activate generated artifacts
    - self-admit canon
    - grant execution authority
    - overwrite validated artifacts
```

---

# 82. Final proof capsule

**Claim**

`12_GENERATORS / GENERATOR_CONTRACT.md` defines the complete operative generator subsystem for AMOS.

**Current class**

`UNKNOWN/GAP`

**Why not VERIFIED**

No authoritative generator source, implementation evidence, runtime registry, policy binding, provenance set, or executed validation suite has been established in this artifact.

**What is established**

A structurally coherent AMOS-aligned placeholder contract can define the required boundaries and completion surface without inventing the missing generator implementation.

**Load-bearing gaps**

```text
source/canon
registry
runtime implementation
policy epoch
authority binding
validation receipts
protocols
provenance
```

**Competing possibility**

An existing AMOS generator specification elsewhere in the corpus may define materially different semantics.

**Falsifier**

Recovery of that authoritative specification.

**Confidence ceiling**

```text
0 for authoritative implementation claims

moderate for this file's usefulness
as a structural placeholder/model
```

**Final status**

```text
PLACEHOLDER
UNVALIDATED
UNKNOWN/GAP
NON_AUTHORITATIVE
```

```

This is the appropriate **full contract-level content**, but its actual status should remain `PLACEHOLDER / UNKNOWN-GAP`: it gives `12_GENERATORS` a complete AMOS architectural surface without pretending that the generator runtime, registry, protocols, validators, or authority bindings have already been recovered or implemented. The distinction follows the Full Brain OS requirement to expose missing dependencies rather than bridge them with fluent prose. :contentReference[oaicite:0]{index=0}
```
