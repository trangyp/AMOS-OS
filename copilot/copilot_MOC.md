---
title: Copilot Subplane MOC
type: moc
source: copilot
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_SPECIFICATION
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 00_ROOT/00_ROOT_MOC
  scope: copilot_governance
tags:
  - amos-os
  - copilot
  - moc
---

# Copilot Subplane MOC

> **Origin Architect / Steward:** Trang Phan
> **AMOS_CORE Target:** `v4.4`
> **Status:** `ACTIVE_SPECIFICATION`

---

## 1. Scope & Purpose
`copilot/copilot_MOC` governs the interactions, historical agent conversation transcripts, and skill definitions utilized during paired Copilot/Agent sessions across the AMOS OS vault.

---

## 2. Directory Structure & Sub-Components
- `copilot/skills/` — Special skill cheat sheets and extension references.
- `copilot/copilot-conversations/` — Historical session transcripts and execution logs.
- `copilot/copilot-custom-prompts/` — Prompt templates and system prompts.

---

## 3. Governance Bindings
- Root MOC: [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
- Agent Governance Contract: [[AGENTS|AGENTS]]
