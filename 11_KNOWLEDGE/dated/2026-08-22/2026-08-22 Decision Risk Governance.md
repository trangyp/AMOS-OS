---
tags: [dated, dated/2026-08-22]
---
# Decision Theory & Risk Governance (Gaps 222-229)

**Date**: 2026-08-22
**Cluster**: `decision_risk`
**Status**: CLOSED (11-layer chains complete)
**Tests**: 43 new tests (820 total)

## Overview

Implemented the Decision Theory & Risk governance module for the AMOS OS Kernel, covering 8 gaps (222-229) across decision-theoretic layer, risk appetite, utility conflicts, non-compensatory constraints, catastrophic-risk gate, tail-risk estimation, risk aggregation, and risk budgeting.

## 8 Subsystems

| Gap | Subsystem | Class | Description |
|-----|-----------|-------|-------------|
| 222 | DecisionTheoryEngine | `DecisionTheoryEngine` | Expected utility computation and action selection |
| 223 | RiskAppetiteModel | `RiskAppetiteModel` | Risk appetite and tolerance modeling |
| 224 | UtilityConflictResolver | `UtilityConflictResolver` | Utility conflict representation and resolution |
| 225 | NonCompensatoryGate | `NonCompensatoryGate` | Non-compensatory constraint enforcement |
| 226 | CatastrophicRiskGate | `CatastrophicRiskGate` | Catastrophic-risk gate (FAIL when triggered) |
| 227 | TailRiskEstimator | `TailRiskEstimator` | Tail-risk estimation (VaR, CVaR) |
| 228 | RiskAggregator | `RiskAggregator` | Risk aggregation across actions |
| 229 | RiskBudgetManager | `RiskBudgetManager` | Risk budget allocation and tracking |

## Key Algorithms

- **Catastrophic risk triggered**: `risk_score >= threshold` (default 0.8)
- **Non-compensatory violated**: `current_value > threshold`
- **High tail risk**: `tail_probability > 0.05`
- **Risk budget exceeded**: `consumed > allocated`
- **Risk aggregation**: sum, max, or mean of action risks
- **Empirical VaR**: sorted_losses[int(percentile * n)]
- **Empirical CVaR**: mean of losses beyond VaR threshold

## Governor Gates

5 post-execution gates (4 CONDITIONAL + 1 FAIL):

| Gate Name | Condition | Status |
|-----------|-----------|--------|
| decision-unresolved-conflicts | Unresolved utility conflicts | CONDITIONAL |
| decision-non-compensatory-violated | Violated constraints | CONDITIONAL |
| decision-catastrophic-risk | Catastrophic risk triggered | **FAIL** |
| decision-risk-budget-exceeded | Budget exceeded | CONDITIONAL |
| decision-high-tail-risk | Tail probability > 5% | CONDITIONAL |

**Note**: The catastrophic-risk gate is the only **FAIL** gate in the entire
kernel. This is intentional — catastrophic risks should block execution.

## Files Modified

- `amos/governance/decision_risk.py` — 8 subsystems + governor (new, ~517 lines)
- `amos/core/types.py` — 8 dataclasses + 5 enums (new)
- `amos/state/store.py` — 8 store method pairs + 8 schema tables (new)
- `amos/kernel.py` — import + instantiation + evaluate_post wiring
- `amos/__init__.py` — exports for all 8 subsystems + governor
- `amos/governance/seed_completion.py` — moved decision_risk to CLOSED_CLUSTERS
- `tests/test_decision_risk.py` — 43 tests (new)
- `tests/test_completion.py` — updated counts (139 closed, 91 open)
- `AGENTS.md` — updated gate list, gap counts, test count

## Completion Graph State

- **139 closed gaps** (91-229) across 14 clusters
- **91 open gaps** (230-320) across 9 clusters
- **19 matrix gaps** (321-339)
- **820 total tests**

## Related

- 2026-08-22 Uncertainty Calibration Governance
- 2026-08-22 Adversarial Robustness Governance
- 2026-08-22 Distributed Consensus Governance
- [[00_Cosmo_Brain_MOC]]

#decision-risk #governance #gaps-222-229 #closed #amos-os-kernel
