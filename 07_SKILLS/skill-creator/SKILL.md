---
title: SKILL
type: skill
name: skill-creator
description: Skill Creator — agent systems capability. Use when agent design, delegation reasoning, or multi-agent governance. Use when amos-agent-systems-master routes to this specialized capability.
parent_skill: amos-agent-systems-master
domain: agent
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, skill-creator]
---


# Skill Creator

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-agent-systems-master`
- **Domain**: agent
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Agent systems engine for Skill Creator

## When to Use

- When creating new AMOS skills with proper structure and provenance
- When designing agent systems with delegation reasoning and multi-agent governance
- When governing agency: who acts, under what authority, with what consequences
- When designing agent externalization: what is delegated, to whom, with what controls
- When attributing agent ownership: who is responsible for each agent action
- When the parent skill (`amos-agent-systems-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **skill_creator.govern_agency**: Govern agency: who acts, under what authority, with what consequences
- **skill_creator.design_externalization**: Design agent externalization: what is delegated, to whom, with what controls
- **skill_creator.attribute_ownership**: Attribute agent ownership: who is responsible for each agent action
- **skill_creator.verify_agentic**: Verify agentic skill-lie algebroid: structural consistency of agent capabilities

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: f1ec52500d2df100) for the full vault-sourced domain knowledge (9459 chars).
- **skill_creator.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **skill_creator.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **skill_creator.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Skill Creation Pipeline

The Cognitive Organism OS defines skill creation through a structured pipeline:

**Pipeline**: ORIENT -> GAP -> SOURCE -> ARCHITECT -> BUILD -> INTEGRATE -> CHALLENGE -> VALIDATE -> PACKAGE

1. **ORIENT**: understand the problem space and identify the capability gap
2. **GAP**: declare the specific gap the skill will fill
3. **SOURCE**: find vault sources for the skill content
4. **ARCHITECT**: design the skill architecture (capabilities, gates, failure modes)
5. **BUILD**: build the skill content with provenance
6. **INTEGRATE**: integrate with parent skill and domain master
7. **CHALLENGE**: challenge the skill with adversarial review
8. **VALIDATE**: validate against all 10 validation gates
9. **PACKAGE**: package with 1:1:1 binding (skill + agent + workflow)

**Skill laws**:
- `SKILL != ONTOLOGY`: a skill is a deployment artifact, not an ontological definition
- `CAPABILITY != AUTHORITY`: having a capability does not authorize its use
- `BUILD != COMPLETE`: building a skill is not completing it; completion requires validation and binding

### Epistemic Boundary

The skill creator is an operational process. It does not prove skills are always correct, that the pipeline is optimal, or that all skills can be built this way.

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
- **G6 (Failure mode)**: On validation failure, downgrade confidence, flag the gap, escala