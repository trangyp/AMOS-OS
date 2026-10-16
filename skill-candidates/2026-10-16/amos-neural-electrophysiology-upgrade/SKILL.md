---
name: amos-neural-electrophysiology-upgrade
description: Analyze EEG, MEG, spikes and neural events using reproducible signal processing. Use for scoped AMOS amos neural electrophysiology upgrade workflows requiring source provenance and validation.
---

# amos-neural-electrophysiology-upgrade

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
Require channel montage, sampling frequency, event timestamps and artifact policy.

## Reference projects (not bundled, not installed)
MNE-Python, Neo, Elephant, SpikeInterface. External packages require independent security/license review; no `curl | sh` or blind pip installs.

## Failure mode
Unverified dependencies, ambiguous units or provenance, biological privacy concerns, schema mismatch or unvalidated performance: HOLD / QUARANTINE. Do not claim execution or installation.

## Evidence-backed methods and checks (2026-10-16)
- MNE-Python commit `8f498626a53704a6a96bcd8a11e22cbd8866efa5`: record `Raw.info` channel types, units, montage and sample frequency; never perform filtering before storing the raw-data hash and filter settings.
- Inspect K-Dense `neuropixels-analysis` Skill at `a1043ef544e3a100c28e70a736b6cf32554d0677` as a distinct external source. Its stated targets include SpikeInterface 0.105.0, ProbeInterface 0.4.0 and Neo 0.14.5; optional proprietary/model-dependent features are not automatically enabled.
- Synthetic validation: generate clean sine+artifact channels, assert channel count/time alignment after resampling, event-onset consistency within one sample, and finite, nonnegative spectral power. These are code-contract tests, not biological validity tests.
- Actual neural recordings: capture device and file format, measurement provenance, artifact exclusions, run/session split and sensor references. If acquisition metadata or consent is missing, HOLD.
- Preserve high-density electrophysiology and scalp EEG as distinct methods; do not map units/spikes onto scalp channels without an independently validated translation.
