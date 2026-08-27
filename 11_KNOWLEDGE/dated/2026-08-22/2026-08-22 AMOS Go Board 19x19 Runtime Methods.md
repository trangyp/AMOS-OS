---
origin_architect: Trang Phan
provenance: cosmo-brain/AMOS_GO_BOARD_19X19.py diff; 75-section formal spec sections 10-72
confidence: 0.95
epistemic_class: SOURCE_DERIVED
conclusion_label: VERIFIED_PRESENT
tags: [canon-group/human-system, canon/framework, rscf/claim, rscf/provenance, rscf/state/observation, topic/2026-08-22-amos-go-board-19x19-runtime-m, dated, dated/2026-08-22]
date: 2026-08-22
---

# AMOS 19×19 Go Board — Runtime Methods (62+ Sections)

> New executable methods added to `cosmo-brain/AMOS_GO_BOARD_19X19.py` to make the 75-section formal specification runnable. 226 self-tests + 251 integration tests pass; 0 failures. 811 grand total across all suites (including 15 Obsidian bridge tests).
>
> Source: `cosmo-brain/AMOS_GO_BOARD_19X19.py`
> See also: 2026-08-22 AMOS Go Board 19x19 Formal System · 2026-08-22 19x19 AI Cognitive Field · 2026-08-22 Tests Logic Bridge Registry

## 1. Move transition engine (§10-11)

`Board19.move_transition(x, y, color)`

```
T = T_O ∘ T_G ∘ T_L ∘ T_E ∘ T_A ∘ T_K ∘ T_Φ ∘ T_Ω ∘ T_M
```

- `T_O` occupancy update
- `T_G` group recompute
- `T_L` liberty recompute
- `T_E` eye detection
- `T_A` aji update
- `T_K` ko detection
- `T_Φ` influence field update
- `T_Ω` option count
- `T_M` memory record

Returns legal flag, cell, color, eyes, aji, ko, influence sum, option count, memory record.

## 2. New runtime methods by section

| Section | Method | Purpose |
|---------|--------|---------|
| 11 | `move_transition(x, y, color)` | Compositional engine T_O∘T_G∘...∘T_M |
| 12 | `dependency_cone(x, y)` | Affected cells, causal reach, causal depth |
| 15 | `permeability(x, y)` | Vulnerable / total boundary channels; hostile invasion porosity |
| 17 | `liberty_independence(x, y)` | Liberty coupling, redundancy, independent count |
| 18-19 | `detect_eyes(x, y)` | Eye positions, quality, PVR, robustness, life |
| 20-23 | `update_aji(x, y)`, `aji_half_life()`, `aji_latent_threat()` | Aji status, opportunity, weakness, decay, threat |
| 24 | `sente_compression(x, y)` | Option-space constraining ratio |
| 25-26 | `gote_cost(x, y)`, `initiative_balance()` | GoteCost, I_Δ initiative balance |
| 27 | `detect_ko()` | Recurrence / forbidden-cycle detection |
| 28 | `ko_leverage(x, y)` | KoLeverage=ThreatValue/LocalCost |
| 29-32 | `compute_influence()`, `compute_territory()`, `influence_gradient()`, `phase_state()` | Influence/territory/gradient/phase fields |
| 33-34 | `territory_debt(x, y)`, `influence_value(x, y)` | TerritoryDebt, InfluenceValue=Expected-Risk |
| 35-38 | `option_space()`, `option_count()`, `option_diversity()`, `option_concentration_risk()`, `future_debt_tensor()` | Future option set, diversity, concentration, 7-component debt |
| 39-41 | `record_move_memory()`, `memory_decay()` | Memory priority, 4 classes, exponential decay |
| 43-46 | `scale_consistency()`, `scale_betrayal()`, `scale_integrity()` | SC, Betrayal, Integrity (bottleneck) |
| 48 | `region_residual()` | Region compression residual |
| 49 | `symmetry_breaking_count()` | D4 distinction entropy |
| 50 | `orbit_class(x, y)` | Orbit sizes: 1/4/8 |
| 51 | `distinction_entropy()` | Entropy of marked vs empty distribution |
| 52-54 | `lacunarity(window_size)` | Λ(r)=Var(Mass)/Mean² |
| 55 | `pressure_field()`, `group_pressure()`, `pressure_to_repair_ratio()` | Pressure and PRR |
| 56-57 | `repair_externality(x, y)` | NetRepair, OverRepair |
| 58-59 | `sacrifice_tensor(x, y)` | SAC 7 components + validity |
| 60 | `trajectory_value(moves, gamma)` | V(τ)=Σγ^k R+TerminalOption |
| 61 | `tree_branching(depth)`, `tree_quality(depth)` | Game-tree branching factor, node count, branch quality |
| 62 | `branch_quality(x, y)` | BranchQuality=EV-Risk-Debt+Option |
| 63 | `robust_branch(branches)` | Robust(b)=min_r V(b,r) minimax |
| 64-65 | `detect_regime()`, `detect_phase_transition()` | Regime state and transition signals |
| 67 | `observer_belief(observer)` | B^A_t(S)≠B^B_t(S)≠TrueOutcome |
| 68 | `confidence_tensor(x, y)` | 6 epistemic tags: SOURCE/OBSERVED/DERIVED/MODEL/COMPETING/UNKNOWN |
| 70 | `move_tensor(x, y, color)` | 21-field move evaluation tensor |
| 71 | `evaluate_move_firewall(m1, m2)` | M1_DOMINATES/M2_DOMINATES/COMPETING |
| 72 | `master_update(x, y, color)` | A_{t+1}=Π_{C_t}[U(A_t,m_t,...)] |

## 3. Key typed return contracts

- `move_transition` → `Dict[str, Any]` with legal, cell, color, eyes, aji, ko, influence, options, memory
- `dependency_cone` → affected count, causal reach, causal depth, affected list
- `liberty_independence` → redundancy, independence matrix, independent count, total liberties
- `detect_eyes` → eye count, positions, quality, PVR, robustness, is_alive
- `update_aji` → status, opportunity, weakness, trigger set
- `future_debt_tensor` → 7 named components

## 4. Test results

| Suite | Tests | Status |
|-------|-------|--------|
| `AMOS_GO_BOARD_19X19.py` self-test | 226 | PASS |
| `test_go_board_19x19.py` comprehensive | 190 | PASS |
| `test_murk_goboard_integration.py` | 251 | PASS |
| **Go Board total** | **667** | **PASS** |
| MURK Engine | 10 | PASS |
| Brain Integration | 9 | PASS |
| MURK Comprehensive | 110 | PASS |
| **Grand total** | **811** | **PASS** |

## 5. Conclusion class

`AMOS MODEL / DERIVED`. The board geometry, coordinate identity, and Go rules are source-grounded. The influence/territory decay models, aji scoring, eye robustness, pressure/repair ratios, and option-space metrics are executable formalizations, not empirical Go strength.
