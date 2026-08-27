---
title: AMOS COUNTERFACTUAL REASONING KERNEL V0 META COGNITION4 2
tags: [canon-group/biology, canon/framework, rscf/claim, rscf/provenance, rscf/state/source-claim, topic/amos-counterfactual-reasoning-kernel-v0, kernel]
type: data
source: 11_KNOWLEDGE/kernel
rscf:
  state: SOURCE_CLAIM
  claim_class: CONDITIONAL
  provenance: AMOS_corpus
  scope: AMOS_knowledge

---
# AMOS COUNTERFACTUAL REASONING KERNEL V0 META COGNITION4 2

```json
{
  "kernel_id": "Counterfactual_Reasoning_Kernel",
  "version": "1.0.0",
  "source": "md/Core/AMOS_Counterfactual_Reasoning_Kernel_v0.md (category: meta_cognition, from AMOS_Omni_KERNEL.json)",
  "description": "Kernel for counterfactual reasoning — what-if analysis, alternative scenario reasoning, reasoning about events that did not happen, and causal inference through comparison of actual vs hypothetical states.",
  "group": "Kernels.Meta_Cognition",
  "category": "Meta_Cognition",
  "priority": 9,
  "required": true,
  "domains": ["counterfactual", "what_if", "alternative_scenarios", "causal_inference", "hypothetical_reasoning", "scenario_analysis"],
  "depends_on": ["Meta_Logic_Kernel", "Meta_Epistemology_Kernel", "Probability_Statistics_Kernel"],
  "meta": {
    "role": "Counterfactual Reasoning Kernel",
    "creator": "Trang Phan (Origin Architect)",
    "status": "defined",
    "binding_rules": ["Law_of_Law", "Rule_of_2", "Rule_of_4", "Absolute_Integrity"],
    "omni_category": "meta_cognition",
    "position": 6
  },
  "purpose": "Enable reasoning about alternative scenarios — what would have happened if X had been different, what could happen if Y changes, and what causal relationships can be inferred by comparing actual outcomes with hypothetical alternatives.",
  "counterfactual_types": {
    "past_counterfactual": "What would have happened if something in the past had been different? (e.g., 'If we had launched earlier...')",
    "future_counterfactual": "What would happen if something changes in the future? (e.g., 'If we increase price by 10%...')",
    "structural_counterfactual": "What does the structure imply would happen under different conditions? (e.g., 'Given this system design, if load doubles...')",
    "causal_counterfactual": "What can we infer about causation by comparing what happened with what would have happened without the cause?"
  },
  "valid_counterfactual_criteria": {
    "plausible_initial_state": "The counterfactual starting point must be plausible or clearly flagged as implausible",
    "minimal_change_principle": "Change only what's necessary for the counterfactual; don't silently change other things",
    "causal_chain_conservation": "Respect the causal structure: if A causes B causes C, changing A propagates through B to C",
    "uncertainty_proportionate": "The further from actuality, the larger the uncertainty. Near-counterfactuals are more reliable than far ones.",
    "assumption_transparency": "All assumptions about how the world would differ must be explicit"
  },
  "common_errors": {
    "over_determination": "Assuming the counterfactual outcome would definitely be X without considering other influencing factors",
    "ignoring_system_reactions": "Treating the system as static when it would react to the change",
    "confusing_correlation_with_causation": "Assuming that because B followed A, changing A would change B",
    "unrealistic_baseline": "Comparing against an unrealistic or cherry-picked baseline",
    "hidden_changes": "Silently changing multiple things in the counterfactual, making the result misleading"
  },
  "rules": {
    "counterfactual_needs_causal_model": "Valid counterfactual reasoning requires a causal model of how things are connected. Without it, you're guessing.",
    "uncertainty_grows_with_distance": "The more different the counterfactual world is from actuality, the larger the uncertainty. State this explicitly.",
    "minimal_intervention": "Change only what's specified. Don't silently assume other things stay the same when they likely wouldn't.",
    "counterfactual_is_not_prediction": "A counterfactual is a reasoned exploration of alternatives, not a prediction. Label it as such."
  },
  "functions": {
    "construct_counterfactual": {
      "description": "Construct a counterfactual scenario from an actual state",
      "inputs": ["actual_state", "intervention_description", "causal_model", "plausibility_constraints"],
      "outputs": ["counterfactual_state", "causal_chain", "uncertainties", "assumption_list", "plausibility_assessment", "alternative_outcomes"]
    },
    "compare_actual_vs_counterfactual": {
      "description": "Compare actual outcome with counterfactual outcome",
      "inputs":["actual_outcome", "counterfactual_outcome", "causal_model", "confidence_levels"],
      "outputs": ["difference_analysis", "causal_attribution", "confounding_factors", "attribution_confidence", "alternative_explanation"]
    },
    "scenario_analysis": {
      "description": "Analyze multiple future counterfactual scenarios",
      "inputs: ["current_state", "scenario_list", "uncertainty_model", "decision_criteria"],
      "outputs": ["scenario_outcomes", "probability_assignments_if_available", "recommended_preparation", "early_warning_signals", "scenario_comparison"]
    }
  },
  "integration": {
    "provides_to": ["Meta_Logic_Kernel", "Multi_Perspective_Reasoning_Kernel", "Strategy_Game_Engine", "Risk_Assessment"],
    "used_by": ["Decision analysis", "Risk assessment", "Strategic planning", "Causal inference", "Policy evaluation"],
    "routes_to": "ROUTE_DEFAULT, specialized routes when counterfactual is domain-specific"
  },
  "safety_constraints": {
    "never_present_counterfactual_as_fact": true,
    "never_ignore_uncertainty_in_far_counterfactuals": true,
    "always_state_assumptions_explicitly": true,
    "always_label_counterfactual_as_counterfactual": true,
    "never_use_counterfactual_to_over_determine_outcomes": true
  },
  "evaluation": {
    "unit_tests": [
      "Construct past counterfactual with causal model: returns counterfactual_state + causal_chain + uncertainties",
      "Compare actual vs counterfactual: returns difference_analysis + causal_attribution + confounding_factors",
      "Detect over_determination error (assuming single outcome): returns error_flagged",
      "Scenario analysis with 3 alternatives: returns scenario_outcomes + recommended_preparation"
    ],
    "failure_modes": [
      "Presenting counterfactual as certain prediction",
      "Ignoring system reactions to change",
      "Over-determining outcome without considering alternatives",
      "Hidden multiple changes in counterfactual"
    ]
  }
}

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]
```

---
**MOC:** [[KERNEL_MOC]]
