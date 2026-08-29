---
title: GENERATOR TEMPLATES
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
- 00-root-moc
- amos-moc
- 00-home
- generators-map
- cognitive-matrix-moc
- amos-rscf-nodes
- generator-registry
- generator-seed
- generator-output
- generator-promotion
- generator-falsification
- generator-supersession
- task-contract
- task-resolver
- capability-resolver
- mode-admission-queue
- mode-composition-registry
- mode-conflict-registry
- mode-coverage-matrix
- mode-dependency-graph
- k-provenance
- k-sybil-hardening
- k-binding
- k-constraint-propagation
- k-gmef
- k-hml
- k-rscf
- k-counterfactual
- k-translation
- 12-generators-moc
canon-group: canon/cognitive-matrix
---

---title: "GENERATOR TEMPLATES"
type: document
tags: [note]
---


# Generator Templates

**STATUS:** CANDIDATE_CANON — SUBSTANTIVE SPECIFICATION
**Artifact Type:** Generator Template Library / Construction Contract
**System:** AMOS OS
**Path:** `25_COGNITIVE_MATRIX/12_GENERATORS/GENERATOR_TEMPLATES.md`
**Lineage Compatibility:** AMOS_CORE v3.0 → v4.4
**Origin Architect / Steward:** Trang Phan
**Claim Class:** `AMOS_MODEL`
**Implementation Status:** NOT ESTABLISHED BY THIS DOCUMENT
**Empirical Validation Status:** NOT ESTABLISHED BY THIS DOCUMENT
**Final Canon Status:** NOT ESTABLISHED BY THIS DOCUMENT

---

# 0. Template Declaration

Generator Templates define canonical structural patterns for constructing, declaring, validating, registering, executing, promoting, versioning, falsifying, and superseding AMOS generator artifacts.

A template is a specification pattern.

It is not an implemented generator.

It is not evidence that a generator satisfying the template behaves correctly.

It is not empirical validation.

It is not authorization for promotion.

It is not final canon merely because it appears in this file.

The governing distinction is:

$$\boxed{ Template \neq Implementation }$$

and:

$$\boxed{ Conformance \neq Validation }$$

A generator can structurally conform to a template while still being incorrect, unsafe, unsupported, incompatible, stale, or inappropriate for a particular scope or regime.

---

# 1. Purpose

`GENERATOR_TEMPLATES.md` exists to provide reusable structural contracts for generator artifacts while preserving AMOS requirements for:

- deterministic interpretation where determinism is required;
- explicit generator identity;
- explicit task binding;
- explicit input and output contracts;
- provenance preservation;
- evidence typing;
- scope and regime boundaries;
- dependency visibility;
- constraint propagation;
- competing hypotheses;
- falsification;
- confidence ceilings;
- uncertainty;
- versioning;
- promotion;
- supersession;
- rollback;
- RSCF integration;
- GMEF integration where applicable;
- H/M/L placement;
- auditability;
- anti-fabrication;
- repairability.

Templates exist to reduce accidental structural variance without erasing meaningful semantic differences between generators.

---

# 2. Core Template Law

Let:

$$T$$

be a generator template and:

$$G$$

a generator constructed using $T$.

Template conformance may establish:

$$Conforms(G,T)$$

It does not establish:

$$Correct(G)$$

or:

$$Validated(G)$$

or:

$$Promoted(G)$$

or:

$$Canonical(G)$$

Therefore:

$$\boxed{ Conforms(G,T) \not\Rightarrow Correct(G) }$$

$$\boxed{ Conforms(G,T) \not\Rightarrow Validated(G) }$$

$$\boxed{ Conforms(G,T) \not\Rightarrow Promoted(G) }$$

---

# 3. Template Roles

Generator templates MAY serve several roles:

```text
DECLARATION_TEMPLATE
CONTRACT_TEMPLATE
SEED_TEMPLATE
EXECUTION_TEMPLATE
OUTPUT_TEMPLATE
PROOF_CAPSULE_TEMPLATE
VALIDATION_TEMPLATE
FALSIFICATION_TEMPLATE
REGISTRY_TEMPLATE
PROMOTION_TEMPLATE
VERSIONING_TEMPLATE
SUPERSESSION_TEMPLATE
FAILURE_TEMPLATE
AUDIT_TEMPLATE
COMPOSITION_TEMPLATE
```

These roles SHOULD remain distinguishable.

---

# 4. Template Classes

AMOS generator templates are divided conceptually into:

```text
STRUCTURAL
SEMANTIC
EXECUTION
EPISTEMIC
GOVERNANCE
LINEAGE
RECOVERY
COMPOSITION
```

A single concrete template MAY combine multiple classes.

---

# 5. Structural Template

A structural template defines required fields and relationships.

Example:

```yaml
generator:
  identity: {}
  contract: {}
  inputs: {}
  outputs: {}
  dependencies: {}
  constraints: {}
```

Structural validity does not prove semantic validity.

---

# 6. Semantic Template

A semantic template specifies what fields mean.

For example:

```yaml
claim_class:
  allowed:
    - VERIFIED
    - DERIVED
    - MODEL
    - CONDITIONAL
    - COMPETING
    - UNKNOWN/GAP
```

The field must not merely exist.

Its value must satisfy its semantic contract.

---

# 7. Execution Template

An execution template defines the conceptual generator execution lifecycle:

```text
TASK
  ↓
RESOLVE
  ↓
BIND
  ↓
CHECK
  ↓
GENERATE
  ↓
VALIDATE
  ↓
PACKAGE
  ↓
RETURN
```

This document does not establish that a literal runtime executes these stages.

---

# 8. Epistemic Template

An epistemic template governs:

```text
claim typing
evidence typing
provenance
confidence ceilings
scope
regime
freshness
competing explanations
falsifiers
uncertainty
```

It exists to prevent fluent generator output from being mistaken for stronger knowledge than its evidence supports.

---

# 9. Governance Template

A governance template governs transitions such as:

```text
DRAFT
→
CANDIDATE
→
VALIDATED
→
PROMOTED
→
ACTIVE
→
DEPRECATED
→
SUPERSEDED
```

Lifecycle names are models unless established by applicable canon or implementation evidence.

---

# 10. Lineage Template

A lineage template preserves:

```text
generator identity
version
seed
dependencies
inputs
outputs
transformations
promotion history
supersession history
```

so later artifacts can reconstruct how an output was produced.

---

# 11. Recovery Template

Recovery templates define behavior when generation fails.

Core principle:

$$Failure(P) \Rightarrow Invalidate(Dependent(P))$$

not:

$$Failure(P) \Rightarrow Invalidate(All)$$

---

# 12. Composition Template

Composition templates define how multiple generators MAY cooperate without losing individual identity.

Example:

```text
G1
 ├──→ G3
G2
 ┘
```

Composition does not automatically merge provenance or confidence.

---

# 13. Canonical Generator Skeleton

The baseline generator declaration SHOULD conceptually contain:

```yaml
generator:

  identity: {}

  metadata: {}

  purpose: {}

  task_contract: {}

  capability_requirements: {}

  mode_requirements: {}

  input_contract: {}

  seed_contract: {}

  output_contract: {}

  dependencies: {}

  constraints: {}

  scope: {}

  regime: {}

  provenance: {}

  execution: {}

  validation: {}

  falsification: {}

  uncertainty: {}

  governance: {}

  versioning: {}

  supersession: {}

  recovery: {}

  audit: {}

  rscf: {}
```

Not every generator requires every optional field.

The smallest sufficient structure SHOULD be preferred while retaining all decision-relevant information.

---

# 14. Template Identity

Every governed generator template SHOULD possess stable identity.

```yaml
template_identity:
  template_id: null
  template_name: null
  template_version: null
  template_hash: null
```

Where hashing is unavailable, the field SHOULD remain absent or unknown rather than fabricated.

---

# 15. Generator Identity Template

```yaml
identity:

  generator_id: null
  generator_name: null

  version: null
  hash: null

  family: null
  class: null

  template_id: null
  template_version: null
```

Identity fields SHOULD distinguish human-readable labels from stable machine-oriented identity.

---

# 16. Identity Invariant

Generator identity must not depend exclusively on mutable aliases.

Weak:

```yaml
generator: recommended
```

Strong:

```yaml
generator_id: causal_generator
version: 4.2
alias: recommended
```

---

# 17. Metadata Template

```yaml
metadata:

  title: null
  description: null

  created_at: null
  modified_at: null

  author_or_origin: null
  steward: null

  status: null

  tags: []
```

Unknown metadata MUST NOT be invented merely to complete the template.

---

# 18. Purpose Template

```yaml
purpose:

  objective: null

  solves:
    - null

  does_not_solve:
    - null

  intended_use:
    - null

  prohibited_use:
    - null
```

Explicit non-goals help prevent scope leakage.

---

# 19. Task Contract Template

```yaml
task_contract:

  accepted_task_classes: []

  required_fields: []

  optional_fields: []

  preconditions: []

  completion_conditions: []

  refusal_conditions: []

  escalation_conditions: []
```

Task binding SHOULD be resolved through the applicable task-resolution architecture.

---

# 20. Capability Requirement Template

```yaml
capability_requirements:

  required: []

  optional: []

  forbidden: []

  fallback: []

  unresolved_policy:
    action: BLOCK_OR_ESCALATE
```

A generator MUST NOT silently assume unavailable capabilities.

---

# 21. Mode Requirement Template

```yaml
mode_requirements:

  required_modes: []

  optional_modes: []

  prohibited_modes: []

  compositions: []

  conflicts: []

  admission_required: true
```

Applicable mode constraints SHOULD be resolved against the mode registries.

---

# 22. Input Contract Template

```yaml
input_contract:

  schema_version: null

  required:
    - field: null
      type: null

  optional: []

  defaults: []

  validation: []

  normalization: []

  prohibited_inputs: []

  unknown_input_policy: null
```

---

# 23. Input Integrity Law

Input normalization MUST NOT silently change decision-relevant semantics.

If:

$$Normalize(x)=x'$$

and $x'$ changes the task meaning, the transformation must be surfaced or rejected.

---

# 24. Seed Contract Template

```yaml
seed_contract:

  seed_schema: null

  deterministic_seed_required: null

  seed_fields: []

  defaults: []

  entropy_sources: []

  provenance_required: true

  replay_supported: null
```

See:

`GENERATOR_SEED.md`

for the dedicated seed specification.

---

# 25. Deterministic Generator Template

Where determinism is required:

```yaml
determinism:

  required: true

  deterministic_inputs: []

  deterministic_dependencies: []

  fixed_configuration: {}

  randomness:
    allowed: false

  replay:
    expected_equivalence: EXACT
```

---

# 26. Controlled-Stochastic Generator Template

Where stochastic behavior is legitimate:

```yaml
determinism:

  required: false

  randomness:
    allowed: true
    seedable: null
    entropy_source: null

  replay:
    expected_equivalence: DISTRIBUTIONAL_OR_CONTRACTUAL
```

A stochastic generator MUST NOT be represented as deterministic merely because one execution happened to reproduce another.

---

# 27. Output Contract Template

```yaml
output_contract:

  schema_version: null

  required_fields: []

  optional_fields: []

  claim_classes: []

  provenance_fields: []

  uncertainty_fields: []

  validation_fields: []

  failure_fields: []

  serialization: null
```

---

# 28. Generator Output Envelope

Recommended conceptual envelope:

```yaml
generator_output:

  output_id: null

  generator:
    id: null
    version: null
    hash: null

  task_ref: null
  seed_ref: null

  content: null

  claim_class: null

  evidence: []

  provenance: []

  scope: {}

  regime: {}

  uncertainty: {}

  competing: []

  falsifiers: []

  validation: {}

  generated_at: null
```

---

# 29. Claim-Class Template

Important generator conclusions SHOULD use the weakest accurate class:

```text
VERIFIED
DERIVED
MODEL
CONDITIONAL
COMPETING
UNKNOWN/GAP
```

A template MUST NOT force a stronger classification merely because a field requires a value.

---

# 30. Evidence-Type Template

Evidence SHOULD distinguish:

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
evidence:
  - evidence_id: E1
    type: OBSERVATION
    source_ref: null
    content_ref: null
```

---

# 31. Provenance Template

```yaml
provenance:

  sources: []

  source_identity: []

  ancestry: []

  transformations: []

  dependencies: []

  correlation_risks: []

  independence:
    status: UNKNOWN
    evidence: []

  freshness: {}
```

---

# 32. Provenance Independence Rule

Multiple references do not imply multiple independent origins.

$$ReferenceCount \neq IndependentEvidenceCount$$

Independence must be demonstrated when it materially affects confidence.

---

# 33. Sybil-Hardening Template

```yaml
sybil_hardening:

  source_clusters: []

  shared_ancestry: []

  duplicate_claims: []

  correlated_sources: []

  independence_verified: false

  unresolved_risks: []
```

Repeated descendants of one source MUST NOT be counted as independent confirmation.

---

# 34. Scope Template

```yaml
scope:

  system: []

  population: []

  environment: []

  scale: []

  task_class: []

  domain: []

  measurement_method: []

  assumptions: []
```

---

# 35. Scope Firewall

Generator conclusions inherit their applicability envelope.

A generator validated for:

```text
domain A
environment E1
scale S1
```

is not automatically validated for:

```text
domain B
environment E2
scale S2
```

---

# 36. Regime Template

```yaml
regime:

  regime_id: null

  environment: {}

  operating_conditions: {}

  measurement_conditions: {}

  assumptions: []

  transition_indicators: []
```

---

# 37. Regime Shift Template

```yaml
regime_shift:

  previous_regime: null
  new_regime: null

  detected_by: []

  invalidated_premises: []

  affected_outputs: []

  revalidation_required: []
```

---

# 38. Temporal Validity Template

```yaml
temporal_validity:

  observed_at: null

  valid_from: null

  valid_until: null

  freshness_window: null

  refresh_conditions: []
```

Freshness requirements SHOULD reflect how quickly the underlying fact or dependency can change.

---

# 39. Dependency Template

```yaml
dependencies:

  required: []

  optional: []

  transitive: []

  dependency_closure:
    status: UNKNOWN

  unresolved: []
```

---

# 40. Dependency Entry Template

```yaml
dependency:

  dependency_id: null

  type: null

  version: null

  hash: null

  required: true

  scope: {}

  compatibility: null

  provenance_ref: null
```

---

# 41. Dependency Closure Law

A generator cannot safely be reasoned about locally when unknown transitive dependencies could alter the conclusion.

Fast-path local execution requires sufficient dependency closure.

---

# 42. Constraint Template

```yaml
constraints:

  inherited: []

  local: []

  hard: []

  soft: []

  conditional: []

  conflicts: []

  propagation_state: null
```

---

# 43. Constraint Inheritance

A child generator cannot silently weaken inherited hard constraints.

Conceptually:

$$C_{parent} \Rightarrow C_{child}$$

unless an authorized governance transition explicitly changes the governing contract.

---

# 44. Binding Template

```yaml
binding:

  task_ref: null

  generator_ref: null

  capability_bindings: []

  mode_bindings: []

  dependency_bindings: []

  constraint_bindings: []

  scope_binding: {}

  regime_binding: {}

  status: null
```

---

# 45. Execution Context Template

```yaml
execution_context:

  execution_id: null

  task_ref: null

  generator_ref: null

  seed_ref: null

  epoch: null

  scope: {}

  regime: {}

  dependencies: []

  constraints: []

  capabilities: []

  modes: []
```

---

# 46. Generator Execution Template

```text
1. ACCEPT TASK
2. VALIDATE TASK CONTRACT
3. RESOLVE GENERATOR
4. RESOLVE CAPABILITIES
5. RESOLVE MODES
6. LOAD REQUIRED DEPENDENCIES
7. PROPAGATE CONSTRAINTS
8. BIND SCOPE / REGIME
9. RESOLVE SEED
10. EXECUTE GENERATION
11. CLASSIFY OUTPUT
12. ATTACH PROVENANCE
13. VALIDATE
14. FALSIFY WHERE REQUIRED
15. PACKAGE OUTPUT
16. COMMIT / RETURN
```

The exact runtime sequence may differ if later canon establishes another implementation.

---

# 47. Minimal Generator Template

For low-complexity generators:

```yaml
generator:

  id: null
  version: null

  purpose: null

  inputs: []
  outputs: []

  dependencies: []

  constraints: []

  claim_class: AMOS_MODEL

  provenance: []

  status: DRAFT
```

Use only where omitted fields cannot materially alter integrity.

---

# 48. Standard Generator Template

```yaml
generator:

  identity:
    id: null
    version: null

  purpose:
    objective: null

  task_contract: {}

  input_contract: {}

  seed_contract: {}

  output_contract: {}

  dependencies: {}

  constraints: {}

  scope: {}

  regime: {}

  provenance: {}

  validation: {}

  falsification: {}

  versioning: {}

  governance: {}
```

---

# 49. Maximum Generator Template

```yaml
amos_generator:

  schema:
    generator_schema_version: null
    template_id: null
    template_version: null

  identity:
    generator_id: null
    generator_name: null
    family: null
    class: null
    version: null
    hash: null

  metadata:
    description: null
    created_at: null
    modified_at: null
    origin: null
    steward: null
    tags: []

  purpose:
    objective: null
    intended_use: []
    non_goals: []
    prohibited_use: []

  task_contract:
    accepted_task_classes: []
    preconditions: []
    completion_conditions: []
    escalation_conditions: []

  capability_requirements:
    required: []
    optional: []
    forbidden: []
    fallback: []

  mode_requirements:
    required: []
    optional: []
    prohibited: []
    compositions: []
    conflicts: []

  input_contract:
    schema_version: null
    required: []
    optional: []
    defaults: []
    validation: []
    normalization: []

  seed_contract:
    schema_version: null
    required_fields: []
    deterministic: null
    replay_supported: null

  output_contract:
    schema_version: null
    required_fields: []
    claim_classes: []
    provenance_required: true
    uncertainty_required: null

  dependencies:
    direct: []
    transitive: []
    closure_status: UNKNOWN

  constraints:
    inherited: []
    local: []
    hard: []
    soft: []
    conditional: []
    conflicts: []

  scope:
    system: []
    population: []
    environment: []
    scale: []
    domain: []
    task_class: []
    assumptions: []

  regime:
    regime_id: null
    conditions: {}
    transition_indicators: []

  temporal_validity:
    valid_from: null
    valid_until: null
    freshness_window: null

  provenance:
    sources: []
    ancestry: []
    transformations: []
    correlation_risks: []
    independence_status: UNKNOWN

  execution:
    strategy: null
    deterministic: null
    stages: []
    termination_conditions: []

  epistemics:
    evidence_types: []
    claim_classes: []
    confidence_model: null
    confidence_ceiling: null

  competing_hypotheses:
    supported: true
    hypotheses: []
    discriminating_tests: []

  causal:
    causal_claims_allowed: null
    evidence_requirements: []
    confounders: []
    mediators: []
    mechanisms: []

  validation:
    required: true
    tests: []
    invariants: []
    status: NOT_RUN

  falsification:
    required: null
    tests: []
    falsifiers: []
    status: NOT_RUN

  sensitivity:
    critical_premises: []
    thresholds: []
    flip_conditions: []
    robustness: UNKNOWN

  uncertainty:
    evidence: null
    model: null
    scope: null
    temporal: null
    causal: null
    execution: null
    provenance_independence: null

  failure:
    classes: []
    recovery: []
    retry_policy: null

  governance:
    lifecycle_state: DRAFT
    promotion_required: true
    authority: null

  versioning:
    version: null
    predecessor: null
    compatibility: UNKNOWN

  supersession:
    supersedes: []
    superseded_by: []
    scope: {}
    regime: {}

  audit:
    execution_logging: null
    provenance_logging: null
    validation_logging: null

  rscf:
    node_id: null
    relations: []

  gmef:
    bindings: []
```

---

# 50. Proof Capsule Template

Important generator conclusions SHOULD conceptually support:

```yaml
proof_capsule:

  capsule_id: null

  claim:
    content: null
    class: null

  load_bearing_premises: []

  evidence: []

  provenance: []

  scope: {}

  regime: {}

  temporal_validity: {}

  dependencies: []

  competing_explanations: []

  falsifiers: []

  invalidation_conditions: []

  uncertainty:
    evidence: null
    model: null
    scope: null
    temporal: null
    causal: null
    execution: null
    provenance_independence: null

  confidence_ceiling: null
```

---

# 51. Proof Capsule Reuse Rule

A proof capsule may be reused only while its:

```text
dependencies
scope
regime
freshness
premises
provenance requirements
```

remain valid.

---

# 52. Proof Capsule Invalidation

If premise $P$ fails:

```text
P
├── C1
└── C2
```

then invalidate:

```text
C1
C2
```

not unrelated conclusions.

---

# 53. Confidence Template

```yaml
confidence:

  value: null

  ceiling: null

  load_bearing_premises: []

  independently_revalidated: []

  limiting_premise: null
```

Derived confidence MUST NOT exceed the weakest load-bearing premise unless the dependency has been independently revalidated under the applicable confidence model.

---

# 54. Competing Hypothesis Template

```yaml
competing_hypotheses:

  - hypothesis_id: H1
    claim: null
    support: []
    falsifiers: []

  - hypothesis_id: H2
    claim: null
    support: []
    falsifiers: []

  discrimination:
    cheapest_high_information_test: null

  state: COMPETING
```

---

# 55. Competition Law

When incompatible hypotheses have:

```text
equal support
incomparable support
correlated support
insufficient support
```

AMOS MUST NOT force convergence.

Return:

```text
COMPETING
```

until discriminating evidence exists.

---

# 56. Causal Generator Template

For generators permitted to produce causal reasoning:

```yaml
causal_contract:

  association_allowed: true

  causal_effect_claims:
    allowed: null

  required_evidence_types: []

  mechanism: []

  enabling_conditions: []

  necessary_conditions: []

  sufficient_conditions: []

  mediators: []

  confounders: []

  feedback: []

  interventions: []

  counterfactual_support: []
```

---

# 57. Causal Firewall

The following alone do not establish causation:

```text
analogy
sequence
co-occurrence
correlation
structural resemblance
```

A generator MUST preserve this distinction.

---

# 58. Counterfactual Generator Template

```yaml
counterfactual:

  factual_world: {}

  intervention:
    variable: null
    from: null
    to: null

  held_constant: []

  causal_model_ref: null

  alternative_world: {}

  outcome_difference: null

  assumptions: []

  uncertainty: {}

  falsifiers: []
```

Counterfactual conclusions cannot exceed the causal support of the underlying model.

---

# 59. Translation Generator Template

```yaml
translation:

  source:
    representation: null
    semantics: null
    scope: {}

  target:
    representation: null
    semantics: null
    scope: {}

  invariant_requirements: []

  lossy_dimensions: []

  ambiguity: []

  validation: []

  reverse_check: null
```

Structural similarity between representations does not establish semantic equivalence.

---

# 60. Synthesis Generator Template

```yaml
synthesis:

  inputs: []

  provenance_clusters: []

  independent_support: []

  contradictions: []

  competing_claims: []

  synthesis_rules: []

  output_claims: []

  unresolved: []
```

Contradictions MUST NOT be silently averaged away.

---

# 61. Evidence Synthesis Template

```text
SOURCE CLAIMS
      ↓
PROVENANCE TOPOLOGY
      ↓
INDEPENDENCE CHECK
      ↓
CONTRADICTION CHECK
      ↓
SCOPE / REGIME CHECK
      ↓
SYNTHESIS
      ↓
CLAIM CLASSIFICATION
```

---

# 62. Retrieval Generator Template

```yaml
retrieval:

  objective: null

  required_scope: null

  retrieval_depth:
    bootstrap: true
    H: null
    M: null
    L: null
    raw_evidence: DO_NOT_LOAD_UNLESS_REQUIRED

  dependency_targets: []

  stopping_conditions: []

  provenance_required: true
```

---

# 63. H/M/L Retrieval Law

Default traversal:

```text
BOOTSTRAP CAPSULE
      ↓
H DOMAIN
      ↓
M SUBSYSTEM
      ↓
L DETAIL
      ↓
RAW EVIDENCE
```

Raw evidence SHOULD remain:

```text
DO_NOT_LOAD_UNLESS_REQUIRED
```

until required by decision-changing uncertainty.

---

# 64. RSCF Generator Template

```yaml
rscf_generator:

  node_id: null

  node_type: generator

  claim_class: AMOS_MODEL

  inputs: []

  outputs: []

  dependencies: []

  relations:
    indexed_by: []
    part_of: []
    governed_by: []
    depends_on: []
    produces: []
    validates_with: []
    supersedes: []
```

---

# 65. Recursive RSCF Template

A generator MAY recursively resolve:

```text
RSCF
 ↓
H
 ↓
M
 ↓
L
```

only to the depth needed to establish sufficient dependency closure.

Unnecessary traversal SHOULD be avoided.

---

# 66. GMEF Binding Template

Where a generator participates in GMEF:

```yaml
gmef_binding:

  generator_ref: null

  environment_ref: null

  model_ref: null

  evidence_ref: []

  constraints: []

  scope: {}

  regime: {}

  validity: null
```

This document does not establish GMEF implementation beyond the applicable AMOS corpus.

---

# 67. Atomic Multi-RSCF Template

```yaml
atomic_multi_rscf:

  transaction_id: null

  nodes: []

  preconditions: []

  shared_constraints: []

  commit_condition: null

  rollback_condition: null

  status: null
```

Use when partial reasoning-state transition would create an invalid intermediate state.

---

# 68. MVCC-Style Template

Where AMOS reasoning uses MVCC concepts:

```yaml
mvcc:

  snapshot_id: null

  base_version: null

  read_set: []

  write_set: []

  conflict_check: null

  commit_state: null
```

This is an architectural reasoning pattern and does not claim literal database MVCC implementation.

---

# 69. CAS-Style Template

```yaml
compare_and_swap:

  expected_state: null

  proposed_state: null

  comparison: null

  on_match: COMMIT

  on_mismatch: REVALIDATE
```

Again, this describes an AMOS coordination concept, not necessarily a literal machine CAS primitive.

---

# 70. Causal Epoch Template

```yaml
causal_epoch:

  epoch_id: null

  predecessor_epoch: null

  generator_state: []

  finalized: false

  finalization_evidence: []

  invalidation_conditions: []
```

---

# 71. Fast-Path Template

```yaml
fast_path:

  dependency_closure_established: false

  provenance_independence_established: false

  scope_compatible: false

  regime_compatible: false

  freshness_valid: false

  non_conflict_established: false

  irreversible_stakes: false

  governance_impact: false

  admitted: false
```

---

# 72. Fast-Path Admission Law

Fast path is admitted only if all load-bearing admission conditions are established.

Unknown is not equivalent to true.

---

# 73. Escalation Template

```yaml
escalation:

  triggers:
    - shared_ancestry
    - contradiction
    - stale_evidence
    - regime_crossing
    - causal_coupling
    - governance_impact
    - irreversible_stakes
    - ambiguous_dependency

  destination: null
```

---

# 74. Validation Template

```yaml
validation:

  validation_id: null

  generator_ref: null

  contract_checks: []

  invariant_checks: []

  regression_checks: []

  provenance_checks: []

  scope_checks: []

  regime_checks: []

  dependency_checks: []

  security_checks: []

  result: null

  failures: []
```

---

# 75. Validation Result Classes

```text
PASS
PASS_CONDITIONALLY
FAIL
INCONCLUSIVE
NOT_RUN
UNKNOWN/GAP
```

`INCONCLUSIVE` MUST NOT be silently converted to `PASS`.

---

# 76. Falsification Template

```yaml
falsification:

  falsification_id: null

  target_claims: []

  target_invariants: []

  adversarial_paths: []

  contradiction_tests: []

  correlated_provenance_tests: []

  stale_premise_tests: []

  scope_leakage_tests: []

  hidden_dependency_tests: []

  causal_overreach_tests: []

  alternative_hypothesis_tests: []

  result: null
```

---

# 77. Adversarial Validation Template

For consequential generator conclusions:

```text
BUILD STRONGEST SUPPORTED CONCLUSION
                 ↓
        INDEPENDENT CHALLENGE
                 ↓
     SEARCH FOR FAILURE MODES
                 ↓
       SURVIVES? / FAILS?
          /             \
        YES             NO
         ↓               ↓
      RETAIN      DOWNGRADE /
                  CONDITION /
                  COMPETING /
                  UNKNOWN
```

---

# 78. Sensitivity Template

```yaml
sensitivity:

  conclusion_ref: null

  load_bearing_premises: []

  thresholds: []

  assumptions: []

  smallest_flip_condition: null

  perturbations: []

  result:
    robustness: UNKNOWN
```

---

# 79. Fragility Rule

If a small plausible perturbation flips the output:

```text
CONDITIONAL
```

is preferred over an unconditional conclusion.

---

# 80. Failure Template

```yaml
generator_failure:

  failure_id: null

  execution_id: null

  generator_ref: null

  class: null

  failed_premise: null

  failed_dependency: null

  failed_constraint: null

  affected_outputs: []

  recoverability: null

  candidate_repairs: []

  provenance: []
```

---

# 81. Failure Classes

Candidate classes:

```text
INVALID_INPUT
UNSATISFIED_TASK_CONTRACT
MISSING_CAPABILITY
MODE_CONFLICT
DEPENDENCY_MISSING
DEPENDENCY_STALE
DEPENDENCY_CONFLICT
CONSTRAINT_VIOLATION
PROVENANCE_INSUFFICIENT
SCOPE_MISMATCH
REGIME_MISMATCH
CAUSAL_SUPPORT_INSUFFICIENT
VALIDATION_FAILURE
FALSIFICATION_FAILURE
OUTPUT_CONTRACT_FAILURE
GOVERNANCE_BLOCK
UNKNOWN_FAILURE
```

---

# 82. Failure Recovery Template

```text
FAILURE
  ↓
LOCALIZE
  ↓
IDENTIFY FAILED PREMISE / EDGE
  ↓
INVALIDATE DEPENDENTS
  ↓
ROLL BACK
  ↓
REROUTE / REPAIR
  ↓
REVALIDATE
```

---

# 83. Retry Template

```yaml
retry:

  previous_failure_ref: null

  changed_conditions: []

  changed_evidence: []

  changed_dependencies: []

  changed_configuration: []

  retry_allowed: null
```

A failed path SHOULD NOT be repeated without a material change.

---

# 84. Registry Entry Template

```yaml
generator_registry_entry:

  generator_id: null
  name: null
  family: null
  class: null

  active_version: null

  available_versions: []

  lifecycle_state: null

  task_classes: []

  capabilities: []

  modes: []

  scope: {}

  regime: {}

  provenance_ref: null

  validation_ref: null

  promotion_ref: null

  supersession_ref: null
```

---

# 85. Promotion Template

```yaml
promotion:

  promotion_id: null

  generator_ref: null

  source_state: null
  target_state: null

  evidence: []

  validation: []

  falsification: []

  unresolved_gaps: []

  governance: {}

  decision: null
```

---

# 86. Promotion Law

Template completeness does not license promotion.

Promotion requires the evidence and governance demanded by the applicable Generator Promotion contract.

---

# 87. Version Template

```yaml
generator_version:

  generator_id: null

  version: null

  hash: null

  predecessor: null

  change_class: null

  changes: []

  compatibility: null

  migration_required: null

  validation_ref: null

  released_at: null
```

---

# 88. Version Change Classes

Candidate classes:

```text
PATCH
MINOR
MAJOR
SECURITY
PROVENANCE
CAUSAL
SCHEMA
DEPENDENCY
GOVERNANCE
EXPERIMENTAL
```

The labels do not themselves establish compatibility.

---

# 89. Supersession Template

```yaml
generator_supersession:

  supersession_id: null

  predecessor: null
  successor: null

  reason: null

  evidence: []

  provenance: []

  scope: {}

  regime: {}

  compatibility: {}

  migration: {}

  effective_boundary: {}

  rollback: {}

  validation: {}

  governance: {}
```

---

# 90. Supersession Law

$$Superseded \neq Erased$$

Historical outputs retain the identity of the generator that actually produced them.

---

# 91. Migration Template

```yaml
migration:

  migration_id: null

  source_generator: null
  target_generator: null

  source_schema: null
  target_schema: null

  transformations: []

  losses: []

  irreversible_changes: []

  validation: []

  rollback_supported: null
```

---

# 92. Rollback Template

```yaml
rollback:

  rollback_id: null

  source_state: null

  target_state: null

  trigger: null

  preconditions: []

  prohibited_conditions: []

  affected_outputs: []

  validation_required: true
```

---

# 93. Audit Template

```yaml
audit:

  event_id: null

  event_type: null

  generator_ref: null

  execution_ref: null

  timestamp: null

  inputs_ref: []

  seed_ref: null

  dependency_refs: []

  output_ref: null

  validation_refs: []

  provenance_refs: []

  governance_refs: []
```

---

# 94. Generator Composition Template

```yaml
composition:

  composition_id: null

  generators: []

  topology: null

  shared_inputs: []

  shared_constraints: []

  intermediate_outputs: []

  provenance_merge_policy: null

  confidence_merge_policy: null

  conflict_policy: null

  atomicity_required: null
```

---

# 95. Sequential Composition

```text
G1
 ↓
O1
 ↓
G2
 ↓
O2
```

G2's output depends on G1.

Therefore the dependency must remain explicit.

---

# 96. Parallel Composition

```text
      TASK
      /  \
     ↓    ↓
    G1    G2
     \    /
      ↓  ↓
     SYNTHESIS
```

Parallel execution does not imply evidence independence.

---

# 97. Competitive Composition

```text
TASK
 ├── G1 → H1
 └── G2 → H2
```

If H1 and H2 conflict, preserve the conflict until discriminating evidence exists.

---

# 98. Generator-of-Generators Template

A generator MAY produce candidate generator specifications.

```yaml
generator_generator:

  parent_generator_ref: null

  output_type: GENERATOR_CANDIDATE

  candidate_template_ref: null

  inherited_constraints: []

  validation_required: true

  promotion_required: true
```

Generated generators are candidates.

They are not automatically trusted.

---

# 99. Recursive Generation Firewall

A generator that produces another generator cannot grant the child more epistemic authority than its evidence and governance support.

$$Authority(G_{child}) \not> AuthorizedSupport(G_{child})$$

---

# 100. Self-Modification Template

Where generator evolution is modeled:

```yaml
self_modification:

  source_generator: null

  proposed_generator: null

  change_set: []

  reason: null

  validation: []

  falsification: []

  promotion_required: true

  supersession_required: null
```

Self-proposed modification does not self-authorize.

---

# 101. Governance Firewall

A generator MAY:

```text
propose
analyze
simulate
test
recommend
```

a governance transition.

It MUST NOT be treated as having governance authority unless such authority is independently established.

---

# 102. Anti-Fabrication Template

Every generator SHOULD preserve:

```yaml
anti_fabrication:

  missing_evidence_policy: EXPOSE_GAP

  unknown_dependency_policy: EXPOSE_OR_ESCALATE

  contradiction_policy: PRESERVE

  unsupported_causal_claim_policy: DOWNGRADE

  unsupported_scope_transfer_policy: REJECT_OR_CONDITION

  missing_canon_policy: DO_NOT_INVENT
```

---

# 103. Missing-Field Rule

A template field with unknown value should be:

```yaml
value: null
```

or:

```text
UNKNOWN
```

or omitted where optional.

It MUST NOT be populated with plausible-sounding fabricated content.

---

# 104. Gap Template

```yaml
gap:

  gap_id: null

  class: null

  missing_information: null

  blocks: []

  minimum_resolution: null

  status: OPEN
```

---

# 105. Gap Classes

```text
CRITICAL
DECISION_RELEVANT
EXPLANATORY
COSMETIC
```

Resolve in that order unless governance requires otherwise.

---

# 106. Critical Gap Law

If a critical gap blocks generator correctness:

```text
UNKNOWN/GAP
```

is preferable to fabricated completion.

---

# 107. Decision Sufficiency Template

```yaml
sufficiency:

  claim_sufficient: false
  decision_sufficient: false
  action_sufficient: false

  unresolved_decision_changing_uncertainty: []
```

Generation SHOULD stop when the required sufficiency level is reached.

---

# 108. Adaptive Complexity Template

```yaml
complexity:

  selected: C0

  levels:
    C0: DIRECT
    C1: COMPACT
    C2: STRUCTURED
    C3: DEEP
    C4: MAXIMUM

  escalation_triggers: []

  deescalation_conditions: []
```

---

# 109. Complexity Escalation

Escalate for material:

```text
stakes
irreversibility
novelty
weak evidence
stale evidence
contradiction
causal ambiguity
scope mismatch
competing models
governance impact
low trust
explicit depth requirement
```

---

# 110. Smallest Sufficient Proof Scope

Generators SHOULD use the smallest proof scope that can safely establish the requested conclusion.

Do not expand the dependency graph merely because additional material exists.

---

# 111. Template Specialization

A specialized template MAY inherit from a general template.

Example:

```text
GENERATOR_BASE
      ↓
CAUSAL_GENERATOR
      ↓
COUNTERFACTUAL_GENERATOR
```

Inherited constraints remain active unless explicitly superseded through governance.

---

# 112. Template Inheritance Object

```yaml
template_inheritance:

  template_id: null

  parent_templates: []

  inherited_fields: []

  overrides: []

  added_constraints: []

  removed_constraints: []

  removal_authorization: []
```

---

# 113. Multiple Template Inheritance

Where multiple templates are composed:

```text
T1 ─┐
    ├──→ T3
T2 ─┘
```

conflicting requirements MUST be resolved explicitly.

---

# 114. Template Conflict

Example:

```text
T1:
randomness forbidden

T2:
randomness required
```

Result:

```text
TEMPLATE_CONFLICT
```

unless a higher-level rule resolves the scope.

---

# 115. Template Compatibility Classes

```text
COMPATIBLE
CONDITIONALLY_COMPATIBLE
MIGRATION_REQUIRED
BREAKING
INCOMPATIBLE
UNKNOWN
```

---

# 116. Template Versioning

Templates themselves require version identity when used for governed generator construction.

```yaml
template_version:
  template_id: generator_base
  version: null
  predecessor: null
  changes: []
```

---

# 117. Template Supersession

A new template version does not retroactively change historical generators.

If:

```text
T1 → T2
```

a generator built under T1 remains historically associated with T1.

---

# 118. Template Migration

A generator MAY be migrated from template T1 to T2.

This is a new transformation event:

```text
G@T1
  ↓ MIGRATION
G'@T2
```

The original lineage must remain recoverable.

---

# 119. Template Validation

A template SHOULD itself be checked for:

```text
internal contradictions
missing required invariants
ambiguous semantics
unsafe defaults
scope leakage
unresolvable dependencies
governance conflicts
```

---

# 120. Template Falsification

A template may be falsified as adequate for a use case if it systematically permits:

```text
invalid outputs
provenance loss
constraint loss
scope leakage
causal overreach
unrecoverable lineage
unsafe promotion
```

---

# 121. Generator Template Invariants

```text
GTPL-I01
Template conformance does not establish generator correctness.

GTPL-I02
Template conformance does not establish empirical validation.

GTPL-I03
Template conformance does not authorize promotion.

GTPL-I04
Unknown fields are never fabricated for structural completeness.

GTPL-I05
Generator identity is explicit.

GTPL-I06
Historical generator identity is immutable.

GTPL-I07
Inputs and outputs are contract-bound.

GTPL-I08
Dependencies remain explicit when load-bearing.

GTPL-I09
Hard inherited constraints cannot be silently weakened.

GTPL-I10
Provenance is preserved across material transformations.

GTPL-I11
Evidence ancestry is distinguished from evidence independence.

GTPL-I12
Scope is explicit for consequential claims.

GTPL-I13
Regime validity is explicit where material.

GTPL-I14
Freshness is bounded where material.

GTPL-I15
Correlation does not automatically license causal inference.

GTPL-I16
Competing hypotheses remain competing without discriminating evidence.

GTPL-I17
Confidence cannot exceed load-bearing support.

GTPL-I18
Critical gaps remain visible.

GTPL-I19
Failure invalidates dependent conclusions, not unrelated state.

GTPL-I20
Supersession preserves history.

GTPL-I21
Generator-produced generators remain candidates until independently governed.

GTPL-I22
Optimization cannot weaken integrity.

GTPL-I23
Fast-path execution requires established local independence.

GTPL-I24
Template inheritance cannot silently erase parent constraints.

GTPL-I25
Canonical status requires the applicable canon process.
```

---

# 122. Generator Definition Template — Copy/Paste

```yaml
---
artifact_type: generator
status: DRAFT
claim_class: AMOS_MODEL
---

generator:

  identity:
    generator_id:
    generator_name:
    version:
    hash:
    template_id:
    template_version:

  purpose:
    objective:
    intended_use: []
    non_goals: []

  task_contract:
    accepted_task_classes: []
    preconditions: []
    completion_conditions: []
    escalation_conditions: []

  capabilities:
    required: []
    optional: []

  modes:
    required: []
    optional: []
    prohibited: []

  input_contract:
    schema_version:
    required: []
    optional: []
    validation: []

  seed_contract:
    schema_version:
    deterministic:
    replay_supported:

  output_contract:
    schema_version:
    required_fields: []
    claim_classes:
      - VERIFIED
      - DERIVED
      - MODEL
      - CONDITIONAL
      - COMPETING
      - UNKNOWN/GAP

  dependencies:
    direct: []
    transitive: []
    closure_status: UNKNOWN

  constraints:
    inherited: []
    local: []
    hard: []
    soft: []
    conflicts: []

  scope:
    system: []
    population: []
    environment: []
    scale: []
    domain: []
    assumptions: []

  regime:
    regime_id:
    conditions: {}

  provenance:
    sources: []
    ancestry: []
    transformations: []
    correlation_risks: []
    independence_status: UNKNOWN

  validation:
    required: true
    tests: []
    status: NOT_RUN

  falsification:
    required:
    falsifiers: []
    status: NOT_RUN

  uncertainty:
    evidence:
    model:
    scope:
    temporal:
    causal:
    execution:
    provenance_independence:

  governance:
    lifecycle_state: DRAFT
    promotion_required: true

  versioning:
    predecessor:
    compatibility: UNKNOWN

  supersession:
    supersedes: []
    superseded_by: []

  recovery:
    failure_classes: []
    rollback: []

  rscf:
    node_id:
    relations: []
```

---

# 123. Generator Output Template — Copy/Paste

```yaml
generator_output:

  output_id:

  generator:
    generator_id:
    version:
    hash:

  task_ref:
  seed_ref:
  execution_ref:

  content:

  claim_class:

  evidence: []

  provenance:
    sources: []
    ancestry: []
    independence_status: UNKNOWN

  scope: {}

  regime: {}

  temporal_validity: {}

  dependencies: []

  competing_explanations: []

  falsifiers: []

  uncertainty:
    evidence:
    model:
    scope:
    temporal:
    causal:
    execution:
    provenance_independence:

  validation:
    status:

  generated_at:
```

---

# 124. Generator Proof Capsule — Copy/Paste

```yaml
generator_proof_capsule:

  capsule_id:

  claim:
    content:
    class:

  load_bearing_premises: []

  evidence: []

  provenance: []

  scope: {}

  regime: {}

  temporal_validity: {}

  dependencies: []

  competing_explanations: []

  falsifiers: []

  invalidation_conditions: []

  sensitivity:
    smallest_flip_condition:
    robustness: UNKNOWN

  uncertainty:
    evidence:
    model:
    scope:
    temporal:
    causal:
    execution:
    provenance_independence:

  confidence:
    ceiling:
    limiting_premise:
```

---

# 125. Generator Validation Template — Copy/Paste

```yaml
generator_validation:

  validation_id:

  generator_ref:

  environment:
  regime:
  scope:

  contract_tests: []

  invariant_tests: []

  regression_tests: []

  provenance_tests: []

  independence_tests: []

  dependency_tests: []

  scope_tests: []

  causal_tests: []

  adversarial_tests: []

  failures: []

  unresolved_gaps: []

  result: NOT_RUN
```

---

# 126. Generator Falsification Template — Copy/Paste

```yaml
generator_falsification:

  falsification_id:

  generator_ref:

  target_claims: []

  target_invariants: []

  contradiction_search: []

  correlated_provenance_search: []

  stale_premise_search: []

  scope_leakage_search: []

  regime_mismatch_search: []

  hidden_dependency_search: []

  causal_overreach_search: []

  stronger_alternative_search: []

  discovered_failures: []

  result: NOT_RUN
```

---

# 127. Generator Promotion Template — Copy/Paste

```yaml
generator_promotion:

  promotion_id:

  generator_ref:

  from_state:
  to_state:

  evidence: []

  provenance: []

  validation_refs: []

  falsification_refs: []

  compatibility:

  scope: {}

  regime: {}

  unresolved_gaps: []

  rollback: {}

  governance:
    authority:
    decision:

  result:
```

---

# 128. Generator Supersession Template — Copy/Paste

```yaml
generator_supersession:

  supersession_id:

  predecessor:
    generator_id:
    version:
    hash:

  successor:
    generator_id:
    version:
    hash:

  reason:
    class:
    description:

  evidence: []

  provenance: []

  scope: {}

  regime: {}

  compatibility:
    overall: UNKNOWN

  migration:
    required:
    transformations: []
    losses: []

  effective_boundary:
    time:
    epoch:

  rollback:
    supported:
    conditions: []

  validation: []

  falsifiers: []

  governance:
    decision:

  state: PROPOSED
```

---

# 129. Generator Failure Template — Copy/Paste

```yaml
generator_failure:

  failure_id:

  generator_ref:
  execution_ref:

  class:

  failed_premise:
  failed_dependency:
  failed_constraint:

  affected_outputs: []

  affected_dependencies: []

  scope: {}

  regime: {}

  recoverability:

  repair_candidates: []

  rollback_target:

  revalidation_required: []

  provenance: []
```

---

# 130. RSCF Node Template — Copy/Paste

```text
RSCF-NODE

node_id: <generator_node_id>

node_type: generator

path: <canonical_path>

claim_class: AMOS_MODEL

RSCF-RELATIONS:

  - INDEXED_BY:
  - INDEXED_BY:

  - PART_OF:
  - PART_OF:

  - GOVERNED_BY: 12_GENERATORS_CONTRACT
  - VERSIONED_BY: 12_GENERATORS_VERSIONING

  - REGISTERED_IN:
  - SEEDED_BY:
  - PRODUCES:

  - VALIDATED_BY:
  - PROMOTED_BY:
  - SUPERSEDED_BY_PROCESS:
```

---

# 131. Template Selection Matrix

| Need                            | Template             |
| ------------------------------- | -------------------- |
| Declare generator               | Generator Definition |
| Define inputs                   | Input Contract       |
| Define seed                     | Seed Contract        |
| Define outputs                  | Output Contract      |
| Preserve evidence               | Provenance           |
| Preserve claim support          | Proof Capsule        |
| Evaluate correctness            | Validation           |
| Attack assumptions              | Falsification        |
| Register generator              | Registry Entry       |
| Admit candidate                 | Promotion            |
| Track evolution                 | Version              |
| Replace generator               | Supersession         |
| Transform versions              | Migration            |
| Recover failure                 | Failure / Rollback   |
| Combine generators              | Composition          |
| Bind graph semantics            | RSCF                 |
| Bind environment/model/evidence | GMEF                 |

---

# 132. Template Selection Rule

Use the smallest template set sufficient to preserve integrity.

Do not require maximum-detail envelopes for trivial generators if the omitted structure cannot alter correctness.

Do not use minimal templates when omitted structure could conceal material risk.

---

# 133. Template Composition Example

A consequential causal generator may require:

```text
GENERATOR DEFINITION
        +
TASK CONTRACT
        +
SEED CONTRACT
        +
OUTPUT CONTRACT
        +
PROVENANCE
        +
CAUSAL CONTRACT
        +
PROOF CAPSULE
        +
VALIDATION
        +
FALSIFICATION
        +
VERSIONING
        +
PROMOTION
```

A simple deterministic formatter may require substantially less.

---

# 134. Template Validation Pipeline

```text
TEMPLATE SELECTED
       ↓
REQUIRED FIELDS
       ↓
SEMANTIC VALIDATION
       ↓
DEPENDENCY VALIDATION
       ↓
CONSTRAINT VALIDATION
       ↓
SCOPE / REGIME VALIDATION
       ↓
PROVENANCE VALIDATION
       ↓
GENERATOR-SPECIFIC VALIDATION
       ↓
READY AS CANDIDATE
```

`READY AS CANDIDATE` is not equivalent to `PROMOTED`.

---

# 135. Generator Construction Pipeline

```text
TASK CLASS
    ↓
TEMPLATE SELECTION
    ↓
GENERATOR DEFINITION
    ↓
DEPENDENCY BINDING
    ↓
CONSTRAINT PROPAGATION
    ↓
CAPABILITY / MODE RESOLUTION
    ↓
SEED DEFINITION
    ↓
OUTPUT CONTRACT
    ↓
VALIDATION
    ↓
FALSIFICATION
    ↓
REGISTRY
    ↓
PROMOTION
```

---

# 136. Template Anti-Patterns

The following SHOULD be rejected or surfaced:

```text
EMPTY TEMPLATE COMPLETION
fields filled with invented values

ALIAS IDENTITY
mutable alias treated as stable generator identity

PROVENANCE COLLAPSE
all evidence flattened into citations without ancestry

CONFIDENCE INFLATION
output confidence exceeds weakest load-bearing support

SCOPE LEAKAGE
local validation treated as universal

REGIME LEAKAGE
one environment treated as all environments

CAUSAL LEAKAGE
correlation rewritten as causation

CONTRADICTION ERASURE
conflicting evidence averaged into one answer

PREMATURE PROMOTION
structural completion treated as validation

RETROACTIVE REBINDING
old output assigned to new generator version

SILENT CONSTRAINT LOSS
specialized template drops inherited hard constraints

UNBOUNDED RECURSION
generator traversal expands without decision value
```

---

# 137. Template Quality Criteria

A high-quality generator template SHOULD maximize:

$$Q_T = f( Integrity, Clarity, Traceability, Composability, Falsifiability, Repairability, ScopeSafety, Efficiency )$$

subject to:

$$Integrity$$

being non-negotiable relative to optimization.

---

# 138. Template Compression Rule

A template MAY be compressed only if compression preserves:

```text
factual support
scope correctness
contradiction visibility
provenance recoverability
causal discipline
constraint visibility
governance state
repairability
```

---

# 139. Template Extension Rule

Extensions SHOULD be additive where possible.

Example:

```yaml
extensions:
  domain_specific:
    ...
```

rather than redefining core field semantics without explicit versioning.

---

# 140. Unknown Extension Rule

Unknown extensions MAY be preserved without execution if safe.

They MUST NOT silently alter core generator semantics.

---

# 141. Template Namespace

Recommended conceptual namespace:

```text
AMOS.GENERATOR.TEMPLATE
```

with specializations such as:

```text
AMOS.GENERATOR.TEMPLATE.BASE
AMOS.GENERATOR.TEMPLATE.DETERMINISTIC
AMOS.GENERATOR.TEMPLATE.STOCHASTIC
AMOS.GENERATOR.TEMPLATE.CAUSAL
AMOS.GENERATOR.TEMPLATE.COUNTERFACTUAL
AMOS.GENERATOR.TEMPLATE.TRANSLATION
AMOS.GENERATOR.TEMPLATE.SYNTHESIS
AMOS.GENERATOR.TEMPLATE.RETRIEVAL
AMOS.GENERATOR.TEMPLATE.COMPOSITE
```

These names are specification-level unless separately established in implementation.

---

# 142. Template Registry Model

A future or external registry MAY represent:

```yaml
template_registry:

  templates:

    - template_id: generator_base
      version: null
      status: null

    - template_id: causal_generator
      version: null
      parent: generator_base
      status: null
```

This document does not claim such a registry currently exists.

---

# 143. Template Provenance

Each substantive template SHOULD preserve:

```text
origin
version
source artifact
parent template
change history
supersession history
```

where available.

---

# 144. Template Provenance Firewall

A template copied, translated, summarized, or generated from another template remains a descendant of that source.

Multiple descendants do not constitute independent architectural validation.

---

# 145. Template Governance

Changes to load-bearing template semantics SHOULD use the applicable:

```text
versioning
validation
provenance
promotion
supersession
canon
```

process.

---

# 146. Canon Boundary

This file defines candidate AMOS generator template structures.

It does not independently prove that:

```text
these templates are implemented;
all AMOS generators use them;
all listed lifecycle states exist in runtime;
all RSCF relations are currently materialized;
GMEF bindings are operational;
MVCC/CAS is literally implemented;
causal epoch finality is literally implemented;
automatic promotion exists;
automatic supersession exists;
automatic rollback exists;
all templates have empirical validation;
this artifact is final canon.
```

Those claims require independent evidence.

---

# 147. Artifact Declaration

```yaml
artifact:

  name: GENERATOR_TEMPLATES

  path:
    25_COGNITIVE_MATRIX/12_GENERATORS/GENERATOR_TEMPLATES.md

  family:
    COGNITIVE_MATRIX/GENERATORS

  artifact_type:
    - TEMPLATE_LIBRARY
    - GENERATOR_CONSTRUCTION_CONTRACT
    - GENERATOR_SCHEMA_MODEL

  node_id: generator_templates

  node_type: note

  claim_class: AMOS_MODEL

  status: CANDIDATE_CANON

  content_state: SUBSTANTIVE_SPECIFICATION

  origin_architect_steward: Trang Phan

  implementation:
    established: false

  empirical_validation:
    established: false

  final_canon:
    established: false
```

---

# 148. Final Generator Template Law

Generator templates exist to create structural discipline without manufacturing epistemic authority.

Therefore:

$$\boxed{ Template \neq Generator }$$

$$\boxed{ Generator \neq ValidatedGenerator }$$

$$\boxed{ StructuralConformance \neq EmpiricalValidation }$$

$$\boxed{ MultipleSources \neq IndependentSources }$$

$$\boxed{ NewVersion \neq AutomaticSupersession }$$

$$\boxed{ GeneratedGenerator \neq PromotedGenerator }$$

and:

$$\boxed{ MissingEvidence \Rightarrow VisibleGap }$$

not fabricated completion.

A valid AMOS generator template should make it possible to determine:

```text
WHAT is being generated?

WHY?

BY WHICH generator?

UNDER WHICH version?

FROM WHICH inputs and seed?

WITH WHICH dependencies?

UNDER WHICH constraints?

WITH WHICH capabilities and modes?

WITH WHICH evidence?

FROM WHICH provenance?

UNDER WHICH scope?

UNDER WHICH regime?

WITH WHAT freshness?

WITH WHAT uncertainty?

WITH WHAT competing explanations?

WHAT would falsify it?

HOW was it validated?

HOW can failure be localized?

HOW can it be repaired?

HOW can it be versioned?

HOW can it be promoted?

HOW can it be superseded?

HOW can its lineage be reconstructed?
```

If a template cannot preserve the information necessary to answer a decision-relevant version of those questions, the template is insufficient for that generator.

The governing objective is therefore:

$$\boxed{ GeneratorTemplate = MinimumSufficientStructure + ExplicitSemantics + Provenance + Constraints + Validation + Falsifiability + GovernedLineage }$$

subject always to:

$$\boxed{ Integrity > Completeness > Fluency > Speed > TokenSavings }$$

---

[[00_ROOT_MOC]]|[[AMOS MOC]]

---

**Related:** [[00_HOME]] · [[GENERATORS_MAP]] · [[COGNITIVE_MATRIX_MOC]] · [[AMOS_RSCF_NODES]] · 12_GENERATORS_CONTRACT · 12_GENERATORS_VERSIONING · [[GENERATOR_REGISTRY]] · [[GENERATOR_SEED]] · [[GENERATOR_OUTPUT]] · [[GENERATOR_PROMOTION]] · [[GENERATOR_FALSIFICATION]] · [[GENERATOR_SUPERSESSION]] · [[TASK_CONTRACT]] · [[TASK_RESOLVER]] · [[CAPABILITY_RESOLVER]] · [[MODE_ADMISSION_QUEUE]] · [[MODE_COMPOSITION_REGISTRY]] · [[MODE_CONFLICT_REGISTRY]] · [[MODE_COVERAGE_MATRIX]] · [[MODE_DEPENDENCY_GRAPH]]

---

RSCF-NODE

node_id: generator_templates

node_type: note

path: 25_COGNITIVE_MATRIX/12_GENERATORS/GENERATOR_TEMPLATES.md

claim_class: AMOS_MODEL

RSCF-RELATIONS:

* INDEXED_BY: [[00_HOME]]

* INDEXED_BY: [[AMOS_RSCF_NODES]]

* PART_OF: [[GENERATORS_MAP]]

* PART_OF: [[COGNITIVE_MATRIX_MOC]]

* GOVERNED_BY: 12_GENERATORS_CONTRACT

* VERSIONED_BY: 12_GENERATORS_VERSIONING

* DEFINES_STRUCTURE_FOR: [[GENERATOR_REGISTRY]]

* DEFINES_STRUCTURE_FOR: [[GENERATOR_SEED]]

* DEFINES_STRUCTURE_FOR: [[GENERATOR_OUTPUT]]

* DEFINES_STRUCTURE_FOR: [[GENERATOR_PROMOTION]]

* DEFINES_STRUCTURE_FOR: [[GENERATOR_FALSIFICATION]]

* DEFINES_STRUCTURE_FOR: [[GENERATOR_SUPERSESSION]]

* BINDS_TO: [[TASK_CONTRACT]]

* RESOLVES_WITH: [[TASK_RESOLVER]]

* RESOLVES_WITH: [[CAPABILITY_RESOLVER]]

* INTERACTS_WITH: [[MODE_ADMISSION_QUEUE]]

* INTERACTS_WITH: [[MODE_COMPOSITION_REGISTRY]]

* INTERACTS_WITH: [[MODE_CONFLICT_REGISTRY]]

* INTERACTS_WITH: [[MODE_COVERAGE_MATRIX]]

* INTERACTS_WITH: [[MODE_DEPENDENCY_GRAPH]]

* USES: [[K_PROVENANCE]]

* USES: [[K_SYBIL_HARDENING]]

* USES: [[K_BINDING]]

* USES: [[K_CONSTRAINT_PROPAGATION]]

* USES: [[K_GMEF]]

* USES: [[K_HML]]

* USES: [[K_RSCF]]

* USES: [[K_COUNTERFACTUAL]]

* USES: [[K_TRANSLATION]]

* PROVIDES_TEMPLATE_FOR: [[GENERATOR_REGISTRY]]

* PROVIDES_TEMPLATE_FOR: [[GENERATOR_SEED]]

* PROVIDES_TEMPLATE_FOR: [[GENERATOR_OUTPUT]]

* PROVIDES_TEMPLATE_FOR: [[GENERATOR_PROMOTION]]

* PROVIDES_TEMPLATE_FOR: [[GENERATOR_FALSIFICATION]]

* PROVIDES_TEMPLATE_FOR: [[GENERATOR_SUPERSESSION]]

```

This replaces the placeholder with a **full generator-template layer**, including reusable copy/paste schemas rather than just descriptive prose. Its status remains deliberately `CANDIDATE_CANON / AMOS_MODEL` until the appropriate provenance and canon process establishes anything stronger.
```

---
**MOC:** [[12_GENERATORS_MOC]]
