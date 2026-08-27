---
title: SKILL
type: skill
source: 07_SKILLS/amos-biology-quantum-bridge-governor
name: amos-biology-quantum-bridge-governor
description: "Biology-Quantum Bridge Governor — biology and neuroscience capability. Bridges C04 biological/neurological systems with C03 quantum physics models. Creates a governed translation layer that maps biological concepts to quantum-mechanical analogues (and vice versa) while enforcing the critical anti-overclaim firewall: quantum-biological mappings are MODEL/METAPHOR, never physical predictions. Enforces the invariant that no AMOS decision may cite quantum entanglement of biological systems as causal evidence. Use when bridging biological and quantum reasoning. Use when amos-c04-bio-neuro-master routes to this specialized capability."
parent_skill: amos-c04-bio-neuro-master
domain: cross-domain (C04 Bio-Neuro ↔ C03 Physics-Cosmos)
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
claim_ceiling: 0.85
status: production_ready
created: 2026-08-27
tags: [note, amos-biology-quantum-bridge-governor, canon/skill]
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: "1.1.0"
---


# Biology-Quantum Bridge Governor

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c04-bio-neuro-master`
- **Domain**: cross-domain (C04 Bio-Neuro ↔ C03 Physics-Cosmos)
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from C04, C03, and Cosmo brain biology-ubi/ and quantum/ directories)

Bridges biological/neurological systems (C04) with quantum physics models (C03). C04 has a quantum-biological model with explicit mapping table (business elements to biological/quantum equivalents) and a hard anti-overclaim boundary. C03 has quantum mechanics, cosmology, and spacetime knowledge. This governor creates a governed translation layer that maps biological concepts to quantum-mechanical analogues while enforcing the critical firewall: all quantum-biological mappings are MODEL/METAPHOR, never physical predictions.

## The Problem This Skill Solves

The `_00_Cosmo brain` exploration explicitly identified: *"Biology ↔ Quantum: Biological systems and quantum mechanics are separate domains without governed bridges that preserve the anti-overclaim firewall."*

Specifically:

1. **C04 has a quantum-biological model** (M2: Quantum-Biological Model of Business) with explicit mapping table and hard anti-overclaim boundary, but no bridge to C03's quantum physics
2. **C03 has quantum mechanics** (Hilbert space, Liouville theorem, Hamiltonian structure, periodic potentials, electronic bands) but no bridge to C04's biological systems
3. **C04 explicitly states** "quantum effects in brain, quantum consciousness are CONTESTED or MODEL" but there is no governed bridge to enforce this boundary
4. **No unified bridge** exists that maps biological to quantum concepts while preserving the anti-overclaim firewall

## When to Use

- When bridging biological and quantum reasoning domains
- When mapping biological concepts to quantum-mechanical analogues
- When validating that quantum-biological mappings preserve the anti-overclaim firewall
- When detecting overclaim in quantum-biological reasoning
- When the parent skill (`amos-c04-bio-neuro-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **bq_bridge.translate_bio_to_quantum**: Translate a biological concept into a quantum-mechanical analogue. Maps biological systems (neural networks, immune systems, metabolism) to quantum concepts (entanglement, field theory, energy flow). Returns quantum_analogue with MODEL/METAPHOR label or UNKNOWN/GAP if no valid mapping exists.
- **bq_bridge.translate_quantum_to_bio**: Translate a quantum concept into a biological analogue. Maps quantum concepts (superposition, measurement, decoherence) to biological phenomena (neural plasticity, perception, memory decay). Returns biological_analogue with MODEL/METAPHOR label.
- **bq_bridge.govern_bridge**: Govern the biology-quantum bridge. Enforces the critical invariant: all mappings are MODEL/METAPHOR, never physical predictions. No AMOS decision may cite quantum entanglement of biological systems as causal evidence. Returns BRIDGE_PERMITTED / BRIDGE_BLOCKED / BRIDGE_CONDITIONAL.
- **bq_bridge.detect_overclaim**: Detect overclaim in quantum-biological reasoning. Checks for physical predictions based on metaphor mappings, causal claims from quantum analogies, and consciousness claims from quantum biology. Returns overclaim report.
- **bq_bridge.validate_firewall**: Validate that the anti-overclaim firewall is preserved. Checks that all quantum-biological mappings carry MODEL/METAPHOR labels, no mapping is promoted to VERIFIED without independent evidence, and no causal claim is made from a metaphor mapping.
- **bq_bridge.trace_mapping_provenance**: Trace the provenance of a bio-quantum mapping from its source domain to its target domain

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-biology-quantum-bridge-governor_MOC]]

## Examples

- **Scenario**: When bridging biological and quantum reasoning domains
  - **Input**: A query matching this skill's domain (cross-domain (C04 Bio-Neuro ↔ C03 Physics-Cosmos))
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When mapping biological concepts to quantum-mechanical analogues
  - **Input**: A query matching this skill's domain (cross-domain (C04 Bio-Neuro ↔ C03 Physics-Cosmos))
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When validating that quantum-biological mappings preserve the anti-overclaim firewall
  - **Input**: A query matching this skill's domain (cross-domain (C04 Bio-Neuro ↔ C03 Physics-Cosmos))
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the cross-domain (C04 Bio-Neuro ↔ C03 Physics-Cosmos) domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `[[amos-c04-bio-neuro-master]]` — routes to this skill when cross-domain (C04 Bio-Neuro ↔ C03 Physics-Cosmos) specialization is needed
- **Peers**: Other skills in the `cross-domain (C04 Bio-Neuro ↔ C03 Physics-Cosmos)` domain may be composed in sequence
- **Orchestrator**: The parent skill or `AMOS_HOME` orchestrates routing
- **Workflow**: Each skill has a corresponding workflow in `08_WORKFLOWS/`
- **Agent**: Each skill has a corresponding agent in `06_AGENTS/`


## Evaluation

### Success Criteria

- Output includes epistemic class label (SOURCE/DERIVED/AMOS_MODEL/EMPIRICAL)
- Output includes provenance reference to source evidence
- Output includes confidence ceiling (capped at 0.95 for DERIVED, 1.0 for SOURCE_CANON)
- Output includes gap flags for unresolved unknowns
- Output does not exceed declared scope

### Failure Modes

- **Overreach**: Output claims validity beyond its epistemic class
- **Scope creep**: Output addresses questions outside the declared domain
- **Provenance loss**: Output cannot trace back to source evidence
- **Confidence inflation**: Output confidence exceeds the weakest-premise ceiling


## Error Handling

- **On scope violation**: Reject the query and route back to parent skill
- **On missing evidence**: Flag as GAP and reduce confidence ceiling to 0.5
- **On contradiction**: Flag as CRITICAL_GAP and halt until resolved
- **On provenance loss**: Mark output as UNKNOWN and require human review
- **On drift**: Trigger drift alignment via `amos-ai-drift-alignment-governor`


## References

- `references/references_MOC.md` — loaded on demand
- `references/vault_domain_knowledge.md` — loaded on demand
- `[[amos-biology-quantum-bridge-governor_MOC]]` — skill Map of Content
- `[[amos-c04-bio-neuro-master]]` — parent skill
- `[[amos-biology-quantum-bridge-governor-workflow]]` — corresponding workflow
- `[[amos-biology-quantum-bridge-governor-agent]]` — corresponding agent

