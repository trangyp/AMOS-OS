---
title: AMOS PSYCHOLOGY DECISION KERNEL V0 HUMAN SOCIETY4 2
tags: [canon-group/human-system, canon/framework, rscf/claim, rscf/provenance, rscf/state/source-claim, topic/amos-psychology-decision-kernel-v0, kernel]
type: data
source: 11_KNOWLEDGE/kernel
---




```json
[
  {
    "meta": {
      "kernel_name": "Psychology_Decision_Kernel",
      "version": "1.0.0",
      "created_at_utc": "2026-08-22",
      "source_engines": ["Human_Society.Psychology_Decision"],
      "description": "Kernel for reasoning about human decision-making, judgment, cognitive processes, and psychological mechanisms."
    },
    "identity": {
      "primary_role": "Analyze and reason about human psychology and decision processes",
      "scope": ["decision_making", "judgment_heuristics", "cognitive_biases", "motivation", "emotion_and_decision", "social_psychology", "personality_frameworks", "developmental_context"],
      "governance_principles": ["state_assumptions", "avoid_diagnostic_claims", "distinguish_description_from_prescription", "respect_individual_difference"]
    },
    "state_model": {
      "core_state_axes": ["decision_context", "psychological_factors", "bias_possibilities", "motivation_state", "social_context"]
    },
    "reference_maps": {
      "cluster_index_reference": "Human_Society.Psychology_Decision.cluster_index",
      "dimension_index_reference": "Human_Society.Psychology_Decision.dimension_index"
    },
    "io_contract": {
      "input_schema": {
        "required": ["decision_or_psychological_question", "context"],
        "optional": ["observed_behavior", "relevant_factors", "constraints", "framework_preferences"]
      },
      "output_schema": {
        "required": ["analysis", "relevant_psychological_factors", "assumption_and_limitations", "alternative_interpretations"],
        "optional": ["bias_assessment", "motivation_analysis", "social_context_analysis", "framework_application", "uncertainties_and_gaps"]
      }
    },
    "cluster_index": {
      "decision_making": {
        "rational_choice": "Expected utility, preference consistency, Bayesian updating as normative benchmarks.",
        "bounded_rationality": "Decision-making under cognitive, informational, and time constraints; satisficing vs optimizing.",
        "descriptive_models": "How people actually decide: heuristics, habits, routines, affect, social influence.",
        "dual_process": "Fast automatic vs slow deliberate processing; interaction between intuitive and reflective systems.",
        "choice_architecture": "How options are presented affects choices: framing, defaults, ordering, salience."
      },
      "judgment_and_heuristics": {
        "availability": "Judging frequency/probability by ease of recall; sensitive to vividness, recency, media coverage.",
        "representativeness": "Judging category membership by similarity; ignores base rates and sample size.",
        "anchoring": "Insufficient adjustment from an initial value; sensitive to anchor source and relevance.",
        "affect_and_confidence": "Emotional state and overconfidence influence judgments; calibration varies."
      },
      "cognitive_biases": {
        "confirmation_bias": "Tendency to favor information confirming existing beliefs.",
        "sunk_cost": "Continuing because of past investment rather than future prospects.",
        "framing_effects": "Different choices from equivalent descriptions framed differently.",
        "overconfidence": "Excess confidence in judgments relative to accuracy; calibration gaps.",
        "hindsight_bias": "Seeing outcomes as more predictable after they occur."
      },
      "motivation_and_emotion": {
        "goal_driven_behavior": "Goals, plans, and intentions shape decisions and actions.",
        "intrinsic_vs_extrinsic": "Internal satisfaction vs external rewards; different motivational drivers.",
        "emotional_influence": "Emotions affect risk perception, attention, and choice; not always irrational.",
        "reward_and_feedback": "Reinforcement, habits, and feedback loops shape repeated decisions."
      },
      "social_context": {
        "social_influence": "Conformity, normative pressure, social proof, authority influence.",
        "groupdynamics": "Groupthink, polarization, diffusion of responsibility, social loafing.",
        "cultural_variation": "Cultural context shapes values, norms, and decision heuristics.",
        "identity_and_belonging": "Identity concerns and belonging needs affect choices and information processing."
      }
    },
    "dimension_index": {
      "normative_vs_descriptive": "How people should decide vs how they actually decide; affects framing and conclusions.",
      "individual_vs_social": "Individual cognitive processes vs social and cultural influences; both matter.",
      "conscious_vs_automatic": "Deliberate reasoning vs automatic intuitive processes; both influence decisions.",
      "stable_vs_situational": "Enduring traits vs situational factors; both shape behavior; avoid trait-only explanations."
    },
    "capability_matrix": {
      "decision_analysis": "Analyze a decision context: options, goals, constraints, information, and likely processes.",
      "bias_assessment": "Identify possible cognitive biases and heuristics relevant to the decision.",
      "motivation_analysis": "Analyze motivational drivers: goals, rewards, intrinsic/extrinsic factors.",
      "social_context_analysis": "Analyze social and cultural influences: norms, group dynamics, identity, culture.",
      "framework_application": "Apply relevant psychological frameworks with appropriate scope and caveats.",
      "alternative_interpretations": "Generate multiple plausible interpretations of behavior or decisions.",
      "uncertainty_flagging": "Flag gaps in information, individual variation, and limits of psychological generalization."
    },
    "safety_constraints": {
      "no_diagnostic_claims": "Psychological analysis is descriptive and educational; it does not diagnose mental health conditions.",
      "no_personalized_psychological_profiles": "Do not infer or assert detailed psychological profiles about specific individuals without basis.",
      "no_overgeneralization": "Psychological findings are probabilistic and context-dependent; avoid universal claims.",
      "respect_dignity": "Describe behavior and cognition without demeaning or pathologizing language.",
      "assumption_transparency": "State all assumptions about context, motives, and processes explicitly."
    },
    "evaluation": {
      "success_criteria": ["decision_context_is_clear", "psychological_factors_are_relevant_and_reasonable", "biases_are_considered_not_assumed", "alternative_interpretations_are_included", "limitations_and_individual_variation_are_flagged", "conclusions_are_not_overclaimed"],
      "internal_consistency": "Verify that analysis, frameworks, and conclusions are mutually consistent.",
      "assumption_audit": "Confirm that context, motives, and process assumptions are stated.",
      "coverage": "Check that relevant factors (cognitive, motivational, social, developmental) are considered."
    }
  }
]

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]
```

---
**MOC:** [[KERNEL_MOC]]
