---
title: REPOSITORY REASONING
tags: [misc, reference, general, canon/knowledge]
type: document
source: 11_KNOWLEDGE/misc
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general

---


# Repository Reasoning

## Acquisition before patch
Resolve:
- entrypoint
- implementation location
- callers/callees
- data/control dependencies
- config/environment
- tests/invariants
- smallest causal patch
- affected dependency cone

## Evidence priority
tests/execution > implementation > config/schema > documentation > comments > assumptions.

README claims default to SOURCE_CLAIM.

## Patch rule
Fix mechanism, not symptom.
Prefer minimal causal patch with explicit regression surface.

## Validation
narrow discriminating test → affected tests → repository-native CI/regression gates.

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
