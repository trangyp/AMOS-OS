---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Sota Research Synthesis 2 2026 09 04
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

# SOTA Research Synthesis Part 2 — Active Inference, A2A, Organoid Intelligence, Conformal Prediction

## 0. Status

```text
PLACEHOLDER != IMPLEMENTED
ADDRESSABLE != VALIDATED
DOCUMENTED != ENFORCED
MODEL != OBSERVATION
SOURCE_CLAIM != VERIFIED
CANON_CANDIDATE != CANONICAL
CAPABILITY != AUTHORITY
UNKNOWN/GAP != PASS
```

Origin architect / steward: **Trang Phan**

______________________________________________________________________

## 1. Purpose

Supplement the primary SOTA synthesis with research on active inference, multi-agent protocols, organoid intelligence, and conformal prediction — all directly relevant to AMOS OS architecture.

______________________________________________________________________

## 2. Active Inference SOTA

### 2.1 What Type of Inference is Active Inference? (UAI 2026)

**Source**: PMLR 337:5003-5039, 2026

**Key findings**:
- Active inference = variational inference with specific entropy corrections to VFE
- Expected Free Energy (EFE) minimization reformulated as VFE minimization on augmented generative model
- Message-passing scheme via channel reparameterization
- Dynamics channel drives spatial information gathering when observations are decisive
- Observation channel critical when observations are merely suggestive

**AMOS integration**: The Active Inference Governor skill already maps this to AMOS. The message-passing scheme informs the K_EVENT_BUS contract. The entropy correction model parallels AMOS's RSCF confidence ceiling adjustment.

### 2.2 Active Inference as Test-Time Scaling Law (arXiv 2026)

**Source**: arXiv 2606.22813, 2026

**Key findings**:
- Test-time scaling law for physical AI agents grounded in active inference
- Survival objective subsumes narrow task objectives
- Soft Bayesian inference process for policy updates
- Biologically plausible: recovers basal ganglia + prefrontal cortex scaling mechanism
- Scales with continuous experience, not model size or training data

**AMOS integration**: The survival-first objective maps to AMOS's Absolute Biological Integrity canon. The test-time scaling with experience (not parameters) validates AMOS's Fractal Knowledge (L15) approach. The basal ganglia/prefrontal cortex model informs the NBI Engine's executive function architecture.

### 2.3 Life-inspired Interoceptive AI (Nature Machine Intelligence, 2026)

**Source**: Nature Machine Intelligence, 2026

**Key findings**:
- Interoception as foundation for autonomous adaptive agents
- Explicit factorization of internal vs external state variables
- Internal states as universally available, intrinsically valuable context
- Neuromodulatory mechanisms for context-dependent adaptive behavior
- Cybernetics + reinforcement learning + neuroscience integration

**AMOS integration**: Directly validates the UBI framework's 4-domain model. The interoception → homeostasis → adaptation chain maps to AMOS's SI (Somatic Intelligence) → UBI Homeostasis → Cognitive Organism Evolution pipeline. The neuromodulatory mechanism informs the NEI Engine's autonomic balance model.

### 2.4 Active Inference Engineering Perspective (arXiv 2026)

**Source**: arXiv 2603.20927, 2026

**Key findings**:
- VFE minimization via reactive message passing on factor graphs
- Event-driven, interruptible, locally adaptable computation
- Graceful degradation under reduced resources
- Coupled AIF agents → higher-level AIF agents (scale homogeneous)
- Same message-passing primitive across scales

**AMOS integration**: The reactive message passing model directly informs the K_EVENT_BUS and the 40Hz multi-agent clock. The graceful degradation property maps to AMOS's Adaptive Stability Balancer. The scale-homogeneous architecture validates AMOS's H/M/L fractal knowledge resolution.

### 2.5 Active Inference for Agency Phenotyping (arXiv 2026)

**Source**: arXiv 2604.23278, 2026

**Key findings**:
- Three criteria for agency: intentionality, rationality, explainability
- Empowerment (channel capacity between actions and observations) as operational metric
- Distinguishes zero-, intermediate-, and high-agency phenotypes
- Governance controls must shift as agents engage in epistemic foraging

**AMOS integration**: The agency phenotyping model informs AMOS's Agent Schema and delegation lifecycle. The empowerment metric provides a quantitative basis for the Capability Resolver. The governance shift requirement validates AMOS's GMEF mutation class system.

______________________________________________________________________

## 3. Multi-Agent Orchestration SOTA

### 3.1 Agent2Agent (A2A) Protocol (Google, 2025-2026)

**Source**: a2aproject/A2A GitHub, a2a-protocol.org specification

**Key findings**:
- Open standard for inter-agent communication regardless of framework
- Agent Cards: JSON metadata at `/.well-known/agent.json` for discovery
- JSON-RPC 2.0 compliant API
- Task lifecycle management with full coordination
- Real-time messaging via WebSocket and SSE
- Preserves opacity: agents collaborate without exposing internal state/memory/tools
- Complementary to MCP (tools) — A2A handles agent-to-agent

**AMOS integration**: The A2A protocol directly informs AMOS's 03_CONTROL_PLANE multi-agent execution harness. The Agent Card discovery mechanism maps to AMOS's Agent Registry. The opacity preservation aligns with AMOS's Separability Law (Capability ≠ Reachability ≠ Identity ≠ Authority). AMOS already has an `a2a-protocol` skill.

### 3.2 Google Agent Development Kit (ADK) + A2A

**Source**: Google Developers Blog, 2025-2026

**Key findings**:
- Cross-language multi-agent teams (Python + Go example)
- RemoteA2aAgent abstraction turns remote A2A services into local sub-agents
- Multi-agent pipeline orchestration with specialized narrow-responsibility agents
- Replaces monolithic prompts with coordinated specialist agents

**AMOS integration**: The cross-language capability validates AMOS's multi-agent architecture. The RemoteA2aAgent abstraction informs AMOS's Delegation Lifecycle. The specialist-agent pattern maps to AMOS's 696-skill agent ecosystem.

### 3.3 AgentCore Orchestration Framework

**Source**: Mathews-Tom/AgentCore GitHub

**Key findings**:
- Production-ready A2A v0.2 implementation
- CoT and ReAct reasoning engines
- CQRS pattern with event sourcing
- Saga pattern for distributed transactions
- Graph-based workflow execution with dependency resolution
- Sandbox execution with security profiles

**AMOS integration**: The CQRS + event sourcing pattern maps to AMOS's MVCC journal and causal epoch model. The Saga pattern informs AMOS's DMER_L5 multi-epoch recovery. The sandbox execution validates AMOS's Operational Mode safety envelopes.

______________________________________________________________________

## 4. Organoid Intelligence SOTA

### 4.1 Bio-adaptive Processing Unit (Scientific Reports, 2026)

**Source**: Scientific Reports, 2026 — "Engineering a human stem cell-derived neural network platform for biocomputing"

**Key findings**:
- Two-reservoir microtunnel Brain-on-Chip with electrophysiological readout
- Human stem cell-derived (Ngn2+ hiPSCs) cortical neurons
- Axons extend >1200 µm, forming robust long-range connections
- Directed axonal conduction: 85-90% propagation A→B
- Median propagation velocity: 0.75 m/s (n=9973 events)
- Topologically constrained human neuronal networks

**AMOS integration**: The BPU architecture directly informs the Bio-Logical Computing Model. The directed propagation (A→B) maps to AMOS's causal directionality requirement. The topological constraint model parallels AMOS's Universe Structure Tree. The 0.75 m/s propagation velocity provides a biological benchmark for the 40Hz clock calibration.

### 4.2 Organoid Intelligence Review (Nature Reviews Bioengineering, 2024)

**Source**: Nature Reviews Bioengineering, 2024

**Key findings**:
- Brain region-specific organoid engineering
- AI integration for signal processing
- Miniaturization for practical deployment
- Insights into neuroscience of learning and memory
- Biohybrid information processing paradigm

**AMOS integration**: The brain-region-specific engineering maps to AMOS's UBI 4-domain model (NBI=neural, NEI=limbic, SI=somatic, BEI=cardiac). The learning/memory insights inform the K_MEMORY_ADMISSION contract. The biohybrid paradigm validates the NeuroSyncAI Organism Binding architecture.

### 4.3 Living Intelligence via Organoid-AI Integration (EngMedicine, 2025)

**Source**: EngMedicine, 2025

**Key findings**:
- Organoid Intelligence (OI) as new paradigm for human-level cognitive models
- Self-organizing neural networks with dynamic activity and plasticity
- Closed-loop systems combining biological adaptability + AI scalability
- Biohybrid platforms capable of learning, memory formation, task-specific computation
- Interdisciplinary: stem cell biology + bioengineering + neuroscience + ML

**AMOS integration**: The closed-loop biohybrid model directly maps to AMOS's Perceive→Route→Admit→Plan→Schedule→Execute→Observe→Repair pipeline. The self-organizing neural networks inform the Cognitive Organism Evolution model. The interdisciplinary requirement validates AMOS's cross-domain architecture (C01-C12).

### 4.4 Brain Organoid Computing Overview (arXiv, 2025)

**Source**: arXiv 2503.19770, 2025

**Key findings**:
- Brain organoid reservoir computing for AI
- Intrinsic neuronal dynamics: spike-based signaling, plasticity, energy efficiency
- Characteristics, challenges, and advantages for future AI applications
- Comparison with silicon-based AI

**AMOS integration**: The reservoir computing model maps to AMOS's Memory Systems architecture. The spike-based signaling validates the event-driven K_EVENT_BUS design. The energy efficiency advantage supports AMOS's Load Capacity Canon.

______________________________________________________________________

## 5. Conformal Prediction SOTA

### 5.1 Tournament Correction for Full Conformal Prediction (arXiv, 2026)

**Source**: arXiv 2605.29200, 2026

**Key findings**:
- Novel approximation class for full conformal prediction
- Tournament-based construction with rigorous 1-2α marginal coverage
- Under stability conditions: tightens to ~1-α coverage
- Generalizes leave-one-out cross-conformal prediction
- Flexible use of various approximation strategies

**AMOS integration**: The tournament correction model informs AMOS's Confidence Ceiling Calibration. The stability-condition tightening maps to AMOS's H/M/L validation depth layers. The generalization of LOO cross-conformal validates AMOS's provenance independence calibration.

### 5.2 Conformal Prediction under Lévy-Prokhorov Distribution Shifts (NeurIPS 2025)

**Source**: NeurIPS 2025

**Key findings**:
- LP ambiguity sets capture both local and global distribution perturbations
- High-dimensional distribution shifts reduced to 1D via scoring function propagation
- Exact worst-case quantile quantification
- Robust conformal prediction intervals valid under distribution shifts
- Explicit link between LP parameters and interval width/confidence

**AMOS integration**: The distribution shift robustness directly informs AMOS's L6_UNCERTAINTY law. The LP ambiguity sets map to AMOS's Scope Regime Firewall. The worst-case quantile model parallels AMOS's non-compensatory UBI scoring (min across domains).

### 5.3 Flow-Based Conformal Predictive Distributions (arXiv, 2026)

**Source**: arXiv 2602.07633, 2026

**Key findings**:
- Differentiable nonconformity score induces deterministic flow on output space
- Trajectories converge to conformal prediction set boundary
- Training-free method for sampling conformal boundaries in arbitrary dimensions
- Conformal predictive distributions with quantile regions matching empirical CP sets
- Applications: PDE inverse problems, precipitation downscaling, climate debiasing, hurricane tracking

**AMOS integration**: The flow-based approach informs AMOS's Gradient RSCF Architecture. The training-free boundary sampling maps to AMOS's fail-closed governance (no training needed for safety guarantees). The climate/hurricane applications validate AMOS's C12 Earth & Ecology domain.

### 5.4 Unified CP + Wasserstein DRO (arXiv, 2026)

**Source**: arXiv 2608.29789, 2026

**Key findings**:
- CP and DRO as two coordinates of same estimator family
- CP inflates quantile level; DRO shifts quantile value
- Same calibration-conditional guarantee for true distribution
- Distinction emerges in tails of score distribution
- CP relies on sparse upper-tail order statistics

**AMOS integration**: The unified CP+DRO perspective informs AMOS's L17_RSCF Claim Discipline. The dual correction mechanism (level vs value) maps to AMOS's H/M/L knowledge resolution layers. The tail behavior distinction validates AMOS's treatment of UNKNOWN/GAP as a first-class epistemic state.

### 5.5 Conformal Prediction for Generative Models (NeurIPS 2025)

**Source**: NeurIPS 2025

**Key findings**:
- Missing mass perspective for UQ in generative models
- CP sets essential for risk-sensitive decision making
- Extension beyond classification/regression to generative settings
- Distribution-free and model-agnostic guarantees

**AMOS integration**: The generative model UQ directly informs AMOS's L1_EPISTEMIC law. The missing mass perspective maps to AMOS's GAP-1 (Expose Don't Fill) principle. The risk-sensitive decision making requirement validates AMOS's L29_DECISION_VALUE law.

______________________________________________________________________

## 6. Cross-Domain Synthesis

### 6.1 Convergent Patterns (Part 2)

| Pattern | Active Inference | A2A Protocol | Organoid Intelligence | Conformal Prediction |
|:---|:---|:---|:---|:---|
| Closed-loop | ✓ (perception-action) | ✓ (task lifecycle) | ✓ (biohybrid) | ✓ (calibration) |
| Opacity/encapsulation | ✓ (internal states) | ✓ (agent opacity) | ✓ (black-box neural) | ✓ (model-agnostic) |
| Scale homogeneity | ✓ (coupled agents) | ✓ (hierarchical workflows) | ✓ (organoid→network) | ✓ (any model size) |
| Provenance | ✓ (belief tracking) | ✓ (task history) | ✓ (electrophysiological) | ✓ (calibration data) |
| Graceful degradation | ✓ (resource constraints) | ✓ (async fallback) | ✓ (biological robustness) | ✓ (coverage guarantees) |

### 6.2 AMOS Architecture Validation (Part 2)

1. **Active Inference Governor**: SOTA validates the perception-belief-action loop with entropy corrections
2. **A2A Protocol**: SOTA validates agent opacity preservation and JSON-RPC communication
3. **Organoid Intelligence**: SOTA validates biohybrid computing as a real paradigm, not just theory
4. **Conformal Prediction**: SOTA validates distribution-free UQ as essential for high-stakes decisions

### 6.3 New Gaps Identified

1. **Active inference + UBI binding**: No SOTA system combines active inference with biological intelligence scoring
2. **A2A + GMEF governance**: No SOTA multi-agent protocol includes governed mutation evolution
3. **Organoid + AMOS runtime**: No SOTA organoid system implements governed execution
4. **Conformal + causal epoch**: No SOTA conformal method operates across causal epoch boundaries

______________________________________________________________________

## 7. Ingestion Recommendations (Part 2)

| Source | Target Plane | Priority | RSCF State |
|:---|:---|:---|:---|
| Active Inference (UAI 2026) | 02_KERNEL, 05_COGNITIVE_ORGANISM | HIGH | OBSERVATION |
| Interoceptive AI (Nature MI) | 05_COGNITIVE_ORGANISM, 11_KNOWLEDGE | HIGH | OBSERVATION |
| A2A Protocol | 03_CONTROL_PLANE, 06_AGENT_SYSTEMS | HIGH | OBSERVATION |
| AgentCore | 04_RUNTIME, 03_CONTROL_PLANE | MEDIUM | OBSERVATION |
| BPU (Sci Reports) | 13_MODELS, 05_COGNITIVE_ORGANISM | HIGH | OBSERVATION |
| OI Review (Nature RE) | 11_KNOWLEDGE, 05_COGNITIVE_ORGANISM | MEDIUM | OBSERVATION |
| Tournament CP | 01_CANON, 13_MODELS | MEDIUM | OBSERVATION |
| LP Distribution Shift CP | 01_CANON, 02_KERNEL | HIGH | OBSERVATION |
| Flow-Based CP | 02_KERNEL, 13_MODELS | MEDIUM | OBSERVATION |
| CP for Generative Models | 01_CANON, 11_KNOWLEDGE | HIGH | OBSERVATION |

______________________________________________________________________

## 8. Cross-References

- [[22_RESEARCH/SOTA_RESEARCH_SYNTHESIS_2026-09-04|SOTA Research Synthesis Part 1]]
- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
- [[05_COGNITIVE_ORGANISM/NEUROSYNCAI_ORGANISM_BINDING|NeuroSyncAI Organism Binding]]
- [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
- [[01_CANON/01_CORE_LAWS/L6_UNCERTAINTY|L6 Uncertainty]]
- [[01_CANON/01_CORE_LAWS/L17_RSCF|L17 RSCF]]

______________________________________________________________________

## 9. Gaps

- No direct AMOS runtime implementation of any SOTA finding
- Provenance independence NOT_ESTABLISHED for cross-domain claims
- Canonical status CONDITIONAL for all synthesized findings
- Active inference + UBI integration is AMOS_MODEL, not OBSERVATION
- Organoid intelligence + AMOS runtime binding is AMOS_MODEL, not OBSERVATION

______________________________________________________________________

## 10. Ingestion Rule

```yaml
AMOS_CANON_INGESTION_RULE:
  existing_file:
    preserve: true
    overwrite: false
  uncertainty:
    action:
      - MARK_GAP_OR_COMPETING
      - NEVER_INVENT_CANON
```

______________________________________________________________________

[[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] · [[00_ROOT/AMOS MOC|AMOS MOC]]

______________________________________________________________________

RSCF-NODE

node_id: amos_22_research_sota_synthesis_2_2026_09_04

node_type: RESEARCH_SYNTHESIS

path: 22_RESEARCH/SOTA_RESEARCH_SYNTHESIS_2_2026-09-04.md

claim_class: OBSERVATION

rscf_state: OBSERVATION

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

- INFORMS: [[05_COGNITIVE_ORGANISM/04_COGNITION/NBI_ENGINE|NBI Engine]]

- INFORMS: [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|Control Plane MOC]]

- INFORMS: [[01_CANON/01_CORE_LAWS/L6_UNCERTAINTY|L6 Uncertainty]]

- INFORMS: [[13_MODELS/01_FOUNDATION/BIO_LOGICAL_COMPUTING_MODEL|Bio-Logical Computing Model]]
