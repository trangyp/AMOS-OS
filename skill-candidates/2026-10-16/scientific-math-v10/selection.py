"""Review-only mathematical candidate selector. No install side effects."""
from itertools import product
import math

GATES=("sha_pinned","license_verified","provenance_verified","tests_pass","security_review","rollback_ready","authority_current")
def exact_portfolio(C,B,G,H,w,cost,budget,requires=(),conflicts=()):
    n=len(C); m=len(w)
    if n<1 or n>20 or m<1 or len(G)!=n or len(H)!=n or len(cost)!=n:raise ValueError("shape")
    if any(len(r)!=m or any(type(v)!=int or v not in (0,1) for v in r) for r in C+B):raise ValueError("incidence")
    if any(len(g)!=7 or any(type(v)!=bool for v in g) for g in G):raise ValueError("gates")
    if any(type(h)!=bool for h in H):raise ValueError("host")
    if any(not isinstance(v,(float,int)) or not math.isfinite(v) or v<0 for v in [*w,*cost,budget]):raise ValueError("units/domain")
    if not math.isclose(sum(w),1,abs_tol=1e-9):raise ValueError("weight sum")
    prior=[any(b[j] for b in B) for j in range(m)]
    feasible=[]
    for bits in product((0,1),repeat=n):
        if any(bits[i] and (not H[i] or not all(G[i])) for i in range(n)):continue
        if sum(cost[i]*bits[i] for i in range(n))>budget+1e-12:continue
        if any(bits[i] and not bits[d] for i,d in requires):continue
        if any(bits[a] and bits[b] for a,b in conflicts):continue
        benefit=sum(w[j] for j in range(m) if not prior[j] and any(bits[i] and C[i][j] for i in range(n)))
        cost_used=sum(cost[i]*bits[i] for i in range(n))
        feasible.append((benefit,cost_used,tuple(i for i,b in enumerate(bits) if b)))
    if not feasible:raise ValueError("infeasible")
    v,c,sel=sorted(feasible,key=lambda x:(-round(x[0],12),x[1],x[2]))[0]
    return {"selected":list(sel),"coverage_gain":v,"cost":c,"status":"REVIEW_ONLY"}
