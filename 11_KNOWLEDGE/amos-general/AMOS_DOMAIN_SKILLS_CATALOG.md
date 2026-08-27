---
title: AMOS DOMAIN SKILLS CATALOG
tags: [canon-group/tech-ai, canon/framework, rscf/claim, rscf/provenance, rscf/state/source-claim, topic/amos-domain-skills-catalog, amos-general]
type: document
source: 11_KNOWLEDGE/amos-general
---



# AMOS Domain-Specific Skills Catalog

Catalog of domain-specific skills that extend the AMOS brain's capabilities beyond the core reasoning layer.

## Skill Inventory

### Reasoning Skills (core)
| Skill | Description | When to Use |
|-------|-------------|-------------|
| amos-reasoning-loop | 9-step HIE pipeline with law-stack gates | Any reasoning task |
| amos-law-stack | 6-law priority validation | Before any non-trivial decision or output |
| amos-cognition-modes | Select cognition layer and reasoning mode | When task type requires specific cognitive approach |

### Communication Skills
| Skill | Description | When to Use |
|-------|-------------|-------------|
| amos-expression-overlay | Post-Theory language, identity, IP disclosure | Final output stage of any response |

### Tech Skills
| Skill | Description | When to Use |
|-------|-------------|-------------|
| amos-tech-kernel-catalog | Browse and apply Tech kernel domains | Tech/software/AI architecture tasks |

### Docs Skills
| Skill | Description | When to Use |
|-------|-------------|-------------|
| amos-docs-bridge | Cross-reference AMOS brain ↔ COSMO docs | When navigating between brain knowledge and project docs |

## Brain Kernel Registry (source of truth for skill capabilities)

From md/Core/AMOS_Kernel_Routing_Workflow.md:

| Kernel ID | Name | Priority | Required | Domains |
|-----------|------|----------|----------|---------|
| K_META_LOGIC | Meta Logic & Law Kernel | 10 | Yes | logic, law_of_law, reasoning |
| K_MATH_COMPUTE | Math & Computation Kernel | 9 | Yes | math, compute, optimization |
| K_BIO_NEURO | Biology & Neuro Kernel | 9 | Yes | ubi, biology, nervous_system |
| K_MIND_BEHAVIOR | Mind, Emotion & Behaviour Kernel | 8 | Yes | psychology, emotion, behaviour |
| K_TECH_ENGINE | Technology & Engineering Kernel | 7 | No | software, ai, cloud, infra |
| K_EV_INFRA | EV Infrastructure Kernel | 7 | No | ev, charging, logistics, fleet |
| K_UNIPOWER_OPS | UniPower Operational Brain | 8 | No | unipower, vn, ops, drivers, stations |
| K_UNIPOWER_TECH | UniPower Tech & Design MetaBrain | 8 | No | unipower, tech, ai, design |

## Routing Rules (from brain root)

| Route | Match Tags | Kernels Activated |
|-------|------------|-------------------|
| ROUTE_EV | ev, charging, station, driver, fleet | K_META_LOGIC, K_MATH_COMPUTE, K_EV_INFRA, K_UNIPOWER_OPS |
| ROUTE_TECH | software, ai, architecture, system_design | K_META_LOGIC, K_MATH_COMPUTE, K_TECH_ENGINE, K_UNIPOWER_TECH |
| ROUTE_PSYCH | emotion, behaviour, psychology, ubi | K_META_LOGIC, K_BIO_NEURO, K_MIND_BEHAVIOR |
| ROUTE_DEFAULT | * (all) | K_META_LOGIC, K_MATH_COMPUTE, K_BIO_NEURO |

## Proposed Future Skills

These skills would extend coverage to domains currently served only by brain kernels:

### Reasoning Extensions
1. **amos-multi-perspective** — Multi-perspective reasoning, bias detection, viewpoint comparison (K_META_LOGIC + K_MIND_BEHAVIOR)
2. **amos-counterfactual** — Counterfactual reasoning, what-if analysis, alternative scenario exploration (K_META_LOGIC + K_MATH_COMPUTE)
3. **amos-ubi-alignment** — Biological intelligence alignment checking, nervous system safety assessment (K_BIO_NEURO + K_META_LOGIC)

### Tech Extensions
4. **amos-architecture-design** — System architecture design, component modeling, integration planning (K_TECH_ENGINE + K_META_LOGIC + K_UNIPOWER_TECH)
5. **amos-data-pipeline** — Data pipeline design, ETL workflow specification, data flow architecture (K_TECH_ENGINE + K_MATH_COMPUTE)
6. **amos-ev-planning** — EV infrastructure planning, charging logistics, fleet optimization (K_EV_INFRA + K_UNIPOWER_OPS + K_MATH_COMPUTE)

### Psychology/Biology Extensions
7. **amos-emotion-analysis** — Emotion state detection, affective pattern recognition, somatic state mapping (K_MIND_BEHAVIOR + K_BIO_NEURO)
8. **amos-behaviour-design** — Behavioural pattern design, habit architecture, routine optimization (K_MIND_BEHAVIOR + K_BIO_NEURO)

### Law/Governance Extensions
9. **amos-law-analysis** — Legal reasoning, jurisdiction mapping, rule system analysis (K_META_LOGIC)
10. **amos-compliance-check** — Regulatory compliance assessment, policy gap analysis (K_META_LOGIC)

### Economic Extensions
11. **amos-economic-analysis** — Economic trend analysis, market modeling, sector assessment (K_MATH_COMPUTE + K_META_LOGIC + K_MIND_BEHAVIOR)
12. **amos-investment-framework** — Investment evaluation, portfolio construction, risk-return analysis (K_MATH_COMPUTE + K_META_LOGIC)

## Skill Creation Pattern

When creating a new AMOS skill:

1. **Identify kernel dependencies:** Which brain kernels does this skill need?
2. **Determine routing:** Which routing rule(s) match this skill's task tags?
3. **Write SKILL.md:** Follow the pattern from existing skills (frontmatter + when to use + how to use + examples)
4. **Place in correct category:** reasoning/, tech/, docs/, communication/, or new category
5. **Test integration:** Verify the skill activates the right kernels and obeys all laws

## Memory: Domain-Specific Skills

Current AMOS skill inventory: 4 skills (amos-reasoning-loop, amos-law-stack, amos-cognition-modes in reasoning/; amos-expression-overlay in communication/; amos-tech-kernel-catalog in tech/; amos-docs-bridge in docs/). Brain kernel registry: 8 kernels (K_META_LOGIC priority 10 required, K_MATH_COMPUTE priority 9 required, K_BIO_NEURO priority 9 required, K_MIND_BEHAVIOR priority 8 required, K_TECH_ENGINE priority 7 optional, K_EV_INFRA priority 7 optional, K_UNIPOWER_OPS priority 8 optional, K_UNIPOWER_TECH priority 8 optional). Routing rules: ROUTE_EV (ev/charging/station/driver/fleet), ROUTE_TECH (software/ai/architecture/system_design), ROUTE_PSYCH (emotion/behaviour/psychology/ubi), ROUTE_DEFAULT (*). 12 proposed future skills across reasoning, tech, psychology/biology, law/governance, and economic domains.

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[AMOS-GENERAL_MOC]]
