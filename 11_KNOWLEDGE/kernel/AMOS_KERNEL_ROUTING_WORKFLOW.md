---
title: AMOS KERNEL ROUTING WORKFLOW
tags:
- canon-group/tech-ai
- canon/os-module
- rscf/claim
- rscf/provenance
- rscf/state/source-claim
- topic/amos-kernel-routing-workflow
- kernel
- k-meta-logic
- amos-ubi-kernel
- 00-home
- knowledge-moc
- system-scan-agent
- amos-simulation-kernel-v0-math-foundations
- automation-profiles
- kernel-moc
type: document
source: 11_KNOWLEDGE/kernel
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: AMOS_knowledge
---

# AMOS Kernel Routing Workflow

Determine which AMOS kernels handle a task, using the brain's kernel registry and routing rules.

## Kernel Registry (from AMOS_KERNEL_CONFIG.json)

| ID | Name | Priority | Required | Domains | Dependencies |
|----|------|----------|----------|---------|--------------|
| [[K_META_LOGIC]] | Meta Logic & Law Kernel | 10 | Yes | logic, law_of_law, reasoning | — |
| K_MATH_COMPUTE | Math & Computation Kernel | 9 | Yes | math, compute, optimization | [[K_META_LOGIC]] |
| K_BIO_NEURO | Biology & Neuro Kernel | 9 | Yes | ubi, biology, nervous_system | [[K_META_LOGIC]] |
| K_MIND_BEHAVIOR | Mind, Emotion & Behaviour Kernel | 8 | Yes | psychology, emotion, behaviour | K_BIO_NEURO, [[K_META_LOGIC]] |
| K_TECH_ENGINE | Technology & Engineering Kernel | 7 | No | software, ai, cloud, infra | [[K_META_LOGIC]], K_MATH_COMPUTE |
| K_EV_INFRA | EV Infrastructure Kernel | 7 | No | ev, charging, logistics, fleet | K_TECH_ENGINE, K_MATH_COMPUTE |
| K_UNIPOWER_OPS | UniPower Operational Brain | 8 | No | unipower, vn, ops, drivers, stations | K_EV_INFRA, K_TECH_ENGINE |
| K_UNIPOWER_TECH | UniPower Tech & Design MetaBrain | 8 | No | unipower, tech, ai, design | K_TECH_ENGINE, [[K_META_LOGIC]] |

## Routing Rules

### ROUTE_EV
Match tags: ev, charging, station, driver, fleet
Activate: [[K_META_LOGIC]], K_MATH_COMPUTE, K_EV_INFRA, K_UNIPOWER_OPS

### ROUTE_TECH
Match tags: software, ai, architecture, system_design
Activate: [[K_META_LOGIC]], K_MATH_COMPUTE, K_TECH_ENGINE, K_UNIPOWER_TECH

### ROUTE_PSYCH
Match tags: emotion, behaviour, psychology, ubi
Activate: [[K_META_LOGIC]], K_BIO_NEURO, K_MIND_BEHAVIOR

### ROUTE_DEFAULT (fallback)
Match tags: * (all)
Activate: [[K_META_LOGIC]], K_MATH_COMPUTE, K_BIO_NEURO

## Routing Procedure

1. Identify task tags (what domains does this touch?)
2. Check specific routes in order: EV → TECH → PSYCH. Multiple routes can match → union of kernels.
3. Apply ROUTE_DEFAULT as baseline (always included).
4. Check dependencies: every kernel's dependencies must also be activated. K_MIND_BEHAVIOR needs K_BIO_NEURO+[[K_META_LOGIC]]. K_TECH_ENGINE needs [[K_META_LOGIC]]+K_MATH_COMPUTE. K_EV_INFRA needs K_TECH_ENGINE+K_MATH_COMPUTE. K_UNIPOWER_OPS needs K_EV_INFRA+K_TECH_ENGINE. K_UNIPOWER_TECH needs K_TECH_ENGINE+[[K_META_LOGIC]].
5. Resolve conflicts: [[K_META_LOGIC]] resolves (Law of Law — never override).
6. Final set = matched kernels + dependency closure + default baseline.

## Task Type → Kernel Mapping

| Task type | Primary | Secondary | Tertiary |
|-----------|---------|-----------|----------|
| Logic, law, reasoning | [[K_META_LOGIC]] | — | — |
| Math, computation, optimisation | K_MATH_COMPUTE | [[K_META_LOGIC]] | — |
| Biology, neuroscience, UBI | K_BIO_NEURO | [[K_META_LOGIC]] | — |
| Emotion, psychology, behaviour | K_MIND_BEHAVIOR | K_BIO_NEURO | [[K_META_LOGIC]] |
| Software, AI, cloud, infra | K_TECH_ENGINE | [[K_META_LOGIC]], K_MATH_COMPUTE | — |
| EV, charging, logistics, fleet | K_EV_INFRA | K_TECH_ENGINE, K_MATH_COMPUTE | K_UNIPOWER_OPS |
| VN operations, drivers, stations | K_UNIPOWER_OPS | K_EV_INFRA, K_TECH_ENGINE | — |
| Tech design, AI, meta-design, governance | K_UNIPOWER_TECH | K_TECH_ENGINE, [[K_META_LOGIC]] | — |

## Mode-Based Selection (from AMOS_Omni_KERNEL routing)

logic-heavy→Meta_Logic_Kernel | math-heavy→Math_Foundations | human_state→[[AMOS_UBI_KERNEL]] | multi-agent→Multi_Agent_Coordination principles | prediction→TSS_TPE_Engine | ecosystem→PSI_Core | org_design→Organizational_Behavior_Kernel | tech_design→Toolchain_Integration_Kernel | policy→Political_Dynamics_Kernel

## Dependency Closure Algorithm

```
function closure(desired):
    result = set(desired)
    queue = list(desired)
    while queue:
        k = queue.pop()
        for dep in dependencies[k]:
            if dep not in result:
                result.add(dep)
                queue.push(dep)
    return result
```

## Logging (from kernel config)

Log: kernel selection, safety decisions, high-risk requests, which routing rule matched.

## Example: EV Charging Network for Hanoi

Task: "Design an EV charging station network for Hanoi with driver scheduling and financial modelling"

Tags: ev, charging, station, driver, fleet, vn, ops, financial, system_design

ROUTE_EV matches → [[K_META_LOGIC]], K_MATH_COMPUTE, K_EV_INFRA, K_UNIPOWER_OPS
ROUTE_TECH matches (system_design) → adds K_TECH_ENGINE, K_UNIPOWER_TECH

Dependency closure: [[K_META_LOGIC]] (none), K_MATH_COMPUTE (+[[K_META_LOGIC]] ✓), K_EV_INFRA (+K_TECH_ENGINE ✓, +K_MATH_COMPUTE ✓), K_UNIPOWER_OPS (+K_EV_INFRA ✓, +K_TECH_ENGINE ✓), K_TECH_ENGINE (+[[K_META_LOGIC]] ✓, +K_MATH_COMPUTE ✓), K_UNIPOWER_TECH (+K_TECH_ENGINE ✓, +[[K_META_LOGIC]] ✓).

Final: [[K_META_LOGIC]], K_MATH_COMPUTE, K_TECH_ENGINE, K_EV_INFRA, K_UNIPOWER_OPS, K_UNIPOWER_TECH (6 kernels).

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS · SYSTEM_SCAN_AGENT · AUTOMATION_PROFILES · [[AMOS_UNIFIED_CODING_KERNEL_VINFINITY]] · [[AMOS_REINFORCEMENT_LEARNING_ANALYSIS_KERNEL]] · [[AMOS_BEHAVIORAL_ECONOMICS_KERNEL]] · [[AMOS_ORG_GOVERNANCE_KERNEL]]

---
**MOC:** [[KERNEL_MOC]]

