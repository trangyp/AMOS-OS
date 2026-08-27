---
title: SKILL
type: skill
source: 07_SKILLS/executive-deck-decision-system
name: executive-deck-decision-system
description: Executive Deck Decision System — strategy and game theory capability. Use when strategic analysis, game theory, or competitive reasoning. Use when amos-c08-strategy-game-master routes to this specialized capability.
parent_skill: amos-c08-strategy-game-master
domain: c08
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, executive-deck-decision-system, canon/skill]
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: "1.1.0"
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

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[executive-deck-decision-system_MOC]]

## Examples

- **Scenario**: When analyzing strategic position and competitive landscape
  - **Input**: A query matching this skill's domain (c08)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When evaluating decisions under uncertainty: expected value, regret
  - **Input**: A query matching this skill's domain (c08)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When modeling game-theoretic interactions and equilibria
  - **Input**: A query matching this skill's domain (c08)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the c08 domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `[[amos-c08-strategy-game-master]]` — routes to this skill when c08 specialization is needed
- **Peers**: Other skills in the `c08` domain may be composed in sequence
- **Orchestrator**: The parent skill or `AMOS_HOME` orchestrates routing
- **Workflow**: Each skill has a corresponding workflow in `08_WORKFLOWS/`
- **Agent**: Each skill has a corresponding agent in `06_AGENTS/`


## Evaluation

### Success Criteria

- Output includes epistemic class label (SOURCE/DERIVED/AMOS_MODEL/EMPIRICAL)
- Output includes provenance reference to source evidence
- Output includes confidence ceiling (capped at 0.95 for DERIVED, 1.0 for SOURCE_CANON)
- Output includes gap flags for unresolved unknowns
- Output does not exceed declared scope

### Failure Modes

- **Overreach**: Output claims validity beyond its epistemic class
- **Scope creep**: Output addresses questions outside the declared domain
- **Provenance loss**: Output cannot trace back to source evidence
- **Confidence inflation**: Output confidence exceeds the weakest-premise ceiling


## Error Handling

- **On scope violation**: Reject the query and route back to parent skill
- **On missing evidence**: Flag as GAP and reduce confidence ceiling to 0.5
- **On contradiction**: Flag as CRITICAL_GAP and halt until resolved
- **On provenance loss**: Mark output as UNKNOWN and require human review
- **On drift**: Trigger drift alignment via `amos-ai-drift-alignment-governor`


## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `[[executive-deck-decision-system_MOC]]` — skill Map of Content
- `[[amos-c08-strategy-game-master]]` — parent skill
- `[[executive-deck-decision-system-workflow]]` — corresponding workflow
- `[[executive-deck-decision-system-agent]]` — corresponding agent

