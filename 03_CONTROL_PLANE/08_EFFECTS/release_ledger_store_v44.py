"""Local SQLite/WAL reference store for AMOS effect release state.

Origin architect / steward: Trang Phan.

This is an AMOS_MODEL local transactional reference. It provides durable local
persistence, idempotency/lineage checks, monotonic versions, and CAS transitions.
It is not distributed consensus and does not by itself authorize an effect.
"""
from __future__ import annotations

from contextlib import closing
from dataclasses import dataclass
from enum import Enum
import hashlib
import sqlite3
from pathlib import Path
from typing import Optional


class ReleaseState(str, Enum):
    PREPARED = "PREPARED"
    DISPATCHING = "DISPATCHING"
    COMMITTED = "COMMITTED"
    EXTERNALIZED_UNKNOWN = "EXTERNALIZED_UNKNOWN"
    ABORTED = "ABORTED"


class LedgerDecision(str, Enum):
    PREPARED_NEW = "PREPARED_NEW"
    PREPARED_EXISTING = "PREPARED_EXISTING"
    EFFECT_ALREADY_COMMITTED = "EFFECT_ALREADY_COMMITTED"
    RECONCILE_EFFECT = "RECONCILE_EFFECT"
    BLOCK_EFFECT_IDEMPOTENCY = "BLOCK_EFFECT_IDEMPOTENCY"
    BLOCK_EFFECT_LINEAGE = "BLOCK_EFFECT_LINEAGE"
    REVALIDATE_EFFECT_LEDGER = "REVALIDATE_EFFECT_LEDGER"
    BLOCK_EFFECT_LEDGER = "BLOCK_EFFECT_LEDGER"
    TRANSITIONED = "TRANSITIONED"
    CAS_MISMATCH = "CAS_MISMATCH"
    ILLEGAL_TRANSITION = "ILLEGAL_TRANSITION"
    NOT_FOUND = "NOT_FOUND"


LEGAL_EDGES = {
    (ReleaseState.PREPARED, ReleaseState.DISPATCHING),
    (ReleaseState.PREPARED, ReleaseState.ABORTED),
    (ReleaseState.DISPATCHING, ReleaseState.COMMITTED),
    (ReleaseState.DISPATCHING, ReleaseState.EXTERNALIZED_UNKNOWN),
    (ReleaseState.EXTERNALIZED_UNKNOWN, ReleaseState.COMMITTED),
    (ReleaseState.EXTERNALIZED_UNKNOWN, ReleaseState.ABORTED),
}


@dataclass(frozen=True)
class LedgerIdentity:
    ledger_id: str
    generation: int
    version: int
    ledger_hash: str


@dataclass(frozen=True)
class EffectIntent:
    idempotency_key: str
    effect_digest: str
    transaction_id: str
    authority_id: str
    principal: str

    def __post_init__(self) -> None:
        for name in (
            "idempotency_key",
            "effect_digest",
            "transaction_id",
            "authority_id",
            "principal",
        ):
            if not getattr(self, name).strip():
                raise ValueError(f"{name} must be non-empty")


@dataclass(frozen=True)
class EffectRecord:
    record_id: int
    intent: EffectIntent
    state: ReleaseState
    record_version: int
    committed_receipt: Optional[str]


@dataclass(frozen=True)
class LedgerResult:
    decision: LedgerDecision
    ledger: LedgerIdentity
    record: Optional[EffectRecord] = None
    reason: Optional[str] = None


def _ledger_hash(ledger_id: str, generation: int, version: int) -> str:
    payload = f"{ledger_id}|{generation}|{version}".encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


class ReleaseLedgerStore:
    def __init__(self, db_path: str | Path, *, ledger_id: str = "EFFECT-LEDGER") -> None:
        self.db_path = str(db_path)
        self.ledger_id = ledger_id.strip()
        if not self.ledger_id:
            raise ValueError("ledger_id must be non-empty")
        self._initialize()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path, isolation_level=None)
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA journal_mode=WAL")
        conn.execute("PRAGMA synchronous=FULL")
        conn.execute("PRAGMA foreign_keys=ON")
        return conn

    def _initialize(self) -> None:
        with closing(self._connect()) as conn:
            conn.execute("BEGIN IMMEDIATE")
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS ledger_meta (
                    singleton INTEGER PRIMARY KEY CHECK (singleton = 1),
                    ledger_id TEXT NOT NULL,
                    generation INTEGER NOT NULL CHECK (generation >= 1),
                    version INTEGER NOT NULL CHECK (version >= 0),
                    ledger_hash TEXT NOT NULL
                )
                """
            )
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS effect_records (
                    record_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    idempotency_key TEXT NOT NULL UNIQUE,
                    effect_digest TEXT NOT NULL UNIQUE,
                    transaction_id TEXT NOT NULL,
                    authority_id TEXT NOT NULL,
                    principal TEXT NOT NULL,
                    state TEXT NOT NULL,
                    record_version INTEGER NOT NULL CHECK (record_version >= 1),
                    committed_receipt TEXT
                )
                """
            )
            row = conn.execute("SELECT * FROM ledger_meta WHERE singleton = 1").fetchone()
            if row is None:
                generation = 1
                version = 0
                conn.execute(
                    "INSERT INTO ledger_meta VALUES (1, ?, ?, ?, ?)",
                    (self.ledger_id, generation, version, _ledger_hash(self.ledger_id, generation, version)),
                )
            elif row["ledger_id"] != self.ledger_id:
                conn.execute("ROLLBACK")
                raise ValueError("existing ledger_id does not match requested ledger_id")
            conn.execute("COMMIT")

    def identity(self) -> LedgerIdentity:
        with closing(self._connect()) as conn:
            row = conn.execute("SELECT * FROM ledger_meta WHERE singleton = 1").fetchone()
            if row is None:
                raise RuntimeError("malformed ledger: missing ledger_meta")
            expected = _ledger_hash(row["ledger_id"], row["generation"], row["version"])
            if row["ledger_hash"] != expected:
                raise RuntimeError("malformed ledger: ledger_hash mismatch")
            return LedgerIdentity(row["ledger_id"], row["generation"], row["version"], row["ledger_hash"])

    def _identity_locked(self, conn: sqlite3.Connection) -> LedgerIdentity:
        row = conn.execute("SELECT * FROM ledger_meta WHERE singleton = 1").fetchone()
        if row is None:
            raise RuntimeError("malformed ledger: missing ledger_meta")
        expected = _ledger_hash(row["ledger_id"], row["generation"], row["version"])
        if row["ledger_hash"] != expected:
            raise RuntimeError("malformed ledger: ledger_hash mismatch")
        return LedgerIdentity(row["ledger_id"], row["generation"], row["version"], row["ledger_hash"])

    def _bump_ledger_locked(self, conn: sqlite3.Connection, current: LedgerIdentity) -> LedgerIdentity:
        new_version = current.version + 1
        new_hash = _ledger_hash(current.ledger_id, current.generation, new_version)
        cur = conn.execute(
            """
            UPDATE ledger_meta
               SET version = ?, ledger_hash = ?
             WHERE singleton = 1
               AND ledger_id = ?
               AND generation = ?
               AND version = ?
               AND ledger_hash = ?
            """,
            (
                new_version,
                new_hash,
                current.ledger_id,
                current.generation,
                current.version,
                current.ledger_hash,
            ),
        )
        if cur.rowcount != 1:
            raise RuntimeError("ledger CAS failed")
        return LedgerIdentity(current.ledger_id, current.generation, new_version, new_hash)

    @staticmethod
    def _record_from_row(row: sqlite3.Row) -> EffectRecord:
        return EffectRecord(
            record_id=row["record_id"],
            intent=EffectIntent(
                row["idempotency_key"],
                row["effect_digest"],
                row["transaction_id"],
                row["authority_id"],
                row["principal"],
            ),
            state=ReleaseState(row["state"]),
            record_version=row["record_version"],
            committed_receipt=row["committed_receipt"],
        )

    def get_by_key(self, idempotency_key: str) -> Optional[EffectRecord]:
        with closing(self._connect()) as conn:
            row = conn.execute(
                "SELECT * FROM effect_records WHERE idempotency_key = ?",
                (idempotency_key,),
            ).fetchone()
            return None if row is None else self._record_from_row(row)

    def prepare(self, intent: EffectIntent) -> LedgerResult:
        with closing(self._connect()) as conn:
            conn.execute("BEGIN IMMEDIATE")
            ledger = self._identity_locked(conn)
            by_key = conn.execute(
                "SELECT * FROM effect_records WHERE idempotency_key = ?",
                (intent.idempotency_key,),
            ).fetchone()
            by_digest = conn.execute(
                "SELECT * FROM effect_records WHERE effect_digest = ?",
                (intent.effect_digest,),
            ).fetchone()

            if by_key is not None and by_key["effect_digest"] != intent.effect_digest:
                conn.execute("ROLLBACK")
                return LedgerResult(LedgerDecision.BLOCK_EFFECT_IDEMPOTENCY, ledger, reason="same_key_different_digest")
            if by_digest is not None and by_digest["idempotency_key"] != intent.idempotency_key:
                conn.execute("ROLLBACK")
                return LedgerResult(LedgerDecision.BLOCK_EFFECT_IDEMPOTENCY, ledger, reason="same_digest_different_key")

            row = by_key or by_digest
            if row is not None:
                record = self._record_from_row(row)
                if (
                    record.intent.transaction_id != intent.transaction_id
                    or record.intent.authority_id != intent.authority_id
                    or record.intent.principal != intent.principal
                ):
                    conn.execute("ROLLBACK")
                    return LedgerResult(LedgerDecision.BLOCK_EFFECT_LINEAGE, ledger, record, "lineage_mismatch")
                conn.execute("ROLLBACK")
                if record.state is ReleaseState.COMMITTED and record.committed_receipt:
                    return LedgerResult(LedgerDecision.EFFECT_ALREADY_COMMITTED, ledger, record)
                if record.state in {ReleaseState.DISPATCHING, ReleaseState.EXTERNALIZED_UNKNOWN}:
                    return LedgerResult(LedgerDecision.RECONCILE_EFFECT, ledger, record)
                return LedgerResult(LedgerDecision.PREPARED_EXISTING, ledger, record)

            conn.execute(
                """
                INSERT INTO effect_records (
                    idempotency_key, effect_digest, transaction_id, authority_id,
                    principal, state, record_version, committed_receipt
                ) VALUES (?, ?, ?, ?, ?, ?, 1, NULL)
                """,
                (
                    intent.idempotency_key,
                    intent.effect_digest,
                    intent.transaction_id,
                    intent.authority_id,
                    intent.principal,
                    ReleaseState.PREPARED.value,
                ),
            )
            row = conn.execute("SELECT * FROM effect_records WHERE record_id = last_insert_rowid()").fetchone()
            new_ledger = self._bump_ledger_locked(conn, ledger)
            conn.execute("COMMIT")
            return LedgerResult(LedgerDecision.PREPARED_NEW, new_ledger, self._record_from_row(row))

    def transition(
        self,
        *,
        record_id: int,
        expected_record_version: int,
        expected_ledger_generation: int,
        expected_ledger_version: int,
        to_state: ReleaseState,
        committed_receipt: Optional[str] = None,
    ) -> LedgerResult:
        with closing(self._connect()) as conn:
            conn.execute("BEGIN IMMEDIATE")
            ledger = self._identity_locked(conn)
            if ledger.generation != expected_ledger_generation:
                conn.execute("ROLLBACK")
                return LedgerResult(LedgerDecision.REVALIDATE_EFFECT_LEDGER, ledger, reason="ledger_generation_changed")
            if ledger.version != expected_ledger_version:
                conn.execute("ROLLBACK")
                return LedgerResult(LedgerDecision.CAS_MISMATCH, ledger, reason="ledger_version_changed")

            row = conn.execute("SELECT * FROM effect_records WHERE record_id = ?", (record_id,)).fetchone()
            if row is None:
                conn.execute("ROLLBACK")
                return LedgerResult(LedgerDecision.NOT_FOUND, ledger)
            record = self._record_from_row(row)
            if record.record_version != expected_record_version:
                conn.execute("ROLLBACK")
                return LedgerResult(LedgerDecision.CAS_MISMATCH, ledger, record, "record_version_changed")
            if (record.state, to_state) not in LEGAL_EDGES:
                conn.execute("ROLLBACK")
                return LedgerResult(LedgerDecision.ILLEGAL_TRANSITION, ledger, record)
            if to_state is ReleaseState.COMMITTED and not (committed_receipt or "").strip():
                conn.execute("ROLLBACK")
                return LedgerResult(LedgerDecision.BLOCK_EFFECT_LEDGER, ledger, record, "committed_receipt_required")
            if to_state is not ReleaseState.COMMITTED and committed_receipt is not None:
                conn.execute("ROLLBACK")
                return LedgerResult(LedgerDecision.BLOCK_EFFECT_LEDGER, ledger, record, "receipt_only_valid_for_commit")

            new_record_version = record.record_version + 1
            cur = conn.execute(
                """
                UPDATE effect_records
                   SET state = ?, record_version = ?, committed_receipt = ?
                 WHERE record_id = ? AND record_version = ? AND state = ?
                """,
                (
                    to_state.value,
                    new_record_version,
                    committed_receipt,
                    record.record_id,
                    record.record_version,
                    record.state.value,
                ),
            )
            if cur.rowcount != 1:
                conn.execute("ROLLBACK")
                return LedgerResult(LedgerDecision.CAS_MISMATCH, ledger, record, "record_cas_failed")

            new_ledger = self._bump_ledger_locked(conn, ledger)
            new_row = conn.execute("SELECT * FROM effect_records WHERE record_id = ?", (record_id,)).fetchone()
            conn.execute("COMMIT")
            return LedgerResult(LedgerDecision.TRANSITIONED, new_ledger, self._record_from_row(new_row))

    def recreate_generation(self) -> LedgerIdentity:
        """Administrative local reference: new ledger incarnation, records cleared."""
        with closing(self._connect()) as conn:
            conn.execute("BEGIN IMMEDIATE")
            current = self._identity_locked(conn)
            generation = current.generation + 1
            version = 0
            new_hash = _ledger_hash(current.ledger_id, generation, version)
            conn.execute("DELETE FROM effect_records")
            conn.execute(
                "UPDATE ledger_meta SET generation = ?, version = ?, ledger_hash = ? WHERE singleton = 1",
                (generation, version, new_hash),
            )
            conn.execute("COMMIT")
            return LedgerIdentity(current.ledger_id, generation, version, new_hash)
