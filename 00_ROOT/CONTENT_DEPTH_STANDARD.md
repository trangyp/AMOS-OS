---
title: AMOS Content Depth Standard
type: documentation_contract
source: 00_ROOT
origin_architect: Trang Phan
amos_core_target: v4.4
status: ACTIVE_DERIVED_STANDARD
conclusion_class: DERIVED
updated: 2026-09-03
rscf:
  state: DERIVED
  claim_class: AMOS_MODEL
  provenance: AMOS_corpus
  scope: active__AMOS_OS
---

# AMOS Content Depth Standard

“Small file” is not automatically a defect. Content depth must match artifact function.

## 1. Navigation gateway / README

May remain compact when its only job is stable identity and routing.

Minimum:
- purpose;
- canonical owner;
- primary links;
- `ROUTE != AUTHORITY` boundary.

A gateway should **not** duplicate a 50–100 KB source document merely to look complete.

## 2. MOC / architecture map

Must be substantive enough to support reasoning without loading raw evidence.

Minimum:
- primary ownership/purpose;
- what it explicitly does not own;
- MECE components/classes;
- lifecycle or flow where relevant;
- inputs/outputs/interfaces;
- authority/epistemic boundaries;
- key local and source-backed artifacts;
- known gaps;
- parent and sibling dependencies.

A MOC that only says “this folder contains X” is under-specified.

## 3. Contract

Must define normative invariants and validation/failure behavior.

Minimum:
- identity/scope;
- allowed inputs/outputs/effects;
- hard invariants;
- preconditions;
- authority/freshness/provenance requirements;
- error/failure/degraded states;
- rollback/recovery where relevant;
- compatibility/version semantics;
- executable-validation boundary.

## 4. Source / knowledge master

May be large. Preserve source terminology, provenance and epistemic class. Do not rewrite it into
runtime truth.

## 5. Model

Must separate assumptions/definitions/model equations from observations and independent empirical
validation.

## 6. Receipt / audit

Must be bounded to subject/version/environment/time/scope. Audit narrative is evidence of the audit,
not universal proof.

## 7. Expansion rule

Expand an artifact only when:
1. the current function requires more semantics;
2. richer source material exists or a clearly marked DERIVED model is justified;
3. expansion reduces ambiguity/overlap;
4. provenance and epistemic boundaries survive.

Do **not** expand by:
- repeating the same source into many planes;
- inventing missing implementation;
- promoting source claims;
- making every README a second MOC;
- increasing token volume without decision value.

## 8. Architecture quality test

A plane is sufficiently documented when a new AMOS worker can determine:
- what the plane owns;
- what neighboring planes own instead;
- how data/control enters and leaves;
- what authority is required;
- where source truth and execution evidence live;
- what failures/gaps remain.

`MORE WORDS != MORE ARCHITECTURE`.
