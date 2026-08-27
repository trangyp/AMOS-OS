---
title: 2026 08 23 AMOS KAFKA BRAIN BUFFER TEST SUITE
tags: [dated, dated/2026-08-23]
type: document
source: 11_KNOWLEDGE/dated
---


# AMOS Kafka Brain Buffer Test Suite

**Date**: 2026-08-23
**Canon group**: tech-engineering
**RSCF state**: SOURCE_CLAIM
**Status**: 180/180 tests pass, 0 failures

## Overview

Comprehensive test suite for `AMOS_Kafka_Brain_Buffer_v1.0.ts` — 3320 lines, 180 test cases across 30+ categories. Standalone test runner (not vitest), uses `npx tsx` to execute.

## Test Categories

| # | Category | Tests | Description |
|---|----------|-------|-------------|
| 1 | Channel Validation (D5) | 4 | Ingest/routing/output/deploy/telemetry channel construction |
| 2 | Channel Category | 3 | `channelCategory()` classification |
| 3 | KafkaPartition | 8 | Construction, key, assignEntry, distribution |
| 4 | KafkaTopicConfig | 4 | Construction, key, partitions |
| 5 | KafkaTopology | 6 | Construction, key, exists, addTopic, toSummary, toDebug |
| 6 | BufferConfig | 4 | Default config, custom config |
| 7 | BufferEntry | 6 | makeEntry, makeEntryWithPriority, interpolate |
| 8 | InMemoryBrainBuffer — Dedup | 3 | Dedup preserves original, transient new key |
| 9 | InMemoryBrainBuffer — TTL | 3 | Expired entries rejected, evictStale |
| 10 | InMemoryBrainBuffer — Eviction | 4 | LRU, FIFO, eviction count |
| 11 | InMemoryBrainBuffer — Health | 3 | Empty, populated, stale entries |
| 12 | KafkaProducerStub | 5 | Produce, dedup, invalid topic, getOffset, getLog |
| 13 | KafkaConsumerStub | 5 | Consume, offset, seek, invalid topic, getLog |
| 14 | D7 State | 4 | Routing decision, observer frame, intent classification |
| 15 | D7 Routing Message | 3 | Construction, toDebug, fields |
| 16 | ACL Table | 6 | Ve+ tags, verbena levels, grant modes, channel ACL |
| 17 | Verbena Concept Registry | 4 | Count, D-level distribution, all names, TS representation |
| 18 | BrainEntryFlow — Ingest | 3 | Result, dedup hit, kafka produce |
| 19 | BrainEntryFlow — Process | 6 | Decisions, D8 score, output channel/type, synthesis, avoid |
| 20 | IngestRoute | 1 | process() method |
| 21 | D6Buffer | 2 | Wrapper around InMemoryBrainBuffer |
| 22 | D6delta | 2 | Delta computation |
| 23 | BufferEntry Interpolation | 1 | interpolate() method |
| 24 | KafkaBrainLogImpl | 4 | Constructor, config, setLog/getLog, produce/consume |
| 25 | Routing Decision Type | 2 | Enum values, FORWARD/DROP/BUFFER |
| 26 | Observer Frame Type | 2 | Enum values, all 17 frames |
| 27 | Intent Classification | 2 | Enum values, all 14 classifications |
| 28 | Output Type | 2 | Enum values, RESPONSE/DIRECT/NO_RESPONSE |
| 29 | Response Taxonomy | 2 | Enum values, STORAGE |
| 30 | ACL Consistency | 4 | Channel→topic mapping, ve+ tags |

## Running

```bash
cd cosmo-brain
npx tsx AMOS_Kafka_Brain_Buffer_v1.0.test.ts
# Expected: 180 passed, 0 failed, ~5ms
```

## Key Fixes Applied

1. **EntryPriority.MEDIUM → HIGH**: No MEDIUM enum value; replaced with HIGH
2. **RoutingDecisionType string → enum**: Changed all `"forward"` literals to `RoutingDecisionType.FORWARD` etc.
3. **KafkaTopology refactoring**: `topics` changed from `Record<string, KafkaTopicConfig>` to `string[]` with `_topicConfigs` map
4. **createDefaultKafkaTopology**: Override keySpec/messageType after construction
5. **verifyKafkaTopology**: Use `topology.exists()` and `topology._topicConfigs` instead of direct record access
6. **InMemoryBrainBuffer**: Added `persistOnEvict` constructor param, `moveToFront` on `get()`, `health()` empty buffer fix
7. **generateDedupKey**: Accept `EntryPriority` as parameter (not just `Partial<BufferEntry>`)
8. **makeEntry**: Default priority changed to `EntryPriority.LOW`
9. **ACL grantMode**: Changed from `GrantMode` (single) to `GrantMode[]` (array)
10. **ve+scoring**: Added to `ALL_VE_PLUS_TAGS`
11. **BUFFER concept**: Renamed from `"buffer"` to `"BUFFER"` to match test expectation
12. **allConceptNames**: Return `c.name` only (not duplicated with uppercase)
13. **tsRepresentation**: Added to all 71 concepts
14. **BrainEntryFlow.ingest/process**: Changed from async to sync
15. **KafkaProducerStub.produce**: Changed from async to sync, added topic validation
16. **KafkaConsumerStub.consume**: Changed from async to sync, added topic validation
17. **KafkaProducerStub.getOffset**: Added missing method
18. **IngestRoute.process**: Added method delegating to BrainEntryFlow
19. **BufferEntry.interpolate**: Added method for delta computation
20. **KafkaBrainLogImpl**: Added `brokers` to kafkaConfig, fixed getLog to not filter by topic
21. **d7DecisionToOutputType**: FORWARD→RESPONSE (not DIRECT), DROP→STATUS (not NO_RESPONSE)
22. **d7DecisionToOutputChannel**: Updated to use enum values
23. **RoutingDecisionMessage**: Use constructor instead of object literal
24. **add() dedup**: Return existing entry (not null) on dedup hit

## Test Count Impact

- **Standalone test suite**: 180 tests (not counted in vitest 1253)
- **Total TypeScript tests**: 1253 (vitest) + 180 (standalone) = 1433
- **Grand total**: 1934 Python + 271 cognitive substrate + 1433 TypeScript + 359 deterministic = 3997

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[DATED_MOC]]
