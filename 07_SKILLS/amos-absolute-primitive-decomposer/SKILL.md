---
title: SKILL
type: skill
name: amos-absolute-primitive-decomposer
description: Absolute Primitive Decomposer — runtime and OS capability. Use when runtime reasoning, OS kernel operations, or adaptive stability. Use when amos-os-runtime-master routes to this specialized capability.
parent_skill: amos-os-runtime-master
domain: runtime
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-absolute-primitive-decomposer]
---


# Absolute Primitive Decomposer

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-os-runtime-master`
- **Domain**: runtime
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Runtime and OS engine for Absolute Primitive Decomposer

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

- **runtime.decompose_to_primitives**: Decompose an input concept or structure into the 19 irreducible Absolute Logic primitives (Existence, NonExistence, Causality, Temporal, Informational, Topological, Identity, Convergence, Divergence, Paradox, PositiveLogic, NegativeLogic, ZeroLogic, DualLogic, MultiLogic, MetaLogic, SupraLogic, AntiLogic, NullLogic) while preserving non-mappable residue.
- **runtime.evaluate_interaction_matrix**: Evaluate the 19x19 interaction matrix to determine the deterministic outcome when any two primitives interact, using category-based rules (Pattern, MetaPattern, Logic, MetaLogic).
- **runtime.detect_logic_collapse**: Detect logic collapse states (Dissolution via Paradox+AntiLogic, Driftless via zero derivatives, TerminalQuiet via NullLogic dominance) that indicate structural reasoning failure.
- **runtime.validate_primitive_mapping**: Validate primitive mappings for support, overreach, residue preservation, and epistemic labeling. Reject mappings that violate the 19x19 interaction matrix or claim empirical validity for AMOS_MODEL formalizations.
- **runtime.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **runtime.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **runtime.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: b635376a0788808e) for the full vault-sourced domain knowledge (7963 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Absolute Primitive Decomposition

The decomposer breaks any system into its irreducible atomic primitives.

**Decomposition law**: A primitive is atomic when it cannot be further decomposed without losing meaning. `Atomic(x) = NOT EXISTS y: Decompose(x, y) AND Meaningful(y)`

**8 Atomic Logic Units (ALUs)** from ULK:
1. Identity (A = A)
2. Distinction (A != NOT A)
3. Composition (A AND B -> C)
4. Negation (NOT A)
5. Implication (A -> B)
6. Existence (EXISTS A)
7. Universal (FORALL A)
8. Relation (A R B)

**7 Universal Meta-Laws (UMLs)**:
1. Law of Law (no unresolved contradictions)
2. Rule of 2 (at least 2 independent supports for any claim)
3. Rule of 4 (check 4 dimensions: scope, regime, evidence, falsifier)
4. Signal Fidelity Preservation
5. Structural Integrity
6. Provenance completeness
7. Scope/regime compliance

**Decomposition protocol**:
1. Identify the system's declared structure
2. Decompose into constituent parts
3. For each part, check if it can be further decomposed
4. If yes, repeat; if no, the part is atomic
5. Record the decomposition tree with provenance

### Epistemic Boundary

Absolute primitive decomposition is an analytical method. It does not prove the primitives are truly atomic in all possible frameworks, only that they are atomic within the declared framework.

## Failure Modes
- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## Validation Gates

---
**Links:** [[07_SKILLS_MOC]]
