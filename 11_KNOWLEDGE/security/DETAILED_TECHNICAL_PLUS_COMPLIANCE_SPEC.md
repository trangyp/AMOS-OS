---
title: DETAILED TECHNICAL PLUS COMPLIANCE SPEC
tags: [security]
type: document
source: 11_KNOWLEDGE/security
---



# **Detailed technical + compliance spec**
**Technical + compliance spec** for:
  1. **MISA integration** (e-invoice + accounting).


  2. **Local payment gateways** : MoMo, VNPAY, ViettelPay and local banks, with UI/flows similar to **Grab / Xanh SM** and compliant with Vietnamese regulation.


* * *
# **0\. Regulatory and Compliance Baseline (Vietnam)**
These are the main laws/standards your payment + invoicing design must align with:
  * **Non-cash payments** :
    * Decree **101/2012/NĐ-CP** on non-cash payments, amended by Decree **80/2016/NĐ-CP**.
    * SBV regulations on payment intermediaries and e-wallets.


  * **Bank cards / payment intermediaries** :
    * Circular **19/2016/TT-NHNN** on bank card operations.


  * **E-invoices** :
    * Decree **123/2020/NĐ-CP** and Circulars guiding e-invoices (MISA is certified to issue).


  * **Personal data** :
    * Decree **13/2023/NĐ-CP** on Personal Data Protection (PDPD) – financial & payment data is **sensitive data** with extra safeguards.


  * **Cybersecurity / information security** :
    * Law on Cyberinformation Security 2015 and Law on Cybersecurity 2018 – requirements on logging, incident handling, storing data in VN, etc.


**Design principles:**
  1. **UniPower is not a payment intermediary** (no e-wallet, no stored balance).


  2. **Only licensed providers** (MoMo, VNPAY, ViettelPay, banks) handle payment and store payment credentials.


  3. **UniPower only processes “necessary” personal data** , with:
     * consent screens in app,
     * minimal data in callbacks,
     * audit log for all payment events.


  4. **All payment and invoice data stored on VN-based servers** , with backups ≥ 5 years.


* * *
# **1\. Unified Payment & Invoice Architecture**
Applies to **all** gateways and MISA.
## **1.1 Components**
  * **UniApp-User** – customer app (UniTaxi).


  * **UniApp-Driver** – driver app (UniTaxi Driver).


  * **UniCore-API** – backend for UniPower (Node/Java/PHP – language-agnostic).


  * **UniPay-Service** – internal payment abstraction service inside UniCore.


  * **Gateways** : MoMo, VNPAY, ViettelPay, Bank PGW/Napas.


  * **MISA eInvoice Service** – certified e-invoice provider.


  * **UniLedger** – internal ledger + reconciliation DB.


## **1.2 Core objects (internal)**
  * Ride – trip record.


  * PaymentIntent – one planned payment for a Ride.


  * PaymentTransaction – actual gateway transaction instance.


  * PaymentMethod – CASH, MOMO, VNPAY, VIETTELPAY, CARD_BANK.


  * InvoiceRequest / Invoice – for MISA.


  * ReconciliationBatch – T+0/T+1 settlement batch per provider.


Status mapping (internal):
  * PaymentIntent.status: PENDING → IN_PROGRESS → SUCCEEDED / FAILED / CANCELED.


  * PaymentTransaction.status: CREATED / PENDING_GATEWAY / SUCCESS / FAILURE / REFUNDED.


* * *
# **2\. UI & UX – Aligning with Grab / Xanh SM Patterns**
The following screens and flows should mimic the mental model of Grab/Xanh SM:
## **2.1 Payment selection before booking**
  * On **“Confirm booking”** screen:
    * Section **Payment method** :
      * Shows active method (e.g. “Tiền mặt”, “MoMo”, “VNPAY”, “ViettelPay”, “Thẻ ngân hàng”).
      * Icon of wallet/card, same style as Grab/Xanh SM.
    * Tap → **Payment Methods Screen** :


Fields:
  * List of methods:
    * Cash
    * MoMo E-Wallet
    * VNPAY QR
    * ViettelPay
    * Card / ATM (Napas) via VNPAY or other PGW.


  * Each row:
    * Logo, short description (“Thanh toán ngay trong ứng dụng”, “Quét QR”, …).
    * Status: Đã liên kết, Chưa liên kết.


  * For wallet methods:
    * Button “Liên kết” opens provider flow (for MoMo typically no long-term link, but you can store a pseudo-link state: “Preferred wallet MoMo”).


UX rules:
  * User must **always see** total fare and chosen payment method on booking screen.


  * When switching from wallet → cash for an ongoing trip, mark PaymentIntent as SWITCHED_TO_CASH and show proper notice (“Chuyến này sẽ thanh toán tiền mặt”).


## **2.2 Payment confirmation after trip**
  * After driver ends ride:
    * Screen Shows:
      * Final fare breakdown (base, surcharges, promotions).
      * Payment method used (icon + text “Đã thanh toán qua MoMo”, etc.).
      * Status chip: Thành công, Đang xử lý…, Thất bại.
    * If gateway callback hasn’t arrived:
      * Show spinner + message:
        * “Hệ thống đang xác nhận thanh toán. Nếu cần, vui lòng không đóng ứng dụng.”
    * If failure:
      * Offer:
        * retry same method,
        * switch to cash.


## **2.3 Receipts & invoices**
  * **Trip history** :
    * Each trip shows a tag:
      * “Tiền mặt”
      * “MoMo thành công”
      * “VNPAY QR thành công”
    * Tap → trip details:
      * Payment reference: internal transaction_id + provider orderId or vnp_TxnRef.
      * Button:
        * “Yêu cầu hóa đơn” (calls MISA through UniCore).
        * “Xem hóa đơn” (download from MISA).


UX, legally:
  * Must show legal entity name and tax ID in the invoice section.


  * Terms and data-protection links accessible from payment screens.


* * *
# **3\. Document 1 – Detailed MISA Integration Spec**
Goal: **end-to-end e-invoice** for every non-cash payment, with optional invoices for cash trips.
## **3.1 Roles and assumptions**
  * UniPower is the **seller** issuing VAT invoices.


  * MISA is the **certified e-invoice platform** (per VN tax regulations).


  * UniCore connects to MISA via their official API (REST/JSON or SOAP depending on deployment).


## **3.2 Data model**
Key fields for InvoiceRequest:
  * invoice_id (internal UUID)


  * ride_id


  * payment_transaction_id


  * buyer_type: INDIVIDUAL / COMPANY


  * Buyer info:
    * buyer_name
    * tax_code (company)
    * company_name
    * address
    * email
    * phone


  * Invoice amounts:
    * subtotal
    * tax_rate
    * tax_amount
    * total_amount


  * Line items (array):
    * description (e.g. “Dịch vụ vận chuyển hành khách bằng taxi công nghệ”)
    * unit
    * quantity
    * unit_price
    * line_total


  * Metadata:
    * payment_method (CASH/MOMO/VNPAY/…)
    * payment_ref (gateway orderId / txnRef)
    * issue_channel: MOBILE_APP
    * created_at, updated_at


## **3.3 API flows**
### **3.3.1 Customer requests invoice**
From UniApp:
  1. User taps **“Yêu cầu hóa đơn”** in trip details.


  2. App shows form:
     * For individual: name, email, phone.
     * For company: company name, tax code, address, email.


  3. App POST → POST /api/invoices/request:


Example body (simplified):
```
    {
      "ride_id": "RIDE-123",
      "buyer_type": "COMPANY",
      "company_name": "Cong ty ABC",
      "tax_code": "0101234567",
      "address": "123 Pho Hue, Ha Noi",
      "email": "ketoan@abc.com"
    }
```
### **3.3.2 UniCore creates InvoiceRequest**
  * Validate ride & payment status SUCCEEDED.


  * Ensure no existing issued invoice for this ride.


  * Save InvoiceRequest with status PENDING.


  * Add to **MISA dispatch queue**.


### **3.3.3 Dispatch to MISA**
Service MisaAdapter runs (sync or background job):
  1. Fetch pending InvoiceRequests.


  2. Transform to MISA request format:
     * mapping fields to MISA schema (customer info, items, tax rate).


  3. Call MISA API:
     * CreateInvoice / IssueInvoice endpoint.
     * Include digital signature or token as required.


  4. MISA returns:
     * success: InvoiceNo, InvoiceSeries, IssueDate, LinkPDF or base64 PDF.
     * failure: error code + message.


### **3.3.4 Handling responses**
  * On success:
    * Update InvoiceRequest.status = ISSUED.
    * Store:
      * misa_invoice_no
      * misa_series
      * misa_issue_date
      * misa_pdf_url or stored blob.


  * On failure:
    * status = FAILED.
    * Keep error message for support UI.
    * Expose to admin to retry after fixing data.


### **3.3.5 Customer view/download**
Endpoint: GET /api/invoices/{ride_id}
  * Returns invoice status + link.


  * If issued:
    * Provide pdf_url (reverse-proxied through UniCore) or direct MISA link.


  * App:
    * Shows Đã phát hành + button **“Tải hóa đơn”**.
    * Opens PDF viewer.


## **3.4 Back-office UI (UniPortal)**
Screens:
  1. **Invoice Queue**
     * Columns: invoice_id, ride_id, buyer_name, tax_code, amount, status, last_error.
     * Actions: “Gửi MISA lại”, “Hủy yêu cầu”.


  2. **Invoice Detail**
     * All input fields + gateway payment reference.
     * Logs of MISA calls (timestamp, payload hash, status).


  3. **Reports**
     * Export CSV for monthly tax declarations.


## **3.5 Compliance controls**
  * **Retention** : store invoice metadata ≥ 10 years; PDFs replicated and backed up.


  * **Security** :
    * protect tax information as **sensitive personal data** under PDPD.
    * log access to Invoice records (who, when, from where).


  * **Data localization** :
    * MISA servers are Vietnam-based; UniCore must ensure logs and copies remain in VN data centers.


* * *
# **4\. Document 2 – MoMo / VNPAY / ViettelPay / Local Bank Integration**
Goal: **one unified payment abstraction** within UniCore, with **provider-specific adapters**.
## **4.1 General payment flow pattern (Grab/Xanh SM style)**
  1. **Pre-trip** :
     * Customer selects or confirms payment method.


  2. **Trip completed** :
     * Fare is finalised.
     * UniCore creates PaymentIntent with amount, currency, method.


  3. **Gateway create payment** :
     * UniPay-Service calls specific adapter: MoMo/VNPAY/ViettelPay/Bank.
     * Adapter returns redirectUrl or deeplink (for wallet app).


  4. **Customer pays** :
     * App:
       * For wallets: opens wallet via deep link (MoMo) or webview (VNPAY QR).
       * For card/banks: opens gateway page for card info or QR.


  5. **Gateway callback** :
     * User returns to app using redirect URL (returnUrl).
     * Gateway also sends server-to-server notification (IPN/webhook) to UniPay-Service.


  6. **UniCore verifies** :
     * Verify cryptographic signature.
     * Check amount, orderId / transactionId, status.
     * Update PaymentIntent & Ride records.


  7. **Driver payout & settlement**:
     * Internal settlement engine uses gateway settlement files (T+0/T+1) → ReconciliationBatch.


This pattern is similar to how MoMo and VNPAY’s own docs describe web/mobile flows.
* * *
## **4.2 MoMo Integration (Wallet / App-to-App)**
### **4.2.1 Key parameters**
From MoMo docs (names may differ depending on product):
  * partnerCode, accessKey, secretKey


  * orderId, requestId


  * amount


  * orderInfo


  * redirectUrl (back to UniApp)


  * ipnUrl (UniCore notification)


  * extraData


  * signature (HMAC SHA256 over request fields)


### **4.2.2 Create payment**
Endpoint (internal): POST /payments/momo/create
Input:
```
    {
      "ride_id": "RIDE-123",
      "amount": 120000,
      "description": "Cuoc phi UniTaxi 123",
      "lang": "vi"
    }
```
Steps:
  1. Validate ride is finished, not yet paid.


  2. Generate:
     * orderId = "UTX-" \+ ride_id + "-" \+ timestamp
     * requestId = UUID.


  3. Build MoMo payload with fields above.


  4. Compute signature using secretKey.


  5. Call MoMo create/payment endpoint.


  6. On success, MoMo returns payUrl or deeplink URL.


  7. Save PaymentTransaction with status PENDING_GATEWAY, store orderId, requestId.


UniApp:
  * Opens payUrl in:
    * mobile browser / in-app webview, or
    * deep link to MoMo app for app-to-app experience (similar to Grab).


### **4.2.3 Callback handling**
### **a) Customer redirect**
  * MoMo redirects user to redirectUrl with query params (orderId, resultCode, message, signature, …).


  * App loads your redirectUrl route (via webview).


  * Backend verifies signature again and shows success/failure screen to user.


### **b) IPN (server-to-server)**
MoMo calls ipnUrl with JSON:
  * Contains orderId, amount, resultCode, transId, signature, etc.


UniCore:
  1. Verify signature with secretKey.


  2. Look up PaymentTransaction by orderId.


  3. If resultCode == 0 (success):
     * mark PaymentTransaction.status = SUCCESS;
     * mark PaymentIntent.status = SUCCEEDED;
     * set Ride.payment_status = PAID_NONCASH.


  4. If failure:
     * mark as FAILURE, keep reason.


  5. Idempotency: ignore duplicate IPNs by checking existing status.


* * *
## **4.3 VNPAY Integration (QR / Card / Bank)**
VNPAY is commonly used by VN platforms; integration pattern is **redirect with signed query**.
### **4.3.1 Key parameters**
Common fields:
  * vnp_Version


  * vnp_TmnCode


  * vnp_Amount (×100 per docs)


  * vnp_Command (pay)


  * vnp_CreateDate


  * vnp_CurrCode (VND)


  * vnp_IpAddr


  * vnp_Locale (vn)


  * vnp_OrderInfo


  * vnp_OrderType


  * vnp_ReturnUrl (back to app)


  * vnp_TxnRef (your order ref)


  * vnp_SecureHash (HMAC over query string)


### **4.3.2 Create payment**
Endpoint: POST /payments/vnpay/create
Steps:
  1. Similar to MoMo, but:
     * build query parameters,
     * sort and concatenate as required,
     * compute vnp_SecureHash.


  2. Redirect URL:
     * paymentUrl = vnp_Url + "?" \+ queryString + "&vnp_SecureHash=" \+ hash.


  3. Return to app for webview open.


### **4.3.3 ReturnUrl + IPN**
  * VNPAY hits ReturnUrl in browser with back query.


  * Also call **IPN URL** server-to-server with transaction status.


UniCore:
  1. Verify vnp_SecureHash.


  2. Validate vnp_Amount vs internal.


  3. Map vnp_ResponseCode:
     * 00 = success.


  4. Update PaymentTransaction and PaymentIntent same as MoMo.


* * *
## **4.4 ViettelPay Integration**
ViettelPay (or Viettel Money) exposes similar REST APIs:
  * Create transaction → receive transaction code + redirect URL.


  * Customer pays in app or via OTP.


  * ViettelPay notifies result via callback.


Integration pattern:
  1. UniCore builds signed request (appId, partnerCode, amount, orderCode, callbackUrl, …).


  2. Uses HTTPS POST to ViettelPay gateway.


  3. Receives paymentUrl.


  4. App opens paymentUrl.


  5. ViettelPay sends callback to UniPay-Service with signed payload.


  6. UniCore verifies signature and updates status.


The exact field names & signature algorithms must follow ViettelPay’s partner document, but you keep **the same internal abstraction** as for MoMo/VNPAY.
* * *
## **4.5 Local bank / card payments (Napas / Internet banking)**
Usually provided through:
  * VNPAY Card/ATM product, or


  * another PGW using **Napas 2.0** switching standard.


Pattern:
  1. UniCore calls PGW with:
     * transaction info,
     * selected bank code,
     * callback URLs.


  2. PGW:
     * shows bank login page or QR.


  3. Bank authenticates and authorizes.


  4. PGW sends result to UniCore IPN.


Implementation in UniCore:
  * Treat as **CARD_BANK method** but reuse the **VNPAY-style adapter** :
    * same internal createPayment, handleCallback, mapStatus.


* * *
## **4.6 Internal APIs (uni pay service)**
Define a **provider-agnostic** interface:
```
    interface PaymentProvider {
      createPayment(intent: PaymentIntent): Promise<CreatePaymentResult>;
      handleCallback(payload: any): PaymentResult;
      handleIpn(payload: any): PaymentResult;
    }
```
Where:
```
    type CreatePaymentResult = {
      payment_transaction_id: string;
      redirect_url: string;
      provider_metadata: any;
    };
    
    type PaymentResult = {
      payment_transaction_id: string;
      status: "SUCCESS" | "FAILURE";
      provider_txn_id?: string;
      error_code?: string;
      raw_payload: any;
    };
```
Concrete adapters:
  * MomoProvider


  * VnpayProvider


  * ViettelPayProvider


  * BankProvider (could wrap VNPAY card product)


* * *
## **4.7 Reconciliation & settlement**
### **4.7.1 Daily process (T+0 / T+1)**
For each provider:
  1. **Download settlement file** (CSV, Excel, API) for previous day.


  2. Import into ReconciliationBatch with fields:
     * provider_txn_id
     * merchant_order_id (orderId/TxnRef)
     * amount
     * fee
     * net_amount
     * status
     * payout_date


  3. Match against internal PaymentTransaction:
     * **FULL MATCH** : amount & status align → mark RECONCILED.
     * **MISMATCH** : log for manual investigation.


  4. Generate summary per day:
     * total collected,
     * total fees,
     * net to UniPower,
     * net to drivers (if using split-payment via future feature).


### **4.7.2 Audit & logging**
  * Every change of payment status must keep:
    * old_status, new_status,
    * actor (system/cron/admin),
    * source (IPN, admin fix, manual adjustment).


  * Logs kept ≥ 5 years.


* * *
## **4.8 Security & Infosec**
Consistent with your Canberra-level Infosec background:
  * **Key management**
    * partner keys (secretKey, certificates) stored in HSM or at least encrypted at rest.
    * Rotation plan with very limited staff access.


  * **Network**
    * restrict payment callback endpoints by IP allow-list where provider supports.


  * **Data**
    * Never store full card PAN or CVV (handled by PGWs).
    * Store only masked card numbers for display.


  * **Monitoring**
    * Alert when:
      * unusually high failure rate per provider,
      * bursts of small repeated payments,
      * abnormal refund activity.


* * *
## **4.9 Edge cases / flows**
  * **Payment timeout**
    * If IPN not received within X minutes:
      * mark PaymentIntent as PENDING_REVIEW.
      * show message: “Hệ thống chưa nhận được kết quả thanh toán. Vui lòng kiểm tra lại trong Lịch sử chuyến đi.”


  * **Customer pays but app closed**
    * Rely solely on IPN → update backend → trip history shows paid.


  * **Partial refunds**
    * Implement Refund entity with mapping to provider’s refund API when available.


  * **Disputes**
    * Store all gateway payloads exactly as received for evidence.


* * *
## **1\. MoMo Payment Flow (App-to-App)**
```
    sequenceDiagram
        participant User as User (UniApp)
        participant App as UniApp Backend
        participant Pay as UniPay-Service
        participant MoMo as MoMo Gateway
    
        User->>App: End ride → request non-cash payment (MoMo)
        App->>Pay: createPayment(ride_id, amount, method=MoMo)
    
        Pay->>Pay: Create PaymentIntent + PaymentTransaction (PENDING_GATEWAY)
        Pay->>MoMo: POST /payment (partnerCode, orderId, amount, redirectUrl, ipnUrl, signature)
        MoMo-->>Pay: payUrl / deeplink
    
        Pay-->>App: redirect_url (payUrl)
        App-->>User: Open MoMo app/webview with payUrl
    
        User->>MoMo: Confirm payment (PIN/OTP)
        MoMo-->>User: Payment result screen
    
        %% Browser redirect
        MoMo-->>App: Redirect to redirectUrl (orderId, resultCode, signature)
        App->>Pay: handleRedirect(orderId, resultCode,...)
    
        %% Server-to-server IPN
        MoMo-->>Pay: IPN to ipnUrl(orderId, amount, resultCode, transId, signature)
        Pay->>Pay: Verify signature & amount
    
        alt resultCode == 0 (success)
            Pay->>Pay: Update PaymentTransaction=SUCCESS<br/>PaymentIntent=SUCCEEDED
            Pay->>App: Notify ride paid (non-cash)
            App-->>User: Show "Thanh toán MoMo thành công"
        else failure
            Pay->>Pay: Update PaymentTransaction=FAILURE
            Pay->>App: Notify payment failed
            App-->>User: Show failure + options (retry / cash)
        end
```
* * *
## **2\. VNPAY (QR / Card / Bank) Flow**
```
    sequenceDiagram
        participant User as User (UniApp)
        participant App as UniApp Backend
        participant Pay as UniPay-Service
        participant VNPAY as VNPAY Gateway
    
        User->>App: End ride → choose VNPAY (QR/Card/Bank)
        App->>Pay: createPayment(ride_id, amount, method=VNPAY)
    
        Pay->>Pay: Create PaymentIntent + PaymentTransaction (PENDING_GATEWAY)
        Pay->>Pay: Build vnp_* params + vnp_SecureHash
        Pay->>VNPAY: Redirect URL (browser/webview open with params)
        VNPAY-->>User: Show QR / card form / bank list
    
        User->>VNPAY: Pay via QR scan / bank auth
        VNPAY-->>User: Show result
    
        %% Browser return
        VNPAY-->>App: Redirect to vnp_ReturnUrl(vnp_TxnRef, vnp_ResponseCode, vnp_SecureHash,...)
        App->>Pay: handleReturn(vnp_*)
    
        %% IPN
        VNPAY-->>Pay: IPN(vnp_TxnRef, vnp_ResponseCode, vnp_SecureHash,...)
        Pay->>Pay: Verify signature + amount
    
        alt vnp_ResponseCode == "00"
            Pay->>Pay: PaymentTransaction=SUCCESS<br/>PaymentIntent=SUCCEEDED
            Pay->>App: Notify ride paid
            App-->>User: Show "Thanh toán VNPAY thành công"
        else
            Pay->>Pay: PaymentTransaction=FAILURE
            Pay->>App: Notify payment failed
            App-->>User: Show failure + options (retry / cash)
        end
```
* * *
## **3\. ViettelPay Flow (same abstraction)**
```
    sequenceDiagram
        participant User as User (UniApp)
        participant App as UniApp Backend
        participant Pay as UniPay-Service
        participant VT as ViettelPay Gateway
    
        User->>App: End ride → choose ViettelPay
        App->>Pay: createPayment(ride_id, amount, method=ViettelPay)
    
        Pay->>Pay: Create PaymentIntent + PaymentTransaction
        Pay->>VT: POST /createTransaction(appId, orderCode, amount, callbackUrl, signature)
        VT-->>Pay: paymentUrl
    
        Pay-->>App: redirect_url(paymentUrl)
        App-->>User: Open ViettelPay app/webview
    
        User->>VT: Confirm payment
        VT-->>User: Show result
    
        VT-->>Pay: Callback(orderCode, resultCode, signature)
        Pay->>Pay: Verify signature + amount
    
        alt resultCode == SUCCESS
            Pay->>Pay: PaymentTransaction=SUCCESS<br/>PaymentIntent=SUCCEEDED
            Pay->>App: Notify ride paid
            App-->>User: Show success
        else
            Pay->>Pay: PaymentTransaction=FAILURE
            Pay->>App: Notify failure
            App-->>User: Show failure + options
        end
```
* * *
## **4\. MISA E-Invoice Flow (after successful non-cash payment)**
```
    sequenceDiagram
        participant User as User (UniApp)
        participant App as UniApp Backend
        participant Core as UniCore-API
        participant MISA as MISA eInvoice
    
        User->>App: Open trip detail → Tap "Yêu cầu hóa đơn"
        App->>Core: POST /invoices/request(ride_id, buyer info)
    
        Core->>Core: Validate ride & payment SUCCEEDED
        Core->>Core: Create InvoiceRequest (status=PENDING)
    
        Note over Core: Invoice job / service
    
        Core->>MISA: CreateInvoice(InvoiceRequest mapped → MISA format)
        MISA-->>Core: Response(success: invoiceNo, series, issueDate, pdfLink<br/>or failure: errorCode, message)
    
        alt success
            Core->>Core: Update InvoiceRequest=ISSUED<br/>store MISA metadata
            Core-->>App: invoice_status=ISSUED, pdf_url
            App-->>User: Show "Đã phát hành" + button "Tải hóa đơn"
            User->>App: Download / view PDF (via Core proxy or MISA link)
        else failure
            Core->>Core: InvoiceRequest=FAILED, store error
            Core-->>App: invoice_status=FAILED, reason
            App-->>User: Show message “Không phát hành được hóa đơn, vui lòng liên hệ CSKH”
        end
```
* * *
## **5\. Full Ride → Pay → Invoice Overview**
```
    sequenceDiagram
        participant User as User (UniApp)
        participant Driver as Driver App
        participant Core as UniCore-API
        participant Pay as UniPay-Service
        participant PGW as Payment Gateway (MoMo/VNPAY/VT)
        participant MISA as MISA eInvoice
    
        User->>Core: Request ride
        Core-->>Driver: Offer ride
        Driver-->>Core: Accept
        Note over User,Driver: Trip in progress
    
        Driver->>Core: End trip (distance/time)
        Core->>Core: Compute fare, create Ride
        User->>Core: Confirm payment method (wallet/card/cash)
    
        alt Non-cash
            Core->>Pay: createPayment(ride_id, amount, method)
            Pay->>PGW: Create transaction
            PGW-->>User: Payment UI
            User->>PGW: Confirm payment
            PGW-->>Pay: IPN result
            Pay->>Core: Payment SUCCEEDED
            Core-->>User: Show paid status
    
            User->>Core: Request invoice
            Core->>MISA: CreateInvoice(...)
            MISA-->>Core: Invoice issued
            Core-->>User: Link PDF / view
        else Cash
            Core->>Core: Mark Ride as CASH_DUE
            Driver->>User: Collect cash
            Driver->>Core: Confirm collected
            Core-->>User: Trip marked paid (cash)
            opt Cash invoice
                User->>Core: Request invoice (cash)
                Core->>MISA: CreateInvoice(...)
                MISA-->>Core: Invoice issued
                Core-->>User: Link PDF
            end
        end
```
\--- **Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[security_MOC]]
