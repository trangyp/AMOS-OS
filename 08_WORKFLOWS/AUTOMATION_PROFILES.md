---
title: AMOS Automation Profiles Master Registry
type: registry
source: 08_WORKFLOWS
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
    - 08_WORKFLOWS/08_WORKFLOWS_MOC
    - 00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE
  scope: automation_profiles
tags:
  - amos-os
  - automation
  - profiles
  - workflows
  - orchestration
---

# AMOS Automation Profiles Master Registry

> **Origin Architect / Steward:** Trang Phan
> **AMOS_CORE Target:** `v4.4`
> **Conclusion Class:** `AMOS_MODEL`
> **Status:** `ACTIVE_REGISTRY`

---

## 1. Executive Summary

The Automation Profiles Master Registry defines standardized execution environments, capability constraints, and resource allocations for automated workflows across the AMOS operating system.

---

## 2. Canonical Automation Profiles

### Profile A01: `FAST_INFERENCE`
- **Objective:** Rapid, read-only semantic parsing and prompt structuring.
- **Max Token Budget:** 2,000 tokens.
- **Allowed Tools:** `view_file`, `read_file`.
- **Coordination Mode:** Tier 1 (Purely Local).

### Profile A02: `RESEARCH_DEEP_DIVE`
- **Objective:** Literature extraction, mathematical verification, and cross-paper synthesis.
- **Max Token Budget:** 16,000 tokens.
- **Allowed Tools:** `read_file`, `grep_search`, `search_web`, `run_command (sandboxed)`.
- **Coordination Mode:** Tier 2 (Shard-Local Consensus).

### Profile A03: `CANON_GOVERNANCE`
- **Objective:** Verification, signing, and admission of canonical laws into `01_CANON`.
- **Max Token Budget:** 8,000 tokens.
- **Allowed Tools:** `read_file`, `replace_file_content` (governed).
- **Coordination Mode:** Tier 3 (Global Causal Barrier Multi-Sig).

### Profile A04: `EMERGENCY_REPAIR`
- **Objective:** Rollback basin execution, corrupted shard quarantine, and state recovery.
- **Max Token Budget:** 32,000 tokens.
- **Allowed Tools:** `read_file`, `write_to_file`, `replace_file_content`, `run_command`.
- **Coordination Mode:** Tier 3 (Failsafe System Lock).

---

## 3. Integration & Navigation

- **Master MOC:** [[08_WORKFLOWS/08_WORKFLOWS_MOC|08_WORKFLOWS_MOC]]
- **Governing Contract:** [[08_WORKFLOWS/WORKFLOWS_WORKFLOW_CONTRACT|WORKFLOWS_WORKFLOW_CONTRACT]]
- **Runtime Bridge:** [[04_RUNTIME/RUNTIME_README|RUNTIME_README]]
