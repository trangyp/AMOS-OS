---
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
title: Vault Domain Knowledge — Amos Information Operator Engine
type: reference
source: 07_SKILLS/amos-information-operator-engine/references
tags:
  - reference
  - amos-information-operator-engine
  - type/skill
  - law-hierarchy
  - trang-framework-recursive-ontology-dynamics
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---

# Vault-Sourced Domain Knowledge

> Source: AMOS_OS Obsidian vault (`_00_Cosmo brain/`)
> Epistemic class: SOURCE_CLAIM
> Extracted from skill: `amos-information-operator-engine`

## Vault-Sourced Content

### Source 1: 2026-08-25 — Information-Measure Governance Layer

> Path: `dated/2026-08-25/2026-08-25 Information-Measure Governance Layer.md` | Size: 2700 chars | Match score: 10

## 2026-08-25 — Information-Measure Governance Layer

## Gap found

"Entropy" and "information" are the corpus's most polysemous words. Six distinct measures circulate: Shannon H, AMOS structural proxy E_X (from ENTROPY_LACUNARITY.md), von Neumann S(ρ) (quantum library: SSA master inequality supersedes Araki-Lieb), thermodynamic S, relative entropy D_KL, and mutual information I(X;Y). The collapse-sense problem was solved (three senses separated); the information-sense problem was not — nothing prevented an E_proxy value being compared to a von Neumann entropy, or D_KL direction being silently reversed.

## Closure (4 channels)

| Channel             | Artifact                                                                                                                                           |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Skill               | `amos/amos-information-measure-governance` — six-measure inventory with formulas/domains/governs columns, five conflation blocks, tagging contract |
| Agent               | `amos-information-theory-master` — 6 capabilities incl. cross-measure equation block and D_KL direction check                                      |
| Workflow            | `amos-information-theory-master-workflow.md` — 7-step pipeline with G11 composition routing                                                        |
| Memory + vault note | recorded                                                                                                                                           |

## The five conflation blocks

1. E_proxy ≠ thermodynamic S (restated at measure level)
1. H ≠ S(ρ) — classical vs quantum entropies differ structurally (conditional von Neumann can be negative)
1. D_KL is asymmetric — direction must be stated; reversal changes the value
1. I(X;Y) ≠ causation — dependence language only; causal phrasing routes to QCLA modes
1. Channel-capacity analogies ("reasoning bandwidth") = MODEL unless channel model + noise declared

## Key design decisions

1. **Tagging contract**: `measure · base · domain` on every invocation — mechanical, checkable.
1. **Cross-measure equations need conversion derivations** — absent derivation, block.
1. **Finite-sample discipline**: Miller–Madow bias correction required for estimated entropies.
1. **Library grounding**: 34 QI/entropy entries support S(ρ)-side claims only; Cover & Thomas supports H-side.

## Epistemic-gate family update

The family now has seven named gates covering the corpus's characteristic failure modes. This layer also demonstrates consolidation economy: it reuses collapse-separation pattern, tensor gate G11, QCI U3-classification, and scaling-law bias-correction practice rather than inventing new machinery.

______________________________________________________________________

______________________________________________________________________

### Source 2: AMOS Cognitive Substrate v2.0 — Implementation Notes

> Path: `cognitive/AMOS_Cognitive_Substrate_v2_Implementation_Notes.md` | Size: 11609 chars | Match score: 5

## AMOS Cognitive Substrate v2.0 — Implementation Notes

> Consolidated execution substrate for the AMOS Cognitive Substrate Layer (gaps 701–900).
> Unifies all 4 Obsidian brain slices into a single integrity-checked cognitive system.
>
> Source: `cosmo-brain/AMOS_COGNITIVE_SUBSTRATE.py` (4298 lines, 182590 bytes)
> Self-test: `_run_substrate_self_test()` — 146/146 passed, 0 failed
> Skill: amos-cognitive-substrate
> Workflow: amos-cognitive-substrate-implementation

## 1. Module structure (12 sections, 4298 lines) (2)

| #   | Section                                     | Gaps    | Key classes                                                                                                       |
| --- | ------------------------------------------- | ------- | ----------------------------------------------------------------------------------------------------------------- |
| 1   | Cognitive object identity & equivalence     | 701–714 | `CognitiveObject`, `SemanticSignature`, `OBJECT_TYPE_MAP`, `EPISTEMIC_CLASS_KEYWORDS`                             |
| 2   | Bindings and context                        | 705–714 | `CognitiveBinding`, `BindingType`, `ContextRegion`, `ContextLocalityGraph`                                        |
| 3   | Operator registry                           | 715–723 | `OperatorSpec`, `OperatorRegistry`, 20 typed operators (`DEDUCE`…`FORGET`) — 11 reasoning + 9 memory/structural   |
| 4   | Execution graph with attribution            | 724–730 | `ReasoningNode`, `ReasoningEdge`, `ReasoningExecutionGraph`, `ReasoningAttribution`                               |
| 5   | Belief state                                | 731–740 | `BeliefState`, `ConfirmationBiasMonitor`, `DisconfirmationBudget`                                                 |
| 6   | Uncertainty decomposition                   | 741–773 | `UncertaintyState`, `UncertaintyComponent`, `localize_evidence()`                                                 |
| 7   | Search state and mode management            | 774–777 | `SearchState`, `ReasoningModeState`, `MetaCognitiveState`                                                         |
| 8   | Memory operational substrate                | 793–800 | `MemoryObject`, `MemoryOperationType`, `MemoryOperationRecord`, `MemoryTrustState`                                |
| 9   | Field lineage and epistemic preservation    | 796–799 | `FieldLineage`, `FieldPreservationRecord`, `check_epistemic_preservation()`                                       |
| 10  | Memory retrieval governance                 | 873–880 | `MemoryOperationGraph.retrieve()`, `query()`, `retrieve_by_tag()`, `get_dependents()`, `dependency_safe_forget()` |
| 11  | Meta-cognitive state and persistence        | 778–780 | `MetaCognitiveState`, `MetaCognitiveEvent`, `save()`/`load()`                                                     |
| 12  | Interface coupling (CognitiveIntegrityGate) | all     | `CognitiveIntegrityGate`, `propose_cognitive_object()`, `execute_operator()`, `admit_to_memory()`                 |

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

______________________________________________________________________

### Source 3: AMOS Cognitive Substrate v2.0 — Implementation Notes

> Path: `cognitive/AMOS_Cognitive_Substrate_v2_Implementation_Notes_2.md` | Size: 9825 chars | Match score: 5

## AMOS Cognitive Substrate v2.0 — Implementation Notes — part 2

> Consolidated execution substrate for the AMOS Cognitive Substrate Layer (gaps 701–900).
> Unifies all 4 Obsidian brain slices into a single integrity-checked cognitive system.
>
> Source: `cosmo-brain/AMOS_COGNITIVE_SUBSTRATE.py` (4298 lines)
> Self-test: `_run_substrate_self_test()` — 146/146 passed, 0 failed
> Skill: amos-cognitive-substrate
> Workflow: amos-cognitive-substrate-implementation

## 1. Module structure (12 sections, 4298 lines)

| #   | Section                                     | Gaps              | Key classes                                                                                                       |
| --- | ------------------------------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------- |
| 1   | Cognitive object identity & equivalence     | 701–714           | `CognitiveObject`, `SemanticSignature`, `OBJECT_TYPE_MAP`, `EPISTEMIC_CLASS_KEYWORDS`                             |
| 2   | Bindings and context                        | 705–714           | `CognitiveBinding`, `BindingType`, `ContextRegion`, `ContextLocalityGraph`                                        |
|     | 3                                           | Operator registry | 715–723                                                                                                           |
| 4   | Execution graph with attribution            | 724–730           | `ReasoningNode`, `ReasoningEdge`, `ReasoningExecutionGraph`, `ReasoningAttribution`                               |
| 5   | Belief state                                | 731–740           | `BeliefState`, `ConfirmationBiasMonitor`, `DisconfirmationBudget`                                                 |
| 6   | Uncertainty decomposition                   | 741–773           | `UncertaintyState`, `UncertaintyComponent`, `localize_evidence()`                                                 |
| 7   | Search state and mode management            | 774–777           | `SearchState`, `ReasoningModeState`, `MetaCognitiveState`                                                         |
| 8   | Memory operational substrate                | 793–800           | `MemoryObject`, `MemoryOperationType`, `MemoryOperationRecord`, `MemoryTrustState`                                |
| 9   | Field lineage and epistemic preservation    | 796–799           | `FieldLineage`, `FieldPreservationRecord`, `check_epistemic_preservation()`                                       |
| 10  | Memory retrieval governance                 | 873–880           | `MemoryOperationGraph.retrieve()`, `query()`, `retrieve_by_tag()`, `get_dependents()`, `dependency_safe_forget()` |
| 11  | Meta-cognitive state and persistence        | 778–780           | `MetaCognitiveState`, `MetaCognitiveEvent`, `save()`/`load()`                                                     |
| 12  | Interface coupling (CognitiveIntegrityGate) | all               | `CognitiveIntegrityGate`, `propose_cognitive_object()`, `execute_operator()`, `admit_to_memory()`                 |

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

______________________________________________________________________

**MOC:** references_MOC

## Related

- [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · references_MOC · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-information-operator-engine-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/amos-information-operator-engine/references/vault_domain_knowledge.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
