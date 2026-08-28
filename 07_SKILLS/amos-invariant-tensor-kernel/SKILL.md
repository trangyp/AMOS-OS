---
title: SKILL — Amos Invariant Tensor Kernel
type: skill
source: 07_SKILLS/amos-invariant-tensor-kernel
name: amos-invariant-tensor-kernel
description: Invariant Tensor Kernel — formal verification capability. Use when formal verification, symbolic execution, proof checking, or mathematical reasoning. Use when amos-formal-engines-master routes to this specialized capability. Do not use for generic tasks outside formal domain.
parent_skill: amos-formal-engines-master
domain: formal
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/formal-engines
- rscf/source_claim
- hml/h
- epistemic/source_claim
- amos_os
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
rscf_state: SOURCE_CLAIM
hml_level: H
gmef_gates:
- L0_integrity
- L1_epistemic
- L2_provenance
- L3_dependency
- L5_scope
- L7_authority
- L22_replayability
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance:
- L0
- L1
- L2
- L3
- L4
- L5
- L7
- L16
- L17
- L18
- L19
- L22
license: MIT
steward: Trang Phan
---

# Invariant Tensor Kernel

## Identity

Origin architect: **Trang Phan**. Domain: formal. Parent: amos-formal-engines-master. Epistemic class: SOURCE_CLAIM. H/M/L: H.
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

- **invariant_tensor.verify_proof**: Verify formal proofs against axioms, inference rules, and consistency constraints
- **invariant_tensor.check_soundness**: Check soundness and completeness of formal systems under test
- **invariant_tensor.propagate_constraints**: Propagate constraints through the formal system and detect unsatisfiable cores
- **invariant_tensor.validate_invariant**: Validate invariants hold under all specified operating conditions
- **invariant_tensor.detect_contradiction**: Detect contradictions and derive minimal conflict explanations

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 883b999b85453e00) for the full vault-sourced domain knowledge (8591 chars).
- **invariant_tensor.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **invariant_tensor.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **invariant_tensor.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Invariant Tensor Kernel

The Cognitive Organism OS defines invariant tensors as structural properties that must hold across all states.

**Invariant types**:
- **Conservation invariants**: quantities that must be conserved (e.g., provenance completeness)
- **Symmetry invariants**: properties that must be symmetric (e.g., scope-regime consistency)
- **Boundary invariants**: properties that must hold at boundaries (e.g., admission gates)
- **Topological invariants**: properties that must hold under continuous deformation (e.g., structural integrity)

**Tensor kernel operations**:
1. **Declare**: declare an invariant with its type, scope, and validation rule
2. **Check**: verify the invariant holds in the current state
3. **Trace**: trace the invariant through state transitions
4. **Repair**: if the invariant is violated, trigger repair
5. **Record**: log invariant checks and violations

**Law**: `Invariant violation -> repair or block`. No state transition is permitted that violates a declared invariant.

### Epistemic Boundary

Invariant tensor kernel is a structural construct. It does not prove all invariants are known, that invariant checking is complete, or that violations are always detectable.

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
- **G6 (Failure mode)**: On validation failure, downgrade confidence, fl

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-invariant-tensor-kernel_MOC]]

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

- **Parent**: `amos-formal-engines-master` — routes to this skill when formal specialization is needed
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


## Do not use

- For generic mathematical analysis outside the formal verification framework
- To claim physical quantum mechanics predictions (AMOS_MODEL only)
- As a substitute for domain-specific numerical or optimization evidence
- Outside formal/math domain reasoning

## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `[[amos-invariant-tensor-kernel_MOC]]` — skill Map of Content
- `amos-formal-engines-master` — parent skill
- `[[amos-invariant-tensor-kernel-workflow]]` — corresponding workflow
- `amos-invariant-tensor-kernel-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-invariant-tensor-kernel
node_type: skill
path: 07_SKILLS/amos-invariant-tensor-kernel/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
