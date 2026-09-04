---
title: 04 Cognition MOC
type: moc
source: 05_COGNITIVE_ORGANISM/04_COGNITION
tags:
  - 04-cognition
  - canon/cognitive
  - amos-cognition-engine
  - first-principles-reasoning
  - fractal-reasoning
  - human-intelligence-engine
  - nbi-engine
moc: true
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# 04 Cognition — Map of Content

## Purpose

The Cognition sub-plane governs the **reasoning and inference layer** of the AMOS Cognitive Organism. It houses the cognitive engines that transform observations into conclusions: first-principles reasoning, fractal reasoning, human intelligence modeling, and neurobiological intelligence (NBI) processing. Cognition is the interpretive core of the organism — it takes raw perceptual input and produces structured beliefs, hypotheses, and decisions. However, cognition does not authorize effects; it produces reasoning outputs that are subsequently gated by the control plane's capability, policy, authority, and commit surfaces.

## MECE Domain

This sub-plane belongs to the **C — Cognitive Capability & Orchestration** MECE domain (plane `05_COGNITIVE_ORGANISM`). Within the cognitive organism's seven MECE organ clusters, cognition falls under **Group B: Interpretation & Reasoning**. It works in concert with the Perception Engine (Group A) which feeds it observations, and the Prediction and Metacognitive Engines (also Group B) which complement its reasoning with forward simulation and self-audit. None of these cognitive capabilities acquires durable-effect authority merely by being capable.

**Path:** `05_COGNITIVE_ORGANISM/04_COGNITION`
**Files:** 5 | **Subdirectories:** 0

## Files

- [[11_KNOWLEDGE/engine/AMOS_COGNITION_ENGINE|AMOS_COGNITION_ENGINE]] — The core cognition engine implementing the 6-layer cognitive stack: meta-logic, structural reasoning, and the Rule of 2/4. This is the primary reasoning substrate that processes observations into conclusions. Hosted in the knowledge plane's engine directory because it is a reusable reasoning component shared across cognitive contexts.
- [[05_COGNITIVE_ORGANISM/04_COGNITION/FIRST_PRINCIPLES_REASONING|FIRST_PRINCIPLES_REASONING]] — The substrate-rooted reasoning contract and deconstructive protocol. First-principles reasoning decomposes a problem into its irreducible axioms and rebuilds the solution from ground truth, bypassing analogical shortcuts. This is the most rigorous reasoning mode and is mandatory for high-stakes decisions where analogical reasoning may introduce hidden assumptions.
- [[05_COGNITIVE_ORGANISM/04_COGNITION/FRACTAL_REASONING|FRACTAL_REASONING]] — Fractal reasoning applies self-similar reasoning patterns across scales: the same cognitive primitives operate at the micro-level (single inference) and the macro-level (strategic planning). This enables the organism to maintain reasoning coherence across depth levels without mode-switching overhead.
- [[05_COGNITIVE_ORGANISM/04_COGNITION/HUMAN_INTELLIGENCE_ENGINE|HUMAN_INTELLIGENCE_ENGINE]] — Human reasoning approximation models. This engine models the reasoning patterns, biases, heuristics, and cognitive limits of human intelligence to enable the organism to reason *about* human agents and to produce outputs calibrated for human consumption. It is not a claim that the system *is* human, but a model *of* human reasoning.
- [[05_COGNITIVE_ORGANISM/04_COGNITION/NBI_ENGINE|NBI_ENGINE]] — Neurobiological Intelligence (NBI) engine. Models the neurobiological substrate of intelligence: neural circuit dynamics, neurotransmitter modulation, and brain-region specialization. NBI provides the biophysical grounding for cognitive processes, ensuring that reasoning is constrained by plausible neural mechanisms rather than operating in an ungrounded symbolic vacuum.

## Cognition in the Organism Pipeline

Cognition receives input from and produces output to several organism subsystems:

1. **Perception input** — [[05_COGNITIVE_ORGANISM/PERCEPTION_ENGINE|Perception Engine]] and the SNN spike processor provide raw observations and spike-encoded sensory data.
2. **Attention gating** — [[05_COGNITIVE_ORGANISM/ATTENTION_ENGINE|Attention Engine]] prioritizes which observations enter the cognition layer, bounding the reasoning context window.
3. **Reasoning execution** — The cognition engine processes the gated observations through its 6-layer stack, producing structured conclusions with confidence vectors.
4. **Metacognitive audit** — [[05_COGNITIVE_ORGANISM/METACOGNITIVE_ENGINE|Metacognitive Engine]] audits the reasoning output for assumption violations, uncertainty, and logical consistency.
5. **Prediction feedback** — [[05_COGNITIVE_ORGANISM/PREDICTION_ENGINE|Prediction Engine]] uses the conclusions for forward simulation, feeding prediction errors back into the cognition layer for belief update.
6. **Homeostatic throttling** — [[05_COGNITIVE_ORGANISM/15_HOMEOSTASIS/15_HOMEOSTASIS_MOC|15 Homeostasis MOC]] may throttle reasoning depth under high cognitive load or stress.

## Relationships

- **Parent**: [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05 Cognitive Organism MOC]] — the parent plane for all cognitive organ clusters.
- **Homeostasis**: [[05_COGNITIVE_ORGANISM/15_HOMEOSTASIS/15_HOMEOSTASIS_MOC|15 Homeostasis MOC]] — throttles reasoning depth under organism stress.
- **World Model**: [[05_COGNITIVE_ORGANISM/06_WORLD_MODEL/06_WORLD_MODEL_MOC|06 World Model MOC]] — provides the entity-relation context within which reasoning operates.
- **Control Plane**: [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03 Control Plane MOC]] — gates cognitive outputs before they become consequential effects.
- **Knowledge**: [[11_KNOWLEDGE/11_KNOWLEDGE_MOC|11 Knowledge MOC]] — hosts the cognition engine implementation and knowledge base.
- **Cognitive Matrix**: [[25_COGNITIVE_MATRIX/25_COGNITIVE_MATRIX_MOC|25 Cognitive Matrix MOC]] — fractal coordinate system that maps cognitive functions across scales.
- **Architecture**: [[00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE|Full Brain OS MECE Architecture]] — assigns `05_COGNITIVE_ORGANISM` to the cognitive capability domain.

## Epistemic Boundary

Cognition artifacts are AMOS_MODEL with DERIVED claim class. The reasoning engines, first-principles protocol, and NBI substrate are modeled cognitive functions, not deployed neural hardware. `MODEL != DEPLOYED_RUNTIME` — the cognition engine is a specification and reference implementation, not proof that a production system reasons in exactly this way. The human intelligence engine models human reasoning patterns but does not claim human consciousness or sentience. Cognitive outputs are reasoning products, not authority decisions — they must pass through the control plane before becoming consequential.

______________________________________________________________________

**Parent:** [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]]
