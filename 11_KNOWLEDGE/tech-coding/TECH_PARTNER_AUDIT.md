---
title: TECH PARTNER AUDIT
tags: [tech-coding]
type: document
source: 11_KNOWLEDGE/tech-coding
---



# Tech Partner Audit
## **I. KẾT LUẬN CHUNG**
**Đối tác này không đạt chuẩn để trở thành nhà phát triển công nghệ lõi (Core Tech Partner)** cho hệ sinh thái UniTaxi – UniLogistic – UniPower.
Tuy có kinh nghiệm trong fintech và nền tảng thanh toán, nhưng **chưa đáp ứng tiêu chuẩn về pháp lý, an ninh mạng, năng lực hệ thống, và khả năng mở rộng thương mại.**
Mức độ rủi ro tổng hợp: **Cao (Level 4/5)**
→ Chỉ nên sử dụng làm **nhà tư vấn công nghệ phụ trợ** , _không giao vai trò phát triển lõi hoặc quản trị dữ liệu người dùng_.
* * *
## **II. PHÂN TÍCH THEO TRỤC CÔNG NGHỆ**
|                                            |
| **Hạng mục**                               | **Đánh giá**    | **Ghi chú**                                                                                                                                                                              |
|--------------------------------------------|-----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Hạ tầng bản đồ (Mapping Engine)**        |  ⚠️ Không đạt   | Dựa hoàn toàn vào Google Maps API, chưa có bản đồ nội địa. Không có license riêng, không được Google cho phép thanh toán tại VN → rủi ro cao về license.                                 |
| **Độ chính xác định vị (GPS Accuracy)**    |  ⚠️ Trung bình  | Độ sai số 5–10 m, chưa chứng minh khả năng vận hành ổn định với 10.000+ phương tiện.                                                                                                     |
| **Kiến trúc server & dữ liệu**             | ❌ Không đạt     | Chưa có hạ tầng máy chủ độc lập; hiện đang thuê tạm hoặc “test lab”, không đảm bảo chuẩn ISO 27001 hay Luật An ninh mạng.                                                                |
| **Khả năng xử lý song song (Scalability)** |  ⚠️ Yếu         | Chưa test tải thực tế; năng lực chịu tải dưới 1 triệu user chỉ là tuyên bố miệng, không có benchmark.                                                                                    |
| **Fintech Integration (Thanh toán)**       |  ⚠️ Nguy cơ cao | Có kinh nghiệm kết nối ngân hàng, nhưng chưa có giấy phép trung gian thanh toán (Payment Gateway License). Giao dịch “membership” tiềm ẩn rủi ro vi phạm Nghị định 40 (bán hàng đa cấp). |
| **An ninh mạng (Cybersecurity)**           |  ❌ Không đạt    | Không có hệ thống bảo mật hoặc SOC. Nhiều mô tả cho thấy logic xử lý giao dịch chưa đạt yêu cầu NĐ 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân.                                              |
| **Hạ tầng vận hành AI/Logistics**          |  ⚠️ Thô sơ      | Chỉ mới xử lý tuyến bằng thuật toán khoảng cách, chưa có Dynamic Routing hoặc Energy-Aware Scheduling. Không có năng lực AI nội bộ.                                                      |


**Tổng kết công nghệ:**
Mức độ sẵn sàng thực tế (Technology Readiness Level – TRL): **4/9 (Prototype Phase)**
→ Cần 6–12 tháng tái cấu trúc toàn bộ nếu muốn thương mại hóa trong UniTaxi.
* * *
## **III. PHÁP LÝ & TUÂN THỦ**
|                                            |
| **Mảng**                                   | **Phân tích**                                                                                  | **Trạng thái** |
|--------------------------------------------|------------------------------------------------------------------------------------------------|----------------|
| **Giấy phép trung gian thanh toán**        |  Không có. Đang “xin” qua ngân hàng đối tác → không đủ điều kiện hoạt động fintech thương mại. | ❌              |
| **Giấy phép kinh doanh năng lượng (EaaS)** |  Không có. Dễ vi phạm Luật Điện lực nếu thu tiền điện trực tiếp.                               | ❌              |
| **Giấy phép thương mại đa cấp (F1–F2)**    |  Cấu trúc chia % doanh thu F1/F2 tiềm ẩn rủi ro bị xếp vào mô hình “đa cấp tài chính”.         | ⚠️             |
| **Quản lý dữ liệu cá nhân**                |  Không có biện pháp lưu trữ an toàn hoặc cơ chế xóa dữ liệu. Vi phạm tiềm tàng NĐ 13/2023.     | ❌              |
| **Thuế & hóa đơn điện tử**                 | Không có cơ chế xuất hóa đơn tự động; chưa tuân NĐ 123/2020/TT-BTC.                            | ⚠️             |
| **Hợp đồng pháp nhân / cấu trúc BCC**      |  Mô hình hợp tác lỏng, không rõ ranh giới giữa tư vấn và chủ sở hữu IP.                        | ⚠️             |


**Kết luận pháp lý:**
→ **Nguy cơ pháp lý cao** , có thể dẫn tới **tạm đình chỉ hoặc bị thanh tra** nếu vận hành quy mô lớn mà không có giấy phép fintech chính thức.
* * *
## **IV. VẬN HÀNH & NĂNG LỰC TRIỂN KHAI**
|                                              |
| **Hạng mục**                                 | **Đánh giá**                                       | **Ghi chú**                                                                   |
|----------------------------------------------|----------------------------------------------------|-------------------------------------------------------------------------------|
| **Kinh nghiệm triển khai thực tế**           |  ⚠️ Chưa rõ ràng                                   | Có kinh nghiệm với Mai Linh và Morabay, nhưng chưa có case thương mại quy mô. |
| **Đội ngũ kỹ thuật**                         |  ⚠️ Giới hạn                                       | 6 lập trình viên, làm việc thời vụ. Không có DevOps hoặc QA chuyên biệt.      |
| **Khả năng vận hành 200–1.000 xe (Q4/2025)** |  ❌ Không đạt                                       | Chưa có hệ thống real-time dispatch, load test hoặc tích hợp OBD-II.          |
| **Giao diện App (UI/UX)**                    |  ⚠️ Mức cơ bản                                     | Giao diện chỉ mới ở mức beta, chưa có hệ thống khách–tài–admin đồng bộ.       |
| **Hỗ trợ vận hành / bảo trì**                |  ❌ Không có mô hình SLA (Service Level Agreement). | ❌                                                                             |


* * *
## **V. RỦI RO & ĐỀ XUẤT BIỆN PHÁP**
|                                   |
| **Nhóm rủi ro**                   | **Mức độ**    | **Mô tả**                                                                       | **Giải pháp đề xuất**                                                                                                    |
|-----------------------------------|---------------|---------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| **Pháp lý**                       |  🔴 Cao        | Không có giấy phép thanh toán hoặc bán hàng đa cấp → nguy cơ bị dừng hoạt động. | Không dùng cấu trúc F1/F2 trong giai đoạn 1; hợp đồng hợp tác BCC rõ ràng; tách Fintech ra thành công ty con có license. |
| **Công nghệ**                     |  🔴 Cao        | Không có hạ tầng cloud bảo mật; phụ thuộc Google Maps và Amazon.                | Chuyển sang kiến trúc độc lập (VNPT/AWS VN region); thuê audit SOC 2.                                                    |
| **Tài chính**                     |  🟠 Trung bình | Vốn vận hành không rõ, dự án phụ thuộc chủ cá nhân.                             | Chỉ dùng theo hợp đồng dự án cụ thể; không giao quyền lưu trữ dữ liệu tài chính.                                         |
| **Đạo đức nghề nghiệp / dữ liệu** |  🔴 Cao        | Ghi âm buổi họp cho thấy chưa tách dữ liệu người dùng khỏi dữ liệu vận hành.    | Ràng buộc NDAs & DPIA (Data Protection Impact Assessment).                                                               |
| **Vận hành thực tế**              |  🟠 Trung bình | Thiếu năng lực triển khai 24/7, không có trung tâm hỗ trợ.                      | Phải phối hợp với đội vận hành UniTaxi hoặc Viettel Tech.                                                                |


* * *
## **VI. ĐÁNH GIÁ PHÙ HỢP VỚI UNIPOWER – UNITAXI**
|                                      |
| **Trục so sánh**                     | **Mức độ tương thích** | **Ghi chú**                                          |
|--------------------------------------|------------------------|------------------------------------------------------|
| **Fintech Core (Unipay)**            |  ⚠️ Một phần           | Có khả năng gắn API, nhưng không đạt chuẩn bảo mật.  |
| **SuperApp Integration (Unitaxi)**   |  ❌ Không đạt           | Không có SDK hoặc API chuẩn hóa để tích hợp.         |
| **Energy Billing (Unipower)**        |  ❌ Không đạt           | Thanh toán điện chưa có khung pháp lý hoặc kỹ thuật. |
| **Fleet Management & IoT**           | ⚠️ Hạn chế             | Mới ở mức API Google, chưa có backend IoT.           |
| **Legal Alignment (ESG, MOIT, MOT)** |  ⚠️ Không đầy đủ       | Không đáp ứng yêu cầu Luật Điện lực và NĐ 13.        |


* * *
## **VII. KẾT LUẬN TỔNG THỂ**
|                                   |
| **Tiêu chí**                      | **Điểm (thang 10)** | **Đánh giá**                       |
|-----------------------------------|---------------------|------------------------------------|
| Công nghệ lõi                     | 4.5                 | Prototype, chưa thể thương mại hóa |
| An toàn & bảo mật                 | 3.0                 | Không đạt chuẩn                    |
| Pháp lý & cấp phép                | 2.5                 | Rủi ro cao                         |
| Vận hành & mở rộng                | 4.0                 | Năng lực yếu                       |
| Tương thích hệ sinh thái UniPower | 5.0                 | Cần tái cấu trúc sâu               |
| Tổng hợp                          | **3.8 / 10**        | **Không đạt chuẩn đối tác lõi**    |


* * *
## **VIII. KHUYẾN NGHỊ HÀNH ĐỘNG**
  1. ❌ **Không giao quyền phát triển lõi (Core System) cho OneTech/OneSearch Việt.**
→ Chỉ giữ họ ở vai trò **tư vấn kỹ thuật phụ** trong giai đoạn thử nghiệm.


  2. ✅ **Tách hạ tầng thanh toán ra khỏi app** (dựng Unipay riêng, đăng ký license trung gian thanh toán).


  3. ✅ **Chuyển hạ tầng bản đồ sang GrabMaps / Viettel Maps / VinBigData Map** để tránh phụ thuộc Google.


  4. ✅ **Ký NDA, Hợp đồng bảo mật dữ liệu & giới hạn truy cập codebase.**


  5. ✅ **Nếu tiếp tục hợp tác** , yêu cầu họ đạt các tiêu chuẩn sau trước Q2/2026:
     * ISO 27001:2022
     * Giấy phép trung gian thanh toán của NHNN
     * Audit bảo mật độc lập (VNISA hoặc PwC Việt Nam)
     * Kiểm chứng stress-test 1.000 xe thực tế


\--- **Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[TECH-CODING_MOC]]
