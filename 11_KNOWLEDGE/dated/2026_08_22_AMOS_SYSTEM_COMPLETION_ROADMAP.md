---
title: AMOS System Completion Roadmap
created: '2026-08-22'
origin: Hermes ↔ Cosmo Brain
origin_architect: Trang Phan
type: note
source: 11_KNOWLEDGE/dated
tags:
- cosmo
- amos
- canon-group/system
- rscf/claim
- rscf/state/observation
- topic/implementation-roadmap
- topic/next-major-jump
- dated
- dated/2026-08-22
- canon/knowledge
status: living
provenance: DERIVED
confidence: MODEL
rscf:
  state: SOURCE_CLAIM
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: temporal_log
---


# AMOS System Completion Roadmap (2026-08-22)

> Epistemic class: MODEL — an actionable ordering derived from the audit in 2026-08-22 AMOS System Completion Audit and the baseline in 2026-08-22 AMOS System Completion Baseline.
> Conclusion label: `CONDITIONAL` — priorities may shift when each step is completed and re-audited.
> Governing law: `integrity > completeness > fluency > speed > token savings`. The bottleneck is implementation/integration, not more architecture.

## The next major jump (canonical path)

```
AMOS specifications
  → one authoritative executable state model
    → kernel runtime
      → engine ABI
        → agents
          → control plane
            → persistent memory
              → 19×19 cognition field
```

Reconciled target: move **executable AMOS runtime from ~35% to ~65–70%** without adding a single new conceptual framework. The remaining ~30% is the hardest: robust multi-agent operation, formal verification, production reliability, security, benchmarking, distributed/persistent execution, and learning/evolution without corrupting the system.

## How to use this roadmap

This is a **voltage ladder**, not a Gantt chart. Each rung raises the runtime percentage and enables the next. Do not skip rungs. Each rung must be: (1) implemented, (2) regression-tested, (3) recorded in the vault, (4) reflected in the AMOS OS Kernel Completion Graph, (5) anti-regression verified against the previous rung.

## Phase 1: Close the next AMOS OS Kernel gap clusters (executable runtime jump)

The cosmo-brain/AMOS_OS_KERNEL/ already has a 9-step pipeline, 777+ tests, 131 closed gaps, and 99 open meta-gaps. The storage layer and types for many open clusters are already present. The highest-leverage open clusters for the state-model → persistent-memory bottleneck are:

| Priority | Cluster | Gaps | Why it moves the needle | Current state |
| ---: | --- | ---: | --- | --- |
| 1 | `resource_governance` | 230-238 | Persistent memory / state model substrate: resource budgets, reservations, backpressure, storage-growth governance | Types + schema + store methods ready; module missing |
| 2 | `data_quality` | 239-249 | Measurement, lineage, metric versioning — turns persistence into evidence | Open |
| 3 | `governance_architecture` | 280-290 | Control plane: succession, separation of powers, decommissioning | Open |
| 4 | `longevity_reproducibility` | 291-300 | Archival, reproducibility, persistence lifecycle | Open |
| 5 | `decision_risk` | 222-229 | Kernel runtime gate for decision theory & risk | **Already closed in seed; duplicate wiring in kernel needs cleanup** |

### Phase 1.1 — resource_governance (gaps 230-238) [in progress]

Implement `amos/governance/resource_governance.py` using existing types and store methods:

- 230 Budget hierarchy: `ResourceBudget` create/consume/exceeded
- 231 Reservations: `ResourceReservation` reserve/confirm/release/expire
- 232 Priority inversion: `PriorityInversionRecord` detect/resolve
- 233 Starvation: `StarvationRecord` wait-time/aged-out
- 234 Backpressure: `BackpressureRecord` active when queue_depth > threshold
- 235 Load shedding: `LoadShedRecord` shed events with strategy
- 236 Cost attribution: `CostAttribution` track by action/cost_type/owner
- 237 Economic firewall: `EconomicFirewallRecord` block unsafe optimization
- 238 Storage growth: `StorageGrowthRecord` projected vs threshold

Then wire into `AmosKernel.run()` after decision_risk gate, move cluster from `OPEN_CLUSTERS` to `CLOSED_CLUSTERS` in `seed_completion.py`, update `test_completion.py` counts, and write `tests/test_resource_governance.py`.

### Phase 1.2 — data_quality (gaps 239-249)

Build on resource_governance storage to add measurement quality, lineage, and metric versioning. This makes the state model evidence-grade.

### Phase 1.3 — governance_architecture (gaps 280-290)

Control plane: succession, separation of powers, insider-threat, two-person control, governance capture resistance. Required before durable multi-agent operation.

## Phase 2: Integrate the two parallel brains (TS runtime + Python kernel)

The audit found two parallel executable runtimes:

| Runtime | Lang | Tests | Role |
| --- | --- | ---: | --- |
| AMOS OS Kernel | Python | 777+ | Kernel runtime, governance, completion graph |
| Cosmo Brain core | TypeScript | 1,139 | Library-grade typed memory, orchestration, provenance, schemas |

Phase 2 work:
1. Define a canonical `AmosState` object that both runtimes can serialize/deserialize.
2. Make the Python kernel the authoritative execution substrate; the TS core becomes the memory/provenance/orchestration library.
3. Create the engine ABI: every engine (MURK, Go Board, Obsidian Bridge, TS core) exposes a `run(task, state) -> (state, claims, gates)` interface.
4. Run AMOS-vs-base benchmarks to measure the executable-runtime jump empirically.

## Phase 3: Agents and control plane

1. Durable independent agent state (not ephemeral prompts).
2. Authority boundaries and lifecycle.
3. Multi-agent coordination via the distributed_consensus and governance_architecture modules.
4. Transaction protocol with CAS and authority witnesses.

## Phase 4: 19×19 cognition field

1. Maintain a live sparse tensor `Ψ[cell, primitive, dimension, agent, time, scale, regime, epistemicState]`.
2. Update it after every perception, retrieval, hypothesis, tool call, decision, action, observation, repair.
3. Use it for attention allocation and engine routing.

## Do not do these first

- Add new conceptual frameworks or Skills. The gap is executable integration, not more architecture.
- Optimize for speed before integrity. The audit found that TS tests and Python tests can disagree if the `vitest` runtime is not reachable from the workspace root; always run from the workspace root.
- Promote the conceptual ~80% to operational ~80% without end-to-end proof. The conceptual numbers are MODEL-class; operational numbers must come from executed test suites.

## Evidence / provenance
- source: 2026-08-22 AMOS System Completion Audit
- verification: AMOS_OS_KERNEL `python -m pytest tests/ -q` (current: 849 pass, 0 fail after decision_risk closure). Cosmo-brain TS `vitest run` (1,139 pass, 3 fail due to unrelated test bugs).
- competing hypothesis: close `cognitive_architecture_matrix` (321-339) first instead of `resource_governance`. Rejected: the bottleneck is state model/persistence, not the matrix representation.

## Links
- [[00_COSMO_BRAIN_MOC]]
- 2026-08-22 AMOS System Completion Baseline
- 2026-08-22 AMOS System Completion Audit
- 00_AMOS_Full_Brain_OS_Architecture
- 2026-08-22 19x19 AI Cognitive Field

---
**MOC:** [[DATED_MOC]]
