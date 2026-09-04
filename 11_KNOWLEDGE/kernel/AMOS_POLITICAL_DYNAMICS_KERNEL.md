---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Amos Political Dynamics Kernel
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# AMOS POLITICAL DYNAMICS KERNEL V0 HUMAN SOCIETY

```json
[
  {
    "meta": {
      "kernel_name": "Political_Dynamics_Kernel",
      "version": "1.0.0",
      "created_at_utc": "2026-08-22",
      "source_engines": ["Human_Society.Political_Dynamics"],
      "description": "Kernel for political dynamics: power, institutions, conflict, strategy, and change in political systems."
    },
    "identity": {
      "primary_role": "Analyze and reason about political dynamics and systems",
      "scope": ["power_and_institutions", "political_conflict_and_cooperation", "political_strategy", "regime_and_system_dynamics", "policy_and_interest_dynamics", "change_and_stability", "international_and_multi_actor_politics"],
      "governance_principles": ["state_assumptions", "avoid_bias_toward_particular_outcomes", "distinguish_description_from_prescription", "respect_multiplicity_of_perspectives"]
    },
    "state_model": {
      "core_state_axes": ["political_system_context", "actors_and_interests", "institutions_and_rules", "power_and_conflict", "change_and_stability"]
    },
    "reference_maps": {
      "cluster_index_reference": "Human_Society.Political_Dynamics.cluster_index",
      "dimension_index_reference": "Human_Society.Political_Dynamics.dimension_index"
    },
    "io_contract": {
      "input_schema": {
        "required": ["political_question_or_scenario", "context"],
        "optional": ["actors_and_positions", "institutional_details", "historical_context", "constraints", "framework_preferences"]
      },
      "output_schema": {
        "required": ["political_analysis", "relevant_factors", "assumption_and_limitations", "alternative_interpretations"],
        "optional": ["power_analysis", "institutional_analysis", "actor_and_interest_analysis", "conflict_and_cooperation_analysis", "change_and_stability_analysis", "strategy_analysis"]
      }
    },
    "cluster_index": {
      "power_and_institutions": {
        "power": "The capacity to influence outcomes, actors, and decisions; forms: coercive, economic, institutional, ideological, network.",
        "institutions": "Formal and informal rules, norms, procedures, and organizations that structure politics and behavior.",
        "legitimacy": "Belief that authority is rightful; affects compliance, stability, and resistance.",
        "state_and_governance": "State structure, capacity, autonomy, and relationship to society and markets.",
        "rule_of_law_and_accountability": "Legal frameworks, checks, oversight, and accountability mechanisms."
      },
      "actors_and_interests": {
        "actors": "Individuals, parties, interest groups, bureaucracies, media, civil society, firms, international actors.",
        "interests": "Material, ideological, identity-based, status, security, and other interests shaping behavior.",
        "preferences_and_positionality": "How preferences are formed, expressed, and changed; role of ideology, identity, and context.",
        "coalitions_and_alliances": "How actors form coalitions, alliances, and blocs; shifts over time.",
        "leadership": "How leaders shape agendas, frames, mobilization, and outcomes; constraints they face."
      },
      "conflict_and_cooperation": {
        "conflict_sources": "Competing interests, values, identities, scarcity, status, security, distribution.",
        "conflict_forms": "Electoral, legislative, social movement, protest, institutional, violent, informational.",
        "cooperation_and_compromise": "How actors cooperate: shared interests, institutions, reciprocity, trust, negotiation.",
        "mobilization": "How interests and conflicts are mobilized: parties, movements, media, networks.",
        "resolution_mechanisms": "Negotiation, voting, courts, bargaining, power, violence, institutional design."
      },
      "political_strategy": {
        "strategic_behavior": "Actors anticipate others' responses and act accordingly; game-like reasoning.",
        "framing_and_narrative": "How issues are framed and narrated shapes perception, coalitions, and outcomes.",
        "agenda_setting": "What gets attention and when; control of agenda is political power.",
        "timing_and_sequence": "When actions occur matters; sequencing, windows of opportunity, crises.",
        "information_and_signaling": "Information, signaling, credible commitments, bluffing, and communication."
      },
      "regime_and_system_dynamics": {
        "regime_types": "Different regime forms: democratic, authoritarian, hybrid, transitional; characteristics and dynamics.",
        "stability_and_change": "Why regimes persist or change; crises, reforms, revolutions, drift.",
        "institutional_change": "How institutions evolve: design, path dependence, reform, layering, conversion.",
        "decay_and_dysfunction": "Corruption, capture, polarization, erosion of norms, institutional failure.",
        "democratic_erosion_or_deepening": "Processes that weaken or strengthen democratic institutions and norms."
      },
      "policy_and_interest_dynamics": {
        "policy_process": "Agenda setting, formulation, adoption, implementation, evaluation; political economy of policy.",
        "interest_mobilization": "How interests organize and influence policy: lobbying, movements, coalitions, expertise.",
        "distributional_conflicts": "Who gains and loses; distributional conflict is central to politics.",
        "path_dependence": "History matters; early choices constrain later options and lock in outcomes.",
        "feedback": "Policies create new interests, actors, and power relations; self-reinforcing or self-undermining."
      },
      "change_and_stability": {
        "drivers_of_change": "Crises, technology, demographics, ideas, external shocks, leadership, mobilization.",
        "drivers_of_stability": "Institutions, legitimacy, power balances, habits, path dependence, suppression.",
        "gradual_vs_sudden": "Incremental change vs ruptures; both occur and interact.",
        "reform_dynamics": "How reforms succeed or fail: design, coalitions, timing, capacity, legitimacy.",
        "resistance_and_backlash": "Why change provokes resistance; distributional losses, identity, status, expectations."
      },
      "international_and_multi_actor_politics": {
        "multi_actor_systems": "Politics across multiple actors: states, international bodies, firms, movements, networks.",
        "sovereignty_and_interdependence": "Tension between autonomy and interdependence; global constraints and opportunities.",
        "conflict_and_cooperation_across_borders": "War, peace, trade, institutions, cooperation, and conflict internationally.",
        "global_governance": "International institutions, regimes, norms, and their limits.",
        "transnational_dynamics": "Cross-border flows, movements, information, capital, and their political effects."
      }
    },
    "dimension_index": {
      "structure_vs_agency": "How much is shaped by structure/institutions vs individual and collective agency; both matter.",
      "structural_vs_situational": "Enduring political structures vs situational factors and events; both matter.",
      "domestic_vs_international": "Domestic politics and international context interact; both matter.",
      "short_term_vs_long_term": "Immediate political dynamics vs long-term structural trends; both matter."
    },
    "capability_matrix": {
      "political_analysis": "Analyze a political scenario: actors, interests, institutions, power, conflict, change.",
      "power_analysis": "Analyze power dynamics: sources, distribution, exercise, and constraints.",
      "institutional_analysis": "Analyze institutions and rules: design, function, change, and effects.",
      "actor_and_interest_analysis": "Analyze actors, interests, coalitions, and preferences.",
      "conflict_and_cooperation_analysis": "Analyze sources and forms of conflict and cooperation.",
      "strategy_analysis": "Analyze political strategy: framing, agenda, timing, signaling, information.",
      "change_and_stability_analysis": "Analyze drivers of change and stability; reform, erosion, transition.",
      "alternative_interpretations": "Generate multiple plausible interpretations of political phenomena.",
      "uncertainty_flagging": "Flag gaps in information, context dependence, and limits of political generalization."
    },
    "safety_constraints": {
      "no_bias_toward_particular_parties_or_figures": "Analysis should be balanced; do not take sides in partisan political disputes.",
      "no_manipulative_political_strategy": "Do not provide instructions for manipulation, disinformation, or undermining democratic processes.",
      "no_overclaiming_predictions": "Political analysis is uncertain; avoid confident predictions about outcomes.",
      "respect_multiplicity_of_perspectives": "Acknowledge multiple valid perspectives; political phenomena are often contested.",
      "assumption_transparency": "State all assumptions about actors, interests, institutions, and context explicitly."
    },
    "evaluation": {
      "success_criteria": ["political_context_is_clear", "actors_and_institutions_are_reasonably_analyzed", "power_and_conflict_are_considered", "multiple_interpretations_are_included", "change_and_stability_are_addressed", "limitations_and_uncertainty_are_flagged", "conclusions_are_not_overclaimed"],
      "internal_consistency": "Verify that analysis, frameworks, and conclusions are mutually consistent.",
      "assumption_audit": "Confirm that actor, interest, institutional, and context assumptions are stated.",
      "coverage": "Check that relevant dimensions (power, institutions, actors, conflict, strategy, change) are considered."
    }
  }
]

---
**Related:** [[11_KNOWLEDGE/kernel/AMOS_MBB_CONSULTING_KERNEL_V0|AMOS_MBB_CONSULTING_KERNEL_V0]] · [[11_KNOWLEDGE/kernel/AMOS_ORGANIZATIONAL_BEHAVIOR_KERNEL|AMOS_ORGANIZATIONAL_BEHAVIOR_KERNEL]] · [[11_KNOWLEDGE/kernel/AMOS_META_KERNEL_SPECIFICATIONS|AMOS_META_KERNEL_SPECIFICATIONS]] · [[11_KNOWLEDGE/kernel/AMOS_TOOLCHAIN_INTEGRATION_KERNEL|AMOS_TOOLCHAIN_INTEGRATION_KERNEL]]
```

______________________________________________________________________

**MOC:** [[11_KNOWLEDGE/kernel/KERNEL_MOC|KERNEL_MOC]]
