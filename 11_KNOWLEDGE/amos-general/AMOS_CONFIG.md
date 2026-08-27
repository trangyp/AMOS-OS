---
title: AMOS CONFIG
tags: [canon-group/biology, canon/framework, rscf/claim, rscf/provenance, rscf/state/source-claim, topic/amos-config, amos-general]
type: data
source: 11_KNOWLEDGE/amos-general
---



```json
{
  "version": "0.1.0",
  "created_at": "2025-12-04T06:50:43.934407Z",
  "project_root": ".",
  "logs_dir": "logs",
  "memory_dir": "memory",
  "workers": {
    "code_worker": {
      "module": "workers",
      "callable": "code_worker"
    },
    "analyst": {
      "module": "workers",
      "callable": "analyst_worker"
    },
    "auditor": {
      "module": "workers",
      "callable": "auditor_worker"
    },
    "planner": {
      "module": "workers",
      "callable": "planner_worker"
    }
  }
}

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]
```

---
**MOC:** [[AMOS-GENERAL_MOC]]
