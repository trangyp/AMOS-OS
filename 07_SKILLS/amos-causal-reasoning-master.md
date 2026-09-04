---
title: AMOS Causal Reasoning Master
aliases:
  - amos-causal-reasoning-master
  - 07_SKILLS/amos-causal-reasoning-master
type: redirect
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 07_SKILLS/amos-causal-reasoning-master/SKILL.md
  scope: 07_SKILLS
---
# AMOS Causal Reasoning Master

> **Origin Architect / Steward:** Trang Phan
> **AMOS_CORE Target:** `v4.4`
> **Domain:** `causal`
> **Epistemic Class:** `AMOS_MODEL`
> **Claim Class:** `DERIVED`
> **Governing Plane:** `07_SKILLS`

---

## Purpose

This redirect anchors the AMOS Causal Reasoning master skill, the root authority for causal closure, causal hierarchy, counterfactual reasoning, and intervention analysis. It features 4 causal modes (Direct, Distributed, Delayed, Cascading) and 6 causal gates. It routes all causal-reasoning queries to the canonical SKILL.md and its consolidated sub-skills.

## Domain Coverage

1. Causal hierarchy analysis: observation, intervention, counterfactual, causal closure
2. Causal claim validation: identification, confounder control, causal gate compliance
3. Causal intervention analysis: do-calculus, effect estimation, counterfactual mapping
4. Provenance tracing to observational data, intervention records, counterfactual models
5. Causal claim assessment: identification type, evidence strength, mechanism vs correlation
6. Causal lifecycle management: observe, hypothesize, test, intervene, validate, finalize
7. Drift detection: confounder emergence, regime change, causal chain break, effect decay

## Key Capabilities

| Capability | Function |
| :--- | :--- |
| `causal_reason.analyze_causal` | Analyze causal hierarchy: observation, intervention, counterfactual |
| `causal_reason.validate_causal` | Validate causal claims for identification and confounder control |
| `causal_reason.apply_intervention` | Apply do-calculus, effect estimation, counterfactual mapping |
| `causal_reason.assess_causal_claim` | Assess causal claims for identification type and evidence strength |
| `causal_reason.detect_causal_drift` | Detect confounder emergence, regime change, causal chain break |

## MECE Mapping to AMOS Planes

- **02_KERNEL**: Causal kernel and causal hierarchy primitives
- **01_CANON**: Canon laws governing causal claim boundaries
- **11_KNOWLEDGE**: Knowledge base for causal reasoning domain content
- **07_SKILLS**: Procedural capability registry (this plane)
- **22_RESEARCH**: Research integration for causal discovery methods

## Epistemic Boundaries

- `CAPABILITY != AUTHORITY`: Implementing a procedure does not confer execution rights
- `DOCUMENTED != IMPLEMENTED`: Skill specification presence does not prove runtime deployment
- `SKILL != AGENT`: This skill is a passive procedure; agents invoke it, it never self-triggers
- Domain claims remain `DERIVED` until independently validated against vault sources

## Sub-Skill Consolidation

This master skill consolidates 3 sub-skills under the `causal` domain. Each sub-skill inherits the master's epistemic boundaries and RSCF state classification while maintaining its own capability scope and validation gates.

## Navigation

- **Canonical SKILL:** [[07_SKILLS/amos-causal-reasoning-master/SKILL.md|AMOS Causal Reasoning Master SKILL.md]]
- **Agent Template:** [[07_SKILLS/amos-causal-reasoning-master/AGENT_TEMPLATE.md|AMOS Causal Reasoning Master AGENT_TEMPLATE]]
- **MOC:** [[07_SKILLS/amos-causal-reasoning-master/amos-causal-reasoning-master_MOC|amos-causal-reasoning-master_MOC]]
- **Skills MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
- **Skill Contract:** [[07_SKILLS/SKILLS_SKILL_CONTRACT|SKILLS_SKILL_CONTRACT]]
- **Vault Source:** [[02_KERNEL/03_CAUSAL/K_CAUSAL_HIERARCHY|K_CAUSAL_HIERARCHY]]
- **AMOS Home:** [[00_ROOT/00_HOME|00_HOME]]
- **RSCF Registry:** [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
