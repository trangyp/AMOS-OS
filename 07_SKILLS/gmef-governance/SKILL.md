---
title: SKILL
type: skill
name: gmef-governance
description: Gmef Governance — strategy and game theory capability. Use when strategic analysis, game theory, or competitive reasoning. Use when amos-c08-strategy-game-master routes to this specialized capability.
parent_skill: amos-c08-strategy-game-master
domain: c08
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, gmef-governance]
---


# Gmef Governance

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c08-strategy-game-master`
- **Domain**: c08
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Strategy and game engine for Gmef Governance

## When to Use

- When analyzing strategic position and competitive landscape
- When evaluating decisions under uncertainty: expected value, regret, risk-adjusted return
- When modeling game-theoretic interactions and equilibria
- When assessing strategic risk: downside scenarios, adversarial responses, black swans
- When governing machine evolution: classifying mutations, enforcing constitutional boundaries
- When the parent skill (`amos-c08-strategy-game-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **gmef_governance.analyze_strategy**: Analyze strategic position: competitive landscape, game-theoretic equilibrium
- **gmef_governance.evaluate_decision**: Evaluate decisions under uncertainty: expected value, regret, risk-adjusted return
- **gmef_governance.model_game**: Model game-theoretic interactions: players, strategies, payoffs, equilibria
- **gmef_governance.assess_risk**: Assess strategic risk: downside scenarios, adversarial responses, black swans
- **gmef_governance.classify_mutation**: Classify evolution mutations (M0-M5) and enforce mutation permission profiles
- **gmef_governance.detect_drift**: Detect governance drift: scope creep, authority decay, or constitutional boundary erosion
- **gmef_governance.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **gmef_governance.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Vault-Sourced Domain Knowledge

> **Source**: `_00_Cosmo brain/misc/G/GMEF.md` (content_hash: 136e7ab44d48b155) (vault canon, SOURCE_CLAIM)

### Governed Machine Evolution Framework (GMEF)

**Constitutional nesting**: `Evolutionary Engine ⊂ Governance Boundary ⊂ Constitutional Boundary`

**Core law**: Capability never implies authority.

### Evolution Cycle

Observe → Propose → Classify → Sandbox → Experiment → Evaluate → Challenge → Govern → Select → Deploy → Remember

### Mutation Permission Profile

`MPP(x) = (C, L, A, R, E)`
- C = mutation class
- L = permitted limits
- A = approval authority
- R = rollback requirement
- E = evidence threshold

### Mutation Classes (M0-M5)

| Class | Description | Governance |
|-------|-------------|------------|
| M0 | Immutable constitutional invariants | Never autonomous |
| M1 | Safety/security boundaries | Human-governed |
| M2 | High-consequence architecture | Explicit approval required |
| M3 | Models/reasoning strategies/policies | Controlled evolution |
| M4 | Parameters/rankings/optimization weights | Bounded autonomous evolution |
| M5 | Low-risk operational adaptation | Autonomous within limits |

### Fitness Function

`F(V) = f(P, R, S, A, I, C, Q)`

Hard constraint failure: `C_hard = 0 => candidate inadmissible`

### Recursive Governance

`G_required ∝ D_recursive × C_consequence`

Governance requirement scales with recursion depth and consequence level.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## Validation Gates

- **G1 (Law of Law)**: No unresolved contradictions within the skill's scope.
- **G2 (Epistemic class)**: All claims labeled SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL — never claim beyond evidence.
- **G3 (Provenance)**: Source path recorded for every derived claim.
- **G4 (Anti-overreach)**: No claim beyond the skill's declared scope and epistemic class.
- **G5 (Equation firewall)**: Equations carry status tags (ESTABLISHED_MATH / SOURCE_DERIVED / AMOS_MODEL / EMPIRICALLY_CALIBRATED / UNVERIFIED).
- **G6 (Failure mode)**: On validation failure, downgrade confide