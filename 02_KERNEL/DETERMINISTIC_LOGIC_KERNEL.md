---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Deterministic Logic Kernel
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# Deterministic Logic Kernel Specification

> [!ABSTRACT] Kernel Specification
> Defines the core deterministic inference engine that enforces AMOS axioms M01–M20 on every reasoning step, manages proof trails, handles non-monotonic consequence retraction, and ensures that no state promotion occurs without valid provenance closure.

---

## 1. Core Axiom Enforcement (M01–M20)

The Deterministic Logic Kernel verifies all inference steps against the 20 fundamental AMOS invariants:

| ID | Invariant | Enforcement |
| :--- | :--- | :--- |
| **M01** | `INTEGRITY > COMPLETENESS > FLUENCY > SPEED > TOKEN_SAVINGS` | Priority ordering hard-coded in optimization gates; no bypass permitted |
| **M04** | `SOURCE_CLAIM != VERIFIED` | Classification check at promotion boundary; `SOURCE_CLAIM` never auto-promotes |
| **M06** | `REPOSITORY_PRESENCE != RUNTIME` | File existence ≠ live execution; both must be independently validated |
| **M10** | `TOOL_ACCESS != TOOL_PERMISSION` | Capability registry checked separately from authorization token |
| **M11** | `AGENT_NAME != CAPABILITY` | Identity lookup decoupled from capability assertion |
| **M12** | `AGENT_CAPABILITY != AUTHORITY` | Capability provenance checked against authority grant chain |
| **M14** | `TEST_PASS != UNIVERSAL_PROOF` | Test scope and regime must be explicitly declared |
| **M15** | `MULTIPLE_COPIES != INDEPENDENT_EVIDENCE` | Source ancestry checked; descendant copies do not increase evidence weight |
| **M18** | `FAILED_PREMISE_INVALIDATES_DEPENDENTS_ONLY` | Graph traversal limited to dependent closure; non-dependent siblings unaffected |
| **M20** | `IRREVERSIBLE_ACTION_REQUIRES_STRONGER_GOVERNANCE` | Irreversible flag triggers elevated authority threshold |

Additional invariants enforced:

| ID | Invariant |
| :--- | :--- |
| **M02** | `UNKNOWN/GAP != PASS` |
| **M03** | `MODEL != OBSERVATION` |
| **M05** | `IMPLEMENTED != VALIDATED` |
| **M07** | `CANON != IMPLEMENTATION` |
| **M08** | `MEMORY != KNOWLEDGE` |
| **M09** | `KNOWLEDGE != STATE` |
| **M13** | `PROPOSAL != COMMIT` |
| **M16** | `FAST_PATH != SKIP_VALIDATION` |
| **M17** | `LOCAL_GAIN_CANNOT_BREAK_HIGHER_SCALE_INTEGRITY` |
| **M19** | `STALE_EVIDENCE_REQUIRES_REVALIDATION` |

---

## 2. Evaluation Rule

If an inference step cannot produce a valid proof trail connecting its conclusion to admitted premises in `01_CANON` or verified observations in `11_KNOWLEDGE`, the Kernel forces the output class to `UNKNOWN/GAP` and halts state promotion.

### 2.1 Proof Trail Requirements

A valid proof trail $\pi$ must satisfy:

$$\pi = \langle p_1, p_2, \ldots, p_n \rangle \quad \text{where} \quad \forall i \in \{1, \ldots, n\}:$$

1. Each premise $p_i$ is either:
   - An axiom from `01_CANON` (immutable, `VERIFIED` epistemic class), or
   - A derived claim with a valid antecedent proof trail ending in canon or observation
2. Every inference rule $r_i$ connecting $p_i$ to $p_{i+1}$ is an admitted rule from the meta-logic catalog (`02_KERNEL/01_META_LOGIC/`)
3. No premise in $\pi$ has been retracted or placed in `QUARANTINED` status since last use
4. The scope and regime of every premise is compatible with the conclusion's declared scope and regime

### 2.2 Evaluation Pipeline

```text
INFERENCE STEP SUBMITTED
        │
        ▼
┌─────────────────────────┐
│ 1. AXIOM CHECK (M01-M20)│  ← Verify no invariant violation
└────────────┬────────────┘
             │ PASS
             ▼
┌─────────────────────────┐
│ 2. PREMISE VALIDATION   │  ← Verify all premises have valid provenance
└────────────┬────────────┘
             │ PASS
             ▼
┌─────────────────────────┐
│ 3. RULE ADMISSION CHECK │  ← Verify inference rule is in admitted catalog
└────────────┬────────────┘
             │ PASS
             ▼
┌─────────────────────────┐
│ 4. PROOF TRAIL ASSEMBLY │  ← Build complete dependency chain
└────────────┬────────────┘
             │ PASS
             ▼
┌─────────────────────────┐
│ 5. SCOPE/REGIME CHECK   │  ← Verify compatibility across all premises
└────────────┬────────────┘
             │ PASS
             ▼
┌─────────────────────────┐
│ 6. STATE PROMOTION      │  ← Output class assigned; RSCF node created
└─────────────────────────┘
```

If any step fails, the kernel emits:

```yaml
inference_result:
  status: HALTED
  failure_step: <step_number>
  failure_reason: <string>
  output_class: UNKNOWN/GAP
  affected_dependents: []
  provenance: <proof_trail_partial>
```

---

## 3. Non-Monotonic Consequence Management

When a premise is retracted (e.g., contradiction detected, evidence stale, authority revoked), the kernel must manage cascading consequences:

### 3.1 Retraction Protocol

```text
PREMISE RETRACTED
        │
        ▼
┌─────────────────────────┐
│ 1. IDENTIFY DEPENDENTS  │  ← Graph traversal from retracted node
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ 2. CLASSIFY IMPACT      │  ← Direct vs transitive dependents
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ 3. RETRACT DEPENDENTS   │  ← Only dependent subtree affected (M18)
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ 4. QUARANTINE OR GAP    │  ← Affected claims → QUARANTINED or UNKNOWN/GAP
└────────────┬────────────┘
             │
             ▼
┌─────────────────────────┐
│ 5. NOTIFY DEPENDENTS    │  ← Downstream agents/state notified
└─────────────────────────┘
```

### 3.2 Minimal Retraction Scope

The kernel enforces minimal retraction scope:

- Only the **dependent closure** of the retracted premise is affected
- Sibling claims sharing some premises but not dependent on the retracted one are **preserved**
- If a claim has **multiple independent proof trails**, only trails containing the retracted premise are invalidated; the claim remains valid if at least one independent trail survives

---

## 4. Admitted Inference Rules

The kernel maintains a catalog of admitted inference rules. Each rule must declare:

```yaml
inference_rule:
  rule_id: "IR-001"
  name: "Modus Ponens"
  form: "P → Q, P ⊢ Q"
  soundness: "classical_propositional"
  scope_restriction: "none"
  authority_required: "kernel_internal"
  admission_status: ADMITTED
  provenance:
    - "01_CANON/01_CORE_LAWS"
```

Rule classes:

| Class | Examples | Authority Level |
| :--- | :--- | :--- |
| **Classical** | Modus Ponens, Modus Tollens, Hypothetical Syllogism | Kernel internal |
| **Monotonic** | Universal Instantiation, Conjunction Introduction | Kernel internal |
| **Non-Monotonic** | Default Reasoning, Circumscription, Belief Revision | Control-plane gated |
| **Probabilistic** | Bayesian Update, Maximum Entropy | Scope-restricted |
| **Analogical** | Structural Mapping, Case-Based Reasoning | High-stakes prohibited |

---

## 5. Integration Points

| Interface | Direction | Contract |
| :--- | :--- | :--- |
| **01_CANON** | Read | Axiom and law definitions; immutable premises |
| **02_KERNEL/01_META_LOGIC** | Read | Admitted inference rule catalog |
| **03_CONTROL_PLANE** | Write | Inference results submitted for authority gating |
| **04_RUNTIME** | Read/Write | Session state; causal epoch tags applied to proof trails |
| **10_MEMORY** | Write | Proof trails persisted as episodic/procedural memory |
| **11_KNOWLEDGE** | Read/Write | Derived claims promoted to knowledge; knowledge retracted triggers retraction protocol |
| **17_OBSERVABILITY** | Write | Inference traces logged for audit |

---

## 6. Failure Modes

| Failure | Detection | Recovery |
| :--- | :--- | :--- |
| **Invalid proof trail** | Evaluation step 2 or 3 fails | Output `UNKNOWN/GAP`; no promotion |
| **Circular dependency** | Proof trail cycle detection | Reject inference; log circular dependency |
| **Stale premise** | Freshness check at step 1 | Force revalidation; mark dependents `QUARANTINED` |
| **Authority violation** | M12 check at step 1 | Reject inference; escalate to control plane |
| **Scope mismatch** | Step 5 scope/compatibility check | Reject inference; log scope conflict |

---

## 7. Cross-Vault References

- [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]]
- [[02_KERNEL/KERNEL_README|KERNEL_README]]
- [[02_KERNEL/01_META_LOGIC/01_META_LOGIC_MOC|META_LOGIC_MOC]]
- [[01_CANON/01_CORE_LAWS/AMOS_CORE_LAWS|AMOS_CORE_LAWS]]
- [[04_RUNTIME/CAUSAL_CONCURRENCY_MVCC|CAUSAL_CONCURRENCY_MVCC]]
- [[03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT|CONTROL_PLANE_CONTRACT]]

---

```RSCF-NODE
node_id: deterministic_logic_kernel_spec
node_type: kernel_specification
domain: 02_KERNEL
claim_class: AMOS_MODEL
confidence_ceiling:
  axiom_enforcement: high
  non_monotonic_management: high
  integration_coverage: high
falsifiers:
  - An admitted inference rule produces an invalid conclusion under known conditions
  - Non-monotonic retraction fails to retract a dependent closure
  - Proof trail assembly admits a premise with unknown provenance
```
