# AMOS Scientific Typed Tensor V6 — executable validation receipt
Date 2026-10-16; origin architect/steward Trang Phan.
Status: offline synthetic mathematical tests VERIFIED WITHIN TEST SCOPE; real-data scientific validity UNKNOWN; ChatGPT/AMOS runtime installation NOT ESTABLISHED.

Artifact: AMOS_SCIENCE_TENSOR_V6_20261016.zip
SHA-256: dba9aa3bb30063625e4d29b7eb266265a22a23603a48f023452d056127e9f60e

Formal contracts:
EEG X[k,c,t] in volts -> Sigma[k,c,c] in V^2; Sigma=ZZ^T/(T-1), symmetric PSD for T>=2.
EEG linear reference A[c_out,c_in]: Sigma_out=A Sigma_in A^T, preserving PSD.
BCI train/test subjects: groups(I_train) intersect groups(I_test)=empty.
Omics raw counts N[i,j] nonnegative integers -> donor pseudobulk Y[d,j] = sum_{i:donor_i=d} N[i,j], with per-gene total count conservation. Implementation uses arbitrary-precision ints.
Reasoning predictive calibration: Brier=mean((p-y)^2), probabilities within [0,1], y binary, n>=1. External theorem proof remains conditional on a trusted proof checker and statement-bound digest, not an LLM assertion.
Conformal threshold: k=ceil((n+1)*(1-alpha)), q=sorted(scores)[k-1] if k<=n else infinity; finite-sample marginal coverage requires exchangeable calibration/test scores.

Observed executed tests: 18 Python unittest cases passed (18/18, exit 0) covering covariance PSD, re-reference equivalence, malformed dimensionality, leakage, count conservation (100 randomized trials), integer-overflow defense, Brier domain, confusion accounting, proof-receipt admission and conformal boundary cases. No independent scientific dataset or theorem prover tested.

Proposed parent integration: amos-reasoning-evidence-bridge; amos-neuroscience-analysis-bridge; amos-biology-omics-bridge; amos-bci-research-bridge. Mathematical validator parent amos-mathematical-rigor-rscf-kernel. Preserve AMOS SOURCE_CANON separate from this AMOS_MODEL extension. Production and ChatGPT installation remain HOLD until authorized host write and read-back.
