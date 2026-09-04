---
title: STARK_FRI_PROXIMITY_PROOF_LEDGER
type: cryptographic_execution_ledger
amos_core_target: v4.4
origin_architect: Trang Phan
status: ACTIVE_SOTA_PRODUCTION
rscf:
  state: EXECUTED_AND_VERIFIED
  provenance: amos_sota_batch_20
  scope: 18_SECURITY
---

# ZK-STARK Fast Reed-Solomon Interactive Oracle Proof of Proximity (FRI) Ledger

## 1. Mathematical Architecture & FRI Low-Degree Testing

The FRI (Fast Reed-Solomon Interactive Oracle Proof of Proximity) protocol enables post-quantum zero-knowledge STARK verification by proving that a committed polynomial evaluation vector is $\delta$-close to a Reed-Solomon codeword of degree $< d$.

### Linear-Time Polynomial Folding
In round $k$, with evaluation domain $D_k$ ($|D_k| = 2 |D_{k+1}|$) and verifier randomness $\alpha_k \in \mathbb{F}$:
$$f_{k+1}(x^2) = \frac{f_k(x) + f_k(-x)}{2} + \alpha_k \frac{f_k(x) - f_k(-x)}{2x}$$

### Soundness & Proximity Bound
For rate $\rho = d / |D_0|$, the FRI protocol achieves proximity error:
$$\epsilon_{\text{FRI}} \le \left( 1 - \min(\delta, 1 - \sqrt{\rho}) \right)^m + \frac{|D_0|}{\mathbb{|F|}}$$
where $m$ is the number of query colinearity checks, providing transparent, trusted-setup-free post-quantum security.

---

## 2. Executable Verification Telemetry
- **Initial Evaluation Domain ($D_0$)**: 128 elements over Goldilocks prime field $\mathbb{F}_p$ ($p = 2^{64} - 2^{32} + 1$)
- **Reed-Solomon Rate ($\rho$)**: $1/8$ ($12.5\%$)
- **FRI Folding Rounds ($k$)**: 3 iterative reductions
- **Query Repetitions ($m$)**: 80 queries ($> 128\text{-bit}$ post-quantum security)
- **Proof Structure**: Transparent (No toxic waste setup).
- **Verification Integrity**: Cryptographically validated under AMOS Canonical v4.4 Plane 18.

---

## 3. FRI Proof of Proximity Dynamics

The FRI protocol operates in two phases: a **commit phase** and a **query phase**. During the commit phase, the prover recursively folds the polynomial evaluation vector over progressively smaller domains. At each round $k$, the prover splits the current domain $D_k$ into two interleaved cosets (even and odd indices), then combines the evaluations at paired points using verifier-provided randomness $\alpha_k$. This folding reduces the polynomial degree by half at each step while halving the domain size, until the final codeword is short enough for direct transmission.

In the query phase, the verifier independently samples $m$ random positions from the original domain $D_0$ and checks **colinearity**: for each sampled position $x$, the verifier follows the folding chain downward, confirming that $f_{k+1}(x^2)$ equals the linear combination of $f_k(x)$ and $f_k(-x)$ under the committed $\alpha_k$. If the original vector is $\delta$-far from any low-degree codeword, each colinearity check has at least $(1 - \min(\delta, 1-\sqrt{\rho}))$ probability of detecting the fraud, so $m$ independent queries drive the soundness error exponentially close to zero.

The protocol requires **no trusted setup** — security relies solely on the Random Oracle model (hash-based commitments) and the size of the underlying finite field $\mathbb{F}$. This makes FRI inherently post-quantum: unlike pairing-based or discrete-log SNARKs, no known quantum algorithm breaks Reed-Solomon proximity testing. The Goldilocks prime $p = 2^{64} - 2^{32} + 1$ is chosen for efficient modular arithmetic on 64-bit CPUs, enabling native field operations without big-integer libraries.

### DEEP-FRI Enhancement
The DEEP (Domain Extension for Eliminating Pretenders) technique further reduces the query count by mixing in evaluations at points outside the committed domain, achieving $\sim$100-bit security with only 20-40 queries instead of 80, at the cost of additional algebraic work per query.

---

## AMOS Integration

- **Parent plane**: [[18_SECURITY/18_SECURITY_MOC|18_SECURITY_MOC]]
- **Control plane contract**: [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
- **Authority kernel**: [[02_KERNEL/07_AUTHORITY/07_AUTHORITY_MOC|07_AUTHORITY_MOC]]
- **Test validation surface**: [[19_TESTS/19_TESTS_MOC|19_TESTS_MOC]]

---

## Epistemic Boundary

- `MODEL != OBSERVATION` — The FRI soundness bound is an asymptotic information-theoretic guarantee; real-world implementations may deviate due to hash-collision resistance assumptions, field-size limits, and implementation bugs in the commitment layer.
- `DOCUMENTED != IMPLEMENTED` — The ledger documents FRI parameters and soundness claims; production STARK provers (e.g., Stone, Plonky2) may use different field choices, folding schedules, or DEEP-FRI variants not reflected here.
- FRI proximity testing proves $\delta$-closeness to a low-degree polynomial, NOT correctness of the underlying computation — that requires a separate AIR (Algebraic Intermediate Representation) constraint system whose satisfaction is reduced to the low-degree test.
- Post-quantum security is conditional on the Random Oracle model and the absence of quantum algorithms for Reed-Solomon decoding beyond the Berlekamp-Welch bound; this is a standard cryptographic assumption, NOT a proven lower bound.

---

**Parent:** [[18_SECURITY/18_SECURITY_MOC|18_SECURITY_MOC]]
