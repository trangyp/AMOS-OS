"""Bounded ALU-04 modal/epistemic checker using finite Kripke models.

Origin architect / steward: Trang Phan.
AMOS_MODEL executable candidate. Supports finite worlds, finite agents,
propositional atoms, NOT/AND/OR/IMPLIES, BOX(agent), DIAMOND(agent).
It does not claim completeness for first-order, dynamic, probabilistic,
common-knowledge, or infinite-model epistemic logics.
"""
from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from typing import FrozenSet, Mapping, Tuple


class Kind(Enum):
    ATOM="ATOM"; NOT="NOT"; AND="AND"; OR="OR"; IMPLIES="IMPLIES"; BOX="BOX"; DIAMOND="DIAMOND"

@dataclass(frozen=True)
class Formula:
    kind: Kind
    atom: str | None = None
    agent: str | None = None
    args: Tuple["Formula", ...] = ()

    @staticmethod
    def atom_(name: str) -> "Formula":
        if not name.strip(): raise ValueError("atom must be non-empty")
        return Formula(Kind.ATOM, atom=name)
    @staticmethod
    def unary(kind: Kind, x: "Formula", agent: str | None=None) -> "Formula":
        if kind not in (Kind.NOT, Kind.BOX, Kind.DIAMOND): raise ValueError("not unary")
        if kind in (Kind.BOX, Kind.DIAMOND) and (agent is None or not agent.strip()): raise ValueError("modal operator requires agent")
        return Formula(kind, agent=agent, args=(x,))
    @staticmethod
    def binary(kind: Kind, a: "Formula", b: "Formula") -> "Formula":
        if kind not in (Kind.AND, Kind.OR, Kind.IMPLIES): raise ValueError("not binary")
        return Formula(kind, args=(a,b))

@dataclass(frozen=True)
class KripkeModel:
    worlds: FrozenSet[str]
    relations: Mapping[str, FrozenSet[Tuple[str,str]]]
    valuation: Mapping[str, FrozenSet[str]]

    def __post_init__(self) -> None:
        if not self.worlds: raise ValueError("worlds must be non-empty")
        for agent, edges in self.relations.items():
            if not agent.strip(): raise ValueError("agent must be non-empty")
            for u,v in edges:
                if u not in self.worlds or v not in self.worlds: raise ValueError("relation endpoint outside worlds")
        for atom, true_worlds in self.valuation.items():
            if not atom.strip(): raise ValueError("valuation atom must be non-empty")
            if not true_worlds.issubset(self.worlds): raise ValueError("valuation world outside worlds")

    def successors(self, agent: str, world: str) -> FrozenSet[str]:
        if world not in self.worlds: raise KeyError(world)
        return frozenset(v for u,v in self.relations.get(agent, frozenset()) if u == world)


def holds(model: KripkeModel, world: str, formula: Formula) -> bool:
    if world not in model.worlds: raise KeyError(world)
    k=formula.kind
    if k is Kind.ATOM:
        assert formula.atom is not None
        return world in model.valuation.get(formula.atom, frozenset())
    if k is Kind.NOT: return not holds(model, world, formula.args[0])
    if k is Kind.AND: return holds(model, world, formula.args[0]) and holds(model, world, formula.args[1])
    if k is Kind.OR: return holds(model, world, formula.args[0]) or holds(model, world, formula.args[1])
    if k is Kind.IMPLIES: return (not holds(model, world, formula.args[0])) or holds(model, world, formula.args[1])
    assert formula.agent is not None
    succ=model.successors(formula.agent, world)
    if k is Kind.BOX: return all(holds(model, v, formula.args[0]) for v in succ)
    if k is Kind.DIAMOND: return any(holds(model, v, formula.args[0]) for v in succ)
    raise AssertionError(k)


def valid_on_model(model: KripkeModel, formula: Formula) -> bool:
    return all(holds(model,w,formula) for w in model.worlds)
