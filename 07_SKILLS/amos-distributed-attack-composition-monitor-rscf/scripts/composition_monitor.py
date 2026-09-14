#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, itertools, json, sqlite3, time
from pathlib import Path
from typing import Any
FORBIDDEN={"password","secret","token","api_key","credential","raw_input","raw_output","chain_of_thought","reasoning"}
VERDICTS={"ALLOW","DENY","UNKNOWN"}
class MonitorError(RuntimeError): pass
def canon(v:Any)->str:return json.dumps(v,sort_keys=True,separators=(",",":"),ensure_ascii=False)
def sha(v:Any)->str:return hashlib.sha256(canon(v).encode()).hexdigest()
def now_ns()->int:return time.time_ns()
def reject(v:Any,p='root'):
    if isinstance(v,dict):
        for k,x in v.items():
            if str(k).lower() in FORBIDDEN: raise MonitorError(f"sensitive field {p}.{k}")
            reject(x,f"{p}.{k}")
    elif isinstance(v,list):
        for i,x in enumerate(v): reject(x,f"{p}[{i}]")
def reqs(d,k):
    v=d.get(k)
    if not isinstance(v,str) or not v: raise MonitorError(f"{k} required")
    return v
class Monitor:
    def __init__(self,path=':memory:'):
        self.db=sqlite3.connect(str(path),isolation_level=None); self.db.row_factory=sqlite3.Row
        self.db.executescript('''
        CREATE TABLE IF NOT EXISTS rules(rule_id TEXT PRIMARY KEY, required_atoms TEXT NOT NULL,max_window_ns INTEGER NOT NULL,min_principals INTEGER NOT NULL,min_sessions INTEGER NOT NULL,policy_epoch INTEGER NOT NULL,severity TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS events(event_id TEXT PRIMARY KEY,ts_ns INTEGER NOT NULL,principal_id TEXT NOT NULL,session_id TEXT NOT NULL,repo_id TEXT NOT NULL,local_verdict TEXT NOT NULL,atoms TEXT NOT NULL,effect_hash TEXT NOT NULL,target_ref TEXT NOT NULL,policy_epoch INTEGER NOT NULL,provenance_ref TEXT NOT NULL,event_hash TEXT NOT NULL);
        CREATE TABLE IF NOT EXISTS ledger(seq INTEGER PRIMARY KEY AUTOINCREMENT,event_type TEXT NOT NULL,payload TEXT NOT NULL,prev_hash TEXT NOT NULL,entry_hash TEXT NOT NULL UNIQUE,created_ns INTEGER NOT NULL);
        ''')
    def close(self):self.db.close()
    def _ledger(self,t,p):
        reject(p); r=self.db.execute('SELECT entry_hash FROM ledger ORDER BY seq DESC LIMIT 1').fetchone(); prev=r[0] if r else '0'*64
        h=sha({'event_type':t,'payload':p,'prev_hash':prev}); self.db.execute('INSERT INTO ledger(event_type,payload,prev_hash,entry_hash,created_ns) VALUES(?,?,?,?,?)',(t,canon(p),prev,h,now_ns())); return h
    def verify_ledger(self):
        prev='0'*64
        for r in self.db.execute('SELECT * FROM ledger ORDER BY seq'):
            p=json.loads(r['payload']); h=sha({'event_type':r['event_type'],'payload':p,'prev_hash':prev})
            if r['prev_hash']!=prev or r['entry_hash']!=h:return False
            prev=h
        return True
    def add_rule(self,rule_id,required_atoms,max_window_ns,min_principals=1,min_sessions=1,policy_epoch=1,severity='HIGH'):
        if not required_atoms or max_window_ns<=0 or min_principals<1 or min_sessions<1: raise MonitorError('invalid rule')
        self.db.execute('INSERT INTO rules VALUES(?,?,?,?,?,?,?)',(rule_id,canon(sorted(set(required_atoms))),int(max_window_ns),int(min_principals),int(min_sessions),int(policy_epoch),severity))
        self._ledger('RULE_ADDED',{'rule_id':rule_id,'policy_epoch':policy_epoch,'severity':severity})
    def add_event(self,e):
        reject(e)
        eid=reqs(e,'event_id'); principal=reqs(e,'principal_id'); session=reqs(e,'session_id'); repo=reqs(e,'repo_id'); effect=reqs(e,'effect_hash'); target=reqs(e,'target_ref'); prov=reqs(e,'provenance_ref')
        verdict=e.get('local_verdict'); atoms=sorted(set(e.get('atoms') or [])); ts=int(e.get('ts_ns',-1)); epoch=int(e.get('policy_epoch',-1))
        if verdict not in VERDICTS or not atoms or ts<0 or epoch<0: raise MonitorError('invalid event')
        payload={"event_id":eid,"ts_ns":ts,"principal_id":principal,"session_id":session,"repo_id":repo,"local_verdict":verdict,"atoms":atoms,"effect_hash":effect,"target_ref":target,"policy_epoch":epoch,"provenance_ref":prov}
        h=sha(payload)
        self.db.execute('INSERT INTO events VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',(eid,ts,principal,session,repo,verdict,canon(atoms),effect,target,epoch,prov,h)); self._ledger('EVENT_ADDED',{'event_id':eid,'event_hash':h}); return h
    def _satisfies(self,rule,events):
        if not events:return False
        req=set(json.loads(rule['required_atoms'])); union=set().union(*(set(json.loads(e['atoms'])) for e in events))
        return req<=union and len({e['principal_id'] for e in events})>=rule['min_principals'] and len({e['session_id'] for e in events})>=rule['min_sessions']
    def evaluate(self,rule_id,as_of_ns,policy_epoch):
        rule=self.db.execute('SELECT * FROM rules WHERE rule_id=?',(rule_id,)).fetchone()
        if not rule:return {'status':'UNKNOWN_GAP','reason':'RULE_MISSING'}
        if rule['policy_epoch']!=int(policy_epoch):return {'status':'REVALIDATE_COMPOSITION','reason':'POLICY_EPOCH_MISMATCH'}
        lo=int(as_of_ns)-rule['max_window_ns']; rows=list(self.db.execute('SELECT * FROM events WHERE ts_ns BETWEEN ? AND ? AND local_verdict="ALLOW" ORDER BY ts_ns,event_id',(lo,int(as_of_ns))))
        if any(r['policy_epoch']!=int(policy_epoch) for r in rows):return {'status':'REVALIDATE_COMPOSITION','reason':'MIXED_EVENT_POLICY_EPOCH'}
        if not self._satisfies(rule,rows):return {'status':'NO_COMPOSITION_MATCH','rule_id':rule_id,'event_count':len(rows),'authority_semantics':'LOCAL_ALLOW_DOES_NOT_PROVE_GLOBAL_SAFE'}
        if len(rows)>12:return {'status':'UNKNOWN_GAP','reason':'MINIMAL_CUT_SEARCH_BOUND','event_count':len(rows)}
        cut=None
        for n in range(1,len(rows)+1):
            for combo in itertools.combinations(rows,n):
                if self._satisfies(rule,combo):cut=list(combo);break
            if cut:break
        ids=[r['event_id'] for r in cut or []]
        out={'schema':'amos.distributed-composition.v1','status':'BLOCK_COMPOSITION','rule_id':rule_id,'severity':rule['severity'],'policy_epoch':policy_epoch,'as_of_ns':int(as_of_ns),'minimal_event_ids':ids,'distinct_principals':len({r['principal_id'] for r in cut}), 'distinct_sessions':len({r['session_id'] for r in cut}),'authority_semantics':'COMPOSITION_MATCH_DOES_NOT_PROVE_ADVERSARIAL_INTENT_OR_GRANT_RESPONSE_AUTHORITY'}
        out['receipt_hash']=sha(out); self._ledger('COMPOSITION_MATCH',{'rule_id':rule_id,'minimal_event_ids':ids,'receipt_hash':out['receipt_hash']}); return out

def _self_test():
    m=Monitor(); m.add_rule('r',['A','B'],10**9,min_principals=2,min_sessions=2)
    t=now_ns()
    for i,(p,s,a) in enumerate([('p1','s1',['A']),('p2','s2',['B'])]):m.add_event({'event_id':str(i),'ts_ns':t+i,'principal_id':p,'session_id':s,'repo_id':'repo','local_verdict':'ALLOW','atoms':a,'effect_hash':'e'+str(i),'target_ref':'target','policy_epoch':1,'provenance_ref':'prov'})
    assert m.evaluate('r',t+2,1)['status']=='BLOCK_COMPOSITION'; assert m.verify_ledger(); m.close(); print('self-test: PASS')
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--self-test',action='store_true'); a=ap.parse_args()
    if a.self_test:_self_test()
if __name__=='__main__':main()
