---
title: "Forex FIX 4.4 & ZeroMQ Low-Latency Socket Adapter Specification"
type: interface_specification
plane: 15_INTERFACES
domain_ref: 21_DOMAINS/50_FOREX
amos_core_target: v4.4
origin_architect: Trang Phan
steward: Trang Phan
status: ACTIVE_INTERFACE
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 21_DOMAINS/50_FOREX/FOREX_DOMAINS_INTERFACES
    - 21_DOMAINS/50_FOREX/DOMAINS_FOREX_CONTRACT
    - 15_INTERFACES/INTERFACES_README
  scope: low_latency_socket_bridge
tags:
  - amos-os
  - interfaces
  - forex
  - fix44
  - zeromq
  - low-latency
  - socket-bridge
---

# Forex FIX 4.4 & ZeroMQ Low-Latency Socket Adapter Specification

## 1. Executive Summary & Interface Architecture

The **Forex FIX 4.4 & ZeroMQ Socket Adapter** (`15_INTERFACES`) provides the ultra-low-latency interprocess communication (IPC) bridge between the AMOS Quantitative Trading Brain and external execution surfaces (Institutional ECNs, MetaTrader 5 bridges, and FIX gateways).

```
+----------------------------------------------------------------------------------------------------+
|                         LOW-LATENCY MULTI-PROTOCOL EXECUTION BRIDGE                                |
|                                                                                                    |
|    [ AMOS Quantitative Core (Plane 21 / 03_FOREX) ]                                                |
|                            ||                                                                      |
|               +------------+------------+                                                          |
|               |                         |                                                          |
|               \/                        \/                                                         |
|    [ ZeroMQ IPC Socket Server ]   [ FIX 4.4 Tag-Value Engine ]                                     |
|    - Endpoint: `ipc:///tmp/amos`  - TLS Socket / Port 9800                                        |
|    - Format: ProtoBuf / JSON-RPC  - MsgTypes: 35=D, 35=8, 35=V                                     |
|    - Latency: $< 1.5\text{ms}$    - Checksum: Tag 10 Modulo 256                                    |
|               ||                        ||                                                         |
|               +------------+------------+                                                          |
|                            ||                                                                      |
|                            \/                                                                      |
|    [ Risk Governance Gate (03_CONTROL_PLANE: INV-FOREX-001 / INV-PORT-001) ]                       |
|                            ||                                                                      |
|                            \/                                                                      |
|    [ Institutional Liquidity Venue / ECN Execution Report ]                                        |
+----------------------------------------------------------------------------------------------------+
```

---

## 2. Protocol Specifications & Packet Schemas

### 2.1 FIX 4.4 Tag-Value Encoding
Standard institutional protocol over TLS 1.3 socket:
- **Delimiter**: SOH (`\x01`, ASCII 01).
- **Mandatory Header Fields**:
  - `8=FIX.4.4` (BeginString)
  - `9=BodyLength`
  - `35=MsgType` (`D` = New Order Single, `8` = Execution Report, `V` = Market Data Request, `0` = Heartbeat)
  - `49=SenderCompID` (`AMOS_QUANT_01`)
  - `56=TargetCompID` (`LIQUIDITY_ECN_01`)
  - `34=MsgSeqNum`
  - `52=SendingTime` (UTC ISO-8601 with microsecond resolution)
- **Mandatory Trailer**:
  - `10=CheckSum` (3-digit ASCII sum of all preceding bytes modulo 256).

### 2.2 Sample FIX 4.4 New Order Single (`35=D`)
```text
8=FIX.4.4|9=142|35=D|49=AMOS_QUANT_01|56=LIQUIDITY_ECN_01|34=1042|52=20260904-12:00:00.000|11=ORD_XAU_9812|55=XAUUSD|54=1|38=0.50|40=1|44=2650.00|59=0|10=184|
```

### 2.3 ZeroMQ Local IPC Bridge
- **Socket Pattern**: `ROUTER / DEALER` for multi-threaded asynchronous order dispatch, or `PUB / SUB` for L1/L2 tick feeds.
- **URI**: `ipc:///tmp/amos_forex_bridge.ipc` or `tcp://127.0.0.1:5555`.
- **Payload Framing**:
  ```json
  {
    "msg_id": "REQ-ZMQ-20260904-001",
    "action": "SUBMIT_ORDER",
    "symbol": "XAUUSD",
    "side": "BUY",
    "volume": 0.50,
    "order_type": "MARKET",
    "stop_loss": 2646.00,
    "take_profit": 2658.00,
    "max_slippage_pips": 2.5,
    "hmac_signature": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
  }
  ```

---

## 3. Fail-Safe Disconnect & Safety Invariants

1. **Heartbeat Loss (Dead-Man Switch)**: If heartbeat (`35=0`) is unacknowledged for $> 2,000\text{ms}$, all active limit orders are cancelled and socket enters emergency quarantine.
2. **Spread Anomaly Filter**: If bid-ask spread expands by $> 3.5\times$ above moving average, socket blocks outgoing orders.
3. **Sequence Number Desynchronization**: Incoming sequence gaps immediately trigger Resend Request (`35=2`).

---

## 4. Operational Invariants

- `INV-IFACE-001` (**Sub-5ms IPC SLA**): ZeroMQ tick-to-order round-trip processing must complete within $\le 5.0\text{ms}$.
- `INV-IFACE-002` (**Strict Checksum Verification**): Every FIX frame must validate `Tag 10` checksum before entering the trading bus.
- `INV-IFACE-003` (**Cryptographic Nonce Signing**): All ZeroMQ order payloads must carry a valid HMAC-SHA256 signature signed by the active session key.

---

## 5. Master Navigation & Bindings

- **Forex Domain:** [[21_DOMAINS/50_FOREX/50_FOREX_MOC|50_FOREX_MOC]]
- **Interface MOC:** [[15_INTERFACES/15_INTERFACES_MOC|15_INTERFACES_MOC]]
- **Integration Log:** [[15_INTERFACES/FIX_ZEROMQ_INTEGRATION_LOG|FIX_ZEROMQ_INTEGRATION_LOG]]
