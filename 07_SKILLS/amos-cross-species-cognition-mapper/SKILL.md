---
title: SKILL
type: skill
name: amos-cross-species-cognition-mapper
description: Cross Species Cognition Mapper — biology and neuroscience capability. Use when biological reasoning, neuroscience, or medical analysis. Use when amos-c04-bio-neuro-master routes to this specialized capability.
parent_skill: amos-c04-bio-neuro-master
domain: c04
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-cross-species-cognition-mapper]
---


# Cross Species Cognition Mapper

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c04-bio-neuro-master`
- **Domain**: c04
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Bio-neuro engine for Cross Species Cognition Mapper

## When to Use

- When mapping biological mechanisms: cellular, neural, developmental
- When assessing cross-species cognition and comparative intelligence
- When modeling morphogenesis: pattern formation and self-organization
- When the parent skill (`amos-c04-bio-neuro-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **cross_species.map_mechanism**: Map biological mechanisms: cellular, neural, developmental, and evolutionary
- **cross_species.assess_cognition**: Assess cross-species cognition: comparative neural computation and intelligence
- **cross_species.model_morphogenesis**: Model morphogenesis: pattern formation, self-organization, and development

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 043531e6396b1924) for the full vault-sourced domain knowledge (9402 chars).
- **cross_species.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **cross_species.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **cross_species.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_C04_BIO_NEURO_MASTER_KNOWLEDGE.md` (content_hash: 6fbde28c766c9d49) (vault canon, SOURCE_CLAIM)

### Cross-Species Cognition Mapping

From C04 Bio & Neuro: NBI (Neurobiological Intelligence) and biological logic translation.

**Cross-species cognition model**:
- **NBI levels**: species vary in NBI complexity (single-cell to human)
- **Cognitive capabilities**: vary across species (memory, learning, problem-solving, social cognition)
- **Biological logic**: shared biological logic principles across species (UBI 4 domains)

**Mapping dimensions**:
- **NBI complexity**: from single-cell to neural network to brain
- **Cognitive capability**: memory, learning, planning, social, tool use
- **Adaptive strategy**: adaptation level, flexibility, innovation
- **Social complexity**: solitary to social to eusocial

**Mapping law**: `SPECIES != MODEL`. A species' cognition is not a model for another species' cognition. Cross-species mapping identifies analogies, not identities.

**UBI 4 domains**: NBI (Neurobiological), NEI (Neuro-Emotional), SI (Somatic), BEI (Bio-Energetic) -- shared across species with varying complexity.

### Epistemic Boundary

Cross-species cognition mapping is an analytical model. It does not prove cognitive universality, that all species can be mapped, or that analogies prove shared mechanisms.

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
- **G4 (Anti-overreach)**: No claim beyond the skill's declared scope and epistemic class.
- **G5 (Equation firewall)**: Equations carry status tags (ESTABLISHED_MATH / SOURCE_DERIVED / AMOS_MODEL / EMPIRICALLY_CALIBRATED / UNVERIFIED).
- **G6 (Failure mode)**: On validation failure, downgrade confidence, flag the gap, escalate — do not force-fit.

## Provenance

- **Skill**: `amos-cross-species-cognition-mapper`
- **Parent**: `amos-c04-bio-neuro-master`
- **Domain**: c04
- **Origin architect**: Trang Phan
- **Vault sources**:
- `amos-general/A/CROSS/AMOS_CROSS_

---
**Links:** [[07_SKILLS_MOC]]
