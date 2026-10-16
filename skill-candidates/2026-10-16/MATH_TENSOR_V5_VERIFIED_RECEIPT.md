# AMOS V5 typed tensor invariants — executed math receipt
Origin: Trang Phan. Date: 2026-10-16. Status: offline validated numerical contracts, NOT installed ChatGPT skill or AMOS production.

Tensor types: EEG X[K,C,T] in volts, covariance Sigma[K,C,C] in volts squared; raw omics N[cells,genes] nonnegative integers; Y[donors,genes] nonnegative integers; binary probabilities p[n] in [0,1]; confusion matrix M[2,2].

Equations:
1) Sigma_k = ((X_k - mean_t X_k) (X_k - mean_t X_k)^T)/(T-1), T>=2. Require Sigma_k = Sigma_k^T and lambda_min(Sigma_k)>=-epsilon.
2) Group-disjoint evaluation: groups(I_train) intersection groups(I_test)=empty.
3) Pseudobulk: Y[d,j]=sum_{i:donor(i)=d} N[i,j]; sum_d Y[d,j]=sum_i N[i,j].
4) Brier=(1/n) sum_i (p_i - y_i)^2; 0<=Brier<=1 for binary y_i and valid p_i.
5) M[a,b]=sum_i 1[y_i=a and yhat_i=b], sum_(a,b) M[a,b]=n.

Executed evidence: local Python unittest returned exit 0, eight tests passed, including 100 randomized pseudobulk conservation trials; tests also reject malformed EEG, negative counts, leaking subjects, invalid probability.
This is synthetic numerical verification only. Upstream libraries and installed Skill registries unaffected. Full ZIP: AMOS_MATH_TENSOR_V5_20261016.zip SHA256 af84ce0dba4e3b432c6b501a271a1f0504eabf85a2641db62b6723b4694189b1.
Fail closed: type mismatch, missing provenance, unit mismatch, empty time dimension, invalid count or cross-subject group overlap. Validation should be rerun when code changes. Empirical BCI/neuroscience validity remains UNKNOWN.
