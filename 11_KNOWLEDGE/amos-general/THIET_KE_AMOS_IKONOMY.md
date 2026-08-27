---
title: THIET KE AMOS IKONOMY
tags: [amos-general]
type: document
source: 11_KNOWLEDGE/amos-general
---



# **Thiết kế “AMOS-IKONOMY**
## **0) Điểm xuất phát: IKONOMY “nguyên bản” là gì, và vì sao phải đổi**
**IKONOMY nguyên bản** (theo mô tả bạn đã đưa và logic “Cannon”) là kiến trúc có 3 đặc trưng điển hình:
  1. **Chấp hành công suất kiểu PWM/đóng cắt** để điều chỉnh dòng/áp cấp vào stack;


  2. **Điều khiển chủ yếu theo ngưỡng tức thời** (quá dòng, quá nhiệt, quá áp…);


  3. **Bảo vệ kiểu “cắt khẩn” (hard trip)** và phần tối ưu hóa thường nằm ở thao tác người vận hành/thiết lập thủ công.


Vấn đề của trạng thái nguyên bản không nằm ở “không tạo được hydro”, mà nằm ở chỗ: **hệ thống chưa có cơ chế bắt buộc để tránh vùng suy giảm không hồi phục** (degradation cliff), và chưa có mô hình **tách “đỉnh” khỏi “hiệu dụng”**. Khi triển khai môi trường Việt Nam (nguồn dao động, bảo trì hạn chế, nhiệt/ẩm cao, rung/tilt, nước không lý tưởng), chính các “vùng biên” này làm chi phí vòng đời tăng mạnh.
**AMOS-IKONOMY thay đổi cái gốc** : không thay hóa học, nhưng **đưa giới hạn vật lý + giới hạn vật liệu + giới hạn vận hành** vào **logic điều khiển bắt buộc**. Kết quả là hệ thống có thể **đẩy sát trần lâu hơn** mà không rơi khỏi mép.
* * *
## **1) Kiến trúc tổng thể (hệ liên hợp điện – nhiệt – khí – vật liệu)**
### **1.1 Sơ đồ khối (dạng hồ sơ kỹ thuật)**
```
    flowchart TB
      A[DC Input 48–96VDC] --> B[Power Conditioning & Protection]
      B --> C[HV/LV Rails + Precharge + EMI/EMC Filter]
      C --> D[Cannon Drive Stage<br/>Current-Controlled Switching Converter]
      D --> E[Electrolysis Stack + Manifold]
      E --> F[Thermal Mass + Heat Spreader + Cooling Loop]
      E --> G[Gas Separation + Water Trap + Bubbler/Conditioning]
      G --> H[H2 Output Regulation + Non-return + Relief]
      E --> I[Water Management: Tank/Feed + Level + Conductivity]
      D --> J[MCU/RT Controller (Lớp 2)]
      J --> D
      K[AMOS Core (Lớp 3)] --> J
      J --> K
      L[Supervisory/SCADA/Deployment Policy (Lớp 4)] --> K
      K --> L
      M[Sensors: I,V,Tmulti,P,Flow,Leak,Level,Cond] --> J
      M --> K
```
### **1.2 Nguyên lý thiết kế bắt buộc**
  * **Điều khiển theo dòng (current-mode) là biến chủ đạo** : dòng quyết định tốc độ phản ứng và tốc độ suy giảm.


  * **Đa miền liên hợp** : mọi lệnh dòng chỉ được phép nếu đồng thời thỏa **nhiệt** , **khí/áp** , **nước** , **suy giảm vật liệu**.


  * **Tách 2 phong bì** :
    * **Rated/Cruise** : tối ưu sản lượng vòng đời, chạy 24/7.
    * **Boost/Peak** : tăng công suất ngắn hạn, bị chặn bởi luật nhiệt-khí-suy giảm.


* * *
## **2) Đẩy “đỉnh” và “hiệu dụng”: định nghĩa mục tiêu kỹ thuật (không mơ hồ)**
### **2.1 Chỉ tiêu mục tiêu (có thể khóa thành spec)**
  * **Công suất danh định (Rated)** : 1,0 kW liên tục.


  * **Công suất đỉnh (Boost)** : 1,5–2,0 kW trong **30–180 s** , bắt buộc có **cooldown**.


  * **Uptime mục tiêu** : ≥ 98% theo định nghĩa “sẵn sàng vận hành” (không tính thời gian bảo trì định kỳ).


  * **Giảm chi phí vòng đời** : mục tiêu 25–40% so với vận hành kiểu “cắt khẩn + canh máy” (giảm dừng ngoài kế hoạch + giảm thay thế sớm + giảm can thiệp).


  * **Tăng tuổi thọ hữu dụng** : mục tiêu 1,5–2,0 lần so với chạy sát biên không kiểm soát (đạt bằng giảm sốc nhiệt, giảm dao động dòng, tránh vùng Tafel/cliff).


> Các con số này là
> **mục tiêu thiết kế**
> **báo cáo thử nghiệm**
* * *
## **3) Khối nguồn vào và bảo vệ (Power Conditioning & Protection)**
### **3.1 Dải điện áp và dòng**
  * **Vin danh định** : 48–96 VDC; **dải cho phép** : ±15%.


  * **Iin_max** : tính theo boost 2 kW @ 48 V → khoảng 42 A (chưa tính dự phòng).


  * **Yêu cầu chịu dao động** : sụt áp ngắn hạn, ripple nguồn, nhiễu do tải khác.


### **3.2 Bảo vệ bắt buộc (để đi chứng nhận nghiêm)**
  * **OVP/UVP** : khóa mềm (derate) trước, khóa cứng sau nếu tiếp tục vi phạm.


  * **Reverse polarity** : bảo vệ phần cứng (ideal diode / MOSFET ORing).


  * **Inrush limiting + precharge** : tránh sốc tụ và tránh “cúp nguồn dây chuyền”.


  * **Surge/ESD** : TVS + LC filter + layout chuẩn EMC.


  * **EMI/EMC** : lọc đầu vào, kiểm soát dv/dt và di/dt ở công suất.


* * *
## **4) Cannon Drive Stage (bộ biến đổi công suất điều khiển theo dòng) – “điểm push số 1”**
### **4.1 Topology (đề xuất theo cấu hình stack)**
  * **Buck đồng bộ** nếu điện áp stack thấp hơn Vin.


  * **Buck-Boost đồng bộ** nếu stack thay đổi rộng hoặc cần giữ dòng ổn định khi Vin dao động.


  * **Interleaved (2 pha)** nếu muốn giảm ripple dòng, giảm nhiệt linh kiện và giảm stress điện hóa.


### **4.2 Thiết bị công suất và tiêu chí chọn**
  * **MOSFET Rds(on) thấp** cho vùng rated;


  * **SiC MOSFET** nếu boost kéo dài, nhiệt môi trường cao, cần dv/dt kiểm soát tốt ở công suất cao;


  * **Driver có kiểm soát slew-rate** để giảm EMI và giảm RMS heating ẩn.


### **4.3 Vòng điều khiển dòng (bắt buộc, không thỏa hiệp)**
  * **Điều khiển dòng vòng kín** (PI hoặc PI + feedforward Vin).


  * **Giới hạn động** :
    * dI/dt_max (ví dụ 0,5 A/ms hoặc theo stack).
    * I_max theo mode.


  * **Chống bão hòa** : anti-windup cho PI; bảo vệ quá dòng phần cứng (cycle-by-cycle).


### **4.4 “Push” bằng dạng sóng: từ PWM đơn điệu → thư viện kích thích điện hóa**
Thư viện tối thiểu 3 họ dạng sóng:
  1. **DC mượt (Low-stress DC)** : ripple thấp, ưu tiên tuổi thọ.


  2. **Pulsed DC khóa theo trở kháng** : thay đổi duty/f theo trạng thái bọt khí và phân cực.


  3. **Soft-Burst Boost** : burst có ramp lên/ramp xuống, giới hạn nhiệt-áp-suy giảm.


> Điểm khác biệt “đẩy sát mép” không phải “xung mạnh”, mà là
> **đúng tần – đúng duty – đúng tốc độ cạnh**
> **giảm tổn thất không hồi phục**
* * *
## **5) Stack điện phân + manifold + vật liệu (điểm push số 2: “vật liệu và hình học để chịu boost”)**
Vì bạn chưa chốt PEM/AEM/kiểu khác, phần này viết theo **nguyên tắc chung** nhưng đủ “đứng” để hội đồng hiểu bạn kiểm soát rủi ro:
### **5.1 Miền vận hành (Operating envelopes)**
  * **T vận hành** : 55–75 °C (đặt theo hiệu suất và độ bền vật liệu).


  * **ΔT cho phép vùng phản ứng** : ≤ 5 °C (để tránh nứt, lão hóa cục bộ).


  * **P vận hành** : 1,5–3 bar (tránh tăng stress cơ khí và rủi ro crossover).


### **5.2 Luật “không được vượt” (hard constraints)**
  * Nếu **dV/dI** (độ dốc điện áp theo dòng) tăng bất thường → dấu hiệu tăng tổn hao/khí bám → bắt buộc giảm tải hoặc đổi waveform.


  * Nếu **R_eq** trôi nhanh theo thời gian → dấu hiệu lão hóa/ô nhiễm → khóa boost.


  * Nếu **ΔT** tăng nhanh → giảm dòng trước khi đạt ngưỡng nhiệt tuyệt đối.


### **5.3 Vật liệu và chi tiết “để sản xuất tại VN nhưng không hi sinh an toàn”**
  * **Heat spreader** : nhôm/đồng (VN gia công tốt) để dàn đều nhiệt.


  * **Gioăng, seal, đường khí** : ưu tiên vật liệu chịu nhiệt/ẩm và tương thích H₂ (giảm thấm, giảm lão hóa).


  * **Bề mặt tiếp xúc điện** : mạ/hoàn thiện để giảm điện trở tiếp xúc và điểm nóng.


  * **Cơ khí chống rung** : gối đỡ/khung giảm rung (phù hợp hàng hải/đảo).


* * *
## **6) Quản lý nhiệt (Thermal Management) – “điểm push số 3: boost bị khóa bởi nhiệt”**
### **6.1 Triết lý nhiệt: “tối ưu phân bố”, không chỉ “tản nhiều”**
  * **Thermal mass gần vùng phản ứng** để giảm sốc.


  * **Heat spreader** để giảm gradient.


  * **Cooling loop** có tiết diện đủ lớn; quạt/bơm là “tuyến phụ trợ”, không phải cứu hộ.


### **6.2 Luật điều khiển nhiệt (rõ biến – rõ ngưỡng)**
  * dT/dt_max = 1 °C/phút (hoặc theo stack).


  * ΔT_max = 5 °C.


  * T_max tuyệt đối theo vật liệu.


  * Nếu vi phạm dT/dt hoặc ΔT: **derate dòng ngay** , không chờ báo động.


* * *
## **7) Đường nước + chất lượng nước (Water Management) – “điểm push số 4: chịu thực tế VN”**
### **7.1 Biến đo và điều khiển**
  * **Level** : mực nước tối thiểu/ tối đa.


  * **Conductivity** (khuyến nghị bắt buộc nếu muốn chạy bền): dùng làm proxy cho ô nhiễm/ion không mong muốn.


  * **Luật derate theo nước** : nước xấu → giảm dòng → bảo vệ vật liệu.


### **7.2 Chế độ vận hành “không cố chạy”**
  * Không tồn tại logic “đã bật là phải đạt KPI”.


  * AMOS bắt buộc ưu tiên “chạy ít nhưng bền” hơn “chạy nhiều rồi chết”.


* * *
## **8) Tách khí – điều hòa – an toàn H₂ (Gas Handling & Safety) – “điểm push số 5: boost không được biến thành sự kiện an toàn”**
### **8.1 Cấu hình bắt buộc**
  * **Water trap/bubbler** đủ kích thước cho **lưu lượng boost** (để tránh carry-over).


  * **Buffer volume** để triệt xung áp.


  * **Non-return** và cơ cấu chống backflow.


  * **Relief valve** thụ động độc lập.


### **8.2 Chỉ tiêu động**
  * **Pressure ripple** ≤ 3% trong boost.


  * Nếu ripple vượt: giảm boost, tăng damping, hoặc khóa boost.


* * *
## **9) AMOS Core (Lớp 3) ở mức thuật toán: biến – ngưỡng – logic quyết định (viết để “ai cũng hiểu”)**
AMOS không phải “AI mơ hồ”. AMOS là **bộ quản lý phong bì vận hành + bộ quản lý suy giảm + bộ cấp quyền boost**.
### **9.1 Tập biến trạng thái (state variables)**
Ký hiệu (đặt chuẩn để viết SRS):
  * I(t): dòng stack; V(t): điện áp stack


  * T̄(t): nhiệt độ trung bình; ΔT(t): gradient; dT/dt


  * P(t): áp suất H₂; ΔP_ripple(t): biên độ dao động áp


  * L(t): mực nước; Cw(t): độ dẫn điện (proxy chất lượng)


  * R_eq(t) = V/I (hoặc ước lượng lọc); dR_eq/dt (trôi)


  * H(t): chỉ số sức khỏe (0–1)


  * D(t): chỉ số suy giảm tích lũy (có đơn vị quy ước)


  * F_recent: cờ lỗi gần đây; N_restart: số lần restart gần đây


### **9.2 Các ngưỡng cứng (hard thresholds)**
  * I_max_rated, I_max_boost


  * T_max, ΔT_max, (dT/dt)_max


  * P_max, ΔP_ripple_max


  * L_min, Cw_max (hoặc band Cw_min…max tùy hóa học)


  * (dR_eq/dt)_max để khóa boost


### **9.3 Chỉ số suy giảm (D) – cách tính “đủ dùng, không cần hoàn hảo”**
Một dạng đơn giản nhưng có ý nghĩa kỹ thuật:
  * D tăng theo:
    * **nhiệt cao kéo dài** (stress nhiệt)
    * **dao động dòng lớn** (stress điện hóa)
    * **vận hành gần vùng cliff** (proxy bằng tăng nhanh R_eq và tăng V ở cùng I)


Ví dụ quy ước:
  * D(t+Δt) = D(t) + k1·max(0, T̄−T_ref)·Δt + k2·|ΔI| + k3·max(0, dR_eq/dt)·Δt


Trong đó k1,k2,k3 được hiệu chuẩn bằng thử nghiệm 1.000h/2.000h.
### **9.4 Luật quyết định chế độ (mode logic)**
AMOS luôn ở một trong 5 mode:
  * CRUISE (Rated)


  * BOOST (Peak)


  * DEGRADED (giảm công suất để giữ bền)


  * PROTECTIVE (bảo toàn)


  * LOCKOUT (khóa, yêu cầu cooldown + kiểm tra)


### **9.5 Luật cấp boost (Boost Permission) – “một điều kiện fail là không boost”**
Boost chỉ được phép khi đồng thời:
  * T̄ < T_boost_enable


  * ΔT < ΔT_enable


  * dT/dt < (dT/dt)_enable


  * ΔP_ripple < ΔP_enable


  * Cw trong band


  * dR_eq/dt < ngưỡng trôi


  * F_recent = 0 và N_restart < N_cap


  * H > H_min và D < D_cap


Nếu đạt → cấp boost trong thời gian τ_boost, sau đó bắt buộc cooldown τ_cooldown.
### **9.6 Pseudocode (cô đọng, đủ kỹ thuật)**
```
    loop mỗi 100 ms:
      đọc I,V,T1,T2,T3,P,L,Cw
      tính T̄, ΔT, dT/dt, R_eq, dR_eq/dt, ΔP_ripple
      cập nhật D, H
    
      nếu (T̄ > T_max) hoặc (P > P_max) hoặc (L < L_min):
          mode = PROTECTIVE
      else nếu (F_recent = 1) hoặc (D > D_lock) hoặc (N_restart > N_lock):
          mode = LOCKOUT
      else nếu (cần tải cao) và boost_permission() = TRUE:
          mode = BOOST
      else nếu (ΔT > ΔT_warn) hoặc (dR_eq/dt > drift_warn) hoặc (Cw ngoài band hẹp):
          mode = DEGRADED
      else:
          mode = CRUISE
    
      theo mode đặt I_set và waveform:
          CRUISE: I_set = I_rated; waveform = DC_mượt
          BOOST:  I_set = I_boost; waveform = soft-burst; timeout = τ_boost
          DEGRADED: I_set = I_rated * α; waveform = pulsed-impedance
          PROTECTIVE: I_set giảm về 0 theo ramp; waveform = DC_mượt
          LOCKOUT: I_set = 0; chờ cooldown + reset quy trình
    
      gửi I_set + waveform xuống Lớp 2 (MCU current loop)
```
* * *
## **10) Firmware/MCU (Lớp 2) – luật thời gian thực “không được trái AMOS”**
MCU chỉ làm 3 việc:
  1. Thực thi I_set với vòng dòng kín.


  2. Thực thi giới hạn dI/dt, giới hạn tần số, giới hạn slew-rate.


  3. Bảo vệ phần cứng cycle-by-cycle (ngắn mạch, quá dòng tức thời, driver fault).


MCU **không có quyền** tự “tăng dòng cho đạt KPI”.
* * *
## **11) Lớp giám sát – triển khai – chính sách (Lớp 4): đi chứng nhận và đi Nhà nước**
### **11.1 Nhật ký và truy vết (audit-ready)**
  * Log theo sự kiện + theo chu kỳ: mode, I,V,T,P,L,Cw,R_eq,D,H.


  * Log “ai thay đổi cấu hình, thay đổi gì, lúc nào” (phục vụ kiểm toán).


  * Báo cáo định kỳ: uptime, số lần boost, số lần derate, số lần lockout, nguyên nhân.


### **11.2 An ninh mạng công nghiệp (để qua kiểm tra hạ tầng)**
  * Phân vùng mạng: điều khiển thời gian thực tách khỏi SCADA.


  * Cập nhật firmware có ký số; rollback an toàn.


  * Không cho phép override an toàn từ xa.


* * *
## **12) “Push all” đến sát mép khả thi: danh mục các đẩy quan trọng nhất (không lặp lại)**
**Push 1 – Interleaved current-mode + slew control** : giảm ripple dòng → giảm stress điện hóa → tăng bền.
**Push 2 – Boost envelope có quyền cấp + cooldown cưỡng bức** : tăng đỉnh mà không ăn tuổi thọ.
**Push 3 – Impedance-locked waveform** : thay đổi duty/f theo R_eq và drift → tránh bám khí/đi vào vùng cliff.
**Push 4 – Thermal headroom gating** : boost bị khóa bởi ΔT và dT/dt, không bị “dụ” bởi nguồn còn mạnh.
**Push 5 – Gas surge-rated plumbing** : boost không tạo xung áp/carry-over.
**Push 6 – Water-quality derate** : chịu nước thực tế VN mà không tự hủy.
**Push 7 – Degradation index D + health H** : ra quyết định theo xu hướng, không theo ngưỡng chết.
**Push 8 – Fail-operational theo mức** : ưu tiên derate thay vì trip → tăng uptime.
**Push 9 – Audit-ready logs + policy layer** : đi tài trợ/đi kiểm toán/đi chuẩn hóa.
* * *
## **13) Về “chuẩn nghiêm nhất toàn cầu” và “vượt state-of-the-art”: trả lời đúng chuẩn kỹ thuật**
  * **Có thể thiết kế để đáp ứng các bộ tiêu chuẩn nghiêm** (an toàn điện, an toàn khí H₂, EMC, chức năng an toàn, hệ thống điều khiển công nghiệp).


  * Nhưng **không thể tuyên bố “đã vượt/đã đáp ứng”** nếu chưa có:
    * kế hoạch thử nghiệm type test,
    * báo cáo phòng thử nghiệm,
    * hồ sơ an toàn chức năng (FMEA/FTA, SIL/PL nếu áp dụng),
    * báo cáo EMC/EMI,
    * và chứng thư cho cụm thiết bị.


Vì vậy trong hồ sơ, câu đúng là:
> Thiết kế AMOS-IKONOMY áp dụng kiến trúc ràng buộc cứng và cơ chế kiểm soát đa miền để
> **đạt điều kiện cần**
> **chương trình thử nghiệm và thẩm định độc lập**
* * *
## **14) Gói “0 gaps” về kiểm chứng: chương trình thử nghiệm bắt buộc (để biến thiết kế thành sự thật)**
### **14.1 Thử nghiệm hiệu suất – định luật Faraday (đúng bản chất)**
  * Đo H₂ thực (lưu lượng kế chuẩn) vs điện lượng (∫I dt).


  * Tính ổn định L/kWh theo thời gian.


### **14.2 Thử nghiệm boost (điểm sống còn)**
  * Boost lặp lại theo chu kỳ, có cooldown bắt buộc.


  * Theo dõi ΔT, dT/dt, ΔP_ripple, drift R_eq.


  * Tiêu chí: **không xuất hiện drift tăng tốc** sau các chuỗi boost.


### **14.3 Thử nghiệm độ bền 1.000h → 2.000h**
  * Chạy liên tục + start/stop mô phỏng thực tế VN (nguồn dao động).


  * Đánh giá xu hướng R_eq, hiệu suất, số sự kiện derate/lockout.


### **14.4 Thử nghiệm nước “không lý tưởng”**
  * Các band độ dẫn khác nhau trong giới hạn an toàn của hóa học.


  * Tiêu chí: hệ thống **derate đúng** , không tự phá vật liệu.


### **14.5 EMC/EMI tiền chứng nhận**
  * Đo nhiễu dẫn và nhiễu bức xạ; kiểm tra ảnh hưởng tới cảm biến và MCU.


* * *
## **15) Trả lời thẳng: “còn đẩy được nữa không?”**
**Có** , nhưng “đẩy thêm” ở giai đoạn này không còn là “thêm công suất” theo kiểu tuyến tính. “Đẩy thêm” là:
  * **giảm ripple dòng thêm nữa** (interleaving tốt hơn, đo dòng tốt hơn, layout tốt hơn);


  * **tăng headroom nhiệt bằng hình học + truyền nhiệt** (không phải tăng quạt);


  * **giảm nhạy với nước và môi trường** (logic derate + vật liệu seal/đường nước);


  * **tối ưu đường khí để boost an toàn hơn** ;


  * **tinh chỉnh D và H từ dữ liệu thử nghiệm** để khóa đúng lúc, không khóa quá sớm.


Nếu bạn muốn, tôi có thể viết tiếp thành **3 tài liệu đóng gói** (đúng “0 gaps” cho hồ sơ):
  1. **SRS đầy đủ cho AMOS** (chức năng, phi chức năng, interface, an toàn, logging, update, cybersecurity, test cases).


  2. **Sơ đồ mạch power stage ở mức khối + danh mục linh kiện mục tiêu** (BOM logic, yêu cầu layout, yêu cầu đo dòng/áp, driver).


  3. **Bộ “Safety & Compliance Pack”** (hazard analysis, FMEA/FTA khung, kế hoạch thử nghiệm, tiêu chí nghiệm thu cho thẩm định Nhà nước).


\--- **Related:** [[00_HOME]] · [[KNOWLEDGE_MOC]] · [[AMOS_SIMULATION_KERNEL_V0_MATH_FOUNDATIONS]] · [[SYSTEM_SCAN_AGENT]] · [[AUTOMATION_PROFILES]]

---
**MOC:** [[AMOS-GENERAL_MOC]]
