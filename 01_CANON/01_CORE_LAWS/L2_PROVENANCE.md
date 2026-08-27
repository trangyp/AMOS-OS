---
title: L2 PROVENANCE
type: note
source: "01_CANON/01_CORE_LAWS"
rscf:
  state: SOURCE_CLAIM
  class: STRUCTURAL
  provenance:
    - internal
  freshness: EVERGREEN
  falsifiers: []
tags: [note, 01-core-laws]
canon-group: canon/core-laws
---

---title: "AMOS Core Laws — L2 Provenance Laws"
type: document
tags: [note]
---


# L2 Provenance Laws

## 0. Status and Governing Boundary

`L2_PROVENANCE.md` defines the AMOS OS **L2 Provenance Law family**.

It replaces the previous structural placeholder with a substantive provenance contract.

The artifact combines two explicitly separated classes of material:

1. **SOURCE-DERIVED AMOS lineage**
   - provenance-topology hardening exists in the AMOS_CORE lineage;
   - AMOS_CORE v3.7.1 explicitly introduces hardened provenance topology;
   - exact-root content fingerprints may collapse provenance aliases representing the same root.

2. **AMOS_MODEL formalization**
   - generalized provenance tensors;
   - provenance graphs;
   - independence matrices;
   - confidence-ceiling equations;
   - admission protocols;
   - invalidation protocols;
   - repair workflows;
   - H/M/L propagation rules.

The second category is a governed formalization and MUST NOT be silently promoted into recovered historical canon.

Origin architect / steward:

**Trang Phan**

---

# 1. Hard Boundaries

```text
SOURCE != CLAIM

CLAIM != EVIDENCE

EVIDENCE != PROVENANCE

PROVENANCE != TRUTH

IDENTITY != AUTHORITY

AUTHORITY != VALIDITY

ALIAS != INDEPENDENT_SOURCE

COPY != CORROBORATION

PARAPHRASE != INDEPENDENCE

REPETITION != INDEPENDENCE

MULTIPLE_PATHS != MULTIPLE_ROOTS

MULTIPLE_URLS != MULTIPLE_ORIGINS

FINGERPRINT_MATCH != UNIVERSAL_SEMANTIC_EQUIVALENCE

ANCESTRY_OVERLAP != INDEPENDENCE

UNKNOWN_ANCESTRY != INDEPENDENT

SOURCE_COUNT != EFFECTIVE_SOURCE_COUNT

DOCUMENTED != VERIFIED

CANONICAL != EMPIRICALLY_TRUE

CAPABILITY != AUTHORITY

PROPOSAL != COMMIT

UNKNOWN/GAP != PASS
````

---

# 2. Purpose

L2 governs the origin, ancestry, transformation history, identity, independence, version lineage, trust boundaries, supersession, revocation, and downstream propagation of information used by AMOS.

The central question is:

> **Where did this information actually come from, what happened to it before it reached the current claim, and how many genuinely independent evidentiary roots support it?**

L2 exists because evidence without provenance can create false confidence.

Consider:

```text
ROOT S
  │
  ├── article A
  │      ↓
  │   summary B
  │      ↓
  │   model answer C
  │
  └── copied article D
         ↓
      report E
```

A naive system may count:

```text
A + B + C + D + E = 5 sources
```

AMOS must instead ask whether these objects ultimately derive from the same load-bearing root.

If they do:

```text
effective independent roots ≈ 1
```

for the information inherited from that root.

---

# 3. Relationship to L0 and L1

The core-law dependency chain is:

```text
L0 INTEGRITY
      ↓
L1 EPISTEMIC
      ↓
L2 PROVENANCE
```

L0 requires structural distinctions to remain intact.

L1 determines the epistemic status of claims.

L2 determines whether the evidence supporting those claims has valid, inspectable, sufficiently independent ancestry.

Conceptually:

```text
CLAIM
  ↓
EVIDENCE
  ↓
SOURCE
  ↓
ROOT
  ↓
ANCESTRY
  ↓
TRANSFORMATIONS
  ↓
INDEPENDENCE
  ↓
TRUST / CONFIDENCE CEILING
```

L2 therefore constrains downstream epistemic confidence.

---

# 4. Core Provenance Principle

The governing principle is:

> **Evidence must carry enough recoverable lineage to distinguish genuine independent support from aliases, copies, descendants, transformations, correlated origins, and unknown ancestry.**

AMOS MUST NOT infer independence merely because evidence appears in separate files, URLs, agents, repositories, memories, reports, or outputs.

---

# 5. Provenance Object

The proposed normalized provenance object is:

```yaml
ProvenanceObject:

  provenance_id: string

  object_id: string

  object_type: null

  source_id: null

  root_id: null

  parent_ids: []

  ancestor_ids: []

  fingerprint: null

  fingerprint_method: null

  transformation_history: []

  creator_or_observer: null

  acquisition_method: null

  source_version: null

  source_time: null

  observation_time: null

  ingestion_time: null

  scope: {}

  regime: {}

  status: null

  trust_state: null

  independence_class: null

  supersedes: []

  superseded_by: []

  revoked_by: []

  downstream_dependents: []

  evidence_refs: []

  uncertainty: {}

  confidence_ceiling: null
```

This schema is an `AMOS_MODEL` formalization.

---

# 6. Source-Derived Provenance Tensor Anchor

AMOS provenance may be represented conceptually as:

```text
P[source, root, fingerprint, parent, time, regime, status]
```

where:

```text
source
```

identifies the immediate source;

```text
root
```

identifies the resolved origin family;

```text
fingerprint
```

supports identity / alias analysis;

```text
parent
```

records immediate ancestry;

```text
time
```

binds provenance temporally;

```text
regime
```

binds applicability;

and:

```text
status
```

records current provenance validity.

The generalized tensor is an `AMOS_MODEL` representation of the provenance architecture.

---

# 7. L2-P001 — Every Material Evidence Object Should Have Provenance

For consequential reasoning:

```text
Evidence(E)
→
Provenance(E)
```

should be recoverable.

A provenance record SHOULD identify, where applicable:

```text
origin

immediate source

parent

root

version

time

transformation

scope

regime

status
```

Missing provenance does not necessarily make evidence false.

It lowers what AMOS may safely infer from it.

---

# 8. L2-P002 — Immediate Source and Root Source Must Remain Distinct

Suppose:

```text
ROOT R
 ↓
REPORT A
 ↓
SUMMARY B
```

For `B`:

```text
immediate_source(B) = A
```

while:

```text
root_source(B) = R
```

These identities must not be collapsed.

---

# 9. L2-P003 — Source Identity Is Not Root Identity

Two objects may have different source identifiers while sharing the same root.

```text
source(A) != source(B)
```

does not imply:

```text
root(A) != root(B)
```

This is a fundamental anti-Sybil rule.

---

# 10. L2-P004 — Exact-Root Fingerprint Collapse

Where fingerprint assumptions are valid, exact-root equivalence may be represented:

```text
SameRoot(i,j)
=
Fingerprint(root_i) == Fingerprint(root_j)
```

If true:

```text
independence(i,j) = SAME_ROOT
```

for claims inherited from that root.

This is a source-anchored AMOS provenance-hardening principle.

---

# 11. L2-P005 — Fingerprint Equality Has Limited Meaning

Fingerprint equality establishes identity under the applicable fingerprint method.

It does NOT establish:

```text
all interpretations are identical

all metadata are identical

all later transformations are identical

all contextual meanings are identical

all downstream claims are equivalent
```

Therefore:

```text
FINGERPRINT_EQUALITY
```

is an identity rule, not a universal semantic-equivalence rule.

---

# 12. L2-P006 — Different Fingerprints Do Not Automatically Prove Independent Origins

```text
Fingerprint(A) != Fingerprint(B)
```

does not prove:

```text
Independent(A,B)
```

because:

```text
B may paraphrase A

B may transform A

A and B may derive from hidden root R

A and B may share a dataset

A and B may share a benchmark

A and B may share an upstream institution
```

Fingerprint inequality is therefore insufficient for provenance independence.

---

# 13. L2-P007 — Alias Collapse

If:

```text
Alias_A → Root_R
Alias_B → Root_R
Alias_C → Root_R
```

then for root-dependent claims:

```text
{Alias_A, Alias_B, Alias_C}
```

constitutes one provenance family.

Conceptually:

```text
EffectiveRoots = 1
```

not `3`.

---

# 14. L2-P008 — Paraphrase Does Not Create Independence

If:

```text
B = paraphrase(A)
```

then:

```text
B
```

does not become an independent evidentiary root merely because wording changed.

The transformation edge must remain visible:

```text
A
 └── PARAPHRASED_AS → B
```

---

# 15. L2-P009 — Summarization Does Not Create Independence

```text
SUMMARY(S)
```

inherits provenance from `S`.

Therefore:

```text
root(SUMMARY(S))
=
root(S)
```

unless the summary independently incorporates additional evidence.

---

# 16. L2-P010 — Translation Does Not Create Independence

If:

```text
B = TRANSLATE(A)
```

then `B` remains provenance-dependent on `A`.

Translation may introduce semantic uncertainty, but not independent confirmation.

---

# 17. L2-P011 — Format Conversion Does Not Create Independence

Conversions such as:

```text
PDF → TXT

DOCX → Markdown

JSON → YAML

repository → archive

web page → screenshot
```

do not create new evidentiary roots.

---

# 18. L2-P012 — Model Restatement Does Not Create Independence

If a model generates a statement based entirely on source `S`:

```text
S
 ↓
MODEL
 ↓
OUTPUT O
```

then `O` does not independently corroborate `S`.

The model output is a descendant.

---

# 19. L2-P013 — Memory Storage Does Not Create Independence

If:

```text
SOURCE S
 ↓
MEMORY M
```

then retrieving `M` later does not create a second independent source.

```text
root(M) = root(S)
```

for the inherited claim.

---

# 20. L2-P014 — Canon Storage Does Not Erase Provenance

Admission into AMOS canon must not erase source ancestry.

Canonicalization may add:

```text
authority status

version

approval

scope

governance metadata
```

but must preserve the lineage of the admitted material.

---

# 21. L2-P015 — Derived Claims Preserve Ancestry

Suppose:

```text
E1 ← R1

E2 ← R2

C = derive(E1,E2)
```

Then:

```text
ancestry(C)
⊇
{R1,R2}
```

The derived claim cannot legitimately present itself as originless.

---

# 22. L2-P016 — Transformation History Must Be Recoverable

Where material, provenance SHOULD preserve transformations such as:

```text
COPY

EXTRACT

PARSE

OCR

TRANSLATE

SUMMARIZE

NORMALIZE

FILTER

AGGREGATE

JOIN

DERIVE

COMPRESS

REWRITE

ANNOTATE

REDACT

CANONICALIZE
```

The transformation sequence may affect interpretation and trust.

---

# 23. L2-P017 — Transformation May Introduce New Uncertainty

If:

```text
A
 ↓ transformation T
B
```

then:

```text
uncertainty(B)
```

may be greater than:

```text
uncertainty(A)
```

where `T` can lose information.

Examples:

```text
OCR error

translation ambiguity

summary omission

schema conversion loss

normalization mistake

aggregation bias
```

---

# 24. L2-P018 — Provenance Is a Graph, Not Merely a Citation List

AMOS provenance SHOULD support:

```text
nodes
+
edges
```

not merely flat references.

Example:

```text
R1 ──→ E1 ──→ C1
 │             │
 │             └──→ C3
 │
 └──→ E2 ──→ C2 ──→ C3

R2 ──→ E3 ─────────→ C3
```

This structure reveals:

```text
shared ancestry
dependency overlap
root diversity
downstream impact
```

---

# 25. Provenance Node

A normalized provenance node MAY contain:

```yaml
node:

  id: null

  type:
    - ROOT_SOURCE
    - SOURCE
    - EVIDENCE
    - OBSERVATION
    - TRANSFORMATION
    - DERIVED_CLAIM
    - MEMORY
    - CANON_OBJECT
    - IMPLEMENTATION_ARTIFACT
    - BENCHMARK_ARTIFACT

  fingerprint: null

  scope: {}

  regime: {}

  time: null

  status: null
```

---

# 26. Provenance Edge

A normalized provenance edge MAY contain:

```yaml
edge:

  parent: null

  child: null

  edge_type:
    - COPIED_FROM
    - DERIVED_FROM
    - SUMMARIZED_FROM
    - TRANSLATED_FROM
    - EXTRACTED_FROM
    - OBSERVED_FROM
    - VALIDATED_BY
    - CONTRADICTED_BY
    - SUPERSEDES
    - REVOKES
    - TRANSFORMED_FROM
    - DEPENDS_ON

  load_bearing: null

  independence: null

  condition: null

  time: null
```

---

# 27. L2-P019 — Load-Bearing Ancestry Matters More Than Incidental Ancestry

Not every ancestor materially supports every claim.

AMOS SHOULD distinguish:

```text
LOAD_BEARING_ANCESTOR
```

from:

```text
INCIDENTAL_ANCESTOR
```

Confidence calculations should focus on ancestry actually required for the conclusion.

---

# 28. L2-P020 — Shared Load-Bearing Ancestry Reduces Independence

Define:

```text
O_ij
=
SharedLoadBearingAncestors(i,j)
```

Conceptually, larger ancestry overlap increases correlation risk.

This does not imply a universal numeric independence formula.

It defines a structural provenance constraint.

---

# 29. Independence Classes

AMOS provenance SHOULD support at least:

```text
INDEPENDENT

PARTIAL

CORRELATED

SAME_ROOT

UNKNOWN
```

These classes describe provenance relationships, not necessarily statistical independence in the mathematical sense.

---

# 30. INDEPENDENT

`INDEPENDENT` should require positive evidence that material support does not share the same relevant root ancestry.

Independence must be demonstrated.

It must not be assumed from surface differences.

---

# 31. PARTIAL

`PARTIAL` applies where sources contain both shared and independent ancestry.

Example:

```text
A uses dataset D + independent experiment X

B uses dataset D + independent experiment Y
```

Their evidence is not fully independent and not fully identical.

---

# 32. CORRELATED

`CORRELATED` applies when evidence shares material upstream dependencies.

Examples:

```text
same benchmark

same dataset

same source institution

same model output

same upstream report

same experimental apparatus

same validator
```

Correlation does not automatically invalidate evidence.

It constrains corroboration claims.

---

# 33. SAME_ROOT

`SAME_ROOT` applies where evidence resolves to the same relevant origin.

Multiple descendants of one root must not be counted as multiple independent roots.

---

# 34. UNKNOWN

When ancestry cannot be established:

```text
independence = UNKNOWN
```

not:

```text
independence = INDEPENDENT
```

Unknown ancestry therefore imposes a confidence ceiling.

---

# 35. L2-P021 — Independence Must Be Demonstrated, Never Assumed

The default relationship for unresolved ancestry is:

```text
UNKNOWN
```

This is one of the strongest provenance safeguards.

Surface diversity is insufficient.

---

# 36. L2-P022 — Effective Corroboration Is Root-Bounded

AMOS MODEL rule:

```text
Support_eff
≤
number_of_distinct_load_bearing_roots
```

Therefore ten descendant reports from one original source cannot create ten independent confirmations of the inherited claim.

---

# 37. L2-P023 — Source Count Must Not Be Used as Independence Count

```text
N_sources
```

and:

```text
N_independent_roots
```

are separate variables.

In general:

```text
N_independent_roots
≤
N_sources
```

---

# 38. L2-P024 — Provenance Confidence Ceiling

AMOS MODEL:

```text
Conf(C)
≤
min(
  PremiseCeiling,
  IndependenceCeiling,
  ScopeCeiling
)
```

Additional systems may include:

```text
FreshnessCeiling
RegimeCeiling
MeasurementCeiling
```

where applicable.

This is a governance formalization, not an externally established statistical theorem.

---

# 39. L2-P025 — Confidence Cannot Be Amplified by Provenance Sybils

Suppose:

```text
R
├── A
├── B
├── C
├── D
└── E
```

If all support the same claim solely through `R`:

```text
confidence_gain_from_independent_corroboration
```

must not be calculated as if five independent roots exist.

---

# 40. L2-P026 — Provenance Must Survive Agent Boundaries

If information moves:

```text
Agent A
   ↓
Agent B
   ↓
Agent C
```

the source ancestry must remain recoverable.

Agent handoff must not reset provenance.

---

# 41. L2-P027 — Provenance Must Survive Skill Boundaries

```text
Skill A
 ↓
Skill B
 ↓
Skill C
```

must preserve evidence lineage where claims are reused.

A new Skill invocation does not create a new source.

---

# 42. L2-P028 — Provenance Must Survive Session Boundaries

Persistent claims reused across sessions SHOULD preserve:

```text
source identity
root identity
timestamp
version
scope
regime
validation state
```

when material.

---

# 43. L2-P029 — Provenance Must Survive Memory Boundaries

Writing evidence into memory must not detach it from:

```text
source

time

scope

regime

status
```

Otherwise memory may become provenance laundering.

---

# 44. L2-P030 — Provenance Must Survive Compression

Context compression may shorten provenance representation.

It must not destroy decision-relevant ancestry.

At minimum, preserve:

```text
root identity

critical parent

version

status

material uncertainty
```

where needed.

---

# 45. L2-P031 — Provenance Must Survive RSCF Composition

When RSCF nodes compose:

```text
N1 + N2 → N3
```

`N3` must retain provenance dependencies on `N1` and `N2`.

RSCF composition must not create epistemic independence.

---

# 46. L2-P032 — Provenance Must Survive H/M/L Translation

If evidence moves:

```text
L → M → H
```

its ancestry remains attached.

Scale translation cannot reset origin.

---

# 47. L2-P033 — Scope Must Be Attached to Provenance

A source may be valid for one scope and irrelevant for another.

Provenance SHOULD therefore include:

```text
scope(source)
```

rather than source identity alone.

---

# 48. L2-P034 — Regime Must Be Attached to Provenance

Evidence originating under regime `R1` may not support conclusions under `R2`.

```text
provenance
+
regime
```

must remain jointly inspectable where regime matters.

---

# 49. L2-P035 — Time Must Be Attached to Provenance

Relevant temporal fields MAY include:

```text
creation_time

observation_time

publication_time

retrieval_time

ingestion_time

validation_time

revocation_time

supersession_time
```

These times have different meanings and should not be collapsed where material.

---

# 50. L2-P036 — Version Must Be Attached to Mutable Sources

For mutable sources:

```text
source identity
```

alone may be insufficient.

AMOS SHOULD preserve:

```text
source_id + version
```

or an equivalent immutable reference.

---

# 51. L2-P037 — Hashes Are Evidence of Byte Identity Under Their Assumptions

A cryptographic hash can support:

```text
BYTE_IDENTITY
```

under the assumed hashing process.

It does not prove:

```text
truth

authorship

authority

semantic correctness

independence
```

---

# 52. L2-P038 — Provenance Identity and Semantic Identity Are Distinct

Two byte-identical files may have different:

```text
storage locations

permissions

timestamps

governance contexts
```

while retaining the same content root.

Conversely, two semantically equivalent statements may have different byte representations.

AMOS must preserve the distinction.

---

# 53. L2-P039 — Provenance and Authorship Are Distinct

Knowing where an artifact came from does not necessarily prove who authored its intellectual content.

Possible identities include:

```text
file creator

uploader

editor

publisher

origin architect

quoted author

data producer
```

These roles should not be silently collapsed.

---

# 54. L2-P040 — Provenance and Ownership Are Distinct

```text
SOURCE_OF_INFORMATION
```

is not automatically:

```text
LEGAL_OWNER
```

or:

```text
CANON_AUTHORITY
```

or:

```text
EXECUTION_AUTHORITY
```

---

# 55. L2-P041 — Provenance and Authority Are Distinct

A source may have valid provenance but insufficient authority for an action.

```text
PROVENANCE_VALID
!=
AUTHORIZED
```

This preserves the boundary between epistemic evidence and control-plane authority.

---

# 56. L2-P042 — Canon Authority Must Be Provenance-Bound

Canon promotion SHOULD preserve:

```text
candidate source

origin

review

approval

version

supersession
```

so later systems can distinguish:

```text
SOURCE MATERIAL
```

from:

```text
CANONICAL ADMISSION
```

---

# 57. L2-P043 — Canonical Admission Does Not Rewrite Source History

When an artifact becomes canonical:

```text
source_history
```

must remain recoverable.

Canon admission adds a governance event.

It does not replace provenance.

---

# 58. L2-P044 — Supersession Must Preserve the Predecessor

When:

```text
B supersedes A
```

AMOS should retain:

```text
A
B
A → SUPERSEDED_BY → B
```

rather than rewriting `A` into `B`.

---

# 59. L2-P045 — Supersession Is Not Deletion

A superseded source may remain necessary for:

```text
historical reconstruction

dependency analysis

replay

audit

rollback

interpretation of older decisions
```

Therefore:

```text
SUPERSEDED
!=
NONEXISTENT
```

---

# 60. L2-P046 — Revocation Must Be Explicit

A provenance root may enter:

```text
REVOKED
```

when its authority, validity, integrity, or admissibility is withdrawn under an applicable governance process.

Revocation SHOULD identify:

```text
who / what revoked it

authority

reason

time

scope

affected dependencies
```

---

# 61. L2-P047 — Revocation Must Propagate Selectively

Core rule:

```text
Invalid(p)
⇒
invalidate(load-bearing descendants of p)
```

Only descendants materially dependent on the invalidated premise should be invalidated where dependency structure is known.

---

# 62. L2-P048 — Revocation Must Not Destroy Independent Support

Suppose:

```text
C
← R1
← R2
```

and `R1` is revoked.

If `R2` independently supports `C`, then:

```text
C
```

requires reassessment.

It does not necessarily become false.

---

# 63. L2-P049 — Provenance Graphs Must Support Selective Invalidation

A valid provenance system should answer:

```text
Which claims depend on source S?

Which depend on version V?

Which depend on root R?

Which depend only on R?

Which have independent surviving support?
```

Without this capability, safe repair becomes difficult.

---

# 64. L2-P050 — Unknown Provenance Must Remain Visible

Evidence with missing ancestry should be labeled:

```text
PROVENANCE_UNKNOWN
```

or equivalent.

It must not silently inherit trusted provenance from neighboring evidence.

---

# 65. L2-P051 — Provenance Gaps Are Epistemic Gaps

If the root source cannot be established:

```text
ROOT = UNKNOWN
```

then claims requiring independent corroboration may remain:

```text
CONDITIONAL
```

or:

```text
UNKNOWN/GAP
```

depending on stakes.

---

# 66. L2-P052 — Provenance Must Be Immutable in History, Mutable in Status

Historical events should remain append-only conceptually:

```text
SOURCE_CREATED

SOURCE_INGESTED

SOURCE_VALIDATED

SOURCE_REVOKED
```

Current status may change.

Historical provenance should not be rewritten to match the current status.

---

# 67. L2-P053 — Provenance Updates Require Versioned State

Changes to:

```text
root resolution

source identity

fingerprint

independence class

scope

regime

status
```

SHOULD produce a new provenance state or equivalent auditable revision.

---

# 68. L2-P054 — Root Resolution May Be Revised

A source initially classified:

```text
INDEPENDENT
```

may later be discovered to share root `R`.

Correct repair:

```text
INDEPENDENT
→
SAME_ROOT
```

plus downstream confidence revalidation.

---

# 69. L2-P055 — Independence Is Claim-Relative

Two sources may be independent for one claim and correlated for another.

Example:

```text
A and B independently collect local observations
```

but both use:

```text
shared benchmark D
```

for a benchmark claim.

Therefore:

```text
Independence(A,B,C)
```

may be more precise than a universal independence label.

---

# 70. L2-P056 — Provenance Independence Is Not Statistical Independence

AMOS provenance independence concerns evidentiary ancestry.

It must not automatically be interpreted as probabilistic independence:

```text
P(A,B)=P(A)P(B)
```

unless separately established.

---

# 71. L2-P057 — Common Tooling Can Create Correlation

Two apparently separate evidence pipelines may share:

```text
parser

model

retrieval engine

dataset

benchmark harness

validator

measurement device
```

Shared tooling may introduce correlated failure.

---

# 72. L2-P058 — Common Validator Does Not Create Independent Validation

If:

```text
A validated by V

B validated by V
```

then validation paths share `V`.

This matters when `V` itself may be systematically wrong.

---

# 73. L2-P059 — Shared Fixtures Can Create False Independence

Two tests may appear independent while using the same:

```text
fixtures

seed data

mock service

oracle

expected outputs
```

Provenance should expose this correlation when consequential.

---

# 74. L2-P060 — Provenance Must Include Negative Lineage Where Material

AMOS may preserve not only what produced a claim but also:

```text
rejected sources

failed validations

contradictory sources

revoked ancestors
```

when these affect interpretation.

---

# 75. Provenance State Machine

```text
DISCOVERED
    ↓
IDENTIFIED
    ↓
ROOT_RESOLVED
    ↓
CLASSIFIED
    ↓
ADMITTED
    ↓
VALID
```

Possible branches:

```text
DISCOVERED
    ↓
UNKNOWN
```

```text
IDENTIFIED
    ↓
QUARANTINED
```

```text
VALID
    ↓
SUPERSEDED
```

```text
VALID
    ↓
REVOKED
```

```text
VALID
    ↓
STALE
```

```text
UNKNOWN
    ↓
ROOT_RESOLVED
```

---

# 76. Provenance Status Vocabulary

Proposed statuses:

```text
DISCOVERED

IDENTIFIED

ROOT_RESOLVED

UNRESOLVED

ADMITTED

QUARANTINED

VALID

STALE

SUPERSEDED

REVOKED

INVALID

UNKNOWN/GAP
```

---

# 77. H/M/L Applicability

L2 applies recursively across all AMOS scales.

## H — Governing Provenance

Examples:

```text
canon ancestry

architecture lineage

core-version lineage

governance authority history

system-wide evidence roots

canonical supersession
```

Errors at H may contaminate many downstream systems.

---

## M — Subsystem Provenance

Examples:

```text
Skill sources

agent evidence

memory lineage

domain-model sources

workflow artifacts

benchmark lineage

repository evidence
```

---

## L — Local Provenance

Examples:

```text
file

paragraph

tool output

observation

variable

test result

source fragment

individual claim
```

---

# 78. Cross-Scale Provenance Rule

For:

```text
L → M → H
```

the root ancestry must remain traceable.

A higher-scale summary does not become an independent origin merely because it aggregates lower-scale evidence.

---

# 79. Control-Plane Requirements

A runtime enforcing L2 SHOULD eventually support:

```text
source registration

root resolution

fingerprinting

parent-child lineage

transformation recording

version identity

independence classification

ancestry overlap

scope tracking

regime tracking

freshness

revocation

supersession

selective invalidation

quarantine

revalidation
```

This document does not claim these functions are currently implemented.

---

# 80. Typed Provenance Tensor

AMOS MODEL:

```text
T[o,p,s,t,r,v,g,e,c,k]
```

where the axes may encode governed object state across:

```text
object

provenance

scale

time

regime

version

governance

evidence

confidence

knowledge class
```

Exact axis semantics require registry-level normalization before runtime implementation.

---

# 81. Typed Provenance Relation

AMOS MODEL:

```text
R[i,j,relation_type,time,regime,provenance]
```

This represents typed relations between provenance objects.

Example relation types:

```text
DERIVED_FROM

COPIED_FROM

SUPERSEDES

REVOKES

VALIDATES

CONTRADICTS

SHARES_ROOT_WITH
```

---

# 82. Hard Admission Gate

Proposed invariant gate:

```text
Admit(x)
=
AND_i I_i(x)
```

where required invariants `I_i` depend on the admission context.

Potential provenance gates include:

```text
identity resolved

source admissible

required provenance present

scope known

regime known

status not revoked
```

Not every evidence class requires identical gates.

---

# 83. Provenance RSCF Node

Normalized RSCF node:

```text
N =
(
 id,
 type,
 HML,
 claim,
 scope,
 regime,
 time,
 observer,
 provenance,
 confidence,
 falsifier,
 status
)
```

---

# 84. Provenance RSCF Edge

Normalized RSCF edge:

```text
E =
(
 parent,
 child,
 edge_type,
 load_bearing,
 independence,
 condition
)
```

These structures allow epistemic reasoning to preserve ancestry.

---

# 85. Provenance Operators

Proposed operators:

```text
REGISTER_SOURCE

REGISTER_ROOT

RESOLVE_ROOT

FINGERPRINT

COMPARE_FINGERPRINT

COLLAPSE_ALIAS

TRACE_PARENT

TRACE_ANCESTRY

CLASSIFY_INDEPENDENCE

COMPUTE_ANCESTRY_OVERLAP

REGISTER_TRANSFORMATION

REGISTER_VERSION

SUPERSEDE

REVOKE

QUARANTINE

ADMIT

INVALIDATE_DESCENDANTS

REVALIDATE

AUDIT_PROVENANCE
```

---

# 86. Agents

Potential provenance roles:

```text
SOURCE_IDENTITY_AGENT

ROOT_RESOLVER

PROVENANCE_AUDITOR

LINEAGE_ANALYST

SYBIL_DETECTOR

INDEPENDENCE_AUDITOR

VERSION_AUDITOR

REVOCATION_AUDITOR

RSCF_PROVENANCE_AUDITOR
```

Agent capability does not grant canon or execution authority.

---

# 87. Skills

Relevant AMOS capabilities include:

```text
provenance Sybil hardening

source reading

claim verification

RSCF modeling

knowledge harvesting

memory conflict governance

benchmark forensics

repository ingestion

semantic grounding

canon compilation
```

Each Skill remains subject to its own provenance and authority boundaries.

---

# 88. Workflow — Source Intake

```text
SOURCE DISCOVERED
      ↓
IDENTIFY SOURCE
      ↓
CAPTURE VERSION
      ↓
CAPTURE TIME
      ↓
CAPTURE SCOPE / REGIME
      ↓
FINGERPRINT WHERE APPLICABLE
      ↓
RESOLVE PARENT
      ↓
RESOLVE ROOT
      ↓
CLASSIFY STATUS
      ↓
ADMIT / QUARANTINE
```

---

# 89. Workflow — Root Resolution

```text
EVIDENCE OBJECT
      ↓
IMMEDIATE SOURCE
      ↓
PARENT CHAIN
      ↓
FINGERPRINT CHECK
      ↓
TRANSFORMATION HISTORY
      ↓
KNOWN ANCESTORS
      ↓
ROOT CANDIDATES
      ↓
RESOLVE / UNKNOWN
```

Unknown must remain a valid output.

---

# 90. Workflow — Sybil Collapse

```text
ENUMERATE EVIDENCE
      ↓
RESOLVE ROOTS
      ↓
COMPARE EXACT ROOT FINGERPRINTS
      ↓
COLLAPSE ROOT ALIASES
      ↓
MAP SHARED ANCESTRY
      ↓
CLASSIFY INDEPENDENCE
      ↓
CALCULATE EFFECTIVE SUPPORT
      ↓
APPLY CONFIDENCE CEILING
```

---

# 91. Workflow — Independence Audit

```text
E1 + E2 + ... + En
        ↓
ROOT RESOLUTION
        ↓
ANCESTRY MATRIX
        ↓
SHARED LOAD-BEARING ANCESTORS
        ↓
COMMON TOOLING / DATA / VALIDATORS
        ↓
INDEPENDENCE CLASSIFICATION
        ↓
EFFECTIVE CORROBORATION
```

---

# 92. Workflow — Revocation

```text
ROOT R REVOKED
      ↓
VERIFY REVOCATION AUTHORITY
      ↓
MARK R
      ↓
TRACE LOAD-BEARING DESCENDANTS
      ↓
CHECK INDEPENDENT SURVIVING ROOTS
      ↓
INVALIDATE / DOWNGRADE AFFECTED CLAIMS
      ↓
PRESERVE UNAFFECTED CLAIMS
      ↓
REVALIDATE
```

---

# 93. Workflow — Supersession

```text
NEW VERSION V2
      ↓
IDENTIFY PREDECESSOR V1
      ↓
VERIFY SUPERSESSION RELATION
      ↓
REGISTER V1 → V2
      ↓
PRESERVE V1 HISTORY
      ↓
MAP DEPENDENT CLAIMS
      ↓
CHECK WHETHER REVALIDATION REQUIRED
```

---

# 94. Workflow — Provenance Repair

```text
PROVENANCE FAILURE DETECTED
        ↓
IDENTIFY EARLIEST BAD NODE / EDGE
        ↓
QUARANTINE AFFECTED SUBGRAPH
        ↓
PRESERVE UNAFFECTED GRAPH
        ↓
RECOVER SOURCE / ROOT / VERSION
        ↓
RECOMPUTE INDEPENDENCE
        ↓
RECOMPUTE CONFIDENCE CEILINGS
        ↓
REVALIDATE DESCENDANTS
```

---

# 95. Protocol — Source Registration

```yaml
source_registration:

  source_id: null

  source_type: null

  root_id: null

  parent_id: null

  fingerprint: null

  fingerprint_method: null

  version: null

  created_at: null

  observed_at: null

  ingested_at: null

  scope: {}

  regime: {}

  status: null

  authority_class: null

  provenance_refs: []
```

---

# 96. Protocol — Independence Assessment

```yaml
independence_assessment:

  object_a: null

  object_b: null

  claim_id: null

  root_a: null

  root_b: null

  exact_root_match: null

  shared_ancestors: []

  shared_load_bearing_ancestors: []

  shared_tools: []

  shared_datasets: []

  shared_validators: []

  classification:
    - INDEPENDENT
    - PARTIAL
    - CORRELATED
    - SAME_ROOT
    - UNKNOWN

  confidence_ceiling: null
```

---

# 97. Protocol — Revocation Record

```yaml
revocation:

  target_id: null

  target_version: null

  revoked_by: null

  authority_witness: null

  reason: null

  scope: {}

  regime: {}

  effective_time: null

  affected_descendants: []

  surviving_independent_support: []

  resulting_status: null
```

---

# 98. Protocol — Supersession Record

```yaml
supersession:

  predecessor: null

  successor: null

  reason: null

  authority: null

  timestamp: null

  predecessor_retained: true

  dependent_claims: []

  revalidation_required: null
```

---

# 99. Provenance Invariants

```text
L2-INV001
Every consequential evidence object must have recoverable provenance or an explicit provenance gap.

L2-INV002
Immediate source and root source must remain distinguishable.

L2-INV003
Multiple aliases of one root count as one provenance family.

L2-INV004
Paraphrase does not create independence.

L2-INV005
Translation does not create independence.

L2-INV006
Summarization does not create independence.

L2-INV007
Memory storage does not create independence.

L2-INV008
Agent handoff does not create independence.

L2-INV009
Skill handoff does not create independence.

L2-INV010
Exact-root fingerprint equality collapses root aliases where fingerprint assumptions are valid.

L2-INV011
Fingerprint equality is not universal semantic equivalence.

L2-INV012
Different fingerprints do not prove independent ancestry.

L2-INV013
Independence must be demonstrated, not assumed.

L2-INV014
Unknown ancestry imposes an independence/confidence ceiling.

L2-INV015
Source count must not substitute for independent-root count.

L2-INV016
Provenance must remain versioned and inspectable.

L2-INV017
Supersession must preserve historical lineage.

L2-INV018
Revocation must propagate selectively through load-bearing dependencies.

L2-INV019
Independent surviving support must not be destroyed by unrelated revocation.

L2-INV020
Provenance must survive H/M/L transformation.
```

---

# 100. Failure Modes

```text
L2-FM001
Different URLs counted as independent roots.

L2-FM002
Copied documents counted independently.

L2-FM003
Paraphrases counted independently.

L2-FM004
Translations counted independently.

L2-FM005
Summaries counted independently.

L2-FM006
Model restatements counted independently.

L2-FM007
Memory copies counted independently.

L2-FM008
Agent handoffs reset provenance.

L2-FM009
Skill handoffs reset provenance.

L2-FM010
Source identity confused with root identity.

L2-FM011
Fingerprint match interpreted as universal semantic identity.

L2-FM012
Fingerprint mismatch interpreted as proof of independence.

L2-FM013
Unknown ancestry assumed independent.

L2-FM014
Shared dataset ignored.

L2-FM015
Shared benchmark ignored.
```

---

# 101. Extended Failure Modes

```text
L2-FM016
Shared validator ignored.

L2-FM017
Shared model ignored.

L2-FM018
Shared fixtures ignored.

L2-FM019
Source version omitted.

L2-FM020
Source time omitted.

L2-FM021
Scope lost during provenance transfer.

L2-FM022
Regime lost during provenance transfer.

L2-FM023
Transformation history erased.

L2-FM024
Canon admission erases original source.

L2-FM025
Supersession deletes predecessor history.

L2-FM026
Revocation deletes unrelated descendants.

L2-FM027
Revocation fails to invalidate dependent descendants.

L2-FM028
Historical provenance rewritten after failure.

L2-FM029
Authorship inferred from uploader identity.

L2-FM030
Ownership inferred from source identity.

L2-FM031
Authority inferred from provenance validity.

L2-FM032
Correlated evidence inflates confidence.

L2-FM033
Evidence count substitutes for root count.

L2-FM034
Provenance gap silently treated as trusted.

L2-FM035
Compression removes load-bearing ancestry.
```

---

# 102. Repair Principles

Provenance repair SHOULD follow:

```text
PRESERVE ORIGINAL ARTIFACT

IDENTIFY BAD NODE OR EDGE

IDENTIFY ROOT

RECOVER PARENTAGE

RECOVER VERSION

RECOVER TRANSFORMATION HISTORY

RECLASSIFY INDEPENDENCE

QUARANTINE AFFECTED CLAIMS

PRESERVE UNAFFECTED CLAIMS

RECALCULATE EFFECTIVE SUPPORT

RECALCULATE CONFIDENCE CEILING

REVALIDATE DESCENDANTS
```

---

# 103. Quarantine Conditions

A provenance object SHOULD be considered for quarantine when:

```text
root unresolved

source identity ambiguous

fingerprint conflict

version conflict

unexpected ancestry cycle

untrusted transformation

revoked ancestor

unknown authority

corrupted metadata

scope missing where required

regime missing where required

suspected Sybil alias
```

Quarantine means:

```text
NOT SAFE FOR NORMAL PROMOTION
```

not:

```text
FALSE
```

---

# 104. Tests

## L2-T001 — Exact Root Alias Collapse

Input:

```yaml
A:
  root_fingerprint: "abc123"

B:
  root_fingerprint: "abc123"
```

Expected:

```text
SameRoot(A,B) = true
```

and:

```text
independence != INDEPENDENT
```

---

## L2-T002 — Paraphrase Independence

Input:

```text
A = original claim
B = paraphrase(A)
```

Expected:

```text
root(B) = root(A)
```

for inherited content.

---

## L2-T003 — Translation Independence

Input:

```text
A = English source
B = Vietnamese translation of A
```

Expected:

```text
B does not count as independent corroboration of A.
```

---

## L2-T004 — Summary Independence

Input:

```text
A → summary B
```

Expected:

```text
independence(A,B) != INDEPENDENT
```

---

## L2-T005 — Hidden Shared Root

Input:

```text
A ← R
B ← R
```

with different filenames and URLs.

Expected:

```text
effective_root_count = 1
```

for root-dependent evidence.

---

## L2-T006 — Unknown Ancestry

Input:

```yaml
source_A:
  root: null
```

Expected:

```text
independence = UNKNOWN
```

not `INDEPENDENT`.

---

## L2-T007 — Selective Revocation

Input:

```text
R1 → C1 → C3
R2 → C2
```

Revoke `R1`.

Expected:

```text
C1 requires invalidation/revalidation
C3 requires invalidation/revalidation
C2 remains unaffected
```

---

## L2-T008 — Independent Surviving Root

Input:

```text
R1 → C
R2 → C
```

with:

```text
R1 independent of R2
```

Revoke `R1`.

Expected:

```text
C requires reassessment
```

but:

```text
C != automatically false
```

---

## L2-T009 — Supersession Preservation

Input:

```text
V1 → superseded by V2
```

Expected:

```text
V1 remains historically recoverable.
```

---

## L2-T010 — Agent Handoff

Input:

```text
Source S
→ Agent A
→ Agent B
→ Agent C
```

Expected:

```text
root(output_C) = S
```

for claims solely inherited from `S`.

---

# 105. Extended Validators

```text
validate_source_identity()

validate_root_identity()

validate_parent_chain()

validate_fingerprint()

validate_alias_collapse()

validate_transformation_history()

validate_version()

validate_scope_provenance()

validate_regime_provenance()

validate_independence()

validate_ancestry_overlap()

validate_effective_root_count()

validate_revocation()

validate_supersession()

validate_selective_invalidation()

validate_provenance_confidence_ceiling()

validate_rscf_provenance()
```

These are required validation surfaces, not claims of existing executable functions.

---

# 106. Falsifiers

This specification should be revised if authoritative AMOS source material establishes that:

```text
exact-root aliases are intentionally treated as independent;

paraphrases create independent provenance;

unknown ancestry defaults to independent;

revocation globally invalidates unrelated knowledge;

provenance history may be rewritten rather than preserved;

or later valid AMOS canon explicitly supersedes these rules.
```

The generalized AMOS_MODEL equations should also be revised if source canon defines materially different tensors, independence classes, confidence equations, or provenance semantics.

---

# 107. Dependencies

```yaml
dependencies:

  hard:
    - "L0_INTEGRITY"
    - "L1_EPISTEMIC"

  architectural:
    - "CORE_LAWS_CANON_CORE_LAWS_CONTRACT"
    - "CORE_LAWS_MAP"
    - "CANON_CONTRACT"
    - "00_ROOT"

  conceptual:
    - "RSCF"
    - "SOURCE_IDENTITY"
    - "VERSION_LINEAGE"
    - "SCOPE"
    - "REGIME"
    - "FRESHNESS"
    - "SUPERSESSION"
    - "REVOCATION"
    - "SELECTIVE_INVALIDATION"
```

---

# 108. Evidence / Provenance

Current artifact-level provenance:

```yaml
provenance:

  origin_architect: "Trang Phan"

  steward: "Trang Phan"

  artifact:
    path: "01_CANON/01_CORE_LAWS/L2_PROVENANCE.md"

  source_lineage:

    - source:
        family: "AMOS_CORE"
        version: "v3.7.1"
        architecture: "Provenance Topology Hardened Runtime"

      source_supported:
        - "provenance topology hardening"
        - "exact-root content fingerprint Sybil collapse"

  formalization:

    class: "AMOS_MODEL"

    includes:
      - "generalized provenance tensor"
      - "ancestry overlap"
      - "independence classification"
      - "effective corroboration ceiling"
      - "confidence ceiling"
      - "selective invalidation"
      - "RSCF provenance schema"

  final_canon_approval:
    status: "UNKNOWN/GAP"
```

---

# 109. Source/Model Firewall

The following distinction MUST remain explicit:

```text
SOURCE-DERIVED:

AMOS_CORE v3.7.1 contains provenance-topology hardening.

Exact-root content fingerprints are used to collapse Sybil origin aliases.


AMOS_MODEL:

P[source,root,fingerprint,parent,time,regime,status]

O_ij = SharedLoadBearingAncestors(i,j)

I_ij ∈ {
  INDEPENDENT,
  PARTIAL,
  CORRELATED,
  SAME_ROOT,
  UNKNOWN
}

Support_eff
≤
number_of_distinct_load_bearing_roots

Conf(C)
≤
min(
  PremiseCeiling,
  IndependenceCeiling,
  ScopeCeiling
)
```

The AMOS_MODEL formalizations MUST NOT be retroactively described as exact source equations unless source recovery establishes that fact.

---

# 110. Uncertainty Vector

```yaml
uncertainty:

  existence_of_provenance_hardening:
    state: "LOW"

  exact_root_alias_collapse:
    state: "LOW"

  complete_original_L2_law_inventory:
    state: "HIGH"

  canonical_L2_numbering:
    state: "HIGH"

  canonical_tensor_definition:
    state: "HIGH"

  canonical_independence_classes:
    state: "MODERATE/HIGH"

  canonical_confidence_equation:
    state: "HIGH"

  canonical_HML_mapping:
    state: "HIGH"

  runtime_implementation:
    state: "UNKNOWN"

  empirical_validation:
    state: "NOT_CLAIMED"
```

---

# 111. Confidence Ceiling

```yaml
confidence_ceiling:

  provenance_hardening_source_anchor:
    class: "SOURCE_DERIVED"

  exact_root_alias_collapse:
    class: "SOURCE_DERIVED"

  generalized_architecture:
    class: "AMOS_MODEL"

  final_canonical_L2_specification:
    value: 0

  implementation:
    value: 0

  runtime_validation:
    value: 0

  empirical_universality:
    value: 0
```

---

# 112. Gap Matrix

```yaml
gap_matrix:

  authoritative_full_L2_source:
    status: "UNKNOWN/GAP"
    severity: "CRITICAL_FOR_FINAL_CANON"

  source_provenance_hardening_anchor:
    status: "RECOVERED/PARTIAL"

  exact_root_fingerprint_rule:
    status: "RECOVERED/PARTIAL"

  complete_canonical_L2_law_inventory:
    status: "UNKNOWN/GAP"
    severity: "CRITICAL"

  canonical_provenance_tensor:
    status: "UNKNOWN/GAP"

  canonical_independence_taxonomy:
    status: "UNKNOWN/GAP"

  canonical_confidence_equation:
    status: "UNKNOWN/GAP"

  canonical_HML_provenance_contract:
    status: "UNKNOWN/GAP"

  executable_provenance_runtime:
    status: "UNKNOWN/GAP"

  executable_validators:
    status: "UNKNOWN/GAP"

  executed_tests:
    status: "UNKNOWN/GAP"

  production_validation:
    status: "UNKNOWN/GAP"

  final_canon_approval:
    status: "UNKNOWN/GAP"
    severity: "CRITICAL"
```

---

# 113. Promotion Requirements

Promotion beyond this state requires recovery or explicit approval of:

```text
AUTHORITATIVE L2 SOURCE MATERIAL

CANONICAL LAW INVENTORY

CANONICAL PROVENANCE TYPES

CANONICAL ROOT DEFINITION

CANONICAL FINGERPRINT RULES

CANONICAL INDEPENDENCE RULES

CANONICAL CONFIDENCE RULES

CANONICAL REVOCATION RULES

CANONICAL SUPERSESSION RULES

H/M/L APPLICABILITY

DEPENDENCY GRAPH

CONTROL-PLANE OWNERSHIP

TEST CONTRACT

VERSION / SUPERSESSION LINEAGE

CANON AUTHORITY
```

---

# 114. Promotion Ladder

Canonical lifecycle:

```text
PLACEHOLDER
    ↓
PROPOSED_SPECIFICATION
    ↓
PARTIAL_SOURCE_ALIGNMENT
    ↓
SOURCE_ALIGNED
    ↓
CANON_REVIEWED
    ↓
CANON_APPROVED
    ↓
REGISTERED
```

Implementation lifecycle:

```text
NOT_IMPLEMENTED
    ↓
IMPLEMENTATION_PROPOSED
    ↓
IMPLEMENTED
    ↓
TESTED
    ↓
VALIDATED
    ↓
RUNTIME_ACTIVE
```

These axes remain independent.

---

# 115. L2 RSCF

```yaml
rscf:

  claim:

    id: "l2_provenance"

    class: "AMOS_MODEL"

    statement: >
      AMOS requires provenance-aware evidence handling in which material
      information preserves source identity, root ancestry, transformations,
      versions, scope, regime, independence status, supersession and revocation
      state; multiple aliases or descendants of the same root must not be
      counted as independent corroboration.

  source_supported_claims:

    - claim:
        "AMOS_CORE v3.7.1 hardens provenance topology."

      class:
        "SOURCE_CLAIM / SOURCE_DERIVED"

    - claim:
        "Exact-root content fingerprints collapse Sybil origin aliases."

      class:
        "SOURCE_CLAIM / SOURCE_DERIVED"

  premises:

    - "surface source identity may differ from root identity"

    - "derived evidence may share load-bearing ancestry"

    - "shared ancestry affects independence"

    - "unknown ancestry cannot safely be assumed independent"

    - "provenance state may change through supersession or revocation"

    - "downstream claims require selective revalidation when load-bearing provenance fails"

  evidence:
    - "AMOS provenance-topology hardening source anchor"

  provenance:
    origin_architect: "Trang Phan"
    source_family: "AMOS_CORE"
    source_version_anchor: "v3.7.1"
    artifact: "01_CANON/01_CORE_LAWS/L2_PROVENANCE.md"

  scope:
    system: "AMOS OS"
    layer: "CORE LAWS"
    family: "L2_PROVENANCE"

  regime:
    - "ARCHITECTURE"
    - "PROVENANCE_GOVERNANCE"
    - "AMOS_MODEL"

  freshness:
    updated: "2026-08-26"

  dependencies:
    - "L0_INTEGRITY"
    - "L1_EPISTEMIC"
    - "CORE_LAWS_CANON_CORE_LAWS_CONTRACT"
    - "CORE_LAWS_MAP"

  competing:

    - id: "SURFACE_SOURCE_INDEPENDENCE"

      statement: >
        Distinct files, URLs, agents or publications should be counted
        as independent sources.

      status: "REJECTED"

    - id: "PARAPHRASE_INDEPENDENCE"

      statement: >
        Paraphrasing a source creates a new independent evidence root.

      status: "REJECTED"

    - id: "UNKNOWN_MEANS_INDEPENDENT"

      statement: >
        Sources with unresolved ancestry may be presumed independent.

      status: "REJECTED"

    - id: "GLOBAL_REVOCATION"

      statement: >
        Failure of one provenance root should invalidate all related
        system knowledge.

      status: "REJECTED"

  falsifiers:

    - "authoritative AMOS canon establishes incompatible provenance rules"

    - "higher valid canon supersedes this specification"

    - "source recovery establishes materially different L2 semantics"

  confidence_ceiling:

    source_anchored_subset: "SOURCE_DERIVED"

    generalized_specification: "AMOS_MODEL"

    final_canon: 0
```

---

# 116. Current Completion State

```yaml
completion:

  artifact:
    name: "L2_PROVENANCE.md"

  placeholder:
    status: false

  substantive_content:
    status: "PRESENT"

  specification:
    status: "COMPLETE_FOR_DECLARED_MODEL_SCOPE"

  epistemic_class:
    status: "AMOS_MODEL"

  source_alignment:
    status: "PARTIAL_SOURCE_ALIGNMENT"

  recovered_source_anchor:
    status: "PRESENT"

  final_canon:
    status: "UNKNOWN/GAP"

  implementation:
    status: "NOT_ESTABLISHED"

  runtime_enforcement:
    status: "NOT_ESTABLISHED"

  executable_validation:
    status: "NOT_ESTABLISHED"
```

---

# 117. Final L2 Provenance Contract

> **AMOS must preserve where information came from, what root it descends from, what transformations it underwent, what version and regime it belongs to, and whether apparently separate evidence is genuinely independent. Multiple aliases, copies, translations, summaries, memories, agents, Skills, or model outputs derived from one root do not become independent corroboration merely through transformation or repetition. Unknown ancestry must remain unknown. Provenance must remain versioned, inspectable, and attached to downstream claims. When a root fails, only its load-bearing descendants should be invalidated, while independently supported knowledge is preserved.**

Compressed L2 law:

```text
IDENTIFY THE SOURCE

RESOLVE THE ROOT

PRESERVE THE PARENT

PRESERVE THE VERSION

PRESERVE THE TIME

PRESERVE THE TRANSFORMATION

PRESERVE SCOPE

PRESERVE REGIME

COLLAPSE ROOT ALIASES

DO NOT COUNT PARAPHRASES AS INDEPENDENT

DO NOT COUNT COPIES AS INDEPENDENT

DO NOT COUNT MEMORY AS A NEW ROOT

DO NOT COUNT AGENT HANDOFFS AS NEW ROOTS

DEMONSTRATE INDEPENDENCE

KEEP UNKNOWN ANCESTRY UNKNOWN

BOUND CORROBORATION BY DISTINCT ROOTS

BOUND CONFIDENCE BY PROVENANCE

PRESERVE SUPERSESSION HISTORY

PROPAGATE REVOCATION SELECTIVELY

KEEP THE PROVENANCE GRAPH INSPECTABLE
```

---

00_ROOT_MOC|AMOS MOC

---

**Related:** [[00_HOME]] · AMOS_RSCF_NODES · L0_INTEGRITY · L1_EPISTEMIC · CORE_LAWS_MAP · CORE_LAWS_CANON_CORE_LAWS_CONTRACT

---

RSCF-NODE

node_id: l2_provenance

node_type: core_law_family

path: 01_CANON/01_CORE_LAWS/L2_PROVENANCE.md

origin_architect: Trang Phan

artifact_status: PROPOSED_SOURCE_ALIGNED_SPECIFICATION

canonical_status: PARTIAL_SOURCE_ALIGNMENT

RSCF-RELATIONS:

* INDEXED_BY: [[00_HOME]]

* INDEXED_BY: AMOS_RSCF_NODES

* GOVERNED_BY: CORE_LAWS_CANON_CORE_LAWS_CONTRACT

* MAPPED_BY: CORE_LAWS_MAP

* DEPENDS_ON: L0_INTEGRITY

* DEPENDS_ON: L1_EPISTEMIC

* DEPENDS_ON: [[00_ROOT_MOC]]

* BELONGS_TO: 01_CANON/01_CORE_LAWS

claim_class: AMOS_MODEL

source_alignment: PARTIAL

final_canon_confidence_ceiling: 0

```
```

---
**MOC:** [[01_CORE_LAWS_MOC]]