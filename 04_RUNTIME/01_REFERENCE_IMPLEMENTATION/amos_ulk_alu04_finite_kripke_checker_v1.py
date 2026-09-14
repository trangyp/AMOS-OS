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

    def __post_init__(self) -> None:
        if not isinstance(self.kind, Kind):
            raise ValueError("formula kind must be a Kind")
        if self.kind is Kind.ATOM:
            if not isinstance(self.atom, str) or not self.atom.strip() or self.agent is not None or self.args:
                raise ValueError("ATOM requires one non-empty atom and no agent/args")
            return
        if self.atom is not None:
            raise ValueError("non-ATOM formula cannot carry atom payload")
        if self.kind is Kind.NOT:
            if self.agent is not None or len(self.args) != 1:
                raise ValueError("NOT requires exactly one argument and no agent")
            return
        if self.kind in (Kind.BOX, Kind.DIAMOND):
            if not isinstance(self.agent, str) or not self.agent.strip() or len(self.args) != 1:
                raise ValueError("modal operator requires one argument and a non-empty agent")
            return
        if self.kind in (Kind.AND, Kind.OR, Kind.IMPLIES):
            if self.agent is not None or len(self.args) != 2:
                raise ValueError("binary Boolean operator requires exactly two arguments and no agent")
            return
        raise ValueError(f"unsupported formula kind: {self.kind}")

    @staticmethod
    def atom_(name: str) -> "Formula":
        return Formula(Kind.ATOM, atom=name)

    @staticmethod
    def unary(kind: Kind, x: "Formula", agent: str | None=None) -> "Formula":
        if not isinstance(x, Formula): raise ValueError("unary operand must be Formula")
        return Formula(kind, agent=agent, args=(x,))

    @staticmethod
    def binary(kind: Kind, a: "Formula", b: "Formula") -> "Formula":
        if not isinstance(a, Formula) or not isinstance(b, Formula): raise ValueError("binary operands must be Formula")
        return Formula(kind, args=(a,b))

@dataclass(frozen=True)
class KripkeModel:
    worlds: FrozenSet[str]
    relations: Mapping[str, FrozenSet[Tuple[str,str]]]
    valuation: Mapping[str, FrozenSet[str]]

    def __post_init__(self) -> None:
        if not self.worlds: raise ValueError("worlds must be non-empty")
        if any(not isinstance(w, str) or not w.strip() for w in self.worlds): raise ValueError("worlds must be non-empty strings")
        for agent, edges in self.relations.items():
            if not isinstance(agent, str) or not agent.strip(): raise ValueError("agent must be non-empty")
            for u,v in edges:
                if u not in self.worlds or v not in self.worlds: raise ValueError("relation endpoint outside worlds")
        for atom, true_worlds in self.valuation.items():
            if not isinstance(atom, str) or not atom.strip(): raise ValueError("valuation atom must be non-empty")
            if not true_worlds.issubset(self.worlds): raise ValueError("valuation world outside worlds")

    def successors(self, agent: str, world: str) -> FrozenSet[str]:
        if world not in self.worlds: raise KeyError(world)
        if agent not in self.relations: raise KeyError(agent)
        return frozenset(v for u,v in self.relations[agent] if u == world)


def holds(model: KripkeModel, world: str, formula: Formula) -> bool:
    if world not in model.worlds: raise KeyError(world)
    if not isinstance(formula, Formula): raise ValueError("formula must be Formula")
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
