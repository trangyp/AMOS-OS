---
title: "AMOS Medical Clinical Kernel vInfinity"
type: kernel
source: 11_KNOWLEDGE/kernel
created: "2026-08-22"
origin: "Google Drive — _00_AMOS_CANON/Kernels/Biology_Cognition/AMOS_Medical_Clinical_Kernel_v0.json (253 lines, 7KB)"
origin_type: "SOURCE"
category: "kernel"
tags:
- amos
- medical
- clinical
- kernel
- v-infinity
- differential-diagnosis
- risk-assessment
- care-pathways
- lens-space
- canon/knowledge
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: AMOS_knowledge
---


# AMOS Medical Clinical Kernel vInfinity

## Meta
- **Name**: Medical_Clinical_Kernel_vInfinity_SUPER
- **Version**: v2.0.0+lens_integration
- **Created**: 2025-11-28T00:10:18.516087Z
- **Description**: Medical / Clinical kernel for structuring differentials, risk, and care pathways (non-prescriptive). Enriched with cross-canon integration, lens_space, and template_library.
- **Domain**: medical_and_clinical_reasoning
- **Density Profile**: kernel_x100k_virtual
- **Cluster Count**: 20
- **Dimension Count**: 20

---

## 20 Clinical Clusters
| ID | Cluster | Focus |
|----|---------|-------|
| 1 | symptom_history_and_presenting_complaint | Patient symptom history and presenting complaint |
| 2 | risk_factors_and_epidemiology | Risk factors and epidemiological context |
| 3 | systems_review | Systematic review of organ systems |
| 4 | physical_examination_structures | Physical examination frameworks |
| 5 | differential_diagnosis_generation | Structured differential diagnosis |
| 6 | diagnostic_test_selection | Evidence-based test selection |
| 7 | labs_and_imaging_interpretation | Lab and imaging result interpretation |
| 8 | severity_and_stability_assessment | Clinical severity and stability scoring |
| 9 | red_flags_and_emergency_signs | Red flag detection and emergency signs |
| 10 | risk_scoring_tools | Clinical risk scoring tools |
| 11 | treatment_options_mapping | Treatment option mapping |
| 12 | shared_decision_making_structure | Shared decision-making frameworks |
| 13 | medication_selection_and_dosing | Medication selection and dosing |
| 14 | non_pharmacological_interventions | Non-pharmacological interventions |
| 15 | monitoring_and_follow_up_plans | Monitoring and follow-up plans |
| 16 | referral_and_consultation_logic | Referral and consultation criteria |
| 17 | clinical_documentation_and_notes | Clinical documentation structures |
| 18 | triage_and_prioritisation | Triage and prioritization logic |
| 19 | care_pathways_and_protocols | Care pathways and protocols |
| 20 | public_health_and_prevention_context | Public health and prevention context |

---

## 20 Clinical Dimensions
| ID | Dimension | Description |
|----|-----------|-------------|
| 01 | symptom_severity | Severity of presenting symptoms |
| 02 | acuity | Clinical acuity level |
| 03 | risk_of_deterioration | Risk of clinical deterioration |
| 04 | diagnostic_uncertainty | Uncertainty in diagnosis |
| 05 | evidence_quality | Quality of supporting evidence |
| 06 | benefit_risk_balance | Benefit-risk balance of interventions |
| 07 | patient_preference_alignment | Alignment with patient preferences |
| 08 | resource_availability | Resource availability for care |
| 09 | time_sensitivity | Time sensitivity of decision |
| 10 | safety_margin | Safety margin in decision |
| 11 | guideline_alignment | Alignment with clinical guidelines |
| 12 | comorbidity_burden | Comorbidity burden |
| 13 | polypharmacy_risk | Polypharmacy risk |
| 14 | adherence_feasibility | Feasibility of adherence |
| 15 | follow_up_reliability | Reliability of follow-up |
| 16 | equity_and_access | Equity and access considerations |
| 17 | ethical_considerations | Ethical considerations |
| 18 | family_and_social_context | Family and social context |
| 19 | public_health_impact | Public health impact |
| 20 | need_for_specialist_input | Need for specialist referral |

---

## Virtual Expansion Model (x100k)
**Virtual Layer Count**: 100,000

### Axes
| Axis | Values |
|------|--------|
| **care_setting** | primary_care, emergency, inpatient, outpatient_specialist, telemedicine |
| **urgency** | immediate_emergency, urgent, semi_urgent, routine |
| **age_group** | neonate, child, adult, older_adult |

**Notes**: Each virtual stateframe is a point in this kernel's tensor space. Use to derive scenarios, evaluations, or plans without storing all explicit layers.

---

## Mapping Functions
### F_cluster_selection
- **Input**: clinical_question, patient_context
- **Output**: cluster_vector_med
- **Logic**: Structure the reasoning task in clinical terms

---

## Reasoning Modes
### mode_structuring_only
- **Description**: Only structure differential and reasoning steps; no direct diagnosis or treatment instruction
- **Pipeline**: F_cluster_selection

---

## Policies
### Safety (2)
1. Do not provide definitive diagnoses or prescribe treatments
2. Always advise consultation with qualified healthcare professionals

---

## Integration Links
**Depends On**:
- AMOS_Scientific_SUPER_Engine
- AMOS_C04_bio_neuro

**Notes**: These references point to full AMOS SUPER engines and C-Canon blocks. Kernel power is derived from combining this kernel with referenced engines at runtime.

---

## Lens Space (4 Views)

### exec (executive_view)
- **Description**: Top-layer view for CEOs, boards, ministers, and investors
- **Focus**: risk, impact, time_horizon, portfolio, tradeoffs

### operator (operator_view)
- **Description**: Execution view for managers and implementers
- **Focus**: process, sequence, dependencies, owners

### expert (expert_view)
- **Description**: Deep domain view for specialists
- **Focus**: method, assumptions, edge_cases

### audit (audit_view)
- **Description**: Assurance and governance view
- **Focus**: controls, evidence, compliance

---

## Template Library
### Doc Templates (4)
exec_one_pager, full_strategy_pack, operating_playbook, risk_and_decision_memo

### Deck Templates (5)
board_update, investment_case, initiative_kickoff, postmortem_review

### Table Templates (3)
option_comparison_matrix, risk_register, kpi_scorecard

---

## Routing
- **clinical_structuring** → mode_structuring_only

---

**Conclusion**: SOURCE — Medical/Clinical kernel with 20 clusters spanning symptom history through public health context, 20 clinical dimensions covering severity/risk/evidence/safety/equity, x100k virtual expansion with 3 axes (care_setting, urgency, age_group), structuring-only reasoning mode (non-prescriptive), integration links to Scientific SUPER and C04 bio_neuro, 4-lens space (exec/operator/expert/audit), and template library. Production-ready for clinical reasoning structuring tasks.

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[KERNEL_MOC]]
