---
title: POS REPLACEMENT
tags: [misc, reference, general, canon/knowledge]
type: document
source: 11_KNOWLEDGE/misc
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


# Pos replacement
Chính xác — và đây là điểm quan trọng mà nhiều startup thanh toán ở Việt Nam **bỏ sót** khi thay thế POS.
Dưới đây là giải thích chi tiết và **hướng xử lý đúng quy định pháp luật Việt Nam** (theo Nghị định 123/2020/NĐ-CP và Thông tư 78/2021/TT-BTC):
* * *
### ️ **1. Vấn đề pháp lý**
Các hình thức thanh toán QR, ví điện tử (MoMo, ZaloPay, VNPay…) **chỉ là phương tiện thanh toán** , **không phải công cụ phát hành hóa đơn**.
  * Khi khách quét QR và thanh toán thành công, hệ thống chỉ ghi nhận **biên lai giao dịch điện tử (transaction receipt)**.


  * Theo quy định, doanh nghiệp vẫn phải **phát hành hóa đơn điện tử hợp lệ (e-invoice)** thông qua **tổ chức trung gian được Tổng cục Thuế cấp phép** như:
    * **MISA meInvoice**
    * **Viettel Invoice**
    * **FPT.eInvoice**
    * **CyberLotus e-Invoice**
    * **VNPT Invoice**


* * *
### ️ **2. Giải pháp tích hợp chuẩn**
Cách hợp pháp và tối ưu cho UniTaxi là **kết hợp 2 tầng:**
### **Tầng 1 – Thanh toán**
  * Dùng **VNPay QR / MoMo / ZaloPay / FPT Pay** làm **phương thức thanh toán**.


  * Dòng tiền đi thẳng về tài khoản doanh nghiệp UniPower.


### **Tầng 2 – Xuất hóa đơn tự động**
  * Sau khi thanh toán thành công, **app UniTaxi gọi API của MISA hoặc Viettel Invoice**.


  * API này tự động tạo **hóa đơn điện tử hợp lệ** , ký số theo mã doanh nghiệp, và gửi **file PDF + mã tra cứu** cho khách qua email/Zalo.


✅ **Hóa đơn này hợp pháp, lưu thông qua hệ thống thuế.**
* * *
### **3. Kết luận – Giải pháp khuyến nghị cho UniPower**
> Không cần máy POS, nhưng vẫn xuất hóa đơn hợp lệ nếu triển khai theo mô hình:
> **VNPay QR / MoMo (thanh toán)** → **MISA hoặc Viettel Invoice (hóa đơn điện tử)**.
  * Giao dịch **vẫn hợp pháp** , **tiện lợi** , và **không vi phạm quy định thuế**.


  * Hệ thống **hoàn toàn tự động** và **minh bạch khi kiểm toán**.


  * Tiết kiệm **40–60% chi phí so với vận hành POS**.


* * *
Bạn có muốn mình viết giúp một **đoạn đề xuất chính thức** (để bạn gửi vào nhóm Ban Điều Hành UniPower hoặc cho CEO phê duyệt hướng này) không?
→ Nội dung sẽ gãy gọn, chuẩn phong cách CTO, đề xuất triển khai _“Thanh toán QR + Xuất hóa đơn điện tử API”_.
Dưới đây là **đoạn đề xuất chính thức** , giọng CTO – ngắn gọn, chuyên nghiệp, phù hợp để bạn gửi vào nhóm **Ban Điều Hành UniPower** hoặc trực tiếp cho **CEO/Chủ tịch** phê duyệt hướng triển khai:
* * *
### **ĐỀ XUẤT HƯỚNG THANH TOÁN CHO HỆ THỐNG UNITAXI**
Hiện nay, POS không còn là giải pháp tối ưu cho hệ thống taxi điện vì chi phí cao, thao tác chậm và khó tích hợp dữ liệu.
Em đề xuất triển khai mô hình **Thanh toán QR + Xuất hóa đơn điện tử tự động** – vừa hiện đại, vừa đúng quy định pháp luật Việt Nam.
**Cấu trúc đề xuất:**
  1. **Thanh toán:** Tích hợp QR động qua **VNPay / MoMo / ZaloPay** – khách quét QR trực tiếp trên app tài xế hoặc app khách hàng.


  2. **Xuất hóa đơn hợp lệ:** Kết nối API với **MISA meInvoice** hoặc **Viettel Invoice** để tự động phát hành hóa đơn điện tử sau mỗi giao dịch.


  3. **Hiệu quả:**
     * Tuân thủ đầy đủ Nghị định 123/2020/NĐ-CP và Thông tư 78/2021/TT-BTC.
     * Tiết kiệm chi phí phần cứng POS và nhân sự xử lý hóa đơn.
     * Giao dịch nhanh, minh bạch và dễ kiểm toán.
     * Dễ mở rộng sang logistic, thuê xe, và dịch vụ doanh nghiệp.


> 👉 Mô hình này đang được Grab, Be và Gojek áp dụng trong giai đoạn chuyển đổi sang hóa đơn điện tử toàn diện, nên hoàn toàn khả thi cho UniPower triển khai trong tháng này.
* * *
Bạn có muốn mình viết thêm **phiên bản rút gọn 3 câu** để bạn đăng trực tiếp vào nhóm Zalo (giọng nói thân mật nhưng vẫn rõ vai trò lãnh đạo kỹ thuật) không?
Rất tốt — đây là phần bạn nên nắm thật chắc khi nói chuyện với CEO, kế toán trưởng, hoặc đối tác ngân hàng.
Dưới đây là bản **phân tích chi tiết, có thể dùng cho trình bày chính thức hoặc gửi lên Ban Điều Hành** :
* * *
## **Mô hình thanh toán QR + hóa đơn điện tử toàn diện**
### (Grab, Be, Gojek và xu hướng pháp lý tại Việt Nam)
* * *
### **1. Bối cảnh chuyển đổi toàn ngành**
Từ **01/07/2022** , toàn bộ doanh nghiệp tại Việt Nam **bắt buộc phải sử dụng hóa đơn điện tử có mã của cơ quan thuế** (Nghị định 123/2020/NĐ-CP & Thông tư 78/2021/TT-BTC).
Các nền tảng gọi xe như **Grab, Be, Gojek** đã buộc phải **chuyển sang mô hình tích hợp trực tiếp API với nhà cung cấp hóa đơn điện tử** để đảm bảo:
  * Mỗi cuốc xe đều được ghi nhận là **giao dịch có mã định danh thuế** ;


  * **Không cần xuất hóa đơn thủ công** ;


  * **Hóa đơn được phát hành tự động** ngay sau thanh toán.


* * *
### **2. Cấu trúc hệ thống (mô hình chuẩn)**
Mô hình này gồm **3 tầng logic** hoạt động liền mạch, không cần POS vật lý:
### **Tầng 1 – Thanh toán**
  * Người dùng chọn hình thức thanh toán: **QR động / Ví điện tử / Thẻ liên kết**.


  * Hệ thống thanh toán trung gian (VNPay, MoMo, ZaloPay, OnePay, Payoo, v.v.) xử lý và gửi xác nhận **Payment Success**.


  * Tiền được chuyển trực tiếp về **tài khoản doanh nghiệp** qua kênh NAPAS.


### **Tầng 2 – Hóa đơn điện tử**
  * Ngay khi giao dịch thành công, **API của nhà cung cấp hóa đơn (MISA, Viettel, VNPT)** được gọi.


  * Dữ liệu chuyến đi (tên tài xế, quãng đường, giá, thuế, phương thức thanh toán) được đẩy lên hệ thống hóa đơn điện tử.


  * Hóa đơn điện tử được:
    * Ký số bằng chứng thư số của UniPower,
    * Cấp mã xác thực bởi Tổng cục Thuế,
    * Gửi ngay cho khách qua email hoặc link tra cứu.


### **Tầng 3 – Đối soát & báo cáo**
  * Hệ thống tự động ghi nhận và đối soát giao dịch theo ngày / tài xế / phương thức thanh toán.


  * Dữ liệu được xuất định kỳ cho phòng kế toán, đảm bảo **khớp sổ ngân hàng – doanh thu – hóa đơn**.


* * *
### **3. Lý do Grab, Be, Gojek chọn mô hình này**
|                     |
| Tiêu chí            | POS truyền thống              | QR + eInvoice                      |
|---------------------|-------------------------------|------------------------------------|
| Tốc độ xử lý        | Chậm (2–3 bước nhập tay)      | Tự động, gần như tức thời          |
| Chi phí             | Cao (máy, phí giao dịch 1–2%) | Thấp hơn 60–70%                    |
| Tính hợp pháp       | Hóa đơn thủ công / rời rạc    | Hóa đơn điện tử hợp lệ, có mã thuế |
| Kiểm toán & kế toán | Khó đối soát                  | Tự động khớp doanh thu – hóa đơn   |
| Mở rộng quy mô      | Giới hạn theo thiết bị POS    | Toàn quốc, không giới hạn          |
| Khả năng tích hợp   | Hạn chế                       | API mở, tích hợp đa nền tảng       |


> 🔸 Grab hiện dùng VNPay QR + MISA meInvoice,
> 🔸 Be dùng **Payoo + Viettel Invoice** ,
> 🔸 Gojek dùng **OnePay + VNPT Invoice**.
* * *
### **4. Lợi ích khi UniPower áp dụng mô hình này**
  * **Tuân thủ tuyệt đối pháp luật Việt Nam** về thuế, kế toán và hóa đơn.


  * **Giảm chi phí vận hành POS** (mỗi máy POS có thể tốn 300k–500k/tháng).


  * **Tăng tốc thanh toán** , khách hàng không phải chờ xử lý hoặc ký tay.


  * **Đồng bộ hóa dữ liệu doanh thu** , phục vụ phân tích hành vi khách hàng, báo cáo thuế và KPI tài xế.


  * **Tạo lợi thế cạnh tranh** : UniTaxi trở thành nền tảng đầu tiên “chạy điện – không tiền mặt – hóa đơn tự động”.


* * *
### **5. Kết luận và đề xuất triển khai**
> 🔹 Giai đoạn 1: Tích hợp thanh toán QR động (VNPay / MoMo) trên app tài xế và khách hàng.
> 🔹 Giai đoạn 2: Kết nối API hóa đơn điện tử với MISA hoặc Viettel.
> 🔹 Giai đoạn 3: Tự động hóa báo cáo thuế và đối soát doanh thu.
Mô hình này không chỉ hiện đại và tiết kiệm, mà còn **đặt UniPower vào cùng tiêu chuẩn vận hành với Grab, Be, Gojek** , đảm bảo khả năng mở rộng và kiểm toán minh bạch.
* * *
Bạn có muốn mình **viết lại phần này thành một slide trình bày nội bộ** (chuẩn định dạng CEO briefing, 1 trang A4, gọn – đẹp – có bullet) để bạn gửi trong nhóm quản trị hoặc trình cho hội đồng không?
--- **Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
