---
title: "23 Operating Model — README"
type: readme
source: 23_OPERATING_MODEL
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: operating_model_readme
---

# 23 Operating Model — README

## Role

Defines how humans and system governance interact — roles, responsibilities, decision rights, authority, review cadence, change control, maintenance, and stewardship. The operating model defines "who does what, with what authority, under what constraints" for AMOS operations.

## Core Principle

```
Operating model != Governance.
Operating model defines structure; governance defines authority.
```

## Directory Structure

```
23_OPERATING_MODEL/
├── 00_INDEX/              ← Operating model indices and navigation registries
├── 01_ROLES/              ← Defined positions with responsibilities and authority levels
├── 02_DECISION_RIGHTS/    ← Who can decide what, under what conditions, with escalation
├── 03_GOVERNANCE_FORUMS/  ← Structured venues for collective decision-making and review
├── 04_ESCALATION/         ← Clear routes for issues exceeding individual authority
├── 05_SERVICE_LEVELS/     ← Agreed-upon performance targets and SLA commitments
├── 23_OPERATING_MODEL_MOC.md ← Master map of content for the Operating Model plane
├── 23_OPERATING_MODEL_README.md ← This file
├── OPERATING_MODEL_OPERATING_MODEL_CONTRACT.md ← Invariant governance contract
└── OLLIVIER_RICCI_CURVATURE_LEDGER.md ← Ricci curvature computation ledger
```

## Operating Model Components

- **Roles:** Defined positions with specific responsibilities, capabilities, and authority levels
- **Decision Rights:** Who can decide what, under what conditions, with what escalation paths
- **Governance Forums:** Structured venues for collective decision-making and review
- **Escalation Paths:** Clear routes for issues that exceed individual authority
- **Service Levels:** Agreed-upon performance targets and SLA commitments
- **Operating Rhythms:** Cadence of reviews, meetings, updates, and maintenance windows

## Hard Boundaries

- **Role != Person** — roles are defined positions; people fill roles temporarily
- **Authority != Capability** — having authority does not imply having capability; both are required
- **Process != Outcome** — following process does not guarantee good outcome; process reduces risk
- **Operating Model != Governance** — operating model defines structure; governance defines authority

## Key Protocols

- **Role Assignment:** Roles assigned based on capability, availability, and conflict-of-interest checks
- **Decision Logging:** All decisions logged with actor, context, rationale, and outcome
- **Escalation SLAs:** Escalation paths have defined response times and resolution targets
- **Forum Minutes:** Governance forums produce structured minutes with decisions and action items
- **Service Level Monitoring:** SLA compliance tracked and reported with breach notification

## Key Artifacts

- **Operating Model Contract:** [[23_OPERATING_MODEL/OPERATING_MODEL_OPERATING_MODEL_CONTRACT|Operating Model Contract]] — invariant governance
- **Roles:** `01_ROLES/` — defined positions with responsibilities and authority levels
- **Decision Rights:** `02_DECISION_RIGHTS/` — decision authority matrix and escalation rules
- **Governance Forums:** `03_GOVERNANCE_FORUMS/` — structured decision-making venues
- **Escalation Paths:** `04_ESCALATION/` — escalation routes and SLA definitions
- **Service Levels:** `05_SERVICE_LEVELS/` — performance targets and SLA commitments

## Canonical Laws Governing

- **M07 (Canon ≠ Implementation):** Operating model specifications are not runtime implementations
- **CAPABILITY ≠ AUTHORITY:** Having capability does not imply having authority; both are required
- **PROPOSAL != COMMIT:** Operational proposals are not commits without governance approval
- **Trang Phan remains origin architect:** Agents must not claim independent authorship of AMOS

## Cross-Plane Relationships

- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_README|03_CONTROL_PLANE_README]] — Operating model implements control plane governance
- **Operations:** [[20_OPERATIONS/20_OPERATIONS_README|20_OPERATIONS_README]] — Operating model governs operational execution
- **Agents:** [[06_AGENTS/06_AGENTS_README|06_AGENTS_README]] — Operating model defines agent roles and authority
- **Security:** [[18_SECURITY/18_SECURITY_README|18_SECURITY_README]] — Operating model enforces security roles and access control
- **Canon:** [[01_CANON/01_CANON_MOC|01_CANON_MOC]] — Canon defines what roles mean; operating model assigns them

## Entry Points

- **Master MOC:** [[23_OPERATING_MODEL/23_OPERATING_MODEL_MOC|23_OPERATING_MODEL_MOC]] · **Contract:** [[23_OPERATING_MODEL/OPERATING_MODEL_OPERATING_MODEL_CONTRACT|Contract]]

## Implementation Status

- **Structural completeness:** 5 subdirectories covering roles, decision rights, forums, escalation, and service levels
- **Contract present:** Operating model contract defines invariant governance boundaries
- **Ricci curvature:** Ollivier-Ricci curvature ledger maintained for structural analysis
- **Executable closure:** UNKNOWN/GAP — operating model specifications are structural patterns unless tied to executed governance workflow evidence

## AMOS MECE Alignment

The Operating Model Plane is Plane 23 of 26. It is mutually exclusive from Control Plane (03_CONTROL_PLANE, which defines authority) and Operations (20_OPERATIONS, which executes). It is collectively exhaustive with all other planes in covering the human-governance-interaction dimension. MECE boundary: it owns roles, decision rights, forums, escalation, and service levels, not governance authority, operational execution, or agent definitions.

______________________________________________________________________

**Parent:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
