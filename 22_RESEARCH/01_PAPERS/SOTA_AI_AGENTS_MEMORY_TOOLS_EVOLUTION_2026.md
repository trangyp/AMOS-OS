---
title: "SOTA AI Agents Memory Tools & Evolution 2026"
type: sota_paper
domain: [ai_agents, memory_systems, tool_use, self_evolution, multi_agent]
created: 2026-09-05
updated: 2026-09-05
tags:
  - amos-os
  - sota
  - research
  - ai-agents
  - memory-systems
  - tool-use
  - self-evolution
  - multi-agent
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: arxiv_2026
  scope: AMOS_general
confidence_ceiling: 0.93
---

# SOTA AI Agents Memory Tools & Evolution 2026

> **Synthesis date:** 2026-09-05 · **Domain:** AI Agent Memory Systems, Tool-Side Memory, Self-Evolving Multi-Agent Frameworks · **Epistemic class:** SOURCE_CLAIM

## 1. Overview

The AI agent memory and tool-use landscape has converged on **structured, persistent, and evolving memory** as the critical differentiator for agent performance in 2026. The frontier has moved from flat context windows to graph-structured memory, provenance-aware shared state, and co-evolutionary skill-workflow systems. Eight key advances define the SOTA:

1. **Tool-side memory graphs** that track tool usage patterns and composition relationships (ToolAtlas)
2. **Self-evolving multi-agent systems** with elastic memory compression (AutoAgent)
3. **Provenance-aware shared memory** for multi-agent task success (MAP-Graph)
4. **Conflict-aware memory primitives** for contradiction detection and resolution (LatticeMind)
5. **Reference trajectory learning** that prevents catastrophic forgetting during harness evolution (HarnessEvolve)
6. **Globally reusable skill graphs** with relation-aware composition (GSE)
7. **Self-developing coding agents** with reviewed core evolution (Ouroboros)
8. **Workflow-skill co-evolution** achieving dramatic token efficiency (FlowEvo)

These advances directly inform AMOS OS's [[10_MEMORY/10_MEMORY_MOC|memory plane]], [[07_SKILLS/amos-agent-systems-master/SKILL|agent systems]], and [[07_SKILLS/amos-autonomous-evolution/SKILL|autonomous evolution]] architecture.

## 2. Key Papers & Breakthroughs

### 2.1 ToolAtlas — Tool-Side Memory Graph
- **arXiv ID:** arXiv:2607.11126
- **Domain:** Tool use, agent memory, tool composition
- **Key result:** Introduces a tool-side memory graph that persists tool usage patterns, composition relationships, and success/failure outcomes across agent sessions. ToolAtlas achieves a 21.6% pass@1 improvement on multi-step tool-use benchmarks by enabling agents to recall and reuse successful tool compositions. The memory graph structure allows agents to discover novel tool chains through graph traversal rather than exhaustive search, reducing planning overhead.
- **AMOS mapping:** [[10_MEMORY/10_MEMORY_MOC|Memory plane]] (tool-use memory graph), [[07_SKILLS/amos-skill-dependency-graph/SKILL|skill dependency graph]] (tool composition as dependency graph), [[07_SKILLS/amos-agent-systems-master/SKILL|agent systems]] (tool composition discovery)
- **Epistemic class:** SOURCE_CLAIM
- **Confidence ceiling:** 0.90

### 2.2 AutoAgent — Self-Evolving Multi-Agent with Elastic Memory
- **arXiv ID:** arXiv:2603.09716
- **Domain:** Multi-agent systems, memory compression, self-evolution
- **Key result:** Presents a self-evolving multi-agent framework with elastic memory compression that dynamically adjusts memory allocation based on task complexity and agent role. AutoAgent's elastic compression maintains critical information while discarding low-relevance context, enabling sustained operation over long horizons without context window exhaustion. The self-evolution mechanism allows agents to modify their own role definitions and collaboration protocols based on observed performance.
- **AMOS mapping:** [[07_SKILLS/amos-autonomous-evolution/SKILL|autonomous evolution]] (self-evolving agent roles), [[10_MEMORY/10_MEMORY_MOC|Memory plane]] (elastic memory compression), [[07_SKILLS/amos-token-budget-governance/SKILL|token budget governance]] (dynamic memory allocation)
- **Epistemic class:** SOURCE_CLAIM
- **Confidence ceiling:** 0.88

### 2.3 MAP-Graph — Provenance-Aware Shared Memory
- **arXiv ID:** arXiv:2608.10509
- **Domain:** Multi-agent memory, provenance tracking, shared state
- **Key result:** Introduces provenance-aware shared memory for multi-agent systems, achieving 94.96% task success rate on collaborative benchmarks. MAP-Graph tracks the origin and modification history of every shared memory entry, enabling agents to reason about information trustworthiness and resolve conflicting updates. Provenance tracking allows rollback to any prior state of shared memory, providing a safety mechanism for multi-agent collaboration.
- **AMOS mapping:** [[10_MEMORY/10_MEMORY_MOC|Memory plane]] (provenance-aware shared memory), [[07_SKILLS/amos-audit-trail/SKILL|audit trail]] (provenance tracking), [[07_SKILLS/amos-rollback-recovery/SKILL|rollback recovery]] (shared memory rollback), [[09_PROTOCOLS/ZK_MERKLE_GOSSIP_CONSENSUS_LEDGER|Merkle gossip consensus]] (shared state consistency)
- **Epistemic class:** SOURCE_CLAIM
- **Confidence ceiling:** 0.91

### 2.4 LatticeMind — Conflict-Aware Memory Primitive
- **arXiv ID:** arXiv:2608.08236
- **Domain:** Memory conflict resolution, contradiction detection
- **Key result:** Introduces a conflict-aware memory primitive that detects and resolves contradictions in agent memory with 0.97 conflict accuracy. LatticeMind uses a lattice-based representation where memory entries are ordered by specificity and trust level, enabling principled resolution when conflicting information is encountered. The conflict detection mechanism operates in real-time during memory writes, preventing contradictory information from corrupting downstream reasoning.
- **AMOS mapping:** [[10_MEMORY/10_MEMORY_MOC|Memory plane]] (conflict-aware memory writes), [[07_SKILLS/amos-failure-memory/SKILL|failure memory]] (contradiction as failure signal), [[07_SKILLS/amos-capability-bound-governance/SKILL|capability-bound governance]] (memory write authority gates)
- **Epistemic class:** SOURCE_CLAIM
- **Confidence ceiling:** 0.89

### 2.5 HarnessEvolve — Reference Trajectory Learning
- **arXiv ID:** arXiv:2609.00829
- **Domain:** Agent harness evolution, catastrophic forgetting prevention
- **Key result:** Presents reference trajectory learning for agent harness evolution that prevents catastrophic forgetting when harness components are modified. HarnessEvolve maintains a reference trajectory of successful task executions and uses it as a constraint during harness updates, ensuring that evolution does not regress on previously solved tasks. The approach enables continuous harness improvement without the performance cliffs typically associated with uncontrolled self-modification.
- **AMOS mapping:** [[07_SKILLS/amos-autonomous-evolution/SKILL|autonomous evolution]] (evolution with regression prevention), [[07_SKILLS/amos-evolution-loop/SKILL|evolution loop]] (reference trajectory as convergence constraint), [[07_SKILLS/amos-rollback-recovery/SKILL|rollback recovery]] (regression-triggered rollback), [[19_TESTS/19_TESTS_README|Test plane]] (regression testing during evolution)
- **Epistemic class:** SOURCE_CLAIM
- **Confidence ceiling:** 0.87

### 2.6 GSE — Globally Reusable Skills with Skill Relation Graph
- **arXiv ID:** arXiv:2608.06153
- **Domain:** Skill reuse, skill composition, relation graphs
- **Key result:** Introduces a Skill Relation Graph that captures semantic and functional relationships between agent skills, enabling globally reusable skill composition. GSE achieves a 61.4% F1 improvement on skill selection and composition benchmarks by leveraging relation-aware retrieval. The Skill Relation Graph allows agents to discover substitute and complementary skills, reducing the need for exhaustive skill enumeration during planning.
- **AMOS mapping:** [[07_SKILLS/amos-skill-dependency-graph/SKILL|skill dependency graph]] (skill relation graph), [[07_SKILLS/amos-domain-skill-router/SKILL|domain skill router]] (relation-aware skill routing), [[07_SKILLS/amos-agent-systems-master/SKILL|agent systems]] (skill composition discovery)
- **Epistemic class:** SOURCE_CLAIM
- **Confidence ceiling:** 0.88

### 2.7 Ouroboros — Self-Developing Coding Agent
- **arXiv ID:** arXiv:2608.08311
- **Domain:** Self-developing agents, reviewed core evolution, coding agents
- **Key result:** Presents a self-developing coding agent where tools, context assembly, prompts, and core implementation improve through reviewed commits that become the runtime for later work. Ouroboros operates in two evolution modes: recursive free evolution (improvement as a task) and experience-driven core evolution (bugs from ordinary work drive structural changes). Terminal-Bench 2.1 score 86.97% (Opus 5); OSWorld-Verified 90.69%; 161-day living-agent deployment under governed human communication.
- **AMOS mapping:** [[07_SKILLS/amos-autonomous-evolution/SKILL|autonomous evolution]] (self-developing harness with trusted-core), [[07_SKILLS/amos-capability-bound-governance/SKILL|capability-bound governance]] (guardrails authoritative under evolutionary pressure), [[07_SKILLS/amos-evolution-receipt/SKILL|evolution receipts]] (reviewed commits as receipts)
- **Epistemic class:** SOURCE_CLAIM
- **Confidence ceiling:** 0.92

### 2.8 FlowEvo — Workflow-Skill Co-Evolution
- **arXiv ID:** arXiv:2607.21596
- **Domain:** Workflow evolution, skill co-evolution, token efficiency
- **Key result:** Introduces workflow-skill co-evolution where workflows and skills improve together through mutual feedback, achieving 85.6% success on ALFWorld while using only 1/3 of the tokens of baseline approaches. FlowEvo's co-evolution mechanism ensures that workflow modifications trigger corresponding skill updates and vice versa, maintaining coherence between procedural knowledge and executable capabilities. The dramatic token efficiency improvement demonstrates that co-evolved workflows are more compact and effective than independently optimized components.
- **AMOS mapping:** [[07_SKILLS/amos-evolution-loop/SKILL|evolution loop]] (co-evolution of workflows and skills), [[07_SKILLS/amos-token-budget-governance/SKILL|token budget governance]] (token-efficient execution), [[07_SKILLS/amos-workflow-optimization/SKILL|workflow optimization]] (co-evolutionary workflow improvement)
- **Epistemic class:** SOURCE_CLAIM
- **Confidence ceiling:** 0.89

## 3. Architectural Implications for AMOS OS

### 3.1 Memory as a First-Class Governed Artifact
MAP-Graph and LatticeMind establish that agent memory must be a governed artifact with provenance, conflict detection, and rollback:
- **Provenance-aware memory** maps directly to AMOS [[07_SKILLS/amos-audit-trail/SKILL|audit trail]] — every memory write must carry provenance
- **Conflict-aware writes** map to AMOS [[07_SKILLS/amos-capability-bound-governance/SKILL|capability-bound governance]] — memory writes are mutations requiring authority
- **Shared memory rollback** maps to AMOS [[07_SKILLS/amos-rollback-recovery/SKILL|rollback recovery]] — multi-agent shared state must be rollback-capable

### 3.2 Skill and Tool Composition as Graph Structure
ToolAtlas and GSE demonstrate that tool/skill relationships are best represented as graphs:
- **Tool-side memory graphs** map to AMOS [[07_SKILLS/amos-skill-dependency-graph/SKILL|skill dependency graph]] — tool composition is a graph traversal problem
- **Skill Relation Graphs** map to AMOS [[07_SKILLS/amos-domain-skill-router/SKILL|domain skill router]] — relation-aware routing improves skill selection
- **Graph-based composition** reduces planning overhead, aligning with AMOS [[07_SKILLS/amos-token-budget-governance/SKILL|token budget governance]]

### 3.3 Safe Self-Evolution
HarnessEvolve and Ouroboros establish complementary approaches to safe agent self-evolution:
- **Reference trajectory learning** prevents catastrophic forgetting — maps to AMOS [[19_TESTS/19_TESTS_README|test plane]] regression testing during evolution
- **Reviewed core evolution** ensures guardrails survive — maps to AMOS [[07_SKILLS/amos-operational-modes/SKILL|operational modes]] safety envelopes
- **Co-evolution** (FlowEvo) ensures workflow-skill coherence — maps to AMOS [[07_SKILLS/amos-evolution-loop/SKILL|evolution loop]] observe→integrate cycle

## 4. Cross-Domain Connections

| AMOS Domain | SOTA Connection | Mapping |
|-------------|----------------|---------|
| [[10_MEMORY/10_MEMORY_MOC|Memory]] | MAP-Graph, LatticeMind, AutoAgent | Provenance-aware, conflict-aware, elastic memory |
| [[07_SKILLS/amos-skill-dependency-graph/SKILL|Skill Dependency Graph]] | ToolAtlas, GSE | Tool/skill composition as graph structure |
| [[07_SKILLS/amos-autonomous-evolution/SKILL|Autonomous Evolution]] | HarnessEvolve, Ouroboros, FlowEvo | Safe self-evolution with regression prevention |
| [[07_SKILLS/amos-audit-trail/SKILL|Audit Trail]] | MAP-Graph | Provenance tracking for shared memory |
| [[07_SKILLS/amos-rollback-recovery/SKILL|Rollback Recovery]] | MAP-Graph, HarnessEvolve | Shared memory rollback + regression rollback |
| [[07_SKILLS/amos-token-budget-governance/SKILL|Token Budget]] | FlowEvo, AutoAgent | Token-efficient co-evolution + elastic compression |
| [[09_PROTOCOLS/ZK_MERKLE_GOSSIP_CONSENSUS_LEDGER|Consensus]] | MAP-Graph | Shared state consistency for multi-agent |

## 5. Open Questions & Gaps

1. **Memory conflict resolution at scale:** LatticeMind achieves 0.97 conflict accuracy, but performance under adversarial memory injection is not reported. AMOS [[18_SECURITY/18_SECURITY_README|security plane]] needs adversarial memory conflict evaluation.
2. **Cross-agent memory transfer:** No SOTA paper addresses how memory graphs transfer between independently developed agent systems. AMOS [[07_SKILLS/amos-transfer-learning/SKILL|transfer learning]] needs cross-agent memory transfer protocols.
3. **Evolution safety under unbounded self-modification:** Ouroboros's 161-day deployment is promising, but no formal proof of safety preservation under unbounded self-modification exists. AMOS treats this as UNKNOWN/GAP per [[01_CANON/01_CORE_LAWS/L10_FAILURE_RECOVERY|L10 failure recovery]].
4. **Co-evolution convergence guarantees:** FlowEvo demonstrates empirical convergence, but no formal convergence proof for workflow-skill co-evolution is provided. AMOS [[07_SKILLS/amos-convergence-detection/SKILL|convergence detection]] needs formal co-evolution convergence criteria.

## 6. References

- arXiv:2607.11126 — ToolAtlas: Tool-Side Memory Graph for Agent Tool Use
- arXiv:2603.09716 — AutoAgent: Self-Evolving Multi-Agent with Elastic Memory Compression
- arXiv:2608.10509 — MAP-Graph: Provenance-Aware Shared Memory for Multi-Agent Systems
- arXiv:2608.08236 — LatticeMind: Conflict-Aware Memory Primitive for Agent Memory
- arXiv:2609.00829 — HarnessEvolve: Reference Trajectory Learning for Agent Harness Evolution
- arXiv:2608.06153 — GSE: Globally Reusable Skills with Skill Relation Graph
- arXiv:2608.08311 — Ouroboros: A Self-Developing Frontier Coding Agent with Reviewed Core Evolution
- arXiv:2607.21596 — FlowEvo: Workflow-Skill Co-Evolution for Token-Efficient Agent Execution

---

## Cross-References

- [[22_RESEARCH/01_PAPERS/SOTA_AI_CODING_AGENTS_SELF_EVOLVING_HARNESSES_2026|SOTA AI Coding Agents & Self-Evolving Harnesses]] — Ouroboros overlap, harness evolution
- [[22_RESEARCH/01_PAPERS/SOTA_BCI_NEURAL_DECODING_FOUNDATION_MODELS_2026|SOTA BCI Neural Decoding & Foundation Models]] — memory encoding parallels
- [[22_RESEARCH/01_PAPERS/SOTA_LLM_INFERENCE_OPTIMIZATION_REASONING_2026|SOTA LLM Inference Optimization & Reasoning]] — token efficiency and reasoning parallels
- [[10_MEMORY/10_MEMORY_MOC|Memory Plane]] — provenance-aware, conflict-aware, elastic memory
- [[07_SKILLS/amos-autonomous-evolution/SKILL|Autonomous Evolution]] — safe self-evolution
- [[07_SKILLS/amos-skill-dependency-graph/SKILL|Skill Dependency Graph]] — tool/skill composition graphs
- [[22_RESEARCH/AMOS_FRONTIER_RESEARCH_BRIDGE_2026-09-04|Frontier Research Bridge]] — cross-domain synthesis

**arXiv bridge note:** All 8 papers are 2026 arXiv preprints (Mar–Sep 2026). Epistemic class is SOURCE_CLAIM for all entries — these are reported results from preprints that have not yet undergone full peer review. Confidence ceilings reflect this. Specific numerical results (pass@1 improvements, task success rates, F1 improvements, token ratios) should be treated as author-reported claims pending independent replication.

**MOC:** [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]] · [[22_RESEARCH/01_PAPERS/01_PAPERS_MOC|01_PAPERS_MOC]]
