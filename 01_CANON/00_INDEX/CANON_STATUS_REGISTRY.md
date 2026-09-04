---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Canon Status Registry
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

# Canon Status Registry

## 0. Status

`CANON_STATUS_REGISTRY.md` defines the proposed AMOS OS **Canon Status**.

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

The Canon Status Registry defines the canonical status values that AMOS artifacts can hold, and the valid transitions between them.

______________________________________________________________________

## 2. Formal Definition

### 2.1 Status Values

| Status | Description |
|:---|:---|
| PLACEHOLDER | Structural placeholder, no substantive content |
| SUBSTANTIVE_SPECIFICATION | Has substantive content, not yet promoted |
| PROPOSED_SPECIFICATION | Formally proposed, under review |
| CONDITIONAL | Conditionally canonical, pending validation |
| ACTIVE_CANON_CANDIDATE | Candidate for full canon promotion |
| CANON_LAW | Fully canonical law |
| SUPERSEDED | Replaced by a newer version |
| DEPRECATED | Should no longer be used |
| UNKNOWN/GAP | Status unknown or gap |

### 2.2 Valid Transitions

```text
PLACEHOLDER → SUBSTANTIVE_SPECIFICATION → PROPOSED_SPECIFICATION → CONDITIONAL → ACTIVE_CANON_CANDIDATE → CANON_LAW
                                                                                                    ↓
                                                                                              SUPERSEDED → DEPRECATED
```

### 2.3 No Skip Promotion

$$\text{Promote}(a, s_1, s_2) \implies \text{ValidTransition}(s_1, s_2)$$

Status promotions must follow valid transitions. Skipping levels requires explicit authority.

______________________________________________________________________

## 3. Cross-References

- [[01_CANON/00_INDEX/CANON_MAP|CANON_MAP]]
- [[01_CANON/00_INDEX/INDEX_CANON_README|INDEX_CANON_README]]
- [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]

______________________________________________________________________

## 4. Gaps

- Executable binding NOT_ESTABLISHED
- Canonical status CONDITIONAL
- Automated validation NOT_ESTABLISHED

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

node_id: amos_01_canon_00_index_canon_status_registry

node_type: REGISTRY

path: 01_CANON/00_INDEX/CANON_STATUS_REGISTRY.md

claim_class: AMOS_MODEL

rscf_state: DERIVED

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

______________________________________________________________________

**MOC:** [[01_CANON/00_INDEX/INDEX_CANON_README|INDEX_CANON_README]]
