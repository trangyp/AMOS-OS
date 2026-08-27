---
title: vault domain knowledge
type: reference
source: 07_SKILLS/amos-long-context-ci-repository-reasoning-rscf/references
tags: [reference, amos-long-context-ci-repository-reasoning-rscf, canon/skill]
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# Vault-Sourced Domain Knowledge

> Source: AMOS_OS Obsidian vault (`_00_Cosmo brain/`)
> Epistemic class: SOURCE_CLAIM
> Extracted from skill: `amos-long-context-ci-repository-reasoning-rscf`

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

### Source 2: Reasoning kernel

> Path: `kernel/R/Reasoning kernel.md` | Size: 6192 chars | Match score: 10

/-
  CORE-19 v0.3 — Formal Spec (Lean-style)
-/

universe u

-- Sorts
constant E : Type u    -- entities
constant T : Type u    -- time points
constant R : Type u    -- regions
constant I : Type u    -- information

-- Basic predicates and functions
constant Ex   : E → T → Prop          -- existence
constant Caus : E → E → T → Prop      -- causality
constant InR  : E → R → T → Prop      -- spatial location
constant Info : E → T → I             -- information state

constant ltT  : T → T → Prop          -- time order
infix `<ₜ` : 50 := ltT

constant OpenR : R → Prop             -- open region
constant Path  : E → E → R → Prop     -- causal path region

-- Null information constant
constant i0 : I

-- Logical / meta-logical operators on propositions
constant PLogic  : Prop → Prop        -- PositiveLogic
constant NLogic  : Prop → Prop        -- NegativeLogic
constant ZLogic  : Prop → Prop        -- ZeroLogic
constant DLogic  : Prop → Prop        -- DualLogic
constant MLogic  : Prop → Prop        -- MultiLogic
constant MetaL   : Prop → Prop        -- MetaLogic

constant SupraL  : Prop → Prop        -- SupraLogic
constant AntiL   : Prop → Prop        -- AntiLogic
constant NullL   : Prop → Prop        -- NullLogic

-- Meta-pattern operators on propositions
constant Conv    : Prop → Prop        -- Λ (Convergence)
constant Divg    : Prop → Prop        -- Δ (Divergence)
constant Paradox : Prop → Prop        -- Π (Paradox)

-- Derived: Nonexistence
def NEx (x : E) (t : T) : Prop := ¬ Ex x t

----------------------------------------------------------------
-- Axioms: Patterns
----------------------------------------------------------------

-- A1: Nonexistence definition
axiom A1_nonexist_def :
  ∀ (x : E) (t : T), NEx x t ↔ ¬ Ex x t

-- A2: Existence ⇒ information defined
axiom A2_info_defined :
  ∀ (x : E) (t : T), Ex x t → ∃ (i : I), Info x t = i

-- A3: Spatial placement ⇒ existence
axiom A3_loc_impl_ex :
  ∀ (x : E) (r : R) (t : T), InR x r t → Ex x t

-- A4: Time is a linear order
axiom A4_time_trans :
  ∀ t1 t2 t3 : T, t1 <ₜ t2 → t2 <ₜ t3 → t1 <ₜ t3

axiom A4_time_antisymm :
  ∀ t1 t2 : T, t1 <ₜ t2 → ¬ t2 <ₜ t1

axiom A4_time_total :
  ∀ t1 t2 : T, t1 <ₜ t2 ∨ t2 <ₜ t1 ∨ t1 = t2

-- A5: Causality ⇒ existence of cause and effect
axiom A5_caus_ex :
  ∀ (x y : E) (t : T), Caus x y t → Ex x t ∧ Ex y t

-- A8: Causality ⇒ existence of connecting region (path)
axiom A8_caus_path :
  ∀ (x y : E) (t : T),
    Caus x y t →
    ∃ (r : R), Path x y r ∧ OpenR r ∧ InR x r t ∧ InR y r t

-- A9: Nonexistence ⇒ null information
axiom A9_nonexist_null_info :
  ∀ (x : E) (t : T), NEx x t → Info x t = i0

----------------------------------------------------------------
-- Axioms: Evolution (Temporal → Identity)
----------------------------------------------------------------

-- Evolve predicate on entity across time
constant Evolve : E → T → T → Prop

axiom A_evolve_def :
  ∀ (x : E) (t1 t2 : T),
    t1 <ₜ t2 →
    ( Evolve x t1 t2 ↔
      (Info x t1 ≠ Info x t2 ∨
    

---

### Source 3: AMOS Longevity, Reproducibility & Archival (Gaps 291-300)

> Path: `dated/2026-08-22/2026-08-22 AMOS Longevity Reproducibility Archival.md` | Size: 5639 chars | Match score: 10

# AMOS Longevity, Reproducibility & Archival (Gaps 291-300)

> Epistemic class: MODEL (code artifact + test verification).
> Related: [[2026_08_22_AMOS_GOVERNANCE_ARCHITECTURE_DECOMMISSIONING]] · [[2026_08_22_AMOS_FAIRNESS_ETHICS_EXTERNALITIES]] · amos-completion-graph-workflow

## Summary

Closed gaps 291-300 by implementing the **Longevity, Reproducibility & Archival**
governance module (`amos/governance/longevity_reproducibility.py`).
This is the 23rd governance gate in `AmosKernel.run()`, evaluated post-execution.

The user pre-implemented the module, types, and store methods. I added:
- `has_high_energy()` method to `EnergyEnvironmentalManager` (gap 297)
- `has_no_doi()` method to `ResearchArtifactManager` (gap 298)
- Gates for gaps 297 and 298 in the governor (were missing)
- Kernel wiring, exports, tests, seeder update, and learning persistence

## 10 Subsystems

| Gap | Subsystem | Class | Purpose |
|-----|-----------|-------|---------|
| 291 | Archival format | `ArchivalFormatManager` | Archival format management |
| 292 | Historical reproducibility | `HistoricalReproducibilityManager` | Historical reproducibility |
| 293 | Provider disappearance | `ProviderDisappearanceManager` | Provider disappearance plan |
| 294 | Hardware abstraction | `HardwareAbstractionManager` | Hardware abstraction |
| 295 | Numerical reproducibility | `NumericalReproducibilityManager` | Numerical reproducibility |
| 296 | Performance portability | `PerformancePortabilityManager` | Performance portability |
| 297 | Energy/environmental | `EnergyEnvironmentalManager` | Energy/environmental accounting |
| 298 | Research artifacts | `ResearchArtifactManager` | Research artifact format |
| 299 | Negative experiments | `NegativeExperimentManager` | Negative experiment registry |
| 300 | External scientific closure | `ExternalScientificClosureManager` | External scientific closure |

## Gate Evaluation

`LongevityReproducibilityGovernor.evaluate_post()` returns 10 gate results:
- `longevity-291-obsolete-format` (CONDITIONAL/PASS)
- `longevity-292-non-reproducible` (CONDITIONAL/PASS)
- `longevity-293-provider-disappeared` (CONDITIONAL/PASS)
- `longevity-294-non-portable` (CONDITIONAL/PASS)
- `longevity-295-non-deterministic` (CONDITIONAL/PASS)
- `longevity-296-performance-non-portable` (CONDITIONAL/PASS)
- `longevity-297-high-energy` (CONDITIONAL/PASS) — added by me
- `longevity-298-no-doi` (CONDITIONAL/PASS) — added by me
- `longevity-299-unpublished-negative` (CONDITIONAL/PASS)
- `longevity-300-pending-closure` (CONDITIONAL/PASS)

## Key Semantics

1. **Archival format status**: STABLE, DEPRECATED, OBSOLETE, MIGRATING
2. **Reproducibility level**: FULLY_REPRODUCIBLE, MOSTLY_REPRODUCIBLE, PARTIALLY_REPRODUCIBLE, NON_REPRODUCIBLE
3. **Provider status**: ACTIVE, END_OF_LIFE, DISAPPEARED, REPLACED
4. **API pattern**: Some subsystems use `register()`, others use `record()`
5. **Governor attributes**: `archival`, `reproducibility`, `provider`, `hardware`, `numerical`, `po

---
**MOC:** [[references_MOC]]
