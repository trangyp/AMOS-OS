---
schema_version: 1.0
title: SKILL — Gmef Governance
type: skill
source: 07_SKILLS/gmef-governance
name: gmef-governance
description: Gmef Governance — strategy and game theory capability. Use when strategic analysis, game theory, or competitive reasoning. Use when amos-c08-strategy-game-master routes to this specialized capability. Do not use for generic tasks outside c08 domain.
parent_skill: amos-c08-strategy-game-master
domain: c08
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
  - type/skill
  - type/skill
  - domain/strategy-game
  - epistemic/source_claim
  - hml/m
  - epistemic/source_claim
  - amos-os
  - law-hierarchy
  - trang-framework-recursive-ontology-dynamics
  - skill
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
rscf_state: SOURCE_CLAIM
hml_level: M
gmef_gates:
  - L0_integrity
  - L1_epistemic
  - L2_provenance
  - L5_scope
  - L7_authority
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance:
  - L0
  - L1
  - L2
  - L4
  - L5
  - L7
  - L16
  - L17
  - L18
license: MIT
steward: Trang Phan
---

# Gmef Governance

## Identity

Origin architect: **Trang Phan**. Domain: c08. Parent: amos-c08-strategy-game-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.

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

## Operations

1. **gmef_governance.analyze_strategy**: Analyze strategic position: competitive landscape, game-theoretic equilibrium
1. **gmef_governance.evaluate_decision**: Evaluate decisions under uncertainty: expected value, regret, risk-adjusted return
1. **gmef_governance.model_game**: Model game-theoretic interactions: players, strategies, payoffs, equilibria
1. **gmef_governance.assess_risk**: Assess strategic risk: downside scenarios, adversarial responses, black swans
1. **gmef_governance.classify_mutation**: Classify evolution mutations (M0-M5) and enforce mutation permission profiles
1. **gmef_governance.detect_drift**: Detect governance drift: scope creep, authority decay, or constitutional boundary erosion
1. **gmef_governance.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
1. **gmef_governance.validate_outputs**: Validate outputs against domain constraints and epistemic class.

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

| Class | Description                              | Governance                   |
| ----- | ---------------------------------------- | ---------------------------- |
| M0    | Immutable constitutional invariants      | Never autonomous             |
| M1    | Safety/security boundaries               | Human-governed               |
| M2    | High-consequence architecture            | Explicit approval required   |
| M3    | Models/reasoning strategies/policies     | Controlled evolution         |
| M4    | Parameters/rankings/optimization weights | Bounded autonomous evolution |
| M5    | Low-risk operational adaptation          | Autonomous within limits     |

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

______________________________________________________________________

**Links:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

## Related

- [[07_SKILLS/gmef-governance/gmef-governance_MOC|gmef-governance_MOC]]

## Examples

- **Scenario**: When analyzing strategic position and competitive landscape

  - **Input**: A query matching this skill's domain (c08)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When evaluating decisions under uncertainty: expected value, regret, risk-adjusted return

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

## Do not use

- For generic strategic analysis outside the strategy/game framework
- To claim empirical validation of evolutionary cycle laws
- As a substitute for domain-specific market or competitive evidence
- Outside strategy/game domain reasoning

## References

- `references/authority_gmef_gate_integration.md` — loaded on demand
- `references/gmef_full.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- \`\` — skill Map of Content
- `amos-c08-strategy-game-master` — parent skill
- \`\` — corresponding workflow
- `gmef-governance-agent` — corresponding agent

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: gmef-governance
node_type: skill
path: 07_SKILLS/gmef-governance/SKILL.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
