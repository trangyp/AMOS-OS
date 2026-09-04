---
title: "23_OPERATING_MODEL — Governance, Roles & Decision Rights"
type: architecture_specification
source: 23_OPERATING_MODEL
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
    - 00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE
    - 01_CANON/01_CANON_README
  scope: operating_model
tags:
  - amos-os
  - operating-model
  - roles
  - decision-rights
  - escalation
---

# 23_OPERATING_MODEL — Master Operating Model

## 1. Plane Purpose

The `23_OPERATING_MODEL` plane (**Partition A: Normative & Governance Definition**) defines the organizational accountability, human stewardship, decision rights, escalation pathways, and service level objectives for the AMOS Full Brain OS.

This plane establishes the governance framework that binds all 26 AMOS planes to a unified accountability structure. It separates human stewardship from autonomous agent execution, ensuring that consequential decisions remain traceable to a responsible and accountable party.

```text
ORIGIN_ARCHITECT = Trang Phan
AGENT_ROLE != HUMAN_ACCOUNTABILITY
GOVERNANCE != BOTTLENECK
DOCUMENTED != IMPLEMENTED
```

---

## 2. Architecture Overview

The operating model is structured around five governance pillars, each addressing a distinct aspect of organizational control:

1. **Roles & Responsibilities** — Who does what, with clear human-agent boundary separation.
2. **Decision Rights** — Who can authorize what, with five-tier escalation hierarchy.
3. **Governance Forums** — Where decisions are deliberated and ratified.
4. **Escalation Pathways** — How conflicts and incidents propagate through authority tiers.
5. **Service Levels** — What performance and integrity guarantees the system must meet.

---

## 3. Key Components

### 3.1 Five Governance Pillars

1. **`01_ROLES/ROLE_REGISTRY.md`**: Definition of human and synthetic role responsibilities, including the Origin Architect, Canon Stewards, Security Council, Specialist Agents, and Orchestrator roles.
2. **`02_DECISION_RIGHTS/DECISION_RIGHTS.md`**: RACI matrices for canon changes, security rules, and code execution. Five-tier hierarchy (D0-D4) with cryptographic receipt requirements.
3. **`03_GOVERNANCE_FORUMS/GOVERNANCE_FORUMS.md`**: Architecture Review Board, Security Council, and Canon Stewardship deliberation structures.
4. **`04_ESCALATION/ESCALATION_PATHS.md`**: Tier 1 to Tier 4 incident and contention escalation ladders with timeout bounds and evidence package requirements.
5. **`05_SERVICE_LEVELS/SERVICE_LEVELS.md`**: Latency, accuracy, token budget, and integrity SLOs with monitoring and breach response procedures.

### 3.2 Authority Boundary

The Origin Architect (Trang Phan) retains sole authority over:
- Canonical law modifications (`01_CANON`)
- Kernel mutations (`02_KERNEL`)
- Post-v4.4 version promotions
- Security-critical architectural changes

All other decisions are delegated through the tier hierarchy with appropriate quorum and receipt requirements.

---

## 4. Navigation

- **Decision Rights:** [[23_OPERATING_MODEL/02_DECISION_RIGHTS/DECISION_RIGHTS|DECISION_RIGHTS]]
- **Roles Registry:** [[23_OPERATING_MODEL/01_ROLES/ROLE_REGISTRY|ROLE_REGISTRY]]
- **Governance Forums:** [[23_OPERATING_MODEL/03_GOVERNANCE_FORUMS/GOVERNANCE_FORUMS|GOVERNANCE_FORUMS]]
- **Escalation Paths:** [[23_OPERATING_MODEL/04_ESCALATION/ESCALATION_PATHS|ESCALATION_PATHS]]
- **Service Levels:** [[23_OPERATING_MODEL/05_SERVICE_LEVELS/SERVICE_LEVELS|SERVICE_LEVELS]]
- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
- **Root Architecture:** [[00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE|FULL_BRAIN_OS_MECE_ARCHITECTURE]]
- **Canon:** [[01_CANON/01_CANON_README|01_CANON_README]]

---

## 5. Status & Gaps

- **Status:** `ACTIVE_SPECIFICATION` — all five governance pillars are documented and structurally present in the vault.
- **Enforcement Gap:** Decision rights enforcement in the runtime requires integration with the control plane capability token system. This integration is specified but not yet implemented (`DOCUMENTED != IMPLEMENTED`).
- **Multi-Stakeholder Succession:** The current model assigns D4 authority solely to the Origin Architect. Organizational succession planning for D4 authority is `UNKNOWN/GAP`.
- **Automated Escalation:** Timeout-based automatic escalation triggers are specified but not yet operationalized in the runtime engine.
- **SLO Monitoring Integration:** Service level objectives are defined but automated breach detection and response workflows are not yet connected to the observability plane.
