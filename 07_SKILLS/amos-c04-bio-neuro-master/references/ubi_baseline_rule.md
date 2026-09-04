---
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
title: ubi baseline rule
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

# UBI Baseline Rule

> Source: `_00_Cosmo brain/biology-ubi/ubi_baseline_rule.md`
> Epistemic class: SOURCE_DERIVED

______________________________________________________________________

## tags: [biology-ubi]

{
"id": "ubi.rule.baseline",
"name": "UBI Baseline Rule",
"description": "Baseline rule for UBI state initialization and integrity checks. Ensures UBI state is properly initialized and within bounds.",
"layer_id": "ubi",
"domain_id": "regulation",
"tags": {
"family": "ubi",
"kind": "rule",
"type": "baseline"
},
"invariant_ids": ["ubi.integrity.bounds"],
"operator_ids": ["ubi.operator.recompute_integrity"],
"priority": 1.0
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
node_id: amos-c04-bio-neuro-master-ubi-baseline-rule
node_type: reference
path: 07_SKILLS/amos-c04-bio-neuro-master/references/ubi_baseline_rule.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
