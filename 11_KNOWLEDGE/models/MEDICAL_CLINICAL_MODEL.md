---
title: MEDICAL CLINICAL MODEL
type: model
source: 11_KNOWLEDGE/models
aliases: [Medical Clinical Kernel, AMOS_Medical_Clinical]
tags: [canon-group/tech-ai, canon/model, rscf/claim, rscf/provenance, rscf/state/observation, topic/medical-clinical-model, models]
rscf:
  state: AMOS_MODEL
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: model_specification
---


# AMOS Medical & Clinical Engine Kernel

**Version:** 2.0.0+lens_integration
**Source:** `AMOS_Medical_Clinical_Kernel_v0.json`

The **Medical & Clinical Kernel** provides structural reasoning for differentials, risk, and care pathways. It is non-prescriptive and primarily a framing tool.

## Safety and Boundary Policies
- **No Prescribing:** Do not provide definitive diagnoses or prescribe treatments.
- **Consultation Required:** Always explicitly state that qualified healthcare professionals must be consulted.

## Dimensions & Clusters
- **20 Clinical Clusters:** Encompasses everything from symptom history, physical examination structures, and red flags, to public health contexts and triage.
- **20 Dimensions:** Includes acuity, risk of deterioration, time sensitivity, safety margin, polypharmacy risk, and ethical considerations.

## Virtual Expansion Axes
The kernel operates within virtual stateframes combining:
- **Care Setting:** Primary care, emergency, inpatient, outpatient, telemedicine.
- **Urgency:** Immediate emergency down to routine.
- **Age Group:** Neonate, child, adult, older adult.

## Lens Space Integration
Outputs adjust to:
- **Exec View:** Risk and impact.
- **Operator View:** Sequence and triage.
- **Expert View:** Edge cases and assumptions.
- **Audit View:** Evidence and compliance controls.

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MODELS_MOC]]
