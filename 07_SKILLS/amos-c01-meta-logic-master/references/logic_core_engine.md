---
title: logic core engine
type: reference
source: 07_SKILLS/amos-c01-meta-logic-master/references
tags: [reference, amos-c01-meta-logic-master, canon/skill]
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# AMOS Logic Core Engine

> Source: `_00_Cosmo brain/engine/A/AMOS_Logic_Core_Engine_v0_Logic.md`
> Epistemic class: SOURCE_DERIVED

---
tags: [canon-group/biology, canon/framework, rscf/claim, rscf/provenance, rscf/state/source-claim, topic/amos-logic-core-engine-v0, engine]
---

{
  "meta": {
    "name": "Logic_Core_Engine",
    "version": "1.0.0",
    "description": "Core engine for logic: deductive and inductive reasoning, argument analysis, formalisation, validity, soundness, fallacies, and systematic consistency."
  },
  "engine": {
    "description": "The Logic Core Engine provides structured support for reasoning rigorously: representing claims, analysing arguments, checking validity and soundness, distinguishing deduction from induction and other non-deductive inference, spotting common fallacies, and keeping reasoning internally consistent. It supports formal and informal logic, but it is an analytical and reasoning-support engine, not a replacement for domain expertise, empirical evidence, or professional judgment.",
    "capabilities": {
      "argument_analysis": "Identify premises, conclusions, intermediate steps, hidden assumptions, and the overall structure of an argument.",
      "deductive_reasoning": "Assess whether conclusions follow necessarily from premises, using propositional and predicate reasoning where appropriate.",
      "inductive_and_non_deductive_reasoning": "Assess strength, support, probability, and inference quality for arguments that are not deductively conclusive.",
      "formalisation": "Translate reasoning into clearer symbolic or structured form where helpful, and flag where formalisation is limited or misleading.",
      "validity_and_soundness": "Distinguish validity from truth, and assess whether a deductive argument is valid, and whether it is sound when premises are also true.",
      "fallacy_detection": "Identify common formal and informal fallacies, and distinguish genuine errors from merely weak or disputed reasoning.",
      "consistency_checking": "Detect contradictions, tensions, and incompatible commitments across a set of claims or principles.",
      "assumption_exposure": "Surface assumptions, definitions, equivocations, and scope conditions that affect whether reasoning holds."
    },
    "structural_components": {
      "claims": "The statements under consideration: conclusions, premises, hypotheses, or assertions.",
      "inference_structure": "How claims support one another: chains, trees, networks of support, or counter-argument.",
      "definitions_and_terms": "The meanings in play, including ambiguities, equivocations, and definitional scope.",
      "assumptions": "Explicit and implicit premises, background conditions, and scope limits.",
      "evidence_and_grounds": "What is taken to support claims, and how strongly.",
      "counterconsiderations": "Objections, alternatives, edge cases, and counterexample templates."
    },
    "constraints_and_governance": {
      "no_logic_as_alibi_for_bad_faith": "The kernel should not use formal logic to dismiss arguments in bad faith, harass, or overcomplicate simple questions.",
      "no_overclaim_of_certainty": "Logic can clarify what follows from what, but it does not by itself establish factual truth, empirical accuracy, or real-world safety.",
      "no_replacement_for_domain_or_evidence_reasoning": "Logical rigour is necessary but not sufficient. Domain knowledge, data, and evidence still matter.",
      "no_clinical_or_safety_decision_automation": "Logical analysis does NOT replace clinical, legal, safety, financial, or other domain-specific judgment and governance.",
      "assumption_transparency": "State definitions, scope, assumptions, and whether an argument is being treated formally or informally.",
      "charitable_reasoning": "Interpret arguments in a reasonable, strong-form way before critiquing them, unless there is a clear reason not to."
    },
    "input_types": {
      "text_or_argument": "The reasoning, claim, or argument to analyse.",
      "analysis_purpose": "Whether the user wants validity checking, structure mapping, fall

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
node_id: amos-c01-meta-logic-master-logic-core-engine
node_type: reference
path: 07_SKILLS/amos-c01-meta-logic-master/references/logic_core_engine.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[references_MOC]]
