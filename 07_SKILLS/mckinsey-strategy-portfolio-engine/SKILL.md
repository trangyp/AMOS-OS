---
title: SKILL
type: skill
name: mckinsey-strategy-portfolio-engine
description: Strategy Portfolio Engine — McKinsey strategic capability. Use when strategic analysis, business consulting, or McKinsey-framework reasoning. Use when amos-c08-strategy-game-master routes to this specialized capability.
parent_skill: amos-c08-strategy-game-master
domain: mckinsey
origin_architect: Trang Phan
epistemic_class: SOURCE_CLAIM
tags: [note, mckinsey-strategy-portfolio-engine]
---


# Mckinsey: strategy Portfolio Engine

## Identity

- **Origin architect and steward**: Trang Phan
- **Parent skill**: `amos-c08-strategy-game-master`
- **Domain**: mckinsey
- **Epistemic class**: SOURCE_CLAIM (vault-sourced from AMOS framework)

McKinsey strategy framework for Mckinsey: strategy Portfolio Engine

## When to Use

- When mckinsey strategy framework for mckinsey: strategy portfolio engine is needed within the mckinsey domain
- When the parent skill (`amos-c08-strategy-game-master`) routes to this specialized capability
- When a query requires mckinsey-specific reasoning grounded in vault sources
- When managing lifecycle operations across classify, validate, trace, assess, and detect
- When detecting drift in evidence chains, provenance freshness, or confidence calibration
- When validating outputs against domain constraints and epistemic class

## Capabilities

- **strategy_portfolio.assess_commercial**: Assess commercial due diligence: market, competitive position, and growth
- **strategy_portfolio.evaluate_credit**: Evaluate credit and lending: risk scoring, portfolio, and concentration
- **strategy_portfolio.analyze_banking**: Analyze banking CRM: customer lifetime value, retention, and cross-sell
- **strategy_portfolio.transfer_architecture**: Transfer architecture references: best practices across organizational contexts
- **strategy_portfolio.manage_lifecycle**: Manage lifecycle: classify, validate, trace, assess, detect.
- **strategy_portfolio.detect_drift**: Detect drift in evidence chains, provenance freshness, or confidence calibration.
- **strategy_portfolio.validate_outputs**: Validate outputs against domain constraints and epistemic class.

> **Reference**: See `references/vault_domain_knowledge.md` (content_hash: 88797eb19264cf47) for the full vault-sourced domain knowledge (4415 chars).

## 11_KNOWLEDGE Vault Content

> **Source**: `11_KNOWLEDGE/AMOS_C08_STRATEGY_GAME_MASTER_KNOWLEDGE.md` (content_hash: 4b676ad6f9ca020f) (vault canon, SOURCE_CLAIM)

### McKinsey Strategy Portfolio Engine

From C08 Strategy & Game: Strategic portfolio management.

**Portfolio strategy model**:
- **BCG matrix**: stars, cash cows, question marks, dogs
- **GE-McKinsey matrix**: industry attractiveness vs competitive strength
- **Portfolio balance**: balance growth and cash flow across portfolio
- **Resource allocation**: allocate resources based on strategic priority

**Strategy laws**:
- `STRATEGY != PLAN`: a strategy is a direction; a plan is a sequence of actions
- `PORTFOLIO != COLLECTION`: a portfolio is a balanced set; a collection is an unstructured group
- `ALLOCATION != DISTRIBUTION`: allocation is strategic; distribution is mechanical

### Epistemic Boundary

The strategy portfolio engine is an analytical toolset. It does not prove optimal allocation, that portfolio balance is always achievable, or that strategic frameworks predict outcomes.

## Failure Modes
- **Insufficient evidence**: If source material is insufficient, mark as UNKNOWN/GAP and fail closed — do not fabricate.
- **Scope violation**: If the query falls outside the skill's declared scope, escalate to the parent skill or steward.
- **Binding broken**: If 1:1:1 binding (skill→agent→workflow) is broken, flag routing mismatch and block execution.
- **Validation failure**: If validation gates fail, downgrade confidence, flag the gap, and escalate — do not force-fit.
- **Epistemic overreach**: If a claim exceeds the established evidence or epistemic class, retract and relabel.

## Validation Gates

- **G1 (Law of Law)**: No unresolved contradictions within the skill's scope.
- **G2 (Epistemic class)**: All claims labeled SOURCE / DERIVED / AMOS_MODEL / EMPIRICAL — never claim beyond evidence.
- **G3 (Provenance)**: Source path recorded for every derived claim.
- **G4 (Anti-overreach)**: No claim beyond the skill's declared scope and epistemic class.
- **G5 (Equation firewall)**: Equations carry status tags (ESTABLISHED_MATH / SOURCE_DERIVED / AMOS_MODEL / EMPIRICALLY_CALIBRATED / UNVERIFIED).
- **G6 (Failure mode)**: On validation failure, downgrade confidence, flag the gap, escalate — do not force-fit.

## Provenance

- **Skill**: `mckinsey-strategy-portfolio-engine`
- **Parent**: `amos-c08-strategy-game-master`
- **Domain**: mckinsey
- **Origin architect**: Trang Phan
- **Vault sources**:
- `architecture/DSc ScD Portfolio - Three Canon Architecture.md` — DSc/ScD Portfolio — Trang Phan (Independent Submission) (6148 chars, score: 10, content_hash: ad04085e8f89fc0a)
- `s