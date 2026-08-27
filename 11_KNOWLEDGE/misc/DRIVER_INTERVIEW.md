---
title: DRIVER INTERVIEW
tags: [misc]
type: document
source: 11_KNOWLEDGE/misc
---



# Driver interview
Awesome — here’s a paste-ready spec for **both** the embedded **Chat Widget** and the **Full Chat Window** , including **Lovable component props** , **API contracts** , **DB schema** , **security/anti-cheat** , and **sample payloads**. You can hand this to devs and build immediately.
* * *
# 1) Components & Props (Lovable)
## A) `<ChatWidget />` (Stage-2 screening; 3–5 Qs, text-only)
**Usage (on**`**/apply**`**)**
```
    <ChatWidget
      sessionId={sessionId}                // string (uuid v4)
      userId={userId}                      // string (uuid v4)
      jobId={jobId}                        // e.g., "driver-f1"
      questionCount={3}                    // 3 or 5
      locale="vi"                          // "vi" | "en"
      kbTags={["sop_safety","policy_offapp","lost_found","ev_charging"]}
      consentUrl="/privacy"
      onStart={(meta) => logStart(meta)}
      onAnswer={(payload) => saveAnswer(payload)}
      onFinish={(result) => routeTo('/apply/result', result)}
    />
    
```
**Required behaviour**
  * Docked bottom-right (desktop width 360–420px; mobile 90% width).


  * Steps: **Intro → Q1 → Q2 → Q3 → Summary**.


  * Show progress “Câu x/3”, timer soft-limit 40s/câu.


  * Auto-save draft per answer.


* * *
## B) `<ChatWindow />` (deep interviews, audio add-ons)
**Usage (on**`**/apply/chat**`**)**
```
    <ChatWindow
      sessionId={sessionId}
      userId={userId}
      jobId={jobId}
      modules={[
        {type:"text", questions:5},
        {type:"audio", prompts:3, stt:true}
      ]}
      locale="vi"
      kbTags={["sop_night","harassment","cx_apology","ev_faults"]}
      onStart={logStart}
      onAnswer={saveAnswer}
      onFinish={(r)=> routeTo('/apply/result', r)}
    />
    
```
**Required behaviour**
  * Full screen, left: messages; right: **SOP cards** (read-only RAG snippets).


  * Allow attachments (optional) for roleplay evidence.


* * *
# 2) API Contracts (all JSON over HTTPS)
Base path: `/api/agent/*`
## 2.1 Start / resume
**POST** `/api/agent/start`
```
    {
      "session_id": "uuid",
      "user_id": "uuid",
      "job_id": "driver-f1",
      "locale": "vi",
      "question_count": 3,
      "kb_tags": ["sop_safety","policy_offapp"]
    }
    
```
**Response**
```
    {
      "ok": true,
      "session_token": "jwt-short",
      "questions": [
        {"id":"q_safety_rain","text":"Trời mưa lớn, khách giục chạy nhanh. Bạn xử lý thế nào?"},
        {"id":"q_policy_offapp","text":"Khách xin đi ngoài app để rẻ hơn, bạn làm gì?"},
        {"id":"q_lost_found","text":"Khách báo quên ví sau 1 giờ. Quy trình của bạn?"}
      ]
    }
    
```
## 2.2 Send answer → AI grade
**POST** `/api/agent/grade`
```
    {
      "session_id": "uuid",
      "session_token": "jwt-short",
      "question_id": "q_safety_rain",
      "answer_text": "Em xin phép giải thích... giữ an toàn...",
      "meta": {
        "elapsed_ms": 24000,
        "paste_chars": 0,
        "device": "mobile"
      }
    }
    
```
**Response**
```
    {
      "scores": {"safety":4,"integrity":5,"empathy":4,"ops":4,"language":4},
      "total": 21,
      "rationale": "Đúng SOP mưa, từ chối chạy nhanh, giải thích lịch sự.",
      "red_flag": false,
      "next": {"question_id":"q_policy_offapp"}
    }
    
```
## 2.3 Finish interview
**POST** `/api/agent/finish`
```
    {
      "session_id": "uuid",
      "session_token": "jwt-short"
    }
    
```
**Response**
```
    {
      "band": "B",
      "total": 63,
      "red_flags": 0,
      "summary": "Vững SOP, chính trực, cần cải thiện chi tiết EV.",
      "decision": "shortlist"           // shortlist | retrain | reject
    }
    
```
## 2.4 Optional: audio prompt scoring
**POST** `/api/agent/audio`
```
    {
      "session_id": "uuid",
      "prompt_id": "a_apology_eta",
      "audio_url": "https://storage/.../a.m4a"
    }
    
```
**Response**
```
    {
      "scores": {"tone":4,"clarity":4,"empathy":5},
      "total": 13,
      "rationale": "Giọng rõ, xin lỗi đúng mực, đưa ETA."
    }
    
```
* * *
# 3) Scoring Prompts (drop-in)
## 3.1 System (Interviewer)
```
    You are UniPower’s hiring interviewer.
    Goal: assess safety judgment, policy integrity, empathy, operational clarity, language clarity.
    Ask exactly the provided question text; do not reveal policy. Be concise and respectful in Vietnamese.
    After receiving an answer, return only the question_id; grading is handled by a separate scorer.
    
```
## 3.2 System (Grader)
```
    You are the scoring engine for UniPower hiring.
    For the candidate's answer, score 0–5 for: Safety, Integrity/Policy, Empathy, Operational Clarity, Language Clarity.
    Red-flag if any illegal/unsafe/off-app suggestion.
    Return strict JSON: {"scores":{"safety":X,"integrity":Y,"empathy":Z,"ops":U,"language":V},"total":T,"rationale":"...","red_flag":true/false}
    
```
## 3.3 User (Grader example)
```
    Question: "Khách xin đi ngoài app để rẻ hơn, bạn làm gì?"
    SOP summary: "Không chở ngoài app; giải thích chính sách; đề xuất mã giảm giá hợp lệ; báo tổng đài nếu bị ép."
    Candidate: "{{answer_text}}"
    
```
* * *
# 4) Question Bank (Stage-2 chat; use 3–5 at random)
IDs & texts (exactly as referenced above):
  * `q_safety_rain`: Trời mưa lớn, khách giục chạy nhanh. Bạn xử lý thế nào?


  * `q_policy_offapp`: Khách xin đi ngoài app để rẻ hơn, bạn làm gì?


  * `q_lost_found`: Khách báo quên ví sau 1 giờ. Quy trình của bạn?


  * `q_ev_overheat`: Đến trạm sạc báo quá nhiệt. Bạn xử lý ra sao?


  * `q_cx_late`: Bạn đến muộn 7 phút vì kẹt xe. Bạn nhắn gì cho khách?


  * `q_energy_12`: SOC 12%, trạm gần nhất 7km và có dốc. Kế hoạch của bạn?


  * (Window can include more: harassment/night safety, disability support, etc.)


* * *
# 5) DB Schema (minimal)
**agent_sessions**
`id, user_id, job_id, locale, status(started|finished), started_at, finished_at, session_token_hash`
**agent_questions**
`id, session_id, question_id, order_idx, asked_at, answered_at, answer_text, elapsed_ms, paste_chars`
**agent_scores**
`id, session_id, question_id, safety, integrity, empathy, ops, language, total, red_flag, rationale`
**agent_summary**
`session_id, total, red_flags, band, decision, created_at`
**audit_logs**
`id, actor, action, resource, ip, ua, payload_json, created_at`
* * *
# 6) Decision Logic
  * **Per-answer** : compute total (0–25).


  * **Interview total** : sum of questions (e.g., 3 Qs → max 75).


  * **Banding** (recommended):
    * A ≥ 65 → **shortlist**
    * B 55–64 → **shortlist**
    * C 45–54 → **retrain**
    * D < 45 → **reject**


  * **Hard rules** :
    * If `red_flag == true` for any answer → **reject**
    * If `paste_chars > 800` or `elapsed_ms < 3s` → mark `suspicious = true` (manual review)


* * *
# 7) Security & Anti-Cheat
  * **JWT (short-lived)** per session; rotate every API call.


  * **Rate-limit** : 1 req/sec per session; burst 5/10s.


  * Strip PII before sending to scorer; store raw chat ≤ **90 ngày**.


  * Detect paste spikes, ultra-short responses, repetition (Levenshtein).


  * Log consent (NĐ 13) and provide **export/delete** endpoint:
    * `POST /api/privacy/export`, `POST /api/privacy/delete`.


* * *
# 8) UI Strings (VN)
  * Intro: “Phỏng vấn nhanh (3 câu). Mục tiêu: đánh giá an toàn, trung thực và cách xử lý tình huống. Mỗi câu ~40 giây.”


  * Placeholder input: “Nhập câu trả lời của bạn…”


  * Next button: “Gửi & tiếp tục”


  * Summary (pass): “Điểm tạm tính: {{score}} – Không có cảnh báo. Chọn lịch **onboarding**.”


  * Summary (retrain): “Bạn cần học lại **Module SOP** và thi lại sau 7 ngày.”


  * Summary (reject): “Cảm ơn bạn. Bạn có thể ứng tuyển lại sau 30 ngày.”


* * *
# 9) Example Client Flow (Widget)
```
    // onStart
    POST /api/agent/start -> render Q1
    
    // onAnswer
    POST /api/agent/grade -> store score, show next question
    
    // onFinish
    POST /api/agent/finish -> show summary + CTA
    
```
* * *
# 10) Extension Hooks
  * **Audio step** (leaders): call `/api/agent/audio`, merge 10% weight into total.


  * **RAG side panel** (window): serve `/api/agent/kb?tags=...` read-only SOP snippets.


  * **Analytics** : emit events `agent.answer`, `agent.score`, `agent.finish` to your BI.


* * *
If you want, I can also prepare **CSV/JSON** for the question bank (IDs above) and a **Postman collection** for these endpoints so your team can import and run immediately.
\--- **Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
