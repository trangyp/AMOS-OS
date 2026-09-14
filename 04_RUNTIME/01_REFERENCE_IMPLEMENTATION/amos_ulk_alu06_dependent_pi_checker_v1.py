from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, FrozenSet, Mapping

class TypeInvariantError(ValueError):
    pass

class NormalizationLimitError(RuntimeError):
    pass

@dataclass(frozen=True)
class Expr: pass

@dataclass(frozen=True)
class Universe(Expr):
    level: int
    def __post_init__(self):
        if type(self.level) is not int or self.level < 0:
            raise TypeInvariantError('universe level must be a non-negative integer')

@dataclass(frozen=True)
class Var(Expr):
    name: str
    def __post_init__(self):
        if not isinstance(self.name, str) or not self.name.strip():
            raise TypeInvariantError('variable name must be a non-empty string')

@dataclass(frozen=True)
class Pi(Expr):
    var: str
    domain: Expr
    codomain: Expr
    def __post_init__(self):
        if not isinstance(self.var, str) or not self.var.strip():
            raise TypeInvariantError('Pi binder must be a non-empty string')
        if not isinstance(self.domain, Expr) or not isinstance(self.codomain, Expr):
            raise TypeInvariantError('Pi domain/codomain must be expressions')

@dataclass(frozen=True)
class Lam(Expr):
    var: str
    domain: Expr
    body: Expr
    def __post_init__(self):
        if not isinstance(self.var, str) or not self.var.strip():
            raise TypeInvariantError('lambda binder must be a non-empty string')
        if not isinstance(self.domain, Expr) or not isinstance(self.body, Expr):
            raise TypeInvariantError('lambda domain/body must be expressions')

@dataclass(frozen=True)
class App(Expr):
    fn: Expr
    arg: Expr
    def __post_init__(self):
        if not isinstance(self.fn, Expr) or not isinstance(self.arg, Expr):
            raise TypeInvariantError('application function/argument must be expressions')

Context = Mapping[str, Expr]

def free_vars(e: Expr) -> FrozenSet[str]:
    if isinstance(e, Universe): return frozenset()
    if isinstance(e, Var): return frozenset({e.name})
    if isinstance(e, Pi): return free_vars(e.domain) | (free_vars(e.codomain) - {e.var})
    if isinstance(e, Lam): return free_vars(e.domain) | (free_vars(e.body) - {e.var})
    if isinstance(e, App): return free_vars(e.fn) | free_vars(e.arg)
    raise TypeError(type(e))

def _fresh(base: str, forbidden: FrozenSet[str]) -> str:
    if base not in forbidden: return base
    i = 0
    while f'{base}_{i}' in forbidden: i += 1
    return f'{base}_{i}'

def rename_bound(e: Expr, old: str, new: str) -> Expr:
    """Rename occurrences bound by an enclosing binder named ``old``.

    Nested binders reusing ``old`` shadow the enclosing binder, so their bodies
    are not traversed for this rename. Domains are outside their own binder.
    """
    if isinstance(e, Universe): return e
    if isinstance(e, Var): return Var(new if e.name == old else e.name)
    if isinstance(e, App): return App(rename_bound(e.fn, old, new), rename_bound(e.arg, old, new))
    if isinstance(e, Pi):
        d = rename_bound(e.domain, old, new)
        if e.var == old:
            return Pi(e.var, d, e.codomain)
        return Pi(e.var, d, rename_bound(e.codomain, old, new))
    if isinstance(e, Lam):
        d = rename_bound(e.domain, old, new)
        if e.var == old:
            return Lam(e.var, d, e.body)
        return Lam(e.var, d, rename_bound(e.body, old, new))
    raise TypeError(type(e))

def substitute(e: Expr, var: str, replacement: Expr) -> Expr:
    if isinstance(e, Universe): return e
    if isinstance(e, Var): return replacement if e.name == var else e
    if isinstance(e, App): return App(substitute(e.fn,var,replacement), substitute(e.arg,var,replacement))
    if isinstance(e, (Pi, Lam)):
        cls = type(e); binder=e.var; domain=substitute(e.domain,var,replacement); body = e.codomain if isinstance(e,Pi) else e.body
        if binder == var:
            new_body = body
        else:
            if binder in free_vars(replacement):
                forbidden = free_vars(body) | free_vars(replacement) | {var}
                fresh = _fresh(binder, forbidden)
                body = rename_bound(body, binder, fresh)
                binder = fresh
            new_body = substitute(body,var,replacement)
        return Pi(binder,domain,new_body) if cls is Pi else Lam(binder,domain,new_body)
    raise TypeError(type(e))

def alpha_equal(a: Expr, b: Expr, env_a: Dict[str,int]|None=None, env_b: Dict[str,int]|None=None) -> bool:
    env_a=dict(env_a or {}); env_b=dict(env_b or {})
    if type(a) is not type(b): return False
    if isinstance(a, Universe): return a.level == b.level
    if isinstance(a, Var):
        ia=env_a.get(a.name); ib=env_b.get(b.name)
        if ia is not None or ib is not None: return ia == ib and ia is not None
        return a.name == b.name
    if isinstance(a, App): return alpha_equal(a.fn,b.fn,env_a,env_b) and alpha_equal(a.arg,b.arg,env_a,env_b)
    if isinstance(a,(Pi,Lam)):
        ad=a.domain; bd=b.domain
        if not alpha_equal(ad,bd,env_a,env_b): return False
        idx=max([-1,*env_a.values(),*env_b.values()])+1
        ea=dict(env_a); eb=dict(env_b); ea[a.var]=idx; eb[b.var]=idx
        abody=a.codomain if isinstance(a,Pi) else a.body
        bbody=b.codomain if isinstance(b,Pi) else b.body
        return alpha_equal(abody,bbody,ea,eb)
    raise TypeError(type(a))

def normalize(e: Expr, budget: int = 10000) -> Expr:
    if type(budget) is not int or budget <= 0: raise TypeInvariantError('normalization budget must be a positive integer')
    steps=[budget]
    def go(x: Expr) -> Expr:
        if steps[0] <= 0: raise NormalizationLimitError('beta-normalization budget exhausted')
        steps[0]-=1
        if isinstance(x,(Universe,Var)): return x
        if isinstance(x,Pi): return Pi(x.var,go(x.domain),go(x.codomain))
        if isinstance(x,Lam): return Lam(x.var,go(x.domain),go(x.body))
        if isinstance(x,App):
            fn=go(x.fn); arg=go(x.arg)
            if isinstance(fn,Lam): return go(substitute(fn.body,fn.var,arg))
            return App(fn,arg)
        raise TypeError(type(x))
    return go(e)

def definitional_equal(a: Expr,b: Expr,budget: int=10000) -> bool:
    return alpha_equal(normalize(a,budget), normalize(b,budget))

def validate_context(ctx: Context) -> None:
    prefix: Dict[str,Expr]={}
    for name, typ in ctx.items():
        if not isinstance(name,str) or not name.strip(): raise TypeInvariantError('context variable must be non-empty string')
        inferred = infer_type(typ,prefix)
        if not isinstance(normalize(inferred), Universe): raise TypeInvariantError(f'context declaration {name} is not typed by a universe')
        prefix[name]=typ

def infer_type(e: Expr, ctx: Context|None=None) -> Expr:
    ctx=dict(ctx or {})
    if isinstance(e,Universe): return Universe(e.level+1)
    if isinstance(e,Var):
        if e.name not in ctx: raise TypeInvariantError(f'unbound variable: {e.name}')
        return ctx[e.name]
    if isinstance(e,Pi):
        td=normalize(infer_type(e.domain,ctx))
        if not isinstance(td,Universe): raise TypeInvariantError('Pi domain must be a type')
        ext=dict(ctx); ext[e.var]=e.domain
        tc=normalize(infer_type(e.codomain,ext))
        if not isinstance(tc,Universe): raise TypeInvariantError('Pi codomain must be a type')
        return Universe(max(td.level,tc.level))
    if isinstance(e,Lam):
        td=normalize(infer_type(e.domain,ctx))
        if not isinstance(td,Universe): raise TypeInvariantError('lambda domain must be a type')
        ext=dict(ctx); ext[e.var]=e.domain
        body_type=infer_type(e.body,ext)
        return Pi(e.var,e.domain,body_type)
    if isinstance(e,App):
        fn_type=normalize(infer_type(e.fn,ctx))
        if not isinstance(fn_type,Pi): raise TypeInvariantError('application function must have Pi type')
        arg_type=infer_type(e.arg,ctx)
        if not definitional_equal(arg_type,fn_type.domain): raise TypeInvariantError('application argument type mismatch')
        return substitute(fn_type.codomain,fn_type.var,e.arg)
    raise TypeError(type(e))

def validate_alu06_invariants() -> tuple[str,...]:
    failures=[]
    u0=Universe(0)
    ident=Lam('A',u0,Lam('x',Var('A'),Var('x')))
    t=infer_type(ident,{})
    expected=Pi('A',u0,Pi('x',Var('A'),Var('A')))
    if not alpha_equal(t,expected): failures.append('DEPENDENT_IDENTITY_TYPE')
    ctx={'A':u0,'a':Var('A')}
    if not definitional_equal(infer_type(App(App(ident,Var('A')),Var('a')),ctx),Var('A')): failures.append('APPLICATION_SUBSTITUTION')
    capture=substitute(Lam('y',u0,Var('x')),'x',Var('y'))
    if not isinstance(capture,Lam) or capture.var=='y' or free_vars(capture)!=frozenset({'y'}): failures.append('CAPTURE_AVOIDANCE')
    return tuple(failures)
