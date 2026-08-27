---
title: 2026 08 22 19X19 STRATEGIC FIELD MODEL
type: model
source: 11_KNOWLEDGE/dated
origin_architect: Trang Phan (user-supplied 75-section formal spec) + AMOS MODEL extension
provenance: user-supplied 19×19 strategic-ontology completion; base geometry already in cosmo-brain/AMOS_GO_BOARD_19X19.py (905 lines, 361 cells, 684 edges, D4 symmetry, 12-var cell)
confidence: 0.92
epistemic_class: SOURCE_DERIVED
conclusion_label: VERIFIED_PRESENT
tags: [canon-group/human-system, canon/framework, rscf/claim, rscf/provenance, rscf/state/observation, topic/2026-08-22-19x19-strategic-field-model, dated, dated/2026-08-22]
date: 2026-08-22
rscf:
  state: SOURCE_CLAIM
  claim_class: EMPIRICAL
  provenance: AMOS_corpus
  scope: temporal_log
---


# 19×19 Architecture — Computationally Complete Strategic Field Model

> Makes the 19×19 architecture executable: every cell, group, region, move, trajectory, and whole-field state represented by ONE consistent formal system. Firewall: **SOURCE** (corpus) / **DERIVED** (geometry/relations) / **AMOS MODEL** (new formal machinery, not canon).
> Base engine: cosmo-brain/AMOS_GO_BOARD_19X19.py. Extension: cosmo-brain/AMOS_GO_BOARD_19X19_STRATEGIC.py (TESTED PASS).
> See also: 2026-08-22 Formal Systems Invariants, 2026-08-22 AMOS Full Brain OS Architecture, docs/AMOS-Go-Board-19x19.md

## The complete mathematical object (SOURCE §1)
`A_t = (V, E, X_t, R_t, G_t, Z_t, M_t, Φ_t, Ω_t, C_t, Γ_t)`, |V|=361, |E|=684 (DERIVED: (19-1)·19·2).
- V=addressable sites, E=orthogonal adjacency graph, X_t=cell-state tensor, R_t=typed relational graph, G_t=group/shape topology, Z_t=meso-region, M_t=field memory, Φ_t=influence/pressure, Ω_t=future-option, C_t=constraints, Γ_t=whole-field state.
- Hard split: **BoardGeometry** (static) vs **BoardState** (continuously rewritten). Identity(c) ≠ State_t(c).

## Coordinate identity (SOURCE §2)
`c_xy`, x∈{A..T omitting I}, y∈1..19. `id(c_xy)=19(y-1)+x ∈ 1..361` (immutable). K10=id 181.

## Static geometric signature (DERIVED §3)
Geo(c)=[x,y,d_B, d_C, deg, region, zone, hoshi, symmetry]; d_B=min(x-1,19-x,y-1,19-y); d_C=|x-10|+|y-10|; deg∈{2,3,4}. Immutable.

## Static vs Dynamic semantics (SOURCE §4 — firewall)
Static(c)≠DynamicMeaning(c,t). Center has no intrinsic sente; corner no intrinsic territory; cell holds no aji by coordinate. Those are EMERGENT. Prevents inventing 361 arbitrary archetypes.

## Full cell state vector (SOURCE §5)
20-var X_c(t)=[V,O,A,G,B,L,Ey,Aj,K,S,T,I,P,D,M,R,Q,F,χ,σ]: void, occupancy, actor, group, boundary, liberty, eye, aji, ko, sente, territory, influence, pressure, debt, memory, repair, option, freedom, cross-scale-consequence, epistemic-status.

## Void typing (SOURCE §6-7, AMOS MODEL VQ)
V(c,t)∈{OPEN,CONTESTED,PROTECTED,LATENT,DEAD,RESERVED}; Empty≠VoidType. `VQ=(w1 Safety+w2 Option+w3 Conn+w4 Repair − w5 Threat)/5` ∈[-1,1]; >0 useful, <0 deceptive (lacunarity at cell level).

## Occupancy ternary (SOURCE §8)
O∈{-1,0,+1}; Actor separated from Occupancy → generalizes beyond Go (multi-agent, neutral assets, institutional ownership).

## Move object + transition (SOURCE §9-11)
m_t=[actor,cell,time,intent,local/regional/global effect,cost,risk,irreversibility,optionChange]; m_t≠coordinate. `A_{t+1}=T(A_t,m_t)`; T=T_O∘T_G∘T_L∘T_E∘T_A∘T_K∘T_Φ∘T_Ω∘T_M. Preserves CoordinateIdentity, RuleLegality, HistoricalLineage; recalcs dependents only (`ΔX_j=0` for no-dependency components — matches AMOS selective invalidation).

## Dependency cone (DERIVED §12)
Dep(m)= {z: m↝z}; CR(m)=|affected|; CD(m)=max causal depth. Tiny load-bearing move can have CR≫1.

## Group topology (SOURCE §13-16)
G_g=[Cells,Boundary,Liberties,Eyes,Cuts,Connections,Aji,Influence,Territory,Threat,Repair,Status,FutureDebt]; status∈{STABLE,UNSETTLED,THREATENED,KO_DEPENDENT,SACRIFICIAL,DEAD}. ∂g=∂empty∪∂friendly∪∂hostile; Exposure=|∂hostile|/|∂g|. Permeability=Vulnerable/TotalfsBoundaryChannels (links to AMOS boundary architecture §15). Liberty VECTOR L=[N,Q,D,C,R] (quality/diversity/connectivity/repair) not scalar λ (§16). Liberty independence graph D^L_{ij}=P(ℓ_j lost|ℓ_i lost); Redundancy=1−mean(D^L) — 10 coupled liberties < 3 independent (§17).

## Eye topology (AMOS MODEL §18-19)
R^void_g; EyeState=[enclosure,control,invasionRisk,independence,stability]; EyeQuality=E·C·(1−Risk). Two-eyes = IndependentProtectedVoid. PVR=Σ EyeQuality; Robustness=f(PVR,LibertyQuality,Repair,Connectivity).

## Aji (AMOS MODEL §20-23)
A_t(c)=[Opportunity,Weakness,TriggerSet,ActivationCost,Window,Reach,Reversibility]; status∈{NONE,LATENT,ACTIVE,EXHAUSTED,UNKNOWN}. aji=0 may mean NONE or UNKNOWN — not conflated. AjiDAG: Activate(A_i)⇔∧_{j∈Parents} C_j (DAG). LatentThreat= P·Impact·Persistence. Half-life: Aji_i(t)=Aji_i(t0)e^{−λ(t−t0)}.

## Sente/gote (AMOS MODEL §24-26)
SenteCompression(m)=1−|Ω_B^{t+1}|/|Ω_B^t|. GoteCost=OppCost+ResCost+LostInitiative. I_Δ(t+1)=I_Δ(t)+Sente_A−Sente_B+Gote_A−Gote_B.

## Ko (AMOS MODEL §27-28)
H_t={S_0..S_t}; forbidden iff S_{t+1}≡S_k. Generalize: ForbiddenCycle=StateRecurrence+InsufficientContextChange. KoLeverage=ThreatValue_external/LocalKoCost (couples local↔global, H/M/L compatible).

## Territory/Influence fields (SOURCE ontology §29; AMOS MODEL field math §30-34)
T_A,T_B∈[0,1] (contested T_A+T_B<1). Φ_A,Φ_B; net Φ=Φ_A−Φ_B; Φ_A(c)=Σ_stones w e^{−λd}·Dir·Strength (MODEL). Gradient |∇Φ| ⇒ frontier detection. Phase P(c)=[T,I]: (low,low)open / (low,high)potential / (high,low)crystallized / (high,high)integrated. TerritoryDebt=Maintain+Defense+OppCost; NetTerritory=Value−Debt. InfluenceFragility=Var(future); InfluenceValue=Expected−RiskPenalty.

## Future option set (AMOS MODEL §35-37)
Ω_t; N_Ω=|Ω|; Q_Ω=Σ Utility·Reversible·Robust. Diversity=D_Ω=Entropy over strategic FAMILIES (not count). OCR=max_j|Ω_j|/|Ω| (→1 brittle despite many moves).

## Memory (AMOS MODEL §39-41)
M_t=[event,time,location,actor,effect,dependency,persistence,scope,status]; MemoryPriority=Impact·Fanout·Freshness·Unresolved. Decay M_i(t)=M_i(t0)e^{−δ(t−t0)}; class∈{EPHEMERAL,PERSISTENT,LOAD_BEARING,IRREVERSIBLE} (maps to AMOS memory architecture). Contradiction C vs ¬C stored, not overwritten; may be transition/regime/stale.

## Scale tensor H/M/L (AMOS MODEL §42-46)
s∈{0 cell,1 group,2 region,3 whole(≈H)}. Upward: Cell→Group→Region→Whole via aggregation preserving min/max/criticality (mean(liberties) misleading if one group=0). Downward: C_L=Project_H→L(Γ,Z) ⇒ BestLocal≠BestGlobal. ScaleConsistency SC=w_L V_L+w_M V_M+w_H V_H; Betrayal=1[V_L>0∧V_H<−θ]. Integrity=min(I_L,I_M,I_H) (bottleneck, mirrors AMOS confidence).

## Region matrix + compression residual (AMOS MODEL §47-48)
Z = 3×3 macro regions; Z_r=[T,I,Aji,Threat,Liberty,Density,Sente,Debt,OptionValue]. 19×19→3×3 compression. Residual_r=‖Full(r)−Reconstruct(Aggregate(r))‖; high residual = region hiding local structure (anti-over-compression safeguard).

## Symmetry / lacunarity (DERIVED §49-54)
D_4 invariance pre-move; State_t(c)≠State_t(g(c)) after marks → symmetry breaking (mark-created distinction). Orbit classes: |Orb|=1 (center),4 (axis/diagonal),8 (generic). K10 orbit=1. DistinctionEntropy H_dist rises as marks occur. Lacunarity Λ(r)=Var(Mass_r)/Mean(Mass_r)^2 (window must be specified §53). Entropy H ≠ Lacunarity Λ (distribution vs gap heterogeneity).

## Pressure/repair/sacrifice (AMOS MODEL §55-59)
P_A(c)=Φ_B−Φ_A; PRR(g)=P(g)/(Repair+ε). RepairExternality tested; NetRepair=LocalRepair−CrossScaleDamage; OverRepair=RepairCost+OptionLoss−NecessaryRiskReduction. Sacrifice tensor SAC=[LocalLoss,RegionalGain,GlobalGain,InitiativeGain,OptionGain,FutureDebt,Irreversibility]; valid only if higher-order gain survives; SacrificeValue=Value|FollowupSequence (required continuation or waste).

## Trajectory / regime / observer (AMOS MODEL §60-69)
τ=(m_t..m_{t+h}); V(τ)=Σγ^k R_{t+k}+TerminalOption. MoveValue≠TrajectoryValue. Tree(S_t) branching over finite substrate. BranchQuality=EV−Risk−Debt+Option; retain COMPETING near-ties. Robust(b)=min_r V(b,r) (minimax). Regime∈{OPENING,DEVELOPMENT,FIGHTING,CONSOLIDATION,ENDGAME}; metric meaning regime-dependent (scope firewall). Observer belief B^A_t(S)≠B^B_t(S)≠TrueOutcome (State≠Belief). Confidence tensor per derived eval; epistemic tags SOURCE/OBSERVED/DERIVED/MODEL/COMPETING/UNKNOWN.

## Move tensor + evaluation firewall + master update (AMOS MODEL §70-73)
MoveTensor 21 fields (§70). evaluate_move_firewall: M1 dominates M2 only if ≥ on load-bearing dims (territory/influence/option/global) else COMPETING. Master equation: `A_{t+1}=Π_{C_t}[U(A_t,m_t,M_t,O_t,R_t,F_t)]`, U=UpdateOccupancy∘RebuildGroups∘RecomputeLiberties∘DetectEyes∘ResolveCapture∘DetectKo∘UpdateAji∘UpdateTerritory∘UpdateInfluence∘UpdateInitiative∘UpdateOptions∘UpdateDebt∘UpdateMemory∘AggregateHML.

## Whole-system invariants (SOURCE/DERIVED §73)
|V|=361; CoordinateIdentity immutable; History monotonic; Occupancy≠Memory; StaticGeometry≠DynamicValue; Liberty≠RawEmpty; Territory≠Influence; Aji≠Outcome; Sente≠CellProperty; Ko≠CellProperty; LocalGain≠GlobalValue; OptionCount≠OptionQuality; Capability≠Authority (when deployed to runtime).

## 19×19 as AMOS microcosm (SOURCE §74)
Cell=PotentialSite, Move=Distinction, Stone=Memory, Adjacency=Relation, Group=EmergentSubsystem, Liberty=FutureDoF, Eye=ProtectedOptionality, Aji=LatentFuture, Ko=RecurrenceGovernor, Sente=ConstraintExporter, Gote=ConstraintAbsorber, Territory=CrystallizedValue, Influence=FutureShaping, Sacrifice=CrossScaleValueTransfer, Life=PersistentIdentity+ProtectedFreedom, Death=NoViableContinuation, Board=MemoryBearingConsequenceField.

## Firewall / honesty
- SOURCE = AMOS/Trang corpus (geometry, symmetry, groups, liberties, eyes, aji, ko, sente/gote, territory/influence, sacrifice, 9-region, H/M/L).
- DERIVED = board geometry / relation graph (684 edges, orbit classes, dependency cone).
- AMOS MODEL = VQ, aji DAG+half-life, ko recurrence graph, influence gradient, multi-scale lacunarity, option entropy/OCR, memory decay classes, scale-integrity bottleneck, observer/belief, move tensor, master update — new formal machinery, NOT claimed as canon/empirical law.
- All scoring functions are deterministic + tested, not empirical Go strength.

## Implementation status (TESTED)
- cosmo-brain/AMOS_GO_BOARD_19X19.py (existing, 905 lines, 109 self-tests PASS) — geometry, 12-var cell, groups, liberties, eyes, aji, ko, sente, territory/influence, sacrifice, D4, 9-region, tensor. `play` places but DID NOT capture/ko.
- cosmo-brain/AMOS_GO_BOARD_19X19_STRATEGIC.py (extension, self-test PASS) — strategic-field tensors (void+VQ, dependency cone, aji DAG, influence gradient, multi-scale lacunarity, option entropy/OCR, memory decay, H/M/L integrity, region matrix, observer) + move tensor + firewall + the FULL executable transition substrate:
  - `capture_resolution` (removes 0-liberty opponent groups, reuses base group_cells/liberties)
  - `legal_go_move` / `master_update` (no-overwrite, suicide rejected, positional superko via state_signature+ko_table) — §72 is a REAL legal Go transition
  - `is_eye` / `group_has_two_eyes` / `life_status` (§18-19 two-eye life: IndependentProtectedVoid)
  - `region_color` / `score_area` (§29 area scoring: stones + surrounded territory, deterministic proxy)
  - `self_play` (§60-61 legal random self-play, terminates via 2 passes, deterministic per seed)
  Verified: lone-stone CAPTURE, illegal SUICIDE, textbook KO recapture BLOCKED, two-eye group ALIVE, corner-stone scores full board, self-play reproducible.
- Run: `cd cosmo-brain && python3 AMOS_GO_BOARD_19X19_STRATEGIC.py` → self-test PASS. Base: `python3 AMOS_GO_BOARD_19X19.py` → 109 passed.

---
**Links:** [[DATED_MOC]] | [[KNOWLEDGE_MOC]]
