---
title: TOKEN
tags: [misc, reference, general]
type: document
source: 11_KNOWLEDGE/misc
---




# AMOS Token and Context Governor

## Objective
Maximize decision-relevant information per token without deleting load-bearing structure.

## Priority score
Retain context in this order:
1. objective and hard constraints
2. decision-changing evidence
3. unresolved contradictions
4. load-bearing premises
5. provenance/freshness/scope
6. active hypotheses
7. required implementation details
8. reusable summaries
9. examples/background
10. redundant narrative

## Progressive disclosure
Do not load raw evidence by default.
Use:
`capsule -> relevant H -> relevant M -> relevant L -> raw`

## Drop rule
Drop an item only if removing it cannot reasonably change:
- answer
- decision
- confidence
- safety
- falsifier
- implementation correctness

## Context pressure
When context is near capacity:
- preserve constraints over prose,
- preserve dependency edges over explanations,
- preserve unresolved conflict over resolved history,
- snapshot before major compression.

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
