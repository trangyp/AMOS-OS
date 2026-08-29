---
schema_version: 1.0
title: SKILL — Amos Fractal Math
type: skill
source: 07_SKILLS/amos-fractal-math
name: amos-fractal-math
description: Fractal Math — fractal systems capability. Use when fractal analysis,
  scale reasoning, or self-similarity detection. Use when amos-fractal-systems-master
  routes to this specialized capability. Do not use for generic tasks outside fractal
  domain.
parent_skill: amos-fractal-systems-master
domain: fractal
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/fractal-systems
- rscf/source_claim
- hml/m
- epistemic/source_claim
- amos_os
- 07-skills-moc
- amos-fractal-math-moc
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
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance:
- L0
- L1
- L2
- L4
- L5
- L16
- L17
license: MIT
steward: Trang Phan
---

# Fractal Math

## Identity

Origin architect: **Trang Phan**. Domain: fractal. Parent: amos-fractal-systems-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.
## When to Use

- When analyzing fractal structure: self-similarity and scale invariance
- When quantifying AI entropy within fractal architectures
- When validating fractal equations against scale-invariance
- When mapping biological fractal patterns: branching and scaling
- When the parent skill (`amos-fractal-systems-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **fractal_math.analyze_fractal**: Analyze fractal structure: self-similarity, scale invariance, and recursion
- **fractal_math.quantify_entropy**: Quantify AI entropy within fractal architectures: information vs disorder
- **fractal_math.validate_equation**: Validate strict fractal equations against scale-invariance requirements
- **fractal_math.map_biology**: Map human biology fractal patterns: branching, scaling, and self-organization
- **fractal_math.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **fractal_math.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **fractal_math.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 66e052a4f7b27637) for the full vault-sourced domain knowledge (4630 chars).

## Operations

1. **fractal_math.analyze_fractal**: Analyze fractal structure: self-similarity, scale invariance, and recursion
2. **fractal_math.quantify_entropy**: Quantify AI entropy within fractal architectures: information vs disorder
3. **fractal_math.validate_equation**: Validate strict fractal equations against scale-invariance requirements
4. **fractal_math.map_biology**: Map human biology fractal patterns: branching, scaling, and self-organization
5. **fractal_math.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
6. **fractal_math.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
7. **fractal_math.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_C03_PHYSICS_COSMOS_MASTER_KNOWLEDGE.md` (content_hash: 4c2c6462c7ab1d23) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Fractal Math

From C03: H/M/L fractal architecture. From Cognitive Organism OS: H/M/L fractal mapping.

**Fractal H/M/L levels**:
- **H (High)**: whole organism / whole system
- **M (Medium)**: organ / subsystem
- **L (Low)**: local event / function

**Fractal integrity law**: `L_PASS != H_HEALTH`. A local pass (L-level) does not prove whole-system health (H-level). Integrity must be checked at all three levels.

**Fractal math operations**:
- **Self-similarity**: patterns repeat at different scales
- **Scale-invariance**: properties hold across scales
- **Lacunarity**: measures distribution of gaps in a structure
- **Fractal dimension**: non-integer dimension characterizing fractal sets

**AMOS fractal stance**: Fractal patterns in AMOS are analytical models (AMOS_MODEL), not physics claims. They describe structural properties, not physical laws.

### Epistemic Boundary

Fractal math is an analytical framework. It does not prove physical fractality, that all systems are fractal, or that fractal dimension captures all structural properties.

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

- **Skill**: `amos-fractal-math`
- **Parent**: `amos-fractal-systems-master`
- **Domain**: fractal
- **Origin architect**: Trang Phan
- **Vault sources**:
-

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-fractal-math_MOC]]

## Examples

- **Scenario**: When analyzing fractal structure: self-similarity and scale invariance
  - **Input**: A query matching this skill's domain (fractal)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When quantifying AI entropy within fractal architectures
  - **Input**: A query matching this skill's domain (fractal)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When validating fractal equations against scale-invariance
  - **Input**: A query matching this skill's domain (fractal)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the fractal domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-fractal-systems-master` — routes to this skill when fractal specialization is needed
- **Peers**: Other skills in the `fractal` domain may be composed in sequence
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

- For generic fractal analysis outside the fractal systems framework
- To claim empirical validation of self-similarity or scale theories
- As a substitute for domain-specific fractal or scale evidence
- Outside fractal systems domain reasoning

## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `` — skill Map of Content
- `amos-fractal-systems-master` — parent skill
- `` — corresponding workflow
- `amos-fractal-math-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-fractal-math
node_type: skill
path: 07_SKILLS/amos-fractal-math/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
