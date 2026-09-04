---
title: 02_COGNITIVE_RPG MOC
type: map_of_content
status: ACTIVE
conclusion_class: DERIVED
origin_architect: Trang Phan
governed_by: [[05_COGNITIVE_ORGANISM/COGNITIVE_ORGANISM_COGNITIVE_ORGANISM_CONTRACT.md|COGNITIVE_ORGANISM_CONTRACT]]
rscf-state: source-claim
---

# 02_COGNITIVE_RPG Map of Content

## Overview
Cognitive role-playing, narrative world-state synthesis, and dynamic persona interaction architecture.

## Core Documents
- [[21_DOMAINS/02_COGNITIVE_RPG/AMOS_LANGUAGE_RPG_TRANSFORMATION_ENGINE.md|AMOS Language RPG Transformation Engine]]
- [[21_DOMAINS/18_C08_STRATEGY_GAME/C08_STRATEGY_GAME_DOMAINS_DOMAIN_SPEC.md|C08 Strategy & Game Theory Spec]]
- [[05_COGNITIVE_ORGANISM/WORLD_MODEL_ENGINE.md|World Model Engine]]

## Navigation
- Return to: [[21_DOMAINS/21_DOMAINS_MOC.md|21_DOMAINS MOC]], [[00_ROOT/00_ROOT_MOC.md|Root MOC]].

---

## Domain Overview
The **02_COGNITIVE_RPG** domain formalizes cognitive role-playing, narrative world-state synthesis, and dynamic persona interaction within the AMOS brain architecture. It provides the representational substrate through which the cognitive organism can simulate counterfactual scenarios, embody multiple agent personas, and synthesize coherent narrative world-states from heterogeneous input streams. This domain bridges the gap between abstract reasoning primitives (MURK, Absolute Logic) and concrete narrative instantiation, enabling the system to "think in character" while preserving epistemic discipline. It is governed by the [[05_COGNITIVE_ORGANISM/COGNITIVE_ORGANISM_COGNITIVE_ORGANISM_CONTRACT.md|COGNITIVE_ORGANISM_CONTRACT]] and feeds synthesized world-states into the World Model Engine for downstream reasoning. The RPG transformation engine is the primary artifact: it maps natural language utterances into structured role-play state transitions, maintaining persona consistency, memory continuity, and deontic constraint propagation across multi-turn interactions. This domain is essential for any AMOS capability that requires simulated social reasoning, strategic counterfactual exploration, or narrative-grounded knowledge synthesis.

## MECE Classification
This domain belongs to **Domain A: Cognitive & Reasoning** in the AMOS MECE taxonomy. It shares this partition with philosophy of mind, formal logic, and the MURK reasoning kernel. The cognitive RPG layer is distinct from pure logic (which operates on abstract propositions) in that it grounds reasoning in embodied narrative context, persona identity, and world-state simulation. It is separated from Domain D (Information & Model) because it produces simulated experiential content rather than indexing or retrieving stored knowledge. Its MECE boundary with Domain E (Governance & Security) is enforced by the cognitive organism contract: RPG-generated world-states are advisory simulations, not authoritative decisions, and cannot bypass the capability-bound governance kernel.

## Key Artifacts
- [[21_DOMAINS/02_COGNITIVE_RPG/AMOS_LANGUAGE_RPG_TRANSFORMATION_ENGINE.md|AMOS Language RPG Transformation Engine]] — core transformation engine mapping natural language to structured RPG state transitions
- [[21_DOMAINS/18_C08_STRATEGY_GAME/C08_STRATEGY_GAME_DOMAINS_DOMAIN_SPEC.md|C08 Strategy & Game Theory Spec]] — strategy and game-theoretic domain specification feeding the RPG layer
- [[05_COGNITIVE_ORGANISM/WORLD_MODEL_ENGINE.md|World Model Engine]] — downstream consumer of synthesized RPG world-states

## Cross-Domain Relationships
- **Cognitive Organism Plane**: [[05_COGNITIVE_ORGANISM/COGNITIVE_ORGANISM_COGNITIVE_ORGANISM_CONTRACT.md|COGNITIVE_ORGANISM_CONTRACT]] — governing contract for all cognitive-layer domains
- **Strategy & Game Theory**: [[21_DOMAINS/18_C08_STRATEGY_GAME/C08_STRATEGY_GAME_DOMAINS_DOMAIN_SPEC.md|C08 Strategy & Game Theory Spec]] — provides game-theoretic primitives consumed by RPG scenarios
- **Root Navigation**: [[00_ROOT/00_ROOT_MOC.md|Root MOC]] — top-level vault navigation
- **Domains Plane**: [[21_DOMAINS/21_DOMAINS_MOC.md|21_DOMAINS MOC]] — parent plane index

## Subdomain Structure
- **Narrative World-State Synthesis**: Construction and maintenance of coherent narrative world-states from heterogeneous input, including spatial, temporal, and social context tracking.
- **Persona Interaction Architecture**: Dynamic persona modeling, identity consistency enforcement, and multi-persona dialogue management across extended interactions.
- **Language-to-State Transformation**: Mapping natural language utterances into structured state transitions, maintaining semantic fidelity and deontic constraint propagation.
- **Counterfactual Scenario Simulation**: Generation and evaluation of alternative narrative trajectories for strategic reasoning and decision support.

## Reasoning Patterns
The cognitive RPG domain employs several distinct reasoning patterns:
- **Narrative abduction**: Inferring plausible world-state explanations from observed dialogue and action sequences.
- **Persona-consistent deduction**: Deriving persona-appropriate responses while maintaining identity constraints and memory continuity.
- **Counterfactual projection**: Simulating alternative decision branches and their narrative consequences.
- **Deontic constraint propagation**: Ensuring that obligations, permissions, and prohibitions are consistently enforced across simulated interactions.

These patterns feed into the broader AMOS reasoning stack via the World Model Engine, which integrates RPG-simulated states with observational data and formal logic outputs.

## Epistemic Boundary
- **Epistemic class**: DERIVED — this MOC is a derived structural index, not a primary source claim.
- **Provenance**: authoritative_AMOS_OS_structure — generated from the canonical vault directory layout.
- **Scope**: active__AMOS_OS — applies to the currently active AMOS OS vault instance.
- **Limitation**: RPG-simulated world-states are advisory simulations; they do not constitute observational evidence or authoritative decisions. `SIMULATION != OBSERVATION`, `NARRATIVE != PROOF`.
- **Claim boundary**: The transformation engine specification is structurally present; end-to-end executable closure of the RPG runtime is `UNKNOWN/GAP` unless independently established.
- **Authority boundary**: RPG-generated persona outputs are simulated responses, not agent commitments. `PERSONA_OUTPUT != AGENT_DECISION`. All consequential decisions must pass through the capability-bound governance kernel (v4.8).

---

**Parent:** [[21_DOMAINS/00_INDEX/DOMAINS_MOC|DOMAINS_MOC]]
