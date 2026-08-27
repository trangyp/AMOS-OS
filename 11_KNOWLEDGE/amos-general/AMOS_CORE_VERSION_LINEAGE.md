---
title: "AMOS Core Version Lineage"
created: "2026-08-22"
origin: "AMOS_CORE_ALL_VERSIONS_EXHAUSTIVE_MASTER.json"
origin_architect: "Trang Phan"
type: "reference"
tags: [canon-group/human-system, canon/metric, rscf/claim, rscf/provenance, rscf/state/observation, topic/amos-core-version-lineage, amos-general]
status: "active"
provenance: "VERIFIED"
confidence: "VERIFIED"
source: "Google Drive — AMOS_CORE_ALL_VERSIONS_EXHAUSTIVE_MASTER.json (compiled 2026-08-14)"
---

# AMOS Core Version Lineage

**16 versions** from v3.0 (Deterministic Reasoning Kernel) to v4.4 (Coordination Avoidance Runtime).  
**Total embedded source**: 3,687,308 bytes UTF-8.  
**Origin**: Trang Phan, compiled 2026-08-14.

---

## Evolution Spine

| Version | Title | Key Innovation |
|---------|-------|----------------|
| v3.0 | Deterministic Reasoning Kernel | Core-19 logic, rewrite system, knowledge base, entailment, contradiction detection |
| v3.1 | Logic Fixed | Canonical contradiction handling, deterministic SAT-backed classical fragment, meta-logic fallback |
| v3.2.1 | RSCF HML Recursive Runtime | Recursive RSCF state, H/M/L alignment, scale translation, entropy, future debt, repair, collapse/regeneration |
| v3.3 | Governed Meta-Evolution Runtime | Recursive depth, consequence radius, irreversibility, external governance hash, self-modification gates |
| v3.4.1 | Distributed Causal Evolution Runtime | Runtime-parent lineage binding, exact transition binding, causal clocks, deterministic distributed reconciliation |
| v3.5 | Epistemic Regime Lineage Runtime | Environment hash, regime epoch, evidence hash/epoch, validity windows, falsifiers, revalidation states |
| v3.6 | Competing Hypothesis Field Runtime | Separation of truth state and governance action state, partial-order hypothesis dominance, COMPETING/GAP preservation |
| v3.7 | Provenance Topology Runtime | Evidence lineage topology, derived independence, source/root/method/dataset relations |
| v3.7.1 | Provenance Topology Hardened Runtime | Root-content fingerprints, Sybil alias collapse, cycle/missing-parent/equivocation rejection |
| v3.8 | Iterative Provenance Runtime | Iterative stack/topological traversal, memoized ancestry, deep provenance without Python recursion |
| v3.9 | Persistent Incremental Provenance Runtime | Persistent live graph, localized cycle checks, dependency-aware invalidation, versioned hashes, copy-on-write |
| v4.0 | MVCC Causal Concurrency Runtime | Immutable snapshots, exact CAS, deterministic same-target conflict reconciliation, versioned rollback |
| v4.1 | Transactional Multi-RSCF Runtime | Transaction IDs, read/write sets, transaction-level CAS, atomic publication, cross-RSCF invariants |
| v4.2 | Deterministic Causal Epoch Runtime | Quorum certification, causal epochs, closed membership, deterministic conflict ordering, compact epoch encoding |
| v4.3 | Hardened Adaptive Epoch Runtime | Derived required shard set, transaction-ID immutable payload binding, shard-local copy-on-write finalization, epoch-bundle compression |
| v4.4 | Coordination Avoidance Runtime | Proof-of-independence fast lane, local finalization for disjoint causal cones, automatic escalation for overlap/uncertainty |

---

## Capability Matrix

| Capability | Introduced | Hardened/Notes |
|------------|------------|----------------|
| Logic | v3.0 | Repaired v3.1 |
| Recursive RSCF + HML scale runtime | v3.2.1 | — |
| Meta-evolution governance | v3.3 | — |
| Distributed causal lineage | v3.4.1 | — |
| Environment + epistemic regime lineage | v3.5 | — |
| Competing hypotheses without forced collapse | v3.6 | — |
| Evidence provenance topology | v3.7 | Hardened v3.7.1 |
| Deep iterative provenance | v3.8 | — |
| Persistent incremental graph | v3.9 | — |
| MVCC snapshot + CAS | v4.0 | — |
| Atomic multi-RSCF transactions | v4.1 | — |
| Causal epoch finality | v4.2 | — |
| Epoch hardening + shard-local finalization | v4.3 | — |
| Coordination avoidance fast lane | v4.4 | No numeric benchmark post-promotion |

---

## Benchmark History (key results)

### v3.0 — FAILED (targeted logic benchmark)
- Contradiction corpus (2000): 8/61 correct, 53 missed, 28 false positive → **precision 22.2%, recall 13.1%**
- Entailment corpus (1000): 13/174 correct, 161 missed, 18 false positive → **precision 41.9%, recall 7.5%**
- Deterministic replay: 10000/10000 ✓

### v3.1 — PASSED (tested boolean fragment)
- Contradiction corpus: **2000/2000 agreement, 61/61 contradictions, 0 false positives, 0 misses**
- Entailment corpus: **1000/1000 agreement, 174/174 valid, 0 false positives, 0 misses**
- Deterministic replay: 10000/10000 ✓
- **Boundary**: 100% refers only to tested propositional fragment against SymPy SAT

### v3.2.1 — PASSED (recursive structural suite)
- Valid scale translations: 50000/50000 ✓
- Identity corruption detected: 50000/50000 ✓
- Recursive tree closure: 100/100 (depth 5, 121 nodes/tree) ✓
- False repair recoveries: 0 ✓
- Local improvement global degradation: 69851/100000 — all rejected ✓
- Boolean + entailment regression: 2000/2000 + 1000/1000 ✓

### v3.3 — PASSED (meta-governance suite)
- Random meta mutations: 250,000 — 0 constitutional M0 accepted
- Targeted depth 2-5 attacks: 100,000 — 0 escapes
- Recursive chains: 1000 chains × 50 changes — 0 governance hash drift
- Deterministic replay mismatch: 0 ✓

### v3.4.1 — PASSED (distributed causal suite)
- Concurrent pairs: 100,000 — 0 order-dependent final states
- Stale parent mutations: 50,000 — 0 stale accepted
- Byzantine attacks: 40,000 — 0 escapes
- Logic regression mismatches: 0/10000 ✓

### v3.5 — PASSED then FAILED (conflicting truth)
- Prior regime shift stale acceptance fixed: 67085/67085 → 0 after fix ✓
- **Failure**: 20,000 equal high-quality incompatible pairs — all prematurely collapsed

### v3.6 — PASSED (competing hypothesis suite)
- Equal incompatible hypotheses: **20000/20000 remained COMPETING** ✓
- Premature collapses: 0 ✓
- True epistemic dominance: 20000/20000 ✓
- Authority changed truth status: 0 ✓
- Deterministic replay: 10000/10000 ✓

### v3.7 — Provenance fix then hardened
- Correlated poisoning cases: 5000 — 0 poisoned incorrectly dominant ✓

### v3.7.1 — PASSED (hardened provenance)
- Sybil provenance attacks: 5000 — 0 incorrectly dominant ✓
- Provenance cycles: 1000/1000 rejected ✓
- Hot resolution: mean 412.7μs, median 329.1μs, p95 647.5μs, throughput 2423/sec
- **Known gap**: depth_3000 → FAIL RecursionError

### v3.8 — PASSED (deep iterative provenance)
- Depth 3000/10000/50000/250000: all PASS ✓
- Million node star: PASS (build 8.44s, full profile 4.89s)
- Single new node rebuild: 8.6s
- Peak RSS: ~1.9 GB

### v3.9 — PASSED then FAILED (overlapping concurrency)
- Million node single add: mean 0.019ms, median 0.0097ms ✓
- Global root change (1M nodes): 368ms
- Independent concurrent additions: 100000/100000 ✓
- **Failure**: 2000 overlapping conflict trials — schedule-dependent winner distribution (A:977, B:1023)

### v4.0 — PASSED then FAILED (multi-RSCF atomicity)
- Same target conflict: 2000/2000 same winner ✓
- Commit throughput: 5792/sec; staging throughput: 19075/sec
- **Failure**: 2000/2000 multi-RSCF partial mixed trials FAIL

### v4.1 — PASSED (transactional multi-RSCF)
- Overlapping transaction trials: 2000 — 0 partial mixed states, 0 atomicity violations
- Transaction sizes passed: [3, 10, 100, 1000] ✓
- Forced partial failure rollback: passed ✓

### v4.2 — PASSED then hardened
- Conflicting certified pairs: 20000 — 0 arrival-order-dependent final states ✓
- Byzantine invalid state attacks: 10000 — 0 forged quorum acceptance ✓
- Optimized distributed: mean 0.35ms, median 0.31ms, p95 0.49ms, p99 0.88ms
- Throughput: 2800 finalized/sec; epoch serialized reduction: ~62%

### v4.3 — PASSED (hardening + sparse finalization)
- Latency reduction: v4.2 sparse 39.4ms → v4.3 sparse 0.52ms (**75.8× reduction, 98.7%**)
- Epoch bundle serialized byte reduction: ~82%
- Benchmark state: 100 shards × 1000 keys = 100,000 keys

### v4.4 — PROMOTED (coordination avoidance)
- Proven local transactions: fast lane ✓
- Overlapping active footprints: blocked from racing through fast lane ✓
- Cross-shard scope: clean handoff to coordinated epoch path ✓
- **Known gap**: No numeric benchmark report after promotion

---

## Known Gaps Across Lineage

1. **v3.0**: Original contradiction rewrite cycle and insufficient propositional entailment semantics
2. **v3.1**: Higher structural runtime layers not yet executable
3. **v3.2.1**: Meta-evolution/governance depth not yet first-class
4. **v3.3**: Distributed stale-state, target-binding, and concurrent merge semantics
5. **v3.4.1**: Authorization validity not bound to changing environment/evidence regime
6. **v3.5**: Equal high-quality incompatible hypotheses prematurely collapsed by deterministic ranking
7. **v3.6**: Evidence independence supplied as scalar rather than verified from provenance topology
8. **v3.7**: Sybil fake-origin aliases sharing identical root payload could regain artificial independence
9. **v3.7.1**: Recursive Python traversal failed around depth ~3000
10. **v3.8**: Million-node local changes still triggered whole-graph reconstruction
11. **v3.9**: Concurrent overlapping writes remained execution-order dependent; no MVCC/CAS snapshot semantics
12. **v4.0**: Multi-RSCF transactions reconciled per target, allowing partial mixed transaction state
13. **v4.1**: Distributed transaction finality under partition and competing certified transactions
14. **v4.2**: Caller-supplied shard subset could omit touched shard; transaction-ID equivocation across disjoint payloads
15. **v4.3**: Independent transactions still paid epoch coordination overhead
16. **v4.4**: No later hard-test result available after promotion; future limits untested

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[AMOS-GENERAL_MOC]]
