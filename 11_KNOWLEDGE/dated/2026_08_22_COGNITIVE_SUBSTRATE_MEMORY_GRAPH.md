---
title: 2026 08 22 COGNITIVE SUBSTRATE MEMORY GRAPH
type: memory
source: 11_KNOWLEDGE/dated
origin_architect: Trang Phan
provenance: cosmo-brain/AMOS_COGNITIVE_SUBSTRATE_MEMORY_GRAPH.py
confidence: 0.9
epistemic_class: DERIVED
conclusion_label: VERIFIED
tags:
- canon-group/tech-ai
- cosmo-brain
- cognitive-substrate
- memory-operation-graph
- field-lineage
- epistemic-preservation
- rscf/claim
- rscf/provenance
- rscf/state/observation
- topic/2026-08-22-cognitive-substrate-memory-graph
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


# Cognitive Substrate Memory Operation Graph

> Slice 3 of the AMOS Cognitive Substrate Layer. Implements the memory side of
> `M_t = (V_t, E_t, O_t, I_t, Q_t, L_t)` with field-level lineage, epistemic-class
> preservation, consolidation with contradiction retention, retrieval graph with
> failure attribution, dependency-safe forgetting, and earliest causal memory cut.
>
> Source: `cosmo-brain/AMOS_COGNITIVE_SUBSTRATE_MEMORY_GRAPH.py` (27 self-tests)
> Test: `cosmo-brain/test_cognitive_substrate_memory_graph.py` (11 integration, 38 total)
> Skill: amos-cognitive-substrate-memory-graph
> See also: 2026-08-22 Cognitive Substrate Reality Gate · 2026-08-22 Cognitive Substrate Reasoning Graph · 2026-08-22 AMOS Obsidian Memory Bridge

## 1. The problem this solves

A memory system is not fundamentally a database of remembered sentences. It is a
**state-transforming execution system**. When an answer fails, the failure must be
reconstructed as an operation-variable execution graph and attributed to the
**earliest causal memory defect** — not blamed on whichever retrieval looked wrong last.

## 2. Core formalization

```
M_t = (V_t, E_t, O_t, I_t, Q_t, L_t)
```

| Component | Meaning | Gaps |
|-----------|---------|------|
| V_t | Memory-object graph (fields with lineage) | 810–815 |
| E_t | Semantic / provenance / dependency edges | 825–826 |
| O_t | Memory operation history | 801–802 |
| I_t | Indexes | 801 |
| Q_t | Quarantine / trust state | 827–830 |
| L_t | Lifecycle state (active, superseded, retracted, archived) | 822–824 |

Memory evolution: `M_{t+1} = Pi_admission(R_reconcile(C_consolidate(U_update(M_t, E_t))))`

## 3. Memory operation pipeline (gap 801)

```
encode -> normalize -> admit -> consolidate -> index -> retrieve -> filter -> interpret -> use -> update
```

Each operation is typed, recorded, and attributable.

## 4. Field-level lineage (gaps 810–812)

Each stored field traces to a source span or derivation operation. When evidence fails,
only the affected field is invalidated — not the entire memory object. This enables
**partial-memory validity**: some fields of a memory object may be valid while others
are stale or wrong.

## 5. Epistemic-class preservation (gaps 831–837)

| Gap | Preservation rule |
|-----|-------------------|
| 831 | SOURCE_CLAIM, OBSERVATION, DERIVED, MODEL, DECISION survive storage unchanged |
| 832 | Modality ("may", "likely", "must", "observed", "predicted") must survive compression |
| 833 | Negation ("not", exceptions, exclusion conditions) must not be dropped |
| 834 | Quantifiers ("some", "most", "all", thresholds) must remain explicit |
| 835 | Correlation cannot become cause during consolidation |
| 836 | Future forecast cannot become present observation after time passes |
| 837 | "Agent A believes X" cannot become "X is true" |

## 6. Consolidation (gaps 841–844)

- Contradictions among sources are **retained**, not erased.
- Summary confidence **cannot exceed** the max source confidence.
- If contradictions exist, confidence is halved and conclusion becomes `COMPETING`.

## 7. Retrieval graph (gaps 873–878)

Retrieval is modeled as graph traversal with path provenance. Failure is separated into:
`STORE_FAILURE | INDEX_FAILURE | QUERY_FAILURE | RANK_FAILURE | FILTER_FAILURE | INTERPRET_FAILURE`.

False-negative detection (gap 877): relevant memory that was available but missed.
False-positive detection (gap 878): retrieved items that contaminated reasoning despite weak applicability.

## 8. Dependency-safe forgetting (gaps 891–893)

Before evicting a memory, the system checks which active conclusions depend on it.
If dependents exist, eviction is **blocked** and the dependent list is returned.
Only when no active dependents remain is the object archived (not deleted).

## 9. Memory cemetery / archive (gaps 898–899)

Archived objects remain queryable for forensic/research use. Resurrection back to
active state requires explicit revalidation of epistemic preservation.

## 10. Reconsolidation governance (gaps 849–850)

Retrieval itself may trigger update — this needs explicit governance. `reconsolidate()`
always records the operation in the execution graph. **Reading a memory must never
silently rewrite it.**

## 11. Cross-slice integration

- **Slice 1 (Reality Gate)**: reality-gate-admitted objects are encoded into this graph.
  Field lineage traces back to the reality-gate object's `oid`.
- **Slice 2 (Reasoning Graph)**: memory objects feed back as trusted reasoning inputs.
  When a memory field is invalidated, the reasoning graph can trace the impact via
  earliest-failure attribution.

## 12. Sequencing

|| Slice | Status | Tests |
|-------|--------|-------|
|| 1. RC/IR reality gate | DONE | 26 |
|| 2. Reasoning execution graph | DONE | 29 |
|| 3. Memory operation graph (this) | DONE | 38 |
||| 4. Interface coupling | DONE | 146 (unified substrate `AMOS_COGNITIVE_SUBSTRATE.py` self-test now covers all 4 slices) |

## 13. Governance record

- Mutation class: M2 (high-consequence decision architecture).
- Authority: explicit user authorization (repo architect).
- Rollback: delete the 5 artifacts listed in the workflow file.
- Reversible: yes — additive only; no existing brain module was modified.

---
**Links:** [[DATED_MOC]] | [[KNOWLEDGE_MOC]]
