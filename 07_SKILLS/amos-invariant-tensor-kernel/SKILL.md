---
title: SKILL
type: skill
name: amos-invariant-tensor-kernel
description: Invariant Tensor Kernel — formal verification capability. Use when formal verification, symbolic execution, proof checking, or mathematical reasoning. Use when amos-formal-engines-master routes to this specialized capability.
parent_skill: amos-formal-engines-master
domain: formal
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-invariant-tensor-kernel]
---


# Invariant Tensor Kernel

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-formal-engines-master`
- **Domain**: formal
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Formal reasoning engine for Invariant Tensor Kernel

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
