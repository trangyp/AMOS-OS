"""Research-only AMOS V11 mathematical contracts (Trang Phan stewardship)."""
import math

def bh_qvalues(p):
    if not p or any(not isinstance(x,(int,float)) or not math.isfinite(x) or x<0 or x>1 for x in p):
        raise ValueError("invalid p")
    m=len(p);order=sorted(range(m),key=lambda i:p[i]);q=[0.0]*m;running=1.0
    for k in range(m-1,-1,-1):
        idx=order[k];running=min(running,m*p[idx]/(k+1),1.0);q[idx]=running
    return q

def interval_to_half_open(start,end,convention):
    if type(start) is not int or type(end) is not int or end<start:raise ValueError("coordinates")
    if convention=="one_closed":
        if start<1:raise ValueError("1-based start")
        return start-1,end
    if convention=="zero_half_open":
        if start<0:raise ValueError("0-based start")
        return start,end
    raise ValueError("coordinate convention")

def gate(gates,host,authority):
    if len(gates)!=7 or any(type(v) is not bool for v in gates):raise ValueError("typed gates")
    return host is True and authority is True and all(gates)
