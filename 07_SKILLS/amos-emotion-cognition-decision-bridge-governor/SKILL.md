---
title: SKILL
type: skill
name: amos-emotion-cognition-decision-bridge-governor
description: Emotion-Cognition-Decision Bridge Governor — mind and behavior capability. Bridges C05 emotion/personality/behavior engines with C01 meta-logic decision gates and C10 technical decision-making. Enforces the emotion influence gating invariant (emotion may bias prioritization and tone, NEVER facts or logic), connects C05's 5-axis emotion state to C01's reasoning mode selection, and unifies C05's decision style ordering with C10's diagnose-before-edit principle. Use when a decision requires both emotional state awareness and cognitive/technical rigor. Use when amos-c05-mind-behavior-master routes to this specialized capability.
parent_skill: amos-c05-mind-behavior-master
domain: cross-domain (C05→C01→C10)
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-emotion-cognition-decision-bridge-governor]
---


# Emotion-Cognition-Decision Bridge Governor

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c05-mind-behavior-master`
- **Domain**: cross-domain (C05 Mind & Behavior → C01 Meta-Logic → C10 Tech & Engineering)
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from C05, C01, C10 master knowledge files)

Bridges the emotion-cognition-decision pipeline across three AMOS domains. C05 provides the 5-axis emotion state, personality traits, and behavior engine goal ordering. C01 provides meta-logic decision gates, reasoning mode selection, and uncertainty/risk assessment. C10 provides technical decision-making with diagnose-before-edit discipline. This governor ensures that emotional state informs cognitive mode selection and decision prioritization without violating the influence gating invariant.

## The Problem This Skill Solves

C05 defines a rich emotion-personality-behavior system with a critical invariant: *"Emotional axes may bias prioritization and tone, never facts or logic."* C01 defines meta-logic decision gates and reasoning mode governance. C10 defines technical decision-making with diagnose-before-edit. However, these three systems operate independently:

1. **C05's emotion state has no bridge to C01's reasoning mode selection** — high `risk_alert` should force conservative routing in C01, but no mechanism connects them
2. **C05's decision style ordering (integrity > correctness > completeness > fluency > speed) has no bridge to C10's technical decisions** — the ordering should govern technical trade-off resolution, but no pipeline carries it
3. **C01's uncertainty/risk assessment has no input from C05's emotional state** — `confidence_level` and `risk_alert` from C05 should inform C01's uncertainty budgeting
4. **No unified decision pipeline** combines emotional state + cognitive mode + technical constraints into a single auditable decision trace

The `_00_Cosmo brain` exploration explicitly identified this gap: *"Emotion ↔ Cognition ↔ Decision: Emotion rules exist but lack direct integration with cognitive engines and decision-making pipelines."*

## When to Use

- When a decision requires both emotional state awareness (C05) and cognitive/technical rigor (C01/C10)
- When routing a query based on emotional state (e.g., high risk_alert → conservative mode)
- When resolving a technical trade-off using C05's decision style ordering
- When validating that emotion influence gating is preserved across domain boundaries
- When producing a unified decision trace that includes emotion state, cognitive mode, and technical constraints
- When C05's behavior engine goal ordering needs to be applied in a C10 technical context
- When the parent skill (`amos-c05-mind-behavior-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **ecd_bridge.route_by_emotion**: Route a reasoning task to the appropriate C01 cognitive mode based on C05's 5-axis emotion state. High `risk_alert` → conservative/defensive mode; high `curiosity_focus` → exploratory mode; high `confidence_level` → execution mode. Returns mode + routing rationale.
- **ecd_bridge.gate_emotion_influence**: Gate emotion influence when crossing from C05 into C01/C10. Enforces the invariant: emotion may bias prioritization and tone, NEVER facts or logic. Returns PERMITTED_INFLUENCE list (pacing, verbosity, caution flags, routing) and BLOCKED_INFLUENCE list (factual content, logical structure, claims of felt experience).
- **ecd_bridge.unify_decision_style**: Unify C05's decision style ordering (integrity > correctness > completeness > fluency > speed) with C10's technical trade-off resolution and C01's meta-logic decision gates. Produces a single ordered preference list applicable across all three domains.
- **ecd_bridge.assess_risk_combined**: Combine C