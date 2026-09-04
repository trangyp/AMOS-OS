---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Skill
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

# AMOS C01 — Meta-Logic Master Knowledge

## Identity

Origin architect and steward: **Trang Phan**.

This is a **parent skill** that consolidates 60 sub-skills into a single domain master.
Following the skill-organizer best practice: fewer, richer skills beat many overlapping ones.
A parent skill with clearly labeled sections is better than 60 separate shallow skills.

**Epistemic class**: SOURCE_CLAIM (vault-sourced from `11_KNOWLEDGE/AMOS_C01_META_LOGIC_MASTER_KNOWLEDGE.md` (content_hash: ff5575df755d7e25)).

## When to Use

- When clarifying questions, cleaning concepts, detecting contradictions, or choosing correct frames

- When decomposing problems into minimal coherent assumptions

- When selecting, combining, or disabling reasoning frameworks based on problem type

- When maintaining epistemic hygiene across domains and timescales

- When producing deterministic, auditable reasoning traces

- When a child skill routes a logic, decomposition, or meta-law task to this master

- When managing lifecycle operations across classify, validate, trace, assess, and detect

- When detecting drift in evidence chains, provenance freshness, or confidence calibration

- When validating outputs against domain constraints and epistemic class

## Capabilities

- **c01.question_decompose**: F01 — Decompose raw questions into minimal coherent sub-questions before inference. Detect multiple questions packed into one prompt, separate goals from constraints, identify missing information, normalize terminology against canon.
- **c01.concept_hygiene**: F02 — Build definition tables for load-bearing terms. Map same-word/multiple-meaning collisions across domains. Replace soft language with structural terms where precision matters. Stabilize glossaries against semantic drift.
- **c01.assumption_graph**: F03 — Surface hidden assumptions from text. Label as facts/estimates/hypotheses/placeholders. Link each to source. Detect assumption collisions between frameworks. Enforce precision discipline (output precision must match input uncertainty).
- **c01.frame_selection**: F04 — List candidate frameworks for problem type. Check compatibility before combining. Govern frame switching (legitimate = problem class changes or current frame fails; frame-shopping = undocumented switching to avoid contradiction). Declare logic mode (deductive/abductive/paraconsistent) pre-inference per Gate G1.
- **c01.reasoning_trace**: F05 — Produce deterministic, auditable traces: mode selected, assumptions active, definitions in force, operators applied, gates passed/failed, binding decisions. Trace without these is narrative, not audit material. Budget trace depth against decision value (F08).
- **c01.conflict_detection**: F06 — Detect structural contradictions. Classify as definitional/evidential/framework conflicts. Apply paraconsistent honesty: same-scope contradiction = real, requires repair; cross-scope = record both with regime tags, neither discarded. Examine deeper assumptions, not coin-flip outputs.
- **c01.meta_strategy**: F07 — Set precision mode (low/medium/high). Select exact vs approximate methods. Choose symbolic vs numeric representation. Govern error-budget allocation. Coordinate multiple reasoning threads. Select/disable cognitive clusters by problem type.
- **c01.uncertainty_tracking**: F08 — Hold competing hypotheses simultaneously; do not collapse to favorite before evidence forces collapse. Track each hypothesis's status, supporting evidence, disconfirming evidence separately. Estimate information value BEFORE pursuing it. Overfitting guardrail: domain context is prerequisite, not optional.
- **c01.binding_analysis**: F09 — The Binding Problem: when does a meta-level finding constrain an object-level claim? Binding requires showing the meta-defect touched the specific inference path to THIS conclusion. Meta findings without traced path = observations, not objections. Detect self-reference loops (G4).
- **c01.root_commitments**: F10 — Map complex concepts to 19 irreducible primitives (State, Transition, Boundary, Force, Capacity, ...). Apply 19×19 interaction matrix. Use 6 pattern primitives (Recurrence, Boundary, Coupling, Gradient, Cycle, Hierarchy) and 6 universal operators (Combine ⊕, Separate ⊖, Transform ⊗, Partition ⊨, Abstract ∇, Instantiate Δ⁻¹) with integrity constraints.

## Operations

1. **c01.question_decompose**: F01 — Decompose raw questions into minimal coherent sub-questions before inference. Detect multiple questions packed into one prompt, separate goals from constraints, identify missing information, normalize te...
1. **c01.concept_hygiene**: F02 — Build definition tables for load-bearing terms. Map same-word/multiple-meaning collisions across domains. Replace soft language with structural terms where precision matters. Stabilize glossaries against se...
1. **c01.assumption_graph**: F03 — Surface hidden assumptions from text. Label as facts/estimates/hypotheses/placeholders. Link each to source. Detect assumption collisions between frameworks. Enforce precision discipline (output precision...
1. **c01.frame_selection**: F04 — List candidate frameworks for problem type. Check compatibility before combining. Govern frame switching (legitimate = problem class changes or current frame fails; frame-shopping = undocumented switching t...
1. **c01.reasoning_trace**: F05 — Produce deterministic, auditable traces: mode selected, assumptions active, definitions in force, operators applied, gates passed/failed, binding decisions. Trace without these is narrative, not audit mater...
1. **c01.conflict_detection**: F06 — Detect structural contradictions. Classify as definitional/evidential/framework conflicts. Apply paraconsistent honesty: same-scope contradiction = real, requires repair; cross-scope = record both with r...
1. **c01.meta_strategy**: F07 — Set precision mode (low/medium/high). Select exact vs approximate methods. Choose symbolic vs numeric representation. Govern error-budget allocation. Coordinate multiple reasoning threads. Select/disable cogn...
1. **c01.uncertainty_tracking**: F08 — Hold competing hypotheses simultaneously; do not collapse to favorite before evidence forces collapse. Track each hypothesis's status, supporting evidence, disconfirming evidence separately. Estimate i...
1. **c01.binding_analysis**: F09 — The Binding Problem: when does a meta-level finding constrain an object-level claim? Binding requires showing the meta-defect touched the specific inference path to THIS conclusion. Meta findings without t...
1. **c01.root_commitments**: F10 — Map complex concepts to 19 irreducible primitives (State, Transition, Boundary, Force, Capacity, ...). Apply 19×19 interaction matrix. Use 6 pattern primitives (Recurrence, Boundary, Coupling, Gradient, Cy...

## Vault-Sourced Domain Knowledge

> **Source**: `11_KNOWLEDGE/AMOS_C01_META_LOGIC_MASTER_KNOWLEDGE.md` (content_hash: ff5575df755d7e25) (vault canon, SOURCE_CLAIM)

### Source Family Mapping

The domain is organized into source families:

- **F01**: Problem framing
- **F02**: Concept hygiene
- **F03**: Assumption graphs
- **F04**: Multi-frame control
- **F05**: Reasoning traces
- **F06**: Conflict detection
- **F07**: Meta-strategic logic
- **F08**: Uncertainty and risk
- **F09**: Temporal meta-logic and binding
- **F10**: Root commitments and universal operators

### Major Knowledge Modules

- M1: Question Decomposition — definitions before reasoning
- M2: Surfacing and Typing Assumptions — assumption graphs
- M3: Frame Selection — logic-mode selection (C01 Super)
- M4: Auditable Traces — root commitments (Logic Root), consistency checking
- M5: Meta-Control Layer — multi-hypothesis tracking
- M6: The Binding Problem — self-reference hazards, temporal meta-logic
- M7: Absolute Logic Model grounding — Identity Law v0, core pattern basis
- M8: Universal Operators — monitoring & hygiene loop, epistemic firewall

### Epistemic Classification

- **Conclusion class**: MIXED (established science + model projections + AMOS synthesis)
- **Evidence policy**: typed_per_node (each claim carries its own evidence type)
- **Canon status**: DOMAIN_KNOWLEDGE_WITH_RESEARCH_BRIDGES
- **Architecture**: HML_fractal_single_file (H/M/L cross-scale reasoning)

### Epistemic Boundary

C01 governs the QUALITY of reasoning processes, not the content of the world. Absolute Logic Model is canon-as-declared within AMOS, not a published mathematical theorem. Symbolic equality ≠ empirical equality. Identity Law v0 is SOURCE_CLAIM. C01 is not a truth oracle and not a source of authority.

## Reasoning Procedure — F01→F10 Pipeline with P1 Reality Contact Loop

> This is the actual execution path, not metadata. Each step uses a domain family from the vault knowledge and passes through the P1 Reality Contact Loop (per `01_CANON/02_UNIVERSE_CANON/P1_REALITY_ENVIRONMENT.md` §26).

### Step 1: Question Decomposition (F01)

**Precondition**: Raw question received.
**Operation**: Detect multiple questions packed into one. Separate goals from constraints. Identify missing information. Normalize terminology against canon. Define success criteria.
**P1 Gate**: Is the decomposed question touchable by observation? If not → UNKNOWN/GAP, not a fabricated answer.
**Self-audit (SAVER)**: Did I accept the asker's framing without challenge? If yes → restart, flag frame-shopping risk.
**Effect**: Clean sub-questions with explicit success criteria.

### Step 2: Concept Hygiene (F02)

**Precondition**: Clean sub-questions from Step 1.
**Operation**: Build definition tables for all load-bearing terms. Map same-word/multiple-meaning collisions. Replace soft language with structural terms. Stabilize glossary.
**P1 Gate**: Does any term silently change referent mid-chain? If yes → every downstream conclusion about that term is unbound (L0 integrity violation).
**Self-audit**: Am I allowing mixed jargon from multiple domains without disambiguation? If yes → this is the most common silent corruption in cross-domain analysis.
**Effect**: Definition table with stable referents.

### Step 3: Assumption Graph (F03)

**Precondition**: Stable definitions from Step 2.
**Operation**: Surface hidden assumptions. Label as facts/estimates/hypotheses/placeholders. Link each to source. Detect assumption collisions. Enforce precision discipline.
**P1 Gate**: Are estimates being treated as facts? Is output precision matching input uncertainty? If precision > uncertainty → false precision hazard.
**Self-audit**: Did I fail to update assumptions when new evidence arrived? Are unlabeled claims present? (Unlabeled = hygiene violation, not style issue.)
**Effect**: Typed assumption graph with epistemic labels.

### Step 4: Frame Selection (F04)

**Precondition**: Typed assumptions from Step 3.
**Operation**: List candidate frameworks. Check compatibility before combining. Declare logic mode (deductive/abductive/paraconsistent) pre-inference. **Gate G1**: Mode declared pre-inference is mandatory; retroactive mode assignment cannot rescue a chain.
**P1 Gate**: Is frame switching legitimate (problem class changed or current frame failed) or frame-shopping (undocumented switching to avoid contradiction)? Frame-shopping invalidates downstream confidence.
**Self-audit**: Am I treating an AMOS MODEL claim as an empirical observation because both appear in one document? If yes → structural error, not stylistic.
**Effect**: Declared framework + logic mode with rationale.

### Step 5: Reasoning Trace (F05)

**Precondition**: Declared frame from Step 4.
**Operation**: Execute reasoning with auditable trace: mode selected, assumptions active, definitions in force, operators applied, gates passed/failed, binding decisions. Budget trace depth against decision value (F08).
**P1 Gate**: Does the trace record all required properties? A trace without mode/assumptions/definitions/operators/gates is narrative, not audit material.
**Self-audit**: Is unbounded meta-analysis making this too slow? Budget check: trace depth vs decision value.
**Effect**: Auditable reasoning trace.

### Step 6: Conflict Detection (F06)

**Precondition**: Reasoning trace from Step 5.
**Operation**: Detect structural contradictions. Classify: definitional / evidential / framework. Apply paraconsistent honesty: same-scope = real contradiction requiring repair; cross-scope = record both with regime tags, neither discarded.
**P1 Gate**: Am I treating all contradictions as fatal (destroys multi-regime reasoning) or none as fatal (destroys validity)? Both are errors.
**Self-audit**: Did I examine deeper assumptions, or did I coin-flip outputs? Conflicts often live at the assumption level.
**Effect**: Classified conflicts with scope tags.

### Step 7: Meta-Strategy (F07)

**Precondition**: Classified conflicts from Step 6.
**Operation**: Set precision mode. Select exact vs approximate. Choose symbolic vs numeric. Govern error-budget. Coordinate threads. Select/disable cognitive clusters.
**P1 Gate**: Is the meta-reasoner over-normalizing and stripping useful nuance? Is there a clear alignment objective to avoid empty abstraction?
**Self-audit**: Am I flagging hidden assumptions in a way that exposes discomfort but adds value? Or just adding overhead?
**Effect**: Precision mode + method selection + thread coordination.

### Step 8: Uncertainty Tracking (F08)

**Precondition**: Meta-strategy from Step 7.
**Operation**: Hold competing hypotheses simultaneously. Do NOT collapse to favorite before evidence forces collapse. Track each hypothesis's status, supporting evidence, disconfirming evidence separately. Estimate information value BEFORE pursuing it.
**P1 Gate**: Am I collapsing competing hypotheses prematurely? L1.05: incompatible hypotheses with equal support stay COMPETING — no forced convergence. Am I purchasing low-value certainty? Low-value certainty purchases are resource failure even when they succeed.
**Self-audit**: Without domain context, am I fitting noise? Domain context is prerequisite, not optional refinement.
**Effect**: Multi-hypothesis tracker with information-value estimates.

### Step 9: Binding Analysis (F09)

**Precondition**: Multi-hypothesis tracker from Step 8.
**Operation**: The Binding Problem — when does a meta-level finding constrain an object-level claim? Binding requires showing the meta-defect touched the specific inference path to THIS conclusion. Meta findings without traced path = observations, not objections. **Gate G3**: Meta→object leaps explained. **Gate G4**: Self-reference loops flagged.
**P1 Gate**: Am I treating meta findings as objections without tracing the path to the object claim? That's overclaim-by-audit. "You reasoned in deductive mode" does NOT weaken a conclusion whose content happens to be true.
**Self-audit**: Is there unbounded self-reference? Unbounded self-reference produces triviality or paradox; both are hazards, not insights.
**Effect**: Bound meta-findings with traced paths; unbound findings recorded as observations.

### Step 10: Root Commitments (F10)

**Precondition**: Bound findings from Step 9.
**Operation**: Map complex concepts to 19 irreducible primitives. Apply 19×19 interaction matrix. Use 6 pattern primitives (Recurrence, Boundary, Coupling, Gradient, Cycle, Hierarchy) with false-positive awareness. Apply 6 universal operators (⊕ ⊖ ⊗ ⊨ ∇ Δ⁻¹) with integrity constraints.
**P1 Gate**: Is the Absolute Logic Model being treated as a published mathematical theorem? It is canon-as-declared within AMOS, a MODEL of logic infrastructure. Symbolic equality ≠ empirical equality.
**Self-audit**: Am I using the operator integrity constraints? (1. Combine: no unresolved contradictions. 2. Separate: boundary well-defined. 3. Transform: valid path. 4. Partition: MECE. 5. Abstract: identity preserved. 6. Instantiate: satisfies abstract constraints.)
**Effect**: Primitive-mapped conclusion with operator integrity checks.

### Decision Gates (per F09)

| Gate   | Check                        | Failure Action                                                   |
| ------ | ---------------------------- | ---------------------------------------------------------------- |
| **G1** | Mode declared pre-inference  | Retroactive assignment cannot rescue chain → restart from Step 4 |
| **G2** | Violations halt dependents   | Dependent conclusions halted, not merely warned                  |
| **G3** | Meta→object leaps explained  | Unexplained leap → record as observation, not objection          |
| **G4** | Self-reference loops flagged | Unbounded self-reference → triviality/paradox hazard             |

This parent skill consolidates the following sub-skills. Each is a section within this domain:

> **Reference**: See `references/meta_logic_config.md` (content_hash: 2a3895960faa40de) for the full C01 meta-logic configuration (objectives, typical questions, core methods, risk notes).

> **Reference**: See `references/determinism_boundaries.md` (content_hash: bb3ef84cb13f5cfb) for the Determinism Boundaries Enhanced (determinism scope, boundary conditions, non-determinism detection).

> **Reference**: See `references/business_logic_vulns.md` (content_hash: b1ac78da289dfe12) for the Business Logic Vulnerabilities (logic vulnerability patterns, business rule bypass, detection methods).

> **Reference**: See `references/absolute_protocol_synthesis.md` (content_hash: b205f3994b81cbe2) for the Absolute Protocol Synthesis Complete (absolute protocol synthesis, logic completion, protocol integration).

> **Reference**: See `references/trang_fpr.md` (content_hash: cd6f0d1f176a6e10) for the Trang First Principle Reasoning (first principle decomposition, root reasoning, principle-based analysis).

> **Reference**: See `references/kernels_logic.md` (content_hash: a93e0c9298eeb12d) for the AMOS Kernels Logic (logic kernels, reasoning kernels, formal logic).

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 97805fcf33b696d1) for additional vault-sourced domain knowledge.

> **Reference**: See `references/universal_reasoning_framework.md` (content_hash: e82119abb7b9e32e) for the Universal Reasoning Framework URF (universal reasoning, reasoning framework, URF architecture).

> **Reference**: See `references/deterministic_logic_law_engine.md` (content_hash: 06a6ba4e21721aff) for the Deterministic Logic and Law Engine (deterministic logic, law engine, logic-law integration).

> **Reference**: See `references/logic_core_engine.md` (content_hash: 84fc3deceda4ebef) for the AMOS Logic Core Engine (logic core, logical reasoning, logic processing).

> **Reference**: See `references/deterministic_logic_law_engine_cognitive.md` (content_hash: 69c48c5d4acf497c) for the AMOS Deterministic Logic and Law Engine Cognitive (deterministic logic, law engine, cognitive logic).

> **Reference**: See `references/mathematics_of_dao.md` (content_hash: 05ab8363342872f0) for the The Mathematics of the Dao (Dao mathematics, philosophical math, Dao logic).

> **Reference**: See `references/architecture_beneath_science.md` (content_hash: 73b990ac1ca3a45f) for the Architecture Beneath Science (science architecture, experiments, scientific method).

> **Reference**: See `references/logic_archive_amos2.md` (content_hash: fd297f84d0b6c593) for the Logic Archive AMOS2 (logic archive, AMOS2, historical logic).

> **Reference**: See `references/logic_architecture_human_reality.md` (content_hash: 3ce9084f6141aa5d) for the Logic as Architecture of Human Reality (logic, architecture, human reality).

> **Reference**: See `references/logic_rule.md` (content_hash: 9133161a3bff15e6) for the Logic Rule (logic rule, logical rules, reasoning rules).

## Validation Gates

- **L0 Integrity**: All 8 ALUs and 7 UMLs accounted for; no part silently dropped
- **L1 Epistemic**: Every claim tagged with epistemic class (SOURCE_CLAIM / DERIVED / AMOS_MODEL)
- **L5 Scope**: Analysis confined to declared scope; no scope creep into domain-specific logic
- **L7 Authority**: No autonomous action beyond authority boundary

## Do not use

- For generic tasks outside c01 domain (logic reasoning, decomposition, meta-law validation)
- As a substitute for domain-specific logic (use domain master skills instead)
- For empirical claims about logic without evidence
- Outside the AMOS canon law hierarchy

## References

- See `references/` directory for detailed reference materials
- [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]] — Skills map of content

______________________________________________________________________

**MOC:** references_MOC · [[00_ROOT/00_HOME|00_HOME]]
