---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Vault Domain Knowledge
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# Vault-Sourced Domain Knowledge

> Source: AMOS_OS Obsidian vault (`_00_Cosmo brain/`)
> Epistemic class: SOURCE_CLAIM
> Extracted from skill: `amos-designer-os`

## Vault-Sourced Content

### Source 1: AMOS Designer OS — Standalone Shell

> Path: `amos-general/A/Designer/AMOS Designer OS.md` | Size: 2623 chars | Match score: 10 | content_hash: 4b27d67a0fa88473

## AMOS Designer OS — Standalone Shell

## What It Is

A minimal, designer-first AMOS shell that runs without editing Python code and without any online API or large model dependency. Designed as a structural shell for organizing ideas, roles, and brain model auditably.

## Files (5)

| File               | Size   | Purpose                                                                  |
| ------------------ | ------ | ------------------------------------------------------------------------ |
| `AMOS.brain`       | 2,066B | Designer-facing control file (identity, goals, constraints, brain model) |
| `AMOS.config.json` | 506B   | Runtime configuration                                                    |
| `README.txt`       | 1,410B | Setup and usage instructions                                             |
| `run_amos.py`      | 4,926B | Simple runtime — loads brain, config, runs workers, logs events          |
| `workers.py`       | 3,323B | Small worker layer (WORKER_REGISTRY, WorkerResponse)                     |

## How to Run

1. Open terminal
1. `cd` into the unzipped folder
1. Run `python run_amos.py`
1. Logs to `logs/` and `memory/`

## AMOS.brain Control File

### Identity

- system_name: "AMOS Designer OS"
- owner: "Trang"
- mission: "Deterministic, auditable, humane intelligence for high-risk systems."

### Goals (4)

1. Model multi-layer reasoning and systemic behaviour
1. Maintain full auditability of every reasoning step
1. Keep humans in control, not the machine
1. Support sovereign-grade AI governance and compliance

### Constraints (4)

1. Deterministic execution (no hidden randomness)
1. Every decision must be loggable and explainable
1. No irreversible actions without explicit human confirmation
1. All worker actions pass through a single motor layer

### 7-Layer Brain Model

| Layer            | Description                                       |
| ---------------- | ------------------------------------------------- |
| sensory_layer    | Raw inputs: text, data, events, metrics           |
| perceptual_layer | Pattern detection from inputs                     |
| concept_layer    | Stable concepts, entities, relationships          |
| narrative_layer  | Stories, scenarios, timelines                     |
| causal_layer     | Cause-effect chains, interventions, levers        |
| systemic_layer   | Multi-system, multi-actor, multi-decade reasoning |
| meta_layer       | Self-audit, ethics, risk, invariants, boundaries  |

______________________________________________________________________

______________________________________________________________________

______________________________________________________________________

import json
from functools import lru_cache

## \_SPEC_JSON = r"""

### Source 3: Tech Engine\_\_Archive

> Path: `engine/T/Tech Engine__Archive.md` | Size: 92349 chars | Match score: 3 | content_hash: 6d78322c6f4a68cf

{
"TECH_ENGINE_V∞": {
"meta": {
"engine_name": "TECH_ENGINE_V∞",
"version": "∞.3",
"description": "Universal technical reasoning kernel for all technology domains, triple-density activated.",
"triple_density": true,
"linked_kernels": \[
"AMOS_CORE_V∞",
"ULF_CORE",
"ABSOLUTE_HUMAN_KERNEL",
"ABSOLUTE_UNIVERSE_KERNEL"
\],
"global_primitives": \[
"computation",
"information",
"causality",
"interaction",
"identity",
"structure",
"state",
"transition",
"resource",
"constraint",
"synchronization",
"signal",
"abstraction",
"composition",
"decomposition",
"failure",
"recovery",
"emergence",
"optimization"
\],
"global_lifecycle": \[
"Ideation",
"Specification",
"Architecture",
"Implementation",
"Integration",
"Validation",
"Deployment",
"Operation",
"Iteration",
"Retirement"
\],
"quality_axes": \[
"correctness",
"robustness",
"security",
"performance",
"scalability",
"maintainability",
"operability",
"usability",
"composability",
"compliance"
\]
},

```
"C01_software_engineering": {
  "subdomains": [
    "backend_systems",
    "frontend_web",
    "mobile_apps",
    "fullstack_delivery",
    "desktop_apps",
    "cli_tools",
    "scripting_automation"
  ],
  "roles": [
    "backend_engineer",
    "frontend_engineer",
    "fullstack_engineer",
    "mobile_engineer",
    "tech_lead",
    "system_architect",
    "software_generalist"
  ],
  "artifacts": [
    "api_specs",
    "service_contracts",
    "data_models",
    "module_designs",
    "codebases",
    "unit_tests",
    "integration_tests",
    "release_notes"
  ],
  "core_patterns": [
    "layered_architecture",
    "hexagonal_architecture",
    "clean_architecture",
    "microservices",
    "modular_monolith",
    "event_driven_architecture",
    "plugin_architecture"
  ],
  "triple_density_modes": [
    "low_level_code_reasoning",
    "system_level_design_reasoning",
    "org_level_software_strategy"
  ]
},

"C02_data_ai_ml": {
  "subdomains": [
    "analytics_engineering",
    "data_engineering",
    "data_warehousing",
    "business_intelligence",
    "machine_learning",
    "mlops_platforms",
    "llm_integration",
    "recommendation_systems",
    "causal_inference_systems"
  ],
  "roles": [
    "data_engineer",
    "analytics_engineer",
    "data_scientist",
    "ml_engineer",
    "mlops_engineer",
    "data_product_manager"
  ],
  "arti
```

______________________________________________________________________

**MOC:** references_MOC

## Related

- [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · references_MOC · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-designer-os-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/amos-designer-os/references/vault_domain_knowledge.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
