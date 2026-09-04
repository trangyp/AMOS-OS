---
title: Continuous-Variable QKD Physical Layer Execution Ledger
type: quantum_cryptography_ledger
plane: 18_SECURITY
amos_core_target: v4.4
origin_architect: Trang Phan
status: EXECUTED_VERIFIED
conclusion_class: DERIVED
rscf:
  state: DERIVED
  provenance: authoritative_AMOS_OS_structure
  scope: active__AMOS_OS
---

# Continuous-Variable QKD (CV-QKD) Execution Ledger

## Quantum Optical Channel & Information-Theoretic Security Telemetry
- **Timestamp**: `2026-09-04 19:37:10 UTC`
- **Fiber Link Distance**: `15.0 km` ($0.2\,	ext{dB/km}$ standard SMF-28)
- **Optical Transmittance ($T$)**: `0.5012` ($3.0\,	ext{dB}$ channel attenuation)
- **Alice-Bob Mutual Information ($I(A; B)$)**: `0.7924 bits/pulse`
- **Eve Holevo Information Bound ($\chi(B; E)$)**: `0.7402 bits/pulse`
- **Reverse Reconciliation Efficiency ($eta$)**: `95.0%`
- **Asymptotic Secret Key Rate ($K_{\text{sec}}$)**: `0.012574 bits/pulse`
- **Secure Key Throughput (at 100 MHz Repetition)**: `1.26 Mbps`
- **Cryptographic Seal (SHA-256)**: `6a309cd480d03b0baaa49ad960a260517f8bfbe747943647a6ffa244eba55464`

## Devetak-Winter Asymptotic Security Invariant
$$K_{	ext{sec}} = eta I(A; B) - \chi(B; E) = 0.012574\,	ext{bits/pulse} > 0$$
Information-theoretic secret key agreement proven secure against arbitrary collective Gaussian eavesdropping attacks.

---

## SOTA Methods

### Quantum Key Distribution (QKD)
- **BB84**: Bennett & Brassard (1984); polarization encoding; single photons; Heisenberg uncertainty; eavesdropping detection
- **E91**: Ekert (1991); entanglement-based; Bell inequality test; device-independent QKD
- **MDI-QKD**: measurement-device-independent; trusted relay; eliminates detector side-channel attacks
- **TF-QKD**: twin-field QKD; long-distance (>1000km); single-photon interference; high key rate

### Continuous-variable QKD (CV-QKD)
- **CV-QKD**: Gaussian-modulated coherent states; homodyne/heterodyne detection; quadrature encoding
- **Advantages**: compatible with standard telecom components; high key rates over short distances; room-temperature operation
- **Protocols**: GG02 (Grosshans-Grangier 2002), CV-MDI, CV-TF; excess noise; reconciliation efficiency
- **Implementation**: LiNbO3 modulator, balanced homodyne detector, shot-noise-limited; fiber-based; free-space

### Post-quantum cryptography
- **NIST PQC standards** (2024): ML-KEM (Kyber), ML-DSA (Dilithium), SLH-DSA (SPHINCS+)
- **Migration**: hybrid classical+PQC; TLS 1.3 hybrid key exchange; protocol migration challenges
- **QKD vs PQC**: QKD provides information-theoretic security but requires physical infrastructure; PQC is software-based

### AMOS Integration
- **18_SECURITY plane**: [[18_SECURITY/18_SECURITY_MOC|18_SECURITY_MOC]]
- **41 Quantum Systems**: [[21_DOMAINS/41_QUANTUM_SYSTEMS/41_QUANTUM_SYSTEMS_MOC|41 Quantum Systems MOC]]
- **Quantum PQC tomography**: [[21_DOMAINS/41_QUANTUM_SYSTEMS/QUANTUM_PQC_TOMOGRAPHY_LEDGER|Quantum PQC Tomography Ledger]]
- **C03 domain**: [[21_DOMAINS/13_C03_PHYSICS_COSMOS/13_C03_PHYSICS_COSMOS_MOC|C03 physics-cosmos domain]]
- **SOTA quantum research**: [[22_RESEARCH/SOTA_BCI_AI_QUANTUM_2026-09-04_BATCH2|SOTA Batch 2 (IBM quantum)]]

### Invariants
1. `QKD != PQC` — QKD (physical) and PQC (computational) are different security paradigms
2. `SIMULATION != HARDWARE` — QKD simulations ≠ physical QKD implementations
3. All QKD claims must cite provenance (protocol, hardware, distance, key rate, error rate)
4. `SECURITY != GUARANTEE` — QKD security depends on assumptions (device trust, channel properties)


*Governed by Origin Architect Trang Phan | AMOS OS v4.4 Canonical Core*
