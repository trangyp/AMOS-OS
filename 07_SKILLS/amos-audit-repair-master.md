---
title: AMOS Audit Repair Master
aliases:
  - amos-audit-repair-master
  - 07_SKILLS/amos-audit-repair-master
type: redirect
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 07_SKILLS/amos-audit-repair-master/SKILL.md
  scope: 07_SKILLS
---
# AMOS Audit Repair Master

> **Origin Architect / Steward:** Trang Phan
> **AMOS_CORE Target:** `v4.4`
> **Domain:** `audit`
> **Epistemic Class:** `AMOS_MODEL`
> **Claim Class:** `DERIVED`
> **Governing Plane:** `07_SKILLS`

---

## Purpose

This redirect anchors the AMOS Audit and Repair master skill, the root authority for failure recovery, gap discovery, quality auditing, validation gates, and repair allocation. It routes all audit-repair queries to the canonical SKILL.md and its consolidated sub-skills.

## Domain Coverage

1. Failure recovery: detect failure, diagnose root cause, apply repair, verify recovery
2. Quality validation against validation gates, equation firewall, golden ratio, integrity requirements
3. Gap discovery using completion graph and unknown-unknown registry
4. Provenance tracing to test results, integrity scans, gap registry, and validation gate outputs
5. Audit claim assessment for severity, scope, evidence strength, and repair priority
6. Audit lifecycle management: scan, detect, classify, allocate repair, verify, document
7. Drift detection: test count drift, gap regression, integrity degradation, gate erosion

## Key Capabilities

| Capability | Function |
| :--- | :--- |
| `audit_repair.execute_recovery` | Execute failure recovery: detect, diagnose, repair, verify |
| `audit_repair.validate_quality` | Validate outputs against validation gates and integrity requirements |
| `audit_repair.discover_gaps` | Discover knowledge gaps using completion graph and unknown-unknown registry |
| `audit_repair.assess_claim` | Assess audit claims for severity, scope, evidence strength |
| `audit_repair.detect_drift` | Detect test count drift, gap regression, integrity degradation |

## MECE Mapping to AMOS Planes

- **19_TESTS**: Test and validation contract for audit execution
- **17_OBSERVABILITY**: Receipt and telemetry sealing for audit events
- **03_CONTROL_PLANE**: Repair authority and escalation gates
- **01_CANON**: L10 failure recovery law hierarchy
- **07_SKILLS**: Procedural capability registry (this plane)

## Epistemic Boundaries

- `CAPABILITY != AUTHORITY`: Implementing a procedure does not confer execution rights
- `DOCUMENTED != IMPLEMENTED`: Skill specification presence does not prove runtime deployment
- `SKILL != AGENT`: This skill is a passive procedure; agents invoke it, it never self-triggers
- Domain claims remain `DERIVED` until independently validated against vault sources

## Sub-Skill Consolidation

This master skill consolidates 8 sub-skills under the `audit` domain. Each sub-skill inherits the master's epistemic boundaries and RSCF state classification while maintaining its own capability scope and validation gates.

## Navigation

- **Canonical SKILL:** [[07_SKILLS/amos-audit-repair-master/SKILL.md|AMOS Audit Repair Master SKILL.md]]
- **Agent Template:** [[07_SKILLS/amos-audit-repair-master/AGENT_TEMPLATE.md|AMOS Audit Repair Master AGENT_TEMPLATE]]
- **MOC:** [[07_SKILLS/amos-audit-repair-master/amos-audit-repair-master_MOC|amos-audit-repair-master_MOC]]
- **Skills MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
- **Skill Contract:** [[07_SKILLS/SKILLS_SKILL_CONTRACT|SKILLS_SKILL_CONTRACT]]
- **Vault Source:** [[01_CANON/01_CORE_LAWS/L10_FAILURE_RECOVERY|L10_FAILURE_RECOVERY]]
- **AMOS Home:** [[00_ROOT/00_HOME|00_HOME]]
- **RSCF Registry:** [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
