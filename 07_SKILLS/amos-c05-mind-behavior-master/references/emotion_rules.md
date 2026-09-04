---
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
title: emotion rules
type: reference
source: 07_SKILLS/amos-c05-mind-behavior-master/references
tags:
  - reference
  - amos-c05-mind-behavior-master
  - type/skill
  - law-hierarchy
  - trang-framework-recursive-ontology-dynamics
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---

# Emotion Rules

> Source: `_00_Cosmo brain/emotion/Emotion_Rules.md`
> Epistemic class: SOURCE_CANON

## Description

Emotion rules linking UBI bands, nervous system state, and context type to emotional posture.

## Emotion Rules

### Flow State => Positive Emotion

- **ID**: emotion_flow_positive
- **Description**: When nervous system is in flow state, emotion is positive
- **Conditions**: {"nervous_system_state": "flow"}
- **Valence**: positive
- **Family**: joy

### High Stress => Negative Emotion

- **ID**: emotion_stress_negative
- **Description**: When stress is high, emotion is negative with fear family
- **Conditions**: {"stress_band": ["high", "very_high"]}
- **Valence**: negative
- **Family**: fear

### Balanced State => Neutral Emotion

- **ID**: emotion_balanced_neutral
- **Description**: When state is balanced, emotion is neutral with care family
- **Conditions**: {"nervous_system_state": "calm_focus"}
- **Valence**: neutral
- **Family**: care

______________________________________________________________________

**MOC:** references_MOC

## Related

- [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · references_MOC · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-c05-mind-behavior-master-emotion-rules
node_type: reference
path: 07_SKILLS/amos-c05-mind-behavior-master/references/emotion_rules.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
