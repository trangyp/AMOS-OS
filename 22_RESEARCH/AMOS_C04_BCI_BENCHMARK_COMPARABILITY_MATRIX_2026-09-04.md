---
title: C04 BCI Benchmark Comparability Matrix 2026-09-04
type: research_frontier
source: 22_RESEARCH
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_FRONTIER_NOTE
conclusion_class: DERIVED
date: 2026-09-04
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_bci_benchmarks
---

# C04 BCI Benchmark Comparability Matrix 2026-09-04

> **Epistemic status:** `AMOS_MODEL` / `DERIVED`. Placeholder for a BCI benchmark comparability matrix. `UNKNOWN/GAP` for quantitative comparisons until populated.

## Purpose

Provide a structured comparability matrix for BCI/neurotechnology benchmarks so that `21_DOMAINS/14_C04_BIO_NEURO` and `05_COGNITIVE_ORGANISM` can reason about transfer, validity, and safety margins across datasets, tasks, and hardware.

## Matrix Axes (proposed)

| Axis | Description |
|------|-------------|
| Modality | intracortical, ECoG, EEG, fNIRS, MEG, ultrasound, optogenetic |
| Task | motor, speech, cognitive state, affect, sensory |
| Subjects | N, clinical vs. healthy, cross-session count |
| Metric | R², classification accuracy, ITR, bit error, AUROC |
| Latency | closed-loop update interval |
| Generalization | within-subject, cross-subject, cross-day, cross-device |
| Safety | fail-closed behavior, impedance monitoring, artifact handling |

## Status

- Rows and benchmark values are `UNKNOWN/GAP`.
- The matrix will be populated from `22_RESEARCH/01_PAPERS/` BCI SOTA syntheses as they are ingested.

## Cross-References

- [[22_RESEARCH/BCI_RESEARCH_MOC|BCI Research MOC]]
- [[22_RESEARCH/FRONTIER_TECH_RESEARCH_MOC|Frontier Technology Research MOC]]
- [[21_DOMAINS/14_C04_BIO_NEURO/C04_NEURAL_DECODING_AND_BCI_ARCHITECTURE|C04 Neural Decoding & BCI Architecture]]
- [[22_RESEARCH/AMOS_C04_BCI_RELIABILITY_SECURITY_FRONTIER_2026-09-04|C04 BCI Reliability / Security Frontier]]
