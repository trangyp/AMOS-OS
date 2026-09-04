---
title: "Gated-Memory Routing — Learning What to Retain for Efficient Multi-Agent LLM Collaboration"
type: research_paper
source: arxiv
arxiv_id: "2609.00237"
url: "https://arxiv.org/abs/2609.00237"
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
epistemic_class: SOURCE_CLAIM
conclusion_class: DERIVED
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance:
    - arxiv:2609.00237
    - EMNLP_2026_main_conference
  scope: multi_agent_memory_routing
tags:
  - research
  - arxiv
  - multi-agent
  - memory
  - gated-routing
  - convergence-detection
  - compaction
  - retrieval
created: 2026-09-05
---

# Gated-Memory Routing — Learning What to Retain

> **arXiv:** [2609.00237](https://arxiv.org/abs/2609.00237)
> **Venue:** EMNLP 2026 (Main Conference)
> **Epistemic class:** `SOURCE_CLAIM` (peer-reviewed, EMNLP 2026)
> **AMOS bridge:** K_Memory_Admission, K_Memory_Retrieval, K_Context_Compaction, Convergence Detection, Memory Systems

## Abstract summary

Multi-agent LLM systems generate large volumes of intermediate reasoning, but existing methods either retain everything (high cost, redundancy) or discard aggressively (loss of useful evidence). Gated-Memory Routing (GMR) introduces a three-gate architecture that learns **what to retain** in shared execution memory:

1. **Memory Write Gate** — conditions each write decision on the current query and learned execution memory; commits only non-redundant reasoning steps.
2. **Retrieval Gate** — conditions each retrieval on the receiving agent's query; supplies a compact, relevant subset of memory rather than the full history.
3. **Adaptive Halting Controller** — monitors accumulated memory evidence and stops multi-agent execution once memory contains sufficient evidence to answer, avoiding unnecessary additional agent invocations.

Each gate is query-conditioned and memory-conditioned, so admission, retrieval, and termination all adapt to the current task state.

## Key results

- **Best average accuracy** across 5 benchmarks, exceeding the strongest baseline by **2.44 points**.
- **31.9% HumanEval inference cost reduction** via adaptive halting and non-redundant memory writes.
- Memory Write Gate eliminates redundant reasoning steps without losing task-critical evidence.
- Retrieval Gate provides each agent a compact, relevant subset, reducing context overhead per invocation.
- Adaptive Halting Controller terminates execution early when memory evidence is sufficient, cutting unnecessary agent calls.

## AMOS bridge analysis

### Bridge to K_Memory_Admission

GMR's **Memory Write Gate** is a direct instance of AMOS K_Memory_Admission:

```text
AMOS K_Memory_Admission:
  "not all generated content enters memory"
  admission filter decides what is worth retaining
  conditions admission on current task + existing memory state

GMR Memory Write Gate:
  conditions each write on query + learned execution memory
  commits only non-redundant reasoning steps
  redundant steps are rejected at the gate
```

Both enforce the same invariant: **memory admission is selective and state-conditioned, not unconditional accumulation**.

### Bridge to K_Memory_Retrieval

GMR's **Retrieval Gate** maps to AMOS K_Memory_Retrieval:

```text
AMOS K_Memory_Retrieval:
  "retrieve compact relevant subset, not full history"
  compaction-aware retrieval — retrieval respects what has been consolidated/evicted
  query-conditioned selection from memory

GMR Retrieval Gate:
  conditions retrieval on receiving agent's query
  supplies compact, relevant subset of memory
  each agent gets only what it needs for its current step
```

Both enforce the same invariant: **retrieval is query-conditioned and compaction-aware, returning the minimal sufficient subset**.

### Bridge to K_Context_Compaction

GMR's **non-redundant step filtering** (via the Memory Write Gate) maps to AMOS K_Context_Compaction:

```text
AMOS K_Context_Compaction:
  "evict redundant context to bound working set"
  compaction removes redundant or low-value context entries
  preserves load-bearing information while shrinking the context window

GMR non-redundant step filtering:
  Memory Write Gate rejects reasoning steps already represented in memory
  redundant intermediate results are never committed
  working memory stays compact across the multi-agent execution
```

Both enforce the same invariant: **redundant context is evicted before it inflates the working set**.

### Bridge to Convergence Detection

GMR's **Adaptive Halting Controller** is a direct instance of AMOS Convergence Detection:

```text
AMOS Convergence Detection:
  "detect when further processing yields diminishing returns"
  track productive vs stuck evolution steps
  halt when sufficient evidence / convergence criterion is met

GMR Adaptive Halting Controller:
  monitors accumulated memory evidence
  stops multi-agent execution once memory contains sufficient evidence
  avoids unnecessary additional agent invocations
```

Both enforce the same invariant: **execution halts when the system has accumulated sufficient evidence to decide**.

### Bridge to Memory Systems

GMR's three-gate architecture maps to the AMOS Memory Systems encode → consolidate → retrieve cycle:

```text
AMOS Memory Systems:
  encode → consolidate → retrieve → utilize
  admission gate → compaction/consolidation → retrieval → utilization

GMR three-gate architecture:
  Memory Write Gate (encode/admit) → non-redundant filtering (consolidate) → Retrieval Gate (retrieve) → Adaptive Halting (utilize/terminate)
```

The full cycle is governed: admission filters what enters, consolidation removes redundancy, retrieval selects what exits, and halting decides when the cycle is sufficient.

## Epistemic boundary

- GMR is validated on 5 benchmarks and accepted at EMNLP 2026 (Main Conference). Its results are `SOURCE_CLAIM` for the multi-agent memory routing domain.
- The AMOS bridges are `AMOS_MODEL` — structural analogies between GMR's gates and AMOS memory skills, not empirical validations of AMOS runtime mechanisms.
- GMR's Adaptive Halting Controller relies on a learned sufficiency estimator; it does not guarantee optimality of the halting point for all task distributions.
- Cost reduction figures (31.9% on HumanEval) are benchmark-specific and may not generalize to all multi-agent workloads or AMOS runtime configurations.

## Related

- [[07_SKILLS/amos-k-memory-admission/SKILL|K_Memory_Admission]]
- [[07_SKILLS/amos-k-memory-retrieval/SKILL|K_Memory_Retrieval]]
- [[07_SKILLS/amos-k-context-compaction/SKILL|K_Context_Compaction]]
- [[07_SKILLS/amos-convergence-detection/SKILL|Convergence Detection]]
- [[07_SKILLS/amos-memory-systems/SKILL|Memory Systems]]
- [[22_RESEARCH/01_PAPERS/ARXIV_2608_19701_CAMA_MEMORY_CORRELATION_BIAS|CAMA — Correlation-Aware Memory Arbitration]]
- [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]]
