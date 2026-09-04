---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Sota Quantum Computing Qml And Ontology 2026
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

# SOTA Quantum Computing, QML Empirical Skepticism, and Quantum Ontology 2026

> **Epistemic Invariant & Boundary**
>
> This document synthesizes state-of-the-art evidence from the 66,029-note Arvix research corpus, empirical audits in `outputs/`, and Trang Phan's recursive ontology models.
> It separates mathematical derivations, empirical benchmark audits, theoretical models, and philosophical interpretations.
>
> ```text
> PROOF OF PRINCIPLE != PRACTICAL ADVANTAGE
> TOY-SCALE EXPRESSIVITY != RUNTIME SUPREMACY
> ANALOGY != IDENTITY
> MODEL CONSISTENCY != PHYSICAL REALITY
> QUANTUM OPENNESS != CONSCIOUS AGENCY
> ```

---

## 1. Executive Summary & Epistemic Landscape

The 2026 quantum landscape exhibits a fundamental bifurcation between **near-term classical-data quantum machine learning (QML)** and **foundational quantum ontology/computation**:

1. **The Empirical Skeptical Verdict on QML**: Exhaustive full-text audits across the 2026 publication peak (auditing candidate advantage papers in `outputs/Quantum_2026-05_Audit.md` and `outputs/Quantum_2026_Rest-of-Year_Audit.md`) demonstrate that **zero audited papers provide a fair, architecture-matched, hardware-realistic runtime win over classical baselines on classical data**. Advantage claims collapse into toy-scale demonstrations (classically simulable at $\le 100$ qubits), artificial quantum-output separations, or cost-prohibitive parity.
2. **The 6-Voice Quantum Consciousness Debate**: Analysis of the historical arc (2007–2026) reveals that quantum-consciousness literature is not an emerging consensus, but a rigorous, unresolved tension among six distinct positions: Dualist Observational (CCC), Materialist Objective Collapse (CSL/IIT), Everettian Quantum Darwinism, Reductionist Quantum Information, Historicist Corrective, and Non-Constitutive Panprotopsychism.
3. **Khung Trang Computable Recursive Survival Dynamics**: A formal meta-ontological framework addressing the explanatory gap of modern quantum theory—specifically how stable identity, boundary closure, system memory, and classical reality emerge recursively from quantum potentials.

---

## 2. Empirical State of the Art: Quantum Machine Learning (QML) Under Scrutiny

### 2.1 The 2026-05 Audit and Empirical Findings

In May 2026, arXiv experienced a peak influx of QML publications. A full-text audit of the five primary candidates claiming "advantage", "fair benchmark", or questioning "do we need QML" established the following evidence base:

| Paper & Identifier | Target Claim | Audit Verdict & Empirical Reality | Failure Mode / Boundary |
| :--- | :--- | :--- | :--- |
| **Do We Really Need QML?**<br>`arXiv:2605.27923` | Multidimensional MNIST benchmark; tests if QML beats classical SVM/CNN. | **No clean win.** QSVM exhibits modest accuracy edge (~0.90 vs ~0.85) at orders-of-magnitude higher compute; shrinks to parity at scale and *reverses* below 200 samples. QCNN wins only efficiency at accuracy-parity. | Simulator-bound; MNIST-only; non-scalable cost. |
| **Fair Benchmarking of QTL**<br>`arXiv:2605.19417` | Controlled benchmark of Quantum Transfer Learning for visual tasks. | **No beat claim.** Compares QTL variants to each other, not classical SOTA. Performance is dataset/budget sensitive (AE-CQTL drops to ~50% chance on CIFAR-10). | Near-term NISQ (4–6 qubits); simulator-only; no classical comparison. |
| **Exponential Sample Advantage**<br>`arXiv:2605.21457` | Exponential sample-complexity advantage for coherent quantum inference. | **Theoretical separation only.** Proven on artificial quantum-output states (purification, cloning, density matrix exponentiation) under idealized coherent access. | Fault-tolerance deferred to outlook; no advantage on classical data. |
| **Algorithmic Advantage on Photonic QNN**<br>`arXiv:2605.10801` | Physical photonic-chip QNN vs parameter-matched classical ANN. | **Downgraded by authors.** Demonstrates higher effective dimension (0.95 vs 0.68) on toy XOR/Iris ($\le 6$ parameters). Authors explicitly state circuits are **classically simulable** ($\le 100$ modes). | Representational expressivity $\ne$ computational/runtime advantage. |
| **Matched Spectral Benchmark**<br>`arXiv:2605.24324` | Parameter-matched evaluation of quantum-inspired feature maps. | **Zero significant wins.** Across 30 encoding-dataset pairs, 27 were significantly worse than classical kernels. | Mechanistic collapse: rank collapse, angle redundancy, basis misalignment. |

### 2.2 Mechanistic Failure Modes of Fixed-Encoding Classical QML

The failure of near-term QML to outperform classical baselines on classical data is driven by three formal geometric mechanisms identified in `arXiv:2605.24324`:

1. **Amplitude Rank Collapse**: Encoding continuous classical vectors into quantum amplitudes via fixed linear unitaries compresses feature variance into lower-dimensional subspaces, causing kernel Gram matrices to degenerate.
2. **Angle Redundancy**: Periodic trigonometric parameterizations ($\cos \theta, \sin \theta$) introduce artificial periodic symmetries not present in the underlying data manifold.
3. **Basis Misalignment**: Hilbert-space inner products $\langle \psi(x) | \psi(x') \rangle$ measure global state overlap rather than task-relevant semantic distance, failing to align with natural decision boundaries.

**Crucial Scope Invariant**: This empirical skepticism strictly applies to **near-term, fixed-encoding, classical-data QML**. It does *not* refute quantum advantages in:
- Hamiltonian simulation of native quantum systems;
- Coherent sampling and state preparation;
- Genuine quantum sensor data inputs;
- Fault-tolerant Shor/Grover asymptotic regimes.

---

## 3. Quantum Foundations & Consciousness: The Six-Voice Map

Tracking the 20-year corpus (from Khrennikov's 2007 *Toward Psycho-robots* to 2026 objectivism critiques) reveals that quantum-consciousness literature consists of six distinct, mutually competing frameworks:

```text
               ┌──────────────────────────────────────────────┐
               │         THE HARD PROBLEM & QUALIA            │
               └──────────────────────┬───────────────────────┘
                                      │
         ┌────────────────────────────┼────────────────────────────┐
         ▼                            ▼                            ▼
┌──────────────────┐        ┌──────────────────┐        ┌──────────────────┐
│ COLLAPSE THEORIES│        │ NO-COLLAPSE (MVI)│        │   REDUCTIONIST   │
│ Dualist (CCC) vs │        │Quantum Darwinism │        │Quantum Info /    │
│ Materialist(CSL) │        │ (Page 2021)      │        │Acausal (Georgiev)│
└────────┬─────────┘        └──────────────────┘        └──────────────────┘
         │
         ├────────────────────────────┬────────────────────────────┐
         ▼                            ▼                            ▼
┌──────────────────┐        ┌──────────────────┐        ┌──────────────────┐
│   PANPSYCHISM    │        │   HISTORICIST    │        │  METHODOLOGICAL  │
│ Non-constitutive │        │De-mythologizing  │        │ Limits of Object-│
│(Gambini-Pullin)  │        │ von Neumann      │        │ivism (DeBrota)   │
└──────────────────┘        └──────────────────┘        └──────────────────┘
```

### 3.1 The Competing Positions

1. **Dualist Observational (Consciousness Causes Collapse - CCC)**:
   - *Anchor*: Knight (2020), *Quantum Mechanics May Need Consciousness*.
   - *Thesis*: Consciousness acts as the non-physical observer triggering wave-function reduction, defended against delayed-choice quantum eraser falsifications.
   - *Epistemic Status*: `COMPETING / SPECULATIVE`. Violates physical causal closure.
2. **Materialist Objective Collapse (Integrated Information Collapse)**:
   - *Anchor*: Okon & Sebastián (2018), *A Consciousness-Based Quantum Objective Collapse Model*.
   - *Thesis*: Continuous Spontaneous Localization (CSL) collapse operator rate depends on Tononi's Integrated Information ($\Phi$). Materialist, physicalist, rejects dualism.
   - *Formal Block*: McQueen, Durham & Müller (2023, *Schrödinger's Dyad*) proved that Lindblad collapse dynamics cannot sensitively depend on qualitative experiential differences without an unphysical explosion of collapse operators.
3. **No-Collapse / Everettian Quantum Darwinism**:
   - *Anchor*: Don Page (2021), *Classicality of Consciousness in Quantum Darwinism*.
   - *Thesis*: Environmental decoherence and quantum Darwinism produce redundant classical records. Conscious perceptions are strictly classical states emerging within Everett branches; no collapse occurs.
4. **Quantum-Information Reductionism**:
   - *Anchor*: Georgiev (2025), *Quantum information theoretic approach to the hard problem of consciousness*.
   - *Thesis*: Consciousness is identically identified with unobservable quantum states ($\rho$). The brain is a third-person classical construct; qualia are intrinsic quantum informational properties. Acausal and non-collapse.
5. **Historicist Corrective**:
   - *Anchor*: Laudisa (2025), *Between Myth and History: von Neumann on Consciousness in Quantum Mechanics*.
   - *Thesis*: Historical deconstruction demonstrating that von Neumann's measurement theory placed the cut arbitrarily and did not claim consciousness physically collapses wave-functions; the "von Neumann-Wigner" interpretation is largely an ex-post myth.
6. **Non-Constitutive Panprotopsychism**:
   - *Anchor*: Gambini & Pullin (2024–2025 four-paper arc).
   - *Thesis*: Entanglement resolves Chalmers' combination problem because parts lose individual identities in entangled states. Uses "regularism" and quantum causal openness to argue consciousness is causal and fundamental without being dualist or epiphenomenal.

---

## 4. Khung Trang: Computable Recursive Survival Dynamics & Quantum Ontology

### 4.1 Ontological Limitations of Modern Quantum Theory

As formalized in Trang Phan's *Khung Trang* research model (`KHUNG_TRANG_QUANTUM_ONTOLOGY_COMPUTABLE_DYNAMICS_RESEARCH_MODEL.md`), modern quantum mechanics possesses extraordinary predictive and mathematical power in interaction dynamics (Hilbert space, gauge symmetry, operator algebra, perturbation theory), but remains ontologically open regarding:
- The exact ontological status of the state vector (physical entity vs Bayesian information);
- The boundary-locking mechanism that prevents macro-superposition;
- The emergence of persistent identity across temporal transitions;
- The cross-layer invariance governing system survival and error-correction.

### 4.2 Mathematical Formalization of Recursive Survival Dynamics

Khung Trang models an open system $S$ interacting with environment $E$ across scales $L, M, H$ using four coupled operators:

$$\mathcal{S}_{\text{system}} = \langle \mathcal{B}, \mathcal{I}, \mathcal{M}, \mathcal{R} \rangle$$

1. **Boundary Operator ($\mathcal{B}_{\text{lock}}$)**:
   Maintains phase coherence within the interior domain $\Omega_{\text{int}}$ while regularizing environmental flux across boundary $\partial \Omega$:
   $$\mathcal{B}_{\text{lock}}(\Psi) = \oint_{\partial \Omega} \left[ \nabla \Psi \cdot \mathbf{n} - \gamma_{\text{env}} \Psi \right] d\sigma = 0$$

2. **Identity Invariant ($\mathcal{I}_{\text{continuity}}$)**:
   Preserves topological and causal invariants under unitary and non-unitary transformations:
   $$\mathcal{I}(\Psi_t, \Psi_{t+\Delta t}) = \text{Tr}\left( \rho_t \rho_{t+\Delta t} \right) \ge 1 - \epsilon_{\text{decay}}$$

3. **Systemic Memory ($\mathcal{M}_{\text{trace}}$)**:
   Encodes historical interaction trajectories into persistent state tensors, preventing Markovian memory loss:
   $$\mathcal{M}_{t} = \alpha \mathcal{M}_{t-\delta t} + (1-\alpha) \mathcal{P}_{\text{project}}(\Psi_t)$$

4. **Recursive Error-Correction ($\mathcal{R}_{\text{ground}}$)**:
   Active ground-state restoration driving deviated states back to viability basins:
   $$\frac{\partial \Psi}{\partial t} = -i [H, \Psi] - \lambda_{\text{repair}} \mathcal{R}_{\text{ground}}(\Psi - \Psi_{\text{target}})$$

### 4.3 Comparison with Standard Physics Frameworks

| Dimension | Standard Quantum Mechanics (Copenhagen/Everett) | Decoherence Theory (Zurek) | Khung Trang Recursive Survival Dynamics |
| :--- | :--- | :--- | :--- |
| **State Definition** | Wavefunction $\Psi \in \mathcal{H}$ | Reduced density matrix $\rho_S = \text{Tr}_E(\rho)$ | Boundary-locked state capsule $\langle \mathcal{B}, \mathcal{I}, \mathcal{M}, \mathcal{R} \rangle$ |
| **Classical Emergence** | Axiomatic measurement / Branching | Pointer states via environment-induced superselection | Dynamic boundary locking + active error recovery |
| **Identity Persistence** | Not modeled (unitary evolution of universe) | Redundant information copying | Invariant continuity index across temporal epochs |
| **Systemic Memory** | Pure state is memoryless; Markovian bath | Entanglement entropy in reservoir | Explicit historical tensor accumulation ($\mathcal{M}$) |
| **Status in AMOS** | `SOURCE_CANON / EMPIRICAL` | `EMPIRICAL / MODEL` | `RESEARCH_MODEL / AMOS_MODEL` (Non-canonical) |

---

## 5. Integration into AMOS Core Architecture

1. **C03 Physics & Cosmos Master**: Owns the empirical boundary for quantum simulation and transport.
2. **C02 Mathematics & Computation**: Owns tensor representations, operator algebra, and spectral benchmark validation.
3. **C05 Mind & Behavior**: Owns cognitive and behavioral modeling, enforcing the firewall `quantum analogy != cognitive law`.
4. **02 Kernel**: Implements deterministic invariants inspired by recursive dynamics (boundary enforcement, state persistence, rollback basins) without claiming physical quantum operation.

---

```RSCF-NODE
node_id: sota_quantum_computing_qml_and_ontology_2026
node_type: specialist_knowledge
domain: C03_PHYSICS_COSMOS
claim_class: MIXED
confidence_ceiling: HIGH_FOR_EMPIRICAL_AUDIT__MODEL_FOR_ONTOLOGY
falsifiers:
  - Demonstration of a fair, matched, hardware-realistic classical-beating QML result on classical data.
  - Experimental refutation of Lindblad operator explosion in IIT-collapse models.
  - Exact simulation showing failure of Khung Trang boundary-locking dynamics.
```
