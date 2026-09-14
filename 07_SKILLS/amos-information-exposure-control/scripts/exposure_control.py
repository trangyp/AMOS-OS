#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, sqlite3, time, uuid
from pathlib import Path
from typing import Any

STATES={"COMMITTABLE_EXPOSURE","REVALIDATE_ORIGIN","REVALIDATE_ACCOUNTANT","REVALIDATE_MISSING_PROOF","REVALIDATE_PROOF_JOIN","BLOCK_BUDGET","DENY_POLICY","UNKNOWN_GAP"}
ACCOUNTANT_KIND="POLICY_UNIT_SUM"
FORBIDDEN={"password","secret","token","api_key","credential","raw_input","raw_output","chain_of_thought","reasoning"}

class ExposureError(RuntimeError): pass

def canon(v:Any)->str:return json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False)
def sha(v:Any)->str:return hashlib.sha256(canon(v).encode()).hexdigest()
def now_ns()->int:return time.time_ns()
def nonempty(name:str,v:Any)->str:
    if not isinstance(v,str) or not v.strip(): raise ExposureError(f"{name} must be non-empty string")
    return v.strip()
def reject_sensitive(v:Any,path:str="$")->None:
    if isinstance(v,dict):
        for k,c in v.items():
            if str(k).lower() in FORBIDDEN: raise ExposureError(f"sensitive key forbidden: {path}.{k}")
            reject_sensitive(c,f"{path}.{k}")
    elif isinstance(v,list):
        for i,c in enumerate(v): reject_sensitive(c,f"{path}[{i}]")
def ledger_hash(prev:str,kind:str,payload:str,ts:int)->str:return hashlib.sha256(f"{prev}|{kind}|{payload}|{ts}".encode()).hexdigest()

JOIN_FIELDS=("effect_hash","semantic_transaction_hash","policy_id","policy_version","policy_epoch","authority_hash","environment_hash","capability_contract_hash","proof_epoch")

def validate_proof_join(join:dict[str,Any])->dict[str,Any]:
    reject_sensitive(join)
    req=join.get("required_skills")
    proofs=join.get("proofs")
    if not isinstance(req,list) or not req or not all(isinstance(x,str) and x for x in req):
        return {"state":"REVALIDATE_MISSING_PROOF","reason":"invalid_required_skills"}
    if not isinstance(proofs,list): return {"state":"REVALIDATE_MISSING_PROOF","reason":"proofs_missing"}
    by={}
    for p in proofs:
        if not isinstance(p,dict): return {"state":"REVALIDATE_PROOF_JOIN","reason":"malformed_proof"}
        sid=p.get("skill_id")
        if not isinstance(sid,str) or not sid or sid in by: return {"state":"REVALIDATE_PROOF_JOIN","reason":"duplicate_or_missing_skill_id"}
        by[sid]=p
    missing=[s for s in req if s not in by]
    if missing:return {"state":"REVALIDATE_MISSING_PROOF","missing":sorted(missing)}
    selected=[by[s] for s in req]
    if any(p.get("decision")!="PASS" for p in selected):return {"state":"REVALIDATE_PROOF_JOIN","reason":"required_proof_not_pass"}
    for f in JOIN_FIELDS:
        vals={canon(p.get(f)) for p in selected}
        if len(vals)!=1 or next(iter(vals)) in {"null","\"\""}:return {"state":"REVALIDATE_PROOF_JOIN","reason":f"mismatch_or_missing:{f}"}
    return {"state":"JOINT_PROOF_PASS","proof_ids":sorted(str(p.get("proof_id","")) for p in selected),"join_hash":sha({"required":sorted(req),"bindings":{f:selected[0][f] for f in JOIN_FIELDS},"proof_ids":sorted(str(p.get("proof_id","")) for p in selected)})}

class ExposureRuntime:
    def __init__(self,db_path:str|Path=":memory:"):
        self.db=sqlite3.connect(str(db_path),isolation_level=None); self.db.row_factory=sqlite3.Row; self._init()
    def close(self):self.db.close()
    def __enter__(self):return self
    def __exit__(self,*_):self.close()
    def _init(self):
        self.db.executescript("""
        CREATE TABLE IF NOT EXISTS control_state(singleton INTEGER PRIMARY KEY CHECK(singleton=1),policy_id TEXT NOT NULL,policy_version TEXT NOT NULL,policy_epoch INTEGER NOT NULL,exposure_epoch INTEGER NOT NULL,accountant_id TEXT NOT NULL,accountant_version TEXT NOT NULL,accountant_kind TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS origins(origin_id TEXT PRIMARY KEY,limit_units INTEGER NOT NULL,allowed_coalitions_json TEXT NOT NULL,policy_id TEXT NOT NULL,policy_version TEXT NOT NULL,policy_epoch INTEGER NOT NULL,exposure_epoch INTEGER NOT NULL,accountant_id TEXT NOT NULL,accountant_version TEXT NOT NULL,accountant_kind TEXT NOT NULL,object_hash TEXT NOT NULL,created_at_ns INTEGER NOT NULL);
        CREATE TABLE IF NOT EXISTS aliases(alias_id TEXT PRIMARY KEY,origin_id TEXT NOT NULL REFERENCES origins(origin_id));
        CREATE TABLE IF NOT EXISTS usage(origin_id TEXT NOT NULL REFERENCES origins(origin_id),coalition_id TEXT NOT NULL,used_units INTEGER NOT NULL DEFAULT 0,PRIMARY KEY(origin_id,coalition_id));
        CREATE TABLE IF NOT EXISTS releases(release_id TEXT PRIMARY KEY,state TEXT NOT NULL,request_hash TEXT NOT NULL,receipt_json TEXT NOT NULL,receipt_hash TEXT NOT NULL,created_at_ns INTEGER NOT NULL);
        CREATE TABLE IF NOT EXISTS ledger(seq INTEGER PRIMARY KEY AUTOINCREMENT,kind TEXT NOT NULL,payload_json TEXT NOT NULL,ts_ns INTEGER NOT NULL,prev_hash TEXT NOT NULL,event_hash TEXT NOT NULL);
        """)
    def event(self,kind:str,payload:dict[str,Any])->str:
        reject_sensitive(payload); p=canon(payload); row=self.db.execute("select event_hash from ledger order by seq desc limit 1").fetchone(); prev=row[0] if row else "0"*64; ts=now_ns(); h=ledger_hash(prev,kind,p,ts); self.db.execute("insert into ledger(kind,payload_json,ts_ns,prev_hash,event_hash) values(?,?,?,?,?)",(kind,p,ts,prev,h)); return h
    def set_control_state(self,**k):
        for x in ("policy_id","policy_version","accountant_id","accountant_version","accountant_kind"):nonempty(x,k.get(x))
        if k["accountant_kind"]!=ACCOUNTANT_KIND: raise ExposureError("unsupported accountant kind")
        pe,ee=k.get("policy_epoch"),k.get("exposure_epoch")
        if not isinstance(pe,int) or pe<0 or not isinstance(ee,int) or ee<0:raise ExposureError("epochs must be non-negative integers")
        old=self.db.execute("select * from control_state where singleton=1").fetchone()
        if old and (pe<old["policy_epoch"] or ee<old["exposure_epoch"]):raise ExposureError("control epoch rollback")
        self.db.execute("insert into control_state values(1,?,?,?,?,?,?,?) on conflict(singleton) do update set policy_id=excluded.policy_id,policy_version=excluded.policy_version,policy_epoch=excluded.policy_epoch,exposure_epoch=excluded.exposure_epoch,accountant_id=excluded.accountant_id,accountant_version=excluded.accountant_version,accountant_kind=excluded.accountant_kind",(k["policy_id"],k["policy_version"],pe,ee,k["accountant_id"],k["accountant_version"],k["accountant_kind"]))
        self.event("CONTROL_STATE",dict(k))
    def register_origin(self,*,origin_id:str,limit_units:int,allowed_coalitions:list[str],policy_id:str,policy_version:str,policy_epoch:int,exposure_epoch:int,accountant_id:str,accountant_version:str,accountant_kind:str=ACCOUNTANT_KIND)->str:
        origin_id=nonempty("origin_id",origin_id); allowed=sorted({nonempty("coalition",x) for x in allowed_coalitions}) if isinstance(allowed_coalitions,list) else []
        if not allowed:raise ExposureError("allowed_coalitions must be non-empty")
        if not isinstance(limit_units,int) or limit_units<0:raise ExposureError("limit_units must be non-negative integer")
        if accountant_kind!=ACCOUNTANT_KIND:raise ExposureError("unsupported accountant kind")
        obj={"origin_id":origin_id,"limit_units":limit_units,"allowed_coalitions":allowed,"policy_id":nonempty("policy_id",policy_id),"policy_version":nonempty("policy_version",policy_version),"policy_epoch":policy_epoch,"exposure_epoch":exposure_epoch,"accountant_id":nonempty("accountant_id",accountant_id),"accountant_version":nonempty("accountant_version",accountant_version),"accountant_kind":accountant_kind}
        h=sha(obj); self.db.execute("insert into origins values(?,?,?,?,?,?,?,?,?,?,?,?)",(origin_id,limit_units,canon(allowed),policy_id,policy_version,policy_epoch,exposure_epoch,accountant_id,accountant_version,accountant_kind,h,now_ns())); self.db.execute("insert into aliases values(?,?)",(origin_id,origin_id)); self.event("ORIGIN_REGISTERED",{"origin_id":origin_id,"object_hash":h}); return h
    def add_alias(self,alias_id:str,origin_id:str):
        alias_id=nonempty("alias_id",alias_id); origin_id=nonempty("origin_id",origin_id)
        if not self.db.execute("select 1 from origins where origin_id=?",(origin_id,)).fetchone():raise ExposureError("unknown origin")
        self.db.execute("insert into aliases values(?,?)",(alias_id,origin_id)); self.event("ALIAS_ADDED",{"alias_id":alias_id,"origin_id":origin_id})
    def resolve(self,ref:str)->str|None:
        row=self.db.execute("select origin_id from aliases where alias_id=?",(ref,)).fetchone(); return row[0] if row else None
    def _origin_valid(self,row:sqlite3.Row,ctl:sqlite3.Row)->bool:
        obj={"origin_id":row["origin_id"],"limit_units":row["limit_units"],"allowed_coalitions":json.loads(row["allowed_coalitions_json"]),"policy_id":row["policy_id"],"policy_version":row["policy_version"],"policy_epoch":row["policy_epoch"],"exposure_epoch":row["exposure_epoch"],"accountant_id":row["accountant_id"],"accountant_version":row["accountant_version"],"accountant_kind":row["accountant_kind"]}
        return row["object_hash"]==sha(obj) and all(row[k]==ctl[k] for k in ("policy_id","policy_version","policy_epoch","exposure_epoch","accountant_id","accountant_version","accountant_kind"))
    def _evaluate(self,request:dict[str,Any])->tuple[str,list[str],dict[str,int],dict[str,Any]|None]:
        try:reject_sensitive(request)
        except ExposureError as e:return "UNKNOWN_GAP",[str(e)],{},None
        required=("coalition_id","effect_hash","semantic_transaction_hash","authorization_receipt_hash","environment_hash","capability_contract_hash","policy_id","policy_version","policy_epoch","exposure_epoch","proof_epoch","charges","required_skills","proofs")
        if any(k not in request for k in required):return "UNKNOWN_GAP",["missing_required_field"],{},None
        ctl=self.db.execute("select * from control_state where singleton=1").fetchone()
        if not ctl:return "UNKNOWN_GAP",["control_state_missing"],{},None
        if request["policy_id"]!=ctl["policy_id"] or request["policy_version"]!=ctl["policy_version"] or request["policy_epoch"]!=ctl["policy_epoch"] or request["exposure_epoch"]!=ctl["exposure_epoch"]:return "DENY_POLICY",["stale_or_wrong_policy_state"],{},None
        coalition=nonempty("coalition_id",request["coalition_id"])
        charges=request["charges"]
        if not isinstance(charges,list) or not charges:return "REVALIDATE_ORIGIN",["charges_missing"],{},None
        agg:dict[str,int]={}
        for c in charges:
            if not isinstance(c,dict) or not isinstance(c.get("units"),int) or c.get("units")<=0 or not isinstance(c.get("origin_ref"),str):return "REVALIDATE_ORIGIN",["invalid_charge"],{},None
            origin=self.resolve(c["origin_ref"])
            if not origin:return "REVALIDATE_ORIGIN",[f"unresolved_origin:{c['origin_ref']}"],{},None
            agg[origin]=agg.get(origin,0)+c["units"]
        for origin,units in agg.items():
            row=self.db.execute("select * from origins where origin_id=?",(origin,)).fetchone()
            if not row or not self._origin_valid(row,ctl):return "REVALIDATE_ACCOUNTANT",[f"origin_or_accountant_stale:{origin}"],agg,None
            if coalition not in json.loads(row["allowed_coalitions_json"]):return "DENY_POLICY",[f"coalition_not_allowed:{origin}"],agg,None
            used=self.db.execute("select used_units from usage where origin_id=? and coalition_id=?",(origin,coalition)).fetchone(); u=used[0] if used else 0
            if u+units>row["limit_units"]:return "BLOCK_BUDGET",[f"budget_exceeded:{origin}"],agg,None
        join=validate_proof_join({"required_skills":request["required_skills"],"proofs":request["proofs"]})
        if join["state"]!="JOINT_PROOF_PASS":return join["state"],[join.get("reason","proof_join_failed")],agg,join
        p0=next(p for p in request["proofs"] if p["skill_id"] in request["required_skills"])
        bindings={"effect_hash":request["effect_hash"],"semantic_transaction_hash":request["semantic_transaction_hash"],"policy_id":request["policy_id"],"policy_version":request["policy_version"],"policy_epoch":request["policy_epoch"],"environment_hash":request["environment_hash"],"capability_contract_hash":request["capability_contract_hash"],"proof_epoch":request["proof_epoch"]}
        for f,v in bindings.items():
            if p0.get(f)!=v:return "REVALIDATE_PROOF_JOIN",[f"release_proof_binding_mismatch:{f}"],agg,join
        return "COMMITTABLE_EXPOSURE",[],agg,join
    def preflight(self,request:dict[str,Any])->dict[str,Any]:
        state,reasons,agg,join=self._evaluate(request); return self._receipt("PREFLIGHT",state,request,reasons,agg,join)
    def commit(self,request:dict[str,Any])->dict[str,Any]:
        self.db.execute("BEGIN IMMEDIATE")
        try:
            state,reasons,agg,join=self._evaluate(request)
            if state=="COMMITTABLE_EXPOSURE":
                coalition=request["coalition_id"]
                for origin,units in agg.items(): self.db.execute("insert into usage(origin_id,coalition_id,used_units) values(?,?,?) on conflict(origin_id,coalition_id) do update set used_units=used_units+excluded.used_units",(origin,coalition,units))
            out=self._receipt("COMMIT",state,request,reasons,agg,join,write=False)
            self.db.execute("insert into releases values(?,?,?,?,?,?)",(out["release_id"],state,out["request_hash"],canon(out),out["receipt_hash"],now_ns())); self.event("EXPOSURE_DECISION",{"release_id":out["release_id"],"state":state,"receipt_hash":out["receipt_hash"]}); self.db.execute("COMMIT"); return out
        except Exception:
            self.db.execute("ROLLBACK"); raise
    def _receipt(self,phase,state,request,reasons,agg,join,write=True):
        release_id=str(uuid.uuid4()); core={"release_id":release_id,"phase":phase,"state":state,"request_hash":sha(request),"canonical_charges":dict(sorted(agg.items())),"proof_join_hash":join.get("join_hash") if join else None,"reasons":sorted(reasons),"authority_semantics":"EXPOSURE_DECISION_DOES_NOT_GRANT_EFFECT_COMMIT_AUTHORITY","accountant_semantics":"POLICY_UNIT_SUM_IS_NOT_DIFFERENTIAL_PRIVACY_EPSILON"}; core["receipt_hash"]=sha(core)
        if write:self.event("EXPOSURE_PREFLIGHT",{"release_id":release_id,"state":state,"receipt_hash":core["receipt_hash"]})
        return core
    def usage(self,origin_id:str,coalition_id:str)->int:
        row=self.db.execute("select used_units from usage where origin_id=? and coalition_id=?",(origin_id,coalition_id)).fetchone();return row[0] if row else 0
    def verify_ledger(self)->bool:
        prev="0"*64
        for r in self.db.execute("select * from ledger order by seq"):
            if r["prev_hash"]!=prev or ledger_hash(prev,r["kind"],r["payload_json"],r["ts_ns"])!=r["event_hash"]:return False
            prev=r["event_hash"]
        return True

def self_test()->None:
    r=ExposureRuntime();r.set_control_state(policy_id="p",policy_version="1",policy_epoch=1,exposure_epoch=1,accountant_id="a",accountant_version="1",accountant_kind=ACCOUNTANT_KIND);r.register_origin(origin_id="o",limit_units=3,allowed_coalitions=["c"],policy_id="p",policy_version="1",policy_epoch=1,exposure_epoch=1,accountant_id="a",accountant_version="1");r.add_alias("alias","o")
    p={"proof_id":"x","skill_id":"s","decision":"PASS","effect_hash":"e","semantic_transaction_hash":"t","policy_id":"p","policy_version":"1","policy_epoch":1,"authority_hash":"au","environment_hash":"env","capability_contract_hash":"cap","proof_epoch":1}
    q={"coalition_id":"c","effect_hash":"e","semantic_transaction_hash":"t","authorization_receipt_hash":"ar","environment_hash":"env","capability_contract_hash":"cap","policy_id":"p","policy_version":"1","policy_epoch":1,"exposure_epoch":1,"proof_epoch":1,"charges":[{"origin_ref":"alias","units":2}],"required_skills":["s"],"proofs":[p]}
    assert r.commit(q)["state"]=="COMMITTABLE_EXPOSURE" and r.usage("o","c")==2 and r.verify_ledger();r.close();print("exposure_control self-test: PASS")

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--self-test",action="store_true");a=ap.parse_args()
    if a.self_test:self_test()
if __name__=="__main__":main()
