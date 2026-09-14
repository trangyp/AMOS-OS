#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

REQ={"schema","decision_id","auth_id","phase","decision","reasons","request_hash","chain_ids","usage_before","evaluated_at_ns","policy_id","policy_version","policy_epoch","revocation_epoch","authority_semantics","commit_semantics","identity_semantics","signature_semantics","receipt_hash"}
AUTHORITY="AUTHORIZATION_DECISION_DOES_NOT_GRANT_EXECUTION_OR_COMMIT_AUTHORITY"
COMMIT="PREFLIGHT_ALLOW_DOES_NOT_IMPLY_COMMIT_TIME_ALLOW"
IDENTITY="AUTHENTICATED_IDENTITY_DOES_NOT_IMPLY_AUTHORIZED_ACTION"
SIGNATURE="EXTERNAL_SIGNATURE_EVIDENCE_DOES_NOT_IMPLY_POLICY_VALIDITY"

def _canon(v: Any) -> str:
    return json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False)

def _sha(v: Any) -> str:
    return hashlib.sha256(_canon(v).encode()).hexdigest()

def validate(d: dict[str, Any]) -> list[str]:
    e=[]
    m=REQ-set(d)
    if m:e.append("missing:"+",".join(sorted(m)))
    if d.get("schema") != "amos.portable-authorization.decision.v1": e.append("bad_schema")
    if d.get("decision") not in {"ALLOW","DENY","UNKNOWN"}: e.append("bad_decision")
    if d.get("phase") not in {"PREFLIGHT","COMMIT"}: e.append("bad_phase")
    if not isinstance(d.get("reasons"),list): e.append("bad_reasons")
    if not isinstance(d.get("chain_ids"),list): e.append("bad_chain_ids")
    if not isinstance(d.get("usage_before"),dict): e.append("bad_usage_before")
    if d.get("authority_semantics") != AUTHORITY: e.append("bad_authority_semantics")
    if d.get("commit_semantics") != COMMIT: e.append("bad_commit_semantics")
    if d.get("identity_semantics") != IDENTITY: e.append("bad_identity_semantics")
    if d.get("signature_semantics") != SIGNATURE: e.append("bad_signature_semantics")
    rh=d.get("receipt_hash")
    if not isinstance(rh,str) or len(rh)!=64: e.append("bad_receipt_hash_shape")
    elif not m:
        base=dict(d); base.pop("receipt_hash",None)
        if _sha(base)!=rh: e.append("receipt_hash_mismatch")
    return e

def _fixture() -> dict[str, Any]:
    x={
      "schema":"amos.portable-authorization.decision.v1","decision_id":"d","auth_id":"a","phase":"PREFLIGHT","decision":"ALLOW",
      "reasons":[],"request_hash":"0"*64,"chain_ids":["a"],"usage_before":{"a":0},"evaluated_at_ns":1,
      "policy_id":"p","policy_version":"1","policy_epoch":1,"revocation_epoch":1,
      "authority_semantics":AUTHORITY,"commit_semantics":COMMIT,"identity_semantics":IDENTITY,"signature_semantics":SIGNATURE
    }
    x["receipt_hash"]=_sha(x)
    return x

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument("receipt",nargs="?"); ap.add_argument("--self-test",action="store_true"); a=ap.parse_args()
    if a.self_test:
        x=_fixture(); assert not validate(x)
        x["decision"]="DENY"; assert "receipt_hash_mismatch" in validate(x)
        print("portable_authorization audit self-test: PASS"); raise SystemExit(0)
    if not a.receipt: raise SystemExit("receipt path required unless --self-test")
    d=json.loads(Path(a.receipt).read_text(encoding="utf-8")); e=validate(d); print(json.dumps({"valid":not e,"errors":e})); raise SystemExit(0 if not e else 2)
