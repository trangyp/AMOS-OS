# AMOS Scientific Invariants V8 — reproducible artifact receipt
Date: 2026-10-16. Origin steward: Trang Phan.
Source archive: https://drive.google.com/file/d/1AO4SwgYs-6F9WmMYJxOeKx4XMtrpyxE4/view
SHA256: 26be67e68805facd4bacfda5f70ce963ada9eab0d1c6203944e0b5c55c7abb31
ZIP size: 8113 bytes.
Local execution: 26 Python unittest cases passed, 0 failures, process exit 0; randomized tests use seeded inputs.

Typed tensors: EEG X[trial,channel,time] V -> bandpower P[trial,channel] V^2; omics raw N[cell,gene] nonnegative integers -> Y[donor,condition,gene] exact integer sums; BCI X[trial,feature] with participant group index; reasoning binary probabilities p[n] and labels y[n].

New V8 invariants:
EEG periodogram P(f)=2 |FFT(z)|^2/(fs T) for interior rFFT frequencies, with DC/Nyquist un-doubled; bandpower sum_f P(f)*df, df=fs/T; power scales as amplitude squared, frequency and Nyquist checked.
BCI leave-one-subject-out: intersection(train groups,test groups)=empty; fresh estimator cloning and fitting each fold, training set must contain both classes. Synthetic accuracy is a contract check only.
Pseudobulk: Y[d,c,j]=sum_{i:donor_i=d and condition_i=c} N[i,j]; per-gene total conservation; Python arbitrary precision avoids int64 aggregate overflow.
ECE= sum_bins(n_b/n) * abs(mean(p_b)-mean(y_b)), requiring valid Bernoulli p,y; explicitly bin dependent, not conformal/coverage guarantee.
Retains V7 covariance PSD, re-reference equivalence, split-conformal threshold, Brier domain, seven-boolean promotion gate, count conservation.

Status: STAGED_TESTED_OFFLINE, not production/ChatGPT installed, not real-data validated. Canon is unchanged. Activation requires host installer, security and license checks, scientific benchmark and current authority.
