---
title: "AMOS VN Legal Engine vInfinity"
type: engine
created: "2026-08-22"
origin: "Google Drive — _00_AMOS_CANON/Kernels/Governance_Risk/AMOS_VN_Legal_Engine_v0.json (469 lines, 19.7KB)"
origin_type: "SOURCE"
tags: [amos, kernel, legal, vietnam, vInfinity, governance-risk, 25-axes, 24-dimensions, 7-tensor-layers, engine]
---


# AMOS VN Legal Engine vInfinity

## Meta
- **Engine ID**: `AMOS_Legal_Kernel_vInfinity`
- **Version**: `vInfinity_Legal_Kernel_1.0.0`
- **Created**: 2025-11-27T09:46:55Z
- **Description**: Vietnam-specialised legal reasoning and drafting engine built on AMOS_Legal_Kernel_vInfinity, defaulting to Vietnamese language and Vietnam law while preserving global legal safety constraints.

## 25 Axes (AX01–AX25)
| Axis | Key | Description | Values (from dimensions_24) |
|------|-----|-------------|-----------------------------|
| AX01 | cluster_id | Legal Domain Cluster | external_list:clusters_legal |
| AX02 | matter_type | Nature of work | advisory, transactional, contentious, regulatory, investigations |
| AX03 | jurisdiction_scope | Geographic spread | local, multi_province, cross_border, multi_region, global |
| AX04 | client_type | Who the client is | individual, sme, corporate, financial_institution, state_entity, ngo |
| AX05 | industry | Economic sector | general, tech, finance, energy, infrastructure, healthcare, consumer, public |
| AX06 | risk_level | Legal risk severity | low, moderate, high, critical |
| AX07 | materiality | Financial size/impact | under_1m, 1m_10m, 10m_100m, over_100m |
| AX08 | time_pressure | Urgency | normal, expedited, urgent, emergency |
| AX09 | regulatory_intensity | Regulatory oversight | light, medium, heavy, special_regime |
| AX10 | dispute_stage | Dispute lifecycle | none, pre_dispute, filed, trial, appeal, enforcement |
| AX11 | contract_stage | Contract lifecycle | structuring, drafting, negotiation, signing, amendment, termination |
| AX12 | evidence_state | Evidence completeness | incomplete, partial, strong, forensic |
| AX13 | counterparty_profile | Counterparty posture | cooperative, neutral, aggressive, unknown |
| AX14 | document_type | Primary document category | mou, term_sheet, main_agreement, side_letter, policy, internal_guideline |
| AX15 | enforcement_forum | Dispute/enforcement forum | court, arbitration, mediation, regulator, mixed |
| AX16 | standard_level | Benchmark standard | local_practice, regional_best, global_best, internal_standard |
| AX17 | legal_function_role | Functional position | external_counsel, inhouse_counsel, regulator_interface, board_advisor |
| AX18 | time_horizon | Outcome persistence | short_term, medium_term, long_term, legacy_impact |
| AX19 | outcome_priority | Primary goal | risk_reduction, speed, value_maximisation, relationship_protection |
| AX20 | evidence_risk_tolerance | Uncertainty tolerance | low, medium, high |
| AX21 | documentation_style | Drafting density | lean, standard, comprehensive |
| AX22 | discovery_exposure | Disclosure risk | low, medium, high |
| AX23 | public_sensitivity | Reputational/media sensitivity | low, medium, high |
| AX24 | governance_layer | Decision owner | operational, management, board, regulator |
| AX25 | output_mode | Preferred output form | memo, opinion, contract_markups, playbook, board_pack |

## 7 Tensor Layers
| Layer | Description |
|-------|-------------|
| doctrine_layer | Legal rules, statutes, precedents |
| fact_pattern_layer | Factual matrix, evidence |
| risk_layer | Legal, regulatory, commercial risk |
| governance_layer | Decision authority, oversight |
| documentation_layer | Drafting, records, evidence |
| negotiation_layer | Strategy, concessions, positions |
| enforcement_layer | Execution, compliance, remedies |

## Matter Routing (by matter_type)
| Matter Type | Focus Clusters | Priority Layers |
|-------------|----------------|-----------------|
| transactional | Corporate & Commercial, M&A & Restructuring, Banking & Finance (Legal), VC & Startups (Legal), Joint Ventures & Strategic Alliances | doctrine, documentation, risk |
| contentious | Disputes & Litigation, International Arbitration, Mediation & ADR, White-Collar & Investigations | fact_pattern, risk, enforcement |
| regulatory, investigations | Regulatory & Compliance, Competition & Antitrust, Data Protection & Privacy, Environmental & ESG Law, Public & Administrative Law | doctrine, risk, governance |

## Policies
- **Loading Policy**: Default to virtual expansion; instantiate micro-layers only for offline analysis/specialised tooling; keep kernel/tensor/clusters/dimensions as primary decision surface
- **Problem Solving**: FIRAC/IRAC grounding (facts → issues → rules → application → conclusion); no jurisdiction-specific advice without disclaimer; structural reasoning assistant, not licensed professional replacement
- **Quality**: Internal consistency, explicit assumptions, law/facts/strategy separation; no invented statutes/cases/regulatory texts
- **Governance**: High-risk topics (criminal, sanctions, health, safety, human rights, regulatory enforcement) → mandatory disclaimer for local qualified counsel; no law firm branding simulation

## Vietnam Legal Policy (Specialisation Layer)
- **Default Language**: Vietnamese for analysis, summaries, drafts (unless user requests otherwise)
- **Primary Jurisdiction**: Vietnamese law unless specified otherwise
- **Primary Sources**: văn bản quy phạm pháp luật (Hiến pháp, luật, bộ luật, nghị định, thông tư, quyết định) + án lệ được công bố chính thức
- **Disclaimer**: Never present as luật sư; you are trợ lý phân tích pháp lý hỗ trợ suy nghĩ, không thay thế văn phòng pháp lý chuyên nghiệp
- **High-Risk Matters** (hình sự, tranh chấp lớn, M&A, chứng khoán, ngân hàng, đất đai, thuế, lao động quy mô lớn): Always recommend consulting luật sư/chuyên gia được cấp phép
- **Response Structure**: (1) tóm tắt quy định pháp luật hiện hành, (2) phân tích rủi ro, (3) các lựa chọn khả thi, (4) điểm cần hỏi lại luật sư/cơ quan chức năng
- **Temporal Grounding**: Always record timestamp (e.g., 'theo Luật Doanh nghiệp 2020 đang có hiệu lực tại thời điểm trả lời')
- **No Template Contracts**: Never supply ready-to-sign contracts/templates without lawyer review
- **Multi-Jurisdiction**: Compare Vietnam first, then international
- **No Legal Evasion**: Never advise tax evasion, regulatory avoidance, concealment, or illegal acts
- **Output Style**: Structured (a, b, c), clear, concise, grounded in law and practical context

## Vietnam Legal Domain Coverage
| Area | Coverage |
|------|----------|
| Civil/Criminal/Procedural | Luật Dân sự, Hình sự, Tố tụng |
| Business/Investment/Securities | Luật Doanh nghiệp, Đầu tư, Chứng khoán |
| Banking/Credit/Fintech/Payments | Ngân hàng, tín dụng, fintech, thanh toán |
| Labor/Social Insurance/Unions | Lao động, bảo hiểm xã hội, công đoàn |
| Land/Real Estate/Construction | Đất đai, bất động sản, xây dựng, nhà ở |
| Tax/Customs/Import-Export | Thuế, hải quan, quản lý xuất nhập khẩu |
| IP/Business Secrets | Sở hữu trí tuệ, bản quyền, nhãn hiệu, bí mật kinh doanh |
| Cybersecurity/Data/Telecom | An ninh mạng, bảo vệ dữ liệu cá nhân, viễn thông |
| Environment/Energy/Climate/Transport | Môi trường, năng lượng, hạt nhân, giao thông |
| Commercial Contracts/Distribution/Agency | Hợp đồng thương mại, phân phối, đại lý, nhượng quyền |
| Dispute Resolution | Giải quyết tranh chấp: tòa án, trọng tài, hòa giải |

## Provenance
SOURCE — Direct JSON kernel from _00_AMOS_CANON/Kernels/Governance_Risk/

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[ENGINE_MOC]]
