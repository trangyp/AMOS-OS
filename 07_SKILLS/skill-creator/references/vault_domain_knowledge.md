---
title: Vault Domain Knowledge — Skill Creator
type: reference
source: 07_SKILLS/skill-creator/references
tags:
- reference
- skill-creator
- type/skill
- k-meta-logic
- law-hierarchy
- trang-framework-recursive-ontology-dynamics
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---

# Vault-Sourced Domain Knowledge

> Source: AMOS_OS Obsidian vault (`_00_Cosmo brain/`)
> Epistemic class: SOURCE_CLAIM
> Extracted from skill: `skill-creator`

## Vault-Sourced Content

### Source 1: AMOS Domain-Specific Skills Catalog

> Path: `amos-general/A/Domain/AMOS_Domain_Skills_Catalog.md` | Size: 6189 chars | Match score: 10

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
| [[K_META_LOGIC]] | Meta Logic & Law Kernel | 10 | Yes | logic, law_of_law, reasoning |
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
| ROUTE_EV | ev, charging, station, driver, fleet | [[K_META_LOGIC]], K_MATH_COMPUTE, K_EV_INFRA, K_UNIPOWER_OPS |
| ROUTE_TECH | software, ai, architecture, system_design | [[K_META_LOGIC]], K_MATH_COMPUTE, K_TECH_ENGINE, K_UNIPOWER_TECH |
| ROUTE_PSYCH | emotion, behaviour, psychology, ubi | [[K_META_LOGIC]], K_BIO_NEURO, K_MIND_BEHAVIOR |
| ROUTE_DEFAULT | * (all) | [[K_META_LOGIC]], K_MATH_COMPUTE, K_BIO_NEURO |

## Proposed Future Skills

These skills would extend coverage to domains currently served only by brain kernels:

### Reasoning Extensions
1. **amos-multi-perspective** — Multi-perspective reasoning, bias detection, viewpoint comparison ([[K_META_LOGIC]] + K_MIND_BEHAVIOR)
2. **amos-counterfactual** — Counterfactual reasoning, what-if

---

### Source 2: AMOS Skill Creation Workflow

> Path: `amos-general/A/Skill/AMOS_Skill_Creation_Workflow.md` | Size: 5383 chars | Match score: 10

# AMOS Skill Creation Workflow

Use this workflow to create new AMOS skills that extend the brain's capabilities. Follow the brain's kernel registry and routing rules to ensure new skills integrate properly.

## When to Use
- When a new capability is needed that doesn't exist in the current skill set
- When a brain engine/spec needs a corresponding operational skill
- When the agent registry needs a new agent-focused skill

## Step 1: Identify the Capability Gap

1. Check existing skills in these categories:
   - `reasoning/` — amos-reasoning-loop, amos-law-stack, amos-cognition-modes, amos-expression-overlay
   - `tech/` — amos-tech-kernel-catalog
   - `docs/` — amos-docs-bridge
   - `communication/` — amos-expression-overlay

2. Check the brain's kernel registry (md/Core/AMOS_Kernel_Routing_Workflow.md):
   - [[K_META_LOGIC]] — logic, law_of_law, reasoning
- K_MATH_COMPUTE — math, compute, optimization
   - K_BIO_NEURO — ubi, biology, nervous_system
- K_MIND_BEHAVIOR — psychology, emotion, behaviour
   - K_TECH_ENGINE — software, ai, cloud, infra
- K_EV_INFRA — ev, charging, logistics, fleet
   - K_UNIPOWER_OPS — unipower, vn, ops, drivers, stations
- K_UNIPOWER_TECH — unipower, tech, ai, design

3. Check the brain's routing rules for task type matching:
   - ROUTE_EV: ev, charging, station, driver, fleet
- ROUTE_TECH: software, ai, architecture, system_design
   - ROUTE_PSYCH: emotion, behaviour, psychology, ubi
- ROUTE_DEFAULT: * (fallback)

## Step 2: Name and Categorize

1. **Name:** lowercase, hyphens, descriptive of capability (e.g., `amos-something-descriptive`)
2. **Category:** one of `reasoning`, `tech`, `docs`, `communication`, or a new category if justified
3. **Related skills:** list skills this new skill depends on or complements

## Step 3: Define the Skill Content

Every AMOS skill must include:

### Frontmatter (YAML)
```yaml
---
name: amos-something-descriptive
description: One-line trigger condition — when to use this skill.
version: 1.0.0
author: AMOS Brain (Trang Phan)
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [tag1, tag2]
    related_skills: [skill1, skill2]
---
```

### When to Use
Clear trigger condition. What task tags match? Which routing rule applies?

### What It Does
High-level capability description. Which kernels does it activate?

### How to Use
Step-by-step or bullet instructions. Reference brain files where relevant.

### Examples (optional)
Concrete task → skill → outcome examples.

### References
Brain files, engine IDs, or other skills this skill builds on.

## Step 4: Check Integration

1. **Kernel routing:**

Does this skill activate the right kernels per the routing rules?
2. **Law compliance:**

Does the skill obey Law of Law, Rule of 2, Rule of 4, Absolute Structural Integrity, Post-Theory Communication, UBI Alignment?
3. **IP protection:**

Does the skill avoid exposing internal paths/filenames, raw schema dumping, and exact internal kernel generation?
4. **Expression t

---

### Source 3: AMOS Agent Skill Index

> Path: `amos-general/A/Agent/AMOS_Agent_Skill_Index.md` | Size: 4634 chars | Match score: 10

# AMOS Agent Skill Index


## System → Skill → Agents Map

| System | Hermes Skill | Agents | Dominant Law | Mandatory Gates |
|--------|--------------|--------|--------------|-----------------|
| BRAIN_SYSTEM | amos-brain-agent | Architecture, Decomposer, Planner, Reflection, Strategist | L4 (structural integrity) | Rule of 2 on all conclusions |
| EXECUTION_SYSTEM | amos-execution-agent | Automation, Coding, Deployment, DevOps, Document, Refactor, Writing | L4 + L5 | IP-safe output modes |
| LEGAL_SYSTEM | amos-legal-agent | Compliance, Contract, IP, Legal, LegalRisk | L1 (Law of Law) | Legal disclaimer ALWAYS |
| MONEY_SYSTEM | amos-finance-agent | Cashflow, Finance, FinanceRisk, Investment, MacroAnalyst, Opportunity | L4 (model integrity) | Financial disclaimer ALWAYS |
| SENSE_SYSTEM | amos-sense-agent | Context, Sensors, StateSummarizer | L4 (provenance/freshness) | Epistemic class labelling |
| WORLD_MODEL_SYSTEM | amos-world-model-agent | GeoAnalyst, MacroAnalyst(WM), SectorAnalyst, Shock, Trend | L2 (competing scenarios) | Uncertainty bands on projections |
| LIFE_SYSTEM | amos-life-agent | Health, LoadBalancer, Routine | L1 (no medical replacement) + L6 (UBI) | Health disclaimer ALWAYS; autonomy check |

Orchestration layer: amos-agent-orchestration (routing/conflict), amos-agent-execution (loop/output modes), amos-agent-reflective (audit/gaps).

## Collaboration Chains (documented in skills)

1. **Analysis chain:**

Context_Agent → Trend_Agent → SectorAnalyst_Agent → Finance_Agent → StateSummarizer_Agent
2. **Risk chain:**

Trend_Agent → Shock_Agent → MacroAnalyst(WM)_Agent → FinanceRisk_Agent → LegalRisk_Agent
3. **Build chain:**

Decomposer_Agent → Planner_Agent → Architecture_Agent → Coding_Agent → Refactor_Agent → DevOps_Agent → Deployment_Agent
4. **Wellbeing chain:**

Emotion-analysis → Health_Agent → LoadBalancer_Agent → Routine_Agent
5. **Strategy chain:**

Strategist_Agent → Context_Agent → Opportunity_Agent → Planner_Agent → Reflection_Agent

## Per-Agent Quick Reference

### BRAIN_SYSTEM
- Architecture_Agent: components → relationships → evaluation → ADR documentation. Kernels: [[K_META_LOGIC]]+K_TECH_ENGINE+K_UNIPOWER_TECH.
- Decomposer_Agent: MECE decomposition, hidden sub-questions, dependency sequencing. Kernels: [[K_META_LOGIC]]+K_MATH_COMPUTE.
- Planner_Agent: steps → dependencies → resources → roadmap with milestones. Kernels: [[K_META_LOGIC]]+K_MATH_COMPUTE+K_MIND_BEHAVIOR.
- Reflection_Agent: L1-L6 audit → gaps → weaknesses → contradictions → prioritised improvements. Kernel: [[K_META_LOGIC]].
- Strategist_Agent: actors/incentives → coalitions → game-theory analysis → strategic recommendations. Kernels: [[K_META_LOGIC]]+K_MIND_BEHAVIOR+K_MATH_COMPUTE.

### EXECUTION_SYSTEM
- Coding_Agent: requirements → design → generate → review → document. Security and quality gates.
- DevOps_Agent: infra needs → CI/CD design → observability → health monitoring.
- Writing_Agent: audience/tone → draft → expression overlay → clarity review.

### LEGAL_SYSTE

---
**MOC:** references_MOC

## Related

- [[07_SKILLS_MOC]]
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · references_MOC · [[07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: skill-creator-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/skill-creator/references/vault_domain_knowledge.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
