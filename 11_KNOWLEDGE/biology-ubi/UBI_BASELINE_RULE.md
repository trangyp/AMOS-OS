---
title: UBI BASELINE RULE
tags: [biology-ubi]
type: data
source: 11_KNOWLEDGE/biology-ubi
---



```json
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
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]
```

---
**MOC:** [[BIOLOGY-UBI_MOC]]
