---
title: Vault Domain Knowledge — Arxiv Grapheval Reasoning Coherence Rscf
type: reference
source: 07_SKILLS/arxiv-grapheval-reasoning-coherence-rscf/references
tags:
- reference
- arxiv-grapheval-reasoning-coherence-rscf
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
> Extracted from skill: `arxiv-grapheval-reasoning-coherence-rscf`

## Vault-Sourced Content

### Source 1: AMOS_Multi_Perspective_Reasoning_Kernel_v0_Meta_Cognition4_2

> Path: `kernel/A/AMOS_Multi_Perspective_Reasoning_Kernel_v0_Meta_Cognition4_2.md` | Size: 7205 chars | Match score: 10

{
  "kernel_id": "Multi_Perspective_Reasoning_Kernel",
  "version": "1.0.0",
  "source": "md/Core/AMOS_Multi_Perspective_Reasoning_Kernel_v0.md (category: meta_cognition, from AMOS_Omni_KERNEL.json)",
  "description": "Kernel for multi-perspective reasoning — holding, comparing, and integrating multiple viewpoints on the same subject, detecting bias through perspective gaps, and synthesising coherent conclusions from competing interpretations.",
  "group": "Kernels.Meta_Cognition",
  "category": "Meta_Cognition",
  "priority": 9,
  "required": true,
  "domains": ["multi_perspective", "viewpoint", "bias_detection", "perspective-taking", "integration", "competing_interpretations"],
  "depends_on": ["Meta_Logic_Kernel", "Meta_Epistemology_Kernel", "Counterfactual_Reasoning_Kernel", "Psychology_Decision_Kernel"],
  "meta": {
    "role": "Multi-Perspective Reasoning Kernel",
    "creator": "Trang Phan (Origin Architect)",
    "status": "defined",
    "binding_rules": ["Law_of_Law", "Rule_of_2", "Rule_of_4", "Absolute_Integrity"],
    "omni_category": "meta_cognition",
    "position": 7
  },
  "purpose": "Enable reasoning that holds multiple perspectives simultaneously, compares them structurally, detects where perspectives diverge and why, and integrates them into conclusions that respect the tensions rather than collapsing them.",
  "perspective_dimensions": {
    "agent_perspective": "How different agents (humans, organisations, systems) view the same situation based on their position, incentives, knowledge, and values",
    "disciplinary_perspective": "How different domains of knowledge (biology, economics, psychology, engineering, law) frame the same phenomenon",
    "temporal_perspective": "How the same situation looks from short-term vs medium-term vs long-term time horizons",
    "scale_perspective": "How the same situation looks at micro vs meso vs macro scale; what's visible at each level",
    "value_perspective": "How different values and ethical frameworks evaluate the same situation or decision"
  },
  "perspective_holding_procedure": {
    "step_1": "Identify the subject or question being reasoned about",
    "step_2": "Identify relevant perspectives (which agents, disciplines, time horizons, scales, values are relevant?)",
    "step_3": "For each perspective, construct the most charitable version: what would a competent holder of that perspective say?",
    "step_4": "Map where perspectives agree (overlap) and where they diverge (tension points)",
    "step_5": "For each tension point, identify the source of divergence: different facts? different values? different time horizons? different scale? different incentives?",
    "step_6": "Check whether any perspective is being under-represented or straw-manned",
    "step_7": "Synthesize: what can be concluded that respects the divergences? What remains genuinely contested?"
  },
  "tension_types": {
    "factual_tension": "Perspectives disagree on what is the case; resolution requires evide

---

### Source 2: AMOS_Counterfactual_Reasoning_Kernel_v0_Meta_Cognition4_2

> Path: `kernel/A/AMOS_Counterfactual_Reasoning_Kernel_v0_Meta_Cognition4_2.md` | Size: 6550 chars | Match score: 10

{
  "kernel_id": "Counterfactual_Reasoning_Kernel",
  "version": "1.0.0",
  "source": "md/Core/AMOS_Counterfactual_Reasoning_Kernel_v0.md (category: meta_cognition, from AMOS_Omni_KERNEL.json)",
  "description": "Kernel for counterfactual reasoning — what-if analysis, alternative scenario reasoning, reasoning about events that did not happen, and causal inference through comparison of actual vs hypothetical states.",
  "group": "Kernels.Meta_Cognition",
  "category": "Meta_Cognition",
  "priority": 9,
  "required": true,
  "domains": ["counterfactual", "what_if", "alternative_scenarios", "causal_inference", "hypothetical_reasoning", "scenario_analysis"],
  "depends_on": ["Meta_Logic_Kernel", "Meta_Epistemology_Kernel", "Probability_Statistics_Kernel"],
  "meta": {
    "role": "Counterfactual Reasoning Kernel",
    "creator": "Trang Phan (Origin Architect)",
    "status": "defined",
    "binding_rules": ["Law_of_Law", "Rule_of_2", "Rule_of_4", "Absolute_Integrity"],
    "omni_category": "meta_cognition",
    "position": 6
  },
  "purpose": "Enable reasoning about alternative scenarios — what would have happened if X had been different, what could happen if Y changes, and what causal relationships can be inferred by comparing actual outcomes with hypothetical alternatives.",
  "counterfactual_types": {
    "past_counterfactual": "What would have happened if something in the past had been different? (e.g., 'If we had launched earlier...')",
    "future_counterfactual": "What would happen if something changes in the future? (e.g., 'If we increase price by 10%...')",
    "structural_counterfactual": "What does the structure imply would happen under different conditions? (e.g., 'Given this system design, if load doubles...')",
    "causal_counterfactual": "What can we infer about causation by comparing what happened with what would have happened without the cause?"
  },
  "valid_counterfactual_criteria": {
    "plausible_initial_state": "The counterfactual starting point must be plausible or clearly flagged as implausible",
    "minimal_change_principle": "Change only what's necessary for the counterfactual; don't silently change other things",
    "causal_chain_conservation": "Respect the causal structure: if A causes B causes C, changing A propagates through B to C",
    "uncertainty_proportionate": "The further from actuality, the larger the uncertainty. Near-counterfactuals are more reliable than far ones.",
    "assumption_transparency": "All assumptions about how the world would differ must be explicit"
  },
  "common_errors": {
    "over_determination": "Assuming the counterfactual outcome would definitely be X without considering other influencing factors",
    "ignoring_system_reactions": "Treating the system as static when it would react to the change",
    "confusing_correlation_with_causation": "Assuming that because B followed A, changing A would change B",
    "unrealistic_baseline": "Comparing against an unrealistic or cherry-picked base

---

### Source 3: Reasoning kernel

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
**MOC:** references_MOC

## Related

- [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
---

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · references_MOC · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: arxiv-grapheval-reasoning-coherence-rscf-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/arxiv-grapheval-reasoning-coherence-rscf/references/vault_domain_knowledge.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
