---
title: UBI IMMUNE INTEGRITY
tags: [biology-ubi]
type: data
source: 11_KNOWLEDGE/biology-ubi
---



```json
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
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]
```

---
**MOC:** [[BIOLOGY-UBI_MOC]]
