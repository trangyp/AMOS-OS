---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Ubi Model Registry
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

# UBI Model Registry

## 0. Status

`UBI_MODEL_REGISTRY.md` defines the proposed AMOS OS **UBI**.

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

The UBI Model Registry catalogs all models used in the Unified Biological Intelligence framework.

______________________________________________________________________

## 2. Formal Definition

### 2.1 Registered UBI Models

| Model | Domain | Status |
|:---|:---|:---|
| NBI Scoring | Neurobiological | CONDITIONAL |
| NEI Scoring | Neuroemotional | CONDITIONAL |
| SI Scoring | Somatic | CONDITIONAL |
| BEI Scoring | Bioelectromagnetic | CONDITIONAL |
| UBI Total | Non-compensatory composite | CONDITIONAL |
| Substrate Distress | Safety veto | CONDITIONAL |
| Quadratic Emergence | Interaction model | CONDITIONAL |
| 40Hz Clock | Synchronization | CONDITIONAL |

### 2.2 Model Authority

All UBI models trace to Trang Phan as origin architect.

### 2.3 Non-Compensatory Invariant

$$\text{UBI}_{\text{total}} = \min(\text{NBI}, \text{NEI}, \text{SI}, \text{BEI})$$

This invariant is preserved across all registered models.

______________________________________________________________________

## 3. Cross-References

- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
- [[00_ROOT/AMOS MOC|AMOS MOC]]
- [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

______________________________________________________________________

## 4. Gaps

- Executable binding NOT_ESTABLISHED
- Canonical status CONDITIONAL
- Automated enforcement NOT_ESTABLISHED

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

node_id: amos_13_models_ubi_model_registry

node_type: MODEL

path: 13_MODELS/04_DOMAIN/UBI_MODEL_REGISTRY.md

claim_class: AMOS_MODEL

rscf_state: DERIVED

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
