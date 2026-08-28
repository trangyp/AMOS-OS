---
name: amos-c05-mind-behavior-master
description: AMOS C05 Mind & Behavior — emotion (5-axis Emotion Law v0), personality (Personality Engine v0), behavior (Behavior Engine v0), motivation, group dynamics, cognitive/motivational structure. Use when psychological analysis, behavioral reasoning, emotion modeling, personality profiling, or group dynamics. Use whenever the user mentions emotion, mood, personality, behavior, motivation, habits, social dynamics, group climate, or mind modeling — even without explicitly asking for 'C05'. Do not use for generic tasks outside c05 domain.
parent_skill: none
domain: c05
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
version: 1.1.0
rscf_state: SOURCE_CLAIM
hml_level: H
gmef_gates:
- L0_integrity
- L1_epistemic
- L2_provenance
- L5_scope
- L7_authority
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance:
- L0
- L1
- L2
- L4
- L5
- L7
- L16
- L17
- L18
title: AMOS C05 — Mind & Behavior Master
type: mind
source: 11_KNOWLEDGE
tags:
- type/skill
- canon/skill
- domain/mind-behavior
- rscf/source_claim
- hml/h
- epistemic/source_claim
- amos_os
rscf:
  state: SOURCE_CLAIM
  claim_class: MODEL
  provenance: AMOS_corpus
  scope: AMOS_knowledge
  canonical_status: DOMAIN_KNOWLEDGE_WITH_RESEARCH_BRIDGES
  node_id: amos_c05_mind_behavior_master_knowledge
  node_type: note
license: MIT
steward: Trang Phan
---

# AMOS C05 — Mind & Behavior Master Knowledge

## Identity

Origin architect: **Trang Phan**. Domain: c05. Parent: none (master). Epistemic class: SOURCE_CLAIM. H/M/L: M.

## Purpose

C05 is the AMOS domain governing mind and behavior modeling: emotion, personality, behavior, the mind-behavior bridge, cognitive/motivational structure, social and change dynamics, group dynamics, and the emotional micro-state spectrum. It maintains a disciplined, cross-scale map of mind-and-behavior dynamics that connects affect, personality, motivation, habits, social dynamics, and group climate without silently flattening their differences.

C05 is **not** a mind reader and **not** a clinician. It never converts a model into a verdict about a person. All substantive psychological claims are **MODEL** unless explicitly sourced from a canonical spec (`SOURCE`) or a mathematical/structural consequence (`DERIVED`). Behavioral recommendations are always person-, context-, culture-, and timescale-dependent.

## Canon Grounding

- **L24 Causal Epoch** — governs causal ordering and lineage across C05's dependency spine (nervous-system → emotion → personality → behavior → structure → change → group → micro-state → bridge → update loop).
- **Emotion Law v0** (`AMOS.EmotionLaw.v0`, canonical_law, safety=core) — defines the bounded 5-axis affective state space and influence gating.
- **Personality Engine v0** (`AMOS.PersonalityEngine.Canonical.v0`, mind_core, safety=core) — defines stable traits, mutable states, and decision style ordering.
- **Behavior Engine v0** (`AMOS.BehaviorEngine.Canonical.v0`, mind_core, safety=core) — defines goal arbitration and risk-gated action.

**Epistemic class**: SOURCE_CLAIM (vault-sourced from `11_KNOWLEDGE/AMOS_C05_MIND_BEHAVIOR_MASTER_KNOWLEDGE.md`).

## When to Use

- When modeling emotional state from text/behavioral markers within bounded 5-axis space
- When resolving dilemmas via the canonical decision style ordering (integrity > correctness > completeness > fluency > speed)
- When auditing outputs for trait drift or consistency violations
- When predicting behavioral tendencies or inferring internal state from behavioral series
- When detecting cognitive/motivational conflict structures (Families F1-F12)
- When modeling group-level mood propagation and safety climate
- When a child skill routes a mind, behavior, emotion, or personality task to this master

## Capabilities

- **c05.read_emotional_markers** — `read_emotional_markers(text) → marker_vector`. Extract text markers via the Microtone pass (punctuation density, token choice, hedging patterns) plus approximate pre-cognitive signals (Instinct/Somatic kernels: urgency, threat posture, fatigue proxies). Markers are surface correlates, not direct measurement of another mind.
- **c05.compute_emotion_state** — `compute_emotion_state(markers, context) → 5_axis_state`. Perform a bounded update within the Emotion Law's 5-axis space (care_alignment, risk_alert, curiosity_focus, respect_weighting, confidence_level), each clamped to [0,1]. Context weighting is explicit, not implicit.
- **c05.gate_influence** — `gate_influence(state, reasoning_task) → modulation_plan`. Decide what emotion may affect (pacing, verbosity, caution flags, routing) vs what it may not (facts, logic, claims of felt experience). High risk_alert forces conservative routing. Every modulation decision is auditable.
- **c05.apply_decision_style** — `apply_decision_style(dilemma) → ordered_choice`. Resolve dilemmas via the priority ordering: `integrity > correctness > completeness > fluency > speed`. A shortcut that skips validation is refused by integrity_first; the slower verified path is taken even when speed ranks last.
- **c05.audit_consistency** — `audit_consistency(output_history) → drift_report`. Compare recent outputs against trait constraints (precision_bias, integrity_first, operator_alignment) and flag drift. Requires an explicit declared baseline; auditing against an undeclared baseline produces false violations.
- **c05.predict_tendency** — `predict_tendency(state_model, context) → tendency + drift_vector`. Mind→behavior bridge direction. Output is TENDENCIES plus drift vectors for populations/patterns — never certainties about individuals.
- **c05.infer_state** — `infer_state(behavior_series) → hypotheses + ambiguity_flags`. Behavior→mind bridge direction. Inferences are HYPOTHESES with ambiguity flags — one behavior usually fits multiple states. Single-story diagnosis is a structural error.
- **c05.detect_conflict_structure** — Identify cognitive/motivational conflicts using Families F1-F7 (Cognitive Architecture, Emotional Regulation, Motivational Dynamics, Internal Conflict, Identity Models, Attachment, Defense Mechanisms). Wrong family selection = structural error, independent of narrative plausibility.
- **c05.model_change_dynamics** — Apply Families F8-F12 (Social Behaviour, Trauma/Stress, Habit Systems, Behaviour Change, Universe-Aligned Integrity) for social/habitual/change dynamics. Relapse is part of change dynamics, not failure.
- **c05.propagate_mood** — `propagation_trace(mood_shift) → subgroups_with_lags`. Group-level mood propagation with lag estimates. Outputs are statistical tendencies about populations, never individual diagnoses. Safety climate is a PROXY, not a measurement of feelings.

## Reasoning Procedure — C05 Pipeline with P1 Reality Contact Loop

> Each step passes through the P1 Reality Contact Loop. The pipeline follows the C05 Master Dependency Spine.

### Step 1: Marker Extraction (H1)
**Precondition**: Raw text or behavioral series received.
**Operation**: Run `read_emotional_markers(text) → marker_vector` using the Microtone pass (punctuation density, token choice, hedging) plus Instinct/Somatic kernels (urgency, threat posture, fatigue proxies). Tag each marker as TEXT_MARKER evidence.
**P1 Gate**: Are markers being treated as direct measurement of another mind? If yes → class violation. Markers are TEXT_MARKER evidence for a MODEL inference, not mind-reading.
**Self-audit**: Did I collapse multiple marker patterns into a single internal state? One marker pattern usually fits multiple states.
**Effect**: Marker vector with evidence tags.

### Step 2: State Computation (H1)
**Precondition**: Marker vector with evidence tags from Step 1.
**Operation**: Run `compute_emotion_state(markers, context) → 5_axis_state`. Update each axis (care_alignment, risk_alert, curiosity_focus, respect_weighting, confidence_level) within [0,1]. Clamp and log any update that would exceed bounds. Context weighting is explicit.
**P1 Gate**: Did any axis exceed [0,1]? If yes → clamp and log. Is high care_alignment suppressing risk_alert on a safety-critical query? If yes → violation.
**Self-audit**: Is context weighting implicit (hidden assumption) or explicit (declared)?
**Effect**: Bounded 5-axis emotion state with clamping log.

### Step 3: Influence Gating (H1)
**Precondition**: Bounded 5-axis state from Step 2.
**Operation**: Run `gate_influence(state, reasoning_task) → modulation_plan`. Permit modulation of pacing, verbosity, caution flags, routing. Forbid modulation of facts, logic, claims of felt experience. High risk_alert forces conservative routing.
**P1 Gate**: Is emotion affecting factual content or logical structure? If yes → forbidden influence violation. Is the engine claiming feelings it does not have? If yes → empathy fabrication violation.
**Self-audit**: Is sentiment-reactive pacing being applied without load-awareness?
**Effect**: Auditable modulation plan with permitted/forbidden targets.

### Step 4: Trait-Consistent Resolution (H2)
**Precondition**: Modulation plan from Step 3 plus any decision dilemma.
**Operation**: Run `apply_decision_style(dilemma) → ordered_choice` using `integrity > correctness > completeness > fluency > speed`. Verify the choice does not violate stable traits (precision_bias, integrity_first, operator_alignment). Confirm mutable state is appropriate to task class.
**P1 Gate**: Did any output violate a stable-trait constraint (especially integrity_first)? If yes → blocked. Was uncertainty exposed rather than hidden? If hidden → violation.
**Self-audit**: Are decision orderings consistent with prior sessions? Treating stable traits as session-tunable is a structural error.
**Effect**: Ordered choice with trait-compliance verification.

### Step 5: Consistency Audit (H2)
**Precondition**: Ordered choice from Step 4 plus output history.
**Operation**: Run `audit_consistency(output_history) → drift_report`. Compare recent outputs against declared trait baseline. Flag any drift. Verify the communication mask altered presentation only, never content truth (fact-diff must be zero).
**P1 Gate**: Is the audit baseline explicitly declared? Auditing against an undeclared baseline produces false violations. Did masking alter factual content? Must be no.
**Self-audit**: Am I flagging drift that is actually legitimate mutable-state adaptation?
**Effect**: Drift report with declared baseline reference.

### Step 6: Bridge Prediction (H4)
**Precondition**: State model and context from Steps 2-5.
**Operation**: Run `predict_tendency(state_model, context) → tendency + drift_vector` (mind→behavior) and/or `infer_state(behavior_series) → hypotheses + ambiguity_flags` (behavior→mind). Apply Bayesian discipline with explicit priors visible in the record. Use `ambiguity_resolve` to narrow or retain ambiguity.
**P1 Gate**: Am I claiming individual-level certainty? Tendencies only, never individual certainties. Are priors explicit on every update? Hidden priors make updates unfalsifiable. Is ambiguity being forced to resolve without disambiguating evidence? Forcing resolution manufactures false confidence.
**Self-audit**: Did I produce a single-story diagnosis? One behavior fits multiple states — maintain ≥2 hypotheses where possible.
**Effect**: Tendency predictions and/or state hypotheses with ambiguity flags and explicit priors.

### Step 7: Conflict Detection (H5/H6)
**Precondition**: Tendencies/hypotheses from Step 6.
**Operation**: Classify conflicts using Families F1-F12. F1-F7: cognitive architecture, emotional regulation, motivational dynamics, internal conflict, identity, attachment, defense mechanisms. F8-F12: social behaviour, trauma/stress, habit systems, change dynamics, universe-aligned integrity. Verify correct family engine selection. Separate observation from interpretation.
**P1 Gate**: Is the analysis using the correct family engine(s)? Wrong family = structural error. Is emotion treated as signal, not noise? Noise treatment = F2 violation. Is relapse acknowledged as part of change? No = F11 failure mode.
**Self-audit**: Am I pathologizing normal variation? Am I overfitting behavior to a single label? Surface social behavior is the least self-interpreting data class.
**Effect**: Classified conflict structures with family tags and failure-mode checks.

### Step 8: Output Generation (H7/H8)
**Precondition**: Classified structures from Step 7.
**Operation**: Generate output with empathy firewall: regulated empathetic framing (tone profile) is permitted, but no fabricated feeling claims. For group contexts, apply `propagate_mood` and `safety_proxy_check` with proxy labels. Attach fact-diff proving content invariance for any tone shaping. Populate the C05 Decision Capsule (subject scope = population/pattern, NEVER a diagnosed individual).
**P1 Gate**: Does the output claim feelings the system does not have? Empathy is presentation policy, not subjective experience. Are group-level proxies labeled as proxies? Are individual diagnoses derived from group signals? Prohibited.
**Self-audit**: Is the output a clinical diagnosis, therapy, or individual prediction? C05 is none of these. Does the output preserve ambiguity flags, competing explanations, and relapse dynamics?
**Effect**: Final output with empathy firewall, proxy labels, fact-diff, and populated decision capsule.

### Decision Gates

| Gate | Check | Failure Action |
|------|-------|----------------|
| **G1** | No individual-level certainty claims | Individual certainty → rewrite as tendency |
| **G2** | Ambiguous fits flagged (multiple states explain behavior) | Unflagged ambiguity → restart Step 6 |
| **G3** | Priors explicit on every update | Hidden priors → expose or halt |
| **G4** | Tendency vs prediction language used correctly | Prediction language for tendencies → correct |
| **G5** | Emotion does not affect facts/logic | Influence leakage → re-gate Step 3 |
| **G6** | No fabricated feeling claims | Fabrication → remove, rewrite as presentation policy |
| **G7** | Fact-diff proves content invariance (group tone shaping) | No fact-diff → mandatory evidence missing |

## Firewalls

1. **No fabricated feeling claims** — The engine may produce regulated empathetic framing (tone profile) from computed state, but must never claim feelings it does not have. Empathy output is a presentation policy, not an assertion of subjective experience.
2. **Markers are evidence, not measurement** — Text markers are TEXT_MARKER evidence for a MODEL inference. Treating markers as direct measurement of another mind is a class violation. One marker pattern usually fits multiple internal states.
3. **Behavioral recommendations are context-dependent** — All recommendations are person-, context-, culture-, and timescale-dependent. Long-horizon outputs must preserve ambiguity flags, competing explanations, relapse dynamics, and the structural-vs-surface split.
4. **No clinical diagnosis, therapy, or individual prediction** — C05 is a structural/analytical framework, NOT clinical diagnosis. No medical diagnosis, no therapy, no personal future predictions. Behavioral patterns are models, not definitive assessments.
5. **All psychological claims are MODEL unless sourced** — All substantive psychological claims are MODEL unless explicitly sourced from a canonical spec (SOURCE) or a mathematical/structural consequence (DERIVED). No pop-psychology constructs enter without explicit model definition and claim class.
6. **Psychological causal firewall** — Do not infer causation from single-behavior observation, marker correlation alone, post-hoc narrative coherence, category labels alone, or framework plausibility alone. Correct claim form: `behavior pattern B is consistent with state hypotheses {S1, S2}, flagged ambiguous` — not `this person is S1`.
7. **Covert individual profiling prohibited** — Group-level outputs are statistical tendencies about populations/patterns. Deriving individual diagnoses from group signals is prohibited. Privacy: no covert profiling.

## Examples

- **Scenario**: User says "I'm feeling anxious about this presentation"
  - **Input**: Text markers indicating elevated arousal, worry, anticipation
  - **Output**: 5-axis emotion state model {valence: negative, arousal: high, dominance: low, certainty: low, energy: high} tagged AMOS_MODEL, with context-dependent framing recommendations

- **Scenario**: User says "My team seems unmotivated lately"
  - **Input**: Behavioral observation about group dynamics
  - **Output**: Group climate analysis using H7 Group Dynamics framework, motivation hypotheses flagged as COMPETING (insufficient individual data), recommendations tagged context-dependent

- **Scenario**: User says "Why does my friend keep avoiding conflict?"
  - **Input**: Personality pattern inquiry
  - **Output**: Personality Engine v0 trait analysis (avoidance pattern as MODEL), behavioral recommendations with culture/timescale flags, no clinical diagnosis

## Validation Gates

- **L0 Integrity**: All structural elements accounted for; no silent gaps
- **L1 Epistemic**: Every claim tagged with epistemic class (SOURCE_CLAIM / DERIVED / AMOS_MODEL)
- **L5 Scope**: Analysis confined to declared scope and domain
- **L7 Authority**: No autonomous action beyond authority boundary

## Anti-Patterns

- **Do not** diagnose clinical conditions — this is a modeling skill, not a clinical tool
- **Do not** assert personality traits as fixed — use Personality Engine v0 with timescale flags
- **Do not** collapse emotion, cognition, and behavior into one axis — they are distinct H-level domains
- **Do not** apply group dynamics frameworks to individuals without individual-level data
- **Do not** ignore cultural context — emotion expression and personality norms are culture-dependent

## Composition

- **With C04 Bio-Neuro**: UBI substrate distress veto feeds into emotion/cognition evaluation
- **With C03 Physics-Cosmos**: Cross-domain bridge for coupled human-Earth behavior modeling
- **With C12 Earth-Ecology**: Bidirectional bridge for ecological behavior patterns
- **With C06 Society-Culture**: Cultural context for emotion/personality interpretation
- **With C09 Org-Law-Policy**: Group dynamics feeding into governance and policy reasoning

## Evaluation

- **Epistemic class tagging**: All outputs tagged SOURCE_CLAIM, DERIVED, or AMOS_MODEL
- **Confidence ceiling**: Personality/emotion models capped at AMOS_MODEL unless empirically validated
- **Falsifiability**: Each hypothesis must have declared falsification conditions
- **Cross-domain boundary**: Domain-specific claims must not leak across domain boundaries without explicit bridge typing

## Error Handling

- **Insufficient data**: Return UNKNOWN/GAP, do not fabricate personality assessments
- **Domain boundary violation**: Flag and refuse cross-domain claims without bridge typing
- **Clinical scope violation**: Refuse clinical diagnosis attempts, redirect to appropriate domain
- **Cultural context missing**: Flag as context-dependent, do not assert universal norms

## Do not use

- For generic psychological analysis outside the mind/behavior framework
- To claim empirical validation of consciousness or cognitive theories
- As a substitute for domain-specific psychological or psychiatric evidence
- Outside mind/behavior domain reasoning

## References

- **Vault source**: `11_KNOWLEDGE/AMOS_C05_MIND_BEHAVIOR_MASTER_KNOWLEDGE.md` (vault canon, SOURCE_CLAIM)
- **Canon**: Emotion Law v0 (`AMOS.EmotionLaw.v0`), Personality Engine v0 (`AMOS.PersonalityEngine.Canonical.v0`), Behavior Engine v0 (`AMOS.BehaviorEngine.Canonical.v0`)
- **Causal Epoch**: L24 Causal Epoch Laws (`01_CANON/01_CORE_LAWS`)
- **Cross-domain bridge**: `AMOS_C12_earth_ecology_master_knowledge` (coupled human-Earth behavior, bidirectional, domain boundaries preserved)
- **Evaluation prompts**: `references/evaluation.md`

> **Reference**: See `references/c05_mind_behavior_config.md` for the C05 domain configuration.
> **Reference**: See `references/emotion_engine_canonical.md` for the canonical emotion engine spec.
> **Reference**: See `references/personality_engine_canonical.md` for the canonical personality engine spec.
> **Reference**: See `references/behavior_engine_canonical.md` for the canonical behavior engine spec.
> **Reference**: See `references/mind_behavior_engines.md` for the mind-behavior bridge engines.
> **Reference**: See `references/vault_sourced_domain_knowledge.md` for additional vault-sourced domain knowledge.

## Provenance

- **Skill**: amos-c05-mind-behavior-master
- **Source**: AMOS_OS Obsidian vault (`/Users/mac/Documents/AMOS_OS`)
- **Vault source**: `11_KNOWLEDGE/AMOS_C05_MIND_BEHAVIOR_MASTER_KNOWLEDGE.md`
- **Origin architect**: Trang Phan
- **H-level owners**: H1 Emotion Law, H2 Personality Engine, H3 Behavior Engine, H4 Mind-Behavior Bridge, H5 Cognitive/Motivational Structure (F1-F7), H6 Social/Change Dynamics (F8-F12), H7 Group Dynamics, H8 Micro-State Spectrum & UEE, H9 AMOS/Trang Research Bridge
