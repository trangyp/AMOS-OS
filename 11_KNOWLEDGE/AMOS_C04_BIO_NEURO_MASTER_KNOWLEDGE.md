---
id: AMOS-C04-BIO-NEURO-MASTER-KNOWLEDGE
title: "AMOS C04 — Biology & Neuro Master Knowledge"
origin_architect: "Trang Phan"
artifact_type: "domain_master_knowledge"
domain: "C04_BIOLOGY_NEURO"
conclusion_class: "MIXED"
evidence_policy: "typed_per_node"
canon_status: "DOMAIN_KNOWLEDGE_WITH_RESEARCH_BRIDGES"
language: "en"
architecture: "HML_fractal_single_file"
placeholder_status: "NONE"
version: "1.1"
source_lineage:
  - "amos-main-core-biological"
  - "amos-biological-programming"
  - "amos-origin-of-logic-biological"
  - "amos-trust-biological-currency"
  - "amos-governance-biological-foundations"
  - "amos-leadership-biological-foundations"
  - "amos-quantum-biological-business"
source_family_mapping:
  - "F01_biological_system_mapping"
  - "F02_homeostasis_and_regulation"
  - "F03_neuro_and_signal_processing"
  - "F04_immune_defense_repair"
  - "F05_evolution_adaptation_learning"
  - "F06_bio_social_coupling_trust_stress"
  - "F07_organizational_biological_models"
  - "F08_ubbi_alignment_governance"
  - "F09_neuro_plausibility_firewall"
tags: ['knowledge', 'note']

---
# AMOS C04 — Biology & Neuro Master Knowledge

> **Epistemic boundary**
>
> This file replaces synthetic micro-module expansion with substantive biology/neuroscience
> knowledge plus AMOS biological-modeling frameworks. It does not claim encyclopedic
> completeness. Established physiology, tested models, contested hypotheses, metaphorical
> frameworks, and normative AMOS abstractions are kept strictly separated and typed.
>
> **Hard anti-overclaim boundary:** claims of quantum effects in the brain, quantum
> consciousness, macroscopic biological coherence beyond established regimes, and
> "logic as physics" unifications are tagged **CONTESTED** or **MODEL**. They are never
> used as load-bearing evidence for operational decisions.
>
> Biological recommendations are always organism-, state-, context-, and timescale-dependent.

## 0. C04 Knowledge Contract

### 0.1 Claim classes
- **VERIFIED** — strongly supported empirical result within a stated regime.
- **DERIVED** — logical consequence of stated premises/model.
- **MODEL** — representation useful within stated scope; includes all metaphorical mappings.
- **CONTESTED** — active scientific dispute; unresolved mechanism or evidence.
- **CONDITIONAL** — dependent on explicit assumptions, regime, or scenario.
- **UNKNOWN/GAP** — insufficient evidence or unresolved mechanism.

### 0.2 Evidence classes
`EXPERIMENT`, `OBSERVATION`, `CLINICAL`, `PHYSIOLOGICAL_MEASURE`, `DERIVED`, `MODEL`,
`METAPHOR`, `SOURCE_CLAIM`, `UNKNOWN`.

**Rule:** any claim resting on a biological *metaphor* (programs as organisms, companies as
bodies) is typed `MODEL/METAPHOR` at minimum and inherits the weakest edge in any chain.

### 0.3 C04 H-level ownership
1. Biological System Structure & Organization
2. Homeostasis, Regulation & Repair
3. Neuro & Signal Processing
4. Immune, Defense & Repair Capacity
5. Evolution, Adaptation & Learning
6. Bio-Social Coupling: Trust, Stress, Cooperation
7. Organizational Biological Models (Biological Programming, Quantum-Biological Business)
8. UBI Alignment & Bio-Realistic Governance
9. AMOS/Trang Biology Research Bridge & Neuro-Plausibility Firewall

A topic has one primary owner. Cross-links are references, not duplicated substantive sections.

### 0.4 Standard knowledge node schema
Where applicable:
**definition → state variables → governing relations → assumptions → mechanisms → observables →
data sources → empirical status → scope/regime → uncertainty → failure modes → competing models →
falsifiers → dependencies → decision relevance → AMOS bridge**.

---

# H1 — Biological System Structure & Organization

## M1. The Organism as a Layered System

### L1. Levels of organization [VERIFIED]
Biology analyzes organisms across nested levels:
- molecules and molecular assemblies;
- organelles;
- cells;
- tissues;
- organs;
- organ systems;
- organism;
- populations and ecosystems.

Levels are analytical partitions; causation runs both upward (emergence) and downward
(regulation). No single level fully explains system behavior.

### L2. Subsystem partition [MODEL]
AMOS models an organism (or organism-like system) with functional subsystems:
- **DNA/specification** — heritable instructions defining structure and behavior;
- **metabolism** — resource intake, conversion, allocation, waste removal;
- **nervous/communication** — signal transmission and coordination;
- **immune/defense** — threat detection, discrimination, response;
- **repair/maintenance** — damage correction and regeneration;
- **regulatory/meta layer** — self-monitoring and adaptation of the above.

This partition maps cleanly onto living systems; mapping it onto software systems or firms
is a **MODEL/METAPHOR** move governed by H7.

### L3. Stock-flow form [DERIVED]
Any biological stock `X` (energy reserve, cell population, hormone level, protein pool)
follows:
`dX/dt = Σ inflows − Σ outflows + production − degradation`.

Reliability of a bio-stock model depends on boundary choice and omitted pathways, exactly
as in Earth-system modeling.

---

## M2. Cells and Information

### L1. The cell as the basic unit [VERIFIED]
All known life is cellular. Cells maintain identity through membranes, regulated transport,
genome expression, and energy management (ATP-centered metabolism).

### L2. Central dogma with caveats [VERIFIED]
Genetic information flows DNA → RNA → protein, with well-established exceptions:
reverse transcription, RNA editing, epigenetic regulation, non-coding RNA function.
Genes are regulatory participants, not solo determinants; environment, development, and
stochasticity shape phenotype.

### L3. Epigenetics [VERIFIED]
Gene expression is modulated without altering sequence — methylation, histone modification,
chromatin state. Some marks are environmentally responsive and some are transgenerational in
model organisms. **CONTESTED** for strong transgenerational inheritance claims in humans.

---

## M3. Energy and Metabolism

### L1. Energy currency [VERIFIED]
Cells use ATP as the dominant short-term energy carrier. Metabolism comprises catabolism
(extracting energy) and anabolism (building structures). Energy budgets constrain everything
else: growth, repair, immunity, cognition.

### L2. Allocation trade-offs [VERIFIED]
Organisms face life-history trade-offs among growth, reproduction, maintenance, and storage.
Chronic stress shifts allocation toward immediate defense and away from repair and long-horizon
functions — this is a load-bearing principle reused throughout AMOS.

### L3. Metabolic failure modes [MODEL]
System-level metabolic failure appears as:
- resource starvation (input failure);
- conversion breakdown (processing failure);
- waste accumulation (removal failure);
- misallocation (regulation failure).

In AMOS organizational modeling these four failure classes are reused diagnostically
(H7), typed MODEL/METAPHOR.

---

# H2 — Homeostasis, Regulation & Repair

## M1. Homeostasis

### L1. Setpoints and regulation [VERIFIED]
Homeostasis is active maintenance of internal variables (temperature, pH, glucose,
osmolarity, ion concentrations) within viable ranges via negative feedback: sensor →
comparator against setpoint → effector correction.

### L2. Allostasis [VERIFIED]
Regulation is also *predictive*: the body anticipates demands and adjusts setpoints ahead of
perturbation (allostasis). Chronic anticipatory activation ("allostatic load") itself becomes
a pathology channel — sustained elevation of cortisol, blood pressure, inflammatory tone.

### L3. Feedback discipline [DERIVED]
- Negative feedback stabilizes; positive feedback amplifies.
- Biological positive feedback exists (blood clotting cascades, action-potential onset,
  inflammatory cascades) but is normally bounded by termination mechanisms.
- **AMOS law:** every amplifying loop must have an identifiable brake. An unbounded positive
  loop in a modeled bio-social system predicts cascade failure unless a brake is specified.

---

## M2. Stress Physiology

### L1. Stress response [VERIFIED]
Acute stress activates the sympathetic-adrenal-medullary axis (fast: adrenaline) and the
hypothalamic-pituitary-adrenal (HPA) axis (slower: cortisol). Acute responses mobilize
energy, sharpen attention, suppress non-essential functions.

### L2. Chronic stress [VERIFIED]
Sustained stress exposure degrades sleep, immune competence, memory consolidation,
cardiovascular health, and ethical self-regulation capacity. Chronic stress narrows
perception toward threat and shortens time horizons.

### L3. AMOS reuse rule [MODEL]
Any AMOS model of a human-bearing system (leader, governance body, team) must carry a
stress/capacity state variable. Systems designed assuming fatigue-resistant, stress-neutral
agents are classified **bio-unrealistic** and flagged at H8.

---

## M3. Repair and Regeneration

### L1. Repair hierarchy [VERIFIED]
Repair operates continuously at multiple scales: molecular (DNA repair enzymes, protein
chaperones, autophagy), cellular (membrane repair, apoptosis of damaged cells), tissue
(wound healing, regeneration varying widely by species and tissue).

### L2. Repair budget coupling [VERIFIED]
Repair competes for the same energy and resource budget as defense and activity.
Under-repair accumulates silently — damage is subclinical long before it is visible.
This motivates AMOS **silent-failure detection**: monitor repair indicators, not just
output indicators.

### L3. Sleep as systemic maintenance [VERIFIED]
Sleep performs memory consolidation, glymphatic clearance of metabolic waste in the brain,
and hormonal regulation. Sleep debt produces progressive, nonlinear judgment degradation.

---

# H3 — Neuro & Signal Processing

## M1. Neuronal Signaling

### L1. Action potentials [VERIFIED]
Neurons transmit information via electrochemical impulses: membrane potential dynamics,
threshold-triggered spikes, all-or-nothing propagation, refractory periods.

### L2. Synapses [VERIFIED]
Chemical synapses transmit via neurotransmitter release; effect can be excitatory or
inhibitory. Signal integration is convergent, divergent, and modulated by neuromodulators
(dopamine, serotonin, norepinephrine, acetylcholine) that change gain and mode rather than
carrying point-to-point messages.

### L3. Plasticity [VERIFIED]
Synaptic strength changes with activity — long-term potentiation/depression are core
mechanisms of learning and memory. Plasticity varies by developmental window, brain region,
and state (sleep, stress).

---

## M2. Brain Organization

### L1. Functional specialization with distribution [VERIFIED]
Brain functions are regionally biased but distributed; no strict one-function-one-region
mapping holds. Networks (default mode, salience, executive control) interact dynamically.

### L2. Prediction-oriented processing [MODEL, well-supported framing]
Modern neuroscience increasingly frames perception and action as prediction-driven:
the brain generates predictive models and updates on error signals (predictive processing).
Useful as an AMOS design frame for perception modules; mechanistic details remain debated.

### L3. Limits of measurement [VERIFIED]
Human cognitive-affective states cannot be read out reliably from single physiological
signals. Inference from heart-rate variability, skin conductance, or imaging to specific
mental states is probabilistic and population-dependent. **Firewall:** no AMOS module may
treat a physiological proxy as a direct readout of psychological content — that inference
belongs to C05 and requires its own evidence chain.

---

## M3. Nervous System States and Behavior

### L1. Autonomic states [VERIFIED]
Autonomic state (sympathetic arousal vs parasympathetic dominance) shapes available behavior:
threat states constrict options, narrow attention, bias risk perception; safe states free
resources for connection, creativity, and learning.

### L2. Emotion as regulation [MODEL]
The AMOS/QLS position treats emotion as a **coherence regulator** rather than logic's
opposite — emotional states modulate system consistency and prioritization. This is a useful
design abstraction grounded in affective-neuroscience evidence that emotion and reasoning
are integrated, not separable. Typed MODEL where it exceeds the evidence.

### L3. Perception as computation [MODEL]
Perception involves sensing, filtering, encoding, and prediction — treatable as biological
computation. Extending this into claims that "reality is nothing but biological computation"
or that the universe is informational substrate is **CONTESTED** philosophy-of-mind territory,
not operational knowledge.

---

# H4 — Immune, Defense & Repair Capacity

## M1. Immune Architecture

### L1. Innate and adaptive immunity [VERIFIED]
Innate immunity provides fast, generic responses (barriers, inflammation, phagocytes);
adaptive immunity provides slow, specific, memory-bearing responses (lymphocytes, antibodies).
Both depend on discrimination between self and non-self and on calibrated response magnitude.

### L2. Immunological memory [VERIFIED]
Adaptive immunity retains memory after exposure, enabling faster secondary responses.
This is the biological basis of vaccination and a canonical AMOS pattern for learning
defense systems: detect → respond → remember → respond faster next time.

### L3. Autoimmunity and overreaction [VERIFIED]
Immune failure has two directions: under-response (missed threats, immunodeficiency) and
over-response (autoimmunity, cytokine storms, allergy). **AMOS security analogy:** defense
systems fail both by missing attacks and by attacking the host. Any AMOS immune-layer design
must specify both false-negative and false-positive costs.

---

## M2. Trust and Immune Function

### L1. Chronic mistrust suppresses immunity [VERIFIED, moderate effect sizes]
Chronic social stress and mistrust correlate with suppressed immune function via sustained
cortisol and inflammatory dysregulation; perceived safety supports recovery. Effect sizes
are moderate and confounded by behavior, sleep, and SES; do not overstate.

### L2. Trust as energy reallocation [MODEL]
AMOS frames trust as an "energy-saving switch": when safety is established, the organism stops
threat-scanning and reallocates resources to growth, learning, and repair. Useful design
heuristic; typed MODEL because it compresses a multi-pathway physiology into one variable.

---

# H5 — Evolution, Adaptation & Learning

## M1. Evolutionary Dynamics

### L1. Variation, selection, retention [VERIFIED]
Evolution proceeds via heritable variation, differential reproductive success, and retention.
Fitness is environment-relative, not absolute; adaptations carry trade-offs.

### L2. Applied evolution in AMOS [MODEL]
AMOS reuses mutation–selection–retention for program and strategy evolution:
generate variants → evaluate fitness against environment → retain winners → control mutation
rate to avoid destructive drift. Uncontrolled mutation is always listed as an exclusion.

### L3. Fitness-landscape honesty [DERIVED]
Applied evolutionary optimization finds local fitness improvements within the explored
neighborhood. Claims of global optimality require justification; otherwise type as local
search result.

---

## M2. Learning and Memory

### L1. Consolidation [VERIFIED]
Memory formation involves encoding, consolidation (sleep-dependent), retrieval, and
reconsolidation. Memories are reconstructive, not verbatim recordings.

### L2. Organizational learning analog [MODEL]
AMOS durable-learning patterns mirror biological ones: encode (capture), consolidate
(rest/digest cycles, review), retrieve (test), reconsolidate (revise). Mapping to institutional
memory is MODEL/METAPHOR.

---

# H6 — Bio-Social Coupling: Trust, Stress, Cooperation

## M1. Trust as Biological Currency

### L1. Core thesis [MODEL, grounded in VERIFIED components]
Trust is treated as the primary currency of survival: the condition under which human systems
stabilize, cooperate, and grow.

Verified components underneath:
- trust/safety correlates with parasympathetic engagement (lower heart rate, restored digestion);
- oxytocin is associated with social bonding and reduced fear response;
- dopamine reinforces cooperative behavior;
- chronic mistrust/stress suppresses immune function;
- perceived psychological safety predicts team learning and creative output.

### L2. Cognitive effects of trust [VERIFIED, bounded]
Trust reduces monitoring overhead, speeds cooperation decisions, and improves information
sharing. It does not eliminate betrayal risk — high trust without verification is a distinct
failure mode (see amos-resilience-vs-control-tradeoff, owned elsewhere).

### L3. Trust at scale [MODEL]
At scale, trust acts as an information amplifier: trusted signals propagate with less
verification cost. This also means trusted-but-wrong signals propagate efficiently —
scale amplification cuts both ways.

---

## M2. Governance Under Biological Constraints

### L1. The foundational error [MODEL, built on VERIFIED limits]
Governance theory often assumes humans who are cognitively stable, emotionally neutral,
fatigue-resistant, consistent under pressure. Real humans are biologically bounded,
emotionally contagious, cognitively biased, stress-reactive, capacity-limited.
The gap between assumption and reality is where governance fails.

### L2. Verified limit mechanisms [VERIFIED]
- Attention saturates; critical information gets missed under overload.
- Sleep debt progressively degrades judgment (nonlinear).
- Acute stress narrows perception; option space collapses (tunnel vision).
- Error rates rise non-linearly with sustained overload.
- Chronic pressure erodes ethical thresholds over time.

**No legal framework overrides cortisol** — institutional rules cannot abolish the physiology
of the people executing them.

### L3. Leadership as a biological act [MODEL, grounded in VERIFIED mechanisms]
Every strategic decision executes through a nervous system. Documented distortions under
stress/fatigue/overload: risk underestimated, trade-offs invisible, long horizons discounted,
complexity oversimplified.

Pressure amplifiers:
| Amplifier | Mechanism | Systemic effect |
|---|---|---|
| Urgency | Suppresses dissent | Silence, not alignment |
| Charisma | Discourages questioning | Compliance without agreement |
| Speed | Bypasses review | Unchecked decisions |

Silence under pressure is one of the most reliable early predictors of downstream systemic
failure. Burnout at the top is a systemic risk: burned-out leaders fail quietly —
oversimplifying, delegating responsibility without authority, optimizing short-term metrics.

### L4. Responsibility vs accountability [DEFINITIONAL]
Responsibility = obligation to act. Accountability = obligation to answer for outcomes.
Systems that separate them produce authority-without-accountability or accountability-
without-authority — both are structural failure configurations.

---

# H7 — Organizational Biological Models

## M1. Biological Programming Paradigm

### L1. Definition [MODEL/METAPHOR — explicit]
Biological Programming designs software as organisms: DNA = immutable specifications;
metabolism = resource management; nervous system = inter-component communication;
immune system = threat detection/security; consciousness = meta-reasoning/self-monitoring.
Distinct from OOP/functional/procedural paradigms by organizing around organism subsystems
rather than objects/functions/procedures.

### L2. Operations [MODEL]
- `design_organism(spec)` — define DNA, metabolism, communication wiring, immune config, meta-layer.
- `evolve_organism(organism, environment)` — assess fitness, propose mutations, verify viability,
  deploy; **exclusion: uncontrolled mutation**.

### L3. Anti-overclaim [BOUNDARY]
Programs are not alive and do not metabolize. The paradigm's value is diagnostic structure
(what does this program's "immune layer" look like? where is its "waste removal"?) —
not literal biological equivalence.

---

## M2. Quantum-Biological Model of Business

### L1. Mapping table [MODEL/METAPHOR — explicit]
| Business element | Biological/quantum equivalent | Function |
|---|---|---|
| Cash flow / capital | Energy flow / current | Circulates resources |
| Innovation / execution | Consciousness | Generates and enacts novelty |
| Strategy / market position | Field / probability cloud | Collapses possibilities into chosen direction |
| Leadership / governance | Observer / measurement | Determines when choices collapse into action |
| Relationships / trust | Entanglement / bonding | Resilient connections under stress |
| Culture / values | DNA / genetic code | Identity and replication rules |
| Operations / processes | Metabolism | Converts inputs into usable energy |

### L2. Diagnostic use [MODEL]
Organizational health failures decompose as:
1. metabolic failure (operations cannot convert resources);
2. immune failure (cannot detect/repel threats);
3. neural failure (decision-making slow or corrupted);
4. reproductive failure (cannot spawn new products/teams).

These map onto DMER categories (distinction quality = neural; repair capacity = immune;
entropy load = metabolic; trajectory = reproductive/directional).

### L3. Hard anti-overclaim [BOUNDARY]
Businesses are not organisms and do not obey quantum mechanics. All mappings here are
**MODEL/METAPHOR** generating diagnostic questions, never physical predictions.
No AMOS decision may cite "quantum entanglement of teams" or similar as causal evidence.

---

## M3. Origin-of-Logic Framework

### L1. Claim structure [CONTESTED/MODEL — explicit]
The QLS-derived framework proposes: logic is not symbolic manipulation but the architecture
by which energy, information, and life maintain consistency; the nervous system materializes
logic rather than computing it; emotion regulates coherence; ethics emerges from consistency
applied to social systems.

### L2. Status split [TYPED]
- Usable as **design lens**: treat emotion as regulator not noise; ground rules in consistency;
  prefer compression/minimal entropy formulations. Type: MODEL.
- As **physics/metaphysics claim** (universe as informational constant, logic-as-energy):
  CONTESTED. Not load-bearing anywhere in AMOS operational chains.

---

# H8 — UBI Alignment & Bio-Realistic Governance

## M1. UBI (Unified Biological Intelligence) Alignment

### L1. Principle [MODEL, canon]
UBI alignment requires AMOS constructs to be compatible with verified biological constraints:
bounded attention, stress-reactivity, sleep dependence, social-safety dependence of cognition,
energy-budget realism.

### L2. Alignment checks [OPERATIONAL]
A design passes UBI alignment only if:
1. no component assumes unlimited human attention or stamina;
2. stress/load states are represented where humans bear decisions;
3. safety/trust conditions are prerequisites for creative/high-cognition modes, not optional;
4. repair/recovery cycles are scheduled, not squeezed;
5. feedback loops include brakes.

### L3. Failure signature [DERIVED]
Bio-unrealistic designs exhibit: chronic urgency normalization, silence as compliance,
burnout treated as individual weakness, review steps removed "for speed", ethics erosion
treated as scandal rather than predicted degradation.

---

## M2. Bio-Realistic Institutional Design

### L1. Design moves [MODEL, grounded in H6]
- Decision-load caps and mandatory recovery windows for high-stakes roles.
- Dissent channels protected structurally (anonymous, delayed-review) so urgency/charisma
  cannot suppress them.
- Accountability paired explicitly with authority.
- Monitoring of leading biological indicators (silence rate, escalation latency, review bypass
  frequency) rather than only outcome metrics.

### L2. Escalation rule [DERIVED]
When biological-limit indicators degrade, reduce decision scope before increasing speed —
the opposite of the instinctive crisis response, which is precisely the failure mode.

---

# H9 — AMOS/Trang Biology Research Bridge & Neuro-Plausibility Firewall

## M1. Cross-Domain Reference Bridge

**Canonical references:** `AMOS_C05_mind_behavior`, `AMOS_C03_physics_cosmos`,
`AMOS_CC05_mind_behavior`.

C04 owns biological/neurological mechanism, homeostasis, repair, immune architecture,
bio-social coupling, and biological-modeling frameworks. C05 owns psychological/behavioral
constructs; C03 owns physical law. Boundaries are preserved.

```yaml
cross_domain_refs:
  - id: AMOS_CC05_mind_behavior
    relation: biology_underpins_behavior
    direction: bidirectional
    ownership_rule: preserve_domain_boundaries
    causal_status: mediated_not_assumed
    confidence_rule: weakest_load_bearing_edge
  - id: AMOS_C03_physics_cosmos
    relation: contested_quantum_biology_claims
    direction: outbound_reference_only
    status_rule: CONTESTED_or_MODEL_only
```

## M2. Neuro-Plausibility Firewall

Claims are routed by class:

| Claim class | Example | Routing |
|---|---|---|
| VERIFIED physiology | HPA axis, synaptic plasticity, immune memory | Usable as evidence |
| Well-supported framing | Predictive processing, allostasis | Usable, cite as framing |
| MODEL/METAPHOR | Programs-as-organisms, business metabolism | Design lens only |
| CONTESTED | Quantum effects in cognition, strong human transgenerational epigenetics | Never load-bearing |
| Pseudoscience-adjacent | "Quantum consciousness proves X", vibration healing claims | Blocked |

Rules:
1. No AMOS conclusion may rest on CONTESTED biology without an independent verified path.
2. Metaphorical mappings must be labeled at first use in any artifact.
3. Physiological proxies never substitute for psychological measurements (C05 handoff required).
4. Confidence of any mediated chain ≤ weakest load-bearing edge.

## M3. Causal Firewall

Do not infer biological causation from correlation alone, single-case anecdotes, or
mechanistic plausibility alone. Prefer: controlled experiment, longitudinal cohort,
convergent independent evidence, dose-response, falsifiable predictions.

## M4. Monitoring-to-Repair Loop

```text
observe bio-indicators (load, sleep, silence, review-bypass, error rate)
→ validate against baseline
→ compare against thresholds
→ update capacity estimate
→ test competing explanations (load vs skill vs incentive)
→ identify decision-changing uncertainty
→ choose reversible intervention (scope reduction first)
→ monitor recovery
→ revise
```

---

# C04 Master Dependency Spine

```text
molecular & cellular foundations
            ↓
metabolism + energy budgets
            ↓
homeostasis ↔ stress ↔ repair cycles
            ↓
neural signaling + plasticity
            ↓
immune defense (detect / respond / remember / calibrate)
            ↓
evolution + learning (variation / selection / retention)
            ↓
bio-social coupling: trust, stress contagion, cooperation
            ↓
organizational biological models (programming, business, leadership)
            ↓
UBI alignment + bio-realistic governance
            ↓
neuro-plausibility firewall + AMOS cross-domain bridge
```

# C04 Decision Capsule Template

```text
System:
Boundary:
Organism/system scale:
Timescale:
Decision:
Irreversibility:
Biological state variables (stress/load/sleep/trust):
Homeostatic ranges assumed:
Feedback loops (with brakes):
Defense layer (false-negative vs false-positive cost):
Repair capacity and budget:
Data sources:
Data freshness:
Claim typing (VERIFIED/MODEL/CONTESTED per node):
Metaphor labels declared:
Competing explanations:
Weakest load-bearing edge:
Decision-sensitive uncertainty:
Least-regret actions:
Triggers for scope reduction:
Monitoring plan:
Falsifiers:
Revalidation date:
```

# C04 Promotion Rule

A new biology/neuro claim may move from `MODEL` toward stronger status only when:
1. terms and system boundary are operationally defined;
2. organism/regime/timescale scope is explicit;
3. data provenance and uncertainty are stated;
4. metaphorical mappings are separated from empirical findings;
5. competing explanations are considered;
6. causal claims identify mechanism and confounders;
7. contested-class content remains quarantined regardless of fluency;
8. physiological→psychological inferences route through C05 with their own evidence;
9. recommendations affecting human load/burnout undergo stronger validation;
10. governance records contradiction, supersession, and revalidation.

# C04 Final Boundary

C04 is not a medical authority, a consciousness oracle, or a license to dress speculation in
biological vocabulary.

Its purpose is to maintain a disciplined map connecting verified biology — homeostasis,
repair, neural signaling, immunity, evolution — to AMOS system design, while keeping
metaphors labeled and contested claims quarantined.

The architecture should remain open and repairable:
**integrity > completeness > fluency > speed**.

---

00_ROOT_MOC|AMOS MOC

---
**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: amos_c04_bio_neuro_master_knowledge
node_type: note
path: 11_KNOWLEDGE/AMOS_C04_BIO_NEURO_MASTER_KNOWLEDGE.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_HOME]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL

---
**MOC:** [[KNOWLEDGE_MOC]]
