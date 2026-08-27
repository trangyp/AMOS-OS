---
title: amos-quantum-error-mitigation
type: quantum
created: 2026-08-25
tags: [canon-group/quantum, canon/error-mitigation, canon/error-correction, rscf/claim, rscf/provenance, rscf/state/source-claim, topic/amos-quantum-error-mitigation, quantum]
status: validated
---


# amos-quantum-error-mitigation

> **Source**: `AMOS_quantum_library_v0.1.0.md` v0.7.0 cycle (AM-QEC-006/007/008), `_00_Cosmo brain/math_fractal_architecture_25000.md`
> **Conclusion class**: AMOS MODEL — derived from quantum library v0.7.0 + vault math architecture

## Core entries (SOURCE)

### AM-QEC-006 — Zero-Noise Extrapolation (ZNE)

**Formal expression**: `Ê(λ=0) = Σ_k c_k · Ê(λ=k·Δλ)`, Richardson extrapolation over scaled noise strengths

**Variables**:
- `λ` — noise strength scaling factor
- `Δλ` — noise increment
- `c_k` — extrapolation coefficients
- `Ê(λ)` — noisy expectation value at scale λ

**Domain tags**: `quantum-error-mitigation`, `zero-noise-extrapolation`, `richardson-extrapolation`, `noise-scalability`

**Regime conditions**:
- Noise model must be sufficiently Markovian
- Extrapolation range must include λ=0 limit
- Coefficients c_k must be numerically stable

**Derivation reference**: Quantum library v0.7.0, cycle v0.7.0

**Experimental status**: validated on superconducting/qudit platforms

**Confidence**: high

**Notes**: 
- Primary mitigation for bias-preserving noise
- Requires noise-strength scaling (pulse stretching, gate folding)
- Richardson extrapolation is the standard; polynomial fits can diverge
- Limitation: does NOT remove stochastic error variance, only bias

**Source**: Tier 1 (PRL/PRA, IBM Quantum, MIT)

---

### AM-QEC-007 — Probabilistic Error Cancellation (PEC)

**Formal expression**: `P_eff = Σ_{s∈S} w_s · P_s`, quasi-probability decomposition of noise channel

**Variables**:
- `P_eff` — effective ideal probability distribution
- `w_s` — quasi-probability weights (can be negative)
- `P_s` — sampled circuit outcomes
- `S` — sample space of noise-realization sequences

**Domain tags**: `quantum-error-mitigation`, `probabilistic-error-cancellation`, `quasi-probability`, `noise-invertibility`

**Regime conditions**:
- Noise channel must be invertible or approximately invertible
- Quasi-probability weights must be sampled with sign handling
- Variance may increase; requires many samples for high precision

**Derivation reference**: Quantum library v0.7.0, cycle v0.7.0

**Experimental status**: validated on trapped-ion/superconducting platforms

**Confidence**: high

**Notes**:
- More general than ZNE: works for any invertible noise channel
- Quasi-probability = probability with negative values → variance increase
- SEPARATE from ZNE: noise-scalability vs noise-invertibility are different axes
- Gate folding is ONE instantiation of quasi-probability, not the only one

**Source**: Tier 1 (PRL/PRA, Google Quantum AI, Caltech)

---

### AM-QEC-008 — Quantum LDPC Codes (QLDPC)

**Formal expression**: `n,k,d` bivariate bicycle code `144,12,12` achieves ~10x qubit reduction vs surface code

**Variables**:
- `n` — number of physical qubits
- `k` — number of logical qubits
- `d` — code distance
- `n,k,d` — stabilizer code parameters

**Domain tags**: `quantum-error-correction`, `ldpc-codes`, `bivariate-bicycle`, `hypergraph-product`, `quantum-error-mitigation`

**Regime conditions**:
- Code must satisfy stabilizer commutation relations
- Syndrome extraction must be fault-tolerant
- Decoder must handle correlated errors

**Derivation reference**: Quantum library v0.7.0, cycle v0.7.0

**Experimental status**: validated small instances; scaling to 1000+ qubits pending

**Confidence**: high

**Notes**:
- BB code `144,12,12` is the canonical example
- ~10x qubit reduction vs surface code for same logical qubit count
- Related families: hypergraph-product codes, bivariate bicycle codes
- Threshold failure mode: single-shot QEC erasure-cost tradeoff

**Source**: Tier 1 (PRL/PRA, IBM Quantum, MIT)

---

## Bounds (SOURCE)

| ID | Bound | Expression |
|----|-------|------------|
| AM-BND-054 | ZNE noise-scaling limit | `Var[Ê(λ)] ≤ Var[Ê(λ=0)] · (1 + O(λ²))` |
| AM-BND-055 | PEC quasi-probability variance | `Var[P_eff] ≥ Var[P_ideal]` (quasi-probability increases variance) |
| AM-BND-056 | QLDPC qubit reduction factor | `n_QLDPC / n_surface ≤ 0.1` for equivalent logical qubit count |

## Invariants (SOURCE)

| ID | Invariant | Condition |
|----|-----------|-----------|
| AM-INV-033 | ZNE extrapolation stability | `|Ê(λ=0) - Ê_exact| ≤ ε` for well-conditioned noise models |
| AM-INV-034 | QLDPC code distance preservation | `d ≥ 2t+1` for correction of up to t errors |

## Failure modes (SOURCE)

| ID | Failure Mode | Detection | Recovery |
|----|--------------|-----------|----------|
| FM53 | ZNE extrapolation divergence | Polynomial fit blows up at λ→0 | Switch to linear Richardson; reduce fit order |
| FM54 | PEC quasi-probability variance explosion | Sample count insufficient for negative weights | Increase shots; use median-of-means |
| FM55 | QLDPC decoder error propagation | Syndrome decoding incorrect under correlated errors | Switch to belief-propagation decoder; add syndrome-correlation checks |

## Experimental constraints (SOURCE)

| ID | Constraint | Platform | Status |
|----|------------|----------|--------|
| EC52 | ZNE on 127-qubit device | superconducting | validated |
| EC53 | PEC on 32-qubit device | trapped-ion | validated |
| EC54 | QLDPC 144,12,12 | superconducting | validated small instances |
| EC55 | Single-shot QEC erasure cost | photonic | experimental |

## Frontier problems (SOURCE)

| ID | Problem | Status |
|----|---------|--------|
| FP34 | Real-time ZNE for dynamic circuits | theoretical |
| FP35 | PEC for non-invertible noise channels | theoretical |
| FP36 | QLDPC decoding at scale (>1000 qubits) | experimental |
| FP37 | Unified ZNE+PEC protocol | theoretical |

## Tensor structures (SOURCE)

| ID | Tensor | Structure |
|----|--------|-----------|
| TS5 | Error-mitigation tensor | `T_mitigation[i,j,k] = noise_channel(i→j) · mitigation_weight(k)` |

## Sources (SOURCE)

| ID | Source | Tier |
|----|--------|------|
| S53 | Tem_by_Line et al., PRL 2020 (ZNE) | Tier 1 |
| S54 | van_den_Berg et al., PRA 2022 (PEC) | Tier 1 |
| S55 | Google Quantum AI, Nature 2023 (QLDPC) | Tier 1 |
| S56 | IBM Quantum, arXiv:2308.07915 (bivariate bicycle) | Tier 1 |
| S57 | Piveteau et al., PRL 2022 (PEC variance) | Tier 1 |
| S58 | Kremenetski et al., PRA 2021 (ZNE bias) | Tier 1 |
| S59 | breuckmann et al., PRX 2023 (QLDPC threshold) | Tier 1 |
| S60 | Higgott et al., PRL 2023 (single-shot QEC) | Tier 1 |

---

## Integration

- Quantum library: 72 canonical entries v0.7.0
- Quantum bridge: 26-domain taxonomy coverage, 0 gaps
- Fractal engine: 25 canonical families FR001-FR025
- Math architecture: 25,000 mappings
- DMER kernel: trajectory classification
- MURK: 19-primitive logic

## Cross-links

- `_00_Cosmo brain/md/2026-08-25_architecture_quantum_audit_and_v070_plan.md`
- `_00_Cosmo brain/md/daily/2026-08-25-quantum-fractal-math-integrity-session.md`
- `amos-quantum-fractal-math`
- `amos-qfm-adversarial-hardening`
- `amos-entropy-lacunarity-viability`

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · qfm-max-power-consolidation · unipower-unitaxi-mece · amos-tech-quantum-engine-layer

---
**MOC:** [[QUANTUM_MOC]]
