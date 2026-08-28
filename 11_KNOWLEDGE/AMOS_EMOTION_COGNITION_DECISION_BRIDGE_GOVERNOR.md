---
title: AMOS EMOTION COGNITION DECISION BRIDGE GOVERNOR
type: emotion
source: 11_KNOWLEDGE
canon-group: reference
rscf-state: derived
tags:
- skill
- knowledge
- vault
- cross-domain
- emotion
- cognition
- decision
- bridge
- c05
- c01
- c10
- canon/knowledge
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: AMOS_knowledge
---


# AMOS Emotion-Cognition-Decision Bridge Governor

## Overview

A new AMOS skill that bridges C05 (Mind & Behavior) with C01 (Meta-Logic) and C10 (Tech & Engineering) decision pipelines. Enforces the emotion influence gating invariant (emotion may bias prioritization and tone, NEVER facts or logic), connects C05's 5-axis emotion state to C01's reasoning mode selection, and unifies C05's decision style ordering with C10's diagnose-before-edit principle.

## Gap Evidence

From _00_Cosmo brain exploration: "Emotion ↔ Cognition ↔ Decision: Emotion rules exist but lack direct integration with cognitive engines and decision-making pipelines."

Specific gaps bridged:
1. C05's emotion state had no bridge to C01's reasoning mode selection
2. C05's decision style ordering had no bridge to C10's technical trade-off resolution
3. C01's uncertainty/risk assessment had no input from C05's emotional state
4. No unified decision pipeline combined emotional state + cognitive mode + technical constraints

## Capabilities (9)

1. `ecd_bridge.route_by_emotion` — Route to C01 cognitive mode based on C05 5-axis emotion state
2. `ecd_bridge.gate_emotion_influence` — Gate emotion influence crossing C05→C01/C10 (permitted: pacing/routing; blocked: facts/logic)
3. `ecd_bridge.unify_decision_style` — Unify C05/C01/C10 decision style orderings
4. `ecd_bridge.assess_risk_combined` — Combine C05 risk_alert + C01 uncertainty + C10 risk gating
5. `ecd_bridge.produce_decision_trace` — Unified auditable trace with all domain contributions
6. `ecd_bridge.detect_influence_violation` — Detect emotion influencing facts/logic across boundaries
7. `ecd_bridge.manage_lifecycle` — Manage lifecycle: classify, validate, trace, assess, detect
8. `ecd_bridge.detect_drift` — Detect emotion state decay, trait drift, decision style inconsistency
9. `ecd_bridge.validate_outputs` — Validate outputs against domain constraints and epistemic class

## Emotion-to-Cognition Routing Map

| C05 Emotion State | C01 Cognitive Mode | Confidence Ceiling |
|---|---|---|
| risk_alert > 0.7 | CONSERVATIVE / DEFENSIVE | ≤ 0.80 |
| curiosity_focus > 0.7 | EXPLORATORY | ≤ 0.70 |
| confidence > 0.8 AND risk < 0.3 | EXECUTION | ≤ 0.90 |
| care_alignment > 0.7 | COLLABORATIVE | ≤ 0.75 |
| respect_weighting > 0.7 | DEFERENTIAL | ≤ 0.75 |

Status: AMOS_MODEL — derived from C05 Emotion Law v0 influence gating rules.

## Unified Decision Style Ordering

```
1. INTEGRITY (C05: integrity_first; C10: diagnose before edit)
2. SAFETY (C05: goal 1; C10: capability bounds)
3. CORRECTNESS (C05: ordering; C10: runtime validation)
4. COMPLETENESS (C05: ordering; C01: assumption graph coverage)
5. USEFULNESS_WITHIN_POLICY (C05: goal 2; C10: bounded by authority)
6. FUTURE_OPERABILITY (C05: goal 3; C10: rollback basin)
7. FLUENCY (C05: ordering; never altering content truth)
8. SPEED (C05: ordering; never overrides integrity/safety/correctness)
```

Status: DERIVED — synthesis of C05 Personality Engine v0, C10 core invariants, C01 decision gates.

## Influence Gating Firewall

**PERMITTED**: pacing, verbosity, caution flags, routing decisions, load-awareness, cognitive mode selection, risk assessment weighting

**BLOCKED**: factual content, logical structure, claims of felt experience, empirical assertions, mathematical/formal correctness, technical diagnosis, architecture decisions

## 1:1:1 Binding

- **Skill**: `.devin/skills/amos-emotion-cognition-decision-bridge-governor/SKILL.md`
- **Agent**: `.devin/agents/amos-emotion-cognition-decision-bridge-governor-agent.json`
- **Workflow**: `.devin/workflows/amos-emotion-cognition-decision-bridge-governor-workflow.md`

## QA Validation

All 10 software-engineering-qa gates pass. Status: PRODUCTION_READY.
- 1:1:1 binding verified, JSON valid, 9 unique capabilities, 10 gates in skill + 10 in workflow
- Epistemic class: SOURCE_CLAIM, Claim ceiling: 0.90
- Trigger: 403 chars, Failure paths defined, Preconditions present

## Provenance

- **Origin architect**: Trang Phan
- **Parent skill**: `amos-c05-mind-behavior-master`
- **Domain**: cross-domain (C05→C01→C10)
- **Vault sources**: AMOS_C05_MIND_BEHAVIOR_MASTER_KNOWLEDGE.md, AMOS_C01_META_LOGIC_MASTER_KNOWLEDGE.md, AMOS_C10_TECH_ENGINEERING_MASTER_KNOWLEDGE.md, AMOS_Full_Brain_OS_Architecture.md, TENSOR_CONTRACTS.md
- **Created**: 2026-08-27
- **Method**: skill-creator + amos-workflow-builder + software-engineering-qa validation

---
**Related:** [[KNOWLEDGE_MOC]] · [[AMOS_C05_MIND_BEHAVIOR_MASTER_KNOWLEDGE]] · [[AMOS_C01_META_LOGIC_MASTER_KNOWLEDGE]] · [[AMOS_C10_TECH_ENGINEERING_MASTER_KNOWLEDGE]] · [[AMOS_CROSS_DOMAIN_TENSOR_COMPOSITION_GOVERNOR]]

---
RSCF-NODE
node_id: amos_emotion_cognition_decision_bridge_governor
node_type: note
path: 11_KNOWLEDGE/AMOS_EMOTION_COGNITION_DECISION_BRIDGE_GOVERNOR.md
RSCF-RELATIONS:
  - INDEXED_BY: [[KNOWLEDGE_MOC]]
  - DEPENDS_ON: [[AMOS_C05_MIND_BEHAVIOR_MASTER_KNOWLEDGE]]
  - DEPENDS_ON: [[AMOS_C01_META_LOGIC_MASTER_KNOWLEDGE]]
  - DEPENDS_ON: [[AMOS_C10_TECH_ENGINEERING_MASTER_KNOWLEDGE]]
  - COMPOSES_WITH: [[AMOS_CROSS_DOMAIN_TENSOR_COMPOSITION_GOVERNOR]]
claim_class: SOURCE_CLAIM
## Vault Sources Enriched (2026-08-27)

### Emotion Rules Engine (Cosmo brain: emotion/Emotion_Rules.md)

Explicit rules linking nervous system state to emotional posture:
- **flow state** → positive emotion, family=joy, type=optimal
- **high/very_high stress** → negative emotion, family=fear, type=stress_response
- **calm_focus** → neutral emotion, family=care, type=balanced

### Biology & Cognition Engine (Cosmo brain: biology-ubi/Biology_Cognition_Model.md)

7-layer scaffolding for biological/neurological/cognitive systems:
1. L1 Biological Foundations (Molecular, Cellular, Organs)
2. L2 Neural Computation (Rate coding, oscillations, microcircuits)
3. L3 Cognitive Domains (Perception, attention, learning, executive)
4. L4 Emotion, Motivation & Behavior (Valence/arousal, emotion families, drives)
5. L5 Variation, Pathology & Recovery
6. L6 Social Cognition (Mentalizing, trust, hierarchies)
7. L7 Interfaces (Logic, Engineering, Governance)

L4 is the primary bridge point between C05 emotion and C01/C10 decision-making.

**Limits**: Not a medical device. High-stakes decisions demand human review.

---
**MOC:** [[KNOWLEDGE_MOC]]
