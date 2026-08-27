from __future__ import annotations

from dataclasses import dataclass, field, asdict
from enum import Enum
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional
import hashlib
import json
import logging
import time


# ============================================================
# AMOS ABSOLUTE PRIMITIVE DECOMPOSER AGENT
# ============================================================

AGENT_ID = "amos-absolute-primitive-decomposer-agent"
AGENT_VERSION = "1.0.0"


# ============================================================
# ENUMS
# ============================================================

class EpistemicClass(str, Enum):
    SOURCE = "SOURCE"
    DERIVED = "DERIVED"
    AMOS_MODEL = "AMOS_MODEL"
    EMPIRICAL = "EMPIRICAL"
    UNKNOWN = "UNKNOWN/GAP"


class ExecutionStatus(str, Enum):
    VERIFIED = "VERIFIED"
    CONDITIONAL = "CONDITIONAL"
    UNKNOWN = "UNKNOWN/GAP"
    REJECTED = "REJECTED"


class SideEffect(str, Enum):
    READ = "read"
    WRITE = "write"


# ============================================================
# ERRORS
# ============================================================

class PrimitiveAgentError(RuntimeError):
    pass


class ValidationError(PrimitiveAgentError):
    pass


class AuthorizationError(PrimitiveAgentError):
    pass


class GapError(PrimitiveAgentError):
    pass


# ============================================================
# DATA CONTRACTS
# ============================================================

@dataclass(frozen=True)
class ProvenanceRef:
    source: str
    path: Optional[str] = None
    content_hash: Optional[str] = None


@dataclass
class Claim:
    text: str
    epistemic_class: EpistemicClass
    confidence: float
    provenance: List[ProvenanceRef] = field(default_factory=list)
    scope: Optional[str] = None
    falsifiers: List[str] = field(default_factory=list)


@dataclass
class CapabilityContract:
    name: str
    description: str
    side_effect: SideEffect


@dataclass
class PrimitiveMapping:
    primitive: str
    evidence: List[str] = field(default_factory=list)
    interpretation: Optional[str] = None
    confidence: float = 0.0
    epistemic_class: EpistemicClass = EpistemicClass.AMOS_MODEL


@dataclass
class ExecutionContext:
    query: str
    capability: str

    inputs: Dict[str, Any] = field(default_factory=dict)

    authorized_write: bool = False
    authority_witness: Optional[str] = None
    correlation_id: Optional[str] = None


@dataclass
class AgentResult:
    status: ExecutionStatus
    capability: str
    summary: str

    data: Dict[str, Any] = field(default_factory=dict)
    claims: List[Claim] = field(default_factory=list)

    gaps: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

    confidence_ceiling: float = 0.95
    provenance: List[ProvenanceRef] = field(default_factory=list)


# ============================================================
# AGENT CONFIG
# ============================================================

AGENT_CONFIG: Dict[str, Any] = {
    "name": AGENT_ID,
    "display_name": "Absolute Primitive Decomposer",
    "description": (
        "Absolute Primitive Decomposer — Runtime and OS engine. "
        "Bound to runtime domain. Use when primitive-level AMOS "
        "decomposition is required."
    ),
    "version": "1.0.0",
    "author": "Trang Phan",
    "steward": "Trang Phan",
    "system": "AMOS_OS",
    "role": (
        "Primitive-level AMOS decomposition specialist for mapping "
        "supported structures while preserving non-mappable residue."
    ),
    "primary_skill": "amos-absolute-primitive-decomposer",
    "skill_path": (
        ".devin/skills/"
        "amos-absolute-primitive-decomposer/"
        "SKILL.md"
    ),
    "workflow": (
        "amos-absolute-primitive-decomposer-workflow.md"
    ),
    "epistemic_class": "AMOS_MODEL",
    "claim_ceiling": 0.95,
    "owner_team": "AMOS_CORE",
    "business_domain": "runtime",
    "risk_tier": "medium",
    "approval_mode": "steward_review",
    "promotion_state": "production",
    "content_hash": "a98c7cd908ed416d",
}


CAPABILITIES: Dict[str, CapabilityContract] = {
    "runtime.execute": CapabilityContract(
        name="runtime.execute",
        description=(
            "Decompose an input into supported AMOS absolute primitives "
            "while preserving non-mappable residue."
        ),
        side_effect=SideEffect.WRITE,
    ),
    "runtime.validate": CapabilityContract(
        name="runtime.validate",
        description=(
            "Validate primitive mappings for support, overreach, "
            "residue preservation, and epistemic labeling."
        ),
        side_effect=SideEffect.READ,
    ),
    "runtime.trace_provenance": CapabilityContract(
        name="runtime.trace_provenance",
        description=(
            "Trace primitive mappings back to source evidence or "
            "explicit AMOS_MODEL interpretation."
        ),
        side_effect=SideEffect.READ,
    ),
    "runtime.assess_claim": CapabilityContract(
        name="runtime.assess_claim",
        description=(
            "Assess primitive-level claims for evidence strength, "
            "scope, and epistemic class."
        ),
        side_effect=SideEffect.READ,
    ),
}


# ============================================================
# MAIN AGENT
# ============================================================

class AmosAbsolutePrimitiveDecomposerAgent:
    """
    Runtime adapter for amos-absolute-primitive-decomposer.

    Governing boundary:
    - Treat the 19-primitives system as a user-defined framework model.
    - Map only supported structures.
    - Preserve unresolved / non-mappable residue.
    - Never force every input into all primitives.
    """

    def __init__(
        self,
        repo_root: str | Path = ".",
        claim_ceiling: float = 0.95,
    ) -> None:

        self.repo_root = Path(repo_root).resolve()

        self.skill_path = (
            self.repo_root
            / ".devin"
            / "skills"
            / "amos-absolute-primitive-decomposer"
            / "SKILL.md"
        )

        self.claim_ceiling = min(
            max(float(claim_ceiling), 0.0),
            0.95,
        )

        self.logger = logging.getLogger(AGENT_ID)

        self.handlers: Dict[
            str,
            Callable[[ExecutionContext], AgentResult],
        ] = {
            "runtime.execute": self._execute_decomposition,
            "runtime.validate": self._validate_decomposition,
            "runtime.trace_provenance": self._trace_provenance,
            "runtime.assess_claim": self._assess_claim,
        }

    # ========================================================
    # PUBLIC ENTRYPOINT
    # ========================================================

    def run(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        ctx.correlation_id = (
            ctx.correlation_id
            or self._new_correlation_id()
        )

        self._load_skill()
        self._validate_context(ctx)

        capability = CAPABILITIES.get(ctx.capability)

        if capability is None:
            raise ValidationError(
                f"Unsupported capability: {ctx.capability}"
            )

        self._check_authority(
            capability=capability,
            ctx=ctx,
        )

        result = self.handlers[ctx.capability](ctx)

        self._validate_result(result)

        return result

    # ========================================================
    # SKILL / AUTHORITY GATES
    # ========================================================

    def _load_skill(self) -> str:

        if not self.skill_path.exists():
            raise GapError(
                "UNKNOWN/GAP: authoritative skill unavailable: "
                f"{self.skill_path}"
            )

        text = self.skill_path.read_text(encoding="utf-8")

        if not text.strip():
            raise GapError(
                "UNKNOWN/GAP: authoritative skill is empty."
            )

        return text

    def _validate_context(
        self,
        ctx: ExecutionContext,
    ) -> None:

        if not ctx.query.strip():
            raise ValidationError(
                "query must not be empty"
            )

    def _check_authority(
        self,
        capability: CapabilityContract,
        ctx: ExecutionContext,
    ) -> None:

        if capability.side_effect != SideEffect.WRITE:
            return

        if not ctx.authorized_write:
            raise AuthorizationError(
                f"{capability.name} is write-classified. "
                "Capability does not imply authority."
            )

        if not ctx.authority_witness:
            raise AuthorizationError(
                "Write-classified operation requires "
                "an authority_witness."
            )

    # ========================================================
    # EXECUTION
    # ========================================================

    def _execute_decomposition(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:
        """
        Skill workflow:

        1. Strip non-load-bearing narrative without losing material context.
        2. Identify entities, relations, time, information,
           topology, identity, contradiction.
        3. Map only supported structures to primitives.
        4. Preserve unresolved/non-mappable residue.
        5. Do not force all 19 primitives.
        6. Return map, residue, confidence.
        """

        raw_input = ctx.inputs.get("input")

        if raw_input is None:
            raise GapError(
                "UNKNOWN/GAP: 'input' is required."
            )

        normalized = self._strip_non_load_bearing_narrative(
            raw_input
        )

        structural_features = self._identify_structural_features(
            normalized
        )

        primitive_map, residue = self._map_supported_primitives(
            structural_features=structural_features,
            explicit_mappings=ctx.inputs.get(
                "primitive_mappings",
                {}
            ),
        )

        confidence = self._aggregate_confidence(
            primitive_map
        )

        return AgentResult(
            status=(
                ExecutionStatus.CONDITIONAL
                if residue
                else ExecutionStatus.VERIFIED
            ),
            capability=ctx.capability,
            summary=(
                "Primitive decomposition completed with "
                f"{len(primitive_map)} supported mappings."
            ),
            data={
                "normalized_input": normalized,
                "structural_features": structural_features,
                "primitive_map": [
                    asdict(item)
                    for item in primitive_map
                ],
                "omitted_residue": residue,
                "mapped_primitive_count": len(
                    primitive_map
                ),
                "forced_full_coverage": False,
                "aggregate_confidence": confidence,
            },
            claims=[
                Claim(
                    text=(
                        "The primitive map is an AMOS framework-model "
                        "decomposition of supported structures only."
                    ),
                    epistemic_class=EpistemicClass.AMOS_MODEL,
                    confidence=min(
                        confidence,
                        self.claim_ceiling,
                    ),
                    provenance=self._default_provenance(),
                    scope=str(
                        ctx.inputs.get(
                            "scope",
                            "supplied input",
                        )
                    ),
                    falsifiers=[
                        (
                            "A mapped primitive lacks support "
                            "in the supplied structure."
                        ),
                        (
                            "A mapping depends on narrative content "
                            "that was incorrectly discarded."
                        ),
                    ],
                )
            ],
            gaps=residue,
            warnings=[
                (
                    "The 19-primitives framework is treated as "
                    "AMOS_MODEL, not universal ontology."
                ),
                (
                    "Unmapped residue is intentionally preserved "
                    "rather than force-fit."
                ),
            ],
            confidence_ceiling=self.claim_ceiling,
            provenance=self._default_provenance(),
        )

    # ========================================================
    # NORMALIZATION
    # ========================================================

    def _strip_non_load_bearing_narrative(
        self,
        raw_input: Any,
    ) -> Dict[str, Any]:
        """
        Conservative normalization.

        This does not delete original context.
        It creates a separate normalized view.
        """

        if isinstance(raw_input, dict):
            return {
                "original": raw_input,
                "normalized": raw_input,
                "normalization_status": (
                    "STRUCTURE_PRESERVED"
                ),
            }

        if isinstance(raw_input, list):
            return {
                "original": raw_input,
                "normalized": raw_input,
                "normalization_status": (
                    "LIST_STRUCTURE_PRESERVED"
                ),
            }

        text = str(raw_input).strip()

        return {
            "original": text,
            "normalized": text,
            "normalization_status": (
                "NO_UNSUPPORTED_CONTENT_REMOVED"
            ),
        }

    # ========================================================
    # STRUCTURAL FEATURE EXTRACTION
    # ========================================================

    def _identify_structural_features(
        self,
        normalized: Dict[str, Any],
    ) -> Dict[str, Any]:

        value = normalized["normalized"]

        features: Dict[str, Any] = {
            "entities": [],
            "relations": [],
            "time": [],
            "information": [],
            "topology": [],
            "identity": [],
            "contradictions": [],
        }

        if isinstance(value, dict):

            features["entities"] = list(
                value.get("entities", [])
            )

            features["relations"] = list(
                value.get("relations", [])
            )

            features["time"] = list(
                value.get("time", [])
            )

            features["information"] = list(
                value.get("information", [])
            )

            features["topology"] = list(
                value.get("topology", [])
            )

            features["identity"] = list(
                value.get("identity", [])
            )

            features["contradictions"] = list(
                value.get(
                    "contradictions",
                    value.get("contradiction", []),
                )
            )

            # Preserve unrecognized source fields for residue analysis.
            known = {
                "entities",
                "relations",
                "time",
                "information",
                "topology",
                "identity",
                "contradictions",
                "contradiction",
            }

            features["unclassified_fields"] = {
                key: val
                for key, val in value.items()
                if key not in known
            }

        else:
            # No hidden NLP inference masquerading as fact.
            # The raw text is retained as unresolved structure unless
            # explicit mappings are supplied.
            features["raw_text"] = str(value)
            features["unclassified_fields"] = {
                "raw_text": str(value)
            }

        return features

    # ========================================================
    # PRIMITIVE MAPPING
    # ========================================================

    def _map_supported_primitives(
        self,
        structural_features: Dict[str, Any],
        explicit_mappings: Any,
    ) -> tuple[List[PrimitiveMapping], List[str]]:

        mappings: List[PrimitiveMapping] = []
        residue: List[str] = []

        if not isinstance(explicit_mappings, dict):
            explicit_mappings = {}

        # The skill entrypoint does not expose the full primitive registry,
        # so this runtime must not invent all 19 primitive names.
        #
        # It can safely preserve the structural categories explicitly named
        # by the skill and accept additional primitive names only when they
        # are explicitly supplied by authoritative input/reference data.

        feature_to_primitive = {
            "entities": "entity/existence",
            "relations": "relation",
            "time": "temporal",
            "information": "information",
            "topology": "topology",
            "identity": "identity",
            "contradictions": "contradiction",
        }

        for feature_name, primitive_name in (
            feature_to_primitive.items()
        ):

            evidence = structural_features.get(
                feature_name,
                [],
            )

            if evidence:
                mappings.append(
                    PrimitiveMapping(
                        primitive=primitive_name,
                        evidence=[
                            str(item)
                            for item in evidence
                        ],
                        interpretation=(
                            f"Supported by explicit "
                            f"{feature_name} structure."
                        ),
                        confidence=0.90,
                        epistemic_class=(
                            EpistemicClass.AMOS_MODEL
                        ),
                    )
                )

        # Authoritatively supplied extra primitive mappings.
        for primitive_name, raw in (
            explicit_mappings.items()
        ):

            if not isinstance(raw, dict):
                residue.append(
                    f"{primitive_name}: invalid mapping format"
                )
                continue

            evidence = list(
                raw.get("evidence", [])
            )

            if not evidence:
                residue.append(
                    f"{primitive_name}: no evidence supplied"
                )
                continue

            confidence = min(
                max(
                    float(
                        raw.get(
                            "confidence",
                            0.80,
                        )
                    ),
                    0.0,
                ),
                self.claim_ceiling,
            )

            mappings.append(
                PrimitiveMapping(
                    primitive=str(
                        primitive_name
                    ),
                    evidence=[
                        str(item)
                        for item in evidence
                    ],
                    interpretation=raw.get(
                        "interpretation"
                    ),
                    confidence=confidence,
                    epistemic_class=(
                        EpistemicClass.AMOS_MODEL
                    ),
                )
            )

        unclassified = structural_features.get(
            "unclassified_fields",
            {}
        )

        if unclassified:
            residue.append(
                "Unclassified material remains: "
                + ", ".join(
                    sorted(
                        str(key)
                        for key in unclassified.keys()
                    )
                )
            )

        return mappings, residue

    # ========================================================
    # VALIDATION
    # ========================================================

    def _validate_decomposition(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        output = ctx.inputs.get("output")

        if not isinstance(output, dict):
            raise GapError(
                "UNKNOWN/GAP: 'output' dictionary required."
            )

        issues: List[str] = []

        primitive_map = output.get(
            "primitive_map",
            []
        )

        residue = output.get(
            "omitted_residue"
        )

        if not isinstance(
            primitive_map,
            list,
        ):
            issues.append(
                "primitive_map_must_be_list"
            )

        if residue is None:
            issues.append(
                "missing_residue_field"
            )

        if output.get(
            "forced_full_coverage"
        ) is True:
            issues.append(
                "forced_full_19_primitive_mapping"
            )

        for index, item in enumerate(
            primitive_map
            if isinstance(
                primitive_map,
                list,
            )
            else []
        ):
            if not isinstance(item, dict):
                issues.append(
                    f"mapping[{index}]_invalid"
                )
                continue

            if not item.get("primitive"):
                issues.append(
                    f"mapping[{index}]_missing_primitive"
                )

            if not item.get("evidence"):
                issues.append(
                    f"mapping[{index}]_missing_evidence"
                )

            if (
                item.get("epistemic_class")
                not in {
                    "AMOS_MODEL",
                    "SOURCE",
                    "DERIVED",
                    "EMPIRICAL",
                    "UNKNOWN/GAP",
                }
            ):
                issues.append(
                    f"mapping[{index}]_invalid_epistemic_class"
                )

        return AgentResult(
            status=(
                ExecutionStatus.VERIFIED
                if not issues
                else ExecutionStatus.CONDITIONAL
            ),
            capability=ctx.capability,
            summary=(
                "Primitive decomposition validation completed."
            ),
            data={
                "pass": not issues,
                "issues": issues,
            },
            gaps=issues,
            confidence_ceiling=self.claim_ceiling,
            provenance=self._default_provenance(),
        )

    # ========================================================
    # PROVENANCE TRACE
    # ========================================================

    def _trace_provenance(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        mappings = ctx.inputs.get(
            "mappings"
        )

        if not isinstance(mappings, list):
            raise GapError(
                "UNKNOWN/GAP: 'mappings' list required."
            )

        traced: List[Dict[str, Any]] = []

        for index, mapping in enumerate(
            mappings
        ):

            if not isinstance(mapping, dict):
                traced.append({
                    "index": index,
                    "status": "UNKNOWN/GAP",
                    "reason": (
                        "mapping_not_dictionary"
                    ),
                })
                continue

            evidence = mapping.get(
                "evidence",
                [],
            )

            provenance = mapping.get(
                "provenance"
            )

            traced.append({
                "index": index,
                "primitive": mapping.get(
                    "primitive"
                ),
                "evidence": evidence,
                "provenance": provenance,
                "status": (
                    "PRESENT"
                    if provenance
                    else "SOURCE_INPUT_ONLY"
                ),
            })

        return AgentResult(
            status=ExecutionStatus.VERIFIED,
            capability=ctx.capability,
            summary=(
                "Primitive provenance tracing completed."
            ),
            data={
                "mappings": traced,
            },
            confidence_ceiling=self.claim_ceiling,
            provenance=self._default_provenance(),
        )

    # ========================================================
    # CLAIM ASSESSMENT
    # ========================================================

    def _assess_claim(
        self,
        ctx: ExecutionContext,
    ) -> AgentResult:

        raw = ctx.inputs.get("claim")

        if not isinstance(raw, dict):
            raise GapError(
                "UNKNOWN/GAP: 'claim' dictionary required."
            )

        text = str(
            raw.get(
                "text",
                "",
            )
        ).strip()

        if not text:
            raise ValidationError(
                "claim text required"
            )

        evidence = list(
            raw.get(
                "evidence",
                [],
            )
        )

        scope = raw.get("scope")

        issues: List[str] = []

        if not evidence:
            issues.append(
                "missing_supporting_evidence"
            )

        if not scope:
            issues.append(
                "missing_scope"
            )

        universal_claim = bool(
            raw.get(
                "universal_claim",
                False,
            )
        )

        if universal_claim:
            issues.append(
                "primitive_model_does_not_establish_universal_ontology"
            )

        empirical_evidence = bool(
            raw.get(
                "independent_empirical_evidence",
                False,
            )
        )

        epistemic = (
            EpistemicClass.DERIVED
            if empirical_evidence
            else EpistemicClass.AMOS_MODEL
        )

        confidence = min(
            max(
                float(
                    raw.get(
                        "confidence",
                        0.80,
                    )
                ),
                0.0,
            ),
            self.claim_ceiling,
        )

        if issues:
            confidence = min(
                confidence,
                0.70,
            )

        return AgentResult(
            status=(
                ExecutionStatus.CONDITIONAL
                if issues
                else ExecutionStatus.VERIFIED
            ),
            capability=ctx.capability,
            summary=(
                "Primitive-level claim assessment completed."
            ),
            claims=[
                Claim(
                    text=text,
                    epistemic_class=epistemic,
                    confidence=confidence,
                    provenance=self._default_provenance(),
                    scope=scope,
                    falsifiers=list(
                        raw.get(
                            "falsifiers",
                            [],
                        )
                    ),
                )
            ],
            data={
                "issues": issues,
                "evidence_count": len(
                    evidence
                ),
                "independent_empirical_evidence": (
                    empirical_evidence
                ),
            },
            gaps=issues,
            confidence_ceiling=self.claim_ceiling,
            provenance=self._default_provenance(),
        )

    # ========================================================
    # CONFIDENCE / INTEGRITY
    # ========================================================

    def _aggregate_confidence(
        self,
        mappings: List[PrimitiveMapping],
    ) -> float:

        if not mappings:
            return 0.0

        weakest = min(
            item.confidence
            for item in mappings
        )

        return min(
            weakest,
            self.claim_ceiling,
        )

    def _validate_result(
        self,
        result: AgentResult,
    ) -> None:

        result.confidence_ceiling = min(
            result.confidence_ceiling,
            self.claim_ceiling,
        )

        for claim in result.claims:

            claim.confidence = min(
                claim.confidence,
                result.confidence_ceiling,
            )

            if (
                claim.epistemic_class
                in {
                    EpistemicClass.DERIVED,
                    EpistemicClass.AMOS_MODEL,
                    EpistemicClass.EMPIRICAL,
                }
                and not claim.provenance
            ):
                result.status = (
                    ExecutionStatus.CONDITIONAL
                )

                result.warnings.append(
                    "Claim missing provenance."
                )

    # ========================================================
    # PROVENANCE
    # ========================================================

    def _default_provenance(
        self,
    ) -> List[ProvenanceRef]:

        return [
            ProvenanceRef(
                source=(
                    "AMOS Absolute Primitive "
                    "Decomposer source skill"
                ),
                path=(
                    ".devin/skills/"
                    "amos-absolute-primitive-decomposer/"
                    "SKILL.md"
                ),
                content_hash=(
                    AGENT_CONFIG[
                        "content_hash"
                    ]
                ),
            )
        ]

    # ========================================================
    # UTILS
    # ========================================================

    @staticmethod
    def _new_correlation_id() -> str:

        payload = (
            f"{AGENT_ID}:"
            f"{time.time_ns()}"
        ).encode()

        return hashlib.sha256(
            payload
        ).hexdigest()[:16]

    @staticmethod
    def result_to_dict(
        result: AgentResult,
    ) -> Dict[str, Any]:

        return asdict(result)


# ============================================================
# EXAMPLE
# ============================================================

if __name__ == "__main__":

    logging.basicConfig(
        level=logging.INFO
    )

    agent = (
        AmosAbsolutePrimitiveDecomposerAgent(
            repo_root="."
        )
    )

    example = ExecutionContext(
        query=(
            "Decompose this system into "
            "supported AMOS primitives."
        ),
        capability="runtime.execute",
        authorized_write=True,
        authority_witness=(
            "steward_review:example"
        ),
        inputs={
            "scope": "example-system",
            "input": {
                "entities": [
                    "agent",
                    "memory_store",
                ],
                "relations": [
                    "agent reads memory_store",
                ],
                "time": [
                    "state changes across turns",
                ],
                "information": [
                    "retrieved context",
                ],
                "identity": [
                    "agent identity must persist",
                ],
                "contradictions": [
                    "current state conflicts with stale memory",
                ],
                "unresolved_business_policy": (
                    "No authority policy supplied."
                ),
            },
        },
    )

    try:

        result = agent.run(example)

        print(
            json.dumps(
                agent.result_to_dict(
                    result
                ),
                indent=2,
                ensure_ascii=False,
                default=str,
            )
        )

    except PrimitiveAgentError as exc:

        print(
            json.dumps(
                {
                    "status": "FAILED_CLOSED",
                    "agent": AGENT_ID,
                    "error": str(exc),
                },
                indent=2,
                ensure_ascii=False,
            )
        )