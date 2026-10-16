# AMOS scientific GitHub intake v10 — source verified scope
Date 2026-10-16. Origin architect Trang Phan. Classification: research candidate; no runtime installation.

Agent Skills collection: K-Dense-AI/scientific-agent-skills, pinned observation a1043ef544e3a100c28e70a736b6cf32554d0677. Its /skills directory returned 177 entries. Five pinned SKILL.md files were inspected: scientific-critical-thinking, neuropixels-analysis, scanpy, neurokit2, biopython. Agent instructions are not Python packages; their compatibility and executable effects need separate review.

Scientific libraries inspected via GitHub metadata: mne-tools/mne-python (BSD-3-Clause), NeuroTechX/moabb (BSD-3-Clause), braindecode/braindecode (BSD-3-Clause), scverse/scanpy (BSD-3-Clause), scverse/scvi-tools (BSD-3-Clause), stanfordnlp/dspy (MIT), SpikeInterface/spikeinterface (MIT), brian-team/brian2 (NOASSERTION). These are repository metadata license indicators, not full license or supply-chain audits. NeuroTechX/pyRiemann path returned NOT_FOUND: do not promote that identifier.

Actual executable enhancement: scientific-math-v10/selection.py computes exact finite coverage selection under capability incidence C[n,m], installed B[r,m], gates G[n,7], host H[n], normalized weights w[m], nonnegative costs, dependencies and conflicts; result REVIEW_ONLY. mathematical equation:
maximize sum_j w_j (1-max_r B_rj)*1[sum_i x_i C_ij>=1]
subject to sum_i cost_i*x_i<=budget, x_i<=H_i*prod_k G_ik, prerequisite and conflict edges. For n<=20 exact enumeration is finite, but cannot establish empirical candidate quality.

CI: workflow validate-amos-neuro-candidates.yml runs test_selection.py plus preexisting tests. GitHub Actions run 38932660796 completed SUCCESS for commit 7acd95a984cb0b38411d8d2f172bd81a0c2ead10. Tests show deterministic finite-model behavior only; not upstream security or scientific performance. Review existing AMOS bridges; do not duplicate Skills.

Remaining: inspect source scripts and references per upstream Skill; security/license compatibility; dependency/version testing; real public EEG/BCI/single-cell holdouts; runtime host installer and readback; merge authorization.
