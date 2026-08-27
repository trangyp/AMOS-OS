---
title: amos-learning-memory-knowledge-feedback-governor-workflow
Type: Workflow
Skill: amos-learning-memory-knowledge-feedback-governor
Agent: amos-learning-memory-knowledge-feedback-governor-agent
Trigger: When C05 inference outcomes need to be encoded into Memory Systems, when memory entries need to be consolidated into the Knowledge Research vault, when indexed knowledge needs to be retrieved to inform new C05 inference, when the full feedback loop needs governance, when detecting knowledge drift, when validating epistemic preservation across domain transitions, or when amos-knowledge-research-master routes to cross-domain learning-memory-knowledge feedback governance
Version: 1.0.0
tags: [note, vault]
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
