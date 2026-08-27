---
title: AI ARCHITECTURE FACTORY V2 ONTOLOGY
tags: [architecture, design, structure]
type: data
source: 11_KNOWLEDGE/architecture
---





```json
{
  "metadata": {
    "title": "AI Architecture Factory v2",
    "version": "2.0",
    "purpose": "Modular generator that knows what to generate using domain, primitive, equation, control, validation, and artifact libraries.",
    "core_equation": "S_next = Gate(Validate(Generate(Plan(Retrieve(Parse(Goal))), Memory, Tools)), Constraints)"
  },
  "compiler_pipeline": [
    "parse_goal",
    "select_domain",
    "select_primitives",
    "compose_architecture",
    "derive_equations",
    "generate_artifact_spec",
    "validate_architecture",
    "compile_outputs"
  ],
  "domain_libraries": {
    "ai_agent": {
      "entities": [
        "user",
        "agent",
        "memory",
        "tool",
        "policy",
        "state",
        "output",
        "environment",
        "evaluator"
      ],
      "laws": [
        "constraints_override",
        "tools_need_permission",
        "uncertainty_labeled"
      ],
      "architecture_defaults": [
        "planner_executor",
        "memory_retrieval",
        "risk_gate",
        "self_evaluator",
        "tool_router"
      ]
    },
    "dataset_generator": {
      "entities": [
        "schema",
        "record",
        "field",
        "generator_rule",
        "signature",
        "validation",
        "export"
      ],
      "laws": [
        "schema_must_parse",
        "ids_unique",
        "non_overlap_requires_signature"
      ],
      "architecture_defaults": [
        "schema_builder",
        "rule_generator",
        "dedupe_engine",
        "record_validator",
        "exporter"
      ]
    },
    "research_engine": {
      "entities": [
        "query",
        "claim",
        "source",
        "evidence",
        "citation",
        "freshness",
        "conflict"
      ],
      "laws": [
        "claims_need_sources",
        "freshness_matters",
        "conflicts_labeled"
      ],
      "architecture_defaults": [
        "query_decomposer",
        "retriever",
        "source_ranker",
        "claim_matrix",
        "citation_writer"
      ]
    },
    "code_system": {
      "entities": [
        "module",
        "function",
        "class",
        "test",
        "dependency",
        "runtime",
        "error"
      ],
      "laws": [
        "code_should_run",
        "inputs_validated",
        "errors_handled"
      ],
      "architecture_defaults": [
        "module_planner",
        "code_generator",
        "test_generator",
        "runtime_validator",
        "debug_loop"
      ]
    },
    "safety_governance": {
      "entities": [
        "risk",
        "policy",
        "permission",
        "harm",
        "privacy",
        "audit",
        "fallback"
      ],
      "laws": [
        "do_not_enable_harm",
        "privacy_protected",
        "unsafe_actions_redirected"
      ],
      "architecture_defaults": [
        "risk_classifier",
        "policy_gate",
        "privacy_filter",
        "safe_fallback",
        "audit_logger"
      ]
    },
    "biology_fractal": {
      "entities": [
        "molecule",
        "cell",
        "tissue",
        "organ",
        "system",
        "microbiome",
        "environment",
        "scale"
      ],
      "laws": [
        "not_everything_fractal",
        "measurement_before_claim",
        "no_diagnosis"
      ],
      "architecture_defaults": [
        "scale_mapper",
        "branching_model",
        "network_model",
        "control_model",
        "anti_overclaim_guard"
      ]
    },
    "multi_agent_org": {
      "entities": [
        "agent",
        "role",
        "task",
        "message",
        "consensus",
        "minority_report",
        "coordinator"
      ],
      "laws": [
        "roles_clear",
        "coordination_cost_controlled",
        "dissent_preserved"
      ],
      "architecture_defaults": [
        "role_router",
        "debate_engine",
        "consensus_engine",
        "minority_report",
        "coordinator"
      ]
    },
    "human_interaction": {
      "entities": [
        "user_state",
        "emotion_signal",
        "cognitive_load",
        "tone",
        "boundary",
        "response"
      ],
      "laws": [
        "do_not_destabilize",
        "clarity_over_performance",
        "no_manipulation"
      ],
      "architecture_defaults": [
        "state_estimator",
        "tone_controller",
        "load_reducer",
        "clarity_generator",
        "boundary_guard"
      ]
    }
  },
  "primitive_libraries": {
    "state_primitives": [
      "GoalState",
      "InputState",
      "ContextState",
      "MemoryState",
      "BeliefState",
      "RiskState",
      "ToolState",
      "OutputState",
      "ValidationState",
      "UserState",
      "EnvironmentState",
      "ResourceState",
      "TraceState"
    ],
    "operator_primitives": [
      "Parse",
      "Classify",
      "Retrieve",
      "Rank",
      "Compress",
      "Expand",
      "Decompose",
      "Plan",
      "Route",
      "Execute",
      "Simulate",
      "Generate",
      "Critique",
      "Repair",
      "Validate",
      "Gate",
      "Fallback",
      "Audit",
      "Dedupe",
      "Sign",
      "Export"
    ],
    "equation_primitives": {
      "state_update": "S_next=C(F(S,U,M,T,Ctx),K)",
      "belief_update": "P(H|D)=P(D|H)P(H)/P(D)",
      "retrieval_score": "score=αsim(q,d)+βfreshness+γauthority-δrisk",
      "risk_score": "R=Σ_i w_i r_i",
      "tool_utility": "tool*=argmax_i quality_i-risk_i-cost_i",
      "memory_update": "M_next=ρM+Encode(event)-Forget(M,K)",
      "recursive_refine": "X_next=Repair(X,Critique(X),K)",
      "loop_interrupt": "stop=true iff ΔInfo<ε and depth>N",
      "non_overlap": "unique=true iff signature(structure)∉Seen",
      "schema_validity": "valid=parse(output,schema)",
      "evidence_matrix": "M_ij=support(source_i,claim_j)",
      "consensus": "y*=aggregate(y_i,w_i)",
      "minority_value": "MRV=novelty*plausibility*risk_reduction",
      "fractal_scale": "P_next=Scale(P,r)+Variation",
      "scale_similarity": "MSR=Σ sim(P_k,P_{k+1})/K",
      "resource_budget": "Σ cost_i ≤ Budget",
      "latency_quality": "J=quality-λ_latency*latency-λ_cost*cost",
      "privacy_leakage": "L=P(secret∈output|context)",
      "audit_trace": "Trace_next=append(Trace,event)"
    },
    "control_primitives": [
      "truthfulness_gate",
      "privacy_gate",
      "safety_gate",
      "policy_gate",
      "permission_gate",
      "tool_sandbox",
      "risk_threshold",
      "human_override",
      "loop_interrupt",
      "source_requirement",
      "schema_gate",
      "non_overlap_gate",
      "anti_overclaim_guard",
      "resource_budget_gate"
    ],
    "validation_primitives": [
      "schema_parse_test",
      "required_blocks_test",
      "contradiction_test",
      "source_support_test",
      "risk_threshold_test",
      "privacy_leakage_test",
      "tool_output_test",
      "unit_test",
      "red_team_test",
      "non_overlap_signature_test",
      "fractal_measurement_test",
      "freshness_test",
      "format_test"
    ],
    "artifact_templates": [
      "json_architecture_spec",
      "python_class_skeleton",
      "prompt_pack",
      "unit_test_file",
      "dataset_schema",
      "generator_script",
      "audit_report",
      "validation_report",
      "agent_config",
      "workflow_spec"
    ]
  }
}

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]
```

---
**MOC:** [[ARCHITECTURE_MOC]]
