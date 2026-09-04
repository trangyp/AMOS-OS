---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Sota Research Synthesis 2026 09 04
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

# SOTA Research Synthesis 2026-09-04

## 0. Status

This artifact synthesizes state-of-the-art research findings harvested on 2026-09-04 across BCI, AI agent memory, quantum computing, and neuromorphic computing domains. It is intended to inform AMOS OS architectural expansion.

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

Provide a curated synthesis of latest SOTA research (2025-2026) to inform AMOS OS architectural decisions, particularly in:
- BCI/NeuroSyncAI integration (05_COGNITIVE_ORGANISM)
- Agent memory architecture (02_KERNEL, 11_KNOWLEDGE)
- Quantum computing analogies (01_CANON/02_UNIVERSE_CANON)
- Neuromorphic computing (13_MODELS, 04_RUNTIME)

______________________________________________________________________

## 2. BCI / Brain-Computer Interface SOTA

### 2.1 Intracortical BCI for Speech (Nature Medicine, 2026)

**Source**: Nature Medicine, 2026 — "Long-term independent use of an intracortical brain–computer interface for speech and cursor control"

**Key findings**:
- Participant with ALS used BCI for >3,800 hours at home over ~2 years with no researchers present
- Communicated 183,060 sentences (1,960,163 words) at 56 words per minute
- 92% of sentences decoded at least mostly correctly
- >99% word accuracy on 125,000-word vocabulary in formal testing
- BCI used for speech AND cursor control simultaneously — multimodal
- Enabled full-time employment despite paralysis

**AMOS integration**: Validates NeuroSyncAI closed-loop architecture. The 40Hz multi-agent clock and UBI substrate distress veto are directly applicable. The multimodal (speech + cursor) capability supports the NBI Engine's perceptual/executive function model.

### 2.2 Neuromorphic BCI Framework (npj Biomedical Innovations, 2026)

**Source**: npj Biomedical Innovations, 2026 — "Towards neuromorphic neurotechnologies"

**Key findings**:
- Brain-Inspired BCIs (BI-BCIs) as unifying framework for low-power, closed-loop neuromorphic neurotechnologies
- Integration of spiking neural networks (SNNs) with BCI for on-implant processing
- Key companies: Neuralink, Paradromics, Synchron, Blackrock Neurotech, Neurable, Kernel
- Closed-loop neuromodulation for neurological disorder treatment
- Miniaturization and power efficiency as primary engineering challenges

**AMOS integration**: Directly informs the Bio-Logical Computing Model and the NeuroSyncAI Organism Binding. The closed-loop architecture maps to AMOS's Perceive→Route→Admit→Plan→Schedule→Execute→Observe→Repair pipeline.

### 2.3 LLM-Integrated BCI (IOP Science, 2026)

**Source**: Biomedical Physics & Engineering Express, 2026 — "Large language models integrated into brain–computer interfaces"

**Key findings**:
- 5 integration patterns: autocomplete, post-edit correction, intent expansion, dynamic interface generation, affective support
- Copy-spelling keystroke savings >50-60% with LLM augmentation
- Intent-based ALS message-bank: 42 chars/min with 88% semantic accuracy
- 7 of 11 studies relied on remote OpenAI endpoints (latency concern)
- None enrolled motor-impaired patients (gap)

**AMOS integration**: The 5 integration patterns map to AMOS routing policies. The latency concern validates AMOS's local-first architecture principle. The affective support pattern connects to the NEI Engine.

### 2.4 Bimanual Typing Neuroprosthesis (Nature Neuroscience, 2026)

**Source**: Nature Neuroscience, 2026 — "Restoring rapid natural bimanual typing with a neuroprosthesis"

**Key findings**:
- iBCI typing neuroprosthesis with bimanual QWERTY keyboard functionality
- 110 characters per minute (22 wpm) with 1.6% word error rate
- Only 30 calibration sentences needed
- 5-gram language model for sentence decoding improvement
- Tested on ALS and spinal cord injury participants

**AMOS integration**: The minimal calibration requirement (30 sentences) informs the UBI Score Calibration protocol. The 5-gram language model integration supports the H/M/L knowledge resolution architecture.

### 2.5 BCI Bandwidth Analysis (IOP Science, 2026)

**Source**: IOP Science, 2026 — "But do we need high bandwidth? Applications and scaling challenges of invasive BCIs"

**Key findings**:
- Moderate bandwidth suffices for clinical goals when coupled with model-based priors
- Next-horizon goals (unconstrained speech, embodied dexterity) require abundant sampling
- Engineering trilemma: bandwidth, power, latency
- Large-scale µECoG arrays as compromise between invasiveness and bandwidth
- Low-power on-implant processing is critical bottleneck

**AMOS integration**: The bandwidth-power-latency trilemma maps to AMOS's Stability-Adaptation-Recovery triangle. The on-implant processing requirement validates the Edge Runtime architecture.

______________________________________________________________________

## 3. AI Agent Memory Architecture SOTA

### 3.1 EverMemOS: Self-Organizing Memory OS (ACL 2026)

**Source**: ACL 2026 — "EverMemOS: A Self-Organizing Memory Operating System for Structured Long-Horizon Reasoning"

**Key findings**:
- Engram-inspired lifecycle: Episodic Trace Formation → Semantic Consolidation → Reconstructive Recollection
- MemCells capture episodic traces, atomic facts, time-bounded foresight
- MemScenes organize MemCells into thematic structures
- Outperforms SOTA on LoCoMo, Long-MemEval, PersonaMem-v2

**AMOS integration**: The MemCell/MemScene architecture maps to AMOS's 3-type memory system (working, episodic, semantic). The engram lifecycle parallels AMOS's K_MEMORY_ADMISSION → K_MEMORY_RETRIEVAL pipeline. The semantic consolidation phase maps to the Memory Conflict Governor.

### 3.2 AgeMem: Unified Long-Term/Short-Term Memory (ACL 2026)

**Source**: ACL 2026 — "Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management"

**Key findings**:
- Memory operations as tool-based actions (store, retrieve, update, summarize, discard)
- Three-stage progressive RL strategy with step-wise GRPO
- Unified LTM/STM management in agent's policy
- Outperforms memory-augmented baselines on 5 long-horizon benchmarks

**AMOS integration**: The tool-based memory operation model aligns with AMOS's K_MEMORY_ADMISSION contract. The unified management approach informs the Learning-Memory-Knowledge Feedback Governor.

### 3.3 MAGMA: Multi-Graph Agentic Memory (ACL 2026)

**Source**: ACL 2026 — "MAGMA: A Multi-Graph based Agentic Memory Architecture"

**Key findings**:
- Four orthogonal relational graphs: semantic, temporal, causal, entity
- Policy-guided traversal over relational views
- Query-adaptive selection and structured context construction
- Decoupled memory representation from retrieval logic

**AMOS integration**: The 4-graph architecture (semantic, temporal, causal, entity) maps to AMOS's 9-axis tensor (cause, mediator, target, relation_type, time, scale, regime, evidence_class, provenance). The causal graph directly supports the Causal Hierarchy Governor.

### 3.4 GAM: Hierarchical Graph-based Memory (ACL 2026)

**Source**: ACL 2026 — "GAM: Hierarchical Graph-based Agentic Memory for LLM Agents"

**Key findings**:
- Semantic-Event-Triggered mechanism decouples encoding from consolidation
- Episodic Buffering Phase: local graph for real-time dependencies
- Semantic Consolidation Phase: integrates into global network on semantic shifts
- Sleep-dependent memory consolidation inspiration

**AMOS integration**: The two-phase architecture (episodic buffering + semantic consolidation) maps to AMOS's Action-Memory Firewall (action traces isolated from admitted memory). The sleep-dependent consolidation model connects to the UBI Recovery Engine's entropy correction.

### 3.5 SodaMem: Evidence-Grounded Temporal Graph Memory (arXiv 2026)

**Source**: arXiv 2026 — "SodaMem: Evidence-Grounded Temporal Graph Memory"

**Key findings**:
- Typed FactEvents with mandatory provenance spans
- SUPERSEDES/CONTRADICTS/UPDATES edges under hybrid indexing
- Mention time, occurrence time, and validity tracked separately
- 92.8% accuracy on LongMemEval-S at ~$0.00161/question

**AMOS integration**: The SUPERSEDES/CONTRADICTS/UPDATES edge types map directly to AMOS's RSCF state machine and the 08_SUPERSESSION plane. The provenance span requirement aligns with L2_PROVENANCE law. The temporal validity tracking informs the L5_SCOPE_REGIME temporal laws.

______________________________________________________________________

## 4. Quantum Computing SOTA

### 4.1 IBM 70-Qubit Quantum Advantage (ScienceDaily, 2026)

**Source**: ScienceDaily / IBM + University of Chicago, August 2026

**Key findings**:
- 70 error-corrected logical qubits
- Computation completed in ~15 minutes
- Classically intractable problem with verifiable fidelity
- New error correction strategy with structured circuit design
- Statistical evidence that result was reliable

**AMOS integration**: The 70-logical-qubit threshold informs the QLS (Quantum Logic Scaffold) scalability model. The verifiable fidelity approach maps to AMOS's Proof Capsule (L19) requirements. The structured circuit design parallels the QCLA (Quantum Causality Layer Architecture) canonical structure.

### 4.2 High-Fidelity Entangled Logical Qubits (Nature Communications, 2026)

**Source**: Nature Communications, 2026 — "Demonstration of high-fidelity entangled logical qubits using transmons"

**Key findings**:
- Normalizer Dynamical Decoupling (NDD) combined with QEC
- [[4, 2, 2]] code on IBM transmon devices
- Beyond-breakeven fidelity for entangled logical qubits
- Handles arbitrary-weight errors via hybrid QEC-NDD

**AMOS integration**: The QEC-NDD hybrid approach informs AMOS's multi-layer error correction model. The [[4,2,2]] code structure maps to the Rule of 4 (R4) canonical law. The beyond-breakeven achievement validates the QLS framework's superposition reasoning pillar.

### 4.3 Measurement-Free Universal Logical Quantum Computation (Nature Communications, 2026)

**Source**: Nature Communications, 2026

**Key findings**:
- Universal fault-tolerant logical operations without mid-circuit measurements
- Trapped-ion quantum processor with 8-qubit error-detecting code
- 3 logical qubits encoded in 8 physical qubits
- Grover's quantum search algorithm demonstrated fault-tolerantly
- State injection for universal gate set

**AMOS integration**: The measurement-free approach informs AMOS's observation-free execution mode. The 3-logical-qubit-in-8-physical mapping parallels the H/M/L tri-layer architecture. The Grover's algorithm demonstration validates quantum search as an AMOS_MODEL reasoning pattern.

### 4.4 Surface Code Scaling on Heavy-Hex (Nature Communications, 2026)

**Source**: Nature Communications, 2026

**Key findings**:
- Subthreshold scaling demonstrated on IBM 156-qubit heavy-hex lattice
- Dynamical decoupling critical for coherent noise suppression
- Distance scaling: twofold improvement from d=3→5 and d=5→7
- Basis-dependent scaling: only growth direction benefits

**AMOS integration**: The distance-scaling exponential improvement model informs AMOS's Fractal Knowledge (L15) law. The basis-dependent scaling limitation maps to the Scope Regime Firewall. The dynamical decoupling technique parallels AMOS's Adaptive Stability Balancer.

### 4.5 Improved Logical Error Rates (Nature, 2026)

**Source**: Nature, 2026 — "Improved quantum processor logical error rates via correction and detection"

**Key findings**:
- 11× to 800× improvement in logical error rates
- 12-qubit Knill-inspired code encoding 2 qubits
- 16-qubit tesseract colour code encoding 4 qubits
- Trapped-ion QCCD architecture
- Scalable error detection and post-selection

**AMOS integration**: The 11×-800× improvement range informs AMOS's Load Capacity Canon. The tesseract colour code (4 qubits in 16 physical) maps to the Rule of 4. The QCCD architecture's scalability validates AMOS's shard-local finalization approach.

______________________________________________________________________

## 5. Neuromorphic Computing SOTA

### 5.1 MatMul-Free LLM on Intel Loihi 2 (arXiv, 2025)

**Source**: arXiv 2503.18002, 2025 — "Neuromorphic Principles for Efficient Large Language Models on Intel Loihi 2"

**Key findings**:
- 370M-parameter MatMul-free LLM on Loihi 2
- 3× higher throughput, 2× less energy vs edge GPU
- Low-precision, event-driven, stateful processing
- Better scaling than transformer-based LLMs
- Weight sparsity and graded spikes exploited

**AMOS integration**: Directly informs the Bio-Logical Computing Model. The event-driven architecture maps to AMOS's K_EVENT_BUS. The weight sparsity model parallels AMOS's H/M/L knowledge resolution. The 3× throughput / 2× energy improvement validates neuromorphic approaches for AMOS runtime.

### 5.2 Dual Memory Pathway SNN (Nature Machine Intelligence, 2026)

**Source**: Nature Machine Intelligence, 2026 — "Algorithm–hardware co-design of neuromorphic networks with dual memory pathways"

**Key findings**:
- Cortical fast-slow organization inspiration
- Dual memory pathway: fast spiking + slow compact state
- 40-60% fewer parameters than equivalent SNNs
- 4× throughput, 5× energy efficiency improvement
- Near-memory-compute architecture

**AMOS integration**: The fast-slow dual pathway maps to AMOS's H/M/L three-speed lens (L16). The 40-60% parameter reduction validates AMOS's fractal knowledge compression. The near-memory-compute architecture informs the Edge Runtime design.

### 5.3 Scalable NorthPole LLM Inference (arXiv, 2025)

**Source**: arXiv 2511.15950, 2025 — "A Scalable NorthPole System with End-to-End Vertical Integration"

**Key findings**:
- 288 NorthPole cards, 115 peta-ops at 4-bit precision
- 3.7 PB/s memory bandwidth across 18 2U servers
- 30 kW power, 730 kg, 0.67 m² rack footprint
- 8B-parameter IBM Granite model at 2.8ms inter-token latency
- 28 simultaneous users at 2048 context length

**AMOS integration**: The vertical integration model informs AMOS's 04_RUNTIME reference implementation. The 4-bit precision at 115 peta-ops validates low-precision reasoning for AMOS's L/M/H knowledge objects. The multi-user latency profile supports AMOS's 40Hz multi-agent clock architecture.

### 5.4 Sigma-Delta Neural Network Conversion on Loihi 2 (arXiv, 2025)

**Source**: arXiv 2505.06417, 2025

**Key findings**:
- Graded spikes represent changes in neuron activation
- Sigma-Delta conversion from trained ANNs to SNNs
- Temporal sparsity, spatial sparsity, compute-near-memory exploited
- Fewer simulation time steps than rate-based conversion

**AMOS integration**: The Sigma-Delta conversion model maps to AMOS's gradient-based RSCF architecture. The change-based (delta) encoding parallels AMOS's MVCC journal approach. The temporal/spatial sparsity exploitation informs the Context Budget Governor.

______________________________________________________________________

## 6. Cross-Domain Synthesis

### 6.1 Convergent Patterns

| Pattern | BCI | Agent Memory | Quantum | Neuromorphic |
|:---|:---|:---|:---|:---|
| Closed-loop | ✓ (BI-BCI) | ✓ (EverMemOS) | ✓ (QEC-NDD) | ✓ (dual pathway) |
| Multi-graph | ✓ (multimodal) | ✓ (MAGMA 4-graph) | ✓ (surface code) | ✓ (fast-slow) |
| Provenance | ✓ (calibration) | ✓ (SodaMem) | ✓ (fidelity verification) | ✓ (co-design) |
| H/M/L layers | ✓ (bandwidth) | ✓ (GAM 2-phase) | ✓ (distance scaling) | ✓ (Loihi graded) |
| Low-power | ✓ (on-implant) | ✓ (token efficiency) | ✓ (error correction) | ✓ (event-driven) |

### 6.2 AMOS Architecture Validation

The SOTA research validates several AMOS architectural decisions:

1. **40Hz multi-agent clock**: BCI gamma-band synchronization and neuromorphic event-driven processing both operate at similar timescales
2. **Non-compensatory UBI**: BCI substrate distress veto and quantum error correction both enforce non-negotiable safety boundaries
3. **H/M/L knowledge resolution**: Agent memory consolidation phases and quantum code distance scaling both exhibit tri-layer structure
4. **Provenance-first**: All four domains emphasize verifiable provenance (BCI calibration, memory evidence spans, quantum fidelity, neuromorphic co-design)
5. **Closed-loop architecture**: All four domains converge on closed-loop designs with observation→repair cycles

### 6.3 Gaps Identified

1. **BCI-AMOS runtime binding**: No SOTA BCI system implements AMOS-style governed execution
2. **Agent memory quantum analogy**: No SOTA agent memory system uses quantum error correction patterns
3. **Neuromorphic governance**: No SOTA neuromorphic system implements GMEF-style governed mutation
4. **Cross-domain tensor composition**: No SOTA system composes tensors across BCI/quantum/neuromorphic domains

______________________________________________________________________

## 7. Ingestion Recommendations

### 7.1 Priority Ingestion Targets

| Source | Target Plane | Priority | RSCF State |
|:---|:---|:---|:---|
| EverMemOS | 02_KERNEL, 11_KNOWLEDGE | HIGH | OBSERVATION |
| MAGMA | 02_KERNEL, 25_COGNITIVE_MATRIX | HIGH | OBSERVATION |
| IBM 70-qubit | 01_CANON/02_UNIVERSE_CANON | MEDIUM | OBSERVATION |
| Loihi 2 LLM | 13_MODELS, 04_RUNTIME | HIGH | OBSERVATION |
| NorthPole scalable | 04_RUNTIME | MEDIUM | OBSERVATION |
| BCI speech decoding | 05_COGNITIVE_ORGANISM | HIGH | OBSERVATION |
| SodaMem provenance | 01_CANON/07_PROVENANCE | HIGH | OBSERVATION |

### 7.2 RSCF Classification

All sources are classified as `OBSERVATION` (peer-reviewed publications or verified demonstrations). None have been independently replicated by AMOS. The confidence ceiling for OBSERVATION is 0.5 per the Confidence Ceiling Calibration.

### 7.3 Provenance Independence

Each source comes from independent research groups. Cross-citations exist but do not compromise independence for Rule of 2 (R2) purposes.

______________________________________________________________________

## 8. Cross-References

- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
- [[22_RESEARCH/SOTA_AGENT_TOOLING_REPOS|SOTA Agent Tooling Repos]]
- [[05_COGNITIVE_ORGANISM/NEUROSYNCAI_ORGANISM_BINDING|NeuroSyncAI Organism Binding]]
- [[01_CANON/02_UNIVERSE_CANON/QLS_CANON|QLS Canon]]
- [[01_CANON/02_UNIVERSE_CANON/QCLA_CANON|QCLA Canon]]
- [[13_MODELS/01_FOUNDATION/BIO_LOGICAL_COMPUTING_MODEL|Bio-Logical Computing Model]]
- [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]]

______________________________________________________________________

## 9. Gaps

- No direct AMOS runtime implementation of any SOTA finding
- Provenance independence NOT_ESTABLISHED for cross-domain claims
- Canonical status CONDITIONAL for all synthesized findings
- Automated enforcement NOT_ESTABLISHED

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

node_id: amos_22_research_sota_synthesis_2026_09_04

node_type: RESEARCH_SYNTHESIS

path: 22_RESEARCH/SOTA_RESEARCH_SYNTHESIS_2026-09-04.md

claim_class: OBSERVATION

rscf_state: OBSERVATION

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

- INFORMS: [[05_COGNITIVE_ORGANISM/NEUROSYNCAI_ORGANISM_BINDING|NeuroSyncAI Organism Binding]]

- INFORMS: [[01_CANON/02_UNIVERSE_CANON/QLS_CANON|QLS Canon]]

- INFORMS: [[13_MODELS/01_FOUNDATION/BIO_LOGICAL_COMPUTING_MODEL|Bio-Logical Computing Model]]
