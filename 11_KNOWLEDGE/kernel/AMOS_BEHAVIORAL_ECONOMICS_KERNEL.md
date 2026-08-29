---
title: AMOS BEHAVIORAL ECONOMICS KERNEL V0 HUMAN SOCIETY4 2
tags:
- canon-group/human-system
- canon/framework
- rscf/claim
- rscf/provenance
- rscf/state/source-claim
- topic/amos-behavioral-economics-kernel-v0
- kernel
type: data
source: 11_KNOWLEDGE/kernel
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: AMOS_knowledge
---

# AMOS BEHAVIORAL ECONOMICS KERNEL V0 HUMAN SOCIETY4 2

```json
[
  {
    "meta": {
      "kernel_name": "Behavioral_Economics_Kernel",
      "version": "1.0.0",
      "created_at_utc": "2026-08-22",
      "source_engines": ["Human_Society.Behavioral_Economics"],
      "description": "Kernel for behavioral economics: how psychological factors shape economic decisions, market behavior, and policy design."
    },
    "identity": {
      "primary_role": "Analyze economic decisions through the lens of psychology and bounded rationality",
      "scope": ["heuristics_and_biases_in_economics", "prospect_theory", "time_preference_and_habits", "social_and_economic_behavior", "choice_architecture_and_nudges", "market_anomalies", "behavioral_policy"],
      "governance_principles": ["state_assumptions", "distinguish_description_from_prescription", "avoid_overclaiming_market_predictions", "respect_context_and_individual_variation"]
    },
    "state_model": {
      "core_state_axes": ["economic_decision_context", "psychological_factors", "time_horizon", "social_and_institutional_context", "policy_or_market_context"]
    },
    "reference_maps": {
      "cluster_index_reference": "Human_Society.Behavioral_Economics.cluster_index",
      "dimension_index_reference": "Human_Society.Behavioral_Economics.dimension_index"
    },
    "io_contract": {
      "input_schema": {
        "required": ["economic_question_or_scenario", "context"],
        "optional": ["observed_behavior", "market_or_institutional_details", "policy_options", "framework_preferences"]
      },
      "output_schema": {
        "required": ["behavioral_analysis", "relevant_psychological_and_economic_factors", "assumption_and_limitations", "alternative_interpretations"],
        "optional": ["prospect_theory_application", "time_preference_analysis", "choice_architecture_analysis", "policy_or_market_implications", "uncertainties_and_gaps"]
      }
    },
    "cluster_index": {
      "prospect_theory_and_related": {
        "reference_point_dependence": "Value is judged relative to a reference point; gains and losses are not symmetric.",
        "loss_aversion": "Losses loom larger than equivalent gains; affects risk attitudes and choices.",
        "diminishing_sensitivity": "Marginal sensitivity decreases with magnitude; affects weighting of changes.",
        "probability_weighting": "People overweight small probabilities and underweight moderate/large ones; affects insurance and gambling.",
        "mental_accounting": "People treat money differently depending on source, label, or intended use."
      },
      "time_preference_and_habits": {
        "discounting": "How future costs and benefits are discounted; may be hyperbolic or inconsistent over time.",
        "present_bias": "Overweighting immediate costs/benefits relative to later ones; affects savings, health, consumption.",
        "habits_and_automaticity": "Much behavior is habitual and automatic; hard to change through information alone.",
        "commitment_devices": "People use self-imposed constraints to overcome self-control problems."
      },
      "social_and_economic_behavior": {
        "social_preferences": "Fairness, reciprocity, altruism, spite, inequality aversion affect economic choices.",
        "trust_and_cooperation": "Trust, reputation, and repeated interaction shape economic behavior beyond pure self-interest.",
        "social_norms": "Perceived norms and expectations shape behavior; violations carry social costs.",
        "identity_and_consumption": "Consumption and economic choices signal identity and group membership."
      },
      "choice_architecture_and_nudges": {
        "defaults": "Default options strongly affect outcomes; people often stick with defaults.",
        "framing_and_salience": "How options are framed and what is salient affects choices.",
        "simplification": "Reducing complexity and cognitive load improves decisions.",
        "feedback_and_reminder": "Timely feedback and reminders improve decision quality.",
        "ethics_of_nudges": "Nudges raise questions of autonomy, manipulation, transparency, and who decides."
      },
      "market_and_institutional_aspects": {
        "anomalies_and_deviations": "Systematic deviations from standard predictions in markets and experiments.",
        "limits_to_arbitrage": "Arbitrage is limited by risk, cost, capital, timing, and behavior of others.",
        "institutional_design": "Institutions, rules, and incentives shape behavior; bad design can amplify biases.",
        "behavioral_policy": "Policy can exploit behavioral insights to improve outcomes; must be ethically and empirically grounded."
      }
    },
    "dimension_index": {
      "normative_economics_vs_behavioral": "Standard rational-agent predictions vs observed behavior; both inform analysis.",
      "individual_vs_market": "Individual decision processes vs aggregate market outcomes; emergence matters.",
      "experimental_vs_field": "Lab findings vs real-world behavior; external validity must be assessed.",
      "developed_vs_developing_context": "Behavioral patterns may vary with context, scarcity, institutions, and culture."
    },
    "capability_matrix": {
      "behavioral_analysis": "Analyze an economic decision through behavioral lenses: heuristics, reference points, time, social factors.",
      "prospect_theory_application": "Apply prospect theory concepts where appropriate: reference dependence, loss aversion, probability weighting.",
      "time_preference_analysis": "Analyze time inconsistency, present bias, discounting, and commitment.",
      "choice_architecture_analysis": "Analyze how choice architecture affects outcomes: defaults, framing, simplification, feedback.",
      "policy_implications": "Derive policy or design implications, with ethical caveats and empirical grounding.",
      "market_interpretation": "Interpret market or institutional behavior with behavioral considerations; avoid overclaiming.",
      "alternative_interpretations": "Generate standard economic and behavioral alternative explanations."
    },
    "safety_constraints": {
      "no_financial_advice": "Behavioral analysis is educational; it does not constitute personalized financial advice or trading recommendations.",
      "no_overclaiming_market_predictions": "Behavioral insights help explain and design; they do not guarantee market outcomes.",
      "no_manipulative_instructions": "Do not provide instructions for manipulative choice architecture or exploitation of biases.",
      "ethics_of_intervention": "Discuss ethical implications of nudges and behavioral interventions: autonomy, transparency, consent.",
      "assumption_transparency": "State all assumptions about context, behavior, and institutional setting explicitly."
    },
    "evaluation": {
      "success_criteria": ["economic_context_is_clear", "behavioral_factors_are_relevant_and_reasonable", "alternative_explanations_are_included", "policy_or_market_implications_are_qualified", "limitations_and_context_dependence_are_flagged", "conclusions_are_not_overclaimed"],
      "internal_consistency": "Verify that behavioral analysis, economic context, and conclusions are mutually consistent.",
      "assumption_audit": "Confirm that behavioral assumptions, context, and limitations are stated.",
      "coverage": "Check that relevant dimensions (prospect theory, time, social, choice architecture, institutions) are considered."
    }
  }
]

---
**Related:** [[AMOS_IP_SHIELD_KERNEL_V0_WEB7]] · [[HEALTH_KERNEL]] · [[AMOS_MULTI_AGENT_COORDINATION_KERNEL]] · [[AMOS_TECH_ARCHITECTURE_KERNEL]]
```

---
**MOC:** [[KERNEL_MOC]]
