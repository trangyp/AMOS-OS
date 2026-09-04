---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Canon Domain Registry
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

# Canon Domain Registry

## 0. Status

`CANON_DOMAIN_REGISTRY.md` defines the proposed AMOS OS **Canon Domain**.

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

The Canon Domain Registry maps canonical artifacts to AMOS domains (C01-C12), ensuring each artifact is properly classified by domain.

______________________________________________________________________

## 2. Formal Definition

### 2.1 Domain Entry

$$\text{Domain}(d) = (\text{domain\_id}, \text{name}, \text{canon\_artifacts}, \text{master\_skill})$$

### 2.2 AMOS Domains

| Domain | Name | Canon Segment |
|:---|:---|:---|
| C01 | Meta Logic | 01_CORE_LAWS |
| C02 | Math & Compute | 05_VARIABLE_REGISTRY |
| C03 | Physics & Cosmos | 02_UNIVERSE_CANON |
| C04 | Bio & Neuro | 03_COGNITION_CANON |
| C05 | Mind & Behavior | 03_COGNITION_CANON |
| C06 | Society & Culture | 02_UNIVERSE_CANON |
| C07 | Econ & Finance | 04_INFRASTRUCTURE_CANON |
| C08 | Strategy & Game | 04_INFRASTRUCTURE_CANON |
| C09 | Org, Law & Policy | 04_INFRASTRUCTURE_CANON |
| C10 | Tech & Engineering | 04_INFRASTRUCTURE_CANON |
| C11 | Design & Language | 06_GLOSSARY |
| C12 | Earth & Ecology | 02_UNIVERSE_CANON |

### 2.3 Domain Coverage

Each domain must have at least one canonical artifact. Domains with no canonical artifacts are UNKNOWN/GAP.

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

node_id: amos_01_canon_00_index_canon_domain_registry

node_type: REGISTRY

path: 01_CANON/00_INDEX/CANON_DOMAIN_REGISTRY.md

claim_class: AMOS_MODEL

rscf_state: DERIVED

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

______________________________________________________________________

**MOC:** [[01_CANON/00_INDEX/INDEX_CANON_README|INDEX_CANON_README]]
