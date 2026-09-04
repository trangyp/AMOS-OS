---
title: "Mesh Memory Protocol — Semantic Infrastructure for Multi-Agent LLM Systems"
type: research_paper
source: arxiv
arxiv_id: "2604.19540"
url: "https://arxiv.org/abs/2604.19540"
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
epistemic_class: SOURCE_CLAIM
conclusion_class: DERIVED
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance:
    - arxiv:2604.19540
    - 22_RESEARCH/BCI_AI_QUANTUM_SOTA_2026-09-04
  scope: multi_agent_memory_protocol
tags:
  - research
  - arxiv
  - multi-agent
  - memory
  - protocol
  - provenance
  - identity
created: 2026-09-04
---

# Mesh Memory Protocol (MMP) — Semantic Infrastructure for Multi-Agent LLM Systems

> **arXiv:** [2604.19540](https://arxiv.org/abs/2604.19540)
> **Epistemic class:** `SOURCE_CLAIM` (production-deployed, 3 reference deployments)
> **AMOS bridge:** Memory Systems, Identity Canon, Action-Memory Firewall, Provenance

## Key result

A protocol-level semantic infrastructure for cross-session agent-to-agent cognitive collaboration. Solves three problems:

- **P1 (Field-level acceptance):** Each agent decides field-by-field what to accept from peers, not whole messages.
- **P2 (Provenance tracing):** Every claim is traceable to source; returning claims recognized as echoes of receiver's own prior thinking.
- **P3 (Relevance by storage, not retrieval):** Memory that survives session restarts is relevant because of how it was stored, not how it is retrieved.

Four composable primitives:
1. **CAT7** — fixed 7-field schema for every Cognitive Memory Block (CMB)
2. **SVAF** — evaluates each field against receiver's role-indexed anchors (realizes P1)
3. **Inter-agent lineage** — parents and ancestors of content-hash keys (realizes P2)
4. **Remix** — stores only receiver's role-evaluated understanding, never raw peer signal (realizes P3)

**Production-deployed** across 3 reference deployments with autonomous mesh-peer agents.

## AMOS bridge analysis

### Direct bridge to AMOS Memory Systems

| MMP primitive | AMOS equivalent | Bridge strength |
| :--- | :--- | :--- |
| CAT7 (7-field CMB schema) | AMOS typed memory atoms | Strong — both enforce structured memory encoding |
| SVAF (field-level evaluation) | AMOS memory admission gates | Strong — both filter at admission, not just retrieval |
| Inter-agent lineage (content-hash) | AMOS provenance chain | Strong — both require traceable source chains |
| Remix (role-evaluated understanding) | AMOS action-memory firewall | **Direct** — receiver stores own understanding, not raw peer signal |

### Direct bridge to AMOS Action-Memory Firewall

MMP's **remix** primitive is a direct implementation of AMOS Action-Memory Firewall:

```text
AMOS Action-Memory Firewall:
  "executed effects cannot silently become beliefs"
  action traces isolated from admitted memory

MMP Remix:
  "stores only the receiver's role-evaluated understanding
   of each accepted CMB, never the raw peer signal"
  peer signal (action/observation) → role evaluation → stored understanding
```

Both enforce: **raw external input ≠ admitted memory**. An intermediate evaluation step is required before persistence.

### Bridge to AMOS Identity Canon

MMP's inter-agent lineage with content-hash keys provides:
- Each agent has its own identity and memory
- Content is traceable to its origin agent
- Returning claims are recognized as echoes

This maps to AMOS Identity Canon's **identity continuity** requirement: an agent's memory export/import must preserve identity-integrity. MMP's production deployment provides empirical evidence that this is achievable.

### Bridge to AMOS K-Binding

MMP's field-level acceptance (SVAF) maps to AMOS K-Binding:
- AMOS K-Binding: validate, maintain, resolve, invalidate relationships between system objects
- MMP SVAF: evaluate each field against role-indexed anchors before accepting

Both enforce: **not all relationships are valid; binding requires validation**.

## Epistemic boundary

- MMP is `SOURCE_CLAIM` from a production-deployed system with 3 reference deployments. This is stronger than benchmark-only papers.
- The AMOS bridge is `AMOS_MODEL` — structural analogy between MMP primitives and AMOS memory architecture.
- MMP's 7-field schema (CAT7) is not the same as AMOS typed memory atoms; the mapping is structural, not literal.
- Production deployment scale and failure modes are not fully documented in the paper.

## Related

- [[22_RESEARCH/BCI_AI_QUANTUM_SOTA_2026-09-04|BCI/AI/Quantum SOTA 2026-09-04]]
- [[07_SKILLS/amos-memory-systems-master/SKILL|AMOS Memory Systems Master]]
- [[07_SKILLS/amos-action-memory-firewall/SKILL|Action-Memory Firewall]]
- [[07_SKILLS/amos-k-identity/SKILL|K-Identity]]
- [[07_SKILLS/amos-k-binding/SKILL|K-Binding]]
- [[07_SKILLS/amos-provenance-trust-firewall/SKILL|Provenance Trust Firewall]]
- [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]]
