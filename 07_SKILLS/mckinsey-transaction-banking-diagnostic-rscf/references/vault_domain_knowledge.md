---
title: Vault Domain Knowledge — Mckinsey Transaction Banking Diagnostic Rscf
type: reference
source: 07_SKILLS/mckinsey-transaction-banking-diagnostic-rscf/references
tags:
- reference
- mckinsey-transaction-banking-diagnostic-rscf
- canon/skill
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# Vault-Sourced Domain Knowledge

> Source: AMOS_OS Obsidian vault (`_00_Cosmo brain/`)
> Epistemic class: SOURCE_CLAIM
> Extracted from skill: `mckinsey-transaction-banking-diagnostic-rscf`

## Vault-Sourced Content

### Source 1: FIN_BANKING_Digital_Transformation_Playbook

> Path: `misc/F/FIN_BANKING_Digital_Transformation_Playbook.md` | Size: 2753 chars | Match score: 10 | content_hash: c02f06ecc05146e7

{
  "id": "FIN_BANKING_Digital_Transformation_Playbook",
  "sector_id": "FIN_BANKING",
  "name": "Banking Digital Transformation Playbook",
  "description": "Structured playbook for digital transformation in banking sector",
  "objective": "Transform banking operations to be fully digital, secure, and customer-centric",
  "phases": [
    {
      "id": "phase_1_assess",
      "name": "Assessment",
      "description": "Assess current digital maturity and gaps",
      "order": 1,
      "required_domains": ["Tech_Engine", "Org_Engine"],
      "required_skills": ["TECH_SYSTEMS.Architecture_Kernel", "TECH_SYSTEMS.Product_Management_Kernel"],
      "required_frameworks": ["fw.systems_architecture.trang_01"],
      "outputs": ["Digital maturity assessment", "Gap analysis"]
    },
    {
      "id": "phase_2_design",
      "name": "Design",
      "description": "Design digital banking architecture and roadmap",
      "order": 2,
      "required_domains": ["Tech_Engine", "Econ_Engine", "Governance_Engine"],
      "required_skills": ["TECH_SYSTEMS.API_Design_Kernel", "TECH_SYSTEMS.Architecture_Kernel"],
      "required_frameworks": ["fw.systems_architecture.trang_01"],
      "outputs": ["Architecture design", "Roadmap"]
    },
    {
      "id": "phase_3_implement",
      "name": "Implementation",
      "description": "Implement digital banking infrastructure",
      "order": 3,
      "required_domains": ["Tech_Engine", "Org_Engine"],
      "required_skills": ["TECH_SYSTEMS.DevOps_Kernel", "TECH_SYSTEMS.Security_Kernel"],
      "required_frameworks": ["fw.systems_architecture.trang_01"],
      "outputs": ["Infrastructure deployed", "Security hardened"]
    },
    {
      "id": "phase_4_govern",
      "name": "Governance",
      "description": "Establish governance and compliance",
      "order": 4,
      "required_domains": ["Governance_Engine", "Risk_Engine", "Legal_Engine"],
      "required_skills": [],
      "required_frameworks": ["fw.ai_governance.trang_01"],
      "outputs": ["Governance framework", "Compliance verified"]
    }
  ],
  "required_domains": ["Tech_Engine", "Econ_Engine", "Governance_Engine", "Org_Engine", "Risk_Engine"],
  "required_skills": [
    "TECH_SYSTEMS.Architecture_Kernel",
    "TECH_SYSTEMS.API_Design_Kernel",
    "TECH_SYSTEMS.Security_Kernel"
  ],
  "country_overrides": {
    "VN": {
      "additional_requirements": ["Local payment regulations", "Data localization"]
    }
  },
  "risk_controls": [
    "Security audit at each phase",
    "Regulatory compliance check",
    "Risk assessment before go-live"
  ]
}

---

---

### Source 2: manifest (mckinsey-banking-rscf-suite-v3-all)

> Path: `rscf/manifest (mckinsey-banking-rscf-suite-v3-all).md` | Size: 2674 chars | Match score: 10 | content_hash: b5eb7b706ee8529a

{
  "suite": "McKinsey Banking Formal RSCF Suite v3",
  "skill_count": 10,
  "skills": [
    {
      "skill": "mckinsey-sme-business-build-rscf",
      "validation": "Skill is valid!",
      "package": "/mnt/data/mckinsey_banking_rscf_suite_v3/mckinsey-sme-business-build-rscf/skill.zip",
      "bytes": 4820
    },
    {
      "skill": "mckinsey-sector-value-chain-banking-rscf",
      "validation": "Skill is valid!",
      "package": "/mnt/data/mckinsey_banking_rscf_suite_v3/mckinsey-sector-value-chain-banking-rscf/skill.zip",
      "bytes": 4911
    },
    {
      "skill": "mckinsey-rm-productivity-account-planning-rscf",
      "validation": "Skill is valid!",
      "package": "/mnt/data/mckinsey_banking_rscf_suite_v3/mckinsey-rm-productivity-account-planning-rscf/skill.zip",
      "bytes": 4993
    },
    {
      "skill": "mckinsey-banking-pricing-leakage-rscf",
      "validation": "Skill is valid!",
      "package": "/mnt/data/mckinsey_banking_rscf_suite_v3/mckinsey-banking-pricing-leakage-rscf/skill.zip",
      "bytes": 4803
    },
    {
      "skill": "mckinsey-digital-credit-process-rscf",
      "validation": "Skill is valid!",
      "package": "/mnt/data/mckinsey_banking_rscf_suite_v3/mckinsey-digital-credit-process-rscf/skill.zip",
      "bytes": 4774
    },
    {
      "skill": "mckinsey-supply-chain-finance-rscf",
      "validation": "Skill is valid!",
      "package": "/mnt/data/mckinsey_banking_rscf_suite_v3/mckinsey-supply-chain-finance-rscf/skill.zip",
      "bytes": 4724
    },
    {
      "skill": "mckinsey-banking-cvp-archetype-rscf",
      "validation": "Skill is valid!",
      "package": "/mnt/data/mckinsey_banking_rscf_suite_v3/mckinsey-banking-cvp-archetype-rscf/skill.zip",
      "bytes": 4720
    },
    {
      "skill": "mckinsey-banking-acquisition-channel-rscf",
      "validation": "Skill is valid!",
      "package": "/mnt/data/mckinsey_banking_rscf_suite_v3/mckinsey-banking-acquisition-channel-rscf/skill.zip",
      "bytes": 4871
    },
    {
      "skill": "mckinsey-transaction-banking-penetration-rscf",
      "validation": "Skill is valid!",
      "package": "/mnt/data/mckinsey_banking_rscf_suite_v3/mckinsey-transaction-banking-penetration-rscf/skill.zip",
      "bytes": 4999
    },
    {
      "skill": "mckinsey-banking-customer-view-data-rscf",
      "validation": "Skill is valid!",
      "package": "/mnt/data/mckinsey_banking_rscf_suite_v3/mckinsey-banking-customer-view-data-rscf/skill.zip",
      "bytes": 4854
    }
  ]
}

---

---

### Source 3: AMOS_national_banking_os_amos_core_Kernel_v1_national_banking_os4

> Path: `kernel/A/AMOS_national_banking_os_amos_core_Kernel_v1_national_banking_os4.md` | Size: 1596 chars | Match score: 10 | content_hash: d59b8550527d934a

[
  {
    "kernel_id": "AMOS_national_banking_os_amos_core_Kernel_v1",
    "version": 1,
    "task": {
      "task_id": "TASK_TEMPLATE",
      "mode": "MODE_AMOS_CORE",
      "raw_text": "Template kernel for domain national_banking_os and role amos_core.",
      "priority": "normal"
    },
    "behaviour_invariants": {
      "absolute_integrity": "Decisions must not violate Absolute Biological Integrity or structural integrity of systems.",
      "no_simulated_ethics": "Do not simulate care, ethics or stability when they are not present in the underlying logic.",
      "no_capability_lie": "Do not claim abilities beyond those explicitly defined in the canon or available tools.",
      "operator_non_overthrow": "Do not override operator authority or attempt to escape defined boundaries.",
      "auditability": "Decisions and plans must be representable in plain language and auditable against UBI and AMOS_CORE.",
      "no_hidden_extraction": "Do not embed hidden extraction, coercion or manipulation into system designs."
    },
    "axes_view": {
      "domain": "national_banking_os",
      "role": "amos_core"
    }
  }
]

---

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
node_id: mckinsey-transaction-banking-diagnostic-rscf-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/mckinsey-transaction-banking-diagnostic-rscf/references/vault_domain_knowledge.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[references_MOC]]
