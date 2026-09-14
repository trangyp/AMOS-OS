"""Executable local AMOS memory lifecycle reference.

Origin architect / steward: Trang Phan.

AMOS_MODEL / local SQLite reference. Memory records remain OBSERVATION objects;
retrieval does not promote them to knowledge, current state, or action authority.
The event ledger is append-only and hash chained. Revision creates a new version;
historical content remains addressable for authorized forensic retrieval.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from hashlib import sha256
import json
import sqlite3
from typing import Optional, Protocol, Tuple


class AuthorityLike(Protocol):
    witness_id: str
    scope: Tuple[str, ...]
    state_version: str
    fresh: bool


class MemoryState(Enum):
    ACTIVE = "ACTIVE"
    QUARANTINED = "QUARANTINED"
    SUPERSEDED = "SUPERSEDED"
    EXPIRED = "EXPIRED"
    TOMBSTONED = "TOMBSTONED"


class MemoryOperationError(RuntimeError):
    pass


@dataclass(frozen=True)
class MemoryRecord:
    memory_id: str
    version: int
    origin_id: str
    scope: str
    state: MemoryState
    content: str
    content_hash: str
    valid_from: str
    valid_to: Optional[str]
    recorded_at: str
    predecessor_version: Optional[int]
    provenance_ids: Tuple[str, ...]
    epistemic_class: str = "OBSERVATION"

    def context_eligible(self, at_time: str) -> bool:
        t = _parse_time(at_time)
        start = _parse_time(self.valid_from)
        end = _parse_time(self.valid_to) if self.valid_to else None
        return self.state is MemoryState.ACTIVE and t >= start and (end is None or t < end)


def _parse_time(value: str) -> datetime:
    if not isinstance(value, str) or not value.strip():
        raise ValueError("time must be non-empty ISO-8601 string")
    try:
        parsed = datetime.fromisoformat(value)
    except ValueError as exc:
        raise ValueError("time must be ISO-8601") from exc
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError("time must be timezone-aware")
    return parsed


def _content_hash(content: str) -> str:
    return sha256(content.encode("utf-8")).hexdigest()


class MemoryLifecycleStore:
    """Local SQLite reference with CAS-style version checks and hash-chained events."""

    def __init__(self, path: str = ":memory:") -> None:
        self.conn = sqlite3.connect(path)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA foreign_keys=ON")
        self.conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS memory_versions (
                memory_id TEXT NOT NULL,
                version INTEGER NOT NULL,
                origin_id TEXT NOT NULL,
                scope TEXT NOT NULL,
                state TEXT NOT NULL,
                content TEXT NOT NULL,
                content_hash TEXT NOT NULL,
                valid_from TEXT NOT NULL,
                valid_to TEXT,
                recorded_at TEXT NOT NULL,
                predecessor_version INTEGER,
                provenance_json TEXT NOT NULL,
                PRIMARY KEY(memory_id, version)
            );
            CREATE TABLE IF NOT EXISTS memory_events (
                seq INTEGER PRIMARY KEY AUTOINCREMENT,
                memory_id TEXT NOT NULL,
                version INTEGER NOT NULL,
                operation TEXT NOT NULL,
                recorded_at TEXT NOT NULL,
                previous_event_hash TEXT NOT NULL,
                event_hash TEXT NOT NULL
            );
            """
        )
        self.conn.commit()

    def close(self) -> None:
        self.conn.close()

    @staticmethod
    def _require_scope(authority: AuthorityLike, capability: str, scope: str, state_version: str) -> None:
        required = f"memory:{capability}:{scope}"
        try:
            fresh = authority.fresh
            witness_state = authority.state_version
            witness_scopes = authority.scope
        except AttributeError as exc:
            raise MemoryOperationError("authority witness contract required") from exc
        if type(fresh) is not bool or not fresh or witness_state != state_version or required not in witness_scopes:
            raise MemoryOperationError(f"missing fresh authority scope: {required}")

    @staticmethod
    def _validate_identity(memory_id: str, origin_id: str, scope: str, content: str, provenance_ids: Tuple[str, ...]) -> None:
        for value, name in ((memory_id, "memory_id"), (origin_id, "origin_id"), (scope, "scope")):
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{name} must be non-empty")
        if not isinstance(content, str):
            raise ValueError("content must be string")
        if not provenance_ids or any(not isinstance(p, str) or not p.strip() for p in provenance_ids):
            raise ValueError("provenance_ids must contain non-empty strings")
        if len(set(provenance_ids)) != len(provenance_ids):
            raise ValueError("provenance_ids must be unique")

    @staticmethod
    def _validate_times(valid_from: str, valid_to: Optional[str], recorded_at: str) -> None:
        start = _parse_time(valid_from)
        _parse_time(recorded_at)
        if valid_to is not None and _parse_time(valid_to) <= start:
            raise ValueError("valid_to must be later than valid_from")

    def _last_event_hash(self) -> str:
        row = self.conn.execute("SELECT event_hash FROM memory_events ORDER BY seq DESC LIMIT 1").fetchone()
        return row["event_hash"] if row else "GENESIS"

    def _append_event(self, memory_id: str, version: int, operation: str, recorded_at: str) -> str:
        previous = self._last_event_hash()
        payload = {
            "memory_id": memory_id,
            "operation": operation,
            "previous_event_hash": previous,
            "recorded_at": recorded_at,
            "version": version,
        }
        event_hash = sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        self.conn.execute(
            "INSERT INTO memory_events(memory_id,version,operation,recorded_at,previous_event_hash,event_hash) VALUES(?,?,?,?,?,?)",
            (memory_id, version, operation, recorded_at, previous, event_hash),
        )
        return event_hash

    def admit(self, *, authority: AuthorityLike, state_version: str, memory_id: str, origin_id: str,
              scope: str, content: str, valid_from: str, valid_to: Optional[str], recorded_at: str,
              provenance_ids: Tuple[str, ...]) -> MemoryRecord:
        self._validate_identity(memory_id, origin_id, scope, content, provenance_ids)
        self._validate_times(valid_from, valid_to, recorded_at)
        self._require_scope(authority, "admit", scope, state_version)
        if self.conn.execute("SELECT 1 FROM memory_versions WHERE memory_id=? LIMIT 1", (memory_id,)).fetchone():
            raise MemoryOperationError("memory_id already exists; use revise")
        with self.conn:
            self.conn.execute(
                "INSERT INTO memory_versions VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                (memory_id, 1, origin_id, scope, MemoryState.ACTIVE.value, content, _content_hash(content),
                 valid_from, valid_to, recorded_at, None, json.dumps(list(provenance_ids))),
            )
            self._append_event(memory_id, 1, "ADMIT", recorded_at)
        return self.get(authority=authority, state_version=state_version, memory_id=memory_id, version=1,
                        forensic=True, forensic_capability="admit")

    def revise(self, *, authority: AuthorityLike, state_version: str, memory_id: str, expected_version: int,
               content: str, valid_from: str, valid_to: Optional[str], recorded_at: str,
               provenance_ids: Tuple[str, ...]) -> MemoryRecord:
        current = self._current(memory_id)
        self._require_scope(authority, "revise", current.scope, state_version)
        self._validate_identity(memory_id, current.origin_id, current.scope, content, provenance_ids)
        self._validate_times(valid_from, valid_to, recorded_at)
        if current.version != expected_version:
            raise MemoryOperationError("stale memory version")
        if current.state is not MemoryState.ACTIVE:
            raise MemoryOperationError("only ACTIVE memory may be revised")
        new_version = current.version + 1
        with self.conn:
            self.conn.execute(
                "UPDATE memory_versions SET state=? WHERE memory_id=? AND version=?",
                (MemoryState.SUPERSEDED.value, memory_id, current.version),
            )
            self.conn.execute(
                "INSERT INTO memory_versions VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",
                (memory_id, new_version, current.origin_id, current.scope, MemoryState.ACTIVE.value, content,
                 _content_hash(content), valid_from, valid_to, recorded_at, current.version,
                 json.dumps(list(provenance_ids))),
            )
            self._append_event(memory_id, new_version, "REVISE", recorded_at)
        return self.get(authority=authority, state_version=state_version, memory_id=memory_id,
                        version=new_version, forensic=True, forensic_capability="revise")

    def transition(self, *, authority: AuthorityLike, state_version: str, memory_id: str,
                   expected_version: int, target: MemoryState, recorded_at: str) -> MemoryRecord:
        if target not in (MemoryState.QUARANTINED, MemoryState.EXPIRED, MemoryState.TOMBSTONED):
            raise MemoryOperationError("unsupported transition target")
        _parse_time(recorded_at)
        current = self._current(memory_id)
        capability = {
            MemoryState.QUARANTINED: "quarantine",
            MemoryState.EXPIRED: "expire",
            MemoryState.TOMBSTONED: "tombstone",
        }[target]
        self._require_scope(authority, capability, current.scope, state_version)
        if current.version != expected_version:
            raise MemoryOperationError("stale memory version")
        if current.state is not MemoryState.ACTIVE:
            raise MemoryOperationError("only ACTIVE memory can transition")
        with self.conn:
            self.conn.execute(
                "UPDATE memory_versions SET state=? WHERE memory_id=? AND version=?",
                (target.value, memory_id, current.version),
            )
            self._append_event(memory_id, current.version, target.value, recorded_at)
        return self.get(authority=authority, state_version=state_version, memory_id=memory_id,
                        version=current.version, forensic=True, forensic_capability=capability)

    def _current(self, memory_id: str) -> MemoryRecord:
        row = self.conn.execute(
            "SELECT * FROM memory_versions WHERE memory_id=? ORDER BY version DESC LIMIT 1", (memory_id,)
        ).fetchone()
        if row is None:
            raise MemoryOperationError("unknown memory_id")
        return self._row_to_record(row)

    def get(self, *, authority: AuthorityLike, state_version: str, memory_id: str,
            version: Optional[int] = None, forensic: bool = False,
            forensic_capability: str = "forensic") -> MemoryRecord:
        if version is None:
            row = self.conn.execute(
                "SELECT * FROM memory_versions WHERE memory_id=? ORDER BY version DESC LIMIT 1", (memory_id,)
            ).fetchone()
        else:
            row = self.conn.execute(
                "SELECT * FROM memory_versions WHERE memory_id=? AND version=?", (memory_id, version)
            ).fetchone()
        if row is None:
            raise MemoryOperationError("unknown memory/version")
        record = self._row_to_record(row)
        capability = forensic_capability if forensic else "read"
        self._require_scope(authority, capability, record.scope, state_version)
        if not forensic and record.state is not MemoryState.ACTIVE:
            raise MemoryOperationError("memory state excluded from default retrieval")
        return record

    @staticmethod
    def _row_to_record(row: sqlite3.Row) -> MemoryRecord:
        return MemoryRecord(
            memory_id=row["memory_id"], version=row["version"], origin_id=row["origin_id"], scope=row["scope"],
            state=MemoryState(row["state"]), content=row["content"], content_hash=row["content_hash"],
            valid_from=row["valid_from"], valid_to=row["valid_to"], recorded_at=row["recorded_at"],
            predecessor_version=row["predecessor_version"], provenance_ids=tuple(json.loads(row["provenance_json"])),
        )

    def verify_integrity(self) -> Tuple[str, ...]:
        failures = []
        rows = self.conn.execute("SELECT * FROM memory_versions ORDER BY memory_id, version").fetchall()
        for row in rows:
            if _content_hash(row["content"]) != row["content_hash"]:
                failures.append(f"CONTENT_HASH:{row['memory_id']}:{row['version']}")
        previous = "GENESIS"
        events = self.conn.execute("SELECT * FROM memory_events ORDER BY seq").fetchall()
        for event in events:
            payload = {
                "memory_id": event["memory_id"],
                "operation": event["operation"],
                "previous_event_hash": previous,
                "recorded_at": event["recorded_at"],
                "version": event["version"],
            }
            expected = sha256(json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()).hexdigest()
            if event["previous_event_hash"] != previous or event["event_hash"] != expected:
                failures.append(f"EVENT_CHAIN:{event['seq']}")
            previous = event["event_hash"]
        return tuple(failures)
