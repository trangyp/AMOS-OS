---
title: "SOTA Causal Reasoning and Foundation Models 2026"
type: research_synthesis
source: 22_RESEARCH
domain: C10_TECH_ENGINEERING
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_RESEARCH_SYNTHESIS
conclusion_class: DERIVED
research_epoch: 2026-09-30
freshness_policy: REVALIDATE_FOR_CURRENT_SOTA
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance:
    - arxiv_2609_03003_causal_foundation_models
    - eacl_2026_doverifier_symbolic_causal_verification
    - acl_2026_findings_causalgym_post_training
    - arxiv_2602_14972_cfms_partial_graphs
    - acl_2026_findings_causal_audit_graph_reasoning
    - arxiv_2605_09079_causim_scaling_causal_simulators
  scope: causal_reasoning_foundation_models_2026
tags:
  - causal
  - foundation-models
  - rscf
  - sota
---

# SOTA Causal Reasoning and Foundation Models 2026

> [!ABSTRACT] Research Synthesis
> Synthesizes the 2026 state of the art in causal reasoning with foundation models: causal foundation models (CFMs) that estimate causal quantities via in-context learning, symbolic verification of LLM-generated causal expressions, post-training methods for causal benchmarks, partial-graph conditioning, auditable graph-based causal chains, and scaling causal simulators. Maps to AMOS L4_CAUSAL, causal-reasoning-master, and scientific-closure-governor.

---

## 1. Overview

The 2026 causal reasoning landscape has undergone a paradigm shift. Causal inference, long the domain of bespoke statistical pipelines requiring per-dataset model specification, identification assumptions, and manual estimator selection, is being absorbed into the foundation model paradigm. Six converging research threads define the current frontier:

1. **Causal Foundation Models (CFMs)** — pretrained networks that estimate causal quantities (e.g., ATE) on entirely new datasets via in-context learning, without any model updates.
2. **Symbolic verification** of LLM-generated causal expressions against ground-truth causal graphs using do-calculus and probability theory.
3. **Post-training recipes** (SFT, DPO, KTO, PPO, GRPO) that produce causal-specialized models dramatically outperforming frontier generalists on causal benchmarks.
4. **Partial-graph conditioning** methods that allow CFMs to incorporate partial causal knowledge, with learnable attention biases emerging as the most effective mechanism.
5. **Auditable graph-based reasoning** with explicit, modular causal chain construction and path-level evidence aggregation.
6. **Causal simulator scaling** — training causal reasoning on increasingly complex synthetic causal environments.

**AMOS Alignment**: AMOS L4_CAUSAL and the causal-reasoning-master skill anticipated the need for epistemically grounded causal inference. The RSCF framework's distinction between SOURCE_CLAIM, DERIVED, and UNKNOWN/GAP maps directly onto the verification and auditability requirements emerging in this literature.

---

## 2. Key Papers

### 2.1 Causal Foundation Models (CFMs)

**Source**: arXiv:2609.03003 (September 2026)

> [SOURCE_CLAIM] Pretrained neural networks can estimate causal quantities — including the Average Treatment Effect (ATE) — on entirely new datasets using in-context learning alone, without any gradient updates or model fine-tuning.

This work represents the most significant paradigm shift in the batch. The core contribution:

- **In-context causal estimation**: A CFM receives a dataset (covariates, treatment, outcome) as context and outputs causal effect estimates directly. No per-dataset model fitting.
- **Foundation model transfer**: The causal inference workflow — traditionally requiring identification strategy selection, propensity modeling, estimator choice, and sensitivity analysis — is collapsed into a single forward pass through a pretrained model.
- **Generalization across domains**: CFMs trained on diverse synthetic and semi-synthetic causal datasets generalize to held-out domains with different structural causal models.

**Epistemic status**: `[SOURCE_CLAIM]` — the claim that in-context causal estimation matches or exceeds bespoke pipelines is asserted by the authors. Independent replication on real-world observational datasets with ground-truth causal effects is `UNKNOWN/GAP`.

**Falsifier**: If CFM estimates on real-world observational data (where ground truth is available, e.g., randomized trial validation) systematically diverge from bespoke doubly-robust estimators by more than the estimators' own variance, the foundation model paradigm for causal inference is not established for practical deployment.

**Provenance**: `arxiv_2609_03003_causal_foundation_models` — single preprint, September 2026. No peer-reviewed replication at synthesis time.

---

### 2.2 DOVERIFIER: Symbolic Verification of LLM Causal Expressions

**Source**: EACL 2026

> [SOURCE_CLAIM] A symbolic verifier can check whether LLM-generated causal expressions (e.g., interventional distributions, counterfactual queries) are derivable from a given causal graph using do-calculus and probability theory, recovering correct answers that string-matching evaluators mark as incorrect.

Key contributions:

- **Symbolic grounding**: Rather than evaluating LLM causal output by string comparison against a gold answer, DOVERIFIER parses the LLM's causal expression and formally verifies derivability from the supplied causal graph.
- **Do-calculus engine**: Implements Pearl's three rules of do-calculus as a symbolic derivation system, checking whether the LLM's proposed expression follows from the graph's structure.
- **Recovery of correct answers**: A significant fraction of LLM outputs marked incorrect by string matching are actually causally equivalent expressions — DOVERIFIER recovers these, raising measured accuracy substantially.

**Epistemic status**: `[SOURCE_CLAIM]` — peer-reviewed (EACL 2026). The recovery claim is well-grounded. The broader claim that symbolic verification improves causal evaluation validity is `DERIVED` from the recovery evidence.

**Falsifier**: If DOVERIFIER's do-calculus engine cannot handle graphs with latent variables or cyclic causal structures common in real-world domains, its verification coverage is bounded and the recovery gains do not generalize.

**Provenance**: `eacl_2026_doverifier_symbolic_causal_verification` — peer-reviewed conference paper.

---

### 2.3 CausalGym + Post-Training: Specialized Causal Models

**Source**: ACL 2026 Findings

> [SOURCE_CLAIM] A 14B-parameter model, post-trained with causal-specific objectives, achieves 93.5% on the CaLM benchmark — versus 55.4% by OpenAI o3 — demonstrating that targeted post-training dramatically outperforms scale alone for causal reasoning.

Post-training methods evaluated:

| Method | Type | CaLM Performance | Notes |
| :--- | :--- | :--- | :--- |
| **SFT** | Supervised fine-tuning | Baseline post-training | Causal examples as supervision |
| **DPO** | Preference optimization | Strong gains | Pairwise causal correctness preferences |
| **KTO** | Kahneman-Tversky optimization | Competitive | Unpaired preference signal |
| **PPO** | RL with reward model | Strong | Causal correctness as reward |
| **GRPO** | Group-relative policy optimization | Best reported | Group-based advantage estimation |

Key findings:

- **Post-training > scale**: The 14B post-trained model (93.5%) vastly outperforms the much larger o3 (55.4%) on causal reasoning, inverting the usual scaling relationship.
- **Generalization under distribution shift**: The post-trained models show strong generalization to causal reasoning tasks drawn from different distributions than training.
- **GRPO superiority**: Group-relative policy optimization emerges as the most effective post-training method, suggesting that relative causal correctness signals are more informative than absolute ones.

**Epistemic status**: `[SOURCE_CLAIM]` — peer-reviewed (ACL 2026 Findings). The 93.5% vs 55.4% comparison is a specific benchmark result. Generalization to non-CaLM causal tasks is `UNKNOWN/GAP`.

**Falsifier**: If CaLM benchmark tasks are systematically simpler than real-world causal reasoning (e.g., lack confounding, selection bias, or measurement error), the 93.5% figure overstates practical causal competence. If o3's 55.4% reflects CaLM format mismatch rather than causal reasoning deficit, the gap is an artifact.

**Provenance**: `acl_2026_findings_causalgym_post_training` — peer-reviewed findings paper.

---

### 2.4 CFMs with Partial Graphs

**Source**: arXiv:2602.14972

> [SOURCE_CLAIM] Causal Foundation Models can be conditioned on partial causal information (incomplete graphs), and learnable biases in the attention mechanism constitute the most effective conditioning method, allowing a general-purpose CFM to match specialized graph-conditioned models.

Conditioning methods evaluated:

1. **Prompt-based conditioning** — encoding partial graph structure in the input prompt
2. **Adapter-based conditioning** — lightweight parameter-efficient adapters for graph information
3. **Learnable attention biases** — injecting graph structure as additive biases into the attention computation

Key findings:

- **Attention biases dominate**: Learnable attention biases that encode causal graph structure (e.g., masking attention from effect to non-parent causes) are the most effective conditioning mechanism.
- **General-purpose matches specialized**: A single general-purpose CFM with attention-bias conditioning matches the performance of models specialized to specific graph structures.
- **Graceful degradation with partial information**: Performance degrades gracefully as the provided graph becomes more incomplete, rather than collapsing.

**Epistemic status**: `[SOURCE_CLAIM]` — preprint. The attention-bias superiority claim is `DERIVED` from controlled comparison. Whether this holds for graphs with >100 nodes is `UNKNOWN/GAP`.

**Falsifier**: If attention biases encode graph structure in a way that is brittle to graph perturbations (small structural changes cause large performance drops), the method is not robust for real-world use where causal graphs are approximate.

**Provenance**: `arxiv_2602_14972_cfms_partial_graphs` — single preprint, February 2026.

---

### 2.5 Causal-Audit: Auditable Graph-Based Reasoning

**Source**: ACL 2026 Findings

> [SOURCE_CLAIM] An explicit, auditable graph-based reasoning framework using target-aware causal chain construction with four modular stages and path-level causal evidence aggregation produces more reliable and transparent causal reasoning than end-to-end LLM approaches.

Four modular stages:

1. **Target identification** — identifying the causal query target and relevant variables
2. **Causal chain construction** — building explicit causal paths from cause to effect
3. **Evidence aggregation** — aggregating causal evidence across paths
4. **Conclusion derivation** — deriving the causal conclusion from aggregated evidence

Key contributions:

- **Auditability**: Each stage produces an explicit artifact (identified targets, constructed chains, aggregated evidence) that can be inspected, challenged, and verified.
- **Path-level granularity**: Rather than a single end-to-end causal judgment, the framework decomposes reasoning into individual causal paths, each with its own evidence weight.
- **Target-awareness**: The causal chain construction is conditioned on the specific query target, avoiding irrelevant causal path exploration.

**Epistemic status**: `[SOURCE_CLAIM]` — peer-reviewed (ACL 2026 Findings). The auditability claim is structurally verifiable. The reliability improvement claim is `DERIVED` from benchmark comparisons.

**Falsifier**: If the four-stage decomposition introduces error accumulation (errors in early stages propagate and amplify through later stages without correction), the modular approach may be less reliable than end-to-end methods for complex causal queries.

**Provenance**: `acl_2026_findings_causal_audit_graph_reasoning` — peer-reviewed findings paper.

---

### 2.6 CauSim: Scaling Causal Simulators

**Source**: arXiv:2605.09079

> [SOURCE_CLAIM] Causal reasoning can be scaled by training on increasingly complex causal simulators, where simulator complexity (number of variables, graph depth, confounding structure) is progressively increased during training.

Key contributions:

- **Curriculum via simulator complexity**: Rather than a fixed training distribution, CauSim defines a curriculum where causal simulator complexity increases over training.
- **Complexity dimensions**: Number of variables, causal graph depth, confounding density, intervention cardinality, and noise distribution complexity.
- **Scaling law for causal reasoning**: Empirical evidence that causal reasoning performance follows a scaling relationship with simulator complexity during training.

**Epistemic status**: `[SOURCE_CLAIM]` — preprint. The scaling law claim is `DERIVED` from empirical curves. Whether the scaling relationship holds beyond the tested complexity range is `UNKNOWN/GAP`.

**Falsifier**: If the scaling relationship plateaus at a complexity level below real-world causal reasoning requirements, the simulator-scaling approach has a bounded ceiling and cannot reach practical causal competence.

**Provenance**: `arxiv_2605_09079_causim_scaling_causal_simulators` — single preprint, May 2026.

---

## 3. Cross-Paper Synthesis

### 3.1 Convergent Themes

| Theme | Papers | Convergence |
| :--- | :--- | :--- |
| **Foundation model paradigm for causal inference** | CFMs, Partial Graphs, CauSim | Causal estimation shifting from bespoke pipelines to pretrained models |
| **Verification and auditability** | DOVERIFIER, Causal-Audit | Moving from opaque LLM outputs to formally verifiable causal reasoning |
| **Post-training specialization** | CausalGym, Causal-Audit | Targeted training dramatically outperforms general-purpose scale |
| **Graph conditioning** | Partial Graphs, DOVERIFIER, Causal-Audit | Causal graphs as structured input/bias for causal reasoning systems |
| **Scaling via complexity** | CauSim, CFMs | Increasing training complexity as the path to causal competence |

### 3.2 Divergent Findings

| Tension | Paper A | Paper B | Resolution Status |
| :--- | :--- | :--- | :--- |
| **Scale vs specialization** | CausalGym (14B > o3) | CFMs (scale enables in-context) | `COMPETING` — both effects may coexist; specialization dominates benchmarks, scale enables zero-shot transfer |
| **End-to-end vs modular** | CFMs (end-to-end in-context) | Causal-Audit (modular stages) | `COMPETING` — CFMs optimize estimation, Causal-Audit optimizes auditability; different objectives |
| **Symbolic vs neural** | DOVERIFIER (symbolic verification) | CFMs (neural estimation) | `COMPATIBLE` — symbolic verification can validate neural outputs; complementary, not competing |

---

## 4. AMOS Cross-References

### 4.1 L4_CAUSAL

The AMOS L4_CAUSAL layer specifies causal reasoning as a fourth-level cognitive capability above perception (L1), correlation (L2), and intervention (L3). The 2026 research validates this hierarchy:

- **CFMs** operationalize L4 (counterfactual/structural reasoning) via in-context estimation
- **DOVERIFIER** provides the formal verification layer that L4_CAUSAL requires for epistemic grounding
- **Causal-Audit** implements the auditability requirement that AMOS imposes on all L4 reasoning

**AMOS invariant preserved**: `CAPABILITY != AUTHORITY` — a CFM's capability to estimate causal effects does not grant it authority to make causal claims without verification. DOVERIFIER-style symbolic verification is the authority mechanism.

### 4.2 causal-reasoning-master

The AMOS `causal-reasoning-master` skill should integrate:

- **CFM estimation** as a first-class causal estimation tool alongside traditional estimators (IPW, doubly robust, regression discontinuity)
- **DOVERIFIER-style verification** as a mandatory validation step for any LLM-generated causal expression
- **CausalGim post-training recipes** (especially GRPO) for AMOS causal reasoning model development
- **Causal-Audit's four-stage decomposition** as the canonical auditable reasoning structure for AMOS causal agents

### 4.3 scientific-closure-governor

The AMOS scientific-closure-governor — which governs when a scientific claim can be promoted from hypothesis to established — must account for:

- **CFM estimates require external validation**: A CFM's in-context ATE estimate is a `[MODEL]` claim, not a `[SOURCE_CLAIM]`. Promotion to established requires validation against ground truth (RCT, natural experiment).
- **DOVERIFIER verification is necessary but not sufficient**: Symbolic derivability from a graph verifies formal correctness but does not verify the graph itself. Graph validation remains a separate epistemic requirement.
- **Benchmark performance is not deployment performance**: CaLM 93.5% does not establish real-world causal competence. The closure governor must enforce deployment-environment validation.

---

## 5. Falsifiers

### 5.1 Global Falsifiers (Apply to Entire Synthesis)

| ID | Falsifier | Scope | Status |
| :--- | :--- | :--- | :--- |
| F-CFM-01 | CFM estimates on real-world observational data systematically diverge from bespoke estimators beyond estimator variance | CFMs | `UNTESTED` |
| F-CFM-02 | CFM in-context causal estimation fails on datasets with >1000 variables or deep causal graphs (>5 levels) | CFMs, Partial Graphs | `UNTESTED` |
| F-DOV-01 | DOVERIFIER cannot handle graphs with latent variables or cycles | DOVERIFIER | `PARTIALLY_TESTED` (do-calculus is defined for DAGs; latent variables via ID algorithm) |
| F-GYM-01 | CaLM benchmark tasks lack real-world complexity (confounding, selection bias, measurement error) | CausalGym | `UNTESTED` |
| F-GYM-02 | o3's 55.4% reflects format mismatch, not causal reasoning deficit | CausalGym | `UNTESTED` |
| F-PG-01 | Attention biases are brittle to graph perturbations | Partial Graphs | `UNTESTED` |
| F-AUD-01 | Four-stage decomposition causes error accumulation without correction | Causal-Audit | `UNTESTED` |
| F-SIM-01 | Simulator scaling plateaus below real-world complexity requirements | CauSim | `UNTESTED` |

### 5.2 Epistemic Boundary

> [!WARNING] Epistemic Boundary
> This synthesis establishes that the **research direction** — foundation models for causal reasoning — is active and producing results. It does **NOT** establish that CFMs are ready for deployment in safety-critical causal decision-making (medicine, policy, economics). All deployment claims remain `UNKNOWN/GAP` until validated on real-world data with ground-truth causal effects.

---

## 6. Implications for AMOS Causal Reasoning

### 6.1 Architecture Implications

| AMOS Component | Implication | Priority |
| :--- | :--- | :--- |
| **L4_CAUSAL** | Integrate CFM as a causal estimation backend alongside traditional estimators | HIGH |
| **causal-reasoning-master** | Add DOVERIFIER-style symbolic verification as mandatory post-processing for LLM causal outputs | HIGH |
| **scientific-closure-governor** | Enforce that CFM estimates require external validation before promotion; benchmark performance ≠ deployment performance | HIGH |
| **RSCF classification** | CFM outputs classified as `[MODEL]`; DOVERIFIER-verified outputs upgrade to `[DERIVED]`; externally validated outputs upgrade to `[SOURCE_CLAIM]` | HIGH |
| **Post-training pipeline** | Adopt GRPO as the preferred post-training method for AMOS causal reasoning models | MEDIUM |
| **Causal audit trail** | Implement Causal-Audit's four-stage decomposition for all AMOS causal agent outputs | MEDIUM |
| **Simulator curriculum** | Integrate CauSim-style complexity scaling for AMOS causal model training | MEDIUM |

### 6.2 RSCF Classification Rules for Causal Claims

```yaml
causal_rscf_classification:
  cfm_in_context_estimate:
    rscf_state: MODEL
    authority: NONE
    note: "Foundation model output without external validation"
  
  doverifier_verified_expression:
    rscf_state: DERIVED
    authority: FORMAL_DERIVABILITY
    note: "Symbolically verified against supplied graph; graph itself unverified"
  
  externally_validated_estimate:
    rscf_state: SOURCE_CLAIM
    authority: GROUND_TRUTH_COMPARISON
    note: "Validated against RCT or natural experiment ground truth"
  
  benchmark_performance_claim:
    rscf_state: SOURCE_CLAIM
    authority: BENCHMARK
    note: "Valid only within benchmark distribution; deployment generalization UNKNOWN/GAP"
  
  scaling_law_claim:
    rscf_state: DERIVED
    authority: EMPIRICAL_FIT
    note: "Empirical scaling relationship; extrapolation beyond tested range UNKNOWN/GAP"
```

### 6.3 AMOS Causal Reasoning Stack (Proposed 2026 Update)

```text
┌─────────────────────────────────────────┐
│  SCIENTIFIC CLOSURE GOVERNOR            │
│  (external validation, promotion gate)   │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│  DOVERIFIER-STYLE SYMBOLIC VERIFICATION  │
│  (do-calculus, derivability checking)    │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│  CAUSAL-AUDIT FOUR-STAGE DECOMPOSITION   │
│  (target → chain → evidence → conclusion)│
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│  CAUSAL FOUNDATION MODEL (CFM)           │
│  (in-context ATE estimation, partial     │
│   graph conditioning via attention bias) │
└──────────────────┬──────────────────────┘
                   │
┌──────────────────▼──────────────────────┐
│  CAUSAL SIMULATOR CURRICULUM (CauSim)    │
│  (complexity-scaled training data)       │
└─────────────────────────────────────────┘
```

---

## 7. Open Questions / GAPS

### 7.1 Established GAPS

| ID | Gap | Status | Resolution Path |
| :--- | :--- | :--- | :--- |
| G-01 | CFM performance on real-world observational data with ground-truth causal effects | `UNKNOWN/GAP` | Validate on datasets with RCT ground truth (e.g., Lalonde, Tennessee STAR) |
| G-02 | DOVERIFIER coverage for graphs with latent variables and cyclic structures | `UNKNOWN/GAP` | Extend with ID algorithm and cyclic causal models |
| G-03 | Whether CaLM benchmark performance generalizes to non-benchmark causal tasks | `UNKNOWN/GAP` | Evaluate post-trained models on held-out causal reasoning distributions |
| G-04 | Attention-bias conditioning robustness to graph perturbations | `UNKNOWN/GAP` | Perturbation studies on partial-graph CFMs |
| G-05 | CauSim scaling law behavior beyond tested complexity range | `UNKNOWN/GAP` | Extend simulator complexity and measure performance curves |
| G-06 | Interaction between CFM in-context estimation and symbolic verification | `UNKNOWN/GAP` | Pipeline CFM outputs through DOVERIFIER; measure verification rate |
| G-07 | Whether post-training methods (GRPO) transfer across causal benchmark families | `UNKNOWN/GAP` | Cross-benchmark evaluation of GRPO-trained models |

### 7.2 AMOS-Specific Open Questions

| ID | Question | AMOS Component |
| :--- | :--- | :--- |
| AQ-01 | Should AMOS L4_CAUSAL treat CFM estimates as `[MODEL]` or `[DERIVED]` when partial graph conditioning is provided? | L4_CAUSAL, RSCF |
| AQ-02 | Can the scientific-closure-governor automate the promotion from `[MODEL]` to `[SOURCE_CLAIM]` when DOVERIFIER + external validation both pass? | scientific-closure-governor |
| AQ-03 | Should AMOS causal agents use Causal-Audit's four-stage decomposition as a mandatory reasoning structure, or allow end-to-end CFM estimation with post-hoc audit? | causal-reasoning-master |
| AQ-04 | How does the `CAPABILITY != AUTHORITY` invariant apply when a CFM's in-context estimate is used as input to a governance decision? | capability-bound governance |
| AQ-05 | Does the CauSim scaling law interact with AMOS's evolutionary debt tracking — i.e., does training on more complex simulators accumulate debt in simpler reasoning modes? | evolutionary-debt |

---

## 8. Cross-Vault References

- [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]] — authority and governance for causal claims
- [[05_COGNITIVE_ORGANISM/05_COGNITIVE_ORGANISM_MOC|05_COGNITIVE_ORGANISM_MOC]] — L4_CAUSAL cognitive layer
- [[11_KNOWLEDGE/11_KNOWLEDGE_MOC|11_KNOWLEDGE_MOC]] — causal knowledge representation and promotion
- [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY_MOC]] — causal audit trails and verification
- [[19_TESTS/19_TESTS_MOC|19_TESTS_MOC]] — causal reasoning evaluation and benchmarking
- [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]] — research synthesis index
- [[22_RESEARCH/03_SOTA/SOTA_BCI_AI_QUANTUM_SYNTHESIS_2026|SOTA_BCI_AI_QUANTUM_SYNTHESIS_2026]] — adjacent SOTA synthesis

---

```RSCF-NODE
node_id: sota_causal_reasoning_foundation_models_2026
node_type: research_synthesis
domain: C10_TECH_ENGINEERING
claim_class: DERIVED
confidence_ceiling: HIGH_FOR_RESEARCH_DIRECTION__MEDIUM_FOR_SPECIFIC_RESULTS__LOW_FOR_DEPLOYMENT_READINESS
falsifiers:
  - CFM estimates diverge from bespoke estimators on real-world data beyond estimator variance
  - CaLM benchmark performance does not generalize to non-benchmark causal tasks
  - DOVERIFIER cannot handle latent or cyclic causal graphs
  - Attention-bias conditioning is brittle to graph perturbations
  - CauSim scaling law plateaus below real-world complexity
  - Four-stage causal audit causes uncorrected error accumulation
gaps:
  - No real-world validation of CFM in-context estimation against ground-truth causal effects
  - No cross-benchmark evaluation of GRPO post-trained causal models
  - No integration of CFM estimation with symbolic verification in a single pipeline
  - No test of attention-bias robustness to graph perturbations
  - No extension of CauSim scaling law beyond tested complexity range
```
