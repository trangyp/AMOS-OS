---
title: EMOTION RULES
tags:
- emotion
- affect
- mind
- canon/knowledge
type: data
source: 11_KNOWLEDGE/emotion
rscf:
  state: AMOS_MODEL
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: emotion_model
---
# EMOTION RULES

```json
{
  "version": "1.0",
  "description": "Emotion rules linking UBI bands, nervous system state, and context type to emotional posture",
  "rules": {
    "emotion_flow_positive": {
      "id": "emotion_flow_positive",
      "name": "Flow State => Positive Emotion",
      "description": "When nervous system is in flow state, emotion is positive",
      "conditions": {
        "nervous_system_state": "flow"
      },
      "emotion_valence": "positive",
      "emotion_family": "joy",
      "tags": {
        "type": "optimal"
      }
    },
    "emotion_stress_negative": {
      "id": "emotion_stress_negative",
      "name": "High Stress => Negative Emotion",
      "description": "When stress is high, emotion is negative with fear family",
      "conditions": {
        "stress_band": ["high", "very_high"]
      },
      "emotion_valence": "negative",
      "emotion_family": "fear",
      "tags": {
        "type": "stress_response"
      }
    },
    "emotion_balanced_neutral": {
      "id": "emotion_balanced_neutral",
      "name": "Balanced State => Neutral Emotion",
      "description": "When state is balanced, emotion is neutral with care family",
      "conditions": {
        "nervous_system_state": "calm_focus"
      },
      "emotion_valence": "neutral",
      "emotion_family": "care",
      "tags": {
        "type": "balanced"
      }
    }
  }
}

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]
```

---
**MOC:** [[emotion_MOC]]
