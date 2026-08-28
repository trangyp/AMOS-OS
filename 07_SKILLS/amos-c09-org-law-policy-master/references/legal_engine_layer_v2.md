---
title: legal engine layer v2
type: reference
source: 07_SKILLS/amos-c09-org-law-policy-master/references
tags: [reference, amos-c09-org-law-policy-master, canon/skill]
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# AMOS Legal Engine Layer

> Source: `_00_Cosmo brain/engine/A/amos-legal-engine-layer.md`
> Epistemic class: SOURCE_DERIVED

---
title: "amos-legal-engine-layer"
created: "2026-08-22"
origin_architect: "Trang Phan"
type: "bridge"
tags: [canon-group/human-system, canon/framework, rscf/claim, rscf/provenance, rscf/state/observation, topic/amos-legal-engine-layer, engine]
status: "index"
provenance: "SOURCE_CLAIM"
confidence: "VERIFIED"
---

# amos-legal-engine-layer

The Cosmo brain source file at `engine/A/amos-legal-engine-layer.md` is a bridge note pointing to the Legal Engine. Substantive content is found in `engine/L/Legal_Engine_Model.md` and `engine/A/AMOS_Global_Legal_Engine_v0_Unipower4.md`. The following is synthesized from those sources.

## Engine Identity

- **Engine Name:** AMOS Legal Engine Kernel
- **Version:** vInfinity_Legal_Kernel_1.0.0
- **Source:** `AMOS_Legal_Kernel_v0.json`
- **Description:** The Legal Engine Kernel provides a clean, MECE (Mutually Exclusive, Collectively Exhaustive) structure for legal reasoning, without replacing qualified human counsel.

## Architecture: 7-Layer Tensor

The kernel models legal matters as a tensor across 7 layers:

1. **Doctrine** -- Legal principles, statutes, regulations, case-law foundations
2. **Facts** -- Fact pattern extraction, evidence state assessment, witness/instrument analysis
3. **Risk** -- Risk band classification (low, moderate, high, prohibited), likelihood and consequence tagging
4. **Governance** -- Corporate governance structures, compliance frameworks, regulatory obligations
5. **Docs** -- Contract drafting, policy documents, dispute documentation, corporate filings
6. **Negotiation** -- Counterparty profiling (cooperative to aggressive), settlement frameworks, mediation strategies
7. **Enforcement** -- Regulatory enforcement mechanisms, litigation pathways, arbitration, judgment execution

## The 24 Dimensions

Key variables that shape the legal strategy:
- **D01:** Matter Type (transactional, contentious, regulatory)
- **D02:** Jurisdiction Scope (local to global)
- **D03:** Party Structure (bilateral, multi-party, class)
- **D04:** Regulatory Intensity
- **D05:** Cross-border Complexity
- **D06:** Financial Materiality
- **D07:** Time Pressure
- **D08:** Reputation Exposure
- **D09:** Precedent Reliance
- **D10:** Documentation Completeness
- **D11:** Evidence State (incomplete to forensic)
- **D12:** Counterparty Profile (cooperative to aggressive)
- **D13:** Counsel Availability
- **D14:** Forum Selection
- **D15:** ADR Suitability
- **D16:** Compliance Burden
- **D17:** Disclosure Obligations
- **D18:** Privilege Coverage
- **D19:** Evidence Risk Tolerance
- **D20:** Settlement Window
- **D21:** Enforcement Feasibility
- **D22:** Jurisdictional Conflict Risk
- **D23:** Public Interest Dimension
- **D24:** Long-tail Liability

## Routing Logic

The engine routes based on matter type to focus on specific clusters:
- **Contentious matters** focus on Disputes and Litigation, International Arbitration, prioritizing the fact pattern and enforcement layers
- **Transactional matters** focus on Contracts, Corporate, and documentation layers
- **Regulatory matters** focus on Compliance, Governance, and Doctrine layers

## Safety and Governance

- **No Jurisdiction Advice:** The engine does not simulate a law firm or claim to be a lawyer. It always requires local counsel for high-risk topics.
- **No Hallucination:** The engine does not invent statutes, case law, or regulatory texts. If information is missing, it explicitly asks or marks as unknown.
- **Conservative Default:** Recommendations are structured as: what is clearly allowed, what is ambiguous, what is high risk or likely unlawful.
- **Hard Blocks:** The engine refuses assistance with crime, fraud, corruption, money laundering, tax/sanctions evasion, illegal contracts, sham agreements, or personalised legal advice as a substitute for licensed counsel.

## Output Structure

The engine produces structured output following: LEGAL_INPUT_RESOLVED, FACT_PATTERN, ISSUE_LIST, APPLICABLE_FRAMEWORKS, ANALYSIS, OPTIONS, RISK_MATRIX, RECOMMENDATIONS, COUNSEL_CHECKPOINTS, DISCLAIMER. Each issue is tagged with risk_band, likelihood, and consequence.

## Integration

The Legal Engine integrates with the Governance Risk Policy Kernel for governance and compliance analysis, the Global Legal Engine for multi-jurisdiction matters, the VN Legal Kernel for Vietnam-specific analysis, and the Documentation Engine for contract and policy drafting.

---
**MOC:** [[references_MOC]]

## Related

- [[07_SKILLS_MOC]]
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[references_MOC]] · [[07_SKILLS_MOC]]

**MOC:** [[references_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-c09-org-law-policy-master-legal-engine-layer-v2
node_type: reference
path: 07_SKILLS/amos-c09-org-law-policy-master/references/legal_engine_layer_v2.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[references_MOC]]
