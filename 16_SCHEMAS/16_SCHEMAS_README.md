---
title: "16 Schemas — README"
type: readme
source: 16_SCHEMAS
origin_architect: Trang Phan
steward: Trang Phan
amos_core_target: v4.4
status: ACTIVE
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: schemas_readme
---

# 16 Schemas — README

## Role

Schemas define typed contracts — schema ID, version, required fields, optional fields, validation rules, compatibility rules, and migration rules. Schemas are the structural backbone of AMOS data integrity: every RSCF claim, every agent state, every knowledge artifact has a schema that governs its valid form.

## Core Principle

```
Untyped data is untrusted data.
All structured data flows through schema validation before use.
```

## Directory Structure

```
16_SCHEMAS/
├── 00_INDEX/              ← Schema indices, maps, and navigation registries
├── 01_RUNTIME/            ← Runtime schemas (causal transition, session, rejection trace)
├── 06_AGENTS/             ← Agent schemas (agent state, capabilities, provenance)
├── 10_RSCF/               ← RSCF schemas (causal epoch, proof capsule, provenance topology)
├── 11_OBSERVABILITY/      ← Observability schemas (canon health, provenance health)
├── 16_SCHEMAS_MOC.md      ← Master map of content for the Schemas plane
├── SCHEMAS_SCHEMA_CONTRACT.md  ← Invariant governance contract for schemas
├── AGENT_SCHEMA.md        ← Agent structure definition
├── KNOWLEDGE_SCHEMA.md    ← Knowledge artifact structure definition
├── MEMORY_SCHEMA.md       ← Memory record structure definition
├── PROTOCOL_SCHEMA.md     ← Protocol structure definition
├── SECURITY_SCHEMA.md     ← Security artifact structure definition
├── TAG_VOCABULARY.md      ← Controlled tag vocabulary
├── TENSORS.md             ← Tensor definitions
├── TENSOR_CONTRACTS.md    ← Tensor invariant contracts
├── TENSOR_REGISTRY.md     ← Tensor registry
├── CLAIM_TENSOR.md        ← Claim tensor definition
├── EVIDENCE_TENSOR.md     ← Evidence tensor definition
├── RELATION_TENSOR.md     ← Relation tensor definition
└── HETEROGENEOUS_XPU_SCHEDULER_SCHEMA.md  ← XPU scheduler schema
```

## Schema Categories

- **RSCF Schemas:** Define the structure of epistemic claims (UNKNOWN/GAP, SOURCE_CLAIM, EVIDENCE, VALIDATED, CANON)
- **Agent Schemas:** Define agent state, capabilities, provenance, and behavioral contracts
- **Knowledge Schemas:** Define domain knowledge structure, relationships, and classification
- **Tensor Schemas:** Define invariant tensor operations, transformations, and composability rules
- **Runtime Schemas:** Define boot, routing, state, and finalization protocol structures

## Key Schema Properties

- **Schema ID:** Globally unique identifier, immutable once published; semantic versioning (major/minor/patch)
- **Required/Optional Fields:** Required fields must be present; optional fields may be present
- **Validation Rules:** Constraints on field values (type, range, format, referential integrity)
- **Compatibility/Migration Rules:** Backward/forward compatibility between versions; migration procedures for version transforms

## Hard Boundaries

- Schema != Data — a schema defines structure; data is an instance of that structure
- Schema != Validation — schemas define what valid looks like; validation enforces it at runtime
- Schema != Contract — schemas are structural; contracts include behavioral expectations

## Key Protocols

- **Schema Registry:** All schemas registered with version, compatibility rules, and deprecation status
- **Validation Pipeline:** Inbound data validated against schema before processing; invalid data rejected with clear error
- **Schema Evolution:** Backward-compatible additions preferred; breaking changes require migration path
- **Schema Documentation:** Every schema field documented with purpose, type, constraints, and examples

## Key Artifacts

- **Schema Contract:** [[16_SCHEMAS/SCHEMAS_SCHEMA_CONTRACT|SCHEMAS_SCHEMA_CONTRACT]] — invariant governance for all schemas
- **Agent Schema:** [[16_SCHEMAS/AGENT_SCHEMA|AGENT_SCHEMA]] · **Knowledge Schema:** [[16_SCHEMAS/KNOWLEDGE_SCHEMA|KNOWLEDGE_SCHEMA]]
- **Tensor Contracts:** [[16_SCHEMAS/TENSOR_CONTRACTS|TENSOR_CONTRACTS]] · **Tag Vocabulary:** [[16_SCHEMAS/TAG_VOCABULARY|TAG_VOCABULARY]]

## Canonical Laws Governing

- **M07 (Canon ≠ Implementation):** Schema specifications are not runtime implementations
- **CAPABILITY ≠ AUTHORITY:** Schema validation capability does not grant execution authority; untyped data is untrusted

## Cross-Plane Relationships

- **Knowledge:** [[11_KNOWLEDGE/KNOWLEDGE_CONTRACT|KNOWLEDGE_CONTRACT]] — Schemas structure knowledge; knowledge validates schemas
- **Runtime:** [[04_RUNTIME/04_RUNTIME_MOC|04_RUNTIME_MOC]] — Schemas validate runtime data; runtime produces schema-validated outputs
- **Provenance:** [[02_KERNEL/08_PROVENANCE/08_PROVENANCE_MOC|08_PROVENANCE_MOC]] — Schema validation is a provenance event
- **Observability:** [[17_OBSERVABILITY/17_OBSERVABILITY_README|17_OBSERVABILITY_README]] — Schema validation failures produce observability signals
- **Security:** [[18_SECURITY/18_SECURITY_README|18_SECURITY_README]] — Security schemas govern access control; State conforms to schema

## Entry Points

- **Master MOC:** [[16_SCHEMAS/16_SCHEMAS_MOC|16_SCHEMAS_MOC]] · **Contract:** [[16_SCHEMAS/SCHEMAS_SCHEMA_CONTRACT|SCHEMAS_SCHEMA_CONTRACT]] · **Index:** [[16_SCHEMAS/00_INDEX/INDEX_SCHEMAS_README|Schema Index]]

## Implementation Status

- **Structural completeness:** Schema contract, agent/knowledge/memory/protocol/security schemas present
- **RSCF schemas:** Causal epoch, proof capsule, provenance topology, competing hypothesis schemas defined
- **Tensor schemas:** Claim, evidence, relation tensors with contracts and registry
- **Executable closure:** UNKNOWN/GAP — structural patterns unless tied to executed validation evidence

## AMOS MECE Alignment

The Schemas Plane is Plane 16 of 26. It is mutually exclusive from Data (instances) and Contracts (behavioral expectations), collectively exhaustive with all other planes in covering the structural-type dimension. MECE boundary: it owns typed structural contracts, not data instances, behavioral contracts, or runtime validation execution.

______________________________________________________________________

**Parent:** [[00_ROOT/00_HOME|00_HOME]] · [[00_ROOT/00_ROOT_MOC|00_ROOT_MOC]]
