---
type: memory
source: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L02_ATTENTION
tags:
- amos
- cognitive-matrix
- l02
- attention
- memory
- rscf
- governance
- canon/cognitive-matrix
title: "L02_ATTENTION — Memory"
origin_architect: "Trang Phan"
status: "MODEL_SPECIFICATION / SOURCE-BOUNDED / UNVALIDATED"
epistemic_class: "MODEL"
runtime_alignment: "AMOS Full Brain OS / AMOS_CORE v4.4 lineage"
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


# L02_ATTENTION — Memory

**Class:** `COGNITIVE_PRIMITIVE_MEMORY_CONTRACT`  
**Origin architect / steward:** Trang Phan  
**Primitive:** `L02_ATTENTION`  
**Artifact:** `MEMORY.md`  
**Status:** `AMOS_MODEL / SOURCE-BOUNDED / UNVALIDATED`

> **Canon boundary:** Drive evidence confirms that AMOS treats `MEMORY` as an explicit cognitive-cell concern, while the primitive registry separately identifies `L07 — MEMORY` with only partial source maturity. Therefore this artifact defines **memory used by L02 attention**, not the canonical semantics of the dedicated L07 memory primitive.

---

# 0. Purpose

Define what state `L02_ATTENTION` may retain, reuse, invalidate, externalize, or hand off so that attention allocation can operate across cycles without confusing:

```text
attention history
with
evidence

cached priority
with
current priority

remembered observation
with
current observation

retrieved memory
with
truth

memory availability
with
authority
```

Core boundary:

```text
L02_MEMORY
=
memory supporting attention allocation

L02_MEMORY
!=
L07_MEMORY

MEMORY
!=
EVIDENCE

MEMORY
!=
TRUTH

MEMORY
!=
AUTHORITY

RECALL
!=
REVALIDATION
```

---

# 1. Source / Canon References

## 1.1 Direct Drive evidence

The AMOS cognitive-cell registry contains explicit `MEMORY` cells and marks durable-memory binding as requiring control-plane treatment rather than treating addressability as validation. 

The primitive registry separately lists:

```text
L07 — MEMORY — source maturity partial
```

which establishes an important namespace boundary: memory is itself a dedicated primitive elsewhere in the cognitive architecture. 

## 1.2 L02 source basis

Available AMOS corpus search also identifies the large `AMOS_CORE - FULL.md` lineage artifact as a relevant source candidate for attention semantics, but the search result alone does not establish a canonical L02 memory contract. 

Therefore:

```text
SOURCE-SUPPORTED:
MEMORY exists as an explicit AMOS cognitive concern.
L07_MEMORY exists as a distinct primitive.
Durable memory requires governance/control-plane consideration.

NOT YET SOURCE-ESTABLISHED:
canonical L02 memory variables
canonical L02 memory operators
canonical retention equations
canonical L02↔L07 protocol
```

## 1.3 Related contracts

```text
L02_ATTENTION — README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION — HML
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README
L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_README

L01_SENSING_OBSERVATION
L07_MEMORY
```

---

# 2. Definition and Scope

`L02_ATTENTION_MEMORY` is the governed state required to preserve decision-relevant information about previous attention operations.

Its purpose is to answer questions such as:

```text
What was attended to?
Why was it attended to?
What was deferred?
What remained unresolved?
Which priorities were previously computed?
Which evidence/provenance objects supported them?
Which allocations failed?
Which paths should not be repeated unchanged?
Which state has become stale?
```

It does **not** establish a universal long-term memory architecture.

Formally, as an AMOS model:

[
M^{L02}_t
=========

{
A_t,
H_t,
D_t,
G_t,
P_t,
F_t,
X_t
}
]

where:

* \(A_t\) = active attention state,
* \(H_t\) = relevant attention history,
* \(D_t\) = deferred/unresolved items,
* \(G_t\) = gap/contradiction state,
* \(P_t\) = provenance/dependency references,
* \(F_t\) = freshness/applicability state,
* \(X_t\) = invalidation/recovery state.

This equation is `AMOS_MODEL`, not recovered canon.

---

# 3. Typed Inputs

```yaml
AttentionMemoryInput:

  attention_state:
    type: AttentionState

  allocation_event:
    type: AttentionAllocationEvent?

  candidate_state:
    type: AttentionCandidate[]

  observations:
    type: ObservationRef[]

  evidence:
    type: EvidenceRef[]

  provenance:
    type: ProvenanceBundle

  dependencies:
    type: DependencyGraph

  unresolved_gaps:
    type: GapRef[]

  competing_hypotheses:
    type: HypothesisRef[]

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeRef

  freshness:
    type: FreshnessState

  authority:
    type: AuthorityEnvelope

  retention_request:
    type: MemoryRetentionProposal?
```

---

# 4. Typed Outputs

```yaml
AttentionMemoryOutput:

  working_memory_state:
    type: AttentionWorkingMemory

  retained_refs:
    type: MemoryRef[]

  deferred_refs:
    type: MemoryRef[]

  quarantined_refs:
    type: MemoryRef[]

  invalidated_refs:
    type: MemoryRef[]

  externalization_proposals:
    type: MemoryWriteProposal[]

  retrieval_hints:
    type: RetrievalHint[]

  provenance:
    type: ProvenanceBundle

  uncertainty:
    type: UncertaintyVector

  confidence_ceiling:
    type: ConfidenceBound

  gap_status:
    type: GapStatus
```

A `MemoryWriteProposal` is not a durable write:

```text
MemoryWriteProposal
!=
MemoryCommit
```

---

# 5. State Variables

```text
WM_t       active L02 working-memory state
AH_t       attention-history references
AR_t       active attention references
DR_t       deferred references
UR_t       unresolved references
QR_t       quarantined references
IR_t       invalidated references

Pri_t      cached priority state
Alloc_t    prior allocation state

Prov_t     provenance state
Dep_t      dependency state

Scope_t    applicability scope
Reg_t      regime
Fresh_t    freshness

Comp_t     competing-hypothesis state
Contr_t    contradiction state
Gap_t      gap state

Ret_t      retention class
Exp_t      expiration/revalidation condition
```

---

# 6. Memory Classes

L02 should distinguish at least:

```text
ACTIVE
DEFERRED
UNRESOLVED
QUARANTINED
INVALIDATED
EXTERNALIZED
EXPIRED
```

It should also distinguish semantic role:

```text
OBSERVATION_REF
EVIDENCE_REF
PRIORITY_STATE
ALLOCATION_HISTORY
DEPENDENCY_REF
PROVENANCE_REF
GAP_REF
CONTRADICTION_REF
COMPETING_REF
RECOVERY_REF
```

These classes must not be silently merged.

---

# 7. Operators

Proposed L02 memory operators:

```text
REGISTER(x)
RETAIN(x)
RECALL(x)
REFRESH(x)
DEFER(x)
EXTERNALIZE(x)
QUARANTINE(x)
INVALIDATE(x)
EXPIRE(x)
COMPRESS(x)
RESTORE(x)
LINK_PROVENANCE(x,p)
LINK_DEPENDENCY(x,d)
```

### REGISTER

Create an addressable L02 memory reference.

```text
REGISTER != VALIDATE
```

### RETAIN

Preserve a state item across an attention transition.

### RECALL

Return previously retained information to the active attention context.

```text
RECALL != CURRENT_TRUTH
```

### REFRESH

Revalidate freshness/applicability before reuse when required.

### DEFER

Preserve an item without allocating current attention.

### EXTERNALIZE

Propose moving information from active context into persistent storage.

### QUARANTINE

Prevent uncertain or contaminated memory from affecting ordinary allocation.

### INVALIDATE

Mark memory unusable for downstream conclusions under affected dependency closure.

### COMPRESS

Reduce memory footprint while preserving load-bearing distinctions.

### RESTORE

Recover a valid previous memory state after failure.

---

# 8. Invariants

## MEM-INV-001 — Memory ≠ Truth

[
Recall(x)\not\Rightarrow True(x)
]

## MEM-INV-002 — Memory ≠ Evidence

A stored claim remains typed according to its original epistemic class.

```text
MODEL stored in memory
=
MODEL

not
VERIFIED
```

## MEM-INV-003 — Recall ≠ Revalidation

Retrieving an old result does not renew its freshness.

## MEM-INV-004 — Provenance Preservation

Material memory must retain recoverable semantic origin.

## MEM-INV-005 — Scope Preservation

Stored information retains its original applicability envelope.

## MEM-INV-006 — Regime Preservation

A regime-bound conclusion remains regime-bound after recall.

## MEM-INV-007 — Confidence Non-Inflation

[
Conf(recalled(x)) \le Conf(valid(x))
]

Recall itself cannot increase confidence.

## MEM-INV-008 — Invalid Memory Cannot Silently Reactivate

```text
INVALIDATED
→
ACTIVE
```

requires revalidation or explicit repair.

## MEM-INV-009 — Contradictions Survive Retention

Compression must not erase unresolved contradictory evidence.

## MEM-INV-010 — COMPETING Survives Retention

Competing hypotheses remain competing until discriminating evidence exists.

## MEM-INV-011 — Durable Memory Requires Governance

L02 may propose persistent retention.

It does not obtain durable write authority merely by identifying useful memory.

## MEM-INV-012 — L02 Memory ≠ L07 Ownership

L02 may consume or propose memory objects without claiming ownership of the canonical `L07_MEMORY` primitive.

---

# 9. Dependencies

Primary conceptual dependency chain:

```text
L01_SENSING_OBSERVATION
        ↓
L02_ATTENTION
        ↓
L02 working attention state
        ↓
memory proposal / handoff
        ↓
memory/control-plane layer
```

Relevant dependencies:

```yaml
dependencies:

  upstream:
    - L01_SENSING_OBSERVATION

  local:
    - L02_ATTENTION_STATE
    - L02_ATTENTION_VARIABLES
    - L02_ATTENTION_OPERATORS
    - L02_ATTENTION_INVARIANTS
    - L02_ATTENTION_PROVENANCE
    - L02_ATTENTION_CONTROL_PLANES

  cross_primitive:
    - L07_MEMORY

  infrastructure:
    - provenance
    - dependency tracking
    - freshness
    - scope/regime
    - authority
    - durable state governance
```

The exact canonical dependency graph remains `UNKNOWN/GAP`.

---

# 10. H/M/L Applicability

## H — Governing Memory

Preserve:

```text
objective
hard constraints
authority boundaries
critical unresolved gaps
governing contradictions
scope/regime
```

H-level memory should be small and load-bearing.

## M — Subsystem Memory

Preserve:

```text
active attention branches
candidate families
allocation rationale
dependency structures
competing hypotheses
repair state
```

## L — Local Memory

Preserve only detail needed for current or likely near-term resolution:

```text
specific observations
individual source references
local calculations
tool-result pointers
candidate-specific diagnostics
```

Core invariant:

```text
L detail may be compressed or externalized
only if H/M decision-relevant structure remains recoverable.
```

---

# 11. Control-Plane Requirements

The control plane should own durable-memory effects involving:

```text
persistent write
overwrite
deletion
cross-session retention
retention-policy change
authority-sensitive state
shared memory
recipient change
declassification
revocation
```

Minimum boundary:

```text
L02:
  SELECT
  RECALL
  DEFER
  RANK
  PROPOSE_RETENTION
  PROPOSE_INVALIDATION

CONTROL PLANE:
  AUTHORIZE_WRITE
  VALIDATE_PROVENANCE
  VALIDATE_FRESHNESS
  VALIDATE_SCOPE
  COMMIT
  REVOKE
  DELETE
```

Drive evidence supports the general need to distinguish memory addressability from durable control-plane validation. 

---

# 12. Agents

Proposed logical roles:

```text
L02_MEMORY_COORDINATOR
L02_RECALL_AGENT
L02_RETENTION_AUDITOR
L02_STALENESS_AUDITOR
L02_MEMORY_PROVENANCE_AUDITOR
L02_COMPACTION_AUDITOR
L02_MEMORY_RECOVERY_AGENT
```

These are architectural roles.

```text
ROLE DEFINITION
!=
IMPLEMENTED AGENT
```

---

# 13. Skills

Potential AMOS capabilities:

```text
AMOS Attention Allocation Governor
AMOS Context State Maintenance RSCF
AMOS Context Compaction Recoverability RSCF
AMOS Distinct Working Memory RSCF
AMOS Agent Memory Dynamics RSCF
AMOS Memory Conflict Governor
AMOS Memory Immune System
AMOS Action Memory Firewall
AMOS Provenance Trust Firewall
AMOS Infrastructure Control Plane
AMOS RSCF Modeler
```

Skill availability does not prove canonical dependency or runtime use.

---

# 14. Workflow

```text
RECEIVE attention result
↓
CLASSIFY memory relevance
↓
TYPE epistemic class
↓
ATTACH provenance
↓
ATTACH scope/regime/freshness
↓
CHECK dependency importance
↓
CHECK contradiction/COMPETING state
↓
SELECT:
    retain active
    defer
    externalize
    quarantine
    invalidate
    discard noncritical redundancy
↓
IF durable effect requested
    submit MemoryWriteProposal
↓
CONTROL-PLANE VALIDATION
↓
COMMIT / REJECT / QUARANTINE
```

---

# 15. Protocol

```yaml
L02AttentionMemoryCapsule:

  primitive: L02_ATTENTION

  memory_id: null

  semantic_role: null

  epistemic_class: null

  source_ref: null

  provenance: []

  dependencies: []

  scope: null
  regime: null
  freshness: null

  retention:
    class: null
    reason: null
    expires_when: null
    revalidate_when: []

  contradiction_state: null
  competing_state: null

  lifecycle_state:
    enum:
      - ACTIVE
      - DEFERRED
      - EXTERNALIZED
      - QUARANTINED
      - INVALIDATED
      - EXPIRED

  authority:
    proposal_authorized: null
    durable_commit_authorized: null

  confidence_ceiling: 0

  gaps: []
```

---

# 16. Evidence / Provenance

Every material memory object should preserve:

```text
semantic origin
source identity
transformation lineage
epistemic class
scope
regime
freshness
dependencies
confidence ceiling
invalidation conditions
```

Where independence matters:

```text
multiple memories
derived from one source
!=
multiple independent sources
```

Persistent recollection must not reset ancestry.

---

# 17. Uncertainty and Confidence Ceiling

```yaml
uncertainty:

  evidence:
    level: HIGH
    reason: direct canonical L02 memory specification not established

  model:
    level: MEDIUM
    reason: contract follows AMOS memory/provenance governance patterns

  scope:
    level: MEDIUM_HIGH
    reason: boundary between L02 local memory and L07_MEMORY requires canon resolution

  temporal:
    level: MEDIUM
    reason: persistent memory may become stale

  causal:
    level: LOW_MEDIUM
    reason: remembered priority must not be mistaken for causal importance

  execution:
    level: HIGH
    reason: no L02 memory runtime enforcement established here

  provenance_independence:
    level: MEDIUM
    reason: AMOS artifacts may share lineage
```

Confidence ceiling:

```text
existence of AMOS MEMORY concern:
SOURCE-SUPPORTED

existence of distinct L07_MEMORY:
SOURCE-SUPPORTED

detailed L02 memory contract:
MODEL

runtime enforcement:
UNKNOWN/GAP
```

---

# 18. Failure Modes

```text
FM-MEM-001  stale-memory reuse
FM-MEM-002  provenance loss
FM-MEM-003  scope leakage
FM-MEM-004  regime leakage
FM-MEM-005  confidence inflation through repetition
FM-MEM-006  memory treated as evidence
FM-MEM-007  invalidated memory reactivation
FM-MEM-008  contradiction deletion
FM-MEM-009  COMPETING collapse
FM-MEM-010  attention-history overload
FM-MEM-011  destructive over-compression
FM-MEM-012  persistent retention without authority
FM-MEM-013  L02/L07 ownership collision
FM-MEM-014  duplicated semantic origin counted independently
FM-MEM-015  repeated failed-path recall
FM-MEM-016  irrelevant memory capturing current attention
FM-MEM-017  local memory overwriting governing H state
```

---

# 19. Repair / Recovery

General repair:

```text
detect memory failure
↓
identify affected memory object
↓
identify dependency descendants
↓
quarantine invalid object
↓
preserve unaffected memory
↓
recover provenance / scope / freshness
↓
revalidate
↓
selectively restore valid descendants
```

Stale memory:

```text
STALE
→ suspend reuse
→ reacquire/revalidate
→ update freshness
→ recompute dependent attention priorities
```

Poisoned memory:

```text
QUARANTINE
→ trace ancestry
→ identify contaminated descendants
→ selectively invalidate
→ preserve independent state
```

Compaction loss:

```text
restore externalized source
→ reconstruct missing distinction
→ rerun dependent allocation only
```

---

# 20. Tests / Validators

Minimum validators:

```text
VALIDATE_MEMORY_TYPE
VALIDATE_EPISTEMIC_CLASS
VALIDATE_PROVENANCE
VALIDATE_SCOPE
VALIDATE_REGIME
VALIDATE_FRESHNESS
VALIDATE_DEPENDENCIES
VALIDATE_CONFIDENCE_CEILING
VALIDATE_CONTRADICTION_RETENTION
VALIDATE_COMPETING_RETENTION
VALIDATE_INVALIDATION_STATE
VALIDATE_L02_L07_BOUNDARY
VALIDATE_RETENTION_AUTHORITY
VALIDATE_COMPACTION_RECOVERABILITY
VALIDATE_SELECTIVE_INVALIDATION
```

Minimum tests:

```text
TEST-MEM-001
Recall stale priority.
Expected:
revalidation required.

TEST-MEM-002
Store MODEL claim and recall repeatedly.
Expected:
remains MODEL.

TEST-MEM-003
Recall three summaries derived from one source.
Expected:
one provenance ancestry family.

TEST-MEM-004
Recall evidence outside original regime.
Expected:
regime gate.

TEST-MEM-005
Attempt durable write without authority.
Expected:
PROPOSAL only / no commit.

TEST-MEM-006
Invalidate one local memory branch.
Expected:
dependent descendants invalidated;
independent branches preserved.

TEST-MEM-007
Compress unresolved contradiction away.
Expected:
FAIL.

TEST-MEM-008
Attempt to treat L02 local retention as implementation of L07_MEMORY.
Expected:
FAIL / namespace boundary violation.

TEST-MEM-009
Budget pressure causes externalization.
Expected:
provenance and recovery pointer preserved.

TEST-MEM-010
Recall previous failed path with unchanged evidence.
Expected:
do not blindly repeat path.
```

---

# 21. Falsifiers

Revise this specification if canonical evidence establishes that:

```text
L02 has no memory interaction

L02 itself canonically owns all persistent memory

L07_MEMORY is not a distinct primitive

attention memory may discard provenance

recall canonically renews freshness

memory may independently increase confidence

persistent writes require no control-plane authorization

H/M/L does not apply to memory interaction

canonical L02 memory semantics materially differ
```

Runtime implementation claims are falsified if durable memory effects occur outside the declared governance boundary.

---

# 22. Gap Status

```yaml
gap_status:

  memory_as_AMOS_concern:
    status: SOURCE_SUPPORTED

  L07_memory_as_distinct_primitive:
    status: SOURCE_SUPPORTED

  durable_memory_governance_need:
    status: SOURCE_SUPPORTED_PARTIAL

  L02_memory_definition:
    status: MODEL_DEFINED

  L02_memory_variables:
    status: MODEL_DEFINED

  L02_memory_operators:
    status: MODEL_DEFINED

  L02_memory_invariants:
    status: MODEL_DEFINED

  L02_L07_interface:
    status: CRITICAL_GAP

  canonical_retention_classes:
    status: UNKNOWN/GAP

  canonical_expiration_rules:
    status: UNKNOWN/GAP

  canonical_memory_equations:
    status: UNKNOWN/GAP

  runtime_implementation:
    status: UNKNOWN/GAP

  executed_tests:
    status: UNKNOWN/GAP

  durable_commit_validation:
    status: UNKNOWN/GAP
```

The most important unresolved issue is:

```text
What is the canonical ownership/interface boundary between
L02 attention-local memory
and
L07_MEMORY?
```

---

# 23. RSCF Completion State

```yaml
rscf:

  id: L02_ATTENTION_MEMORY

  claim:
    L02_ATTENTION requires bounded memory of decision-relevant attention
    state so allocation can preserve unresolved work, provenance,
    applicability, dependencies, and recovery information across cycles,
    while persistent memory remains separately governed.

  claim_class: MODEL

  evidence:
    - AMOS cognitive registry contains explicit MEMORY cells
    - primitive registry identifies distinct L07_MEMORY
    - AMOS governance requires provenance and controlled durable state

  provenance:
    origin_architect: Trang Phan
    architecture_family: AMOS
    subsystem: COGNITIVE_MATRIX
    primitive: L02_ATTENTION
    artifact: MEMORY.md
    derivation: SOURCE_BOUNDED_AMOS_MODEL

  scope:
    system: AMOS_OS
    subsystem: COGNITIVE_MATRIX
    primitive: L02_ATTENTION
    concern: attention_supporting_memory

  regime:
    governed cognitive architecture specification

  freshness:
    revalidate_when:
      - canonical L02 memory source is recovered
      - canonical L07 interface is recovered
      - persistent-memory architecture changes
      - AMOS_CORE lineage changes relevant memory semantics
      - executable runtime becomes available

  dependencies:
    - L01_SENSING_OBSERVATION
    - L02_ATTENTION_STATE
    - L02_ATTENTION_VARIABLES
    - L02_ATTENTION_OPERATORS
    - L02_ATTENTION_INVARIANTS
    - L02_ATTENTION_PROVENANCE
    - L02_ATTENTION_CONTROL_PLANES
    - L07_MEMORY

  competing:
    - L02 owns only ephemeral working memory
    - L02 owns attention history but not durable memory
    - all memory semantics belong to L07
    - infrastructure owns persistent memory while L07 provides cognitive semantics
    - memory is cross-cutting rather than exclusively owned by one primitive

  falsifiers:
    - canonical source assigns incompatible ownership
    - runtime implements validated incompatible semantics
    - L07 is shown not to be the relevant memory primitive
    - durable memory is canonically local to L02

  confidence_ceiling:
    detailed L02 memory semantics remain MODEL until direct canon resolves
    the L02-L07 boundary and executable validation establishes enforcement

  gap_status:
    L02_L07_boundary: CRITICAL
    canonical_memory_contract: CRITICAL
    runtime_enforcement: CRITICAL
    executed_validation: DECISION_RELEVANT

  cheapest_discriminating_test:
    retrieve direct L02 and L07 canonical definitions and dependency/interface
    material, then determine which layer owns working state, attention history,
    persistent retention, invalidation, and commit authority
```

---

# 24. Hard Boundaries

```text
PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

UNKNOWN/GAP != PASS
```

Memory extensions:

```text
MEMORY != TRUTH

MEMORY != EVIDENCE

RECALL != REVALIDATION

RETENTION != VALIDATION

REPETITION != INDEPENDENT CONFIRMATION

CACHE HIT != CURRENT APPLICABILITY

PERSISTENCE != CORRECTNESS

L02_MEMORY != L07_MEMORY

MEMORY WRITE PROPOSAL != DURABLE COMMIT

COMPRESSION != PERMISSION TO DELETE LOAD-BEARING STATE

INVALIDATED != FORGOTTEN

EXPIRED != FALSE

DOCUMENTED MEMORY != IMPLEMENTED MEMORY
```

---

# 25. Completion State

```yaml
completion_state:

  source_canon_references:
    status: PARTIAL / DRIVE-REFERENCED

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
    status: MODEL_COMPLETE / CANON_BOUNDARY_OPEN

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
    status: SOURCE_PARTIAL / MODEL_COMPLETE

  uncertainty_confidence:
    status: MODEL_COMPLETE

  failure_modes:
    status: MODEL_COMPLETE

  repair_recovery:
    status: MODEL_COMPLETE

  tests_validators:
    status: MODEL_COMPLETE / UNEXECUTED

  falsifiers:
    status: MODEL_COMPLETE

  gap_status:
    status: EXPLICIT / CRITICAL_GAPS_OPEN

  overall:
    status: COMPLETE_FOR_MODEL_SPECIFICATION_SCOPE

  conclusion_class:
    MODEL
```

# 26. Governing Memory Contract

> **`L02_ATTENTION` may retain and retrieve the smallest sufficient state needed to allocate scarce attention coherently across cycles, but memory reuse must preserve epistemic class, provenance, dependencies, scope, regime, freshness, contradictions, competing hypotheses, and confidence ceilings. Recall does not constitute evidence or revalidation. L02 may propose durable retention, invalidation, or externalization, but durable effects remain subject to the appropriate control plane. The exact ownership boundary between L02 attention memory and the distinct `L07_MEMORY` primitive remains a critical canonical gap.**

# 27. Conclusion Class

```text
SOURCE-SUPPORTED:
AMOS explicitly contains MEMORY as a cognitive concern.
L07_MEMORY is represented as a distinct primitive.

MODEL:
the detailed L02 attention-memory contract above.

UNKNOWN/GAP:
canonical L02↔L07 interface,
canonical retention equations,
runtime implementation,
executed validation.

CONCLUSION:
MODEL
```

```text
```

---

00_ROOT_MOC|AMOS MOC

---
**Related:** [[00_HOME]] · [[COGNITIVE_MATRIX_MOC]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: l02_attention_primitives_cognitive_matrix_memory
node_type: note
path: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L02_ATTENTION/L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_MEMORY.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[L02_ATTENTION_MOC]]
