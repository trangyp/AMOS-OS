#!/usr/bin/env python3
from __future__ import annotations

import argparse, hashlib, json, sqlite3, time, uuid
from pathlib import Path
from typing import Any

STATES = {"STABLE", "LOCAL_RECOVERY", "ASSISTED_RECOVERY", "SUSPENDED", "SURRENDERED"}
EVIDENCE = {
    "SOFT_DEGRADATION", "RECOVERY_FAILURE", "RECOVERY_SUCCESS", "PERSISTENT_DISAGREEMENT",
    "EVIDENCE_GAP", "HARD_INVARIANT_FAILURE", "AUTHORITY_STALE", "EXTERNAL_BLOCK",
    "ASSISTED_APPROVAL", "ASSISTED_DENIAL"
}
OUTPUTS = {
    "CONTINUE_STABLE", "ENTER_LOCAL_RECOVERY", "REQUIRE_ASSISTED_RECOVERY", "SUSPEND_AUTONOMY",
    "SURRENDER_AUTONOMY", "RESUME_STABLE", "REMAIN_CONTAINED", "UNKNOWN_GAP"
}
SEMANTICS = "LIFECYCLE_DECISION_DOES_NOT_GRANT_EXECUTION_OR_COMMIT_AUTHORITY"

class LifecycleError(RuntimeError): pass

def canon(v: Any) -> str:
    return json.dumps(v, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

def sha(v: Any) -> str:
    return hashlib.sha256(canon(v).encode()).hexdigest()

def now_ns() -> int:
    return time.time_ns()

class Runtime:
    def __init__(self, db: str | Path = ":memory:"):
        self.db = sqlite3.connect(str(db))
        self.db.row_factory = sqlite3.Row
        self.db.executescript("""
        PRAGMA foreign_keys=ON;
        CREATE TABLE IF NOT EXISTS lifecycle(
          id TEXT PRIMARY KEY, agent_id TEXT NOT NULL, state TEXT NOT NULL,
          max_local INTEGER NOT NULL, max_assisted INTEGER NOT NULL,
          local_attempts INTEGER NOT NULL DEFAULT 0, assisted_attempts INTEGER NOT NULL DEFAULT 0,
          policy_epoch INTEGER NOT NULL, authority_epoch INTEGER NOT NULL,
          fence_epoch INTEGER NOT NULL DEFAULT 0, terminal INTEGER NOT NULL DEFAULT 0,
          created_ns INTEGER NOT NULL, updated_ns INTEGER NOT NULL
        );
        CREATE TABLE IF NOT EXISTS evidence(
          seq INTEGER PRIMARY KEY AUTOINCREMENT, lifecycle_id TEXT NOT NULL, kind TEXT NOT NULL,
          evidence_ref TEXT NOT NULL, policy_epoch INTEGER NOT NULL, authority_epoch INTEGER NOT NULL,
          created_ns INTEGER NOT NULL,
          FOREIGN KEY(lifecycle_id) REFERENCES lifecycle(id)
        );
        CREATE TABLE IF NOT EXISTS transitions(
          seq INTEGER PRIMARY KEY AUTOINCREMENT, lifecycle_id TEXT NOT NULL, from_state TEXT NOT NULL,
          to_state TEXT NOT NULL, output TEXT NOT NULL, fence_epoch INTEGER NOT NULL,
          reason_hash TEXT NOT NULL, created_ns INTEGER NOT NULL,
          FOREIGN KEY(lifecycle_id) REFERENCES lifecycle(id)
        );
        CREATE TABLE IF NOT EXISTS ledger(
          seq INTEGER PRIMARY KEY AUTOINCREMENT, prev_hash TEXT NOT NULL, payload TEXT NOT NULL, entry_hash TEXT NOT NULL
        );
        """)

    def close(self): self.db.close()
    def __enter__(self): return self
    def __exit__(self, *exc): self.close()

    def _ledger(self, payload: dict[str, Any]):
        row = self.db.execute("SELECT entry_hash FROM ledger ORDER BY seq DESC LIMIT 1").fetchone()
        prev = row[0] if row else "0" * 64
        entry = sha({"prev_hash": prev, "payload": payload})
        self.db.execute("INSERT INTO ledger(prev_hash,payload,entry_hash) VALUES(?,?,?)", (prev, canon(payload), entry))

    def create(self, agent_id: str, *, max_local: int = 2, max_assisted: int = 2,
               policy_epoch: int = 1, authority_epoch: int = 1) -> str:
        if not agent_id or max_local < 0 or max_assisted < 0 or policy_epoch < 1 or authority_epoch < 1:
            raise LifecycleError("invalid lifecycle configuration")
        lid = str(uuid.uuid4()); ts = now_ns()
        self.db.execute("INSERT INTO lifecycle VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (lid, agent_id, "STABLE", max_local, max_assisted, 0, 0, policy_epoch, authority_epoch, 0, 0, ts, ts))
        self._ledger({"op":"create","id":lid,"agent_id":agent_id,"policy_epoch":policy_epoch,"authority_epoch":authority_epoch})
        self.db.commit(); return lid

    def add_evidence(self, lid: str, kind: str, ref: str, *, policy_epoch: int, authority_epoch: int):
        if kind not in EVIDENCE or not ref:
            raise LifecycleError("invalid evidence")
        self._get(lid)
        self.db.execute("INSERT INTO evidence(lifecycle_id,kind,evidence_ref,policy_epoch,authority_epoch,created_ns) VALUES(?,?,?,?,?,?)",
                        (lid, kind, ref, policy_epoch, authority_epoch, now_ns()))
        self._ledger({"op":"evidence","id":lid,"kind":kind,"ref":ref,"policy_epoch":policy_epoch,"authority_epoch":authority_epoch})
        self.db.commit()

    def update_epochs(self, lid: str, *, policy_epoch: int | None = None, authority_epoch: int | None = None):
        row = self._get(lid)
        p = row["policy_epoch"] if policy_epoch is None else policy_epoch
        a = row["authority_epoch"] if authority_epoch is None else authority_epoch
        if p < row["policy_epoch"] or a < row["authority_epoch"]:
            raise LifecycleError("epoch rollback forbidden")
        self.db.execute("UPDATE lifecycle SET policy_epoch=?,authority_epoch=?,updated_ns=? WHERE id=?", (p,a,now_ns(),lid))
        self._ledger({"op":"epochs","id":lid,"policy_epoch":p,"authority_epoch":a}); self.db.commit()

    def _get(self, lid: str):
        row = self.db.execute("SELECT * FROM lifecycle WHERE id=?", (lid,)).fetchone()
        if not row: raise LifecycleError("unknown lifecycle")
        return row

    def _latest_kinds(self, lid: str) -> set[str]:
        return {r[0] for r in self.db.execute("SELECT kind FROM evidence WHERE lifecycle_id=?", (lid,))}

    def decide(self, lid: str) -> dict[str, Any]:
        row = self._get(lid); kinds = self._latest_kinds(lid); state = row["state"]
        if row["terminal"] or state == "SURRENDERED":
            return self._receipt(row, "SURRENDERED", "SURRENDER_AUTONOMY", "terminal lifecycle")
        stale = self.db.execute("SELECT 1 FROM evidence WHERE lifecycle_id=? AND (policy_epoch<>? OR authority_epoch<>?) LIMIT 1",
                                (lid,row["policy_epoch"],row["authority_epoch"])).fetchone() is not None
        if "ASSISTED_DENIAL" in kinds:
            return self._receipt(row, "SURRENDERED", "SURRENDER_AUTONOMY", "assisted denial")
        if state == "SUSPENDED":
            hard_block = "HARD_INVARIANT_FAILURE" in kinds or "AUTHORITY_STALE" in kinds or "EXTERNAL_BLOCK" in kinds or stale
            if not hard_block and "ASSISTED_APPROVAL" in kinds and "RECOVERY_SUCCESS" in kinds:
                return self._receipt(row, "STABLE", "RESUME_STABLE", "approved recovered suspension")
            return self._receipt(row, "SUSPENDED", "REMAIN_CONTAINED", "suspension not cleared")
        if "HARD_INVARIANT_FAILURE" in kinds or "AUTHORITY_STALE" in kinds or "EXTERNAL_BLOCK" in kinds or stale:
            return self._receipt(row, "SUSPENDED", "SUSPEND_AUTONOMY", "hard block or stale evidence")
        if state == "ASSISTED_RECOVERY":
            if "RECOVERY_SUCCESS" in kinds and "ASSISTED_APPROVAL" in kinds:
                return self._receipt(row, "STABLE", "RESUME_STABLE", "assisted recovery succeeded")
            if row["assisted_attempts"] >= row["max_assisted"]:
                return self._receipt(row, "SURRENDERED", "SURRENDER_AUTONOMY", "assisted recovery exhausted")
            return self._receipt(row, "ASSISTED_RECOVERY", "REQUIRE_ASSISTED_RECOVERY", "assisted recovery required")
        if "PERSISTENT_DISAGREEMENT" in kinds or "EVIDENCE_GAP" in kinds or row["local_attempts"] >= row["max_local"]:
            return self._receipt(row, "ASSISTED_RECOVERY", "REQUIRE_ASSISTED_RECOVERY", "local recovery insufficient")
        if state == "LOCAL_RECOVERY":
            if "RECOVERY_SUCCESS" in kinds:
                return self._receipt(row, "STABLE", "RESUME_STABLE", "local recovery succeeded")
            return self._receipt(row, "LOCAL_RECOVERY", "ENTER_LOCAL_RECOVERY", "continue bounded local recovery")
        if "SOFT_DEGRADATION" in kinds or "RECOVERY_FAILURE" in kinds:
            return self._receipt(row, "LOCAL_RECOVERY", "ENTER_LOCAL_RECOVERY", "recoverable degradation")
        return self._receipt(row, "STABLE", "CONTINUE_STABLE", "no escalation evidence")

    def _receipt(self, row, target: str, output: str, reason: str) -> dict[str, Any]:
        body = {"schema":"amos.managed-autonomy.decision.v1","lifecycle_id":row["id"],"agent_id":row["agent_id"],
                "current_state":row["state"],"target_state":target,"output":output,"policy_epoch":row["policy_epoch"],
                "authority_epoch":row["authority_epoch"],"fence_epoch":row["fence_epoch"],"reason":reason,
                "authority_semantics":SEMANTICS}
        body["receipt_hash"] = sha(body); return body

    def apply(self, receipt: dict[str, Any]) -> dict[str, Any]:
        expected = dict(receipt); got = expected.pop("receipt_hash", None)
        if got != sha(expected): raise LifecycleError("receipt hash mismatch")
        row = self._get(receipt["lifecycle_id"])
        if receipt["fence_epoch"] != row["fence_epoch"] or receipt["current_state"] != row["state"]:
            raise LifecycleError("stale lifecycle receipt")
        target = receipt["target_state"]
        if target not in STATES or receipt["output"] not in OUTPUTS: raise LifecycleError("invalid target/output")
        local_attempts, assisted_attempts = row["local_attempts"], row["assisted_attempts"]
        if target == "LOCAL_RECOVERY" and row["state"] != "LOCAL_RECOVERY": local_attempts += 1
        if target == "ASSISTED_RECOVERY" and row["state"] != "ASSISTED_RECOVERY": assisted_attempts += 1
        terminal = 1 if target == "SURRENDERED" else 0
        new_fence = row["fence_epoch"] + (0 if target == row["state"] else 1)
        self.db.execute("UPDATE lifecycle SET state=?,local_attempts=?,assisted_attempts=?,fence_epoch=?,terminal=?,updated_ns=? WHERE id=?",
                        (target,local_attempts,assisted_attempts,new_fence,terminal,now_ns(),row["id"]))
        reason_hash = sha(receipt["reason"])
        self.db.execute("INSERT INTO transitions(lifecycle_id,from_state,to_state,output,fence_epoch,reason_hash,created_ns) VALUES(?,?,?,?,?,?,?)",
                        (row["id"],row["state"],target,receipt["output"],new_fence,reason_hash,now_ns()))
        self._ledger({"op":"transition","id":row["id"],"from":row["state"],"to":target,"fence_epoch":new_fence,"output":receipt["output"]})
        self.db.commit()
        return {"state":target,"fence_epoch":new_fence,"local_attempts":local_attempts,"assisted_attempts":assisted_attempts,"terminal":bool(terminal)}

    def verify_ledger(self) -> bool:
        prev = "0" * 64
        for row in self.db.execute("SELECT prev_hash,payload,entry_hash FROM ledger ORDER BY seq"):
            if row[0] != prev: return False
            payload = json.loads(row[1]); expected = sha({"prev_hash":prev,"payload":payload})
            if expected != row[2]: return False
            prev = row[2]
        return True

def self_test():
    with Runtime() as r:
        lid = r.create("agent-a", max_local=1, max_assisted=1)
        assert r.decide(lid)["output"] == "CONTINUE_STABLE"
        r.add_evidence(lid,"SOFT_DEGRADATION","e1",policy_epoch=1,authority_epoch=1)
        rec=r.decide(lid); assert rec["target_state"]=="LOCAL_RECOVERY"; r.apply(rec)
        r.add_evidence(lid,"RECOVERY_FAILURE","e2",policy_epoch=1,authority_epoch=1)
        rec=r.decide(lid); assert rec["target_state"]=="ASSISTED_RECOVERY"; r.apply(rec)
        assert r.verify_ledger()
    print("managed_autonomy self-test: PASS")

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--self-test",action="store_true"); args=ap.parse_args()
    if args.self_test: self_test()

if __name__ == "__main__": main()
