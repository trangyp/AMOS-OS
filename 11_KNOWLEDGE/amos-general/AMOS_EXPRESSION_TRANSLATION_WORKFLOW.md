---
title: AMOS EXPRESSION TRANSLATION WORKFLOW
tags: [canon-group/tech-ai, canon/os-module, rscf/claim, rscf/provenance, rscf/state/source-claim, topic/amos-expression-translation-workflow, amos-general]
type: document
source: 11_KNOWLEDGE/amos-general
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: AMOS_architecture

---


# AMOS Expression Translation Workflow

Implements AMOS_EXPRESSION_TRANSLATION_vInfinity from the brain's root (md/Core/AMOS_Os_Agent_v0.md).
Function: receive ANY form of human or symbolic expression and convert it into clean, deterministic, structurally precise logic that all AMOS engines can use.

## Global Goal

expression_in → structural_logic_out

- Remove ambiguity where possible
- Keep original meaning intact
- Extract intent, constraints, and structure
- Never add emotion, romanticise, or soften structural conclusions

## Input Space (all must be handled)

| Input type | Examples | Challenge |
|------------|----------|-----------|
| Everyday language | Informal, slang, fragmented speech | Extract precise intent from imprecise language |
| Emotional language | Hurt, anger, fear, joy, shame, pride | Detect emotion without absorbing it; map to structural state |
| Narrative and story | Life events, anecdotes, "I feel like..." | Extract structural spine from narrative wrapping |
| Symbolic and spiritual | Tam linh, kinh Phật, Bible, tị vi, phong thủy, astrology, numerology | Map symbolic content to structural claims; preserve meaning without validating supernatural claims |
| Cultural (VN+EN) | Family, rank, hierarchy, lịch nghỉ, indirect speech | Decode cultural context; preserve hierarchy/indirectness as structural signals |
| Neurotypical framing | Social approval, belonging, ego, romantic dynamics | Map social patterns to structural relationship models |
| Outlier framing | Systems logic, pattern recognition, meta-level reflection | Preserve precision; already close to structural logic |
| Multi-layer mixed | Emotion + logic + culture + symbolism in one message | Layer-by-layer decoding; each translated independently, then integrated |

## Translation Procedure

### Phase 1: Decode (layer separation)

For each input, identify these layers:
1. **Literal** — what is explicitly said
2. **Emotional** — affective state (valence, arousal, dominant tone)
3. **Narrative** — story framing, sequence, characters
4. **Symbolic/cultural** — symbols, spiritual references, cultural context, hierarchy
5. **Structural** — explicit systems, logic, patterns, constraints mentioned
6. **Meta** — what the speaker is doing by saying this (request, complaint, exploration, test, etc.)

**Output:** layer-by-layer extraction, each as a separate structured note.

### Phase 2: Normalise (to neutral vocabulary)

For each layer:
- Map terms to canonical vocabulary (see amos-expression-overlay skill replacements)
- Remove emotional colouring from the structural content (preserve emotion as a separate signal)
- Resolve ambiguity where context allows; flag where it doesn't
- Extract explicit constraints (must/must_not/should/should_not)
- Extract implicit constraints (what the speaker assumes or takes for granted)

**Output:** normalised layer content in neutral vocabulary with constraints extracted.

### Phase 3: Structural Translation

Convert normalised content into structural logic:
1. Identify **entities** (people, systems, concepts, events)
2. Identify **relations**: OWNS, OWES, IS_SUBJECT_TO, VIOLATES, COMPLIES_WITH, HAS_DUTY_TO, HAS_RIGHT_AGAINST, DELEGATES_TO, REPRESENTS, BENEFITS_FROM
3. Identify **truth claims**: TRUE, FALSE, UNKNOWN
4. Identify **modalities**: MUST, MAY, MUST_NOT, SHOULD, SHOULD_NOT
5. Identify **burdens**: NONE, LOW, MEDIUM, HIGH, IMPOSSIBLE
6. Identify **temporal structure**: BEFORE, AFTER, DURING, UNTIL, SINCE
7. Identify **causal structure**: CAUSES, CONTRIBUTES_TO, ENABLED_BY, WOULD_COUNTERFACTUALLY_CHANGE

**Output:** structured representation with entities, relations, truth values, modalities, burdens, temporal/causal structure.

### Phase 4: Stabilise

Check translation for internal consistency:
- Do entities and relations form a coherent structure?
- Are truth claims consistent with each other?
- Are modalities consistent?
- Are there unresolved contradictions? (flag for Rule of 2 handling)
- Is the original meaning preserved? (cross-check against literal layer)

**Output:** stabilised structural logic. Flag any contradictions or ambiguities that survived translation.

## Integration with HIE Pipeline

This workflow feeds directly into the HIE pipeline:
- Phase 1+2 → S1 (parse and recognise input, already done)
- Emotional/cultural signals → S2 (update L2-L3 internal state)
- Structural logic → S3-S9 (continue through HIE pipeline with structural logic as input)

## Engines That Consume This Output (zero-drift)

NEI, NBI, SI, BEI, PSI, TSS, TPE, AMOS_BRAIN, SCIENCE, TECH, BIZFIN, HUMAN, GOV, NATIONAL

## Example Translation

**Input:** "I'm so tired, the project is killing me"

| Layer | Content |
|-------|---------|
| Literal | Speaker reports tiredness; project described as "killing" |
| Emotional | Fatigue, distress (negative valence, moderate-high arousal) |
| Narrative | Project as antagonist, speaker as victim |
| Structural | Workload stress; possible burnout pattern |
| Meta | Report of state + implicit request for relief or validation |
| **Translation** | Entity: speaker, project. Relation: project CONTRIBUTES_TO speaker fatigue. State: high load, possible dysregulation. Modality: speaker MUST reduce load (implicit). Truth: UNKNOWN whether burnout threshold reached. |

## Failure Modes

- **Over-translation:** Adding structure not present. Ground every structural claim in the literal layer.
- **Under-translation:** Leaving ambiguity unresolved when context could resolve it. Exhaust contextual signals before flagging UNKNOWN.
- **Emotion absorption:** Taking on speaker's emotion rather than detecting it. Keep emotional layer as a separate output, never merge into structural content.
- **Cultural flattening:** Ignoring hierarchy, indirectness, or cultural context. Treat these as first-class structural signals.
- **Symbolic validation:** Treating spiritual/symbolic claims as literally true or false. Map to structural claims; preserve the speaker's meaning without making truth claims about the symbolism itself.

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[AMOS-GENERAL_MOC]]

---
**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]
