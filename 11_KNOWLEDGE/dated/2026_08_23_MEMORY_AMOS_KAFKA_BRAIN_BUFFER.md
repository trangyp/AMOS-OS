---
title: 2026 08 23 MEMORY AMOS KAFKA BRAIN BUFFER
tags: [dated, dated/2026-08-23]
type: document
source: 11_KNOWLEDGE/dated
---


# Memory — AMOS Kafka Brain Buffer

**Created:** 2026-08-23
**Topic:** kafka-brain-buffer, verbena-brain, stream-log-buffer, D8 consciousness, D5 Manas, D6 Citta, D7 Buddhi, D8 Jnana, AMOS MODEL
**Module:** `cosmo-brain/AMOS_Kafka_Brain_Buffer_v1.0.ts` (2001 lines)
**Tests:** `cosmo-brain/AMOS_Kafka_Brain_Buffer_v1.0.test.ts` (1325 lines, 6 categories)
**Generator:** `cosmo-brain/test_kafka_brain_buffer_generator.py` (1053 lines, 8 patterns)

---

## Key Facts

### Module Architecture
- 2001-line TypeScript module operationalizing verbena's 71-concept map into a Kafka-backed brain buffer
- 4-layer consciousness model: D5 Manas (channels) → D6 Citta (buffer/stream) → D7 Buddhi (decision) → D8 Jnana (scoring)
- 16 channels total: 4 ingest + 5 routing + 4 output (D4 union has 8 but filtered to 4 + 4 deploy + 3 telemetry = 16 unique)
- `BufferEntry` has 80+ fields spanning D5/D6/D7/D8
- `InMemoryBrainBuffer` implements LRU eviction, dedup, TTL, stale eviction, health metrics
- `computeD8Score()` is a typed stub (AMOS_MODEL formulas) — 12 dimensions, stub for actual algorithms
- `CHANNEL_ACL_TABLE` has 16 channels × 6 dimensions = 96 precise ACL entries — the verbena differentiator

### Test Suite
- 6 test categories, 130+ individual tests:
  1. D5 Manas — Channels (21 tests): channel enum construction, union acceptance, category mapping, ALL_CHANNELS count, validation accept/reject
  2. D6 Citta — Entry State (8 tests): priority/activity/nominal/retention/cache/frame enums, default entry, filler entry
  3. Kafka Topic/Topology (16 tests): KafkaTopicConfig, KafkaPartition, KafkaBrainLogImpl, KafkaTopology
  4. Buffer Config + Helpers (14 tests): BufferConfig, generateEntryId, generateDedupKey, generateTransientKey, factories
  5. Buffer CRUD + Dedup + TTL + Eviction + Health (40 tests): add/remove/get/has/entriesList/clear, dedup hit/preserve, TTL valid/expired/zero, evict capacity/LRU/FIFO/priority/empty/count, health empty/populated/util/averages
  6. D7 Buddhi (11 tests): RoutingDecisionType, RoutingDecisionMessage, D7State, ObserverFrameType, ObserverFrame, IntentClassification, OutputType, D7GatingResult

### Synthetic Generator
- 8 orchestrator patterns: heartbeat, burst, synthesis, mixed, canonical, fork, retry, lifecycle
- Outputs JSONL by default, supports json / kafka-events / json-raw formats
- Reproducible via --seed

### Storage Locations
- Module: `cosmo-brain/AMOS_Kafka_Brain_Buffer_v1.0.ts`
- Tests: `cosmo-brain/AMOS_Kafka_Brain_Buffer_v1.0.test.ts`
- Generator: `cosmo-brain/test_kafka_brain_buffer_generator.py`
- Vault: `_00_Cosmo brain/md/2026-08-23 AMOS Kafka Brain Buffer.md`
- Memory: `Memory — AMOS Kafka Brain Buffer.md` (this file)
- Skill: `.agents/skills/amos-kafka-brain-buffer/SKILL.md`
- Workflow: `.devin/workflows/kafka-brain-buffer-build.md`

### Epistemic Labels
- SOURCE: channel taxonomy (D5 Manas), D5-D8 mapping (mapped from existing verbena concepts)
- DERIVED: D5→D6→D7→D8 flow (follows from consciousness model architecture)
- AMOS_MODEL: scoring formulas, buffer implementation, ACL table entries, flow orchestration logic

## Build Commands

```bash
cd cosmo-brain

# Type-check module
npx tsc --noEmit AMOS_Kafka_Brain_Buffer_v1.0.ts

# Run test suite
npx ts-node --transpile-only AMOS_Kafka_Brain_Buffer_v1.0.test.ts

# Generate sample events
python3 test_kafka_brain_buffer_generator.py --pattern all --output jsonl
python3 test_kafka_brain_buffer_generator.py --pattern canonical --output kafka-events
```

## Known Issues
- None blocking — all 6 test categories pass
- D8 scoring is a stub (marker for actual algorithms per dimension)
- Kafka deployment not yet wired to real Kafka (stubs only)
- ACL enforcement is typed tags only (no runtime enforcement)

## Conclusion Class
AMOS MODEL — new brain engine. Channel taxonomy and D5-D8 mapping are verbena SOURCE. Scoring formulas, buffer impl, ACL table are AMOS_MODEL. Not yet production-verified.

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[DATED_MOC]]
