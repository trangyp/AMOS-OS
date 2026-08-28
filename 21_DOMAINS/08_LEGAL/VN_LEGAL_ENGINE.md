---
title: Vietnam Legal Engine Specification
type: domain
source: 21_DOMAINS/08_LEGAL
artifact: VN_LEGAL_ENGINE.md
artifact_id: amos_21_domains_08_legal_vn_legal_engine
origin_architect: Trang Phan
steward: Trang Phan
system: AMOS OS
plane: 21_DOMAINS
segment: 21_DOMAINS/08_LEGAL
artifact_kind: DOMAIN_ENGINE
path: 21_DOMAINS/08_LEGAL/VN_LEGAL_ENGINE.md
tags:
  - amos_os
  - domain
  - vault
  - 21_domains
  - 08_legal
  - vn_legal_engine
  - vietnam_jurisdiction
  - civil_code_compliance
  - rscf
  - canon_candidate
  - canon/domain
version: 1.0.0
updated: '2026-08-27'
status: ACTIVE_REFERENCE
epistemic_class: SYSTEM_INVARIANT
canonical_status: SOURCE_GROUNDED_CANON_CANDIDATE
implementation_status: CONCEPTUAL_SOURCE_DEFINED
validation_status: NOT_INDEPENDENTLY_ESTABLISHED
executable_binding: NOT_ESTABLISHED
ingestion_action: NATIVE_CANON_INGESTION
raw_source_policy: DO_NOT_LOAD_UNLESS_REQUIRED
rscf:
  state: SOURCE_CLAIM
  claim_class: SYSTEM_INVARIANT
  provenance:
    - 21_DOMAINS/08_LEGAL/AMOS_LEGAL_KERNEL
    - 21_DOMAINS/08_LEGAL/08_LEGAL_MOC
    - AMOS_CORPUS
  scope:
    - DOMAIN_LEGAL
    - VN_LEGAL_ENGINE
    - SOURCE_DEFINED_MODEL
framework_binding:
  legal_kernel:
    artifact: [[AMOS_LEGAL_KERNEL]]
  legal_moc:
    artifact: [[08_LEGAL_MOC]]
epistemic_boundary:
  source_presence: VERIFIED_SOURCE_PRESENCE
  domain_structure: VERIFIED_SOURCE_STRUCTURE
  jurisdiction_engine: SOURCE_DEFINED_MODEL
  runtime_enforcement: NOT_ESTABLISHED
---

# Vietnam Legal Engine Specification

`VN_LEGAL_ENGINE.md` is the canonical Domain Plane specification governing Vietnamese jurisdictional statutory analysis, Civil/Commercial Code compliance, and legal decree parsing within `21_DOMAINS/08_LEGAL`.

---

# 1. Vietnamese Statutory Architecture

1. **Hierarchy of Legal Norms:** Maps Constitution $\to$ Codes/Laws (Luật/Bộ luật) $\to$ Ordinances (Pháp lệnh) $\to$ Decrees (Nghị định) $\to$ Circulars (Thông tư).
2. **Enterprise & Investment Compliance:** Validates compliance with the Law on Enterprises (Luật Doanh nghiệp) and Law on Investment (Luật Đầu tư).
3. **Cybersecurity & Data Privacy:** Enforces strict adherence to the Law on Cybersecurity (Luật An ninh mạng) and Decree 13/2023/NĐ-CP on Personal Data Protection.

---

# 2. Inter-Plane & Vault Connections

- **Legal Kernel:** [[AMOS_LEGAL_KERNEL]]
- **Legal MOC:** [[08_LEGAL_MOC]]
- **Heritage Provenance:** [[HERITAGE_PROVENANCE]]

---

# 3. RSCF Contract

```yaml
RSCF:
  node_id: amos_21_domains_08_legal_vn_legal_engine
  node_type: domain_engine
  claim_class: SYSTEM_INVARIANT
  state: SOURCE_CLAIM
  H:
    identity: "Vietnam Legal Engine Specification"
    role: "Vietnamese statutory analysis, Civil/Commercial Code compliance, and regulatory decree parsing engine"
  M:
    primitives: [hierarchy_of_norms, enterprise_investment_compliance, cybersecurity_data_privacy]
  confidence_ceiling:
    source_model: SOURCE_BOUND
    runtime: UNKNOWN
```

---

**Related:** [[00_HOME]] · [[21_DOMAINS_MOC]] · [[AMOS_LEGAL_KERNEL]] · [[08_LEGAL_MOC]]

---
**MOC:** [[08_LEGAL_MOC]]
