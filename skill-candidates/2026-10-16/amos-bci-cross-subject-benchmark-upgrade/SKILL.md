---
name: amos-bci-cross-subject-benchmark-upgrade
description: Benchmark BCI decoders across subjects and sessions with leakage prevention. Use for scoped AMOS amos bci cross subject benchmark upgrade workflows requiring source provenance and validation.
---

# amos-bci-cross-subject-benchmark-upgrade

**Owner / origin:** Trang Phan (AMOS). **Status:** CANDIDATE — no automatic runtime activation or canon promotion.

## Contract
Parent route: `amos-bci-research-bridge`. Inputs: research objective; authorized dataset; modality; study design; baseline; tool availability; source snapshots; validation policy. Outputs: typed analysis proposal/results; errors and uncertainties; RSCF capsule; unresolved dependencies; reproducibility receipt.

## Procedure
1. Verify parent and current AMOS registry/version; identify overlap before selecting this child.
2. Resolve each external code dependency to verified repo origin, commit SHA, license, required privileges and compatible environment; otherwise HOLD.
3. Define inputs and measurement units, cohort/study design, baseline and negative controls.
4. Separate source claims, AMOS models, hypotheses and independently executed results. Preserve competing explanations.
5. Only run allowlisted, sandboxed code where execution is authorized; use split-by-subject/donor/session or other study-appropriate separation and no test-set tuning.
6. Test statistical significance or calibration and out-of-distribution behavior where feasible; record versions, seeds, artifact hashes and full failure traces.
7. Return explicit RSCF: ID, claim/class, H/M/L if appropriate, premises, evidence/semantic origin, timestamp, scope/version/regime, dependencies, competitors, falsifiers, confidence ceiling, invalidation triggers.
8. Request parent/control-plane approval for writes, device effects, privacy-sensitive material or runtime promotion. No implicit authority.

## Scientific guard
Cross-subject held-out split must be genuinely independent; no medical claims.

## Reference projects (not bundled, not installed)
MOABB, Braindecode, pyRiemann. External packages require independent security/license review; no `curl | sh` or blind pip installs.

## Failure mode
Unverified dependencies, ambiguous units or provenance, biological privacy concerns, schema mismatch or unvalidated performance: HOLD / QUARANTINE. Do not claim execution or installation.

## Executable acceptance contract
Upstream pins: MOABB `0e3b1d9ed798198413a8c4b0da6213a188ad76e8`; Braindecode `573215292ed6919c128cd97a6cc528414d852e10`; pyRiemann `acfcd1ac9bc05c19387e53c848b103cb91262b71`. Before running, lock Python/package builds and licenses. Split entire subjects into train/validation/test; nested model selection stays within training subjects; held-out subjects are evaluated exactly once. Report N subjects, sessions, class balance, paradigm, metrics, 95% uncertainty intervals and failure counts. Compare chance level, CSP + linear baseline, tangent-space + logistic baseline, and deep model only when resources permit. Test random-label shuffle and subject-ID permutation to detect leakage. Clinical outcomes and realtime device commands excluded.
