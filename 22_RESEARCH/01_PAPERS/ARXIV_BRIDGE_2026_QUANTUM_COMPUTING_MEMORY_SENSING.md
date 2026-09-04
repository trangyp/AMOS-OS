---
title: "ArXiv Bridge 2026 — Quantum Computing, Memory & Sensing"
type: arxiv_bridge
source: 22_RESEARCH/01_PAPERS/ARXIV_BRIDGE_2026_QUANTUM_COMPUTING_MEMORY_SENSING
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
epistemic_class: SOURCE_CLAIM
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: SOURCE_CLAIM
  provenance:
    - arxiv_2026_corpus
    - 11_KNOWLEDGE/_arxiv_md/_arxiv_md_MOC
    - 22_RESEARCH/02_ARXIV_BRIDGES
  scope: arxiv_bridge_2026_quantum_computing_memory_sensing
tags:
  - amos-os
  - 22_research
  - arxiv-bridge
  - quantum-computing
  - quantum-memory
  - quantum-sensing
  - quantum-error-correction
  - sota-2026
---

# ArXiv Bridge 2026 — Quantum Computing, Memory & Sensing

> **Steward:** Trang Phan · **AMOS_CORE:** `v4.4` · **Epistemic:** `SOURCE_CLAIM` · **Date:** 2026-09-04
> **Corpus:** `/Users/mac/Documents/_arxiv_md_external/obsidian-arxiv-md/2026/`

## Purpose

This bridge connects 2026 arXiv pre-prints in quantum computing (qubit aging, topological readout, error correction), quantum memory (telecom-band storage, passive self-correction), and quantum sensing (diamond NV, metrology) to their corresponding AMOS planes — spanning physical substrate, information-theoretic, and cryptographic layers.
---
## 1. Qubit Dynamics & Aging
### 1.1 Aging of Coupled Qubits

| Field | Value |
|-------|-------|
| **arXiv ID** | `2602.20534v1` |
| **Title** | Aging of coupled qubits |
| **Date** | 2026-02 |
| **Target Planes** | [[13_MODELS/13_MODELS_MOC|13_MODELS]], [[18_SECURITY/18_SECURITY_MOC|18_SECURITY]] |
| **Epistemic Class** | `SOURCE_CLAIM` |
| **AMOS Relevance** | First study of aging transitions in coupled qubit networks — sudden population drop at inactive-qubit threshold. Informs models plane for qubit degradation dynamics and security plane for fault-threshold analysis. |
| **Confidence Ceiling** | `SOURCE_CLAIM` for theory; hardware validation NOT ESTABLISHED. |
### 1.2 Measuring and Correcting Nanosecond Pulse Distortions in Quantum-Dot Spin Qubits

| Field | Value |
|-------|-------|
| **arXiv ID** | `2602.17899v1` |
| **Title** | Measuring and correcting nanosecond pulse distortions in quantum-dot spin qubits |
| **Date** | 2026-02 |
| **Target Planes** | [[15_INTERFACES/15_INTERFACES_MOC|15_INTERFACES]], [[13_MODELS/13_MODELS_MOC|13_MODELS]] |
| **Epistemic Class** | `EMPIRICAL` |
| **AMOS Relevance** | Pulse distortion correction for quantum-dot spin qubits — relevant to interfaces plane for quantum I/O fidelity; calibration informs models plane for hardware-aware gate compilation. |
| **Confidence Ceiling** | `EMPIRICAL` for specific platform; `SOURCE_CLAIM` for other spin-qubit modalities. |
### 1.3 Comparative Assessment of Germanium-Based Spin-Qubit Modalities

| Field | Value |
|-------|-------|
| **arXiv ID** | `2605.13680v1` |
| **Title** | Comparative assessment of germanium-based spin-qubit modalities |
| **Date** | 2026-05 |
| **Target Planes** | [[13_MODELS/13_MODELS_MOC|13_MODELS]], [[15_INTERFACES/15_INTERFACES_MOC|15_INTERFACES]] |
| **Epistemic Class** | `EMPIRICAL` |
| **AMOS Relevance** | Systematic comparison of Ge-based spin-qubit modalities — provides models plane with substrate selection criteria; interface plane benefits from cross-modal control/readout benchmarking. |
| **Confidence Ceiling** | `EMPIRICAL` for benchmarked modalities; `SOURCE_CLAIM` for scalability. |
---
## 2. Topological Quantum Computing & Error Correction
### 2.1 Native Topological Readout on Qubit Hardware: Fibonacci-Chain Benchmark

| Field | Value |
|-------|-------|
| **arXiv ID** | `2605.25913v1` |
| **Title** | Native topological readout on qubit hardware: a Fibonacci-chain benchmark of measurement-compilation trade-offs |
| **Date** | 2026-05 |
| **Target Planes** | [[13_MODELS/13_MODELS_MOC|13_MODELS]], [[18_SECURITY/18_SECURITY_MOC|18_SECURITY]] |
| **Epistemic Class** | `EMPIRICAL` |
| **AMOS Relevance** | Benchmarks fusion readout vs grouped-Pauli reconstruction for Fibonacci anyon chains on NISQ hardware. Informs models plane for topological compilation; security plane gains shot-budget crossover analysis. |
| **Confidence Ceiling** | `EMPIRICAL` for Fibonacci-chain MSE; `SOURCE_CLAIM` for 2D extension. |
### 2.2 Topological Subsystem Bivariate Bicycle Codes with Four-Qubit Check Operators

| Field | Value |
|-------|-------|
| **arXiv ID** | `2605.04151v1` |
| **Title** | Topological subsystem bivariate bicycle codes with four-qubit check operators |
| **Date** | 2026-05 |
| **Target Planes** | [[18_SECURITY/18_SECURITY_MOC|18_SECURITY]], [[13_MODELS/13_MODELS_MOC|13_MODELS]] |
| **Epistemic Class** | `SOURCE_CLAIM` |
| **AMOS Relevance** | Novel topological subsystem codes with low-weight four-qubit checks — reduces measurement overhead. Security plane gains QEC primitives; models plane benefits from scalable code construction. |
| **Confidence Ceiling** | `SOURCE_CLAIM` for code properties; hardware threshold NOT ESTABLISHED. |
### 2.3 Trapped-Ion Multiqubit Gates Compatible with Scalable QEC

| Field | Value |
|-------|-------|
| **arXiv ID** | `2605.28536v1` |
| **Title** | Trapped-Ion Multiqubit Gates Compatible with Scalable Quantum Error Correction |
| **Date** | 2026-05 |
| **Target Planes** | [[18_SECURITY/18_SECURITY_MOC|18_SECURITY]], [[13_MODELS/13_MODELS_MOC|13_MODELS]] |
| **Epistemic Class** | `EMPIRICAL` |
| **AMOS Relevance** | Multiqubit gates on trapped ions designed for QEC compatibility — bridges physical gates and logical correction. Security plane gains fault-tolerant primitives; models plane benefits from reduced circuit depth. |
| **Confidence Ceiling** | `EMPIRICAL` for trapped-ion gates; `SOURCE_CLAIM` for fault-tolerant scalability. |
### 2.4 Complex Abelian Varieties and Quantum Error Correction

| Field | Value |
|-------|-------|
| **arXiv ID** | `2605.28784v1` |
| **Title** | Complex abelian varieties and quantum error correction: a mathematical framework |
| **Date** | 2026-05 |
| **Target Planes** | [[18_SECURITY/18_SECURITY_MOC|18_SECURITY]], [[01_CANON/01_CANON_MOC|01_CANON]] |
| **Epistemic Class** | `SOURCE_CLAIM` |
| **AMOS Relevance** | Mathematical framework connecting complex abelian varieties to QEC code construction — provides canon plane with algebraic-geometric foundations; security plane gains new code families. |
| **Confidence Ceiling** | `SOURCE_CLAIM` for framework; `EMPIRICAL` code performance NOT ESTABLISHED. |
---
## 3. Quantum Memory
### 3.1 Telecom Quantum Memory over One Microsecond in Nanophotonic Lithium Niobate

| Field | Value |
|-------|-------|
| **arXiv ID** | `2605.11588v2` |
| **Title** | Telecom quantum memory over one microsecond in nanophotonic lithium niobate |
| **Date** | 2026-05 |
| **Target Planes** | [[10_MEMORY/10_MEMORY_MOC|10_MEMORY]], [[15_INTERFACES/15_INTERFACES_MOC|15_INTERFACES]] |
| **Epistemic Class** | `EMPIRICAL` |
| **AMOS Relevance** | On-chip telecom-band quantum memory exceeding 1 µs via erbium-doped thin-film LiNbO₃ AFC protocol — maps to memory plane for quantum storage; interface plane gains 20-mode storage at 2.2 GHz bandwidth. |
| **Confidence Ceiling** | `EMPIRICAL` for storage fidelity; `SOURCE_CLAIM` for network integration. |
### 3.2 A Passive Self-Correcting Quantum Memory in Three Dimensions

| Field | Value |
|-------|-------|
| **arXiv ID** | `2605.10943v1` |
| **Title** | A passive self-correcting quantum memory in three dimensions |
| **Date** | 2026-05 |
| **Target Planes** | [[10_MEMORY/10_MEMORY_MOC|10_MEMORY]], [[18_SECURITY/18_SECURITY_MOC|18_SECURITY]] |
| **Epistemic Class** | `SOURCE_CLAIM` |
| **AMOS Relevance** | 3D passive self-correcting quantum memory leveraging dimensional energy barriers — informs memory plane for autonomous storage; security plane benefits from passive fault tolerance reducing correction-circuit attack surface. |
| **Confidence Ceiling** | `SOURCE_CLAIM` for theory; finite-temperature realization NOT ESTABLISHED. |
---
## 4. Quantum Cryptography & Factoring
### 4.1 Factoring 2048-bit RSA with a Half-Million-Qubit Modular Atomic Processor

| Field | Value |
|-------|-------|
| **arXiv ID** | `2605.03951v1` |
| **Title** | Factoring 2048-bit RSA integers with a half-million-qubit modular atomic processor |
| **Date** | 2026-05 |
| **Target Planes** | [[18_SECURITY/18_SECURITY_MOC|18_SECURITY]], [[21_DOMAINS/21_DOMAINS_MOC|21_DOMAINS]] |
| **Epistemic Class** | `SOURCE_CLAIM` |
| **AMOS Relevance** | Resource estimate for Shor's algorithm on 2048-bit RSA using 500K-qubit neutral-atom processor — impacts security plane for post-quantum threat modeling; domain plane gains quantum-cryptographic application mapping. |
| **Confidence Ceiling** | `SOURCE_CLAIM` for estimates; actual factoring NOT ESTABLISHED. |
---
## 5. Quantum Sensing & Metrology
### 5.1 High-Pressure Magnetic Transition in Iron via Diamond Quantum Sensing

| Field | Value |
|-------|-------|
| **arXiv ID** | `2605.00576v1` |
| **Title** | High-pressure magnetic transition in iron observed via diamond quantum sensing |
| **Date** | 2026-05 |
| **Target Planes** | [[15_INTERFACES/15_INTERFACES_MOC|15_INTERFACES]], [[21_DOMAINS/21_DOMAINS_MOC|21_DOMAINS]] |
| **Epistemic Class** | `EMPIRICAL` |
| **AMOS Relevance** | Diamond NV-center quantum sensing applied to high-pressure condensed-matter physics — demonstrates interface plane's quantum sensor modality; domain plane gains cross-domain measurement primitive. |
| **Confidence Ceiling** | `EMPIRICAL` for transition observation; `SOURCE_CLAIM` for other transitions. |
### 5.2 Journey in Quantum Metrology and Sensing from Foundations to Applications

| Field | Value |
|-------|-------|
| **arXiv ID** | `2605.21702v1` |
| **Title** | Journey in quantum metrology and sensing from foundations to applications |
| **Date** | 2026-05 |
| **Target Planes** | [[15_INTERFACES/15_INTERFACES_MOC|15_INTERFACES]], [[21_DOMAINS/21_DOMAINS_MOC|21_DOMAINS]] |
| **Epistemic Class** | `SOURCE_CLAIM` |
| **AMOS Relevance** | Comprehensive review of quantum metrology and sensing — provides interface plane with theoretical framework for quantum-enhanced measurement; domain plane gains cross-application survey. |
| **Confidence Ceiling** | `SOURCE_CLAIM` as review; cited results carry own epistemic classes. |
---
## Bridge Summary

| Domain | Papers | Primary AMOS Planes |
|--------|--------|---------------------|
| Qubit Dynamics & Aging | 3 | 13_MODELS, 15_INTERFACES, 18_SECURITY |
| Topological QEC | 4 | 18_SECURITY, 13_MODELS, 01_CANON |
| Quantum Memory | 2 | 10_MEMORY, 15_INTERFACES, 18_SECURITY |
| Quantum Cryptography | 1 | 18_SECURITY, 21_DOMAINS |
| Quantum Sensing & Metrology | 2 | 15_INTERFACES, 21_DOMAINS |
| **Total** | **12** | |
---
## Epistemic Boundary

Hardware demonstrations (§1.2, §1.3, §2.1, §2.3, §3.1, §5.1) are `EMPIRICAL` on specific platforms but `SOURCE_CLAIM` for cross-platform generalization. Theoretical frameworks (§1.1, §2.2, §2.4, §3.2, §4.1, §5.2) remain `SOURCE_CLAIM` without hardware validation. RSA factoring (§4.1) and passive self-correcting memory at finite temperature (§3.2) are NOT ESTABLISHED.

`EMPIRICAL != UNIVERSAL` · `SOURCE_CLAIM != VERIFIED` · `RESOURCE_ESTIMATE != DEMONSTRATED` · `THEORY != DEPLOYED`
---
## Navigation

- [[22_RESEARCH/02_ARXIV_BRIDGES|ArXiv Bridges MOC]]
- [[22_RESEARCH/01_PAPERS/ARXIV_BRIDGE_2026_QUANTUM_HARDWARE_SENSING|Quantum Hardware & Sensing]]
- [[22_RESEARCH/01_PAPERS/ARXIV_BRIDGE_2026_BCI_AI_QUANTUM|BCI/AI/Quantum]]
- [[22_RESEARCH/01_PAPERS/ARXIV_BRIDGE_2026_CAUSAL_PREDICTIVE|Causal/Predictive]]
- [[22_RESEARCH/01_PAPERS/ARXIV_BRIDGE_2026_DIFFUSION_FEDERATED_EMBODIED|Diffusion/Federated/Embodied]]
- [[22_RESEARCH/01_PAPERS/01_PAPERS_MOC|Papers MOC]] · [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]]
