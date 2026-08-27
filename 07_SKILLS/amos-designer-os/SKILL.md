---
title: SKILL
type: skill
name: amos-designer-os
description: Designer Os — technology and engineering capability. Use when software development, engineering design, or technical architecture. Use when amos-c10-tech-engineering-master routes to this specialized capability.
parent_skill: amos-c10-tech-engineering-master
domain: c10
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, amos-designer-os]
---


# Designer Os

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c10-tech-engineering-master`
- **Domain**: c10
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

Tech-engineering engine for Designer Os

## When to Use

- When analyzing software architecture: patterns, dependencies, coupling
- When discovering program behavior via black-box analysis or symbolic execution
- When verifying code facts: type safety, memory safety, termination
- When enforcing bounded code: resource, time, and capability limits
- When the parent skill (`amos-c10-tech-engineering-master`) routes to this specialized capability
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **designer.analyze_architecture**: Analyze software architecture: patterns, dependencies, coupling, cohesion
- **designer.discover_program**: Discover program behavior: black-box analysis, symbolic execution, fuzzing
- **designer.verify_code_facts**: Verify code facts: type safety, memory safety, termination, complexity
- **designer.optimize_performance**: Optimize performance: profiling, bottleneck analysis, and resource tuning
- **designer.enforce_bounds**: Enforce bounded code: resource limits, time limits, and capability limits
- **designer.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **designer.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **designer.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 3a6ed833110a8adb) for the full vault-sourced domain knowledge (5421 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `_00_Cosmo brain/amos-general/A/Designer/AMOS Designer OS.md` (content_hash: 3985deaea31b207d) (vault canon, SOURCE_CLAIM)

### Designer OS

From Cosmo Brain AMOS Designer OS: Standalone shell for organizing ideas, roles, and brain model auditably. 5-file standalone shell with 7-layer brain model.

**5 Files**:
- `AMOS.brain` (2,066B): designer-facing control file (identity, goals, constraints, brain model)
- `AMOS.config.json` (506B): runtime configuration
- `README.txt` (1,410B): setup and usage instructions
- `run_amos.py` (4,926B): simple runtime -- loads brain, config, runs workers, logs events
- `workers.py` (3,323B): small worker layer (WORKER_REGISTRY, WorkerResponse)

**4 Goals**:
1. Model multi-layer reasoning and systemic behaviour
2. Maintain full auditability of every reasoning step
3. Keep humans in control, not the machine
4. Support sovereign-grade AI governance and compliance

**4 Constraints**:
1. Deterministic execution (no hidden randomness)
2. Every decision must be loggable and explainable
3. No irreversible actions without explicit human confirmation
4. All worker actions pass through a single motor layer

**7-Layer Brain Model**:
1. **Sensory layer**: raw inputs (text, data, events, metrics)
2. **Perceptual layer**: pattern detection from inputs
3. **Concept layer**: stable concepts, entities, relationships
4. **Narrative layer**: stories, scenarios, timelines
5. **Causal layer**: cause-effect chains, interventions, levers
6. **Systemic layer**: multi-system, multi-actor, multi-decade reasoning
7. **Meta layer**: self-audit, ethics, risk, invariants, boundaries

**Designer OS laws**:
- `DESIGNER != USER`: the designer organizes the system; the user operates it
- `AUDITABLE != TRANSPARENT**: auditable means decisions are loggable; transparent means visible in real-time
- `DETERMINISTIC != RIGID**: deterministic means reproducible; rigid means inflexible

### Epistemic Boundary

Designer OS is a standalone shell architecture. It does not prove all design is auditable, that the 7-layer model is exhaustive, or that deterministic execution covers all cases.

## Failure Modes

- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not 