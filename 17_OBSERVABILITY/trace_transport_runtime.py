#!/usr/bin/env python3
from __future__ import annotations
import base64, hashlib, json, random, sqlite3, time, urllib.error, urllib.request, uuid
from dataclasses import dataclass
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any, Callable, Iterable
from urllib.parse import urlparse

TERMINAL_EXPORT_STATES={"ACKED","PARTIAL","PERMANENT_FAILURE","PROTOCOL_ERROR","RECONCILED_PRESENT"}
SENDABLE_EXPORT_STATES={"QUEUED","RETRYABLE"}
EXPORT_STATES=SENDABLE_EXPORT_STATES|TERMINAL_EXPORT_STATES|{"SENDING","IN_DOUBT"}

def _json(v:Any)->str:return json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False)
def _sha(v:Any)->str:return hashlib.sha256(_json(v).encode()).hexdigest()
def _now()->float:return time.time()
def _ns(v:float)->str:return str(int(round(float(v)*1_000_000_000)))
def _b64_hex(v:str,n:int,name:str)->str:
    try: raw=bytes.fromhex(v)
    except ValueError as exc: raise TransportContractError(f"{name} must be hexadecimal") from exc
    if len(raw)!=n: raise TransportContractError(f"{name} must be {n} bytes")
    return base64.b64encode(raw).decode()
def _any(v:Any)->dict[str,Any]:
    if v is None:return {"stringValue":""}
    if isinstance(v,bool):return {"boolValue":v}
    if isinstance(v,int):return {"intValue":str(v)}
    if isinstance(v,float):return {"doubleValue":v}
    if isinstance(v,(dict,list,tuple)):return {"stringValue":_json(v)}
    return {"stringValue":str(v)}
def _kv(d:dict[str,Any])->list[dict[str,Any]]:return [{"key":k,"value":_any(d[k])} for k in sorted(d)]

class TransportContractError(RuntimeError):pass

@dataclass(frozen=True)
class RetryPolicy:
    max_attempts:int=5; initial_interval:float=1.0; max_interval:float=30.0; multiplier:float=2.0; jitter_fraction:float=.2
    def validate(self)->None:
        if self.max_attempts<1:raise TransportContractError("max_attempts must be >= 1")
        if min(self.initial_interval,self.max_interval)<0:raise TransportContractError("retry intervals must be non-negative")
        if self.multiplier<1:raise TransportContractError("multiplier must be >= 1")
        if not 0<=self.jitter_fraction<=1:raise TransportContractError("jitter_fraction must be in [0,1]")
    def delay(self,attempt:int,rng:Callable[[],float]=random.random)->float:
        self.validate(); base=min(self.max_interval,self.initial_interval*self.multiplier**max(0,attempt-1))
        spread=base*self.jitter_fraction
        return max(0.0,base-spread+2*spread*rng()) if spread else base

class OtlpHttpJsonEncoder:
    """Bounded AMOS -> OTLP/HTTP JSON projection; not conformance certification."""
    @staticmethod
    def encode(spans:Iterable[dict[str,Any]],*,run_id:str,build_id:str,service_name:str="amos-os",scope_name:str="amos.agentops",scope_version:str="transport-reference-v1")->dict[str,Any]:
        rows=[dict(s) for s in spans]
        if not rows:raise TransportContractError("cannot export an empty trace")
        tids={s.get("trace_id") for s in rows}
        if len(tids)!=1 or None in tids:raise TransportContractError("one export request must contain exactly one AMOS trace")
        if any(s.get("status")=="STARTED" for s in rows):raise TransportContractError("open spans cannot be exported as round-trip evidence")
        if not run_id or not build_id:raise TransportContractError("run_id and build_id are required")
        out=[]
        for s in rows:
            attrs={"amos.span.kind":s.get("kind","UNKNOWN"),"amos.subject":s.get("subject",""),"amos.provenance.root":s.get("provenance_root",""),"amos.environment":s.get("environment",""),"amos.effect.state":s.get("effect_state","NONE"),"amos.capture.mode":s.get("capture_mode","METADATA_ONLY"),"amos.run.id":run_id,"amos.build.id":build_id,"amos.observed.at.unix_nano":_ns(float(s.get("observed_at",s.get("event_time",0)))),"amos.event.time.unix_nano":_ns(float(s.get("event_time",0)))}
            for src,dst in (("subject_version","amos.subject.version"),("authority_ref","amos.authority.ref"),("correlation_id","amos.correlation.id"),("input_hash","amos.input.sha256"),("output_hash","amos.output.sha256")):
                if s.get(src) not in (None,""):attrs[dst]=s[src]
            if s.get("error_type"):attrs["error.type"]=s["error_type"]
            if s.get("error_message"):attrs["amos.error.message.redacted"]=s["error_message"]
            status=str(s.get("status","UNSET")); attrs["amos.span.status"]=status
            item={"traceId":_b64_hex(str(s["trace_id"]),16,"trace_id"),"spanId":_b64_hex(str(s["span_id"]),8,"span_id"),"name":str(s.get("name") or s.get("kind") or "amos-span"),"kind":1,"startTimeUnixNano":_ns(float(s.get("started_at",s.get("event_time",0)))),"endTimeUnixNano":_ns(float(s.get("ended_at") or s.get("observed_at") or s.get("event_time",0))),"attributes":_kv(attrs),"status":{"code":1 if status=="OK" else 2 if status=="ERROR" else 0}}
            if s.get("parent_span_id"):item["parentSpanId"]=_b64_hex(str(s["parent_span_id"]),8,"parent_span_id")
            out.append(item)
        return {"resourceSpans":[{"resource":{"attributes":_kv({"service.name":service_name,"amos.run.id":run_id,"amos.build.id":build_id})},"scopeSpans":[{"scope":{"name":scope_name,"version":scope_version},"spans":out}]}]}

class TransportQueue:
    """Durable local telemetry outbox. HTTP ACK is not read-back verification."""
    def __init__(self,db_path:str|Path,*,max_active:int=1000):
        if max_active<1:raise TransportContractError("max_active must be >= 1")
        self.path=str(db_path); self.max_active=max_active; self.db=sqlite3.connect(self.path); self.db.row_factory=sqlite3.Row; self._init(); self.recover_inflight()
    def close(self)->None:self.db.close()
    def _init(self)->None:
        self.db.executescript("""CREATE TABLE IF NOT EXISTS exports(export_id TEXT PRIMARY KEY,trace_id TEXT NOT NULL,run_id TEXT NOT NULL,build_id TEXT NOT NULL,endpoint TEXT NOT NULL,payload_json TEXT NOT NULL,payload_hash TEXT NOT NULL,state TEXT NOT NULL,attempt_count INTEGER NOT NULL DEFAULT 0,created_at REAL NOT NULL,updated_at REAL NOT NULL,next_attempt_at REAL,last_http_status INTEGER,last_error TEXT,ack_hash TEXT,partial_rejected_spans INTEGER NOT NULL DEFAULT 0,partial_error_message TEXT,last_retry_after REAL);CREATE TABLE IF NOT EXISTS transport_ledger(seq INTEGER PRIMARY KEY AUTOINCREMENT,export_id TEXT NOT NULL,event_type TEXT NOT NULL,payload_json TEXT NOT NULL,prev_hash TEXT,event_hash TEXT NOT NULL,recorded_at REAL NOT NULL);"""); self.db.commit()
    def _ledger(self,eid:str,event:str,payload:dict[str,Any])->None:
        r=self.db.execute("SELECT event_hash FROM transport_ledger ORDER BY seq DESC LIMIT 1").fetchone(); prev=r[0] if r else None; body={"export_id":eid,"event_type":event,"payload":payload,"prev_hash":prev}
        self.db.execute("INSERT INTO transport_ledger(export_id,event_type,payload_json,prev_hash,event_hash,recorded_at) VALUES(?,?,?,?,?,?)",(eid,event,_json(payload),prev,_sha(body),_now()))
    def _row(self,eid:str)->sqlite3.Row:
        r=self.db.execute("SELECT * FROM exports WHERE export_id=?",(eid,)).fetchone()
        if not r:raise TransportContractError("export not found")
        return r
    def enqueue(self,*,trace_id:str,run_id:str,build_id:str,endpoint:str,payload:dict[str,Any])->str:
        u=urlparse(endpoint)
        if u.scheme not in {"http","https"} or not u.netloc:raise TransportContractError("endpoint must be absolute http(s) URL")
        active=self.db.execute("SELECT COUNT(*) FROM exports WHERE state NOT IN ('ACKED','PARTIAL','PERMANENT_FAILURE','PROTOCOL_ERROR','RECONCILED_PRESENT')").fetchone()[0]
        if active>=self.max_active:raise TransportContractError("transport queue capacity exceeded")
        eid=uuid.uuid4().hex; now=_now(); raw=_json(payload); ph=hashlib.sha256(raw.encode()).hexdigest()
        self.db.execute("INSERT INTO exports(export_id,trace_id,run_id,build_id,endpoint,payload_json,payload_hash,state,created_at,updated_at) VALUES(?,?,?,?,?,?,?,?,?,?)",(eid,trace_id,run_id,build_id,endpoint,raw,ph,"QUEUED",now,now)); self._ledger(eid,"ENQUEUED",{"trace_id":trace_id,"payload_hash":ph,"endpoint_origin":f"{u.scheme}://{u.netloc}"}); self.db.commit(); return eid
    def begin_attempt(self,eid:str,*,now:float|None=None)->dict[str,Any]:
        r=self._row(eid)
        if r["state"] not in SENDABLE_EXPORT_STATES:raise TransportContractError(f"export state {r['state']} is not directly sendable")
        cur=_now() if now is None else float(now)
        if r["next_attempt_at"] is not None and cur<r["next_attempt_at"]:raise TransportContractError("retry is not due yet")
        n=r["attempt_count"]+1; self.db.execute("UPDATE exports SET state='SENDING',attempt_count=?,updated_at=?,last_error=NULL WHERE export_id=?",(n,cur,eid)); self._ledger(eid,"ATTEMPT_STARTED",{"attempt":n}); self.db.commit(); return dict(self._row(eid))
    def mark_response(self,eid:str,*,http_status:int,response_body:bytes|str|None,headers:dict[str,str]|None=None,retry_policy:RetryPolicy|None=None,now:float|None=None,rng:Callable[[],float]=random.random)->str:
        r=self._row(eid)
        if r["state"]!="SENDING":raise TransportContractError("response can only finish a SENDING attempt")
        cur=_now() if now is None else float(now); h={str(k).lower():str(v) for k,v in (headers or {}).items()}; policy=retry_policy or RetryPolicy(); policy.validate()
        body={}; valid=False
        if response_body not in (None,b"",""):
            try:
                v=json.loads(response_body.decode() if isinstance(response_body,bytes) else str(response_body)); valid=isinstance(v,dict); body=v if valid else {}
            except (UnicodeDecodeError,json.JSONDecodeError):pass
        state="PERMANENT_FAILURE"; nxt=retry=partial_msg=err=ack=None; rejected=0
        if http_status==200:
            if h.get("content-type","").split(";",1)[0].strip().lower()!="application/json" or not valid:state="PROTOCOL_ERROR"; err="HTTP 200 did not contain a valid OTLP/HTTP JSON response"
            else:
                present="partialSuccess" in body or "partial_success" in body; part=body.get("partialSuccess",body.get("partial_success",{})) or {}
                if isinstance(part,dict):
                    try:rejected=int(part.get("rejectedSpans",part.get("rejected_spans",0)) or 0)
                    except (TypeError,ValueError):rejected=0
                    partial_msg=part.get("errorMessage",part.get("error_message"))
                state="PARTIAL" if present else "ACKED"; ack=hashlib.sha256((str(http_status)+"\n"+_json(body)).encode()).hexdigest()
        elif http_status==400:err="HTTP 400 permanent bad data"
        elif http_status in {429,503}:
            state="RETRYABLE"; retry=self._retry_after(h.get("retry-after"),cur) or policy.delay(r["attempt_count"],rng); nxt=cur+retry; err=f"HTTP {http_status} retryable"
        elif http_status in {502,504}:
            state="RETRYABLE"; retry=policy.delay(r["attempt_count"],rng); nxt=cur+retry; err=f"HTTP {http_status} retryable OTLP response"
        else:err=f"HTTP {http_status} not classified as retryable"
        if state=="RETRYABLE" and r["attempt_count"]>=policy.max_attempts:state="PERMANENT_FAILURE"; nxt=None; err=f"retry budget exhausted after {r['attempt_count']} attempts"
        self.db.execute("UPDATE exports SET state=?,updated_at=?,next_attempt_at=?,last_http_status=?,last_error=?,ack_hash=?,partial_rejected_spans=?,partial_error_message=?,last_retry_after=? WHERE export_id=?",(state,cur,nxt,int(http_status),err,ack,rejected,partial_msg,retry,eid)); self._ledger(eid,"ATTEMPT_RESPONSE",{"http_status":int(http_status),"state":state,"partial_rejected_spans":rejected,"retry_after_seconds":retry}); self.db.commit(); return state
    def mark_network_outcome_unknown(self,eid:str,error:str,*,now:float|None=None)->None:
        r=self._row(eid)
        if r["state"]!="SENDING":raise TransportContractError("network ambiguity can only finish a SENDING attempt")
        self.db.execute("UPDATE exports SET state='IN_DOUBT',updated_at=?,last_error=?,next_attempt_at=NULL WHERE export_id=?",(_now() if now is None else float(now),str(error)[:1000],eid)); self._ledger(eid,"OUTCOME_UNKNOWN",{"error_type":"NETWORK_OR_TIMEOUT"}); self.db.commit()
    def reconcile_in_doubt(self,eid:str,*,observed_in_backend:bool,evidence_ref:str)->str:
        if self._row(eid)["state"]!="IN_DOUBT":raise TransportContractError("only IN_DOUBT exports can be reconciled")
        if not evidence_ref:raise TransportContractError("reconciliation requires evidence_ref")
        state="RECONCILED_PRESENT" if observed_in_backend else "QUEUED"; ack=_sha({"export_id":eid,"evidence_ref":evidence_ref,"reconciled_present":True}) if observed_in_backend else None
        self.db.execute("UPDATE exports SET state=?,updated_at=?,next_attempt_at=NULL,ack_hash=?,last_error=NULL WHERE export_id=?",(state,_now(),ack,eid)); self._ledger(eid,"RECONCILED",{"observed_in_backend":bool(observed_in_backend),"evidence_ref_hash":hashlib.sha256(evidence_ref.encode()).hexdigest()}); self.db.commit(); return state
    def recover_inflight(self)->int:
        rows=self.db.execute("SELECT export_id FROM exports WHERE state='SENDING'").fetchall()
        for r in rows:self.db.execute("UPDATE exports SET state='IN_DOUBT',updated_at=?,last_error='process restarted during SENDING' WHERE export_id=?",(_now(),r["export_id"])); self._ledger(r["export_id"],"RECOVERED_AS_IN_DOUBT",{})
        self.db.commit(); return len(rows)
    def get(self,eid:str)->dict[str,Any]:return dict(self._row(eid))
    def receipt(self,eid:str)->dict[str,Any]:
        r=self.get(eid); p={"export_id":r["export_id"],"trace_id":r["trace_id"],"run_id":r["run_id"],"build_id":r["build_id"],"payload_hash":r["payload_hash"],"state":r["state"],"attempt_count":r["attempt_count"],"last_http_status":r["last_http_status"],"ack_hash":r["ack_hash"],"partial_rejected_spans":r["partial_rejected_spans"],"transport_semantics":"HTTP_ACK_IS_NOT_BACKEND_READBACK_VERIFICATION","authority_semantics":"TRANSPORT_DOES_NOT_GRANT_AUTHORITY"}; p["receipt_hash"]=_sha(p); return p
    def verify_integrity(self)->list[str]:
        e=[]; prev=None
        for r in self.db.execute("SELECT * FROM transport_ledger ORDER BY seq"):
            b={"export_id":r["export_id"],"event_type":r["event_type"],"payload":json.loads(r["payload_json"]),"prev_hash":r["prev_hash"]}
            if r["prev_hash"]!=prev:e.append(f"transport ledger prev_hash mismatch at seq {r['seq']}")
            if r["event_hash"]!=_sha(b):e.append(f"transport ledger event_hash mismatch at seq {r['seq']}")
            prev=r["event_hash"]
        for r in self.db.execute("SELECT * FROM exports"):
            if r["state"] not in EXPORT_STATES:e.append(f"invalid export state {r['state']} for {r['export_id']}")
            if hashlib.sha256(r["payload_json"].encode()).hexdigest()!=r["payload_hash"]:e.append(f"payload hash mismatch for {r['export_id']}")
        return e
    @staticmethod
    def _retry_after(v:str|None,now:float)->float|None:
        if not v:return None
        try:return max(0.0,float(v.strip()))
        except ValueError:
            try:return max(0.0,parsedate_to_datetime(v.strip()).timestamp()-now)
            except (TypeError,ValueError,OverflowError):return None

class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,req,fp,code,msg,headers,newurl):return None

class OtlpHttpJsonClient:
    def __init__(self,*,timeout:float=5.0):
        if timeout<=0:raise TransportContractError("timeout must be positive")
        self.timeout=timeout; self.opener=urllib.request.build_opener(_NoRedirect())
    def send_once(self,q:TransportQueue,eid:str,*,headers:dict[str,str]|None=None,retry_policy:RetryPolicy|None=None,now:float|None=None,rng:Callable[[],float]=random.random)->str:
        hs={"Content-Type":"application/json","Accept":"application/json"}
        for k,v in (headers or {}).items():
            k=str(k); v=str(v)
            if any(c in k or c in v for c in ("\n","\r")):raise TransportContractError("header contains newline")
            hs[k]=v
        r=q.begin_attempt(eid,now=now); req=urllib.request.Request(r["endpoint"],data=r["payload_json"].encode(),headers=hs,method="POST")
        try:
            with self.opener.open(req,timeout=self.timeout) as resp:return q.mark_response(eid,http_status=resp.status,response_body=resp.read(),headers=dict(resp.headers.items()),retry_policy=retry_policy,now=now,rng=rng)
        except urllib.error.HTTPError as exc:return q.mark_response(eid,http_status=exc.code,response_body=exc.read(),headers=dict(exc.headers.items()) if exc.headers else {},retry_policy=retry_policy,now=now,rng=rng)
        except (urllib.error.URLError,TimeoutError,OSError) as exc:q.mark_network_outcome_unknown(eid,f"{type(exc).__name__}: {exc}",now=now); return "IN_DOUBT"

class RoundTripVerifier:
    @staticmethod
    def verify(*,trace_id:str,run_id:str,build_id:str,expected_spans:Iterable[dict[str,Any]],observed_spans:Iterable[dict[str,Any]])->dict[str,Any]:
        er=[dict(s) for s in expected_spans]; ors=[dict(s) for s in observed_spans]; exp={str(s["span_id"]):s for s in er}; obs={}; dup=[]; contamination=[]
        for s in ors:
            sid=str(s.get("span_id",''))
            if not sid:contamination.append("observed span missing span_id"); continue
            if sid in obs:dup.append(sid)
            obs[sid]=s; attrs=s.get("attributes") or {}
            if str(s.get("trace_id"))!=trace_id:contamination.append(f"span {sid} trace_id mismatch")
            if attrs.get("amos.run.id")!=run_id:contamination.append(f"span {sid} run_id mismatch")
            if attrs.get("amos.build.id")!=build_id:contamination.append(f"span {sid} build_id mismatch")
        missing=sorted(set(exp)-set(obs)); extra=sorted(set(obs)-set(exp)); mism=[]
        for sid in sorted(set(exp)&set(obs)):
            e,o=exp[sid],obs[sid]
            if (o.get("parent_span_id") or None)!=(e.get("parent_span_id") or None):mism.append(f"span {sid} parent mismatch")
            if str(o.get("name"))!=str(e.get("name")):mism.append(f"span {sid} name mismatch")
            attrs=o.get("attributes") or {}; req={"amos.span.kind":e.get("kind","UNKNOWN"),"amos.subject":e.get("subject",""),"amos.provenance.root":e.get("provenance_root",""),"amos.environment":e.get("environment",""),"amos.effect.state":e.get("effect_state","NONE"),"amos.capture.mode":e.get("capture_mode","METADATA_ONLY"),"amos.run.id":run_id,"amos.build.id":build_id}
            for k,v in req.items():
                if attrs.get(k)!=v:mism.append(f"span {sid} attribute {k} mismatch")
        ok=not(dup or contamination or missing or extra or mism); p={"trace_id":trace_id,"run_id":run_id,"build_id":build_id,"status":"VERIFIED_ROUNDTRIP" if ok else "NOT_VERIFIED","expected_span_count":len(er),"observed_span_count":len(ors),"missing_span_ids":missing,"extra_span_ids":extra,"duplicate_span_ids":sorted(set(dup)),"mismatches":mism,"contamination":contamination,"authority_semantics":"ROUNDTRIP_EVIDENCE_DOES_NOT_GRANT_AUTHORITY","causal_semantics":"READBACK_MATCH_DOES_NOT_PROVE_CAUSALITY"}; p["receipt_hash"]=_sha(p); return p
    @staticmethod
    def normalize_phoenix(records:Iterable[dict[str,Any]])->list[dict[str,Any]]:
        out=[]
        for r in records:
            c=r.get("context") or {}; a=r.get("attributes") or {}; out.append({"trace_id":r.get("trace_id") or c.get("trace_id"),"span_id":r.get("span_id") or c.get("span_id"),"parent_span_id":r.get("parent_span_id",r.get("parent_id")),"name":r.get("name"),"status":r.get("status") or r.get("status_code"),"attributes":{k:v for k,v in a.items() if str(k).startswith("amos.")}})
        return out
