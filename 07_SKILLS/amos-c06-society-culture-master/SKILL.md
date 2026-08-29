---
schema_version: 1.0
title: SKILL — Amos C06 Society Culture Master
type: skill
source: 07_SKILLS/amos-c06-society-culture-master
name: amos-c06-society-culture-master
description: AMOS C06 Society & Culture — social dynamics, cultural analysis, Vietnamese
  language/regional analysis, linguistic patterns, anthropology. Use when social analysis,
  cultural reasoning, or Vietnamese. Do not use for generic tasks outside c06 domain.
parent_skill: none
domain: c06
origin_architect: Trang Phan
epistemic_class: SOURCE_CANON
tags:
- type/skill
- type/skill
- domain/society-culture
- epistemic/source_claim
- hml/m
- epistemic/source_canon
- amos-os
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
rscf_state: SOURCE_CLAIM
hml_level: M
gmef_gates:
- L0_integrity
- L1_epistemic
- L2_provenance
- L5_scope
- L7_authority
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance:
- L0
- L1
- L2
- L4
- L5
- L7
- L16
- L17
- L18
license: MIT
steward: Trang Phan
---

# AMOS C06 — Society & Culture Master Knowledge

## Identity

Origin architect and steward: **Trang Phan**.

This is a **parent skill** that consolidates 17 sub-skills into a single domain master.
Following the skill-organizer best practice: fewer, richer skills beat many overlapping ones.
A parent skill with clearly labeled sections is better than 17 separate shallow skills.

**Epistemic class**: SOURCE_CLAIM (vault-sourced from `11_KNOWLEDGE/AMOS_C06_SOCIETY_CULTURE_MASTER_KNOWLEDGE.md` (content_hash: 6277c28f48ab4433)).

## When to Use

- When analyzing social dynamics, power structures, or collective action patterns
- When performing cultural analysis, linguistic pattern analysis, or anthropological reasoning
- When analyzing Vietnamese language/regional patterns and heritage
- When mapping institutional incentives and cultural codes in conflicts
- When a child skill routes a social, cultural, or anthropological task to this master

- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **c06.political_analysis**: F01 — Populate the 5-axis political state model (political_system_context · actors_and_interests · institutions_and_rules · power_and_conflict · change_and_stability) before any political analysis. An unpopulated axis is an unstated assumption. Generate ≥2 rival readings of the same facts; single-interpretation output is contract-invalid. Distinguish description from prescription; avoid bias toward particular outcomes. Label power definitions (capacity / agenda-control / preference-shaping) — silently switching conflates different mechanisms.
- **c06.institutional_analysis**: F02 — Map formal rules vs informal norms; measuring only the formal layer misreads real governance. Track state capacity across extractive, coercive, administrative, informational, and juridical dimensions. Apply CPR design principles as empirical regularities within studied regimes, not universal laws. Identify institutional change pathways (drift, layering, conversion, displacement, crisis redesign) — predicting which dominates requires actor configuration and veto-structure analysis, not just rule text.
- **c06.network_collective_action**: F03 — Compute network quantities (degree, betweenness, clustering, homophily). Distinguish simple vs complex contagion — clustered networks aid adoption of costly behaviors where simple contagion does not. Surface collective-action free-riding and its empirical solutions (selective incentives, identity, repeated-game reputation). Report network sampling design; missing ties and platform artifacts can invert conclusions. Weak ties carry novel information; strong ties carry trust — both are complements, not rivals.
- **c06.cultural_transmission**: F04 — Analyze culture as shared, learned patterns transmitted across generations. Apply cultural dimension frameworks as coarse country-level averages only — never predict individual behavior from them. Model Vietnamese ritual energy (gia hệ) as MODEL-class structural metaphors, NOT physically measurable quantities. Track cultural change mechanisms (transmission bias, prestige, migration, institutional change). Apply repair-survival condition: continuity requires maintenance exceeding decay; numeric thresholds (e.g., 0.6) are uncalibrated placeholders.
- **c06.conflict_change**: F05 — Classify conflict forms by opportunity structure, repression costs, and institutional access. Apply bargaining models with incomplete information (delay and breakdown risk that complete-info models miss). Distinguish escalation mechanisms (security-dilemma spirals, audience costs, sunk-cost entrapment, commitment problems) — each implies different de-escalation levers; conflating them produces wrong advice. Separate structural vulnerability (slow variables) from triggers (fast variables); point predictions of regime change dates are almost never defensible.
- **c06.ethics_fairness**: F06 — Apply six fairness governance gates (BiasAudit, DistributionalHarm, StakeholderRegistry, ExternalityModeler, EthicalConflict, EmergencyPower). Enforce gate precedence: FAIL > CONDITIONAL everywhere; emergency-power precedence: abuse_detected > no-sunset > no-oversight > active. Declare fairness metric choice as a value decision (impossibility results among parity-type criteria under unequal base rates). Enforce consent lifecycle (PENDING → GRANTED → WITHDRAWN | EXPIRED); withdrawn consent = absolute block. Apply HIE safety constraints: never induce panic, never coerce, never invalidate lived experience.
- **c06.vietnam_regional**: F07 — Operate within VN engine stack (Legal, Omnistructure, vInfinity) across 63 provinces and 8 legal domains. Enforce mandatory guardrails: No Legal Advice gate (Vietnamese disclaimer), No Evasion gate (no tax evasion / AML circumvention), conservative compliance-first bias. Respect physical grounding (North–South logistics, port capacities, urban density) and political mapping (central committee → provincial → district). Apply Sắc-Gọn-Chắc writing calibration for executive Vietnamese. Verify provincial implementation against current sources — C06 provides structure, not live regulatory text.
- **c06.social_measurement**: F08 — Apply survey error taxonomy (coverage, sampling, nonresponse, measurement, processing). Flag sensitive-topic self-report bias varying by political context. Test measurement invariance before cross-national ranking — identical questions do not produce identical constructs across cultures. Report platform bias in digital trace data (users ≠ populations). Enforce indicator hygiene: every social indicator must answer what decision changes if it moves; indicators without decision linkage are decoration.
- **c06.scenario_intervention**: F09 — Distinguish scenarios from forecasts: "if A,B,C hold, then outcome distribution X is modeled" — not a forecast absent justified probabilities. Every political scenario set must contain ≥2 rival readings with discriminating observations. Name intervention mechanism before tool (incentives, information, capability, coordination, norms). Apply unintended-consequences checklist (displacement, adaptation, perverse incentives, elite capture, legitimacy costs, measurement gaming). Attribution requires counterfactual reasoning plus mechanism evidence — before/after alone is insufficient.
- **c06.meta_society_bridge**: F10 — Apply Alternative-Interpretation Operator: AI(x) = {interpretation_1, ..., interpretation_k}, k ≥ 2, each carrying mechanism, supporting evidence, discriminating observation. Contract fails if k < 2, if interpretations are strawman variants, or if no discriminating observation identified. Model cultural entropy (CulturalDrift = TransmissionDecay − RepairRate). Enforce cross-domain coupling firewalls: environment→society only through specified mediators; mind→society only via aggregation mechanisms. Chain confidence cannot exceed weakest load-bearing edge.

## Operations

1. **c06.political_analysis**: F01 — Populate the 5-axis political state model (political_system_context · actors_and_interests · institutions_and_rules · power_and_conflict · change_and_stability) before any political analysis. An unpopula...
2. **c06.institutional_analysis**: F02 — Map formal rules vs informal norms; measuring only the formal layer misreads real governance. Track state capacity across extractive, coercive, administrative, informational, and juridical dimensions...
3. **c06.network_collective_action**: F03 — Compute network quantities (degree, betweenness, clustering, homophily). Distinguish simple vs complex contagion — clustered networks aid adoption of costly behaviors where simple contagion does n...
4. **c06.cultural_transmission**: F04 — Analyze culture as shared, learned patterns transmitted across generations. Apply cultural dimension frameworks as coarse country-level averages only — never predict individual behavior from them. Mod...
5. **c06.conflict_change**: F05 — Classify conflict forms by opportunity structure, repression costs, and institutional access. Apply bargaining models with incomplete information (delay and breakdown risk that complete-info models miss). D...
6. **c06.ethics_fairness**: F06 — Apply six fairness governance gates (BiasAudit, DistributionalHarm, StakeholderRegistry, ExternalityModeler, EthicalConflict, EmergencyPower). Enforce gate precedence: FAIL > CONDITIONAL everywhere; emergen...
7. **c06.vietnam_regional**: F07 — Operate within VN engine stack (Legal, Omnistructure, vInfinity) across 63 provinces and 8 legal domains. Enforce mandatory guardrails: No Legal Advice gate (Vietnamese disclaimer), No Evasion gate (no tax...
8. **c06.social_measurement**: F08 — Apply survey error taxonomy (coverage, sampling, nonresponse, measurement, processing). Flag sensitive-topic self-report bias varying by political context. Test measurement invariance before cross-nation...
9. **c06.scenario_intervention**: F09 — Distinguish scenarios from forecasts: "if A,B,C hold, then outcome distribution X is modeled" — not a forecast absent justified probabilities. Every political scenario set must contain ≥2 rival readin...
10. **c06.meta_society_bridge**: F10 — Apply Alternative-Interpretation Operator: AI(x) = {interpretation_1, ..., interpretation_k}, k ≥ 2, each carrying mechanism, supporting evidence, discriminating observation. Contract fails if k < 2, if...

## Vault-Sourced Domain Knowledge

> **Source**: `11_KNOWLEDGE/AMOS_C06_SOCIETY_CULTURE_MASTER_KNOWLEDGE.md` (content_hash: 6277c28f48ab4433) (vault canon, SOURCE_CLAIM)

### Source Family Mapping

The domain is organized into source families:

- **F01**: Political dynamics and power
- **F02**: Institutions and governance
- **F03**: Social networks and collective action
- **F04**: Culture, ritual, and transmission
- **F05**: Conflict, cooperation, and change
- **F06**: Ethics, fairness, and consent
- **F07**: Vietnam regional systems
- **F08**: Monitoring and social data
- **F09**: Scenarios, policy, and intervention
- **F10**: Meta-society research bridge

### Major Knowledge Modules

- H1: Political Dynamics, Power & Conflict — political dynamics kernel, power, conflict/cooperation
- H2: Institutions & Governance — state capacity, common-pool resources
- H3: Social Networks & Collective Action — network structure, diffusion, collective action
- H4: Culture, Ritual & Transmission — Vietnamese cultural ritual energy (gia hệ) [MODEL]
- H5: Social Change, Stability & Regime Dynamics — change and stability

### Epistemic Classification

- **Conclusion class**: MIXED (established science + model projections + AMOS synthesis)
- **Evidence policy**: typed_per_node (each claim carries its own evidence type)
- **Canon status**: DOMAIN_KNOWLEDGE_WITH_RESEARCH_BRIDGES
- **Architecture**: HML_fractal_single_file (H/M/L cross-scale reasoning)

### Epistemic Boundary

Social analysis is always context-, population-, institution-, and timescale-dependent. Contested sociological claims are COMPETING-tagged. Political analysis must remain descriptive unless prescription is explicitly framed. Alternative interpretations REQUIRED for all political output. Ritual energy/lineage energy are NOT physically measurable quantities. Power-law claims frequently overstated from sparse data.


## Reasoning Procedure — F01→F10 Pipeline with P1 Reality Contact Loop

> Each step uses a domain family from the vault knowledge and passes through the P1 Reality Contact Loop. The universalization firewall applies throughout: no VN-specific or single-society claim is universalized without cross-cultural evidence.

### Step 1: Political State Setup (F01)
**Precondition**: Political question or scenario received.
**Operation**: Populate the 5-axis state model (political_system_context · actors_and_interests · institutions_and_rules · power_and_conflict · change_and_stability). An axis left unpopulated is an unstated assumption — block until assumption register exists. Generate ≥2 rival readings of the same facts. Distinguish description from prescription; flag any prescriptive slippage.
**P1 Gate**: Is the output a single-interpretation political analysis? If yes → contract-invalid; regenerate with ≥2 rival readings. Is any axis silently unpopulated? If yes → unstated assumption, block.
**Self-audit**: Am I steering toward a preferred political outcome? Am I presenting a contested sociological theory as settled? Both are governance-principle violations.
**Effect**: Populated 5-axis state model with assumption register and ≥2 rival interpretations.

### Step 2: Institutional Mapping (F02)
**Precondition**: Populated political state from Step 1.
**Operation**: Map formal rules (constitutions, statutes, procedures) vs informal norms (customs, patronage, unwritten conventions). Track state capacity across 5 dimensions (extractive, coercive, administrative, informational, juridical). Identify accountability channels (horizontal, vertical, diagonal, internal). Apply CPR design principles as empirical regularities, not universal laws. Identify institutional change pathway (drift, layering, conversion, displacement, crisis).
**P1 Gate**: Is only the formal layer being measured? If yes → real governance is misread; informal practice can undermine, bypass, or reshape formal rules. Are identical rules assumed to produce identical outcomes across societies? If yes → path-dependence violation.
**Self-audit**: Did I predict which change pathway dominates from rule text alone? That requires actor configuration and veto-structure analysis, not just rules.
**Effect**: Institutional map with formal/informal layers, capacity dimensions, and change pathway identified.

### Step 3: Network & Collective Action Analysis (F03)
**Precondition**: Institutional map from Step 2.
**Operation**: Compute network quantities (degree, betweenness, clustering, homophily, path length). Distinguish simple vs complex contagion. Identify collective-action problems (free-riding, commitment, credibility, time-inconsistency) and their empirical solutions. Map weak-tie information flow vs strong-tie trust enforcement as complements.
**P1 Gate**: Is the observed network treated as the true social network? If yes → sampling artifacts can invert conclusions; report sampling design. Are power-law degree distributions claimed from sparse data? If yes → frequently overstated.
**Self-audit**: Did I collapse simple and complex contagion into casual "virality"? That distinction predicts opposite effects of network clustering on adoption.
**Effect**: Network structure analysis with contagion type identified and sampling caveats reported.

### Step 4: Cultural Transmission Analysis (F04)
**Precondition**: Network analysis from Step 3.
**Operation**: Analyze culture as shared, learned patterns (meaning, practice, value, artifact). Apply cultural dimension frameworks as coarse country-level averages only. Track cultural change mechanisms (transmission bias, prestige, innovation, migration, institutional change, media). For Vietnamese ritual energy (gia hệ): model as structural metaphors, never as physically measurable quantities. Apply repair-survival condition: CulturalDrift ≤ 0 for continuity. Use ritual proxies (participation rates, expenditure, teaching events) with explicit proxy labeling.
**P1 Gate**: Is a cultural dimension score being used to predict a specific person's behavior? If yes → MODEL scope violation. Is ritual energy presented as an instrumented observable? If yes → epistemic class violation (MODEL, not EMPIRICAL). Is a VN-specific cultural pattern being universalized without cross-cultural evidence? If yes → universalization firewall breach.
**Self-audit**: Am I treating uncalibrated numeric thresholds (e.g., transmission fidelity > 0.6) as empirical constants? They are uncalibrated placeholders.
**Effect**: Cultural analysis with MODEL-class labeling, proxy identification, and universalization firewall enforced.

### Step 5: Conflict & Change Dynamics (F05)
**Precondition**: Cultural analysis from Step 4.
**Operation**: Classify conflict form by opportunity structure, repression costs, and institutional access. Apply bargaining models with incomplete information (delay and breakdown risk). Distinguish escalation mechanisms (security-dilemma spirals, audience costs, sunk-cost entrapment, commitment problems). Separate structural vulnerability (slow variables) from triggers (fast variables). Produce branching outcome scenarios, not point predictions.
**P1 Gate**: Am I producing a point prediction of regime change? If yes → almost never defensible; replace with scenario branching. Am I conflating escalation mechanisms? If yes → each implies different de-escalation levers; conflating produces wrong advice.
**Self-audit**: Did I present platform causation of polarization as settled? The causal weight attributable to online platforms specifically remains COMPETING.
**Effect**: Conflict analysis with mechanism-specific escalation dynamics and branching scenarios.

### Step 6: Ethics & Fairness Gates (F06)
**Precondition**: Conflict scenarios from Step 5.
**Operation**: Apply six fairness gates (BiasAudit, DistributionalHarm, StakeholderRegistry, ExternalityModeler, EthicalConflict, EmergencyPower). Enforce gate precedence: FAIL > CONDITIONAL everywhere. Declare fairness metric choice as a value decision. Check consent lifecycle states; withdrawn consent = absolute block. Apply HIE safety constraints (no panic induction, no coercion, no invalidation of lived experience).
**P1 Gate**: Is a single fairness metric being satisfied while ignoring impossibility results? If yes → metric choice is a value decision and must be declared. Is emergency power active without sunset clause or oversight? If yes → precedence rule blocks.
**Self-audit**: Are UBI biological claims (loop-collapse model, deterministic restoration) being presented as established clinical consensus? They are SOURCE_CLAIM/MODEL-class AMOS constructs.
**Effect**: Fairness gate evaluation with metric declaration, consent status, and HIE safety constraints applied.

### Step 7: Vietnam Regional Grounding (F07)
**Precondition**: Fairness-gated analysis from Step 6 (when VN context is relevant; otherwise skip with justification).
**Operation**: Operate within VN engine stack across 63 provinces and 8 legal domains. Enforce No Legal Advice gate (Vietnamese disclaimer), No Evasion gate, conservative compliance-first bias. Respect physical grounding (North–South logistics, port capacities, urban density) and political mapping (central committee → provincial → district). Apply Sắc-Gọn-Chắc writing calibration for executive Vietnamese output. Map regional differentiation (North/Central/South) as real but averaged — intra-regional variance is substantial.
**P1 Gate**: Is legal advice being given without the mandatory Vietnamese disclaimer? If yes → No Legal Advice gate breach. Is provincial implementation assumed from structural frame alone? If yes → must verify against current sources; C06 provides structure, not live regulatory text.
**Self-audit**: Am I rendering political judgments about VN governance? The engine prohibits political-judgment rendering. Am I treating region-level generalizations as individual predictions? They are averages with substantial intra-regional variance.
**Effect**: VN-grounded analysis with guardrails enforced, physical/political grounding respected, and writing calibration applied.

### Step 8: Data & Measurement Validation (F08)
**Precondition**: VN-grounded (or skipped) analysis from Step 7.
**Operation**: Apply survey error taxonomy (coverage, sampling, nonresponse, measurement, processing). Flag sensitive-topic self-report bias varying by political context. Test measurement invariance before cross-national ranking. Report platform bias in digital trace data (users ≠ populations, algorithmic mediation of visibility). Enforce indicator hygiene: every social indicator must answer what decision changes if it moves.
**P1 Gate**: Are identical survey questions assumed to produce identical constructs across cultures? If yes → measurement invariance must be tested, not assumed. Are digital trace data treated as population-representative? If yes → platform demographic skew and API changes limit external validity.
**Self-audit**: Did I rank countries without testing measurement invariance? Did I use an indicator without decision linkage? Indicators without decision linkage are decoration.
**Effect**: Validated data assessment with error taxonomy, invariance testing, and indicator hygiene enforced.

### Step 9: Scenario & Intervention Design (F09)
**Precondition**: Validated data from Step 8.
**Operation**: Produce scenarios (not forecasts): "if A,B,C hold, then outcome distribution X is modeled." Every political scenario set must contain ≥2 rival readings with discriminating observations. Name intervention mechanism before tool (incentives, information, capability, coordination, norms). Apply unintended-consequences checklist (displacement, adaptation, perverse incentives, elite capture, legitimacy costs, measurement gaming). Require counterfactual reasoning plus mechanism evidence for attribution.
**P1 Gate**: Is the scenario presented as a forecast without justified probabilities? If yes → scenario ≠ forecast. Is before/after comparison used as sole attribution evidence? If yes → insufficient wherever trends were already moving.
**Self-audit**: Are prescriptive statements ("should", "ought", "recommend") explicitly framed as prescription and separated from the descriptive body? If not → normative labeling violation.
**Effect**: Scenario set with ≥2 rival readings, mechanism-first intervention design, and counterfactual attribution.

### Step 10: Meta-Society Integration (F10)
**Precondition**: Scenario set from Step 9.
**Operation**: Apply Alternative-Interpretation Operator: AI(x) = {interpretation_1, ..., interpretation_k}, k ≥ 2, each with mechanism, supporting evidence, discriminating observation. Contract fails if k < 2, if strawman variants, or if no discriminating observation. Model cultural entropy (CulturalDrift = TransmissionDecay − RepairRate). Enforce cross-domain coupling firewalls: environment→society only through specified mediators; mind→society only via aggregation mechanisms. Populate C06 Decision Capsule Template with all required fields.
**P1 Gate**: Is the Alternative-Interpretation Operator satisfied? k < 2 → contract-invalid. Are cross-domain chains claimed without specified mediators? If yes → "climate causes conflict" is invalid; claim form must be "may alter risk through mechanism M." Chain confidence exceeds weakest load-bearing edge? If yes → confidence ceiling violation.
**Self-audit**: Is the Decision Capsule contract-valid? It requires ≥2 alternative interpretations and a discriminating observation. Am I publishing a universal scalar "social health score"? That requires operationalization, weights, uncertainty propagation, and validated thresholds.
**Effect**: Integrated society/culture analysis with AI operator satisfied, cross-domain firewalls enforced, and decision capsule populated.

### Decision Gates (C06-Specific)

| Gate | Check | Failure Action |
|------|-------|---------------|
| **G-AI** | Alternative interpretations ≥2 with discriminating observations | Single-interpretation output → contract-invalid; regenerate |
| **G-UF** | Universalization firewall: no VN-specific claim universalized without cross-cultural evidence | Breach → flag and require cross-cultural evidence |
| **G-DP** | Description vs prescription separated | Prescriptive slippage → rewrite descriptively or explicitly frame |
| **G-ME** | Measurement invariance tested before cross-national ranking | Untested → block ranking |
| **G-CD** | Cross-domain coupling through specified mediators only | Unmediated chain → invalid claim form |


## Consolidated Sub-Skills (17)

This parent skill consolidates the following sub-skills. Each is a section within this domain:


> **Reference**: See `references/marketing_gtm_kernel.md` (content_hash: 71c84689e279640c) for the AMOS Marketing GTM Kernel v0 (marketing go-to-market, GTM strategy, market entry).


> **Reference**: See `references/cci_official_manual.md` (content_hash: c1efa7e2c8c16707) for the Cross-Civilizational Intelligence CCI Official Manual (CCI framework, cross-civilizational analysis, intelligence comparison).


> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: a14c77927348d612) for additional vault-sourced domain knowledge.


> **Reference**: See `references/domain_config.md` (content_hash: 0234c8fc3695eb41) for additional vault-sourced domain knowledge.


> **Reference**: See `references/dignity.md` (content_hash: 3e38bf1a5fd36456) for the Dignity (human dignity, social dignity, dignity frameworks).


> **Reference**: See `references/vn_absolute_architecture.md` (content_hash: b20277d806691d26) for the AMOS Absolute Architecture VN (Vietnamese absolute architecture, full stack, zero gap).


> **Reference**: See `references/vietnam_engines_model.md` (content_hash: d760128f5a0ae9ce) for the AMOS Vietnam Engines Model (Vietnam engines, VN modeling, Vietnamese systems).


> **Reference**: See `references/vietnamese_writing_engine.md` (content_hash: f3f439c0b7047d11) for the AMOS Vietnamese Writing Engine (Vietnamese writing, VN language processing, Vietnamese text).


> **Reference**: See `references/vn_omnistructure_engine.md` (content_hash: 03bbca9003629279) for the AMOS VN Omnistructure Engine (Vietnamese omnistructure, VN systems, omnistructure architecture).


> **Reference**: See `references/vn_omnistructure_clean_engine.md` (content_hash: 966e567a708cbb01) for the AMOS Absolute VN Omnistructure Clean Engine (VN omnistructure, country packs, clean architecture).


> **Reference**: See `references/china_engines_model.md` (content_hash: e633c4ce6d8426e2) for the AMOS China Engines Model (China engines, Chinese systems, country-specific modeling).


> **Reference**: See `references/vietnam_engine_layer.md` (content_hash: 82f367eb4f00e76d) for the AMOS Vietnam Engine Layer (Vietnam engine, VN layer, Vietnamese systems).


> **Reference**: See `references/vietnamese_fractal_logic_analysis.md` (content_hash: 8c52b82137bde62f) for the Vietnamese Fractal Logic Analysis (Vietnamese fractals, VN language fractals, fractal logic).


> **Reference**: See `references/society_culture_engine_cognitive.md` (content_hash: e31bcc62723503da) for the AMOS Society Culture Engine Cognitive (society cognition, cultural cognition, cognitive society).


> **Reference**: See `references/vn_governance_politics_pack.md` (content_hash: baafe13c5c22f7ce) for the AMOS VN Governance and Politics Pack (Vietnamese governance, VN politics, governance pack).


> **Reference**: See `references/cultural_bifurcation_emotion_logic.md` (content_hash: ae6c5b1297e276ae) for the Cultural Bifurcation of Emotion and Logic (cultural bifurcation, emotion vs logic, cultural cognition).


> **Reference**: See `references/humanity_ice_age_to_present.md` (content_hash: 3cbbe9f072fd82ba) for the Humanity from Ice Age to Present (humanity history, ice age, human evolution).


> **Reference**: See `references/when_humanity_began.md` (content_hash: 706e7235788e8937) for the When Humanity Truly Began (humanity origin, human beginning, anthropological).


> **Reference**: See `references/vn_omnistructure_model.md` (content_hash: eade89d6fd662a82) for the VN Omnistructure Model (Vietnamese omnistructure, VN model, society model).


> **Reference**: See `references/vietnamese_writing_model.md` (content_hash: 62b0ed4cb60883d8) for the Vietnamese Writing Model (Vietnamese writing, VN language, writing model).


> **Reference**: See `references/vietnam_environment_report.md` (content_hash: f34c2ed7001d8370) for the Vietnam Environment Report (Vietnam, environment, Vietnamese analysis).


> **Reference**: See `references/vn_marketing_strategy.md` (content_hash: bd81b38e15854f47) for the Vietnamese Marketing Strategy (marketing strategy, Vietnamese, growth).


> **Reference**: See `references/vn_trust_marketplace_strategy.md` (content_hash: 93fc60d40e2e7ba7) for the Vietnam Trust Marketplace Strategy (trust marketplace, Vietnam, strategy).


> **Reference**: See `references/vn_labor_shortage_report.md` (content_hash: ee73008d6132e41d) for the Vietnam Labor Shortage Deep Report (labor shortage, workforce, Vietnamese).

## Validation Gates

- **L0 Integrity**: All cultural frameworks (F01-F10) accounted for; no part silently dropped
- **L1 Epistemic**: Every claim tagged with epistemic class (SOURCE_CLAIM / DERIVED / AMOS_MODEL)
- **L5 Scope**: Analysis confined to declared scope; no scope creep into domain-specific analysis
- **L7 Authority**: No autonomous action beyond authority boundary

## Do not use

- For generic tasks outside c06 domain (social analysis, cultural reasoning, Vietnamese language)
- As a substitute for domain-specific cultural analysis
- For empirical claims about social dynamics without evidence
- Outside the AMOS canon law hierarchy

## References

- See `references/` directory for detailed reference materials
- [[07_SKILLS_MOC]] — Skills map of content

---

**MOC:** references_MOC · [[00_HOME]]
