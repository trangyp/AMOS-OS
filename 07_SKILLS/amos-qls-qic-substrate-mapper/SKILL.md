---
title: SKILL — Amos Qls Qic Substrate Mapper
type: skill
source: 07_SKILLS/amos-qls-qic-substrate-mapper
name: amos-qls-qic-substrate-mapper
description: Qls Qic Substrate Mapper — runtime and OS capability. Use when runtime
  reasoning, OS kernel operations, or adaptive stability. Use when amos-os-runtime-master
  routes to this specialized capability.
parent_skill: amos-os-runtime-master
domain: runtime
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/os-runtime
- canon-group/tech-ai
- topic/runtime
- rscf/epistemic
- rscf/S-state
- rscf/μ-mutation
- rscf/G-relation
- rscf/C-constraint
- rscf/type-system
- sota/progressive-disclosure
- sota/anti-patterns
- amos_os
- amos-qls-qic-substrate-mapper
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
---




# Qls Qic Substrate Mapper

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-os-runtime-master`
- **Domain**: runtime
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Runtime and OS engine for Qls Qic Substrate Mapper

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

- **qls_qic.monitor_stability**: Monitor runtime stability: drift, oscillation, divergence, and regime transitions
- **qls_qic.calibrate_feedback**: Calibrate feedback control loops to maintain stable operating conditions
- **qls_qic.decompose_primitive**: Decompose complex operations into primitive, atomic, verifiable steps
- **qls_qic.align_drift**: Align AI drift back to authorized operating envelope when deviation is detected
- **qls_qic.enforce_closed_loop**: Enforce closed-loop learning: every output feeds back into the next iteration

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: f68386fed89b4021) for the full vault-sourced domain knowledge (9570 chars).
- **qls_qic.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **qls_qic.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **qls_qic.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/indexes/Master Non-Overlap Index v0 3.md` (content_hash: e26ee91dd65dd1ad) (vault canon, SOURCE_CLAIM)
> **Additional source**: `_00_Cosmo brain/quantum/Quantum Logic Systems™ (QLS) Where Information Com.md` (content_hash: 332099eacb54beba) (vault canon, SOURCE_CLAIM)

### QLS QIC Substrate Mapper

From Cosmo Brain Master Non-Overlap Index: QIC substrate in QLS/Law Layer (section B, item 1). From QLS: QIC units as discrete distinguishable interaction-capable coherence units.

**QIC substrate components** (from Master Non-Overlap Index):
- **QIC substrate**: the foundational substrate of QIC units
- **QLS operators**: operators acting on QIC units
- **Four Constraints**: identity, interaction, transformation, continuity
- **5 domains**: physical logic, biological logic, cognitive logic, social logic, technological logic
- **QLS cognition model**: how QLS applies to cognition
- **Civilization model**: how QLS applies to civilization
- **Technology model**: how QLS applies to technology
- **Failure grammar**: how QLS failures are described

**QIC unit definition**: discrete distinguishable interaction-capable coherence unit -- the fundamental unit of the QLS substrate.

**Mapping protocol**:
1. **Identify QIC units**: identify the QIC units in the system
2. **Map substrate**: map the QIC substrate structure
3. **Map operators**: map the QLS operators acting on the units
4. **Map constraints**: map the Four Constraints
5. **Map domains**: map the 5 domains
6. **Record**: record with provenance and epistemic class

**Mapping laws**:
- `QIC != PARTICLE`: QIC is a logical unit; it is not a physical particle
- `SUBSTRATE != MEDIUM**: substrate is the foundational layer; medium is the carrier
- `MAP != IDENTITY**: mapping represents the substrate; it is not the substrate itself

### Epistemic Boundary

QLS QIC substrate mapping is an AMOS_MODEL. It does not prove QIC units are physical, that the substrate is complete, or that the mapping captures all QLS dynamics.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## Valid

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-qls-qic-substrate-mapper_MOC]]

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


## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `[[amos-qls-qic-substrate-mapper_MOC]]` — skill Map of Content
- `amos-os-runtime-master` — parent skill
- `[[amos-qls-qic-substrate-mapper-workflow]]` — corresponding workflow
- `amos-qls-qic-substrate-mapper-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-qls-qic-substrate-mapper
node_type: skill
path: 07_SKILLS/amos-qls-qic-substrate-mapper/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
