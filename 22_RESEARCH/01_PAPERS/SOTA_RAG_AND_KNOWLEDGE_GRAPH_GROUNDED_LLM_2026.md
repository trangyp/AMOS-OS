---
title: "SOTA RAG and Knowledge-Graph-Grounded LLM 2026"
type: research_synthesis
epistemic_class: SOURCE_CLAIM
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance:
    - ArXiv corpus 2026 (2602–2609)
    - ACL/EMNLP/NAACL 2026 proceedings
    - public web corpus snapshot 2026-09-04
  scope: rag_knowledge_graph_grounded_llm_2026
  freshness: 2026-09-04
  falsifier: "Graph-RAG and evidence-calibration results validated on benchmarks — production-scale deployment reliability NOT ESTABLISHED"
tags:
  - amos-os
  - research
  - sota
  - rag
  - knowledge-graph
  - graphrag
  - evidence-calibration
  - hyperbolic-embeddings
---

# SOTA RAG and Knowledge-Graph-Grounded LLM 2026

**Date:** 2026-09-04
**Epistemic class:** SOURCE_CLAIM (ArXiv + ACL/EMNLP/NAACL 2026)
**Confidence ceiling:** 0.85

---

## Abstract

Retrieval-Augmented Generation (RAG) grounded in knowledge graphs has undergone a structural transformation in 2026. The field has moved beyond flat vector retrieval toward graph-structured, evidence-calibrated, and geometrically-aware systems. This synthesis covers five converging research fronts: (1) GraphRAG on consumer hardware — making graph-based RAG economically viable without cloud APIs; (2) RADAR and PRA-RAG — formal defenses against retrieval corruption and corpus poisoning; (3) evidence-force calibration — Dempster-Shafer-based uncertainty quantification that disentangles epistemic from aleatoric uncertainty in multi-source retrieval; (4) RAG-GNN integration — fusing graph neural network topology with retrieved literature for domain-specific reasoning; and (5) hyperbolic RAG — exploiting the exponential volume growth of hyperbolic space to preserve hierarchical structure that Euclidean embeddings destroy. Together, these advances address the core limitations of 2025-era RAG: hallucination under knowledge conflict, vulnerability to adversarial retrieval, loss of hierarchical semantics, and prohibitive cloud costs for graph construction.

---

## Key Findings (2026 Results)

### 1. GraphRAG on Consumer Hardware

**Noēsis** (arXiv:2608.15919) — A decoupled Graph-RAG architecture achieving 59.5 EM / 74.7 F1 on HotpotQA (1,000 questions), surpassing Microsoft GraphRAG by +27.8 EM while using a 35B on-premises model for graph construction rather than GPT-4o. Key innovations: (a) Bidirectional Graph Traversal with Graph-Feedback Context Resolver simulating human sequential reading with degrading memory; (b) AIMD Concurrency Controller adapted from TCP congestion control, achieving 23× speedup with zero OOM events; (c) Moēsis domain-aware selective quantization for MoE models achieving 6.3× prompt processing speedup on 12 GB consumer GPUs; (d) Mesh cross-KB semantic routing with sub-2 ms latency. Corpus ingestion: 13.4 MB in 1 min 6 s vs 25 min sequential.

**SmartRAG** (arXiv:2607.14661) — Fully on-device graph-based RAG for mobile devices. Four-module architecture (Perception, Memory, Focus, Thinking) with EvoNER continually learnable NER. MRGraph three-layer provenance-preserving KG. A quantized 1.7B-parameter backbone achieves multi-hop reasoning competitive with models up to 18× larger on commodity smartphones.

**Project Citadel** (Towards AI, May 2026) — Sovereign dual-engine GraphRAG on AMD Mini-PC (128 GB RAM, RTX 3090 eGPU). Neo4j + pgvector + Gemma4:31b. Eliminates cloud API costs for 70M+ token document ingestion pipelines.

### 2. RADAR: Defense Against Retrieval Corruption

**RADAR** (arXiv:2605.22041) — Models reliable context selection as a graph-based energy minimization problem solved exactly via Max-Flow Min-Cut. Bayesian memory node recursively updates belief state instead of archiving raw historical documents, balancing stability against attacks with adaptability to genuine knowledge shifts. Superior robustness on dynamic datasets with minimal storage overhead.

**PRA-RAG** (ACL 2026 Findings) — Provably Robust Aggregation providing theoretical robustness guarantees against poisoning attacks that manipulate retrieved texts. Addresses the gap where existing defenses lack formal guarantees and perform unreliably when the LLM has limited knowledge of the retrieved domain.

### 3. Evidence-Force Calibration

**ERA** (arXiv:2604.20854) — Evidence-based Reliability Alignment shifting confidence estimation from scalar probabilities to explicit evidence distributions. Models internal and external knowledge as independent belief masses via Dirichlet distribution. Uses Dempster-Shafer Theory to measure geometric discordance between information sources, disentangling epistemic from aleatoric uncertainty. Significantly outperforms baselines on the coverage-abstention trade-off.

**EvidentialRAG** (arXiv:2607.10491) — Converts retrieved chunks into probabilistic evidence via Dirichlet evidence vectors. Conflict-preserving Dempster-Shafer fusion transfers unresolved disagreement into epistemic uncertainty rather than normalizing it away. On CRAG ambiguous subset: hallucination decreases from 45.3% (Corrective RAG) to 34.8%; conflict resolution increases from 35.2% to 51.2%; ECE improves to 0.122.

**SURE-RAG** (arXiv:2605.03534) — Sufficiency and Uncertainty-Aware Evidence Verification. Treats evidence sufficiency as a set-level property. Four interpretable feature blocks (coverage, relation strength, uncertainty, retrieval). Calibrated SURE-RAG attains 0.9075 Macro-F1, well above GPT-4o judge (0.7284). At 30% coverage, risk falls 37% relative.

**NAACL** (arXiv:2601.11004) — Noise-Aware Confidence Calibration. Improves ECE scores by 10.9% in-domain and 8.0% out-of-domain by training models to assess passage- and group-level utility before answering.

### 4. RAG-GNN Integration

**RAG-GNN** (arXiv:2602.00586) — Integrates GNN representations with dynamically retrieved literature via contrastive learning for precision medicine. Information-theoretic decomposition: network topology contributes 77.3% of predictive information; retrieved documents provide 8.6% unique information. Only method achieving positive silhouette scores for functional clustering. Identified DDR1 as therapeutic target via retrieved synthetic lethality evidence with KRAS mutations.

**Quest-GNN** (arXiv:2510.11541v2) — Question-Adaptive Graph Neural Network for multi-hop retrieval. Intra/inter-level message passing guided by the question. Up to 33.8% improvement on high-hop questions.

**Deep GraphRAG** (arXiv:2601.11144) — Hierarchical global-to-local retrieval with three-stage process (inter-community filtering, community-level refinement, entity-level search). DW-GRPO reinforcement learning enables compact 1.5B models to approach 70B performance in knowledge integration.

### 5. Hyperbolic RAG

**HypRAG** (arXiv:2602.07739) — Hyperbolic dense retrieval in Lorentz model. HyTE-H (hybrid architecture) achieves up to 29% gains over Euclidean baselines in context relevance and answer relevance on RAGBench using substantially smaller models. Over 20% radial increase from general to specific concepts — a property absent in Euclidean embeddings.

**HyperbolicRAG** (arXiv:2511.18808) — Poincaré manifold embeddings aligning semantic similarity with hierarchical containment. Unsupervised contrastive regularization across abstraction levels. Mutual-ranking fusion exploiting cross-space agreement.

**HyRAG** (arXiv:2606.03307) — Hyperbolic RAG for Graph Foundation Models. Hyperbolic Knowledge Indexing retains tree-like hierarchies; Multi-granularity Retrieval provides global anchors and local nuances; Dual-path Fusion at feature and structural levels. Significant zero-shot improvements on graph benchmarks.

**HyperRAG** (ACL 2026) — Query-centric framework dynamically constructing hypergraphs in hyperbolic space, capturing both explicit entity-based links and implicit query-aware connections.

---

## Technical Details

The 2026 RAG stack converges on a layered architecture: (1) **ingestion** with adaptive concurrency (AIMD control), (2) **indexing** in hyperbolic or hierarchical graph space, (3) **retrieval** with query-adaptive routing between dense, graph, and hybrid strategies, (4) **evidence aggregation** via Dempster-Shafer fusion with conflict-preserving rules, (5) **defense** via Max-Flow Min-Cut context selection and Bayesian belief updating, and (6) **generation** with calibrated abstention.

The evidence-force paradigm (ERA, EvidentialRAG) represents a paradigm shift: rather than treating retrieved passages as deterministic context, each chunk is mapped to a Dirichlet evidence vector. Conflicts between sources are preserved as epistemic uncertainty rather than normalized away, enabling the generator to route to direct answering, conflict-aware answering, or abstention. This is directly applicable to AMOS's epistemic class system (SOURCE_CLAIM vs OBSERVATION vs DERIVED).

Hyperbolic embeddings address a fundamental geometric mismatch: natural language and knowledge graphs exhibit tree-structured hierarchies whose exponential volume growth matches hyperbolic space but not Euclidean space. The 20%+ radial separation between general and specific concepts in HypRAG demonstrates that hyperbolic geometry provides an inductive bias that Euclidean RAG fundamentally lacks.

---

## AMOS Integration

- **[[11_KNOWLEDGE/11_KNOWLEDGE_MOC|Knowledge Plane]]** — GraphRAG architectures (Noēsis, Deep GraphRAG) provide the retrieval backbone for AMOS's knowledge graph. The three-layer provenance-preserving MRGraph from SmartRAG maps directly to AMOS's RSCF provenance tracking (SOURCE_CLAIM → OBSERVATION → DERIVED). The [[11_KNOWLEDGE/SOTA_AGENTIC_RAG_KNOWLEDGE_GRAPHS_2026|Agentic RAG synthesis]] covers the agent-decision layer; this paper covers the geometric and evidential foundations.

- **[[06_AGENTS/06_AGENTS_MOC|Agents Plane]]** — RADAR's Bayesian memory node and Max-Flow Min-Cut context selection provide the defense mechanism for AMOS agents that retrieve from dynamic external sources. The belief-state updating (vs raw document archiving) aligns with AMOS's `amos-failure-memory` skill: retain compressed beliefs, not raw logs.

- **[[25_COGNITIVE_MATRIX/01_PRIMITIVES/L08_REPRESENTATION/L08_REPRESENTATION_MOC|L08 Representation]]** — Hyperbolic RAG (HypRAG, HyperbolicRAG, HyRAG) directly informs AMOS's representation layer. The finding that hyperbolic space preserves hierarchical structure that Euclidean embeddings destroy supports AMOS's existing [[22_RESEARCH/01_PAPERS/SOTA_HYPERBOLIC_KNOWLEDGE_EMBEDDINGS_POINCARE_LORENTZ_2026|hyperbolic knowledge embeddings]] research. The 20% radial separation between abstraction levels provides a measurable geometric signal for AMOS's cognitive matrix representation primitives.

- **[[25_COGNITIVE_MATRIX/01_PRIMITIVES/L09_INFERENCE/L09_INFERENCE_MOC|L09 Inference]]** — Evidence-force calibration (ERA, EvidentialRAG, SURE-RAG) provides the inference-time uncertainty quantification for AMOS's inference layer. The Dempster-Shafer fusion with conflict-preserving rules maps to AMOS's COMPETING epistemic class: when retrieved sources disagree, the system should preserve the conflict as epistemic uncertainty and route to abstention rather than forcing a single answer. SURE-RAG's three-way decision (SUPPORTED / REFUTED / INSUFFICIENT) maps to AMOS's SOURCE_CLAIM / DERIVED / UNKNOWN-GAP classification.

---

## Falsifiers

- `F-RAG-1`: Noēsis's +27.8 EM over GraphRAG is measured on HotpotQA only — multi-domain generalization of the bidirectional traversal + AIMD pipeline NOT ESTABLISHED.
- `F-RAG-2`: RADAR's Max-Flow Min-Cut defense is validated on a novel dynamic dataset — formal robustness guarantees against adaptive adversaries who observe the defense mechanism NOT ESTABLISHED.
- `F-RAG-3`: ERA and EvidentialRAG's Dempster-Shafer fusion assumes independent evidence sources — performance under correlated retrieval noise (e.g., multiple sources derived from the same upstream document) NOT ESTABLISHED.
- `F-RAG-4`: HypRAG's 29% gains are on RAGBench — transfer to domain-specific hierarchical knowledge (e.g., AMOS's 26-plane cognitive matrix) NOT ESTABLISHED.
- `F-RAG-5`: RAG-GNN's 77.3%/8.6% information decomposition is specific to cancer signaling networks — generalization to other domain topologies NOT ESTABLISHED.

---

## References

1. Noēsis: Bidirectional Graph-RAG with Adaptive Parallelism — arXiv:2608.15919 (2026)
2. SmartRAG: Native Graph-Based RAG for Mobile Device — arXiv:2607.14661 (2026)
3. RADAR: Defending RAG Dynamically against Retrieval Corruption — arXiv:2605.22041 (2026)
4. PRA-RAG: Provably Robust Aggregation in RAG — ACL 2026 Findings
5. ERA: Evidence-based Reliability Alignment for Honest RAG — arXiv:2604.20854 (2026)
6. EvidentialRAG: Quantifying Information Conflict via Evidential Deep Learning — arXiv:2607.10491 (2026)
7. SURE-RAG: Sufficiency and Uncertainty-Aware Evidence Verification — arXiv:2605.03534 (2026)
8. NAACL: Noise-Aware Confidence Calibration for Robust LLMs in RAG — arXiv:2601.11004 (2026)
9. RAG-GNN: Integrating Retrieved Knowledge with GNNs for Precision Medicine — arXiv:2602.00586 (2026)
10. Quest-GNN: Question-Adaptive Graph Learning for Multi-hop RAG — arXiv:2510.11541 (2026)
11. Deep GraphRAG: Hierarchical Retrieval and Adaptive Integration — arXiv:2601.11144 (2026)
12. HypRAG: Hyperbolic Dense Retrieval for RAG — arXiv:2602.07739 (2026)
13. HyperbolicRAG: Enhancing RAG with Hyperbolic Representations — arXiv:2511.18808 (2025)
14. HyRAG: Generalizing Graph Foundation Models via Hyperbolic RAG — arXiv:2606.03307 (2026)
15. HyperRAG: Query-Aware Knowledge Retrieval via Hyperbolic Structuring — ACL 2026
16. Entropic Claim Resolution: Uncertainty-Driven Evidence Selection for RAG — arXiv:2603.28444 (2026)

---

**Parent:** [[22_RESEARCH/01_PAPERS/01_PAPERS_MOC|Papers MOC]] · [[00_ROOT/00_ROOT_MOC|Root MOC]]
