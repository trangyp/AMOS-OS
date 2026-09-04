---
title: "CAMA — Correlation-Aware Memory Arbitration for Multi-Agent Systems"
type: research_paper
source: arxiv
arxiv_id: "2608.19701"
url: "https://arxiv.org/abs/2608.19701"
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
epistemic_class: SOURCE_CLAIM
conclusion_class: DERIVED
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance:
    - arxiv:2608.19701
    - 22_RESEARCH/BCI_AI_QUANTUM_SOTA_2026-09-04
  scope: multi_agent_memory_arbitration
tags:
  - research
  - arxiv
  - multi-agent
  - memory
  - sybil-hardening
  - provenance
created: 2026-09-04
---

# CAMA — Correlation-Aware Memory Arbitration

> **arXiv:** [2608.19701](https://arxiv.org/abs/2608.19701)
> **Epistemic class:** `SOURCE_CLAIM` (peer-reviewed preprint)
> **AMOS bridge:** K-Sybil-Hardening, Memory Systems, Provenance Trust Firewall

## Abstract summary

Long-term multi-agent systems accumulate memories from different agents. Existing methods treat retrieved memories as independent evidence and combine them via voting or weighting. This independence assumption fails when memories share upstream sources or bias, creating **Memory Correlation Bias** — correlated evidence counted repeatedly, forming a false majority.

CAMA (Correlation-Aware Memory Arbitration) jointly:
1. Decouples retrieved memories by modeling them as query-conditioned evidence groups
2. Recovers missing independent evidence via neural dependency inference + provenance-based symbolic priors
3. Estimates effective number of independent evidence sources
4. Learns a sequential recovery policy that actively retrieves alternative evidence or traces upstream sources

## Key results

- Outperforms SOTA baselines on multiple benchmarks
- Suppresses false majorities induced by correlated memories
- Sequential recovery policy minimizes retrieval cost while recovering sufficient independent evidence

## AMOS bridge analysis

### Direct bridge to K-Sybil-Hardening

CAMA's **Memory Correlation Bias** is the multi-agent generalization of AMOS K-Sybil-Hardening:

```text
AMOS K-Sybil-Hardening:
  "apparent multiplicity ≠ independent epistemic support"
  one origin represented as many sources → false independence

CAMA Memory Correlation Bias:
  memories from different agents sharing upstream source → false majority
  correlated evidence counted as independent → inflated confidence
```

Both enforce the same invariant: **count independent sources, not apparent instances**.

### Bridge to Provenance Trust Firewall

CAMA's provenance-based symbolic priors mirror AMOS Provenance Trust Firewall:
- CAMA traces upstream sources to determine independence
- AMOS Provenance Trust Firewall validates that provenance chains are independent before trusting aggregated evidence

### Bridge to Memory Systems

CAMA's sequential recovery policy maps to AMOS Memory Systems:
- AMOS: encode → consolidate → retrieve → utilize
- CAMA: retrieve → detect correlation → recover alternative evidence → arbitrate

The recovery policy is an AMOS-style "fail-closed → active repair" pattern: when initial retrieval lacks sufficient independent evidence, the system does not accept the false majority but actively seeks more.

## Epistemic boundary

- CAMA is validated on benchmark datasets, not AMOS runtime. Its results are `SOURCE_CLAIM` for the multi-agent memory domain.
- The AMOS bridge is `AMOS_MODEL` — a structural analogy, not an empirical validation of AMOS mechanisms.
- CAMA's dependency inference is approximate; it does not guarantee detection of all correlated sources.

## Related

- [[22_RESEARCH/BCI_AI_QUANTUM_SOTA_2026-09-04|BCI/AI/Quantum SOTA 2026-09-04]]
- [[07_SKILLS/amos-k-sybil-hardening/SKILL|K-Sybil-Hardening]]
- [[07_SKILLS/amos-provenance-trust-firewall/SKILL|Provenance Trust Firewall]]
- [[07_SKILLS/amos-memory-conflict-governor/SKILL|Memory Conflict Governor]]
- [[07_SKILLS/amos-memory-immune-system/SKILL|Memory Immune System]]
- [[22_RESEARCH/22_RESEARCH_MOC|22_RESEARCH_MOC]]
