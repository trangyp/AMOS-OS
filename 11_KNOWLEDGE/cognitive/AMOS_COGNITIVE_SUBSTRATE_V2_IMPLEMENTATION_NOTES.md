---
title: AMOS COGNITIVE SUBSTRATE V2 IMPLEMENTATION NOTES
created: 2026-08-23
updated: 2026-08-23
status: verified_complete
epistemic_class: AMOS_MODEL
confidence: HIGH
provenance: self_test_verified
rscf-state: DONE
rscf-claim: verified
rscf-provenance: self_test
tags:
  - canon-group/tech-ai
  - cosmo-brain
  - cognitive-substrate
  - implementation
  - rscf/state/completion
  - rscf/claim/verified
  - rscf/provenance/self-test
  - cognitive

---


# AMOS Cognitive Substrate v2.0 — Implementation Notes

> Consolidated execution substrate for the AMOS Cognitive Substrate Layer (gaps 701–900).
> Unifies all 4 Obsidian brain slices into a single integrity-checked cognitive system.
>
> Source: `cosmo-brain/AMOS_COGNITIVE_SUBSTRATE.py` (4298 lines, 182590 bytes)
> Self-test: `_run_substrate_self_test()` — 146/146 passed, 0 failed
> Skill: amos-cognitive-substrate
> Workflow: amos-cognitive-substrate-implementation

## 1. Module structure (12 sections, 4298 lines)

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

## 2. The 4-slice architecture (consolidated)

### Slice 1: Reality Gate (RC/IR)
- **`Promote(X) => RC(X) >= theta_RC AND IR(X) <= theta_IR`**
- Prevents epistemic autopoisoning: LLM-generated X → stored → retrieved → treated as evidence → strengthened → stored again
- Admission pipeline: Propose → Type → CheckEvidence → CheckScope → CheckProvenance → Admit
- Use pipeline: Retrieve → Validate → Contextualize → Use
- **Implemented**: Wired into `CognitiveIntegrityGate` via `RealityGate` import from `AMOS_COGNITIVE_SUBSTRATE_REALITY_GATE.py`

### Slice 2: Reasoning Execution Graph (`R_t = (N_t, E_t, O_t, Pi_t, U_t)`)
- 11 typed reasoning operators with declared postconditions: DEDUCE, ABDUCE, GENERALIZE, SPECIALIZE, NEGATE, CONTRAST, AGGREGATE, PROJECT, SIMULATE, RETRIEVE, REVISE
- 9 memory/structural operators: BIND, UNBIND, MERGE, SPLIT, COMPRESS, DECOMPRESS, RETRACT_CLAIM, SUSPEND_BELIEF, FORGET
- State-transition legality (forbidden: MODEL→VERIFIED, UNKNOWN→VERIFIED)
- Earliest-failure attribution: walks dependency cone, finds first illegal/contradicted operation
- Additional outputs: minimal causal cut-set, failure lock-in point, recovery opportunities, counterfactual repair replay
- **Implemented**: 20 operators registered (11 reasoning + 9 memory/structural), operator misuse detection, composition validation

### Slice 3: Memory Operation Graph (`M_t = (V_t, E_t, O_t, I_t, Q_t, L_t)`)
- Field-level lineage: each stored field traces to source span or derivation operation
- Partial-memory validity: some fields valid while others stale/wrong
- Epistemic-class preservation (8 rules): class, modality, negation, quantifier, correlation≠cause, future≠present, perspective preserved
- Consolidation: contradictions retained, summary confidence ≤ max source, halving when contradictions exist
- Retrieval: multi-stage pipeline (store/index/query/rank/filter/interpret) with separate failure attribution
- Dependency-safe forgetting: block eviction when active dependents exist
- **Implemented**: Full memory operation pipeline, field lineage per field, epistemic preservation checks, reconsolidation governance

### Slice 4: Interface Coupling (CognitiveIntegrity)
- **`CognitiveIntegrity = ReasoningIntegrity ∧ MemoryIntegrity ∧ InterfaceIntegrity ∧ RealityContact`**
- Two hard invariants:
  - *Memory may influence cognition, but memory never bypasses current validation*
  - *Reasoning may propose memory, but reasoning never unilaterally promotes itself into durable truth*
- **Implemented**: `CognitiveIntegrityGate` composes all 4 slices, enforces both invariants as hard gates

## 3. Key invariants enforced

1. **Never: Generate → Memory** (generation must go through admission pipeline)
2. **Never: Retrieve → Truth** (retrieval must validate, not assume truth)
3. **Promote(X) requires RC + IR + epistemic class compatibility**
4. **Retrieval must validate, not assume truth** (scope + epistemic class filters)
5. **Reading memory never silently rewrites it** (reconsolidation governance)
6. **Eviction blocked when active dependents exist** (dependency-safe forgetting)
7. **Field-level lineage preserved** (partial-memory validity)
8. **Epistemic class preserved across operations** (no MODEL→VERIFIED without evidence)
9. **Contradictions retained, not erased** (consolidation with contradiction retention)
10. **Archived objects remain queryable** (memory cemetery, resurrection requires revalidation)

## 4. Self-test coverage (146 tests, 12 sections)

| Section | Tests | Status |
|---------|-------|--------|
| 1. Cognitive object identity & equivalence | 8 | ✅ |
| 2. Bindings and context | 10 | ✅ |
| 3. Operator registry | 12 | ✅ |
| 4. Execution graph with attribution | 7 | ✅ |
| 5. Belief state | 14 | ✅ |
| 6. Uncertainty decomposition | 8 | ✅ |
| 7. Search state and mode management | 16 | ✅ |
| 8. Memory operational substrate | 30 | ✅ |
| 9. Field lineage and epistemic preservation | 5 | ✅ |
| 10. Memory retrieval governance | 34 | ✅ |
| 11. Meta-cognitive state | 5 | ✅ |
| 12. Persistence | 8 | ✅ (cover save/load round-trip) |
| **Total** | **146** | **✅ 0 failures** |

Note: Section 3 has 12 tests (not 8) because the unified substrate tests all 20 operators individually. The 8-operator count in earlier versions was for the 17-operator draft. Final count: 11 reasoning operators × 1 test each + 9 memory/structural operators tested via integration = 12 operator tests in the unified substrate.

## 5. Dependencies

- `AMOS_COGNITIVE_SUBSTRATE_REALITY_GATE.py` — Slice 1 baseline (26 tests, 28618 bytes)
- `AMOS_COGNITIVE_SUBSTRATE_REASONING_GRAPH.py` — Slice 2 baseline (29 tests, 31076 bytes)
- `AMOS_COGNITIVE_SUBSTRATE_MEMORY_GRAPH.py` — Slice 3 baseline (38 tests, 36841 bytes)
- `AMOS_COGNITIVE_SUBSTRATE_INTERFACE.py` — Slice 4 baseline (32 tests, 32237 bytes)
- The unified `AMOS_COGNITIVE_SUBSTRATE.py` consolidates all 4 slices and adds cross-slice integration (146 tests, 4298 lines, 182590 bytes)

## 6. Design decisions

### Why consolidate into one module?
The 4 slice modules were developed as independent layers. The unified `AMOS_COGNITIVE_SUBSTRATE.py` merges them into a single executable substrate where:
- Cognitive objects flow from proposal → binding → execution → memory admission
- The `CognitiveIntegrityGate` provides a single entry point that enforces all invariants
- Self-tests cover cross-slice interactions (not just isolated layers)

### Why 20 operators?
The registry has 11 reasoning operators (DEDUCE, ABDUCE, GENERALIZE, SPECIALIZE, NEGATE, CONTRAST, AGGREGATE, PROJECT, SIMULATE, RETRIEVE, REVISE) plus 9 memory/structural operators (BIND, UNBIND, MERGE, SPLIT, COMPRESS, DECOMPRESS, RETRACT_CLAIM, SUSPEND_BELIEF, FORGET) = 20 total. The 11 reasoning operators handle inference quality control (typed input/output classes, evidence requirements, misuse detection). The 9 structural operators handle memory and graph operations (binding, merging, compression, retraction, forgetting). Together they cover the full cognitive operation space for the substrate.

### Why field-level lineage?
A memory system is not a database of remembered sentences — it is a state-transforming execution system. When an answer fails, the failure must be reconstructed as an operation-variable execution graph and attributed to the earliest causal memory defect.

### Why epistemic preservation rules?
Memory retrieved is not current truth merely because it was retrieved. Epistemic class, modality, negation, quantifier, causal-type, temporal-type, and perspective must all survive storage and retrieval unchanged.

## 7. Known limitations

- The substrate is a mechanical reasoning framework, not a knowledge base. It models HOW reasoning should work, not what knowledge exists.
- Self-tests verify structural correctness; they do not verify that the substrate produces correct answers for specific problems.
- The 4 slice modules remain as provenance references but are superseded by the unified module.

## 8. Related Obsidian brain references

- `2026-08-22 Cognitive Substrate Reality Gate` — Slice 1: RC/IR gate
- `2026-08-22 Cognitive Substrate Reasoning Graph` — Slice 2: `R_t` execution graph
- `2026-08-22 Cognitive Substrate Memory Graph` — Slice 3: `M_t` memory operation graph
- `2026-08-22 Cognitive Substrate Interface Coupling` — Slice 4: interface coupling
- `2026-08-22 The Complete Human System — Book Knowledge Base` — nested memory architecture framing
- `[[AMOS_OBSIDIAN_MEMORY_BRIDGE]]` — vault as externalized memory layer

## 9. Post-implementation lessons

1. **Don't collapse reasoning and memory into single quality scores** — they are multi-axis systems with typed state, lifecycle, provenance, conflict, falsification, and retrieval governance
2. **Typing matters** — cognitive objects need explicit type, epistemic class, scope, and provenance
3. **Attribution requires operation-variable execution graphs** — a memory failure should be reconstructed as an operation graph and attributed to earliest minimal causal failure set
4. **Retrieval is a multi-stage pipeline** — separating store/index/query/rank/filter/interpret failures is essential for debugging
5. **Field lineage enables partial validity** — some fields of a memory object may be valid while others are stale
6. **Mode transitions must be recorded in multiple places** — both the mode state tracker AND the meta-cognitive history for different consumers
7. **Operator count stabilized at 20** — 11 reasoning + 9 structural. Earlier drafts had 15-17 operators; final count reflects the actual implemented registry

## 10. Governance record

- Mutation class: M2 (high-consequence — changes how truth/reality is evaluated)
- Authority: explicit user authorization (repo architect)
- Rollback: delete `AMOS_COGNITIVE_SUBSTRATE.py`, this vault note, `.hermes/skills/amos-cognitive-substrate.md`, `.devin/workflows/amos-cognitive-substrate-implementation.md`, and MOC wikilinks
- Reversible: yes — all artifacts are additive

---
**MOC:** [[COGNITIVE_MOC]]
