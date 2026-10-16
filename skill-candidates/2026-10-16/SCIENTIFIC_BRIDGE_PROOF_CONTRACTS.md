# AMOS Scientific Bridge Proof Contracts — 2026-10-16
Origin steward: Trang Phan. Candidate upgrade to existing Skills; not source canon and not an installation receipt.

## Routing, cross-domain typed interface
Parent nodes: amos-reasoning-evidence-bridge (R), amos-neuroscience-analysis-bridge (N), amos-biology-omics-bridge (O), amos-bci-research-bridge (B).
Each emits a typed evidence capsule E=(schema,axes,units,source_sha,subject_scope,regime,time,assumptions,results,uncertainty,falsifiers,authority).
The bridge does not infer missing input units, subject IDs or biological references. All unobserved entries become UNKNOWN, not zero. Cross-scale composition must use an explicit translation operator with a declared information-loss boundary.

## N: EEG/MEG and spikes
X in Real[K,C,T] (V, trial/channel/time), sample-rate fs in Hz and reference A in Real[Cout,C].
Z_k=X_k-mean_t(X_k); S_k=Z_k Z_k^T/(T-1) in V². Invariant S=S^T and v^T S v >=0 for finite real X, T>1.
After linear referencing, S'_k=A S_k A^T. This transforms covariance but does not magically improve acquisition quality.
One-sided periodogram at f: PSD_f=c_f |DFT(Z)_f|²/(fs*T) in V²/Hz with c_f=1 at DC and Nyquist (for even T), 2 otherwise. Summing PSD*df yields variance; avoid interpreting PSD bins as physiological causes.
MNE-Python for time-series measurement, NeuroKit2 for physiology and SpikeInterface for extracellular sorting are tool families, NOT the same data modality or an installation certificate.
Adversarial tests: dimensional mismatch; fs<=0; reference mismatch; Nyquist violation; artifacts; timestamp drift; sensor identity mismatch; T<2; nonfinite signal. Spatial connectivity and source localization require separate inverse-problem assumptions.

## B: BCI offline decoding and generalization
Dataset D=(X[N,C,T],y[N],g[N],session[N],clock[N]); labels y from declared task, not mind states.
Subject-generalization: for each held-out group h, I_test={i:g_i=h}, I_train=remaining; groups(I_test) intersection groups(I_train)=empty. Never fit scaler, ICA, CSP, feature selection or hyperparameters on test examples.
Prefer MOABB standard datasets/evaluation protocol and compare CSP+linear, pyRiemann tangent-space, Braindecode architectures only with the same folds, preprocessing and tuning budgets. Label-shuffled negative controls should approach chance under a correctly controlled experiment; departures trigger diagnostics rather than an automatic fraud verdict.
Empirical risk estimate Rhat=sum_i L(y_i,predict_i)/N; this is descriptive, not deployment risk. Report group bootstrap uncertainty, confidence calibration, per-subject dispersion and subject count. A high synthetic metric is not empirical generalization.
No live device control, stimulation or medical use by default; BrainFlow is a device acquisition library requiring explicit protocol and authority.

## O: molecular genomics, single-cell, spatial transcriptomics
Counts M in nonnegative integers[cells,genes], donor d_i and condition c_i; genomic reference assembly and annotation version must be fixed before comparing features.
Pseudobulk Y[d,c,j]=sum_i 1[d_i=d and c_i=c] M[i,j]; per-gene conserved total sum_dc Y[d,c,j]=sum_i M[i,j]. Implement Python integer accumulation to avoid fixed-width overflow.
For m null-hypothesis p-values sorted p_(1)<=...<=p_(m), BH q_(i)=min_{k>=i} min(1,m p_(k)/k); valid FDR interpretation requires statistically valid p-values and accepted null dependency conditions, not just numerical monotonicity.
Donor, not cell, is often the independent biological replication unit. Batch confounding, doublets, ambient RNA, barcode errors and selection bias must be considered. CellRank pseudotime and Squidpy spatial neighborhoods are inferential associations, not directly observed cellular lineage or causal mechanisms.
Genome coordinate contract: 1-based inclusive [s,e] maps to zero-based half-open [s-1,e), with fixed build/contig/strand; interval math without assembly identity is insufficient for biological equivalence.

## R: rigorous reasoning, probabilistic models and formal proof
Proof object P=(formal_claim,proof_artifact,checker_identity,checker_version,axiom_scope,result,hash). Accept only externally checked claims under explicitly registered axioms. Unsat from a solver proves unsatisfiability of the encoded formula under solver assumptions, not empirical truth.
For Bernoulli predictions p_i, label y_i in {0,1}, Brier=mean_i(p_i-y_i)^2, 0<=Brier<=1 and N>=1. Expected calibration error is bin-dependent, not a certified probability bound.
Split conformal threshold k=ceil((n+1)(1-alpha)); q=ordered_score[k] (1-based), +inf if k>n. Coverage theorem requires score construction without target leakage and exchangeability; time-dependent EEG and cohort-shift biology can violate that.
Probabilistic programming (Pyro/NumPyro) requires prior assumptions, posterior predictive checks, chain convergence and sensitivity; DSPy metric optimization requires held-out data and cannot certify correctness by self-evaluation.

## Scientific intake tensor + bounded optimizer
Candidate capability C in Bool[n,m]; baseline B in Bool[r,m]; seven-gate evidence tensor G in Bool[n,7]. Candidate permissions are separate from host compatibility and all gates.
Given normalized w in simplex and one-unit costs c>=0, select x in Bool[n] maximizing union coverage:
max sum_j w_j (1-max_r B_rj) 1[sum_i x_i C_ij>=1]
subject to sum_i c_i x_i<=budget, prerequisites x_i<=x_d, conflicts x_i+x_j<=1, x_i<=H_i product_k G_ik.
This is AMOS_MODEL governance mathematics, not evidence that any selected Skill improves science.
Hard invariants: missing witness => HOLD; version mismatch => HOLD; same semantic origin does not count twice; no reviewer-approved installed source overwrite; commit-time authority freshness rechecked.

## Source-classification and provenance
K-Dense scientific-agent-skills collection hosts 177 instruction-Skill directories at observed pinned snapshot a1043ef544e3a100c28e70a736b6cf32554d0677. Domain examples include scientific-critical-thinking, neuropixels-analysis, scanpy, neurokit2, biopython, genomic-coordinates, cellxgene-census, statsmodels, cellprofiler, alphagenome, scientific-brainstorming.
External Python tool libraries include mne, MOABB, Braindecode, DSPy, Scanpy, scvi-tools, SpikeInterface, Brian2, pyRiemann and BrainFlow; do NOT conflate installing Python dependencies with registering a ChatGPT Skill.
Source metadata and Skill instructions are not independently audited trust. Security, license, device permission, dependency version, and empirical generalization remain validation gates.

## RSCF scoped capsule
ID: RSCF-AMOS-SCIENTIFIC-BRIDGE-CONTRACTS-20261016
Class: DERIVED for algebraic identities; MODEL for AMOS routing/promotion; OBSERVATION only for executed CI receipts.
Scope: offline research and synthetic tests, Oct 2026 snapshot.
Competing: trial-level cross-validation vs subject-out; cell-level DE vs donor-level; LLM self-check vs external checker.
Falsifiers: failed invariant, leaked fold, missing donor/assembly or uncertainty evidence, independent holdout regression, license conflict, stale authority.
Consequence: HOLD (candidate), not canonical promotion or clinical/device authorization.
