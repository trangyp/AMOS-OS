---
title: 11k architecture decision record
type: reference
source: 07_SKILLS/amos-c10-tech-engineering-master/references
tags: [reference, amos-c10-tech-engineering-master, canon/skill]
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: skill_reference
---


# 11K Architecture Decision Record

> Source: `/Users/mac/Documents/AMOS_OS/11_KNOWLEDGE/Cosmo_Brain/ARCHITECTURE_DECISION_RECORD.md`
> Epistemic class: SOURCE_DERIVED

# COSMO Architecture Decision Record (ADR)

This document captures all significant architectural decisions made during the COSMO project. Each decision includes context, alternatives considered, and the chosen approach with its rationale.

## ADR-001: Monorepo Structure

**Status**: Accepted

**Context**: The project needs to share code between mobile (React Native + Expo), web (Next.js), and admin consoles while maintaining clear boundaries between UI, domain, and infrastructure logic.

**Considered Options**:
1. **Monorepo with npm workspaces** (chosen): Single version management, shared packages, unified CI/CD
2. **Multi-repo**: Separate version cycles, but duplication and context switching overhead
3. **Mobile-first repo + web separate**: Tight coupling issues, harder to share domain logic

**Decision**: Use monorepo with turbo for task orchestration and npm workspaces for package management.

**Rationale**: 
- Enables shared `packages/domain`, `packages/audio`, `packages/art-engine`
- Single source of truth for types and tokens
- Unified testing and type checking
- Turbine-powered CI ensures only changed packages run tests

**Related Files**: `package.json`, `turbo.json`, `packages/*`

---

## ADR-002: Backend Platform: Supabase

**Status**: Accepted

**Context**: Need for auth, Postgres, storage, and edge functions with minimal infrastructure management.

**Considered Options**:
1. **Supabase (chosen)**: Postgres + Auth + Storage + Edge Functions + RLS in one package
2. **Firebase**: Real-time db, auth, storage, but limited SQL flexibility
3. **Self-hosted Postgres + Auth service**: Full control, but high ops overhead
4. **AWS Amplify**: Good integration, but costlier at scale

**Decision**: Use Supabase for all backend needs.

**Rationale**:
- PostgreSQL with full SQL power and JSONB for flexible schemas
- Row-level security (RLS) out-of-the-box for data isolation
- Storage with signed URLs for secure sharing (gifts)
- Edge Functions for processing (audio feature extraction, artwork generation)
- Built-in auth (email/password, Apple, Google, magic links)
- Generous free tier for MVP
- TypeScript types for all services

**Related Files**: `supabase/migrations/`, `supabase/functions/`, `packages/api-client/`

---

## ADR-003: Artwork Determinism and Versioning

**Status**: Accepted

**Context**: The resonance artwork must be deterministic — same audio + same features + same seed → same artwork. This enables replay, comparison, and version management.

**Considered Options**:
1. **Deterministic SVG generation with seeded PRNG** (chosen): Same inputs always produce same output
2. **Hash-based content addressable storage**: Content-addressed by feature vector hash
3. **Server-side rendering only**: No client-side generation, always server-generated

**Decision**: Use deterministic SVG generation with explicit versioning.

**Implementation Detail**:
- `artwork_engine_version = "cosmo-art-v1"` stored with each artwork
- `seed UUID` stored per artwork (can be user-selected or derived from features)
- `parameter_payload_json` stores all mapped visual parameters
- `mapFeaturesToVisualParameters()` in `packages/art-engine` is the core mapping function
- Reproducibility record stored per artwork generation

**Rationale**:
- Enables before/after comparison with morph animation
- Same scan re-generates same artwork (user can re-view at any time)
- Version upgrades can be applied systematically
- Fallback: if animation fails, show static art without re-processing

**Related Files**: `packages/art-engine/`, `DATABASE_PROPOSAL.md` (resonance_artworks table)

---

## ADR-004: Audio Storage Privacy-First

**Status**: Accepted

**Context**: Audio recordings are the most sensitive user data. Default behavior must be privacy-protecting.

**Considered Options**:
1. **Audio storage OFF by default** (chosen): `save_audio_default: false` in user preferences
2. **Audio storage ON by default**: Convenient but violates privacy-first principle
3. **

---
**MOC:** [[references_MOC]]

## Related

- [[07_SKILLS_MOC]]
---

**Related:** [[00_HOME]] · [[AMOS_RSCF_NODES]] · [[LAW_HIERARCHY]] · [[references_MOC]] · [[07_SKILLS_MOC]]

**MOC:** [[references_MOC]]

**Trang Framework:** [[TRANG_FRAMEWORK_RECURSIVE_ONTOLOGY_DYNAMICS]]

---
RSCF-NODE
node_id: amos-c10-tech-engineering-master-11k-architecture-decision-record
node_type: reference
path: 07_SKILLS/amos-c10-tech-engineering-master/references/11k_architecture_decision_record.md
RSCF-RELATIONS:
- INDEXED_BY: [[00_HOME]]
- INDEXED_BY: [[AMOS_RSCF_NODES]]
- CHILD_OF: [[references_MOC]]
