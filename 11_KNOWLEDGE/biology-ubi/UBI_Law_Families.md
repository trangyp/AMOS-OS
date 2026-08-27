---
tags: [biology-ubi]
---
{
  "version": "1.0",
  "description": "UBI law families for biological intelligence",
  "law_families": {
    "energy": {
      "id": "energy",
      "name": "Energy Law Family",
      "description": "Laws governing energy levels and capacity",
      "invariants": [
        "minimum_energy_band",
        "energy_restoration_rate"
      ],
      "tags": {
        "domain": "biological",
        "type": "capacity"
      }
    },
    "stress": {
      "id": "stress",
      "name": "Stress Law Family",
      "description": "Laws governing stress levels and management",
      "invariants": [
        "maximum_stress_band",
        "stress_accumulation_rate"
      ],
      "tags": {
        "domain": "biological",
        "type": "regulation"
      }
    },
    "regeneration": {
      "id": "regeneration",
      "name": "Regeneration Law Family",
      "description": "Laws governing regeneration and recovery",
      "invariants": [
        "mandatory_regeneration_windows",
        "regeneration_capacity"
      ],
      "tags": {
        "domain": "biological",
        "type": "recovery"
      }
    },
    "coherence": {
      "id": "coherence",
      "name": "Coherence Law Family",
      "description": "Laws governing system coherence and integration",
      "invariants": [
        "minimum_coherence_threshold"
      ],
      "tags": {
        "domain": "biological",
        "type": "integration"
      }
    },
    "overload": {
      "id": "overload",
      "name": "Overload Law Family",
      "description": "Laws governing overload states and prevention",
      "invariants": [
        "maximum_overload_threshold",
        "overload_recovery_path"
      ],
      "tags": {
        "domain": "biological",
        "type": "safety"
      }
    }
  }
}

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
