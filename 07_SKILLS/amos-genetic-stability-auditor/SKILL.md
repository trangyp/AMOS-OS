---
title: SKILL
type: skill
source: 07_SKILLS/amos-genetic-stability-auditor
name: amos-genetic-stability-auditor
description: Genetic Stability Auditor — audit and repair capability. Use when auditing, failure analysis, gap discovery, or repair allocation. Use when amos-audit-repair-master routes to this specialized capability.
parent_skill: amos-audit-repair-master
domain: audit
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-genetic-stability-auditor, canon/skill]
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
version: "1.1.0"
---


# Genetic Stability Auditor

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-audit-repair-master`
- **Domain**: audit
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Audit and verification engine for Genetic Stability Auditor

## When to Use

- When auditing claims against evidence and provenance
- When detecting gaps in capabilities, evidence, tests, or monitors
- When allocating repair resources to highest-leverage gaps
- When verifying gap closure across the full lifecycle chain
- When the parent skill (`amos-audit-repair-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **genetic_stability.audit_claim**: Audit claims against evidence, provenance, and epistemic class
- **genetic_stability.detect_gap**: Detect gaps: missing capabilities, missing evidence, missing tests, missing monitors
- **genetic_stability.allocate_repair**: Allocate repair resources to highest-leverage gaps and failure modes
- **genetic_stability.verify_closure**: Verify gap closure: requirement → capability → component → test → evidence
- **genetic_stability.benchmark_forensics**: Benchmark forensic analysis: trace performance regressions to root causes
- **genetic_stability.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **genetic_stability.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **genetic_stability.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_C04_BIO_NEURO_MASTER_KNOWLEDGE.md` (content_hash: 6fbde28c766c9d49) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_COGNITIVE_ORGANISM_OS_DETAIL.md` (content_hash: 61279c4b00128110) (vault canon, SOURCE_CLAIM)

### Genetic Stability Auditing

From C04 Bio & Neuro: Genetic stability and biological integrity. From Cognitive Organism OS: Structural integrity under stress.

**Genetic stability model**:
- **Genome integrity**: the genome remains intact and functional
- **Mutation rate**: mutations occur at a sustainable rate (not too high, not too low)
- **Repair mechanisms**: DNA repair mechanisms maintain genome integrity
- **Selection pressure**: selection removes deleterious mutations

**Auditing dimensions**:
- **Integrity**: is the genetic material intact?
- **Stability**: is the mutation rate within sustainable bounds?
- **Repair**: are repair mechanisms functioning?
- **Selection**: is selection pressure appropriate?
- **Drift**: is genetic drift within tolerance?

**Stability law**: `STABILITY = INTEGRITY - (MUTATION_RATE - REPAIR_RATE)`. If mutation rate exceeds repair rate, stability degrades.

**AMOS mapping**: Genetic stability is mapped to system stability (AMOS_MODEL). The mapping is an analogy, not a biological claim.

### Epistemic Boundary

Genetic stability auditing is an analytical model. It does not prove biological accuracy, that the mapping is valid, or that all stability factors are captured.

## I. CORE META LAW

### Law 1 — Multi-Scale Coupling Law

$$S_{total} = S_{micro} \times S_{meso} \times S_{macro}$$

If any layer destabilizes → compensation shifts to other layers.

If one approaches zero → total stability collapses.

---

## II. MICRO LAYER (Cellular / Endothelial)

Micro stability:

$$S_{micro} = \frac{G \times NO}{Ox \times Sh}$$

Where: Glycocalyx integrity (G), Nitric oxide (NO), Oxidative load (Ox), Shear stress (Sh).

Micro drifts → meso compensates → macro shifts.

---

## III. MESO LAYER (Autonomic + Vascular Coordination)

$$S_{meso} = \frac{Para \times Br}{Sym \times Pv}$$

Where: Parasympathetic tone (Para), Baroreflex sensitivity (Br), Sympathetic tone (Sym), Perfusion variance (Pv).

High Sym + high Pv = oscillatory instability.

---

## IV. MACRO LAYER (Environment + Social + Structure)

$$S_{macro} = \frac{R \times Rc}{En \times Su}$$

Where: Resource reliability (R), Relational coherence (Rc), Environmental noise (En), Social unpredictability (Su).

This is why environment shifts physiology directly.

---

## V. Meta Law of Gain

Every system has Input gain (G_i) and Damping coefficient (D).

- $$G_i > D \rightarrow oscillation$$
- $$G_i \gg D \rightarrow instability$$
- $$G_i

---
**Links:** [[07_SKILLS_MOC]]

## Related

- [[amos-genetic-stability-auditor_MOC]]

## Examples

- **Scenario**: When auditing claims against evidence and provenance
  - **Input**: A query matching this skill's domain (audit)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When detecting gaps in capabilities, evidence, tests, or monitors
  - **Input**: A query matching this skill's domain (audit)
  - **Output**: Structured result with epistemic labels and provenance

- **Scenario**: When allocating repair resources to highest-leverage gaps
  - **Input**: A query matching this skill's domain (audit)
  - **Output**: Structured result with epistemic labels and provenance


## Anti-Patterns

- **Do not use** for tasks outside the audit domain
- **Do not use** when the query requires empirical validation that this skill cannot provide
- **Do not use** when a parent skill or higher-level orchestrator should route instead
- **Do not bypass** epistemic class labeling — every output must carry SOURCE/DERIVED/AMOS_MODEL tags
- **Do not chain** more than 3 skills without explicit orchestrator approval


## Composition

- **Parent**: `[[amos-audit-repair-master]]` — routes to this skill when audit specialization is needed
- **Peers**: Other skills in the `audit` domain may be composed in sequence
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

- `references/amos-genetic-stability-auditor_code.md` — loaded on demand
- `references/references_MOC.md` — loaded on demand
- `[[amos-genetic-stability-auditor_MOC]]` — skill Map of Content
- `[[amos-audit-repair-master]]` — parent skill
- `[[amos-genetic-stability-auditor-workflow]]` — corresponding workflow
- `[[amos-genetic-stability-auditor-agent]]` — corresponding agent

