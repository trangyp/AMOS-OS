---
title: "SKILL — Amos Information Exposure Control"
type: skill
source: 07_SKILLS/amos-information-exposure-control
name: amos-information-exposure-control
description: Information Exposure Control — info capability. Use when executing the core capability within this domain. Use when amos-information-theory-master routes to this specialized capability.
parent_skill: amos-information-theory-master
domain: info
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-information-exposure-control, canon/skill]
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: "1.1.0"
---


# Information Exposure Control

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-information-theory-master`
- **Domain**: info
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Information theory engine for Information Exposure Control

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

- **information_exposure.measure_entropy**: Measure entropy and lacunarity: information content, gaps, and structure
- **information_exposure.analyze_topology**: Analyze information collapse topology: how information condenses and structures
- **information_exposure.control_exposure**: Control information exposure: what is revealed, to whom, and under what conditions
- **information_exposure.map_geometry**: Map information geometry: manifolds, distances, and projections in information space

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: e5b0b8a7a7332c2e) for the full vault-sourced domain knowledge (8923 chars).
- **information_exposure.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **information_exposure.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **information_exposure.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/amos-general/A/PROTECTED/AMOS_PROTECTED_KNOWLEDGE_TRAINING_CONTROL_ARCHITECTURE_MAX_DETAIL.md` (content_hash: 4e3fde2833882d11) (vault canon, SOURCE_CLAIM)
> **Additional source**: `_00_Cosmo brain/security/Bounded Intelligence Security™ (BIS™).md` (content_hash: 6258a1ebb7a6cc96) (vault canon, SOURCE_CLAIM)

### Information Exposure Control

From Cosmo Brain Protected Knowledge Training Control Architecture: Governed knowledge-exposure system with typed knowledge objects and semantic-origin lineage. From BIS: Bounded Intelligence Security.

**Exposure control architecture**:
- **Typed knowledge objects**: all knowledge is typed with exposure classification
- **Semantic-origin lineage**: every knowledge object has a semantic origin lineage
- **Origin equivalence classes**: knowledge objects grouped by origin equivalence
- **Information classification**: knowledge classified by exposure level
- **Least privilege**: exposure follows least privilege principle
- **Capability attenuation**: capabilities attenuated by exposure rules

**Exposure control laws**:
- `INTERNAL != EXTERNAL`: internal information is not external information; exposure rules differ
- `DECLARED != UNDECLARED`: only declared information can be exposed; undeclared exposure is a violation
- `SCOPE_BOUND`: exposure is valid only within declared scope and audience

**Anti-exfiltration**:
- **Output-only behavioral definition**: the system is defined by its outputs, not its internal state
- **Human-embedded final enforcement**: humans are the final enforcement layer
- **Ephemeral enforcement**: some enforcement is ephemeral (not persisted)

**Exposure accounting**:
- **Semantic transaction validation**: validate that transactions don't expose undeclared information
- **Multi-origin atomic reservations**: atomic reservations for multi-origin knowledge
- **Commit-time revalidation**: revalidate exposure at commit time
- **Provenance topology**: track exposure through provenance topology
- **Receiver-bound release**: release is bound to declared receivers

### Epistemic Boundary

Information exposure control is a security construct. It does not prove all exposure is controlled, that boundaries are always correct, or that violations are always detected.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag rout

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-information-exposure-control_MOC]]

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
- `[[amos-information-exposure-control_MOC]]` — skill Map of Content
- `amos-information-theory-master` — parent skill
- `[[amos-information-exposure-control-workflow]]` — corresponding workflow
- `amos-information-exposure-control-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-information-exposure-control
node_type: skill
path: 07_SKILLS/amos-information-exposure-control/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
