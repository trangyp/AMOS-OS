---
title: "Kojensi Case Study: Secure Multi-Agency Classified Collaboration"
type: case_study
source: 21_DOMAINS/59_SECURITY
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_CASE_STUDY
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - "Google Drive/Kojensi Case Study — Secure Classified Collaboration.gdoc"
    - 21_DOMAINS/00_INDEX/DOMAIN_EXTENSION_PROTOCOL
  scope: classified_security_collaboration
tags:
  - amos-os
  - domains
  - security
  - classified-collaboration
  - kojensi
---

# Kojensi Case Study: Secure Multi-Agency Classified Collaboration

> **Origin Architect / Steward:** Trang Phan
> **Target Core Lineage:** `v4.4`
> **Domain Family:** `C09: SECURITY & DEFENSE`

---

## 1. Context & Operational Challenge

Government defense agencies, sovereign intelligence services, and private contractors require cross-organizational collaboration on classified programs (Protected, Secret, Top Secret) without risking unauthorized lateral data movement or compartment breaches.

The challenge is threefold:
1. **Lateral Movement Prevention:** No user, even with valid credentials, may traverse between sovereign tenant compartments without explicit, cryptographically verified authorization.
2. **Provenance Non-Repudiation:** Every intelligence product must carry an immutable provenance chain identifying origin, handling caveats, and all downstream consumers.
3. **Cross-Domain Transfer Control:** Information moving between classification levels must pass through validated guard mechanisms with full audit trails.

```text
CLEARANCE != ACCESS
COMPARTMENT != TENANT
PROVENANCE != METADATA
```

---

## 2. Architectural Scope

This case study maps the Kojensi multi-level security platform onto the AMOS security envelope, demonstrating how AMOS architectural primitives (capability tokens, enforcement root attestation, delegation witnesses) translate to real-world classified collaboration requirements.

### 2.1 MECE Partition Mapping

| AMOS Plane | Role in Case Study |
| :--- | :--- |
| `18_SECURITY` | Cryptographic enforcement, ABAC, watermarking, PQC readiness |
| `03_CONTROL_PLANE` | Capability token issuance, epoch leases, authority delegation |
| `09_PROTOCOLS` | Cross-domain transfer protocols, BFT consensus for audit logs |
| `12_STATE` | Compartment-isolated state shards, MVCC for concurrent access |
| `17_OBSERVABILITY` | Immutable audit trail, provenance nonces, tamper-evident logging |
| `23_OPERATING_MODEL` | Decision rights for classification level changes, escalation paths |

---

## 3. Zero-Trust Cryptographic Enforcement

The AMOS security envelope integrates with Kojensi multi-level security protocols:

### 3.1 Attribute-Based Access Control (ABAC)

Cryptographic verification of user security clearance, citizenship, nationality caveats, and need-to-know tokens. Each access decision evaluates a multi-dimensional policy vector:

$$\text{Access}(u, r, o) = \bigwedge_{i} P_i(\text{attr}_u, \text{attr}_r, \text{attr}_o)$$

Where $P_i$ are independent policy predicates covering clearance level, compartment membership, nationality caveat, need-to-know token validity, and temporal access window. All predicates must evaluate to TRUE; any FALSE result triggers fail-closed denial.

### 3.2 Deterministic Information Barriers

Complete physical and logical isolation between sovereign tenants. State shards are partitioned by tenant identity with zero shared memory regions. Cross-tenant communication is mediated exclusively through validated cross-domain guard protocols.

### 3.3 Immutable Watermarking & Export Control

Cryptographically watermarks all exported intelligence capsules with auditable provenance nonces. Each export generates a BLAKE3 receipt binding the exporter identity, export timestamp, content hash, and classification level:

$$\mathcal{R}_{\text{export}} = \text{BLAKE3}(\text{ExporterID} \parallel \text{Timestamp} \parallel \text{ContentHash} \parallel \text{ClassificationLevel})$$

---

## 4. Enforcement Trust Contract Integration

The AMOS Enforcement Trust Contract (ETC v43) provides the trust chain verification that prevents zombie-agent and supply-chain attacks in classified environments:

- **Policy Artifact Verification:** Kojensi policy artifacts must carry Sigstore/Cosign-class signatures validated against approved signer identities.
- **Delegation Witness:** Temporal, revocable delegation chains ensure that revoked clearances propagate immediately to all downstream sessions.
- **Enforcement Root Attestation:** The enforcement mechanism itself is measured and verified, ensuring that the access control engine has not been tampered with.

$$\text{MayExternalize}_{\text{v43}} = \text{MayExternalize}_{\text{v42}} \wedge \text{EnforcementTrustContractValid} \wedge \text{DelegationWitnessValid}$$

---

## 5. Cross-Domain Transfer Protocol

Information transfer between classification levels follows a guarded pipeline:

1. **Source Validation:** Export request verified against source compartment ABAC policy.
2. **Content Sanitization:** Automated classification review identifies and redacts content above the target classification level.
3. **Guard Verification:** Independent guard service validates sanitization completeness and issues transfer receipt.
4. **Destination Injection:** Content injected into target compartment with provenance chain linking to source export receipt.
5. **Audit Seal:** Both source and destination audit logs sealed with BFT consensus quorum.

---

## 6. Safety Invariants

- `INV-SEC-KOJ-001` (**Lateral Movement Prevention**): No user session may access resources outside its verified compartment, regardless of credential validity.
- `INV-SEC-KOJ-002` (**Provenance Non-Repudiation**): All intelligence products carry immutable provenance chains; provenance records cannot be modified or deleted.
- `INV-SEC-KOJ-003` (**Fail-Closed on Ambiguity**): Any access decision with incomplete attribute evaluation results in denial, not admission.
- `INV-SEC-KOJ-004` (**Revocation Propagation**): Clearance revocation must propagate to all active sessions within one epoch tick.

---

## 7. Navigation & Bindings

- **Security Plane:** [[18_SECURITY/18_SECURITY_MOC|18_SECURITY_MOC]]
- **Control Plane Contracts:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
- **Protocols Plane:** [[09_PROTOCOLS/09_PROTOCOLS_MOC|09_PROTOCOLS_MOC]]
- **State Plane:** [[12_STATE/12_STATE_MOC|12_STATE_MOC]]
- **Observability Plane:** [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY_MOC]]
- **Operating Model:** [[23_OPERATING_MODEL/OPERATING_MODEL_README|OPERATING_MODEL_README]]
- **Domain Hub:** [[21_DOMAINS/21_DOMAINS_MOC|21_DOMAINS_MOC]]
- **Domain Extension Protocol:** [[21_DOMAINS/00_INDEX/DOMAIN_EXTENSION_PROTOCOL|DOMAIN_EXTENSION_PROTOCOL]]

---

## 8. Known Gaps

- **Air-Gap Integration:** The case study assumes network-connected deployment. Fully air-gapped sovereign environments require offline synchronization protocols not yet specified.
- **Post-Quantum Migration:** Current Kojensi deployments use classical cryptography (RSA-4096, AES-256). Migration to NIST FIPS 203 (ML-KEM) is specified but not deployed.
- **Multi-Level Classification Automation:** Automated content sanitization across classification levels remains `UNKNOWN/GAP` for complex multimedia intelligence products.
- **Epistemic Boundary:** `DOCUMENTED != IMPLEMENTED` — the enforcement mechanisms described here are architectural specifications. Production Kojensi deployments may implement subsets of these controls.
