---
schema_version: 1.0
title: SKILL — Amos Context Continuity Governor
type: skill
source: 07_SKILLS/amos-context-continuity-governor
name: amos-context-continuity-governor
description: Context Continuity Governor — boundary and scope capability. Use when
  evaluating scope boundaries, context continuity, or capability bounds. Use when
  amos-boundary-scope-master routes to this specialized capability. Do not use for
  generic tasks outside boundary domain.
parent_skill: amos-boundary-scope-master
domain: boundary
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/boundary-scope
- rscf/source_claim
- hml/h
- epistemic/source_claim
- amos_os
- 07-skills-moc
- amos-context-continuity-governor-moc
- 00-home
- amos-rscf-nodes
- law-hierarchy
- references-moc
- trang-framework-recursive-ontology-dynamics
- skill
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
rscf_state: SOURCE_CLAIM
hml_level: H
gmef_gates:
- L0_integrity
- L1_epistemic
- L2_provenance
- L5_scope
- L7_authority
collapse_class: fail_closed
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

# Context Continuity Governor

## Identity

Origin architect: **Trang Phan**. Domain: boundary. Parent: amos-boundary-scope-master. Epistemic class: SOURCE_CLAIM. H/M/L: H.
## When to Use

- When boundary and scope governance for context continuity governor is needed within the boundary domain
- When the parent skill (`amos-boundary-scope-master`) routes to this specialized capability
- When a query requires boundary-specific reasoning grounded in vault sources
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **context_continuity.evaluate_scope**: Evaluate scope boundaries: what is in-scope, out-of-scope, and at the boundary
- **context_continuity.check_admission**: Check admission criteria: whether a query enters this capability legitimately
- **context_continuity.detect_drift**: Detect context drift, persona drift, or scope creep beyond authorized bounds
- **context_continuity.enforce_compaction**: Enforce context compaction and recoverability when budget is exceeded
- **context_continuity.audit_boundary**: Audit boundary crossings and log violations for governance review
- **context_continuity.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **context_continuity.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 8940d50a1c67341a) for the full vault-sourced domain knowledge (7483 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/misc/TO/TOKEN_GOVERNOR.md` (content_hash: 61701ef736e3657a) (vault canon, SOURCE_CLAIM)
> **Additional source**: `_00_Cosmo brain/fractal/SKILL (fractal-state).md` (content_hash: 7ba1e6df8d84a479) (vault canon, SOURCE_CLAIM)

### Context Continuity Governor

From Cosmo Brain Token/Context Governor: 10-level retention priority and drop rule. From Fractal State Skill: H/M/L progressive disclosure for context management.

**10-level retention priority** (SOURCE_CLAIM):
1. **Objective**: the task objective (highest priority)
2. **Hard constraints**: constraints that cannot be violated
3. **Decision-changing evidence**: evidence that could change the decision
4. **Unresolved contradictions**: contradictions that need resolution
5. **Load-bearing premises**: premises that support conclusions
6. **Provenance/scope/regime/freshness**: RSCF metadata
7. **Active hypotheses**: hypotheses currently being tested
8. **Implementation details**: how things are implemented
9. **Recoverable background**: background that can be recovered if needed
10. **Redundant narrative**: narrative that can be dropped (lowest priority)

**Drop rule**: Drop only when removal cannot reasonably change: answer, decision, confidence, safety, falsifier, or implementation correctness.

**Compression**: Use IDs, hashes, schemas, equations, relation edges, and proof capsules internally. Use prose primarily at system boundaries.

**H/M/L progressive disclosure** (from Fractal State Skill):
1. Determine the appropriate scale level (H/M/L)
2. Load capsule-first summary at the chosen level
3. Expand recursively only when deeper detail is needed
4. Track information gain at each expansion
5. Stop when information gain falls below threshold

**Governor laws**:
- `CONTINUITY != PRESERVATION`: continuity maintains the thread; preservation keeps everything
- `CONTEXT != STATE**: context is the active working set; state is the full system state
- `DROP != DELETE**: dropping removes from active context; it does not delete the information

### Epistemic Boundary

Context continuity governance is an operational construct. It does not prove all context is preserved, that the priority order is always correct, or that dropping is always safe.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, f

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-context-continuity-governor_MOC]]

## Examples

- **Scenario**: When boundary and scope governance for context continuity governor is needed within the boundary domain
  - **Input**: A query matching this skill's domain (boundary)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When the parent skill (`amos-boundary-scope-master`) routes to this specialized capability
  - **Input**: A query matching this skill's domain (boundary)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When a query requires boundary-specific reasoning grounded in vault sources
  - **Input**: A query matching this skill's domain (boundary)
  - **Output**: Structured result with epistemic labels and provenance


## Validation Gates

- **L0 Integrity**: All structural elements accounted for; no silent gaps
- **L1 Epistemic**: Every claim tagged with epistemic class (SOURCE_CLAIM / DERIVED / AMOS_MODEL)
- **L5 Scope**: Analysis confined to declared scope and domain
- **L7 Authority**: No autonomous action beyond authority boundary

## Anti-Patterns

- **Do not use** for tasks outside the boundary domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-boundary-scope-master` — routes to this skill when boundary specialization is needed
- **Peers**: Other skills in the `boundary` domain may be composed in sequence
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

- For generic scope analysis outside the boundary/scope framework
- To claim empirical validation of context continuity theories
- As a substitute for domain-specific scope or boundary evidence
- Outside boundary/scope domain reasoning

## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `` — skill Map of Content
- `amos-boundary-scope-master` — parent skill
- `` — corresponding workflow
- `amos-context-continuity-governor-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-context-continuity-governor
node_type: skill
path: 07_SKILLS/amos-context-continuity-governor/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
