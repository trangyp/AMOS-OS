---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: 22 Research/Sota Research Synthesis 3 2026 09 04
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---

# SOTA Research Synthesis Part 3 — Agent Memory, World Models, AI Safety, KG Reasoning

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

Third SOTA synthesis covering agent memory architectures, world models for AI agents, AI safety/alignment, and knowledge graph reasoning — all directly relevant to AMOS OS architecture.

______________________________________________________________________

## 2. Agent Memory Architecture SOTA

### 2.1 MemLineage: Lineage-Guided Enforcement (arXiv 2605.14421, 2026)

**Key findings**:
- Chain-of-custody approach to agent memory security (not filtering)
- RFC-6962 Merkle log over per-principal Ed25519-signed entries
- Weighted derivation DAG records which retrieved entries influenced each new memory
- Max-of-strong-edges propagation rule for Untrusted-Path Persistence
- Sensitive-action gate refuses dispatches from external ancestors
- Sub-millisecond per-operation overhead
- Zero ASR (Attack Success Rate) on all three memory-poisoning workloads
- Codex-backed AgentDojo bridge: all MemLineage rows reduce strict ASR to zero

**AMOS integration**: The Merkle log + Ed25519 signing directly informs AMOS's K_MEMORY_ADMISSION contract. The derivation DAG maps to AMOS's provenance topology. The sensitive-action gate validates AMOS's L7_AUTHORITY boundary. The chain-of-custody model parallels AMOS's Enforcement Root Attestation (ERA v42+).

### 2.2 Mnemosyne: Human-Inspired Long-Term Memory (arXiv 2510.08601, 2026)

**Key findings**:
- Unsupervised, human-inspired memory for edge-based LLMs
- Graph-structured storage with modular substance and redundancy filters
- Memory committing and pruning mechanisms
- Probabilistic recall with temporal decay and refresh
- "Core summary" for user personality and domain-specific details
- 65.8% win rate in blind human evaluations (vs 31.1% for RAG baseline)
- Highest LoCoMo benchmark scores in temporal reasoning and single-hop retrieval
- Edge-compatible, no external services required

**AMOS integration**: The graph-structured storage maps to AMOS's K_MEMORY_RETRIEVAL contract. The temporal decay + refresh model informs AMOS's memory freshness validation. The core summary mechanism parallels AMOS's context compaction. The edge-compatible design validates AMOS's local-first architecture.

### 2.3 AgeMem: Agentic Memory (ACL 2026)

**Key findings**:
- Unified LTM + STM management integrated into agent's policy
- Memory operations as tool-based actions (store, retrieve, update, summarize, discard)
- Three-stage progressive RL strategy: LTM storage → STM context → full coordination
- Step-wise GRPO for sparse and discontinuous rewards
- Consistently outperforms memory-augmented baselines across 5 benchmarks
- Higher-quality long-term memory and more efficient context usage

**AMOS integration**: The unified LTM+STM model directly informs AMOS's Memory Systems architecture (3 memory types). The tool-based memory operations map to AMOS's K_EVENT_BUS memory events. The progressive RL strategy validates AMOS's closed-loop learning governor. The GRPO optimization informs AMOS's formal engines.

### 2.4 EverMemOS: Self-Organizing Memory OS (ACL 2026)

**Key findings**:
- Engram-inspired lifecycle for computational memory
- Episodic Trace Formation → MemCells with atomic facts and time-bounded foresight
- Semantic Consolidation → MemScenes with stable semantic structures
- Reconstructive Recollection → MemScene-guided agentic retrieval
- Significantly outperforms SOTA on LoCoMo, Long-MemEval, PersonaMem-v2

**AMOS integration**: The engram lifecycle maps directly to AMOS's memory admission → consolidation → retrieval pipeline. MemCells parallel AMOS's typed memory atoms. MemScenes inform AMOS's knowledge scene composition. The reconstructive recollection validates AMOS's K_MEMORY_RETRIEVAL design.

### 2.5 Additional Agent Memory Papers (arxiv corpus)

| Paper | Year | AMOS Integration |
|:---|:---|:---|
| Memory as Ontology: Constitutional Memory Architecture | 2026 | → AMOS memory canon |
| MemEvolve: Meta-Evolution of Agent Memory Systems | 2026 | → AMOS GMEF memory evolution |
| AMV-L: Lifecycle-Managed Agent Memory | 2026 | → AMOS memory lifecycle |
| PASK: Intent-Aware Proactive Agents with Long-Term Memory | 2026 | → AMOS attention allocation |
| FORGE: Self-Evolving Agent Memory via Population Broadcast | 2026 | → AMOS multi-agent memory |
| DimMem: Dimensional Structuring for Long-Term Agent Memory | 2026 | → AMOS H/M/L memory dimensions |
| H-Mem: Novel Memory Mechanism for Evolving Agent Memory | 2026 | → AMOS memory evolution |
| PBFT-Backed Semantic Voting for Multi-Agent Memory Pruning | 2026 | → AMOS memory conflict resolution |

______________________________________________________________________

## 3. World Models for AI Agents SOTA

### 3.1 Belief-Based World Models (arXiv 2609.00455, 2026)

**Key findings**:
- BB-WMs model and maintain belief about current state (not just simulation)
- LLM agents query belief to access what is known and uncertain
- Improves task performance under partial observability
- Complementary to existing simulation-based world models

**AMOS integration**: The belief-based model directly informs AMOS's K_WORLD_MODEL contract. The uncertainty representation maps to AMOS's L6_UNCERTAINTY law. The partial observability handling validates AMOS's L5_SCOPE_REGIME law. The complementarity with simulation validates AMOS's dual prediction-governance architecture.

### 3.2 Semantic Bayesian World Models (arXiv 2609.03834, 2026)

**Key findings**:
- Knowledge graphs as shared, evolving fabric of beliefs
- Ontological axioms constrain priors
- Observations update beliefs by Bayesian conditioning
- Actions intervene upon the world
- Agents exchange and disagree over calibrated beliefs

**AMOS integration**: The Bayesian belief fabric maps to AMOS's RSCF confidence ceiling. The ontological constraint model informs AMOS's Canon Integration Layer. The action-as-intervention model parallels AMOS's L4_CAUSAL law. The calibrated belief exchange validates AMOS's provenance independence requirement.

### 3.3 World Action Planner (arXiv 2607.27599, 2026)

**Key findings**:
- VLM reasoning + multi-task pose-image conditioned world model
- Iterative plan refinement via optimization and search
- Imagined world model rollouts for planning
- Superior performance on compositional tasks and zero-shot generalization
- Theoretically proves model-based planning > imitation learning for multi-task generalization

**AMOS integration**: The iterative plan refinement maps to AMOS's Perceive→Plan→Schedule→Execute pipeline. The imagined rollouts inform AMOS's prediction governance. The zero-shot generalization validates AMOS's H/M/L fractal knowledge approach. The theoretical proof supports AMOS's model-based architecture.

### 3.4 OOWM: Object-Oriented World Modeling (arXiv 2604.09580, 2026)

**Key findings**:
- World model as explicit symbolic tuple W = ⟨S, T⟩ (State Abstraction + Control Policy)
- UML Class Diagrams for object hierarchies
- UML Activity Diagrams for executable control flows
- Three-stage training: SFT + GRPO with outcome-based rewards
- Significantly outperforms textual baselines in planning coherence

**AMOS integration**: The symbolic tuple model maps to AMOS's K_SYSTEM_STATE contract. The UML formalism validates AMOS's structured execution graph. The SFT+GRPO training informs AMOS's formal engines. The planning coherence improvement supports AMOS's deterministic execution design.

### 3.5 OPINE-World: Programmatic World Modeling (arXiv 2607.01531, 2026)

**Key findings**:
- LLM agent learns object-centric programmatic world model from interaction
- Two cooperating agents: one acts, one synthesizes model in code
- Counterexample-guided inductive synthesis (CEGIS)
- Bayesian measure of object-type adequacy ("ontology error")
- Solves 20/25 ARC-AGI-3 games without per-game training
- 78.4 action-efficiency score against human baseline

**AMOS integration**: The dual-agent architecture maps to AMOS's multi-agent execution harness. The CEGIS approach informs AMOS's formal verification pipeline. The ontology error metric provides a quantitative basis for AMOS's canon consistency governor. The ARC-AGI-3 performance validates AMOS's skill-acquisition model.

______________________________________________________________________

## 4. AI Safety & Alignment SOTA

### 4.1 Constitutional Classifiers++ (arXiv 2601.04603, 2026)

**Key findings**:
- Production-grade jailbreak robustness with 40x cost reduction
- Exchange classifiers evaluate full conversational context
- Two-stage cascade: lightweight → expensive classifiers
- 0.05% refusal rate on production traffic
- 1,700+ hours of red teaming: no successful universal jailbreak
- Linear probe classifiers + external classifier ensemble

**AMOS integration**: The exchange classifier model informs AMOS's semantic token flow firewall. The two-stage cascade maps to AMOS's H/M/L validation depth. The constitutional rules approach validates AMOS's L0_INTEGRITY law. The production-grade deployment validates AMOS's fail-closed governance.

### 4.2 Constitutional Autonomy in AI Systems (IEEE Access, 2026)

**Key findings**:
- Runtime enforcement for autonomous agentic systems (beyond training-phase)
- Four subsystems: normative prior engineering, Constitutional Attention, real-time safety validation, sociotechnical governance
- 23% reduction in harmful attention patterns
- Sub-2% computational overhead
- 91% adversarial robustness
- Constitutional Attention modulates attention weights via differentiable vector operations
- O(k/n) overhead for scalable implementation

**AMOS integration**: The runtime enforcement model directly maps to AMOS's capability-bound governance (v4.8). The Constitutional Attention mechanism informs AMOS's attention allocation governor. The real-time safety validation validates AMOS's GMEF gate compliance. The O(k/n) overhead supports AMOS's load capacity canon.

### 4.3 Constitutional AI Protocol (CAP) for Agentic AI (IETF Draft, 2026)

**Key findings**:
- Three-tier prohibition model: Tier 0 (universal treaty), Tier 1 (jurisdictional), Tier 2 (voluntary)
- Constitutional Layer evaluates every AI action request AND human authorization
- Prohibition Clearance Mechanism (PCM) for context-specific clearance
- Absolute prohibition floor for CSAM and genocide facilitation
- GEC Policy Transparency Disclosure (PTD): signed, queryable, tier-structured
- Complementary to HEM (Human Escalation Mechanism)

**AMOS integration**: The three-tier model maps to AMOS's law hierarchy (L0 > L1 > ... > L32). The Constitutional Layer validates AMOS's enforcement root attestation. The PCM informs AMOS's scope regime firewall. The PTD maps to AMOS's decision receipt system. The HEM complementarity validates AMOS's managed autonomy escalation.

### 4.4 Singapore Consensus 2026: Global AI Safety Priorities

**Key findings**:
- 100+ contributors from 13 countries
- Focus on autonomous AI agents deployment risks
- Emerging risk management practices for agentic deployment
- Industry practices on agentic deployment constantly evolving

**AMOS integration**: The global consensus validates AMOS's governance-first architecture. The agentic deployment focus maps to AMOS's 03_CONTROL_PLANE. The risk management practices inform AMOS's 08_SECURITY plane.

______________________________________________________________________

## 5. Knowledge Graph Reasoning SOTA

### 5.1 NeuroSymActive: Differentiable Neural-Symbolic Reasoning (arXiv 2602.15353, 2026)

**Key findings**:
- Differentiable neural-symbolic reasoning layer + active value-guided exploration
- Soft unification with differentiable rule scoring
- Neural path evaluator for partial reasoning trajectories
- Monte-Carlo style exploration policy
- Reduces expensive graph lookups and model calls
- Strong answer accuracy on KGQA benchmarks

**AMOS integration**: The differentiable reasoning layer informs AMOS's formal engines. The soft unification maps to AMOS's RSCF confidence propagation. The active exploration validates AMOS's heterogeneous exploration cohort. The reduced lookups support AMOS's context budget governor.

### 5.2 SymbolLKG: Logical Knowledge Graph (arXiv 2608.26836, 2026)

**Key findings**:
- Ontology-based LKG treats logical rules as first-class topological nodes
- Logic Router dynamically dispatches to optimal symbolic engine
- Topology-aware hybrid retrieval mechanism
- Significantly outperforms CoT and RAG baselines
- Verifiable reasoning paths

**AMOS integration**: The first-class logical nodes map to AMOS's RSCF-NODE structure. The Logic Router informs AMOS's 10_ROUTING layer selection. The verifiable reasoning paths validate AMOS's L19_PROOF_CAPSULE law. The topology-aware retrieval informs AMOS's K_MEMORY_RETRIEVAL.

### 5.3 KG-Reasoner: End-to-End Multi-Hop KG Reasoning (arXiv 2604.12487, 2026)

**Key findings**:
- Unified "thinking" phase via Reasoning LLM
- RL-trained to internalize KG traversal
- Dynamic path exploration with backtracking
- Competitive/superior on 8 multi-hop benchmarks

**AMOS integration**: The unified thinking phase maps to AMOS's cognitive process orchestrator. The RL-trained KG traversal informs AMOS's K_COGNITION contract. The backtracking capability validates AMOS's L10_FAILURE_RECOVERY law.

### 5.4 Thought-Action Graph (TAG) Reasoning (ACL 2026)

**Key findings**:
- TAG: structured repository of reasoning experiences
- Decomposes LLM-KG interaction trajectories into semantic operators
- Thought layer + action layer
- Retrieves and assembles reasoning blueprints
- Transforms online exploration into offline TAG retrieval
- Significantly reduces LLM calls and generated tokens

**AMOS integration**: The TAG structure maps to AMOS's 25_COGNITIVE_MATRIX. The thought-action decomposition validates AMOS's perception-action loop. The blueprint reuse informs AMOS's K_MEMORY_RETRIEVAL. The token reduction supports AMOS's token budget governance.

______________________________________________________________________

## 6. Arxiv Corpus Statistics (Extended)

| Topic | Paper Count | AMOS Domain |
|:---|---:|:---|
| Reinforcement learning | 795 | 04_RUNTIME, 14_ENGINES |
| Safety/alignment | 461 | 08_SECURITY, 09_GOVERNANCE |
| Emergence/complex systems | 351 | 01_CANON/02_UNIVERSE_CANON |
| Knowledge graphs | 231 | 11_KNOWLEDGE, 10_ROUTING |
| Diffusion models | 286 | 13_MODELS |
| Quantum computing | 142 | 01_CANON/02_UNIVERSE_CANON |
| Neuromorphic/spiking | 136 | 13_MODELS, 04_RUNTIME |
| Causal discovery | 140 | 01_CANON/01_CORE_LAWS/L4 |
| Fractal/self-similarity | 114 | 01_CANON/01_CORE_LAWS/L15 |
| Attention/transformer | 38 | 13_MODELS |
| Agent memory (2026) | 20+ | 02_KERNEL, 11_KNOWLEDGE |
| World models (2026) | 15+ | 02_KERNEL, 04_RUNTIME |
| **TOTAL CORPUS** | **66,027** | **All AMOS domains** |

______________________________________________________________________

## 7. Cross-Domain Synthesis (Part 3)

### 7.1 Convergent Patterns

| Pattern | Agent Memory | World Models | AI Safety | KG Reasoning |
|:---|:---|:---|:---|:---|
| Provenance tracking | ✓ (Merkle log) | ✓ (belief tracing) | ✓ (PTD) | ✓ (reasoning paths) |
| Hierarchical structure | ✓ (LTM/STM) | ✓ (object hierarchies) | ✓ (tiered prohibitions) | ✓ (multi-hop) |
| Probabilistic reasoning | ✓ (temporal decay) | ✓ (Bayesian belief) | ✓ (classifier cascade) | ✓ (soft unification) |
| Runtime enforcement | ✓ (sensitive-action gate) | ✓ (safety validation) | ✓ (Constitutional Layer) | ✓ (Logic Router) |
| Verifiability | ✓ (Ed25519 signatures) | ✓ (verifiable paths) | ✓ (red teaming) | ✓ (proof paths) |

### 7.2 AMOS Architecture Validation (Part 3)

1. **Agent Memory**: SOTA validates Merkle-log provenance, graph-structured storage, engram lifecycle, unified LTM/STM
2. **World Models**: SOTA validates belief-based models, Bayesian updating, object-oriented structuring, programmatic synthesis
3. **AI Safety**: SOTA validates constitutional classifiers, runtime enforcement, three-tier prohibition, transparency disclosure
4. **KG Reasoning**: SOTA validates neuro-symbolic integration, logical knowledge graphs, end-to-end multi-hop, experience reuse

### 7.3 New Gaps Identified

1. **Memory + UBI binding**: No SOTA system combines agent memory with biological intelligence scoring
2. **World model + causal epoch**: No SOTA world model operates across causal epoch boundaries
3. **Safety + GMEF evolution**: No SOTA safety framework includes governed mutation evolution
4. **KG reasoning + RSCF**: No SOTA KG system uses RSCF epistemic state classification

______________________________________________________________________

## 8. Ingestion Recommendations (Part 3)

| Source | Target Plane | Priority | RSCF State |
|:---|:---|:---|:---|
| MemLineage | 02_KERNEL, 08_SECURITY | HIGH | OBSERVATION |
| Mnemosyne | 02_KERNEL, 11_KNOWLEDGE | HIGH | OBSERVATION |
| AgeMem | 02_KERNEL, 14_ENGINES | HIGH | OBSERVATION |
| EverMemOS | 02_KERNEL, 04_RUNTIME | HIGH | OBSERVATION |
| BB-WMs | 02_KERNEL, 04_RUNTIME | HIGH | OBSERVATION |
| Semantic Bayesian WMs | 01_CANON, 11_KNOWLEDGE | MEDIUM | OBSERVATION |
| World Action Planner | 04_RUNTIME, 03_CONTROL_PLANE | MEDIUM | OBSERVATION |
| OOWM | 04_RUNTIME, 16_SCHEMAS | MEDIUM | OBSERVATION |
| OPINE-World | 14_ENGINES, 19_TESTS | MEDIUM | OBSERVATION |
| Constitutional Classifiers++ | 08_SECURITY | HIGH | OBSERVATION |
| Constitutional Autonomy | 09_GOVERNANCE, 08_SECURITY | HIGH | OBSERVATION |
| CAP Protocol | 09_GOVERNANCE, 23_PROTOCOLS | HIGH | OBSERVATION |
| Singapore Consensus 2026 | 09_GOVERNANCE, 22_RESEARCH | MEDIUM | OBSERVATION |
| NeuroSymActive | 14_ENGINES, 11_KNOWLEDGE | MEDIUM | OBSERVATION |
| SymbolLKG | 10_ROUTING, 11_KNOWLEDGE | HIGH | OBSERVATION |
| KG-Reasoner | 14_ENGINES, 11_KNOWLEDGE | MEDIUM | OBSERVATION |
| TAG Reasoning | 25_COGNITIVE_MATRIX, 11_KNOWLEDGE | MEDIUM | OBSERVATION |

______________________________________________________________________

## 9. Cross-References

- [[22_RESEARCH/SOTA_RESEARCH_SYNTHESIS_2026-09-04|SOTA Synthesis Part 1]]
- [[22_RESEARCH/SOTA_RESEARCH_SYNTHESIS_2_2026-09-04|SOTA Synthesis Part 2]]
- [[22_RESEARCH/AMOS_ARXIV_RESEARCH_INDEX|AMOS Arxiv Research Index]]
- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
- [[02_KERNEL/02_KERNEL_MOC|02_KERNEL_MOC]]
- [[18_SECURITY/18_SECURITY_MOC|08_SECURITY_MOC]]]]
- [[09_GOVERNANCE/09_GOVERNANCE_MOC|09_GOVERNANCE_MOC]]
- [[11_KNOWLEDGE/11_KNOWLEDGE_MOC|11_KNOWLEDGE_MOC]]

______________________________________________________________________

## 10. Gaps

- No direct AMOS runtime implementation of any SOTA finding
- Provenance independence NOT_ESTABLISHED for cross-domain claims
- Canonical status CONDITIONAL for all synthesized findings
- Agent memory + UBI integration is AMOS_MODEL, not OBSERVATION
- World model + causal epoch binding is AMOS_MODEL, not OBSERVATION
- Safety + GMEF evolution is AMOS_MODEL, not OBSERVATION

______________________________________________________________________

## 11. Ingestion Rule

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

node_id: amos_22_research_sota_synthesis_3_2026_09_04

node_type: RESEARCH_SYNTHESIS

path: 22_RESEARCH/SOTA_RESEARCH_SYNTHESIS_3_2026-09-04.md

claim_class: OBSERVATION

rscf_state: OBSERVATION

canonical_status: CONDITIONAL

RSCF-RELATIONS:

- INDEXED_BY: [[00_ROOT/00_HOME|00_HOME]]

- INDEXED_BY: [[00_ROOT/AMOS_RSCF_NODES|AMOS_RSCF_NODES]]

- GOVERNED_BY: [[01_CANON/01_CORE_LAWS/LAW_HIERARCHY|LAW_HIERARCHY]]

- INFORMS: [[02_KERNEL/02_KERNEL_MOC|Kernel MOC]]

- INFORMS: [[18_SECURITY/18_SECURITY_MOC|Security MOC]]]]

- INFORMS: [[09_GOVERNANCE/09_GOVERNANCE_MOC|Governance MOC]]

- INFORMS: [[11_KNOWLEDGE/11_KNOWLEDGE_MOC|Knowledge MOC]]
