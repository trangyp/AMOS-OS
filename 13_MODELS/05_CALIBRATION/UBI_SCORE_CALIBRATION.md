---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Ubi Score Calibration
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

# UBI Score Calibration

## 0. Status

`UBI_SCORE_CALIBRATION.md` defines the proposed AMOS OS **UBI Score**.

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

The UBI Score Calibration defines the calibration protocol for UBI domain scoring.

______________________________________________________________________

## 2. Formal Definition

### 2.1 Calibration Protocol

1. Establish baseline UBI scores through diagnostic assessment
2. Validate scoring against wearable telemetry data
3. Cross-validate with clinical assessment (if available)
4. Track score stability over time
5. Adjust scoring weights based on validation evidence

### 2.2 Score Range

Each UBI domain is scored [0, 1]:
- 0.0-0.3: Distressed — recovery mode required
- 0.3-0.5: Below baseline — regulation needed
- 0.5-0.7: Baseline — normal operation
- 0.7-1.0: Optimal — enhanced capacity

### 2.3 Non-Compensatory Verification

$$\text{UBI}_{\text{total}} = \min(\text{NBI}, \text{NEI}, \text{SI}, \text{BEI})$$

Calibration must verify that the non-compensatory property holds — no domain can compensate for another.

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

node_id: amos_13_models_ubi_score_calibration

node_type: MODEL

path: 13_MODELS/05_CALIBRATION/UBI_SCORE_CALIBRATION.md

claim_class: AMOS_MODEL

rscf_state: DERIVED

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
