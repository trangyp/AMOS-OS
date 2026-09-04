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

# Absolute Primitive Decomposer

## Identity

Origin architect: **Trang Phan**. Domain: runtime. Parent: amos-os-runtime-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.

## When to Use

- When monitoring runtime stability: drift, oscillation, divergence
- When calibrating feedback control loops for stable operation
- When decomposing complex operations into primitive steps
- When enforcing closed-loop learning and drift alignment
- When the parent skill (`amos-os-runtime-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **runtime.decompose_to_primitives**: Decompose an input concept or structure into the 19 irreducible Absolute Logic primitives (Existence, NonExistence, Causality, Temporal, Informational, Topological, Identity, Convergence, Divergence, Paradox, PositiveLogic, NegativeLogic, ZeroLogic, DualLogic, MultiLogic, MetaLogic, SupraLogic, AntiLogic, NullLogic) while preserving non-mappable residue.
- **runtime.evaluate_interaction_matrix**: Evaluate the 19x19 interaction matrix to determine the deterministic outcome when any two primitives interact, using category-based rules (Pattern, MetaPattern, Logic, MetaLogic).
- **runtime.detect_logic_collapse**: Detect logic collapse states (Dissolution via Paradox+AntiLogic, Driftless via zero derivatives, TerminalQuiet via NullLogic dominance) that indicate structural reasoning failure.
- **runtime.validate_primitive_mapping**: Validate primitive mappings for support, overreach, residue preservation, and epistemic labeling. Reject mappings that violate the 19x19 interaction matrix or claim empirical validity for AMOS_MODEL formalizations.
- **runtime.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **runtime.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **runtime.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: b635376a0788808e) for the full vault-sourced domain knowledge (7963 chars).

## Operations

1. **runtime.decompose_to_primitives**: Decompose an input concept or structure into the 19 irreducible Absolute Logic primitives (Existence, NonExistence, Causality, Temporal, Informational, Topological, Identity, Convergence, Divergence,...
1. **runtime.evaluate_interaction_matrix**: Evaluate the 19x19 interaction matrix to determine the deterministic outcome when any two primitives interact, using category-based rules (Pattern, MetaPattern, Logic, MetaLogic).
1. **runtime.detect_logic_collapse**: Detect logic collapse states (Dissolution via Paradox+AntiLogic, Driftless via zero derivatives, TerminalQuiet via NullLogic dominance) that indicate structural reasoning failure.
1. **runtime.validate_primitive_mapping**: Validate primitive mappings for support, overreach, residue preservation, and epistemic labeling. Reject mappings that violate the 19x19 interaction matrix or claim empirical validity for AMOS_MODE...
1. **runtime.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
1. **runtime.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
1. **runtime.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Absolute Primitive Decomposition

The decomposer breaks any system into its irreducible atomic primitives.

**Decomposition law**: A primitive is atomic when it cannot be further decomposed without losing meaning. `Atomic(x) = NOT EXISTS y: Decompose(x, y) AND Meaningful(y)`

**8 Atomic Logic Units (ALUs)** from ULK:

1. Identity (A = A)
1. Distinction (A != NOT A)
1. Composition (A AND B -> C)
1. Negation (NOT A)
1. Implication (A -> B)
1. Existence (EXISTS A)
1. Universal (FORALL A)
1. Relation (A R B)

**7 Universal Meta-Laws (UMLs)**:

1. Law of Law (no unresolved contradictions)
1. Rule of 2 (at least 2 independent supports for any claim)
1. Rule of 4 (check 4 dimensions: scope, regime, evidence, falsifier)
1. Signal Fidelity Preservation
1. Structural Integrity
1. Provenance completeness
1. Scope/regime compliance

**Decomposition protocol**:

1. Identify the system's declared structure
1. Decompose into constituent parts
1. For each part, check if it can be further decomposed
1. If yes, repeat; if no, the part is atomic
1. Record the decomposition tree with provenance

### Epistemic Boundary

Absolute primitive decomposition is an analytical method. It does not prove the primitives are truly atomic in all possible frameworks, only that they are atomic within the declared framework.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## Validation Gates

______________________________________________________________________

**Links:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

## Related

- [[07_SKILLS/amos-primitive-decomposer/amos-primitive-decomposer_MOC|amos-primitive-decomposer_MOC]]

## Examples

- **Scenario**: When monitoring runtime stability: drift, oscillation, divergence

  - **Input**: A query matching this skill's domain (runtime)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When calibrating feedback control loops for stable operation

  - **Input**: A query matching this skill's domain (runtime)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When decomposing complex operations into primitive steps

  - **Input**: A query matching this skill's domain (runtime)
  - **Output**: Structured result with epistemic labels and provenance

## Anti-Patterns

- **Do not use** for tasks outside the runtime domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval

## Composition

- **Parent**: `amos-os-runtime-master` — routes to this skill when runtime specialization is needed
- **Peers**: Other skills in the `runtime` domain may be composed in sequence
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

- For generic runtime analysis outside the AMOS OS/runtime framework
- To claim empirical validation of OS or runtime theories
- As a substitute for domain-specific runtime or infrastructure evidence
- Outside runtime/OS domain reasoning

## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- \`\` — skill Map of Content
- `amos-os-runtime-master` — parent skill
- \`\` — corresponding workflow
- `amos-primitive-decomposer-agent` — corresponding agent

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-primitive-decomposer
node_type: skill
path: 07_SKILLS/amos-primitive-decomposer/SKILL.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
