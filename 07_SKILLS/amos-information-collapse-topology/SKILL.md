---
schema_version: 1.0
title: SKILL — Amos Information Collapse Topology
type: skill
source: 07_SKILLS/amos-information-collapse-topology
name: amos-information-collapse-topology
description: Information Collapse Topology — info capability. Use when executing the core capability within this domain. Use when amos-information-theory-master routes to this specialized capability. Do not use for generic tasks outside info domain.
parent_skill: amos-information-theory-master
domain: info
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/information-theory
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

# Information Collapse Topology


## Identity

Origin architect: **Trang Phan**. Domain: info. Parent: amos-information-theory-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.
## When to Use

- When measuring entropy and lacunarity: information content and gaps
- When analyzing information collapse topology and structure
- When controlling information exposure and disclosure
- When mapping information geometry: manifolds and projections
- When the parent skill (`amos-information-theory-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **information_collapse.measure_entropy**: Measure entropy and lacunarity: information content, gaps, and structure
- **information_collapse.analyze_topology**: Analyze information collapse topology: how information condenses and structures
- **information_collapse.control_exposure**: Control information exposure: what is revealed, to whom, and under what conditions
- **information_collapse.map_geometry**: Map information geometry: manifolds, distances, and projections in information space
- **information_collapse.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **information_collapse.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **information_collapse.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: da43f41f0aa090c9) for the full vault-sourced domain knowledge (8315 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/amos-general/A/Universe/AMOS_UNIVERSE_CORE.md` (content_hash: 15f6a73982ed5a30) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_C03_PHYSICS_COSMOS_MASTER_KNOWLEDGE.md` (content_hash: 4c2c6462c7ab1d23) (vault canon, SOURCE_CLAIM)

### Information Collapse Topology

From Cosmo Brain Universe Core: Information Engine (ENG3) governing information, encoding, memory, and entanglement. INF13_CollapseTopology as structure of state collapse.

**Information Engine (ENG3)**:
- **Governs**: information, encoding, memory, and entanglement
- **Outputs**: information topology, encoding modes, entanglement maps, probability lattice

**INF13_CollapseTopology**: structure of state collapse -- how information states collapse from superposition to definite states.

**Collapse topology model**:
- **State space**: the space of all possible information states
- **Collapse paths**: paths from superposition to definite states
- **Collapse conditions**: conditions that trigger collapse
- **Collapse topology**: the topological structure of collapse paths

**Collapse laws**:
- `COLLAPSE != DESTRUCTION`: collapse reduces superposition to a definite state; it does not destroy information
- `TOPOLOGY != GEOMETRY**: topology studies connectivity; geometry studies distances
- `INFORMATION != PHYSICAL**: information collapse is an AMOS_MODEL; it is not a physics claim about quantum collapse

**Mapping protocol**:
1. **Define state space**: define the space of possible information states
2. **Identify collapse paths**: identify paths from superposition to definite states
3. **Identify collapse conditions**: identify conditions that trigger collapse
4. **Map topology**: map the topological structure of collapse paths
5. **Record**: record with provenance and epistemic class

### Epistemic Boundary

Information collapse topology is an AMOS_MODEL. It does not prove collapse is physical, that the topology is complete, or that collapse paths are exhaustive.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## Validation Gates

- **G1 (Law of Law)**: No unresolved contradictions within the skill's scope.
- **G2 (Epistemic class)**: All claims labeled SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL — never claim beyond evidence.
- **G3 (Provenance)**: Source path recorded for

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-information-collapse-topology_MOC]]

## Examples

- **Scenario**: When measuring entropy and lacunarity: information content and gaps
  - **Input**: A query matching this skill's domain (info)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When analyzing information collapse topology and structure
  - **Input**: A query matching this skill's domain (info)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When controlling information exposure and disclosure
  - **Input**: A query matching this skill's domain (info)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the info domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-information-theory-master` — routes to this skill when info specialization is needed
- **Peers**: Other skills in the `info` domain may be composed in sequence
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

- For generic information analysis outside the information theory framework
- To claim empirical validation of entropy or complexity theories
- As a substitute for domain-specific information or complexity evidence
- Outside information theory domain reasoning

## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `` — skill Map of Content
- `amos-information-theory-master` — parent skill
- `` — corresponding workflow
- `amos-information-collapse-topology-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-information-collapse-topology
node_type: skill
path: 07_SKILLS/amos-information-collapse-topology/[[SKILL]].md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
