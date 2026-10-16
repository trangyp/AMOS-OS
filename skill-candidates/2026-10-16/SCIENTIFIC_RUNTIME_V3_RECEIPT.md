# AMOS Scientific Runtime V3 — execution receipt
Date: 2026-10-16. Origin steward: Trang Phan.

A runnable research package containing MNE, Biopython, sklearn and NumPy adapters was built and tested in an isolated local session (6 of 6 tests passed). It is stored in AMOS Drive as `AMOS_SCIENTIFIC_RUNTIME_V3_20261016.zip` at https://drive.google.com/file/d/1PYfStm1AgcvVTSXFLhSmM8wcz2hnrxKv/view

SHA256: `9bdcad0cb322d5fb01963293b500f06c99309f41e618a28ff87b38d2e7b30c74`
Observed environment: numpy 2.3.5; scikit-learn 1.8.0; mne 1.11.0; biopython 1.86.
Tests cover participant-grouped BCI feature cross-validation, MNE synthetic EEG spectral power, Biopython offline FASTA QC, raw-count integrity and proof-checker admission guard. These are synthetic/local software tests, not real-dataset validation.
Not installed in ChatGPT or AMOS production. No source code autoexecuted from external GitHub repositories. Real datasets, toolchain compatibility and permission/security checks remain prerequisites.

**Promotion state: HOLD / candidate**. Use the Drive ZIP as exact content source; do not infer that this receipt or passing CI installs the runtime.
