---
schema_version: 1.0
title: SKILL — Amos Cross Species Cognition Mapper
type: skill
source: 07_SKILLS/amos-cross-species-cognition-mapper
name: amos-cross-species-cognition-mapper
description: Cross Species Cognition Mapper — biology and neuroscience capability.
  Use when biological reasoning, neuroscience, or medical analysis. Use when amos-c04-bio-neuro-master
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
- amos-cross-species-cognition-mapper-moc
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

# Cross Species Cognition Mapper

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

## Related

- [[amos-cross-species-cognition-mapper_MOC]]

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
- `amos-cross-species-cognition-mapper-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-cross-species-cognition-mapper
node_type: skill
path: 07_SKILLS/amos-cross-species-cognition-mapper/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
