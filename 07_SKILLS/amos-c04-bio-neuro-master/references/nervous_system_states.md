---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Nervous System States
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

# Nervous System States

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
node_id: amos-c04-bio-neuro-master-nervous-system-states
node_type: reference
path: 07_SKILLS/amos-c04-bio-neuro-master/references/nervous_system_states.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
