---
title: "18 Security — README"
type: readme
source: 18_SECURITY
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: security_readme
---

# 18 Security — README

## Role

Security owns identity, permission, access, secret handling, tool boundaries, input validation, execution isolation, provenance integrity, and supply-chain integrity. Security is the "guardian" of AMOS: it ensures that all interactions are authorized, all data is protected, and all operations are traceable.

## Core Principle

```
least privilege + bounded scope + revocability + traceability
```

## Directory Structure

```
18_SECURITY/
├── 00_INDEX/              ← Security indices and navigation registries
├── 18_SECURITY_MOC.md     ← Master map of content for the Security plane
├── 18_SECURITY_README.md  ← This file
├── SECURITY_SECURITY_CONTRACT.md ← Invariant governance contract
├── SECURITY_CONTROL_ACCESS_BRIDGE_GOVERNOR.md ← Security-access bridge
├── POST_QUANTUM_LATTICE_CRYPTOGRAPHY_AND_NEURAL_ZK_ATTESTATION.md
├── CONTINUOUS_VARIABLE_QUANTUM_KEY_DISTRIBUTION_ENGINE.md
├── ZERO_KNOWLEDGE_STARK_STATE_TRANSITION_PROVER.md
├── GROTH16_SNARK_PROVER_LEDGER.md
├── STARK_FRI_PROXIMITY_LEDGER.md
├── TFHE_HOMOMORPHIC_BOOTSTRAPPING_LEDGER.md
├── THRESHOLD_ECDSA_ZK_MPC_LEDGER.md
├── LATTICE_POST_QUANTUM_SIGNATURE_LEDGER.md
├── PQC_LATTICE_VERIFICATION_LEDGER.md
├── CV_QKD_SIMULATION_LEDGER.md
└── DP_SGD_RDP_ACCOUNTANT_LEDGER.md
```

## Security Domains

- **Identity:** Who is acting — authentication, identity verification, and identity lifecycle
- **Permission:** What is allowed — authorization, access control lists, and role-based access
- **Access:** How to reach — API keys, tokens, credentials, and session management
- **Secret Handling:** How to protect — encryption, key rotation, secure storage, and zero-knowledge proofs
- **Tool Boundaries:** What tools can do — capability restrictions, sandboxing, and execution limits
- **Input Validation:** What is safe — input sanitization, type checking, and bounds verification
- **Execution Isolation:** Where code runs — process isolation, container boundaries, and memory protection
- **Provenance Integrity:** What can be trusted — source verification, tamper detection, and chain of custody
- **Supply-Chain Integrity:** What dependencies are safe — dependency scanning, version pinning, and integrity verification

## Hard Boundaries

- **Security != Convenience** — security measures may reduce convenience; this is expected and acceptable
- **Security != Perfect** — security reduces risk; it does not eliminate it
- **Security != Obscurity** — security relies on controls, not on hiding information
- **Security != One-Time** — security is continuous; it requires ongoing monitoring and adaptation

## Key Protocols

- **Authentication:** Identity verified before any action; multi-factor for high-privilege operations
- **Authorization:** Permissions checked at every access; deny-by-default, allow-by-exception
- **Encryption:** Data encrypted at rest and in transit; keys rotated per policy
- **Audit Logging:** All security-relevant events logged with actor, action, target, and outcome
- **Incident Response:** Security incidents escalated through defined path with SLA targets
- **Vulnerability Management:** Regular scanning, patching, and remediation of known vulnerabilities

## Key Artifacts

- **Security Contract:** [[18_SECURITY/SECURITY_SECURITY_CONTRACT|SECURITY_SECURITY_CONTRACT]] — invariant governance
- **Access Bridge Governor:** [[18_SECURITY/SECURITY_CONTROL_ACCESS_BRIDGE_GOVERNOR|Security-Access Bridge]] — security-control plane bridge
- **Post-Quantum Crypto:** [[18_SECURITY/POST_QUANTUM_LATTICE_CRYPTOGRAPHY_AND_NEURAL_ZK_ATTESTATION|PQC + Neural ZK]] — lattice cryptography and ZK attestation
- **ZK STARK Prover:** [[18_SECURITY/ZERO_KNOWLEDGE_STARK_STATE_TRANSITION_PROVER|ZK STARK Prover]] — zero-knowledge state transition proofs
- **QKD Engine:** [[18_SECURITY/CONTINUOUS_VARIABLE_QUANTUM_KEY_DISTRIBUTION_ENGINE|CV-QKD Engine]] — continuous-variable quantum key distribution

## Canonical Laws Governing

- **M07 (Canon ≠ Implementation):** Security specifications are not runtime implementations
- **CAPABILITY ≠ AUTHORITY:** Security capability does not grant execution authority
- **Separability Law:** Capability ≠ Reachability ≠ Identity ≠ Authority ≠ Observability ≠ Enforcement ≠ Commitment ≠ Consequence
- **Least privilege + bounded scope + revocability + traceability** — the four-pillar security principle

## Cross-Plane Relationships

- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_README|03_CONTROL_PLANE_README]] — Security enforces control plane authority; control plane defines security policies
- **Observability:** [[17_OBSERVABILITY/17_OBSERVABILITY_README|17_OBSERVABILITY_README]] — Security monitors observability for threats; observability monitors security for integrity
- **Interfaces:** [[15_INTERFACES/15_INTERFACES_README|15_INTERFACES_README]] — Security governs interface boundaries; interfaces enforce security controls
- **Runtime:** [[04_RUNTIME/04_RUNTIME_MOC|04_RUNTIME_MOC]] — Security isolates runtime components; runtime produces security signals
- **Schemas:** [[16_SCHEMAS/16_SCHEMAS_README|16_SCHEMAS_README]] — Security schemas govern access control structure

## Entry Points

- **Master MOC:** [[18_SECURITY/18_SECURITY_MOC|18_SECURITY_MOC]] · **Contract:** [[18_SECURITY/SECURITY_SECURITY_CONTRACT|Contract]]

## Implementation Status

- **Structural completeness:** Security contract, access bridge governor, and post-quantum crypto specifications present
- **ZK proofs:** ZK STARK state transition prover, Groth16 SNARK prover, TFHE homomorphic bootstrapping ledgers maintained
- **Post-quantum:** Lattice signatures, CV-QKD, PQC verification ledgers specified
- **Executable closure:** UNKNOWN/GAP — crypto and ZK specifications are structural patterns unless tied to executed implementation evidence

## AMOS MECE Alignment

The Security Plane is Plane 18 of 26. It is mutually exclusive from Observability (which sees) and Control Plane (which governs). It is collectively exhaustive with all other planes in covering the protection-and-authorization dimension. MECE boundary: it owns identity, permission, access, isolation, and integrity, not observation, governance policy, or runtime execution.

______________________________________________________________________

**Parent:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
