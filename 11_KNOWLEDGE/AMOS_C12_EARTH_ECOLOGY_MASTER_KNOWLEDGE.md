---
id: AMOS-C12-EARTH-ECOLOGY-MASTER-KNOWLEDGE
title: "AMOS C12 — Earth & Ecology Master Knowledge"
origin_architect: "Trang Phan"
artifact_type: "domain_master_knowledge"
domain: "C12_EARTH_ECOLOGY"
conclusion_class: "MIXED"
evidence_policy: "typed_per_node"
canon_status: "DOMAIN_KNOWLEDGE_WITH_RESEARCH_BRIDGES"
language: "en"
architecture: "HML_fractal_single_file"
placeholder_status: "NONE"
version: "1.1"
source_lineage:
  - "AMOS_C12_Earth_Ecology_SUPER.md"
source_family_mapping:
  - "F01_system_mapping"
  - "F02_climate_dynamics"
  - "F03_ecology_and_biodiversity"
  - "F04_food_water_health"
  - "F05_land_ocean_use"
  - "F06_risk_and_tipping_points"
  - "F07_scenarios_and_policy"
  - "F08_monitoring_and_data"
  - "F09_infrastructure_and_design"
  - "F10_meta_ecology_governance"
tags: ['knowledge', 'note']

---
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
- micronutrients;
- disturbance;
- herbivory.

Multiple limitation and co-limitation are common.

---

## M5. Disturbance Ecology

### L1. Disturbance
Disturbance alters ecosystem structure or resource availability.
Examples:
- fire;
- storm;
- flood;
- drought;
- grazing;
- pests;
- disease;
- human land conversion.

### L2. Resilience
Ecological resilience can mean:
- rate of return after disturbance;
- ability to remain within a regime;
- capacity to reorganize while retaining function.

These definitions must not be mixed without clarification.

### L3. Regime shifts
Some ecosystems can shift between alternative states when feedbacks stabilize different
configurations.

Evidence for alternative stable states must be ecosystem-specific; not every abrupt change
is a true bistable regime shift.

---

## M6. Invasive Species

### L1. Process
Invasion involves transport, introduction, establishment, spread, and impact.
Most introduced species do not become highly damaging invaders.

### L2. Risk drivers
Risk depends on:
- propagule pressure;
- climate suitability;
- disturbance;
- enemy release;
- resource availability;
- trait compatibility;
- network position.

### L3. Management
Prevention and early detection are usually more cost-effective than long-term control after
widespread establishment.

---

# H4 — Food, Water, Health & Human-Earth Coupling

## M1. Food-System Structure

### L1. Food security dimensions
Food security includes:
- availability;
- access;
- utilization/nutrition;
- stability over time.

Production alone is not a complete food-security metric.

### L2. Crop yield
Yield depends on:
- cultivar/genotype;
- temperature;
- water;
- radiation;
- soil fertility;
- pests/disease;
- management;
- atmospheric CO₂;
- extreme events.

Climate effects vary by crop, baseline climate, region, and adaptation.

### L3. Fisheries
Fishery production depends on:
- stock dynamics;
- recruitment;
- fishing mortality;
- habitat;
- temperature;
- oxygen;
- food-web change;
- governance.

Maximum sustainable yield is model- and uncertainty-dependent and should not be treated as a
fixed biological constant.

---

## M2. Soil Systems

### L1. Soil functions
Soils regulate:
- plant growth;
- water storage;
- nutrient cycling;
- carbon storage;
- habitat;
- pollutant transformation.

### L2. Soil organic matter
Soil carbon changes through litter inputs, roots, microbial processing, stabilization,
erosion, leaching, combustion, and disturbance.

### L3. Erosion
Erosion risk depends on rainfall erosivity, soil erodibility, slope, cover, and management.
Topsoil loss can reduce productivity and increase downstream sedimentation.

---

## M3. Freshwater Systems

### L1. Quantity
Water availability depends on precipitation, snow/ice, evapotranspiration, surface storage,
groundwater, infrastructure, withdrawals, and environmental flow requirements.

### L2. Quality
Major pressures include:
- nutrients;
- pathogens;
- sediments;
- salinity;
- heavy metals;
- organic pollutants;
- emerging contaminants.

### L3. Eutrophication
Excess nutrient loading can increase primary production and lead to oxygen depletion,
harmful algal blooms, habitat loss, and food-web changes.

---

## M4. Groundwater

### L1. Storage and recharge
Aquifers store water in pore spaces and fractures.
Recharge can be slow relative to extraction.

### L2. Drawdown
Persistent pumping above recharge or sustainable yield can lower water tables, reduce stream
baseflow, induce land subsidence, and mobilize poor-quality water.

### L3. Fossil groundwater
Some aquifers contain water recharged under past climates and effectively nonrenewable over
human planning horizons.

---

## M5. Environmental Health

### L1. Exposure pathway
A health effect requires a pathway:
`hazard → environmental concentration → exposure → dose → biological response`.

Presence of a contaminant does not itself prove human health impact without exposure/dose
assessment.

### L2. Air pollution
Fine particulate matter, ozone, nitrogen oxides, sulfur compounds, and other pollutants can
affect respiratory and cardiovascular health.

### L3. Heat
Heat-health risk is strongly modulated by age, health, occupation, urban form, cooling access,
housing quality, and acclimatization.

### L4. Vector-borne disease
Climate can affect vectors and pathogens through temperature and moisture, but disease risk
also depends on immunity, land use, mobility, housing, surveillance, and public health.

C12 must not infer disease burden from climate suitability alone.

---

## M6. Migration and Conflict Risk

### L1. Causal firewall
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

### L2. Correct claim form
Use:
`environmental stress may alter risk through specified mediating mechanisms`
rather than:
`climate change causes conflict`.

---

# H5 — Land, Ocean Use & Resource Systems

## M1. Land-Use Change

### L1. Drivers
Land-use change arises from:
- agriculture;
- forestry;
- urbanization;
- mining;
- infrastructure;
- conservation;
- abandonment;
- restoration.

### L2. Land-cover vs land-use
Land cover is physical surface condition; land use is human purpose/activity.
They must not be conflated.

### L3. Fragmentation
Habitat fragmentation changes patch size, connectivity, edge conditions, movement, and
species interactions.

---

## M2. Agriculture

### L1. Yield vs resilience
High average yield and high resilience are not equivalent.
Resilience may require:
- crop diversity;
- soil health;
- irrigation reliability;
- storage;
- seed diversity;
- financial buffers;
- adaptive management.

### L2. Irrigation
Irrigation can increase yield but may create:
- groundwater depletion;
- salinization;
- energy demand;
- downstream flow reduction.

### L3. Regenerative claims
"Regenerative agriculture" is a broad practice label.
Claims must be tied to measurable outcomes such as soil carbon, erosion, biodiversity,
nutrient leakage, profitability, water retention, or resilience.

---

## M3. Forestry

### L1. Carbon
Forests store carbon in biomass, dead wood, litter, and soils.
Carbon outcomes depend on baseline, disturbance, harvest, regrowth, product use, leakage, and
time horizon.

### L2. Fire
Fire can be both ecological process and hazard.
Suppression, fuel accumulation, climate, ignition, invasive grasses, land abandonment, and
management interact.

### L3. Afforestation caution
Tree planting is not universally beneficial.
Potential trade-offs include:
- water use;
- albedo change;
- biodiversity loss;
- grassland conversion;
- fire risk;
- non-native species.

---

## M4. Marine Resource Use

### L1. Fisheries
Sustainable management requires stock assessment, bycatch accounting, habitat protection,
enforcement, and uncertainty margins.

### L2. Aquaculture
Aquaculture impacts depend on species, feed, disease management, siting, effluent, escapes,
energy, and wild-fish inputs.

### L3. Marine spatial planning
Competing uses include:
- fishing;
- conservation;
- shipping;
- offshore energy;
- tourism;
- cables;
- military zones.

Planning must represent spatial conflict and cumulative impact.

---

## M5. Urban Ecology

### L1. Cities as ecosystems
Cities alter:
- energy flows;
- hydrology;
- heat;
- habitat;
- nutrient cycles;
- pollution;
- mobility.

### L2. Urban heat island
Heat islands arise from reduced vegetation, thermal properties, geometry, anthropogenic heat,
and ventilation patterns.

### L3. Green-blue infrastructure
Examples:
- urban trees;
- wetlands;
- bioswales;
- green roofs;
- floodable parks;
- restored streams.

Performance depends on climate, maintenance, species, design, land availability, and
governance.

---

# H6 — Risk, Tipping, Collapse & Resilience

## M1. Hazard–Exposure–Vulnerability

### L1. Risk decomposition
A useful conceptual model:
`Risk = f(Hazard, Exposure, Vulnerability, Capacity)`.

Multiplication is not universally correct; dependencies and nonlinearities may dominate.

### L2. Exposure
Exposure is the presence of people, assets, ecosystems, or functions in hazard zones.

### L3. Vulnerability
Vulnerability includes susceptibility and limited capacity to anticipate, cope, recover, or
adapt.

### L4. Adaptive capacity
Capacity depends on:
- wealth;
- institutions;
- knowledge;
- infrastructure;
- social networks;
- technology;
- legal authority;
- trust;
- ecological condition.

---

## M2. Tipping Elements

### L1. Definition
A tipping element is a system component that may undergo a large qualitative change when
drivers cross a critical region.

### L2. Threshold uncertainty
Exact thresholds are often uncertain and may depend on rate, spatial pattern, interacting
stressors, and system history.

### L3. Hysteresis
Some transitions can show hysteresis: reversing the forcing does not immediately restore the
original state.

### L4. Early warning
Candidate indicators include:
- rising variance;
- autocorrelation;
- slower recovery;
- spatial correlation;
- flickering.

These are not universal predictors and can generate false positives or negatives.

---

## M3. Cascading Risk

### L1. Cascade structure
A cascade occurs when failure in one subsystem alters conditions in another.

Example:
`drought → crop loss → price increase → household stress → migration pressure → political strain`.

Each arrow requires its own evidence and may be moderated by buffers.

### L2. Coupling strength
Cascade severity increases with:
- tight coupling;
- synchronization;
- common dependencies;
- low redundancy;
- long repair delay;
- shared infrastructure;
- correlated hazards.

### L3. Buffers
Buffers include:
- storage;
- insurance;
- ecological refugia;
- reserve capacity;
- diversified supply;
- modular design;
- emergency governance.

---

## M4. Resilience

### L1. Engineering resilience
Focus: recovery speed to a reference operating state.

### L2. Ecological resilience
Focus: ability to absorb disturbance without crossing into a different regime.

### L3. Transformative capacity
When the prior regime is no longer viable, transformation may be safer than restoration.

### L4. Least-regret action
A least-regret action performs acceptably across multiple plausible futures and avoids high
irreversibility when uncertainty is large.

---

## M5. Planetary Boundaries

### L1. Concept
Planetary-boundary frameworks identify broad Earth-system processes where large perturbation
may increase risk of destabilizing system function.

### L2. Epistemic caution
Boundaries are not literal planetary cliff edges with universally precise thresholds.
They are risk-oriented scientific constructs with heterogeneous evidence and uncertainty.

### L3. Decision use
Useful for:
- screening;
- portfolio risk;
- global context;
- identifying coupled pressures.

Not sufficient alone for local regulation or project approval.

---

# H7 — Monitoring, Data & Earth Observation

## M1. Measurement Architecture

### L1. Monitoring objective
Every indicator should answer:
`What decision changes if this variable changes?`

### L2. Temporal scale
Sampling frequency must match process timescale.
A monthly average can miss flash floods; daily measurements can miss long-term trends without
consistent continuity.

### L3. Spatial scale
Pixel, station, plot, watershed, biome, and national indicators are not interchangeable.

---

## M2. Remote Sensing

### L1. Platforms
Remote sensing includes:
- optical satellites;
- thermal sensors;
- radar;
- lidar;
- passive microwave;
- airborne systems;
- drones.

### L2. NDVI
`NDVI = (NIR - Red) / (NIR + Red)`.

NDVI is useful for vegetation greenness but can saturate in dense vegetation and is affected
by atmosphere, soil background, sensor characteristics, and phenology.

### L3. Radar
Synthetic-aperture radar can observe surface structure and moisture-related properties under
cloud cover and at night, but interpretation is geometry- and wavelength-dependent.

### L4. Lidar
Lidar can characterize vegetation structure, elevation, canopy height, and topography.

---

## M3. In-Situ Monitoring

### L1. Weather stations
Measure variables such as temperature, precipitation, humidity, wind, pressure, and radiation.

### L2. Stream gauges
Measure river stage and infer discharge using rating curves, whose validity can change with
channel geometry.

### L3. Ecological plots
Long-term plots provide demographic, biomass, species, and functional data.

### L4. Sensor quality
Monitoring requires:
- calibration;
- maintenance;
- metadata;
- missing-data handling;
- drift detection;
- versioned corrections.

---

## M4. Data Fusion

### L1. Sources
C12 may integrate:
- remote sensing;
- station data;
- surveys;
- ecological fieldwork;
- administrative data;
- model outputs;
- citizen science;
- local/Indigenous knowledge.

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

### L3. Independence
Two datasets derived from the same satellite product are not independent confirmation.

---

## M5. Indicators

### L1. Indicator types
- pressure;
- state;
- impact;
- response;
- resilience;
- exposure;
- vulnerability.

### L2. Composite indices
Composite indices require:
- explicit weighting;
- normalization;
- missing-data policy;
- sensitivity analysis.

An index can conceal trade-offs and should not replace component variables in high-stakes use.

---

# H8 — Scenarios, Policy, Infrastructure & Governance

## M1. Scenario Design

### L1. Scenario vs prediction
A scenario is a conditional future:
`if assumptions A, B, C hold, then outcome distribution X is modeled`.

A scenario is not a forecast unless probabilities are explicitly justified.

### L2. Scenario dimensions
Common dimensions:
- emissions;
- population;
- technology;
- land use;
- policy;
- behavior;
- economic structure;
- adaptation.

### L3. Internal consistency
Scenario assumptions should not contradict one another without an explicit mechanism.

---

## M2. Climate Projection Use

### L1. Ensemble interpretation
Model ensembles sample structural and parametric uncertainty imperfectly.
Ensemble spread is not a complete probability distribution of the future.

### L2. Downscaling
Dynamical and statistical downscaling translate coarse climate information toward local
scales.

Downscaled precision does not guarantee local truth if driving models or local processes are
misrepresented.

### L3. Decision framing
Use:
- scenario envelopes;
- threshold analysis;
- sensitivity analysis;
- robust decision-making;
- adaptive pathways.

Avoid single-number deterministic infrastructure futures.

---

## M3. Adaptation

### L1. Adaptation types
- anticipatory;
- reactive;
- incremental;
- transformational;
- ecosystem-based;
- infrastructure-based;
- behavioral;
- institutional.

### L2. Maladaptation
An action is maladaptive if it reduces short-term risk while increasing long-term or
transferred risk.

Examples:
- flood defenses that induce unsafe development behind them;
- groundwater pumping that solves drought short term but depletes aquifers;
- cooling that increases grid fragility under peak load.

---

## M4. Mitigation

### L1. Emissions
Mitigation reduces net forcing by reducing emissions, enhancing removals, or altering
radiative drivers.

### L2. Sector coupling
Electricity, transport, buildings, industry, land use, food, and waste interact through
energy and material flows.

### L3. Carbon removal
Carbon-removal options differ in:
- permanence;
- land demand;
- energy;
- cost;
- ecological effect;
- monitoring;
- reversal risk.

Avoid counting temporary storage as permanent removal without a permanence model.

---

## M5. Infrastructure Resilience

### L1. Design inputs
Infrastructure design should consider:
- current hazard;
- projected hazard;
- asset lifetime;
- failure consequence;
- redundancy;
- maintenance;
- dependencies;
- recovery time.

### L2. Critical dependencies
Power, water, transport, telecoms, health, food logistics, and finance are interconnected.

### L3. Adaptive design
Options include:
- modular expansion;
- staged investment;
- trigger-based upgrades;
- flexible standards;
- relocatable assets.

---

## M6. Nature-Based Solutions

### L1. Definition
Nature-based solutions intentionally use ecosystem processes to address societal challenges
while delivering biodiversity/ecosystem benefits.

### L2. Evaluation
Evaluate:
- hazard reduction;
- ecological integrity;
- maintenance;
- land tenure;
- social distribution;
- failure under extremes;
- time to maturity.

### L3. Greenwashing firewall
A project is not ecologically beneficial merely because it contains vegetation or uses
"nature-based" language.

---

## M7. Ecological Economics

### L1. Embedded economy
Economic systems depend on energy, materials, ecosystem functions, labor, and institutions.

### L2. Externality
An externality is a cost or benefit not fully reflected in a transaction.

### L3. Discounting
Discount rates strongly influence valuation of long-horizon impacts.
The choice is partly normative and must be explicit.

### L4. Non-substitutability
Some ecological functions may have thresholds or irreversibilities that make monetary
substitution incomplete.

---

## M8. Governance

### L1. Institutional mapping
Governance analysis should identify:
- formal authority;
- informal power;
- enforcement capacity;
- funding;
- information flows;
- accountability;
- jurisdictional overlap.

### L2. Common-pool resources
Fisheries, forests, aquifers, grazing lands, and atmospheric sinks often require collective
governance because exclusion and depletion dynamics differ from ordinary private goods.

### L3. Polycentric governance
Multiple centers of authority can increase adaptability and redundancy, but can also create
coordination failures.

### L4. Cross-border systems
Rivers, fisheries, migratory species, air pollution, climate, and trade cross political
boundaries. Jurisdiction boundaries do not define ecological boundaries.

---

## M9. Environmental Justice

### L1. Distribution
Environmental harms and benefits are unevenly distributed.

### L2. Procedural justice
Decision quality depends partly on who has voice, information, representation, and appeal.

### L3. Recognition
Policies can fail when they ignore culturally specific relationships to land, water, species,
and livelihood.

AMOS should treat justice assumptions as explicit normative premises, not hidden scientific
facts.

---

# H9 — AMOS/Trang Earth-System Research Bridge

## M1. Source Family Integration

The source C12 engine identifies ten families:
1. planetary system mapping;
2. climate and energy dynamics;
3. ecology and biodiversity;
4. food, water, health;
5. land and ocean use;
6. systemic risk and tipping points;
7. scenario and policy pathways;
8. monitoring/data/indicators;
9. infrastructure/regenerative design;
10. meta-ecology/governance.

This master file preserves those functions but replaces repeated `earth_ecology_micro_module`
placeholder records with substantive knowledge and explicit epistemic boundaries.

---

## M2. HML Mapping for Earth Systems

### L1. H layer
Examples:
- long-horizon biosphere stability;
- watershed viability;
- regional food security;
- coastal habitability.

### L2. M layer
Examples:
- institutions;
- land-use systems;
- supply chains;
- infrastructure networks;
- ecosystem configuration.

### L3. L layer
Examples:
- farm practice;
- pump operation;
- zoning decision;
- habitat patch;
- monitoring station;
- local species interaction.

HML is an AMOS reasoning structure, not a scientific claim that Earth has exactly three
ontological levels.

---

## M3. RSCF Earth-System Mapping

A domain-specific RSCF representation may encode:
- **State** — ecological/climatic system variables;
- **Constraint** — physical, biological, legal, resource, or boundary conditions;
- **Feedback** — causal loops and adaptive response;
- **Repair** — restoration or recovery mechanism where physically/biologically real.

A valid RSCF mapping must preserve the actual science rather than replacing process models
with generic labels.

---

## M4. Earth-System Viability

### L1. Proposed AMOS form
A conceptual viability function may include:
`V = f(ecological integrity, water, food, climate exposure, adaptive capacity, future options)`.

**Class:** MODEL.

### L2. Correct use
Use this for organizing decision variables and trade-offs.

### L3. Incorrect use
Do not claim a universal scalar "planetary health score" unless:
- variables are operationalized;
- weights are justified;
- uncertainty is propagated;
- thresholds are validated;
- trade-offs remain visible.

---

## M5. Collapse Propagation

A proposed AMOS abstraction:
`CollapsePropagation = LocalFailure × CouplingStrength × TransmissionSpeed × RepairDelay`.

**Class:** MODEL.

A rigorous implementation requires:
- causal graph;
- coupling matrix;
- temporal dynamics;
- threshold rules;
- stochastic disturbances;
- intervention capability;
- empirical calibration.

Useful mathematical neighbors include network science, reliability engineering, epidemic-like
propagation models, percolation, control theory, and viability theory.

---

## M6. Resilience Operator

A proposed AMOS resilience construct may combine:
- resistance;
- recovery speed;
- redundancy;
- diversity;
- modularity;
- adaptive capacity;
- option preservation.

No fixed multiplicative formula is universally valid.

A better engineering implementation may define a recovery curve:
`R_resilience = ∫ performance(t) dt`
relative to a baseline and disruption window.

---

## M7. Future Debt

The AMOS notion of `FutureDebt` can represent deferred ecological or infrastructural costs.

Candidate measurable proxies:
- maintenance backlog;
- soil depletion;
- groundwater drawdown;
- accumulated contamination;
- habitat fragmentation;
- carbon lock-in;
- unfunded adaptation need.

**Class:** MODEL / decision metric.
It should not be presented as a physical state variable without operational definition.

---

## M8. Option Preservation

`Q` or future-option preservation is useful where irreversible decisions matter.

Examples:
- retaining migration corridors;
- avoiding development in future flood-retreat zones;
- maintaining genetic diversity;
- preserving aquifer storage;
- keeping modular infrastructure pathways open.

This maps naturally to real-options analysis, robust decision-making, and adaptive pathways.

---

## M9. Tipping-Point Governance

AMOS should distinguish:
- known threshold;
- estimated threshold;
- suspected threshold;
- unknown threshold;
- early-warning signal;
- post-hoc regime-shift interpretation.

The engine must not manufacture precise tipping values when literature only supports a broad
risk region.

---

## M10. Climate–Biosphere–Society Coupling

A valid cross-domain chain should explicitly encode mediation.

Example:
`warming`
→ `soil-moisture deficit`
→ `crop stress`
→ `yield loss`
→ `market response`
→ `household food access`
→ `health outcome`.

Each edge can be modified by technology, trade, policy, inequality, storage, irrigation,
insurance, and adaptation.

The final outcome confidence cannot exceed the weakest load-bearing edge without independent
revalidation.

---

## M11. Ecological Causal Firewall

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

## M12. Scenario Firewall

Scenario pathways are not probabilities unless explicitly probabilized.

Correct:
`Under pathway X and adaptation assumption Y, model Z produces outcome range R.`

Incorrect:
`The future will be R.`

---

## M13. Indigenous and Local Knowledge

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

## M14. Monitoring-to-Decision Loop

```text
observe
→ validate
→ compare against thresholds/models
→ update state estimate
→ test competing explanations
→ identify decision-changing uncertainty
→ choose reversible action where possible
→ monitor outcome
→ revise
```

This is the correct operational form of C12 rather than a static x100k registry.

---

# C12 ↔ CC05 Mind & Behavior Reference Bridge

## Cross-domain reference

**Canonical reference:** `AMOS_CC05_mind_behavior`

C12 owns Earth-system, ecological, environmental, resource, and coupled human–Earth state.
`AMOS_CC05_mind_behavior` owns mind/behavior mechanisms such as perception, cognition,
emotion, motivation, learning, decision behavior, social behavior, and behavioral adaptation.

The reference is bidirectional at the conceptual layer but does **not** merge domain ownership.

## C12 → CC05 handoff

C12 may provide environmental inputs such as:
- heat, air quality, noise, crowding, and other exposures;
- disaster and extreme-event experience;
- food/water/resource insecurity;
- ecological degradation or restoration;
- environmental risk signals;
- displacement and livelihood pressure;
- urban and built-environment conditions;
- climate/ecological uncertainty.

CC05 may then model behavioral or psychological responses within its own scope.

## CC05 → C12 handoff

CC05 outputs may become human-system drivers in C12 when behavior changes:
- energy or water demand;
- mobility;
- consumption;
- land-use decisions;
- conservation behavior;
- risk preparation;
- evacuation or migration;
- technology adoption;
- institutional compliance;
- collective-resource use.

## Causal firewall

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

## Reference declaration

```yaml
cross_domain_refs:
  - id: AMOS_CC05_mind_behavior
    relation: coupled_human_earth_behavior
    direction: bidirectional
    ownership_rule: preserve_domain_boundaries
    causal_status: mediated_not_assumed
    confidence_rule: weakest_load_bearing_edge
```

---

# C12 Master Dependency Spine

```text
solar input + planetary physics
            ↓
atmosphere ↔ ocean ↔ cryosphere
            ↓
water + carbon + nutrient cycles
            ↓
ecosystem structure + biodiversity
            ↓
food / water / health systems
            ↓
land + ocean use + infrastructure
            ↓
risk / tipping / cascading failure
            ↓
monitoring + state estimation
            ↓
scenarios + governance + adaptation
            ↓
AMOS cross-scale decision architecture
```

# C12 Decision Capsule Template

```text
System:
Boundary:
Location:
Timescale:
Decision:
Irreversibility:
Climate regime:
Ecological regime:
Human system:
Observed state:
Key stocks:
Key flows:
Known feedbacks:
Potential thresholds:
Hazards:
Exposure:
Vulnerability:
Adaptive capacity:
Data sources:
Data freshness:
Model ensemble:
Scenario assumptions:
Competing explanations:
Decision-sensitive uncertainty:
Least-regret actions:
Triggers for escalation:
Monitoring plan:
Falsifiers:
Revalidation date:
```

# C12 Promotion Rule

A new Earth/ecology claim may move from `MODEL` toward stronger status only when:
1. terms and system boundary are operationally defined;
2. spatial and temporal scales are explicit;
3. data provenance and uncertainty are available;
4. scenario assumptions are separated from observations;
5. competing explanations are considered;
6. causal claims identify mechanism and confounders;
7. model skill is evaluated in the relevant regime;
8. projections preserve scenario dependence;
9. irreversible recommendations undergo stronger validation;
10. governance records contradiction, supersession, and revalidation.

# C12 Final Boundary

C12 is not a planetary oracle.

Its purpose is to maintain a disciplined, cross-scale map of Earth-system dynamics that can
connect climate, ecology, water, food, health, infrastructure, risk, and governance without
silently flattening their differences.

The architecture should remain open and repairable:
**integrity > completeness > fluency > speed**.

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00_ROOT/00-Home]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: amos_c12_earth_ecology_master_knowledge
node_type: note
path: 11_KNOWLEDGE/AMOS_C12_EARTH_ECOLOGY_MASTER_KNOWLEDGE.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_ROOT/00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[KNOWLEDGE_MOC]]
