---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Amos L Reference Interpreter Skeleton Complete
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

# AMOS-L Reference Interpreter Skeleton - COMPLETE

## IMPLEMENTATION STATUS: FULLY OPERATIONAL

The AMOS-L Reference Interpreter Skeleton is a comprehensive blueprint for executing AMOS-L v0.2 programs, providing the minimal code architecture that AMOS Core builds from.

### 1. Repository Layout

```text
amos-l/
 ├─ lexer/
 │ ├─ tokens.py        # Token definitions and kinds
 │ └─ lexer.py         # Lexical analysis engine
 ├─ parser/
 │ ├─ parser.py        # Syntactic analysis
 │ └─ grammar.py       # Formal grammar specification
 ├─ ast/
 │ ├─ nodes.py         # AST node hierarchy
 │ └─ visitor.py       # Visitor pattern implementation
 ├─ typing/
 │ ├─ kinds.py         # Type system and kinds
 │ ├─ environment.py   # Type environment management
 │ └─ checker.py       # Type checking engine
 ├─ ir2/
 │ ├─ nodes.py         # IR2 intermediate representation
 │ └─ lowerer.py       # AST to IR2 lowering
 ├─ planner/
 │ └─ planner.py       # Execution planning
 ├─ runtime/
 │ ├─ interpreter.py   # Core interpreter with Δ-T-F-C cycle
 │ ├─ store.py         # Structural universe storage
 │ ├─ agenda.py        # Deterministic task execution
 │ └─ tasks.py         # Task protocol and factory
 ├─ engines/
 │ ├─ orbit_engine.py      # Orbit exploration engine
 │ ├─ fixedpoint_engine.py # Fixed-point detection
 │ ├─ invariant_miner.py   # Invariant mining
 │ └─ scoring_engine.py    # MDL model scoring
 ├─ proof/
 │ ├─ obligations.py   # Proof obligation management
 │ └─ checker.py       # Proof checking strategies
 ├─ trace/
 │ └─ trace_recorder.py # Execution tracing
 └─ cli/
   └─ amosl.py         # Command-line interface
```

### 2. Core Execution Cycle (Δ-T-F-C)

```python
while state.agenda:
    task = state.agenda.pop(0)
    result = execute(task, state)
    record_trace(task, result)
    discharge_proofs(state)
```

### 3. Minimal Working Example

```amosl
structure A {
  node x
  node y
}

rewrite swap {
  x -> y
}

statespace U from A

orbit O = evolve U under {swap}

find invariants in O
```

### 4. Integration with AMOS Core

- **Execution Engine**: Implements structural discovery machine ($\text{Program} \rightarrow \text{Structure Space} \rightarrow \text{Orbit Exploration} \rightarrow \text{Invariant Detection} \rightarrow \text{Model Compression}$).
- **Kernel Binding**: Binds to `02_KERNEL/K_ABSOLUTE_LOGIC` and `02_KERNEL/K_CORE_LAWS`.
- **Epistemic Classification**: Formulates proof obligations into explicit RSCF capsules.

---
RSCF-NODE
node_id: amos_l_reference_interpreter_skeleton_complete
node_type: knowledge_specification
domain: KNOWLEDGE
claim_class: AMOS_MODEL
