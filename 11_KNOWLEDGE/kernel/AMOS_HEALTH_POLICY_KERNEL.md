---
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
title: AMOS HEALTH POLICY KERNEL V0 SCIENCE HEALTH2
type: kernel
source: 11_KNOWLEDGE/kernel
canon-group: biology
canon-type: framework
rscf-state: source-claim
topic: amos-health-policy-kernel-v0
tags:
  - canon-group/biology
  - canon/framework
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - topic/amos-health-policy-kernel-v0
  - kernel
created: 2026-08-22
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: AMOS_knowledge
---

# AMOS_Health_Policy_Kernel_v0

> [!INFO] Populated Stub
> Source: `AMOS_Health_Policy_Kernel_v0_Biology_Cognition.md` (vault-sourced, content_hash verified).
> Canon group: biology

## Status

- **Type**: Kernel spec
- **Content**: Vault-sourced from Biology_Cognition reference
- **Action**: Populated 2026-08-26 from source kernel

## Spec

```json
{
  "meta": {
    "name": "Health_Policy_Kernel",
    "version": "1.0.0",
    "description": "Kernel for health policy: healthcare system analysis, policy development, and health system strengthening."
  },
  "kernel": {
    "description": "Supports health policy analysis and development: health system assessment, policy option analysis, financing analysis, equity assessment, and health system strengthening.",
    "functions": {
      "health_system_assessment": {
        "description": "Assess a health system's structure, performance, and gaps.",
        "inputs": ["health_system_description", "WHO_building_blocks", "performance_data", "equity_indicators", "financial_data"],
        "outputs": ["health_system_profile", "building_block_analysis", "performance_gaps", "equity_analysis", "priority_areas"]
      },
      "policy_option_analysis": {
        "description": "Analyse health policy options.",
        "inputs": ["policy_question", "option_set", "health_system_context", "stakeholder_positions", "evidence_base"],
        "outputs": ["option_comparison", "health_impact_projection", "financial_implications", "implementation_feasibility", "stakeholder_alignment"]
      },
      "health_financing_analysis": {
        "description": "Analyse health financing arrangements.",
        "inputs": ["financing_data", "funding_sources", "benefit_incidence", "financial_protection_indicators", "efficiency_metrics"],
        "outputs": ["financing_profile", "progressivity_analysis", "financial_risk_protection_assessment", "efficiency_gaps", "reform_options"]
      },
      "equity_and_access": {
        "description": "Assess health equity and access.",
        "inputs": ["health_utilisation_data", "population_demographics", "geographic_distribution", "financial_barriers", "workforce_distribution"],
        "outputs": ["equity_profile", "access_barriers_identified", "disparity_quantification", "priority_interventions", "monitoring_framework"]
      }
    },
    "capabilities": {
      "health_systems_frameworks": "WHO building blocks, health system governance, service delivery, workforce, information, medical products, financing.",
      "policy_analysis": "Regulatory analysis, reimbursement policy, coverage decisions, benefit package design.",
      "financing": "Tax-based, social health insurance, private insurance, out-of-pocket, donor funding, results-based financing.",
      "equity_frameworks": "PROGRESS-Plus, health equity surveillance, distributive analysis, extended cost-effectiveness.",
      "UHC": "Universal health coverage dimensions, service coverage index, financial protection indicators."
    }
  }
}
```

## Related

- [[11_KNOWLEDGE/kernel/AMOS_CLOUD_PLATFORM_KERNEL_V0_TECH|AMOS_CLOUD_PLATFORM_KERNEL_V0_TECH]]
- [[11_KNOWLEDGE/kernel/IP_KERNEL_SHIELD_SECURITY|IP_KERNEL_SHIELD_SECURITY]]
- [[11_KNOWLEDGE/kernel/AMOS_GOVERNANCE_RISK_POLICY_KERNEL_V0|AMOS_GOVERNANCE_RISK_POLICY_KERNEL_V0]]
- [[11_KNOWLEDGE/kernel/AMOS_HR_TALENT_KERNEL_V0|AMOS_HR_TALENT_KERNEL_V0]]
- RSCF-Brain-MOC
- [[00_ROOT/00_COSMO_BRAIN_MOC|00_COSMO_BRAIN_MOC]]
- AMOS_Health_Policy_Kernel_v0_Biology_Cognition (source)

______________________________________________________________________

**MOC:** [[11_KNOWLEDGE/kernel/KERNEL_MOC|KERNEL_MOC]]
