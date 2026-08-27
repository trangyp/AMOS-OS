---
title: vault domain knowledge
type: reference
source: 07_SKILLS/amos-repair-substrate-capture-resistance-rscf/references
tags: [reference, amos-repair-substrate-capture-resistance-rscf, canon/skill]
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# Vault-Sourced Domain Knowledge

> Source: AMOS_OS Obsidian vault (`_00_Cosmo brain/`)
> Epistemic class: SOURCE_CLAIM
> Extracted from skill: `amos-repair-substrate-capture-resistance-rscf`

## Vault-Sourced Content

### Source 1: Cognitive Substrate Reasoning Execution Graph

> Path: `dated/2026-08-22/2026-08-22 Cognitive Substrate Reasoning Graph.md` | Size: 4567 chars | Match score: 12

# Cognitive Substrate Reasoning Execution Graph

> Slice 2 of the AMOS Cognitive Substrate Layer. Implements the reasoning side of
> `R_t = (N_t, E_t, O_t, Pi_t, U_t)` with typed inference operators, transition
> legality, earliest-failure attribution, minimal causal cut-set, and counterfactual
> repair replay.
>
> Source: `cosmo-brain/AMOS_COGNITIVE_SUBSTRATE_REASONING_GRAPH.py` (20 self-tests)
> Test: `cosmo-brain/test_cognitive_substrate_reasoning_graph.py` (9 integration, 29 total)
> Skill: amos-cognitive-substrate-reasoning-graph
> See also: [[2026_08_22_COGNITIVE_SUBSTRATE_REALITY_GATE]] · amos-core-reasoning · amos-competing-hypotheses

## 1. The problem this solves

Reasoning is no longer "what the LLM says between goal and answer." It becomes an
and persisted. When the final answer is wrong, the system can trace back to the
looked wrong.

## 2. Core formalization

```
R_t = (N_t, E_t, O_t, Pi_t, U_t)
```

| Component | Meaning | Gaps addressed |
|-----------|---------|----------------|
| N_t | Cognitive objects (nodes) | 701–704 |
| E_t | Bindings / dependencies (edges) | 705–708 |
| O_t | Operations performed (execution history) | 724 |
| Pi_t | Active reasoning policy | 737–740 |
| U_t | Localized uncertainty | 781–784 |

Transition: `R_{t+1} = T_{o_t}(R_t, e_t, c_t)` with typed operator `o_t`.

## 3. Inference operator registry (gaps 719–723)

11 typed reasoning operators (DEDUCE, ABDUCE, GENERALIZE, SPECIALIZE, NEGATE, CONTRAST, AGGREGATE, PROJECT, SIMULATE, RETRIEVE, REVISE) plus 9 memory/structural operators (BIND, UNBIND, MERGE, SPLIT, COMPRESS, DECOMPRESS, RETRACT_CLAIM, SUSPEND_BELIEF, FORGET) = 20 total in the unified substrate.

- Each operator declares which epistemic classes it may produce (postconditions).
- Causal operators (`ABDUCT`, `PROJECT`, `SIMULATE`) require causal evidence.
- Composition validation: composition between incompatible operators is flagged (e.g., status change without evidence); repeated same operator is a no-op.

## 4. State-transition legality (gap 717)

Forbidden transitions:
- `MODEL → VERIFIED` (without evidence)
- `MODEL → DERIVED` (without evidence)
- `UNKNOWN → VERIFIED`
- `UNKNOWN → DERIVED`

## 5. Earliest-failure attribution (gaps 725–730)

When a conclusion fails, the system walks the dependency cone in topological order
and finds the **first** illegal or contradicted operation — the root cause. The final
wrong output is merely the **symptom**.

Additional outputs:
- **Minimal causal cut-set**: smallest set of ops whose correction rescues the outcome.
- **Failure lock-in point**: first op after which recovery became unlikely.
- **Recovery opportunities**: ops that had enough info to correct but didn't.
- **Counterfactual repair replay**: re-run with one suspected failure corrected to
  test causal attribution.

## 6. Uncertainty localization (gaps 781–784)

Uncertainty is attached to specific nodes, not whole-answer vague confidence.
Multiple uncertainty sources compound nonline

---

### Source 2: AMOS Cognitive Substrate v2.0 — Implementation Notes

> Path: `cognitive/AMOS_Cognitive_Substrate_v2_Implementation_Notes.md` | Size: 11609 chars | Match score: 10

# AMOS Cognitive Substrate v2.0 — Implementation Notes

> Consolidated execution substrate for the AMOS Cognitive Substrate Layer (gaps 701–900).
> Unifies all 4 Obsidian brain slices into a single integrity-checked cognitive system.
>
> Source: `cosmo-brain/AMOS_COGNITIVE_SUBSTRATE.py` (4298 lines, 182590 bytes)
> Self-test: `_run_substrate_self_test()` — 146/146 passed, 0 failed
> Skill: amos-cognitive-substrate
> Workflow: amos-cognitive-substrate-implementation

## 1. Module structure (12 sections, 4298 lines) (2)

| # | Section | Gaps | Key classes |
|---|---------|------|-------------|
| 1 | Cognitive object identity & equivalence | 701–714 | `CognitiveObject`, `SemanticSignature`, `OBJECT_TYPE_MAP`, `EPISTEMIC_CLASS_KEYWORDS` |
| 2 | Bindings and context | 705–714 | `CognitiveBinding`, `BindingType`, `ContextRegion`, `ContextLocalityGraph` |
| 3 | Operator registry | 715–723 | `OperatorSpec`, `OperatorRegistry`, 20 typed operators (`DEDUCE`…`FORGET`) — 11 reasoning + 9 memory/structural |
| 4 | Execution graph with attribution | 724–730 | `ReasoningNode`, `ReasoningEdge`, `ReasoningExecutionGraph`, `ReasoningAttribution` |
| 5 | Belief state | 731–740 | `BeliefState`, `ConfirmationBiasMonitor`, `DisconfirmationBudget` |
| 6 | Uncertainty decomposition | 741–773 | `UncertaintyState`, `UncertaintyComponent`, `localize_evidence()` |
| 7 | Search state and mode management | 774–777 | `SearchState`, `ReasoningModeState`, `MetaCognitiveState` |
| 8 | Memory operational substrate | 793–800 | `MemoryObject`, `MemoryOperationType`, `MemoryOperationRecord`, `MemoryTrustState` |
| 9 | Field lineage and epistemic preservation | 796–799 | `FieldLineage`, `FieldPreservationRecord`, `check_epistemic_preservation()` |
| 10 | Memory retrieval governance | 873–880 | `MemoryOperationGraph.retrieve()`, `query()`, `retrieve_by_tag()`, `get_dependents()`, `dependency_safe_forget()` |
| 11 | Meta-cognitive state and persistence | 778–780 | `MetaCognitiveState`, `MetaCognitiveEvent`, `save()`/`load()` |
| 12 | Interface coupling (CognitiveIntegrityGate) | all | `CognitiveIntegrityGate`, `propose_cognitive_object()`, `execute_operator()`, `admit_to_memory()` |

## 2. The 4-slice architecture (consolidated) (2)

### Slice 1: Reality Gate (RC/IR)
- **`Promote(X) => RC(X) >= theta_RC AND IR(X) <= theta_IR`**
- Prevents epistemic autopoisoning: LLM-generated X → stored → retrieved → treated as evidence → strengthened → stored again
- Admission pipeline: Propose → Type → CheckEvidence → CheckScope → CheckProvenance → Admit
- Use pipeline: Retrieve → Validate → Contextualize → Use
- **Implemented**: Wired into `CognitiveIntegrityGate` via `RealityGate` import from `AMOS_COGNITIVE_SUBSTRATE_REALITY_GATE.py`

### Slice 2: Reasoning Execution Graph (`R_t = (N_t, E_t, O_t, Pi_t, U_t)`)
- 11 typed reasoning operators with declared postconditions: DEDUCE, ABDUCE, GENERALIZE, SPECIALIZE, NEGATE, CONTRAST, AGGREGATE, PROJECT, SIMULATE, RETRIEVE, REVISE
- 9 memory/structural operato

---

### Source 3: AMOS Cognitive Substrate v2.0 — Implementation Notes

> Path: `cognitive/AMOS_Cognitive_Substrate_v2_Implementation_Notes_2.md` | Size: 9825 chars | Match score: 10

# AMOS Cognitive Substrate v2.0 — Implementation Notes

> Consolidated execution substrate for the AMOS Cognitive Substrate Layer (gaps 701–900).
> Unifies all 4 Obsidian brain slices into a single integrity-checked cognitive system.
>
> Source: `cosmo-brain/AMOS_COGNITIVE_SUBSTRATE.py` (4298 lines)
> Self-test: `_run_substrate_self_test()` — 146/146 passed, 0 failed
> Skill: amos-cognitive-substrate
> Workflow: amos-cognitive-substrate-implementation

## 1. Module structure (12 sections, 4298 lines)

| # | Section | Gaps | Key classes |
|---|---------|------|-------------|
| 1 | Cognitive object identity & equivalence | 701–714 | `CognitiveObject`, `SemanticSignature`, `OBJECT_TYPE_MAP`, `EPISTEMIC_CLASS_KEYWORDS` |
| 2 | Bindings and context | 705–714 | `CognitiveBinding`, `BindingType`, `ContextRegion`, `ContextLocalityGraph` |
|| 3 | Operator registry | 715–723 | `OperatorSpec`, `OperatorRegistry`, 20 typed operators (`DEDUCE`…`FORGET`) — 11 reasoning + 9 memory/structural |
| 4 | Execution graph with attribution | 724–730 | `ReasoningNode`, `ReasoningEdge`, `ReasoningExecutionGraph`, `ReasoningAttribution` |
| 5 | Belief state | 731–740 | `BeliefState`, `ConfirmationBiasMonitor`, `DisconfirmationBudget` |
| 6 | Uncertainty decomposition | 741–773 | `UncertaintyState`, `UncertaintyComponent`, `localize_evidence()` |
| 7 | Search state and mode management | 774–777 | `SearchState`, `ReasoningModeState`, `MetaCognitiveState` |
| 8 | Memory operational substrate | 793–800 | `MemoryObject`, `MemoryOperationType`, `MemoryOperationRecord`, `MemoryTrustState` |
| 9 | Field lineage and epistemic preservation | 796–799 | `FieldLineage`, `FieldPreservationRecord`, `check_epistemic_preservation()` |
| 10 | Memory retrieval governance | 873–880 | `MemoryOperationGraph.retrieve()`, `query()`, `retrieve_by_tag()`, `get_dependents()`, `dependency_safe_forget()` |
| 11 | Meta-cognitive state and persistence | 778–780 | `MetaCognitiveState`, `MetaCognitiveEvent`, `save()`/`load()` |
| 12 | Interface coupling (CognitiveIntegrityGate) | all | `CognitiveIntegrityGate`, `propose_cognitive_object()`, `execute_operator()`, `admit_to_memory()` |

## 2. The 4-slice architecture (consolidated)

### Slice 1: Reality Gate (RC/IR)
- **`Promote(X) => RC(X) >= theta_RC AND IR(X) <= theta_IR`**
- Prevents epistemic autopoisoning: LLM-generated X → stored → retrieved → treated as evidence → strengthened → stored again
- Admission pipeline: Propose → Type → CheckEvidence → CheckScope → CheckProvenance → Admit
- Use pipeline: Retrieve → Validate → Contextualize → Use
- **Implemented**: Wired into `CognitiveIntegrityGate` via `RealityGate` import from `AMOS_COGNITIVE_SUBSTRATE_REALITY_GATE.py`

### Slice 2: Reasoning Execution Graph (`R_t = (N_t, E_t, O_t, Pi_t, U_t)`)
- 11 typed reasoning operators with declared postconditions (DEDUCE, ABDUCE, GENERALIZE, SPECIALIZE, NEGATE, CONTRAST, AGGREGATE, PROJECT, SIMULATE, RETRIEVE, REVISE)
- State-transition legality (forbidden: M

---
**MOC:** [[references_MOC]]
