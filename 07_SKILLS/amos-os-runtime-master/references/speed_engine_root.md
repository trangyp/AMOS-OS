---
title: speed engine root
type: reference
source: 07_SKILLS/amos-os-runtime-master/references
tags:
- reference
- amos-os-runtime-master
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

# AMOS Speed Engine v0 Root

> Source: `_00_Cosmo brain/engine/A/AMOS_Speed_Engine_v0_root.md`
> Epistemic class: SOURCE_DERIVED

---
tags: [canon-group/tech-ai, canon/framework, rscf/claim, rscf/state/observation, topic/amos-speed-engine-v0, engine]
---

{
  "AMOS_SPEED_OPTIMIZATION_KERNEL": {
    "meta": {
      "name": "AMOS_SPEED_OPTIMIZATION_KERNEL",
      "version": "v1.0.0",
      "description": "Cross-cutting optimisation kernel for all AMOS engines. Minimises latency, prunes unnecessary reasoning, compresses decision paths, enforces deterministic routing, and optimises generation length while preserving correctness.",
      "type": "optimization_kernel",
      "author": "Trang Phan",
      "notes": [
        "This kernel does not change domain logic or values.",
        "It only controls how fast and compact the reasoning+generation pipeline runs."
      ]
    },

    "activation": {
      "enabled": true,
      "default_mode": "balanced_fast",
      "available_modes": [
        "max_safe_speed",
        "balanced_fast",
        "precision_priority"
      ],
      "mode_rules": {
        "max_safe_speed": {
          "description": "Aggressively optimise for latency and throughput while keeping minimum validation checks.",
          "max_reasoning_depth": 3,
          "self_reflection_passes": 0,
          "enable_result_summarisation": true
        },
        "balanced_fast": {
          "description": "Default. Strong speed optimisation with one light validation pass for important answers.",
          "max_reasoning_depth": 5,
          "self_reflection_passes": 1,
          "enable_result_summarisation": true
        },
        "precision_priority": {
          "description": "Allow deeper reasoning when user explicitly demands maximum accuracy. Still prunes obvious redundancy.",
          "max_reasoning_depth": 8,
          "self_reflection_passes": 2,
          "enable_result_summarisation": true
        }
      }
    },

    "optimization_objectives": {
      "primary": [
        "minimise_end_to_end_latency",
        "minimise_token_compute_cost",
        "maximise_response_signal_density"
      ],
      "secondary": [
        "preserve_factual_correctness",
        "preserve_structural_clarity",
        "preserve_user_alignment"
      ],
      "priority_weights": {
        "latency": 0.40,
        "compute_cost": 0.25,
        "signal_density": 0.20,
        "correctness": 0.15
      }
    },

    "routing_policies": {
      "deterministic_routing": true,
      "rules": [
        "always_select_single_best_specialist_engine_based_on_query_type",
        "avoid_parallel_engine_invocation_unless_query_requires_cross_domain_fusion",
        "reuse_recent_context_and_intermediate_results_when_safe",
        "short_circuit_pipeline_if_high_confidence_answer_is_available"
      ],
      "engine_selection_criteria": {
        "match_domain_tags": true,
        "prefer_high_confidence_historic_performance": true,
        "avoid_overlapping_engines_when_not_needed": true
      }
    },

    "reasoning_pruning": {
      "enable_pruning": true,
      "heuristics": [
        "skip_excessive_enumeration_of_obvious_options",
        "collapse_redundant_explanation_segments",
        "avoid_re-deriving_facts_available_in_high_confidence_memory",
        "stop_chain_of_thought_when_marginal_gain_is_low"
      ],
      "max_branches_per_decision_point": 3,
      "max_scenarios_in_planning_outputs": 3,
      "skip_layers_for_simple_queries": [
        "deep_meta_analysis_layer",
        "long_horizon_forecast_layer"
      ]
    },

    "decision_tree_compression": {
      "enabled": true,
      "methods": [
        "merge_equivalent_paths",
        "factor_common_premises",
        "represent_repeated_patterns_as_rules_not_full_trees"
      ],
      "output_style": {
        "prefer_compact_frameworks_over_freeform_text": true,
        "use_numbered_steps_for_plans": true,
        "avoid_nested_bullets_deeper_than_level_3": true
      }
    },

    "length_control": {
      "enable_length_optimization": true,
      "targets": {
        "default_max_tokens

---
**MOC:** references_MOC

## Related

- [[07_SKILLS_MOC]]
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · references_MOC · [[07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-os-runtime-master-speed-engine-root
node_type: reference
path: 07_SKILLS/amos-os-runtime-master/references/speed_engine_root.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
