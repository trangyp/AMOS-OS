---
title: 2026 08 22 COGNITIVE SUBSTRATE REALITY GATE
type: cognitive
origin_architect: Trang Phan
provenance: cosmo-brain/AMOS_COGNITIVE_SUBSTRATE_REALITY_GATE.py
confidence: 0.9
epistemic_class: DERIVED
conclusion_label: "VERIFIED"
tags: [canon-group/tech-ai, cosmo-brain, cognitive-substrate, reality-contact, epistemic-autopoisoning, rscf/claim, rscf/provenance, rscf/state/observation, topic/2026-08-22-cognitive-substrate-reality-gate, dated, dated/2026-08-22]
date: 2026-08-22
---



# Cognitive Substrate Reality Gate

> First executable slice of the AMOS Cognitive Substrate Layer (gaps 701–900).
> Prevents epistemic autopoisoning by requiring reality contact before any
> LLM-generated claim is promoted to durable memory.
>
> Source: `cosmo-brain/AMOS_COGNITIVE_SUBSTRATE_REALITY_GATE.py` (17 self-tests)
> Test: `cosmo-brain/test_cognitive_substrate_reality_gate.py` (9 integration, 26 total)
> Skill: amos-cognitive-substrate-reality-gate
> See also: [[00_COSMO_BRAIN_MOC]] · 2026-08-22 AMOS Obsidian Memory Bridge · amos-provenance-trust · amos-core-reasoning

## 1. The problem this solves

The deepest failure mode in long-horizon AMOS cognition is **epistemic autopoisoning**:

```
LLM generates X -> X stored -> X retrieved -> X treated as evidence -> X strengthened -> X stored again
```

Confidence rises with **no new reality contact**. The system becomes internally coherent
and externally wrong. Ordinary hallucination detection cannot catch this because the
output is self-consistent.

## 2. The gate

```
Promote(X)  =>  RC(X) >= theta_RC  AND  IR(X) <= theta_IR
```

- `RC(X)` — number/quality of **independent external** observations supporting X.
- `IR(X)` — fraction of support ultimately descending from **AMOS-generated** state.

Default thresholds: `theta_RC = 1.0`, `theta_IR = 0.5`. Raise both for high-stakes claims.

## 3. Memory I/O pipelines

Write path (forbids `Generate -> Memory`):
```
Propose -> Type -> CheckEvidence -> CheckScope -> CheckProvenance -> Admit
```

Read path (forbids `Retrieve -> Truth`):
```
Retrieve -> Validate -> Contextualize -> Use
```

Failure at any stage **quarantines** the object; provenance is retained, nothing is
silently deleted.

## 4. Key invariants enforced

- Claim strength must not exceed evidence strength (high confidence does not bypass the gate).
- Repetition does not establish source independence (non-independent contacts are not double-counted).
- Short internal-recursion paths raise IR and tighten the gate.
- Counterfactual repair: a quarantined object is rescued only by adding an independent
  external contact and re-running `promote()` — the substrate-level analogue of
  "earliest causal failure correction."

## 5. Formalization (AMOS MODEL, not a source theorem)

Reasoning state: `R_t = (N_t, E_t, O_t, Π_t, U_t)` — cognitive objects, bindings,
operations, reasoning policy, localized uncertainty.

Memory state: `M_t = (V_t, E_t, O_t, I_t, Q_t, L_t)` — memory-object graph, edges,
operation history, indexes, quarantine/trust, lifecycle.

This gate is the **interface integrity** component of:

```
CognitiveIntegrity = ReasoningIntegrity ∧ MemoryIntegrity ∧ InterfaceIntegrity ∧ RealityContact
```

## 6. Sequencing (this is slice 1 of the substrate; now consolidated in unified substrate)

|| Slice | Status | Notes |
|-------|--------|-------|
| RC/IR reality gate (this) | DONE | 26 tests pass |
| Reasoning execution graph `R_t` | DONE | 29 tests pass; see `2026-08-22 Cognitive Substrate Reasoning Graph` |
| Memory operation graph `M_t` | DONE | 38 tests pass; see `2026-08-22 Cognitive Substrate Memory Graph` |
| Interface coupling | DONE | Unified in `AMOS_COGNITIVE_SUBSTRATE.py` (4298 lines, 146 self-tests); see `AMOS_Cognitive_Substrate_v2_Implementation_Notes` |

All 4 slices are now consolidated in the single unified module `cosmo-brain/AMOS_COGNITIVE_SUBSTRATE.py`. The original slice modules remain as provenance references and independent self-test suites.

## 7. Governance record

- Mutation class: M2 (high-consequence decision architecture — changes how truth/reality is evaluated).
- Burden: `log2(3+1) + 2*0.4 + 2*0.2 = 3.2` (exceeds autonomous envelope depth<=2, consequence<=0.35).
- Authority: explicit user authorization (repo architect), recorded here per `amos-governed-evolution`.
- Rollback path: delete the Python module, test file, skill directory, this note, and the MOC wikilink.
- Reversible: yes — all artifacts are additive; no existing brain module was modified.

---
**MOC:** [[DATED_MOC]]
