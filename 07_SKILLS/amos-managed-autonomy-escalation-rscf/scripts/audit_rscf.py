#!/usr/bin/env python3
import argparse, hashlib, json

def canon(v): return json.dumps(v, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
def sha(v): return hashlib.sha256(canon(v).encode()).hexdigest()
def validate(r):
    x=dict(r); h=x.pop("receipt_hash",None)
    return h==sha(x) and x.get("schema")=="amos.managed-autonomy.decision.v1" and x.get("authority_semantics")=="LIFECYCLE_DECISION_DOES_NOT_GRANT_EXECUTION_OR_COMMIT_AUTHORITY"
def self_test():
    r={"schema":"amos.managed-autonomy.decision.v1","authority_semantics":"LIFECYCLE_DECISION_DOES_NOT_GRANT_EXECUTION_OR_COMMIT_AUTHORITY"}; r["receipt_hash"]=sha(r)
    assert validate(r); print("managed_autonomy receipt self-test: PASS")
if __name__=="__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("--self-test",action="store_true"); ap.add_argument("file",nargs="?"); a=ap.parse_args()
    if a.self_test: self_test()
    elif a.file: print("PASS" if validate(json.load(open(a.file,encoding="utf-8"))) else "FAIL")
