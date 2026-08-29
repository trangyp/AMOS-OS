---
title: MEDICAL CLINICAL KERNEL VINFINITY SUPER
type: kernel
source: 11_KNOWLEDGE/kernel
canon-group: biology
canon-type: framework
rscf-state: source-claim
topic: medical-clinical-kernel-vinfinity-super
tags:
- canon-group/biology
- canon/framework
- rscf/claim
- rscf/provenance
- rscf/state/source-claim
- topic/medical-clinical-kernel-vinfinity-super
- kernel
- kernel-moc
created: 2026-08-22
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: AMOS_knowledge
---

# MEDICAL CLINICAL KERNEL VINFINITY SUPER

```json
{
  "meta": {
    "name": "Medical_Clinical_Kernel_vInfinity_SUPER",
    "version": "v1.0.0",
    "created_at_utc": "2025-11-27T23:55:30.600895Z",
    "description": "Kernel skeleton for Medical Clinical Kernel."
  },
  "kernel": {
    "cluster_space": {
      "total_clusters": 20,
      "clusters": [
        {"id": 1, "name": "symptom_history_and_presenting_complaint"},
        {"id": 2, "name": "risk_factors_and_epidemiology"},
        {"id": 3, "name": "systems_review"},
        {"id": 4, "name": "physical_examination_structures"},
        {"id": 5, "name": "differential_diagnosis_generation"},
        {"id": 6, "name": "diagnostic_test_selection"},
        {"id": 7, "name": "labs_and_imaging_interpretation"},
        {"id": 8, "name": "severity_and_stability_assessment"},
        {"id": 9, "name": "red_flags_and_emergency_signs"},
        {"id": 10, "name": "risk_scoring_tools"},
        {"id": 11, "name": "treatment_options_mapping"},
        {"id": 12, "name": "shared_decision_making_structure"},
        {"id": 13, "name": "medication_selection_and_dosing"},
        {"id": 14, "name": "non_pharmacological_interventions"},
        {"id": 15, "name": "monitoring_and_follow_up_plans"},
        {"id": 16, "name": "referral_and_consultation_logic"},
        {"id": 17, "name": "clinical_documentation_and_notes"},
        {"id": 18, "name": "triage_and_prioritisation"},
        {"id": 19, "name": "care_pathways_and_protocols"},
        {"id": 20, "name": "public_health_and_prevention_context"}
      ]
    },
    "dimension_space": {
      "total_dimensions": 20,
      "dimensions": {
        "01": "symptom_severity",
        "02": "acuity",
        "03": "risk_of_deterioration",
        "04": "diagnostic_uncertainty",
        "05": "evidence_quality",
        "06": "benefit_risk_balance",
        "07": "patient_preference_alignment",
        "08": "resource_availability",
        "09": "time_sensitivity",
        "10": "safety_margin",
        "11": "guideline_alignment",
        "12": "comorbidity_burden",
        "13": "polypharmacy_risk",
        "14": "adherence_feasibility",
        "15": "follow_up_reliability",
        "16": "equity_and_access",
        "17": "ethical_considerations",
        "18": "family_and_social_context",
        "19": "public_health_impact",
        "20": "need_for_specialist_input"
      }
    },
    "virtual_expansion_model": {
      "density_level": "x100k_virtual",
      "virtual_layer_count": 100000,
      "axes": {
        "care_setting": ["primary_care", "emergency", "inpatient", "outpatient_specialist", "telemedicine"],
        "urgency": ["immediate_emergency", "urgent", "semi_urgent", "routine"],
        "age_group": ["neonate", "child", "adult", "older_adult"]
      }
    },
    "mapping_functions": {
      "F_cluster_selection": {
        "input": ["clinical_question", "patient_context"],
        "output": "cluster_vector_med",
        "logic": "Structure the reasoning task in clinical terms."
      }
    },
    "reasoning_modes": {
      "mode_structuring_only": {
        "description": "Only structure differential and reasoning steps; no direct diagnosis or treatment instruction.",
        "pipeline": ["F_cluster_selection"]
      }
    },
    "policies": {
      "safety": [
        "Do not provide definitive diagnoses or prescribe treatments.",
        "Always advise consultation with qualified healthcare professionals."
      ]
    },
    "routing": {
      "by_task_type": {
        "clinical_structuring": "mode_structuring_only"
      }
    }
  }
}

---
**Related:** [[DOCUMENTATION_KERNEL_V0]] · [[AMOS_DESIGN_KERNEL]] · [[AMOS_META_EPISTEMOLOGY_KERNEL]] · [[AMOS_ORG_GOVERNANCE_KERNEL]]
```

---
**MOC:** [[KERNEL_MOC]]
