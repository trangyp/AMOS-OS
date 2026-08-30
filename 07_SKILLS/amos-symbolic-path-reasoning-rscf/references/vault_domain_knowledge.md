---
title: Vault Domain Knowledge — Amos Symbolic Path Reasoning Rscf
type: reference
source: 07_SKILLS/amos-symbolic-path-reasoning-rscf/references
tags:
- reference
- amos-symbolic-path-reasoning-rscf
- type/skill
- law-hierarchy
- 2026-08-22-cognitive-substrate-reality-gate
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
> Extracted from skill: `amos-symbolic-path-reasoning-rscf`

## Vault-Sourced Content

### Source 1: Reasoning kernel

> Path: `kernel/R/Reasoning kernel.md` | Size: 6192 chars | Match score: 15

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

### Source 2: Cognitive Substrate Reasoning Execution Graph

> Path: `dated/2026-08-22/2026-08-22 Cognitive Substrate Reasoning Graph.md` | Size: 4567 chars | Match score: 10

# Cognitive Substrate Reasoning Execution Graph

> Slice 2 of the AMOS Cognitive Substrate Layer. Implements the reasoning side of
> `R_t = (N_t, E_t, O_t, Pi_t, U_t)` with typed inference operators, transition
> legality, earliest-failure attribution, minimal causal cut-set, and counterfactual
> repair replay.
>
> Source: `cosmo-brain/AMOS_COGNITIVE_SUBSTRATE_REASONING_GRAPH.py` (20 self-tests)
> Test: `cosmo-brain/test_cognitive_substrate_reasoning_graph.py` (9 integration, 29 total)
> Skill: amos-cognitive-substrate-reasoning-graph
> See also: 2026_08_22_COGNITIVE_SUBSTRATE_REALITY_GATE · amos-core-reasoning · amos-competing-hypotheses

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

### Source 3: 2026-08-23 COSMO Critical Path Pages Converted

> Path: `dated/2026-08-23/2026-08-23 COSMO Critical Path Pages Converted.md` | Size: 2952 chars | Match score: 10

# 2026-08-23 COSMO Critical Path Pages Converted

## Summary

Converted 6 critical-path web pages from static mockups to functional implementations with real data fetching, state management, and database persistence.

## Pages Converted

### 1. Artwork Reveal 1 (`apps/web/src/app/artwork-reveal-1/page.tsx`)
- Fetches artwork from `resonance_artworks` table using session ID
- Displays actual generated image from Supabase storage
- Shows loading state while fetching
- Fallback to placeholder when no artwork exists

### 2. Artwork Reveal 2 (`apps/web/src/app/artwork-reveal-2/page.tsx`)
- Full-page artwork reveal experience
- Fetches artwork by session or latest for user
- Displays artwork version and palette
- Dynamic image from Supabase storage

### 3. Artwork Explanation (`apps/web/src/app/artwork-explanation/page.tsx`)
- Fetches latest artwork with features (flow, variation, energy, continuity, texture)
- Displays real percentages in progress bars
- Shows technical details (duration, version, palette, seed)
- Uses real session data for duration

### 4. Post-Practice Reflection (`apps/web/src/app/post-practice-reflection/page.tsx`)
- Full state management for feelings, body shifts, gratitude notes
- Saves reflections to `session_reflections` table
- Interactive selection with visual feedback
- Would-return preference with binary choice

### 5. Account Settings (`apps/web/src/app/account-settings/page.tsx`)
- Fetches user profile data
- Editable display name
- Saves to `profiles` table
- Uses real user initials in avatar

### 6. User Profile (`apps/web/src/app/user-profile/page.tsx`)
- Displays real user name and bio
- Shows total scans and artworks from hooks
- Member since date from user creation
- Dynamic stats from journey and gallery

## Also Updated (Mobile)

### Tabs Index (`apps/mobile/src/app/(tabs)/index.tsx`)
- Replaced hardcoded mock data with real hooks
- Dynamic greeting based on time of day
- Real user name from auth
- Gallery grid from real artworks
- Stats from journey and practices

## Core Loop Status

The core transformation loop is now fully functional:
1. Scan → scan-type-selection-1 → scan-preparation-1 → microphone-permission
2. Record → resonance-recording-1 → recording-review
3. Process → process-audio edge function → artwork generation
4. Reveal → artwork-reveal-1/2 → artwork-explanation
5. Reflect → post-practice-reflection → save to database
6. Review → journey timeline → gallery

## Remaining Work

- 147 web pages still have mockup-container class (secondary features)
- Build fails due to pre-existing monorepo package linking issues
- Community, marketplace, and advanced features still mocked

## Vault Links

- [[11_KNOWLEDGE/COSMO_BRAIN_MOC|COSMO_BRAIN_MOC]]
- cosmo-obsidian-memory

---
**MOC:** references_MOC
---

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · references_MOC · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-symbolic-path-reasoning-rscf-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/amos-symbolic-path-reasoning-rscf/references/vault_domain_knowledge.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
