---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Cross Framework Alias Table
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

# Cross-Framework Alias Table

## 0. Status

`CROSS_FRAMEWORK_ALIAS_TABLE.md` defines the proposed AMOS OS **Cross-Framework Alias** glossary.

This artifact replaces a structural placeholder with substantive content.

```text
PLACEHOLDER != IMPLEMENTED
ADDRESSABLE != VALIDATED
DOCUMENTED != ENFORCED
MODEL != OBSERVATION
SOURCE_CLAIM != VERIFIED
CANON_CANDIDATE != CANONICAL
CANONICAL != EMPIRICAL_TRUTH
CAPABILITY != AUTHORITY
UNKNOWN/GAP != PASS
```

Origin architect / steward: **Trang Phan**

______________________________________________________________________

## 1. Purpose

The Cross-Framework Alias Table maps equivalent terms across different AMOS frameworks, ensuring consistent reference when concepts appear under different names in different canons.

______________________________________________________________________

## 2. Term Definitions

| Term | Definition | Category |
|:---|:---|:---|
| Coherence | Omega: Ω | UBI: — | Trang: — | RSCF: confidence_ceiling | Crosswalk |
| Entropy | Omega: H | UBI: — | Trang: H operator | RSCF: — | Crosswalk |
| Stability | Omega: S | UBI: SI score | Trang: — | RSCF: scope | Crosswalk |
| Reserves | Omega: R | UBI: — | Trang: R (Relation) | RSCF: — | Crosswalk |
| Force | Omega: F | UBI: — | Trang: — | RSCF: — | Crosswalk |
| Distinction | Omega: — | UBI: — | Trang: D | RSCF: — | Crosswalk |
| Memory | Omega: — | UBI: — | Trang: M | RSCF: provenance | Crosswalk |
| Repair | Omega: recovery | UBI: — | Trang: Repair | RSCF: — | Crosswalk |
| Recursion | Omega: cascade | UBI: fractal | Trang: Recursion | RSCF: — | Crosswalk |
| Selection | Omega: — | UBI: — | Trang: Selection | RSCF: — | Crosswalk |
| Collapse | Omega: P_collapse | UBI: τ<0.2 | Trang: Cascade | RSCF: UNKNOWN/GAP | Crosswalk |
| Emergence | Omega: — | UBI: e=i² | Trang: — | RSCF: — | Crosswalk |

______________________________________________________________________

## 3. Usage Notes

- All terms in this glossary are AMOS_MODEL unless otherwise stated
- Terms marked as "Core" are foundational to the framework
- Terms marked as "Alias" are alternative names for canonical terms
- Terms marked as "Crosswalk" map concepts across different canons
- No term in this glossary should be interpreted as empirical truth

______________________________________________________________________

## 4. Cross-References

- See [[01_CANON/06_GLOSSARY/CANONICAL_GLOSSARY|CANONICAL_GLOSSARY]] for the master glossary
- See [[01_CANON/06_GLOSSARY/CANON_ALIASES|CANON_ALIASES]] for canonical aliases
- See [[01_CANON/06_GLOSSARY/DEPRECATED_TERMS|DEPRECATED_TERMS]] for deprecated terminology
- See [[01_CANON/05_VARIABLE_REGISTRY/UNIVERSAL_VARIABLE_REGISTRY|UNIVERSAL_VARIABLE_REGISTRY]] for variable definitions

______________________________________________________________________

## 5. Gaps

- Canonical status CONDITIONAL — proposed specification, not yet promoted to full canon
- Cross-glossary consistency validation NOT_ESTABLISHED
- Automated term resolution NOT_ESTABLISHED

______________________________________________________________________

## 6. Ingestion Rule

```yaml
AMOS_CANON_INGESTION_RULE:
  existing_folder:
    preserve: true
  existing_file:
    preserve: true
    overwrite: false
  new_framework:
    action: ADD_FILE_TO_EXISTING_FOLDER
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

node_id: amos_01_canon_06_glossary_cross_framework_alias_table

node_type: glossary

path: 01_CANON/06_GLOSSARY/CROSS_FRAMEWORK_ALIAS_TABLE.md

claim_class: AMOS_MODEL

rscf_state: DERIVED

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

______________________________________________________________________

**MOC:** [[01_CANON/06_GLOSSARY/06_GLOSSARY_MOC|06_GLOSSARY_MOC]]
