---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Transformer Inference Efficiency Workflow Orchestration
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# Transformer Inference Efficiency — Workflow Orchestration

## Purpose

Route an efficiency question to the smallest sufficient lever set without loading every optimization Skill.

## Router

`OBJECTIVE -> BOTTLENECK -> LEVER OWNER -> MATCHED BASELINE -> SINGLE-LEVER TEST -> COMPOSITION TEST IF NEEDED -> STOP`

### Bottleneck routing

- KV-cache size / decode memory bandwidth → GQA and/or KV quantization.
- attention matrix work → sparse attention.
- context extension → RoPE scaling.
- exact dense attention kernel IO → FlashAttention.
- token-dependent depth compute → Mixture-of-Depths.
- attention replacement / recurrent sequence dynamics → selective SSM.

## Composition gate

Compose levers only when the single-lever result leaves a decision-relevant bottleneck.

For any composition record:
- ordering;
- shared state;
- interaction assumptions;
- benchmark baseline;
- failure attribution;
- rollback path.

## Stop rule

Stop when:
1. the target bottleneck is no longer load-bearing, or
2. marginal expected decision value of another lever is lower than test/integration cost.

## Validation boundary

`INDIVIDUAL BENCHMARK PASS != COMPOSED BENCHMARK PASS`

`MODEL QUALITY RETAINED != SYSTEM LATENCY IMPROVED`

`PREFILL WIN != DECODE WIN`

## Authority

This workflow proposes and evaluates optimization paths. Release/deployment remains separately authorized.
