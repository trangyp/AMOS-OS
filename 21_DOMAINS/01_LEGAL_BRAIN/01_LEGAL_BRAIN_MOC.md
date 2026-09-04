---
title: 01_LEGAL_BRAIN MOC
type: map_of_content
status: ACTIVE
conclusion_class: DERIVED
origin_architect: Trang Phan
governed_by: [[21_DOMAINS/08_LEGAL/DOMAINS_LEGAL_CONTRACT.md|DOMAINS_LEGAL_CONTRACT]]
---

# 01_LEGAL_BRAIN Map of Content

## Overview
Specialized cognitive legal synthesis engine integrating Vietnamese and international statutory jurisprudence, deontic logic, and contract semantics.

## Core Documents
- [[21_DOMAINS/01_LEGAL_BRAIN/AMOS_LEGAL_ENGINE_KERNEL_CANON.md|AMOS Legal Engine Kernel Canon]]
- [[21_DOMAINS/08_LEGAL/LEGAL_DOMAINS_DOMAIN_SPEC.md|Legal Domains Specification]]
- [[21_DOMAINS/19_C09_ORG_LAW_POLICY/C09_ORG_LAW_POLICY_DOMAINS_DOMAIN_SPEC.md|C09 Organizational Law & Policy Spec]]

## Governance & Interfaces
- Governed under the [[AGENTS.md|AMOS Agent Contract]] lineage boundary (v3.0 -> v4.4).
- Cross-references: [[21_DOMAINS/21_DOMAINS_MOC.md|21_DOMAINS MOC]], [[00_ROOT/00_ROOT_MOC.md|Root MOC]].

---

## Domain Overview
The **01_LEGAL_BRAIN** domain is a specialized cognitive legal synthesis engine integrating Vietnamese and international statutory jurisprudence, deontic logic, and contract semantics. Within the AMOS brain architecture, this domain provides the legal reasoning layer, enabling the system to parse, interpret, and synthesize legal arguments across multiple jurisdictions with particular depth in Vietnamese statutory law. The Legal Engine Kernel Canon is the primary artifact, encoding the core reasoning kernel that maps legal propositions through deontic logic operators (obligation, permission, prohibition) and contract semantic frameworks. This domain interfaces with the legal domains specification and the organizational law and policy specification to ensure that legal reasoning remains grounded in authoritative statutory sources rather than speculative legal theory. The domain is essential for any AMOS capability that must reason about legal compliance, contract validity, regulatory obligations, or policy implications. It enforces strict separation between legal synthesis (which produces reasoned legal arguments) and legal authority (which resides with qualified legal practitioners and judicial bodies), recognizing that AI-generated legal analysis is advisory and does not constitute legal advice.

## MECE Classification
This domain belongs to **Domain E: Governance & Security** in the AMOS MECE taxonomy. It shares this partition with security engineering, organizational law, and policy enforcement. The legal brain is distinct from security engineering (which focuses on technical enforcement mechanisms) in that it focuses on normative legal reasoning, statutory interpretation, and deontic logic. It is separated from Domain C (Social & Economic) because it models legal norm structures rather than descriptive social behavior. Its MECE boundary with Domain A (Cognitive & Reasoning) is maintained by limiting this domain to legal-specific reasoning, while general cognitive reasoning is handled in the cognitive organism plane. The domain is governed by the [[21_DOMAINS/08_LEGAL/DOMAINS_LEGAL_CONTRACT.md|DOMAINS_LEGAL_CONTRACT]].

## Key Artifacts
- [[21_DOMAINS/01_LEGAL_BRAIN/AMOS_LEGAL_ENGINE_KERNEL_CANON.md|AMOS Legal Engine Kernel Canon]] — core legal reasoning kernel encoding deontic logic and contract semantics
- [[21_DOMAINS/08_LEGAL/LEGAL_DOMAINS_DOMAIN_SPEC.md|Legal Domains Specification]] — formal specification for the legal domain
- [[21_DOMAINS/19_C09_ORG_LAW_POLICY/C09_ORG_LAW_POLICY_DOMAINS_DOMAIN_SPEC.md|C09 Organizational Law & Policy Spec]] — organizational law and policy domain specification

## Cross-Domain Relationships
- **Legal Contract**: [[21_DOMAINS/08_LEGAL/DOMAINS_LEGAL_CONTRACT.md|DOMAINS_LEGAL_CONTRACT]] — governing contract for legal domain operations
- **Organizational Law & Policy**: [[21_DOMAINS/19_C09_ORG_LAW_POLICY/C09_ORG_LAW_POLICY_DOMAINS_DOMAIN_SPEC.md|C09 Organizational Law & Policy Spec]] — organizational policy interface
- **Security Domain**: [[21_DOMAINS/09_SECURITY/09_SECURITY_MOC.md|09_SECURITY MOC]] — classified systems legal compliance interface
- **Human Systems Engineering**: [[21_DOMAINS/03_HUMAN_SYSTEMS_ENGINE/03_HUMAN_SYSTEMS_ENGINE_MOC.md|03_HUMAN_SYSTEMS_ENGINE MOC]] — employment law and regulatory interface
- **Root Navigation**: [[00_ROOT/00_ROOT_MOC.md|Root MOC]] — top-level vault navigation
- **Domains Plane**: [[21_DOMAINS/21_DOMAINS_MOC.md|21_DOMAINS MOC]] — parent plane index

## Epistemic Boundary
- **Epistemic class**: DERIVED — this MOC is a derived structural index, not a primary source claim.
- **Provenance**: authoritative_AMOS_OS_structure — generated from the canonical vault directory layout.
- **Scope**: active__AMOS_OS — applies to the currently active AMOS OS vault instance.
- **Limitation**: AI-generated legal synthesis is advisory analysis, not authoritative legal advice. `LEGAL_SYNTHESIS != LEGAL_AUTHORITY`, `JURISPRUDENCE_MODEL != JUDICIAL_RULING`. Qualified legal practitioners retain authoritative legal judgment.
- **Claim boundary**: The legal engine kernel canon specification is structurally present; end-to-end executable legal reasoning closure across all jurisdictions is `UNKNOWN/GAP` without validated statutory databases and judicial precedent corpora.

---

**Parent:** [[21_DOMAINS/00_INDEX/DOMAINS_MOC|DOMAINS_MOC]]
