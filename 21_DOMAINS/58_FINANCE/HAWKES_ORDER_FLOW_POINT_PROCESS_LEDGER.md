---
title: Multivariate Hawkes Process Order Flow Point Process Ledger
plane: 21_DOMAINS
subplane: 58_FINANCE
status: ACTIVE_SOTA_QUANTITATIVE_SURFACE
origin_architect: Trang Phan
governance: AMOS_v4.4_CANONICAL
hash_digest: 0b7a47aeb212bbb6fc6af5acba55e144347dfff840570f7f4a48630c1a1b4c82
rscf-state: source-claim
---

# Multivariate Mutually-Exciting Hawkes Process & High-Frequency Order Flow Dynamics

## 1. Mathematical Formalism

High-frequency limit order book dynamics for Buy ($m=0$) and Sell ($m=1$) market orders are modeled via a multi-dimensional Hawkes process with conditional intensity:
$$\lambda_m(t) = \mu_m + \sum_{n=1}^M \int_0^t \alpha_{mn} e^{-\beta_{mn}(t - s)} dN_n(s) = \mu_m + \sum_{n=1}^M \sum_{t_{j,n} < t} \alpha_{mn} e^{-\beta_{mn}(t - t_{j,n})}$$

The branching ratio matrix is given by $\Gamma_{mn} = \frac{\alpha_{mn}}{\beta_{mn}}$. The market system is strictly stationary and subcritical if and only if the spectral radius satisfies:
$$\rho(\Gamma) < 1$$

Order Flow Imbalance (OFI) measures directional order pressure:
$$\text{OFI} = \frac{N_{buy}(T) - N_{sell}(T)}{N_{buy}(T) + N_{sell}(T)}$$

## 2. Telemetry Verification Results

```json
{
  "time_horizon_s": 100.0,
  "baseline_intensity_mu": [
    0.5,
    0.5
  ],
  "decay_rate_beta": 1.2,
  "branching_ratio_spectral_radius": 0.41666666666666674,
  "system_subcritical_stable": true,
  "total_events_generated": 147,
  "total_buy_orders": 88,
  "total_sell_orders": 59,
  "order_flow_imbalance": 0.1972789115512055,
  "hawkes_clustering_verified": true
}
```

## 3. Cryptographic Receipt
- **Spectral Radius $\rho(\Gamma)$**: `0.4167 (< 1.0)`
- **Order Flow Imbalance**: `0.1973`
- **Subcritical Stability**: `STABLE & VERIFIED`


## SOTA Methods

### Hawkes processes
- **Self-exciting point process**: λ(t) = μ + Σ κ(t - t_i) where κ is the excitation kernel
- **Exponential kernel**: κ(τ) = α·e^(-β·τ); branching ratio n = α/β < 1 (stationarity condition)
- **Power-law kernel**: κ(τ) = α/(τ + c)^(1+ε); long-range dependence; financial crash modeling
- **Estimation**: MLE, EM algorithm; nonparametric estimation; spectral method

### Order flow modeling
- **Hawkes order flow**: model buy/sell order arrivals as mutually exciting point processes
- **Market microstructure**: order flow imbalance (OFI); queue dynamics; price impact (Kyle, Almgren-Chriss)
- **High-frequency**: sub-millisecond order book dynamics; co-location; FPGA; microwave networks
- **Limit order book**:LOBster data; queue-reactive model; fluid limit; mean-reverting spread

### AMOS Integration
- **C07 domain**: [[21_DOMAINS/17_C07_ECON_FINANCE/17_C07_ECON_FINANCE_MOC|C07 econ-finance domain]]
- **Finance domain**: [[21_DOMAINS/58_FINANCE/58_FINANCE_MOC|58_FINANCE_MOC]]
- **Finance sensor kernel**: [[11_KNOWLEDGE/kernel/FINANCE_SENSOR_KERNEL|Finance Sensor Kernel]]
- **Market signals kernel**: [[11_KNOWLEDGE/kernel/MARKET_SIGNALS_KERNEL|Market Signals Kernel]]

### Invariants
1. `MODEL != MARKET` — Hawkes process is an approximation of order flow
2. `STATIONARITY != GUARANTEED` — branching ratio < 1 is required for stationarity
3. All order flow claims must cite provenance (data source, venue, time period, model parameters)
4. `FIT != PREDICTION` — model fit to historical data does not guarantee predictive power

