---
title: "Cornucopia Codes — Ultra-Low Overhead Quantum Error Correction"
type: research_paper
source: arxiv
arxiv_id: "2608.02773"
url: "https://arxiv.org/abs/2608.02773"
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
epistemic_class: SOURCE_CLAIM
conclusion_class: DERIVED
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance:
    - arxiv:2608.02773
    - 22_RESEARCH/BCI_AI_QUANTUM_SOTA_2026-09-04
  scope: quantum_error_correction
tags:
  - research
  - arxiv
  - quantum
  - qec
  - qldpc
  - fault-tolerance
  - neutral-atom
created: 2026-09-04
---

# Cornucopia Codes — Ultra-Low Overhead QEC

> **arXiv:** [2608.02773](https://arxiv.org/abs/2608.02773)
> **Epistemic class:** `SOURCE_CLAIM` (preprint, simulation-validated)
> **AMOS bridge:** C03 Physics-Cosmos, C02 Math-Compute

## Key result

A family of qLDPC codes achieving **encoding rate >1/2** with **pseudo-threshold >0.4%** under circuit-level noise. The `[[2844,1426,18]]` block encodes **1,426 logical qubits** at distance 18, with extrapolated logical error rate of 2.6×10⁻¹⁶ per logical qubit per cycle (at 0.1% physical error).

Comparison: bivariate bicycle codes would need >68,000 physical qubits for the same logical count at comparable error rate. Cornucopia uses 2,844 — a **24× reduction**.

Syndrome extraction: 12 entangling layers per cycle, independent of code size. Co-designed for reconfigurable neutral-atom arrays.

## AMOS bridge analysis

### C03 Physics-Cosmos: Quantum error correction

This represents a step-change in QEC efficiency. The vault's quantum stack canon tracks surface codes and bivariate bicycle codes as primary QEC approaches. Cornucopia codes establish a new efficiency frontier:

```text
Surface code:      ~1% encoding rate, threshold ~1%
Bivariate bicycle: ~1% encoding rate, threshold ~1%
Cornucopia:        >50% encoding rate, threshold ~0.4%
```

The threshold is lower (0.4% vs 1%) but the encoding rate is 50× higher. For physical error rates below 0.1%, Cornucopia dominates decisively.

### C02 Math-Compute: Encoding efficiency optimization

The code construction uses affine-permutation-based geometry with co-designed layout, atom rearrangement, and syndrome extraction. This is a constrained optimization problem:
- Maximize encoding rate (logical/physical qubit ratio)
- Maximize distance (error correction capability)
- Minimize syndrome extraction depth (circuit complexity)
- Satisfy hardware connectivity constraints (neutral-atom arrays)

### L23 MVCC-CAS analogy

The parallel syndrome extraction (all X and Z checks in 12 layers, independent of code size) mirrors AMOS L23 MVCC-CAS: concurrent operations must be validated without serial bottlenecks. The "coordination avoidance" pattern in AMOS (proof-based coordination avoidance) maps to the parallel syndrome extraction pattern in Cornucopia.

## Epistemic boundary

- Results are **simulation-validated**, not experimentally demonstrated on hardware. The `SOURCE_CLAIM` is for the code construction and simulation results.
- Neutral-atom compatibility is architectural, not validated. Atom rearrangement fidelity at scale is `UNKNOWN/GAP`.
- The 0.4% pseudo-threshold is below current best physical qubit error rates (~0.1-0.5% for superconducting, ~0.01% for trapped ions). Cornucopia may require trapped-ion-level fidelity to achieve advantage.

## Related

- [[22_RESEARCH/BCI_AI_QUANTUM_SOTA_2026-09-04|BCI/AI/Quantum SOTA 2026-09-04]]
- [[07_SKILLS/amos-c03-physics-cosmos-master/SKILL|C03 Physics-Cosmos Master]]
- [[07_SKILLS/amos-c02-math-compute-master/SKILL|C02 Math-Compute Master]]
- [[07_SKILLS/amos-l23-mvcc-cas/SKILL|L23 MVCC-CAS]]
- [[07_SKILLS/amos-quantum-stack-canon/SKILL|Omega Quantum Stack Canon]]
- [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]]
