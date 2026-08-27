# Canonical Example Node: 0708.2180v1 (Annals of Statistics 2007)

```yaml
AMOS_KNOWLEDGE_OBJECT:
  schema_family: RSCF
  schema_role: KNOWLEDGE_RSCF
  schema_version: "AMOS_CORE_v4.4-compatible-conceptual"
  object_status: ACTIVE_REFERENCE
  ingestion_state: NORMALIZED_FROM_PRIMARY_SOURCE
  mutation_policy: APPEND_OR_VERSION_NEVER_SILENT_OVERWRITE

  # ============================================================
  # 0. IDENTITY / FRACTAL ADDRESS
  # ============================================================

  identity:
    node_id: "RSCF.KNOWLEDGE.MATHEMATICS.STATISTICS.NONPARAMETRIC_SET_ESTIMATION.MINKOWSKI_CONTENT.0708_2180"
    canonical_slug: "0708_2180v1_nonparametric_estimation_lengths_surface_areas"
    canonical_title: "A Nonparametric Approach to the Estimation of Lengths and Surface Areas"
    source_title: "A NONPARAMETRIC APPROACH TO THE ESTIMATION OF LENGTHS AND SURFACE AREAS"
    preferred_path:
      H: "11_KNOWLEDGE/mathematics/statistics"
      M: "nonparametric_set_estimation/minkowski_content/surface_area"
      L: "arxiv/2007/0708_2180v1"
    legacy_path: "11_KNOWLEDGE/_arxiv_md/2007/0708_2180V1_A_NONPARAMETRIC_APPROACH_TO_THE_ESTIMATION_OF_LENGTHS_AND_SURFACE_AREAS.md"
    parent_rscf:
      - "RSCF.KNOWLEDGE.MATHEMATICS"
      - "RSCF.KNOWLEDGE.STATISTICS"
      - "RSCF.KNOWLEDGE.NONPARAMETRIC_SET_ESTIMATION"
      - "RSCF.KNOWLEDGE.INTEGRAL_GEOMETRY"
      - "RSCF.KNOWLEDGE.IMAGE_ANALYSIS"
    node_type: KNOWLEDGE
    knowledge_type:
      - PRIMARY_SOURCE
      - JOURNAL_ARTICLE
      - MATHEMATICAL_STATISTICS
      - NONPARAMETRIC_SET_ESTIMATION
      - MINKOWSKI_CONTENT
      - CONVERGENCE_RATES
      - STATISTICAL_IMAGE_ANALYSIS
    source_epoch:
      arxiv_id: "0708.2180"
      arxiv_version: "v1"
      arxiv_date: "2007-08-16"
      journal_reference: "The Annals of Statistics, 2007, Vol. 35, No. 3, 1031–1051"
      doi: "10.1214/009053606000001532"

  # ============================================================
  # 1. EPISTEMIC CONTRACT
  # ============================================================

  epistemic_contract:
    minkowski_content_formalism: SOURCE_CLAIM
    estimator_definition_L_n: SOURCE_CLAIM
    theorem_1_strong_consistency: SOURCE_CLAIM
    theorem_2_L1_error_convergence_rate: SOURCE_CLAIM
    theorem_3_monte_carlo_approximation: SOURCE_CLAIM
    cardiology_contour_index_application: APPLIED_CASE_STUDY
    simulation_study: SIMULATION
    AMOS_structural_synthesis: DERIVED
    conclusion_class: DERIVED

    source_boundary: >
      This node preserves Cuevas, Fraiman, and Rodriguez-Casal's nonparametric
      estimator of Minkowski content (boundary length for d=2, surface area for d=3),
      its almost sure consistency, optimal bandwidth rate, Monte Carlo realization,
      and 2D image analysis application. It does not establish universal minimax
      optimality for non-standard sets or general dimension d > 3 without positive reach.

    hard_rules:
      - "The estimator requires a two-sample / binary design: points inside G (red) and outside G (green)."
      - "Standardness of G and positive reach of boundary dG are load-bearing assumptions for Theorem 2 rate O((log n / n)^{1/(d+2)})."
      - "The rate is established under uniform sampling on compact bounding rectangle R; non-uniform density requires density weighting."
      - "Monte Carlo pixel integration error is additive to the statistical sampling error."
      - "Cardiology Contour Index results demonstrate methodology feasibility on clinical imagery, not certified diagnostic efficacy."

    confidence_ceiling:
      mathematical_theorems: SOURCE_BOUND
      convergence_rates: SOURCE_BOUND
      simulation_results: SIMULATION_BOUND
      cardiology_application: CASE_STUDY_BOUND

  # ============================================================
  # 2. PROVENANCE
  # ============================================================

  provenance:
    source_id: "SRC.ARXIV.0708.2180v1"
    arxiv_id: "0708.2180"
    arxiv_version: "v1"
    category: "math.ST"
    authors:
      - "Antonio Cuevas"
      - "Ricardo Fraiman"
      - "Alberto Rodriguez-Casal"
    institutions:
      - "Universidad Autonoma de Madrid"
      - "Universidad de San Andres"
      - "Universidad de Santiago de Compostela"
    pages: 22
    source_type:
      - JOURNAL_ARTICLE
      - THEORETICAL_STATISTICS
    raw_source_policy: DO_NOT_LOAD_UNLESS_REQUIRED

  # ============================================================
  # 3. BOOTSTRAP CAPSULE
  # ============================================================

  bootstrap_capsule:
    class: DERIVED
    text: >
      Cuevas, Fraiman, and Rodriguez-Casal develop a nonparametric statistical estimator
      for the Minkowski content L_0(G) (boundary length in d=2, surface area in d=3) of a compact
      set G in R^d from a binary-classified random sample on a bounding rectangle. The estimator
      L_n(G) measures the volume of an empirical boundary band T_n (points within epsilon_n of both
      inside and outside sample points) scaled by 2*epsilon_n. Under standardness conditions,
      L_n is strongly consistent. Under the geometric assumption of positive reach on the boundary,
      the L1-error satisfies E|L_n - L_0(G)| = O(epsilon_n) + O(sqrt(log n / (n*epsilon_n^d))),
      yielding an optimal bandwidth epsilon_n ~ (log n / n)^{1/(d+2)} and rate O((log n / n)^{1/(d+2)}).
      A Monte Carlo approximation on grid pixels is proven consistent, and applied to estimate the
      cardiology Contour Index of human left ventricle boundaries from medical ultrasound/tomography images.
    retrieval_keywords:
      - Minkowski content
      - nonparametric set estimation
      - surface area estimation
      - boundary length
      - positive reach
      - standardness
      - contour index
      - statistical image analysis

  # ============================================================
  # 4. H / M / L FRACTAL ARCHITECTURE
  # ============================================================

  HML:
    H:
      id: "H.NONPARAMETRIC_SURFACE_AREA_ESTIMATION"
      governing_question: >
        How can the surface area or boundary length of an unknown set G in R^d be
        consistently estimated with optimal convergence rates solely from point-membership queries?
      master_pattern:
        class: DERIVED
        expression: >
          BINARY_RANDOM_SAMPLE(X_i, I_G(X_i))
          -> EMPIRICAL_BOUNDARY_BAND(T_n)
          -> SCALED_VOLUME_ESTIMATOR(L_n = mu(T_n)/(2*epsilon_n))
          -> CONSISTENT_MINKOWSKI_CONTENT(L_0(G))

    M:
      id: "M.MINKOWSKI_CONTENT_ESTIMATION_ENGINE"
      subsystems:
        M1_SAMPLING_MODEL:
          role: "Uniform i.i.d. point generation on bounding rectangle R containing G with indicator oracle I_G(x)."
        M2_BOUNDARY_DETECTION:
          role: "Construction of boundary band T_n where balls B(x, epsilon_n) capture both internal and external points."
        M3_VOLUME_SCALING:
          role: "Scaling Lebesgue measure mu(T_n) by (2*epsilon_n)^{-1} to approximate boundary differential."
        M4_GEOMETRIC_REGULARITY:
          role: "Standardness and Federer positive reach constraints controlling bias O(epsilon_n) and variance."
        M5_MONTE_CARLO_GRID:
          role: "Discretization using m uniform grid points to compute mu(T_n) in digital image analysis."
        M6_SHAPE_INDEX:
          role: "Computation of normalized Contour Index CI = L(G) / (2*sqrt(pi*A(G)))."

    L:
      id: "L.MINKOWSKI_ESTIMATOR_FORMAL_OBJECTS"
      canonical_variables:
        G: "Compact set of interest in R^d"
        dG: "Boundary of G"
        mu: "d-dimensional Lebesgue measure"
        L0_G: "Minkowski content (boundary measure)"
        epsilon_n: "Smoothing bandwidth sequence tending to 0"
        T_n: "Empirical boundary band {x in R : B(x, epsilon_n) contains red & green points}"
        reach_dG: "Federer reach of the boundary"
        CI: "Contour index L(G)/(2*sqrt(pi*A(G)))"

  # ============================================================
  # 5. CORE MATHEMATICAL FORMALISM
  # ============================================================

  mathematical_framework:
    minkowski_content_definition:
      expression: "L_0(G) = lim_{epsilon -> 0} mu(dG + B(0, epsilon)) / (2*epsilon)"
      class: SOURCE_CLAIM

    estimator_definition:
      expression: "L_n(G) = mu(T_n) / (2*epsilon_n)"
      where:
        T_n: "{x in R : exists X_i in G, X_j not in G with ||x - X_i|| <= epsilon_n, ||x - X_j|| <= epsilon_n}"
      class: SOURCE_CLAIM

    monte_carlo_estimator:
      expression: "L_{n,m}(G) = (mu(R) / (2*m*epsilon_n)) * sum_{j=1}^m I_{T_n}(U_j)"
      class: SOURCE_CLAIM

  # ============================================================
  # 6. THEOREMS & PROOF CAPSULES
  # ============================================================

  theorems:
    THEOREM_1_STRONG_CONSISTENCY:
      statement: >
        Let G subset R be compact with mu(dG) = 0. Assume G and R \ G are standard sets,
        and dG is mu-regular. If epsilon_n -> 0 and (n*epsilon_n^d / log n) -> inf,
        then L_n(G) -> L_0(G) almost surely as n -> inf.
      epistemic_class: SOURCE_CLAIM
      assumptions:
        - compact_G
        - standardness_G_and_complement
        - mu_regular_boundary
        - bandwidth_rate_n_eps_d_over_logn_tends_to_inf
      proof_backbone: >
        Decomposes error into |mu(T_n) - mu(B(dG, epsilon_n))| and |mu(B(dG, epsilon_n))/(2*eps_n) - L_0(G)|.
        Uses Devroye-Wise boundary coverage on epsilon_n-balls combined with Borel-Cantelli lemma.
      confidence_ceiling: SOURCE_BOUND

    THEOREM_2_CONVERGENCE_RATE:
      statement: >
        If reach(dG) >= r_0 > 0, G is standard, and epsilon_n -> 0, then:
        E|L_n(G) - L_0(G)| <= C_1 * epsilon_n + C_2 * sqrt(log n / (n*epsilon_n^d)).
        Choosing optimal bandwidth epsilon_n = O((log n / n)^{1/(d+2)}) yields the optimal rate:
        E|L_n(G) - L_0(G)| = O((log n / n)^{1/(d+2)}).
      epistemic_class: SOURCE_CLAIM
      assumptions:
        - positive_reach_r0
        - standardness
        - optimal_bandwidth_choice
      proof_backbone: >
        Positive reach bounds the geometric bias |mu(B(dG, eps))/(2*eps) - L_0| = O(eps).
        Statistical estimation variance of the empirical tube is bounded by O(sqrt(log n / (n*eps^d)))
        via exponential concentration inequalities.
      confidence_ceiling: SOURCE_BOUND

    THEOREM_3_MONTE_CARLO_CONSISTENCY:
      statement: >
        If m = m_n -> inf such that (m_n * epsilon_n^2 / log n) -> inf, then
        |L_{n,m_n}(G) - L_n(G)| -> 0 almost surely, preserving strong consistency.
      epistemic_class: SOURCE_CLAIM
      confidence_ceiling: SOURCE_BOUND

  # ============================================================
  # 7. DEPENDENCY & INVALIDATION GRAPH
  # ============================================================

  dependency_graph:
    weakest_load_bearing_premises:
      - standardness_of_boundary
      - positive_reach_condition
      - uniform_sampling_distribution
      - two_sided_oracle_availability

    invalidation_rules:
      - if: "reach(dG) == 0 (e.g. fractal boundaries or sharp inward cusps)"
        invalidates:
          - THEOREM_2_CONVERGENCE_RATE
          - O_epsilon_bias_bound
        preserves:
          - THEOREM_1_STRONG_CONSISTENCY
          - estimator_definition_L_n

      - if: "only one-sided sample available (points inside G only)"
        invalidates:
          - estimator_L_n
        preserves:
          - classical_devroye_wise_volume_estimation

  # ============================================================
  # 8. ROUTING & QUERY TARGETS
  # ============================================================

  routing_index:
    consistency_conditions: "theorems.THEOREM_1_STRONG_CONSISTENCY.assumptions"
    optimal_bandwidth: "theorems.THEOREM_2_CONVERGENCE_RATE.statement"
    rate_of_convergence: "theorems.THEOREM_2_CONVERGENCE_RATE.statement"
    geometric_bias_bound: "dependency_graph.invalidation_rules"
    cardiology_application: "identity.canonical_title"

  # ============================================================
  # 9. FINAL KNOWLEDGE CAPSULE
  # ============================================================

  final_capsule: >
    0708.2180 establishes the foundational nonparametric theory for boundary length
    and surface area estimation via scaled empirical boundary tubes. It proves that
    surface estimation is achievable at rate O((log n / n)^{1/(d+2)}) under positive
    reach, bridging integral geometry and statistical image processing.
```
