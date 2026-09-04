---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Rscf Structure Validation Receipt
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# RSCF Structure Validation Receipt

Certifies that a knowledge capsule has been validated for structural conformance with the RSCF schema.

________________________________________________________________________

## 1. Validation Contract

This receipt certifies that the target artifact's RSCF fields have been checked for:

- Schema conformance (all required RSCF fields present)
- Typed field validity (field values match declared types)
- Reference integrity (wikilinks point to existing targets)
- Claim class consistency (declared claim_class matches evidence posture)

________________________________________________________________________

## 2. Inputs / Checks Performed

| Check | Description |
|-------|-------------|
| Field presence | `state`, `claim_class`, `provenance`, `scope` are present in YAML frontmatter |
| Type validity | `state` ∈ {SOURCE_CLAIM, OBSERVATION, DERIVED, MODEL, CANON_LAW, CANON_SPEC, …} |
| Claim class validity | `claim_class` ∈ {SOURCE_CLAIM, CANONICAL_INVARIANT, AMOS_MODEL, OBSERVATION, …} |
| Reference check | All wikilinks in RSCF-RELATIONS resolve to existing files |
| Scope declaration | `scope` field is non-empty for material claims |
| Provenance declaration | `provenance` field traces to a known source lineage |

________________________________________________________________________

## 3. Gates

This receipt is emitted at:

- **Commit gate**: Before a material RSCF node enters the canonical knowledge base
- **Evolution gate**: After GMEF mutation — re-validates structural integrity
- **Repair gate**: After rollback or structural repair — confirms schema conformance restored

________________________________________________________________________

## 4. Evidence Required

- YAML frontmatter parsing pass with no schema errors
- Wikilink resolution pass with no unresolved references
- Claim class consistency check (no mismatch between declared class and content posture)

________________________________________________________________________

## 5. What This Receipt Certifies

- The artifact **has** the required RSCF structural fields
- The field values are **type-valid** per the RSCF schema
- References **resolve** to existing artifacts

________________________________________________________________________

## 6. What This Receipt Does NOT Certify

| Limitation | AMOS Invariant |
|-----------|----------------|
| Does NOT certify the claims are true | TEST_PASS ≠ UNIVERSAL_PROOF |
| Does NOT certify provenance is accurate | SOURCE_CLAIM ≠ VERIFIED |
| Does NOT certify the dependency graph is sound | Structural ≠ Semantic validity |
| Does NOT certify scope/regime applicability | Requires separate SCOPE_REGIME_VALIDATION_RECEIPT |
| Does NOT certify the artifact is fit for purpose | Requires separate domain validation |

A receipt documents an **executed validation**, not a universal proof.

________________________________________________________________________

## 7. Integration

- **Control-plane**: This receipt is a prerequisite for the commit gate admission check. An RSCF node without structural validation cannot enter canonical state.
- **Provenance**: Receipt issuance is recorded in the provenance chain of the validated artifact.
- **Rollback**: If structural validity is later found broken, the artifact is rolled back and this receipt is invalidated.
- **Related receipts**: [[01_CANON/01_CORE_LAWS/PROVENANCE_TOPOLOGY_VALIDATION_RECEIPT|PROVENANCE_TOPOLOGY_VALIDATION_RECEIPT]], [[01_CANON/01_CORE_LAWS/SCOPE_REGIME_VALIDATION_RECEIPT|SCOPE_REGIME_VALIDATION_RECEIPT]]

________________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · [[01_CANON/01_CORE_LAWS/L17_RSCF|L17_RSCF]]

**MOC:** [[01_CANON/01_CORE_LAWS/01_CORE_LAWS_MOC|01_CORE_LAWS_MOC]]

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

________________________________________________________________________

RSCF-NODE
node_id: rscf_structure_validation_receipt
node_type: receipt
path: 01_CANON/01_CORE_LAWS/RSCF_STRUCTURE_VALIDATION_RECEIPT.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- VALIDATES: [[01_CANON/01_CORE_LAWS/01_CORE_LAWS_MOC|01_CORE_LAWS_MOC]]
