---
title: SKILL — Amos C09 Org Law Policy Master
type: skill
source: 07_SKILLS/amos-c09-org-law-policy-master
name: amos-c09-org-law-policy-master
description: AMOS C09 Org, Law & Policy — governance, authority, compliance, regulatory
  frameworks, constitutional governance, legal reasoning, policy analysis. Use for
  governance design, legal analysis, or pol...
parent_skill: none
domain: c09
origin_architect: Trang Phan
epistemic_class: SOURCE_CANON
tags:
- type/skill
- canon/skill
- domain/org-law-policy
- canon-group/human-system
- topic/governance
- capability/ast
- rscf/epistemic
- sota/progressive-disclosure
- sota/anti-patterns
- amos_os
- amos-c09-org-law-policy-master
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
---



# AMOS C09 — Organization, Law & Policy Master Knowledge

## Identity

Origin architect and steward: **Trang Phan**.

This is a **parent skill** that consolidates 29 sub-skills into a single domain master.
Following the skill-organizer best practice: fewer, richer skills beat many overlapping ones.
A parent skill with clearly labeled sections is better than 29 separate shallow skills.

**Epistemic class**: SOURCE_CLAIM (vault-sourced from `11_KNOWLEDGE/AMOS_C09_ORG_LAW_POLICY_MASTER_KNOWLEDGE.md` (content_hash: bead46b07fc02558)).

## When to Use

AMOS C09 Org, Law & Policy — governance, authority, compliance, regulatory frameworks, constitutional governance, legal reasoning, policy analysis. Use for governance design, legal analysis, or pol...

- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **c09_org_law.enforce_governance**: Enforce AMOS C09 Org, Law & Policy governance: separation of powers, contract hierarchy, ownership accountability, and sanctions.
- **c09_org_law.validate_governance**: Validate AMOS C09 Org, Law & Policy outputs against constitutional hierarchy, authority separation, and RSCF governance constraints.
- **c09_org_law.analyze_economy**: Analyze AMOS C09 Org, Law & Policy economy: agent ownership chains, contract tiers, incentive structures, and audit ledger.
- **c09_org_law.trace_governance_provenance**: Trace AMOS C09 Org, Law & Policy governance decisions to contracts, legislative state, audit records, and source evidence.
- **c09_org_law.assess_economy_claim**: Assess AMOS C09 Org, Law & Policy economic claims for source status, empirical support, scope, assumptions, and overreach.
- **c09_org_law.manage_governance_lifecycle**: Manage AMOS C09 Org, Law & Policy governance lifecycle: propose, legislate, execute, adjudicate, audit, and finalize.
- **c09_org_law.detect_governance_drift**: Detect governance drift: authority creep, contract violation, sanction evasion, and audit gap growth.
- **c09_org_law.escalate_governance_gaps**: Escalate AMOS C09 Org, Law & Policy governance gaps: flag constitutional violations, require adjudication, trigger legislative change.
- **c09_org_law.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **c09_org_law.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **c09_org_law.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Consolidated Sub-Skills (29)

This parent skill consolidates the following sub-skills. Each is a section within this domain:

*...and 9 more sub-skills.*

## Vault-Sourced Domain Knowledge

> **Source**: `11_KNOWLEDGE/AMOS_C09_ORG_LAW_POLICY_MASTER_KNOWLEDGE.md` (content_hash: bead46b07fc02558) (vault canon, SOURCE_CLAIM)

### Major Knowledge Modules

- **M1: Organization as Governed System** — organizational structure, governance frameworks
- **M2: Decision Rights Framework** — authority allocation, decision matrices [MODEL]
- **M3: Structural Forms and Group Models** — organizational forms, group dynamics [MODEL]
- **M4: Operating Model** — processes, workflows, operational governance
- **M1: Control Framework** — internal controls, oversight mechanisms
- **M2: Risk Taxonomy for Organizations** — risk classification, assessment [MODEL]
- **M3: Compliance Architecture** — compliance frameworks, monitoring [CONDITIONAL]
- **M1: Legal Primitives** — legal concepts, rule types, legal reasoning [MODEL]
- **M2: Rule System Analysis** — statutory analysis, regulatory interpretation
- **M3: Analysis Pipeline** — legal analysis workflow [MODEL]
- **M1: Jurisdiction Identification** — jurisdictional scope, conflict of laws
- **M2: Multi-Jurisdiction Operations** — cross-border compliance, regulatory arbitrage
- **M1: Regulatory Intensity Classes** — regulatory burden classification [MODEL]
- **M2: Policy Gap Analysis Method** — gap identification, policy recommendations
- **M3: Compliance Reasoning Example Form** — compliance analysis templates
- **M1: Vietnam-Focused Engine Pattern** — Vietnamese legal/governance model [MODEL]
- **M2: Chinese Legal Ecosystem Model** — conceptual only [MODEL]
- **M3: Generalizable Lesson** — cross-jurisdictional patterns [MODEL]
- **M1: Succession Is Structural** — organizational succession [MODEL]

### Epistemic Classification

- **Conclusion class**: MIXED (establish
- [[AGENT_TEMPLATE]]

---
**MOC:** [[amos-c09-org-law-policy-master_MOC]]

## Examples

- **Scenario**: When managing lifecycle operations across classify, validate, trace, assess, and detect
  - **Input**: A query matching this skill's domain (c09)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When detecting drift in evidence chains, provenance freshness, or confidence calibration
  - **Input**: A query matching this skill's domain (c09)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When validating outputs against domain constraints and epistemic class
  - **Input**: A query matching this skill's domain (c09)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the c09 domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `none` — routes to this skill when c09 specialization is needed
- **Peers**: Other skills in the `c09` domain may be composed in sequence
- **Orchestrator**: The parent skill or `AMOS_HOME` orchestrates routing
- **Workflow**: Each skill has a corresponding workflow in `08_WORKFLOWS/`
- **Agent**: Each skill has a corresponding agent in `06_AGENTS/`


## Evaluation

### Success Criteria

- Output includes epistemic class label (SOURCE/DERIVED/AMOS_MODEL/EMPIRICAL)
- Output includes provenance reference to source evidence
- Output includes confidence ceiling (capped at 0.95 for DERIVED, 1.0 for SOURCE_CANON)
- Output includes gap flags for unresolved unknowns
- Output does not exceed declared scope

### Failure Modes

- **Overreach**: Output claims validity beyond its epistemic class
- **Scope creep**: Output addresses questions outside the declared domain
- **Provenance loss**: Output cannot trace back to source evidence
- **Confidence inflation**: Output confidence exceeds the weakest-premise ceiling


## Error Handling

- **On scope violation**: Reject the query and route back to parent skill
- **On missing evidence**: Flag as GAP and reduce confidence ceiling to 0.5
- **On contradiction**: Flag as CRITICAL_GAP and halt until resolved
- **On provenance loss**: Mark output as UNKNOWN and require human review
- **On drift**: Trigger drift alignment via `amos-ai-drift-alignment-governor`


## References

- `references/advanced_governance_report.md` — loaded on demand
- `references/bio_data_ownership_charter.md` — loaded on demand
- `references/bio_data_ownership_legal_tech.md` — loaded on demand
- `references/bod_engine_v0.md` — loaded on demand
- `references/brain_governance_ssot_report.md` — loaded on demand
- `references/change_management_engine.md` — loaded on demand
- `references/chinese_legal_engine.md` — loaded on demand
- `references/core_v47_hardened_governance.md` — loaded on demand
- `references/crisis_management_kernel.md` — loaded on demand
- `references/deterministic_organisation_governance.md` — loaded on demand
- `references/domain_config.md` — loaded on demand
- `references/ethical_reasoning_kernel.md` — loaded on demand
- `references/ethics_as_infrastructure.md` — loaded on demand
- `references/global_legal_engine.md` — loaded on demand
- `references/global_legal_engine_layer.md` — loaded on demand
- `references/global_legal_engine_model.md` — loaded on demand
- `references/gov_engine_sector_packs.md` — loaded on demand
- `references/governance_economy_engine.md` — loaded on demand
- `references/governance_politics_pack_au.md` — loaded on demand
- `references/governance_tensor.md` — loaded on demand
- `references/hse_ceo_engine_layer.md` — loaded on demand
- `references/kernels_governance_risk.md` — loaded on demand
- `references/law_stack_enforcement.md` — loaded on demand
- `references/legal_check_agent.md` — loaded on demand
- `references/legal_engine_layer_v2.md` — loaded on demand
- `references/legal_kernel.md` — loaded on demand
- `references/legal_kernel_org_risk.md` — loaded on demand
- `references/legal_risk_agent.md` — loaded on demand
- `references/legal_super_engine.md` — loaded on demand
- `references/omega_governance_ssot.md` — loaded on demand
- `references/org_engine.md` — loaded on demand
- `references/org_governance_engine.md` — loaded on demand
- `references/org_governance_engine_layer.md` — loaded on demand
- `references/org_governance_engine_v0.md` — loaded on demand
- `references/policy_design_engine.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- `references/trang_ip_protection_plan.md` — loaded on demand
- `references/ubi_law_families.md` — loaded on demand
- `references/uni_power_strategic_governance.md` — loaded on demand
- `references/unified_org_systems_engine.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `references/vn_legal_engine.md` — loaded on demand
- `references/vn_legal_engine_domains.md` — loaded on demand
- `references/vn_legal_engine_v0_domains.md` — loaded on demand
- `references/vn_legal_engine_vinfinity.md` — loaded on demand
- `references/vn_nab_legal_audit_report.md` — loaded on demand
- `references/vn_shareholder_board_report.md` — loaded on demand
- `references/vn_technical_legal_terms.md` — loaded on demand
- `[[amos-c09-org-law-policy-master_MOC]]` — skill Map of Content
- `none` — parent skill
- `[[amos-c09-org-law-policy-master-workflow]]` — corresponding workflow
- `amos-c09-org-law-policy-master-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-c09-org-law-policy-master
node_type: skill
path: 07_SKILLS/amos-c09-org-law-policy-master/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
