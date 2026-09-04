---
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
title: WORKFLOW
type: note
source: 08_WORKFLOWS/law-stack-enforcement-pipeline
tags:
  - note
  - law-stack-enforcement-pipeline
  - type/workflow
rscf:
  state: AMOS_MODEL
  claim_class: CONDITIONAL
  provenance: AMOS_corpus
  scope: workflow_process
---

# Law Stack Enforcement Pipeline

## Overview

A 3-stage pipeline enforcing the Law of Law™/Rule of 2™/Rule of 4™ hierarchy across AMOS OS skills.

## Stage 1: Constraint Gate (G1)

**Input:** Proposed law text
**Check:** Does the law satisfy Constraint (Part I of 7-Part Canon)?

- Are there genuine constraints, or is the law claiming universal authority without bounds?
- **Pass:** Law proceeds to Stage 2
- **Fail:** Law rejected — cannot proceed to R2 gate

## Stage 2: Rule of 2 Gate (G2)

**Input:** Law that passed Constraint
**Check:** Does the law adhere to the Rule of 2™ as a named binary attractor?

- **Dual-frame test:** Two domains must both be stable for the law to hold
- **Rubber-stamp test:** Does the law merely assert Rule of 2 without proof? → Fail
- **Pass:** Law proceeds to Stage 3
- **Fail:** Law rejected — does not satisfy Rule of 2

## Stage 3: Rule of 4 Gate (G3)

**Input:** Law that passed Rule of 2
**Check:** Is the law quadrant-complete across the four canonical families?

- **Four families:** UBI (biological), TSS (socio-technical), PSI (psychological), QLS (quantum logic)
- **Each quadrant must have:** Declared canonical family + exponent gate + mechanism tag
- **Pass:** Law is fully enforced — output carries QFI/CEL receipt
- **Fail:** Law rejected — quadrant incomplete; must declare which family is missing

## Output Receipt

When all 3 gates pass, the pipeline appends to the skill's output:

- `law_stack::LOL✓R2✓R4`
- `capability_authorized: true`
- `evolution_allowed: true`
- `mutation_gate_passed: true`
- `all_gates_passed: true`
- GMEF failure memory entry (if any gate had previously failed)

## Usage

```bash
## Run the pipeline on a skill's proposed law
hermes pipeline run law-stack-enforcement-pipeline \
  --law-text "<proposed law>" \
  --skill "<target skill name>"
```

______________________________________________________________________

**MOC:** [[08_WORKFLOWS/law-stack-enforcement-pipeline/law-stack-enforcement-pipeline_MOC|law-stack-enforcement-pipeline_MOC]]

## Related

- [[08_WORKFLOWS/08_WORKFLOWS_MOC|08_WORKFLOWS_MOC]]
