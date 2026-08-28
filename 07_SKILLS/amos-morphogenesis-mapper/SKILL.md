---
schema_version: 1.0
title: SKILL — Amos Morphogenesis Mapper
type: skill
source: 07_SKILLS/amos-morphogenesis-mapper
name: amos-morphogenesis-mapper
description: Morphogenesis Mapper — biology and neuroscience capability. Use when
  biological reasoning, neuroscience, or medical analysis. Use when amos-c04-bio-neuro-master
  routes to this specialized capability. Do not use for generic tasks outside c04
  domain.
parent_skill: amos-c04-bio-neuro-master
domain: c04
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/bio-neuro
- rscf/source_claim
- hml/m
- epistemic/source_claim
- amos_os
- 07-skills-moc
- amos-morphogenesis-mapper-moc
- 00-home
- amos-rscf-nodes
- law-hierarchy
- references-moc
- trang-framework-recursive-ontology-dynamics
- skill
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
rscf_state: SOURCE_CLAIM
hml_level: M
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
license: MIT
steward: Trang Phan
---

# Morphogenesis Mapper

## Identity

Origin architect: **Trang Phan**. Domain: c04. Parent: amos-c04-bio-neuro-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.
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

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-morphogenesis-mapper_MOC]]

## Examples

- **Scenario**: When mapping biological mechanisms: cellular, neural, developmental
  - **Input**: A query matching this skill's domain (c04)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When assessing cross-species cognition and comparative intelligence
  - **Input**: A query matching this skill's domain (c04)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When modeling morphogenesis: pattern formation and self-organization
  - **Input**: A query matching this skill's domain (c04)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the c04 domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-c04-bio-neuro-master` — routes to this skill when c04 specialization is needed
- **Peers**: Other skills in the `c04` domain may be composed in sequence
- **Orchestrator**: The parent skill or `AMOS_HOME` orchestrates routing
- **Workflow**: Each skill has a corresponding workflow in `08_WORKFLOWS/`
- **Agent**: Each skill has a corresponding agent in `06_AGENTS/`


## Evaluation

### Success Criteria

- Output includes epistemic class label (SOURCE/DERIVED/AMOS_MODEL/EMPIRICAL)
- Output includes provenance reference to source evidence
- Output includes confidence ceiling (capped at 0.95 for DERIVED, 1.0 for SOURCE_CANON)
- Output includes gap flags for unresolved unknowns
- Output does not exceed declared scope

### Failure Modes

- **Overreach**: Output claims validity beyond its epistemic class
- **Scope creep**: Output addresses questions outside the declared domain
- **Provenance loss**: Output cannot trace back to source evidence
- **Confidence inflation**: Output confidence exceeds the weakest-premise ceiling


## Error Handling

- **On scope violation**: Reject the query and route back to parent skill
- **On missing evidence**: Flag as GAP and reduce confidence ceiling to 0.5
- **On contradiction**: Flag as CRITICAL_GAP and halt until resolved
- **On provenance loss**: Mark output as UNKNOWN and require human review
- **On drift**: Trigger drift alignment via `amos-ai-drift-alignment-governor`


## Do not use

- For generic biological analysis outside the bio/neuro framework
- To claim empirical validation of biological intelligence laws
- As a substitute for domain-specific medical or neuroscience evidence
- Outside biology/neuroscience domain reasoning

## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `` — skill Map of Content
- `amos-c04-bio-neuro-master` — parent skill
- `` — corresponding workflow
- `amos-morphogenesis-mapper-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-morphogenesis-mapper
node_type: skill
path: 07_SKILLS/amos-morphogenesis-mapper/[[SKILL]].md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
