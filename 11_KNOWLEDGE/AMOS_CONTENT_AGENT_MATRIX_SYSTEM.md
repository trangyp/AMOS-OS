---
artifact_id: AMOS-CONTENT-AGENT-MATRIX
name: amos-content-agent-matrix-system
title: "AMOS Content Agent Matrix — Governed Multi-Agent Content Operating System"
document_version: "3.0.0"
protocol_version: "2.0.0"
domain_model_version: "1.0.0"
amos_core_target: "v4.4"

created: "2026-08-22"
updated: "2026-08-25"

origin_architect: "Trang Phan"
steward: "Trang Phan"

canon-group: meta
canon-type: framework
canon-scope: content-agent-system

rscf-state: source-claim
rscf-class: "AMOS_MODEL / SOURCE_CLAIM"
source_status: "SOURCE_CLAIM"
validation_status: "REQUIRES_EMPIRICAL_VALIDATION"

topic: content-agent-matrix

aliases:
  - "Content Agent System"
  - "Content Matrix Agent"
  - "AMOS Content OS"
  - "AMOS Content Agency"
  - "30-Day Content Matrix"

tags:
  - agents
  - canon-group/tech-ai
  - canon/framework
  - canon/protocol
  - rscf/claim
  - rscf/provenance
  - rscf/state/source-claim
  - topic/content-agent
  - topic/content-matrix
  - topic/multi-agent
  - topic/content-marketing
  - topic/orchestration

governing_law: "integrity > completeness > fluency > speed > token savings"
---

# AMOS Content Agent Matrix
## Governed Multi-Agent Content Operating System

> **Document:** `v3.0.0`  
> **Protocol:** `v2.0.0`  
> **Domain Model:** `v1.0.0`  
> **AMOS_CORE target:** `v4.4`  
> **Origin architect / steward:** Trang Phan  
> **Primary source:** “HƯỚNG DẪN XÂY DỰNG HỆ THỐNG MA TRẬN CONTENT AGENT VỚI CLAUDE”  
> **Epistemic class:** `AMOS_MODEL / SOURCE_CLAIM`

---

# 0. PURPOSE

AMOS Content Agent Matrix chuyển mô hình content thủ công thành một **hệ điều hành nội dung có cấu trúc**.

Mục tiêu không chỉ là:

```text
generate posts
```

mà là:

```text
UNDERSTAND AUDIENCE
→ BUILD CONTENT STRATEGY
→ ALLOCATE CONTENT
→ GENERATE ASSETS
→ REVIEW
→ PUBLISH
→ OBSERVE
→ LEARN
→ REPLAN
```

Hệ thống kết hợp:

```text
CONTENT MATRIX
+
CUSTOMER JOURNEY
+
CONTENT PILLARS
+
MULTI-AGENT SPECIALIZATION
+
ORCHESTRATION
+
EVIDENCE
+
VALIDATION
+
LEARNING LOOP
```

---

# 1. SOURCE / MODEL / REALITY FIREWALL

Tài liệu nguồn cung cấp một kiến trúc content gồm:

```text
4 customer-journey stages
5 content groups
6 agents
6–8 content pillars
30-day planning matrix
weekly execution cycle
```

Các cấu trúc này được giữ nguyên dưới lớp:

```text
SOURCE_CLAIM
```

AMOS không tự động nâng các quy tắc như:

```text
30–40% Viral
20% Story
25% Education
10–15% Proof
8–10% Conversion
10 nurture → 1 sales
```

thành luật tối ưu phổ quát.

Phân lớp:

```text
SOURCE:
what the original content framework prescribes

AMOS_MODEL:
how the system is formalized and governed

OBSERVATION:
what analytics actually show

DECISION:
what strategy is selected for a specific channel/account
```

Hard invariant:

```text
PrescribedRatio
!=
EmpiricallyOptimalRatio
```

---

# 2. VERSION LINEAGE

```text
SOURCE GUIDE
    ↓
Content Matrix + Claude Agent Prompts
    ↓
v1.x — manual multi-role prompt system
    ↓
v2.x — structured multi-agent content workflow
    ↓
v3.0.0 — AMOS governed Content Agent Matrix OS
```

## 2.1 Version identity

```yaml
VERSION_ID:
  artifact: AMOS-CONTENT-AGENT-MATRIX
  document: 3.0.0
  protocol: 2.0.0
  domain_model: 1.0.0
  core_target: AMOS_CORE_4.4
```

## 2.2 Version invariant

```text
PromptVersion
!=
AgentVersion
!=
ContentStrategyVersion
!=
MatrixVersion
!=
PublishedContentVersion
```

---

# 3. CORE SYSTEM IDEA

Nguồn mô tả content như một chuỗi tâm lý 30 ngày.

AMOS giữ ý tưởng này dưới dạng:

```text
ContentProgram
=
Sequence(ContentUnit_t)
```

với:

[
C_{1:T}
=======

[C_1,C_2,\dots,C_T]
]

Trong đó mỗi content unit có:

```text
audience stage
content class
pillar
goal
message
proof state
CTA
channel
time
performance evidence
```

Một bài content không nhất thiết đứng độc lập.

Nó có thể tạo dependency với content trước và sau.

---

# 4. CUSTOMER JOURNEY MODEL

Nguồn định nghĩa 4 tầng:

```text
J1 — Awareness
J2 — Connection
J3 — Trust / Authority
J4 — Conversion
```

AMOS representation:

```text
UNKNOWN
↓
AWARE
↓
CONNECTED
↓
TRUSTING
↓
READY_TO_ACT
```

## 4.1 Journey tensor

```text
J[
  awareness,
  affinity,
  trust,
  intent
]
```

Mỗi dimension nằm trong:

[
[0,1]
]

nếu hệ thống dùng normalized scoring.

Đây là:

`AMOS_MODEL`

không phải trực tiếp là trạng thái tâm lý có thể quan sát hoàn hảo.

---

# 5. FOUR STAGES

## J1 — Awareness

Mục tiêu nguồn:

```text
views
followers
reach
attention
```

Content chính:

```text
Viral / Awareness
```

---

## J2 — Connection

Mục tiêu:

```text
empathy
recognition
affinity
```

Content:

```text
Story / Connection
```

---

## J3 — Trust / Authority

Mục tiêu:

```text
credibility
expertise
proof
trust
```

Content:

```text
Education
Proof
Case Study
```

---

## J4 — Conversion

Mục tiêu:

```text
lead
DM
download
booking
purchase
```

Content:

```text
Conversion / CTA
```

---

# 6. CONTENT CLASS MODEL

Nguồn định nghĩa 5 nhóm:

```text
C1 VIRAL_AWARENESS
C2 STORY_CONNECTION
C3 EDUCATION_AUTHORITY
C4 PROOF_CASE_STUDY
C5 CONVERSION_CTA
```

Canonical schema:

```yaml
ContentClass:
  class_id:
  name:
  primary_journey_stage:
  objective:
  required_evidence:
  CTA_type:
  risk_flags:
```

---

# 7. SOURCE ALLOCATION POLICY

Nguồn đề xuất:

| Class                 | Source allocation |
| --------------------- | ----------------: |
| Viral / Awareness     |            30–40% |
| Story / Connection    |               20% |
| Education / Authority |               25% |
| Proof / Case Study    |            10–15% |
| Conversion / CTA      |             8–10% |

Nguồn cũng đề xuất:

```text
10 nurture posts
→
1 conversion post
```

Class:

```text
SOURCE_CLAIM / STRATEGY_HEURISTIC
```

Không phải:

```text
UNIVERSAL_MARKETING_LAW
```

---

# 8. ALLOCATION CONSISTENCY CORRECTION

Khoảng tỷ lệ nguồn không tạo một allocation duy nhất.

Lower-bound total:

[
30+20+25+10+8=93%
]

Upper-bound total:

[
40+20+25+15+10=110%
]

Do đó cần explicit allocator.

Ví dụ với 30 content units:

```text
Viral       = 11
Story       = 6
Education   = 8
Proof       = 3
Conversion  = 2
```

Tổng:

[
11+6+8+3+2=30
]

Tỷ lệ:

```text
36.7%
20.0%
26.7%
10.0%
6.7%
```

Lưu ý:

`Conversion = 6.7%`

không nằm trong khoảng `8–10%`.

Vì vậy chính ví dụ nguồn và tỷ lệ nguồn không hoàn toàn tương thích.

AMOS không che mâu thuẫn này.

---

# 9. ALLOCATION ENGINE

Một allocator chính xác hơn:

[
n_k
===

\operatorname{round}
(
Nw_k
)
]

với:

[
\sum_k w_k=1
]

và:

[
\sum_k n_k=N
]

Canonical configuration:

```yaml
allocation:
  mode: normalized_weights

  weights:
    viral: 0.35
    story: 0.20
    education: 0.25
    proof: 0.12
    conversion: 0.08

  total_units: 30

  rounding:
    method: largest_remainder
```

Weights là:

```text
CONFIG
```

không phải canon law.

---

# 10. CONTENT PILLARS

Nguồn đề xuất:

```text
6–8 pillars
```

Pillar đóng vai trò semantic backbone.

```yaml
ContentPillar:
  pillar_id:
  title:
  audience_problem:
  desired_outcome:
  expertise_domain:
  journey_coverage:
  evidence_sources:
  prohibited_claims:
```

Hard invariant:

```text
EveryContentUnit
must map to
at least one declared pillar.
```

Cross-pillar content có thể tồn tại nhưng phải explicit.

---

# 11. CONTENT MATRIX

Canonical matrix:

| Field            | Meaning                                        |
| ---------------- | ---------------------------------------------- |
| Day              | thời điểm                                      |
| Content Class    | Viral / Story / Education / Proof / Conversion |
| Title / Hook     | creative hypothesis                            |
| Pillar           | semantic ownership                             |
| Journey Stage    | J1–J4                                          |
| Objective        | intended effect                                |
| CTA              | intended next action                           |
| Evidence         | claim support                                  |
| Personal Context | creator-specific material                      |
| Channel          | TikTok / Shorts / Reels / etc.                 |
| Status           | lifecycle                                      |
| Metrics          | post-publication evidence                      |

Nguồn chỉ yêu cầu 6 cột.

AMOS v3 mở rộng để hệ thống có thể học từ execution.

---

# 12. CONTENT UNIT OBJECT

```yaml
ContentUnit:
  content_id:
  matrix_version:

  schedule:
    day:
    publish_at:

  strategy:
    content_class:
    pillar:
    journey_stage:
    objective:

  creative:
    title:
    hook:
    script:
    CTA:
    visual_direction:
    caption:
    hashtags:

  evidence:
    claims: []
    source_refs: []
    proof_status:

  creator_overlay:
    personal_story:
    personal_experience:
    brand_voice:

  runtime:
    channel:
    status:
    published_url:

  metrics:
    views:
    watch_time:
    completion_rate:
    saves:
    shares:
    comments:
    follows:
    clicks:
    leads:
    sales:
```

---

# 13. CONTENT LIFECYCLE

```text
IDEA
↓
RESEARCHED
↓
PLANNED
↓
DRAFTED
↓
VISUALIZED
↓
REVIEWED
↓
APPROVED
↓
PUBLISHED
↓
MEASURED
↓
LEARNED
↓
ARCHIVED / REUSED
```

Invalid jump:

```text
IDEA
→
PUBLISHED
```

without applicable gates.

---

# 14. AGENT ARCHITECTURE

Nguồn định nghĩa 6 agents:

```text
A0 ORCHESTRATOR
A1 RESEARCH
A2 STRATEGY
A3 CONTENT
A4 VISUAL
A5 REVIEWER
```

AMOS mapping:

```text
A0 → ORCHESTRATOR
A1 → RESEARCHER
A2 → ANALYST / STRATEGIST
A3 → CONTENT SPECIALIST
A4 → DESIGNER
A5 → AUDITOR + VALIDATOR
```

---

# 15. A0 — ORCHESTRATOR

Vai trò:

```text
Objective
→ decomposition
→ routing
→ dependency control
→ synthesis
```

Orchestrator không phải agent “biết tất cả”.

Nó là:

```text
control / coordination role
```

## Contract

```yaml
Orchestrator:
  reads:
    - objective
    - content_strategy
    - matrix_state
    - agent_outputs

  writes:
    - task_assignments
    - workflow_state
    - final_package

  authority:
    may_route: true
    may_publish: false
    may_modify_source_evidence: false
```

---

# 16. A1 — RESEARCH AGENT

Nguồn yêu cầu:

```text
top viral content
view counts
pain points
trends
content ideas
weekly recommendations
```

AMOS hardening:

```text
CurrentMarketClaim
requires
CurrentEvidence
```

Nếu agent không có retrieval:

```text
views = UNKNOWN/GAP
trend = UNKNOWN/GAP
viral_rank = UNKNOWN/GAP
```

Không được tự sinh dữ liệu.

---

# 17. RESEARCH EVIDENCE OBJECT

```yaml
ResearchObservation:
  observation_id:
  platform:
  content_url:
  creator:
  observed_at:

  metrics:
    views:
    likes:
    comments:
    shares:

  interpretation:
    hook_pattern:
    format:
    topic:
    audience_signal:

  provenance:
    source:
    retrieval_method:
    freshness:
```

Hard rule:

```text
GeneratedIdea
!=
MarketObservation
```

---

# 18. A2 — STRATEGY AGENT

Strategy Agent biến evidence thành matrix.

```text
Research
+
Audience
+
Pillars
+
Objectives
+
Constraints
→
Content Matrix
```

Nó phải phân biệt:

```text
source rule
configured rule
data-derived recommendation
```

---

# 19. STRATEGY OBJECTIVE

Một generic strategy objective:

[
U
=

w_RR
+
w_EE
+
w_TT
+
w_CC
]

Trong đó:

* (R): reach;
* (E): engagement;
* (T): trust proxy;
* (C): conversion.

Weights phụ thuộc business objective.

Class:

`AMOS_MODEL`

---

# 20. A3 — CONTENT AGENT

Nguồn yêu cầu script 60–90 giây với:

```text
Hook
Body
CTA
Delivery notes
```

Canonical object:

```yaml
Script:
  hook:
  body:
  proof:
  transition:
  CTA:
  duration_target:
  tone:
  prohibited_claims:
```

Content Agent không được:

```text
fabricate personal experience
fabricate testimonials
fabricate medical evidence
fabricate business results
```

---

# 21. PERSONAL STORY FIREWALL

Nguồn khuyến nghị:

```text
"kể chuyện cá nhân"
"ví dụ thật"
```

AMOS distinction:

```text
CreatorSuppliedExperience
=
usable as first-person story

ModelGeneratedExperience
!=
creator's real experience
```

Do đó:

```text
AI must never invent first-person biography
and present it as creator truth.
```

---

# 22. A4 — VISUAL AGENT

Visual Agent tạo:

```text
thumbnail concepts
caption
hashtags
text overlay
visual direction
```

Canonical:

```yaml
VisualPackage:
  content_id:
  thumbnail_options: []
  overlay_text: []
  shot_list: []
  caption:
  hashtags: []
  platform_variant: {}
```

Visual recommendation là:

```text
DESIGN_PROPOSAL
```

không phải performance proof.

---

# 23. A5 — REVIEWER AGENT

Nguồn yêu cầu Reviewer kiểm tra:

```text
allocation
journey flow
voice
titles
scripts
errors
recommendations
```

AMOS nâng thành validation gate.

```yaml
ReviewResult:
  content_id:
  strategy_valid:
  voice_valid:
  evidence_valid:
  claim_valid:
  CTA_valid:
  platform_valid:
  duplication_valid:
  risk_valid:

  issues: []
  required_repairs: []

  decision:
    APPROVE
    CONDITIONAL
    REJECT
```

---

# 24. REVIEWER INDEPENDENCE

Reviewer nhận toàn bộ output từ agent trước.

Nhưng:

```text
ReviewerReadingSameGeneratedOutput
!=
IndependentExternalValidation
```

Reviewer có thể kiểm tra:

```text
consistency
logic
format
policy
known constraints
```

nhưng không biến source-less factual claims thành facts.

---

# 25. MULTI-AGENT PIPELINE

Source sequence:

```text
Research
→ Strategy
→ Content
→ Visual
→ Reviewer
```

AMOS adds Orchestrator and state:

```text
USER OBJECTIVE
↓
ORCHESTRATOR
↓
RESEARCH
↓
EVIDENCE GATE
↓
STRATEGY
↓
MATRIX VALIDATION
↓
CONTENT
↓
CLAIM VALIDATION
↓
VISUAL
↓
REVIEWER
↓
FINAL SYNTHESIS
↓
HUMAN APPROVAL / PUBLISH
```

---

# 26. ACTUAL ORCHESTRATION FIREWALL

Nguồn mô tả:

> Orchestrator tự động giao việc cho các Agent khác.

Nếu hệ thống chỉ sử dụng nhiều chat riêng biệt:

```text
separate chats
!=
automatic orchestration
```

Để gọi là runtime multi-agent:

```text
Orchestrated
=
WorkerCallable
∧ StateTransferExists
∧ TaskRoutingExists
∧ ResultReturnExists
∧ FailureHandlingExists
```

Nếu không:

```text
architecture_state = MANUAL_MULTI_ROLE_WORKFLOW
```

---

# 27. EXTERNALIZATION ARCHITECTURE

AMOS mapping:

| Burden                     | Artifact         |
| -------------------------- | ---------------- |
| audience profile           | MEMORY / STATE   |
| current campaign objective | CONTEXT          |
| content matrix             | PERSISTENT STATE |
| research methodology       | SKILL            |
| allocation algorithm       | CODE             |
| agent-to-agent contract    | PROTOCOL         |
| publishing integration     | TOOL             |
| publishing permission      | HARNESS POLICY   |

Hard rule:

```text
Prompt
should not carry
all persistent state.
```

---

# 28. STATE MODEL

```yaml
ContentSystemState:
  campaign_id:
  version:

  audience:
  offer:
  pillars:

  objectives:
  constraints:

  content_matrix:
  research_state:
  production_state:
  review_state:
  publication_state:
  analytics_state:

  decisions: []
  unresolved_gaps: []

  epoch:
  rollback_pointer:
```

---

# 29. H / M / L MODEL

```text
H — Campaign / business level
    audience
    positioning
    objective
    offer
    channel strategy

M — Content system
    journey
    pillars
    classes
    matrix
    agents
    workflows

L — Content artifacts
    title
    hook
    script
    thumbnail
    caption
    hashtags
    metrics
```

Invariant:

```text
L-level viral performance
does not automatically prove
H-level business success.
```

---

# 30. CONTENT CLAIM PROVENANCE

Every factual content claim should support:

```yaml
Claim:
  claim_id:
  text:
  type:
  source:
  source_date:
  freshness:
  confidence:
  scope:
```

Especially for:

```text
health
finance
legal
scientific
statistical
market
product-performance
```

claims.

---

# 31. PROOF / CASE STUDY FIREWALL

Nguồn khuyến nghị sử dụng:

```text
before/after
student
real result
```

AMOS hard constraint:

```text
ProofContent
requires
Proof
```

Không được generate:

```text
fake testimonial
fake before/after
fake customer outcome
fake revenue
fake health outcome
```

---

# 32. HEALTH CONTENT GUARD

Nguồn sử dụng giảm cân/sức khỏe làm ví dụ.

Health-content claims cần:

```text
medical evidence
appropriate uncertainty
no diagnosis
no invented mechanism
no guaranteed result
```

Hard rule:

```text
EducationContent
!=
MedicalAdvice
```

---

# 33. RESEARCH → STRATEGY TRANSACTION

```yaml
ResearchBundle:
  research_id:
  period:
  audience:
  evidence: []
  trends: []
  pain_points: []
  content_patterns: []
  uncertainty: []
```

Strategy Agent chỉ được dùng:

```text
validated / admitted ResearchBundle
```

Không dùng invisible assumptions như facts.

---

# 34. STRATEGY → CONTENT CONTRACT

```yaml
ContentBrief:
  content_id:
  pillar:
  content_class:
  journey_stage:
  audience_problem:
  key_message:
  intended_emotion:
  evidence:
  CTA:
  constraints:
```

Content Agent không được tự thay strategy nếu không explicit.

---

# 35. CONTENT → VISUAL CONTRACT

```yaml
VisualBrief:
  content_id:
  hook:
  dominant_message:
  emotional_tone:
  CTA:
  script:
  required_visual_elements:
  prohibited_elements:
```

---

# 36. REVIEW CONTRACT

Reviewer nhận:

```text
ResearchBundle
ContentMatrix
ContentBrief
Script
VisualPackage
```

không chỉ output cuối cùng.

Điều này cho phép kiểm tra lineage.

---

# 37. WEEKLY OPERATING CYCLE

Nguồn đề xuất:

```text
Sunday:
plan

Mon–Fri:
refine + batch production

Saturday:
publish
```

AMOS treats this as:

```text
CONFIGURED_WORKFLOW
```

không phải universal optimal cadence.

Canonical cycle:

```text
OBSERVE
↓
RESEARCH
↓
PLAN
↓
PRODUCE
↓
REVIEW
↓
PUBLISH
↓
MEASURE
↓
LEARN
↓
NEXT CYCLE
```

---

# 38. CLOSED LEARNING LOOP

Nguồn chủ yếu dừng ở generation.

AMOS bổ sung feedback:

[
Strategy_{t+1}
==============

Update
(
Strategy_t,
Performance_t
)
]

Nhưng update phải controlled.

```text
HighViews
does not automatically imply
RepeatEverything
```

---

# 39. ANALYTICS TENSOR

```text
M[
  reach,
  views,
  watch_time,
  completion,
  engagement,
  saves,
  shares,
  follows,
  profile_visits,
  clicks,
  leads,
  conversions,
  revenue
]
```

Không compress sớm thành một score duy nhất nếu decision cần phân biệt metrics.

---

# 40. FUNNEL METRICS

Example:

[
CTR
===

\frac{Clicks}{Impressions}
]

[
CVR
===

\frac{Conversions}{QualifiedVisits}
]

[
FollowRate
==========

\frac{NewFollowers}{Views}
]

[
ShareRate
=========

\frac{Shares}{Views}
]

Định nghĩa denominator phải explicit.

---

# 41. VIRALITY FIREWALL

```text
HighViews
!=
HighBusinessValue
```

và:

```text
Virality
!=
Authority
```

và:

```text
Engagement
!=
Conversion
```

AMOS phải giữ metrics tách biệt.

---

# 42. CONTENT MATRIX PERFORMANCE

Matrix performance có thể model:

[
P(M)
====

f(
Reach,
Retention,
Trust,
Conversion
)
]

Nhưng:

```text
f
```

phải được định nghĩa theo business objective.

Không có một universal content score.

---

# 43. ADAPTIVE ALLOCATION

Thay vì cố định tỷ lệ mãi mãi:

[
w_{k,t+1}
=========

w_{k,t}
+
\eta
\Delta_{k,t}
]

trong đó:

* (w_{k,t}): allocation weight;
* (\Delta_{k,t}): validated performance signal;
* (\eta): learning rate.

Class:

`AMOS_MODEL`

Constraints:

[
\sum_kw_k=1
]

và:

[
w_k\ge0
]

---

# 44. EXPLORATION / EXPLOITATION

Content engine cần cân bằng:

```text
EXPLOIT
=
repeat proven formats

EXPLORE
=
test new formats
```

Model:

[
Budget
======

B_{exploit}
+
B_{explore}
]

Không nên tối ưu chỉ bằng past winners vì:

```text
platform regime changes
audience fatigue
creative saturation
```

---

# 45. CONTENT FATIGUE

Nếu cùng hook / format lặp lại:

```text
performance decay
may emerge
```

Track:

```yaml
CreativeFatigue:
  format_id:
  recent_frequency:
  performance_trend:
  audience_overlap:
  status:
```

---

# 46. NOVELTY

Novelty không đồng nghĩa quality.

```text
Novel
!=
Useful
```

Strategy Agent nên tối ưu:

```text
relevance
+
distinctiveness
+
evidence
+
fit
```

---

# 47. PLATFORM REGIME

TikTok, YouTube Shorts, Instagram Reels và Facebook Reels không phải cùng một hệ.

```yaml
PlatformContext:
  platform:
  format:
  audience:
  algorithm_regime:
  length:
  CTA_constraints:
  metadata:
  freshness:
```

Cross-platform transfer phải là:

```text
CONDITIONAL
```

---

# 48. CONTENT LOCALIZATION

Nguồn ưu tiên thị trường Việt Nam.

Do đó:

```text
VietnamMarketObservation
```

không được generalize thành:

```text
GlobalMarketTruth
```

Language, platform usage, cultural reference, pricing, health beliefs và conversion behavior có thể khác.

---

# 49. HUMAN CREATOR BOUNDARY

Agent system hỗ trợ creator.

Nó không nên thay creator trong:

```text
personal truth
lived experience
brand values
ethical boundaries
final endorsement
```

Canonical relation:

```text
AI proposes
Human owns identity
Human approves publication
```

---

# 50. AUTHORITY MODEL

```yaml
Authority:
  orchestrator:
    may_route: true
    may_publish: false

  research:
    may_observe: true
    may_invent_market_data: false

  strategy:
    may_propose_matrix: true
    may_change_business_objective: false

  content:
    may_draft: true
    may_invent_testimonial: false

  visual:
    may_design: true
    may_publish: false

  reviewer:
    may_approve_draft: true
    may_override_creator_truth: false

  human:
    may_final_approve: true
```

---

# 51. INFORMATION BOUNDARY

Sensitive creator information should be minimized.

```text
CreatorPersonalData
only enters
content generation
when explicitly relevant.
```

Memory should not accumulate private information without need.

---

# 52. FAILURE REGISTRY

```text
F01 FAKE_MARKET_RESEARCH
F02 STALE_TREND_DATA
F03 CONTENT_RATIO_OVERFITTING
F04 JOURNEY_STAGE_MISMATCH
F05 PILLAR_DRIFT
F06 INVENTED_PERSONAL_STORY
F07 FABRICATED_TESTIMONIAL
F08 UNSUPPORTED_HEALTH_CLAIM
F09 CTA_OVERLOAD
F10 AGENT_HANDOFF_LOSS
F11 ORCHESTRATOR_STATE_DRIFT
F12 REVIEWER_SELF_CONFIRMATION
F13 CROSS_PLATFORM_SCOPE_LEAK
F14 METRIC_GOODHARTING
F15 CONTENT_FATIGUE
F16 DUPLICATE_IDEA_LOOP
F17 PUBLISH_WITHOUT_APPROVAL
F18 ANALYTICS_WITHOUT_DENOMINATOR
F19 SOURCE_CORRELATION
F20 AUTOMATION_WITHOUT_AUTHORITY
```

---

# 53. FAILURE RECOVERY

```text
Failure
↓
Locate failed artifact
↓
Identify dependent content
↓
Quarantine affected units
↓
Preserve unaffected units
↓
Repair
↓
Re-review
↓
Republish only if needed
```

Example:

```text
bad health claim
```

should invalidate:

```text
affected script
caption
visual claim
derived posts
```

not the entire campaign.

---

# 54. SELECTIVE INVALIDATION

[
Invalid(p)
\Rightarrow
Invalid(Descendants(p))
]

Example:

```text
ResearchObservation R17 falsified
↓
invalidate content ideas dependent on R17
↓
recompute only affected strategy units
```

---

# 55. LOOP DETECTION

Content system can enter repetition loops:

```text
same pain point
same title
same hook
same visual
same CTA
```

A fingerprint can be:

```text
F(content)
=
hash(
pillar,
content_class,
hook_pattern,
message,
CTA
)
```

Repeated high-similarity fingerprints should trigger novelty review.

---

# 56. CONTENT PROVENANCE GRAPH

```text
Research Source
      ↓
Research Observation
      ↓
Strategy Hypothesis
      ↓
Content Brief
      ↓
Script
      ↓
Visual Package
      ↓
Review
      ↓
Published Content
      ↓
Performance Evidence
```

This is preferable to isolated prompts.

---

# 57. RSCF — CONTENT ALLOCATION

```yaml
claim_id: CONTENT-MATRIX-ALLOC-001

claim: >
  A balanced campaign may benefit from distributing content across
  awareness, connection, authority, proof, and conversion functions.

class: AMOS_MODEL

source_claim:
  viral: 30-40%
  story: 20%
  education: 25%
  proof: 10-15%
  conversion: 8-10%

competing:
  - equal allocation
  - audience-stage-dependent allocation
  - performance-adaptive allocation
  - launch-period-specific allocation
  - platform-specific allocation

falsifiers:
  - controlled data shows persistent underperformance
  - allocation fails to fit campaign objective
  - platform regime changes invalidate historical assumptions

confidence_ceiling:
  structural_categories: medium-high
  exact_ratios: source-bounded
```

---

# 58. RSCF — MULTI-AGENT CLAIM

```yaml
claim_id: CONTENT-MULTIAGENT-001

claim: >
  Separating research, strategy, content creation, visual design,
  review, and orchestration can improve modularity and auditability.

class: AMOS_MODEL

does_not_establish:
  - six agents are always better than one
  - multi-agent output is automatically more accurate
  - prompt-separated chats constitute automated orchestration

competing:
  - single-agent structured workflow
  - three-agent compressed workflow
  - human-led hybrid workflow
  - deterministic pipeline with one model

falsifier:
  - controlled evaluation shows equal or superior results with
    materially lower orchestration complexity
```

---

# 59. RSCF — RESEARCH CLAIM

```yaml
claim_id: CONTENT-RESEARCH-001

claim: >
  Current platform trends and viral-content observations can inform
  weekly content planning.

class: CONDITIONAL

requires:
  - real market observation
  - source provenance
  - freshness
  - platform scope

invalid_if:
  - data is fabricated
  - data is stale
  - platform/context mismatch exists
```

---

# 60. RSCF — CUSTOMER JOURNEY

```yaml
claim_id: CONTENT-JOURNEY-001

claim: >
  Content can be organized according to awareness, connection,
  trust, and conversion objectives.

class: STRUCTURAL_MODEL

status: AMOS_MODEL

does_not_establish:
  - users always move linearly
  - every user passes every stage
  - one content unit affects only one stage
```

---

# 61. NON-LINEAR JOURNEY CORRECTION

Nguồn mô tả journey tương đối tuyến tính.

AMOS correction:

```text
UserJourney
may be
non-linear
```

Possible transitions:

```text
Aware → Convert
Trust → Disconnect
Convert → Trust
Connected → Ignore
```

Do đó:

[
P(J_{t+1}|J_t,C_t)
]

là probabilistic, không deterministic.

---

# 62. CONTENT MATRIX AS POLICY

Matrix không phải truth.

Nó là:

```text
planned content policy
```

State transition:

```text
PLAN
→ EXECUTE
→ OBSERVE
→ UPDATE
```

---

# 63. WEEKLY POLICY UPDATE

```yaml
WeeklyReview:
  planned_units:
  published_units:
  performance:
  winners:
  failures:
  anomalies:
  audience_signals:
  strategy_changes:
  next_experiments:
```

---

# 64. EXPERIMENT REGISTRY

```yaml
Experiment:
  experiment_id:
  hypothesis:
  variable:
  control:
  treatment:
  metric:
  duration:
  result:
  confidence:
  decision:
```

Examples:

```text
hook format
video length
CTA
thumbnail
content class
posting time
pillar
```

---

# 65. GOODHART FIREWALL

Nếu hệ thống tối ưu:

```text
views only
```

nó có thể sinh:

```text
clickbait
low trust
low conversion
audience mismatch
```

Do đó:

```text
Metric
must match
Objective
```

---

# 66. CONTENT QUALITY TENSOR

```text
Q[
  relevance,
  clarity,
  originality,
  evidence,
  emotional_fit,
  brand_fit,
  CTA_fit,
  platform_fit
]
```

Không nhất thiết compress thành một scalar.

---

# 67. REVIEW SCORE

Nếu cần scalar:

[
Q_{total}
=========

\sum_iw_iQ_i
]

với:

[
\sum_iw_i=1
]

Weights phải config/calibrated.

---

# 68. AUTOPUBLISH GOVERNANCE

Nguồn đề xuất:

```text
Make.com / Zapier
→ automated posting
```

AMOS hardening:

```text
Generated
!=
AuthorizedToPublish
```

Autopublish requires:

```text
review pass
approval
correct account
correct schedule
policy compliance
credential protection
rollback/correction path
```

---

# 69. AUTOPUBLISH STATE MACHINE

```text
DRAFT
↓
REVIEWED
↓
APPROVED
↓
QUEUED
↓
PUBLISHED
↓
VERIFIED
```

Invalid:

```text
GENERATED
→
PUBLISHED
```

unless user explicitly configures such authority and risk is acceptable.

---

# 70. 30-DAY MATRIX GENERATION CONTRACT

Inputs:

```yaml
MatrixRequest:
  campaign_id:
  niche:
  audience:
  offer:
  pillars:
  duration_days:
  channels:
  objectives:
  allocation_policy:
  evidence_bundle:
  creator_constraints:
```

Outputs:

```yaml
MatrixResult:
  version:
  allocation_summary:
  journey_summary:
  units: []
  unresolved_gaps: []
  assumptions: []
  experiments: []
```

---

# 71. VALIDATION GATES

Before matrix approval:

```text
V1 PillarCoverage
V2 JourneyCoverage
V3 AllocationConsistency
V4 ClaimEvidence
V5 NoDuplicateContent
V6 BrandVoice
V7 CTAConsistency
V8 Health/Legal/FinancialSafety if applicable
V9 PlatformFit
V10 CreatorTruth
```

---

# 72. AGENT HANDOFF CONTRACT

Every handoff should include:

```yaml
Handoff:
  from:
  to:
  task_id:
  objective:
  inputs:
  assumptions:
  evidence:
  constraints:
  expected_output:
  unresolved_gaps:
```

This prevents context loss.

---

# 73. ORCHESTRATOR STATE

```yaml
OrchestratorState:
  cycle_id:
  current_phase:
  current_agent:
  completed_agents: []
  pending_agents: []
  failed_agents: []
  artifacts: []
  unresolved_gaps: []
  retry_count:
```

---

# 74. RETRY RULE

```text
Retry
only if
failure condition changed
or
new evidence exists.
```

Không retry vô hạn cùng prompt.

---

# 75. MODEL / TOOL SEPARATION

```text
LLM
=
reasoning / generation

Search
=
external evidence acquisition

Analytics API
=
performance observation

Scheduler
=
execution tool

Automation platform
=
orchestration / effect layer
```

Một LLM không tự có access chỉ vì prompt yêu cầu.

---

# 76. CONTENT AGENT SYSTEM — AMOS STACK

```text
HUMAN / CREATOR
        ↓
AMOS CONTENT CONTROL PLANE
        ↓
ORCHESTRATOR
   ┌────┼────┬────┬────┐
   ↓    ↓    ↓    ↓    ↓
RESEARCH STRATEGY CONTENT VISUAL REVIEWER
   │      │       │      │      │
   └──────┴───────┴──────┴──────┘
                 ↓
         CONTENT STATE GRAPH
                 ↓
         HUMAN APPROVAL GATE
                 ↓
            PUBLISH TOOL
                 ↓
             ANALYTICS
                 ↓
          LEARNING / UPDATE
```

---

# 77. MINIMUM VIABLE CONFIGURATION

Một version nhỏ hơn có thể là:

```text
Orchestrator
+
Research/Strategy
+
Content/Visual
+
Reviewer
```

Do đó:

```text
6 agents
```

không phải irreducible requirement.

Agent count nên tối ưu theo:

```text
quality
coordination cost
context cost
latency
maintainability
```

---

# 78. ORCHESTRATION COST

Generic model:

[
Cost_{total}
============

Cost_{generation}
+
Cost_{handoff}
+
Cost_{validation}
+
Cost_{retry}
]

Multi-agent chỉ có lợi khi:

[
Value_{quality}

>

Cost_{coordination}
]

Class:

`AMOS_MODEL`

---

# 79. COMPLETION MODEL

```text
ContentCycleComplete
=
ResearchComplete
∧ StrategyComplete
∧ ContentComplete
∧ VisualComplete
∧ ReviewComplete
∧ ApprovalComplete
```

Published cycle:

```text
PublishedCycleComplete
=
ContentCycleComplete
∧ PublishComplete
∧ PublicationVerified
```

Learning cycle:

```text
LearningCycleComplete
=
PublishedCycleComplete
∧ MetricsObserved
∧ ReviewPerformed
∧ StrategyUpdated
```

---

# 80. COMPLETION != SUCCESS

```text
CycleCompleted
!=
CampaignSucceeded
```

Campaign success requires outcomes relative to explicit objective.

---

# 81. PRODUCTION-READINESS GATE

```text
ProductionReady
=
AgentContractsValid
∧ HandoffsValid
∧ EvidenceRetrievalValid
∧ StatePersistenceValid
∧ ReviewGateValid
∧ PublishAuthorityValid
∧ ToolIntegrationValid
∧ ErrorRecoveryValid
∧ AnalyticsValid
```

Without executed evidence:

```text
ProductionReady = UNKNOWN/GAP
```

---

# 82. SOURCE PROMPT STATUS

Các 6 prompts trong source nên được giữ như:

```text
PROMPT_BASELINE_V1
```

không nên coi là runtime protocol final.

V3 nên chuyển:

```text
repeated prose rules
```

thành:

```text
shared configuration
+
typed state
+
agent contracts
+
validators
```

---

# 83. SHARED CONFIGURATION

```yaml
ContentSystemConfig:
  language: vi
  niche:
  audience:
  pillars: []

  journey:
    stages:
      - awareness
      - connection
      - trust
      - conversion

  classes:
    - viral
    - story
    - education
    - proof
    - conversion

  allocation:
    weights: {}

  voice:
    characteristics:
      - natural
      - clear
      - authentic

  creator:
    facts: []
    experiences: []

  safety:
    fabricated_testimonials: deny
    fabricated_experience: deny
```

Agents reference config instead of duplicating the entire ruleset.

---

# 84. DRIFT PREVENTION

Duplicating rules into six prompts creates:

```text
PromptDriftRisk
```

Ví dụ một agent thay tỷ lệ, agent khác dùng tỷ lệ cũ.

V3 solution:

```text
ONE SHARED CONFIG
+
ROLE-SPECIFIC SKILL
```

---

# 85. SINGLE SOURCE OF TRUTH

```text
ContentRules
should have
one authoritative version.
```

Agent prompts chỉ reference.

Không copy-paste nhiều versions nếu system có shared state.

---

# 86. CONTENT MEMORY

Persistent memory nên lưu:

```text
approved pillars
brand voice
past experiments
published content
performance summaries
rejected patterns
creator-approved facts
```

Không nên lưu blindly:

```text
all generated drafts
all trend guesses
all unverified observations
```

---

# 87. NEGATIVE MEMORY

Store failures such as:

```yaml
NegativePattern:
  pattern:
  reason:
  evidence:
  date:
  applicable_scope:
  expires:
```

Ví dụ:

```text
hook format overused
CTA caused dropoff
unsupported claim rejected
```

---

# 88. FRESHNESS

Trend research nhanh stale.

```yaml
Freshness:
  trend_observation:
    ttl: short

  evergreen_audience_problem:
    ttl: longer

  creator_identity:
    ttl: persistent_until_changed
```

No one TTL fits all data.

---

# 89. PROVENANCE TOPOLOGY

Nếu 10 articles copy cùng một viral claim từ một original source:

```text
10 URLs
!=
10 independent sources
```

Research Agent nên track ancestry khi material.

---

# 90. RSCF MASTER NODE

```yaml
node_id: AMOS_CONTENT_AGENT_MATRIX_V3

node_type: domain_agent_architecture

domain: CONTENT_MARKETING_AUTOMATION

origin_architect: Trang Phan
steward: Trang Phan

document_version: 3.0.0
protocol_version: 2.0.0
domain_model_version: 1.0.0
core_target: AMOS_CORE_4.4

claim: >
  A content-production workflow can be represented as a governed
  multi-role system combining research, strategy, content generation,
  visual design, review, orchestration, publication, and feedback.

class: AMOS_MODEL

source_elements:
  - four-stage customer journey
  - five content classes
  - 30-day matrix
  - six agent roles
  - weekly operating cycle
  - source allocation heuristics

derived_extensions:
  - typed agent contracts
  - state graph
  - provenance
  - evidence gates
  - adaptive allocation
  - publication governance
  - analytics feedback
  - selective invalidation
  - failure recovery

competing_architectures:
  - single-agent structured workflow
  - three-agent workflow
  - deterministic content pipeline
  - human-led workflow

falsifiers:
  - multi-agent coordination degrades quality
  - agent specialization produces no measurable advantage
  - content allocation heuristics consistently underperform alternatives
  - handoff cost dominates workflow benefit

confidence_ceiling:
  source_architecture: high
  universal_optimality: not_claimed
  exact_content_ratios: source_bounded
  runtime_effectiveness: implementation_dependent
```

---

# 91. CHANGELOG

## v3.0.0 — 2026-08-25

### MAJOR

* converted exported HTML source into governed Markdown architecture;
* preserved the original four-stage customer journey;
* preserved the original five content classes;
* preserved the six original agent roles;
* preserved the 30-day content-matrix concept;
* preserved the weekly operating cycle;
* classified source content ratios as strategy heuristics rather than universal laws;
* detected inconsistency between percentage ranges and one 30-post example;
* added deterministic allocation requirements;
* mapped agents into AMOS functional templates;
* separated manual multi-chat workflows from true runtime orchestration;
* added Research evidence/provenance requirements;
* added prohibition against fabricated trend metrics;
* added creator-truth firewall;
* added testimonial/proof firewall;
* added health-content safeguards;
* added typed agent handoff contracts;
* added campaign state;
* added content lifecycle;
* added provenance graph;
* added review and approval gates;
* added publishing authority;
* added closed analytics feedback;
* added adaptive allocation;
* added exploration/exploitation;
* added content fatigue monitoring;
* added platform-regime boundaries;
* added non-linear customer journey correction;
* added negative memory;
* added freshness semantics;
* added selective invalidation;
* added failure recovery;
* added orchestration-cost model;
* added production-readiness gates;
* replaced repeated prompt rules with shared configuration architecture;
* introduced single-source-of-truth rules to prevent prompt drift.

## v1.x / Source Guide

Preserved source concepts:

```text
30-day psychological content sequence
4 customer journey stages
5 content groups
6–8 pillars
weekly matrix design
six Claude agent roles
Research → Strategy → Content → Visual → Reviewer
Orchestrator coordination
manual Claude.ai project setup
Make.com / Zapier future automation
```

---

# 92. FINAL AMOS POSITION

The source framework's strongest idea is not the exact content percentage.

It is the decomposition:

```text
AUDIENCE
↓
JOURNEY
↓
CONTENT FUNCTION
↓
PILLAR
↓
CONTENT MATRIX
↓
SPECIALIST WORKERS
↓
REVIEW
↓
PUBLICATION
```

AMOS extends this into:

```text
AUDIENCE
↓
EVIDENCE
↓
STRATEGY
↓
MATRIX
↓
AGENT EXECUTION
↓
PROVENANCE
↓
VALIDATION
↓
HUMAN AUTHORITY
↓
PUBLICATION
↓
OBSERVATION
↓
LEARNING
↓
NEXT STRATEGY
```

The central rule becomes:

> **Content is not a queue of generated posts. It is a versioned decision system whose research, strategy, creation, proof, publication, performance, and learning state remain traceable across the full campaign lifecycle.**

The second rule is:

> **An agent role is not equivalent to autonomous orchestration; runtime capability must be demonstrated through actual task routing, state transfer, execution, validation, and failure handling.**

The third rule is:

> **Content heuristics are starting policies. Real analytics determine whether they survive, adapt, or are rejected.**

---

**Related:** [[00_ROOT/00-Home]] · 06-Knowledge-Base-MOC · AMOS_AGENT_SCHEMA_FULL · AMOS_AGENT_TEMPLATES · AMOS_AGENT_ONBOARDING_GUIDE · system_scan_agent · automation_profiles

```

:contentReference[oaicite:0]{index=0}
```

---

[[00_ROOT/00_ROOT_MOC.md|AMOS MOC]]

---
**Related:** [[00_ROOT/00-Home]] · [[AMOS_RSCF_NODES]]

---
RSCF-NODE
node_id: amos_content_agent_matrix_system
node_type: note
path: 11_KNOWLEDGE/AMOS_CONTENT_AGENT_MATRIX_SYSTEM.md
RSCF-RELATIONS:
  - INDEXED_BY: [[00_ROOT/00-Home]]
  - INDEXED_BY: [[AMOS_RSCF_NODES]]
claim_class: AMOS_MODEL
