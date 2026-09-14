from __future__ import annotations

import hashlib
import json
import sqlite3
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any, Callable, Optional


class WorkflowError(RuntimeError):
    pass


class ReplayDivergence(WorkflowError):
    pass


class VersionMismatch(WorkflowError):
    pass


class AmbiguousEffect(WorkflowError):
    pass


class IntegrityViolation(WorkflowError):
    pass


class StepKind(str, Enum):
    PURE = "PURE"
    EFFECT = "EFFECT"


class StepStatus(str, Enum):
    STARTED = "STARTED"
    COMPLETED = "COMPLETED"
    RETRYABLE = "RETRYABLE"
    AMBIGUOUS = "AMBIGUOUS"


class RunStatus(str, Enum):
    RUNNING = "RUNNING"
    CONTINUED_AS_NEW = "CONTINUED_AS_NEW"
    COMPLETED = "COMPLETED"
    BLOCKED = "BLOCKED"


def _json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _hash_text(value: str) -> str:
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _hash_json(value: Any) -> str:
    return _hash_text(_json(value))


@dataclass(frozen=True)
class RunRef:
    workflow_id: str
    run_id: int


class DurableWorkflowStore:
    """Local durable-execution reference implementation for AMOS.

    Scope: SQLite-backed replay/checkpoint semantics and failure handling.
    This is not a distributed consensus engine and grants no execution authority.
    """

    def __init__(self, database: str | Path = ":memory:") -> None:
        self.database = str(database)
        self.conn = sqlite3.connect(self.database)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA foreign_keys = ON")
        self._init_schema()

    def close(self) -> None:
        self.conn.close()

    def _init_schema(self) -> None:
        self.conn.executescript(
            """
            CREATE TABLE IF NOT EXISTS workflow_runs (
                workflow_id TEXT NOT NULL,
                run_id INTEGER NOT NULL,
                parent_run_id INTEGER,
                code_version TEXT NOT NULL,
                status TEXT NOT NULL,
                explicit_state_json TEXT NOT NULL,
                explicit_state_hash TEXT NOT NULL,
                PRIMARY KEY (workflow_id, run_id)
            );

            CREATE TABLE IF NOT EXISTS workflow_steps (
                workflow_id TEXT NOT NULL,
                run_id INTEGER NOT NULL,
                step_id TEXT NOT NULL,
                kind TEXT NOT NULL,
                input_hash TEXT NOT NULL,
                effect_key TEXT,
                status TEXT NOT NULL,
                attempt INTEGER NOT NULL,
                output_json TEXT,
                output_hash TEXT,
                error TEXT,
                PRIMARY KEY (workflow_id, run_id, step_id),
                FOREIGN KEY (workflow_id, run_id)
                  REFERENCES workflow_runs(workflow_id, run_id)
            );

            CREATE TABLE IF NOT EXISTS workflow_events (
                workflow_id TEXT NOT NULL,
                run_id INTEGER NOT NULL,
                seq INTEGER NOT NULL,
                event_type TEXT NOT NULL,
                payload_json TEXT NOT NULL,
                prev_hash TEXT NOT NULL,
                event_hash TEXT NOT NULL,
                PRIMARY KEY (workflow_id, run_id, seq),
                FOREIGN KEY (workflow_id, run_id)
                  REFERENCES workflow_runs(workflow_id, run_id)
            );

            CREATE TABLE IF NOT EXISTS version_patches (
                workflow_id TEXT NOT NULL,
                from_version TEXT NOT NULL,
                to_version TEXT NOT NULL,
                patch_id TEXT NOT NULL,
                PRIMARY KEY (workflow_id, from_version, to_version)
            );
            """
        )
        self.conn.commit()

    def start(self, workflow_id: str, code_version: str, state: Any) -> RunRef:
        row = self.conn.execute(
            "SELECT COALESCE(MAX(run_id), 0) AS n FROM workflow_runs WHERE workflow_id=?",
            (workflow_id,),
        ).fetchone()
        run_id = int(row["n"]) + 1
        state_json = _json(state)
        self.conn.execute(
            """
            INSERT INTO workflow_runs(
                workflow_id, run_id, parent_run_id, code_version, status,
                explicit_state_json, explicit_state_hash
            ) VALUES (?, ?, NULL, ?, ?, ?, ?)
            """,
            (
                workflow_id,
                run_id,
                code_version,
                RunStatus.RUNNING.value,
                state_json,
                _hash_text(state_json),
            ),
        )
        self._append_event(
            workflow_id,
            run_id,
            "RUN_STARTED",
            {"code_version": code_version, "state_hash": _hash_text(state_json)},
        )
        self.conn.commit()
        return RunRef(workflow_id, run_id)

    def register_patch(
        self, workflow_id: str, from_version: str, to_version: str, patch_id: str
    ) -> None:
        if not patch_id.strip():
            raise ValueError("patch_id is required")
        self.conn.execute(
            """
            INSERT OR REPLACE INTO version_patches(
                workflow_id, from_version, to_version, patch_id
            ) VALUES (?, ?, ?, ?)
            """,
            (workflow_id, from_version, to_version, patch_id),
        )
        self.conn.commit()

    def resume(self, ref: RunRef, code_version: str) -> dict[str, Any]:
        self.verify_integrity(ref)
        row = self._run_row(ref)
        stored = row["code_version"]
        if stored != code_version:
            patch = self.conn.execute(
                """
                SELECT patch_id FROM version_patches
                WHERE workflow_id=? AND from_version=? AND to_version=?
                """,
                (ref.workflow_id, stored, code_version),
            ).fetchone()
            if patch is None:
                raise VersionMismatch(
                    f"workflow code changed from {stored} to {code_version} without compatibility patch"
                )
            self.conn.execute(
                "UPDATE workflow_runs SET code_version=? WHERE workflow_id=? AND run_id=?",
                (code_version, ref.workflow_id, ref.run_id),
            )
            self._append_event(
                ref.workflow_id,
                ref.run_id,
                "VERSION_PATCH_APPLIED",
                {
                    "from_version": stored,
                    "to_version": code_version,
                    "patch_id": patch["patch_id"],
                },
            )
            self.conn.commit()
        return self.snapshot(ref)

    def execute_step(
        self,
        ref: RunRef,
        step_id: str,
        kind: StepKind,
        input_value: Any,
        fn: Callable[[Any], Any],
        *,
        effect_key: Optional[str] = None,
        simulate_interrupt_after_start: bool = False,
    ) -> Any:
        self.verify_integrity(ref)
        run = self._run_row(ref)
        if run["status"] != RunStatus.RUNNING.value:
            raise WorkflowError(f"run is not executable: {run['status']}")

        input_hash = _hash_json(input_value)
        existing = self.conn.execute(
            """
            SELECT * FROM workflow_steps
            WHERE workflow_id=? AND run_id=? AND step_id=?
            """,
            (ref.workflow_id, ref.run_id, step_id),
        ).fetchone()

        if existing is not None:
            self._validate_step_identity(existing, kind, input_hash, effect_key)
            if existing["status"] == StepStatus.COMPLETED.value:
                return json.loads(existing["output_json"])
            if kind == StepKind.EFFECT and existing["status"] in {
                StepStatus.STARTED.value,
                StepStatus.AMBIGUOUS.value,
            }:
                if existing["status"] != StepStatus.AMBIGUOUS.value:
                    self.conn.execute(
                        """
                        UPDATE workflow_steps SET status=?
                        WHERE workflow_id=? AND run_id=? AND step_id=?
                        """,
                        (
                            StepStatus.AMBIGUOUS.value,
                            ref.workflow_id,
                            ref.run_id,
                            step_id,
                        ),
                    )
                    self._append_event(
                        ref.workflow_id,
                        ref.run_id,
                        "EFFECT_AMBIGUOUS",
                        {"step_id": step_id, "effect_key": effect_key},
                    )
                    self.conn.commit()
                raise AmbiguousEffect(
                    f"effect step {step_id} started without durable completion receipt"
                )
            if existing["status"] == StepStatus.RETRYABLE.value or kind == StepKind.PURE:
                self.conn.execute(
                    """
                    UPDATE workflow_steps SET status=?, attempt=attempt+1, error=NULL
                    WHERE workflow_id=? AND run_id=? AND step_id=?
                    """,
                    (
                        StepStatus.STARTED.value,
                        ref.workflow_id,
                        ref.run_id,
                        step_id,
                    ),
                )
        else:
            if kind == StepKind.EFFECT:
                if not effect_key:
                    raise ValueError("effect steps require an explicit effect_key")
                prior = self.conn.execute(
                    """
                    SELECT * FROM workflow_steps
                    WHERE workflow_id=? AND effect_key=? AND status=?
                    ORDER BY run_id, step_id LIMIT 1
                    """,
                    (
                        ref.workflow_id,
                        effect_key,
                        StepStatus.COMPLETED.value,
                    ),
                ).fetchone()
                if prior is not None:
                    if prior["input_hash"] != input_hash:
                        raise ReplayDivergence(
                            "effect_key reused with different input; refusing ambiguous deduplication"
                        )
                    output_json = prior["output_json"]
                    output_hash = prior["output_hash"]
                    self.conn.execute(
                        """
                        INSERT INTO workflow_steps(
                            workflow_id, run_id, step_id, kind, input_hash,
                            effect_key, status, attempt, output_json, output_hash, error
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, 0, ?, ?, NULL)
                        """,
                        (
                            ref.workflow_id,
                            ref.run_id,
                            step_id,
                            kind.value,
                            input_hash,
                            effect_key,
                            StepStatus.COMPLETED.value,
                            output_json,
                            output_hash,
                        ),
                    )
                    self._append_event(
                        ref.workflow_id,
                        ref.run_id,
                        "EFFECT_RECEIPT_REUSED",
                        {
                            "step_id": step_id,
                            "effect_key": effect_key,
                            "output_hash": output_hash,
                        },
                    )
                    self.conn.commit()
                    return json.loads(output_json)

            self.conn.execute(
                """
                INSERT INTO workflow_steps(
                    workflow_id, run_id, step_id, kind, input_hash, effect_key,
                    status, attempt, output_json, output_hash, error
                ) VALUES (?, ?, ?, ?, ?, ?, ?, 1, NULL, NULL, NULL)
                """,
                (
                    ref.workflow_id,
                    ref.run_id,
                    step_id,
                    kind.value,
                    input_hash,
                    effect_key,
                    StepStatus.STARTED.value,
                ),
            )

        self._append_event(
            ref.workflow_id,
            ref.run_id,
            "STEP_STARTED",
            {
                "step_id": step_id,
                "kind": kind.value,
                "input_hash": input_hash,
                "effect_key": effect_key,
            },
        )
        self.conn.commit()

        if simulate_interrupt_after_start:
            raise WorkflowError("simulated interruption after durable STARTED record")

        try:
            output = fn(input_value)
        except Exception as exc:
            if kind == StepKind.EFFECT:
                status = StepStatus.AMBIGUOUS.value
                event_type = "EFFECT_AMBIGUOUS"
            else:
                status = StepStatus.RETRYABLE.value
                event_type = "PURE_STEP_RETRYABLE"
            self.conn.execute(
                """
                UPDATE workflow_steps SET status=?, error=?
                WHERE workflow_id=? AND run_id=? AND step_id=?
                """,
                (status, repr(exc), ref.workflow_id, ref.run_id, step_id),
            )
            self._append_event(
                ref.workflow_id,
                ref.run_id,
                event_type,
                {"step_id": step_id, "error_type": type(exc).__name__},
            )
            self.conn.commit()
            if kind == StepKind.EFFECT:
                raise AmbiguousEffect(
                    f"effect step {step_id} raised after dispatch; reconcile before retry"
                ) from exc
            raise

        output_json = _json(output)
        output_hash = _hash_text(output_json)
        self.conn.execute(
            """
            UPDATE workflow_steps
            SET status=?, output_json=?, output_hash=?, error=NULL
            WHERE workflow_id=? AND run_id=? AND step_id=?
            """,
            (
                StepStatus.COMPLETED.value,
                output_json,
                output_hash,
                ref.workflow_id,
                ref.run_id,
                step_id,
            ),
        )
        self._append_event(
            ref.workflow_id,
            ref.run_id,
            "EFFECT_RECEIPT" if kind == StepKind.EFFECT else "STEP_COMPLETED",
            {
                "step_id": step_id,
                "effect_key": effect_key,
                "output_hash": output_hash,
            },
        )
        self.conn.commit()
        return output

    def reconcile_effect(
        self, ref: RunRef, step_id: str, outcome: str, output: Any = None
    ) -> None:
        self.verify_integrity(ref)
        row = self.conn.execute(
            """
            SELECT * FROM workflow_steps
            WHERE workflow_id=? AND run_id=? AND step_id=?
            """,
            (ref.workflow_id, ref.run_id, step_id),
        ).fetchone()
        if row is None or row["kind"] != StepKind.EFFECT.value:
            raise WorkflowError("reconciliation target is not an effect step")
        if row["status"] not in {
            StepStatus.STARTED.value,
            StepStatus.AMBIGUOUS.value,
        }:
            raise WorkflowError(f"effect is not reconcilable from status {row['status']}")

        normalized = outcome.upper()
        if normalized == "COMPLETED":
            output_json = _json(output)
            output_hash = _hash_text(output_json)
            self.conn.execute(
                """
                UPDATE workflow_steps
                SET status=?, output_json=?, output_hash=?, error=NULL
                WHERE workflow_id=? AND run_id=? AND step_id=?
                """,
                (
                    StepStatus.COMPLETED.value,
                    output_json,
                    output_hash,
                    ref.workflow_id,
                    ref.run_id,
                    step_id,
                ),
            )
            payload = {
                "step_id": step_id,
                "outcome": normalized,
                "output_hash": output_hash,
            }
        elif normalized == "NOT_APPLIED":
            self.conn.execute(
                """
                UPDATE workflow_steps SET status=?, error=NULL
                WHERE workflow_id=? AND run_id=? AND step_id=?
                """,
                (
                    StepStatus.RETRYABLE.value,
                    ref.workflow_id,
                    ref.run_id,
                    step_id,
                ),
            )
            payload = {"step_id": step_id, "outcome": normalized}
        else:
            raise ValueError("outcome must be COMPLETED or NOT_APPLIED")

        self._append_event(ref.workflow_id, ref.run_id, "EFFECT_RECONCILED", payload)
        self.conn.commit()

    def continue_as_new(
        self, ref: RunRef, new_code_version: str, carry_state: Any
    ) -> RunRef:
        self.verify_integrity(ref)
        ambiguous = self.conn.execute(
            """
            SELECT COUNT(*) AS n FROM workflow_steps
            WHERE workflow_id=? AND run_id=? AND status=?
            """,
            (ref.workflow_id, ref.run_id, StepStatus.AMBIGUOUS.value),
        ).fetchone()["n"]
        started_effects = self.conn.execute(
            """
            SELECT COUNT(*) AS n FROM workflow_steps
            WHERE workflow_id=? AND run_id=? AND kind=? AND status=?
            """,
            (
                ref.workflow_id,
                ref.run_id,
                StepKind.EFFECT.value,
                StepStatus.STARTED.value,
            ),
        ).fetchone()["n"]
        if ambiguous or started_effects:
            raise AmbiguousEffect("cannot continue-as-new with unresolved effects")

        current = self._run_row(ref)
        if current["status"] != RunStatus.RUNNING.value:
            raise WorkflowError(f"run is not continuable: {current['status']}")

        state_json = _json(carry_state)
        next_run_id = ref.run_id + 1
        exists = self.conn.execute(
            "SELECT 1 FROM workflow_runs WHERE workflow_id=? AND run_id=?",
            (ref.workflow_id, next_run_id),
        ).fetchone()
        if exists:
            raise WorkflowError("next run already exists")

        parent_final_hash = self._last_event_hash(ref)
        self.conn.execute(
            """
            UPDATE workflow_runs SET status=?
            WHERE workflow_id=? AND run_id=?
            """,
            (RunStatus.CONTINUED_AS_NEW.value, ref.workflow_id, ref.run_id),
        )
        self._append_event(
            ref.workflow_id,
            ref.run_id,
            "CONTINUED_AS_NEW",
            {
                "next_run_id": next_run_id,
                "carry_state_hash": _hash_text(state_json),
            },
        )
        self.conn.execute(
            """
            INSERT INTO workflow_runs(
                workflow_id, run_id, parent_run_id, code_version, status,
                explicit_state_json, explicit_state_hash
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                ref.workflow_id,
                next_run_id,
                ref.run_id,
                new_code_version,
                RunStatus.RUNNING.value,
                state_json,
                _hash_text(state_json),
            ),
        )
        self._append_event(
            ref.workflow_id,
            next_run_id,
            "RUN_STARTED_FROM_PARENT",
            {
                "parent_run_id": ref.run_id,
                "parent_event_hash": parent_final_hash,
                "code_version": new_code_version,
                "state_hash": _hash_text(state_json),
            },
        )
        self.conn.commit()
        return RunRef(ref.workflow_id, next_run_id)

    def complete(self, ref: RunRef) -> None:
        self.verify_integrity(ref)
        unresolved = self.conn.execute(
            """
            SELECT COUNT(*) AS n FROM workflow_steps
            WHERE workflow_id=? AND run_id=? AND status IN (?, ?)
            """,
            (
                ref.workflow_id,
                ref.run_id,
                StepStatus.AMBIGUOUS.value,
                StepStatus.STARTED.value,
            ),
        ).fetchone()["n"]
        if unresolved:
            raise WorkflowError("cannot complete with unresolved steps")
        self.conn.execute(
            "UPDATE workflow_runs SET status=? WHERE workflow_id=? AND run_id=?",
            (RunStatus.COMPLETED.value, ref.workflow_id, ref.run_id),
        )
        self._append_event(ref.workflow_id, ref.run_id, "RUN_COMPLETED", {})
        self.conn.commit()

    def snapshot(self, ref: RunRef) -> dict[str, Any]:
        run = self._run_row(ref)
        steps = self.conn.execute(
            """
            SELECT step_id, kind, input_hash, effect_key, status, attempt,
                   output_json, output_hash, error
            FROM workflow_steps
            WHERE workflow_id=? AND run_id=? ORDER BY step_id
            """,
            (ref.workflow_id, ref.run_id),
        ).fetchall()
        return {
            "workflow_id": ref.workflow_id,
            "run_id": ref.run_id,
            "parent_run_id": run["parent_run_id"],
            "code_version": run["code_version"],
            "status": run["status"],
            "explicit_state": json.loads(run["explicit_state_json"]),
            "explicit_state_hash": run["explicit_state_hash"],
            "steps": [
                {
                    "step_id": row["step_id"],
                    "kind": row["kind"],
                    "input_hash": row["input_hash"],
                    "effect_key": row["effect_key"],
                    "status": row["status"],
                    "attempt": row["attempt"],
                    "output": json.loads(row["output_json"])
                    if row["output_json"]
                    else None,
                    "output_hash": row["output_hash"],
                    "error": row["error"],
                }
                for row in steps
            ],
            "event_head": self._last_event_hash(ref),
        }

    def verify_integrity(self, ref: RunRef) -> None:
        run = self._run_row(ref)
        if _hash_text(run["explicit_state_json"]) != run["explicit_state_hash"]:
            raise IntegrityViolation("explicit state hash mismatch")

        prev = "GENESIS"
        events = self.conn.execute(
            """
            SELECT seq, event_type, payload_json, prev_hash, event_hash
            FROM workflow_events
            WHERE workflow_id=? AND run_id=? ORDER BY seq
            """,
            (ref.workflow_id, ref.run_id),
        ).fetchall()
        expected_seq = 1
        for event in events:
            if event["seq"] != expected_seq:
                raise IntegrityViolation("event sequence gap")
            if event["prev_hash"] != prev:
                raise IntegrityViolation("event prev_hash mismatch")
            material = f"{prev}|{event['event_type']}|{event['payload_json']}"
            expected_hash = _hash_text(material)
            if event["event_hash"] != expected_hash:
                raise IntegrityViolation("event hash mismatch")
            prev = event["event_hash"]
            expected_seq += 1

        completed = self.conn.execute(
            """
            SELECT output_json, output_hash FROM workflow_steps
            WHERE workflow_id=? AND run_id=? AND status=?
            """,
            (ref.workflow_id, ref.run_id, StepStatus.COMPLETED.value),
        ).fetchall()
        for step in completed:
            if step["output_json"] is None or step["output_hash"] is None:
                raise IntegrityViolation("completed step missing output receipt")
            if _hash_text(step["output_json"]) != step["output_hash"]:
                raise IntegrityViolation("step output hash mismatch")

    def _validate_step_identity(
        self,
        row: sqlite3.Row,
        kind: StepKind,
        input_hash: str,
        effect_key: Optional[str],
    ) -> None:
        if row["kind"] != kind.value:
            raise ReplayDivergence("step kind changed across replay")
        if row["input_hash"] != input_hash:
            raise ReplayDivergence("step input changed across replay")
        if kind == StepKind.EFFECT and row["effect_key"] != effect_key:
            raise ReplayDivergence("effect key changed across replay")

    def _run_row(self, ref: RunRef) -> sqlite3.Row:
        row = self.conn.execute(
            "SELECT * FROM workflow_runs WHERE workflow_id=? AND run_id=?",
            (ref.workflow_id, ref.run_id),
        ).fetchone()
        if row is None:
            raise WorkflowError(f"unknown workflow run: {ref}")
        return row

    def _last_event_hash(self, ref: RunRef) -> str:
        row = self.conn.execute(
            """
            SELECT event_hash FROM workflow_events
            WHERE workflow_id=? AND run_id=? ORDER BY seq DESC LIMIT 1
            """,
            (ref.workflow_id, ref.run_id),
        ).fetchone()
        return row["event_hash"] if row else "GENESIS"

    def _append_event(
        self, workflow_id: str, run_id: int, event_type: str, payload: Any
    ) -> None:
        row = self.conn.execute(
            """
            SELECT seq, event_hash FROM workflow_events
            WHERE workflow_id=? AND run_id=? ORDER BY seq DESC LIMIT 1
            """,
            (workflow_id, run_id),
        ).fetchone()
        seq = (row["seq"] + 1) if row else 1
        prev_hash = row["event_hash"] if row else "GENESIS"
        payload_json = _json(payload)
        event_hash = _hash_text(f"{prev_hash}|{event_type}|{payload_json}")
        self.conn.execute(
            """
            INSERT INTO workflow_events(
                workflow_id, run_id, seq, event_type, payload_json,
                prev_hash, event_hash
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                workflow_id,
                run_id,
                seq,
                event_type,
                payload_json,
                prev_hash,
                event_hash,
            ),
        )
