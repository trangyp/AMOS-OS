---
title: "MAP-Graph — Provenance-Aware Shared Memory for Multi-Agent Workflows"
type: research_paper
source: arxiv
arxiv_id: "2608.10509"
url: "https://arxiv.org/abs/2608.10509"
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
epistemic_class: SOURCE_CLAIM
conclusion_class: DERIVED
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance:
    - arxiv:2608.10509
    - 22_RESEARCH/BCI_AI_QUANTUM_SOTA_2026-09-04
  scope: multi_agent_provenance_memory
tags:
  - research
  - arxiv
  - multi-agent
  - memory
  - provenance
  - trust
  - action-gating
  - permission-filtering
created: 2026-09-04
---

# MAP-Graph — Provenance-Aware Shared Memory

> **arXiv:** [2608.10509](https://arxiv.org/abs/2608.10509)
> **Epistemic class:** `SOURCE_CLAIM` (controlled benchmark, 2700 synthetic tasks per method across 3 domains)
> **AMOS bridge:** Provenance Trust Firewall, K-Binding, K_Memory_Admission, Commit-time gating, Action-Memory Firewall

## Abstract summary

MAP-Graph introduces a provenance-aware memory layer for multi-agent workflows. It represents agents, sources, memories, claims, and actions as nodes in a typed execution graph. The system traces ancestry through the graph, excludes permission-ineligible records from retrieval, reranks eligible memories by semantic similarity combined with multiplicative path trust, and applies a risk-sensitive gate before action execution. This makes provenance an operational control signal — not merely an audit trail — that directly gates which memories are admissible and which actions may execute.

## Key results

- 94.96% overall task success across 3 domains (2700 synthetic tasks per method)
- 72.70% exact decision accuracy; 90.22% in the clean setting
- Ablations isolate the contributions of permission filtering, path trust reranking, and action gating
- Transfer tests with two additional backbone LLMs preserve the advantages, indicating backbone-agnostic gains
- Provenance is used as an operational control signal: it filters, reranks, and gates — not just records

## AMOS bridge analysis

### Bridge to Provenance Trust Firewall

MAP-Graph's use of provenance as an operational control signal is the core instantiation of the AMOS Provenance Trust Firewall:

```text
AMOS Provenance Trust Firewall:
  provenance gates trust — untrusted or untraceable chains are rejected
  provenance is a control surface, not just an audit log

MAP-Graph provenance control:
  ancestry traced through typed execution graph
  permission-ineligible records excluded from retrieval
  path trust multiplies into memory ranking
  risk-sensitive gate blocks actions before execution
```

Both enforce the same invariant: **provenance determines admissibility, not just traceability**. MAP-Graph provides empirical evidence that provenance-gated retrieval and action execution improve task success.

### Bridge to K-Binding

MAP-Graph's permission filtering maps directly to AMOS K-Binding validation:

```text
AMOS K-Binding:
  not all relationships are valid — binding requires permission eligibility
  invalid bindings are rejected before they influence state

MAP-Graph permission filtering:
  records lacking required permissions are excluded from retrieval
  eligibility is checked against the typed graph before memory is admitted
```

Both enforce the same invariant: **permission eligibility is a precondition for binding**, not a post-hoc correction.

### Bridge to K_Memory_Admission

MAP-Graph's path trust reranking maps to AMOS K_Memory_Admission with provenance-weighted trust:

```text
AMOS K_Memory_Admission:
  memories are admitted by trust-weighted ranking, not raw similarity
  provenance weight modulates which memories surface

MAP-Graph path trust reranking:
  eligible memories reranked by semantic similarity × multiplicative path trust
  trust沿 the ancestry path compounds — weak links reduce ranked score
```

Both enforce the same invariant: **trust modulates admission rank**, so semantically similar but low-provenance memories are deprioritized.

### Bridge to Commit-time gating

MAP-Graph's risk-sensitive action gate maps to AMOS commit-time enforcement:

```text
AMOS commit-time enforcement:
  actions are gated at commit time — approval is not execution
  risk threshold determines whether an effect may externalize

MAP-Graph risk-sensitive gate:
  gate evaluates risk before action execution
  high-risk actions are blocked or escalated, not merely logged
```

Both enforce the same invariant: **a decision to act is not permission to execute**; a separate gate controls externalization.

### Bridge to Action-Memory Firewall

MAP-Graph's lineage retention maps to AMOS action-memory isolation with provenance preservation:

```text
AMOS Action-Memory Firewall:
  actions and memories are isolated — action effects do not corrupt memory provenance
  lineage is preserved for audit and rollback

MAP-Graph lineage retention:
  typed graph retains full ancestry of agents, sources, memories, claims, actions
  provenance chain is queryable for audit after execution
```

Both enforce the same invariant: **action effects and memory provenance are structurally separated**, preserving auditability.

## Epistemic boundary

- MAP-Graph is validated on 2700 synthetic tasks per method across 3 domains — a controlled benchmark, not AMOS runtime. Its results are `SOURCE_CLAIM` for the multi-agent provenance memory domain.
- The AMOS bridges are `AMOS_MODEL` — structural analogies, not empirical validations of AMOS mechanisms.
- Transfer tests with two additional backbones suggest backbone-agnostic gains, but do not establish generalization to arbitrary agent architectures or real-world deployment conditions.
- Permission filtering, path trust, and action gating are ablation-isolated contributions, but their interaction effects and scaling behavior beyond the tested domains remain `UNKNOWN/GAP`.

## Related

- [[22_RESEARCH/BCI_AI_QUANTUM_SOTA_2026-09-04|BCI/AI/Quantum SOTA 2026-09-04]]
- [[07_SKILLS/amos-provenance-trust-firewall/SKILL|Provenance Trust Firewall]]
- [[07_SKILLS/amos-k-binding/SKILL|K-Binding]]
- [[07_SKILLS/amos-k-memory-admission/SKILL|K_Memory_Admission]]
- [[07_SKILLS/amos-commit-time-gating/SKILL|Commit-time Gating]]
- [[07_SKILLS/amos-action-memory-firewall/SKILL|Action-Memory Firewall]]
- [[22_RESEARCH/01_PAPERS/ARXIV_2608_19701_CAMA_MEMORY_CORRELATION_BIAS|CAMA — Correlation-Aware Memory Arbitration]]
- [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]]
