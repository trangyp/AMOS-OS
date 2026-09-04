---
title: Authority Kernel Contract — Subplane Governance Specification
type: specification
source: 02_KERNEL/07_AUTHORITY
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_SPECIFICATION
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 02_KERNEL/KERNEL_KERNEL_CONTRACT
    - 01_CANON/01_CORE_LAWS/CANON_CORE_LAWS_CONTRACT
    - 18_SECURITY/SECURITY_SECURITY_CONTRACT
    - 00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE
  scope: subplane_governance
tags:
  - amos-os
  - 02-kernel
  - authority
  - specification
---

# Authority Kernel Contract — Subplane Governance Specification

> **Origin Architect / Steward:** Trang Phan
> **AMOS_CORE Target:** `v4.4`
> **Epistemic Class:** `AMOS_MODEL`
> **Status:** `ACTIVE_SPECIFICATION`

---

## 1. Architectural Scope & Purpose

`KERNEL_AUTHORITY_CONTRACT` defines the cryptographic capability-based access control (CapBAC), permission delegation calculi, Macaroon attenuation tokens, and steward authority verification gates inside the AMOS Kernel. It enforces the fundamental invariant `CAPABILITY != AUTHORITY`, preventing unprivileged subagents or external actors from executing privileged state transformations.

---

## 2. Mathematical Foundations & Capability Calculus

An Authority Token (Macaroon) $\mathcal{T}_{\text{auth}}$ is formalized as:

$$\mathcal{T}_{\text{auth}} = \langle \text{Location}, \text{Identifier}, \mathcal{C}_{\text{caveats}}, \sigma_{\text{signature}} \rangle$$

Where:
- $\text{Location}$ specifies the target plane / service URI.
- $\text{Identifier}$ is a 128-bit cryptographic nonce.
- $\mathcal{C}_{\text{caveats}} = [ c_1, c_2, \dots, c_k ]$ is an ordered list of first-party and third-party attenuation predicates:
  $$c_i : (\text{Request}, \text{Context}) \to \{ \text{True}, \text{False} \}$$
- $\sigma_{\text{signature}} = \text{HMAC-SHA256}(K_{\text{root}}, \text{Identifier} \mathbin{\Vert} c_1 \mathbin{\Vert} \dots \mathbin{\Vert} c_k)$ is the chained cryptographic signature.

### Invariant 1: Attenuation Monotonicity
Any subagent holding token $\mathcal{T}$ can only restrict (attenuate) permissions by appending caveat $c_{k+1}$; it can never expand permissions:
$$\text{Perm}(\mathcal{T} \cup \{ c_{k+1} \}) \subseteq \text{Perm}(\mathcal{T})$$

### Invariant 2: Steward Origin Sovereignty
Canonical-tier operations ($\mathcal{P}_{\text{canon}}$) require signature verification from the root key belonging to origin architect **Trang Phan**:
$$\text{Commit}(\mathcal{P}_{\text{canon}}) \implies \text{VerifySig}(K_{\text{Trang Phan}}, \text{CommitPayload}) = \text{True}$$

---

## 3. Epistemic Invariants & Security Boundaries

1. **`CAPABILITY != AUTHORITY`**: Possessing a tool or memory pointer does not grant permission to execute it without an unexpired, unrevoked capability token.
2. **Fail-Closed Gate:** Missing, malformed, or expired tokens reject with zero side-effects.
3. **Revocation Propagation:** Revocation of parent token immediately invalidates all attenuated child tokens via distributed epoch counters.

---

## 4. Execution Mechanics & Capability Verification Pipeline

```text
[Inbound Execution Request (Agent / API / BCI)]
                     │
                     ▼
       [Macaroon Chained HMAC Validator] ──► [Invalid Sig? -> Trap & Log Security Alert]
                     │ (Valid Sig)
                     ▼
      [Contextual Caveat Evaluator (Time, Plane, Rate)]
                     │
                     ▼
      [Revocation Bloom Filter Check] ───► [Revoked? -> Reject]
                     │ (Active)
                     ▼
         [Grant Capability Lock & Dispatch]
```

---

## 5. Failure Modes & Degradation

- **Replay Attack:** Re-sending an intercepted token. **Mitigation:** Strict nonce check and tight $\Delta t_{\text{validity}} \le 30\,\text{s}$ expiration windows.
- **Privilege Escalation Attempt:** Tampering with caveat chain. **Mitigation:** Chained HMAC breaks; immediate process quarantine and lock-out.

---

## 6. Cross-Plane Bindings

- **`01_CANON/01_CORE_LAWS`**: Enforces Authority Law.
- **`06_AGENTS`**: Limits agent privileges in [[06_AGENTS/AGENTS_AGENT_CONTRACT|AGENTS_AGENT_CONTRACT]].
- **`14_TOOLS`**: Wraps tool invocation in sandbox capability checks.
- **`18_SECURITY`**: Root key management and KMS integration.

---

## 7. Verification & Formal Invariants

Formal verification of Macaroon attenuation in Lean 4:
$$\forall (T : \text{Macaroon}) (c : \text{Caveat}), \quad \text{AccessSet}(T \circ c) \subseteq \text{AccessSet}(T)$$

---

## 8. Lineage & Stewardship

- **Origin Architect:** Trang Phan
- **Steward:** Trang Phan
- **Target:** `v4.4`

---

## 9. Attestation Metadata

```yaml
subplane: 02_KERNEL/07_AUTHORITY
contract_status: ACTIVE_SPECIFICATION
steward: Trang Phan
verification_status: CRYPTOGRAPHICALLY_LOCKED
```
