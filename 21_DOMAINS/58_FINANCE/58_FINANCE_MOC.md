---
title: 09 Finance MOC
type: moc
source: 21_DOMAINS/58_FINANCE
tags:
  - 09-finance
  - canon/domain
  - finance-domains-domain-spec
  - finance-domains-interfaces
  - finance-domains-provenance
  - macro-economy-kernel
  - omega-fx-structural-os
  - trang-zero-forex
moc: true
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---

# 09 Finance — Map of Content

**Path:** `21_DOMAINS/58_FINANCE`
**Files:** 8 | **Subdirectories:** 1

## Files

- [[21_DOMAINS/58_FINANCE/DOMAINS_FINANCE_CONTRACT|DOMAINS_FINANCE_CONTRACT]]
- [[21_DOMAINS/58_FINANCE/FINANCE_DOMAINS_DOMAIN_SPEC|FINANCE_DOMAINS_DOMAIN_SPEC]]
- [[21_DOMAINS/58_FINANCE/FINANCE_DOMAINS_INTERFACES|FINANCE_DOMAINS_INTERFACES]]
- [[21_DOMAINS/58_FINANCE/FINANCE_DOMAINS_PROVENANCE|FINANCE_DOMAINS_PROVENANCE]]
- [[21_DOMAINS/58_FINANCE/FINANCE_DOMAINS_README|FINANCE_DOMAINS_README]]
- [[21_DOMAINS/58_FINANCE/MACRO_ECONOMY_KERNEL|MACRO_ECONOMY_KERNEL]]
- [[21_DOMAINS/58_FINANCE/OMEGA_FX_STRUCTURAL_OS|OMEGA_FX_STRUCTURAL_OS]]
- [[21_DOMAINS/58_FINANCE/TRANG_ZERO_FOREX|TRANG_ZERO_FOREX]]

## Subdirectories

- [[01_CANON/00_INDEX/00_INDEX_MOC|00_INDEX_MOC]] — 00_INDEX

______________________________________________________________________


## Domain Scope

The Finance domain covers financial markets, investment, risk management, and financial technology:

### Sub-domains
- **Investment**: equity, fixed income, derivatives, alternative investments; DCF, relative valuation, portfolio theory
- **Risk management**: market risk (VaR, ES), credit risk (PD, LGD), operational risk; stress testing, scenario analysis
- **Financial technology**: fintech, DeFi, payment systems, blockchain, algorithmic trading
- **Corporate finance**: capital structure, WACC, dividend policy, M&A, LBO

### SOTA Methods
- **Quantitative finance**: factor models (Fama-French 5-factor), risk parity, Black-Litterman; ML for alpha generation
- **Algorithmic trading**: HFT (microsecond latency), statistical arbitrage, mean reversion; market microstructure
- **Risk metrics**: VaR (historical, parametric, Monte Carlo), Expected Shortfall (ES), stress testing (CCAR, DFAST)
- **DeFi**: AMM (Uniswap V3), lending (Aave, Compound), derivatives (dYdX); oracle (Chainlink); liquid staking (Lido)

### AMOS Integration
- **C07 domain**: [[21_DOMAINS/17_C07_ECON_FINANCE/17_C07_ECON_FINANCE_MOC|C07 econ-finance domain]]
- **Cashflow engine**: [[11_KNOWLEDGE/engine/CASHFLOW_ENGINE|Cashflow Engine]]
- **Investment engine**: [[11_KNOWLEDGE/engine/INVESTMENT_ENGINE|Investment Engine]]
- **Sector rotation engine**: [[11_KNOWLEDGE/engine/SECTOR_ROTATION_ENGINE|Sector Rotation Engine]]
- **Political risk engine**: [[11_KNOWLEDGE/engine/POLITICAL_RISK_ENGINE|Political Risk Engine]]
- **Finance sensor kernel**: [[11_KNOWLEDGE/kernel/FINANCE_SENSOR_KERNEL|Finance Sensor Kernel]]
- **Market signals kernel**: [[11_KNOWLEDGE/kernel/MARKET_SIGNALS_KERNEL|Market Signals Kernel]]

### Invariants
1. `MODEL != MARKET` — financial models are approximations, not reality
2. `BACKTEST != FUTURE_PERFORMANCE` — past performance does not guarantee future results
3. All financial claims must cite provenance (data source, methodology, time period)
4. `CAPABILITY != AUTHORITY` — ability to model markets does not grant trading authority


**Parent:** [[21_DOMAINS/21_DOMAINS_MOC|21_DOMAINS_MOC]]
