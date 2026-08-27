---
title: ALIGNMENT WOOBERLY VS UNITAXI
tags: [misc, reference, general]
type: document
source: 11_KNOWLEDGE/misc
---





# **Alignment — Wooberly vs UniTaxi**
|               |
| **Area**      | **Feature Set**                       | **Wooberly OOTB** | **UniTaxi Needs** | **Gap / Note**                |
|---------------|---------------------------------------|-------------------|-------------------|-------------------------------|
| Rider App UX  | Signup/OTP                            | ☑️                | ☑️                | Meets                         |
|               | Set pickup/drop, suggestions          | ☑️                | ☑️                | Meets                         |
|               | Multi-vehicle categories              | ☑️                | ☑️                | Meets                         |
|               | Promo codes                           | ☑️                | ☑️                | Meets                         |
|               | Cancel with reason                    | ☑️                | ☑️                | Meets                         |
|               | In-app chat                           | ☑️                | ☑️                | Meets                         |
|               | Schedule ride                         | ☑️                | ☑️                | Meets                         |
|               | Emergency contacts (basic)            | ☑️                | ☑️                | Meets (enhance later for SOS) |
|               | RTL / Multi-language basics           | ☑️                | ☑️                | Meets                         |
| Driver App UX | Availability toggle                   | ☑️                | ☑️                | Meets                         |
|               | Accept/decline jobs                   | ☑️                | ☑️                | Meets                         |
|               | Extra fees (e.g., toll)               | ☑️                | ☑️                | Meets                         |
|               | Earnings dashboard                    | ☑️                | ☑️                | Meets                         |
|               | Trip history, ratings, notifications  | ☑️                | ☑️                | Meets                         |
|               | In-app chat                           | ☑️                | ☑️                | Meets                         |
| Admin         | Dashboard (live map/heatmap)          | ☑️                | ☑️                | Meets                         |
|               | Manage riders/drivers/vehicles        | ☑️                | ☑️                | Meets                         |
|               | Categories/locations/geofencing       | ☑️                | ☑️                | Meets                         |
|               | Fare mgmt, bookings (incl. scheduled) | ☑️                | ☑️                | Meets                         |
|               | Cancellations & reasons               | ☑️                | ☑️                | Meets                         |
|               | Ratings, promo codes, notifications   | ☑️                | ☑️                | Meets                         |
|               | Multi-language & chat monitoring      | ☑️                | ☑️                | Meets                         |


# **Gaps — UniTaxi (VN) Requirements to Build**
## **A) Legal, tax & compliance (VN)**
|                                                                                                                                                                                  |
| **Requirement**                                                                                                                                                                  | **Wooberly OOTB** | **UniTaxi Needs** | **Action / Build**                                                                 |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|-------------------|------------------------------------------------------------------------------------|
| E-Invoice end-to-end (MISA/Viettel), B2C invoice flow, status sync (Queued/Sent/Accepted/Rejected), PDF/XML ≥5y, GDT ≤24h, edit/cancel per Decree 123/TT78, Admin Invoice Centre | ⬜                 | ☑️                | Build **Invoice Service + Rider invoice UI + Admin E-Invoice Centre**              |
| Data residency (VN), PDPD consent, PII masking, AES-256 at rest, TLS 1.3, immutable audit                                                                                        | ⬜                 | ☑️                | Build **Security & Compliance layer** (consent UX, masking, audit ledger)          |
| Driver onboarding per Decree 10/Circular 12 (CCCD, B2+, health cert, police clearance), OCR + face match, expiry checks, one-driver-per-CCCD, approval workflow & alerts         | ⬜                 | ☑️                | Build **KYC module** (OCR/FR SDK) + **Verification queue** \+ **Expiry scheduler** |


## **B) Payments & finance**
|                                                                                                                                                |
| **Requirement**                                                                                                                                | **Wooberly OOTB** | **UniTaxi Needs** | **Action / Build**                                             |
|------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|-------------------|----------------------------------------------------------------|
| Local payments: **VNPay/MoMo/ZaloPay** \+ reconciliation + cash fallback                                                                       | ⬜                 | ☑️                | Build **Payment gateway adapters** \+ settlement reports       |
| Referral & Rewards **3% lifetime** (immutable link, “retained profit” calc, **Referral Wallet** , **PIT 5%** withholding, anti-fraud, exports) | ⬜                 | ☑️                | Build **Referral Engine + Ledger** \+ anti-fraud + FIN exports |
| Wallets & payouts (drivers + referrals), sub-ledgers, negative balance, approvals, PIT reports, bank/e-wallet disburse                         | ⬜                 | ☑️                | Build **Ledger service** \+ **Payout orchestrator**            |


## **D) Pricing, dispatch & analytics**
|                                                                                                                                              |
| **Requirement**                                                                                                                              | **Wooberly OOTB** | **UniTaxi Needs** | **Action / Build**                                      |
|----------------------------------------------------------------------------------------------------------------------------------------------|-------------------|-------------------|---------------------------------------------------------|
| VN pricing governance: versioned fare tables per city/zone, ToD/surge, multi-PSP fees, approval & full audit                                 | ⬜                 | ☑️                | Build **Pricing service** (change logs, role approvals) |
| SLO/SLA & monitoring: P95/99 API targets, uptime 99.9%, ops dashboards (match time P50/P90, completion), alerting (payments, e-invoice, SOS) | ⬜                 | ☑️                | Build **Observability stack + Ops dashboard + Alerts**  |


* * *
# **🧾 Wooberly Deliverables — Free vs Paid Comparison.**
|                                            |
| **Category**                               | **Item / Service**                                    | **Included (Free)** | **Additional Cost / Notes**                           |
|--------------------------------------------|-------------------------------------------------------|---------------------|-------------------------------------------------------|
| 🎯 **Product**                              |  Full source code (Admin, Rider App, Driver App)      | ☑️                  | Delivered within 8 hours post-payment                 |
|                                            | 1-time setup / installation on 1 server               | ☑️                  | Only once; reinstallation later = paid                |
|                                            | Hosting / server                                      | ⬜                   | You must provide (AWS / DigitalOcean etc.)            |
|                                            | Base product features (same as demo)                  | ☑️                  | Any new feature = paid customisation                  |
| 💻 **Technology Stack**                     |  Flutter mobile apps (iOS/Android)                    | ☑️                  | Unified codebase                                      |
|                                            | NodeJS, ExpressJS, ReactJS, GraphQL backend           | ☑️                  | Standard open-source frameworks                       |
|                                            | MySQL database                                        | ☑️                  | You host / manage                                     |
|                                            | Firebase, Socket.IO, Google Maps SDK                  | ☑️                  | You provide API keys + pay usage                      |
| 🔧 **Installation Process**                 |  Trello setup with installation team                  | ☑️                  | Closed after 30 days inactivity                       |
|                                            | Installation documentation (Ubuntu/Mac)               | ☑️                  | Provided after purchase                               |
|                                            | Folder structure & architecture doc                   | ☑️                  | Included                                              |
|                                            | API specification document                            | ☑️                  | Included                                              |
|                                            | Support for design uploads (icons, logos)             | ⬜                   | You must provide assets; design work = paid           |
| 💰 **Third-Party Requirements (Your cost)** |  Twilio SMS / OTP                                     | ⬜                   | You pay per usage                                     |
|                                            | Google Maps Billing                                   | ⬜                   | You pay per usage                                     |
|                                            | Stripe account (default payment)                      | ⬜                   | You set up / share API keys                           |
|                                            | Custom payment gateways (VNPay, MoMo, ZaloPay)        | ⬜                   | Requires paid customization                           |
|                                            | Apple Developer Account                               | ⬜                   | US$99/year, must grant direct access                  |
|                                            | Google Play Developer Account                         | ⬜                   | US$25 one-time                                        |
|                                            | SSL Certificate (Let’s Encrypt)                       | ☑️                  | Free (optional paid SSL = +US$50/install)             |
| 🌐 **App Store Design & Submission**        | Base UI included (same as demo)                       | ☑️                  | Meets Android Play rules                              |
|                                            | iOS app submission design work                        | ⬜                   | +US$400 (16h) for compliant design                    |
|                                            | Design review of external team assets                 | ⬜                   | +US$100 (4h)                                          |
| 📞 **Technical Support**                    |  Free support period (bug fix, text/color changes)    | ☑️                  | Starts from purchase date                             |
|                                            | Translation support (up to 3 languages, 2 iterations) | ☑️                  | Beyond that = paid                                    |
|                                            | Critical bug fixing                                   | ☑️                  | Free with time frame commitment                       |
|                                            | Reinstallation or modified code issues                | ⬜                   | Not covered                                           |
|                                            | Custom changes / new features                         | ⬜                   | US$25/hour                                            |
|                                            | Local setup / Git issues                              | ⬜                   | Not supported                                         |
|                                            | Communication channel                                 | ☑️                  | Email only (no calls/WhatsApp)                        |
| ⏱ **Support SLA**                          |  Response time 24–48h on business days                | ☑️                  | No weekend support                                    |
| 📑 **Legal & Policy**                       | Terms & Conditions                                    | ☑️                  | https://www.rentallscript.com/terms-and-conditions/   |
|                                            | Refund policy (no refunds post-delivery)              | ☑️                  | https://www.rentallscript.com/returns-refunds-policy/ |
|                                            | FAQ (product-specific)                                | ☑️                  | https://www.rentallscript.com/uber-clone/#faq         |


# **✅ Summary — What You Get “Free”**
  * Complete source code for **Admin + Rider + Driver apps**.


  * One-time installation on your server.


  * Documentation (installation, architecture, API).


  * Free support for:
    * Text/color/static content changes.
    * Translation (3 languages, ≤2 rounds).
    * Critical bug fixes.


  * SSL via **Let’s Encrypt**.


  * Trello project coordination + email support.


# **💵 What’s Not Free / Paid Customisation**
  * New features (e.g., **VNPay/MoMo/ZaloPay** , **MISA/Viettel eInvoice** , **iSAC integration** , **ESG/CO₂e** , **Referral wallet** , etc.).


  * Server, domains, Apple/Google developer accounts.


  * Any **redesign** for iOS store acceptance (US$400 typical).


  * Additional installs or re-installs.


  * All **third-party API usage** (Twilio, Google Maps, Stripe, etc.).


  * Extended support, local/Git issues, or modified code.


* * *
# **🚀 Next Steps to Launch UniTaxi MVP**
* * *
## **PHASE 0 – PREPARATION**
**🎯 Goal:** Secure environment and admin access for the installation team.
|                                         |
| **Task**                                | **Responsible**         | **Deliverable**                        | **Notes**                                                |
|-----------------------------------------|-------------------------|----------------------------------------|----------------------------------------------------------|
| ✅ Purchase Wooberly license             | UniPower                | Payment confirmation                   | Choose “Wooberly Taxi” base version                      |
| ✅ Share server access                   | UniPower                | SSH root to clean Ubuntu 24.04         | AWS or DigitalOcean (4GB RAM / 50GB SSD min)             |
| ✅ Provide domain & SSL                  | UniPower                | app.unitaxi.vn + Let’s Encrypt SSL     | SSL free via Let’s Encrypt                               |
| ✅ Prepare developer accounts            | UniPower                | Apple ($99/yr) + Google ($25 one-time) | Business-level, DUNS verified                            |
| ✅ Provide branding package              | UniPower                | Logo, colour codes, app icons          | PNG/SVG per their design folder format                   |
| ✅ Share Google Maps & Firebase API keys | UniPower                | API credentials                        | Enable Directions, Distance Matrix, Geocode, and Billing |
| ✅ Sign technical engagement email       | UniPower & RadicalStart | Formal approval to begin installation  | Needed for Trello activation                             |


* * *
## **PHASE 1 – BASE INSTALLATION**
**🎯 Goal:** Deploy stock Wooberly + configure environment.
|                                        |
| **Task**                               | **Responsible** | **Deliverable**                 | **Notes**                   |
|----------------------------------------|-----------------|---------------------------------|-----------------------------|
| Install admin + rider + driver apps    | RadicalStart    | Base app live on your server    | One-time free installation  |
| Configure Firebase, Maps, Twilio (OTP) | RadicalStart    | Working demo environment        | You cover API usage cost    |
| Upload UniPower branding               | RadicalStart    | Themed login & splash screens   | Uses your colours and logo  |
| Connect domain + SSL                   | RadicalStart    | HTTPS app URLs                  | Done via Let’s Encrypt      |
| Verify OTP, booking, dispatch flow     | UniPower QA     | Confirm working end-to-end flow | Using internal test numbers |


* * *
## **PHASE 2 – LOCALISATION & COMPLIANCE **
**🎯 Goal:** Make app usable in Vietnam & compliant with Decree 10.
|                                            |
| **Task**                                   | **Responsible**     | **Deliverable**              | **Notes**                             |
|--------------------------------------------|---------------------|------------------------------|---------------------------------------|
| Translate static content                   | RadicalStart (Free) | VN/EN bilingual text         | Max 3 languages / 2 iterations        |
| Localise address & map defaults            | RadicalStart        | vi_VN locale, VN road naming | Verify map accuracy for HCMC/Hanoi    |
| Enable multi-currency (VND)                | RadicalStart        | VND symbol, zero decimals    | Check formatting in fare display      |
| Configure SMS Gateway (Twilio or local VN) | UniPower            | Local number for OTP         | Optional: migrate to VN Gateway later |
| Test driver onboarding (manual review)     | UniPower Ops        | Verify KYC flow              | Manual upload until OCR module ready  |


* * *
## **PHASE 3 – CUSTOM INTEGRATIONS**
**🎯 Goal:** Add critical Vietnam-only modules.
|                                               |
| **Task**                                      | **Responsible**        | **Deliverable**                 | **Notes**                        |
|-----------------------------------------------|------------------------|---------------------------------|----------------------------------|
| Add eInvoice provider API (MISA or Viettel)   | UniPower Tech Partner  | Invoice Service (Admin + Rider) | Custom build (start parallel)    |
| Replace Stripe with VNPay/MoMo/ZaloPay        | RadicalStart / Partner | Local payment integration       | +US$25/hour est. 40–60h          |
| Connect iSAC API (battery %, nearest charger) | UniPower Tech Partner  | EV data visible in driver app   | Sidecar API ready                |
| Build referral wallet (3% lifetime)           | UniPower Dev           | Sub-ledger + Admin reports      | Phase 3 optional if time permits |


* * *
## **PHASE 4 – TESTING & PILOT **
**🎯 Goal:** Validate stability, speed, and compliance.
|                                 |
| **Task**                        | **Responsible** | **Deliverable**                                   | **Notes**                                |
|---------------------------------|-----------------|---------------------------------------------------|------------------------------------------|
| Functional testing              | UniPower QA     | Checklist: booking, cancel, payment, invoice, SOS | Match time ≤ 60s                         |
| Performance testing             | RadicalStart    | API latency report (P95 < 300ms)                  | Load 300 drivers, 1k rides/day           |
| App Store submissions           | RadicalStart    | Play Store + TestFlight builds                    | Apple review may require unique branding |
| Safety check: SOS, masked calls | UniPower Ops    | Verify live GPS & call routing                    | Critical for legal compliance            |


* * *
## **PHASE 5 – LAUNCH & TRAINING **
**🎯 Goal:** Go live with 300 EV drivers (pilot phase).
|                                       |
| **Task**                              | **Responsible** | **Deliverable**             | **Notes**                               |
|---------------------------------------|-----------------|-----------------------------|-----------------------------------------|
| Final data migration                  | UniPower        | Fleet, driver, station data | Import via UniPortal                    |
| Admin dashboard handover              | RadicalStart    | Credentials & guide         | Full operational control                |
| Pilot launch (300 EVs, 10 Đội trưởng) | UniPower        | MVP Go-live                 | With driver training & safety briefing  |
| Feedback & optimisation plan          | Both teams      | Post-launch backlog         | Prioritise automation + ESG module next |


* * *
# **⚙️ Post-Launch**
After MVP launch, focus on:
  * Automating **driver onboarding (OCR, face match)**.


  * Implementing **referral wallet + PIT tax handling**.


  * Expanding to **UniPortal v2.0** with finance, compliance, and EV dashboards.


  * Adding **Carbon Scoring / ESG reports** for corporate clients.


  * Integrating **charging loyalty programs** with partner minimarts.


* * *
# **📋 Quick Checklist for UniPower to Start Installation**
|                                               |
| **✅**                                         | **Item** |
|-----------------------------------------------|----------|
| ☐ Purchase Wooberly license (confirm version) |          |
| ☐ Set up clean Ubuntu 24.04 server (AWS / DO) |          |
| ☐ Register Apple & Google developer accounts  |          |
| ☐ Purchase domain + SSL (Let’s Encrypt free)  |          |
| ☐ Prepare logo, colours, app icons            |          |
| ☐ Generate Google Maps API key (with billing) |          |
| ☐ Create Firebase project (iOS & Android)     |          |
| ☐ Twilio / VN Gateway SMS credentials         |          |
| ☐ Share all credentials via Trello board      |          |
| ☐ Approve installation start                  |          |


\--- **Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
