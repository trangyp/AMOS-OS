---
schema_version: 1.0
title: SKILL — Amos Ust Structure Mapper
type: skill
source: 07_SKILLS/amos-ust-structure-mapper
name: amos-ust-structure-mapper
description: Ust Structure Mapper — runtime and OS capability. Use when runtime reasoning,
  OS kernel operations, or adaptive stability. Use when amos-os-runtime-master routes
  to this specialized capability. Do not use for generic tasks outside runtime domain.
parent_skill: amos-os-runtime-master
domain: runtime
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/os-runtime
- rscf/source_claim
- hml/m
- epistemic/source_claim
- amos_os
- 07-skills-moc
- amos-ust-structure-mapper-moc
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
- L8_execution
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance:
- L0
- L1
- L2
- L4
- L5
- L7
- L8
- L16
- L17
- L18
license: MIT
steward: Trang Phan
---

# Ust Structure Mapper

## Identity

Origin architect: **Trang Phan**. Domain: runtime. Parent: amos-os-runtime-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.
## When to Use

- When monitoring runtime stability: drift, oscillation, divergence
- When calibrating feedback control loops for stable operation
- When decomposing complex operations into primitive steps
- When enforcing closed-loop learning and drift alignment
- When the parent skill (`amos-os-runtime-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **ust_structure.monitor_stability**: Monitor runtime stability: drift, oscillation, divergence, and regime transitions
- **ust_structure.calibrate_feedback**: Calibrate feedback control loops to maintain stable operating conditions
- **ust_structure.decompose_primitive**: Decompose complex operations into primitive, atomic, verifiable steps
- **ust_structure.align_drift**: Align AI drift back to authorized operating envelope when deviation is detected
- **ust_structure.enforce_closed_loop**: Enforce closed-loop learning: every output feeds back into the next iteration
- **ust_structure.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **ust_structure.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **ust_structure.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 5845760e81d7bada) for the full vault-sourced domain knowledge (7866 chars).

## Operations

1. **ust_structure.monitor_stability**: Monitor runtime stability: drift, oscillation, divergence, and regime transitions
2. **ust_structure.calibrate_feedback**: Calibrate feedback control loops to maintain stable operating conditions
3. **ust_structure.decompose_primitive**: Decompose complex operations into primitive, atomic, verifiable steps
4. **ust_structure.align_drift**: Align AI drift back to authorized operating envelope when deviation is detected
5. **ust_structure.enforce_closed_loop**: Enforce closed-loop learning: every output feeds back into the next iteration
6. **ust_structure.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
7. **ust_structure.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
8. **ust_structure.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### UST (Universe Structure) Mapper

From Cognitive Organism OS: Universe structure mapping through the 7-part canon.

**7-part universe canon mapping**:
- **Constraint**: capacity, authority, identity boundaries
- **Flow**: events, memory, evidence, action
- **Structure**: organ topology and interfaces
- **Enforcement**: policy and authority gates
- **Time**: lifecycle, freshness, fatigue
- **Adaptation**: learning and repair
- **Termination**: shutdown, collapse, recovery

**UST mapping protocol**:
1. **Identify the system**: what system is being mapped?
2. **Apply 7-part canon**: map the system to each of the 7 parts
3. **Check completeness**: are all 7 parts represented?
4. **Check consistency**: are the parts internally consistent?
5. **Record**: record the UST mapping with provenance

**Law**: `MAPPING != REALITY`. A UST mapping is a structural description, not a reality claim. The 7-part canon is an analytical framework, not a physical theory.

### Epistemic Boundary

UST structure mapping is an analytical framework. It does not prove the 7-part canon is universal, that all systems can be mapped, or that the mapping captures all structural properties.

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

- **Skill**: `amos-ust-structure-mapper`
-

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-ust-structure-mapper_MOC]]

## Examples

- **Scenario**: When monitoring runtime stability: drift, oscillation, divergence
  - **Input**: A query matching this skill's domain (runtime)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When calibrating feedback control loops for stable operation
  - **Input**: A query matching this skill's domain (runtime)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When decomposing complex operations into primitive steps
  - **Input**: A query matching this skill's domain (runtime)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the runtime domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-os-runtime-master` — routes to this skill when runtime specialization is needed
- **Peers**: Other skills in the `runtime` domain may be composed in sequence
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

- For generic runtime analysis outside the AMOS OS/runtime framework
- To claim empirical validation of OS or runtime theories
- As a substitute for domain-specific runtime or infrastructure evidence
- Outside runtime/OS domain reasoning

## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `` — skill Map of Content
- `amos-os-runtime-master` — parent skill
- `` — corresponding workflow
- `amos-ust-structure-mapper-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-ust-structure-mapper
node_type: skill
path: 07_SKILLS/amos-ust-structure-mapper/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
