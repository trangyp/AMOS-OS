---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: 18 Security Moc
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# 18 Security — Map of Content

> [!ABSTRACT] Security Plane Executive Summary
> The **Security Plane** (`18_SECURITY`) owns protected boundaries, programmatic access control (DAC, MAC, RBAC), capability token validation, Sybil hardening, and runtime policy enforcement in the AMOS Full Brain OS.
> It enforces the invariant:
> $$\text{CAPABILITY} \neq \text{AUTHORITY} \quad\land\quad \text{TRUST SCORE} \neq \text{ROOT KEY}$$

---

## 1. Core Subsystem Architecture

* [[18_SECURITY/SECURITY_CONTROL_ACCESS_BRIDGE_GOVERNOR|Security Control Access Bridge Governor]] — The C09 $\to$ C10 $\to$ Runtime bridge enforcing Bounded Intelligence Security (BIS), the 10 Security QA Gates, and policy-to-enforcement drift detection.
* [[18_SECURITY/SECURITY_SECURITY_CONTRACT|SECURITY_SECURITY_CONTRACT]] — Formal security plane boundary contracts and threat models.
* [[18_SECURITY/SECURITY_README|SECURITY_README]] — Structural overview and sibling map.

---

## 2. Inbound & Outbound Interfaces

* **Control Plane Gates:** [[03_CONTROL_PLANE/04_AUTHORITY/AUTHZ_ENGINE_VALIDATION_RECEIPT|AUTHZ Engine Validation Receipt]].
* **Runtime Sandbox:** [[04_RUNTIME/04_RUNTIME_MOC|04_RUNTIME_MOC]].
* **Cryptographic Law:** [[01_CANON/01_CORE_LAWS/L7_AUTHORITY|L7_AUTHORITY]].

---
[[00_ROOT/00_ROOT_MOC|Root MOC]] · [[AMOS_HOME|AMOS Home]]
