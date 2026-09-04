---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Transformer Inference Efficiency Skill Stack
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

# Transformer Inference Efficiency — MECE Skill Stack

## 1. Purpose

Separate transformer/sequence-model efficiency levers by the system variable they actually change.
"Efficiency" is an outcome class, not a semantic owner.

## 2. Primary ownership

### E1 — Attention head topology
Owner: `arxiv-grouped-query-attention-rscf`

Changes `q_heads <-> kv_heads <-> grouping`. Does not own precision, sparsity, positions or kernels.

### E2 — KV numerical precision
Owner: `arxiv-kv-cache-quantization-rscf`

Changes cache precision, scale/metadata and residual full-precision windows.

### E3 — Attention edge topology / sparsity
Owner: `arxiv-sparse-attention-scaling-rscf`

Changes which query-key interactions are computed/retained.

### E4 — Positional/context coordinate transform
Owner: `arxiv-long-context-rope-scaling-rscf`

Changes positional-frequency/context mapping. Does not reduce dense-attention work by itself.

### E5 — Exact-attention IO/kernel execution
Owner: `arxiv-flash-attention-io-rscf`

Changes tiling, memory traffic, partitioning and fused exact-attention execution.

### E6 — Conditional depth
Owner: `arxiv-mixture-of-depths-rscf`

Changes which tokens traverse which layer/depth compute.

### E7 — Alternative sequence dynamics
Owner: `arxiv-selective-state-space-rscf`

Changes attention-vs-state-space sequence mechanism and selective recurrent dynamics.

### E8 — KV retention / eviction policy
Evidence owner: `22_RESEARCH/RSCF_TECH_RANDOM_ATTENTION_KV_EVICTION_2609_03430_PARTIAL`

Changes which stored prompt/generated KV states remain available under a cache budget.

This is currently a **research-bound architecture lever**, not a claim that a dedicated reusable Skill owner
has been behaviorally validated.

Hard distinction:

```text
KV PRECISION != KV RETENTION POLICY
ATTENTION SPARSITY != CACHE EVICTION
PROMPT CACHE != GENERATED REASONING CACHE
SELECTION COMPLEXITY != SELECTION VALUE
CACHE REDUNDANCY != SEMANTIC IRRELEVANCE
```

### E9 — Runtime cache placement / persistence / offload
Primary physical owner: `04_RUNTIME` with `14_TOOLS`/host dependencies.

Changes where cache state lives and how it is restored/moved across device/host/session boundaries.
This is a cross-plane runtime lever rather than a Skill-family semantic owner unless a specific capability
package is selected.

```text
CACHE POLICY != CACHE PLACEMENT
CACHE RESTORE != MEMORY TRUTH
PERSISTENT KV != PERSISTENT SEMANTIC MEMORY
```


### E10 — Runtime KV scheduling / reservation / routing
Primary physical owner: `04_RUNTIME` with `14_TOOLS`, scheduler and serving-system dependencies.

Changes **when** KV capacity is reserved, expanded, reclaimed, migrated, preempted, or assigned across
requests / request classes / serving groups.

This is distinct from:
- structural representation/retention;
- spatial placement/migration;
- semantic context meaning.

Current system-aware KV serving research supports a three-behavior decomposition:

```text
TEMPORAL
= execution / scheduling / reservation / preemption / routing

SPATIAL
= placement / migration / offload / disaggregation

STRUCTURAL
= representation / precision / compression / retention / eviction
```

The three axes may interact, but none substitutes for another.

```text
KV RESERVATION != KV RETENTION
KV ROUTING != KV PLACEMENT
KV PLACEMENT != KV SEMANTIC IMPORTANCE
OUTPUT-LENGTH UNCERTAINTY != MODEL UNCERTAINTY
PREEMPTION RISK != ANSWER RISK
```

A runtime allocator must bind the workload/SLO regime and include the cost of over-reservation,
under-reservation, recomputation/preemption, queueing, transfer, and quality changes.


## 3. Cross-cutting outcome tensor

```text
EFF[
  model,
  checkpoint,
  lever,
  phase,
  prompt_or_generated_state,
  seq,
  batch,
  dtype,
  cache_budget,
  cache_policy,
  placement,
  reservation_policy,
  scheduler,
  request_class,
  output_length_uncertainty,
  preemption_policy,
  hardware,
  runtime,
  memory_bytes,
  bandwidth,
  flops,
  ttft,
  tpot,
  latency,
  tail_latency,
  throughput,
  power,
  energy_per_request,
  quality,
  adaptation_cost,
  selector_overhead,
  recovery_cost,
  provenance,
  status
]
```

## 4. Composition rule

Multiple levers may compose, but gains are not additive by default.

`Gain(E1+E2+...)=MEASURED_COMPOSITION`, not `sum(individual gains)`.

Load-bearing interactions include:

- GQA changes KV-cache size and therefore quantization/eviction benefit;
- quantization can alter selector statistics or recovery cost;
- sparse attention changes kernel regularity and exact-attention kernel applicability;
- RoPE extension changes sequence regime and magnifies cache/attention costs;
- MoD shifts compute bottlenecks across layers;
- SSM alternatives change the execution topology;
- retention policy changes memory traffic and may shift the bottleneck into selection metadata or host transfer;
- cache placement/offload can dominate an otherwise faster kernel.

## 5. Prompt / generated-state separation

Current Sep-4 Random Attention evidence makes this distinction explicit:

```text
PROMPT / INSTRUCTION STATE
!= GENERATED REASONING STATE
```

A cache policy should type which class it is compressing or evicting. A policy that works when prompt tokens
are protected is not licensed for prompt eviction.

The current source reports workload-specific benchmark/serving results and remains partial normalization;
it does not establish a universal random-eviction law.

## 6. Benchmark identity

Every material efficiency result should bind:

```yaml
inference_benchmark:
  model:
  checkpoint:
  task_or_workload:
  quality_metric:
  prompt_length:
  generated_length:
  batch_or_concurrency:
  phase: prefill | decode | mixed
  dtype:
  kv_heads:
  cache_precision:
  cache_budget:
  eviction_policy:
  prompt_protection:
  attention_sparsity:
  positional_method:
  depth_routing:
  kernel:
  runtime:
  hardware:
  memory_bytes:
  selector_overhead:
  transfer_or_offload:
  reservation_policy:
  scheduler:
  request_class:
  output_length_uncertainty:
  preemption_or_recompute_cost:
  ttft:
  tpot:
  throughput:
  power_or_energy:
  baseline:
  provenance:
```

## 7. Benchmark invariants

1. Match model/checkpoint/quality target where possible.
2. Separate prefill, decode, training and backward regimes.
3. Report actual memory bytes, not nominal bits alone.
4. FLOPs, bandwidth, latency, TTFT, TPOT and throughput are separate.
5. Hardware/software/kernel/runtime versions are part of benchmark identity.
6. Quality retention is task/distribution/cache-budget bounded.
7. End-to-end system speedup cannot be inferred from one optimized kernel.
8. Selector/metadata cost belongs in cache-policy accounting.
9. Prompt protection is a load-bearing condition when the method assumes it.
10. Persistent/offloaded cache must include transfer/restore latency and memory boundary.
11. Power/energy claims require a declared measurement boundary.
12. Scheduling/reservation results must report workload distribution, SLO and preemption/recompute accounting.
13. Temporal, spatial and structural KV optimizations must not be reported as one interchangeable `cache optimization` class.

## 8. Failure / gap states

- `QUALITY_TARGET_NONCOMPARABLE`
- `CACHE_BUDGET_NONCOMPARABLE`
- `PROMPT_REASONING_CLASS_COLLAPSE`
- `SELECTOR_OVERHEAD_OMITTED`
- `RUNTIME_VERSION_UNKNOWN`
- `MEMORY_BYTES_UNMEASURED`
- `HOST_TRANSFER_UNACCOUNTED`
- `KERNEL_GAIN_PROMOTED_TO_SYSTEM_GAIN`
- `THROUGHPUT_WITHOUT_LATENCY`
- `POWER_BOUNDARY_UNDEFINED`
- `BENCHMARK_TO_PRODUCTION_SCOPE_LEAK`
- `COMPOSITION_INTERACTION_UNMEASURED`
- `OUTPUT_LENGTH_UNCERTAINTY_UNMODELED`
- `RESERVATION_POLICY_OMITTED`
- `PREEMPTION_RECOMPUTE_COST_OMITTED`
- `TEMPORAL_SPATIAL_STRUCTURAL_KV_COLLAPSE`

## 9. Full Brain ownership

- Skill semantics → `07_SKILLS`
- composition/order → `26_WORKFLOWS`
- current model/cache state → `12_STATE` + `13_MODELS`
- runtime/cache placement and measured serving behavior → `04_RUNTIME`
- hardware/effect adapter → `14_TOOLS`
- typed crossing → `15_INTERFACES`
- runtime metrics → `17_OBSERVABILITY`
- executable benchmark evidence → `19_TESTS`
- external paper claims → `22_RESEARCH`
- deployment/release authority → `03_CONTROL_PLANE`

`EFFICIENCY CLAIM != DEPLOYMENT VALIDITY`.

## 10. Conclusion

`DERIVED / AMOS_MODEL`.

The stack now separates ten materially different efficiency levers and binds current KV-retention evidence
without promoting one research paper into a universal runtime law or a new Full-Brain peer.
