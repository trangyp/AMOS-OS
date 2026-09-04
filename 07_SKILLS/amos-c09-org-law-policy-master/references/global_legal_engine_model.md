---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Global Legal Engine Model
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

# AMOS Global Legal Engine Model

> Source: `_00_Cosmo brain/engine/A/AMOS_Global_Legal_Engine_Model.md`
> Epistemic class: SOURCE_DERIVED

______________________________________________________________________

## type: doc title: Bridge to AMOS_Global_Legal_Engine_Model created: 2026-08-22 tags: [canon-group/tech-ai, canon/model, rscf/claim, rscf/state/derived, topic/amos-global-legal-engine-model, engine]

## Bridge: AMOS_Global_Legal_Engine_Model

The Cosmo brain source file at `engine/A/AMOS_Global_Legal_Engine_Model.md` is itself a thin bridge note. The substantive model content is found in the related engine files `AMOS_Global_Legal_Engine_v0_Unipower4.md` (engine layer) and `engine/L/Legal_Engine_Model.md` (kernel model). The following content is synthesized from those sources.

## Model Overview

The Global Legal Engine Model represents the conceptual architecture for deterministic legal reasoning across multiple jurisdictions. It is designed as a kernel for GPT-based agents, providing structured analysis without replacing qualified human counsel.

## Engine Architecture

The engine models legal matters as a tensor across 7 layers:

1. **Doctrine** -- Legal principles, statutes, regulations, case-law
1. **Facts** -- Fact pattern extraction, evidence state assessment
1. **Risk** -- Risk band classification (low, moderate, high, prohibited)
1. **Governance** -- Corporate governance, compliance frameworks
1. **Docs** -- Contract drafting, policy documents, dispute documentation
1. **Negotiation** -- Counterparty profiling, settlement frameworks
1. **Enforcement** -- Regulatory enforcement, litigation, arbitration

## The 24 Dimensions

Key variables that shape the legal strategy include:

- **D01:** Matter Type (transactional, contentious, regulatory)
- **D02:** Jurisdiction Scope (local to global)
- **D06:** Financial Materiality
- **D11:** Evidence State (incomplete to forensic)
- **D12:** Counterparty Profile (cooperative to aggressive)
- **D19:** Evidence Risk Tolerance

## Reasoning Axes

The model operates across five orthogonal axes:

- **A_domain:** substantive_law, procedure, governance, compliance, dispute
- **B_perspective:** individual, company, regulator, counterparty, third_party
- **C_time_horizon:** past_events, current_position, forward_risk, long_term_structure
- **D_jurisdiction:** specified_jurisdiction, comparable_jurisdictions, generic_principles_only
- **E_risk_band:** low, moderate, high, prohibited

## Routing Logic

The engine routes based on matter type to focus on specific clusters. For example, contentious matters focus on Disputes and Litigation, International Arbitration, and prioritize the fact pattern and enforcement layers. Transactional matters focus on Contracts, Corporate, and documentation layers.

## Safety and Governance

- **No Jurisdiction Advice:** The model does not simulate a law firm or claim to be a lawyer. It always requires local counsel for high-risk topics.
- **No Hallucination:** The model does not invent statutes, case law, or regulatory texts.
- **Conservative Default:** Recommendations are structured as what is clearly allowed, what is ambiguous, and what is high risk or likely unlawful.

## Jurisdiction Coverage

The model covers global public international law, United States (federal + state), European Union, United Kingdom, Vietnam, Singapore, and OECD-model generalisation. For unspecified jurisdictions, the model keeps to generic principles and flags uncertainty.

## Output Structure

The model produces structured output following the template: LEGAL_INPUT_RESOLVED, FACT_PATTERN, ISSUE_LIST, APPLICABLE_FRAMEWORKS, ANALYSIS, OPTIONS, RISK_MATRIX, RECOMMENDATIONS, COUNSEL_CHECKPOINTS, DISCLAIMER. Each issue is tagged with risk_band, likelihood, and consequence.

## Integration Points

The Global Legal Engine Model integrates with the Governance_Risk Policy Kernel for governance and compliance analysis, the Org Governance Engine for corporate governance, and the VN Legal Kernel for Vietnam-specific legal matters. It also feeds into the Documentation Engine for contract and policy drafting.

______________________________________________________________________

**MOC:** references_MOC

## Related

- [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · references_MOC · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-c09-org-law-policy-master-global-legal-engine-model
node_type: reference
path: 07_SKILLS/amos-c09-org-law-policy-master/references/global_legal_engine_model.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
