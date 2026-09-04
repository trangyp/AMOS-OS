---
title: AMOS Boundary Scope Master
aliases:
  - amos-boundary-scope-master
  - 07_SKILLS/amos-boundary-scope-master
type: redirect
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 07_SKILLS/amos-boundary-scope-master/SKILL.md
  scope: 07_SKILLS
---
# AMOS Boundary Scope Master

> **Origin Architect / Steward:** Trang Phan
> **AMOS_CORE Target:** `v4.4`
> **Domain:** `boundary`
> **Epistemic Class:** `AMOS_MODEL`
> **Claim Class:** `DERIVED`
> **Governing Plane:** `07_SKILLS`

---

## Purpose

This redirect anchors the AMOS Boundary and Scope master skill, the root authority for scope regimes, boundary admission, context continuity, and capability bounds. It routes all boundary-scope queries to the canonical SKILL.md and its consolidated sub-skills.

## Domain Coverage

1. Influence evaluation: consent, provenance, and risk gates for memory-action boundaries
2. Hard partition gate validation with epistemic class preservation and consent state requirements
3. Memory state analysis: working, episodic, semantic stores, consolidation, retrieval graph health
4. Provenance tracing to source, encoding operation, consolidation history, and field-level lineage
5. Memory claim assessment for epistemic class, freshness, contradiction status, confidence ceiling
6. Lifecycle management: encode, normalize, admit, consolidate, index, retrieve, filter, update
7. Drift detection: stale entries, broken provenance, epistemic class erosion, context discontinuity

## Key Capabilities

| Capability | Function |
| :--- | :--- |
| `boundary_scope.evaluate_influence` | Evaluate memory-action influence through consent, provenance, risk gates |
| `boundary_scope.validate_gates` | Validate hard partition gates and epistemic class preservation |
| `boundary_scope.analyze_state` | Analyze memory state: working, episodic, semantic stores, consolidation |
| `boundary_scope.trace_provenance` | Trace memory entries to source, encoding, consolidation history |
| `boundary_scope.detect_drift` | Detect stale entries, broken provenance, epistemic class erosion |

## MECE Mapping to AMOS Planes

- **01_CANON**: L5 scope regime law hierarchy
- **03_CONTROL_PLANE**: Boundary admission and capability token scoping
- **10_MEMORY**: Memory store integration for boundary evaluation
- **07_SKILLS**: Procedural capability registry (this plane)
- **17_OBSERVABILITY**: Receipt sealing for boundary decisions

## Epistemic Boundaries

- `CAPABILITY != AUTHORITY`: Implementing a procedure does not confer execution rights
- `DOCUMENTED != IMPLEMENTED`: Skill specification presence does not prove runtime deployment
- `SKILL != AGENT`: This skill is a passive procedure; agents invoke it, it never self-triggers
- Domain claims remain `DERIVED` until independently validated against vault sources

## Sub-Skill Consolidation

This master skill consolidates 2 sub-skills under the `boundary` domain. Each sub-skill inherits the master's epistemic boundaries and RSCF state classification while maintaining its own capability scope and validation gates.

## Navigation

- **Canonical SKILL:** [[07_SKILLS/amos-boundary-scope-master/SKILL.md|AMOS Boundary Scope Master SKILL.md]]
- **Agent Template:** [[07_SKILLS/amos-boundary-scope-master/AGENT_TEMPLATE.md|AMOS Boundary Scope Master AGENT_TEMPLATE]]
- **MOC:** [[07_SKILLS/amos-boundary-scope-master/amos-boundary-scope-master_MOC|amos-boundary-scope-master_MOC]]
- **Skills MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
- **Skill Contract:** [[07_SKILLS/SKILLS_SKILL_CONTRACT|SKILLS_SKILL_CONTRACT]]
- **Vault Source:** [[01_CANON/01_CORE_LAWS/L5_SCOPE_REGIME|L5_SCOPE_REGIME]]
- **AMOS Home:** [[00_ROOT/00_HOME|00_HOME]]
- **RSCF Registry:** [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
