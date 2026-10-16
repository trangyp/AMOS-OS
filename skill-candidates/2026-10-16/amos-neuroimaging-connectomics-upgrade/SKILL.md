---
name: amos-neuroimaging-connectomics-upgrade
description: Analyze fMRI and neural connectivity with explicit preprocessing, confounds and multiplicity controls. Use for scoped AMOS amos neuroimaging connectomics upgrade workflows requiring source provenance and validation.
---

# amos-neuroimaging-connectomics-upgrade

**Owner / origin:** Trang Phan (AMOS). **Status:** CANDIDATE — no automatic runtime activation or canon promotion.

## Contract
Parent route: `amos-neuroscience-analysis-bridge`. Inputs: research objective; authorized dataset; modality; study design; baseline; tool availability; source snapshots; validation policy. Outputs: typed analysis proposal/results; errors and uncertainties; RSCF capsule; unresolved dependencies; reproducibility receipt.

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
Do not claim functional coupling proves anatomical wiring or causation.

## Reference projects (not bundled, not installed)
Nilearn, Nipype, MNE-Connectivity. External packages require independent security/license review; no `curl | sh` or blind pip installs.

## Failure mode
Unverified dependencies, ambiguous units or provenance, biological privacy concerns, schema mismatch or unvalidated performance: HOLD / QUARANTINE. Do not claim execution or installation.
