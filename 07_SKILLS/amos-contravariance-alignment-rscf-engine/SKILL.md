---
title: SKILL
type: skill
source: 07_SKILLS/amos-contravariance-alignment-rscf-engine
name: amos-contravariance-alignment-rscf-engine
description: Contravariance Alignment — RSCF epistemic capability. Use when classifying claims by epistemic state, validating outputs against epistemic and scope constraints, or analyzing evidence structure. Use when amos-rscf-epistemic-master routes to this s...
parent_skill: amos-rscf-epistemic-master
domain: rscf
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-contravariance-alignment-rscf-engine, canon/skill]
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: "1.1.0"
---


# Contravariance Alignment Rscf Engine

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-rscf-epistemic-master`
- **Domain**: rscf
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

RSCF epistemic engine for Contravariance Alignment Rscf Engine

## When to Use

- When classifying claims by epistemic state (VERIFIED, DERIVED, MODEL, UNKNOWN/GAP)
- When validating evidence chains for provenance, freshness, and scope
- When assessing confidence ceilings based on epistemic class
- When detecting falsifiers that would downgrade confidence
- When the parent skill (`amos-rscf-epistemic-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **contravariance_alignment.classify_claim**: Classify claims by epistemic state (VERIFIED, DERIVED, MODEL, UNKNOWN/GAP) and bind to evidence
- **contravariance_alignment.validate_evidence**: Validate evidence chains: provenance, freshness, scope, and regime validity
- **contravariance_alignment.trace_provenance**: Trace output provenance to vault sources and tag with content_hash
- **contravariance_alignment.assess_confidence**: Assess confidence ceiling based on epistemic class and evidence strength
- **contravariance_alignment.detect_falsifier**: Detect falsifiers and downgrade confidence when counter-evidence emerges
- **contravariance_alignment.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **contravariance_alignment.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **contravariance_alignment.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## Vault-Sourced Content

### Source 1: AMOS ALIGNMENT LAYER

> Path: `fractal/AMOS_FRACTAL_CONSCIOUSNESS_WHITEPAPER_FULL_FIXED.md` | Size: 175078 chars | Match score: 5 | content_hash: f70925f6ac8d7eb5

# AMOS ALIGNMENT LAYER

## Canon identity


This edition preserves the source whitepaper while making its epistemic status
explicit. It does **not** treat symbolic resemblance, fractal analogy,
astrological correspondence, quantum vocabulary, or cross-scale similarity as
empirical proof.

## Epistemic classes

```yaml
SOURCE_CLAIM:
  meaning: claim stated by the source document
  status: preserved without automatic validation

OBSERVATION:
  meaning: measurement or directly recorded phenomenon

DERIVED:
  meaning: conclusion logically derived from admitted premises

AMOS_MODEL:
  meaning: Trang/AMOS structural interpretation or formal bridge

SYMBOLIC:
  meaning: metaphor, archetype, analogy, or interpretive mapping

COMPETING:
  meaning: multiple live explanations remain unresolved

UNKNOWN/GAP:
  meaning: evidence is missing, insufficient, or not independently established
```

## Core AMOS firewalls

```text
structural similarity != semantic identity
structural similarity != causation
sequence != causation
logical implication != empirical causal effect
quantum entanglement != evidence of telepathy
interpersonal synchrony != quantum entanglement
fractal analogy != proof of universal fractal ontology
astrological symbolism != physical causal mechanism
observer-dependent measurement != consciousness-causes-reality
cultural usefulness != empirical predictive validity
```

## H/M/L projection

```yaml
H:
  scope: civilization / society / worldview / long-horizon system
M:
  scope: institutions / culture / brain-body systems / interpersonal systems
L:
  scope: cells / signals / observations / local events / individual claims
```

Cross-scale transfer is admitted only when a bridge is explicit:

```text
Bridge(A_scale -> B_scale)
=
{
  preserved_structure,
  lost_information,
  assumptions,
  scope,
  regime,
  provenance,
  falsifiers
}
```

## Master state

```text
Ω_t =
  Matter_t,
  Light_t,
  Time_t,
  Energy_t,
  Biology_t,
  Cognition_t,
  Symbol_t,
  Culture_t,
  Society_t,
  Memory_t,
  Observer_t,
  Provenance_t,
  Epistemic_t,
  Regime_t,
  Contradiction_t
>
```

This is an `AMOS_MODEL` representation for organizing the whitepaper.

## Claim admission

```text
Admit(C)
=
TypeGate(C)
∧ ProvenanceGate(C)
∧ ScopeGate(C)
∧ RegimeGate(C)
∧ CausalGate(C)
∧ ContradictionGate(C)
```

A hard failure is not c

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-contravariance-alignment-rscf-engine_MOC]]

## Examples

- **Scenario**: When classifying claims by epistemic state (VERIFIED, DERIVED, MODEL, UNKNOWN/GAP)
  - **Input**: A query matching this skill's domain (rscf)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When validating evidence chains for provenance, freshness, and scope
  - **Input**: A query matching this skill's domain (rscf)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When assessing confidence ceilings based on epistemic class
  - **Input**: A query matching this skill's domain (rscf)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the rscf domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `amos-rscf-epistemic-master` — routes to this skill when rscf specialization is needed
- **Peers**: Other skills in the `rscf` domain may be composed in sequence
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

- `references/equations_docs.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- `[[amos-contravariance-alignment-rscf-engine_MOC]]` — skill Map of Content
- `amos-rscf-epistemic-master` — parent skill
- `[[amos-contravariance-alignment-rscf-engine-workflow]]` — corresponding workflow
- `amos-contravariance-alignment-rscf-engine-agent` — corresponding agent

