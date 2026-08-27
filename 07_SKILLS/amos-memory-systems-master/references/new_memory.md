---
title: new memory
type: reference
tags: [reference, amos-memory-systems-master]
---

# New Memory

> Source: `_00_Cosmo brain/memory/New_Memory.md`
> Epistemic class: SOURCE_DERIVED

---
type: doc
title: AMOS Memory Architecture — New Memory, Working Memory, Evolution Memory
created: 2026-08-22
tags: [canon-group/biology, canon/framework, rscf/claim, rscf/provenance, rscf/state/source-claim, topic/new-memory, memory]
---

# AMOS Memory Architecture

The AMOS memory system is a multi-layered architecture that treats memory as coherence carried through transformation. It encompasses several distinct memory subsystems: the core Memory Architecture, Distinct Working Memory, Evolutionary and Anti-Regression Memory, and a Learning and Memory Fractal Architecture with 50 templates.

## Memory Architecture

### Principle

Memory is coherence carried through transformation.

### Memory State

`M = [origin, state_history, relation_history, mutation_lineage, repair_history, evidence_history, supersession, contradiction_history, provenance]`

### Retention Classes

| Class | Description |
|-------|-------------|
| HOT | Decision-active |
| WARM | Validated reusable capsule |
| COLD | Recoverable detail |
| QUARANTINED | Conflict/contamination/staleness |
| EXPIRED | Invalid in current regime |
| RAW_ARCHIVE | Exact source, do-not-load by default |

### Invariants

Preserve at all times:
- Objective
- Hard constraints
- Load-bearing premises
- Unresolved contradictions
- Provenance anchors
- Falsifiers
- Rollback points

Compression may remove repetition but not provenance, contradiction, scope, validity state, or repair history.

## Distinct Working Memory

Working memory separates three distinct carriers:

- **Recall-carried state** — information retrieved from long-term memory
- **Summary-carried state** — compressed representations of prior reasoning
- **Locality-carried state** — context-dependent environmental information

Do not count duplicate information across carriers as independent support.

Each working-memory slot records:
`[content, carrier, provenance, novelty, dependency_role, expiry, contradiction_state]`

## Evolutionary and Anti-Regression Memory

### Evolution Record

`ER = {parent, mutation, hypothesis, experiment, evidence, consequences, decision, authority, deployment, rollback, failure}`

### Key Principles

- **Rollback is not Forgetting**: Rejected or harmful changes retain a failure signature.
- Similarity to a prior failure increases scrutiny but does not automatically prove future failure.

## Learning and Memory Fractal Architecture

The learning and memory system uses a fractal architecture with 500,000 entries and 50 templates organized across 9 fractal scales.

### Core Law

Learning is the reduction of memory entropy through attention, meaning, repetition, feedback, retrieval, and transfer.

### Fractal Scales

signal, word, concept, chunk, lesson, skill, habit, identity, lifelong_system

### L/M/H Levels

| Level | Description |
|-------|-------------|
| L | Low learning: weak attention, poor encoding, high entropy, low recall |
| M | Functional but shallow: recognition without reliable recall or transfer |
| H | Deep learning: strong encoding, retrieval, transfer, validation, and identity integration |

### Key Templates (50 total)

| ID | Name | Formula | Layer |
|----|------|---------|-------|
| LM001 | attention_capture | AC = relevant_signal / total_signal | attention |
| LM004 | encoding_strength | ES = attention * meaning * emotion * repetition | encoding |
| LM007 | working_memory_load | WML = active_chunks / capacity | working_memory |
| LM011 | consolidation_strength | CS = sleep_quality * repetition * emotional_salience * low_interference | consolidation |
| LM012 | retrieval_strength | RS = cue_quality * encoding_strength * recency * frequency | retrieval |
| LM014 | forgetting_curve | F = initial_memory * exp(-decay_rate * time) | forgetting |
| LM020 | learning_update | LU = learning_rate * prediction_error * feedback_quality | learning |
| LM021 | transfer_score | TS = applied_correctly_new_context / learned_skill | transfer |
| LM027 | memory_entropy | ME = w1*interference + w2*schema_conflict + w3*retrieval_error + w4*attention_leak + w5*context_gap | entropy |
| LM048 | memory_integrity | MI = encoding * consolidation * retrieval * validation * (1-entropy) | integrity |
| LM049 | learning_quality | LQ = attention * encoding * feedback * retrieval_practice * transfer * (1-load) | quality |
| LM050 | final_mastery | Mastery = retention * transfer * speed * accuracy * metacognitive_accuracy | mastery |

### Learning Permission Rules

**Allow learning if**: attention_ok, load_balanced, feedback_quality_high, retrieval_practice_present, entropy_not_high.

**Block learning if**: overload, high_interference, illusion_of_knowing, wrong_feedback, attention_leak_high.

**Main goal**: Convert fragile recognition into validated recall, transfer, and mastery.

## Memory Write Agent

The MemoryWrite_Agent is a BRAIN_SYSTEM component that handles memory write operations. It is registered in the runtime registry and appends trace entries to the context. The default implementation is non-destructive: it ensures component registration, appends a trace entry, and returns the context unchanged to allow layering of real logic.

## Related Vault Sources

- `_00_Cosmo brain/memory/New_Memory.md` — Bridge note (original source)
- `_00_Cosmo brain/memory/MEMORY_ARCHITECTURE.md` — Core memory architecture with retention classes
- `_00_Cosmo brain/memory/WORKING_MEMORY.md` — Distinct working memory specification
- `_00_Cosmo brain/memory/EVOLUTION_MEMORY.md` — Evolutionary and anti-regression memory
- `_00_Cosmo brain/memory/learning_memory_architecture.md` — 50-template learning and memory fractal architecture
- `_00_Cosmo brain/memory/memory_write_agent.md` — Memory write agent component

---
**MOC:** [[references_MOC]]
