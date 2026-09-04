---
title: Real-Time Order-Book Depth-of-Market (DOM) L2/L3 Streaming Visualizer
type: observability_specification
plane: 17_OBSERVABILITY
domain_ref: 21_DOMAINS/03_FOREX
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
status: ACTIVE_SPECIFICATION
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 17_OBSERVABILITY/17_OBSERVABILITY_MOC
    - 21_DOMAINS/03_FOREX/03_FOREX_MOC
    - 15_INTERFACES/FOREX_FIX44_ZEROMQ_SOCKET_ADAPTER
  scope: dom_orderbook_streaming
tags:
  - amos-os
  - observability
  - forex
  - depth-of-market
  - dom
  - l2-l3-orderbook
  - ofi
  - microprice
---

# Real-Time Order-Book Depth-of-Market (DOM) L2/L3 Streaming Visualizer

## 1. Executive Summary & Telemetry Architecture

The **Real-Time Order-Book Depth-of-Market (DOM) L2/L3 Streaming Visualizer** (`17_OBSERVABILITY`) provides microsecond-level observability into institutional market depth, bid/ask liquidity ladders, Order Flow Imbalance (OFI), and microprice drift for AMOS quantitative execution algorithms.

```
+----------------------------------------------------------------------------------------------------+
|                         L2/L3 DEPTH-OF-MARKET STREAMING TELEMETRY PIPELINE                         |
|                                                                                                    |
|    [ FIX 4.4 Market Data Snapshot `35=W` / Incremental Refresh `35=X` (15_INTERFACES) ]            |
|                                            ||                                                      |
|                                            \/                                                      |
|    [ L2/L3 10-Level Order-Book Reconstruction Engine (Bids & Asks Sorted by Price-Time Priority) ] |
|                                            ||                                                      |
|                                            \/                                                      |
|    [ Microstructure Feature Extractor: Microprice, OFI, Cumulative Volume Delta (CVD) ]            |
|                                            ||                                                      |
|                                            \/                                                      |
|    [ Real-Time 60 FPS Telemetry Stream & Terminal ANSI Ladder Dashboard (17_OBSERVABILITY) ]       |
+----------------------------------------------------------------------------------------------------+
```

---

## 2. Microstructure Mathematical Formulation

### 2.1 Microprice Calculation
While the midprice $P_{\text{mid}} = \frac{P_a^{(1)} + P_b^{(1)}}{2}$ ignores volume asymmetry, the **Microprice** weights top-of-book quotes by opposing liquidity:

$$P_{\text{micro}} = \frac{v_b^{(1)} P_a^{(1)} + v_a^{(1)} P_b^{(1)}}{v_a^{(1)} + v_b^{(1)}}$$

When buy volume $v_b^{(1)} \gg v_a^{(1)}$, $P_{\text{micro}} \to P_a^{(1)}$, predicting imminent upward price movement.

### 2.2 Order Flow Imbalance (OFI)
For discrete time intervals $\Delta t = t_k - t_{k-1}$:

$$\text{OFI}_k = I_{\{P_b(k) \ge P_b(k-1)\}} v_b(k) - I_{\{P_b(k) \le P_b(k-1)\}} v_b(k-1) - \left( I_{\{P_a(k) \le P_a(k-1)\}} v_a(k) - I_{\{P_a(k) \ge P_a(k-1)\}} v_a(k-1) \right)$$

where $I_{\{\cdot\}}$ is the indicator function. Positive $\text{OFI}_k > 0$ signals aggressive buyer demand consuming ask depth.

---

## 3. Real-Time ANSI Terminal DOM Ladder Architecture

```text
========================================================================================
   AMOS QUANTITATIVE ENGINE — REAL-TIME DEPTH-OF-MARKET (XAUUSD)
   Midprice: $2650.15 | Microprice: $2650.28 | Spread: 0.30 | OFI: +8.40 Lots | VPIN: 0.142
========================================================================================
 Level |      Ask Depth (Lots)      |   Price   |      Bid Depth (Lots)      | Imbalance
-------+----------------------------+-----------+----------------------------+-----------
 L5    | [██████████] 12.50         |  2650.90  |                            |   +12.50
 L4    | [███████] 8.20             |  2650.70  |                            |    +8.20
 L3    | [█████] 5.40               |  2650.50  |                            |    +5.40
 L2    | [███] 3.10                 |  2650.40  |                            |    +3.10
 L1    | [█] 1.20                   |  2650.30  |                            |    +1.20
-------+----------------------------+-----------+----------------------------+-----------
 SPREAD| >>> SPREAD: $0.30 <<<      |  2650.15  | >>> MIDPRICE <<<           |   OFI: +8.4
-------+----------------------------+-----------+----------------------------+-----------
 L1    |                            |  2650.00  | [████████] 9.60            |    -9.60
 L2    |                            |  2649.80  | [████████████] 14.20       |   -14.20
 L3    |                            |  2649.60  | [████████████████] 18.50   |   -18.50
 L4    |                            |  2649.40  | [███████████] 13.10        |   -13.10
 L5    |                            |  2649.20  | [████████████████████]24.00|   -24.00
========================================================================================
```

---

## 4. Operational Invariants & Telemetry SLAs

- `INV-OBS-001` (**Sub-16.6ms Render SLA**): Telemetry stream must refresh at $\ge 60\text{ FPS}$ ($\Delta t \le 16.6\text{ ms}$).
- `INV-OBS-002` (**Zero Queue Drop**): L2/L3 incremental delta processing queue drop rate $= 0.000\%$.
- `INV-OBS-003` (**Microprice Drift Alert**): $|P_{\text{micro}} - P_{\text{mid}}| > 2.0 \times \text{Spread}$ triggers immediate order book imbalance warning to `03_CONTROL_PLANE`.

---

## 5. Master Navigation & Bindings

- **Observability MOC:** [[17_OBSERVABILITY/17_OBSERVABILITY_MOC|17_OBSERVABILITY_MOC]]
- **DOM Telemetry Ledger:** [[17_OBSERVABILITY/DOM_STREAMING_TELEMETRY_LEDGER|DOM_STREAMING_TELEMETRY_LEDGER]]
- **Forex Domain:** [[21_DOMAINS/03_FOREX/03_FOREX_MOC|03_FOREX_MOC]]
- **Socket Adapter:** [[15_INTERFACES/FOREX_FIX44_ZEROMQ_SOCKET_ADAPTER|FOREX_FIX44_ZEROMQ_SOCKET_ADAPTER]]
