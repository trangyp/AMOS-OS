---
title: "16_SCHEMAS MOC — Schemas & Typed Data Contracts"
type: moc
source: 16_SCHEMAS
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_MOC
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE
    - 00_ROOT/00_ROOT_MOC
  scope: 16_schemas_navigation
tags:
  - amos-os
  - 16_schemas
  - moc
  - navigation
---

# 16_SCHEMAS MOC — Schemas & Typed Data Contracts

**Origin Architect / Steward:** Trang Phan  
**AMOS_CORE Target:** `v4.4`  
**Epistemic Class:** `AMOS_MODEL`

---

## 1. Core Architecture & Navigation

- [[16_SCHEMAS/SCHEMAS_README|SCHEMAS_README]] — Schema taxonomy and validation engines
- [[16_SCHEMAS/06_AGENTS/agent.schema|agent.schema]] — Canonical agent definition schema
- [[16_SCHEMAS/00_INDEX/SCHEMA_MAP|SCHEMA_MAP]] — Schema navigation map

---

## 2. Invariants

```text
CAPABILITY != AUTHORITY
OBSERVED != CURRENT
PROPOSAL != COMMIT
UNKNOWN/GAP != PASS
```

---

## 3. Parent Navigation

- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] — Master Navigation Hub
- [[00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE|FULL_BRAIN_OS_MECE_ARCHITECTURE]] — Full OS Partition Architecture
