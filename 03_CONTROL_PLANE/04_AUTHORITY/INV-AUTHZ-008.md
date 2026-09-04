---
title: INV-AUTHZ-008 — Non-Repudiation of Tool Receipts
type: authority_invariant
source: 03_CONTROL_PLANE/04_AUTHORITY
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_INVARIANT
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT
    - 01_CANON/01_CORE_LAWS/LAW_HIERARCHY
  scope: authority_governance
tags:
  - amos-os
  - authority
  - invariant
  - control-plane
  - inv-authz-008
---

# INV-AUTHZ-008 — Non-Repudiation of Tool Receipts

## 1. Formal Specification

> **Invariant Statement:**
> `Every external tool execution must produce an immutable signed receipt in 17_OBSERVABILITY.`

## 2. Invariant Rule & Mathematical Formulation

Let $\mathcal{E}$ be the set of external tool executions, $\text{Receipt}(e)$ the receipt for execution $e$, and $\text{Sign}(e)$ the cryptographic signature binding the executor to the receipt:

$$\forall e \in \mathcal{E}, \quad \exists r \in \text{Receipts} : \text{Bind}(r, e) \land \text{VerifySig}(\text{Sign}(e), r) = \text{True}$$

The non-repudiation property requires that once a receipt is written, the executor cannot deny having performed the action:

$$\forall e \in \mathcal{E}, \quad \text{Repudiate}(\text{Executor}(e), e) = \text{False}$$

The receipt content hash is:

$$h(r) = \text{BLAKE3}(\text{ToolID} \parallel \text{ExecutorID} \parallel \text{InputHash} \parallel \text{OutputHash} \parallel \text{Epoch} \parallel \text{Timestamp})$$

and the receipt chain requires:

$$\text{PrevHash}(r_i) = h(r_{i-1})$$

## 3. Enforcement & Verification

- **Evaluation Point:** Evaluated at the completion of every external tool execution. The Control Plane gate blocks the tool's output from being consumed until the receipt is written and verified.
- **Violation Consequence:** If a tool execution completes without a receipt, the tool output is discarded. A `MISSING_RECEIPT_VIOLATION` is emitted to `17_OBSERVABILITY`. The tool is flagged for re-execution under stricter monitoring.
- **Recovery Procedure:** The tool execution is replayed with receipt generation enforced. If the tool cannot produce a receipt, its capability token is revoked per [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-004|INV-AUTHZ-004]].
- **Verification Cadence:** Synchronous at every tool execution completion. A periodic audit verifies the receipt chain integrity by checking hash links.
- **Governed By:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

## 4. Attack Vectors & Mitigations

- **Receipt Suppression:** A tool execution completes but the executor suppresses receipt generation to hide its actions. Mitigated by the Control Plane gate blocking output consumption until the receipt is verified.
- **Receipt Tampering:** An attacker modifies a receipt after it is written to alter the recorded tool output. Mitigated by the BLAKE3 hash chain and cryptographic signature on each receipt, plus [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-020|INV-AUTHZ-020]] audit trail immutability.
- **Receipt Repudiation:** An executor denies having performed a recorded action. Mitigated by the Ed25519 signature binding the executor's identity to the receipt, making repudiation cryptographically impossible.
- **Fake Receipt Injection:** An attacker injects fabricated receipts to create a false audit trail. Mitigated by the hash chain requirement that each receipt must link to the previous one, and by signature verification of the claimed executor.

## 5. Dependencies & Prerequisites

- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-018|INV-AUTHZ-018]] — Cryptographic token integrity ensures executor signatures are authentic.
- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-020|INV-AUTHZ-020]] — Audit trail immutability prevents receipt modification after writing.
- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-014|INV-AUTHZ-014]] — Monotonic provenance ledger ensures the receipt chain is append-only.
- **Requires:** Ed25519 signing capability for every tool executor.
- **Requires:** BLAKE3 hashing infrastructure for receipt content addressing.

## 6. Provenance & Audit Trail

- **Receipt Type:** `TOOL_EXECUTION_RECEIPT` — emitted for every external tool execution.
- **Storage Location:** `17_OBSERVABILITY` with tool-ID-indexed and executor-indexed partitions.
- **Receipt Fields:** Tool ID, executor identity, input hash, output hash, epoch, timestamp, Ed25519 signature, previous receipt hash, BLAKE3 content hash.
- **Immutability:** Tool execution receipts are append-only per [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-014|INV-AUTHZ-014]] and protected by [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-020|INV-AUTHZ-020]].

## 7. Related Invariants

- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-004|INV-AUTHZ-004]] — Explicit Revocation Immediacy
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-011|INV-AUTHZ-011]] — Sandboxed Execution Confinement
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-014|INV-AUTHZ-014]] — Monotonic Provenance Ledger
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-018|INV-AUTHZ-018]] — Cryptographic Token Integrity
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-020|INV-AUTHZ-020]] — Audit Trail Immutability

## 8. Navigation & Bindings

- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
- **Control Plane Contract:** [[03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT|CONTROL_PLANE_CONTRACT]]
- **Canon Law Hierarchy:** [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- **Kernel:** [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]]
- **Observability:** [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY_MOC]]
