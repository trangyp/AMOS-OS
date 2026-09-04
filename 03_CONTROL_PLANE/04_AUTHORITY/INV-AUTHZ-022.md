---
title: INV-AUTHZ-022 — No Silent Failure
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
  - inv-authz-022
---

# INV-AUTHZ-022 — No Silent Failure

## 1. Formal Specification

> **Invariant Statement:**
> `All failed transactions must emit structured error records explaining the exact violated invariant.`

## 2. Invariant Rule & Mathematical Formulation

Let $\mathcal{F}$ be the set of failed transactions, $\text{ErrorRecord}(f)$ the error record for failure $f$, and $\text{Invariant}(f)$ the violated invariant:

$$\forall f \in \mathcal{F}, \quad \exists r \in \text{ErrorRecords} : \text{Bind}(r, f) \land \text{Specifies}(r, \text{Invariant}(f))$$

The error record must be structured and contain minimum required fields:

$$\text{Valid}(r) \iff \text{TransactionID}(r) \neq \emptyset \land \text{InvariantID}(r) \neq \emptyset \land \text{ErrorDescription}(r) \neq \emptyset \land \text{Timestamp}(r) \neq \emptyset$$

No failure may occur without an error record:

$$\text{Fail}(T) \implies \exists r : \text{Emitted}(r, T) \land \text{Stored}(r, \text{17\_OBSERVABILITY})$$

The error emission is synchronous with the failure:

$$\text{Time}(\text{Emit}(r)) \le \text{Time}(\text{Fail}(T)) + \epsilon_{\text{emit}}$$

where $\epsilon_{\text{emit}} \to 0$.

## 3. Enforcement & Verification

- **Evaluation Point:** Evaluated at the transaction failure handler in the Control Plane. When a transaction fails, the handler must emit a structured error record before returning control to the caller.
- **Violation Consequence:** If a transaction fails without emitting an error record, the system treats this as a meta-failure. A `SILENT_FAILURE_VIOLATION` receipt is emitted by the meta-failure detector. The transaction is force-rolled back.
- **Recovery Procedure:** The failed transaction is rolled back using the pre-allocated rollback basin per [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-010|INV-AUTHZ-010]]. The error record guides the recovery procedure by identifying the violated invariant.
- **Verification Cadence:** Synchronous at every transaction failure. A periodic audit scans for transactions that failed without corresponding error records.
- **Governed By:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

## 4. Attack Vectors & Mitigations

- **Silent Failure Suppression:** An agent suppresses error records to hide failed transactions and their causes. Mitigated by the synchronous emission requirement that forces error record generation before control returns.
- **Error Record Vagueness:** An agent emits an error record with vague or missing invariant identification. Mitigated by the structured format requirement that mandates specific fields including the invariant ID.
- **Error Record Loss:** An error record is lost due to storage failure. Mitigated by replicated storage of error records and by the meta-failure detector that identifies missing records.
- **Error Record Flooding:** An attacker triggers massive numbers of failures to flood the error record storage. Mitigated by rate limiting and by [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-040|INV-AUTHZ-040]] resource exhaustion failsafe.

## 5. Dependencies & Prerequisites

- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-010|INV-AUTHZ-010]] — Rollback basin pre-condition ensures failed transactions can be rolled back.
- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-020|INV-AUTHZ-020]] — Audit trail immutability ensures error records cannot be modified after emission.
- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-014|INV-AUTHZ-014]] — Monotonic provenance ledger ensures error records are append-only.
- **Requires:** A structured error record format with mandatory fields.
- **Requires:** A synchronous error emission mechanism in the transaction failure handler.

## 6. Provenance & Audit Trail

- **Receipt Type:** `STRUCTURED_ERROR_RECORD` — emitted for every failed transaction, recording the transaction ID, violated invariant, error description, and timestamp.
- **Storage Location:** `17_OBSERVABILITY` with transaction-ID-indexed and invariant-ID-indexed partitions.
- **Receipt Fields:** Transaction ID, violated invariant ID, error description, error category, timestamp, agent identity, state hash at failure, BLAKE3 hash.
- **Immutability:** Error records are append-only per [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-014|INV-AUTHZ-014]] and protected by [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-020|INV-AUTHZ-020]].

## 7. Related Invariants

- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-009|INV-AUTHZ-009]] — Quarantine on Anomaly
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-010|INV-AUTHZ-010]] — Rollback Basin Pre-condition
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-014|INV-AUTHZ-014]] — Monotonic Provenance Ledger
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-017|INV-AUTHZ-017]] — Fail-Closed on Desync
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-020|INV-AUTHZ-020]] — Audit Trail Immutability

## 8. Navigation & Bindings

- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
- **Control Plane Contract:** [[03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT|CONTROL_PLANE_CONTRACT]]
- **Canon Law Hierarchy:** [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- **Kernel:** [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]]
- **Observability:** [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY_MOC]]
