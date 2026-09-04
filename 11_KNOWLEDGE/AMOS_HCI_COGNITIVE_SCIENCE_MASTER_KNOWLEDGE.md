---
canon-group: meta
canon-type: framework
rscf-state: source-claim
rscf-claim: verified
rscf-provenance: AMOS_corpus
conclusion_class: AMOS_MODEL
epistemic_class: SOURCE_CLAIM
topic: Amos Hci Cognitive Science Master Knowledge
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

# AMOS HCI & Cognitive Science of Interaction Knowledge Master

## 1. Role

This knowledge master provides the theoretical foundation for human-computer interaction within AMOS OS. It bridges the operational UX design kernels with the cognitive science of interaction, covering cognitive load theory, distributed cognition, situated action, affordance theory, and BCI-specific human factors.

**AMOS Context:** As a cognitive OS with BCI interfaces, AMOS must understand how humans interact with computational systems at the deepest level — not just UI patterns, but the cognitive science that makes interaction succeed or fail.

## 2. H-Level Ownership

| Owner | Domain | Responsibility |
|-------|--------|---------------|
| H1 | Cognitive Load Theory | Intrinsic, extraneous, germane load; working memory limits |
| H2 | Distributed Cognition | Cognition across agents, artifacts, and environment |
| H3 | Situated Action | Context-dependent, improvisational interaction |
| H4 | Affordance Theory | Gibsonian affordances, signifiers, perceived action possibilities |
| H5 | Interaction Design Patterns | Reusable interaction structures, design systems |
| H6 | BCI Human Factors | Setup burden, fatigue, calibration, cognitive overhead |
| H7 | Attention & Multitasking | Selective attention, dual-task interference, interruption science |
| H8 | Error & Recovery | Human error taxonomy, recovery strategies, resilient interaction |
| H9 | AMOS Integration | Human-system interface design for cognitive OS |

## 3. Cognitive Load Theory (Sweller, 1988)

### 3.1 Three Types of Cognitive Load

| Load Type | Definition | AMOS Application |
|-----------|-----------|-----------------|
| **Intrinsic** | Difficulty inherent to the material/task | AMOS task complexity; BCI command vocabulary size |
| **Extraneous** | Difficulty imposed by presentation/interface | AMOS UI/interface design quality |
| **Germane** | Effort devoted to learning/schema construction | AMOS user learning curve, onboarding |

**Total Cognitive Load:** $CL_{total} = CL_{intrinsic} + CL_{extraneous} + CL_{germane}$

**Constraint:** $CL_{total} \leq CL_{capacity}$ (working memory capacity)

When $CL_{total} > CL_{capacity}$, performance degrades, errors increase, and learning fails.

### 3.2 Working Memory Limits

Miller (1956): $7 \pm 2$ chunks in working memory

Cowan (2001): $4 \pm 1$ chunks when controlled for rehearsal

**AMOS Application:** AMOS interface designs must present information in chunks of 4±1 items. BCI command vocabularies should not exceed working memory limits without hierarchical organization.

### 3.3 Expertise Reversal Effect

Instructional techniques that help novices can harm experts (Kalyuga et al., 2003).

**AMOS Application:** AMOS interfaces must adapt to user expertise level — detailed guidance for novices, minimal scaffolding for experts. The BCI calibration process must account for user learning over time.

### 3.4 Cognitive Load Measurement

| Method | Type | Invasiveness |
|--------|------|-------------|
| NASA-TLX | Subjective | Low |
| Dual-task performance | Behavioral | Medium |
| Pupillometry | Physiological | Low |
| EEG theta/alpha ratio | Physiological | Medium (requires EEG) |
| fNIRS | Physiological | High (requires headgear) |

**AMOS Application:** BCI systems can directly measure cognitive load via EEG theta/alpha ratio — a unique advantage of brain-computer interfaces over traditional UIs.

## 4. Distributed Cognition (Hutchins, 1995)

### 4.1 Core Principles

1. **Cognition is distributed across agents:** No single agent holds all knowledge
2. **Cognition is distributed across artifacts:** Tools, representations, and media carry cognitive work
3. **Cognition is distributed across time:** Past cognitive products shape current cognition

**AMOS Application:** AMOS is inherently a distributed cognitive system — knowledge, reasoning, and decision-making are distributed across agents, kernels, and memory systems.

### 4.2 Representational State Transformation

```text
INPUT REPRESENTATION → MEDIUM → OUTPUT REPRESENTATION
        ↓                            ↓
   (cognitive work)            (cognitive work)
```

Cognitive work is performed by transforming representations across media.

**AMOS Application:** Every AMOS pipeline transforms representations: raw data → RSCF claims → validated knowledge → decisions → actions. Each transformation is a unit of distributed cognitive work.

### 4.3 Organizational Distribution

| Distribution Type | Description | AMOS Analog |
|------------------|-------------|-------------|
| Spatial | Cognition distributed across physical locations | Shards, distributed processing |
| Temporal | Cognition distributed across time | Memory, provenance chains |
| Social | Cognition distributed across agents | Multi-agent reasoning |
| Embodied | Cognition uses body and environment | BCI neural interface |

## 5. Situated Action (Suchman, 1987)

### 5.1 Plans vs Situated Action

| Concept | Definition | Implication |
|---------|-----------|-------------|
| **Plan** | Pre-specified sequence of actions | Works in predictable environments |
| **Situated Action** | Improvisational response to local circumstances | Necessary when plans meet reality |

"Plans are resources for situated action, not blueprints for it." — Suchman

**AMOS Application:** AMOS workflows are plans, but agents must be prepared to adapt them when circumstances deviate. The runtime decision path includes explicit deviation handling.

### 5.2 Common Ground (Clark & Brennan, 1991)

Successful interaction requires **common ground** — mutual knowledge, beliefs, and assumptions.

**AMOS Application:** Human-AMOS interaction requires common ground about:
- What AMOS can and cannot do (capability transparency)
- What authority AMOS has (authority transparency)
- What AMOS knows and doesn't know (knowledge transparency)

The CAPABILITY != AUTHORITY invariant (M01) is a common-ground enforcement mechanism.

## 6. Affordance Theory

### 6.1 Gibsonian Affordances (Gibson, 1979)

An affordance is a relationship between an actor and the environment — a possibility for action:

$$\text{Affordance} = f(\text{actor properties}, \text{environment properties})$$

Key property: affordances exist whether or not they are perceived.

### 6.2 Norman's Affordances & Signifiers (Norman, 1988, 2013)

- **Perceived affordances:** What the user thinks they can do
- **Signifiers:** Signals that communicate where action should take place

Norman's key insight: **What matters is not affordances but signifiers** — how the user knows what to do.

**AMOS Application:** AMOS interfaces must provide clear signifiers for:
- Available actions (what AMOS can do)
- Authority boundaries (what requires escalation)
- State (what AMOS currently knows/believes)
- Uncertainty (where AMOS is uncertain)

### 6.3 Affordances in BCI

BCI-specific affordances:
- **Neural affordances:** The brain's capacity for specific control signals (motor imagery, P300, SSVEP)
- **Calibration affordances:** Feedback that guides user toward learnable control patterns
- **Error affordances:** Clear indication of misclassification so user can correct

## 7. Attention & Multitasking

### 7.1 Selective Attention (Broadbent, 1958; Treisman, 1964)

The cognitive system can selectively process some stimuli while ignoring others.

**Bottleneck theories:**
- Early selection (Broadbent): Filter before semantic processing
- Late selection (Deutsch & Deutsch): Filter after semantic processing
- Attenuation (Treisman): Partial processing of unattended stimuli

**AMOS Application:** AMOS output to the user must account for attentional bottlenecks — critical information must be in the attended channel, not peripheral.

### 7.2 Dual-Task Interference

When two tasks require the same cognitive resources, performance on one or both degrades.

**AMOS Application:** BCI users can only control one BCI paradigm at a time. AMOS must serialize BCI commands or use distinct neural pathways for parallel commands.

### 7.3 Interruption Science

| Factor | Effect on Interruption Recovery |
|--------|-------------------------------|
| Task complexity | More complex = harder to resume |
| Interruption duration | Longer = harder to resume |
| Relevance of interruption | Relevant = faster recovery |
| Working memory load at interruption | Higher load = harder to resume |

**AMOS Application:** AMOS interruptions to human users must be:
- Relevant (filtered by authority and context)
- Timed (not during high cognitive load)
- Bounded (minimal information required)

## 8. Error & Recovery

### 8.1 Human Error Taxonomy (Reason, 1990)

| Error Type | Description | AMOS Prevention |
|-----------|-------------|-----------------|
| **Slip** | Correct intention, wrong execution | Confirmation for irreversible actions |
| **Lapse** | Memory failure | Persistent state display |
| **Mistake** | Wrong intention (incomplete/incorrect model) | Explicit reasoning transparency |
| **Violation** | Deliberate deviation from procedure | Authority boundary enforcement |

### 8.2 Error Recovery Strategies

```text
ERROR DETECTED
↓
CLASSIFY (slip/lapse/mistake/violation)
↓
DISPLAY ERROR STATE
↓
SUGGEST CORRECTION (if possible)
↓
ALLOW UNDO (if applicable)
↓
LEARN FROM ERROR (update user model)
```

**AMOS Application:** AMOS must support error recovery at every level:
- **BCI level:** Misclassified neural signal → immediate feedback + re-classification opportunity
- **Agent level:** Wrong inference → rollback (K_FAILURE_RECOVERY)
- **System level:** System error → graceful degradation + notification

### 8.3 Resilient Interaction

The goal is not to prevent all errors but to make systems **resilient** — able to recover from errors without catastrophic consequences.

**AMOS Application:** AMOS's fail-closed recovery architecture (K_FAILURE_RECOVERY) is a form of resilient interaction at the system level.

## 9. BCI-Specific Human Factors

### 9.1 BCI Interaction Challenges

| Challenge | Description | Mitigation |
|-----------|-------------|------------|
| Setup burden | Electrode application, gel, calibration | Dry electrodes, auto-calibration |
| Fatigue | Neural fatigue from sustained control | Adaptive task difficulty, rest periods |
| Cognitive load | BCI adds cognitive overhead beyond normal interaction | Minimize BCI-specific load, integrate naturally |
| Poor usability | BCI systems designed by engineers, not designers | Human-centered design process |
| Latency | Neural signal processing delay | Predictive algorithms, feedforward displays |
| Error rates | BCI misclassification frustrates users | Error correction, confidence-based filtering |

### 9.2 BCI Usability Metrics

| Metric | Definition | Target |
|--------|-----------|--------|
| Information transfer rate (ITR) | Bits per minute of correct communication | Maximize |
| Fitts's law throughput | Efficiency of target acquisition | > 2 bits/second |
| Error rate | Proportion of incorrect commands | < 5% |
| Calibration time | Time to achieve acceptable accuracy | < 5 minutes |
| User satisfaction | Subjective rating (SUS, NASA-TLX) | > 80/100 |

### 9.3 Adaptive BCI Interfaces

```text
MONITOR user performance
↓
ESTIMATE cognitive load (EEG theta/alpha)
↓
IF load > threshold:
    Simplify interface
    Reduce command vocabulary
    Increase confirmation threshold
ELSE IF load < threshold:
    Enrich interface
    Expand command vocabulary
    Decrease confirmation threshold
```

## 10. AMOS Integration

### 10.1 Human-System Interface Design Principles

| Principle | Description | AMOS Implementation |
|-----------|-------------|---------------------|
| **Transparency** | User understands what AMOS is doing | Explicit reasoning traces, confidence displays |
| **Controllability** | User can override AMOS at any time | Kill switch, manual override authority |
| **Predictability** | User can anticipate AMOS behavior | Consistent interaction patterns, preview |
| **Feedback** | User knows the result of their actions | Immediate confirmation, state display |
| **Graceful Degradation** | AMOS fails without catastrophic user impact | Fail-closed, degraded-mode operation |
| **Adaptivity** | AMOS adapts to user expertise and state | Cognitive load monitoring, adaptive interface |

### 10.2 Interaction Architecture

```text
HUMAN (BCI + traditional input)
↓
INPUT PROCESSING (signal classification, intent estimation)
↓
COGNITIVE MODEL (user state, expertise, load)
↓
ADAPTIVE INTERFACE (adjust to user state)
↓
AMOS REASONING (inference, decision)
↓
OUTPUT (display, feedback, confirmation)
↓
HUMAN PERCEPTION (attention, comprehension)
```

### 10.3 Cross-Domain Bridges

- **Cognitive Load → BCI:** EEG theta/alpha ratio as real-time CL measurement
- **Distributed Cognition → AMOS Architecture:** AMOS is a distributed cognitive system
- **Affordance Theory → BCI Design:** Neural affordances as action possibilities
- **Error Theory → Recovery:** Human error taxonomy maps to AMOS failure taxonomy
- **Attention Science → Interface Design:** Attentional bottlenecks constrain information presentation

## 11. Knowledge Status

| Claim | Class | Status | Falsifiers |
|-------|-------|--------|------------|
| Working memory capacity is 4±1 chunks | VERIFIED | Empirically established (Cowan 2001) | Systematic failure of chunking experiments |
| Cognitive load exceeds capacity degrades performance | VERIFIED | Well-established (Sweller 1988+) | Performance improvement under overload |
| Distributed cognition describes real cognitive systems | DERIVED | Supported by ethnographic studies (Hutchins 1995) | Cognition proven to be always individual |
| Affordances exist independent of perception | MODEL | Theoretical claim (Gibson 1979) | Affordances proven to require perception |
| BCI cognitive load can be measured via EEG | DERIVED | Supported by neuroscience literature | EEG theta/alpha uncorrelated with CL |

______________________________________________________________________

**MOC:** [[11_KNOWLEDGE/KNOWLEDGE_MOC|KNOWLEDGE_MOC]] · [[00_ROOT/00_HOME|00_HOME]]

**Related:** [[11_KNOWLEDGE/AMOS_C05_MIND_BEHAVIOR_MASTER_KNOWLEDGE|AMOS_C05_MIND_BEHAVIOR_MASTER_KNOWLEDGE]] · [[11_KNOWLEDGE/AMOS_C11_DESIGN_LANGUAGE_MASTER_KNOWLEDGE|AMOS_C11_DESIGN_LANGUAGE_MASTER_KNOWLEDGE]] · [[11_KNOWLEDGE/AMOS_C04_BIO_NEURO_MASTER_KNOWLEDGE|AMOS_C04_BIO_NEURO_MASTER_KNOWLEDGE]] · [[15_INTERFACES/BCI_EXPRESSION_GATEWAY_ADAPTER|BCI_EXPRESSION_GATEWAY_ADAPTER]]
