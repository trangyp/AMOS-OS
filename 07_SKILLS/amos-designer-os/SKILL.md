---
schema_version: 1.0
title: SKILL — Amos Designer Os
type: skill
source: 07_SKILLS/amos-designer-os
name: amos-designer-os
description: Designer Os — technology and engineering capability. Use when software
  development, engineering design, or technical architecture. Use when amos-c10-tech-engineering-master
  routes to this specialized capability. Do not use for generic tasks outside c10
  domain.
parent_skill: amos-c10-tech-engineering-master
domain: c10
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags:
- type/skill
- type/skill
- domain/tech-engineering
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
- L8_execution
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance:
- L0
- L1
- L2
- L4
- L5
- L7
- L8
- L16
- L17
- L18
license: MIT
steward: Trang Phan
---

# Designer Os

## Identity

Origin architect: **Trang Phan**. Domain: c10. Parent: amos-c10-tech-engineering-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.
## When to Use

- When analyzing software architecture: patterns, dependencies, coupling
- When discovering program behavior via black-box analysis or symbolic execution
- When verifying code facts: type safety, memory safety, termination
- When enforcing bounded code: resource, time, and capability limits
- When the parent skill (`amos-c10-tech-engineering-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **designer.analyze_architecture**: Analyze software architecture: patterns, dependencies, coupling, cohesion
- **designer.discover_program**: Discover program behavior: black-box analysis, symbolic execution, fuzzing
- **designer.verify_code_facts**: Verify code facts: type safety, memory safety, termination, complexity
- **designer.optimize_performance**: Optimize performance: profiling, bottleneck analysis, and resource tuning
- **designer.enforce_bounds**: Enforce bounded code: resource limits, time limits, and capability limits
- **designer.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **designer.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **designer.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 3a6ed833110a8adb) for the full vault-sourced domain knowledge (5421 chars).

## Operations

1. **designer.analyze_architecture**: Analyze software architecture: patterns, dependencies, coupling, cohesion
2. **designer.discover_program**: Discover program behavior: black-box analysis, symbolic execution, fuzzing
3. **designer.verify_code_facts**: Verify code facts: type safety, memory safety, termination, complexity
4. **designer.optimize_performance**: Optimize performance: profiling, bottleneck analysis, and resource tuning
5. **designer.enforce_bounds**: Enforce bounded code: resource limits, time limits, and capability limits
6. **designer.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
7. **designer.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
8. **designer.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/amos-general/A/Designer/AMOS Designer OS.md` (content_hash: 3985deaea31b207d) (vault canon, SOURCE_CLAIM)

### Designer OS

From Cosmo Brain AMOS Designer OS: Standalone shell for organizing ideas, roles, and brain model auditably. 5-file standalone shell with 7-layer brain model.

**5 Files**:
- `AMOS.brain` (2,066B): designer-facing control file (identity, goals, constraints, brain model)
- `AMOS.config.json` (506B): runtime configuration
- `README.txt` (1,410B): setup and usage instructions
- `run_amos.py` (4,926B): simple runtime -- loads brain, config, runs workers, logs events
- `workers.py` (3,323B): small worker layer (WORKER_REGISTRY, WorkerResponse)

**4 Goals**:
1. Model multi-layer reasoning and systemic behaviour
2. Maintain full auditability of every reasoning step
3. Keep humans in control, not the machine
4. Support sovereign-grade AI governance and compliance

**4 Constraints**:
1. Deterministic execution (no hidden randomness)
2. Every decision must be loggable and explainable
3. No irreversible actions without explicit human confirmation
4. All worker actions pass through a single motor layer

**7-Layer Brain Model**:
1. **Sensory layer**: raw inputs (text, data, events, metrics)
2. **Perceptual layer**: pattern detection from inputs
3. **Concept layer**: stable concepts, entities, relationships
4. **Narrative layer**: stories, scenarios, timelines
5. **Causal layer**: cause-effect chains, interventions, levers
6. **Systemic layer**: multi-system, multi-actor, multi-decade reasoning
7. **Meta layer**: self-audit, ethics, risk, invariants, boundaries

**Designer OS laws**:
- `DESIGNER != USER`: the designer organizes the system; the user operates it
- `AUDITABLE != TRANSPARENT**: auditable means decisions are loggable; transparent means visible in real-time
- `DETERMINISTIC != RIGID**: deterministic means reproducible; rigid means inflexible

### Epistemic Boundary

Designer OS is a standalone shell architecture. It does not prove all design is auditable, that the 7-layer model is exhaustive, or that deterministic execution covers all cases.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not

---
**Links:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

## Related

- [[07_SKILLS/amos-designer-os/amos-designer-os_MOC|amos-designer-os_MOC]]

## Examples

- **Scenario**: When analyzing software architecture: patterns, dependencies, coupling
  - **Input**: A query matching this skill's domain (c10)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When discovering program behavior via black-box analysis or symbolic execution
  - **Input**: A query matching this skill's domain (c10)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When verifying code facts: type safety, memory safety, termination
  - **Input**: A query matching this skill's domain (c10)
  - **Output**: Structured result with epistemic labels and provenance


## Validation Gates

- **L0 Integrity**: All structural elements accounted for; no silent gaps
- **L1 Epistemic**: Every claim tagged with epistemic class (SOURCE_CLAIM / DERIVED / AMOS_MODEL)
- **L5 Scope**: Analysis confined to declared scope and domain
- **L7 Authority**: No autonomous action beyond authority boundary

## Anti-Patterns

- **Do not use** for tasks outside the c10 domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-c10-tech-engineering-master` — routes to this skill when c10 specialization is needed
- **Peers**: Other skills in the `c10` domain may be composed in sequence
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

- For generic engineering analysis outside the tech/engineering framework
- To claim empirical validation of software engineering laws
- As a substitute for domain-specific technical or engineering evidence
- Outside tech/engineering domain reasoning

## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `` — skill Map of Content
- `amos-c10-tech-engineering-master` — parent skill
- `` — corresponding workflow
- `amos-designer-os-agent` — corresponding agent
---

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-designer-os
node_type: skill
path: 07_SKILLS/amos-designer-os/SKILL.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
