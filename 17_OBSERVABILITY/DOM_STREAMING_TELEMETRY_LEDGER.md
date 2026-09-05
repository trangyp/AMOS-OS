---
title: Forex L2/L3 Depth-of-Market (DOM) — Live Telemetry Ledger
type: telemetry_ledger
plane: 17_OBSERVABILITY
domain_ref: 21_DOMAINS/50_FOREX
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
status: ACTIVE_TELEMETRY
epistemic_class: EMPIRICAL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: EMPIRICAL
  provenance:
    - 17_OBSERVABILITY/REALTIME_ORDERBOOK_DOM_STREAMING_VISUALIZER
    - 21_DOMAINS/50_FOREX/50_FOREX_MOC
    - 15_INTERFACES/FOREX_FIX44_ZEROMQ_SOCKET_ADAPTER
  scope: live_dom_telemetry
---

# Forex L2/L3 Depth-of-Market (DOM) — Live Telemetry Ledger

> **Asset:** `XAUUSD (Spot Gold)`
> **Telemetry Stream Status:** `100% OPERATIONAL (60 FPS Stream)`
> **Best Bid / Ask:** `$2650.0 / $2650.3`
> **Midprice:** `$2650.15` | **Microprice:** `$2650.196`
> **Spread:** `$0.3` | **Order Book Imbalance (OBI):** `+0.070`
> **Cryptographic Stream Receipt:** `d7dfa9d57edb8c0ba24a2db912fdc740bafd119cae322df85ffa13b350ca9e8c`

---

## 1. Real-Time ASCII Depth-of-Market Ladder

```text
========================================================================================
   AMOS QUANTITATIVE ENGINE — REAL-TIME DEPTH-OF-MARKET (XAUUSD)
   Midprice: $2650.15 | Microprice: $2650.196 | Spread: $0.3 | OBI: +0.070
========================================================================================
 Level |      Ask Depth (Lots)      |   Price   |      Bid Depth (Lots)      | Imbalance
-------+----------------------------+-----------+----------------------------+-----------
 L5    | [██████████████████  ] 18.29 |  2651.10  |                            |   +18.29
 L4    | [███████████████     ] 15.83 |  2650.90  |                            |   +15.83
 L3    | [████████████████████] 21.92 |  2650.70  |                            |   +21.92
 L2    | [███                 ]  3.34 |  2650.50  |                            |   + 3.34
 L1    | [█████               ]  5.59 |  2650.30  |                            |   + 5.59
-------+----------------------------+-----------+----------------------------+-----------
 SPREAD| >>> SPREAD: $0.30  <<<    |  2650.15  | >>> MIDPRICE <<<           |   OBI: +0.07
-------+----------------------------+-----------+----------------------------+-----------
 L1    |                            |  2650.00  | [██████████          ] 10.61 |   -10.61
 L2    |                            |  2649.80  | [████████████████████] 23.87 |   -23.87
 L3    |                            |  2649.60  | [██████████████████  ] 18.84 |   -18.84
 L4    |                            |  2649.40  | [███████████████     ] 15.77 |   -15.77
 L5    |                            |  2649.20  | [█████               ]  5.59 |   - 5.59
========================================================================================
```

---

## 2. Quantitative Microstructure Metrics

| Metric | Measured Value | Operational SLA / Interpretation |
| :--- | :--- | :--- |
| **Spread** | **$0.3** | Normal institutional spread ($\le \$0.50$) |
| **Top-of-Book Asymmetry** | Bid: 10.61 Lots \| Ask: 5.59 Lots | Skewed toward Buyers |
| **Microprice Drift** | $\Delta = 0.046$ | Predictive directional pressure indicator |
| **Total 5-Level Depth** | Bid: 74.68 Lots \| Ask: 64.97 Lots | Total available book liquidity |
| **Order Book Imbalance (OBI)** | **+0.070** | Normalized skew parameter $\in [-1, 1]$ |

---

## 3. Operational Invariants Verified

- `INV-OBS-001` (**Sub-16.6ms Render SLA**): Telemetry stream frame rate confirmed at 60 FPS.
- `INV-OBS-002` (**Zero Queue Drop**): 10-level L2 delta processing queue drop rate $= 0.000\%$.
- `INV-OBS-003` (**Microprice Drift SLA**): $|P_{\text{micro}} - P_{\text{mid}}| = 0.046 \le 2 \times \text{Spread}$.

---

## 4. Master Navigation & Bindings

- [[17_OBSERVABILITY/REALTIME_ORDERBOOK_DOM_STREAMING_VISUALIZER|REALTIME_ORDERBOOK_DOM_STREAMING_VISUALIZER]] — Observability Specification.
- [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY_MOC]] — Observability Master Map.
- [[21_DOMAINS/50_FOREX/50_FOREX_MOC|50_FOREX_MOC]] — Forex Domain Map.
