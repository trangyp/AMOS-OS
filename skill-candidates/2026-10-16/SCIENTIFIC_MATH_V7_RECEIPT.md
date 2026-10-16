# AMOS Scientific Math V7 — verified candidate receipt
Date 2026-10-16. Origin architect/steward: Trang Phan.
Artifact: https://drive.google.com/file/d/1XQksbimt8zBpRAjro8QRv823CE3liOdR/view
SHA256: a024aba4e02c186602756eb4c31eeca52b463ee9a4cb163a05a20278ee1b3ab5
Status: OFFLINE_NUMERICAL_TESTS_PASSED; CHATGPT_INSTALL=NOT_DONE; PRODUCTION_DEPLOY=NOT_DONE.

Tensor/logic interfaces:
EEG X[K,C,T] in volts; covariance S[K,C,C] in V^2. Equations S=ZZ^T/(T-1); S_referenced = A S A^T. PSD and reference-transform equality tested.
Omics counts N[cells,genes] nonnegative integer; donor pseudobulk Y[donors,genes] conserves total counts; Python integer accumulator avoids int64 overflow.
BCI split: train/test participant group intersection empty; duplicate/out-of-range indices disallowed.
Reasoning Brier score = mean((p-y)^2), y binary and 0<=p<=1; split conformal quantile k=ceil((n+1)(1-alpha)), threshold infinity when k>n, coverage requires exchangeability.
Governance: promotable = host_compatible AND authority_current AND conjunction of 7 typed boolean gates.
Observed test output: 15 unittest cases passed; one test exercised 100 randomized pseudobulk conservation cases. These are synthetic implementation tests, not real EEG/BCI/omics external validity or formal theorem proof.
Source basis: AMOS mathematical rigor skill and candidate 2026-10-16 upstream research; upstream libraries are NOT copied or installed by this package. RSCF candidate class AMOS_MODEL / CONDITIONAL, invalidate on code or axis/unit changes.
