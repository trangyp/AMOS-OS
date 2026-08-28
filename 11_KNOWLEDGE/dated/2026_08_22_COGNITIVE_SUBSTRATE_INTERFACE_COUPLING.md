---
title: 2026 08 22 COGNITIVE SUBSTRATE INTERFACE COUPLING
type: cognitive
source: 11_KNOWLEDGE/dated
origin_architect: Trang Phan
provenance: cosmo-brain/AMOS_COGNITIVE_SUBSTRATE_INTERFACE.py
confidence: 0.9
epistemic_class: DERIVED
conclusion_label: VERIFIED
tags:
- canon-group/tech-ai
- cosmo-brain
- cognitive-substrate
- interface-coupling
- epistemic-autopoisoning
- cognitive-integrity
- rscf/claim
- rscf/provenance
- rscf/state/observation
- topic/2026-08-22-cognitive-substrate-interface
- dated
- dated/2026-08-22
- canon/knowledge
date: 2026-08-22
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: temporal_log
---


# Cognitive Substrate Interface Coupling

> Slice 4 (final) of the AMOS Cognitive Substrate Layer. Implements the asymmetric
> gated coupling between reasoning and memory, completing:
>
> `CognitiveIntegrity = ReasoningIntegrity ∧ MemoryIntegrity ∧ InterfaceIntegrity ∧ RealityContact`
>
> Source: `cosmo-brain/AMOS_COGNITIVE_SUBSTRATE_INTERFACE.py` (19 self-tests)
> Test: `cosmo-brain/test_cognitive_substrate_interface.py` (13 integration, 32 total)
> Skill: amos-cognitive-substrate-interface
> See also: 2026-08-22 Cognitive Substrate Reality Gate · 2026-08-22 Cognitive Substrate Reasoning Graph · 2026-08-22 Cognitive Substrate Memory Graph · amos-core-reasoning

## 1. The problem this solves

The deepest failure mode in long-horizon AMOS cognition is **epistemic autopoisoning**:

```
LLM generates X -> X stored -> X retrieved -> X treated as evidence
-> X strengthened -> X stored again
```

Confidence rises with **no new reality contact**. The system becomes internally coherent
and externally wrong. Slices 1-3 provide the components; this slice binds them together
with asymmetric gated pipelines that structurally forbid the autopoisoning loop.

## 2. The coupling

The coupling is **ASYMMETRIC and GATED**:

**Read path** (reasoning reads memory):
```
Retrieve -> Validate -> Contextualize -> Use
```

**Write path** (reasoning writes memory):
```
Propose -> Type -> CheckEvidence -> CheckScope -> CheckProvenance -> Admit
```

**NEVER**:
- `Retrieve -> Truth` (retrieved memory is not automatically true)
- `Generate -> Memory` (LLM output is not automatically memory)

## 3. Firewalls

| Firewall | Gap | What it blocks |
|----------|-----|----------------|
| Reality gate | 868-871 | Model-only claims (RC=0) entering memory |
| Provenance cycle detection | 870 | Memory descending from model itself being treated as evidence |
| Self-generated corroboration | 872 | Multiple outputs from one internal claim counted as independent sources |
| Counterfactual contamination | 765 | Generated future scenarios re-entering memory as observations |

## 4. Provenance cycle detection (gap 870)

The interface tracks which memory objects were generated from which reasoning objects
(`_reasoning_to_memory`) and which reasoning objects were derived from memory
(`_memory_to_reasoning`). When a memory object is retrieved, the system checks whether
it ultimately descends from the model itself — if so, it is rejected at the Validate stage.

## 5. Self-generated corroboration firewall (gap 872)

Multiple memory objects traced to the same reasoning source are **not independent**.
`check_corroboration_independence([mid_a, mid_b, ...])` detects this and returns the
reason. This prevents the system from treating its own repeated outputs as multiple
independent sources of evidence.

## 6. Counterfactual contamination firewall (gap 765)

Generated future scenarios (temporal_type = "future_forecast") must never re-enter
memory as observations (epistemic_class = OBSERVATION). The write pipeline checks this
at the CheckProvenance stage and blocks the write.

## 7. CognitiveIntegrity evaluation

The completion standard:

```
CognitiveIntegrity = ReasoningIntegrity ∧ MemoryIntegrity
                     ∧ InterfaceIntegrity ∧ RealityContact
```

| Component | Check |
|-----------|-------|
| ReasoningIntegrity | No illegal operations in reasoning graph |
| MemoryIntegrity | No quarantined objects in active use |
| InterfaceIntegrity | No autopoisoning detected |
| RealityContact | At least one object with RC > 0 |

## 8. Cross-slice integration

This slice binds all three prior slices:
- **Slice 1 (Reality Gate)**: RC/IR gate runs at the CheckEvidence stage of the write pipeline.
- **Slice 2 (Reasoning Graph)**: read pipeline injects memory objects as trusted reasoning nodes.
- **Slice 3 (Memory Graph)**: write pipeline encodes admitted objects with field lineage and epistemic preservation.

## 9. Full 4-slice test summary

| Slice | Module | Self-tests | Integration | Total |
|-------|--------|-----------|-------------|-------|
| 1. Reality Gate | `AMOS_COGNITIVE_SUBSTRATE_REALITY_GATE.py` | 17 | 9 | 26 |
| 2. Reasoning Graph | `AMOS_COGNITIVE_SUBSTRATE_REASONING_GRAPH.py` | 20 | 9 | 29 |
| 3. Memory Graph | `AMOS_COGNITIVE_SUBSTRATE_MEMORY_GRAPH.py` | 27 | 11 | 38 |
| 4. Interface Coupling | `AMOS_COGNITIVE_SUBSTRATE_INTERFACE.py` | 19 | 13 | 32 |
| **TOTAL** | | **83** | **42** | **125** |

## 10. Governance record

- Mutation class: M2 (high-consequence decision architecture — changes how truth/reality is evaluated).
- Authority: explicit user authorization (repo architect).
- Rollback: delete the 5 artifacts listed in the workflow file.
- Reversible: yes — all artifacts are additive; no existing brain module was modified.

---
**Links:** [[DATED_MOC]] | [[KNOWLEDGE_MOC]]
