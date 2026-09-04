---
title: AMOS Forex Quantitative Validation Engine
type: specification_contract
amos_core_target: v4.4
origin_architect: Trang Phan
status: ACTIVE_SPEC
conclusion_class: SOURCE_CLAIM
tags:
- amos
- core
- runtime
- kernel
- rscf
rscf:
  state: SOURCE_CLAIM
  claim_class: SOURCE_CLAIM
  provenance: authoritative_AMOS_CORE_source
  scope: active__21_DOMAINS
---

# AMOS Forex Quantitative Validation Engine

```python

from pathlib import Path
import json, math, hashlib
import numpy as np

SOURCE = Path("/mnt/data/forex.txt")
REPORT = Path("/mnt/data/amos_forex_gap_closed_validation_v2_report.json")
spec = json.loads(SOURCE.read_text(encoding="utf-8"))
rng = np.random.default_rng(20260814)

tests = []
def record(group, name, passed, detail=None):
    tests.append({
        "group": group,
        "name": name,
        "passed": bool(passed),
        "detail": detail or {}
    })

def gmean(xs):
    xs=np.asarray(xs,float)
    return float(np.prod(xs)**(1/len(xs)))

# ---------- Source-defined normalized H/M/L helpers ----------
# The source requires normalized values to remain in [0,1].
def clamp01(x): return float(min(1.0,max(0.0,x)))
def hml_raw(*xs): return [clamp01(x) for x in xs]
def bounded_index(xs, weights=None):
    xs=np.asarray(xs,float)
    if weights is None: weights=np.ones(len(xs))
    weights=np.asarray(weights,float)
    return float(np.dot(xs,weights)/weights.sum())

# ---------- Repaired bounded stability ----------
def stability(boundary, memory, repair, relation, entropy, contradiction, fragmentation, observer_variance):
    P = gmean([boundary,memory,repair,relation])
    D = gmean([1-entropy,1-contradiction,1-fragmentation,1-observer_variance])
    return math.sqrt(P*D)

# 1-17: FULL source-defined deterministic invariant suite.
raw = hml_raw(*rng.uniform(-2,3,10000))
record("source_invariants","HML raw values remain within 0..1",
       min(raw)>=0 and max(raw)<=1, {"min":min(raw),"max":max(raw)})

idx = [bounded_index(rng.random(8), rng.random(8)+1e-9) for _ in range(30000)]
record("source_invariants","bounded HML indices remain within 0..1",
       min(idx)>=0 and max(idx)<=1, {"min":min(idx),"max":max(idx)})

ss=[stability(*rng.random(8)) for _ in range(100000)]
record("source_invariants","bounded stability never explodes",
       min(ss)>=0 and max(ss)<=1, {"min":min(ss),"max":max(ss),"n":len(ss)})

viol=0
for _ in range(50000):
    b,m,r,rel,c,f,o=rng.random(7); e1,e2=sorted(rng.random(2))
    viol += stability(b,m,r,rel,e2,c,f,o) > stability(b,m,r,rel,e1,c,f,o)+1e-12
record("source_invariants","stability decreases when entropy increases all else equal",viol==0,{"violations":int(viol)})

viol=0
for _ in range(50000):
    b,m,rel,e,c,f,o=rng.random(7); r1,r2=sorted(rng.random(2))
    viol += stability(b,m,r2,rel,e,c,f,o)+1e-12 < stability(b,m,r1,rel,e,c,f,o)
record("source_invariants","stability increases when repair capacity increases all else equal",viol==0,{"violations":int(viol)})

fd=rng.lognormal(0,2,100000); ds=rng.lognormal(0,1,100000)
dp=1-np.exp(-fd/ds)
record("source_invariants","debt pressure remains in 0..1",
       float(dp.min())>=0 and float(dp.max())<=1,{"min":float(dp.min()),"max":float(dp.max())})

dist2=rng.gamma(2,1,(50000,6)); tau=rng.uniform(.1,4,(50000,1))
z=-dist2/(2*tau*tau); z-=z.max(axis=1,keepdims=True)
p=np.exp(z); p/=p.sum(axis=1,keepdims=True)
err=float(np.abs(p.sum(axis=1)-1).max())
record("source_invariants","regime probabilities sum to 1",err<1e-12,{"max_error":err})

def tat2(e1,e2,theta_ind=.70,theta_quality=.60):
    overlap=1.0 if e1["family"]==e2["family"] or e1["parent"]==e2["parent"] else 0.0
    dep=max(e1.get("dependence",0),e2.get("dependence",0))
    independence=1-max(overlap,dep)
    return independence>=theta_ind and e1["quality"]>=theta_quality and e2["quality"]>=theta_quality

record("source_invariants","duplicate-family Tát 2 fails",
       not tat2({"family":"momentum","parent":"price","quality":.9},
                {"family":"momentum","parent":"price","quality":.95}))
record("source_invariants","independent valid Tát 2 passes",
       tat2({"family":"structure","parent":"htf","quality":.8,"dependence":.1},
            {"family":"liquidity","parent":"flow","quality":.85,"dependence":.1}))

def evidence_valid(e):
    return (not e.get("expired",False)) and (not e.get("falsified",False)) and e.get("quality",1)>=.6

def gate(rr=2.0,news=False,stale=False,spread=False,tat2_ok=True,risk_ok=True,evidence=None):
    if evidence is None: evidence={"quality":1}
    if rr<2 or news or stale or spread or not tat2_ok or not risk_ok or not evidence_valid(evidence):
        return "NO_TRADE"
    return "TRADE"

for name, passed in [
    ("RR below policy threshold is rejected",gate(rr=1.99)=="NO_TRADE"),
    ("news execution block rejects trade",gate(news=True)=="NO_TRADE"),
    ("stale quote rejects trade",gate(stale=True)=="NO_TRADE"),
    ("abnormal spread rejects trade",gate(spread=True)=="NO_TRADE"),
    ("full valid candidate can reach TRADE",gate()=="TRADE"),
    ("risk gate failure overrides prediction",gate(risk_ok=False)=="NO_TRADE"),
    ("expired evidence cannot authorize trade",gate(evidence={"quality":.9,"expired":True})=="NO_TRADE"),
    ("falsified evidence cannot authorize trade",gate(evidence={"quality":.9,"falsified":True})=="NO_TRADE"),
]:
    record("source_invariants",name,passed)

# ---------- Gap-closing engineering implementations ----------
# Point-in-time integrity / no look-ahead
def pit_filter(records, cutoff):
    return [r for r in records if r["knowledge_time"] <= cutoff]
records=[
    {"id":"a","knowledge_time":10},
    {"id":"b","knowledge_time":20},
    {"id":"revision_future","knowledge_time":30},
]
visible=pit_filter(records,20)
record("integrity","point-in-time guard excludes future knowledge",
       [r["id"] for r in visible]==["a","b"],{"visible":[r["id"] for r in visible]})

# Triple barrier / target-race label.
def triple_barrier(path, upper, lower):
    for px in path:
        if px>=upper: return 1
        if px<=lower: return -1
    return 0
record("target_race","upper barrier first => +1",triple_barrier([100,101,103],102,98)==1)
record("target_race","lower barrier first => -1",triple_barrier([100,99,97],102,98)==-1)
record("target_race","expiry first => 0",triple_barrier([100,100.5,100.2],102,98)==0)

# Empirical transition matrix estimator with Dirichlet smoothing.
def transition_matrix(states,k,alpha=1.0):
    C=np.full((k,k),alpha,float)
    for a,b in zip(states[:-1],states[1:]): C[a,b]+=1
    return C/C.sum(axis=1,keepdims=True)
states=rng.integers(0,4,10000)
T=transition_matrix(states,4)
record("regime","transition matrix rows normalize",np.allclose(T.sum(axis=1),1),{"max_error":float(np.abs(T.sum(axis=1)-1).max())})
record("regime","transition probabilities are bounded",float(T.min())>=0 and float(T.max())<=1,{"min":float(T.min()),"max":float(T.max())})

# Calibration metrics.
def brier(y,p): return float(np.mean((np.asarray(p)-np.asarray(y))**2))
def logloss(y,p):
    p=np.clip(np.asarray(p),1e-12,1-1e-12); y=np.asarray(y)
    return float(-np.mean(y*np.log(p)+(1-y)*np.log(1-p)))
def ece(y,p,bins=10):
    y=np.asarray(y); p=np.asarray(p); out=0.0
    edges=np.linspace(0,1,bins+1)
    for i in range(bins):
        mask=(p>=edges[i]) & (p<(edges[i+1] if i<bins-1 else edges[i+1]+1e-15))
        if mask.any(): out += mask.mean()*abs(y[mask].mean()-p[mask].mean())
    return float(out)

y=np.array([0,0,1,1]); perfect=np.array([0,0,1,1],float); neutral=np.full(4,.5)
record("calibration","perfect probabilities have Brier 0",abs(brier(y,perfect))<1e-15)
record("calibration","perfect predictions beat neutral Brier",brier(y,perfect)<brier(y,neutral))
record("calibration","log loss finite under clipping",math.isfinite(logloss(y,perfect)))
record("calibration","ECE bounded in 0..1",0<=ece(y,neutral)<=1,{"ece":ece(y,neutral)})

# Split-conformal regression interval coverage sanity.
def conformal_q(residuals,alpha=.1):
    r=np.sort(np.abs(np.asarray(residuals)))
    n=len(r); rank=min(n-1,max(0,math.ceil((n+1)*(1-alpha))-1))
    return float(r[rank])
cal=rng.normal(0,1,5000); q=conformal_q(cal,.1)
test=rng.normal(0,1,20000)
coverage=float(np.mean(np.abs(test)<=q))
record("uncertainty","split-conformal coverage sanity near nominal",
       coverage>=.88,{"nominal":.90,"observed":coverage,"q":q})

# Drift detector: two-sample standardized mean shift.
def mean_shift_score(a,b):
    a=np.asarray(a); b=np.asarray(b)
    denom=math.sqrt(a.var(ddof=1)/len(a)+b.var(ddof=1)/len(b))+1e-12
    return abs(a.mean()-b.mean())/denom
stable=mean_shift_score(rng.normal(0,1,3000),rng.normal(0,1,3000))
drift=mean_shift_score(rng.normal(0,1,3000),rng.normal(.5,1,3000))
record("drift","drift detector distinguishes large shift",drift>stable and drift>5,
       {"stable_score":stable,"drift_score":drift})

# Walk-forward purging and embargo.
def wf_split(n,train_end,test_start,test_end,embargo):
    train=np.arange(0,max(0,train_end-embargo))
    test=np.arange(test_start,min(test_end,n))
    return train,test
tr,te=wf_split(1000,700,700,850,5)
record("validation","walk-forward train/test do not overlap",len(np.intersect1d(tr,te))==0)
record("validation","embargo enforced",tr.max()<=694 and te.min()==700,{"train_max":int(tr.max()),"test_min":int(te.min())})

# Feature ablation utility.
def ablation_delta(full_score,ablated_score): return float(full_score-ablated_score)
record("ablation","positive marginal feature value detected",ablation_delta(.62,.57)>.0)
record("ablation","harmful feature can be identified",ablation_delta(.57,.62)<.0)

# Forecast skill definition.
def forecast_skill(loss_model,loss_baseline):
    return 1-loss_model/loss_baseline
record("validation","forecast skill >0 iff model beats baseline",forecast_skill(.20,.25)>0)
record("validation","forecast skill <0 when model loses to baseline",forecast_skill(.30,.25)<0)

# Uncertainty entropy.
def normalized_entropy(prob):
    prob=np.asarray(prob,float); prob=prob[prob>0]
    if len(prob)<=1: return 0.0
    return float(-(prob*np.log(prob)).sum()/math.log(len(prob)))
record("uncertainty","normalized entropy bounded",0<=normalized_entropy([.2,.3,.5])<=1)
record("uncertainty","certainty entropy is zero",normalized_entropy([1,0,0])==0)

# Deterministic replay.
payload={"state":[.1,.2,.7],"policy":"NO_TRADE","risk":.004}
def digest(o): return hashlib.sha256(json.dumps(o,sort_keys=True,separators=(",",":")).encode()).hexdigest()
hs=[digest(payload) for _ in range(10000)]
record("replay","deterministic replay hash stable",len(set(hs))==1,{"replays":10000})

# Governance: 100% invariant != 100% prediction; source explicitly marks it a non-objective.
non_objectives=spec["artifact"]["non_objectives"]
warning=spec["deterministic_invariant_test_suite"]["warning"]
record("governance","spec rejects guaranteed market prediction claim",
       "100_percent trading accuracy" in non_objectives)
record("governance","spec distinguishes invariant pass rate from market accuracy",
       "not 100 percent market prediction accuracy" in warning)

passed=sum(t["passed"] for t in tests)
source_tests=[t for t in tests if t["group"]=="source_invariants"]
source_pass=sum(t["passed"] for t in source_tests)
failed=[t for t in tests if not t["passed"]]

report={
    "artifact":spec["artifact"],
    "result_classification":{
        "source_defined_deterministic_invariants":"VERIFIED_BY_EXECUTION",
        "engineering_gap_closures":"VERIFIED_AS_IMPLEMENTATIONS_AND_PROPERTY_TESTS",
        "real_market_predictive_accuracy":"UNKNOWN_GAP"
    },
    "source_invariants":{
        "passed":source_pass,"total":len(source_tests),
        "pass_rate":source_pass/len(source_tests) if source_tests else None
    },
    "expanded_engineering_suite":{
        "passed":passed,"total":len(tests),
        "pass_rate":passed/len(tests) if tests else None,
        "failed":len(failed)
    },
    "tests":tests,
    "remaining_empirical_gap":{
        "status":"OPEN_EXTERNAL_EVIDENCE_GAP",
        "cannot_be_closed_by_unit_tests":True,
        "reason":"No usable point-in-time EUR/USD historical candle/bid-ask dataset was available in the supplied runtime or matching Drive search.",
        "minimum_evidence_to_close":[
            "timestamped historical EUR/USD OHLC or bid/ask",
            "spread/slippage/transaction cost or broker-fill assumptions",
            "point-in-time macro/news vintages for any macro/news features",
            "purged walk-forward out-of-sample results",
            "calibration and regime-segmented performance"
        ],
        "integrity_rule":"Do not convert deterministic pass rate into a market-prediction accuracy claim."
    }
}
REPORT.write_text(json.dumps(report,indent=2,ensure_ascii=False),encoding="utf-8")
print(json.dumps({
    "source_invariants": f"{source_pass}/{len(source_tests)}",
    "source_invariant_pass_rate": source_pass/len(source_tests),
    "expanded_suite": f"{passed}/{len(tests)}",
    "expanded_suite_pass_rate": passed/len(tests),
    "failed_tests":len(failed),
    "real_market_prediction_accuracy":"UNKNOWN — external historical evidence still absent",
    "report":str(REPORT)
},indent=2,ensure_ascii=False))

```

