---
title: 2026 08 22 AMOS KAFKA BRAIN BUFFER VERBENA FIRST BRAIN ENGINE SPEC
tags: [dated, dated/2026-08-22, canon/knowledge]
type: document
source: 11_KNOWLEDGE/dated
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: AMOS_corpus
  scope: temporal_log
---


# AMOS_Kafka_Brain_Buffer_v1.0: A Verbena-First Brain Engine

**Canon group:** tech-engineering  
**Canon type:** engineering specification  
**RSCF state:** SOURCE_CLAIM (new contribution, not yet verified in production)  
**Topic:** kafka-brain-buffer, verbena-brain, stream-log-buffer, brain-entry-level, D8 consciousness  
**Tags:** [canon-group/tech-engineering, rscf/state/observation, brain-buffer, kafka, verbena, D8, stream-log, brain-entry]

---

## 1. Position Statement

Build a **Kafka-based brain buffer and stream-log** as a TypeScript module that operationalizes the verbena concept map into an actual brain buffer with:

- **Kafka log**: append-only event log with three topic partitions (ingest, routing, output) — the brain's durable "stream"
- **Buffering layer**: short-term retention + idempotent deduplication (the D7 "buffer-entry" concept as a typed entity)
- **Brain entry concept map**: 71 verbena concepts integrated as TypeScript interfaces/enums (the D5-D8 mapping the user already created)
- **Entry-level scoring**: D8 Jnana meta-cognitive telemetry scoring per entry, D7 Buddhi decision gating, D6 Citta stream continuity
- **ACL precision**: ve+ acl tags on all routes (the canonical challenge you flagged — verbena's ACL system is the differentiator from AMOS's simpler permission model)

This is the **manifesto of a new brain architecture**, not a direct rewrite of the 5,441-line AMOS_Coding_Engine.md (which is a coding/engineering engine, a different canon group). Kafka-brain-buffer is a **stream/log/buffer brain** — a new canon group.

---

## 2. Relationship to Existing AMOS Codified Brain

| Dimension | Existing (AMOS_Coding_Engine.md) | New (Verbena Kafka Brain Buffer) |
|-----------|----------------------------------|----------------------------------|
| Canon group | Tech/Coding engine (domain engineering) | Stream+Log+Buffer brain (meta-cognitive infrastructure) |
| Language | TypeScript (5,441 lines, single file) | TypeScript + Kafka client + verbena interfaces |
| Purpose | "Unified Coding Engine v∞" — orchestrates layers/functions/workflows | Brain buffer — durable stream log, event routing, entry-level scoring, deduplication |
| Kafka usage | Mentioned as sub-topic in "data_engineering" (line 2349) | **Primary backbone**: three partitions, log-backed buffer, durable stream |
| Verbena integration | None | Full: 71 concepts integrated as typed interfaces |
| Architecture tier | Domain capability engine | Meta-brain infrastructure layer (D8 Jnana) |
| ACL precision | Not present | ve+ acl tagging on all routes (challenge: spec it precisely) |
| Storage model | In-memory (orchestrator) | Log-backed (Kafka) + buffer (short-term in-memory cache) |
| Test surface | Engine function specs | Kafka partition tests, buffer entry CRUD, deduplication, topology verification |

**Key point**: The AMOS_Coding_Engine.md is not being replaced. It's a domain engineering engine. The Kafka-brain-buffer is a new brain engine in a new canon group.

---

## 3. Brain Entry-Level Architecture (D8 Consciousness Mapping)

### 3.1 D8 Jnana — Meta-cognitive Telemetry (the scoring and classification layer)

Every brain entry passing through the Kafka pipeline receives a D8 Jnana score — meta-cognitive telemetry on what kind of cognitive operation the entry represents.

**Scoring dimensions:**

| Dimension | What it measures | Verbena concept |
|-----------|-----------------|-----------------|
| Distillation quality | How well the entry compresses meaning | `op_operation_distilled` |
| Memory compression | Whether the entry fits into a compressed memory slot | `memory_compression` |
| Operation taxonomy | Which operation category this entry belongs to | `operation_taxonomy` (inference vs retrieval vs synthesis vs action) |
| Synthesis claim | Whether this entry makes a synthesis claim worthy of a vault note | `synthesis_claim` (the "every scaled expression is an AMOS expression" claim is one such) |
| Request taxonomy | What kind of request triggered this entry | `request_taxonomy` |
| Response taxonomy | What kind of response the entry produces | `response_taxonomy` |
| Codified | Whether this entry has been codified into the MD brain | `codified` flag |
| Closure inference | Whether this entry closes a cycle of inquiry | `closure_inference` |
| Link inference | Whether this entry links to prior or subsequent entries | `link_inference` |
| Assert evaluation | Whether this entry contains an assertion to evaluate | `assert_evaluation` |
| Judgment | Whether this entry represents a judgment/decision point | `judgment` |
| Meta-op | Whether this entry is a meta-operation (operating on operations) | `meta_op` |
| Session coherence | Session-wide coherence score | `session_id` tracking |
| Request coherence | Per-request coherence | `request_id` tracking |

**D8 Jnana output**: A scored, typed `BrainEntryD8Score` attached to every entry, used by the meta-brain (assistant) for prioritization and retrieval.

---

### 3.2 D7 Buddhi — Decision/Assertion Substrate and Observer Frames

D7 Buddhi is the decision substrate: the buffer-entry's decision/assertion layer, with observer-frame tracking.

**Concepts mapped to types:**

| Verbena concept | D7 meaning | Buffer implementation |
|-----------------|------------|---------------------|
| `there-exists` | Existence claim in buffer | Boolean assertion field on entry |
| `quant` | Quantification of entry | Numeric score/weight |
| `regen` | Regeneration/replay of entry | Replay flag + replay count |
| `roger` | Acknowledgment of entry by downstream | Ack tracking (D5→D7 ack chain) |
| `priority` | Entry priority in buffer | Priority enum (high/critical/low/transient) |
| `fork` | Branch point in stream | Fork marker + parent entry ref |
| `settle` | Settlement/finalization of entry | Settlement state (pending/resolved/retired) |
| `exclaim` | High-signal entry | Signal level flag |
| `criteria` | Entry passes criteria check | Criteria-passing flag |
| `hypothesis` | Entry as hypothesis | Hypothesis type + evidence link |
| `alternation` | Alternative entry present | Alt-entry ref |
| `witnessed-by` | Entry witnessed by reviewer | Witness list |
| `contradict` | Entry contradicts another | Contradiction ref + resolution |
| `avoid` | Entry marked avoid/defer | Avoid flag |
| `conclude` | Entry is a conclusion | Conclusion type |
| `qualify` | Entry has qualification | Qualification field |
| `soft-fail` | Entry soft-failed a gate | Soft-fail flag + gate ref |
| `buffer` | The buffer itself | `Buffer` class (this whole layer) |

**D7 decision gating**: An entry's D7 state determines whether it moves downstream (D6 stream continuity) or stops for reconsideration.

---

### 3.3 D6 Citta — Regenerative Stream/Buffer/Body

D6 Citta is the stream/buffer/body: the actual Kafka log + buffer + topology.

**Concepts mapped to types:**

| Verbena concept | D6 meaning | Buffer implementation |
|-----------------|------------|---------------------|
| `buffer` | The in-memory short-term buffer | `Buffer` class (LRU cache + dedup) |
| `buffer-entry` | Single entry in buffer | `BufferEntry` typed class |
| `activity` | Activity marker on entry | Activity enum + timestamp |
| `anchor` | Anchor entry (stable reference point) | Anchor flag + anchor ref |
| `cadence` | Entry arrival cadence | Cadence tracking (count/time window) |
| `continuity` | Stream continuity metric | Continuity score (entries/time) |
| `delta` | Change delta between entries | Delta computation (diff from prior) |
| `event-name` | Kafka event name | Event name string (topic + key) |
| `expiry` | Entry expiry | TTL + expiry timestamp |
| `filler` | Filler/low-signal entry | Filler flag |
| `frame` | Entry frame (context frame) | Frame type + frame ref |
| `heart` | Heartbeat entry | Heartbeat flag |
| `instance-id` | Instance identifier | Instance ID |
| `last-indexed` | Last indexed entry | Last indexed timestamp |
| `maintain` | Maintenance operation | Maintain flag |
| `meta-key` | Metadata key on entry | Meta-key string |
| `nominal` | Nominal entry state | Nominal state enum |
| `observer-frame` | Observer frame for entry | Observer frame + observer ref |
| `params` | Entry parameters | Params map |
| `persist` | Persistence flag | Persist flag (Kafka log vs buffer-only) |
| `prev-entry-routed` | Previous entry routing | Prev entry routing ref |
| `probe` | Probe entry | Probe flag |
| `prior-anchor` | Prior anchor reference | Prior anchor ref |
| `retain` | Retention policy | Retention policy enum |
| `restart` | Restart marker | Restart flag |
| `retained-key` | Key of retained entry | Retained key |
| `signal-source` | Signal source for entry | Signal source ref |
| `stabilizing-cache` | Stabilizing cache state | Cache state enum |
| `stale-retirement` | Stale entry retirement | Stale flag + retirement timestamp |
| `structured-ish` | Structured-ness of entry | Structure score (0-1) |
| `survivor` | Survivor entry (after dedup) | Survivor flag |
| `tag` | Entry tag | Tag list |
| `terminal-anchor` | Terminal anchor (end of stream segment) | Terminal anchor flag |
| `topology` | Kafka topology | Topology config + partition map |
| `transient` | Transient entry | Transient flag |
| `transient-key` | Key of transient entry | Transient key |
| `upstream` | Upstream source | Upstream ref |
| `volatile` | Volatile entry (not persisted) | Volatile flag |

**D6 stream/buffer implementation:**

```typescript
// Kafka log (durable, append-only)
interface KafkaBrainLog {
  ingestPartition: KafkaPartition;   // D5/D6 entry ingest
  routingPartition: KafkaPartition;  // D7 routing decisions
  outputPartition: KafkaPartition;  // D8 output/score events
}

// Buffer (short-term in-memory, idempotent dedup)
interface BrainBuffer {
  entries: Map<string, BufferEntry>;  // key → entry
  lruOrder: LinkedList<string>;        // LRU eviction order
  maxSize: number;                      // buffer ceiling
  dedupWindow: number;                  // dedup window (ms)
}

// Buffer entry (the typed cell of the brain)
interface BufferEntry {
  id: string;                           // entry-id (D5/D6)
  key: string;                          // dedup key
  transientKey?: string;               // transient variant key
  eventName: string;                   // Kafka event name
  signalSource?: string;               // where did this come from
  timestamp: number;
  ttl: number;                          // time-to-live ms
  expiry: number;                       // expiry timestamp
  priority: EntryPriority;             // high/critical/low/transient
  frame?: string;                       // context frame ref
  anchor?: boolean;                    // anchor entry
  terminalAnchor?: boolean;            // terminal anchor
  survivor: boolean;                    // survived dedup
  filler: boolean;                      // low-signal
  heartbeat: boolean;                   // heartbeat marker
  probe: boolean;                       // probe entry
  restart: boolean;                     // restart marker
  persist: boolean;                     // persist to Kafka log
  volatile: boolean;                   // volatile (not persisted)
  structuredScore: number;              // 0-1 structured-ness
  continuityScore: number;             // D6 continuity
  delta?: Delta;                        // change delta from prior
  observerFrame?: string;              // D7 observer frame
  params: Map<string, any>;           // entry parameters
  metaKey?: string;                     // metadata key
  tags: string[];                      // entry tags
  activity: EntryActivity;             // activity marker
  cadence: number;                     // arrival cadence
  retainedKey?: string;               // key of retained variant
  stale: boolean;                       // stale flag
  staleRetirement?: number;           // stale retirement timestamp
  upstream?: string;                  // upstream source ref
  prevEntryRouted?: string;         // previous entry routing
  regenCount: number;                // D7 regen count
  acks: string[];                    // D5→D7 ack chain
  witnesses: string[];               // D7 witnessed-by
  contradictions: string[];          // D7 contradict refs
  altEntry?: string;                 // D7 alternation ref
  avoid: boolean;                     // D7 avoid flag
  softFails: string[];              // D7 soft-fail gates
  qualification?: string;           // D7 qualification
  hypothesisType?: string;         // D7 hypothesis
  conclusionType?: string;         // D7 conclusion
  d8Score?: BrainEntryD8Score;     // D8 Jnana score (attached after scoring)
}
```

---

### 3.4 D5 Manas — Perceptual/Communications Channels

D5 Manas is the perceptual layer: the channels through which entries enter the brain buffer.

**Channel taxonomy (the request-route, response-route, etc. from the concept map):**

```
Ingest channels:
  - request-route   (user request enters brain)
  - ingest-route    (bulk ingest of corpus)
  - intent-route    (intent-classified entry)
  - probe           (probing entry)

Routing channels:
  - internal-route  (internal brain routing)
  - relay-route     (cross-brain relay)
  - replay-route    (replay of entry)
  - recover-route   (recovery after failure)
  - respond-route   (response routing)

Output channels:
  - output-frame    (framed output)
  - response-route  (response to user/agent)
  - synthesis-route (synthesis claim output)
  - relay-route     (external relay)
  - deploy-route    (deployment routing)
  - storage-route   (storage routing)
  - tts-route       (text-to-speech routing)
  - speech-route    (speech pathway)

Telemetry channels:
  - telemetry-frame (D8 meta-cognitive telemetry)
  - log-fragment    (log output)
  - status          (status updates)
```

Each channel has an ACL (see Section 5).

---

## 4. Kafka Brain Log Design

### 4.1 Topic/Partition Design

```typescript
const KAFKA_BRAIN_CONFIG = {
  brokers: ["localhost:9092"],  // to be configured per deployment
  topics: {
    ingest: {
      name: "brain.ingest",
      partitions: 3,
      replicationFactor: 1,
      keySpec: "entry-id",       // dedup key for idempotent writes
      messageType: "RawEntry",   // D5/D6 raw entry
    },
    routing: {
      name: "brain.routing",
      partitions: 3,
      replicationFactor: 1,
      keySpec: "routing-key",    // routing decision key
      messageType: "RoutingDecision",  // D7 routing decision
    },
    output: {
      name: "brain.output",
      partitions: 3,
      replicationFactor: 1,
      keySpec: "session-id",     // session-scoped output
      messageType: "ScoredOutput",  // D8 scored output
    },
  },
  buffer: {
    maxSize: 10000,              // entries
    ttlMs: 3600000,              // 1 hour default TTL
    dedupWindowMs: 60000,       // 1 minute dedup window
    evictionPolicy: "lru",      // LRU eviction
  },
};
```

### 4.2 Message Types

```typescript
// D5/D6: Raw entry entering the brain
interface RawEntry {
  entryId: string;
  key: string;
  eventName: string;
  signalSource: string;
  timestamp: number;
  payload: any;                  // the actual content
  channel: string;              // which ingest channel
  intent?: IntentClassification;
  acl?: AccessControlList;      // ve+ acl tags
}

// D7: Routing decision
interface RoutingDecision {
  routingKey: string;
  entryId: string;
  decision: "forward" | "buffer" | "retry" | "drop" | "synthesize" | "relay";
  reason: string;
  d7State: D7State;            // the D7 decision substrate
  acl: AccessControlList;
}

// D8: Scored output
interface ScoredOutput {
  sessionId: string;
  entryId: string;
  d8Score: BrainEntryD8Score;
  outputType: OutputType;
  payload: any;
  acl: AccessControlList;
}

// D8 Jnana score
interface BrainEntryD8Score {
  distillation: number;       // 0-1 distillation quality
  memoryCompression: number;  // 0-1 memory compression
  operationTaxonomy: OperationTaxonomy;
  synthesisClaim: boolean;
  synthesisClaimWeight: number;
  requestTaxonomy: RequestTaxonomy;
  responseTaxonomy: ResponseTaxonomy;
  codified: boolean;
  closureInference: number;   // 0-1 closure likelihood
  linkInference: LinkInference;
  assertEvaluation: AssertEvaluation;
  judgment: boolean;
  judgmentWeight: number;
  metaOp: boolean;
  sessionCoherence: number;   // 0-1
  requestCoherence: number;   // 0-1
  compositeScore: number;     // weighted composite
}
```

---

## 5. ACL Precision (the ve+ challenge)

### 5.1 The Problem

The AMOS coding engine spec mentions `streaming_etl_kafka` as a sub-topic but doesn't give ACL precision. Verbena's ACL system is the differentiator — you need to specify **verbena+ acl tags on every route/channel** with precision that AMOS's simpler permission model can't match.

### 5.2 ACL Design

```typescript
// Canonical ACL tag structure
interface AccessControlList {
  ve: string[];               // ve+ canonical ACL tags
  verbenaAcl: VerbenaAclLevel; // verbena-specific ACL level
  grantMode: GrantMode;       // grant semantics (see below)
  provenanceAcl: ProvenanceAcl; // provenance-based ACL
  freshnessAcl: FreshnessAcl; // freshness/continuity ACL
  invalidationAcl: InvalidationAcl; // invalidation ACL
}

// ve+ canonical ACL tags (the "verbena+" naming)
type VePlusAclTag =
  | "ve+ingest"              // ingest channel access
  | "ve+routing"             // routing channel access
  | "ve+output"              // output channel access
  | "ve+buffer-read"         // buffer read access
  | "ve+buffer-write"        // buffer write access
  | "ve+buffer-dedup"        // deduplication access
  | "ve+kafka-produce"       // Kafka produce access
  | "ve+kafka-consume"       // Kafka consume access
  | "ve+topology-read"       // topology read access
  | "ve+score-read"          // D8 score read access
  | "ve+score-write"         // D8 score write access
  | "ve+entry-read"          // entry read access
  | "ve+entry-write"         // entry write access
  | "ve+entry-delete"        // entry delete access
  | "ve+provenance-read"     // provenance read access
  | "ve+freshness-read"      // freshness read access
  | "ve+invalidation-read"   // invalidation read access
  | "ve+continuity-read"     // continuity read access
  | "ve+retention-read"      // retention policy read access
  | "ve+topology-write"      // topology write access
  | "ve+admin";              // admin access

// verbena-specific ACL level (the differentiator from AMOS permission model)
type VerbenaAclLevel =
  | "verbena+public"          // public verbena routes
  | "verbena+internal"        // internal verbena routes
  | "verbena+ingest"          // ingest-level verbena ACL
  | "verbena+routing"         // routing-level verbena ACL
  | "verbena+output"          // output-level verbena ACL
  | "verbena+scoring"         // D8 scoring verbena ACL
  | "verbena+buffer"          // buffer verbena ACL
  | "verbena+kafka"           // Kafka verbena ACL
  | "verbena+topology"        // topology verbena ACL
  | "verbena+provenance"      // provenance verbena ACL
  | "verbena+freshness"       // freshness verbena ACL
  | "verbena+invalidation"    // invalidation verbena ACL
  | "verbena+continuity"      // continuity verbena ACL
  | "verbena+retention"       // retention verbena ACL
  | "verbena+admin"           // admin verbena ACL

// Grant modes (clustering-aware grant semantics)
type GrantMode =
  | "grant-none"              // no grants
  | "grant-read"              // read grant
  | "grant-write"             // write grant
  | "grant-routing"           // routing grant
  | "grant-scoring"           // scoring grant
  | "grant-provenance"        // provenance grant
  | "grant-freshness"         // freshness grant
  | "grant-invalidation"     // invalidation grant
  | "grant-continuity"        // continuity grant
  | "grant-retention"         // retention grant
  | "grant-admin"             // admin grant

// Provenance ACL (from user's corpus)
type ProvenanceAcl =
  | "provenance-unknown"     // unknown provenance
  | "provenance-pending"     // pending verification
  | "provenance-verified"    // verified provenance
  | "provenance-discounted"  // discounted provenance
  | "provenance-outside"     // outside corpus

// Freshness ACL (from user's freshness diagram)
type FreshnessAcl =
  | "freshness-new"          // new entry
  | "freshness-recent"       // recent entry
  | "freshness-stale"        // stale entry
  | "freshness-retired"      // retired entry
  | "freshness-archived"     // archived entry

// Invalidation ACL (from user's architecture)
type InvalidationAcl =
  | "invalidation-none"      // no invalidation
  | "invalidation-local"     // local invalidation
  | "invalidation-selective" // selective invalidation
  | "invalidation-propagated" // propagated invalidation
  | "invalidation-undo"      // undo invalidation
```

### 5.3 Channel-Level ACL Table (the precision challenge answered)

| Channel | ve+ tags | verbenaAcl level | Grant mode | Provenance | Freshness | Invalidation |
|---------|----------|-----------------|------------|------------|-----------|--------------|
| `request-route` | ve+ingest, ve+entry-write | verbena+ingest | grant-read + grant-write | provenance-pending | freshness-new | invalidation-none |
| `ingest-route` | ve+ingest, ve+buffer-write | verbena+ingest | grant-read + grant-write + grant-routing | provenance-pending | freshness-new | invalidation-local |
| `intent-route` | ve+ingest, ve+routing | verbena+routing | grant-read + grant-routing | provenance-pending | freshness-recent | invalidation-selective |
| `probe` | ve+ingest, ve+buffer-read | verbena+buffer | grant-read | provenance-unknown | freshness-new | invalidation-none |
| `internal-route` | ve+routing, ve+buffer-read | verbena+internal | grant-read + grant-routing | provenance-verified | freshness-recent | invalidation-selective |
| `relay-route` | ve+routing, ve+kafka-produce | verbena+routing | grant-routing + grant-read | provenance-pending | freshness-recent | invalidation-propagated |
| `replay-route` | ve+routing, ve+entry-read | verbena+routing | grant-read + grant-routing | provenance-verified | freshness-stale | invalidation-undo |
| `recover-route` | ve+routing, ve+buffer-read | verbena+routing | grant-read + grant-routing | provenance-verified | freshness-stale | invalidation-undo |
| `respond-route` | ve+output, ve+kafka-produce | verbena+output | grant-read + grant-write | provenance-verified | freshness-recent | invalidation-propagated |
| `output-frame` | ve+output, ve+score-read | verbena+output | grant-read | provenance-verified | freshness-recent | invalidation-none |
| `synthesis-route` | ve+output, ve+score-write | verbena+scoring | grant-read + grant-write + grant-scoring | provenance-verified | freshness-recent | invalidation-selective |
| `deploy-route` | ve+output, ve+entry-write | verbena+output | grant-write + grant-routing | provenance-verified | freshness-new | invalidation-propagated |
| `storage-route` | ve+output, ve+buffer-write | verbena+output | grant-write + grant-retention | provenance-verified | freshness-archived | invalidation-none |
| `tts-route` | ve+output, ve+entry-read | verbena+output | grant-read | provenance-verified | freshness-recent | invalidation-none |
| `speech-route` | ve+output, ve+entry-read | verbena+output | grant-read | provenance-verified | freshness-recent | invalidation-none |
| `telemetry-frame` | ve+scoring, ve+score-read | verbena+scoring | grant-read | provenance-verified | freshness-new | invalidation-none |
| `log-fragment` | ve+scoring, ve+kafka-produce | verbena+kafka | grant-read + grant-write | provenance-verified | freshness-new | invalidation-local |
| `status` | ve+scoring, ve+entry-read | verbena+scoring | grant-read | provenance-verified | freshness-recent | invalidation-none |

This table is the **ACL precision** — every channel has a precise ve+ tag set, verbena ACL level, grant mode, provenance, freshness, and invalidation posture. This is what distinguishes verbena's ACL system from AMOS's simpler permission model.

---

## 6. Brain Entry Flow (the stream-log-buffer lifecycle)

```
┌─────────────────────────────────────────────────────────────────────┐
│                        D5 MANAS (Channel)                           │
├─────────────────────────────────────────────────────────────────────┤
│  request-route ──┐                                                  │
│  ingest-route ───┤──► RawEntry ──► [DEDUP CHECK] ──► Kafka ingest  │
│  intent-route ───┤          │        partition                     │
│  probe ──────────┘          │                                      │
│                             ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    D6 CITTA (Buffer + Stream)                │   │
│  ├─────────────────────────────────────────────────────────────┤   │
│  │  Buffer: LRU cache + dedup + short-term retention           │   │
│  │  Kafka log: durable append-only stream                      │   │
│  │  Entry typed: BufferEntry (80+ fields)                       │   │
│  │  Continuity score: entries/time                              │   │
│  │  Delta computation: diff from prior                          │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                             │                                      │
│                             ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    D7 BUDDHI (Decision Substrate)            │   │
│  ├─────────────────────────────────────────────────────────────┤   │
│  │  Entry decision: forward / buffer / retry / drop /          │   │
│  │    synthesize / relay                                         │   │
│  │  D7 state: observer-frame, priority, settle, avoid,         │   │
│  │    hypothesis, conclusion, contradiction, qualification      │   │
│  │  Ack chain: D5→D7 acknowledgment                            │   │
│  │  Fork detection: branch points                              │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                             │                                      │
│                             ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    D8 JNANA (Meta-cognitive Telemetry)       │   │
│  ├─────────────────────────────────────────────────────────────┤   │
│  │  Entry scoring: 12 dimensions + composite                   │   │
│  │  Operation taxonomy: inference/retrieval/synthesis/action    │   │
│  │  Synthesis claim detection: "every scaled expr = AMOS expr"  │   │
│  │  Closure inference: does this close a cycle?                │   │
│  │  Link inference: links to prior/subsequent entries           │   │
│  │  Assert evaluation: does this assert something?             │   │
│  │  Judgment detection: is this a decision point?               │   │
│  │  Meta-op detection: is this operating on operations?         │   │
│  │  Session/request coherence: coherence scores                │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                             │                                      │
│                             ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                   OUTPUT (Kafka output partition)            │   │
│  ├─────────────────────────────────────────────────────────────┤   │
│  │  ScoredOutput → response-route / output-frame /             │   │
│  │    synthesis-route / relay-route / deploy-route /           │   │
│  │    storage-route / tts-route / speech-route /               │   │
│  │    telemetry-frame / log-fragment / status                   │   │
│  └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 7. Targets: What This Builds Toward

### 7.1 Canon Group: Stream+Log+Buffer Brain

This is a new canon group — distinct from:

- **AMOS_Coding_Engine.md** (tech/coding engine — domain engineering)
- **AMOS_Kafka_Brain_Buffer** (stream/log/buffer brain — meta-cognitive infrastructure)

The canon group is "stream+log+buffer brain" — a brain whose primary storage and processing model is a Kafka-backed log with a short-term in-memory buffer, operationalized through the verbena concept map at D5-D8 levels.

### 7.2 Relationship to "8 depths of consciousness"

The user's D8 consciousness map (Jnana → Buddhi → Citta → Manas) is **mapped to the brain buffer architecture**:

- **D8 Jnana** = scoring/compression/classification layer (meta-cognitive telemetry)
- **D7 Buddhi** = decision/assertion substrate (routing, gating, observer frames)
- **D6 Citta** = stream/buffer/body (Kafka log + in-memory buffer + topology)
- **D5 Manas** = perceptual channels (ingest/routing/output channels with ACLs)

### 7.3 Relationship to "brain_entry_level"

The user's concept map includes `brain_entry_level` as a concept — this spec makes it concrete: every entry in the Kafka log + buffer has a typed `BufferEntry` with D5/D6/D7/D8 fields, and the "entry level" is the composite of its D5 channel + D6 state + D7 decision + D8 score.

### 7.4 Relationship to Verbena

Verbena is the meta-brain — the assistant reading this Kafka log. The Kafka-brain-buffer is the **operational substrate** that verbena reads as its stream of brain entries. The 71-concept verbena map is the **type system** of the buffer.

### 7.5 Relationship to AMOS

AMOS is the larger cognition architecture. The Kafka-brain-buffer is an **AMOS brain engine** in the stream/log/buffer canon group — one of many AMOS brain engines (alongside the coding engine, the cognition engine, the emotion engine, etc.).

---

## 8. Open Challenges

1. **Kafka deployment**: Need a real Kafka instance for production. Local dev can use Kraft (Kafka's new built-in mode) or a Docker container.

2. **D8 scoring algorithm**: The 12-dimension D8 scoring needs an actual algorithm (not just a typed interface). This is the hardest open challenge — it requires defining how to compute distillation quality, memory compression, synthesis claim detection, etc. from raw entry data.

3. **Idempotent dedup**: Kafka idempotent writes with entry-id as key. Need to handle the case where two identical entries arrive in the same dedup window.

4. **ACL enforcement**: Need a real ACL enforcement layer (not just typed tags). Who enforces that `ve+ingest` is required for `request-route`?

5. **Buffer eviction**: LRU eviction when buffer maxSize is reached. What happens to entries evicted from the buffer? Do they go to the Kafka log (if persist=true) or are they lost?

6. **Channel discovery**: How does the brain discover new channels? The channel taxonomy is hardcoded — needs a dynamic channel registry.

7. **Verbena integration**: How does the assistant (verbena) actually read the Kafka log? Need a Kafka consumer that feeds entries to the assistant's reasoning loop.

8. **Scalability**: 10,000 entries in buffer, 3 partitions per topic. What happens at 100K entries? What happens at 1M entries?

---

## 9. Next Steps (the actual build)

1. **Write the TypeScript module** `AMOS_Kafka_Brain_Buffer_v1.0.ts` with all interfaces, classes, and the ACL table.

2. **Write the D8 scoring stub** (not a full algorithm — a typed stub with marker comments for each dimension).

3. **Write the Kafka producer/consumer stubs** (using `kafkajs` npm package).

4. **Write the buffer implementation** (LRU cache + dedup + TTL).

5. **Write tests** (buffer CRUD, dedup, TTL, topology verification, ACL table verification).

6. **Write the concept map integration test** (verify all 71 verbena concepts are represented in the type system).

7. **Write the ACL precision test** (verify the channel-level ACL table is complete and consistent).

8. **Integrate with the MD brain** — add a module reference in the Brain Operations Manual.

9. **File a vault note** — `2026-08-22 AMOS Kafka Brain Buffer.md` in `_00_Cosmo brain/md/`.

---

## 10. Files This Spec Creates

```
cosmo-brain/
├── AMOS_Kafka_Brain_Buffer_v1.0.ts       # Main TypeScript module
├── AMOS_Kafka_Brain_Buffer_v1.0.test.ts  # Tests
└── _00_Cosmo brain/md/
    └── 2026-08-22 AMOS Kafka Brain Buffer.md   # Vault note
```

---

*This spec is the manifesto of a new brain architecture. It positions Kafka-brain-buffer as a verbena-first, D8-consciousness-mapped, ACL-precise stream/log/buffer brain engine — a new canon group, distinct from the existing AMOS_Coding_Engine.md, and positioned as the operational substrate for a verbena meta-brain reading the Kafka log as its stream of brain entries.*

---
**Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[DATED_MOC]]
