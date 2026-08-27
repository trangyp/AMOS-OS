---
title: SKILL
type: skill
name: amos-sensory-map-integrator
description: Sensory Map Integrator — biology and neuroscience capability. Use when biological reasoning, neuroscience, or medical analysis. Use when amos-c04-bio-neuro-master routes to this specialized capability.
parent_skill: amos-c04-bio-neuro-master
domain: c04
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-sensory-map-integrator]
---


# Sensory Map Integrator

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c04-bio-neuro-master`
- **Domain**: c04
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Bio-neuro engine for Sensory Map Integrator

## When to Use

- When mapping neurotransmitter systems: synthesis, release, reuptake, receptor activation
- When integrating sensory maps across biological cognition layers
- When modeling 7-layer biological scaffolding from molecular to social cognition
- When assessing cross-species cognition and comparative intelligence
- When the parent skill (`amos-c04-bio-neuro-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **sensory_map.map_mechanism**: Map biological mechanisms: cellular, neural, developmental, and evolutionary
- **sensory_map.assess_cognition**: Assess cross-species cognition: comparative neural computation and intelligence
- **sensory_map.model_morphogenesis**: Model morphogenesis: pattern formation, self-organization, and development
- **sensory_map.map_neurotransmitters**: Map neurotransmitter systems: synthesis sites, release sites, receptor subtypes
- **sensory_map.integrate_layers**: Integrate biological cognition layers: molecular → neural → cognitive → social
- **sensory_map.detect_drift**: Detect drift in neurotransmitter maps, cognition models, or evidence freshness
- **sensory_map.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **sensory_map.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Vault-Sourced Domain Knowledge

> **Sources**: `_00_Cosmo brain/system/Neurotransmitter Map — Complete Human System.md` (content_hash: 65ce68025b96d942), `_00_Cosmo brain/biology-ubi/Biology_Cognition_Model.md` (content_hash: ba8c82870d94b577) (vault canon, SOURCE_CLAIM)

### Neurotransmitter System Map

11 neurotransmitters with complete mapping (synthesis → release → reuptake → receptor activation):

- **Dopamine**: mesolimbic, mesocortical, nigrostriatal pathways
- **Serotonin**: mood, sleep, appetite regulation
- **Norepinephrine**: attention, arousal, stress response
- **GABA**: inhibitory balance
- **Glutamate**: excitatory signaling, learning
- **Acetylcholine**: memory, muscle activation
- **Histamine**: wakefulness, inflammatory response
- **Oxytocin**: social bonding, trust
- **Vasopressin**: social behavior, water balance
- **Cortisol**: stress response (GR/MR receptors)
- **Melatonin**: circadian regulation (MT1/MT2 receptors)

**Receptor types**: ionotropic (fast, ligand-gated) vs metabotropic (slow, G-protein coupled)

### 7-Layer Biological Cognition Model

| Layer | Name | Focus |
|-------|------|-------|
| L1 | Molecular | DNA/RNA, neurotransmitters, receptor binding |
| L2 | Cellular | Neurons, glia, signal transduction |
| L3 | Circuit | Rate coding, oscillations, synchrony |
| L4 | System | Perception, attention, learning, memory |
| L5 | Emotion | Motivation, affect, behavioral drives |
| L6 | Social | Social cognition, theory of mind, interfaces |
| L7 | Interface | External coupling, environment, culture |

### Epistemic Boundary

Neurotransmitter mapping is SOURCE_CLAIM (vault-sourced structural model). Biological cognition layers are AMOS_MODEL. Neither constitutes medical advice or neuroscience proof. Always recommend professional medical review for clinical questions.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## Validation Gates

- **G1 (Law of Law)**: No unresolved contradictions within the skill's scope.
- **G2 (Epistemic class)**: All claims labeled SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL — never claim beyond evidence.
- **G3 (Provenance)**: Source path recorded for every derived claim.
- *

---
**Links:** [[07_SKILLS_MOC]]
