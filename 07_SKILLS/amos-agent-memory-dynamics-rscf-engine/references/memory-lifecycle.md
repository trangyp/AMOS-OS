# AMOS Memory Lifecycle Reference

## State model

`ACTIVE -> QUARANTINED | EXPIRED | TOMBSTONED`

A revision creates a new `ACTIVE` version and marks the predecessor `SUPERSEDED`.

Historical content remains addressable for forensics and lineage.

## Time model

Track two independent clocks:
- `valid_from` / `valid_to`: when the remembered fact/event applies in the represented world.
- `recorded_at`: when AMOS stored that memory version.

This is a bi-temporal boundary. Do not substitute ingestion time for event-valid time.

## Provenance of imported mechanisms

Mechanisms were adapted, not vendored.

- Letta Code `85cb7ed50a69cdc6ae7084abc9e9ec271d43b215`: Git-tracked context/memory files, explicit long-horizon memory editing, and owner-sensitive recovery patterns.
- Mem0 `c7ee362aff94a369af70f13f2b4f853f6793ff4c`: explicit add/get/search/update/delete/history memory lifecycle APIs.
- Graphiti `c035afb7990b6077331a81e98b04efcfd9bf8184`: episodic graph memory with `valid_at` / `invalid_at` temporal boundaries and ingestion/event-time separation.

Repository/project descriptions remain `SOURCE_CLAIM`. AMOS adopts only mechanisms tested in its own runtime.

## Scope boundary

The executable reference is local SQLite semantics. It does not establish:
- distributed consistency;
- embedding/vector quality;
- graph extraction correctness;
- memory truthfulness;
- production latency;
- cross-tenant authorization correctness;
- privacy/compliance sufficiency;
- automatic knowledge promotion.

These remain `UNKNOWN/GAP` until separately evidenced.
