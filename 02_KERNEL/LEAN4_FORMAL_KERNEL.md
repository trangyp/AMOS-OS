---
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
title: Lean 4 Formal Kernel
source: 02_KERNEL/02_COGNITION
type: engine_specification
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 02_KERNEL/LEAN4_INVARIANT_PROVER_ENGINE
    - 02_KERNEL/LEAN4_PROOF_VERIFICATION_LEDGER
    - 22_RESEARCH/01_MATHEMATICS/AMOS_137_MATH_REGISTRY
    - 02_KERNEL/02_KERNEL_MOC
  scope: lean4_formal_kernel_spec
tags:
  - amos-os
  - 02_kernel
  - lean4
  - formal-verification
  - engine
---

# Lean 4 Formal Kernel

> **Origin Architect / Steward:** Trang Phan
> **AMOS_CORE Target:** `v4.4`
> **Epistemic Class:** `AMOS_MODEL`
> **Conclusion Class:** `DERIVED`

---

## 1. Architectural Scope

The **Lean 4 Formal Kernel** is the AMOS-side specification of a Calculus-of-Inductive-Constructions (CIC) proof engine used to verify invariants before they are admitted into the AMOS knowledge base. It exists as a *model* of a formal verification pipeline, not as a deployed compiler or proof assistant. Actual proof construction and checking are delegated to an external Lean 4 toolchain that is governed by the contracts below.

```text
FORMAL_MODEL != RUNTIME_VERIFIER
PROVEN_IN_LEAN != AMOS_CANONICAL
DOCUMENTED != IMPLEMENTED
```

---

## 2. Core Components

| Component | Plane | Role |
|-----------|-------|------|
| [[02_KERNEL/LEAN4_INVARIANT_PROVER_ENGINE|LEAN4_INVARIANT_PROVER_ENGINE]] | 02_KERNEL/02_COGNITION | Constructs invariant propositions and tactic scripts. |
| [[02_KERNEL/LEAN4_PROOF_VERIFICATION_LEDGER|LEAN4_PROOF_VERIFICATION_LEDGER]] | 02_KERNEL/02_COGNITION | Records proof status, elaboration time, and cryptographic proof hash. |
| [[22_RESEARCH/01_MATHEMATICS/AMOS_137_MATH_REGISTRY|AMOS_137_MATH_REGISTRY]] | 22_RESEARCH/01_MATHEMATICS | Master registry of formalized equations and invariants. |

---

## 3. Governing Invariants

- **INV-L4FK-001 (Model Boundary):** This artifact is an `AMOS_MODEL` of a formal kernel; it does not by itself execute proofs.
- **INV-L4FK-002 (Proof Closure):** Only theorems with zero `sorry` placeholders and stated tactic closures are recorded as `VERIFIED`.
- **INV-L4FK-003 (Constructive Preference):** Classical choice axioms are not invoked without explicit declaration and scope limitation.
- **INV-L4FK-004 (Hash Anchoring):** Every verified proof is bound to a `BLAKE3/SHA-256` digest of its source terms and dependencies.

---

## 4. Inputs & Outputs

- **Input:** `FORMAL_KERNEL_INPUT{proposition, dependencies[], tactic_hints[], confidence_ceiling}`
- **Output:** `FORMAL_KERNEL_OUTPUT{status, proof_hash, elaboration_time, sorry_count, dependency_closure}`

---

## 5. Safety & Epistemic Firewalls

- `FORMAL_PROOF != EMPIRICAL_VALIDATION` — logical correctness does not imply runtime correctness.
- `VERIFIED_LEMMA != UNIVERSAL_TRUTH` — a proof is valid within the stated axioms and type theory.

---

## 6. Navigation

- [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]] — Kernel master map
- [[02_KERNEL/KERNEL_README|KERNEL_README]] — Kernel readme
- [[01_CANON/01_CORE_LAWS/L22_ATOMIC_REASONING|L22_ATOMIC_REASONING]] — atomic reasoning law
- [[22_RESEARCH/01_MATHEMATICS/AMOS_137_MATH_REGISTRY|AMOS_137_MATH_REGISTRY]] — math registry
