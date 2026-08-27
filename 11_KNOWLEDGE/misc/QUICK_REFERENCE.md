---
title: QUICK REFERENCE
tags: [misc, reference, general, canon/knowledge]
type: document
source: 11_KNOWLEDGE/misc
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general

---


# Quick Reference - Hierarchical AI Architecture Generator

## Instant Start

```python
from hierarchical_ai_architecture_generator import HierarchicalGenerator, GoalDrivenGenerator

# Hierarchical (rule-based)
h = HierarchicalGenerator()
entries = h.generate(limit=100)
safety = h.query(ai_layer="safety_controller")

# Goal-driven (ontology-based)
g = GoalDrivenGenerator()
archs = g.generate("Build safe multi-agent system", count=50)
```

## Core Components

| Component | Import Path | Purpose |
|-----------|-------------|---------|
| `HierarchicalGenerator` | `.core` | Rule-based 7-level hierarchy |
| `GoalDrivenGenerator` | `.goal_core` | Natural language goal parsing |
| `UnifiedGenerator` | `.unified_generator` | Combines both approaches |
| `PatternLibrary` | `.patterns` | Code templates for 5 pattern types |
| `AMOSArchitectureBridge` | `.integration` | AMOS ecosystem integration |

## CLI Commands

```bash
# Main CLI
python -m hierarchical_ai_architecture_generator generate --limit 1000
python -m hierarchical_ai_architecture_generator query --layer safety_controller
python -m hierarchical_ai_architecture_generator demo

# Goal-driven CLI
python goal_driven_ai_architecture_generator_v2.py generate \
    --goal "Create retrieval system" --count 50
python goal_driven_ai_architecture_generator_v2.py explain --goal "Build safe code"

# Master demo
python master_demo.py
```

## Key Enums

**MetaEquationType (8)**: CONTROLLED_STATE_TRANSFORM, RECURSIVE_REFINEMENT, GRAPH_PROPAGATION, RISK_GATED_ACTION, COMPRESSION_EXPANSION, FRACTAL_SCALE_RECURRENCE, EVIDENCE_SUPPORT_MATRIX, RESOURCE_CONSTRAINED_OPT

**AILayer (20)**: input_perception → signal_noise_filter → intent_understanding → short_term_memory → long_term_memory → retrieval_engine → recursive_reasoning → planning_engine → tool_executor → code_executor → multi_agent_layer → causal_reasoner → uncertainty_estimator → safety_controller → privacy_controller → governance_auditor → language_generator → self_evaluator → user_state_model → ecosystem_monitor

**GoalType (8)**: REASONING, GENERATION, RETRIEVAL, AGENTIC_EXECUTION, SAFETY_GOVERNANCE, MEMORY_PERSONALIZATION, MULTI_AGENT, FRACTAL_SCALING

## Patterns with Code Templates

| Pattern | Class | Use Case |
|---------|-------|----------|
| State Machine | `StateMachinePattern` | Controlled transitions |
| Recursive Refinement | `RecursiveRefinementPattern` | Iterative improvement |
| Graph Propagation | `GraphPropagationPattern` | Networked info flow |
| Risk Gated | `RiskGatedPattern` | Safety-critical ops |
| Compression-Expansion | `CompressionExpansionPattern` | Efficient representation |

## File Map

```
hierarchical_ai_architecture_generator/
├── core.py                    # HierarchicalGenerator, ArchitectureEntry, enums
├── patterns.py                # 5 pattern classes with code templates
├── integration.py             # AMOSArchitectureBridge
├── demo.py                    # Feature demos
├── cli.py                     # Main CLI
├── goal_core.py               # GoalDrivenGenerator, GoalOntology
├── goal_driven_ai_architecture_generator_v2.py  # Goal CLI
├── unified_generator.py       # UnifiedGenerator (3 modes)
├── master_demo.py             # Comprehensive demo
├── test_implementation.py     # Test suite
└── README.md                  # Full documentation
```

## Core Equation

```
S_next = C(F(S, U))
```

Where: **S**=state, **U**=input/universe, **F**=transform, **C**=control gate

## Quick Queries

```python
# By layer
h.query(ai_layer=AILayer.SAFETY_CONTROLLER)

# By constraint
h.query(constraint=Constraint.PRIVACY)

# Complex
h.query(ai_layer=AILayer.PLANNING_ENGINE, 
        constraint=Constraint.SAFETY,
        validation=Validation.RISK_SCORE)

# By goal type
g.query(goal_type=GoalType.SAFETY_GOVERNANCE)
```

## Export/Import

```python
# Export
h.export_to_json(entries, "architectures.json")

# Import
new_entries = h.import_from_json("architectures.json")
```

## Validation

```python
# Built-in validators
- Signature uniqueness
- Formula syntax
- Architecture completeness

# Custom validator
def my_validator(entry):
    return entry.constraint != Constraint.SAFETY or \
           entry.validation == Validation.RISK_SCORE

h.add_validator(my_validator)
```

## Unified Generator Modes

```python
from unified_generator import UnifiedGenerator, GenerationMode

# Mode 1: Hierarchical only
gen = UnifiedGenerator(mode=GenerationMode.HIERARCHICAL)
entries = gen.generate(limit=100)

# Mode 2: Goal-driven only  
gen = UnifiedGenerator(mode=GenerationMode.GOAL)
entries = gen.generate(goal="Build safe system", limit=50)

# Mode 3: Hybrid (combines both)
gen = UnifiedGenerator(mode=GenerationMode.HYBRID)
entries = gen.generate(goal="Create retrieval system", limit=100)
```

## Version

**v2.0.0** - Complete implementation with hierarchical + goal-driven + unified generators, pattern library, AMOS bridge, and full CLI.

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
