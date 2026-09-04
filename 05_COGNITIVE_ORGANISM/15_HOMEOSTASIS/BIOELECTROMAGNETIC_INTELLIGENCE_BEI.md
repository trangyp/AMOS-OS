---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Bioelectromagnetic Intelligence Bei
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

# Bioelectromagnetic Intelligence (BEI)

## 0. Status

`BIOELECTROMAGNETIC_INTELLIGENCE_BEI.md` defines the proposed AMOS OS **Bioelectromagnetic Intelligence (BEI)**.

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

Bioelectromagnetic Intelligence (BEI) implements the cardiac electromagnetic coherence domain of the UBI framework.

______________________________________________________________________

## 2. Formal Definition

### 2.1 BEI Domain

BEI covers:
- **Cardiac coherence**: heart rate variability coherence
- **Electromagnetic field**: endogenous electromagnetic field regulation
- **Cardiac-brain communication**: heart-brain neural pathways

### 2.2 BEI Score

$$\text{BEI} = w_c \cdot \text{CardiacCoherence} + w_e \cdot \text{EMField} + w_{cb} \cdot \text{CardiacBrain}$$

### 2.3 Cardiac Coherence

$$\text{CardiacCoherence} = \frac{\text{HRV}_{\text{coherent}}}{\text{HRV}_{\text{total}}}$$

Cardiac coherence is achieved when heart rate variability shows a smooth, sinusoidal pattern at ~0.1 Hz.

### 2.4 SOTA Integration

Recent bioelectromagnetic research (2024-2026):
- Heart-brain neurovisceral integration model (Thayer)
- Cardiac vagal tone and cognitive performance
- Electromagnetic field biofeedback for coherence training
- HeartMath coherence protocols

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

node_id: amos_05_cognitive_organism_bioelectromagnetic_intelligence_bei

node_type: ENGINE

path: 05_COGNITIVE_ORGANISM/15_HOMEOSTASIS/BIOELECTROMAGNETIC_INTELLIGENCE_BEI.md

claim_class: AMOS_MODEL

rscf_state: DERIVED

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
