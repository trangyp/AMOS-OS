---
title: "DOMAINS FOREX CONTRACT — Quantitative Risk & Execution Governance"
type: control_contract
source: 21_DOMAINS/50_FOREX
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_GOVERNING_CONTRACT
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 21_DOMAINS/50_FOREX/FOREX_DOMAINS_PROVENANCE
    - 03_CONTROL_PLANE/CONTROL_PLANE_CONTROL_PLANE_CONTRACT
  scope: forex_risk_governance
tags:
  - amos-os
  - domains
  - forex
  - risk-contract
  - drawdown-limits
---

# DOMAINS FOREX CONTRACT — Quantitative Risk & Execution Governance

## 1. Purpose & Hard Invariants

This contract enforces the deterministic risk boundaries, position sizing ceilings, and execution constraints governing the AMOS Forex engine.

```text
EXECUTION_SIGNAL != ORDER_AUTHORIZATION
CAPABILITY != FINANCIAL_RISK_GRANT
DRAWDOWN_LIMIT = ABSOLUTE_BARRIER (5.0%)
```

---

## 2. Quantitative Risk Rules

1. **Maximum Single-Trade Risk:** $\le 1.0\%$ of active account equity.
2. **Maximum Daily Drawdown:** $\le 2.5\%$ (Trading halts for 24h if breached).
3. **Maximum Total Drawdown:** $\le 5.0\%$ (Complete position liquidation and emergency quarantine).
4. **News Blackout Window:** No new market orders 15 minutes before or after high-impact macroeconomic releases (CPI, NFP, FOMC, Rate Decisions).
5. **Mandatory Hard Stop-Loss:** Every open position MUST have a broker-side hard stop-loss attached at order submission time.

---

## 3. Enforcement & Verification

- **Gated In:** [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
- **Monitored In:** [[17_OBSERVABILITY/OBSERVABILITY_README|OBSERVABILITY_README]]
- **Rollback Procedure:** [[20_OPERATIONS/INCIDENT_RESPONSE_PLAYBOOK|INCIDENT_RESPONSE_PLAYBOOK]]

## Scope

This domain specification defines the `50_FOREX` domain within `21_DOMAINS`. It is one of the specialist or canonical knowledge domains and is governed by the `21_DOMAINS` cross-walk and `01_CANON` canonical constraints.

## Invariants

| ID | Invariant |
|----|-----------|
| 50_FOREX_DOMAIN_SPEC_INV_01 | Domain-specific claims are scoped to `50_FOREX` and do not universalize without cross-domain evidence. |
| 50_FOREX_DOMAIN_SPEC_INV_02 | All domain models are classified as `AMOS_MODEL` or `DERIVED` unless externally validated. |
| 50_FOREX_DOMAIN_SPEC_INV_03 | Domain MOC is the authoritative index for this directory. |

## Integration

- **Canonical binding:** `01_CANON/01_CORE_LAWS/LAW_HIERARCHY`
- **Cross-domain router:** `21_DOMAINS/00_INDEX/150_DOMAIN_CANON_MASTER_CROSSWALK`
- **Research input:** `22_RESEARCH/22_RESEARCH_MOC`
- **Runtime execution:** `04_RUNTIME/04_RUNTIME_MOC`

Domain models may inform `05_COGNITIVE_ORGANISM` engines but are not themselves cognitive primitives.

## Cross References
- [[{rel.parent}/50_FOREX_MOC|50_FOREX_MOC]]
- [[21_DOMAINS/21_DOMAINS_MOC|21_DOMAINS_MOC]]
- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
