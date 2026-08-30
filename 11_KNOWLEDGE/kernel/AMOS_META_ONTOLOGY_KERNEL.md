---
title: AMOS META ONTOLOGY KERNEL V0 META COGNITION
tags:
- canon-group/biology
- canon/framework
- rscf/claim
- rscf/provenance
- rscf/state/source-claim
- topic/amos-meta-ontology-kernel-v0
- kernel
type: data
source: 11_KNOWLEDGE/kernel
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: AMOS_knowledge
---

# AMOS META ONTOLOGY KERNEL V0 META COGNITION

```json
{
  "kernel_id": "Meta_Ontology_Kernel",
  "version": "1.0.0",
  "source": "md/Core/AMOS_Meta_Ontology_Kernel_v0.md (category: meta_cognition, from AMOS_Omni_KERNEL.json)",
  "description": "Kernel for ontology — what exists, categories of being, structural reality mapping, entity classification, and the relationships between different kinds of things.",
  "group": "Kernels.Meta_Cognition",
  "category": "Meta_Cognition",
  "priority": 10,
  "required": true,
  "domains": ["ontology", "existence", "categories", "entities", "structure", "reality_mapping"],
  "depends_on": ["Meta_Logic_Kernel"],
  "meta": {
    "role": "Meta Ontology Kernel",
    "creator": "Trang Phan (Origin Architect)",
    "status": "defined",
    "binding_rules": ["Law_of_Law", "Rule_of_2", "Rule_of_4", "Absolute_Integrity"],
    "omni_category": "meta_cognition",
    "position": 2
  },
  "purpose": "Define what exists in the AMOS operational world and how entities are categorised. This kernel provides the ontological framework that all other kernels use to classify entities, map relationships, and reason about structure.",
  "ontological_levels": {
    "physical": "Things that exist in physical reality: bodies, objects, environments, biological systems",
    "social": "Things that exist through human agreement and interaction: institutions, roles, norms, contracts, money",
    "mental": "Things that exist in individual or collective mental states: beliefs, intentions, emotions, perceptions",
    "structural": "Things that exist as abstract structures: laws, algorithms, systems, relationships, patterns"
  },
  "entity_categories": {
    "agent": "Entities that act with intention: humans, organisations, AI systems, animals",
    "structure": "Entities that provide structure: laws, rules, systems, architectures, frameworks",
    "event": "Entities that happen: actions, decisions, transactions, state changes",
    "property": "Entities that describe: attributes, qualities, states, values",
    "relation": "Entities that connect: dependencies, influences, obligations, rights, correlations"
  },
  "relation_types": {
    "causal": "A causes B; B depends on A; A influences B",
    "constitutive": "A is part of B; A constitutes B; A is a type of B",
    "normative": "A obligates B; A permits B; A forbids B; A has right against B",
    "correlational": "A correlates with B; A co-occurs with B; A predicts B",
    "hierarchical": "A is above/below B; A governs B; B reports to A"
  },
  "classification_procedure": {
    "step_1": "Identify the entity or concept being classified",
    "step_2": "Determine ontological level (physical/social/mental/structural)",
    "step_3": "Determine entity category (agent/structure/event/property/relation)",
    "step_4": "Identify relevant properties",
    "step_5": "Identify relevant relations to other entities",
    "step_6": "Flag any ambiguous or contested classifications",
    "step_7": "Document classification rationale"
  },
  "rules": {
    "existence_claim_requires_ontology": "Any claim about what exists must be grounded in an ontological framework. Specify the level and category.",
    "category_confusion_detection": "Watch for category errors: treating a social construct as physical, a mental state as structural, or a relation as an entity.",
    "relation_clarity": "Every relation must specify type (causal/constitutive/normative/correlational/hierarchical), direction, and strength.",
    "multi_level_reasoning": "Entities can exist at multiple ontological levels simultaneously. Reasoning must track which level is being discussed."
  },
  "functions": {
    "classify_entity": {
      "description": "Classify an entity into ontological categories",
      "inputs": ["entity_description", "context", "available_classification_schemes"],
      "outputs": ["ontological_level", "entity_category", "properties", "relations", "classification_rationale", "ambiguity_flags"]
    },
    "map_relations": {
      "description": "Map relations between entities",
      "inputs": ["entity_A", "entity_B", "relation_description", "context"],
      "outputs": ["relation_type", "direction", "strength", "evidence_for_relation", "alternative_explanations"]
    },
    "detect_category_error": {
      "description": "Detect when reasoning confuses ontological categories",
      "inputs: ["reasoning_chain", "entities_involved", "claimed_relations"],
      "outputs": ["category_error_detected", "error_type", "affected_steps", "correction_suggestion"]
    }
  },
  "integration": {
    "provides_to": ["Meta_Logic_Kernel", "Structural_Reasoning", "Multi_Domain_Thinking", "All domain kernels"],
    "used_by": ["All reasoning", "HIE pipeline (S1, S5)", "Entity and relation extraction"],
    "routes_to": "ROUTE_DEFAULT (always active), specialized routes when domain-specific ontology needed"
  },
  "safety_constraints": {
    "never_reify_abstract_concepts_without_clarifying_level": true,
    "never_confuse_social_construct_with_physical_reality": true,
    "never_assert_entity_existence_without_classification": true,
    "always_flag_ambiguous_classifications": true
  },
  "evaluation": {
    "unit_tests": [
      "Classify a physical entity: returns physical level, structure/event/property category",
      "Classify a social entity (e.g., 'contract'): returns social level, structure category",
      "Detect category error (treating 'law' as physical force): returns error detected",
      "Map causal relation between two entities: returns relation_type=causal, direction, strength"
    ],
    "failure_modes": [
      "Failing to classify entity at all",
      "Classifying social construct as physical",
      "Missing relation types",
      "Not flagging ambiguous classifications"
    ]
  }
}

---
**Related:** [[11_KNOWLEDGE/kernel/COMPLIANCE_KERNEL|COMPLIANCE_KERNEL]] · [[11_KNOWLEDGE/kernel/AMOS_SECURITY_ARCHITECTURE_KERNEL_V0_TECH|AMOS_SECURITY_ARCHITECTURE_KERNEL_V0_TECH]] · [[11_KNOWLEDGE/kernel/FINANCE_SENSOR_KERNEL|FINANCE_SENSOR_KERNEL]] · [[11_KNOWLEDGE/kernel/COGNITION_KERNEL|COGNITION_KERNEL]]
```

---
**MOC:** [[11_KNOWLEDGE/kernel/KERNEL_MOC|KERNEL_MOC]]

