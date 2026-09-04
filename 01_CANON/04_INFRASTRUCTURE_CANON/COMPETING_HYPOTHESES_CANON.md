---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Competing Hypotheses Canon
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

# Competing Hypotheses Infrastructure Canon

> **Authoritative Canon Boundary**
>
> This document defines the canonical laws governing **Competing Hypotheses Preservation and Resolution** within AMOS Core v4.4.
>
> ```text
> PREMATURE CONVERGENCE == EPISTEMIC BIAS
> ABSENCE OF DISCRIMINATING EVIDENCE -> PRESERVE COMPETING STATE
> FLUENT PREFERENCE != DISCRIMINATING PROOF
> ACTION UNDER AMBIGUITY REQUIRES BOUNDED-REGRET SAFEGUARDS
> ```

---

## 1. Architectural Purpose & Problem Statement

Standard language models and heuristic engines suffer from premature collapse: when faced with ambiguous or multi-causal observations, they arbitrarily select one plausible explanation and discard alternatives, leading to confirmation bias and unrecoverable reasoning errors.

The **Competing Hypotheses Canon** mandates that whenever evidence supports multiple mutually incompatible explanations, AMOS OS must preserve the candidate set as an explicit `COMPETING` multi-state structure until discriminating evidence is obtained.

---

## 2. Canonical Laws of Competing Hypotheses

### Law CHC-01: Explicit Multi-State Retention
When multiple candidate models $\{H_1, H_2, \dots, H_m\}$ satisfy baseline admissibility without definitive refutation:
$$\text{State}(\text{HypothesisSet}) \leftarrow \text{COMPETING}(\{H_1, H_2, \dots, H_m\})$$
Arbitrary selection based on fluency, recency, or superficial plausibility is strictly prohibited.

### Law CHC-02: Uniform Falsification Standard
Every competitor in the set must be evaluated against identical falsification thresholds and evidence standards. Asymmetric skepticism is an epistemic integrity violation.

### Law CHC-03: Active Discriminating Probe Design
When a high-stakes decision depends on resolving competing hypotheses, the cognitive organism must formulate targeted investigative probes:
$$\text{Probe}(H_i, H_j) \implies \text{Experiment / Query whose outcome } O \text{ satisfies } P(O|H_i) \ne P(O|H_j)$$

### Law CHC-04: Bounded-Regret Action Governance
If an action must be executed while hypotheses remain `COMPETING`:
1. The decision must be tagged as conditional;
2. The chosen action must minimize maximum possible harm across all unrefuted competitors (minimax regret);
3. Rollback basins must be preserved for all viable alternatives.

---

## 3. Integration with the Cognitive Loop

```text
[OBSERVED AMBIGUITY]
         │
         ▼  Generate Plausible Explanations
[HYPOTHESIS ENSEMBLE: {H1, H2, ..., Hm}]
         │
         ▼  Evaluate Existing Evidence Closure
[NO DISCRIMINATING EVIDENCE]
         │
         ▼  Preserve COMPETING Status (Law CHC-01)
[COMPETING HYPOTHESES GRAPH]
         │
    ┌────┴────────────────────────┐
    │                             │
[DESIGN DISCRIMINATING PROBE]  [BOUNDED-REGRET ACTION]
Query / Evidence Search        Minimax Regret Safeguards
Discharge Invalidation Gates   Rollback Basin Prepared
```

---

## 4. Cross-Plane Bindings

- **`05_COGNITIVE_ORGANISM/04_COGNITION`**: Manages the competing hypothesis ensemble during reasoning.
- **`03_CONTROL_PLANE`**: Fences consequential actions under uncommitted hypothesis sets.
- **`16_SCHEMAS/TENSORS`**: Formats competing claim vectors.
- **`17_OBSERVABILITY`**: Tracks hypothesis branching and resolution history.

---

```RSCF-NODE
node_id: amos_01_canon_04_infrastructure_canon_competing_hypotheses_canon
node_type: infrastructure_canon
plane: 01_CANON
domain: INFRASTRUCTURE
claim_class: CANONICAL_LAW
status: ACTIVE_CANON
confidence_ceiling: ABSOLUTE_FOR_CANONICAL_LAW
falsifiers:
  - Premature pruning of a viable explanatory hypothesis without disproving evidence.
  - Consequential action committed under unverified assumption without minimax regret bounding.
```
