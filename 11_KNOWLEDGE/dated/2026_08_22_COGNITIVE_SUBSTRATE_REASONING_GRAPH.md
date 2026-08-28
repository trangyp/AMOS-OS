---
title: 2026 08 22 COGNITIVE SUBSTRATE REASONING GRAPH
type: cognitive
source: 11_KNOWLEDGE/dated
origin_architect: Trang Phan
provenance: cosmo-brain/AMOS_COGNITIVE_SUBSTRATE_REASONING_GRAPH.py
confidence: 0.9
epistemic_class: DERIVED
conclusion_label: VERIFIED
tags:
- canon-group/tech-ai
- cosmo-brain
- cognitive-substrate
- reasoning-execution-graph
- earliest-failure-attribution
- rscf/claim
- rscf/provenance
- rscf/state/observation
- topic/2026-08-22-cognitive-substrate-reasoning-graph
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


# Cognitive Substrate Reasoning Execution Graph

> Slice 2 of the AMOS Cognitive Substrate Layer. Implements the reasoning side of
> `R_t = (N_t, E_t, O_t, Pi_t, U_t)` with typed inference operators, transition
> legality, earliest-failure attribution, minimal causal cut-set, and counterfactual
> repair replay.
>
> Source: `cosmo-brain/AMOS_COGNITIVE_SUBSTRATE_REASONING_GRAPH.py` (20 self-tests)
> Test: `cosmo-brain/test_cognitive_substrate_reasoning_graph.py` (9 integration, 29 total)
> Skill: amos-cognitive-substrate-reasoning-graph
> See also: 2026-08-22 Cognitive Substrate Reality Gate · amos-core-reasoning · amos-competing-hypotheses

## 1. The problem this solves

Reasoning is no longer "what the LLM says between goal and answer." It becomes an
**executable operation graph** where every transition is typed, legality-checked,
and persisted. When the final answer is wrong, the system can trace back to the
**earliest load-bearing wrong transition** — not merely blame the last output that
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
Multiple uncertainty sources compound nonlinearly: `u_total = 1 - (1 - min(u_i))^n`.

## 7. Cross-slice integration

- Uses `CognitiveObject` from slice 1 (Reality Gate).
- Reality-gate-admitted nodes are trusted reasoning inputs.
- Quarantined nodes, if injected, trigger legality failures — the two slices
  compose to prevent both `Generate → Memory` and `Retrieve → Truth`.

## 8. Sequencing

| Slice | Status | Tests |
|-------|--------|-------|
|| 1. RC/IR reality gate | DONE | 26 |
|| 2. Reasoning execution graph (this) | DONE | 29 |
|| 3. Memory operation graph `M_t` | DONE | 38 |
||| 4. Interface coupling | DONE | 146 (unified substrate `AMOS_COGNITIVE_SUBSTRATE.py` self-test now covers all 4 slices) |

## 9. Governance record

- Mutation class: M2 (high-consequence decision architecture).
- Authority: explicit user authorization (repo architect).
- Rollback: delete the 5 artifacts listed in the workflow file.
- Reversible: yes — additive only; no existing brain module was modified.

---
**Links:** [[DATED_MOC]] | [[KNOWLEDGE_MOC]]
