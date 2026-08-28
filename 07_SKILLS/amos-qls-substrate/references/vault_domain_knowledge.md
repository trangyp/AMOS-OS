---
title: "Vault Domain Knowledge — Amos Qls Substrate"
type: reference
source: 07_SKILLS/amos-qls-substrate/references
tags: [reference, amos-qls-substrate, canon/skill]
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# Vault-Sourced Domain Knowledge

> Source: AMOS_OS Obsidian vault (`_00_Cosmo brain/`)
> Epistemic class: SOURCE_CLAIM
> Extracted from skill: `amos-qls-substrate`

## Vault-Sourced Content

### Source 1: AMOS Cognitive Substrate v2.0 — Implementation Notes

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

### Source 2: AMOS Cognitive Substrate v2.0 — Implementation Notes

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

### Source 3: AMOS Cognitive Substrate — Four-Workflow Bridge to Matrix

> Path: `cognitive/Cognitive_Substrate_Workflow_Bridge.md` | Size: 8805 chars | Match score: 10

# AMOS Cognitive Substrate — Four-Workflow Bridge to Matrix

## Canonical summary

The AMOS Cognitive Architecture Matrix (29 layers × 12 operations × 9 planes × H/M/L) is the master reference for cognitive completeness. The 4 cognitive substrate workflows are the operational implementations of the matrix's lower layers. The bridge maps each workflow to the matrix cells it implements.

## Matrix → workflow mapping

### 1. amos-cognitive-substrate-interface.md → Matrix cells: L1 Observation, L5 Binding, L6 Working State, L7 Memory

This workflow binds reasoning and memory through asymmetric gated pipelines (RC/IR reality gate, provenance cycle detection, counterfactual contamination firewall, scope checking). It implements:

- L1 Observation formation + verification (reality-contact gate)
- L5 Binding formation (reasoning→memory binding with provenance)
- L6 Working State (reasoning graph as working state)
- L7 Memory (memory graph encode/normalize/admit/index/consolidate/retrieve)
- L7 Memory activation, retrieval failure attribution (earliest causal cut)
- L7 Memory field-level invalidation, supersession

### 2. amos-cognitive-substrate-memory-graph.md → Matrix cells: L7 Memory

This workflow persists memory operations as a typed execution graph with attribution, failure typing, field-level invalidation, supersession, consolidation with contradiction retention. It implements:

- L7 Memory formation, binding, activation, retrieval, revision, promotion, demotion, consolidation, forgetting, replay, invalidation, verification, archiving
- L7 Memory failure typing (STORE/INDEX/QUERY/RANK/FILTER/INTERPRET)
- L7 Memory earliest causal cut attribution
- L7 Memory field-level invalidation
- L7 Memory supersession
- L7 Memory consolidation with contradiction retention

### 3. amos-cognitive-substrate-reality-gate.md → Matrix cells: L1 Observation, L23 Metacognition

This workflow admits claims to durable memory through the RC/IR reality gate (reality contacts, internal recursions, quarantine not delete, autopoisoning detection). It implements:

- L1 Observation formation + verification (reality-contact certification)
- L23 Metacognition (autopoisoning detection, gap/contradiction detection, quarantine decision, recovery decision)

### 4. amos-cognitive-substrate-reasoning-graph.md → Matrix cells: L9 Inference, L10 World Model, L13 Prediction, L17 Decision

This workflow persists reasoning as an executable operation graph with transition legality, operator preconditions/postconditions, composition validation, failure attribution, counterfactual repair. It implements:

- L9 Inference formation + verification (operator sequence, transition legality)
- L10 World Model (reasoning graph as world model)
- L13 Prediction (multi-step reasoning as prediction)
- L17 Decision (reasoning output as decision)
- L20 Credit Assignment (failure attribution to earliest wrong transition)
- L21 Lesson (counterfactual repair as lesson formation)

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
node_id: amos-qls-substrate-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/amos-qls-substrate/references/vault_domain_knowledge.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[references_MOC]]
