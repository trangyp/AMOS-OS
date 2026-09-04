---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Sota Cognitive Architecture 2026
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

# SOTA Cognitive Architectures 2026

> **Status:** `ACTIVE` · **Epistemic class:** `OBSERVATION`
> **Scope:** Global cognitive architecture landscape — classical through modern, mapped to AMOS integration points.

---

## 0. Purpose

This research brief surveys the state of cognitive architecture research as of September 2026. Cognitive architectures (CAs) are computational frameworks that aim to formalize the full architecture of the mind — perception, memory, reasoning, learning, metacognition, and (in some formulations) consciousness — into a single coherent system.

The brief serves two functions:
1. **Landscape mapping** — cataloging classical and modern architectures, key paradigms, and consciousness models that define the field.
2. **AMOS integration positioning** — identifying where AMOS's [[05_COGNITIVE_ORGANISM/COGNITIVE_STACK_30_LAYER_SPECIFICATION|30-layer cognitive stack]], [[05_COGNITIVE_ORGANISM/GLOBAL_WORKSPACE_IMPLEMENTATION|global workspace implementation]], [[02_KERNEL/ABSOLUTE_LOGIC_KERNEL_19x19|Absolute Logic Kernel]], and [[11_KNOWLEDGE/RSCF_FORMAL_SPECIFICATION|RSCF formal specification]] align with, diverge from, or extend the broader field.

> [!NOTE] Epistemic Boundary
> All claims in this brief are classified as `OBSERVATION` / `DERIVED`. AMOS architectural parallels are structural mappings, not claims of equivalent implementation or validation. See [[03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT]] for authority and promotion rules.

---

## 1. Classical Architectures

Classical cognitive architectures (1980s–2010s) established the foundational vocabularies and design patterns still in use. Each targets a "Universal Intermediate Theory of Cognition" — a substrate-independent description of cognitive function.

### 1.1 Soar (Laird, Newell, Rosenbloom — 1987–present)

| Attribute | Detail |
|-----------|--------|
| **Proponents** | John E. Laird, Allen Newell, Paul Rosenbloom |
| **Core abstraction** | Problem spaces with states, operators, and search |
| **Key mechanism** | Impasse-driven chunking — when the system cannot select an operator, it creates a new rule via problem-space search and stores it as a production (learning by doing) |
| **Memory systems** | Semantic (long-term production rules), episodic (state sequences), procedural (compiled chunks), imagery (spatial) |
| **Theoretical claim** | Universal Intermediate Theory of Cognition — a single architecture that can implement any cognitive task by defining the appropriate problem space |
| **Scale (2026)** | Soar 9.6+; integrated with reinforcement learning, RLHF-style reward shaping; used in military simulation (USC/ISI), robotics, game AI |
| **AMOS mapping** | Soar's impasse-driven chunking parallels AMOS's adaptive knowledge acquisition at L18–L20 of the [[05_COGNITIVE_ORGANISM/COGNITIVE_STACK_30_LAYER_SPECIFICATION\|30-layer stack]]. Problem spaces map to goal-state management in control planes C4–C6. |

**Strengths:** Well-understood learning mechanism; decades of empirical validation; clean separation of memory systems.

**Weaknesses:** Production system bottleneck at scale; no native treatment of consciousness or affect; limited perceptual grounding; chunking requires explicit impasse detection.

### 1.2 ACT-R (Adaptive Control of Thought — Rational) (Anderson — 1993–present)

| Attribute | Detail |
|-----------|--------|
| **Proponent** | John R. Anderson (Carnegie Mellon) |
| **Core abstraction** | Production system with modular task modules (visual, auditory, motor, declarative, goal,imaginal) |
| **Key mechanism** | Activation-based retrieval — declarative chunks have activation levels determined by base-level learning (power-law forgetting), spreading activation from contextual cues, and noise |
| **Memory systems** | Declarative (symbolic chunks with activation), procedural (IF-THEN productions), associative (spreading activation network) |
| **Theoretical claim** | Rational analysis — cognitive architecture optimizes performance given environmental statistics; memory retrieval is approximately Bayesian |
| **Scale (2026)** | ACT-R 7.0; 600+ published models; cognitive tutor lineage (CMU/ARI); neuroimaging validation (fMRI activation correlates with module usage) |
| **AMOS mapping** | ACT-R's modular task architecture informs AMOS's engine separation (Attention Engine, Memory Engine, Reasoning Engine). Activation-based retrieval maps to L7 (Memory) activation decay in the [[05_COGNITIVE_ORGANISM/COGNITIVE_STACK_30_LAYER_SPECIFICATION\|30-layer stack]]. |

**Strengths:** Strong neuroimaging validation; elegant memory decay model; rational analysis framework connects to Bayesian optimality.

**Weaknesses:** Symbolic production system limits sub-symbolic flexibility; scaling to complex real-world environments is non-trivial; no native metacognitive layer.

### 1.3 LIDA (Learning Intelligent Distribution Agent) (Franklin — 1995–present)

| Attribute | Detail |
|-----------|--------|
| **Proponent** | Stan Franklin (University of Memphis) |
| **Core abstraction** | Global Workspace Theory (GWT) implementation — cognitive cycle as attentional broadcast loop |
| **Key mechanism** | Attentional consciousness — each cognitive cycle (~100–500ms) selects the globally most salient information and broadcasts it to all modules; conscious access = broadcast winner |
| **Memory systems** | Episodic (event memories), semantic (statistical regularities), procedural (skill-like knowledge via classifier nets), sensory (modality-specific buffers) |
| **Theoretical claim** | Functional consciousness emerges from the global broadcast mechanism; consciousness is a process, not a state |
| **Scale (2026)** | LIDA 2.x; used in robotics, virtual agents, game AI; cognitive cycle timing validated against human reaction times |
| **AMOS mapping** | LIDA is the **closest classical ancestor** to AMOS's [[05_COGNITIVE_ORGANISM/GLOBAL_WORKSPACE_IMPLEMENTATION\|global workspace implementation]]. The 9 control planes C1–C9 parallel LIDA's attentional broadcast across modules. AMOS extends LIDA by adding: (a) formal verification substrate ([[02_KERNEL/ABSOLUTE_LOGIC_KERNEL_19x19\|ALAK 19×19]]), (b) structural coherence tracking ([[11_KNOWLEDGE/RSCF_FORMAL_SPECIFICATION\|RSCF]]), (c) 30-layer depth vs. LIDA's ~12 functional modules. |

**Strengths:** Directly grounded in neuroscience (GWT); explicit treatment of consciousness as functional architecture; real-time cognitive cycle.

**Weaknesses:** Limited learning mechanisms; no formal reasoning kernel; scalability to complex domains unproven.

### 1.4 SPA (Semantic Pointer Architecture) (Numenta — 2005–present)

| Attribute | Detail |
|-----------|--------|
| **Proponents** | Jeff Hawkins, Subutai Ahmad, Numenta research team |
| **Core abstraction** | Cortical Learning Algorithm (CLA) — Hierarchical Temporal Memory (HTM) successor; spatial pooling + temporal memory as cortical columns |
| **Key mechanism** | Grid Cells / Temporal Memory Vector (TMV) — neurons encode temporal sequences through sparse distributed representations; prediction via dendritic computation |
| **Memory systems** | Sparse distributed representations (SDR); spatial pooler (encoding stability); temporal memory (sequence learning and prediction) |
| **Theoretical claim** | Neocortex performs prediction through hierarchical temporal memory; all cortical regions share a common algorithm |
| **Scale (2026)** | HTM 0.9.2 (deprecated); Numenta pivoted to biologically-plausible AI research; Grok (commercial); Thousand Brains Theory (2020–2026) — reference frames as cognitive substrate |
| **AMOS mapping** | SPA's hierarchical prediction aligns with predictive processing in L1–L5 of the [[05_COGNITIVE_ORGANISM/COGNITIVE_STACK_30_LAYER_SPECIFICATION\|30-layer stack]]. Sparse distributed representations inform efficiency constraints on RSCF ([[11_KNOWLEDGE/RSCF_FORMAL_SPECIFICATION]]). |

**Strengths:** Neurobiologically grounded; excellent at anomaly detection and temporal prediction; efficient sparse computation.

**Weaknesses:** Limited to temporal/predictive tasks; no symbolic reasoning layer; commercial focus limited academic ecosystem growth.

### 1.5 CLARION (Connectionist Learning with Adaptive Rule Induction ON-line) (Sun — 1992–present)

| Attribute | Detail |
|-----------|--------|
| **Proponent** | Ron Sun (RPI) |
| **Core abstraction** | Dual-process architecture — implicit (sub-symbolic, neural network) vs. explicit (symbolic, rule-based) knowledge interaction |
| **Key mechanism** | Bottom-up knowledge extraction — implicit knowledge (from neural networks) is crystallized into explicit rules through a learning process; top-down knowledge drives decision-making |
| **Memory systems** | Implicit knowledge (connectionist/sub-symbolic), explicit knowledge (symbolic rules), working memory (interface between the two) |
| **Theoretical claim** | Human cognition requires both implicit and explicit knowledge systems that interact bidirectionally; neither alone is sufficient |
| **Scale (2026)** | CLARION-B; validated on social reasoning, metacognition tasks, gaming AI; limited industrial adoption |
| **AMOS mapping** | CLARION's implicit/explicit duality maps to AMOS's separation between probabilistic LLM reasoning (implicit) and the [[02_KERNEL/ABSOLUTE_LOGIC_KERNEL_19x19\|Absolute Logic Kernel]] (explicit deterministic reasoning). The bidirectional interface is analogous to AMOS's L22–L25 (metacognitive integration layers). |

**Strengths:** Principled treatment of implicit/explicit knowledge; validated on metacognition tasks; psychological plausibility.

**Weaknesses:** Scaling implicit/explicit interaction to complex domains is computationally expensive; limited to small-scale demonstrations.

---

## 2. Modern Architectures (2020–2026)

The post-LLM era has produced a new class of cognitive architectures — some emergent from LLM deployment patterns, some deliberately designed by cognitive science labs.

### 2.1 Anthropic Constitutional AI as Implicit Cognitive Architecture

| Attribute | Detail |
|-----------|--------|
| **System** | Claude (Anthropic) with Constitutional AI (CAI) training |
| **Core abstraction** | Constitutional workspace — principled reasoning within a structured value space (J-space) |
| **Key mechanism** | Constitutional principles act as implicit cognitive constraints; J-space (Anthropic's term for structured reasoning space) functions as a bounded global workspace |
| **Memory systems** | Context window (working memory), retrieved context (long-term memory), constitutional principles (procedural/guiding knowledge) |
| **Theoretical claim** | Alignment through constitutional principles creates a cognitively coherent reasoning agent without explicit rule-based control |
| **Scale (2026)** | Claude 4.x; millions of API interactions/day; constitutional principles evolved through iterated RLHF and red-teaming |
| **AMOS mapping** | J-space parallels AMOS's [[05_COGNITIVE_ORGANISM/GLOBAL_WORKSPACE_IMPLEMENTATION\|global workspace]] as a bounded shared state. Constitutional principles map to control-plane governance contracts. AMOS extends by adding formal verification ([[02_KERNEL/ABSOLUTE_LOGIC_KERNEL_19x19]]) and structural coherence tracking ([[11_KNOWLEDGE/RSCF_FORMAL_SPECIFICATION]]). |

**Strengths:** Massive scale; emergent cognitive coherence from training; constitutional framework enables principled behavior.

**Weaknesses:** No formal architectural specification; J-space is a heuristic construct, not a formal workspace; no explicit metacognition; reasoning is implicit (trained), not architecturally guaranteed.

### 2.2 LeCun's JEPA (Joint Embedding Predictive Architecture)

| Attribute | Detail |
|-----------|--------|
| **Proponent** | Yann LeCun (AMI Labs, ex-Meta FAIR) |
| **Core abstraction** | World Model as cognitive core — predicts latent state transitions in an abstract embedding space, not in pixel space |
| **Key mechanism** | Latent prediction — the architecture learns to predict future latent states given current state and action, avoiding the computational cost of pixel-level generation |
| **Memory systems** | World model (predictive model of environment dynamics), actor (policy), cost module (value assessment), short-term memory (latent state) |
| **Theoretical claim** | A single cognitive architecture with a world model, cost module, short-term memory, and action selection is sufficient for general intelligence; no language or LLM needed as a core component |
| **Scale (2026)** | V-JEPA 2 (2025); AMI Labs $1.03B seed (Mar 2026); Causal-JEPA; integrated with robotics (physical world grounding) |
| **AMOS mapping** | JEPA's world model maps to L10–L14 (World Modeling layers) of the [[05_COGNITIVE_ORGANISM/COGNITIVE_STACK_30_LAYER_SPECIFICATION\|30-layer stack]]. Latent prediction parallels active inference in AMOS's predictive processing pipeline. Cost module maps to L26 (Value Assessment). |

**Strengths:** Neuroscience-aligned; efficient latent prediction; scales with compute; embodied grounding via robotics.

**Weaknesses:** No explicit symbolic reasoning; limited natural language integration (by design); training requires massive world interaction data; no consciousness model.

### 2.3 Cognitive Architecture 2.0 (Chaturvedi et al. — 2023–2026)

| Attribute | Detail |
|-----------|--------|
| **Authors** | Shreya Chaturvedi et al. |
| **Core abstraction** | LLM-as-cognitive-core integration — classical CA modules (perception, memory, reasoning, action) orchestrated around an LLM backbone |
| **Key mechanism** | LLM as the central reasoning and language module, with classical CA components wrapping it: perception (multimodal encoders), memory (RAG + vector stores), action (tool use + planning) |
| **Theoretical claim** | LLMs provide the missing "language of thought" that classical CAs lacked; wrapping them in CA structure yields more coherent and capable agents |
| **Scale (2026)** | Primarily academic; influenced commercial agent frameworks; spawned variants (CogAgent, Cognitive Agent Framework) |
| **AMOS mapping** | AMOS is a **descendant** of this lineage. The 30-layer [[05_COGNITIVE_ORGANISM/COGNITIVE_STACK_30_LAYER_SPECIFICATION\|stack]] is the "CA 2.0 blueprint" taken to its logical extreme — LLMs are one component (L15–L17, Language Engine), not the core. The [[02_KERNEL/ABSOLUTE_LOGIC_KERNEL_19x19\|Absolute Logic Kernel]] provides what CA 2.0 lacks: deterministic reasoning substrate. |

**Strengths:** Practical integration of LLM capabilities; modular design enables component upgrades; addresses LLM limitations (hallucination, planning) via architectural structure.

**Weaknesses:** LLM as core creates single-point-of-failure; no formal verification; limited metacognition; no consciousness model.

### 2.4 AutoGPT / LangGraph as De Facto Agentic Cognitive Architectures

| Attribute | Status | Key Features |
|----------|--------|--------------|
| **AutoGPT** | Active (2023–2026) | Autonomous goal pursuit; recursive self-prompting; memory (vector store); tool use |
| **LangGraph** | Active (2023–2026) | State machine graph; conditional branching; human-in-the-loop; persistence |
| **CrewAI** | Active (2024–2026) | Multi-agent role specialization; task delegation; sequential/parallel execution |
| **OpenAI Swarm** | Active (2024–2026) | Lightweight agent handoff; routine/context switching; stateless design |

These frameworks are **de facto cognitive architectures** — they organize perception, reasoning, memory, and action into coherent computational loops — but they lack:
- Formal architectural specifications
- Principled memory consolidation
- Metacognitive monitoring
- Consciousness models
- Theoretical grounding in cognitive science

**AMOS mapping:** AMOS's agent framework (06_AGENTS) uses LangGraph-style state machines at the operational layer but wraps them in the full 30-layer [[05_COGNITIVE_ORGANISM/COGNITIVE_STACK_30_LAYER_SPECIFICATION|cognitive stack]] with RSCF epistemic grounding ([[11_KNOWLEDGE/RSCF_FORMAL_SPECIFICATION]]). The difference is architectural depth: de facto CAs are operational; AMOS is principled.

### 2.5 MAOS (Multi-Agent Operating Systems)

| Attribute | Detail |
|-----------|--------|
| **Core abstraction** | Distributed cognition — multiple agents, each with specialized cognitive functions, collectively producing emergent cognitive behavior |
| **Key mechanism** | Agent specialization + inter-agent communication protocols + shared state management |
| **Theoretical claim** | Complex cognition cannot be centralized; it requires distribution across specialized agents with well-defined interaction protocols |
| **Scale (2026)** | Multi-agent frameworks (CrewAI, AutoGen, MetaGPT) demonstrate distributed task decomposition; enterprise deployments in customer service, coding, research |
| **AMOS mapping** | MAOS maps directly to AMOS's multi-agent architecture: 9 control planes as specialized agents, 30-layer stack as shared cognitive substrate, RSCF as communication protocol grounding. AMOS extends by adding formal verification and authority chains (see [[03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT]]). |

---

## 3. Key Paradigms

Theoretical paradigms underpin architectural decisions. These are the dominant frameworks in 2026.

### 3.1 Global Workspace Theory (GWT)

| Attribute | Detail |
|-----------|--------|
| **Proponents** | Bernard Baars (1988), Stanislas Dehaene, Jean-Pierre Changeux |
| **Core claim** | Consciousness arises from a global broadcast mechanism — information that wins the competition for access to a global workspace becomes conscious and is broadcast to all specialized processors |
| **Mechanism** | Competitive selection → ignition (nonlinear amplification) → global broadcast → access consciousness |
| **Neural correlate** | Prefrontal-parietal network; gamma-band synchrony; ignition dynamics in EEG/fMRI |
| **Key papers** | Baars (1988) *A Cognitive Theory of Consciousness*; Dehaene & Naccache (2001); Mashour et al. (2020) |
| **AMOS mapping** | **Primary architectural paradigm.** AMOS's [[05_COGNITIVE_ORGANISM/GLOBAL_WORKSPACE_IMPLEMENTATION\|global workspace implementation]] is a direct engineering of GWT. The 9 control planes (C1–C9) function as specialized processors competing for workspace access. Ignition = threshold-triggered state transitions. Broadcast = cross-plane state propagation. |

### 3.2 Higher-Order Theories (HOT)

| Attribute | Detail |
|-----------|--------|
| **Proponents** | Hakwan Lau, David Rosenthal, Richard Brown |
| **Core claim** | Consciousness requires higher-order representations — a mental state is conscious only when there is a representation *of* that state (meta-representation) |
| **Variant** | Higher-Order Thought (HOT) — Rosenthal; Higher-Order Perception (HOP) — Lycan; Higher-Order Representation (HOR) — Lau |
| **Key distinction** | Metacognition as the mechanism of consciousness — awareness = modeling one's own cognitive states |
| **AMOS mapping** | AMOS's L22–L25 (metacognitive layers) implement higher-order monitoring. [[05_COGNITIVE_ORGANISM/GLOBAL_WORKSPACE_IMPLEMENTATION\|MIRROR]] functions as a self-modeling subsystem, analogous to Lau's prediction-error account of metacognition. |

### 3.3 Predictive Processing (PP)

| Attribute | Detail |
|-----------|--------|
| **Proponents** | Andy Clark, Karl Friston, Jakob Hohwy |
| **Core claim** | The brain is a prediction machine — it continuously generates predictions about incoming sensory input and updates its generative model based on prediction errors |
| **Mechanism** | Hierarchical prediction → error propagation → model update → active inference (acting to minimize prediction error) |
| **Formal framework** | Free Energy Principle (Friston) — systems minimize variational free energy (surprise); Bayesian brain hypothesis is a special case |
| **Key papers** | Clark (2013) *Whatever Next?*; Friston (2010) *The Free-Energy Principle*; Hohwy (2013) *The Predictive Mind* |
| **AMOS mapping** | Predictive processing maps to AMOS's L1–L5 (perception and prediction layers) in the [[05_COGNITIVE_ORGANISM/COGNITIVE_STACK_30_LAYER_SPECIFICATION\|30-layer stack]]. Active inference informs action selection at L28–L29. The free energy principle provides a theoretical constraint on all cognitive operations. |

### 3.4 Bayesian Brain Hypothesis

| Attribute | Detail |
|-----------|--------|
| **Proponents** | David Knill, Alexandre Pouget, Joshua Tenenbaum |
| **Core claim** | The brain performs approximate Bayesian inference — maintaining probability distributions over hypotheses and updating them given evidence |
| **Mechanism** | Prior × Likelihood → Posterior; approximate inference via sampling, variational methods, or message passing |
| **Key papers** | Knill & Pouget (2004); Körding & Wolpert (2004); Tenenbaum et al. (2011) |
| **Relationship to PP** | Bayesian brain is a computational-level description; predictive processing is a process-level implementation |
| **AMOS mapping** | Bayesian inference underlies RSCF ([[11_KNOWLEDGE/RSCF_FORMAL_SPECIFICATION]]) trust vector computation. The [[02_KERNEL/ABSOLUTE_LOGIC_KERNEL_19x19\|Absolute Logic Kernel]] provides deterministic complement to probabilistic Bayesian reasoning — hybrid symbolic-probabilistic architecture. |

### 3.5 Enactivism

| Attribute | Detail |
|-----------|--------|
| **Proponents** | Francisco Varela, Evan Thompson, Alva Noë |
| **Core claim** | Cognition is not representation of a pre-given world but enaction — it emerges from the dynamic coupling of organism and environment through sensorimotor interaction |
| **Key concept** | Sense-making — meaning arises from the organism's activity, not from passive representation |
| **Critique of classical CAs** | Classical CAs treat cognition as computation over internal representations; enactivism argues this misses the constitutive role of action and environment |
| **AMOS mapping** | Enactivism challenges AMOS's representational architecture at a fundamental level. However, AMOS partially addresses this through: (a) embodied action layers (L28–L29), (b) environment-coupled control planes, (c) RSCF as a relational (not purely representational) knowledge framework. |

---

## 4. Consciousness Models

The relationship between consciousness and cognitive architecture is contested. These models represent the leading theoretical positions.

### 4.1 Integrated Information Theory (IIT)

| Attribute | Detail |
|-----------|--------|
| **Proponent** | Giulio Tononi (University of Wisconsin–Madison) |
| **Core claim** | Consciousness is identical to integrated information (Φ) — the amount of information generated by a system above and beyond its parts |
| **Key concepts** | Cause-effect structure (CES), Φ (phi) as the measure of integrated information, exclusion postulate, composition postulate |
| **2025–2026 updates** | IIT 5.0 refinements; ongoing debate about Φ computability (NP-hard); ASPEN (Algorithmic System for Perceiving Emergent Normality) framework as practical approximation; disputes with Global Neuronal Workspace over neural correlates |
| **Criticisms** | Φ is computationally intractable for large systems; panpsychism implication (any system with Φ > 0 has some consciousness); limited empirical testability |
| **AMOS mapping** | RSCF ([[11_KNOWLEDGE/RSCF_FORMAL_SPECIFICATION]]) structural coherence is a **functional analog** of Φ — it measures the degree to which knowledge elements form an integrated, non-decomposable structure. AMOS does not claim Φ or consciousness; RSCF tracks integration as an engineering metric, not a metaphysical claim. Hard boundary: `RSCF_COHERENCE != PHI != CONSCIOUSNESS`. |

### 4.2 Global Neuronal Workspace (GNW)

| Attribute | Detail |
|-----------|--------|
| **Proponents** | Stanislas Dehaene, Jean-Pierre Changeux, George Mashour |
| **Core claim** | Consciousness = global availability of information via a fronto-parietal neuronal workspace; unconscious processing is local and modular; consciousness is global and broadcast |
| **Key mechanism** | Ignition — a nonlinear phase transition when local processing wins competition for workspace access; all-or-nothing dynamics |
| **Neural evidence** | P3b ERP component as ignition marker; prefrontal-parietal gamma synchrony; anesthesia studies showing workspace collapse |
| **2025–2026 updates** | Mashour & Bhatt (2025) GNW vs. IIT debate; updated ignition dynamics models; workspace as computational architecture validated by prefrontal lesion studies |
| **AMOS mapping** | Directly informs [[05_COGNITIVE_ORGANISM/GLOBAL_WORKSPACE_IMPLEMENTATION\|AMOS's global workspace implementation]]. The 9 control planes as workspace modules; ignition = threshold-triggered state transitions; broadcast = cross-plane state propagation. AMOS's workspace is engineered, not biological, but the architectural pattern is deliberately aligned. |

### 4.3 Orchestrated Objective Reduction (Orch-OR)

| Attribute | Detail |
|-----------|--------|
| **Proponents** | Roger Penrose, Stuart Hameroff |
| **Core claim** | Consciousness arises from quantum computations in microtubules — objective reduction (OR) of quantum superpositions produces moments of conscious experience |
| **Key mechanism** | Quantum coherence in microtubules → orchestrated collapse (objective reduction) → discrete conscious moments |
| **Status (2026)** | Highly controversial; some experimental support for quantum effects in microtubules (Fisher 2025); majority of neuroscience community remains skeptical; no engineering applications |
| **AMOS mapping** | No direct AMOS alignment. AMOS's [[02_KERNEL/ABSOLUTE_LOGIC_KERNEL_19x19\|Absolute Logic Kernel]] operates on classical (deterministic) logic. Quantum coherence as consciousness mechanism is outside AMOS's current architectural scope. However, AMOS's quantum computing modules (see [[22_RESEARCH/SOTA_QUANTUM_COMPUTING_2026]]) may eventually interface with Orch-OR insights if quantum biological effects prove engineerable. |

### 4.4 Attention Schema Theory (AST)

| Attribute | Detail |
|-----------|--------|
| **Proponent** | Michael Graziano (Princeton) |
| **Core claim** | Awareness is the brain's simplified model of its own attention — the brain constructs an "attention schema" that it uses to monitor and control attention, and this schema is what we experience as consciousness |
| **Key mechanism** | Self-modeling — the brain builds a representation of its own attentional process (the attention schema), and this representation is the content of conscious awareness |
| **Key papers** | Graziano (2013) *Consciousness and the Social Brain*; Gastaut (1950s) historical precedent; Chambon et al. (2024) meta-analysis |
| **AMOS mapping** | **Direct AMOS alignment.** MIRROR (Self-Modeling Engine) in the [[05_COGNITIVE_ORGANISM/GLOBAL_WORKSPACE_IMPLEMENTATION\|global workspace implementation]] functions as an attention schema — it models AMOS's own attentional state across control planes. The parallel is deliberate: Graziano's AST provides the theoretical justification for MIRROR's architectural role. |

### 4.5 Higher-Order Workspace Theory (HOWT)

| Attribute | Detail |
|-----------|--------|
| **Proponents** | Hakwan Lau, Christof Koch, Colin Klein |
| **Core claim** | Synthesis of Global Workspace Theory and Higher-Order Theories — consciousness requires both global broadcast (GWT) and higher-order monitoring (HOT) of that broadcast |
| **Key mechanism** | Prefrontal cortex generates higher-order representations of workspace contents; consciousness = workspace content + prefrontal monitoring of that content |
| **AMOS mapping** | HOWT's dual requirement (broadcast + monitoring) is reflected in AMOS's [[05_COGNITIVE_ORGANISM/GLOBAL_WORKSPACE_IMPLEMENTATION\|global workspace implementation]]: (a) broadcast across control planes = GWT component, (b) MIRROR + L22–L25 metacognitive layers = HOT component. AMOS's architecture is arguably closer to HOWT than to pure GWT or pure HOT. |

---

## 5. AMOS Positioning

### 5.1 Architectural Mapping Summary

| AMOS Component | CA Parallel | Theoretical Grounding |
|----------------|-------------|----------------------|
| **30-layer cognitive stack** (L0–L29) | Full cognitive architecture (all CAs) | Architectural hierarchy as universal cognitive function decomposition |
| **9 control planes** (C1–C9) | Global workspace (LIDA, GWT) | Baars/Dehaene global broadcast; operational workspace architecture |
| **MIRROR** (Self-Modeling) | Attention Schema Theory (Graziano) | Awareness as self-model of attentional process |
| **RSCF** (Structural Coherence) | Integrated Information Theory (Tononi) | Structural coherence as functional analog of Φ (engineering metric, not metaphysical claim) |
| **Absolute Logic Kernel** (ALAK 19×19) | Deterministic reasoning substrate | Complement to probabilistic approaches (Bayesian brain, PP); formal verification |
| **Language Engine** (L15–L17) | CA 2.0 LLM backbone | LLM as cognitive language module, not core architecture |
| **World Model** (L10–L14) | JEPA (LeCun) | Latent prediction of environment dynamics |
| **Metacognitive Layers** (L22–L25) | Higher-Order Theories (Lau, Rosenthal) | Meta-representations of cognitive states |

### 5.2 What AMOS Adds Beyond Classical CAs

| Dimension | Classical CA | AMOS |
|-----------|-------------|------|
| **Formal verification** | Ad hoc or absent | [[02_KERNEL/ABSOLUTE_LOGIC_KERNEL_19x19\|ALAK 19×19]] provides deterministic substrate |
| **Epistemic grounding** | Implicit (if any) | [[11_KNOWLEDGE/RSCF_FORMAL_SPECIFICATION\|RSCF]] — SOURCE_CLAIM, OBSERVATION, DERIVED, MODEL, DECISION, COMPETING, UNKNOWN/GAP |
| **Layer depth** | 8–15 modules | 30 layers with typed interfaces |
| **Control planes** | 1–3 (if any) | 9 planes with formal governance |
| **Self-modeling** | Limited or absent | MIRROR as architectural primitive |
| **Scalability design** | Academic prototype | Enterprise-grade with authority chains |

### 5.3 Hard Boundaries

```text
AMOS != GENERAL_INTELLIGENCE
ARCHITECTURE != CONSCIOUSNESS
DOCUMENTATION != IMPLEMENTATION
RSCF_COHERENCE != PHI
MIRROR != AWARENESS
ALAK_19x19 != WHOLE_REASONING
```

---

## 6. Gap Analysis

### 6.1 Field-Wide Gaps (All Cognitive Architectures)

| Gap | Severity | AMOS Status | Notes |
|-----|----------|-------------|-------|
| **Formal verification** | Critical | Partially addressed (ALAK) | No CA has been formally verified end-to-end; AMOS has formal kernel but full stack verification is ongoing |
| **Human-level general intelligence** | Critical | Not claimed | No architecture achieves human-level GI; AMOS explicitly does not claim this |
| **Memory consolidation at scale** | High | Partially addressed (Memory Engine) | No CA scales memory consolidation to human lifetime equivalents; AMOS has architecture but unvalidated at scale |
| **Metacognitive monitoring** | High | Partially addressed (MIRROR, L22–L25) | Limited empirical validation of metacognitive architectures; AMOS MIRROR is theoretical |
| **Emotional/somatic integration** | High | Gap | Affect and embodiment largely absent from computational CAs; AMOS has no explicit emotion/soma module |
| **Social cognition** | Medium | Gap | Theory of mind, social reasoning minimal in CAs; AMOS multi-agent exists but social cognition is absent |
| **Developmental trajectories** | Medium | Gap | No CA models cognitive development (infancy → adulthood); all assume fully formed architecture |
| **Consciousness integration** | Unknown | Gap | No CA claims or measures consciousness integration; AMOS does not claim consciousness |

### 6.2 Specific Architectural Gaps

| Architecture | Primary Gap | Impact |
|-------------|-------------|--------|
| **Soar** | No native perceptual grounding; limited real-world deployment | Problem spaces are abstract; embodiment remains unaddressed |
| **ACT-R** | Symbolic bottleneck; no flexible attention mechanism | Production systems limit sub-symbolic flexibility |
| **LIDA** | Limited learning; no formal reasoning substrate | Cognitive cycle is elegant but narrow in capability |
| **CA 2.0** | LLM as core creates fragility; no verification | Architectural dependency on stochastic core |
| **JEPA** | No language integration; no metacognition (by design) | Powerful but incomplete as cognitive architecture |
| **AutoGPT/LangGraph** | No theoretical grounding; no formal memory consolidation | De facto CAs are operational, not principled |

---

## 7. Future Directions

### 7.1 Near-Term (2026–2028)

| Direction | Key Actors | AMOS Implications |
|-----------|-----------|-------------------|
| **LLM-augmented classical CAs** | Anthropic, Google DeepMind, CMU ACT-R group | AMOS Language Engine (L15–L17) already positions LLMs as modules, not cores |
| **Neurosymbolic cognitive architectures** | MIT CSRL, Stanford HAI, AMI Labs | ALAK + LLM hybrid aligns with AMOS's dual symbolic-probabilistic design |
| **World model integration** | AMI Labs (JEPA), World Labs, NVIDIA Cosmos | AMOS World Model layers (L10–L14) can absorb JEPA-family advances |
| **Consciousness measurement benchmarks** | Templeton Foundation, Allen Institute | Potential validation pathway for MIRROR and RSCF coherence metrics |

### 7.2 Medium-Term (2028–2032)

| Direction | Description | AMOS Positioning |
|-----------|-------------|-----------------|
| **Developmental cognitive architectures** | CAs that model cognitive growth from simple to complex | AMOS's layer architecture could support developmental bootstrapping (L0→L29 incrementally) |
| **Multi-agent cognitive systems** | Distributed cognition across agent collectives with shared workspaces | AMOS's 9 control planes + multi-agent framework already architecturally aligned |
| **Formally verified CAs** | End-to-end formal verification of cognitive architectures | ALAK provides foundation; full verification would require extending to all 30 layers |
| **Emotional/somatic architectures** | Integration of affect, interoception, and embodiment | Open gap; would require new layers or layer extensions in the [[05_COGNITIVE_ORGANISM/COGNITIVE_STACK_30_LAYER_SPECIFICATION\|30-layer stack]] |

### 7.3 Long-Term (2032+)

| Direction | Description |
|-----------|-------------|
| **Embodied cognitive architectures** | Full sensorimotor integration with physical or simulated embodiment |
| **Social cognitive architectures** | Theory of mind, cultural cognition, collective intelligence as first-class architectural components |
| **Consciousness-integrated architectures** | If consciousness models converge (IIT, GWT, AST), architectures may incorporate consciousness-adjacent mechanisms |
| **Universal cognitive architecture** | A single architecture spanning all cognitive functions — the original Soar/Newell vision, realized at 2026 scale |

---

## 8. Key References

| Ref | Citation | Relevance |
|-----|----------|-----------|
| [1] | Laird, Newell, Rosenbloom (1987). "Soar: An Architecture for General Intelligence." *Artificial Intelligence*, 33(1), 1–64. | Classical CA foundation |
| [2] | Anderson, J.R. (2007). *How Can the Human Mind Occur in the Physical Universe?* Oxford University Press. | ACT-R theoretical foundation |
| [3] | Franklin, S. (2007). "A Foundational Architecture for Artificial General Intelligence." *Advances in Artificial General Intelligence*, 36–54. | LIDA / GWT implementation |
| [4] | Ahmad, S., Hawkins, J. (2021). "Properties of Sparse Distributed Representations and their Application to Hierarchical Temporal Memory." *arXiv:1503.07469*. | SPA / HTM |
| [5] | Sun, R. (2006). "The CLARION Cognitive Architecture: Extending Cognitive Modeling to Social Simulation." *Cognition and Multi-Agent Interaction*, 79–120. | Implicit/explicit duality |
| [6] | Baars, B.J. (1988). *A Cognitive Theory of Consciousness.* Cambridge University Press. | GWT foundation |
| [7] | Dehaene, S., Naccache, L. (2001). "Towards a Cognitive Neuroscience of Consciousness." *Cognition*, 79, 1–37. | GNW |
| [8] | Tononi, G. (2004). "An Information Integration Theory of Consciousness." *BMC Neuroscience*, 5(42). | IIT foundation |
| [9] | Graziano, M. (2013). *Consciousness and the Social Brain.* Oxford University Press. | AST |
| [10] | Clark, A. (2013). "Whatever Next? Predictive Brains, Situated Agents, and the Future of Cognitive Science." *Behavioral and Brain Sciences*, 36(3), 181–204. | Predictive Processing |
| [11] | Friston, K. (2010). "The Free-Energy Principle: A Unified Brain Theory?" *Nature Reviews Neuroscience*, 11(2), 127–138. | Free Energy Principle |
| [12] | LeCun, Y. (2022). "A Path Towards Autonomous Machine Intelligence." *OpenReview*. | JEPA |
| [13] | Chaturvedi, S. et al. (2023). "Cognitive Architectures for General AI." *arXiv:2309.15324*. | CA 2.0 |
| [14] | Mashour, G.A. et al. (2020). "Consciousness and the Prefrontal Parietal Network." *Anesthesiology*, 132(2), 248–258. | GNW updates |
| [15] | Lau, H. (2019). *Being You: A New Science of Consciousness.* Dutton. | HOT / metacognition |

---

> [!AMOS INTEGRATION] Cross-Reference Index
> - [[05_COGNITIVE_ORGANISM/COGNITIVE_STACK_30_LAYER_SPECIFICATION]] — 30-layer stack specification (L0–L29)
> - [[05_COGNITIVE_ORGANISM/GLOBAL_WORKSPACE_IMPLEMENTATION]] — GWT implementation, MIRROR, control plane broadcast
> - [[02_KERNEL/ABSOLUTE_LOGIC_KERNEL_19x19]] — ALAK 19×19 deterministic reasoning substrate
> - [[11_KNOWLEDGE/RSCF_FORMAL_SPECIFICATION]] — RSCF structural coherence framework
> - [[03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT]] — Control plane governance
> - [[22_RESEARCH/SOTA_QUANTUM_COMPUTING_2026]] — Quantum computing research (Orch-OR interface)
> - [[22_RESEARCH/SOTA_WORLD_MODELS_GENERATIVE_SIMULATION_2026]] — World models (JEPA lineage)
> - [[22_RESEARCH/SOTA_AGENTIC_AI_MULTI_AGENT_SYSTEMS_2026]] — Multi-agent systems (MAOS lineage)

---

> **Lineage:** This brief is classified as `OBSERVATION` / `DERIVED` under the AMOS RSCF framework. All claims about AMOS architectural parallels are structural mappings, not claims of implementation equivalence or validation. Promotions to `AMOS_MODEL` or `CANONICAL_ALIGNED` require governed review per [[03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT]].
