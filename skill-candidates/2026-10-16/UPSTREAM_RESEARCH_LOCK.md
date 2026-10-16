# External source checkpoints — 2026-10-16

Status: research candidates only; no external package installation, executable validation or canon promotion.

| Repository | Git commit | Role |
|---|---|---|
| K-Dense-AI/scientific-agent-skills | a1043ef544e3a100c28e70a736b6cf32554d0677 | instruction skills (research, not bulk import) |
| stanfordnlp/dspy | 869874767729866f96f77e757a685ee72fb663a5 | reasoning software |
| mne-tools/mne-python | 8f498626a53704a6a96bcd8a11e22cbd8866efa5 | neural signals |
| NeuroTechX/moabb | 0e3b1d9ed798198413a8c4b0da6213a188ad76e8 | BCI benchmarks |
| braindecode/braindecode | 573215292ed6919c128cd97a6cc528414d852e10 | EEG deep learning |
| brainflow-dev/brainflow | e3caf4b7289a2616efb76c8a3276d2c2086fd488 | sensor acquisition |
| pyRiemann/pyRiemann | acfcd1ac9bc05c19387e53c848b103cb91262b71 | classical BCI baselines |
| scverse/scanpy | 8ed52d9dad906c260e52405380ed4ed1e353d4e7 | single-cell analysis |
| scverse/scvi-tools | 5555ecc11049b11ee98fedc1e64e56b65df6b591 | probabilistic omics |
| brian-team/brian2 | 9f803d0c81901024a653249dd5d8c09575feb226 | neural simulation |

Source snapshots from GitHub API. K-Dense scientific-critical-thinking, neurokit2, neuropixels-analysis, scanpy and biopython instruction files were inspected. A science library is not automatically an installable ChatGPT Skill. Licensing and code-execution permission checks are pending.

## Validation and ownership gates
Compare frozen baseline and candidate. For BCI enforce subject-disjoint testing and acquisition consent; for single-cell analysis enforce donor-aware separation; for formal reasoning use a deterministic checker; for cross-modal neuroscience require verified sample/time joins. Keep clinical interpretation and real-time hardware control out of automatic activation. Preserve existing AMOS skill owner identities and unresolved aliases. Mark state STAGED_NOT_INSTALLED until successful runtime readback.
