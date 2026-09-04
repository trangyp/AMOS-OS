---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Somatic Intelligence Si
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

# Somatic Intelligence (SI)

## 0. Status

`SOMATIC_INTELLIGENCE_SI.md` defines the proposed AMOS OS **Somatic Intelligence (SI)**.

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

Somatic Intelligence (SI) implements the body awareness and interoceptive accuracy domain of the UBI framework.

______________________________________________________________________

## 2. Formal Definition

### 2.1 SI Domain

SI covers:
- **Body awareness**: proprioception, kinesthesia
- **Interoceptive accuracy**: sensing internal body states
- **Somatic regulation**: body-based emotional regulation

### 2.2 SI Score

$$\text{SI} = w_b \cdot \text{BodyAwareness} + w_i \cdot \text{InteroceptiveAccuracy} + w_s \cdot \text{SomaticRegulation}$$

### 2.3 Interoceptive Accuracy Test

The heartbeat counting task is the canonical interoceptive accuracy measure:
$$\text{IA} = 1 - \frac{|\text{Reported} - \text{Actual}|}{\text{Actual}}$$

### 2.4 SOTA Integration

Recent interoception research (2024-2026):
- Interoceptive inference and predictive coding (Seth)
- Embodied cognition frameworks (Varela/Thompson)
- Gut-brain axis and microbiome influence on interoception
- Somatic markers in decision-making (Damasio)

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

node_id: amos_05_cognitive_organism_somatic_intelligence_si

node_type: ENGINE

path: 05_COGNITIVE_ORGANISM/15_HOMEOSTASIS/SOMATIC_INTELLIGENCE_SI.md

claim_class: AMOS_MODEL

rscf_state: DERIVED

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
