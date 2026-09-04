---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Logic Kernel
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

# Deterministic Logic Kernel

> [!abstract] Kernel Specification
> Defines the core deterministic inference engine for AMOS: logical objects, evaluation rules, contradiction handling, entailment protocols, and non-monotonic consequence management. This is the AMOS reasoning/spec pattern for propositional and first-order logic operations — it is **not** a claim that AMOS OS deploys this as a live runtime (per AGENTS.md invariant 4).

---

## 1. Purpose

The Deterministic Logic Kernel provides:

- A formal substrate for propositional and restricted first-order inference
- Normalization of equivalent logical expressions under supported input forms
- Explicit contradiction preservation rather than silent repair
- Entailment tracking with provenance and scope discipline
- Non-monotonic retraction and cascading consequence management

This kernel is referenced by [[02_KERNEL/DETERMINISTIC_LOGIC_KERNEL|02_KERNEL Deterministic Logic Kernel]] (the canonical specification in `02_KERNEL/`). This file provides the knowledge-layer operational profile.

---

## 2. Core Logical Objects

| Object | Symbol | Definition |
| :--- | :--- | :--- |
| **Atom** | $p, q, r$ | Indivisible propositions with a truth-value assignment |
| **Negation** | $\lnot p$ | Classical complement; if $p$ is TRUE, $\lnot p$ is FALSE |
| **Conjunction** | $p \land q$ | TRUE iff both $p$ and $q$ are TRUE |
| **Disjunction** | $p \lor q$ | TRUE iff at least one of $p, q$ is TRUE |
| **Implication** | $p \rightarrow q$ | Equivalently $\lnot p \lor q$; material conditional |
| **Bottom** | $\bot$ | Contradiction / unsatisfiable; always FALSE in classical fragments |
| **Paradox** | $\pi$ | Explicit paradox state; preserved rather than collapsed |

### 2.1 Logic Modes

| Mode | Description | Validity |
| :--- | :--- | :--- |
| **Positive** | Only atoms and conjunctions | Fragment-verified |
| **Negative** | Negation introduced | Requires contradiction tracking |
| **Zero** | Identity / vacuous cases | Edge-case coverage |
| **Dual** | Classical two-valued | Fully supported |
| **Multi** | Multi-valued / fuzzy extension | Scope-restricted |
| **Meta** | Reasoning about reasoning | Control-plane gated |

### 2.2 Convergence and Divergence

- **Convergence**: Inference sequence terminates in a unique normal form for given premises/mode
- **Divergence**: Sequence cycles or fails to terminate; detected via cycle detection in proof trail assembly

---

## 3. Invariants

| ID | Invariant | Enforcement |
| :--- | :--- | :--- |
| **LK-01** | Normalization is deterministic for equivalent supported inputs | Canonical form uniqueness check |
| **LK-02** | Contradiction is preserved explicitly, never silently repaired | Bottom/Paradox states never collapsed without authority |
| **LK-03** | Syntactic normalization is distinguished from semantic entailment | Two-phase evaluation: normalize → then check entailment |
| **LK-04** | Classical truth is not inferred from unsupported meta-logic operators | Mode gate: meta-logic outputs carry `PROPOSAL` class |
| **LK-05** | Propositional behavior is used only within its verified fragment | Scope check: fragment boundary enforced at premise admission |
| **LK-06** | No state promotion occurs without valid provenance closure | Proof trail required for every entailment claim |

These invariants are consistent with AMOS core law ordering: $\text{INTEGRITY} > \text{COMPLETENESS} > \text{FLUENCY}$ (M01).

---

## 4. Contradiction Management

### 4.1 Explicit Contradiction States

A proposition and its negation may coexist as an explicit contradiction state: $\text{CONTRADICTION}(p) \iff p \land \lnot p$ both carry SUPPORTED truth-values. The kernel does **not** resolve this to $\bot$ automatically — the contradiction is flagged with metadata ($p, \lnot p$, sources, timestamp), downstream consumers receive the explicit state, and resolution requires higher-authority rules. Without authority, the kernel emits `UNKNOWN/GAP`.

### 4.2 Contradiction Detection Pipeline

Contradiction detection: (1) existence check — is $\lnot p$ already supported? (2) provenance compare — are $p$ and $\lnot p$ from independent sources? (3) flag contradiction state (do not auto-resolve), (4) escalate to control-plane or quarantine.

### 4.3 Bottom vs Paradox

- **Bottom** ($\bot$): Classical contradiction, resolvable within the logic fragment
- **Paradox** ($\pi$): Self-referential or undecidable; preserved as a first-class state and never silently eliminated

---

## 5. Entailment Rules

### 5.1 Entailment Claim Requirements

An entailment claim $\Gamma \vdash \phi$ requires:

1. A premise set $\Gamma = \{p_1, p_2, \ldots, p_n\}$ with valid provenance
2. An admitted inference rule $r$ (see §5.2)
3. An applicable logic fragment (mode and scope declaration)
4. A proof trail $\pi$ connecting $\Gamma$ to $\phi$

### 5.2 Admitted Inference Rules

| Rule | Form | Class |
| :--- | :--- | :--- |
| Modus Ponens | $p, p \rightarrow q \vdash q$ | Classical |
| Modus Tollens | $\lnot q, p \rightarrow q \vdash \lnot p$ | Classical |
| Hypothetical Syllogism | $p \rightarrow q, q \rightarrow r \vdash p \rightarrow r$ | Classical |
| Conjunction Elimination | $p \land q \vdash p$ | Classical |
| Disjunction Introduction | $p \vdash p \lor q$ | Classical |
| Contradiction Introduction | $p, \lnot p \vdash \bot$ | Classical |
| Default Reasoning | $\text{ABNORMAL}(p) \text{ not shown} \vdash p$ (defeasible) | Non-Monotonic |
| Belief Revision (AGM) | $K * p = \text{Cn}(K \cup \{p\}) \setminus \text{inconsistencies}$ | Non-Monotonic |

### 5.3 Proof Trail Formalization

A valid proof trail $\pi$ satisfies:

$$\pi = \langle (p_1, r_1, p_2), (p_2, r_2, p_3), \ldots, (p_{n-1}, r_{n-1}, p_n) \rangle$$

where:

- Each $p_i$ is a supported proposition or premise
- Each $r_i$ is an admitted inference rule
- $p_n = \phi$ (the conclusion)
- No $p_i$ has been retracted or placed in `QUARANTINED` status
- Scope and regime of every premise are compatible with the conclusion

---

## 6. Non-Monotonic Consequence Management

### 6.1 Retraction Protocol

When a premise is retracted (contradiction detected, evidence stale, authority revoked): (1) identify dependents via graph traversal, (2) classify impact as direct vs transitive, (3) retract dependent subtree only (M18), (4) quarantine affected claims or mark `UNKNOWN/GAP`, (5) notify downstream agents/state.

### 6.2 Minimal Retraction Scope (M18 Enforcement)

- Only the **dependent closure** of the retracted premise is affected
- Sibling claims sharing premises but not dependent on the retracted one are **preserved**
- If a claim has **multiple independent proof trails**, only trails containing the retracted premise are invalidated; the claim remains valid if at least one independent trail survives

---

## 7. Failure Modes

| Failure | Detection | Recovery |
| :--- | :--- | :--- |
| Invalid proof trail | Premise validation fails | Output `UNKNOWN/GAP`; no promotion |
| Circular dependency | Cycle detection in trail | Reject inference; log circular dependency |
| Stale premise | Freshness check | Force revalidation; mark dependents `QUARANTINED` |
| Scope mismatch | Fragment compatibility check | Reject inference; log scope conflict |
| Divergent normalization | Termination check | Flag as unsupported input; escalate |

---

## 8. Integration Points

| Interface | Direction | Contract |
| :--- | :--- | :--- |
| [[02_KERNEL/DETERMINISTIC_LOGIC_KERNEL\|02_KERNEL Logic Spec]] | Read | Canonical axiom/inference definitions |
| [[11_KNOWLEDGE/kernel/COGNITION_KERNEL\|COGNITION_KERNEL]] | Write | Logical operations supply the symbolic plane for cognitive processing |
| [[11_KNOWLEDGE/kernel/AMOS_CONTROL_SYSTEMS_KERNEL\|AMOS_CONTROL_SYSTEMS_KERNEL]] | Read | Invariant enforcement order feeds control-system priority |
| [[11_KNOWLEDGE/kernel/AMOS_SIMULATION_KERNEL\|AMOS_SIMULATION_KERNEL]] | Write | Entailment results used in counterfactual evaluation |
| [[11_KNOWLEDGE/kernel/AMOS_PROBABILITY_STATISTICS_KERNEL\|AMOS_PROBABILITY_STATISTICS_KERNEL]] | Read/Write | Probabilistic rules interface with certainty factors |
| [[01_CANON/01_CORE_LAWS\|AMOS_CORE_LAWS]] | Read | Axiom definitions; immutable premises |
| [[03_CONTROL_PLANE\|CONTROL_PLANE]] | Write | Inference results submitted for authority gating |

---

```RSCF-NODE
node_id: logic_kernel_knowledge_spec
node_type: kernel_specification
domain: 11_KNOWLEDGE/kernel
claim_class: AMOS_MODEL
confidence_ceiling:
  contradiction_management: high
  entailment_formalization: high
  non_monotonic_retraction: high
falsifiers:
  - Contradiction state is silently resolved without authority
  - Entailment claim accepted without valid proof trail
  - Non-monotonic retraction affects siblings outside dependent closure
```

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]] · [[02_KERNEL/DETERMINISTIC_LOGIC_KERNEL|02_KERNEL Logic Spec]] · [[11_KNOWLEDGE/kernel/COGNITION_KERNEL|COGNITION_KERNEL]] · [[11_KNOWLEDGE/kernel/AMOS_SIMULATION_KERNEL|AMOS_SIMULATION_KERNEL]] · [[11_KNOWLEDGE/kernel/AMOS_PROBABILITY_STATISTICS_KERNEL|AMOS_PROBABILITY_STATISTICS_KERNEL]]

______________________________________________________________________

**MOC:** [[11_KNOWLEDGE/kernel/KERNEL_MOC|KERNEL_MOC]]
