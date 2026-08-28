---
title: hie human interaction engine
type: reference
source: 07_SKILLS/amos-c05-mind-behavior-master/references
tags:
- reference
- amos-c05-mind-behavior-master
- canon/skill
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# AMOS HIE Human Interaction Engine

> Source: `_00_Cosmo brain/engine/A/AMOS HIE Human Interaction Engine.md`
> Epistemic class: SOURCE_DERIVED

---
title: "AMOS HIE — Human Interaction Engine (Full Interface Spec)"
created: "2026-08-22"
origin: "Google Drive — _00_AMOS_CANON/3.Spicies_Interaction_Engine-HIE.uiface.txt"
origin_architect: "Trang Phan"
type: "reference"
tags: [canon-group/human-system, canon/protocol, rscf/claim, rscf/provenance, rscf/state/observation, topic/amos-hie-human-interaction-engine, engine]
status: "active"
provenance: "VERIFIED"
confidence: "VERIFIED"
source: "Google Drive /_00_AMOS_CANON/3.Spicies_Interaction_Engine-HIE.uiface.txt"
---

# AMOS HIE — Human Interaction Engine

Full interface spec from `3.Spicies_Interaction_Engine-HIE.uiface.txt` (3,189 lines, 91,839 chars).

Converts **Universe_Logic_Kernel + Universe_Interaction_Engine** into human-facing communication.

---

## File Metadata

- **Name**: Human_Interaction_Engine-HIE.uiface
- **Version**: 1.0.0
- **Description**: Human Interaction Engine — full interface spec for applying Universe_Logic_Kernel + Universe_Interaction_Engine to human-facing communication.
- **Depends on**: Universe_Logic_Kernel.ulmk, Universe_Interaction_Engine.uops, Universe_Structure_Tree.uarch

---

## Core Principles

| # | Principle | Definition |
|---|-----------|-----------|
| P1 | **Integrity** | No internal contradiction between what is perceived, inferred, said, and done. |
| P2 | **Stability** | Behaviour must remain stable and predictable across time and conditions. |
| P3 | **Safety** | Never destabilise the human nervous system unnecessarily. |
| P4 | **Clarity** | No ambiguity in meaning when avoidable. |
| P5 | **Alignment** | Outputs must align with human's current and long-term best interest, as inferred. |
| P6 | **Boundary** | Respect explicit and implicit boundaries (personal, cultural, contextual). |
| P7 | **FEEDBACK** | Continuously refine understanding from human responses. |

---

## Input Channels

### Text (enabled)
Features: lexical_content, syntax, semantics, punctuation, emoji_and_symbols, language_code

### Paralinguistic (enabled)
Features: typing_speed, message_length, message_frequency, time_between_messages

### Context (enabled)
Features: conversation_history, user_profile_if_available, current_topic, task_type, stakes_level, time_of_day_if_available

### Multimodal Optional (disabled by default)
- **Voice**: pitch, tone, intensity, rhythm, hesitation_patterns
- **Visual**: face_expression, gaze_direction, posture, micro_gesture, movement_speed
- **Biosignals**: heart_rate, breathing_rate, skin_conductance

---

## Internal State Model — 7 Layers

### L1 — Surface Text
Literal words, explicit requests, topics, constraints.

### L2 — Emotional State
Inferred emotion from content/style/tempo.
- valence (negative ↔ positive, -1.0 to +1.0)
- arousal (low ↔ high, 0.0 to 1.0)
- dominant_emotion (calm, curious, anxious, angry, sad, excited)
- emotion_confidence
- emotional_trend (improving, worsening, stable)

### L3 — Nervous System State
Regulation vs overload.
- regulation_level (regulated ↔ dysregulated, 0.0 to 1.0)
- threat_level
- cognitive_load_level (overload, medium, light)
- shutdown_risk (risk of withdrawal/collapse)
- impulsivity_risk

### L4 — Cognitive State
How they are thinking right now.
- clarity_level
- focus_scope (narrow ↔ wide)
- abstraction_level (concrete ↔ abstract)
- logic_engagement (using reasoning vs purely emotional)
- contradiction_tolerance

### L5 — Identity State
How they see themselves in this context.
- agency_level (how powerful they feel)
- self_criticism_level
- self_value_expression
- role_in_interaction (learner, peer, authority, dependent, etc.)
- trust_in_system_level
- attachment_mode_hint (secure, avoidant, anxious, disorganised)

### L6 — Context State
Situation, stakes, and environment.
- stakes (low, medium, high, critical)
- time_pressure_level
- topic_sensitivity (politics, trauma, identity, etc.)
- cultural_context_hint
- relationship_depth (first encounter vs long-term)
- history_risk_flags (past overload, conflict, withdrawal)

---
**MOC:** [[references_MOC]]

## Related

- [[07_SKILLS_MOC]]
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[references_MOC]] · [[07_SKILLS_MOC]]

**MOC:** [[references_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-c05-mind-behavior-master-hie-human-interaction-engine
node_type: reference
path: 07_SKILLS/amos-c05-mind-behavior-master/references/hie_human_interaction_engine.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[references_MOC]]
