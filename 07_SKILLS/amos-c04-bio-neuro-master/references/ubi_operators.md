---
title: ubi operators
type: reference
source: 07_SKILLS/amos-c04-bio-neuro-master/references
tags:
- reference
- amos-c04-bio-neuro-master
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

# UBI Operators

> Source: `_00_Cosmo brain/biology-ubi/UBI_Operators.md`
> Epistemic class: SOURCE_DERIVED

---
tags: [biology-ubi]
---
{
  "version": "1.0",
  "description": "UBI operators for biological intelligence",
  "operators": {
    "op.recommend_rest": {
      "id": "op.recommend_rest",
      "name": "Recommend Rest",
      "description": "Recommends rest when energy is low or stress is high",
      "conditions": {
        "energy_band": "low",
        "or": {
          "stress_band": ["high", "very_high"]
        }
      },
      "action": "recommend_rest",
      "tags": {
        "domain": "biological",
        "type": "recommendation"
      }
    },
    "op.recommend_focus_shift": {
      "id": "op.recommend_focus_shift",
      "name": "Recommend Focus Shift",
      "description": "Recommends shifting focus when overload is detected",
      "conditions": {
        "overload_detected": true
      },
      "action": "recommend_focus_shift",
      "tags": {
        "domain": "biological",
        "type": "recommendation"
      }
    },
    "op.recommend_break_pattern": {
      "id": "op.recommend_break_pattern",
      "name": "Recommend Break Pattern",
      "description": "Recommends breaking current pattern when stress accumulates",
      "conditions": {
        "stress_accumulation": "high",
        "pattern_duration": "long"
      },
      "action": "recommend_break_pattern",
      "tags": {
        "domain": "biological",
        "type": "recommendation"
      }
    }
  }
}

---
**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]] · AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS · SYSTEM_SCAN_AGENT · AUTOMATION_PROFILES

---
**MOC:** references_MOC
---

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · references_MOC · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-c04-bio-neuro-master-ubi-operators
node_type: reference
path: 07_SKILLS/amos-c04-bio-neuro-master/references/ubi_operators.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
