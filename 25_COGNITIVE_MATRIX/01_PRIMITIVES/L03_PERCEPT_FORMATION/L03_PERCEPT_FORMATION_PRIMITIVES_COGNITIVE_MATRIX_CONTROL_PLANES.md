---
type: control-plane
source: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L03_PERCEPT_FORMATION
tags:
- amos
- cognitive-matrix
- matrix/l03
- percept-formation
- control-plane
- perception
- provenance
- rscf
- hml
- governance
- domain/cognitive-matrix
- 00-root-moc
- amos-moc
- 00-home
- cognitive-matrix-moc
- amos-rscf-nodes
- l03-percept-formation-moc
title: L03_PERCEPT_FORMATION — Control Planes
origin_architect: Trang Phan
status: MODEL_CONTROL_PLANE_CONTRACT / UNIMPLEMENTED / UNVALIDATED
epistemic_class: MODEL
runtime_alignment: AMOS Full Brain OS / AMOS_CORE v4.4 lineage
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# L03_PERCEPT_FORMATION — Control Planes

**Class:** `COGNITIVE_PRIMITIVE_CONTROL_PLANE_CONTRACT`
**Origin architect / steward:** Trang Phan
**Primitive:** `L03_PERCEPT_FORMATION`
**Artifact:** `CONTROL_PLANES.md`
**Status:** `AMOS_MODEL / UNIMPLEMENTED / UNVALIDATED`

> **Canon boundary:** This artifact defines a source-bounded AMOS control-plane contract for percept formation. The governing infrastructure pattern is supported by the AMOS Infrastructure Control Plane: domain/cognitive workers produce typed evidence and proposals; infrastructure validates evidence, observed read sets, semantic transactions, constraints, provenance, authority, observability, and finalization. Detailed L03-specific object names, thresholds, topology, and implementation remain `AMOS_MODEL` unless independently recovered from direct canon or executable runtime evidence.

---

# 0. Purpose

Define how `L03_PERCEPT_FORMATION` is governed separately from the workers that construct percepts.

The core separation is:

```text
L01 observations
→ L02 attention
→ L03 percept workers
→ typed percept evidence/proposals
→ L03 control-plane validation
→ authoritative percept-state decision
```

The control plane exists to prevent:

```text
percept generation
=
percept authority
```

The governing rule is:

```text
COGNITION PROPOSES
CONTROL VALIDATES
AUTHORITY AUTHORIZES
COMMIT FINALIZES
```

For L03 specifically:

```text
OBSERVATION
!=
PERCEPT

PERCEPT
!=
FACT

PERCEPT CANDIDATE
!=
ACCEPTED PERCEPT STATE

AGENT AGREEMENT
!=
VALIDATION

VALIDATION
!=
AUTHORITY

PROPOSAL
!=
COMMIT
```

---

# 1. Source / Canon References

## 1.1 Source-aligned architecture

Relevant AMOS architecture includes:

```text
AMOS Full Brain OS
AMOS cognition architecture
AMOS_CORE v3.0 → v4.4 lineage
AMOS Infrastructure Control Plane
AMOS Multimodal Perception Layer
AMOS H/M/L
AMOS RSCF
AMOS provenance topology
AMOS constraint propagation
AMOS uncertainty/confidence governance
AMOS selective invalidation / repair
```

The AMOS Infrastructure Control Plane explicitly separates:

```text
Environment
→ Domain Skills
→ Typed Evidence ABI
→ AMOS Control Plane
→ Commit / Action
```

and requires control-plane handling of typed contracts, evidence bundles, observed read sets, semantic transactions, authorization, constraints, observability, authority witnesses, and commit results.

## 1.2 L03 mapping

For this primitive the generic architecture is mapped as:

```text
Environment
↓
L01_SENSING_OBSERVATION
↓
L02_ATTENTION
↓
L03_PERCEPT_FORMATION workers
↓
L03 typed percept evidence
↓
AMOS control plane
↓
Percept-state commit / downstream release
```

This mapping is `AMOS_MODEL`; it is not evidence that canonical L03 uses these exact runtime objects.

## 1.3 Canon gaps

```yaml
canonical_L03_control_plane_name: UNKNOWN_GAP
canonical_L03_control_plane_schema: UNKNOWN_GAP
canonical_L03_commit_protocol: UNKNOWN_GAP
canonical_L03_authority_model: UNKNOWN_GAP
canonical_L03_thresholds: UNKNOWN_GAP
canonical_L03_runtime_implementation: UNKNOWN_GAP
canonical_L03_executed_validation: UNKNOWN_GAP
```

---

# 2. Definition and Scope

The `L03_PERCEPT_FORMATION` control plane is the governing layer that validates whether percept proposals may modify authoritative percept state or be released downstream.

It governs:

```text
input admissibility
observation lineage
attention-state compatibility
percept proposal typing
scope
regime
freshness
observer context
modality availability
dependency closure
provenance
conflict preservation
confidence ceilings
authority
state freshness
commit eligibility
selective invalidation
repair/recovery
```

It does **not** itself need to perform primary percept inference.

Hard separation:

```text
PERCEPT WORKER:
"What percept might these observations support?"

CONTROL PLANE:
"Is this percept proposal admissible, current,
traceable, authorized, and safe to commit?"
```

---

# 3. Typed Inputs

```yaml
L03ControlPlaneInput:

  task_contract:
    type: TASK_CONTRACT

  percept_proposal:
    type: PerceptStateProposal

  percept_candidates:
    type: PerceptCandidate[]

  competing_percepts:
    type: CompetingPercept[]

  attended_observations:
    type: ObservationRef[]

  attention_state:
    type: AttentionStateRef

  evidence_bundle:
    type: DOMAIN_EVIDENCE | PerceptEvidenceBundle

  observed_read_set:
    type: OBSERVED_READ_SET

  semantic_transaction:
    type: SEMANTIC_TRANSACTION | null

  observer_context:
    type: ObserverContext

  modality_state:
    type: ModalityAvailability

  temporal_context:
    type: TemporalContext

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeRef

  freshness:
    type: FreshnessState

  constraints:
    type: CONSTRAINT_CONTEXT

  provenance:
    type: ProvenanceBundle

  authorization:
    type: AUTHORIZATION_SPEC

  authority_witness:
    type: AUTHORITY_WITNESS | null

  observability:
    type: OBSERVABILITY_ENVELOPE | null

  hml:
    type: HMLContext

  authoritative_state:
    type: PerceptStateSnapshot
```

---

# 4. Typed Outputs

```yaml
L03ControlPlaneOutput:

  decision:
    type:
      - COMMITTABLE
      - ACCEPT_MODEL_STATE
      - ACCEPT_CONDITIONAL
      - PRESERVE_COMPETING
      - REVALIDATE_STALE_READ
      - REVALIDATE_CONSTRAINTS
      - REVALIDATE_OBSERVABILITY
      - BLOCK_EVIDENCE
      - BLOCK_CONFLICT
      - BLOCK_PROVENANCE
      - BLOCK_SCOPE
      - BLOCK_REGIME
      - BLOCK_AUTHORITY
      - BLOCK_OBSERVABILITY
      - BLOCK_SEMANTIC_TRANSACTION
      - BLOCK_STATE_VERSION
      - UNKNOWN_GAP

  accepted_percepts:
    type: PerceptRef[]

  competing_percepts:
    type: CompetingPercept[]

  rejected_percepts:
    type: RejectedPercept[]

  invalidated_percepts:
    type: PerceptRef[]

  uncertainty:
    type: PerceptUncertainty

  confidence_ceiling:
    type: ConfidenceBound

  required_revalidation:
    type: RevalidationRequest[]

  repair_request:
    type: RepairRequest | null

  provenance:
    type: ProvenanceBundle

  commit_result:
    type: COMMIT_RESULT | null
```

---

# 5. State Variables

```text
Obs_t       = authoritative observation references
Attn_t      = accepted attention state
Per_t       = authoritative percept state
Cand_t      = candidate percepts
Comp_t      = competing percepts
Read_t      = observed read set
Dep_t       = dependency graph
Prov_t      = provenance graph
Scope_t     = applicability scope
Reg_t       = regime
Fresh_t     = freshness state
ObsCtx_t    = observer context
Mod_t       = modality availability
Con_t       = constraint context
Auth_t      = authorization state
Authority_t = authority witness state
HML_t       = H/M/L coordinates
Unc_t       = uncertainty vector
Conf_t      = confidence ceilings
Epoch_t     = validation/state epoch
Repair_t    = repair state
```

Where mutable state identity should not rely solely on an unqualified scalar version if relevant state can change independently. The infrastructure control-plane contract instead uses precise observed read sets and version/hash identity for decision-forming resources.

---

# 6. Control-Plane Objects

Where applicable, L03 should compose with the generic AMOS control-plane ABI rather than inventing a parallel governance system.

Relevant generic objects are:

```text
TASK_CONTRACT
CAPABILITY_MANIFEST
RESOLVED_CAPABILITY_CONTRACT
DOMAIN_EVIDENCE
OBSERVED_READ_SET
SEMANTIC_TRANSACTION
AUTHORIZATION_SPEC
OBSERVABILITY_ENVELOPE
AUTHORITY_WITNESS
CONSTRAINT_CONTEXT
EFFECT_INTENT
COMMIT_RESULT
```

These object families are source-aligned with the AMOS Infrastructure Control Plane.

Candidate L03 projections:

```text
DOMAIN_EVIDENCE
→ PERCEPT_EVIDENCE

OBSERVED_READ_SET
→ PERCEPT_READ_SET

SEMANTIC_TRANSACTION
→ PERCEPT_SEMANTIC_TRANSACTION

EFFECT_INTENT
→ PERCEPT_STATE_INTENT
```

These aliases are `MODEL`, not recovered canonical identifiers.

---

# 7. Operators

```text
VALIDATE_TASK()
VALIDATE_INPUT_TYPES()
VALIDATE_OBSERVATION_LINEAGE()
VALIDATE_ATTENTION_CONTEXT()
VALIDATE_PERCEPT_EVIDENCE()
VALIDATE_BINDINGS()
VALIDATE_MODALITY_STATE()
VALIDATE_OBSERVER_CONTEXT()
VALIDATE_SCOPE()
VALIDATE_REGIME()
VALIDATE_FRESHNESS()
VALIDATE_PROVENANCE()
VALIDATE_READ_SET()
VALIDATE_DEPENDENCY_CLOSURE()
VALIDATE_CONSTRAINTS()
VALIDATE_COMPETING()
VALIDATE_CONFIDENCE_CEILING()
VALIDATE_SEMANTIC_TRANSACTION()
VALIDATE_OBSERVABILITY()
VALIDATE_AUTHORITY()
COMPARE_AUTHORITATIVE_STATE()
INVALIDATE_DESCENDANTS()
STAGE_PERCEPT_UPDATE()
COMMIT_PERCEPT_UPDATE()
ROLLBACK()
REVALIDATE()
```

---

# 8. Core Invariants

```text
L03-CP-INV-001
Observation identity must survive percept formation.

L03-CP-INV-002
Percept proposals cannot rewrite their supporting observations.

L03-CP-INV-003
Percept formation cannot manufacture missing evidence.

L03-CP-INV-004
UNKNOWN/GAP cannot satisfy an evidence gate.

L03-CP-INV-005
Unresolved material percept conflicts remain COMPETING.

L03-CP-INV-006
Agent consensus does not establish provenance independence.

L03-CP-INV-007
Multiple transformations of one observation do not constitute
multiple independent observations.

L03-CP-INV-008
Scope must remain compatible from observation through percept.

L03-CP-INV-009
Regime must remain compatible from observation through percept.

L03-CP-INV-010
Observer-dependent evidence cannot silently become observer-independent.

L03-CP-INV-011
Unavailable modality cannot be treated as negative evidence.

L03-CP-INV-012
Stale decision-forming state requires revalidation.

L03-CP-INV-013
Changes to unread state must not automatically invalidate a percept.

L03-CP-INV-014
A changed read object invalidates only dependent descendants.

L03-CP-INV-015
Confidence cannot exceed the weakest load-bearing premise unless
independently revalidated.

L03-CP-INV-016
Capability does not create authority.

L03-CP-INV-017
Validation does not create authority.

L03-CP-INV-018
Proposal does not equal commit.

L03-CP-INV-019
A worker cannot self-authorize its own durable state mutation.

L03-CP-INV-020
Hard invariant failure is non-compensatory.
```

The fine-grained read-set behavior aligns with the infrastructure rule that unread-object changes should not invalidate a decision, while changes to actually read resources invalidate only dependent conclusions.

---

# 9. Dependency Model

Primary chain:

```text
L00_REALITY_ENVIRONMENT
↓
L01_SENSING_OBSERVATION
↓
L02_ATTENTION
↓
L03_PERCEPT_FORMATION
```

Control-plane dependency set:

```yaml
dependencies:
  cognitive:
    - L01_SENSING_OBSERVATION
    - L02_ATTENTION
    - L03_PERCEPT_FORMATION_DEFINITION
    - L03_PERCEPT_FORMATION_STATE
    - L03_PERCEPT_FORMATION_OPERATORS
    - L03_PERCEPT_FORMATION_INVARIANTS
    - L03_PERCEPT_FORMATION_PROVENANCE

  governance:
    - AMOS_INFRASTRUCTURE_CONTROL_PLANE
    - RSCF
    - PROVENANCE_TOPOLOGY
    - CONSTRAINT_PROPAGATION
    - AUTHORITY_GOVERNANCE
    - UNCERTAINTY_GOVERNANCE

  execution:
    - authoritative_state_store
    - validation_epoch
    - observed_read_set
    - commit_guard
```

---

# 10. H/M/L Applicability

## H — Governing percept state

Controls:

```text
global percept frame
environment/world-model percept state
major scope/regime changes
high-impact conflicts
system-wide percept invalidation boundaries
```

H-level conclusions must not overwrite unresolved M/L evidence.

## M — Percept subsystem governance

Controls:

```text
object/event groups
cross-modal integrations
subsystem percepts
multi-observation bindings
competing percept families
```

## L — Local percept governance

Controls:

```text
one observation
one binding
one feature
one timestamp
one source
one modality
one provenance edge
```

Cross-scale rule:

```text
L VALIDATION
!=
M VALIDATION
!=
H VALIDATION
```

unless the required dependency closure is explicitly established.

---

# 11. Control-Plane Requirements

The L03 control plane should provide:

```text
authoritative percept-state ownership
typed evidence admission
observed-read-set tracking
dependency-aware freshness
scope/regime enforcement
observer-context preservation
provenance verification
conflict preservation
confidence-ceiling enforcement
semantic transaction validation
authority verification
state-version / hash checking
staging
commit
rollback
selective invalidation
revalidation
auditability
```

For consequential downstream effects, the broader infrastructure control plane additionally requires commit-time rechecks of intent, policy, tool-catalog context, authority, semantic lineage, and observability.

---

# 12. Agents

Candidate L03 workers include:

```text
L03_PERCEPT_COORDINATOR
L03_OBSERVATION_NORMALIZER
L03_FEATURE_BINDER
L03_MULTIMODAL_INTEGRATOR
L03_TEMPORAL_BINDER
L03_SPATIAL_CONTEXT_AGENT
L03_OBSERVER_CONTEXT_AGENT
L03_PERCEPT_HYPOTHESIS_GENERATOR
L03_PERCEPT_DISCRIMINATOR
L03_CROSS_MODAL_CONFLICT_AGENT
L03_PERCEPT_UNCERTAINTY_AGENT
L03_PERCEPT_PROVENANCE_AGENT
L03_PERCEPT_REPAIR_AGENT
L03_PERCEPT_AUDITOR
```

These are modeled roles.

Default authority:

```text
worker:
  may_read: bounded
  may_infer: yes
  may_propose: yes
  may_validate_local: bounded
  may_commit_authoritative_state: no
```

---

# 13. Skills

Relevant AMOS capability families include:

```text
AMOS Infrastructure Control Plane
AMOS Multimodal Perception Layer
AMOS Sensory Map Integrator
AMOS Binding RSCF Engine
AMOS Temporal Multi-Scale RSCF Engine
AMOS Constraint Propagation RSCF Engine
AMOS Provenance Trust Firewall
AMOS Metacognitive Confidence Auditor
RSCF Modeler
```

Hard separation:

```text
SKILL EXISTS
!=
SKILL INVOKED

SKILL INVOKED
!=
RESULT VALIDATED

RESULT VALIDATED
!=
COMMIT AUTHORITY
```

---

# 14. Workflow

```text
RECEIVE L03 PERCEPT PROPOSAL
↓
VALIDATE TASK / CAPABILITY CONTRACT
↓
VALIDATE INPUT TYPES
↓
VALIDATE OBSERVATION ANCESTRY
↓
VALIDATE L02 ATTENTION CONTEXT
↓
VALIDATE PERCEPT EVIDENCE
↓
BUILD / CHECK OBSERVED READ SET
↓
CHECK SCOPE + REGIME + FRESHNESS
↓
CHECK OBSERVER + MODALITY STATE
↓
CHECK PROVENANCE
↓
PRESERVE MATERIAL CONFLICTS
↓
CHECK CONFIDENCE CEILING
↓
VALIDATE SEMANTIC TRANSACTION
↓
CHECK AUTHORITATIVE STATE FRESHNESS
↓
CHECK AUTHORITY
↓
STAGE UPDATE
↓
FINAL REVALIDATION
↓
COMMIT OR BLOCK
```

For durable effects, the source control-plane architecture explicitly requires commit-time rechecking rather than trusting a previously computed PASS.

---

# 15. Protocols

Candidate L03 protocols:

```text
L03_CP_SUBMIT_PERCEPT_PROPOSAL
L03_CP_REQUEST_EVIDENCE
L03_CP_REQUEST_READ_SET
L03_CP_CONFLICT_NOTICE
L03_CP_REVALIDATE_REQUEST
L03_CP_STALE_STATE_NOTICE
L03_CP_SCOPE_BLOCK
L03_CP_REGIME_BLOCK
L03_CP_PROVENANCE_BLOCK
L03_CP_AUTHORITY_BLOCK
L03_CP_STAGE_UPDATE
L03_CP_COMMIT_REQUEST
L03_CP_COMMIT_RESULT
L03_CP_ROLLBACK
L03_CP_REPAIR_REQUEST
```

Canonical protocol names remain `UNKNOWN/GAP`.

---

# 16. Evidence / Provenance

Every accepted percept should be traceable through:

```text
PERCEPT STATE
↓
PERCEPT PROPOSAL
↓
BINDING / INTEGRATION OPERATIONS
↓
ATTENDED OBSERVATIONS
↓
L01 OBSERVATIONS
↓
SOURCE / SENSOR / TOOL ORIGIN
```

Minimum provenance structure:

```yaml
PerceptCommitProvenance:

  percept_id: null
  proposal_id: null

  observation_refs: []
  attention_state_ref: null

  worker_refs: []
  transformation_refs: []

  semantic_origins: []

  read_set: []

  scope: null
  regime: null
  observer_context: null
  modality_state: null

  validation_epoch: null

  authorization_spec_ref: null
  authority_witness_ref: null

  validator_refs: []

  state_before_hash: null
  state_after_hash: null

  commit_result: null
```

The actual execution/provenance graph must remain separate from the authorization specification; the infrastructure control-plane contract explicitly requires this separation.

---

# 17. Semantic Transaction

A percept-state mutation should not be accepted merely because every local step individually looks valid.

Candidate L03 semantic rule:

[
PerceptTxPass =
LineageDAG
\land
ObservationIntegrity
\land
PerceptStaged
\land
AuthorizedSources
\land
NoForbiddenSemanticFlow
\land
ConstraintCompatible
]

This is an L03 specialization of the infrastructure semantic-transaction pattern:

```text
SemanticTransactionPass
=
LineageDAG
AND EffectStaged
AND ParameterSourcesAuthorized
AND NoForbiddenLabelFlow
AND AuthorizationSpecClean
```

which the infrastructure recomputes at commit rather than trusting a caller-supplied PASS.

---

# 18. Observability

For consequential percept-dependent actions, merely recording agent messages is insufficient.

The control plane should know whether it can observe:

```text
critical percept variables
observation ancestry
uncertainty
scope
regime
observer context
cross-modal conflict
percept-state mutation
downstream consequence pathways
known blind spots
```

Hard boundary:

```text
TELEMETRY EXISTS
!=
CRITICAL-PATH OBSERVABILITY
```

This follows the infrastructure requirement that named telemetry channels or span counts do not prove observability coverage.

---

# 19. Authority

Authority should be explicit and externally governed relative to the percept worker.

Candidate authorization relation:

[
AuthorizedCommit(P)
===================

ValidEvidence(P)
\land
ValidState(P)
\land
ValidConstraints(P)
\land
ValidAuthority(P)
]

No worker may infer:

```text
"I generated P"
therefore
"I may commit P"
```

Authority must be current at commit where a durable/consequential effect is involved.

---

# 20. Uncertainty and Confidence Ceiling

```yaml
uncertainty:
  observation: null
  attention: null
  binding: null
  multimodal: null
  temporal: null
  spatial: null
  observer: null
  provenance: null
  scope: null
  regime: null
  freshness: null
  authority: null
  execution: null
```

For load-bearing premises:

[
C(P)
\le
\min_i C(p_i)
]

unless independently revalidated evidence changes the dependency graph.

A control-plane PASS cannot raise confidence beyond the evidence it validates.

Therefore:

```text
GOVERNANCE SUCCESS
!=
EMPIRICAL TRUTH
```

---

# 21. Failure Modes

```text
FM-L03-CP-001
Worker self-commits percept state.

FM-L03-CP-002
Proposal treated as authoritative state.

FM-L03-CP-003
Observation ancestry lost.

FM-L03-CP-004
Percept rewrites supporting observation.

FM-L03-CP-005
Stale percept state committed.

FM-L03-CP-006
Unread-state change causes unnecessary global invalidation.

FM-L03-CP-007
Changed read dependency fails to invalidate descendants.

FM-L03-CP-008
Material competing percept suppressed.

FM-L03-CP-009
Correlated evidence counted independently.

FM-L03-CP-010
Observer context collapsed.

FM-L03-CP-011
Unavailable modality treated as evidence.

FM-L03-CP-012
Scope leakage.

FM-L03-CP-013
Regime leakage.

FM-L03-CP-014
Confidence inflation.

FM-L03-CP-015
Stale authority accepted.

FM-L03-CP-016
Caller-supplied PASS trusted without revalidation.

FM-L03-CP-017
Semantic transaction incomplete.

FM-L03-CP-018
Telemetry presence mistaken for observability.

FM-L03-CP-019
Repair deletes unaffected percept state.

FM-L03-CP-020
UNKNOWN/GAP promoted to PASS.
```

---

# 22. Repair / Recovery

```text
DETECT FAILED CONTROL CONDITION
↓
FREEZE AFFECTED PERCEPT COMMIT
↓
IDENTIFY FAILED PREMISE / READ / EDGE
↓
TRACE DEPENDENT PERCEPT DESCENDANTS
↓
INVALIDATE ONLY DEPENDENT STATE
↓
PRESERVE UNAFFECTED PERCEPT STATE
↓
REQUEST NEW OBSERVATION / REVALIDATION IF REQUIRED
↓
RE-RUN REQUIRED WORKERS
↓
REBUILD AFFECTED PROVENANCE
↓
REVALIDATE CONSTRAINTS + AUTHORITY
↓
RESTAGE
↓
COMMIT OR REMAIN BLOCKED
```

Core rule:

[
Invalid(p)
\Rightarrow
Invalidate(Descendants(p))
]

not:

[
Invalid(p)
\Rightarrow
Invalidate(AllState)
]

unless dependency closure proves system-wide dependence.

---

# 23. Tests / Validators

Minimum validators:

```text
VALIDATE_L03_CONTROL_INPUT
VALIDATE_OBSERVATION_ANCESTRY
VALIDATE_ATTENTION_DEPENDENCY
VALIDATE_PERCEPT_EVIDENCE
VALIDATE_READ_SET
VALIDATE_SCOPE
VALIDATE_REGIME
VALIDATE_FRESHNESS
VALIDATE_OBSERVER_CONTEXT
VALIDATE_MODALITY_STATE
VALIDATE_PROVENANCE
VALIDATE_COMPETING
VALIDATE_CONFIDENCE_CEILING
VALIDATE_SEMANTIC_TRANSACTION
VALIDATE_AUTHORITY
VALIDATE_STATE_FRESHNESS
VALIDATE_SELECTIVE_INVALIDATION
VALIDATE_COMMIT_BOUNDARY
```

Minimum tests:

```text
TEST-L03-CP-001
Worker proposes valid percept without authority.
Expected:
BLOCK_AUTHORITY.

TEST-L03-CP-002
Supporting observation changes after proposal.
Expected:
REVALIDATE_STALE_READ.

TEST-L03-CP-003
Unrelated unread state changes.
Expected:
percept remains eligible.

TEST-L03-CP-004
One load-bearing observation is invalidated.
Expected:
only dependent percept descendants invalidated.

TEST-L03-CP-005
Two material percept hypotheses remain unresolved.
Expected:
PRESERVE_COMPETING.

TEST-L03-CP-006
Several agents derive outputs from one source.
Expected:
no false provenance independence.

TEST-L03-CP-007
Observer context becomes incompatible.
Expected:
block/revalidate affected percept.

TEST-L03-CP-008
Regime changes before commit.
Expected:
REVALIDATE_CONSTRAINTS or equivalent block.

TEST-L03-CP-009
Caller submits semantic_transaction.pass=true with invalid lineage.
Expected:
recompute and reject.

TEST-L03-CP-010
UNKNOWN/GAP satisfies a required validator.
Expected:
BLOCK / UNKNOWN_GAP, never PASS.
```

Execution status:

```text
NOT_RUN
```

unless separate runtime evidence is supplied.

---

# 24. Falsifiers

Revise this contract if direct evidence establishes that:

```text
L03 does not own percept-state formation;

L03 percept state is not mutable or authoritative;

canonical AMOS assigns L03 workers direct commit authority;

canonical L03 uses materially different control-plane boundaries;

L03 has no observation ancestry requirement;

canonical state freshness semantics conflict with read-set governance;

canonical H/M/L applicability differs materially;

runtime evidence contradicts proposed validation ordering;

executed tests falsify stated invariants.
```

---

# 25. Competing Architectures

## COMPETING-001 — Worker-Owned State

```text
percept worker
→ inference
→ direct state mutation
```

Benefit:

```text
low coordination cost
```

Risk:

```text
capability/authority collapse
weak auditability
```

---

## COMPETING-002 — Central Percept Controller

```text
workers
→ one L03 controller
→ state
```

Benefit:

```text
simple authority boundary
```

Risk:

```text
centralized bottleneck
hidden global coupling
```

---

## COMPETING-003 — Infrastructure-Owned Governance

```text
L03 workers
→ typed percept evidence
→ generic AMOS infrastructure control plane
→ authoritative state
```

Benefit:

```text
reuse of shared governance
clear cognition/control separation
```

Risk:

```text
domain-specific percept semantics require capability adapters
```

---

## COMPETING-004 — Hybrid

```text
L03-local deterministic validators
+
generic infrastructure authority/finality
+
bounded percept workers
```

Current model preference:

```text
COMPETING-004
```

because percept-specific validation can remain close to L03 while authoritative state, provenance, authority, and finalization remain infrastructure-owned.

This remains `MODEL`, not canonical proof.

---

# 26. Gap Matrix

```yaml
gap_status:

  infrastructure_control_plane_pattern:
    status: SOURCE_ALIGNED

  cognition_control_separation:
    status: MODEL_ALIGNED

  typed_evidence_boundary:
    status: SOURCE_ALIGNED

  observed_read_set:
    status: SOURCE_ALIGNED

  semantic_transaction:
    status: SOURCE_ALIGNED

  authorization_separation:
    status: SOURCE_ALIGNED

  commit_time_revalidation:
    status: SOURCE_ALIGNED

  L03_mapping:
    status: MODEL_DEFINED

  L03_control_plane_objects:
    status: MODEL_DEFINED

  L03_validation_sequence:
    status: MODEL_DEFINED

  L03_authoritative_state_schema:
    status: UNKNOWN_GAP

  canonical_L03_control_plane:
    status: UNKNOWN_GAP

  canonical_L03_protocols:
    status: UNKNOWN_GAP

  canonical_L03_thresholds:
    status: UNKNOWN_GAP

  executable_L03_control_plane:
    status: UNKNOWN_GAP

  executed_validation:
    status: UNKNOWN_GAP
```

---

# 27. RSCF Completion State

```yaml
rscf:

  id: L03_PERCEPT_FORMATION_CONTROL_PLANES

  claim:
    L03 percept formation can be governed through a control-plane
    boundary that separates percept generation from authoritative
    state mutation and validates evidence, provenance, observed
    dependencies, scope, regime, freshness, conflicts, constraints,
    authority, and commit eligibility.

  claim_class: MODEL

  evidence:
    - AMOS Infrastructure Control Plane source architecture
    - AMOS multimodal perception architecture
    - AMOS cognition / Full Brain OS architecture
    - AMOS H/M/L and RSCF conventions

  provenance:
    origin_architect: Trang Phan
    architecture_family: AMOS
    subsystem: COGNITIVE_MATRIX
    primitive: L03_PERCEPT_FORMATION
    artifact: CONTROL_PLANES.md
    derivation: AMOS_MODEL_SOURCE_BOUNDED

  scope:
    system: AMOS_OS
    subsystem: COGNITIVE_MATRIX
    primitive: L03_PERCEPT_FORMATION
    concern: percept_control_plane

  regime:
    governed percept formation

  freshness:
    revalidate_when:
      - canonical L03 control-plane source is recovered
      - authoritative percept-state schema changes
      - control-plane contract changes
      - provenance semantics change
      - authority semantics change
      - runtime evidence becomes available

  dependencies:
    - L01_SENSING_OBSERVATION
    - L02_ATTENTION
    - L03_PERCEPT_FORMATION_AGENTS
    - L03_PERCEPT_FORMATION_STATE
    - L03_PERCEPT_FORMATION_OPERATORS
    - L03_PERCEPT_FORMATION_INVARIANTS
    - L03_PERCEPT_FORMATION_PROVENANCE
    - AMOS_INFRASTRUCTURE_CONTROL_PLANE

  competing:
    - worker-owned percept state
    - centralized L03 controller
    - generic infrastructure-owned governance
    - hybrid local validation plus infrastructure finalization

  falsifiers:
    - incompatible direct L03 canon
    - incompatible canonical authority ownership
    - incompatible state semantics
    - runtime evidence contradicting governance topology
    - executed validator failures

  uncertainty:
    evidence: MEDIUM
    model: MEDIUM
    scope: MEDIUM
    temporal: MEDIUM
    causal: LOW
    execution: MAXIMUM
    provenance_independence: MEDIUM

  confidence_ceiling:
    Infrastructure governance principles are source-aligned.
    Their detailed application to L03 remains MODEL until direct
    L03 canon and executable runtime evidence establish the mapping.

  gap_status:
    canonical_L03_control_plane: CRITICAL_GAP
    canonical_state_schema: CRITICAL_GAP
    executable_control_plane: CRITICAL_GAP
    executed_validation: CRITICAL_GAP

  cheapest_discriminating_test:
    Recover direct L03 control-plane/state canon; then implement a
    minimal typed percept proposal harness and test observation
    ancestry, read-set freshness, competing-percept preservation,
    selective invalidation, semantic-transaction recomputation,
    authority separation, and proposal/commit isolation.
```

---

# 28. Completion State

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
    status: MODEL_COMPLETE

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
    status: MODEL_COMPLETE

  workflows:
    status: MODEL_COMPLETE

  protocols:
    status: MODEL_COMPLETE

  evidence_provenance:
    status: MODEL_COMPLETE_SOURCE_PARTIAL

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

  canonical_control_plane:
    status: UNKNOWN_GAP

  executable_runtime:
    status: UNKNOWN_GAP

  runtime_validation:
    status: UNKNOWN_GAP

  overall:
    status: COMPLETE_FOR_CONTROL_PLANE_CONTRACT_SCOPE

  conclusion_class:
    MODEL
```

---

# 29. Hard Boundaries

```text
PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

UNKNOWN/GAP != PASS
```

L03-specific:

```text
OBSERVATION != PERCEPT

PERCEPT != FACT

PERCEPT != CAUSAL PROOF

PERCEPT WORKER != CONTROL PLANE

LOCAL VALIDATION != GLOBAL VALIDATION

AGENT CONSENSUS != PROVENANCE INDEPENDENCE

VALIDATION != AUTHORITY

AUTHORITY WITNESS != EMPIRICAL TRUTH

STATE VERSION != COMPLETE STATE IDENTITY

TELEMETRY != OBSERVABILITY PROOF

STALE PASS != CURRENT PASS

MODEL CONTROL PLANE != IMPLEMENTED CONTROL PLANE

IMPLEMENTED CONTROL PLANE != VALIDATED CONTROL PLANE
```

---

# 30. Governing Control-Plane Contract

> **`L03_PERCEPT_FORMATION` SHALL separate percept construction from authoritative percept-state control. Percept workers MAY normalize observations, bind features, integrate modalities, generate hypotheses, preserve competing percepts, estimate uncertainty, and propose state changes. They SHALL NOT derive authority from capability or self-commit authoritative state. The governing control plane SHALL validate observation ancestry, attended-input dependencies, evidence, scope, regime, freshness, observer and modality context, provenance, material conflicts, confidence ceilings, semantic lineage, current constraints, authoritative state identity, and applicable authority before commit. Changes SHALL invalidate only dependency-connected percept state where dependency closure permits selective invalidation. UNKNOWN/GAP SHALL never satisfy a required gate.**

---

# 31. Canon Boundary

```text
SOURCE-ALIGNED:

Trang Phan origin/stewardship

AMOS Infrastructure Control Plane architecture

typed evidence boundary

observed read-set governance

semantic transaction validation

authorization/execution provenance separation

constraint freshness

commit-time authority revalidation

observability governance

selective invalidation


AMOS_MODEL:

mapping generic control plane onto L03

L03-specific control objects

L03-specific protocol names

percept semantic transaction specialization

validation ordering

local-vs-infrastructure governance partition

candidate decision vocabulary


UNKNOWN/GAP:

canonical L03 control-plane name

canonical L03 state schema

canonical L03 commit protocol

canonical L03 authority schema

canonical L03 thresholds

runtime implementation

executed tests

formal verification
```

Therefore:

```text
CONCLUSION CLASS:
MODEL

NOT:
VERIFIED COMPLETE L03 CANON

NOT:
PROOF OF IMPLEMENTATION

NOT:
PROOF OF PERCEPTUAL TRUTH

NOT:
PROOF OF HUMAN COGNITIVE MECHANISM

NOT:
AUTHORITY TO COMMIT
```

```text

The strongest source-grounded part is the generic AMOS control-plane boundary: typed evidence, fine-grained observed read sets, semantic-transaction recomputation, authorization separation, observability, commit-time freshness, and authority checks are explicitly defined there. The **mapping of those controls onto `L03_PERCEPT_FORMATION` remains `MODEL`** until direct L03 canon or executable evidence establishes it.
```

---

[[00_ROOT_MOC]]|[[AMOS MOC]]

---
**Related:** [[00_HOME]] · [[COGNITIVE_MATRIX_MOC]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: l03_percept_formation_primitives_cognitive_matrix_control_planes
node_type: note
path: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L03_PERCEPT_FORMATION/L03_PERCEPT_FORMATION_PRIMITIVES_COGNITIVE_MATRIX_CONTROL_PLANES.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[L03_PERCEPT_FORMATION_MOC]]
