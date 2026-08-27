---
title: SOURCE LINEAGE
type: note
artifact_id: AMOS-OS-SOURCE-LINEAGE
canonical_name: SOURCE_LINEAGE
artifact_type: canonical_lineage_framework
status: SOURCE_CLAIM
conclusion_class: AMOS_MODEL
amos_core_target: v4.4

origin_architect: Trang Phan
steward: Trang Phan

domain: canon
scope: AMOS_OS
authority_scope: source-ancestry-derivation-transformation-and-supersession-lineage

created: 2026-08-25
updated: 2026-08-25

tags: [amos-os, canon, universe, canon-group/meta, canon/framework, canon/provenance, canon/lineage, canon/source-lineage, canon/supersession, rscf/claim, rscf/provenance, rscf/state/source-claim, topic/source-lineage, topic/source-ancestry, topic/causal-lineage, topic/provenance-topology, topic/dependency-lineage, topic/version-lineage, topic/supersession, topic/sybil-hardening, topic/persistent-provenance]

aliases:
  - AMOS Source Lineage
  - AMOS OS Source Lineage
  - Source Ancestry
  - Canon Source Lineage
---




# AMOS OS Source Lineage

> **Origin architect / steward:** Trang Phan  
> **AMOS Core target:** `v4.4`  
> **Conclusion class:** `AMOS_MODEL`  
> **Status:** `SOURCE_CLAIM`

## 1. Purpose

`SOURCE_LINEAGE.md` defines how AMOS OS represents the ancestry, transformation, derivation, migration, consolidation, version evolution, and supersession of sources.

Its central question is:

```text
HOW DID THIS ARTIFACT,
CLAIM,
MODEL,
DECISION,
OR STATE

GET HERE?
```

Source lineage provides the path:

```text
ORIGIN
↓
SOURCE
↓
TRANSFORMATION
↓
DERIVATION
↓
ARTIFACT
↓
CLAIM
↓
DEPENDENT CLAIMS
↓
CURRENT STATE
```

The governing law is:

```text
NO LINEAGE
→ NO ASSUMED ANCESTRY

UNKNOWN LINEAGE
→ UNKNOWN/GAP
```

---

# 2. Source Lineage Boundary

Source lineage is related to provenance but is not identical to it.

```text
PROVENANCE
=
broader evidence concerning origin,
identity,
history,
scope,
version,
authority,
and evidence topology

SOURCE LINEAGE
=
the ancestry graph connecting
sources and their descendants
```

Therefore:

```text
SOURCE_LINEAGE ⊂ PROVENANCE
```

conceptually.

This notation describes the AMOS model and is not asserted as a universal provenance ontology.

---

# 3. Source Lineage Is Not Truth

```text
KNOWN_LINEAGE != VERIFIED_TRUTH
```

A perfectly reconstructed chain may show:

```text
SOURCE A
↓
DOCUMENT B
↓
MODEL C
↓
CLAIM D
```

without establishing that D is empirically correct.

Lineage answers:

```text
WHERE DID D COME FROM?
```

Verification answers:

```text
HOW WELL IS D SUPPORTED?
```

---

# 4. Source Lineage Is Not Authority

```text
SOURCE_LINEAGE != AUTHORITY
```

A source can be historically foundational without being currently authoritative.

Example:

```text
HISTORICAL SOURCE
↓
CANON V1
↓
CANON V2
↓
CURRENT CANON
```

The historical source remains an ancestor.

Current authority may belong only to the current governed canon.

---

# 5. Fundamental Lineage Object

A lineage record SHOULD be capable of representing:

```yaml
lineage:
  lineage_id:

  subject:
    subject_id:
    subject_type:

  source:
    source_id:
    source_type:
    source_revision:
    source_hash:

  relation:
    relation_type:
    transformation_type:

  ancestry:
    direct_parents: []
    ancestors: []
    roots: []

  descendants:
    direct_children: []

  lifecycle:
    introduced_at:
    effective_from:
    superseded_at:

  governance:
    status:
    authority_ref:

  epistemic:
    conclusion_class:
    independence_state:

  scope:
    system:
    environment:
    regime:

  integrity:
    lineage_state:
    unresolved_edges: []
```

Unknown fields remain explicit rather than inferred.

---

# 6. Lineage Node Types

A lineage graph may contain:

```text
SOURCE
ARTIFACT
CLAIM
OBSERVATION
MODEL
RSCF
DECISION
STATE
VERSION
REVISION
TRANSFORMATION
MIGRATION
CANON
ARCHIVE_RECORD
```

Node type matters.

For example:

```text
SOURCE → CLAIM
```

is not semantically identical to:

```text
CLAIM → DERIVED_CLAIM
```

---

# 7. Lineage Edge Types

Canonical edge vocabulary SHOULD distinguish at least:

```text
DERIVED_FROM
COPIED_FROM
PARAPHRASED_FROM
SUMMARIZED_FROM
TRANSLATED_FROM
TRANSFORMED_FROM
MIGRATED_FROM
CONSOLIDATED_FROM
EXTRACTED_FROM
GENERATED_FROM
SUPPORTED_BY
OBSERVED_FROM
IMPORTS
DEPENDS_ON
SUPERSEDES
SUPERSEDED_BY
RENAMED_FROM
SPLIT_FROM
MERGED_FROM
INVALIDATED_BY
SHARES_ANCESTRY_WITH
```

Do not collapse materially different relationships into a generic:

```text
RELATED_TO
```

when lineage semantics matter.

---

# 8. Direct Parent

For:

```text
A
↓
B
```

A is a direct parent of B when B materially derives from A without another known lineage node between them.

Formally, within the AMOS graph model:

```text
parent(B) = A
```

does not imply:

```text
root(B) = A
```

A may itself have ancestors.

---

# 9. Ancestor

An ancestor is any upstream lineage node reachable through lineage-bearing edges.

```text
A
↓
B
↓
C
↓
D
```

For D:

```text
direct_parent = C

ancestors = {
  C,
  B,
  A
}
```

---

# 10. Root Source

A root source is the earliest established source for a lineage within the currently resolved provenance scope.

```text
ROOT
↓
...
↓
CURRENT ARTIFACT
```

Critical qualification:

```text
ROOT SOURCE
!=
ABSOLUTE HISTORICAL ORIGIN
```

It means:

```text
EARLIEST CURRENTLY ESTABLISHED ROOT
```

If earlier evidence appears, the graph expands.

---

# 11. Unknown Root

If ancestry terminates because evidence is missing:

```text
?
↓
SOURCE B
↓
CLAIM C
```

the root state is:

```text
UNKNOWN/GAP
```

Do not silently declare B the original source.

---

# 12. Original Source

`ORIGINAL_SOURCE` may be assigned only within a defined lineage scope.

Recommended interpretation:

```text
earliest source currently established
for this semantic lineage
within this evidence corpus
```

This avoids overstating historical certainty.

---

# 13. Copy Lineage

If:

```text
SOURCE A
↓ COPY
FILE B
```

then:

```text
B COPIED_FROM A
```

and:

```text
independent_root_count = 1
```

Copying creates another artifact.

It does not create independent evidence.

---

# 14. Paraphrase Lineage

```text
SOURCE A
↓ PARAPHRASE
CLAIM B
```

means B remains ancestry-dependent on A.

Canonical law:

```text
PARAPHRASE
!=
INDEPENDENT SOURCE
```

---

# 15. Summary Lineage

```text
A
↓
SUMMARY B
```

B may compress A while retaining A as a load-bearing source.

Lossy compression does not break ancestry.

---

# 16. Translation Lineage

```text
ENGLISH SOURCE A
↓ TRANSLATION
VIETNAMESE SOURCE B
```

B remains derived from A unless independent content was introduced.

Canonical law:

```text
LANGUAGE CHANGE
!=
NEW EVIDENCE ROOT
```

---

# 17. Format Transformation

Examples:

```text
JSON
→ Markdown

Markdown
→ Python

Python
→ Documentation

Document
→ RSCF capsule
```

Canonical rule:

```text
FORMAT CHANGE
!=
SOURCE INDEPENDENCE
```

Transformation lineage must survive representation changes.

---

# 18. Extraction Lineage

When a subset is extracted:

```text
MASTER SOURCE
↓
EXTRACT
↓
SUBSET ARTIFACT
```

the subset retains the master source as ancestry.

Extraction does not create a new origin.

---

# 19. Consolidation Lineage

When:

```text
SOURCE A
SOURCE B
SOURCE C
↓
CONSOLIDATION
↓
ARTIFACT D
```

D has multiple direct parents:

```text
parents(D) = {A, B, C}
```

All materially load-bearing sources should remain recoverable.

---

# 20. Consolidation Independence

If:

```text
A ← ROOT X
B ← ROOT X
C ← ROOT Y
```

then consolidation D has:

```text
artifact_parent_count = 3
```

but only:

```text
independent_root_count <= 2
```

subject to confirmation that X and Y are independent.

---

# 21. Merge Lineage

A merge combines previously distinct semantic or artifact branches.

```text
A ─┐
   ├→ C
B ─┘
```

The merge must preserve both ancestors.

Do not rewrite history as:

```text
C
```

with no parents.

---

# 22. Split Lineage

A source may split:

```text
A
├→ B
└→ C
```

Possible reasons include:

```text
scope separation
semantic separation
module decomposition
canon restructuring
```

B and C retain A as ancestry.

---

# 23. Migration Lineage

Repository migrations should preserve:

```text
OLD LOCATION
↓ MIGRATED_TO
NEW LOCATION
```

Canonical law:

```text
MIGRATION
!=
NEW ORIGIN
```

Migration metadata SHOULD retain:

```text
old path
new path
artifact identity
migration date
semantic-change state
```

---

# 24. Rename Lineage

```text
OLD_FILENAME
↓ RENAMED_TO
NEW_FILENAME
```

Canonical law:

```text
RENAME
!=
NEW ARTIFACT
```

unless governance explicitly creates a new semantic identity.

This protects AMOS against filename-based provenance loss.

---

# 25. Identity Firewall

These identities are distinct:

```text
FILENAME
ARTIFACT_ID
SEMANTIC_ID
SOURCE_ID
CLAIM_ID
VERSION_ID
REVISION_ID
LINEAGE_ID
```

Therefore:

```text
filename changed
```

does not imply:

```text
artifact identity changed
```

and:

```text
artifact identity changed
```

does not automatically imply:

```text
semantic meaning changed
```

---

# 26. Version Lineage

Conceptually:

```text
V1
↓
V2
↓
V3
```

Version lineage should preserve the relation between revisions rather than relying only on filenames.

Canonical law:

```text
VERSION LABEL
!=
LINEAGE PROOF
```

A filename containing `v4.4` does not itself prove descent from `v4.3`.

---

# 27. Revision Lineage

Revision history may be represented:

```text
R₀
↓
R₁
↓
R₂
```

Revision sequence establishes artifact evolution when the underlying revision system supports it.

It does not automatically establish semantic supersession.

---

# 28. Semantic Lineage

Semantic evolution SHOULD distinguish:

```text
UNCHANGED
CLARIFIED
RENAMED
NARROWED
EXTENDED
REFACTORED
SPLIT
MERGED
SUPERSEDED
RETIRED
```

Example:

```text
TERM A
↓ CLARIFIED
TERM A'
↓ NARROWED
TERM A''
```

This belongs jointly with:

```text
CANONICAL_GLOSSARY
DEPRECATED_TERMS
ALIASES
CANON_PROVENANCE
```

---

# 29. Supersession Lineage

```text
A
↓ SUPERSEDED_BY
B
```

means B replaces A for a declared scope.

It does not mean A disappears.

Canonical law:

```text
SUPERSESSION
!=
DELETION
```

Historical reconstruction requires A to remain resolvable.

---

# 30. Partial Supersession

Supersession may be scoped.

Example:

```text
A
├── rule X → superseded by B
└── rule Y → remains current
```

Do not mark the entire artifact obsolete when only one semantic region was replaced.

---

# 31. Deprecation Lineage

```text
ACTIVE
↓
DEPRECATED
↓
ARCHIVED
```

is a lifecycle lineage.

Deprecation means:

```text
not preferred/current
```

not:

```text
never existed
```

---

# 32. Historical Lineage

AMOS preserves historical lineage because present canon may depend on understanding earlier definitions.

Conceptually:

```text
HISTORICAL
↓
TRANSITION
↓
CURRENT
```

Removing the historical node breaks explanatory provenance.

---

# 33. AMOS Core Evolution Spine

The current AMOS architecture preserves this conceptual evolution spine:

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

This is a conceptual lineage map.

It must not be converted into artifact-level historical assertions unless corresponding source artifacts establish each transition.

---

# 34. Conceptual vs Artifact Lineage

Critical distinction:

```text
CONCEPTUAL LINEAGE
!=
ARTIFACT LINEAGE
```

A concept may evolve across multiple artifacts.

An artifact may contain multiple conceptual lineages.

Therefore the system should not assume a one-to-one mapping.

---

# 35. Claim Lineage

Claims may evolve:

```text
C₀
↓ refined
C₁
↓ scoped
C₂
↓ revalidated
C₃
```

Each transition should preserve:

```text
prior claim
change type
reason
source
scope
```

where material.

---

# 36. Derived Claim Lineage

If:

```text
P₁
P₂
P₃
↓
DERIVATION
↓
C
```

then C inherits the provenance of its load-bearing premises.

Conceptually:

```text
Ancestors(C)
⊇
Ancestors(P₁)
∪
Ancestors(P₂)
∪
Ancestors(P₃)
```

for materially load-bearing ancestry.

---

# 37. Confidence Inheritance

Derived confidence cannot exceed the weakest load-bearing premise unless independently revalidated.

Therefore source lineage matters to confidence propagation.

```text
WEAK SOURCE
↓
LOAD-BEARING PREMISE
↓
DERIVED CLAIM
```

The weakness cannot be erased merely by additional derivation layers.

---

# 38. Revalidation Branch

Independent revalidation may create:

```text
SOURCE A
↓
CLAIM C
↑
INDEPENDENT OBSERVATION B
```

If B is genuinely independent, C now has more than one support lineage.

Independence must be established rather than inferred from different storage locations.

---

# 39. Shared Ancestry

Example:

```text
        SOURCE A
       /        \
      B          C
       \        /
          D
```

B and C are distinct descendants but correlated through A.

Canonical law:

```text
MULTIPLE DESCENDANTS
!=
MULTIPLE INDEPENDENT ROOTS
```

---

# 40. Provenance Sybil Problem

A provenance Sybil pattern occurs when one origin appears as many apparently independent sources.

Example:

```text
SOURCE X
├→ ARTICLE A
├→ SUMMARY B
├→ AGENT OUTPUT C
├→ REPORT D
└→ KNOWLEDGE NOTE E
```

Without ancestry analysis:

```text
apparent_sources = 5
```

With lineage analysis:

```text
established_root_sources = 1
```

Canonical law:

```text
SOURCE MULTIPLICATION
!=
EVIDENCE MULTIPLICATION
```

---

# 41. Independence Firewall

Sources A and B should not be classified `INDEPENDENT` merely because they have:

```text
different filenames
different authors listed downstream
different URLs
different agents
different repositories
different formats
```

Independence concerns material ancestry.

Recommended states:

```text
INDEPENDENT
PARTIALLY_INDEPENDENT
CORRELATED
SHARED_ANCESTRY
UNKNOWN
```

---

# 42. Unknown Independence

Canonical rule:

```text
UNKNOWN
!=
INDEPENDENT
```

When ancestry cannot be resolved:

```text
independence_state: UNKNOWN
```

This is especially important for consequential evidence aggregation.

---

# 43. Dependency Lineage

Source ancestry and dependency ancestry overlap but are not identical.

```text
SOURCE_LINEAGE
```

tracks origin.

```text
DEPENDENCY_LINEAGE
```

tracks what a result requires to remain valid.

Example:

```text
SOURCE A
↓
PREMISE B
↓
MODEL C
↓
DECISION D
```

A may simultaneously be source ancestry and a validity dependency.

---

# 44. Causal Lineage

AMOS distinguishes:

```text
SOURCE LINEAGE
DEPENDENCY LINEAGE
CAUSAL LINEAGE
```

A document being sourced from another document does not prove external causation.

Canonical firewall:

```text
DERIVED_FROM
!=
CAUSED_BY
```

---

# 45. Causal Firewall

Sequence alone does not establish causation:

```text
A existed first
B existed later
```

does not prove:

```text
A caused B
```

A lineage edge requires evidence appropriate to the edge type.

---

# 46. Scope Lineage

Claims may inherit scope from their sources.

Example:

```text
SOURCE A
scope = environment X
↓
CLAIM B
```

B must not silently become:

```text
scope = universal
```

Canonical law:

```text
LINEAGE PRESERVES
LOAD-BEARING SCOPE CONSTRAINTS
```

unless separately validated beyond them.

---

# 47. Regime Lineage

A source established under regime R₁ may not remain valid under R₂.

```text
SOURCE
regime = R₁
↓
CLAIM
↓
REGIME SHIFT
↓
REVALIDATE
```

Lineage remains historically correct even if validity expires.

---

# 48. Temporal Lineage

Lineage SHOULD distinguish:

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

These are not interchangeable timestamps.

---

# 49. Freshness Lineage

A lineage edge may remain valid while a claim becomes stale.

Example:

```text
A is still correctly sourced from B
```

while:

```text
B no longer describes the current environment
```

Therefore:

```text
LINEAGE_VALIDITY
!=
CLAIM_FRESHNESS
```

---

# 50. Model Lineage

A model should retain:

```text
input sources
assumptions
prior models
transformation/derivation path
version
```

Canonical law:

```text
MODEL OUTPUT
DOES NOT ERASE
MODEL INPUT LINEAGE
```

---

# 51. RSCF Lineage

An RSCF node may retain:

```yaml
rscf_lineage:
  node_id:
  derived_from: []
  supported_by: []
  depends_on: []
  supersedes: []
  invalidated_by: []
  shared_ancestry: []
```

This allows dependency-aware invalidation.

---

# 52. Recursive RSCF Lineage

For recursive structures:

```text
RSCF-H
↓
RSCF-M
↓
RSCF-L
↓
EVIDENCE
```

lineage should remain traversable in both directions:

```text
claim → evidence
evidence → dependents
```

where implementation supports it.

---

# 53. H/M/L Source Resolution

AMOS retrieval should resolve lineage at the smallest sufficient level:

```text
H
↓
M
↓
L
↓
RAW SOURCE
```

Do not load every raw ancestor when higher-level lineage already resolves the decision.

But escalate when:

```text
ancestry ambiguous
sources conflict
independence uncertain
scope unclear
freshness uncertain
```

---

# 54. Persistent Lineage

Important lineage must survive transient reasoning.

Canonical principle:

```text
EPHEMERAL DERIVATION
↓
PERSISTENT LINEAGE
```

when the result becomes load-bearing.

Potential persistence targets include:

```text
RSCF
provenance registry
knowledge records
state ledger
canon records
audit logs
```

---

# 55. Lineage and Memory

Memory may preserve lineage metadata.

But:

```text
MEMORY
!=
CANON
```

Persistence in memory does not itself grant canonical status.

---

# 56. Lineage and Knowledge

Knowledge artifacts should retain enough ancestry to distinguish:

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL
DECISION
UNKNOWN
```

This prevents derived material from masquerading as primary evidence.

---

# 57. Lineage and Research

External research lineage should preserve original attribution.

Example:

```text
PAPER A
↓
AMOS SUMMARY B
↓
AMOS MODEL C
```

The model must not imply:

```text
AMOS originated PAPER A
```

Canonical law:

```text
INTEGRATION
!=
ORIGINATION
```

---

# 58. Code Lineage

Code lineage may include:

```text
repository
path
commit
revision
generated_from
forked_from
migrated_from
```

Code derived from generated templates should retain that relationship where it affects interpretation.

---

# 59. Generated Artifact Lineage

Generated artifacts should identify their generator where consequential.

```text
TEMPLATE
+
INPUT
+
GENERATOR
↓
GENERATED ARTIFACT
```

Potential lineage:

```yaml
generated_from:
  template:
  input_sources: []
  generator:
  generator_version:
```

---

# 60. Agent Output Lineage

Agent output should not be treated as a primary independent source merely because an agent produced it.

Conceptually:

```text
SOURCES
+
CONTEXT
+
MODEL/AGENT
↓
OUTPUT
```

The output inherits relevant source ancestry.

Canonical law:

```text
AGENT GENERATION
!=
INDEPENDENT CONFIRMATION
```

---

# 61. Multi-Agent Lineage

If five agents consume the same source:

```text
SOURCE A
├→ AGENT 1
├→ AGENT 2
├→ AGENT 3
├→ AGENT 4
└→ AGENT 5
```

then agent count is five.

Independent evidence roots may still be one.

---

# 62. Tool Output Lineage

Tool output SHOULD distinguish:

```text
tool identity
input
execution environment
timestamp
raw result
derived interpretation
```

where material.

A tool is an execution source, not necessarily the epistemic origin of the underlying data.

---

# 63. Observation Lineage

Observation lineage may be:

```text
ENVIRONMENT
↓
INSTRUMENT
↓
RAW OBSERVATION
↓
NORMALIZED OBSERVATION
↓
DERIVED CLAIM
```

Preserving each transformation improves falsifiability.

---

# 64. Decision Lineage

A consequential decision may require:

```text
EVIDENCE
+
MODEL
+
POLICY
+
AUTHORITY
+
STATE
↓
DECISION
```

The decision's lineage should preserve all load-bearing inputs.

---

# 65. State Lineage

State evolution may be represented:

```text
STATE S₀
↓ EVENT E₁
STATE S₁
↓ EVENT E₂
STATE S₂
```

This differs from source lineage but can intersect with it when state transitions are evidence-bearing.

---

# 66. MVCC Lineage

MVCC-style reasoning introduces version ancestry:

```text
READ Vₙ
↓
PROPOSE Vₙ₊₁
↓
VALIDATE CURRENT VERSION
↓
COMMIT / CONFLICT
```

Lineage may record:

```text
read_version
expected_version
parent_version
result_version
```

---

# 67. CAS Lineage

CAS-style mutation should preserve:

```text
expected state
observed state
proposed state
result
```

A failed compare operation remains part of execution lineage.

---

# 68. Atomic Multi-RSCF Lineage

If a result depends atomically on:

```text
RSCF-A
RSCF-B
RSCF-C
```

then all three belong to the load-bearing lineage.

Dropping one parent produces incomplete dependency closure.

---

# 69. Causal Epoch Lineage

Where causal epoch concepts are used, a lineage record MAY include:

```text
epoch_id
parent_epoch
dependency_epoch
state_version
commit ancestry
```

This section defines the conceptual lineage requirement.

It does not assert that every AMOS runtime currently implements literal causal epochs.

---

# 70. Shard-Local Lineage

Local finalization may use local lineage closure when:

```text
dependency closure is local
authority is local
provenance independence is established
no global invariant is affected
```

Canonical firewall:

```text
LOCAL LINEAGE CLOSURE
!=
GLOBAL LINEAGE CLOSURE
```

---

# 71. Coordination-Avoidance Lineage

Proof-based coordination avoidance requires demonstrating that two operations do not share relevant dependencies.

Therefore:

```text
NO SHARED LINEAGE
```

cannot merely be asserted.

The required dependency/provenance graph must support it.

---

# 72. Lineage Closure

For a claim C:

```text
Closure(C)
```

is the set of load-bearing ancestry required to evaluate C within the current scope.

Closure is decision-relative.

AMOS does not require retrieving every historical ancestor when distant history cannot alter the conclusion.

---

# 73. Minimal Sufficient Lineage

The v4.4 fast-path principle is:

```text
USE THE SMALLEST
SUFFICIENT
PROVENANCE CLOSURE
```

Local reasoning is allowed only when material ancestry has been resolved sufficiently.

---

# 74. Escalation Conditions

Lineage resolution escalates when:

```text
ancestry is ambiguous
source independence is unknown
source identity conflicts
scope differs
regime differs
freshness fails
supersession is unresolved
causal coupling exists
authority depends on lineage
irreversible action depends on the result
```

---

# 75. Lineage Conflict

A lineage conflict exists when incompatible ancestry claims exist.

Example:

```text
ARTIFACT C
claimed derived_from A

ARTIFACT C
claimed derived_from B
```

Possible states:

```text
A and B both parents
A correct / B incorrect
B correct / A incorrect
ambiguous
```

Until discriminated:

```text
COMPETING
```

may be appropriate.

---

# 76. Competing Lineages

AMOS must preserve competing ancestry hypotheses when evidence is insufficient.

```text
H₁:
A → C

H₂:
B → C
```

Do not choose whichever chain is more narratively convenient.

Preferred action:

```text
find the cheapest
high-information
discriminating evidence
```

---

# 77. Lineage Falsifiers

A lineage claim should be falsifiable where possible.

Example:

```text
CLAIM:
B was derived from A
```

Possible falsifiers:

```text
B predates A
hash/revision evidence contradicts the relation
author history identifies a different source
source content cannot support the claimed transformation
migration records identify another parent
```

---

# 78. Lineage Invalidation

If:

```text
A
↓
B
↓
C
```

and the edge:

```text
A → B
```

is invalidated, then B's ancestry and dependent lineage involving that edge must be reevaluated.

Do not automatically invalidate unrelated properties of B.

---

# 79. Descendant Invalidation

Canonical recovery principle:

```text
INVALIDATE
FAILED EDGE
+
DEPENDENT DESCENDANTS
```

not:

```text
INVALIDATE ENTIRE KNOWLEDGE GRAPH
```

unless the failed edge is globally load-bearing.

---

# 80. Lineage Repair

```text
DETECT GAP
↓
LOCATE BROKEN EDGE
↓
SEARCH CANDIDATE SOURCES
↓
TEST IDENTITY
↓
TEST TEMPORAL ORDER
↓
TEST TRANSFORMATION RELATION
↓
RESTORE EDGE OR KEEP GAP
↓
REVALIDATE DESCENDANTS
```

Never invent a missing parent.

---

# 81. Broken Lineage States

Recommended states:

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

A binary:

```text
lineage_valid = true
```

is often insufficient.

---

# 82. Lineage Gap Classification

Use:

```text
CRITICAL
DECISION_RELEVANT
EXPLANATORY
COSMETIC
```

### CRITICAL

Missing lineage prevents safe authority/canon determination.

### DECISION_RELEVANT

Missing ancestry may change confidence or independence.

### EXPLANATORY

History is incomplete but current decision remains stable.

### COSMETIC

Missing metadata does not affect semantics or governance.

---

# 83. Source Identity Collision

Two records may appear to describe the same source but differ materially.

Potential discriminators:

```text
hash
revision
date
author
path
stable ID
content
```

Do not merge them based on title alone.

---

# 84. Duplicate Source Detection

Duplicate detection may identify:

```text
EXACT_COPY
NEAR_COPY
PARAPHRASE
COMMON_ANCESTRY
UNKNOWN_RELATION
```

Only evidence-supported equivalence should collapse roots.

---

# 85. Content Similarity Firewall

```text
STRUCTURAL SIMILARITY
!=
COMMON ORIGIN
```

Two artifacts may independently resemble one another.

Similarity may justify investigation.

It does not prove lineage.

---

# 86. Temporal Firewall

```text
A predates B
```

is compatible with:

```text
B derived from A
```

but does not prove it.

Temporal ordering is a necessary condition for some ancestry claims, not sufficient evidence by itself.

---

# 87. Citation Firewall

A citation from B to A is evidence that B references A.

It does not always prove:

```text
all of B derived from A
```

Edge scope should be as precise as the evidence supports.

---

# 88. Lineage Granularity

Lineage may exist at:

```text
repository
artifact
section
paragraph
claim
equation
symbol
code function
state transition
```

Use the smallest granularity needed to avoid false ancestry claims.

---

# 89. Claim-Level Lineage

For high-value canon, claim-level lineage is preferable to assuming:

```text
entire document
derived from
entire source document
```

when only one section is actually derived.

---

# 90. Equation Lineage

Equations may require lineage including:

```text
equation_id
source
variables
assumptions
derivation
units
scope
version
```

Canonical rule:

```text
SAME SYMBOLS
!=
SAME EQUATION LINEAGE
```

---

# 91. Symbol Lineage

Symbols may evolve:

```text
ψ
↓ old meaning

ψ
↓ new meaning
```

If meaning changes, semantic lineage must distinguish the two uses even if the glyph remains identical.

---

# 92. Unit Lineage

Unit definitions may derive from:

```text
external standards
AMOS-local scales
domain conventions
```

Their origins must remain distinct.

```text
USED BY AMOS
!=
CREATED BY AMOS
```

---

# 93. Variable Lineage

A variable registry entry SHOULD preserve where known:

```text
introduced_by
defined_in
derived_from
unit lineage
formula lineage
superseded_by
```

This prevents semantic drift across models.

---

# 94. Canon Harvest Lineage

Knowledge promotion follows:

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

Every transition must preserve upstream ancestry.

---

# 95. README and Documentation Lineage

Documentation remains:

```text
SOURCE_CLAIM
```

unless independently validated.

If code documentation says:

```text
SYSTEM PROVIDES X
```

lineage establishes who/what asserted X.

Implementation/test evidence determines whether X is actually supported.

---

# 96. Archive Lineage

Archive artifacts may be upstream ancestors of current canon.

Therefore:

```text
ARCHIVED
!=
DISCONNECTED
```

Archive placement changes lifecycle status, not historical ancestry.

---

# 97. Deletion

Deletion should not erase known lineage.

Where deletion is required:

```text
artifact removed
```

while preserving an appropriate tombstone or historical record where governance permits.

Conceptually:

```text
DELETED ARTIFACT
↓
LINEAGE TOMBSTONE
```

---

# 98. Lineage Tombstone

A lineage tombstone MAY preserve:

```yaml
tombstone:
  artifact_id:
  prior_path:
  removal_date:
  removal_reason:
  superseded_by:
  prior_hash:
  lineage_refs: []
```

Exact implementation belongs to state/provenance schemas.

---

# 99. Lineage Ledger

A future append-oriented lineage ledger MAY use events such as:

```text
CREATE
IMPORT
COPY
EXTRACT
DERIVE
TRANSFORM
TRANSLATE
SUMMARIZE
MERGE
SPLIT
MIGRATE
RENAME
PROMOTE
DEPRECATE
SUPERSEDE
INVALIDATE
RESTORE
ARCHIVE
```

Each event should identify its subject and relevant parents.

---

# 100. Lineage Event Contract

Conceptually:

```yaml
lineage_event:
  event_id:
  event_type:

  subject_id:
  parent_ids: []

  actor:
  timestamp:

  prior_state:
  resulting_state:

  source_refs: []
  authority_ref:

  revision:
  hash:

  notes:
```

This is a model contract, not an assertion that a specific ledger implementation already exists.

---

# 101. Source Lineage Invariants

```text
LIN-001
UNKNOWN LINEAGE != KNOWN LINEAGE

LIN-002
DIFFERENT FILE != INDEPENDENT SOURCE

LIN-003
COPY != NEW EVIDENCE ROOT

LIN-004
PARAPHRASE != NEW EVIDENCE ROOT

LIN-005
TRANSLATION != NEW EVIDENCE ROOT

LIN-006
FORMAT TRANSFORMATION != NEW EVIDENCE ROOT

LIN-007
MIGRATION != NEW ORIGIN

LIN-008
RENAME != NEW ORIGIN

LIN-009
CONSOLIDATION MUST PRESERVE MATERIAL PARENTS

LIN-010
MERGE MUST PRESERVE BOTH BRANCHES

LIN-011
SPLIT MUST PRESERVE THE COMMON ANCESTOR

LIN-012
SUPERSESSION != ERASURE

LIN-013
DEPRECATION != DELETION

LIN-014
ARCHIVE != LOSS OF LINEAGE

LIN-015
SOURCE LINEAGE != TRUTH

LIN-016
SOURCE LINEAGE != AUTHORITY

LIN-017
DERIVED_FROM != CAUSED_BY

LIN-018
TEMPORAL ORDER != CAUSATION

LIN-019
SIMILARITY != COMMON ORIGIN

LIN-020
MULTIPLE DESCENDANTS != MULTIPLE INDEPENDENT ROOTS

LIN-021
UNKNOWN INDEPENDENCE != INDEPENDENCE

LIN-022
DERIVED CLAIMS INHERIT LOAD-BEARING ANCESTRY

LIN-023
SCOPE CONSTRAINTS PROPAGATE THROUGH LOAD-BEARING LINEAGE

LIN-024
INVALIDATION PROPAGATES ONLY THROUGH DEPENDENT EDGES

LIN-025
LINEAGE REPAIR MUST NOT INVENT HISTORY
```

---

# 102. Minimum Source Lineage Contract

Every consequential lineage-bearing artifact SHOULD eventually support:

| Field                | Purpose                                    |
| -------------------- | ------------------------------------------ |
| `artifact_id`        | stable artifact identity                   |
| `source_id`          | source identity                            |
| `source_type`        | source classification                      |
| `derived_from`       | direct ancestry                            |
| `consolidated_from`  | multi-source ancestry                      |
| `supersedes`         | outgoing supersession                      |
| `superseded_by`      | incoming supersession                      |
| `revision`           | revision identity                          |
| `hash`               | content/integrity identity where available |
| `scope`              | applicability envelope                     |
| `conclusion_class`   | epistemic classification                   |
| `independence_state` | source independence                        |
| `lineage_state`      | completeness/ambiguity state               |

Missing information remains explicit.

---

# 103. Validation Checklist

Before treating lineage as closed:

```text
[ ] subject identity resolved
[ ] direct parent(s) identified
[ ] ancestry relation typed
[ ] transformation type identified
[ ] temporal ordering checked
[ ] duplicate ancestry checked
[ ] source identity collisions checked
[ ] root candidates identified
[ ] independence tested
[ ] shared ancestry tested
[ ] version lineage checked
[ ] semantic lineage checked
[ ] supersession checked
[ ] alias history checked
[ ] scope inheritance checked
[ ] regime compatibility checked
[ ] freshness checked
[ ] contradictions checked
[ ] unresolved edges exposed
```

---

# 104. Adversarial Tests

A mature lineage implementation SHOULD survive:

```text
ONE SOURCE COPIED INTO 100 FILES
→ ONE ESTABLISHED ROOT, NOT 100

FILE RENAMED
→ LINEAGE SURVIVES

FILE MOVED
→ LINEAGE SURVIVES

JSON CONVERTED TO MARKDOWN
→ ORIGINAL ANCESTRY SURVIVES

SUMMARY GENERATED BY AGENT
→ SOURCE ANCESTRY SURVIVES

FIVE AGENTS READ SAME SOURCE
→ NOT FIVE INDEPENDENT SOURCES

TWO SOURCES HAVE SAME TITLE
→ DO NOT AUTO-MERGE

TWO SOURCES LOOK SIMILAR
→ DO NOT ASSERT COMMON ORIGIN

SOURCE B PREDATES CLAIMED SOURCE A
→ A→B LINEAGE MUST FAIL OR BE REEXAMINED

OLD CANON SUPERSEDED
→ OLD CANON REMAINS HISTORICALLY RESOLVABLE

ARCHIVE MOVEMENT
→ DOES NOT BREAK CURRENT DESCENDANT LINEAGE

PARENT EDGE INVALIDATED
→ ONLY DEPENDENT LINEAGE REEVALUATED

SOURCE UNKNOWN
→ UNKNOWN/GAP

TWO PLAUSIBLE PARENTS
→ COMPETING UNTIL DISCRIMINATED
```

---

# 105. Failure Recovery

```text
DETECT LINEAGE FAILURE
↓
IDENTIFY NODE OR EDGE
↓
FREEZE DEPENDENT PROMOTION IF MATERIAL
↓
PRESERVE UNAFFECTED BRANCHES
↓
ROLL BACK TO NEAREST VALID LINEAGE STATE
↓
SEARCH ALTERNATIVE EVIDENCE
↓
RESTORE EDGE
OR
KEEP UNKNOWN/GAP
↓
REVALIDATE DEPENDENTS
```

Do not repeat a failed ancestry hypothesis without changed evidence.

---

# 106. Current Canonical Gaps

The following remain `UNKNOWN/GAP` unless separately reconstructed from source artifacts:

```text
complete artifact-by-artifact AMOS historical lineage

complete version-by-version source graph

exact first introduction of every AMOS concept

complete v3.0 → v4.4 file transition history

complete migration history across historical vault structures

complete semantic lineage for all renamed concepts

complete alias ancestry

complete source-independence topology

complete external research ancestry

complete code-generation lineage

complete revision hashes for all historical canon
```

These gaps must not be filled by inference alone.

---

# 107. Promotion Gate

Promotion toward stronger canonical status requires:

```text
SOURCE INVENTORY
↓
IDENTITY NORMALIZATION
↓
DIRECT-PARENT RESOLUTION
↓
TRANSFORMATION CLASSIFICATION
↓
ANCESTRY GRAPH CONSTRUCTION
↓
DUPLICATE / COPY DETECTION
↓
INDEPENDENCE ANALYSIS
↓
VERSION RECONSTRUCTION
↓
SEMANTIC LINEAGE ANALYSIS
↓
SUPERSESSION ANALYSIS
↓
CONTRADICTION AUDIT
↓
CANON REVIEW
```

Any unresolved decision-changing lineage remains visible.

---

# 108. RSCF Node

```RSCF-NODE
node_id: AMOS-OS-SOURCE-LINEAGE
node_type: canonical_lineage_framework
domain: AMOS_OS_CANON
functional_type: ProvenanceLineage
lifecycle_stage: CanonGovernance
claim_class: AMOS_MODEL

RSCF-RELATIONS:
  - INDEXED_BY: 00_ROOT_MOC|AMOS MOC
  - INDEXED_BY: CANON_MAP
  - GOVERNED_BY: AMOS_CORE_LAWS
  - CONSTRAINED_BY: INVARIANT_REGISTRY
  - CONSTRAINED_BY: LAW_HIERARCHY
  - SUBSYSTEM_OF: CANON_PROVENANCE
  - DEFINES_LINEAGE_FOR: CANONICAL_GLOSSARY
  - DEFINES_LINEAGE_FOR: DEPRECATED_TERMS
  - DEFINES_LINEAGE_FOR: ALIASES
  - DEFINES_LINEAGE_FOR: SYMBOL_REGISTRY
  - DEFINES_LINEAGE_FOR: UNIT_REGISTRY
  - DEFINES_LINEAGE_FOR: UNIVERSAL_VARIABLE_REGISTRY
  - RELATED_TO: HML_CANON
  - RELATED_TO: PERSISTENCE_CANON
  - RELATED_TO: AUTHORITY_CANON
  - RELATED_TO: CONTROL_PLANE_CANON
  - RELATED_TO: 11_KNOWLEDGE/00_AMOS_Full_Brain_OS_Architecture
  - PRESERVES: README
```

---

# 109. Canonical Summary

AMOS source lineage follows:

```text
ORIGIN
↓
SOURCE
↓
DIRECT PARENT
↓
TRANSFORMATION
↓
DERIVATION
↓
CLAIM / MODEL / ARTIFACT
↓
DEPENDENT DESCENDANTS
↓
SUPERSESSION / CURRENT STATE
```

Core laws:

```text
SOURCE LINEAGE != TRUTH

SOURCE LINEAGE != AUTHORITY

DERIVED_FROM != CAUSED_BY

COPY != INDEPENDENT SOURCE

PARAPHRASE != INDEPENDENT SOURCE

TRANSLATION != INDEPENDENT SOURCE

FORMAT CHANGE != INDEPENDENT SOURCE

MIGRATION != NEW ORIGIN

RENAME != NEW ORIGIN

MULTIPLE DESCENDANTS != MULTIPLE ROOTS

UNKNOWN INDEPENDENCE != INDEPENDENCE

CONSOLIDATION MUST PRESERVE ALL
LOAD-BEARING PARENTS

SUPERSESSION != ERASURE

DEPRECATION != DELETION

ARCHIVE != LINEAGE LOSS

SIMILARITY != COMMON ORIGIN

TEMPORAL ORDER != CAUSATION

DERIVED CLAIMS INHERIT
LOAD-BEARING SOURCE ANCESTRY

LINEAGE REPAIR MUST NOT
INVENT MISSING HISTORY
```

Canonical objective:

```text
PRESERVE THE ROOT.

PRESERVE THE PARENTS.

PRESERVE THE EDGES.

PRESERVE TRANSFORMATIONS.

PRESERVE VERSION HISTORY.

PRESERVE SEMANTIC EVOLUTION.

PRESERVE SHARED ANCESTRY.

PRESERVE SOURCE INDEPENDENCE.

PRESERVE SUPERSESSION.

PRESERVE INVALIDATION PATHS.

PRESERVE HISTORICAL RECOVERABILITY.

DO NOT TURN COPIES INTO SOURCES.

DO NOT TURN SIMILARITY INTO ANCESTRY.

DO NOT TURN ANCESTRY INTO CAUSATION.

DO NOT TURN UNKNOWN HISTORY
INTO A CONVENIENT STORY.

WHEN THE SOURCE PATH CANNOT
BE ESTABLISHED:

UNKNOWN/GAP.
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
[[CANON_PROVENANCE]] ·
[[CANONICAL_GLOSSARY]] ·
[[DEPRECATED_TERMS]] ·
ALIASES ·
[[HML_CANON]] ·
[[PERSISTENCE_CANON]] ·
[[AUTHORITY_CANON]] ·
[[CONTROL_PLANE_CANON]] ·
[[SYMBOL_REGISTRY]] ·
[[UNIT_REGISTRY]] ·
[[UNIVERSAL_VARIABLE_REGISTRY]] ·
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
