---
title: "AMOS Automation Profiles Master Registry"
type: registry
source: 11_KNOWLEDGE
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_REGISTRY
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - AMOS-UNIVERSE/automation_profiles.json
  scope: automation_profiles
tags:
  - amos-os
  - automation
  - profiles
  - workflows
---

# AMOS Automation Profiles Master Registry

> **Origin Architect / Steward:** Trang Phan  
> **AMOS_CORE Target:** `v4.4`  
> **Conclusion Class:** `AMOS_MODEL`

## 1. Profiles Specification

```json
{
  "profiles": {
    "DAILY_CORE": {
      "description": "Daily self-checks across AMOS OS, cognition, and life-systems planning.",
      "tasks": [
        "BIOLOGICAL_DAILY_SUMMARY",
        "WORK_DAY_FOCUS_PLAN",
        "OS_DAILY_INTEGRITY_SCAN",
        "COGNITION_DAILY_REFLECTION"
      ],
      "schedule_hint": "daily"
    },
    "WEEKLY_STRATEGIC": {
      "description": "Weekly strategic planning across all 10 bands and 150 domains.",
      "tasks": [
        "DOMAIN_BAND_PROGRESS_SUMMARY",
        "WEEKLY_OBJECTIVES_PLAN",
        "SYSTEMIC_RISK_REVIEW",
        "UBI_CANON_EXTENSION"
      ],
      "schedule_hint": "weekly"
    },
    "OS_MAINTENANCE": {
      "description": "Regular AMOS OS maintenance and self-repair routines.",
      "tasks": [
        "FULL_SYSTEM_AUDIT",
        "LOOPS_STABILITY_CHECK",
        "IMPORTS_INTEGRITY_CHECK",
        "MEMORY_INDEX_COMPACTION"
      ],
      "schedule_hint": "interval"
    },
    "OS_EVOLUTION": {
      "description": "Structured evolution of cognition, domain canon, and automation rules.",
      "tasks": [
        "COGNITION_BLUEPRINT_UPGRADE",
        "DOMAIN_CANON_REVIEW",
        "AUTOMATION_RULES_REFINEMENT",
        "MODE_CONSTRAINTS_AUDIT"
      ],
      "schedule_hint": "weekly"
    }
  }
}
```

## 2. Integration & Execution

- **Governed By:** [[08_WORKFLOWS/08_WORKFLOWS_MOC|08_WORKFLOWS_MOC]]
- **Executed In:** [[04_RUNTIME/RUNTIME_README|RUNTIME_README]]
