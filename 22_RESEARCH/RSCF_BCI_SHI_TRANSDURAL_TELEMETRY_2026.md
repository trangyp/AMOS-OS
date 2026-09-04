---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Rscf Bci Shi Transdural Telemetry 2026
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
AMOS_KNOWLEDGE_OBJECT:
  schema_family: RSCF
  schema_role: KNOWLEDGE_RSCF
  schema_version: AMOS_CORE_v4.4-compatible-conceptual
  object_status: ACTIVE_REFERENCE
  ingestion_state: PARTIAL_NORMALIZATION
  mutation_policy: APPEND_OR_VERSION_NEVER_SILENT_OVERWRITE

  identity:
    node_id: rscf_bci_shi_event_based_transdural_telemetry_2026
    canonical_slug: event-based-body-coupled-transdural-telemetry-2026
    canonical_title: An Event based Body Coupled Transdural Telemetry for Intracortical Brain Computer Interfaces
    source_title: An Event based Body Coupled Transdural Telemetry for Intracortical Brain Computer Interfaces
    preferred_path: {H: C04_BIO_NEURO, M: BCI_TELEMETRY, L: TRANSDURAL_BCC}
    node_type: KNOWLEDGE
    knowledge_type: [PEER_REVIEWED_ARTICLE, BCI, TELEMETRY, NEURAL_INTERFACE]
    source_epoch: {published: 2026-09-01, retrieved: 2026-09-04}

  epistemic_contract:
    source_boundary: >
      Publisher abstract and displayed results/system-design text were inspected. The entire paper,
      supplementary methods and all safety evidence were not exhaustively normalized.
    hard_rules:
      - TELEMETRY_BENCHMARK != CHRONIC_CLINICAL_EFFECTIVENESS
      - PHANTOM_OR_EX_VIVO_VALIDATION != IN_VIVO_HUMAN_DEPLOYMENT
      - THERMAL_GUIDELINE_COMPATIBILITY != COMPLETE_IMPLANT_SAFETY
    confidence_ceiling: {system_architecture: HIGH, chronic_clinical_claim: LOW}

  provenance:
    source_id: doi:10.1038/s44172-026-00735-z
    category: Communications Engineering / BCI telemetry
    authors: [Chengyao Shi, Laura Nuttin, Zhenyu Gao, Yuming He, Pietro Russo, Hua-Peng Liaw, Marios Gourdouparis, Dennis Lambrechts, Guido Dolmans, Yao-Hong Liu]
    source_type: [PEER_REVIEWED_PRIMARY_ARTICLE]
    source_topics: [intracortical BCI, body channel communication, transdural telemetry, event-based compression, thermal load]
    raw_source_policy: DO_NOT_LOAD_UNLESS_REQUIRED
    raw_source_load_triggers: [exact circuit detail, full safety method, exact phantom protocol, statistical comparison]

  bootstrap_capsule:
    class: DERIVED
    text: >
      The paper proposes a two-stage wireless iBCI architecture with a transdural galvanic-coupled
      body-channel link from a free-floating MEA to an intracranial unit, followed by a transcutaneous
      external link. The inspected publisher text reports phantom and ex-vivo cadaveric-head validation,
      transmission up to 500 Mbps at 20% duty cycling, BER below 1e-5, and send-on-delta compression up
      to 11.4x. Brain-on-a-chip experiments are reported as safety evidence against unintended neural
      activity. AMOS implication: telemetry, compression, power/thermal budget, signal integrity and
      clinical translation require separate evidence lanes.
    retrieval_keywords: [iBCI telemetry, body channel communication, transdural, SODA compression, implant bandwidth]

  HML:
    H: {id: H_BCI_IMPLANT_DATA_PATH, governing_question: "How can high-density intracortical data cross the dura under size/power/thermal constraints?", governing_fields: [BCI, implant telemetry], master_pattern: {class: DERIVED, expression: "MEA -> EVENT_COMPRESSION -> TRANSDURAL_BCC -> INTRACRANIAL_RX -> TRANSCUTANEOUS_LINK"}}
    M:
      id: M_TELEMETRY_STACK
      subsystems:
        free_floating_mea: neural source/interface
        event_encoder: send-on-delta compression
        transdural_bcc: galvanic-coupled body-channel link
        intracranial_receiver: bridge unit
        transcutaneous_link: downstream external path
        safety_models: phantom/ex-vivo/brain-on-chip evidence
    L:
      id: L_REPORTED_METRICS
      canonical_variables:
        throughput: "up to 500 Mbps"
        duty_cycle: "20%"
        ber: "< 1e-5"
        compression: "up to 11.4x"

  claim_graph:
    C1: {class: OBSERVATION, text: "Publisher reports up to 500 Mbps transmission with 20% duty cycling and BER below 1e-5 in the tested setup."}
    C2: {class: OBSERVATION, text: "SODA reportedly achieves up to 11.4x compression in the tested setup."}
    C3: {class: SOURCE_CLAIM, text: "Brain-on-a-chip testing did not evoke unintended neural activity under the tested conditions."}
    A1: {class: DERIVED, text: "BCI architecture must type telemetry maturity separately from decoder or clinical maturity."}

  dependency_graph:
    C1: [phantom/ex-vivo setup, channel design, measurement protocol]
    C2: [neural event distribution, encoder settings]
    C3: [brain-on-chip model validity, tested stimulation/telemetry envelope]
    A1: [C1, C2, C3]

  causal_firewall:
    source_supports: [component/system telemetry performance in tested models, reported safety-model observations]
    source_does_not_establish: [chronic implanted-human safety, long-term biocompatibility, clinical efficacy, decoder accuracy]

  applicability_envelope:
    modality: intracortical high-density MEA telemetry
    validation: phantom + ex-vivo human cadaveric head + brain-on-chip
    excluded_promotion: regulated chronic human use

  sensitivity:
    highest_leverage_variables: [data sparsity, compression setting, implant geometry, tissue/channel properties, duty cycle, thermal budget]
    result_flipping_conditions:
      - in-vivo channel loss/thermal behavior materially differs from tested models
      - compression degrades task-relevant neural information

  invalidation_conditions:
    - corrected/retracted source
    - independent in-vivo evidence contradicts performance/safety assumptions
    - AMOS uses telemetry metrics as proof of clinical effectiveness

  uncertainty_vector:
    evidence_uncertainty: MEDIUM
    model_uncertainty: MEDIUM
    scope_uncertainty: HIGH
    temporal_uncertainty: LOW
    causal_uncertainty: MEDIUM
    execution_uncertainty: MEDIUM
    provenance_independence_uncertainty: LOW
    dominant_uncertainty: translation from bench/ex-vivo/safety models to chronic implanted humans

  routing_index:
    aliases: [transdural BCC, iBCI telemetry, SODA BCI]
    semantic_routes:
      bandwidth_energy: [C1, C2]
      safety_boundary: [C3, causal_firewall, applicability_envelope]
      architecture_owner: [A1]

  failure_recovery: {rollback_policy: LOCAL_DEPENDENCY_INVALIDATION}
  lifecycle:
    pipeline: [EPHEMERAL_SOURCE, PERSISTENT_EVIDENCE, NORMALIZED_RSCF]
    current_stage: NORMALIZED_RSCF
    retention_class: FRONTIER_RESEARCH
    revalidation_triggers: [in-vivo study, chronic implant study, source revision]
    promotion_requirements: {knowledge: full-method inspection + independent evidence topology, clinical: regulated evidence}

  final_capsule:
    claim: {class: CONDITIONAL, text: "The tested transdural BCC architecture is a promising telemetry primitive, not evidence of chronic clinical BCI effectiveness."}
    strongest_source_support: [peer-reviewed article, reported bench/ex-vivo metrics]
    weakest_load_bearing_premises: [translation from test models to living chronic implant]
    unresolved: [long-term in-vivo performance, full safety envelope]
    confidence_ceiling: {telemetry_architecture: HIGH, clinical_translation: LOW}
    safe_reuse: [BCI telemetry subsystem architecture, maturity firewall]
    revalidation_required: [human chronic deployment claim]
