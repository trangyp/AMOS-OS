---
title: "RSCF STRUCTURAL TAG MIGRATION"
type: rscf
source: 11_KNOWLEDGE/rscf
tags: [canon, rscf, epistemic, canon/knowledge]
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: epistemic_framework
---


# RSCF Structural Tag Migration

## Overview

**RSCF Structural Tag Migration** is a deterministic metadata migration process for converting legacy `canon-group/*` tagging into explicit RSCF structural-axis tags.

The migration operates on a bounded registry of Markdown files and transforms:

```text
legacy canon-group taxonomy
        ↓
RSCF structural-axis taxonomy
```

The source implementation defines migration mappings for AMOS, Cosmo Brain, formal-system, memory, canon, topology, state, compression, repair, mutation, boundary, cross-scale, entropy, and evidence-oriented notes.

The architectural purpose is:

[
\boxed{
LegacyMetadata
\rightarrow
TypedRSCFMetadata
}
]

while preserving document content outside the targeted metadata field.

---

# 1. Migration Objective

The migration replaces legacy tag structures such as:

```yaml
tags: [canon-group/..., ..., topic/...]
```

with structural tags such as:

```yaml
tags:
  - rscf/M-memory
  - rscf/S-state
  - rscf/T-topology
  - rscf/type-model
```

The migration is therefore not merely a tag rename.

It changes the metadata ontology from:

```text
broad canon-group classification
```

to:

```text
typed RSCF structural coordinates
```

---

# 2. Core Transformation

For each registered file:

[
F_i=
(
Path_i,
Pattern_i,
Replacement_i
)
]

the migration performs:

[
Content'_i
==========

Replace(
Content_i,
Pattern_i,
Replacement_i
)
]

subject to the invariant:

[
Body(Content'_i)
================

Body(Content_i)
]

except for explicitly targeted metadata cleanup.

---

# 3. Migration Registry

The migration registry is explicit rather than dynamically inferred.

Each record defines:

```text
filename
legacy tag pattern
canonical replacement tags
```

Conceptually:

```text
MIGRATIONS
   │
   ├── File A
   │     ├── match pattern
   │     └── target tags
   │
   ├── File B
   │     ├── match pattern
   │     └── target tags
   │
   └── ...
```

This preserves deterministic behavior.

---

# 4. RSCF Structural Axes

The target taxonomy includes multiple RSCF structural dimensions.

## Distinction

```text
rscf/D-distinction
```

Used when a note primarily establishes:

```text
identity
classification
difference
inventory boundaries
canonical separation
```

---

# 5. Constraint

```text
rscf/C-constraint
```

Used for:

```text
hard limits
invariants
canon constraints
structural admissibility
```

---

# 6. Relation

```text
rscf/G-relation
```

Used for:

```text
coupling
interconnection
dependency
cross-component relation
```

---

# 7. State

```text
rscf/S-state
```

Used for:

```text
runtime condition
formal state
field state
system state
dynamic configuration
```

---

# 8. Topology

```text
rscf/T-topology
```

Used for:

```text
architecture
graph structure
geometry
connectivity
spatial organization
```

---

# 9. Memory

```text
rscf/M-memory
```

Used for:

```text
persistent knowledge
historical state
lineage
memory architecture
vault persistence
```

---

# 10. Compression

```text
rscf/K-compression
```

Used for:

```text
summarization
representation reduction
bridge compression
structural abstraction
```

---

# 11. Repair

```text
rscf/P-repair
```

Used for:

```text
correction
test repair
integration repair
bridge restoration
structural recovery
```

---

# 12. Mutation

```text
rscf/μ-mutation
```

Used for:

```text
evolution
change
version transition
runtime mutation
architecture modification
```

---

# 13. Boundary

```text
rscf/B-boundary
```

Used for:

```text
memory boundaries
system boundaries
persistence interfaces
access separation
```

---

# 14. Cross-Scale

```text
rscf/X-cross-scale
```

Used for:

```text
multi-level systems
human-system architecture
micro/meso/macro relationships
scale translation
```

---

# 15. Entropy

```text
rscf/E-entropy
```

Used for:

```text
drift
disorder
lacunarity
state degradation
uncertainty accumulation
```

---

# 16. RSCF Type Axis

The target taxonomy also includes artifact-type tags.

Examples include:

```text
rscf/type-model
rscf/type-system
rscf/type-process
rscf/type-evidence
rscf/type-concept
```

These tags answer a different question from the structural axis.

For example:

```text
rscf/M-memory
```

describes the structural dimension.

While:

```text
rscf/type-evidence
```

describes the epistemic/artifact type.

These should not be collapsed into one axis.

---

# 17. Multi-Axis Tagging

A document may carry multiple orthogonal RSCF tags.

Example:

```yaml
tags:
  - rscf/M-memory
  - rscf/S-state
  - rscf/T-topology
  - rscf/type-model
```

This represents:

[
Document=
Memory
+
State
+
Topology
+
ModelType
]

rather than forcing one exclusive category.

---

# 18. Example — AI Cognitive Field

Target note:

```text
2026-08-22 19x19 AI Cognitive Field.md
```

Target tags:

```yaml
tags:
  - ai-cognition
  - attention
  - cognitive-field
  - kernel-routing
  - metacognition
  - rscf/M-memory
  - rscf/type-model
  - strategic-field
```

Primary RSCF interpretation:

```text
Memory + Model
```

---

# 19. Example — Strategic Field Model

Target tags include:

```text
rscf/M-memory
rscf/S-state
rscf/T-topology
rscf/type-model
```

This identifies the note as simultaneously:

```text
persistent structural knowledge
+
field state representation
+
topological system
+
model artifact
```

---

# 20. Example — Canon Completeness Audit

Target tags include:

```text
rscf/C-constraint
rscf/D-distinction
rscf/type-evidence
```

This encodes:

```text
constraint evaluation
+
canonical distinction
+
evidence artifact
```

---

# 21. Example — 7-Part Universe Canon

Target tags include:

```text
rscf/C-constraint
rscf/D-distinction
rscf/Z-collapse
rscf/type-concept
```

The note therefore functions as:

```text
constraint framework
+
distinction system
+
collapse model
+
conceptual canon object
```

---

# 22. Example — Full Brain OS Architecture

Target tags include:

```text
rscf/G-relation
rscf/M-memory
rscf/T-topology
rscf/type-system
```

This identifies the architecture as:

[
System=
Relations
+
Memory
+
Topology
]

---

# 23. Example — Runtime Methods

Target tags include:

```text
rscf/M-memory
rscf/S-state
rscf/type-process
rscf/μ-mutation
```

This distinguishes executable processes from static model notes.

---

# 24. Example — Memory Bridge

Target tags include:

```text
rscf/B-boundary
rscf/M-memory
rscf/type-system
```

The structural interpretation is:

[
MemoryBridge=
Boundary
+
Memory
+
System
]

---

# 25. Example — Brain Inventory

Target tags include:

```text
rscf/D-distinction
rscf/M-memory
rscf/type-evidence
```

Its primary function is therefore:

```text
identify what exists
distinguish artifacts
record memory
provide evidence
```

---

# 26. Example — Formal Systems Invariants

Target tags include:

```text
rscf/C-constraint
rscf/G-relation
rscf/S-state
rscf/type-model
```

This captures:

```text
constraints
+
couplings
+
dynamic state
+
formal model
```

---

# 27. Example — Logic Bridge Registry

Target tags include:

```text
rscf/K-compression
rscf/P-repair
rscf/type-evidence
```

This identifies the bridge registry as both:

```text
compressed structural mapping
```

and:

```text
repair/integration evidence
```

---

# 28. Example — Human System Knowledge Base

Target tags include:

```text
rscf/M-memory
rscf/X-cross-scale
rscf/type-evidence
```

This identifies the note as:

```text
persistent knowledge
+
cross-scale architecture
+
evidence-oriented corpus
```

---

# 29. Example — Trang Phi Framework

Target tags include:

```text
rscf/E-entropy
rscf/M-memory
rscf/S-state
rscf/type-model
```

The resulting structural identity is:

[
TrangPhiFramework=
Entropy
+
Memory
+
State
+
Model
]

---

# 30. Idempotency

The migration must satisfy:

[
\boxed{
M(M(x))=M(x)
}
]

Once a note has:

```text
rscf/*
```

tags and no:

```text
canon-group/*
```

tag, it is considered migrated.

Re-running the migration must not alter it again.

---

# 31. Already-Migrated Detection

The source migration checks the first frontmatter-style tags line:

```python
tags_match = re.search(
    r'^tags: $$([^$$]+)$$',
    content,
    re.MULTILINE,
)
```

A document is treated as already migrated when:

```text
canon-group not present
AND
rscf/ present
```

Conceptually:

[
Migrated(x)
===========

RSCFTagPresent(x)
\land
\neg LegacyCanonGroup(x)
]

---

# 32. Duplicate Legacy Tag Cleanup

The migration also removes:

```yaml
tags: [memory, tag]
```

when encountered as a duplicate metadata line.

This cleanup is secondary to the structural tag migration.

Its purpose is to prevent parallel obsolete tag declarations from surviving the transformation.

---

# 33. File Presence Handling

The migration registry may contain files that are unavailable in the current directory.

The source behavior is:

```text
missing file
→ SKIP
```

rather than:

```text
missing file
→ create new file
```

This preserves the boundary:

[
Migration
\neq
ContentCreation
]

---

# 34. No-Match State

A file may exist while its legacy tag pattern does not match.

The source reports:

```text
NO MATCH
```

This is structurally different from:

```text
ALREADY MIGRATED
```

These states should remain distinct.

Recommended states:

```text
MIGRATED
ALREADY_MIGRATED
FILE_MISSING
PATTERN_MISMATCH
VALIDATION_FAILED
```

---

# 35. Migration State Machine

The migration lifecycle is:

```text
REGISTERED
    ↓
FILE_CHECK
    │
    ├── missing → FILE_MISSING
    │
    ▼
READ
    ↓
CURRENT_TAG_CHECK
    │
    ├── already RSCF → ALREADY_MIGRATED
    │
    ▼
LEGACY_PATTERN_MATCH
    │
    ├── no match → PATTERN_MISMATCH
    │
    ▼
TRANSFORM
    ↓
CLEANUP
    ↓
WRITE
    ↓
MIGRATED
```

---

# 36. Round-Based Execution

The source supports repeated migration rounds:

```text
Round 1
Round 2
Round 3
...
```

with an early stop condition:

[
Changed=0
\Rightarrow
Stop
]

The repeated rounds provide an operational idempotency check.

However:

[
MultipleRounds
\neq
ProofOfCorrectness
]

They only demonstrate that the configured transform eventually reaches a fixed point.

---

# 37. Fixed-Point Condition

The desired migration endpoint is:

[
M(x^*)=x^*
]

where (x^*) contains the target RSCF tags.

This is the metadata fixed point.

---

# 38. Structural Invariants

The migration should preserve the following invariants.

## Invariant 1 — Body preservation

[
Body_{before}=Body_{after}
]

except for explicitly targeted metadata cleanup.

## Invariant 2 — Single structural tag declaration

A migrated note should have one authoritative frontmatter tag field.

## Invariant 3 — Legacy removal

[
canon-group/*
\notin
Tags_{after}
]

for migrated documents.

## Invariant 4 — RSCF presence

[
\exists t\in Tags:
t.startswith("rscf/")
]

## Invariant 5 — Determinism

Identical source content and migration registry must produce identical output.

## Invariant 6 — Idempotency

[
M(M(x))=M(x)
]

---

# 39. RSCF Axis Separation

A central migration rule is:

[
StructuralAxis
\neq
ArtifactType
]

For example:

```text
rscf/M-memory
```

and:

```text
rscf/type-model
```

must remain separate.

Likewise:

```text
rscf/T-topology
```

does not mean:

```text
rscf/type-system
```

The first describes structure.

The second describes artifact class.

---

# 40. Canon Group vs RSCF Axis

Legacy `canon-group/*` tags primarily encode broad filing or family placement.

RSCF axes encode decision-relevant structure.

Thus:

[
CanonGroup
\rightarrow
OrganizationalClassification
]

while:

[
RSCFAxis
\rightarrow
StructuralSemantics
]

The migration is therefore an ontology refinement.

---

# 41. Metadata Ontology

The target metadata model can be represented as:

[
TagSet=
DomainTags
\cup
RSCFAxes
\cup
RSCFType
]

Example:

```yaml
tags:
  - formal-system
  - geometry
  - rscf/M-memory
  - rscf/T-topology
  - rscf/type-model
```

This preserves both domain meaning and RSCF structure.

---

# 42. Provenance Boundary

A successful migration establishes:

```text
the metadata transformation executed
```

It does not independently establish:

```text
the note is scientifically correct
the note is canonical truth
the assigned RSCF axes are semantically perfect
the migrated file has been admitted into runtime authority
```

Therefore:

[
MigrationSuccess
\neq
CanonAdmission
]

---

# 43. Canon Admission Boundary

A migrated note should conceptually pass:

```text
schema validation
semantic validation
provenance validation
version validation
dependency compatibility
authority check
```

before becoming an authoritative control-plane object.

The migration itself performs metadata transformation only.

---

# 44. Migration Authority

The operation mutates persistent Markdown files.

Therefore the effect should be modeled as:

[
WriteEffect(
File,
OldMetadata,
NewMetadata
)
]

A governed runtime should preserve:

```text
file identity
previous state
migration version
migration mapping
timestamp
result
```

---

# 45. Rollback Model

The migration is reversible when the previous metadata is retained.

Conceptually:

[
Rollback(
File_i
)
=

Restore(
Tags_{before}
)
]

Without a backup, revision history, or version-control commit, reversibility is weaker.

---

# 46. Migration Manifest

A mature migration should emit:

```yaml
migration:
  id: rscf-tag-migrate
  version: 1.0
  source_taxonomy: canon-group
  target_taxonomy: rscf-axis

results:
  - file: ...
    before: ...
    after: ...
    state: MIGRATED
```

This separates migration evidence from the files being migrated.

---

# 47. Migration Result Tensor

The migration state can be modeled as:

[
T[
file,
sourceTag,
targetTag,
status,
time,
version,
validation
]
]

Possible status values:

```text
MIGRATED
ALREADY_MIGRATED
MISSING
NO_MATCH
FAILED
```

---

# 48. Selective Failure

A failure on one note should not automatically invalidate successfully migrated unrelated notes.

Thus:

[
Failure(F_i)
\not\Rightarrow
Failure(F_j)
]

unless the migration is explicitly configured as an atomic all-or-nothing transaction.

---

# 49. Atomic Mode

For canon-critical migrations, a stronger execution mode is:

```text
READ ALL
   ↓
VALIDATE ALL
   ↓
TRANSFORM IN MEMORY
   ↓
VALIDATE OUTPUTS
   ↓
COMMIT ALL
```

with:

[
Commit=
\begin{cases}
ALL & \text{if every required file passes}\
NONE & \text{otherwise}
\end{cases}
]

This is stronger than independent per-file writes.

---

# 50. Scope Boundary

The migration applies only to filenames explicitly registered in:

```text
MIGRATIONS
```

Therefore:

[
Scope=
RegisteredFiles
]

and not:

[
Scope=
EntireVault
]

unless the registry is deliberately expanded.

---

# 51. Pattern Boundary

Each migration pattern targets a specific legacy tag structure:

```text
canon-group/...
topic/...
```

A pattern mismatch should not be automatically interpreted as malformed content.

Possible explanations include:

```text
already migrated
frontmatter reformatted
topic slug changed
tag order changed
legacy pattern differs
file version changed
```

Therefore:

```text
NO MATCH
```

should remain an explicit migration state.

---

# 52. Semantic Migration Risk

Regex matching operates on text representation rather than parsed YAML structure.

This introduces possible risks:

```text
tag order sensitivity
formatting sensitivity
multiple tags fields
body text accidentally matching frontmatter-like text
multiline YAML incompatibility
quote differences
```

The current source script is therefore:

```text
TEXT MIGRATION
```

rather than:

```text
FULL YAML-AWARE MIGRATION
```

---

# 53. Recommended Structural Direction

The stronger architectural form is:

```text
Markdown File
    ↓
Frontmatter Detection
    ↓
YAML Parse
    ↓
Tag Schema Validation
    ↓
Legacy Tag Classification
    ↓
RSCF Mapping
    ↓
Canonical Tag Ordering
    ↓
Serialize
    ↓
Postcondition Validation
```

This reduces dependence on formatting-specific regex patterns.

---

# 54. Deterministic Tag Ordering

For reproducible metadata, tags should use a stable ordering policy.

Example:

```text
1. domain tags
2. architecture tags
3. RSCF structural axes
4. RSCF type tag
```

A deterministic ordering function ensures:

[
Serialize(Tags)
]

produces the same text across repeated migrations.

---

# 55. Canonical Tag Uniqueness

A target tag list should satisfy:

[
|Tags|=
|Unique(Tags)|
]

Duplicate tags should be removed without altering semantic meaning.

---

# 56. RSCF Migration Validation

For each migrated file, validation should confirm:

```text
target file exists
legacy canon-group tag removed
expected RSCF tags present
single authoritative tags field exists
body content preserved
document remains valid Markdown
```

---

# 57. Migration Confidence

Migration confidence should depend on:

[
Confidence=
f(
ExactFileMatch,
ExactLegacyMatch,
TargetSchemaPass,
BodyPreservation,
Idempotency
)
]

A successful string replacement alone is weaker evidence than full postcondition validation.

---

# 58. RSCF Status Classes

Migration outcomes may use:

```text
VERIFIED
DERIVED
MODEL
CONDITIONAL
UNKNOWN/GAP
```

Example:

```text
VERIFIED
The migration produced the expected target tags and passed postconditions.

DERIVED
The assigned RSCF structure follows from the migration registry.

MODEL
The RSCF taxonomy itself is an AMOS structural model.

CONDITIONAL
A mapping remains dependent on interpretation of the source note.

UNKNOWN/GAP
The legacy pattern does not match and the correct mapping cannot be determined.
```

---

# 59. Migration Architecture

```text
                         MIGRATION REGISTRY
                                │
                                ▼
                         FILE ENUMERATION
                                │
                                ▼
                         FILE PRESENCE CHECK
                                │
              ┌─────────────────┴─────────────────┐
              │                                   │
           MISSING                              PRESENT
              │                                   │
              ▼                                   ▼
            SKIP                         READ FRONTMATTER
                                                  │
                                                  ▼
                                         MIGRATION CHECK
                                                  │
                         ┌────────────────────────┼─────────────────────┐
                         │                        │                     │
                  ALREADY RSCF               LEGACY MATCH          NO MATCH
                         │                        │                     │
                         ▼                        ▼                     ▼
                       PASS                 TRANSFORM                GAP
                                                  │
                                                  ▼
                                              CLEANUP
                                                  │
                                                  ▼
                                             VALIDATE
                                                  │
                              ┌───────────────────┴───────────────────┐
                              │                                       │
                            PASS                                    FAIL
                              │                                       │
                              ▼                                       ▼
                            WRITE                                  REJECT
                              │
                              ▼
                         MIGRATED STATE
```

---

# 60. Core Migration Equation

The migration can be compressed as:

[
\boxed{
Tags_{t+1}
==========

RSCFMap(
Tags_t,
FileIdentity
)
}
]

subject to:

[
Body_{t+1}=Body_t
]

and:

[
LegacyCanonGroup_{t+1}=0
]

for successfully migrated notes.

---

# 61. Fixed-Point Equation

The desired final state is:

[
\boxed{
RSCFMap(
RSCFMap(T)
)
=

RSCFMap(T)
}
]

This is the principal migration idempotency invariant.

---

# 62. RSCF Master Capsule

```text
CLAIM
The migration converts selected legacy canon-group tags into
explicit RSCF structural-axis and artifact-type metadata.

CLASS
MODEL / MIGRATION PROCESS.

SOURCE
_rscf_tag_migrate migration registry.

LOAD-BEARING COMPONENTS
File identity
→ legacy pattern
→ target RSCF tag set
→ already-migrated detection
→ replacement
→ duplicate cleanup
→ write
→ repeated fixed-point check.

SUPPORTED
The source defines explicit file-to-tag mappings and an
idempotent round-based migration process.

LIMITATIONS
The implementation is regex-based rather than YAML-aware.
Pattern mismatch may result from formatting changes rather
than semantic incompatibility.

NOT ESTABLISHED
Successful migration does not independently prove canon
admission, scientific correctness, or semantic validity of
every assigned structural axis.

PROMOTION CONDITION
Schema validation + semantic review + provenance retention +
postcondition verification.
```

---

# 63. Final Architecture

The migration is best understood as:

[
\boxed{
LegacyTaxonomy
\rightarrow
StructuralRSCFTaxonomy
}
]

with:

[
\boxed{
DocumentMeaning
\ preserved
}
]

and:

[
\boxed{
MetadataSemantics
\ increased
}
]

The target architecture separates:

```text
domain
structure
artifact type
state
topology
memory
constraints
repair
mutation
boundary
cross-scale
entropy
```

rather than relying on a single broad `canon-group/*` classification.

The governing migration invariant is:

[
\boxed{
TransformMetadata
\ without
\ rewritingKnowledge
}
]

---

**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · rscf · AMOS_CORE · AMOS_FULL_BRAIN_OS_Architecture · 2026-08-22 7-Part Universe Canon · 2026-08-22 Brain Inventory · 2026-08-22 Formal Systems Invariants · 2026-08-22 Tests Logic Bridge Registry · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[rscf_MOC]]
