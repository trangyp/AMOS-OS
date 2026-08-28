---
title: amos-learning-memory-knowledge-feedback-governor-workflow
type: workflow
source: 08_WORKFLOWS
Type: Workflow
Skill: amos-learning-memory-knowledge-feedback-governor
Agent: amos-learning-memory-knowledge-feedback-governor-agent
Trigger: When C05 inference outcomes need to be encoded into Memory Systems, when
  memory entries need to be consolidated into the Knowledge Research vault, when indexed
  knowledge needs to be retrieved to inform new C05 inference, when the full feedback
  loop needs governance, when detecting knowledge drift, when validating epistemic
  preservation across domain transitions, or when amos-knowledge-research-master routes
  to cross-domain learning-memory-knowledge feedback governance
Version: 1.0.0
tags:
- type/workflow
- canon/workflow
- domain/memory-systems
- canon-group/tech-ai
- topic/memory
- capability/memory
- capability/governance
- capability/learning
- capability/preconditions
- capability/orchestration_pattern
- capability/evaluation_gates
- capability/monitoring
- rscf/epistemic
- rscf/C-constraint
- rscf/G-relation
- rscf/M-memory
- rscf/μ-mutation
- rscf/type-system
- orchestration/event-driven
- sota/evaluation-gates
- sota/human-in-the-loop
- amos_os
rscf:
  state: AMOS_MODEL
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: workflow_process
---






# Workflow: Learning-Memory-Knowledge Feedback Governor

## Preconditions

- The `amos-learning-memory-knowledge-feedback-governor` skill exists and is loaded.
- The `amos-learning-memory-knowledge-feedback-governor-agent` agent is available and has valid content_hash.
- The query spans C05 (inference/learning) and at least one of Memory Systems or Knowledge Research.
- C05 Mind & Behavior Master Knowledge is available (inference loop, learning models, claim classes).
- Memory Systems contract is available (encode/consolidate/retrieve, memory layers, formation rules).
- Knowledge Research MOC is available (index structure, Obsidian vault integration, 18 methods).
- Epistemic class labeling is enabled (SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL / MODEL).
- Provenance tracking is enabled across all domain transitions.

## Steps

1. **Intake** (`lmk_feedback.manage_lifecycle`): Identify the problem and confirm it matches the Learning-Memory-Knowledge Feedback Governor scope.
   - Classify the query: does it span C05 + Memory Systems and/or Knowledge Research?
   - Identify the loop phase: ENCODE, CONSOLIDATE, RETRIEVE, APPLY, or FULL_LOOP
   - Identify the C05 inference outcome (if encoding)
   - Identify the memory entries (if consolidating)
   - Identify the knowledge needed (if retrieving)
   - Gate: `scope_confirmed` — query spans C05 + at least one of Memory/Knowledge; fail closed if intra-C05 only

2. **Encode Learning** (`lmk_feedback.encode_learning`): Encode C05 inference outcome into Memory Systems.
   - Extract inference outcome from C05 (result, epistemic class, confidence, provenance)
   - Map to memory layer: working memory (immediate) → episodic memory (consolidated)
   - Preserve epistemic class: MODEL stays MODEL, SOURCE stays SOURCE
   - Set confidence: memory confidence ≤ inference confidence
   - Stamp with provenance: C05 inference ID, timestamp, session context
   - If inference outcome is UNKNOWN/GAP: do not encode, mark as UNKNOWN/GAP, fail closed
   - Gate: `learning_encoded` — memory entry created with preserved epistemic class and provenance; no fabrication

3. **Corroboration Check**: Verify sufficient corroboration for consolidation.
   - Count independent memory entries from separate inference episodes for the same claim
   - Require 2+ independent entries (different sessions, different inputs, different reasoning paths)
   - If fewer than 2: BLOCK consolidation, retain memory entries for future corroboration
   - Record corroboration evidence: entry IDs, episode timestamps, independence verification
   - Gate: `corroboration_checked` — 2+ independent entries verified; or consolidation blocked with retention

4. **Consolidate to Knowledge** (`lmk_feedback.consolidate_to_knowledge`): Consolidate memory entries into indexed Knowledge Research vault.
   - Merge 2+ corroborating memory entries into a single knowledge artifact
   - Set consolidated epistemic class: no promotion (MODEL + MODEL = MODEL, not VERIFIED)
   - Set consolidated confidence: confidence ≤ min(corroborating entries)
   - Declare scope and regime: knowledge artifact states where it applies and when it expires
   - Stamp with full provenance chain: C05 inference IDs → memory entry IDs → knowledge artifact ID
   - Index in Knowledge Research vault (ObsidianBrain.create_note or append_to_moc)
   - Gate: `knowledge_consolidated` — knowledge artifact created with full provenance, scope, and freshness stamp

5. **Retrieve for Inference** (`lmk_feedback.retrieve_for_inference`): Retrieve knowledge entries to inform new C05 inference.
   - Query Knowledge Research vault for relevant knowledge (ObsidianBrain.search_notes or related_notes)
   - Validate freshness: check regime expiry — is the knowledge still within its valid regime?
   - Validate scope: is the retrieved knowledge applicable to the current inference context?
   - Tag retrieved knowledge with source class (SOURCE / DERIVED / AMOS_MODEL / MODEL)
   - Set retrieval confidence: confidence ≤ freshness_factor × original_confidence
   - If knowledge is stale (expired regime): BLOCK application, flag as DRIFT
   - If knowledge is out of scope: BLOCK application, flag as SCOPE_VIOLATION
   - Gate: `knowledge_retrieved` — knowledge retrieved, freshness validated, scope checked; stale/out-of-scope blocked

6. **Apply to New Inference**: Apply r

---
**MOC:** [[08_WORKFLOWS_MOC]]

## Orchestration Pattern

**Pattern**: Single-Agent with Validation Gates

This workflow follows a single-agent orchestration with explicit validation gates between steps:
1. **Intake** -> validation gate -> **Skill Invocation** -> validation gate -> **Application** -> validation gate -> **Output**
2. Each gate checks: epistemic labeling, provenance, scope compliance, confidence ceiling
3. On gate failure: route to error handling or escalate to parent workflow


## Evaluation Gates

### Gate 1: Intake Validation
- Query matches skill scope
- Required inputs present
- No scope violations detected

### Gate 2: Skill Load Validation
- Skill file exists and is valid
- Agent binding is valid
- Required vault sources accessible

### Gate 3: Output Validation
- Epistemic class labels present
- Provenance recorded for all derived claims
- Confidence ceiling not exceeded
- No unresolved CRITICAL_GAPs
- Scope compliance verified


## Error Handling

| Error Type | Detection | Recovery |
|---|---|---|
| Scope violation | Gate 1 check | Route to parent skill |
| Missing evidence | Gate 3 check | Flag as GAP, reduce confidence to 0.5 |
| Contradiction | Gate 3 check | Flag as CRITICAL_GAP, halt |
| Provenance loss | Gate 3 check | Mark as UNKNOWN, request human review |
| Timeout | Step budget exceeded | Return partial result with warnings |
| Drift | Confidence calibration check | Trigger drift alignment governor |


## Human-in-the-Loop

- **Default**: Automated execution without human intervention
- **Escalation triggers**:
  - CRITICAL_GAP detected
  - Confidence below 0.3
  - Scope violation requiring reclassification
  - Contradiction that cannot be auto-resolved
- **Review checkpoint**: After Gate 3, if any warnings are present


## Monitoring

- **Trace level**: Full (inputs, outputs, intermediate steps)
- **Metrics**: Step count, token usage, confidence, gap count, execution time
- **Alerts**: CRITICAL_GAP, confidence < 0.3, scope violation, timeout
- **Provenance**: Every output traces back to source evidence via provenance chain


## Composition

- **Skill**: `amos-learning-memory-knowledge-feedback-governor`
- **Agent**: `amos-learning-memory-knowledge-feedback-governor-agent`
- **Parent workflow**: Routes via `AMOS_HOME` or parent skill workflow
- **Chain depth**: Maximum 3 workflows in sequence without orchestrator approval
- **Parallel execution**: Supported when independent capabilities are invoked

