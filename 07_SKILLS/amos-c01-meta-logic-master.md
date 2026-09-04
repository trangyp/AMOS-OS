---
title: AMOS C01 Meta Logic Master
aliases:
  - amos-c01-meta-logic-master
  - 07_SKILLS/amos-c01-meta-logic-master
type: redirect
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 07_SKILLS/amos-c01-meta-logic-master/SKILL.md
  scope: 07_SKILLS
---
# AMOS C01 Meta Logic Master

> **Origin Architect / Steward:** Trang Phan
> **AMOS_CORE Target:** `v4.4`
> **Domain:** `c01`
> **Epistemic Class:** `AMOS_MODEL`
> **Claim Class:** `DERIVED`
> **Governing Plane:** `07_SKILLS`

---

## Purpose

This redirect anchors the AMOS C01 Meta Logic master skill, the root authority for the irreducible logic core including 8 ALUs, 7 UMLs, 6 UOPs, and 5 Pattern Families. It routes all meta-logic queries to the canonical SKILL.md and its 60 consolidated sub-skills.

## Domain Coverage

1. Question decomposition into minimal coherent sub-questions before inference
2. Concept hygiene: definition tables for load-bearing terms, semantic drift detection
3. Assumption graph construction: surface hidden assumptions, label facts/estimates/hypotheses
4. Frame selection: candidate frameworks, compatibility checking, logic mode declaration
5. Reasoning trace production: deterministic, auditable traces with mode, assumptions, operators
6. Conflict detection: structural contradictions classified as definitional/evidential/framework
7. Meta-law validation: Law of Law, Rule of 2, Rule of 4 enforcement

## Key Capabilities

| Capability | Function |
| :--- | :--- |
| `c01.question_decompose` | Decompose raw questions into minimal coherent sub-questions |
| `c01.concept_hygiene` | Build definition tables for load-bearing terms, detect semantic drift |
| `c01.assumption_graph` | Surface hidden assumptions, label as facts/estimates/hypotheses |
| `c01.frame_selection` | List candidate frameworks, check compatibility, declare logic mode |
| `c01.reasoning_trace` | Produce deterministic, auditable reasoning traces with gate results |

## MECE Mapping to AMOS Planes

- **02_KERNEL**: Meta-logic kernel and reasoning primitives
- **01_CANON**: Core laws and meta-law hierarchy
- **05_COGNITIVE_ORGANISM**: Cognitive architecture consuming logic primitives
- **07_SKILLS**: Procedural capability registry (this plane)
- **19_TESTS**: Formal verification and metamorphic testing

## Epistemic Boundaries

- `CAPABILITY != AUTHORITY`: Implementing a procedure does not confer execution rights
- `DOCUMENTED != IMPLEMENTED`: Skill specification presence does not prove runtime deployment
- `SKILL != AGENT`: This skill is a passive procedure; agents invoke it, it never self-triggers
- Domain claims remain `DERIVED` until independently validated against vault sources

## Sub-Skill Consolidation

This master skill consolidates 60 sub-skills under the `c01` domain. Each sub-skill inherits the master's epistemic boundaries and RSCF state classification while maintaining its own capability scope and validation gates.

## Navigation

- **Canonical SKILL:** [[07_SKILLS/amos-c01-meta-logic-master/SKILL.md|AMOS C01 Meta Logic Master SKILL.md]]
- **Agent Template:** [[07_SKILLS/amos-c01-meta-logic-master/AGENT_TEMPLATE.md|AMOS C01 Meta Logic Master AGENT_TEMPLATE]]
- **MOC:** [[07_SKILLS/amos-c01-meta-logic-master/amos-c01-meta-logic-master_MOC|amos-c01-meta-logic-master_MOC]]
- **Skills MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
- **Skill Contract:** [[07_SKILLS/SKILLS_SKILL_CONTRACT|SKILLS_SKILL_CONTRACT]]
- **Vault Source:** [[11_KNOWLEDGE/AMOS_C01_META_LOGIC_MASTER_KNOWLEDGE|AMOS_C01_META_LOGIC_MASTER_KNOWLEDGE]]
- **AMOS Home:** [[00_ROOT/00_HOME|00_HOME]]
- **RSCF Registry:** [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
