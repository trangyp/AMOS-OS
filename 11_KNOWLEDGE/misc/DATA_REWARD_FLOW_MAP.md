---
title: DATA REWARD FLOW MAP
tags: [misc, reference, general]
type: document
source: 11_KNOWLEDGE/misc
---





# **Data → Reward Flow Map**
## **1 — Base Eligibility (Consensus-Required)**
**Directly determines if a session gets** _**any**_**payout.**
  * `signal_hash` → Confirms authorized master waveform.


  * `spec_version` → Valid protocol compliance.


  * `node_pubkey` → Identifies payout recipient.


  * `timestamp_start` / `timestamp_end` → Valid measurement window.


  * `consent_token` → Proof of opt-in.


  * `hrv_rmssd_delta_ms` & `rsa_delta` → Core effect score (`S_eff`).


  * `artifact_rate` → Quality gate + part of `S_qual`.


  * `psb_hash` & `node_signature` → Authenticates the Proof-of-Signal Block.


**Reward algorithm stage:**
  * **Preconditions** → Fail = `Reward_sats = 0`


  * `S_eff` computed from `hrv_rmssd_delta_ms` & `rsa_delta`


  * `artifact_rate` feeds into `Q_art` in `S_qual`.


* * *
## **2 — Reward Multiplier Inputs**
**Increase sats earned per valid session.**
### **A. Effect & Quality**
  * `affect_var_delta` → Bonus in `S_eff` (optional weight)


  * `min_valid_rr_count` → `Q_rr` multiplier in `S_qual`


  * `r2_fit` → Quality bonus in `S_qual`


  * `motion_vector` → Motion penalty in `S_qual`


### **B. Context Completeness**
  * `ambient_noise_level` → `C_env` in `S_ctx`


  * `ambient_light_level` → `C_env` in `S_ctx`


  * `delivery_modalities` → `C_mods` in `S_ctx`


### **C. Coverage & Trust**
  * `geo_hint` → Scarcity index for `S_cov`


  * `accept_rate_90d` / `anom_rate_30d` → `S_trust`


**Reward algorithm stage:**
  * **Multipliers applied after**`**S_eff**`**and**`**S_qual**`


  * `S_ctx` adds up to +10%


  * `S_cov` adds up to +30% (geo/time scarcity)


  * `S_trust` adds up to +20% for long-term good behavior


* * *
## **3 — Vault-Only Monetizable (No Direct Reward Impact)**
**Not part of the reward formula, but high market value in Sovereign Data Vault.**
  * `rr_intervals_series`


  * `ppg_waveform_segments`


  * `ecg_waveform_segments`


  * `respiration_trace`


  * `device_profile` & `sensor_sampling_rate`


  * `mood_index`, `calmness_index`, `alertness_index`


  * `open_comment`


**Monetization path:**
  * Licensed to research, healthcare, or wellness partners for BTC payments


  * Does not influence sats per session (keeps reward formula predictable and fair)


* * *
## **4 — Final Reward Formula Recap**
```
    Reward_sats = floor( B_base * S_eff * S_qual * S_ctx * S_cov * S_trust )
    
```
  * **B_base** : Base sats per PSB (epoch-controlled)


  * **S_eff** : Effect score from `hrv_rmssd_delta_ms`, `rsa_delta` (+optional affect_var_delta)


  * **S_qual** : Quality score from `artifact_rate`, `min_valid_rr_count`, `r2_fit`, `motion_vector`


  * **S_ctx** : Completeness bonus from `ambient_noise_level`, `ambient_light_level`, `delivery_modalities`


  * **S_cov** : Scarcity multiplier from `geo_hint` (opt-in) & time slot coverage


  * **S_trust** : Trust multiplier from acceptance rate & anomaly rate history


* * *
```
    flowchart TD
        subgraph CR[Consensus-Required - Base Eligibility]
            A1(signal_hash)
            A2(spec_version)
            A3(node_pubkey)
            A4(timestamp_start / timestamp_end)
            A5(consent_token)
            A6(hrv_rmssd_delta_ms)
            A7(rsa_delta)
            A8(artifact_rate)
            A9(psb_hash)
            A10(node_signature)
        end
    
        subgraph RM[Reward Multiplier Inputs]
            B1(affect_var_delta)
            B2(min_valid_rr_count)
            B3(r2_fit)
            B4(motion_vector)
            B5(ambient_noise_level)
            B6(ambient_light_level)
            B7(delivery_modalities)
            B8(geo_hint)
            B9(accept_rate_90d / anom_rate_30d)
        end
    
        subgraph VM[Vault-Only Monetizable]
            C1(rr_intervals_series)
            C2(ppg_waveform_segments)
            C3(ecg_waveform_segments)
            C4(respiration_trace)
            C5(device_profile / sensor_sampling_rate)
            C6(mood_index / calmness_index / alertness_index)
            C7(open_comment)
        end
    
        CR --> F[Reward Formula]
        RM --> F
        VM --> D[Monetization Layer: BTC licensing / research data sales]
    
        style CR fill:#ffcccc,stroke:#333,stroke-width:1px
        style RM fill:#ccffcc,stroke:#333,stroke-width:1px
        style VM fill:#ccccff,stroke:#333,stroke-width:1px
        style F fill:#ffffcc,stroke:#333,stroke-width:1px
        style D fill:#e6e6fa,stroke:#333,stroke-width:1px
    
```
This shows:
  * **Red** = minimum data for consensus (no reward without it)


  * **Green** = optional reward multipliers


  * **Blue** = vault-only monetizable data


  * **Yellow** = reward calculation


  * **Lavender** = off-chain monetization


Do you want me to now create the **Bitcoin-style PSB block diagram** that visually packages these datapoints before they are timestamped on-chain?
* * *
## **1 — Data → Reward Flow Map** (Mermaid)
_(Shows how each datapoint type connects to the payout formula)_
```
    flowchart TD
        subgraph CR["Consensus-Required (Base Eligibility)"]
            A1(signal_hash)
            A2(spec_version)
            A3(node_pubkey)
            A4(timestamp_start / timestamp_end)
            A5(consent_token)
            A6(hrv_rmssd_delta_ms)
            A7(rsa_delta)
            A8(artifact_rate)
            A9(psb_hash)
            A10(node_signature)
        end
    
        subgraph RM["Reward Multiplier Inputs"]
            B1(affect_var_delta)
            B2(min_valid_rr_count)
            B3(r2_fit)
            B4(motion_vector)
            B5(ambient_noise_level)
            B6(ambient_light_level)
            B7(delivery_modalities)
            B8(geo_hint)
            B9(accept_rate_90d / anom_rate_30d)
        end
    
        subgraph VM["Vault-Only Monetizable"]
            C1(rr_intervals_series)
            C2(ppg_waveform_segments)
            C3(ecg_waveform_segments)
            C4(respiration_trace)
            C5(device_profile / sensor_sampling_rate)
            C6(mood_index / calmness_index / alertness_index)
            C7(open_comment)
        end
    
        CR --> F["Reward Formula: Reward_sats = floor( B_base * S_eff * S_qual * S_ctx * S_cov * S_trust )"]
        RM --> F
        VM --> D["Monetization Layer: BTC licensing / research data sales"]
    
        style CR fill:#ffcccc,stroke:#333,stroke-width:1px
        style RM fill:#ccffcc,stroke:#333,stroke-width:1px
        style VM fill:#ccccff,stroke:#333,stroke-width:1px
        style F fill:#ffffcc,stroke:#333,stroke-width:1px
        style D fill:#e6e6fa,stroke:#333,stroke-width:1px
    
```
* * *
## **2 — Bitcoin-style PSB Structure**
 _(Shows how datapoints are packaged into a Proof-of-Signal Block before on-chain timestamping)_
```
    graph TB
        subgraph PSB[Proof-of-Signal Block]
            H1[Block Header]
            H2[Previous PSB Hash]
            H3[Timestamp]
            H4[Node Public Key]
            H5[Validator Signature]
    
            subgraph DATA[Payload]
                D1[Consensus-Required Data]
                D2[Reward Multiplier Data]
                D3[Vault-Only Monetizable Data]
            end
    
            H6[Block Hash]
        end
    
        H1 --> H2 --> H3 --> H4 --> H5 --> DATA --> H6
        style PSB fill:#f0f8ff,stroke:#333,stroke-width:1px
        style DATA fill:#f9f9f9,stroke:#333,stroke-width:1px
    
```
* * *
## **3 — Monetization Path Diagram**
 _(Shows reward vs external licensing flows)_
```
    flowchart LR
        A[Data Collection Node] --> B[Proof-of-Signal Block]
        B --> C[Reward Engine]
        B --> D[Sovereign Data Vault]
    
        C --> E[On-Chain BTC Reward]
        D --> F[Off-Chain Licensing]
        D --> G[Research / Healthcare Partnerships]
    
        style A fill:#ffebcc,stroke:#333,stroke-width:1px
        style B fill:#f0f8ff,stroke:#333,stroke-width:1px
        style C fill:#ffffcc,stroke:#333,stroke-width:1px
        style D fill:#ccccff,stroke:#333,stroke-width:1px
        style E fill:#ccffcc,stroke:#333,stroke-width:1px
        style F fill:#e6e6fa,stroke:#333,stroke-width:1px
        style G fill:#e6e6fa,stroke:#333,stroke-width:1px
    
```
* * *
If you want, I can also **link all three diagrams into a single “Signal Economy Architecture” doc** so it’s ready for investor decks and engineering wikis.
Do you want me to package them like that next?
\--- **Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
