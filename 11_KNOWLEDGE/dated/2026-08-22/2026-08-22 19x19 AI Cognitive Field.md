---
origin_architect: Trang Phan
provenance: user-supplied 19×19 strategic-ontology AI-cognition extension (sections 127–237); base geometry in cosmo-brain/AMOS_GO_BOARD_19X19.py and strategic field in cosmo-brain/AMOS_GO_BOARD_19X19_STRATEGIC.py
confidence: 0.88
epistemic_class: SOURCE_DERIVED
conclusion_label: MODEL
tags: [ai-cognition, attention, cognitive-field, kernel-routing, metacognition, rscf/M-memory, rscf/type-model, strategic-field, dated, dated/2026-08-22]
date: 2026-08-22
---

# 19×19 AI Cognitive Field

> **Model boundary**: The 19×19 field is a formal coordinate system for organizing AI cognition — not a claim that an LLM literally contains a Go board or biological brain. Mappings are structural analogies (`AMOS MODEL`), not proof of biological cognition or consciousness.
>
> Source: `AMOS_GO_BOARD_19X19.py` (geometry), `AMOS_GO_BOARD_19X19_STRATEGIC.py` (strategic field), `AMOS_STRATEGIC_FIELD_19X19.py` (recursive field). This note extends those to AI cognition.
> See also: 2026-08-22 19x19 Strategic Field Model, amos-go-board-19x19, 2026-08-22 AMOS Full Brain OS Architecture

## 1. Core reinterpretation

For AI cognition, the 19×19 board becomes a finite active cognitive workspace `C_t` with 361 addressable slots.

- `Cell ≠ Token` — a cell is an addressable cognitive-state slot.
- `C[cell, primitive, dimension]` is a sparse cognitive tensor.
- One position may hold a `Claim`, `Observation`, `Hypothesis`, `Goal`, `Constraint`, `Memory`, `PlanStep`, `ToolResult`, `Risk`, or `ActionCandidate`.

## 2. The nine-hoshi AI cognitive compass

The nine hoshi anchors form a macro control surface (§173–175):

| Hoshi | Cognitive role | Region |
|-------|----------------|--------|
| D16 | Evidence | NW |
| K16 | Goal | N |
| Q16 | Constraints | NE |
| D10 | Memory | W |
| K10 | Current Decision / Executive Focus | C |
| Q10 | Action Space | E |
| D4 | Competing Hypotheses | SW |
| K4 | Risk | S |
| Q4 | Output / Effect | SE |

K10 is the geometric fixed point = executive focus, not a magic cognitive center.

## 3. Primitive → AI cognition mapping

| 19×19 primitive | AI cognition mapping |
|-----------------|----------------------|
| Empty point | Uncommitted hypothesis / cognitive optionality |
| Stone | Cognitive commitment (`MARK` / `Admit`) |
| Shape | Reasoning schema / connected cognitive subgraph |
| Liberty | Viable next reasoning or action option |
| Eye | Protected internal reserve (epistemic + governance) |
| Aji | Latent insight or latent failure (`Aji⁺` / `Aji⁻`) |
| Ko | Loop prevention / recurrence governor |
| Sente | Information/action initiative |
| Gote | Reactive cognitive debt |
| Territory | Validated stable knowledge |
| Influence | Plausible prior / model pressure |
| Memory | Persistent reasoning state with dependency topology |
| Entropy | Contradiction, drift, repair burden |
| Repair | Selective reasoning correction |
| Sacrifice | Discarding local work for global integrity |
| Life | Viable reasoning structure |
| Death | Falsified / non-viable reasoning branch |
| Agency | Bounded goal-directed selection |

## 4. Void budget and cognitive optionality

`V_C(t)` = uncommitted viable hypothesis/action capacity.

- `V_C → 0` → rigidity, premature certainty, tunnel vision.
- `V_C → ∞` relative to task budget → endless branching, indecision, context explosion.
- Healthy cognition requires `V_min < V_C < V_max`.

## 5. Admission gate and commitment debt

Before a cognition object becomes load-bearing, it should satisfy:

```
Admit(x) = Relevant ∧ Typed ∧ ScopeKnown ∧ ProvenanceKnown ∧ NotHardContradicted
```

`D_commit(x) = Maintenance + Revalidation + DependencyRisk + CorrectionCost`

More committed state ≠ better cognition.

## 6. Two-eye AI robustness

- **Eye 1**: protected epistemic integrity (provenance, confidence discipline, contradiction visibility)
- **Eye 2**: protected governance integrity (authority, safety, permissions, rollback)

AI stability requires at least two structurally independent reserves.

## 7. Cognitive ko / loop governor

```
RetryAllowed ⟺ EvidenceChanged ∨ MethodChanged ∨ ConstraintChanged
LoopDetected ⟺ hash(goal, assumptions, activeHypothesis, tool, error)_t = hash(...)_{t-k}
```

## 8. Cognitive initiative vs gote

```
CI_t = (InformationGainGenerated + UncertaintyReduced + FutureChoicesPreserved) / (ReactiveRepairBurden + ε)
```

- `CI_t > 0` → proactive (sente)
- `CI_t < 0` → debt-dominated reactive (gote)

## 9. Territory vs influence vs aji

| State | Meaning |
|-------|---------|
| High-confidence evidence | Territory |
| Moderate pattern/prior | Influence |
| Weak unresolved possibility | Aji |
| No evidence | Void |
| Contradicted proposition | Dead group |

Three epistemic maturity layers: `Latent → Plausible → Validated`.

## 10. Cognitive collapse threshold

```
CR_C = UnresolvedCriticalConstraints / (RepairCapacity + ε)
```

If `CR_C > θ`, transition to `UNKNOWN/GAP` or `RECOVERY` — do not fabricate certainty.

`StableCognition = GoalContinuity × EvidenceIntegrity × MemoryValidity × RepairCapacity × AuthorityIntegrity`

Cognitive life = viable alternatives + protected invariants + repair capacity + reality contact.

## 11. Master cognitive tensor

```
Ψ[c, p, d, a, o, s, r, t, e, m]
```

where:

- `c` ∈ 361 cognitive cells
- `p` ∈ 19 primitives
- `d` ∈ 19 evaluation dimensions
- `a` = agent
- `o` = observer
- `s` = H/M/L scale
- `r` = regime
- `t` = time
- `e` = epistemic class
- `m` = memory/provenance state

Sparse tensor: only activate `DecisionRelevant(Ψ) = 1`.

Update equation (§234):

```
Ψ_{t+1} = Π_C [ Repair( Update( Ψ_t, Perception_t, Memory_t, ToolObservation_t, Action_t ) ) ]
```

`Π_C` projects onto safety, authority, epistemic invariants, scope, regime.

## 12. Cognitive action selection

```
a* = argmax_{a∈A_valid} [ IG(a) + OV(a) + GF(a) + RB(a) - Cost(a) - Debt(a) - Risk(a) ]
```

subject to `Authority(a)=PASS`, `Safety(a)=PASS`, `Scope(a)=PASS`.

Stop condition (§236):

```
DecisionSufficiency = ClaimSufficiency ∧ ActionSufficiency ∧ GovernanceSufficiency
```

and `ExpectedValue(MoreReasoning) < ExpectedCost(MoreReasoning)`.

## 13. Cognitive hierarchy and routing

```
Perception → 19×19 Cognitive Field → Omni Kernel / Router → Brain Core Engines → Skills / Tools / Models → Agent Plan → RSCF / Metacognitive Audit → Control Plane → Commit → Environment → Observation → (loop)
```

The 19×19 field becomes the state map feeding the Omni Kernel router.

### Routing triggers (§228–231)

| Field condition | Routed target |
|-----------------|---------------|
| Evidence deficit (NW) | Research engine |
| High math uncertainty (Hypotheses+Evidence) | Math engine |
| Implementation need (E/SE) | Code engine |
| Risk contradiction (S) | Audit engine |
| Contradiction detected | Logic kernel |
| Scope leakage | Boundary kernel |
| High causal claim | Causal kernel |
| Low confidence | Metacognitive kernel |

## 14. Metacognition as observer above the board

Metacognitive layer `Meta_t` monitors:

- goal fit
- evidence fit
- confidence fit
- contradictions
- loop state
- context pressure
- repair need

Output: `KEEP | DOWNGRADE | REVISE | ESCALATE | UNKNOWN`.

`MetacognitiveModel ≠ ConsciousSelf` — representation of low confidence is not subjective experience.

## 15. Externalization architecture

Cognitive objects migrate from working field to external infrastructure:

| Repeated stable form | External artifact |
|----------------------|-------------------|
| Repeated procedure | Skill |
| Stable fact | Memory |
| Interaction rule | Protocol |
| Deterministic logic | Code |
| Permission rule | Harness |

`WorkingField → ExternalizedCognitiveInfrastructure`.

## 16. Multi-agent and provenance

- Each agent has a private cognitive board + a shared coordination board.
- Shared memory does **not** imply independent evidence (`TwoStonesFromSameSource ≠ TwoIndependentSupports`).
- Every major cognitive mark carries provenance: `[source, parent, method, time, version]`.
- Bad information `x_bad` invalidates descendants `D(x_bad)` but leaves unrelated state intact.

## 17. Conclusion class

This note and its mappings are `AMOS MODEL / DERIVED`.
The 19×19 ontology, Full Brain constraints, and AMOS memory/externalization principles are source-grounded.
The nine-hoshi AI cognitive compass, sparse cognition tensor, cognitive initiative/debt metrics, attention-center formulation, and detailed AI mappings are new formal extensions and should remain `MODEL` until implemented and evaluated.
