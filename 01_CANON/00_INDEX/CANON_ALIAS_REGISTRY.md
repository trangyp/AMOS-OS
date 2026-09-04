---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Canon Alias Registry
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

# Canon Alias Registry

## 0. Status

`CANON_ALIAS_REGISTRY.md` defines the proposed AMOS OS **Canon Alias**.

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

The Canon Alias Registry records alternative names for canonical AMOS artifacts, ensuring search and reference consistency.

______________________________________________________________________

## 2. Formal Definition

### 2.1 Alias Entry

$$\text{Alias}(a) = (\text{alias}, \text{canonical\_name}, \text{type})$$

### 2.2 Registered Aliases

| Alias | Canonical Name | Type |
|:---|:---|:---|
| Full Brain OS | AMOS Brain Master OS | PRODUCT |
| Super Mind OS | AMOS Engines Master | PRODUCT |
| Omega Infinity Stack | Omega Quantum Stack | PRODUCT |
| Rule of Two | Rule of 2 (R2) | LAW |
| Rule of Four | Rule of 4 (R4) | LAW |
| Khung Trang | Trang Architecture | FRAMEWORK |
| Phuong Phap Trang | Trang Method | METHOD |
| MURK | Absolute Logic Kernel | COMPONENT |

### 2.3 Alias Resolution

All references using aliases must resolve to the canonical name. Unresolved aliases are UNKNOWN/GAP.

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

node_id: amos_01_canon_00_index_canon_alias_registry

node_type: REGISTRY

path: 01_CANON/00_INDEX/CANON_ALIAS_REGISTRY.md

claim_class: AMOS_MODEL

rscf_state: DERIVED

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

______________________________________________________________________

**MOC:** [[01_CANON/00_INDEX/INDEX_CANON_README|INDEX_CANON_README]]
