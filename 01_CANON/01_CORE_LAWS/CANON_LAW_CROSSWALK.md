---
title: Canon Law Crosswalk
type: canon
source: 01_CANON/01_CORE_LAWS
artifact: CANON_LAW_CROSSWALK.md
artifact_id: amos_01_canon_01_core_laws_canon_law_crosswalk
origin_architect: Trang Phan
steward: Trang Phan
system: AMOS OS
plane: 01_CANON
segment: 01_CANON/01_CORE_LAWS
artifact_kind: CROSSWALK
path: 01_CANON/01_CORE_LAWS/CANON_LAW_CROSSWALK.md
canon_group: amos_core
schema_family: RSCF
schema_role: CANON_CROSSWALK_RSCF
schema_version: AMOS_CORE_v4.4-compatible-conceptual
tags:
- amos-os
- canon
- universe
- crosswalk
- core_laws
- law_hierarchy
- provenance
- lineage
- supersession
- dependency_graph
- scope
- regime
- causal_firewall
- competing_hypotheses
- validation
- rscf
- canon/universe
- placeholder_expanded
- law-hierarchy
- references
- law/L19-proof-capsule
- routing-policy-validation-receipt
- authz-engine-validation-receipt
version: 0.2.0
updated: '2026-08-27'
status: PLACEHOLDER_EXPANDED
epistemic_class: AMOS_MODEL
canonical_status: UNKNOWN/GAP
implementation_status: NOT_ESTABLISHED
validation_status: NOT_ESTABLISHED
executable_binding: NOT_ESTABLISHED
ingestion_action: ADD_ONLY
crosswalk_population_status: PARTIAL_TARGET_MODEL
native_law_inventory_status: NOT_ESTABLISHED
native_mapping_status: NOT_ESTABLISHED
conflict_resolution_status: NOT_ESTABLISHED
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: core_laws
  regime: canon_placeholder
  confidence_ceiling: source_supported
  provenance_independence: NOT_ESTABLISHED
---

# Canon Law Crosswalk

## 0. Status

`CANON_LAW_CROSSWALK.md` is an **ADD-ONLY placeholder-expanded artifact** for:

```text
01_CANON/01_CORE_LAWS

Its function is to reserve and define the target contract for a governed crosswalk among AMOS canonical law artifacts.

It does **not** presently establish that all AMOS law families have been discovered, normalized, reconciled, validated, or promoted.

Current state:

```yaml
status: PLACEHOLDER_EXPANDED
epistemic_class: AMOS_MODEL
canonical_status: UNKNOWN/GAP
implementation_status: NOT_ESTABLISHED
validation_status: NOT_ESTABLISHED
executable_binding: NOT_ESTABLISHED

native_law_inventory_status: NOT_ESTABLISHED
native_mapping_status: NOT_ESTABLISHED
crosswalk_population_status: PARTIAL_TARGET_MODEL
```

Origin architect / steward:

**Trang Phan**

System:

**AMOS OS**

---

# 1. Governing Integrity Boundary

The crosswalk MUST preserve:

```text
PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

DOCUMENTED != ENFORCED

MODEL != OBSERVATION

SOURCE_CLAIM != VERIFIED

CANON_CANDIDATE != CANONICAL

CANONICAL != EMPIRICAL_TRUTH

CROSSWALK_ENTRY != LAW

MAPPING != EQUIVALENCE

SIMILARITY != IDENTITY

OVERLAP != DUPLICATION

DEPENDENCY != DERIVATION

DERIVATION != CAUSATION

PRECEDENCE != EMPIRICAL_SUPERIORITY

SUPERSESSION != DELETION

REFERENCE != AUTHORITY

CAPABILITY != AUTHORITY

AUTHORIZATION != COMMIT

PROPOSAL != COMMIT

IMPLEMENTED != VALIDATED

LOGGED != APPROVED

UNKNOWN/GAP != PASS
```

These distinctions are mandatory.

---

# 2. Purpose

The **Canon Law Crosswalk** is intended to become the canonical relational index for AMOS core-law families.

Its target responsibilities are:

```text
DISCOVER
+
IDENTIFY
+
NORMALIZE
+
LINK
+
COMPARE
+
TYPE RELATIONSHIPS
+
PRESERVE PROVENANCE
+
PRESERVE CONFLICT
+
PRESERVE LINEAGE
+
TRACK SUPERSESSION
+
EXPOSE GAPS
```

It SHOULD eventually answer questions such as:

```text
Which canonical laws exist?

Which artifacts express the same framework?

Which laws overlap?

Which laws depend on other laws?

Which laws constrain other laws?

Which laws conflict?

Which laws supersede historical formulations?

Which mappings are merely analogical?

Which claims have empirical support?

Which claims remain AMOS models?

Which dependencies are load-bearing?

Which law governs when multiple rules apply?
```

The current placeholder cannot yet answer all of these questions authoritatively.

---

# 3. Non-Purpose

The crosswalk MUST NOT itself be used to claim:

* universal laws of reality;
* scientific proof;
* biological truth;
* mathematical theoremhood;
* philosophical certainty;
* equivalence between differently named laws;
* causal relations merely from structural mappings;
* final canonical status for mapped artifacts;
* empirical validity merely because a law appears in the crosswalk;
* runtime enforcement not established by executable bindings;
* authority from centrality in the graph;
* independent evidence merely because several artifacts repeat one source;
* resolution of contradictions that remain unresolved.

---

# 4. Crosswalk Is Metadata, Not Truth

Canonical rule:

```text
LAW
!=
CROSSWALK ENTRY
```

A crosswalk entry describes relationships concerning a law.

It does not create the law.

Likewise:

```text
LAW_A MAPS_TO LAW_B
```

does not establish:

```text
LAW_A = LAW_B
```

unless identity is independently demonstrated.

---

# 5. Ingestion Rule

```yaml
AMOS_CANON_INGESTION_RULE:

  existing_folder:
    preserve: true

  existing_file:
    preserve: true
    overwrite: false

  new_framework:
    action: ADD_FILE_TO_EXISTING_FOLDER

  master_source:
    action: NORMALIZE_TO_RSCF_FILE

  framework_existing_in_multiple_sources:
    action:
      - CREATE_ONE_CANONICAL_NODE
      - LINK_ALL_SOURCE_PROVENANCE
      - DO_NOT_CREATE_DUPLICATE_CANON

  historical_source:
    action:
      - LINK_TO_CANON
      - RECORD_LINEAGE
      - PRESERVE_HERITAGE

  external_research:
    action:
      - KEEP_OUT_OF_NATIVE_CANON
      - LINK_AS_EVIDENCE

  duplicate_filename:
    action:
      - COMPARE_CONTENT_AND_LINEAGE
      - DO_NOT_OVERWRITE

  uncertainty:
    action:
      - MARK_GAP_OR_COMPETING
      - NEVER_INVENT_CANON
```

---

# 6. Crosswalk Admission Rule

No substantive mapping SHOULD enter the canonical crosswalk solely because two artifacts have similar titles, equations, terminology, structures, or purposes.

A candidate relation must be represented first as:

```text
PROPOSED RELATION
```

and then tested against:

```text
IDENTITY
PROVENANCE
CONTENT
SCOPE
REGIME
VERSION
LINEAGE
DEPENDENCIES
CONFLICTS
```

before stronger relation types are assigned.

---

# 7. Relation Strength Discipline

Crosswalk relations have materially different meanings.

A target relation vocabulary includes:

```text
IDENTICAL_TO

ALIAS_OF

RENAMED_FROM

SUPERSEDES

SUPERSEDED_BY

DERIVED_FROM

DEPENDS_ON

REQUIRES

CONSTRAINS

GOVERNS

SPECIALIZES

GENERALIZES

OVERLAPS_WITH

COMPATIBLE_WITH

CONFLICTS_WITH

COMPETES_WITH

ANALOGOUS_TO

EVIDENCED_BY

FALSIFIED_BY

VALIDATED_BY

IMPLEMENTED_BY

INDEXED_BY
```

These MUST NOT be silently substituted for one another.

---

# 8. Identity Relation

`IDENTICAL_TO` is a strong relation.

It SHOULD require evidence that two references resolve to the same canonical conceptual entity.

```text
SAME NAME
!=
IDENTICAL_TO
```

and:

```text
SAME EQUATION
!=
IDENTICAL_TO
```

without provenance and semantic identity.

---

# 9. Alias Relation

`ALIAS_OF` indicates distinct names for one canonical identity.

Target contract:

```yaml
relation:
  type: ALIAS_OF
  source: artifact_or_law_A
  target: artifact_or_law_B
  canonical_identity: stable_id
  provenance:
    - source_ref
```

Alias status MUST NOT be inferred from similarity alone.

---

# 10. Rename Relation

A rename preserves identity across naming change.

```text
OLD_NAME
↓ RENAMED_TO
NEW_NAME
```

It is different from supersession.

```text
RENAMED_FROM
!=
SUPERSEDED_BY
```

---

# 11. Supersession Relation

Supersession indicates that a newer canonical formulation replaces an older formulation for a declared purpose or scope.

Conceptually:

```text
LAW_v1
↓ SUPERSEDED_BY
LAW_v2
```

Historical content remains preserved.

```text
SUPERSEDED
!=
DELETED
```

---

# 12. Derivation Relation

`DERIVED_FROM` means a claim depends logically, mathematically, procedurally, or model-wise on another source.

It MUST declare the derivation type where material.

```yaml
derivation:
  source: LAW_A
  target: LAW_B
  type:
    - logical
    - mathematical
    - procedural
    - model
    - unknown
```

Derivation does not automatically establish empirical causation.

---

# 13. Dependency Relation

`DEPENDS_ON` represents a load-bearing or material prerequisite.

```text
A DEPENDS_ON B
```

means failure of `B` may invalidate `A`.

It does not necessarily mean:

```text
B CAUSES A
```

---

# 14. Requires Relation

`REQUIRES` SHOULD represent an explicit prerequisite contract.

Example target semantics:

```text
LAW_A
REQUIRES
VARIABLE_REGISTRY_X
```

or:

```text
POLICY_A
REQUIRES
AUTHORITY_REF
```

The exact prerequisite must be declared.

---

# 15. Constraint Relation

`CONSTRAINS` means one artifact restricts the allowed interpretation or operation of another.

```text
LAW_A
CONSTRAINS
LAW_B
```

does not necessarily imply hierarchical superiority.

The constraint's scope MUST be declared.

---

# 16. Governance Relation

`GOVERNS` is an authority-sensitive relation.

It MUST NOT be inferred merely because one artifact is architecturally central.

```text
CENTRALITY
!=
AUTHORITY
```

Governance requires an explicit canonical or authorized basis.

---

# 17. Specialization Relation

```text
GENERAL LAW
↓ SPECIALIZES
NARROWER LAW
```

A specialization SHOULD declare what dimensions narrow:

```text
DOMAIN
SCOPE
REGIME
POPULATION
SCALE
TIME
ASSUMPTIONS
```

---

# 18. Generalization Relation

A generalization expands applicability.

This is epistemically dangerous because:

```text
VALID IN NARROW DOMAIN
!=
VALID GENERALLY
```

Therefore `GENERALIZES` requires explicit support.

---

# 19. Overlap Relation

`OVERLAPS_WITH` means two artifacts share some conceptual or operational region.

It does not establish duplication.

```text
OVERLAP
!=
IDENTITY
```

The overlapping region SHOULD be declared.

---

# 20. Compatibility Relation

`COMPATIBLE_WITH` means no identified contradiction exists within a declared shared scope.

But:

```text
NO OBSERVED CONTRADICTION
!=
PROOF OF COMPATIBILITY
```

Compatibility should therefore remain bounded by tested scope.

---

# 21. Conflict Relation

`CONFLICTS_WITH` represents incompatible claims under an overlapping applicability envelope.

A valid conflict record SHOULD identify:

```text
CLAIM A
CLAIM B
SHARED SCOPE
SHARED REGIME
CONFLICTING PREDICTION / REQUIREMENT
```

Claims applying to different regimes are not necessarily contradictory.

---

# 22. Competing Relation

`COMPETES_WITH` SHOULD be used where alternative models or explanations remain viable.

```text
H1
vs
H2
```

If current evidence does not discriminate:

```text
STATE = COMPETING
```

The crosswalk MUST preserve both.

---

# 23. Analogy Relation

`ANALOGOUS_TO` is explicitly weaker than equivalence.

```text
ANALOGOUS_TO
!=
IDENTICAL_TO
```

and:

```text
STRUCTURAL SIMILARITY
!=
CAUSATION
```

Cross-domain mappings SHOULD default to `ANALOGOUS_TO` or `MODEL` until stronger support exists.

---

# 24. Evidence Relation

`EVIDENCED_BY` links a claim to evidence.

Evidence type SHOULD remain explicit:

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL
DECISION
UNKNOWN
```

A source repeating a claim is not automatically an independent observation.

---

# 25. Validation Relation

`VALIDATED_BY` requires an actual validation artifact or receipt appropriate to the claim.

```text
DOCUMENTED_BY
!=
VALIDATED_BY
```

and:

```text
TESTED_ONCE
!=
UNIVERSALLY VALIDATED
```

---

# 26. Implementation Relation

`IMPLEMENTED_BY` links a canonical model or rule to an executable implementation.

It does not establish validation:

```text
IMPLEMENTED_BY
!=
VALIDATED_BY
```

---

# 27. Crosswalk Entry Target Schema

A substantive entry SHOULD normalize conceptually to:

```yaml
crosswalk_entry:

  entry_id: stable_identifier

  source:
    artifact_id: required
    law_id: optional
    version: required

  relation:
    type: required

  target:
    artifact_id: required
    law_id: optional
    version: required

  claim_class:
    value: required

  provenance:
    native_sources:
      - source_ref
    ancestry_status: established | partial | unknown

  scope:
    domain: required
    scale: optional
    environment: optional
    temporal_window: optional

  regime:
    value: required

  relation_basis:
    - evidence_or_source_ref

  assumptions:
    - assumption

  dependencies:
    - dependency_ref

  competing_relations:
    - relation_ref

  falsifiers:
    - invalidation_condition

  validation:
    status: required
    receipt: optional

  confidence_ceiling:
    value: required
```

This is a target schema, not evidence that populated entries currently exist.

---

# 28. Law Identity Target Schema

```yaml
canonical_law_identity:

  law_id: stable_identifier

  canonical_title: required

  artifact_id: required

  version: required

  status:
    canonical: required
    implementation: required
    validation: required

  epistemic_class: required

  provenance:
    root_sources:
      - ref

  lineage:
    predecessors:
      - ref
    successors:
      - ref

  aliases:
    - ref

  scope:
    - envelope

  dependencies:
    - ref

  relations:
    - crosswalk_entry_ref
```

---

# 29. Crosswalk Matrix — Target

The mature artifact MAY expose a matrix conceptually like:

| Source Law | Relation         | Target Law | Scope    | Provenance | Status    |
| ---------- | ---------------- | ---------- | -------- | ---------- | --------- |
| LAW_A      | `DEPENDS_ON`     | LAW_B      | declared | linked     | candidate |
| LAW_A      | `CONFLICTS_WITH` | LAW_C      | declared | linked     | competing |
| LAW_D      | `SUPERSEDES`     | LAW_E      | declared | linked     | candidate |
| LAW_F      | `ANALOGOUS_TO`   | LAW_G      | declared | linked     | model     |

The rows above are schema examples only.

They are not assertions that `LAW_A` through `LAW_G` exist.

---

# 30. Current Named Core-Law Artifact Surface

From the presently supplied Canon-plane artifact context, the crosswalk can safely recognize the existence of reserved artifact identities including:

```text
[[ABSOLUTE_LOGIC_CANON]]
[[ABSOLUTE_STRUCTURAL_INTEGRITY_CANON]]
[[BIO_LOGICAL_LAWS_CANON]]
CANON_LAW_CROSSWALK
[[LAW_HIERARCHY]]
```

For the first three named canon artifacts, the supplied state indicates placeholder status rather than populated substantive canon.

Therefore:

```text
ARTIFACT IDENTITY RECOGNIZED
!=
SUBSTANTIVE LAW CONTENT RECOVERED
```

---

# 31. Current Minimal Crosswalk

The strongest presently supportable artifact-level crosswalk is:

| Artifact                                 | Artifact Kind | Current Role          | Canonical Status |
| ---------------------------------------- | ------------- | --------------------- | ---------------- |
| `ABSOLUTE_LOGIC_CANON.md`                | `LOG`         | reserved canon slot   | `UNKNOWN/GAP`    |
| `ABSOLUTE_STRUCTURAL_INTEGRITY_CANON.md` | `CANON`       | reserved canon slot   | `UNKNOWN/GAP`    |
| `BIO_LOGICAL_LAWS_CANON.md`              | `LOG`         | reserved canon slot   | `UNKNOWN/GAP`    |
| `CANON_LAW_CROSSWALK.md`                 | `CROSSWALK`   | relational index slot | `UNKNOWN/GAP`    |

No stronger semantic equivalence among these artifacts is established by their placeholder definitions.

---

# 32. Current Supported Relations

Based only on the supplied placeholder contracts, the following relation class is supportable:

```text
[[ABSOLUTE_LOGIC_CANON]]
GOVERNED_BY
[[LAW_HIERARCHY]]

[[ABSOLUTE_STRUCTURAL_INTEGRITY_CANON]]
GOVERNED_BY
[[LAW_HIERARCHY]]

[[BIO_LOGICAL_LAWS_CANON]]
GOVERNED_BY
[[LAW_HIERARCHY]]

CANON_LAW_CROSSWALK
GOVERNED_BY
[[LAW_HIERARCHY]]
```

These are artifact metadata relations inherited from the supplied RSCF relation blocks.

They do not establish the substantive content of `LAW_HIERARCHY`.

---

# 33. Current Shared Index Relations

The supplied artifacts additionally declare:

```text
[[ABSOLUTE_LOGIC_CANON]]
INDEXED_BY
[[00_HOME]]

[[ABSOLUTE_LOGIC_CANON]]
INDEXED_BY
[[AMOS_RSCF_NODES]]
```

and equivalent index relationships for the other supplied core-law artifacts.

These are graph-navigation relations, not epistemic validation relations.

---

# 34. Unsupported Relations

The current evidence does **not** establish:

```text
[[ABSOLUTE_LOGIC_CANON]]
IDENTICAL_TO
[[ABSOLUTE_STRUCTURAL_INTEGRITY_CANON]]
```

nor:

```text
[[BIO_LOGICAL_LAWS_CANON]]
DERIVED_FROM
[[ABSOLUTE_LOGIC_CANON]]
```

nor:

```text
[[ABSOLUTE_STRUCTURAL_INTEGRITY_CANON]]
GOVERNS
[[BIO_LOGICAL_LAWS_CANON]]
```

nor any substantive ordering among these framework families.

Such relations remain:

```text
UNKNOWN/GAP
```

until native sources establish them.

---

# 35. Law Hierarchy Boundary

The existence of:

```text
[[LAW_HIERARCHY]]
```

indicates a target governing artifact.

However, the supplied crosswalk placeholder does not itself establish its substantive precedence rules.

Therefore:

```text
[[LAW_HIERARCHY]] REFERENCE EXISTS
```

does not imply:

```text
LAW HIERARCHY CONTENT KNOWN
```

---

# 36. Precedence Target

If future native canon establishes precedence, a precedence rule SHOULD declare:

```yaml
precedence_rule:

  higher: law_ref
  lower: law_ref

  relation:
    type: governs | constrains | overrides

  applicability:
    scope: required
    regime: required

  authority:
    source_ref: required

  exceptions:
    - condition

  provenance:
    - ref
```

---

# 37. Precedence Is Scoped

No law SHOULD automatically be treated as globally superior merely because it occupies a higher architectural layer.

```text
ARCHITECTURAL HEIGHT
!=
UNIVERSAL PRECEDENCE
```

Precedence may depend on:

```text
DOMAIN
REGIME
OPERATION
AUTHORITY
VERSION
EPOCH
```

---

# 38. Conflict Resolution Target

When two laws appear to conflict:

```text
LAW_A
vs
LAW_B
```

the target resolution sequence is:

```text
CHECK IDENTITY
↓
CHECK VERSION
↓
CHECK SCOPE
↓
CHECK REGIME
↓
CHECK PRECEDENCE
↓
CHECK SUPERSESSION
↓
CHECK AUTHORITY
↓
CHECK PROVENANCE
↓
PRESERVE COMPETING IF UNRESOLVED
```

Do not resolve contradiction merely by selecting the more fluent or more recent formulation.

---

# 39. Scope Firewall

Every substantive crosswalk relation SHOULD declare an applicability envelope.

Target:

```yaml
scope:
  system: required
  domain: required
  environment: optional
  scale: optional
  population: optional
  temporal_window: required_if_material
  measurement_method: optional
  assumptions:
    - assumption
```

A relation valid within one scope MUST NOT silently generalize outside it.

---

# 40. Regime Firewall

Suppose:

```text
LAW_A COMPATIBLE_WITH LAW_B
```

under regime `R1`.

This does not establish:

```text
LAW_A COMPATIBLE_WITH LAW_B
```

under `R2`.

Relation validity is regime-bound when regime matters.

---

# 41. Temporal Validity

Crosswalk entries SHOULD declare freshness or temporal validity where relevant.

A relation may become stale because:

```text
LAW VERSION CHANGED

SOURCE SUPERSEDED

DEPENDENCY INVALIDATED

REGIME CHANGED

AUTHORITY EPOCH EXPIRED

NEW CONFLICT DISCOVERED
```

Stale entries MUST NOT be silently reused.

---

# 42. Version-Aware Mapping

Relations SHOULD bind versions.

Preferred:

```text
LAW_A@v2
SUPERSEDES
LAW_A@v1
```

rather than an unqualified:

```text
LAW_A
SUPERSEDES
LAW_A
```

Version ambiguity should fail closed for consequential operations.

---

# 43. Lineage Graph

Target:

```text
SOURCE
  ↓
HISTORICAL FORMULATION
  ↓
CANON CANDIDATE
  ↓
CANONICAL VERSION
  ↓
SUPERSEDED VERSION
```

All material transitions SHOULD remain traversable.

---

# 44. Provenance Topology

A crosswalk relation SHOULD preserve not only source references but ancestry.

Conceptually:

```text
ROOT_SOURCE_A
      ↓
ARTIFACT_A
      ↓
CROSSWALK_RELATION_X
```

and:

```text
ROOT_SOURCE_B
      ↓
ARTIFACT_B
      ↓
CROSSWALK_RELATION_X
```

If `ROOT_SOURCE_A = ROOT_SOURCE_B`, apparent dual support may be correlated.

---

# 45. Anti-Sybil Rule

Invalid confidence inflation:

```text
ROOT SOURCE A
├─ FILE 1
├─ FILE 2
├─ FILE 3
└─ FILE 4

THEREFORE
4 INDEPENDENT CONFIRMATIONS
```

Correct:

```text
1 ROOT ANCESTRY
+
4 DESCENDANTS
```

unless genuine independence is demonstrated.

---

# 46. Provenance Independence

A relation claiming independent confirmation SHOULD test for shared:

```text
SOURCE
AUTHORSHIP
DATA
MODEL
TRANSFORMATION
DOCUMENT LINEAGE
MEASUREMENT PIPELINE
ASSUMPTIONS
```

Independence is demonstrated, not assumed.

---

# 47. Causal Firewall

Crosswalk edges MUST preserve causal typing.

```text
DEPENDS_ON
!=
CAUSES
```

```text
CORRELATED_WITH
!=
CAUSES
```

```text
PRECEDES
!=
CAUSES
```

```text
ANALOGOUS_TO
!=
CAUSES
```

Only appropriately typed evidence licenses causal relations.

---

# 48. Structural Similarity Firewall

Two laws may share:

```text
VARIABLE STRUCTURE
EQUATION FORM
GRAPH TOPOLOGY
FEEDBACK PATTERN
OPTIMIZATION FORM
```

without sharing meaning or causal mechanism.

Therefore:

```text
ISOMORPHIC FORM
!=
IDENTICAL SEMANTICS
```

---

# 49. Cross-Domain Mapping Firewall

Suppose one law belongs to:

```text
BIOLOGY
```

and another to:

```text
COMPUTATION
```

A structural correspondence SHOULD default to:

```text
ANALOGOUS_TO
```

or:

```text
MODEL
```

not `IDENTICAL_TO`.

Cross-domain equivalence requires independent validation.

---

# 50. Evidence Topology

Crosswalk support objects SHOULD distinguish:

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL
DECISION
UNKNOWN
```

A crosswalk SHOULD never flatten these into a generic `evidence` bucket when the distinction can change the conclusion.

---

# 51. Confidence Ceiling

For a relation:

```text
R(A,B)
```

derived from premises:

```text
P1 ... Pn
```

the relation's confidence cannot exceed its weakest load-bearing premise unless independently revalidated.

Conceptually:

```text
CONFIDENCE(R)
<=
MIN_LOAD_BEARING_CONFIDENCE(P1...Pn)
```

This is a reasoning discipline, not a claim of a universally valid mathematical probability formula.

---

# 52. Competing Mappings

A source pair may support multiple possible relations.

Example:

```text
A ALIAS_OF B
```

versus:

```text
A SPECIALIZES B
```

If evidence cannot discriminate:

```text
RELATION_STATE = COMPETING
```

Do not arbitrarily choose one.

---

# 53. Discriminating Test

The preferred next check is the cheapest test that distinguishes competing mappings.

For example:

```text
SAME STABLE ID?
```

may distinguish alias from specialization more efficiently than broad semantic comparison.

---

# 54. Sensitivity

For consequential crosswalk decisions identify what smallest premise could flip the relation.

Examples:

```text
VERSION MATCH

SCOPE MATCH

ROOT PROVENANCE

SUPERSESSION RECORD

AUTHORITY EPOCH

ONE LOAD-BEARING DEFINITION
```

Fragile relations SHOULD be marked:

```text
CONDITIONAL
```

---

# 55. Proof Capsule — Crosswalk Entry

A consequential relation SHOULD conceptually carry:

```yaml
proof_capsule:

  claim:
    source: law_A
    relation: relation_type
    target: law_B

  claim_class: required

  load_bearing_premises:
    - premise

  provenance:
    - ref

  scope:
    - condition

  temporal_validity:
    state: required

  regime:
    state: required

  dependencies:
    - ref

  competing_relations:
    - relation

  falsifiers:
    - invalidation_condition

  confidence_ceiling:
    value: required

  provenance_independence:
    state: established | partial | unknown
```

---

# 56. Current Proof Capsule

```yaml
proof_capsule:

  id: PC_CANON_LAW_CROSSWALK_CURRENT

  claim: >
    AMOS OS reserves a Canon-plane artifact named
    CANON_LAW_CROSSWALK.md for crosswalking core-law artifacts.

  claim_class: SOURCE_CLAIM

  evidence:
    - CANON_LAW_CROSSWALK placeholder artifact

  scope:
    system: AMOS_OS
    plane: 01_CANON
    segment: 01_CANON/01_CORE_LAWS

  dependencies:
    - AMOS_CANON_INGESTION_RULE

  falsifiers:
    - canonical manifest supersedes or removes the artifact
    - provenance establishes the artifact is not part of AMOS corpus

  confidence_ceiling: source_supported

  populated_native_crosswalk_established: false
  executable_crosswalk_established: false
```

---

# 57. RSCF Crosswalk Graph

Target:

```text
CANON_LAW_CROSSWALK
        │
        ├── INDEXES ─────────> LAW
        │
        ├── LINKS ───────────> LAW ↔ LAW
        │
        ├── TRACKS ──────────> VERSION
        │
        ├── TRACKS ──────────> LINEAGE
        │
        ├── TRACKS ──────────> PROVENANCE
        │
        ├── TRACKS ──────────> SCOPE
        │
        ├── TRACKS ──────────> REGIME
        │
        ├── PRESERVES ───────> CONFLICT
        │
        ├── REFERENCES ──────> EVIDENCE
        │
        └── REFERENCES ──────> VALIDATION_RECEIPT
```

---

# 58. H/M/L Fractal Target

```text
H — CANON LAW SYSTEM
      ↓
M — LAW FAMILY / RELATION FAMILY
      ↓
L — LAW / RELATION / VERSION / PROVENANCE EDGE
      ↓
RAW SOURCE OR EVIDENCE
```

Raw source material defaults to:

```text
DO_NOT_LOAD_UNLESS_REQUIRED
```

---

# 59. H-Layer Node

Target:

```text
RSCF.AMOS.CANON.CROSSWALK.H.SYSTEM
```

Responsibility:

```text
ROUTING
INDEXING
RELATION DISCOVERY
CONFLICT VISIBILITY
LINEAGE NAVIGATION
```

It MUST NOT infer unsupported semantic relations merely to complete the graph.

---

# 60. Candidate M-Layer Families

Organizational target only:

```text
M.IDENTITY_RELATIONS

M.LINEAGE_RELATIONS

M.DEPENDENCY_RELATIONS

M.GOVERNANCE_RELATIONS

M.SCOPE_RELATIONS

M.COMPATIBILITY_RELATIONS

M.CONFLICT_RELATIONS

M.ANALOGY_RELATIONS

M.EVIDENCE_RELATIONS

M.IMPLEMENTATION_RELATIONS

M.VALIDATION_RELATIONS
```

These are schema categories, not claims that corresponding populated native-canon relations already exist.

---

# 61. Candidate L-Layer Nodes

```text
L.LAW_IDENTITY

L.CROSSWALK_ENTRY

L.VERSION_EDGE

L.PROVENANCE_EDGE

L.DEPENDENCY_EDGE

L.CONFLICT_EDGE

L.COMPETING_EDGE

L.SCOPE_ENVELOPE

L.REGIME_ENVELOPE

L.FALSIFIER

L.[[L19_PROOF_CAPSULE]]

L.VALIDATION_RECEIPT

L.GAP
```

---

# 62. Dependency Closure

When evaluating one relation:

```text
A RELATION B
```

load only dependencies that can change that relation's classification.

Target traversal:

```text
RELATION
↓
IDENTITY
↓
LOAD-BEARING DEFINITIONS
↓
SCOPE / REGIME
↓
PROVENANCE
↓
CONFLICTS
```

Do not load the entire AMOS canon when a smaller proof closure is sufficient.

---

# 63. Fast Path

A relation may use local validation only when:

```text
DEPENDENCY CLOSURE ESTABLISHED

PROVENANCE INDEPENDENCE SUFFICIENT

SCOPE COMPATIBLE

REGIME COMPATIBLE

FRESHNESS ACCEPTABLE

NO MATERIAL CONFLICT
```

Otherwise escalate.

---

# 64. Escalation Conditions

Escalate crosswalk reasoning when:

```text
SHARED PROVENANCE ANCESTRY

CONFLICTING SOURCES

STALE VERSION

CROSS-REGIME MAPPING

CAUSAL COUPLING

GOVERNANCE IMPACT

IRREVERSIBLE MUTATION

AMBIGUOUS DEPENDENCY

UNRESOLVED IDENTITY

SUPERSESSION UNCERTAINTY
```

---

# 65. Adversarial Validation

For consequential relations, challenge the strongest candidate relation through a genuinely different path.

Search for:

```text
CONTRADICTION

SHARED ANCESTRY

STALE PREMISE

SCOPE LEAKAGE

REGIME MISMATCH

HIDDEN DEPENDENCY

CAUSAL OVERREACH

MISIDENTIFIED VERSION

MISCLASSIFIED ALIAS

UNRECORDED SUPERSESSION

STRONGER ALTERNATIVE RELATION
```

If challenge succeeds, downgrade or preserve competing mappings.

---

# 66. Gap Taxonomy

```text
CRITICAL
DECISION-RELEVANT
EXPLANATORY
COSMETIC
```

Priority:

```text
CRITICAL
>
DECISION-RELEVANT
>
EXPLANATORY
>
COSMETIC
```

---

# 67. Critical Gap — Complete Native Law Inventory

```yaml
gap:
  id: GAP_CROSSWALK_NATIVE_LAW_INVENTORY
  class: CRITICAL
  state: UNKNOWN/GAP

  description: >
    A complete verified inventory of native AMOS canonical
    core-law artifacts has not been established from the
    supplied placeholder alone.

  required:
    - native_canon_manifest
    - stable_artifact_ids
    - versions
    - provenance
```

---

# 68. Critical Gap — Substantive Law Content

```yaml
gap:
  id: GAP_CROSSWALK_SUBSTANTIVE_LAWS
  class: CRITICAL
  state: UNKNOWN/GAP

  description: >
    The substantive law definitions required to establish
    semantic relationships among reserved law families have
    not been established by this placeholder.
```

---

# 69. Critical Gap — Hierarchy Semantics

```yaml
gap:
  id: GAP_CROSSWALK_LAW_HIERARCHY
  class: CRITICAL
  state: UNKNOWN/GAP

  description: >
    [[LAW_HIERARCHY]] is referenced as a governing artifact, but
    its complete substantive precedence semantics are not
    established by the supplied crosswalk placeholder.
```

---

# 70. Critical Gap — Executable Binding

```yaml
gap:
  id: GAP_CROSSWALK_EXECUTABLE_BINDING
  class: CRITICAL
  state: UNKNOWN/GAP

  description: >
    No executable implementation enforcing or validating the
    crosswalk has been established.
```

---

# 71. Critical Gap — Validation

```yaml
gap:
  id: GAP_CROSSWALK_VALIDATION
  class: CRITICAL
  state: UNKNOWN/GAP

  description: >
    No artifact-specific executed validation receipt proving
    crosswalk correctness has been established.
```

---

# 72. Worked Semantics — Add Relation

Given a proposed relation:

```text
LAW_A
DEPENDS_ON
LAW_B
```

target process:

1. resolve `LAW_A` identity and version;
2. resolve `LAW_B` identity and version;
3. recover native source supporting dependency;
4. determine whether dependency is load-bearing;
5. declare scope and regime;
6. inspect competing mappings;
7. inspect shared provenance;
8. classify epistemic status;
9. create proposal;
10. validate;
11. commit or hold;
12. record receipt.

Without steps 3–8:

```text
RELATION = UNKNOWN/GAP
```

---

# 73. Worked Semantics — Apparent Duplicate

Suppose:

```text
FILE_A = "Absolute Logic"
FILE_B = "Absolute Logical Law"
```

Do not immediately deduplicate.

Required:

```text
COMPARE CONTENT
+
COMPARE STABLE ID
+
COMPARE PROVENANCE
+
COMPARE LINEAGE
+
COMPARE VERSION
```

Possible results:

```text
IDENTICAL_TO

ALIAS_OF

RENAMED_FROM

OVERLAPS_WITH

DISTINCT

COMPETING

UNKNOWN/GAP
```

---

# 74. Worked Semantics — Conflicting Laws

Suppose:

```text
LAW_A says X

LAW_B says NOT X
```

First check whether both claims share:

```text
SCOPE
REGIME
TIME
DEFINITIONS
ASSUMPTIONS
```

If yes and both remain supported:

```text
CONFLICTS_WITH
+
COMPETING
```

If they apply to different regimes, preserve both without manufacturing contradiction.

---

# 75. Worked Semantics — Supersession

Suppose native provenance establishes:

```text
LAW_A@2.0
SUPERSEDES
LAW_A@1.0
```

Then:

```text
LAW_A@1.0
```

remains available for lineage and historical interpretation.

Operational routing may prefer `2.0` only within the scope authorized by the supersession record.

---

# 76. Worked Semantics — Weak Similarity

Suppose two laws have the same algebraic form:

```text
Y = kX
```

This supports, at most, a structural observation.

It does not establish:

```text
IDENTICAL_TO
```

because variables, units, domains, mechanisms, and scope may differ.

---

# 77. Worked Semantics — Shared Source

Suppose:

```text
LAW_A documented in FILE_1
LAW_A documented in FILE_2
```

but:

```text
FILE_2 derived from FILE_1
```

Then the crosswalk MUST preserve:

```text
ONE ROOT ANCESTRY
```

rather than counting two independent confirmations.

---

# 78. Worked Semantics — Dependency Failure

Suppose:

```text
LAW_C
DEPENDS_ON
LAW_B

LAW_B
DEPENDS_ON
PREMISE_A
```

If `PREMISE_A` fails:

```text
INVALIDATE:
LAW_B-dependent conclusion
LAW_C-dependent conclusion
```

Do not invalidate unrelated laws.

---

# 79. Worked Semantics — Scope Change

Suppose:

```text
RELATION R(A,B)
```

is validated for:

```text
REGIME_1
```

A request applies it to:

```text
REGIME_2
```

Correct state:

```text
REVALIDATE
```

not automatic reuse.

---

# 80. Worked Semantics — Governance

Suppose an artifact is referenced by many canonical nodes.

This graph centrality does not establish:

```text
GOVERNS
```

Governance requires explicit authority.

```text
POPULARITY
!=
AUTHORITY
```

---

# 81. Mutation Discipline

For any consequential crosswalk mutation:

```text
ADMIT
↓
BIND SCOPE
↓
CHECK AUTHORITY
↓
RESOLVE IDENTITY
↓
RESOLVE VERSION
↓
RESOLVE PROVENANCE
↓
CHECK DEPENDENCIES
↓
CHECK CONFLICTS
↓
PROPOSE
↓
VALIDATE
↓
COMMIT OR HOLD
↓
RECEIPT
```

---

# 82. Fail-Closed Rule

If a load-bearing field is unresolved:

```text
UNKNOWN/GAP
```

is not equivalent to:

```text
PASS
```

Consequential crosswalk mutations SHOULD fail closed.

---

# 83. Rollback Basin

Before a consequential mutation, preserve enough prior state to reverse:

```text
RELATION ADDITION

RELATION REMOVAL

IDENTITY MERGE

SUPERSESSION

PRECEDENCE CHANGE

CANONICAL PROMOTION
```

Identity merges require especially strong rollback discipline because incorrect merges can corrupt large dependency subgraphs.

---

# 84. Identity Merge Safety

A proposed merge:

```text
NODE_A + NODE_B → NODE_C
```

SHOULD require:

```text
IDENTITY EVIDENCE
+
PROVENANCE CHECK
+
DEPENDENCY CHECK
+
CONFLICT CHECK
+
ROLLBACK PLAN
```

When uncertain:

```text
KEEP SEPARATE
+
LINK AS POSSIBLY_RELATED
```

rather than destructive merge.

---

# 85. Repair Semantics

If a crosswalk relation is later invalidated:

```text
REMOVE / DOWNGRADE FAILED EDGE
↓
INVALIDATE DEPENDENT RELATIONS
↓
PRESERVE UNAFFECTED GRAPH
↓
REBUILD LOCAL CLOSURE
```

Global recomputation is last resort.

---

# 86. Canonical Promotion Checklist

Before this crosswalk becomes populated canon:

* [ ] complete native law inventory established;
* [ ] stable identities assigned or recovered;
* [ ] versions resolved;
* [ ] native provenance linked;
* [ ] duplicate candidates compared;
* [ ] aliases distinguished from identity;
* [ ] supersession lineage established;
* [ ] dependency edges typed;
* [ ] governance edges authorized;
* [ ] scope envelopes declared;
* [ ] regime envelopes declared;
* [ ] conflict edges preserved;
* [ ] competing mappings preserved;
* [ ] external evidence kept outside native canon;
* [ ] provenance independence evaluated;
* [ ] negative cases tested;
* [ ] rollback basin demonstrated;
* [ ] executable binding status declared;
* [ ] artifact-specific validation receipt executed;
* [ ] unresolved critical gaps remain visible.

---

# 87. Negative Validation Matrix

Required target cases:

```text
MISSING ARTIFACT

MISSING LAW ID

DUPLICATE ID

VERSION AMBIGUITY

MALFORMED RELATION

UNSUPPORTED IDENTITY

UNSUPPORTED ALIAS

UNSUPPORTED SUPERSESSION

UNSUPPORTED DERIVATION

UNSUPPORTED CAUSAL EDGE

SCOPE MISMATCH

REGIME MISMATCH

STALE RELATION

SHARED PROVENANCE

CONFLICTING SOURCES

CYCLIC DEPENDENCY

CYCLIC SUPERSESSION

UNAUTHORIZED GOVERNANCE EDGE

FAILED VALIDATION RECEIPT

FAILED ROLLBACK

UNKNOWN/GAP TREATED AS PASS
```

---

# 88. Cycle Discipline

Some relation types may legitimately cycle.

For example:

```text
COMPATIBLE_WITH
OVERLAPS_WITH
ANALOGOUS_TO
```

may be symmetric.

Other cycles are suspicious or invalid.

Example:

```text
A SUPERSEDES B
B SUPERSEDES A
```

requires investigation.

Likewise a dependency cycle may require explicit recursive semantics rather than silent acceptance.

---

# 89. Symmetry Discipline

Relations SHOULD declare symmetry.

Examples conceptually:

```text
OVERLAPS_WITH
→ potentially symmetric

CONFLICTS_WITH
→ generally symmetric at relation level

ANALOGOUS_TO
→ often symmetric structurally

DEPENDS_ON
→ directional

SUPERSEDES
→ directional

GOVERNS
→ directional
```

Exact semantics remain subject to native canon.

---

# 90. Transitivity Discipline

Do not assume transitivity unless relation semantics establish it.

For example:

```text
A ANALOGOUS_TO B
B ANALOGOUS_TO C
```

does not prove:

```text
A ANALOGOUS_TO C
```

Likewise:

```text
A COMPATIBLE_WITH B
B COMPATIBLE_WITH C
```

does not prove:

```text
A COMPATIBLE_WITH C
```

---

# 91. Relation Algebra — Target Metadata

Each relation type MAY eventually declare:

```yaml
relation_type:
  name: DEPENDS_ON
  directional: true
  symmetric: false
  transitive: conditional
  authority_sensitive: false
  scope_sensitive: true
  regime_sensitive: true
  causal: false
```

This is target metadata.

Native canon must determine final semantics.

---

# 92. Canon Law Crosswalk Query Contract

Target query:

```yaml
query:
  source_law: optional
  target_law: optional
  relation_type: optional
  version: optional
  scope: optional
  regime: optional
  epistemic_class: optional
  canonical_status: optional
```

Target response SHOULD preserve:

```text
MATCHED RELATIONS
+
PROVENANCE
+
SCOPE
+
REGIME
+
CONFLICTS
+
GAPS
+
CONFIDENCE CEILING
```

---

# 93. Query Integrity Rule

A query returning no conflict MUST NOT automatically report:

```text
COMPATIBLE
```

Correct:

```text
NO CONFLICT FOUND
```

unless compatibility has actually been established.

Absence of evidence is not proof.

---

# 94. Crosswalk Completeness Rule

A crosswalk may be internally correct yet incomplete.

Therefore maintain separately:

```text
CORRECTNESS STATUS
```

and:

```text
COMPLETENESS STATUS
```

Current completeness:

```text
UNKNOWN/GAP
```

---

# 95. Crosswalk Freshness Rule

Each substantive relation SHOULD be invalidated or rechecked when any load-bearing component changes:

```text
SOURCE VERSION

LAW VERSION

SCOPE

REGIME

AUTHORITY EPOCH

DEPENDENCY

SUPERSESSION STATE

VALIDATION RECEIPT
```

---

# 96. Cross-Plane Bindings

Target:

```text
CANON_LAW_CROSSWALK
        │
        ├─ GOVERNED_BY ─────> [[LAW_HIERARCHY]]
        │
        ├─ INDEXED_BY ──────> [[00_HOME]]
        │
        ├─ INDEXED_BY ──────> [[AMOS_RSCF_NODES]]
        │
        ├─ INTERACTS_WITH ──> KERNEL
        │
        ├─ CONTROLLED_BY ───> CONTROL_PLANE
        │
        ├─ OBSERVED_BY ─────> OBSERVABILITY
        │
        └─ RECOVERED_BY ────> OPERATIONS
```

References:

*
*
*
*
*
*
*

---

# 97. Observability Boundary

Observability may report:

```text
RELATION CREATED

RELATION USED

RELATION FAILED

CONFLICT DETECTED

VERSION STALE
```

but:

```text
OBSERVABILITY
!=
AUTHORITY
```

Monitoring cannot approve canon mutation.

---

# 98. Validation Receipt Boundary

Current placeholder references:

```text
[[ROUTING_POLICY_VALIDATION_RECEIPT]]

[[AUTHZ_ENGINE_VALIDATION_RECEIPT]]
```

These generic references do not themselves establish that the Canon Law Crosswalk has been validated.

A mature artifact SHOULD possess crosswalk-specific executed receipts.

---

# 99. Target Crosswalk Validation Receipt

```yaml
validation_receipt:

  artifact_id:
    amos_01_canon_01_core_laws_canon_law_crosswalk

  artifact_version:
    required

  validator:
    required

  executed_at:
    required

  tested:
    identity_resolution: required
    version_resolution: required
    provenance_resolution: required
    relation_typing: required
    scope_validation: required
    regime_validation: required
    conflict_preservation: required
    negative_cases: required
    rollback: required

  result:
    PASS | FAIL | CONDITIONAL

  unresolved_gaps:
    - gap_ref
```

No such executed receipt is established by this placeholder.

---

# 100. Canonical Knowledge Capsule

**Class: AMOS_MODEL / SOURCE_CLAIM**

The **Canon Law Crosswalk** is an AMOS Canon-plane slot intended to represent typed relationships among canonical law artifacts while preserving identity, provenance, lineage, scope, regime, conflicts, competing interpretations, and validation state.

The crosswalk does not create laws and does not create empirical truth.

Its core integrity rules are:

```text
CROSSWALK_ENTRY != LAW

MAPPING != EQUIVALENCE

SIMILARITY != IDENTITY

DEPENDENCY != CAUSATION

SUPERSESSION != DELETION

REFERENCE != AUTHORITY

NO CONFLICT FOUND != VERIFIED COMPATIBILITY
```

The supplied artifact context supports recognition of reserved canonical slots including:

```text
[[ABSOLUTE_LOGIC_CANON]]
[[ABSOLUTE_STRUCTURAL_INTEGRITY_CANON]]
[[BIO_LOGICAL_LAWS_CANON]]
CANON_LAW_CROSSWALK
```

and their declared governance relation to:

```text
[[LAW_HIERARCHY]]
```

but does not yet establish substantive semantic mappings among those law families.

Accordingly, the populated native law crosswalk remains:

```text
UNKNOWN/GAP
```

---

# 101. Final Integrity Rule

Until the native law inventory and substantive law sources are recovered:

```text
DO NOT INVENT
MISSING CROSSWALK RELATIONS
```

Instead:

```text
PRESERVE ARTIFACT IDENTITY
+
PRESERVE VERSION
+
PRESERVE PROVENANCE
+
PRESERVE LINEAGE
+
PRESERVE CONFLICT
+
PRESERVE COMPETING RELATIONS
+
MARK UNKNOWN/GAP
+
RETRIEVE NATIVE SOURCE
+
NORMALIZE
+
VALIDATE
+
PROMOTE WITH RECEIPTS
```

---

# 102. Canonical Invariants

```text
INTEGRITY > COMPLETENESS > FLUENCY > SPEED > TOKEN SAVINGS

PLACEHOLDER != IMPLEMENTED

ADDRESSABLE != VALIDATED

DOCUMENTED != ENFORCED

MODEL != OBSERVATION

SOURCE_CLAIM != VERIFIED

CANON_CANDIDATE != CANONICAL

CANONICAL != EMPIRICAL_TRUTH

CROSSWALK_ENTRY != LAW

MAPPING != EQUIVALENCE

SIMILARITY != IDENTITY

OVERLAP != DUPLICATION

DEPENDENCY != DERIVATION

DERIVATION != CAUSATION

STRUCTURAL SIMILARITY != CAUSATION

REFERENCE != AUTHORITY

CENTRALITY != AUTHORITY

SUPERSESSION != DELETION

IMPLEMENTED != VALIDATED

CAPABILITY != AUTHORITY

AUTHORIZATION != COMMIT

PROPOSAL != COMMIT

LOGGED != APPROVED

UNKNOWN/GAP != PASS
```

```
---

00_ROOT_MOC|AMOS MOC

---

**Related:**  ·

---

RSCF-NODE

node_id: amos_01_canon_01_core_laws_canon_law_crosswalk

node_type: crosswalk

path: 01_CANON/01_CORE_LAWS/CANON_LAW_CROSSWALK.md

origin_architect: Trang Phan

steward: Trang Phan

system: AMOS OS

claim_class: AMOS_MODEL

rscf_state: placeholder_expanded

canonical_status: UNKNOWN/GAP

implementation_status: NOT_ESTABLISHED

validation_status: NOT_ESTABLISHED

executable_binding: NOT_ESTABLISHED

native_law_inventory_status: NOT_ESTABLISHED

native_mapping_status: NOT_ESTABLISHED

RSCF-RELATIONS:

- INDEXED_BY:

- INDEXED_BY:

- GOVERNED_BY:

- INTERACTS_WITH:

- CONTROLLED_BY:

- OBSERVED_BY:

- RECOVERED_BY:

---

**MOC:**

---

**Origin Architect / Steward:** Trang Phan

**System:** AMOS OS

**Epistemic Class:** AMOS_MODEL

**Canonical Status:** UNKNOWN/GAP

**Native law inventory:** NOT_ESTABLISHED

**Native semantic crosswalk:** NOT_ESTABLISHED

**Executable binding:** NOT_ESTABLISHED

**Validation:** NOT_ESTABLISHED


```
```
