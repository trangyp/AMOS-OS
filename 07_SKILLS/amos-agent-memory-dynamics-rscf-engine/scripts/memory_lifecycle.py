#!/usr/bin/env python3
"""Evidence-bound local memory lifecycle reference for AMOS.

This module implements local SQLite semantics only. It is not a production
memory service, authorization system, knowledge validator, or distributed
consensus layer.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

ALLOWED_STATUS = {"ACTIVE", "QUARANTINED", "TOMBSTONED"}
ALLOWED_SOURCE_CLASS = {
    "OBSERVATION",
    "SOURCE_CLAIM",
    "DERIVED",
    "MODEL",
    "DECISION",
    "UNKNOWN",
}


class MemoryErrorBase(RuntimeError):
    pass


class MemoryNotFound(MemoryErrorBase):
    pass


class MemoryAuthorityError(MemoryErrorBase):
    pass


class MemoryConflictError(MemoryErrorBase):
    pass


class MemoryStateError(MemoryErrorBase):
    pass


class MemoryIntegrityError(MemoryErrorBase):
    pass


def _canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _hash_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _hash_json(value: Any) -> str:
    return _hash_text(_canonical_json(value))


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="microseconds").replace("+00:00", "Z")


def _normalize_time(value: str | datetime | None, *, default_now: bool = False) -> str | None:
    if value is None:
        return _utc_now() if default_now else None
    if isinstance(value, datetime):
        dt = value
    elif isinstance(value, str):
        raw = value[:-1] + "+00:00" if value.endswith("Z") else value
        dt = datetime.fromisoformat(raw)
    else:
        raise TypeError("time value must be str, datetime, or None")
    if dt.tzinfo is None:
        raise ValueError("time value must be timezone-aware")
    return dt.astimezone(timezone.utc).isoformat(timespec="microseconds").replace("+00:00", "Z")


def _parse_time(value: str) -> datetime:
    raw = value[:-1] + "+00:00" if value.endswith("Z") else value
    return datetime.fromisoformat(raw).astimezone(timezone.utc)


def _tokens(text: str) -> set[str]:
    return {m.group(0).lower() for m in re.finditer(r"[A-Za-z0-9_]+", text)}


@dataclass(frozen=True)
class MemoryView:
    memory_id: str
    revision: int
    namespace: str
    content: str
    content_hash: str
    provenance_id: str
    source_class: str
    epistemic_class: str
    required_scope: str
    status: str
    valid_from: str
    valid_to: str | None
    expires_at: str | None
    recorded_at: str
    metadata: dict[str, Any]
    retrieval_score: float | None = None
    snapshot_stale: bool = False

    def to_dict(self) -> dict[str, Any]:
        return {
            "memory_id": self.memory_id,
            "revision": self.revision,
            "namespace": self.namespace,
            "content": self.content,
            "content_hash": self.content_hash,
            "provenance_id": self.provenance_id,
            "source_class": self.source_class,
            "epistemic_class": self.epistemic_class,
            "required_scope": self.required_scope,
            "status": self.status,
            "valid_from": self.valid_from,
            "valid_to": self.valid_to,
            "expires_at": self.expires_at,
            "recorded_at": self.recorded_at,
            "metadata": self.metadata,
            "retrieval_score": self.retrieval_score,
            "snapshot_stale": self.snapshot_stale,
        }


class MemoryLifecycleStore:
    """Local reference implementation for governed memory lifecycle semantics."""

    def __init__(self, path: str | Path = ":memory:") -> None:
        self.path = str(path)
        self.conn = sqlite3.connect(self.path)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA foreign_keys = ON")
        self._init_schema()

    def close(self) -> None:
        self.conn.close()

    def __enter__(self) -> "MemoryLifecycleStore":
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any) -> None:
        self.close()

    def _init_schema(self) -> None:
        self.conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS memory_objects (
                memory_id TEXT PRIMARY KEY,
                namespace TEXT NOT NULL,
                required_scope TEXT NOT NULL,
                status TEXT NOT NULL,
                latest_revision INTEGER NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS memory_revisions (
                memory_id TEXT NOT NULL,
                revision INTEGER NOT NULL,
                content TEXT NOT NULL,
                content_hash TEXT NOT NULL,
                provenance_id TEXT NOT NULL,
                source_class TEXT NOT NULL,
                valid_from TEXT NOT NULL,
                valid_to TEXT,
                expires_at TEXT,
                recorded_at TEXT NOT NULL,
                metadata_json TEXT NOT NULL,
                PRIMARY KEY(memory_id, revision),
                FOREIGN KEY(memory_id) REFERENCES memory_objects(memory_id)
            );

            CREATE TABLE IF NOT EXISTS memory_events (
                event_id INTEGER PRIMARY KEY AUTOINCREMENT,
                event_type TEXT NOT NULL,
                memory_id TEXT,
                revision INTEGER,
                payload_json TEXT NOT NULL,
                recorded_at TEXT NOT NULL,
                prev_hash TEXT NOT NULL,
                event_hash TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS memory_conflicts (
                conflict_id TEXT PRIMARY KEY,
                left_memory_id TEXT NOT NULL,
                left_revision INTEGER NOT NULL,
                right_memory_id TEXT NOT NULL,
                right_revision INTEGER NOT NULL,
                reason TEXT NOT NULL,
                status TEXT NOT NULL,
                recorded_at TEXT NOT NULL
            );

            CREATE TABLE IF NOT EXISTS context_snapshots (
                snapshot_id TEXT PRIMARY KEY,
                namespace TEXT NOT NULL,
                query TEXT NOT NULL,
                as_of TEXT NOT NULL,
                max_chars INTEGER NOT NULL,
                selection_json TEXT NOT NULL,
                snapshot_hash TEXT NOT NULL,
                created_at TEXT NOT NULL
            );
            """
        )
        self.conn.commit()

    def _append_event(
        self,
        event_type: str,
        memory_id: str | None,
        revision: int | None,
        payload: Mapping[str, Any],
        *,
        recorded_at: str | None = None,
    ) -> str:
        ts = _normalize_time(recorded_at, default_now=True)
        assert ts is not None
        row = self.conn.execute(
            "SELECT event_hash FROM memory_events ORDER BY event_id DESC LIMIT 1"
        ).fetchone()
        prev_hash = row["event_hash"] if row else "GENESIS"
        payload_json = _canonical_json(dict(payload))
        event_hash = _hash_json(
            {
                "event_type": event_type,
                "memory_id": memory_id,
                "revision": revision,
                "payload": json.loads(payload_json),
                "recorded_at": ts,
                "prev_hash": prev_hash,
            }
        )
        self.conn.execute(
            """
            INSERT INTO memory_events(
                event_type, memory_id, revision, payload_json,
                recorded_at, prev_hash, event_hash
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (event_type, memory_id, revision, payload_json, ts, prev_hash, event_hash),
        )
        return event_hash

    @staticmethod
    def _authorize(required_scope: str, scopes: Iterable[str]) -> None:
        granted = set(scopes)
        if "*" not in granted and required_scope not in granted:
            raise MemoryAuthorityError(f"missing required scope: {required_scope}")

    def _object(self, memory_id: str) -> sqlite3.Row:
        row = self.conn.execute(
            "SELECT * FROM memory_objects WHERE memory_id = ?", (memory_id,)
        ).fetchone()
        if row is None:
            raise MemoryNotFound(memory_id)
        return row

    def _revision(self, memory_id: str, revision: int) -> sqlite3.Row:
        row = self.conn.execute(
            "SELECT * FROM memory_revisions WHERE memory_id = ? AND revision = ?",
            (memory_id, revision),
        ).fetchone()
        if row is None:
            raise MemoryNotFound(f"{memory_id}@{revision}")
        return row

    def admit(
        self,
        *,
        memory_id: str,
        namespace: str,
        content: str,
        provenance_id: str,
        required_scope: str,
        source_class: str = "OBSERVATION",
        valid_from: str | datetime | None = None,
        expires_at: str | datetime | None = None,
        metadata: Mapping[str, Any] | None = None,
        recorded_at: str | datetime | None = None,
    ) -> MemoryView:
        if not memory_id or not namespace or not content or not provenance_id or not required_scope:
            raise ValueError("memory_id, namespace, content, provenance_id, and required_scope are required")
        if source_class not in ALLOWED_SOURCE_CLASS:
            raise ValueError(f"unsupported source_class: {source_class}")
        ts = _normalize_time(recorded_at, default_now=True)
        effective = _normalize_time(valid_from) or ts
        expiry = _normalize_time(expires_at)
        assert ts is not None and effective is not None
        if expiry is not None and _parse_time(expiry) <= _parse_time(effective):
            raise ValueError("expires_at must be after valid_from")
        content_hash = _hash_text(content)
        meta_json = _canonical_json(dict(metadata or {}))
        with self.conn:
            exists = self.conn.execute(
                "SELECT 1 FROM memory_objects WHERE memory_id = ?", (memory_id,)
            ).fetchone()
            if exists:
                raise MemoryConflictError(f"memory already exists: {memory_id}")
            self.conn.execute(
                """
                INSERT INTO memory_objects(
                    memory_id, namespace, required_scope, status,
                    latest_revision, created_at, updated_at
                ) VALUES (?, ?, ?, 'ACTIVE', 1, ?, ?)
                """,
                (memory_id, namespace, required_scope, ts, ts),
            )
            self.conn.execute(
                """
                INSERT INTO memory_revisions(
                    memory_id, revision, content, content_hash, provenance_id,
                    source_class, valid_from, valid_to, expires_at, recorded_at,
                    metadata_json
                ) VALUES (?, 1, ?, ?, ?, ?, ?, NULL, ?, ?, ?)
                """,
                (
                    memory_id,
                    content,
                    content_hash,
                    provenance_id,
                    source_class,
                    effective,
                    expiry,
                    ts,
                    meta_json,
                ),
            )
            self._append_event(
                "ADMIT",
                memory_id,
                1,
                {
                    "content_hash": content_hash,
                    "namespace": namespace,
                    "provenance_id": provenance_id,
                    "required_scope": required_scope,
                    "source_class": source_class,
                    "valid_from": effective,
                    "expires_at": expiry,
                },
                recorded_at=ts,
            )
        return self.get(memory_id, scopes={required_scope}, as_of=effective)

    def revise(
        self,
        *,
        memory_id: str,
        expected_revision: int,
        content: str,
        provenance_id: str,
        source_class: str = "OBSERVATION",
        effective_at: str | datetime | None = None,
        expires_at: str | datetime | None = None,
        metadata: Mapping[str, Any] | None = None,
        recorded_at: str | datetime | None = None,
    ) -> MemoryView:
        if not content or not provenance_id:
            raise ValueError("content and provenance_id are required")
        if source_class not in ALLOWED_SOURCE_CLASS:
            raise ValueError(f"unsupported source_class: {source_class}")
        obj = self._object(memory_id)
        if obj["status"] != "ACTIVE":
            raise MemoryStateError(f"cannot revise {obj['status'].lower()} memory")
        if int(obj["latest_revision"]) != int(expected_revision):
            raise MemoryConflictError(
                f"stale revision: expected {expected_revision}, current {obj['latest_revision']}"
            )
        prior = self._revision(memory_id, expected_revision)
        ts = _normalize_time(recorded_at, default_now=True)
        effective = _normalize_time(effective_at) or ts
        expiry = _normalize_time(expires_at)
        assert ts is not None and effective is not None
        if _parse_time(effective) < _parse_time(prior["valid_from"]):
            raise ValueError("effective_at cannot precede prior valid_from")
        if expiry is not None and _parse_time(expiry) <= _parse_time(effective):
            raise ValueError("expires_at must be after effective_at")
        new_revision = expected_revision + 1
        content_hash = _hash_text(content)
        meta_json = _canonical_json(dict(metadata or {}))
        with self.conn:
            self.conn.execute(
                "UPDATE memory_revisions SET valid_to = ? WHERE memory_id = ? AND revision = ?",
                (effective, memory_id, expected_revision),
            )
            self.conn.execute(
                """
                INSERT INTO memory_revisions(
                    memory_id, revision, content, content_hash, provenance_id,
                    source_class, valid_from, valid_to, expires_at, recorded_at,
                    metadata_json
                ) VALUES (?, ?, ?, ?, ?, ?, ?, NULL, ?, ?, ?)
                """,
                (
                    memory_id,
                    new_revision,
                    content,
                    content_hash,
                    provenance_id,
                    source_class,
                    effective,
                    expiry,
                    ts,
                    meta_json,
                ),
            )
            cur = self.conn.execute(
                """
                UPDATE memory_objects
                SET latest_revision = ?, updated_at = ?
                WHERE memory_id = ? AND latest_revision = ? AND status = 'ACTIVE'
                """,
                (new_revision, ts, memory_id, expected_revision),
            )
            if cur.rowcount != 1:
                raise MemoryConflictError("concurrent memory revision detected")
            self._append_event(
                "REVISE",
                memory_id,
                new_revision,
                {
                    "content_hash": content_hash,
                    "previous_revision": expected_revision,
                    "provenance_id": provenance_id,
                    "source_class": source_class,
                    "valid_from": effective,
                    "expires_at": expiry,
                },
                recorded_at=ts,
            )
        return self.get(memory_id, scopes={obj["required_scope"]})

    def quarantine(
        self,
        memory_id: str,
        *,
        expected_revision: int,
        reason: str,
        recorded_at: str | datetime | None = None,
    ) -> None:
        self._set_status(
            memory_id,
            expected_revision=expected_revision,
            target="QUARANTINED",
            event_type="QUARANTINE",
            reason=reason,
            recorded_at=recorded_at,
        )

    def restore(
        self,
        memory_id: str,
        *,
        expected_revision: int,
        reason: str,
        recorded_at: str | datetime | None = None,
    ) -> None:
        obj = self._object(memory_id)
        if obj["status"] != "QUARANTINED":
            raise MemoryStateError("only quarantined memory can be restored")
        self._set_status(
            memory_id,
            expected_revision=expected_revision,
            target="ACTIVE",
            event_type="RESTORE",
            reason=reason,
            recorded_at=recorded_at,
        )

    def tombstone(
        self,
        memory_id: str,
        *,
        expected_revision: int,
        reason: str,
        recorded_at: str | datetime | None = None,
    ) -> None:
        self._set_status(
            memory_id,
            expected_revision=expected_revision,
            target="TOMBSTONED",
            event_type="TOMBSTONE",
            reason=reason,
            recorded_at=recorded_at,
        )

    def _set_status(
        self,
        memory_id: str,
        *,
        expected_revision: int,
        target: str,
        event_type: str,
        reason: str,
        recorded_at: str | datetime | None,
    ) -> None:
        if target not in ALLOWED_STATUS:
            raise ValueError(target)
        if not reason:
            raise ValueError("reason is required")
        obj = self._object(memory_id)
        if int(obj["latest_revision"]) != int(expected_revision):
            raise MemoryConflictError("stale revision for status transition")
        if obj["status"] == "TOMBSTONED" and target != "TOMBSTONED":
            raise MemoryStateError("tombstoned memory cannot be reactivated")
        ts = _normalize_time(recorded_at, default_now=True)
        assert ts is not None
        with self.conn:
            cur = self.conn.execute(
                """
                UPDATE memory_objects SET status = ?, updated_at = ?
                WHERE memory_id = ? AND latest_revision = ?
                """,
                (target, ts, memory_id, expected_revision),
            )
            if cur.rowcount != 1:
                raise MemoryConflictError("concurrent status transition detected")
            self._append_event(
                event_type,
                memory_id,
                expected_revision,
                {"reason": reason, "target_status": target},
                recorded_at=ts,
            )

    def declare_conflict(
        self,
        *,
        left_memory_id: str,
        left_expected_revision: int,
        right_memory_id: str,
        right_expected_revision: int,
        reason: str,
        recorded_at: str | datetime | None = None,
    ) -> str:
        if left_memory_id == right_memory_id:
            raise ValueError("conflict requires two distinct memory objects")
        if not reason:
            raise ValueError("reason is required")
        left = self._object(left_memory_id)
        right = self._object(right_memory_id)
        if int(left["latest_revision"]) != left_expected_revision:
            raise MemoryConflictError("left memory revision is stale")
        if int(right["latest_revision"]) != right_expected_revision:
            raise MemoryConflictError("right memory revision is stale")
        ts = _normalize_time(recorded_at, default_now=True)
        assert ts is not None
        conflict_id = "conf-" + _hash_json(
            {
                "left": [left_memory_id, left_expected_revision],
                "right": [right_memory_id, right_expected_revision],
                "reason": reason,
                "recorded_at": ts,
            }
        )[:20]
        with self.conn:
            self.conn.execute(
                """
                INSERT INTO memory_conflicts(
                    conflict_id, left_memory_id, left_revision,
                    right_memory_id, right_revision, reason, status, recorded_at
                ) VALUES (?, ?, ?, ?, ?, ?, 'OPEN', ?)
                """,
                (
                    conflict_id,
                    left_memory_id,
                    left_expected_revision,
                    right_memory_id,
                    right_expected_revision,
                    reason,
                    ts,
                ),
            )
            for memory_id, revision in (
                (left_memory_id, left_expected_revision),
                (right_memory_id, right_expected_revision),
            ):
                self.conn.execute(
                    "UPDATE memory_objects SET status = 'QUARANTINED', updated_at = ? WHERE memory_id = ?",
                    (ts, memory_id),
                )
                self._append_event(
                    "CONFLICT_DECLARED",
                    memory_id,
                    revision,
                    {"conflict_id": conflict_id, "reason": reason},
                    recorded_at=ts,
                )
        return conflict_id

    def get(
        self,
        memory_id: str,
        *,
        scopes: Iterable[str],
        as_of: str | datetime | None = None,
        include_quarantined: bool = False,
        include_tombstoned: bool = False,
        include_expired: bool = False,
    ) -> MemoryView:
        obj = self._object(memory_id)
        self._authorize(obj["required_scope"], scopes)
        status = obj["status"]
        if status == "QUARANTINED" and not include_quarantined:
            raise MemoryStateError("memory is quarantined")
        if status == "TOMBSTONED" and not include_tombstoned:
            raise MemoryStateError("memory is tombstoned")
        target = _normalize_time(as_of, default_now=True)
        assert target is not None
        rows = self.conn.execute(
            "SELECT * FROM memory_revisions WHERE memory_id = ? ORDER BY revision DESC",
            (memory_id,),
        ).fetchall()
        chosen: sqlite3.Row | None = None
        t = _parse_time(target)
        for row in rows:
            start = _parse_time(row["valid_from"])
            end = _parse_time(row["valid_to"]) if row["valid_to"] else None
            if start <= t and (end is None or t < end):
                chosen = row
                break
        if chosen is None:
            raise MemoryNotFound(f"no revision valid at {target}: {memory_id}")
        if chosen["expires_at"] and not include_expired:
            if t >= _parse_time(chosen["expires_at"]):
                raise MemoryStateError("memory is expired for this retrieval time")
        return MemoryView(
            memory_id=memory_id,
            revision=int(chosen["revision"]),
            namespace=obj["namespace"],
            content=chosen["content"],
            content_hash=chosen["content_hash"],
            provenance_id=chosen["provenance_id"],
            source_class=chosen["source_class"],
            epistemic_class="OBSERVATION",
            required_scope=obj["required_scope"],
            status=status,
            valid_from=chosen["valid_from"],
            valid_to=chosen["valid_to"],
            expires_at=chosen["expires_at"],
            recorded_at=chosen["recorded_at"],
            metadata=json.loads(chosen["metadata_json"]),
        )

    def search(
        self,
        *,
        namespace: str,
        query: str,
        scopes: Iterable[str],
        top_k: int = 10,
        as_of: str | datetime | None = None,
        include_expired: bool = False,
    ) -> list[MemoryView]:
        if top_k < 1:
            raise ValueError("top_k must be positive")
        query_tokens = _tokens(query)
        rows = self.conn.execute(
            "SELECT memory_id FROM memory_objects WHERE namespace = ? AND status = 'ACTIVE' ORDER BY memory_id",
            (namespace,),
        ).fetchall()
        ranked: list[MemoryView] = []
        for row in rows:
            try:
                view = self.get(
                    row["memory_id"],
                    scopes=scopes,
                    as_of=as_of,
                    include_expired=include_expired,
                )
            except (MemoryAuthorityError, MemoryStateError, MemoryNotFound):
                continue
            content_tokens = _tokens(view.content)
            if query_tokens:
                overlap = len(query_tokens & content_tokens)
                score = overlap / len(query_tokens)
                if score <= 0:
                    continue
            else:
                score = 1.0
            ranked.append(
                MemoryView(**{**view.__dict__, "retrieval_score": round(score, 6)})
            )
        ranked.sort(key=lambda item: (-(item.retrieval_score or 0.0), item.memory_id, -item.revision))
        return ranked[:top_k]

    def assemble_context(
        self,
        *,
        namespace: str,
        query: str,
        scopes: Iterable[str],
        max_chars: int,
        as_of: str | datetime | None = None,
    ) -> dict[str, Any]:
        if max_chars < 1:
            raise ValueError("max_chars must be positive")
        target = _normalize_time(as_of, default_now=True)
        assert target is not None
        candidates = self.search(
            namespace=namespace,
            query=query,
            scopes=scopes,
            top_k=1000,
            as_of=target,
        )
        selected: list[MemoryView] = []
        seen_hashes: set[str] = set()
        used = 0
        for item in candidates:
            if item.content_hash in seen_hashes:
                continue
            cost = len(item.content)
            if selected and used + cost > max_chars:
                continue
            if not selected and cost > max_chars:
                continue
            selected.append(item)
            seen_hashes.add(item.content_hash)
            used += cost
        selection = [
            {
                "memory_id": item.memory_id,
                "revision": item.revision,
                "content_hash": item.content_hash,
                "retrieval_score": item.retrieval_score,
            }
            for item in selected
        ]
        basis = {
            "namespace": namespace,
            "query": query,
            "as_of": target,
            "max_chars": max_chars,
            "selection": selection,
        }
        snapshot_hash = _hash_json(basis)
        snapshot_id = "ctx-" + snapshot_hash[:20]
        created_at = _utc_now()
        with self.conn:
            self.conn.execute(
                """
                INSERT OR IGNORE INTO context_snapshots(
                    snapshot_id, namespace, query, as_of, max_chars,
                    selection_json, snapshot_hash, created_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    snapshot_id,
                    namespace,
                    query,
                    target,
                    max_chars,
                    _canonical_json(selection),
                    snapshot_hash,
                    created_at,
                ),
            )
            self._append_event(
                "CONTEXT_ASSEMBLED",
                None,
                None,
                {
                    "snapshot_id": snapshot_id,
                    "snapshot_hash": snapshot_hash,
                    "namespace": namespace,
                    "selection_count": len(selection),
                },
                recorded_at=created_at,
            )
        return {
            "snapshot_id": snapshot_id,
            "snapshot_hash": snapshot_hash,
            "epistemic_class": "OBSERVATION",
            "as_of": target,
            "used_chars": used,
            "memories": [item.to_dict() for item in selected],
        }

    def replay_context_snapshot(
        self,
        snapshot_id: str,
        *,
        scopes: Iterable[str],
    ) -> dict[str, Any]:
        row = self.conn.execute(
            "SELECT * FROM context_snapshots WHERE snapshot_id = ?", (snapshot_id,)
        ).fetchone()
        if row is None:
            raise MemoryNotFound(snapshot_id)
        selection = json.loads(row["selection_json"])
        memories: list[dict[str, Any]] = []
        any_stale = False
        for item in selection:
            obj = self._object(item["memory_id"])
            self._authorize(obj["required_scope"], scopes)
            if obj["status"] != "ACTIVE":
                raise MemoryStateError(
                    f"snapshot replay blocked by current memory status: {obj['status']}"
                )
            rev = self._revision(item["memory_id"], int(item["revision"]))
            if rev["content_hash"] != item["content_hash"]:
                raise MemoryIntegrityError("snapshot revision content hash mismatch")
            stale = int(obj["latest_revision"]) != int(item["revision"])
            any_stale = any_stale or stale
            memories.append(
                MemoryView(
                    memory_id=item["memory_id"],
                    revision=int(item["revision"]),
                    namespace=obj["namespace"],
                    content=rev["content"],
                    content_hash=rev["content_hash"],
                    provenance_id=rev["provenance_id"],
                    source_class=rev["source_class"],
                    epistemic_class="OBSERVATION",
                    required_scope=obj["required_scope"],
                    status=obj["status"],
                    valid_from=rev["valid_from"],
                    valid_to=rev["valid_to"],
                    expires_at=rev["expires_at"],
                    recorded_at=rev["recorded_at"],
                    metadata=json.loads(rev["metadata_json"]),
                    retrieval_score=item.get("retrieval_score"),
                    snapshot_stale=stale,
                ).to_dict()
            )
        return {
            "snapshot_id": snapshot_id,
            "snapshot_hash": row["snapshot_hash"],
            "epistemic_class": "OBSERVATION",
            "snapshot_stale": any_stale,
            "memories": memories,
        }

    def events(self, memory_id: str | None = None) -> list[dict[str, Any]]:
        if memory_id is None:
            rows = self.conn.execute("SELECT * FROM memory_events ORDER BY event_id").fetchall()
        else:
            rows = self.conn.execute(
                "SELECT * FROM memory_events WHERE memory_id = ? ORDER BY event_id",
                (memory_id,),
            ).fetchall()
        return [
            {
                **dict(row),
                "payload": json.loads(row["payload_json"]),
            }
            for row in rows
        ]

    def verify_integrity(self) -> dict[str, Any]:
        issues: list[str] = []
        objects = self.conn.execute("SELECT * FROM memory_objects ORDER BY memory_id").fetchall()
        for obj in objects:
            rows = self.conn.execute(
                "SELECT * FROM memory_revisions WHERE memory_id = ? ORDER BY revision",
                (obj["memory_id"],),
            ).fetchall()
            if not rows:
                issues.append(f"NO_REVISIONS:{obj['memory_id']}")
                continue
            revisions = [int(row["revision"]) for row in rows]
            if revisions != list(range(1, len(rows) + 1)):
                issues.append(f"REVISION_GAP:{obj['memory_id']}")
            if int(obj["latest_revision"]) != revisions[-1]:
                issues.append(f"LATEST_REVISION_MISMATCH:{obj['memory_id']}")
            for row in rows:
                if _hash_text(row["content"]) != row["content_hash"]:
                    issues.append(f"CONTENT_HASH:{obj['memory_id']}@{row['revision']}")

        prev_hash = "GENESIS"
        events = self.conn.execute("SELECT * FROM memory_events ORDER BY event_id").fetchall()
        for row in events:
            if row["prev_hash"] != prev_hash:
                issues.append(f"EVENT_PREV_HASH:{row['event_id']}")
            expected = _hash_json(
                {
                    "event_type": row["event_type"],
                    "memory_id": row["memory_id"],
                    "revision": row["revision"],
                    "payload": json.loads(row["payload_json"]),
                    "recorded_at": row["recorded_at"],
                    "prev_hash": row["prev_hash"],
                }
            )
            if expected != row["event_hash"]:
                issues.append(f"EVENT_HASH:{row['event_id']}")
            prev_hash = row["event_hash"]

        snapshots = self.conn.execute("SELECT * FROM context_snapshots ORDER BY snapshot_id").fetchall()
        for row in snapshots:
            basis = {
                "namespace": row["namespace"],
                "query": row["query"],
                "as_of": row["as_of"],
                "max_chars": int(row["max_chars"]),
                "selection": json.loads(row["selection_json"]),
            }
            expected = _hash_json(basis)
            if expected != row["snapshot_hash"]:
                issues.append(f"SNAPSHOT_HASH:{row['snapshot_id']}")
            if row["snapshot_id"] != "ctx-" + expected[:20]:
                issues.append(f"SNAPSHOT_ID:{row['snapshot_id']}")

        return {
            "status": "PASS" if not issues else "QUARANTINE",
            "issues": issues,
            "objects": len(objects),
            "events": len(events),
            "snapshots": len(snapshots),
        }


def _self_test() -> dict[str, Any]:
    with MemoryLifecycleStore() as store:
        store.admit(
            memory_id="m1",
            namespace="demo",
            content="alpha beta",
            provenance_id="source-1",
            required_scope="demo:read",
            recorded_at="2026-09-14T00:00:00Z",
        )
        store.revise(
            memory_id="m1",
            expected_revision=1,
            content="alpha gamma",
            provenance_id="source-2",
            effective_at="2026-09-14T01:00:00Z",
            recorded_at="2026-09-14T01:00:00Z",
        )
        snapshot = store.assemble_context(
            namespace="demo",
            query="alpha",
            scopes={"demo:read"},
            max_chars=100,
            as_of="2026-09-14T02:00:00Z",
        )
        integrity = store.verify_integrity()
        if integrity["status"] != "PASS":
            raise AssertionError(integrity)
        return {"status": "PASS", "snapshot_id": snapshot["snapshot_id"]}


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="AMOS local memory lifecycle reference")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--check-db", type=Path)
    args = parser.parse_args(argv)
    if args.self_test:
        print(_canonical_json(_self_test()))
        return 0
    if args.check_db:
        with MemoryLifecycleStore(args.check_db) as store:
            result = store.verify_integrity()
            print(_canonical_json(result))
            return 0 if result["status"] == "PASS" else 1
    parser.error("use --self-test or --check-db")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
