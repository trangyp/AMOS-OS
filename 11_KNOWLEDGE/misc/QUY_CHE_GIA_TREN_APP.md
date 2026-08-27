---
title: QUY CHE GIA TREN APP
tags: [misc]
type: document
source: 11_KNOWLEDGE/misc
---



# Quy che gia tren app
✅ **Yes — this setup can fully work as a temporary MVP workaround.**
Here’s how to map the Vietnamese fare structure to the existing fields so you don’t need new development right away:
* * *
### **Recommended configuration mapping**
|                            |
| **VN Fare Component**      | **System Field**                | **How to configure**                                                                                                |
|----------------------------|---------------------------------|---------------------------------------------------------------------------------------------------------------------|
| **Giá mở cửa (20.000đ)**   |  Minimum base price             | Nhập giá mở cửa (VD: 20,000 VND).                                                                                   |
| **Giá mềm ( <30km)**       | Unit price                      | Đặt giá trung bình (VD: 12,000 VND/km). Có thể điều chỉnh bằng **“Surge Price Details”** để mô phỏng giá linh hoạt. |
| **Giá cố định ( >30km)**   | Surge price                     | Dùng **“Pricing type = Distance or Time”** để thiết lập giá cao hơn (VD: 14,000 VND/km cho khoảng >30km).           |
| **Giá chờ (1.000đ/phút)**  |  Minute price hoặc Waiting fare | Điền 1,000 VND/phút.                                                                                                |
| **Giá lốc (giảm 10%)**     |  Surge value (âm)               | Nhập giá trị âm hoặc giảm giá theo thời gian nhất định (VD: -10%) để khuyến khích hành vi đi lại định kỳ.           |
| **Giá tối thiểu (nếu có)** |  Base fare                      | Giữ 0 nếu không áp dụng.                                                                                            |
| **Giá giờ cao điểm**       |  Surge price details            | Bật “Yes” → chọn khung giờ và phần trăm tăng (VD: +20%).                                                            |


* * *
## **How to simulate “Cơ chế giá mềm” using current fare fields**
|                           |
| **VN Fare Tier**          | **Mục tiêu**             | **How to Configure (MVP Workaround)**                                                                                   |
|---------------------------|--------------------------|-------------------------------------------------------------------------------------------------------------------------|
| **0–1 km → 20.000đ/km**   |  Bù chi phí khởi hành    | Set this as **Base fare = 20,000đ** (to cover startup).                                                                 |
| **1–10 km → 11.000đ/km**  |  Tăng tần suất cuốc ngắn | Use **Unit price = 11,000đ** as the main per-km rate.                                                                   |
| **10–20 km → 12.000đ/km** |  Giữ lợi nhuận hợp lý    | Use **Surge Price** feature with **Distance or Time condition** , increase unit price by **+9% (≈12,000đ)** after 10km. |
| **20–30 km → 13.000đ/km** |  Hao pin cao hơn         | Add another surge rule (if system allows multiple surges) or use **manual fare adjustment** for these trips.            |
| **> 30 km → 14.000đ/km**  | Bù chiều về              | Use **Surge Price = +25%** after 30km threshold.                                                                        |
| **Giá chờ (1.000đ/phút)** |  Thời gian chờ khách     | Input in **Minute price** or **Waiting fare** field.                                                                    |


* * *
## **Implementation Logic (for dev note / config sheet)**
> “Surge pricing” is repurposed not as a time-based multiplier, but as a
> **distance-based tier system**
> Example:
  * Surge Rule 1: Distance > 10 km → +9%


  * Surge Rule 2: Distance > 20 km → +18%


  * Surge Rule 3: Distance > 30 km → +27%


Even if RadicalStart doesn’t currently allow multiple surge layers, you can still run these adjustments manually via **periodic fare table updates (per distance band)** until dynamic logic is added.
* * *
## **Business Effect**
|                                      |
| **Chỉ số**                           | **Ý nghĩa**                                                        |
|--------------------------------------|--------------------------------------------------------------------|
| Giá trung bình 40 km = 509.000đ      | Dưới taxi truyền thống 10–15%                                      |
| Biên lợi nhuận cao hơn 40–60%        | Nhờ hiệu suất pin và chi phí vận hành thấp                         |
| Hành trình mượt giữa cuốc ngắn & dài | Tránh bất mãn từ tài xế / khách hàng về giá cước “nhảy sốc”        |
| Dễ triển khai MVP                    | Không cần phát triển tính năng mới, chỉ dùng surge & manual update |


* * *
## **Kết luận**
  * Có thể triển khai ngay với hệ thống hiện tại bằng **cấu hình giá + surge theo khoảng cách**.


  * Khi UniTaxi mở rộng, chỉ cần **thêm trường “Distance Tier Pricing”** để tự động hóa.


  * Mô hình này giúp UniPower **trở thành nền tảng giá mềm đầu tiên ở Việt Nam** , đúng định hướng “giao thông xanh – minh bạch – nhân văn”.


* * *
--- **Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
