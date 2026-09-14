"""Bounded ALU-05 Dung abstract argumentation checker.

Origin architect / steward: Trang Phan.
AMOS_MODEL executable candidate over finite argument sets. Implements conflict
freedom, defence/acceptability, the characteristic function, grounded extension,
admissibility, and bounded preferred-extension enumeration.
"""
from __future__ import annotations
from dataclasses import dataclass
from itertools import combinations
from typing import FrozenSet, Tuple

@dataclass(frozen=True)
class ArgumentationFramework:
    arguments: FrozenSet[str]
    attacks: FrozenSet[Tuple[str,str]]
    def __post_init__(self) -> None:
        if any(not a.strip() for a in self.arguments): raise ValueError("arguments must be non-empty strings")
        for a,b in self.attacks:
            if a not in self.arguments or b not in self.arguments: raise ValueError("attack endpoint outside argument set")
    def attackers(self, a: str) -> FrozenSet[str]:
        if a not in self.arguments: raise KeyError(a)
        return frozenset(x for x,y in self.attacks if y==a)
    def attacked_by(self, S: FrozenSet[str]) -> FrozenSet[str]:
        return frozenset(y for x,y in self.attacks if x in S)

def conflict_free(af: ArgumentationFramework, S: FrozenSet[str]) -> bool:
    if not S.issubset(af.arguments): raise ValueError("set contains unknown argument")
    return not any(a in S and b in S for a,b in af.attacks)

def defends(af: ArgumentationFramework, S: FrozenSet[str], a: str) -> bool:
    attacked=af.attacked_by(S)
    return all(attacker in attacked for attacker in af.attackers(a))

def characteristic(af: ArgumentationFramework, S: FrozenSet[str]) -> FrozenSet[str]:
    if not S.issubset(af.arguments): raise ValueError("set contains unknown argument")
    return frozenset(a for a in af.arguments if defends(af,S,a))

def grounded_extension(af: ArgumentationFramework) -> FrozenSet[str]:
    S=frozenset()
    for _ in range(len(af.arguments)+1):
        nxt=characteristic(af,S)
        if nxt==S: return S
        S=nxt
    raise AssertionError("finite characteristic iteration failed to stabilize")

def admissible(af: ArgumentationFramework, S: FrozenSet[str]) -> bool:
    return conflict_free(af,S) and S.issubset(characteristic(af,S))

def preferred_extensions(af: ArgumentationFramework, max_arguments: int=18) -> Tuple[FrozenSet[str], ...]:
    n=len(af.arguments)
    if n>max_arguments: raise ValueError("preferred enumeration is exponential; explicit bound exceeded")
    args=sorted(af.arguments)
    admiss=[]
    for r in range(n+1):
        for combo in combinations(args,r):
            S=frozenset(combo)
            if admissible(af,S): admiss.append(S)
    maximal=[S for S in admiss if not any(S<T for T in admiss)]
    return tuple(sorted(maximal,key=lambda s:(len(s),tuple(sorted(s)))))
