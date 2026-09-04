---
title: "INV-AUTHZ-013 — Anti-Poisoning Invariant"
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
  - inv-authz-013
---

# INV-AUTHZ-013 — Anti-Poisoning Invariant

## 1. Formal Specification

> **Invariant Statement:**
> `No external unverified data stream may directly write into 01_CANON or 02_KERNEL.`

## 2. Invariant Rule & Mathematical Formulation

Let $\mathcal{D}_{\text{ext}}$ be the set of external data streams, $\text{Verified}(d)$ the verification status of stream $d$, and $\text{Target}(d)$ the write destination:

$$\forall d \in \mathcal{D}_{\text{ext}}, \quad \text{Target}(d) \in \{\text{01\_CANON}, \text{02\_KERNEL}\} \implies \text{Verified}(d) = \text{True}$$

The verification pipeline requires multiple stages:

$$\text{Verified}(d) = \text{SchemaValid}(d) \land \text{ProvenanceTraced}(d) \land \text{ContentScanned}(d) \land \text{GatekeeperApproved}(d)$$

The data flow constraint prohibits any direct path from external sources to canon or kernel:

$$\nexists \text{Path}(d, \text{01\_CANON}) : \text{Source}(d) \in \mathcal{D}_{\text{ext}} \land \neg \text{Verified}(d)$$

$$\nexists \text{Path}(d, \text{02\_KERNEL}) : \text{Source}(d) \in \mathcal{D}_{\text{ext}} \land \neg \text{Verified}(d)$$

## 3. Enforcement & Verification

- **Evaluation Point:** Evaluated at the data ingestion barrier, which sits between external data sources and the internal vault structure. Every write to `01_CANON` or `02_KERNEL` is intercepted and checked for source verification.
- **Violation Consequence:** If an unverified external data stream attempts to write to canon or kernel, the write is blocked. A `DATA_POISONING_ATTEMPT` receipt is emitted to `17_OBSERVABILITY`. The source is flagged and may be blacklisted.
- **Recovery Procedure:** The data must pass through the full verification pipeline before reattempting the write. If the source is blacklisted, a manual review by a gatekeeper is required to unblock it.
- **Verification Cadence:** Synchronous at every write to canon or kernel. A periodic audit scans the canon and kernel for any content that bypassed the verification pipeline.
- **Governed By:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

## 4. Attack Vectors & Mitigations

- **Direct Data Injection:** An attacker sends data directly to the canon or kernel write interface, bypassing the verification pipeline. Mitigated by the ingestion barrier that intercepts all writes and checks source verification.
- **Pipeline Bypass via Privilege Escalation:** An attacker gains elevated privileges to write directly to canon. Mitigated by [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-005|INV-AUTHZ-005]] preventing self-escalation and [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-006|INV-AUTHZ-006]] requiring multi-party authorization for canon mutations.
- **Verified Source Spoofing:** An attacker compromises a verified external source to inject poisoned data. Mitigated by the multi-stage verification that includes content scanning and provenance tracing, not just source identity.
- **Schema-Valid Poisoning:** An attacker crafts data that passes schema validation but contains semantically malicious content. Mitigated by the content scanning stage that performs semantic analysis beyond schema validation.

## 5. Dependencies & Prerequisites

- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-006|INV-AUTHZ-006]] — Multi-party authorization for canon adds an additional layer of protection.
- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-031|INV-AUTHZ-031]] — Schema validation gating provides the first stage of the verification pipeline.
- **Depends On:** [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-011|INV-AUTHZ-011]] — Sandboxed execution confinement ensures external tools processing data are isolated.
- **Requires:** A data ingestion barrier with write interception capability.
- **Requires:** A multi-stage verification pipeline including schema, provenance, content, and gatekeeper approval.

## 6. Provenance & Audit Trail

- **Receipt Type:** `DATA_INGESTION_RECEIPT` — emitted for every data write to canon or kernel, recording the source, verification pipeline results, and approval status.
- **Storage Location:** `17_OBSERVABILITY` with source-indexed and target-indexed partitions.
- **Receipt Fields:** Source identity, target path, schema validation result, provenance trace, content scan result, gatekeeper approval, write decision, epoch, BLAKE3 hash.
- **Immutability:** Ingestion receipts are append-only per [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-014|INV-AUTHZ-014]].

## 7. Related Invariants

- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-006|INV-AUTHZ-006]] — Multi-Party Authorization for Canon
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-011|INV-AUTHZ-011]] — Sandboxed Execution Confinement
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-031|INV-AUTHZ-031]] — Schema Validation Gating
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-012|INV-AUTHZ-012]] — Reality Grounding Requirement
- [[03_CONTROL_PLANE/04_AUTHORITY/INV-AUTHZ-048|INV-AUTHZ-048]] — Popperian Falsification Floor

## 8. Navigation & Bindings

- **Control Plane:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
- **Control Plane Contract:** [[03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT|CONTROL_PLANE_CONTRACT]]
- **Canon Law Hierarchy:** [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- **Kernel:** [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]]
- **Observability:** [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY_MOC]]
