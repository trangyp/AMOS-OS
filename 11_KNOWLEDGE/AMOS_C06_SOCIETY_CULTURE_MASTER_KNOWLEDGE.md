---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Amos C06 Society Culture Master Knowledge
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

# AMOS C06 — Society & Culture Master Knowledge

> **Epistemic boundary**
>
> This file replaces synthetic micro-module expansions with substantive society-and-culture
> knowledge. It does not claim encyclopedic completeness. Established findings, contested
> sociological theories, model-class abstractions, normative claims, and AMOS/Trang constructs
> are kept separate and typed.
>
> Social analysis is always context-, population-, institution-, and timescale-dependent.
> Contested sociological claims are **COMPETING**-tagged by default. Political analysis must
> remain descriptive unless prescription is explicitly framed. The political-dynamics kernel's
> **alternative_interpretations REQUIRED output rule** applies to all C06 political output:
> an analysis without ≥2 rival readings of the same facts is contract-invalid.

## 0. C06 Knowledge Contract

### 0.1 Claim classes

- **VERIFIED** — strongly supported empirical result within a stated regime.
- **DERIVED** — mathematical or logical consequence of stated premises/model.
- **MODEL** — representation useful within stated scope (includes most AMOS equations).
- **CONDITIONAL** — dependent on explicit assumptions, scenario, or regime.
- **COMPETING** — unresolved alternatives; the default tag for contested sociological theory
  (e.g., drivers of inequality, institutional origins, cultural-evolution mechanisms).
- **UNKNOWN/GAP** — insufficient evidence or unresolved mechanism.

### 0.2 Evidence classes

`OBSERVATION`, `SURVEY`, `ETHNOGRAPHY`, `HISTORICAL_RECORD`, `ADMINISTRATIVE_DATA`,
`EXPERIMENT`, `NETWORK_DATA`, `MODEL`, `SCENARIO`, `SOURCE_CLAIM`, `UNKNOWN`.

### 0.3 C06 H-level ownership

1. Political Dynamics, Power & Conflict
1. Institutions & Governance Structures
1. Social Networks & Collective Action
1. Culture, Ritual & Cultural Transmission
1. Social Change, Stability & Regime Dynamics
1. Ethics, Fairness, Consent & Human Interaction
1. Vietnam Regional Society Systems
1. Monitoring, Data & Social Measurement
1. Scenarios, Policy & Intervention Design
1. AMOS/Trang Society Research Bridge

A topic has one primary owner. Cross-links are references, not duplicated substantive sections.

### 0.4 Standard knowledge node schema

Where applicable:
**definition → state variables → governing relations → assumptions → mechanisms → observables →
data sources → empirical status → scope/regime → uncertainty → failure modes → competing models →
falsifiers → dependencies → decision relevance → AMOS bridge**.

______________________________________________________________________

## H1 — Political Dynamics, Power & Conflict

## M1. Political Dynamics Kernel v0

### L1. Kernel identity

Source engine: `Human_Society.Political_Dynamics` (kernel v1.0.0).
Seven scopes:

- power_and_institutions;
- political_conflict_and_cooperation;
- political_strategy;
- regime_and_system_dynamics;
- policy_and_interest_dynamics;
- change_and_stability;
- international_and_multi_actor_politics.

### L2. State model (5 axes)

Before any analysis, populate:
`political_system_context · actors_and_interests · institutions_and_rules · power_and_conflict · change_and_stability`

An axis left unpopulated is an unstated assumption.

### L3. Governance principles (4)

1. **state_assumptions** — every analysis carries its assumption register.
1. **avoid_bias_toward_particular_outcomes** — no steering toward preferred conclusions.
1. **distinguish_description_from_prescription** — describe what is; prescribe nothing without
   explicit framing.
1. **respect_multiplicity_of_perspectives** — alternative interpretations are REQUIRED output,
   not optional.

### L4. I/O contract

Inputs — required: `political_question_or_scenario`, `context`; optional:
actors_and_positions, institutional_details, historical_context, constraints,
framework_preferences.

Outputs — required: `political_analysis`, `relevant_factors`,
`assumption_and_limitations`, **`alternative_interpretations`**.

**Contract rule:** an output missing `alternative_interpretations` is contract-invalid. This is
the anti-bias mechanism made structural, not stylistic preference.

### L5. Decision gates

1. Single-interpretation output? → contract-invalid; regenerate with ≥2 rival readings.
1. Prescriptive slippage without framing? → rewrite descriptively.
1. Assumptions unstated? → block until assumption register exists.

### L6. Worked example

Question: why is a coalition unstable?
Axis setup maps actors/institutions. Two rival readings generated and BOTH presented:
(a) substantive policy disagreement among members; (b) leadership contest masked as policy
dispute. Neither is privileged without additional discriminating evidence.

______________________________________________________________________

## M2. Power

### L1. Definitions (plural, must be labeled)

Common analytical senses:

- power as capacity to achieve outcomes;
- power as control over agenda-setting;
- power as shaping preferences/perception itself.

These are distinct constructs; analyses that silently switch between them conflate different
mechanisms. **Class:** COMPETING across traditions (behavioral vs structural vs discursive).

### L2. Sources of power

Typical bases include:

- coercive capacity;
- economic resources;
- legitimacy/authority;
- information and expertise;
- network position (brokerage, centrality);
- institutional rule-control;
- popular mobilization capacity.

### L3. Legitimacy

Legitimation can rest on procedure, tradition, charisma, performance, ideology, or some mix.
Legitimacy is audience-relative: a regime legitimate to one constituency may not be to another.
Claims about a polity's "true" legitimacy require specifying the judging population.

### L4. Power asymmetry measurement

Asymmetry is measurable through veto points, resource shares, agenda control, and exit options —
but each measure captures a different face of power. No single scalar captures power fully.

______________________________________________________________________

## M3. Political Conflict and Cooperation

### L1. Conflict forms

Forms include electoral competition, protest, litigation, bargaining, low-intensity violence,
civil war, and international rivalry. Form choice depends on opportunity structure, repression
costs, and institutional access.

### L2. Cooperation problems

Political cooperation faces collective-action problems: free riding, commitment problems,
credibility of promises, and time-inconsistency. Solutions observed empirically include repeated
interaction, enforcement institutions, side-payments, and focal norms.

### L3. Bargaining models

Bargaining outcomes depend on reservation values, patience, outside options, information, and
commitment technology. Incomplete-information bargaining predicts delay and breakdown risk that
complete-information models miss.

### L4. Escalation dynamics

Escalation is often driven by:

- security-dilemma spirals under mistrust;
- audience costs constraining backing down;
- sunk-cost entrapment;
- commitment problems over shifting power.

Each mechanism implies different de-escalation levers; conflating them produces wrong advice.

______________________________________________________________________

## H2 — Institutions & Governance Structures

## M1. Institutions

### L1. Definition

Institutions are the formal rules and informal norms that structure repeated social interaction.
They constrain and enable action; they are both constraints on and products of power (**class:
COMPETING between rule-centered and power-centered views of institutional origin**).

### L2. Formal vs informal

Formal institutions: constitutions, statutes, procedures, courts, parties.
Informal institutions: norms, customs, patronage networks, unwritten conventions.
Formal rules can be undermined, bypassed, or reshaped by informal practice; measuring only the
formal layer misreads real governance.

### L3. Institutional effects

Institutions shape transaction costs, credible commitment, property expectations, conflict-
resolution channels, and distribution. Effects are path-dependent and context-bound; identical
rules transplanted into different societies frequently produce divergent outcomes.

### L4. Institutional change

Change pathways include gradual drift, layering, conversion, displacement, and crisis-driven
redesign. Predicting which pathway dominates in a given case requires actor configuration and
veto-structure analysis, not just rule text.

______________________________________________________________________

## M2. State Capacity and Governance Quality

### L1. Capacity dimensions

- extractive capacity (taxation);
- coercive capacity (monopoly of legitimate force, in principle);
- administrative/implementation capacity;
- informational capacity (statistics, registries, surveillance);
- juridical capacity (consistent adjudication).

### L2. Governance quality indicators

Candidate indicators: rule consistency, corruption measures, service delivery, contract
enforcement, budget transparency, grievance channels. All indicators have known measurement
error and cultural response biases (especially survey-based corruption scores).

### L3. Accountability

Accountability operates through horizontal (other state branches), vertical (electorates),
diagonal/societal (media, civil society), and internal-audit channels. Weakening one channel
shifts load onto others; total accountability capacity is what matters for governance risk.

### L4. Polycentric governance

Multiple centers of authority can increase adaptability and redundancy but also create
coordination failures and jurisdictional conflicts — the same trade-off documented in common-pool
resource governance applies to general political authority.

______________________________________________________________________

## M3. Common-Pool Resources and Collective Governance

### L1. CPR structure

Common-pool resources (fisheries, forests, aquifers, grazing lands) combine subtractability with
difficulty of exclusion, generating overuse pressure absent governance.

### L2. Design principles

Long-studied successful CPR arrangements tend to feature: clear boundaries, locally adapted
rules, participation in rule-making, monitoring, graduated sanctions, accessible conflict
resolution, and nested tiers. These are empirical regularities, not universal laws; failures
exist even where design boxes are checked.

**Class:** VERIFIED as robust empirical patterns within studied regimes; COMPETING on the general
theory of when they transfer.

______________________________________________________________________

## H3 — Social Networks & Collective Action

## M1. Network Structure

### L1. Basic quantities

For graph `G = (V, E)`:

- degree centrality `k_i`;
- betweenness centrality (brokerage);
- clustering coefficient (local density);
- average path length;
- homophily (assortative tie formation).

### L2. Small-world structure

Many real social networks show high local clustering with short average path lengths. This is a
well-replicated structural regularity, though degree distributions vary widely across contexts
(power-law claims are frequently overstated from sparse data).

### L3. Weak ties and brokerage

Weak ties often carry novel information across group boundaries; brokers spanning structural
holes gain advantage. Strong ties dominate trust and enforcement functions. Both roles matter;
they are complements, not rivals.

### L4. Network data caveats

Observed networks are samples of true social relations. Missing ties, recall bias, and platform-
specific artifacts can invert conclusions. Network inference should report sampling design.

______________________________________________________________________

## M2. Diffusion and Contagion

### L1. Diffusion processes

Adoption/diffusion models include simple contagion, complex contagion (adoption requiring
multiple reinforcing signals), threshold models, and seeding strategies. Complex contagion
predicts clustered networks aid adoption of costly or controversial behaviors where simple
contagion does not — a distinction frequently collapsed in casual "virality" claims.

### L2. Cascades

Cascade size and probability depend on network topology, seed selection, threshold distribution,
and timing. Most cascades remain small; predictability of which specific content cascades is
limited (**class:** VERIFIED limits on prediction; MODEL for cascade mechanics).

### L3. Echo chambers and polarization

Exposure to like-minded content can reinforce polarization, but measured polarization trends
also reflect sorting, elite cues, and offline factors. The causal weight attributable to online
platforms specifically remains contested.

**Class:** COMPETING — do not present platform causation of polarization as settled.

______________________________________________________________________

## M3. Collective Action

### L1. Core problem

Rational individuals may free ride on collective goods (Olson). Mobilization therefore requires
selective incentives, identity, moral commitments, social pressure, coordination structures, or
repeated-game reputation — pure altruism alone rarely sustains large-scale action.

### L2. Movements

Social movements typically require: grievances, resources, political opportunities, and framing
that resonates. Movement success is usually defined against specific goals and windows; broad
"movements work/movements fail" claims ignore goal heterogeneity.

### L3. Trust and social capital

Trust and associational density correlate with cooperation and governance outcomes across many
studies, but causal direction (trust ↔ institutions) runs both ways and remains unresolved at
the macro level.

**Class:** CORRELATION VERIFIED / CAUSAL DIRECTION COMPETING.

______________________________________________________________________

## H4 — Culture, Ritual & Cultural Transmission

## M1. Culture

### L1. Working definition

Culture: shared, learned patterns of meaning, practice, value, and artifact transmitted across
generations. It is analytically separable from biology and from individual preference.

### L2. Cultural dimensions caution

Cross-national dimension frameworks (e.g., individualism-collectivism, power distance) are
useful coarse descriptors of country-level averages but: (a) describe central tendencies, not
individuals; (b) are snapshot measures of dynamic systems; (c) should never be used to predict a
specific person's behavior.

**Class:** MODEL with explicit scope limits.

### L3. Cultural change

Mechanisms include transmission bias (conformity, prestige), innovation, migration/contact,
institutional change, media environments, and economic restructuring. Cultural traits persist
when transmission fidelity exceeds decay/attrition — the same repair-vs-entropy logic AMOS uses
below.

______________________________________________________________________

## M2. Vietnamese Cultural Ritual Energy (gia hệ)

### L1. Source scope

Source skill: `amos-vn-cultural-ritual-energy-10000`. It contains ~10,000 equation records
modeling lineage ritual energy across three time layers, seven regions, and eight civilizational
lenses.

**Epistemic class:** MODEL throughout. The source itself declares these are structural metaphor
equations for cultural energy patterns; they are NOT physically measurable quantities. C06 must
never present `ritual energy`, `lineage energy`, etc., as instrumented observables.

### L2. Three time layers

1. **Đông Sơn** (~500 BCE–100 CE): foundational ritual patterns, bronze drum resonance,
   agricultural-cycle rituals, ancestor worship origination.
1. **Lý-Trần** (11th–14th c.): Buddhist-influenced ritual energy, court rituals, village đình
   communal-house energy, filial piety institutionalization.
1. **Đổi Mới** (1986–present): ritual under market economy, diaspora continuity, digital ritual
   adaptation, transmission under globalization.

Historical characterizations here are SOURCE_CLAIM-level interpretive frames, not verified
historiography per element.

### L3. Seven regions

Red River Delta; Mekong Delta; Central Coast; Northern Mountains; Central Highlands; Southeast;
Diaspora (hải ngoại).

### L4. Eight civilizational lenses

Agricultural cycle energy; ancestor ritual energy; marriage alliance energy; household boundary
energy; filial piety energy; cultural transmission energy; ritual continuity energy; lineage
survival energy.

### L5. Core representative equations

```
LE(t) = Σ(ritual_energy_i(t)) × transmission_efficiency × cultural_coherence
RE    = offering_value × sincerity_index × ritual_correctness × ancestral_resonance
HBE   = boundary_strength × internal_coherence × external_pressure_resistance
CT    = parent_energy × child_receptivity × cultural_medium_strength × time_decay
Cultural_E = -(1/ln N) Σ p_i ln p_i     (normalized diversity entropy)
```

All terms except the Shannon-form entropy expression are latent constructs without independent
measurement protocols. Use for organizing qualitative analysis and scenario comparison only.

### L6. Repair-survival condition

```
RitualRepairRate > CulturalEntropyAccumulationRate → lineage survives
```

This encodes the general claim that cultural continuity requires maintenance exceeding decay.
The threshold form is a heuristic; no calibrated rate estimates exist.

### L7. Invariants (as stated by source)

1. Lineage Continuity: ritual energy must not stay below threshold more than 3 generations.
1. Filial Piety Conservation: transforms across generations rather than vanishing.
1. Household Boundary Integrity: boundary energy must exceed external pressure for survival.
1. Transmission Fidelity > 0.6 for continuity.
1. Ritual Correctness Preservation: form may evolve; core structure preserved.

**Class:** MODEL / design invariants for simulation, not empirical constants. The numeric
thresholds (e.g., 0.6) are uncalibrated placeholders.

______________________________________________________________________

## M3. Ritual Function

### L1. Functions documented cross-culturally

Ritual commonly serves: social bonding and synchrony, marking life transitions, transmitting
norms to new generations, managing uncertainty, legitimating authority, and memorializing
collective identity. Multiple functions coexist in one practice.

### L2. Ritual persistence

Rituals persist when they retain perceived efficacy and social payoff, and mutate when cost
exceeds benefit or carriers disappear. Diaspora adaptation (compressed forms, digital
participation) illustrates form-flexibility with function-retention.

### L3. Measurement honesty

Ritual "strength" proxies available empirically: participation rates, expenditure, inter-
generational teaching events, language use, site maintenance. Proxy ≠ essence; report which
proxy was used.

______________________________________________________________________

## H5 — Social Change, Stability & Regime Dynamics

## M1. Change and Stability

### L1. Stability sources

Regime/system stability draws on coercion, legitimation, co-optation, performance delivery,
institutionalized participation channels, elite cohesion, and external support. Stability is
multi-causal; single-factor stability predictions routinely fail.

### L2. Change triggers

Documented trigger classes: elite splits, fiscal stress, lost wars, urbanization/demographic
pressure, economic shocks, information shocks, succession crises. Triggers interact with
structural vulnerability; a trigger without pre-existing weakness rarely produces systemic change.

### L3. Path dependence

Early institutional choices constrain later option sets through increasing returns and network
effects. History matters, but path dependence is not determinism — critical junctures reopen
choice sets.

### L4. Prediction discipline

C06 must distinguish:

- structural vulnerability assessment (slow variables);
- trigger identification (fast variables);
- outcome scenarios (branching, conditional);
- point predictions of regime change (almost never defensible).

Forecasting specific regime collapse dates is outside C06's honest capability.

______________________________________________________________________

## M2. Regime Typologies

### L1. Spectrum

Democracy ↔ hybrid regime ↔ authoritarianism is a spectrum along multiple dimensions
(participation, contestation, civil liberties, accountability), not a single axis. Composite
regime indices embed weighting judgments that should be surfaced, not hidden.

### L2. Authoritarian resilience

Authoritarian durability mechanisms include party institutionalization, performance legitimacy,
selective repression, controlled representation, and information management. Durability varies
enormously; typology-level averages hide this variance.

### L3. Democratization

Transitions are shaped by elite pacts, mass mobilization, external pressure, economic
development, and prior institutional legacies. Consolidation is a separate, harder problem than
transition. Competing grand theories of democratization drivers remain unresolved.

**Class:** descriptive regularities VERIFIED; unified causal theory COMPETING.

______________________________________________________________________

## M3. Migration and Demographic Change

### L1. Migration drivers

Migration arises from wage/livelihood differentials, networks lowering move costs, conflict/
persecution, climate/environmental stress, and policy regimes — mediated by household strategy
and information. Environmental stress contributes through livelihood channels; it rarely acts
alone (same causal firewall as C12).

### L2. Integration

Integration outcomes depend on legal status, labor-market access, language, discrimination,
networks, and receiving-society institutions. Assimilation vs multiculturalism outcomes are
context-dependent and partly normative framings.

### L3. Urbanization

Urbanization restructures kinship, labor, and political participation. Cities concentrate both
opportunity and grievance; their net effect on stability is regime- and policy-dependent.

______________________________________________________________________

## H6 — Ethics, Fairness, Consent & Human Interaction

## M1. Fairness Governance Gates (Gaps 274–279)

### L1. Six gates

From `amos-human-social-systems` / `amos-fairness-ethics`:

- BiasAuditChecker (gap 274): demographic parity, equalized odds, disparate impact, calibration…
- DistributionalHarmChecker (gap 275): allocation/quality/representational/dignitary harm.
- StakeholderRegistry (gap 276): primary/secondary/tertiary/marginalized/adversary.
- ExternalityModeler (gap 277): positive/negative × direct/indirect/cumulative/systemic.
- EthicalConflictChecker (gap 278): competing values/duty/rights/principle conflicts.
- EmergencyPowerGovernor (gap 279): status + sunset clause + oversight.

### L2. Gate precedence rules

FAIL takes precedence over CONDITIONAL everywhere. Emergency-power precedence:
`abuse_detected > no-sunset-clause > no-oversight > active(CONDITIONAL)`.
Any FAIL blocks emergency action.

### L3. Fairness metric plurality

No single fairness metric can be satisfied simultaneously in general (known impossibility
results among parity-type criteria under unequal base rates). Metric choice is a value decision
and must be declared.

**Class:** DERIVED impossibility results VERIFIED within their assumptions; metric choice NORMATIVE.

______________________________________________________________________

## M2. Consent and Privacy Governance (Gaps 258–269)

### L1. Twelve gates

ConsentLifecycleManager (258), PurposeLimitationEnforcer (259), DataMinimizationEngine (260),
RightToDeleteManager (261), DeletionAuditResolver (262), DataResidencyManager (263),
JurisdictionEngine (264), CompliancePolicyCompiler (265), RegulatoryChangeMonitor (266),
LicensingIPTracker (267), DerivativeWorkTracker (268), ExportControlChecker (269).

### L2. Hard blocking rules

- Withdrawn consent (258 FAIL) → no further processing permitted.
- Purpose violation (259 FAIL) → immediate processing block.
- Unapproved cross-border transfer (263 FAIL) → data egress blocked.
  These are absolute gates, not scored trade-offs.

### L3. Consent lifecycle states

`PENDING → GRANTED → WITHDRAWN | EXPIRED`; expired consent is CONDITIONAL, withdrawn is FAIL.

______________________________________________________________________

## M3. Human Interaction Engine (HIE)

### L1. Seven internal state layers

L1 surface text → L2 emotional state → L3 nervous system regulation → L4 cognitive state →
L5 identity state → L6 context state → L7 wider system state.

### L2. Nine-step pipeline

parse → update state → select goal → select strategy → select content → safety/ethics filter →
select channel/intensity → realize in language → evaluate and tag for learning.

### L3. Safety constraints (absolute)

Never deliberately induce panic/collapse; never manipulate/coerce; never invalidate lived
experience; never overpromise; always mark uncertainty; prefer nervous-system safety over speed.

### L4. Scope note

The UBI biological claims embedded in the human-living-systems sources (loop-collapse model of
distress, deterministic restoration) are SOURCE_CLAIM/MODEL-class constructs of the AMOS corpus,
not established clinical consensus. C06 carries them as framework assumptions with that label.

______________________________________________________________________

## H7 — Vietnam Regional Society Systems

## M1. Structural Layers

### L1. Engine stack

Unipower VN comprises three engines: `AMOS_VN_Legal_Engine`, `ABSOLUTE_VN_OMNISTRUCTURE`,
`VN_Legal_Engine_vInfinity`, covering 8 legal domains (Enterprise, Investment, Land, Labor,
Environment, Cybersecurity/Data, EV/Mobility, Tax) across 63 provinces, with 12 omnistructure
dimensions mapped to 19 primitive systems.

### L2. Omnistructure grounding directives

- Physical grounding: do not invent locations, infrastructure, or logistics; respect defined
  geographic constraints (North–South logistics, port capacities, urban density).
- Political mapping: recognize structured power flow from central committee levels down through
  provincial and district administration.
- Economic corridors: operate within existing/planned economic zones and grid constraints.
- Integration base: invoked beneath legal and mobility engines for physical/political viability.

### L3. Mandatory guardrails (Vietnam engine)

- **No Legal Advice gate**: mandatory Vietnamese disclaimer ("Đây không phải là tư vấn pháp
  lý…"); structural mapping only.
- **No Evasion gate**: no tax evasion, beneficial-ownership hiding, or AML/KYC circumvention.
- **Conservative bias**: compliance-first pathway whenever regulatory interpretations diverge.
- **Output contract**: LEGAL_INPUT_RESOLVED → DOMAIN_AND_LAYER_MAP → PROVINCE_AND_REGULATOR_MAP
  → REGULATORY_FRAMEWORK → RISK_AND_ENFORCEMENT_ANALYSIS → COMPLIANCE_ARCHITECTURE →
  SCENARIOS_AND_PATHWAYS → DISCLAIMER.

### L4. Provincial variation caveat

The 63-province coverage is a structural frame. Actual provincial implementation, enforcement,
and incentive environments vary and must be verified against current sources before operational
use; C06 provides structure, not live regulatory text.

______________________________________________________________________

## M2. Vietnamese Society and Culture Context

### L1. Family and lineage structure

Vietnamese society historically organizes strong family/lineage obligations, ancestor veneration,
filial piety, and household boundaries — the substrate modeled by the gia hệ skill (H4-M2).
Contemporary urbanization, migration, and market economy reshape but do not erase these patterns;
Đổi Mới-era adaptations are the active regime.

### L2. Regional differentiation

North/Central/South differences in history, economy, dialect, and institutional experience are
real and consequential for operations and communication. Region-level generalizations remain
averages; intra-regional variance is substantial.

### L3. Communal institutions

Village communal houses (đình), religious pluralism (Buddhist, Confucian, Taoist, folk, Catholic,
Protestant, indigenous highland traditions), and festival calendars constitute the communal
institutional fabric referenced by ritual-energy modeling.

### L4. Communication norms (engine-encoded)

Executive Vietnamese writing follows Sắc-Gọn-Chắc (sharp–concise–solid) tone calibration:
no vague qualifiers ("tương đối", "khá", "có vẻ"), numbers over adjectives, 40% diagnosis /
40% solution / 20% recommendation structure, documents opening with "Tài liệu này nhằm giải
quyết vấn đề gì?". This is an AMOS house style, not a description of all Vietnamese discourse.

______________________________________________________________________

## M3. Regional Engine Layer (comparative)

### L1. Six comparative layers

Australia, China, Singapore, US, UK, EU engines provide structural mapping with time horizons
short (0–2y), medium (3–7y), long (8–30y).

### L2. China layer specifics

32 dimensions × 12 axes structural model; cross-border mode for sanctions/data-transfer
questions; mandatory recommendation of licensed local counsel; no political-judgment rendering.

### L3. Policy & Geostrategy engine

20 clusters (political stability, economic dependencies, military posture, alliances, sanctions…)
× virtual expansion axes (Policy Domain × Time Horizon × Level) × 4 lens views
(Exec / Operator / Expert / Audit). Ethical constraint: no advocacy of human-rights violations;
no incitement of conflict or violence.

______________________________________________________________________

## H8 — Monitoring, Data & Social Measurement

## M1. Survey and Administrative Data

### L1. Survey error taxonomy

Coverage error, sampling error, nonresponse error, measurement error (question wording, social
desirability, translation), processing error. Sensitive-topic self-reports (corruption,
discrimination, trust in authorities) carry systematic bias that varies by political context.

### L2. Administrative data caveats

Official statistics reflect reporting incentives and classification changes. Series breaks
(e.g., administrative reforms) require reconciliation before trend inference.

### L3. Cross-national comparability

Identical questions do not produce identical constructs across languages and cultures.
Measurement invariance should be tested, not assumed, before ranking countries.

______________________________________________________________________

## M2. Network and Digital Trace Data

### L1. Platform bias

Digital trace data represent platform users, not populations. Demographic skew, algorithmic
mediation of visibility, and API access changes limit external validity.

### L2. Ethics of trace data

Collection and reuse of social trace data must pass the consent gates (H6-M2): purpose
limitation, minimization, jurisdiction checks apply even to "public" posts in most frameworks.

### L3. Indicator hygiene

Every social indicator answers: *what decision changes if this variable moves?* Indicators
without decision linkage are decoration.

______________________________________________________________________

## H9 — Scenarios, Policy & Intervention Design

## M1. Scenario Discipline

### L1. Scenario vs forecast

`if assumptions A,B,C hold, then outcome distribution X is modeled` — a scenario is not a
forecast absent justified probabilities.

### L2. Multi-perspective requirement

Because the political-dynamics kernel mandates alternative interpretations, every C06 political
scenario set must contain at least two rival readings of the same underlying facts, with
discriminating observations named for choosing between them later.

### L3. Normative labeling

Any prescriptive statement ("should", "ought", "recommend") must be explicitly framed as
prescription, separated from the descriptive body.

______________________________________________________________________

## M2. Intervention Design

### L1. Mechanism-first

Interventions succeed through specified mechanisms (incentives, information, capability,
coordination, norms). Name the mechanism before the tool; otherwise evaluation cannot attribute
effects.

### L2. Unintended consequences checklist

- displacement of activity to unregulated arenas;
- strengthening the target's adaptation;
- perverse incentives;
- elite capture of benefits;
- legitimacy costs of enforcement;
- measurement gaming.

### L3. Evaluation standards

Attribution requires counterfactual reasoning (experimental or quasi-experimental where feasible)
plus mechanism evidence. Before/after comparisons alone are insufficient wherever trends were
already moving.

______________________________________________________________________

## H10 — AMOS/Trang Society Research Bridge

## M1. Source Family Integration

The C06 sources identify ten families:

1. political dynamics and power;
1. institutions and governance;
1. social networks and collective action;
1. culture, ritual, transmission;
1. conflict, cooperation, change;
1. ethics/fairness/consent;
1. Vietnam regional systems;
1. social data/monitoring;
1. scenarios/policy/intervention;
1. meta-society research bridge.

This file preserves those functions while replacing placeholder micro-modules with typed,
bounded knowledge.

______________________________________________________________________

## M2. HML Mapping for Society

### L1. H layer

Examples: regime trajectories; institutional viability; cultural continuity across generations;
social-cohesion horizons.

### L2. M layer

Examples: parties/bureaucracies/courts; movement organizations; firms and unions; media systems;
lineage/household institutions.

### L3. L layer

Examples: a vote, a bribe, a ritual offering, a tie formation, a permit approval, a household
boundary negotiation.

HML is an AMOS reasoning structure, not a claim that society has exactly three ontological levels.

______________________________________________________________________

## M3. RSCF Society Mapping

Domain-specific RSCF encoding may use:

- **State** — actor positions, institutional configurations, cultural variables;
- **Constraint** — legal rules, resource bounds, legitimacy requirements, consent gates;
- **Feedback** — legitimacy↔performance loops, repression↔mobilization spirals, trust dynamics;
- **Repair** — institutional reform, truth/reconciliation processes, ritual renewal, gate resets.

A valid RSCF mapping preserves actual social science; generic labels must not replace mechanism.

______________________________________________________________________

## M4. Alternative-Interpretation Operator

The political kernel's required-output rule generalizes as an operator:

```text
AI(x) = {interpretation_1, ..., interpretation_k}, k ≥ 2
each interpretation_i carries: mechanism, supporting evidence, discriminating observation
```

Contract validity fails if k < 2, if interpretations are strawman variants of one thesis, or if
no discriminating observation is identified. This is C06's structural anti-bias device.

**Class:** MODEL (analysis-governance rule).

______________________________________________________________________

## M5. Cultural Entropy Operator

Proposed abstraction:

```text
CulturalDrift = TransmissionDecay − RepairRate(RitualRenewal, Teaching, InstitutionalSupport)
LineageContinuity ⟺ CulturalDrift ≤ 0 sustained
```

**Class:** MODEL. Useful for organizing continuity risk discussion; not a measured quantity.
Mathematical neighbors: population transmission models (cultural evolution), Markov chain
absorption, reliability maintenance theory.

______________________________________________________________________

## M6. Society Viability Function

Conceptual form:
`V_soc = f(institutional trust, conflict-resolution capacity, cultural coherence, economic inclusion, voice/accountability, future options)`.

**Class:** MODEL. Same usage discipline as C12's viability function: organize trade-offs; never
publish a universal scalar "social health score" without operationalization, weights, uncertainty
propagation, and validated thresholds.

______________________________________________________________________

## M7. Cross-Domain Coupling Firewalls

### L1. Environment→Society chain

Environmental stress affects society only through specified mediators (livelihoods, prices,
displacement, governance). Claim form: "may alter risk through mechanism M", never "climate
causes conflict". Ownership: Earth-side facts belong to C12; mediation analysis is joint.

### L2. Mind↔Society chain

Individual psychological states [CC05] aggregate to collective behavior only via specified
aggregation mechanisms (networks, institutions, thresholds). C06 owns the aggregation layer;
CC05 owns individual-layer constructs.

### L3. Confidence rule

Chain confidence cannot exceed the weakest load-bearing edge without independent revalidation.

```yaml
cross_domain_refs:
  - id: AMOS_CC05_mind_behavior
    relation: mind_to_collective_aggregation
    direction: bidirectional
    ownership_rule: preserve_domain_boundaries
    causal_status: mediated_not_assumed
  - id: AMOS_C12_EARTH_ECOLOGY
    relation: environment_to_society_coupling
    direction: bidirectional
    ownership_rule: preserve_domain_boundaries
    causal_status: mediated_not_assumed
    confidence_rule: weakest_load_bearing_edge
```

______________________________________________________________________

## M8. Monitoring-to-Decision Loop (Society Form)

```text
observe (surveys/admin/network data)
→ validate (error taxonomy check)
→ compare against models/thresholds
→ update state estimate
→ test competing explanations (≥2 rival readings — kernel-mandated)
→ identify decision-changing uncertainty
→ choose reversible action where possible
→ monitor outcome
→ revise
```

This is the correct operational form of C06, replacing static registry expansion.

______________________________________________________________________

## C06 Master Dependency Spine

```text
individuals + households + interaction rules
            ↓
social networks + trust + norms
            ↓
culture + ritual + transmission systems
            ↓
institutions + governance + state capacity
            ↓
political power + conflict + cooperation
            ↓
change / stability / regime dynamics
            ↓
ethics + fairness + consent gates
            ↓
monitoring + social measurement
            ↓
scenarios + policy + intervention design
            ↓
AMOS cross-scale decision architecture
```

## C06 Decision Capsule Template

```text
System:
Boundary (polity/community/institution):
Location:
Timescale:
Decision:
Irreversibility:
Actors and interests:
Institutional rules (formal + informal):
Power configuration:
Conflict lines:
Cultural context:
Network structure (if relevant):
Data sources:
Data freshness:
Known measurement biases:
Scenario assumptions:
Alternative interpretation 1:
Alternative interpretation 2:
Discriminating observation(s):
Prescriptive elements (explicitly framed):
Decision-sensitive uncertainty:
Least-regret actions:
Triggers for escalation:
Monitoring plan:
Falsifiers:
Revalidation date:
```

Note: the capsule is contract-valid only when at least two alternative interpretations and a
discriminating observation are filled — mirroring the kernel's required-output rule.

## C06 Promotion Rule

A new society/culture claim may move from `MODEL` toward stronger status only when:

1. terms and population/boundary are operationally defined;
1. spatial, temporal, and unit-of-analysis scales are explicit;
1. data provenance and known measurement biases are documented;
1. scenario assumptions are separated from observations;
1. competing explanations are considered (≥2 rival readings for political claims);
1. causal claims identify mechanism and confounders;
1. contested sociological theory is tagged COMPETING, never presented as settled;
1. normative prescriptions are explicitly framed and separated from description;
1. irreversible recommendations undergo stronger validation;
1. governance records contradiction, supersession, and revalidation.

## C06 Final Boundary

C06 is not a society oracle and holds no political position.

Its purpose is a disciplined, cross-scale map of social and cultural dynamics that connects
power, institutions, networks, culture, ethics, and regional specificity without silently
flattening their differences — and that refuses single-interpretation political analysis by
construction.

The architecture remains open and repairable:
**integrity > completeness > fluency > speed**.

______________________________________________________________________

[[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] · [[00_ROOT/AMOS MOC|AMOS MOC]]

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

______________________________________________________________________

RSCF-NODE
node_id: amos_c06_society_culture_master_knowledge
node_type: note
path: 11_KNOWLEDGE/AMOS_C06_SOCIETY_CULTURE_MASTER_KNOWLEDGE.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
  claim_class: AMOS_MODEL

______________________________________________________________________

**MOC:** [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]]
