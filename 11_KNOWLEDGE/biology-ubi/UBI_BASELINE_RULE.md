---
tags: [biology-ubi]
---
{
  "id": "ubi.rule.baseline",
  "name": "UBI Baseline Rule",
  "description": "Baseline rule for UBI state initialization and integrity checks. Ensures UBI state is properly initialized and within bounds.",
  "layer_id": "ubi",
  "domain_id": "regulation",
  "tags": {
    "family": "ubi",
    "kind": "rule",
    "type": "baseline"
  },
  "invariant_ids": ["ubi.integrity.bounds"],
  "operator_ids": ["ubi.operator.recompute_integrity"],
  "priority": 1.0
}

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
