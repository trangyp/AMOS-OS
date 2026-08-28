---
title: SKILL — Amos Law Stack Enforcement
type: note
source: 07_SKILLS/amos-law-stack-enforcement
tags:
- type/skill
- canon/skill
- domain/os-runtime
- canon-group/tech-ai
- topic/runtime
- capability/stack
- capability/lol_check
- capability/canonical_order_enforcement
- capability/gate_failure_flagging
- capability/emergency_policy_rejection
- rscf/epistemic
- rscf/C-constraint
- rscf/T-topology
- rscf/type-system
- sota/progressive-disclosure
- sota/anti-patterns
- amos_os
- amos-law-stack-enforcement
rscf:
  state: DERIVED
  claim_class: CONDITIONAL
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
---





# AMOS Law Stack Enforcement

## When to Use
- When validating whether a system's rules hold across scale transitions
- When checking if a proposed law adheres to the Law of Law™/Rule of 2™/Rule of 4™ hierarchy
- When a draft law short-circuits the canonical order: LoL→R2→R4 (contradictory drafts fail gate)
- When reasoning-shape ≠ authorization (integrity stack owns UBI Score/ledger, not output filter)

## Source
Vault-generated from law stack enforcement research (2026-08-25)

## 7-Part Mapping
| Part | Owned By | Gap Status |
|------|----------|-----------|
| I — Constraint | amos-law-stack-enforcement | ✅ Filled |
| II — Flow | — | ⚪ Empty |
| III — Structure | — | ⚪ Empty |
| IV — Enforcement | amos-law-stack-enforcement | ✅ Filled |
| V — Time | — | ⚪ Empty |
| VI — Adaptation | — | ⚪ Empty |
| VII — Termination | — | ⚪ Empty |

## Part Details

### Part I — Constraint
- **Properties:** Scarcity · Boundaries · Non-infinite capacity · Irreversibility
- **Law Stack Connection:** A proposed law must first satisfy Constraint before Enforcement applies
- **Examples:** Finite energy (physics), speed of light, metabolic limits (biology), logistics ceilings (war), time/attention/legitimacy (civilization)
- **Law Stack Gate:** PreventionCheck — if constraint fails, law cannot proceed to R2 gate

### Part IV — Enforcement
- **Definition:** The mechanism that prevents deviation from structure. Enforcement is not morality. It is mechanical correction.
- **Law Stack Connection:** This is the primary responsibility — LoL→R2→R4 order must be preserved
- **Properties:** Rule consistency · Boundary correction · Deviation cost · Predictability
- **Examples:** Physical laws, immune systems, military discipline, legal systems
- **Law Stack Gate:** G3 — Law Stack validation runs before any expression translation; canon compliance fields derived from actual law stack results (capability_authorized, evolution_allowed, mutation_gate_passed, all_gates_passed)

## Epistemic Boundary
This skill enforces the **Law of Law™/Rule of 2™/Rule of 4™** — the most-cited framework in the vault (official manual 743 lines) with ZERO executable enforcement previously. Created to fill the G3 'Law Stack' gate which had no defined checks. Contradictory drafts short-circuit: LoL→R2→R4 order must be preserved, and R4 quadrant completeness requires declared canonical family (UBI/TSS/PSI/QLS).

## References
- [[references]] — session-specific detail and authoritative sources
- references/README — references subdirectory readme

---
**MOC:** [[amos-law-stack-enforcement_MOC]]

## Examples

- **Scenario**: When validating whether a system's rules hold across scale transitions
  - **Input**: A query matching this skill's domain ()
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When checking if a proposed law adheres to the Law of Law™/Rule of 2™/Rule of 4™ hierarchy
  - **Input**: A query matching this skill's domain ()
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When a draft law short-circuits the canonical order: LoL→R2→R4 (contradictory drafts fail gate)
  - **Input**: A query matching this skill's domain ()
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the  domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Peers**: Other skills in the `` domain may be composed in sequence
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
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-law-stack-enforcement
node_type: skill
path: 07_SKILLS/amos-law-stack-enforcement/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
