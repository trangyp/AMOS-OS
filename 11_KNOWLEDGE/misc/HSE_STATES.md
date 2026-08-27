---
title: HSE STATES
tags: [misc, reference, general, canon/knowledge]
type: data
source: 11_KNOWLEDGE/misc
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general

---
# HSE STATES

```json
{
  "version": "1.0",
  "description": "HSE behavioural states (subset of ~200 micro-states)",
  "states": [
    {
      "id": "baseline",
      "name": "Baseline State",
      "family": "habit",
      "stability_band": "medium",
      "load_band": "medium",
      "drift_tendency": 0.3,
      "tags": {
        "type": "stable"
      }
    },
    {
      "id": "crisis_acute",
      "name": "Acute Crisis",
      "family": "crisis",
      "stability_band": "low",
      "load_band": "very_high",
      "drift_tendency": 0.9,
      "tags": {
        "type": "crisis",
        "requires_intervention": "true"
      }
    },
    {
      "id": "recovery_early",
      "name": "Early Recovery",
      "family": "recovery",
      "stability_band": "low",
      "load_band": "high",
      "drift_tendency": 0.6,
      "tags": {
        "type": "recovery",
        "fragile": "true"
      }
    },
    {
      "id": "recovery_stable",
      "name": "Stable Recovery",
      "family": "recovery",
      "stability_band": "medium",
      "load_band": "medium",
      "drift_tendency": 0.4,
      "tags": {
        "type": "recovery",
        "stable": "true"
      }
    },
    {
      "id": "drift_mild",
      "name": "Mild Drift",
      "family": "drift",
      "stability_band": "medium",
      "load_band": "medium",
      "drift_tendency": 0.7,
      "tags": {
        "type": "drift",
        "correctable": "true"
      }
    },
    {
      "id": "drift_severe",
      "name": "Severe Drift",
      "family": "drift",
      "stability_band": "low",
      "load_band": "high",
      "drift_tendency": 0.9,
      "tags": {
        "type": "drift",
        "requires_intervention": "true"
      }
    }
  ]
}

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]
```

---
**MOC:** [[MISC_MOC]]
