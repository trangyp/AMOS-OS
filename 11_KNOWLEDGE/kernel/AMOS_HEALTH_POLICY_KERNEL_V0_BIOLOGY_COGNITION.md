---
tags: [canon-group/biology, canon/framework, rscf/claim, rscf/provenance, rscf/state/source-claim, topic/amos-health-policy-kernel-v0, kernel]
---

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
        "outputs": ["equity_profile", "access_barriers_identified", "disparity Quantification", "priority_interventions", "monitoring_framework"]
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

---
**Related:** [[docs/moc/00-Home]] · [[docs/moc/06-Knowledge-Base-MOC]] · [[docs/brain/AMOS_Simulation_Kernel_v0_Math_Foundations]] · [[docs/brain/system_scan_agent]] · [[docs/brain/automation_profiles]]
