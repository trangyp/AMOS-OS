---
title: LIST OF COLLECTABLE DATAPOINTS
tags: [misc, reference, general, canon/knowledge]
type: document
source: 11_KNOWLEDGE/misc
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general

---


# **Complete list of collectable datapoints**
Here’s the **complete audited list** of collectable datapoints in your Proof-of-Signal network — grouped for clarity, with flags for _consensus-required_ , _reward-multiplier_ , and _vault-only monetizable_ categories.
* * *
## **1 — Core Session Metadata**
 _(Consensus-Required)_
  * `signal_hash` — cryptographic fingerprint of delivered master signal.


  * `spec_version` — version of the Master Signal Spec used.


  * `node_pubkey` — Ed25519 public key of delivering node.


  * `timestamp_start` / `timestamp_end` — UTC session start/end times.


  * `consent_token` — cryptographic proof of user opt-in.


  * `geo_hint` _(optional, reward-multiplier)_ — coarse location cell ID if opted in.


* * *
## **2 — Biological KPI Deltas**
 _(Consensus-Required)_
  * `hrv_rmssd_delta_ms` — RMSSD HRV change from pre to post session.


  * `rsa_delta` — Respiratory sinus arrhythmia change (vagal tone).


_(Reward-Multiplier)_
  * `affect_var_delta` — Change in affect variability index.


* * *
## **3 — Quality & Confidence Metrics**
 _(Consensus-Required)_
  * `artifact_rate` — % of invalid HR/HRV data from motion/noise.


_(Reward-Multiplier)_
  * `min_valid_rr_count` — number of valid heartbeat intervals in session.


  * `r2_fit` — model fit score for expected vs. actual response.


  * `motion_vector` — magnitude of movement during session.


* * *
## **4 — Raw Biological Signal Data**
 _(Vault-Only Monetizable)_ — stored locally unless explicit export consent.
  * `rr_intervals_series` — raw R-R intervals with timestamps.


  * `ppg_waveform_segments` — optical pulse waveform samples.


  * `ecg_waveform_segments` — electrocardiogram samples.


  * `respiration_trace` — respiration pattern from PPG or dedicated sensor.


* * *
## **5 — Device & Environment Context**
 _(Reward-Multiplier)_
  * `device_profile` — device model, sensor type, firmware version.


  * `sensor_sampling_rate` — HR/HRV capture rate (Hz).


  * `delivery_modalities` — modalities used (audio/haptic/visual/EMF).


  * `session_duration` — seconds of actual signal delivery.


  * `ambient_noise_level` — environmental dB reading.


  * `ambient_light_level` — lux reading during session.


* * *
## **6 — Cryptographic & Network Layer**
 _(Consensus-Required)_
  * `psb_hash` — SHA-256 of Proof-of-Signal Block.


  * `node_signature` — Ed25519 signature over PSB.


_(Optional, Governance)_
  * `validator_signature` — from third-party validation node.


  * `blockchain_txid` — proof timestamp transaction ID.


* * *
## **7 — Optional User Self-Report**
 _(Reward-Multiplier, Vault-Only Monetizable)_
  * `mood_index` — pre/post Likert scale score.


  * `calmness_index` — pre/post Likert scale score.


  * `alertness_index` — pre/post Likert scale score.


  * `open_comment` — free-text qualitative note.


* * *
### **Audit Notes**
  * **Consensus-Required** datapoints are the _minimum proof set_ — no rewards without them.


  * **Reward-Multiplier** datapoints boost payouts for quality, coverage, and completeness.


  * **Vault-Only Monetizable** datapoints hold _external market value_ but remain in your Sovereign Data Vault unless explicitly licensed.


  * All optional data fields must be **opt-in** per privacy laws (GDPR/CCPA/PIPEDA).


  * Raw biometrics (e.g., ECG waveforms) require special handling in HIPAA and GDPR-covered jurisdictions.


* * *
--- **Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
