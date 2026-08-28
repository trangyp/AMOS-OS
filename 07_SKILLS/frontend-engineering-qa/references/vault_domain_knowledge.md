---
title: Vault Domain Knowledge — Frontend Engineering Qa
type: reference
source: 07_SKILLS/frontend-engineering-qa/references
tags:
- reference
- frontend-engineering-qa
- canon/skill
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# Vault-Sourced Domain Knowledge

> Source: AMOS_OS Obsidian vault (`_00_Cosmo brain/`)
> Epistemic class: SOURCE_CLAIM
> Extracted from skill: `frontend-engineering-qa`

## Vault-Sourced Content


import json
from functools import lru_cache

_SPEC_JSON = r"""
---

### Source 2: Tech Engine__Archive

> Path: `engine/T/Tech Engine__Archive.md` | Size: 92349 chars | Match score: 3 | content_hash: 6d78322c6f4a68cf

{
  "TECH_ENGINE_V∞": {
    "meta": {
      "engine_name": "TECH_ENGINE_V∞",
      "version": "∞.3",
      "description": "Universal technical reasoning kernel for all technology domains, triple-density activated.",
      "triple_density": true,
      "linked_kernels": [
        "AMOS_CORE_V∞",
        "ULF_CORE",
        "ABSOLUTE_HUMAN_KERNEL",
        "ABSOLUTE_UNIVERSE_KERNEL"
      ],
      "global_primitives": [
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
      ],
      "global_lifecycle": [
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
      ],
      "quality_axes": [
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
      ]
    },

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

---

### Source 3: amos_consulting_amos_invest_amos_canon_tech_engine

> Path: `engine/A/amos_consulting_amos_invest_amos_canon_tech_engine.md` | Size: 92134 chars | Match score: 3 | content_hash: bb926f76c0b9bc21

{
  "TECH_ENGINE_V∞": {
    "meta": {
      "engine_name": "TECH_ENGINE_V∞",
      "version": "∞.3",
      "description": "Universal technical reasoning kernel for all technology domains, triple-density activated.",
      "triple_density": true,
      "linked_kernels": [
        "AMOS_CORE_V∞",
        "ULF_CORE",
        "ABSOLUTE_HUMAN_KERNEL",
        "ABSOLUTE_UNIVERSE_KERNEL"
      ],
      "global_primitives": [
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
      ],
      "global_lifecycle": [
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
      ],
      "quality_axes": [
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
      ]
    },

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

---
**MOC:** [[references_MOC]]

## Related

- [[07_SKILLS_MOC]]
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[references_MOC]] · [[07_SKILLS_MOC]]

**MOC:** [[references_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: frontend-engineering-qa-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/frontend-engineering-qa/references/vault_domain_knowledge.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[references_MOC]]
