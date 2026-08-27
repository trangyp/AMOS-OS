---
title: SKILL
type: skill
source: 07_SKILLS/amos-reality-simulation-distinction
name: amos-reality-simulation-distinction
description: Reality Simulation Distinction — canon and universe capability. Use when canon reasoning, universe-level analysis, or invariant verification. Use when amos-canon-universe-master routes to this specialized capability.
parent_skill: amos-canon-universe-master
domain: canon
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-reality-simulation-distinction, canon/skill]
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: "1.1.0"
---


# Reality Simulation Distinction

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-canon-universe-master`
- **Domain**: canon
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Canon and universe engine for Reality Simulation Distinction

## When to Use

- When compiling canonical structure from vault sources
- When checking canon consistency for contradictions and gaps
- When enforcing canon invariants across all parts
- When navigating canon to locate parts for any topic
- When the parent skill (`amos-canon-universe-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **reality_simulation.compile_canon**: Compile canonical structure from sources into a consistent, navigable canon
- **reality_simulation.check_consistency**: Check canon consistency: no contradictions, no gaps, no orphan references
- **reality_simulation.enforce_invariant**: Enforce canon invariants: structural laws that must hold across all parts
- **reality_simulation.navigate_canon**: Navigate canon: locate the canonical part for any topic or query
- **reality_simulation.validate_substrate**: Validate canonical software substrate against canon requirements

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: ac915a0d5093c8dd) for the full vault-sourced domain knowledge (9498 chars).
- **reality_simulation.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **reality_simulation.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **reality_simulation.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_C03_PHYSICS_COSMOS_MASTER_KNOWLEDGE.md` (content_hash: 4c2c6462c7ab1d23) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Reality-Simulation Distinction

From C03 Physics & Cosmos: Simulation hypothesis and reality distinction. From Cognitive Organism OS: Reality Gate as L0 cognitive substrate.

**Reality-Simulation distinction model**:
- **Reality**: the actual state of the world, independent of observation
- **Simulation**: a model that mimics some aspects of reality
- **Distinction**: the boundary between reality and simulation must be maintained

**Reality Gate (L0)**:
- **Perception-as-science-substrate filter**: perceptions are filtered through a science substrate before being accepted as reality
- **Anti-autopoisoning**: the system cannot poison its own perception with self-generated hallucinations
- **Reality check**: every observation must pass a reality check before being accepted

**Distinction laws**:
- `SIMULATION != REALITY`: a simulation is not reality; it is a model
- `MODEL != TRUTH`: a model is not truth; it is an approximation
- `PERCEPTION != REALITY`: perception is the system's interpretation; it is not reality itself

**Simulation types**:
- **Physical simulation**: simulates physical processes
- **Cognitive simulation**: simulates cognitive processes
- **Social simulation**: simulates social processes
- **Economic simulation**: simulates economic processes

### Epistemic Boundary

Reality-simulation distinction is an epistemological framework. It does not prove reality is knowable, that simulations are always distinguishable from reality, or that the Reality Gate is perfect.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## Validation Gates

- **G1 (Law of Law)**: No unresolved contradictions within the skill's scope.
- **G2 (Epistemic class)**: All claims labeled SOURCE / DERIVED /

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-reality-simulation-distinction_MOC]]

## Examples

- **Scenario**: When compiling canonical structure from vault sources
  - **Input**: A query matching this skill's domain (canon)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When checking canon consistency for contradictions and gaps
  - **Input**: A query matching this skill's domain (canon)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When enforcing canon invariants across all parts
  - **Input**: A query matching this skill's domain (canon)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the canon domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-canon-universe-master` — routes to this skill when canon specialization is needed
- **Peers**: Other skills in the `canon` domain may be composed in sequence
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
- `[[amos-reality-simulation-distinction_MOC]]` — skill Map of Content
- `amos-canon-universe-master` — parent skill
- `[[amos-reality-simulation-distinction-workflow]]` — corresponding workflow
- `amos-reality-simulation-distinction-agent` — corresponding agent

