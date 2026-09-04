---
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
title: nervous system state drift
type: reference
source: 07_SKILLS/amos-context-persona-drift-rscf/references
tags:
  - reference
  - amos-context-persona-drift-rscf
  - type/skill
  - system-scan-agent
  - automation-profiles
  - amos-simulation-kernel-v0-math-foundations
  - law-hierarchy
  - trang-framework-recursive-ontology-dynamics
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---

# Nervous System States for Drift

> Source: `_00_Cosmo brain/system/Nervous_System_States.md`
> Epistemic class: SOURCE_DERIVED

______________________________________________________________________

## tags: [system]

{
"version": "1.0",
"description": "Nervous system state patterns for UBI",
"states": {
"calm_focus": {
"id": "calm_focus",
"name": "Calm Focus",
"description": "Balanced state with good focus capacity",
"sympathetic_activation": 0.5,
"parasympathetic_activation": 0.5,
"vagal_tone_band": "medium",
"somatic_tension_band": "low",
"interoceptive_clarity_band": "medium",
"tags": {
"type": "balanced",
"optimal": "true"
}
},
"hyper_vigilance": {
"id": "hyper_vigilance",
"name": "Hyper-Vigilance",
"description": "High stress, low energy state with hyper-vigilance",
"sympathetic_activation": 0.8,
"parasympathetic_activation": 0.2,
"vagal_tone_band": "low",
"somatic_tension_band": "high",
"interoceptive_clarity_band": "low",
"tags": {
"type": "stress",
"requires_rest": "true"
}
},
"shutdown": {
"id": "shutdown",
"name": "Shutdown Tendency",
"description": "Low energy, low activation state",
"sympathetic_activation": 0.2,
"parasympathetic_activation": 0.8,
"vagal_tone_band": "high",
"somatic_tension_band": "low",
"interoceptive_clarity_band": "low",
"tags": {
"type": "low_energy",
"requires_regeneration": "true"
}
},
"flow": {
"id": "flow",
"name": "Flow State",
"description": "High energy, low stress flow state",
"sympathetic_activation": 0.6,
"parasympathetic_activation": 0.4,
"vagal_tone_band": "high",
"somatic_tension_band": "low",
"interoceptive_clarity_band": "high",
"tags": {
"type": "optimal",
"optimal": "true"
}
},
"somatic_overload": {
"id": "somatic_overload",
"name": "Somatic Overload",
"description": "High somatic tension and overload",
"sympathetic_activation": 0.9,
"parasympathetic_activation": 0.1,
"vagal_tone_band": "low",
"somatic_tension_band": "very_high",
"interoceptive_clarity_band": "low",
"tags": {
"type": "overload",
"requires_rest": "true"
}
}
}
}

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]] · AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS · SYSTEM_SCAN_AGENT · AUTOMATION_PROFILES

______________________________________________________________________

## **MOC:** references_MOC

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · references_MOC · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-context-persona-drift-rscf-nervous-system-state-drift
node_type: reference
path: 07_SKILLS/amos-context-persona-drift-rscf/references/nervous_system_state_drift.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
