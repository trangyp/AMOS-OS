---
title: SKILL — Amos Universal Coordinate System
type: skill
source: 07_SKILLS/amos-universal-coordinate-system
name: amos-universal-coordinate-system
description: Universal Coordinate System — runtime and OS capability. Use when runtime
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
- amos-universal-coordinate-system
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
---




# Universal Coordinate System

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-os-runtime-master`
- **Domain**: runtime
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Runtime and OS engine for Universal Coordinate System

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

- **universal_coord_sys.monitor_stability**: Monitor runtime stability: drift, oscillation, divergence, and regime transitions
- **universal_coord_sys.calibrate_feedback**: Calibrate feedback control loops to maintain stable operating conditions
- **universal_coord_sys.decompose_primitive**: Decompose complex operations into primitive, atomic, verifiable steps
- **universal_coord_sys.align_drift**: Align AI drift back to authorized operating envelope when deviation is detected
- **universal_coord_sys.enforce_closed_loop**: Enforce closed-loop learning: every output feeds back into the next iteration

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 16b980aa9c1dcbb0) for the full vault-sourced domain knowledge (9422 chars).
- **universal_coord_sys.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **universal_coord_sys.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **universal_coord_sys.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/trang/trang_amos_reality_architecture_master_max_detail.md` (content_hash: da2bc7dc1c2ceeeb) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_C03_PHYSICS_COSMOS_MASTER_KNOWLEDGE.md` (content_hash: 4c2c6462c7ab1d23) (vault canon, SOURCE_CLAIM)

### Universal Coordinate System

From Trang Reality Architecture Master: Topology Before Geometry philosophy. Before measurement, coordinate systems, angles, distances, or quantities can exist, reality must first answer deeper structural questions.

**Topology Before Geometry principle** (SOURCE_CLAIM):
Before coordinate systems can exist, reality must answer:
1. **Connection**: what is connected to what?
2. **Separation**: what is separate from what?
3. **Transformation**: what transforms into what?
4. **Persistence**: what persists over time?
5. **Influence**: what influences what?

**Mathematics as observer-generated compression**: mathematics is the observer's compression of recurring structural patterns, not a pre-existing reality.

**Coordinate system model**:
- **Topological coordinates**: based on connectivity (before geometry)
- **Geometric coordinates**: based on distances and angles (after topology)
- **Universal coordinates**: coordinates that span multiple domains

**Coordinate system laws**:
- `TOPOLOGY > GEOMETRY`: topology is prior to geometry; geometry requires topology
- `COORDINATE != MEASUREMENT**: a coordinate is a reference; a measurement is an observation
- `UNIVERSAL != UNIFORM**: universal coordinates span domains; they are not uniform across domains

### Epistemic Boundary

Universal coordinate system is an AMOS_MODEL. It does not prove a single coordinate system works for all domains, that topology is always prior, or that the 5 structural questions are exhaustive.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## Validation Gates

- **G1 (Law of Law)**: No unresolved contradictions within the skill's scope.
- **

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-universal-coordinate-system_MOC]]

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
- `[[amos-universal-coordinate-system_MOC]]` — skill Map of Content
- `amos-os-runtime-master` — parent skill
- `[[amos-universal-coordinate-system-workflow]]` — corresponding workflow
- `amos-universal-coordinate-system-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-universal-coordinate-system
node_type: skill
path: 07_SKILLS/amos-universal-coordinate-system/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
