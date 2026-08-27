---
title: "Vault Domain Knowledge — Amos C08 Strategy Game Master"
type: reference
source: 07_SKILLS/amos-c08-strategy-game-master/references
tags: [reference, amos-c08-strategy-game-master, canon/skill]
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# amos-c08-strategy-game-master — Vault-Sourced Domain Knowledge

> Load this reference only when detailed domain knowledge is needed.
> This content was moved from SKILL.md for progressive loading.

---

> **Source**: `11_KNOWLEDGE/AMOS_C08_STRATEGY_GAME_MASTER_KNOWLEDGE.md` from the AMOS_OS Obsidian vault.
> This is substantive domain knowledge, not script-generated content.

# AMOS C08 — Strategy, Game Theory & Negotiation Master Knowledge

> **Epistemic boundary**
>
> This file replaces synthetic micro-module expansion with substantive strategy, game-theory,
> negotiation, and 19×19 strategic-field knowledge. It does not claim encyclopedic completeness.
> Established game-theoretic results within stated assumptions, formal-system constructions,
> analogy-based models, competing solution concepts, normative bargaining choices, and
> AMOS/Trang abstractions are kept separate.
>
> **Analogy ≠ isomorphism.** The Go Board is a formal state space used as a governed MODEL.
> A board mapping can organize reasoning; it cannot prove real-world causation or substitute
> for domain evidence. Legal and ethical constraints always rank above strategic analogy.
>
> Strategic recommendations are actor-, information-, commitment-, and timescale-dependent.
> Long-horizon outputs must preserve uncertainty about other actors' payoffs and beliefs,
> multiplicity of equilibria, non-stationary incentives, and enforcement limits.

## 0. C08 Knowledge Contract

### 0.1 Claim classes
- **VERIFIED** — established result under explicitly stated assumptions (e.g., Nash existence in finite games with mixed strategies).
- **DERIVED** — mathematical/logical consequence of a stated game form or formal system.
- **MODEL** — representation useful within stated scope (includes all Go-Board formal machinery).
- **CONDITIONAL** — dependent on explicit assumptions, scenario, or information regime.
- **COMPETING** — unresolved alternatives (e.g., equilibrium selection criteria).
- **UNKNOWN/GAP** — insufficient specification or unresolved mechanism.

### 0.2 Evidence classes
`AXIOM`, `THEOREM`, `COMPUTATION`, `SIMULATION`, `CASE_OBSERVATION`, `SOURCE_CLAIM`,
`MODEL`, `SCENARIO`, `ANALOGY`, `UNKNOWN`.

### 0.3 C08 H-level ownership
1. Game Structure & Incentive Mapping
2. Solution Concepts & Equilibrium Analysis
3. Coalitions, Bargaining & Agreement Design
4. Credible Commitment, Threats & Enforcement
5. Information, Belief & Signaling
6. 19×19 Strategic Field Ontology
7. Go Board Formal System (State Space, Not Semantics)
8. Multi-Agent Strategy Dynamics & Recurrence Control
9. AMOS/Trang Strategy Research Bridge

A topic has one primary owner. Cross-links are references, not duplicated substantive sections.

### 0.4 Standard knowledge node schema
Where applicable:
**definition → actors/actions/payoffs → governing relations → assumptions → mechanisms →
observables → test/computation status → empirical status → scope/regime → uncertainty →
failure modes → competing models → falsifiers → dependencies → decision relevance → AMOS bridge**.

---

# H1 — Game Structure & Incentive Mapping

## M1. The Game Being Played

### L1. Identification before analysis
Before any strategic conclusion, identify:
- who the actors are;
- what each actor can actually choose;
- what payoff each combination produces for each actor;
- what information each actor holds at each decision point;
- what moves happen simultaneously vs sequentially;
- how often the interaction repeats.

A mis-specified game invalidates every downstream equilibrium claim.

### L2. Canonical game forms
Common structural families:
- prisoner's dilemma (unilateral defection temptation, mutual cooperation best jointly);
- stag hunt (coordination on efficient outcome vs safe outcome);
- chicken/hawk–dove (mutual escalation worst);
- pure coordination;
- bargaining over surplus division;
- zero-sum contest;
- public-goods contribution;
- principal–agent.

Classification is a MODEL judgment: real situations may blend structures, and the fit should
record why alternatives fail.

### L3. Payoff matrix discipline
Payoffs must be made explicit as `actor × action-profile → outcome` before conclusions.
Numbers assumed without a source are marked ASSUMPTION, not fact. Ordinal payoffs support
equilibrium identification; cardinal claims require a value model.

---

## M2. Incentive Structure

### L1. Dominance
A strategy strictly dominates another if it yields a better outcome regardless of others'
actions. Iterated elimination of dominated strategies narrows prediction only where dominance
is genuine.

### L2. Externalities and incentive misalignment
An actor's choice can impose costs/benefits on others not reflected in that actor's own
payoff. Misalignment between private and collective payoffs drives many observed failures.

### L3. Repeated-play effects
Repetition changes incentives when future consequences feed back into present payoffs.
Cooperation can be sustained by credible future punishment in repeated games under
discounting conditions — this is conditional, not automatic.

---

# H2 — Solution Concepts & Equilibrium Analysis

## M1. Nash Equilibrium

### L1. Definition
A profile where no single actor gains by unilateral deviation. Existence in finite games with
mixed strategies is a VERIFIED theorem class result.

### L2. Multiplicity
Many games have multiple equilibria. Claiming one outcome without an explicit selection
argument (focal points, risk dominance vs payoff dominance, history, convention) is an error.

### L3. Refinements
Subgame-perfect, sequential, trembling-hand, and evolutionary stability refine Nash under
different assumptions. Each refinement adds assumptions; results do not transfer between them
without justification.

## M2. Equilibrium Honesty Gates

### L1. Gate list
1. Single equilibrium claimed where multiple exist? → flag selection problem.
2. Equilibrium computed from guessed payoffs? → mark as scenario, not prediction.
3. Equilibrium treated as guaranteed outcome? → equilibria describe stable profiles, not
   guarantees of arrival, especially with bounded rationality or learning frictions.

### L2. Bounded rationality caveat
Real actors face computation limits, framing, emotion, and time pressure. Nash predictions
degrade accordingly; behavioral deviations are documented phenomena, not noise to be ignored.

---

# H3 — Coalitions, Bargaining & Agreement Design

## M1. Coalition Analysis

### L1. Formation and stability
A coalition is stable if no member gains by deviating given expected responses. Test proposed
alliances against deviation incentives rather than declared intent.

### L2. Value distribution concepts
Shapley-style value assigns shares based on marginal contribution across orderings; core
concepts ask whether any subgroup can profitably secede. These are competing allocation
norms/models, not facts about what will be agreed.

## M2. Bargaining

### L1. BATNA inventory
The credible walk-away alternative largely determines bargaining power. Map every party's
BATNA before evaluating offers.

### L2. Zone of agreement
Agreement exists where overlapping reservation values permit mutually acceptable terms.
Without overlap, no clever tactic creates surplus.

### L3. Fairness arguments vs power
Fairness rhetoric affects perception but does not move the feasible set. Distinguish
normative fairness claims (explicitly normative) from power-based splits (structural).

## M3. Agreement Design

### L1. Mechanism properties
Incentive compatibility, participation constraints, budget balance, and robustness to
private information are designable properties — trade-offs among them are structural.

### L2. Contract incompleteness
Not all future contingencies can be specified. Residual rights, renegotiation clauses, and
governance fill gaps; assume they matter.

---

# H4 — Credible Commitment, Threats & Enforcement

## M1. Credibility

### L1. Ex-post rationality test
A threat is credible only if carrying it out would be rational for the threatener after the
fact. Verify the commitment mechanism, not the announcement.

### L2. Commitment devices
Burning bridges, contracts, escrow, reputation systems, staged payments, and third-party
enforcement convert cheap talk into binding constraint — each has cost and failure modes.

### L3. Reputation
Reputation sustains cooperation when future value of the relationship exceeds short-term gain
from betrayal. Reputation mechanisms require observability, memory, and consequence channels.

---

# H5 — Information, Belief & Signaling

## M1. Information Regimes

### L1. Asymmetry
Actors may differ in what they know (adverse selection) or in actions taken unseen (moral
hazard). Different problems need different remedies.

### L2. Common knowledge
Some results require common knowledge of rationality or payoffs. Weakening common-knowledge
assumptions changes conclusions materially.

## M2. Signaling and Screening

### L1. Signal credibility
A signal informs only if it costs less to send for honest types than dishonest types
(costly-signaling logic). Costless signals are cheap talk.

### L2. Screening
The uninformed party can design menus that induce self-selection. Menu design quality
determines separation vs pooling.

---

# H6 — 19×19 Strategic Field Ontology

## M1. Finite Field with Large Future Consequence

### L1. Core concept [MODEL]
The Trang/AMOS ontology treats a 19×19 field as a finite strategic space where individual
placements carry recursively expanding consequence. Governing concepts:

- option preservation — keep degrees of freedom alive;
- irreversible marks — placements that cannot be undone;
- liberties — remaining local degrees of freedom of a group/position;
- protected internal void — secured interior reserve supporting viability;
- aji — latent future potential in existing structure;
- initiative — forcing tempo (sente) vs responsive tempo (gote);
- territory vs influence — realized value vs option value;
- sacrifice — deliberate concession traded for larger positional gain;
- ko/dead-loop prevention — recurrence constraints blocking infinite repetition.

### L2. Epistemic status
This ontology is a governed MODEL for organizing multi-scale strategic reasoning.
It is not a claim that all strategy is literally a Go game, and board analogies cannot
prove real-world causation.

## M2. Move Evaluation Discipline

### L1. Multi-axis comparison
Compare candidate moves by immediate gain, future debt, reversibility, and preserved options
— not by immediate gain alone.

### L2. Sacrifice validity
A sacrifice is valid only if evaluated against the full consequence path, including whether
the conceded material/value can actually be recovered under opponent's best response.

### L3. Runtime procedure
1. Confirm the 19×19 mapping is useful and explicitly MODEL-scoped.
2. Map positions, empty options, constraints, irreversible marks.
3. Identify liberties/future degrees of freedom.
4. Separate territory from influence.
5. Detect dead loops and ko-like recurrence constraints.
6. Evaluate sacrifices by H/M/L consequence.
7. Compare moves across the four axes above.
8. Emit recommendation plus invalidation conditions.

---

# H7 — Go Board Formal System (State Space, Not Semantics)

## M1. Static Geometry [SOURCE-derived]

| Property | Value |
|----------|-------|
| Board size | 19×19 = 361 cells |
| Columns | A–T excluding I = 19 |
| Rows | 1–19 |
| Corners | 4 (A1, A19, T1, T19) |
| Side cells | 68 |
| Interior | 289 |
| Hoshi points | 9 at {4, 10, 16}² |
| Center | K10 (id 181) |
| Adjacency edges | 684 (derived) |
| D4 symmetry group | 8 transformations |

Zone classification by boundary depth: corner ≤3, side 4–6, center 7–9.
Nine macro regions: NW, N, NE, W, C, E, SW, S, SE.

Field measures (AMOS MODEL formulas):
`BoundarySupport = 1 − d_B/9`; `CenterInfluence = 1 − d_C/18`;
`ExpansionFreedom = 0.5·(d_B/9 + deg/4)`.

## M2. Address-Space Boundary — Critical

### L1. State space, not archetypes
The 361 coordinates are a **state space**, NOT 361 separately defined semantic archetypes.
Meaning emerges through geometry, time, relation, and board history. Assigning mystical
meanings to all 361 cells is canon fabrication and prohibited.

### L2. B3 discipline: address-space tested, not semantic-equivalence
Structures sharing size (e.g., 19-long axes in different systems) are NOT interchangeable.
A `cell` axis from Go Board is not compatible with a `variable` axis from another 19-variable
system despite equal length. Compatibility requires typed-axis validation, never length match.
Analogy ≠ isomorphism; structural isomorphism claims (e.g., MURK↔GoBoard 361↔361) are
registered as cross-system reasoning tools, not proofs of shared meaning.

## M3. Cell State and Machinery [AMOS MODEL]

### L1. Core cell state variables
Possibility, mark, boundary depth, liberty count, aji, territory value, influence value,
ko state, initiative (sente/gote), group membership, local entropy, strategic value.
The executable implementation extends these into a 20-variable vector.

### L2. Supplemental modules (75-section registry, selected)
Eye topology and protected void reserve · initiative differential and ko recurrence graph ·
territory/influence phase states (open/potential/crystallized/locked) · future debt tensor ·
memory tensor with decay classes · multi-scale lacunarity · option diversity/concentration ·
pressure and repair tensors · sacrifice tensor (7 fields) · trajectory objects and branching
future tree · branch robustness · regime state and phase transitions · observer belief models
(B^A ≠ B^B) · confidence tensor with epistemic tags · move tensor · move evaluation firewall
(`M1_DOMINATES / M2_DOMINATES / COMPETING`) · master update pipeline · full-system invariants.

Compositional evaluation pipeline:
`T = T_O ∘ T_G ∘ T_L ∘ T_E ∘ T_A ∘ T_K ∘ T_Φ ∘ T_Ω ∘ T_M`.

### L3. Computation status
Formal implementation carries registered self-test suites (Go Board suites totaling ~630
passing tests per skill record). Passing tests establish executable consistency of the formal
machinery — they do NOT validate the model against empirical strategic outcomes in external
domains.

## M4. Decision Gates

1. Eye-quality gate — internal void must meet threshold for life claims.
2. Initiative gate — sente/gote balance computed, not asserted.
3. Phase-state gate — territory/influence phase identified before evaluation.
4. Lacunarity gate — multi-scale lacunarity computed where scale claims are made.
5. Firewall gate — move passes M1/M2/COMPETING evaluation.
6. Invariant gate — all system invariants hold after update.

---

# H8 — Multi-Agent Strategy Dynamics & Recurrence Control

## M1. Sequential Interaction

### L1. Backward induction
Optimal play in known-horizon sequential games follows backward induction under common
knowledge assumptions; the centipede-game literature documents tension between this logic
and observed human play.

### L2. Finitely vs infinitely repeated
Cooperation-supporting strategies differ sharply by horizon type. Unraveling arguments apply
only to known finite horizons with common knowledge.

## M2. Learning and Adaptation

### L1. Adaptive opponents
Opponents learn; fixed-opponent analysis decays in validity. Strategy against adaptive agents
requires modeling their update process.

### L2. Evolutionary dynamics
Repl


## Vault-Sourced Domain Content

> Source: `11_KNOWLEDGE/AMOS_C08_STRATEGY_GAME_MASTER_KNOWLEDGE.md` (24246 bytes in vault)

### 0.1 Claim Classes

- **VERIFIED** — established result under explicitly stated assumptions (e.g., Nash existence in finite games with mixed strategies).
- **DERIVED** — mathematical/logical consequence of a stated game form or formal system.
- **MODEL** — representation useful within stated scope (includes all Go-Board formal machinery).
- **CONDITIONAL** — dependent on explicit assumptions, scenario, or information regime.
- **COMPETING** — unresolved alternatives (e.g., equilibrium selection criteria).
- **UNKNOWN/GAP** — insufficient specification or unresolved mechanism.

### 0.2 Evidence Classes

`AXIOM`, `THEOREM`, `COMPUTATION`, `SIMULATION`, `CASE_OBSERVATION`, `SOURCE_CLAIM`,
`MODEL`, `SCENARIO`, `ANALOGY`, `UNKNOWN`.

### 0.4 Standard Knowledge Node Schema

Where applicable:
**definition → actors/actions/payoffs → governing relations → assumptions → mechanisms →
observables → test/computation status → empirical status → scope/regime → uncertainty →
failure modes → competing models → falsifiers → dependencies → decision relevance → AMOS bridge**.

---

# H1 — Game Structure & Incentive Mapping

### L2. Canonical Game Forms

Common structural families:
- prisoner's dilemma (unilateral defection temptation, mutual cooperation best jointly);
- stag hunt (coordination on efficient outcome vs safe outcome);
- chicken/hawk–dove (mutual escalation worst);
- pure coordination;
- bargaining over surplus division;
- zero-sum contest;
- public-goods contribution;
- principal–agent.

Classification is a MODEL judgment: real situations may blend structures, and the fit should
record why alternatives fail.

### L3. Payoff Matrix Discipline

Payoffs must be made explicit as `actor × action-profile → outcome` before conclusions.
Numbers assumed without a source are marked ASSUMPTION, not fact. Ordinal payoffs support
equilibrium identification; cardinal claims require a value model.

---

### L1. Gate List

1. Single equilibrium claimed where multiple exist? → flag selection problem.
2. Equilibrium computed from guessed payoffs? → mark as scenario, not prediction.
3. Equilibrium treated as guaranteed outcome? → equilibria describe stable profiles, not
   guarantees of arrival, especially with bounded rationality or learning frictions.

### L2. Contract Incompleteness

Not all future contingencies can be specified. Residual rights, renegotiation clauses, and
governance fill gaps; assume they matter.

---

# H4 — Credible Commitment, Threats & Enforcement

### L2. Common Knowledge

Some results require common knowledge of rationality or payoffs. Weakening common-knowledge
assumptions changes conclusions materially.

### L2. Epistemic Status

This ontology is a governed MODEL for organizing multi-scale strategic reasoning.
It is not a claim that all strategy is literally a Go game, and board analogies cannot
prove real-world causation.

### L3. Runtime Procedure

1. Confirm the 19×19 mapping is useful and explicitly MODEL-scoped.
2. Map positions, empty options, constraints, irreversible marks.
3. Identify liberties/future degrees of freedom.
4. Separate territory from influence.
5. Detect dead loops and ko-like recurrence constraints.
6. Evaluate sacrifices by H/M/L consequence.
7. Compare moves across the four axes above.
8. Emit recommendation plus invalidation conditions.

---

# H7 — Go Board Formal System (State Space, Not Semantics)

### L2. B3 Discipline: Address-Space Tested, Not Semantic-Equivalence

Structures sharing size (e.g., 19-long axes in different systems) are NOT interchangeable.
A `cell` axis from Go Board is not compatible with a `variable` axis from another 19-variable
system despite equal length. Compatibility requires typed-axis validation, never length match.
Analogy ≠ isomorphism; structural isomorphism claims (e.g., MURK↔GoBoard 361↔361) are
registered as cross-system reasoning tools, not proofs of shared meaning.

### M4. Decision Gates

1. Eye-quality gate — internal void must meet threshold for life claims.
2. Initiative gate — sente/gote balance computed, not asserted.
3. Phase-state gate — territory/influence phase identified before evaluation.
4. Lacunarity gate — multi-scale lacunarity computed where scale claims are made.
5. Firewall gate — move passes M1/M2/COMPETING evaluation.
6. Invariant gate — all system invariants hold after update.

---

# H8 — Multi-Agent Strategy Dynamics & Recurrence Control

### M3. Rscf Strategy Mapping

A domain-specific RSCF representation encodes:
- **State** — position, resources, beliefs, obligations;
- **Constraint** — rules, contracts, laws, ethics, capacity limits;
- **Feedback** — responses, reputation effects, adaptation;
- **Repair** — recovery mechanisms after bad outcomes where genuinely available.

Legal and ethical constraints rank above strategic analogy in every repair/mapping decision.

### M6. Credibility Firewall

Never present as credible:
- threats without ex-post-rational execution paths;
- commitments without enforcement mechanisms;
- signals without differential cost structure;
- equilibria selected without a selection argument.

### M7. Analogy Firewall

Correct:
`Under the 19×19 MODEL, position X exhibits low liberty and high aji; recommend testing Y.`

Incorrect:
`Life is a Go game, therefore X must lose.`

Board mappings organize hypotheses; domain evidence decides them.

---

# C08 ↔ CC05 Mind & Behavior Reference Bridge

### Causal Firewall

```text
strategic situation [C08]
→ perception / emotion / bias [CC05]
→ chosen behavior [CC05/C08 boundary]
→ payoff consequence [C08]
```

Every cross-domain arrow inherits its own evidence, population, context, confounders, and
uncertainty. C08 must not infer psychological states from game structure alone, nor treat
behavioral constructs as payoff observations.

```yaml
cross_domain_refs:
  - id: AMOS_CC05_mind_behavior
    relation: strategic_interaction_behavior_coupling
    direction: bidirectional
    ownership_rule: preserve_domain_boundaries
    causal_status: mediated_not_assumed
    confidence_rule: weakest_load_bearing_edge
```

---

# C08 Master Dependency Spine

```text
actors + available actions
            ↓
payoffs + information regimes
            ↓
game structure identification
            ↓
equilibrium / dominance analysis
            ↓
coalitions + bargaining + BATNA
            ↓
credible commitments + enforcement
            ↓
19×19 strategic field MODEL
            ↓
go board formal system (state space)
            ↓
multi-agent dynamics + recurrence control
            ↓
negotiation + agreement design
            ↓
AMOS cross-scale decision architecture
```

# C08 Decision Capsule Template

```text
Situation:
Boundary (who is in the game):
Decision:
Irreversibility:
Actors:
Actions available to each:
Information held by each:
Timing (simultaneous/sequential):
Repetition horizon:
Observed behavior so far:
Payoff estimates + sources:
Assumed payoffs (flagged):
Candidate game structures:
Selected structure + why others fail:
Equilibria found:
Multiplicity handling / selection argument:
Coalition candidates:
Stability check:
BATNA inventory (each party):
Commitment mechanisms available:
Threats + ex-post rationality check:
Signaling/screening opportunities:
19×19 mapping useful? (yes/no + why):
Territory vs influence split:
Liberties / options preserved:
Aji / latent potential:
Ko-like recurrence risks:
Sacrifice candidates + validity:
Competing explanations:
Decision-sensitive uncertainty:
Recommended move(s):
Invalidation conditions:
Revalidation date:
```

# C08 Promotion Rule

A new strategy/game claim may move from `MODEL` toward stronger status only when:
1. actors, actions, payoffs, and information are operationally defined;
2. the game structure is identified with rejected alternatives recorded;
3. assumed payoffs are separated from sourced payoffs;
4. multiplicity of equilibria is addressed with an explicit selection argument;
5. credibility claims pass the ex-post-rationality test;
6. formal

... (truncated, see vault source for full content)

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

---
**MOC:** [[references_MOC]]

## Related

- [[07_SKILLS_MOC]]
