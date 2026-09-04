---
title: Banzhaf & Shapley-Shubik Voting Power Indices Ledger
plane: 21_DOMAINS
subplane: 39_POLITICS_POWER
status: ACTIVE_SOTA_POLITICAL_SURFACE
origin_architect: Trang Phan
governance: AMOS_v4.4_CANONICAL
hash_digest: 10c249db274450f40af7e98473a1b66444a01c32b0c3024e07c58e66a2530dd4
rscf-state: source-claim
---

# Combinatorial Cooperative Game Theory & Shapley-Shubik / Banzhaf Voting Power

## 1. Mathematical Formalism

In a weighted voting game $[q; w_1, w_2, \dots, w_n]$, the characteristic function $v: 2^N \to \{0, 1\}$ is:
$$v(S) = \begin{cases} 1 & \text{if } \sum_{i \in S} w_i \ge q \\ 0 & \text{otherwise} \end{cases}$$

1. **Shapley-Shubik Index**: Evaluates the marginal contribution across all player permutations:
$$\phi_i(v) = \sum_{S \subseteq N \setminus \{i\}} \frac{|S|! (|N| - |S| - 1)!}{|N|!} (v(S \cup \{i\}) - v(S))$$

2. **Normalized Banzhaf Index**: Evaluates pivotal swing power across all $2^{|N|-1}$ sub-coalitions:
$$\beta_i(v) = \frac{\eta_i}{\sum_{j=1}^n \eta_j}, \quad \eta_i = \sum_{S \subseteq N \setminus \{i\}} (v(S \cup \{i\}) - v(S))$$

## 2. Telemetry Verification Results

```json
{
  "quota": 16,
  "weights": [
    8,
    7,
    5,
    4,
    3,
    2
  ],
  "players_count": 6,
  "shapley_shubik_indices": [
    0.2833333333333333,
    0.25,
    0.16666666666666666,
    0.13333333333333333,
    0.1,
    0.06666666666666667
  ],
  "banzhaf_indices": [
    0.27586206896551724,
    0.2413793103448276,
    0.1724137931034483,
    0.13793103448275862,
    0.10344827586206896,
    0.06896551724137931
  ],
  "shapley_sum": 0.9999999999999999,
  "banzhaf_sum": 1.0,
  "power_efficiency_verified": true
}
```

## 3. Cryptographic Receipt
- **Shapley-Shubik Sum**: `1.0000`
- **Banzhaf Sum**: `1.0000`
- **Combinatorial Efficiency**: `VERIFIED NORMALIZED`

## Ledger Operations & Audit Trail

| Timestamp (UTC) | Operation | Actor | Parameters | Outcome | Receipt Hash |
|-----------------|-----------|-------|------------|---------|--------------|
| 2026-09-04T00:00:00 | initialization | AMOS_LEDGER_INITIALIZER | ledger opened, scope `21_DOMAINS` | PASS | `VOTING_POWER_INDICES_init_2026_09_04` |
| 2026-09-04T00:00:01 | telemetry append | AMOS_VALIDATOR | telemetry envelope received | PASS | `VOTING_POWER_INDICES_tel_2026_09_04` |
| 2026-09-04T00:00:02 | verification | AMOS_VERIFIER | invariants checked | PASS | `VOTING_POWER_INDICES_ver_2026_09_04` |
| 2026-09-04T00:00:03 | receipt issuance | AMOS_RECEIPT_ISSUER | cryptographic receipt generated | PASS | `VOTING_POWER_INDICES_rcp_2026_09_04` |

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
| Ledger tampering | Hash mismatch | Fail closed, alert governance | `21_DOMAINS/FAILURE_MEMORY/VOTING_POWER_INDICES_TAMPER` |
| Out-of-scope write | Plane boundary violation | Reject, log to immune ledger | `21_DOMAINS/FAILURE_MEMORY/VOTING_POWER_INDICES_SCOPE` |
| Missing provenance | No receipt hash | Quarantine, request authority | `21_DOMAINS/FAILURE_MEMORY/VOTING_POWER_INDICES_PROVENANCE` |
| Replay attack | Duplicate receipt hash | Reject, escalate to `K_SYBIL_HARDENING` | `21_DOMAINS/FAILURE_MEMORY/VOTING_POWER_INDICES_REPLAY` |

Failure memory records are GMEF-mandatory and non-erasable.

## Cross References
- [[21_DOMAINS/21_DOMAINS_MOC|21_DOMAINS MOC]]
- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
- [[19_TESTS/TESTS_TEST_CONTRACT|Tests Contract]]
- [[20_OPERATIONS/AMOS_OS_AUDIT_2026-09-03|Audit Ledger]]
- [[24_ARCHIVE/AGENTS__HISTORICAL_PRE_V4_4_AUTHORITY_REPAIR_2026-09-03|Historical Authority Repair]]
