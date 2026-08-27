---
title: SKILL
type: skill
name: executive-deck-decision-system
description: Executive Deck Decision System — strategy and game theory capability. Use when strategic analysis, game theory, or competitive reasoning. Use when amos-c08-strategy-game-master routes to this specialized capability.
parent_skill: amos-c08-strategy-game-master
domain: c08
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, executive-deck-decision-system]
---


# Executive Deck Decision System

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c08-strategy-game-master`
- **Domain**: c08
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Strategy and game engine for Executive Deck Decision System

## When to Use

- When analyzing strategic position and competitive landscape
- When evaluating decisions under uncertainty: expected value, regret
- When modeling game-theoretic interactions and equilibria
- When assessing strategic risk: downside, adversarial, black swans
- When the parent skill (`amos-c08-strategy-game-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **executive_deck.analyze_strategy**: Analyze strategic position: competitive landscape, game-theoretic equilibrium
- **executive_deck.evaluate_decision**: Evaluate decisions under uncertainty: expected value, regret, risk-adjusted return
- **executive_deck.model_game**: Model game-theoretic interactions: players, strategies, payoffs, equilibria
- **executive_deck.assess_risk**: Assess strategic risk: downside scenarios, adversarial responses, black swans

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: bbf4188f2b149fe5) for the full vault-sourced domain knowledge (9587 chars).
- **executive_deck.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **executive_deck.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **executive_deck.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_C08_STRATEGY_GAME_MASTER_KNOWLEDGE.md` (content_hash: 4b676ad6f9ca020f) (vault canon, SOURCE_CLAIM)

### Executive Deck Decision System

From C08 Strategy & Game: Executive decision-making and communication.

**Executive deck principles**:
- **Pyramid principle**: conclusion first, then supporting arguments, then evidence
- **One message per slide**: each slide communicates one key message
- **Action title**: slide title states the conclusion, not the topic
- **Evidence-backed**: every claim backed by evidence with provenance
- **Decision-oriented**: deck drives toward a decision, not just information

**Decision system**:
1. **Frame**: frame the decision context and stakes
2. **Options**: present 2-3 viable options
3. **Evaluate**: evaluate each option against criteria
4. **Recommend**: recommend one option with justification
5. **Risk**: present key risks and mitigations
6. **Next steps**: present concrete next steps

**Law**: `DECK != DECISION`. A deck supports a decision; it does not make the decision. The decision authority rests with the executive.

### Epistemic Boundary

The executive deck decision system is a communication tool. It does not prove the decision is correct, that all options are covered, or that the deck captures all relevant information.

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
- **G6 (Failure mode)**: On validation failure, downgrade confidence, flag the gap, escalate — do not force-fit.

## Provenance

- **Skill**: `executive-deck-decision-system`
- **Parent**: `amos-c