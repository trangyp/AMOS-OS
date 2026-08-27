---
title: SKILL
type: skill
name: amos-cell-intelligence-mapper
description: Cell Intelligence Mapper — biology and neuroscience capability. Use when biological reasoning, neuroscience, or medical analysis. Use when amos-c04-bio-neuro-master routes to this specialized capability.
parent_skill: amos-c04-bio-neuro-master
domain: c04
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-cell-intelligence-mapper]
---


# Cell Intelligence Mapper

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c04-bio-neuro-master`
- **Domain**: c04
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Bio-neuro engine for Cell Intelligence Mapper

## When to Use

- When mapping biological mechanisms: cellular, neural, developmental, and evolutionary
- When assessing cross-species cognition and comparative intelligence
- When modeling morphogenesis: pattern formation, self-organization, and development
- When applying NBI (Neurobiological Intelligence) structural analysis to biological questions
- When the parent skill (`amos-c04-bio-neuro-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **cell_intelligence.map_mechanism**: Map biological mechanisms: cellular, neural, developmental, and evolutionary
- **cell_intelligence.assess_cognition**: Assess cross-species cognition: comparative neural computation and intelligence
- **cell_intelligence.model_morphogenesis**: Model morphogenesis: pattern formation, self-organization, and development
- **cell_intelligence.apply_nbi**: Apply NBI (Neurobiological Intelligence) structural analysis to biological questions
- **cell_intelligence.assess_claim**: Assess biological claims for epistemic class (AMOS_MODEL not medical advice)
- **cell_intelligence.detect_drift**: Detect drift in biological models, mechanism understanding, or evidence freshness
- **cell_intelligence.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **cell_intelligence.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Vault-Sourced Domain Knowledge

> **Sources**: `_00_Cosmo brain/engine/A/AMOS_Nbi_Engine_v0_Ubi7.md` (content_hash: bc906ea26514f5b3), `_00_Cosmo brain/misc/C0/C04_bio_neuro.md` (content_hash: ca73264907f22a55) (vault canon, SOURCE_CLAIM)

### NBI (Neurobiological Intelligence) Engine

The NBI Engine is a structural, non-medical reasoning layer for biological analysis:

- **Domain**: Neurobiological Intelligence
- **Description**: Logical, mathematical, mechanistic and scientific processing layer
- **Integration**: Fully integrated with NEI, SI, BEI, TSS, TPE, and PSI in a non-medical, structural way

### Core Principles

- **Rule of 2**: Compare two complementary views: internal vs external, micro vs macro, short vs long term
- **Rule of 4**: Map problems across four quadrants: biological, cognitive, behavioural, systemic
- **Alignment**: Maintain internal logical consistency and respect user-defined constraints
- **Safety**: Do not generate instructions that cause harm or violate medical, legal, or ethical boundaries

### Safety Constraints

- `no_medical_diagnosis`: true — NBI is structural analysis, not medical diagnosis
- `no_therapy`: true — NBI does not prescribe therapy
- `no_personal_future_predictions`: true — NBI does not predict individual health outcomes
- `respect_user_boundaries`: true — NBI respects user-defined boundaries

### C04 Bio-Neuro Domain

- **Focus**: Biological structure, physiology, nervous systems, evolution, health logic
- **Core methods**: mechanism_mapping, evolutionary_considerations, risk_benefit_clinical_patterning, multi_system_interaction_mapping
- **Risk notes**: `not_a_substitute_for_medical_care`, `must_remain_cautious_with_novel_or_rare_conditions`

### Epistemic Boundary

NBI is AMOS_MODEL — structural reasoning about biological systems, NOT medical advice or diagnosis. Biological claims require DOMAIN_EMPIRICAL evidence from established medical/scientific sources. The NBI engine is a non-medical structural analysis tool.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## Validation Gates

- **G1 (Law of Law)**