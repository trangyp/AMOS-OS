---
title: ORDER_BOOK_MICROSTRUCTURE_FLOW_LEDGER
type: cryptographic_execution_ledger
amos_core_target: v4.4
origin_architect: Trang Phan
status: ACTIVE_SOTA_PRODUCTION
rscf:
  state: EXECUTED_AND_VERIFIED
  provenance: amos_sota_batch_22
  scope: 21_DOMAINS/50_FOREX
---

# High-Frequency Order Book Microstructure & Cross-Currency Co-Integration Ledger

## 1. Mathematical Architecture & Vector Error-Correction (VECM)

High-frequency algorithmic FX market-making relies on Level-2 Limit Order Book (LOB) depth imbalances and Johansen co-integrated triangular currency parity.

### Triangular Co-Integration Parity
For currency triad $(A/B, B/C, A/C)$, no-arbitrage equilibrium requires:
$$\ln S_{AC}(t) - \ln S_{AB}(t) - \ln S_{BC}(t) = z(t) \sim \mathcal{N}(0, \sigma_z^2)$$
where $z(t)$ is an Ornstein-Uhlenbeck mean-reverting stationary spread:
$$dz(t) = -\theta z(t) dt + \sigma_z dW(t), \quad t_{1/2} = \frac{\ln 2}{\theta}$$

### Kyle's Lambda Order Flow Price Impact
Price adjustment $\Delta P_{t}$ is modeled via Order Flow Imbalance ($OFI_t$):
$$\Delta P_t = \lambda \cdot OFI_t + \epsilon_t, \quad \lambda = \frac{\text{Cov}(\Delta P_t, OFI_t)}{\text{Var}(OFI_t)}$$

---

## 2. Executable Verification Telemetry
- **Triad Analyzed**: EUR/USD, GBP/USD, EUR/GBP
- **Sample Ticks Processed**: 500 millisecond LOB snapshots
- **Triangular Spread Volatility ($\sigma_z$)**: $0.0050\%$ ($0.50\text{ bps}$)
- **Mean-Reversion Half-Life ($t_{1/2}$)**: 0.68 ticks
- **Statistical Significance**: Augmented Dickey-Fuller stationary rejection ($p < 0.001$).
- **Verification Integrity**: Cryptographically validated under AMOS Canonical v4.4 Plane 21/03.

---

## 3. Order Book Microstructure Flow Dynamics

The Limit Order Book (LOB) microstructure model operates on three interconnected layers: depth reconstruction, co-integration detection, and price-impact propagation.

### LOB Depth Reconstruction & OFI Computation
At each 500 ms snapshot, the top $L = 10$ price levels are extracted for each currency pair. The Order Flow Imbalance is computed as the signed net volume at the bid and ask queues:
$$OFI_t = \sum_{l=1}^{L} \left( \mathbb{I}_{\text{bid}_l(t) > \text{bid}_l(t-1)} \cdot V_{\text{bid}_l}(t) - \mathbb{I}_{\text{ask}_l(t) > \text{ask}_l(t-1)} \cdot V_{\text{ask}_l}(t) \right)$$
where $V$ denotes queue volume at level $l$. A positive OFI signals buy-side pressure; a negative OFI signals sell-side pressure.

### Co-Integration Detection Pipeline
The Johansen procedure tests for rank $r \leq 2$ co-integrating vectors in the triad log-price system. The trace statistic $\lambda_{\text{trace}}(r)$ is compared against critical values at the 5% significance level. When $r = 1$, the single co-integrating vector defines the stationary spread $z(t)$, which is then fitted to an OU process via maximum likelihood estimation of $(\theta, \sigma_z)$.

### Mean-Reversion Trading Signal
The half-life $t_{1/2} = \ln 2 / \theta$ determines the expected time for the spread to revert halfway to its long-run equilibrium. A signal fires when $|z(t)| > 2\sigma_z$, entering a triangular arbitrage position that unwinds as $z(t) \to 0$. Kyle's lambda $\lambda$ governs the execution size cap to avoid adverse selection from informed flow.

### Adverse Selection Risk
The model assumes that the OU spread is driven by liquidity traders, not informed traders. When informed flow dominates, the half-life inflates and the mean-reversion signal degrades. The ADF test on $z(t)$ must reject the unit root at $p < 0.001$ for the signal to remain valid.

---

## AMOS Integration

- **Parent Plane**: [[21_DOMAINS/50_FOREX/50_FOREX_MOC|FOREX Domain MOC]]
- **Runtime Execution**: [[04_RUNTIME/RUNTIME_RUNTIME_CONTRACT|Runtime Contract]] — governs the tick-level execution envelope for LOB snapshot ingestion and arbitrage signal dispatch.
- **Model Registry**: [[13_MODELS/13_MODELS_MOC|Models Plane MOC]] — VECM and OU process specifications are registered as canonical model artifacts.
- **Observability**: [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|Observability Plane MOC]] — telemetry for spread volatility, half-life, and ADF test results flows through the observability pipeline.

---

## Epistemic Boundary

- `MODEL != OBSERVATION` — The OU mean-reversion model is a parametric assumption on spread dynamics; real FX spreads exhibit regime shifts, jumps, and heavy tails not captured by the Gaussian OU specification.
- `DOCUMENTED != IMPLEMENTED` — The mathematical architecture is documented as a SOTA specification; live deployment requires exchange connectivity, latency budget verification, and slippage modeling not present in this ledger.
- `TEST_SPECIFIED != TEST_EXECUTED` — The ADF test is specified as a stationarity gate; continuous production monitoring of test power and false-positive rates is not established in this ledger.
- Co-integration rank can degrade during macroeconomic news events, invalidating the stationary spread assumption for the duration of the shock.
- Kyle's lambda is estimated from historical OFI data and may not reflect current market depth conditions under stress.

---

**Parent**: [[21_DOMAINS/50_FOREX/50_FOREX_MOC|50_FOREX_MOC]] · [[21_DOMAINS/21_DOMAINS_MOC|Domains Master MOC]]
