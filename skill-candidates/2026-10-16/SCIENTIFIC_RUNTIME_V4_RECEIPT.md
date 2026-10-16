# AMOS Scientific Runtime V4 — executable research upgrade
Date: 2026-10-16. Origin architect/steward: Trang Phan.

Verified artifact: https://drive.google.com/file/d/1-9lniO-OYua4sUjOTyykCzmLAEdRXKAA/view
Filename: AMOS_SCIENTIFIC_RUNTIME_V4_20261016.zip
SHA256: c4828d2fb87a580485095c3c04b5780258027a831ed1057dfb546af34f2f3028
Archive size: 9054 bytes.

V4 adds genuine executable adapters in amos_science/advanced.py:
1. eeg_bandpowers: scipy Welch spectral integration for theta/alpha/beta with Nyquist, finite-value and shape guards.
2. bci_loso: scikit-learn LeaveOneGroupOut, train-only scaling and logistic classification, per-subject confusion matrices and shuffled-training-label negative control.
3. donor_pseudobulk: integer raw cell-count aggregation to donor x condition and independent donor counts.
4. assess_verifier: requires external checker receipt before classifying any formal result as conditionally verified.

Retains V3 MNE synthetic EEG, Biopython FASTA QC, group holdout, raw count quality checks and proof admission.

Local test receipt: 10 unittest cases succeeded, 0 failed, Python subprocess exit 0; observed artifact_tool warmup warning did not affect pytest/unittest execution. Libraries already present locally were NumPy, SciPy, scikit-learn, MNE and Biopython. No patient data, device stimulation, internet-side execution or clinical conclusion.

External dependency/agent-Skill research includes K-Dense Scientific Agent Skills (177 directory entries as observed at snapshot), MNE, MOABB, Braindecode, DSPy and scvi-tools. These are separate instruction Skills or libraries and are not automatically installed by this archive.

Status: TESTED_OFFLINE_CANDIDATE; ChatGPT Skill installed: NO; AMOS production installed: NO; real biological/neural datasets benchmarked: NO. Preserve incumbent installed four AMOS bridges and source/canon provenance. Merge/promotion requires independent code/security review and actual runtime readback.
