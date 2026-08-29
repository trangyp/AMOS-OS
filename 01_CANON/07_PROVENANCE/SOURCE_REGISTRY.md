---
title: SOURCE REGISTRY
type: registry
source: 01_CANON/07_PROVENANCE
artifact_id: AMOS-OS-SOURCE-REGISTRY
canonical_name: SOURCE_REGISTRY
artifact_type: canonical_source_registry
status: SOURCE_CLAIM
conclusion_class: AMOS_MODEL
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
domain: canon
scope: AMOS_OS
authority_scope: source-identification-classification-registration-and-resolution
created: 2026-08-25
updated: 2026-08-25
tags:
- amos-os
- canon
- universe
- canon-group/meta
- canon/framework
- canon/registry
- canon/source-registry
- canon/provenance
- canon/lineage
- rscf/claim
- rscf/provenance
- rscf/state/source-claim
- topic/source-registry
- topic/source-identity
- topic/source-classification
- topic/provenance-topology
- topic/source-independence
- topic/evidence-topology
- topic/freshness
- topic/sybil-hardening
- topic/persistent-provenance
- readme
- architecture
- system-map
- neural-network
- canon-map
- amos-core-laws
- invariant-registry
- law-hierarchy
- canon-provenance
- source-lineage
- canonical-glossary
- deprecated-terms
- symbol-registry
- unit-registry
- universal-variable-registry
- hml-canon
- persistence-canon
- authority-canon
- control-plane-canon
aliases:
- AMOS Source Registry - AMOS OS Source Registry - Canon Source Registry
---

# AMOS OS Source Registry
> **Origin architect / steward:** Trang Phan
> **AMOS Core target:** `v4.4`
> **Conclusion class:** `AMOS_MODEL`
> **Status:** `SOURCE_CLAIM`
## 1. Purpose
`SOURCE_REGISTRY.md` defines the canonical AMOS OS contract for registering, identifying, classifying, resolving, and auditing sources used by canon, knowledge, RSCFs, models, agents, decisions, tests, and derived artifacts.
The registry answers:
```text
WHAT IS THE SOURCE?
WHAT TYPE OF SOURCE IS IT?
WHERE DID IT COME FROM?
WHICH EXACT REVISION WAS USED?
WHAT SCOPE DOES IT SUPPORT?
HOW FRESH IS IT?
WHAT IS ITS PROVENANCE?
IS IT INDEPENDENT?
WHAT DEPENDS ON IT?
HAS IT BEEN SUPERSEDED?
CAN IT STILL BE RELIED UPON?
```
The registry is not a list of things believed to be true.
It is a typed source-identity and provenance control structure.
rscf:
  state: DERIVED
  claim_class: EMPIRICAL
  provenance: AMOS_corpus
  scope: AMOS_general
---


# 2. Core Law

```text
REGISTERED SOURCE
!=
VERIFIED CLAIM
```

Registration establishes that AMOS knows about a source.

It does not establish that the source is:

```text
correct
complete
independent
authoritative
current
applicable
empirically validated
```

Those properties require separate evidence.

---

# 3. Source Registry Boundary

The Source Registry must remain distinct from:

```text
SOURCE REGISTRY
!=
CLAIM REGISTRY

SOURCE REGISTRY
!=
KNOWLEDGE BASE

SOURCE REGISTRY
!=
CANON

SOURCE REGISTRY
!=
AUTHORITY REGISTRY

SOURCE REGISTRY
!=
MODEL REGISTRY

SOURCE REGISTRY
!=
PROVENANCE LEDGER

SOURCE REGISTRY
!=
SOURCE LINEAGE
```

Conceptually:

```text
SOURCE_REGISTRY
=
IDENTITY + TYPE + LOCATION + METADATA
+ PROVENANCE REFERENCES
+ VALIDITY ENVELOPE
+ LIFECYCLE STATE

SOURCE_LINEAGE
=
ANCESTRY RELATIONSHIPS

CANON_PROVENANCE
=
BROADER CANON ORIGIN AND GOVERNANCE RECORD
```

---

# 4. What Counts as a Source

Within AMOS, a source may include:

```text
CANON_ARTIFACT
INTERNAL_ARTIFACT
EXTERNAL_DOCUMENT
RESEARCH_PAPER
DATASET
DATABASE
API
WEB_RESOURCE
CODE
REPOSITORY
COMMIT
TEST_RESULT
BENCHMARK
OBSERVATION
INSTRUMENT_OUTPUT
USER_INPUT
AGENT_OUTPUT
MODEL_OUTPUT
RSCF
STATE_RECORD
LEDGER_RECORD
POLICY
STANDARD
SPECIFICATION
ARCHIVED_ARTIFACT
UNKNOWN_SOURCE
```

Source type must be explicit when material.

---

# 5. Epistemic Type Firewall

Source identity and epistemic class are different dimensions.

AMOS should distinguish:

```text
SOURCE_CLAIM
OBSERVATION
DERIVED
MODEL
DECISION
UNKNOWN
```

For example:

```text
type:
  RESEARCH_PAPER

epistemic_class:
  SOURCE_CLAIM
```

is valid.

A paper is a source artifact.

Its statements do not become `VERIFIED` merely because the artifact is registered.

---

# 6. Minimum Source Record

Every consequential source SHOULD support a record equivalent to:

```yaml
source:
  source_id:
  canonical_name:
  source_type:

  identity:
    title:
    creator:
    publisher:
    uri:
    repository:
    path:

  version:
    version_id:
    revision_id:
    hash:

  temporal:
    created_at:
    published_at:
    observed_at:
    retrieved_at:
    effective_from:
    effective_until:
    last_verified_at:

  provenance:
    origin:
    lineage_ref:
    parent_sources: []
    provenance_state:

  epistemic:
    class:
    conclusion_class:
    independence_state:
    correlation_risk:

  applicability:
    scope:
    environment:
    population:
    scale:
    regime:
    measurement_method:
    assumptions: []

  lifecycle:
    status:
    supersedes: []
    superseded_by: []
    deprecated_at:
    archived_at:

  integrity:
    verification_state:
    freshness_state:
    unresolved_gaps: []

  governance:
    authority_class:
    authority_ref:

  dependencies:
    dependents: []
```

Unknown fields remain explicit.

---

# 7. Source Identity

A source should have a stable registry identity:

```text
source_id
```

`source_id` must not be silently equated with:

```text
filename
URL
title
artifact_id
claim_id
revision_id
hash
```

These are separate identifiers.

---

# 8. Identity Firewall

```text
SOURCE_ID
!=
ARTIFACT_ID

SOURCE_ID
!=
FILENAME

SOURCE_ID
!=
URI

SOURCE_ID
!=
VERSION_ID

SOURCE_ID
!=
REVISION_ID

SOURCE_ID
!=
CONTENT_HASH
```

A source can move without changing semantic source identity.

A source can also change content while retaining a location.

Therefore location alone cannot establish identity.

---

# 9. Canonical Source ID

Recommended conceptual format:

```text
SRC::<namespace>::<stable-id>
```

Example:

```text
SRC::AMOS::CORE-V4-4
```

This is a naming model only.

Actual IDs should follow the repository's governed schema once finalized.

---

# 10. Source Type

Recommended top-level classification:

```text
INTERNAL
EXTERNAL
OBSERVATIONAL
GENERATED
DERIVED
UNKNOWN
```

These may be refined into subtypes.

---

# 11. Internal Sources

Examples:

```text
AMOS_CANON
AMOS_KERNEL
AMOS_CONTROL_PLANE
AMOS_KNOWLEDGE
AMOS_MODEL
AMOS_TEST
AMOS_STATE
AMOS_ARCHIVE
AMOS_RSCF
AMOS_RESEARCH
```

Internal location does not grant authority.

```text
INTERNAL
!=
CANONICAL
```

---

# 12. External Sources

Examples:

```text
ACADEMIC_PAPER
BOOK
STANDARD
OFFICIAL_DOCUMENT
PUBLIC_DATASET
DATABASE
WEBSITE
API
REPOSITORY
VENDOR_DOCUMENTATION
THIRD_PARTY_REPORT
```

External source classification must preserve attribution.

```text
USED_BY_AMOS
!=
CREATED_BY_AMOS
```

---

# 13. Observation Sources

Observation sources may include:

```text
SENSOR_OUTPUT
TEST_RUN
EXPERIMENT_RESULT
BENCHMARK_RESULT
RUNTIME_TRACE
METRIC
LOG
MANUAL_OBSERVATION
```

Observation records should preserve the measurement environment where material.

---

# 14. Generated Sources

Generated material may include:

```text
AGENT_OUTPUT
MODEL_OUTPUT
GENERATED_REPORT
GENERATED_CODE
GENERATED_SUMMARY
SIMULATION_OUTPUT
```

Generated output must not automatically be treated as independent evidence.

```text
GENERATED
!=
INDEPENDENT
```

---

# 15. Derived Sources

Derived artifacts include:

```text
SUMMARY
PARAPHRASE
TRANSLATION
EXTRACTION
NORMALIZATION
TRANSFORMATION
CONSOLIDATION
ANALYSIS
```

Derived source records should reference their load-bearing parents.

---

# 16. Unknown Sources

If a source is known to exist but its origin cannot be established:

```yaml
source_type: UNKNOWN
provenance_state: UNKNOWN/GAP
```

Do not infer origin from:

```text
writing style
filename
folder
similarity
apparent age
repetition
```

---

# 17. Source Status

Recommended lifecycle states:

```text
CANDIDATE
REGISTERED
ACTIVE
RESTRICTED
STALE
DEPRECATED
SUPERSEDED
INVALIDATED
ARCHIVED
MISSING
UNKNOWN
```

These states describe registry lifecycle.

They do not directly encode epistemic truth.

---

# 18. Registration State

A newly discovered source may begin as:

```text
CANDIDATE
```

After minimum identity checks:

```text
REGISTERED
```

After applicability review:

```text
ACTIVE
```

where appropriate.

---

# 19. Verification State

Verification must be separate from lifecycle.

Recommended values:

```text
UNVERIFIED
IDENTITY_VERIFIED
CONTENT_VERIFIED
PROVENANCE_VERIFIED
INDEPENDENTLY_REVALIDATED
PARTIALLY_VERIFIED
CONFLICTING
UNKNOWN
```

A source may therefore be:

```yaml
status: ACTIVE
verification_state: UNVERIFIED
```

without contradiction.

---

# 20. Source Conclusion Class

Where conclusions are attached to registry records, use the weakest accurate class:

```text
VERIFIED
DERIVED
MODEL
CONDITIONAL
COMPETING
UNKNOWN/GAP
```

The registry itself should not upgrade a source merely because metadata is complete.

---

# 21. Provenance State

Recommended values:

```text
COMPLETE_FOR_SCOPE
PARTIAL
AMBIGUOUS
CONFLICTING
BROKEN
UNKNOWN/GAP
```

`COMPLETE_FOR_SCOPE` does not mean all historical ancestry is known.

It means sufficient provenance has been resolved for the declared scope.

---

# 22. Source Lineage Binding

Every source MAY bind to:

```text
lineage_ref
```

pointing to its ancestry representation.

Example:

```yaml
provenance:
  lineage_ref: SRC-LINEAGE-001
```

The Source Registry should not duplicate an entire lineage graph when a canonical lineage structure already exists.

---

# 23. Direct Parents

For derived sources:

```yaml
parent_sources:
  - SRC-A
  - SRC-B
```

Parent identity must be preserved.

If parents are unknown:

```yaml
parent_sources: []
provenance_state: UNKNOWN/GAP
```

An empty parent list must not silently mean:

```text
ORIGINAL SOURCE
```

---

# 24. Root Source State

Recommended field:

```yaml
root_state:
  known_roots: []
  unresolved_roots: true
```

This prevents accidental conversion of:

```text
earliest source found
```

into:

```text
absolute origin
```

---

# 25. Source Independence

Independence is first-class.

Recommended values:

```text
INDEPENDENT
PARTIALLY_INDEPENDENT
CORRELATED
SHARED_ANCESTRY
UNKNOWN
```

Canonical law:

```text
UNKNOWN
!=
INDEPENDENT
```

---

# 26. Independence Evidence

An `INDEPENDENT` classification should have support.

Potential evidence:

```text
distinct primary observations
separate data-generation processes
resolved ancestry showing separate roots
independent experimental collection
independent institutional records
```

Different URLs alone are insufficient.

---

# 27. Correlation Risk

Recommended levels:

```text
LOW
MEDIUM
HIGH
UNKNOWN
```

Correlation risk may arise through:

```text
shared source
shared dataset
shared model
shared institution
shared methodology
shared upstream API
common publication lineage
common generated summary
```

Correlation is contextual and should not be inferred solely from organizational similarity.

---

# 28. Provenance Sybil Hardening

The registry must resist source multiplication.

Example:

```text
ORIGINAL A
├→ ARTICLE B
├→ SUMMARY C
├→ AGENT D
└→ REPORT E
```

The registry may contain four descendant records.

But evidence aggregation must preserve:

```text
established independent roots = 1
```

unless additional independent roots are demonstrated.

---

# 29. Duplicate Sources

Duplicates should be classified as:

```text
EXACT_DUPLICATE
CONTENT_DUPLICATE
NEAR_DUPLICATE
DERIVATIVE
SHARED_ANCESTRY
POSSIBLE_DUPLICATE
DISTINCT
UNKNOWN
```

Do not collapse records merely because titles match.

---

# 30. Hash Identity

Where available:

```text
hash
```

may establish exact content identity.

But:

```text
SAME HASH
→ SAME BYTES
```

does not necessarily imply:

```text
SAME SEMANTIC ROLE
```

Different registry records may intentionally reference identical bytes under different governed contexts.

---

# 31. Version Identity

Sources may expose:

```text
version_id
revision_id
commit_id
release_id
edition
```

These fields are not interchangeable.

Missing version metadata remains:

```text
UNKNOWN/GAP
```

---

# 32. Version Rule

```text
FILENAME VERSION
!=
VERIFIED SOURCE VERSION
```

Example:

```text
document_v4.4.md
```

does not prove the document is a legitimate v4.4 descendant.

Version identity requires lineage or governed metadata.

---

# 33. Temporal Metadata

The registry SHOULD distinguish:

```text
created_at
published_at
observed_at
retrieved_at
modified_at
effective_from
effective_until
verified_at
```

Temporal semantics must not be collapsed into a generic `date`.

---

# 34. Freshness

Recommended freshness states:

```text
CURRENT
FRESH_WITHIN_SCOPE
AGING
STALE
EXPIRED
TIMELESS_BY_DEFINITION
UNKNOWN
```

Freshness is scope-dependent.

A historical law may remain relevant as historical evidence while being stale for current operational decisions.

---

# 35. Freshness Bound

A source MAY declare:

```yaml
freshness:
  valid_for:
  revalidate_after:
  last_checked:
```

where the domain supports such bounds.

No universal freshness interval should be invented.

---

# 36. Applicability Envelope

Important sources should preserve:

```text
system
population
environment
scale
time
regime
measurement method
assumptions
```

A source is not automatically portable outside this envelope.

---

# 37. Scope Firewall

```text
SOURCE VALID IN SCOPE A
```

does not establish:

```text
SOURCE VALID IN SCOPE B
```

Cross-scope use requires explicit justification or revalidation.

---

# 38. Regime Firewall

```text
SOURCE VALID UNDER R₁
```

may become stale under:

```text
R₂
```

even if the source's historical provenance remains correct.

---

# 39. Measurement Method

For empirical observations, record where material:

```text
instrument
sampling method
measurement procedure
normalization
calibration
error bounds
```

Missing measurement information may limit confidence.

---

# 40. Source Authority

Authority should be separately typed.

Possible classes:

```text
CANONICAL
GOVERNING
OFFICIAL_EXTERNAL
PRIMARY_EVIDENCE
SECONDARY
REFERENCE
INFORMATIVE
UNTRUSTED
UNKNOWN
```

Authority must be scoped.

---

# 41. Authority Firewall

```text
AUTHORITATIVE
!=
EMPIRICALLY TRUE
```

and:

```text
EMPIRICALLY STRONG
!=
GOVERNING AUTHORITY
```

Example:

A policy can be authoritative for institutional behavior without being an empirical scientific observation.

---

# 42. Canonical Source

A source is canonical only through governed canon status.

Location in:

```text
01_CANON
```

is not alone sufficient evidence of completed canon promotion.

The artifact's governance state must agree.

---

# 43. Source Trust

AMOS treats trust as:

```text
LOCAL
TYPED
SCOPED
PROVENANCE-AWARE
REGIME-AWARE
FRESHNESS-BOUNDED
```

Avoid universal:

```text
trusted = true
```

for consequential sources.

---

# 44. Trust Dimensions

A source trust profile MAY include:

```yaml
trust:
  identity:
  provenance:
  content:
  independence:
  freshness:
  scope_fit:
  authority:
```

These dimensions should not be compressed prematurely into one scalar.

---

# 45. Source Quality

Source quality and source authority are separate.

Possible quality dimensions:

```text
methodological rigor
completeness
precision
replicability
traceability
measurement quality
internal consistency
```

A high-quality source can still be outside scope.

---

# 46. Claim Binding

Sources support claims through explicit bindings.

Conceptually:

```text
SOURCE
↓ supports
CLAIM
```

A registry SHOULD allow downstream systems to identify:

```text
which claims depend on this source?
```

---

# 47. Dependency Binding

Recommended:

```yaml
dependencies:
  dependents:
    - CLAIM-001
    - RSCF-014
    - MODEL-007
```

This enables targeted invalidation.

---

# 48. Load-Bearing Sources

A source is load-bearing when removing or invalidating it can materially alter a conclusion.

Recommended marker:

```yaml
dependency_role: LOAD_BEARING
```

Other possible roles:

```text
SUPPORTING
CONTEXTUAL
ILLUSTRATIVE
DISCRIMINATING
FALSIFYING
```

---

# 49. Weakest-Premise Ceiling

If a conclusion depends on:

```text
SRC-A → strong
SRC-B → weak
SRC-C → strong
```

and B is load-bearing, derived confidence cannot silently ignore B.

Canonical principle:

```text
DERIVED CONFIDENCE
<=
WEAKEST LOAD-BEARING PREMISE
```

unless independent revalidation removes or replaces that dependency.

---

# 50. Conflicting Sources

The registry must preserve source conflict.

Example:

```text
SRC-A → CLAIM X

SRC-B → NOT CLAIM X
```

Do not overwrite one source.

Recommended relation:

```text
CONFLICTS_WITH
```

The claim layer determines whether the result is:

```text
COMPETING
CONDITIONAL
UNKNOWN/GAP
```

---

# 51. Competing Source Sets

A registry may expose:

```yaml
competing_source_sets:
  - hypothesis: H1
    sources: [SRC-A, SRC-B]

  - hypothesis: H2
    sources: [SRC-C]
```

Source count alone must not choose the winner.

Independence and quality matter.

---

# 52. Discriminating Sources

When hypotheses compete, prefer evidence that can distinguish them.

Recommended role:

```text
DISCRIMINATING
```

A new source that merely repeats shared ancestry may have low decision value.

---

# 53. Falsifying Sources

A source may challenge an existing claim.

Recommended relation:

```text
FALSIFIES
```

or:

```text
CHALLENGES
```

depending on evidentiary strength.

Contradictory evidence must remain visible.

---

# 54. Source Supersession

Sources may supersede earlier sources.

```text
SRC-A
↓ SUPERSEDED_BY
SRC-B
```

Supersession should include scope.

A new source may replace an older source only for part of its applicability envelope.

---

# 55. Partial Supersession

Example:

```text
SRC-A
├── policy X → superseded by SRC-B
└── historical record Y → still valid
```

Do not mark all of A invalid.

---

# 56. Deprecated Sources

Deprecated means:

```text
not preferred for new dependency creation
```

It does not mean:

```text
historically false
```

Deprecated sources remain resolvable for lineage.

---

# 57. Invalidated Sources

Invalidation should state why.

Recommended reasons:

```text
IDENTITY_FAILURE
PROVENANCE_FAILURE
CONTENT_ERROR
FABRICATION
SCOPE_FAILURE
REGIME_FAILURE
MEASUREMENT_FAILURE
SUPERSESSION
CORRUPTION
UNKNOWN
```

---

# 58. Source Invalidation Propagation

If:

```text
SRC-A
↓
CLAIM-B
↓
MODEL-C
```

and A fails, evaluate only dependent descendants.

Do not invalidate unrelated registry entries.

---

# 59. Archive State

Archived sources remain historical nodes.

```text
ARCHIVED
!=
ERASED
```

Their registry entries should preserve enough information to reconstruct lineage.

---

# 60. Missing Sources

A source referenced by lineage but unavailable should be represented explicitly:

```yaml
status: MISSING
availability: UNAVAILABLE
```

Do not delete its identity merely because content cannot currently be retrieved.

---

# 61. Source Tombstones

A removed source MAY retain:

```yaml
source_tombstone:
  source_id:
  former_location:
  former_hash:
  removal_date:
  removal_reason:
  superseded_by:
  lineage_ref:
```

This preserves recoverability.

---

# 62. External Source Licensing

Where material, external source records SHOULD preserve:

```text
license
copyright status
reuse constraints
citation requirements
unknown IP state
```

Missing license information should remain explicit.

---

# 63. Proprietary Sources

A source may be:

```text
PROPRIETARY
INTERNAL_RESTRICTED
PUBLIC
LICENSED
UNKNOWN
```

Source registration does not imply permission to expose raw contents.

---

# 64. IP Firewall

```text
SOURCE ACCESS
!=
SOURCE REDISTRIBUTION AUTHORITY
```

AMOS may reason from a proprietary source while restricting raw export.

---

# 65. Sensitive Sources

A registry may flag:

```text
PRIVATE
CONFIDENTIAL
RESTRICTED
SECRET
PERSONAL_DATA
SECURITY_SENSITIVE
```

Actual classification semantics must be governed by the security layer.

---

# 66. Source Accessibility

Recommended availability states:

```text
AVAILABLE
PARTIALLY_AVAILABLE
RESTRICTED
OFFLINE
MISSING
UNKNOWN
```

Availability is not epistemic quality.

---

# 67. Retrieval Reference

Source records MAY preserve retrieval information:

```yaml
retrieval:
  uri:
  local_ref:
  repository_ref:
  content_address:
```

Do not rely exclusively on unstable paths.

---

# 68. Content Addressing

Where hashes are available:

```text
SOURCE_ID
→ REVISION
→ HASH
```

provides stronger identity resolution than filename alone.

Conceptually:

```text
stable semantic identity
+
immutable content identity
```

should remain distinct.

---

# 69. Canon Source Registration

Canon source registration SHOULD preserve:

```text
artifact identity
canonical name
revision
provenance
governance state
supersession state
authority scope
```

No source becomes canon merely by being added to this registry.

---

# 70. Research Source Registration

Research sources SHOULD preserve:

```text
authors
title
publication
date
identifier
version
retrieval date
study scope
methodology metadata
```

where available and decision-relevant.

---

# 71. Dataset Registration

Datasets SHOULD preserve where material:

```text
dataset identity
version
collection period
population
sampling method
schema
license
transformations
known limitations
```

---

# 72. API Source Registration

API sources SHOULD preserve:

```text
provider
endpoint family
API version
retrieval time
query/input
response identity
environment
```

A current API response is an observation at a time, not an eternal fact.

---

# 73. Code Source Registration

Code sources MAY preserve:

```text
repository
branch
commit
path
hash
runtime environment
dependencies
license
```

Repository head is not sufficient for reproducible lineage if the underlying revision changes.

---

# 74. Test Evidence Registration

Test sources SHOULD preserve:

```text
test ID
system version
environment
inputs
expected result
actual result
timestamp
runner
```

A passing test supports only the property tested under that environment.

---

# 75. Benchmark Registration

Benchmark sources SHOULD preserve:

```text
benchmark identity
version
dataset
hardware
software
configuration
measurement method
run date
```

Canonical firewall:

```text
BENCHMARK SUCCESS
!=
UNIVERSAL VALIDITY
```

and:

```text
REPORTED LATENCY
!=
HARDWARE-INDEPENDENT LATENCY
```

---

# 76. Agent Output Registration

When an agent output becomes persistent evidence, record where material:

```text
agent identity
agent configuration/version
input sources
execution time
output
source ancestry
```

Agent generation does not erase upstream provenance.

---

# 77. Model Output Registration

Model outputs SHOULD preserve:

```text
model identity
model version
inputs
prompt/configuration where governed
source dependencies
timestamp
environment
```

Canonical law:

```text
MODEL OUTPUT
!=
PRIMARY OBSERVATION
```

unless the output itself is the object being observed.

---

# 78. User Input Sources

User-provided information may be registered as:

```text
USER_INPUT
```

when it becomes a load-bearing source.

Its epistemic class remains appropriate to what it represents.

User assertion alone does not automatically become verified empirical evidence.

---

# 79. RSCF Source Registration

RSCFs may themselves become sources for downstream reasoning.

A registry binding SHOULD preserve:

```text
RSCF ID
claim class
dependencies
provenance
scope
freshness
invalidation state
```

---

# 80. H/M/L Integration

Source retrieval follows the AMOS fractal path:

```text
BOOTSTRAP
↓
H DOMAIN
↓
M SUBSYSTEM
↓
L DETAIL
↓
RAW SOURCE
```

Raw source content defaults conceptually to:

```text
DO_NOT_LOAD_UNLESS_REQUIRED
```

The registry enables source discovery without requiring full content loading.

---

# 81. Smallest Sufficient Retrieval

The source registry supports:

```text
SOURCE METADATA FIRST
↓
RELEVANT LINEAGE
↓
RELEVANT CLAIM
↓
RAW SOURCE ONLY IF NEEDED
```

This reduces unnecessary retrieval while preserving integrity.

---

# 82. Escalation Conditions

Raw source inspection should escalate when:

```text
claim materially depends on exact wording
provenance is ambiguous
sources conflict
independence is uncertain
scope is unclear
freshness is questionable
transformation fidelity is uncertain
high-stakes action depends on the result
```

---

# 83. Source Registry Query Model

Conceptually, the registry should support queries such as:

```text
GET SOURCE BY ID

GET SOURCE BY HASH

GET SOURCE BY ARTIFACT

GET SOURCES FOR CLAIM

GET SOURCES FOR RSCF

GET SOURCES BY TYPE

GET SOURCES BY DOMAIN

GET SOURCES BY STATUS

GET SOURCES BY FRESHNESS

GET SOURCES BY PROVENANCE STATE

GET SOURCES SHARING ANCESTRY

GET INDEPENDENT ROOT SOURCES

GET SUPERSEDED SOURCES

GET SOURCES WITH UNKNOWN LINEAGE

GET DEPENDENTS OF SOURCE
```

---

# 84. Registry Indexes

Potential logical indexes:

```text
BY_SOURCE_ID
BY_ARTIFACT_ID
BY_HASH
BY_TYPE
BY_DOMAIN
BY_STATUS
BY_AUTHORITY
BY_PROVENANCE
BY_ROOT
BY_VERSION
BY_SCOPE
BY_REGIME
BY_FRESHNESS
BY_DEPENDENT
BY_SUPERSESSION
```

These are architectural requirements, not claims about current physical implementation.

---

# 85. Registration Workflow

```text
DISCOVER SOURCE
↓
ASSIGN CANDIDATE IDENTITY
↓
CLASSIFY TYPE
↓
CAPTURE LOCATION
↓
CAPTURE VERSION
↓
CAPTURE TEMPORAL METADATA
↓
RESOLVE PROVENANCE
↓
CHECK DUPLICATES
↓
CHECK SHARED ANCESTRY
↓
ASSESS SCOPE
↓
ASSESS FRESHNESS
↓
ASSESS AUTHORITY
↓
REGISTER
```

---

# 86. Promotion Workflow

```text
CANDIDATE
↓
IDENTITY CHECK
↓
PROVENANCE CHECK
↓
SCOPE CHECK
↓
INDEPENDENCE CHECK
↓
FRESHNESS CHECK
↓
CONFLICT CHECK
↓
REGISTERED / ACTIVE
```

Promotion should stop when a decision-changing gap remains unresolved.

---

# 87. Source Update Workflow

```text
NEW REVISION DETECTED
↓
DO NOT OVERWRITE HISTORY
↓
REGISTER REVISION
↓
LINK VERSION LINEAGE
↓
COMPARE MATERIAL CHANGES
↓
REVALIDATE DEPENDENTS IF REQUIRED
↓
UPDATE CURRENT POINTER
```

---

# 88. Mutable Source Firewall

For mutable URLs or files:

```text
SAME LOCATION
!=
SAME CONTENT
```

The registry should capture revision or retrieval identity where possible.

---

# 89. Replacement Firewall

Replacing content at the same path must not silently rewrite provenance history.

```text
PATH STABILITY
!=
CONTENT STABILITY
```

---

# 90. Source Conflict Workflow

```text
CONFLICT DETECTED
↓
PRESERVE BOTH SOURCES
↓
CHECK IDENTITY
↓
CHECK VERSION
↓
CHECK SCOPE
↓
CHECK REGIME
↓
CHECK INDEPENDENCE
↓
CHECK FRESHNESS
↓
SEARCH DISCRIMINATING EVIDENCE
↓
RESOLVE
OR
KEEP COMPETING
```

---

# 91. Source Failure Recovery

```text
SOURCE FAILURE
↓
IDENTIFY FAILURE TYPE
↓
IDENTIFY DEPENDENTS
↓
FREEZE UNSAFE PROMOTION
↓
PRESERVE UNAFFECTED BRANCHES
↓
SEARCH ALTERNATIVE SOURCE
↓
REVALIDATE DEPENDENTS
↓
RESTORE
OR
UNKNOWN/GAP
```

---

# 92. Source Registry Invariants

```text
SRC-001
REGISTERED != VERIFIED

SRC-002
REGISTERED != CANONICAL

SRC-003
SOURCE != CLAIM

SRC-004
SOURCE != AUTHORITY

SRC-005
SOURCE_ID != FILENAME

SRC-006
SOURCE_ID != URL

SRC-007
SOURCE_ID != HASH

SRC-008
SOURCE_ID != VERSION_ID

SRC-009
LOCATION != IDENTITY

SRC-010
SAME LOCATION != SAME CONTENT

SRC-011
DIFFERENT LOCATION != DIFFERENT ORIGIN

SRC-012
COPY != INDEPENDENT SOURCE

SRC-013
PARAPHRASE != INDEPENDENT SOURCE

SRC-014
TRANSLATION != INDEPENDENT SOURCE

SRC-015
GENERATED OUTPUT != INDEPENDENT CONFIRMATION

SRC-016
MULTIPLE DESCENDANTS != MULTIPLE ROOT SOURCES

SRC-017
UNKNOWN INDEPENDENCE != INDEPENDENCE

SRC-018
AUTHORITY != EMPIRICAL VALIDITY

SRC-019
FRESHNESS != PROVENANCE VALIDITY

SRC-020
PROVENANCE VALIDITY != CURRENT APPLICABILITY

SRC-021
SCOPE MUST NOT SILENTLY EXPAND

SRC-022
SUPERSESSION != DELETION

SRC-023
ARCHIVE != PROVENANCE LOSS

SRC-024
INVALIDATION PROPAGATES ONLY THROUGH DEPENDENCIES

SRC-025
MISSING METADATA REMAINS UNKNOWN/GAP
```

---

# 93. Minimum Integrity Gate

Before a source is used as load-bearing evidence:

```text
[ ] source identity resolved sufficiently
[ ] source type known or explicitly UNKNOWN
[ ] exact revision identified where material
[ ] provenance state assessed
[ ] duplicate/shared ancestry checked
[ ] independence assessed
[ ] scope compatibility checked
[ ] regime compatibility checked
[ ] freshness checked
[ ] authority type understood
[ ] contradictions checked
[ ] downstream role identified
[ ] unresolved material gaps exposed
```

---

# 94. High-Stakes Gate

For legal, financial, health, safety, institutional, security, or irreversible decisions, increase validation.

At minimum consider:

```text
PRIMARY SOURCE ACCESS
INDEPENDENT CONFIRMATION
CURRENT REVISION
CURRENT REGIME
SCOPE FIT
PROVENANCE INDEPENDENCE
CONTRADICTION SEARCH
QUALIFIED HUMAN REVIEW
```

where applicable.

---

# 95. Adversarial Validation

For consequential source sets, challenge the apparent evidence structure.

Ask:

```text
ARE THESE REALLY DIFFERENT SOURCES?

DO THEY SHARE AN UPSTREAM ROOT?

IS ONE COPYING ANOTHER?

IS THE SOURCE STALE?

IS THE SOURCE OUT OF SCOPE?

HAS IT BEEN SUPERSEDED?

IS THE VERSION CORRECT?

IS AUTHORITY BEING CONFUSED WITH TRUTH?

IS REPETITION BEING CONFUSED WITH CONFIRMATION?

IS AN AGENT OUTPUT BEING COUNTED AS PRIMARY EVIDENCE?

IS A MODEL OUTPUT BEING COUNTED AS AN OBSERVATION?
```

---

# 96. Adversarial Tests

A mature registry SHOULD survive:

```text
100 COPIES OF ONE DOCUMENT
→ 100 ARTIFACTS
→ 1 ESTABLISHED SOURCE ROOT

ONE URL CHANGES CONTENT
→ NEW REVISION DETECTED

FILE RENAMED
→ SOURCE IDENTITY PRESERVED

FILE MOVED
→ SOURCE IDENTITY PRESERVED

AGENT SUMMARIZES PAPER
→ PAPER REMAINS UPSTREAM SOURCE

FIVE AGENTS SUMMARIZE SAME PAPER
→ NOT FIVE INDEPENDENT SOURCES

TWO SOURCES SHARE DATASET
→ CORRELATION RISK VISIBLE

OLD SOURCE SUPERSEDED
→ HISTORICAL SOURCE REMAINS RESOLVABLE

SOURCE OUTSIDE SCOPE
→ NO SILENT GENERALIZATION

SOURCE STALE
→ CURRENT CLAIM REVALIDATED

UNKNOWN ROOT
→ UNKNOWN/GAP

CONFLICTING SOURCES
→ COMPETING PRESERVED

MISSING SOURCE
→ MISSING, NOT DELETED

HIGH AUTHORITY + WEAK EMPIRICAL BASIS
→ AUTHORITY AND EVIDENCE REMAIN SEPARATE
```

---

# 97. Registry Integrity Metrics

Potential metrics include:

```text
registered_source_count
sources_with_verified_identity
sources_with_known_revision
sources_with_known_hash
sources_with_complete_for_scope_provenance
sources_with_unknown_lineage
sources_with_unknown_independence
sources_with_high_correlation_risk
stale_sources
superseded_sources
missing_sources
conflicting_sources
load_bearing_sources_with_gaps
```

Metrics describe registry condition.

They do not establish truth.

---

# 98. Source Registry and Canon Provenance

Relationship:

```text
SOURCE_REGISTRY
↓ identifies source objects

SOURCE_LINEAGE
↓ connects ancestry

CANON_PROVENANCE
↓ records canon origin and governance

CANON
↓ declares governed canonical state
```

No layer should silently absorb the responsibilities of another.

---

# 99. Source Registry and Knowledge

```text
SOURCE
↓
EVIDENCE
↓
CLAIM
↓
RSCF
↓
KNOWLEDGE
```

The registry anchors the source side of this chain.

It does not determine final claim confidence by itself.

---

# 100. Source Registry and State

Registry state may be persisted through governed state infrastructure.

Conceptually:

```text
REGISTRY RECORD
↓
PERSISTENT STATE
↓
REVISION
↓
AUDITABLE CHANGE
```

Exact storage implementation belongs outside canon unless separately specified.

---

# 101. Source Registry and Control Plane

The control plane may govern:

```text
source promotion
source restriction
source invalidation
source supersession
authority assignment
commit of registry changes
```

But:

```text
CONTROL PLANE
!=
SOURCE
```

---

# 102. Source Registry and Runtime

Runtime may:

```text
query
resolve
retrieve
cache
validate
route
```

source records.

Runtime should not silently redefine canonical source identity.

---

# 103. Source Registry and Agents

Agents may propose:

```text
new sources
new metadata
new relationships
new conflicts
new invalidations
```

Canonical law:

```text
AGENT PROPOSAL
!=
REGISTRY COMMIT
```

where governance requires controlled mutation.

---

# 104. Source Registry and Skills

Skills may implement procedures such as:

```text
source discovery
citation extraction
duplicate detection
freshness checking
lineage reconstruction
source comparison
```

A skill performs procedure.

It does not acquire authority merely by execution.

---

# 105. Source Registry and Tools

Tools may retrieve source data.

```text
TOOL
!=
SOURCE AUTHORITY
```

A search engine, API, connector, or crawler is an access mechanism unless it is itself the data-generating source.

---

# 106. Source Registry and Security

Security controls should determine:

```text
who may read
who may register
who may modify
who may deprecate
who may invalidate
who may expose raw content
```

Capability to edit the registry does not imply authority to redefine canon.

---

# 107. Source Registry and Observability

Registry operations SHOULD eventually be observable through events such as:

```text
SOURCE_DISCOVERED
SOURCE_REGISTERED
SOURCE_UPDATED
SOURCE_REVALIDATED
SOURCE_CONFLICT_DETECTED
SOURCE_DEPRECATED
SOURCE_SUPERSEDED
SOURCE_INVALIDATED
SOURCE_MISSING
SOURCE_RESTORED
```

where implementation supports them.

---

# 108. Source Registry and Tests

Tests SHOULD eventually verify:

```text
stable identity
duplicate handling
version handling
lineage binding
supersession
scope enforcement
freshness handling
independence handling
missing-source handling
invalidation propagation
```

---

# 109. Canonical Registry Template

```yaml
source_record:

  source_id:
  canonical_name:

  classification:
    source_type:
    epistemic_type:
    authority_class:

  identity:
    title:
    creator:
    publisher:
    artifact_id:
    uri:
    repository:
    path:

  version:
    version_id:
    revision_id:
    commit_id:
    hash:

  temporal:
    created_at:
    published_at:
    observed_at:
    retrieved_at:
    modified_at:
    effective_from:
    effective_until:
    last_verified_at:

  provenance:
    origin:
    lineage_ref:
    direct_parents: []
    known_roots: []
    unresolved_roots:
    provenance_state:

  independence:
    state:
    correlation_risk:
    shared_ancestry_with: []

  applicability:
    system:
    population:
    environment:
    scale:
    time:
    regime:
    measurement_method:
    assumptions: []

  lifecycle:
    status:
    supersedes: []
    superseded_by: []
    deprecated_at:
    archived_at:

  integrity:
    verification_state:
    freshness_state:
    conclusion_class:
    unresolved_gaps: []

  access:
    availability:
    sensitivity:
    license:
    ip_status:

  dependency:
    dependents: []
    dependency_role:

  governance:
    authority_ref:
    registered_by:
    registered_at:
    last_reviewed_by:
```

---

# 110. Current Canonical Gaps

The following remain `UNKNOWN/GAP` until separately populated and validated:

```text
complete AMOS source inventory

complete source IDs

complete historical source hashes

complete revision identities

complete source ancestry

complete independent-root topology

complete source correlation map

complete supersession graph

complete external research registry

complete dataset registry

complete benchmark source registry

complete code-source registry

complete source licensing inventory

complete freshness policy by source type

complete authority classification

complete dependency bindings

complete source-level access policy
```

This framework must not invent those records.

---

# 111. Promotion Gate

This artifact defines the registry contract.

Actual source records should be promoted only through:

```text
DISCOVERY
→ IDENTITY
→ CLASSIFICATION
→ PROVENANCE
→ LINEAGE
→ INDEPENDENCE
→ SCOPE
→ FRESHNESS
→ CONFLICT CHECK
→ GOVERNED REGISTRATION
```

If a critical field cannot be resolved:

```text
UNKNOWN/GAP
```

remains the correct state.

---

# 112. RSCF Node

```RSCF-NODE
node_id: AMOS-OS-SOURCE-REGISTRY
node_type: canonical_source_registry
domain: AMOS_OS_CANON
functional_type: SourceRegistry
lifecycle_stage: CanonGovernance
claim_class: AMOS_MODEL

RSCF-RELATIONS:
  - INDEXED_BY: 00_ROOT_MOC|AMOS MOC
  - INDEXED_BY: CANON_MAP
  - GOVERNED_BY: AMOS_CORE_LAWS
  - CONSTRAINED_BY: INVARIANT_REGISTRY
  - CONSTRAINED_BY: LAW_HIERARCHY
  - PROVENANCE_GOVERNED_BY: CANON_PROVENANCE
  - LINEAGE_GOVERNED_BY: SOURCE_LINEAGE
  - REGISTERS_SOURCES_FOR: CANONICAL_GLOSSARY
  - REGISTERS_SOURCES_FOR: SYMBOL_REGISTRY
  - REGISTERS_SOURCES_FOR: UNIT_REGISTRY
  - REGISTERS_SOURCES_FOR: UNIVERSAL_VARIABLE_REGISTRY
  - SUPPORTS: HML_CANON
  - SUPPORTS: PERSISTENCE_CANON
  - SUPPORTS: AUTHORITY_CANON
  - SUPPORTS: CONTROL_PLANE_CANON
  - SUPPORTS: 11_KNOWLEDGE/00_AMOS_Full_Brain_OS_Architecture
  - PRESERVES_HISTORY_WITH: README
```

---

# 113. Canonical Summary

```text
DISCOVER
↓
IDENTIFY
↓
CLASSIFY
↓
VERSION
↓
PROVENANCE
↓
LINEAGE
↓
INDEPENDENCE
↓
SCOPE
↓
FRESHNESS
↓
AUTHORITY TYPE
↓
REGISTER
↓
BIND DEPENDENCIES
↓
MONITOR
↓
REVALIDATE / SUPERSEDE / INVALIDATE
```

Core laws:

```text
REGISTERED != VERIFIED

REGISTERED != CANONICAL

SOURCE != CLAIM

SOURCE != AUTHORITY

SOURCE_ID != FILENAME

SOURCE_ID != URL

LOCATION != IDENTITY

SAME LOCATION != SAME CONTENT

COPY != INDEPENDENT SOURCE

PARAPHRASE != INDEPENDENT SOURCE

TRANSLATION != INDEPENDENT SOURCE

AGENT OUTPUT != INDEPENDENT CONFIRMATION

MODEL OUTPUT != PRIMARY OBSERVATION

MULTIPLE DESCENDANTS != MULTIPLE ROOTS

UNKNOWN INDEPENDENCE != INDEPENDENCE

AUTHORITY != EMPIRICAL VALIDITY

FRESHNESS != PROVENANCE

PROVENANCE != CURRENT APPLICABILITY

SCOPE MUST NOT SILENTLY EXPAND

SUPERSESSION != DELETION

ARCHIVE != LINEAGE LOSS

MISSING SOURCE != NONEXISTENT SOURCE

TOOL != SOURCE AUTHORITY

AGENT PROPOSAL != REGISTRY COMMIT

UNKNOWN/GAP != PASS
```

Canonical objective:

```text
KNOW WHAT THE SOURCE IS.

KNOW WHICH REVISION WAS USED.

KNOW WHERE IT CAME FROM.

KNOW WHAT IT CAN SUPPORT.

KNOW WHETHER IT IS CURRENT.

KNOW WHETHER IT IS INDEPENDENT.

KNOW WHAT SHARES ITS ANCESTRY.

KNOW WHAT DEPENDS ON IT.

KNOW WHETHER IT WAS SUPERSEDED.

KNOW WHEN ITS VALIDITY ENDS.

DO NOT COUNT COPIES AS CONFIRMATION.

DO NOT COUNT AGENTS AS SOURCES
WHEN THEY SHARE THE SAME ROOT.

DO NOT CONFUSE AUTHORITY WITH TRUTH.

DO NOT CONFUSE REGISTRATION
WITH VERIFICATION.

DO NOT HIDE CONFLICT.

DO NOT INVENT MISSING PROVENANCE.

WHEN SOURCE IDENTITY,
ANCESTRY,
SCOPE,
OR VALIDITY
CANNOT BE ESTABLISHED:

UNKNOWN/GAP.
```

## Related

README ·
[[00_ROOT_MOC]]|[[AMOS MOC]] ·
[[ARCHITECTURE]] ·
[[SYSTEM_MAP]] ·
NAMING_STANDARD ·
[[NEURAL_NETWORK]] ·
[[CANON_MAP]] ·
[[AMOS_CORE_LAWS]] ·
[[INVARIANT_REGISTRY]] ·
[[LAW_HIERARCHY]] ·
[[CANON_PROVENANCE]] ·
[[SOURCE_LINEAGE]] ·
[[CANONICAL_GLOSSARY]] ·
[[DEPRECATED_TERMS]] ·
ALIASES ·
[[SYMBOL_REGISTRY]] ·
[[UNIT_REGISTRY]] ·
[[UNIVERSAL_VARIABLE_REGISTRY]] ·
[[HML_CANON]] ·
[[PERSISTENCE_CANON]] ·
[[AUTHORITY_CANON]] ·
[[CONTROL_PLANE_CANON]] ·
11_KNOWLEDGE/00_AMOS_Full_Brain_OS_Architecture ·
README ·
README

```text
```

---

[[00_ROOT_MOC]]|[[AMOS MOC]]

---
**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]]

---
**MOC:** [[07_PROVENANCE_MOC]]

