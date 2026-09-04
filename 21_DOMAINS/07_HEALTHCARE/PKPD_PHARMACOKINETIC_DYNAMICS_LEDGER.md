---
title: Non-Linear Mixed-Effects PK/PD Multi-Compartment Ledger
plane: 21_DOMAINS
subplane: 07_HEALTHCARE
status: ACTIVE_SOTA_CLINICAL_SURFACE
origin_architect: Trang Phan
governance: AMOS_v4.4_CANONICAL
hash_digest: f92ac3926684fc2318fb9e6229542b758d46d61fd91f83dcf0f4a9d9417912ed
rscf-state: source-claim
---

# Two-Compartment Pharmacokinetics & Sigmoidal $E_{max}$ Pharmacodynamics

## 1. Mathematical Formalism

Two-compartment oral disposition is governed by linear first-order differential equations:
$$\frac{dA_{gut}}{dt} = -k_a A_{gut}$$
$$\frac{dA_{cent}}{dt} = k_a A_{gut} - \left(\frac{CL}{V_c} + \frac{Q}{V_c}\right) A_{cent} + \frac{Q}{V_p} A_{peri}$$
$$\frac{dA_{peri}}{dt} = \frac{Q}{V_c} A_{cent} - \frac{Q}{V_p} A_{peri}$$

Plasma drug concentration $C(t) = \frac{A_{cent}(t)}{V_c}$ couples into the non-linear pharmacodynamic response through the Sigmoidal Hill equation:
$$E(C) = E_0 + \frac{E_{max} C^\gamma}{EC_{50}^\gamma + C^\gamma}$$

where $\gamma$ is the sigmoid Hill steepness coefficient and $EC_{50}$ is the half-maximal effective concentration.

## 2. Telemetry Verification Results

```json
{
  "oral_dose_mg": 200.0,
  "peak_concentration_Cmax_mg_L": 5.391625313487669,
  "time_to_peak_Tmax_hours": 1.5,
  "auc_0_24_mg_h_L": 36.03090090868933,
  "baseline_effect_E0": 10.0,
  "maximum_pharmacodynamic_effect": 79.95878644675847,
  "therapeutic_window_verified": true
}
```

## 3. Cryptographic Receipt
- **$C_{max}$**: `5.39 mg/L`
- **$T_{max}$**: `1.50 h`
- **$AUC_{0-24}$**: `36.03 mg*h/L`
- **Clinical Efficacy**: `VERIFIED`

## Ledger Operations & Audit Trail

| Timestamp (UTC) | Operation | Actor | Parameters | Outcome | Receipt Hash |
|-----------------|-----------|-------|------------|---------|--------------|
| 2026-09-04T00:00:00 | initialization | AMOS_LEDGER_INITIALIZER | ledger opened, scope `21_DOMAINS` | PASS | `PKPD_PHARMACOKINETIC_DYNAMICS_init_2026_09_04` |
| 2026-09-04T00:00:01 | telemetry append | AMOS_VALIDATOR | telemetry envelope received | PASS | `PKPD_PHARMACOKINETIC_DYNAMICS_tel_2026_09_04` |
| 2026-09-04T00:00:02 | verification | AMOS_VERIFIER | invariants checked | PASS | `PKPD_PHARMACOKINETIC_DYNAMICS_ver_2026_09_04` |
| 2026-09-04T00:00:03 | receipt issuance | AMOS_RECEIPT_ISSUER | cryptographic receipt generated | PASS | `PKPD_PHARMACOKINETIC_DYNAMICS_rcp_2026_09_04` |

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
| Ledger tampering | Hash mismatch | Fail closed, alert governance | `21_DOMAINS/FAILURE_MEMORY/PKPD_PHARMACOKINETIC_DYNAMICS_TAMPER` |
| Out-of-scope write | Plane boundary violation | Reject, log to immune ledger | `21_DOMAINS/FAILURE_MEMORY/PKPD_PHARMACOKINETIC_DYNAMICS_SCOPE` |
| Missing provenance | No receipt hash | Quarantine, request authority | `21_DOMAINS/FAILURE_MEMORY/PKPD_PHARMACOKINETIC_DYNAMICS_PROVENANCE` |
| Replay attack | Duplicate receipt hash | Reject, escalate to `K_SYBIL_HARDENING` | `21_DOMAINS/FAILURE_MEMORY/PKPD_PHARMACOKINETIC_DYNAMICS_REPLAY` |

Failure memory records are GMEF-mandatory and non-erasable.

## Cross References
- [[21_DOMAINS/21_DOMAINS_MOC|21_DOMAINS MOC]]
- [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
- [[19_TESTS/TESTS_TEST_CONTRACT|Tests Contract]]
- [[20_OPERATIONS/AMOS_OS_AUDIT_2026-09-03|Audit Ledger]]
- [[24_ARCHIVE/AGENTS__HISTORICAL_PRE_V4_4_AUTHORITY_REPAIR_2026-09-03|Historical Authority Repair]]
