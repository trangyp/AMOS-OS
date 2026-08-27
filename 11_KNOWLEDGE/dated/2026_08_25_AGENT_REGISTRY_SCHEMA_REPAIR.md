---
title: 2026-08-25 Agent Registry Schema Repair
type: daily-learning
date: 2026-08-25
epistemic: DERIVED
tags: [integrity, agents, schema, dated, dated/2026-08-25]
---


# 2026-08-25 — Agent Registry Schema Repair

## Defect found

Integrity sweep of all 607 agent JSONs found **26 invalid entries**:
- 25 used a divergent schema (`purpose` instead of `description`; `capabilities` as free-text string or list-of-dicts) from the vault_consolidation generator
- 1 had literal name `"0"` (amos-quantum-enhanced-tensor-field-agent) — collision-prone and unsearchable

## Repair

- 22 files: `description` derived from `purpose`/display_name+capabilities; written back valid
- 1 file renamed `0.json` → `amos-quantum-enhanced-tensor-field-agent.json` (content preserved, name fixed)
- 4 files already had descriptions after purpose-merge
- Re-verified: **607/607 agents parse with name + description present**

## Lesson

Generators drift in schema even within one session's outputs. The registry-level invariant "every agent has name + description" should be a standing check in the brain-consistency audit.

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[DATED_MOC]]
