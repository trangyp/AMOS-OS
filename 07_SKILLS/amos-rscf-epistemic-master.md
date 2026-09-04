---
title: AMOS Rscf Epistemic Master
aliases:
  - amos-rscf-epistemic-master
  - 07_SKILLS/amos-rscf-epistemic-master
type: redirect
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 07_SKILLS/amos-rscf-epistemic-master/SKILL.md
  scope: 07_SKILLS
---
# AMOS Rscf Epistemic Master

> **Origin Architect / Steward:** Trang Phan
> **AMOS_CORE Target:** `v4.4`
> **Domain:** `rscf`
> **Epistemic Class:** `AMOS_MODEL`
> **Claim Class:** `DERIVED`
> **Governing Plane:** `07_SKILLS`

---

## Purpose

This redirect anchors the AMOS RSCF Epistemic master skill, the root authority for claim classification, evidence validation, provenance tracing, scope regime enforcement, freshness checking, falsifier availability, and confidence ceiling assignment. It features 6 RSCF state kinds. It routes all rscf-epistemic queries to the canonical SKILL.md and its 61 consolidated sub-skills.

## Domain Coverage

1. Claim classification using RSCF state kinds: OBSERVATION, SOURCE_CLAIM, DERIVED, MODEL, DECISION, UNKNOWN
2. Epistemic validation: epistemic class labels, claim ceiling, falsifier availability, scope regime
3. Evidence analysis: source independence, contradiction status, freshness, dependency chain
4. Provenance tracing to source evidence, derivation chain, epistemic class, RSCF proof capsule
5. Epistemic claim assessment: confidence ceiling, competing hypotheses, falsifier strength
6. RSCF lifecycle management: classify, validate, trace, assess, label, finalize with proof capsule
7. Drift detection: class inflation, ceiling erosion, falsifier neglect, provenance decay

## Key Capabilities

| Capability | Function |
| :--- | :--- |
| `rscf_episte.classify_claim` | Classify claims using 6 RSCF state kinds |
| `rscf_episte.validate_epistemic` | Validate against epistemic class labels, claim ceiling, falsifiers |
| `rscf_episte.analyze_evidence` | Analyze evidence: source independence, contradiction, freshness |
| `rscf_episte.assess_claim` | Assess claims for confidence ceiling, competing hypotheses, falsifiers |
| `rscf_episte.detect_drift` | Detect class inflation, ceiling erosion, falsifier neglect, provenance decay |

## MECE Mapping to AMOS Planes

- **01_CANON**: L11 knowledge and memory law hierarchy
- **03_CONTROL_PLANE**: Epistemic authority and claim classification gates
- **02_KERNEL**: Kernel primitives for epistemic reasoning
- **07_SKILLS**: Procedural capability registry (this plane)
- **17_OBSERVABILITY**: Receipt sealing for epistemic classification events

## Epistemic Boundaries

- `CAPABILITY != AUTHORITY`: Implementing a procedure does not confer execution rights
- `DOCUMENTED != IMPLEMENTED`: Skill specification presence does not prove runtime deployment
- `SKILL != AGENT`: This skill is a passive procedure; agents invoke it, it never self-triggers
- Domain claims remain `DERIVED` until independently validated against vault sources

## Sub-Skill Consolidation

This master skill consolidates 61 sub-skills under the `rscf` domain. Each sub-skill inherits the master's epistemic boundaries and RSCF state classification while maintaining its own capability scope and validation gates.

## Navigation

- **Canonical SKILL:** [[07_SKILLS/amos-rscf-epistemic-master/SKILL.md|AMOS Rscf Epistemic Master SKILL.md]]
- **Agent Template:** [[07_SKILLS/amos-rscf-epistemic-master/AGENT_TEMPLATE.md|AMOS Rscf Epistemic Master AGENT_TEMPLATE]]
- **MOC:** [[07_SKILLS/amos-rscf-epistemic-master/amos-rscf-epistemic-master_MOC|amos-rscf-epistemic-master_MOC]]
- **Skills MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
- **Skill Contract:** [[07_SKILLS/SKILLS_SKILL_CONTRACT|SKILLS_SKILL_CONTRACT]]
- **Vault Source:** [[01_CANON/01_CORE_LAWS/L11_KNOWLEDGE_MEMORY|L11_KNOWLEDGE_MEMORY]]
- **AMOS Home:** [[00_ROOT/00_HOME|00_HOME]]
- **RSCF Registry:** [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
