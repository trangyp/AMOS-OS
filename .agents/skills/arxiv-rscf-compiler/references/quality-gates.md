# AMOS Quality Gates & Epistemic Verification Checklist

Before finalizing or committing any compiled `AMOS_KNOWLEDGE_OBJECT`, the compiler must execute the following 7-dimension quality audit.

---

## 1. Source Fidelity Gate
- [ ] **No Invented Metadata**: Authors, dates, arXiv IDs, and page counts must exactly match the source.
- [ ] **No Altered Constants**: Physical constants, numerical tables, and convergence exponents must be exact.
- [ ] **No Fabricated Proofs**: If a paper cites another work for a step, state `cited_external_proof` rather than inventing an in-situ proof.

---

## 2. Theorem & Mathematical Integrity Gate
- [ ] **Assumptions Explicitly Stated**: Every theorem block must list its required regularity conditions (e.g. standardness, positive reach, smoothness).
- [ ] **Scope Preserved**: Do not drop dimensional restrictions ($d=2, 3$ vs. arbitrary $d$) or geometric constraints (compact, convex, bounded).
- [ ] **Sufficient $\neq$ Necessary**: Mark whether a condition is sufficient, necessary, or an equivalence.
- [ ] **Bound $\neq$ Equality**: Do not convert an upper bound $O(n^{-1/4})$ into an exact rate without lower bound proof.
- [ ] **Asymptotic $\neq$ Finite-Sample**: Clearly distinguish $n \to \infty$ limits from finite-$n$ guarantees.

---

## 3. Epistemic Integrity Gate
- [ ] **Weakest Accurate Class**: Use the most conservative classification:
  $$\text{SOURCE\_CLAIM} \quad\Big|\quad \text{OBSERVATION} \quad\Big|\quad \text{DERIVED} \quad\Big|\quad \text{MODEL} \quad\Big|\quad \text{CONDITIONAL} \quad\Big|\quad \text{UNKNOWN}$$
- [ ] **Simulation $\neq$ Real-World Validation**: Mark numerical runs on synthetic grids as `SIMULATION`, reserving `OBSERVATION` for real physical/clinical data.
- [ ] **Correlation $\neq$ Causation**: Mark statistical associations and regressions as `ASSOCIATION` unless causal identification is rigorously established.
- [ ] **Unknowns Preserved**: Open questions and unproven conjectures must remain tagged as `UNKNOWN/GAP`.

---

## 4. Provenance & Version Gate
- [ ] **Exact Version Tracked**: Track whether the source is `v1`, `v2`, or a journal reprint.
- [ ] **No Silent Merging**: Do not merge claims from `v1` and `v2` without noting version lineage.
- [ ] **Citation Independence**: Descendants of a single original paper must not be counted as multiple independent validations.

---

## 5. Dependency & Invalidation Gate
- [ ] **Weakest Premises Isolated**: Identify the specific assumptions most vulnerable to failure (e.g. `positive_reach`, `low_salt_approximation`).
- [ ] **Local Invalidation Functional**: Verify that if a weak premise fails, the blast radius correctly invalidates dependent theorems without destroying unrelated results.

---

## 6. Token & Deduplication Gate
- [ ] **Deduplicate by Key**: Reference conditions and variables by key rather than rewriting long definitions repeatedly.
- [ ] **Zero Conclusion-Changing Pruning**: Never eliminate a caveat, boundary condition, or counterexample to save tokens.

---

## 7. Completeness Gate
- [ ] **Accurate Ingestion State**:
  - Set `ingestion_state: NORMALIZED_FROM_PRIMARY_SOURCE` *only* if all material sections, appendices, and proofs were inspected.
  - If only abstract and main results were reviewed, set `ingestion_state: PARTIAL_NORMALIZATION`.

---

## Conceptual Test Harness by Paper Type

### Test A: Pure Theory Papers (Mathematics / Formal Logic)
*Must verify:*
1. Full definitions of mathematical structures.
2. Explicit assumption list for every Theorem/Lemma/Proposition.
3. Proof backbone isolating load-bearing lemmas.
4. Optimal vs non-optimal convergence rates and constants.
5. Exact invalidation conditions if assumptions are violated.

### Test B: Empirical / Experimental Papers (Physics / Biology / Medicine)
*Must verify:*
1. Exact sample size ($N$), data collection regime, and measurement apparatus.
2. Baselines, control groups, and statistical confidence intervals ($\pm \sigma$).
3. Explicit separation between raw observational data and theoretical model fits.
4. Measurement limitations, sensor noise, and systematic error bars.

### Test C: Hybrid / Applied Papers (Image Processing / Algorithms / Engineering)
*Must verify:*
1. Theoretical algorithm bounds separated from empirical benchmark scores.
2. Simulation parameters (grid sizes, synthetic noise levels) distinguished from real-world data.
3. Practical application scope (e.g. medical imaging, hardware requirements) marked as `APPLIED_CASE_STUDY`, not universal clinical validation.
