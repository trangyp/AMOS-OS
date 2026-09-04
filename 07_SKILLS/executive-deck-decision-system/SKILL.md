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

# Executive Deck Decision System

## Identity

Origin architect: **Trang Phan**. Domain: c08. Parent: amos-c08-strategy-game-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.

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

## Operations

1. **executive_deck.analyze_strategy**: Analyze strategic position: competitive landscape, game-theoretic equilibrium
1. **executive_deck.evaluate_decision**: Evaluate decisions under uncertainty: expected value, regret, risk-adjusted return
1. **executive_deck.model_game**: Model game-theoretic interactions: players, strategies, payoffs, equilibria
1. **executive_deck.assess_risk**: Assess strategic risk: downside scenarios, adversarial responses, black swans
1. **executive_deck.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
1. **executive_deck.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
1. **executive_deck.validate_outputs**: Validate outputs against domain constraints and epistemic class.

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
1. **Options**: present 2-3 viable options
1. **Evaluate**: evaluate each option against criteria
1. **Recommend**: recommend one option with justification
1. **Risk**: present key risks and mitigations
1. **Next steps**: present concrete next steps

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
- **Parent**: \`amos-c

______________________________________________________________________

**Links:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

## Related

- [[07_SKILLS/executive-deck-decision-system/executive-deck-decision-system_MOC|executive-deck-decision-system_MOC]]

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

- **Parent**: `amos-c08-strategy-game-master` — routes to this skill when c08 specialization is needed
- **Peers**: Other skills in the `c08` domain may be composed in sequence
- **Orchestrator**: The parent skill or `AMOS_HOME` orchestrates routing
- **Workflow**: Each skill has a corresponding workflow in `26_WORKFLOWS/`
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

## Do not use

- For generic strategic analysis outside the strategy/game framework
- To claim empirical validation of evolutionary cycle laws
- As a substitute for domain-specific market or competitive evidence
- Outside strategy/game domain reasoning

## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- \`\` — skill Map of Content
- `amos-c08-strategy-game-master` — parent skill
- \`\` — corresponding workflow
- `executive-deck-decision-system-agent` — corresponding agent

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: executive-deck-decision-system
node_type: skill
path: 07_SKILLS/executive-deck-decision-system/SKILL.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
