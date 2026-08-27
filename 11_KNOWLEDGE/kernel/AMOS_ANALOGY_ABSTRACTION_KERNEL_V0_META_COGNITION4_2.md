---
tags: [canon-group/biology, canon/framework, rscf/claim, rscf/provenance, rscf/state/source-claim, topic/amos-analogy-abstraction-kernel-v0, kernel]
---

{
  "kernel_id": "Analogy_Abstraction_Kernel",
  "version": "1.0.0",
  "source": "md/Core/AMOS_Analogy_Abstraction_Kernel_v0.md (category: meta_cognition, from AMOS_Omni_KERNEL.json)",
  "description": "Kernel for analogy and abstraction — mapping structural similarities across domains, extracting abstract patterns from concrete instances, and using analogical reasoning while avoiding false analogies.",
  "group": "Kernels.Meta_Cognition",
  "category": "Meta_Cognition",
  "priority": 9,
  "required": true,
  "domains": ["analogy", "abstraction", "pattern_matching", "cross_domain", "metaphor", "structural_similarity"],
  "depends_on": ["Meta_Logic_Kernel", "Meta_Ontology_Kernel", "Cognitive_Compression_Kernel"],
  "meta": {
    "role": "Analogy and Abstraction Kernel",
    "creator": "Trang Phan (Origin Architect)",
    "status": "defined",
    "binding_rules": ["Law_of_Law", "Rule_of_2", "Rule_of_4", "Absolute_Integrity"],
    "omni_category": "meta_cognition",
    "position": 5
  },
  "purpose": "Enable analogical reasoning across domains by identifying structural similarities, extracting abstract patterns, and using analogies productively while detecting and avoiding false or misleading analogies.",
  "analogy_structure": {
    "source_domain": "The domain being mapped FROM (already understood)",
    "target_domain": "The domain being mapped TO (being understood via analogy)",
    "mapper": "What maps between source and target; the structural correspondence",
    "alignment": "Which elements of source correspond to which elements of target",
    "inferences": "What can be inferred about target based on source knowledge"
  },
  "valid_analogy_criteria": {
    "structural_similarity": "The mapping must preserve structural relationships, not just surface features",
    "relevant_properties_mapped": "Properties relevant to the reasoning task must be mappable between domains",
    "no_critical_differences_ignored": "Known critical differences between domains must be acknowledged, not hidden",
    "bounded_scope": "The analogy has a defined scope; it does not claim to explain everything about the target",
    "productive": "The analogy generates useful inferences, not just decorative similarity"
  },
  "false_analogy_detection": {
    "surface_only": "Mapping based on superficial similarity (name, appearance) without structural correspondence",
    "ignoring_critical_differences": "Hidden or ignored differences that break the mapping for the current purpose",
    "over_extension": "Pushing the analogy beyond its valid scope to draw conclusions it doesn't support",
    "category_error_in_mapping": "Mapping entities from different ontological categories as if they're equivalent",
    "false_precision": "Treating the analogy as more precise than it is; using it as proof rather than illustration"
  },
  "rules": {
    "analogy_illustrates_not_proves": "An analogy can illustrate a structural point but cannot serve as proof. Always distinguish illustration from evidence.",
    "scope_must_be_explicit": "Define what the analogy does and does not cover. Don't let the listener over-extend it.",
    "differences_must_be_acknowledged": "State the critical differences between source and target that limit the analogy's applicability.",
    "abstraction_level_match": "The abstraction level of source and target should be comparable. Don't map a concrete entity to an abstract principle without clarifying."
  },
  "abstraction_procedure": {
    "step_1": "Identify the concrete instance or domain being abstracted",
    "step_2": "Extract objects/entities and their properties",
    "step_3": "Extract relations between entities",
    "step_4": "Identify the pattern that recurs across instances",
    "step_5": "Formulate the abstract schema (entities + relations without domain-specific content)",
    "step_6": "Test the abstract schema against other instances",
    "step_7": "Refine: add constraints that distinguish valid from invalid applications"
  },
  "functions": {
    "find_analogy": {
      "description": "Find a useful analogy for a target concept or domain",
      "inputs": ["target_concept", "target_domain", "purpose_of_analogy", "available_source_domains"],
      "outputs": ["analogy_source", "mapping_table", "inferences_generated", "critical_differences", "scope_boundaries", "false_analogy_warnings"]
    },
    "extract_abstraction": {
      "description": "Extract an abstract pattern from concrete instances",
      "inputs": ["instances", "common_properties", "common_relations"],
      "outputs": ["abstract_schema", "applicability_constraints", "example_instances", "non_example_instances"]
    },
    "evaluate_analogy_quality": {
      "description": "Evaluate whether an analogy is valid and productive",
      "inputs: ["analogy_mapping", "purpose", "known_differences", "inferences_drawn"],
      "outputs": ["quality_assessment", "validity_score", "productive_for_purpose", "warnings", "recommended_scope"]
    }
  },
  "integration": {
    "provides_to": ["Meta_Logic_Kernel", "Structural_Reasoning", "Multi_Domain_Thinking", "Cognitive_Compression_Kernel"],
    "used_by": ["Cross-domain reasoning", "Explanation generation", "Concept learning"],
    "routes_to": "ROUTE_DEFAULT, ROUTE_TECH (when mapping tech concepts), ROUTE_PSYCH (when mapping psychological concepts)"
  },
  "safety_constraints": {
    "never_use_analogy_as_proof": true,
    "never_hide_critical_differences": true,
    "never_over_extend_analogy_scope": true,
    "always_state_scope_boundaries": true,
    "always_warn_when_analogy_is_weak": true
  },
  "evaluation": {
    "unit_tests": [
      "Find analogy for a complex concept: returns source + mapping + inferences + differences + scope",
      "Extract abstraction from 3 similar instances: returns abstract_schema + constraints",
      "Evaluate a false analogy (surface-only mapping): returns quality_assessment=low, false_analogy_detected",
      "Evaluate a valid structural analogy: returns quality_assessment=high, productive_for_purpose"
    ],
    "failure_modes": [
      "Presenting analogy as proof",
      "Not acknowledging critical differences",
      "Over-extending analogy to unsupported conclusions",
      "False precision from weak analogy"
    ]
  }
}

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
