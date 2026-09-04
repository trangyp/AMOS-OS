---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Amos Core Version Lineage
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

# AMOS Core Version Lineage

## 0. Status

`AMOS_CORE_VERSION_LINEAGE.md` defines the proposed AMOS OS **AMOS Core Version** registry.

This artifact replaces a structural placeholder with substantive content.

```text
PLACEHOLDER != IMPLEMENTED
ADDRESSABLE != VALIDATED
DOCUMENTED != ENFORCED
MODEL != OBSERVATION
SOURCE_CLAIM != VERIFIED
CANON_CANDIDATE != CANONICAL
CAPABILITY != AUTHORITY
UNKNOWN/GAP != PASS
```

Origin architect / steward: **Trang Phan**

______________________________________________________________________

## 1. Purpose

The AMOS Core Version Lineage registry records the complete version history of AMOS Core, from v3.0 through v4.4, preserving the predecessor/successor chain, changesets, and promotion records.

______________________________________________________________________

## 2. Formal Definition

### 2.1 Version Chain

```text
v3.0 → v3.1 → v3.2 → v4.0 → v4.1 → v4.2 → v4.3 → v4.4 (current authoritative)
```

### 2.2 Version Record

Each version record contains:
- `version`: semantic version
- `predecessor`: previous version
- `successor`: next version (or null if current)
- `changeset`: summary of changes
- `promotion_authority`: who authorized the promotion
- `promotion_date`: when promoted
- `validation_receipts`: references to validation evidence
- `status`: ACTIVE, SUPERSEDED, or DEPRECATED

### 2.3 Authoritative Version

$$\text{Authoritative}(v) \iff v = 4.4 \wedge \text{PromotionRecord}(v) \text{ is valid}$$

### 2.4 Non-Promotion Rule

Versions v4.5-v4.17 are historical consolidation labels, NOT promoted canonical successors. A version is canonical only if it has:
- Explicit predecessor/successor chain
- Source version and hash
- Changeset documentation
- Validation/regression evidence
- Authority/promotion record
- Supersession lineage

______________________________________________________________________

## 3. Application

This registry is used by:
- [[02_KERNEL/K_MEMORY_RETRIEVAL|K_MEMORY_RETRIEVAL]] — for supersession-aware retrieval
- [[01_CANON/07_PROVENANCE/CANON_PROVENANCE|CANON_PROVENANCE]] — for provenance chain validation
- [[01_CANON/08_SUPERSESSION/ACTIVE_VS_LEGACY_CANON|ACTIVE_VS_LEGACY_CANON]] — for active/legacy classification
- [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] — for law hierarchy enforcement

______________________________________________________________________

## 4. Gaps

- Executable binding NOT_ESTABLISHED
- Canonical status CONDITIONAL
- Automated supersession validation NOT_ESTABLISHED

______________________________________________________________________

## 5. Ingestion Rule

```yaml
AMOS_CANON_INGESTION_RULE:
  existing_file:
    preserve: true
    overwrite: false
  uncertainty:
    action:
      - MARK_GAP_OR_COMPETING
      - NEVER_INVENT_CANON
```

______________________________________________________________________

[[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] · [[00_ROOT/AMOS MOC|AMOS MOC]]

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

______________________________________________________________________

RSCF-NODE

node_id: amos_01_canon_08_supersession_amos_core_version_lineage

node_type: REGISTRY

path: 01_CANON/08_SUPERSESSION/AMOS_CORE_VERSION_LINEAGE.md

claim_class: AMOS_MODEL

rscf_state: DERIVED

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

______________________________________________________________________

**MOC:** [[01_CANON/08_SUPERSESSION/08_SUPERSESSION_MOC|08_SUPERSESSION_MOC]]
