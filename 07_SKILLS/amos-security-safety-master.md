---
title: AMOS Security Safety Master
aliases:
  - amos-security-safety-master
  - 07_SKILLS/amos-security-safety-master
type: redirect
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 07_SKILLS/amos-security-safety-master/SKILL.md
  scope: 07_SKILLS
---
# AMOS Security Safety Master

> **Origin Architect / Steward:** Trang Phan
> **AMOS_CORE Target:** `v4.4`
> **Domain:** `security`
> **Epistemic Class:** `AMOS_MODEL`
> **Claim Class:** `DERIVED`
> **Governing Plane:** `07_SKILLS`

---

## Purpose

This redirect anchors the AMOS Security and Safety master skill, the root authority for adversarial robustness, privacy, safety firewalls, immune systems, and drift alignment. It routes all security-safety queries to the canonical SKILL.md and its consolidated sub-skills.

## Domain Coverage

1. Security influence evaluation: consent, provenance, and risk gates for security-action boundaries
2. Security gate validation: hard partition gates, epistemic class preservation, consent state
3. Security state analysis: working, episodic, semantic stores, consolidation, retrieval graph
4. Provenance tracing to source, encoding operation, consolidation history, field-level lineage
5. Security claim assessment: epistemic class, freshness, contradiction status, confidence ceiling
6. Security lifecycle management: encode, normalize, admit, consolidate, index, retrieve, filter, update
7. Drift detection: stale entries, broken provenance, epistemic class erosion, context discontinuity

## Key Capabilities

| Capability | Function |
| :--- | :--- |
| `security_safety.evaluate_influence` | Evaluate security-action influence through consent, provenance, risk gates |
| `security_safety.validate_gates` | Validate hard partition gates and epistemic class preservation |
| `security_safety.analyze_state` | Analyze security state: working, episodic, semantic, consolidation |
| `security_safety.assess_claim` | Assess security claims for epistemic class, freshness, confidence ceiling |
| `security_safety.detect_drift` | Detect stale entries, broken provenance, epistemic class erosion |

## MECE Mapping to AMOS Planes

- **18_SECURITY**: Security plane and safety enforcement
- **03_CONTROL_PLANE**: Security authority and admission gates
- **01_CANON**: Canon laws governing security claim boundaries
- **07_SKILLS**: Procedural capability registry (this plane)
- **17_OBSERVABILITY**: Receipt sealing for security lifecycle events

## Epistemic Boundaries

- `CAPABILITY != AUTHORITY`: Implementing a procedure does not confer execution rights
- `DOCUMENTED != IMPLEMENTED`: Skill specification presence does not prove runtime deployment
- `SKILL != AGENT`: This skill is a passive procedure; agents invoke it, it never self-triggers
- Domain claims remain `DERIVED` until independently validated against vault sources

## Sub-Skill Consolidation

This master skill consolidates 2 sub-skills under the `security` domain. Each sub-skill inherits the master's epistemic boundaries and RSCF state classification while maintaining its own capability scope and validation gates.

## Navigation

- **Canonical SKILL:** [[07_SKILLS/amos-security-safety-master/SKILL.md|AMOS Security Safety Master SKILL.md]]
- **Agent Template:** [[07_SKILLS/amos-security-safety-master/AGENT_TEMPLATE.md|AMOS Security Safety Master AGENT_TEMPLATE]]
- **MOC:** [[07_SKILLS/amos-security-safety-master/amos-security-safety-master_MOC|amos-security-safety-master_MOC]]
- **Skills MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
- **Skill Contract:** [[07_SKILLS/SKILLS_SKILL_CONTRACT|SKILLS_SKILL_CONTRACT]]
- **Vault Source:** [[18_SECURITY/SECURITY_README|SECURITY_README]]
- **AMOS Home:** [[00_ROOT/00_HOME|00_HOME]]
- **RSCF Registry:** [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
