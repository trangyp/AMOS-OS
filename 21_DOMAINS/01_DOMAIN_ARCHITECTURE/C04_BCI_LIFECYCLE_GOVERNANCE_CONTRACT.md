---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: C04 Bci Lifecycle Governance Contract
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

# C04 BCI Lifecycle Governance Contract

## 1. Role

This contract owns the **functional lifecycle boundary** for implanted or otherwise dependency-creating BCI systems after initial feasibility: maintenance, support continuity, software/model updates, post-trial transition, deactivation, transfer, abandonment risk, explantation and terminal data/model disposition.

It does not perform surgery, provide legal advice, establish jurisdiction-specific duties, or authorize a clinical intervention.

```text
IMPLANT SUCCESS != LIFECYCLE CLOSURE
TRIAL END != DUTY END
SOFTWARE END-OF-SUPPORT != SAFE DEVICE END
EXPLANT OPTION != EXPLANT OBLIGATION
INITIAL CONSENT != PERMANENT AUTHORITY FOR FUTURE REMOVAL
```

## 2. MECE lifecycle states

1. **Active supported use** — device/model operates with current medical, technical and financial support.
2. **Maintenance / update** — components, decoder, firmware, calibration or security controls require change.
3. **Degraded support** — supplier/research capability is reduced but continuity remains possible.
4. **Transfer / handover** — responsibility moves to another clinical, technical or organizational owner.
5. **Post-trial continuation** — research phase ends while participant remains dependent on the system.
6. **Planned deactivation** — function is intentionally stopped without immediate explant.
7. **Abandonment-risk state** — required support may become unavailable because of insolvency, program closure, obsolete hardware/software, loss of expertise or financing.
8. **Explantation evaluation** — removal is considered as a distinct clinical/ethical decision.
9. **Explantation / retained dormant implant** — device is removed, partially removed, or retained inactive according to current evidence, preference and risk.
10. **Terminal data/model disposition** — raw signals, decoded outputs, model weights, adaptation state and credentials are exported, retained, transferred or deleted under explicit authority.

## 3. Lifecycle object

```yaml
BCILifecycle:
  participant_or_user_scope:
  device_identity:
  implant_components:
  software_firmware_versions:
  decoder_model_identity:
  support_owner:
  medical_owner:
  technical_owner:
  financial_owner:
  vendor_sponsor_state:
  labeled_or_expected_lifetime:
  patch_update_path:
  replacement_parts_path:
  calibration_support_path:
  data_export_path:
  model_export_path:
  emergency_disable:
  deactivation_plan:
  post_trial_plan:
  insolvency_or_shutdown_plan:
  transfer_plan:
  explant_options:
  explant_risks:
  retained_implant_risks:
  current_user_preference:
  renewed_consent_state:
  privacy_security_state:
  unresolved_obligations:
  review_date:
```

## 4. Evidence-backed lifecycle concerns

A 2024 JAMA Network Open consensus statement on neurological device abandonment proposes that abandonment can involve failures to provide fundamental consent-relevant information, reasonable medical/technical/financial support through the device lifetime, or responses to safety/ineffectiveness needs.

A 2025 systematic review of neural-device explantation found that the decision space extends beyond medical complications to therapeutic benefit, emotional well-being, identity, autonomy, financial issues, post-trial responsibility and neurorights.

2026 ethics work further highlights that long-term embodiment or functional dependence can change the meaning of earlier consent to explantation. This is normative analysis, not universal legal doctrine.

## 5. Governance invariants

### LIFECYCLE-1 Pre-implant support disclosure
Before an irreversible implant decision, material uncertainty about post-trial support, maintenance, funding, vendor failure and explant options should be visible.

### LIFECYCLE-2 No silent abandonment
Loss of sponsor/company/research support enters a governed degraded state; it is not treated as a normal completion event.

### LIFECYCLE-3 Renewed decision authority
Explantation/deactivation decisions use current clinical evidence, current user preference and current risk-benefit state. Historical consent alone is not sufficient when circumstances materially changed.

### LIFECYCLE-4 Functional dependence matters
If the BCI has become a primary communication, mobility or agency channel, withdrawal of support has a consequence radius beyond ordinary software discontinuation.

### LIFECYCLE-5 Software/model continuity is a medical-device dependency where function depends on it
Decoder weights, calibration state, firmware, credentials and compatible compute can be necessary to preserve function. Their loss must be represented explicitly.

### LIFECYCLE-6 Privacy survives support termination
End-of-support does not erase duties or user interests around neural data, decoded inferences, personalized model parameters and adaptation state.

### LIFECYCLE-7 Security patch sunset is a risk transition
If security updates cease, the system becomes a changed-risk regime requiring re-evaluation rather than silent continued use.

### LIFECYCLE-8 Explant is not automatically safer
Removal can itself create surgical and functional risk; retained inactive hardware can also create risk. The architecture preserves both branches until a clinical decision is made.

## 6. Cross-plane handoffs

- C09 / Operating Model: sponsor, clinical, technical, financial roles and escalation.
- Control Plane: authority/freshness for updates, stimulation, deactivation and disclosure effects.
- Security: credential rotation, patching, remote-access shutdown, retained-data controls.
- Memory/Knowledge: preserve provenance and distinguish user-owned data from research-derived models.
- Operations: maintenance, incident, transfer, deactivation and explant runbooks.
- Observability: device health, drift, update history, adverse events, support-state changes.
- Interfaces/Tools: replacement compatibility and hardware/software API continuity.
- Research: current evidence and competing lifecycle models.

## 7. Failure modes

- study ends before a support owner is identified;
- vendor insolvency strands a functioning implant;
- decoder/cloud dependency becomes unavailable;
- obsolete connector or compute hardware makes the implant unusable;
- security support ends while remote connectivity remains enabled;
- participant cannot export their personalized model/data;
- explant is assumed from old consent despite changed dependence/preferences;
- device is left in place without monitoring plan;
- support obligations are described but not financially provisioned;
- responsibility is fragmented across sponsor, hospital and vendor with no terminal owner.

## 8. Evidence / authority boundary

This contract is a source-bound AMOS model. It does not establish jurisdiction-specific legal obligations, clinical indications, insurance coverage, or a universal right to continued device support. Those require current domain-specific authority.

---
RSCF-NODE
node_id: c04_bci_lifecycle_governance_contract
node_type: specialist_domain_contract
claim_class: AMOS_MODEL
