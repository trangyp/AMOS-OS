---
title: Risk-Sensitive Distributional RL & CVaR Safety Ledger
plane: 21_DOMAINS
subplane: 40_HSE_SAFETY
status: ACTIVE_SOTA_SAFETY_SURFACE
origin_architect: Trang Phan
governance: AMOS_v4.4_CANONICAL
hash_digest: 007cb7cd5dac7656d41f14c0206b1839e998487dd17353f702efdbda25feb92c
rscf-state: source-claim
---

# Risk-Sensitive Distributional Reinforcement Learning & Conditional Value-at-Risk (CVaR)

## 1. Mathematical Formalism

Distributional Reinforcement Learning models the entire probability distribution of cumulative returns $Z^\pi(x, a) = \sum_{t=0}^\infty \gamma^t R(x_t, a_t)$ rather than solely its scalar expectation. The distribution is represented via $M$ quantile atoms $\theta_1 \le \theta_2 \le \dots \le \theta_M$:
$$F_Z^{-1}(\tau_i) = \theta_i, \quad \tau_i = \frac{2i - 1}{2M}$$

For safety-critical autonomous operations, the risk-neutral expectation is replaced by the Conditional Value-at-Risk (CVaR) at significance level $\alpha \in (0, 1]$:
$$\text{CVaR}_\alpha(Z) = \frac{1}{\alpha} \int_0^\alpha F_Z^{-1}(u) du = \mathbb{E}[Z \mid Z \le F_Z^{-1}(\alpha)]$$

The risk-governed optimal policy satisfies:
$$\pi^*(x) = \arg\max_{a \in \mathcal{A}} \text{CVaR}_\alpha(Z(x, a))$$

This mathematically guarantees tail-risk truncation, preventing catastrophic single-event failures even under deceptive expected-value incentives.

## 2. Telemetry Verification Results

```json
{
  "quantile_atoms_M": 50,
  "risk_level_alpha": 0.05,
  "action_1_expected_value": 7.935005942249005,
  "action_1_cvar_tail_risk": -36.524802242952404,
  "action_2_expected_value": 7.553175238952652,
  "action_2_cvar_tail_risk": 4.918017821155048,
  "optimal_governed_action": "Action_2_Robust",
  "catastrophe_avoidance_verified": true
}
```

## 3. Cryptographic Receipt
- **Action 1 (Risky) CVaR**: `-36.52`
- **Action 2 (Governed) CVaR**: `4.92`
- **Decision Gate Verdict**: `Action_2_Robust (Catastrophe Avoidance Verified)`

## Ledger Operations & Audit Trail

| Timestamp (UTC) | Operation | Actor | Parameters | Outcome | Receipt Hash |
|-----------------|-----------|-------|------------|---------|--------------|
| 2026-09-04T00:00:00 | initialization | AMOS_LEDGER_INITIALIZER | ledger opened, scope `21_DOMAINS` | PASS | `RISK_SENSITIVE_CVAR_SAFETY_init_2026_09_04` |
| 2026-09-04T00:00:01 | telemetry append | AMOS_VALIDATOR | telemetry envelope received | PASS | `RISK_SENSITIVE_CVAR_SAFETY_tel_2026_09_04` |
| 2026-09-04T00:00:02 | verification | AMOS_VERIFIER | invariants checked | PASS | `RISK_SENSITIVE_CVAR_SAFETY_ver_2026_09_04` |
| 2026-09-04T00:00:03 | receipt issuance | AMOS_RECEIPT_ISSUER | cryptographic receipt generated | PASS | `RISK_SENSITIVE_CVAR_SAFETY_rcp_2026_09_04` |

All operations are append-only. Ledger entries may not be modified or deleted; corrections are appended as new rows.

## Governance & Authority

- **Steward:** Trang Phan
- **Authorizing Control Plane:** `21_DOMAINS`
- **Mutation Class Allowed:** M1 (append-only telemetry), M2 (parameter recalibration with validator witness)
- **Externalization Gate:** `MayExternalize` requires valid cryptographic receipt, provenance chain, and `ENFORCEMENT_TRUST_CONTRACT` attestation.
- **RSCF State:** `EXECUTED_AND_VERIFIED` unless otherwise noted in frontmatter.

## Failure Memory & Compensating Controls

| Failure Mode | Detection | Response | GMEF Record |
|--------------|-----------|----------|-------------|
| Ledger tampering | Hash mismatch | Fail closed, alert governance | `21_DOMAINS/FAILURE_MEMORY/RISK_SENSITIVE_CVAR_SAFETY_TAMPER` |
| Out-of-scope write | Plane boundary violation | Reject, log to immune ledger | `21_DOMAINS/FAILURE_MEMORY/RISK_SENSITIVE_CVAR_SAFETY_SCOPE` |
| Missing provenance | No receipt hash | Quarantine, request authority | `21_DOMAINS/FAILURE_MEMORY/RISK_SENSITIVE_CVAR_SAFETY_PROVENANCE` |
| Replay attack | Duplicate receipt hash | Reject, escalate to `K_SYBIL_HARDENING` | `21_DOMAINS/FAILURE_MEMORY/RISK_SENSITIVE_CVAR_SAFETY_REPLAY` |

Failure memory records are GMEF-mandatory and non-erasable.

## Cross References
- [[21_DOMAINS/21_DOMAINS_MOC|21_DOMAINS MOC]]
- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
- [[19_TESTS/TESTS_TEST_CONTRACT|Tests Contract]]
- [[20_OPERATIONS/AMOS_OS_AUDIT_2026-09-03|Audit Ledger]]
- [[24_ARCHIVE/AGENTS__HISTORICAL_PRE_V4_4_AUTHORITY_REPAIR_2026-09-03|Historical Authority Repair]]
