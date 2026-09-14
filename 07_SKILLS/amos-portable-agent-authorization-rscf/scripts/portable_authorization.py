#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
import time
import uuid
from pathlib import Path
from typing import Any

DECISIONS = {"ALLOW", "DENY", "UNKNOWN"}
SIGNATURE_STATES = {"NOT_PRESENT", "PRESENT_UNVERIFIED", "VERIFIED_EXTERNAL", "INVALID"}
IDENTITY_STATES = {"AUTHENTICATED", "UNVERIFIED", "INVALID"}
SIG_POLICIES = {"OPTIONAL", "REQUIRED"}
CONSEQUENCE = {"LOW": 1, "MEDIUM": 2, "HIGH": 3, "CRITICAL": 4}

AUTHORITY_SEMANTICS = "AUTHORIZATION_DECISION_DOES_NOT_GRANT_EXECUTION_OR_COMMIT_AUTHORITY"
COMMIT_SEMANTICS = "PREFLIGHT_ALLOW_DOES_NOT_IMPLY_COMMIT_TIME_ALLOW"
IDENTITY_SEMANTICS = "AUTHENTICATED_IDENTITY_DOES_NOT_IMPLY_AUTHORIZED_ACTION"
SIGNATURE_SEMANTICS = "EXTERNAL_SIGNATURE_EVIDENCE_DOES_NOT_IMPLY_POLICY_VALIDITY"

FORBIDDEN_DURABLE_KEYS = {"password", "secret", "token", "api_key", "credential", "raw_input", "raw_output", "chain_of_thought", "reasoning"}

class AuthorizationError(RuntimeError):
    pass

def _now_ns() -> int:
    return time.time_ns()

def _canon(v: Any) -> str:
    return json.dumps(v, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

def _sha(v: Any) -> str:
    return hashlib.sha256(_canon(v).encode()).hexdigest()

def _nonempty(name: str, value: Any) -> str:
    if not isinstance(value, str) or not value.strip():
        raise AuthorizationError(f"{name} must be non-empty string")
    return value.strip()

def _reject_sensitive(v: Any, path: str = "$") -> None:
    if isinstance(v, dict):
        for k, child in v.items():
            if str(k).lower() in FORBIDDEN_DURABLE_KEYS:
                raise AuthorizationError(f"sensitive durable key forbidden: {path}.{k}")
            _reject_sensitive(child, f"{path}.{k}")
    elif isinstance(v, list):
        for i, child in enumerate(v):
            _reject_sensitive(child, f"{path}[{i}]")

def _as_set(name: str, values: Any) -> set[str]:
    if not isinstance(values, list) or not values:
        raise AuthorizationError(f"{name} must be non-empty list")
    out = {_nonempty(name, x) for x in values}
    return out

def resource_within(child: str, parent: str) -> bool:
    child = _nonempty("resource", child)
    parent = _nonempty("resource_prefix", parent)
    if child == parent:
        return True
    p = parent.rstrip("/")
    return child.startswith(p + "/")

def scope_within(child_scopes: set[str], parent_scopes: set[str]) -> bool:
    return all(any(resource_within(c, p) for p in parent_scopes) for c in child_scopes)

def _ledger_hash(prev: str, kind: str, payload: str, ts: int) -> str:
    return hashlib.sha256(f"{prev}|{kind}|{payload}|{ts}".encode()).hexdigest()

class AuthorizationRuntime:
    def __init__(self, db_path: str | Path = ":memory:") -> None:
        self.db = sqlite3.connect(str(db_path), isolation_level=None)
        self.db.row_factory = sqlite3.Row
        self.db.execute("PRAGMA foreign_keys=ON")
        self._init()

    def close(self) -> None:
        self.db.close()

    def __enter__(self) -> "AuthorizationRuntime":
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any) -> None:
        self.close()

    def _init(self) -> None:
        self.db.executescript("""
        CREATE TABLE IF NOT EXISTS control_state(
          singleton INTEGER PRIMARY KEY CHECK(singleton=1),
          policy_id TEXT NOT NULL,
          policy_version TEXT NOT NULL,
          policy_epoch INTEGER NOT NULL,
          revocation_epoch INTEGER NOT NULL
        );
        CREATE TABLE IF NOT EXISTS authz(
          auth_id TEXT PRIMARY KEY,
          issuer_id TEXT NOT NULL,
          issuer_key_id TEXT NOT NULL,
          subject_id TEXT NOT NULL,
          actions_json TEXT NOT NULL,
          resources_json TEXT NOT NULL,
          recipients_json TEXT NOT NULL,
          not_before_ns INTEGER NOT NULL,
          expires_at_ns INTEGER NOT NULL,
          max_uses INTEGER NOT NULL,
          consequence_ceiling TEXT NOT NULL,
          parent_id TEXT,
          depth INTEGER NOT NULL,
          max_delegation_depth INTEGER NOT NULL,
          policy_id TEXT NOT NULL,
          policy_version TEXT NOT NULL,
          policy_epoch INTEGER NOT NULL,
          issued_revocation_epoch INTEGER NOT NULL,
          signature_policy TEXT NOT NULL,
          signature_state TEXT NOT NULL,
          verifier_id TEXT,
          verifier_version TEXT,
          signature_evidence_ref TEXT,
          object_hash TEXT NOT NULL,
          created_at_ns INTEGER NOT NULL,
          FOREIGN KEY(parent_id) REFERENCES authz(auth_id)
        );
        CREATE TABLE IF NOT EXISTS revocations(
          auth_id TEXT PRIMARY KEY,
          revocation_epoch INTEGER NOT NULL,
          evidence_ref TEXT NOT NULL,
          revoked_at_ns INTEGER NOT NULL,
          FOREIGN KEY(auth_id) REFERENCES authz(auth_id)
        );
        CREATE TABLE IF NOT EXISTS usage(
          auth_id TEXT PRIMARY KEY,
          used_count INTEGER NOT NULL DEFAULT 0,
          FOREIGN KEY(auth_id) REFERENCES authz(auth_id)
        );
        CREATE TABLE IF NOT EXISTS decisions(
          decision_id TEXT PRIMARY KEY,
          auth_id TEXT NOT NULL,
          phase TEXT NOT NULL,
          decision TEXT NOT NULL,
          request_hash TEXT NOT NULL,
          receipt_json TEXT NOT NULL,
          receipt_hash TEXT NOT NULL,
          created_at_ns INTEGER NOT NULL
        );
        CREATE TABLE IF NOT EXISTS ledger(
          seq INTEGER PRIMARY KEY AUTOINCREMENT,
          kind TEXT NOT NULL,
          payload_json TEXT NOT NULL,
          ts_ns INTEGER NOT NULL,
          prev_hash TEXT NOT NULL,
          event_hash TEXT NOT NULL
        );
        """)

    def _event(self, kind: str, payload: dict[str, Any]) -> str:
        _reject_sensitive(payload)
        p = _canon(payload)
        row = self.db.execute("SELECT event_hash FROM ledger ORDER BY seq DESC LIMIT 1").fetchone()
        prev = row["event_hash"] if row else "0" * 64
        ts = _now_ns()
        h = _ledger_hash(prev, kind, p, ts)
        self.db.execute("INSERT INTO ledger(kind,payload_json,ts_ns,prev_hash,event_hash) VALUES(?,?,?,?,?)", (kind, p, ts, prev, h))
        return h

    def set_control_state(self, *, policy_id: str, policy_version: str, policy_epoch: int, revocation_epoch: int) -> None:
        _nonempty("policy_id", policy_id); _nonempty("policy_version", policy_version)
        if not isinstance(policy_epoch, int) or policy_epoch < 0 or not isinstance(revocation_epoch, int) or revocation_epoch < 0:
            raise AuthorizationError("epochs must be non-negative integers")
        old = self.db.execute("SELECT * FROM control_state WHERE singleton=1").fetchone()
        if old and (policy_epoch < old["policy_epoch"] or revocation_epoch < old["revocation_epoch"]):
            raise AuthorizationError("control epochs cannot move backward")
        self.db.execute("INSERT INTO control_state VALUES(1,?,?,?,?) ON CONFLICT(singleton) DO UPDATE SET policy_id=excluded.policy_id,policy_version=excluded.policy_version,policy_epoch=excluded.policy_epoch,revocation_epoch=excluded.revocation_epoch", (policy_id, policy_version, policy_epoch, revocation_epoch))
        self._event("CONTROL_STATE_SET", {"policy_id": policy_id, "policy_version": policy_version, "policy_epoch": policy_epoch, "revocation_epoch": revocation_epoch})

    def _control(self) -> sqlite3.Row | None:
        return self.db.execute("SELECT * FROM control_state WHERE singleton=1").fetchone()

    def _auth(self, auth_id: str) -> sqlite3.Row:
        row = self.db.execute("SELECT * FROM authz WHERE auth_id=?", (auth_id,)).fetchone()
        if row is None:
            raise AuthorizationError(f"unknown auth_id: {auth_id}")
        return row

    def _object_payload(self, row: sqlite3.Row) -> dict[str, Any]:
        return {
            "auth_id": row["auth_id"],
            "issuer_id": row["issuer_id"],
            "issuer_key_id": row["issuer_key_id"],
            "subject_id": row["subject_id"],
            "actions": json.loads(row["actions_json"]),
            "resource_prefixes": json.loads(row["resources_json"]),
            "recipients": json.loads(row["recipients_json"]),
            "not_before_ns": int(row["not_before_ns"]),
            "expires_at_ns": int(row["expires_at_ns"]),
            "max_uses": int(row["max_uses"]),
            "consequence_ceiling": row["consequence_ceiling"],
            "parent_id": row["parent_id"],
            "depth": int(row["depth"]),
            "max_delegation_depth": int(row["max_delegation_depth"]),
            "policy_id": row["policy_id"],
            "policy_version": row["policy_version"],
            "policy_epoch": int(row["policy_epoch"]),
            "issued_revocation_epoch": int(row["issued_revocation_epoch"]),
            "signature_policy": row["signature_policy"],
            "signature_state": row["signature_state"],
            "verifier_id": row["verifier_id"],
            "verifier_version": row["verifier_version"],
            "signature_evidence_ref": row["signature_evidence_ref"],
        }

    def _object_hash_valid(self, row: sqlite3.Row) -> bool:
        return _sha(self._object_payload(row)) == row["object_hash"]

    def _signature_fields(self, signature_state: str, verifier_id: str | None, verifier_version: str | None, evidence_ref: str | None) -> tuple[str | None, str | None, str | None]:
        if signature_state not in SIGNATURE_STATES:
            raise AuthorizationError("invalid signature_state")
        if signature_state == "VERIFIED_EXTERNAL":
            return (_nonempty("verifier_id", verifier_id), _nonempty("verifier_version", verifier_version), _nonempty("signature_evidence_ref", evidence_ref))
        if verifier_id is not None or verifier_version is not None or evidence_ref is not None:
            raise AuthorizationError("verifier metadata only allowed with VERIFIED_EXTERNAL")
        return None, None, None

    def create_root(self, **kw: Any) -> str:
        if kw.get("parent_id") is not None:
            raise AuthorizationError("root cannot have parent_id")
        return self._insert(parent=None, **kw)

    def delegate(self, parent_id: str, **kw: Any) -> str:
        parent = self._auth(parent_id)
        if not self._object_hash_valid(parent):
            raise AuthorizationError("parent authorization object hash mismatch")
        return self._insert(parent=parent, parent_id=parent_id, **kw)

    def _insert(
        self,
        *,
        parent: sqlite3.Row | None,
        issuer_id: str,
        issuer_key_id: str,
        subject_id: str,
        actions: list[str],
        resource_prefixes: list[str],
        recipients: list[str],
        not_before_ns: int,
        expires_at_ns: int,
        max_uses: int,
        consequence_ceiling: str,
        max_delegation_depth: int,
        policy_id: str,
        policy_version: str,
        policy_epoch: int,
        issued_revocation_epoch: int,
        signature_policy: str,
        signature_state: str,
        verifier_id: str | None = None,
        verifier_version: str | None = None,
        signature_evidence_ref: str | None = None,
        auth_id: str | None = None,
        parent_id: str | None = None,
    ) -> str:
        issuer_id = _nonempty("issuer_id", issuer_id); issuer_key_id = _nonempty("issuer_key_id", issuer_key_id); subject_id = _nonempty("subject_id", subject_id)
        acts = _as_set("actions", actions); resources = _as_set("resource_prefixes", resource_prefixes); recips = _as_set("recipients", recipients)
        if not isinstance(not_before_ns, int) or not isinstance(expires_at_ns, int) or not_before_ns >= expires_at_ns:
            raise AuthorizationError("invalid validity interval")
        if not isinstance(max_uses, int) or max_uses <= 0:
            raise AuthorizationError("max_uses must be positive integer")
        if consequence_ceiling not in CONSEQUENCE:
            raise AuthorizationError("invalid consequence_ceiling")
        if not isinstance(max_delegation_depth, int) or max_delegation_depth < 0:
            raise AuthorizationError("max_delegation_depth must be non-negative integer")
        _nonempty("policy_id", policy_id); _nonempty("policy_version", policy_version)
        if not isinstance(policy_epoch, int) or policy_epoch < 0 or not isinstance(issued_revocation_epoch, int) or issued_revocation_epoch < 0:
            raise AuthorizationError("invalid epoch")
        if signature_policy not in SIG_POLICIES:
            raise AuthorizationError("invalid signature_policy")
        verifier_id, verifier_version, signature_evidence_ref = self._signature_fields(signature_state, verifier_id, verifier_version, signature_evidence_ref)
        depth = 0 if parent is None else int(parent["depth"]) + 1
        if parent is not None:
            if issuer_id != parent["subject_id"]:
                raise AuthorizationError("child issuer must equal parent subject")
            if depth > int(parent["max_delegation_depth"]):
                raise AuthorizationError("delegation depth exceeds parent bound")
            pacts = set(json.loads(parent["actions_json"])); pres = set(json.loads(parent["resources_json"])); prec = set(json.loads(parent["recipients_json"]))
            if not acts <= pacts: raise AuthorizationError("child actions widen parent")
            if not scope_within(resources, pres): raise AuthorizationError("child resource scope widens parent")
            if not recips <= prec: raise AuthorizationError("child recipients widen parent")
            if not (int(parent["not_before_ns"]) <= not_before_ns < expires_at_ns <= int(parent["expires_at_ns"])): raise AuthorizationError("child lifetime widens parent")
            if max_uses > int(parent["max_uses"]): raise AuthorizationError("child max_uses widens parent")
            if CONSEQUENCE[consequence_ceiling] > CONSEQUENCE[parent["consequence_ceiling"]]: raise AuthorizationError("child consequence ceiling widens parent")
            if policy_id != parent["policy_id"] or policy_version != parent["policy_version"] or policy_epoch != int(parent["policy_epoch"]): raise AuthorizationError("child policy binding must equal parent")
            if signature_policy == "OPTIONAL" and parent["signature_policy"] == "REQUIRED": raise AuthorizationError("child cannot weaken signature policy")
            if max_delegation_depth > int(parent["max_delegation_depth"]): raise AuthorizationError("child delegation bound cannot widen parent")
        aid = auth_id or uuid.uuid4().hex
        _nonempty("auth_id", aid)
        obj = {
            "auth_id": aid, "issuer_id": issuer_id, "issuer_key_id": issuer_key_id, "subject_id": subject_id,
            "actions": sorted(acts), "resource_prefixes": sorted(resources), "recipients": sorted(recips),
            "not_before_ns": not_before_ns, "expires_at_ns": expires_at_ns, "max_uses": max_uses,
            "consequence_ceiling": consequence_ceiling, "parent_id": parent_id, "depth": depth,
            "max_delegation_depth": max_delegation_depth, "policy_id": policy_id, "policy_version": policy_version,
            "policy_epoch": policy_epoch, "issued_revocation_epoch": issued_revocation_epoch,
            "signature_policy": signature_policy, "signature_state": signature_state,
            "verifier_id": verifier_id, "verifier_version": verifier_version, "signature_evidence_ref": signature_evidence_ref,
        }
        h = _sha(obj)
        self.db.execute("INSERT INTO authz VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (
            aid, issuer_id, issuer_key_id, subject_id, _canon(sorted(acts)), _canon(sorted(resources)), _canon(sorted(recips)),
            not_before_ns, expires_at_ns, max_uses, consequence_ceiling, parent_id, depth, max_delegation_depth,
            policy_id, policy_version, policy_epoch, issued_revocation_epoch, signature_policy, signature_state,
            verifier_id, verifier_version, signature_evidence_ref, h, _now_ns()
        ))
        self.db.execute("INSERT INTO usage(auth_id,used_count) VALUES(?,0)", (aid,))
        self._event("AUTH_CREATED", {"auth_id": aid, "parent_id": parent_id, "object_hash": h})
        return aid

    def revoke(self, auth_id: str, *, evidence_ref: str, revocation_epoch: int) -> None:
        self._auth(auth_id); _nonempty("evidence_ref", evidence_ref)
        control = self._control()
        if control is None: raise AuthorizationError("control state required")
        if revocation_epoch <= int(control["revocation_epoch"]): raise AuthorizationError("revocation epoch must advance current state")
        self.db.execute("UPDATE control_state SET revocation_epoch=? WHERE singleton=1", (revocation_epoch,))
        self.db.execute("INSERT INTO revocations VALUES(?,?,?,?) ON CONFLICT(auth_id) DO UPDATE SET revocation_epoch=excluded.revocation_epoch,evidence_ref=excluded.evidence_ref,revoked_at_ns=excluded.revoked_at_ns", (auth_id, revocation_epoch, evidence_ref, _now_ns()))
        self._event("AUTH_REVOKED", {"auth_id": auth_id, "revocation_epoch": revocation_epoch, "evidence_ref": evidence_ref})

    def _chain(self, leaf_id: str) -> list[sqlite3.Row]:
        out: list[sqlite3.Row] = []
        seen: set[str] = set(); cur = self._auth(leaf_id)
        while True:
            if cur["auth_id"] in seen: raise AuthorizationError("authorization cycle")
            seen.add(cur["auth_id"]); out.append(cur)
            if cur["parent_id"] is None: break
            cur = self._auth(cur["parent_id"])
        out.reverse()
        return out

    def _validate_chain_edge(self, parent: sqlite3.Row, child: sqlite3.Row) -> list[str]:
        reasons: list[str] = []
        if child["issuer_id"] != parent["subject_id"]: reasons.append("issuer_parent_subject_mismatch")
        if not set(json.loads(child["actions_json"])) <= set(json.loads(parent["actions_json"])): reasons.append("action_attenuation_broken")
        if not scope_within(set(json.loads(child["resources_json"])), set(json.loads(parent["resources_json"]))): reasons.append("resource_attenuation_broken")
        if not set(json.loads(child["recipients_json"])) <= set(json.loads(parent["recipients_json"])): reasons.append("recipient_attenuation_broken")
        if not (int(parent["not_before_ns"]) <= int(child["not_before_ns"]) < int(child["expires_at_ns"]) <= int(parent["expires_at_ns"])): reasons.append("lifetime_attenuation_broken")
        if int(child["max_uses"]) > int(parent["max_uses"]): reasons.append("use_attenuation_broken")
        if CONSEQUENCE[child["consequence_ceiling"]] > CONSEQUENCE[parent["consequence_ceiling"]]: reasons.append("consequence_attenuation_broken")
        if child["policy_id"] != parent["policy_id"] or child["policy_version"] != parent["policy_version"] or int(child["policy_epoch"]) != int(parent["policy_epoch"]): reasons.append("policy_binding_broken")
        if child["signature_policy"] == "OPTIONAL" and parent["signature_policy"] == "REQUIRED": reasons.append("signature_policy_weakened")
        return reasons

    def _evaluate_inner(self, auth_id: str, request: dict[str, Any], now_ns: int) -> tuple[str, list[str], list[sqlite3.Row], dict[str, int]]:
        _reject_sensitive(request)
        required = {"subject_id", "action", "resource", "recipient", "consequence", "identity_state", "identity_evidence_ref"}
        missing = sorted(required - set(request))
        if missing: return "UNKNOWN", ["missing_request_fields:" + ",".join(missing)], [], {}
        if request["identity_state"] not in IDENTITY_STATES: return "UNKNOWN", ["invalid_identity_state"], [], {}
        if request["identity_state"] == "INVALID": return "DENY", ["identity_invalid"], [], {}
        if request["identity_state"] != "AUTHENTICATED": return "UNKNOWN", ["identity_not_authenticated"], [], {}
        try: _nonempty("identity_evidence_ref", request["identity_evidence_ref"])
        except AuthorizationError: return "UNKNOWN", ["identity_evidence_missing"], [], {}
        if request["consequence"] not in CONSEQUENCE: return "UNKNOWN", ["invalid_consequence"], [], {}
        control = self._control()
        if control is None: return "UNKNOWN", ["control_state_unknown"], [], {}
        try: chain = self._chain(auth_id)
        except AuthorizationError: return "UNKNOWN", ["authorization_chain_unknown"], [], {}
        reasons: list[str] = []
        for row in chain:
            if not self._object_hash_valid(row):
                reasons.append(f"authorization_object_hash_mismatch:{row['auth_id']}")
        if reasons:
            return "DENY", reasons, chain, {}
        for p, c in zip(chain, chain[1:]): reasons.extend(self._validate_chain_edge(p, c))
        if reasons: return "DENY", reasons, chain, {}
        leaf = chain[-1]
        if request["subject_id"] != leaf["subject_id"]: reasons.append("subject_mismatch")
        if request["action"] not in set(json.loads(leaf["actions_json"])): reasons.append("action_not_allowed")
        if not any(resource_within(request["resource"], p) for p in json.loads(leaf["resources_json"])): reasons.append("resource_not_allowed")
        if request["recipient"] not in set(json.loads(leaf["recipients_json"])): reasons.append("recipient_not_allowed")
        if CONSEQUENCE[request["consequence"]] > CONSEQUENCE[leaf["consequence_ceiling"]]: reasons.append("consequence_exceeds_ceiling")
        counts: dict[str, int] = {}
        for row in chain:
            if not (int(row["not_before_ns"]) <= now_ns <= int(row["expires_at_ns"])): reasons.append(f"time_invalid:{row['auth_id']}")
            if self.db.execute("SELECT 1 FROM revocations WHERE auth_id=?", (row["auth_id"],)).fetchone(): reasons.append(f"revoked:{row['auth_id']}")
            u = int(self.db.execute("SELECT used_count FROM usage WHERE auth_id=?", (row["auth_id"],)).fetchone()["used_count"]); counts[row["auth_id"]] = u
            if u >= int(row["max_uses"]): reasons.append(f"use_limit_exhausted:{row['auth_id']}")
            if row["signature_state"] == "INVALID": reasons.append(f"signature_invalid:{row['auth_id']}")
            elif row["signature_policy"] == "REQUIRED" and row["signature_state"] != "VERIFIED_EXTERNAL":
                return "UNKNOWN", [f"signature_not_verified:{row['auth_id']}"], chain, counts
        if leaf["policy_id"] != control["policy_id"] or leaf["policy_version"] != control["policy_version"] or int(leaf["policy_epoch"]) != int(control["policy_epoch"]): reasons.append("policy_state_stale")
        if int(control["revocation_epoch"]) < max(int(r["issued_revocation_epoch"]) for r in chain): return "UNKNOWN", ["revocation_state_stale"], chain, counts
        return ("DENY" if reasons else "ALLOW"), reasons, chain, counts

    def _receipt(self, auth_id: str, phase: str, request: dict[str, Any], decision: str, reasons: list[str], chain: list[sqlite3.Row], counts: dict[str, int], now_ns: int) -> dict[str, Any]:
        control = self._control()
        receipt = {
            "schema": "amos.portable-authorization.decision.v1", "decision_id": uuid.uuid4().hex,
            "auth_id": auth_id, "phase": phase, "decision": decision, "reasons": reasons,
            "request_hash": _sha(request), "chain_ids": [r["auth_id"] for r in chain], "usage_before": counts,
            "evaluated_at_ns": now_ns,
            "policy_id": control["policy_id"] if control else None, "policy_version": control["policy_version"] if control else None,
            "policy_epoch": int(control["policy_epoch"]) if control else None, "revocation_epoch": int(control["revocation_epoch"]) if control else None,
            "authority_semantics": AUTHORITY_SEMANTICS, "commit_semantics": COMMIT_SEMANTICS,
            "identity_semantics": IDENTITY_SEMANTICS, "signature_semantics": SIGNATURE_SEMANTICS,
        }
        receipt["receipt_hash"] = _sha(receipt)
        self.db.execute("INSERT INTO decisions VALUES(?,?,?,?,?,?,?,?)", (receipt["decision_id"], auth_id, phase, decision, receipt["request_hash"], _canon(receipt), receipt["receipt_hash"], _now_ns()))
        self._event("AUTH_DECISION", {"decision_id": receipt["decision_id"], "auth_id": auth_id, "phase": phase, "decision": decision, "receipt_hash": receipt["receipt_hash"]})
        return receipt

    def preflight(self, auth_id: str, request: dict[str, Any], *, now_ns: int | None = None) -> dict[str, Any]:
        t = _now_ns() if now_ns is None else int(now_ns)
        d, reasons, chain, counts = self._evaluate_inner(auth_id, request, t)
        return self._receipt(auth_id, "PREFLIGHT", request, d, reasons, chain, counts, t)

    def commit(self, auth_id: str, request: dict[str, Any], *, now_ns: int | None = None) -> dict[str, Any]:
        t = _now_ns() if now_ns is None else int(now_ns)
        self.db.execute("BEGIN IMMEDIATE")
        try:
            d, reasons, chain, counts = self._evaluate_inner(auth_id, request, t)
            if d == "ALLOW":
                for row in chain:
                    self.db.execute("UPDATE usage SET used_count=used_count+1 WHERE auth_id=?", (row["auth_id"],))
            receipt = self._receipt(auth_id, "COMMIT", request, d, reasons, chain, counts, t)
            self.db.execute("COMMIT")
            return receipt
        except Exception:
            self.db.execute("ROLLBACK")
            raise

    def export_object(self, auth_id: str) -> dict[str, Any]:
        r = self._auth(auth_id)
        return {k: r[k] for k in r.keys() if k not in {"actions_json", "resources_json", "recipients_json"}} | {
            "actions": json.loads(r["actions_json"]), "resource_prefixes": json.loads(r["resources_json"]), "recipients": json.loads(r["recipients_json"])
        }

    def verify_ledger(self) -> bool:
        prev = "0" * 64
        for r in self.db.execute("SELECT * FROM ledger ORDER BY seq"):
            if r["prev_hash"] != prev or _ledger_hash(prev, r["kind"], r["payload_json"], int(r["ts_ns"])) != r["event_hash"]: return False
            prev = r["event_hash"]
        return True

def _self_test() -> None:
    now = 2_000_000_000_000_000_000
    with AuthorizationRuntime() as rt:
        rt.set_control_state(policy_id="p", policy_version="1", policy_epoch=1, revocation_epoch=1)
        root = rt.create_root(issuer_id="org", issuer_key_id="k1", subject_id="agent-a", actions=["read","write"], resource_prefixes=["repo:amos/root"], recipients=["tool-a","tool-b"], not_before_ns=now-10, expires_at_ns=now+100, max_uses=3, consequence_ceiling="HIGH", max_delegation_depth=2, policy_id="p", policy_version="1", policy_epoch=1, issued_revocation_epoch=1, signature_policy="REQUIRED", signature_state="VERIFIED_EXTERNAL", verifier_id="sigstore", verifier_version="1", signature_evidence_ref="e:sig")
        child = rt.delegate(root, issuer_id="agent-a", issuer_key_id="k2", subject_id="agent-b", actions=["read"], resource_prefixes=["repo:amos/root/sub"], recipients=["tool-a"], not_before_ns=now-5, expires_at_ns=now+50, max_uses=2, consequence_ceiling="MEDIUM", max_delegation_depth=2, policy_id="p", policy_version="1", policy_epoch=1, issued_revocation_epoch=1, signature_policy="REQUIRED", signature_state="VERIFIED_EXTERNAL", verifier_id="sigstore", verifier_version="1", signature_evidence_ref="e:child")
        req={"subject_id":"agent-b","action":"read","resource":"repo:amos/root/sub/file","recipient":"tool-a","consequence":"LOW","identity_state":"AUTHENTICATED","identity_evidence_ref":"id:e"}
        assert rt.preflight(child, req, now_ns=now)["decision"] == "ALLOW"
        assert rt.commit(child, req, now_ns=now)["decision"] == "ALLOW"
        assert rt.verify_ledger()
    print("portable_authorization self-test: PASS")

if __name__ == "__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("--self-test",action="store_true"); a=ap.parse_args()
    if a.self_test: _self_test()
