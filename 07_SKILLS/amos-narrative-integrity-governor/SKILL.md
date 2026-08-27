---
title: SKILL
type: skill
source: 07_SKILLS/amos-narrative-integrity-governor
name: amos-narrative-integrity-governor
description: Narrative Integrity Governor — mind and behavior capability. Use when psychological analysis, behavioral reasoning, or cognitive modeling. Use when amos-c05-mind-behavior-master routes to this specialized capability.
parent_skill: amos-c05-mind-behavior-master
domain: c05
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-narrative-integrity-governor, canon/skill]
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: "1.1.0"
---


# Narrative Integrity Governor

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c05-mind-behavior-master`
- **Domain**: c05
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Mind-behavior engine for Narrative Integrity Governor

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

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/trang/Trang Reality Architecture.md` (content_hash: 713f2b286bff07a0) (vault canon, SOURCE_CLAIM)
> **Additional source**: `_00_Cosmo brain/amos-general/A/Universe/AMOS_UNIVERSE_OS_FULL_BUNDLE.md` (content_hash: c3aef595e3657ad7) (vault canon, SOURCE_CLAIM)

### Narrative Integrity Governor

From Trang Reality Architecture: Narrative Integrity as self-story remaining coherent with lived reality. From Universe OS: Civilization narrative integrity as system identity field.

**Narrative integrity definition**: Self-story remaining coherent with lived reality.

**6 Dependencies of narrative integrity**:
1. **Truthful memory**: memory must be truthful
2. **Coherent values**: values must be coherent
3. **Embodied alignment**: actions must align with stated values
4. **Behavioral consistency**: behavior must be consistent over time
5. **Reality contact**: the narrative must maintain contact with reality
6. **Adaptive revision**: the narrative must adapt when reality changes

**4 Causes of narrative collapse**:
1. Self-story contradicts reality
2. Trauma fragments continuity
3. Social masking replaces authenticity
4. Awareness can no longer reconcile contradiction

**Anti-faking architecture** (from Trang Master Detail):
- Penalizes narrative drift, deception gaps, value drift, and self-deception
- Narrative integrity is symbolic continuity stabilization

**Civilization narrative integrity** (from Universe OS):
- `civilization narrative integrity` as system identity field
- `knowledge_integrity_index: float[0..1]`
- `civilization_type == CCI.Steward_State -> lower planetary entropy growth`

**Governor laws**:
- `NARRATIVE != FICTION`: narrative is self-story; fiction is deliberate invention
- `INTEGRITY != CONSISTENCY**: integrity requires reality contact; consistency is internal only
- `COLLAPSE != CHANGE**: collapse is integrity loss; change can be adaptive

### Epistemic Boundary

Narrative integrity governance is an epistemic construct. It does not prove all narrative collapse is detected, that the 6 dependencies are exhaustive, or that integrity can always be restored.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epis

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-narrative-integrity-governor_MOC]]

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
- `[[amos-narrative-integrity-governor_MOC]]` — skill Map of Content
- `amos-c05-mind-behavior-master` — parent skill
- `[[amos-narrative-integrity-governor-workflow]]` — corresponding workflow
- `amos-narrative-integrity-governor-agent` — corresponding agent

