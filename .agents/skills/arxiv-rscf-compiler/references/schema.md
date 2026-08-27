# AMOS Knowledge Object Schema Specification

## Root Object Header

Every compiled knowledge node must begin with the canonical AMOS root object header:

```yaml
AMOS_KNOWLEDGE_OBJECT:
  schema_family: RSCF
  schema_role: KNOWLEDGE_RSCF
  schema_version: "AMOS_CORE_v4.4-compatible-conceptual"
  object_status: ACTIVE_REFERENCE
  ingestion_state: NORMALIZED_FROM_PRIMARY_SOURCE
  mutation_policy: APPEND_OR_VERSION_NEVER_SILENT_OVERWRITE
```

---

## The 22 Modular Schema Sections

> [!IMPORTANT]
> **Flexibility Rule**: Do NOT mechanically emit all 22 sections for every paper. The compiler must produce the **smallest sufficient structure** that captures all conclusion-changing information without omitting critical caveats.

---

### Section 0: Identity / Fractal Address
Defines unambiguous namespacing and hierarchical placement across the 26 AMOS planes.

```yaml
identity:
  node_id: "RSCF.KNOWLEDGE.{DOMAIN}.{SUBDOMAIN}.{TOPIC}.{ARXIV_ID}"
  canonical_slug: "YYMM_NNNNvX_short_descriptive_title"
  canonical_title: "Full Title of the Scientific Work"
  preferred_path:
    H: "11_KNOWLEDGE/{domain}"
    M: "{subdomain}/{methodology}"
    L: "arxiv/{year}/{slug}"
  legacy_path: "11_KNOWLEDGE/_arxiv_md/{year}/{original_filename}.md"
  parent_rscf:
    - "RSCF.KNOWLEDGE.{DOMAIN}"
    - "RSCF.KNOWLEDGE.{SUBDOMAIN}"
  node_type: KNOWLEDGE
  knowledge_type:
    - PRIMARY_SOURCE
    - THEORETICAL_MATHEMATICS # or EXPERIMENTAL_PHYSICS, STATISTICAL_METHODOLOGY, etc.
  source_epoch:
    arxiv_id: "YYMM.NNNN"
    arxiv_version: "vX"
    arxiv_date: "YYYY-MM-DD"
```

---

### Section 1: Epistemic Contract
The legal and epistemic boundary of the knowledge object. Declares confidence ceilings and non-negotiable rules.

```yaml
epistemic_contract:
  primary_claim_A: SOURCE_CLAIM
  empirical_dataset_B: OBSERVATION
  mathematical_derivation_C: DERIVED
  theoretical_analogy_D: MODEL
  unresolved_conjecture_E: UNKNOWN

  source_boundary: >
    Exact scope of what the paper establishes versus what remains speculative,
    unvalidated, or model-dependent.

  hard_rules:
    - "Rule 1: Specificity constraint (do not generalize beyond stated conditions)."
    - "Rule 2: Boundary constraint (distinguish simulation from real-world proof)."
    - "Rule 3: Exact definition constraint (e.g. bound != equality)."

  confidence_ceiling:
    source_theorems: SOURCE_BOUND
    empirical_measurements: OBSERVATION_BOUND
    universal_generalizations: MODEL
```

---

### Section 2: Provenance
Detailed citation metadata and load-trigger rules.

```yaml
provenance:
  source_id: "SRC.ARXIV.YYMM.NNNNvX"
  arxiv_id: "YYMM.NNNN"
  arxiv_version: "vX"
  category: "math.ST / physics.optics / quant-ph / etc."
  authors:
    - "Author One"
    - "Author Two"
  institutions:
    - "Primary Institution"
  pages: 22
  source_type:
    - ARXIV_PREPRINT
    - JOURNAL_ARTICLE
  source_topics:
    - topic_one
    - topic_two
  raw_source_policy: DO_NOT_LOAD_UNLESS_REQUIRED
  raw_source_load_triggers:
    - exact_theorem_statement
    - exact_numerical_constants
    - proof_backbone_reconstruction
    - ambiguous_notation_resolution
```

---

### Section 3: Bootstrap Capsule
Compact, dense 1-paragraph conceptual digest for fast retrieval without opening full sections.

```yaml
bootstrap_capsule:
  class: DERIVED
  text: >
    Dense 1-paragraph summary explaining the central problem, governing method,
    primary mathematical/empirical result, primary assumption, and main limitation.
  retrieval_keywords:
    - keyword_1
    - keyword_2
    - keyword_3
```

---

### Section 4: H / M / L Fractal Architecture
Multi-scale decomposition enabling cognitive zooming from global law to exact variables.

```yaml
HML:
  H:
    id: "H.GOVERNING_QUESTION"
    governing_question: "What fundamental question or global hypothesis does this resolve?"
    master_pattern:
      class: DERIVED
      expression: "INPUT_STATE -> MECHANISM_TRANSFORMATION -> OUTPUT_RESULT"

  M:
    id: "M.SYSTEM_OR_METHODOLOGY_ARCHITECTURE"
    subsystems:
      M1_STAGE_ONE:
        role: description_of_subsystem_1
      M2_STAGE_TWO:
        role: description_of_subsystem_2

  L:
    id: "L.FORMAL_VARIABLES_AND_EQUATIONS"
    canonical_variables:
      var_1: definition_and_units
      var_2: definition_and_units
    canonical_equations:
      eq_1: "LaTeX string or clean ASCII equation"

  HML_integrity_rule: >
    L-level variables inherit M-level mechanisms. H-level claims are valid
    only while L-level regularity conditions are strictly satisfied.
```

---

### Sections 5–15: Technical Machinery & Empirical Bounds
Emitted as needed by the source domain:

- **Technical Objects / Models**: Formal definitions, sampling designs, Hamiltonians, boundary conditions.
- **Claim Graph**: Numbered claims (`C001`, `C002`) with epistemic classes, premises, and evidence pointers.
- **Dependency Graph**: Explicit dependency chains and `weakest_load_bearing_premises`.
- **Causal / Inference Firewall**: Distinguishing correlation vs causation, association vs mechanism.
- **Applicability Envelope**: Data regimes, dimensions, regularity conditions, asymptotic vs finite-sample bounds.
- **Trade-off Relocation / Sensitivity**: Where constraints relocate (e.g. noise vs power vs bandwidth).

---

### Section 18: Proof Capsules
Compact proof backbones for load-bearing theorems:

```yaml
proof_capsules:
  THEOREM_1:
    statement: "Exact formal assertion of the theorem."
    epistemic_class: SOURCE_CLAIM
    premises:
      - premise_1
      - premise_2
    proof_backbone: >
      Step-by-step logical reduction (e.g. geometric tube expansion +
      Borel-Cantelli lemma + martingale convergence).
    falsifiers:
      - violation_of_premise_1
    confidence_ceiling: SOURCE_BOUND
```

---

### Sections 19–22: Governance, Recovery & Final Capsule

```yaml
governance_and_lifecycle:
  weakest_load_bearing_premises:
    - premise_alpha
    - premise_beta
  unresolved_gaps:
    - unaddressed_edge_case_1
  safe_reuse:
    - canonical_definition_A
    - asymptotic_rate_B
  revalidation_required:
    - extension_to_untested_dimensions
    - deployment_under_non_standard_distributions
  final_capsule: >
    Final definitive conclusion summarizing durable knowledge preserved
    for the AMOS OS matrix.
```
