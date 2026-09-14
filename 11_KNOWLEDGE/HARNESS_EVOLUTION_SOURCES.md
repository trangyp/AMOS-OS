---
title: AMOS Harness Evolution Source Registry
type: source-registry
origin_architect: Trang Phan
epistemic_class: DERIVED
status: active
---

# Harness Evolution Source Registry

This registry pins mechanism sources used by the local AMOS harness-evolution reference implementation. Repository statements and benchmark numbers remain `SOURCE_CLAIM` unless independently rerun.

## External sources

### Agentic Harness Engineering

- Repository: `china-qijizhifeng/agentic-harness-engineering`
- Pinned commit: `8b2a55d97590363fe50c3cc6b5e833b020a4bb4c`
- Adapted: explicit harness component classes; evidence/root-cause/targeted-fix change manifests; predicted fix/regression sets; next-evaluation verification.
- Related component-detection repair: `faf44bc4aea57413c520bc5711c6ebf628e0da1e` adds exact `LongTermMEMORY.md` detection.
- Boundary: reported benchmark improvements are not AMOS-verified performance evidence.

### NexAU

- Repository: `nex-agi/NexAU`
- Pinned commit: `4d3767e41f43b617f484c75ae1b51704dee26ff0`
- Adapted: separately typed prompt/tool/skill/sub-agent/middleware contributions; fail-fast undeclared variables; strict manifest/config handling.
- Boundary: AMOS repository classes `AGENT_CONFIG|WORKFLOW|POLICY_CONFIG|TOOL_REGISTRY` are AMOS extensions, not NexAU claims.

### Harbor

- Repository: `harbor-framework/harbor`
- Pinned commit: `4008e2df847e445b0b3c41cff852b5460a62bfb7`
- Adapted: lifecycle-aware cleanup of shared-verifier `/tests` and `/logs/verifier` state before the next agent phase; preserve legitimate agent-owned state when no shared verifier residue exists.
- Invariant: `VERIFIER_OR_REWARD_LEAKAGE_INVALIDATES_COMPARATIVE_EVIDENCE`.

### SWE-agent

- Repository: `SWE-agent/SWE-agent`
- Scanned commit: `3ea751c087f32b16e039a2233dd6eefecef325d5`
- Role: contemporary coding-agent/benchmark boundary reference.
- No unique load-bearing mechanism from this scan is promoted into the local runtime; retain as contextual source only.

## Internal AMOS dependencies

### Interactive evaluation

- Repository: `trangyp/AMOS-OS`
- Lineage head: `b86cfae1dc5628a9249ef6fd587c836eac127443` (PR #19)
- Provides: exact run identity, coverage/sealing, comparable baseline/candidate receipts, fixes/regressions/critical-regressions.

### Evaluator calibration

- Repository: `trangyp/AMOS-OS`
- Lineage head: `aa46e695f6dc6f1cd4860e36758ff8074aa5a0d4` (PR #22)
- Provides: held-out evaluator validation, reliability-gate evidence, evaluator/config identity.

## Provenance rule

Do not count forks, mirrors, copied benchmark descriptions, or repeated descendants as independent confirmation. Mechanism adoption does not adopt source authority, benchmark validity, or deployment safety.
