from dataclasses import dataclass
from enum import Enum
from typing import Optional, Sequence, Tuple
from classical_sat_firewall import BoolFormula, conjunction, globally_consistent, is_satisfiable
from core19_runtime import ImplementationStatus, LogicFragment, P02BindingRegistry, implementation_status


class InferenceStatus(Enum):
    VERIFIED_BOUNDED='VERIFIED_BOUNDED'
    NOT_ENTAILED='NOT_ENTAILED'
    INCONSISTENT_INPUT='INCONSISTENT_INPUT'
    COMPETING='COMPETING'
    UNKNOWN_GAP='UNKNOWN/GAP'


@dataclass(frozen=True)
class Premise:
    claim_id:str
    formula:BoolFormula
    provenance:str
    confidence:Optional[float]=None

    def __post_init__(self):
        if not self.claim_id.strip(): raise ValueError('premise claim_id must be non-empty')
        if not self.provenance.strip(): raise ValueError('premise provenance must be non-empty')
        if self.confidence is not None and not (0.0<=self.confidence<=1.0): raise ValueError('premise confidence must be within [0, 1]')


@dataclass(frozen=True)
class InferenceRequest:
    fragment:LogicFragment
    premises:Tuple[Premise,...]
    conclusion:Optional[BoolFormula]=None
    scope:str='bounded_core19_classical'
    regime:str='reference_runtime'
    source_version:str='2026-09-14'
    uses_p02:bool=False
    p02_namespace:Optional[str]=None
    p02_version:Optional[str]=None
    causal_claim:bool=False
    causal_evidence_bound:bool=False

    def __post_init__(self):
        if not self.scope.strip() or not self.regime.strip() or not self.source_version.strip(): raise ValueError('scope, regime, and source_version must be explicit')


@dataclass(frozen=True)
class InferenceResult:
    status:InferenceStatus
    reason:str
    fragment_status:ImplementationStatus
    dependency_claim_ids:Tuple[str,...]
    provenance:Tuple[str,...]
    scope:str
    regime:str
    source_version:str
    confidence_ceiling:Optional[float]
    globally_consistent:Optional[bool]
    entailed:Optional[bool]


def _confidence_ceiling(premises:Sequence[Premise]):
    values=[p.confidence for p in premises if p.confidence is not None]
    if len(values)!=len(premises) or not values: return None
    return min(values)


def _result(r,*,status,reason,fragment_status,globally_consistent_state=None,entailed=None):
    return InferenceResult(status,reason,fragment_status,tuple(p.claim_id for p in r.premises),tuple(p.provenance for p in r.premises),r.scope,r.regime,r.source_version,_confidence_ceiling(r.premises),globally_consistent_state,entailed)


def evaluate_inference(request,*,p02_registry=None,max_atoms=20):
    fragment_state=implementation_status(request.fragment)
    if fragment_state is not ImplementationStatus.EXECUTABLE_BOUNDED:
        if fragment_state is ImplementationStatus.CANONICAL_BOUNDED_CLAIM_REBIND_PENDING:
            reason='fragment has a canonical bounded claim but executable evidence is rebind-pending'
        elif fragment_state is ImplementationStatus.EXECUTABLE_BOUNDED_CANDIDATE_REBOUND:
            reason='fragment has bounded execution evidence in its specialist checker, but this L09 API accepts only the classical propositional BoolFormula ABI'
        else:
            reason='fragment is specification-only in this L09 repair surface'
        return _result(request,status=InferenceStatus.UNKNOWN_GAP,reason=reason,fragment_status=fragment_state)
    if request.uses_p02:
        if p02_registry is None or request.p02_namespace is None or request.p02_version is None:
            return _result(request,status=InferenceStatus.COMPETING,reason='P02 is cross-lineage COMPETING and requires explicit namespace/version binding',fragment_status=fragment_state)
        if not p02_registry.resolve(request.p02_namespace,request.p02_version).resolved:
            return _result(request,status=InferenceStatus.COMPETING,reason='P02 namespace/version is unresolved; no cross-lineage winner may be fabricated',fragment_status=fragment_state)
    if request.causal_claim and not request.causal_evidence_bound:
        return _result(request,status=InferenceStatus.UNKNOWN_GAP,reason='logical implication/association does not establish causation without a bound causal model/evidence contract',fragment_status=fragment_state)
    premise_formulas=tuple(p.formula for p in request.premises)
    try: consistent=globally_consistent(premise_formulas,max_atoms=max_atoms)
    except ValueError as exc: return _result(request,status=InferenceStatus.UNKNOWN_GAP,reason=str(exc),fragment_status=fragment_state)
    if not consistent: return _result(request,status=InferenceStatus.INCONSISTENT_INPUT,reason='premise set is globally inconsistent; contradiction remains inspectable and no explosion-based conclusion is promoted',fragment_status=fragment_state,globally_consistent_state=False)
    if request.conclusion is None: return _result(request,status=InferenceStatus.VERIFIED_BOUNDED,reason='premise set is globally consistent within the bounded classical fragment',fragment_status=fragment_state,globally_consistent_state=True)
    try:
        countermodel_query=BoolFormula.and_(conjunction(premise_formulas),BoolFormula.not_(request.conclusion))
        entailed=not is_satisfiable(countermodel_query,max_atoms=max_atoms)
    except ValueError as exc: return _result(request,status=InferenceStatus.UNKNOWN_GAP,reason=str(exc),fragment_status=fragment_state,globally_consistent_state=True)
    if entailed: return _result(request,status=InferenceStatus.VERIFIED_BOUNDED,reason='conclusion follows by bounded classical entailment: premises AND NOT(conclusion) is unsatisfiable',fragment_status=fragment_state,globally_consistent_state=True,entailed=True)
    return _result(request,status=InferenceStatus.NOT_ENTAILED,reason='a satisfying countermodel exists; conclusion is not entailed by the declared premises',fragment_status=fragment_state,globally_consistent_state=True,entailed=False)
