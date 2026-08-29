---
title: Vault Domain Knowledge — Amos C12 Earth Ecology Master
type: reference
source: 07_SKILLS/amos-c12-earth-ecology-master/references
tags:
- reference
- amos-c12-earth-ecology-master
- canon/skill
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

# amos-c12-earth-ecology-master — Vault-Sourced Domain Knowledge

> Load this reference only when detailed domain knowledge is needed.
> This content was moved from SKILL.md for progressive loading.

---

> **Source**: `11_KNOWLEDGE/AMOS_C12_EARTH_ECOLOGY_MASTER_KNOWLEDGE.md` from the AMOS_OS Obsidian vault.
> This is substantive domain knowledge, not script-generated content.

# AMOS C12 — Earth & Ecology Master Knowledge

> **Epistemic boundary**
>
> This file replaces the synthetic `x100k` micro-module expansion with substantive Earth-system
> and ecology knowledge. It does not claim encyclopedic completeness. Established observations,
> tested models, scenario-dependent projections, competing hypotheses, normative policy choices,
> and AMOS/Trang abstractions are kept separate.
>
> Earth-system recommendations are always scope-, scenario-, location-, and timescale-dependent.
> Long-horizon outputs must preserve uncertainty, model disagreement, data gaps, adaptation
> capacity, governance constraints, and potential regime shifts.

## 0. C12 Knowledge Contract

### 0.1 Claim classes
- **VERIFIED** — strongly supported empirical result within a stated regime.
- **DERIVED** — mathematical or logical consequence of stated premises/model.
- **MODEL** — representation useful within stated scope.
- **CONDITIONAL** — dependent on explicit assumptions, scenario, or regime.
- **COMPETING** — unresolved alternatives.
- **UNKNOWN/GAP** — insufficient evidence or unresolved mechanism.

### 0.2 Evidence classes
`OBSERVATION`, `EXPERIMENT`, `REMOTE_SENSING`, `MONITORING`, `DERIVED`, `MODEL`,
`SCENARIO`, `SOURCE_CLAIM`, `UNKNOWN`.

### 0.3 C12 H-level ownership
1. Earth-System Structure & Biogeophysical Flows
2. Climate Dynamics, Oceans & Cryosphere
3. Ecology, Biodiversity & Biogeochemistry
4. Food, Water, Health & Human-Earth Coupling
5. Land, Ocean Use & Resource Systems
6. Risk, Tipping, Collapse & Resilience
7. Monitoring, Data & Earth Observation
8. Scenarios, Policy, Infrastructure & Governance
9. AMOS/Trang Earth-System Research Bridge

A topic has one primary owner. Cross-links are references, not duplicated substantive sections.

### 0.4 Standard knowledge node schema
Where applicable:
**definition → state variables → governing relations → assumptions → mechanisms → observables →
data sources → empirical status → scope/regime → uncertainty → failure modes → competing models →
falsifiers → dependencies → decision relevance → AMOS bridge**.

---

# H1 — Earth-System Structure & Biogeophysical Flows

## M1. Earth as a Coupled System

### L1. Major interacting subsystems
C12 models Earth as a coupled system containing:
- atmosphere;
- hydrosphere;
- ocean;
- cryosphere;
- lithosphere;
- pedosphere;
- biosphere;
- anthroposphere.

These are analytical partitions, not physically independent worlds. Matter, energy, momentum,
organisms, information, and human actions cross subsystem boundaries continuously.

### L2. Stocks and flows
A stock `X` changes according to:
`dX/dt = Σ inflows - Σ outflows + internal production - internal loss`.

Examples:
- atmospheric carbon stock;
- soil organic carbon;
- groundwater storage;
- glacier mass;
- forest biomass;
- nutrient pools.

A stock-flow diagram is only as reliable as its boundary definitions and omitted pathways.

### L3. Conservation
Earth-system budgets often use conservation laws:
- mass conservation;
- energy conservation;
- elemental budgets;
- water balance.

For a watershed:
`ΔS = P - ET - Q - G ± transfers`
where `S` is storage, `P` precipitation, `ET` evapotranspiration, `Q` runoff, and `G` net
groundwater exchange under the chosen sign convention.

### L4. Feedback
Feedback exists when a state change alters processes that subsequently affect that state.

Positive feedback amplifies a perturbation; negative feedback dampens it.

Examples:
- ice-albedo feedback;
- water-vapor feedback;
- vegetation–soil–moisture feedback;
- predator–prey regulation;
- carbon-cycle feedbacks.

"Positive" does not mean beneficial; "negative" does not mean harmful.

---

## M2. Planetary Energy Balance

### L1. Incoming and outgoing radiation
At global equilibrium scale, absorbed solar energy and outgoing longwave radiation are central.

A simple zero-dimensional balance:
`(1 - α) S0 / 4 = OLR`
where `α` is planetary albedo and `S0` solar irradiance.

This model omits spatial structure, clouds, atmospheric dynamics, ocean heat uptake, and
spectral greenhouse physics.

### L2. Effective radiating temperature
If Earth were approximated as a black/gray body:
`OLR ≈ ε σ T_e^4`.

The surface is warmer than the effective emission temperature because greenhouse gases and
clouds alter infrared radiative transfer.

### L3. Radiative forcing
Radiative forcing measures a perturbation to the planetary energy budget under a specified
definition. Climate response depends on feedbacks, ocean heat uptake, spatial pattern, and
timescale.

### L4. Climate sensitivity
Equilibrium climate sensitivity and transient climate response are distinct quantities.
They are inferred from models, paleoclimate, observations, and process constraints.

AMOS rule:
Never treat one sensitivity estimate as a universal response parameter independent of state,
timescale, forcing pattern, or model assumptions.

---

## M3. Carbon Cycle

### L1. Major carbon reservoirs
Key reservoirs include:
- atmosphere;
- terrestrial vegetation;
- soils;
- ocean dissolved inorganic carbon;
- marine biota;
- sediments and rocks;
- fossil carbon.

### L2. Fast and slow carbon cycles
Fast exchanges occur over days to centuries among atmosphere, land, and ocean.
Slow geological processes operate over millennia to millions of years.

### L3. Anthropogenic perturbation
Human activities transfer carbon from geological and biospheric reservoirs into the
atmosphere through fossil-fuel combustion, cement production, and land-use change.

Atmospheric CO₂ increases when emissions exceed net uptake by land and ocean sinks.

### L4. Sink nonstationarity
Land and ocean sinks vary with:
- temperature;
- precipitation;
- CO₂ fertilization;
- nutrient limitation;
- fire;
- land management;
- ocean circulation;
- acidification;
- ecosystem disturbance.

Historical sink fractions must not be assumed constant under future regimes.

---

## M4. Water Cycle

### L1. Global hydrological cycle
Water moves through evaporation, condensation, precipitation, infiltration, runoff,
groundwater flow, ice storage, and biological transpiration.

### L2. Clausius–Clapeyron relation
Saturation vapor pressure increases approximately exponentially with temperature.
Near typical lower-atmospheric temperatures, saturation water-vapor capacity rises by roughly
several percent per kelvin, but precipitation response is constrained by energy and dynamics.

### L3. Regional water balance
Regional hydroclimate depends on:
- circulation;
- topography;
- land cover;
- snowpack;
- soil moisture;
- groundwater;
- reservoirs;
- irrigation;
- evapotranspiration.

Global trends cannot be transferred mechanically to local water availability.

---

## M5. Nutrient Cycles

### L1. Nitrogen
Nitrogen cycles through fixation, assimilation, mineralization, nitrification,
denitrification, volatilization, leaching, and transport.

Reactive nitrogen added through fertilizer and combustion can increase productivity while
also driving eutrophication, air pollution, greenhouse forcing, and biodiversity loss.

### L2. Phosphorus
Phosphorus has no large atmospheric gas phase comparable to nitrogen.
Agricultural phosphorus is obtained largely from mined phosphate rock and recirculated
through soils, food systems, water bodies, waste streams, and sediments.

### L3. Stoichiometric constraint
Biological productivity can be limited by whichever nutrient or resource is scarce relative
to demand. Limitation is ecosystem- and regime-dependent.

---

# H2 — Climate Dynamics, Oceans & Cryosphere

## M1. Atmosphere and Circulation

### L1. Primitive physical basis
Atmospheric models solve discretized forms of:
- momentum conservation;
- mass continuity;
- thermodynamic energy;
- water species;
- radiative transfer;
- parameterized unresolved processes.

General circulation models are physically constrained numerical models, not literal replicas
of every microscale process.

### L2. Global circulation
Large-scale structure includes:
- Hadley, Ferrel, and polar cells;
- jet streams;
- storm tracks;
- monsoon systems;
- Walker circulation;
- planetary waves.

Their positions and strengths vary seasonally and interannually.

### L3. Modes of variability
Climate variability includes El Niño–Southern Oscillation, North Atlantic variability,
Indian Ocean variability, Pacific decadal variability, and other coupled modes.

These modes can strongly modulate regional climate without representing long-term forced
trend by themselves.

---

## M2. Greenhouse Effect

### L1. Mechanism
Greenhouse gases absorb and emit infrared radiation at wavelength-dependent bands.
Increasing greenhouse-gas concentrations alters the effective level from which Earth emits
radiation to space, creating an energy imbalance until the climate system adjusts.

### L2. Major greenhouse agents
Long-lived greenhouse gases include:
- carbon dioxide;
- methane;
- nitrous oxide;
- halogenated gases.

Water vapor is a major greenhouse gas but acts primarily as a climate feedback at global
climate timescales because atmospheric water vapor responds strongly to temperature.

### L3. Aerosols
Aerosols affect climate through scattering/absorption and cloud interactions.
Their spatial heterogeneity and short atmospheric lifetime create large regional complexity.

---

## M3. Extremes and Compound Events

### L1. Heat extremes
Heat risk depends on temperature, humidity, radiation, wind, nighttime cooling, exposure,
housing, health status, labor conditions, and acclimatization.

### L2. Drought
Drought has multiple definitions:
- meteorological;
- agricultural;
- hydrological;
- ecological;
- socioeconomic.

A rainfall deficit does not map one-to-one to groundwater or crop drought.

### L3. Flood
Flood hazard arises from combinations of:
- intense precipitation;
- saturated soils;
- river discharge;
- snowmelt;
- storm surge;
- drainage capacity;
- land cover;
- channel modification.

### L4. Compound events
Examples include:
- heat + drought;
- storm surge + river flooding;
- wildfire + post-fire landslide;
- drought + crop failure + price shock;
- heat + power-grid stress.

Risk assessment should preserve joint probability and dependency rather than multiplying
independent probabilities when the hazards are correlated.

---

## M4. Ocean System

### L1. Ocean heat uptake
The ocean stores most of the excess heat accumulated by the climate system because of its
large heat capacity.

### L2. Circulation
Ocean circulation includes wind-driven gyres, overturning circulation, mesoscale eddies, and
vertical mixing. Circulation transports heat, carbon, oxygen, nutrients, and organisms.

### L3. Ocean acidification
Dissolved CO₂ alters carbonate chemistry:
`CO₂ + H₂O ↔ H₂CO₃ ↔ HCO₃⁻ + H⁺ ↔ CO₃²⁻ + 2H⁺`.

Increased anthropogenic CO₂ lowers average ocean pH and carbonate-ion availability, affecting
calcifying organisms and ecosystem processes.

### L4. Deoxygenation
Ocean warming reduces oxygen solubility and can strengthen stratification. Nutrient loading
can additionally produce local hypoxia through respiration of organic matter.

---

## M5. Cryosphere

### L1. Components
Cryosphere includes:
- mountain glaciers;
- ice sheets;
- sea ice;
- snow cover;
- permafrost;
- seasonally frozen ground.

### L2. Sea ice
Melting floating sea ice has little direct effect on sea level through displacement, but
strongly affects albedo, ecosystems, and ocean-atmosphere exchange.

### L3. Land ice
Loss of glaciers and land-based ice sheets contributes to sea-level rise.

### L4. Permafrost
Permafrost stores large quantities of frozen organic carbon.
Thaw can increase CO₂ and methane emissions, but rates depend on hydrology, vegetation,
microbiology, fire, and landscape change.

---

## M6. Sea-Level Change

### L1. Main drivers
Global mean sea level changes through:
- thermal expansion;
- glacier mass loss;
- ice-sheet mass loss;
- terrestrial water storage changes.

### L2. Local relative sea level
Local risk also depends on:
- land subsidence/uplift;
- sediment compaction;
- groundwater extraction;
- tectonics;
- gravitational/fingerprint effects;
- tides and storm surge.

Global mean sea level is not a sufficient local design variable.

---

# H3 — Ecology, Biodiversity & Biogeochemistry

## M1. Ecological Organization

### L1. Levels
Ecology studies:
- individuals;
- populations;
- communities;
- ecosystems;
- landscapes;
- biomes;
- biosphere.

These are nested but not perfectly separable scales.

### L2. Population growth
Exponential model:
`dN/dt = rN`.

Logistic model:
`dN/dt = rN(1 - N/K)`.

Real populations can depart strongly from these models because of age structure, migration,
resource variation, predation, disease, environmental stochasticity, and nonstationary
carrying capacity.

### L3. Metapopulations
Spatially separated habitat patches can be connected by dispersal.
Persistence may depend on colonization, local extinction, connectivity, patch quality, and
source-sink dynamics.

---

## M2. Species Interactions

### L1. Interaction types
Common categories include:
- competition;
- predation;
- herbivory;
- parasitism;
- mutualism;
- commensalism.

Context can change the sign or strength of an interaction.

### L2. Trophic structure
Food webs encode energy and material transfer.
Trophic cascades can occur when changes at one trophic level propagate to others.

### L3. Keystone and foundation species
A keystone species has disproportionate ecological effect relative to abundance.
A foundation species creates or structures habitat for many other organisms.

These labels are empirical ecological roles, not permanent species properties independent of
ecosystem context.

---

## M3. Biodiversity

### L1. Dimensions
Biodiversity includes:
- genetic diversity;
- species diversity;
- functional diversity;
- phylogenetic diversity;
- ecosystem diversity.

### L2. Diversity indices
Shannon index:
`H' = -Σ p_i ln p_i`.

Simpson-family indices emphasize dominance in different ways depending on convention.

No single index captures biodiversity value, functional redundancy, evolutionary history,
or ecosystem integrity.

### L3. Extinction debt
Habitat loss and fragmentation can create delayed extinctions.
Observed persistence immediately after disturbance does not prove long-term viability.

### L4. Functional redundancy
Multiple species may contribute to similar functions, potentially buffering ecosystem
processes. Redundancy is partial and context-dependent; species are not interchangeable units.

---

## M4. Productivity and Ecosystem Metabolism

### L1. Primary production
Gross primary production `GPP` is total photosynthetic carbon fixation.
Net primary production:
`NPP = GPP - R_auto`
where `R_auto` is autotrophic respiration.

### L2. Net ecosystem production
A common conceptual form:
`NEP = GPP - R_ecosystem`
with sign conventions varying.

### L3. Limitation
Productivity may be limited by:
- light;
- water;
- temperature;
- nitrogen;
- phosphorus;
-


## Vault-Sourced Domain Content

> Source: `11_KNOWLEDGE/AMOS_C12_EARTH_ECOLOGY_MASTER_KNOWLEDGE.md` (45598 bytes in vault)

### 0.1 Claim Classes

- **VERIFIED** — strongly supported empirical result within a stated regime.
- **DERIVED** — mathematical or logical consequence of stated premises/model.
- **MODEL** — representation useful within stated scope.
- **CONDITIONAL** — dependent on explicit assumptions, scenario, or regime.
- **COMPETING** — unresolved alternatives.
- **UNKNOWN/GAP** — insufficient evidence or unresolved mechanism.

### 0.2 Evidence Classes

`OBSERVATION`, `EXPERIMENT`, `REMOTE_SENSING`, `MONITORING`, `DERIVED`, `MODEL`,
`SCENARIO`, `SOURCE_CLAIM`, `UNKNOWN`.

### 0.4 Standard Knowledge Node Schema

Where applicable:
**definition → state variables → governing relations → assumptions → mechanisms → observables →
data sources → empirical status → scope/regime → uncertainty → failure modes → competing models →
falsifiers → dependencies → decision relevance → AMOS bridge**.

---

# H1 — Earth-System Structure & Biogeophysical Flows

### L2. Major Greenhouse Agents

Long-lived greenhouse gases include:
- carbon dioxide;
- methane;
- nitrous oxide;
- halogenated gases.

Water vapor is a major greenhouse gas but acts primarily as a climate feedback at global
climate timescales because atmospheric water vapor responds strongly to temperature.

### L1. Food Security Dimensions

Food security includes:
- availability;
- access;
- utilization/nutrition;
- stability over time.

Production alone is not a complete food-security metric.

### L1. Causal Firewall

Environmental stress can contribute to migration or conflict risk but rarely acts alone.

Potential mediators include:
- livelihoods;
- food prices;
- water governance;
- institutions;
- inequality;
- displacement policy;
- conflict history;
- border regimes.

### L2. Threshold Uncertainty

Exact thresholds are often uncertain and may depend on rate, spatial pattern, interacting
stressors, and system history.

### L2. Epistemic Caution

Boundaries are not literal planetary cliff edges with universally precise thresholds.
They are risk-oriented scientific constructs with heterogeneous evidence and uncertainty.

### L2. Provenance

Each fused variable should retain:
- source;
- spatial resolution;
- temporal resolution;
- uncertainty;
- processing chain;
- license;
- calibration;
- version.

### L3. Greenwashing Firewall

A project is not ecologically beneficial merely because it contains vegetation or uses
"nature-based" language.

---

### M3. Rscf Earth-System Mapping

A domain-specific RSCF representation may encode:
- **State** — ecological/climatic system variables;
- **Constraint** — physical, biological, legal, resource, or boundary conditions;
- **Feedback** — causal loops and adaptive response;
- **Repair** — restoration or recovery mechanism where physically/biologically real.

A valid RSCF mapping must preserve the actual science rather than replacing process models
with generic labels.

---

### M11. Ecological Causal Firewall

Do not infer causation from:
- correlation across sites;
- before/after sequence alone;
- spatial coincidence;
- model fit alone;
- mechanistic plausibility alone.

Causal evidence can draw from:
- manipulative experiments;
- natural experiments;
- time-series identification;
- mechanistic process evidence;
- causal inference with explicit assumptions;
- convergent independent evidence.

---

### M12. Scenario Firewall

Scenario pathways are not probabilities unless explicitly probabilized.

Correct:
`Under pathway X and adaptation assumption Y, model Z produces outcome range R.`

Incorrect:
`The future will be R.`

---

### M13. Indigenous And Local Knowledge

Local and Indigenous knowledge can provide long-horizon observations, process knowledge, and
context unavailable in instrumental records.

AMOS treatment should preserve:
- source identity;
- community ownership;
- consent;
- context;
- epistemic status;
- non-extractive use.

It should not strip knowledge from governance or cultural context and relabel it as generic
data.

---

### Causal Firewall

Environmental condition → mind/behavior → Earth-system outcome is a mediated causal chain.
C12 must not infer psychological states directly from environmental measurements, and CC05
behavioral constructs must not be treated as ecological observations.

Example:

```text
heat exposure [C12]
→ perceived thermal stress / cognition / behavior [CC05]
→ cooling behavior [CC05]
→ electricity demand [C12-linked human system]
→ grid/emissions consequence [C12]
```

Every cross-domain arrow inherits its own evidence, population, environment, timescale,
confounders, and uncertainty.

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
node_id: amos-c12-earth-ecology-master-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/amos-c12-earth-ecology-master/references/vault_domain_knowledge.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
