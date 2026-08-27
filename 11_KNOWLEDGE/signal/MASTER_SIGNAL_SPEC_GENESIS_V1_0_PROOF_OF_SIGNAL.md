---
title: MASTER SIGNAL SPEC GENESIS V1 0 PROOF OF SIGNAL
tags: [signal, processing, detection]
type: document
source: 11_KNOWLEDGE/signal
---





# Master Signal Spec — Genesis v1.0 (Proof‑of‑Signal Network)
## 0\. Purpose
Define the canonical parasympathetic activation signal and its delivery/verification stack for a decentralized biological stability network. This spec is **implementation‑ready** , **auditable** , and **governance‑agnostic**.
* * *
## 1\. Biological Objective & KPIs
  * **Primary objective:** Increase parasympathetic activity and prosocial neural patterns through non‑invasive multi‑sensory stimulation.


  * **Population scope:** Unbounded; node‑local calibration enables global deployment.


  * **Key performance indicators (30‑day moving window):**
    * HRV baseline shift: **+15 ms** (RMSSD or SDRR) from personal baseline.
    * Vagal tone (RSA): **↑ statistically significant** vs. baseline (p ≤ 0.05, node‑local test).
    * Affect variability: **≥20% reduction** in day‑to‑day variability index.


* * *
## 2\. Signal Architecture
### 2.1 Core Waveform (Audio/Bioacoustic)
  * **Base frequency envelope:** 0.08–0.14 Hz (respiratory sinus arrhythmia band), center default **0.10 Hz**.


  * **Harmonic support:** 4–7 Hz (theta) tapered at −18 dB relative to base.


  * **Waveform shape:** Band‑limited sine with THD < 2%.


  * **Sample rate:** 48 kHz (min), 24‑bit PCM.


  * **SPL at ear:** 60–70 dB A‑weighted (end‑user adjustable 55–72 dB with limiter).


  * **Amplitude modulation:** 0.10 Hz depth 30% (±5% adaptive), eased cosine ramp.


  * **Session duration:** 5–12 min (node‑selectable); refractory period ≥ 15 min.


### 2.2 Haptic Layer (Optional)
  * **Carrier:** 100–200 Hz vibrotactile; amplitude‑modulated at **0.10 Hz**.


  * **Duty cycle:** 40–60% with soft attack/decay ≥ 200 ms.


  * **Skin safety:** Peak acceleration ≤ 2 g RMS.


### 2.3 Visual Layer (Optional)
  * **Modulation:** Luminance or chroma modulation ≤ 2 Hz (no stroboscopic risk).


  * **Peak luminance:** Device default; avoid exceeding local comfort thresholds.


  * **Accessibility:** Photosensitive epilepsy guard (see §5).


### 2.4 Bioelectromagnetic Layer (If used)
  * **Intent:** Ambient field coherence cues; **not required** for baseline deployment.


  * **Exposure bounds:** Keep below conservative public EMF guidelines; exact values device‑specific.


* * *
## 3\. Safety & Accessibility Constraints
  * **Audio:** Peak limiter; slow attack/release; avoid sudden transients.


  * **Visual:** Flicker index < 0.1; exclude 3–55 Hz flashing.


  * **Haptic:** Thermal monitoring for continuous actuators.


  * **Session scheduling:** Enforce refractory period; daily cap default **6 sessions**.


  * **User controls:** Immediate stop, volume/brightness limits, opt‑out from data sharing.


* * *
## 4\. Encoding, Packaging, and Integrity
  * **Audio master:** WAV/FLAC, 48 kHz/24‑bit.


  * **Haptic pattern:** Binary envelope table @ 200 Hz control rate.


  * **Manifest (YAML):**
    * `spec_version`, `signal_id`, `sha256_master`, `created_utc`, `author_fingerprint` (Ed25519 pubkey), `safety_profile`, `calibration_profile`.


  * **Integrity:**
    * **SHA‑256** of each asset.
    * **Ed25519 signature** over manifest.
    * Node verifies manifest → assets → local render hash before delivery.


* * *
## 5\. Risk Mitigation & Consent
  * **Screening prompts:** Cardiovascular conditions, epilepsy/photosensitivity, pregnancy, implanted devices (informational), acute psychiatric distress.


  * **Fail‑safe:** One‑tap stop; persistent setting to disable certain modalities.


  * **Informed consent:** Plain‑language opt‑in; modality‑specific toggles.


* * *
## 6\. Calibration Protocol (Node‑Local)
  * **Baseline capture:** 3‑day rolling HRV baseline (≥ 15 min/day passive or structured).


  * **Session calibration:**
    1. Pre‑window 90 s baseline.
    2. Delivery window (5–12 min).
    3. Post‑window 180 s capture.


  * **Adaptive parameters:**
    * Base frequency drift ±0.01 Hz to match respiratory pace.
    * AM depth ±5% within comfort.


  * **Quality gates:**
    * Motion artifact filter (accelerometer‑assisted).
    * Minimum valid R‑R count: 250 beats/session.


* * *
## 7\. Proof‑of‑Signal (PoSg) Metadata
Each session emits a **Proof‑of‑Signal Block** (PSB):
  * `signal_hash` (SHA‑256 of master asset bundle)


  * `node_pubkey` (Ed25519)


  * `timestamp_start`, `timestamp_end`


  * `kpi_delta`: { `hrv_rmssd_delta_ms`, `rsa_delta`, `affect_var_delta` }


  * `quality`: { `artifact_rate`, `r2_fit`, `temp_flag` }


  * `geo_hint` (optional, coarse)


  * `consent_token` (blind signature proving consent)


  * `psb_hash` and `node_signature`


**Validation rules (validator nodes):**
  * Hash == current authorized master; timestamps in window; KPI deltas within plausible bounds (node‑local model). Blocks failing checks are rejected.


* * *
## 8\. Difficulty Adjustment & Rewards (Protocol Outline)
  * **Epoch:** 30 days.


  * **Target acceptance rate:** X PSBs/day (configurable by governance).


  * **Adjustment:** Statistical threshold for minimum effect size auto‑adjusted to hit target acceptance rate, analogous to mining difficulty.


  * **Rewards:** Micropayments to `node_pubkey` for accepted PSBs.


* * *
### 8.1 Reward Function (Normative)
**Preconditions (quality gates):** reward=0 if any true — `artifact_rate ≥ τ_art` (default 0.20), `min_valid_rr_count < 250`, invalid time window, `signal_hash` mismatch/spec mismatch, or attestation fail.
**Base payout** : `B_base = B_epoch` (epoch budgeted base sats). Halving every `HALVING_EPOCHS`.
**Effect score** (baseline‑normalized):
  * `z_rmssd = (RMSSD_post − RMSSD_pre) / σ_rmssd_personal`


  * `z_rsa = (RSA_post − RSA_pre) / σ_rsa_personal`


  * `S_eff = clamp( α*z_rmssd + (1−α)*z_rsa , 0 , 2.0 )` (default `α=0.5`). If `S_eff < θ_eff` → reward=0.


**Quality score:**
  * `Q_art = (1 − artifact_rate) ^ β_art` (default `β_art=1.5`)


  * `Q_rr = 1 + min((min_valid_rr_count−250)/500, 0.10)`


  * `Q_mot


  * **HR/HRV:** PPG or ECG with validated R‑R extraction.


  * **Sampling:** ECG ≥ 250 Hz; PPG ≥ 64 Hz.


  * **IMU:** 3‑axis accelerometer for artifact suppression.


  * **Clock:** NTP or GNSS‑synced; drift < 100 ms per session.


  * **TEE/SE:** Trusted execution or secure element for key storage and attestation.


* * *
## 10\. Networking & Privacy
  * **PSB transport:** gRPC/QUIC with TLS 1.3.


  * **Privacy:** Differential privacy on aggregates; raw waveforms and raw R‑R intervals remain on device unless explicit user export.


  * **Provenance:** PSB and master manifest hashes timestamped on Bitcoin (OP_RETURN/Taproot commit).


* * *
## 11\. APIs (Excerpt)
### 11.1 Local Render API
  * `GET /signal/current` → manifest + hashes.


  * `POST /signal/render` {device_profile} → returns device‑specific render pack.


### 11.2 Session Control API
  * `POST /session/start` {modalities, target_duration}


  * `POST /session/stop`


  * `GET /session/result/:id` → KPIs + PSB


### 11.3 PSB Submit API
  * `POST /psb/submit` {psb} → {status, reward_txid}


Schemas are JSON; all responses signed by node key.
* * *
## 12\. Governance & Versioning
  * **spec_version:** `1.0.0‑genesis`


  * **Change control:** Multi‑sig proposal → on‑chain hash → community client auto‑update.


  * **Backward compatibility:** Clients must support ≥ 2 prior spec versions.


* * *
## 13\. Test Suite (Conformance)
  * **Audio conformance:** THD, sample‑accurate hash, SPL sweep.


  * **Sensor conformance:** R‑R accuracy vs. reference, artifact rejection under motion.


  * **PSB conformance:** Schema validity, signature correctness, replay‑attack resistance.


* * *
## 14\. Deployment Profiles
  * **Mobile (baseline):** Audio‑only or audio+haptic; PPG from camera or wearable bridge.


  * **Wearable:** Haptic+audio; native PPG/ECG.


  * **Public node:** Environmental audio/light; aggregate PSBs only with opt‑in personal devices nearby.


* * *
## 15\. Legal & Compliance Notes
  * **Classification:** Wellness/relaxation technology; not a diagnostic or therapeutic device.


  * **Data:** User‑controlled; exportable; subject to regional privacy laws.


* * *
## 16\. Genesis Procedure
  1. Freeze this spec → compute `spec_sha256`.


  2. Freeze master asset bundle → compute `sha256_master`.


  3. Publish both hashes on Bitcoin (timestamp txid recorded in manifest).


  4. Release open‑source clients + validator.


* * *
## 17\. Roadmap to v1.1
  * Personalized respiratory pacing model.


  * Multi‑recipient group coherence mode.


  * Expanded validator heuristics (robustness to spoofing).


**End of Spec**
\--- **Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[SIGNAL_MOC]]
