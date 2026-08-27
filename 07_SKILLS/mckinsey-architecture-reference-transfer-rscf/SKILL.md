---
title: SKILL
type: skill
name: mckinsey-architecture-reference-transfer-rscf
description: Architecture Reference Transfer — McKinsey strategic capability. Use when strategic analysis, business consulting, or McKinsey-framework reasoning. Use when amos-c08-strategy-game-master routes to this specialized capability.
parent_skill: amos-c08-strategy-game-master
domain: mckinsey
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, mckinsey-architecture-reference-transfer-rscf]
---


# Mckinsey: architecture Reference Transfer Rscf

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c08-strategy-game-master`
- **Domain**: mckinsey
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

McKinsey strategy framework for Mckinsey: architecture Reference Transfer Rscf

## When to Use

- When mckinsey strategy framework for mckinsey: architecture reference transfer rscf is needed within the mckinsey domain
- When the parent skill (`amos-c08-strategy-game-master`) routes to this specialized capability
- When a query requires mckinsey-specific reasoning grounded in vault sources
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **architecture_reference.assess_commercial**: Assess commercial due diligence: market, competitive position, and growth
- **architecture_reference.evaluate_credit**: Evaluate credit and lending: risk scoring, portfolio, and concentration
- **architecture_reference.analyze_banking**: Analyze banking CRM: customer lifetime value, retention, and cross-sell
- **architecture_reference.transfer_architecture**: Transfer architecture references: best practices across organizational contexts
- **architecture_reference.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **architecture_reference.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **architecture_reference.validate_outputs**: Validate outputs against domain constraints and epistemic class.

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_C08_STRATEGY_GAME_MASTER_KNOWLEDGE.md` (content_hash: 4b676ad6f9ca020f) (vault canon, SOURCE_CLAIM)
> **Additional source**: `11_KNOWLEDGE/AMOS_C09_ORG_LAW_POLICY_MASTER_KNOWLEDGE.md` (content_hash: bead46b07fc02558) (vault canon, SOURCE_CLAIM)

### McKinsey Architecture Reference Transfer

From C08 Strategy & Game: Consulting frameworks and strategic architecture. From C09 Org & Law: Organizational architecture and governance.

**Reference transfer model**:
- **Architecture reference**: a documented architecture pattern from one domain
- **Transfer**: applying the architecture pattern to a new domain
- **Adaptation**: adapting the pattern to fit the new domain's constraints
- **Validation**: validating that the transferred architecture works in the new domain

**Transfer protocol**:
1. **Identify reference**: identify the source architecture pattern
2. **Analyze constraints**: analyze the target domain's constraints
3. **Map**: map the reference architecture to the target domain
4. **Adapt**: adapt the architecture to fit target constraints
5. **Validate**: validate the adapted architecture
6. **Document**: document the transfer with provenance

**Transfer laws**:
- `REFERENCE != SOLUTION`: a reference architecture is not a solution; it must be adapted
- `PATTERN != GUARANTEE`: a pattern that works in one domain does not guarantee success in another
- `TRANSFER != COPY`: transfer is adaptation, not copying

### Epistemic Boundary

Architecture reference transfer is an analytical methodology. It does not prove the transferred architecture is optimal, that all patterns transfer, or that adaptation is always successful.

## Instant Start

> **Reference**: See `references/mckinsey-architecture-reference-transfer-rscf_code.md` (content_hash: 39b5c8a5b4df8e2c) for the code implementation.

## Core Components

| Component | Import Path | Purpose |
|-----------|-------------|---------|
| `HierarchicalGenerator` | `.core` | Rule-based 7-level hierarchy |
| `GoalDrivenGenerator` | `.goal_core` | Natural language goal parsing |
| `UnifiedGenerator` | `.unified_generator` | Combines both approaches |
| `PatternLibrary` | `.patterns` | Code templates for 5 pattern types |
| `AMOSArchitectureBridge` | `.integration` | AMOS ecosystem integration |

## CLI Commands

```bash
# Main CLI
python -m hierarchical_ai_architecture_generator generate --limit 1000
python -m hierarchical_ai_architecture_generator query --layer safety_controller
python -m hierarchical_ai_architecture_generator demo

# Goal-driven CLI
python goal_driven_ai_architecture_generator_v2.py generate \
    --goal "Create retrieval system" --count 50
python goal_driven_ai_architecture_ge

---
**Links:** [[07_SKILLS_MOC]]
