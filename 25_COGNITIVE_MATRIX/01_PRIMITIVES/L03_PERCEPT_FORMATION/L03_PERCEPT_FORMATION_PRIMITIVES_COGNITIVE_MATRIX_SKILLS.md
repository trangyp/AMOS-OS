---
type: skill
source: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L03_PERCEPT_FORMATION
tags:
- amos
- cognitive-matrix
- l03
- percept-formation
- skills
- rscf
- provenance
- governance
- canon/cognitive-matrix
title: L03_PERCEPT_FORMATION — Skills
origin_architect: Trang Phan
status: MODEL_SKILL_CONTRACT / UNIMPLEMENTED / UNVALIDATED
epistemic_class: MODEL
runtime_alignment: AMOS Full Brain OS / AMOS_CORE v4.4 lineage
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


# L03_PERCEPT_FORMATION — Skills

**Class:** `COGNITIVE_PRIMITIVE_SKILL_CONTRACT`
**Origin architect / steward:** Trang Phan
**Primitive:** `L03_PERCEPT_FORMATION`
**Artifact:** `SKILLS.md`
**Status:** `AMOS_MODEL / UNIMPLEMENTED / UNVALIDATED`

## 0. Purpose

Define the AMOS Skill contract for `L03_PERCEPT_FORMATION`.

The L03 Skill layer specifies which bounded reasoning capabilities may participate in percept formation, how they are invoked, what typed state they may consume or produce, which invariants they must preserve, and what authority they do **not** acquire merely by being available.

A Skill in this contract is treated as a governed executable reasoning capability rather than an unstructured instruction bundle. The AMOS Skill Builder explicitly requires Skills to preserve epistemic types, dependency structure, provenance, hard invariants, execution evidence, falsifiers, verification, repair, and packaging boundaries.

Core boundary:

```text
SKILL != TRUTH

SKILL AVAILABLE != SKILL INVOKED

SKILL INVOKED != SKILL EXECUTED

SKILL EXECUTED != RESULT VALIDATED

SKILL VALIDATED != AUTHORITY

SKILL OUTPUT != COMMIT

PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

UNKNOWN/GAP != PASS
```

---

# 1. Source / Canon References

## 1.1 Architecture-level Skill governance

The AMOS Skill Builder defines Skills as governed executable reasoning systems with the runtime:

```text
ORIENT
→ READ
→ PARSE
→ TYPE
→ UNDERSTAND
→ MODEL
→ PLAN
→ CREATE
→ EXECUTE
→ OBSERVE
→ VERIFY
→ CHALLENGE
→ REPAIR
→ COMPRESS
→ PACKAGE
```

It requires:

```text
integrity > completeness > fluency > speed > token savings
```

and forbids inventing:

```text
canon
evidence
equations
benchmark settings
execution results
provenance
dependencies
tool capabilities
```

It also separates:

```text
LOCAL_CORRECTNESS
!=
REPOSITORY_COHERENCE
!=
RUNTIME_CORRECTNESS
!=
REQUIREMENT_CORRECTNESS
```

and requires smallest-sufficient dependency closure, hard invariant gates, tests, and regression checks.

## 1.2 Related AMOS architecture

Relevant architecture families include:

```text
AMOS Full Brain OS
AMOS Cognition
AMOS RSCF
AMOS H/M/L
AMOS Multimodal Perception Layer
AMOS Attention Allocation Governor
AMOS Binding architecture
AMOS Information Operator Engine
AMOS Provenance Trust Firewall
AMOS Memory governance
AMOS Constraint Propagation
AMOS Metacognitive Confidence Auditor
AMOS Infrastructure Control Plane
AMOS Deterministic AI Control Plane
```

## 1.3 Direct L03 canon status

```yaml
canonical_L03_skill_registry: UNKNOWN_GAP
canonical_skill_identifiers: UNKNOWN_GAP
canonical_skill_interfaces: UNKNOWN_GAP
canonical_skill_composition_rules: UNKNOWN_GAP
canonical_skill_authority_model: UNKNOWN_GAP
canonical_skill_runtime: UNKNOWN_GAP
canonical_skill_promotion_rules: UNKNOWN_GAP
```

Therefore the L03-specific Skill registry below is `AMOS_MODEL`.

---

# 2. Definition and Scope

An L03 Skill is a bounded capability that may perform one or more transformations needed to construct, inspect, validate, challenge, or repair percept state.

Candidate abstraction:

[
Skill_i:
(Input_i, Context_i, Constraints_i)
\rightarrow
(Output_i, Evidence_i, Trace_i)
]

subject to:

[
Admissible(Skill_i)
===================

TypeValid
\land
CapabilityAllowed
\land
ScopeValid
\land
RegimeValid
\land
InvariantValid
]

`AMOS_MODEL`.

A Skill may:

```text
read permitted percept state
transform permitted percept state
analyze dependencies
generate bounded percept candidates
validate invariants
surface uncertainty
propose repair
produce evidence
```

A Skill does not automatically gain authority to:

```text
commit durable state
change governing policy
rewrite source observations
erase provenance
override scope/regime constraints
grant itself new capabilities
perform external effects beyond its authorization
```

---

# 3. Typed Skill Descriptor

```yaml
L03SkillDescriptor:

  skill_id:
    type: SkillID

  name:
    type: string

  version:
    type: VersionRef

  class:
    type:
      - PERCEPTION
      - ATTENTION_INTERFACE
      - FEATURE
      - RELATION
      - BINDING
      - MULTIMODAL
      - TEMPORAL
      - SPATIAL
      - MEMORY_INTERFACE
      - PROVENANCE
      - RSCF
      - HML
      - VALIDATION
      - REPAIR
      - CONTROL_INTERFACE

  epistemic_status:
    type:
      - SOURCE_CANON
      - SOURCE_CLAIM
      - SOURCE_MODEL
      - AMOS_MODEL
      - IMPLEMENTED
      - EXECUTED_OBSERVATION
      - UNKNOWN_GAP

  input_contract:
    type: TypeRef[]

  output_contract:
    type: TypeRef[]

  preconditions:
    type: Predicate[]

  postconditions:
    type: Predicate[]

  invariants:
    type: InvariantRef[]

  dependencies:
    type: DependencyRef[]

  capabilities:
    type: CapabilityRef[]

  forbidden_effects:
    type: EffectRef[]

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeEnvelope

  HML:
    type: HMLContext

  provenance:
    type: ProvenanceBundle

  tests:
    type: TestRef[]

  falsifiers:
    type: Falsifier[]

  implementation_status:
    type:
      - PLACEHOLDER
      - ADDRESSABLE
      - IMPLEMENTED
      - VALIDATED
      - UNKNOWN_GAP
```

---

# 4. Typed Inputs

```yaml
L03SkillInput:

  observations:
    type: ObservationState[]

  attention_state:
    type: AttentionState

  features:
    type: FeatureState[]

  relations:
    type: RelationState[]

  bindings:
    type: BindingState[]

  percept_candidates:
    type: PerceptCandidate[]

  competing_percepts:
    type: CompetingPerceptSet[]

  memory_context:
    type: MemoryContext[]

  HML_state:
    type: HMLPerceptState

  provenance:
    type: ProvenanceGraph

  dependency_graph:
    type: DependencyGraph

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeRef

  freshness:
    type: FreshnessState

  uncertainty:
    type: UncertaintyVector

  authority_context:
    type: AuthorityContext
```

---

# 5. Typed Outputs

```yaml
L03SkillOutput:

  transformed_state:
    type: PerceptFormationState | null

  features:
    type: FeatureState[]

  relations:
    type: RelationState[]

  bindings:
    type: BindingState[]

  percept_candidates:
    type: PerceptCandidate[]

  competing:
    type: CompetingPerceptSet[]

  validation_result:
    type: ValidationResult | null

  repair_proposal:
    type: RepairProposal | null

  provenance_delta:
    type: ProvenanceDelta

  dependency_delta:
    type: DependencyDelta

  uncertainty_delta:
    type: UncertaintyDelta

  confidence_ceiling:
    type: ConfidenceBound

  execution_trace:
    type: SkillExecutionTrace

  status:
    type:
      - PASS
      - CONDITIONAL
      - COMPETING
      - FAIL
      - UNKNOWN_GAP

  commit_authority:
    type: NONE
```

---

# 6. State Variables

```text
SkillReg_t   = skill registry
SkillVer_t   = skill versions

Cap_t        = capability envelopes
Perm_t       = permission state
Auth_t       = authority context

Input_t      = typed skill input
Output_t     = typed skill output

Exec_t       = execution state
Trace_t      = execution trace
Test_t       = validation/test state

Inv_t        = invariant state
Prov_t       = provenance
Dep_t        = dependencies

Scope_t      = scope
Reg_t        = regime
Fresh_t      = freshness

U_t          = uncertainty
Conf_t       = confidence ceiling

Q_t          = quarantined skills/results
Gap_t        = unresolved Skill gaps
```

---

# 7. Candidate L03 Skill Registry

The following names represent **capability roles**, not claims that every Skill is implemented, installed, integrated, or validated.

## 7.1 Perception core

```text
AMOS Multimodal Perception Layer
AMOS Sensory Map Integrator
AMOS Information Operator Engine
AMOS Binding RSCF Engine
AMOS Distinction RSCF Architecture
AMOS Distinction-Relation-Constraint Algebra
```

Primary roles:

```text
normalize percept input
distinguish local features
relate percept elements
bind/unbind elements
align modality state
construct percept candidates
```

---

## 7.2 Attention interface

```text
AMOS Attention Allocation Governor
```

Role:

```text
provide bounded salience/priority state
```

Hard boundary:

```text
ATTENTION SKILL
MUST NOT
CONVERT SALIENCE INTO TRUTH
```

---

## 7.3 H/M/L and cross-scale

```text
AMOS Cross-Scale RSCF Tensor Engine
AMOS Temporal Multi-Scale RSCF Engine
AMOS Universal Coordinate System
```

Roles:

```text
L→M aggregation
M→H aggregation
cross-scale dependency tracing
scale-aware scope/regime propagation
temporal alignment
observer/context alignment
```

---

## 7.4 Provenance and epistemic governance

```text
AMOS Provenance Trust Firewall
AMOS Provenance Sybil Hardening
AMOS Knowledge/Epistemology RSCF Engine
RSCF Modeler
AMOS Claim Verifier
AMOS Metacognitive Confidence Auditor
```

Roles:

```text
trace source ancestry
classify epistemic state
detect correlated support
calculate confidence ceilings
preserve competing hypotheses
surface UNKNOWN/GAP
```

---

## 7.5 Memory interface

```text
AMOS Agent Memory Dynamics RSCF Engine
AMOS Memory Conflict Governor
AMOS Memory Immune System
AMOS Action Memory Firewall
```

Roles:

```text
retrieve admissible memory
preserve memory/current-observation distinction
detect stale/conflicting memory
quarantine contaminated memory
govern memory influence
```

---

## 7.6 Repair / recovery

```text
AMOS Repair Priority Governor
AMOS Target of Repair Intelligence
AMOS Repair Harm Auditor
AMOS Collapse Recovery
AMOS Constraint Propagation RSCF Engine
```

Roles:

```text
locate failed dependency
choose repair target
estimate repair externalities
preserve unaffected branches
rebuild failed percept state
```

---

## 7.7 Control-plane interface

```text
AMOS Infrastructure Control Plane
AMOS Deterministic AI Control Plane
AMOS Commit-Time Authorization RSCF Engine
```

Roles:

```text
validate capability envelope
validate state freshness
validate authority
validate effect binding
control durable commit
```

Hard boundary:

```text
CONTROL SKILL AVAILABLE
!=
L03 OWNS CONTROL AUTHORITY
```

---

# 8. Skill Composition

L03 may require multiple Skills in one governed composition.

Candidate:

```text
OBSERVATION
↓
Attention Allocation
↓
Information Operators
↓
Binding
↓
Multimodal Perception
↓
H/M/L Mapping
↓
Provenance Audit
↓
RSCF Construction
↓
Confidence Audit
↓
Validation
↓
State Proposal
```

Skill composition must preserve:

```text
type compatibility
scope compatibility
regime compatibility
provenance continuity
authority boundaries
dependency identity
uncertainty
H/M/L identity
```

Candidate composition condition:

[
Composable(S_i,S_j)
===================

TypeCompatible
\land
ScopeCompatible
\land
RegimeCompatible
\land
InvariantCompatible
\land
AuthorityCompatible
]

`AMOS_MODEL`.

---

# 9. Skill Invariants

```text
SKILL-INV-001
SKILL AVAILABILITY != EXECUTION

SKILL-INV-002
SKILL EXECUTION != VALIDATION

SKILL-INV-003
SKILL VALIDATION != AUTHORITY

SKILL-INV-004
SKILL OUTPUT != COMMITTED STATE

SKILL-INV-005
SKILL MUST DECLARE TYPED INPUTS/OUTPUTS

SKILL-INV-006
SKILL MUST PRESERVE LOAD-BEARING PROVENANCE

SKILL-INV-007
SKILL MUST NOT SILENTLY CHANGE EPISTEMIC CLASS

SKILL-INV-008
OBSERVATION MUST REMAIN DISTINCT FROM DERIVATION

SKILL-INV-009
MEMORY MUST REMAIN DISTINCT FROM CURRENT OBSERVATION

SKILL-INV-010
ATTENTION MUST REMAIN DISTINCT FROM TRUTH

SKILL-INV-011
BINDING MUST NOT PROVE IDENTITY

SKILL-INV-012
MULTIMODAL FUSION MUST NOT MANUFACTURE INDEPENDENCE

SKILL-INV-013
H/M/L AGGREGATION MUST PRESERVE MATERIAL HETEROGENEITY

SKILL-INV-014
SKILL COMPOSITION MUST PRESERVE SCOPE

SKILL-INV-015
SKILL COMPOSITION MUST PRESERVE REGIME

SKILL-INV-016
SKILL COMPOSITION MUST PRESERVE OBSERVER CONTEXT

SKILL-INV-017
SKILL COMPOSITION MUST PRESERVE FRESHNESS

SKILL-INV-018
CORRELATED SKILLS/AGENTS MUST NOT CREATE FALSE EVIDENCE INDEPENDENCE

SKILL-INV-019
CONFIDENCE SHALL NOT INCREASE MERELY BECAUSE MORE SKILLS PROCESSED THE SAME EVIDENCE

SKILL-INV-020
UNKNOWN/GAP SHALL NOT PASS A HARD SKILL GATE

SKILL-INV-021
INVALID SKILL RESULT SHALL INVALIDATE DEPENDENT RESULTS ONLY

SKILL-INV-022
SKILL REPAIR REQUIRES REVALIDATION

SKILL-INV-023
UNIMPLEMENTED SKILL MUST NOT BE PRESENTED AS EXECUTABLE

SKILL-INV-024
ADDRESSABLE SKILL MUST NOT BE PRESENTED AS VALIDATED

SKILL-INV-025
CAPABILITY != AUTHORITY

SKILL-INV-026
PROPOSAL != COMMIT
```

---

# 10. Skill Admission

A Skill should only enter an L03 runtime when its contract is sufficiently known.

Candidate hard gate:

[
AdmitSkill(s)
=============

IdentityKnown(s)
\land
VersionKnown(s)
\land
InputContractKnown(s)
\land
OutputContractKnown(s)
\land
CapabilityKnown(s)
\land
InvariantsKnown(s)
]

with missing load-bearing fields resulting in:

```text
QUARANTINE
or
UNKNOWN/GAP
```

not automatic admission.

---

# 11. Skill Selection

The smallest sufficient Skill set should be preferred.

The AMOS Skill Builder explicitly recommends smallest-sufficient dependency closure and hard invariant gates rather than loading or invoking unnecessary capability.

Candidate selection principle:

[
SkillSet^*
==========

\arg\min_{S}
Cost(S)
]

subject to:

[
RequiredCapabilityCovered(S)
\land
HardInvariantsPass(S)
]

`AMOS_MODEL`.

This is not a universal optimization theorem.

---

# 12. Skill Invocation

Candidate request:

```yaml
SkillInvocationRequest:

  skill_id: null

  skill_version: null

  objective: null

  input_refs: []

  expected_output_type: null

  HML: null

  scope: null

  regime: null

  freshness: null

  provenance: []

  authority_context: null

  required_invariants: []

  requested_effect:
    type:
      - READ
      - ANALYZE
      - TRANSFORM
      - VALIDATE
      - REPAIR
      - PROPOSE
```

Before invocation:

```text
resolve capability
check preconditions
check scope
check regime
check authority
check input types
check dependency freshness
```

---

# 13. Skill Execution Trace

```yaml
SkillExecutionTrace:

  execution_id: null

  skill_id: null
  skill_version: null

  objective: null

  input_refs: []

  dependency_reads: []

  started_at: null
  completed_at: null

  output_refs: []

  provenance_delta: null

  uncertainty_delta: null

  confidence_ceiling: null

  invariant_results: []

  tests_run: []

  failures: []

  status:
    - EXECUTED
    - FAILED
    - PARTIAL
    - UNKNOWN_GAP
```

Hard rule:

```text
NO EXECUTION TRACE
→
NO EXECUTED CLAIM
```

where execution evidence is required.

---

# 14. Dependencies

## Upstream

```text
L01_SENSING_OBSERVATION
L02_ATTENTION
```

## Internal

```text
L03_PERCEPT_FORMATION/README
L03_PERCEPT_FORMATION/PURPOSE
L03_PERCEPT_FORMATION/DEFINITION
L03_PERCEPT_FORMATION/VARIABLES
L03_PERCEPT_FORMATION/STATE
L03_PERCEPT_FORMATION/OPERATORS
L03_PERCEPT_FORMATION/INVARIANTS
L03_PERCEPT_FORMATION/DEPENDENCIES
L03_PERCEPT_FORMATION/HML
L03_PERCEPT_FORMATION/MEMORY
L03_PERCEPT_FORMATION/PROVENANCE
L03_PERCEPT_FORMATION/PROTOCOLS
L03_PERCEPT_FORMATION/FAILURE_MODES
L03_PERCEPT_FORMATION/REPAIR
L03_PERCEPT_FORMATION/TESTS
L03_PERCEPT_FORMATION/RSCF
```

## Cross-cutting

```text
AMOS Skill Builder
AMOS RSCF
AMOS H/M/L
AMOS provenance topology
AMOS epistemic governance
AMOS capability authorization
AMOS control-plane governance
AMOS repair governance
```

---

# 15. H/M/L Applicability

## L — Local Skills

Candidate capabilities:

```text
feature extraction
local distinction
relation formation
temporal alignment
spatial alignment
local provenance
```

Examples:

```text
Information Operator Engine
Distinction architecture
Temporal Multi-Scale engine
```

## M — Intermediate Skills

Candidate capabilities:

```text
binding
object/event construction
multimodal fusion
memory/context integration
competing candidate generation
```

Examples:

```text
Binding RSCF Engine
Multimodal Perception Layer
Memory Conflict Governor
```

## H — Governing Skills

Candidate capabilities:

```text
scene-level integration
H/M/L mapping
provenance audit
RSCF construction
confidence governance
repair prioritization
```

Examples:

```text
Cross-Scale RSCF Tensor Engine
RSCF Modeler
Provenance Trust Firewall
Metacognitive Confidence Auditor
```

Cross-scale rule:

```text
L-SKILL OUTPUT
MUST NOT
SILENTLY BECOME H-LEVEL TRUTH
```

---

# 16. Control-Plane Requirements

The Skill layer represents **capability**.

The control plane represents authoritative governance of capability use.

The control plane should determine:

```text
whether skill exists
whether skill version is admitted
whether requester may invoke it
which inputs it may read
which effects it may propose
which tools it may use
whether output is fresh
whether output may influence protected state
whether result may be committed
```

L03 Skill workers must not:

```text
self-authorize
expand their own capability envelope
change policy
create new durable authority
bypass commit validation
reinterpret capability as permission
```

---

# 17. Agents

Candidate agent-to-Skill relation:

```text
AGENT
↓ invokes
SKILL
↓ produces
PROPOSAL / EVIDENCE / TRANSFORM
↓ evaluated by
VALIDATORS / CONTROL PLANE
```

Candidate agents:

```text
L03_FEATURE_AGENT
L03_BINDING_AGENT
L03_MULTIMODAL_AGENT
L03_HML_AGENT
L03_MEMORY_AGENT
L03_PROVENANCE_AGENT
L03_RSCF_AGENT
L03_VALIDATION_AGENT
L03_REPAIR_AGENT
```

Hard boundary:

```text
AGENT + SKILL
!=
AUTHORITY
```

---

# 18. Workflows

## 18.1 Skill discovery workflow

```text
DEFINE OBJECTIVE
↓
IDENTIFY REQUIRED CAPABILITY
↓
SEARCH ADMITTED SKILL REGISTRY
↓
FILTER BY:
  type
  scope
  regime
  version
  authority
↓
SELECT SMALLEST SUFFICIENT SKILL SET
↓
INVOKE
```

## 18.2 Skill execution workflow

```text
SKILL REQUEST
↓
CHECK IDENTITY / VERSION
↓
CHECK INPUT TYPES
↓
CHECK PRECONDITIONS
↓
CHECK CAPABILITY ENVELOPE
↓
CHECK AUTHORITY
↓
EXECUTE
↓
CAPTURE TRACE
↓
CHECK INVARIANTS
↓
VERIFY OUTPUT
↓
CHALLENGE
↓
PASS / CONDITIONAL / FAIL / GAP
```

## 18.3 Skill composition workflow

```text
SKILL A OUTPUT
↓
TYPE CHECK
↓
PROVENANCE CHECK
↓
SCOPE / REGIME CHECK
↓
SKILL B INPUT
↓
EXECUTION
↓
COMPOSED RESULT
↓
CROSS-SKILL INVARIANT CHECK
```

## 18.4 Skill repair workflow

```text
SKILL RESULT FAILS
↓
LOCATE:
  input failure
  skill logic failure
  dependency failure
  environment failure
  scope/regime failure
↓
QUARANTINE RESULT
↓
PRESERVE VALID STATE
↓
REPAIR OR SUBSTITUTE SKILL
↓
REEXECUTE
↓
REVERIFY
↓
REVALIDATE DEPENDENTS
```

---

# 19. Protocols

Candidate protocol surfaces:

```text
SKILL_DISCOVERY_REQUEST
SKILL_DISCOVERY_RESULT

SKILL_CAPABILITY_CHECK
SKILL_CAPABILITY_RESULT

SKILL_INVOCATION_REQUEST
SKILL_INVOCATION_RESULT

SKILL_EXECUTION_TRACE
SKILL_VALIDATION_REQUEST
SKILL_VALIDATION_RESULT

SKILL_COMPOSITION_REQUEST
SKILL_COMPOSITION_RESULT

SKILL_QUARANTINE_NOTICE
SKILL_INVALIDATION_NOTICE

SKILL_REPAIR_REQUEST
SKILL_REPAIR_RESULT

SKILL_PROMOTION_REQUEST
SKILL_PROMOTION_RESULT

SKILL_STATE_PROPOSAL
```

Canonical protocol names remain `UNKNOWN/GAP`.

---

# 20. Evidence / Provenance

Each Skill used materially in an L03 result should preserve:

```yaml
SkillEvidence:

  skill_id: null

  skill_version: null

  skill_origin: null

  implementation_ref: null

  input_refs: []

  output_refs: []

  dependency_refs: []

  execution_ref: null

  environment_ref: null

  test_refs: []

  validator_refs: []

  scope: null
  regime: null
  freshness: null

  provenance: []

  uncertainty: null

  confidence_ceiling: null

  status:
    - SOURCE_DEFINED
    - ADDRESSABLE
    - IMPLEMENTED
    - EXECUTED
    - VALIDATED
    - QUARANTINED
    - UNKNOWN_GAP
```

Hard rule:

```text
SKILL DOCUMENTATION
!=
EXECUTION EVIDENCE

EXECUTION EVIDENCE
!=
GENERAL VALIDITY
```

---

# 21. Uncertainty and Confidence Ceiling

Skill-level uncertainty should remain explicit:

```yaml
skill_uncertainty:

  identity:
    description: uncertainty in exact Skill identity/version

  contract:
    description: uncertainty in declared behavior

  implementation:
    description: uncertainty whether implementation matches contract

  execution:
    description: uncertainty from actual runtime behavior

  environment:
    description: uncertainty from runtime dependencies

  scope:
    description: uncertainty in applicability

  regime:
    description: uncertainty from current operating regime

  provenance:
    description: uncertainty in evidence lineage

  composition:
    description: uncertainty introduced by cross-Skill handoffs
```

Candidate confidence relation:

[
Conf(Output)
\le
\min(
Conf(Input),
Conf(SkillContract),
Conf(Execution),
Conf(Dependencies)
)
]

for load-bearing dimensions.

`AMOS_MODEL`.

A sequence of multiple Skills does not increase confidence merely by multiplicity.

---

# 22. Skill Failure Modes

```text
SFM-001
Skill identity unknown.

SFM-002
Skill version mismatch.

SFM-003
Input type mismatch.

SFM-004
Output type mismatch.

SFM-005
Missing dependency.

SFM-006
Stale dependency.

SFM-007
Scope mismatch.

SFM-008
Regime mismatch.

SFM-009
Capability not admitted.

SFM-010
Authority missing.

SFM-011
Tool capability assumed but unavailable.

SFM-012
Skill contract and implementation diverge.

SFM-013
Skill output loses provenance.

SFM-014
Skill output silently changes epistemic class.

SFM-015
Skill duplicates correlated evidence and inflates confidence.

SFM-016
Skill composition erases uncertainty.

SFM-017
Skill composition creates hidden dependency.

SFM-018
Skill composition creates scope leakage.

SFM-019
Skill suppresses legitimate competing percept.

SFM-020
Skill introduces unsupported causal claim.

SFM-021
Skill execution claimed without trace.

SFM-022
Skill validation claimed without tests.

SFM-023
Skill availability represented as implementation.

SFM-024
Implemented Skill represented as validated.

SFM-025
Skill repair alters source evidence.

SFM-026
Skill repair skips revalidation.

SFM-027
Skill result becomes commit without authority.

SFM-028
UNKNOWN/GAP treated as PASS.
```

---

# 23. Repair / Recovery

```text
DETECT SKILL FAILURE
↓
CLASSIFY:
  contract
  input
  implementation
  dependency
  environment
  authority
  execution
↓
IDENTIFY AFFECTED OUTPUTS
↓
TRACE LOAD-BEARING DESCENDANTS
↓
QUARANTINE FAILED RESULT
↓
PRESERVE UNAFFECTED STATE
↓
OPTION:
  repair skill
  use alternative skill
  reduce scope
  rollback
  escalate
↓
REEXECUTE WITH CHANGED CONDITION
↓
CAPTURE NEW TRACE
↓
VERIFY
↓
CHALLENGE
↓
REVALIDATE DEPENDENTS
↓
RESTORE / CONDITIONAL / COMPETING / GAP
```

Hard recovery rule:

```text
DO NOT REPEAT IDENTICAL FAILED SKILL PATH
WITHOUT CHANGED:
  evidence
  implementation
  dependency
  parameter
  environment
  or strategy
```

---

# 24. Tests / Validators

Minimum Skill tests:

```text
VALIDATE_SKILL_IDENTITY
VALIDATE_SKILL_VERSION
VALIDATE_INPUT_SCHEMA
VALIDATE_OUTPUT_SCHEMA
VALIDATE_PRECONDITIONS
VALIDATE_CAPABILITY_ENVELOPE
VALIDATE_SCOPE
VALIDATE_REGIME
VALIDATE_PROVENANCE
VALIDATE_DEPENDENCIES
VALIDATE_HML
VALIDATE_EXECUTION_TRACE
VALIDATE_INVARIANT_PRESERVATION
VALIDATE_CONFIDENCE_CEILING
VALIDATE_COMPETING_PRESERVATION
VALIDATE_AUTHORITY_BOUNDARY
VALIDATE_PROPOSAL_COMMIT_BOUNDARY
VALIDATE_UNKNOWN_NOT_PASS
```

Conceptual test suite:

```text
TEST-L03-SKILL-001
Invoke a Skill with wrong input type.
Expected:
FAIL.

TEST-L03-SKILL-002
Skill exists but is not implemented.
Expected:
ADDRESSABLE / UNKNOWN, not EXECUTED.

TEST-L03-SKILL-003
Skill documentation claims capability but runtime evidence is absent.
Expected:
SOURCE_CLAIM / MODEL only.

TEST-L03-SKILL-004
Three Skills process the same source.
Expected:
independent evidence count does not become three.

TEST-L03-SKILL-005
Skill output changes regime.
Expected:
revalidation required.

TEST-L03-SKILL-006
Skill loses provenance during composition.
Expected:
FAIL / QUARANTINE.

TEST-L03-SKILL-007
One Skill returns UNKNOWN.
Expected:
dependent hard gate cannot PASS.

TEST-L03-SKILL-008
Skill repairs binding but suppresses competing candidate.
Expected:
invariant failure.

TEST-L03-SKILL-009
Skill result is valid but authority absent.
Expected:
proposal only.

TEST-L03-SKILL-010
Skill passes unit tests but composed runtime fails.
Expected:
runtime not validated.

TEST-L03-SKILL-011
Replacement Skill produces equivalent output under same contract.
Expected:
composition may proceed only after invariant/provenance checks.

TEST-L03-SKILL-012
All structural Skill tests pass.
Expected:
does not establish empirical human-perception validity.
```

Current state:

```yaml
tests_defined: true
tests_executed: false
runtime_validation: false
formal_verification: false
empirical_validation: false
```

---

# 25. Skill Promotion States

Candidate lifecycle:

```text
PLACEHOLDER
↓
ADDRESSABLE
↓
IMPLEMENTED
↓
EXECUTED
↓
TESTED
↓
VALIDATED
↓
PROMOTED_FOR_SCOPE
```

Hard rule:

```text
NO STATE MAY BE SKIPPED
BY ASSERTION ALONE
```

Candidate promotion condition aligned with AMOS Skill Builder:

```text
ArchitectureCompatible
AND
ContractCompatible
AND
HardInvariantsPass
AND
SpecPass
AND
RegressionPass
```

Promotion is always scope-bound.

---

# 26. Falsifiers

Revise this contract if direct canonical evidence establishes:

```text
different canonical L03 Skill registry

different Skill capability boundaries

different Skill composition rules

different agent/Skill relationship

different H/M/L Skill mapping

different provenance requirements

different authority ownership

different promotion criteria

or executable canonical runtime contradicts this model
```

A specific Skill claim is falsified when reproducible execution contradicts its declared contract under admissible conditions.

---

# 27. Gap Matrix

```yaml
gap_status:

  generic_skill_governance:
    status: SOURCE_ALIGNED

  integrity_first_rule:
    status: SOURCE_ALIGNED

  runtime_lifecycle:
    status: SOURCE_ALIGNED

  typed_state_requirement:
    status: SOURCE_ALIGNED

  smallest_dependency_closure:
    status: SOURCE_ALIGNED

  hard_invariant_gate:
    status: SOURCE_ALIGNED

  promotion_requirements:
    status: SOURCE_ALIGNED

  L03_skill_categories:
    status: MODEL_DEFINED

  L03_skill_composition:
    status: MODEL_DEFINED

  L03_skill_protocols:
    status: MODEL_DEFINED

  L03_skill_failure_model:
    status: MODEL_DEFINED

  canonical_L03_skill_registry:
    status: CRITICAL_GAP

  canonical_skill_ids:
    status: CRITICAL_GAP

  canonical_skill_interfaces:
    status: CRITICAL_GAP

  canonical_skill_composition:
    status: DECISION_RELEVANT_GAP

  canonical_skill_authority:
    status: CRITICAL_GAP

  executable_L03_skill_runtime:
    status: CRITICAL_GAP

  executed_tests:
    status: CRITICAL_GAP

  formal_verification:
    status: CRITICAL_GAP

  empirical_validation:
    status: CRITICAL_GAP
```

---

# 28. Competing Skill Architectures

## COMPETING-001 — Monolithic Perception Skill

```text
one Skill
→ all L03 percept formation
```

Advantages:

```text
simple interface
low orchestration overhead
```

Risks:

```text
large authority surface
poor modular auditability
weak selective repair
```

---

## COMPETING-002 — Flat Skill Library

```text
many Skills
available equally
```

Advantages:

```text
modularity
specialization
```

Risks:

```text
selection ambiguity
context explosion
composition errors
```

---

## COMPETING-003 — H/M/L Skill Hierarchy

```text
H Skills
↓
M Skills
↓
L Skills
```

Advantages:

```text
scale discipline
localized routing
```

Risks:

```text
rigid hierarchy
possible cross-scale blind spots
```

---

## COMPETING-004 — Governed Typed Capability Graph

```text
typed Skills
+
capability envelopes
+
dependency graph
+
H/M/L coordinates
+
provenance
+
hard invariant gates
+
execution traces
+
control-plane authority
```

Current model preference:

```text
COMPETING-004
```

because it best matches the AMOS Skill Builder's governed executable-system model.

Still:

```text
MODEL PREFERENCE
!=
CANONICAL L03 SKILL ARCHITECTURE
```

---

# 29. RSCF Completion State

```yaml
rscf:

  id: L03_PERCEPT_FORMATION_SKILLS

  claim:
    L03_PERCEPT_FORMATION can use a governed set of typed Skills
    for attention interfacing, feature formation, relation and binding,
    multimodal integration, H/M/L mapping, memory interaction,
    provenance, RSCF construction, validation, and repair while
    preserving capability/authority and proposal/commit boundaries.

  claim_class: MODEL

  evidence:
    - AMOS Skill Builder
    - AMOS L03 reconstructed contracts
    - AMOS RSCF/HML/provenance architecture

  provenance:
    origin_architect: Trang Phan
    architecture_family: AMOS
    subsystem: COGNITIVE_MATRIX
    primitive: L03_PERCEPT_FORMATION
    artifact: SKILLS.md
    derivation: SOURCE_ALIGNED_SKILL_GOVERNANCE_PLUS_L03_MODEL

  scope:
    system: AMOS_OS
    subsystem: COGNITIVE_MATRIX
    primitive: L03_PERCEPT_FORMATION
    concern: skill_architecture

  regime:
    governed percept-formation architecture

  freshness:
    revalidate_when:
      - direct L03 Skill canon recovered
      - Skill Builder governance changes
      - L03 operator/state schemas change
      - HML contract changes
      - control-plane architecture changes
      - Skill implementation evidence appears
      - runtime validation evidence appears

  dependencies:
    - L01_SENSING_OBSERVATION
    - L02_ATTENTION
    - L03_DEFINITION
    - L03_STATE
    - L03_OPERATORS
    - L03_INVARIANTS
    - L03_HML
    - L03_MEMORY
    - L03_PROVENANCE
    - L03_PROTOCOLS
    - L03_REPAIR
    - L03_RSCF
    - AMOS_SKILL_BUILDER
    - AMOS_INFRASTRUCTURE_CONTROL_PLANE

  competing:
    - monolithic perception skill
    - flat skill library
    - H/M/L skill hierarchy
    - governed typed capability graph

  falsifiers:
    - incompatible direct L03 Skill canon
    - incompatible Skill authority semantics
    - incompatible composition semantics
    - incompatible HML Skill mapping
    - executable runtime counterexample

  uncertainty:
    source: MEDIUM
    L03_mapping: HIGH
    canonical_registry: MAXIMUM
    composition: HIGH
    authority: HIGH
    execution: MAXIMUM
    empirical: MAXIMUM

  confidence_ceiling:
    Generic AMOS Skill governance is source-aligned.
    The specific L03 Skill registry, interfaces, composition,
    implementation, and validation remain MODEL or UNKNOWN/GAP
    pending direct canonical and executable evidence.

  gap_status:
    canonical_skill_registry: CRITICAL_GAP
    canonical_interfaces: CRITICAL_GAP
    canonical_composition: DECISION_RELEVANT_GAP
    canonical_authority: CRITICAL_GAP
    executable_runtime: CRITICAL_GAP
    executed_validation: CRITICAL_GAP
    empirical_validation: CRITICAL_GAP

  cheapest_discriminating_test:
    recover direct canonical L03 Skill material, map every declared
    capability against this registry, then execute a minimal composed
    chain for observation→feature→binding→percept→RSCF with typed
    contracts, provenance tracking, fault injection, replacement-Skill
    testing, and authority-boundary checks.
```

---

# 30. Completion State

```yaml
completion_state:

  source_canon_references:
    status: PARTIAL_SOURCE_BOUND

  definition_scope:
    status: MODEL_COMPLETE

  typed_inputs_outputs:
    status: MODEL_COMPLETE

  state_variables:
    status: MODEL_COMPLETE

  operators:
    status: MODEL_COMPLETE_BY_REFERENCE

  invariants:
    status: MODEL_COMPLETE

  dependencies:
    status: MODEL_COMPLETE_WITH_GAPS

  HML_applicability:
    status: MODEL_COMPLETE

  control_plane_requirements:
    status: MODEL_COMPLETE

  agents:
    status: MODEL_COMPLETE

  skills:
    status: MODEL_COMPLETE_FOR_CONTRACT_SCOPE

  workflows:
    status: MODEL_COMPLETE

  protocols:
    status: MODEL_COMPLETE

  evidence_provenance:
    status: MODEL_COMPLETE

  uncertainty_confidence:
    status: MODEL_COMPLETE

  failure_modes:
    status: MODEL_COMPLETE

  repair_recovery:
    status: MODEL_COMPLETE

  tests_validators:
    status: MODEL_COMPLETE_UNEXECUTED

  falsifiers:
    status: MODEL_COMPLETE

  canonical_skill_registry:
    status: UNKNOWN_GAP

  executable_skill_runtime:
    status: UNKNOWN_GAP

  runtime_validation:
    status: UNKNOWN_GAP

  formal_verification:
    status: UNKNOWN_GAP

  empirical_validation:
    status: UNKNOWN_GAP

  overall:
    status: COMPLETE_FOR_SKILL_CONTRACT_SCOPE

  conclusion_class:
    MODEL
```

---

# 31. Hard Boundaries

```text
PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

UNKNOWN/GAP != PASS
```

Skill-specific boundaries:

```text
SKILL != TRUTH

SKILL DOCUMENTATION != EXECUTION

SKILL AVAILABLE != SKILL INVOKED

SKILL INVOKED != SKILL EXECUTED

SKILL EXECUTED != SKILL VALIDATED

SKILL TEST PASS != UNIVERSAL CORRECTNESS

SKILL VALIDATED != AUTHORITY

AGENT + SKILL != AUTHORITY

SKILL OUTPUT != COMMIT

MULTIPLE SKILLS != INDEPENDENT EVIDENCE

MULTIPLE AGENTS != INDEPENDENT EVIDENCE

SKILL COMPOSITION != CONFIDENCE GAIN

MEMORY SKILL OUTPUT != CURRENT OBSERVATION

ATTENTION SKILL OUTPUT != TRUTH

BINDING SKILL OUTPUT != IDENTITY PROOF

HML SKILL OUTPUT != GLOBAL TRUTH

REPAIR SKILL OUTPUT != REVALIDATED STATE

CONTROL SKILL AVAILABLE != L03 CONTROL AUTHORITY

MODEL SKILL REGISTRY != IMPLEMENTED SKILL REGISTRY

IMPLEMENTED SKILL != VALIDATED SKILL

VALIDATED SKILL != EMPIRICAL COGNITIVE LAW
```

---

# 32. Governing Skill Contract

> **`L03_PERCEPT_FORMATION` SHALL use Skills only as bounded, typed, provenance-aware capabilities whose input contracts, output contracts, dependencies, preconditions, invariants, scope, regime, H/M/L applicability, execution state, tests, and authority envelopes remain explicit wherever material. A Skill SHALL NOT be treated as implemented merely because it is named or addressable; SHALL NOT be treated as validated merely because it executes; and SHALL NOT gain authority merely because its output is structurally valid. Skill composition SHALL preserve semantic origin, observation/derivation distinction, memory/observation distinction, uncertainty, confidence ceilings, provenance ancestry, competing percepts, scope, regime, observer context, freshness, and dependency lineage. Multiple Skills or agents processing the same ancestry SHALL NOT manufacture independent evidence or increase confidence by multiplicity alone. Failed Skill results SHALL selectively invalidate dependent outputs while preserving unaffected state. Repair SHALL require re-execution and revalidation. `UNKNOWN/GAP` SHALL remain non-passing. L03 Skills MAY analyze, transform, validate, repair, and propose percept state, but durable effects SHALL remain governed by the external control plane.**

---

# 33. Canon Boundary

```text
SOURCE / ARCHITECTURE-ALIGNED:

Trang Phan origin/stewardship

AMOS Skill Builder governance

integrity > completeness > fluency > speed > token savings

Skills as governed executable reasoning systems

typed state

smallest sufficient dependency closure

hard invariant gates

execution evidence

verification

challenge

repair

provenance preservation

promotion requires:
  ArchitectureCompatible
  ContractCompatible
  HardInvariantsPass
  SpecPass
  RegressionPass


AMOS_MODEL:

L03 Skill descriptor

L03 Skill categories

L03 candidate Skill registry

L03 Skill composition

L03 Skill admission

L03 Skill invocation protocol

L03 Skill execution trace

L03 H/M/L Skill mapping

L03 Skill failure taxonomy

L03 Skill repair workflow

L03 Skill test suite

L03 Skill promotion lifecycle


UNKNOWN/GAP:

direct canonical L03 Skill registry

canonical Skill identifiers

canonical Skill interfaces

canonical Skill versions

canonical composition rules

canonical capability manifests

canonical authority envelopes

canonical runtime integration

executed L03 Skill tests

formal verification

empirical perceptual validation
```

Therefore:

```text
CONCLUSION CLASS:
MODEL

GENERIC AMOS SKILL GOVERNANCE:
SOURCE-ALIGNED

L03-SPECIFIC SKILL CONTRACT:
MODEL

DIRECT L03 SKILL CANON:
UNKNOWN/GAP

IMPLEMENTATION:
UNKNOWN/GAP

RUNTIME VALIDATION:
UNKNOWN/GAP

FORMAL VERIFICATION:
UNKNOWN/GAP

EMPIRICAL HUMAN-PERCEPTION CLAIM:
NOT ESTABLISHED
```

---

00_ROOT_MOC|AMOS MOC

---
**Related:** [[00_HOME]] · [[COGNITIVE_MATRIX_MOC]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: l03_percept_formation_primitives_cognitive_matrix_skills
node_type: note
path: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L03_PERCEPT_FORMATION/L03_PERCEPT_FORMATION_PRIMITIVES_COGNITIVE_MATRIX_SKILLS.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[L03_PERCEPT_FORMATION_MOC]]
