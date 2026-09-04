---
title: "ObserverBench — Testing Mechanistic Estimates for Intervention and Control"
type: research_paper
source: arxiv
arxiv_id: "2609.03026"
url: "https://arxiv.org/abs/2609.03026"
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
epistemic_class: SOURCE_CLAIM
conclusion_class: DERIVED
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance:
    - arxiv:2609.03026
    - 22_RESEARCH/01_PAPERS/ARXIV_2609_03026_OBSERVERBENCH
  scope: mechanistic_interpretability_intervention_control_benchmark
tags:
  - research
  - arxiv
  - mechanistic-interpretability
  - observability
  - intervention
  - control
  - safety
  - benchmark
created: 2026-09-02
---

# ObserverBench — Testing Mechanistic Estimates for Intervention and Control

> **arXiv:** [2609.03026](https://arxiv.org/abs/2609.03026)
> **Epistemic class:** `SOURCE_CLAIM` (benchmark with fixed task contracts, runnable baselines)
> **AMOS bridge:** RSCF Epistemic Boundary, Observability Plane, K_Effect_Classification, Audit-Repair

## Abstract summary

ObserverBench is a benchmark framework for testing whether internal estimators (observers) — mechanistic interpretability probes, sparse autoencoder (SAE) readouts, linear probes — are adequate for **intervention, control, and safety tasks**, not merely for passive measurement. The central insight is that an internal estimate that is accurate on average can still choose a poor action. The benchmark separates **estimation accuracy** from **loss caused by the chosen action**, reporting both independently.

In closed-loop control settings, observer errors matter most at the starting point and along directions the intervention can actually reach. AUROC, the standard interpretability metric, can rank monitors differently from deployment loss — a monitor that scores well on average may allocate intervention budget poorly when violation costs are asymmetric. Sparse SAE readouts trail layer-matched dense controls across tested models.

Tested on GPT-2-small, Qwen2.5-7B, and Gemma-2-9B-it.

## Key results

- An internal estimate that is accurate on average can still choose a poor action — estimation quality ≠ intervention quality
- Reports estimation accuracy separately from loss caused by chosen action, breaking the conflation between measurement and control
- In closed-loop control, observer errors matter at the starting point and along directions the intervention can reach
- AUROC can rank monitors differently from deployment loss — average-case ranking ≠ consequence-aware ranking
- Sparse SAE readouts trail layer-matched dense controls across GPT-2-small, Qwen2.5-7B, Gemma-2-9B-it
- Benchmark uses fixed task contracts with runnable baselines, enabling reproducible comparison

## AMOS bridge analysis

### Bridge 1 — RSCF epistemic boundary: confidence ≠ correctness

ObserverBench's core finding — "accurate on average ≠ chooses good action" — is the empirical instantiation of AMOS's RSCF epistemic boundary principle:

```text
AMOS RSCF epistemic boundary:
  "confidence ≠ correctness"
  a model's internal confidence is not evidence of external correctness
  estimation quality is not intervention quality

ObserverBench:
  "accurate on average ≠ chooses good action"
  a monitor with high AUROC can still select a poor intervention
  estimation accuracy is measured separately from action loss
```

Both enforce the same invariant: **do not treat measurement quality as decision quality**. An observer that measures well in expectation does not thereby govern well.

### Bridge 2 — Observability plane: evaluate by action quality, not measurement accuracy

ObserverBench's separation of estimation from action quality maps directly to AMOS's observability plane:

```text
AMOS observability plane:
  observability must be evaluated by whether it supports correct
  control decisions, not merely by whether it produces accurate
  measurements

ObserverBench:
  estimation accuracy (AUROC, MSE) reported separately from
  deployment loss (loss caused by chosen action)
  a monitor that measures accurately but intervenes poorly is
  flagged as inadequate for control
```

The AMOS observability plane requires that observability be judged by its contribution to governance, not by its fidelity as a sensor. ObserverBench provides the empirical protocol for this: measure the action, not just the estimate.

### Bridge 3 — K_Effect_Classification: consequence, not just detection

ObserverBench shows that when violation costs differ, perfect separation (AUROC) can still allocate intervention budget poorly:

```text
AMOS K_Effect_Classification:
  effect classification must consider consequence (violation cost),
  not just detection accuracy
  different effect classes carry different consequence weights

ObserverBench:
  AUROC ranks monitors differently from deployment loss
  when violation costs are asymmetric, a high-AUROC monitor
  can still choose actions with high deployment loss
  detection quality ≠ budget allocation quality
```

Both require that effect classification be consequence-aware: the cost of a missed or misallocated intervention must enter the evaluation, not just the detection rate.

### Bridge 4 — Audit-Repair: focus on reachable failure modes

ObserverBench's finding that observer errors matter at the starting point and along directions the intervention can reach maps to AMOS Audit-Repair:

```text
AMOS Audit-Repair:
  audit must focus on reachable failure modes, not all possible errors
  repair budget allocated to failure modes the system can actually
  encounter and act upon

ObserverBench:
  in closed-loop control, observer errors matter at the starting
  point and along directions the intervention can reach
  errors in unreachable directions do not affect deployment loss
  audit value is direction-conditioned, not uniform
```

Both enforce the same discipline: **audit and repair are not exhaustive — they are reach-conditioned**. An error that cannot be reached by any intervention carries no deployment cost; an error at the starting point or along a reachable direction carries the full cost.

## Epistemic boundary

- ObserverBench is a benchmark with fixed task contracts and runnable baselines. Its results are `SOURCE_CLAIM` for the mechanistic interpretability intervention/control domain.
- The AMOS bridges are `AMOS_MODEL` — structural analogies between ObserverBench's empirical findings and AMOS governance principles, not empirical validation of AMOS mechanisms.
- ObserverBench tests three model families (GPT-2-small, Qwen2.5-7B, Gemma-2-9B-it); generalization to other architectures or scales is not established.
- The SAE-vs-dense-control finding is specific to the tested SAE configurations and layer choices; it does not prove that all sparse readouts trail dense controls.

## Related

- [[22_RESEARCH/01_PAPERS/ARXIV_2608_19701_CAMA_MEMORY_CORRELATION_BIAS|CAMA — Memory Correlation Bias]]
- [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]]
- [[07_SKILLS/amos-capability-bound-governance/SKILL|Capability Bound Governance]]
- [[07_SKILLS/amos-audit-trail/SKILL|Audit Trail]]
- [[07_SKILLS/amos-validation-pipeline/SKILL|Validation Pipeline]]
- [[07_SKILLS/amos-failure-memory/SKILL|Failure Memory]]
