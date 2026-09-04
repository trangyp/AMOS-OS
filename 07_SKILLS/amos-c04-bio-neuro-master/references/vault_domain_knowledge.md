---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Vault Domain Knowledge
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

# amos-c04-bio-neuro-master — Vault-Sourced Domain Knowledge

> Load this reference only when detailed domain knowledge is needed.
> This content was moved from SKILL.md for progressive loading.

______________________________________________________________________

> **Source**: `11_KNOWLEDGE/AMOS_C04_BIO_NEURO_MASTER_KNOWLEDGE.md` from the AMOS_OS Obsidian vault.
> This is substantive domain knowledge, not script-generated content.

## AMOS C04 — Biology & Neuro Master Knowledge

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
1. Homeostasis, Regulation & Repair
1. Neuro & Signal Processing
1. Immune, Defense & Repair Capacity
1. Evolution, Adaptation & Learning
1. Bio-Social Coupling: Trust, Stress, Cooperation
1. Organizational Biological Models (Biological Programming, Quantum-Biological Business)
1. UBI Alignment & Bio-Realistic Governance
1. AMOS/Trang Biology Research Bridge & Neuro-Plausibility Firewall

A topic has one primary owner. Cross-links are references, not duplicated substantive sections.

### 0.4 Standard knowledge node schema

Where applicable:
**definition → state variables → governing relations → assumptions → mechanisms → observables →
data sources → empirical status → scope/regime → uncertainty → failure modes → competing models →
falsifiers → dependencies → decision relevance → AMOS bridge**.

______________________________________________________________________

## H1 — Biological System Structure & Organization

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

______________________________________________________________________

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

______________________________________________________________________

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

______________________________________________________________________

## H2 — Homeostasis, Regulation & Repair

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

______________________________________________________________________

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

______________________________________________________________________

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

______________________________________________________________________

## H3 — Neuro & Signal Processing

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

______________________________________________________________________

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

______________________________________________________________________

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

______________________________________________________________________

## H4 — Immune, Defense & Repair Capacity

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

______________________________________________________________________

## M2. Trust and Immune Function

### L1. Chronic mistrust suppresses immunity [VERIFIED, moderate effect sizes]

Chronic social stress and mistrust correlate with suppressed immune function via sustained
cortisol and inflammatory dysregulation; perceived safety supports recovery. Effect sizes
are moderate and confounded by behavior, sleep, and SES; do not overstate.

### L2. Trust as energy reallocation [MODEL]

AMOS frames trust as an "energy-saving switch": when safety is established, the organism stops
threat-scanning and reallocates resources to growth, learning, and repair. Useful design
heuristic; typed MODEL because it compresses a multi-pathway physiology into one variable.

______________________________________________________________________

## H5 — Evolution, Adaptation & Learning

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

______________________________________________________________________

## M2. Learning and Memory

### L1. Consolidation [VERIFIED]

Memory formation involves encoding, consolidation (sleep-dependent), retrieval, and
reconsolidation. Memories are reconstructive, not verbatim recordings.

### L2. Organizational learning analog [MODEL]

AMOS durable-learning patterns mirror biological ones: encode (capture), consolidate
(rest/digest cycles, review), retrieve (test), reconsolidate (revise). Mapping to institutional
memory is MODEL/METAPHOR.

______________________________________________________________________

## H6 — Bio-Social Coupling: Trust, Stress, Cooperation

## M1. Trust as Biological Currency

### L1. Core thesis [MODEL, grounded in VERIFIED components]

Trust is treated as the primary currency of survival: the condition under which human systems
stabilize, cooperate, and grow.

Verified components underneath:

- trust

## Vault-Sourced Domain Content

> Source: `11_KNOWLEDGE/AMOS_C04_BIO_NEURO_MASTER_KNOWLEDGE.md` (29455 bytes in vault)

### 0.1 Claim Classes

- **VERIFIED** — strongly supported empirical result within a stated regime.
- **DERIVED** — logical consequence of stated premises/model.
- **MODEL** — representation useful within stated scope; includes all metaphorical mappings.
- **CONTESTED** — active scientific dispute; unresolved mechanism or evidence.
- **CONDITIONAL** — dependent on explicit assumptions, regime, or scenario.
- **UNKNOWN/GAP** — insufficient evidence or unresolved mechanism.

### 0.2 Evidence Classes

`EXPERIMENT`, `OBSERVATION`, `CLINICAL`, `PHYSIOLOGICAL_MEASURE`, `DERIVED`, `MODEL`,
`METAPHOR`, `SOURCE_CLAIM`, `UNKNOWN`.

**Rule:** any claim resting on a biological *metaphor* (programs as organisms, companies as
bodies) is typed `MODEL/METAPHOR` at minimum and inherits the weakest edge in any chain.

### 0.4 Standard Knowledge Node Schema

Where applicable:
**definition → state variables → governing relations → assumptions → mechanisms → observables →
data sources → empirical status → scope/regime → uncertainty → failure modes → competing models →
falsifiers → dependencies → decision relevance → AMOS bridge**.

______________________________________________________________________

## H1 — Biological System Structure & Organization — part 2

### L3. Metabolic Failure Modes [Model]

System-level metabolic failure appears as:

- resource starvation (input failure);
- conversion breakdown (processing failure);
- waste accumulation (removal failure);
- misallocation (regulation failure).

In AMOS organizational modeling these four failure classes are reused diagnostically
(H7), typed MODEL/METAPHOR.

______________________________________________________________________

## H2 — Homeostasis, Regulation & Repair — part 2

### L3. Feedback Discipline [Derived]

- Negative feedback stabilizes; positive feedback amplifies.
- Biological positive feedback exists (blood clotting cascades, action-potential onset,
  inflammatory cascades) but is normally bounded by termination mechanisms.
- **AMOS law:** every amplifying loop must have an identifiable brake. An unbounded positive
  loop in a modeled bio-social system predicts cascade failure unless a brake is specified.

______________________________________________________________________

### L1. Repair Hierarchy [Verified]

Repair operates continuously at multiple scales: molecular (DNA repair enzymes, protein
chaperones, autophagy), cellular (membrane repair, apoptosis of damaged cells), tissue
(wound healing, regeneration varying widely by species and tissue).

### L2. Repair Budget Coupling [Verified]

Repair competes for the same energy and resource budget as defense and activity.
Under-repair accumulates silently — damage is subclinical long before it is visible.
This motivates AMOS **silent-failure detection**: monitor repair indicators, not just
output indicators.

### L2. Immunological Memory [Verified]

Adaptive immunity retains memory after exposure, enabling faster secondary responses.
This is the biological basis of vaccination and a canonical AMOS pattern for learning
defense systems: detect → respond → remember → respond faster next time.

### L2. Cognitive Effects Of Trust [Verified, Bounded]

Trust reduces monitoring overhead, speeds cooperation decisions, and improves information
sharing. It does not eliminate betrayal risk — high trust without verification is a distinct
failure mode (see amos-resilience-vs-control-tradeoff, owned elsewhere).

### L2. Operations [Model]

- `design_organism(spec)` — define DNA, metabolism, communication wiring, immune config, meta-layer.
- `evolve_organism(organism, environment)` — assess fitness, propose mutations, verify viability,
  deploy; **exclusion: uncontrolled mutation**.

### L3. Anti-Overclaim [Boundary]

Programs are not alive and do not metabolize. The paradigm's value is diagnostic structure
(what does this program's "immune layer" look like? where is its "waste removal"?) —
not literal biological equivalence.

______________________________________________________________________

### L3. Hard Anti-Overclaim [Boundary]

Businesses are not organisms and do not obey quantum mechanics. All mappings here are
**MODEL/METAPHOR** generating diagnostic questions, never physical predictions.
No AMOS decision may cite "quantum entanglement of teams" or similar as causal evidence.

______________________________________________________________________

### L2. Status Split [Typed]

- Usable as **design lens**: treat emotion as regulator not noise; ground rules in consistency;
  prefer compression/minimal entropy formulations. Type: MODEL.
- As **physics/metaphysics claim** (universe as informational constant, logic-as-energy):
  CONTESTED. Not load-bearing anywhere in AMOS operational chains.

______________________________________________________________________

## H8 — UBI Alignment & Bio-Realistic Governance

### L1. Principle [Model, Canon]

UBI alignment requires AMOS constructs to be compatible with verified biological constraints:
bounded attention, stress-reactivity, sleep dependence, social-safety dependence of cognition,
energy-budget realism.

### M2. Neuro-Plausibility Firewall

Claims are routed by class:

| Claim class            | Example                                                                  | Routing                 |
| ---------------------- | ------------------------------------------------------------------------ | ----------------------- |
| VERIFIED physiology    | HPA axis, synaptic plasticity, immune memory                             | Usable as evidence      |
| Well-supported framing | Predictive processing, allostasis                                        | Usable, cite as framing |
| MODEL/METAPHOR         | Programs-as-organisms, business metabolism                               | Design lens only        |
| CONTESTED              | Quantum effects in cognition, strong human transgenerational epigenetics | Never load-bearing      |
| Pseudoscience-adjacent | "Quantum consciousness proves X", vibration healing claims               | Blocked                 |

Rules:

1. No AMOS conclusion may rest on CONTESTED biology without an independent verified path.
1. Metaphorical mappings must be labeled at first use in any artifact.
1. Physiological proxies never substitute for psychological measurements (C05 handoff required).
1. Confidence of any mediated chain ≤ weakest load-bearing edge.

### M3. Causal Firewall

Do not infer biological causation from correlation alone, single-case anecdotes, or
mechanistic plausibility alone. Prefer: controlled experiment, longitudinal cohort,
convergent independent evidence, dose-response, falsifiable predictions.

### M4. Monitoring-To-Repair Loop

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

______________________________________________________________________

## C04 Master Dependency Spine

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

## C04 Decision Capsule Template

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

## C04 Promotion Rule

A new biology/neuro claim may move from `MODEL` toward stronger status only when:

1. terms and system boundary are operationally defined;
1. organism/regime/timescale scope is explicit;
1. data provenance and uncertainty are stated;
1. metaphorical mappings are separated from empirical findings;
1. competing explanations are considered;
1. causal claims identify mechanism and confounders;
1. contested-class content remains qua

... (truncated, see vault source for full content)

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

______________________________________________________________________

**MOC:** references_MOC

## Related

- [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · references_MOC · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**MOC:** references_MOC

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-c04-bio-neuro-master-vault-domain-knowledge
node_type: reference
path: 07_SKILLS/amos-c04-bio-neuro-master/references/vault_domain_knowledge.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: references_MOC
