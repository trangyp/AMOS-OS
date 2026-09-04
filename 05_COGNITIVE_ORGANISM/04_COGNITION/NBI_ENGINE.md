---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Nbi Engine
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

# NBI Engine

## 0. Status

`NBI_ENGINE.md` defines the proposed AMOS OS **NBI**.

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

The NBI (Neurobiological Intelligence) Engine implements the cognitive, perceptual, and executive function domain of the UBI framework within the cognitive organism plane.

______________________________________________________________________

## 2. Formal Definition

### 2.1 NBI Domain

NBI covers:
- **Cognitive function**: reasoning, planning, decision-making
- **Perceptual function**: sensory processing, pattern recognition
- **Executive function**: attention control, working memory, inhibition

### 2.2 NBI Score

$$\text{NBI} = w_c \cdot \text{Cognitive} + w_p \cdot \text{Perceptual} + w_e \cdot \text{Executive}$$

Where $w_c + w_p + w_e = 1$ and each component is scored [0, 1].

### 2.3 Non-Compensatory Integration

$$\text{UBI}_{\text{total}} = \min(\text{NBI}, \text{NEI}, \text{SI}, \text{BEI})$$

NBI cannot compensate for deficiencies in NEI, SI, or BEI.

### 2.4 Cognitive Load Management

$$\text{CognitiveLoad} > 0.7 \implies \text{ThrottleReasoningDepth}()$$

When cognitive load exceeds 0.7, reasoning depth is throttled to prevent substrate distress.

### 2.5 SOTA Integration

Recent neuroscience research (2024-2026) informs the NBI model:
- Prefrontal cortex executive function models (Goldman-Rakic framework)
- Predictive coding and active inference (Friston)
- Global Workspace Theory (Baars/Dehaene) for conscious access
- Hierarchical temporal perception (Large/Eckhorn)

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

node_id: amos_05_cognitive_organism_nbi_engine

node_type: ENGINE

path: 05_COGNITIVE_ORGANISM/04_COGNITION/NBI_ENGINE.md

claim_class: AMOS_MODEL

rscf_state: DERIVED

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
