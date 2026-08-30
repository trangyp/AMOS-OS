---
Type: Workflow
Skill: amos-flow-canon
Agent: amos-flow-canon-agent
Trigger: When analyzing how power, energy, capital, or information moves through a system; when throughput needs structural characterization; when identifying bottlenecks, leakage, or queue dynamics; or when flow is asserted but not structurally characterized.
Version: 1.1.0
title: AMOS Flow Canon
tags:
- type/workflow
- domain/canon-universe
- amos-os
---

# AMOS Flow Canon

## Preconditions

- Skill `amos-flow-canon` is loaded and available.
- Input falls within the declared domain scope.
- User request matches the trigger conditions above.

## Steps

1. **Detect flow assertion** — Identify where a flow claim is made (throughput, transmission, conversion, power movement).
2. **Characterize throughput** — Determine the constrained throughput rate, conversion efficiency, and capacity limits.
3. **Detect bottleneck** — Identify the rate-limiting step or component that constrains overall throughput.
4. **Detect leakage** — Identify dissipation points where flow is lost without productive conversion.
5. **Analyze queue** — Characterize queue dynamics: depth, wait time, backpressure, and overflow risk.
6. **Map to 7-Part** — Connect flow findings to Part I (Constraint: capacity limits), Part III (Structure: flow topology), Part IV (Enforcement: flow invariants).
7. **Scale transition check** — Verify flow persistence across H/M/L scale transitions.
8. **Finalize** — Emit flow audit with throughput, bottleneck, leakage, and queue findings.

## Operations

1. **Detect flow assertion** — Identify where a flow claim is made (throughput, transmission, conversion, power movement).
2. **Characterize throughput** — Determine the constrained throughput rate, conversion efficiency, and capacity limits.
3. **Detect bottleneck** — Identify the rate-limiting step or component that constrains overall throughput.
4. **Detect leakage** — Identify dissipation points where flow is lost without productive conversion.
5. **Analyze queue** — Characterize queue dynamics: depth, wait time, backpressure, and overflow risk.
6. **Map to 7-Part** — Connect flow findings to Part I (Constraint: capacity limits), Part III (Structure: flow topology), Part IV (Enforcement: flow invariants).
7. **Scale transition check** — Verify flow persistence across H/M/L scale transitions.
8. **Finalize** — Emit flow audit with throughput, bottleneck, leakage, and queue findings.

## Validation Gates

- [ ] Throughput structurally characterized (rate, capacity, conversion efficiency)
- [ ] Bottleneck identified or explicitly marked as absent
- [ ] Leakage identified or explicitly marked as absent
- [ ] Queue dynamics characterized (depth, wait, backpressure)
- [ ] Flow mapped to 7-Part Canon (Parts I, III, IV)
- [ ] Scale transition checked (H/M/L)
- [ ] Epistemic class labeled
- [ ] Provenance recorded
- [ ] Confidence ceiling enforced

## Error Handling

- **Scope violation**: Reject and route to parent skill.
- **Contradiction**: Flag CRITICAL_GAP and halt; do not fabricate canon.
- **Provenance loss**: Mark output as UNKNOWN and request human review.
- **Drift**: Trigger drift alignment governor before re-execution.

## Composition

- Can be invoked by parent master skill for domain-specific audits.
- Can delegate to `amos-audit-repair-master` for gap escalation.
- No delegation to non-AMOS skills.

## Provenance

- **Origin architect**: Trang Phan
- **Steward**: Trang Phan
- **Epistemic class**: AMOS_MODEL
- **RSCF state**: SOURCE_CLAIM
