---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Cognitive Organism Map
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

# Cognitive Organism Map

This map is the semantic routing surface for `05_COGNITIVE_ORGANISM`. It is derived from the active
Cognitive Organism and Full Brain sources. It indexes responsibilities; it does not create authority,
implementation, empirical truth, or biological equivalence.

## 1. Reading order

1. [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]] — plane purpose, architecture and organ registry.
2. [[05_COGNITIVE_ORGANISM/COGNITIVE_ORGANISM_README|COGNITIVE_ORGANISM_README]] — operating model, loops, inputs/outputs and failure semantics.
3. [[05_COGNITIVE_ORGANISM/COGNITIVE_ORGANISM_COGNITIVE_ORGANISM_CONTRACT|COGNITIVE_ORGANISM_CONTRACT]] — normative plane contract.
4. [[01_CANON/03_COGNITION_CANON/COGNITIVE_ORGANISM_CANON|COGNITIVE_ORGANISM_CANON]] — source-bound cognition canon surface.
5. [[01_CANON/03_COGNITION_CANON/FULL_BRAIN_OS_CANON|FULL_BRAIN_OS_CANON]] — broader Full Brain boundary.
6. [[11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL|AMOS_COGNITIVE_ORGANISM_OS_DETAIL]] — richer source knowledge when detail is decision-relevant.

## 2. MECE functional partition

The organism's functions are routed into seven non-overlapping responsibility groups. Cross-group
dependencies are edges, not duplicate ownership.

```text
A. INPUT / REPRESENTATION
   Perception · Attention · Context · WorldModel

B. INTERPRETATION / REASONING
   Cognition · Hypothesis · Simulation · DecisionSupport

C. AFFECT / DRIVE
   EmotionModel · Instinct · Motivation · Goal

D. PROSPECTIVE / ACTION FORMATION
   Planning · AgencyProposal · ActionInterface

E. ADAPTATION / CONTINUITY
   Memory · Learning · Reflection · Identity · Lifecycle

F. SOCIAL / EXPRESSION
   Social · Expression

G. REGULATION / ASSURANCE
   Homeostasis · Risk · Safety · Repair · Observability
```

`MECE_PARTITION != INDEPENDENT_EXECUTION`

A function may depend on several groups while retaining one primary responsibility owner.

## 3. Core substrates

The source-defined substrates cut across all functions:

```text
Identity
State
Flow
Memory
Governance
```

They are substrates, not additional organs. In particular:

`STATE != ORGAN` · `MEMORY_SUBSTRATE != MEMORY_RETRIEVAL_OPERATION` · `GOVERNANCE != COGNITION`

## 4. Governed cognitive loop

```text
OBSERVE
→ REPRESENT
→ ATTEND
→ CONTEXTUALIZE
→ RETRIEVE
→ INTERPRET / REASON
→ PRESERVE COMPETING HYPOTHESES
→ SIMULATE
→ PLAN
→ DECIDE / PROPOSE
→ AUTHORITY GATE
→ ACT IF AUTHORIZED
→ OBSERVE OUTCOME
→ LEARN
→ REFLECT
→ REGULATE / REPAIR
```

Loops may short-circuit when claim, decision and action sufficiency are reached. They must escalate
when critical gaps, provenance correlation, scope/regime mismatch, stale premises, contradictions,
causal ambiguity or irreversible stakes can change the result.

## 5. Cross-plane routing

```text
01_CANON      -> normative constraints
02_KERNEL     -> reasoning/state-integrity primitives
03_CONTROL    -> authority and effect admission
04_RUNTIME    -> bounded execution/replay/repair
05_ORGANISM   -> cognitive orchestration
06_AGENTS     -> delegated goal-bearing actors where admitted
07_SKILLS     -> reusable capability procedures
26_WORKFLOWS  -> explicit process/state transitions
10_MEMORY     -> durable/typed memory
11_KNOWLEDGE  -> source/evidence/knowledge graph
12_STATE      -> versioned state
13_MODELS     -> models and simulations
16_SCHEMAS    -> typed contracts
17_OBSERVABILITY -> receipts/metrics/traces
18_SECURITY   -> trust and access constraints
19_TESTS      -> executable validation
20_OPERATIONS -> recovery and operational governance
25_MATRIX     -> fractal cognitive decomposition
```

## 6. Map boundary

```text
MAP EDGE != DEPENDENCY PROOF
MAP LOCATION != AUTHORITY
MAP COMPLETENESS != SYSTEM COMPLETENESS
COGNITIVE FUNCTION != EFFECT AUTHORITY
MODEL != OBSERVATION
ORGANISM_MODEL != BIOLOGICAL_ORGANISM
UNKNOWN/GAP != PASS
```

Cross-plane dependencies must be established by the referenced artifact's own typed
contract/provenance rather than inferred from this map.

**Parent:** [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
