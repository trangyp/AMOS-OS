---
name: arxiv-rscf-compiler
description: 'Transforms arXiv/scientific papers into compact, source-faithful AMOS
  RSCF knowledge objects (AMOS_KNOWLEDGE_OBJECT) designed for extremely low downstream
  retrieval-token cost. Trigger whenever asked to: reformat an arXiv paper, convert
  a paper to AMOS RSCF, normalize research papers, compile papers into H/M/L knowledge
  objects, ingest scientific literature into AMOS knowledge, or create theorem/equation
  knowledge nodes.'
parent_skill: amos-knowledge-research-master
domain: knowledge
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
version: 1.1.0
rscf_state: SOURCE_CLAIM
hml_level: M
gmef_gates:
- L0_integrity
- L1_epistemic
- L2_provenance
- L5_scope
- L7_authority
collapse_class: reversible
qfm_gate_set: QFM_v43
law_compliance:
- L0
- L1
- L2
- L4
- L5
- L7
- L16
- L17
- L18
tags:
- type/skill
- canon/skill
- domain/knowledge-research
- rscf/source_claim
- hml/m
- epistemic/source_claim
- amos_os
---


# arXiv-RSCF Knowledge Compiler

## Identity

Origin architect: **Trang Phan**. Domain: knowledge. Parent: amos-knowledge-research-master. Epistemic class: SOURCE_CLAIM. H/M/L: M.

## When to Use

- When reformatting an arXiv paper into AMOS RSCF knowledge objects
- When normalizing research papers into H/M/L knowledge capsules
- When ingesting scientific literature into AMOS knowledge
- When creating theorem/equation knowledge nodes from academic papers

The `arxiv-rscf-compiler` transforms raw academic and scientific literature into compact, source-grounded, and invariant-gated **`AMOS_KNOWLEDGE_OBJECT`** nodes.

This is **not** an extractive summarizer or text condenser. It is a **semantic knowledge compiler** that executes a one-time, model-driven semantic conversion to enable amortized, sub-second, ultra-low-token downstream querying ($100$–$1,000$ tokens per query).

---

## Capabilities

- **paper_normalization**: Transform arXiv papers into source-faithful AMOS_KNOWLEDGE_OBJECTs
- **hml_tiering**: Tier content into H/M/L levels for low retrieval-token cost
- **equation_status_tagging**: Tag equations as ESTABLISHED_MATH/SOURCE_DERIVED/AMOS_MODEL
- **theorem_scope_boundary**: Define theorem scope boundaries with falsifiers
- **provenance_binding**: Bind knowledge objects to arXiv IDs with full provenance
- **batch_ingestion**: Ingest multiple papers into normalized knowledge capsules
- **rscf_schema_compliance**: Ensure 22-section schema compliance for knowledge objects

## Non-Negotiable Core Principle: Model-Side Semantic Intelligence

```text
RAW SCIENTIFIC PAPER
        │
        ▼ (Model-side semantic reading, classification & reasoning — NO SCRIPTS)
STRUCTURED EPISTEMIC CONTRACT & H/M/L ARCHITECTURE
        │
        ▼ (Deduplicated, keyed, type-safe AMOS_KNOWLEDGE_OBJECT)
DURABLE ATOMIC KNOWLEDGE SLICES (100–1,000 tokens per downstream query)
```

> [!CRITICAL]
> **Deterministic Code & Script Prohibition**:
> The semantic paper-to-RSCF conversion MUST NOT be performed with Python, regex, AST parsers, extraction scripts, templating scripts, or rule-based NLP pipelines.
> The LLM itself must read, reason over, classify, verify, and compile the scientific content.
> Python/scripts may only be used for non-semantic QA (e.g. file existence, packaging).

---

## Core Invariants

1. **Integrity Hierarchy**:
   $$\text{Integrity} > \text{Completeness} > \text{Fluency} > \text{Speed} > \text{Token Savings}$$
2. **Conservative Epistemic Classification**:
   Always use the weakest accurate class (`SOURCE_CLAIM`, `OBSERVATION`, `DERIVED`, `MODEL`, `CONDITIONAL`, `COMPETING`, `UNKNOWN`).
   - Never promote: $\text{Simulation} \to \text{Empirical Validation}$, $\text{Upper Bound} \to \text{Minimax Optimality}$, $\text{Correlation} \to \text{Causation}$, $\text{Source Claim} \to \text{Verified Ground Truth}$, $\text{UNKNOWN} \to \text{Guessed Answer}$.
3. **Conservation of Conclusion-Changing Premises**:
   Never reduce token count by dropping regularity conditions, sample constraints, dimension restrictions, or domain boundaries.
4. **Local Dependency Invalidation**:
   Build explicit dependency edges (`weakest_load_bearing_premises`, `invalidation_conditions`) so downstream invalidation is local, not catastrophic.
5. **Mutation Policy**:
   `APPEND_OR_VERSION_NEVER_SILENT_OVERWRITE`. Preserve exact source provenance and version (`v1`, `v2`, journal revision).

---

## Progressive Loading & Compilation Workflow

To minimize compilation context overhead, follow aggressive progressive loading:

### Step 1: Rapid Orientation & Source Map (Passive)
Inspect the paper's header, abstract, section headings, conclusion, and theorem/table captions. Construct an internal mental source map:
- Governing question ($H$)
- Primary machinery ($M$)
- Core variables, equations, and datasets ($L$)

### Step 2: Targeted Deep Semantic Inspection (Active)
Read only the sections that define or bound conclusion-changing components:
- Model definitions, sampling design, and foundational assumptions.
- Primary theorems, proof backbones, and mathematical bounds.
- Empirical datasets, metrics, baselines, and statistical error rates.
- Failure modes, counterexamples, and unaddressed gaps.

### Step 3: Progressive Reference Consultation
When formulating complex blocks, consult external references on demand:
- For schema layout and available sections: consult [`references/schema.md`](file:///Users/mac/Documents/AMOS_OS/.agents/skills/arxiv-rscf-compiler/references/schema.md).
- For pre-commit validation and epistemic audits: consult [`references/quality-gates.md`](file:///Users/mac/Documents/AMOS_OS/.agents/skills/arxiv-rscf-compiler/references/quality-gates.md).
- For canonical output formatting: consult [`references/example-node.md`](file:///Users/mac/Documents/AMOS_OS/.agents/skills/arxiv-rscf-compiler/references/example-node.md).

### Step 4: Knowledge Object Compilation
Emit the compiled `AMOS_KNOWLEDGE_OBJECT` using the smallest sufficient structure that preserves all conclusion-changing information.

---

## H / M / L Architecture

Every compiled knowledge object must structure its concepts into three fractal scales:

- **$H$ (High-level Principle)**: Governing scientific question, foundational claim, or global hypothesis.
- **$M$ (Middle-level Mechanism)**: Subsystems, theorem families, experimental protocols, algorithmic stages, or conceptual components.
- **$L$ (Low-level Formal Objects)**: Exact variables, equations, parameters, datasets, numerical measurements, and regularity conditions.

*Routing Rule*: Queries should route to 1–3 atomic slices ($L$ or $M$), never reloading the entire paper.

---

## Proof Capsule Standard

For major theorems and empirical conclusions, compile compact proof capsules:

```yaml
proof_capsule:
  claim_id: THEOREM_1_STRONG_CONSISTENCY
  epistemic_class: SOURCE_CLAIM
  governing_statement: "L_n(G) -> L_0(G) almost surely as n -> inf"
  load_bearing_premises:
    - standardness_condition
    - epsilon_n_bandwidth_rate
    - bounded_compact_support
  proof_backbone: >
    Combines Devroye-Wise boundary coverage with epsilon-tube volume
    convergence and Borel-Cantelli lemma on binomial tails.
  falsifiers:
    - failure_of_standardness
    - bandwidth_decay_too_fast
  confidence_ceiling: SOURCE_BOUND
```

---

## Scope & External Research Firewall

- If asked to **"reformat / convert / normalize this paper"**:
  Compile *that specific source only*. Do not search external web literature or merge external assertions into the source claim layer.
- If asked to **"update / verify / compare with SOTA"**:
  Compile the original source node faithfully first, then attach separate explicit extension objects (`DERIVED` / `EXTERNAL_AUDIT`).

---

## Reference Pointers

- **[Schema Specification](references/schema.md)**: Full 22-section schema catalog, flexible output rules, and object templates.
- **[Quality Gates & Auditing](references/quality-gates.md)**: Mandatory verification checklist covering source fidelity, theorem scope, and epistemic boundaries.
- **[Canonical Example Node](references/example-node.md)**: Complete normalized reference node for `0708.2180v1`.

## Examples

- **Scenario**: User says "Convert this arXiv paper to AMOS RSCF format"
  - **Input**: arXiv paper (e.g., 2401.12345v2)
  - **Output**: Compact AMOS_KNOWLEDGE_OBJECT with 22-section schema, H/M/L tiered content, theorem scope boundaries, epistemic class labels, low retrieval-token cost

- **Scenario**: User says "Ingest this scientific literature into AMOS knowledge"
  - **Input**: Multiple scientific papers
  - **Output**: Batch of normalized AMOS_KNOWLEDGE_OBJECTs, each with source-faithful content, equation status tags (ESTABLISHED_MATH/SOURCE_DERIVED/AMOS_MODEL), provenance to arXiv ID

## Validation Gates

- **L0 Integrity**: All structural elements accounted for; no silent gaps
- **L1 Epistemic**: Every claim tagged with epistemic class (SOURCE_CLAIM / DERIVED / AMOS_MODEL)
- **L5 Scope**: Analysis confined to declared scope and domain
- **L7 Authority**: No autonomous action beyond authority boundary

## Do not use

- For generic document conversion outside arXiv/RSCF framework
- To alter or fabricate scientific claims (source-faithful only)
- As a substitute for domain-specific peer review or validation
- Outside knowledge research domain reasoning
