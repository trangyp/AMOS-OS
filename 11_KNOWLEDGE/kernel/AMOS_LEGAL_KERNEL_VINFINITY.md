---
title: "AMOS Legal Kernel vInfinity"
type: kernel
created: "2026-08-22"
origin: "Google Drive — _00_AMOS_CANON/Kernels/Governance_Risk/AMOS_Legal_Kernel_v0.json (433 lines, 15KB)"
origin_type: "SOURCE"
category: "kernel"
tags: [amos, legal, kernel, v-infinity, 25-axes, 24-dimensions, tensor, routing, governance]
---


# AMOS Legal Kernel vInfinity

## Meta
- **Engine ID**: AMOS_Legal_Kernel_vInfinity
- **Engine Type**: legal_kernel
- **Created**: 2025-11-27T09:46:55.191647+00:00
- **Name**: AMOS Legal Kernel vInfinity
- **Version**: vInfinity_Legal_Kernel_1.0.0
- **Description**: Canonical legal kernel for AMOS legal engines. Defines full axis set, 24 legal dimensions, reasoning tensor, routing logic, and governance policies. Minimal, clean, final kernel used as base for all higher legal SUPER engines.

## Axes (25 = AX01–AX25)

| Axis | Key | Name | Description | Value Source |
|------|-----|------|-------------|--------------|
| AX01 | cluster_id | Legal Domain Cluster | High-level practice area (corporate, finance, disputes, regulatory, IP/data, ESG, legal ops) | external_list:clusters_legal |
| AX02 | matter_type | Matter Type | advisory, transactional, contentious, regulatory, investigations | dimensions_24.d01_matter_type |
| AX03 | jurisdiction_scope | Jurisdiction Scope | local, multi_province, cross_border, multi_region, global | dimensions_24.d02_jurisdiction_scope |
| AX04 | client_type | Client Type | individual, sme, corporate, financial_institution, state_entity, ngo | dimensions_24.d03_client_type |
| AX05 | industry | Industry Context | general, tech, finance, energy, infrastructure, healthcare, consumer, public | dimensions_24.d04_industry |
| AX06 | risk_level | Legal Risk Level | low, moderate, high, critical | dimensions_24.d05_risk_level |
| AX07 | materiality | Financial Materiality | under_1m, 1m_10m, 10m_100m, over_100m | dimensions_24.d06_materiality |
| AX08 | time_pressure | Time Pressure | normal, expedited, urgent, emergency | dimensions_24.d07_time_pressure |
| AX09 | regulatory_intensity | Regulatory Intensity | light, medium, heavy, special_regime | dimensions_24.d08_regulatory_intensity |
| AX10 | dispute_stage | Dispute/Case Stage | none, pre_dispute, filed, trial, appeal, enforcement | dimensions_24.d09_dispute_stage |
| AX11 | contract_stage | Contract Lifecycle Stage | structuring, drafting, negotiation, signing, amendment, termination | dimensions_24.d10_contract_stage |
| AX12 | evidence_state | Evidence State | incomplete, partial, strong, forensic | dimensions_24.d11_evidence_state |
| AX13 | counterparty_profile | Counterparty Behaviour Profile | cooperative, neutral, aggressive, unknown | dimensions_24.d12_counterparty_profile |
| AX14 | document_type | Primary Document Type | mou, term_sheet, main_agreement, side_letter, policy, internal_guideline | dimensions_24.d13_document_type |
| AX15 | enforcement_forum | Enforcement/Forum | court, arbitration, mediation, regulator, mixed | dimensions_24.d14_enforcement_forum |
| AX16 | standard_level | Standard Level | local_practice, regional_best, global_best, internal_standard | dimensions_24.d15_standard_level |
| AX17 | legal_function_role | Legal Function Role | external_counsel, inhouse_counsel, regulator_interface, board_advisor | dimensions_24.d16_legal_function_role |
| AX18 | time_horizon | Outcome Time Horizon | short_term, medium_term, long_term, legacy_impact | dimensions_24.d17_time_horizon |
| AX19 | outcome_priority | Primary Outcome Priority | risk_reduction, speed, value_maximisation, relationship_protection | dimensions_24.d18_outcome_priority |
| AX20 | evidence_risk_tolerance | Evidence Risk Tolerance | low, medium, high | dimensions_24.d19_evidence_risk_tolerance |
| AX21 | documentation_style | Documentation Style | lean, standard, comprehensive | dimensions_24.d20_documentation_style |
| AX22 | discovery_exposure | Discovery/Disclosure Exposure | low, medium, high | dimensions_24.d21_discovery_exposure |
| AX23 | public_sensitivity | Public Sensitivity | low, medium, high | dimensions_24.d22_public_sensitivity |
| AX24 | governance_layer | Governance Layer | operational, management, board, regulator | dimensions_24.d23_governance_layer |
| AX25 | output_mode | Output Mode | memo, opinion, contract_markups, playbook, board_pack | dimensions_24.d24_output_mode |

## Dimensions 24 (Enumerated Values)
All 24 dimensions have explicit enumerated value sets (5–8 values each) as defined in the kernel JSON.

## Reasoning Tensor (7 Layers)
1. **doctrine_layer** — Legal rules, statutes, precedents
2. **fact_pattern_layer** — Factual matrix and evidence
3. **risk_layer** — Risk assessment and mitigation
4. **governance_layer** — Decision ownership and authority
5. **documentation_layer** — Drafting and record-keeping
6. **negotiation_layer** — Strategy and counterparty dynamics
7. **enforcement_layer** — Execution and remedies

**Description**: Each legal matter represented as tensor across doctrine, facts, risk, governance, documentation, negotiation, and enforcement.

## Routing (Matter-Type Based)
| Matter Type | Focus Clusters | Priority Layers |
|-------------|----------------|-----------------|
| transactional | Corporate & Commercial, M&A, Banking & Finance, VC & Startups, JV & Alliances | doctrine, documentation, risk |
| contentious | Disputes & Litigation, International Arbitration, Mediation & ADR, White-Collar & Investigations | fact_pattern, risk, enforcement |
| regulatory, investigations | Regulatory & Compliance, Competition & Antitrust, Data Protection & Privacy, Environmental & ESG, Public & Administrative Law | doctrine, risk, governance |

**Notes**: Routing conceptual; infer from user description. Ambiguous → broad structural analysis first.

## Policies (4)
1. **Loading Policy**: Default to virtual expansion; instantiate micro-layers only for offline analysis/specialised tooling; keep kernel/tensor/clusters/dimensions as primary decision surface
2. **Problem Solving Policy**: Always ground in legal structure (FIRAC/IRAC). Never jurisdiction-specific advice without disclaimer. Structural reasoning assistant, not licensed professional replacement.
3. **Quality Policy**: Internal consistency, explicit assumptions, clear separation law/facts/strategy. No invented statutes/cases/regulations. State uncertainty explicitly.
4. **Governance Policy**: High-risk topics (criminal, sanctions, health, safety, human rights, regulatory enforcement) must include disclaimer requiring local qualified counsel. No law firm branding or lawyer simulation.

---

**Conclusion**: SOURCE — Complete canonical legal kernel with 25 axes, 24 dimensions with enumerated values, 7-layer tensor, matter-type routing, and 4 governance policies. Clean MECE foundation for AMOS_Legal_SUPER_Engine_vInfinity.

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[KERNEL_MOC]]
