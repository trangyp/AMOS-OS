---
title: 03_HUMAN_SYSTEMS_ENGINE MOC
type: map_of_content
status: ACTIVE
conclusion_class: DERIVED
origin_architect: Trang Phan
governed_by: [[21_DOMAINS/33_ORGANIZATIONAL_BEHAVIOR/DOMAINS_ORGANIZATIONAL_BEHAVIOR_CONTRACT.md|DOMAINS_ORGANIZATIONAL_BEHAVIOR_CONTRACT]]
rscf-state: source-claim
---

# 03_HUMAN_SYSTEMS_ENGINE Map of Content

## Overview
Human systems engineering, organizational socio-dynamics, institutional culture, and workplace psychology in Vietnamese enterprise contexts.

## Core Documents
- [[21_DOMAINS/03_HUMAN_SYSTEMS_ENGINE/HSE_VIETNAMESE_ORGANIZATIONAL_CANON.md|HSE Vietnamese Organizational Canon]]
- [[21_DOMAINS/33_ORGANIZATIONAL_BEHAVIOR/ORGANIZATIONAL_BEHAVIOR_DOMAINS_DOMAIN_SPEC.md|Organizational Behavior Spec]]
- [[21_DOMAINS/40_HSE_SAFETY/HSE_SAFETY_DOMAINS_DOMAIN_SPEC.md|HSE Safety Spec]]

## Navigation
- Return to: [[21_DOMAINS/21_DOMAINS_MOC.md|21_DOMAINS MOC]], [[00_ROOT/00_ROOT_MOC.md|Root MOC]].

---

## Domain Overview
The **03_HUMAN_SYSTEMS_ENGINE** domain addresses human systems engineering, organizational socio-dynamics, institutional culture, and workplace psychology with a particular focus on Vietnamese enterprise contexts. Within the AMOS brain architecture, this domain provides the socio-organizational modeling layer that enables the system to reason about human collective behavior, organizational design, cultural norms, and safety-critical human factors. It synthesizes insights from organizational behavior science, human factors engineering, and occupational health and safety (HSE) into a unified representational framework. The domain is essential for any AMOS capability that must model how humans behave within structured institutions, predict organizational responses to policy changes, or design interventions that account for cultural and psychological realities. The Vietnamese Organizational Canon is the primary artifact, encoding culturally-specific organizational patterns, hierarchical dynamics, and communication norms prevalent in Vietnamese enterprises. This domain interfaces with the organizational behavior contract and the HSE safety specification to ensure that human-systems reasoning remains grounded in validated behavioral science rather than speculative generalization.

## MECE Classification
This domain belongs to **Domain C: Social & Economic** in the AMOS MECE taxonomy. It shares this partition with economics, finance, legal systems, and organizational law. Human systems engineering is distinct from pure economics (which models resource allocation) in that it focuses on the human behavioral and cultural substrate within which economic activity occurs. It is separated from Domain E (Governance & Security) because it models descriptive organizational behavior rather than prescribing governance authority. Its MECE boundary with Domain A (Cognitive & Reasoning) is maintained by limiting this domain to collective and institutional phenomena, while individual cognition is handled in the cognitive organism plane.

## Key Artifacts
- [[21_DOMAINS/03_HUMAN_SYSTEMS_ENGINE/HSE_VIETNAMESE_ORGANIZATIONAL_CANON.md|HSE Vietnamese Organizational Canon]] — culturally-grounded organizational behavior canon for Vietnamese enterprises
- [[21_DOMAINS/33_ORGANIZATIONAL_BEHAVIOR/ORGANIZATIONAL_BEHAVIOR_DOMAINS_DOMAIN_SPEC.md|Organizational Behavior Spec]] — formal domain specification for organizational behavior modeling
- [[21_DOMAINS/40_HSE_SAFETY/HSE_SAFETY_DOMAINS_DOMAIN_SPEC.md|HSE Safety Spec]] — occupational health, safety, and environment specification

## Cross-Domain Relationships
- **Organizational Behavior**: [[21_DOMAINS/33_ORGANIZATIONAL_BEHAVIOR/DOMAINS_ORGANIZATIONAL_BEHAVIOR_CONTRACT.md|DOMAINS_ORGANIZATIONAL_BEHAVIOR_CONTRACT]] — governing contract for organizational modeling
- **HSE Safety**: [[21_DOMAINS/40_HSE_SAFETY/HSE_SAFETY_DOMAINS_DOMAIN_SPEC.md|HSE Safety Spec]] — safety-critical human factors interface
- **Organizational Law & Policy**: [[21_DOMAINS/19_C09_ORG_LAW_POLICY/C09_ORG_LAW_POLICY_DOMAINS_DOMAIN_SPEC.md|C09 Organizational Law & Policy Spec]] — legal and policy constraints on organizational design
- **Root Navigation**: [[00_ROOT/00_ROOT_MOC.md|Root MOC]] — top-level vault navigation
- **Domains Plane**: [[21_DOMAINS/21_DOMAINS_MOC.md|21_DOMAINS MOC]] — parent plane index

## Subdomain Structure
- **Organizational Culture Modeling**: Encoding and analyzing cultural norms, hierarchical dynamics, and communication patterns within Vietnamese enterprises.
- **Workplace Psychology**: Individual and group psychological factors affecting productivity, satisfaction, and organizational commitment.
- **Institutional Design**: Structural design of organizational units, reporting hierarchies, and decision-making processes.
- **HSE Safety Integration**: Human factors in occupational health, safety, and environmental management, bridging organizational behavior with safety engineering.

## Reasoning Patterns
The human systems engineering domain employs several distinct reasoning patterns:
- **Cultural-contextual reasoning**: Interpreting organizational behavior through culturally-grounded frameworks rather than universal assumptions.
- **Socio-dynamic modeling**: Tracking how individual behaviors aggregate into collective organizational dynamics over time.
- **Institutional constraint analysis**: Identifying how formal structures, policies, and informal norms shape organizational outcomes.
- **Safety-human factors integration**: Reasoning about how human psychological and cultural factors influence safety-critical system performance.

These patterns interface with the organizational behavior contract to ensure that human-systems reasoning remains within validated behavioral science boundaries.

## Epistemic Boundary
- **Epistemic class**: DERIVED — this MOC is a derived structural index, not a primary source claim.
- **Provenance**: authoritative_AMOS_OS_structure — generated from the canonical vault directory layout.
- **Scope**: active__AMOS_OS — applies to the currently active AMOS OS vault instance.
- **Limitation**: Organizational behavior models are culturally situated; generalization beyond Vietnamese enterprise contexts requires separate validation. `CULTURAL_MODEL != UNIVERSAL_LAW`.
- **Claim boundary**: The Vietnamese Organizational Canon encodes observed patterns, not causal laws. Predictive accuracy in novel organizational contexts is `UNKNOWN/GAP` without empirical validation.
- **Authority boundary**: Organizational behavior analyses are advisory models, not management directives. `ORG_ANALYSIS != MANAGEMENT_DECISION`. Consequential organizational changes require human authority.

---

**Parent:** [[21_DOMAINS/00_INDEX/DOMAINS_MOC|DOMAINS_MOC]]
