---
title: AMOS SYSTEMS CORE ENGINE V0 SYSTEMS4 2
tags:
- canon-group/biology
- canon/framework
- rscf/claim
- rscf/provenance
- rscf/state/source-claim
- topic/amos-systems-core-engine-v0
- engine
- engine-moc
- trang-framework-recursive-ontology-dynamics
type: data
source: 11_KNOWLEDGE/engine
rscf:
  state: AMOS_MODEL
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: engine_specification
---

# AMOS SYSTEMS CORE ENGINE V0 SYSTEMS4 2

```json
{
  "meta": {
    "name": "Systems_Core_Engine",
    "version": "1.0.0",
    "description": "Core engine for systems thinking: understanding, modeling, and reasoning about complex systems."
  },
  "engine": {
    "description": "A core engine for systems thinking that provides the foundational concepts, modeling approaches, and reasoning patterns for understanding complex systems across domains.",
    "core_concepts": {
      "system_definition": "A set of interconnected elements that function as a whole; the behaviour of the system emerges from the interactions of its parts.",
      "emergence": "System-level properties that are not present in individual parts and cannot be predicted by analyzing parts in isolation.",
      "feedback_loops": "Circular causal relationships where output feeds back as input: reinforcing (amplifying) and balancing (stabilizing).",
      "system_boundaries": "The line between what is inside and outside the system; boundary choice determines what is relevant.",
      "stock_and_flow": "Accumulations (stocks) and the rates of change (flows) that change them; fundamental to dynamic modeling.",
      "delays": "Time lags between cause and effect that can cause oscillations and destabilize systems.",
      "leverage_points": "Places in a system where a small shift can produce large changes; identified through systems analysis."
    },
    "modeling_approaches": {
      "causal_loop_diagrams": {
        "description": "Map feedback loops and causal relationships visually.",
        "when_to_use": "Exploring system structure, identifying feedback, communicating system dynamics.",
        "outputs": ["loop_diagram", "loop_type_identification", "system_archetypes_recognized"]
      },
      "stock_flow_diagrams": {
        "description": "Model system dynamics with stocks, flows, and feedbacks.",
        "when_to_use": "Quantitative dynamic modeling, simulating system behavior over time.",
        "outputs": ["stock_flow_model", "simulation_results", "behavior_modes_identified", "sensitivity_analysis"]
      },
      "systems_archetypes": {
        "description": "Recognize common patterns of system behavior.",
        "archetypes": [
          "Tragedy of the Commons",
          "Fixes That Fail",
          "Growth and Underinvestment",
          "Shifting the Burden",
          "Escalation",
          "Success to the Successful",
          "Accidental Adversaries",
          "Drifting Goals",
          "Rich Get Richer"
        ],
        "when_to_use": "Diagnosing persistent system problems, identifying root causes, designing effective interventions."
      },
      "boundary_analysis": {
        "description": "Systematically examine what is inside and outside the system boundary.",
        "steps": ["identify_system_purpose", "map_system_elements", "identify_boundaries", "test_boundary_completeness", "consider_wider_system"],
        "when_to_use": "Ensuring problems are framed correctly, avoiding sub-optimization, identifying missing elements."
      }
    },
    "reasoning_patterns": {
      "holistic_vs_reductionist": "Balance between analyzing parts and understanding the whole; use reductionist methods for detail, holistic for structure and behavior.",
      "static_vs_dynamic": "Static analysis for structure at a point in time; dynamic analysis for behavior over time.",
      "analytic_vs_simulative": "Analytic methods for understanding relationships; simulative methods for exploring behavior under different conditions.",
      "qualitative_vs_quantitative": "Qualitative for understanding structure and generating hypotheses; quantitative for testing and prediction.",
      "linear_vs_nonlinear": "Linear relationships for simple cases; nonlinear for thresholds, tipping points, and complex behavior."
    },
    "applications": {
      "organisation_design": "Apply systems thinking to organisational structure, process, and culture.",
      "policy_analysis": "Use systems approaches to understand policy impacts, unintended consequences, and leverage points.",
      "engineering_systems": "Apply systems engineering principles to technical system design and integration.",
      "ecological_systems": "Use systems thinking for ecosystem understanding, management, and restoration.",
      "social_systems": "Apply to social, economic, and cultural systems for deeper understanding."
    }
  }
}

---
**Related:**  ·  ·  ·  · 
```

---
**MOC:** [[ENGINE_MOC]]

---
**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
