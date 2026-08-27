---
title: SKILL
type: skill
name: amos-morphogenesis-mapper
description: Morphogenesis Mapper — biology and neuroscience capability. Use when biological reasoning, neuroscience, or medical analysis. Use when amos-c04-bio-neuro-master routes to this specialized capability.
parent_skill: amos-c04-bio-neuro-master
domain: c04
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-morphogenesis-mapper]
---


# Morphogenesis Mapper

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c04-bio-neuro-master`
- **Domain**: c04
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Bio-neuro engine for Morphogenesis Mapper

## When to Use

- When mapping biological mechanisms: cellular, neural, developmental
- When assessing cross-species cognition and comparative intelligence
- When modeling morphogenesis: pattern formation and self-organization
- When the parent skill (`amos-c04-bio-neuro-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **morphogenesis.map_mechanism**: Map biological mechanisms: cellular, neural, developmental, and evolutionary
- **morphogenesis.assess_cognition**: Assess cross-species cognition: comparative neural computation and intelligence
- **morphogenesis.model_morphogenesis**: Model morphogenesis: pattern formation, self-organization, and development
- **morphogenesis.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **morphogenesis.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **morphogenesis.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: e18a2e3f25a4b772) for the full vault-sourced domain knowledge (8481 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_C04_BIO_NEURO_MASTER_KNOWLEDGE.md` (content_hash: 6fbde28c766c9d49) (vault canon, SOURCE_CLAIM)

### Morphogenesis Mapping

From C04 Bio & Neuro: Biological development and form generation.

**Morphogenesis model**:
- **Pattern formation**: how biological patterns emerge (Turing patterns, reaction-diffusion)
- **Cell differentiation**: how cells specialize from a single fertilized egg
- **Morphogen gradients**: how concentration gradients guide development
- **Apoptosis**: how programmed cell death shapes structures

**Mapping to AMOS**:
- **Pattern formation -> Structure emergence**: how AMOS structures emerge from simple rules
- **Cell differentiation -> Capability specialization**: how generic capabilities specialize
- **Morphogen gradients -> Signal gradients**: how signals guide system development
- **Apoptosis -> Pruning**: how unnecessary components are removed

**Mapping law**: `BIOLOGICAL != ARCHITECTURAL`. Biological morphogenesis is not identical to system architecture development. The mapping is an analogy (AMOS_MODEL).

### Epistemic Boundary

Morphogenesis mapping is an analytical analogy. It does not prove the system develops biologically, that the mapping is biologically accurate, or that morphogenesis principles apply to all systems.

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

- **Skill**: `amos-morphogenesis-mapper`
- **Parent**: `amos-c04-bio-neuro-master`
- **Domain**: c04
- **Origin architect**: Trang Phan
- **Vault sources**:
- `brain/A/amos_brain_performance_optimizer.md` — -*- coding: utf-8 -*- (48128 chars, score: 3), content_hash: 7371c326ec17ca19
  - `brain/A/amos_brain_