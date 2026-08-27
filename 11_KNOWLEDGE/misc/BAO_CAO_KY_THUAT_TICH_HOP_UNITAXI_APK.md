---
title: BAO CAO KY THUAT TICH HOP UNITAXI APK
tags: [misc]
type: document
source: 11_KNOWLEDGE/misc
---



# **BÁO CÁO KỸ THUẬT – TÍCH HỢP UNITAXI (APK)**
Triển khai Hệ Điều Hành Vận Hành UniPower (3N: Nhàn – Nhanh – Nhạy)**
 **Dành cho CEO – CTO – Ban Điều Hành UniPower**
* * *
# **I. EXECUTIVE SUMMARY**
UniTaxi (Rider App + Driver App) vận hành trên **Wooberly backend** , đang kết nối với:
  * hệ thống điều phối chuyến (Wooberly),


  * hệ thống xe – tài xế – doanh thu của UniPower,


  * hạ tầng trạm sạc **iSAC** ,


  * đối soát – kế toán – hóa đơn qua **MISA AMIS**.


**Mục tiêu dự án AMIS:**
  1. Đưa toàn bộ dữ liệu & quy trình UniTaxi → **Hệ điều hành vận hành thống nhất (AMIS)**.


  2. Tự động hóa 60–70% quy trình vận hành (onboarding, cuốc xe, tài chính, bảo trì, trạm sạc).


  3. Giảm tải thủ công, tăng tốc đối soát, nâng cấp khả năng mở rộng lên 2.000–10.000 xe.


**Đánh giá kỹ thuật: khả thi 95%** nếu đảm bảo:
  * Chuẩn hóa **Data Contract Wooberly → AMIS → iSAC**


  * Xây lớp tích hợp **Integration Layer (API Gateway + Message Queue + ETL)**


  * Tạo **Master Data Management (MDM)** cho tài xế – xe – cuốc – trạm iSAC


  * Thiết kế **Dashboard vận hành realtime UniTaxi**


* * *
# **II. KIỂM TRA TÍNH KHẢ THI KỸ THUẬT**
## **1\. Nguồn dữ liệu cần tích hợp từ UniTaxi (Wooberly backend)**
### **A. Dữ liệu từ Rider App (khách hàng)**
|            |
| **Nhóm**   | **Trường chính**                                                    | **Mức độ**  |
|------------|---------------------------------------------------------------------|-------------|
| Cuốc xe    | trip_id, customer_id, start_time, end_time, route, distance, status | Bắt buộc    |
| Thanh toán | amount, method, transaction_id, captured_status                     | Bắt buộc    |
| Phản hồi   | rating, complaint_code                                              | Khuyến nghị |


* * *
### **B. Dữ liệu từ Driver App (tài xế)**
|           |
| **Nhóm**  | **Trường chính**                                   | **Mức độ** |
|-----------|----------------------------------------------------|------------|
| Tài xế    | driver_id, license, contract_type, status          | Bắt buộc   |
| Xe        | vehicle_id, battery_level, odometer, health_status | Bắt buộc   |
| Hoạt động | online, offline, busy, idle, trip_assigned         | Bắt buộc   |


* * *
### **C. Dữ liệu từ iSAC (trạm sạc & phiên sạc)**
|               |
| **Nhóm**      | **Trường chính**                                        | **Mục đích**          |
|---------------|---------------------------------------------------------|-----------------------|
| Trạm sạc      | station_id, charger_id, status, error_code              | Giám sát vận hành     |
| Phiên sạc     | session_id, vehicle_id, kWh, cost, start_time, end_time | Đối soát chi phí      |
| Doanh thu sạc | amount, tax, reconciled_flag                            | Đẩy sang AMIS Finance |


* * *
## **2\. Tính khả thi kết nối AMIS**
**Cách tích hợp khả thi:**
  * REST API 2 chiều


  * Webhook: TripStatusUpdated, PaymentCaptured, ChargerStatusChanged


  * Message Queue (Kafka / RabbitMQ): xử lý giờ cao điểm


  * ETL batch cuối ngày: reconciliation


**Rủi ro & giải pháp**
|                                                                    |
| **Rủi ro**                                                         | **Giải pháp**                   |
|--------------------------------------------------------------------|---------------------------------|
| Data Wooberly không thống nhất                                     | Data Contract + MDM             |
| API bị nghẽn giờ cao điểm                                          | Queue + Cache Layer             |
| Trùng lặp sự kiện                                                  | Idempotent API + Event Sourcing |
| Chênh lệch doanh thu giữa Wooberly – cổng thanh toán – iSAC – AMIS | Reconciliation pipeline         |


* * *
# **III. KIẾN TRÚC KỸ THUẬT UNI-TAXI → AMIS**
## **1\. Kiến trúc tổng thể**
```
    Rider App (Wooberly)
    Driver App (Wooberly)
               ↓
           Wooberly Backend
               ↓
      Integration Layer (API Gateway + MQ + ETL)
               ↓
              AMIS
     (CRM • HRM • Finance • Workflow • Dashboard)
    
    iSAC → Integration Layer → AMIS (song song)
```
* * *
## **2\. Luồng dữ liệu theo nhóm**
### **A. Luồng cuốc xe (Trip Flow)**
Nguồn: **Wooberly** → Đích: **AMIS Workflow + AMIS Finance**
**Sự kiện bắt buộc:**
  * TripCreated


  * DriverAssigned


  * TripStart


  * TripEnd


  * PaymentCaptured


**Mục tiêu vận hành:**
  * CEO biết số cuốc theo giờ


  * CFO biết doanh thu theo trạng thái


  * Ops phát hiện điểm nghẽn (tài xế, khu vực, ứng dụng)


* * *
### **B. Luồng xe điện (EV Operations)**
Nguồn: Driver App → Wooberly → AMIS
**Dữ liệu cần:**
  * battery_level


  * last_charge


  * predicted_range


  * health_status


**Ứng dụng:**
  * Cảnh báo pin thấp


  * Tự động tạo ticket bảo trì


  * Phân bổ xe – tài xế – tuyến theo pin


* * *
### **C. Luồng trạm sạc (iSAC)**
Nguồn: iSAC → Integration Layer → AMIS
**Sự kiện:**
  * ChargerStatusChanged


  * SessionStart / SessionEnd


  * SessionRevenue


  * ChargerOffline


**Ứng dụng:**
  * Cảnh báo realtime


  * Đối soát doanh thu sạc


  * Tính EV cost per trip


* * *
# **IV. ROADMAP TRIỂN KHAI 12 THÁNG (UNI-TAXI + iSAC + AMIS)**
## **Giai đoạn 0 — 0 đến 4 tuần**
  * Xây **Data Contract** : trip / driver / vehicle / station / charger / session


  * Chuẩn hóa schema trong Wooberly + iSAC


  * Thiết lập Integration Layer


* * *
## **Giai đoạn 1 — 1 đến 3 tháng**
  * Kết nối 3 luồng cốt lõi: **Trip – Revenue – Driver**


  * Tạo Dashboard **UniTaxi Realtime**


  * Đối soát doanh thu cơ bản


* * *
## **Giai đoạn 2 — 3 đến 6 tháng**
  * Tự động hóa onboarding tài xế


  * Tự động hóa reconciliation Wooberly – iSAC – AMIS – cổng thanh toán


  * Tự động ticket bảo trì xe


* * *
## **Giai đoạn 3 — 6 đến 12 tháng**
  * Tích hợp CRM – HRM – Finance đầy đủ


  * Chuẩn hóa vòng đời tài xế & xe


  * Mở rộng sang tỉnh/thành mới


* * *
# **V. KPI GIÁM SÁT**
## **A. KPI vận hành**
  * Trip Success Rate ≥ **94%**


  * Cuốc lỗi do app < **1%**


  * Time-to-assign < **6 giây**


  * Driver Online Peak ≥ **70%**


## **B. KPI tài chính**
  * Revenue reconciliation accuracy ≥ **99%**


  * Revenue leakage giảm ≥ **30%**


## **C. KPI đội xe EV**
  * Vehicle readiness ≥ **90%**


  * Pin < 20% → cảnh báo trong **10 giây**


  * Thời gian xử lý sự cố xe < **2 giờ**


* * *
# **VI. KẾT LUẬN CHO CEO & CTO**
## **1\. Mức khả thi kỹ thuật: ~95%**
## **2\. Hạng mục bắt buộc (phê duyệt ngay)**
  * Chuẩn hóa dữ liệu Wooberly + iSAC (Data Contract + MDM)


  * Xây Integration Layer (API Gateway + Queue + ETL)


  * MDM: driver – vehicle – trip – station – charger – session


  * Ký Data Contract giữa UniTaxi – iSAC – AMIS


## **3\. Lợi ích dự án**
  * Giảm ~60% lỗi vận hành


  * Rút ngắn 40–50% thời gian xử lý thủ công


  * Đối soát doanh thu nhanh & chính xác


  * Giảm 20–30% chi phí vận hành đội xe


  * Mở rộng lên 2.000–10.000 xe mà không thay core


  * Chuẩn hóa pháp lý hoàn toàn theo VN


* * *
\--- **Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
