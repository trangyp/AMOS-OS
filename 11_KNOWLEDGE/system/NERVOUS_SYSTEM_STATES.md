---
title: NERVOUS SYSTEM STATES
tags: [system, architecture, design, canon/knowledge]
type: data
source: 11_KNOWLEDGE/system
rscf:
  state: AMOS_MODEL
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: system_design
---
# NERVOUS SYSTEM STATES

```json
{
  "version": "1.0",
  "description": "Nervous system state patterns for UBI",
  "states": {
    "calm_focus": {
      "id": "calm_focus",
      "name": "Calm Focus",
      "description": "Balanced state with good focus capacity",
      "sympathetic_activation": 0.5,
      "parasympathetic_activation": 0.5,
      "vagal_tone_band": "medium",
      "somatic_tension_band": "low",
      "interoceptive_clarity_band": "medium",
      "tags": {
        "type": "balanced",
        "optimal": "true"
      }
    },
    "hyper_vigilance": {
      "id": "hyper_vigilance",
      "name": "Hyper-Vigilance",
      "description": "High stress, low energy state with hyper-vigilance",
      "sympathetic_activation": 0.8,
      "parasympathetic_activation": 0.2,
      "vagal_tone_band": "low",
      "somatic_tension_band": "high",
      "interoceptive_clarity_band": "low",
      "tags": {
        "type": "stress",
        "requires_rest": "true"
      }
    },
    "shutdown": {
      "id": "shutdown",
      "name": "Shutdown Tendency",
      "description": "Low energy, low activation state",
      "sympathetic_activation": 0.2,
      "parasympathetic_activation": 0.8,
      "vagal_tone_band": "high",
      "somatic_tension_band": "low",
      "interoceptive_clarity_band": "low",
      "tags": {
        "type": "low_energy",
        "requires_regeneration": "true"
      }
    },
    "flow": {
      "id": "flow",
      "name": "Flow State",
      "description": "High energy, low stress flow state",
      "sympathetic_activation": 0.6,
      "parasympathetic_activation": 0.4,
      "vagal_tone_band": "high",
      "somatic_tension_band": "low",
      "interoceptive_clarity_band": "high",
      "tags": {
        "type": "optimal",
        "optimal": "true"
      }
    },
    "somatic_overload": {
      "id": "somatic_overload",
      "name": "Somatic Overload",
      "description": "High somatic tension and overload",
      "sympathetic_activation": 0.9,
      "parasympathetic_activation": 0.1,
      "vagal_tone_band": "low",
      "somatic_tension_band": "very_high",
      "interoceptive_clarity_band": "low",
      "tags": {
        "type": "overload",
        "requires_rest": "true"
      }
    }
  }
}

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]
```

---
**MOC:** [[SYSTEM_MOC]]

---
**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
