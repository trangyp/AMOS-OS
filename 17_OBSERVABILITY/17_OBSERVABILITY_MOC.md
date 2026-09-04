---
title: 17_OBSERVABILITY MOC — Observability & Epistemic Health
type: moc
source: 17_OBSERVABILITY
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
  scope: 17_observability_navigation
tags:
  - amos-os
  - 17_observability
  - moc
  - navigation
---

# 17_OBSERVABILITY MOC — Observability & Epistemic Health

**Origin Architect / Steward:** Trang Phan
**AMOS_CORE Target:** `v4.4`
**Epistemic Class:** `AMOS_MODEL`

---

## 1. Observability Specifications & Telemetry Visualizers

- [[17_OBSERVABILITY/REALTIME_ORDERBOOK_DOM_STREAMING_VISUALIZER|REALTIME_ORDERBOOK_DOM_STREAMING_VISUALIZER]] — Real-time 60 FPS 10-level Depth-of-Market (DOM) streaming visualizer, Microprice drift, and Order Flow Imbalance (OFI).
- [[17_OBSERVABILITY/DOM_STREAMING_TELEMETRY_LEDGER|DOM_STREAMING_TELEMETRY_LEDGER]] — Live ASCII Depth-of-Market telemetry trace, liquidity ladders, and invariant receipts.
- [[17_OBSERVABILITY/OBSERVABILITY_README|OBSERVABILITY_README]] — OpenTelemetry collectors, metric schemas, trace contexts, and alert routes.
- [[17_OBSERVABILITY/OBSERVABILITY_OBSERVABILITY_CONTRACT|OBSERVABILITY_OBSERVABILITY_CONTRACT]] — Invariants: non-authoritative metrics, monotonic sequence IDs, sub-100ms emission latency.
- [[17_OBSERVABILITY/00_INDEX/OBSERVABILITY_OBSERVABILITY_MAP|OBSERVABILITY_OBSERVABILITY_MAP]] — Observability navigation map

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
