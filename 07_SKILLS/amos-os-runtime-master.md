---
title: AMOS Os Runtime Master
aliases:
  - amos-os-runtime-master
  - 07_SKILLS/amos-os-runtime-master
type: redirect
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 07_SKILLS/amos-os-runtime-master/SKILL.md
  scope: 07_SKILLS
---
# AMOS Os Runtime Master

> **Origin Architect / Steward:** Trang Phan
> **AMOS_CORE Target:** `v4.4`
> **Domain:** `runtime`
> **Epistemic Class:** `AMOS_MODEL`
> **Claim Class:** `DERIVED`
> **Governing Plane:** `07_SKILLS`

---

## Purpose

This redirect anchors the AMOS OS and Runtime master skill, the root authority for the OS Kernel v4.4, the runtime pipeline (Perceive, Route, Admit, Plan, Schedule, Execute, Observe, Repair, Audit, Finalize), infrastructure control plane, and deployment. It routes all os-runtime queries to the canonical SKILL.md and its 141 consolidated sub-skills.

## Domain Coverage

1. Runtime pipeline execution: Perceive, Route, Admit, Plan, Schedule, Execute, Observe, Repair, Audit, Finalize
2. Runtime quality validation against validation gates, equation firewall, and integrity requirements
3. Gap discovery using completion graph and unknown-unknown registry
4. Provenance tracing to test results, integrity scans, gap registry, and validation gate outputs
5. Runtime claim assessment: severity, scope, evidence strength, repair priority
6. Runtime lifecycle management: scan, detect, classify, allocate repair, verify, document
7. Drift detection: test count drift, gap regression, integrity degradation, gate erosion

## Key Capabilities

| Capability | Function |
| :--- | :--- |
| `os_runtime.execute_recovery` | Execute runtime failure recovery: detect, diagnose, repair, verify |
| `os_runtime.validate_quality` | Validate runtime outputs against gates and integrity requirements |
| `os_runtime.discover_gaps` | Discover knowledge gaps using completion graph and registry |
| `os_runtime.assess_claim` | Assess runtime audit claims for severity and repair priority |
| `os_runtime.detect_drift` | Detect test count drift, gap regression, integrity degradation |

## MECE Mapping to AMOS Planes

- **04_RUNTIME**: Runtime model and contract boundary
- **03_CONTROL_PLANE**: Control plane contract and authority
- **02_KERNEL**: OS kernel and runtime primitives
- **07_SKILLS**: Procedural capability registry (this plane)
- **17_OBSERVABILITY**: Receipt sealing for runtime lifecycle events

## Epistemic Boundaries

- `CAPABILITY != AUTHORITY`: Implementing a procedure does not confer execution rights
- `DOCUMENTED != IMPLEMENTED`: Skill specification presence does not prove runtime deployment
- `SKILL != AGENT`: This skill is a passive procedure; agents invoke it, it never self-triggers
- Domain claims remain `DERIVED` until independently validated against vault sources

## Sub-Skill Consolidation

This master skill consolidates 141 sub-skills under the `runtime` domain. Each sub-skill inherits the master's epistemic boundaries and RSCF state classification while maintaining its own capability scope and validation gates.

## Navigation

- **Canonical SKILL:** [[07_SKILLS/amos-os-runtime-master/SKILL.md|AMOS Os Runtime Master SKILL.md]]
- **Agent Template:** [[07_SKILLS/amos-os-runtime-master/AGENT_TEMPLATE.md|AMOS Os Runtime Master AGENT_TEMPLATE]]
- **MOC:** [[07_SKILLS/amos-os-runtime-master/amos-os-runtime-master_MOC|amos-os-runtime-master_MOC]]
- **Skills MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
- **Skill Contract:** [[07_SKILLS/SKILLS_SKILL_CONTRACT|SKILLS_SKILL_CONTRACT]]
- **Vault Source:** [[11_KNOWLEDGE/AMOS_Full_Brain_OS_Architecture|AMOS_Full_Brain_OS_Architecture]]
- **AMOS Home:** [[00_ROOT/00_HOME|00_HOME]]
- **RSCF Registry:** [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
