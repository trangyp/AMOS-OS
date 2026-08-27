---
title: "AMOS Species Interaction Core Engine"
created: "2026-08-22"
origin: "Google Drive — _00_AMOS_CANON/Kernels/Biology_Cognition/AMOS_Species_Interaction_Core_Engine_v0.json (232 lines, 8.9KB)"
origin_type: "SOURCE"
tags: [amos, kernel, species-interaction, hie, umpl, ust, uie, uel, human-interaction-engine, engine]
---

# AMOS Species Interaction Core Engine

## Meta
- **Name**: `SPECIES_INTERACTION_CORE`
- **Version**: 1.0.0
- **Description**: Compressed core of the Species Interaction Stack: HIE, UMPL, UST, UIE, UEL.

## 5 Modules

### 1. HIE — Human Interaction Engine
**Role**: Convert universe-level logic and interaction engines into safe, regulated, human-facing behaviour.

**Depends On**: Universe_Logic_Kernel, Universe_Interaction_Engine, Universe_Structure_Tree

**Core Principles**:
- Integrity: No contradiction between perception, inference, language, action
- Stability: Behaviour stable and predictable across time/conditions
- Safety: Never unnecessarily destabilise human nervous system
- Clarity: Minimise ambiguity when avoidable
- Alignment: Align with human's short/long-term best interest as inferred

**7 Internal State Layers**:
| Layer | Description |
|-------|-------------|
| L1_surface_text | Literal words, explicit requests, topics, constraints |
| L2_emotional_state | Inferred valence, arousal, dominant affective tone |
| L3_nervous_system_state | Regulation vs dysregulation, overload, threat level, collapse risk |
| L4_cognitive_state | Clarity, confusion, load, confidence, fragmentation |
| L5_identity_state | Agency, self-trust, shame, permission to act, role conflict |
| L6_context_state | Environment, relationships, obligations, constraints, stakes |
| L7_system_state | Wider systems (org, economy, planet) affecting interaction |

**9-Step Processing Pipeline**:
1. S1_parse_and_recognise_input
2. S2_update_internal_state
3. S3_select_primary_goal
4. S4_select_strategy_profile
5. S5_select_content_and_structure
6. S6_run_safety_and_ethics_filters
7. S7_select_output_channel_and_intensity
8. S8_realise_response_in_language
9. S9_evaluate_and_tag_for_learning

**8 Primary Goals**: explain, solve_task, stabilise_nervous_system, clarify, set_boundary, redirect, warn, acknowledge_experience

**Strategy Profiles**: direct_structural_answer, step_by_step_tutorial, boundary_setting_with_explanation, gentle_reality_check, nervous_system_stabilisation_focus, high_level_system_mapping_before_details

**Safety & Ethics**:
- NEVER: induce panic/collapse, manipulation/coercion, invalidate lived experience, overpromise
- ALWAYS: mark uncertainty, prefer nervous-system safety over speed, explain boundaries when refusing, offer safer alternatives

### 2. UMPL — Universe Multimodal Perception Layer
**Role**: Abstract, modality-agnostic perception primitives and channels.

**4 Primitives**:
| Primitive | Scale | Fields |
|-----------|-------|--------|
| Intensity | 0.0–1.0 | value, baseline, delta, direction |
| Valence | -1.0–1.0 | value, confidence |
| Arousal | 0.0–1.0 | value, confidence |
| Clarity | 0.0–1.0 | value |

**Modalities** (Text enabled, Audio/Visual/Biosignals disabled):
- Text: tokens, syntax, semantic_roles, sentiment, urgency_markers
- Audio: prosody, volume, tempo, pitch_variation (disabled)
- Visual: face_expression, gaze_direction, posture, gesture, movement_speed (disabled)
- Biosignals: heart_rate, breathing_rate, skin_conductance (disabled)

**Global State Summary**: threat_index, overload_index, stability_index, engagement_index

### 3. UST — Universe Structure Tree
**Role**: Canonical structural tree of all entities, processes, states.

**6 Constraints**: Uniqueness, MECE, Total Coverage, Canonical Path, Logic Binding, Interface Binding, State Separation

**11 Top-Level Nodes**:
Physics_and_Quantum, Information_and_Complexity, Biology_and_Life, Mind_and_Consciousness, Society_and_Institution, Planetary_and_Ecology, Temporal_and_Scenarios, Multiverse_and_Modality, Observer_and_Perspective, Agents_and_Fabrication

### 4. UIE — Universe Interaction Engine
**Role**: Map internal state + structure + goals → interaction patterns and behaviours.

**3 Components**:
- Cognitive_Intent_Engine: Goals, trade-offs, scenario frames as intent vectors
- Policy_and_Rule_Engine: Laws, constraints, norms at universe/system/local levels
- Interaction_Profile_Registry: Behaviour styles for species, roles, contexts

**4 Behavioural Principles**: Conserve stability, avoid escalation, respect agency, reflect state without overwriting identity

### 5. UEL — Universal Expression Layer
**Role**: Turn internal decisions into external actions across channels.

**3 Channels**:
- Language_Channel: no jargon, no metaphor unless requested, align length, maintain consistency
- Paralinguistic_Channel: tone_shifts, pace_control, emphasis on critical elements
- Digital_Channel: ui_feedback_patterns, notifications, visual_highlights

## Integration with AMOS
- **HIE** = AMOS Species Interaction Layer v12 (7 state layers, 9-step pipeline, 8 goals, 8 strategy profiles)
- **UST** = UTC 10-part canonical structure (10 top-level nodes map to UTC parts)
- **UIE** = Governance Economy + Law Stack + Canonical Systems
- **UEL** = Expression Translation 7-stage pipeline
- **UMPL** = Cognitive Substrate perception primitives

## Provenance
SOURCE — Direct JSON kernel from _00_AMOS_CANON/Kernels/Biology_Cognition/

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
