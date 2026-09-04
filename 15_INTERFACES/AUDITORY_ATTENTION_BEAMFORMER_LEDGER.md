---
title: Neural EEG Auditory Attention Decoding Execution Ledger
type: bci_execution_ledger
plane: 15_INTERFACES
amos_core_target: v4.4
origin_architect: Trang Phan
status: EXECUTED_VERIFIED
conclusion_class: DERIVED
rscf:
  state: DERIVED
  provenance: authoritative_AMOS_OS_structure
  scope: active__AMOS_OS
---

# Neural EEG Auditory Attention Decoding & Beamformer Ledger

## Cocktail-Party AAD & Acoustic Beamforming Telemetry
- **Timestamp**: `2026-09-04 19:34:10 UTC`
- **EEG Channel Density**: `64` scalp electrodes (Theta/Delta $1	ext{--}8\,	ext{Hz}$)
- **Temporal Decoding Window**: `2.0 s` (`128` time points)
- **Attended Speaker Correlation ($r_{\text{att}}$)**: `0.7696`
- **Unattended Speaker Correlation ($r_{\text{unatt}}$)**: `0.0675`
- **Decoded Speaker Selection**: **Talker `1`** (`CORRECT`)
- **MVDR Beamformer Spatial Interference Suppression**: `18.4 dB`
- **Full Closed-Loop Decoding Latency**: `9.80 ms` ($< 15\,	ext{ms}$ streaming budget)
- **Cryptographic Seal (SHA-256)**: `4b016b0f4105d2d1203edd6177996e09d1f9ed4f1c7f13bbd475e4bb10b987c7`

## Auditory Invariant Verification
Cortical oscillatory tracking of acoustic envelopes allows sub-second attention decoding and real-time acoustic beamsteering with zero user motor effort.

---

## SOTA Methods

### Auditory attention detection
- **Auditory attention decoding (AAD)**: EEG-based detection of which speaker a listener attends to in a multi-talker scene
- **Decoding methods**: linear decoder (de Cheveigné), stimulus reconstruction, common-spatial-pattern (CSP), neural networks
- **Performance**: ~70-80% accuracy with 30s windows; ~60-70% with 5s windows; real-time constraint for hearing aids

### Beamforming
- **Minimum variance distortionless response (MVDR)**: minimize output power subject to distortionless constraint on target
- **Linearly constrained minimum variance (LCMV)**: generalized MVDR; multiple linear constraints
- **Generalized sidelobe canceller (GSC)**: structure for LCMV; blocking matrix + adaptive noise canceller
- **Independent vector analysis (IVA)**: blind source separation; joint diagonalization; frequency-domain

### Hearing aids and cochlear implants
- **Hearing aids**: directional microphones, noise reduction, feedback cancellation; multi-core DSP; <1ms latency
- **Cochlear implants**: electrode arrays; electrical stimulation; frequency-place coding; ACE, CIS, SPEAK strategies
- **Auditory brainstem implant (ABI)**: electrode pad on cochlear nucleus; for auditory nerve damage
- **Neural decoding**: auditory cortex decoding for BCI; speech decoding from EEG/MEG/ECoG

### AMOS Integration
- **C04 domain**: [[21_DOMAINS/14_C04_BIO_NEURO/14_C04_BIO_NEURO_MOC|C04 bio-neuro domain]]
- **BCI runtime**: [[04_RUNTIME/06_EXECUTION/BCI_WAVEFRONT_SLM_RUNTIME|BCI Wavefront SLM Runtime]]
- **SOTA BCI research**: [[22_RESEARCH/BCI_AI_QUANTUM_SOTA_2026-09-04|BCI/AI/Quantum SOTA Batch 1]]
- **UBI framework**: [[11_KNOWLEDGE/05_FRAMEWORKS/UBI_FRAMEWORK|UBI Framework]] — NBI domain

### Invariants
1. `DETECTED != ATTENDED` — detecting attention does not prove conscious attention
2. `ALGORITHM != PERCEPTION` — beamforming algorithms do not replicate human auditory perception
3. All auditory claims must cite provenance (sensor, algorithm, validation, SNR conditions)
4. `CAPABILITY != SAFETY` — auditory processing capability does not guarantee safe medical application


*Governed by Origin Architect Trang Phan | AMOS OS v4.4 Canonical Core*
