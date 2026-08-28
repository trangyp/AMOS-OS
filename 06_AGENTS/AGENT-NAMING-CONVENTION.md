---
title: AGENT NAMING CONVENTION
type: note
source: 06_AGENTS
tags:
- note
- vault
- canon/agent
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


# AMOS Agent Naming Convention

> **Description**: Stable, logical, MECE naming rules for all `.devin/agents/` files.
> **Version**: 1.1.0 (2026-08-25)
> **Status**: Applied — all arXiv paper and dispatcher agents in `.devin/agents/` now use function-first, `arxiv`-free names.

---

## Naming Rule

```text
amos-{domain}-{function}-{qualifier}-agent.json
```

- **No `arxiv` in the agent file name.** ArXiv IDs appear only in the `source_id` or `arxiv_id` metadata field inside the agent JSON, not in the file name.
- **Domain**: pick one from the MECE groups below (e.g., `qic`, `math`, `blackhole`, `ai-ml`).
- **Function**: a verb or noun describing what the agent computes/answers.
- **Qualifier**: optional disambiguator (e.g., `hft-e`, `wse2`, `tripartite`).
- **Suffix**: always `-agent.json`.

## Examples

- `amos-qic-third-order-negativity-agent` — QIC, tripartite separability
- `amos-math-sheaf-descent-topoi-agent` — Math, sheaf descent on topoi
- `amos-blackhole-charged-spin-dynamics-agent` — QG, Schwarzschild + magnetic field
- `amos-qml-tilted-loss-vqa-agent` — QML, Quantum Tilted Loss for VQAs
- `amos-atom-supercurrent-accelerometer-agent` — Atom, atomtronic supercurrent
- `amos-ai-ml-paper-agent` — AI/ML paper dispatcher
- `amos-qfm-paper-catalog-agent` — Q/F/M paper catalog dispatcher

## MECE Grouping

- **QIC** — quantum information, entanglement, separability, measurement.
- **QEC** — quantum error correction, LDPC, fault tolerance.
- **QML** — quantum machine learning, VQA, barren plateaus, optimization.
- **QFT / QG** — quantum field theory, quantum gravity, black holes, cosmology.
- **CondMat / Atom** — condensed matter, atomtronics, many-body, QHE.
- **Optics / Sensing** — quantum optics, NV sensing, polarization, satellites.
- **Math** — category theory, topology, algebra, sheaves, TDA.
- **Fractal** — fractal geometry, combinatorial Loewner, scale-invariance.
- **CS / TDA / ML** — classical computer science, TDA, machine learning for physics.
- **Materials** — WSe2, strain, transport.
- **AI-ML / Bio-Health / ...** — arXiv subject dispatchers for non-Q/F/M papers.

## Migration Rule

- **New agents**: use function-first names.
- **Existing arXiv agents**: now renamed to function-first names.  
  ArXiv IDs retained only as JSON metadata (`source_id`, `arxiv_id`).
- **Skill + workflow names**: match the agent name; rename together.

---
**Related:** [[00_HOME]] · `amos-agent-registry-index.md` · `amos-qfm-paper-agents-index.md`

---
**MOC:** [[06_AGENTS_MOC]]
