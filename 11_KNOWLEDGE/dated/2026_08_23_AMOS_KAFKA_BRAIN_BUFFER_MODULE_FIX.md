---
title: "AMOS Kafka Brain Buffer — Module Fix Progress (Updated)"
created: "2026-08-23"
origin: "Hermes ↔ Cosmo Brain"
origin_architect: "Trang Phan"
type: note
source: 11_KNOWLEDGE/dated
tags: [cosmo, amos, canon-group/tech-ai, rscf/claim, rscf/state/observation, topic/kafka-brain-buffer, topic/typescript, topic/bugfix, dated, dated/2026-08-23, canon/knowledge]
status: "complete"
provenance: "OBSERVATION"
confidence: "HIGH"
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: temporal_log
---


# AMOS Kafka Brain Buffer — Module Fix Progress (Updated)

> Epistemic class: OBSERVATION
> Conclusion label: `HIGH` — Fixed duplicate exports, added missing exports/classes/functions.
> Test results: 180/180 pass (was 0/180).
> Governing law: `integrity > completeness > fluency > speed > token savings`.

## What was done

Fixed the `AMOS_Kafka_Brain_Buffer_v1.0.ts` module so it loads and runs with
the test file `AMOS_Kafka_Brain_Buffer_v1.0.test.ts`. Progress: 0 → 180 passing.

## Fixes Applied (cumulative)

### Module fixes
1. **Duplicate export block removed** — 100-line re-export caused esbuild errors
2. **Concept registry added** — 71 concepts (16 D5 + 31 D6 + 17 D7 + 7 D8) with `tsRepresentation`
3. **ACL constant arrays added** — `ALL_VE_PLUS_TAGS`, `ALL_VERBENA_ACL_LEVELS`, etc.
4. **`BufferConfig`** — converted to class with `defaultConfig()`, `custom()`, `persistOnEvict`
5. **`KafkaTopology`** — rewritten to match test API: `KafkaTopology(brainId, topics[], partitionCount, broker)`
6. **`KafkaPartition`** — converted to class with `key()`, `assignEntry()`
7. **`KafkaTopicConfig`** — converted to class with `key()`, `isValid()`
8. **`RoutingDecisionType`** — converted from type alias to const object for runtime access
9. **`FrameType.INGEST`** — added (was `RAW`)
10. **`channelCategory`** — fixed deploy channels returning "output" instead of "deploy"
11. **`TELEMETRY_CHANNELS`** — removed "status" (test says it's not telemetry)
12. **`createUserRequestEntry`** — priority HIGH (was CRITICAL)
13. **`generateTransientKey`** — accepts `(priority, ttl)` or `(entry)` overload
14. **`BufferHealth`** — empty buffer returns COLD (was DRY)
15. **`getEntriesByPriority`** — added to `InMemoryBrainBuffer`
16. **`toDebug()`** — added to `RoutingDecisionMessage` and `ObserverFrame`
17. **`conceptsByDLevel`** — returns `VerbenaConcept[]` with `tsRepresentation` (was `string[]`)
18. **`allConceptNames`** — returns both lowercase and uppercase names

### New classes/functions added
- `makeEntry(key, opts?)` — creates BufferEntry with defaults
- `makeEntryWithPriority(key, priority)` — creates entry with specific priority
- `isValidBrainRoute/Ingest/Routing/Output/Deploy/TelemetryChannel()` — validation functions
- `INGEST_CHANNELS`, `ROUTING_CHANNELS`, `OUTPUT_CHANNELS`, `DEPLOY_CHANNELS`, `TELEMETRY_CHANNELS` — channel arrays
- `D6Buffer` — thin wrapper around InMemoryBrainBuffer
- `D6delta` — delta tracking with `fromPrior()` static method
- `IngestRoute`, `OutputRoute`, `RequestRoute`, `SynthesisRoute` — route classes with `toTopic()`
- `KafkaBrainLogImpl` — Kafka log with `produce()`, `consume()`, `setLog()`, `getLog()`
- `D7State`, `RoutingDecisionMessage`, `ObserverFrame` — class stubs with constructors

### Test file fixes
- Added missing imports: `makeEntry`, `makeEntryWithPriority`, `D6Buffer`, `D6delta`, route classes, `KafkaProducerStub`, `KafkaConsumerStub`
- Fixed `assertEqual` to use JSON comparison for objects (was using `!==`)

## Current Test Results

| Metric | Before | After |
|--------|--------|-------|
| Module loads | No | Yes |
| Tests passing | 0/180 | 180/180 |
| Tests failing | 180/180 | 0/180 |
| Compilation errors | 35 | 0 |

## All Issues Resolved

All 180 tests pass. The 29 remaining issues from the 151/180 milestone were resolved:

### Buffer implementation (8 fixes)
- `add()` returns existing entry on dedup hit (not null) — enables `wasDedupHit` detection
- `get()` calls `moveToFront()` for LRU ordering
- `health()` empty buffer: `size === 0 || staleCount < size * 0.5` for healthy=true
- `makeEntry` default priority changed to `EntryPriority.LOW`
- Added `persistOnEvict` constructor parameter

### Flow processing (8 fixes)
- `ingest()` and `process()` changed from async to sync
- `KafkaProducerStub.produce()` changed to sync with topic validation
- `KafkaConsumerStub.consume()` changed to sync with topic validation
- D7 output mapping: FORWARD→RESPONSE, DROP→STATUS, BUFFER→NO_RESPONSE
- `RoutingDecisionMessage` uses constructor (not object literal)

### Other (13 fixes)
- `RoutingDecisionType` string literals → enum values in all switch cases
- `toDebug()` uses enum key name (FORWARD) not value (forward)
- `ve+scoring` added to `ALL_VE_PLUS_TAGS` (22 total)
- `grantMode` changed from `GrantMode` to `GrantMode[]` array
- `request-route` grantMode includes both `grant-read` and `grant-write`
- `BUFFER` concept renamed from lowercase to uppercase
- `allConceptNames()` returns `c.name` only (71, not 142)
- `tsRepresentation` field added to all 71 concepts
- `IngestRoute.process()` method added
- `BufferEntry.interpolate()` method added for delta computation
- `KafkaBrainLogImpl.kafkaConfig` includes `brokers` array
- `KafkaBrainLogImpl.getLog()` returns all entries for valid topic
- `KafkaProducerStub.getOffset()` method added

## Key Lessons

1. **ESM type erasure**: Interfaces and type aliases are erased at runtime by esbuild.
   Tests that import them as values need runtime stubs or the types must be converted
   to classes/const objects.

2. **Test-driven API discovery**: The test file defines the expected API. When the
   module doesn't match, the tests reveal exactly what's missing.

3. **assertEqual for objects**: Using `!==` for object comparison always fails because
   objects are different references. Use `JSON.stringify` comparison as fallback.

4. **Constructor signature matching**: The test's constructor arguments must match
   the class constructor parameters exactly — both order and types matter.

5. **Enum vs string union**: When tests check `Object.keys(Enum)` or use enum names
   in debug output, const enums or string unions don't work — use proper TS enums.

6. **Sync vs async**: Test runners that call methods without `await` require sync
   methods. `await` on a non-Promise value returns the value, but `async` methods
   return Promises that may not resolve in sync test contexts.

7. **ACL array fields**: When tests use `.includes()` on a field, the field must be
   an array, not a single value. Check test assertions carefully for array vs scalar.

## Links

- [[00_COSMO_BRAIN_MOC]]
- 2026-08-23 AMOS Kafka Brain Buffer
- 2026-08-23 Memory — AMOS Kafka Brain Buffer

---
**MOC:** [[DATED_MOC]]
