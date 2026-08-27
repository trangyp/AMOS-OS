---
title: ubi baseline rule
type: reference
source: 07_SKILLS/amos-c04-bio-neuro-master/references
tags: [reference, amos-c04-bio-neuro-master, canon/skill]
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
