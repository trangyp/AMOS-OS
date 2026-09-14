#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,re,sys
from pathlib import Path
from typing import Any
HEX64=re.compile(r"^[0-9a-f]{64}$")
TRANSPORT_STATES={"QUEUED","SENDING","ACKED","PARTIAL","RETRYABLE","PERMANENT_FAILURE","PROTOCOL_ERROR","IN_DOUBT","RECONCILED_PRESENT"}
ROUNDTRIP_STATES={"VERIFIED_ROUNDTRIP","NOT_VERIFIED"}
FORBIDDEN={"input_value","output_value","prompt","completion","raw_input","raw_output","input.value","output.value","authorization","api_key","token","password"}
def _forbidden(v:Any,path:str="$ ")->list[str]:
    out=[]
    if isinstance(v,dict):
        for k,x in v.items():
            p=f"{path.rstrip()}.{k}"; out += [p] if str(k).lower() in FORBIDDEN else []; out += _forbidden(x,p)
    elif isinstance(v,list):
        for i,x in enumerate(v): out += _forbidden(x,f"{path.rstrip()}[{i}]")
    return out
def _h(v:Any)->bool:return bool(HEX64.fullmatch(str(v or "")))
def validate_transport(o:dict[str,Any])->list[str]:
    e=[]
    for k in ("export_id","trace_id","run_id","build_id","payload_hash","state","attempt_count","transport_semantics","authority_semantics","receipt_hash"):
        if k not in o:e.append(f"missing {k}")
    if o.get("state") not in TRANSPORT_STATES:e.append("invalid transport state")
    if not all(str(o.get(k,"" )).strip() for k in ("export_id","trace_id","run_id","build_id")):e.append("transport identity fields must be non-empty")
    if not isinstance(o.get("attempt_count"),int) or o.get("attempt_count",-1)<0:e.append("attempt_count must be non-negative integer")
    if o.get("transport_semantics")!="HTTP_ACK_IS_NOT_BACKEND_READBACK_VERIFICATION":e.append("transport receipt must preserve ACK/readback distinction")
    if o.get("authority_semantics")!="TRANSPORT_DOES_NOT_GRANT_AUTHORITY":e.append("transport receipt must not claim authority")
    if o.get("state")=="ACKED" and o.get("last_http_status")!=200:e.append("ACKED requires observed HTTP 200")
    if o.get("state")=="RECONCILED_PRESENT" and o.get("last_http_status")==200:e.append("RECONCILED_PRESENT must not masquerade as HTTP ACKED")
    if o.get("status")=="VERIFIED_ROUNDTRIP" or o.get("roundtrip_verified") is True:e.append("transport receipt cannot self-promote to round-trip verification")
    if not _h(o.get("payload_hash")):e.append("payload_hash must be 64 lowercase hex chars")
    if not _h(o.get("receipt_hash")):e.append("receipt_hash must be 64 lowercase hex chars")
    return e
def validate_roundtrip(o:dict[str,Any])->list[str]:
    e=[]
    for k in ("trace_id","run_id","build_id","status","expected_span_count","observed_span_count","missing_span_ids","extra_span_ids","duplicate_span_ids","mismatches","contamination","authority_semantics","causal_semantics","receipt_hash"):
        if k not in o:e.append(f"missing {k}")
    if o.get("status") not in ROUNDTRIP_STATES:e.append("invalid round-trip status")
    if not all(str(o.get(k,"" )).strip() for k in ("trace_id","run_id","build_id")):e.append("round-trip identity fields must be non-empty")
    for k in ("expected_span_count","observed_span_count"):
        if not isinstance(o.get(k),int) or o.get(k,-1)<0:e.append(f"{k} must be non-negative integer")
    for k in ("missing_span_ids","extra_span_ids","duplicate_span_ids","mismatches","contamination"):
        if not isinstance(o.get(k),list):e.append(f"{k} must be list")
    if o.get("authority_semantics")!="ROUNDTRIP_EVIDENCE_DOES_NOT_GRANT_AUTHORITY":e.append("round-trip evidence must not claim authority")
    if o.get("causal_semantics")!="READBACK_MATCH_DOES_NOT_PROVE_CAUSALITY":e.append("read-back match must not claim causal proof")
    if o.get("status")=="VERIFIED_ROUNDTRIP":
        if o.get("expected_span_count")!=o.get("observed_span_count"):e.append("verified round-trip requires equal expected/observed span counts")
        for k in ("missing_span_ids","extra_span_ids","duplicate_span_ids","mismatches","contamination"):
            if o.get(k):e.append(f"verified round-trip cannot contain {k}")
    if not _h(o.get("receipt_hash")):e.append("receipt_hash must be 64 lowercase hex chars")
    return e
def validate(o:dict[str,Any])->list[str]:
    e=[f"receipt contains forbidden persisted field: {p}" for p in _forbidden(o)]
    e += validate_transport(o) if "export_id" in o else validate_roundtrip(o) if "expected_span_count" in o or o.get("status") in ROUNDTRIP_STATES else ["unknown receipt type"]
    return e
def self_test()->int:
    t={"export_id":"e","trace_id":"t","run_id":"r","build_id":"b","payload_hash":"a"*64,"state":"ACKED","attempt_count":1,"last_http_status":200,"ack_hash":"b"*64,"partial_rejected_spans":0,"transport_semantics":"HTTP_ACK_IS_NOT_BACKEND_READBACK_VERIFICATION","authority_semantics":"TRANSPORT_DOES_NOT_GRANT_AUTHORITY","receipt_hash":"c"*64}
    r={"trace_id":"t","run_id":"r","build_id":"b","status":"VERIFIED_ROUNDTRIP","expected_span_count":2,"observed_span_count":2,"missing_span_ids":[],"extra_span_ids":[],"duplicate_span_ids":[],"mismatches":[],"contamination":[],"authority_semantics":"ROUNDTRIP_EVIDENCE_DOES_NOT_GRANT_AUTHORITY","causal_semantics":"READBACK_MATCH_DOES_NOT_PROVE_CAUSALITY","receipt_hash":"d"*64}
    if validate(t) or validate(r):return 1
    b=dict(t); b["status"]="VERIFIED_ROUNDTRIP"; b["prompt"]="secret"; x=validate(b)
    if not any("self-promote" in z for z in x) or not any("forbidden persisted" in z for z in x):return 1
    b=dict(r); b["missing_span_ids"]=["x"]
    if not validate(b):return 1
    print("SELF_TEST_PASS"); return 0
def main()->int:
    ap=argparse.ArgumentParser(); ap.add_argument("path",nargs="?"); ap.add_argument("--self-test",action="store_true"); a=ap.parse_args()
    if a.self_test:return self_test()
    if not a.path:return 2
    try:o=json.loads(Path(a.path).read_text())
    except Exception as exc:print(f"invalid receipt: {exc}",file=sys.stderr);return 2
    e=validate(o)
    for x in e:print("ERROR",x)
    print(f"TRANSPORT_ROUNDTRIP_CONTRACT errors={len(e)}");return 1 if e else 0
if __name__=="__main__":raise SystemExit(main())
