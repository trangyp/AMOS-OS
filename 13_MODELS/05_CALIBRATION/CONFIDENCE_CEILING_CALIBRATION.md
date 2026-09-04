---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Confidence Ceiling Calibration
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

# Confidence Ceiling Calibration

## 0. Status

`CONFIDENCE_CEILING_CALIBRATION.md` defines the proposed AMOS OS **Confidence Ceiling**.

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

The Confidence Ceiling Calibration defines the maximum confidence allowed for claims based on their RSCF state and provenance.

______________________________________________________________________

## 2. Formal Definition

### 2.1 Confidence Ceiling Formula

$$\text{ConfidenceCeiling}(c) = f(\text{state}(c), \text{provenance\_independence}(c))$$

### 2.2 Ceiling by State

| RSCF State | Max Confidence |
|:---|:---|
| SOURCE_CLAIM | 0.3 |
| OBSERVATION | 0.5 |
| DERIVED | 0.6 |
| MODEL | 0.7 |
| DECISION | 0.8 |
| CANONICAL_INVARIANT | 1.0 |

### 2.3 Independence Adjustment

$$\text{AdjustedConfidence} = \text{ConfidenceCeiling} \cdot \text{IndependenceFactor}$$

Where IndependenceFactor = 1.0 for independent sources, 0.5 for partially independent, 0.0 for non-independent.

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

node_id: amos_13_models_confidence_ceiling_calibration

node_type: MODEL

path: 13_MODELS/05_CALIBRATION/CONFIDENCE_CEILING_CALIBRATION.md

claim_class: AMOS_MODEL

rscf_state: DERIVED

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
