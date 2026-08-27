---
tags: [biology-ubi]
---
{
  "id": "ubi.immune.integrity",
  "name": "Immune System Integrity",
  "description": "Invariant: Immune system integrity score must be in [0.0, 1.0]. This is a computational metric, not a medical assessment.",
  "layer_id": "ubi",
  "domain_id": "repair",
  "tags": {
    "family": "ubi",
    "kind": "invariant",
    "type": "system",
    "system": "immune"
  },
  "constraints": [
    "immune.activation_level ∈ [0.0, 1.0]",
    "immune.threat_index ∈ [0.0, 1.0]",
    "immune.recovery_capacity ∈ [0.0, 1.0]",
    "immune.integrity_score() ∈ [0.0, 1.0]"
  ]
}

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
