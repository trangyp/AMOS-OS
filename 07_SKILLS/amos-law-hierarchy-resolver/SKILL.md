---
title: SKILL — Amos Law Hierarchy Resolver
type: skill
source: 07_SKILLS/amos-law-hierarchy-resolver
name: amos-law-hierarchy-resolver
description: Law Hierarchy Resolver — meta logic capability. Use when logic reasoning,
  decomposition, or meta-law validation. Use when amos-c01-meta-logic-master routes
  to this specialized capability.
parent_skill: amos-c01-meta-logic-master
domain: c01
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- canon/skill
- domain/meta-logic
- canon-group/tech-ai
- topic/logic
- capability/hierarchy
- capability/failur
- capability/resolution
- capability/reasoning
- rscf/epistemic
- rscf/C-constraint
- rscf/G-relation
- rscf/T-topology
- rscf/M-memory
- rscf/type-model
- sota/progressive-disclosure
- sota/anti-patterns
- amos_os
- amos-law-hierarchy-resolver
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: 1.1.0
---






# Law Hierarchy Resolver

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c01-meta-logic-master`
- **Domain**: c01
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Logic and law engine for Law Hierarchy Resolver

## When to Use

- When resolving conflicts between meta-laws, domain laws, and operational rules
- When applying the Law of Law, Rule of 2, and Rule of 4 to validate structural consistency
- When determining which law takes precedence in a hierarchy conflict
- When checking whether a system has unresolved contradictions or logical drift
- When the parent skill (`amos-c01-meta-logic-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **law_hierarchy.resolve_hierarchy**: Resolve law hierarchy: meta-laws, domain laws, and operational rules
- **law_hierarchy.validate_consistency**: Validate cross-law consistency using the Law of Law constraint
- **law_hierarchy.apply_rule_of_2**: Apply the Rule of 2 to decompose systems into complementary force pairs
- **law_hierarchy.apply_rule_of_4**: Apply the Rule of 4 to classify system behavior into structural quadrants
- **law_hierarchy.detect_drift**: Detect logical drift, contradiction, or overextension beyond structural boundaries
- **law_hierarchy.escalate_gaps**: Escalate unresolved law conflicts as UNKNOWN/GAP — do not force-fit
- **law_hierarchy.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **law_hierarchy.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Vault-Sourced Domain Knowledge

> **Sources**: `_00_Cosmo brain/misc/L/Law of Law Rule of 2 Rule of 4.md` (content_hash: 0e3a9a742d48438d), `_00_Cosmo brain/amos-general/A/all/AMOS All Frameworks Canon Hierarchy.md` (content_hash: 4628ba22a3b5d427) (vault canon, SOURCE_CLAIM)

### The Law of Law™

The governing constraint applied to all reasoning. Every valid system, interpretation, or prediction must be bound by a higher-order structure that prevents contradiction, drift, and recursive incoherence.

**Core Definition**: Every system operates within an overarching set of governing constraints, and these constraints themselves operate within a final meta-constraint. This final constraint determines which interpretations are allowed, which transitions are legitimate, and which outcomes are structurally impossible.

**Function — Stabilizer**:
- Prevents: contradictory outcomes, logically impossible transitions, drift in analysis, overextension beyond structural boundaries
- Ensures: structural alignment, lawful causal pathways, constraint inheritance, cross-time self-consistency

### The Rule of 2™

Defines the fundamental dual structure underlying all human-linked systems. Ensures every system reduces to two core forces that interact.

**Core Definition**: All systems contain two opposing but complementary forces that maintain dynamic equilibrium:
- expansion ↔ contraction
- integration ↔ fragmentation
- stability ↔ volatility
- overload ↔ capacity
- opportunity ↔ constraint

**Function**: Simplifies complex systems into predictable behavior pairs. Foundation of TSS cycle logic and structural interpretation of system movement.

### The Rule of 4™

Defines the structural quadrants that govern all higher-order system behavior.

**Core Definition**: Four quadrants classify system state and determine which interventions are structurally valid:
1. **Stable + Aligned** — maintain and optimize
2. **Stable + Misaligned** — correct direction before acceleration
3. **Unstable + Aligned** — stabilize before scaling
4. **Unstable + Misaligned** — halt, diagnose, restructure

### Canon Hierarchy (5 Levels)

| Level | Name | Role |
|-------|------|------|
| 1 | Meta-Framework | UBA (Universal Bio-Logical Architecture) — above everything |
| 2 | Top-Level Disciplines | Bio-Logical Computing, Cognitive Systems Architecture, AMOS Organism OS, Governance, Life Systems |
| 3 | Core Frameworks | UBI, QLS, QCLA, ULF, PSI, TSS, TPE, AMOS_CORE |
| 4 | Domain Engines | C01-C12 domain-specific reasoning engines |
| 5 | Operational Skills | Individual skills, agents, workflows |

**Precedence Rule**: Higher levels constrain lower levels. A lower-level rule cannot override a higher-level law. Conflicts escalate upward.

## Failur

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-law-hierarchy-resolver_MOC]]

## Examples

- **Scenario**: When resolving conflicts between meta-laws, domain laws, and operational rules
  - **Input**: A query matching this skill's domain (c01)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When applying the Law of Law, Rule of 2, and Rule of 4 to validate structural consistency
  - **Input**: A query matching this skill's domain (c01)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When determining which law takes precedence in a hierarchy conflict
  - **Input**: A query matching this skill's domain (c01)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the c01 domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-c01-meta-logic-master` — routes to this skill when c01 specialization is needed
- **Peers**: Other skills in the `c01` domain may be composed in sequence
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
- `[[amos-law-hierarchy-resolver_MOC]]` — skill Map of Content
- `amos-c01-meta-logic-master` — parent skill
- `[[amos-law-hierarchy-resolver-workflow]]` — corresponding workflow
- `amos-law-hierarchy-resolver-agent` — corresponding agent
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[07_SKILLS_MOC]] · [[references_MOC]]

**MOC:** [[07_SKILLS_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-law-hierarchy-resolver
node_type: skill
path: 07_SKILLS/amos-law-hierarchy-resolver/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS_MOC]]
