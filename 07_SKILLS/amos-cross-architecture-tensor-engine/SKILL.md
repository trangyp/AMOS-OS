---
title: SKILL
type: skill
source: 07_SKILLS/amos-cross-architecture-tensor-engine
name: amos-cross-architecture-tensor-engine
description: Cross Architecture Tensor Engine — formal verification capability. Use when formal verification, symbolic execution, proof checking, or mathematical reasoning. Use when amos-formal-engines-master routes to this specialized capability.
parent_skill: amos-formal-engines-master
domain: formal
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-cross-architecture-tensor-engine, canon/skill]
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: "1.1.0"
---


# Cross Architecture Tensor Engine

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-formal-engines-master`
- **Domain**: formal
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Formal reasoning engine for Cross Architecture Tensor Engine

## When to Use

- When verifying formal proofs against axioms and inference rules
- When checking soundness and completeness of formal systems
- When propagating constraints and detecting unsatisfiable cores
- When validating invariants under all operating conditions
- When the parent skill (`amos-formal-engines-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **cross_architecture.verify_proof**: Verify formal proofs against axioms, inference rules, and consistency constraints
- **cross_architecture.check_soundness**: Check soundness and completeness of formal systems under test
- **cross_architecture.propagate_constraints**: Propagate constraints through the formal system and detect unsatisfiable cores
- **cross_architecture.validate_invariant**: Validate invariants hold under all specified operating conditions
- **cross_architecture.detect_contradiction**: Detect contradictions and derive minimal conflict explanations

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 3f6468869089682d) for the full vault-sourced domain knowledge (8524 chars).
- **cross_architecture.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **cross_architecture.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **cross_architecture.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/trang/trang_amos_reality_architecture_master_max_detail.md` (content_hash: da2bc7dc1c2ceeeb) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Cross-Architecture Tensor Engine

From Trang Reality Architecture: Cross-Architecture Tensor Engine for universal mapping across architectures.

**Tensor equation** (AMOS_MODEL):
```
TENSOR = (O × C × S × V) / (D + X)
```
- O = ontology, C = coherence, S = structure, V = validation
- D = drift, X = contradiction

**Required components**:
- **Tensor transformation rules**: rules for transforming tensors across architectures
- **Tensor inheritance**: inheritance rules for tensor properties
- **Tensor interaction algebra**: algebra for tensor interactions
- **Tensor collapse conditions**: conditions under which tensors collapse

**Cross-architecture laws**:
- `TENSOR != MATRIX`: a tensor is a typed multi-dimensional structure; a matrix is a 2D array
- `CROSS != MERGE`: cross-architecture composition connects tensors; it does not merge them
- `ARCHITECTURE != IMPLEMENTATION`: the tensor engine works at the architecture level; implementation is separate

### Epistemic Boundary

Cross-architecture tensor engine is an AMOS_MODEL. It does not prove all architectures are tensor-compatible, that the tensor equation is empirically validated, or that cross-architecture mapping is always possible.

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
- **G5

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-cross-architecture-tensor-engine_MOC]]

## Examples

- **Scenario**: When verifying formal proofs against axioms and inference rules
  - **Input**: A query matching this skill's domain (formal)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When checking soundness and completeness of formal systems
  - **Input**: A query matching this skill's domain (formal)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When propagating constraints and detecting unsatisfiable cores
  - **Input**: A query matching this skill's domain (formal)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the formal domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `[[amos-formal-engines-master]]` — routes to this skill when formal specialization is needed
- **Peers**: Other skills in the `formal` domain may be composed in sequence
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
- `[[amos-cross-architecture-tensor-engine_MOC]]` — skill Map of Content
- `[[amos-formal-engines-master]]` — parent skill
- `[[amos-cross-architecture-tensor-engine-workflow]]` — corresponding workflow
- `[[amos-cross-architecture-tensor-engine-agent]]` — corresponding agent

