---
tags: ['cognitive_matrix', 'primitives', 'l02_attention', 'note']
---

# L02_ATTENTION — Provenance

**Class:** `COGNITIVE_MATRIX_CONTRACT`
**Origin architect / steward:** Trang Phan  
**Status:** `CONTRACT_FILLED / NOT_IMPLEMENTED / NOT_VALIDATED`
**Filled by:** governed normalization pass · **Date:** `2026-08-26`

## Purpose

Define the AMOS contract for `L02_ATTENTION / PROVENANCE.md`.

## Source / Canon References

Current source basis:

* `L02_ATTENTION/PLACEHOLDER.md`
* `AMOS_COGNITIVE_CELL_REGISTRY.csv`
* `PRIMITIVE_REGISTRY.md`
* AMOS Full Brain OS / AMOS_CORE v4.4 lineage
* sibling L02 contracts where explicitly established

The recovered L02 placeholder identifies the primitive as attention allocation over scarce reasoning/observation resources. 

No canonical `PROVENANCE.md` has yet been recovered from the inspected `L02_ATTENTION` folder. The folder currently exposes the L02 placeholder rather than an independently validated provenance specification. 

Therefore:

```text
L02 provenance architecture below
=
AMOS_MODEL specification

not
=
recovered canonical L02 provenance implementation
```

---

## 1. Definition and Scope

`L02_ATTENTION` provenance records the origin, ancestry, transformation history, applicability envelope, and validation state of information used to allocate attention.

Conceptually:

[
Prov_{L02}(x)
=============

(origin, ancestry, transformations, evidence, scope,
regime, time, HML, authority, dependencies, status)
]

where `x` may be:

```text
observation
attention candidate
assessment
priority proposal
allocation proposal
focus state
escalation
memory recall
derived conclusion
repair
commit request
```

Provenance answers:

> **Where did this attention-relevant state come from, what transformations produced it, under what conditions is it valid, and what downstream states depend upon it?**

It does **not** determine truth by itself.

```text
PROVENANCE != TRUTH

TRACEABILITY != VALIDATION

SOURCE IDENTITY != SOURCE INDEPENDENCE

MULTIPLE REFERENCES != MULTIPLE ORIGINS
```

---

## 2. Typed Inputs

```yaml
ProvenanceInput:

  object_id: ObjectId

  object_class:
    type:
      - OBSERVATION
      - SOURCE_CLAIM
      - DERIVED
      - MODEL
      - DECISION
      - UNKNOWN_GAP

  source_refs:
    type: SourceRef[]

  parent_objects:
    type: ObjectRef[]

  transformations:
    type: TransformationRef[]

  evidence:
    type: EvidenceRef[]

  scope:
    type: ScopeEnvelope

  regime:
    type: RegimeRef

  hml:
    type: HMLCoordinate

  observation_time:
    type: Timestamp | UNKNOWN

  derivation_time:
    type: Timestamp | UNKNOWN

  freshness:
    type: FreshnessState

  authority:
    type: AuthorityContext | NONE

  dependencies:
    type: DependencyRef[]

  confidence:
    type: ConfidenceBound
```

---

## 3. Typed Outputs

```yaml
ProvenanceRecord:

  provenance_id: ProvenanceId

  object_id: ObjectId

  semantic_origin: SemanticOrigin

  immediate_sources: SourceRef[]

  ancestry: ProvenanceNode[]

  transformations: TransformationRef[]

  dependency_edges: DependencyEdge[]

  independence_state:
    type:
      - INDEPENDENT
      - CORRELATED
      - SHARED_ANCESTRY
      - UNKNOWN

  scope: ScopeEnvelope

  regime: RegimeRef

  hml: HMLCoordinate

  freshness: FreshnessState

  epistemic_class: EpistemicClass

  authority_state: AuthorityContext

  confidence_ceiling: ConfidenceBound

  validation_state:
    type:
      - VALIDATED
      - CONDITIONAL
      - QUARANTINED
      - INVALIDATED
      - UNKNOWN_GAP
```

---

## 4. State Variables

```text
Prov_t       = active provenance graph
Src_t        = source identities
Origin_t     = semantic origins
Anc_t        = ancestry relations
Dep_t        = dependency graph
Transform_t  = transformation history
Scope_t      = applicability scope
Regime_t     = active regime
Fresh_t      = freshness state
HML_t        = H/M/L coordinate
Auth_t       = authority context
Conflict_t   = provenance conflicts
Trust_t      = bounded source trust state
Conf_t       = confidence ceiling
Epoch_t      = validation/revalidation epoch
```

Candidate provenance node:

```yaml
ProvenanceNode:

  id: null
  source_id: null
  semantic_origin: null
  parent_ids: []
  transformation: null
  timestamp: null
  scope: null
  regime: null
  hml: null
  epistemic_class: UNKNOWN_GAP
  confidence_ceiling: 0
```

---

## 5. Operators

Candidate AMOS_MODEL operators:

```text
REGISTER_SOURCE()
RESOLVE_ORIGIN()
LINK_PARENT()
TRACE_ANCESTRY()
ADD_DEPENDENCY()
RECORD_TRANSFORMATION()

CHECK_SCOPE()
CHECK_REGIME()
CHECK_FRESHNESS()
CHECK_HML()

CHECK_INDEPENDENCE()
DETECT_SHARED_ANCESTRY()
DETECT_ALIAS()
DETECT_REPLAY()
DETECT_PROVENANCE_CONFLICT()

PROPAGATE_CONFIDENCE_CEILING()
PROPAGATE_INVALIDATION()

QUARANTINE()
REVALIDATE()
SUPERSEDE()
REPAIR_LINEAGE()
```

---

## 6. Core Provenance Invariants

```text
L02-PROV-INV-001
Every consequential attention object must have recoverable provenance.

L02-PROV-INV-002
Unknown provenance remains UNKNOWN/GAP.

L02-PROV-INV-003
Missing provenance cannot be synthesized as historical fact.

L02-PROV-INV-004
Derived objects retain dependency links to load-bearing premises.

L02-PROV-INV-005
Transformation does not erase semantic origin.

L02-PROV-INV-006
Aliases do not create independent evidence.

L02-PROV-INV-007
Copies do not create independent evidence.

L02-PROV-INV-008
Paraphrases do not automatically create independent evidence.

L02-PROV-INV-009
Multiple descendants of one source do not count as independent confirmation.

L02-PROV-INV-010
Source authority does not automatically establish claim validity.

L02-PROV-INV-011
Scope must propagate through derived claims.

L02-PROV-INV-012
Regime must propagate through derived claims.

L02-PROV-INV-013
Freshness constraints propagate to dependent attention states.

L02-PROV-INV-014
H/M/L transformations must remain traceable.

L02-PROV-INV-015
Epistemic class cannot silently strengthen through transformation.

L02-PROV-INV-016
Derived confidence cannot exceed the weakest load-bearing premise unless independently revalidated.

L02-PROV-INV-017
Contradictory provenance must remain visible.

L02-PROV-INV-018
Revoked or falsified provenance selectively invalidates descendants.

L02-PROV-INV-019
Unaffected provenance branches remain intact after local invalidation.

L02-PROV-INV-020
Provenance does not confer execution authority.

L02-PROV-INV-021
Addressable evidence is not automatically admissible evidence.

L02-PROV-INV-022
A provenance record is not proof of implementation.

L02-PROV-INV-023
A provenance record is not proof that the referenced claim is true.

L02-PROV-INV-024
MODEL-derived provenance cannot be relabelled CANON without source evidence.
```

---

## 7. Independence / Sybil Hardening

For evidence items:

[
E_1,E_2,\ldots,E_n
]

the count of references must be distinguished from the count of independent origins:

[
N_{independent}
\leq
N_{references}
]

Example:

```text
Source S
 ├─ Summary A
 ├─ Summary B
 └─ Agent report C
```

does not establish:

```text
3 independent confirmations
```

because all three may descend from `S`.

L02 attention allocation should therefore avoid giving additional epistemic weight merely because the same semantic origin appears repeatedly.

---

## 8. Semantic-Origin Resolution

Provenance must distinguish:

```text
FILE
AUTHOR
DOCUMENT VERSION
CLAIM
SEMANTIC ORIGIN
TRANSFORMATION
DERIVATIVE
```

Example:

```text
AMOS source
↓
summary
↓
RSCF capsule
↓
skill
↓
agent response
```

may represent several artifacts but one load-bearing semantic origin.

Candidate relation:

[
Origin(summary)
===============

# Origin(RSCF)

Origin(skill_claim)
]

where all are faithful descendants of the same original claim.

---

## 9. Dependency Provenance

Attention conclusions require explicit dependency edges.

```text
Observation
↓
Assessment
↓
Priority
↓
Allocation Proposal
```

If observation `O` is invalidated:

[
Invalid(O)
\Rightarrow
Invalidate(Descendants(O))
]

but:

```text
unrelated observations
unrelated candidates
unaffected allocations
```

must not automatically be invalidated.

This implements selective rather than global rollback.

---

## 10. Scope Provenance

Every consequential provenance capsule should preserve applicability:

```yaml
ScopeEnvelope:

  system: null
  population: null
  environment: null
  subsystem: null
  scale: null
  measurement_method: null
  assumptions: []
```

Hard invariant:

```text
SOURCE VALID IN SCOPE A
!=
SOURCE VALID IN SCOPE B
```

without transfer evidence.

---

## 11. Regime Provenance

```yaml
RegimeEnvelope:

  regime_id: null
  regime_definition: null
  valid_from: null
  valid_until: null
  assumptions: []
```

A regime shift may make previously valid attention evidence stale.

Therefore:

```text
historically valid
!=
currently applicable
```

---

## 12. Temporal Provenance

L02 should distinguish:

```text
source creation time
observation time
retrieval time
derivation time
validation time
decision time
commit time
```

Candidate:

```yaml
TemporalProvenance:

  source_time: null
  observation_time: null
  retrieval_time: null
  derivation_time: null
  validation_time: null
  use_time: null
```

These timestamps must not be silently collapsed.

---

## 13. H/M/L Provenance

### H — Governing provenance

Tracks:

```text
objectives
global constraints
authority
systemic evidence
governance decisions
cross-domain assumptions
```

### M — Subsystem provenance

Tracks:

```text
candidate pools
priority derivations
resource allocations
subsystem dependencies
escalations
```

### L — Local provenance

Tracks:

```text
observations
local measurements
focus transitions
operator inputs
local outcomes
```

Cross-scale transfer should retain lineage:

```text
L observation
→ M synthesis
→ H decision
```

The H-level synthesis must not erase the L/M evidence chain.

---

## 14. Provenance Across Compression

Because AMOS uses progressive disclosure:

```text
raw evidence
↓
L detail
↓
M synthesis
↓
H capsule
```

compression must preserve at minimum:

```text
claim identity
semantic origin
load-bearing dependencies
scope
regime
freshness
contradictions
confidence ceiling
falsifiers
recovery pointer
```

Compression may remove noncritical detail.

It may not remove load-bearing provenance.

---

## 15. Control-Plane Requirements

Infrastructure/control-plane validation is required when provenance participates in:

```text
durable state commit
memory admission
authority-bearing action
external disclosure
cross-agent effect
irreversible operation
shared resource allocation
policy enforcement
```

Control plane should validate, where applicable:

```text
source identity
semantic origin
ancestry
freshness
scope
regime
authority witness
dependency versions
revocation state
state version
```

L02 may propose provenance-bearing state.

It must not self-create authority merely because provenance exists.

---

## 16. Agents

Candidate logical roles:

```text
L02_PROVENANCE_RESOLVER
L02_ANCESTRY_TRACER
L02_INDEPENDENCE_AUDITOR
L02_FRESHNESS_VALIDATOR
L02_SCOPE_VALIDATOR
L02_REGIME_VALIDATOR
L02_PROVENANCE_CONFLICT_AGENT
L02_INVALIDATION_AGENT
L02_PROVENANCE_REPAIR_AGENT
```

These are `AMOS_MODEL` roles, not proof of implemented autonomous agents.

---

## 17. Skills

Relevant AMOS capability families include:

```text
provenance topology / Sybil hardening
provenance trust firewall
RSCF modeling
claim verification
information boundary governance
context state maintenance
execution provenance/replay
memory conflict governance
knowledge harvest
infrastructure control-plane governance
```

Skill presence means:

```text
CAPABILITY AVAILABLE
```

not:

```text
AUTHORITY GRANTED
```

---

## 18. Workflow

Candidate provenance workflow:

```text
RECEIVE OBJECT
↓
IDENTIFY SOURCE
↓
RESOLVE SEMANTIC ORIGIN
↓
TRACE ANCESTRY
↓
CLASSIFY EPISTEMIC TYPE
↓
CHECK SCOPE
↓
CHECK REGIME
↓
CHECK FRESHNESS
↓
CHECK DEPENDENCIES
↓
CHECK INDEPENDENCE
↓
CHECK CONTRADICTIONS
↓
CALCULATE CONFIDENCE CEILING
↓
ADMIT / QUARANTINE / REVALIDATE / REJECT
↓
PRESERVE LINEAGE
```

---

## 19. Protocols

Candidate protocol messages:

```text
PROVENANCE_REGISTER
PROVENANCE_QUERY
PROVENANCE_TRACE
PROVENANCE_VALIDATE
PROVENANCE_INDEPENDENCE_CHECK
PROVENANCE_CONFLICT_NOTICE
PROVENANCE_FRESHNESS_CHECK
PROVENANCE_REVALIDATION_REQUEST
PROVENANCE_INVALIDATION_NOTICE
PROVENANCE_SUPERSESSION_NOTICE
PROVENANCE_QUARANTINE
PROVENANCE_REPAIR
PROVENANCE_ACK
PROVENANCE_NACK
```

These remain `AMOS_MODEL` pending canonical recovery.

---

## 20. Evidence Classes

L02 provenance should preserve the distinction among:

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL
DECISION
UNKNOWN/GAP
```

Examples:

```text
"AMOS source says X"
=
SOURCE_CLAIM

"runtime trace recorded X"
=
OBSERVATION

"X and Y imply Z under assumptions"
=
DERIVED

"we propose architecture Z"
=
MODEL

"control plane selected Z"
=
DECISION

"origin unavailable"
=
UNKNOWN/GAP
```

No transformation may silently upgrade these classes.

---

## 21. Confidence Ceiling

Candidate rule:

[
C_{derived}
\le
\min(C_{load-bearing})
]

unless the conclusion has genuinely independent revalidation.

Provenance uncertainty dimensions:

```yaml
uncertainty:

  source_identity: null
  ancestry: null
  independence: null
  transformation_fidelity: null
  scope: null
  regime: null
  freshness: null
  dependency_completeness: null
```

Overall confidence must be bounded by material unresolved uncertainty.

---

## 22. Failure Modes

```text
FM-L02-PROV-001   Missing Source
FM-L02-PROV-002   Unknown Origin
FM-L02-PROV-003   Broken Ancestry
FM-L02-PROV-004   Provenance Stripping
FM-L02-PROV-005   Provenance Laundering
FM-L02-PROV-006   Alias-As-Independence
FM-L02-PROV-007   Copy-As-Independence
FM-L02-PROV-008   Paraphrase-As-Independence
FM-L02-PROV-009   Circular Provenance
FM-L02-PROV-010   Hidden Shared Ancestor
FM-L02-PROV-011   Scope Loss
FM-L02-PROV-012   Regime Loss
FM-L02-PROV-013   Freshness Loss
FM-L02-PROV-014   Timestamp Collapse
FM-L02-PROV-015   HML Lineage Loss
FM-L02-PROV-016   Transformation Loss
FM-L02-PROV-017   Dependency Loss
FM-L02-PROV-018   Revocation Ignored
FM-L02-PROV-019   Supersession Ignored
FM-L02-PROV-020   Confidence Inflation
FM-L02-PROV-021   Source Authority Substituted for Evidence
FM-L02-PROV-022   Contradiction Suppression
FM-L02-PROV-023   Global Invalidation From Local Failure
FM-L02-PROV-024   Stale Provenance Reuse
FM-L02-PROV-025   Model Provenance Reported as Canon
```

---

## 23. Repair / Recovery

```text
DETECT PROVENANCE FAILURE
↓
FREEZE DEPENDENT PROMOTION/COMMIT
↓
IDENTIFY EARLIEST INVALID NODE/EDGE
↓
TRACE DESCENDANTS
↓
PRESERVE UNAFFECTED BRANCHES
↓
RECOVER SOURCE OR ORIGIN
↓
REBUILD MINIMUM LINEAGE
↓
RECHECK SCOPE/REGIME/FRESHNESS
↓
RECHECK INDEPENDENCE
↓
RECOMPUTE CONFIDENCE CEILINGS
↓
REVALIDATE DESCENDANTS
↓
RESUME / QUARANTINE / INVALIDATE
```

No failed path should be retried without changed evidence or corrected lineage.

---

## 24. Tests / Validators

```text
TEST-L02-PROV-001
Every consequential object has provenance identity.

TEST-L02-PROV-002
Unknown origin remains UNKNOWN/GAP.

TEST-L02-PROV-003
Copying a source does not increase independent-source count.

TEST-L02-PROV-004
Paraphrasing does not automatically create independence.

TEST-L02-PROV-005
Shared ancestry is detected.

TEST-L02-PROV-006
Scope survives derivation.

TEST-L02-PROV-007
Regime survives derivation.

TEST-L02-PROV-008
Freshness survives derivation.

TEST-L02-PROV-009
H/M/L transfer preserves lineage.

TEST-L02-PROV-010
Compression preserves load-bearing provenance.

TEST-L02-PROV-011
Derived confidence cannot exceed weakest premise without revalidation.

TEST-L02-PROV-012
Contradictory sources remain visible.

TEST-L02-PROV-013
Revocation invalidates dependent descendants.

TEST-L02-PROV-014
Independent branches survive local invalidation.

TEST-L02-PROV-015
MODEL cannot become CANON through repeated citation.

TEST-L02-PROV-016
SOURCE_CLAIM cannot become OBSERVATION through summarization.

TEST-L02-PROV-017
Provenance does not grant authority.

TEST-L02-PROV-018
Addressability does not imply admissibility.

TEST-L02-PROV-019
Unexecuted provenance validator remains UNEXECUTED.

TEST-L02-PROV-020
Missing provenance cannot return PASS.
```

---

## 25. Adversarial Validators

Test specifically for:

```text
Sybil source multiplication
citation laundering
recursive self-citation
alias attacks
version substitution
stale-source replay
source spoofing
timestamp spoofing
authority spoofing
semantic-origin stripping
scope stripping
regime stripping
provenance graph cycles
hidden common ancestry
fabricated independence
confidence inflation
```

---

## 26. Falsifiers

This contract must be revised if recovered canon or executable evidence establishes that:

```text
L02 does not own provenance responsibilities;

attention provenance is exclusively infrastructure-owned;

canonical AMOS provenance uses materially different evidence classes;

canonical provenance does not propagate through H/M/L;

canonical confidence propagation differs;

canonical invalidation semantics differ;

canonical source-independence rules differ;

or runtime behavior materially contradicts this MODEL.
```

---

## 27. Gap Matrix

```yaml
gap_status:

  L02_role:
    status: SOURCE_SUPPORTED

  scarce_attention_resource_role:
    status: SOURCE_SUPPORTED

  provenance_requirement:
    status: SOURCE_SUPPORTED_AT_PLACEHOLDER_REQUIREMENT_LEVEL

  provenance_schema:
    status: MODEL_DEFINED

  semantic_origin:
    status: MODEL_DEFINED

  ancestry_tracking:
    status: MODEL_DEFINED

  independence_detection:
    status: MODEL_DEFINED

  scope_propagation:
    status: MODEL_DEFINED

  regime_propagation:
    status: MODEL_DEFINED

  freshness_propagation:
    status: MODEL_DEFINED

  HML_provenance:
    status: MODEL_DEFINED

  invalidation:
    status: MODEL_DEFINED

  repair:
    status: MODEL_DEFINED

  canonical_L02_provenance_spec:
    status: UNKNOWN/GAP

  canonical_provenance_schema:
    status: UNKNOWN/GAP

  canonical_source_identity_rules:
    status: UNKNOWN/GAP

  canonical_independence_algorithm:
    status: UNKNOWN/GAP

  canonical_confidence_equation:
    status: UNKNOWN/GAP

  runtime_implementation:
    status: UNKNOWN/GAP

  executed_tests:
    status: UNKNOWN/GAP

  formal_verification:
    status: UNKNOWN/GAP
```

---

## 28. RSCF Completion State

```yaml
claim_class: MODEL

claim:
  L02_ATTENTION requires provenance-preserving attention state
  so that source identity, semantic origin, ancestry, dependencies,
  scope, regime, freshness, H/M/L transformations, epistemic class,
  and confidence ceilings remain recoverable across attention allocation.

evidence:
  - L02_ATTENTION/PLACEHOLDER.md

provenance:
  origin_architect: Trang Phan
  architecture_family: AMOS
  primitive: L02_ATTENTION
  artifact: PROVENANCE.md
  derivation: SOURCE_BOUNDED_AMOS_MODEL

scope:
  system: AMOS_OS
  subsystem: COGNITIVE_MATRIX
  primitive: L02_ATTENTION
  concern: provenance

regime:
  governed_attention_allocation

freshness:
  revalidate_when:
    - canonical L02 provenance source is recovered
    - canonical provenance topology changes
    - L02 state or operator contract changes
    - AMOS_CORE provenance semantics change
    - executable runtime evidence becomes available

dependencies:
  - L01_SENSING_OBSERVATION
  - L02_ATTENTION_DEFINITION
  - L02_ATTENTION_STATE
  - L02_ATTENTION_VARIABLES
  - L02_ATTENTION_OPERATORS
  - L02_ATTENTION_INVARIANTS
  - L02_ATTENTION_DEPENDENCIES
  - L02_ATTENTION_HML
  - L02_ATTENTION_PROTOCOLS
  - L02_ATTENTION_CONTROL_PLANES

competing:
  - provenance owned directly by L02
  - provenance owned by shared cognitive infrastructure
  - provenance owned entirely by AMOS control plane
  - hybrid local-plus-infrastructure provenance

falsifiers:
  - recovered canon assigns provenance elsewhere
  - canonical schemas materially contradict this model
  - runtime implementation contradicts modeled lineage semantics

uncertainty:
  evidence: HIGH
  model: MEDIUM
  scope: MEDIUM
  temporal: MEDIUM
  causal: LOW
  execution: HIGH
  provenance_independence: MEDIUM

confidence_ceiling:
  source-supported statements are limited to the recovered
  L02 role and placeholder completion requirements;
  detailed provenance structures remain MODEL.

gap_status:
  canonical_provenance_contract: CRITICAL_GAP
  canonical_schema: CRITICAL_GAP
  runtime_implementation: CRITICAL_GAP
  executed_validation: CRITICAL_GAP
```

## Hard Boundaries

```text
PLACEHOLDER != IMPLEMENTED
ADDRESSABLE != VALIDATED
CAPABILITY != AUTHORITY
PROPOSAL != COMMIT
UNKNOWN/GAP != PASS

PROVENANCE != TRUTH
SOURCE != CLAIM
CITATION != VALIDATION
COPY != INDEPENDENT SOURCE
PARAPHRASE != INDEPENDENT SOURCE
MULTIPLE DESCENDANTS != MULTIPLE ORIGINS
TRACEABLE != CORRECT
AUTHORITATIVE SOURCE != AUTOMATICALLY TRUE
MODEL LINEAGE != CANON LINEAGE
DOCUMENTED != IMPLEMENTED
IMPLEMENTED != VALIDATED
```

**Conclusion class: `MODEL`.** The provenance contract is structurally specified, but canonical L02 provenance semantics, executable implementation, and executed validation remain `UNKNOWN/GAP`.

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00-Home]] · [[COGNITIVE_MATRIX_MOC]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: l02_attention_primitives_cognitive_matrix_provenance
node_type: note
path: 25_COGNITIVE_MATRIX/01_PRIMITIVES/L02_ATTENTION/L02_ATTENTION_PRIMITIVES_COGNITIVE_MATRIX_PROVENANCE.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
