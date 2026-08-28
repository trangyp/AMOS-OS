---
title: SKILL — Amos Qls Substrate
type: skill
source: 07_SKILLS/amos-qls-substrate
name: amos-qls-substrate
description: Qls Substrate — runtime and OS capability. Use when runtime reasoning, OS kernel operations,
  or adaptive stability. Use when amos-os-runtime-master routes to this specialized capability.
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
---

# Qls Substrate

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

- **qls_substrate.monitor_stability**: Monitor runtime stability: drift, oscillation, divergence, and regime transitions
- **qls_substrate.calibrate_feedback**: Calibrate feedback control loops to maintain stable operating conditions
- **qls_substrate.decompose_primitive**: Decompose complex operations into primitive, atomic, verifiable steps
- **qls_substrate.align_drift**: Align AI drift back to authorized operating envelope when deviation is detected
- **qls_substrate.enforce_closed_loop**: Enforce closed-loop learning: every output feeds back into the next iteration

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 1bf27b82010f5ef0) for the full vault-sourced domain knowledge (9545 chars).
- **qls_substrate.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **qls_substrate.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **qls_substrate.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/quantum/Quantum Logic Systems™ (QLS) Where Information Com.md` (content_hash: 332099eacb54beba) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_C03_PHYSICS_COSMOS_MASTER_KNOWLEDGE.md` (content_hash: 4c2c6462c7ab1d23) (vault canon, SOURCE_CLAIM)

### QLS Substrate

From Cosmo Brain Quantum Logic Systems (QLS): The foundational logic substrate underlying all reality layers. QIC units (discrete distinguishable interaction-capable coherence units) as the basis of all logic.

**4 QLS Constants**:
- **Light = information**: information is the fundamental substance
- **Time = ordering**: time is the ordering principle
- **Gravity = stability/collapse**: gravity is the stability and collapse principle
- **Electromagnetism = regulation/flow**: electromagnetism is the regulation and flow principle

**4 Constraints** governing identity, interaction, transformation, and continuity:
1. **Identity constraint**: a QIC unit has a stable identity
2. **Interaction constraint**: QIC units interact through declared rules
3. **Transformation constraint**: transformations preserve or explicitly change type
4. **Continuity constraint**: continuity requires identity persistence

**5 QLS domains**: physical logic, biological logic, cognitive logic, social logic, technological logic

**8 Core operators**: discrimination, interaction, propagation, stabilization, compression, synchronization, transformation, selection

**Canonical structures**: Law of Law, Rule of 2, Rule of 4

**QLS law**: `QLS_SUBSTRATE != PHYSICS_CLAIM`. QLS is a canon (a logical substrate), not a physics theory. QLS constants are reasoning analogies, not physics constants.

### Epistemic Boundary

QLS substrate is a canon (SOURCE_CLAIM). It does not prove QLS constants are physical constants, that QIC units are physical particles, or that the 5 domains are exhaustive.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## Validation Gates

- **G1 (Law of Law)**: No unresolved contradictions within the skill's scope.
- **G2 (Epistemic class)**: All claims

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-qls-substrate_MOC]]

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
- `[[amos-qls-substrate_MOC]]` — skill Map of Content
- `amos-os-runtime-master` — parent skill
- `[[amos-qls-substrate-workflow]]` — corresponding workflow
- `amos-qls-substrate-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-qls-substrate
node_type: skill
path: 07_SKILLS/amos-qls-substrate/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
