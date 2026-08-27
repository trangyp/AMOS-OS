---
title: SKILL
type: skill
name: amos-learning-memory-knowledge-feedback-governor
description: Learning-Memory-Knowledge Feedback Governor — cross-domain capability bridging C05 Mind & Behavior (inference/learning), Memory Systems (encode/consolidate/retrieve), and Knowledge Research (index/curate/retrieve). Governs the unified feedback loop: C05 inference → encode → Memory → consolidate → Knowledge → retrieve → C05 inference. Enforces epistemic preservation across domain transitions, requires 2+ corroborating entries for consolidation, validates knowledge freshness before application, and traces full provenance chains across the loop. Use when learning outcomes need to be encoded to memory, memory entries need to be consolidated to knowledge, knowledge needs to be retrieved to inform new inference, or the full feedback loop needs governance. Use when amos-knowledge-research-master routes to this specialized capability.
parent_skill: amos-knowledge-research-master
domain: cross-domain (C05 → Memory → Knowledge)
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-learning-memory-knowledge-feedback-governor]
---


# Learning-Memory-Knowledge Feedback Governor

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-knowledge-research-master`
- **Domain**: cross-domain (C05 Mind & Behavior → Memory Systems → Knowledge Research)
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from C05, Memory, and Knowledge master knowledge files)

Bridges the learning-memory-knowledge feedback loop across three AMOS domains. C05 produces inference and learning outcomes. Memory Systems provides encode, consolidate, and retrieve operations with working/episodic/semantic stores. Knowledge Research provides ingest, index, curate, and retrieve operations with the 68,979-note Obsidian vault. This governor ensures that learning flows to memory, memory consolidates to knowledge, and knowledge returns to inform new inference — with epistemic class preserved and provenance traced across every transition.

## The Problem This Skill Solves

The `_00_Cosmo brain` exploration explicitly identified: *"Learning and Memory and Knowledge: Learning platforms, memory architecture, and knowledge indexes are separate domains without unified learning-memory-knowledge feedback loops."*

Specifically:

1. **C05's inference loop produces learning but has no bridge to memory encoding** — inference outcomes are lost unless explicitly captured
2. **Memory Systems has encode/consolidate/retrieve but has no bridge to knowledge indexing** — memory entries remain local, never becoming queryable knowledge
3. **Knowledge Research has ingest/index/curate but has no bridge back to C05's inference loop** — indexed knowledge is not automatically retrieved to inform new reasoning
4. **No unified feedback loop connects all three domains** — each operates in isolation, losing learning over time

## The Feedback Loop

```text
C05 Inference
    → ENCODE → Memory Systems (working → episodic → semantic)
    → CONSOLIDATE → Knowledge Research (index, curate, retrieve)
    → RETRIEVE → C05 Inference context
    → APPLY → New C05 Inference
    → (loop repeats)
```

The loop has 4 transition types:

- **ENCODE**: C05 inference results to typed memory entries (working memory first, then episodic)
- **CONSOLIDATE**: Memory entries to indexed knowledge (requires 2+ corroborating entries)
- **RETRIEVE**: Knowledge entries to C05 inference context (validated for freshness)
- **APPLY**: Retrieved knowledge informs new inference (scope/regime checked)

## When to Use

- When C05 inference outcomes need to be encoded into Memory Systems
- When memory entries need to be consolidated into the Knowledge Research vault
- When indexed knowledge needs to be retrieved to inform new C05 inference
- When governing the full feedback loop (LOOP_PERMITTED / BLOCKED / CONDITIONAL)
- When detecting knowledge drift (stale entries, broken provenance, class erosion)
- When validating that epistemic class is preserved across domain transitions
- When tracing the full provenance chain across the learning-memory-knowledge loop
- When the parent skill (`amos-knowledge-research-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **lmk_feedback.encode_learning**: Encode C05 inference outcome into Memory Systems. Maps inference results to typed memory entries (working → episodic → semantic). Preserves epistemic class from inference. Returns memory entry ID + provenance chain.
- **lmk_feedback.consolidate_to_knowledge**: Consolidate memory entries into indexed Knowledge Research vault. Requires 2+ corroborating memory entries from independent inference episodes. Produces indexed knowledge artifact