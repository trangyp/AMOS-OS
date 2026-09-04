---
title: "15_INTERFACES MOC — Interfaces & System Surfaces"
type: moc
source: 15_INTERFACES
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE_MOC
epistemic_class: AMOS_MODEL
conclusion_class: DERIVED
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance:
    - 00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE
    - 00_ROOT/00_ROOT_MOC
  scope: 15_interfaces_navigation
tags:
  - amos-os
  - 15_interfaces
  - moc
  - navigation
---

# 15_INTERFACES MOC — Interfaces & System Surfaces

**Origin Architect / Steward:** Trang Phan
**AMOS_CORE Target:** `v4.4`
**Epistemic Class:** `AMOS_MODEL`

---

## 1. System Interface Specifications

- [[15_INTERFACES/WEB_BASED_BCI_OPTOGENETIC_NEURAL_FLOW_DECODER|WEB_BASED_BCI_OPTOGENETIC_NEURAL_FLOW_DECODER]] — Real-time 60 FPS WebGL/HTML5 Canvas visual neural flow decoder, HD-DOT cortical fluorescence grid ($128 \times 128$), and holographic SLM phase maps.
- [bci_neural_flow_visualizer.html](bci_neural_flow_visualizer.html) — Interactive standalone Web application visualizer for BCI & optogenetic closed-loop telemetry.
- [[15_INTERFACES/AUTOMATED_EVENT_DRIVEN_WEBHOOK_DISPATCHER|AUTOMATED_EVENT_DRIVEN_WEBHOOK_DISPATCHER]] — Cryptographically signed (HMAC-SHA256 / Ed25519) HTTP/3 webhook dispatcher with exponential backoff and DLQ spillover.
- [[15_INTERFACES/WEBHOOK_DISPATCHER_EXECUTION_LEDGER|WEBHOOK_DISPATCHER_EXECUTION_LEDGER]] — Event delivery trace, idempotency verification, and cryptographic receipts.
- [[15_INTERFACES/FOREX_FIX44_ZEROMQ_SOCKET_ADAPTER|FOREX_FIX44_ZEROMQ_SOCKET_ADAPTER]] — Low-latency FIX 4.4 tag-value serialization, Tag 10 checksum verification, and ZeroMQ IPC socket bridge ($< 1.0\text{ms}$).
- [[15_INTERFACES/FIX_ZEROMQ_INTEGRATION_LOG|FIX_ZEROMQ_INTEGRATION_LOG]] — Live simulated socket bridge execution trace, packet hex dumps, and latency receipts.
- [[15_INTERFACES/INTERFACES_README|INTERFACES_README]] — WASI 0.2 WIT components, OpenAPI 3.1 cryptographic headers, and gRPC IPC protocols.
- [[15_INTERFACES/INTERFACES_INTERFACE_CONTRACT|INTERFACES_INTERFACE_CONTRACT]] — Invariants governing interface non-repudiation, deterministic schema evolution, and rate limiting.
- [[15_INTERFACES/00_INDEX/INTERFACE_MAP|INTERFACE_MAP]] — System interface navigation map

---

## 2. Invariants

```text
CAPABILITY != AUTHORITY
OBSERVED != CURRENT
PROPOSAL != COMMIT
UNKNOWN/GAP != PASS
```

---

## 3. Parent Navigation

- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]] — Master Navigation Hub
- [[00_ROOT/FULL_BRAIN_OS_MECE_ARCHITECTURE|FULL_BRAIN_OS_MECE_ARCHITECTURE]] — Full OS Partition Architecture
