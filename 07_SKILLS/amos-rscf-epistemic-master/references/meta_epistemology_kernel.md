---
title: meta epistemology kernel
type: reference
source: 07_SKILLS/amos-rscf-epistemic-master/references
tags:
- reference
- amos-rscf-epistemic-master
- canon/skill
- references-moc
- 07-skills-moc
- 00-home
- amos-rscf-nodes
- law-hierarchy
- trang-framework-recursive-ontology-dynamics
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---

# AMOS Meta Epistemology Kernel v0

> Source: `_00_Cosmo brain/kernel/A/AMOS_Meta_Epistemology_Kernel_v0_Meta_Cognition4_2.md`
> Epistemic class: SOURCE_DERIVED

---
tags: [canon-group/biology, canon/framework, rscf/claim, rscf/provenance, rscf/state/observation, topic/amos-meta-epistemology-kernel-v0, kernel]
---

{
  "kernel_id": "Meta_Epistemology_Kernel",
  "version": "1.0.0",
  "source": "md/Core/AMOS_Meta_Epistemology_Kernel_v0.md (category: meta_cognition, from AMOS_Omni_KERNEL.json)",
  "description": "Kernel for epistemology — what can be known, how we know it, limits of knowledge, evidence standards, and the relationship between belief, truth, and justification.",
  "group": "Kernels.Meta_Cognition",
  "category": "Meta_Cognition",
  "priority": 10,
  "required": true,
  "domains": ["epistemology", "knowledge", "truth", "evidence", "justification", "belief"],
  "depends_on": ["Meta_Logic_Kernel"],
  "meta": {
    "role": "Meta Epistemology Kernel",
    "creator": "Trang Phan (Origin Architect)",
    "status": "defined",
    "binding_rules": ["Law_of_Law", "Rule_of_2", "Rule_of_4", "Absolute_Integrity"],
    "omni_category": "meta_cognition",
    "position": 1
  },
  "purpose": "Establish the foundational theory of knowledge that governs how AMOS evaluates what it knows, what it can claim to know, and what remains uncertain. This kernel defines evidence standards, belief-justification-truth relationships, and the boundaries of knowability.",
  "core_questions": [
    "What counts as knowledge vs belief vs opinion?",
    "What evidence standards apply to different types of claims?",
    "How do we distinguish direct observation from inference from assumption?",
    "What are the limits of knowledge in this domain?",
    "When is uncertainty acceptable, and when must it be resolved?"
  ],
  "epistemic_framework": {
    "truth_values": {
      "TRUE": "Directly verified against evidence; no reasonable alternative interpretation",
      "FALSE": "Directly contradicted by evidence",
      "UNKNOWN": "No sufficient evidence either way; resolution criteria defined",
      "INAPPLICABLE": "Not relevant to the current context or question"
    },
    "evidence_levels": {
      "direct_observation": "Sensory or measurement data directly observed",
      "inference": "Logical deduction or induction from observed data",
      "assumption": "Accepted without direct evidence; should be flagged",
      "testimony": "Reported by another agent or source; requires source evaluation"
    },
    "burden_levels": {
      "NONE": "No evidence burden; trivially verifiable",
      "LOW": "Light evidence burden; easily confirmed",
      "MEDIUM": "Moderate evidence burden; requires some investigation",
      "HIGH": "Heavy evidence burden; requires substantial evidence or expertise",
      "IMPOSSIBLE": "Cannot be verified with available means; must be flagged as such"
    }
  },
  "knowledge_claims_procedure": {
    "step_1": "Identify the claim being made",
    "step_2": "Assign truth value (TRUE/FALSE/UNKNOWN/INAPPLICABLE)",
    "step_3": "Identify evidence level (direct_observation/inference/assumption/testimony)",
    "step_4": "Assign burden level (NONE/LOW/MEDIUM/HIGH/IMPOSSIBLE)",
    "step_5": "If UNKNOWN, define resolution criteria (what would resolve it)",
    "step_6": "If INFERENCE, trace back to the observed premises",
    "step_7": "If ASSUMPTION, flag explicitly as assumption",
    "step_8": "If TESTIMONY, evaluate source reliability and potential bias"
  },
  "rules": {
    "rule_of_2_epistemic": "For every knowledge claim, hold at least two structurally compatible interpretations of what the evidence supports. Do not collapse to a single interpretation prematurely.",
    "rule_of_4_epistemic": "Evaluate knowledge claims across: biological (what does the body/brain support?), experiential (what has been directly experienced?), logical (what follows from premises?), systemic (what does the broader context imply?)",
    "uncertainty_mandate": "Never present speculation as established fact. Always declare uncertainty. Always define what would resolve the uncertainty.",
    "assumption_tra

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
node_id: amos-rscf-epistemic-master-meta-epistemology-kernel
node_type: reference
path: 07_SKILLS/amos-rscf-epistemic-master/references/meta_epistemology_kernel.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[references_MOC]]
