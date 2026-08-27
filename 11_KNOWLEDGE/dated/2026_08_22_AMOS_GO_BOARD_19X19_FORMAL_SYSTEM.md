---
title: 2026 08 22 AMOS GO BOARD 19X19 FORMAL SYSTEM
type: system
source: 11_KNOWLEDGE/dated
origin_architect: Trang Phan
provenance: docs/AMOS-Go-Board-19x19.md; cosmo-brain/AMOS_GO_BOARD_19X19.py; cosmo-brain/AMOS_GO_BOARD_19X19_STRATEGIC.py
confidence: 0.92
epistemic_class: SOURCE_DERIVED
conclusion_label: VERIFIED_PRESENT
tags: [canon-group/human-system, canon/framework, rscf/claim, rscf/provenance, rscf/state/observation, topic/2026-08-22-amos-go-board-19x19-formal-sy, dated, dated/2026-08-22]
date: 2026-08-22
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: temporal_log
---


# AMOS 19×19 Go Board — Formal System

> The 19×19 Go board is a formal state space mapping 361 intersections into an AMOS structural reasoning field. It is NOT 361 separately source-defined archetypes — meaning emerges from geometry + time + relation + board history.
>
> Source code: `cosmo-brain/AMOS_GO_BOARD_19X19.py` (109 self-tests) · `cosmo-brain/test_go_board_19x19.py` (190 tests) · `cosmo-brain/test_murk_goboard_integration.py` (108 tests)
> See also: 2026-08-22 19x19 Strategic Field Model · 2026-08-22 19x19 AI Cognitive Field · murk-engine-expansion

## 1. Static geometry

| Property | Value |
|----------|-------|
| Board size | 19×19 = 361 cells |
| Columns | A–T (excluding I) = 19 |
| Rows | 1–19 |
| Corners | 4 (A1, A19, T1, T19) |
| Sides | 68 |
| Interior | 289 |
| Hoshi | 9 at {4, 10, 16}² |
| Center | K10 (id 181) |
| Adjacency edges | 684 (derived: (19−1)·19·2) |
| D4 symmetry | 8 transformations |

### Zone classification

- **CORNER_ZONE**: boundary depth ≤ 3
- **SIDE_ZONE**: boundary depth 4–6
- **CENTER_ZONE**: boundary depth 7–9

### Macro regions

NW, N, NE, W, C, E, SW, S, SE.

## 2. AMOS field measures

| Measure | Formula | Range |
|---------|---------|-------|
| BoundarySupport | 1 − d_B/9 | [0, 1] |
| CenterInfluence | 1 − d_C/18 | [0, 1] |
| ExpansionFreedom | 0.5·(d_B/9 + deg/4) | [0, 1] |

## 3. Cell state model (12 core variables)

| Var | Symbol | Description |
|-----|--------|-------------|
| possibility | P | OPEN/COLLAPSED |
| mark | M | 0/1 stone present |
| boundary | B | boundary depth |
| liberty | L | liberty count of group |
| aji | A | latent potential |
| territory | T | territorial value |
| influence | I | influence field value |
| ko | K | ko restriction state |
| initiative | N | SENTE/GOTE |
| group | G | group membership |
| entropy | E | local entropy |
| strategic_value | S | H/M/L assessment |

The executable implementation adds a 20-variable state vector: V/O/A/G/B/L/Ey/Aj/K/S/T/I/P/D/M/R/Q/F/χ/σ.

## 4. Epistemic boundary

The 361 coordinates are a **state space**, not 361 archetypes. Their meanings emerge through:

- geometry (position, boundary, center distance)
- time (move history, temporal evolution)
- relation (adjacency, group membership, influence)
- board history (aji, ko, memory)

Assigning mystical meanings to all 361 cells would be canon fabrication.

## 5. 75-section formal specification registry

| Section | Feature | Status |
|---------|---------|--------|
| 1 | Complete mathematical object (𝔸_t) | AMOS MODEL |
| 2 | Full coordinate identity (immutable ID) | SOURCE |
| 3 | Static geometric signature | SOURCE |
| 4 | Static vs dynamic semantics firewall | SOURCE |
| 5 | 20-variable cell state vector | AMOS MODEL |
| 6 | Typed void states (VType: 6 types) | AMOS MODEL |
| 7 | Void quality (VQ computation) | AMOS MODEL |
| 8 | Ternary occupancy (−1/0/+1) | AMOS MODEL |
| 9 | Move object (typed entity, 22 fields) | AMOS MODEL |
| 10 | Move transition (compositional engine) | AMOS MODEL |
| 11 | Compositional transition engine (T_O∘T_G∘...) | AMOS MODEL |
| 12 | Dependency cone (CR/CD) | AMOS MODEL |
| 13 | Group topology (13 components) | AMOS MODEL |
| 14 | Group boundary & exposure | AMOS MODEL |
| 16 | Liberty vector (N/Q/D/C/R) | AMOS MODEL |
| 17 | Liberty independence graph + redundancy | AMOS MODEL |
| 18-19 | Eye topology (EyeQuality/PVR/Robustness) | AMOS MODEL |
| 20-23 | Aji system (DAG/half-life/latent threat) | AMOS MODEL |
| 24 | Sente compression (option-space control) | AMOS MODEL |
| 25-26 | Gote cost + initiative balance (I_Δ) | AMOS MODEL |
| 27 | Ko recurrence detection | AMOS MODEL |
| 28 | Ko leverage (ThreatValue/LocalCost) | AMOS MODEL |
| 29 | Territory field (T_A, T_B per cell) | AMOS MODEL |
| 30 | Influence field (exp decay model) | AMOS MODEL |
| 31 | Influence gradient (∇Φ) | AMOS MODEL |
| 32 | Territory-influence phase state (4 phases) | AMOS MODEL |
| 33-34 | Territory debt + influence value/fragility | AMOS MODEL |
| 35 | Future option set (Ω_t) | AMOS MODEL |
| 36 | Option diversity (entropy by region) | AMOS MODEL |
| 37 | Option concentration risk (OCR) | AMOS MODEL |
| 38 | Future debt tensor (7 components) | AMOS MODEL |
| 39-41 | Memory system (decay/classes/priority) | AMOS MODEL |
| 42 | Scale tensor (4 scales) | AMOS MODEL |
| 43-46 | Scale consistency + betrayal + integrity | AMOS MODEL |
| 47 | Region matrix (3×3, 9 components) | AMOS MODEL |
| 48 | Region compression residual | AMOS MODEL |
| 49 | Symmetry breaking (D4) | AMOS MODEL |
| 50 | Orbit classes (1/4/8) | AMOS MODEL |
| 51 | Distinction entropy | AMOS MODEL |
| 52-54 | Lacunarity (Λ(r) = Var/Mean²) | AMOS MODEL |
| 55 | Pressure field + group pressure + PRR | AMOS MODEL |
| 56-57 | Repair externality (NetRepair/OverRepair) | AMOS MODEL |
| 58-59 | Sacrifice tensor (7 components) | AMOS MODEL |
| 60 | Trajectory value (V(τ) = Σγ^k R) | AMOS MODEL |
| 62 | Branch quality (EV-Risk-Debt+Option) | AMOS MODEL |
| 63 | Robust branch (minimax) | AMOS MODEL |
| 64 | Regime states (5 regimes) | AMOS MODEL |
| 65 | Phase transition detection | AMOS MODEL |
| 67 | Observer belief (B^A ≠ B^B) | AMOS MODEL |
| 68 | Confidence tensor (6 epistemic tags) | AMOS MODEL |
| 70 | Move tensor (21 fields) | AMOS MODEL |
| 71 | Evaluate move firewall (dominates/competing) | AMOS MODEL |
| 72 | Master update equation (Π U) | AMOS MODEL |
| 73 | Full-system invariants (13 invariants) | AMOS MODEL |
| 74 | AMOS microcosm (17 mappings) | AMOS MODEL |

## 6. Test status

| Suite | Tests | Status |
|-------|-------|--------|
| `AMOS_GO_BOARD_19X19.py` | 214 | PASS |
| `test_go_board_19x19.py` | 190 | PASS |
| `test_murk_goboard_integration.py` | 226 | PASS |
| **Go Board total** | **630** | **PASS** |

## 7. Approved knowledge (ak registry)

- **ak-018**: MURK reasoning quality K-category
- **ak-019**: Full 19×19 formal system (361 cells, 684 edges, D4 symmetry, sacrifice validity)
- **ak-020**: Epistemic boundary — 361 coordinates are state space, NOT 361 archetypes
- **ak-021**: MURK↔GoBoard structural isomorphism (361↔361, cross-system reasoning)
- **ak-022**: 75-section formal specification implementation

## 8. Conclusion class

The geometry, coordinate identity, and board rules are source-grounded. The 20-variable cell state, VType, Regime, Move, GroupTopology, LibertyVector, ScaleTensor, RegionMatrix, influence/territory fields, and the formal machinery are `AMOS MODEL` — executable formalizations, not empirical Go strength.

---
**Links:** [[DATED_MOC]] | [[KNOWLEDGE_MOC]]
