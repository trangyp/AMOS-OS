---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Nei Engine
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

# NEI Engine

## 0. Status

`NEI_ENGINE.md` defines the proposed AMOS OS **NEI**.

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

The NEI (Neuroemotional Intelligence) Engine implements the emotional awareness and autonomic balance domain of the UBI framework.

______________________________________________________________________

## 2. Formal Definition

### 2.1 NEI Domain

NEI covers:
- **Emotional awareness**: recognition and labeling of emotional states
- **Autonomic balance**: parasympathetic/sympathetic regulation
- **Affective regulation**: emotion modulation and recovery

### 2.2 NEI Score

$$\text{NEI} = w_a \cdot \text{Awareness} + w_b \cdot \text{AutonomicBalance} + w_r \cdot \text{Regulation}$$

### 2.3 Vagal Coherence

$$\text{VagalCoherence} = \text{HRV}_{\text{high-freq}} / \text{HRV}_{\text{total}}$$

Vagal coherence is the primary physiological indicator of NEI. High vagal coherence indicates strong autonomic balance.

### 2.4 5-Axis Emotion Model

The NEI Engine uses the AMOS 5-axis emotion model:
- Valence (positive/negative)
- Arousal (calm/excited)
- Dominance (submissive/dominant)
- Certainty (uncertain/certain)
- Sociality (isolated/connected)

### 2.5 SOTA Integration

Recent affective neuroscience research (2024-2026):
- Polyvagal theory extensions (Porges)
- Emotion regulation strategies (Gross framework)
- Interoceptive prediction error (Seth/Friston)
- Cardiac vagal tone as executive function marker

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

node_id: amos_05_cognitive_organism_nei_engine

node_type: ENGINE

path: 05_COGNITIVE_ORGANISM/07_EMOTION_REGULATION/NEI_ENGINE.md

claim_class: AMOS_MODEL

rscf_state: DERIVED

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
