"""AMOS scientific assurance contracts. Candidate only, no device execution."""
from math import ceil, isfinite
from itertools import product

def verify_tensor(shape, axes, unit, provenance):
    if len(shape)!=len(axes) or len(set(axes))!=len(axes) or not all(type(n)==int and n>0 for n in shape):
        raise ValueError("tensor dimensions")
    if unit not in ("V","V^2","count","probability","feature","boolean") or not provenance:
        raise ValueError("unit/provenance")
    return {"axes":tuple(axes),"shape":tuple(shape),"unit":unit}

def constrained_skill_selection(candidates, installed, gates, weights, costs, budget, dependencies=(), conflicts=()):
    """Exact union-coverage finite selection; never grants install authority."""
    n=len(candidates);m=len(weights)
    if n>18 or n==0 or m==0 or len(gates)!=n or len(costs)!=n or any(len(x)!=m for x in candidates+installed):
        raise ValueError("dimensions")
    if any(type(z)!=bool for g in gates for z in g) or any(len(g)!=7 for g in gates):
        raise ValueError("seven witnessed boolean gates")
    if any(type(z)!=int or z not in (0,1) for row in candidates+installed for z in row):
        raise ValueError("binary incidence")
    if any(not isfinite(x) or x<0 for x in weights+costs+[budget]) or abs(sum(weights)-1)>1e-9:
        raise ValueError("dimensionless weights / single-unit cost budget")
    for a,b in list(dependencies)+list(conflicts):
        if min(a,b)<0 or max(a,b)>=n:raise ValueError("dependency/conflict bounds")
    existing=[any(row[j] for row in installed) for j in range(m)]
    feasible=[]
    for x in product((0,1),repeat=n):
        if any(x[i] and not all(gates[i]) for i in range(n)): continue
        c=sum(costs[i]*x[i] for i in range(n))
        if c>budget:continue
        if any(x[i] and not x[j] for i,j in dependencies):continue
        if any(x[i] and x[j] for i,j in conflicts):continue
        gain=sum(weights[j] for j in range(m) if not existing[j] and any(x[i]*candidates[i][j] for i in range(n)))
        feasible.append((gain,c,tuple(i for i,b in enumerate(x) if b)))
    if not feasible:raise ValueError("no admissible portfolio")
    best=sorted(feasible,key=lambda z:(-round(z[0],12),z[1],z[2]))[0]
    return {"selected":best[2],"coverage":best[0],"status":"REVIEW_ONLY"}

def pseudobulk(raw,groups):
    """Integer exact donor/condition reduction, conservation checked."""
    if len(raw)!=len(groups) or not raw or not raw[0]:raise ValueError("axes")
    width=len(raw[0])
    if any(len(row)!=width or any(type(v)!=int or v<0 for v in row) for row in raw):raise ValueError("raw count domain")
    keys=list(dict.fromkeys(groups))
    y=[[sum(raw[i][j] for i in range(len(raw)) if groups[i]==key) for j in range(width)] for key in keys]
    if any(sum(y[k][j] for k in range(len(keys)))!=sum(row[j] for row in raw) for j in range(width)):
        raise ArithmeticError("count conservation")
    return keys,y

def conformal_rank(scores,alpha):
    if not scores or not 0<alpha<1 or any(not isfinite(s) for s in scores):raise ValueError("exchangeable-score candidate")
    k=ceil((len(scores)+1)*(1-alpha))
    return float("inf") if k>len(scores) else sorted(scores)[k-1]

def leave_group_out(groups,train,test):
    if not train or not test or min(train+test)<0 or max(train+test)>=len(groups):raise ValueError("split bounds")
    if set(train)&set(test) or {groups[i] for i in train}&{groups[j] for j in test}:raise ValueError("leakage")
    return True
