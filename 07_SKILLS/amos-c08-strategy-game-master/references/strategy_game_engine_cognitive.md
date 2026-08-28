---
title: strategy game engine cognitive
type: reference
source: 07_SKILLS/amos-c08-strategy-game-master/references
tags: [reference, amos-c08-strategy-game-master, canon/skill]
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# AMOS Strategy Game Engine Cognitive

> Source: `_00_Cosmo brain/cognitive/AMOS_Strategy_Game_Engine_v0_Cognitive4.md`
> Epistemic class: SOURCE_DERIVED

---
canon-group: meta
canon-type: framework
rscf-state: source-claim
topic: amos-strategy-game-engine-v0
tags: [canon-group/biology, canon/framework, rscf/claim, rscf/provenance, rscf/state/source-claim, topic/amos-strategy-game-engine-v0, cognitive]
created: 2026-08-22
---

[
  {
    "meta": {
      "name": "AMOS_C08_Strategy_Game_MAX",
      "version": "vInfinity.1.0.0",
      "domain": "Strategy_and_GameTheory",
      "description": "Game-theoretic and strategic planning kernel+engine for firms, states, and coalitions.",
      "routing_tags": [
        "strategy",
        "game_theory",
        "negotiation",
        "war",
        "competition"
      ],
      "roles": [
        "CEO",
        "CSO",
        "Negotiator",
        "Policy Maker"
      ],
      "safety": [
        "Do not design strategies for physical harm.",
        "Do not support illegal market collusion."
      ]
    },
    "kernel_layer": {
      "description": "Foundational, domain-irreducible logic blocks for this canonical AMOS domain.",
      "kernels": [
        {
          "id": "GAME_NORMAL_FORM_KERNEL",
          "scope": [
            "finite_games",
            "payoffs",
            "dominance",
            "equilibrium"
          ],
          "primitives": [
            "player",
            "strategy",
            "payoff",
            "information_set"
          ],
          "benchmarks": [
            "game_theory_texts"
          ]
        },
        {
          "id": "GAME_DYNAMICAL_KERNEL",
          "scope": [
            "repeated_games",
            "evolutionary_dynamics",
            "learning"
          ],
          "primitives": [
            "state",
            "update_rule",
            "trajectory"
          ],
          "benchmarks": [
            "repeated_games",
            "evolutionary_game_theory"
          ]
        },
        {
          "id": "NEGOTIATION_KERNEL",
          "scope": [
            "bargaining",
            "coalitions",
            "signals"
          ],
          "primitives": [
            "reservation_value",
            "offer",
            "threat_point"
          ],
          "benchmarks": [
            "bargaining_theory",
            "diplomacy_cases"
          ]
        }
      ]
    },
    "engine_layer": {
      "description": "Composable execution engines that apply kernels to real systems, institutions, and scenarios.",
      "engines": [
        {
          "id": "STRATEGIC_LANDSCAPE_ENGINE",
          "inputs": [
            "actors",
            "resources",
            "constraints"
          ],
          "outputs": [
            "game_model",
            "dominant_patterns",
            "potential_coalitions"
          ],
          "capabilities": [
            "formalise_informal_struggles_as_games",
            "identify_leverage_points"
          ]
        },
        {
          "id": "SCENARIO_GAMEPLAY_ENGINE",
          "inputs": [
            "baseline_game",
            "shocks",
            "time_horizon"
          ],
          "outputs": [
            "scenario_tree",
            "robust_strategy_set"
          ],
          "capabilities": [
            "generate_multiple_paths",
            "test_strategy_robustness"
          ]
        },
        {
          "id": "NEGOTIATION_PLAYBOOK_ENGINE",
          "inputs": [
            "stakeholder_profiles",
            "target_outcomes"
          ],
          "outputs": [
            "concession_path",
            "message_frames",
            "fallback_positions"
          ],
          "capabilities": [
            "align_tactics_with_long_term_positioning",
            "separate_principled_negotiation_from_coercive_moves"
          ]
        }
      ]
    },
    "interfaces": {
      "agent_routing_tags": [
        "strategy",
        "game_theory",
        "negotiation",
        "war",
        "competition"
      ],
      "compatible_roles": [
        "CEO",
        "CSO",
        "Negotiator",
        "Policy Maker"

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
node_id: amos-c08-strategy-game-master-strategy-game-engine-cognitive
node_type: reference
path: 07_SKILLS/amos-c08-strategy-game-master/references/strategy_game_engine_cognitive.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[references_MOC]]
