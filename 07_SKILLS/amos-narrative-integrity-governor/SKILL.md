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

# Narrative Integrity Governor

## Identity

Origin architect: **Trang Phan**. Domain: c05. Parent: amos-c05-mind-behavior-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.

## When to Use

- When modeling cognitive processes: attention, awareness, compression
- When allocating attention resources across competing demands
- When assessing awareness levels and meta-cognition
- When governing artistic and emotional expression within bounds
- When the parent skill (`amos-c05-mind-behavior-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **narrative_integrity.model_cognition**: Model cognitive processes: attention, awareness, compression, and inference
- **narrative_integrity.allocate_attention**: Allocate attention resources across competing demands and priorities
- **narrative_integrity.assess_awareness**: Assess awareness levels: meta-cognition, self-monitoring, and calibration
- **narrative_integrity.govern_expression**: Govern artistic and emotional expression within healthy bounds

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 5b43952d71cab1c1) for the full vault-sourced domain knowledge (9047 chars).

- **narrative_integrity.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **narrative_integrity.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **narrative_integrity.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Operations

1. **narrative_integrity.model_cognition**: Model cognitive processes: attention, awareness, compression, and inference
1. **narrative_integrity.allocate_attention**: Allocate attention resources across competing demands and priorities
1. **narrative_integrity.assess_awareness**: Assess awareness levels: meta-cognition, self-monitoring, and calibration
1. **narrative_integrity.govern_expression**: Govern artistic and emotional expression within healthy bounds
1. **narrative_integrity.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
1. **narrative_integrity.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
1. **narrative_integrity.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/trang/Trang Reality Architecture.md` (content_hash: 713f2b286bff07a0) (vault canon, SOURCE_CLAIM)
> **Additional source**: `_00_Cosmo brain/amos-general/A/Universe/AMOS_UNIVERSE_OS_FULL_BUNDLE.md` (content_hash: c3aef595e3657ad7) (vault canon, SOURCE_CLAIM)

### Narrative Integrity Governor

From Trang Reality Architecture: Narrative Integrity as self-story remaining coherent with lived reality. From Universe OS: Civilization narrative integrity as system identity field.

**Narrative integrity definition**: Self-story remaining coherent with lived reality.

**6 Dependencies of narrative integrity**:

1. **Truthful memory**: memory must be truthful
1. **Coherent values**: values must be coherent
1. **Embodied alignment**: actions must align with stated values
1. **Behavioral consistency**: behavior must be consistent over time
1. **Reality contact**: the narrative must maintain contact with reality
1. **Adaptive revision**: the narrative must adapt when reality changes

**4 Causes of narrative collapse**:

1. Self-story contradicts reality
1. Trauma fragments continuity
1. Social masking replaces authenticity
1. Awareness can no longer reconcile contradiction

**Anti-faking architecture** (from Trang Master Detail):

- Penalizes narrative drift, deception gaps, value drift, and self-deception
- Narrative integrity is symbolic continuity stabilization

**Civilization narrative integrity** (from Universe OS):

- `civilization narrative integrity` as system identity field
- `knowledge_integrity_index: float[0..1]`
- `civilization_type == CCI.Steward_State -> lower planetary entropy growth`

**Governor laws**:

- `NARRATIVE != FICTION`: narrative is self-story; fiction is deliberate invention
- \`INTEGRITY != CONSISTENCY\*\*: integrity requires reality contact; consistency is internal only
- \`COLLAPSE != CHANGE\*\*: collapse is integrity loss; change can be adaptive

### Epistemic Boundary

Narrative integrity governance is an epistemic construct. It does not prove all narrative collapse is detected, that the 6 dependencies are exhaustive, or that integrity can always be restored.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- \*\*Epis

______________________________________________________________________

**Links:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

## Related

- [[07_SKILLS/amos-narrative-integrity-governor/amos-narrative-integrity-governor_MOC|amos-narrative-integrity-governor_MOC]]

## Examples

- **Scenario**: When modeling cognitive processes: attention, awareness, compression

  - **Input**: A query matching this skill's domain (c05)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When allocating attention resources across competing demands

  - **Input**: A query matching this skill's domain (c05)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When assessing awareness levels and meta-cognition

  - **Input**: A query matching this skill's domain (c05)
  - **Output**: Structured result with epistemic labels and provenance

## Validation Gates

- **L0 Integrity**: All structural elements accounted for; no silent gaps
- **L1 Epistemic**: Every claim tagged with epistemic class (SOURCE_CLAIM / DERIVED / AMOS_MODEL)
- **L5 Scope**: Analysis confined to declared scope and domain
- **L7 Authority**: No autonomous action beyond authority boundary

## Anti-Patterns

- **Do not use** for tasks outside the c05 domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval

## Composition

- **Parent**: `amos-c05-mind-behavior-master` — routes to this skill when c05 specialization is needed
- **Peers**: Other skills in the `c05` domain may be composed in sequence
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

- For generic psychological analysis outside the mind/behavior framework
- To claim empirical validation of consciousness or cognitive theories
- As a substitute for domain-specific psychological or psychiatric evidence
- Outside mind/behavior domain reasoning

## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- \`\` — skill Map of Content
- `amos-c05-mind-behavior-master` — parent skill
- \`\` — corresponding workflow
- `amos-narrative-integrity-governor-agent` — corresponding agent

______________________________________________________________________

**Related:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]] · [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]] · [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]] · references_MOC

**MOC:** [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]

**Trang Framework:** [[11_KNOWLEDGE/TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS|TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

______________________________________________________________________

RSCF-NODE
node_id: amos-narrative-integrity-governor
node_type: skill
path: 07_SKILLS/amos-narrative-integrity-governor/SKILL.md
RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]
- CHILD_OF: [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
