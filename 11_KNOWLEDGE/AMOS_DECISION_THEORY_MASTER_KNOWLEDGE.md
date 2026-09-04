---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Amos Decision Theory Master Knowledge
tags:
  - canon-group/tech-ai
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - misc
created: 2026-08-22
---
---
---

# AMOS Decision Theory Knowledge Master

## 1. Role

This knowledge master provides a unified treatment of decision theory for AMOS OS, integrating the previously fragmented coverage across C02 (mathematical optimization), C05 (behavioral decision processes), and C08 (game-theoretic decision making). Decision theory is the formal framework for choosing actions under uncertainty, and it underpins every consequential operation in AMOS OS.

## 2. H-Level Ownership

| Owner | Domain | Responsibility |
|-------|--------|---------------|
| H1 | Normative Foundations | Expected utility, rational choice axioms |
| H2 | Bayesian Decision Theory | Posterior-weighted decisions, expected value of information |
| H3 | Multi-Attribute Utility | Multiple objectives, Pareto optimality, trade-off analysis |
| H4 | Sequential Decision Making | Dynamic programming, MDPs, reinforcement learning |
| H5 | Bounded Rationality | Satisficing, heuristic search, cognitive limits |
| H6 | Behavioral Decision Theory | Prospect theory, framing effects, cognitive biases |
| H7 | Group Decision Making | Social choice, voting theory, mechanism design |
| H8 | Risk and Uncertainty | Risk measures, robust decision-making, minimax |
| H9 | AMOS Integration | Decision gates in control plane, authority escalation |

## 3. Normative Decision Theory

### 3.1 Expected Utility Theory (von Neumann-Morgenstern, 1944)

**Axioms:**

| Axiom | Statement | AMOS Analog |
|-------|-----------|-------------|
| Completeness | For any $A, B$: $A \succeq B$ or $B \succeq A$ | AMOS can always compare outcomes |
| Transitivity | $A \succeq B \wedge B \succeq C \implies A \succeq C$ | No circular preference loops |
| Continuity | $A \succeq B \succeq C \implies \exists \alpha: \alpha A + (1-\alpha)C \sim B$ | Intermediate outcomes are representable as gambles |
| Independence | $\alpha A + (1-\alpha)C \succeq \alpha B + (1-\alpha)C \iff A \succeq B$ | Adding common outcome doesn't change preference |

**Expected Utility:**

$$EU(a) = \sum_{s \in S} p(s) \cdot u(a, s)$$

where $a$ is an action, $s$ is a state of the world, $p(s)$ is the probability of state $s$, and $u(a, s)$ is the utility of action $a$ in state $s$.

**Optimal Decision:** $a^* = \arg\max_a EU(a)$

**AMOS Application:** The default decision framework for AMOS agents when full information is available. The control plane uses EU comparison for action selection.

### 3.2 Savage's Subjective Expected Utility (1954)

When probabilities are subjective (not objective frequencies):

$$SEU(a) = \sum_{s \in S} \mu(s) \cdot u(a, s)$$

where $\mu(s)$ is the agent's subjective belief (degree of confidence) in state $s$.

**AMOS Application:** AMOS agents operating with incomplete information use subjective probabilities derived from available evidence. The RSCF claim class determines the confidence weighting.

## 4. Bayesian Decision Theory

### 4.1 Expected Value of Information (EVI)

Before acquiring evidence $e$, the expected value of information is:

$$EVI(e) = EU(a^*_e) - EU(a^*)$$

where $a^*_e$ is the optimal action after observing $e$, and $a^*$ is the optimal action without $e$.

If $EVI(e) > 0$, acquiring evidence $e$ is decision-relevant.

**AMOS Application:** Determines whether gathering additional evidence (search, observation, experiment) is worth the cost before making a consequential decision.

### 4.2 Value of Perfect Information (EVPI)

$$EVPI = \mathbb{E}_e[EU(a^*_e)] - EU(a^*)$$

The maximum amount an agent should pay to resolve all uncertainty before deciding.

### 4.3 Bayesian Decision Network

```text
P(HYPOTHESIS | EVIDENCE) ∝ P(EVIDENCE | HYPOTHESIS) × P(HYPOTHESIS)
        ↓
DECISION = argmax_A Σ_H P(H | E) × U(A, H)
```

**AMOS Application:** The canonical decision-making pipeline in AMOS: update beliefs via Bayesian reasoning, then select action maximizing expected utility under updated beliefs.

## 5. Multi-Attribute Utility Theory

### 5.1 Multi-Objective Decision

When outcomes have multiple attributes $x_1, \ldots, x_k$:

$$U(x_1, \ldots, x_k) = \sum_{i=1}^{k} w_i \cdot u_i(x_i)$$

under conditions of **preferential independence** and **utility independence**.

If independence conditions don't hold, more complex utility functions are required.

### 5.2 Pareto Optimality

An outcome $x$ is **Pareto optimal** if no other outcome $y$ satisfies:
- $y_i \geq x_i$ for all $i$ (weakly better on all attributes)
- $y_j > x_j$ for at least one $j$ (strictly better on at least one)

**AMOS Application:** Multi-objective optimization in AMOS (e.g., accuracy vs speed vs resource usage). Pareto-optimal designs are the candidates; the control plane selects from the Pareto front using authority-level weighting.

### 5.3 Constraint Method

$$\max_{a} EU(a) \text{ subject to } EU_i(a) \geq \underline{EU}_i \text{ for all } i \neq i^*$$

Optimize one attribute while holding others above minimum thresholds.

**AMOS Application:** AMOS's INTEGRITY > COMPLETENESS > FLUENCY > SPEED > TOKEN_SAVINGS priority ordering (M01) is a constraint method — optimize lower-priority attributes only after higher-priority thresholds are met.

## 6. Sequential Decision Making

### 6.1 Markov Decision Process (MDP)

An MDP is a tuple $(S, A, T, R, \gamma)$:
- $S$: set of states
- $A$: set of actions
- $T(s'|s,a)$: transition probability
- $R(s,a)$: reward function
- $\gamma$: discount factor

**Value Iteration:**

$$V_{k+1}(s) = \max_a \left[ R(s,a) + \gamma \sum_{s'} T(s'|s,a) V_k(s') \right]$$

**Policy:** $\pi(s) = \arg\max_a \left[ R(s,a) + \gamma \sum_{s'} T(s'|s,a) V(s') \right]$

**AMOS Application:** AMOS runtime execution as an MDP — states are system configurations, actions are operations, transitions are state changes, rewards are outcome quality measures.

### 6.2 Partially Observable MDP (POMDP)

When the agent cannot directly observe the state:

$$b(s) = P(s | \text{observations})$$

The agent maintains a belief state $b$ and selects actions based on belief:

$$\pi(b) = \arg\max_a \sum_s b(s) \cdot U(s, a)$$

**AMOS Application:** AMOS agents operating with incomplete information (which is most of the time) use belief states derived from RSCF evidence weighting.

### 6.3 Planning Horizon

| Horizon | Description | AMOS Application |
|---------|-------------|-----------------|
| Single-step | Choose one action, no future consideration | Simple task execution |
| Finite horizon | Fixed number of steps ahead | Task planning with deadline |
| Infinite horizon | Indefinite future, discounted | Long-term knowledge strategy |
| Risk-sensitive | Optimize worst-case or variance | Safety-critical operations |

## 7. Bounded Rationality (Simon, 1955)

### 7.1 Satisficing

When optimization is computationally intractable, choose the first option that meets an **aspiration level** $\alpha$:

$$\text{Choose } a \text{ s.t. } U(a) \geq \alpha$$

**AMOS Application:** When full EU computation is too expensive (e.g., real-time BCI decoding), AMOS agents satisfice using heuristic thresholds.

### 7.2 Resource-Rational Analysis

The optimal decision procedure accounts for cognitive/computational costs:

$$\text{Choose procedure } \pi \text{ s.t. } \text{Value}(\pi) - \text{Cost}(\pi) \text{ is maximized}$$

**AMOS Application:** AMOS's fast-path vs full-path decision routing (M16: FAST_PATH != SKIP_VALIDATION) — fast paths are resource-rational shortcuts that sacrifice optimality for speed.

### 7.3 Heuristics and Biases

| Heuristic | Description | AMOS Mitigation |
|-----------|-------------|-----------------|
| Availability | Judging probability by ease of recall | Cross-reference with base rates |
| Representativeness | Judging probability by similarity to prototype | Bayesian update required |
| Anchoring | Over-relying on initial information | Explicit anchor adjustment protocol |
| Framing | Different choices based on presentation | Normalize to consistent reference frame |

## 8. Behavioral Decision Theory

### 8.1 Prospect Theory (Kahneman & Tversky, 1979)

$$V = \sum_{i} \pi(p_i) \cdot v(x_i)$$

Value function $v(x)$:
- Defined on gains and losses (reference-dependent)
- Concave for gains (risk aversion): $v''(x) < 0$ for $x > 0$
- Convex for losses (risk seeking): $v''(x) > 0$ for $x < 0$
- Loss aversion: $v(-x) \approx -2.25 \cdot v(x)$

Probability weighting function $\pi(p)$:
- Overweights small probabilities
- Underweights large probabilities

**AMOS Application:** AMOS acknowledges that human decision-makers in the loop exhibit prospect theory effects. The control plane accounts for framing effects when presenting options to human stewards.

### 8.2 Cumulative Prospect Theory (Tversky & Kahneman, 1992)

Generalizes prospect theory to continuous distributions and satisfies stochastic dominance.

### 8.3 Hyperbolic Discounting

$$U(a_t) = u(a_t) \cdot \beta \cdot \delta^t$$

where $\beta < 1$ captures present bias and $\delta$ is the long-run discount rate.

**AMOS Application:** AMOS agents without explicit future-planning may exhibit myopic behavior. The runtime decision path includes explicit long-horizon checks to mitigate hyperbolic discounting.

## 9. Risk and Uncertainty

### 9.1 Risk Measures

| Measure | Formula | Properties |
|---------|---------|------------|
| Variance | $\text{Var}(X) = \mathbb{E}[(X-\mu)^2]$ | Symmetric, penalizes upside |
| Semivariance | $\text{Var}^-(X) = \mathbb{E}[\min(X-\mu, 0)^2]$ | Downside risk only |
| Value at Risk (VaR) | $P(X \leq \text{VaR}_\alpha) = \alpha$ | Simple, non-subadditive |
| Conditional VaR (CVaR) | $\mathbb{E}[X | X \leq \text{VaR}_\alpha]$ | Coherent risk measure |
| Entropic Risk | $\frac{1}{\theta}\log \mathbb{E}[e^{\theta X}]$ | Consistent with EU |

### 9.2 Minimax Decision Rule

$$a^* = \arg\min_a \max_{s} L(a, s)$$

Choose the action that minimizes the worst-case loss.

**AMOS Application:** Safety-critical decisions use minimax: the action must be acceptable even under the worst-case scenario. This aligns with AMOS's fail-closed philosophy.

### 9.3 Robust Decision Making

When probability distributions are uncertain (ambiguity), use **maxmin expected utility**:

$$a^* = \arg\max_a \min_{\mu \in \mathcal{M}} \sum_s \mu(s) \cdot u(a, s)$$

where $\mathcal{M}$ is a set of possible probability distributions.

**AMOS Application:** When evidence is sparse or conflicting (COMPETING claims), AMOS uses robust decision-making over the set of plausible belief distributions.

## 10. Group Decision Making

### 10.1 Arrow's Impossibility Theorem

No social welfare function satisfies all of: unrestricted domain, Pareto efficiency, independence of irrelevant alternatives, non-dictatorship.

**AMOS Application:** When multiple AMOS agents must reach consensus, no perfect aggregation mechanism exists. AMOS uses controlled voting with explicit trade-off transparency.

### 10.2 Mechanism Design

Design the rules of the game so that self-interested agents produce desired outcomes.

**AMOS Application:** The control plane's authority and permission system is a mechanism design — agents act in their local interest, and the mechanism ensures system-wide invariants are preserved.

## 11. AMOS Integration

### 11.1 Decision Gates in Control Plane

```text
REQUEST
↓
IDENTIFY decision type
├── Single-attribute, full info → Expected Utility
├── Multi-attribute → Multi-Attribute Utility
├── Sequential → MDP/POMDP
├── Under uncertainty → Robust/Minimax
├── With human in loop → Prospect Theory aware
└── Computationally constrained → Satisficing
↓
COMPUTE optimal action (within resource budget)
↓
AUTHORITY CHECK (M01, M12)
↓
EXECUTE or ESCALATE
```

### 11.2 Decision-Theory-Informed Invariants

| Invariant | Decision Theory Basis |
|-----------|----------------------|
| M01: INTEGRITY > COMPLETENESS > ... | Multi-attribute constraint method |
| M12: AGENT_CAPABILITY != AUTHORITY | Authority is a decision right, not an ability |
| M16: FAST_PATH != SKIP_VALIDATION | Resource-rational analysis: fast ≠ optimal |
| M17: LOCAL_GAIN != BREAK_HIGHER_SCALE | Multi-level optimization: local EU ≠ global EU |
| M20: IRREVERSIBLE_ACTION_REQUIRES_STRONGER_GOVERNANCE | Minimax: irreversible actions have worst-case amplification |

### 11.3 Cross-Domain Decision Bridges

- **Game Theory → Decision Theory:** Nash equilibrium as fixed point of best-response dynamics
- **Behavioral → Normative:** Prospect theory describes how humans actually decide; EU theory prescribes how they should decide
- **Sequential → Single-step:** MDP value iteration reduces to single-step EU at each time step
- **Bounded → Full rationality:** Satisficing is EU-optimal given computational constraints

## 12. Knowledge Status

| Claim | Class | Status | Falsifiers |
|-------|-------|--------|------------|
| EU theory is normatively correct under its axioms | VERIFIED | Axiomatic (von Neumann-Morgenstern 1944) | Axiom violation |
| Humans systematically violate EU axioms | VERIFIED | Empirically established (Kahneman & Tversky 1979) | Systematic EU compliance |
| Prospect theory better predicts human choices | VERIFIED | Empirically supported across cultures | Prospect theory failure |
| Bounded rationality is normatively appropriate for computational agents | DERIVED | Resource-rational analysis framework | Unbounded computation available |
| Multi-attribute independence conditions hold for AMOS decisions | MODEL | Assumed for tractability | Non-independent attributes |

______________________________________________________________________

**MOC:** [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]] · [[00_ROOT/00_HOME|00_HOME]]

**Related:** [[11_KNOWLEDGE/AMOS_C02_MATH_COMPUTE_MASTER_KNOWLEDGE|AMOS_C02_MATH_COMPUTE_MASTER_KNOWLEDGE]] · [[11_KNOWLEDGE/AMOS_C05_MIND_BEHAVIOR_MASTER_KNOWLEDGE|AMOS_C05_MIND_BEHAVIOR_MASTER_KNOWLEDGE]] · [[11_KNOWLEDGE/AMOS_C08_STRATEGY_GAME_MASTER_KNOWLEDGE|AMOS_C08_STRATEGY_GAME_MASTER_KNOWLEDGE]] · [[03_CONTROL_PLANE/03_CONTROL_PLANE_MOC|03_CONTROL_PLANE_MOC]]
