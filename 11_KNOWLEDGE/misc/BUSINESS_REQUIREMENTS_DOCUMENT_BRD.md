---
title: BUSINESS REQUIREMENTS DOCUMENT BRD
tags:
- misc
- reference
- general
- canon/knowledge
type: document
source: 11_KNOWLEDGE/misc
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


# **BUSINESS REQUIREMENTS DOCUMENT (BRD)**
# **Rider App (Khách hàng)**
## **1) Chức năng bắt buộc**
  * **Đăng ký/Đăng nhập** : OTP qua SMS; lưu hồ sơ cơ bản (tên, SĐT).


  * **Định vị & bản đồ**: tự động lấy vị trí hiện tại; chọn điểm đón/trả; gợi ý địa điểm gần.


  * **Ước tính giá & hiển thị giá cố định**: hiện _tổng giá_ trước khi đặt (km + phút + phụ phí cố định nếu có).


  * **Đặt xe tức thì** : tạo cuốc; nhận trạng thái theo thời gian thực (đang tìm tài xế → tài xế nhận → đang tới → đang chở → hoàn thành).


  * **Theo dõi tài xế** : hiển thị biển số, ảnh/ tên tài xế, ETA, vị trí trực tiếp.


  * **Thanh toán** : tiền mặt + ví điện tử (VNPay/MoMo/ZaloPay) + thẻ (nếu có); biên lai điện tử.


  * **Hủy cuốc** : hủy trước khi tài xế đến/đón (áp dụng phí hủy rõ ràng nếu vượt ngưỡng).


  * **Đánh giá & phản hồi**: chấm sao và góp ý nhanh sau chuyến.


  * **Lịch sử chuyến đi** : xem lại chi tiết cuốc và biên lai.


  * **Hỗ trợ nhanh** : nút trợ giúp/cuộc gọi ẩn số tới CS.


## **2) Màn hình tối thiểu**
  * Onboarding/OTP • Trang chính (map) • Chọn điểm đến • Chi tiết giá • Trạng thái cuốc • Thanh toán • Đánh giá • Lịch sử • Hỗ trợ.


## **3) Tiêu chí chấp nhận (Acceptance)**
  * Đặt cuốc → ghép tài xế thành công trong ≤60 giây (khi có tài xế gần).


  * Giá hiển thị trước = giá thanh toán (sai số tính theo mét/giây < 2%).


  * Đường truyền kém: vẫn thao tác cơ bản, tự đồng bộ khi mạng ổn định.


  * Ứng dụng khởi chạy < 3 giây trên Android tầm trung.


* * *
# **‍✈️ Driver App (Tài xế)**
## **1) Chức năng bắt buộc**
  * **Đăng nhập** : OTP; kiểm tra trạng thái kích hoạt (đã duyệt hồ sơ).


  * **Bật/Tắt nhận cuốc (Trực tuyến/Ngoại tuyến)**.


  * **Hàng đợi cuốc & nhận cuốc**: xem chi tiết điểm đón/trả, ước tính cước & thời gian; bấm _Nhận_.


  * **Điều hướng** : mở điều hướng (Google/Apple Maps) tới điểm đón & tới điểm trả.


  * **Trạng thái chuyến** : _Đến điểm đón_ → _Đã đón khách_ → _Kết thúc chuyến_.


  * **Thu nhập cơ bản** : tổng doanh thu ngày/tuần; số cuốc/giờ; phí/chiết khấu hiển thị rõ.


  * **Hủy cuốc theo quy định** : chọn lý do; log lại.


  * **Lịch sử chuyến** : chi tiết từng cuốc (km, phút, giá, chia sẻ doanh thu).


  * **Hỗ trợ nhanh** : gọi CS; báo cáo sự cố.


_(Nếu là EV: có thể thêm hiển thị % pin và trạm sạc gần nhất — nhưng không bắt buộc cho bản tối thiểu.)_
## **2) Màn hình tối thiểu**
  * OTP/Đăng nhập • Bật/Tắt nhận cuốc • Danh sách/Pop-up cuốc mới • Điều hướng • Trạng thái chuyến • Thu nhập • Lịch sử • Hỗ trợ.


## **3) Tiêu chí chấp nhận (Acceptance)**
  * Nhận thông báo cuốc mới trong ≤2 giây từ lúc dispatch gửi.


  * Quy trình: Nhận cuốc → Điều hướng → Kết thúc → Đồng bộ doanh thu hoàn tất < 5 giây.


  * App vẫn hiển thị trạng thái và lưu log tạm khi mất mạng ngắn (≤2 phút), tự đồng bộ lại.


* * *
# **Nền tảng chung (cho cả 2 app)**
## **API bắt buộc (tối thiểu)**
  * **Auth** : /otp/send, /auth/verify


  * **Rider** : /rides/quote, /rides/create, /rides/status/{id}, /rides/cancel/{id}


  * **Driver** : /driver/status (online/offline), /driver/jobs/next, /driver/jobs/accept/{id}, /driver/jobs/arrive/{id}, /driver/jobs/start/{id}, /driver/jobs/complete/{id}, /driver/job/cancel/{id}


  * **Payments** : /payment/initiate, /payment/callback, /receipt/{rideId}


  * **Profiles** : /me, /driver/me, /history/rides


## **Luồng lõi (happy path)**
  1. Rider: mở app → định vị → nhập điểm đến → xem giá → đặt → ghép driver → theo dõi → thanh toán → đánh giá.


  2. Driver: online → nhận cuốc → đến điểm đón → đón khách → kết thúc → thu nhập cập nhật.


## **Edge cases cần xử lý**
  * Không tìm thấy tài xế: hiển thị _thử lại_ hoặc gợi ý thời gian/điểm đón khác.


  * Tài xế hủy giữa chừng: tự động gán lại tài xế gần nhất; rider được thông báo.


  * Rider hủy sát giờ: áp dụng phí hủy theo rule (rõ ràng trong biên lai).


  * Thanh toán ví lỗi: fallback sang tiền mặt; hệ thống auto-đối soát sau.


  * Mất GPS/mạng: lưu cục bộ các mốc thời gian; đồng bộ khi có mạng.


## **Bảo mật & hiệu năng**
  * OAuth2/JWT; TLS 1.3; mã hóa dữ liệu nhạy cảm.


  * Giới hạn tần suất (rate limit) các API đặt/hủy để chống lạm dụng.


  * Log/audit tối thiểu cho: tạo cuốc, nhận cuốc, hủy, thanh toán.


  * Mục tiêu: uptime ≥ 99.9%; phản hồi API < 1.5–2s.


* * *
# **Công nghệ đề xuất (nhẹ, triển khai nhanh)**
  * **Mobile** : Flutter (1 codebase cho Rider & Driver).


  * **Backend** : Node.js (NestJS), PostgreSQL, Redis.


  * **Realtime** : WebSocket/Socket.IO (trạng thái cuốc, push cuốc mới).


  * **Maps** : Google Maps SDK (geocode, directions, distance matrix).


  * **Payments** : VNPay/MoMo/ZaloPay (server-to-server callback).


  * **Deploy** : Docker + VNPT/AWS; giám sát Prometheus + Grafana.


* * *
# **️ Kế hoạch delivery gợi ý (6 tuần “đủ chạy”)**
  * **Tuần 1–2** : Auth + Map + Quote + Create Ride; Driver online/offline + nhận cuốc cơ bản.


  * **Tuần 3–4** : Trạng thái chuyến trọn vẹn, realtime; lịch sử/biên lai; thu nhập tài xế; hủy & phí hủy.


  * **Tuần 5** : Tích hợp thanh toán ví; hardening hiệu năng; QA end-to-end.


  * **Tuần 6** : Pilot live 200–500 xe; fix lỗi; chuẩn bị mở rộng.


* * *
# **Tiêu chí “xong” (Definition of Done – bản tối thiểu)**
  * Đặt – nhận – hoàn thành cuốc **ổn định** ; tỷ lệ lỗi < 1%/1000 cuốc.


  * Giá hiển thị trước khớp giá thu tiền; biên lai tự sinh.


  * Tài xế online ≥ 2 giờ mà không crash; pin & dữ liệu nền tối ưu.


  * Kênh hỗ trợ phản hồi < 5 phút (hotline/in-app call).


* * *
\
Tuyệt vời — dưới đây là **bản yêu cầu đã bổ sung** (giữ cấu trúc MVP, thêm các hạng mục pháp lý, an toàn, khả dụng, và hook EV). Phần mới được đánh dấu **[MỚI]** để đội dev/QA nắm rõ phạm vi tăng thêm.
* * *
# **Rider App (Khách hàng)**
## **1) Chức năng bắt buộc**
  * **Đăng ký/Đăng nhập** : OTP qua SMS; lưu hồ sơ cơ bản (tên, SĐT).


  * **Định vị & bản đồ**: tự động lấy vị trí hiện tại; chọn điểm đón/trả; gợi ý địa điểm gần.


  * **Ước tính giá & hiển thị giá cố định**: hiện _tổng giá_ trước khi đặt (km + phút + phụ phí cố định nếu có).
**[MỚI]** Hiển thị **thuế VAT** và tổng thanh toán sau thuế.


  * **Đặt xe tức thì** : tạo cuốc; nhận trạng thái theo thời gian thực (đang tìm tài xế → tài xế nhận → đang tới → đang chở → hoàn thành).


  * **Theo dõi tài xế** : hiển thị biển số, ảnh/tên tài xế, ETA, vị trí trực tiếp.


  * **Thanh toán** : tiền mặt + ví điện tử (VNPay/MoMo/ZaloPay) + thẻ (nếu có); **biên lai điện tử**.
**[MỚI]** **Yêu cầu xuất Hóa đơn điện tử (HĐĐT)** : toggle “Xuất HĐ công ty”; nhập **MST, Tên Cty, Địa chỉ, Email nhận HĐ** ; lưu “hồ sơ người mua” cho lần sau.
**[MỚI]** Nhận **link tải HĐĐT (PDF/XML)** trong lịch sử chuyến; thông báo “HĐ sẽ gửi sau” nếu đang chờ phát hành.


  * **Hủy cuốc** : hủy trước khi tài xế đến/đón (áp dụng phí hủy rõ ràng nếu vượt ngưỡng).


  * **Đánh giá & phản hồi**: chấm sao và góp ý nhanh sau chuyến.
**[MỚI]** Báo cáo sự cố/đồ thất lạc (lost & found) kèm ảnh.


  * **Lịch sử chuyến đi** : xem chi tiết cuốc và biên lai.
**[MỚI]** Tải **HĐĐT** ; yêu cầu **điều chỉnh thông tin hóa đơn** trong 24h (nếu nhà cung cấp HĐĐT cho phép).


  * **Hỗ trợ nhanh** : nút trợ giúp/cuộc gọi ẩn số tới CS.
**[MỚI]** **SOS** : gọi khẩn + gửi vị trí GPS tức thời (ẩn số) tới hotline/bên an ninh.


## **2) Màn hình tối thiểu**
  * Onboarding/OTP • Trang chính (map) • Chọn điểm đến • Chi tiết giá • Trạng thái cuốc • Thanh toán • Đánh giá • Lịch sử • Hỗ trợ.
**[MỚI]** **Form HĐĐT** (MST/Tên Cty/Địa chỉ/Email) • **Màn Hóa đơn** (xem/tải PDF, XML) • **Màn SOS** (xác nhận gọi khẩn + chia sẻ vị trí).


## **3) Tiêu chí chấp nhận (Acceptance)**
  * Đặt cuốc → ghép tài xế thành công trong ≤60 giây (khi có tài xế gần).


  * Giá hiển thị trước = giá thanh toán (sai số tính theo mét/giây < 2%).
**[MỚI]** VAT hiển thị đúng theo cấu hình thuế hiện hành.


  * Đường truyền kém: vẫn thao tác cơ bản, tự đồng bộ khi mạng ổn định.
**[MỚI]** **Lưu tạm dữ liệu chuyến & yêu cầu HĐĐT** khi offline ≤2 phút; không mất dữ liệu sau khi kết nối lại.


  * Ứng dụng khởi chạy < 3 giây trên Android tầm trung.
**[MỚI]** Bấm “Xuất HĐĐT” → nhận email/SMS link hoặc thấy trạng thái “đang phát hành” trong ≤2 phút.


* * *
# **‍✈️ Driver App (Tài xế)**
## **1) Chức năng bắt buộc**
  * **Đăng nhập** : OTP; kiểm tra trạng thái kích hoạt (đã duyệt hồ sơ).
**[MỚI]** **Chặn phiên đăng nhập trùng** (không cho 2 thiết bị hoạt động song song).


  * **Bật/Tắt nhận cuốc (Trực tuyến/Ngoại tuyến)**.
**[MỚI]** **Tạm nghỉ ngắn** (break 15’): không nhận cuốc nhưng giữ online cho đối soát.


  * **Hàng đợi cuốc & nhận cuốc**: xem chi tiết điểm đón/trả, ước tính cước & thời gian; bấm _Nhận_.


  * **Điều hướng** : mở điều hướng (Google/Apple Maps) tới điểm đón & tới điểm trả.


  * **Trạng thái chuyến** : _Đến điểm đón_ → _Đã đón khách_ → _Kết thúc chuyến_.
**[MỚI]** Log **bằng chứng đón khách** (1 chạm; tùy chọn ảnh/ghi chú nếu chính sách yêu cầu).


  * **Thu nhập cơ bản** : tổng doanh thu ngày/tuần; số cuốc/giờ; phí/chiết khấu hiển thị rõ.
**[MỚI]** Tách **doanh thu trước VAT / sau VAT** (nếu tài xế là tổ chức chịu VAT).


  * **Hủy cuốc theo quy định** : chọn lý do; log lại.


  * **Lịch sử chuyến** : chi tiết từng cuốc (km, phút, giá, chia sẻ doanh thu).


  * **Hỗ trợ nhanh** : gọi CS; báo cáo sự cố.
**[MỚI]** **SOS** : gọi khẩn + gửi GPS tới hotline.
**[MỚI – EV (khuyến nghị)]** Hiển thị **% pin** và **trạm sạc UniPower gần nhất** khi pin < ngưỡng (hook EV, có thể tắt/bật theo khu vực).


## **2) Màn hình tối thiểu**
  * OTP/Đăng nhập • Bật/Tắt nhận cuốc • Danh sách/Pop-up cuốc mới • Điều hướng • Trạng thái chuyến • Thu nhập • Lịch sử • Hỗ trợ.
**[MỚI]** **SOS** • **Break Mode** • **Cảnh báo pin thấp/Trạm sạc** (EV – tùy chọn).


## **3) Tiêu chí chấp nhận (Acceptance)**
  * Nhận thông báo cuốc mới trong ≤2 giây từ lúc dispatch gửi.


  * Quy trình: Nhận cuốc → Điều hướng → Kết thúc → Đồng bộ doanh thu hoàn tất < 5 giây.


  * App vẫn hiển thị trạng thái và lưu log tạm khi mất mạng ngắn (≤2 phút), tự đồng bộ lại.
**[MỚI]** Không cho đăng nhập đồng thời 2 thiết bị; nếu phát hiện → buộc đăng xuất thiết bị cũ.


* * *
# **Yêu cầu nền tảng bổ sung (Backend/Compliance) — [MỚI]**
## **A) Hóa đơn điện tử (bắt buộc pháp lý khi UniPower thu tiền)**
  * Tích hợp API nhà cung cấp HĐĐT (MISA/Viettel/FPT/VNPT/BKAV…).


  * Truyền **buyer profile** (MST/Tên/Địa chỉ/Email) nếu khách chọn “Xuất HĐ công ty”.


  * Nhận **invoice_id, số hóa đơn, pdf/xml url, qrcode** ; lưu trữ ≥5 năm.


  * **Đồng bộ Tổng cục Thuế** : theo dõi trạng thái queued/sent/accepted/rejected; tự retry; log mã lỗi.


  * Cho phép **điều chỉnh/huỷ hóa đơn** đúng quy trình khi hoàn tiền/hủy cuốc sau phát hành.


## **B) An toàn & pháp lý**
  * **SOS Gateway** : định tuyến cuộc gọi khẩn + đính kèm tọa độ; ghi lại log thời gian thực.


  * **Bảo vệ dữ liệu cá nhân (PII)** : mã hóa at-rest/in-transit; ẩn số khi gọi; xóa/ẩn thông tin nhạy cảm trên màn hình lock.


  * **Chống gian lận** : chặn đa phiên, phát hiện vị trí giả (mock location), kiểm tra bất thường dòng cuốc.


  * **Điều khoản & Chính sách**: màn **Điều khoản sử dụng/Chính sách bảo mật** trước khi sử dụng; checkbox đồng ý.


## **C) Khả dụng & vận hành**
  * **Offline resilience** : hàng đợi sự kiện (trip state, payment, invoice request) để đồng bộ lại khi có mạng.


  * **Observability** : log tập trung, trace giao dịch (trip → payment → invoice) để đối soát 100%.


  * **UniPortal (ops)** : bảng điều khiển thời gian thực (cuốc đang chạy, heatmap nhu cầu, tình trạng driver); xuất **Báo cáo VAT** hàng tháng.


## **D) Hook EV (khuyến nghị bật theo khu vực)**
  * API **UniPower Charging** : gợi ý trạm sạc theo SOC, công suất, tình trạng sẵn sàng.


  * Cảnh báo **SOC thấp** khi nhận cuốc dài vượt phạm vi pin hiện tại.


* * *
# **Non-Functional & QA — [MỚI]**
  * **Hiệu năng** : P95 API chính ≤ 300 ms; P99 ≤ 800 ms.


  * **Độ tin cậy** : Uptime ≥ 99.9% cho Dispatch/Payment/Billing.


  * **Bảo mật** : Pentest không rò rỉ PII/thuế; rate limit & WAF.


  * **Kiểm thử bắt buộc** :
    * **Offline >2 phút** không mất dữ liệu chuyến & yêu cầu HĐĐT.
    * **Giao dịch nhiều phương thức** (mixed payments) vẫn phát hành 1 HĐĐT tổng.
    * **GDT rejected** → hiển thị pending, retry thành công trong 24h.


* * *
# **UniPower Referral & Revenue-Sharing System (3% Lifetime Benefit)**
## **1\. Purpose & Overview**
The referral system is designed to **reward UniPower members** (drivers, riders, or partners) who help expand the UniPower ecosystem.
Each member receives **3% of the net profit** generated by any user they refer — **for as long as both remain active** in the system.
This program incentivises organic growth while keeping full transparency, automation, and legal compliance with Vietnamese tax law.
* * *
## **2\. Core Structure**
### **Referral Logic**
  * Every registered user automatically receives:
    * A **unique referral code** (e.g., UNI1234)
    * A **referral QR code** (e.g., https://unipower.vn/r/UNI1234)


  * When a new user registers via **QR scan** or **referral code** , the backend records a **referral link** :


```
    referrer_id → referee_id
```
  * 

  * The referral relationship is **one-time and permanent**.


  * The referrer earns **3% of UniPower’s net profit** generated by the referred member’s activities (rides, transactions, partnerships) as long as both accounts remain active.


* * *
## **3\. Financial Flow**
### **Profit Base for Reward Calculation**
  * The 3% benefit is calculated from **UniPower’s retained net profit portion** , not from the total transaction amount.
Example:


```
    Rider pays 100,000₫
    Driver receives 85,000₫
    UniPower retains 15,000₫ (net profit portion)
    → Referrer earns 3% × 15,000₫ = 450₫
```
### **Reward Trigger**
  * Generated automatically at the time of **trip settlement** (for drivers) or **invoice confirmation** (for riders or partners).


  * Stored in the user’s **Referral Wallet** inside the UniPower app.


### **Payout & Settlement**
  * Minimum withdrawal threshold: e.g., **100,000₫**.


  * Payout methods: internal UniWallet → VNPay / MoMo / bank transfer.


  * Cycle: **Monthly automatic settlement** or **manual withdrawal** by the user.


* * *
## **4\. Referral Identification Options**
|                          |
| **Option**               | **Description**                                         | **Pros**                                      | **Cons**                    |
|--------------------------|---------------------------------------------------------|-----------------------------------------------|-----------------------------|
| **QR-based referral**    |  Each user shares a QR code for others to scan          | Seamless onboarding, strong offline usability | Requires camera permissions |
| **Referral code**        |  User manually enters the referrer’s code during signup | Very easy to implement                        | Typing errors possible      |
| **Hybrid (Recommended)** |  QR automatically fills the code; code entry as backup  | Best UX, works both online & offline          | Slightly more backend logic |


✅ **Recommended for MVP:** Hybrid model — generate both a **code and QR** per user.
  * The referral QR is a short URL (e.g., https://unipower.vn/signup?ref=UNI1234).


  * When the app opens with a referral parameter, the backend links the referrer and referee automatically.


* * *
## **5\. Database Schema (Simplified)**
**Table: users**
|               |
| **Field**     | **Type** | **Description**          |
|---------------|----------|--------------------------|
| id            | INT      | User ID                  |
| name          | VARCHAR  | Full name                |
| phone         | VARCHAR  | Login ID                 |
| referral_code | VARCHAR  | Unique referral code     |
| referrer_id   | INT      | ID of referring user     |
| role          | ENUM     | Rider / Driver / Partner |
| active        | BOOLEAN  | Account status           |


**Table: referral_rewards**
|                |
| **Field**      | **Type** | **Description**                |
|----------------|----------|--------------------------------|
| id             | INT      | Reward record ID               |
| referrer_id    | INT      | Who earned the reward          |
| referee_id     | INT      | Whose transaction triggered it |
| transaction_id | INT      | Related trip or order          |
| profit_base    | DECIMAL  | UniPower profit portion        |
| reward_amount  | DECIMAL  | 3% of profit base              |
| created_at     | DATETIME | Time of calculation            |
| status         | ENUM     | pending / paid / cancelled     |


**Table: wallet**
|                 |
| **Field**       | **Type** | **Description**              |
|-----------------|----------|------------------------------|
| id              | INT      | Wallet ID                    |
| user_id         | INT      | Linked user                  |
| balance         | DECIMAL  | Current wallet balance       |
| total_earned    | DECIMAL  | Cumulative referral earnings |
| last_withdrawal | DATETIME | Last payout date             |


* * *
## **6\. Legal & Tax Compliance (Vietnam)**
  * Referral earnings are classified as **“marketing or referral income”** under Vietnamese law.


  * UniPower must:
    * Record all referral reward transactions.
    * Deduct **5% PIT (Personal Income Tax)** for individual referrers.
    * Issue a valid **e-invoice for referral income** under UniPower’s tax ID.
    * Report referral income in the monthly tax declaration.


If the referrer is an official business entity or partner with a tax code, UniPower can settle **B2B-style payouts** with standard VAT invoices.
* * *
## **7\. App-Level Functional Requirements**
### **Rider / Driver / Partner App**
**Referral Page – “Invite Friends”**
  * Displays:
    * User’s QR code
    * Referral code
    * Share button (“Copy link” / “Share via Zalo/Facebook”)
    * Summary of total earned and active referees
    * Referral Terms & Conditions


**Signup Flow**
  * If QR scanned → app opens with referral param auto-filled.


  * If manually entered → validate code and lock-in permanently.


  * Display referrer name confirmation before finalising.


**Referral Wallet**
  * Show:
    * Total earned
    * Pending earnings
    * Transaction history
    * Withdraw button


  * Real-time balance updates (≤10 seconds after transaction confirmation).


* * *
## **8\. Backend Logic**
  1. **Registration:**
     * When referral_code detected, backend resolves to referrer_id and links new user.


  2. **Transaction Processing:**
     * When any transaction with profit occurs, fetch referrer_id.
     * Compute reward = net_profit × 0.03.
     * Create a new record in referral_rewards and update wallet balance.


  3. **Payout:**
     * When user withdraws or during monthly batch payout, deduct **5% PIT**.
     * Log transaction, issue e-invoice, and send confirmation message.


* * *
## **9\. Anti-Fraud Rules**
  * Only **one referral level** — no multi-level chains.


  * Both referrer and referee must be **active** (last login < 30 days).


  * Referee must have completed at least **one paid trip or transaction**.


  * No referral reward for self-referrals, duplicate numbers, or same device IDs.


  * Maximum reward per referred user per month: configurable (e.g., ₫200,000).


  * Referral relationship is **immutable** (cannot be changed after signup).


* * *
## **10\. Technical Summary**
|               |
| **Component** | **Description**                                            |
|---------------|------------------------------------------------------------|
| Referral Code | Auto-generated alphanumeric (Base36 from userID)           |
| Referral QR   | Short link encoded with referral param                     |
| Tracking      | Relational mapping (referrer_id → referee_id)              |
| Wallet        | Sub-ledger within UniWallet service                        |
| Admin Portal  | Dashboard: top referrers, earnings, audit logs, export CSV |
| Notification  | “You earned 3% from your referral’s activity!” push/email  |
| API Exposure  | /api/v1/referrals (link, reward, wallet, withdraw)         |


* * *
## **11\. Acceptance Criteria**
  * Each user receives a **unique code and QR** upon registration.


  * New signups via code or QR correctly link the referrer.


  * Rewards automatically calculated as **3% of UniPower’s profit portion** (accuracy < ±1₫).


  * Referral wallet updates within **10 seconds** after qualifying transaction.


  * History and payout records visible in-app and Admin Portal.


  * Duplicate or fraudulent referrals blocked at registration.


  * Tax (5% PIT) deducted and logged on every withdrawal.


  * Monthly summary export for Finance includes:
    * Total referrals, total payout, withheld PIT, outstanding balance.


* * *
## **12\. Example User Flow**
  1. Driver A shares their referral QR with friend B.


  2. B scans and registers → referrer_id = A.


  3. B starts driving, generating ₫2,000,000 in UniPower profit that month.


  4. A automatically earns ₫60,000 (3% × 2,000,000).


  5. A’s Referral Wallet updates instantly.


  6. When balance > ₫100,000, A withdraws → UniPower deducts 5% PIT → pays ₫57,000 net.


  7. Invoice generated and stored for audit.


* * *
## **13\. Optional Future Enhancements**
  * **Tiered rewards** (e.g., 3% first 6 months → 1% thereafter).


  * **Referral leaderboard** (monthly ranking with bonuses).


  * **Promo integration** (QR scan triggers ride discounts for new users).


  * **Geo-restricted campaigns** (target city or driver hub).


  * **Blockchain logging (phase 3)** for transparent audit trail of all referral rewards.


* * *
## **14\. Security & Compliance**
  * All referral data encrypted in-transit (TLS 1.2+) and at-rest (AES-256).


  * Payout actions restricted to verified accounts (KYC).


  * Session control to prevent device spoofing or shared credentials.


  * Monthly referral ledger archived for 5 years (tax audit requirement).


  * GDPR-style user consent for marketing and referral participation.


* * *
## **15\. Summary**
|                       |
| **Category**          | **Status** | **Notes**                          |
|-----------------------|------------|------------------------------------|
| Legal compliance      | ✅          | Follows VN tax & invoice laws      |
| Technical scalability | ✅          | Single-level model; low complexity |
| Payout automation     | ✅          | Wallet-based, easy reconciliation  |
| Fraud prevention      | ✅          | One-level link, KYC, active check  |
| UX simplicity         | ✅          | QR + code hybrid onboarding        |
| Viral potential       | ✅          | Encourages organic user growth     |


* * *
### **Final Recommendation**
Implement the **Hybrid Referral Model (QR + Code)** with:
  * 3% lifetime profit share,


  * automatic wallet accrual,


  * 5% tax withholding,


  * real-time notifications,


  * fully auditable payout ledger.


This achieves **high viral growth** , **legal compliance** , and **financial transparency** — perfectly aligned with UniPower’s ethical and scalable ecosystem.
* * *
\--- **Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
