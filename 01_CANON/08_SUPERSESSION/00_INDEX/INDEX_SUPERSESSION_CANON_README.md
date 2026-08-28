---
title: INDEX SUPERSESSION CANON README
type: index
source: 01_CANON/08_SUPERSESSION/00_INDEX
tags:
- 00_INDEX
- canon/universe
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: index_navigation
---

# INDEX SUPERSESSION CANON README

## 1. Purpose

`INDEX_SUPERSESSION_CANON_README.md` is the canonical navigation and indexing artifact for the AMOS supersession subsystem.

Its purpose is to make supersession artifacts:

- addressable,
- discoverable,
- dependency-visible,
- provenance-linked,
- version-aware,
- scope-aware,
- auditable,
- and safely resolvable.

This artifact does **not** itself supersede another artifact.

It does **not** grant authority to supersede canon.

It does **not** convert a proposal into committed canon.

It does **not** establish that a replacement artifact is superior, validated, executable, or authoritative.

Its role is indexing and controlled resolution.

```text
INDEXING != AUTHORITY
DISCOVERY != VALIDATION
REFERENCE != DEPENDENCY PROOF
NEWER != SUPERIOR
SUPERSESSION PROPOSAL != SUPERSESSION COMMIT
SUPERSEDED != DELETED
REPLACED != FORGOTTEN
CAPABILITY != AUTHORITY
UNKNOWN/GAP != PASS
```

The index therefore acts as an entry point into the supersession control structure while preserving the distinction between:

```text
what exists
what is indexed
what claims to supersede something
what is authorized to supersede something
what has actually been committed
what remains historically recoverable
```

---

# 2. Canonical role of supersession

AMOS treats supersession as a governed lineage transition rather than ordinary replacement.

A canonical artifact may evolve from one state or version to another, but the transition must preserve sufficient lineage to answer:

```text
What existed before?
What replaces it?
Why was replacement proposed?
Who or what authorized the transition?
Which evidence supported it?
Which dependencies are affected?
Which conclusions become stale?
Which artifacts remain valid?
Can the previous state be reconstructed?
What would invalidate the supersession?
```

The supersession subsystem therefore protects **canonical continuity**.

A valid supersession relation conceptually has the form:

```text
OLD_ARTIFACT
    │
    │ SUPERSEDED_BY
    ▼
NEW_ARTIFACT
```

but the edge alone is insufficient.

The transition requires contextual state:

```yaml
supersession:
  predecessor_ref: required
  successor_ref: required
  predecessor_version: required
  successor_version: required
  proposal_ref: required_if_governed
  authority_ref: required_if_consequential
  evidence_refs: []
  provenance_refs: []
  dependency_impact: []
  effective_epoch: null
  rollback_ref: null
  validation_receipt: null
  status: PROPOSED | VALIDATED | COMMITTED | REJECTED | REVOKED | UNKNOWN
```

The precise executable schema remains dependent on the sibling normative contract.

---

# 3. Index

Primary sibling artifacts:

- [[SUPERSESSION_CANON_SUPERSESSION_CONTRACT]]
- [[SUPERSESSION_MAP]]

Supporting canonical infrastructure:

- [[LAW_HIERARCHY]]
- [[AMOS_RSCF_NODES]]
- [[00_HOME]]
- [[HML_CANON]]
- [[PERSISTENCE_CANON]]

Operational and governance dependencies:

- [[KERNEL_README]]
- [[CONTROL_PLANE_README]]
- [[OBSERVABILITY_README]]
- [[OPERATIONS_README]]

Validation references:

- [[ROUTING_POLICY_VALIDATION_RECEIPT]]
- [[AUTHZ_ENGINE_VALIDATION_RECEIPT]]

These links provide navigation.

Their presence does not prove that the referenced artifact exists, is current, is validated, or is applicable to a particular operation.

---

# 4. Source / canon references

This artifact is governed conceptually by the AMOS canon hierarchy and inherits the integrity constraints of the wider AMOS architecture.

Load-bearing references include:

```text
AMOS Core Laws
        ↓
Canon plane
        ↓
Supersession subsystem
        ↓
Supersession contract
        ↓
Supersession map
        ↓
Supersession index
```

Primary references:

```text
AMOS Core Laws
LAW_HIERARCHY
SUPERSESSION_CANON_SUPERSESSION_CONTRACT
SUPERSESSION_MAP
AMOS_RSCF_NODES
[[00_HOME]]
```

Where these references disagree, the index must not silently choose a winner.

The conflict must be exposed to the governing canon/supersession mechanism.

---

# 5. Definition

A **supersession** is a governed relation declaring that an identified artifact, version, rule, model, schema, mapping, or canonical state is replaced for a defined scope by another identified artifact or state.

Supersession is not equivalent to deletion.

Formally:

```text
Supersede(A_v1, A_v2, S, E)
```

means:

```text
within scope S
and applicable epoch/regime E,
A_v2 becomes the designated successor to A_v1
subject to applicable authority,
validation,
provenance,
dependency,
and commit requirements.
```

It does not imply:

```text
A_v1 never existed
A_v1 was entirely false
A_v2 is universally valid
A_v2 applies outside S
A_v2 is empirically verified
A_v1 may be destroyed
```

---

# 6. Scope

This index covers canonical resolution of supersession artifacts under:

```text
01_CANON/08_SUPERSESSION/
```

Its scope includes:

- supersession contracts,
- supersession maps,
- predecessor/successor discovery,
- canonical lineage navigation,
- supersession status discovery,
- version transition references,
- provenance references,
- affected dependency discovery,
- historical-state discovery,
- supersession validation references,
- rollback references,
- and cross-plane navigation.

It does not independently govern:

- runtime execution,
- authorization,
- identity issuance,
- evidence creation,
- validation execution,
- storage implementation,
- distributed consensus,
- physical effects,
- or external-world truth.

Those remain responsibilities of their respective planes and contracts.

---

# 7. Indexing rule

Within its own directory, this index resolves artifacts by basename.

```text
local reference
    ↓
basename resolution
    ↓
directory-local candidate set
```

Cross-plane resolution must proceed through canonical navigation structures:

```text
[[00_HOME]]
        +
AMOS_RSCF_NODES
```

A basename match alone must not silently resolve an ambiguous reference.

If:

```text
count(candidate_matches) = 0
```

then:

```text
resolution = UNKNOWN/GAP
```

If:

```text
count(candidate_matches) > 1
```

and identity/version/scope cannot disambiguate, then:

```text
resolution = AMBIGUOUS
authority = NONE
mutation = DENIED
```

Only a uniquely resolved artifact satisfying required identity constraints may proceed.

---

# 8. Identity contract

Supersession must operate on stable identities, not merely human-readable names.

Minimum conceptual identity tuple:

```text
ArtifactIdentity :=
(
  artifact_id,
  canonical_path,
  version,
  content_digest?
)
```

Where required, resolution may additionally bind:

```text
epoch
scope
regime
schema_version
provenance_ref
```

A filename alone is insufficient for consequential supersession.

```text
same basename != same artifact
same title != same version
same path != same content
same content != same authority state
```

---

# 9. Typed inputs

The index may conceptually consume:

```yaml
SupersessionIndexQuery:
  artifact_ref: string
  version_ref: string | null
  scope_ref: string | null
  regime_ref: string | null
  epoch_ref: string | null
  relation_type: string | null
  requester_ref: string | null
```

Possible relation types include:

```text
SUPERSEDES
SUPERSEDED_BY
PREDECESSOR_OF
SUCCESSOR_OF
DERIVED_FROM
REPLACED_WITHIN_SCOPE
REVOKED_BY
RESTORED_FROM
```

These relation labels remain AMOS model semantics unless bound by the normative supersession contract.

---

# 10. Typed outputs

Conceptual output:

```yaml
SupersessionResolution:
  query_ref: string
  resolved_artifact_ref: string | null
  canonical_path: string | null
  current_version: string | null
  predecessor_refs: []
  successor_refs: []
  supersession_status: string
  effective_scope: null
  effective_regime: null
  effective_epoch: null
  authority_ref: null
  validation_refs: []
  provenance_refs: []
  dependency_refs: []
  rollback_ref: null
  uncertainty: {}
  confidence_ceiling: 0.0
  gap_status: []
```

Resolution status may include:

```text
CURRENT
SUPERSEDED
PARTIALLY_SUPERSEDED
PROPOSED
REVOKED
AMBIGUOUS
UNKNOWN/GAP
```

---

# 11. State variables

Conceptual state variables include:

```yaml
index_state:
  artifact_registry: {}
  basename_registry: {}
  version_registry: {}
  supersession_edges: []
  provenance_edges: []
  dependency_edges: []
  authority_bindings: []
  validation_receipts: []
  rollback_refs: []
  active_epoch: null
  unresolved_gaps: []
```

The existence of these conceptual variables does not claim that a specific runtime persistence implementation currently exists.

---

# 12. Supersession state machine

A governed supersession should distinguish at least:

```text
CURRENT
   │
   ▼
PROPOSED_FOR_SUPERSESSION
   │
   ▼
VALIDATION_PENDING
   │
   ├──────────────► REJECTED
   │
   ▼
VALIDATED
   │
   ▼
COMMIT_PENDING
   │
   ▼
SUPERSEDED
```

Possible later paths include:

```text
SUPERSEDED
   │
   ├──► RESTORED
   ├──► SUPERSEDED_AGAIN
   └──► HISTORICAL_ONLY
```

The index must not collapse:

```text
PROPOSED
VALIDATED
COMMITTED
```

into one state.

---

# 13. Operators

Conceptual index operators include:

```text
RESOLVE(ref)
RESOLVE_VERSION(ref, version)
LOOKUP_PREDECESSOR(ref)
LOOKUP_SUCCESSOR(ref)
LOOKUP_LINEAGE(ref)
LOOKUP_SUPERSESSION_STATUS(ref)
CHECK_SCOPE(edge, scope)
CHECK_REGIME(edge, regime)
CHECK_EPOCH(edge, epoch)
CHECK_AUTHORITY(edge)
CHECK_VALIDATION(edge)
CHECK_PROVENANCE(edge)
CHECK_DEPENDENCY_IMPACT(edge)
REGISTER_GAP(gap)
EMIT_RESOLUTION_RECEIPT(result)
```

Mutation operators belong to governed supersession/control-plane paths and are not granted by this README.

---

# 14. Core invariants

### I-SUP-001 — Identity before supersession

No artifact may be superseded unless the predecessor and proposed successor are uniquely identified.

### I-SUP-002 — Proposal is not commit

```text
PROPOSAL != COMMIT
```

A candidate successor remains non-authoritative until required gates complete.

### I-SUP-003 — Historical preservation

Supersession must preserve sufficient predecessor identity and provenance for historical reconstruction.

### I-SUP-004 — No silent deletion

Supersession must not be implemented as provenance-destroying deletion.

### I-SUP-005 — Scoped replacement

A supersession applies only inside its declared applicability envelope.

### I-SUP-006 — Authority required

A supersession edge cannot create its own authority.

```text
SUPERSESSION_CLAIM != SUPERSESSION_AUTHORITY
```

### I-SUP-007 — Dependency visibility

Known load-bearing descendants affected by supersession must remain discoverable.

### I-SUP-008 — Local invalidation

Failure of one premise invalidates dependent conclusions, not unrelated valid state.

### I-SUP-009 — No confidence inheritance inflation

A successor cannot gain confidence merely because it supersedes an older artifact.

### I-SUP-010 — Provenance continuity

The predecessor→successor lineage must remain provenance-recoverable.

### I-SUP-011 — Ambiguity fails closed

Ambiguous identity, version, scope, regime, authority, or epoch prevents consequential commit.

### I-SUP-012 — Unknown is not pass

```text
UNKNOWN/GAP != PASS
```

---

# 15. Persistent provenance

Supersession is a provenance event.

A transition should preserve:

```yaml
provenance:
  predecessor:
    id: null
    version: null
    digest: null

  successor:
    id: null
    version: null
    digest: null

  transition:
    proposal_ref: null
    authority_ref: null
    validation_ref: null
    commit_receipt_ref: null
    effective_epoch: null
    timestamp: null
```

The lineage must remain traversable in both directions where supported:

```text
predecessor → successor
successor → predecessor
```

A one-way pointer that destroys recoverability is insufficient for strong canonical lineage.

---

# 16. Dependency propagation

Supersession may affect downstream conclusions.

If:

```text
A → B → C
```

and `A` is superseded by `A'`, this does not automatically mean:

```text
B invalid
C invalid
```

Instead, dependency sensitivity must be evaluated.

Conceptually:

```text
Affected(A → A') =
{
  descendants whose load-bearing premises
  materially depend on changed semantics
}
```

Only affected descendants require invalidation or revalidation.

This preserves unaffected work and avoids unnecessary global recomputation.

---

# 17. Atomic multi-RSCF implications

A supersession operation may touch multiple RSCF nodes.

For example:

```text
OLD_CANON
NEW_CANON
DEPENDENCY_NODE_A
DEPENDENCY_NODE_B
PROVENANCE_NODE
SUPERSESSION_MAP
```

Where correctness requires these changes to be treated as one logical transition, partial canonical visibility must be prevented.

Conceptually:

```text
all required supersession updates commit
OR
no authoritative supersession state becomes visible
```

This is a model-level integrity requirement.

It does not assert that this README implements distributed atomic transactions.

---

# 18. Epoch semantics

Supersession may be time- or epoch-sensitive.

An artifact may be:

```text
valid before E42
superseded beginning E42
historically addressable after E42
```

Therefore:

```text
current(A, epoch_1)
```

may differ from:

```text
current(A, epoch_2)
```

A supersession query without a required epoch must not fabricate one.

When temporal applicability matters and epoch cannot be resolved:

```text
temporal_status = UNKNOWN/GAP
```

---

# 19. Scope and regime firewall

Supersession must inherit an applicability envelope.

Conceptually:

```yaml
applicability:
  system: null
  domain: null
  environment: null
  scale: null
  time: null
  regime: null
  measurement_method: null
  assumptions: []
```

A successor validated under one regime must not silently supersede a predecessor globally.

Example:

```text
A' supersedes A for regime R1
```

does not establish:

```text
A' supersedes A for R2
```

unless explicitly governed.

---

# 20. H/M/L applicability

The supersession index participates across AMOS fractal resolution levels.

### H — Domain level

Determines:

- which canonical plane owns the artifact,
- whether the supersession crosses domains,
- which high-level authority governs the transition.

### M — Subsystem level

Determines:

- supersession subsystem rules,
- contract dependencies,
- lineage topology,
- validation and control-plane requirements.

### L — Detail level

Determines:

- exact artifact identity,
- version,
- digest,
- edge,
- receipt,
- changed field,
- dependency impact,
- falsifier.

Default traversal:

```text
H
↓
M
↓
L only when decision-changing
↓
raw evidence only when required
```

---

# 21. RSCF semantics

Each consequential supersession conclusion should conceptually carry an RSCF-compatible proof capsule.

Example:

```yaml
claim:
  successor_ref: A_v2
  predecessor_ref: A_v1
  relation: SUPERSEDES

claim_class: AMOS_MODEL

scope:
  domain: null
  regime: null

load_bearing_premises:
  - identity_unique
  - predecessor_exists
  - successor_exists
  - authority_valid
  - validation_sufficient
  - dependency_impact_resolved

evidence: []

provenance: []

dependencies: []

competing: []

falsifiers: []

confidence_ceiling: 0
```

Confidence must not exceed the weakest unresolved load-bearing premise.

---

# 22. Competing successors

AMOS must not force convergence when multiple successor candidates remain genuinely unresolved.

Example:

```text
             ┌── Candidate B
Artifact A ──┤
             └── Candidate C
```

If neither candidate has sufficient discriminating support:

```text
status = COMPETING
```

not:

```text
pick newest
pick most popular
pick most referenced
pick first indexed
```

The preferred next action is the cheapest high-information test capable of discriminating between B and C.

---

# 23. Provenance independence

Multiple supporting references do not necessarily represent independent evidence.

For example:

```text
Source X
 ├── Document B
 ├── Document C
 └── Document D
```

B, C, and D may all descend from the same source.

Therefore:

```text
3 references != 3 independent confirmations
```

Supersession validation should detect correlated ancestry where it materially affects confidence.

---

# 24. Causal boundary

Supersession is primarily a canonical/lineage relation.

It does not itself establish causal truth.

```text
A superseded B
```

does not mean:

```text
B caused A
A empirically disproved B
B caused a system failure
A will cause improved outcomes
```

Such claims require appropriately typed evidence.

---

# 25. Control-plane requirements

Consequential supersession must pass applicable control-plane gates.

Conceptual gates include:

```text
identity gate
version gate
scope gate
regime gate
authority gate
dependency gate
provenance gate
validation gate
conflict gate
rollback gate
commit gate
receipt gate
```

Failure of a required gate results in:

```text
HOLD
DENY
UNKNOWN/GAP
```

according to the governing contract.

No gate may be inferred passed merely because no failure was observed.

---

# 26. Authority model

The index possesses navigation capability only.

```yaml
authority:
  discover: ALLOWED
  resolve: CONDITIONAL
  report: ALLOWED
  propose_supersession: NONE_BY_README
  validate_supersession: NONE_BY_README
  commit_supersession: NONE
  delete_predecessor: NONE
```

Authority must come from the appropriate governed authority reference.

```text
CAPABILITY != AUTHORITY
```

---

# 27. Agents

Conceptual roles interacting with the subsystem may include:

### Index Resolver

Finds candidate artifacts and versions.

### Lineage Resolver

Traverses predecessor/successor relations.

### Provenance Auditor

Checks source ancestry and provenance continuity.

### Dependency Auditor

Determines potentially affected descendants.

### Validation Agent

Evaluates required validation evidence.

### Authority Gate

Checks whether the proposed transition is authorized.

### Conflict Detector

Detects competing successors, contradictory edges, and ambiguous state.

### Receipt Writer

Records the outcome of consequential governed transitions.

### Recovery Agent

Restores or reconstructs a prior valid state when governed rollback is required.

These are architectural roles.

Their description here does not prove executable implementations exist.

---

# 28. Required skills

Relevant capabilities include:

```text
artifact resolution
canonical path resolution
version comparison
schema validation
dependency traversal
provenance tracing
scope checking
regime checking
authority verification
conflict detection
supersession impact analysis
rollback planning
receipt verification
gap classification
```

Skill availability does not imply authority to act.

---

# 29. Canonical workflow

```text
REQUEST
  ↓
RESOLVE PREDECESSOR
  ↓
RESOLVE PROPOSED SUCCESSOR
  ↓
VERIFY IDENTITY + VERSION
  ↓
BIND SCOPE / REGIME / EPOCH
  ↓
TRACE PROVENANCE
  ↓
CHECK AUTHORITY
  ↓
CHECK DEPENDENCY CLOSURE
  ↓
CHECK COMPETING SUCCESSORS
  ↓
VALIDATE REQUIRED EVIDENCE
  ↓
VERIFY ROLLBACK BASIN
  ↓
PROPOSE
  ↓
COMMIT GATE
  ├── fail → HOLD / DENY / GAP
  └── pass
        ↓
      COMMIT
        ↓
      PERSIST LINEAGE
        ↓
      EMIT RECEIPT
        ↓
      REVALIDATE AFFECTED DESCENDANTS
```

---

# 30. Worked semantics

Given an operation touching `SUPERSESSION · CANON README` within the Canon plane:

### 30.1 Admit

Resolve the artifact by canonical identity plus applicable version.

Unresolved identity:

```text
UNKNOWN/GAP
```

The operation fails closed for consequential mutation.

### 30.2 Bind scope

Declare applicable:

```text
domain
environment
regime
H/M/L level
epoch
```

where material.

### 30.3 Check authority

Resolve `authority_ref`.

The authority must be valid for:

```text
principal
operation
artifact
scope
epoch
```

Capability alone never authorizes.

### 30.4 Validate preconditions

Traverse dependency closure only to the smallest set capable of changing the result.

Do not load unrelated evidence.

### 30.5 Challenge

Check for:

- contradictory successor claims,
- correlated provenance,
- stale evidence,
- scope leakage,
- hidden dependencies,
- invalid authority,
- stronger competing candidates.

### 30.6 Propose

Create a candidate supersession state.

```text
PROPOSAL != COMMIT
```

### 30.7 Commit or hold

If all mandatory gates pass, the governing system may commit.

If any load-bearing premise fails:

```text
preserve unaffected state
invalidate dependent conclusions only
record failure/gap
retain predecessor recoverability
emit appropriate receipt where governed
```

---

# 31. MVCC / CAS conceptual requirements

Where concurrent mutation exists, supersession should avoid silently overwriting a state that changed after validation.

Conceptually:

```text
read predecessor at version V
validate against V
attempt commit only if current version == V
```

Equivalent conceptual CAS rule:

```text
CAS(expected_version, proposed_successor)
```

If the expected version no longer matches:

```text
commit = REJECTED
reason = STALE_BASE
```

The operation must re-resolve dependencies rather than assume the previous validation remains valid.

This is an architectural reasoning requirement, not a claim that this Markdown artifact implements MVCC or CAS.

---

# 32. Persistence requirements

A committed supersession should preserve enough persistent state to reconstruct:

```text
predecessor
successor
transition
authority
evidence
provenance
epoch
scope
validation
receipt
rollback path
```

Persistence should survive ordinary navigation/index regeneration.

If the index can be rebuilt but the provenance cannot, canonical lineage integrity is incomplete.

---

# 33. Observability boundary

Observability may report:

```text
supersession proposed
validation failed
commit succeeded
rollback occurred
dependency revalidation pending
```

but telemetry is not authority.

```text
OBSERVED != AUTHORIZED
LOGGED != VALIDATED
METRIC != CANON
```

The observability plane may provide evidence but cannot independently declare canonical supersession.

---

# 34. Failure modes

### F-SUP-001 — Missing predecessor

Referenced predecessor cannot be resolved.

**Result:** `UNKNOWN/GAP`.

### F-SUP-002 — Missing successor

Proposed successor cannot be resolved.

**Result:** hold supersession.

### F-SUP-003 — Ambiguous basename

Multiple artifacts match.

**Result:** require stronger identity.

### F-SUP-004 — Stale version

Validation occurred against an obsolete predecessor version.

**Result:** invalidate affected validation and rerun from changed dependency.

### F-SUP-005 — Unauthorized supersession

No valid authority exists.

**Result:** deny commit.

### F-SUP-006 — Broken provenance

Transition ancestry cannot be reconstructed.

**Result:** downgrade trust / hold promotion.

### F-SUP-007 — Scope leakage

A scoped successor is treated as globally superseding the predecessor.

**Result:** reject generalized conclusion.

### F-SUP-008 — Competing successors

Multiple incompatible candidates remain supported.

**Result:** `COMPETING`.

### F-SUP-009 — Dependency orphaning

Descendants reference a predecessor whose transition was not propagated or represented.

**Result:** dependency repair required.

### F-SUP-010 — Premature deletion

Predecessor removed before lineage/rollback requirements are satisfied.

**Result:** integrity failure.

### F-SUP-011 — Receipt missing

Consequential commit claims success without required receipt.

**Result:** commit status cannot be treated as verified.

### F-SUP-012 — Validation conflation

Presence of a validation reference is treated as successful execution.

**Result:** reject inference.

---

# 35. Repair and recovery

AMOS recovery should invalidate the smallest affected region.

General repair pattern:

```text
detect failed edge/premise
        ↓
freeze consequential mutation
        ↓
identify dependent descendants
        ↓
preserve unaffected nodes
        ↓
restore nearest valid predecessor state if required
        ↓
repair failed relation
        ↓
revalidate affected closure
        ↓
emit recovery receipt
```

Global recomputation is a last resort.

A failed supersession path should not simply be retried without changed evidence or corrected state.

---

# 36. Rollback basin

Before consequential supersession, the system should establish whether a safe rollback basin exists.

A rollback basin includes sufficient information to recover:

```text
previous canonical identity
previous version
previous dependency state
previous provenance edges
previous authority context where required
transition receipt
```

If rollback is required by governance but cannot be demonstrated:

```text
promotion = HOLD
```

---

# 37. Validation requirements

A supersession transition should be tested across at least:

```text
identity
schema
version
lineage
scope
regime
authority
dependency
provenance
conflict
rollback
receipt
```

Validation must distinguish:

```text
schema-valid
semantically-valid
authority-valid
dependency-valid
provenance-valid
operationally-executed
```

Passing one does not imply passing the others.

---

# 38. Validators

Conceptual validators:

```text
V-SUP-001 IdentityUniquenessValidator
V-SUP-002 VersionContinuityValidator
V-SUP-003 LineageAcyclicityValidator
V-SUP-004 AuthorityValidator
V-SUP-005 ScopeCompatibilityValidator
V-SUP-006 RegimeCompatibilityValidator
V-SUP-007 ProvenanceContinuityValidator
V-SUP-008 DependencyImpactValidator
V-SUP-009 CompetingSuccessorValidator
V-SUP-010 RollbackValidator
V-SUP-011 ReceiptValidator
V-SUP-012 LinkIntegrityValidator
```

These names define architectural validator roles; they do not establish executable implementations.

---

# 39. Negative tests

Required negative cases include:

```text
missing predecessor
missing successor
malformed identity
duplicate basename
unknown version
stale version
missing authority
expired authority
wrong-scope authority
cross-regime supersession
missing provenance
cyclic lineage
multiple active successors
missing rollback state
missing validation receipt
failed validation receipt
tampered digest
unresolved dependency
broken cross-plane reference
```

Each negative case must fail visibly rather than silently defaulting to success.

---

# 40. Lineage-cycle test

Supersession lineage should normally reject cycles such as:

```text
A superseded_by B
B superseded_by C
C superseded_by A
```

unless an explicit higher-level model defines a different legal semantic.

Default result:

```text
INVALID_LINEAGE
```

because ordinary supersession represents directional canonical history.

---

# 41. Sensitivity test

Before a consequential supersession conclusion, identify the smallest premise capable of changing the decision.

Typical flip premises include:

```text
authority validity
artifact identity
version freshness
scope compatibility
regime compatibility
validation result
provenance independence
existence of competing successor
```

Test these before low-value background evidence.

If one unresolved premise can flip the decision:

```text
claim_class = CONDITIONAL
```

or:

```text
UNKNOWN/GAP
```

depending on severity.

---

# 42. Falsifiers

A claim that a supersession is valid is falsified or invalidated by evidence such as:

- predecessor identity mismatch,
- successor identity mismatch,
- invalid or revoked authority,
- failed required validation,
- stale validation base,
- scope incompatibility,
- regime incompatibility,
- provenance corruption,
- unresolved competing successor,
- broken required dependency,
- invalid transition epoch,
- failed atomicity requirement,
- missing mandatory receipt,
- or evidence that the purported commit never occurred.

Falsification should invalidate the dependent supersession conclusion, not unrelated canonical state.

---

# 43. Confidence ceiling

Confidence is bounded by the weakest load-bearing premise.

Conceptually:

```text
C_supersession ≤ min(
    C_identity,
    C_version,
    C_authority,
    C_scope,
    C_regime,
    C_provenance,
    C_dependency,
    C_validation,
    C_commit
)
```

Repeated references descending from one provenance source do not independently raise this ceiling.

A missing critical premise may force:

```text
confidence_ceiling = 0
```

for a claim of committed supersession.

---

# 44. Evidence classes

Supersession evidence must retain type.

Relevant classes include:

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL
DECISION
UNKNOWN
```

Examples:

```text
"README says A supersedes B"
    = SOURCE_CLAIM

"validated map contains edge A→B"
    = OBSERVATION, if actually inspected

"therefore B is globally invalid"
    = unsupported unless scope/dependencies establish it

"authorized governance committed A→B"
    = DECISION, if supported by valid authority + receipt
```

Evidence types must not be silently upgraded.

---

# 45. Gap taxonomy

Unresolved gaps should be classified:

### CRITICAL

Blocks safe canonical supersession.

Examples:

```text
unknown identity
unknown authority
unknown predecessor
unknown successor
```

### DECISION-RELEVANT

May change whether supersession should occur.

Examples:

```text
competing successor
uncertain dependency impact
stale validation
```

### EXPLANATORY

Does not currently change the decision but limits understanding.

### COSMETIC

Formatting or naming issues without semantic consequence.

Resolution priority:

```text
CRITICAL
    ↓
DECISION-RELEVANT
    ↓
EXPLANATORY
    ↓
COSMETIC
```

---

# 46. Current gaps

Automated link-integrity execution for this index remains:

```text
PARTIAL
```

Referenced validation artifacts:

```text
ROUTING_POLICY_VALIDATION_RECEIPT
AUTHZ_ENGINE_VALIDATION_RECEIPT
```

must not be interpreted merely from their names as proof that:

- they exist,
- they executed,
- they passed,
- they cover this exact artifact,
- they remain fresh,
- or they remain valid in the current regime.

Until an applicable executed receipt is inspected and validated, executable binding remains conditional.

---

# 47. Promotion-gate checklist

Before this artifact or its executable bindings are promoted beyond conditional model status:

- [ ] typed schema bound to this artifact
- [ ] stable artifact identity implemented
- [ ] explicit versioning implemented
- [ ] basename ambiguity detection implemented
- [ ] predecessor/successor resolution implemented
- [ ] supersession state machine validated
- [ ] scope applicability validated
- [ ] regime applicability validated
- [ ] epoch semantics validated
- [ ] authority checks validated
- [ ] provenance edges persisted
- [ ] dependency impact traversal validated
- [ ] competing-successor handling validated
- [ ] stale-base rejection demonstrated
- [ ] rollback basin demonstrated
- [ ] lineage-cycle rejection demonstrated
- [ ] negative cases executed
- [ ] cross-plane link integrity executed
- [ ] required receipts persisted
- [ ] executed validation receipt specific to this artifact exists
- [ ] critical gaps explicitly registered
- [ ] `UNKNOWN/GAP` fails closed
- [ ] predecessor remains historically recoverable

---

# 48. Cross-plane bindings

### Canon

Governed by:

LAW_HIERARCHY|AMOS Core Laws · [[LAW_HIERARCHY]]

The supersession index cannot supersede higher-order law merely by recording an edge.

### Kernel

Interaction:

[[KERNEL_README]]

Kernel behavior may consume resolved canonical state but must not infer authority from index presence alone.

### Control plane

Governed transition gates:

[[CONTROL_PLANE_README]]

Authorization and consequential mutation remain control-plane concerns.

### Observability

Observed by:

[[OBSERVABILITY_README]]

Observability provides evidence and receipts but never becomes canonical authority merely through observation.

### Operations

Recovery:

[[OPERATIONS_README]]

Operational procedures provide rollback, restoration, incident response, and lineage repair where governed.

---

# 49. Anti-regression rule

A proposed successor must not be accepted merely because it is newer.

For integrity-sensitive canon, promotion must preserve or improve required properties such as:

```text
factual support
scope correctness
contradiction visibility
provenance recoverability
causal discipline
dependency integrity
rollback capability
safety
governance compatibility
user fit
```

If an optimization weakens a required integrity property without authorized justification:

```text
promotion = REJECT
```

or:

```text
promotion = HOLD
```

until repaired.

---

# 50. Supersession map semantics

`[[SUPERSESSION_MAP]]` should represent lineage relationships without becoming the sole proof of those relationships.

Conceptually:

```text
SUPERSESSION_MAP
     │
     ├── indexes predecessor
     ├── indexes successor
     ├── indexes relation
     ├── indexes effective scope
     ├── indexes effective epoch
     └── references supporting provenance
```

The map is evidence about canonical topology.

It does not independently create authority.

---

# 51. Index reconstruction rule

The index should be reconstructable from canonical artifacts and persistent provenance where the architecture supports such reconstruction.

Conceptually:

```text
canonical artifacts
      +
persistent identities
      +
supersession edges
      +
provenance
      ↓
reconstructed index
```

Therefore the index should not be the only surviving location of critical supersession truth.

If destroying the index destroys the lineage, the architecture has conflated navigation with canonical persistence.

---

# 52. Proof-capsule requirement

For an important claim:

```text
"A_v2 is the current canonical successor of A_v1"
```

the smallest sufficient proof capsule should conceptually establish:

```yaml
claim: A_v2 supersedes A_v1
class: DECISION | DERIVED | AMOS_MODEL

premises:
  - A_v1 uniquely identified
  - A_v2 uniquely identified
  - supersession relation valid
  - scope applicable
  - regime applicable
  - authority valid
  - required validation passed
  - commit occurred

provenance:
  - predecessor_ref
  - successor_ref
  - transition_ref
  - authority_ref
  - receipt_ref

dependencies: []

competing: []

falsifiers:
  - authority_revoked
  - receipt_invalid
  - successor_identity_mismatch
  - applicable_newer_supersession

confidence_ceiling: bounded
```

Only the smallest result-changing dependency closure should be loaded.

---

# 53. Stop conditions

A supersession resolution is sufficient when three conditions are satisfied:

### Claim sufficiency

The requested lineage claim is adequately supported for its declared class.

### Decision sufficiency

Remaining uncertainty cannot materially change the current governance decision.

### Action sufficiency

The next safe action is known.

If these conditions are satisfied, further traversal should stop rather than accumulating redundant evidence.

---

# 54. Hard boundaries

```text
PLACEHOLDER != IMPLEMENTED
ADDRESSABLE != VALIDATED
INDEXED != VERIFIED
REFERENCE != PROOF
DISCOVERY != AUTHORITY
CAPABILITY != AUTHORITY
PROPOSAL != COMMIT
VALIDATED != COMMITTED
SUPERSEDED != DELETED
NEWER != BETTER
SIMILAR != EQUIVALENT
OBSERVED != AUTHORIZED
UNKNOWN/GAP != PASS
MULTIPLE REFERENCES != INDEPENDENT CONFIRMATION
```

These boundaries are load-bearing.

---

# 55. Canonical index contract

The operational meaning of this README can be compressed to:

```text
RESOLVE EXACTLY
        ↓
PRESERVE VERSION
        ↓
BIND SCOPE + REGIME + EPOCH
        ↓
TRACE LINEAGE
        ↓
VERIFY PROVENANCE
        ↓
CHECK AUTHORITY
        ↓
CHECK DEPENDENCIES
        ↓
PRESERVE COMPETING STATES
        ↓
VALIDATE
        ↓
PROPOSE
        ↓
COMMIT ONLY THROUGH GOVERNED PATH
        ↓
PERSIST PREDECESSOR + SUCCESSOR + RECEIPT
        ↓
REVALIDATE ONLY AFFECTED DESCENDANTS
```

---

# 56. RSCF completion state

```yaml
claim_class: AMOS_MODEL

artifact:
  id: amos_01_canon_08_supersession_00_index_index_supersession_canon_readme_md
  type: note
  role: CANON_INDEX
  authority: INDEX_ONLY

evidence:
  - supplied_AMOS_canon_structure
  - supplied_supersession_index_contract

provenance:
  origin_architect: Trang Phan
  corpus: AMOS_OS

scope:
  plane: 01_CANON
  subsystem: 08_SUPERSESSION
  package: 00_INDEX

regime:
  canonical_status: CONDITIONAL

freshness:
  updated: 2026-08-26

dependencies:
  - SUPERSESSION_CANON_SUPERSESSION_CONTRACT
  - SUPERSESSION_MAP
  - LAW_HIERARCHY
  - AMOS_RSCF_NODES
  - CONTROL_PLANE_README
  - PERSISTENCE_CANON

competing: []

falsifiers:
  - canonical supersession contract defines incompatible semantics
  - higher-order canon supersedes this contract
  - artifact identity or path is changed through governed supersession
  - executed validation demonstrates required assumptions are false

uncertainty:
  executable_binding: PARTIAL
  link_integrity_execution: PARTIAL
  validation_receipt_status: UNKNOWN_UNTIL_INSPECTED
  runtime_implementation: NOT_ESTABLISHED_BY_THIS_ARTIFACT

confidence_ceiling:
  canonical_model_semantics: CONDITIONAL
  runtime_implementation: UNKNOWN

gap_status:
  - DECISION_RELEVANT: executable link-integrity validation incomplete
  - DECISION_RELEVANT: artifact-specific executed validation receipt not established here
```

---

# 57. RSCF relations

```text
RSCF-NODE

node_id: amos_01_canon_08_supersession_00_index_index_supersession_canon_readme_md

node_type: note

path: 01_CANON/08_SUPERSESSION/00_INDEX/INDEX_SUPERSESSION_CANON_README.md

RSCF-RELATIONS:

  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: AMOS_RSCF_NODES

  - GOVERNED_BY: LAW_HIERARCHY

  - SIBLING_OF: SUPERSESSION_CANON_SUPERSESSION_CONTRACT
  - SIBLING_OF: SUPERSESSION_MAP

  - DEPENDS_ON: SUPERSESSION_CANON_SUPERSESSION_CONTRACT
  - DEPENDS_ON: SUPERSESSION_MAP

  - INTERACTS_WITH: KERNEL_README
  - GATED_BY: CONTROL_PLANE_README
  - OBSERVED_BY: OBSERVABILITY_README
  - RECOVERED_BY: OPERATIONS_README

claim_class: AMOS_MODEL
```

---

# 58. Canon status

```yaml
status:
  artifact_addressable: true
  navigation_contract_defined: true
  supersession_semantics_defined: true
  authority_granted: false
  runtime_implementation_proven: false
  artifact_specific_validation_proven: false
  link_integrity_execution: PARTIAL
  canonical_class: AMOS_MODEL
  promotion_state: CONDITIONAL
```

The artifact is therefore suitable as a **full AMOS supersession index specification**, while executable implementation and artifact-specific validation remain explicitly separate claims.

---

00_ROOT_MOC|AMOS MOC

---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[SUPERSESSION_CANON_SUPERSESSION_CONTRACT]] · [[SUPERSESSION_MAP]]

---

**Origin architect / steward:** Trang Phan
**Claim class:** `AMOS_MODEL`
**Canonical status:** `CONDITIONAL`

---
**MOC:** [[00_INDEX_MOC]]
