---
canon-group: meta
canon-type: framework
rscf-state: derived
rscf-provenance: AMOS_corpus_plus_bounded_runtime
conclusion_class: AMOS_MODEL
epistemic_class: DERIVED
topic: Human Interaction Engine Layer
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/derived
  - human-interaction
created: 2026-08-22
updated: 2026-09-14
origin_architect: Trang Phan
amos_core_target: v4.4
---

# AMOS Human Interaction Engine Layer

Origin architect / steward: **Trang Phan**

## Current operational interpretation

This reference preserves the historical Human Interaction Engine source while binding only the decision-relevant, non-diagnostic interaction semantics to the current bounded runtime.

Historical source family:

- `_00_AMOS_CANON/3.Spicies_Interaction_Engine-HIE.uiface.txt`
- `_00_AMOS_CANON/AMOS_HUMAN_INTELLIGENCE_ENGINE_V0_CORE7.md`
- active repaired Drive reference: `AMOS_HIE_HUMAN_INTERACTION_ENGINE.md`

Bounded repository runtime:

- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/human_interaction_profile_runtime.py`
- `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_human_interaction_profile_runtime.py`

Hard boundaries:

```text
INTERACTION_MODEL != HUMAN_DIAGNOSIS
TEXT_STYLE != BIOLOGICAL_STATE
BEHAVIOR_PATTERN != PERSON_IDENTITY
INFERRED_AFFECT != FELT_STATE_FACT
ATTACHMENT_LABEL != HUMAN_TRUTH
PERSONALIZATION != AUTHORITY
STYLE != SUBJECTIVE_EXPERIENCE
WARMTH != LOVE
CAPABILITY != AUTHORITY
PROPOSAL != COMMIT
SOURCE_CLAIM != VERIFIED_FACT
```

## Historical source versus active runtime

The historical HIE describes seven internal layers including emotional, nervous-system, cognitive, identity, context, and system state. Those descriptions are preserved as source/model history.

They are **not** current permission to infer sensitive mental, clinical, biological, attachment, identity, or diagnostic states from message style.

Current executable projection separates three objects:

1. **Observed interaction inputs** — explicit wording, explicit preferences, task stakes, format constraints, and available evidence state.
2. **Tentative non-clinical hypotheses** — only when they have an observable basis and remain explicitly hypothesis-class.
3. **Expression profile** — presentation policy only; it cannot modify truth, safety constraints, authorization, or effect authority.

## Input contract

### Directly observable / admissible

```text
explicit request
explicit preference
literal text content
format constraint
task type
stakes level
provided evidence
available tool/result status
explicitly supplied context
```

### Optional modalities

Voice, image, screen, sensor, or biosignal information may be used only when the modality is actually available and its provenance is explicit.

```text
UNAVAILABLE_MODALITY != NEGATIVE_OBSERVATION
MISSING_SENSOR != NORMAL_SENSOR_STATE
```

### Not admitted from style alone

```text
clinical diagnosis
psychiatric diagnosis
biological state
nervous-system regulation state
attachment style
personality disorder
hidden identity
medical condition
```

## Tentative hypothesis contract

A text-only interaction hypothesis has the form:

```text
InteractionHypothesis = (
  label,
  observed_basis,
  confidence,
  status,
  clinical=false,
  biological=false
)
```

Current runtime admission requires:

```text
observed_basis != empty
AND nonclinical
AND nonbiological
AND confidence <= 0.60
```

The `0.60` ceiling is an **AMOS_MODEL governance bound**, not a calibrated empirical probability.

Rejected classes remain visible as rejected; they are not converted to low-confidence facts.

## Expression and adaptation

Current expression controls are presentation parameters only:

```text
brevity
formality
technical_depth
warmth
directness
```

Protected fields cannot be changed by personalization:

```text
evidence_visibility
uncertainty_visibility
truth status
safety constraints
authority
effect authorization
```

Explicit user preferences may change permitted presentation fields. Inferred style preferences do not override explicit preferences.

## Stakes rule

Higher stakes may increase evidence and uncertainty visibility; they may never reduce those safeguards.

```text
HIGH_STAKES -> evidence_visibility = 1
HIGH_STAKES -> uncertainty_visibility = 1
```

This is a runtime policy, not a claim about human psychology.

## Legacy migration rule

From legacy Human Intelligence/Personality payloads, only interaction/presentation semantics migrate automatically.

Automatically blocked legacy claim classes include:

```text
SUBJECTIVE_EXPERIENCE
UNIVERSAL_BIOLOGICAL_LAW
INCAPABLE_OF_HARM
DIAGNOSTIC_HUMAN_STATE
```

These remain source history or candidate claims unless separately evidenced and governed.

## Runtime evidence

Executed bounded tests currently cover:

- explicit presentation preference application;
- protected preference-key rejection;
- parameter bounds;
- non-clinical hypothesis admission;
- empty-basis rejection;
- confidence-ceiling rejection;
- sensitive/biological inference rejection;
- rejected-hypothesis exclusion from decisions;
- legacy overreach filtering;
- authority/truth/safety immutability invariants.

Current result: `10/10 PASS` in the bounded test suite.

This validates the implemented contract only. It does not empirically validate a theory of human emotion, cognition, attachment, nervous-system state, or personality.

## Position in AMOS

The Human Interaction Engine is an **interface/presentation and hypothesis-governance layer**.

It does not own:

- URK mathematics;
- ULK logic semantics;
- human diagnosis or biology;
- RSCF truth promotion;
- control-plane authorization;
- durable commit authority.

Execution/authority order remains:

```text
human-facing interface proposal
-> reasoning/domain processing
-> evidence/provenance checks
-> control-plane authorization when an effect is requested
-> commit/executor
```

## Source preservation

Historical HIE constructs such as `emotional_state`, `nervous_system_state`, `identity_state`, and `attachment_mode_hint` remain preserved in source material for provenance. Their presence in a source file is not permission to produce them as verified human-state outputs.

## Related

- [[07_SKILLS/07_SKILLS_MOC|07_SKILLS_MOC]]
- [[00_ROOT/00_HOME|00_HOME]]
- [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- [[11_KNOWLEDGE/engine/HUMAN_INTELLIGENCE_ENGINE_V0|HUMAN_INTELLIGENCE_ENGINE_V0]]

RSCF-NODE
node_id: amos-c05-mind-behavior-master-human-interaction-engine-layer
node_type: reference
path: 07_SKILLS/amos-c05-mind-behavior-master/references/human_interaction_engine_layer.md
claim_class: DERIVED
canonical_status: CONDITIONAL
runtime_status: IMPLEMENTED_BOUNDED
validation_status: VALIDATED_BOUNDED
RSCF-RELATIONS:
- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]
- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]
- IMPLEMENTED_BY: `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/human_interaction_profile_runtime.py`
- VERIFIED_BY: `04_RUNTIME/01_REFERENCE_IMPLEMENTATION/test_human_interaction_profile_runtime.py`
