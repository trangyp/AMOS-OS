---
title: "03 Forex Moc — Specialist Domain Specification"
type: domain_specification
source: 21_DOMAINS
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_SPECIFICATION
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 21_DOMAINS/00_INDEX/DOMAIN_EXTENSION_PROTOCOL
    - 00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE
  scope: domain_specialization
tags:
  - amos-os
  - domains
  - c01-c12
  - 03-forex-moc
---

# 03_FOREX MOC — Forex Market Microstructure & Algorithmic Trading Hub

**Origin Architect / Steward:** Trang Phan  
**AMOS_CORE Target:** `v4.4`  
**Epistemic Class:** `AMOS_MODEL`

---

## 3. Quantitative Microstructure & Automated Bot Engines

- [[21_DOMAINS/03_FOREX/CONTINUOUS_AUTOMATED_FOREX_EXECUTION_BOT|CONTINUOUS_AUTOMATED_FOREX_EXECUTION_BOT]] — Asynchronous multi-asset bot runner (XAUUSD, EURUSD, GBPUSD, USDJPY), 3-tier dynamic circuit breakers, and vector Kelly sizing.
- [[21_DOMAINS/03_FOREX/CONTINUOUS_EXECUTION_BOT_LEDGER|CONTINUOUS_EXECUTION_BOT_LEDGER]] — 1,000-tick continuous execution ledger, PnL receipts, and max drawdown verification.
- [[21_DOMAINS/03_FOREX/FOREX_DOMAINS_PROVENANCE|FOREX_DOMAINS_PROVENANCE]] — Quantitative microstructure models, empirical verification logs, and data integrity receipts.
- [[21_DOMAINS/03_FOREX/MULTI_CURRENCY_PORTFOLIO_MICROSTRUCTURE|MULTI_CURRENCY_PORTFOLIO_MICROSTRUCTURE]] — 4-Asset portfolio microstructure (XAUUSD, EURUSD, GBPUSD, USDJPY) with vector Quarter-Kelly allocation.
- [[21_DOMAINS/03_FOREX/FOREX_DOMAINS_INTERFACES|FOREX_DOMAINS_INTERFACES]] — FIX 4.4 tag-value protocol specifications and MT5/ZeroMQ interprocess bridge schemas.
- [[21_DOMAINS/03_FOREX/DOMAINS_FOREX_CONTRACT|DOMAINS_FOREX_CONTRACT]] — Hard risk boundaries (1.5% lot exposure, mandatory stop-loss, kill-switch latency < 25ms).
- [[21_DOMAINS/03_FOREX/FOREX_DOMAINS_DOMAIN_SPEC|FOREX_DOMAINS_DOMAIN_SPEC]] — High-frequency market microstructure and liquidity surface modeling.
- [[21_DOMAINS/03_FOREX/FOREX_BACKTEST_VALIDATION_REPORT|FOREX_BACKTEST_VALIDATION_REPORT]] — Live simulated high-frequency backtest report for single-asset XAUUSD.
- [[21_DOMAINS/03_FOREX/MULTI_CURRENCY_PORTFOLIO_REPORT|MULTI_CURRENCY_PORTFOLIO_REPORT]] — Live 4-asset portfolio simulation and covariance risk ledger.
- [[21_DOMAINS/03_FOREX/FOREX_DOMAINS_README|FOREX_DOMAINS_README]] — Domain overview, execution regimes, and telemetry pipelines.

---

## 2. Integrated Quantitative Currency & Macro Engines

- [[21_DOMAINS/09_FINANCE/TRANG_ZERO_FOREX|TRANG_ZERO_FOREX]] — Trang Zero-Arbitrage Forex Market Model.
- [[21_DOMAINS/09_FINANCE/OMEGA_FX_STRUCTURAL_OS|OMEGA_FX_STRUCTURAL_OS]] — Multi-Currency High-Frequency Structural Trading OS.
- [[21_DOMAINS/09_FINANCE/MACRO_ECONOMY_KERNEL|MACRO_ECONOMY_KERNEL]] — Macroeconomic Interest Rate & Central Bank Policy Kernel.

---

## 3. Governance Invariants

```text
MARKET_MODEL != ARBITRAGE_FREE_GUARANTEE
BACKTEST_PROFITABLE != LIVE_EXECUTION_STABLE
KILL_SWITCH_LATENCY < 25MS (STRICT_INVARIANT)
```

---

## 4. Parent Navigation

- **Master Domain Hub:** [[21_DOMAINS/21_DOMAINS_MOC|21_DOMAINS_MOC]]
- **Agent Roles:** [[06_AGENTS/AGENT_ROLE_REGISTRY|AGENT_ROLE_REGISTRY]] (`SPEC_QUANT_FOREX`)
- **Master Root Hub:** [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
