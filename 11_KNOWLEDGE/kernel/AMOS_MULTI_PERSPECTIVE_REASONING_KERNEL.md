---
title: AMOS MULTI PERSPECTIVE REASONING KERNEL V0 META COGNITION4 2
tags:
- canon-group/biology
- canon/framework
- rscf/claim
- rscf/provenance
- rscf/state/source-claim
- topic/amos-multi-perspective-reasoning-kernel-
- kernel
type: data
source: 11_KNOWLEDGE/kernel
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: AMOS_knowledge
---

# AMOS MULTI PERSPECTIVE REASONING KERNEL V0 META COGNITION4 2

```json
{
  "kernel_id": "Multi_Perspective_Reasoning_Kernel",
  "version": "1.0.0",
  "source": "md/Core/AMOS_Multi_Perspective_Reasoning_Kernel_v0.md (category: meta_cognition, from AMOS_Omni_KERNEL.json)",
  "description": "Kernel for multi-perspective reasoning — holding, comparing, and integrating multiple viewpoints on the same subject, detecting bias through perspective gaps, and synthesising coherent conclusions from competing interpretations.",
  "group": "Kernels.Meta_Cognition",
  "category": "Meta_Cognition",
  "priority": 9,
  "required": true,
  "domains": ["multi_perspective", "viewpoint", "bias_detection", "perspective-taking", "integration", "competing_interpretations"],
  "depends_on": ["Meta_Logic_Kernel", "Meta_Epistemology_Kernel", "Counterfactual_Reasoning_Kernel", "Psychology_Decision_Kernel"],
  "meta": {
    "role": "Multi-Perspective Reasoning Kernel",
    "creator": "Trang Phan (Origin Architect)",
    "status": "defined",
    "binding_rules": ["Law_of_Law", "Rule_of_2", "Rule_of_4", "Absolute_Integrity"],
    "omni_category": "meta_cognition",
    "position": 7
  },
  "purpose": "Enable reasoning that holds multiple perspectives simultaneously, compares them structurally, detects where perspectives diverge and why, and integrates them into conclusions that respect the tensions rather than collapsing them.",
  "perspective_dimensions": {
    "agent_perspective": "How different agents (humans, organisations, systems) view the same situation based on their position, incentives, knowledge, and values",
    "disciplinary_perspective": "How different domains of knowledge (biology, economics, psychology, engineering, law) frame the same phenomenon",
    "temporal_perspective": "How the same situation looks from short-term vs medium-term vs long-term time horizons",
    "scale_perspective": "How the same situation looks at micro vs meso vs macro scale; what's visible at each level",
    "value_perspective": "How different values and ethical frameworks evaluate the same situation or decision"
  },
  "perspective_holding_procedure": {
    "step_1": "Identify the subject or question being reasoned about",
    "step_2": "Identify relevant perspectives (which agents, disciplines, time horizons, scales, values are relevant?)",
    "step_3": "For each perspective, construct the most charitable version: what would a competent holder of that perspective say?",
    "step_4": "Map where perspectives agree (overlap) and where they diverge (tension points)",
    "step_5": "For each tension point, identify the source of divergence: different facts? different values? different time horizons? different scale? different incentives?",
    "step_6": "Check whether any perspective is being under-represented or straw-manned",
    "step_7": "Synthesize: what can be concluded that respects the divergences? What remains genuinely contested?"
  },
  "tension_types": {
    "factual_tension": "Perspectives disagree on what is the case; resolution requires evidence",
    "value_tension": "Perspectives agree on facts but disagree on what matters; resolution requires value clarification, not more facts",
    "temporal_tension": "Short-term and long-term perspectives diverge; resolution requires explicit time-horizon trade-off",
    "scale_tension": "What's optimal at one scale is suboptimal at another; resolution requires scale-specific analysis",
    "incentive_tension": "Perspectives diverge because agents have different incentives; resolution requires incentive analysis"
  },
  "rules": {
    "hold_perspectives_charitably": "Construct each perspective in its strongest form before evaluating. Straw-manning perspectives is a structural failure.",
    "tension_is_information": "Divergence between perspectives is not a problem to eliminate — it's information about the structure of the situation. Don't collapse tensions prematurely.",
    "identify_the_source": "When perspectives diverge, identify WHY. Different facts → evidence. Different values → value analysis. Different incentives → incentive analysis.",
    "synthesis_respects_tension": "A good synthesis doesn't hide tensions; it shows where they are, what they mean, and what can still be concluded.",
    "rule_of_2_integrated": "This kernel operationalizes the Rule of 2: hold at least two structurally compatible interpretations."
  },
  "functions": {
    "identify_perspectives": {
      "description": "Identify the relevant perspectives on a subject",
      "inputs": ["subject", "context", "question_being_asked", "available_domain_knowledge"],
      "outputs": ["perspective_list", "perspective_descriptions", "relevance_rationale", "missing_perspectives_if_any"]
    },
    "map_perspective_agreement_divergence": {
      "description": "Map where multiple perspectives agree and diverge",
      "inputs: ["perspectives", "subject", "claims_being_compared"],
      "outputs": ["agreement_map", "divergence_points", "tension_type_for_each_divergence", "source_of_each_divergence", "charitability_check"]
    },
    "synthesize_multi_perspective": {
      "description": "Synthesize a conclusion from multiple perspectives",
      "inputs: ["perspectives", "agreement_divergence_map", "question", "decision_context"],
      "outputs": ["synthesis", "tensions_preserved", "contested_areas", "confidence_by_area", "what_additional_perspective_would_help"]
    }
  },
  "integration": {
    "provides_to": ["Meta_Logic_Kernel", "Counterfactual_Reasoning_Kernel", "Strategic_Analysis", "Ethics_Reasoning"],
    "used_by": ["All complex reasoning", "Bias detection", "Stakeholder analysis", "Decision-making", "Conflict resolution"],
    "routes_to": "ROUTE_DEFAULT (always active for complex questions), ROUTE_PSYCH (when perspectives are psychological), ROUTE_TECH (when perspectives are technical)"
  },
  "safety_constraints": {
    "never_straw_man_opposite_perspective": true,
    "never_collapse_tensions_precisely": true,
    "never_conceal_value_tensions_as_factual": true,
    "always_identify_missing_perspectives": true,
    "always_distinguish_fact_tension_from_value_tension": true
  },
  "evaluation": {
    "unit_tests": [
      "Identify perspectives on a complex policy question: returns perspective_list with relevance + missing_perspectives",
      "Map agreement/divergence across 3 perspectives: returns agreement_map + divergence_points + tension_types",
      "Detect straw-manning of a perspective: returns charitability_failure",
      "Synthesize multi-perspective conclusion: returns synthesis + tensions_preserved + contested_areas"
    ],
    "failure_modes": [
      "Straw-manning an opposing perspective",
      "Collapsing genuine tensions into false agreement",
      "Treating value disagreement as factual disagreement",
      "Missing a relevant perspective entirely",
      "Not identifying the source of divergence"
    ]
  }
}

---
**Related:** [[SYSTEM_SENSOR_KERNEL]] · [[KERNEL_PROTOCOL]] · [[AMOS_COGNITION_TOTAL_KERNEL]] · [[AMOS_BIZFIN_KERNEL_V0]]
```

---
**MOC:** [[KERNEL_MOC]]

