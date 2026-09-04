---
title: "SOTA Synthesis: LLM Agent Tool-Use Planning & Invocation (2026)"
type: research_synthesis
paper_id: AMOS-SOTA-LLM-AGENT-TOOL-USE-2026
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
status: ACTIVE_SYNTHESIS
epistemic_class: SOURCE_CLAIM
conclusion_class: DERIVED
rscf:
  state: SOURCE_CLAIM
  claim_class: EMPIRICAL_SURVEY
  provenance:
    - arXiv:2608.02650 (HyperAgent — Tool-Schema Hypergraph)
    - arXiv:2603.12740 (ToolTree — MCTS-Inspired Tool Planning)
    - arXiv:2608.03468 (ToolLIFT — Function-Level Workflow Graphs)
    - arXiv:2609.01736 (HEART/Tool Primitives — NL Tool Interface)
    - arXiv:2609.03236 (Speculative Macro Commit — Two-Tier Agent)
  scope: llm_agent_tool_use_planning_invocation_2026
  freshness: 2026-09-04
  falsifier: "Benchmark gains (AppWorld, ToolBench) do not establish deployment-grade tool-use reliability under adversarial or distribution-shifted conditions"
tags:
  - amos-os
  - research
  - sota-2026
  - llm-agents
  - tool-use
  - planning
  - rscf
  - sota
---

# SOTA Synthesis: LLM Agent Tool-Use Planning & Invocation (2026)

> **Author / Steward:** Trang Phan
> **Target OS:** `AMOS_OS v4.4`
> **Epistemic Class:** `SOURCE_CLAIM / DERIVED`
> **Date:** September 2026

---

## Overview

The 2026 LLM agent tool-use landscape has undergone a structural shift from **prompt-level function calling** to **graph-structured, search-based, and speculative planning** over tool spaces. Five breakthrough strands define the SOTA:

1. **Hypergraph-based planning** (HyperAgent) models tools as hyperedges connecting input-schema to output-schema nodes, enabling deficit-oriented DAG expansion and principled redundancy elimination.
2. **Search-based tool planning** (ToolTree) adapts Monte Carlo Tree Search to tool selection with dual-stage LLM evaluation and bidirectional pruning, yielding ~10% average gains over prior SOTA.
3. **Workflow-level abstraction** (ToolLIFT) lifts tool-specific trajectories into function-level workflow graphs, decoupling workflow planning from tool selection and achieving strong out-of-distribution generalization via source-gated RL.
4. **Natural-language tool interfaces** (HEART/Tool Primitives) eliminate brittle schema-based invocation by routing through a Planner/Router/Verifier architecture over a 25,519-function repository.
5. **Speculative execution** (Speculative Macro Commit) introduces a two-tier actor-drafter architecture with a macro library of recurring multi-action skeletons, reducing latency 10–18%.

Together, these advances mark the transition from **reactive tool calling** to **structured, verifiable, and speculative tool-use planning** — a shift directly relevant to AMOS's agent-systems and tool-layer architecture.

---

## Key Papers

### 1. HyperAgent: Tool-Schema Hypergraph (TSH) for Planning — arXiv:2608.02650

- **[SOURCE_CLAIM]** HyperAgent introduces the **Tool-Schema Hypergraph (TSH)**, a bipartite hypergraph where tools are represented as hyperedges connecting input-schema nodes to output-schema nodes.
- **Architecture**: Each tool is a hyperedge `e: (input_schema_nodes) → (output_schema_nodes)`. Task planning constructs a DAG by chaining hyperedges whose output schemas satisfy downstream input schemas.
- **Deficit-oriented expansion**: The planner identifies "schema deficits" — required input parameters not yet satisfied by the current partial DAG — and selects tools that produce those parameters, enabling principled, goal-directed expansion rather than greedy LLM selection.
- **Results**: Improvements on the **AppWorld benchmark**; significant reduction in redundant API calls compared to ReAct-style and function-calling baselines.
- **Provenance**: arXiv:2608.02650 (Aug 2026); peer-review status UNKNOWN/GAP.
- **Falsifier (F-HA-01)**: TSH planning assumes schema completeness and correctness — tools with underspecified or dynamically-typed schemas may produce invalid hyperedges. `UNTESTED` on dynamically-typed API ecosystems.
- **Falsifier (F-HA-02)**: AppWorld benchmark gains may not generalize to open-world tool repositories with >10K tools. `UNTESTED`.
- **AMOS Mapping**: TSH maps to AMOS `14_TOOLS` tool registry and `06_AGENTS` dependency graph. Deficit-oriented expansion instantiates AMOS's dependency-cone (CR/CD) computation for tool selection.

### 2. ToolTree: MCTS-Inspired Planning for Tool Use — arXiv:2603.12740

- **[SOURCE_CLAIM]** ToolTree adapts **Monte Carlo Tree Search (MCTS)** to the tool-use planning problem, treating each tool invocation as a node expansion in a search tree.
- **Dual-stage LLM evaluation**: A pre-execution **prior** evaluates the promise of a candidate tool call before execution; a post-execution **utility** assessment evaluates the observed result. Both signals backpropagate through the tree.
- **Bidirectional pruning**: Forward pruning eliminates low-prior branches before execution (saving API calls); backward pruning retroactively prunes branches whose post-execution utility falls below threshold, preventing wasted downstream expansion.
- **Results**: **~10% average gain** over prior SOTA across multiple tool-use benchmarks.
- **Provenance**: arXiv:2603.12740 (Mar 2026); peer-review status UNKNOWN/GAP.
- **Falsifier (F-TT-01)**: MCTS search depth is bounded by LLM evaluation cost — deep multi-step tasks (>15 tool calls) may exhaust the evaluation budget before finding high-utility paths. `UNTESTED` on deep horizons.
- **Falsifier (F-TT-02)**: Dual-stage evaluation relies on LLM judgment quality — if the LLM's pre-execution prior is systematically miscalibrated, pruning removes optimal branches. `UNTESTED` under adversarial tool descriptions.
- **AMOS Mapping**: ToolTree's search-based planning maps to AMOS `06_AGENTS` planning layer and the MURK reasoning engine's minimax robust-branch evaluation. Bidirectional pruning instantiates AMOS's mutation-gate-layer forward/backward filtering.

### 3. ToolLIFT: Function-Level Workflow Graphs (FWG) — arXiv:2608.03468

- **[SOURCE_CLAIM]** ToolLIFT **lifts** tool-specific execution trajectories into **Function-level Workflow Graphs (FWG)** — abstract graphs where nodes represent function-level operations (not individual tool calls) and edges represent data-flow dependencies.
- **Decoupled architecture**: Workflow planning (which functions to compose) is decoupled from tool selection (which specific tool implements each function), enabling workflow reuse across tool ecosystems.
- **RL training**: Reinforcement learning with **source-gated rewards** (reward signal gated by trajectory source quality) and **skill-specific rewards** (per-function reward shaping). This produces policies that generalize across tool variants.
- **Results**: **Strong out-of-distribution (OOD) generalization** — workflows learned on one tool set transfer to unseen tools implementing the same functions.
- **Provenance**: arXiv:2608.03468 (Aug 2026); peer-review status UNKNOWN/GAP.
- **Falsifier (F-TL-01)**: FWG abstraction assumes function-level semantics are stable across tool implementations — tools with side-effects or implicit state may break the abstraction. `UNTESTED` on stateful APIs.
- **Falsifier (F-TL-02)**: Source-gated RL reward design may introduce bias toward training-distribution trajectory patterns. `UNTESTED` for systematic reward-hacking susceptibility.
- **AMOS Mapping**: FWG maps to AMOS `06_AGENTS` workflow abstraction and `14_TOOLS` tool-binding layer. Source-gated rewards map to AMOS provenance-gated commit authority (proof-carrying commits with source attestation).

### 4. HEART / Tool Primitives: Natural Language as Tool Interface — arXiv:2609.01736

- **[SOURCE_CLAIM]** HEART (Human-Executable Agent Reasoning with Tools) eliminates **brittle schema-based tool invocation** by using natural language as the tool interface, mediated by a **Planner / Router / Verifier** architecture.
- **ToolFace repository**: A curated repository of **25,519 functions** with natural-language descriptions, enabling the Router to map natural-language intents to function implementations without rigid schema matching.
- **Architecture**:
  - **Planner**: Decomposes task into natural-language sub-goals.
  - **Router**: Maps each sub-goal to a candidate function in ToolFace via semantic retrieval.
  - **Verifier**: Checks execution results against the natural-language intent, enabling retry on mismatch.
- **Results**: Eliminates schema-parsing failures; robust to API description variations and parameter naming inconsistencies.
- **Provenance**: arXiv:2609.01736 (Sep 2026); peer-review status UNKNOWN/GAP.
- **Falsifier (F-HE-01)**: Natural-language routing introduces semantic ambiguity — functions with overlapping descriptions may cause Router misselection at scale (>25K functions). `PARTIALLY_TESTED` (validated on subset).
- **Falsifier (F-HE-02)**: Verifier relies on LLM judgment — verification of numerical or side-effecting results may be unreliable. `UNTESTED` on numerical-precision tasks.
- **AMOS Mapping**: Planner/Router/Verifier maps to AMOS `06_AGENTS` agent architecture and `03_CONTROL_PLANE` commit orchestrator. ToolFace repository maps to AMOS `14_TOOLS` tool registry with semantic retrieval via `10_MEMORY` vector store.

### 5. Speculative Macro Commit: Two-Tier Agent Architecture — arXiv:2609.03236

- **[SOURCE_CLAIM]** Speculative Macro Commit introduces a **two-tier agent architecture**: an **authoritative actor** (large model, e.g., Qwen3.5-27B) and a **speculative drafter** (small model, e.g., Qwen3.5-4B) that proposes multi-action skeletons.
- **Macro library**: A library of **recurring multi-action skeletons** (macros) is maintained. The drafter proposes a macro instantiation; the actor verifies and commits or rejects.
- **Mechanism**: The drafter speculatively executes a macro skeleton; the actor asynchronously validates. On acceptance, the committed actions skip the actor's per-step generation, reducing latency. On rejection, the actor falls back to step-by-step generation.
- **Results**: **10–18% latency reduction** on multi-step tool-use tasks. Qwen3.5-27B/4B pairing validated.
- **Provenance**: arXiv:2609.03236 (Sep 2026); peer-review status UNKNOWN/GAP.
- **Falsifier (F-SMC-01)**: Macro library coverage determines gains — tasks outside the macro distribution fall back to step-by-step, negating latency benefits. `UNTESTED` on novel task distributions.
- **Falsifier (F-SMC-02)**: Speculative drafting with a 4B model may introduce safety risks if the drafter proposes harmful action sequences that the actor fails to catch under time pressure. `UNTESTED` under adversarial macro injection.
- **AMOS Mapping**: Two-tier architecture maps to AMOS `04_RUNTIME` execution modes (fast-path vs. verified-path) and `amos-speed-optimization-layer` (max_safe_speed / balanced_fast / precision_priority). Macro library maps to AMOS `06_AGENTS` skill library with provenance-gated reuse.

---

## AMOS Cross-References

- [[06_AGENTS/06_AGENTS_MOC|06_AGENTS_MOC]] — Agent architecture, planning, dependency graphs
- [[14_TOOLS/14_TOOLS_MOC|14_TOOLS_MOC]] — Tool registry, tool binding, tool execution layer
- `amos-agent-systems-master` — Master skill for agent system design and orchestration
- `amos-os-runtime-master` — Master skill for runtime execution modes and speed optimization
- [[22_RESEARCH/01_PAPERS/SOTA_AI_AGENTS_AND_TOOL_USE_FRAMEWORKS_2026|SOTA AI Agents & Tool Use Frameworks (earlier synthesis)]]
- [[22_RESEARCH/01_PAPERS/SOTA_MULTI_AGENT_FRAMEWORKS_2026|SOTA Multi-Agent Frameworks]]
- [[07_SKILLS/amos-capability-bound-governance/SKILL|Capability-Bound Governance]] — Tool invocation authority gating

---

## Falsifiers

### Global Falsifiers

| ID | Falsifier | Scope | Status |
|:---|:---|:---|:---|
| F-GLOBAL-01 | Benchmark gains (AppWorld, ToolBench) do not establish deployment-grade reliability under adversarial or distribution-shifted tool ecosystems | All papers | `UNTESTED` |
| F-GLOBAL-02 | LLM-based evaluation (ToolTree priors, HEART Verifier) is susceptible to prompt-injection via malicious tool descriptions | ToolTree, HEART | `UNTESTED` |
| F-GLOBAL-03 | Schema/hypergraph abstractions (TSH, FWG) break on dynamically-typed or side-effecting APIs | HyperAgent, ToolLIFT | `UNTESTED` |
| F-GLOBAL-04 | Speculative execution (SMC) may commit harmful macro instantiations before actor verification completes under race conditions | Speculative Macro Commit | `UNTESTED` |
| F-GLOBAL-05 | All five methods assume single-agent tool use — multi-agent concurrent tool access with shared state is NOT ESTABLISHED | All papers | `UNTESTED` |

### Epistemic Boundary

> [!WARNING] Epistemic Boundary
> This synthesis establishes that **structured tool-use planning** (hypergraph, search, workflow, NL-interface, speculative) produces measurable benchmark improvements. It does **NOT** establish that these methods are ready for safety-critical autonomous tool use (financial transactions, infrastructure control, medical systems). All deployment claims remain `UNKNOWN/GAP` until validated under adversarial conditions with formal safety guarantees.

---

## Implications for AMOS OS

### Architecture Implications

| AMOS Component | Implication | Priority |
|:---|:---|:---|
| **14_TOOLS** | Adopt TSH-style schema hypergraph as the canonical tool registry representation; enable deficit-oriented tool selection | HIGH |
| **06_AGENTS** | Integrate ToolTree-style MCTS planning as an optional planning mode for complex multi-tool tasks | MEDIUM |
| **06_AGENTS** | Adopt FWG abstraction to decouple workflow planning from tool binding, enabling cross-tool-ecosystem portability | HIGH |
| **14_TOOLS** | Evaluate NL-based tool routing (HEART-style) as an alternative to rigid schema matching for large tool registries | MEDIUM |
| **04_RUNTIME** | Implement speculative macro execution as a speed-optimization-layer mode with actor-verified commit semantics | MEDIUM |
| **amos-capability-bound-governance** | All tool invocations require capability-bound authority gating; speculative drafts require provisional authority with commit-time verification | HIGH |
| **RSCF classification** | Tool-use plans classified as `[MODEL]`; executed-and-verified results upgrade to `[SOURCE_CLAIM]`; speculative drafts remain `[MODEL]` until actor commit | HIGH |

### RSCF Classification Rules for Tool-Use Claims

```yaml
tool_use_rscf_classification:
  tsh_dag_plan:
    rscf_state: MODEL
    authority: SCHEMA_DERIVABILITY
    note: "Plan derived from tool schemas; schema correctness unverified"

  tooltree_selected_path:
    rscf_state: MODEL
    authority: LLM_EVALUATION_PRIOR
    note: "Path selected via LLM prior; post-execution utility may revise"

  fwg_workflow:
    rscf_state: DERIVED
    authority: TRAJECTORY_LIFT
    note: "Workflow lifted from executed trajectories; function-level abstraction"

  heart_verified_result:
    rscf_state: SOURCE_CLAIM
    authority: NL_VERIFIER
    note: "Result verified against natural-language intent; verifier reliability bounded"

  smc_committed_macro:
    rscf_state: SOURCE_CLAIM
    authority: ACTOR_COMMIT
    note: "Macro committed by authoritative actor; speculative draft prior to commit is MODEL"

  benchmark_performance_claim:
    rscf_state: SOURCE_CLAIM
    authority: BENCHMARK
    note: "Valid only within benchmark distribution; deployment generalization UNKNOWN/GAP"
```

### Proposed AMOS Tool-Use Stack (2026 Update)

```text
┌──────────────────────────────────────────────┐
│  CAPABILITY-BOUND GOVERNANCE GATE             │
│  (authority check per tool invocation)        │
└──────────────────┬───────────────────────────┘
                   │
┌──────────────────▼───────────────────────────┐
│  SPECULATIVE MACRO LAYER (optional)           │
│  (drafter proposes, actor commits/rejects)    │
└──────────────────┬───────────────────────────┘
                   │
┌──────────────────▼───────────────────────────┐
│  PLANNING LAYER (TSH / ToolTree / FWG)        │
│  (hypergraph DAG / MCTS search / workflow)    │
└──────────────────┬───────────────────────────┘
                   │
┌──────────────────▼───────────────────────────┐
│  ROUTING LAYER (HEART-style NL or schema)     │
│  (Planner → Router → Verifier)                │
└──────────────────┬───────────────────────────┘
                   │
┌──────────────────▼───────────────────────────┐
│  TOOL REGISTRY (14_TOOLS)                     │
│  (schema hypergraph + semantic index)         │
└──────────────────────────────────────────────┘
```

---

## Open Questions / GAPS

### Established GAPS

| ID | Gap | Status | Resolution Path |
|:---|:---|:---|:---|
| G-01 | TSH performance on dynamically-typed or underspecified API schemas | `UNKNOWN/GAP` | Test on GraphQL/REST APIs with optional/dynamic parameters |
| G-02 | ToolTree MCTS scaling to >15-step tool chains within evaluation budget | `UNKNOWN/GAP` | Profile evaluation cost vs. depth; explore budget-adaptive search |
| G-03 | FWG abstraction robustness to stateful/side-effecting tools | `UNKNOWN/GAP` | Test on APIs with authentication state, pagination, rate limits |
| G-04 | HEART Router accuracy at >25K function scale with overlapping descriptions | `UNKNOWN/GAP` | Scale-test on full ToolFace; measure precision/recall |
| G-05 | SMC macro library coverage on novel task distributions | `UNKNOWN/GAP` | Evaluate on out-of-distribution tasks; measure fallback rate |
| G-06 | Multi-agent concurrent tool access with shared mutable state | `UNKNOWN/GAP` | Extend all methods to concurrent multi-agent setting |
| G-07 | Adversarial robustness of LLM-based evaluation (priors, verifiers) | `UNKNOWN/GAP` | Red-team with malicious tool descriptions and prompt injection |

### AMOS-Specific Open Questions

| ID | Question | AMOS Component |
|:---|:---|:---|
| AQ-01 | Should AMOS adopt TSH as the canonical tool registry format, or maintain dual schema + NL representations? | 14_TOOLS, RSCF |
| AQ-02 | Can ToolTree's MCTS planning be integrated with the MURK reasoning engine's minimax robust-branch evaluation? | amos-agent-systems-master |
| AQ-03 | Should FWG workflows be classified as `[DERIVED]` or `[MODEL]` when lifted from unverified trajectories? | RSCF, 06_AGENTS |
| AQ-04 | Does HEART's NL-based routing satisfy AMOS capability-bound governance, or does NL ambiguity bypass authority checks? | amos-capability-bound-governance |
| AQ-05 | Can SMC's speculative drafts be governed by provisional authority with commit-time attestation, consistent with ERA/ETC? | amos-enforcement-root-attestation |
| AQ-06 | How should AMOS handle tool-use plans that span multiple RSCF states (e.g., TSH plan [MODEL] → executed result [SOURCE_CLAIM])? | RSCF, scientific-closure-governor |

---

## References

1. HyperAgent: Tool-Schema Hypergraph for LLM Agent Planning. arXiv:2608.02650 (Aug 2026).
2. ToolTree: MCTS-Inspired Planning for LLM Tool Use. arXiv:2603.12740 (Mar 2026).
3. ToolLIFT: Lifting Tool Trajectories to Function-Level Workflow Graphs. arXiv:2608.03468 (Aug 2026).
4. HEART: Natural Language as Tool Interface with ToolFace Repository. arXiv:2609.01736 (Sep 2026).
5. Speculative Macro Commit: Two-Tier Agent Architecture for Latency Reduction. arXiv:2609.03236 (Sep 2026).

---

## Navigation

- [[22_RESEARCH/01_PAPERS/01_PAPERS_MOC|Papers MOC]]
- [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]]
- [[22_RESEARCH/01_PAPERS/SOTA_AI_AGENTS_AND_TOOL_USE_FRAMEWORKS_2026|SOTA AI Agents & Tool Use Frameworks (earlier synthesis)]]
- [[22_RESEARCH/01_PAPERS/SOTA_MULTI_AGENT_FRAMEWORKS_2026|SOTA Multi-Agent Frameworks]]
- [[22_RESEARCH/01_PAPERS/SOTA_FOUNDATION_AGENTS_AND_COGNITIVE_ARCHITECTURES_2026|SOTA Foundation Agents]]
