---
title: ubi baseline rule
type: reference
source: 07_SKILLS/amos-c04-bio-neuro-master/references
tags:
- reference
- amos-c04-bio-neuro-master
- canon/skill
- 00-home
- knowledge-moc
- system-scan-agent
- automation-profiles
- references-moc
- amos-simulation-kernel-v0-math-foundations
- amos-rscf-nodes
- law-hierarchy
- 07-skills-moc
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

---
tags: [biology-ubi]
---
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

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[references_MOC]]
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[references_MOC]] · [[07_SKILLS_MOC]]

**MOC:** [[references_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-c04-bio-neuro-master-ubi-baseline-rule
node_type: reference
path: 07_SKILLS/amos-c04-bio-neuro-master/references/ubi_baseline_rule.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[references_MOC]]
