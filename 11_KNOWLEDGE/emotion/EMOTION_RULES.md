---
tags: [emotion]
---
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
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
