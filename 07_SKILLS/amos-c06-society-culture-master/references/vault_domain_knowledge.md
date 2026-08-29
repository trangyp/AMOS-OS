---
title: Vault Domain Knowledge — Amos C06 Society Culture Master
type: reference
source: 07_SKILLS/amos-c06-society-culture-master/references
tags:
- reference
- amos-c06-society-culture-master
- type/skill
- skill
- references-moc
- 07-skills-moc
- 00-home
- amos-rscf-nodes
- law-hierarchy
- trang-framework-recursive-ontology-dynamics
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---

# amos-c06-society-culture-master — Vault-Sourced Domain Knowledge

> Load this reference only when detailed domain knowledge is needed.
> This content was moved from SKILL.md for progressive loading.

---

> **Source**: `11_KNOWLEDGE/AMOS_C06_SOCIETY_CULTURE_MASTER_KNOWLEDGE.md` from the AMOS_OS Obsidian vault.
> This is substantive domain knowledge, not script-generated content.

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
2. Institutions & Governance Structures
3. Social Networks & Collective Action
4. Culture, Ritual & Cultural Transmission
5. Social Change, Stability & Regime Dynamics
6. Ethics, Fairness, Consent & Human Interaction
7. Vietnam Regional Society Systems
8. Monitoring, Data & Social Measurement
9. Scenarios, Policy & Intervention Design
10. AMOS/Trang Society Research Bridge

A topic has one primary owner. Cross-links are references, not duplicated substantive sections.

### 0.4 Standard knowledge node schema
Where applicable:
**definition → state variables → governing relations → assumptions → mechanisms → observables →
data sources → empirical status → scope/regime → uncertainty → failure modes → competing models →
falsifiers → dependencies → decision relevance → AMOS bridge**.

---

# H1 — Political Dynamics, Power & Conflict

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
2. **avoid_bias_toward_particular_outcomes** — no steering toward preferred conclusions.
3. **distinguish_description_from_prescription** — describe what is; prescribe nothing without
   explicit framing.
4. **respect_multiplicity_of_perspectives** — alternative interpretations are REQUIRED output,
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
2. Prescriptive slippage without framing? → rewrite descriptively.
3. Assumptions unstated? → block until assumption register exists.

### L6. Worked example
Question: why is a coalition unstable?
Axis setup maps actors/institutions. Two rival readings generated and BOTH presented:
(a) substantive policy disagreement among members; (b) leadership contest masked as policy
dispute. Neither is privileged without additional discriminating evidence.

---

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

---

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

---

# H2 — Institutions & Governance Structures

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

---

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

---

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

---

# H3 — Social Networks & Collective Action

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

---

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

---

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

---

# H4 — Culture, Ritual & Cultural Transmission

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

---

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
2. **Lý-Trần** (11th–14th c.): Buddhist-influenced ritual energy, court rituals, village đình
   communal-house energy, filial


## Vault-Sourced Domain Content

> Source: `11_KNOWLEDGE/AMOS_C06_SOCIETY_CULTURE_MASTER_KNOWLEDGE.md` (40086 bytes in vault)

### 0.1 Claim Classes

- **VERIFIED** — strongly supported empirical result within a stated regime.
- **DERIVED** — mathematical or logical consequence of stated premises/model.
- **MODEL** — representation useful within stated scope (includes most AMOS equations).
- **CONDITIONAL** — dependent on explicit assumptions, scenario, or regime.
- **COMPETING** — unresolved alternatives; the default tag for contested sociological theory
  (e.g., drivers of inequality, institutional origins, cultural-evolution mechanisms).
- **UNKNOWN/GAP** — insufficient evidence or unresolved mechanism.

### 0.2 Evidence Classes

`OBSERVATION`, `SURVEY`, `ETHNOGRAPHY`, `HISTORICAL_RECORD`, `ADMINISTRATIVE_DATA`,
`EXPERIMENT`, `NETWORK_DATA`, `MODEL`, `SCENARIO`, `SOURCE_CLAIM`, `UNKNOWN`.

### 0.4 Standard Knowledge Node Schema

Where applicable:
**definition → state variables → governing relations → assumptions → mechanisms → observables →
data sources → empirical status → scope/regime → uncertainty → failure modes → competing models →
falsifiers → dependencies → decision relevance → AMOS bridge**.

---

# H1 — Political Dynamics, Power & Conflict

### L1. Kernel Identity

Source engine: `Human_Society.Political_Dynamics` (kernel v1.0.0).
Seven scopes:
- power_and_institutions;
- political_conflict_and_cooperation;
- political_strategy;
- regime_and_system_dynamics;
- policy_and_interest_dynamics;
- change_and_stability;
- international_and_multi_actor_politics.

### L4. I/O Contract

Inputs — required: `political_question_or_scenario`, `context`; optional:
actors_and_positions, institutional_details, historical_context, constraints,
framework_preferences.

Outputs — required: `political_analysis`, `relevant_factors`,
`assumption_and_limitations`, **`alternative_interpretations`**.

**Contract rule:** an output missing `alternative_interpretations` is contract-invalid. This is
the anti-bias mechanism made structural, not stylistic preference.

### L5. Decision Gates

1. Single-interpretation output? → contract-invalid; regenerate with ≥2 rival readings.
2. Prescriptive slippage without framing? → rewrite descriptively.
3. Assumptions unstated? → block until assumption register exists.

### L2. Formal Vs Informal

Formal institutions: constitutions, statutes, procedures, courts, parties.
Informal institutions: norms, customs, patronage networks, unwritten conventions.
Formal rules can be undermined, bypassed, or reshaped by informal practice; measuring only the
formal layer misreads real governance.

### L1. Source Scope

Source skill: `amos-vn-cultural-ritual-energy-10000`. It contains ~10,000 equation records
modeling lineage ritual energy across three time layers, seven regions, and eight civilizational
lenses.

**Epistemic class:** MODEL throughout. The source itself declares these are structural metaphor
equations for cultural energy patterns; they are NOT physically measurable quantities. C06 must
never present `ritual energy`, `lineage energy`, etc., as instrumented observables.

### L5. Core Representative Equations

```
LE(t) = Σ(ritual_energy_i(t)) × transmission_efficiency × cultural_coherence
RE    = offering_value × sincerity_index × ritual_correctness × ancestral_resonance
HBE   = boundary_strength × internal_coherence × external_pressure_resistance
CT    = parent_energy × child_receptivity × cultural_medium_strength × time_decay
Cultural_E = -(1/ln N) Σ p_i ln p_i     (normalized diversity entropy)
```
All terms except the Shannon-form entropy expression are latent constructs without independent
measurement protocols. Use for organizing qualitative analysis and scenario comparison only.

### L6. Repair-Survival Condition

```
RitualRepairRate > CulturalEntropyAccumulationRate → lineage survives
```
This encodes the general claim that cultural continuity requires maintenance exceeding decay.
The threshold form is a heuristic; no calibrated rate estimates exist.

### L4. Prediction Discipline

C06 must distinguish:
- structural vulnerability assessment (slow variables);
- trigger identification (fast variables);
- outcome scenarios (branching, conditional);
- point predictions of regime change (almost never defensible).

Forecasting specific regime collapse dates is outside C06's honest capability.

---

### L1. Six Gates

From `amos-human-social-systems` / `amos-fairness-ethics`:
- BiasAuditChecker (gap 274): demographic parity, equalized odds, disparate impact, calibration…
- DistributionalHarmChecker (gap 275): allocation/quality/representational/dignitary harm.
- StakeholderRegistry (gap 276): primary/secondary/tertiary/marginalized/adversary.
- ExternalityModeler (gap 277): positive/negative × direct/indirect/cumulative/systemic.
- EthicalConflictChecker (gap 278): competing values/duty/rights/principle conflicts.
- EmergencyPowerGovernor (gap 279): status + sunset clause + oversight.

### L2. Gate Precedence Rules

FAIL takes precedence over CONDITIONAL everywhere. Emergency-power precedence:
`abuse_detected > no-sunset-clause > no-oversight > active(CONDITIONAL)`.
Any FAIL blocks emergency action.

### L1. Twelve Gates

ConsentLifecycleManager (258), PurposeLimitationEnforcer (259), DataMinimizationEngine (260),
RightToDeleteManager (261), DeletionAuditResolver (262), DataResidencyManager (263),
JurisdictionEngine (264), CompliancePolicyCompiler (265), RegulatoryChangeMonitor (266),
LicensingIPTracker (267), DerivativeWorkTracker (268), ExportControlChecker (269).

### L2. Nine-Step Pipeline

parse → update state → select goal → select strategy → select content → safety/ethics filter →
select channel/intensity → realize in language → evaluate and tag for learning.

### L3. Safety Constraints (Absolute)

Never deliberately induce panic/collapse; never manipulate/coerce; never invalidate lived
experience; never overpromise; always mark uncertainty; prefer nervous-system safety over speed.

### L4. Scope Note

The UBI biological claims embedded in the human-living-systems sources (loop-collapse model of
distress, deterministic restoration) are SOURCE_CLAIM/MODEL-class constructs of the AMOS corpus,
not established clinical consensus. C06 carries them as framework assumptions with that label.

---

# H7 — Vietnam Regional Society Systems

### M3. Rscf Society Mapping

Domain-specific RSCF encoding may use:
- **State** — actor positions, institutional configurations, cultural variables;
- **Constraint** — legal rules, resource bounds, legitimacy requirements, consent gates;
- **Feedback** — legitimacy↔performance loops, repression↔mobilization spirals, trust dynamics;
- **Repair** — institutional reform, truth/reconciliation processes, ritual renewal, gate resets.

A valid RSCF mapping preserves actual social science; generic labels must not replace mechanism.

---

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

---
**MOC:** references_MOC

## Related

- [[07_SKILLS_MOC]]
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · references_MOC · [[07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-c06-society-culture-master-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/amos-c06-society-culture-master/references/vault_domain_knowledge.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
