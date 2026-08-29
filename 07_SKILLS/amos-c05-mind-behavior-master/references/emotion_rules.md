---
title: emotion rules
type: reference
source: 07_SKILLS/amos-c05-mind-behavior-master/references
tags:
- reference
- amos-c05-mind-behavior-master
- canon/skill
- references-moc
- 07-skills-moc
- 00-home
- amos-rscf-nodes
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

---
**MOC:** references_MOC

## Related

- [[07_SKILLS_MOC]]
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · references_MOC · [[07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-c05-mind-behavior-master-emotion-rules
node_type: reference
path: 07_SKILLS/amos-c05-mind-behavior-master/references/emotion_rules.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
