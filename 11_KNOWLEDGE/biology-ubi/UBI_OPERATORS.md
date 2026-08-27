---
title: UBI OPERATORS
tags: [biology-ubi]
type: data
source: 11_KNOWLEDGE/biology-ubi
---



```json
{
  "version": "1.0",
  "description": "UBI operators for biological intelligence",
  "operators": {
    "op.recommend_rest": {
      "id": "op.recommend_rest",
      "name": "Recommend Rest",
      "description": "Recommends rest when energy is low or stress is high",
      "conditions": {
        "energy_band": "low",
        "or": {
          "stress_band": ["high", "very_high"]
        }
      },
      "action": "recommend_rest",
      "tags": {
        "domain": "biological",
        "type": "recommendation"
      }
    },
    "op.recommend_focus_shift": {
      "id": "op.recommend_focus_shift",
      "name": "Recommend Focus Shift",
      "description": "Recommends shifting focus when overload is detected",
      "conditions": {
        "overload_detected": true
      },
      "action": "recommend_focus_shift",
      "tags": {
        "domain": "biological",
        "type": "recommendation"
      }
    },
    "op.recommend_break_pattern": {
      "id": "op.recommend_break_pattern",
      "name": "Recommend Break Pattern",
      "description": "Recommends breaking current pattern when stress accumulates",
      "conditions": {
        "stress_accumulation": "high",
        "pattern_duration": "long"
      },
      "action": "recommend_break_pattern",
      "tags": {
        "domain": "biological",
        "type": "recommendation"
      }
    }
  }
}

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]
```

---
**MOC:** [[BIOLOGY-UBI_MOC]]
