---
title: "SOTA Federated Learning and Privacy-Preserving AI 2026"
type: research_synthesis
plane: 22_RESEARCH
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
status: ACTIVE_SYNTHESIS
updated: 2026-09-04
epistemic_class: SOURCE_CLAIM
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: SOURCE_CLAIM
  provenance:
    - public web corpus snapshot 2026-09-04
    - ArXiv corpus 2026 (2604.07125)
    - IACR ePrint 2026 (2026/1376, 2026/324)
    - MLSys 2026, Nature Scientific Reports 2026
  scope: state_of_the_art_research_2026
tags:
  - amos-os
  - research
  - sota
  - federated-learning
  - differential-privacy
  - secure-aggregation
  - privacy-preserving
  - homomorphic-encryption
  - models
---

# SOTA Federated Learning and Privacy-Preserving AI 2026

**Origin Architect / Steward:** Trang Phan
**AMOS_CORE Target:** `v4.4`
**Epistemic Class:** `SOURCE_CLAIM`
**Freshness:** `2026-09-04`

---

## Abstract

Federated learning (FL) and privacy-preserving AI have converged in 2026 on a unified architecture combining adaptive differential privacy (DP), secure aggregation (SA), and homomorphic encryption (HE). The central challenge — balancing privacy guarantees against model utility and communication efficiency — has been addressed by several breakthrough frameworks. HEAD-FL (IACR 2026/1376) integrates round-adaptive Gaussian perturbation under Rényi DP with verifiable homomorphic aggregation, achieving superior privacy-utility tradeoffs via FedAvg. DDP-SA (arXiv 2604.07125) combines client-side local DP with full-threshold additive secret sharing for scalable end-to-end protection. AdaDP-FedSec (Nature Scientific Reports 2026) demonstrates adaptive privacy budget allocation recovering ~75% of the performance gap between DP-FL and centralized training while pushing membership inference attack success to chance levels. FLiPD (IACR 2026/324) optimizes SA protocols with distributed DP noise generation secure against majority client collusion. DisAgg (MLSys 2026) introduces distributed aggregator committees to eliminate expensive cryptographic operations. These advances are directly relevant to AMOS's distributed agent architecture, `03_CONTROL_PLANE` governance, and the enforcement trust contract (v43) supply-chain provenance requirements.

---

## Key Findings

| Paper | Source | Key Finding | AMOS Binding |
| :--- | :--- | :--- | :--- |
| HEAD-FL: Adaptive DP + Verifiable Homomorphic Aggregation | IACR ePrint 2026/1376 | Round-adaptive Gaussian perturbation under RDP framework; tight cumulative privacy accounting with (ε,δ)-DP conversion; FedAvg reduces communication overhead; robust to client dropouts | `03_CONTROL_PLANE` — adaptive privacy for federated governance |
| DDP-SA: Distributed DP + Secure Aggregation | arXiv 2604.07125 | Two-stage protection: Laplace noise perturbation + additive secret sharing; no single server reveals individual updates; scales linearly with participants; higher accuracy than standalone LDP | `04_RUNTIME` — scalable privacy for distributed runtime |
| AdaDP-FedSec: Adaptive DP-FL with Secure Aggregation | Nature Sci. Reports 2026 | Adaptive privacy budget based on gradient variance; Shamir SS + Paillier HE hybrid; contribution-aware weighted aggregation; recovers ~75% of centralized performance gap; MIA success near chance | `13_MODELS` — privacy-preserving multi-institutional model training |
| FLiPD: MPC + DP for Federated Learning | IACR ePrint 2026/324 | Distributed DP noise generation secure against majority client collusion; client-server comm cost same as unprotected FL; server-server comm 11% lower than Prio+; 87% accuracy on HAR, 90% on MNIST | `03_CONTROL_PLANE` — collusion-resistant aggregation |
| DisAgg: Distributed Aggregators for Efficient SA | MLSys 2026 | Client committee performs aggregation via secret sharing; eliminates local masking and expensive public-key ops; handles client dropouts natively; reduces cryptographic overhead | `04_RUNTIME` — efficient secure aggregation protocol |

---

## Technical Details

### Adaptive Differential Privacy

HEAD-FL (IACR 2026/1376) introduces a **round-adaptive Gaussian perturbation mechanism** analyzed under the Rényi Differential Privacy (RDP) framework. Unlike fixed-noise approaches that apply the same noise level throughout training, HEAD-FL dynamically adjusts noise based on the training round and gradient sensitivity. RDP enables tighter cumulative privacy accounting than standard (ε,δ)-DP composition, as it tracks the Rényi divergence across rounds and converts to (ε,δ)-DP at the end. This adaptive approach achieves improved privacy-utility tradeoffs because early rounds (where gradients carry more signal) can use less noise, while later rounds (where gradients are noisier and less informative) can afford more privacy noise without significant utility loss.

AdaDP-FedSec (Nature 2026) takes a complementary approach: the adaptive privacy budget allocation dynamically calibrates DP noise based on **gradient variance and institutional data characteristics**. The adaptive budgeting mechanism yields 3–5% point improvements over uniform noise allocation at matched total privacy expenditure, emerging as the most impactful component. The framework also incorporates a **contribution-aware weighted aggregation** scheme and dual-layer personalized model architecture to address cross-institutional data heterogeneity (non-IID data).

### Secure Aggregation Protocols

**DDP-SA** (arXiv 2604.07125) introduces a two-stage protection mechanism: (1) clients perturb local gradients with calibrated Laplace noise (local DP), then (2) decompose noisy gradients into additive secret shares distributed across multiple intermediate servers. This design ensures no single compromised server or channel can reveal individual client updates, and the parameter server reconstructs only the aggregated noisy gradient. The framework scales linearly with participant count.

**FLiPD** (IACR 2026/324) addresses a critical gap: most SA protocols assume an honest-but-curious server but do not protect against **client collusion with the server**. FLiPD uses distributed DP noise generation where noise is shared across clients, making the protocol secure even when the majority of clients collude with the server. Crucially, client-server communication cost is essentially the same as in unprotected FL (plaintext updates), and server-server communication is 11% lower than Prio+ (the prior SOTA).

**DisAgg** (MLSys 2026) rethinks the aggregation architecture itself: instead of a single central server, a small **committee of clients called Aggregators** performs the aggregation. Each client secret-shares its update vector to Aggregators, which locally compute partial sums and return only aggregated shares for server-side reconstruction. This eliminates local masking and expensive public-key operations while handling client dropouts natively.

### Privacy-Utility Tradeoff Landscape

The 2026 SOTA reveals a converging picture: adaptive DP noise allocation (HEAD-FL, AdaDP-FedSec) consistently outperforms fixed noise by 3–5% accuracy points at matched privacy budgets. Hybrid approaches combining LDP + MPC (DDP-SA) or DP + HE (HEAD-FL, AdaDP-FedSec) provide stronger end-to-end guarantees than either technique alone. The membership inference attack (MIA) success rate can be pushed to near-chance levels (AdaDP-FedSec) while recovering approximately 75% of the performance gap to centralized training — a practical but not complete solution.

---

## AMOS Integration

- **`03_CONTROL_PLANE`**: Federated learning is the natural training paradigm for AMOS's distributed agent swarm. HEAD-FL's round-adaptive DP and FLiPD's collusion resistance directly inform the `03_CONTROL_PLANE` contract for how agent updates are aggregated without revealing individual agent behavior. The enforcement trust contract (v43) requires supply-chain provenance — FLiPD's distributed DP noise generation provides a mechanism for privacy-preserving provenance attestation.

- **`04_RUNTIME`**: DisAgg's distributed aggregator committees map onto AMOS's runtime architecture where a subset of agents can serve as aggregators for model updates. DDP-SA's linear scaling with participants is critical for AMOS's 696-agent ecosystem. The `amos-high-throughput-arrow-ipc-state-bus` skill provides the IPC substrate for secret sharing across agents.

- **`13_MODELS`**: AdaDP-FedSec's adaptive privacy budget allocation and contribution-aware weighted aggregation address the non-IID challenge that AMOS faces when agents operate in diverse environments. The dual-layer personalized model architecture allows AMOS to maintain both a global shared model and per-agent personalized models.

- **`19_TESTS`**: The MIA success rate metric (pushed to near-chance by AdaDP-FedSec) should be adopted as a standard test in AMOS's `19_TESTS` contract for any privacy-preserving model deployment. The `amos-validation-pipeline` should include privacy attack resistance as a validation stage.

- [[22_RESEARCH/01_PAPERS/SOTA_HOMOMORPHIC_ENCRYPTION_AND_VERIFIABLE_COMPUTATION_FOR_DECENTRALIZED_AGENTS_2026|SOTA Homomorphic Encryption]] — HE and verifiable computation for agents
- [[22_RESEARCH/01_PAPERS/SOTA_BFT_SMR_DISTRIBUTED_CONSENSUS_FOR_AGENTIC_SWARMS_2026|SOTA BFT SMR Consensus]] — distributed consensus for agent swarms
- [[22_RESEARCH/01_PAPERS/SOTA_MULTI_AGENT_FRAMEWORKS_2026|SOTA Multi-Agent Frameworks]] — multi-agent system architectures
- [[22_RESEARCH/01_PAPERS/SOTA_AGENTIC_AI_SAFETY_AND_ALIGNMENT_2026|SOTA Agentic AI Safety]] — safety for agentic systems

---

## Falsifiers

- `F-2026-09-04-FL-1`: If HEAD-FL's round-adaptive DP does not maintain privacy guarantees under adaptive attacks (not just static MIA), AMOS must fall back to fixed-noise DP with conservative budgets for all federated training.
- `F-2026-09-04-FL-2`: If DDP-SA's linear scaling breaks down at >10,000 participants (AMOS's agent count could exceed this), AMOS must shard the aggregation hierarchy.
- `F-2026-09-04-FL-3`: If AdaDP-FedSec's 75% performance recovery does not hold for LLM-scale models (tested only on NLP classification), AMOS must restrict federated training to smaller task-specific models and keep LLM training centralized.
- `F-2026-09-04-FL-4`: If DisAgg's aggregator committee is vulnerable to targeted committee corruption (not random failure), AMOS must use Byzantine-resistant committee selection, linking to the BFT consensus SOTA.

---

## References

1. HEAD-FL: Secure and Efficient FL with Adaptive DP and Verifiable Homomorphic Aggregation — IACR ePrint 2026/1376 — https://eprint.iacr.org/2026/1376
2. DDP-SA: Scalable Privacy-Preserving FL via Distributed DP and Secure Aggregation — arXiv 2604.07125 — https://arxiv.org/pdf/2604.07125
3. AdaDP-FedSec: Adaptive DP-FL with Secure Aggregation — Nature Scientific Reports 2026 — https://www.nature.com/articles/s41598-026-63985-z
4. FLiPD: Privacy-Preserving FL via MPC and DP — IACR ePrint 2026/324 — https://eprint.iacr.org/2026/324.pdf
5. DisAgg: Distributed Aggregators for Efficient Secure Aggregation — MLSys 2026 — https://proceedings.mlsys.org/paper_files/paper/2026/file/5c40a52354e95a6fc701a84cdcd97bc8-Paper-Conference.pdf

---

## Navigation

- [[22_RESEARCH/01_PAPERS/01_PAPERS_MOC|Papers MOC]]
- [[00_ROOT/00_ROOT_MOC|Root MOC]]
