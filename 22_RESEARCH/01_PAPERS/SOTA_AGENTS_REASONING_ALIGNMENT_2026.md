---
canon-group: research
canon-type: synthesis
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: arxiv_web_2026-09
conclusion_class: ACTIVE_RESEARCH_SYNTHESIS
epistemic_class: SOURCE_CLAIM
topic: SOTA AI Agents Reasoning Alignment 2026 Synthesis
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - research/sota
  - research/agents
  - research/reasoning
  - research/alignment
  - research/interpretability
created: 2026-09-05
---

# SOTA AI Agents, Reasoning, and Alignment — 2026 Synthesis

> **Epistemic boundary:** `ACTIVE_RESEARCH_SYNTHESIS` — All claims below are `SOURCE_CLAIM` from cited papers. None of these methods are implemented in AMOS. AMOS bindings are `DERIVED` implications, not deployment claims.

## 1. AI Agents — Benchmarks, Frameworks, and Long-Horizon Runtimes

### 1.1 OmniaBench — General Agent Benchmark Across Diverse Scenarios

**Source:** arXiv:2607.14989 (Jul 2026, Huawei Cloud Post-Training Team, PKU DCAI Team)

**Claim:** Existing agent benchmarks focus on limited scenarios, tool ecosystems, or interaction formats. OmniaBench derives application-oriented scenario knowledge from app stores, product documents, industry resources, web retrieval, and human refinement, forming a hierarchical taxonomy spanning ToC, ToB, and ToE with 90 level-1 and 354 level-2 domains. It introduces a ten-dimensional capability taxonomy and eight compositional atomic difficulty factors.

**Key results:**
- 1,431 tasks total, with a 644-task contamination-resistant subset
- Claude-Sonnet-5 achieves 58.54 Overall Pass@1; GPT-5.6-Sol achieves 57.14
- Persistent limitations in planning, constraint maintenance, and adaptive correction across frontier models

**AMOS binding (`DERIVED`):** The ten-dimensional capability taxonomy and atomic difficulty factors map to AMOS's `21_DOMAINS` capability decomposition. The persistent planning/constraint/correction failures validate AMOS's `03_CONTROL_PLANE` separation of `PLAN`, `EXECUTE`, and `AUDIT` as distinct governed stages. Relevant to `21_DOMAINS/01_DOMAIN_ARCHITECTURE` and `03_CONTROL_PLANE`.

### 1.2 AgencyBench — Long-Horizon Agents in 1M-Token Real-World Contexts

**Source:** ACL 2026 (aclanthology.org/2026.acl-long.337)

**Claim:** Existing benchmarks focus on single agentic capability and rely on human-in-the-loop feedback, creating a scalability bottleneck. AgencyBench evaluates 6 core agentic capabilities across 32 real-world scenarios comprising 138 tasks with specific queries, deliverables, and rubrics. Uses a user-simulation agent for iterative feedback and a Docker sandbox for visual/functional rubric-based assessment.

**Key results:**
- Average 90 tool calls, 1 million tokens, hours of execution time per scenario
- Closed-source models significantly outperform open-source (48.4% vs 32.1%)
- Significant disparities in resource efficiency, feedback-driven self-correction, and tool-use preferences

**AMOS binding (`DERIVED`):** The long-horizon, million-token, multi-tool-call scenario shape directly informs AMOS's `10_MEMORY` context-continuity and compaction contracts. The closed/open-source gap validates AMOS's `L16_HML` rigor lens — high-stakes long-horizon reasoning demands `H`-level validation. Relevant to `10_MEMORY` and `11_KNOWLEDGE/03_RSCF`.

### 1.3 OctoTools — Training-Free Multi-Agent Framework with Extensible Tools

**Source:** ACL 2026 (aclanthology.org/2026.acl-long.1)

**Claim:** Solving complex reasoning tasks involves visual understanding, domain knowledge retrieval, numerical calculation, and multi-step reasoning. OctoTools introduces standardized tool cards to encapsulate tool functionality, a planner for both high-level and low-level planning, and an executor to carry out tool usage. Training-free, user-friendly, and extensible.

**Key results:**
- 9.3% average accuracy gain over GPT-4o across 16 diverse tasks (MathVista, MMLU-Pro, MedQA, GAIA-Text)
- Outperforms AutoGen, GPT-Functions, and LangChain by up to 10.6% with the same tool set
- Robust with compact backbones and noisy tool environments

**AMOS binding (`DERIVED`):** The standardized tool-card pattern maps to AMOS's `09_PROTOCOLS` tool-binding contracts and `13_MODELS` capability declarations. The planner/executor separation mirrors AMOS's `03_CONTROL_PLANE` plan-execute split. Relevant to `09_PROTOCOLS` and `03_CONTROL_PLANE`.

### 1.4 LongHorizon-Harness — Manage-Execute-Audit Loop for Long-Horizon Tasks

**Source:** arXiv:2608.01964 (Aug 2026)

**Claim:** Existing agent harnesses maintain task execution, task state, and completion assessment within a growing context, making state difficult to track and allowing incorrect self-assessments to propagate. LongHorizon-Harness reformulates long-horizon execution as a task-state management problem: a manager maintains task state outside execution, a fresh-context executor performs subtasks, and a read-only auditor verifies environment state before the next round.

**Key results:**
- Qwen3.7-Plus: 51.8% → 80.7% on WeaveBench, 69.7% → 77.2% on Terminal-Bench 2.1, 2.8% → 8.3% on OSWorld 2.0
- Claude Opus 4.7: 20.0% → 34.3% on OSWorld 2.0 subset
- Consistent gains across models, harnesses, and interaction domains

**AMOS binding (`DERIVED`):** The Manage-Execute-Audit (MEA) loop is a near-direct instance of AMOS's runtime pipeline `PLAN → EXECUTE → OBSERVE → AUDIT`. The explicit externalization of task state and read-only auditor maps to AMOS's `K_SYSTEM_STATE` and `11_VALIDATION` contracts. The fresh-context executor validates AMOS's `10_MEMORY` context-compaction discipline. Highly relevant to `04_RUNTIME/06_EXECUTION` and `03_CONTROL_PLANE`.

### 1.5 Argus — Persistent Self-Evolving Agentic Reasoning Runtime

**Source:** arXiv:2608.05144 (Aug 2026)

**Claim:** Long-horizon reasoning requires an agentic runtime that persists when evidence supports its approach and pivots when measurements reveal failure. Argus separates stable user intent from operational objectives, constraints, and verification criteria. Manager, Planner, Engineer, and Reviewer execute bounded missions over durable project state. Memories, skills, procedures, verifiers, routing decisions, and rejected routes are admitted only after role-owned review and task-native verification. Model weights remain fixed; self-evolution occurs through persistent runtime state and control policy.

**Key results:**
- ~78% on SWE-Bench Pro vs 59% for Direct Copilot (1.41× aggregate tokens)
- Mature waves use 21% fewer solve-input tokens and 15% less active workflow time than startup waves
- 34 verifier recoveries and 22 strict review-loop rescues recorded
- 76.8% on AARRI-Bench

**AMOS binding (`DERIVED`):** Argus's role-owned admission (Manager/Planner/Engineer/Reviewer) maps to AMOS's `03_CONTROL_PLANE` role separation and `K_AUTHORITY` checks. The "weights fixed, self-evolution via runtime state" pattern validates AMOS's `MODEL != DEPLOYED_RUNTIME` boundary — the runtime evolves without retraining. The verification-gated admission of memories and skills maps to `K_MEMORY_ADMISSION` and `PROMOTION_GATES`. Highly relevant to `03_CONTROL_PLANE`, `10_MEMORY`, and `13_MODELS`.

## 2. Reasoning — Test-Time Compute, Self-Correction, and Error Localization

### 2.1 Breadth-Depth Refinement — Verifier-Free Test-Time Self-Correction

**Source:** arXiv:2608.05643 (Aug 2026)

**Claim:** Wider sampling alone suffers diminishing returns because new rollouts repeat existing answer patterns. Verifier-based selection depends on external reward model calibration. The proposed verifier-free breadth-depth framework samples multiple independent rollouts, refines each through iterative self-critique and self-correction, and aggregates by majority voting. Breadth preserves diverse initial attempts; depth repairs local reasoning errors before aggregation.

**Key results:**
- Consistently improves over greedy decoding, majority voting, verifier-based best-of-N, beam search, and lookahead decoding
- Qwen2.5-1.5B: MATH500 58.0%, AMC 25.0% → 32.5% over strongest verifier-based baseline
- Tested on AIME24, AIME25, AMC, OlympiadBench, MATH500

**AMOS binding (`DERIVED`):** The breadth-depth separation maps to AMOS's `K_MULTI_HYPOTHESIS` (breadth = maintain multiple hypotheses) and `K_CAUSAL_EPOCH` (depth = refine within a bounded epoch). The verifier-free design aligns with AMOS's preference for internal consistency checks over external oracle dependence. Relevant to `02_KERNEL/01_META_LOGIC` and `11_KNOWLEDGE/03_RSCF`.

### 2.2 SVR — Self-Verifying Refinement via Joint Verdict-Confidence RL

**Source:** arXiv:2607.28457 (Jul 2026)

**Claim:** Uniform test-time compute budgets waste computation on easy inputs; verifier-guided refinement relies on external feedback. SVR is an oracle-free multi-turn RL framework where the model produces a solution with a discrete correctness verdict and confidence score, retaining the answer only when verdict is Correct and confidence exceeds a threshold. Ground-truth correctness is used only for training rewards, never exposed to the policy at inference.

**Key results:**
- Qwen3.5-2B: 0.563 macro-average accuracy across 7 math benchmarks with only 2.99 inference turns average
- Exceeds standard GRPO, strong multi-turn baselines, and fixed-budget oracle-guided reference
- Adaptive stopping activated only at inference

**AMOS binding (`DERIVED`):** The joint verdict-confidence gating maps to AMOS's `K_EFFECT_CLASSIFICATION` (what kind of effect will this produce?) and `PROMOTION_GATES` (confidence threshold for commit). The adaptive stopping parallels AMOS's `L16_HML` — `L`-rigor for easy inputs, escalating to `H`-rigor only when confidence is low. Relevant to `02_KERNEL` and `13_MODELS/01_FOUNDATION`.

### 2.3 TTEL — Test-Time Scaling via Error Localization

**Source:** arXiv:2607.21453 (Jul 2026, Google)

**Claim:** Standard test-time scaling approaches (independent sampling, sequential refinement) operate without token-level credit assignment, discarding valid reasoning prefixes. TTEL performs token-level error localization by comparing conditional probabilities under informed feedback against a null-context baseline, isolating the step where an error occurred, truncating the trajectory, and branching a new generation that maximally reuses the valid prefix.

**Key results:**
- Strictly dominating Pareto frontiers on pass-at-k vs generated-token cost
- Qwen3-8B on LiveCodeBench: pass@64 of 71.0% with ~half the tokens of independent sampling (360.4k vs 735.0k)
- Outperforms baselines on AIME-2025 and HMMT-2025 across Qwen3-8B and Qwen3-4B-Thinking-2507

**AMOS binding (`DERIVED`):** Token-level error localization maps to AMOS's `K_BINDING` (dependency closure — which step caused the failure?) and `L10_FAILURE_RECOVERY` (recover from the minimal failing prefix, not the whole trajectory). The prefix-reuse pattern validates AMOS's `K_CAUSAL_EPOCH` — recover the valid epoch, branch from the failure point. Relevant to `02_KERNEL/03_CAUSAL` and `01_CANON/01_CORE_LAWS/L10_FAILURE_RECOVERY`.

### 2.4 Test-time Recursive Thinking (TRT) — Self-Improvement Without External Feedback

**Source:** arXiv:2602.03094 (Feb 2026)

**Claim:** LLMs can self-improve at test time without additional training by combining strategic exploration (diverse candidate generation conditioned on accumulated knowledge) with self-guided verification (ranking without ground truth). TRT generates multiple rollouts conditioned on rollout-specific strategies, ranks them via self-judgment, and synthesizes reusable insights by contrasting the best solution against alternatives.

**Key results:**
- Open-source models reach 100% accuracy on AIME-25/24
- Closed-source models improve by 10.4-14.8 percentage points on LiveCodeBench's hardest problems
- No external feedback required

**AMOS binding (`DERIVED`):** The "synthesize reusable insights by contrasting best vs alternatives" pattern maps to AMOS's `K_MULTI_HYPOTHESIS` resolution and `11_KNOWLEDGE` knowledge consolidation. The self-judgment ranking aligns with `K_MEMORY_RETRIEVAL` ranking contracts. Relevant to `02_KERNEL/01_META_LOGIC` and `11_KNOWLEDGE`.

### 2.5 EvoResearcher — Training-Free Inference-Time Self-Reflection with Cost-Bounded Early Stopping

**Source:** arXiv:2608.18884 (Aug 2026)

**Claim:** Training reasoning models via RL (GRPO) is expensive and commits to a full training pipeline. EvoResearcher is a training-free inference-time protocol adding cost-bounded self-reflection to a frozen LLM backbone. It iterates generate → self-critique → revise until a maximum depth is exhausted or the critique returns a CONFIRMED sentinel (implicit early stop). A self-reflective meta-reward (correctness, efficiency, reflection depth, tool-call diversity) acts as prompt-level design principles.

**Key results:**
- Validated on Big-Bench Hard (100 multi-step reasoning), GSM8K (500 arithmetic), MATH (500 competition)
- Cross-model replication on Qwen2.5-72B
- Zero gradient updates; pure-reasoning prompts

**AMOS binding (`DERIVED`):** The cost-bounded early-stop with CONFIRMED sentinel maps to AMOS's `L16_HML` budget-aware rigor and `K_EFFECT_CLASSIFICATION` commit-readiness checks. The four-component meta-reward (correctness, efficiency, depth, diversity) parallels AMOS's typed-tensor axes. Relevant to `02_KERNEL` and `13_MODELS`.

## 3. Alignment — Interpretability, Causal Dynamics, and Latent Reasoning Control

### 3.1 Causal-Dynamic Interpretability Framework for LLM Generation

**Source:** ACL 2026 (aclanthology.org/2026.acl-long.933)

**Claim:** Existing interpretability methods study internal and external perspectives in isolation, overlooking causality and temporal dynamics. The proposed framework characterizes backdoor-adjusted causal effects of both the generated prefix and the prompt on the current token using a Structural Causal Model. Introduces two metrics: contextual causal influence and question-answer causal influence, providing a unified causal view of internal consistency and external alignment.

**Key results:**
- Unifies internal consistency (mechanistic) and external alignment (instruction-following) under a single causal framework
- Captures how influences evolve during autoregressive generation

**AMOS binding (`DERIVED`):** The backdoor-adjusted causal effect on token generation maps to AMOS's `K_WORLD_MODEL` (what caused this prediction?) and `01_CANON/01_CORE_LAWS/L4_CAUSAL`. The unification of internal consistency and external alignment parallels AMOS's `CANON != KNOWLEDGE` boundary — canonical constraints and empirical evidence are distinct but causally linked. Relevant to `02_KERNEL/03_CAUSAL` and `01_CANON`.

### 3.2 Interpretability-Guided Intervention for Latent Reasoning

**Source:** ACL 2026 (aclanthology.org/2026.acl-long.1568)

**Claim:** Latent reasoning (multi-step inference in continuous hidden states) offers efficiency over explicit CoT but its opacity hinders reliability. This work uses structural, causal, and geometric probes to reveal that latent vectors encode compressed, faithful reasoning-step representations, with early vectors acting as critical causal hubs. It operationalizes these insights into training-free, decode-time interventions that impose geometric and semantic priors to refine latent reasoning.

**Key results:**
- Consistent reasoning accuracy improvements across multiple model scales and task domains
- No parameter updates required
- Early latent vectors identified as critical causal hubs

**AMOS binding (`DERIVED`):** The "early vectors as causal hubs" finding maps to AMOS's `L24_CAUSAL_EPOCH` — early epochs carry disproportionate causal weight. The decode-time intervention pattern (impose priors without retraining) validates AMOS's `MODEL != DEPLOYED_RUNTIME` boundary — runtime behavior can be steered without model modification. Relevant to `02_KERNEL/03_CAUSAL` and `04_RUNTIME`.

### 3.3 Mechanistic Tomography — Designed Measurement for Control-Oriented Interpretability

**Source:** arXiv:2608.19338 (Aug 2026)

**Claim:** Mechanistic interpretability seeks quantities models do not expose directly: represented states, component effects, interactions, and intervention responses. This work formulates the shared measurement problem as mechanistic tomography — the design and analysis of measurements for recovering internal mechanisms and intervention effects. Once an estimate guides an intervention, it acts as an observer.

**Key results:**
- On GPT-2-small IOI: reproduces conditional backup, identifies Name Mover–Negative Name Mover interaction as largest held-out predictive term
- On Qwen-2.5-7B: calibrated additive map reaches held-out R²=0.983 on a finite refusal-response surface
- Pairwise lifting recovers interactions that first-order maps miss; procedure stops at simpler family when held-out error permits

**AMOS binding (`DERIVED`):** The "estimate guides intervention, which acts as observer" pattern maps to AMOS's `04_RUNTIME` observe → repair → audit loop and `K_EFFECT_CLASSIFICATION`. The "stop at simpler family when error permits" principle aligns with AMOS's `L16_HML` — use the minimum sufficient rigor. Relevant to `02_KERNEL` and `04_RUNTIME`.

### 3.4 Tensor Product Representations as Unifying Interpretability Hypothesis

**Source:** arXiv:2608.29034 (Aug 2026)

**Claim:** Different interpretability methods stand in relative isolation. This work proposes Tensor Product Representations (TPRs) as a unifying hypothesis: compositional structure represented as filler-role bindings in vector space. Mathematically and empirically, TPRs unify additive analogies, linear probing, sparse autoencoders, and activation patching — all derivable from TPRs.

**Key results:**
- Mathematical derivation showing all four methods derive from TPRs
- Empirical construction of each method's TPR variant on toy models through LLMs
- TPR-constructed variants perform comparably to standard variants

**AMOS binding (`DERIVED`):** The filler-role binding structure maps to AMOS's `K_BINDING` (typed dependencies between objects) and the typed-tensor architecture (`13_MODELS`). The unification of disparate methods under one structural hypothesis parallels AMOS's `L0_INTEGRITY` — a single consistent structural substrate. Relevant to `02_KERNEL/01_META_LOGIC` and `13_MODELS`.

### 3.5 Temporal Preference Concepts in LLMs — Causal Localization and Steering

**Source:** arXiv:2606.05194 (Jun 2026)

**Claim:** LLMs increasingly make decisions trading off near-term gains against long-term consequences, yet little is known about how they internally represent these tradeoffs. This work causally localizes a temporal-preference subgraph in Qwen3-4B-Instruct-2507 using gradient-based attribution and activation patching. The geometry of time horizon is encoded in the residual stream. Unintervened LLMs discount the future several times less steeply than humans, but this preference is unstable across contexts, motivating explicit control rather than implicit reliance on training. Steering vectors can shift temporal preference.

**Key results:**
- Mid-to-upper-layer nodes identified as temporal-preference locus via converging gradient attribution and activation patching
- Time-horizon geometry encoded in residual stream at localized layers
- LLMs discount future less steeply than humans; preference unstable across contexts
- Steering vectors can shift temporal preference

**AMOS binding (`DERIVED`):** The causal localization of temporal preference maps to AMOS's `K_COUNTERFACTUAL` (what would change if this circuit were different?) and `L5_SCOPE_REGIME` (temporal scope laws). The "unstable across contexts, motivating explicit control" finding validates AMOS's `CAPABILITY != AUTHORITY` boundary — having a temporal preference is not the same as governed temporal reasoning. The steering-vector control maps to `03_CONTROL_PLANE` policy enforcement. Highly relevant to `01_CANON/01_CORE_LAWS/L5_SCOPE_REGIME`, `02_KERNEL/03_CAUSAL`, and `03_CONTROL_PLANE`.

## 4. Cross-Cutting Synthesis — Implications for AMOS Architecture

### 4.1 The Manage-Execute-Audit Pattern Is Convergent

LongHorizon-Harness (MEA loop), Argus (Manager/Planner/Engineer/Reviewer), and OctoTools (planner/executor) all converge on separating planning, execution, and verification into distinct governed roles. This independently validates AMOS's `03_CONTROL_PLANE` architecture and the runtime pipeline `PLAN → EXECUTE → OBSERVE → AUDIT`. The empirical gains (e.g., Qwen3.7-Plus 51.8% → 80.7% on WeaveBench) are substantial.

**Epistemic status:** `DERIVED` — the convergence is observational, not a proof that AMOS's specific implementation is correct.

### 4.2 Test-Time Compute Maps to H/M/L Rigor Allocation

SVR's adaptive stopping (easy inputs get fewer turns), EvoResearcher's cost-bounded early stop, and Mechanistic Tomography's "stop at simpler family when error permits" all instantiate the same principle: allocate rigor proportional to need. This is the empirical analog of AMOS's `L16_HML` three-speed lens.

**Epistemic status:** `DERIVED` — the mapping is architectural, not validated on AMOS runtime.

### 4.3 Error Localization Validates Causal-Epoch Recovery

TTEL's token-level error localization and prefix-reuse, and Argus's verification-gated admission, both validate AMOS's `K_CAUSAL_EPOCH` and `L10_FAILURE_RECOVERY` — recover from the minimal failing unit, not the whole trajectory. The token-level credit assignment in TTEL is the fine-grained version of AMOS's bounded-epoch recovery.

**Epistemic status:** `DERIVED` — the principle is shared; AMOS's implementation status remains `PARTIAL`.

### 4.4 Interpretability-Guided Control Validates Model ≠ Runtime Boundary

The latent-reasoning interventions (decode-time priors, no retraining), Mechanistic Tomography's intervention-as-observer, and temporal-preference steering vectors all demonstrate that runtime behavior can be steered without modifying model weights. This is direct empirical support for AMOS's `MODEL != DEPLOYED_RUNTIME` and `CAPABILITY != AUTHORITY` boundaries.

**Epistemic status:** `DERIVED` — the boundary is empirically supported; AMOS's specific control-plane enforcement remains `PROPOSED_SPECIFICATION`.

### 4.5 Persistent Gaps in Frontier Agent Capability

OmniaBench (frontier models at ~58% Pass@1) and AgencyBench (48.4% closed-source) show that even the strongest 2026 models fail on ~40-50% of general agent tasks, with persistent weaknesses in planning, constraint maintenance, and adaptive correction. This validates AMOS's decision to treat agent capability as `CAPABILITY != AUTHORITY` — capability at a benchmark does not authorize autonomous deployment.

**Epistemic status:** `SOURCE_CLAIM` — benchmark numbers are directly cited; the AMOS implication is `DERIVED`.

## 5. Provenance and Status

- All paper claims are `SOURCE_CLAIM` with arXiv/ACL provenance as cited.
- All AMOS bindings are `DERIVED` — architectural implications drawn from the research, not deployment claims.
- No claim is made that AMOS implements, enforces, or deploys any of these methods.
- No claim is made that the cited methods are validated on AMOS runtime.
- `LATEST != AUTHORITATIVE` — these are recent papers; recency does not establish canonical status.
- `DOCUMENTED != IMPLEMENTED` — documenting these methods in the vault does not implement them in AMOS.
- `MODEL != DEPLOYED_RUNTIME` — the architectural mappings are models of how AMOS *could* relate to this research, not descriptions of deployed behavior.

## 6. Cross-Links

- `22_RESEARCH/01_PAPERS/SOTA_VLA_QUANTUM_BCI_2026.md` — companion synthesis (VLA, quantum, BCI)
- `03_CONTROL_PLANE` — plan/execute/audit governance
- `04_RUNTIME/06_EXECUTION` — runtime pipeline
- `02_KERNEL/01_META_LOGIC` — reasoning kernel
- `02_KERNEL/03_CAUSAL` — causal contracts
- `02_KERNEL/06_RISK_REPAIR` — failure recovery
- `10_MEMORY` — context continuity, compaction, admission
- `11_KNOWLEDGE/03_RSCF` — epistemic classification
- `13_MODELS/01_FOUNDATION` — model foundation
- `21_DOMAINS/01_DOMAIN_ARCHITECTURE` — domain decomposition
- `01_CANON/01_CORE_LAWS/L4_CAUSAL` — causal laws
- `01_CANON/01_CORE_LAWS/L5_SCOPE_REGIME` — scope and temporal laws
- `01_CANON/01_CORE_LAWS/L10_FAILURE_RECOVERY` — failure recovery laws
- `01_CANON/01_CORE_LAWS/L16_HML` — H/M/L rigor lens
- `01_CANON/01_CORE_LAWS/L24_CAUSAL_EPOCH` — causal epoch law
