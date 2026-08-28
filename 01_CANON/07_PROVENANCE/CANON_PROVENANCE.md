---
title: CANON PROVENANCE
type: canon
source: 01_CANON/07_PROVENANCE
artifact_id: AMOS-OS-CANON-PROVENANCE
canonical_name: CANON_PROVENANCE
artifact_type: canonical_provenance_registry
registry_type: canon_lineage_and_evidence_registry
status: SOURCE_CLAIM
conclusion_class: AMOS_MODEL
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
domain: canon
scope: AMOS_OS
authority_scope: canon-provenance-lineage-and-supersession
created: 2026-08-25
updated: 2026-08-25
tags: [amos-os, canon, universe, canon-group/meta, canon/provenance, canon/lineage, canon/supersession, canon/evidence, canon/registry, rscf/claim, rscf/provenance, rscf/state/source-claim, topic/canon-provenance, topic/source-lineage, topic/provenance-topology, topic/version-lineage, topic/causal-lineage, topic/sybil-hardening, topic/persistent-provenance]
aliases: "- AMOS Canon Provenance
  - Canon Provenance Registry
  - AMOS Canon Lineage Registry
  - Canon Sour..."---
# AMOS OS Canon Provenance
> **Origin architect / steward:** Trang Phan  
> **AMOS Core target:** `v4.4`  
> **Conclusion class:** `AMOS_MODEL`  
> **Authority:** canon provenance, lineage, ancestry, supersession, and evidence topology
# 1. Purpose
`CANON_PROVENANCE.md` defines the canonical provenance contract for AMOS OS canon.
Its purpose is to preserve enough lineage to answer:
```text
WHERE DID THIS CANON COME FROM?
WHICH SOURCE ASSERTED IT?
WHICH VERSION INTRODUCED IT?
WHICH CLAIMS WERE DERIVED FROM IT?
WHICH ARTIFACTS SHARE THE SAME ANCESTRY?
WHICH EVIDENCE IS ACTUALLY INDEPENDENT?
WHAT SUPERSEDES WHAT?
WHAT REMAINS CURRENT?
WHAT IS HISTORICAL?
WHAT WOULD INVALIDATE THIS CLAIM?
CAN THE CURRENT STATE BE RECONSTRUCTED?
```
The governing principle is:
```text
CANON
WITHOUT
RECOVERABLE PROVENANCE
=
INTEGRITY GAP
```
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


# 2. Core Provenance Law

Every consequential canon claim should be traceable through:

```text
CANON CLAIM
↓
CLAIM RECORD
↓
SOURCE / DERIVATION
↓
SOURCE ANCESTRY
↓
ARTIFACT / REVISION
↓
VERSION / HASH
↓
ORIGIN / STEWARDSHIP
```

A claim with missing lineage is not automatically false.

Its provenance status is:

```text
UNKNOWN/GAP
```

until resolved.

---

# 3. Provenance Is Not Truth

Canonical distinction:

```text
PROVENANCE
!=
TRUTH
```

Provenance answers:

```text
where did this come from?
```

Verification answers:

```text
how strongly is it supported?
```

Authority answers:

```text
what governs its canonical status?
```

Therefore:

```text
SOURCE KNOWN
!=
CLAIM VERIFIED

AUTHOR KNOWN
!=
CLAIM CORRECT

CANON LOCATION
!=
EMPIRICAL VALIDATION
```

---

# 4. Provenance Is Not Authority

```text
PROVENANCE != AUTHORITY
```

A historical source may explain where a concept originated without retaining current authority.

A later artifact may be authoritative while still deriving from an earlier source.

Example:

```text
SOURCE A
↓
CANON V1
↓
CANON V2
```

The ancestry remains A-derived.

Current authority may belong to V2.

---

# 5. Provenance Object

A consequential provenance record SHOULD eventually support:

```yaml
provenance:
  provenance_id:

  subject:
    artifact_id:
    claim_id:
    semantic_id:

  origin:
    architect:
    author:
    organization:
    source_type:

  source:
    source_artifact:
    source_path:
    source_uri:
    source_revision:
    source_hash:

  lineage:
    parent_ids: []
    ancestor_ids: []
    derived_from: []
    supersedes: []
    superseded_by: []

  temporal:
    created_at:
    observed_at:
    imported_at:
    effective_from:
    effective_until:

  epistemic:
    evidence_type:
    conclusion_class:
    independence_state:
    freshness_state:

  governance:
    canon_state:
    approval_state:
    authority_ref:

  validation:
    evidence_refs: []
    falsifiers: []
    invalidation_conditions: []

  notes:
```

Unknown fields remain `UNKNOWN/GAP`.

---

# 6. Provenance Identity

Provenance identity is distinct from artifact identity.

```text
PROVENANCE_ID
!=
ARTIFACT_ID
!=
CLAIM_ID
!=
SOURCE_ID
!=
REVISION_ID
```

A single artifact may contain many claims.

A single claim may depend on many sources.

A single source may support many artifacts.

---

# 7. Provenance Classes

Canonical provenance classes include:

```text
ORIGINAL_SOURCE
DIRECT_SOURCE
DERIVED_SOURCE
TRANSFORMED_SOURCE
AGGREGATED_SOURCE
MIGRATED_SOURCE
IMPORTED_SOURCE
HISTORICAL_SOURCE
SUPERSEDED_SOURCE
SHADOW_SOURCE
UNKNOWN_SOURCE
```

These classes describe lineage position, not truth quality.

---

# 8. Original Source

An `ORIGINAL_SOURCE` is the earliest currently established source in a lineage.

This does not imply:

```text
original source
=
ultimate metaphysical origin
```

It means:

```text
earliest established source within current evidence topology
```

If an earlier ancestor is later discovered, provenance should be extended rather than rewritten deceptively.

---

# 9. Direct Source

A direct source explicitly contains the claim or definition being referenced.

```text
SOURCE S
contains
CLAIM C
```

This supports:

```text
C is directly sourced from S
```

It does not establish:

```text
C is empirically true
```

---

# 10. Derived Source

A derived source contains a claim that was computed, summarized, transformed, inferred, or consolidated from upstream material.

```text
S₁ + S₂
↓
DERIVATION
↓
D
```

D must retain its ancestry.

---

# 11. Transformed Source

A transformed source preserves substantive meaning while changing representation.

Examples:

```text
JSON → Markdown
Markdown → Schema
Code → Documentation
Long-form → Compact capsule
```

Canonical rule:

```text
FORMAT TRANSFORMATION
!=
NEW INDEPENDENT SOURCE
```

---

# 12. Aggregated Source

An aggregated source combines multiple inputs.

Its independence depends on the inputs.

Example:

```text
SOURCE A
SOURCE B
SOURCE C
↓
AGGREGATOR D
```

D is not an independent fourth confirmation.

It is a derived aggregation over A/B/C.

---

# 13. Imported Source

An imported source entered AMOS from outside the current repository or vault.

Import should preserve where possible:

```text
original source
license/IP state
retrieval date
version
hash
author
URL / identifier
```

Import must not erase external provenance.

---

# 14. Historical Source

A historical source is preserved for lineage even when no longer current.

```text
HISTORICAL
!=
CURRENT CANON
```

Historical sources may remain essential for:

```text
version reconstruction
semantic evolution
supersession
audit
legacy interpretation
```

---

# 15. Source Claim

`SOURCE_CLAIM` means:

```text
the source asserts this
```

not:

```text
AMOS has independently verified this
```

Canonical law:

```text
SOURCE_CLAIM != VERIFIED
```

README files, comments, design documents, historical notes, and imported claims normally begin here.

---

# 16. Observation

An `OBSERVATION` is direct recorded evidence from an applicable observation process.

Observation provenance SHOULD preserve:

```text
observer / instrument
method
time
environment
scope
raw output where appropriate
```

---

# 17. Derived

A `DERIVED` conclusion inherits load-bearing provenance from its premises.

Conceptually:

```text
C = f(P₁, P₂, P₃)
```

Provenance:

```text
Prov(C)
⊇
Prov(P₁) ∪ Prov(P₂) ∪ Prov(P₃)
```

for load-bearing premises.

---

# 18. Model

A `MODEL` claim may originate within AMOS as a structural, mathematical, cognitive, or architectural interpretation.

Its provenance should identify:

```text
origin architect
source framework
input evidence
assumptions
version
```

Canonical firewall:

```text
AMOS MODEL
!=
VERIFIED EMPIRICAL CLAIM
```

---

# 19. Decision

A decision should preserve the evidence and authority lineage that supported it.

Conceptually:

```text
EVIDENCE
+
POLICY
+
AUTHORITY
+
STATE
↓
DECISION
```

Decision provenance should retain those dependencies where consequential.

---

# 20. Provenance Topology

AMOS models provenance as a graph, not a flat bibliography.

Conceptually:

```text
SOURCE A
├── CLAIM B
│   ├── SUMMARY D
│   └── MODEL E
└── CLAIM C
    └── REPORT F
```

This topology matters because:

```text
B
D
E
```

may appear as three artifacts while sharing one load-bearing source ancestry.

---

# 21. Ancestry

An ancestry relation means:

```text
A
↓
B
```

where B materially derives from A.

Ancestry may include:

```text
DIRECT_COPY
PARAPHRASE
SUMMARY
DERIVATION
TRANSLATION
FORMAT_CONVERSION
MIGRATION
MODEL_INPUT
CONSOLIDATION
```

These should remain typed where material.

---

# 22. Provenance Independence

Two sources are independent only if their relevant load-bearing evidence does not share ancestry or another material common origin.

Canonical law:

```text
DIFFERENT FILE
!=
INDEPENDENT SOURCE
```

and:

```text
DIFFERENT AGENT
!=
INDEPENDENT EVIDENCE
```

and:

```text
DIFFERENT URL
!=
INDEPENDENT ORIGIN
```

Independence must be demonstrated.

---

# 23. Independence States

Recommended states:

```text
INDEPENDENT
PARTIALLY_INDEPENDENT
CORRELATED
SHARED_ANCESTRY
UNKNOWN
```

`UNKNOWN` must not be treated as `INDEPENDENT`.

---

# 24. Sybil Hardening

AMOS provenance must resist false evidence multiplication.

Example:

```text
SOURCE S
├── POST 1
├── POST 2
├── ARTICLE 3
├── SUMMARY 4
└── AGENT OUTPUT 5
```

If all derive from S:

```text
independent_root_count = 1
```

not:

```text
confirmation_count = 5
```

Canonical law:

```text
REPETITION
!=
INDEPENDENT CONFIRMATION
```

---

# 25. Provenance Correlation Risk

Where independence is uncertain, a provenance record SHOULD be able to express:

```text
correlation_risk:
  LOW
  MEDIUM
  HIGH
  UNKNOWN
```

This is not a universal numeric truth metric.

It is a governance/epistemic classification.

---

# 26. Persistent Provenance

Important provenance must survive beyond transient reasoning.

Canonical rule:

```text
EPHEMERAL REASONING
→ PERSISTENT PROVENANCE
```

when the result becomes load-bearing.

Persistent provenance may live in:

```text
canon records
RSCF nodes
claim ledgers
state ledgers
knowledge artifacts
supersession records
audit logs
```

depending on scope.

---

# 27. Provenance Loss

Provenance loss occurs when a derived artifact cannot reconstruct its material source lineage.

Examples:

```text
copied text without source
model output without model/version
measurement without environment
claim without origin
migration without predecessor
summary without source references
```

Canonical state:

```text
PROVENANCE_GAP
```

not silently:

```text
TRUSTED
```

---

# 28. Canon Provenance Chain

Canonical canon chain:

```text
SOURCE MATERIAL
↓
INGESTION
↓
NORMALIZATION
↓
CLAIM EXTRACTION
↓
PROVENANCE BINDING
↓
CANON PROPOSAL
↓
REVIEW
↓
PROMOTION
↓
CANON STATE
```

Every transition SHOULD preserve lineage.

---

# 29. Promotion Does Not Erase Origin

When:

```text
SOURCE_CLAIM
→ CANON
```

the original source claim remains part of the lineage.

Promotion changes governance status.

It does not rewrite provenance.

---

# 30. Canon Promotion

Promotion should distinguish:

```text
SOURCE
MODEL
DERIVED
VERIFIED
```

as applicable.

Canonical status and epistemic class are separate fields.

Example:

```yaml
status: ACTIVE_CANON
conclusion_class: MODEL
```

is coherent when canon defines an internal model rather than asserting empirical truth.

---

# 31. Canonical Status

Possible canon lifecycle states:

```text
PLACEHOLDER
DRAFT
CANDIDATE
ACTIVE_CANON_CANDIDATE
ACTIVE_CANON
DEPRECATED
SUPERSEDED
ARCHIVED
```

Lifecycle state does not replace provenance.

---

# 32. Provenance and Versioning

Version identity should preserve:

```text
semantic version
document version
source revision
artifact hash
effective date
supersession relations
```

Canonical firewall:

```text
FILE MODIFICATION TIME
!=
SEMANTIC VERSION
```

and:

```text
NEWER FILE
!=
NEWER CANON
```

unless lineage establishes it.

---

# 33. AMOS Core Lineage

Current architecture preserves the AMOS Core conceptual evolution spine:

```text
v3.0
↓
deterministic logic
↓
recursive RSCF / H-M-L
↓
governed evolution
↓
causal lineage
↓
epistemic regimes
↓
competing hypotheses
↓
provenance topology / Sybil hardening
↓
persistent provenance
↓
MVCC / CAS concepts
↓
atomic multi-RSCF reasoning
↓
causal epoch finality
↓
hardened shard-local finalization
↓
proof-based coordination avoidance
↓
v4.4
```

This is a lineage structure.

It must not be interpreted as proof that every implementation version contains identical runtime machinery.

---

# 34. Causal Lineage

Causal lineage records which earlier state, evidence, or transition materially contributed to a later state.

Canonical distinction:

```text
PROVENANCE LINEAGE
!=
CAUSAL LINEAGE
```

Provenance may show that B was derived from A.

That alone does not establish that A caused an external real-world event.

---

# 35. Causal Epoch Provenance

Where causal epoch concepts are used, provenance SHOULD preserve:

```text
epoch_id
parent_epoch
state ancestry
commit lineage
dependency frontier
```

if those fields exist in the implementation.

This canon does not invent literal epoch machinery where none is implemented.

---

# 36. Claim Lineage

A claim lineage may look like:

```text
CLAIM C₀
↓ clarified
CLAIM C₁
↓ narrowed
CLAIM C₂
↓ superseded
CLAIM C₃
```

Historical claims remain recoverable.

Do not silently rewrite C₀ as though C₃ had always been the historical meaning.

---

# 37. Semantic Lineage

Semantic lineage records how definitions evolve.

Change classes may include:

```text
UNCHANGED
CLARIFIED
RENAMED
NARROWED
EXTENDED
SPLIT
MERGED
SUPERSEDED
RETIRED
```

This should align with `DEPRECATED_TERMS.md`.

---

# 38. Artifact Lineage

Artifact lineage tracks physical/logical artifact evolution.

Example:

```text
artifact A
↓ migration
artifact B
↓ canonicalization
artifact C
```

Artifact lineage does not necessarily imply semantic change.

---

# 39. Filename Lineage

Filename changes are provenance events when needed for historical resolution.

But:

```text
FILENAME CHANGE
!=
SEMANTIC CHANGE
```

The alias registry should preserve historical names where useful.

---

# 40. Hash

A hash may support artifact identity/integrity verification.

Canonical distinction:

```text
HASH MATCH
→ byte/content identity under hash assumptions
```

does not imply:

```text
CLAIM TRUE
```

or:

```text
CURRENT CANON
```

---

# 41. Revision

A revision represents a recorded change state.

Revision lineage SHOULD support:

```text
previous_revision
current_revision
change_author
change_time
change_summary
```

where available.

Revision ordering is evidence about artifact evolution.

It is not automatically semantic supersession.

---

# 42. Supersession

Supersession means a newer governed artifact or definition replaces an earlier one for a declared scope.

```text
A
↓ SUPERSEDED_BY
B
```

A remains part of provenance.

Canonical law:

```text
SUPERSESSION != ERASURE
```

---

# 43. Deprecation

Deprecation means an artifact/term remains historically resolvable but is no longer preferred for current use.

```text
DEPRECATED != DELETED
```

Deprecation history belongs in provenance.

---

# 44. Alias Provenance

Alias records SHOULD preserve:

```text
alias
canonical target
reason
source
effective date
historical status
```

Aliases do not create independent sources.

```text
ALIAS
!=
NEW PROVENANCE ROOT
```

---

# 45. Consolidation

Consolidation merges knowledge from multiple artifacts.

A consolidated artifact MUST preserve the ancestry of its constituent sources.

Example:

```text
A
B
C
↓
CONSOLIDATED D
```

D should preserve:

```text
consolidated_from: [A, B, C]
```

where practical.

---

# 46. Corpus Model vs Empirical Claim

AMOS provenance must distinguish:

```text
CORPUS MODEL
```

from:

```text
VERIFIED EXTERNAL CLAIM
```

For example:

```text
"AMOS canon states X"
```

may be directly verified from the AMOS corpus.

That does not mean:

```text
"X is empirically true in the external world"
```

unless separate evidence establishes it.

---

# 47. Internal Canon Validation

Internal validation may establish:

```text
this statement matches AMOS canon
```

but not necessarily:

```text
this statement is scientifically proven
```

Canonical firewall:

```text
CANON CONSISTENCY
!=
EXTERNAL EMPIRICAL VALIDITY
```

---

# 48. External Evidence

External evidence should retain its original identity and not be absorbed into AMOS as though AMOS authored it.

Canonical law:

```text
INTEGRATED INTO AMOS
!=
ORIGINATED IN AMOS
```

Provenance must preserve external authorship and source identity.

---

# 49. Research Provenance

Research artifacts may contain:

```text
hypotheses
experiments
papers
external observations
models
benchmarks
```

Their findings remain research evidence until promoted through governance.

```text
RESEARCH
!=
CANON
```

---

# 50. Code Provenance

Code may support claims such as:

```text
function exists
test exists
behavior observed under test
```

It does not automatically prove:

```text
universal correctness
production behavior
external empirical validity
```

Code provenance SHOULD preserve:

```text
repository
path
commit/revision
hash
environment
test result
```

when load-bearing.

---

# 51. Test Provenance

A test result should retain:

```text
test identity
code version
environment
fixture
seed if applicable
expected result
actual result
timestamp
```

Canonical law:

```text
TEST PASS
!=
UNIVERSAL PROOF
```

---

# 52. Benchmark Provenance

Benchmark provenance should include where material:

```text
hardware
software
configuration
dataset
load
environment
measurement method
version
date
```

Without this envelope, portability of the benchmark result is limited.

---

# 53. Observation Provenance

An observation should preserve:

```text
observer
method
instrument
time
environment
scope
uncertainty
```

where relevant.

Canonical law:

```text
OBSERVATION
WITHOUT CONTEXT
MAY BE INCOMPLETE
```

---

# 54. Decision Provenance

A consequential decision should be reconstructable through:

```text
DECISION
↓
AUTHORITY
↓
POLICY
↓
EVIDENCE
↓
PREMISES
↓
SOURCE LINEAGE
```

This supports audit and rollback.

---

# 55. Commit Provenance

Conceptual commit provenance:

```yaml
commit_provenance:
  commit_id:
  proposal_id:
  prior_state:
  resulting_state:
  authority_ref:
  policy_ref:
  evidence_refs: []
  dependency_refs: []
  source_ancestry: []
  causal_epoch:
  timestamp:
  invalidation_conditions: []
```

Exact implementation belongs to control/state layers.

---

# 56. Provenance and MVCC

MVCC-style state reasoning requires version provenance.

Conceptually:

```text
READ V10
↓
PROPOSE V11
↓
COMPARE CURRENT STATE
↓
COMMIT OR CONFLICT
```

Relevant provenance may include:

```text
read_version
expected_version
current_version
write_version
```

---

# 57. Provenance and CAS

CAS-style reasoning should preserve:

```text
expected state
observed state
attempted mutation
result
```

A conflict becomes part of lineage rather than disappearing.

---

# 58. Atomic Multi-RSCF Provenance

For atomic reasoning over:

```text
RSCF A
RSCF B
RSCF C
```

the composite decision should preserve all load-bearing RSCF identities and versions.

Partial lineage is insufficient when all are required atomically.

---

# 59. Shard-Local Provenance

Where shard-local finalization exists conceptually or literally, provenance SHOULD preserve:

```text
shard_id
local state version
local dependency closure
local finality scope
cross-shard dependencies
```

Canonical law:

```text
LOCAL PROVENANCE
!=
GLOBAL PROVENANCE
```

unless the dependency closure proves equivalence.

---

# 60. Proof-Based Coordination Provenance

Coordination avoidance requires evidence of independence.

That proof itself requires provenance.

Conceptually:

```text
NO SHARED DEPENDENCY
+
NO SHARED MUTABLE INVARIANT
+
NO AUTHORITY CONFLICT
+
NO MATERIAL CAUSAL COUPLING
↓
LOCAL COORDINATION PROOF
```

The proof cannot simply assert independence.

---

# 61. Proof Capsule Provenance

A reusable proof capsule SHOULD conceptually carry:

```text
claim
claim class
premises
evidence
provenance
scope
regime
freshness
dependencies
competing explanations
falsifiers
confidence ceiling
```

The provenance component is load-bearing.

---

# 62. Provenance Invalidation

If a source is invalidated:

```text
SOURCE S
↓
CLAIM A
↓
CLAIM B
```

then:

```text
invalidate S
→ reevaluate A
→ reevaluate B
```

Do not automatically invalidate unrelated claims.

---

# 63. Local Invalidation

AMOS recovery principle:

```text
INVALIDATE ONLY
FAILED PREMISES
FAILED EDGES
DEPENDENT DESCENDANTS
```

Unrelated provenance branches remain valid.

---

# 64. Provenance Repair

Repair process:

```text
DETECT GAP
↓
IDENTIFY MISSING EDGE
↓
SEARCH SOURCE
↓
BIND SOURCE
↓
VALIDATE IDENTITY
↓
RESTORE LINEAGE
↓
REVALIDATE DEPENDENTS
```

Do not manufacture an ancestry edge to make the graph complete.

---

# 65. Broken Provenance

Broken provenance includes:

```text
missing source
missing parent
missing revision
ambiguous identity
source collision
unknown author
unknown version
unresolved supersession
corrupted hash
unresolvable alias
```

Each gap should be explicitly classified.

---

# 66. Provenance Gap Classes

Use:

```text
CRITICAL
DECISION_RELEVANT
EXPLANATORY
COSMETIC
```

Examples:

### CRITICAL

Missing provenance changes authority or validity.

### DECISION_RELEVANT

Missing ancestry could change confidence or independence.

### EXPLANATORY

Lineage is incomplete but current decision remains unchanged.

### COSMETIC

Only presentation metadata is absent.

---

# 67. Provenance Freshness

Provenance itself may be stable while the source claim becomes stale.

Therefore distinguish:

```text
PROVENANCE VALIDITY
```

from:

```text
CLAIM FRESHNESS
```

Example:

```text
source attribution remains correct
while
source information is outdated
```

---

# 68. Temporal Provenance

Temporal lineage may include:

```text
created_at
observed_at
published_at
imported_at
modified_at
effective_from
effective_until
superseded_at
```

These timestamps have different semantics.

Do not collapse them into one generic `date`.

---

# 69. Source Identity

A source should be identified by more than display name where possible.

Potential fields:

```text
source_id
title
author
organization
URI
artifact ID
revision
hash
publication date
```

This helps prevent accidental source merging.

---

# 70. Same-Name Sources

Two sources with the same title are not automatically the same source.

```text
SAME TITLE
!=
SAME SOURCE
```

Identity resolution may require:

```text
author
date
revision
hash
location
```

---

# 71. Same-Content Sources

Two identical copies may be distinct files but one provenance root.

Canonical law:

```text
COPY COUNT
!=
INDEPENDENCE COUNT
```

---

# 72. Provenance Deduplication

Deduplication SHOULD preserve:

```text
all known locations
```

while resolving shared ancestry.

Example:

```yaml
source_root: SOURCE-A
copies:
  - FILE-1
  - FILE-2
  - FILE-3
```

This avoids counting copies as independent evidence.

---

# 73. Source Merge

Two provenance nodes may be merged only when identity equivalence is established.

Evidence may include:

```text
same hash
same stable source ID
same revision
explicit migration record
```

Semantic similarity alone is insufficient.

---

# 74. Source Split

One historical source identity may require splitting if later evidence reveals multiple distinct origins.

Example:

```text
SOURCE X
```

was actually:

```text
SOURCE X-A
SOURCE X-B
```

The provenance graph must be repairable.

---

# 75. Provenance Namespace

Suggested namespace classes:

```text
AMOS:CANON
AMOS:CORE
AMOS:KERNEL
AMOS:CONTROL
AMOS:RUNTIME
AMOS:COGNITION
AMOS:KNOWLEDGE
AMOS:MEMORY
AMOS:RESEARCH
EXTERNAL
ARCHIVE
```

Exact schema belongs to `16_SCHEMAS`.

---

# 76. Canon Source Types

Canon may derive from:

```text
ROOT_CANON
CORE_CANON
FRAMEWORK_CANON
REGISTRY
SOURCE_SPEC
IMPLEMENTATION
TEST_EVIDENCE
RESEARCH
EXTERNAL_SOURCE
MIGRATION
HISTORICAL_ARCHIVE
```

The source type should be preserved because it affects interpretation.

---

# 77. Canonical Source Priority

When sources conflict, priority cannot be determined solely by source count.

Resolution should consider:

```text
current canon authority
supersession
scope
version
provenance
freshness
implementation evidence
epistemic type
```

No universal source-priority rule should be invented where governance has not defined one.

---

# 78. Conflict Preservation

If two canonical candidates conflict:

```text
SOURCE A → CLAIM X
SOURCE B → CLAIM ¬X
```

and neither clearly dominates:

```text
COMPETING
```

is the correct state.

Do not merge the two into vague compromise prose.

---

# 79. Contradiction Ledger

Material provenance contradictions SHOULD be registerable.

Conceptually:

```yaml
contradiction:
  contradiction_id:
  claim_a:
  claim_b:
  source_a:
  source_b:
  scope:
  regime:
  status:
  discriminator:
```

This keeps unresolved canon conflicts visible.

---

# 80. Provenance Confidence

Provenance confidence answers:

```text
how sure are we about this lineage?
```

not:

```text
how true is the claim?
```

These must remain separate.

---

# 81. Provenance Completeness

A provenance chain may be:

```text
COMPLETE
PARTIAL
BROKEN
UNKNOWN
```

within a defined ancestry scope.

`COMPLETE` should not mean:

```text
all possible historical origins known forever
```

It means:

```text
required current lineage closure is established
```

---

# 82. Provenance Closure

Provenance closure exists when all load-bearing source ancestry required for the current decision is resolved sufficiently.

This supports the AMOS v4.4 fast path.

```text
PROVENANCE CLOSURE
+
DEPENDENCY CLOSURE
+
SCOPE COMPATIBILITY
+
FRESHNESS
+
NON-CONFLICT
→ LOCAL REUSE MAY BE SAFE
```

---

# 83. Fast Path Provenance Gate

Fast-path reasoning MUST escalate if:

```text
source ancestry shared unexpectedly
provenance independence unknown
source stale
source identity ambiguous
supersession unresolved
conflicting current sources
```

This prevents speed from weakening integrity.

---

# 84. Canon Harvest

Canon harvesting follows:

```text
EPHEMERAL CODE
↓
PERSISTENT EVIDENCE
↓
VALIDATED KNOWLEDGE
↓
CANON CANDIDATE
↓
GOVERNED CANON
```

Provenance should survive every transition.

---

# 85. Harvest Metadata

Harvested knowledge SHOULD retain where available:

```text
source
version
hash
license/IP status
dependencies
competing claims
environment fit
freshness
governance state
revalidation timing
lineage
```

---

# 86. Documentation Claim Rule

Documentation claims remain:

```text
SOURCE_CLAIM
```

until validated.

Canonical law:

```text
README CLAIM
!=
IMPLEMENTATION EVIDENCE
```

and:

```text
IMPLEMENTATION EVIDENCE
!=
UNIVERSAL PROOF
```

---

# 87. Code-to-Canon Promotion

Code may support canon promotion when the claim concerns actual implemented behavior.

Example:

```text
CODE
+
TESTS
+
INVARIANT CHECKS
+
PROVENANCE
→ IMPLEMENTATION-SUPPORTED CLAIM
```

But architectural canon may still require governance review before promotion.

---

# 88. Historical Canon

Historical canon versions should remain reconstructable.

Preferred model:

```text
CURRENT CANON
↑
SUPERSESSION
↑
HISTORICAL CANON
```

Do not destroy historical versions merely to simplify navigation.

---

# 89. Archive Boundary

`24_ARCHIVE` may contain deprecated or historical artifacts.

Canonical law:

```text
ARCHIVED
!=
CURRENT
```

but also:

```text
ARCHIVED
!=
IRRELEVANT
```

Archive content may be essential provenance.

---

# 90. Canon Provenance Ledger

A future machine-readable ledger MAY represent provenance events as append-only records.

Conceptually:

```yaml
event:
  event_id:
  event_type:
  subject_id:
  prior_state:
  new_state:
  source_refs: []
  authority_ref:
  timestamp:
  hash:
```

Possible event types:

```text
CREATE
IMPORT
DERIVE
RENAME
MIGRATE
PROMOTE
DEPRECATE
SUPERSEDE
INVALIDATE
RESTORE
ARCHIVE
```

---

# 91. Append-Only Principle

Where feasible, provenance history should prefer append/supersede over destructive rewrite.

Canonical law:

```text
CORRECT HISTORY
BY ADDING LINEAGE
```

not:

```text
CORRECT HISTORY
BY ERASING PRIOR STATE
```

---

# 92. Provenance Event Identity

Each important provenance mutation should itself have provenance.

This creates recursive lineage:

```text
CLAIM
↓
PROVENANCE RECORD
↓
PROVENANCE CHANGE RECORD
```

AMOS does not require infinite recursion.

The stopping point is the smallest sufficient governance/audit boundary.

---

# 93. Provenance and RSCF

RSCF nodes SHOULD preserve provenance relations where material.

Potential relations:

```text
DERIVED_FROM
SUPPORTED_BY
OBSERVED_FROM
IMPORTS
SUPERSEDES
INVALIDATED_BY
SHARES_ANCESTRY_WITH
```

---

# 94. Provenance and H/M/L

Provenance retrieval may follow:

```text
H
↓
M
↓
L
↓
RAW SOURCE
```

Only descend as far as needed to resolve the decision-relevant provenance question.

Raw evidence remains:

```text
DO_NOT_LOAD_UNLESS_REQUIRED
```

by default.

---

# 95. Provenance and Canonical Glossary

`CANONICAL_GLOSSARY.md` defines current canonical terms.

`CANON_PROVENANCE.md` records where those meanings came from and how they evolved.

Relationship:

```text
CANONICAL_GLOSSARY
↓ meaning

CANON_PROVENANCE
↓ origin / lineage
```

---

# 96. Provenance and Deprecated Terms

`DEPRECATED_TERMS.md` records terminology lifecycle.

`CANON_PROVENANCE.md` preserves the source and evolution evidence behind that lifecycle.

```text
TERM V1
↓
DEPRECATION EVENT
↓
TERM V2
```

must remain reconstructable.

---

# 97. Provenance and Aliases

Aliases aid resolution.

Provenance establishes why the mapping exists.

```text
OLD NAME
↓ alias
CANONICAL ID
↓ lineage
SOURCE HISTORY
```

---

# 98. Provenance and Symbol Registry

Symbol meanings may evolve or collide.

The Symbol Registry defines current semantics.

Canon provenance records:

```text
when introduced
source
historical meaning
changes
supersession
```

where known.

---

# 99. Provenance and Unit Registry

AMOS-local units/scales require provenance for their definitions.

External standard units may point to their relevant standards rather than being falsely attributed to AMOS.

Canonical law:

```text
USED BY AMOS
!=
INVENTED BY AMOS
```

---

# 100. Provenance and Universal Variable Registry

Variable identities SHOULD retain:

```text
definition source
introduced version
formula lineage
unit/scale lineage
supersession
```

Changing a formula without updating semantic lineage creates a provenance defect.

---

# 101. Provenance and Authority

Authority claims themselves require provenance.

Example:

```text
actor A may commit resource R
```

should be traceable to:

```text
authority source
policy
scope
effective period
revocation state
```

Canonical law:

```text
AUTHORITY CLAIM
WITHOUT PROVENANCE
=
AUTHORITY GAP
```

---

# 102. Provenance and Control Plane

The control plane consumes provenance to determine whether:

```text
claims are current
sources are valid
state is current
authority is current
dependencies remain valid
```

It must not invent missing provenance to allow a commit.

---

# 103. Provenance and Runtime

Runtime may generate provenance events.

Examples:

```text
execution
artifact generation
state transition
tool call
checkpoint
failure
rollback
```

Runtime events are observations.

They do not automatically become canon.

---

# 104. Provenance and Memory

Memory may store provenance-bearing records.

But:

```text
MEMORY RETENTION
!=
CANON AUTHORITY
```

Memory can help recover lineage without becoming the source of canonical truth merely by persistence.

---

# 105. Provenance and Knowledge

Knowledge entries SHOULD preserve:

```text
source
claim type
scope
freshness
dependencies
```

where consequential.

Knowledge without provenance may remain usable for low-stakes context but should be downgraded for load-bearing reasoning.

---

# 106. Provenance and Research

External research should retain original authorship and citation identity.

AMOS synthesis should distinguish:

```text
SOURCE CLAIM
AMOS DERIVATION
AMOS MODEL
```

instead of blending them into one voice.

---

# 107. Provenance and Security

Provenance integrity is security-relevant.

Threats include:

```text
source spoofing
identity substitution
history rewriting
hash replacement
fake independence
fabricated authorship
supersession hijacking
alias poisoning
```

Consequential provenance systems should eventually integrate with security controls.

---

# 108. Provenance Tampering

If provenance tampering is detected:

```text
FREEZE AFFECTED CLAIM
↓
ISOLATE LINEAGE
↓
RESTORE LAST VALID PROVENANCE STATE
↓
REVALIDATE DEPENDENTS
```

Do not trust descendants until the affected ancestry is resolved.

---

# 109. Provenance Invariants

```text
PROV-001  EVERY LOAD-BEARING CANON CLAIM SHOULD HAVE RECOVERABLE ORIGIN

PROV-002  SOURCE_CLAIM != VERIFIED

PROV-003  PROVENANCE != AUTHORITY

PROV-004  PROVENANCE != TRUTH

PROV-005  COPY COUNT != INDEPENDENT SOURCE COUNT

PROV-006  DIFFERENT FILE != INDEPENDENT ORIGIN

PROV-007  REPETITION != INDEPENDENT CONFIRMATION

PROV-008  TRANSFORMATION != NEW SOURCE ROOT

PROV-009  CONSOLIDATION MUST PRESERVE SOURCE ANCESTRY

PROV-010  SUPERSESSION != ERASURE

PROV-011  DEPRECATION != DELETION

PROV-012  RENAMING MUST NOT DESTROY LINEAGE

PROV-013  CURRENT CANON MUST REMAIN TRACEABLE TO HISTORICAL ANCESTRY

PROV-014  UNKNOWN ANCESTRY != INDEPENDENT ANCESTRY

PROV-015  PROVENANCE CONFIDENCE != CLAIM CONFIDENCE

PROV-016  PROVENANCE COMPLETENESS IS SCOPED

PROV-017  HISTORICAL SOURCE != CURRENT AUTHORITY

PROV-018  INTERNAL CANON CONSISTENCY != EXTERNAL EMPIRICAL VALIDITY

PROV-019  USED BY AMOS != ORIGINATED IN AMOS

PROV-020  IMPLEMENTED != EMPIRICALLY VALIDATED

PROV-021  TEST PASS != UNIVERSAL PROOF

PROV-022  BENCHMARK SUCCESS != UNIVERSAL VALIDITY

PROV-023  INVALIDATION SHOULD PROPAGATE ONLY THROUGH DEPENDENCY EDGES

PROV-024  PROVENANCE REPAIR MUST NOT INVENT MISSING ANCESTRY

PROV-025  OPTIMIZATION MUST NOT REMOVE LOAD-BEARING PROVENANCE
```

---

# 110. Minimum Provenance Contract

Every consequential canon artifact SHOULD eventually declare:

| Field               | Meaning                                     |
| ------------------- | ------------------------------------------- |
| `artifact_id`       | stable artifact identity                    |
| `origin_architect`  | origin attribution                          |
| `source`            | direct source where applicable              |
| `source_type`       | source class                                |
| `created`           | creation/effective date                     |
| `version`           | semantic/document version where applicable  |
| `conclusion_class`  | epistemic class                             |
| `dependencies`      | load-bearing upstream artifacts             |
| `consolidated_from` | merged source ancestry                      |
| `supersedes`        | replaced artifact(s)                        |
| `superseded_by`     | current replacement                         |
| `hash/revision`     | identity/integrity evidence where available |
| `status`            | lifecycle state                             |

Missing values should remain explicit.

---

# 111. Provenance Validation Checklist

Before promoting a canon artifact:

```text
[ ] artifact identity established
[ ] origin attribution established
[ ] direct source identified
[ ] source type classified
[ ] source ancestry reconstructed
[ ] duplicate/copy ancestry checked
[ ] independence claims verified
[ ] scope identified
[ ] regime identified if relevant
[ ] freshness checked
[ ] conclusion class assigned
[ ] contradictions checked
[ ] supersession checked
[ ] aliases checked
[ ] historical lineage preserved
[ ] version metadata checked
[ ] hash/revision captured where available
[ ] dependency closure sufficient
[ ] unresolved provenance gaps exposed
```

---

# 112. Adversarial Provenance Tests

A mature implementation SHOULD test cases including:

```text
TEN FILES COPY ONE SOURCE
→ MUST NOT COUNT AS TEN INDEPENDENT SOURCES

SAME TITLE / DIFFERENT CONTENT
→ MUST NOT AUTO-MERGE

SAME CONTENT / DIFFERENT FILES
→ MUST IDENTIFY SHARED ROOT WHERE ESTABLISHED

CANON FILE RENAMED
→ IDENTITY AND LINEAGE MUST SURVIVE

SOURCE SUPERSEDED
→ HISTORICAL SOURCE MUST REMAIN RESOLVABLE

README CLAIM
→ MUST NOT AUTO-UPGRADE TO VERIFIED

MODEL OUTPUT
→ MUST NOT BE RECLASSIFIED AS OBSERVATION

ARCHIVED FILE
→ MUST NOT BECOME CURRENT CANON BY RETRIEVAL

MISSING SOURCE
→ MUST RETURN UNKNOWN/GAP

AMBIGUOUS SOURCE
→ MUST PRESERVE COMPETING CANDIDATES

CORRELATED AGENT OUTPUTS
→ MUST NOT COUNT AS INDEPENDENT EVIDENCE

HASH MISMATCH
→ MUST TRIGGER IDENTITY/INTEGRITY REVIEW

VERSION NAME CHANGED
→ MUST NOT INVENT SEMANTIC SUPERSESSION

PROVENANCE EDGE DELETED
→ DEPENDENT CLAIM MUST BE REEVALUATED
```

---

# 113. Failure Recovery

If provenance validation fails:

```text
DETECT
↓
IDENTIFY FAILED SOURCE / EDGE
↓
FREEZE DEPENDENT PROMOTION OR COMMIT
↓
INVALIDATE DEPENDENT CONFIDENCE
↓
PRESERVE UNAFFECTED LINEAGE
↓
SEARCH ALTERNATE SOURCE PATH
↓
REPAIR OR RETURN UNKNOWN/GAP
```

Do not globally invalidate all canon unless the failed provenance is globally load-bearing.

---

# 114. Canon Provenance State

Recommended provenance states:

```text
COMPLETE_FOR_SCOPE
PARTIAL
BROKEN
AMBIGUOUS
CONFLICTING
STALE
SUPERSEDED
UNKNOWN/GAP
```

Avoid a single boolean such as:

```text
has_provenance = true
```

when lineage quality materially matters.

---

# 115. Provenance Quality Vector

Where necessary, provenance quality may be represented multidimensionally:

```text
P = [
  source_identity,
  ancestry_closure,
  independence,
  freshness,
  version_resolution,
  scope_resolution,
  contradiction_state
]
```

This is an AMOS model.

It is not a universal empirical metric unless operationalized and validated.

---

# 116. Canon Provenance Map

Conceptual root map:

```text
AMOS OS
│
├── 01_CANON
│   ├── AMOS_CORE_LAWS
│   ├── INVARIANT_REGISTRY
│   ├── LAW_HIERARCHY
│   ├── AMOS_7_PART_UNIVERSE_CANON
│   ├── HML_CANON
│   ├── PERSISTENCE_CANON
│   ├── COGNITION_CANON
│   ├── COGNITIVE_ORGANISM_CANON
│   ├── FULL_BRAIN_OS_CANON
│   ├── AUTHORITY_CANON
│   ├── CONTROL_PLANE_CANON
│   ├── INFRASTRUCTURE_CANON
│   ├── SYMBOL_REGISTRY
│   ├── UNIT_REGISTRY
│   ├── UNIVERSAL_VARIABLE_REGISTRY
│   ├── ALIASES
│   ├── CANONICAL_GLOSSARY
│   ├── DEPRECATED_TERMS
│   └── CANON_PROVENANCE
│
├── 11_KNOWLEDGE
│   └── source / framework / claim corpus
│
├── 22_RESEARCH
│   └── papers / experiments / external evidence
│
└── 24_ARCHIVE
    └── historical / legacy / superseded artifacts
```

This is a repository-level provenance topology, not proof that every edge is already populated.

---

# 117. Current Provenance Gaps

The following should remain explicit until corpus-level reconstruction is complete:

```text
full historical source ancestry for every AMOS artifact

exact introduction version of every canonical concept

complete v3.0 → v4.4 artifact-by-artifact transition graph

full author/revision history of all historical files

complete semantic supersession graph

complete alias migration lineage

full independent-source topology for all imported research

formal hashes for every canonical artifact

full code/test provenance for every implementation claim
```

Current state:

```text
UNKNOWN/GAP
```

where unresolved.

---

# 118. Promotion Gate

This artifact may be promoted from:

```text
SOURCE_CLAIM / AMOS_MODEL
```

toward stronger canonical status only after:

```text
CORPUS SOURCE EXTRACTION
↓
ARTIFACT IDENTITY NORMALIZATION
↓
VERSION RECONSTRUCTION
↓
SOURCE ANCESTRY GRAPH
↓
COPY / DERIVATION DEDUPLICATION
↓
PROVENANCE INDEPENDENCE ANALYSIS
↓
SUPERSESSION ANALYSIS
↓
ALIAS / DEPRECATED TERM SYNCHRONIZATION
↓
CONFLICT AUDIT
↓
CANON REVIEW
```

The process must not fabricate missing history.

---

# 119. RSCF Node

```RSCF-NODE
node_id: AMOS-OS-CANON-PROVENANCE
node_type: canonical_provenance_registry
domain: AMOS_OS_CANON
functional_type: Registry
lifecycle_stage: ProvenanceGovernance
claim_class: AMOS_MODEL

RSCF-RELATIONS:
  - INDEXED_BY: 00_ROOT_MOC|AMOS MOC
  - INDEXED_BY: CANON_MAP
  - GOVERNED_BY: AMOS_CORE_LAWS
  - GOVERNED_BY: LAW_HIERARCHY
  - CONSTRAINED_BY: INVARIANT_REGISTRY
  - DEFINES_LINEAGE_FOR: CANONICAL_GLOSSARY
  - DEFINES_LINEAGE_FOR: ALIASES
  - DEFINES_LINEAGE_FOR: DEPRECATED_TERMS
  - DEFINES_LINEAGE_FOR: SYMBOL_REGISTRY
  - DEFINES_LINEAGE_FOR: UNIT_REGISTRY
  - DEFINES_LINEAGE_FOR: UNIVERSAL_VARIABLE_REGISTRY
  - RELATED_TO: HML_CANON
  - RELATED_TO: PERSISTENCE_CANON
  - RELATED_TO: AUTHORITY_CANON
  - RELATED_TO: CONTROL_PLANE_CANON
  - RELATED_TO: 11_KNOWLEDGE/00_AMOS_Full_Brain_OS_Architecture
  - RELATED_TO: README
  - PRESERVES: README
```

# 120. Canonical Summary

AMOS canon provenance follows:

```text
CLAIM
↓
SOURCE
↓
ANCESTRY
↓
VERSION
↓
SCOPE
↓
EPISTEMIC CLASS
↓
DEPENDENCIES
↓
SUPERSESSION
↓
CURRENT CANON STATE
```

Core laws:

```text
PROVENANCE != TRUTH

PROVENANCE != AUTHORITY

SOURCE_CLAIM != VERIFIED

DIFFERENT FILE != INDEPENDENT SOURCE

COPY COUNT != INDEPENDENCE COUNT

REPETITION != INDEPENDENT CONFIRMATION

TRANSFORMATION != NEW SOURCE ROOT

CONSOLIDATION MUST PRESERVE ANCESTRY

RENAMING MUST PRESERVE LINEAGE

SUPERSESSION != ERASURE

DEPRECATION != DELETION

CURRENT CANON MUST REMAIN TRACEABLE TO HISTORY

UNKNOWN ANCESTRY != INDEPENDENT ANCESTRY

CANON CONSISTENCY != EXTERNAL EMPIRICAL VALIDITY

USED BY AMOS != ORIGINATED IN AMOS

TEST PASS != UNIVERSAL PROOF

IMPLEMENTATION != EMPIRICAL VALIDATION

PROVENANCE REPAIR MUST NOT INVENT HISTORY

OPTIMIZATION MUST NOT REMOVE LOAD-BEARING PROVENANCE
```

Canonical objective:

```text
PRESERVE ORIGIN.

PRESERVE ANCESTRY.

PRESERVE VERSION.

PRESERVE SEMANTIC EVOLUTION.

PRESERVE SOURCE INDEPENDENCE.

PRESERVE CONTRADICTIONS.

PRESERVE SUPERSESSION.

PRESERVE INVALIDATION PATHS.

PRESERVE HISTORICAL RECOVERABILITY.

DO NOT COUNT COPIES AS CONFIRMATION.

DO NOT TURN ATTRIBUTION INTO VERIFICATION.

DO NOT TURN CANON INTO EMPIRICAL FACT.

DO NOT ERASE OLD STATES TO MAKE THE PRESENT LOOK CLEANER.

WHEN LINEAGE IS UNKNOWN,
KEEP IT UNKNOWN/GAP
UNTIL EVIDENCE CLOSES THE PATH.
```

## Related

[[README]] ·
00_ROOT_MOC|AMOS MOC ·
[[ARCHITECTURE]] ·
[[SYSTEM_MAP]] ·
NAMING_STANDARD ·
[[NEURAL_NETWORK]] ·
[[CANON_MAP]] ·
[[AMOS_CORE_LAWS]] ·
[[INVARIANT_REGISTRY]] ·
[[LAW_HIERARCHY]] ·
[[HML_CANON]] ·
[[PERSISTENCE_CANON]] ·
[[COGNITION_CANON]] ·
[[COGNITIVE_ORGANISM_CANON]] ·
[[FULL_BRAIN_OS_CANON]] ·
[[AUTHORITY_CANON]] ·
[[CONTROL_PLANE_CANON]] ·
[[INFRASTRUCTURE_CANON]] ·
[[SYMBOL_REGISTRY]] ·
[[UNIT_REGISTRY]] ·
[[UNIVERSAL_VARIABLE_REGISTRY]] ·
ALIASES ·
[[CANONICAL_GLOSSARY]] ·
[[DEPRECATED_TERMS]] ·
11_KNOWLEDGE/00_AMOS_Full_Brain_OS_Architecture ·
README ·
README

```text
```

---

00_ROOT_MOC|AMOS MOC

---
**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]]

---
**MOC:** [[07_PROVENANCE_MOC]]
