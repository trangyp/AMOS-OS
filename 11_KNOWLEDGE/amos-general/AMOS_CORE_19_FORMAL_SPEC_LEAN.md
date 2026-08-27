---
title: "AMOS CORE-19 v0.3 — Formal Specification (Lean-style)"
type: reference
tags: [canon-group/tech-ai, amos, deterministic-logic, formal-spec, CORE-19, lean, theorem-proving, sorts, predicates, canon/framework, rscf/state/observation, rscf/claim, rscf/provenance, topic/amos-core-19-formal-spec-lean]
---

# AMOS CORE-19 v0.3 — Formal Specification (Lean-style)

## Sorts

```lean
universe u

-- Sorts
constant E : Type u    -- entities
constant T : Type u    -- time points
constant R : Type u    -- regions
constant I : Type u    -- information
```

## Basic Predicates and Functions

```lean
-- Basic predicates and functions
constant Ex   : E → T → Prop          -- existence
constant Caus : E → E → T → Prop      -- causality
constant InR  : E → R → T → Prop      -- spatial location
constant Info : E → T → I             -- information state

constant ltT  : T → T → Prop          -- time order
infix `<ₜ` : 50 := ltT

constant OpenR : R → Prop             -- open region
constant Path  : E → E → R → Prop     -- causal path region
```

## Meta-Logical Operators

```lean
-- Null information constant
constant i0 : I

-- Logical / meta-logical operators on propositions
constant PLogic  : Prop → Prop        -- PositiveLogic
constant NLogic  : Prop → Prop        -- NegativeLogic
constant CLogic  : Prop → Prop        -- ContradictionLogic
constant ELogic  : Prop → Prop        -- ExistenceLogic
constant MLogic  : Prop → Prop        -- ModalLogic
```

## Core Structure

This is a Lean-style formal specification defining the foundational types and predicates for AMOS's deterministic reasoning kernel. The spec uses Lean's dependent type system to encode:

- **Sorts**: Entity, Time, Region, Information
- **Predicates**: Existence, Causality, Spatial Location, Information State
- **Meta-logical operators**: Positive, Negative, Contradiction, Existence, Modal logic

### Design Principles

1. **Explicit typing**: Every concept has a well-defined type
2. **Temporal grounding**: All predicates indexed by time points
3. **Causal tracking**: Explicit causality predicate linking entities through time
4. **Meta-logical soundness**: Logical operators defined at the meta-level to prevent self-reference paradoxes

### Relationship to AMOS

This formal spec underpins the Core-19 reasoning kernel used across all AMOS engines. It provides the type-theoretic foundation for:
- The 19×19 semantic matrix
- The MURK absolute logic DB
- All domain engine reasoning chains

---

*Source: Google Drive /_00_AMOS_CANON/Reasoning kernel.txt — Lean-style formal specification, 211 lines.*

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[AMOS-GENERAL_MOC]]
