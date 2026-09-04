---
title: C04 BCI Specialist Architecture
type: domain_architecture
source: 21_DOMAINS/01_DOMAIN_ARCHITECTURE
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_ARCHITECTURE
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_bci_specialist
---

# C04 BCI Specialist Architecture

> **Epistemic status:** `AMOS_MODEL` / `DERIVED`. This note defines the BCI specialist architecture within `21_DOMAINS/14_C04_BIO_NEURO`. It does not claim clinical validation.

## Role

The C04 BCI specialist owns the **neural-decoding / brain-computer interface** boundary of the AMOS OS domain model. It translates BCI `OBSERVATION`s into governed proposals, under the authority of `05_COGNITIVE_ORGANISM` sensing and `02_KERNEL` runtime safety gates.

## Components

| Component | Responsibility | Related |
|-----------|----------------|---------|
| Signal Interface | Admits raw neural, EMG, EOG, and bioelectromagnetic signals | [[05_COGNITIVE_ORGANISM/01_SENSING_OBSERVATION/BCI_NEUROTECH_INTERFACE_MODEL|BCI Interface Model]] |
| Manifold Decoder | Produces latent intent manifolds from time-series signals | [[21_DOMAINS/14_C04_BIO_NEURO/C04_NEURAL_DECODING_AND_BCI_ARCHITECTURE|Neural Decoding & BCI Architecture]] |
| Reliability Gate | Fails closed on SNR/impedance drift | [[22_RESEARCH/AMOS_C04_BCI_RELIABILITY_SECURITY_FRONTIER_2026-09-04|BCI Reliability Frontier]] |
| Commit Arbiter | Promotes 250 ms phase-locked intent to `PROPOSAL` | [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|Control Plane MOC]] |

## Invariants

- `INV-BCI-S01` — Decoded intent is `OBSERVATION`, never `COMMIT`.
- `INV-BCI-S02` — 250 ms phase-locked stability before proposal.
- `INV-BCI-S03` — Raw neural data is not stored as canonical `SOURCE_CLAIM`.

## Cross-References

- [[21_DOMAINS/14_C04_BIO_NEURO/14_C04_BIO_NEURO_MOC|C04 Bio-Neuro MOC]]
- [[21_DOMAINS/01_DOMAIN_ARCHITECTURE/01_DOMAIN_ARCHITECTURE_MOC|Domain Architecture MOC]]
- [[22_RESEARCH/BCI_RESEARCH_MOC|BCI Research MOC]]
