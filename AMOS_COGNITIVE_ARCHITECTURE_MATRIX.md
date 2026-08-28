---
title: AMOS COGNITIVE ARCHITECTURE MATRIX
type: note
source: .
tags:
- note
- vault
- canon/general
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


# AMOS Cognitive Architecture Matrix

> **Status:** v1.0 — formal 4-axis matrix exposing every cognitive-primitive × lifecycle-operation × control-plane × scale interaction in AMOS, with rule-based coverage status.
> **Companion artifact:** `AMOS_Cognitive_Architecture_Matrix.json` (machine-readable, 13,770 cells).
> **Generator:** `build_amos_cognitive_matrix.py` (auditable, reproducible).

## 1. Purpose

The prior gap analysis (gaps 901–1500) enumerated **capabilities** as a flat list. That abstraction is wrong: it exposes missing *modules* but hides missing **interactions**. A complete AMOS cognitive architecture is not `LLM → Skills → Agents`, nor even `Kernel → Engine → Agent → Memory`. It is a 30-layer cognitive stack (L0–L29) wrapped by 9 cross-cutting control planes, where every primitive must pass through every lifecycle operation at every scale under every plane.

The matrix's job is therefore not to count features. It is to make the **interaction space** addressable so that the gaps that live *between* modules become visible. The headline finding confirms the gap document's conclusion:

> **The completion denominator is not yet closed.** Of 13,770 addressable interaction cells, only **1.98%** are existing, **22.96%** partial, **7.04%** explicitly missing, and **68.02%** are *structural gaps* — interactions AMOS has not yet recognized or named.

A flat "1501–2000" list would have continued to miss the 9,367 structural-gap cells. The matrix is the correct abstraction to expose them.

The architectural invariant this matrix enforces:

```
LLM ⊂ CognitiveExecution
AMOS = Kernel + CognitiveRuntime + MemorySystem + WorldModel
      + ReasoningSystem + SimulationSystem + DecisionSystem
      + LearningSystem + AgentSystem + GovernanceSystem
AMOS ≠ LLM
```

## 2. The Four Axes

### Axis P — Cognitive Primitives (30, L0–L29)

The vertical cognitive stack. Each primitive carries a **maturity** score versus current AMOS, derived from the gap document's explicit claims (not guessed).

| ID | Primitive | Subsystem / Gap ref | Maturity | Basis |
|----|-----------|---------------------|----------|-------|
| L0 | Reality / Environment | Environment substrate | missing | Not a typed subsystem |
| L1 | Sensing / Observation | 931–960 | missing | Perception needs epistemic machinery |
| L2 | Attention | 901–930 | missing | Attention missing as real subsystem |
| L3 | Percept Formation | 931–960 | missing | Observation ≠ Interpretation firewall absent |
| L4 | Object / Entity Formation | 961–990 | missing | Persistent entity identity absent |
| L5 | Binding | 991–1020 | missing | Explicit relational cognition absent |
| L6 | Working State | 1021–1050 | missing | No cognitive workspace beyond context window |
| L7 | Memory | 1051–1140 | partial | HOT/WARM lifecycle exists; activation/interference/forgetting missing |
| L8 | Representation | 1141–1170 | partial | Partial representation; world-model engine largely missing |
| L9 | Inference | Reasoning kernel | partial | CORE-19 reasoning kernel exists |
| L10 | World Modeling | 1141–1170 | missing | Enormous gap; LLM must not be the world model |
| L11 | Causal Modeling | Causal mediation | partial | Counterfactual/causal kernels exist |
| L12 | Counterfactual Simulation | 1201–1230 | partial | Counterfactual kernel exists; simulation worlds missing |
| L13 | Prediction | 1171–1200 | missing | Prediction governance missing |
| L14 | Valuation | 1231–1260 | missing | No explicit value-function architecture |
| L15 | Goal Formation | Kernel goals | partial | Goals exist in kernel typed state |
| L16 | Planning | Planning | partial | Planning exists; limited machinery |
| L17 | Decision | 1261–1290 | partial | Decision filter exists; much missing |
| L18 | Action | Execution plane | existing | Agents/Skills/Tools execution exists |
| L19 | Outcome Observation | 931–960 | missing | Observation-to-outcome loop absent |
| L20 | Credit Assignment | 1291–1320 | missing | No explicit credit/blame attribution |
| L21 | Learning | 1291–1320 | partial | GMEF pieces exist; learning semantics incomplete |
| L22 | Consolidation | Consolidation | missing | No offline consolidation analogue |
| L23 | Metacognition | 1321–1350 | partial | Self-review loop exists; metacognitive model missing |
| L24 | Self-Regulation | 1351–1380 | partial | Operational modes exist; cognitive control incomplete |
| L25 | Identity / Continuity | 1381–1410 | missing | Major gap for persistent operation |
| L26 | Social Cognition | 1411–1440 | missing | Other actors not modeled beyond text |
| L27 | Multi-Agent Cognition | 1441–1470 | partial | Coordination kernel exists; collective cognition missing |
| L28 | Governance | Governance plane | existing | Governance kernel / GMEF / RSCF exist |
| L29 | Evolution | Evolution loop | existing | Governed evolution / evolution loop exist |

### Axis O — Lifecycle Operations (17)

The horizontal lifecycle a cognitive primitive passes through:

`Distinction → Object → Relation → Binding → State → Memory → Model → Inference → Prediction → Simulation → Value → Goal → Plan → Decision → Action → Observation → Learning`

### Axis C — Control Planes (9)

Cross-cutting fields wrapping the entire stack. Each carries a **coverage** score versus current AMOS.

| ID | Plane | Facets | Coverage |
|----|-------|--------|----------|
| C1 | Governance | Authority · Risk · Ethics · GMEF · Finality | existing |
| C2 | Metacognitive | Monitor · Confidence · Drift · Repair · Stop | partial |
| C3 | Executive | Goals · Value · Planning · Decision · Attention | partial |
| C4 | Reasoning | Inference · Causal · Counterfactual · Prediction · Simulation | partial |
| C5 | Representation | Objects · Relations · Bindings · WorldModel · Ontology | missing |
| C6 | Memory | Working · Episodic · Semantic · Procedural · Provenance | partial |
| C7 | Perception | Observation · Measurement · Feature · Percept · RealityContact | missing |
| C8 | Execution | Agents · Skills · Tools · Models · Environment | existing |
| C9 | Kernel/Control | TypedState · Transactions · Epochs · Replay · Invalidation | existing |

### Axis S — Scale (3)

| ID | Scale |
|----|-------|
| H | High scale / hard / long-horizon / cross-system |
| M | Mid scale |
| L | Low scale / easy / local |

**Cardinality:** 30 × 17 × 9 × 3 = **13,770 cells**.

## 3. Status Taxonomy

| Code | Status | Meaning |
|------|--------|---------|
| `e` | existing | Verified present in current AMOS |
| `p` | partial | Present but incomplete |
| `m` | missing | Explicitly identified absent (gaps 901–1500) |
| `g` | structural_gap | Interaction not yet recognized/named in AMOS — **newly exposed by this matrix** |

The `structural_gap` class is the matrix's reason to exist. It captures interactions that are neither implemented nor explicitly named — exactly the hidden gaps a flat list cannot surface.

## 4. Derivation Rules (auditable)

Status for each cell `(P, O, C, S)` is computed, not fabricated:

1. If `(P, C)` is in the **explicit-gaps** map (derived from gaps 901–1500) → `m` (missing), with a `gap_ref`.
2. Else `base = combine(maturity[P], coverage[C])`: any `missing` → 0, any `partial` → 1, else 2.
3. **Scale adjust:** `H` (high/hard) → `base − 1` floored at 0; `M` and `L` unchanged.
4. `base` maps `{0 → m, 1 → p, 2 → e}`.
5. If status is `m` and `(P, C)` is **not** explicit → reclassify as `g` (structural_gap).

Rules 1 and 5 are the key distinction: explicitly-named absences become `missing`; absences the matrix itself exposes become `structural_gap`. The full rule set is encoded in `build_amos_cognitive_matrix.py` and reproduced verbatim in the JSON `derivation_rules` field.

## 5. Explicit Gap Map (gaps 901–1500 → primitive × plane)

19 `(primitive, plane)` pairs are explicitly named missing. Each expands across all 17 lifecycle ops × 3 scales = 51 cells, yielding 969 explicit-missing cells.

| Primitive | Plane | Gap ref |
|-----------|-------|---------|
| L2 Attention | C3 Executive | 901–930 |
| L1 Sensing | C7 Perception | 931–960 |
| L3 Percept | C7 Perception | 931–960 |
| L4 Object/Entity | C5 Representation | 961–990 |
| L5 Binding | C5 Representation | 991–1020 |
| L6 Working State | C6 Memory | 1021–1050 |
| L7 Memory | C6 Memory | 1051–1140 |
| L10 World Model | C5 Representation | 1141–1170 |
| L13 Prediction | C4 Reasoning | 1171–1200 |
| L12 Counterfactual Sim | C4 Reasoning | 1201–1230 |
| L14 Valuation | C3 Executive | 1231–1260 |
| L17 Decision | C3 Executive | 1261–1290 |
| L21 Learning | C2 Metacognitive | 1291–1320 |
| L23 Metacognition | C2 Metacognitive | 1321–1350 |
| L24 Self-Regulation | C2 Metacognitive | 1351–1380 |
| L25 Identity/Continuity | C9 Kernel/Control | 1381–1410 |
| L26 Social Cognition | C5 Representation | 1411–1440 |
| L27 Multi-Agent | C8 Execution | 1441–1470 |
| L29 Evolution (security) | C1 Governance | 1471–1500 |

## 6. Summary Results

| Status | Cells | % |
|--------|------:|--:|
| existing | 272 | 1.98% |
| partial | 3,162 | 22.96% |
| missing | 969 | 7.04% |
| structural_gap | 9,367 | 68.02% |
| **Total** | **13,770** | **100%** |

### Coverage by control plane

| Plane | e | p | m | g |
|-------|--:|--:|--:|--:|
| C1 Governance | 68 | 442 | 51 | 969 |
| C2 Metacognitive | 0 | 408 | 153 | 969 |
| C3 Executive | 0 | 476 | 153 | 901 |
| C4 Reasoning | 0 | 476 | 102 | 952 |
| C5 Representation | 0 | 0 | 204 | 1,326 |
| C6 Memory | 0 | 476 | 102 | 952 |
| C7 Perception | 0 | 0 | 102 | 1,428 |
| C8 Execution | 102 | 425 | 51 | 952 |
| C9 Kernel/Control | 102 | 459 | 51 | 918 |

### Coverage by primitive (selected)

| Primitive | e | p | m | g |
|-----------|--:|--:|--:|--:|
| L18 Action | 102 | 187 | 0 | 170 |
| L28 Governance | 102 | 187 | 0 | 170 |
| L29 Evolution | 68 | 170 | 51 | 170 |
| L7 Memory | 0 | 204 | 51 | 204 |
| L10 World Model | 0 | 0 | 51 | 408 |
| L25 Identity | 0 | 0 | 51 | 408 |
| L2 Attention | 0 | 0 | 51 | 408 |
| L0 Reality | 0 | 0 | 0 | 459 |

(Full per-primitive and per-plane breakdowns are in the JSON `summary` field.)

## 7. Interpretation

- **The 68% structural-gap rate is the real headline.** It does not mean AMOS is "68% broken"; it means 68% of the *addressable interaction space* has never been named as a concept. This is precisely the "completion denominator is not yet closed" claim made operational.
- **Existing coverage (1.98%) clusters in L18 Action / L28 Governance / L29 Evolution × C1/C8/C9 planes** — the execution, governance, and kernel-control planes, which is consistent with the current kernel design treating the LLM as replaceable and assigning authoritative typed state to the kernel.
- **The Representation (C5) and Perception (C7) planes are 0% existing** — confirming the document's claim that perception machinery and world-model representation are the deepest gaps.
- **Scale H is the hardest tier** by construction (rule 3): high-scale interactions are downgraded one level, so long-horizon / cross-system cognition is where structural gaps concentrate.

## 8. How to query the JSON

```python
import json
m = json.load(open("AMOS_Cognitive_Architecture_Matrix.json"))
cells = m["cells"]                       # {"L7:Memory:C6:H": "p", ...}
# All structural-gap cells in the Representation plane at high scale:
gap_cells = [k for k,v in cells.items()
             if v=="g" and k.split(":")[2]=="C5" and k.split(":")[3]=="H"]
# Explicit missing for a primitive:
miss = [k for k,v in cells.items() if v=="m" and k.startswith("L10:")]
```

Cell key format: `<PrimitiveID>:<LifecycleOp>:<PlaneID>:<ScaleID>` (e.g. `L7:Binding:C6:H`).

## 9. Relationship to existing AMOS artifacts

- The 8-sub-domain **Cognitive Stack** (`_00_Cosmo brain/Core/Cognitive_Stack/`) is the meta-cognition + domain-cognition kernel family *inside* the Omni Kernel — it populates a subset of cells in the Reasoning (C4), Memory (C6), and Metacognitive (C2) planes. This matrix is the superset those kernels sit inside.
- The current **OS Kernel** memory spec (HOT/WARM/COLD/QUARANTINED/EXPIRED/RAW_ARCHIVE with provenance, dependencies, freshness, contradiction state, falsifiers, rollback/replay) populates L7 × C6 × C9 cells at `partial` — it covers lifecycle classes but not activation dynamics, interference, or forgetting (gaps 1051–1140).
- **GMEF / RSCF / governed-evolution** populate L28/L29 × C1 cells at `existing`/`partial`.

## 10. Next steps (not another flat list)

1. **Triage structural gaps by criticality.** 9,367 `g` cells cannot all be addressed at once. Rank by (irreversibility × dependency-centrality × scale) — the attention-allocation formula from gaps 901–930 applied to the matrix itself.
2. **Promote high-value `g` → `m`.** Where a structural gap corresponds to a real missing interaction, name it and assign a gap id (extending past 1500) so it becomes trackable.
3. **Fill `m` → `p` → `e`** per the existing governed-evolution pipeline, with the matrix cell as the unit of progress rather than a loose feature.
4. **Re-run the generator** as maturity/coverage scores change. The matrix is regenerable; the JSON is the live coverage ledger.

---

*Generated by `build_amos_cognitive_matrix.py`. All coverage statuses are rule-derived from the gap document's explicit claims; no status is fabricated. See the JSON `derivation_rules` field for the exact rule set.*

---
**Related:** [[00_HOME]] · generated_architecture · AMOS_quantum_library_v0.1.0 · PRIVACY_POLICY

---
```RSCF-NODE
node_id: AMOS_COGNITIVE_ARCHITECTURE_MATRIX
node_type: spec
domain: AMOS_SPEC
path: AMOS_COGNITIVE_ARCHITECTURE_MATRIX.md
RSCF-RELATIONS:
  - INDEXED_BY: P1
  - RELATED_TO: AMOS_quantum_library_v0.1.0
  - RELATED_TO: PRIVACY_POLICY
claim_class: AMOS_MODEL
```

---
**MOC:** [[AMOS_HOME]]

---
**MOC:** [[_MOC]]
