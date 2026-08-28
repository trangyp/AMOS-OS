---
title: EMAIL MESSAGE YEU CAU BAN GIAO
tags: [misc, reference, general, canon/knowledge]
type: document
source: 11_KNOWLEDGE/misc
rscf:
  state: DERIVED
  claim_class: DERIVED
  provenance: AMOS_corpus
  scope: AMOS_general
---


# EMAIL / MESSAGE YÊU CẦU BÀN GIAO
* * *
## 1\. QUYỀN TRUY CẬP & TÀI KHOẢN
Vui lòng cung cấp đầy đủ:
**Danh sách + quyền truy cập thực tế:**
  * Server (IP, user, quyền root/sudo)


  * Cloud (AWS/GCP/Azure – account + IAM)


  * Database (host, user admin, quyền truy cập)


  * Firewall / network (login + quyền cấu hình)


  * Domain + DNS + SSL (nơi quản lý + login)


  * Git repo (link + quyền owner)


  * CI/CD (Jenkins/Gitlab CI…)


  * App Store + Google Play (account + quyền)


  * Vendor accounts (DC, payment, SMS, email…)


**Yêu cầu thêm:**
  * Danh sách ai đang giữ quyền admin


  * MFA / OTP đang thuộc về ai


  * Tài khoản dùng chung (nếu có)


* * *
## 2\. HẠ TẦNG & HỢP ĐỒNG
**Danh sách hạ tầng:**
  * Server vật lý (DC nào, rack nào)


  * Cloud (service nào đang dùng)


  * Network (leased line, VPN, firewall)


**Với mỗi nhà cung cấp:**
  * Tên vendor


  * Hợp đồng + ngày hết hạn


  * Công nợ hiện tại


  * SLA cam kết


  * Điều kiện tạm ngưng/cắt dịch vụ


* * *
## 3\. DANH SÁCH HỆ THỐNG (SYSTEM INVENTORY)
Vui lòng cung cấp bảng gồm:
  * Tên hệ thống (app khách, app tài xế, backend…)


  * Mô tả chức năng chính


  * Môi trường chạy (server/cloud nào)


  * Database sử dụng


  * Người phụ trách chính


  * Mức độ quan trọng (critical / high / normal)


* * *
## 4\. KIẾN TRÚC & LUỒNG HỆ THỐNG
  * Sơ đồ tổng thể (system architecture)


  * Sơ đồ network (IP, kết nối giữa các hệ)


  * Luồng chính:
    * booking → dispatch → tài xế → thanh toán


  * Danh sách tất cả tích hợp bên thứ ba


**Yêu cầu:**
  * Chỉ rõ hệ thống nào phụ thuộc hệ thống nào


* * *
## 5\. BACKUP & KHÔI PHỤC
  * Danh sách hệ thống đang được backup


  * Loại backup (full/incremental)


  * Tần suất (daily/weekly…)


  * Nơi lưu (server/cloud/offsite)


**Bắt buộc cung cấp:**
  * Quy trình restore từng hệ thống


  * Lần test restore gần nhất (ngày + kết quả)


* * *
## 6\. CODE & TRIỂN KHAI
**Source code:**
  * Danh sách repo đầy đủ


  * Repo nào là production


**Deploy:**
  * Quy trình deploy backend (step-by-step)


  * Quy trình deploy mobile (Android/iOS)


  * CI/CD pipeline (nếu có)


**Mobile:**
  * Keystore Android


  * Certificate iOS


  * Quyền ký app


* * *
## 7\. DATABASE & DỮ LIỆU
  * Danh sách database (tên, loại, dung lượng)


  * Database nào là production


  * Có replication không


**Dữ liệu chính:**
  * Khách hàng


  * Tài xế


  * Giao dịch


  * Thanh toán


**Yêu cầu:**
  * Cách đối soát dữ liệu (nếu có)


* * *
## 8\. VẬN HÀNH (OPS)
  * Hệ thống monitoring đang dùng (tool gì)


  * Dashboard (link)


  * Alert (gửi cho ai, qua đâu)


**Sự cố:**
  * Quy trình xử lý incident


  * Danh sách sự cố lớn 6–12 tháng:
    * nguyên nhân
    * cách xử lý


**Runbook:**
  * Restart system


  * Xử lý lỗi phổ biến


* * *
## 9\. TÍCH HỢP BÊN THỨ BA
Cho mỗi tích hợp:
  * Tên đối tác (payment, SMS, map…)


  * Mục đích sử dụng


  * API endpoint / tài liệu


  * API key / credential


  * SLA


  * Người phụ trách


* * *
## 10\. BẢO MẬT
  * Firewall rule hiện tại


  * Danh sách port mở


  * VPN (cách truy cập)


  * Patch hệ điều hành


**Secret:**
  * Nơi lưu password / API key


  * Danh sách key quan trọng


  * SSL certificate (file + private key)


* * *
## 11\. NHÂN SỰ & PHỤ THUỘC
  * Sơ đồ team tech


  * Ai phụ trách từng hệ thống


  * Hệ thống nào chỉ 1 người biết


**Tài liệu:**
  * SOP


  * Wiki


  * Hướng dẫn vận hành


* * *
## 12\. CHI PHÍ & THANH TOÁN
  * Chi phí DC / cloud


  * Chi phí license


  * Chi phí vendor


**Yêu cầu:**
  * Chi phí theo tháng


  * Các khoản sắp đến hạn


* * *
# YÊU CẦU CÁCH BÀN GIAO
  * Gửi tài liệu dạng file (Excel/Doc)


  * Cấp quyền truy cập thực tế


  * Tổ chức session walkthrough (3–5 ngày)


  * Ghi lại video nếu có thể


* * *
# 10 ĐIỂM PHẢI XÁC NHẬN TRONG BUỔI BÀN GIAO
  1. Ai giữ toàn bộ quyền admin?


  2. Hệ thống nào quan trọng nhất?


  3. Backup có restore được không?


  4. Nếu DC down → xử lý thế nào?


  5. Thanh toán phụ thuộc hệ nào?


  6. Có vendor nào giữ code/data không?


  7. Có hệ thống nào không có owner?


  8. Có rủi ro bị cắt dịch vụ không?


  9. Có lỗi lớn nào chưa fix?


  10. Có phụ thuộc cá nhân không?


* * *
\--- **Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[MISC_MOC]]
