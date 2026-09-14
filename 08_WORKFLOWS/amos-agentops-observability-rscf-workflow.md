---
title: amos-agentops-observability-rscf-workflow
type: workflow
skill: amos-agentops-observability-rscf
agent: amos-agentops-observability-rscf-agent
origin_architect: Trang Phan
version: 2.0.0
epistemic_class: AMOS_MODEL
---

# AMOS AgentOps Observability Workflow

State machine:

`INTAKE -> BIND_SUBJECT -> SELECT_CAPTURE -> START_TRACE -> OBSERVE -> RECORD_MISSINGNESS -> CLOSE_SPANS -> VERIFY_LEDGER -> BUILD_RECEIPT -> CLAIM_GATE -> TERMINAL`

## Gates

1. **INTAKE** — define the runtime/agent behavior being observed and the claim the trace is intended to support or falsify.
2. **BIND_SUBJECT** — bind subject identity/version, environment, provenance root and scope.
3. **SELECT_CAPTURE** — default `METADATA_ONLY`; permit `REDACTED_CONTENT` only when content is decision-relevant and persistence is authorized.
4. **START_TRACE** — create one trace root; reject orphan or cross-trace parentage.
5. **OBSERVE** — use typed spans: `WORKFLOW|AGENT|MODEL|TOOL|MEMORY|EFFECT|EVAL`.
6. **RECORD_MISSINGNESS** — record expected/captured/dropped signal counts and cause where known.
7. **CLOSE_SPANS** — terminal status is `OK|ERROR|IN_DOUBT|CANCELLED`; external effect state remains a separate observation.
8. **VERIFY_LEDGER** — hash/lineage mismatch invalidates evidence.
9. **BUILD_RECEIPT** — bind trace identity, subjects, environments, coverage and effect states.
10. **CLAIM_GATE** — enforce:
   - `TRACE != AUTHORITY`
   - `TRACE_EDGE != CAUSAL_PROOF`
   - `SPAN_SUCCESS != EFFECT_COMMITTED`
   - `NO_SPAN != NO_EVENT`
11. **TERMINAL** — return `OBSERVED`, `INCOMPLETE`, `IN_DOUBT`, or `INVALIDATED_EVIDENCE` with gaps.

## Recovery

- Exporter/backend ambiguity: mark coverage gap; do not infer successful export.
- Ambiguous external effect: `IN_DOUBT -> observe/reconcile -> retry|compensate|finalize` only after discrimination.
- Sensitive payload discovered in telemetry: quarantine the telemetry artifact, rotate/revoke secrets when applicable, and re-run with metadata-only or corrected redaction.
- Missing authority: telemetry may record an authority reference, but cannot supply or mint it.

## Validation surfaces

- `python -m unittest -v 19_TESTS/test_agent_trace_runtime.py`
- `python 07_SKILLS/amos-agentops-observability-rscf/scripts/trace_contract_check.py --self-test`

GitHub CI is the branch validation authority for the repository copy.
