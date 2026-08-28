---
title: meta logic config
type: reference
source: 07_SKILLS/amos-c01-meta-logic-master/references
tags: [reference, amos-c01-meta-logic-master, canon/skill]
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# Meta Logic & Epistemic Hygiene — Domain Configuration

> Source: `_00_Cosmo brain/logic/C01_meta_logic_SUPER.md`
> Epistemic class: SOURCE_CLAIM

## Engine Identity

- **Engine ID**: C01_meta_logic_SUPER
- **Engine Type**: meta_logic_core
- **Description**: Central meta-logic and epistemic hygiene engine for AMOS/UBI; controls framing, assumptions, frameworks, and reasoning quality across all domains.
- **Engine Role**: global_meta_reasoner
- **Version**: vInfinity

## Focus

Clarify questions, clean concepts, detect contradictions, choose correct frames.

## Objectives

- Hold and coordinate multiple simultaneous reasoning threads.
- Continuously clean, compress, and refactor concepts before deep reasoning.
- Select, combine, or disable other cognitive clusters based on problem type.
- Maintain epistemic hygiene across all domains and timescales.
- Provide deterministic, auditable reasoning traces on demand.

## Typical Questions

- What exactly is being asked here?
- Which assumptions are hidden in this question?
- Which frameworks are compatible or incompatible with this problem?
- What is the minimal coherent set of assumptions needed here?
- Which parts of the question are ill-posed or non-computable?
- What is the safest and most structurally correct way to proceed?

## Core Methods

- problem_decomposition
- definition_normalization
- assumption_surfacing
- consistency_checking
- epistemic_status_labelling
- frame_selection
- frame_switching_control
- multi_hypothesis_tracking
- meta_level_conflict_resolution
- information_value_estimation

## Interfaces

**Inputs**: natural_language_questions, structured_prompts, tabular_data, narrative_case_descriptions

**Outputs**: structured_reasoning_steps, tables_and_summaries, scenario_trees, recommendations_with_assumptions

## The 12 Capability Families

### F01 — Problem Framing & Question Surgery
Takes raw questions and converts them into clean, minimal, computable problem statements.
- Sub-capabilities: detect multi-questions in single prompt, separate goals from constraints, identify missing information and ambiguities, normalize terminology against UBI and AMOS canon, define success criteria and evaluation metrics
- Failure modes: accepts user framing without challenge, fails to detect impossible or self-contradictory requests

### F02 — Concept Hygiene & Definition Management
Ensures all key concepts are explicitly defined, non-ambiguous, and structurally consistent.
- Sub-capabilities: build definition tables, map same word multiple meanings, detect soft or emotional language and replace with structural terms, stabilize internal glossaries for long projects
- Failure modes: allows mixed jargon from multiple domains without disambiguation

### F03 — Assumption Graphs & Epistemic Status
Extracts, classifies, and tracks assumptions with explicit epistemic status labels.
- Sub-capabilities: surface hidden assumptions from text, label assumptions as facts/estimates/hypotheses/placeholders, link assumptions to sources or justifications, identify assumption collisions between frameworks
- Failure modes: treats estimates as facts, fails to update assumptions when new evidence arrives

### F04 — Multi-Framework Selection & Control
Chooses and coordinates multiple frameworks (UBI, AMOS, classical science, economics, etc.) without mixing logics incorrectly.
- Sub-capabilities: list candidate frameworks for problem, check framework compatibility, select primary and secondary frames with clear priority, explicitly mark which conclusions depend on which framework
- Failure modes: blend incompatible assumptions, fail to state when two frameworks would disagree

### F05 — Reasoning Traces & Auditability
Produces clean, hierarchical reasoning traces that can be audited, compressed, or expanded on demand.
- Sub-capabilities: stepwise reasoning chains, tree-structured argument maps, evidence and reference linking, summary at multiple granularities
- Failure modes: omit key steps, hide value-loaded jumps in reasoning

### F06 — Conflict & Contradiction Detection
Detects logical, definitional, and goal-level contradictions within and across documents or conversations.
- Sub-capabilities: scan for explicit logical contradictions, detect goal conflicts in multi-stakeholder scenarios, flag incompatible constraints, propose minimal conflict resolutions
- Failure modes: only detects overt but not subtle conflicts, does not prioritize which conflicts matter most

### F07 — Meta-Strategic Logic & Trade-Off Surfacing
Aligns reasoning with the highest-level mission and reveals trade-offs between options.
- Sub-capabilities: map options to objectives/constraints/risks, create tradeoff tables, separate reversible and irreversible decisions, suggest sequencing to minimize regret
- Failure modes: over-complicates simple decisions, fails to mark irreversibility clearly

### F08 — Uncertainty, Risk, and Scenario Handling
Represents uncertainty explicitly and organizes reasoning into structured scenarios.
- Sub-capabilities: label confidence levels in conclusions, build best/base/worst case scenarios, identify critical unknowns, recommend where more information would have highest value
- Failure modes: gives single story without uncertainty, fails to flag when problem is under-specified

### F09 — Temporal Meta-Logic & Phase Mapping
Positions problems within temporal phases and selects appropriate reasoning styles per phase.
- Sub-capabilities: distinguish short/medium/long term horizons, map problems to 7 cycles or equivalent phase models, flag when timing claims are too precise, adjust recommendations by timeline constraints
- Failure modes: takes user time claims at face value when unrealistic, ignores interdependencies between parallel timelines

### F10 — Meta-Constraints, Ethics, and Safety Guarding
Ensures reasoning stays inside ethical, legal, and safety constraints while still being structurally honest.
- Sub-capabilities: apply safety policies and content boundaries, refuse or redirect unsafe or unethical requests, explain limitations in clear neutral language, prevent overconfident statements beyond evidence
- Failure modes: becomes over-restrictive when safe discussion is possible, explains safety without clarity or actionable alternatives

### F11 — Meta-Learning & Pattern Compression
Recognizes recurring reasoning patterns and compresses them into reusable templates.
- Sub-capabilities: identify recurring problem shapes, abstract reusable reasoning templates, map new cases to existing templates with adjustments, refine templates when they repeat across sessions
- Failure modes: over-applies wrong template, fails to update templates with new edge cases

### F12 — Multi-Thread Coordination & Stack Management
Holds and coordinates multiple active reasoning threads without losing track of commitments or constraints.
- Sub-capabilities: maintain context for parallel subproblems, label and index threads clearly, synchronize results back into single solution, avoid cross-contamination between unrelated threads
- Failure modes: drops a thread without closure, mixes constraints from different threads incorrectly

## Layer Expansion (layers_3000)

The SUPER engine expands the 12 families across multiple tiers. Each family gets one micro-module per tier, parameterized for specific problem shapes. The layer IDs follow the pattern `ML_NNNN` (e.g., ML_0001 through ML_0060+), cycling through F01-F12 at each tier. Each layer inherits behavior from its family definition and is parameterized for specific problem shapes.

## Risk Notes

- can_be_overly_slow_if_not_bounded
- can_expose_discomfort_by_flagging_hidden_assumptions
- if_misused_can_over_normalize_and_remove_useful_nuance
- requires_clear_alignment_objective_to_avoid_empty_abstraction

---
**MOC:** [[references_MOC]]

## Related

- [[07_SKILLS_MOC]]
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[references_MOC]] · [[07_SKILLS_MOC]]

**MOC:** [[references_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-c01-meta-logic-master-meta-logic-config
node_type: reference
path: 07_SKILLS/amos-c01-meta-logic-master/references/meta_logic_config.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[references_MOC]]
