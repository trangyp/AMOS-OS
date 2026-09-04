---
title: 06_AGENTS — Master Map of Content
type: moc
source: 06_AGENTS
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
  scope: agents_navigation
tags:
  - amos-os
  - agents
  - moc
  - agent-schema
---

# 06_AGENTS — Master Map of Content

**Origin Architect / Steward:** Trang Phan
**Target Core Lineage:** `v4.4`
**Epistemic Class:** `AMOS_MODEL`

---

## 1. Core Architecture & Contracts

- [[06_AGENTS/AGENTS_README|AGENTS_README]] — Agent classification, lifecycle, and runtime boundaries
- [[06_AGENTS/AGENTS_AGENT_CONTRACT|AGENTS_AGENT_CONTRACT]] — Invariants, non-escalation, and authority gates
- [[06_AGENTS/AMOS_AGENT_SCHEMA_FULL|AMOS_AGENT_SCHEMA_FULL]] — Canonical construction schema (v3.0.0)
- [[06_AGENTS/AGENT_ROLE_REGISTRY|AGENT_ROLE_REGISTRY]] — Definitive role taxonomy across all 26 planes
- SPECIALIST_AGENT_CATALOG — Specialist agent definitions (QFM, Canon, Legal, Flow)

---

## 2. Invariants

```text
AGENT != IDENTITY_OWNER
CAPABILITY != AUTHORITY
DELEGATION != ESCALATION
UNKNOWN/GAP != PASS
```

---

## 3. Specialist Sub-Planes & Agents

- `amos-flow-auditor-agent/` — End-to-end task audit and state verification
- `amos-law-stack-gate-agent/` — Canon law compliance and invariant enforcement
- `amos-qfm-paper-agents/` — Quantum and mathematical literature extraction specialists
- `amos-7-part-universe-canon-agent/` — Universe canon coherence validator

---

## 4. Master Navigation

- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] — Root navigation hub
- [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]] — Executable capabilities bound to agents
- [[09_PROTOCOLS/09_PROTOCOLS_MOC|09_PROTOCOLS_MOC]] — Inter-agent handoff protocols
- [[18_SECURITY/18_SECURITY_MOC|18_SECURITY_MOC]] — Capability token isolation
