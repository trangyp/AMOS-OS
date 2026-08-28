---
title: SKILL — Amos Information Operator Engine
type: skill
source: 07_SKILLS/amos-information-operator-engine
name: amos-information-operator-engine
description: Information Operator Engine — info capability. Use when executing the
  core capability within this domain. Use when amos-information-theory-master routes
  to this specialized capability.
parent_skill: amos-information-theory-master
domain: info
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/information-theory
- canon-group/tech-ai
- topic/information
- rscf/epistemic
- rscf/T-topology
- rscf/C-constraint
- rscf/type-system
- sota/progressive-disclosure
- sota/anti-patterns
- amos_os
- amos-information-operator-engine
- capability/execution
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
---







# Information Operator Engine

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

- **information_operator.measure_entropy**: Measure entropy and lacunarity: information content, gaps, and structure
- **information_operator.analyze_topology**: Analyze information collapse topology: how information condenses and structures
- **information_operator.control_exposure**: Control information exposure: what is revealed, to whom, and under what conditions
- **information_operator.map_geometry**: Map information geometry: manifolds, distances, and projections in information space

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 660fea16ecf8df88) for the full vault-sourced domain knowledge (8890 chars).
- **information_operator.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **information_operator.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **information_operator.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/amos-general/A/Universe/AMOS_UNIVERSE_OS_FULL_BUNDLE.md` (content_hash: c3aef595e3657ad7) (vault canon, SOURCE_CLAIM)
> **Additional source**: `_00_Cosmo brain/misc/R/REALITY GRAMMAR EQUATION v0.md` (content_hash: 907eaf846225a77b) (vault canon, SOURCE_CLAIM)

### Information Operator Engine

From Cosmo Brain Universe OS Full Bundle: P2_INFORMATION layer with InfoOperators and InfoGeometry modules. From Reality Grammar Equation: Information operators on information states.

**P2_INFORMATION layer modules**:
- **QLS (Quantum Logic Scaffold)**: foundational logic substrate
- **QCLA (Quantum Causality Layer Architecture)**: causal layer architecture
- **InfoOperators**: information operators on information states
- **InfoGeometry**: information geometry mapping

**Information operator model**:
- **Operators act on information states**: each operator transforms one information state to another
- **Typed operators**: operators are typed (input type, output type)
- **Composable operators**: operators can be composed (output of one feeds into another)
- **Reversible operators**: some operators are reversible (can be undone)

**Operator classes**:
- **Discrimination**: distinguish one piece of information from another
- **Interaction**: combine two pieces of information
- **Propagation**: propagate information through the system
- **Stabilization**: stabilize information against noise
- **Compression**: compress information while preserving structure
- **Synchronization**: synchronize information across components
- **Transformation**: transform information from one form to another
- **Selection**: select relevant information from a larger set

**Operator laws**:
- `OPERATOR != FUNCTION`: an operator is typed and composable; a function is a programming construct
- `INFORMATION_STATE != DATA**: an information state is typed and structured; data is raw
- `COMPOSITION != SEQUENCE**: composition is typed; sequence is ordered

### Epistemic Boundary

Information operator engine is an AMOS_MODEL. It does not prove all information processing is operator-based, that the 8 operator classes are exhaustive, or that composition is always safe.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrad

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-information-operator-engine_MOC]]

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


## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `[[amos-information-operator-engine_MOC]]` — skill Map of Content
- `amos-information-theory-master` — parent skill
- `[[amos-information-operator-engine-workflow]]` — corresponding workflow
- `amos-information-operator-engine-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-information-operator-engine
node_type: skill
path: 07_SKILLS/amos-information-operator-engine/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
