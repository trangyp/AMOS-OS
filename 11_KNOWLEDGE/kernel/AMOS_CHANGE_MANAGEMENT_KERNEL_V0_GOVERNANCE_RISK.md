---
title: AMOS CHANGE MANAGEMENT KERNEL V0 GOVERNANCE RISK
tags:
- canon-group/human-system
- canon/framework
- rscf/claim
- rscf/provenance
- rscf/state/source-claim
- topic/amos-change-management-kernel-v0
- kernel
- kernel-moc
type: data
source: 11_KNOWLEDGE/kernel
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: AMOS_knowledge
---

# AMOS CHANGE MANAGEMENT KERNEL V0 GOVERNANCE RISK

```json
{
  "meta": {
    "name": "Change_Management_Kernel",
    "version": "1.0.0",
    "description": "Kernel for change management: organisational change planning, stakeholder engagement, and change adoption."
  },
  "kernel": {
    "description": "Supports change management: change strategy, stakeholder impact analysis, communication planning, resistance management, and adoption measurement.",
    "functions": {
      "change_strategy": {
        "description": "Define the change strategy and approach.",
        "inputs": ["change_description", "change_rationale", "scope", "constraints", "stakeholder_context"],
        "outputs": ["change_strategy_document", "change_model_selection", "success_definition", "risk_assumptions"]
      },
      "stakeholder_impact": {
        "description": "Analyse how change affects different stakeholders.",
        "inputs": ["change_description", "stakeholder_list", "current_state_for_each_group", "future_state_for_each_group"],
        "outputs": ["impact_matrix", "stakeholder_readiness Assessment", "resistance_predictions", "support_needs"]
      },
      "communication_plan": {
        "description": "Design change communication.",
        "inputs": ["change_description", "stakeholder_segments", "key_messages", "communication_channels", "timing"],
        "outputs": ["communication_plan", "message_matrix_by_audience", "channel_strategy", "feedback_mechanisms"]
      },
      "adoption_measurement": {
        "description": "Measure change adoption and effectiveness.",
        "inputs": ["change_objectives", "adoption_indicators", "measurement_methods", "baseline_data"],
        "outputs": ["adoption_dashboard", "progress_against_targets", "barriers_identified", "course_correction_recommendations"]
      }
    },
    "capabilities": {
      "change_models": "Kotter 8-step, ADKAR, Lewin's unfreeze-change-refreeze, McKinsey 7-S, agile change.",
      "stakeholder_analysis": "Impact assessment, readiness assessment, influence-interest mapping.",
      "communication": "Message development, channel selection, frequency planning, two-way feedback.",
      "resistance_management": "Resistance root cause analysis, targeted interventions, sponsor coaching.",
      "adoption_metrics": "Usage metrics, proficiency measures, behavioural change indicators, stakeholder sentiment."
    }
  }
}

---
**Related:**  ·  ·  ·  · 
```

---
**MOC:** [[KERNEL_MOC]]
