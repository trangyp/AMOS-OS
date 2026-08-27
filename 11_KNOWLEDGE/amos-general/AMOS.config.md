---
tags: [canon-group/biology, canon/framework, rscf/claim, rscf/provenance, rscf/state/source-claim, topic/amos-config, amos-general]
---

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
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
