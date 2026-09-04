---
title: "Forex Domain — Interfaces & Connectivity Specifications"
type: interface_specification
source: 21_DOMAINS/03_FOREX
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_INTERFACE_SPECIFICATION
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 21_DOMAINS/03_FOREX/FOREX_DOMAINS_PROVENANCE
    - 15_INTERFACES/INTERFACES_INTERFACE_CONTRACT
  scope: forex_interfaces
tags:
  - amos-os
  - domains
  - forex
  - fix-protocol
  - mt5-api
  - streaming
---

# Forex Domain — Interfaces & Connectivity Specifications

## 1. System Surface Architecture

The Forex domain connects to institutional liquidity providers and retail broker bridges via four typed interface protocols:

```mermaid
graph TD
    A[AMOS Quantitative Forex Engine] --> B[FIX 4.4 Financial Exchange Surface]
    A --> C[MetaTrader 5 ZeroMQ IPC Bridge]
    A --> D[Binance / Crypto REST & WebSocket Stream]
    A --> E[Dukascopy Historical Tick Ingestion Pipeline]
```

---

## 2. Interface Protocols

### 2.1 FIX 4.4 Institutional Bridge
- **Standard:** Tag-value financial protocol over TLS socket.
- **Message Types Supported:**
  - `35=D` (New Order Single)
  - `35=8` (Execution Report)
  - `35=V` (Market Data Request - L2 Snapshot/Incremental)
  - `35=W` (Market Data Snapshot Full Refresh)
- **Heartbeat Interval:** 30 seconds (`35=0`).

### 2.2 MetaTrader 5 ZeroMQ IPC Socket
- **Architecture:** Local Unix domain socket or TCP `127.0.0.1:5555`.
- **Payload Format:** High-performance JSON-RPC / Protocol Buffers.
- **Latency SLA:** Round-trip tick-to-order $< 5	ext{ms}$.

---

## 3. Fail-Safe Disconnect & Circuit Breaker

1. **Heartbeat Loss:** If market data stream stalls for $> 2.0	ext{s}$, all pending limit orders are cancelled immediately.
2. **Spread Anomaly:** If bid-ask spread widens by $> 3.5	imes$ historical moving average, trading pauses automatically.
