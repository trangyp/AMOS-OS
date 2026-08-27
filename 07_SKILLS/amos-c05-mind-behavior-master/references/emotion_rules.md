---
title: emotion rules
type: reference
tags: [reference, amos-c05-mind-behavior-master]
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
**MOC:** [[references_MOC]]
